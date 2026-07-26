# Analysis Artifact Contract

Use a stable folder such as `analyses/H-YYYY-NNN/` or a project-equivalent
analysis root.

## Required Files

- `plan.md`: purpose, estimand, sample, preprocessing, model/statistic, null,
  multiplicity, controls, outputs, compute plan, interpretation limits.
- `config.json`: machine-readable frozen choices and source paths/hashes.
- `code/`: implementation, validators, tests.
- `results/`: arrays, tables, figures, controls, summaries, manifests.
- `log.md`: timestamps, commands, wall time, approvals, failures, fixes.
- `result_manifest.json`: hashes for result/provenance files.
- `summary.md`: what ran, pass/fail, N/support, effect sizes, limitations, and
  result status (see Result Summary below).

All of the above are Analyst-authored (see
[soul-roles.md](soul-roles.md)); the Analyst does not certify its own result.

## Freeze Rule

`plan.md` and `config.json` must exist before outcome inspection. Amendments
after outcome access must be dated, labeled post-hoc, and cannot silently alter
the evidential status of the original analysis.

## Controls

Match controls to the analysis class:

- positive/planted signal control;
- negative or null control;
- boundary/window ownership control;
- duplicate/primary-key control;
- transform/range/unit control;
- cache/hash/provenance control;
- figure rendering/nonblank control when figures are deliverables.

## Result Summary

`summary.md` should state:

- what was run;
- what passed/failed;
- exact N/support;
- effect sizes/intervals/p-values where applicable;
- multiplicity family;
- limitations and residual risks;
- whether the result is descriptive, exploratory, selection-informed,
  confirmatory, falsifying, or diagnostic only.
