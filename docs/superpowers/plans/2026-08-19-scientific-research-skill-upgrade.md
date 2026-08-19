# Scientific Research Data Analysis Skill Upgrade — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add instrument validation and claim discipline to the
`scientific-research-data-analysis` skill, replace its planning interview with
propose-then-verify while keeping common understanding mandatory, and make the
instrument chain machine-checkable.

**Architecture:** The skill is a prose Claude Skill: one `SKILL.md` entry point,
nine on-demand reference files under `references/`, three helper scripts under
`scripts/`. This upgrade adds two reference files, rewrites two prose sections
that change agent behavior, edits five reference files in place, and extends
two scripts. No file is restructured and no workflow step is renumbered.

**Tech Stack:** Markdown (prose skill files); Python 3 standard library only
(`argparse`, `json`, `hashlib`, `datetime`, `pathlib`, `unittest`). No third-party
dependencies are added — the repository has none and introduces none here.

## Global Constraints

- **Spec is the content source.** The design spec at
  `docs/superpowers/specs/2026-08-19-scientific-research-skill-upgrade-design.md`
  is committed and complete. Each task names the spec section that defines its
  prose. Do not paraphrase the spec from memory — open it and read the named
  section. Copying the spec's prose into this plan would create two sources of
  truth that drift; the spec is the single source.
- **No `should` as a soft preference.** Every rule written in this upgrade is
  either a gate ("X does not count as done unless…") or a bounded permission
  ("you may X, provided Y"). This applies to new prose and to prose you touch.
- **Line width:** wrap prose at 80 columns, matching every existing file.
- **Encoding:** the existing scripts write `encoding="ascii"`. Keep prose ASCII
  in script-generated files. Reference `.md` files may use UTF-8 punctuation,
  matching the existing files (they contain `—` and `×`).
- **Python:** standard library only. No new dependencies, no `pyproject.toml`,
  no pytest.
- **Working directory:** all paths below are relative to the repository root
  `/Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills`.
- **Relative links:** reference files link to each other by bare filename
  (`[soul-roles.md](soul-roles.md)`); `SKILL.md` links with the `references/`
  prefix (`[references/soul-roles.md](references/soul-roles.md)`). Match the
  existing convention exactly.
- **Commit after every task.** One commit per task, message given in the task.

---

### Task 1: New reference file — instrument validation

**Files:**
- Create: `scientific-research-data-analysis/references/instrument-validation.md`
- Read for content: `docs/superpowers/specs/2026-08-19-scientific-research-skill-upgrade-design.md` §6 (6.1 through 6.9)
- Read for style: `scientific-research-data-analysis/references/data-contract.md`

**Interfaces:**
- Consumes: nothing.
- Produces: the file `references/instrument-validation.md` containing the
  headings listed in Step 1. Task 3 links to it from `SKILL.md` step 6. Task 5
  links to it from `soul-roles.md` and `adversarial-review.md`. Task 6's
  validator implements the schema defined in its "Instrument record" section.

- [ ] **Step 1: Write the verification check and confirm it fails**

Create nothing yet. Run this check first so you can see it fail:

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis
grep -c '^## ' references/instrument-validation.md
```

Expected: FAIL — `grep: references/instrument-validation.md: No such file or directory`

- [ ] **Step 2: Write the file**

Open the spec at
`docs/superpowers/specs/2026-08-19-scientific-research-skill-upgrade-design.md`
and read §6 in full. Write the file with exactly these headings, in this order,
turning each spec subsection into the corresponding section's prose:

```markdown
# Instrument Validation

## A Generator Is Not Its Own Evaluator     <- spec 6.1
## When The Gate Fires                      <- spec 6.2
## PASS Conditions                          <- spec 6.3
### PASS Is A Property Of The Chain         <- spec 6.3.1
### Cascade Invalidation                    <- spec 6.3.2
## Instrument Record                        <- spec 6.4
## Degenerate-Output Detectors              <- spec 6.5
## Canary Before Scale                      <- spec 6.6
## Method Tiering                           <- spec 6.7
## Fallback Ladder                          <- spec 6.8
## Documentation Is Not Validation          <- spec 6.9
```

Open with a one-paragraph lede in the style of `data-contract.md`'s opening,
naming the owning role: the Analyst owns this file, the Adversary re-checks it
(this matches the role assignment Task 5 writes into `soul-roles.md`).

These exact strings must appear verbatim, because later tasks and the
acceptance criteria grep for them:

- `A generator is not its own evaluator`
- `real project data`
- `PENDING`
- `PASS`, `FAIL`, `STALE`
- `log the drop with its consequence stated`
- `Process exit status is not evidence of scientific validity`

The record schema in the "Instrument Record" section must list exactly these
twelve keys, because Task 6 validates them:
`stage`, `position`, `consumes`, `name`, `version`, `install_source`,
`parameters`, `input_ref`, `runtime_s`, `output_shape`, `validated_at`,
`status`.

Cross-link `interpretation-rules.md` from the Method Tiering section (the
Diagnostic tier is defined there) and `data-contract.md` from the Instrument
Record section (first-stage `input_ref` points at a data-contract entry).

- [ ] **Step 3: Run the verification checks**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis
grep -c '^## ' references/instrument-validation.md
grep -q 'A generator is not its own evaluator' references/instrument-validation.md && echo "lede OK"
grep -q 'PENDING' references/instrument-validation.md && echo "pending OK"
grep -q 'log the drop with its consequence stated' references/instrument-validation.md && echo "ladder OK"
for k in stage position consumes name version install_source parameters input_ref runtime_s output_shape validated_at status; do
  grep -q "$k" references/instrument-validation.md || echo "MISSING KEY: $k"
done
grep -nE '\b[Ss]hould\b' references/instrument-validation.md
```

