---
type: artifact-card
id: auditory-somatosensory-confounds
title: Auditory And Somatosensory Confounds
tags:
  - artifact:auditory
  - artifact:somatosensory
  - caution:sensory-confounds
---

## What It Is

TEP activity partly driven by TMS click, scalp sensation, cranial muscle activation, expectation, or sham-control differences.

## Why It Matters

Several TEP components and condition differences can include sensory-evoked contributions rather than direct cortical effects at the target.

## Detection Clues

Similarity to auditory/somatosensory control responses, broad scalp topographies, condition differences in click/sensation, and late components such as N100. Spatial correlation between peripherally evoked potentials and TEPs emerges from roughly 60 ms post-pulse; components earlier than ~60 ms show little spatial overlap and are more likely to reflect direct cortical activity, though the N45 can still carry some sensory contribution (Biabani et al. 2019).

## Mitigation Options

Masking noise, realistic sham, sensory control conditions, active control targets, trial-level covariates, contrast/subtraction strategies such as auditory ERP subtraction when justified, and cautious interpretation. Among ICA, linear regression, and SSP-SIR for sensory-component removal, SSP-SIR offers the best tradeoff: it suppresses sensory contributions while better preserving non-sensory signal, whereas ICA broadly reduces all TEP peaks and linear regression distorts early source topographies (Biabani et al. 2019). When using SSP-SIR for this purpose, confirm that the projected PCs match peripheral-evoked-potential topographies rather than projecting blindly.

## Pipeline Implications

Preprocessing cannot solve poor controls. Keep condition labels separate and avoid removing sensory components without a defined analysis goal. By default, do not reject auditory/somatosensory-related ICA components; handle them through masking, appropriate condition contrasts, or justified subtraction/modeling.

## Interpretation Caveats

Do not present active-vs-sham TEP differences as direct cortical excitability unless sensory confounds are addressed. Masking reduces but cannot eliminate auditory input: even at maximal masking intensity, subjects still perceive the TMS click (Biabani et al. 2019). Perceptual masking success does not guarantee equivalent neural confounds — N45, N100, and P180 were larger at 90% RMT than at perceptually indistinguishable realistic sham despite active masking (Gordon et al. 2018). Reporting of perceived sensory experience remains rare across the literature, which limits cross-study auditing of sensory control.

Distinguish two claims that are often conflated. That peripherally evoked potentials (PEPs) **overlap and add to** TEPs is well supported, and PEPs can dominate later components. Whether sensory input additionally **modulates (interacts with)** the direct cortical response is a separate question: using saturated and individually PEP-matched shams, no significant PEP–TEP interaction was found within ~110 ms post-stimulation for M1 or SMA, supporting removal of PEPs by matched-sham subtraction (Gordon et al. 2026). The practical implication is that a well-matched sham can be subtracted to isolate the cortical TEP, but this does not license treating un-subtracted late components as artifact-free cortical activity, and the null-interaction result should not be over-extended beyond the tested window or targets.

## Sources

Biabani et al. 2019; Gordon et al. 2018; Gordon et al. 2026; `papers/methodological-choices-matter.md`; TMS click masking workflow.
