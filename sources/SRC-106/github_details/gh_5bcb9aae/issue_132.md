# [Issue #132] [Issue]: amd-smi's python parser doesn't allow to set compute partitions

source: https://github.com/ROCm/amdsmi/issues/132
state: closed | updated: 2025-11-16T12:09:31Z
labels: status: triage

## 正文

### Problem Description

Hi folks!

I am running ROCm 6.4.3 on a server with multiple MI300X, and I am not able to set any compute partition:

```
$ sudo /opt/rocm/bin/amd-smi set -C DPX
usage: amd-smi set [-h] [-g GPU [GPU ...]] [-f % | -l LEVEL | -P SETPROFILE | -d SCLKMAX |
                   -C <ACCELERATOR_TYPE> or <PROFILE_INDEX> | -M PARTITION | -o WATTS |
                   -p POLICY_ID | -x POLICY_ID | -c CLK_TYPE [FREQ_LEVELS ...] |
                   -L CLK_TYPE LIM_TYPE VALUE | -R STATUS] [--json | --csv] [--file FILE]
                   [--loglevel LEVEL]
amd-smi set: error: argument -C/--compute-partition: invalid choice: 'DPX' (choose from S, P, X, ,,  , D, P, X, ,,  , Q, P, X, ,,  , C, P, X, ,,  , 0, ,,  , 1, ,,  , 2, ,,  , 3)
```

I checked the code and it seems that the python parser uses a data structure for choices that comes from https://github.com/ROCm/amdsmi/blob/release/rocm-rel-6.4/amdsmi_cli/amdsmi_parser.py#L1127, where the code returns a string like the following:

```
'SPX, DPX, QPX, CPX, 0, 1, 2, 3'
```

The fix should be easy, something like:

```
 set_value_exclusive_group.add_argument('-C', '--compute-partition', action='store', choices=[a.strip() for a in accelerator_set_choices.split(",")], type=lambda value: self._is_command_supported(value, accelerator_set_choices, '--compute-partition'), required=False, help=set_compute_partition_help, metavar='<ACCELERATOR_TYPE> or <PROFILE_INDEX>')
```

Or a more profound one if you want `accelerator_set_choices` to return a list instead of a string (but it seems used elsewhere so not sure what you prefer).

### Operating System

Debian Trixie

### CPU

AMD EPYC 9654 96-Core Processor

### GPU

AMD Instinct MI300X

### ROCm Version

ROCm 6.4.3

### ROCm Component

amdsmi

### Steps to Reproduce

See above in the description :)

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (14)

### darren-amd · 2025-10-17

Hi @elukey,

Thanks for reporting the issue. I gave this a try in a 6.4.3 container with an MI300X and was unable to reproduce the issue. Could you please provide me the output of `sudo amd-smi partition --accelerator`, `rocminfo`, and `sudo amd-smi set --help`? Thanks!

### elukey · 2025-10-17

Hi @darren-amd!

