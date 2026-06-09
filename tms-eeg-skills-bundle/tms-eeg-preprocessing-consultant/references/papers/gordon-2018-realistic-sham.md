---
type: paper-card
id: gordon-2018-realistic-sham
title: Comparison of cortical EEG responses to realistic sham versus real TMS of human motor cortex
year: 2018
authors: Gordon et al.
source_pdf: ../../../../TMS-EEG-artifacts/articles/methodology/Exported Items/files/2056/Gordon et al. - 2018 - Comparison of cortical EEG responses to realistic sham versus real TMS of human motor cortex.pdf
doi: 10.1016/j.brs.2018.08.003
tags:
  - artifact:auditory
  - artifact:somatosensory
  - design:sham
use_for:
  - sham/control caveats
  - sensory confound discussion
confidence: seed-card
---

## Why This Matters For The Agent

Realistic sham comparisons are central to separating direct TMS-evoked cortical responses from sensory/control effects.

## Key Methods

Three M1 conditions — realistic sham vs. 90% RMT vs. 110% RMT — with active sensory masking and two-pass ICA. Subjects could not reliably distinguish realistic sham from 90% RMT (~67% correct, near chance). Despite this perceptual equivalence and matched masking, N45, N100, and P180 were significantly larger at 90% RMT than at sham, and sensory-related responses persisted after masking and ICA.

## Practical Recommendations

Ask whether realistic sham or sensory controls are present before interpreting active TMS TEPs. Perceptual indistinguishability between active and sham does not imply equivalent neural confounds; sham-subtracted TEPs at matched perceptual intensity are a stronger interpretive basis than active-only TEPs.

## Agent Rules Extracted

Active-vs-sham differences must be discussed with auditory/somatosensory confounds in mind. No pipeline (masking + ICA included) fully removes sensory contributions.

## Claims To Avoid

Do not treat sham-subtracted TEPs as automatically pure cortical activity.

## Questions This Source Helps Answer

How should realistic sham be used in TMS-EEG interpretation?

## Related Cards

`artifacts/auditory-somatosensory-confounds.md`.
