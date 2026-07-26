# Methodology Extraction

The methodology block is the part of a literature note that decays least and gets reused most. Write it as data, not prose.

---

## Core rules

1. **Fields, not paragraphs.** `**Field**: value` lines. A reader scanning for "what intensity did they use" must find it in under two seconds.
2. **Numbers survive verbatim.** Exact values, exact units, exact test statistics. No rounding, no unit conversion, no hedging words. `120% RMT` never becomes "supra-threshold".
3. **`not reported` is a finding.** If the paper doesn't state it, write `not reported`. Never infer a plausible default and never leave the field out — an omitted field is indistinguishable from an oversight.
4. **Mark provenance when you reason.** `[inferred]` for anything you derived from a figure, a supplement, or a cited protocol paper; `[from ref: Smith2019]` when the method is delegated to another paper. Default (unmarked) = stated in the text.
5. **Recruited ≠ analysed.** Always record both, plus exclusions with reasons. Attrition is where a lot of studies quietly fall apart.
6. **What they did, not what it achieved.** No effect sizes, no "successfully", no "robustly" in this block. Those go under Results.
7. **Preserve their sequence.** Preprocessing and analysis pipelines are order-dependent; number the steps in the order performed.
8. **Ambiguity is recorded, not resolved.** `unclear whether X applied per-block or per-session` is a legitimate and useful field value.
9. **Close with gaps.** A final `**Reproducibility gaps**:` line listing every `not reported` / `unclear` item.

**Self-check before moving on:** could someone draft a replication protocol from this block alone? Every field they'd have to guess at should already be flagged as a gap.

---

## Universal fields (every empirical study)

```
**Design**: (between/within/mixed; RCT / quasi-exp / observational / cross-sectional / longitudinal / case series; blinding; randomization method; n conditions)
**Sample**: N recruited → N analysed; exclusions (n + reason each)
**Participants**: age (M ± SD, range); sex/gender breakdown as reported; handedness; population & recruitment source; inclusion & exclusion criteria
**Power**: a priori analysis? assumed effect size, α, target power, software — or `no power analysis reported`
**Materials / apparatus**: hardware + model, software + version, stimuli source
**Procedure**: sessions, blocks, trials per condition, timing, ISI/ITI + jitter, counterbalancing, session spacing
**Variables**: IVs with levels · DVs with units · covariates · control conditions
**Analysis**: statistical model (spelled out, incl. random-effects structure), software + version, α, multiple-comparison correction, effect-size measure, handling of missing data/outliers
**Open science**: preregistration (link/ID or `none`), data availability, code availability, ethics approval + committee
**Funding / COI**: only if notable
**Reproducibility gaps**: …
```

---

## Design-specific add-ons

### TMS / TMS-EEG
```
**Stimulator & coil**: make, model, coil geometry, pulse waveform (mono/biphasic), current direction
**Target & localization**: region, coordinates (MNI/Talairach), localization method (neuronavigation + e-field modelling / MRI-guided / scalp heuristic e.g. F3, 5cm rule)
**Coil orientation**: handle angle relative to midline/sulcus, tilt, hold method (fixed arm vs handheld), position tolerance
**Intensity**: value + reference (%RMT / %AMT / %MSO / SI1mV), thresholding method (visual, EMG criterion, ML/PEST), muscle used, RMT value itself
**Dose**: pulses per condition, protocol (single/paired/rTMS/TBS), ITI + jitter
**Control condition**: sham type (sham coil / tilted coil / active-sham with scalp electrical stim), matched for click and scalp sensation?
**Masking**: auditory masking (noise type, level in dB, individually tailored?), foam under coil, earplugs
**EEG**: amplifier + cap, n channels, sampling rate, online filters, reference & ground, impedance criterion, TMS-artifact handling at acquisition (sample-and-hold, DC vs AC)
**Preprocessing (ordered)**: 1. artifact window removal + interpolation (ms range) 2. downsampling 3. filters (type, order, cutoffs) 4. epoching + baseline window 5. bad-channel/trial rejection criteria 6. ICA (algorithm, n components, rejection criteria) 7. SOUND/SSP-SIR/other 8. re-reference
**Outcome quantification**: TEP components + time windows, ROI/electrode cluster, GMFA/LMFP, latency/amplitude definitions
**Artifact control checks**: reported? (decay, muscle, auditory-evoked-potential contamination, sham comparison)
```

### EEG / MEG (non-TMS)
```
**System**: amplifier, cap/sensor layout, n channels, sampling rate, online filters, reference, ground, impedance criterion
**Task/paradigm**: trial structure, n trials per condition, stimulus timing
**Preprocessing (ordered)**: filters (type, order, cutoffs, direction), re-referencing, epoching + baseline, artifact rejection criteria (automatic/manual, thresholds), ICA/SSP details, interpolation
**Analysis space**: sensor vs source; if source: head model, inverse solution, regularization
**Measures**: ERP components + windows + electrode clusters; time-frequency method (wavelet cycles, multitaper params), frequency bands with exact limits
**Statistics**: cluster-based permutation? (n permutations, cluster-forming threshold, cluster statistic), correction across time/space/frequency
```

