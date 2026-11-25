# Deliverables and handoff

## Standard deliverables depending on request
1. `run.py` / MATLAB `.m` / notebook or tested script; no hidden unverified environment assumptions.
2. `data_dictionary` and an unmodified-source manifest or schema contract.
3. Generated figures in requested formats and a compact tables export, with versioned, descriptive names.
4. `README` with exact commands, required libraries/toolboxes, expected input structure, output locations and actual validation status.
5. Validation summary: source file, row/column counts, missingness, duplication policy, transformations, tests run and any unresolved substantive issues.

## Claim check
Use labels **measured, observed, simulated, analytical, illustrative, calculated, predicted** accurately. Record timestamps/versions for time-varying series. Do not write 'experimentally validated' from example-only tests.

## Naming and packaging
Use file names that reflect task and actual origin. Archive only necessary deliverables; exclude logs with private paths/secrets. Never include credentials or private source files in reusable global templates.

## Example CLI usage
```
python scripts/validate_dataset.py examples/analytic_square.csv --key x --output validation.json
python scripts/plot_from_csv.py examples/analytic_square.csv --x x --y y --kind line --xlabel "x (dimensionless)" --ylabel "y = x² (dimensionless)" --output figure.png
```
These demonstrate the workflow for the mathematical identity y=x², **not scientific experimental findings**.

