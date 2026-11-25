# Data analysis and statistics

- State the estimand, sample inclusion, unit of observation, independent variable, outcome, groups and missingness before testing.
- Descriptive statistics: calculate n, mean/median, SD/IQR appropriately; distinguish sample SD (ddof=1) from population SD.
- Choose hypothesis tests from distributional assumptions, pairing, independence and design; adjust for multiple testing where warranted.
- Compute confidence intervals using valid method, sample structure and variance assumptions; p-values only from real calculations, never guessed.
- For cross-validation: report fold design, class stratification, leakage defenses, which values were per-fold, and what was pooled; do not mix original paper baselines with fold-wise comparisons as if equivalent.
- For classification: define confusion matrix layout, precision/recall/F1 averaging, ROC-AUC class handling and threshold; report denominator and sample counts.
- For regression/forecasting: confirm MSE/RMSE/MAE units and transform inversions; evaluate temporal leakage and data split.
- For numerical solvers: record time/space step, stability, iteration tolerance, convergence criterion and independent solution or sensitivity checks.
- Every claim of improvement must specify comparable baseline and recomputed delta, including whether absolute points or relative percent.
- Do not use statistical significance as a proxy for practical significance; show effect magnitude when justified.

