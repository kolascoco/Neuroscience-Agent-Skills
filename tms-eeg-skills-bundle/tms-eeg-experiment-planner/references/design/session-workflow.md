---
type: design-card
id: session-workflow
title: TMS-EEG Session Workflow
tags:
  - session
  - checklist
  - qc
---

## Purpose

Provide a day-of-experiment workflow that catches artifact and target-engagement problems before the full dataset is collected.

## Session Flow

1. Confirm safety screening, consent, hearing protection, and TMS/EEG compatibility.
2. Prepare EEG cap carefully: impedances, gel, active electrodes, lead orientation, reference, ground, and physiological channels.
3. Register anatomy/electrodes/head if neuronavigation or source analysis is planned.
4. Locate target and define initial coil orientation/current direction.
5. Determine RMT if needed, but treat it as a starting point.
6. Run online single-pulse checks and inspect single trials.
7. Use 10-30 trial rt-TEP averages to evaluate early local response and artifacts.
8. Adjust coil orientation, position, intensity, masking, or target if online QC fails.
9. Collect main blocks only after go/no-go criteria are met.
10. Monitor drift, discomfort, artifacts, impedance, and condition balance throughout.
11. Save complete metadata, logs, screenshots, and neuronavigation/coil-position records.

## Go/No-Go Criteria

Proceed only if:

- pulse/recharge/decay artifacts are manageable
- craniofacial muscle artifact is not dominating the endpoint window
- masking and sham/control conditions are acceptable
- early local TEP/i-TEP is visible if it is a primary QC or endpoint
- participant tolerates stimulation and masking
- sufficient trials can be collected after expected rejection

## Failure Response

If online QC fails, try small coil rotations/repositioning, intensity adjustment, wire/cap fixes, masking retuning, or a backup target. Do not assume offline preprocessing will solve acquisition-level failures.
