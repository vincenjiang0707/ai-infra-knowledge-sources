# [Issue #2160] NCCL_TOPO_XML_MAX_NODES=256 limit hit during intra-node XML fusion on 32-NIC hosts (AWS p5.48xlarge)

source: https://github.com/NVIDIA/nccl/issues/2160
state: open | updated: 2026-09-21T01:37:53Z
labels: resolved

## 正文

# Issue: hit `NCCL_TOPO_XML_MAX_NODES=256` limit during intra-node XML fusion on 32-NIC hosts (AWS p5.48xlarge)

## Summary

On AWS p5.48xlarge (8 x H100, 32 EFA NICs), `ncclTopoFuseXml` hits its 256-node XML buffer cap while fusing the 8 local-rank XMLs at initialization. The error fires as:

```
graph/xml.h: NCCL WARN Error : too many XML nodes (max 256)
```

Each rank autogenerates ~126 XML nodes from its `/sys/class/pci_bus/*` walk on this host shape; per-rank dedup during `ncclTopoFuseXmlRecursive` is insufficient to hold the merged output below 256 nodes on our reproducer.

## Reproducer

- Hardware: AWS p5.48xlarge (8 GPUs, 32 EFA NICs)
- NCCL: 2.30.4 (`nvidia-nccl-cu13==2.30.4` pip wheel)
- Plugin: stock aws-ofi-nccl v1.19.1, no topology patches, no `NCCL_TOPO_FILE` override
- Workload: DeepSeek DeepEP V2 `tests/elastic/test_ep.py`. We expect any workload that exercises the same intra-node XML fusion path on this host shape to reproduce, but we have not attempted a minimal `nccl-tests` repro.

The overflow fires during early init, before any collective.

## Observation vs. inferred mechanism

**Observed:** The overflow reproduces consistently on this host shape with the stock setup above. We additionally tried supplying an identical 122-node `NCCL_TOPO_FILE` to every rank; the overflow still fires. We also tried narrowing visible EFA devices via libfabric (`FI_EFA_DEVICE_LIST`); the overflow still fires, because NCCL walks `/sys/class/pci_bus/*` independently of what libfabric exposes.

**Inferred (from reading the 2.30.4 source, not a live-debugger trace):** The non-MNNVL branch of `ncclTopoGetSystem` reuses the initial 256-slot XML buffer for the fused output rather than allocating a larger buffer (the MNNVL branch does allocate a larger buffer). This path relies on `xmlFindNode` dedup in `ncclTopoFuseXmlRecursive` to keep the merged buffer within 256. `xmlFindNode` (static inline in `src/graph/xml.h`) requires `nAttrs` match plus every attribute key/value match, and per-rank generated attrs on the `gpu`/`pci` nodes may be preventing sufficient collapse of otherwise-equivalent subtrees. We did not step through a live debugger to confirm which specific attribute difference blocks which dedup call.

## Candidate fixes

**(a) Allocate a larger destination XML buffer in the non-MNNVL intra-node fuse path** (analogous to the MNNVL path). Architecturally symmetric.

**(b) Bump `NCCL_TOPO_XML_MAX_NODES`** (the one-line `#define` change). Simpler but increases the buffer footprint for every topology-load path.

**(c) Fix the dedup** in `xmlFindNode` / `ncclTopoFuseXmlRecursive` so rank-specific attributes do not block collapse of otherwise-identical subtrees. We are not familiar enough with the invariants your dedup code relies on to recommend a specific change here.

We tested option (b) locally (`#define` 256 -> 2048) across three DeepEP-based images on the reproducer hardware: 351 combined `test_ep.py` config runs produced zero `too many XML nodes` warnings. That validates option (b) works for our workload; it does not say anything about the structural correctness of other paths in NCCL that allocate XML buffers.

## Happy to send a minimal PR

If the maintainers prefer option (a), I am happy to attempt a PR, though I recognize dynamic allocation in the fuse path may require touching the underlying `ncclXml` struct if it embeds a fixed-size array. If you prefer option (b), it is a 1-line bump. Either way I'd rather not guess which shape you'd accept without a maintainer nudge.

