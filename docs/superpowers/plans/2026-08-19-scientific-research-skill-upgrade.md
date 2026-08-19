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

The "Instrument Record" section documents a **two-file split** (spec 6.4). Read
that spec section carefully — the record does not live in one place, because
its two halves have different lifetimes:

- **Declared, in frozen `config.json` under key `instruments`** — exactly these
  seven keys: `stage`, `position`, `consumes`, `name`, `version`,
  `install_source`, `parameters`.
- **Observed, in mutable `gate_status.json` under key `instrument_status`** —
  exactly these six keys: `stage`, `status`, `validated_at`, `runtime_s`,
  `output_shape`, `input_ref`.

State the reason for the split explicitly in the prose: `config.json` is frozen
before outcome inspection, and instrument status changes throughout the work as
stages move PENDING to PASS and cascades mark stages STALE. Mutable state in a
frozen file would contradict the freeze rule. Also state the agreement rule:
both files name the same set of stages.

Cross-link `interpretation-rules.md` from the Method Tiering section (the
Diagnostic tier is defined there), `data-contract.md` from the Instrument
Record section (first-stage `input_ref` points at a data-contract entry), and
`analysis-artifact-contract.md` from the Instrument Record section (both files
are Required Files there).

- [ ] **Step 3: Run the verification checks**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis
grep -c '^## ' references/instrument-validation.md
grep -q 'A generator is not its own evaluator' references/instrument-validation.md && echo "lede OK"
grep -q 'PENDING' references/instrument-validation.md && echo "pending OK"
grep -q 'log the drop with its consequence stated' references/instrument-validation.md && echo "ladder OK"
for k in stage position consumes name version install_source parameters input_ref runtime_s output_shape validated_at status instrument_status gate_status.json; do
  grep -q "$k" references/instrument-validation.md || echo "MISSING KEY: $k"
done
grep -q 'frozen' references/instrument-validation.md && echo "split rationale OK"
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

In the "Lead With The Unfavorable Reading" section, add one sentence tying the
configuration count to analysis families: where the analysis belongs to a
family declared in `config.json`, the count is the family size at write time,
not a recollection. Do not link `interpretation-rules.md` for this — a later
task adds the family rule there and the cross-link belongs in that direction.

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

- [ ] **Step 2b: Correct the contract drift**

Read spec §8.2. A real analysis folder contains `gate_status.json` and
`final_report.md`, which appear nowhere in this skill, and lacks `summary.md`,
which the contract requires. The contract adopts observed reality. In
`references/analysis-artifact-contract.md`:

1. Add `gate_status.json` to `## Required Files`: records gate outcomes and
   carries the `instrument_status` array defined in
   `[instrument-validation.md](instrument-validation.md)`. Keys beyond
   `instrument_status` are permitted and unvalidated. Note that unlike
   `config.json` it is mutable — it records results, not frozen decisions.
2. Rename `summary.md` to `final_report.md` in the `## Required Files` entry
   and in the `## Result Summary` section. The content requirements are
   unchanged; only the filename moves.
3. In `## Required Files`, add the declared `instruments` key to the
   `config.json` entry's description.

Do not touch `soul-roles.md` here — Task 5 owns that file and renames its
`summary.md` mention.

- [ ] **Step 2c: Add the canonical filename table**

Read spec 11.1. A survey of a real 52-analysis project found fourteen distinct
filenames carrying statistician-review output and about nineteen carrying
controller-audit output, including two spellings of the same artifact. A gate
whose output has no canonical name cannot be checked mechanically.

Add a `## Canonical Filenames` section to
`references/analysis-artifact-contract.md`, placed immediately after
`## Required Files`. Reproduce the table from spec 11.1 with these exact
filenames — each is the most frequent observed spelling, so adopting it costs
the least renaming:

| Artifact | Canonical filename |
|---|---|
| Data-contract audit (Scout) | `input_audit.md` / `input_audit.json` |
| Statistician pre-analysis review | `statistician_review.md` |
| Statistician post-result review | `statistician_post_result_review.md` |
| Adversarial review (Adversary) | `adversarial_review.md` |
| Freeze record | `freeze_manifest.json` |
| Gate outcomes and instrument status | `gate_status.json` |
| Result hashes | `result_manifest.json` |
| Final narrative | `final_report.md` |
| Theory-update entry | `lab_journal_entry.md` |

