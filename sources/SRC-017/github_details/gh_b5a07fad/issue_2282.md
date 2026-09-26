# [Issue #2282] [Issue]: NET/IB out-of-bounds write / crash when a node exposes more than MAX_IB_DEVS active IB ports

source: https://github.com/NVIDIA/nccl/issues/2282
state: open | updated: 2026-08-12T11:20:55Z
labels: 

## 正文

### How is this issue impacting you?

Application crash

### Share Your Debug Logs

The crash occurs inside ncclIbInitDevices() during NET/IB device enumeration,
before any collective runs. This node exposes 22 IB devices / 54 active RoCE
ports (multi-port mlx5 roce_r* devices + 8 roce_vf_* VFs), i.e. more than the
default MAX_IB_DEVS (32).

Full NCCL_DEBUG=INFO logs / a core backtrace can be provided on request.

### Steps to Reproduce the Issue

Minimal steps:
1. Use a host that exposes more than MAX_IB_DEVS (32) active IB/RoCE ports.
   Here: 22 IB devices / 54 active RoCE ports (multi-port mlx5 roce_r* + 8 roce_vf_* VFs).
2. Build stock NCCL (MAX_IB_DEVS defaults to 32) and run any NCCL program, e.g.:
   all_reduce_perf -b 1M -e 1M -f 2 -g 8
3. NCCL crashes during initialization, in NET/IB device enumeration.

- Intermittency: deterministic, 100% at init.
- Also reproducible on any machine by lowering MAX_IB_DEVS below the active-port
  count and rebuilding.
- Raising MAX_IB_DEVS above the active-port count (e.g. 128) avoids the crash,
  which pointed to an enumeration overflow rather than a hardware issue.

### NCCL Version

2.30.7

### Your platform details

- GPU & Network: 8-GPU node; multi-port RoCE (mlx5). 22 IB devices,
  54 active RoCE ports total (several roce_r* devices report many phys ports; + 8 roce_vf_* VFs).
- Environment: bare-metal, Ubuntu 24.04, CUDA 13.2.
- Scalability: fails at initialization, independent of rank/node count.

### Error Message & Behavior

First error: segfault during ncclIbInit (NET/IB device enumeration), before any collective runs.

Expected vs actual: NCCL should use at most MAX_IB_DEVS devices and ignore the rest;
it must never write past ncclIbDevs[MAX_IB_DEVS].

Root cause: in ncclIbInitDevices() (src/transport/net_ib/init.cc) the bound
`ncclNIbDevs < MAX_IB_DEVS` is only checked in the OUTER per-device loop:

    for (int d = 0; d < nIbDevs && ncclNIbDevs < MAX_IB_DEVS; d++) {
      for (int port_num = 1; port_num <= devAttr.phys_port_cnt; port_num++) {   // no bound
        for (int dev = devOffset; dev < devCount; ++dev) {                      // no bound
          ncclIbDevs[ncclNIbDevs] = ...;                                        // write
          ncclNIbDevs++;
        }
      }
    }

The inner per-port loop and the data-direct sub-loop both write ncclIbDevs[ncclNIbDevs]
and increment ncclNIbDevs without re-checking the bound, so a single multi-port device
can push ncclNIbDevs past MAX_IB_DEVS within one outer iteration and write past the end
of the global ncclIbDevs[MAX_IB_DEVS] array. The overflowed index is also handed to the
per-device async thread and later to qsort().

I will open a PR with a fix (guard both inner loops with the same bound + warn once when
the limit is reached; MAX_IB_DEVS itself unchanged) and link it here.

## 评论 (4)

### armratner · 2026-07-14

Hi Peng, what is the use case to having such a big amount of VFs?
Is this experimental?

- Armen

### Peng-Xu · 2026-07-15

> Hi Peng, what is the use case to having such a big amount of VFs? Is this experimental?
> 
> * Armen

Hi Armen,

The VFs just exposed it — the real issue is a missing bounds check in NCCL's own enumeration code. In ncclIbInitDevices() the outer per-device loop is guarded with ncclNIbDevs < MAX_IB_DEVS, but the inner per-port / data-direct loops are not, so any host with more than MAX_IB_DEVS active ports writes past ncclIbDevs[MAX_IB_DEVS] — an out-of-bounds write that crashes. The patch adds the same guard to the inner loops.

(For context: real production, not an experiment)

Thanks, Peng

### armratner · 2026-08-05

Appologies Peng, I've missed your reply, I understand what you're saying.
What I'm asking is, is this is is a real use case?

Armen

### Peng-Xu · 2026-08-12

Hi Armen,

Yes, this is a real production deployment.

These are 8-GPU bare-metal nodes used in our production GPU cluster. The large port count comes from our network topology and SR-IOV configuration. Several mlx5/RoCE devices expose multiple ports, together with 8 RoCE VFs used for different workload scenarios, resulting in 54 active RoCE ports visible to NCCL.

This configuration is used to support several production scenarios, and we expect the scale to grow further. In future deployments, the number of exposed ports/devices could potentially reach 256 or more.

So this is not a configuration created specifically to reproduce or stress NCCL. We encountered the issue naturally in production, and we would like the enumeration logic to remain safe even as the configuration scales.

Thanks,
Peng
