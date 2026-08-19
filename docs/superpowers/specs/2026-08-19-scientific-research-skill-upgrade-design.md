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

The `## Rule` section is rewritten. `## Reopening Choices` is kept as-is.
`## Compact Ledger Mode` is amended (see 5.3).

The freeze precondition keeps all three of its terms and its strength: plan,
config, and data contract are **frozen** — not merely present — before analysis
code is written or any outcome is inspected.

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

### 5.3 `## Compact Ledger Mode` is amended, not preserved

The section reads, in the version this upgrade inherits:

> "For read-only planning or simple low-risk tasks, skip the round structure: a
> single compact ledger may group related decisions. Label anything unresolved
> and do not proceed to outcomes."

"The round structure" named the three frontier rounds. With those gone, the
phrase binds instead to the only mechanism `## Rule` now prescribes — the
proposal and its confirmation — turning the section into a bypass. Two further
properties make it load-bearing: its trigger is a disjunction that admits
result-producing work an agent self-labels "simple low-risk", broader than the
Operating Rule's read-only branch; and its backstop bars inspecting outcomes
without barring the writing or running of analysis code.

The section is therefore amended on both counts:

- Its trigger narrows to match the Operating Rule's first branch exactly:
  read-only discussion, brainstorming, or plan sketch. The separate
  "simple low-risk tasks" clause is removed.
- It states that the compact ledger changes how decisions are grouped for
  presentation and never removes the explicit-confirmation requirement.

What the section keeps: a compact ledger may group related decisions in one
presentation, and anything unresolved is labeled.

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

A stage passes validation the first time the project depends on it for a
result, and again whenever any of these change: tool version, parameters, or
input data regime. The PASS record is reused for the project's lifetime
otherwise, subject to the cascade rule in 6.3.2.

### 6.3 PASS conditions

A stage is validated only when all hold:

1. It ran on **real project data**, not a toy or synthetic example.
2. It ran at the **same version and parameters** used in production.
3. The output **parses** and carries the expected shape, units, and range.
4. The **downstream step consumed it** — the next stage in the pipeline
   accepted the output and produced its own.
5. The output is **not degenerate** (see 6.5).

A stage that exits zero without satisfying all five is not validated. Process
exit status is not evidence of scientific validity.

#### 6.3.1 PASS is a property of the chain, not of a tool

Conditions 1 and 4 point in opposite directions along the pipeline, so no stage
can be validated in isolation. Condition 1 requires that the stage saw real
project data — for any stage after the first, that means the real output of its
validated predecessor, never a synthetic stand-in. Condition 4 requires that
the stage's successor consumed its output. Every stage therefore depends on
both of its neighbours, and PASS attaches to a **position in a chain**, not to
a tool in the abstract. The same tool at two positions holds two records.

Consequences:

- **The chain is linear.** Each stage after the first consumes the stage at
  `position - 1`. Two stages consuming one predecessor would make "the terminal
  stage" ambiguous and would let a fork escape the staleness rule, since each
  branch is compared only against the shared parent.
- **Validation runs in pipeline order.** A stage cannot be validated before its
  predecessor, because its condition-1 input does not exist yet.
- **A stage reaches PASS only after its successor has run once on its output.**
  Until then it is PENDING, not PASS.
- **The terminal stage's condition 4** is satisfied by the reported artifact —
  the figure, table, or statistic — being produced from its output.
- **The chain has a PASS only when every stage holds a current PASS** and one
  end-to-end run on real project data has completed.

#### 6.3.2 Cascade invalidation

A change at any stage clears that stage's PASS **and the PASS of every stage
downstream of it**, because those records were earned against output that no
longer exists. Changing the first stage's parameters invalidates the whole
chain.

Where a stage's consumer changes how it consumes, the producer's condition 4 is
re-tested even when the producer itself did not change.

**Mechanical check.** A stage whose `validated_at` predates the `validated_at`
of any upstream stage is stale. This requires no judgment and is enforced by
`scripts/validate_analysis_config.py` (Change 5).

### 6.4 Instrument record — declared and observed

The record splits across two files, because its two halves have different
lifetimes. The **declared chain** is a frozen decision: which stages exist,
in what order, each consuming which predecessor. The **observed state** changes
throughout the work as stages move PENDING to PASS and cascades mark stages
STALE. Writing mutable status into `config.json` would contradict the freeze
rule that governs that file, so the two are stored separately.

