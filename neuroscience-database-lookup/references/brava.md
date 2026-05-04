# BRAVA

Source: http://cng.gmu.edu/brava/all_subjects.php?clear=1

BRAVA is a browsable brain arterial/vascular reconstruction resource hosted by the Center for Neural Informatics, Structures, and Plasticity at George Mason University. Use it for subject-level cerebral arterial tree files, SWC downloads, vascular morphology metrics, and artery-specific filtering.

## Best Uses

- Browse all available vascular reconstruction subjects.
- Download all SWC files as a ZIP.
- Inspect a subject page by ID.
- Filter by vascular territory: complete, ACA, MCA, PCA.
- View or extract vascular morphology metrics.

## Main Pages

```text
http://cng.gmu.edu/brava/all_subjects.php?clear=1
http://cng.gmu.edu/brava/search_advanced.php
http://cng.gmu.edu/brava/metrics.php
http://cng.gmu.edu/brava/files/swc_files.zip
```

## Browse All Subjects

```bash
curl -L -s "http://cng.gmu.edu/brava/all_subjects.php?clear=1" |
  rg "query_subject.php|swc_files.zip|metrics.php|type_metric"
```

Observed page features:

- A `Download swc files` button linking to `files/swc_files.zip`
- A `View statistics for metrics` form pointing to `metrics.php`
- Territory filters for `complete`, `aca`, `mca`, and `pca`
- Subject links such as `query_subject.php?id=1`, `query_subject.php?id=2`, etc.
- Subject codes such as `BG001`, `BG0002`, `BG0003`, and many more

## Download SWC Files

```bash
curl -L -o brava_swc_files.zip \
  "http://cng.gmu.edu/brava/files/swc_files.zip"
```

## Subject Page

```bash
curl -L -s "http://cng.gmu.edu/brava/query_subject.php?id=1"
```

Parse the returned HTML for metadata, links to files, and metric tables.

## Territory Filter Examples

```bash
curl -L -s "http://cng.gmu.edu/brava/all_subjects.php?type_metric=aca&ad_search="
curl -L -s "http://cng.gmu.edu/brava/all_subjects.php?type_metric=mca&ad_search="
curl -L -s "http://cng.gmu.edu/brava/all_subjects.php?type_metric=pca&ad_search="
```

## Output Requirements

This is not a JSON API. Return structured extracted HTML results:

- Page URL
- Number/list of subject links found
- Download ZIP URL
- Any selected subject metadata
- Any metric names or filters used

Mention that SWC files are neuronal/vascular tree-style morphology files and should be parsed with tools that understand SWC tabular morphology.
