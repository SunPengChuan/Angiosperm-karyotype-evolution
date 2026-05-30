# Fusion Points Database

This database catalogues chromosome fusion points identified in extant angiosperm genomes. Each fusion point is recorded as a small gene set (~200 genes total, ~100 genes on each side of the fusion point) extracted from the corresponding chromosome of an extant species. These extracted regions are the units we use to validate ancestral karyotype reconstructions.

## Fusion Points Table

The table below is the master record of the database. Each row defines one extracted gene set, identified by a `Mark` (e.g., `A1`, `B2`). Rows sharing a chromosomal rearrangement event are grouped together; the trailing number on the Mark indexes independent observations of that event in different species.

| Chromosomal Rearrangement | Species                     | Chr   | Position | Mark |
|---------------------------|-----------------------------|-------|----------|------|
| AAK/1_2/NCF               | *Amborella trichopoda*      | Chr1  | 1218     | A1   |
| AAK/1_2/NCF               | *Amborella trichopoda*      | Chr1  | 2287     | A2   |
| AAK/1_2/NCF               | *Nymphaea colorata*         | Chr1  | 3091     | A3   |
| AAK/1_2/NCF               | *Nymphaea colorata*         | Chr1  | 3358     | A4   |
| AAK/9_15/EEJ              | *Trithuria bibracteata*     | Chr3  | 495      | Q1   |
| AAK/9_15/EEJ              | *Nymphaea colorata*         | Chr5  | 712      | Q2   |
| AAK/7_14/EEJ              | *Trithuria bibracteata*     | Chr4  | 1430     | R1   |
| AAK/7_14/EEJ              | *Nymphaea colorata*         | Chr4  | 2015     | R2   |
| AAK/7_14/EEJ              | *Nymphaea colorata*         | Chr4  | 1777     | R3   |
| AAK/7_16/EEJ              | *Illicium verum*            | Chr8  | 655      | B1   |
| AAK/7_16/EEJ              | *Theobroma cacao*           | Chr3  | 1840     | B2   |
| AAK/7_16/EEJ              | *Elaeis guineensis*         | Chr4  | 898      | B3   |
| AAK/7_16/EEJ              | *Ananas comosus*            | Chr3  | 490      | B4   |
| AAK/2_11/EEJ              | *Illicium verum*            | Chr9  | 1290     | O1   |
| AAK/2_11/EEJ              | *Acorus gramineus*          | Chr4  | 188      | O2   |
| AAK/2_11/EEJ              | *Aquilegia coerulea*        | Chr3  | 3896     | O3   |
| AAK/2_11/EEJ              | *Theobroma cacao*           | Chr3  | 738      | O4   |
| AAK/2_11/EEJ              | *Arabidopsis thaliana*      | Chr1  | 5814     | O5   |
| AAK/1_9/RCT               | *Aquilegia coerulea*        | Chr2  | 3229     | C1   |
| AAK/1_9/RCT               | *Acorus gramineus*          | Chr1  | 1390     | C2   |
| AAK/1_9/RCT               | *Theobroma cacao*           | Chr9  | 1424     | C3   |
| AAK/(1_9/RCT)_6/EEJ       | *Acorus gramineus*          | Chr3  | 1987     | P1   |
| AAK/(1_9/RCT)_6/EEJ       | *Aquilegia coerulea*        | Chr7  | 3021     | P2   |
| AAK/(1_9/RCT)_6/EEJ       | *Theobroma cacao*           | Chr9  | 37       | P3   |
| AAK/(2_11/EEJ)_5/RCT      | *Acorus gramineus*          | Chr4  | 2327     | D1   |
| AAK/(2_11/EEJ)_5/RCT      | *Theobroma cacao*           | Chr9  | 610      | D2   |
| AAK/(2_11/EEJ)_5/RCT      | *Acorus gramineus*          | Chr4  | 132      | E1   |
| AAK/(2_11/EEJ)_5/RCT      | *Aquilegia coerulea*        | Chr3  | 2892     | E2   |
| AAK/(2_11/EEJ)_5/RCT      | *Theobroma cacao*           | Chr6  | 1645     | E3   |
| AMAK/5_11/EEJ             | *Dioscorea alata*           | Chr17 | 375      | F1   |
| AMAK/5_11/EEJ             | *Dioscorea alata*           | Chr17 | 1105     | F2   |
| AMAK/5_11/EEJ             | *Spirodela polyrhiza*       | Chr8  | 448      | F3   |
| AMAK/5_11/EEJ             | *Spirodela polyrhiza*       | Chr8  | 797      | F4   |
| AMAK/2_6/EEJ              | *Dioscorea alata*           | Chr14 | 831      | G1   |
| AMAK/2_6/EEJ              | *Spirodela polyrhiza*       | Chr7  | 538      | G2   |
| AMAK/2_6/EEJ              | *Ananas comosus*            | Chr21 | 379      | G3   |
| AMAK/7_9/EEJ              | *Ananas comosus*            | Chr22 | 460      | H1   |
| AMAK/8_12/EEJ             | *Ananas comosus*            | Chr4  | 763      | I1   |
| AMAK/8_12/EEJ             | *Ananas comosus*            | Chr13 | 278      | I2   |
| AMAK/1_4_13/mix           | *Dioscorea alata*           | Chr13 | 359      | J1   |
| AMAK/1_4_13/mix           | *Dioscorea alata*           | Chr13 | 392      | J2   |
| AMAK/1_4_13/mix           | *Dioscorea alata*           | Chr8  | 536      | J3   |
| AMAK/1_4_13/mix           | *Elaeis guineensis*         | Chr13 | 108      | J4   |
| AMK-A/1_8/EEJ             | *Acanthochlamys bracteata*  | chr6  | 1228     | K1   |
| AMK-A/2_7/EEJ             | *Ananas comosus*            | Chr6  | 645      | L1   |
| AMK-A/2_7/EEJ             | *Ananas comosus*            | Chr6  | 598      | L2   |
| AMK-A/2_8/NCF             | *Ananas comosus*            | Chr15 | 116      | M1   |
| AMK-A/2_8/NCF             | *Ananas comosus*            | Chr15 | 713      | M2   |
| AMK-A/1_7/EEJ             | *Ananas comosus*            | Chr19 | 440      | N1   |

`Position` is the gene order index of the fusion point on the source chromosome.

### Rearrangement type codes

- **NCF**: nested chromosome fusion
- **EEJ**: end-to-end joining
- **RCT**: reciprocal translocation
- **mix**: complex/mixed rearrangement
- Compound notations such as `(1_9/RCT)_6/EEJ` describe stepwise events (here, the RCT product of chr 1 and 9 then end-joined with chr 6).

## Extracted Gene Set

For each Mark, ~200 genes are extracted from the source chromosome — roughly 100 genes upstream (gene order < fusion position) and ~100 genes downstream (gene order > fusion position). The two halves are colour-tagged (red / blue) in the `lens` / `ancestor.txt` files so the fusion point sits at the boundary.

The `gff` follows the same convention as the karyotype gff files: Mark, local gene ID, source start, source end, strand, local gene order, source gene ID.

## Files

- **fusions_db.\***: the consolidated database (gff, ancestor.txt, lens, pep.fa) covering all 49 currently available Marks. 

Note: most Marks contain ~200 genes (≈100 either side of the fusion point), but Q1, Q2, R1, R2, R3 contain only ~100 genes (≈50 either side); P1 contains 186 genes due to chromosome end truncation.

All Marks in the master table have corresponding gene sets in the database.
