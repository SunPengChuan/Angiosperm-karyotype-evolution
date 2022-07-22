##  Construction of the ancestral angiosperm karyotype (AAK)

**Step1：**

```
cd ./dotplot/atr42s_ive
wgdi -d total.conf
```

<img src="D:\git\Angiosperm-karyotype-evolution\AAK_construction\dotplot\atr42s_ive\ive_atr42s.dotplot.order.png" style="zoom:20%;" />

```
# Record protochromosomes to atr42s.step1.txt according to atr42s.lens
# atr42s.step1.txt
1	1	2708	white	1
2	1	3074	white	1
3	1	3007	white	1
4	1	2732	#187C3A	1
5	1	1933	#72C8D5	1
6	1	2394	#AD1F25	1
7	1	1962	#7D7E2D	1
8	1	2183	#E7211A	1
9	1	2729	#EFEA3C	1
10	1	2163	#AB549C	1
11	1	2139	#F6BCC6	1
12	1	2123	white	1
13	1	2212	white	1

wgdi -d total1.conf
```

<img src="D:\git\Angiosperm-karyotype-evolution\AAK_construction\dotplot\atr42s_ive\ive_atr42s.dotplot.total1.png" style="zoom:20%;" />

**Step2：**

```
cd ./dotplot/lc2s_atr42s/
cp ../atr42s_ive/atr42s.step1.txt .
wgdi -d tota.conf
```

<img src="D:\git\Angiosperm-karyotype-evolution\AAK_construction\dotplot\lc2s_atr42s\lc2s_atr42s.dotplot.png" style="zoom:20%;" />

```
wgdi -icl total.conf
wgdi -bi total.conf
wgdi -c total.conf	
wgdi -km total.conf

# Add a new color to lc2s.step1.txt with Chr19 of Liriodendron chinense as protochromosome and delete its homologous chromosome chr1 and finally rename to lc2s.step2.txt
wgdi -km total1.conf
wgdi -d total1.conf
```

<img src="D:\git\Angiosperm-karyotype-evolution\AAK_construction\dotplot\lc2s_atr42s\lc2s_atr42s.dotplot.total1.png" style="zoom:20%;" />

**Step3：**

```
cd ./dotplot/atr42s_ive
cp ../lc2s_atr42s/atr42s.step2.txt .
wgdi -km total2.conf
```

<img src="D:\git\Angiosperm-karyotype-evolution\AAK_construction\dotplot\atr42s_ive\ive_atr42s.dotplot.total2.png" style="zoom:20%;" />

```
# Add new colors to ive.step1.txt with the blank region of Chr9 and chr14 of Illicium verum as protochromosomes, and delete its homologous region Chr10 and Chr2, and finally rename to ive.step2.txt

wgdi -km total3.conf
wgdi -d total3.conf
```

<img src="D:\git\Angiosperm-karyotype-evolution\AAK_construction\dotplot\atr42s_ive\ive_atr42s.dotplot.total3.png" style="zoom:20%;" />

```
# Add new colors to atr42s.step3.txt with blank region of Chr1 and Chr2 of Amborella trichopoda as protochromosomes and rename to atr42s.step4.txt

wgdi -km total4.conf
wgdi -d total4.conf
```

<img src="D:\git\Angiosperm-karyotype-evolution\AAK_construction\dotplot\atr42s_ive\ive_atr42s.dotplot.total4.png" style="zoom:20%;" />

**Step4：**

```
cd ./dotplot/atr42s_agr8s/
cp ../atr42s_ive/atr42s.step4.txt .

wgdi -km total.conf
wgdi -d total.conf
```

<img src="D:\git\Angiosperm-karyotype-evolution\AAK_construction\dotplot\atr42s_agr8s\atr42s_agr8s.dotplot.total.png" style="zoom:20%;" />

```
# Adjust the boundaries of the ancestor file (atr42s.step4.txt) based on collinearity and rename it to atr42s.step5.txt

wgdi -km total1.conf
wgdi -d total1.conf
```

<img src="D:\git\Angiosperm-karyotype-evolution\AAK_construction\dotplot\atr42s_agr8s\atr42s_agr8s.dotplot.total1.png" style="zoom:20%;" />

```
cd ./dotplot/agr8s_ive/
cp ../atr42s_ive/ive.step3.txt .
cp ../atr42s_agr8s/agr8s.step2.txt .

wgdi -d total.conf
```

<img src="D:\git\Angiosperm-karyotype-evolution\AAK_construction\dotplot\agr8s_ive\ive_agr8s.dotplot.order.png" style="zoom:20%;" />

```
cd ./dotplot/atr42s_agr8s/
cp ../atr42s_agr8s/atr42s.step6.txt .

wgdi -km tota.conf
wgdi -d total.conf
```

<img src="D:\git\Angiosperm-karyotype-evolution\AAK_construction\dotplot\atr42s_agr8s\atr42s_agr8s.dotplot.total2.png" style="zoom:20%;" />

**Step5：**

```
cd ./dotplot/nc476s_atr42s/

wgdi -km total.conf
wgdi -d total.conf
```

<img src="D:\git\Angiosperm-karyotype-evolution\AAK_construction\dotplot\nc476s_atr42s\nc476s_atr42s.dotplot.png" style="zoom:20%;" />

```
# Add a new color to atr42s.step6.txt with blank region of Chrs 3,12,13 of Amborella trichopoda as a protochromosome and rename to atr42s.step7.txt

wgdi -km total1.conf
wgdi -d total1.conf
```

<img src="D:\git\Angiosperm-karyotype-evolution\AAK_construction\dotplot\nc476s_atr42s\nc476s_atr42s.dotplot.total1.png" style="zoom:20%;" />