### MRI / fMRI
```
**Scanner**: manufacturer, field strength, head coil channels
**Sequence**: TR, TE, flip angle, voxel size, slices, multiband factor, n volumes, fieldmap
**Preprocessing**: pipeline + version (e.g. fMRIPrep x.y.z), motion correction, normalization template, smoothing FWHM, motion scrubbing criteria
**Model**: GLM regressors, HRF, nuisance regressors, first- and second-level structure
**Thresholding**: cluster-forming threshold, correction method (FWE/FDR/TFCE), cluster extent, software
**ROIs**: definition (atlas + version, functional localizer, anatomical tracing)
```

### Meta-analysis / systematic review
```
**Protocol**: PRISMA adherence, registration (PROSPERO ID)
**Databases & dates**: sources searched, date range, last search date
**Search string**: as given (or `not reported` — common and worth flagging)
**Screening**: n screened → n full-text → k included; n screeners, agreement statistic
**Eligibility**: inclusion & exclusion criteria
**Included set**: k studies, total N, study designs
**Effect size metric**: measure + how computed from source stats
**Model**: fixed vs random effects, estimator (REML/DL), weighting
**Heterogeneity**: I², τ², Q
**Bias assessment**: risk-of-bias tool, publication-bias tests (funnel, Egger, p-curve, trim-and-fill)
**Moderators**: variables tested, method (meta-regression / subgroup)
```

### Clinical trial
```
**Registration**: trial ID + registry, pre- or post-hoc
**Arms**: n arms, allocation ratio, randomization + concealment method
**Blinding**: participants / providers / assessors / analysts; blinding integrity check
**Intervention**: dose, schedule, duration, adherence measurement
**Comparator**: placebo/active/TAU/waitlist
**Outcomes**: primary (pre-specified?), secondary, timepoints
**Analysis population**: ITT / per-protocol / modified ITT; dropout handling
**Adverse events**: monitoring + reporting
```

### Animal research
```
**Species/strain**, sex, age/weight, n per group, housing & light cycle
**Randomization & blinding**, exclusion criteria, ARRIVE compliance
**Procedures**: surgery, anaesthesia, drug doses + routes + timing
**Euthanasia & tissue processing**, ethics protocol number
```

### Computational / modelling / ML
```
**Model class & architecture**, free parameters, priors/initialization
**Data**: source dataset(s) + version, n samples, splits (train/val/test), leakage controls
**Fitting**: optimizer, loss, hyperparameter search method + grid, stopping criterion, seeds, n runs
**Validation**: cross-validation scheme, held-out test set, baselines compared
**Metrics**: exact definitions
**Compute & code**: hardware, runtime, repository link, dependency versions
```

### Qualitative
```
**Approach**: grounded theory / IPA / thematic analysis / ethnography
**Sampling**: strategy, n participants, saturation criterion
**Data collection**: interview/focus group, structure, duration, setting, transcription
**Analysis**: coding procedure, n coders, inter-coder agreement, software
**Rigor**: member checking, triangulation, audit trail, reflexivity statement
```

### Survey / questionnaire
```
**Instruments**: name, version, n items, response scale, reliability in *this* sample (α/ω) vs cited
**Administration**: online/in-person, platform, attention checks, order randomization
**Sampling**: frame, recruitment platform, compensation, response rate, completion rate
```

---

## Non-empirical sources

Do not fabricate a Methods section. Replace it:

- **Narrative review / theory** → `**Argument structure**` (premises → inferential moves → conclusion), `**Scope of literature covered**` (and how it was selected, if stated — usually not, worth flagging), `**Key assumptions**`
- **Methods/tool paper or docs** → `**Pipeline**` (ordered steps), `**Parameters & defaults**`, `**Validation performed**`, `**Known limitations / failure modes**`
- **Opinion / blog** → `**Claim**`, `**Reasoning**`, `**Evidence offered**` (and its type: data, anecdote, authority, analogy), `**Counterarguments addressed / ignored**`

---

## Red flags worth a line in the note

Record these under `Critical appraisal`, phrased as observations, not verdicts:

- No a priori power analysis, or one computed from the observed effect
- N per cell much smaller than the total N suggests
- Exclusion criteria that appear to have been decided after seeing the data
- Number of comparisons implied by the design vs number corrected for
- Outcome measures in Results that were not announced in Methods (or a preregistration that lists different ones)
- Method delegated entirely to a citation, with parameters that likely differed
- Control condition not matched on an obvious confound (in TMS-EEG: click, scalp sensation, coil position)
- Statistics reported without effect sizes or CIs
- Conclusions about a population the sample doesn't represent
- Author-stated limitations that are conspicuously narrower than the actual ones
