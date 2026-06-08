---
type: step-card
id: filtering
title: Filtering
tags:
  - step:filtering
applies_to:
  - conservative-mne-python
  - tesa-inspired-two-pass-ica
load_with:
  - artifacts/pulse-artifact.md
  - steps/downsampling-and-resampling.md
---

## Purpose

Condition the signal for ICA, evoked analysis, and metrics while avoiding artifact spread.

## When To Apply

For the analysis dataset, apply filters late by default: after pulse artifact handling, bad-channel/bad-trial inspection, major TMS-related artifact cleaning, and any SOUND/SSP-SIR/ICA decisions. In SOUND/SSP-SIR-style workflows, this usually means after the ocular/movement ICA -> SOUND -> SSP-SIR sequence, plus any optional residual ICA. Do not filter across unhandled pulse transients.

A narrow exception is a separate ICA-training copy: a gentle high-pass or detrending step can sometimes improve ICA stability, but the agent must keep this distinct from the final analysis data and must not let an early high-pass silently define the TEP waveform.

## Inputs Needed

Sampling rate, analysis frequency band, artifact window, line noise frequency, and target metric.

## Decision Rules

Choose filters based on analysis goals. Preserve transparent reporting of passband, transition, phase, and order.

Do not apply filters across unhandled TMS pulse artifacts. Handle or mark/remove/interpolate the pulse window before filtering when the filter could spread the transient into the surrounding TEP window.

Prefer the late-filtering order used in the local MATLAB/TESA lesson for epoched data: pulse removal/interpolation -> bad channel/trial inspection -> ICA for ocular/movement/background muscle artifacts, avoiding TMS-stimulus-locked component rejection -> SOUND -> SSP-SIR for early TMS-evoked muscle artifact -> optional second artifact-window handling -> low-pass/notch filtering -> baseline -> downsample/trim -> final trial QC.

Use gentler filters when possible. Very steep cutoffs, narrow transition bands, and zero-phase filtering around sharp discontinuities can create ringing that resembles time-locked neural activity.

## Method Options

Low-pass, notch/bandstop, cautious bandpass, separate ICA-filtered copy when appropriate, and no filtering for diagnostic raw inspection. For short epoched TMS-EEG data, prefer baseline correction over a 1 Hz high-pass unless the high-pass was applied to long continuous data or is specifically justified.

## Learning Mode Explanation

Filters can smear sharp artifacts and alter component timing; pulse handling and gross artifact cleaning come first. The safest advisor default is to postpone analysis filters until the data no longer contain large sharp TMS-related transients.

Filter-induced ringing is an oscillatory artifact caused when a filter encounters a sharp edge or large transient. In TMS-EEG, this often means the TMS pulse, interpolation boundary, recharge artifact, muscle burst, or an abrupt epoch edge. Zero-phase filters can create ringing both before and after the transient; causal filters can shift timing and ring after the transient. Ringing near the pulse can be mistaken for early TEP or i-TEP components.

## Code-Engineer Notes

Verify MNE filter API and parameters through Context7/GitHub fallback.

## QC Checks

Plot frequency spectra and time-domain traces before/after; verify no ringing around the pulse, pulse-interpolation boundary, and early TEP/i-TEP windows. Compare active and sham/control conditions because filter ringing can become condition-specific if artifact morphology differs.

## Failure Modes

Filtering before interpolation, filtering across unhandled pulse artifacts, applying analysis high-pass filters too early, using a 1 Hz high-pass on short epochs, overly steep low-pass/notch filters, line-noise overcorrection, filter-induced ringing, and changing early-latency morphology.

## Sources

Local MATLAB/TESA lesson pipeline card; methodological choices paper card; pulse artifact step card; downsampling/resampling step card.
