---
type: paper-card
id: gordon-2026-somatosensory-inputs
title: Investigating the effects of TMS-related somatosensory inputs on TMS-evoked potentials provides evidence against significant interaction
year: 2026
authors: Gordon, Metsomaa, Belardinelli, Ziemann
source_pdf: ../../../../TMS-EEG-artifacts/articles/methodology/Exported Items/files/2055/Gordon et al. - 2026 - Investigating the effects of TMS-related somatosensory inputs on TMS-evoked potentials provides evid.pdf
doi: 10.1038/s41598-026-37418-w
tags:
  - artifact:somatosensory
  - caution:sensory-confounds
use_for:
  - sensory confound discussion
  - TEP interpretation caveats
confidence: seed-card
---

## Why This Matters For The Agent

Tests whether TMS-related somatosensory input *modulates* (interacts with) the cortical TEP, and whether sham subtraction is a valid way to remove peripherally evoked potentials (PEPs). Key nuance: PEPs overlap TEPs (PEPs emerge ~70 ms, with a negative deflection ~100 ms and positive ~200 ms, frontocentral), but the question here is interaction, not mere overlap.

## Key Methods

20 healthy right-handed participants, single session, M1 and SMA targets. Two sham designs compared: (1) "PEP saturation" — high-intensity somatosensory (scalp electric) stimulation in both sham and real TMS to saturate PEP amplitude so any extra sensory input causes little/no change; (2) "PEP individualized matching" — sham stimulus intensity individually tuned to match the PEP amplitude of real TMS. In both, PEPs from sham and real TMS should match, enabling subtraction. Logic: if post-subtraction TEPs do not differ between conditions / across sensory-intensity levels, there is no relevant PEP–TEP interaction, justifying PEP removal by subtraction (assessed by equivalence testing).

## Practical Recommendations

Results showed no significant TEP difference within ~110 ms post-stimulation after sham subtraction, regardless of sham protocol or whether M1 or SMA was stimulated — evidence *against* a relevant interaction between TMS-related somatosensory input and TEPs, and support for the validity of both sham protocols for removing PEPs by subtraction. Use to justify well-matched sham subtraction as a PEP-removal strategy, while still reporting the sham design and the analyzed window.

## Agent Rules Extracted

Sensory input should be considered, not hand-waved, in TEP interpretation — but this study indicates PEPs add (rather than multiplicatively interact) and can be removed by matched sham subtraction within the early/mid window. Distinguish "PEPs overlap TEPs" (true) from "sensory input modulates the cortical response" (not supported here).

## Claims To Avoid

Do not claim sensory input necessarily distorts/modulates the cortical TEP — the finding is the absence of significant interaction within ~110 ms. Do not extend the null-interaction result beyond the tested window/targets or treat unmatched sham as adequate.

## Questions This Source Helps Answer

Does TMS-related somatosensory input interact with the TEP, or merely add to it? Is sham subtraction a valid way to remove PEPs? Do the saturation and individualized-matching sham designs agree?

## Related Cards

`artifacts/auditory-somatosensory-confounds.md`; `papers/biabani-2019-sensory-inputs.md`; `papers/gordon-2018-realistic-sham.md`.