State the two rules that make the table binding:

- A review that ran under a different filename did not run, because it cannot
  be found.
- Where one analysis needs several instances of an artifact — per stage, per
  amendment — the canonical stem takes a suffix
  (`adversarial_review_<stage>.md`), never a new stem.

- [ ] **Step 2d: Add the analysis-family block**

Read spec 11.2. In `## Required Files`, extend the `config.json` description
with the `family` block: `family_id`, `parent_analysis`, `varies`. State the
rule: an analysis that changes a parameter of an earlier analysis addressing
the same question sets `parent_analysis` to that analysis id, shares its
`family_id`, and names the changed parameters in `varies`. State that every
family member's `final_report.md` records the family size at write time —
configuration k of n tried.

The interpretation consequence is written by Task 5 into
`interpretation-rules.md`; do not duplicate it here, cross-link it.

- [ ] **Step 3: Point theory-update stubs at the ideas list**

In `references/theory-update.md`, rule 7 currently reads "Propose at most three
next stubs per update." Extend it so the stubs have a destination: they are
recorded in the project `ideas.md`, and the two artifacts stay consistent.
Leave the rest of rule 7 unchanged — stubs remain inputs to a future Theorist
pass, not self-authorizing.

Add `ideas.md` to the `## Changelog Entry` list so each theory update records
which ideas it added or closed.

Then add a `## Journal And Theory Are Different Artifacts` section, from spec
11.4. The evidence: in the surveyed project the lab journal reached 403 KB and
5,746 lines and stayed current, while every file in `theory/` was frozen for a
month as roughly thirty analyses ran. Step 9 stopped executing and nothing
detected it. The section states:

- The **lab journal** is an append-only record. It grows without bound. It is
  written on every update and is not a decision aid.
- The **theory document** is current-state and bounded. It is **re-derived**,
  not appended to: superseded claims are removed or marked, never accumulated.
- Appending a journal entry does not satisfy step 9. A theory update that
  leaves the theory document unchanged states why in the journal entry, naming
  the artifact that failed to move it.

- [ ] **Step 4: Run the verification checks**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis
grep -q '## Project Ideas List' references/analysis-artifact-contract.md && echo "section OK"
grep -q 'project root' references/analysis-artifact-contract.md && echo "location OK"
grep -q 'never silently deleted' references/analysis-artifact-contract.md && echo "status OK"
grep -q 'instrument-validation.md' references/analysis-artifact-contract.md && echo "ladder link OK"
grep -q 'ideas.md' references/theory-update.md && echo "stub destination OK"
grep -q 'gate_status.json' references/analysis-artifact-contract.md && echo "gate_status OK"
grep -q 'final_report.md' references/analysis-artifact-contract.md && echo "report rename OK"
grep -q 'summary\.md' references/analysis-artifact-contract.md && echo "FAIL: summary.md survives"
grep -q '## Canonical Filenames' references/analysis-artifact-contract.md && echo "filename table OK"
for f in input_audit.md statistician_review.md statistician_post_result_review.md adversarial_review.md freeze_manifest.json result_manifest.json lab_journal_entry.md; do
  grep -q "$f" references/analysis-artifact-contract.md || echo "MISSING CANONICAL NAME: $f"
done
grep -q 'family_id' references/analysis-artifact-contract.md && echo "family block OK"
grep -q 'parent_analysis' references/analysis-artifact-contract.md && echo "parent OK"
grep -q 'append-only' references/theory-update.md && echo "journal split OK"
grep -q 're-derived' references/theory-update.md && echo "theory rederive OK"
grep -nE '\b[Ss]hould\b' references/analysis-artifact-contract.md references/theory-update.md
```

Expected: seven `OK` lines, no `FAIL` line. The final grep must print nothing — note that
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

Four edits:

1. In `## Step-To-Role Map`, the step 2 row currently reads
   "Orchestrator interviews". Change the row's role cell to
   "Orchestrator drafts and defends the proposal".
2. In `## Roles`, the Analyst bullet gains ownership of
   `[instrument-validation.md](instrument-validation.md)`.
