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

Mark, remove, or repair channels that distort ICA, averages, and topographies.

## When To Apply

Mark bad channels before ICA and averaging; revisit after major cleaning steps. For ICA, exclude marked bad channels from the decomposition. Repair/interpolate channels after ICA, or use SOUND/channel-repair methods later when geometry and full-channel metadata are available.

## Inputs Needed

Montage, channel locations, raw traces, noise profile, and condition labels.

## Decision Rules

Mark persistently bad channels before ICA so they are not used to estimate components. Avoid interpolating bad channels before ICA unless the workflow explicitly handles the resulting rank/dependency issue. Avoid interpolating channels without valid montage/locations.

## Method Options

Manual inspection, robust amplitude/variance criteria, bad-channel marking/exclusion for ICA, SOUND/channel repair, neighbor-based interpolation after ICA, and condition-aware checks.

## Learning Mode Explanation

Bad channels can dominate decompositions and create false topographic patterns.

## Code-Engineer Notes

Use MNE/EEGLAB bad-channel marking before ICA. Use interpolation or SOUND/channel-repair APIs after verifying montage availability and after ICA/component decisions unless a protocol explicitly requires a different rank-aware order.

## QC Checks

Report bad channels, reasons, whether they were excluded from ICA, repair/interpolation method, and before/after topographies.

## Failure Modes

Interpolating too many channels, ignoring lead artifacts, and hiding target-proximal artifacts.

## Sources

MNE-Python repo card; lead configuration artifact cards.