**Declared — `config.json`, key `instruments`.** One entry per stage, in
pipeline order. Frozen with the rest of the config; a change here is a dated,
labelled plan amendment like any other frozen-decision change.

```
{ "stage", "position", "consumes",
  "name", "version", "install_source", "parameters" }
```

- `stage` is the chain-position identifier and the join key to the observed
  record. `position` is its index; `consumes` names the upstream stage it takes
  input from (`null` for the first). Together these make the chain explicit so
  the cascade in 6.3.2 is computable rather than remembered.
- `name`, `version`, `install_source`, `parameters` identify the tool. The same
  tool at two positions produces two entries with different `stage` values.

**Observed — `gate_status.json`, key `instrument_status`.** One entry per
declared stage. Rewritten freely as work proceeds; it is a record of results,
not a frozen decision.

```
{ "stage", "status", "validated_at", "runtime_s", "output_shape", "input_ref" }
```

- `status` is one of `PASS`, `PENDING`, `FAIL`, `STALE`.
- `validated_at` is an ISO-8601 timestamp **carrying a UTC offset**. A naive
  timestamp is rejected: it cannot order a cascade across machines, and mixing
  naive and aware values raises at comparison time rather than reporting a
  diagnosis. A date without a time is likewise rejected.
- `input_ref` identifies the input without requiring a rehash of large raw
  data: for the first stage it is the data-contract entry (which already
  carries a SHA-256 per `data-contract.md`); for later stages it is the
  upstream stage name plus that stage's `validated_at`.

`gate_status.json` carries `instrument_status` at minimum. Other top-level keys
recording gate outcomes are permitted and are not validated by this skill.

**Agreement.** The two files name the same set of stages. A declared stage with
no observed entry, or an observed entry naming no declared stage, is an error.
Both files are validated together by `scripts/validate_analysis_config.py`
(Change 5).

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
   A claim carried forward from an earlier step is re-verified before it
   appears in a later artifact; carrying it forward unchecked does not count as
   re-verifying it.
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
- `config.json` gains the declared `instruments` block (6.4).
- Result Summary gains the retrievability check (open every referenced file).
- Cross-reference to the project ideas list (8.1). The per-analysis folder does
  not carry its own ideas file.
- **Contract drift correction** (8.2).

### 8.2 Aligning the contract with what agents produce

A survey of a real analysis folder found the documented contract and actual
agent output had diverged. `gate_status.json` and `final_report.md` appear
nowhere in the skill yet are produced every run; `summary.md` is required by
the contract yet absent from the folder; `audits/` is created by
`init_analysis.py` and unused. A contract agents do not follow is worse than no
contract, so the contract adopts observed reality:

- **`gate_status.json` is added to Required Files.** It records gate outcomes
  and carries `instrument_status` (6.4). Keys beyond `instrument_status` are
  permitted and unvalidated.
- **`summary.md` is renamed `final_report.md`** throughout
  `analysis-artifact-contract.md` and `soul-roles.md`. The Result Summary
  section's content requirements are unchanged; only the filename moves.
- **`audits/` is dropped** from `init_analysis.py`. Adversarial review output
  lands in `results/` alongside other artifacts.
- `tests/` is retained: it is created by the scaffold and present in practice.

### 8.1 Project ideas list — `ideas.md`

One file per **project**, at the project root, above `analyses/` — derived from
the analyses root rather than from the working directory, so it lands in the
project regardless of where the scaffold is invoked from. Required, not
optional. A per-analysis ideas file is explicitly rejected: fragmenting the
list across analysis folders destroys the accumulation that gives it value.

**Purpose.** Creative output degrades under exactly the conditions that demand
it — after a failure, against a deadline, late in a session. The file decouples
idea generation from idea selection in time: ideas are captured while thinking
is unhurried, and chosen from when the work stalls.

**Contents.** One line per idea, ranked by expected value, each carrying a
one-line rationale and a rough cost. An idea names what it would test or
change, not merely a topic.

**When it is written.** Continuously, whenever an idea surfaces and is not
pursued. Specifically:

- while discussing results — any alternative reading, follow-up, or "we could
  also look at" that is not being pursued now is captured rather than lost;
- during analysis — a method, control, or comparison considered and set aside;
- at data audit — a question the data raised that is out of the current scope;
- at theory update — the next stubs proposed by `theory-update.md` are entered
  here, and the two artifacts stay consistent.