3. In `## Roles`, the Adversary bullet gains re-check of the instrument record.
4. Line 24 of `## Roles` currently ends "manifests, logs, and `summary.md`."
   Change `summary.md` to `final_report.md`, matching the contract rename Task
   4 made. Add `gate_status.json` to that same Analyst list.

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
3. Add an `## Analysis Families` section, from spec 11.2. The evidence: in the
   surveyed project, nine analyses (`F007`-`F014`) addressed one question while
   varying exclusion threshold, sample size, and time window; the first
   declared `exploratory`, `selection-informed`, and a multiplicity claim, and
   the later ones declared none of them. No analysis anywhere stated how many
   configurations had been tried. The section states:
   - A member of a family larger than one is not labeled **confirmatory**
     unless the whole family was frozen before outcome access.
   - Absent that freeze, the family is **selection-informed**, and the family
     size at write time is reported alongside the result — configuration k of
     n tried.
   - The family is declared in `config.json`'s `family` block; cross-link
     `[analysis-artifact-contract.md](analysis-artifact-contract.md)`.
   Add a matching entry to `## Prohibited Moves`: do not report a family
   member's result without its family size.

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
grep -q '## Analysis Families' references/interpretation-rules.md && echo "families OK"
grep -q 'selection-informed' references/interpretation-rules.md && echo "selection OK"
grep -q 'instrument-validation.md' references/statistician-review.md && echo "degenerate OK"
grep -q 'final_report.md' references/soul-roles.md && echo "report rename OK"
grep -q 'Orchestrator interviews' references/soul-roles.md && echo "FAIL: old wording survives"
grep -q 'summary\.md' references/soul-roles.md && echo "FAIL: summary.md survives"
grep -nE '\b[Ss]hould\b' references/soul-roles.md references/adversarial-review.md references/interpretation-rules.md references/statistician-review.md
```

Expected: eight `OK` lines, no `FAIL` line, final grep prints nothing.

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

The record is split across two files (spec 6.4): the **declared** chain in
frozen `config.json`, the **observed** status in mutable `gate_status.json`.
Read spec 6.4 before starting.

**Files:**
- Create: `scientific-research-data-analysis/scripts/test_validate_analysis_config.py`
- Modify: `scientific-research-data-analysis/scripts/validate_analysis_config.py`
- Modify: `scientific-research-data-analysis/scripts/init_analysis.py`
- Read for content: spec 6.4 (two-file schema), 6.3.1 and 6.3.2 (chain rules), 8.2 (drift), 9 (script checks)

**Interfaces:**
- Consumes: the seven declared keys and six observed keys written in Task 1's
  "Instrument Record" section, and the `ideas.md` column headers from Task 4.
- Produces:
  - `validate_instruments(declared: list, observed: list) -> None` in
    `validate_analysis_config.py` — raises `SystemExit` on any violation,
    returns `None` on success.
  - `ALLOWED_STATUS` = `{"PASS", "PENDING", "FAIL", "STALE"}`
  - `DECLARED_KEYS` — the seven config keys.
  - `OBSERVED_KEYS` — the six gate-status keys.
  - `"instruments"` added to `REQUIRED_TOP_LEVEL`.
  - `--gate-status PATH` CLI flag, defaulting to `gate_status.json` beside the
    config.

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


def declared(position, name, consumes):
    """One well-formed entry for config.json's instruments array."""
    return {
        "stage": name,
        "position": position,
        "consumes": consumes,
        "name": name,
        "version": "1.0.0",
        "install_source": "pypi",
        "parameters": {},
    }


def observed(name, validated_at, status="PASS", consumes=None):
    """One well-formed entry for gate_status.json's instrument_status array."""
    return {
        "stage": name,
        "status": status,
        "validated_at": validated_at,
        "runtime_s": 1.5,
        "output_shape": "[64, 1000]",
        "input_ref": "sources[0]" if consumes is None else consumes,
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


def run(config, gate_status=None, write_gate_status=True):
    """Run the validator against a temp config, returning the CompletedProcess."""
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        config_path = base / "config.json"
        config_path.write_text(json.dumps(config), encoding="utf-8")
        if write_gate_status:
            payload = {"instrument_status": gate_status or []}
            (base / "gate_status.json").write_text(
                json.dumps(payload), encoding="utf-8"
            )
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(config_path)],
            capture_output=True,
            text=True,
        )


DECLARED_CHAIN = [
    declared(0, "filter", None),
    declared(1, "ica", "filter"),
    declared(2, "epoch", "ica"),
]

OBSERVED_CHAIN = [
    observed("filter", "2026-08-19T10:00:00+00:00"),
    observed("ica", "2026-08-19T11:00:00+00:00", consumes="filter"),
    observed("epoch", "2026-08-19T12:00:00+00:00", consumes="ica"),
]


class TestSchema(unittest.TestCase):
    def test_missing_instruments_key_names_the_fix(self):
        config = config_with([])
        del config["instruments"]
        result = run(config)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("instruments", result.stderr)

    def test_empty_chain_passes(self):
        result = run(config_with([]))
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_wellformed_chain_passes(self):
        result = run(config_with(DECLARED_CHAIN), OBSERVED_CHAIN)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PASS", result.stdout)

    def test_declared_missing_key_fails(self):
        broken = [dict(DECLARED_CHAIN[0])]
        del broken[0]["install_source"]
        result = run(config_with(broken), [OBSERVED_CHAIN[0]])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("install_source", result.stderr)

    def test_observed_missing_key_fails(self):
        broken = [dict(OBSERVED_CHAIN[0])]
        del broken[0]["output_shape"]
        result = run(config_with([DECLARED_CHAIN[0]]), broken)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("output_shape", result.stderr)

    def test_invalid_status_fails(self):
        broken = [observed("filter", "2026-08-19T10:00:00+00:00", status="OK")]
        result = run(config_with([DECLARED_CHAIN[0]]), broken)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("status", result.stderr)

    def test_unparseable_validated_at_fails(self):
        broken = [observed("filter", "yesterday")]
        result = run(config_with([DECLARED_CHAIN[0]]), broken)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("validated_at", result.stderr)


class TestTwoFileAgreement(unittest.TestCase):
    def test_missing_gate_status_file_names_the_fix(self):
        result = run(
            config_with([DECLARED_CHAIN[0]]), write_gate_status=False
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("gate_status.json", result.stderr)

    def test_declared_stage_without_observed_entry_fails(self):
        result = run(config_with(DECLARED_CHAIN), [OBSERVED_CHAIN[0]])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ica", result.stderr)

    def test_observed_entry_without_declared_stage_fails(self):
        extra = OBSERVED_CHAIN + [observed("ghost", "2026-08-19T13:00:00+00:00")]
        result = run(config_with(DECLARED_CHAIN), extra)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ghost", result.stderr)


class TestChainShape(unittest.TestCase):
    def test_duplicate_position_fails(self):
        broken = [declared(0, "filter", None), declared(0, "ica", "filter")]
        result = run(config_with(broken), OBSERVED_CHAIN[:2])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("position", result.stderr)

    def test_gap_in_positions_fails(self):
        broken = [declared(0, "filter", None), declared(2, "ica", "filter")]
        result = run(config_with(broken), OBSERVED_CHAIN[:2])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("position", result.stderr)

    def test_consumes_unknown_stage_fails(self):
        broken = [declared(0, "filter", None), declared(1, "ica", "nonexistent")]
        result = run(config_with(broken), OBSERVED_CHAIN[:2])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("nonexistent", result.stderr)

    def test_first_stage_with_consumes_fails(self):
        broken = [declared(0, "filter", "ghost")]
        result = run(config_with(broken), [OBSERVED_CHAIN[0]])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("consumes", result.stderr)

    def test_later_stage_without_consumes_fails(self):
        broken = [declared(0, "filter", None), declared(1, "ica", None)]
        result = run(config_with(broken), OBSERVED_CHAIN[:2])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("consumes", result.stderr)

    def test_cycle_fails(self):
        broken = [
            declared(0, "filter", None),
            declared(1, "ica", "epoch"),
            declared(2, "epoch", "ica"),
        ]
        result = run(config_with(broken), OBSERVED_CHAIN)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("cycle", result.stderr.lower())


class TestCascade(unittest.TestCase):
    def test_downstream_validated_before_upstream_is_stale(self):
        broken = [
            observed("filter", "2026-08-19T14:00:00+00:00"),
            observed("ica", "2026-08-19T11:00:00+00:00", consumes="filter"),
        ]
        result = run(config_with(DECLARED_CHAIN[:2]), broken)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("STALE", result.stderr)

    def test_pass_downstream_of_pending_fails(self):
        broken = [
            observed("filter", "2026-08-19T10:00:00+00:00", status="PENDING"),
            observed("ica", "2026-08-19T11:00:00+00:00", status="PASS", consumes="filter"),
        ]
        result = run(config_with(DECLARED_CHAIN[:2]), broken)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("PENDING", result.stderr)

    def test_pending_downstream_of_pass_is_allowed(self):
        ok = [
            observed("filter", "2026-08-19T10:00:00+00:00", status="PASS"),
            observed("ica", "2026-08-19T11:00:00+00:00", status="PENDING", consumes="filter"),
        ]
        result = run(config_with(DECLARED_CHAIN[:2]), ok)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("INCOMPLETE", result.stdout)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the tests to verify they fail**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis
python3 -m unittest discover -s scripts -p 'test_*.py' -v
```

