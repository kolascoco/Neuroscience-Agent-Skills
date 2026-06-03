---
type: artifact-card
id: auditory-somatosensory-confounds
title: Auditory And Somatosensory Confounds
tags:
  - artifact:auditory
  - artifact:somatosensory
  - caution:sensory-confounds
---

## What It Is

TEP activity partly driven by TMS click, scalp sensation, cranial muscle activation, expectation, or sham-control differences.

## Why It Matters

Several TEP components and condition differences can include sensory-evoked contributions rather than direct cortical effects at the target.

## Detection Clues

Similarity to auditory/somatosensory control responses, broad scalp topographies, condition differences in click/sensation, and late components such as N100.

## Mitigation Options

Masking noise, realistic sham, sensory control conditions, active control targets, trial-level covariates, and cautious interpretation.

## Pipeline Implications

Preprocessing cannot solve poor controls. Keep condition labels separate and avoid removing sensory components without a defined analysis goal.

## Interpretation Caveats

Do not present active-vs-sham TEP differences as direct cortical excitability unless sensory confounds are addressed.

## Sources

Gordon et al. 2018; Gordon et al. 2026; TMS click masking workflow.
