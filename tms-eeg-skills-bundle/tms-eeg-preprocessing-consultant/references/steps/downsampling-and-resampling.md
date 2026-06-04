---
type: step-card
id: downsampling-and-resampling
title: Downsampling And Resampling
tags:
  - step:downsampling
  - step:resampling
  - artifact:sampling-sync
  - caution:filtering
  - caution:early-latency
applies_to:
  - conservative-mne-python
  - tesa-inspired-two-pass-ica
  - automated-artist-aaratep
  - itep-early-response-analysis
load_with:
  - steps/filtering.md
  - artifacts/sampling-sync-early-artifacts.md
  - artifacts/stimulation-intensity-sampling-rate-sync.md
---

## Purpose

Reduce data size and computational load while preserving timing, spectral content, and early TMS-EEG morphology.

## When To Apply

Downsampling is safest after the largest sharp TMS-related transients have been handled or removed from the data segment being resampled. In TMS-EEG, do not casually downsample raw continuous data that still contains unhandled pulse artifacts, recharge artifacts, or large decay transients.

Reasonable places to downsample can include:

- after pulse artifact removal/interpolation and gross artifact-window handling
- after epoching, if pulse windows and event timing are already verified
- after an initial high-rate i-TEP inspection has established which early windows are recoverable
- before computationally heavy ICA or automated steps, only if the target analysis does not require the original high sampling rate
- after producing/archiving a high-rate copy for i-TEP or pulse-artifact QC

Avoid downsampling before:

- verifying TMS trigger timing and pulse sample index
- defining pulse artifact and decay windows
- inspecting immediate or very early TEP windows
- checking whether anti-alias filtering smears the pulse into the early post-pulse interval

## Inputs Needed

Original sampling rate, target sampling rate, analysis endpoint, relevant frequency band, TMS pulse/removal window, trigger timing precision, whether i-TEPs are analyzed, and the resampling method/filter used by the software.

## Decision Rules

- Keep the original high-sampling data for provenance and early-artifact inspection.
- For i-TEPs or responses within the first few milliseconds, analyze and QC at the native high sampling rate whenever possible.
- If downsampling, choose a target rate high enough for the desired temporal and spectral resolution.
- Confirm the resampling function applies an appropriate anti-alias low-pass filter before decimation.
- Inspect whether the anti-alias filter spreads, rings, or shifts sharp TMS-related transients.
- Never compare conditions that were downsampled differently unless this is explicitly justified and tested.

## Why Aliasing Is Dangerous

Downsampling lowers the Nyquist frequency. Any signal energy above the new Nyquist frequency can fold back into lower frequencies as aliasing if it is not attenuated first. TMS-EEG data contain sharp, high-amplitude, broadband transients, so careless decimation can convert high-frequency pulse/muscle/artifact energy into lower-frequency activity that looks physiological.

Anti-alias filtering is therefore necessary, but it introduces a second risk: the filter itself can smear or ring around sharp events, especially around the TMS pulse.

## What Filter-Induced Ringing Is

Filter-induced ringing is an oscillatory artifact introduced by a filter when it is applied to a sharp edge, discontinuity, or high-amplitude transient. In TMS-EEG, the pulse artifact, interpolation boundaries, recharge artifact, muscle bursts, or abrupt epoch edges can trigger ringing.

Ringing can appear before and/or after the event, depending on filter type and phase:

- zero-phase filters can produce symmetric pre- and post-event ringing
- causal filters can produce post-event ringing and latency shifts
- steep filters and narrow transition bands can increase ringing
- filtering across an unhandled pulse artifact can spread pulse energy into the TEP window

## Learning Mode Explanation

Downsampling is not just "throwing away samples." A responsible resampling algorithm first low-pass filters the data so frequencies that cannot be represented at the lower sampling rate are removed. That anti-alias filter protects against spectral folding, but it can also distort sharp TMS artifacts. This is why TMS-EEG workflows usually handle the pulse artifact before filtering/resampling and then inspect the time-domain signal around the pulse after every major operation.

## Code-Engineer Notes

- In MNE-Python, prefer verified `Raw.resample()` / `Epochs.resample()` usage and document the target sampling rate. Check current MNE docs before writing exact parameters.
- In EEGLAB/TESA workflows, `pop_resample` is commonly used, but resampling should be placed deliberately in the pipeline and not before pulse/artifact-window decisions.
- For recipes, include an explicit native-rate QC copy or "do not downsample for i-TEP" branch when early responses are the endpoint.
- Avoid hard-coding universal target rates such as 1000 Hz; the correct value depends on early-latency goals, hardware, and preprocessing sequence.

## QC Checks

- Compare raw/native-rate and downsampled traces around each TMS pulse.
- Plot the first 50 ms post-pulse before and after resampling.
- Check for new oscillations around interpolation boundaries or the pulse.
- Confirm event latencies remain aligned after resampling.
- Compare spectra before/after and confirm expected attenuation above the new Nyquist limit.
- For i-TEPs, report why downsampling did or did not occur.

## Failure Modes

- Decimating without anti-alias filtering.
- Letting anti-alias filtering smear the TMS pulse into early TEP windows.
- Downsampling before pulse interpolation/removal.
- Losing sample-level timing needed for i-TEP analysis.
- Mistaking filter ringing for N15/P30 or immediate TEP activity.
- Resampling active and sham/control data inconsistently.

## Sources

General signal-processing rules for resampling and anti-aliasing; TMS-EEG methodological choices paper card; Jamil et al. 2024 sampling/synchronization card; early pulse residual risk and sampling-sync artifact cards.
