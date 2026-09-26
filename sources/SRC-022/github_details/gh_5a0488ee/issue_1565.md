# [Issue #1565] [Issue]: permuteNetIds hangs when number of NICs is large and MERGE_NIC option is off

source: https://github.com/ROCm/rccl/issues/1565
state: closed | updated: 2026-01-22T02:01:17Z
labels: 

## 正文

### Problem Description

in the current implementation, `permuteNetIds` try to match the topology by permuting over all the ordering of the NIC. 
This is feasible when the number of nics is small (i.e 8) or if the number of NICs is large, but `MERGE_NICS` is turned on (halving the number of NICs seen by rccl) 
This is not feasible when those two conditions are false (i.e the number of NICs is 16 and MERGE_NICS is 0). In this case, `permuteNetIds` in rome_models.cc tries to do 16 factorial permutations which results in rccl hanging and never finishing as the number of permutations is simply too large to complete in a reasonable timeframe. 



### Operating System

Ubuntu Jammy

### CPU

AMD EPYC 9534 64-Core Processor

### GPU

MI300X

### ROCm Version

6.3.0

### ROCm Component

rccl

### Steps to Reproduce

This is easily reproducible with any callstack that leads down to `permuteNetIds` given the system is setup to permute over a large number of NICs. 
I have able to reproduce this issue with 16 interface per node, 2 node, setup, running rccl-test with MERGE_NICS off. 

I have wrote a fix for this issue that I will be making a pr for. 

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (3)

### codinggosu · 2025-02-25

https://github.com/ROCm/rccl/pull/1566 addresses this

### systems-assistant[bot] · 2026-01-22

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/2781

### ammallya · 2026-01-22

Imported to ROCm/rocm-systems
