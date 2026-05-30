# Ancestral Karyotypes

This directory contains reconstructed ancestral karyotypes used as references for collinearity-based comparative genomics.

## Karyotype folders

| Abbreviation | Full name |
|--------------|-----------|
| AAK   | Ancestral Angiosperm Karyotype |
| AMAK  | Ancestral Mesangiospermae Karyotype |
| AMK-A | Ancestral Monocot Karyotype (except Acoraceae) |
| AEK   | Ancestral Eudicot Karyotype |

## Files in each folder

Each karyotype folder contains four files:

- **ancestor**: chromosome–color correspondence, used to distinguish chromosomes in visualizations.
- **gff**: gene annotations, including chromosome, position, and length of each gene.
- **lens**: number of genes per chromosome, used for genome analysis.
- **pep**: protein sequences for the annotated genes.

## Purpose and usage

The goal of these ancestral gene sets is to provide collinearity information between ancestral and modern chromosomes, not to serve as a comprehensive gene catalog.

Each ancestral chromosome is built from a specific chromosome or region of an extant species. The set is then used to identify collinear blocks in modern species. Because the role of these genes is purely as anchors for collinearity, the set is not fixed and can be adjusted, for example:

- Expanding the genes within a collinear block to improve coverage in modern species.
- Replacing an ancestral chromosome with a homologous chromosome from another species when it gives a cleaner mapping.

The ultimate criterion for validating an ancestral karyotype is the location of chromosome fusion points, i.e., specific chromosomal regions in extant genomes, rather than the reconstructed ancestral gene set itself.
