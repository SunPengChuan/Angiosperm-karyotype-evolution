# AEK (Ancestral Eudicot Karyotype)

The Ancestral Eudicot Karyotype consists of 7 chromosomes. Internal AEK gene IDs use the `eud` prefix (`eud1`–`eud7`); collinearity anchors supplemented from *Vitis vinifera* keep their original `vvi161s` IDs.

*Buxus sinica* (`bsi11s`, common boxwood) is included here as a reference. Boxwood has experienced only a single whole-genome duplication and no inter-chromosomal rearrangements since the eudicot ancestor, so its 14 chromosomes (7 paired blocks) share the same collinearity as AEK. It is not the structural backbone of AEK, only a reference whose collinearity is consistent with AEK.

## Files

- **AEK.\***: the 7-chromosome ancestral eudicot karyotype (gff, ancestor.txt, lens, pep.fa)
- **bsi11s.\***: the *Buxus sinica* karyotype, included as a collinearity reference (14 chromosomes plus unanchored contigs)

## Notes

- Because *Buxus* has not undergone inter-chromosomal rearrangements since the eudicot ancestor, fusion points identified on AEK can be cross-checked directly against *Buxus* chromosomes.
- The AEK gene set is not a final catalogue. Genes within collinear blocks can be expanded or substituted as needed to improve mapping to a given modern eudicot genome; the validating criterion remains the chromosomal location of fusion points in extant genomes.
