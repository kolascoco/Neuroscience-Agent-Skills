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

Identify non-target physiological and sensory components that can shape TEPs, while separating cleaning decisions from interpretation/control decisions.

## When To Apply

During ICA/component review and interpretation of active vs sham/control or task-condition differences.

## Inputs Needed

EOG/ECG channels if available, sham/control conditions, component maps, time courses, and spectra.

## Decision Rules

Sensory-related components are not automatically "bad" and should not be removed by default. Normally, reduce them through acquisition design such as masking, and handle remaining sensory responses through contrasts or subtraction where justified by the experiment, for example rest vs motor imagery comparisons or subtracting an auditory ERP/control response.

## Method Options

Component rejection, regression/projection, condition modeling, or cautious interpretation.

## Learning Mode Explanation

Some TEP components can include auditory and somatosensory responses to the click/scalp sensation. Removing such components with ICA can remove real condition-related signal if the component overlaps with cortical TEP activity.

## Code-Engineer Notes

Produce component plots and leave decision points visible. If sensory subtraction/contrast is used, report the control condition and assumptions.

## QC Checks

Component labels, sham/control similarity, sensor distribution, timing relative to known sensory evoked responses, and whether a subtraction/contrast was applied.

## Failure Modes

Removing genuine cortical responses by default ICA rejection, leaving sensory confounds unmentioned, and claiming specificity without controls.

## Sources

Gordon paper cards; auditory/somatosensory artifact card.
