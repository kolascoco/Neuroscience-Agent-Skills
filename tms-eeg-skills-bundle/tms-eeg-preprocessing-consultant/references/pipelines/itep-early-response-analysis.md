---
type: pipeline-card
id: itep-early-response-analysis
title: Immediate TEP/i-TEP Early-Response Analysis Branch
tags:
  - pipeline:itep
  - metric:itep
  - caution:early-latency
default_for:
  - immediate TEPs
  - early post-pulse response analysis
  - M1 i-TEP questions
avoid_when:
  - acquisition metadata are missing
  - pulse artifact window is unknown
  - user wants only late TEP components
step_cards:
  - steps/itep-analysis-window-selection.md
  - steps/downsampling-and-resampling.md
  - steps/early-response-baseline-and-reference.md
  - steps/early-tep-topography-and-roi.md
  - steps/early-latency-qc.md
artifact_cards:
  - artifacts/early-pulse-residual-risk.md
  - artifacts/lead-configuration-early-artifacts.md
  - artifacts/sampling-sync-early-artifacts.md
  - artifacts/muscle-artifact.md
repo_cards:
  - repos/mne-python.md
paper_cards:
  - papers/beck-2024-iteps.md
  - papers/nuyts-2025-immediate-tep-mapping.md
  - papers/lankinen-2026-lead-configuration-early-artifacts.md
  - papers/jamil-2024-intensity-sampling-sync.md
  - papers/gordon-2018-realistic-sham.md
  - papers/gordon-2026-somatosensory-inputs.md
---

## Use When

Use when the user asks for immediate TEPs, i-TEPs, early TMS-EEG responses, or analysis windows close to the pulse artifact.

## Required Inputs

Sampling frequency, TMS hardware synchronization, pulse timestamp method, interpolation/removal window, amplifier recovery behavior, EEG lead configuration, reference, target, active/sham/control design, and exact early analysis window.

## Workflow Order

1. Verify acquisition metadata and pulse timing precision.
2. Define early window only after pulse/recovery artifacts are characterized.
3. Inspect single-trial and averaged traces around the pulse at high temporal resolution.
4. Evaluate lead-configuration and sampling/synchronization risks, including whether downsampling or anti-alias filtering could distort early windows.
5. Compare active against sham/control and sensory conditions if available.
6. Analyze topography/ROI with conservative language.
7. Report all artifact windows and acquisition parameters.

## Step Cards To Load

Load all i-TEP step cards plus early artifact cards. For code, use `recipes/itep_early_window_analysis.md`.

## Parameter Defaults To Consider

Do not give universal early windows. Tie windows to the acquisition protocol, artifact duration, and local papers.

## QC Checkpoints

Overlay raw/interpolated traces, inspect channel-wise early topographies, verify no condition-specific pulse residual, report sampling/sync details, and compare with sham/control when available.

## Common Failure Modes

Residual pulse artifact, recharge/decay artifact, lead-loop effects, sampling misalignment, anti-alias/filter ringing, muscle artifact, baseline/reference distortions, and overconfident cortical interpretation.

## Learning Mode Response

Explain why early responses require stricter proof: the closer the analysis window is to the pulse, the more acquisition and artifact physics can dominate.

## Code-Engineer Mode Response

Generate analysis code that explicitly marks artifact windows, plots raw/interpolated early traces, computes early-window amplitudes/topographies, and labels all assumptions.

## Claims And Caveats

i-TEPs should not be described as clean cortical activity unless residual artifact, lead configuration, sampling/synchronization, muscle, and control-condition evidence are addressed.
