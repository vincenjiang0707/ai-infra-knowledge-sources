# [Issue #2441] [Issue]: Performance drop 60% in all_reduce_perf 1MB size on AMD CPU

source: https://github.com/NVIDIA/nccl/issues/2441
state: open | updated: 2026-09-23T15:55:55Z
labels: 

## 正文

### How is this issue impacting you?

Lower performance than expected

### Share Your Debug Logs

A performance drop has been introduced, at least on specific hardware. Note the difference in algbw around 1000000B size below:

**BAD RESULTS**
```
# nccl-tests version 2.18.3 nccl-headers=23005 nccl-library=23005
# Collective test starting: all_reduce_perf
# nThread 1 nGpus 1 minBytes 500000 maxBytes 1500000 step: 100000(bytes) warmup iters: 1 iters: 20 agg iters: 1 validation: 1 graph: 0 unalign: 0
#
# Using devices
#  Rank  0 Group  0 Pid 516704 on   gpu-0001 device  0 [0000:61:00] NVIDIA H100 NVL
#  Rank  1 Group  0 Pid 516703 on   gpu-0001 device  1 [0000:81:00] NVIDIA H100 NVL
#  Rank  2 Group  0 Pid 102501 on   gpu-0003 device  0 [0000:61:00] NVIDIA H100 NVL
#  Rank  3 Group  0 Pid 102505 on   gpu-0003 device  1 [0000:81:00] NVIDIA H100 NVL
#
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw  #wrong     time   algbw   busbw  #wrong 
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)             (us)  (GB/s)  (GB/s)         
      500000        125000     float     sum      -1   188.69    2.65    3.97       0   187.07    2.67    4.01       0
      600000        150000     float     sum      -1   226.65    2.65    3.97       0   218.29    2.75    4.12       0
      700000        175000     float     sum      -1   268.44    2.61    3.91       0   272.81    2.57    3.85       0
      800000        200000     float     sum      -1   293.51    2.73    4.09       0   298.92    2.68    4.01       0
      900000        225000     float     sum      -1   320.81    2.81    4.21       0   320.50    2.81    4.21       0
     1000000        250000     float     sum      -1   343.55    2.91    4.37       0   330.00    3.03    4.55       0
     1100000        275000     float     sum      -1   152.97    7.19   10.79       0   155.83    7.06   10.59       0
     1200000        300000     float     sum      -1   169.20    7.09   10.64       0   167.52    7.16   10.74       0
     1300000        325000     float     sum      -1   179.04    7.26   10.89       0   179.55    7.24   10.86       0
     1400000        350000     float     sum      -1   188.43    7.43   11.14       0   192.10    7.29   10.93       0
     1500000        375000     float     sum      -1   199.46    7.52   11.28       0   198.58    7.55   11.33       0
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 7.20321 
#
# Collective test concluded: all_reduce_perf
# 
```

**GOOD RESULTS**
```
# nccl-tests version 2.18.3 nccl-headers=23005 nccl-library=23005
# Collective test starting: all_reduce_perf
# nThread 1 nGpus 1 minBytes 500000 maxBytes 1500000 step: 100000(bytes) warmup iters: 1 iters: 20 agg iters: 1 validation: 1 graph: 0 unalign: 0
#
# Using devices
#  Rank  0 Group  0 Pid 518105 on   gpu-0001 device  0 [0000:61:00] NVIDIA H100 NVL
#  Rank  1 Group  0 Pid 518104 on   gpu-0001 device  1 [0000:81:00] NVIDIA H100 NVL
#  Rank  2 Group  0 Pid 103910 on   gpu-0003 device  0 [0000:61:00] NVIDIA H100 NVL
#  Rank  3 Group  0 Pid 103909 on   gpu-0003 device  1 [0000:81:00] NVIDIA H100 NVL
#
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw  #wrong     time   algbw   busbw  #wrong 
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)             (us)  (GB/s)  (GB/s)         
      500000        125000     float     sum      -1   195.98    2.55    3.83       0   189.47    2.64    3.96       0
      600000        150000     float     sum      -1   235.38    2.55    3.82       0   264.05    2.27    3.41       0
      700000        175000     float     sum      -1   113.68    6.16    9.24       0   115.22    6.08    9.11       0
      800000        200000     float     sum      -1   130.87    6.11    9.17       0   130.28    6.14    9.21       0
      900000        225000     float     sum      -1   134.32    6.70   10.05       0   133.70    6.73   10.10       0
     1000000        250000     float     sum      -1   145.95    6.85   10.28       0   145.33    6.88   10.32       0
     1100000        275000     float     sum      -1   158.45    6.94   10.41       0   156.33    7.04   10.55       0
     1200000        300000     float     sum      -1   170.61    7.03   10.55       0   170.35    7.04   10.57       0
     1300000        325000     float     sum      -1   181.67    7.16   10.73       0   180.50    7.20   10.80       0
     1400000        350000     float     sum      -1   191.86    7.30   10.95       0   191.16    7.32   10.99       0
     1500000        375000     float     sum      -1   200.43    7.48   11.23       0   200.24    7.49   11.24       0
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 9.11404 
#
# Collective test concluded: all_reduce_perf
# 
```

