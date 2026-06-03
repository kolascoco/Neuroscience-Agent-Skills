---
type: repo-card
id: pytepfit
title: PyTepFit
source_url: https://github.com/GriffithsLab/PyTepFit
context7: preferred
github_fallback: https://github.com/GriffithsLab/PyTepFit
tags:
  - repo:pytepfit
  - ecosystem:python
  - pipeline:tepfit
  - model:jansen-rit
  - model:connectome
---

## Role In The Skill

Reference repository for whole-brain modeling of TMS-EEG TEPs from Momi, Wang, and Griffiths 2023. Use for model-aware TEP analysis after preprocessing, not for artifact cleaning.

## Software Lookup Policy

1. If Context7 is available, resolve/query this library there for current API names, parameters, examples, and installation notes.
2. If Context7 is unavailable or incomplete, use the GitHub fallback URL below.
3. Do not invent function signatures. If uncertain, say which repo/source should be checked.

## What The Agent Should Reuse

Conceptual workflow for fitting simulated TMS-EEG responses to empirical TEPs, including connectome-based neural mass modeling, lead-field/channel-space comparison, optimization, and model-vs-empirical fit checks.

## Workflow Concepts

The repo README describes a 200-region Schaefer atlas/connectome framework, Jansen-Rit neural mass model, TMS perturbation to excitatory interneuron membrane potential, lead-field projection to channel space, and optimization of model parameters against empirical preprocessed TMS-EEG.

## Important Assumptions

The repository is primarily notebooks plus Python code and depends on scientific Python and neuroimaging libraries. The README states the empirical data were already preprocessed; this is downstream analysis.

## Useful Source Areas To Inspect

README, `requirements.txt`, `nb/`, `tepfit/`, data-structure examples, and notebooks reproducing main figures.

## Failure Modes

Treating PyTepFit as a preprocessing toolbox, assuming repository paths/data are available, overclaiming physiology from fitted parameters, and using artifact-contaminated empirical TEPs.

## Related Cards

`pipelines/tepfit-network-modeling-analysis.md`; `steps/tepfit-modeling-analysis.md`; `papers/momi-2023-recurrent-network-dynamics.md`.
