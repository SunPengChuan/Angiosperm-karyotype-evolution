### What is Karyotype Evolution?

Karyotype comprises both chromosome numbers and character of each chromosome for one species. Karyotype evolution represents chromosomal changes from the ancestral genome to the modern genome. This information is critical for reconstructing ancestral karyotypes and tracing how modern species evolved step by step. The evolution of ancestral karyotypes, especially involving changes in the number of chromosomes, usually results in speciation with rapid reproductive isolation. However, in the long evolutionary history of the karyotype of one current species, ancestral chromosomes fusion or fission gradually and randomly in the offspring lineages. This means that each intact ancestral chromosome (protochromosome) could be retained across the highly diverged lineages. In addition, the lineage closer to the common ancestor with fewer genome changes (for example, whole-genome duplication, WGD) may retain more protochromosomes than those distantly related ones with more WGD. If one protochromosome fused with another to produce one new chromosome or fissioned into two new chromosomes, the syntenic blocks could be identified as a basic rule. The other basic rule for such an ancestral karyotype should be that all protochromosomes or their syntenic blocks correspond completely to all chromosomes of each offspring species.

### The method to identify ancestral karyotypes

The previous approaches for karyotype reconstruction define contiguous ancestral regions (CARs) based on collinearity. However, due to chromosome structural abnormalities and short syntenic blocks, undefined regions become gap regions and the final result is highly dependent on the input files and parameters. In addition, a large number of gap regions in the results cannot continue to explore chromosomal changes. Different from these previous methods, we identify the protochromosomes by searching the shared intact chromosomes or chromosome-like syntenic blocks during chromosomal fusions across the highly diverged lineages. During chromosomal fusions, chromosome-like syntenic blocks are retained, in which chromosomes are protected by telomeres, and the fused chromosomes, therefore, have telomeres. However, it should be noted that our method did not exclude the chromosomal fissions, in which one protochromosome produced two chromosomes. Under this scenario, we can identify this protochromosome in other lineages, which may be intactly retained or fused with other protochromosomes. We summarize karyotypic changes during three basic chromosomal fusion types and also processes that we used to identify protochromosomes for ancestral angiosperm karyotype.

###### Karyotype evolution model and uniqueness of chromosomal fusions

Three basic chromosomal fusions comprise reciprocally translocated chromosome arms (RTA), end-end joining (EEJ) and nested chromosome fusion (NCF) (Fig.1). Chromosome translocations include reciprocal translocation and Robertsonian translocation, which correspond to RTA and EEJ, respectively. The NCF pattern is also widely recognized and used.

![Karyotype evolution model](figures/Karyotype%20evolution%20model.png)

Although chromosomal structural variations occur frequently in genomes, the probability seems to be very low that the positions of protochromosome fusion happen to overlap with the breakpoints of further structural variations at the later evolutionary stage. Therefore, such fusion positions could be accurate to infer whether two lineages share the same ancestor or not. Similarly, the inversion often occurs during chromosomal evolution, it is nearly impossible to disrupt the positions of protochromosome fusion. So, inversions have little effect on karyotype reconstruction.

Chromosomal fission usually refers to when one protochromosome breaks into two or more independent chromosomes. The RTA defined above comprises special chromosomal fission. Other chromosomal fission was not considered here because of two reasons. First, WGD is common in plants and chromosomal fusions occur more frequently after WGD. Second, if protochromosomal fission occurs in one lineage, for example, breaking into chromosomes, the identification of this protochromosome could be replaced by other lineages in which it may have remained intact or fused with other protochromosome with chromosome-like syntenic blocks. In addition, two fissioned chromosomes also correspond to syntenic blocks, which could be identified and deleted during the second cycle of the protochromosome identification.

###### Basic steps for construction of ancestral chromosome karyotype and karyotypic evolution

<div style="display:flex">
  <img src="figures/method1.png" style="width:50%">
  <img src="figures/method2.png" style="width:50%">
</div>

The spiral process consists of (i) identification of chromosome-like synteny blocks (CLSBs) by comparisons of all sampled genomes; (ii) extraction of the most intact CLSBs as protochromosomes, with automatic adding of telomeres at their ends; and (iii) removal of identified protochromosomes and connection of the flanking parts, followed by the next rounds of ‘protochromosome exploration’ until no genomic block is left in any of the sampled genomes. 

Karyotypes with the same chromosomal fusion positions are used to infer evolutionary relationships following five steps: Records of all CLSBs (1), fusion positions based on the number of homologs within the gap between two protochromosomes (2), the karyotypic composition of protochromosomes in each extant genome (3), the same fusion positions across species, (4) and karyotypic changes that parsimoniously lead from a common ancestor to its descendants (5). All of these processes can be performed automatically using the WGDI toolkit.


### Karyotype reconstruction demonstration

The detailed process is at https://github.com/SunPengChuan/wgdi-example/.

### What can Karyotype Evolution be used for?

(1) Paleogenomics and exploring the evolutionary trajectories of species.

(2) Phylogenetic and Species Taxonomy.

(3) Helps in verifying genome assembly.

(4) Detection of autopolyploidy or allopolyploidy.

