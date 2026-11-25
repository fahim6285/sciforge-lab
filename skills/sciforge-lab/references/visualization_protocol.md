# Scientific visualization protocol

## Choose the right chart
- Line: ordered temporal/numeric trajectories where connecting points has meaning.
- Scatter: paired observations, with overlaid fits only when they were calculated and labeled.
- Bar: categorical aggregates with declared statistic and sample size as relevant.
- Histogram/density: distributions; disclose bins and scale.
- Box/violin: distributions with enough points; note sample size and outliers.
- Heatmap: matrix with defined rows, columns, value scale and interpretable colorbar; use consistent units.
- Confusion matrix: specify class order and raw vs normalized entries; derive from actual labels/predictions.
- Error bars: state SD/SE/CI and method, per-group n, and only draw when computed from data.

## Figure rules
- Source of every series identified, axes with labels and physical units, correct numeric scale, consistent units and category ordering.
- Do not crop zero baselines in bar charts if it distorts interpretation. Zoomed line/scatter axes may be valid but must be explicit and not misleading.
- Use readable ticks and legends; export vector PDF/SVG when requested, and high-resolution PNG suitable for print.
- Choose colorblind-safe palettes where feasible, and distinguish groups by line style/marker too. Avoid arbitrary rainbow heatmaps for ordinal quantities.
- No smoothing, interpolation, synthetic uncertainty, synthetic points or cosmetic trend manipulation without methodological disclosure.
- Place table captions above and figure captions below if the user's publication format requests it.
- In output check: reopen files or inspect render, verify no clipped labels, crowded legends, accidental truncation or inconsistent values.
- Prefer separate figures rather than dense subplots unless comparisons clearly benefit from multipanel layout.

## Plot CLI
`scripts/plot_from_csv.py` provides a lightweight reproducible renderer for line/scatter/bar/histogram using actual CSV fields. It handles a single y-series, optional error column and neutral default styling. For complex plots, build a task-specific script, not a misleading generic chart.

