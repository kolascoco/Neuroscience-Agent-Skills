---
type: step-card
id: pulse-artifact-removal-or-interpolation
title: Pulse Artifact Removal Or Interpolation
tags:
  - step:pulse-interpolation
  - artifact:pulse
applies_to:
  - conservative-mne-python
  - tesa-inspired-two-pass-ica
  - sound-ssp-sir-enhanced
load_with:
  - artifacts/pulse-artifact.md
---

## Purpose

Prevent the large TMS pulse artifact from contaminating filters, ICA, averages, and early response estimates.

## When To Apply

After pulse timing is verified and before filtering or ICA.

## Inputs Needed

Pulse onset samples, sampling rate, artifact window, interpolation/removal method, and hardware recovery characteristics.

## Decision Rules

Use the smallest defensible window that removes pulse contamination without erasing analyzable signal. For i-TEPs, justify the window explicitly.

## Method Options

Mark samples, remove and interpolate, replace with local interpolation, or use toolbox-specific pulse artifact routines.

## Learning Mode Explanation

Filtering across a huge pulse transient can spread artifact into neighboring time points. Handling the pulse first protects downstream steps.

## Code-Engineer Notes

Use `recipes/interpolate_pulse_artifact.md`; verify implementation details for tmseegpy/TESA if using those libraries.

## QC Checks

Overlay pre/post traces around pulse, inspect all channels, document interpolation window, and compare active vs sham pulse residuals.

## Failure Modes

Window too short, window too long for early TEPs, interpolation ringing, filter smearing, and condition-specific residual artifact.

## Sources

Jamil et al. 2024 paper card; pulse artifact card.
