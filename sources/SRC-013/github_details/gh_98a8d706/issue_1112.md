# [Issue #1112] Switch to consuming upstream images instead of building our own

source: https://github.com/llm-d/llm-d/issues/1112
state: open | updated: 2026-09-11T01:17:05Z
labels: enhancement, Image builds, lifecycle/stale, triage-accepted

## 正文

## Context

We currently build and maintain 5 device-specific container images (`llm-d-cuda`, `llm-d-rocm`, `llm-d-xpu`, `llm-d-cpu`, `llm-d-hpu`) plus an `llm-d-rdma-tools` diagnostic image. This involves ~6 Dockerfiles, ~15 build scripts, NVSHMEM patches, constraint files, and ~2,500 lines of CI workflows — all layering customizations on top of upstream vLLM.

The maintenance cost is significant and growing. Many of the customizations we carry (NIXL, DeepEP, FlashInfer, etc.) are being upstreamed into vLLM. We should stop building these images and consume upstream vLLM images directly.

## Scope of changes

### 1. Inventory what our images add over upstream

Before removing anything, we need a clear picture of what upstream vLLM images already include vs. what we add. Current customizations by category:

| Customization | Devices | Upstream status |
|---|---|---|
| NVSHMEM (with CoreWeave/RoCE patches) | CUDA | Not in upstream images |
| DeepEP, DeepGEMM, FlashInfer wheels | CUDA | FlashInfer in upstream; DeepEP/DeepGEMM not yet |
| GDRCopy + custom UCX | CUDA, ROCm | Not in upstream |
| llm-d-kv-cache offloading connector | CUDA, CPU | llm-d-specific, never upstream |
| NIXL / RIXL | CUDA, ROCm, CPU, HPU | Being upstreamed into vLLM |
| LMCache + InfiniStore | CUDA | Not in upstream |
| EFA (AWS Elastic Fabric Adapter) | CUDA | Not in upstream |
| OTEL tracing packages | All | Not in upstream |
| RHEL UBI9 base | CUDA | Upstream is Ubuntu only |
| Debug builds (NVSHMEM logging) | CUDA | Not in upstream |
| tcmalloc LD_PRELOAD | CPU | Not in upstream |
| Custom vllm-gaudi plugin wiring | HPU | Separate upstream image exists |

### 2. Decide on a strategy for llm-d-specific components

Components that will never be upstream (primarily the `llm-d-kv-cache` offloading connector) need an alternative delivery mechanism:

- [ ] **Option A**: Thin addon layer — a minimal `FROM vllm/vllm-openai:vX.Y` Dockerfile that only adds llm-d-specific bits
- [ ] **Option B**: Init container that pip-installs wheels at pod startup
- [ ] **Option C**: Volume-mounted plugin directory

Trade-offs: Option A still requires image builds but dramatically reduces scope. Options B/C add cold-start latency.

### 3. Track upstream inclusion of key components

Before we can drop our images, we need these to land in upstream vLLM images (or decide we can live without them):

- [ ] NIXL — track upstream vLLM inclusion
- [ ] DeepEP — track upstream vLLM inclusion
- [ ] DeepGEMM — track upstream vLLM inclusion
- [ ] NVSHMEM patches — contribute upstream or to vLLM image build
- [ ] LMCache / InfiniStore — track upstream vLLM inclusion
- [ ] OTEL tracing packages — propose as optional layer or accept runtime install

### 4. Start with XPU (zero-risk)

XPU already uses the upstream Dockerfile as-is (fetched via `make xpu-prepare`). This is the easiest starting point:

- [ ] Update XPU guide manifests to reference upstream `vllm/vllm-openai` directly
- [ ] Remove XPU-specific build logic from Makefile (`xpu-prepare` target)
- [ ] Remove XPU jobs from `build-image.yml` and `ci-release.yaml`
- [ ] Update E2E workflows (`e2e-inference-scheduling-xpu.yaml`, `e2e-pd-xpu.yaml`, `e2e-prefix-cache-xpu.yaml`)

