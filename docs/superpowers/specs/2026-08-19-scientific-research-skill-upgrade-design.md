# Scientific Research Data Analysis Skill — Upgrade Design

**Date:** 2026-08-19
**Target:** `scientific-research-data-analysis/`
**Source of findings:** Anthropic, `claude-protein-binder-design` prompt dataset
(Hugging Face), plus `scientific-research-data-analysis/anthropic_scientific_exploration_prompt_analysis.md`

## 1. Context

The skill governs scientific analysis from idea to results: a nine-step
workflow with a shared-understanding gate, SOUL role separation, a data
contract, a freeze rule, and adversarial review. It is oriented toward
statistical inference on existing data — estimand, null model, multiplicity,
exclusions.

Anthropic's protein-binder campaign prompts govern a different shape of work:
generate → screen → rank → select, driven by third-party tools used as
instruments. Two layers of that document transfer to this skill and are absent
from it today:

1. **Instrument discipline** — a tool is not trusted until it has been proven
   to work on real data, and the thing that generates a result does not get to
   be the sole judge of it.
2. **Claim discipline** — every number and identifier that leaves a session
   traces to an executed lookup or measurement.

A third finding reframes the skill's autonomy model: in the source prompt,
autonomy is bought with pre-decided failure behavior, not with looser gates. An
agent interrupts when it meets an unhandled case, so every failure path decided
in advance is one interruption pre-spent.

## 2. Goals

- Raise effectiveness by catching tool failure and untraceable claims early.
- Raise autonomy by replacing the round-by-round planning interview with a
  drafted proposal, and by giving failed instruments a self-clearing ladder.
- Raise creativity by giving unexplored ideas a durable home outside the
  current plan.
- Preserve the skill's existing architecture: one reference file per concern,
  loaded on demand.

## 3. Non-goals

- No campaign mode, agent swarm, or spend governor. The primary use is
  interactive analysis with occasional unattended runs.
- No restructuring of the nine-step workflow, and no renumbering of steps.
- No general mechanical-enforcement rewrite. Only the instrument record is
  wired into a script, because only it has a stable schema.
- Exploration-search rules (evidence-for-stopping, allocate-by-evidence) are
  out of scope. They matter most in a search over many candidates.

## 4. Confirmed design decisions

| Decision | Choice |
|---|---|
| Structure | New reference files plus surgical edits; no restructure |
| Planning gate | Propose-then-verify, replacing the frontier interview |
| Common understanding | Retained as a mandatory, explicitly confirmed outcome |
| Instrument validation trigger | First use in a project; re-fires on version, parameter, or data-regime change |
| Scope additions | Instrument validation, claim discipline, fallback ladder, ideas list |

## 5. Change 1 — Operating Rule and planning gate

### 5.1 `SKILL.md` Operating Rule

The middle branch is rewritten. Current behavior requires a frontier-round
interview and explicit confirmation of every open choice before any
result-producing work. New behavior:

- **Read-only discussion, brainstorming, or plan sketch** — compact decision
  ledger. Unchanged.
- **Result-producing work** — the agent establishes the facts itself, drafts
  the complete analysis proposal, and presents it once: the plan, every degree
  of freedom it filled, the rationale for each, and what it left open. The user
  approves, edits, or rejects in one pass.
- **Two categories still block:**
  - **The scientific target.** Hypothesis, estimand, and null model are
    confirmed before any test runs.
  - **Expensive or irreversible compute.** First real-data run, compute over
    30 minutes, confirmatory one-shot runs. Presented with analysis id,
    dataset, operation, and time estimate.

The freeze rule does not move: `plan.md` and `config.json` exist before any
outcome is inspected.

One existing line is reformulated rather than deleted. Current text: "Never
fill a scientific degree of freedom with a silent default." Replacement: **a
default may be filled, never silently.** Every filled degree of freedom appears
in the proposal as a named assumption with its rationale, in a form the user
can reject.

`claim-discipline.md` is referenced from the Operating Rule as a standing rule
that applies at every step, not as a workflow step of its own.

### 5.2 `references/common-understanding-gate.md`

The `## Rule` section is rewritten. `## Compact Ledger Mode` and
`## Reopening Choices` are kept as-is.

**Common understanding remains mandatory.** The planning stage always ends in
confirmed shared understanding. The mechanism changed; the requirement did not.
Two guarding clauses:

- Confirmation is explicit. Silence is not confirmation, and absence of
  objection is not confirmation.
- An agent that cannot draft a proposal it can defend has not established
  understanding. It returns to fact-finding rather than presenting a proposal
  full of open questions.

**The necessity test.** A question may be asked only when the answer is not
determined by any of:

1. **A fact the agent can establish itself.** Facts are never asked of the
   user. A single read, grep, or listing is done inline; anything requiring
   directory-tree exploration, a script run, or cross-referencing is dispatched
   to a sub-agent.
2. **A decision already confirmed in this session.** The agent derives the
   consequence and states the derivation.