```

ACCELERATOR_PARTITION_PROFILES:
GPU_ID  PROFILE_INDEX  MEMORY_PARTITION_CAPS  ACCELERATOR_TYPE  PARTITION_ID     NUM_PARTITIONS  NUM_RESOURCES  RESOURCE_INDEX  RESOURCE_TYPE  RESOURCE_INSTANCES  RESOURCES_SHARED  
0       0              NPS1                   SPX               N/A              1               4              0               XCC            8                   1
                                                                                                                1               DECODER        4                   1
                                                                                                                2               DMA            16                  1
                                                                                                                3               JPEG           32                  1
        1              NPS1                   DPX*              0                2               4              4               XCC            4                   1
                                                                                                                5               DECODER        2                   1
                                                                                                                6               DMA            8                   1
                                                                                                                7               JPEG           16                  1
        2              NPS1,NPS4              QPX               N/A              4               4              8               XCC            2                   1
                                                                                                                9               DECODER        1                   1
                                                                                                                10              DMA            4                   1
                                                                                                                11              JPEG           8                   1
        3              NPS1,NPS4              CPX               N/A              0               4              12              XCC            1                   1
                                                                                                                13              DECODER        1                   2
                                                                                                                14              DMA            2                   1
                                                                                                                15              JPEG           8                   2
1       0              NPS1                   SPX               N/A              1               4              0               XCC            8                   1
                                                                                                                1               DECODER        4                   1
                                                                                                                2               DMA            16                  1
                                                                                                                3               JPEG           32                  1
        1              NPS1                   DPX*              1                2               4              4               XCC            4                   1
                                                                                                                5               DECODER        2                   1
                                                                                                                6               DMA            8                   1
                                                                                                                7               JPEG           16                  1
        2              NPS1,NPS4              QPX               N/A              4               4              8               XCC            2                   1
                                                                                                                9               DECODER        1                   1
                                                                                                                10              DMA            4                   1
                                                                                                                11              JPEG           8                   1
        3              NPS1,NPS4              CPX               N/A              0               4              12              XCC            1                   1
                                                                                                                13              DECODER        1                   2
                                                                                                                14              DMA            2                   1
                                                                                                                15              JPEG           8                   2
2       0              NPS1                   SPX               N/A              1               4              0               XCC            8                   1
                                                                                                                1               DECODER        4                   1
                                                                                                                2               DMA            16                  1
                                                                                                                3               JPEG           32                  1
        1              NPS1                   DPX*              0                2               4              4               XCC            4                   1
                                                                                                                5               DECODER        2                   1
                                                                                                                6               DMA            8                   1
                                                                                                                7               JPEG           16                  1
        2              NPS1,NPS4              QPX               N/A              4               4              8               XCC            2                   1
                                                                                                                9               DECODER        1                   1
                                                                                                                10              DMA            4                   1
                                                                                                                11              JPEG           8                   1
        3              NPS1,NPS4              CPX               N/A              0               4              12              XCC            1                   1
                                                                                                                13              DECODER        1                   2
                                                                                                                14              DMA            2                   1
                                                                                                                15              JPEG           8                   2
3       0              NPS1                   SPX               N/A              1               4              0               XCC            8                   1
                                                                                                                1               DECODER        4                   1
                                                                                                                2               DMA            16                  1
                                                                                                                3               JPEG           32                  1
        1              NPS1                   DPX*              1                2               4              4               XCC            4                   1
                                                                                                                5               DECODER        2                   1
                                                                                                                6               DMA            8                   1
                                                                                                                7               JPEG           16                  1
        2              NPS1,NPS4              QPX               N/A              4               4              8               XCC            2                   1
                                                                                                                9               DECODER        1                   1
                                                                                                                10              DMA            4                   1
                                                                                                                11              JPEG           8                   1
        3              NPS1,NPS4              CPX               N/A              0               4              12              XCC            1                   1
                                                                                                                13              DECODER        1                   2
                                                                                                                14              DMA            2                   1
                                                                                                                15              JPEG           8                   2
4       0              NPS1                   SPX               N/A              1               4              0               XCC            8                   1
                                                                                                                1               DECODER        4                   1
                                                                                                                2               DMA            16                  1
                                                                                                                3               JPEG           32                  1
        1              NPS1                   DPX*              0                2               4              4               XCC            4                   1
                                                                                                                5               DECODER        2                   1
                                                                                                                6               DMA            8                   1
                                                                                                                7               JPEG           16                  1
        2              NPS1,NPS4              QPX               N/A              4               4              8               XCC            2                   1
                                                                                                                9               DECODER        1                   1
                                                                                                                10              DMA            4                   1
                                                                                                                11              JPEG           8                   1
        3              NPS1,NPS4              CPX               N/A              0               4              12              XCC            1                   1
                                                                                                                13              DECODER        1                   2
                                                                                                                14              DMA            2                   1
                                                                                                                15              JPEG           8                   2
5       0              NPS1                   SPX               N/A              1               4              0               XCC            8                   1
                                                                                                                1               DECODER        4                   1
                                                                                                                2               DMA            16                  1
                                                                                                                3               JPEG           32                  1
        1              NPS1                   DPX*              1                2               4              4               XCC            4                   1
                                                                                                                5               DECODER        2                   1
                                                                                                                6               DMA            8                   1
                                                                                                                7               JPEG           16                  1
        2              NPS1,NPS4              QPX               N/A              4               4              8               XCC            2                   1
                                                                                                                9               DECODER        1                   1
                                                                                                                10              DMA            4                   1
                                                                                                                11              JPEG           8                   1
        3              NPS1,NPS4              CPX               N/A              0               4              12              XCC            1                   1
                                                                                                                13              DECODER        1                   2
                                                                                                                14              DMA            2                   1
                                                                                                                15              JPEG           8                   2
6       0              NPS1                   SPX               N/A              1               4              0               XCC            8                   1
                                                                                                                1               DECODER        4                   1
                                                                                                                2               DMA            16                  1
                                                                                                                3               JPEG           32                  1
        1              NPS1                   DPX*              0                2               4              4               XCC            4                   1
                                                                                                                5               DECODER        2                   1
                                                                                                                6               DMA            8                   1
                                                                                                                7               JPEG           16                  1
        2              NPS1,NPS4              QPX               N/A              4               4              8               XCC            2                   1
                                                                                                                9               DECODER        1                   1
                                                                                                                10              DMA            4                   1
                                                                                                                11              JPEG           8                   1
        3              NPS1,NPS4              CPX               N/A              0               4              12              XCC            1                   1
                                                                                                                13              DECODER        1                   2
                                                                                                                14              DMA            2                   1
                                                                                                                15              JPEG           8                   2
7       0              NPS1                   SPX               N/A              1               4              0               XCC            8                   1
                                                                                                                1               DECODER        4                   1
                                                                                                                2               DMA            16                  1
                                                                                                                3               JPEG           32                  1
        1              NPS1                   DPX*              1                2               4              4               XCC            4                   1
                                                                                                                5               DECODER        2                   1
                                                                                                                6               DMA            8                   1
                                                                                                                7               JPEG           16                  1
        2              NPS1,NPS4              QPX               N/A              4               4              8               XCC            2                   1
                                                                                                                9               DECODER        1                   1
                                                                                                                10              DMA            4                   1
                                                                                                                11              JPEG           8                   1
        3              NPS1,NPS4              CPX               N/A              0               4              12              XCC            1                   1
                                                                                                                13              DECODER        1                   2
                                                                                                                14              DMA            2                   1
                                                                                                                15              JPEG           8                   2
8       0              NPS1                   SPX               N/A              1               4              0               XCC            8                   1
                                                                                                                1               DECODER        4                   1
                                                                                                                2               DMA            16                  1
                                                                                                                3               JPEG           32                  1
        1              NPS1                   DPX*              0                2               4              4               XCC            4                   1
                                                                                                                5               DECODER        2                   1
                                                                                                                6               DMA            8                   1
                                                                                                                7               JPEG           16                  1
        2              NPS1,NPS4              QPX               N/A              4               4              8               XCC            2                   1
                                                                                                                9               DECODER        1                   1
                                                                                                                10              DMA            4                   1
                                                                                                                11              JPEG           8                   1
        3              NPS1,NPS4              CPX               N/A              0               4              12              XCC            1                   1
                                                                                                                13              DECODER        1                   2
                                                                                                                14              DMA            2                   1
                                                                                                                15              JPEG           8                   2
9       0              NPS1                   SPX               N/A              1               4              0               XCC            8                   1
                                                                                                                1               DECODER        4                   1
                                                                                                                2               DMA            16                  1
                                                                                                                3               JPEG           32                  1
        1              NPS1                   DPX*              1                2               4              4               XCC            4                   1
                                                                                                                5               DECODER        2                   1
                                                                                                                6               DMA            8                   1
                                                                                                                7               JPEG           16                  1
        2              NPS1,NPS4              QPX               N/A              4               4              8               XCC            2                   1
                                                                                                                9               DECODER        1                   1
                                                                                                                10              DMA            4                   1
                                                                                                                11              JPEG           8                   1
        3              NPS1,NPS4              CPX               N/A              0               4              12              XCC            1                   1
                                                                                                                13              DECODER        1                   2
                                                                                                                14              DMA            2                   1
                                                                                                                15              JPEG           8                   2
10      0              NPS1                   SPX               N/A              1               4              0               XCC            8                   1
                                                                                                                1               DECODER        4                   1
                                                                                                                2               DMA            16                  1
                                                                                                                3               JPEG           32                  1
        1              NPS1                   DPX*              0                2               4              4               XCC            4                   1
                                                                                                                5               DECODER        2                   1
                                                                                                                6               DMA            8                   1
                                                                                                                7               JPEG           16                  1
        2              NPS1,NPS4              QPX               N/A              4               4              8               XCC            2                   1
                                                                                                                9               DECODER        1                   1
                                                                                                                10              DMA            4                   1
                                                                                                                11              JPEG           8                   1
        3              NPS1,NPS4              CPX               N/A              0               4              12              XCC            1                   1
                                                                                                                13              DECODER        1                   2
                                                                                                                14              DMA            2                   1
                                                                                                                15              JPEG           8                   2
11      0              NPS1                   SPX               N/A              1               4              0               XCC            8                   1
                                                                                                                1               DECODER        4                   1
                                                                                                                2               DMA            16                  1
                                                                                                                3               JPEG           32                  1
        1              NPS1                   DPX*              1                2               4              4               XCC            4                   1
                                                                                                                5               DECODER        2                   1
                                                                                                                6               DMA            8                   1
                                                                                                                7               JPEG           16                  1
        2              NPS1,NPS4              QPX               N/A              4               4              8               XCC            2                   1
                                                                                                                9               DECODER        1                   1
                                                                                                                10              DMA            4                   1
                                                                                                                11              JPEG           8                   1
        3              NPS1,NPS4              CPX               N/A              0               4              12              XCC            1                   1
                                                                                                                13              DECODER        1                   2
                                                                                                                14              DMA            2                   1
                                                                                                                15              JPEG           8                   2
12      0              NPS1                   SPX               N/A              1               4              0               XCC            8                   1
                                                                                                                1               DECODER        4                   1
                                                                                                                2               DMA            16                  1
                                                                                                                3               JPEG           32                  1
        1              NPS1                   DPX*              0                2               4              4               XCC            4                   1
                                                                                                                5               DECODER        2                   1
                                                                                                                6               DMA            8                   1
                                                                                                                7               JPEG           16                  1
        2              NPS1,NPS4              QPX               N/A              4               4              8               XCC            2                   1
                                                                                                                9               DECODER        1                   1
                                                                                                                10              DMA            4                   1
                                                                                                                11              JPEG           8                   1
        3              NPS1,NPS4              CPX               N/A              0               4              12              XCC            1                   1
                                                                                                                13              DECODER        1                   2
                                                                                                                14              DMA            2                   1
                                                                                                                15              JPEG           8                   2
13      0              NPS1                   SPX               N/A              1               4              0               XCC            8                   1
                                                                                                                1               DECODER        4                   1
                                                                                                                2               DMA            16                  1
                                                                                                                3               JPEG           32                  1
        1              NPS1                   DPX*              1                2               4              4               XCC            4                   1
                                                                                                                5               DECODER        2                   1
                                                                                                                6               DMA            8                   1
                                                                                                                7               JPEG           16                  1
        2              NPS1,NPS4              QPX               N/A              4               4              8               XCC            2                   1
                                                                                                                9               DECODER        1                   1
                                                                                                                10              DMA            4                   1
                                                                                                                11              JPEG           8                   1
        3              NPS1,NPS4              CPX               N/A              0               4              12              XCC            1                   1
                                                                                                                13              DECODER        1                   2
                                                                                                                14              DMA            2                   1
                                                                                                                15              JPEG           8                   2
14      0              NPS1                   SPX               N/A              1               4              0               XCC            8                   1
                                                                                                                1               DECODER        4                   1
                                                                                                                2               DMA            16                  1
                                                                                                                3               JPEG           32                  1
        1              NPS1                   DPX*              0                2               4              4               XCC            4                   1
                                                                                                                5               DECODER        2                   1
                                                                                                                6               DMA            8                   1
                                                                                                                7               JPEG           16                  1
        2              NPS1,NPS4              QPX               N/A              4               4              8               XCC            2                   1
                                                                                                                9               DECODER        1                   1
                                                                                                                10              DMA            4                   1
                                                                                                                11              JPEG           8                   1
        3              NPS1,NPS4              CPX               N/A              0               4              12              XCC            1                   1
                                                                                                                13              DECODER        1                   2
                                                                                                                14              DMA            2                   1
                                                                                                                15              JPEG           8                   2
15      0              NPS1                   SPX               N/A              1               4              0               XCC            8                   1
                                                                                                                1               DECODER        4                   1
                                                                                                                2               DMA            16                  1
                                                                                                                3               JPEG           32                  1
        1              NPS1                   DPX*              1                2               4              4               XCC            4                   1
                                                                                                                5               DECODER        2                   1
                                                                                                                6               DMA            8                   1
                                                                                                                7               JPEG           16                  1
        2              NPS1,NPS4              QPX               N/A              4               4              8               XCC            2                   1
                                                                                                                9               DECODER        1                   1
                                                                                                                10              DMA            4                   1
                                                                                                                11              JPEG           8                   1
        3              NPS1,NPS4              CPX               N/A              0               4              12              XCC            1                   1
                                                                                                                13              DECODER        1                   2
                                                                                                                14              DMA            2                   1
                                                                                                                15              JPEG           8                   2

ACCELERATOR_PARTITION_RESOURCES:
RESOURCE_INDEX  RESOURCE_TYPE  RESOURCE_INSTANCES  RESOURCES_SHARED  
0               XCC            8                   1
1               DECODER        4                   1
2               DMA            16                  1
3               JPEG           32                  1
4               XCC            4                   1
5               DECODER        2                   1
6               DMA            8                   1
7               JPEG           16                  1
8               XCC            2                   1
9               DECODER        1                   1
10              DMA            4                   1
11              JPEG           8                   1
12              XCC            1                   1
13              DECODER        1                   2
14              DMA            2                   1
15              JPEG           8                   2
0               XCC            8                   1
1               DECODER        4                   1
2               DMA            16                  1
3               JPEG           32                  1
4               XCC            4                   1
5               DECODER        2                   1
6               DMA            8                   1
7               JPEG           16                  1
8               XCC            2                   1
9               DECODER        1                   1
10              DMA            4                   1
11              JPEG           8                   1
12              XCC            1                   1
13              DECODER        1                   2
14              DMA            2                   1
15              JPEG           8                   2
0               XCC            8                   1
1               DECODER        4                   1
2               DMA            16                  1
3               JPEG           32                  1
4               XCC            4                   1
5               DECODER        2                   1
6               DMA            8                   1
7               JPEG           16                  1
8               XCC            2                   1
9               DECODER        1                   1
10              DMA            4                   1
11              JPEG           8                   1
12              XCC            1                   1
13              DECODER        1                   2
14              DMA            2                   1
15              JPEG           8                   2
0               XCC            8                   1
1               DECODER        4                   1
2               DMA            16                  1
3               JPEG           32                  1
4               XCC            4                   1
5               DECODER        2                   1
6               DMA            8                   1
7               JPEG           16                  1
8               XCC            2                   1
9               DECODER        1                   1
10              DMA            4                   1
11              JPEG           8                   1
12              XCC            1                   1
13              DECODER        1                   2
14              DMA            2                   1
15              JPEG           8                   2
0               XCC            8                   1
1               DECODER        4                   1
2               DMA            16                  1
3               JPEG           32                  1
4               XCC            4                   1
5               DECODER        2                   1
6               DMA            8                   1
7               JPEG           16                  1
8               XCC            2                   1
9               DECODER        1                   1
10              DMA            4                   1
11              JPEG           8                   1
12              XCC            1                   1
13              DECODER        1                   2
14              DMA            2                   1
15              JPEG           8                   2
0               XCC            8                   1
1               DECODER        4                   1
2               DMA            16                  1
3               JPEG           32                  1
4               XCC            4                   1
5               DECODER        2                   1
6               DMA            8                   1
7               JPEG           16                  1
8               XCC            2                   1
9               DECODER        1                   1
10              DMA            4                   1
11              JPEG           8                   1
12              XCC            1                   1
13              DECODER        1                   2
14              DMA            2                   1
15              JPEG           8                   2
0               XCC            8                   1
1               DECODER        4                   1
2               DMA            16                  1
3               JPEG           32                  1
4               XCC            4                   1
5               DECODER        2                   1
6               DMA            8                   1
7               JPEG           16                  1
8               XCC            2                   1
9               DECODER        1                   1
10              DMA            4                   1
11              JPEG           8                   1
12              XCC            1                   1
13              DECODER        1                   2
14              DMA            2                   1
15              JPEG           8                   2
0               XCC            8                   1
1               DECODER        4                   1
2               DMA            16                  1
3               JPEG           32                  1
4               XCC            4                   1
5               DECODER        2                   1
6               DMA            8                   1
7               JPEG           16                  1
8               XCC            2                   1
9               DECODER        1                   1
10              DMA            4                   1
11              JPEG           8                   1
12              XCC            1                   1
13              DECODER        1                   2
14              DMA            2                   1
15              JPEG           8                   2
0               XCC            8                   1
1               DECODER        4                   1
2               DMA            16                  1
3               JPEG           32                  1
4               XCC            4                   1
5               DECODER        2                   1
6               DMA            8                   1
7               JPEG           16                  1
8               XCC            2                   1
9               DECODER        1                   1
10              DMA            4                   1
11              JPEG           8                   1
12              XCC            1                   1
13              DECODER        1                   2
14              DMA            2                   1
15              JPEG           8                   2
0               XCC            8                   1
1               DECODER        4                   1
2               DMA            16                  1
3               JPEG           32                  1
4               XCC            4                   1
5               DECODER        2                   1
6               DMA            8                   1
7               JPEG           16                  1
8               XCC            2                   1
9               DECODER        1                   1
10              DMA            4                   1
11              JPEG           8                   1
12              XCC            1                   1
13              DECODER        1                   2
14              DMA            2                   1
15              JPEG           8                   2
0               XCC            8                   1
1               DECODER        4                   1
2               DMA            16                  1
3               JPEG           32                  1
4               XCC            4                   1
5               DECODER        2                   1
6               DMA            8                   1
7               JPEG           16                  1
8               XCC            2                   1
9               DECODER        1                   1
10              DMA            4                   1
11              JPEG           8                   1
12              XCC            1                   1
13              DECODER        1                   2
14              DMA            2                   1
15              JPEG           8                   2
0               XCC            8                   1
1               DECODER        4                   1
2               DMA            16                  1
3               JPEG           32                  1
4               XCC            4                   1
5               DECODER        2                   1
6               DMA            8                   1
7               JPEG           16                  1
8               XCC            2                   1
9               DECODER        1                   1
10              DMA            4                   1
11              JPEG           8                   1
12              XCC            1                   1
13              DECODER        1                   2
14              DMA            2                   1
15              JPEG           8                   2
0               XCC            8                   1
1               DECODER        4                   1
2               DMA            16                  1
3               JPEG           32                  1
4               XCC            4                   1
5               DECODER        2                   1
6               DMA            8                   1
7               JPEG           16                  1
8               XCC            2                   1
9               DECODER        1                   1
10              DMA            4                   1
11              JPEG           8                   1
12              XCC            1                   1
13              DECODER        1                   2
14              DMA            2                   1
15              JPEG           8                   2
0               XCC            8                   1
1               DECODER        4                   1
2               DMA            16                  1
3               JPEG           32                  1
4               XCC            4                   1
5               DECODER        2                   1
6               DMA            8                   1
7               JPEG           16                  1
8               XCC            2                   1
9               DECODER        1                   1
10              DMA            4                   1
11              JPEG           8                   1
12              XCC            1                   1
13              DECODER        1                   2
14              DMA            2                   1
15              JPEG           8                   2
0               XCC            8                   1
1               DECODER        4                   1
2               DMA            16                  1
3               JPEG           32                  1
4               XCC            4                   1
5               DECODER        2                   1
6               DMA            8                   1
7               JPEG           16                  1
8               XCC            2                   1
9               DECODER        1                   1
10              DMA            4                   1
11              JPEG           8                   1
12              XCC            1                   1
13              DECODER        1                   2
14              DMA            2                   1
15              JPEG           8                   2
0               XCC            8                   1
1               DECODER        4                   1
2               DMA            16                  1
3               JPEG           32                  1
4               XCC            4                   1
5               DECODER        2                   1
6               DMA            8                   1
7               JPEG           16                  1
8               XCC            2                   1
9               DECODER        1                   1
10              DMA            4                   1
11              JPEG           8                   1
12              XCC            1                   1
13              DECODER        1                   2
14              DMA            2                   1
15              JPEG           8                   2


Legend:
  * = Current mode
```

