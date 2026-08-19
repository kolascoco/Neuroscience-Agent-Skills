# Interpretation Rules

Use restrained language matched to the design.

## Reporting Posture

- The headline states the worst defensible reading of the data, not the most
  flattering reading the evidence still supports.
- Deviations from the frozen plan are disclosed in the report itself, not
  left for a reader to find by diffing `config.json` against the narrative.
- An analysis tuned after seeing its results is reported as such, with the
  number of configurations tried.
- Messy or inconclusive results are reported as messy or inconclusive, not
  rounded up to a clean finding for readability.

## Labels

These labels classify an *analysis*. The epistemic tiers in
[claim-discipline.md](claim-discipline.md) classify a *statement* made from
one; apply both, since an exploratory analysis can still yield a statement
tiered OBSERVATION.

- **Descriptive:** summarizes observed data; no inferential claim.
- **Exploratory:** inference was run, but the family/question arose within the
  exploration program.
- **Selection-informed:** data-adaptive choice influenced the tested target;
  inference is conditional or diagnostic unless selection is propagated through
  the null.
- **Confirmatory:** frozen before outcome access on an independent or reserved
  confirmation dataset/split.
- **Diagnostic:** influence, QC, sensitivity, or presentation-only; cannot
  authorize exclusion or rescue a claim.

## Analysis Families

A family is declared in `config.json`'s `family` block (`family_id`,
`parent_analysis`, `varies`); see
[analysis-artifact-contract.md](analysis-artifact-contract.md) for the schema.

- A member of a family larger than one is not labeled confirmatory unless the
  whole family was frozen before outcome access.
- Absent that freeze, the family is selection-informed, and the family size at
  write time is reported alongside the result — configuration k of n tried.

## Prohibited Moves

- Do not call a post-hoc sensitivity a replication.
- Do not use selected-subset p-values to improve original evidential status.
- Do not turn subject influence into exclusion unless exclusion was
  outcome-blind and frozen.
- Do not add significance markers to descriptive maps.
- Do not report a metric or phase result without source, transform, unit, and
  frequency/window coordinates where relevant.
- Do not let a later positive rescue an earlier null; create a new analysis.
- Do not report a family member's result without its family size.

## Required Limitation Language

Report the null model, multiplicity family, support thresholds, missingness,
selection status, and any assumptions needed for exchangeability or model
validity.
