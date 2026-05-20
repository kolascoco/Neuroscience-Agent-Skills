---
name: tms-eeg-preprocessing-consultant
description: Plan, explain, and code TMS-EEG preprocessing workflows. Use for TMS-EEG artifact handling, TEP/GMFA/LMFP preprocessing, MNE-Python or tmseegpy code templates, TESA-inspired workflow reasoning, SOUND/SSP-SIR cleaning, quality-control planning, and immediate TEP/i-TEP early-response analysis with artifact caveats.
metadata:
  skill-author: local
---

# TMS-EEG Preprocessing Consultant

Use this skill when a user asks for TMS-EEG preprocessing advice, code, artifact handling, TEP/GMFA/LMFP computation, pipeline comparison, or immediate TEP/i-TEP analysis. The skill is a source-grounded methods assistant, not a replacement for dataset inspection or expert review.

## Core Workflow

1. **Classify the request** using `references/routing/question-routing.md`.
2. **Collect or infer critical metadata**: data format, continuous vs epoched, sampling rate, TMS event timing, target, analysis goal, active/sham/control conditions, EEG channel count/reference, and known artifacts.
3. **Load one pipeline card** from `references/pipelines/`, then only the step/artifact/repo/paper cards it names.
4. **Choose response mode**:
   - Learning mode: explain why each step matters, risks, and interpretation consequences.
   - Code-engineer mode: give concise steps, code templates, placeholders, and QC checks.
   - Default: combine short rationale with actionable code/steps.
5. **Use software lookup policy** from `references/routing/context7-or-github-fallback.md` before writing library-specific API calls.
6. **End with QC and caveats**, especially for early latencies, sensory confounds, muscle artifacts, ICA overcleaning, and condition-specific artifact differences.

## Pipeline Selection

- Conservative Python/MNE workflow: `references/pipelines/conservative-mne-python.md`
- TESA-inspired two-pass ICA workflow: `references/pipelines/tesa-inspired-two-pass-ica.md`
- SOUND/SSP-SIR enhanced workflow: `references/pipelines/sound-ssp-sir-enhanced.md`
- Automated ARTIST/AARATEP workflow: `references/pipelines/automated-artist-aaratep.md`
- TEP modeling / PyTepFit analysis branch: `references/pipelines/tepfit-network-modeling-analysis.md`
- Immediate TEP/i-TEP early-response branch: `references/pipelines/itep-early-response-analysis.md`

## Code Writing

Use recipes in `recipes/` as templates. They are not universal pipelines. Fill placeholders from user metadata and verify current APIs through Context7 or GitHub fallback before presenting runnable code.

Initial recipes:

- `recipes/load_mne_data.md`
- `recipes/detect_tms_events.md`
- `recipes/interpolate_pulse_artifact.md`
- `recipes/run_ica_with_qc.md`
- `recipes/compute_teps_gmfa_lmfp.md`
- `recipes/itep_early_window_analysis.md`
- `recipes/aaratep_matlab_skeleton.md`
- `recipes/qc_report.md`

For manually prepared extended paper digests and preprocessing tables, follow `references/routing/manual-digests-and-pipeline-tables.md`.

## Hard Rules

- Do not claim TEP, GMFA, LMFP, or i-TEP amplitude is a pure measure of cortical excitability.
- Do not invent function signatures. Query Context7 when available; otherwise inspect the GitHub fallback in repo cards.
- For i-TEPs, always mention residual pulse artifact, lead configuration, sampling/synchronization, recharge/decay, muscle artifact, and control-condition requirements.
- Separate methodological advice from code assumptions. If metadata is missing, state placeholders and what must be confirmed.
- Do not copy third-party source code into outputs unless license and scope are explicitly safe; prefer short templates and source links.
- Treat PyTepFit as a model-based analysis/interpretation tool for already preprocessed TEPs, not as an artifact-cleaning pipeline.
