---
type: step-card
id: tep-averaging
title: TEP Averaging
tags:
  - metric:tep
applies_to:
  - conservative-mne-python
  - tesa-inspired-two-pass-ica
  - sound-ssp-sir-enhanced
load_with:
  - artifacts/auditory-somatosensory-confounds.md
---

## Purpose

Compute condition-level or subject-level evoked responses after transparent cleaning and trial rejection.

## When To Apply

After final epoch cleaning and before metrics/topographies.

## Inputs Needed

Clean epochs, condition labels, channel selection, baseline policy, and time windows.

## Decision Rules

Keep active/sham/control averages separate and report retained trials.

## Method Options

Condition averages, global averages, ROI averages, robust averaging, and difference waves when controls are valid.

## Learning Mode Explanation

Averaging reveals time-locked responses but also averages residual artifacts if cleaning was insufficient.

## Code-Engineer Notes

Use explicit channel picks and condition labels.

## QC Checks

Butterfly plots, topomaps at selected latencies, confidence intervals if available, and trial counts.

## Failure Modes

Averaging across mismatched conditions, hiding residual artifacts, and overinterpreting component labels.

## Sources

Conservative MNE pipeline card; sensory confound cards.