```
usage: amd-smi set [-h] [-g GPU [GPU ...]] [-f % | -l LEVEL | -P SETPROFILE | -d SCLKMAX |
                   -C <ACCELERATOR_TYPE> or <PROFILE_INDEX> | -M PARTITION | -o WATTS |
                   -p POLICY_ID | -x POLICY_ID | -c CLK_TYPE [FREQ_LEVELS ...] |
                   -L CLK_TYPE LIM_TYPE VALUE | -R STATUS] [--json | --csv] [--file FILE]
                   [--loglevel LEVEL]

If no GPU is specified, will select all GPUs on the system.                                    
A set argument must be provided; Multiple set arguments are accepted

Set Arguments:
  -h, --help                                                     show this help message and exit
  -g, --gpu GPU [GPU ...]                                        Select a GPU ID, BDF, or UUID from the possible choices:
                                                                 ID: 0  | BDF: 0000:05:00.0 | UUID: abff74a1-0000-1000-80d1-3c23a9580558
                                                                 ID: 1  | BDF: 0000:05:00.1 | UUID: abff74a1-0000-1000-80d1-3c23a9580558
                                                                 ID: 2  | BDF: 0000:26:00.0 | UUID: 77ff74a1-0000-1000-8009-1c467da33120
                                                                 ID: 3  | BDF: 0000:26:00.1 | UUID: 77ff74a1-0000-1000-8009-1c467da33120
                                                                 ID: 4  | BDF: 0000:46:00.0 | UUID: 44ff74a1-0000-1000-800d-0d8545b906a9
                                                                 ID: 5  | BDF: 0000:46:00.1 | UUID: 44ff74a1-0000-1000-800d-0d8545b906a9
                                                                 ID: 6  | BDF: 0000:65:00.0 | UUID: 6eff74a1-0000-1000-80d9-3b857254b09c
                                                                 ID: 7  | BDF: 0000:65:00.1 | UUID: 6eff74a1-0000-1000-80d9-3b857254b09c
                                                                 ID: 8  | BDF: 0000:85:00.0 | UUID: 1fff74a1-0000-1000-803d-9f30292ace59
                                                                 ID: 9  | BDF: 0000:85:00.1 | UUID: 1fff74a1-0000-1000-803d-9f30292ace59
                                                                 ID: 10 | BDF: 0000:a6:00.0 | UUID: 0aff74a1-0000-1000-8085-dd841fd2b28c
                                                                 ID: 11 | BDF: 0000:a6:00.1 | UUID: 0aff74a1-0000-1000-8085-dd841fd2b28c
                                                                 ID: 12 | BDF: 0000:c6:00.0 | UUID: c1ff74a1-0000-1000-809a-ded85f80b4bf
                                                                 ID: 13 | BDF: 0000:c6:00.1 | UUID: c1ff74a1-0000-1000-809a-ded85f80b4bf
                                                                 ID: 14 | BDF: 0000:e5:00.0 | UUID: 87ff74a1-0000-1000-8000-232c018c9f54
                                                                 ID: 15 | BDF: 0000:e5:00.1 | UUID: 87ff74a1-0000-1000-8000-232c018c9f54
                                                                   all  | Selects all devices
  -f, --fan %                                                    Set GPU fan speed (0-255 or 0-100%)
  -l, --perf-level LEVEL                                         Set one of the following performance levels:
                                                                 	AUTO, LOW, HIGH, MANUAL, STABLE_STD, STABLE_PEAK, STABLE_MIN_MCLK, STABLE_MIN_SCLK, DETERMINISM
  -P, --profile SETPROFILE                                       Set power profile level (#) or choose one of available profiles:
                                                                 	CUSTOM_MASK, VIDEO_MASK, POWER_SAVING_MASK, COMPUTE_MASK, VR_MASK, THREE_D_FULL_SCR_MASK, BOOTUP_DEFAULT
  -d, --perf-determinism SCLKMAX                                 Set performance determinism and select one of the corresponding performance levels:
                                                                 	AUTO, LOW, HIGH, MANUAL, STABLE_STD, STABLE_PEAK, STABLE_MIN_MCLK, STABLE_MIN_SCLK, DETERMINISM
  -C, --compute-partition <ACCELERATOR_TYPE> or <PROFILE_INDEX>  Set one of the following the accelerator type or profile index:
                                                                 	SPX, DPX, QPX, CPX, 0, 1, 2, 3.
                                                                 	Use `sudo amd-smi partition --accelerator` to find acceptable values.
  -M, --memory-partition PARTITION                               Set one of the following the memory partition modes:
                                                                 	NPS1, NPS2, NPS4, NPS8
  -o, --power-cap WATTS                                          Set power capacity limit:
                                                                 	min cap: 0 W, max cap: 750 W
  -p, --soc-pstate POLICY_ID                                     Set the GPU soc pstate policy using policy id, an integer. Valid id's include:
                                                                 	0: soc_pstate_default, 1: soc_pstate_0, 2: soc_pstate_1, 3: soc_pstate_2
  -x, --xgmi-plpd POLICY_ID                                      Set the GPU XGMI per-link power down policy using policy id, an integer. Valid id's include:
                                                                 	0: plpd_disallow, 1: plpd_default, 2: plpd_optimized
  -c, --clk-level CLK_TYPE [FREQ_LEVELS ...]                     Set one or more sclk (aka gfxclk), mclk, fclk, pcie, or socclk frequency levels.
                                                                 	Use `amd-smi static --clock` to find acceptable levels.
  -L, --clk-limit CLK_TYPE LIM_TYPE VALUE                        Sets the sclk (aka gfxclk) or mclk minimum and maximum frequencies. 
                                                                 	ex: amd-smi set -L (sclk | mclk) (min | max) value
  -R, --process-isolation STATUS                                 Enable or disable the GPU process isolation on a per partition basis: 0 for disable and 1 for enable.

Command Modifiers:
  --json                                                         Displays output in JSON format (human readable by default).
  --csv                                                          Displays output in CSV format (human readable by default).
  --file FILE                                                    Saves output into a file on the provided path (stdout by default).
  --loglevel LEVEL                                               Set the logging level from the possible choices:
                                                                 	DEBUG, INFO, WARNING, ERROR, CRITICAL

```

