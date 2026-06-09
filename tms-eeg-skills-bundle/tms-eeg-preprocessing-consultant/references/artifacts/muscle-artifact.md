---
type: artifact-card
id: muscle-artifact
title: TMS-Evoked Muscle Artifact
tags:
  - artifact:muscle
  - caution:early-latency
---

## What It Is

Scalp, facial, neck, or target-adjacent muscle activity evoked by TMS.

## Why It Matters

It can dominate early and mid-latency EEG, especially for frontal/lateral targets, and can differ between active and sham conditions. Peak-to-peak amplitude can exceed 1 mV (>1000 µV) for frontal/lateral targets (Rogasch et al. 2017). For DLPFC, muscle artifact and early-local TEP amplitude are strongly negatively correlated across subregions (R ≈ −0.71): regions with more artifact show smaller measured EL-TEPs, which can reflect either true signal suppression or preprocessing over-rejection (Gogulski et al. 2024).

## Detection Clues

High-frequency bursts, frontotemporal emphasis, strong single-trial variability, and ICA/projection/SSP-SIR components with muscle-like spectra/topographies. A TMS-evoked muscle component often has a brief biphasic or MEP-like time course, very early post-pulse onset, and focal topography near frontal, temporal, jaw, facial, or neck channels.

## Mitigation Options

Optimize coil placement, reduce discomfort, reject contaminated trials, inspect ICA/projection/SSP-SIR components, and use controls/sham. For DLPFC, either document a short removed/interpolated early interval such as `-2` to `10-12 ms`, or justify projection/SSP-SIR cleaning if the aim is to recover early TEP information masked by muscle artifact.

## Pipeline Implications

Inspect before and after component cleaning. Do not assume averaging removes muscle artifact.

Do not treat interpolated samples as physiological signal. If a DLPFC workflow removes/interpolates up to about `12 ms`, analysis windows starting later, such as `20-60 ms` or `30-60 ms`, are easier to defend than claims about the excised interval.

## Interpretation Caveats

Residual muscle activity can mimic stronger evoked responses; mention it for DLPFC and lateral targets. Conversely, aggressive muscle cleanup can also suppress true nearby cortical signal, so compare pre/post topographies and sensitivity to projection count or SSP-SIR PCs.

## Sources

TESA-inspired pipeline; Rogasch et al. 2017 (amplitude); Maki 2011 projection paper; Mutanen 2016 SSP-SIR/muscle recovery paper; Gogulski et al. 2024 DLPFC mapping/reliability papers; Kabir 2024 DLPFC state-dynamics paper.
