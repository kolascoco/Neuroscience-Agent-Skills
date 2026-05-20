---
type: step-card
id: data-intake-and-metadata
title: Data Intake And Metadata
tags:
  - step:data-intake
applies_to:
  - conservative-mne-python
  - sound-ssp-sir-enhanced
load_with:
  - routing/context7-or-github-fallback.md
---

## Purpose

Establish the dataset facts that determine safe preprocessing choices.

## When To Apply

Always, before recommending a concrete pipeline or code.

## Inputs Needed

Data format, sampling rate, event channel, montage, reference, target, conditions, acquisition hardware notes, and analysis goal.

## Decision Rules

If event timing, sampling rate, or artifact windows are unknown, provide placeholders and ask the user to verify before running code.

## Method Options

Use MNE readers for common formats; use BIDS metadata when available; inspect annotations/events before epoching.

## Learning Mode Explanation

TMS-EEG preprocessing is order-sensitive. Bad assumptions about timing or acquisition can make later artifact removal look successful while distorting the actual evoked response.

## Code-Engineer Notes

Use `recipes/load_mne_data.md`. Verify reader functions through Context7 or GitHub fallback.

## QC Checks

Print sampling rate, channel types, event counts, bad channels, annotations, condition labels, and montage availability.

## Failure Modes

Wrong event channel, missing montage, accidental resampling before pulse handling, hidden annotations, and confusing active/sham labels.

## Sources

MNE-Python repo card; conservative MNE pipeline card.