Expected: FAIL — 19 tests run, most error out, because
`validate_analysis_config.py` does not yet know about `instruments`,
`gate_status.json`, or the `--gate-status` flag.

- [ ] **Step 3: Implement the validator changes**

In `scripts/validate_analysis_config.py`, add to the imports:

```python
from datetime import datetime
```

Add `"instruments"` to `REQUIRED_TOP_LEVEL`, and add these module constants
after it:

```python
ALLOWED_STATUS = {"PASS", "PENDING", "FAIL", "STALE"}

DECLARED_KEYS = {
    "stage",
    "position",
    "consumes",
    "name",
    "version",
    "install_source",
    "parameters",
}

OBSERVED_KEYS = {
    "stage",
    "status",
    "validated_at",
    "runtime_s",
    "output_shape",
    "input_ref",
}
```

Add these functions above `main()`:

```python
def parse_time(value: str, label: str) -> datetime:
    try:
        return datetime.fromisoformat(value)
    except (TypeError, ValueError):
        raise SystemExit(f"{label} validated_at is not ISO-8601: {value!r}")


def check_entries(records, required, kind):
    """Type-check one array and index it by stage name."""
    if not isinstance(records, list):
        raise SystemExit(f"{kind} must be a list")
    by_stage = {}
    for index, record in enumerate(records):
        label = f"{kind}[{index}]"
        if not isinstance(record, dict):
            raise SystemExit(f"{label} must be an object")
        missing = sorted(required - set(record))
        if missing:
            raise SystemExit(f"{label} missing keys: {', '.join(missing)}")
        if record["stage"] in by_stage:
            raise SystemExit(f"{kind} has duplicate stage name: {record['stage']}")
        by_stage[record["stage"]] = record
    return by_stage


def validate_instruments(declared: object, observed: object) -> None:
    """Validate the declared chain and its observed status. Raises SystemExit."""
    declared_by_stage = check_entries(declared, DECLARED_KEYS, "instruments")
    observed_by_stage = check_entries(
        observed, OBSERVED_KEYS, "instrument_status"
    )

    if not declared_by_stage:
        if observed_by_stage:
            raise SystemExit(
                "instrument_status records stages that config.json does not "
                f"declare: {', '.join(sorted(observed_by_stage))}"
            )
        return

    unobserved = sorted(set(declared_by_stage) - set(observed_by_stage))
    if unobserved:
        raise SystemExit(
            "declared stages have no instrument_status entry in "
            f"gate_status.json: {', '.join(unobserved)}"
        )
    undeclared = sorted(set(observed_by_stage) - set(declared_by_stage))
    if undeclared:
        raise SystemExit(
            "instrument_status records stages that config.json does not "
            f"declare: {', '.join(undeclared)}"
        )

    for stage_name, record in observed_by_stage.items():
        if record["status"] not in ALLOWED_STATUS:
            raise SystemExit(
                f"instrument_status[{stage_name}] status must be one of "
                f"{sorted(ALLOWED_STATUS)}, got {record['status']!r}"
            )
        parse_time(record["validated_at"], f"instrument_status[{stage_name}]")

    positions = sorted(record["position"] for record in declared)
    if positions != list(range(len(declared))):
        raise SystemExit(
            f"instrument position values must be contiguous from 0, got {positions}"
        )

    ordered = sorted(declared, key=lambda record: record["position"])
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
        if upstream_name not in declared_by_stage:
            raise SystemExit(
                f"stage {record['stage']} consumes unknown stage: {upstream_name}"
            )
        if declared_by_stage[upstream_name]["position"] >= record["position"]:
            raise SystemExit(
                f"cycle: stage {record['stage']} consumes {upstream_name}, "
                "which is not upstream of it"
            )

    for record in ordered:
        upstream_name = record["consumes"]
        if upstream_name is None:
            continue
        own = observed_by_stage[record["stage"]]
        up = observed_by_stage[upstream_name]
        if parse_time(own["validated_at"], record["stage"]) < parse_time(
            up["validated_at"], upstream_name
        ):
            raise SystemExit(
                f"stage {record['stage']} is STALE: validated at "
                f"{own['validated_at']} but upstream {upstream_name} was "
                f"validated later at {up['validated_at']}"
            )
        if own["status"] == "PASS" and up["status"] != "PASS":
            raise SystemExit(
                f"stage {record['stage']} cannot be PASS while upstream "
                f"{upstream_name} is {up['status']}"
            )
```

