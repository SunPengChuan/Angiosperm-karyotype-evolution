# AMK-A (Ancestral Monocot Karyotype except Acoraceae)

The reconstructed Ancestral Monocot Karyotype (excluding Acoraceae) consists of 8 chromosomes, each derived from a continuous gene-order region of an extant species' chromosome.

## Chromosome Source

Positions are recorded as gene-order indices. For example, `spo4s17g00001` denotes the 1st gene on chromosome 17 of *Spirodela polyrhiza*.

| AMK-A Chr | Source Species         | Source Chr | Gene Range | # Genes |
|-----------|------------------------|------------|------------|---------|
| AMK-A1    | *Spirodela polyrhiza*  | 17         | 1–558      | 558     |
| AMK-A2    | *Spirodela polyrhiza*  | 18         | 1–564      | 564     |
| AMK-A3    | *Dioscorea alata*      | 17         | 1–1216     | 1216    |
| AMK-A4    | *Dioscorea alata*      | 10         | 1–959      | 959     |
| AMK-A5    | *Dioscorea alata*      | 11         | 1–1046     | 1046    |
| AMK-A6    | *Dioscorea alata*      | 12         | 1–962      | 962     |
| AMK-A7    | *Dioscorea alata*      | 3          | 1–1021     | 1021    |
| AMK-A8    | *Dioscorea alata*      | 13         | 1–947      | 947     |

Species abbreviations: `spo4s` = *Spirodela polyrhiza*, `da480s` = *Dioscorea alata*.

## Files

- **amka1s.gff**: gene annotations (AMK-A chr, AMK-A gene ID, source start, source end, strand, AMK-A gene order, source gene ID)
- **amka1s.ancestor.txt**: chromosome length and gene count
- **amka1s.lens**: chromosome display info for visualization
- **amka1s.pep.fa**: protein sequences for the annotated genes
