---
type: step-card
id: epoching-and-baseline
title: Epoching And Baseline
tags:
  - step:epoching
applies_to:
  - conservative-mne-python
load_with:
  - steps/tms-pulse-detection.md
---

## Purpose

Create pulse-locked trials and define a baseline that does not contaminate post-pulse estimates. Baseline correction sets the pre-TMS signal level to zero, so TEP amplitudes start from the same pre-pulse reference level rather than from an arbitrary voltage offset.

## When To Apply

After pulse handling strategy is defined and events are verified.

## Inputs Needed

Event IDs, epoch window, baseline window, condition labels, and artifact annotations.

## Decision Rules

Use a pre-pulse baseline that is free of preceding stimulation and task events. For high-frequency rTMS, baseline may need special handling.

Short baselines such as `[-50 -10] ms` can be useful after ICA, SOUND, or other cleaning steps to adjust slow baseline shifts. Longer windows such as `[-300 -5] ms` can be more stable because they use more samples, but they are safe only when the whole interval is physiologically quiet and artifact-free. The `300 ms` length is not magic or universal; choose the window from the study design, stimulation history, task timing, and visual QC.

## Method Options

Epoch continuous data, reject annotated segments, apply baseline correction, or defer baseline correction for diagnostic comparisons.

## Learning Mode Explanation

Epoching aligns trials. Baseline correction subtracts the average pre-pulse signal from each epoch so the pre-TMS level becomes zero; this makes post-pulse TEP amplitudes easier to compare across trials, channels, and conditions.

## Code-Engineer Notes

Use explicit `tmin`, `tmax`, `baseline`, and `event_id` placeholders.

## QC Checks

Trial counts by condition, baseline variance, dropped epochs, and event timing alignment.

## Failure Modes

Overlapping epochs, contaminated baseline, mislabeled conditions, treating a conventional baseline window as a magic value, and baseline correction removing meaningful state differences.

## Sources

MNE-Python repo card; conservative MNE pipeline card.