Add the CLI flag next to the existing arguments in `main()`:

```python
    parser.add_argument("--gate-status", type=Path, default=None)
```

In `main()`, after the existing `required_outputs` type check and before the
`--check-files` block, add:

```python
    declared = config["instruments"]
    gate_path = args.gate_status or args.config.parent / "gate_status.json"
    if not isinstance(declared, list):
        raise SystemExit("instruments must be a list")
    if declared and not gate_path.is_file():
        raise SystemExit(
            f"gate_status.json not found at {gate_path}; create it containing "
            '{"instrument_status": []} and record one entry per declared stage'
        )
    if gate_path.is_file():
        gate_status = json.loads(gate_path.read_text(encoding="utf-8"))
        observed = gate_status.get("instrument_status", [])
    else:
        observed = []
    validate_instruments(declared, observed)
```

Replace the final `print("PASS")` with a chain-state report that keeps `PASS`
in the output so existing usage is unaffected:

```python
    if declared:
        states = {record["status"] for record in observed}
        chain = "PASS" if states == {"PASS"} else "INCOMPLETE"
        print(f"PASS (instrument chain: {chain}, {len(declared)} stages)")
    else:
        print("PASS (no instruments recorded)")
```

Note the legacy path: a `config.json` written before this upgrade has no
`instruments` key, so `REQUIRED_TOP_LEVEL` rejects it with
`missing required config keys: instruments`. That message is the migration
instruction — add `"instruments": []` to the config and create a
`gate_status.json` containing `{"instrument_status": []}`.