3. **A defensible default.** The agent states it as a named assumption the user
   can reject.

When none of the three applies, ask. Otherwise decide and record.

**Derived decisions inherit confirmation.** A decision determined by an
already-confirmed choice is presented as a consequence — "because you chose X,
Y follows" — not re-asked. Confirming one decision shrinks the remaining
question set; it never unlocks a new round of questions.

**Mechanical check.** More than three questions surviving the necessity test is
evidence that facts were not established. The agent returns to fact-finding and
re-derives rather than presenting the list.

The frontier concept survives with a changed job: it no longer sequences
questions to the user, it orders what the agent resolves for itself before a
coherent proposal exists.

This necessity test governs any grilling or interview procedure invoked on an
analysis in this skill's scope, including `anthropic-skills:grilling`.

## 6. Change 2 — New reference file: `references/instrument-validation.md`

Owner: Analyst (see `soul-roles.md`). Re-checked by Adversary at step 7.

### 6.1 Opening principle

**A generator is not its own evaluator.** Whatever produced a result does not
get to be the sole judge of it. In practice:

- A model's own fit statistics are not validation of that model.
- An artifact-removal step is not confirmed by the metric that step optimized.
- A pipeline's own QC panel is not sole evidence the pipeline worked.

Independent evaluation means a different instrument, a held-out measurement, or
a check the generating procedure did not optimize.

### 6.2 When the gate fires

A tool passes validation the first time the project depends on it for a result,
and again whenever any of these change: tool version, parameters, or input data
regime. The PASS record is reused for the project's lifetime otherwise.

### 6.3 PASS conditions

A tool is validated only when all hold:

1. It ran on **real project data**, not a toy or synthetic example.
2. It ran at the **same version and parameters** used in production.
3. The output **parses** and carries the expected shape, units, and range.
4. The **downstream step consumed it** — the next stage in the pipeline
   accepted the output and produced its own.
5. The output is **not degenerate** (see 6.5).

A tool that exits zero without satisfying all five is not validated. Process
exit status is not evidence of scientific validity.

### 6.4 Instrument record

Recorded in `config.json` under an `instruments` array, one entry per tool:

```
{ "name", "version", "install_source", "parameters",
  "input_path", "input_sha256", "runtime_s", "output_shape",
  "validated_at", "status" }
```

This block is validated by `scripts/validate_analysis_config.py` (Change 5).

### 6.5 Degenerate-output detectors

Treat anomalies as bugs until investigated. Halt the affected stage, diagnose,
then proceed. Detectors:

- a gate or filter that passes everything, fails everything, or returns a
  constant;
- a score of exactly zero, a perfect metric, or an impossible runtime;
- output identical across inputs that differ;
- an all-NaN or all-zero array where signal is expected.

A NaN in a result column is a missing measurement, not a flag value.

### 6.6 Canary before scale

Before any fan-out, run one case from the same specification. After the first
chunk of a batch stage, confirm **from its outputs** — item counts, pass/fail
counts, and one spot-checked example — that the stage ran as specified, before
launching the rest.

**Cheapest falsifying check first.** Before committing significant compute to a
plan, run the fastest check that could kill it. A seconds-scale check that
could invalidate a multi-hour run runs first.

### 6.7 Method tiering

Every instrument carries one tier, recorded with it:

- **Required** — feeds the reported result.
- **Shadow** — tracked and reported, decides nothing.
- **Diagnostic** — can flag a problem; cannot authorize a claim or an
  exclusion. Consistent with the Diagnostic label in
  `interpretation-rules.md`.
- **Fallback** — used only after the ladder in 6.8, and recorded as such.

Substitution across tiers is explicit, justified, and logged.

### 6.8 Fallback ladder

On instrument failure, in order:

1. **Diagnose.** Read the tool's own documentation and source before declaring
   it broken; a config flag or known limitation is usually documented there.
2. **Retry only if the retry differs in a way you can name and log.** A retry
   that cannot be distinguished from the previous attempt is not a retry.
3. **Approved fallback.** Substitute a tool of equal or better tier.
4. **Log the drop with its consequence stated** — which analysis objective is
   now weaker, and by how much.

Unattended substitution is permitted. Silent substitution is not: step 4 is the
condition that makes step 3 allowable without asking.

**Unavailability requires logged queries.** Before concluding a tool, package,
or version does not exist, query its canonical sources directly and log the
exact queries with the conclusion.

### 6.9 Documentation is not validation

A skill, wrapper, or helper that mentions a tool is reference material only.
Its existence is not evidence the tool works in this environment, and a helper
it provides is not a validated instrument. Where a skill and upstream
documentation disagree, upstream wins.

## 7. Change 3 — New reference file: `references/claim-discipline.md`

Standing rule, referenced from the Operating Rule. Applies at every step.

1. **State only what you established.** Any factual claim in a summary, figure
   caption, or manuscript traces to an executed computation or a saved artifact
   that can be cited. "Verified" means a check was run and its output exists.
