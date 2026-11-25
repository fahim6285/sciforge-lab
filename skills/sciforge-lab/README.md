# SciForge Lab by Fahim — Skill-based Scientific Software & Visualization Agent

**Purpose:** A reusable, field-neutral capability for trustworthy scientific computing, data quality checks, tested code and publication-quality figures. **No private user research or previously authored work is included.**

## What is in the package

- `SKILL.md`: agent identity, activation, boundaries, process and mandatory quality gate.
- `references/`: data contracts, execution and tests, visualization, statistics, reproducibility and integrity.
- `scripts/validate_dataset.py`: CSV audit with missing/nonfinite/numeric and duplicate-key checks.
- `scripts/plot_from_csv.py`: generic line/scatter/bar/histogram figure generator.
- `examples/analytic_square.csv`: **analytical-only demonstration**, y=x², for testing; not empirical data.
- `templates/analysis_brief.md`, `templates/source_manifest.csv`, `templates/figure_spec.md`: lightweight reproducibility templates.

## Try it
From this `skills/sciforge-lab/` directory:
```
python scripts/validate_dataset.py examples/analytic_square.csv --key x --output validation.json
python scripts/plot_from_csv.py examples/analytic_square.csv --x x --y y --kind line --output square_example.png --xlabel "x (dimensionless)" --ylabel "y (dimensionless)"
```
Dependencies: validation uses Python standard library; plotting requires `matplotlib` (and standard library). Do not present mathematical demo plots as experimental results.

## Typical agent requests
- Audit this dataset's fields, types, missingness and duplicates, then produce a validation report.
- Convert my MATLAB procedure to Python and show which tests actually passed.
- Read the measured values, build high-resolution line and scatter figures, and provide the scripts.
- Diagnose why two tables and their figures differ; calculate the discrepancy from actual data.
- Create a Colab-friendly, single-cell scientific analysis workflow with deterministic output files.

Version 1.0.0. Creator branding: **by Fahim**. Created without including any prior project datasets, specific research methods/results, medical information or institutional records.