A git bisect returned this commit as the introducer:
```
commit 2f1c174c4bdf12383b4e1ad01bd62d429d1301dc
Author: Martin Vit <martin@voipmonitor.org>
Date:   Tue Mar 31 14:04:28 2026 +0000


    Fix AMD inter-CPU bandwidth detection: add per-generation values
    
    NCCL uses a single flat bandwidth value (16 GB/s) for all AMD CPUs,
    while Intel has 4 model-specific tiers. This leads to suboptimal
    topology decisions on modern AMD platforms where inter-socket bandwidth
    is significantly higher.
    
    This patch:
    
    1. Adds per-generation AMD CPU model detection using CPUID family IDs:
       - Zen 1/2 (Naples/Rome, family 23): 16 GB/s (unchanged)
       - Zen 3/4 (Milan/Genoa, family 25): 24 GB/s
       - Zen 5 (Turin, family 26): 32 GB/s
    
    2. Fixes the CPUID familyId/modelId computation in xml.cc per x86 spec:
       - familyId: add extFamilyId only when base familyId == 15
       - modelId: add extModelId << 4 only when familyId is 6 or 15
    
    Bandwidth values were validated on dual-socket AMD EPYC 9575F (Turin)
    with cross-socket GPU P2P measurements averaging 32.18 GB/s. Zen 3/4
    value (24 GB/s) is a conservative estimate pending hardware validation.
    
    Signed-off-by: Martin Vit <martin@voipmonitor.org>
    
    Mirrored-from: 18c0eac4e206ef5766d9e0c1c8f9338a04a7ba11


 src/graph/topo.cc   | 15 ++++++++++++++-
 src/graph/topo.h    |  4 +++-
 src/graph/xml.cc    |  6 ++++--
 src/include/graph.h |  3 +++
 4 files changed, 24 insertions(+), 4 deletions(-) 
```

### Steps to Reproduce the Issue

Run nccl-tests sweep around 1000000B size, and see the algbw drops from a target ~10 GB/s to ~4GB/s.


### NCCL Version

2f1c174c4bdf12383b4e1ad01bd62d429d1301dc

### Your platform details

Hardware:
AMD EPYC 9534 64-Core Processor
2x NVIDIA H100 NVL

