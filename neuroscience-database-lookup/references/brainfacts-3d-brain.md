# BrainFacts 3D Brain

Source: https://www.brainfacts.org/3d-brain

BrainFacts 3D Brain is an interactive educational brain anatomy page. Use it for explanatory anatomy lookups, teaching language, region names, and conceptual orientation. It is not a raw research dataset or a structured API.

## Best Uses

- Explain brain anatomy and function to a general audience.
- Identify broad brain regions for educational context.
- Link users to an interactive 3D anatomy resource.
- Pair with research databases when the user needs both simple explanation and primary sources.

## Page Characteristics

The page is a public interactive web resource with the title `3D Brain`. The HTML includes BrainFacts navigation categories such as:

- Thinking, Sensing & Behaving
- Diseases & Disorders
- Brain Anatomy & Function
- Neuroscience in Society
- In the Lab
- Explore
- 3D Brain
- Core Concepts
- Glossary

## Fetch Example

```bash
curl -L -s "https://www.brainfacts.org/3d-brain" |
  rg "3D Brain|Brain Anatomy|Diseases|Thinking|Glossary"
```

## Access Pattern

Use the page directly for interactive educational exploration:

```text
https://www.brainfacts.org/3d-brain
```

Do not treat this as a downloadable data repository. For scientific claims, supplement with paper/database lookups.

## Output Requirements

Return:

- The BrainFacts URL
- The anatomy concept or page section relevant to the user
- A plain-language summary
- A note that this is educational material, not raw data
