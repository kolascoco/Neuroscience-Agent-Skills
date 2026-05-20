---
type: step-card
id: bad-channel-detection-and-interpolation
title: Bad Channel Detection And Interpolation
tags:
  - step:bad-channel
applies_to:
  - conservative-mne-python
load_with:
  - artifacts/lead-configuration-early-artifacts.md
---

## Purpose

Remove or repair channels that distort interpolation, ICA, averages, and topographies.

## When To Apply

Before ICA and averaging; revisit after major cleaning steps.

## Inputs Needed

Montage, channel locations, raw traces, noise profile, and condition labels.

## Decision Rules

Mark persistently bad channels before ICA. Avoid interpolating channels without valid montage/locations.

## Method Options

Manual inspection, robust amplitude/variance criteria, neighbor-based interpolation, and condition-aware checks.

## Learning Mode Explanation

Bad channels can dominate decompositions and create false topographic patterns.

## Code-Engineer Notes

Use MNE bad channel marking/interpolation APIs after verifying montage availability.

## QC Checks

Report bad channels, reasons, interpolation method, and before/after topographies.

## Failure Modes

Interpolating too many channels, ignoring lead artifacts, and hiding target-proximal artifacts.

## Sources

MNE-Python repo card; lead configuration artifact cards.
