# Instrument Validation

Confirm that every tool in the pipeline does what it claims on this project's
data, not on its own say-so. The Analyst owns this file: it applies the rule
while implementing each stage. The Adversary re-checks it at SKILL.md step 7,
against the frozen instrument record, not against the Analyst's narrative.

## A Generator Is Not Its Own Evaluator

**A generator is not its own evaluator.** Whatever produced a result does not
get to be the sole judge of it. In practice:

- A model's own fit statistics are not validation of that model.
- An artifact-removal step is not confirmed by the metric that step optimized.
- A pipeline's own QC panel is not sole evidence the pipeline worked.

Independent evaluation means a different instrument, a held-out measurement,
or a check the generating procedure did not optimize.

## When The Gate Fires

A stage passes validation the first time the project depends on it for a
result, and again whenever any of these change: tool version, parameters, or
input data regime. The PASS record is reused for the project's lifetime
otherwise, subject to the cascade rule below.

## PASS Conditions

A stage is validated only when all hold:

1. It ran on **real project data**, not a toy or synthetic example.
2. It ran at the **same version and parameters** used in production.
3. The output **parses** and carries the expected shape, units, and range.
4. The **downstream step consumed it** — the next stage in the pipeline
   accepted the output and produced its own.
5. The output is **not degenerate** (see Degenerate-Output Detectors below).

A stage that exits zero without satisfying all five is not validated.
**Process exit status is not evidence of scientific validity.**

### PASS Is A Property Of The Chain

Conditions 1 and 4 point in opposite directions along the pipeline, so no
stage can be validated in isolation. Condition 1 requires that the stage saw
real project data — for any stage after the first, that means the real output
of its validated predecessor, never a synthetic stand-in. Condition 4
requires that the stage's successor consumed its output. Every stage
therefore depends on both of its neighbors, and PASS attaches to a
**position in a chain**, not to a tool in the abstract. The same tool at two
positions holds two records.

Consequences:

- Validation runs in pipeline order. A stage cannot be validated before its
  predecessor, because its condition-1 input does not exist yet.
- A stage reaches PASS only after its successor has run once on its output.
  Until then it is `PENDING`, not `PASS`.
- The terminal stage's condition 4 is satisfied by the reported artifact —
  the figure, table, or statistic — being produced from its output.
- The chain has a PASS only when every stage holds a current PASS and one
  end-to-end run on real project data has completed.

### Cascade Invalidation

A change at any stage clears that stage's PASS and the PASS of every stage
downstream of it, because those records were earned against output that no
longer exists. Changing the first stage's parameters invalidates the whole
chain.

Where a stage's consumer changes how it consumes, the producer's condition 4
is re-tested even when the producer itself did not change.

A stage whose `validated_at` predates the `validated_at` of any upstream
stage is stale (`STALE`). This requires no judgment and is enforced by
`scripts/validate_analysis_config.py`.

## Instrument Record

The record splits across two files, because its two halves have different
lifetimes. The declared chain is a frozen decision: which stages exist, in
what order, each consuming which predecessor. The observed state changes
throughout the work as stages move `PENDING` to `PASS` and cascades mark
stages `STALE`. Writing mutable status into `config.json` would contradict the
freeze rule that governs that file (see
[analysis-artifact-contract.md](analysis-artifact-contract.md)), so the two
are stored separately, and both must agree on the same set of stages.

**Declared — frozen `config.json`, key `instruments`.** One entry per stage,
in pipeline order. Frozen with the rest of the config; a change here is a
dated, labeled plan amendment like any other frozen-decision change. Exactly
these seven keys per entry:

- `stage` — the chain-position identifier and the join key to the observed
  record.
- `position` — its index in the chain.
- `consumes` — the upstream stage it takes input from (`null` for the first
  stage).
- `name`, `version`, `install_source`, `parameters` — identify the tool. The
  same tool at two positions produces two entries with different `stage`
  values.

`stage`, `position`, and `consumes` together make the chain explicit so the
cascade above is computable rather than remembered.

**Observed — mutable `gate_status.json`, key `instrument_status`.** One entry
per declared stage. Rewritten freely as work proceeds; it is a record of
results, not a frozen decision. Exactly these six keys per entry:

- `stage` — matches the declared `stage` it reports on.
- `status` — one of `PASS`, `PENDING`, `FAIL`, `STALE`.
- `validated_at` — timestamp of the run that produced this status.
- `runtime_s` — wall time of that run.
- `output_shape` — the parsed shape/units/range check from PASS condition 3.
- `input_ref` — identifies the input without requiring a rehash of large raw
  data: for the first stage it is the data-contract entry (which already
  carries a SHA-256 per [data-contract.md](data-contract.md)); for later
  stages it is the upstream stage name plus that stage's `validated_at`.

`gate_status.json` carries `instrument_status` at minimum. Other top-level
keys recording gate outcomes are permitted and are not validated by this
skill.

**Agreement.** The two files name the same set of stages. A declared stage
with no observed entry, or an observed entry naming no declared stage, is an
error. `config.json` and `gate_status.json` are both Required Files under
[analysis-artifact-contract.md](analysis-artifact-contract.md), and both are
validated together by `scripts/validate_analysis_config.py`.

## Degenerate-Output Detectors

Treat anomalies as bugs until investigated. Halt the affected stage, diagnose,
then proceed. Detectors:

- a gate or filter that passes everything, fails everything, or returns a
  constant;
- a score of exactly zero, a perfect metric, or an impossible runtime;
- output identical across inputs that differ;
- an all-NaN or all-zero array where signal is expected.

A NaN in a result column is a missing measurement, not a flag value.

## Canary Before Scale

Before any fan-out, run one case from the same specification. After the first
chunk of a batch stage, confirm from its outputs — item counts, pass/fail
counts, and one spot-checked example — that the stage ran as specified,
before launching the rest.

**Cheapest falsifying check first.** Before committing significant compute to
a plan, run the fastest check that could kill it. A seconds-scale check that
could invalidate a multi-hour run runs first.

## Method Tiering

Every instrument carries one tier, recorded with it:

- **Required** — feeds the reported result.
- **Shadow** — tracked and reported, decides nothing.
- **Diagnostic** — can flag a problem; cannot authorize a claim or an
  exclusion. Consistent with the Diagnostic label in
  [interpretation-rules.md](interpretation-rules.md).
- **Fallback** — used only after the ladder below, and recorded as such.

Substitution across tiers is explicit, justified, and logged.

## Fallback Ladder

On instrument failure, in order:

1. **Diagnose.** Read the tool's own documentation and source before
   declaring it broken; a config flag or known limitation is usually
   documented there.
2. **Retry only if the retry differs in a way you can name and log.** A retry
   that cannot be distinguished from the previous attempt is not a retry.
3. **Approved fallback.** Substitute a tool of equal or better tier.
4. **Log the drop with its consequence stated** — which analysis objective is
   now weaker, and by how much.

Provided you log the drop with its consequence stated, unattended
substitution is permitted; that condition is what makes step 3 allowable
without asking. Silent substitution — skipping step 4 — is not permitted.

**Unavailability requires logged queries.** Before concluding a tool,
package, or version does not exist, query its canonical sources directly and
log the exact queries with the conclusion.

## Documentation Is Not Validation

A skill, wrapper, or helper that mentions a tool is reference material only.
Its existence is not evidence the tool works in this environment, and a
helper it provides is not a validated instrument. Where a skill and upstream
documentation disagree, upstream wins.
