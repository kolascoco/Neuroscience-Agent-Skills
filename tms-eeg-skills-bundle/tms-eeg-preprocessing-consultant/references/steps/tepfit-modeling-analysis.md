---
type: step-card
id: tepfit-modeling-analysis
title: PyTepFit TEP Modeling Analysis
tags:
  - pipeline:tepfit
  - model:jansen-rit
  - model:connectome
  - model:recurrent-network
applies_to:
  - tepfit-network-modeling-analysis
load_with:
  - repos/pytepfit.md
  - papers/momi-2023-recurrent-network-dynamics.md
---

## Purpose

Use PyTepFit-style whole-brain modeling to reason about how cleaned TEP waveforms may relate to local and recurrent large-scale network dynamics.

## When To Apply

After preprocessing, artifact QC, TEP averaging, and any source/channel-space alignment required by the modeling workflow.

## Inputs Needed

Clean empirical TEPs, source/channel representation, model assumptions, connectome/atlas information, lead field or mapping assumptions, and fit/evaluation metrics.

## Decision Rules

Do not use this step to clean data. If preprocessing artifacts remain unresolved, return to preprocessing QC before modeling.

## Method Options

Use verified PyTepFit notebooks/scripts, reproduce the published workflow, or provide conceptual analysis guidance when source/model inputs are unavailable.

## Learning Mode Explanation

PyTepFit addresses why TEP peaks can emerge over time: some components may reflect local reverberation while later responses may depend on recurrent network feedback.

## Code-Engineer Notes

Context7 did not resolve PyTepFit on 2026-05-19; use the GitHub fallback README, notebooks, requirements, and `tepfit/` source before writing code.

## QC Checks

Verify empirical TEP quality, channel/source alignment, model fit diagnostics, parameter reporting, and comparison with sham/sensory caveats where relevant.

## Failure Modes

Fitting residual artifacts, treating model parameters as directly measured physiology, mismatched atlas/lead-field assumptions, and uncritical reuse of published data paths.

## Sources

Momi et al. 2023 paper card; PyTepFit repo card.