Expected: first command prints `9` (the two `###` subsections do not match
`^## `); three `OK` lines; no `MISSING KEY` lines; the final grep prints
nothing.

- [ ] **Step 4: Verify every link resolves**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis/references
grep -o '](\([a-z0-9-]*\.md\)[^)]*)' instrument-validation.md | sed 's/](\([^)#]*\).*/\1/' | sort -u | while read -r f; do
  test -f "$f" || echo "BROKEN LINK: $f"
done
```

Expected: no output.

- [ ] **Step 5: Commit**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills
git add scientific-research-data-analysis/references/instrument-validation.md
git commit -m "Add instrument-validation reference to scientific research skill"
```

---

### Task 2: New reference file — claim discipline

**Files:**
- Create: `scientific-research-data-analysis/references/claim-discipline.md`
- Read for content: `docs/superpowers/specs/2026-08-19-scientific-research-skill-upgrade-design.md` §7
- Read for style: `scientific-research-data-analysis/references/interpretation-rules.md`

**Interfaces:**
- Consumes: nothing.
- Produces: the file `references/claim-discipline.md`. Task 3 references it
  from the `SKILL.md` Operating Rule as a standing rule. Task 5 cross-links its
  epistemic tiers from `interpretation-rules.md`.

- [ ] **Step 1: Confirm the check fails**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis
grep -c '^## ' references/claim-discipline.md
```

Expected: FAIL — no such file.

- [ ] **Step 2: Write the file**

Read spec §7 in full. It contains nine numbered rules. Write them as sections
under these headings:

```markdown
# Claim Discipline

## Standing Rule                    <- lede: applies at every workflow step
## State Only What You Established  <- spec 7.1
## Identifiers Are Never Written From Memory  <- spec 7.2
## Counts Are Measured, Never Intended        <- spec 7.3
## One Source Per Number                      <- spec 7.4
## Open, Do Not Path-Resolve                  <- spec 7.5
## Epistemic Tiers At Synthesis               <- spec 7.6
## Lead With The Unfavorable Reading          <- spec 7.7 and 7.8
## Standards Bind Tighter Under Autonomy      <- spec 7.9
```

These exact strings must appear verbatim:

- `OBSERVATION`, `INFERENCE`, `HYPOTHESIS`, `UNRESOLVED`
- `the literal output of a lookup executed in the same session`
- `report measured and the gap`
- `the number of configurations tried`

In the identifiers section, name this repository's own lookup skills as the
means of compliance: `paper-lookup`, `zotero-research-skill`, and
`neuroscience-database-lookup`. Do not link them as files — they are sibling
skills, not files in this directory. Name them in prose only.

- [ ] **Step 3: Run the verification checks**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis
grep -c '^## ' references/claim-discipline.md
for s in OBSERVATION INFERENCE HYPOTHESIS UNRESOLVED; do
  grep -q "$s" references/claim-discipline.md || echo "MISSING TIER: $s"
done
grep -q 'the literal output of a lookup executed in the same session' references/claim-discipline.md && echo "identifiers OK"
grep -q 'the number of configurations tried' references/claim-discipline.md && echo "tuning OK"
grep -nE '\b[Ss]hould\b' references/claim-discipline.md
```

Expected: first command prints `9`; no `MISSING TIER` lines; two `OK` lines;
the final grep prints nothing.

- [ ] **Step 4: Verify every link resolves**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis/references
grep -o '](\([a-z0-9-]*\.md\)[^)]*)' claim-discipline.md | sed 's/](\([^)#]*\).*/\1/' | sort -u | while read -r f; do
  test -f "$f" || echo "BROKEN LINK: $f"
done
```

Expected: no output.

- [ ] **Step 5: Commit**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills
git add scientific-research-data-analysis/references/claim-discipline.md
git commit -m "Add claim-discipline reference to scientific research skill"
```

---

### Task 3: Operating Rule and planning gate — propose-then-verify

This is the only task that changes existing agent behavior. Read spec §5 in
full before editing.

**Files:**
- Modify: `scientific-research-data-analysis/SKILL.md` (Operating Rule block;
  Workflow step 6; Completion Standard)
- Modify: `scientific-research-data-analysis/references/common-understanding-gate.md`
  (`## Rule` section only)
- Read for content: spec §5.1, §5.2, and §8 (the `SKILL.md` row)

**Interfaces:**
- Consumes: `references/instrument-validation.md` (Task 1) and
  `references/claim-discipline.md` (Task 2) — both must exist before this task
  links to them.
- Produces: the rewritten Operating Rule and gate. Task 5 rewords the
  `soul-roles.md` step 2 row to match the wording chosen here; use exactly
  "drafts and defends the proposal" so the two files agree.

