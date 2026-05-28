# Angiosperm Karyotype Evolution

This repository contains the data and code associated with our study on ancestral karyotype reconstruction in angiosperms. It includes genome data for 30+ species, reconstructed ancestral karyotypes, a fusion positions database, and step-by-step construction workflows using the [WGDI](https://github.com/SunPengChuan/wgdi) toolkit.

## Repository Structure

| Directory | Description |
|-----------|-------------|
| `genome/` | Genome data (gff, lens, cds, pep) for all sampled species |
| `Karyotype/` | Reconstructed ancestral karyotypes: AAK, AEK, AMAK, AMK-A |
| `fusion_positions_database/` | Chromosomal fusion positions database |
| `AAK_construction/` | Step-by-step workflow and intermediate files for AAK construction |
| `dotplot/` | Dotplot figures comparing pairwise genome synteny |
| `figures/` | Figures used in the paper |

## Ancestral Karyotypes

Four ancestral karyotypes are reconstructed and provided in `Karyotype/`:

| Abbreviation | Full name |
|---|---|
| AAK | Ancestral angiosperm karyotype |
| AMAK | Ancestral Mesangiospermae karyotype |
| AMK-A | Ancestral monocot karyotype (excluding Acoraceae) |
| AEK | Ancestral eudicot karyotype |

Each karyotype folder contains four files:

- `.ancestor` — chromosome-to-color mapping for visualization
- `.gff` — gene annotation (location and length)
- `.lens` — gene count per chromosome
- `.pep.fa` — protein sequences

> Note: the ancestral gene sets are intended to represent collinearity between ancestral chromosomes, not as comprehensive gene catalogs.

## Genome Data

Species included (abbreviations used in filenames):

| Species | Abbreviation |
|---|---|
| *Amborella trichopoda* | atr42s |
| *Nymphaea colorata* | nc476s |
| *Brasenia schreberi* | bsc1s |
| *Illicium verum* | ive |
| *Liriodendron chinense* | lc2s |
| *Cinnamomum kanehirae* | cm170s |
| *Chloranthus sessilifolius* | cs471s |
| *Aristolochia fimbriata* | afi49s |
| *Ceratophyllum demersum* | cd4s |
| *Vitis vinifera* | vvi161s |
| *Aquilegia coerulea* | ac472s |
| *Acorus gramineus* | agr8s |
| *Asparagus setaceus* | ase9s |
| *Acanthochlamys bracteata* | abr7s |
| *Ananas comosus* | aco40s |
| *Dioscorea alata* | da480s |
| *Elaeis guineensis* | elg3s |
| *Musa acuminata* | mac41s |
| *Oryza sativa* | os53s |
| *Zostera marina* | zma82s |
| *Spirodela polyrhiza* | spo4s |
| *Dendrobium chrysotoxum* | dch50s |
| *Euryale ferox* | ef3s |
| *Ginkgo biloba* | gbi44s |
| *Sequoiadendron giganteum* | sgi44s |
| *Azolla filiculoides* | afi61s |
| *Selaginella moellendorffii* | smo62s |
| *Physcomitrium patens* | ppt60s |

## Usage

All analyses depend on the [WGDI](https://github.com/SunPengChuan/wgdi) toolkit. A detailed reconstruction walkthrough is available at [wgdi-example](https://github.com/SunPengChuan/wgdi-example/).

The [`AAK_construction/commond.md`](AAK_construction/commond.md) file documents the full step-by-step process used to build the AAK, including WGDI commands and intermediate dotplot checkpoints.

## Citation

> (Paper citation to be added upon publication)

---

## Background

### What is Karyotype Evolution?

Karyotype comprises both chromosome numbers and character of each chromosome for one species. Karyotype evolution represents chromosomal changes from the ancestral genome to the modern genome. This information is critical for reconstructing ancestral karyotypes and tracing how modern species evolved step by step.

In the long evolutionary history of a species, ancestral chromosomes fuse or fission gradually and randomly in offspring lineages, meaning each intact ancestral chromosome (protochromosome) could be retained across highly diverged lineages. Lineages closer to the common ancestor with fewer genome changes (e.g., fewer whole-genome duplications, WGD) tend to retain more protochromosomes. Syntenic blocks serve as the key evidence for identifying fusion and fission events.

### Method

Previous approaches define contiguous ancestral regions (CARs) based on collinearity, but suffer from gap regions caused by structural abnormalities and short syntenic blocks. Our approach instead identifies protochromosomes by searching for shared intact chromosomes or chromosome-like syntenic blocks (CLSBs) across highly diverged lineages.

The spiral workflow consists of three iterative steps:
1. Identify CLSBs by pairwise genome comparisons
2. Extract the most intact CLSBs as protochromosomes, adding telomeres at their ends
3. Remove identified protochromosomes and connect flanking regions, then repeat until no genomic block remains

**Three basic chromosomal fusion types** are recognized:

- **RCT** — Reciprocal chromosome translocated
- **EEJ** — End-end joining (Robertsonian translocation)
- **NCF** — Nested chromosome fusion

![Karyotype evolution model](figures/Karyotype%20evolution%20model.png)

Fusion positions are highly specific: the probability that a later structural variation breakpoint coincides with a protochromosome fusion site is extremely low, making fusion positions reliable phylogenetic markers. Inversions similarly have little effect on karyotype reconstruction.

### Applications

1. Paleogenomics — reconstructing evolutionary trajectories of species
2. Phylogenetics and species taxonomy
3. Verification of genome assembly quality
4. Detection of autopolyploidy or allopolyploidy
