---
type: step-card
id: ocular-cardiac-auditory-components
title: Ocular, Cardiac, And Auditory/Sensory Components
tags:
  - step:component-review
  - artifact:auditory
  - artifact:somatosensory
applies_to:
  - tesa-inspired-two-pass-ica
  - conservative-mne-python
load_with:
  - artifacts/auditory-somatosensory-confounds.md
---

## Purpose

Identify non-target physiological and sensory components that can shape TEPs.

## When To Apply

During ICA/component review and interpretation of active vs sham differences.

## Inputs Needed

EOG/ECG channels if available, sham/control conditions, component maps, time courses, and spectra.

## Decision Rules

Sensory-related components are not automatically "bad"; decide based on analysis goal and control design.

## Method Options

Component rejection, regression/projection, condition modeling, or cautious interpretation.

## Learning Mode Explanation

Some TEP components can include auditory and somatosensory responses to the click/scalp sensation.

## Code-Engineer Notes

Produce component plots and leave decision points visible.

## QC Checks

Component labels, sham similarity, sensor distribution, and timing relative to known sensory evoked responses.

## Failure Modes

Removing genuine cortical responses, leaving sensory confounds unmentioned, and claiming specificity without controls.

## Sources

Gordon paper cards; auditory/somatosensory artifact card.
