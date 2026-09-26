# [Issue #2107] [Issue]: Intel Granite Rapids (GNR) are misdetected with lower UPI InterCpuBw

source: https://github.com/NVIDIA/nccl/issues/2107
state: open | updated: 2026-09-03T14:06:31Z
labels: 

## 正文

### How is this issue impacting you?

Lower performance than expected

### Share Your Debug Logs

Hello

Current version of ncclTopoGetInterCpuBw function has no support of GNR family of Intel Xeon CPUs
https://github.com/NVIDIA/nccl/blob/v2.30.3-1/src/graph/topo.cc#L73

```
  if (cpu->cpu.arch == NCCL_TOPO_CPU_ARCH_X86 && cpu->cpu.vendor == NCCL_TOPO_CPU_VENDOR_INTEL) {
    *bw =
      cpu->cpu.model == NCCL_TOPO_CPU_MODEL_INTEL_ERP ? ERP_QPI_BW :
      cpu->cpu.model == NCCL_TOPO_CPU_MODEL_INTEL_SRP ? SRP_QPI_BW :
      cpu->cpu.model == NCCL_TOPO_CPU_MODEL_INTEL_SKL ? SKL_QPI_BW :
      BDW_QPI_BW;
  }
```

I think that `familyId == 6 && modelId == 0xAD` will detect GNR Xeon chips, and they have UPI speed of 24 GT/s per channel (with multiple UPI links between sockets)
https://www.intel.com/content/www/us/en/products/sku/242668/intel-xeon-6507p-processor-48m-cache-3-50-ghz/specifications.html

I think for NCCL graph this will be GNR_QPI_BW equal to 48.0

Some [sources](https://github.com/torvalds/linux/blob/v7.0/arch/x86/include/asm/intel-family.h#L126) also mention modelId 0xAE as GRANITERAPIDS D, but they are probably [single socket only](https://www.intel.com/content/www/us/en/ark/products/codename/228655/products-formerly-granite-rapidsd.html#@Server).

Current version may allocate less channels for 2 NUMA GNR machines with multiple PCIe-only GPUs without NVlink. I had 'SYS[22.0]' in NCCL_DEBUG with current code, and 'SYS[48.0]' after fixing, and busbw of all_reduce_perf improved after the fix.

### Steps to Reproduce the Issue

_No response_

### NCCL Version

2.30.3

### Your platform details

_No response_

### Error Message & Behavior

_No response_

## 评论 (1)

### avnf · 2026-09-03

Commit https://github.com/NVIDIA/nccl/commit/35671f48a5ccc27dbf5854372c948cb8c36456cf from https://github.com/NVIDIA/nccl/pull/2339 (2.31.2-1 release) had partial fix for GNR family, probably from

> Improves algorithm selection on newer Intel CPUs.

UPI Speed of ERP is now used for GNR CPUs.

```
      // Granite Rapids (0xAD/0xAE) and Sierra Forest (0xAF) are newer than Emerald Rapids but carry LOWER model IDs
      cpu->cpu.model = (familyId == 6 && (modelId >= 0xCF || modelId == 0xAD || modelId == 0xAE || modelId == 0xAF)) ?
                         NCCL_TOPO_CPU_MODEL_INTEL_ERP :
```

