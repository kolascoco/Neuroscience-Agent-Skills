---
type: paper-card
id: lankinen-2026-lead-configuration-early-artifacts
title: The effect of EEG lead configuration on early TMS-EEG artifacts
year: 2026
authors: Lankinen, Fadel, Nummenmaa, Ilmoniemi, Raij
source_pdf: ../../../../TMS-EEG-artifacts/articles/TMS-EEG/The_effect_of_EEG_lead_configuration_on_early_TMS-.pdf
doi: 10.64898/2026.02.10.705170
tags:
  - artifact:lead-configuration
  - metric:itep
  - caution:early-latency
use_for:
  - early artifact risk
  - lead configuration caveats
confidence: preprint-seed-card
---

## Why This Matters For The Agent

Lead configuration is a first-order caveat for early TMS-EEG/i-TEP claims.

## Key Methods

Systematic test of multiple electrode lead configurations (23 conditions). Pulse artifact measured at ~0.2 ms native width, stretched to ~0.55 ms by low-pass filtering; decay artifact lasts tens of milliseconds. The artifact arises from mutual inductance between coil windings and the electrode lead loop, so amplitude scales with dI/dt and lead loop geometry. Pulse and decay artifact amplitudes are strongly correlated (ρ ≈ 0.86), confirming a shared physical origin. 14 of 23 configurations produced negative-polarity decay artifacts, and lead crossing can drive artifacts to near zero.

## Practical Recommendations

Ask for or report electrode lead/cable configuration when early responses are analyzed. Document lead routing direction and approximate loop geometry per session; test a few pulses and optimize routing before recording. For i-TEP claims, report lead configuration alongside amplifier specifications.

## Agent Rules Extracted

Do not interpret early topographies without considering lead configuration. When the decay artifact is large, check whether it tracks lead geometry (same polarity across trials, correlated with pulse) rather than physiology; if lead configuration is undocumented, treat early (<50 ms) topographic claims as provisional.

## Claims To Avoid

Avoid source/topography claims from early responses when lead setup is unknown.

## Questions This Source Helps Answer

How can EEG lead configuration affect early TMS-EEG artifacts?

## Related Cards

`artifacts/lead-configuration-early-artifacts.md`; `steps/early-response-baseline-and-reference.md`.
