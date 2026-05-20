---
type: step-card
id: automated-artifact-rejection
title: Automated Artifact Rejection
tags:
  - step:automated-rejection
  - pipeline:artist-aaratep
  - caution:overcleaning
applies_to:
  - automated-artist-aaratep
  - tesa-inspired-two-pass-ica
load_with:
  - artifacts/overcleaning-and-ica-risk.md
---

## Purpose

Use algorithmic rules to identify bad channels, bad epochs, artifact components, or TMS-specific artifact patterns reproducibly.

## When To Apply

When the user asks for ARTIST/AARATEP automation, large-scale processing, or reduced manual artifact labeling.

## Inputs Needed

Event timing, epochs, sampling rate, channel montage, artifact windows, algorithm thresholds, dependency versions, and review criteria.

## Decision Rules

Automated rejection is acceptable only if decisions are logged and reviewable. If a result depends on automation, include before/after QC and retained-data summaries.

## Method Options

ARTIST-style automated artifact rejection, ICLabel-assisted component rejection, TMS-specific IC rules, bad-channel algorithms, and threshold-based epoch rejection.

## Learning Mode Explanation

Automation can make preprocessing more consistent across subjects, but it can also encode systematic mistakes if assumptions do not fit the dataset.

## Code-Engineer Notes

For AARATEP, verify MATLAB function names and parameters from Context7 or GitHub. Do not reimplement ARTIST from memory.

## QC Checks

Report rejected channels, epochs, components, thresholds/rules, retained trials by condition, and before/after evoked traces.

## Failure Modes

Silent overcleaning, dataset mismatch, unbalanced rejection by condition, dependency drift, and unreported rule changes.

## Sources

Wu et al. 2018 ARTIST paper card; AARATEP repo card.
