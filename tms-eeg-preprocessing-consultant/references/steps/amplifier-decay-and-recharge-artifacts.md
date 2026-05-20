---
type: step-card
id: amplifier-decay-and-recharge-artifacts
title: Amplifier Decay And Recharge Artifacts
tags:
  - artifact:decay
  - artifact:recharge
applies_to:
  - tesa-inspired-two-pass-ica
  - conservative-mne-python
load_with:
  - artifacts/pulse-artifact.md
---

## Purpose

Detect slower hardware recovery artifacts after the main pulse transient.

## When To Apply

Immediately after pulse artifact handling and before interpreting early or mid-latency components.

## Inputs Needed

Amplifier model if known, raw traces around pulse, sampling rate, and channel-wise recovery profile.

## Decision Rules

Do not treat the post-pulse signal as physiological until recovery artifacts are visually inspected.

## Method Options

Visual trace inspection, channel-wise amplitude/range checks, decay-window annotation, and exclusion of contaminated windows.

## Learning Mode Explanation

The pulse artifact is not always a single instant; hardware recovery can extend into windows that look like neural responses.

## Code-Engineer Notes

Add QC plots rather than automatic correction unless the method is verified for the data.

## QC Checks

Plot channel-wise traces from pre-pulse to at least 100 ms post-pulse and inspect consistency across conditions.

## Failure Modes

Mislabeling recovery as i-TEP, applying ICA to dominated recovery windows, and failing to report excluded windows.

## Sources

Jamil et al. 2024 paper card; i-TEP pipeline card.
