---
type: step-card
id: itep-analysis-window-selection
title: i-TEP Analysis Window Selection
tags:
  - metric:itep
  - caution:early-latency
applies_to:
  - itep-early-response-analysis
load_with:
  - artifacts/early-pulse-residual-risk.md
---

## Purpose

Define immediate-response windows only after artifact duration and acquisition timing are characterized.

## When To Apply

For any i-TEP or very early post-pulse analysis.

## Inputs Needed

Sampling rate, pulse artifact/removal window, amplifier recovery, synchronization, target, and paper/protocol-specific window.

## Decision Rules

No universal i-TEP window. The chosen window must be later than credible residual pulse/recovery contamination or explicitly model that risk.

## Method Options

Protocol-derived windows, exploratory early-window scans with correction, ROI/time-window preregistration, and sensitivity analysis across nearby windows.

## Learning Mode Explanation

i-TEPs live close to the largest artifact in the recording, so window choice is a methodological claim.

## Code-Engineer Notes

Make windows constants in code and print them in the report.

## QC Checks

Show raw/interpolated traces around the window and mark artifact boundaries.

## Failure Modes

Choosing windows post hoc, overlapping artifact interpolation, and ignoring sampling jitter.

## Sources

Beck 2024 and Nuyts 2025 paper cards; Jamil 2024 paper card.
