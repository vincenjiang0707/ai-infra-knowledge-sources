source: https://docs.nvidia.com/deploy/mps/mpsv3-memory-partitioning.html

# MPS v3 Memory Partitioning[#](https://docs.nvidia.com#mps-v3-memory-partitioning)

MPS v3 memory partitioning fractionalizes a GPU’s device memory across cgroups and
containers, so that a single tenant cannot monopolize the GPU and schedulers such as
Kubernetes can pack workloads by memory. Unlike the older userspace memory limits, this
feature accounts for *all* device memory and integrates with the Linux kernel cgroup
controllers.

This feature requires Linux with cgroup **v2** mounted at `/sys/fs/cgroup`

, CUDA 13.4 or
newer, and a non-MIG device. MIG is explicitly unsupported, with memory reporting left
unaltered for MIG handles. Managed and UVM memory have additional limitations; see
[Known Limitations](https://docs.nvidia.com#id3).

## Soft and Hard Limits[#](https://docs.nvidia.com#soft-and-hard-limits)

Memory partitioning is expressed with two thresholds that define three zones:

```
-- HARD LIMIT --------
FAILURE ZONE (allocations return OUT_OF_MEMORY)
-- SOFT LIMIT --------
PRESSURE ZONE (allocations still succeed; you are "borrowing" from others' share.
Under real contention MPS may evict/kill you.)
-- (0) ---------------
SAFE ZONE: (guaranteed available)
```

Under the dmem controller:

**Hard limit**maps to`dmem.max`

. It is enforced at allocation time; an allocation that would exceed it fails with an out-of-memory error.**Soft limit**maps to`dmem.min`

. It is a*target*, not instant failure. Crossing it makes a client an eviction*candidate*; the client is only actually evicted under real memory pressure.

## Backends[#](https://docs.nvidia.com#backends)

Memory partitioning has two backends, chosen automatically when the driver loads:

**dmem**: used when the kernel (6.14 or newer) has the DMEM cgroup controller present. The kernel`dmem`

controller enforces the hard and soft limits natively.**misc**(the fallback): used on kernels without the DMEM controller. The driver does its own per-cgroup accounting internally.

Note

The dmem backend organizes reservations as a hierarchy per root cgroup. For deployments
that share a single root cgroup across independent workloads follow one of the deployment
models in [Hierarchy and Containers](https://docs.nvidia.com#id1) so that each workload is partitioned independently. The misc backend, which has a flat
one-limit-per-container model with no hierarchy, is a simple alternative for those cases.

Advanced: forcing a backend

The backend can be overridden with the `RmMemacctMode`

registry key, set through the
driver module parameter:

```
# /etc/modprobe.d/nvidia.conf, then reload nvidia.ko
options nvidia NVreg_RegistryDwords="RmMemacctMode=1"
```

Values: `0`

off, `1`

force misc, `2`

force dmem, `3`

auto-detected (default).
The override can only downgrade. The misc backend can also be selected by disabling the
kernel controller with the `cgroup_disable=dmem`

kernel command-line parameter.

## Setting Limits[#](https://docs.nvidia.com#setting-limits)

Limits can be set through `nvidia-smi`

or NVML, both set the same underlying state.
Always set limits through `nvidia-smi`

or NVML rather than writing the `dmem.*`

files
directly. These tools resolve the device key, handle the backend, and maintain
the ancestor propagation described in [Hierarchy and Containers](https://docs.nvidia.com#id1), which manual writes do
not. Limits are specified in **MiB** for `nvidia-smi`

and in bytes for NVML. Both limits
accept a “max” sentinel meaning “device capacity.”

### Using nvidia-smi[#](https://docs.nvidia.com#using-nvidia-smi)

Recommended for manual and operational use.

```
# Set soft = 4 GiB, hard = 8 GiB on a cgroup, for GPU 0
$ sudo nvidia-smi memory-limits --set \
--namespace /sys/fs/cgroup/mygroup \
--soft-limit 4000 --hard-limit 8000 -i 0
# Read back
$ nvidia-smi memory-limits --get -n /sys/fs/cgroup/mygroup -i 0
namespace: /sys/fs/cgroup/mygroup
soft limit: 4096 MiB
hard limit: 8192 MiB
current used: 512 MiB
```

### Using the NVML API[#](https://docs.nvidia.com#using-the-nvml-api)

Recommended for frameworks and orchestrators. Setting limits is privileged; reading them is not.

```
nvmlDeviceSetMemoryLimits_v1_t lim = {
.nameSpace = "/sys/fs/cgroup/mygroup", // full path to the cgroup dir
.softLimit = 4ULL<<30, // bytes (or bSetToMax)
.hardLimit = 8ULL<<30,
};
nvmlDeviceSetMemoryLimits_v1(device, &lim); // privileged
nvmlDeviceGetMemoryLimits_v1_t got = { .nameSpace = "/sys/fs/cgroup/mygroup" };
nvmlDeviceGetMemoryLimits_v1(device, &got); // non-privileged
// got.softLimit / hardLimit / currentLimit (+ bIsMax flags)
```

NVML opens the cgroup directory and applies the limit through the driver. It defaults to the sysfs/dmem path and falls back to the driver’s internal control when dmem is not present. MIG handles are rejected.

## How Limits Are Reported[#](https://docs.nvidia.com#how-limits-are-reported)

Once memory partitioning is active for a container’s cgroup, memory queries reflect the
**limit**, not the physical device.

`cuMemGetInfo`

(v1/v2): reports total and free memory capped to the hard limit and the remaining headroom under it.NVML

`nvmlDeviceGetMemoryInfo_v2`

: reports used, total, and free memory adjusted to account for the soft-limit headroom guarantee and reserved physical memory.MIG: reporting is

**not**altered.

## Enforcement[#](https://docs.nvidia.com#enforcement)

**Hard limit:**an allocation that would exceed`dmem.max`

fails. On dmem the kernel rejects it; on misc the driver checks against the group’s available budget and rejects it. CUDA maps this to`CUDA_ERROR_OUT_OF_MEMORY`

.**Soft limit:**crossing it fires a subdevice soft-limit-exceeded notifier carrying the offending PID. This only*marks it as a candidate*; it is not a kill. Actual eviction is reactive and handled by MPS; see[MPS Pressure Handling and Eviction](https://docs.nvidia.com#mps-pressure-handling-and-eviction).

## Hierarchy and Containers[#](https://docs.nvidia.com#hierarchy-and-containers)

### Setting on a leaf versus a parent[#](https://docs.nvidia.com#setting-on-a-leaf-versus-a-parent)

You can only set a limit on a cgroup that has the dmem controller enabled (has

`dmem.*`

files). Setting on a cgroup with no dmem files returns “not found.”A cgroup with no dmem files (its parent did not add

`+dmem`

to`subtree_control`

) inherits the nearest dmem-enabled ancestor’s limit on*reads*. Set the limit on the enabled ancestor; fileless descendants read it back.**Docker:**setting the limit on the Docker root or pod slice might*not*reach the container, since a**new leaf**cgroup is created for the container with`+dmem`

enabled (so the leaf has its own`dmem.max`

of`max`

). It reports the full GPU and never inherits the ancestor. The fix is to discover the container’s real cgroup*after*creation (for example,`docker inspect`

the container PID, then read its actual`/sys/fs/cgroup/...`

path) and apply the limit on that leaf.

### Ancestor reservation propagation (dmem)[#](https://docs.nvidia.com#ancestor-reservation-propagation-dmem)

Because the kernel computes effective protection hierarchically, a leaf’s `dmem.min`

is
only honored if every ancestor reserves at least as much. The driver’s set-limit path
therefore propagates: it walks parents and adds the delta so that each
`ancestor.dmem.min`

equals the sum of its subtree’s leaf soft limits.

Setting a leaf’s soft

**raises**its ancestors’`dmem.min`

; resetting it to 0**lowers**them.The walk stops at the first ancestor without

`dmem.min`

(the cgroup root, or a gap where`+dmem`

is not enabled). A gap breaks propagation and kernel protection above it so keep the dmem-enabled chain contiguous from the leaf to the reservation point.Only the driver path propagates. This is why limits must be set through

`nvidia-smi`

or NVML; writing the`dmem.*`

files directly bypasses propagation and causes drift.

The ancestor propagation only *decrements* ancestors when the leaf soft is lowered or
zeroed through NVML or `nvidia-smi`

. If the leaf cgroup is **deleted directly** (the
normal container exit/crash lifecycle), the driver never sees it, so the down-delta does
not run and each ancestor keeps its leaf’s contribution.

Before deleting a leaf, zero its soft first (

`nvidia-smi memory-limits --set ... --soft-limit 0 ...`

or NVML with`bSetToMax`

/0) so the ancestors are decremented.Or avoid relying on propagation at all; see

[Deployment models](https://docs.nvidia.com#id2).

### Deployment models[#](https://docs.nvidia.com#deployment-models)

To workaround the shared-root aggregation with dmem, choose one of:

**Separate root per workload.**Each hierarchy is independent; propagation only walks up to its own root and cannot interfere with another.**Force the root reservation to 0**after every set-limits call. A`dmem.min`

of 0 at the root overrides the event system to use manual filesystem checks instead.**Use the misc fallback**(most reliable today). misc has no hierarchy.

## MPS Pressure Handling and Eviction[#](https://docs.nvidia.com#mps-pressure-handling-and-eviction)

MPS is the component that reacts to memory pressure. The MPS server subscribes per-GPU to the soft-limit notifier at startup.

Handling is currently **reactive, not proactive**. The soft limit means “borrowing,” so crossing it
never kills a client outright. The flow is:

A client crosses its soft limit, and the server marks that PID a

**candidate**.Another client’s allocation hits the

**hard**wall and would OOM. Because that client is still within its own soft limit, the CUDA driver requests eviction from the server and blocks on the reply.The server picks an over-soft victim, force-terminates it, and replies with a retry.

The requester retries the allocation with bounded back-off; on success it returns

`CUDA_SUCCESS`

, otherwise`CUDA_ERROR_OUT_OF_MEMORY`

.The evicted victim’s next CUDA call returns

`CUDA_ERROR_MPS_CLIENT_TERMINATED`

.

The server will not evict the requester itself.

## dmem versus misc[#](https://docs.nvidia.com#dmem-versus-misc)

Aspect |
dmem |
misc |
|---|---|---|
Limit store |
kernel |
driver-internal map |
Hierarchy |
kernel effective protection plus driver |
nearest limited ancestor; limits do not nest (a parent cap does not bound limited children) |
Over-soft detection |
MPS compares |
MPS is notified by the driver on charge and uncharge |

## Known Limitations[#](https://docs.nvidia.com#known-limitations)

**MIG:**unsupported; memory reporting is not altered for MIG handles.**UVM / managed memory:**`cudaMallocManaged`

is only tracked by the memory controller in system memory.**Shared root cgroups (dmem):**the kernel aggregates usage up to the root. When a root cgroup is shared across independent workloads, use a deployment model from[Deployment models](https://docs.nvidia.com#id2)to partition each workload independently, and zero a leaf’s soft before deleting its cgroup so the ancestor reservation is released.**Multi-GPU:**`dmem.*`

files are per-GPU; always use the exact device key. Resolve the key from the target device’s PCI BDF.**Contiguous dmem chain:**a gap where`+dmem`

is not enabled at some level breaks propagation and kernel protection above it.

## Diagnostics and Troubleshooting[#](https://docs.nvidia.com#diagnostics-and-troubleshooting)

**Which backend?**Check whether the target cgroup has a`dmem.max`

file. If it does, you are on dmem; if not, you are on misc (or the feature is off):if [ -e /sys/fs/cgroup/<cgroup>/dmem.max ]; then echo "dmem backend" else echo "misc backend (or memory partitioning is off)" fi

**Walk the hierarchy (dmem):**inspect each level’s`dmem.current`

,`dmem.min`

, and`dmem.max`

to confirm the reservations propagated as expected up to the intended ancestor.**Limit not reflected in a container:**check whether the container’s*own*cgroup has a`dmem.max`

value (`max`

means unlimited, which shadows the ancestor). Set the limit on the container’s real leaf cgroup.**Eviction never fires for a within-soft requester:**verify the requester can reach the MPS daemon’s control socket (pipe directory), and that its cgroup soft limit is actually being read.**MPS eviction events:**the MPS daemon logs per-device eviction events – eviction requests, evictions performed, and no-victim counts – useful for confirming eviction behavior under pressure.

## Quick Reference[#](https://docs.nvidia.com#quick-reference)

Set the soft and hard limits on a cgroup for a GPU:

```
sudo nvidia-smi memory-limits --set -n <cgroup> --soft-limit <MiB> --hard-limit <MiB> -i <idx>
```

Read the limits back:

```
nvidia-smi memory-limits --get -n <cgroup> -i <idx>
```