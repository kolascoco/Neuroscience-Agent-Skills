# Analysis Artifact Contract

Use a stable folder such as `analyses/H-YYYY-NNN/` or a project-equivalent
analysis root.

## Required Files

- `plan.md`: purpose, estimand, sample, preprocessing, model/statistic, null,
  multiplicity, controls, outputs, compute plan, interpretation limits.
- `config.json`: machine-readable frozen choices and source paths/hashes.
  Carries the declared `instruments` array (see
  [instrument-validation.md](instrument-validation.md)) and a `family` block
  (see Analysis Families below), always present; null-valued for a
  standalone analysis.
- `code/`: implementation, validators, tests.
- `tests/`: automated tests for `code/`.
- `results/`: arrays, tables, figures, controls, summaries, manifests.
- `log.md`: timestamps, commands, wall time, approvals, failures, fixes.
- `result_manifest.json`: hashes for result/provenance files.
- `gate_status.json`: records gate outcomes and carries the `instrument_status`
  array defined in [instrument-validation.md](instrument-validation.md). Keys
  beyond `instrument_status` are permitted and unvalidated. Unlike
  `config.json`, this file is mutable: it records results, not frozen
  decisions.
- `final_report.md`: what ran, pass/fail, N/support, effect sizes,
  limitations, and result status (see Result Summary below).
- `ideas.md`: project-level, not per-analysis. Lives at the project root,
  above `analyses/`, not inside this folder (see Project Ideas List below).

All of the above except `ideas.md` are Analyst-authored (see
[soul-roles.md](soul-roles.md)); the Analyst does not certify its own result.

## Canonical Filenames

Unless a path is shown, the filename lives at the analysis folder root.

| Artifact | Canonical filename |
|---|---|
| Data-contract audit (Scout) | `input_audit.md` / `input_audit.json` |
| Statistician pre-analysis review | `statistician_review.md` |
| Statistician post-result review | `statistician_post_result_review.md` |
| Adversarial review (Adversary) | `results/adversarial_review.md` |
| Freeze record | `freeze_manifest.json` |
| Gate outcomes and instrument status | `gate_status.json` |
| Result hashes | `result_manifest.json` |
| Final narrative | `final_report.md` |
| Theory-update entry | `lab_journal_entry.md` |
| Theory document | `theory.md`, project root, above `analyses/` |

Two rules make the table binding:

- A review that ran under a different filename did not run, because it
  cannot be found.
- Where one analysis needs several instances of an artifact — per stage, per
  amendment — the canonical stem takes a suffix
  (`adversarial_review_<stage>.md`), never a new stem.

## Analysis Families

`config.json` gains a `family` block: `family_id`, `parent_analysis`,
`varies`.

- An analysis that changes a parameter of an earlier analysis addressing the
  same question sets `parent_analysis` to that earlier analysis's id, shares
  its `family_id`, and names the changed parameters in `varies`.
- Every family member's `final_report.md` records the family size at write
  time: configuration k of n tried.

Analysis ids are unique: `init_analysis.py` exits non-zero on a duplicate id
and on any id whose ordinal prefix is already taken by a sibling directory.
An id is never reused; a variant of an earlier analysis takes its own new id
and records that earlier analysis as its `parent_analysis` above, rather than
reusing the parent's id.

The interpretation consequence — when a family member may be labeled
confirmatory versus selection-informed — is written in
[interpretation-rules.md](interpretation-rules.md); this file specifies only
the `config.json` schema.

## Project Ideas List

One file per project, `ideas.md`, at the project root, above `analyses/`.
Required, not optional. A per-analysis ideas file is rejected: fragmenting
the list across analysis folders destroys the accumulation that gives it
value.

**Purpose.** Creative output degrades under the conditions that demand it, so
the file decouples idea generation from idea selection in time.

**Relation to the theory document.** `theory.md` states the direction the
project is committed to; `ideas.md` lists the directions an analysis could go
instead. An entry moves from `ideas.md` into the theory only on evidence
recorded in an artifact (see [theory-update.md](theory-update.md)).

**Contents.** One line per idea, ranked by expected value, each with a
one-line rationale and a rough cost. An idea names what it would test or
change, not merely a topic. Columns: `Rank`, `Idea`, `Rationale`,
`Rough cost`, `Status`.

**Write triggers.** While discussing results, during analysis, at data
audit, and at theory update.

**Read triggers.** When an analysis stalls, when a method is dropped via the
fallback ladder in [instrument-validation.md](instrument-validation.md), and
at every theory update.

**Status values.** `open`, `in progress`, `done` (naming the analysis id that
took it up), `dropped` (with a reason). An idea is never silently deleted.

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

`final_report.md` states:

- what was run;
- what passed/failed;
- exact N/support;
- effect sizes/intervals/p-values where applicable;
- multiplicity family;
- limitations and residual risks;
- whether the result is descriptive, exploratory, selection-informed,
  confirmatory, falsifying, or diagnostic only.
