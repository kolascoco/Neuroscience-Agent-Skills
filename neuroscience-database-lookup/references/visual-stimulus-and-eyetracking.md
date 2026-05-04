# Visual Stimulus and Eye-Tracking Datasets

Use this reference for cognitive neuroscience, visual cognition, memory, attention, saliency, eye tracking, fMRI task stimuli, object photos, emotional faces, natural images, memorability, and experiment stimulus selection.

## Bank of Standardized Stimuli (BOSS)

User-provided dataset link:

```text
https://drive.google.com/drive/folders/1FpnEFkbqe_huRwfsCf7gs5R1zuc1ZOkn
```

Canonical project page cited in BOSS Phase II:

```text
https://sites.google.com/site/bosstimuli/
```

Primary references:

- Brodeur et al. (2010), "The Bank of Standardized Stimuli (BOSS), a new set of 480 normative photos of objects to be used as visual stimuli in cognitive research", PLOS ONE. DOI: `10.1371/journal.pone.0010773`.
- Brodeur et al. (2014), "Bank of Standardized Stimuli (BOSS) Phase II: 930 New Normative Photos", PLOS ONE. DOI: `10.1371/journal.pone.0106953`.

Use for:

- Object recognition, naming, memory, semantic category, manipulation, visual complexity, familiarity, and psycholinguistic control.
- Selecting standardized object photos with norms rather than uncontrolled image search results.

Notes:

- BOSS Phase II reports 930 new normative photo stimuli and describes the full BOSS resource as a large photo bank with norms across more than 15 dimensions.
- The BOSS resource includes normative color photos, non-normative exemplars, alternate viewpoints, and some black-and-white line drawing versions.
- Check the Google Drive and canonical page before promising exact file counts.

## ABCD fMRI Tasks and Emotional Stimuli

Source: `https://abcdstudy.org/scientists/abcd-fmri-tasks-and-tools/`

Use for:

- ABCD fMRI task programs and stimuli.
- Monetary Incentive Delay task.
- Stop Signal task.
- Emotional N-Back task.
- RADIATE Emotional Face Stimulus Set.

Access notes observed:

- Tasks are provided for research and educational purposes.
- ABCD notes E-Prime Professional 2.0 compatibility and scanner-specific downloads for GE, Siemens/Philips, and Goggles variants.
- Emotional N-Back downloads include practice, behavioral, and recognition-memory materials.
- RADIATE emotional face stimuli require agreement to approved institutional research or educational use and non-identification of photographed individuals.
- Preserve the ABCD page citation guidance when returning these links.

## Large-Scale Image Memorability (LaMem)

Source: `http://memorability.csail.mit.edu/`

Use for:

- Image memorability prediction.
- Natural image memory benchmarks.
- Cognitive/computational neuroscience work that needs memorability scores.

Observed details:

- LaMem contains 60,000 images from diverse sources.
- The project page provides download access for LaMem and MemNet.
- The page provides an image memorability API, but warns not to overload the free academic server.

Citation:

- Khosla et al. (2015), "Understanding and Predicting Image Memorability at a Large Scale", ICCV. DOI: `10.1109/ICCV.2015.275`.

## Contextual Guidance of Eye Movements

Source: `https://people.csail.mit.edu/torralba/GlobalFeaturesAndAttention/`

Use for:

- Real-world scene search.
- Eye movements and attention.
- Global scene features, saliency, and contextual guidance models.

Observed downloads:

- Paper PDF.
- Images.zip.
- Fixation data.zip.
- LabelMe links for training datasets such as person search, painting search, and mug search.

Citation:

- Torralba, Oliva, Castelhano, and Henderson (2006), "Contextual guidance of eye movements and attention in real-world scenes: The role of global features on object search", Psychological Review.

## FIGRIM Fixation Dataset

Source: `http://figrim.mit.edu/index_eyetracking.html`

Use for:

- Scene memorability.
- Eye fixation prediction.
- Saliency model training and testing.
- Object annotation plus fixation analyses.

Observed details:

- 2,787 images across 21 indoor and outdoor scene categories.
- 630 target images and over 2,000 filler images.
- Target images include fixation data, memorability scores, precomputed fixation maps, and complete object annotations.
- Filler images include fixation data and precomputed fixation maps.
- Downloads include images, fixation maps, fixation locations, metadata, object annotations, and code.
- Academic research purpose only notice appears on the page.

Citation:

- Bylinskii et al. (2015), "Intrinsic and Extrinsic Effects on Image Memorability", Vision Research.

## Selection Guidance

| User asks for... | Prefer |
|---|---|
| Standardized object photos | BOSS |
| Emotional faces or ABCD-compatible fMRI tasks | ABCD fMRI Tasks and RADIATE |
| Image memorability scores at scale | LaMem |
| Eye movements during contextual object search | Contextual Guidance of Eye Movements |
| Fixations, saliency maps, memorability, and object annotations | FIGRIM Fixation Dataset |
| Broad visual cognition and neuroimaging datasets | Oliva Lab datasets |

## Output Requirements

Return:

- Dataset name and direct source URL.
- Stimulus type: objects, scenes, emotional faces, fMRI task scripts, fixation maps, images, or annotations.
- Participant/observer counts if available.
- Image/task counts if available.
- File formats and download links observed.
- Citation and license/use restrictions.
- Whether the link is direct, Google Drive, GitHub, institutional page, form-gated, or API-like.
