---
type: step-card
id: tms-pulse-detection
title: TMS Pulse Detection
tags:
  - step:pulse-detection
  - artifact:pulse
applies_to:
  - conservative-mne-python
load_with:
  - artifacts/pulse-artifact.md
---

## Purpose

Identify pulse onset times accurately enough for artifact marking, epoching, and early-response analysis.

## When To Apply

Before interpolation, epoching, averaging, or i-TEP analysis.

## Inputs Needed

Stimulus channel, trigger labels, amplifier annotations, or a validated pulse-detection method.

## Decision Rules

Prefer hardware triggers. Use signal-derived pulse detection only when triggers are missing and validate every detected event visually.

## Method Options

Read event channels, parse annotations, threshold dedicated trigger channels, or detect large pulse transients as a fallback.

## Learning Mode Explanation

Small timing errors can smear TEPs and make early windows uninterpretable.

## Code-Engineer Notes

Use `recipes/detect_tms_events.md`; keep event IDs explicit.

## QC Checks

Plot events over raw data, count pulses by condition, verify inter-pulse intervals, and overlay pulse-locked trials.

## Failure Modes

Duplicate triggers, missing pulses, delayed triggers, stimulation blocks mislabeled as conditions, and thresholding EMG/EEG artifacts as pulses.

## Sources

MNE-Python repo card; i-TEP pipeline card for early timing sensitivity.
