# Statistician Review

Use before inference or when reviewing a completed result.

## Pre-Analysis Review

Check:

1. Estimand is clear and matches the theory question.
2. Unit of analysis and dependency structure are modeled correctly.
3. Sample size, support, precision, and SESOI are realistic.
4. Model family/statistic is appropriate for outcome scale and censoring.
5. Null/exchangeability matches the data-generating and selection process.
6. Multiplicity family is complete and correction is aligned to the claim.
7. Tails, thresholds, seeds, and stopping rules are frozen.
8. Missingness/exclusion rules are outcome-blind.
9. Planned controls can detect implementation and null-model failures.

Each finding includes severity, reason, and concrete fix. Write the review to
`statistician_review.md` per the canonical filename table in
[analysis-artifact-contract.md](analysis-artifact-contract.md).

## Post-Result Review

Check exact reporting, assumptions, N at every stage, p-value/interval
calculation, skew/asymmetry diagnostics where relevant, multiplicity wording,
and whether inference exceeded the frozen plan. Write the review to
`statistician_post_result_review.md` per the same table.

A test that returns a constant, a filter that passes or fails everything, an
exactly zero statistic, a perfect metric, or an all-NaN result is treated as
a bug until investigated — see
[instrument-validation.md](instrument-validation.md).

Nulls and failed hypotheses deserve the same precision as positives.
