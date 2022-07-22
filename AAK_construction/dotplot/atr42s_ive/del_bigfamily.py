from os import sep
import re
import sys
import numpy as np
import wgdi.base as base

gff1 = base.newgff(sys.argv[1])
gff2 = base.newgff(sys.argv[2])
blast = base.newblast(sys.argv[3], 100, 1e-5, gff1, gff2, 'FALSE')
id = []
for name, group in blast.groupby([1]):
    if len(group)>20:
        id+=group.index.tolist()
blast.drop(index=id,inplace=True)

blast.to_csv(sys.argv[4],sep="\t",header=False,index=False)