This is a kubernetes node so we don't have rocminfo installed at the moment, we have only amd-smi. If the output is really needed I'll try to install it!

I installed packages from https://repo.radeon.com/rocm/apt/6.4/, more precisely:

```
elukey@ml-serve1012:~$ dpkg -l | grep amd-smi
ii  amd-smi-lib                          25.3.0.60400-47~24.04                amd64        AMD System Management libraries
elukey@ml-serve1012:~$ dpkg -l | grep rocm
ii  rocm-core                            6.4.0.60400-47~24.04                 amd64        ROCm Runtime software stack
```

I am wondering at this point if I selected the right package. The bug seems present when inspecting the code, maybe it was fixed in some commit that I am missing?


### elukey · 2025-10-17

Ok so I may have 6.4.0 now that I compare release dates:

https://github.com/ROCm/ROCm/releases/tag/rocm-6.4.3
vs
https://repo.radeon.com/rocm/apt/6.4/ (timestamps)

I noticed the version in the package name but there was also another big suffix and I kinda assumed the Debian repo had 6.4.3. Is there a way to get more up-to-date Debian packages to be published? I think at this point that something fixed it between 6.4.0 and 6.4.3 :)

### darren-amd · 2025-10-20

> Ok so I may have 6.4.0 now that I compare release dates:
> 
> https://github.com/ROCm/ROCm/releases/tag/rocm-6.4.3 vs https://repo.radeon.com/rocm/apt/6.4/ (timestamps)
> 
> I noticed the version in the package name but there was also another big suffix and I kinda assumed the Debian repo had 6.4.3. Is there a way to get more up-to-date Debian packages to be published? I think at this point that something fixed it between 6.4.0 and 6.4.3 :)