- [ ] **Step 1: Record the current state so the diff is reviewable**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis
grep -n 'silent default' SKILL.md
grep -n 'frontier rounds' SKILL.md
grep -n 'Frontier' references/common-understanding-gate.md
```

Expected: `SKILL.md` matches on the "Never fill a scientific degree of freedom
with a silent default" line and the "work it in frontier rounds" line;
`common-understanding-gate.md` matches inside its `## Rule` section. These are
the lines this task replaces.

- [ ] **Step 2: Rewrite the SKILL.md Operating Rule**

Replace the middle bullet of the Operating Rule per spec §5.1. The rewritten
block states, in this order:

1. Read-only discussion, brainstorming, or plan sketch — compact decision
   ledger. Unchanged from current text.
2. Result-producing work — the agent establishes facts itself, drafts the
   complete proposal, and presents it once with every filled degree of freedom,
   its rationale, and what was left open.
3. Two categories still block: **the scientific target** (hypothesis, estimand,
   null model — confirmed before any test runs) and **expensive or irreversible
   compute** (first real-data run, compute over 30 minutes, confirmatory
   one-shot runs — presented with analysis id, dataset, operation, and time
   estimate).
4. The freeze rule is restated unchanged: `plan.md` and `config.json` exist
   before any outcome is inspected.

Replace the line "Never fill a scientific degree of freedom with a silent
default." with this exact sentence:

> A default may be filled, never silently. Every filled degree of freedom
> appears in the proposal as a named assumption with its rationale, in a form
> the user can reject.

Keep the existing sentence "Facts are discovered from files; decisions are
asked of the user." immediately before it — it is still true and now explains
the necessity test's first branch.

Add a sentence at the end of the Operating Rule naming
`[references/claim-discipline.md](references/claim-discipline.md)` as a
standing rule that applies at every step rather than as a workflow step.

- [ ] **Step 3: Add instrument validation to SKILL.md step 6 and the Completion Standard**

In Workflow step 6 ("Implement minimally"), add instrument validation as the
step's precondition, linking
`[references/instrument-validation.md](references/instrument-validation.md)`.
The existing sentences about controls and caching stay.

In the Completion Standard, add this exact sentence:

> Under-use of authorized time or compute is a planning failure, not thrift; an
> analysis that returns a thin result well inside its approved budget reports
> why the remaining budget was not used.

- [ ] **Step 4: Rewrite the gate's Rule section**

In `references/common-understanding-gate.md`, replace the `## Rule` section per
spec §5.2. Keep `## Compact Ledger Mode` and `## Reopening Choices` byte-for-byte
unchanged. The new `## Rule` states:

1. Common understanding remains mandatory, reached by proposal rather than
   interview. Confirmation is explicit — silence is not confirmation, and
   absence of objection is not confirmation.
2. An agent that cannot draft a proposal it can defend returns to fact-finding
   rather than presenting a proposal full of open questions.
3. The three-part necessity test (fact the agent can establish / decision
   already confirmed / defensible default stated as a named assumption).
4. Derived decisions inherit confirmation, presented as "because you chose X,
   Y follows" rather than re-asked.
5. The mechanical check: more than three surviving questions is evidence facts
   were not established; return to fact-finding and re-derive.
6. The frontier concept survives with a changed job — it orders what the agent
   resolves for itself, not what it asks.
7. The necessity test governs any grilling or interview procedure invoked on an
   analysis in this skill's scope, naming `anthropic-skills:grilling`.

Keep the existing paragraph distinguishing facts from decisions, including its
inline-versus-sub-agent rule for expensive fact-finding — it is the operative
detail of necessity-test branch 1.

- [ ] **Step 5: Run the verification checks**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis
grep -q 'A default may be filled, never silently' SKILL.md && echo "default rule OK"
grep -q 'Under-use of authorized time or compute is a planning failure' SKILL.md && echo "budget rule OK"
grep -q 'claim-discipline.md' SKILL.md && echo "claim link OK"
grep -q 'instrument-validation.md' SKILL.md && echo "instrument link OK"
grep -q 'silent default' SKILL.md && echo "FAIL: old wording survives"
grep -q 'Silence is not confirmation' references/common-understanding-gate.md && echo "confirmation OK"
grep -q 'anthropic-skills:grilling' references/common-understanding-gate.md && echo "grilling OK"
grep -q '## Compact Ledger Mode' references/common-understanding-gate.md && echo "compact mode preserved"
grep -q '## Reopening Choices' references/common-understanding-gate.md && echo "reopening preserved"
grep -nE '\b[Ss]hould\b' SKILL.md references/common-understanding-gate.md
```

Expected: seven `OK`/`preserved` lines, no `FAIL` line, final grep prints
nothing.

- [ ] **Step 6: Verify SKILL.md links resolve**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis
grep -o '](references/[a-z0-9-]*\.md)' SKILL.md | sed 's/](\(.*\))/\1/' | sort -u | while read -r f; do
  test -f "$f" || echo "BROKEN LINK: $f"
done
```

Expected: no output.

