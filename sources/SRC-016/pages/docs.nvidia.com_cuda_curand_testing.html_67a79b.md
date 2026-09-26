source: https://docs.nvidia.com/cuda/curand/testing.html

# Testing[](https://docs.nvidia.com#testing)

The XORWOW generator was proposed by
Marsaglia [[5]](https://docs.nvidia.com/bibliography.html#bibliography__xorwow) and has been
tested using the TestU01 “Crush” framework of
tests [[6]](https://docs.nvidia.com/bibliography.html#bibliography__testu01). The full suite
of NIST pseudorandomness
tests [[7]](https://docs.nvidia.com/bibliography.html#bibliography__nist) has also been run,
though the focus has been on TestU01. The most rigorous the the TestU01
batteries is “BigCrush”, which executes 106 statistical tests over the
course of approximately 5 hours on a high-end CPU/GPU. The XORWOW
generator passes all of the tests on most runs, but does produce
occasional suspect statistics. Below is an example of the summary output
from a run that did not pass all tests, with the detail of the specific
failure.

```
========= Summary results of BigCrush =========
Version: TestU01 1.2.3
Generator: curandXORWOW
Number of statistics: 160
Total CPU time: 05:17:59.63
The following tests gave p-values outside [0.001, 0.9990]:
(eps means a value < 1.0e-300):
(eps1 means a value < 1.0e-15):
Test p-value
----------------------------------------------
81 LinearComp, r = 29 1 - 7.1e-11
----------------------------------------------
All other tests were passed
Detail from test 81:
scomp_LinearComp test:
-----------------------------------------------
N = 1, n = 400020, r = 29, s = 1
-----------------------------------------------
Number of degrees of freedom : 12
Chi2 statistic for size of jumps : 7.11
p-value of test : 0.85
-----------------------------------------------
Normal statistic for number of jumps : -6.41
p-value of test : 1 - 7.1e-11 *****
```

To put this into perspective, there is a table
in [[6]](https://docs.nvidia.com/bibliography.html#bibliography__testu01) that gives the
results of running various levels of the “Crush” tests on a broad
selection of generators. Only a small number of generators pass all of
the BigCrush tests. For example the widely-respected Mersenne
twister [[8]](https://docs.nvidia.com/bibliography.html#bibliography__matsumoto) consistently
fails two of the linear complexity tests.

The MRG32k3a generator was proposed
in [[9]](https://docs.nvidia.com/bibliography.html#bibliography__lecuyer), with a specific
implementation suggested
in [[10]](https://docs.nvidia.com/bibliography.html#bibliography__lecuyer-simard). This
generator passes all “BigCrush” tests frequently, with occasional
marginal results similar to those shown below.

```
========= Summary results of BigCrush =========
Version: TestU01 1.2.3
Generator: curandMRG32k3a
Number of statistics: 160
Total CPU time: 07:14:55.41
The following tests gave p-values outside [0.001, 0.9990]:
(eps means a value < 1.0e-300):
(eps1 means a value < 1.0e-15):
Test p-value
----------------------------------------------
59 WeightDistrib, r = 0 5.2e-4
----------------------------------------------
All other tests were passed
Detail from test 59:
svaria_WeightDistrib test:
-----------------------------------------------
N = 1, n = 20000000, r = 0, k = 256, Alpha = 0, Beta = 0.25
-----------------------------------------------
Number of degrees of freedom : 67
Chi-square statistic : 111.55
p-value of test : 5.2e-4 *****
-----------------------------------------------
CPU time used : 00:02:56.25
```

The MTGP32 generator is an adaptation of the work outlined
in [[1]](https://docs.nvidia.com/bibliography.html#bibliography__saito). The MTGP32 generator
exhibits some marginal results on “BigCrush”. Below is an example.

```
========= Summary results of BigCrush =========
Version: TestU01 1.2.3
Generator: curandMtgp32Int
Number of statistics: 160
Total CPU time: 05:45:29.49
The following tests gave p-values outside [0.001, 0.9990]:
(eps means a value < 1.0e-300):
(eps1 means a value < 1.0e-15):
Test p-value
----------------------------------------------
12 CollisionOver, t = 21 0.9993
----------------------------------------------
All other tests were passed
Detail from test 12:
smultin_MultinomialOver test:
-----------------------------------------------
N = 30, n = 20000000, r = 28, d = 4, t = 21,
Sparse = TRUE
GenerCell = smultin_GenerCellSerial
Number of cells = d^t = 4398046511104
Expected number per cell = 1 / 219902.33
EColl = n^2 / (2k) = 45.47473509
Hashing = TRUE
Collision test
CollisionOver: density = n / k = 1 / 219902.33
Expected number of collisions = Mu = 45.47
-----------------------------------------------
Results of CollisionOver test:
POISSON approximation :
Expected number of collisions = N*Mu : 1364.24
Observed number of collisions : 1248
p-value of test : 0.9993 *****
-----------------------------
Total number of cells containing j balls
j = 0 : 131940795334368
j = 1 : 599997504
j = 2 : 1248
j = 3 : 0
j = 4 : 0
j = 5 : 0
-----------------------------------------------
CPU time used : 00:04:32.52
```

The MT19937 generator is, by far, the most widely used PRNG

```
========= Summary results of BigCrush =========
Version: TestU01 1.2.3
Generator: curandMT19937Int
Number of statistics: 160
Total CPU time: 03:12:59.34
All tests were passed
```

The Philox4_32_10 generator is one of the counter-based RNGs described
in [[17]](https://docs.nvidia.com/bibliography.html#bibliography__shaw).

```
========= Summary results of BigCrush =========
Version: TestU01 1.2.3
Generator: curandPHILOXInt
Number of statistics: 160
Total CPU time: 03:18:50.30
All tests were passed
```

Sobol’ sequences are generated using the direction vectors recommended
by Joe and Kuo [[2]](https://docs.nvidia.com/bibliography.html#bibliography__joekuo). The
scrambled Sobol’ method is described
in [[3]](https://docs.nvidia.com/bibliography.html#bibliography__matousek)
and [[4]](https://docs.nvidia.com/bibliography.html#bibliography__owen).

Testing of the normal distribution, with the each of the generators, has
been done using the Pearson chi-squared
test [[11]](https://docs.nvidia.com/bibliography.html#bibliography__pearson), [[12]](https://docs.nvidia.com/bibliography.html#bibliography__placket),
the Jarque-Bera
test [[13]](https://docs.nvidia.com/bibliography.html#bibliography__jarquebera), the
Kolmogorov-Smirnov
test [[14]](https://docs.nvidia.com/bibliography.html#bibliography__kolmogorov), [[15]](https://docs.nvidia.com/bibliography.html#bibliography__massey),
and the Anderson-Darling
test [[16]](https://docs.nvidia.com/bibliography.html#bibliography__anderson).

Tests are run over the range +/- 6 standard deviations. Three Pearson tests are run, with cell counts 1000, 100, and 25. The test output has columns labeled PK for Pearson with 1000 cells, PC for Pearson with 100 cells, P25 for Pearson with 25 cells, JB for Jarque-Bera, KS for Kolmogorov-Smirnov, and AD for Anderson-Darling. The rejection criterion for each test is printed below the label.

The following tables are representative of the test output for statistical testing of the normal distribution for XORWOW, MRG32k3a, MTGP32, MT19937, Philox, Sobol’ 32-bit, and scrambled Sobol’ 32-bit generators. The rows of each table represent the statistical results computed over successive sequences of 10000 samples.

XORWOW Generator:

```
PK PC P25 JB KS AD
<1058 <118 <33 <4.6 <0.0122 <.632
----------------------------------------------------------------------------
684.48120 58.97784 20.44693 2.84152 0.00540 0.32829
686.37925 54.84938 7.79583 0.55109 0.00900 0.25832
673.21437 69.15825 15.46540 0.30335 0.00872 0.26772
568.26999 49.99519 8.85046 0.66624 0.00870 0.22939
639.10690 84.23040 10.19753 0.19844 0.00542 0.27939
```

MRg32k3a Generator:

```
PK PC P25 JB KS AD
<1058 <118 <33 <4.6 <0.0122 <.632
----------------------------------------------------------------------------
764.38500 74.48157 19.32716 1.50118 0.01103 0.60351
795.31006 74.15086 11.78414 1.15159 0.00821 0.35343
741.85426 91.88692 20.67103 2.34232 0.00900 0.61787
644.62093 70.68369 17.18277 0.32870 0.01243* 0.34630
806.02693 93.50691 23.10548 2.67340 0.00978 0.51466
```

MTGP32 Generator:

```
PK PC P25 JB KS AD
<1058 <118 <33 <4.6 <0.0122 <.632
----------------------------------------------------------------------------
924.62604 110.19868 23.45811 0.86919 0.00519 0.33411
708.76047 79.42919 20.67913 1.13427 0.01142 0.54632
674.17713 65.80415 13.09834 1.07799 0.01040 0.23860
733.35915 57.13829 17.66337 3.17017 0.01188 0.30864
620.17297 50.39043 14.75682 0.57970 0.00845 0.28916
```

MT19937 Generator:

```
PK PC P25 JB KS AD
<1058 <118 <33 <4.6 <0.0077 <.632
----------------------------------------------------------------------------
663.51515 67.53027 9.70908 0.70428 0.00482 0.22643
758.11526 65.27417 10.81213 0.16740 0.00541 0.24615
678.79743 60.92754 27.50102 1.33330 0.00546 0.42693
741.21087 82.42319 24.10450 1.84422 0.00570 0.41724
644.92464 71.74918 18.32281 1.01582 0.00546 0.30622
```

Philox_4x32_10 Generator:

```
PK PC P25 JB KS AD
<1058 <118 <33 <4.6 <0.0122 <.632
----------------------------------------------------------------------------
688.73231 78.60241 18.28300 0.23786 0.00520 0.24052
600.66650 59.78966 21.59090 4.24401 0.00464 0.49806
916.60146 78.16294 10.01345 1.53526 0.00660 0.25025
713.67544 61.20329 15.82239 0.79568 0.00614 0.26091
699.84498 80.73224 16.07304 1.37786 0.00464 0.29227
```

Sobol’ 32-bit generator:

```
PK PC P25 JB KS AD
<1058 <118 <33 <4.6 <0.0122 <.632
----------------------------------------------------------------------------
157.04578 6.47398 1.45802 0.19007 0.00024 0.00188
243.82767 11.98164 1.34982 0.00668 0.00030 0.00086
229.87234 10.40206 2.73912 0.04165 0.00036 0.00137
290.29451 17.09013 3.25717 0.02583 0.00042 0.00172
327.32072 19.22832 5.09510 0.00335 0.00036 0.00127
```

Scrambled Sobol’ 32-bit generator:

```
PK PC P25 JB KS AD
<1058 <118 <33 <4.6 <0.0122 <.632
----------------------------------------------------------------------------
255.80606 10.93180 1.33766 0.01226 0.00036 0.00112
258.84244 8.45589 1.56766 0.04164 0.00036 0.00170
585.34346 49.33610 5.32037 0.04069 0.00043 0.00208
337.50312 27.64720 3.38925 0.01953 0.00041 0.00211
729.56687 56.89682 32.89772 0.00911 0.00040 0.00204
```

Even though the log-normal distribution is closely derived from the normal distribution, it has also been tested using the Pearson chi-squared test and the Kolmogorov-Smirnov test.

The following tables are representative of the test output for statistical testing of the log normal distribution for XORWOW, MRG32k3a, MTGP32, MT19937, Philox, Sobol’ 32-bit, and scrambled Sobol’ 32-bit generators.

XORWOW generator:

```
PK PC P25 KS
<1058 <118 <33 <0.0122
----------------------------------------------------
1019.57936 105.63667 13.15820 0.00540
991.93663 91.95369 20.46549 0.00900
983.09678 115.34978 20.50434 0.00872
966.45604 113.30013 24.54060 0.00870
996.35262 111.50026 21.01332 0.00542
```

MRG32k3a generator:

```
PK PC P25 KS
<1058 <118 <33 <0.0122
----------------------------------------------------
1000.00359 90.12428 22.82709 0.00826
942.17843 81.16259 16.13670 0.00739
1005.62148 102.29924 23.62705 0.00697
1053.68391 98.75565 28.65422 0.01107
998.38936 103.43649 19.26568 0.00803
```

MTGP32 generator:

```
PK PC P25 KS
<1058 <118 <33 <0.0122
----------------------------------------------------
1010.18903 94.51850 17.98126 0.00771
993.78319 76.86543 12.48859 0.00831
1010.22068 63.76027 11.65743 0.00677
963.33103 89.44369 17.96636 0.01200
927.15616 75.85515 13.64221 0.00566
```

MT19937 generator:

```
PK PC P25 KS
<1058 <118 <33 <0.0122
----------------------------------------------------
929.15309 83.63208 16.91037 0.00482
1058.79511 114.19971 27.28300 0.00541
963.35338 103.52657 26.68634 0.00546
1009.21512 114.36706 38.44470 0.00570
976.91303 84.83272 14.78584 0.00546
```

Philox_4x32_10 generator:

```
PK PC P25 KS
<1058 <118 <33 <0.0122
----------------------------------------------------
992.19843 100.39826 14.91235 0.00357
962.03714 115.40663 18.03086 0.00595
1006.41781 92.84903 27.33686 0.00385
1009.75491 96.93654 11.99484 0.00520
1003.85449 89.00801 15.64060 0.00464
```

Sobol’ 32-bit generator:

```
PK PC P25 KS
<1058 <118 <33 <0.0122
----------------------------------------------------
289.42589 5.03327 0.48858 0.00024
386.79860 6.57783 0.76902 0.00030
355.04631 8.54472 1.12228 0.00036
434.19211 9.54021 2.07006 0.00042
343.57507 10.71571 0.42503 0.00036
```

Scrambled Sobol- 32-bit generator:

```
PK PC P25 KS
<1058 <118 <33 <0.0122
----------------------------------------------------
354.55037 8.20727 0.24592 0.00036
506.45280 12.93848 0.73323 0.00036
451.96949 18.18903 0.69465 0.00043
593.25666 16.55782 0.54769 0.00041
423.05263 12.06600 0.53472 0.00040
```

Testing of the Poisson-distribution, with the each of the generators,
has been done using the Pearson chi-squared
test [[11]](https://docs.nvidia.com/bibliography.html#bibliography__pearson).

Tests are run over a broad range of lambda values, and the statistics are compared to those for Poisson distribution results using MKL.