Hi @elukey,

We have instructions on installing the latest ROCm on Debian [here](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html#quick-start-installation-guide), which at this time is ROCm 7.0.2.

### elukey · 2025-10-22

@darren-amd Hi again!

I tried amd-smi from rocm 7.0.2 but I still get the same error. I checked the code:

1) [Here](https://github.com/ROCm/amdsmi/blob/rocm-7.0.2/amdsmi_cli/amdsmi_parser.py#L1266) should be where the parser gets the available values. The `choices` field should be a list, brought by `accelerator_set_choices`.
2) `accelerator_set_choices` is set [here](https://github.com/ROCm/amdsmi/blob/rocm-7.0.2/amdsmi_cli/amdsmi_parser.py#L1219), and it seems coming from the helpers.py module.
3) The function used in the helpers module is [this one](https://github.com/ROCm/amdsmi/blob/rocm-7.0.2/amdsmi_cli/amdsmi_helpers.py#L768), that returns a [string](https://github.com/ROCm/amdsmi/blob/rocm-7.0.2/amdsmi_cli/amdsmi_helpers.py#L779) for accellerator_choices.

So the wrong value is still provided to the argparse's choice field, that explains what I am seeing in my tests. How have you tested the 6.4.3 version? Am I missing something important?

### darren-amd · 2025-10-22

Hi @elukey,

Thanks for the extra information, I took another look at your output of `sudo amd-smi partition --accelerator` which seems to indicate that you are already in DPX mode, although setting to DPX again doesn't seem to reproduce your error message either. I've been running inside of a container which might be worth a try:
```
docker run -it \
  --privileged \
  --device=/dev/kfd \
  --device=/dev/dri \
  --network=host \
  --group-add sudo \
  --cap-add=SYS_MODULE \
  --cap-add=SYS_PTRACE \
  --shm-size="5gb" \
  --ipc=host \
  --name "smi-test" \
  -v /lib/modules:/lib/modules \
  rocm/dev-ubuntu-22.04:7.0.2-complete \
  /bin/bash
```
Could you also provide the output of `sudo amd-smi partition --accelerator`, `amd-smi`, and `sudo amd-smi set --help` from inside the container if it doesn't work? Also the amdgpu version if you haven't upgraded. Thanks!

### elukey · 2025-10-23

I was able to set DPX modifying the python script as I described above :)

