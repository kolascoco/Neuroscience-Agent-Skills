# Clinical EEG and Big Data Resources

Use this reference when a user asks for EEG databases, clinical EEG, Parkinson or psychiatric EEG datasets, EEG biomarkers, or broad neuroscience "big data" repositories.

## TDBRAIN

Primary paper: van Dijk et al. (2022), "The two decades brainclinics research archive for insights in neurophysiology (TDBRAIN) database", Scientific Data. DOI: `10.1038/s41597-022-01409-z`.

Dataset access:

- Brainclinics Foundation resources: `https://www.brainclinics.com/resources`
- Synapse project: `https://www.synapse.org/TDBRAIN`
- Dataset DOI observed in the paper: `https://doi.org/10.70303/syn25671079`
- Code: `https://github.com/BCDgitprojects/TDBRAIN/`

What it contains:

- Clinical lifespan EEG database, ages 5-89.
- 1274 participants and 1346 EEG sessions.
- Heterogeneous psychiatric and clinical referrals, including major depressive disorder, ADHD, subjective memory complaints, OCD, tinnitus, insomnia, Parkinson disease, dyslexia, chronic pain, and healthy participants.
- Raw resting-state EEG, eyes-open and eyes-closed.
- Auditory oddball and visual 1-back behavioral task data.
- ECG, EOG, EMG/artifact channels and demographic, clinical, personality, and day-of-measurement metadata.
- Organized in BIDS and provided in BrainVision Analyzer readable format.

Access notes:

- Brainclinics access requires ORCID login and a Data Use Agreement.
- Synapse access requires registration and agreement to repository terms.
- Some clinical and treatment outcome data are blinded for prospective validation and replication.
- Use for biomarker replication, EEG preprocessing, de-artifacting methods, lifespan EEG patterns, psychiatric diagnostic/prognostic modeling, and treatment outcome prediction.

## Moscow State University EEG Database Links

Source: `http://brain.bio.msu.ru/eeg_database_links.htm`

Use this as an older HTML catalog for EEG records from the Laboratory for Neurophysiology and Neuro-Computer Interfaces.

Observed entries:

- `eeg_schizophrenia.htm` - EEG of healthy adolescents and adolescents with symptoms of schizophrenia.
- `eeg_mov_matrix_BCI.htm` - event-related potentials in a moving matrix modification of the P300 BCI.

Access pattern:

```bash
curl -L -s "http://brain.bio.msu.ru/eeg_database_links.htm" |
  rg "href=.*eeg_|EEG|Database"
```

Notes:

- This is an older HTML site, not an API.
- Follow the dataset-specific HTML page before reporting file formats, license, or citation details.
- Preserve the source page URL because deep links may be fragile.

## Narayanan Lab Datasets

Source: `https://narayanan.lab.uiowa.edu/datasets`

Use for Parkinson disease, cognitive control, interval timing, frontal theta, basal ganglia, stimulation, behavior, modeling, code, and EEG/LFP datasets.

Notable entries observed:

- Resting-state EEG measures cognitive impairment in Parkinson's disease.
- Resting-state EEG distinguishes depression in Parkinson's disease.
- Evoked mid-frontal activity predicts cognitive dysfunction in Parkinson's disease, with OpenNeuro links for Simon, Oddball, and Timing datasets.
- Timing variability and midfrontal rhythms correlate with cognition in Parkinson's disease.
- Multiple rodent timing, striatal, prefrontal, and stimulation datasets.

Access pattern:

```bash
curl -L -s "https://narayanan.lab.uiowa.edu/datasets" |
  rg "Parkinson|EEG|OpenNeuro|Code/Data|Dataset|Behavioral Data"
```

Notes:

- The page is a curated lab list with PubMed, OSF, OpenNeuro, Bitly, Dropbox, and other external links.
- Verify each target link before returning it because many entries redirect through short links.
- Report whether the result is raw data, processed data, code, behavioral data, modeling resources, or paper-only.

## Big Data Review Guidance

Primary paper: Dipietro et al. (2023), "The evolution of Big Data in neuroscience and neurology", Journal of Big Data. DOI: `10.1186/s40537-023-00751-2`.

Use this paper to improve dataset recommendations. When comparing neuroscience resources, evaluate them through:

- Volume: number of participants, sessions, files, channels, samples, images, or scans.
- Variety: modalities such as MRI, EEG, MEG, DTI, genetics, clinical assessments, behavior, wearables, and biospecimens.
- Velocity: whether data collection is fixed, ongoing, longitudinal, real-time, wearable-based, or periodically updated.
- Veracity: harmonization, quality control, missingness, site effects, measurement standards, preprocessing transparency, and experimental limitations.
- Value: whether the dataset supports clinical, preclinical, mechanistic, diagnostic, prognostic, educational, or benchmarking use.

Important recommendation for agents:

Do not rank datasets only by size. Prefer resources that have clear access terms, citation instructions, standardized formats, quality-control information, and enough metadata to support the user's scientific question.

Useful database families highlighted by the review include:

- Human Connectome Project and Connectome Coordination Facility resources.
- ADNI for Alzheimer disease neuroimaging and biomarkers.
- PPMI and PDBP for Parkinson disease biomarkers.
- DABI, EBRAINS, OpenNeuro, OASIS, Open MEG Archive, NeuroML-DB, Open Source Brain, iEEG.org, and NIH/NDA-style repositories.

When returning broad search results, include a short "Big Data Fit" note that calls out strengths and caveats across the 5 V's.
