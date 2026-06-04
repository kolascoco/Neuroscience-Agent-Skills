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

After pulse artifact handling, not across unhandled pulse transients.

## Inputs Needed

Sampling rate, analysis frequency band, artifact window, line noise frequency, and target metric.

## Decision Rules

Choose filters based on analysis goals. Preserve transparent reporting of passband, transition, phase, and order.

Do not apply filters across unhandled TMS pulse artifacts. Handle or mark/remove/interpolate the pulse window before filtering when the filter could spread the transient into the surrounding TEP window.

Use gentler filters when possible. Very steep cutoffs, narrow transition bands, and zero-phase filtering around sharp discontinuities can create ringing that resembles time-locked neural activity.

## Method Options

High-pass/low-pass, notch filtering, separate ICA-filtered copy when appropriate, and no filtering for diagnostic raw inspection.

## Learning Mode Explanation

Filters can smear sharp artifacts and alter component timing; pulse handling comes first.

Filter-induced ringing is an oscillatory artifact caused when a filter encounters a sharp edge or large transient. In TMS-EEG, this often means the TMS pulse, interpolation boundary, recharge artifact, muscle burst, or an abrupt epoch edge. Zero-phase filters can create ringing both before and after the transient; causal filters can shift timing and ring after the transient. Ringing near the pulse can be mistaken for early TEP or i-TEP components.

## Code-Engineer Notes

Verify MNE filter API and parameters through Context7/GitHub fallback.

## QC Checks

Plot frequency spectra and time-domain traces before/after; verify no ringing around the pulse, pulse-interpolation boundary, and early TEP/i-TEP windows. Compare active and sham/control conditions because filter ringing can become condition-specific if artifact morphology differs.

## Failure Modes

Filtering before interpolation, filtering across unhandled pulse artifacts, overly aggressive high-pass, overly steep low-pass/notch filters, line-noise overcorrection, filter-induced ringing, and changing early-latency morphology.

## Sources

Methodological choices paper card; pulse artifact step card; downsampling/resampling step card.