- [ ] **Step 7: Commit**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills
git add scientific-research-data-analysis/SKILL.md scientific-research-data-analysis/references/common-understanding-gate.md
git commit -m "Replace planning interview with propose-then-verify gate"
```

---

### Task 4: Project ideas list

**Files:**
- Modify: `scientific-research-data-analysis/references/analysis-artifact-contract.md`
- Modify: `scientific-research-data-analysis/references/theory-update.md`
- Read for content: spec §8.1 and the `theory-update.md` row in §8

**Interfaces:**
- Consumes: nothing.
- Produces: the `ideas.md` specification. Task 6's `init_analysis.py` change
  creates the file this section describes; the column headers written there
  must match the ones specified here: `Rank`, `Idea`, `Rationale`,
  `Rough cost`, `Status`.

- [ ] **Step 1: Confirm the checks fail**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis
grep -q 'ideas.md' references/analysis-artifact-contract.md && echo "found" || echo "absent as expected"
grep -q 'ideas.md' references/theory-update.md && echo "found" || echo "absent as expected"
```

Expected: both print `absent as expected`.

- [ ] **Step 2: Add the ideas list section to the artifact contract**

Read spec §8.1. Add a new `## Project Ideas List` section to
`references/analysis-artifact-contract.md`, placed after `## Required Files`
and before `## Freeze Rule`. It states:

- One file per project, at the project root, above `analyses/`. Required, not
  optional. A per-analysis ideas file is rejected — fragmenting the list across
  analysis folders destroys the accumulation that gives it value.
- Purpose: creative output degrades under the conditions that demand it, so the
  file decouples idea generation from idea selection in time.
- Contents: one line per idea, ranked by expected value, each with a one-line
  rationale and a rough cost. An idea names what it would test or change, not
  merely a topic.
- Write triggers: while discussing results, during analysis, at data audit, and
  at theory update.
- Read triggers: when an analysis stalls, when a method is dropped via the
  fallback ladder in `instrument-validation.md`, and at every theory update.
- Status values: `open`, `in progress`, `done` (naming the analysis id that
  took it up), `dropped` (with a reason). An idea is never silently deleted.

Also add `ideas.md` to the `## Required Files` list with a one-line description
noting it lives at the project root, not in the analysis folder.

- [ ] **Step 3: Point theory-update stubs at the ideas list**

In `references/theory-update.md`, rule 7 currently reads "Propose at most three
next stubs per update." Extend it so the stubs have a destination: they are
recorded in the project `ideas.md`, and the two artifacts stay consistent.
Leave the rest of rule 7 unchanged — stubs remain inputs to a future Theorist
pass, not self-authorizing.

Add `ideas.md` to the `## Changelog Entry` list so each theory update records
which ideas it added or closed.

- [ ] **Step 4: Run the verification checks**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis
grep -q '## Project Ideas List' references/analysis-artifact-contract.md && echo "section OK"
grep -q 'project root' references/analysis-artifact-contract.md && echo "location OK"
grep -q 'never silently deleted' references/analysis-artifact-contract.md && echo "status OK"
grep -q 'instrument-validation.md' references/analysis-artifact-contract.md && echo "ladder link OK"
grep -q 'ideas.md' references/theory-update.md && echo "stub destination OK"
grep -nE '\b[Ss]hould\b' references/analysis-artifact-contract.md references/theory-update.md
```

Expected: five `OK` lines. The final grep must print nothing — note that
`analysis-artifact-contract.md:41` currently contains "`summary.md` should
state:". Change it to "`summary.md` states:" as part of this task, since you
are already editing this file.

- [ ] **Step 5: Verify links resolve**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis/references
for src in analysis-artifact-contract.md theory-update.md; do
  grep -o '](\([a-z0-9-]*\.md\)[^)]*)' "$src" | sed 's/](\([^)#]*\).*/\1/' | sort -u | while read -r f; do
    test -f "$f" || echo "BROKEN LINK in $src: $f"
  done
done
```

Expected: no output.

- [ ] **Step 6: Commit**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills
git add scientific-research-data-analysis/references/analysis-artifact-contract.md scientific-research-data-analysis/references/theory-update.md
git commit -m "Specify project-level ideas list and point theory stubs at it"
```

---

### Task 5: Remaining reference file edits

**Files:**
- Modify: `scientific-research-data-analysis/references/soul-roles.md`
- Modify: `scientific-research-data-analysis/references/adversarial-review.md`
- Modify: `scientific-research-data-analysis/references/interpretation-rules.md`
- Modify: `scientific-research-data-analysis/references/statistician-review.md`
- Read for content: spec §8 (the four corresponding rows)

**Interfaces:**
- Consumes: `references/instrument-validation.md` (Task 1) and
  `references/claim-discipline.md` (Task 2) — this task links to both. The
  step 2 wording must match Task 3's: "drafts and defends the proposal".
- Produces: nothing later tasks depend on.

- [ ] **Step 1: soul-roles.md**

Three edits:

1. In `## Step-To-Role Map`, the step 2 row currently reads
   "Orchestrator interviews". Change the row's role cell to
   "Orchestrator drafts and defends the proposal".
2. In `## Roles`, the Analyst bullet gains ownership of
   `[instrument-validation.md](instrument-validation.md)`.
3. In `## Roles`, the Adversary bullet gains re-check of the instrument record.

Leave `## Executing Roles As One Agent`, `## Handoff Rule`, and `## Gates`
unchanged.

- [ ] **Step 2: adversarial-review.md**

Three edits:

