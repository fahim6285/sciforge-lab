# Code construction and validation

## Pipeline structure
- CLI or notebook cell with explicit file input and output path; dependencies at top; no hidden external downloads.
- Separate import, schema check, numerical operations, post-processing, metrics and outputs. Small functions with type/shape assumptions and defensible errors.
- Avoid hard-coded machine paths, undocumented file names, unnecessary deep learning frameworks, external personal credentials or private network resources.
- Seed random number generators for stochastic procedures, and record algorithm/library/hardware constraints; deterministic seeds do not guarantee GPU determinism.

## Verification levels
- **Static-reviewed:** syntax/logic inspected, no execution claimed.
- **Smoke-tested:** code runs on analytically known or explicitly dummy inputs; cannot establish performance on real data.
- **Data-executed:** code genuinely executed on the specified dataset, with relevant outputs inspected.
- **Independent-check passed:** direct recomputation, reference solution, unit tests, tolerance checks or cross-environment comparison validates meaningful results.

## Numerical checks
- Always inspect shapes, scales, dtypes, NaN/Inf propagation, precision and significant figures.
- Prefer stable algorithms; benchmark only if timing actually measured with hardware and run settings recorded.
- Check conservation, boundedness, positivity or invariants only when problem statement justifies them.
- For optimizer/model comparisons, normalize dataset, split, compute budget and evaluation criteria before inferring advantage.
- If executing MATLAB on a system without MATLAB: clearly say so; optionally provide compatible alternatives and mark execution status accurately.

## Test plan
- Input absent, empty, malformed header, missing field, nonnumeric value, duplicate key, nonfinite data.
- Known analytic value and boundary cases.
- Output generated, can reopen it, dimensions/series lengths match inputs, and source content preserved.
- Verify whether axis choices and data filtering have scientific implications.

