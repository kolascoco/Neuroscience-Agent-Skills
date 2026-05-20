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

It can dominate early and mid-latency EEG, especially for frontal/lateral targets, and can differ between active and sham conditions.

## Detection Clues

High-frequency bursts, frontotemporal emphasis, strong single-trial variability, and ICA components with muscle-like spectra/topographies.

## Mitigation Options

Optimize coil placement, reduce discomfort, reject contaminated trials, inspect ICA components, and use controls/sham.

## Pipeline Implications

Inspect before and after component cleaning. Do not assume averaging removes muscle artifact.

## Interpretation Caveats

Residual muscle activity can mimic stronger evoked responses; mention it for DLPFC and lateral targets.

## Sources

TESA-inspired pipeline; methodological cleaning papers.
