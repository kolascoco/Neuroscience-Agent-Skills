---
type: step-card
id: trial-rejection
title: Trial Rejection
tags:
  - step:trial-rejection
applies_to:
  - conservative-mne-python
load_with:
  - artifacts/muscle-artifact.md
---

## Purpose

Exclude trials with residual artifacts while preserving enough balanced data for reliable averages.

## When To Apply

After major cleaning and before final averaging; sometimes also before ICA for gross artifacts.

## Inputs Needed

Epochs, artifact criteria, condition labels, and minimum trial requirements.

## Decision Rules

Report retained trials per condition. Avoid rejection policies that systematically differ by condition without discussion.

## Method Options

Manual review, amplitude/range thresholds, annotation-based rejection, robust statistics, and condition-balanced criteria.

## Learning Mode Explanation

TEPs depend on averaging many trials; rejection improves quality but can bias condition comparisons.

## Code-Engineer Notes

Output dropped epoch logs and summary tables.

## QC Checks

Rejected/retained counts, reasons, condition balance, and post-rejection averages.

## Failure Modes

Too few trials, active/sham imbalance, removing target-specific effects, and inconsistent thresholds.

## Sources

Conservative MNE pipeline card; TEP reliability paper cards when available.