```
$ sudo /opt/rocm/bin/amd-smi partition --accelerator

ACCELERATOR_PARTITION_PROFILES:
GPU_ID  PROFILE_INDEX  MEMORY_PARTITION_CAPS  ACCELERATOR_TYPE  PARTITION_ID     NUM_PARTITIONS  NUM_RESOURCES  RESOURCE_INDEX  RESOURCE_TYPE  RESOURCE_INSTANCES  RESOURCES_SHARED  
0       0              NPS1                   SPX               N/A              1               4              0               XCC            8                   1
                                                                                                                1               DECODER        4                   1
                                                                                                                2               DMA            16                  1
                                                                                                                3               JPEG           32                  1
        1              NPS1                   DPX*              0                2               4              4               XCC            4                   1
                                                                                                                5               DECODER        2                   1
                                                                                                                6               DMA            8                   1
                                                                                                                7               JPEG           16                  1
        2              NPS1,NPS4              QPX               N/A              4               4              8               XCC            2                   1
                                                                                                                9               DECODER        1                   1
                                                                                                                10              DMA            4                   1
                                                                                                                11              JPEG           8                   1
        3              NPS1,NPS4              CPX               N/A              8               4              12              XCC            1                   1
                                                                                                                13              DECODER        1                   2
                                                                                                                14              DMA            2                   1
                                                                                                                15              JPEG           8                   2
1       N/A            N/A                    N/A               1                N/A             N/A            N/A             N/A            N/A                 N/A
2       0              NPS1                   SPX               N/A              1               4              0               XCC            8                   1
                                                                                                                1               DECODER        4                   1
                                                                                                                2               DMA            16                  1
                                                                                                                3               JPEG           32                  1
        1              NPS1                   DPX*              0                2               4              4               XCC            4                   1
                                                                                                                5               DECODER        2                   1
                                                                                                                6               DMA            8                   1
                                                                                                                7               JPEG           16                  1
        2              NPS1,NPS4              QPX               N/A              4               4              8               XCC            2                   1
                                                                                                                9               DECODER        1                   1
                                                                                                                10              DMA            4                   1
                                                                                                                11              JPEG           8                   1
        3              NPS1,NPS4              CPX               N/A              8               4              12              XCC            1                   1
                                                                                                                13              DECODER        1                   2
                                                                                                                14              DMA            2                   1
                                                                                                                15              JPEG           8                   2
3       N/A            N/A                    N/A               1                N/A             N/A            N/A             N/A            N/A                 N/A
4       0              NPS1                   SPX               N/A              1               4              0               XCC            8                   1
                                                                                                                1               DECODER        4                   1
                                                                                                                2               DMA            16                  1
                                                                                                                3               JPEG           32                  1
        1              NPS1                   DPX*              0                2               4              4               XCC            4                   1
                                                                                                                5               DECODER        2                   1
                                                                                                                6               DMA            8                   1
                                                                                                                7               JPEG           16                  1
        2              NPS1,NPS4              QPX               N/A              4               4              8               XCC            2                   1
                                                                                                                9               DECODER        1                   1
                                                                                                                10              DMA            4                   1
                                                                                                                11              JPEG           8                   1
        3              NPS1,NPS4              CPX               N/A              8               4              12              XCC            1                   1
                                                                                                                13              DECODER        1                   2
                                                                                                                14              DMA            2                   1
                                                                                                                15              JPEG           8                   2
5       N/A            N/A                    N/A               1                N/A             N/A            N/A             N/A            N/A                 N/A
6       0              NPS1                   SPX               N/A              1               4              0               XCC            8                   1
                                                                                                                1               DECODER        4                   1
                                                                                                                2               DMA            16                  1
                                                                                                                3               JPEG           32                  1
        1              NPS1                   DPX*              0                2               4              4               XCC            4                   1
                                                                                                                5               DECODER        2                   1
                                                                                                                6               DMA            8                   1
                                                                                                                7               JPEG           16                  1
        2              NPS1,NPS4              QPX               N/A              4               4              8               XCC            2                   1
                                                                                                                9               DECODER        1                   1
                                                                                                                10              DMA            4                   1
                                                                                                                11              JPEG           8                   1
        3              NPS1,NPS4              CPX               N/A              8               4              12              XCC            1                   1
                                                                                                                13              DECODER        1                   2
                                                                                                                14              DMA            2                   1
                                                                                                                15              JPEG           8                   2
7       N/A            N/A                    N/A               1                N/A             N/A            N/A             N/A            N/A                 N/A
8       0              NPS1                   SPX               N/A              1               4              0               XCC            8                   1
                                                                                                                1               DECODER        4                   1
                                                                                                                2               DMA            16                  1
                                                                                                                3               JPEG           32                  1
        1              NPS1                   DPX*              0                2               4              4               XCC            4                   1
                                                                                                                5               DECODER        2                   1
                                                                                                                6               DMA            8                   1
                                                                                                                7               JPEG           16                  1
        2              NPS1,NPS4              QPX               N/A              4               4              8               XCC            2                   1
                                                                                                                9               DECODER        1                   1
                                                                                                                10              DMA            4                   1
                                                                                                                11              JPEG           8                   1
        3              NPS1,NPS4              CPX               N/A              8               4              12              XCC            1                   1
                                                                                                                13              DECODER        1                   2
                                                                                                                14              DMA            2                   1
                                                                                                                15              JPEG           8                   2
9       N/A            N/A                    N/A               1                N/A             N/A            N/A             N/A            N/A                 N/A
10      0              NPS1                   SPX               N/A              1               4              0               XCC            8                   1
                                                                                                                1               DECODER        4                   1
                                                                                                                2               DMA            16                  1
                                                                                                                3               JPEG           32                  1
        1              NPS1                   DPX*              0                2               4              4               XCC            4                   1
                                                                                                                5               DECODER        2                   1
                                                                                                                6               DMA            8                   1
                                                                                                                7               JPEG           16                  1
        2              NPS1,NPS4              QPX               N/A              4               4              8               XCC            2                   1
                                                                                                                9               DECODER        1                   1
                                                                                                                10              DMA            4                   1
                                                                                                                11              JPEG           8                   1
        3              NPS1,NPS4              CPX               N/A              8               4              12              XCC            1                   1
                                                                                                                13              DECODER        1                   2
                                                                                                                14              DMA            2                   1
                                                                                                                15              JPEG           8                   2
11      N/A            N/A                    N/A               1                N/A             N/A            N/A             N/A            N/A                 N/A
12      0              NPS1                   SPX               N/A              1               4              0               XCC            8                   1
                                                                                                                1               DECODER        4                   1
                                                                                                                2               DMA            16                  1
                                                                                                                3               JPEG           32                  1
        1              NPS1                   DPX*              0                2               4              4               XCC            4                   1
                                                                                                                5               DECODER        2                   1
                                                                                                                6               DMA            8                   1
                                                                                                                7               JPEG           16                  1
        2              NPS1,NPS4              QPX               N/A              4               4              8               XCC            2                   1
                                                                                                                9               DECODER        1                   1
                                                                                                                10              DMA            4                   1
                                                                                                                11              JPEG           8                   1
        3              NPS1,NPS4              CPX               N/A              8               4              12              XCC            1                   1
                                                                                                                13              DECODER        1                   2
                                                                                                                14              DMA            2                   1
                                                                                                                15              JPEG           8                   2
13      N/A            N/A                    N/A               1                N/A             N/A            N/A             N/A            N/A                 N/A
14      0              NPS1                   SPX               N/A              1               4              0               XCC            8                   1
                                                                                                                1               DECODER        4                   1
                                                                                                                2               DMA            16                  1
                                                                                                                3               JPEG           32                  1
        1              NPS1                   DPX*              0                2               4              4               XCC            4                   1
                                                                                                                5               DECODER        2                   1
                                                                                                                6               DMA            8                   1
                                                                                                                7               JPEG           16                  1
        2              NPS1,NPS4              QPX               N/A              4               4              8               XCC            2                   1
                                                                                                                9               DECODER        1                   1
                                                                                                                10              DMA            4                   1
                                                                                                                11              JPEG           8                   1
        3              NPS1,NPS4              CPX               N/A              8               4              12              XCC            1                   1
                                                                                                                13              DECODER        1                   2
                                                                                                                14              DMA            2                   1
                                                                                                                15              JPEG           8                   2
15      N/A            N/A                    N/A               1                N/A             N/A            N/A             N/A            N/A                 N/A

ACCELERATOR_PARTITION_RESOURCES:
RESOURCE_INDEX  RESOURCE_TYPE  RESOURCE_INSTANCES  RESOURCES_SHARED  
0               XCC            8                   1
1               DECODER        4                   1
2               DMA            16                  1
3               JPEG           32                  1
4               XCC            4                   1
5               DECODER        2                   1
6               DMA            8                   1
7               JPEG           16                  1
8               XCC            2                   1
9               DECODER        1                   1
10              DMA            4                   1
11              JPEG           8                   1
12              XCC            1                   1
13              DECODER        1                   2
14              DMA            2                   1
15              JPEG           8                   2
N/A             N/A            N/A                 N/A
0               XCC            8                   1
1               DECODER        4                   1
2               DMA            16                  1
3               JPEG           32                  1
4               XCC            4                   1
5               DECODER        2                   1
6               DMA            8                   1
7               JPEG           16                  1
8               XCC            2                   1
9               DECODER        1                   1
10              DMA            4                   1
11              JPEG           8                   1
12              XCC            1                   1
13              DECODER        1                   2
14              DMA            2                   1
15              JPEG           8                   2
N/A             N/A            N/A                 N/A
0               XCC            8                   1
1               DECODER        4                   1
2               DMA            16                  1
3               JPEG           32                  1
4               XCC            4                   1
5               DECODER        2                   1
6               DMA            8                   1
7               JPEG           16                  1
8               XCC            2                   1
9               DECODER        1                   1
10              DMA            4                   1
11              JPEG           8                   1
12              XCC            1                   1
13              DECODER        1                   2
14              DMA            2                   1
15              JPEG           8                   2
N/A             N/A            N/A                 N/A
0               XCC            8                   1
1               DECODER        4                   1
2               DMA            16                  1
3               JPEG           32                  1
4               XCC            4                   1
5               DECODER        2                   1
6               DMA            8                   1
7               JPEG           16                  1
8               XCC            2                   1
9               DECODER        1                   1
10              DMA            4                   1
11              JPEG           8                   1
12              XCC            1                   1
13              DECODER        1                   2
14              DMA            2                   1
15              JPEG           8                   2
N/A             N/A            N/A                 N/A
0               XCC            8                   1
1               DECODER        4                   1
2               DMA            16                  1
3               JPEG           32                  1
4               XCC            4                   1
5               DECODER        2                   1
6               DMA            8                   1
7               JPEG           16                  1
8               XCC            2                   1
9               DECODER        1                   1
10              DMA            4                   1
11              JPEG           8                   1
12              XCC            1                   1
13              DECODER        1                   2
14              DMA            2                   1
15              JPEG           8                   2
N/A             N/A            N/A                 N/A
0               XCC            8                   1
1               DECODER        4                   1
2               DMA            16                  1
3               JPEG           32                  1
4               XCC            4                   1
5               DECODER        2                   1
6               DMA            8                   1
7               JPEG           16                  1
8               XCC            2                   1
9               DECODER        1                   1
10              DMA            4                   1
11              JPEG           8                   1
12              XCC            1                   1
13              DECODER        1                   2
14              DMA            2                   1
15              JPEG           8                   2
N/A             N/A            N/A                 N/A
0               XCC            8                   1
1               DECODER        4                   1
2               DMA            16                  1
3               JPEG           32                  1
4               XCC            4                   1
5               DECODER        2                   1
6               DMA            8                   1
7               JPEG           16                  1
8               XCC            2                   1
9               DECODER        1                   1
10              DMA            4                   1
11              JPEG           8                   1
12              XCC            1                   1
13              DECODER        1                   2
14              DMA            2                   1
15              JPEG           8                   2
N/A             N/A            N/A                 N/A
0               XCC            8                   1
1               DECODER        4                   1
2               DMA            16                  1
3               JPEG           32                  1
4               XCC            4                   1
5               DECODER        2                   1
6               DMA            8                   1
7               JPEG           16                  1
8               XCC            2                   1
9               DECODER        1                   1
10              DMA            4                   1
11              JPEG           8                   1
12              XCC            1                   1
13              DECODER        1                   2
14              DMA            2                   1
15              JPEG           8                   2
N/A             N/A            N/A                 N/A


Legend:
  * = Current mode
```

