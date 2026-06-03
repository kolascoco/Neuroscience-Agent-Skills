---
type: step-card
id: early-response-baseline-and-reference
title: Early-Response Baseline And Reference
tags:
  - metric:itep
  - step:baseline
applies_to:
  - itep-early-response-analysis
load_with:
  - artifacts/lead-configuration-early-artifacts.md
---

## Purpose

Ensure baseline and reference choices do not create or suppress early responses.

## When To Apply

Before i-TEP amplitude/topography estimation.

## Inputs Needed

Reference scheme, montage, pre-pulse baseline window, target, and lead configuration.

## Decision Rules

Report reference and baseline explicitly. Test sensitivity when early effects are small or topography-dependent.

## Method Options

Average reference, linked mastoids or original reference when justified, ROI-specific sensitivity checks, and no-baseline diagnostic plots.

## Learning Mode Explanation

Reference and baseline choices can reshape early topographies and amplitudes.

## Code-Engineer Notes

Keep reference/baseline operations explicit and reversible in code.

## QC Checks

Compare early topographies under reference/baseline alternatives when feasible.

## Failure Modes

Unreported rereferencing, contaminated baseline, and reference-driven false lateralization.

## Sources

Lead configuration paper card; i-TEP pipeline card.
