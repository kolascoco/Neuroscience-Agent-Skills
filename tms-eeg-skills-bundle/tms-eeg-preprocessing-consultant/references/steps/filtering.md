---
type: step-card
id: filtering
title: Filtering
tags:
  - step:filtering
applies_to:
  - conservative-mne-python
  - tesa-inspired-two-pass-ica
load_with:
  - artifacts/pulse-artifact.md
---

## Purpose

Condition the signal for ICA, evoked analysis, and metrics while avoiding artifact spread.

## When To Apply

After pulse artifact handling, not across unhandled pulse transients.

## Inputs Needed

Sampling rate, analysis frequency band, artifact window, line noise frequency, and target metric.

## Decision Rules

Choose filters based on analysis goals. Preserve transparent reporting of passband, transition, phase, and order.

## Method Options

High-pass/low-pass, notch filtering, separate ICA-filtered copy when appropriate, and no filtering for diagnostic raw inspection.

## Learning Mode Explanation

Filters can smear sharp artifacts and alter component timing; pulse handling comes first.

## Code-Engineer Notes

Verify MNE filter API and parameters through Context7/GitHub fallback.

## QC Checks

Plot frequency spectra and time-domain traces before/after; verify no ringing around the pulse.

## Failure Modes

Filtering before interpolation, overly aggressive high-pass, line-noise overcorrection, and changing early-latency morphology.

## Sources

Methodological choices paper card; pulse artifact step card.
