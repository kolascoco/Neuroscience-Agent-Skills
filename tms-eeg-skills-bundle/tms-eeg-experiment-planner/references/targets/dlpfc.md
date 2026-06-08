---
type: target-card
id: dlpfc
title: DLPFC TMS-EEG Planning
tags:
  - target:dlpfc
  - muscle-artifact
  - sensory-confounds
---

## Planning Focus

DLPFC is scientifically important but artifact-sensitive. Target subregion, coil orientation, muscle artifact, masking, and sensory controls should be planned before acquisition.

## Risks

- craniofacial and scalp muscle artifacts
- auditory/somatosensory confounds
- weak early local TEP
- target-specific reliability differences
- interpreting N100/P200 as direct cortical activation

## Practical Advice

Use online TEP monitoring to find a target/orientation with interpretable early local responses and manageable muscle artifact. Record blinks before DLPFC sessions when ICA will be used. Consider backup medial/posterior or lower-muscle target options if anterior/lateral DLPFC is too contaminated.

For muscle artifact, inspect single trials and short averages for a focal high-frequency, biphasic/MEP-like response near frontal, temporal, jaw, or facial channels. If this dominates the first `10-20 ms`, plan in advance whether preprocessing will remove/interpolate the earliest interval or use projection/SSP-SIR-style recovery; do not design an endpoint that depends on samples you expect to interpolate.

## Sources

Gogulski 2024 DLPFC reliability/mapping; Maki 2011 muscle projection; Biabani et al. 2019; local good-practice note.