2. **Never write an identifier from memory.** Every DOI, PMID, accession,
   dataset id, URL, atlas coordinate, and citation is the literal output of a
   lookup executed in the same session that wrote it.
3. **Counts are measured, never intended.** N at every stage is read from the
   artifact at write time, never reconstructed from what the config commanded.
   Where measured disagrees with planned, report measured and the gap.
4. **One source per number.** Every reported figure comes from a single saved
   query re-run at write time. Numbers are not hand-carried between
   `summary.md`, a figure caption, and a manuscript.
5. **Open, do not path-resolve.** Before declaring outputs complete, open every
   file the summary references.
6. **Epistemic tiers at synthesis.** Label each statement OBSERVATION,
   INFERENCE, HYPOTHESIS, or UNRESOLVED. The agent's own proposals and any
   sub-agent's recommendation remain labeled as such.
7. **Lead with the unfavorable reading.** The headline states the worst
   defensible reading of the data. Deviations from the frozen plan are
   disclosed. An analysis tuned after seeing its results is reported as such,
   with the number of configurations tried.
8. **Report messy or inconclusive results as messy or inconclusive.**
9. **Standards bind tighter under autonomy.** Propose-then-verify reduces human
   review, which leaves the agent's own verification as the only gate. Between
   shipping a confident result and flagging an uncertainty, flag the
   uncertainty.

## 8. Change 4 — Edits to existing files

### `SKILL.md`
- Operating Rule rewritten per 5.1.
- Step 6 (Implement minimally) gains instrument validation as its precondition,
  linking `instrument-validation.md`.
- Completion Standard gains: **under-use of authorized time or compute is a
  planning failure, not thrift.** An analysis that returns a thin result well
  inside its approved budget reports why the remaining budget was not used.

### `references/soul-roles.md`
- Step 2 row reworded from "Orchestrator interviews" to "Orchestrator drafts
  and defends the proposal".
- Analyst gains ownership of `instrument-validation.md`.
- Adversary gains re-check of the instrument record.

### `references/adversarial-review.md`
- Two reviewer properties made explicit: at least one reviewer generates **new
  measurements** rather than only reading documents; at least one forms its
  verdict from raw artifacts without the analyst's conclusions. The second
  sharpens the existing Inputs rule.
- Every review finding ships with the exact command or query that produced each
  number.
- Checklist gains an instrument-record item.

### `references/interpretation-rules.md`
- Unfavorable-first headline rule.
- Post-hoc tuning disclosed with the number of configurations tried.
- Cross-reference to the epistemic tiers in `claim-discipline.md`.

### `references/analysis-artifact-contract.md`
- `config.json` gains the `instruments` block (6.4).
- New optional file `ideas.md` in the analysis folder: candidate directions not
  in the current plan, ranked, each with a one-line rationale and a rough cost.
  Maintained continuously as ideas occur, consulted when the analysis stalls.
  Rationale: creative output degrades under pressure, so idea generation is
  decoupled in time from idea selection.
- Result Summary gains the retrievability check (open every referenced file).

### `references/statistician-review.md`
- Post-Result Review gains degenerate-output detection (6.5).

## 9. Change 5 — `scripts/validate_analysis_config.py`

- Validate the `instruments` array: required keys present, `validated_at`
  parseable, `status` in an allowed enum.
- Fail when a tool referenced in `code/` has no entry in the instrument record.
- Keep the script's existing checks unchanged.

The script remains a helper, not a substitute for scientific approval.

## 10. Change 6 — Style pass

The existing files are already close to this style. A survey at spec time found
two soft uses of `should` (`analysis-artifact-contract.md:41`,
`statistician-review.md:19`) and three other hedge words across the whole
skill. The pass is therefore small in the existing files, and its main job is
holding the two new files to the same standard.

- **Remove `should`.** Each rule becomes either a gate ("X does not count as
  done unless…") or a bounded permission ("you may X, provided Y"). The source
  prompt uses `should` roughly once in 114KB; that discipline is most of why
  its rules survive contact with a busy agent.
- Use the reclassification form where it earns its place: name the tempting
  benign reading, then override it.
- Mark which rules `validate_analysis_config.py` checks, so the remainder is
  honestly labeled as judgment.
- Verification: `grep -rniE '\b(should|prefer|try to|when possible|ideally)\b'`
  over `SKILL.md` and `references/` returns only occurrences that are gates or
  bounded permissions in context.

## 11. Acceptance criteria

1. Two new reference files exist and are linked from `SKILL.md`.
2. The Operating Rule describes propose-then-verify, retains the two blocking
   categories, and retains the freeze rule.
3. `common-understanding-gate.md` states that common understanding is mandatory
   and explicitly confirmed, and contains the three-part necessity test and the
   derived-decisions-inherit-confirmation rule.
4. No occurrence of `should` as a soft preference remains in `SKILL.md` or any
   reference file.
5. `validate_analysis_config.py` accepts a config with a well-formed
   `instruments` block and rejects one where a code-referenced tool is missing
   from it.
6. Every cross-reference link between files resolves.
