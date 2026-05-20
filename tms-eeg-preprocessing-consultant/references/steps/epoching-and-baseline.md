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

Create pulse-locked trials and define a baseline that does not contaminate post-pulse estimates.

## When To Apply

After pulse handling strategy is defined and events are verified.

## Inputs Needed

Event IDs, epoch window, baseline window, condition labels, and artifact annotations.

## Decision Rules

Use a pre-pulse baseline that is free of preceding stimulation and task events. For high-frequency rTMS, baseline may need special handling.

## Method Options

Epoch continuous data, reject annotated segments, apply baseline correction, or defer baseline correction for diagnostic comparisons.

## Learning Mode Explanation

Epoching aligns trials; baseline defines the zero reference for amplitude estimates.

## Code-Engineer Notes

Use explicit `tmin`, `tmax`, `baseline`, and `event_id` placeholders.

## QC Checks

Trial counts by condition, baseline variance, dropped epochs, and event timing alignment.

## Failure Modes

Overlapping epochs, contaminated baseline, mislabeled conditions, and baseline removing meaningful state differences.

## Sources

MNE-Python repo card; conservative MNE pipeline card.
