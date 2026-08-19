# Data Contract

Prepare immutable, synchronized inputs before analysis. The Scout role
(see [soul-roles.md](soul-roles.md)) produces this audit; the Orchestrator
enforces the stop conditions before allowing SKILL.md step 4 to proceed.

## Required Inventory

- Source paths, file sizes, SHA-256 hashes, software versions, access dates.
- Subject/session/trial/event inventory with inclusion status and reasons.
- Column schema, dtypes, units, missingness, and value ranges.
- Primary keys for each physical unit; duplicate and collision report.
- Timing/alignment report when data streams must join.
- Preprocessing provenance: reference/filtering/rejection/normalization,
  feature extraction, coordinate systems, units, and versioned code.
- Outcome labels and behavioral variables with definitions and timing.
- Support table for each planned subject x condition x feature/model cell.

## Stop Conditions

Stop and resolve before analysis when:

- identifiers are ambiguous or non-unique;
- physical events/trials duplicate with inconsistent outcomes;
- units or sign conventions are unknown;
- preprocessing/reference/filtering is undocumented;
- trial/event to epoch/sample alignment is not bijective where required;
- stage/window ownership loses or duplicates samples;
- missingness rules are not frozen;
- a required feature cannot be reconstructed from documented sources.

## Data Audit Output

Write a short audit artifact with PASS/FAIL per contract item, as
`input_audit.md` (and `input_audit.json` for the machine-readable form) per
the canonical filename table in
[analysis-artifact-contract.md](analysis-artifact-contract.md). Do not include
new scientific results or exploratory plots beyond inventories, row counts,
schema summaries, and support counts.
