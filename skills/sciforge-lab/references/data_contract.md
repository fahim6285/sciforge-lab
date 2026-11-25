# Data intake and contract

1. Record each actual source's filename, format, modification/version if available, units, origin and role: observation / simulation / analytical / illustrative.
2. Data schema: field name, unit, type, allowed range/labels if grounded, null policy, key identifiers, temporal resolution, grouping and measurement uncertainty. Do not apply guessed biological/engineering bounds.
3. Check row count, columns, unique keys, duplicates, nulls, ±infinity, invalid date/time, encoding issues and locale-specific decimal separators. Preserve raw files unchanged; save normalized copy separately.
4. Distinguish exact duplicates, repeated measurements, overlapping windows and true replicates; never blindly drop duplicate rows.
5. Align signals and series only with a documented join key and tolerance. Guard against look-ahead leakage and target leakage; split before fitting preprocessing when modeling.
6. Record every transformation in an audit: filtering, imputation, resampling, normalization, unit conversion, outlier rule, joins, sample exclusion, and how many rows each operation changes.
7. If only charts or a summary table are present, do not pretend raw measurements exist. Extraction estimates must be explicitly marked and separately sourced.
8. The bundled CLI `scripts/validate_dataset.py` is CSV-focused and informational; use domain-specific validations and proper parsers for other formats.

## Input questions, only when truly blocking
- What is the actual dataset or file?
- What must be computed or plotted (and from which named columns)?
- Which executable target (Python / MATLAB / Colab) and output format?
If nonessential answers are missing, choose reasonable transparent defaults and deliver a useful partial implementation.

