###### all.species.csv 

Extracting collinear genes of all angiosperm species, *Am. trichopoda* was used as the reference. 

| Species                    | columns   |
| -------------------------- | --------- |
| Amborella trichopoda       | 1         |
| Nymphaea colorata          | 2-3       |
| Illicium verum             | 52-53     |
| Vitis vinifera             | 49-51     |
| Aquilegia coerulea         | ac472s    |
| Ceratophyllum demersum     | 41-48     |
| Chloranthus sessilifolius  | 32-33     |
| Cinnamomum kanehirae       | 37-40     |
| Liriodendron chinense      | 35-36     |
| Aristolochia fimbriata     | 34        |
| Acorus gramineus           | 4-5       |
| Elaeis guineensis          | 22-25     |
| Asparagus setaceus         | 18-21     |
| Acanthochlamys bracteata   | 10-13     |
| Dioscorea alata            | 14-17     |
| Ananas comosus             | 26-31     |
| Spirodela polyrhiza        | 6-9       |
| Ginkgo biloba              | 54        |
| Sequoiadendron giganteum   | 55        |
| Azolla filiculoides        | 56        |
| Selaginella moellendorffii | 57        |
| Physcomitrium patens       | 58        |

###### alignment_filter.csv 

Only genes that had a collinear relationship in all three ANA species and at least one eudicot, one monocot, one magnoliid ortholog, and a best hit in at least one outgroup species were retained.

###### total.conf

We used WGDI with the parameter '-at' and ASTRAL to constructed phylogenetic tree. this file is the parameter of '-at'.

all.pep all.cds ： These two files are files that merge the corresponding sequences of the species involved through the 'cat' command.



add_Aquilegia coerulea_Euryale ferox.csv

The order of species has changed.