### 5. Remove Dockerfiles and build scripts

Once upstream images cover our needs (per device):

- [ ] `docker/Dockerfile.cuda` (527 lines)
- [ ] `docker/Dockerfile.cpu` (157 lines)
- [ ] `docker/Dockerfile.rocm` (158 lines)
- [ ] `docker/Dockerfile.hpu` (84 lines)
- [ ] `docker/Dockerfile.rdma-tools` (124 lines)
- [ ] `docker/scripts/` (entire directory — 15+ build scripts)
- [ ] `docker/packages/` (constraint files, RPM caches)
- [ ] `docker/build-constraints.txt`, `docker/constraints.txt`
- [ ] `patches/` (4 NVSHMEM patches)
- [ ] `docker/common-versions`

### 6. Remove or simplify CI workflows

- [ ] `.github/workflows/build-image.yml` (~1,474 lines) — remove or reduce to addon-layer-only
- [ ] `.github/workflows/nightly-build-image.yaml` — remove
- [ ] `.github/workflows/ci-release.yaml` (~1,000+ lines) — remove image-build jobs, keep non-image release steps

### 7. Simplify the Makefile

Remove image-build targets: `image-build`, `image-push`, `image-retag`, `buildah-build`, `xpu-prepare`, and related variables/checks.

### 8. Update all image references (65 files)

All guides, deployment manifests, benchmark templates, and E2E workflows reference `ghcr.io/llm-d/llm-d-{device}:vX.Y.Z`. These need updating to point to upstream image names.

**Guides** (~30 values files):
- `guides/pd-disaggregation/ms-pd/values*.yaml`
- `guides/inference-scheduling/ms-inference-scheduling/values*.yaml`
- `guides/precise-prefix-cache-aware/ms-kv-events/values*.yaml`
- `guides/tiered-prefix-cache/cpu/manifests/`
- `guides/wide-ep-lws/manifests/`
- `guides/simulated-accelerators/`
- `guides/workload-autoscaling/`
- `guides/benchmark/`

**E2E / CI workflows** (~20 files):
- `nightly-e2e-*.yaml` workflows
- `e2e-*.yaml` workflows

**Docs**:
- `RELEASE.md`
- `docs/infra-providers/digitalocean/README.md`
- `guides/simulated-accelerators/README.md`

### 9. Validate E2E tests still pass

- [ ] Audit which E2E tests depend on packages only present in our custom images
- [ ] Update test assumptions or add runtime-install steps as needed

## Risks to track

- **RHEL/UBI base**: Upstream vLLM only provides Ubuntu. If users/partners require RHEL-based images (OpenShift), we need an alternative path.
- **Version pinning**: We currently pin exact commits of vLLM + kernel libraries together. With upstream images, we lose control over which versions ship together — need a compatibility matrix.
- **NVSHMEM patches**: These fix real infrastructure bugs (RoCE device creation on certain kernels). If not accepted upstream, P/D disaggregation breaks on affected hardware.
- **Cold-start latency**: Runtime-installed components add startup time, which matters for autoscaling.

## Suggested execution order

1. **XPU** — already upstream, zero risk
2. **HPU** — upstream `vllm-gaudi` image exists, minimal delta
3. **ROCm** — upstream `vllm-openai-rocm` exists, main delta is RIXL/UCX
4. **CPU** — small image, few customizations
5. **CUDA** — most complex, most customizations, do last

cc @llm-d/maintainers

## 评论 (2)

### Gregory-Pereira · 2026-04-20

Independent of this we need to track what we need to move upstream to vLLM. Examples include:

- EFA enabled image
- XPU enhancements
- HPU image (not sure)



### github-actions[bot] · 2026-09-11

This issue is marked as stale after 90d of inactivity. After an additional 30d of inactivity (15d to become rotten, then 15d more), it will be closed. To prevent this issue from being closed, add a comment or remove the `lifecycle/stale` label.
