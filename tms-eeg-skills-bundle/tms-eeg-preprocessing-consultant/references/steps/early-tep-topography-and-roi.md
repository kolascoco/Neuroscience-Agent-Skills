---
type: step-card
id: early-tep-topography-and-roi
title: Early TEP Topography And ROI
tags:
  - metric:itep
  - step:topography
applies_to:
  - itep-early-response-analysis
load_with:
  - artifacts/lead-configuration-early-artifacts.md
---

## Purpose

Analyze spatial patterns and ROI amplitudes for early responses without overclaiming source specificity.

## When To Apply

After early windows, artifact boundaries, and reference choices are defined.

## Inputs Needed

Montage, ROI channels, target, time window, cleaned evoked data, and control conditions.

## Decision Rules

Define ROI before outcome interpretation. Topography can support plausibility but does not prove cortical origin.

## Method Options

Topomaps, ROI mean amplitude, peak amplitude/latency, lateralization checks, and rostro-caudal mapping summaries.

## Learning Mode Explanation

Early topographies can reveal structured responses, but artifact and lead geometry can also impose structure.

## Code-Engineer Notes

Use `recipes/itep_early_window_analysis.md`.

## QC Checks

Plot topographies at window center, ROI traces, and condition differences.

## Failure Modes

Post hoc ROI selection, ignoring bad/interpolated channels, and topographic overinterpretation.

## Sources

Beck 2024 and Nuyts 2025 paper cards.
