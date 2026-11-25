#!/usr/bin/env python3
"""Audit a CSV without modifying it. Standard-library only; not a domain validator."""
import argparse
import csv
import hashlib
import json
import math
from collections import Counter
from pathlib import Path

MISSING = {"", "na", "n/a", "null", "none", "nan"}


def audit(path, key=None):
    src = Path(path)
    if not src.is_file():
        raise ValueError(f"CSV not found: {src}")
    with src.open("rb") as stream:
        checksum = hashlib.sha256(stream.read()).hexdigest()
    with src.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        headers = reader.fieldnames
        if not headers:
            raise ValueError("CSV must have a header row")
        if len(set(headers)) != len(headers):
            raise ValueError("Duplicate CSV column names; repair the source/header")
        if key and key not in headers:
            raise ValueError(f"Duplicate-check key {key!r} not present; fields: {headers}")
        missing = Counter({h: 0 for h in headers})
        finite_numeric = Counter({h: 0 for h in headers})
        nonfinite = Counter({h: 0 for h in headers})
        text_nonmissing = Counter({h: 0 for h in headers})
        sample_values = {h: [] for h in headers}
        keys = Counter()
        total = malformed = 0
        duplicate_full_rows = 0
        rows_seen = set()
        for record in reader:
            total += 1
            if None in record:
                malformed += 1
            signature = tuple(record.get(h) for h in headers)
            if signature in rows_seen:
                duplicate_full_rows += 1
            rows_seen.add(signature)
            if key:
                kval = record.get(key)
                if kval is not None and kval.strip():
                    keys[kval.strip()] += 1
            for col in headers:
                value = record.get(col)
                raw = "" if value is None else value.strip()
                if raw.lower() in MISSING:
                    missing[col] += 1
                    continue
                try:
                    parsed = float(raw)
                except (ValueError, TypeError):
                    text_nonmissing[col] += 1
                    if len(sample_values[col]) < 3 and raw not in sample_values[col]:
                        sample_values[col].append(raw)
                    continue
                if math.isfinite(parsed):
                    finite_numeric[col] += 1
                else:
                    nonfinite[col] += 1
    return {
        "file": str(src), "sha256": checksum, "row_count": total,
        "columns": headers, "malformed_rows": malformed,
        "duplicate_full_rows_including_replicates": duplicate_full_rows,
        "duplicate_key_values": {k: n for k, n in keys.items() if n > 1} if key else None,
        "columns_audit": {h: {
            "missing_cells": missing[h], "finite_numeric_cells": finite_numeric[h],
            "nonfinite_numeric_cells": nonfinite[h], "text_cells": text_nonmissing[h],
            "sample_text_values": sample_values[h],
        } for h in headers},
        "caveat": "Informational syntax audit only; duplicate rows may be legitimate replicates. Data units, scientific bounds and whether a column should be numeric require a user schema.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", help="Input CSV (never modified)")
    parser.add_argument("--key", help="Optional key column for duplicate value checks")
    parser.add_argument("--output", help="JSON report path; prints to terminal regardless")
    args = parser.parse_args()
    result = audit(args.file, args.key)
    result_json = json.dumps(result, indent=2, ensure_ascii=False)
    if args.output:
        dest = Path(args.output)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(result_json + "\n", encoding="utf-8")
    print(result_json)

if __name__ == "__main__":
    main()

