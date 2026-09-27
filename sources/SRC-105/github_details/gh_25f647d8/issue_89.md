# [Issue #89] Bundled CUDA libraries

source: https://github.com/NVIDIA/DCGM/issues/89
state: closed | updated: 2025-04-14T18:24:46Z
labels: 

## 正文

Installing dcgm on a stateless node is untenable at the moment, because the dcgm package is a 1.5GB behemoth of which ~1GB are different versions of CUBLAS and ~240MB are different versions of CURAND. Appropiate versions of both libraries are usually present somewhere else in the system as they are pretty much essential for CUDA applications.

Please consider packaging those libraries separately and letting us point DCGM to our own location for those libraries.
 

## 评论 (5)

### damianam · 2025-02-19

The situation did not improve in the latest releases, it got worse. I think this is a very important issue for diskless systems, and would be great if minimizing the installation footprint of DCGM gets some traction.

### zzzoom · 2025-04-09

I guess we'll have to go with [gpud](https://github.com/leptonai/gpud).

### nikkon-dev · 2025-04-12

The latest DCGM packages are split into multiple packages. Please see the release notes [here](https://docs.nvidia.com/datacenter/dcgm/latest/release-notes/changelog.html#deprecations-and-breaking-changes).

The parts that require cublas are not in the -cuda11/12 packages, and those are not necessary if you only need monitoring functionality of the DCGM and do not need diagnostics. 

### damianam · 2025-04-14

From my POV this is not solved. The latest DCGM is split in CUDA 11 and CUDA 12 packages. But installing just the CUDA 12 packages take more than 1.2 GB. Just `libdcgm_cublas_proxy12.so.4.2.2` takes already 765 MB. And the reason for that is the number of different architectures supported by the same package:

```
$ cuobjdump libdcgm_cublas_proxy12.so.4.2.2  | grep arch | sort | uniq -c | sort -V -k4
    104 arch = sm_50
      1 arch = sm_52
    105 arch = sm_60
     91 arch = sm_61
    161 arch = sm_70
    109 arch = sm_75
    305 arch = sm_80
    110 arch = sm_86
     58 arch = sm_89
    391 arch = sm_90
     83 arch = sm_90a
   1684 arch = sm_100
    575 arch = sm_120
     21 arch = sm_120a
```

To me it would make a lot of sense to split that package not just depending on CUDA versions, but also on architectures. That would slim down the size quite a bit, which is very problematic here for diskless nodes.

### nikkon-dev · 2025-04-14

@damianam, 
Unfortunately, the DCGM team is unable to divide Cublas into smaller components. We have provided feedback to the Cublas library team; however, there are currently no plans to separate it into smaller parts for each architecture.
