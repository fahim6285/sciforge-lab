#!/usr/bin/env python3
"""Render one series from a CSV. No synthetic data or hidden resampling."""
import argparse
import csv
import math
from pathlib import Path


def render(args):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    with open(args.file, "r", encoding="utf-8-sig", newline="") as stream:
        rd = csv.DictReader(stream)
        cols = rd.fieldnames or []
        for name in [args.x, args.y, args.yerr]:
            if name and name not in cols:
                raise ValueError(f"Column {name!r} not found in {cols}")
        if args.kind != "histogram" and not args.x:
            raise ValueError("--x is required for line/scatter/bar plots")
        raw = list(rd)

    if not raw:
        raise ValueError("No data rows")
    xs, ys, es = [], [], []
    for rowno, r in enumerate(raw, 2):
        if not r.get(args.y):
            raise ValueError(f"Missing y in CSV row {rowno}; fix source or filter explicitly")
        try:
            y = float(r[args.y])
        except ValueError as e:
            raise ValueError(f"Non-numeric y in row {rowno}") from e
        if not math.isfinite(y):
            raise ValueError(f"Nonfinite y in row {rowno}")
        ys.append(y)
        if args.x:
            raw_x = r.get(args.x)
            if raw_x is None or raw_x == "":
                raise ValueError(f"Missing x in row {rowno}")
            try:
                x = float(raw_x)
                if not math.isfinite(x):
                    raise ValueError(f"Nonfinite x in row {rowno}")
            except ValueError:
                x = raw_x  # categorical coordinate
            xs.append(x)
        if args.yerr:
            try:
                v = float(r[args.yerr])
            except (ValueError, TypeError) as e:
                raise ValueError(f"Invalid error magnitude in row {rowno}") from e
            if not math.isfinite(v) or v < 0:
                raise ValueError(f"Error magnitude must be finite/nonnegative, row {rowno}")
            es.append(v)
    if args.kind == "histogram" and args.yerr:
        raise ValueError("Error bars do not apply to a histogram")
    fig, ax = plt.subplots(figsize=(7.5, 4.8), constrained_layout=True)
    if args.kind == "line":
        if args.yerr:
            ax.errorbar(xs, ys, yerr=es, marker="o", linewidth=1.7, capsize=3)
        else:
            ax.plot(xs, ys, marker="o", linewidth=1.7)
    elif args.kind == "scatter":
        if args.yerr:
            ax.errorbar(xs, ys, yerr=es, fmt="o", capsize=3)
        else:
            ax.scatter(xs, ys)
    elif args.kind == "bar":
        ax.bar([str(i) for i in xs], ys, yerr=es if args.yerr else None, capsize=3 if args.yerr else 0)
    elif args.kind == "histogram":
        ax.hist(ys, bins=args.bins)
    if args.title:
        ax.set_title(args.title)
    ax.set_xlabel(args.xlabel or (args.x if args.kind != "histogram" else args.y))
    ax.set_ylabel(args.ylabel or ("Count" if args.kind == "histogram" else args.y))
    ax.grid(True, axis="y", alpha=0.2)
    if args.kind == "bar":
        ax.tick_params(axis="x", labelrotation=40)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.suffix.lower() not in {".png", ".svg", ".pdf"}:
        raise ValueError("Output must end .png, .svg or .pdf")
    fig.savefig(out, dpi=args.dpi)
    plt.close(fig)
    print(f"Saved {out} ({len(ys)} source rows plotted, no point generation or smoothing)")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("file")
    ap.add_argument("--x", help="Column for x coordinates (unused by histogram)")
    ap.add_argument("--y", required=True, help="Column of actual values to plot")
    ap.add_argument("--yerr", help="Column of supplied nonnegative error magnitudes; supply valid uncertainty definition")
    ap.add_argument("--kind", choices=["line", "scatter", "bar", "histogram"], default="line")
    ap.add_argument("--xlabel", help="X-axis label, including units")
    ap.add_argument("--ylabel", help="Y-axis label, including units or uncertainty meaning")
    ap.add_argument("--title", help="Optional chart title")
    ap.add_argument("--bins", type=int, default=12, help="Number of histogram bins")
    ap.add_argument("--dpi", type=int, default=300)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    if args.dpi < 72 or args.dpi > 2400 or args.bins < 1:
        ap.error("--dpi must be 72..2400 and --bins positive")
    render(args)

if __name__ == "__main__":
    main()