```
$ sudo /opt/rocm/bin/amd-smi
+------------------------------------------------------------------------------+
| AMD-SMI 26.0.2+39589fda      amdgpu version: Linuxver ROCm version: 7.0.2    |
| Platform: Linux Baremetal                                                    |
|-------------------------------------+----------------------------------------|
| BDF                        GPU-Name | Mem-Uti   Temp   UEC       Power-Usage |
| GPU  HIP-ID  OAM-ID  Partition-Mode | GFX-Uti    Fan               Mem-Usage |
|=====================================+========================================|
| 0000:05:00.0    AMD Instinct MI300X | 0 %      40 °C   0           142/750 W |
|   0       0       7        DPX/NPS1 | 0 %        N/A           283/196592 MB |
|-------------------------------------+----------------------------------------|
| 0000:05:00.1    AMD Instinct MI300X | N/A        N/A   0                 N/A |
|   1       1     N/A             N/A | N/A        N/A            492/98296 MB |
|-------------------------------------+----------------------------------------|
| 0000:26:00.0    AMD Instinct MI300X | 0 %      41 °C   0           141/750 W |
|   2       2       6        DPX/NPS1 | 0 %        N/A           283/196592 MB |
|-------------------------------------+----------------------------------------|
| 0000:26:00.1    AMD Instinct MI300X | N/A        N/A   0                 N/A |
|   3       3     N/A             N/A | N/A        N/A            492/98296 MB |
|-------------------------------------+----------------------------------------|
| 0000:46:00.0    AMD Instinct MI300X | 0 %      43 °C   0           142/750 W |
|   4       4       4        DPX/NPS1 | 0 %        N/A           283/196592 MB |
|-------------------------------------+----------------------------------------|
| 0000:46:00.1    AMD Instinct MI300X | N/A        N/A   0                 N/A |
|   5       5     N/A             N/A | N/A        N/A            492/98296 MB |
|-------------------------------------+----------------------------------------|
| 0000:65:00.0    AMD Instinct MI300X | 0 %      39 °C   0           140/750 W |
|   6       6       5        DPX/NPS1 | 0 %        N/A           283/196592 MB |
|-------------------------------------+----------------------------------------|
| 0000:65:00.1    AMD Instinct MI300X | N/A        N/A   0                 N/A |
|   7       7     N/A             N/A | N/A        N/A            492/98296 MB |
|-------------------------------------+----------------------------------------|
| 0000:85:00.0    AMD Instinct MI300X | 0 %      42 °C   0           146/750 W |
|   8       8       3        DPX/NPS1 | 0 %        N/A           283/196592 MB |
|-------------------------------------+----------------------------------------|
| 0000:85:00.1    AMD Instinct MI300X | N/A        N/A   0                 N/A |
|   9       9     N/A             N/A | N/A        N/A            492/98296 MB |
|-------------------------------------+----------------------------------------|
| 0000:a6:00.0    AMD Instinct MI300X | 0 %      39 °C   0           138/750 W |
|  10      10       2        DPX/NPS1 | 0 %        N/A           283/196592 MB |
|-------------------------------------+----------------------------------------|
| 0000:a6:00.1    AMD Instinct MI300X | N/A        N/A   0                 N/A |
|  11      11     N/A             N/A | N/A        N/A            492/98296 MB |
|-------------------------------------+----------------------------------------|
| 0000:c6:00.0    AMD Instinct MI300X | 0 %      41 °C   0           142/750 W |
|  12      12       0        DPX/NPS1 | 0 %        N/A           283/196592 MB |
|-------------------------------------+----------------------------------------|
| 0000:c6:00.1    AMD Instinct MI300X | N/A        N/A   0                 N/A |
|  13      13     N/A             N/A | N/A        N/A            492/98296 MB |
|-------------------------------------+----------------------------------------|
| 0000:e5:00.0    AMD Instinct MI300X | 0 %      39 °C   0           136/750 W |
|  14      14       1        DPX/NPS1 | 0 %        N/A           283/196592 MB |
|-------------------------------------+----------------------------------------|
| 0000:e5:00.1    AMD Instinct MI300X | N/A        N/A   0                 N/A |
|  15      15     N/A             N/A | N/A        N/A            492/98296 MB |
+-------------------------------------+----------------------------------------+
+------------------------------------------------------------------------------+
| Processes:                                                                   |
|  GPU        PID  Process Name          GTT_MEM  VRAM_MEM  MEM_USAGE     CU % |
|==============================================================================|
|  No running processes found                                                  |
+------------------------------------------------------------------------------+
```

```
$ sudo /opt/rocm/bin/amd-smi set --help
usage: amd-smi set [-h] [-f % | -l LEVEL | -P PROFILE_LEVEL | -d SCLKMAX | -C TYPE/INDEX |
                   -M PARTITION | -o WATTS | -p POLICY_ID | -x POLICY_ID |
                   -c CLK_TYPE [FREQ_LEVELS ...] | -L CLK_TYPE LIM_TYPE VALUE | -R STATUS]
                   [-g GPU [GPU ...]] [--json | --csv] [--file FILE] [--loglevel LEVEL]

If no GPU is specified, will select all GPUs on the system.                                    
A set argument must be provided; Multiple set arguments are accepted.                                    
Requires 'sudo' privileges.

Set Arguments:
  -h, --help                                  show this help message and exit
  -f, --fan %                                 Set GPU fan speed (0-255 or 0-100%)
  -l, --perf-level LEVEL                      Set one of the following performance levels:
                                              	AUTO, LOW, HIGH, MANUAL, STABLE_STD, STABLE_PEAK, STABLE_MIN_MCLK, STABLE_MIN_SCLK, DETERMINISM
  -P, --profile PROFILE_LEVEL                 Set power profile level (#) or choose one of available profiles:
                                              	CUSTOM_MASK, VIDEO_MASK, POWER_SAVING_MASK, COMPUTE_MASK, VR_MASK, THREE_D_FULL_SCR_MASK, BOOTUP_DEFAULT
  -d, --perf-determinism SCLKMAX              Set performance determinism and select one of the corresponding performance levels:
                                              	AUTO, LOW, HIGH, MANUAL, STABLE_STD, STABLE_PEAK, STABLE_MIN_MCLK, STABLE_MIN_SCLK, DETERMINISM
  -C, --compute-partition TYPE/INDEX          Set one of the following the accelerator TYPE or profile INDEX:
                                              	SPX, DPX, QPX, CPX, 0, 1, 2, 3.
                                              	Use `sudo amd-smi partition --accelerator` to find acceptable values.
  -M, --memory-partition PARTITION            Set one of the following the memory partition modes:
                                              	NPS1, NPS2, NPS4, NPS8
  -o, --power-cap WATTS                       Set power capacity limit:
                                              	min cap: 0 W, max cap: 750 W
  -p, --soc-pstate POLICY_ID                  Set the GPU soc pstate policy using policy id, an integer. Valid id's include:
                                              	0: soc_pstate_default, 0: 
  -x, --xgmi-plpd POLICY_ID                   Set the GPU XGMI per-link power down policy using policy id, an integer. Valid id's include:
                                              	0: plpd_disallow, 0: 
  -c, --clk-level CLK_TYPE [FREQ_LEVELS ...]  Set one or more sclk (aka gfxclk), mclk, fclk, pcie, or socclk frequency levels.
                                              	Use `amd-smi static --clock` to find acceptable levels.
  -L, --clk-limit CLK_TYPE LIM_TYPE VALUE     Sets the sclk (aka gfxclk) or mclk minimum and maximum frequencies. 
                                              	ex: amd-smi set -L (sclk | mclk) (min | max) value
  -R, --process-isolation STATUS              Enable or disable the GPU process isolation on a per partition basis: 0 for disable and 1 for enable.

Device Arguments:
  -g, --gpu GPU [GPU ...]                     Select a GPU ID, BDF, or UUID from the possible choices:
                                              ID: 0  | BDF: 0000:05:00.0 | UUID: abff74a1-0000-1000-80d1-3c23a9580558
                                              ID: 1  | BDF: 0000:05:00.1 | UUID: abff74a1-0000-1000-80d1-3c23a9580558
                                              ID: 2  | BDF: 0000:26:00.0 | UUID: 77ff74a1-0000-1000-8009-1c467da33120
                                              ID: 3  | BDF: 0000:26:00.1 | UUID: 77ff74a1-0000-1000-8009-1c467da33120
                                              ID: 4  | BDF: 0000:46:00.0 | UUID: 44ff74a1-0000-1000-800d-0d8545b906a9
                                              ID: 5  | BDF: 0000:46:00.1 | UUID: 44ff74a1-0000-1000-800d-0d8545b906a9
                                              ID: 6  | BDF: 0000:65:00.0 | UUID: 6eff74a1-0000-1000-80d9-3b857254b09c
                                              ID: 7  | BDF: 0000:65:00.1 | UUID: 6eff74a1-0000-1000-80d9-3b857254b09c
                                              ID: 8  | BDF: 0000:85:00.0 | UUID: 1fff74a1-0000-1000-803d-9f30292ace59
                                              ID: 9  | BDF: 0000:85:00.1 | UUID: 1fff74a1-0000-1000-803d-9f30292ace59
                                              ID: 10 | BDF: 0000:a6:00.0 | UUID: 0aff74a1-0000-1000-8085-dd841fd2b28c
                                              ID: 11 | BDF: 0000:a6:00.1 | UUID: 0aff74a1-0000-1000-8085-dd841fd2b28c
                                              ID: 12 | BDF: 0000:c6:00.0 | UUID: c1ff74a1-0000-1000-809a-ded85f80b4bf
                                              ID: 13 | BDF: 0000:c6:00.1 | UUID: c1ff74a1-0000-1000-809a-ded85f80b4bf
                                              ID: 14 | BDF: 0000:e5:00.0 | UUID: 87ff74a1-0000-1000-8000-232c018c9f54
                                              ID: 15 | BDF: 0000:e5:00.1 | UUID: 87ff74a1-0000-1000-8000-232c018c9f54
                                                all  | Selects all devices

Command Modifiers:
  --json                                      Displays output in JSON format
  --csv                                       Displays output in CSV format
  --file FILE                                 Saves output into a file on the provided path
  --loglevel LEVEL                            Set the logging level from the possible choices:
                                                  DEBUG, INFO, WARNING, ERROR, CRITICAL
```

