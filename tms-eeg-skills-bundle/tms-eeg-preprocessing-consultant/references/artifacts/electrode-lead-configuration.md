---
type: artifact-card
id: electrode-lead-configuration
title: Electrode Lead Configuration
tags:
  - artifact:lead-configuration
  - caution:early-latency
---

## What It Is

Artifact induced in electrode leads by the TMS pulse, arising from mutual inductance between the TMS coil windings and the loop formed by each electrode lead wire. Amplitude is proportional to the coil current rate (dI/dt) and the mutual inductance, which depends on lead loop area and orientation relative to the coil (Lankinen et al. 2026). This card covers the hardware/physics mechanism; for what to check during preprocessing see `artifacts/lead-configuration-early-artifacts.md`.

## Why It Matters

Lead configuration determines pulse artifact amplitude, polarity, and the subsequent decay artifact (pulse and decay are strongly correlated, ρ ≈ 0.86), and therefore shapes early topographies, especially in i-TEP windows. Early EEG topographies can reflect lead geometry in addition to, or instead of, cortical generators.

## Detection Clues

Channel patterns aligned with lead layout, target-adjacent channels with disproportionate early responses, and replication differences across cap setups.

## Mitigation Options

Careful cable layout, documentation, cap setup consistency, lead-aware QC, and sensitivity analysis. Lead crossing (routing wires to cancel loop area relative to the coil) can produce near-zero pulse and decay artifacts; in Lankinen et al. 2026, 14 of 23 configurations produced negative-polarity decay artifacts purely from loop geometry. Optimizing cable routing before acquisition is more effective than post-hoc correction.

## Pipeline Implications

Do not treat early topography as physiological without considering lead geometry.

## Interpretation Caveats

Early component localization/topography must mention lead configuration if relevant.

## Sources

Lankinen/Fadel/Nummenmaa/Ilmoniemi/Raij 2026 preprint paper card.