1. In `## Checklist`, add an item: the instrument record is current — every
   stage holds a PASS, no stage is STALE, and the chain's `validated_at`
   ordering is consistent. Link
   `[instrument-validation.md](instrument-validation.md)`.
2. Add a `## Reviewer Composition` section stating the two required
   properties: at least one reviewer generates new measurements rather than
   only reading documents, and at least one forms its verdict from raw
   artifacts without the analyst's conclusions.
3. In `## Verdicts`, add: every review finding ships with the exact command or
   query that produced each number.

- [ ] **Step 3: interpretation-rules.md**

Two edits:

1. Add a `## Reporting Posture` section: the headline states the worst
   defensible reading of the data; deviations from the frozen plan are
   disclosed; an analysis tuned after seeing its results is reported as such,
   with the number of configurations tried; messy or inconclusive results are
   reported as messy or inconclusive.
2. In `## Labels`, add a cross-reference to the epistemic tiers in
   `[claim-discipline.md](claim-discipline.md)`, noting the distinction: the
   labels here classify an *analysis*, the tiers there classify a *statement*.

- [ ] **Step 4: statistician-review.md**

Two edits:

1. In `## Post-Result Review`, add degenerate-output detection: a test that
   returns a constant, a filter that passes or fails everything, an exactly
   zero statistic, a perfect metric, or an all-NaN result is treated as a bug
   until investigated. Link
   `[instrument-validation.md](instrument-validation.md)`.
2. Line 19 currently reads "Each finding should include severity, reason, and
   concrete fix." Change to "Each finding includes severity, reason, and
   concrete fix."

- [ ] **Step 5: Run the verification checks**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis
grep -q 'drafts and defends the proposal' references/soul-roles.md && echo "step2 wording OK"
grep -q 'instrument-validation.md' references/soul-roles.md && echo "analyst owns OK"
grep -q '## Reviewer Composition' references/adversarial-review.md && echo "reviewers OK"
grep -q 'exact command or query' references/adversarial-review.md && echo "findings OK"
grep -q '## Reporting Posture' references/interpretation-rules.md && echo "posture OK"
grep -q 'claim-discipline.md' references/interpretation-rules.md && echo "tiers link OK"
grep -q 'instrument-validation.md' references/statistician-review.md && echo "degenerate OK"
grep -q 'Orchestrator interviews' references/soul-roles.md && echo "FAIL: old wording survives"
grep -nE '\b[Ss]hould\b' references/soul-roles.md references/adversarial-review.md references/interpretation-rules.md references/statistician-review.md
```

Expected: seven `OK` lines, no `FAIL` line, final grep prints nothing.

- [ ] **Step 6: Verify links resolve**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis/references
for src in soul-roles.md adversarial-review.md interpretation-rules.md statistician-review.md; do
  grep -o '](\([a-z0-9-]*\.md\)[^)]*)' "$src" | sed 's/](\([^)#]*\).*/\1/' | sort -u | while read -r f; do
    test -f "$f" || echo "BROKEN LINK in $src: $f"
  done
done
```

Expected: no output.

