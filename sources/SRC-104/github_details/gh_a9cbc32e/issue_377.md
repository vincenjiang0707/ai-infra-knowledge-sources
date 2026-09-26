# [Issue #377] local:remote in QPX-NPS4 is not reported correctly 

source: https://github.com/ROCm/rocprofiler-compute/issues/377
state: closed | updated: 2025-08-06T18:28:15Z
labels: enhancement

## 正文

**Is your feature request related to a problem? Please describe.**
I am running a microbenchmark for QPX+NPS4 mode on MI300X and see the amount of remote:local traffic. However, “TCC_EA0_RDREQ_sum” is always equal “TCC_EA0_RDREQ_DRAM_sum”, no matter what I did in the kernel code . For example, I wrote my code such that each XCD reads all required data from other adjacent XCD’s memory, so all the traffic is remote, however, these the two counters are still the same. It seems what's happening in non-SPX mode on MI300, these requests are still being counted as going "to a DRAM, somewhere".

**Describe the solution you'd like**
What I expect as in MI200 multi-socket, in this microbenchmark,  "TCC_EA0_RDREQ_sum" should be higher than "TCC_EA0_RDREQ_DRAM_sum”
Some further tests would be:
•	On MI300X, I still expect accesses to the CPU DRAM to be counted as "remote"
•	We need to check how these are counted on MI300A, where everything is HBM.
•	We need to check how memory access to a different socket is counted




## 评论 (2)

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/54

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
