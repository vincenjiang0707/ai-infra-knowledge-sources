# [Issue #2335] VFIO P2P on GeForce maps to a private mirror; NCCL hangs or corrupts

source: https://github.com/NVIDIA/nccl/issues/2335
state: closed | updated: 2026-08-22T08:29:39Z
labels: 

## 正文

## Summary

On a 2-GPU VFIO passthrough VM, QEMU's `x-nv-gpudirect-clique` makes the NVIDIA driver grant bidirectional peer access, but the resulting mapping is a **private mirror**, not a path to the peer:

- GPU A writes a pattern through GPU B's peer window.
- GPU A reads the complete pattern back through that window.
- GPU B reads its allocation locally and still sees zeros.
- The result is symmetric in both directions.

This causes every normal NCCL P2P protocol to hang; the one tested copy-engine workaround completes with silently wrong results. The complete observable address chain is correct through QEMU/VFIO, the host IOMMU, Linux DMA APIs, and NVIDIA's open Kernel RM. The mirror forms **after the open KRM boundary**, inside closed GSP-RM/GPU peer-aperture or page-table state.

## Environment

- 2× GeForce RTX 3090 (GA102), PCIe passthrough, no NVLink
- Guest: Ubuntu 24.04, kernel 6.8, NVIDIA 610.57.04 open kernel module
- Host: Proxmox VE 9.1, QEMU 10.1, q35
- `x-nv-gpudirect-clique=1` on both GPUs
- `NVreg_RegistryDwords="RMForceStaticBar1=1;PeerMappingOverride=1"`
- `cudaDeviceCanAccessPeer=1` and `nvidia-smi topo -p2p {r,w}=OK` both ways
- NCCL failure reproduced on 2.25.1, 2.28.9, and 2.29.7

## Minimal discriminator

Observed with a 1 KiB target allocation:

```text
dir 0->1  writer read-back: c0ffee00 5ec897b9  (PAT=c0ffee00 5ec897b9)
dir 0->1  owner local read:  00000000 00000000
dir 1->0  writer read-back: c0ffee00 5ec897b9  (PAT=c0ffee00 5ec897b9)
dir 1->0  owner local read:  00000000 00000000
```

On a healthy mapping, both reads return the pattern. Round-trip bandwidth tests falsely pass because write-to-mirror followed by read-from-mirror is an identity operation.

<details>
<summary>Complete CUDA reproducer</summary>

Build with `nvcc -arch=sm_86 -O2 -o mirror-proof mirror-proof.cu`.

```cuda
#include <cstdio>
#include <cuda_runtime.h>
#define N 256
#define PAT(i) (0xC0FFEE00u ^ (0x9E3779B9u*(unsigned)(i)))
#define CK(x) do { cudaError_t e_=(x); if (e_!=cudaSuccess) { \
  printf("API_ERR %s: %s\n", #x, cudaGetErrorString(e_)); return 1; } } while (0)

__global__ void k_write(unsigned *d) {
  for (int i=0; i<N; i++) d[i]=PAT(i);
  __threadfence_system();
}
__global__ void k_read(const unsigned *d, unsigned *out) {
  for (int i=0; i<N; i++) out[i]=d[i];
}

int main() {
  for (int d=0; d<2; d++) {
    CK(cudaSetDevice(d));
    cudaError_t e=cudaDeviceEnablePeerAccess(1-d,0);
    if (e!=cudaSuccess && e!=cudaErrorPeerAccessAlreadyEnabled) return 1;
    cudaGetLastError();
  }
  for (int p=0; p<2; p++) {
    int c=1-p; unsigned *tgt,*rb_p,*rb_c,h[8];
    CK(cudaSetDevice(c));
    CK(cudaMalloc(&tgt,N*4)); CK(cudaMemset(tgt,0,N*4));
    CK(cudaMalloc(&rb_c,N*4)); CK(cudaDeviceSynchronize());
    CK(cudaSetDevice(p)); CK(cudaMalloc(&rb_p,N*4));
    k_write<<<1,1>>>(tgt); CK(cudaDeviceSynchronize());
    k_read<<<1,1>>>(tgt,rb_p); CK(cudaDeviceSynchronize());
    CK(cudaMemcpy(h,rb_p,32,cudaMemcpyDeviceToHost));
    printf("dir %d->%d writer: %08x %08x (PAT=%08x %08x)\n",
           p,c,h[0],h[1],PAT(0),PAT(1));
    CK(cudaSetDevice(c));
    k_read<<<1,1>>>(tgt,rb_c); CK(cudaDeviceSynchronize());
    CK(cudaMemcpy(h,rb_c,32,cudaMemcpyDeviceToHost));
    printf("dir %d->%d owner:  %08x %08x\n",p,c,h[0],h[1]);
    CK(cudaFree(tgt)); CK(cudaFree(rb_c));
    CK(cudaSetDevice(p)); CK(cudaFree(rb_p));
  }
}
```
</details>

