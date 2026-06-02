---
type: step-card
id: sound-cleaning
title: SOUND Cleaning
tags:
  - step:sound
applies_to:
  - sound-ssp-sir-enhanced
load_with:
  - repos/pytep-sound-ssp-sir.md
---

## Purpose

Use SOUND-style denoising when a source/model-informed approach is appropriate for sensor noise.

## When To Apply

Only when required geometry/metadata and verified implementation details are available.

## Inputs Needed

EEG data, electrode locations, model assumptions, and method parameters from verified docs/source.

## Decision Rules

Do not recommend SOUND as a black-box default. Confirm montage/channel coordinates and compare before/after outputs. Start with `lambda_val=0.1` and `iter_num=5` only as a local guide, then tune from diagnostics.

## Method Options

Use verified PyTEP-SOUND-SSP-SIR code or describe pseudocode if API cannot be confirmed.

## Learning Mode Explanation

SOUND is conceptually different from ICA: it uses spatial/model assumptions to reduce noise, so metadata quality matters.

## Code-Engineer Notes

Query Context7 first; otherwise inspect the GitHub fallback repo.

## QC Checks

Noise reduction, channel RMS/peak-to-peak diagnostics, rank/model warnings, topographies, evoked waveforms, and condition-specific changes.

## Failure Modes

Missing electrode geometry, invalid assumptions, unreported parameters, and accidental removal of evoked signal.

## Sources

PyTEP-SOUND-SSP-SIR repo card.
