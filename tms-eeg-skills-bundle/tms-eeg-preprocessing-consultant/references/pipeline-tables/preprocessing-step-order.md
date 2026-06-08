---
type: pipeline-table
id: preprocessing-step-order
title: Preprocessing Step Order Across TMS-EEG Pipelines
tags:
  - pipeline-tables
  - preprocessing-order
  - pipeline:artist
  - pipeline:tmseeg
  - pipeline:tesa
  - pipeline:sound-ssp-sir
  - step:rereference
  - step:downsampling
  - step:baseline
---

## Purpose

Use this card when a user asks where a step belongs in a TMS-EEG preprocessing workflow, or when comparing TESA, ARTIST/AARATEP, TMSEEG, SOUND/SSP-SIR, and conservative local workflows. The key lesson is that step order is method-specific; the agent should explain tradeoffs instead of imposing one universal pipeline.

This table is seeded from a user-provided summary table. Verify exact step windows and implementation details from the linked paper/repo cards before writing paper-specific methods or runnable code.

## Table

| Pipeline | Source cue | Summary order | Advisor interpretation |
|---|---|---|---|
| Al et al. 2023 | PLOS Biology, DOI `10.1371/journal.pbio.3002393` | Epochs -> long pre-baseline -> pulse artifact removal -> ICA 1 -> bandpass -> ICA 2 -> bad-channel interpolation -> second bandpass -> average reference -> downsample to 500 Hz | Supports late average reference and late downsampling after major artifact handling. Baseline window is unusually long and should be justified by epoch length and task design. |
| ARTIST | Wu et al. 2018, DOI `10.1002/hbm.23938` | Pulse artifact removal -> downsample to 1 kHz -> ICA for decay -> bandpass -> notch -> epochs -> bad epochs -> bad-channel interpolation -> ICA 2 -> average reference -> baseline | Early downsampling is source-specific and should not be copied blindly. If used, require anti-alias filtering QC and inspection of pulse/interpolation boundaries. Distinguish this ARTIST order from AARATEP implementation notes. |
| TMSEEG | Atluri et al. 2016, DOI `10.3389/fncir.2016.00078` | Pulse artifact removal -> epochs -> bad epochs/channels -> ICA for decay -> bandpass/notch -> ICA 2 -> bad epochs/channels -> average reference -> bad-channel interpolation -> baseline -> downsample to 1 kHz | Strongly illustrates iterative QC: remove high-amplitude/variable artifacts early, use ICA for consistent artifacts, then repeat bad trial/channel inspection. |
| TESA | Rogasch et al. 2017/TESA source cue `S1053811916305845` | Channel rejection -> epochs -> baseline -> pulse artifact removal/interpolation -> downsample to 1 kHz -> bad epochs -> ICA 1 -> bandpass/notch -> ICA 2 -> bad-channel interpolation -> average reference -> final baseline | Compatible with a TESA-style two-pass ICA card, but local lesson scripts may place some checks differently. Treat baseline and downsampling order as dataset/source-specific. |
| SOUND/SSP-SIR | SOUND/SSP-SIR source cue `S1053811917308480`, TESA SSP-SIR manual, and PyTEP-SOUND-SSP-SIR code | Epochs/pulse interpolation/baseline/QC as protocol-specific early steps -> bad epochs/channels -> ICA for ocular/movement/background artifacts when needed -> 1 Hz high-pass in some published SOUND/SSP-SIR pipelines before SOUND -> SOUND -> optional residual ICA -> SSP-SIR -> downsample/low-pass/re-epoch/baseline | Do not describe SOUND/SSP-SIR as "high-pass first" by default. The verified paper example places a 1 Hz high-pass after earlier pulse/ICA/QC steps and before SOUND; the TESA/PyTEP SSP-SIR implementation additionally creates an internal 100 Hz high-pass copy to estimate muscle-artifact topographies. Neither point means the analysis data should generally be high-pass filtered before pulse handling. The ICA slot here is for ocular, blink, eye-movement, and non-stimulus-locked/background muscle artifacts. Do not remove TMS-evoked muscle or clear TMS-stimulus-locked components with ordinary ICA rejection; use interpolation, projection/SSP-SIR, trial rejection, or target/protocol adjustment. |

## Cross-Pipeline Rules

- Pulse artifact handling is always an early decision, even if exact epoching/baseline order differs.
- For the advisor's default recommendation, place analysis filters late, after pulse removal/interpolation and major artifact cleaning. The local MATLAB/TESA lesson follows this order for low-pass/notch filtering.
- Filtering before pulse removal/interpolation can create ringing around the pulse; only follow such ordering when reproducing a source-specific protocol and inspect the result.
- If a high-pass/detrending step is used to improve ICA, label it as an ICA-training-data choice and keep it separate from the final analysis waveform whenever possible.
- Downsampling appears early in ARTIST, mid-pipeline in TESA, and late in TMSEEG/Al et al. 2023/SOUND-style summaries. Therefore downsampling should be decided from sampling rate, anti-aliasing, pulse handling, and the time/frequency features needed.
- Average rereferencing is usually late, after gross bad-channel handling and before final features. For GMFA/LMFP, apply the final reference across all EEG channels before ROI channel selection.
- Baseline windows vary widely across examples; choose the baseline from the study design, epoch length, stimulation timing, pre-pulse contamination, and the metric being computed.
- Bad epochs/channels may need to be inspected more than once: before ICA to stabilize decomposition and after ICA/filtering to catch residual artifacts.

## Mismatch Notes Against Current Skill Cards

The current preprocessing advisor is intentionally conservative and does not encode one canonical order. The user-provided table adds value by making the variability explicit.

Main differences to remember:

- `automated-artist-aaratep.md` follows the AARATEP README-style order, which should not be conflated with the original ARTIST summary order.
- `sound-ssp-sir-enhanced.md` recommends pulse handling before filtering for general use. Do not summarize SOUND/SSP-SIR as high-pass-first: some published workflows include a 1 Hz high-pass before SOUND after earlier cleanup, while SSP-SIR internally uses high-pass-filtered data only to estimate the muscle-artifact subspace.
- `sound-ssp-sir-enhanced.md` and the TESA SOUND/SSP-SIR example place ocular/movement ICA before SOUND and SSP-SIR. A later ICA pass is optional residual cleanup, not the default location for the main physiological-artifact ICA.
- `tesa-inspired-two-pass-ica.md` includes local lesson-script defaults and broader TESA-style logic; exact Rogasch/TESA paper order should be verified before methods-section wording.
- TMSEEG/Atluri 2016 should be used when the user asks about MATLAB GUI workflows, step-by-step interactive QC, or artifact database/visual feedback concepts.

## Notes For Agent Use

When asked "what is the correct order?", answer with:

1. the most defensible default for the user's data and target,
2. how that choice differs from major published pipelines,
3. which order-sensitive risks must be checked with QC plots.

Do not present baseline, downsampling, filtering, or rereferencing as universally fixed-position operations. However, when the user asks for the safest default rather than reproducing a named protocol, recommend late analysis filtering after TMS-specific artifact handling.

## Related Cards

- `pipelines/tesa-inspired-two-pass-ica.md`
- `pipelines/automated-artist-aaratep.md`
- `pipelines/sound-ssp-sir-enhanced.md`
- `steps/filtering.md`
- `steps/downsampling-and-resampling.md`
- `steps/tep-averaging.md`
- `steps/gmfa-lmfp-computation.md`
- `papers/atluri-2016-tmseeg.md`
- `papers/wu-2018-artist.md`
- `papers/rogasch-2016-tesa.md`
- `papers/mutanen-2022-source-based-artifact-rejection.md`
