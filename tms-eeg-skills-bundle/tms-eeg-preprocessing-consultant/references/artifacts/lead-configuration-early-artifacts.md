---
type: artifact-card
id: lead-configuration-early-artifacts
title: Lead Configuration And Early Artifacts
tags:
  - artifact:lead-configuration
  - metric:itep
  - caution:early-latency
---

## What It Is

Early post-pulse artifacts shaped by electrode leads, wire routing, and cap setup. This card covers the preprocessing-level implications (what to check and report); for the hardware/physics mechanism see `artifacts/electrode-lead-configuration.md`.

## Why It Matters

Lead effects can appear as spatially structured early responses.

## Detection Clues

Spatial pattern follows hardware layout more than expected neuroanatomy; early effects change across cap/lead setup.

## Mitigation Options

Document lead layout, keep setup consistent, inspect topographies against lead geometry, and avoid unsupported source claims.

## Pipeline Implications

Pair early topographies with hardware/setup notes. For i-TEP analysis, retain a copy of minimally processed data at the native sampling rate for comparison with artifact-corrected data. Hardware-related artifact produces reproducible single-trial patterns (consistent polarity across trials), unlike the variable muscle artifact, and its topography tends to mirror lead-wire layout rather than neuroanatomical expectations.

## Interpretation Caveats

Early topographies do not automatically imply cortical generators.

## Sources

Lankinen/Fadel/Nummenmaa/Ilmoniemi/Raij 2026 preprint.
