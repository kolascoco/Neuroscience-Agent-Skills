---
type: step-card
id: ssp-sir-cleaning
title: SSP-SIR Cleaning
tags:
  - step:ssp-sir
applies_to:
  - sound-ssp-sir-enhanced
load_with:
  - repos/pytep-sound-ssp-sir.md
---

## Purpose

Apply projection/subspace methods to attenuate structured TMS-related artifacts when justified.

## When To Apply

After pulse handling and with verified method assumptions.

## Inputs Needed

Artifact definition windows, projection parameters, rank information, validation plots, and plausible EEG channel coordinates. SSP-SIR/SOUND workflows need channel locations; missing or zero coordinates should be fixed before this step.

## Decision Rules

Track rank and compare evoked responses before/after. Do not project away early responses without explicit justification. Use `pc=2`, `time_range=[5, 50] ms`, `art_scale="manual"`, and `M=None` only as starting values from the local guide.

SSP-SIR mainly targets early TMS-evoked muscle artifact. It is not a full replacement for ICA. In TESA SOUND/SSP-SIR-style workflows, ICA for blinks, eye movements, and non-stimulus-locked/background muscle is commonly placed before SOUND and SSP-SIR, after pulse handling and bad-trial/channel cleanup. Do not remove TMS-evoked muscle artifacts with ICA, and do not reject components with clear TMS-stimulus-locked activity by ordinary ICA review. Use an additional post-SSP-SIR ICA pass only when residual non-stimulus-locked stereotyped artifacts remain and QC shows that component removal does not distort the TEP.

For DLPFC muscle artifact, distinguish short-window excision from SSP-SIR recovery. If the pipeline already removes/interpolates `-2` to `10-12 ms`, do not claim physiological interpretability inside that interval. If SSP-SIR is used to recover muscle-masked TEPs, inspect candidate components for strong high-frequency power, focal muscle-like topography, and a brief biphasic/MEP-like time course. Prefer sensitivity checks across `pc` values and artifact windows.

## Method Options

Use verified SSP-SIR implementation, MNE projection primitives if applicable, or pseudocode with source-check notes.

## Practical Starting Parameters

| Setting | Starting value | Notes |
|---|---|---|
| Pulse window | `[-2, 10] ms` | Conservative default before filtering |
| Longer pulse/recharge | `[-2, 12] ms` | Use when recovery extends later |
| Strong artifact | `[-5, 15] ms` | Use carefully; can erase early signal |
| Analysis high-pass | `0.1-1 Hz` only if justified | Match analysis goal; do not apply before pulse/high-amplitude artifact handling by default |
| Low-pass | `80-100 Hz` | Avoid excessive smoothing |
| Notch | `50/60 Hz` | Local mains |
| Baseline | `[-500, -50] ms` | Must be clean |
| SOUND `lambda_val` | `0.1` | `0.05` less aggressive; `0.2-0.3` for noisier data |
| SOUND `iter_num` | `5` | Try `10` only if diagnostics justify |
| SSP-SIR `art_scale` | `manual` | Best controlled default when artifact window is known |
| SSP-SIR `time_range` | `[5, 50] ms` | Early TMS-evoked muscle window; for DLPFC, verify against the actual biphasic burst and any samples already interpolated |
| SSP-SIR `pc` | `2` | `1` mild; `3-5` severe artifact only |
| SSP-SIR `M` | `None` | Let rank-based estimate handle it unless justified |

SSP-SIR muscle-artifact estimation is different from analysis high-pass filtering. TESA/PyTEP estimates the muscle-artifact subspace from a high-pass-filtered copy of the data, around `100 Hz`, so high-frequency muscle topographies can be identified. This method-internal copy should not be reported as a general instruction to high-pass filter the analysis waveform before pulse handling.

## Learning Mode Explanation

Projection methods remove dimensions of the data; that can clean artifacts but can also remove meaningful signal.

## Code-Engineer Notes

Always print/report projection count and rank effects.

## QC Checks

Rank, projection vectors/topographies, pre/post TEPs, early TEP attenuation, residual muscle artifact, and whether attenuation extends outside the artifact window. Always compare before/after cleaning around `0-100 ms`.

Under-cleaning clues:

- Large high-frequency burst remains around `5-50 ms`.
- Biphasic/MEP-like deflection remains near frontal/temporal/jaw/neck channels.
- Early post-TMS channels dominate the butterfly plot.
- RMS/peak-to-peak diagnostics remain high.

Over-cleaning clues:

- Early TEP peaks are flattened.
- Topographies become unnaturally smooth.
- Attenuation extends far outside the artifact window.

## Failure Modes

Rank loss, overprojection, condition imbalance, undocumented artifact windows, missing channel coordinates, and treating SSP-SIR as a complete preprocessing pipeline.

## Sources

PyTEP-SOUND-SSP-SIR repo card; SOUND/SSP-SIR pipeline card; local `SSP_SIR_PIPELINE.md` authoring note.
