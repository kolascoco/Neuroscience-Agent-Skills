# Oliva Lab Datasets

Source: http://olivalab.mit.edu/datasets.html

The MIT Computational Perception and Cognition lab dataset page collects visual cognition, memorability, scene understanding, and neuroimaging challenge datasets. Use it for fMRI/MEG responses to images/videos, natural scene stimuli, visual memorability, saliency, image datasets, and Algonauts challenge data.

## Best Uses

- Locate visual cognition datasets with brain responses.
- Find Algonauts challenge data and tutorials.
- Find fMRI/MEG datasets for image or video perception.
- Retrieve stimulus datasets used in cognitive neuroscience and computer vision.

## Notable Dataset Entries Observed

- **Algonauts Project 2023** - human brain responses to natural visual scenes; 8 subjects; 7T fMRI responses; 73,000 natural-scene images; includes ROI indices and Python Colab tutorial.
- **Algonauts Project 2021** - 1,102 three-second videos and fMRI human brain data for 10 subjects; form-gated download.
- **Algonauts Project 2019** - fMRI and MEG human brain data for image perception.
- **MEG and fMRI Data of Images** - MEG and fMRI data while 15 participants viewed images.
- **MEG and fMRI Data of Two Object Datasets** - object image stimuli, MEG RDMs, MEG epoched raw data, and fMRI data.
- **Human Brain Memorability/Machine Vision ROI resources** - fMRI image recognition experiments and ROI definitions.
- **LaMem**, **FIGRIM**, **SUN**, **Places**, **Memento10k**, and other visual cognition/computer vision datasets.

## Catalog Extraction

```bash
curl -L -s "http://olivalab.mit.edu/datasets.html" |
  rg "<h4|fMRI|MEG|brain|dataset|download|href" |
  sed -n "1,140p"
```

## Access Pattern

This is an HTML catalog, not one API. For a user query:

1. Fetch the catalog.
2. Extract relevant `<h4>` blocks and links.
3. Follow the dataset-specific link.
4. Report whether access is direct, form-gated, challenge-specific, or external.

## Output Requirements

Return:

- Dataset title
- Catalog URL and dataset-specific URL
- Data type: stimuli, fMRI, MEG, behavioral, memorability scores, ROI masks, model resources
- Subject/image/video counts when available
- Download/access restrictions
- Citation or project page when present
