# [Issue #2429] Guides don't say what the cluster needs before you deploy

source: https://github.com/llm-d/llm-d/issues/2429
state: open | updated: 2026-09-17T13:29:45Z
labels: 

## 正文

Deploying the wide-ep guide from scratch on a new GKE cluster hit four failures before the first request worked, all cluster setup no doc covers.

Guides state GPU counts, but not the rest of what the cluster needs: networking objects, driver versions, controller versions, CPU node sizes. Setup docs exist (`docs/infrastructure/providers/`, `docs/infrastructure/rdma/`) but only pd-disaggregation links one.

Proposal:

1. **Required "cluster requirements" block in every guide README**: accelerator type/count, RDMA yes/no, controller versions, router CPU node sizing, provider setup doc link. Four guides already render their README from `guide.yaml` with a CI freshness check; add the block to that template and migrate the remaining guides onto it (or add the block by hand where migration isn't worth it).
2. **One preflight script in `helpers/`**, generalizing `docs/infrastructure/providers/digitalocean/verify-do-prerequisites.sh`. It checks: client tools, CRDs, LWS version, required Network objects Ready, GPU driver in a known-good range, free CPU/GPU for the guide's pods.

Also: link `docs/infrastructure/rdma/` and `multi-node.md` from guides that need them.

The four failures, for reference: missing `rdma-0..7` Network objects (pods rejected at admission), R580 driver crashing DeepEP high-throughput kernels, router pod too big for the default CPU node, decode OOM at default `--gpu-memory-utilization`.


## 评论 (2)

### alexeymoskalev-devops · 2026-09-13

Hi @BenjaminBraunDev — I'd like to take this on, in two steps.

**Step 1, preflight.** A cluster-level check that runs before anything is
deployed, generalizing the DigitalOcean script
(`docs/infrastructure/providers/digitalocean/verify-do-prerequisites.sh`):
client tools, Gateway API / GAIE / LWS CRDs present and at the versions
`guides/env.sh` expects, the guide's required `Network` objects (RDMA guides),
GPU driver within a known-good range (from GPU feature discovery node labels),
and enough schedulable CPU/GPU for the guide's pods, including a CPU node large
enough for the router. Of your four failures that covers three; decode OOM at
the default `--gpu-memory-utilization` is a runtime setting and belongs in the
requirements block instead. This is complementary to the in-pod preflight in
llm-d-pd-utils, which gates `vllm serve` after scheduling — the failures here
happen before a pod runs.

Shape: a bash script under `helpers/preflight/` that reads a new
`requirements:` block from `guide.yaml` (next to `prerequisites:`), so the
check and the README come from the same source; `scripts/guide.py` only
validates the block. Guides not yet on guide.yaml can pass the requirements
file explicitly.

**Step 2, the "cluster requirements" block** rendered into README by
`scripts/guide.py render` (already covered by `ci-guides-check`) for the four
guides on guide.yaml, and added by hand to wide-ep first, since that is where
the failures came from. Migrating the rest can be a follow-up.

I'll open step 1 as its own PR. If you'd rather sequence it differently or
have a preferred schema for the requirements block, happy to adjust.

### KashmirAwana · 2026-09-17

It sounds like there are some missing details about cluster setup requirements in the guides, especially regarding networking objects and hardware specs. I'd take a closer look at how the guides currently describe the necessary cluster configurations.