## Address-chain localization

| Layer | Observation | Verdict |
|---|---|---|
| Guest BAR1 | GPU 0 `0x380000000000`; GPU 1 `0x381000000000`; 32 GiB each | Correct |
| QEMU/VFIO + host IOMMU | Guest IOVAs mapped to physical peer BAR1: `0x380000000000 -> 0x7f000000000`, `0x381000000000 -> 0x7e000000000` | Correct; no faults |
| NVIDIA open KRM during mirror repro | kprobe/kretprobe on `nv_dma_map_peer()` and `nv_dma_map_mmio()` | `NV_OK` |
| Peer GPU 0 BAR1 | input `0x380000000000` -> DMA output `0x380000000000` | Correct |
| Peer GPU 1 BAR1 | input `0x381000000000` -> DMA output `0x381000000000` | Correct |
| GPU-visible result | writer sees pattern; owner sees zeros | Mirror forms after KRM |

The host-IOMMU trace was captured on a separate boot with the same BAR layout and the clique hint removed; the clique property is a capability assertion and does not implement a different DMA mapping path. The KRM trace and mirror result were captured together on the same clique-enabled run.

There were no Xid, AER, VFIO, guest-IOMMU, or host-IOMMU faults. A full guest-RAM scan with a passing positive control found no live mirror tags. This rules out an absent/wrong VFIO BAR mapping, guest or host RAM aliasing, Linux `dma_map_resource()`, and peer-to-self substitution in open KRM.

`NVreg_EnableGpuFirmwareLogs=1` could not provide deeper logs because the packaged driver lacks `gsp_log_ga10x.bin`.

## NCCL effect

Official `nccl-tests` reproducer:

```bash
all_reduce_perf -b 4 -e 4 -n 1 -w 1 -g 2 -T 10
```

| Path | Result |
|---|---|
| Ring/LL | hangs polling receiver flags |
| Simple | hangs polling `ncclRecvMem::tail` |
| LL128 | hangs polling receiver flags |
| Simple + `NCCL_P2P_USE_CUDA_MEMCPY=1` | **completes with wrong output** (`#wrong 2`) |

Changing the polls to cache-volatile loads or system-scope acquire/release operations did not help: no transaction reaches the intended peer allocation.

## Questions for NVIDIA

1. Is clique-granted P2P between VFIO-passed GeForce GPUs expected to provide a valid peer aperture, or is this outside the supported envelope?
2. If unsupported, can the driver decline the grant instead of exposing silently incorrect backing?
3. Which component owns peer-aperture programming after `nv_dma_map_peer()` returns, and is a vendor diagnostic build or trace available?

## Workaround

`NCCL_P2P_DISABLE=1` or `NCCL_P2P_LEVEL=PXB` is stable. Do **not** use `NCCL_P2P_USE_CUDA_MEMCPY=1` on this failure class because it can silently return incorrect results.

---

