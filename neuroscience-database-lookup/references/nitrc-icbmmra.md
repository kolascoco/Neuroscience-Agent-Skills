# NITRC ICBM MRA Atlas

Source: https://www.nitrc.org/projects/icbmmra/

The NITRC Magnetic Resonance Angiography Atlas Dataset is a public NITRC resource for human brain arterial vasculature imaged with magnetic resonance angiography.

## Best Uses

- Retrieve the ICBM MRA atlas download.
- Find human MRA/NIfTI data for cerebral arterial vasculature.
- Cite dataset provenance and technical parameters.
- Link BRAVA-style vascular morphology questions to a source MRA atlas.

## Key Metadata Observed

- Project: `Magnetic Resonance Angiography Atlas Dataset`
- NITRC group ID: `1113`
- Main download: `mra_brains.tar`
- Direct observed download path: `/frs/download.php/9725/mra_brains.tar`
- File size shown by NITRC: about `1010140 K`
- Format association: `NIfTI`
- License shown: `Freeware`
- Registered: Feb 1, 2017
- Data description: 3T time-of-flight MRA, high-resolution `620 um isotropic`
- Sample: 61 healthy volunteers, 36 female / 25 male, average age 31.2 +/- 10.7, range 19-64 years

## Project Page

```bash
curl -L -s "https://www.nitrc.org/projects/icbmmra/" |
  rg "Magnetic|mra_brains|NIfTI|Freeware|volunteers|isotropic|download.php"
```

## Download

```bash
curl -L -o mra_brains.tar \
  "https://www.nitrc.org/frs/download.php/9725/mra_brains.tar"
```

If the direct download fails, use:

```text
https://www.nitrc.org/frs/?group_id=1113
```

## Output Requirements

Return the project URL, group ID, file link, observed metadata, license label, file format, and any access issue. For analysis, recommend checking contents after extraction:

```bash
tar -tf mra_brains.tar | head
```

Use `nibabel` for NIfTI inspection once downloaded.