## Context / incident writeup

Full incident writeup with raw logs, controlled experiments, and the source-reading chain:
https://github.com/antonai-work/deepep-v2-efa-base/blob/main/docs/INCIDENT-PR1226-AWS-OFI-NCCL-XML-OVERFLOW.md

Thanks for your work on NCCL.


## 评论 (4)

### kodlan · 2026-09-04

It seems like this could be reproduced without EFA -  in ncclTopoGetSystem the intra-node fusion writes the merged topology back into the same 256 node buffer each rank used for its own XML, while the MNNVL path allocates nLocalRanks x 256 for the exact same loop. Since fusion only dedups nodes whose attributes all match and every rank's gpu node has its own rank attribute, the fused tree is the union of the per-rank trees and can go past 256. With a topology file that gives the gpu 18 nvlink children 14 ranks on one GPU hit the same "too many XML nodes (max 256)" here, 12 ranks fit.

#2386 makes the enlargement unconditional (option a above)

### dmvevents · 2026-09-04

Thanks @kodlan -- your mechanism matches the EFA-side symptoms we saw,
and the non-EFA repro makes it much stronger: it pins the overflow on
the fusion buffer sizing itself rather than anything NIC-count-specific
(our 32-NIC host was just an easy way to exceed the cap). The
`nLocalRanks x 256` sizing in the MNNVL path being adjacent to a
single-256 fusion buffer for the same loop is exactly the asymmetry we
hoped a maintainer-side look would find.

#2386 is the option (a) we offered to attempt, done properly -- happy to
drop that offer in its favor. Two datapoints that may help it along:

- Our option (b) test (a blunt 256 -> 2048 bump) ran 351 combined
  `test_ep.py` configurations on the p5.48xlarge reproducer with zero
  `too many XML nodes` warnings, so enlarging the fused buffer
  empirically cleared the overflow for this workload family (no claim
  beyond that); #2386's
  per-local-rank sizing is the principled version of the same headroom.
- When #2386 (or a successor) lands, we can re-run the original 8-rank /
  32-NIC reproducer on the same hardware shape and report back here.

### kodlan · 2026-09-05

```bash
> Thanks [@kodlan](https://github.com/kodlan) -- your mechanism matches the EFA-side symptoms we saw, and the non-EFA repro makes it much stronger: it pins the overflow on the fusion buffer sizing itself rather than anything NIC-count-specific (our 32-NIC host was just an easy way to exceed the cap). The `nLocalRanks x 256` sizing in the MNNVL path being adjacent to a single-256 fusion buffer for the same loop is exactly the asymmetry we hoped a maintainer-side look would find.
> 
> [#2386](https://github.com/NVIDIA/nccl/pull/2386) is the option (a) we offered to attempt, done properly -- happy to drop that offer in its favor. Two datapoints that may help it along:
> 
> * Our option (b) test (a blunt 256 -> 2048 bump) ran 351 combined
>   `test_ep.py` configurations on the p5.48xlarge reproducer with zero
>   `too many XML nodes` warnings, so enlarging the fused buffer
>   empirically cleared the overflow for this workload family (no claim
>   beyond that); [graph: size the fused topology XML for all local ranks #2386](https://github.com/NVIDIA/nccl/pull/2386)'s
>   per-local-rank sizing is the principled version of the same headroom.
> * When [graph: size the fused topology XML for all local ranks #2386](https://github.com/NVIDIA/nccl/pull/2386) (or a successor) lands, we can re-run the original 8-rank /
>   32-NIC reproducer on the same hardware shape and report back here.
```

Thanks. On p5 2048 bump and #2386 give the fused tree the same budget (8*256) the difference is #2386 only grows the fuser buffer and leaves the other  xml paths at 256.
A rereunof the 8rank /32 nic reproducer would be great.

### marksantesson · 2026-09-15

@dmvevents, we've pushed a version of @kodlan 's change to github's dev branch. Please check out [this sha](https://github.com/NVIDIA/nccl/commit/4ae8e52892b1362bbeda3b38a83e2f342d12a74c) and verify that it works for you.
