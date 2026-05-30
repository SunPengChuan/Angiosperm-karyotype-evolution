# AMAK (Ancestral Mesangiospermae Karyotype)

The reconstructed Ancestral Mesangiospermae Karyotype consists of 13 chromosomes, each derived from a continuous gene-order region of an extant species' chromosome.

## Chromosome Source

Positions are recorded as gene-order indices. For example, `agr8s7g01159` denotes the 1159th gene on chromosome 7 of *Acorus gramineus*.

| AMAK Chr | Source Species          | Source Chr | Gene Range | # Genes |
|----------|-------------------------|------------|------------|---------|
| AMAK1    | *Acorus gramineus*      | 7          | 1159–1868  | 710     |
| AMAK2    | *Ananas comosus*        | 17         | 1–329      | 329     |
| AMAK3    | *Liriodendron chinense* | 19         | 1–1161     | 1161    |
| AMAK4    | *Acorus americanus*     | 11         | 750–1317   | 568     |
| AMAK5    | *Acorus gramineus*      | 11         | 337–1025   | 689     |
| AMAK6    | *Ananas comosus*        | 17         | 330–760    | 431     |
| AMAK7    | *Acorus gramineus*      | 2          | 1540–2174  | 635     |
| AMAK8    | *Liriodendron chinense* | 18         | 1–1260     | 1260    |
| AMAK9    | *Acorus gramineus*      | 5          | 1–1880     | 1878    |
| AMAK10   | *Spirodela polyrhiza*   | 18         | 1–564      | 564     |
| AMAK11   | *Chloranthus sessilifolius* | 13     | 1–1537     | 1537    |
| AMAK12   | *Dioscorea alata*       | 7          | 1–949      | 949     |
| AMAK13   | *Acorus gramineus*      | 6          | 1–2346     | 995     |

Species abbreviations: `agr8s` = *Acorus gramineus*, `aam1s` = *Acorus americanus*, `aco40s` = *Ananas comosus*, `lc2s` = *Liriodendron chinense*, `spo4s` = *Spirodela polyrhiza*, `cs471s` = *Chloranthus sessilifolius*, `da480s` = *Dioscorea alata*.

## Files

- **amak1s.gff**: gene annotations (AMAK chr, AMAK gene ID, source start, source end, strand, AMAK gene order, source gene ID)
- **amak1s.ancestor.txt**: chromosome length and gene count
- **amak1s.lens**: chromosome display info for visualization
- **amak1s.pep.fa**: protein sequences for the annotated genes
