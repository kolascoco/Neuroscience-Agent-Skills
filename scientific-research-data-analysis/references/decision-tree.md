# Decision Tree

Use only the branches relevant to the task. Wording below defaults to
electrophysiology/neuroimaging vocabulary — treat each term as one example of
a general question (e.g. "epoch" asks what your time segment is, "channel"
asks what your measurement unit within a sample is) and substitute your
field's equivalent where it differs.

## Scientific Target *(Theorist, checked by Statistician)*

1. Purpose: exact reproduction, sensitivity analysis, exploratory screen,
   confirmation, or theory update?
2. Primary estimand: effect size, prediction, coupling magnitude, preferred
   phase, group contrast, trajectory, classification accuracy, or another
   defined quantity?
3. Analysis class: descriptive, exploratory inferential, confirmatory, or
   diagnostic only?
4. Interpretation rule: what wording is allowed if results are positive, null,
   fragile, or blocked?

## Data And Sample *(Scout)*

5. Dataset/version: immutable paths, hashes, download/access date, license.
6. Unit of analysis: subject, trial, event, observation, image, sample, epoch,
   cluster, patient, session.
7. Primary keys: columns that uniquely identify each physical unit.
8. Inclusion/exclusion: subject, trial/event, channel/feature, site/batch;
   timing of exclusions relative to outcome access.
9. Missingness: omit, model, impute, reject, or report-only; minimum support.

## Preprocessing And Features *(Scout gathers, Analyst implements)*

10. Preprocessing inherited from source or newly applied? Reference/filtering,
    normalization, artifact rejection, feature scaling, alignment.
11. Timing/window ownership and boundary rules.
12. Feature construction: source variables, transforms, units, sign conventions.
13. Any data-adaptive selection? If yes, freeze train/test separation and
    propagate selection into nulls or label as selection-informed.

## Statistics *(Statistician)*

14. Model/statistic: formula, family, random effects/clustering, robust SE,
    permutation statistic, or descriptive summary.
15. Null/exchangeability: what is shuffled/rotated/flipped, within which block,
    synchronized across which dimensions, how many draws, seed.
16. Multiplicity family: exact list of tests/maps/endpoints; correction level.
17. Direction/tail/threshold: one-sided or two-sided, cluster-forming threshold,
    ROI threshold, decision alpha.
18. Power/precision/SESOI: smallest effect of interest and expected uncertainty.

## Outputs *(Analyst produces, Orchestrator reviews)*

19. Required tables, arrays, figures, manifests, logs, tests, and summaries.
20. Figure conventions: scales, labels, significance markers, null maps.
21. Compute plan: benchmark, cache keys, runtime gates, HPC/local execution.
22. Review plan: statistician, adversary (including reproducibility), theory
    update, manuscript readiness.