```
$ dpkg -l | grep amd-smi
ii  amd-smi-lib                          26.0.2.70002-56~24.04                amd64        AMD System Management libraries
$ dpkg -l | grep rocm-
ii  rocm-core                            7.0.2.70002-56~24.04                 amd64        ROCm Runtime software stack
$ dpkg -l | grep amdgpu
ii  libdrm-amdgpu1:amd64                 2.4.124-2                            amd64        Userspace interface to amdgpu-specific kernel DRM services -- runtime

```

@darren-amd Hi! Here all the info. I am using the packages for noble, I noticed that you tested jammy, but not sure what changes. Could you please also tell me what package versions you use in your container? Just to compare them with mine. I checked the code on the host and it is the one that I indicated earlier on, not sure how it could work as-is since it uses a string where a list is needed.

### elukey · 2025-10-28

I ran `rocm/dev-ubuntu-22.04:7.0.2-complete` locally and I do see the same problem, namely choices in argparse being a string and not a list..

### elukey · 2025-11-08

@darren-amd Hi! I am wondering if we could try to find the diff between my testing environment and yours, because this bug is really blocking for me :(

### darren-amd · 2025-11-10

Hi @elukey,

Sorry for the delay, your output from `amd-smi` seems to suggest you are already in DPX mode:
```
|=====================================+========================================|
| 0000:05:00.0    AMD Instinct MI300X | 0 %      40 °C   0           142/750 W |
|   0       0       7        DPX/NPS1 | 0 %        N/A           283/196592 MB |
|-------------------------------------+----------------------------------------|
```
My package versions inside of the container match yours, the only difference I see is: `amdgpu version: Linuxver` in amd-smi. Could you try updating your amdgpu versions: [update driver](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html#amdgpu-driver-installation). I will also take a look at the linked PR, does that fix your issue? 


### elukey · 2025-11-12

Hi @darren-amd,

Yep as written before I was able to set DPX modifying directly the Python script on the host, in order to bypass the parsing issue. I use the Linux kernel drivers, so it may be difficult for me to test other things, but I am reasonably sure this is a python issue.

Could you please modify the following file in your testing container and report back what the print emits? It should output something when executing the amd-smi command:

```
diff --git a/amdsmi_cli/amdsmi_parser.py b/amdsmi_cli/amdsmi_parser.py
index 763b6661..8d86c0a4 100644
--- a/amdsmi_cli/amdsmi_parser.py
+++ b/amdsmi_cli/amdsmi_parser.py
@@ -1217,6 +1217,7 @@ class AMDSMIParser(argparse.ArgumentParser):
                 perf_det_choices_str = ", ".join(self.helpers.get_perf_det_levels())
                 set_perf_det_help = f"Set performance determinism and select one of the corresponding performance levels:\n\t{perf_det_choices_str}"
                 (accelerator_set_choices, _) = self.helpers.get_accelerator_choices_types_indices()
+                print(f"accelerator_set_choices: {accelerator_set_choices}, type: {type(accelerator_set_choices)}")
                 memory_partition_choices_str = ", ".join(self.helpers.get_memory_partition_types())
                 set_compute_partition_help = f"Set one of the following the accelerator TYPE or profile INDEX:\n\t{accelerator_set_choices}.\n\tUse `sudo amd-smi partition --accelerator` to find acceptable values."
                 set_memory_partition_help = f"Set one of the following the memory partition modes:\n\t{memory_partition_choices_str}"
```

In my case I get a string, that is not compatible down below with the `choices` argparse field of `--compute-partition`, because it would require a list. The pull request should fix the issue, but I am curious to know why you are not able to repro.

Thanks!





### darren-amd · 2025-11-12

Thanks @elukey,

It does look like the output for the choices is a string instead of a list, but I was not able to reproduce the issue. I mocked up a quick example and it seems that when you pass in a string as choices to argparse, passing a string with consecutive characters works. This may be related to python versioning? What version of python are you on? I'm on 3.12.

For example for:
```
import argparse

parser = argparse.ArgumentParser()
my_string_choices = "AB,C"
my_list_choices = ['AB', 'C']

parser.add_argument('-s', '--string-choices', choices=my_string_choices, help="String choices")
parser.add_argument('-l', '--list-choices', choices=my_list_choices, help="List choices")

args = parser.parse_args()
print(f"Parsed args: {args}")
```
Running `python3 test.py -s AB` is a valid argument. However, we should probably change this behavior so I will get the linked PR reviewed.

### elukey · 2025-11-13

@darren-amd interesting! I am running python 3.13.5 (Debian Trixie) and your script leads to:

```
usage: test.py [-h] [-s {A,B,,,C}] [-l {AB,C}]
test.py: error: argument -s/--string-choices: invalid choice: 'AB' (choose from A, B, ,, C)
```
I tried pyenv and installed 3.12:

```
python3.12 /tmp/test.py -s AB
Parsed args: Namespace(string_choices='AB', list_choices=None)
```

Very interesting :D



### darren-amd · 2025-11-13

@elukey Cool find! 

I got the PR merged internally and it should propagate to the external repo soon. I'll let you know once it's there, thanks for the report!