*Disclosure: this investigation and report were prepared with AI assistance (Claude and Codex) under my direction. The traces and measurements are from my hardware, and I stand behind the content.*


## 评论 (6)

### aarav1109s · 2026-08-10

Proposed NCCL-side mitigation in https://github.com/NVIDIA/nccl/pull/2338 (from @aarav1109s):

- Opt-in `NCCL_P2P_VALIDATE=1`: owner-verified one-way `cudaMemcpyPeer` during `p2pCanConnect`; failed pairs fall back instead of hanging / silently corrupting under `NCCL_P2P_USE_CUDA_MEMCPY`.
- Troubleshooting + env docs for this false-grant / private-mirror class (destination-local check, not round-trip bandwidth).

This does not fix the post-KRM aperture programming called out in the issue; it only fails closed when the visibility contract is broken. Happy to adjust probe placement/default based on maintainer guidance (CONTRIBUTING asks to discuss driver workarounds first).

### aarav1109s · 2026-08-10

Follow-up on https://github.com/NVIDIA/nccl/pull/2338 (`7cfb5757`): when `NCCL_P2P_VALIDATE=1` cannot resolve a peer to a visible CUDA device (IPC/VMM invisible-device path), validation now fails closed and disables P2P for that pair instead of silently skipping the probe.

### xiaofanl-nvidia · 2026-08-19

Based on the problem description, this is more about the RM driver behavior for P2P mapping on this platform, not really an NCCL issue. If lower level P2P mapping is not set up correctly, NCCL will not work. I don't think it's reasonable to ask NCCL to not trust the lower level APIs and do extra checks. 

I will bring this issue up to RM team's attention. But I also encourage the users running into this issue to bring up with official support channel if that's available to you. 

Closing this for now from NCCL POV. I will still update this later if I hear back from RM team. 

### xiaofanl-nvidia · 2026-08-21

@noonghunna driver team confirmed that they have logged an internal case for this issue. You can use this number to refer to it if you are working with a solutions architect from NV: 6637419. Thanks for the detailed report. I believe that was helpful to the driver team. 

### noonghunna · 2026-08-22

Thank you @xiaofanl-nvidia. I'm not currently working with a solutions architect at the moment, but i'll make a note of it. 
I'm glad that the team found the findings helpful.

### noonghunna · 2026-08-22

**Follow-up — layer attribution (for internal case #6637419)**

Thanks, @xiaofanl-nvidia. One result from after we filed that may help the driver team narrow the case: we localized *where* the mirrored peer writes actually land, and it is **not in the guest's physical RAM**.

**Method.** Planted 262,144 uniquely-tagged pages across the guest's physical address space, exercised the peer path, then scanned the guest's `/proc/kcore` direct map (~198 GiB) for both the owner-side and mirror-side payloads.

- **Control** (owner-local tags): recovered as expected — the scan works.
- **Mirror**: **0 of 262,144** mirror-side tags present anywhere in guest RAM (only 133 incidental background matches, far below the 262,144 detection threshold).

So the mirror's backing store is **outside the guest's physical memory**. Two hypotheses remain, and neither is separable from inside the guest:

1. **Host RAM not mapped into the guest** — there is a ~56–60 GiB gap between host (256 GiB) and guest (196.5 GiB) that a guest-side scan structurally cannot see.
2. **An own-BAR / private-aperture loopback** — the peer write resolving into the device's own aperture rather than the peer's HBM.

Distinguishing the two needs a **host-side IOMMU page-table dump** (our Proxmox host kernel exposes no AMD-Vi debugfs) or **GSP-side instrumentation** — neither reachable from the guest. That is the boundary of what a guest-side repro can attribute; the remainder is host-IOMMU / driver-side.

Rig, for the record: Proxmox (QEMU/KVM) Q35 + ICH9 guest, 2× RTX 3090 via VFIO passthrough, GeForce (no NVLink), host 256 GiB / guest 196.5 GiB. Happy to run any specific host-side capture a solutions architect wants against #6637419.