Networking: Slingshot-200 Cassini-2 NICs
```
# lscpu
Architecture:             x86_64
  CPU op-mode(s):         32-bit, 64-bit
  Address sizes:          52 bits physical, 57 bits virtual
  Byte Order:             Little Endian
CPU(s):                   256
  On-line CPU(s) list:    0-255
Vendor ID:                AuthenticAMD
  Model name:             AMD EPYC 9534 64-Core Processor
    CPU family:           25
    Model:                17
    Thread(s) per core:   2
    Core(s) per socket:   64
    Socket(s):            2
    Stepping:             1
    Frequency boost:      enabled
    CPU(s) scaling MHz:   62%
    CPU max MHz:          2450.0000
    CPU min MHz:          1500.0000
    BogoMIPS:             4892.27
    Flags:                fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good amd_lbr_v2 nopl n
                          onstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_leg
                          acy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba perfmon_v2 ibrs ibpb stibp 
                          ibrs_enhanced vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec x
                          getbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local user_shstk avx512_bf16 clzero irperf xsaveerptr rdpru wbnoinvd amd_ppin cppc amd_ibpb_ret arat npt lbrv svm_lock nrip_sav
                          e tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif x2avic v_spec_ctrl vnmi avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqdq av
                          x512_vnni avx512_bitalg avx512_vpopcntdq la57 rdpid overflow_recov succor smca fsrm flush_l1d debug_swap
Virtualization features:  
  Virtualization:         AMD-V
Caches (sum of all):      
  L1d:                    4 MiB (128 instances)
  L1i:                    4 MiB (128 instances)
  L2:                     128 MiB (128 instances)
  L3:                     512 MiB (16 instances)
NUMA:                     
  NUMA node(s):           8
  NUMA node0 CPU(s):      0-15,128-143
  NUMA node1 CPU(s):      16-31,144-159
  NUMA node2 CPU(s):      32-47,160-175
  NUMA node3 CPU(s):      48-63,176-191
  NUMA node4 CPU(s):      64-79,192-207
  NUMA node5 CPU(s):      80-95,208-223
  NUMA node6 CPU(s):      96-111,224-239
  NUMA node7 CPU(s):      112-127,240-255
Vulnerabilities:          
  Gather data sampling:   Not affected
  Itlb multihit:          Not affected
  L1tf:                   Not affected
  Mds:                    Not affected
  Meltdown:               Not affected
  Mmio stale data:        Not affected
  Reg file data sampling: Not affected
  Retbleed:               Not affected
  Spec rstack overflow:   Mitigation; Safe RET
  Spec store bypass:      Mitigation; Speculative Store Bypass disabled via prctl
  Spectre v1:             Mitigation; usercopy/swapgs barriers and __user pointer sanitization
  Spectre v2:             Mitigation; Enhanced / Automatic IBRS; IBPB conditional; STIBP always-on; RSB filling; PBRSB-eIBRS Not affected; BHI Not affected
  Srbds:                  Not affected
  Tsx async abort:        Not affected
```

### Error Message & Behavior

~60% slower performance at specific message sizes

## 评论 (8)

### codambro · 2026-09-22

