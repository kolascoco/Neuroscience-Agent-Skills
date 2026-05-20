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

## Inputs Needed

Target, coil position, channel traces, EMG if available, ICA components, and time-frequency/high-frequency signatures.

## Decision Rules

Expect stronger muscle artifacts for lateral/frontal targets. Do not remove components without checking scalp map, time course, and spectral content.

## Method Options

Trial rejection, component rejection, target/protocol adjustment, artifact-specific cleaning, and explicit caveat if residual muscle remains.

## Learning Mode Explanation

Muscle artifact is physiological but non-cortical; it can look like early TEP energy and differ by condition.

## Code-Engineer Notes

Pair component review plots with automated suggestions. Avoid black-box removal.

## QC Checks

High-frequency activity, frontotemporal channels, component maps, active/sham balance, and retained trial counts.

## Failure Modes

Overcleaning cortical response, undercleaning early components, and condition-specific muscle differences.

## Sources

Muscle artifact card; TESA-inspired pipeline card.
