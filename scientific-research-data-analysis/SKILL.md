---
name: scientific-research-data-analysis
description: Govern scientific research data analyses from idea to results. Use when planning, adapting, running, auditing, reproducing, or reporting empirical analyses in any domain, especially when a task involves datasets, hypotheses, preprocessing, exclusions, statistics, null models, permutation tests, reproducibility, provenance, result interpretation, lab journals, or theory updates.
---

# Scientific Research Data Analysis

Use this skill to keep scientific work honest, traceable, and useful. It is
domain-general: load domain-specific skills or documentation when the data type
requires them, but let this skill govern the scientific workflow. Reference-file
examples default to electrophysiology/neuroimaging vocabulary (channel, epoch,
reference/filtering, ROI) — these name the first things to clarify in any
dataset; map each to your field's equivalent unit when it differs.

## Operating Rule

Classify the request before acting.

- **Read-only discussion, brainstorming, or plan sketch:** use a compact
  decision ledger; do not require a full gate.
- **Result-producing work, reproducibility tests, adapted analyses, new nulls,
  p-values, model fitting, or outcome inspection:** the agent establishes the
  facts itself, drafts the complete proposal, and presents it once — the plan,
  every degree of freedom it filled, the rationale for each, and what it left
  open (see
  [references/common-understanding-gate.md](references/common-understanding-gate.md)).
  The user approves, edits, or rejects the proposal in one pass. Do not write
  analysis code or inspect outcomes until the plan/config/data contract are
  frozen and the user explicitly confirms them.
- **Two categories still block; the agent stops and waits for confirmation
  before proceeding:**
  - **The scientific target.** Hypothesis, estimand, and null model are
    confirmed before any test runs.
  - **Expensive or irreversible compute.** First real-data run, compute over
    30 minutes, or a confirmatory one-shot run, presented with analysis id,
    dataset, operation, and time estimate.

Facts are discovered from files; decisions are asked of the user.
A default may be filled, never silently. Every filled degree of freedom
appears in the proposal as a named assumption with its rationale, in a form
the user can reject.

[references/claim-discipline.md](references/claim-discipline.md) applies as a
standing rule at every step of this workflow, not as a step of its own.

## Workflow

Each step names the role that owns it (defined in
[references/soul-roles.md](references/soul-roles.md)). Read that file now, not
only "when role separation matters" — in nearly every real session you are the
only agent present, and that file explains how to honor role separation alone,
including the one step below where independent execution is required rather
than advisory.

1. **Orient and scope.** *Role: Orchestrator.* Identify whether the task is
   planning, data audit, implementation, statistical review, adversarial
   review, theory update, or writing.
2. **Build shared understanding.** *Role: Orchestrator drafts and defends the
   proposal, drawing on Theorist (estimand/hypothesis) and Statistician
   (design/null) judgment.* For result-producing work, follow
   [references/common-understanding-gate.md](references/common-understanding-gate.md)
   and the relevant branches of [references/decision-tree.md](references/decision-tree.md).
3. **Audit the data contract.** *Role: Scout.* Before analysis, read
   [references/data-contract.md](references/data-contract.md). Stop on
   ambiguous identifiers, unclear units, trial/event misalignment, undocumented
   preprocessing, or unresolved missingness.
4. **Freeze artifacts.** *Role: Analyst writes; Orchestrator confirms the
   freeze.* Create or update `plan.md` and config before outcome inspection. Use
   [references/analysis-artifact-contract.md](references/analysis-artifact-contract.md).
5. **Validate design.** *Role: Statistician.* For statistical plans or
   inference, read [references/statistician-review.md](references/statistician-review.md).
6. **Implement minimally.** *Role: Analyst.* Before trusting any instrument
   used for the first time in this project, complete
   [references/instrument-validation.md](references/instrument-validation.md).
   Keep code inside the analysis folder. Add positive, negative/null,
   boundary, and provenance controls before trusting results. Cache expensive
   intermediates with input/config/code hashes.
7. **Audit independently.** *Role: Adversary — independent execution is
   required whenever your platform can provide it, not merely preferred.* After
   results, use [references/adversarial-review.md](references/adversarial-review.md);
   see [soul-roles.md](references/soul-roles.md#executing-roles-as-one-agent)
   for exactly how to satisfy this alone when it cannot.
8. **Interpret with restraint.** *Role: Analyst drafts, Statistician checks.*
   Apply [references/interpretation-rules.md](references/interpretation-rules.md).
   Null, blocked, and fragile results are scientific information.
9. **Update theory and writing only from artifacts.** *Role: Theory-updater for
   theory; Writer for manuscripts.* For theory integration, read
   [references/theory-update.md](references/theory-update.md). For manuscripts,
   every empirical sentence must be anchored to artifacts.

## Reusable Scripts

- `scripts/init_analysis.py`: create a small analysis scaffold.
- `scripts/validate_analysis_config.py`: validate required config fields and
  path/hash records.
- `scripts/manifest_results.py`: write SHA-256 manifests for result folders.

Scripts are helpers, not substitutes for scientific approval. Patch them for
project-specific schema only after the relevant choices are frozen.

## Completion Standard

Scientific work is complete only when the frozen plan is honored, controls pass,
outputs are complete, figures are inspected, hashes/manifests/logs exist,
limitations are explicit, and the next status is clear: blocked, revised,
exploratory, confirmed, falsified, or integrated.

Under-use of authorized time or compute is a planning failure, not thrift; an
analysis that returns a thin result well inside its approved budget reports
why the remaining budget was not used.
