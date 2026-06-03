---
type: paper-card
id: gordon-2026-somatosensory-inputs
title: Investigating The Effects Of TMS-Related Somatosensory Inputs On TMS-Evoked Potentials Provides Evidence Against Significant Interaction
year: 2026
authors: Gordon PC; Metsomaa J; Belardinelli P; Ziemann U
source_pdf: ../../../../TMS-EEG-artifacts/articles/methodology/Exported Items/files/2055/Gordon et al. - 2026 - Investigating the effects of TMS-related somatosensory inputs on TMS-evoked potentials provides evid.pdf
doi: 10.1038/s41598-026-37418-w
tags:
  - somatosensory-control
  - sham
  - pep
  - tep-interpretation
  - m1
  - sma
use_for:
  - planning realistic sham and somatosensory control conditions
  - deciding whether PEP subtraction assumptions are plausible
  - explaining late N100/P200 sensory confounds
confidence: high
---

## Why This Matters For The Agent

This paper directly addresses whether TMS-related somatosensory inputs merely overlap with TEPs as peripheral evoked potentials (PEPs), or whether they substantially modulate TMS-driven cortical responses. It is a planning source for sham/control design rather than a generic preprocessing source.

## Key Methods

- Compared real TMS with sham designs intended to match or saturate PEPs.
- Tested M1 and SMA targets.
- Used MRI-guided neuronavigation.
- Recorded EEG at high sampling frequency with masking noise.
- Compared sham-subtracted TMS-EEG responses within early post-stimulation windows.

## Practical Recommendations

- Plan somatosensory controls before acquisition; do not try to infer them after preprocessing.
- Consider either individualized PEP matching or high-intensity PEP saturation when the study relies on subtracting sensory responses.
- Report whether sham/control PEPs actually resemble real-TMS PEPs.
- Treat N100/P200-dominated effects with caution unless sensory controls are strong.
- If the target can produce motor output, monitor EMG and consider excluding trials with MEPs when reafference would confound the EEG endpoint.

## Agent Rules Extracted

- When the user asks for sham/control planning, ask whether they need auditory-only, somatosensory-only, realistic sham, active control, or PEP-subtraction logic.
- Recommend sensory ratings and online inspection of sham-real similarity when interpretation depends on subtraction.
- State that evidence for absent PEP-TEP interaction in this study does not remove the need to match PEPs in the user's own setup.

## Claims To Avoid

- Do not claim that somatosensory inputs are irrelevant to all TMS-EEG designs.
- Do not claim that sham subtraction is valid without checking PEP matching.
- Do not generalize M1/SMA results to every target, coil, intensity, or population without caveats.

## Questions This Source Helps Answer

- How should I design somatosensory controls?
- Can I subtract sham responses from real TMS?
- Why are late TEP components vulnerable to sensory confounds?
- What should I report about sham/control design?

## Related Cards

- `references/design/sham-and-sensory-controls.md`
- `references/papers/gordon-2018-realistic-sham.md`
- `references/papers/grasin-2019-realistic-sham.md`
- `references/targets/m1.md`
- `references/targets/sma.md`
