# AAK (Ancestral Angiosperm Karyotype)

The reconstructed Ancestral Angiosperm Karyotype consists of 16 chromosomes, each derived from a continuous gene-order region of an extant species' chromosome.

## Chromosome Source

Positions are recorded as gene-order indices. For example, `ive12g01424` denotes the 1424th gene on chromosome 12 of *Illicium verum*.

| AAK Chr | Source Species         | Source Chr | Gene Range  | # Genes |
|---------|------------------------|------------|-------------|---------|
| AAK1    | *Illicium verum*       | 12         | 1424–2235   | 812     |
| AAK2    | *Illicium verum*       | 9          | 1291–2037   | 747     |
| AAK3    | *Amborella trichopoda* | 10         | 1–2163      | 2163    |
| AAK4    | *Amborella trichopoda* | 11         | 1–2139      | 2139    |
| AAK5    | *Brasenia schreberi*   | 32         | 647–1122    | 476     |
| AAK6    | *Brasenia schreberi*   | 4          | 1–701       | 701     |
| AAK7    | *Illicium verum*       | 8          | 1–655       | 655     |
| AAK8    | *Liriodendron chinense*| 19         | 1–1161      | 1161    |
| AAK9    | *Amborella trichopoda* | 2          | 2098–3074   | 977     |
| AAK10   | *Illicium verum*       | 14         | 812–1743    | 932     |
| AAK11   | *Amborella trichopoda* | 4          | 1–2732      | 2732    |
| AAK12   | *Amborella trichopoda* | 5          | 1–1933      | 1933    |
| AAK13   | *Amborella trichopoda* | 6          | 1–2394      | 2394    |
| AAK14   | *Amborella trichopoda* | 7          | 1–1962      | 1962    |
| AAK15   | *Amborella trichopoda* | 8          | 1–2183      | 2183    |
| AAK16   | *Amborella trichopoda* | 9          | 1–2729      | 2729    |

Species abbreviations: `ive` = *Illicium verum*, `atr42s` = *Amborella trichopoda*, `bsc1s` = *Brasenia schreberi*, `lc2s` = *Liriodendron chinense*.

## Files

- **aak1s.gff**: gene annotations (AAK chr, AAK gene ID, source start, source end, strand, AAK gene order, source gene ID)
- **aak1s.ancestor.txt**: chromosome length and gene count
- **aak1s.lens**: chromosome display info for visualization