- [ ] **Step 4: Run the tests to verify they pass**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis
python3 -m unittest discover -s scripts -p 'test_*.py' -v
```

Expected: PASS — 19 tests, `OK`.

- [ ] **Step 5: Update the scaffold script**

In `scripts/init_analysis.py`, four changes.

First, drop `audits` from the directory loop (spec 8.2 — nothing uses it):

```python
    for name in ("code", "results", "tests"):
```

Second, add `"instruments": []` to the config template dict, immediately after
`"required_outputs": []`:

```python
                    "required_outputs": [],
                    "instruments": [],
                    "interpretation": "unfrozen",
```

Third, create `gate_status.json` beside `config.json`. Add this block after the
config-writing block:

```python
    gate_status = root / "gate_status.json"
    if not gate_status.exists():
        gate_status.write_text(
            json.dumps({"gates": {}, "instrument_status": []}, indent=2) + "\n",
            encoding="ascii",
        )
```

Fourth, create the project ideas list. Add this argument next to `--root`:

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

- [ ] **Step 5b: Enforce unique analysis ids**

Read spec 11.3. The surveyed project contains two directories named `F014_…`
and two named `F030_…`; ids are hand-assigned and collide. In
`init_analysis.py`, add this check immediately after `root` is computed and
before any directory is created:

```python
    if root.exists():
        raise SystemExit(f"analysis id already exists: {root}")
    prefix = args.analysis_id.split("_")[0]
    clashes = sorted(
        sibling.name
        for sibling in args.root.glob(f"{prefix}_*")
        if sibling.is_dir()
    )
    if clashes:
        raise SystemExit(
            f"analysis id prefix {prefix!r} is already taken by: "
            f"{', '.join(clashes)}; a variant takes its own id and records "
            "parent_analysis in config.json"
        )