**When it is read.** When an analysis stalls, when a method is dropped via the
fallback ladder (6.8), and at every theory update.

**Status marking.** Each entry carries one of: open, in progress, done
(pointing at the analysis id that took it up), or dropped with a reason.
An idea is never silently deleted.

### `references/theory-update.md`
- The "at most three next stubs" rule gains its destination: stubs are recorded
  in the project `ideas.md` (8.1). Stubs remain inputs to a future Theorist
  pass, not self-authorizing.

### `references/statistician-review.md`
- Post-Result Review gains degenerate-output detection (6.5).

## 9. Change 5 — `scripts/validate_analysis_config.py`

The script takes `config.json` and reads `gate_status.json` from the same
directory, overridable with `--gate-status PATH`.

- Validate the declared `instruments` array in `config.json`: required keys
  present, no duplicate `stage` names.
- Validate `instrument_status` in `gate_status.json`: required keys present,
  `validated_at` parseable, `status` in `{PASS, PENDING, FAIL, STALE}`.
- **Agreement check:** the two files name the same set of stages. Report any
  declared stage missing an observed entry, and any observed entry naming no
  declared stage.
- **Not mechanically checked:** whether every tool `code/` actually uses has an
  instrument record. An import is not decidable as an instrument — `numpy` is
  not one, `mne` may be — so a static check produces false positives until it
  is disabled, which is worse than no check. Coverage of the record is a
  judgment call and lives on the Adversary's checklist in
  `adversarial-review.md`, not in this script.
- **Legacy configs:** a `config.json` without `instruments` fails with a
  message naming the fix — add `"instruments": []` and create a
  `gate_status.json` containing `{"instrument_status": []}`.
- **Chain checks** (6.3.1, 6.3.2), all mechanical:
  - `position` values form a contiguous ordering with no gaps or duplicates;
  - every `consumes` names an existing stage, and only the first stage has
    `consumes: null`;
  - the graph is acyclic;
  - **staleness** — any stage whose `validated_at` predates the `validated_at`
    of any upstream stage is reported STALE, along with every stage downstream
    of it;
  - no stage carries `PASS` while any upstream stage carries `PENDING`, `FAIL`,
    or `STALE`.
- Report the chain's overall state: PASS only when every stage is PASS.
- Keep the script's existing checks unchanged.

The script remains a helper, not a substitute for scientific approval. It
checks the chain's arithmetic; it cannot check that a stage's output is
scientifically correct.

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

## 11. Field-use findings and resulting changes

A real project using this skill was surveyed on 2026-08-19: 52 analysis folders
(`F001`-`F048`) plus an earlier generation under
`TW_theta_coupling_reproduction/`. The survey found the plan-and-freeze half of
the workflow working and the review-and-report half decaying. The four changes
below come from that evidence; each cites what was observed.

### 11.1 Canonical artifact filenames

**Observed.** Fourteen distinct filenames carry statistician-review output
(`statistician_review.md`, `statistician_design_review.md`,
`statistician_result_review.md`, `statistician_final_review.md`,
`statistical_review.md`, and more), including two spellings of one artifact:
`post_result_statistician_review.md` and `postresult_statistician_review.md`.
Roughly nineteen filenames carry controller-audit output. Two filenames carry
the freeze record: `freeze_manifest.json` and `freeze.json`.

**Consequence.** "Did the adversarial review run on F031?" cannot be answered
without opening the folder and reading. A gate whose output has no canonical
name is not mechanically checkable.

**Change.** `analysis-artifact-contract.md` gains a fixed filename table. Each
name is the most frequent observed spelling, so adopting it costs the least
renaming:

| Artifact | Canonical filename | Observed |
|---|---|---|
| Data-contract audit (Scout) | `input_audit.md` / `.json` | 22 / 15 |
| Statistician pre-analysis review | `statistician_review.md` | 29 |
| Statistician post-result review | `statistician_post_result_review.md` | 3 + 3 (two spellings) |
| Adversarial review (Adversary) | `adversarial_review.md` | 13 |
| Freeze record | `freeze_manifest.json` | 13 (vs `freeze.json` 6) |
| Gate outcomes + instrument status | `gate_status.json` | 17 |
| Result hashes | `result_manifest.json` | 14 |
| Final narrative | `final_report.md` | 7 (vs `summary.md` 3) |
| Theory-update entry | `lab_journal_entry.md` | 15 |

