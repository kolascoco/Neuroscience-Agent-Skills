---
type: step-card
id: early-latency-qc
title: Early-Latency QC
tags:
  - metric:itep
  - step:qc
  - caution:early-latency
applies_to:
  - itep-early-response-analysis
load_with:
  - artifacts/early-pulse-residual-risk.md
  - artifacts/sampling-sync-early-artifacts.md
---

## Purpose

Provide evidence that early effects are not dominated by pulse, sampling, lead, recharge, or muscle artifacts.

## When To Apply

Always for i-TEP analyses and early post-pulse claims.

## Inputs Needed

Raw traces, cleaned traces, pulse windows, sampling/sync metadata, lead configuration, sham/control data, and condition labels.

## Decision Rules

If early artifact controls are missing, frame i-TEP results as provisional or exploratory.

## Method Options

Overlay single trials, inspect per-channel residuals, compare sham/control, test window sensitivity, and plot acquisition/reporting parameters.

## Learning Mode Explanation

Early-latency QC is the bridge between an interesting waveform and a defensible physiological claim.

## Code-Engineer Notes

Generate plots that mark pulse onset, interpolation window, i-TEP window, and condition labels.

## QC Checks

No unreported samples removed, no condition-specific residual, no suspicious lead-channel pattern, and stable result across nearby windows.

## Failure Modes

Clean-looking averages hiding single-trial artifacts, unbalanced conditions, and insufficient reporting.

## Sources

Jamil 2024, Lankinen 2026, Beck 2024, Nuyts 2025 paper cards.