Attached `NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=INIT,BOOTSTRAP,ENV,GRAPH,TUNING` for both good and bad run, as well as topo dump from `NCCL_TOPO_DUMP_FILE`.
As a test, I tried using the "good" topo file against the offending nccl commit with `NCCL_TOPO_FILE=ncclSystem.good.txt`, but it did not help.
This is the diff:
```
# diff ncclSystem.good.txt ncclSystem.bad.txt 
2c2
<   <cpu host_hash="0x9a77867c7a11a438" numaid="1" affinity="00000000,00000000,00000000,ffff0000,00000000,00000000,00000000,ffff0000" arch="x86_64" vendor="AuthenticAMD" familyid="175" modelid="17">
---
>   <cpu host_hash="0x9a77867c7a11a438" numaid="1" affinity="00000000,00000000,00000000,ffff0000,00000000,00000000,00000000,ffff0000" arch="x86_64" vendor="AuthenticAMD" familyid="25" modelid="17">
7c7
<   <cpu host_hash="0x9a77867c7a11a438" numaid="0" affinity="00000000,00000000,00000000,0000ffff,00000000,00000000,00000000,0000ffff" arch="x86_64" vendor="AuthenticAMD" familyid="175" modelid="17">
---
>   <cpu host_hash="0x9a77867c7a11a438" numaid="0" affinity="00000000,00000000,00000000,0000ffff,00000000,00000000,00000000,0000ffff" arch="x86_64" vendor="AuthenticAMD" familyid="25" modelid="17">
14c14
<   <cpu host_hash="0x9a77867c7a11a438" numaid="7" affinity="ffff0000,00000000,00000000,00000000,ffff0000,00000000,00000000,00000000" arch="x86_64" vendor="AuthenticAMD" familyid="175" modelid="17">
---
>   <cpu host_hash="0x9a77867c7a11a438" numaid="7" affinity="ffff0000,00000000,00000000,00000000,ffff0000,00000000,00000000,00000000" arch="x86_64" vendor="AuthenticAMD" familyid="25" modelid="17">
```
[bad.nccl_debug.log](https://github.com/user-attachments/files/32524330/bad.nccl_debug.log)
[good.nccl_debug.log](https://github.com/user-attachments/files/32524332/good.nccl_debug.log)
[ncclSystem.bad.txt](https://github.com/user-attachments/files/32524333/ncclSystem.bad.txt)
[ncclSystem.good.txt](https://github.com/user-attachments/files/32524331/ncclSystem.good.txt)

### codambro · 2026-09-22

If I modify the TOPO file manually to set `familyId` to 24 to force `NCCL_TOPO_CPU_MODEL_AMD_ZEN12`, bandwidth returns to expected values.

### ryanhankins · 2026-09-22

@voipmonitor FYI

### sjeaugey · 2026-09-23

The new code adjusts bandwidth to reflect what more recent CPUs can do. Unfortunately, in your case, the performance is pretty low.

It could be due to various factors, like low CPU memory bandwidth, or other things we can hardly control. Setting the family id to a lower value (even 0) should tell NCCL that your GPU-to-GPU bandwidth through the CPU is lower and re-adjust the tuning.

Out of curiosity, could you run again with `mpirun --bind-to numa`? (or equivalent for your MPI version) It looks like you left the MPI default `--bind-to core`, which can severely limit the network communication performance.

### codambro · 2026-09-23

We use numactl to bind. Unfortunately our NIC and GPUs are not on the same NUMA domain. So there is some penalty there we can't avoid. This ticket though is specifically for the perf drop at the 1MB size before/after the offending commit.

### sjeaugey · 2026-09-23

I was referring to the CPU affinity. With default settings, `--bind-to core`, the NCCL network thread would be bound to a single core, which would also run the main thread and potentially others. This can affect the network performance negatively, potentially more for the LL protocol than for the Simple protocol, which could explain why performance is bad when we use LL and why you see a performance degradation.

It could also be that the memory bandwidth is low -- I just want to remove one issue, since I believe I saw in your logs that each process was bound to a single core. I could have misunderstood the logs though.

### codambro · 2026-09-23

slurm equivalent is ldoms, but it was no different

```
# srun -N 2 --ntasks-per-node=2 --cpu-bind=ldoms ./all_reduce_perf -b 500000 -e 1500000 -i 100000
# nccl-tests version 2.18.3 nccl-headers=23005 nccl-library=23005
# Collective test starting: all_reduce_perf
# nThread 1 nGpus 1 minBytes 500000 maxBytes 1500000 step: 100000(bytes) warmup iters: 1 iters: 20 agg iters: 1 validation: 1 graph: 0 unalign: 0
#
# Using devices
#  Rank  0 Group  0 Pid 363100 on   gpu-0001 device  0 [0000:61:00] NVIDIA H100 NVL
#  Rank  1 Group  0 Pid 363101 on   gpu-0001 device  1 [0000:81:00] NVIDIA H100 NVL
#  Rank  2 Group  0 Pid  45578 on   gpu-0003 device  0 [0000:61:00] NVIDIA H100 NVL
#  Rank  3 Group  0 Pid  45579 on   gpu-0003 device  1 [0000:81:00] NVIDIA H100 NVL
#
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw  #wrong     time   algbw   busbw  #wrong 
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)             (us)  (GB/s)  (GB/s)         
      500000        125000     float     sum      -1   192.43    2.60    3.90       0   210.98    2.37    3.55       0
      600000        150000     float     sum      -1   270.75    2.22    3.32       0   241.48    2.48    3.73       0
      700000        175000     float     sum      -1   280.79    2.49    3.74       0   290.15    2.41    3.62       0
      800000        200000     float     sum      -1   338.11    2.37    3.55       0   312.38    2.56    3.84       0
      900000        225000     float     sum      -1   357.12    2.52    3.78       0   340.26    2.65    3.97       0
     1000000        250000     float     sum      -1   373.04    2.68    4.02       0   369.82    2.70    4.06       0
     1100000        275000     float     sum      -1   156.74    7.02   10.53       0   162.24    6.78   10.17       0
     1200000        300000     float     sum      -1   176.40    6.80   10.20       0   178.91    6.71   10.06       0
     1300000        325000     float     sum      -1   187.06    6.95   10.42       0   182.77    7.11   10.67       0
     1400000        350000     float     sum      -1   194.49    7.20   10.80       0   195.59    7.16   10.74       0
     1500000        375000     float     sum      -1   207.62    7.22   10.84       0   206.01    7.28   10.92       0
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 6.83755 
#
# Collective test concluded: all_reduce_perf
#
```

### sjeaugey · 2026-09-23

Ok, thanks for confirming.