A review that ran under a different filename did not run, because it cannot be
found. Where one analysis needs several instances of an artifact (per stage,
per amendment), the canonical stem takes a suffix:
`adversarial_review_<stage>.md`, never a new stem.

### 11.2 Analysis families and configuration counts

**Observed.** `F007` through `F014` are nine analyses of one question, varying
exclusion threshold (6, 10, 15), sample size (n13, n16, n19, n25, n31), and
tmax (2000, 5000). `F007`'s plan declares `exploratory`, `selection-informed`,
and a multiplicity claim. `F010`, `F013`, and `F014` declare none of them. No
analysis in the project states how many configurations were tried.

**Consequence.** A garden of forking paths recorded in the filesystem, with the
labels that would flag it dropped exactly as the family grew.

**Change.** `config.json` gains a `family` block:

```
{ "family_id", "parent_analysis", "varies" }
```

- An analysis that changes a parameter of an earlier analysis addressing the
  same question sets `parent_analysis` to that analysis id and shares its
  `family_id`. `varies` names the parameters changed.
- Every family member's final report states the family size at write time:
  configuration k of n tried.
- `interpretation-rules.md`: a member of a family larger than one is not
  labeled confirmatory unless the whole family was frozen before outcome
  access. Absent that, the family is selection-informed, and the count is
  reported with the result.

### 11.3 Unique analysis ids

**Observed.** `F014` and `F030` each name two different directories. Ids are
assigned by hand and collide.

**Change.** `init_analysis.py` exits non-zero when the target directory already
exists, and when any sibling directory shares the new id's ordinal prefix
followed by `_`. An id is not reused; a variant takes its own id and records
`parent_analysis` per 11.2.

### 11.4 The theory document and the lab journal are different artifacts

**Observed.** `lab_journal/theta_coupled_tw_progress.md` is 403 KB and 5,746
lines, current to 2026-08-18. Every file in `theory/` was last modified
2026-07-23. Roughly thirty analyses ran after the theory stopped being updated,
and nothing detected it.

**Consequence.** Step 9 silently stopped executing a third of the way through
the project. Everything learned went into an append-only log too large to read
under pressure, while the short document that could guide a decision went a
month stale.

**Change.** `theory-update.md` states the distinction as a rule:

- The **lab journal** is an append-only record. It grows without bound. It is
  written to on every update and is not a decision aid.
- The **theory document** is current-state and bounded. It is **re-derived**,
  not appended to: superseded claims are removed or marked, not accumulated.
- Appending a journal entry does not satisfy step 9. A theory update that
  leaves the theory document unchanged states why in the journal entry, naming
  the artifact that failed to move it.

A staleness detector — flagging when the theory document is older than N
completed analyses — is deferred to separate work; it needs a script and a
threshold the project owner chooses.

## 12. Acceptance criteria

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
5a. Chain semantics hold: PASS is defined per stage-position rather than per
   tool; a stage is PENDING until its successor consumes its output; a change
   at any stage cascades STALE to every downstream stage; and the script
   detects staleness from `validated_at` ordering alone.
5b. The declared chain lives in frozen `config.json` and the observed status in
   mutable `gate_status.json`; the script validates both and reports any stage
   present in one and missing from the other.
5c. The contract's Required Files match a real analysis folder:
   `gate_status.json` is listed, `final_report.md` has replaced `summary.md`
   in both `analysis-artifact-contract.md` and `soul-roles.md`, and
   `init_analysis.py` no longer creates `audits/`.
6. The project ideas list is specified as one required file at the project
   root, with its write triggers (results discussion, analysis, data audit,
   theory update) and read triggers (stall, method drop, theory update) named,
   and `theory-update.md` points its stubs at it.
7. Every cross-reference link between files resolves.
8. `analysis-artifact-contract.md` carries the canonical filename table (11.1),
   and the names in it match the table's spellings exactly.
9. `config.json` accepts a `family` block with `family_id`, `parent_analysis`,
   and `varies`; `interpretation-rules.md` states that a member of a family
   larger than one is not labeled confirmatory unless the whole family was
   frozen before outcome access.
10. `init_analysis.py` exits non-zero on a duplicate analysis id and on an id
   whose ordinal prefix is already taken by a sibling directory.
11. `theory-update.md` states that the lab journal is append-only and the
   theory document is re-derived, and that a journal entry alone does not
   satisfy step 9.