- [ ] **Step 7: Commit**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills
git add scientific-research-data-analysis/references/
git commit -m "Wire instrument validation and claim discipline into review references"
```

---

### Task 6: Instrument chain validation in the scripts

This is the only task with executable code, and the only one using real TDD.

**Files:**
- Create: `scientific-research-data-analysis/scripts/test_validate_analysis_config.py`
- Modify: `scientific-research-data-analysis/scripts/validate_analysis_config.py`
- Modify: `scientific-research-data-analysis/scripts/init_analysis.py`
- Read for content: spec §6.4 (record schema), §6.3.1 and §6.3.2 (chain rules), §9 (script checks)

**Interfaces:**
- Consumes: the twelve-key record schema written in Task 1's "Instrument
  Record" section, and the `ideas.md` column headers from Task 4.
- Produces:
  - `validate_instruments(instruments: list) -> None` in
    `validate_analysis_config.py` — raises `SystemExit` with a message on any
    violation, returns `None` on success.
  - `ALLOWED_STATUS: set[str]` = `{"PASS", "PENDING", "FAIL", "STALE"}`
  - `REQUIRED_INSTRUMENT_KEYS: set[str]` — the twelve keys.
  - `"instruments"` added to `REQUIRED_TOP_LEVEL`.

- [ ] **Step 1: Write the failing tests**

Create `scientific-research-data-analysis/scripts/test_validate_analysis_config.py`:

```python
#!/usr/bin/env python3
"""Tests for validate_analysis_config.py.

Run: python3 -m unittest discover -s scripts -p 'test_*.py' -v
Standard library only; no third-party test runner.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "validate_analysis_config.py"


def stage(position, name, consumes, validated_at, status="PASS"):
    """Build one well-formed instrument record."""
    return {
        "stage": name,
        "position": position,
        "consumes": consumes,
        "name": name,
        "version": "1.0.0",
        "install_source": "pypi",
        "parameters": {},
        "input_ref": "sources[0]" if consumes is None else consumes,
        "runtime_s": 1.5,
        "output_shape": "[64, 1000]",
        "validated_at": validated_at,
        "status": status,
    }


def config_with(instruments):
    return {
        "analysis_id": "H-2026-001",
        "status": "draft",
        "sources": [],
        "frozen_decisions": {},
        "compute_gates": {},
        "required_outputs": [],
        "interpretation": "unfrozen",
        "instruments": instruments,
    }


def run(config):
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "config.json"
        path.write_text(json.dumps(config), encoding="utf-8")
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(path)],
            capture_output=True,
            text=True,
        )


CHAIN = [
    stage(0, "filter", None, "2026-08-19T10:00:00+00:00"),
    stage(1, "ica", "filter", "2026-08-19T11:00:00+00:00"),
    stage(2, "epoch", "ica", "2026-08-19T12:00:00+00:00"),
]


class TestInstrumentsBlock(unittest.TestCase):
    def test_missing_instruments_key_fails(self):
        config = config_with([])
        del config["instruments"]
        result = run(config)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("instruments", result.stderr)

    def test_empty_instruments_list_passes(self):
        result = run(config_with([]))
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_wellformed_chain_passes(self):
        result = run(config_with(CHAIN))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PASS", result.stdout)

    def test_missing_key_fails(self):
        broken = [dict(CHAIN[0])]
        del broken[0]["output_shape"]
        result = run(config_with(broken))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("output_shape", result.stderr)

    def test_invalid_status_fails(self):
        broken = [stage(0, "filter", None, "2026-08-19T10:00:00+00:00", status="OK")]
        result = run(config_with(broken))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("status", result.stderr)

    def test_unparseable_validated_at_fails(self):
        broken = [stage(0, "filter", None, "yesterday")]
        result = run(config_with(broken))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("validated_at", result.stderr)


class TestChainShape(unittest.TestCase):
    def test_duplicate_position_fails(self):
        broken = [
            stage(0, "filter", None, "2026-08-19T10:00:00+00:00"),
            stage(0, "ica", "filter", "2026-08-19T11:00:00+00:00"),
        ]
        result = run(config_with(broken))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("position", result.stderr)

    def test_gap_in_positions_fails(self):
        broken = [
            stage(0, "filter", None, "2026-08-19T10:00:00+00:00"),
            stage(2, "ica", "filter", "2026-08-19T11:00:00+00:00"),
        ]
        result = run(config_with(broken))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("position", result.stderr)

    def test_consumes_unknown_stage_fails(self):
        broken = [
            stage(0, "filter", None, "2026-08-19T10:00:00+00:00"),
            stage(1, "ica", "nonexistent", "2026-08-19T11:00:00+00:00"),
        ]
        result = run(config_with(broken))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("nonexistent", result.stderr)

    def test_first_stage_with_consumes_fails(self):
        broken = [stage(0, "filter", "ghost", "2026-08-19T10:00:00+00:00")]
        result = run(config_with(broken))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("consumes", result.stderr)

    def test_later_stage_without_consumes_fails(self):
        broken = [
            stage(0, "filter", None, "2026-08-19T10:00:00+00:00"),
            stage(1, "ica", None, "2026-08-19T11:00:00+00:00"),
        ]
        result = run(config_with(broken))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("consumes", result.stderr)

    def test_cycle_fails(self):
        broken = [
            stage(0, "filter", None, "2026-08-19T10:00:00+00:00"),
            stage(1, "ica", "epoch", "2026-08-19T11:00:00+00:00"),
            stage(2, "epoch", "ica", "2026-08-19T12:00:00+00:00"),
        ]
        result = run(config_with(broken))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("cycle", result.stderr.lower())


class TestCascade(unittest.TestCase):
    def test_downstream_validated_before_upstream_is_stale(self):
        broken = [
            stage(0, "filter", None, "2026-08-19T14:00:00+00:00"),
            stage(1, "ica", "filter", "2026-08-19T11:00:00+00:00"),
        ]
        result = run(config_with(broken))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("STALE", result.stderr)

    def test_pass_downstream_of_pending_fails(self):
        broken = [
            stage(0, "filter", None, "2026-08-19T10:00:00+00:00", status="PENDING"),
            stage(1, "ica", "filter", "2026-08-19T11:00:00+00:00", status="PASS"),
        ]
        result = run(config_with(broken))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("PENDING", result.stderr)

    def test_pending_downstream_of_pass_is_allowed(self):
        ok = [
            stage(0, "filter", None, "2026-08-19T10:00:00+00:00", status="PASS"),
            stage(1, "ica", "filter", "2026-08-19T11:00:00+00:00", status="PENDING"),
        ]
        result = run(config_with(ok))
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the tests to verify they fail**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis
python3 -m unittest discover -s scripts -p 'test_*.py' -v
```

Expected: FAIL. `test_missing_instruments_key_fails` and
`test_empty_instruments_list_passes` will not both hold, and every chain test
fails, because `validate_analysis_config.py` does not yet know about
`instruments`.

- [ ] **Step 3: Implement the validator changes**

In `scripts/validate_analysis_config.py`:

Add to the imports:

```python
from datetime import datetime
```

Add `"instruments"` to `REQUIRED_TOP_LEVEL`, and add these module constants
after it:

```python
ALLOWED_STATUS = {"PASS", "PENDING", "FAIL", "STALE"}

REQUIRED_INSTRUMENT_KEYS = {
    "stage",
    "position",
    "consumes",
    "name",
    "version",
    "install_source",
    "parameters",
    "input_ref",
    "runtime_s",
    "output_shape",
    "validated_at",
    "status",
}
```

Add this function above `main()`:

```python
def parse_time(value: str, label: str) -> datetime:
    try:
        return datetime.fromisoformat(value)
    except (TypeError, ValueError):
        raise SystemExit(f"{label} validated_at is not ISO-8601: {value!r}")


def validate_instruments(instruments: object) -> None:
    """Validate the instrument chain. Raises SystemExit on any violation."""
    if not isinstance(instruments, list):
        raise SystemExit("instruments must be a list")
    if not instruments:
        return

    by_stage: dict[str, dict] = {}
    for index, record in enumerate(instruments):
        label = f"instruments[{index}]"
        if not isinstance(record, dict):
            raise SystemExit(f"{label} must be an object")
        missing = sorted(REQUIRED_INSTRUMENT_KEYS - set(record))
        if missing:
            raise SystemExit(f"{label} missing keys: {', '.join(missing)}")
        if record["status"] not in ALLOWED_STATUS:
            raise SystemExit(
                f"{label} status must be one of {sorted(ALLOWED_STATUS)}, "
                f"got {record['status']!r}"
            )
        parse_time(record["validated_at"], label)
        if record["stage"] in by_stage:
            raise SystemExit(f"duplicate stage name: {record['stage']}")
        by_stage[record["stage"]] = record

    positions = sorted(record["position"] for record in instruments)
    if positions != list(range(len(instruments))):
        raise SystemExit(
            f"instrument position values must be contiguous from 0, got {positions}"
        )

    ordered = sorted(instruments, key=lambda record: record["position"])
    for record in ordered:
        upstream_name = record["consumes"]
        if record["position"] == 0:
            if upstream_name is not None:
                raise SystemExit(
                    f"first stage {record['stage']} must have consumes: null"
                )
            continue
        if upstream_name is None:
            raise SystemExit(
                f"stage {record['stage']} must name an upstream stage in consumes"
            )
        if upstream_name not in by_stage:
            raise SystemExit(
                f"stage {record['stage']} consumes unknown stage: {upstream_name}"
            )
        if by_stage[upstream_name]["position"] >= record["position"]:
            raise SystemExit(
                f"cycle: stage {record['stage']} consumes {upstream_name}, "
                "which is not upstream of it"
            )

    for record in ordered:
        if record["consumes"] is None:
            continue
        upstream = by_stage[record["consumes"]]
        own = parse_time(record["validated_at"], record["stage"])
        up = parse_time(upstream["validated_at"], upstream["stage"])
        if own < up:
            raise SystemExit(
                f"stage {record['stage']} is STALE: validated at {record['validated_at']} "
                f"but upstream {upstream['stage']} was validated later at "
                f"{upstream['validated_at']}"
            )
        if record["status"] == "PASS" and upstream["status"] != "PASS":
            raise SystemExit(
                f"stage {record['stage']} cannot be PASS while upstream "
                f"{upstream['stage']} is {upstream['status']}"
            )
```

In `main()`, after the existing `required_outputs` type check and before the
`--check-files` block, add:

```python
    validate_instruments(config["instruments"])
```

Replace the final `print("PASS")` with a chain-state report that keeps `PASS`
in the output so existing usage is unaffected:

```python
    instruments = config["instruments"]
    if instruments:
        states = {record["status"] for record in instruments}
        chain = "PASS" if states == {"PASS"} else "INCOMPLETE"
        print(f"PASS (instrument chain: {chain}, {len(instruments)} stages)")
    else:
        print("PASS (no instruments recorded)")
```

- [ ] **Step 4: Run the tests to verify they pass**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis
python3 -m unittest discover -s scripts -p 'test_*.py' -v
```

Expected: PASS — 15 tests, `OK`.

- [ ] **Step 5: Update the scaffold script**

In `scripts/init_analysis.py`, two changes.

First, add `"instruments": []` to the config template dict, immediately after
`"required_outputs": []`, so a freshly scaffolded config validates:

```python
                    "required_outputs": [],
                    "instruments": [],
                    "interpretation": "unfrozen",
```

Second, create the project ideas list. Add this argument next to the existing
`--root` argument:

```python
    parser.add_argument("--project-root", type=Path, default=Path("."))
```

and add this block immediately before the final `print(root)`:

```python
    ideas = args.project_root / "ideas.md"
    if not ideas.exists():
        ideas.write_text(
            "\n".join(
                [
                    "# Project Ideas",
                    "",
                    "Ranked candidate directions not in any current plan.",
                    "Written while discussing results, during analysis, at data",
                    "audit, and at theory update. Read when an analysis stalls,",
                    "when a method is dropped, and at every theory update.",
                    "",
                    "Status: open | in progress | done (<analysis-id>) |",
                    "dropped (<reason>). An idea is never silently deleted.",
                    "",
                    "| Rank | Idea | Rationale | Rough cost | Status |",
                    "|---|---|---|---|---|",
                    "",
                ]
            ),
            encoding="ascii",
        )
```

- [ ] **Step 6: Verify the scaffold end to end**

```bash
cd "$(mktemp -d)"
python3 /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis/scripts/init_analysis.py H-2026-001
test -f ideas.md && echo "ideas.md created"
grep -q '| Rank | Idea | Rationale | Rough cost | Status |' ideas.md && echo "headers OK"
python3 /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis/scripts/validate_analysis_config.py analyses/H-2026-001/config.json
```

Expected: `ideas.md created`, `headers OK`, and
`PASS (no instruments recorded)`.

- [ ] **Step 7: Commit**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills
git add scientific-research-data-analysis/scripts/
git commit -m "Validate instrument chain and scaffold the project ideas list"
```

---

### Task 7: Style pass and acceptance verification

**Files:**
- Modify: any file where the sweep below reports a soft preference
- Read: spec §10 and §11

**Interfaces:**
- Consumes: every artifact from Tasks 1-6.
- Produces: nothing.

- [ ] **Step 1: Sweep for soft-preference language**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis
grep -rniE '\b(should|prefer|preferably|try to|when possible|if possible|ideally)\b' SKILL.md references/
```

Review each hit. A hit survives only when it reads as a gate or a bounded
permission in context — for example `interpretation-rules.md`'s "Prefer" inside
a rule that also states the prohibition. Rewrite every hit that reads as a soft
preference: turn it into a gate ("X does not count as done unless…") or a
bounded permission ("you may X, provided Y").

Known hits from the spec-time survey, both already handled in earlier tasks —
confirm they are gone: `analysis-artifact-contract.md:41` and
`statistician-review.md:19`.

- [ ] **Step 2: Verify every acceptance criterion from spec §11**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis

echo "--- 1. new reference files exist and are linked ---"
test -f references/instrument-validation.md && test -f references/claim-discipline.md && echo OK
grep -q 'references/instrument-validation.md' SKILL.md && grep -q 'references/claim-discipline.md' SKILL.md && echo OK

echo "--- 2. operating rule ---"
grep -q 'A default may be filled, never silently' SKILL.md && echo OK
grep -q 'plan.md' SKILL.md && grep -q 'before outcome inspection' SKILL.md && echo "freeze rule OK"

echo "--- 3. gate ---"
grep -q 'Silence is not confirmation' references/common-understanding-gate.md && echo OK
grep -q 'because you chose' references/common-understanding-gate.md && echo "derived OK"

echo "--- 4. no soft should ---"
grep -rniE '\b(should|prefer|try to|when possible|ideally)\b' SKILL.md references/ || echo "clean"

echo "--- 5 and 5a. validator ---"
python3 -m unittest discover -s scripts -p 'test_*.py' 2>&1 | tail -3

echo "--- 6. ideas list ---"
grep -q '## Project Ideas List' references/analysis-artifact-contract.md && echo OK
grep -q 'ideas.md' references/theory-update.md && echo "stubs OK"

echo "--- 7. all links resolve ---"
cd references
for src in *.md; do
  grep -o '](\([a-z0-9-]*\.md\)[^)]*)' "$src" | sed 's/](\([^)#]*\).*/\1/' | sort -u | while read -r f; do
    test -f "$f" || echo "BROKEN LINK in $src: $f"
  done
done
cd ..
grep -o '](references/[a-z0-9-]*\.md)' SKILL.md | sed 's/](\(.*\))/\1/' | sort -u | while read -r f; do
  test -f "$f" || echo "BROKEN LINK in SKILL.md: $f"
done
echo "link check done"
```

Expected: every `OK` line prints; the criterion-4 grep prints `clean` or only
context-justified hits; unittest reports `OK`; no `BROKEN LINK` lines.

- [ ] **Step 3: Confirm the skill frontmatter still parses**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis
head -5 SKILL.md
```

Expected: the file still opens with `---`, then `name:` and `description:`,
then `---`. The description field is unchanged by this upgrade — it already
covers the added material.

- [ ] **Step 4: Commit**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills
git add -A scientific-research-data-analysis/
git commit -m "Style pass: convert remaining soft preferences to gates"
```

---

## Self-Review Record

**Spec coverage:** §5.1 → Task 3 Steps 2-3. §5.2 → Task 3 Step 4. §6.1-6.9 →
Task 1. §6.4 schema → Task 1 Step 2 and Task 6 Step 3. §6.3.1-6.3.2 → Task 1
Step 2 and Task 6 Steps 1/3. §7 → Task 2. §8 `SKILL.md` row → Task 3 Steps 2-3.
§8 `soul-roles`/`adversarial-review`/`interpretation-rules`/`statistician-review`
rows → Task 5. §8.1 → Task 4 and Task 6 Step 5. §8 `theory-update` row → Task 4
Step 3. §9 → Task 6. §10 → Task 7 Step 1. §11 → Task 7 Step 2.

**Type consistency:** `validate_instruments` is defined in Task 6 Step 3 and
called in the same step. `ALLOWED_STATUS` and `REQUIRED_INSTRUMENT_KEYS` are
defined once and used only there. The twelve record keys in Task 1 Step 2, Task
6 Step 1's `stage()` helper, and Task 6 Step 3's `REQUIRED_INSTRUMENT_KEYS` are
the same twelve. The `ideas.md` column headers in Task 4 Step 2 and Task 6 Step
5 match. The step 2 role wording "drafts and defends the proposal" is written
in Task 3 and asserted in Task 5.

**Known limitation:** the markdown tasks verify structure and required phrases
by grep, not prose quality. A human or reviewing agent reads the resulting
prose; grep only proves the load-bearing sentences are present.