```

Add `"family": {"family_id": None, "parent_analysis": None, "varies": []}` to
the config template, immediately after `"instruments": []`.

- [ ] **Step 5c: Validate the family block and test both new rules**

In `validate_analysis_config.py`, add `"family"` to `REQUIRED_TOP_LEVEL` and
add this check in `main()` immediately after the `validate_instruments` call:

```python
    family = config["family"]
    if not isinstance(family, dict):
        raise SystemExit("family must be an object")
    missing = sorted({"family_id", "parent_analysis", "varies"} - set(family))
    if missing:
        raise SystemExit(f"family missing keys: {', '.join(missing)}")
    if not isinstance(family["varies"], list):
        raise SystemExit("family.varies must be a list")
    if family["parent_analysis"] and not family["family_id"]:
        raise SystemExit(
            "family.parent_analysis is set without family_id; a variant shares "
            "its parent's family_id"
        )
```

Add `"family": {"family_id": None, "parent_analysis": None, "varies": []}` to
the `config_with()` helper in the test file, then append this test class:

```python
class TestFamily(unittest.TestCase):
    def test_missing_family_key_fails(self):
        config = config_with([])
        del config["family"]
        result = run(config)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("family", result.stderr)

    def test_parent_without_family_id_fails(self):
        config = config_with([])
        config["family"] = {
            "family_id": None,
            "parent_analysis": "F007",
            "varies": ["threshold"],
        }
        result = run(config)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("family_id", result.stderr)

    def test_wellformed_family_passes(self):
        config = config_with([])
        config["family"] = {
            "family_id": "memory_performance",
            "parent_analysis": "F007",
            "varies": ["exclusion_threshold", "tmax"],
        }
        result = run(config)
        self.assertEqual(result.returncode, 0, result.stderr)
```

Run `python3 -m unittest discover -s scripts -p 'test_*.py' -v`.
Expected: PASS — 22 tests, `OK`.

Then verify the id checks by hand:

```bash
cd "$(mktemp -d)"
SKILL=/Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis
python3 "$SKILL/scripts/init_analysis.py" F014_first
python3 "$SKILL/scripts/init_analysis.py" F014_second 2>&1 | grep -q 'already taken' && echo "prefix clash rejected OK"
python3 "$SKILL/scripts/init_analysis.py" F014_first 2>&1 | grep -qE 'already exists|already taken' && echo "duplicate rejected OK"
```

Expected: both `OK` lines.

- [ ] **Step 6: Verify the scaffold end to end**

```bash
cd "$(mktemp -d)"
SKILL=/Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills/scientific-research-data-analysis
python3 "$SKILL/scripts/init_analysis.py" H-2026-001
test -f ideas.md && echo "ideas.md created"
grep -q '| Rank | Idea | Rationale | Rough cost | Status |' ideas.md && echo "headers OK"
test -f analyses/H-2026-001/gate_status.json && echo "gate_status.json created"
test -d analyses/H-2026-001/audits && echo "FAIL: audits still created" || echo "audits dropped OK"
python3 "$SKILL/scripts/validate_analysis_config.py" analyses/H-2026-001/config.json
```

Expected: `ideas.md created`, `headers OK`, `gate_status.json created`,
`audits dropped OK`, and `PASS (no instruments recorded)`.

- [ ] **Step 7: Commit**

```bash
cd /Users/nikolaj_syrov/Documents/GitHub/Neuroscience-Agent-Skills
git add scientific-research-data-analysis/scripts/
git commit -m "Validate the instrument chain across config and gate_status"
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

echo "--- 5b. two-file split ---"
grep -q 'gate_status.json' references/instrument-validation.md && echo OK
grep -q 'instrument_status' references/instrument-validation.md && echo "observed key OK"

echo "--- 5c. contract matches reality ---"
grep -q 'gate_status.json' references/analysis-artifact-contract.md && echo OK
grep -q 'final_report.md' references/analysis-artifact-contract.md && echo "report OK"
grep -rq 'summary\.md' SKILL.md references/ && echo "FAIL: summary.md survives" || echo "rename complete"
grep -q 'audits' scripts/init_analysis.py && echo "FAIL: audits survives" || echo "audits dropped"

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
