---
type: step-card
id: muscle-artifact-handling
title: Muscle Artifact Handling
tags:
  - artifact:muscle
  - step:muscle-cleaning
applies_to:
  - conservative-mne-python
  - tesa-inspired-two-pass-ica
load_with:
  - artifacts/muscle-artifact.md
---

## Purpose

Identify and reduce TMS-evoked muscle activity that can obscure early and mid-latency EEG.

## When To Apply

After pulse handling and before final TEP averaging; often around ICA/component cleaning.

For DLPFC and other lateral/frontal targets, first decide whether the scientific question tolerates losing the earliest post-pulse samples. Many recent DLPFC workflows remove/interpolate the pulse-plus-early-muscle interval, for example `-2` to `10 ms` or `-2` to `12 ms`, and then analyze later early-local windows such as `20-60 ms` or `30-60 ms`. If the goal is to preserve more of the early response, use projection/SSP-SIR-style cleaning with explicit component QC instead of silently extending interpolation.

## Inputs Needed

Target, coil position, channel traces, EMG if available, ICA components, and time-frequency/high-frequency signatures.

## Decision Rules

Expect stronger muscle artifacts for lateral/frontal targets, especially anterolateral DLPFC. Do not remove components without checking scalp map, time course, and spectral content. TMS-evoked muscle components are suspicious when they show focal frontal/temporal/jaw/neck topographies, strong high-frequency power, and a brief biphasic or MEP-like time course after the pulse.

## Method Options

Trial rejection, target/protocol adjustment, short-window removal/interpolation up to about `10-12 ms` when early samples are not interpreted, projection/SSP-style cleaning, SSP-SIR for early TMS-evoked muscle, and explicit caveat if residual muscle remains. Do not use ordinary ICA component rejection for TMS-evoked muscle artifacts or clear TMS-stimulus-locked components.

## Learning Mode Explanation

Muscle artifact is physiological but non-cortical; it can look like early TEP energy and differ by condition. For DLPFC, stronger responses from medial/posterior targets may be partly easier to measure because anterolateral targets can activate more scalp/facial muscle and mask or suppress recoverable EL-TEPs during preprocessing.

## Code-Engineer Notes

Pair component review plots with automated suggestions. Avoid black-box removal.

## QC Checks

High-frequency activity, biphasic/MEP-like time courses, frontotemporal or jaw/neck channels, component maps, active/sham balance, retained trial counts, and whether the chosen early analysis window overlaps interpolated or projected data.

## Failure Modes

Overcleaning cortical response, undercleaning early components, and condition-specific muscle differences.

## Sources

Muscle artifact card; Maki 2011 projection paper card; Mutanen 2016 muscle-masked TEP recovery card; DLPFC reliability/state-dependency paper cards; TESA-inspired pipeline card.
