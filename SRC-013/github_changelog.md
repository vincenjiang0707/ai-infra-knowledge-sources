# Changelog (aggregated from releases.body)

> releases: 11

## v0.2.0 (2025-07-29)

# 📦 llm-d v0.2.0 Release Notes

For information on installing and using the new release refer to our [quickstarts](https://github.com/llm-d-incubation/llm-d-infra/tree/main/quickstart).

**Release Date:** 2025-07-28

---

## Core Objectives

This release had a few key objectives:
- Migrate from monolithic to composable installs based on community feedback
- Support wide expert parallelism cases of "one rank per node"
- Align with upstream gateway-api-inference-extension helm charts

## 🧩 Component Summary

| Component | Version | Previous Version | Type |
|-----------|---------|------------------| ---- |
| llmd/llm-d-inference-scheduler | `v0.2.1` | `0.0.4` | Image |
| llm-d/llm-d-model-service | NA (Deprecated) | `0.0.10` | Image |
| llm-d-incubation/llm-d-modelservice | `v0.2.0` | NA (New) | Helm Chart |
| llm-d/llm-d-routing-sidecar | `v0.2.0` | `0.0.6` | Image |
| llm-d/llm-d-deployer | NA (Deprecated) | `1.0.22` | Helm Chart |
| vllm-project/vllm | `v0.10.0` | NA (built from fork) | Wheel installed in `llm-d` |
| llm-d/llm-d | `v0.2.0` | `0.0.8` | Image |
| llm-d/llm-d-inference-sim| `v0.3.0` | `0.0.4`| Image |
| llm-d-incubation/llm-d-infra | `v1.1.1` | NA (New) | Helm Chart |
| kubernetes-sig/gateway-api-inference-extension | `v0.5.1` | NA (New - external) | Image |
| llm-d/llm-d-kv-cache-manager | `v0.2.0` | `v0.1.0` | Go Package (consumed in `inference-scheduler`) |
| llm-d/llm-d-benchmark | `v0.2.0` | `v0.0.8` | Tooling and Image |

NOTE: In future we want to support compatibility matrixes. However as we are still getting off the ground, we cannot ensure that these components work with legacy versions.

---

## 🔹 llm-d/llm-d-inference-scheduler

- **Description**: The inference scheduler makes optimized routing decisions for inference requests to vLLM model servers.  This component depends on the upstream gateway-api-inference-extension scheduling framework and includes features specific to vLLM. 
- **Diff**: [0.0.4 → v0.2.1](https://github.com/llm-d/llm-d-inference-scheduler/compare/0.0.4...v0.2.1)
- **Upstream Changelog** - since we bumped the upstream version of GIE many changes do not show up in the diff. The following has been pulled from release notes:

---

## 🔹 llm-d/llm-d-model-service (Deprecated)

- **Description**: `ModelService` is a Kubernetes operator (CRD + controller) that enables the creation of vllm pods and routing resources for a given model.
- **Status**: This repo is being deprecated as a component of `llm-d` and has been archived.
- **Replacement**: [`lm-d-incubation/llm-d-modelservice`](https://github.com/llm-d-incubation/llm-d-modelservice)

---

## 🔹 llm-d-incubation/llm-d-modelservice (New)

- **Description**: `modelservice` is a Helm chart that simplifies LLM deployment on llm-d by declaratively managing Kubernetes resources for serving base models. It enables reproducible, scalable, and tunable model deployments through modular presets, and clean integration with llm-d ecosystem components (including vLLM, Gateway API Inference Extension, LeaderWorkerSet).
- **History** (new): [v0.2.0](https://github.com/llm-d-incubation/llm-d-modelservice/commits/llm-d-modelservice-v0.2.0/)

---

## 🔹 llm-d/llm-d-routing-sidecar

- **Description**: A reverse proxy routing traffic between the `inference-scheduler` and the prefill and decode workers based on the x-prefiller-host-port HTTP request header.
- **Diff**: [0.0.6 → v0.2.0](https://github.com/llm-d/llm-d-routing-sidecar/compare/0.0.6...v0.2.0)

---

## 🔹 llm-d/llm-d-deployer (Deprecated)

- **Description**: A repo containing examples, Helm charts, and release assets for `llm-d`.
- **Status**: This repo is being deprecated as a component of `llm-d` however the repo will not be archived so that it may support people who want to try the legacy install. Will be minimally maintained.
- **Replacement**: [`llm-d-incubation/llm-d-infra`](https://github.com/llm-d-incubation/llm-d-infra)

---

## 🔹 vllm-project/vllm (Upstream)

- **Description**: `vLLM` is a fast and easy-to-use library for LLM inference and serving. This project is the inferencing engine that forms the upstream of our `llm-d/llm-d` image.
- **Release**: [v0.10.0](https://github.com/vllm-project/vllm/releases/tag/v0.10.0)

---

## 🔹 llm-d/llm-d

- **Description**: A midstreamed image of `vllm-project/vllm` for inferencing, supporting features such as PD disaggregation, KV cache awareness and more.
- **Diff**: [0.0.8 → v0.2.0](https://github.com/llm-d/llm-d/compare/0.0.8...v0.2.0)

---

## 🔹 llm-d/llm-d-inference-sim

- **Description**: a light weight vLLM simulator emulates responses to the HTTP REST endpoints of vLLM.
- **Diff**: [0.0.4 → v0.3.0](https://github.com/llm-d/llm-d-inference-sim/compare/0.0.4...v0.3.0)

---

## 🔹 llm-d-incubation/llm-d-infra (New)

- **Description**: This repository includes examples, Helm charts, and release assets for llm-d-infra.
- **History** (new): [v1.1.1](https://github.com/llm-d-incubation/llm-d-infra/commits/v1.1.1/)

---

## 🔹 kubernetes-sig/gateway-api-inference-extension (New - Upstream)

- **Note**: Note: The upstream project is a dependency of llm-d and we directly reference the published Helm charts.  The release notes will not include all changes in this component from release to release, please consult with the upstream release pages.
- **Description**: A Helm chart to deploy an InferencePool, a corresponding EndpointPicker (epp) deployment, and any other related assets.
- **History** (new - external): [v0.5.1](https://github.com/kubernetes-sigs/gateway-api-inference-extension/commits/v0.5.1)

---

## 🔹 llm-d/llm-d-kv-cache-manager

- **Description**: This repository contains the llm-d-kv-cache-manager, a pluggable service designed to enable KV-Cache Aware Routing and lay the foundation for advanced, cross-node cache coordination in vLLM-based serving platforms.
- **Diff**: [v0.1.0 → v0.2.0](https://github.com/llm-d/llm-d-kv-cache-manager/compare/v0.1.0...v0.2.0)

---

## 🔹 llm-d/llm-d-benchmark

- **Description**: This repository provides an automated workflow for benchmarking LLM inference using the llm-d stack. It includes tools for deployment, experiment execution, data collection, and teardown across multiple environments and deployment styles.
- **Diff**: [v0.0.8 → v0.2.0](https://github.com/llm-d/llm-d-benchmark/compare/v0.0.8...v0.2.0)

---

For more information on any of the component project or versions, please checkout their repos directly. Thank you to all contributors who helped make this happen.

## v0.3.0 (2025-10-10)

# 📦 llm-d v0.3.0 Release Notes

This release of the `llm-d` repo will capture the release for the entirety of the project, guides, components, and all. 

**Release Date:** 2025-10-10

---

## Core Objectives

This release had a few key objectives:
- Increase support for specialized hardware backends (TPU, XPU)
- Increase cloud provider support (DOKS)
- Establish a metrics and observability story
- Wide-ep optimizations (EPLB, DBO, Async Scheduling, etc.)

## 🧩 Component Summary

| Component | Version | Previous Version | Type |
|-----------|---------|------------------| ---- |
| llm-d/llm-d-inference-scheduler | `v0.3.2` | `v0.2.1` | Image |
| llm-d-incubation/llm-d-modelservice | `v0.2.10` |`v0.2.0` | Helm Chart |
| llm-d/llm-d-routing-sidecar | `v0.3.0` | `v0.2.0` | Image |
| vllm-project/vllm | `v0.11.0` | `v0.10.0` | Editable install based on precompiled wheel |
| llm-d/llm-d-cuda | `v0.3.0` | `v0.2.0` | Image |
| llm-d/llm-d-gke | `v0.3.0` | NA (new) | Image |
| llm-d/llm-d-aws | `v0.3.0` | NA (new) | Image |
| llm-d/llm-d-xpu | `v0.3.0` | NA (new) | Image |
| llm-d/llm-d-inference-sim | `v0.5.1` | `v0.3.0`| Image |
| llm-d-incubation/llm-d-infra | `v1.3.3` | `v1.1.1` | Helm Chart |
| kubernetes-sig/gateway-api-inference-extension | `v1.0.1` | `v0.5.1` | Helm Chart |
| llm-d/llm-d-kv-cache-manager | `v0.3.2` | `v0.2.0` | Go Package (consumed in `inference-scheduler`) |
| llm-d/llm-d-benchmark | `v0.3.0` | `v0.2.0` | Tooling and Image |

NOTE: In future we want to support compatibility matrixes. However as we are still getting off the ground, we cannot ensure that these components work with legacy versions.

---

## 🔹 llm-d/llm-d-inference-scheduler

- **Description**: This scheduler that makes optimized routing decisions for inference requests to the llm-d inference framework.
- **Diff**: [v0.2.1 → v0.3.2 ](https://github.com/llm-d/llm-d-inference-scheduler/compare/v0.2.1...v0.3.2)

---

## 🔹 llm-d-incubation/llm-d-modelservice

- **Description**: `modelservice` is a Helm chart that simplifies LLM deployment on llm-d by declaratively managing Kubernetes resources for serving base models. It enables reproducible, scalable, and tunable model deployments through modular presets, and clean integration with llm-d ecosystem components (including vLLM, Gateway API Inference Extension, LeaderWorkerSet).
- **Diff**: [v0.2.0 → v0.2.10 ](https://github.com/llm-d-incubation/llm-d-modelservice/compare/llm-d-modelservice-v0.2.0...llm-d-modelservice-v0.2.10)

---

## 🔹 llm-d/llm-d-routing-sidecar

- **Description**: A reverse proxy redirecting incoming requests to the prefill worker specified in the x-prefiller-host-port HTTP request header.
- **Diff**: [v0.2.0 → v0.3.0](https://github.com/llm-d/llm-d-routing-sidecar/compare/v0.2.0...v0.3.0)

---

## 🔹 vllm-project/vllm (upstream)

- **Description**: `vLLM` is a fast and easy-to-use library for LLM inference and serving. This project is the inferencing engine that forms the upstream of our `llm-d/llm-d` image.
- **Diff**: [v0.10.0 → v0.11.0](https://github.com/vllm-project/vllm/compare/v0.10.0...v0.11.0)

---

## 🔹 llm-d/llm-d

- **Description**: A midstreamed image of `vllm-project/vllm` for inferencing, supporting features such as PD disaggregation, KV cache awareness and more.
- **Diff**: [v0.2.0 → v0.3.0](https://github.com/llm-d/llm-d/compare/v0.2.0...v0.3.0)
- **Image Variants**: Different image variants of this component:
    - XPU: `ghcr.io/llm-d/llm-d-xpu:v0.3.0`
    - AWS: `ghcr.io/llm-d/llm-d-aws:v0.3.0`
        - Release `v0.3.0` workaround for getting EFA to work
    - CUDA: `ghcr.io/llm-d/llm-d-cuda:v0.3.0`
    - GKE: `ghcr.io/llm-d/llm-d-gke:v0.3.0`
        - Release `v0.3.0` workaround for running wide-ep on GKE with H200s

---

## 🔹 llm-d/llm-d-inference-sim

- **Description**: A light weight vLLM simulator emulates responses to the HTTP REST endpoints of vLLM.
- **Diff**: [v0.3.0 → v0.5.1](https://github.com/llm-d/llm-d-inference-sim/compare/v0.3.0...v0.5.1)

---

## 🔹 llm-d-incubation/llm-d-infra

- **Description**: A helm chart for deploying gateway and gateway related infrastructure assets for llm-d.
- **Diff**: [v1.1.1 → v1.3.3](https://github.com/llm-d-incubation/llm-d-infra/compare/v1.1.1...v1.3.3)

---

## 🔹 kubernetes-sig/gateway-api-inference-extension

- **Description**: A Helm chart to deploy an InferencePool, a corresponding EndpointPicker (epp) deployment, and any other related assets.
- **Diff**: [v0.5.1 → v1.0.1](https://github.com/kubernetes-sigs/gateway-api-inference-extension/compare/v0.5.1...v1.0.1)

---

## 🔹 llm-d/llm-d-kv-cache-manager

- **Description**: This repository contains the llm-d-kv-cache-manager, a pluggable service designed to enable KV-Cache Aware Routing and lay the foundation for advanced, cross-node cache coordination in vLLM-based serving platforms.
- **Diff**: [v0.2.0 → v0.3.0](https://github.com/llm-d/llm-d-kv-cache-manager/compare/v0.2.0...v0.3.0)

---

## 🔹 llm-d/llm-d-benchmark

- **Description**: This repository provides an automated workflow for benchmarking LLM inference using the llm-d stack. It includes tools for deployment, experiment execution, data collection, and teardown across multiple environments and deployment styles.
- **Diff**: [v0.2.0 → v0.3.0](https://github.com/llm-d/llm-d-benchmark/compare/v0.2.0...v0.3.0)

---

For more information on any of the component project or versions, please checkout their repos directly. For information on installing and using the new release refer to our [guides](https://github.com/llm-d/llm-d/blob/v0.3.0/guides). Thank you to all contributors who helped make this happen.


## v0.3.1 (2025-11-06)

# Release overview

This release was focused on following up on our objectives from the v0.3.0 that could not make it into that release. A few key stories to highlight:

- ARM support
- Refactor image build process to scripts
- Unifying the GKE image into our core Cuda image
- Adding AKS cloud provider support

Welcome to all our new contributors, and thanks to the team for their hard work.

## Component version bumps:

- Inference SIM ([`v0.5.1` --> `v0.6.1`](https://github.com/llm-d/llm-d-inference-sim/compare/v0.5.1...v0.6.1))
- llm-d image (`v0.3.0` --> `v0.3.1`, diff encapsulated in change-log below)

## What's Changed
* [bugfix] changing filename to not reference old plugin by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/353
* Deprecate all InferenceModel in XPU guides by @yankay in https://github.com/llm-d/llm-d/pull/358
* version bump on vllm release v0.11.0 tag move by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/365
* Update SIGS.md owners by @petecheslock in https://github.com/llm-d/llm-d/pull/363
* Clear /dev/shm before process startup to prevent crashloops by @smarterclayton in https://github.com/llm-d/llm-d/pull/364
* Add hardware and platform support issue template by @Ayobami-00 in https://github.com/llm-d/llm-d/pull/359
* minor typo in the inference guide by @effi-ofer in https://github.com/llm-d/llm-d/pull/377
* docs: introduce AKS as a well-lit infra provider by @chewong in https://github.com/llm-d/llm-d/pull/335
* Correct # of measured output tokens / s by @smarterclayton in https://github.com/llm-d/llm-d/pull/350
* refactor dockerfiles to a set bash scripts by @wseaton in https://github.com/llm-d/llm-d/pull/324
* Add wide ep gke test by @rlakhtakia in https://github.com/llm-d/llm-d/pull/367
* Intel pd workflow + v0.3 lagging updates by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/310
* Use the vLLM image for xpu by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/357
* Fix markdown-link-checker failed issue by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/385
* feat: Add updated readiness probe for vLLM containers by @rajinator in https://github.com/llm-d/llm-d/pull/330
* Fix queries and load script in monitoring by @Hritik003 in https://github.com/llm-d/llm-d/pull/383
* Arm cuda support (from clean branch) by @wseaton in https://github.com/llm-d/llm-d/pull/382
* Fix deadlink error in markdown-link-check by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/404
* Update bug report template by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/413
* Fix release image tagging by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/379
* Update monitoring install for CKS by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/375
* Patch nvshmem to avoid an uninitialized value passed to RoCE by @smarterclayton in https://github.com/llm-d/llm-d/pull/407
* [Docs] Fix InferencePool version number getting cut off in WideEP guide by @tlrmchlsmth in https://github.com/llm-d/llm-d/pull/414
* Fix broken monitoring dashboard link by @smarterclayton in https://github.com/llm-d/llm-d/pull/422
* Set correct variables for built NVSHMEM by @smarterclayton in https://github.com/llm-d/llm-d/pull/417
* Update DeepEP to a version with a patch for setting NVSHMEM HCA mappings to CUDA device by @smarterclayton in https://github.com/llm-d/llm-d/pull/397
* swap release to tag creation image tagging by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/423
* pr vs release tag by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/424
* enable cache busting by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/425
* release.tag_name does not exist for a tag not part of a release by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/427
* unify darwin/arm64 with other platforms when install helmfile in install-deps.sh by @yitingdc in https://github.com/llm-d/llm-d/pull/267
* Set LD_LIBRARY_PATH for nvshmem appropriately by @smarterclayton in https://github.com/llm-d/llm-d/pull/429
* Update GKE to align to UBI images by @smarterclayton in https://github.com/llm-d/llm-d/pull/415
* updating to tags for v0.3.1 release by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/432
* bugfixing by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/433

## New Contributors
* @yankay made their first contribution in https://github.com/llm-d/llm-d/pull/358
* @Ayobami-00 made their first contribution in https://github.com/llm-d/llm-d/pull/359
* @effi-ofer made their first contribution in https://github.com/llm-d/llm-d/pull/377
* @chewong made their first contribution in https://github.com/llm-d/llm-d/pull/335
* @rlakhtakia made their first contribution in https://github.com/llm-d/llm-d/pull/367
* @rajinator made their first contribution in https://github.com/llm-d/llm-d/pull/330
* @Hritik003 made their first contribution in https://github.com/llm-d/llm-d/pull/383
* @yitingdc made their first contribution in https://github.com/llm-d/llm-d/pull/267

**Full Changelog**: https://github.com/llm-d/llm-d/compare/v0.3.0...v0.3.1

## v0.5.0 (2026-02-04)

# 📦 llm-d v0.5.0 Release Notes  

This release of the `llm-d` repo will capture the release for the entirety of the project, guides, and components.

**Release Date:** 2026-02-03

---

## Core Objectives

- Reproducible benchmarking
- Scaling KV-cache
- Autoscaling improvements
- Greater Metrics + tracing story

## 🏗️ Infrastructure Changes - BREAKING CHANGES

| Component | Version | Previous Version |
|-----------|---------|------------------|
| Gateway API | `v1.4.0` | `v1.3.0` |
| Istio | `1.28.1` | `1.28-alpha.89f30b26ba71bf5e538083a4720d0bc2d8c06401` |
| KGateway | `v2.1.1` | `v2.0.3` |
| GKE Gateways | NA - tied to GKE | NA - tied to GKE |

**NOTE:** We upgraded to the following versions to consume the new v1 Inference Pool API. This means cluster admins should descale their workloads and upgrade these Infrastructure level components before proceeding. You should be able to use the old `inference.networking.x-k8s.io/v1alpha2` API, however the guides will require changes to make them work - use this at your own risk.

## 🧩 LLM-D Component Summary

| Component | Version | Previous Version | Type |
|-----------|---------|------------------| ---- |
| llm-d/llm-d-inference-scheduler | `v0.5.0` | `v0.4.0-rc1` | Image |
| llm-d/llm-d-kv-cache | `v0.5.0` | `v0.4.0` | Library |
| llm-d-incubation/llm-d-modelservice | `v0.4.5` |`v0.3.8` | Helm Chart |
| llm-d/llm-d-routing-sidecar | `v0.5.0` | `v0.4.0-rc1` | Image |
| llm-d/llm-d-inference-sim | `v0.7.1` | `v0.6.1` | Image |
| llm-d/llm-d-cuda | `v0.5.0` | `v0.4.0` | Image |
| llm-d/llm-d-aws | Deprecated | `v0.4.0` | Image |
| llm-d/llm-d-xpu | `v0.5.0` | `v0.4.0` | Image |
| llm-d/llm-d-cpu | `v0.5.0` | `v0.4.0` | Image (New) |
| vllm-project/vllm | `v0.14.1` | `v0.11.2` + additional cherry-picks (built from fork) | Wheel installed in `llm-d` |
| llm-d-incubation/llm-d-infra | `v1.3.6` | `v1.3.4` | Helm Chart |
| kubernetes-sig/gateway-api-inference-extension | `v1.3.0` | `v1.2.0-rc1` | Helm Chart |
| llm-d/llm-d-workload-variant-autoscaler | `v0.5.0` | `v0.0.8` | Helm Chart + Image |

### Deprecations and changes

**Temporary Deprecation**: EFA

We ran into a bug 2 days before release, between EFA and and our regular path. This was that the base image install version of libiverbs / rdma core is different than the version being packaged by EFA. Having both these versions causes nvshmem initialization errors for anything over RDMA. As a temporary measure we have dissabled EFA while we figure out a proper way to deine who owns the core RDMA core user space packages.

**WVA promotion**:

Our [Workload-Variant-Autoscaler](https://github.com/llm-d-incubation/workload-variant-autoscaler) has graduated from a experimental to core component of llm-d! Congratulations to the SIG team!

### Migrations

The `llm-d/llm-d-routing-sidecar` image has been moved under the `llm-d/llm-d-inference-scheduler` repo, and its previous one **archieved**.

### 🧩 CUDA Image Specific Component Summary 

| Component | Version | Previous Version |
|-----------|---------|------------------|
| LMCache | `v0.3.13` | `v0.3.8` |
| UCX | `v1.20.0` | `v1.19.0` |
| NVSHMEM | `v3.4.5-0` (git) | `v3.3.20` (developer source distribution) |
| NIXL | `v0.9.0` | `v0.6.0` |
| GDR Copy | `v2.5.1` | Commit `0f7366e` (maps to v2.5.1, no change) |
| Infinistore | `v0.2.33` | NA (New) | 
| EFA installer (Temporary deprecation) | `v1.46.0` | `v1.43.3` |
| Flashinfer | `v0.5.3` | `v0.5.2` |
| DEEPGEMM | `v0.5.3` | `v0.5.2` |
| DEEPEP | `v0.5.3` | `v0.5.2` |
| PPLX | `v0.5.3` | `v0.5.2` |

### RC Images in v0.4.0 release 🤦🏼 

Due to some unfortunate circumstances last release, we shipped the official release with many code compelete RC images. We plan to have better release hygeine going forward.

## Meta changes

- Change the default NIXL port to 5600 to be consistent with vLLM v0.11.1 +
- Adopt the new v1 inferencepool API
- Remove routing sidecar from non-pd deployments as its not necesary
    - in those cases adjust decode port 8200 back to default 8000 port as it no longer needs to be proxied
- More accurate labels for model and accelerator type on inference servers
- And many more! Please see each component's diff / changelog for a more complete understanding of the changes across the project.

---

## 🔹 llm-d/llm-d-inference-scheduler

- **Description**: The scheduler that makes optimized routing decisions for inference requests to the llm-d inference framework.
- **Diff**: [v0.4.0-rc1 → v0.5.0](https://github.com/llm-d/llm-d-inference-scheduler/compare/v0.4.0-rc1...v0.5.0)

---


## 🔹 llm-d/llm-d-kv-cache

- **Description**: The libraries for tokenization, KV-events processing, and KV-cache indexing and offloading.
- **Diff**: [v0.4.0 → v0.5.0](https://github.com/llm-d/llm-d-kv-cache/compare/v0.4.0...v0.5.0)

---

## 🔹 llm-d-incubation/llm-d-modelservice

- **Description**: `modelservice` is a Helm chart that simplifies LLM deployment on llm-d by declaratively managing Kubernetes resources for serving base models. It enables reproducible, scalable, and tunable model deployments through modular presets, and clean integration with llm-d ecosystem components (including vLLM, Gateway API Inference Extension, LeaderWorkerSet).
- **Diff**: [v0.3.8 → v0.4.5](https://github.com/llm-d-incubation/llm-d-modelservice/compare/llm-d-modelservice-v0.3.8...llm-d-modelservice-v0.4.5)

---

## 🔹 llm-d/llm-d-routing-sidecar

- **Description**: A reverse proxy redirecting incoming requests to the prefill worker specified in the x-prefiller-host-port HTTP request header.
- **Diff**: [v0.4.0-rc.1 → v0.5.0]
    - Note, no compare link can be provided because **this component was moved under the inference-scheduler repo**.

---

## 🔹 llm-d/llm-d-inference-sim

- **Description**: A light-weight inference simulator.
- **Diff**: [v0.6.1 → v0.7.1](https://github.com/llm-d/llm-d-inference-sim/compare/v0.6.0...v0.7.1)

---

## 🔹 llm-d/llm-d

Note: in the `v0.4.0` release the guides were not as updated as we would have liked. Because of this we built a v0.4.0 image but we used the v0.3.1 image in the guides.

- **Description**: A midstreamed image of `vllm-project/vllm` for inferencing, supporting features such as PD disaggregation, KV cache awareness and more.
- **Diff**: [v0.4.0 → v0.5.0](https://github.com/llm-d/llm-d/compare/v0.4.0...v0.5.0)
- **Image Variants**: Different image variants of this component:
    - XPU: `ghcr.io/llm-d/llm-d-xpu:v0.5.0`
    - AWS: Deprecated
    - CUDA: `ghcr.io/llm-d/llm-d-cuda:v0.5.0`
    - CPU: `ghcr.io/llm-d/llm-d-cpu:v0.5.0`

---

## 🔹 vllm-project/vllm

Note: last release we built our inferencing images off of the [nerual magic fork of vLLM](https://github.com/neuralmagic/vllm/tree/llm-d-release-0.4). This was built off of vLLM `v0.11.2` with additional cherry-picks for feature work that did not make it in on time.

As vLLM has an extreemly high contribution velocity, rather than listing a Diff it makes more sense to refer to the release notes for the releases that happened in between directly:
- [Release v0.12.0](https://github.com/vllm-project/vllm/releases/tag/v0.12.0)
- [Release v0.13.0](https://github.com/vllm-project/vllm/releases/tag/v0.13.0)
- [Release v0.14.0](https://github.com/vllm-project/vllm/releases/tag/v0.14.0)
- [Release v0.14.1](https://github.com/vllm-project/vllm/releases/tag/v0.14.1)

---

## 🔹 llm-d-incubation/llm-d-infra

- **Description**: A helm chart for deploying gateway and gateway related infrastructure assets for llm-d.
- **Diff**: [v1.3.4 → v1.3.6](https://github.com/llm-d-incubation/llm-d-infra/compare/v1.3.4...v1.3.6)

---

## 🔹 kubernetes-sig/gateway-api-inference-extension

- **Description**: A Helm chart to deploy an InferencePool, a corresponding EndpointPicker (epp) deployment, and any other related assets.
- **Diff**: [v1.2.0-rc1 → v1.3.0](https://github.com/kubernetes-sigs/gateway-api-inference-extension/compare/v1.2.0-rc1...v1.3.0)

---

## 🔹 llm-d/llm-d-workload-variant-autoscaler (New - Experimental)

- **Description**: [TODO: Add description of the workload variant autoscaler]
- **Diff**: [v0.0.8 → v0.5.0](https://github.com/llm-d-incubation/workload-variant-autoscaler/compare/v0.0.8...v0.5.0)
- **NOTE**: This component was previously experimental, but it has graduated to a core component of LLM-D. We hoped to move it from the `llm-d-incubation` org to the `llm-d` main org for this release but did not have time - stay tuned for this in the next release.

---

For more information on any of the component project or versions, please checkout their repos directly. For information on installing and using the new release refer to our [guides](https://github.com/llm-d/llm-d/blob/v0.5.0/guides). Thank you to all contributors who helped make this happen.


## In repo change-log - inference image and guides only

* docs: added standalone EPP without gateway api guide by @capri-xiyue in https://github.com/llm-d/llm-d/pull/508
* refactor wideep to use recipes folder. by @zetxqx in https://github.com/llm-d/llm-d/pull/455
* Fix dead link by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/510
* Add tiered prefix cache to the top level guide by @liu-cong in https://github.com/llm-d/llm-d/pull/516
* Update the correct vllm kv cache utilization metric name in inference scheduler by @liu-cong in https://github.com/llm-d/llm-d/pull/509
* fix: EPP configuration issues in precise-prefix-cache-aware guide by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/512
* Add tiered prefix cache to GKE doc by @liu-cong in https://github.com/llm-d/llm-d/pull/523
* Update TPU and XPU supported well-lit paths by @liu-cong in https://github.com/llm-d/llm-d/pull/524
* Link to the 0.4 release blog by @smarterclayton in https://github.com/llm-d/llm-d/pull/525
* Update wide-ep example to 0.4.0 image and tune startup threshold by @smarterclayton in https://github.com/llm-d/llm-d/pull/529
* update epp metrics auth to align with upstream changes by @sallyom in https://github.com/llm-d/llm-d/pull/528
* add prow gitaction by @Jooho in https://github.com/llm-d/llm-d/pull/530
* Add known issues and instructions to install from different branches by @liu-cong in https://github.com/llm-d/llm-d/pull/536
* Update WVA guide to v0.4.1 with semver range support by @mamy-CS in https://github.com/llm-d/llm-d/pull/533
* EFA support rebased by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/391
* Update README.md by @smarterclayton in https://github.com/llm-d/llm-d/pull/539
* Replace old reference to three well lit paths by @seanhorgan in https://github.com/llm-d/llm-d/pull/543
* Rename the llm-d-kv-cache-manager project in the docs by @petecheslock in https://github.com/llm-d/llm-d/pull/540
* Update Istio in guide to 1.28.1 GA by @shmuelk in https://github.com/llm-d/llm-d/pull/513
* support for agentGateway by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/479
* Update the XPU PD docs. by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/511
* [docs] Improve accelerator documentation by @poussa in https://github.com/llm-d/llm-d/pull/515
* chore: update inferencepool chart to v1.2.1 for GA API support by @clubanderson in https://github.com/llm-d/llm-d/pull/579
* Update Grafana dashboards to use current vLLM v1 metrics by @sallyom in https://github.com/llm-d/llm-d/pull/546
* Set the OffloadingConnector as default in the web UI docs by @petecheslock in https://github.com/llm-d/llm-d/pull/582
* docs: add link to KServe llm-d integration by @terrytangyuan in https://github.com/llm-d/llm-d/pull/560
* Resolve Grafana deployment failure and enable automatic dashboard loading by @petecheslock in https://github.com/llm-d/llm-d/pull/557
* Fix broken link in workload-autoscaling README by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/583
* chore: pre-commint/lint and github workflow for build by @zdtsw in https://github.com/llm-d/llm-d/pull/568
* chore: add CLAUDE.md to .gitignore by @nathan-weinberg in https://github.com/llm-d/llm-d/pull/576
* Simple benchmarking guide, towards benchmarking well-lit paths by @deanlorenz in https://github.com/llm-d/llm-d/pull/559
* Lagging v0.4 updates by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/548
* fix(GHA): ignore lint for markdown file with line number + build for XPU and CPU with "docker/build-push-action" by @zdtsw in https://github.com/llm-d/llm-d/pull/612
* Fix the XPU CI workflow failed and update the XPU vLLM image by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/592
* Fixing wide ep decode port name by @Edwinhr716 in https://github.com/llm-d/llm-d/pull/613
* explain how to test libfabric plugin locally by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/618
* update vllm to v0.13; swap to upstream vllm by @wseaton in https://github.com/llm-d/llm-d/pull/558
* fix: DestinationRule creation from Helm for wideEP by @zdtsw in https://github.com/llm-d/llm-d/pull/616
* Updating inference-scheduling path to use TPU7x by @Edwinhr716 in https://github.com/llm-d/llm-d/pull/584
* Update GKE Wide EP test to fix persistent failures by @rlakhtakia in https://github.com/llm-d/llm-d/pull/571
* build(efa): uplift version from 1.43.3 to 1.46.0 by @zdtsw in https://github.com/llm-d/llm-d/pull/607
* build(cpu): optimize docker build by @zdtsw in https://github.com/llm-d/llm-d/pull/611
* [XPU] Update P/D config to use DRA by @poussa in https://github.com/llm-d/llm-d/pull/518
* modified procedure to delete gateway by @ryojsb in https://github.com/llm-d/llm-d/pull/556
* Fix missing environment variable documentation in build scripts by @yurekami in https://github.com/llm-d/llm-d/pull/564
* Update intellegent inference scheduling well lit path and values.yaml by @BenjaminBraunDev in https://github.com/llm-d/llm-d/pull/619
* docs: Make getting started commands more copy/paste friendly by @russellb in https://github.com/llm-d/llm-d/pull/440
* Simplify Intel Gaudi DRA config for inference-scheduling by @poussa in https://github.com/llm-d/llm-d/pull/514
* docs: Update docs to reflect current gateway service type default by @russellb in https://github.com/llm-d/llm-d/pull/447
* Refactor: Improve dependency installation script by @ErikJiang in https://github.com/llm-d/llm-d/pull/348
* build: remove "aws" from official release process by @zdtsw in https://github.com/llm-d/llm-d/pull/635
* install OTel packages in all images by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/630
* Updating guide docs to fix typo on chart variable name by @pulasthi in https://github.com/llm-d/llm-d/pull/587
* WVA release update v0.5 by @mamy-CS in https://github.com/llm-d/llm-d/pull/622
* update to use registry.k8s.io to install inferencePool charts by @zetxqx in https://github.com/llm-d/llm-d/pull/627
* Benchmarking for Inference-scheduling well lit path by @deanlorenz in https://github.com/llm-d/llm-d/pull/638
* Add support to install wva only by @mamy-CS in https://github.com/llm-d/llm-d/pull/532
* Add the XPU precise-prefix-cache-aware example by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/402
* Fix the deadlink by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/643
* docs: Clarify WideEP network requirements by @dagrayvid in https://github.com/llm-d/llm-d/pull/639
* Enable disaggregated tokenization option in precise prefix cache aware by @delavet in https://github.com/llm-d/llm-d/pull/624
* Benchmarking of precise well-lit path by @dmitripikus in https://github.com/llm-d/llm-d/pull/652
* fix[lint]: various kinds of lint error+warning by @zdtsw in https://github.com/llm-d/llm-d/pull/645
* Update build-nvshmem.sh by @elvircrn in https://github.com/llm-d/llm-d/pull/653
* enforce cache busters by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/654
* call cache buster from saved arg instead of bash function by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/657
* Revert "Update build-nvshmem.sh (#653)" by @elvircrn in https://github.com/llm-d/llm-d/pull/660
* [Bugfix] Fix patches by @tlrmchlsmth in https://github.com/llm-d/llm-d/pull/655
* Add .DS_store to .gitignore by @tlrmchlsmth in https://github.com/llm-d/llm-d/pull/667
* fix: port for NIXL should be updated to 5600 by @zdtsw in https://github.com/llm-d/llm-d/pull/668
* Add manifests for KV cache offloading with Lustre instance as local disk by @Sneha-at in https://github.com/llm-d/llm-d/pull/631
* Fix LMCache non crashing build failure by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/662
* PD disaggregation guide fix: add missing VLLM_NIXL_SIDE_CHANNEL_HOST env var by @ycjiang50 in https://github.com/llm-d/llm-d/pull/650
* fixing KV transfer ports and relevant env vars in PD by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/670
* Add pd benchmark section. by @zetxqx in https://github.com/llm-d/llm-d/pull/672
* feat: enable memory-backed /dev/shm for vLLM cpu tensor parallelism by @vinayK34 in https://github.com/llm-d/llm-d/pull/673
* Option of using fewer GPUs in 'inference-scheduling' and 'precise' well-lit paths by @dmitripikus in https://github.com/llm-d/llm-d/pull/677
* [infra] add Python output suppression flag for vLLM installation by @amito in https://github.com/llm-d/llm-d/pull/572
* Add wide wp benchmark results on B200 by @liu-cong in https://github.com/llm-d/llm-d/pull/665
* temporarily disable EFA by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/675
* [docs]: Add shared storage guide using llm-d FS backend by @kfirtoledo in https://github.com/llm-d/llm-d/pull/609
* Release v0.5.0 prep by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/617
* Fix XPU pd and inference-scheduling failed issue by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/604
* fix: fixed monitoring session by @capri-xiyue in https://github.com/llm-d/llm-d/pull/686
* swapping to new tags + misc guide cleanup by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/687
* Bugfixing release workflow for v0.5 by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/689
* add KVEvents discovery deployment option for precise path by @vMaroon in https://github.com/llm-d/llm-d/pull/690
* more workflow updates and robustness on env vars by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/691
* needs manifest aggregation logic to releas workflows by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/693
* push runtime image and add latest tag by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/694
* try known good commit of deepep by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/692
* adding setuptools and setuptools-scm for LMCache version metadata by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/695

## New Contributors
* @capri-xiyue made their first contribution in https://github.com/llm-d/llm-d/pull/508
* @Jooho made their first contribution in https://github.com/llm-d/llm-d/pull/530
* @seanhorgan made their first contribution in https://github.com/llm-d/llm-d/pull/543
* @shmuelk made their first contribution in https://github.com/llm-d/llm-d/pull/513
* @zdtsw made their first contribution in https://github.com/llm-d/llm-d/pull/568
* @nathan-weinberg made their first contribution in https://github.com/llm-d/llm-d/pull/576
* @deanlorenz made their first contribution in https://github.com/llm-d/llm-d/pull/559
* @Edwinhr716 made their first contribution in https://github.com/llm-d/llm-d/pull/613
* @ryojsb made their first contribution in https://github.com/llm-d/llm-d/pull/556
* @yurekami made their first contribution in https://github.com/llm-d/llm-d/pull/564
* @BenjaminBraunDev made their first contribution in https://github.com/llm-d/llm-d/pull/619
* @ErikJiang made their first contribution in https://github.com/llm-d/llm-d/pull/348
* @pulasthi made their first contribution in https://github.com/llm-d/llm-d/pull/587
* @dagrayvid made their first contribution in https://github.com/llm-d/llm-d/pull/639
* @delavet made their first contribution in https://github.com/llm-d/llm-d/pull/624
* @dmitripikus made their first contribution in https://github.com/llm-d/llm-d/pull/652
* @Sneha-at made their first contribution in https://github.com/llm-d/llm-d/pull/631
* @ycjiang50 made their first contribution in https://github.com/llm-d/llm-d/pull/650
* @vinayK34 made their first contribution in https://github.com/llm-d/llm-d/pull/673
* @amito made their first contribution in https://github.com/llm-d/llm-d/pull/572
* @kfirtoledo made their first contribution in https://github.com/llm-d/llm-d/pull/609

**Full Changelog**: https://github.com/llm-d/llm-d/compare/v0.4...v0.5.0 

## v0.4.0 (2025-11-26)

# 📦 llm-d v0.4.0 Release Notes

This release of the `llm-d` repo will capture the release for the entirety of the project, guides, components, and all.

**Release Date:** 2025-11-26

---

## 🧩 Component Summary

| Component | Version | Previous Version | Type |
|-----------|---------|------------------| ---- |
| llmd/llm-d-inference-scheduler | `v0.4.0-rc.1` | `v0.3.1` | Image |
| llm-d-incubation/llm-d-modelservice | `v0.3.8` |`v0.2.10` | Helm Chart |
| llm-d/llm-d-routing-sidecar | `v0.4.0-rc.1` | `v0.3.1` | Image |
| llm-d/llm-d-cuda | `v0.4.0` | `v0.3.1` | Image |
| llm-d/llm-d-aws | `v0.4.0` | `v0.3.1` | Image |
| llm-d/llm-d-xpu | `v0.4.0` | `v0.3.1` | Image |
| llm-d/llm-d-cpu | `v0.4.0` | `v0.3.1` | Image (New) |
| llm-d-incubation/llm-d-infra | `v1.3.4` | `v1.3.3` | Helm Chart |
| kubernetes-sig/gateway-api-inference-extension | `v1.2.0-rc.1` | `v1.0.1` | Helm Chart |
| llm-d/llm-d-workload-variant-autoscaler | `v0.0.8` | NA (new) | Helm Chart + Image |

---

## 🔹 lmd/llm-d-inference-scheduler

- **Description**: This scheduler that makes optimized routing decisions for inference requests to the llm-d inference framework.
- **Diff**: [v0.3.1 → v0.4.0-rc.1](https://github.com/llm-d/llm-d-inference-scheduler/compare/v0.3.1...v0.4.0-rc.1)

---

## 🔹 llm-d-incubation/llm-d-modelservice

- **Description**: `modelservice` is a Helm chart that simplifies LLM deployment on llm-d by declaratively managing Kubernetes resources for serving base models. It enables reproducible, scalable, and tunable model deployments through modular presets, and clean integration with llm-d ecosystem components (including vLLM, Gateway API Inference Extension, LeaderWorkerSet).
- **Diff**: [v0.2.10 → v0.3.8](https://github.com/llm-d-incubation/llm-d-modelservice/compare/llm-d-modelservice-v0.2.10...llm-d-modelservice-v0.3.8)

---

## 🔹 llm-d/llm-d-routing-sidecar

- **Description**: A reverse proxy redirecting incoming requests to the prefill worker specified in the x-prefiller-host-port HTTP request header.
- **Diff**: [v0.3.1 → v0.4.0-rc.1](https://github.com/llm-d/llm-d-routing-sidecar/compare/v0.3.1...v0.4.0-rc.1)

---

## 🔹 llm-d/llm-d

- **Description**: A midstreamed image of `vllm-project/vllm` for inferencing, supporting features such as PD disaggregation, KV cache awareness and more.
- **Diff**: [v0.3.1 → v0.4.0](https://github.com/llm-d/llm-d/compare/v0.3.1...v0.4.0)
- **Image Variants**: Different image variants of this component:
    - XPU: `ghcr.io/llm-d/llm-d-xpu:v0.4.0`
    - AWS: `ghcr.io/llm-d/llm-d-aws:v0.4.0`
    - CUDA: `ghcr.io/llm-d/llm-d-cuda:v0.4.0`
    - CPU: `ghcr.io/llm-d/llm-d-cpu:v0.4.0`

---

## 🔹 llm-d-incubation/llm-d-infra

- **Description**: A helm chart for deploying gateway and gateway related infrastructure assets for llm-d.
- **Diff**: [v1.3.3 → v1.3.4](https://github.com/llm-d-incubation/llm-d-infra/compare/v1.3.3...v1.3.4)

---

## 🔹 kubernetes-sig/gateway-api-inference-extension

- **Description**: A Helm chart to deploy an InferencePool, a corresponding EndpointPicker (epp) deployment, and any other related assets.
- **Diff**: [v1.0.1 → v1.2.0-rc.1](https://github.com/kubernetes-sigs/gateway-api-inference-extension/compare/v1.0.1...v1.2.0-rc.1)

---

## 🔹 llm-d/llm-d-workload-variant-autoscaler (New - Experimental)

- **Description**: Variant optimization autoscaler for distributed inference workloads
- **History** (new): [v0.0.5](https://github.com/llm-d-incubation/workload-variant-autoscaler/tree/v0.0.5)
- **Note**: This is an experimental component being included in this release for early testing and feedback.

---

For more information on any of the component project or versions, please checkout their repos directly. For information on installing and using the new release refer to our [guides](https://github.com/llm-d/llm-d/blob/v0.4.0/guides). Thank you to all contributors who helped make this happen. Automated release notes will be included below, but it should be noted this only tracks work in the main repo, and does not fully reflect a changelog across the project

## What's Changed
* Add umbrella kv cache offloading well-lit path folder structure by @liu-cong in https://github.com/llm-d/llm-d/pull/401
* Correct wide-ep resource requirements. by @liu-cong in https://github.com/llm-d/llm-d/pull/373
* add information about component testing by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/361
* doc(guides): Introduce standardized recipes for Gateway, InferencePool, and vLLM by @zetxqx in https://github.com/llm-d/llm-d/pull/444
* Fix a broken link in the cpu prefix cache readme by @smarterclayton in https://github.com/llm-d/llm-d/pull/451
* Add more GKE specific workarounds and known issues by @smarterclayton in https://github.com/llm-d/llm-d/pull/419
* Update SIGs documentation to remove outdated schedule details.  by @petecheslock in https://github.com/llm-d/llm-d/pull/431
* Update links to deploying vLLM multi-host in stable docs by @smarterclayton in https://github.com/llm-d/llm-d/pull/436
* fix kutomization error and model flag error in cpu offloading. by @zetxqx in https://github.com/llm-d/llm-d/pull/453
* Add GKE B200 readme notes by @smarterclayton in https://github.com/llm-d/llm-d/pull/454
* doc: enrich the prefix-cache-storage vllm cpu native offloading with benchmark results by @zetxqx in https://github.com/llm-d/llm-d/pull/438
* Add CPU for llm-d Inference Scheduling by @ZhengHongming888 in https://github.com/llm-d/llm-d/pull/428
* Add cpu offloading example for GKE + LMCache by @dannawang0221 in https://github.com/llm-d/llm-d/pull/318
* Add tab format for better UX on the website by @liu-cong in https://github.com/llm-d/llm-d/pull/452
* Rename `prefix-cache-storage` to `tiered-prefix-cache` by @vMaroon in https://github.com/llm-d/llm-d/pull/468
* Remove the dockerfile.gke as it is no longer used by @smarterclayton in https://github.com/llm-d/llm-d/pull/462
* Token credentials fix + vLLM v0.11.1 by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/456
* guides: Make vLLM log more useful in inference-scheduling by @russellb in https://github.com/llm-d/llm-d/pull/439
* Inference scheduling support for Intel Gaudi accelerator by @poussa in https://github.com/llm-d/llm-d/pull/374
* Add JIT directories and model directories by @smarterclayton in https://github.com/llm-d/llm-d/pull/418
* Use markdown comments for Tabs support on docusaurus by @petecheslock in https://github.com/llm-d/llm-d/pull/474
* Highlight P/D benefits with throughput-interactivity tradeoff by @liu-cong in https://github.com/llm-d/llm-d/pull/472
* add benchmark results lmcache results and tuned epp scorers by @zetxqx in https://github.com/llm-d/llm-d/pull/457
* Add step by step guide for setting up p/d with TPU on GKE by @yangligt2 in https://github.com/llm-d/llm-d/pull/443
* refactor: restructure vllm recipe with base and overlay pattern by @diego-torres in https://github.com/llm-d/llm-d/pull/475
* [Build] Add FI JIT Cache to Image by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/482
* Add instructions to clone git repo and checkout the release by @liu-cong in https://github.com/llm-d/llm-d/pull/477
* Create CPU dockefile for PD and Inference Scheduling by @ZhengHongming888 in https://github.com/llm-d/llm-d/pull/465
* guides/prereq/client-setup/install-deps.sh - increment HELMFILE_VERSION to 1.2.1 by @herbertkb in https://github.com/llm-d/llm-d/pull/492
* docs: Addresses CPU support added in PR #428 by @aneeshkp in https://github.com/llm-d/llm-d/pull/466
* Infra, MS and GAIE bumps + istio change compat by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/459
* Update release version for cpu offloading guide by @liu-cong in https://github.com/llm-d/llm-d/pull/495
* enable TLS in monitoring for prom by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/496
* helmfile and supporting artifacts for wva by @clubanderson in https://github.com/llm-d/llm-d/pull/464
* updating LMCACHe to be non fork by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/501
* component bumps for WVA guide by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/502
* Build vLLM 0.11.2 + patches for 0.4 by @smarterclayton in https://github.com/llm-d/llm-d/pull/461
* Avoid defining LMCACHE_COMMIT_SHA in multiple places by @terrytangyuan in https://github.com/llm-d/llm-d/pull/503
* WVA guide integration targeting v0.4 by @mamy-CS in https://github.com/llm-d/llm-d/pull/470
* fixing AWS image by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/506
* remove pre-passing values for VLLM by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/507

## New Contributors
* @zetxqx made their first contribution in https://github.com/llm-d/llm-d/pull/444
* @ZhengHongming888 made their first contribution in https://github.com/llm-d/llm-d/pull/428
* @dannawang0221 made their first contribution in https://github.com/llm-d/llm-d/pull/318
* @russellb made their first contribution in https://github.com/llm-d/llm-d/pull/439
* @poussa made their first contribution in https://github.com/llm-d/llm-d/pull/374
* @yangligt2 made their first contribution in https://github.com/llm-d/llm-d/pull/443
* @diego-torres made their first contribution in https://github.com/llm-d/llm-d/pull/475
* @herbertkb made their first contribution in https://github.com/llm-d/llm-d/pull/492
* @aneeshkp made their first contribution in https://github.com/llm-d/llm-d/pull/466
* @mamy-CS made their first contribution in https://github.com/llm-d/llm-d/pull/470

**Full Changelog**: https://github.com/llm-d/llm-d/compare/v0.3.1...v0.4.0

## v0.5.1 (2026-03-05)

## LLM-D Component Summary

| Component | Version | Previous Version | Type |
|-----------|---------|------------------|------|
| llm-d/llm-d-inference-scheduler | `v0.6.0` | `v0.5.0` | Image |
| llm-d/llm-d-kv-cache | `v0.6.0` | `v0.5.0` | Library |
| llm-d-incubation/llm-d-modelservice | `v0.4.7` | `v0.4.5` | Helm Chart |
| llm-d/llm-d-routing-sidecar | `v0.6.0` | `v0.5.0` | Image |
| llm-d/llm-d-inference-sim | `v0.7.1` | `v0.7.1` | Image |
| llm-d/llm-d-cuda | `v0.5.1` | `v0.5.0` | Image |
| llm-d/llm-d-cuda (debug) | `v0.5.1` | NA | Image (New) |
| llm-d/llm-d-aws (EFA) | `v0.5.1` | Deprecated in v0.5.0 | Image (Re-enabled) |
| llm-d/llm-d-xpu | `v0.5.1` | `v0.5.0` | Image |
| llm-d/llm-d-cpu | `v0.5.1` | `v0.5.0` | Image |
| llm-d/llm-d-rocm | `v0.5.1` | NA | Image (New) |
| llm-d/llm-d-hpu | `v0.5.1` | NA | Image (New) |
| vllm-project/vllm | `v0.15.1` | `v0.14.1` | Wheel installed in `llm-d` |
| llm-d-incubation/llm-d-infra | `v1.3.6` | `v1.3.6` | Helm Chart |
| kubernetes-sigs/gateway-api-inference-extension | `v1.3.1` | `v1.3.0` | Helm Chart (Pending upstream release) |
| llm-d/llm-d-workload-variant-autoscaler | `v0.5.1` | `v0.5.0` | Helm Chart + Image |

---

## Infrastructure Changes

| Component | Version | Previous Version |
|-----------|---------|------------------|
| Gateway API | `v1.3.1` | `v1.3.0` |
| Istio | `1.28.1` | `1.28.1` |
| KGateway | `v2.1.1` | `v2.1.1` |

---

## What's Changed
* Fix XPU example errors by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/696
* Simplify storage offloading guides into a single one  by @liu-cong in https://github.com/llm-d/llm-d/pull/683
* feat: remove standalone by @capri-xiyue in https://github.com/llm-d/llm-d/pull/688
* update permissions for lustre guide setup by @Sneha-at in https://github.com/llm-d/llm-d/pull/710
* Fix: add retries for model discovery by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/704
* [BUGFIX] Comment caching to avoid error by @diegocastanibm in https://github.com/llm-d/llm-d/pull/719
* Fix lint issues by @diegocastanibm in https://github.com/llm-d/llm-d/pull/721
* llm-d install doc on openshift 4.20 by @fgharo in https://github.com/llm-d/llm-d/pull/538
* Enables AMD inference scheduling well-lit path by @vcave in https://github.com/llm-d/llm-d/pull/642
* [build fix] Remove linking compat dir by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/727
* just deprecate queue scorrer params by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/730
* Add Gaudi inference scheduling CI workflow test by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/486
* fix gke monitoring in helmfile by @zetxqx in https://github.com/llm-d/llm-d/pull/697
* add intel HPU for llm-d P/D disaggregation by @ZhengHongming888 in https://github.com/llm-d/llm-d/pull/372
* Add the XPU CI test by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/380
* feat: add feature request issue template by @thillai-c in https://github.com/llm-d/llm-d/pull/733
* Add the format hint for CI by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/717
* feat: add support to build for CPU on AMX by @zdtsw in https://github.com/llm-d/llm-d/pull/725
* fix: add missing check-buildah target in Makefile by @GuilinDev in https://github.com/llm-d/llm-d/pull/735
* docs: fix typos and spelling errors across docs, guides, and Dockerfile by @thillai-c in https://github.com/llm-d/llm-d/pull/731
* docs: update container image link in PROJECT.md by @petecheslock in https://github.com/llm-d/llm-d/pull/738
* Add debug variant support for llm-d images across CUDA by @kapiljain1989 in https://github.com/llm-d/llm-d/pull/734
* 🌱 Add typos config and Dependabot by @clubanderson in https://github.com/llm-d/llm-d/pull/746
* chore: update bug report issue template with current versions by @thillai-c in https://github.com/llm-d/llm-d/pull/732
* ✨ Add nightly E2E OpenShift workflows for 5 guides by @clubanderson in https://github.com/llm-d/llm-d/pull/747
* 🌱 Standardize governance workflows via llm-d-infra by @clubanderson in https://github.com/llm-d/llm-d/pull/744
* 🌱 Remove dependabot configuration by @clubanderson in https://github.com/llm-d/llm-d/pull/756
* linting links by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/757
* 🐛 Fix broken reusable workflow references by @clubanderson in https://github.com/llm-d/llm-d/pull/762
* 🐛 Bump nightly pod_wait_timeout from 15m to 30m by @clubanderson in https://github.com/llm-d/llm-d/pull/760
* 🐛 Fix PD disaggregation nightly decode tensor parallelism by @clubanderson in https://github.com/llm-d/llm-d/pull/764
* 🐛 Fix tiered-prefix-cache CrashLoopBackOff: num_cpu_blocks → cpu_bytes_to_use by @clubanderson in https://github.com/llm-d/llm-d/pull/768
* ⚠️ Revert: Fix tiered-prefix-cache CrashLoopBackOff (#768) by @clubanderson in https://github.com/llm-d/llm-d/pull/769
* 🐛 Fix tiered-prefix-cache CrashLoopBackOff: num_cpu_blocks → cpu_bytes_to_use by @clubanderson in https://github.com/llm-d/llm-d/pull/770
* adding required packages for LMCache runtime by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/701
* ✨ Add upstream dependency monitor, dependabot, and remove legacy CI callers by @clubanderson in https://github.com/llm-d/llm-d/pull/771
* Set accelerator_type to H100 and rename OCP nightly workflows by @diegocastanibm in https://github.com/llm-d/llm-d/pull/777
* ✨ Add CKS nightly E2E workflows for IS and PD by @clubanderson in https://github.com/llm-d/llm-d/pull/780
* ressurect efa by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/741
* ✨ Add wide-ep and benchmark CKS nightly callers by @clubanderson in https://github.com/llm-d/llm-d/pull/782
* deps(actions): bump docker/build-push-action from 5 to 6 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/755
* deps(actions): bump actions/upload-artifact from 4 to 6 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/752
* ✨ Fix dev image latest tag + nightly build + image_override for all E2E nightlies by @clubanderson in https://github.com/llm-d/llm-d/pull/783
* deps(actions): bump actions/checkout from 4 to 6 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/751
* Update interactive-pod to use latest guidellm by @natoscott in https://github.com/llm-d/llm-d/pull/716
* 🌱 OCP H100 nodeSelector + CKS GPU preemption for nightly E2E by @clubanderson in https://github.com/llm-d/llm-d/pull/788
* 🐛 Fix typo in CKS benchmark caller workflow dispatch by @clubanderson in https://github.com/llm-d/llm-d/pull/790
* 🐛 Build WVA image from main + prevent fork schedule runs by @clubanderson in https://github.com/llm-d/llm-d/pull/794
* 🐛 Fix CKS WVA test target: use test-e2e-openshift (no kind dependency) by @clubanderson in https://github.com/llm-d/llm-d/pull/797
* 🐛 Build WVA controller image from main for CKS nightly by @clubanderson in https://github.com/llm-d/llm-d/pull/798
* 🐛 Add docker build retry for WVA nightly E2E workflows by @clubanderson in https://github.com/llm-d/llm-d/pull/801
* ✨ Enable GPU preemption on all nightly E2E workflows by @clubanderson in https://github.com/llm-d/llm-d/pull/810
* bump to nixl 0.10.0 and vllm v0.15.1 by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/713
* Replace RHEL packages with static CentOS Stream 9 RPMs by @dagrayvid in https://github.com/llm-d/llm-d/pull/669
* sa was missing, copy it in by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/813
* ocp nightly wide-ep sa was missing, copy it in by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/814
* Fix typos tracked in _typos.toml by @lisperz in https://github.com/llm-d/llm-d/pull/786
* feat: add support to use kv-cache UDS tokenizer sidecar in guide by @zdtsw in https://github.com/llm-d/llm-d/pull/740
* Add RDMA tools container image for RoCE/InfiniBand validation by @dagrayvid in https://github.com/llm-d/llm-d/pull/626
* docs: update README for v0.5 release by @chcost in https://github.com/llm-d/llm-d/pull/822
* Proposal: Prism - Performance analysis for distributed inference systems by @seanhorgan in https://github.com/llm-d/llm-d/pull/796
* 🐛 Fix uds-tokenizer image tag in PPC guide (v0.5.0-rc1 → v0.5.1-rc1) by @clubanderson in https://github.com/llm-d/llm-d/pull/829
* Add gke rilb gateway class by @liu-cong in https://github.com/llm-d/llm-d/pull/815
* Release doc by @diegocastanibm in https://github.com/llm-d/llm-d/pull/819
* Add gateway provider prereq to the tiered prefix cache guides by @liu-cong in https://github.com/llm-d/llm-d/pull/761
* [BUG] sourcing docker/vllm-version in ci-release by @diegocastanibm in https://github.com/llm-d/llm-d/pull/823
* ⚠️ Skip gateway provider install on OCP nightly E2Es by @clubanderson in https://github.com/llm-d/llm-d/pull/833
* Add a MAINTAINERS file for current and future maintainers list by @petecheslock in https://github.com/llm-d/llm-d/pull/817
* update: bump llm-d-modelservice chart to 0.4.6 by @zdtsw in https://github.com/llm-d/llm-d/pull/644
* Add sig-rl structure proposal by @smarterclayton in https://github.com/llm-d/llm-d/pull/840
* Update benchmark templates to 0.5 by @dmitripikus in https://github.com/llm-d/llm-d/pull/816
* Revert "Update benchmark templates to 0.5" by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/841
* Add ADOPTERS.md to document project contributors and supporters by @petecheslock in https://github.com/llm-d/llm-d/pull/830
* [ADOPTERS.md] Add Tesla as a user of llm-d by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/845
* Change the model name and workflow name by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/742
* 🐛 fix: increase startup probe and pod wait timeouts for IS nightly E2E by @clubanderson in https://github.com/llm-d/llm-d/pull/852
* [Benchmark Guide] [WVA + IS] Document and Provide a WVA + IS Benchmark Guide by @Vezio in https://github.com/llm-d/llm-d/pull/820
* Update benchmark templates to 0.5 (#816) by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/843
* Remove pplx All2All backend by @tlrmchlsmth in https://github.com/llm-d/llm-d/pull/855
* Use an argument instead of an env for the All2All backend by @tlrmchlsmth in https://github.com/llm-d/llm-d/pull/856
* Update README for clarity by @smarterclayton in https://github.com/llm-d/llm-d/pull/839
* 🐛 Fix WVA nightlies to use consolidated test suite by @clubanderson in https://github.com/llm-d/llm-d/pull/863
* Adds DaoCloud as a contributor to the llm-d adopters list. by @yankay in https://github.com/llm-d/llm-d/pull/867
* ✨ feat: add caller_ref input to WVA nightly workflows by @clubanderson in https://github.com/llm-d/llm-d/pull/891
* [Feature] Enable DP-Aware WideEP by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/827
* Enables AMD prefill/decode disaggregation well-lit path by @vcave in https://github.com/llm-d/llm-d/pull/776
* swap to nm fork for llm-d releases by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/893
* Fix: rename std to std_dev in inference-perf benchmark configs by @edingroot in https://github.com/llm-d/llm-d/pull/890
* Modify Intelligent Inference Scheduling guide by @roytman in https://github.com/llm-d/llm-d/pull/898
* distributed tracing proposal by @sallyom in https://github.com/llm-d/llm-d/pull/119
* Distributed tracing implementation docs and guides by @sallyom in https://github.com/llm-d/llm-d/pull/745
* fixing dynamo docs paths by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/901
* Bump versions v060 rc1 for testing by @diegocastanibm in https://github.com/llm-d/llm-d/pull/903
* Fix llm-d-routing-sidecar for P/D by @maugustosilva in https://github.com/llm-d/llm-d/pull/904
* Collect logs for all containers on gaie-epp by @maugustosilva in https://github.com/llm-d/llm-d/pull/906
* New contents for `pd-config.yaml` on P/D Disaggregation by @maugustosilva in https://github.com/llm-d/llm-d/pull/907
* Version bump by @diegocastanibm in https://github.com/llm-d/llm-d/pull/894
* tokenizer-uds v0.6.0 by @diegocastanibm in https://github.com/llm-d/llm-d/pull/913

## New Contributors
* @diegocastanibm made their first contribution in https://github.com/llm-d/llm-d/pull/719
* @fgharo made their first contribution in https://github.com/llm-d/llm-d/pull/538
* @vcave made their first contribution in https://github.com/llm-d/llm-d/pull/642
* @thillai-c made their first contribution in https://github.com/llm-d/llm-d/pull/733
* @GuilinDev made their first contribution in https://github.com/llm-d/llm-d/pull/735
* @kapiljain1989 made their first contribution in https://github.com/llm-d/llm-d/pull/734
* @dependabot[bot] made their first contribution in https://github.com/llm-d/llm-d/pull/755
* @lisperz made their first contribution in https://github.com/llm-d/llm-d/pull/786
* @Vezio made their first contribution in https://github.com/llm-d/llm-d/pull/820
* @edingroot made their first contribution in https://github.com/llm-d/llm-d/pull/890
* @roytman made their first contribution in https://github.com/llm-d/llm-d/pull/898
* @maugustosilva made their first contribution in https://github.com/llm-d/llm-d/pull/904

**Full Changelog**: https://github.com/llm-d/llm-d/compare/v0.5.0...v0.5.1

## v0.6.0 (2026-04-03)

## LLM-D Component Summary

| Component | Version | Previous Version | Type |
|-----------|---------|------------------|------|
| llm-d/llm-d-inference-scheduler | `v0.7.1` | `v0.6.0` | Image |
| llm-d/llm-d-uds-tokenizer | `v0.7.1` | `v0.6.0` | Image |
| llm-d/llm-d-kv-cache | `v0.7.1` | `v0.6.0` | Library |
| llm-d/llm-d-routing-sidecar | `v0.7.1` | `v0.6.0` | Image |
| llm-d/llm-d-inference-sim | `v0.8.2` | `v0.7.1` | Image |
| llm-d/llm-d-cuda | `v0.6.0` | `v0.5.1` | Image |
| llm-d/llm-d-cuda (debug) | `v0.6.0` | `v0.5.1` | Image |
| llm-d/llm-d-aws (EFA) | `v0.6.0` | `v0.5.1` | Image |
| llm-d/llm-d-xpu | `v0.6.0` | `v0.5.1` | Image (Temporarily Unavailable) |
| llm-d/llm-d-hpu | `v0.6.0` | `v0.5.1` | Image (Temporarily Unavailable) |
| llm-d/llm-d-cpu | `v0.6.0` | `v0.5.1` | Image |
| llm-d/llm-d-rocm | `v0.6.0` | `v0.5.1` | Image |
| llm-d/llm-d-kv-cache/llmd_fs_backend_connector | `v0.17.1` | `v0.15.1` | Wheel installed in `llm-d` |
| llm-d/llm-d-workload-variant-autoscaler | `v0.6.0` | `v0.5.1` | Helm Chart + Image |
| llm-d-incubation/llm-d-infra | `v1.4.0` | `v1.3.6` | Helm Chart |
| llm-d-incubation/llm-d-modelservice | `v0.4.9` | `v0.4.7` | Helm Chart |
| vllm-project/vllm | `v0.17.1` | `v0.15.1` | Wheel installed in `llm-d` |
| kubernetes-sigs/gateway-api-inference-extension | `v1.4.0` | `v1.3.1` | Helm Chart |

---

## Infrastructure Changes

| Component | Version | Previous Version |
|-----------|---------|------------------|
| Gateway API | `v1.5.1` | `v1.4.0` |
| Istio | `1.29.1` | `1.28.1` |
| agentgateway (old KGateway) | `v2.2.1` | `v2.1.1` |

---

## What's Changed
* Add SGLang option for inference-scheduling well-lit path by @andreyod in https://github.com/llm-d/llm-d/pull/527
* add step to build hpu by @diegocastanibm in https://github.com/llm-d/llm-d/pull/917
* 🌱 Remove per-repo gh-aw typo/link/upstream workflows by @clubanderson in https://github.com/llm-d/llm-d/pull/920
* docs: Small fixes in the inference-scheduling installation guide by @roytman in https://github.com/llm-d/llm-d/pull/924
* Fix link to vLLM Native CPU Offloading documentation by @petecheslock in https://github.com/llm-d/llm-d/pull/928
* docs: Remove unnecessary backticks around llm-d by @terrytangyuan in https://github.com/llm-d/llm-d/pull/933
* Partial enablement of CICD for GKE by @maugustosilva in https://github.com/llm-d/llm-d/pull/934
* Add hpu to ci-release by @diegocastanibm in https://github.com/llm-d/llm-d/pull/918
* Only report on 404 broken links and not temp issues or scraper blocks by @petecheslock in https://github.com/llm-d/llm-d/pull/846
* hpu: update images by @poussa in https://github.com/llm-d/llm-d/pull/936
* fix: correct typos in documentation and code comments by @BaskDuan in https://github.com/llm-d/llm-d/pull/973
* Fix the HPU failed issue and enable HPU PR checks in CI by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/965
* chore: update xpu image build inputs by @VincyZhang in https://github.com/llm-d/llm-d/pull/911
* Add HPA + IGW metrics autoscaling guide to the autoscaling well-lit path by @aishukamal in https://github.com/llm-d/llm-d/pull/972
* deps(actions): bump actions/checkout from 4 to 6 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/836
* Build llm-d-cuda locally by @diegocastanibm in https://github.com/llm-d/llm-d/pull/865
* build: add CUDA versions into central build file by @zdtsw in https://github.com/llm-d/llm-d/pull/982
* Mark myself as inactive project maintainer while on leave by @smarterclayton in https://github.com/llm-d/llm-d/pull/985
* update the result for inference-scheduling and precise-prefix-cache-aware by @zetxqx in https://github.com/llm-d/llm-d/pull/722
* install storage offloading connector by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/640
* try set and unset cuda stubs in LIBRARY_PATH by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/987
* upgrading to vLLM v0.17.1 by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/977
* Refresh support for kgateway agentgateway GIE and GW API by @danehans in https://github.com/llm-d/llm-d/pull/421
* Update gke inference scheduling test to address failures by @rlakhtakia in https://github.com/llm-d/llm-d/pull/649
* deps(actions): bump google-github-actions/setup-gcloud from 2.2.0 to 3.0.1 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/835
* updating common configurations with infra refactor 272 by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/997
* ci test helm chart schemas + helmfile examples + dry run k8s apply by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/998
* any build triggered from push to main should be latest by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/996
* fix: use VLLM_PRECOMPILED_WHEEL_COMMIT from vllm 0.17.1 by @zdtsw in https://github.com/llm-d/llm-d/pull/1007
* enable building from open PRs by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1011
* build: reduce cuda runtime image size by switch base image by @zdtsw in https://github.com/llm-d/llm-d/pull/606
* github: pin to a version for trivy than mastser by @zdtsw in https://github.com/llm-d/llm-d/pull/1018
* ci: use pull_request for upstream PRs, pull_request_target for forks by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1023
* removing sm70 and 75 because lack of cuda 12.9.X support rdma-tools by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1024
* docs: llm-d planner proposal by @anfredette in https://github.com/llm-d/llm-d/pull/963
* Image verification workflow by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1010
* deps(actions): bump actions/setup-go from 5 to 6 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1016
* deps(actions): bump github/codeql-action from 3 to 4 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1015
* deps(actions): bump lycheeverse/lychee-action from 2.7.0 to 2.8.0 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/930
* Add benchmarking numbers for Lustre with LMcache connector by @Sneha-at in https://github.com/llm-d/llm-d/pull/1020
* Add P/D Disaggregation with RoCE/GDR for OpenShift by @maugustosilva in https://github.com/llm-d/llm-d/pull/1025
* Move benchmark templates into the specific guide directories by @deanlorenz in https://github.com/llm-d/llm-d/pull/784
* build: add infiniband-diags to rdma-tools runtime image by @rajkiranjoshi in https://github.com/llm-d/llm-d/pull/1040
* fix: typos from nightly scan by @tessapham in https://github.com/llm-d/llm-d/pull/1037
* Attempted fix for CI/CD GKE by explicitly exporting LD_LIBRARY_PATH by @maugustosilva in https://github.com/llm-d/llm-d/pull/1032
* Change `HELMFILE_ENV` on P/D Disaggregation (OpenShift) to `ocp` by @maugustosilva in https://github.com/llm-d/llm-d/pull/1041
* Adding Topology Aware Scheduling labels on Wide-EP GKE example by @Edwinhr716 in https://github.com/llm-d/llm-d/pull/531
* Fix `llm-d.ai/guide` for pods on PD guide by @maugustosilva in https://github.com/llm-d/llm-d/pull/1047
* Async Processor well-lit path guide  by @shimib in https://github.com/llm-d/llm-d/pull/1031
* And llm_d_ref defaults to main by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1049
* docs: expand suspended hyphens in Inference Scheduler description by @skmahe1077 in https://github.com/llm-d/llm-d/pull/1050
* deps(actions): bump docker/setup-buildx-action from 3 to 4 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1044
* deps(actions): bump actions/github-script from 7 to 8 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1043
* deps(actions): bump docker/metadata-action from 5 to 6 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1042
* llm-d skills proposal by @rachelt44 in https://github.com/llm-d/llm-d/pull/1039
* Additional fix for gke ld library path by @maugustosilva in https://github.com/llm-d/llm-d/pull/1052
* 🐛 Fix kubectl attach race condition in e2e-validate.sh by @clubanderson in https://github.com/llm-d/llm-d/pull/1051
* Fix pd on gke by @maugustosilva in https://github.com/llm-d/llm-d/pull/1053
* ✨ Add /test-nightly slash command for fork PRs by @clubanderson in https://github.com/llm-d/llm-d/pull/1048
* Bump simulator version to v0.8.2 by @mayabar in https://github.com/llm-d/llm-d/pull/1045
* build: add libibverbs-utils to rdma-tools runtime image by @rajkiranjoshi in https://github.com/llm-d/llm-d/pull/1055
* fix: add missing sizeLimit and fix label typo in inference-scheduling configs by @wenhug in https://github.com/llm-d/llm-d/pull/1038
* docs: replace Envoy proxy references with Gateway API by @tessapham in https://github.com/llm-d/llm-d/pull/1036
* docs: update KV events topic to ip:port format for scheduler v0.7.0 by @bongwoobak in https://github.com/llm-d/llm-d/pull/1008
* deps(actions): bump haya14busa/action-update-semver from 1.3.0 to 1.5.1 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/754
* deps(actions): bump actions/setup-python from 5 to 6 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/753
* docs: assign a level of maturity for each guide by @maugustosilva in https://github.com/llm-d/llm-d/pull/1058
* update versions for v0.6.0 release by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1064
* Add SGLang option to PD disaggregation well-lit path by @andreyod in https://github.com/llm-d/llm-d/pull/580
* docs: bump inference-scheduler image to v0.7.1 by @bongwoobak in https://github.com/llm-d/llm-d/pull/1069
* ✨ Add glob patterns and run URL feedback to /test-nightly by @clubanderson in https://github.com/llm-d/llm-d/pull/1065
* ✨ Replace blocking lychee CI with gh-aw nightly checkers by @clubanderson in https://github.com/llm-d/llm-d/pull/1066
* Images Preparation for v0.6.0 by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1067
* Last version bump before cutting `v0.6` release by @maugustosilva in https://github.com/llm-d/llm-d/pull/1070

## New Contributors
* @andreyod made their first contribution in https://github.com/llm-d/llm-d/pull/527
* @BaskDuan made their first contribution in https://github.com/llm-d/llm-d/pull/973
* @VincyZhang made their first contribution in https://github.com/llm-d/llm-d/pull/911
* @aishukamal made their first contribution in https://github.com/llm-d/llm-d/pull/972
* @danehans made their first contribution in https://github.com/llm-d/llm-d/pull/421
* @anfredette made their first contribution in https://github.com/llm-d/llm-d/pull/963
* @rajkiranjoshi made their first contribution in https://github.com/llm-d/llm-d/pull/1040
* @tessapham made their first contribution in https://github.com/llm-d/llm-d/pull/1037
* @shimib made their first contribution in https://github.com/llm-d/llm-d/pull/1031
* @skmahe1077 made their first contribution in https://github.com/llm-d/llm-d/pull/1050
* @rachelt44 made their first contribution in https://github.com/llm-d/llm-d/pull/1039
* @mayabar made their first contribution in https://github.com/llm-d/llm-d/pull/1045
* @wenhug made their first contribution in https://github.com/llm-d/llm-d/pull/1038
* @bongwoobak made their first contribution in https://github.com/llm-d/llm-d/pull/1008

**Full Changelog**: https://github.com/llm-d/llm-d/compare/v0.5.1...v0.6.0

## v0.7.0 (2026-05-12)

## LLM-D Component Summary

- **⚠️ BREAKING CHANGE — CUDA 13.0.2 runtime:** All llm-d CUDA images now ship with CUDA 13.0.2 (upgraded from 12.x). This requires **NVIDIA driver 580 or later** on the host. Nodes running older drivers must be upgraded before deploying v0.7.0 images.
-  UX Change - due to the difficulty configuring gateways for many adopters, we have made the default deployment of llm-d to use "standalone mode" where we use a generic proxy instead of the more feature full gateway. We still recomend a fully gateway for customers in production.

| Component | Version | Previous Version | Type |
|-----------|---------|------------------|------|
| llm-d/llm-d-inference-scheduler | `v0.8.0` | `v0.7.1` | Image |
| llm-d/llm-d-uds-tokenizer | `vllm-v0.19.1` | `v0.7.1` | Image |
| llm-d/llm-d-kv-cache | `v0.8.0` | `v0.7.1` | Library |
| llm-d/llm-d-routing-sidecar | `v0.8.0` | `v0.7.1` | Image |
| llm-d/llm-d-inference-sim | `v0.8.2` | `v0.7.1` | Image |
| llm-d/llm-d-cuda | `v0.7.0` | `v0.6.0` | Image |
| llm-d/llm-d-cuda (debug) | `v0.7.0` | `v0.6.0` | Image |
| llm-d/llm-d-cuda-gb200 | `v0.7.0` | N/A | Image (New) |
| llm-d/llm-d-aws (EFA) | `v0.7.0` | `v0.6.0` | Image |
| llm-d/llm-d-xpu | `v0.7.0` | `v0.6.0` | Image |
| llm-d/llm-d-hpu | `v0.7.0` | `v0.6.0` | Image |
| llm-d/llm-d-cpu | `v0.7.0` | `v0.6.0` | Image |
| llm-d/llm-d-rocm | `v0.7.0` | `v0.6.0` | Image |
| llm-d/llm-d-kv-cache/llmd_fs_backend_connector | `v0.19.1` | `v0.17.1` | Wheel installed in `llm-d` |
| llm-d/llm-d-workload-variant-autoscaler | `v0.7.0` | `v0.6.0` | Helm Chart + Image |
| llm-d-incubation/llm-d-infra (Deprecated)  | N/A  | `v1.4.0` | Helm Chart |
| llm-d-incubation/llm-d-modelservice (Deprecated) | N/A | `v0.4.9` | Helm Chart |
| vllm-project/vllm | `v0.19.1` | `v0.17.1` | Wheel installed in `llm-d` |
| kubernetes-sigs/gateway-api-inference-extension | `v1.5.0` | `v1.4.0` | Helm Chart |


---

## Infrastructure Changes

| Component | Version | Previous Version |
|-----------|---------|------------------|
| Gateway API | `v1.5.1` | `v1.4.0` |
| Istio | `1.29.1` | `1.28.1` |
| agentgateway (old KGateway) | `v2.2.1` | `v2.1.1` |

## What's Changed
* Simplify WVA guide test by @lionelvillard in https://github.com/llm-d/llm-d/pull/1072
* fix concurrency group to sha not PR by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1073
* fix block-size alignment by @vMaroon in https://github.com/llm-d/llm-d/pull/1084
* Revise maturity status and TPU VM type details by @seanhorgan in https://github.com/llm-d/llm-d/pull/1085
* Fix formatting of automated test status in README by @seanhorgan in https://github.com/llm-d/llm-d/pull/1087
* Fix image on pd user guide by @Edwinhr716 in https://github.com/llm-d/llm-d/pull/1086
* Updated maturity testing level on all guides by @maugustosilva in https://github.com/llm-d/llm-d/pull/1094
* Skip latest tag for release candidates by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1034
* fix(xpu): enable TP=2 for Qwen3-32B for fixing XPU prefix-cache test failed by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/1081
* [guides] Add a commented `priorityClassName` for use in nightly CI/CD by @maugustosilva in https://github.com/llm-d/llm-d/pull/1062
* deps(actions): bump docker/build-push-action from 6 to 7 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1089
* deps(actions): bump actions/github-script from 7 to 8 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1091
* deps(actions): bump google-github-actions/auth from 2.1.12 to 3.0.0 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1090
* deps(actions): bump dorny/paths-filter from 3 to 4 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1092
* deps(actions): bump docker/login-action from 3 to 4 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1093
* Add shared drive for sig-rl by @petecheslock in https://github.com/llm-d/llm-d/pull/1109
* Fix llm-d performance dashboard queries by @danehans in https://github.com/llm-d/llm-d/pull/1098
* Fix/e2e validate single curl pod by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/1078
* Add Moreh as a contributor to the adopters list by @hhk7734 in https://github.com/llm-d/llm-d/pull/1111
* Update guides with status badges. by @maugustosilva in https://github.com/llm-d/llm-d/pull/1110
* fix: use vllmServe modelCommand in precise-prefix-cache-aware XPU values by @sharvil10 in https://github.com/llm-d/llm-d/pull/1101
* Add deployment health-check smoke test for llm-d clusters by @lisperz in https://github.com/llm-d/llm-d/pull/767
* [1/N] Documentation Revamp by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1100
* fix: split vLLM command array and fill in quickstart TODOs by @madhugoutham in https://github.com/llm-d/llm-d/pull/1126
* add OCI well-lit-path for P/D disaggregation by @hexfusion in https://github.com/llm-d/llm-d/pull/1123
* fix: use the proper git ref for tag extraction by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1133
* Update latency-predictor.md diagram by @LukeAVanDrie in https://github.com/llm-d/llm-d/pull/1127
* docs: fix typos detected by nightly scan (issue #1056) by @ianliuy in https://github.com/llm-d/llm-d/pull/1135
* [Docs][4/N] Update architecture/core/epp/scheduling.md docs by @ahg-g in https://github.com/llm-d/llm-d/pull/1122
* [2/N] Proxy Doc by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1121
* [Docs][6/N]: add Istio gateway setup guide by @madhugoutham in https://github.com/llm-d/llm-d/pull/1146
* docs: add EPP flow control reference by @LukeAVanDrie in https://github.com/llm-d/llm-d/pull/1130
* [Docs] [3/N] Add Disaggregation Architecture Docs by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1138
* [Docs] Add glossary page by @ianliuy in https://github.com/llm-d/llm-d/pull/1148
* Add agentgateway guide by @danehans in https://github.com/llm-d/llm-d/pull/1159
* fix(docs): correct typos from nightly scan, add false-positive config by @ianliuy in https://github.com/llm-d/llm-d/pull/1160
* [Docs] Guides Directory Cleanup by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1163
* [Docs][EPP] Doc for request handling and control by @zetxqx in https://github.com/llm-d/llm-d/pull/1128
* fix(docker): add LIBRARY_PATH and ldconfig to CUDA runtime stage by @ianliuy in https://github.com/llm-d/llm-d/pull/1147
* Update ms-inference-scheduling/values_tpu_v7.yaml to use RunAI model streamer by @amacaskill in https://github.com/llm-d/llm-d/pull/1102
* deps(actions): bump hashicorp/setup-terraform from 3.1.2 to 4.0.0 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1153
* deps(actions): bump aws-actions/configure-aws-credentials from 4.3.1 to 6.1.0 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1152
* deps(actions): bump actions/github-script from 8 to 9 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1150
* deps(actions): bump j178/prek-action from 1 to 2 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1151
* deps(actions): bump actions/upload-artifact from 6 to 7 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1149
* [Docs] Remove `customizing-a-guide.md` by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1165
* [Docs] Move `guides/benchmarks` to `helpers/benchmark.md` by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1164
* [Docs][Istio] Align to AgentGateway Doc by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1161
* deps(docker): bump gdrcopy from v2.5.1 to v2.5.2 by @ianliuy in https://github.com/llm-d/llm-d/pull/1171
* [Docs] Envoy Proxy -> GAIE-Conformant Proxy by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1162
* Updated the basic architecture diagram by @ahg-g in https://github.com/llm-d/llm-d/pull/1173
* [Docs] Fix Broken Quickstart Links by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1175
* [Docs] Remove guide/prereq/infrastructure by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1168
* Added GKE gateway guide by @ahg-g in https://github.com/llm-d/llm-d/pull/1174
* [Docs] Move Client Tools from Guides --> Helpers by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1167
* feat: add Rebellions as a supported accelerator vendor by @rebel-jinmoo in https://github.com/llm-d/llm-d/pull/1115
* docs: rewrite predicted latency architecture and add well-lit path by @kaushikmitr in https://github.com/llm-d/llm-d/pull/1166
* [Docs][Autoscaling][2/N] hpa/keda vs hpa design choices/features by @lionelvillard in https://github.com/llm-d/llm-d/pull/1157
* [Docs][7/N] KV Indexer by @vMaroon in https://github.com/llm-d/llm-d/pull/1143
* [Docs][autoscaling][1/N] Autoscaling intro by @lionelvillard in https://github.com/llm-d/llm-d/pull/1145
* [Docs] Refine RDMA docs by @praveingk in https://github.com/llm-d/llm-d/pull/1181
* Fixup merge conflict markers in `tiered-prefix-cache/storage/README.md` by @tlrmchlsmth in https://github.com/llm-d/llm-d/pull/1190
* [Docs] fix broken link by @lionelvillard in https://github.com/llm-d/llm-d/pull/1191
* docs: llm-d-inference-payload-processor proposal by @nilig in https://github.com/llm-d/llm-d/pull/1184
* [Docs] Well Lit Paths Doc by @chcost in https://github.com/llm-d/llm-d/pull/1156
* Tweaks to the latency predictor docs by @ahg-g in https://github.com/llm-d/llm-d/pull/1201
* [Docs] Restructure Predicted Latency Well Lit Path Doc by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1200
* [Docs][Autoscaling][4/N] first pass at the HPA+IGW doc by @lionelvillard in https://github.com/llm-d/llm-d/pull/1192
* Updating native HPA-based autoscaling guide to reference EPP instead of IGW by @ahg-g in https://github.com/llm-d/llm-d/pull/1212
* [Docs] Rename Well-Lit-Paths -> Guides, Guides -> Resources by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1199
* deps(actions): bump actions/checkout from 4 to 6 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1221
* deps(actions): bump helm/kind-action from 1.12.0 to 1.14.0 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1220
* deps(actions): bump actions/download-artifact from 4 to 8 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1219
* [Docs][8/N] KV Offloader Doc by @vMaroon in https://github.com/llm-d/llm-d/pull/1144
* [Docs] Fix Various Nits by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1215
* Update TPU recommendations in README by @seanhorgan in https://github.com/llm-d/llm-d/pull/1213
* Fix typos by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1223
* [Docs] Remove envoy reference by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1225
* Proposal doc for Inference Resilience Operator by @aishukamal in https://github.com/llm-d/llm-d/pull/984
* docs(epp): polish architecture and configuration guides by @LukeAVanDrie in https://github.com/llm-d/llm-d/pull/1227
* [Docs] Consolidate Gateway Docs To Use YAML by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1178
* Update model server doc by @ahg-g in https://github.com/llm-d/llm-d/pull/1237
* [Refactor Install]: Helm -> Kustomize for IIS by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1131
* Add workflow write by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1245
* fixing workflow call file pointers by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1248
* Added placeholder links by @ahg-g in https://github.com/llm-d/llm-d/pull/1246
* Remove workflow permit by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1260
* fix: broken links in guides and docs by @zdtsw in https://github.com/llm-d/llm-d/pull/1265
* Streamline optimized baseline guide by @liu-cong in https://github.com/llm-d/llm-d/pull/1249
* Add FULL_DUPLEX_STREAMED requirement by @roytman in https://github.com/llm-d/llm-d/pull/1271
* Update CI for optimized baseline guide by @liu-cong in https://github.com/llm-d/llm-d/pull/1268
* Consolidated Gateway guides by @ahg-g in https://github.com/llm-d/llm-d/pull/1259
* cleaup unused docs by @ahg-g in https://github.com/llm-d/llm-d/pull/1276
* fixed incorrectly setting namespace to default in the optimized-baseline  by @ahg-g in https://github.com/llm-d/llm-d/pull/1274
* [Docs] Recover precise prefix cache-aware well-lit-path by @vMaroon in https://github.com/llm-d/llm-d/pull/1272
* deps(actions): bump aquasecurity/trivy-action from 0.35.0 to 0.36.0 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1275
* Data layer docs by @ahg-g in https://github.com/llm-d/llm-d/pull/1242
* precise-prefix-cache-scheduling guide helm -> kustomize by @vMaroon in https://github.com/llm-d/llm-d/pull/1258
* Point `optimized-baseline-ocp` to the new `reusable-nightly-e2e-openshift.yaml` by @maugustosilva in https://github.com/llm-d/llm-d/pull/1278
* Add details on gke patch for optimized baseline by @liu-cong in https://github.com/llm-d/llm-d/pull/1282
* Added API and HTTP Headers References and updated the inferencepool architectural doc by @ahg-g in https://github.com/llm-d/llm-d/pull/1277
* Align TPU v6/v7 optimized baseline with Qwen3-32B by @yangligt2 in https://github.com/llm-d/llm-d/pull/1286
* fix: remove unsupported description field to fix precise-prefix-cache… by @revit13 in https://github.com/llm-d/llm-d/pull/1287
* Add kustomize to prerequisite in client-setup/README.md by @revit13 in https://github.com/llm-d/llm-d/pull/1289
* Add how to check gib is installed  by @liu-cong in https://github.com/llm-d/llm-d/pull/1283
* docs: add Before You Write Code contribution scope section by @hexfusion in https://github.com/llm-d/llm-d/pull/1214
* fix: Fix typos lint by @ying-jeanne in https://github.com/llm-d/llm-d/pull/1267
* Fix broken links to gateway guides by @ahg-g in https://github.com/llm-d/llm-d/pull/1291
* Remove hashSeed/PYTHONHASHSEED and enable speculativeIndexing in precise-prefix-cache guide by @bongwoobak in https://github.com/llm-d/llm-d/pull/1290
* fix: migrate e2e-optimized-baseline-xpu workflow from helmfile to kus… by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/1251
* Matrix of Badges by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1281
* docs: reorganize predicted latency docs and fix broken links by @kaushikmitr in https://github.com/llm-d/llm-d/pull/1247
* [Docs][Autoscaling][3/N] Comprehensive WVA doc. by @lionelvillard in https://github.com/llm-d/llm-d/pull/1176
* Ensure `precise-prefix-cache-aware` passes both CKS and OCP by @maugustosilva in https://github.com/llm-d/llm-d/pull/1296
* remove support building images from upstream branches by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1292
* revert to pull request target by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1300
* [Docs] Feature matrix and artifacts by @chcost in https://github.com/llm-d/llm-d/pull/1185
* ci: migrate e2e-prefix-cache-xpu from helmfile to kustomize by @xiaojun-zhang in https://github.com/llm-d/llm-d/pull/1297
* docs: coordinator incubation repo proposal by @nilig in https://github.com/llm-d/llm-d/pull/1293
* Add AWS EFS backend guide for tiered prefix cache storage by @sudoalok in https://github.com/llm-d/llm-d/pull/1264
* Upgrade to CUDA13 and support GB200 by @tlrmchlsmth in https://github.com/llm-d/llm-d/pull/1134
* Align WVA guide with optimized-baseline and kustomize install flow by @mamy-CS in https://github.com/llm-d/llm-d/pull/1285
* Fix matrix by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1314
* Increase timeout in simulated accelerators by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1316
* docs: add batch-gateway well-lit path documentation by @lioraron in https://github.com/llm-d/llm-d/pull/1187
* update the llm-d-fs-connector kustomizations for v0.8 by @effi-ofer in https://github.com/llm-d/llm-d/pull/1308
* [Doc][Autoscaling] Remove wrong p/d support characterization by @lionelvillard in https://github.com/llm-d/llm-d/pull/1295
* Add missing details tag in docs by @petecheslock in https://github.com/llm-d/llm-d/pull/1299
* Transitioning to llm-d Router by @ahg-g in https://github.com/llm-d/llm-d/pull/1305
* Update EPP image to v0.8.0 and add support for both 1.4 and 1.5 igw helm charts by @ahg-g in https://github.com/llm-d/llm-d/pull/1317
* [Docs] PD Guide from Helm->Kustomize by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1238
* Fix precise-prefix-cache guide: remove tokenizer plugin, fix speculativeIndexing placement by @bongwoobak in https://github.com/llm-d/llm-d/pull/1321
* Update wide-ep guide; temporarily use 0.5 image by @liu-cong in https://github.com/llm-d/llm-d/pull/1288
* ci: install kustomize in client-setup install-deps.sh by @xiaojun-zhang in https://github.com/llm-d/llm-d/pull/1319
* ci: migrate e2e-pd-xpu from helmfile to kustomize by @xiaojun-zhang in https://github.com/llm-d/llm-d/pull/1304
* quick cleanup  by @liu-cong in https://github.com/llm-d/llm-d/pull/1328
* Updated the epp design drawing by @ahg-g in https://github.com/llm-d/llm-d/pull/1331
* Added kv management umbrella docs by @ahg-g in https://github.com/llm-d/llm-d/pull/1332
* fix: use WORKFLOW_TOKEN for fork PR /test-nightly push by @clubanderson in https://github.com/llm-d/llm-d/pull/1335
* fix: remove invalid workflows permission, use WORKFLOW_TOKEN PAT by @clubanderson in https://github.com/llm-d/llm-d/pull/1336
* [0.7] remove prepare data plugin by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1337
* fix: persist-credentials false so WORKFLOW_TOKEN works for fork pushes by @clubanderson in https://github.com/llm-d/llm-d/pull/1338
* Bump deprecated kgateway path to v2.2.3 by @danehans in https://github.com/llm-d/llm-d/pull/1234
* [Docs] Polish Getting Started and Glossary by @ahg-g in https://github.com/llm-d/llm-d/pull/1333
* [Guides Storage]: Align tiered-prefix-cache storage guide with optimized-baseline by @kfirtoledo in https://github.com/llm-d/llm-d/pull/1318
* Add flow control well-lit path guide. by @LukeAVanDrie in https://github.com/llm-d/llm-d/pull/1301
* removed empty docs by @ahg-g in https://github.com/llm-d/llm-d/pull/1339
* [Guides] Clean Up README by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1341
* [Guides] TPU PD Disaggregation to Qwen 3.5 on TPU v7 by @yangligt2 in https://github.com/llm-d/llm-d/pull/1327
* [Guides] Remove TMP Doc by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1343
* [Bugfix] Offloading Connector by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1312
* [Docs] P/D Tweaks For Deprecated Features by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1351
* [Guides] Standardize H1 by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1349
* remove stale e2es by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1352
* [Release] Bump to GAIE v1.5.0 by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1353
* Fix AWS image by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1356
* [Docs] Added docs/well-lit-paths/README.md file by @ahg-g in https://github.com/llm-d/llm-d/pull/1358
* [Docs] Added workload autoscaling and async processing well-lit paths docs by @ahg-g in https://github.com/llm-d/llm-d/pull/1359
* [Docs] Clean Up Proposals by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1342
* [CI] Add predicted-latency-based-scheduling nightly E2E (OCP/GKE/CKS) by @kaushikmitr in https://github.com/llm-d/llm-d/pull/1347
* fix: add missing versions to bug report template by @liulanze in https://github.com/llm-d/llm-d/pull/1357
* [Guides] Add lightweight TPU landing page for P/D Disaggregation by @yangligt2 in https://github.com/llm-d/llm-d/pull/1346
* [PD - 0.7 release] Update Image by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1361
* [Docs]: Update docs with latest data producer plugin changes by @rahulgurnani in https://github.com/llm-d/llm-d/pull/1313
* fix: correct typos in documentation by @EzgiTastan in https://github.com/llm-d/llm-d/pull/1364
* [Build] Use Proper Wheel Variant by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1362
* Moved the note on the intention of the guides up by @ahg-g in https://github.com/llm-d/llm-d/pull/1373
* Fix HPU image name by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1374
* [Docs]: Metrics and Tracing by @madhugoutham in https://github.com/llm-d/llm-d/pull/1207
* add back hpu optimized baseline by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1378
* [Guides] Refactor Tiered Prefix Cache by @liu-cong in https://github.com/llm-d/llm-d/pull/1345
* [Build] DeepGEMM Version by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1367
* Update local build by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1382
* [Guides] Fix duplicate metrics service port in predicted-latency values by @kaushikmitr in https://github.com/llm-d/llm-d/pull/1383
* [bugfix] Fix DeepGEMM JIT in llm-d builds by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1386
* [Docs] Promote wip-docs-new to production location by @chcost in https://github.com/llm-d/llm-d/pull/1340
* deps(actions): bump github/codeql-action from 3 to 4 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1394
* deps(actions): bump docker/login-action from 3 to 4 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1395
* deps(actions): bump docker/setup-buildx-action from 3 to 4 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1396
* deps(actions): bump docker/build-push-action from 6 to 7 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1397
* deps(actions): bump aquasecurity/trivy-action from 0.35.0 to 0.36.0 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1398
* update: clean deprecated env variable for vllm to build AVX by @zdtsw in https://github.com/llm-d/llm-d/pull/1231
* Polishing docs and drawings by @ahg-g in https://github.com/llm-d/llm-d/pull/1404
* ci: migrate nightly GKE pd disaggregation test to Kustomize & Gateway… by @yangligt2 in https://github.com/llm-d/llm-d/pull/1403
* Fix: nightly CI pipeline fails due to broken Helm values path by @weizhoublue in https://github.com/llm-d/llm-d/pull/1388
* Fix/predicted latency duplicate metrics port by @kaushikmitr in https://github.com/llm-d/llm-d/pull/1406
* Fix MDX syntax error in optimized-baseline guide by @chcost in https://github.com/llm-d/llm-d/pull/1405
* [Docs] Migrate Async Processor Helmfile -> Direct Helm Application by @shimib in https://github.com/llm-d/llm-d/pull/1366
* Add CNCF Sandbox project references to README by @alexagriffith in https://github.com/llm-d/llm-d/pull/1375
* Enable `/test-nightly build-image` by @maugustosilva in https://github.com/llm-d/llm-d/pull/1409
* one build approval per set of chagnes in a PR by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1413
* chore(xpu): bump VLLM_XPU_COMMIT_SHA to v0.19.1 by @xiaojun-zhang in https://github.com/llm-d/llm-d/pull/1418
* enable security events on nightly-permissions workflow by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1410
* Simplified EPP components headers by @ahg-g in https://github.com/llm-d/llm-d/pull/1421
* Make active-active HA the default for precise-prefix-cache-aware by @vMaroon in https://github.com/llm-d/llm-d/pull/1415
* drop ci for simulated accelerators by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1387
* docs: document feature gate removal process by @rahulgurnani in https://github.com/llm-d/llm-d/pull/1419
* [Docs] Make sure all references are relative by @ahg-g in https://github.com/llm-d/llm-d/pull/1407
* deps(docker): bump LMCache from v0.4.1 to v0.4.4-cu13 by @liulanze in https://github.com/llm-d/llm-d/pull/1368
* Added a how to configure section to the EPP docs by @ahg-g in https://github.com/llm-d/llm-d/pull/1425
* Remove wva helmfile resources by @mamy-CS in https://github.com/llm-d/llm-d/pull/1424
* Fix InferencePool diagram reference by @chcost in https://github.com/llm-d/llm-d/pull/1416
* [Guides] Add TPU KV cache offloading support to tiered prefix cache by @dannawang0221 in https://github.com/llm-d/llm-d/pull/1411
* [Docs] Clean Up Artifacts by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1370
* Unified drawings color theme, sizes and placement by @ahg-g in https://github.com/llm-d/llm-d/pull/1431
* Added more clarifications on proxy terminology and its relation to cloud load balancers by @ahg-g in https://github.com/llm-d/llm-d/pull/1435
* Updated feature matrix by @ahg-g in https://github.com/llm-d/llm-d/pull/1436
* refine the terminology under router by @ahg-g in https://github.com/llm-d/llm-d/pull/1437
* Improve clarity of RDMA and networking documentation by @alexagriffith in https://github.com/llm-d/llm-d/pull/1385
* fixed typos by @ahg-g in https://github.com/llm-d/llm-d/pull/1438
* remove upstream_versions by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1439
* added nightly badges for p/d on gke and predicted latency by @ahg-g in https://github.com/llm-d/llm-d/pull/1432
* Add "llm-d.ai/subguide" tracking labels for Prefix Cache Offloading by @adinilfeld in https://github.com/llm-d/llm-d/pull/1428
* Add a nightly P/D on GKE badge to the main matrix by @maugustosilva in https://github.com/llm-d/llm-d/pull/1444
* AMD guides and docker update by @vcave in https://github.com/llm-d/llm-d/pull/1443
* Bump Istio from 1.29.1 to 1.29.2 by @liulanze in https://github.com/llm-d/llm-d/pull/1447
* Fix broken link in openshift-aws documentation by @petecheslock in https://github.com/llm-d/llm-d/pull/1451
* Attempt to deploy full Qwen3-32B for tiered-prefix-cache by @maugustosilva in https://github.com/llm-d/llm-d/pull/1445
* upgrade to CNCF runners by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1455
* add tiered prefix cache nightly for gke by @liu-cong in https://github.com/llm-d/llm-d/pull/1454
* Revert "upgrade to CNCF runners" by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1458
* docs: disable OpenShift predicted-latency nightly by @kaushikmitr in https://github.com/llm-d/llm-d/pull/1452
* optimized-baseline: mount /.triton and /.config emptyDirs for non-root pods by @rdwj in https://github.com/llm-d/llm-d/pull/1450
* Bump agentgateway from v1.0.0 to v1.1.0 by @liulanze in https://github.com/llm-d/llm-d/pull/1459
* Rename resources-new to resources by @chcost in https://github.com/llm-d/llm-d/pull/1460
* Add GKE CPU offloading LMCache nightly, rename workflows, and fix GPU requirements by @liu-cong in https://github.com/llm-d/llm-d/pull/1457
* [Guides] update precise prefix-cache routing guide's benchmark data by @vMaroon in https://github.com/llm-d/llm-d/pull/1462
* feat: modularize GKE NCCL tuner patch into shared component by @liu-cong in https://github.com/llm-d/llm-d/pull/1461
* Various fixes to the guides by @ahg-g in https://github.com/llm-d/llm-d/pull/1467
* (Guides) refresh scheduling-guides benchmark reports with v0.8.0 numbers by @vMaroon in https://github.com/llm-d/llm-d/pull/1463
* nightlies should comment status on PR by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1465
* remove feature-matrix.md by @ahg-g in https://github.com/llm-d/llm-d/pull/1474
* Updated GKE's supported paths by @ahg-g in https://github.com/llm-d/llm-d/pull/1475
* Updated GKE provider docs on what paths are supported on what hardware by @ahg-g in https://github.com/llm-d/llm-d/pull/1477
* [Bugfix] Fix WideEP Build + IMA by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1448
* removed redundant nightly tests badges by @ahg-g in https://github.com/llm-d/llm-d/pull/1476
* Update GKE PD nightly by @liu-cong in https://github.com/llm-d/llm-d/pull/1456
* [Guides] Bump WideEP by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1324
* point to the async processor well lit path instead of the guide directly by @ahg-g in https://github.com/llm-d/llm-d/pull/1479
* [Guides | Bugfix] Consistency + Fix HTTPRoutes in Gateway Mode by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1348
* Add recipe for llm-d-fs connector storage offloading with Lustre by @Sneha-at in https://github.com/llm-d/llm-d/pull/1427
* Polish the main README.md file by @ahg-g in https://github.com/llm-d/llm-d/pull/1482
* Fix: PD disaggregation CKS nightly values by @weizhoublue in https://github.com/llm-d/llm-d/pull/1484
* Move badge matrix to release by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1481
* Add release template to repository by @maugustosilva in https://github.com/llm-d/llm-d/pull/1487
* optimized-baseline README.md fix by @Amit-Berman in https://github.com/llm-d/llm-d/pull/1486
* Final batch of CI/CD fixes before release v0.7.0 by @maugustosilva in https://github.com/llm-d/llm-d/pull/1480
* Switch `llm-d-cuda` on `wide-ep-lws` to `v0.7.0` by @maugustosilva in https://github.com/llm-d/llm-d/pull/1489
* Add additional steps for release process. by @maugustosilva in https://github.com/llm-d/llm-d/pull/1491
* Add documentation release branch step to release template by @chcost in https://github.com/llm-d/llm-d/pull/1492
* Add Performance Highlights, v0.7 news, and badge bump to README by @chcost in https://github.com/llm-d/llm-d/pull/1483
* Prep v0.7.0 by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1270
* fix pd.values by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1493

## New Contributors
* @hhk7734 made their first contribution in https://github.com/llm-d/llm-d/pull/1111
* @sharvil10 made their first contribution in https://github.com/llm-d/llm-d/pull/1101
* @madhugoutham made their first contribution in https://github.com/llm-d/llm-d/pull/1126
* @hexfusion made their first contribution in https://github.com/llm-d/llm-d/pull/1123
* @LukeAVanDrie made their first contribution in https://github.com/llm-d/llm-d/pull/1127
* @ianliuy made their first contribution in https://github.com/llm-d/llm-d/pull/1135
* @amacaskill made their first contribution in https://github.com/llm-d/llm-d/pull/1102
* @rebel-jinmoo made their first contribution in https://github.com/llm-d/llm-d/pull/1115
* @praveingk made their first contribution in https://github.com/llm-d/llm-d/pull/1181
* @nilig made their first contribution in https://github.com/llm-d/llm-d/pull/1184
* @revit13 made their first contribution in https://github.com/llm-d/llm-d/pull/1287
* @ying-jeanne made their first contribution in https://github.com/llm-d/llm-d/pull/1267
* @xiaojun-zhang made their first contribution in https://github.com/llm-d/llm-d/pull/1297
* @sudoalok made their first contribution in https://github.com/llm-d/llm-d/pull/1264
* @lioraron made their first contribution in https://github.com/llm-d/llm-d/pull/1187
* @liulanze made their first contribution in https://github.com/llm-d/llm-d/pull/1357
* @rahulgurnani made their first contribution in https://github.com/llm-d/llm-d/pull/1313
* @EzgiTastan made their first contribution in https://github.com/llm-d/llm-d/pull/1364
* @weizhoublue made their first contribution in https://github.com/llm-d/llm-d/pull/1388
* @alexagriffith made their first contribution in https://github.com/llm-d/llm-d/pull/1375
* @adinilfeld made their first contribution in https://github.com/llm-d/llm-d/pull/1428
* @rdwj made their first contribution in https://github.com/llm-d/llm-d/pull/1450
* @Amit-Berman made their first contribution in https://github.com/llm-d/llm-d/pull/1486

**Full Changelog**: https://github.com/llm-d/llm-d/compare/v0.6...v0.7.0

## v0.8.0 (2026-06-24)

## LLM-D v0.8.0 Component Summary

> **Themes:** solidify CI coverage & project operations, expand accelerator coverage, graduate multimodal/batch/flow-control to production, introduce initial RL support.

| Component | Version | Previous Version | Type | Notes |
|-----------|---------|------------------|------|-------|
| llm-d/llm-d-router-endpoint-picker | `v0.9.0` | `v0.8.0` | Image + Helm Chart | Core EPP image (renamed from llm-d-inference-scheduler) |
| llm-d/llm-d-router-disagg-sidecar | `v0.9.0` | `v0.8.0` | Image | P/D routing sidecar (renamed from llm-d-routing-sidecar) |
| llm-d/llm-d-uds-tokenizer | `vllm-v0.23.0` | `vllm-v0.19.1` | Image | Tokenizer sidecar aligned with vLLM version |
| llm-d/llm-d-kv-cache | `v0.9.0` | `v0.8.0` | Library | HMA support, storage events, multi-tier offloading |
| llm-d/llm-d-inference-sim | `v0.9.2` | `v0.8.2` | Image | Multimodal support, Mooncake bootstrap, configurable latency |
| llm-d/llm-d-cuda | `v0.8.0` | `v0.7.0` | Image | vLLM v0.23.0, CUDA 13.0.2 |
| llm-d/llm-d-aws (EFA) | `v0.8.0` | `v0.7.0` | Image | |
| llm-d/llm-d-hpu | `v0.8.0` | `v0.7.0` | Image | |
| llm-d/llm-d-kv-cache/llmd_fs_backend_connector | `v0.23` | `v0.19.1` | Wheel installed in `llm-d` | Migrated to vLLM 0.23.0 offload API |
| llm-d/llm-d-benchmark | `v0.7.0` | `v0.6.8.1` | Image | Benchmark workload launcher |
| llm-d/llm-d-workload-variant-autoscaler | `v0.8.0` | `v0.7.0` | Helm Chart + Image | CRD migration to llm-d.ai API group, improved observability |
| vllm-project/vllm | `v0.23.0` | `v0.19.1` | Wheel installed in `llm-d` | Confirmed by @Gregory-Pereira and @tessapham |
| kubernetes-sigs/gateway-api-inference-extension | `v1.5.0` | `v1.5.0` | Helm Chart | Charts now published from llm-d-router OCI registry |

### Upstream vLLM Images (replacing llm-d-built images)

> Per PR [#1791](https://github.com/llm-d/llm-d/pull/1791), the following platforms now use upstream vLLM images directly instead of llm-d-built custom images:

| Platform | New Image | Tag | Previous llm-d Image |
|----------|-----------|-----|---------------------|
| GPU (CUDA) | `vllm/vllm-openai` | `v0.23.0` | `ghcr.io/llm-d/llm-d-cuda` (still available for advanced builds) |
| ROCm (AMD) | `vllm/vllm-openai-rocm` | | `ghcr.io/llm-d/llm-d-rocm` |
| CPU | `ghcr.io/llm-d/llm-d-cpu` | `v0.7.0` | Same image, version bump |
| XPU (Intel) | `vllm/vllm-openai` | `v0.23.0` | `ghcr.io/llm-d/llm-d-xpu` |

---

## Infrastructure Changes

| Component | Version | Previous Version | Notes |
|-----------|---------|------------------|-------|
| Gateway API | `v1.5.1` | `v1.5.1` | No change |
| Istio | `1.29.4` | `1.29.1` | Patch update |
| kgateway (agentgateway) | `v2.3.3` | `v2.2.1` | |

---

## Deprecated / Removed Components

| Component | Status | Replaced By |
|-----------|--------|-------------|
| llm-d/llm-d-inference-scheduler | **Renamed** | `ghcr.io/llm-d/llm-d-router-endpoint-picker` |
| llm-d/llm-d-routing-sidecar | **Renamed** | `ghcr.io/llm-d/llm-d-router-disagg-sidecar` |
| llm-d/llm-d-cuda (debug) | **Removed** | N/A |
| llm-d/llm-d-cuda-gb200 | **Removed** | N/A |
| llm-d/llm-d-xpu | **Removed** | `vllm/vllm-openai` |
| llm-d/llm-d-rocm | **Removed** | `vllm/vllm-openai-rocm` |

---

## New Capabilities in This Release

| Capability | Component(s) | Status |
|------------|--------------|--------|
| Multi-modal serving (production) | llm-d-router, llm-d-inference-sim | Graduated |
| Batch gateway (production) | llm-d-router | Graduated |
| Flow control (production) | llm-d-router | Graduated |
| Non-Kubernetes mode (RL/Slurm) | llm-d-router (FileDiscovery plugin) | New |
| Responses API support | llm-d-router | New |
| Multi-tier KV offloading (CPU → storage) | llm-d-kv-cache | New |
| HMA (Heterogeneous Memory Allocation) support | llm-d-kv-cache, fs-connector | New |
| DP-Aware scheduling | llm-d-router | Graduating |
| Mooncake connector | llm-d-kv-cache | New |
| Predicted latency scheduling | llm-d-router | New |
| Agentic workload routing | llm-d-router | New |
| TPU nightly tests | CI/CD | New |

## What's Changed
* Simplify WVA guide test by @lionelvillard in https://github.com/llm-d/llm-d/pull/1072
* fix concurrency group to sha not PR by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1073
* fix block-size alignment by @vMaroon in https://github.com/llm-d/llm-d/pull/1084
* Revise maturity status and TPU VM type details by @seanhorgan in https://github.com/llm-d/llm-d/pull/1085
* Fix formatting of automated test status in README by @seanhorgan in https://github.com/llm-d/llm-d/pull/1087
* Fix image on pd user guide by @Edwinhr716 in https://github.com/llm-d/llm-d/pull/1086
* Updated maturity testing level on all guides by @maugustosilva in https://github.com/llm-d/llm-d/pull/1094
* Skip latest tag for release candidates by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1034
* fix(xpu): enable TP=2 for Qwen3-32B for fixing XPU prefix-cache test failed by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/1081
* [guides] Add a commented `priorityClassName` for use in nightly CI/CD by @maugustosilva in https://github.com/llm-d/llm-d/pull/1062
* deps(actions): bump docker/build-push-action from 6 to 7 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1089
* deps(actions): bump actions/github-script from 7 to 8 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1091
* deps(actions): bump google-github-actions/auth from 2.1.12 to 3.0.0 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1090
* deps(actions): bump dorny/paths-filter from 3 to 4 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1092
* deps(actions): bump docker/login-action from 3 to 4 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1093
* Add shared drive for sig-rl by @petecheslock in https://github.com/llm-d/llm-d/pull/1109
* Fix llm-d performance dashboard queries by @danehans in https://github.com/llm-d/llm-d/pull/1098
* Fix/e2e validate single curl pod by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/1078
* Add Moreh as a contributor to the adopters list by @hhk7734 in https://github.com/llm-d/llm-d/pull/1111
* Update guides with status badges. by @maugustosilva in https://github.com/llm-d/llm-d/pull/1110
* fix: use vllmServe modelCommand in precise-prefix-cache-aware XPU values by @sharvil10 in https://github.com/llm-d/llm-d/pull/1101
* Add deployment health-check smoke test for llm-d clusters by @lisperz in https://github.com/llm-d/llm-d/pull/767
* [1/N] Documentation Revamp by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1100
* fix: split vLLM command array and fill in quickstart TODOs by @madhugoutham in https://github.com/llm-d/llm-d/pull/1126
* add OCI well-lit-path for P/D disaggregation by @hexfusion in https://github.com/llm-d/llm-d/pull/1123
* fix: use the proper git ref for tag extraction by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1133
* Update latency-predictor.md diagram by @LukeAVanDrie in https://github.com/llm-d/llm-d/pull/1127
* docs: fix typos detected by nightly scan (issue #1056) by @ianliuy in https://github.com/llm-d/llm-d/pull/1135
* [Docs][4/N] Update architecture/core/epp/scheduling.md docs by @ahg-g in https://github.com/llm-d/llm-d/pull/1122
* [2/N] Proxy Doc by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1121
* [Docs][6/N]: add Istio gateway setup guide by @madhugoutham in https://github.com/llm-d/llm-d/pull/1146
* docs: add EPP flow control reference by @LukeAVanDrie in https://github.com/llm-d/llm-d/pull/1130
* [Docs] [3/N] Add Disaggregation Architecture Docs by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1138
* [Docs] Add glossary page by @ianliuy in https://github.com/llm-d/llm-d/pull/1148
* Add agentgateway guide by @danehans in https://github.com/llm-d/llm-d/pull/1159
* fix(docs): correct typos from nightly scan, add false-positive config by @ianliuy in https://github.com/llm-d/llm-d/pull/1160
* [Docs] Guides Directory Cleanup by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1163
* [Docs][EPP] Doc for request handling and control by @zetxqx in https://github.com/llm-d/llm-d/pull/1128
* fix(docker): add LIBRARY_PATH and ldconfig to CUDA runtime stage by @ianliuy in https://github.com/llm-d/llm-d/pull/1147
* Update ms-inference-scheduling/values_tpu_v7.yaml to use RunAI model streamer by @amacaskill in https://github.com/llm-d/llm-d/pull/1102
* deps(actions): bump hashicorp/setup-terraform from 3.1.2 to 4.0.0 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1153
* deps(actions): bump aws-actions/configure-aws-credentials from 4.3.1 to 6.1.0 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1152
* deps(actions): bump actions/github-script from 8 to 9 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1150
* deps(actions): bump j178/prek-action from 1 to 2 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1151
* deps(actions): bump actions/upload-artifact from 6 to 7 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1149
* [Docs] Remove `customizing-a-guide.md` by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1165
* [Docs] Move `guides/benchmarks` to `helpers/benchmark.md` by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1164
* [Docs][Istio] Align to AgentGateway Doc by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1161
* deps(docker): bump gdrcopy from v2.5.1 to v2.5.2 by @ianliuy in https://github.com/llm-d/llm-d/pull/1171
* [Docs] Envoy Proxy -> GAIE-Conformant Proxy by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1162
* Updated the basic architecture diagram by @ahg-g in https://github.com/llm-d/llm-d/pull/1173
* [Docs] Fix Broken Quickstart Links by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1175
* [Docs] Remove guide/prereq/infrastructure by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1168
* Added GKE gateway guide by @ahg-g in https://github.com/llm-d/llm-d/pull/1174
* [Docs] Move Client Tools from Guides --> Helpers by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1167
* feat: add Rebellions as a supported accelerator vendor by @rebel-jinmoo in https://github.com/llm-d/llm-d/pull/1115
* docs: rewrite predicted latency architecture and add well-lit path by @kaushikmitr in https://github.com/llm-d/llm-d/pull/1166
* [Docs][Autoscaling][2/N] hpa/keda vs hpa design choices/features by @lionelvillard in https://github.com/llm-d/llm-d/pull/1157
* [Docs][7/N] KV Indexer by @vMaroon in https://github.com/llm-d/llm-d/pull/1143
* [Docs][autoscaling][1/N] Autoscaling intro by @lionelvillard in https://github.com/llm-d/llm-d/pull/1145
* [Docs] Refine RDMA docs by @praveingk in https://github.com/llm-d/llm-d/pull/1181
* Fixup merge conflict markers in `tiered-prefix-cache/storage/README.md` by @tlrmchlsmth in https://github.com/llm-d/llm-d/pull/1190
* [Docs] fix broken link by @lionelvillard in https://github.com/llm-d/llm-d/pull/1191
* docs: llm-d-inference-payload-processor proposal by @nilig in https://github.com/llm-d/llm-d/pull/1184
* [Docs] Well Lit Paths Doc by @chcost in https://github.com/llm-d/llm-d/pull/1156
* Tweaks to the latency predictor docs by @ahg-g in https://github.com/llm-d/llm-d/pull/1201
* [Docs] Restructure Predicted Latency Well Lit Path Doc by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1200
* [Docs][Autoscaling][4/N] first pass at the HPA+IGW doc by @lionelvillard in https://github.com/llm-d/llm-d/pull/1192
* Updating native HPA-based autoscaling guide to reference EPP instead of IGW by @ahg-g in https://github.com/llm-d/llm-d/pull/1212
* [Docs] Rename Well-Lit-Paths -> Guides, Guides -> Resources by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1199
* deps(actions): bump actions/checkout from 4 to 6 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1221
* deps(actions): bump helm/kind-action from 1.12.0 to 1.14.0 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1220
* deps(actions): bump actions/download-artifact from 4 to 8 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1219
* [Docs][8/N] KV Offloader Doc by @vMaroon in https://github.com/llm-d/llm-d/pull/1144
* [Docs] Fix Various Nits by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1215
* Update TPU recommendations in README by @seanhorgan in https://github.com/llm-d/llm-d/pull/1213
* Fix typos by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1223
* [Docs] Remove envoy reference by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1225
* Proposal doc for Inference Resilience Operator by @aishukamal in https://github.com/llm-d/llm-d/pull/984
* docs(epp): polish architecture and configuration guides by @LukeAVanDrie in https://github.com/llm-d/llm-d/pull/1227
* [Docs] Consolidate Gateway Docs To Use YAML by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1178
* Update model server doc by @ahg-g in https://github.com/llm-d/llm-d/pull/1237
* [Refactor Install]: Helm -> Kustomize for IIS by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1131
* Add workflow write by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1245
* fixing workflow call file pointers by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1248
* Added placeholder links by @ahg-g in https://github.com/llm-d/llm-d/pull/1246
* Remove workflow permit by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1260
* fix: broken links in guides and docs by @zdtsw in https://github.com/llm-d/llm-d/pull/1265
* Streamline optimized baseline guide by @liu-cong in https://github.com/llm-d/llm-d/pull/1249
* Add FULL_DUPLEX_STREAMED requirement by @roytman in https://github.com/llm-d/llm-d/pull/1271
* Update CI for optimized baseline guide by @liu-cong in https://github.com/llm-d/llm-d/pull/1268
* Consolidated Gateway guides by @ahg-g in https://github.com/llm-d/llm-d/pull/1259
* cleaup unused docs by @ahg-g in https://github.com/llm-d/llm-d/pull/1276
* fixed incorrectly setting namespace to default in the optimized-baseline  by @ahg-g in https://github.com/llm-d/llm-d/pull/1274
* [Docs] Recover precise prefix cache-aware well-lit-path by @vMaroon in https://github.com/llm-d/llm-d/pull/1272
* deps(actions): bump aquasecurity/trivy-action from 0.35.0 to 0.36.0 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1275
* Data layer docs by @ahg-g in https://github.com/llm-d/llm-d/pull/1242
* precise-prefix-cache-scheduling guide helm -> kustomize by @vMaroon in https://github.com/llm-d/llm-d/pull/1258
* Point `optimized-baseline-ocp` to the new `reusable-nightly-e2e-openshift.yaml` by @maugustosilva in https://github.com/llm-d/llm-d/pull/1278
* Add details on gke patch for optimized baseline by @liu-cong in https://github.com/llm-d/llm-d/pull/1282
* Added API and HTTP Headers References and updated the inferencepool architectural doc by @ahg-g in https://github.com/llm-d/llm-d/pull/1277
* Align TPU v6/v7 optimized baseline with Qwen3-32B by @yangligt2 in https://github.com/llm-d/llm-d/pull/1286
* fix: remove unsupported description field to fix precise-prefix-cache… by @revit13 in https://github.com/llm-d/llm-d/pull/1287
* Add kustomize to prerequisite in client-setup/README.md by @revit13 in https://github.com/llm-d/llm-d/pull/1289
* Add how to check gib is installed  by @liu-cong in https://github.com/llm-d/llm-d/pull/1283
* docs: add Before You Write Code contribution scope section by @hexfusion in https://github.com/llm-d/llm-d/pull/1214
* fix: Fix typos lint by @ying-jeanne in https://github.com/llm-d/llm-d/pull/1267
* Fix broken links to gateway guides by @ahg-g in https://github.com/llm-d/llm-d/pull/1291
* Remove hashSeed/PYTHONHASHSEED and enable speculativeIndexing in precise-prefix-cache guide by @bongwoobak in https://github.com/llm-d/llm-d/pull/1290
* fix: migrate e2e-optimized-baseline-xpu workflow from helmfile to kus… by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/1251
* Matrix of Badges by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1281
* docs: reorganize predicted latency docs and fix broken links by @kaushikmitr in https://github.com/llm-d/llm-d/pull/1247
* [Docs][Autoscaling][3/N] Comprehensive WVA doc. by @lionelvillard in https://github.com/llm-d/llm-d/pull/1176
* Ensure `precise-prefix-cache-aware` passes both CKS and OCP by @maugustosilva in https://github.com/llm-d/llm-d/pull/1296
* remove support building images from upstream branches by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1292
* revert to pull request target by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1300
* [Docs] Feature matrix and artifacts by @chcost in https://github.com/llm-d/llm-d/pull/1185
* ci: migrate e2e-prefix-cache-xpu from helmfile to kustomize by @xiaojun-zhang in https://github.com/llm-d/llm-d/pull/1297
* docs: coordinator incubation repo proposal by @nilig in https://github.com/llm-d/llm-d/pull/1293
* Add AWS EFS backend guide for tiered prefix cache storage by @sudoalok in https://github.com/llm-d/llm-d/pull/1264
* Upgrade to CUDA13 and support GB200 by @tlrmchlsmth in https://github.com/llm-d/llm-d/pull/1134
* Align WVA guide with optimized-baseline and kustomize install flow by @mamy-CS in https://github.com/llm-d/llm-d/pull/1285
* Fix matrix by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1314
* Increase timeout in simulated accelerators by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1316
* docs: add batch-gateway well-lit path documentation by @lioraron in https://github.com/llm-d/llm-d/pull/1187
* update the llm-d-fs-connector kustomizations for v0.8 by @effi-ofer in https://github.com/llm-d/llm-d/pull/1308
* [Doc][Autoscaling] Remove wrong p/d support characterization by @lionelvillard in https://github.com/llm-d/llm-d/pull/1295
* Add missing details tag in docs by @petecheslock in https://github.com/llm-d/llm-d/pull/1299
* Transitioning to llm-d Router by @ahg-g in https://github.com/llm-d/llm-d/pull/1305
* Update EPP image to v0.8.0 and add support for both 1.4 and 1.5 igw helm charts by @ahg-g in https://github.com/llm-d/llm-d/pull/1317
* [Docs] PD Guide from Helm->Kustomize by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1238
* Fix precise-prefix-cache guide: remove tokenizer plugin, fix speculativeIndexing placement by @bongwoobak in https://github.com/llm-d/llm-d/pull/1321
* Update wide-ep guide; temporarily use 0.5 image by @liu-cong in https://github.com/llm-d/llm-d/pull/1288
* ci: install kustomize in client-setup install-deps.sh by @xiaojun-zhang in https://github.com/llm-d/llm-d/pull/1319
* ci: migrate e2e-pd-xpu from helmfile to kustomize by @xiaojun-zhang in https://github.com/llm-d/llm-d/pull/1304
* quick cleanup  by @liu-cong in https://github.com/llm-d/llm-d/pull/1328
* Updated the epp design drawing by @ahg-g in https://github.com/llm-d/llm-d/pull/1331
* Added kv management umbrella docs by @ahg-g in https://github.com/llm-d/llm-d/pull/1332
* fix: use WORKFLOW_TOKEN for fork PR /test-nightly push by @clubanderson in https://github.com/llm-d/llm-d/pull/1335
* fix: remove invalid workflows permission, use WORKFLOW_TOKEN PAT by @clubanderson in https://github.com/llm-d/llm-d/pull/1336
* [0.7] remove prepare data plugin by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1337
* fix: persist-credentials false so WORKFLOW_TOKEN works for fork pushes by @clubanderson in https://github.com/llm-d/llm-d/pull/1338
* Bump deprecated kgateway path to v2.2.3 by @danehans in https://github.com/llm-d/llm-d/pull/1234
* [Docs] Polish Getting Started and Glossary by @ahg-g in https://github.com/llm-d/llm-d/pull/1333
* [Guides Storage]: Align tiered-prefix-cache storage guide with optimized-baseline by @kfirtoledo in https://github.com/llm-d/llm-d/pull/1318
* Add flow control well-lit path guide. by @LukeAVanDrie in https://github.com/llm-d/llm-d/pull/1301
* removed empty docs by @ahg-g in https://github.com/llm-d/llm-d/pull/1339
* [Guides] Clean Up README by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1341
* [Guides] TPU PD Disaggregation to Qwen 3.5 on TPU v7 by @yangligt2 in https://github.com/llm-d/llm-d/pull/1327
* [Guides] Remove TMP Doc by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1343
* [Bugfix] Offloading Connector by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1312
* [Docs] P/D Tweaks For Deprecated Features by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1351
* [Guides] Standardize H1 by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1349
* remove stale e2es by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1352
* [Release] Bump to GAIE v1.5.0 by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1353
* Fix AWS image by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1356
* [Docs] Added docs/well-lit-paths/README.md file by @ahg-g in https://github.com/llm-d/llm-d/pull/1358
* [Docs] Added workload autoscaling and async processing well-lit paths docs by @ahg-g in https://github.com/llm-d/llm-d/pull/1359
* [Docs] Clean Up Proposals by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1342
* [CI] Add predicted-latency-based-scheduling nightly E2E (OCP/GKE/CKS) by @kaushikmitr in https://github.com/llm-d/llm-d/pull/1347
* fix: add missing versions to bug report template by @liulanze in https://github.com/llm-d/llm-d/pull/1357
* [Guides] Add lightweight TPU landing page for P/D Disaggregation by @yangligt2 in https://github.com/llm-d/llm-d/pull/1346
* [PD - 0.7 release] Update Image by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1361
* [Docs]: Update docs with latest data producer plugin changes by @rahulgurnani in https://github.com/llm-d/llm-d/pull/1313
* fix: correct typos in documentation by @EzgiTastan in https://github.com/llm-d/llm-d/pull/1364
* [Build] Use Proper Wheel Variant by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1362
* Moved the note on the intention of the guides up by @ahg-g in https://github.com/llm-d/llm-d/pull/1373
* Fix HPU image name by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1374
* [Docs]: Metrics and Tracing by @madhugoutham in https://github.com/llm-d/llm-d/pull/1207
* add back hpu optimized baseline by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1378
* [Guides] Refactor Tiered Prefix Cache by @liu-cong in https://github.com/llm-d/llm-d/pull/1345
* [Build] DeepGEMM Version by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1367
* Update local build by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1382
* [Guides] Fix duplicate metrics service port in predicted-latency values by @kaushikmitr in https://github.com/llm-d/llm-d/pull/1383
* [bugfix] Fix DeepGEMM JIT in llm-d builds by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1386
* [Docs] Promote wip-docs-new to production location by @chcost in https://github.com/llm-d/llm-d/pull/1340
* deps(actions): bump github/codeql-action from 3 to 4 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1394
* deps(actions): bump docker/login-action from 3 to 4 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1395
* deps(actions): bump docker/setup-buildx-action from 3 to 4 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1396
* deps(actions): bump docker/build-push-action from 6 to 7 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1397
* deps(actions): bump aquasecurity/trivy-action from 0.35.0 to 0.36.0 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1398
* update: clean deprecated env variable for vllm to build AVX by @zdtsw in https://github.com/llm-d/llm-d/pull/1231
* Polishing docs and drawings by @ahg-g in https://github.com/llm-d/llm-d/pull/1404
* ci: migrate nightly GKE pd disaggregation test to Kustomize & Gateway… by @yangligt2 in https://github.com/llm-d/llm-d/pull/1403
* Fix: nightly CI pipeline fails due to broken Helm values path by @weizhoublue in https://github.com/llm-d/llm-d/pull/1388
* Fix/predicted latency duplicate metrics port by @kaushikmitr in https://github.com/llm-d/llm-d/pull/1406
* Fix MDX syntax error in optimized-baseline guide by @chcost in https://github.com/llm-d/llm-d/pull/1405
* [Docs] Migrate Async Processor Helmfile -> Direct Helm Application by @shimib in https://github.com/llm-d/llm-d/pull/1366
* Add CNCF Sandbox project references to README by @alexagriffith in https://github.com/llm-d/llm-d/pull/1375
* Enable `/test-nightly build-image` by @maugustosilva in https://github.com/llm-d/llm-d/pull/1409
* one build approval per set of chagnes in a PR by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1413
* chore(xpu): bump VLLM_XPU_COMMIT_SHA to v0.19.1 by @xiaojun-zhang in https://github.com/llm-d/llm-d/pull/1418
* enable security events on nightly-permissions workflow by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1410
* Simplified EPP components headers by @ahg-g in https://github.com/llm-d/llm-d/pull/1421
* Make active-active HA the default for precise-prefix-cache-aware by @vMaroon in https://github.com/llm-d/llm-d/pull/1415
* drop ci for simulated accelerators by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1387
* docs: document feature gate removal process by @rahulgurnani in https://github.com/llm-d/llm-d/pull/1419
* [Docs] Make sure all references are relative by @ahg-g in https://github.com/llm-d/llm-d/pull/1407
* deps(docker): bump LMCache from v0.4.1 to v0.4.4-cu13 by @liulanze in https://github.com/llm-d/llm-d/pull/1368
* Added a how to configure section to the EPP docs by @ahg-g in https://github.com/llm-d/llm-d/pull/1425
* Remove wva helmfile resources by @mamy-CS in https://github.com/llm-d/llm-d/pull/1424
* Fix InferencePool diagram reference by @chcost in https://github.com/llm-d/llm-d/pull/1416
* [Guides] Add TPU KV cache offloading support to tiered prefix cache by @dannawang0221 in https://github.com/llm-d/llm-d/pull/1411
* [Docs] Clean Up Artifacts by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1370
* Unified drawings color theme, sizes and placement by @ahg-g in https://github.com/llm-d/llm-d/pull/1431
* Added more clarifications on proxy terminology and its relation to cloud load balancers by @ahg-g in https://github.com/llm-d/llm-d/pull/1435
* Updated feature matrix by @ahg-g in https://github.com/llm-d/llm-d/pull/1436
* refine the terminology under router by @ahg-g in https://github.com/llm-d/llm-d/pull/1437
* Improve clarity of RDMA and networking documentation by @alexagriffith in https://github.com/llm-d/llm-d/pull/1385
* fixed typos by @ahg-g in https://github.com/llm-d/llm-d/pull/1438
* remove upstream_versions by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1439
* added nightly badges for p/d on gke and predicted latency by @ahg-g in https://github.com/llm-d/llm-d/pull/1432
* Add "llm-d.ai/subguide" tracking labels for Prefix Cache Offloading by @adinilfeld in https://github.com/llm-d/llm-d/pull/1428
* Add a nightly P/D on GKE badge to the main matrix by @maugustosilva in https://github.com/llm-d/llm-d/pull/1444
* AMD guides and docker update by @vcave in https://github.com/llm-d/llm-d/pull/1443
* Bump Istio from 1.29.1 to 1.29.2 by @liulanze in https://github.com/llm-d/llm-d/pull/1447
* Fix broken link in openshift-aws documentation by @petecheslock in https://github.com/llm-d/llm-d/pull/1451
* Attempt to deploy full Qwen3-32B for tiered-prefix-cache by @maugustosilva in https://github.com/llm-d/llm-d/pull/1445
* upgrade to CNCF runners by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1455
* add tiered prefix cache nightly for gke by @liu-cong in https://github.com/llm-d/llm-d/pull/1454
* Revert "upgrade to CNCF runners" by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1458
* docs: disable OpenShift predicted-latency nightly by @kaushikmitr in https://github.com/llm-d/llm-d/pull/1452
* optimized-baseline: mount /.triton and /.config emptyDirs for non-root pods by @rdwj in https://github.com/llm-d/llm-d/pull/1450
* Bump agentgateway from v1.0.0 to v1.1.0 by @liulanze in https://github.com/llm-d/llm-d/pull/1459
* Rename resources-new to resources by @chcost in https://github.com/llm-d/llm-d/pull/1460
* Add GKE CPU offloading LMCache nightly, rename workflows, and fix GPU requirements by @liu-cong in https://github.com/llm-d/llm-d/pull/1457
* [Guides] update precise prefix-cache routing guide's benchmark data by @vMaroon in https://github.com/llm-d/llm-d/pull/1462
* feat: modularize GKE NCCL tuner patch into shared component by @liu-cong in https://github.com/llm-d/llm-d/pull/1461
* Various fixes to the guides by @ahg-g in https://github.com/llm-d/llm-d/pull/1467
* (Guides) refresh scheduling-guides benchmark reports with v0.8.0 numbers by @vMaroon in https://github.com/llm-d/llm-d/pull/1463
* nightlies should comment status on PR by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1465
* remove feature-matrix.md by @ahg-g in https://github.com/llm-d/llm-d/pull/1474
* Updated GKE's supported paths by @ahg-g in https://github.com/llm-d/llm-d/pull/1475
* Updated GKE provider docs on what paths are supported on what hardware by @ahg-g in https://github.com/llm-d/llm-d/pull/1477
* [Bugfix] Fix WideEP Build + IMA by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1448
* removed redundant nightly tests badges by @ahg-g in https://github.com/llm-d/llm-d/pull/1476
* Update GKE PD nightly by @liu-cong in https://github.com/llm-d/llm-d/pull/1456
* [Guides] Bump WideEP by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1324
* point to the async processor well lit path instead of the guide directly by @ahg-g in https://github.com/llm-d/llm-d/pull/1479
* [Guides | Bugfix] Consistency + Fix HTTPRoutes in Gateway Mode by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1348
* Add recipe for llm-d-fs connector storage offloading with Lustre by @Sneha-at in https://github.com/llm-d/llm-d/pull/1427
* Polish the main README.md file by @ahg-g in https://github.com/llm-d/llm-d/pull/1482
* Fix: PD disaggregation CKS nightly values by @weizhoublue in https://github.com/llm-d/llm-d/pull/1484
* Move badge matrix to release by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1481
* Add release template to repository by @maugustosilva in https://github.com/llm-d/llm-d/pull/1487
* optimized-baseline README.md fix by @Amit-Berman in https://github.com/llm-d/llm-d/pull/1486
* Final batch of CI/CD fixes before release v0.7.0 by @maugustosilva in https://github.com/llm-d/llm-d/pull/1480
* Switch `llm-d-cuda` on `wide-ep-lws` to `v0.7.0` by @maugustosilva in https://github.com/llm-d/llm-d/pull/1489
* Add additional steps for release process. by @maugustosilva in https://github.com/llm-d/llm-d/pull/1491
* Add documentation release branch step to release template by @chcost in https://github.com/llm-d/llm-d/pull/1492
* Add Performance Highlights, v0.7 news, and badge bump to README by @chcost in https://github.com/llm-d/llm-d/pull/1483
* Prep v0.7.0 by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1270
* fix pd.values by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1493
* Update the SIG inference scheduler to sig-router by @petecheslock in https://github.com/llm-d/llm-d/pull/1497
* Minor: Update README for TPU v7 to TPU 7x by @seanhorgan in https://github.com/llm-d/llm-d/pull/1495
* Fix duplicate version badge and paragraph in README by @chcost in https://github.com/llm-d/llm-d/pull/1500
* [docs] Add user impact assessment to contributions by @elevran in https://github.com/llm-d/llm-d/pull/1505
* refactor(pd-xpu): switch PD XPU RDMA flow to kustomization by @VincyZhang in https://github.com/llm-d/llm-d/pull/925
* ci: add TPU nightly E2E tests (optimized-baseline, P/D, tiered-prefix-cache) by @sudoalok in https://github.com/llm-d/llm-d/pull/1496
* Update use case title from MaaS to Model-as-a-Service by @alexagriffith in https://github.com/llm-d/llm-d/pull/1515
* Proposal for RL platform-native time-slicing by @aishukamal in https://github.com/llm-d/llm-d/pull/1509
* Updated reference to inference-scheduler to llm-d router by @ahg-g in https://github.com/llm-d/llm-d/pull/1553
* fix: precise-prefix require Helm v4 for plugin.yaml by @zdtsw in https://github.com/llm-d/llm-d/pull/1563
* fix(ci): wire nightly WVA controller image into kustomize apply by @mamy-CS in https://github.com/llm-d/llm-d/pull/1576
* refactor(guides): align guides with llm-d Router terminology by @slashpai in https://github.com/llm-d/llm-d/pull/1560
* chore: add missing nightly test into slash command by @zdtsw in https://github.com/llm-d/llm-d/pull/1581
* fix: add timeout 90mins for nightly GithubAction by @zdtsw in https://github.com/llm-d/llm-d/pull/1575
* Revert "fix: add timeout 90mins for nightly GithubAction" by @maugustosilva in https://github.com/llm-d/llm-d/pull/1583
* Fixes for upstream transformations by @petecheslock in https://github.com/llm-d/llm-d/pull/1579
* fix: re-add the definition of OTHER_NIGHTLIES by @maugustosilva in https://github.com/llm-d/llm-d/pull/1587
* cleanup: removing unused params by @lionelvillard in https://github.com/llm-d/llm-d/pull/1578
* fix: harden install helpers with retry and download-to-file by @madhugoutham in https://github.com/llm-d/llm-d/pull/1588
* docs nitpick: remove RDMA from "RoCE RDMA" by @VadimEisenberg in https://github.com/llm-d/llm-d/pull/1592
* proposal for graduating llm-d-async from incubation to production by @shimib in https://github.com/llm-d/llm-d/pull/1594
* fix(precise guide): minor fixes by @vMaroon in https://github.com/llm-d/llm-d/pull/1593
* docs: add graduation proposal for batch-gateway by @lioraron in https://github.com/llm-d/llm-d/pull/1555
* fix: e2e nightly on OCP by @zdtsw in https://github.com/llm-d/llm-d/pull/1574
* add XPU nightly entries by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1573
* docs: migrate rollout guides from gateway-api-inference-extension by @Neha-dot-Yadav in https://github.com/llm-d/llm-d/pull/1552
* docs: add x-llm-d-request-dropped-reason to EPP HTTP headers reference by @lioraron in https://github.com/llm-d/llm-d/pull/1501
* Updated llm-d Router metrics names by @ahg-g in https://github.com/llm-d/llm-d/pull/1605
* [Proposal] Add non-Kubernetes deployment mode proposal by @chcost in https://github.com/llm-d/llm-d/pull/1547
* Updated the EPP config api docs with the latest changes by @ahg-g in https://github.com/llm-d/llm-d/pull/1606
* Add nightly E2E caller workflows for XPU guides by @xiaojun-zhang in https://github.com/llm-d/llm-d/pull/1250
* Action lint plus fix lint errors by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1584
* fix(ci): apply TLS overlay after namespace creation in WVA OCP nightly by @mamy-CS in https://github.com/llm-d/llm-d/pull/1591
* fix workflows xpu by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1609
* cicd: allow dry-run workflow to be executed even in case `guides/prereq/gateway-provider/install-gateway-provider-dependencies.sh` is not present by @maugustosilva in https://github.com/llm-d/llm-d/pull/1612
* Fix anchor link for sig router by @petecheslock in https://github.com/llm-d/llm-d/pull/1613
* Updated the guides to use the new helm charts released by the llm-d project by @ahg-g in https://github.com/llm-d/llm-d/pull/1607
* Fixed flag setting in the precise guide by @ahg-g in https://github.com/llm-d/llm-d/pull/1615
* docs: trim infra-provider guides for OpenShift and DigitalOcean by @sudoalok in https://github.com/llm-d/llm-d/pull/1601
* fix(nightly):   e2e for OCP on P/D + WideEP + WVA by @zdtsw in https://github.com/llm-d/llm-d/pull/1602
* docs: update EPP header references to x-llm-d by @wenhug in https://github.com/llm-d/llm-d/pull/1590
* fix(nightly-xpu): rename scheduler to router for xpu workflows by @xiaojun-zhang in https://github.com/llm-d/llm-d/pull/1621
* Add TPU and XPU workflows to the release table by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1626
* fix(nightly): switch to use new Chart with fix in old config by @zdtsw in https://github.com/llm-d/llm-d/pull/1634
* docs: fix broken Flow Control link in guides README by @javierdejesusda in https://github.com/llm-d/llm-d/pull/1596
* fix(ci): decouple router chart version from GAIE_VERSION by @weizhoublue in https://github.com/llm-d/llm-d/pull/1639
* Point to the /releases endpoint vs the tagged version so that the link works when the before the release is tagged by @petecheslock in https://github.com/llm-d/llm-d/pull/1638
* fix: use explicit exception type in lint-dockerfile-envvars.py by @Iceber in https://github.com/llm-d/llm-d/pull/1630
* [CI] build-image.yml use wrong github.event_name by @weizhoublue in https://github.com/llm-d/llm-d/pull/1326
* Cleaned up the guides/prereq/gateway-provider directory by @ahg-g in https://github.com/llm-d/llm-d/pull/1600
* Add no-kubernetes-deployment guide by @ezrasilvera in https://github.com/llm-d/llm-d/pull/1618
* Add badge guides by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1649
* fix: use llm-d.ai/engine-type for pod label by @zdtsw in https://github.com/llm-d/llm-d/pull/1642
* fix(flow-control): migrate InferenceObjective to llm-d.ai/v1alpha2 API group by @gyliu513 in https://github.com/llm-d/llm-d/pull/1640
* fix(ci): satisfy chart v0 tokenizer modelName validation by @gyliu513 in https://github.com/llm-d/llm-d/pull/1657
* refactor(nightly/wva): extract custom_deploy_script into standalone shell scripts by @lionelvillard in https://github.com/llm-d/llm-d/pull/1627
* [Docs] Streamline monitoring setup: consolidate docs site and move scripts to guides/recipes by @sudoalok in https://github.com/llm-d/llm-d/pull/1542
* Update cpu offloading config with benchmark by @liu-cong in https://github.com/llm-d/llm-d/pull/1654
* update: add guide for precies-prefix to use new vllm launch render by @zdtsw in https://github.com/llm-d/llm-d/pull/1507
* docs(observability): Add landing page by @gyliu513 in https://github.com/llm-d/llm-d/pull/1669
* Dynamic nightly lists identification by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1666
* [PD] Increase keep-alive timeout in well-lit P/D guides by @ilmarkov in https://github.com/llm-d/llm-d/pull/1564
* fix links in the epp/scheduler docs by @ahg-g in https://github.com/llm-d/llm-d/pull/1680
* Ref PR by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1682
* chore(guides): add OWNERS files to all well-lit path guides by @liu-cong in https://github.com/llm-d/llm-d/pull/1663
* cicd: start the migrations for nightly e2e to nightly benchmark by @maugustosilva in https://github.com/llm-d/llm-d/pull/1637
* feat: added optimized baseline multimodal guide by @capri-xiyue in https://github.com/llm-d/llm-d/pull/1620
* update: e2e to use new tokenizer than UDS by @zdtsw in https://github.com/llm-d/llm-d/pull/1689
* Add Cohere as a user in ADOPTERS.md by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1691
* fix: fixed typo by @capri-xiyue in https://github.com/llm-d/llm-d/pull/1694
* Use released manifests to install the inferencepool api by @ahg-g in https://github.com/llm-d/llm-d/pull/1695
* feat: add HF_TOKEN secret reference to guide manifests and update READMEs to reduce HF rate limiting by @liu-cong in https://github.com/llm-d/llm-d/pull/1684
* doc(core): fix inferencepool definition and provide variant definition. by @lionelvillard in https://github.com/llm-d/llm-d/pull/1664
* docs: add note about Prometheus Adapter deprecation by @omerap12 in https://github.com/llm-d/llm-d/pull/1655
* update: migrate precise-prefix-cache-scorer and a bunch of default configs by @zdtsw in https://github.com/llm-d/llm-d/pull/1688
* Add Jetbrains as a user in ADOPTERS.md by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1692
* Add WVA benchmark data by @asm582 in https://github.com/llm-d/llm-d/pull/1586
* doc: Add entries to instruct CI/CD automation to ignore certain commands on the guide by @maugustosilva in https://github.com/llm-d/llm-d/pull/1699
* Update Optimized Baseline TPU nightly test to use benchmark CI/CD by @rlakhtakia in https://github.com/llm-d/llm-d/pull/1700
* fix: update llmd multimodal guideline after token producer change by @capri-xiyue in https://github.com/llm-d/llm-d/pull/1704
* Converted optimized-baseline XPU workflow to the new format by @maugustosilva in https://github.com/llm-d/llm-d/pull/1693
* docs: add SGLang overview Grafana dashboard by @sudoalok in https://github.com/llm-d/llm-d/pull/1687
* update deploy configs to use DP supervisor by @tessapham in https://github.com/llm-d/llm-d/pull/1678
* New column AMD ROCm by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1716
* docs(optimized-baseline): document no-hit-lru-scorer in overview by @kfirtoledo in https://github.com/llm-d/llm-d/pull/1714
* Fix precise guide config by @liu-cong in https://github.com/llm-d/llm-d/pull/1706
* Normalize the names of "nightly E2E" workflows by @maugustosilva in https://github.com/llm-d/llm-d/pull/1721
* Temporarily default all (benchmark) workloads to `sanity_random.yaml` by @maugustosilva in https://github.com/llm-d/llm-d/pull/1725
* Update sync script and companies in columns by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1726
* Fixed grafana dashboard script by @ahg-g in https://github.com/llm-d/llm-d/pull/1729
* Add Stelia as a user of llm-d by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1698
* fix(guides): fix tokenizer container in precise guide for OpenShift by @Amit-Berman in https://github.com/llm-d/llm-d/pull/1733
* Fix bug in CI by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1734
* Remove e2e* files and clean ci-pr-test by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1739
* Add color badges by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1724
* Remove all references to `optimized-baseline` CI workflows for HPU by @maugustosilva in https://github.com/llm-d/llm-d/pull/1742
* Add a new CI job to query for past success on nightlies for `optimized-baseline` by @maugustosilva in https://github.com/llm-d/llm-d/pull/1747
* Update optimized baseline guide with sglang support by @rahulgurnani in https://github.com/llm-d/llm-d/pull/1720
* Add `consolidate-status` CI workflows to all tested variations of `optimized-baseline` by @maugustosilva in https://github.com/llm-d/llm-d/pull/1748
* Update optimized baseline and client setup documentation by @omerap12 in https://github.com/llm-d/llm-d/pull/1662
* Add benchmarking templates and report to the predicted-latency-routing guide by @kaushikmitr in https://github.com/llm-d/llm-d/pull/1705
* docs: add EPP HTTP APIs reference by @zetxqx in https://github.com/llm-d/llm-d/pull/1741
* Converted `predicted-latency-routing` to nightly benchmarks by @maugustosilva in https://github.com/llm-d/llm-d/pull/1756
* fix(autoscaling): update WVA guide to use HPA instead of VA by @lionelvillard in https://github.com/llm-d/llm-d/pull/1652
* fix(gke): override RDMA resource requests to fix scheduling on H200 by @liu-cong in https://github.com/llm-d/llm-d/pull/1738
* ci: add nightly e2e for the flow-control guide by @LukeAVanDrie in https://github.com/llm-d/llm-d/pull/1728
* Convert precise-prefix-cache by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1757
* updated the relevant apis to use the llm-d apigroup by @ahg-g in https://github.com/llm-d/llm-d/pull/1764
* Updated badge and job names for `precise-prefix` and `predicted-latency` by @maugustosilva in https://github.com/llm-d/llm-d/pull/1766
* Modify `precise-prefix-cache` on Intel XPU to conform with new standard by @maugustosilva in https://github.com/llm-d/llm-d/pull/1768
* docs: make multimodal a proper umbrella well-lit path guide by @capri-xiyue in https://github.com/llm-d/llm-d/pull/1762
* Update latency predictor guide with support for sglang by @rahulgurnani in https://github.com/llm-d/llm-d/pull/1702
* Use generic proxy terminology in router docs by @danehans in https://github.com/llm-d/llm-d/pull/1771
* chore: update batch-gateway refs after repo transfer by @lioraron in https://github.com/llm-d/llm-d/pull/1763
* Add Community Managers section to MAINTAINERS.md by @petecheslock in https://github.com/llm-d/llm-d/pull/1736
* tiered-prefix-cache guide changes - multi-tier support and others by @effi-ofer in https://github.com/llm-d/llm-d/pull/1561
* Converted `pd-disaggregation`, `tiered-prefix-cache` and `wide-ep-lws` CI/CD to nightly benchmark by @maugustosilva in https://github.com/llm-d/llm-d/pull/1774
* Add agentic-inference umbrella well-lit path by @vMaroon in https://github.com/llm-d/llm-d/pull/1743
* guides: add HF token step to predicted-latency README, bump benchmark image by @kaushikmitr in https://github.com/llm-d/llm-d/pull/1761
* align agnetic with multimodal guide name in using serving instead of inference by @ahg-g in https://github.com/llm-d/llm-d/pull/1776
* [SGLang]: Add SGLang tiered prefix cache support for CPU offloading using hicache by @rahulgurnani in https://github.com/llm-d/llm-d/pull/1722
* Fix file path in tiered prefix guide  by @liu-cong in https://github.com/llm-d/llm-d/pull/1785
* Additional set of fixes for guide name in `tiered-prefix-cache` by @maugustosilva in https://github.com/llm-d/llm-d/pull/1789
* docs(disaggregation): add SGLang P/D operations guide by @bongwoobak in https://github.com/llm-d/llm-d/pull/1709
* upgrading benchmarking image by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1790
* benchmark results for DP-aware wideEP scheduling by @tessapham in https://github.com/llm-d/llm-d/pull/1707
* feat: Leverage llm-d-benchmark within Optimized Baseline for Benchmarking llm-d by @Vezio in https://github.com/llm-d/llm-d/pull/1760
* Add workload and decode pod params by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1697
* optimized-baseline: mount /.triton and /.config emptyDirs on non-gpu vllm variants by @javierdejesusda in https://github.com/llm-d/llm-d/pull/1711
* add benchmark results for kv cache cpu offload on gpt-oss-120b  by @rachelt44 in https://github.com/llm-d/llm-d/pull/1676
* fix(pd): increase keep-alive timeout in remaining vLLM prefill manifests by @weizhoublue in https://github.com/llm-d/llm-d/pull/1686
* docs: added hf token part in multimodal optimized baseline guide by @capri-xiyue in https://github.com/llm-d/llm-d/pull/1796
* fix sync matrix script to use the json files by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1797
* Added "consolidate status" badges to all guides by @maugustosilva in https://github.com/llm-d/llm-d/pull/1794
* Update ADOPTERS.md by @jspisak in https://github.com/llm-d/llm-d/pull/1798
* feat: Continued Guide Refactoring to Point to llm-d-benchmark by @Vezio in https://github.com/llm-d/llm-d/pull/1799
* Add precise-prefix-cache nightly test by @rlakhtakia in https://github.com/llm-d/llm-d/pull/1802
* benchmark: remove benchmark workloads from this repo by @maugustosilva in https://github.com/llm-d/llm-d/pull/1804
* Add TPU nightly for precise prefix cache and update benchmark to use Qwen model by @rlakhtakia in https://github.com/llm-d/llm-d/pull/1667
* Add TPU V6 Recipe and nightly test for P/D by @rlakhtakia in https://github.com/llm-d/llm-d/pull/1661
* docs: fix typo in tiered prefix cache guide by @Bhimesh1 in https://github.com/llm-d/llm-d/pull/1803
* docs: fix agentic-serving rename and separate workloads by @vMaroon in https://github.com/llm-d/llm-d/pull/1807
* Fix in benchmark link by @rachelt44 in https://github.com/llm-d/llm-d/pull/1810
* [doc] add epp grpc apis doc by @zetxqx in https://github.com/llm-d/llm-d/pull/1805
* Add agentic code generation workload well-lit path  by @achandrasekar in https://github.com/llm-d/llm-d/pull/1727
* Update title for `tiered-prefix-cache` in OpenShift by @maugustosilva in https://github.com/llm-d/llm-d/pull/1813
* Add blue to dry-run badges in nightlies by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1816
* feat: add guide for SGLang in precise-prefix-cache-routing by @zdtsw in https://github.com/llm-d/llm-d/pull/1643
* Add recipes for deepseek-ai/DeepSeek-V4-Pro on NVL72/GB200 by @SageMoore in https://github.com/llm-d/llm-d/pull/1737
* Updated the documentation of the CI system by @maugustosilva in https://github.com/llm-d/llm-d/pull/1818
* docs: consolidate gateway installation guides by @alexagriffith in https://github.com/llm-d/llm-d/pull/1778
* change tiered-prefix-cache guide to use vllm v0.23.0 by @effi-ofer in https://github.com/llm-d/llm-d/pull/1812
* Add UCCL transport to images by @praveingk in https://github.com/llm-d/llm-d/pull/1377
* removing helmfile and helmdiff plugin from deps by @kapiljain1989 in https://github.com/llm-d/llm-d/pull/1825
* agentic-serving with token-load scorer by @kaushikmitr in https://github.com/llm-d/llm-d/pull/1817
* Add v6 recipe for Tiered Prefix Cache. by @rlakhtakia in https://github.com/llm-d/llm-d/pull/1815
* build new llm-d-cuda image with vLLM v0.23.0 by @tessapham in https://github.com/llm-d/llm-d/pull/1769
* DP-aware scheduling on GKE clusters by @tessapham in https://github.com/llm-d/llm-d/pull/1679
* [Multimodal]: fix path references in optimized baseline guide by @rahulgurnani in https://github.com/llm-d/llm-d/pull/1823
* Encode disaggregation guide by @roytman in https://github.com/llm-d/llm-d/pull/1614
* AWS EFA example for pd-disaggregation guide by @erezzarum in https://github.com/llm-d/llm-d/pull/1554
* Re-organized the well-lit paths docs into three groupings by @ahg-g in https://github.com/llm-d/llm-d/pull/1830
* Add Prime Intellect as an adopter of llm-d by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1834
* Add failure cat to the nightly workflows by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1839
* Reorganize part 2: create two new pillars, operations and infrastructure by @ahg-g in https://github.com/llm-d/llm-d/pull/1836
* fix: resolve documentation and manifest issues found during v0.9.0-rc.2 release verification by @liu-cong in https://github.com/llm-d/llm-d/pull/1842
* feat: centralize model server images via Kustomize Components by @liu-cong in https://github.com/llm-d/llm-d/pull/1845
* Updated EPP metrics as per the latest changes by @ahg-g in https://github.com/llm-d/llm-d/pull/1850
* [SGLang]: Increase the memory used for KV cache and update benchmark results in optimized baseline by @rahulgurnani in https://github.com/llm-d/llm-d/pull/1840
* refactor: kustomize overlay cleanup — images, labels, naming, sidecar by @liu-cong in https://github.com/llm-d/llm-d/pull/1851
* guides(autoscaling): Add asm582 as reviewer by @lionelvillard in https://github.com/llm-d/llm-d/pull/1838
* Fix: Align GKE overlay patch targets with actual LeaderWorkerSet names by @weizhoublue in https://github.com/llm-d/llm-d/pull/1857
* Update dir path for storage validation by @amirfr3 in https://github.com/llm-d/llm-d/pull/1860
* Bump LWS to 0.9.0 by @yankay in https://github.com/llm-d/llm-d/pull/1858
* Added router operations guide by @ahg-g in https://github.com/llm-d/llm-d/pull/1863
* Moved the multi-node guide to infrastructure by @ahg-g in https://github.com/llm-d/llm-d/pull/1861
* docs(autoscaling): VA deprecation, migration doc. by @lionelvillard in https://github.com/llm-d/llm-d/pull/1837
* guides(autoscaling): Move prometheus adapter installation to main guide by @lionelvillard in https://github.com/llm-d/llm-d/pull/1765
* predicted-latency-routing: add TPU agentic-serving benchmark path by @kaushikmitr in https://github.com/llm-d/llm-d/pull/1841
* fix: correct tracing manifest path for otel collector and jaeger installer by @shell720 in https://github.com/llm-d/llm-d/pull/1862
* Fixed links and references across docs by @ahg-g in https://github.com/llm-d/llm-d/pull/1867
* docs(tiered-prefix-cache): refocus guide on deployment, reflect vLLM-native tiering by @vMaroon in https://github.com/llm-d/llm-d/pull/1869
* docs: move artifacts.md from getting-started to api-reference by @Ibrahim2595 in https://github.com/llm-d/llm-d/pull/1874
* fix: add missing amd-ci kustomize overlay for PD disaggregation by @liu-cong in https://github.com/llm-d/llm-d/pull/1876
* docs(autoscaling): add multi-inference pool setup guide by @vivekk16 in https://github.com/llm-d/llm-d/pull/1878
* docs(agentic-serving): add Nemotron-3-Ultra on H200 deployment; make accelerator the dimension by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1740
* docs(autoscaling): fix WVA architecture inconsistencies and diagram by @lionelvillard in https://github.com/llm-d/llm-d/pull/1879
* docs: fix quickstart to use llm-d router chart instead of upstream GAIE chart by @acmenezes in https://github.com/llm-d/llm-d/pull/1870
* docs: rewrite getting-started intro as combined landing page (mdx) — supersedes #1800 by @Ibrahim2595 in https://github.com/llm-d/llm-d/pull/1820
* Updating tpu-vllm image version. by @gushob21 in https://github.com/llm-d/llm-d/pull/1864
* Update EPP metrics prefix  by @ahg-g in https://github.com/llm-d/llm-d/pull/1880
* guides(autoscaling): Add experimental replicas rebalancing guide by @asm582 in https://github.com/llm-d/llm-d/pull/1793
* guides(autoscaling): fix broken link by @lionelvillard in https://github.com/llm-d/llm-d/pull/1888
* chore(release): pin autoscaling guides to release-0.8 by @lionelvillard in https://github.com/llm-d/llm-d/pull/1889
* Update Optimized baseline guide benchmarks by @oshfeder in https://github.com/llm-d/llm-d/pull/1675
* Remove HPU (Intel Gaudi) support by @xiaojun-zhang in https://github.com/llm-d/llm-d/pull/1886
* feat: centralize shared env vars in guides/env.sh by @liu-cong in https://github.com/llm-d/llm-d/pull/1856
* [SGLang] Update the well-lit path guide for precise prefix cache aware routing with optimal config and updated benchmark numbers by @rahulgurnani in https://github.com/llm-d/llm-d/pull/1887
* Organized the optimized-baseline benchmarking results under one directory by @ahg-g in https://github.com/llm-d/llm-d/pull/1890
* Bump api-server-count from 1 to 4 for DeepSeek-V4 NVL72 GB200 guide by @tlrmchlsmth in https://github.com/llm-d/llm-d/pull/1877
* fix(guides): use centralized image components and track overrides by @liu-cong in https://github.com/llm-d/llm-d/pull/1896
* Use prebuilt vLLM XPU image instead of building from source by @xiaojun-zhang in https://github.com/llm-d/llm-d/pull/1577
* docs: make multimodal concise and added additional readme.md in guides/ by @capri-xiyue in https://github.com/llm-d/llm-d/pull/1873
* Moved precise kv-cache benchmarking results out of the main guide by @ahg-g in https://github.com/llm-d/llm-d/pull/1900
* Separated benchmarking numbers from the tiered prefix cache guides  by @ahg-g in https://github.com/llm-d/llm-d/pull/1899
* v0.8.0 release prep: swap to current official images by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1885
* [PD Disaggregation][Vllm] Add GKE RDMA/DRA/DRANET configs and related documentation updates by @huaxig in https://github.com/llm-d/llm-d/pull/1821
* [TensorRT-LLM] trtllm-serve recipe and optimized baseline guide by @BenjaminBraunDev in https://github.com/llm-d/llm-d/pull/1866
* docs(getting-started): reorder landing CTAs and refine founded-by line by @Ibrahim2595 in https://github.com/llm-d/llm-d/pull/1901
* add missing consolidation-* workflows for past status of tiered prefix by @amirfr3 in https://github.com/llm-d/llm-d/pull/1835
* deps(actions): bump actions/checkout from 6 to 7 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1904
* guides/precise-prefix-cache-routing: run the renderer as a Service, not an EPP sidecar by @vMaroon in https://github.com/llm-d/llm-d/pull/1871
* Update multimodal-serving/e-disaggregation guide. by @revit13 in https://github.com/llm-d/llm-d/pull/1832
* Revert "deps(actions): bump actions/checkout from 6 to 7" by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1908
* Removed direct references to llm-d epp image and consolidated references to the router charts by @ahg-g in https://github.com/llm-d/llm-d/pull/1909
* Build images from PR by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1910
* add dry_run to the parameters by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1912
* guides: add Envoy AI Gateway installation instructions by @nacx in https://github.com/llm-d/llm-d/pull/1788
* Fix docs by @ahg-g in https://github.com/llm-d/llm-d/pull/1915
* Updated guides on how to enable monitoring on llm-d router by @ahg-g in https://github.com/llm-d/llm-d/pull/1916
* Adding well lit path for py-inference-scheduler into verl by @kfswain in https://github.com/llm-d/llm-d/pull/1814
* docs: fold Traffic Control & Autoscaling into Foundations by @Ibrahim2595 in https://github.com/llm-d/llm-d/pull/1917
* [WideEP] Migrate DP Aware To Main Example by @tessapham in https://github.com/llm-d/llm-d/pull/1854
* Polish gateway landing page doc by @ahg-g in https://github.com/llm-d/llm-d/pull/1932
* ci: let guide OWNERS trigger /test-nightly for their guide by @kfirtoledo in https://github.com/llm-d/llm-d/pull/1929
* Use released manifests to install the llm-d router crds by @ahg-g in https://github.com/llm-d/llm-d/pull/1914
* Use router v0.9.0 by @liu-cong in https://github.com/llm-d/llm-d/pull/1935
* build llm-d image with vllm patch for DP supervisor by @tessapham in https://github.com/llm-d/llm-d/pull/1907
* Mooncake tiered offloading guide integration by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1826
* chore: update xpu image to vllm 0.23 by @poussa in https://github.com/llm-d/llm-d/pull/1924
* Use router v0.9.0 by @liu-cong in https://github.com/llm-d/llm-d/pull/1936
* guides(autoscaling): fix broken link by @lionelvillard in https://github.com/llm-d/llm-d/pull/1938
* Enable `wide-ep-lws` on `GKE` and `CKS` by @maugustosilva in https://github.com/llm-d/llm-d/pull/1928
* Use router sidecar v0.9.0 Signed-off-by: Cong Liu <conliu@google.com> by @liu-cong in https://github.com/llm-d/llm-d/pull/1939

## New Contributors
* @hhk7734 made their first contribution in https://github.com/llm-d/llm-d/pull/1111
* @sharvil10 made their first contribution in https://github.com/llm-d/llm-d/pull/1101
* @madhugoutham made their first contribution in https://github.com/llm-d/llm-d/pull/1126
* @hexfusion made their first contribution in https://github.com/llm-d/llm-d/pull/1123
* @LukeAVanDrie made their first contribution in https://github.com/llm-d/llm-d/pull/1127
* @ianliuy made their first contribution in https://github.com/llm-d/llm-d/pull/1135
* @amacaskill made their first contribution in https://github.com/llm-d/llm-d/pull/1102
* @rebel-jinmoo made their first contribution in https://github.com/llm-d/llm-d/pull/1115
* @praveingk made their first contribution in https://github.com/llm-d/llm-d/pull/1181
* @nilig made their first contribution in https://github.com/llm-d/llm-d/pull/1184
* @revit13 made their first contribution in https://github.com/llm-d/llm-d/pull/1287
* @ying-jeanne made their first contribution in https://github.com/llm-d/llm-d/pull/1267
* @xiaojun-zhang made their first contribution in https://github.com/llm-d/llm-d/pull/1297
* @sudoalok made their first contribution in https://github.com/llm-d/llm-d/pull/1264
* @lioraron made their first contribution in https://github.com/llm-d/llm-d/pull/1187
* @liulanze made their first contribution in https://github.com/llm-d/llm-d/pull/1357
* @rahulgurnani made their first contribution in https://github.com/llm-d/llm-d/pull/1313
* @EzgiTastan made their first contribution in https://github.com/llm-d/llm-d/pull/1364
* @weizhoublue made their first contribution in https://github.com/llm-d/llm-d/pull/1388
* @alexagriffith made their first contribution in https://github.com/llm-d/llm-d/pull/1375
* @adinilfeld made their first contribution in https://github.com/llm-d/llm-d/pull/1428
* @rdwj made their first contribution in https://github.com/llm-d/llm-d/pull/1450
* @Amit-Berman made their first contribution in https://github.com/llm-d/llm-d/pull/1486
* @slashpai made their first contribution in https://github.com/llm-d/llm-d/pull/1560
* @VadimEisenberg made their first contribution in https://github.com/llm-d/llm-d/pull/1592
* @Neha-dot-Yadav made their first contribution in https://github.com/llm-d/llm-d/pull/1552
* @javierdejesusda made their first contribution in https://github.com/llm-d/llm-d/pull/1596
* @Iceber made their first contribution in https://github.com/llm-d/llm-d/pull/1630
* @ezrasilvera made their first contribution in https://github.com/llm-d/llm-d/pull/1618
* @gyliu513 made their first contribution in https://github.com/llm-d/llm-d/pull/1640
* @ilmarkov made their first contribution in https://github.com/llm-d/llm-d/pull/1564
* @omerap12 made their first contribution in https://github.com/llm-d/llm-d/pull/1655
* @asm582 made their first contribution in https://github.com/llm-d/llm-d/pull/1586
* @jspisak made their first contribution in https://github.com/llm-d/llm-d/pull/1798
* @Bhimesh1 made their first contribution in https://github.com/llm-d/llm-d/pull/1803
* @achandrasekar made their first contribution in https://github.com/llm-d/llm-d/pull/1727
* @SageMoore made their first contribution in https://github.com/llm-d/llm-d/pull/1737
* @erezzarum made their first contribution in https://github.com/llm-d/llm-d/pull/1554
* @amirfr3 made their first contribution in https://github.com/llm-d/llm-d/pull/1860
* @shell720 made their first contribution in https://github.com/llm-d/llm-d/pull/1862
* @Ibrahim2595 made their first contribution in https://github.com/llm-d/llm-d/pull/1874
* @vivekk16 made their first contribution in https://github.com/llm-d/llm-d/pull/1878
* @acmenezes made their first contribution in https://github.com/llm-d/llm-d/pull/1870
* @gushob21 made their first contribution in https://github.com/llm-d/llm-d/pull/1864
* @oshfeder made their first contribution in https://github.com/llm-d/llm-d/pull/1675
* @huaxig made their first contribution in https://github.com/llm-d/llm-d/pull/1821
* @nacx made their first contribution in https://github.com/llm-d/llm-d/pull/1788
* @kfswain made their first contribution in https://github.com/llm-d/llm-d/pull/1814

**Full Changelog**: https://github.com/llm-d/llm-d/compare/v0.6...v0.8.0

## v0.8.1 (2026-06-26)

## LLM-D v0.8.0 Component Summary

> **Themes:** solidify CI coverage & project operations, expand accelerator coverage, graduate multimodal/batch/flow-control to production, introduce initial RL support.

| Component | Version | Previous Version | Type | Notes |
|-----------|---------|------------------|------|-------|
| llm-d/llm-d-router-endpoint-picker | `v0.9.0` | `v0.8.0` | Image + Helm Chart | Core EPP image (renamed from llm-d-inference-scheduler) |
| llm-d/llm-d-router-disagg-sidecar | `v0.9.0` | `v0.8.0` | Image | P/D routing sidecar (renamed from llm-d-routing-sidecar) |
| llm-d/llm-d-uds-tokenizer | `vllm-v0.23.0` | `vllm-v0.19.1` | Image | Tokenizer sidecar aligned with vLLM version |
| llm-d/llm-d-kv-cache | `v0.9.0` | `v0.8.0` | Library | HMA support, storage events, multi-tier offloading |
| llm-d/llm-d-inference-sim | `v0.9.2` | `v0.8.2` | Image | Multimodal support, Mooncake bootstrap, configurable latency |
| llm-d/llm-d-cuda | `v0.8.0` | `v0.7.0` | Image | vLLM v0.23.0, CUDA 13.0.2 |
| llm-d/llm-d-aws (EFA) | `v0.8.0` | `v0.7.0` | Image | |
| llm-d/llm-d-hpu | `v0.8.0` | `v0.7.0` | Image | |
| llm-d/llm-d-kv-cache/llmd_fs_backend_connector | `v0.23` | `v0.19.1` | Wheel installed in `llm-d` | Migrated to vLLM 0.23.0 offload API |
| llm-d/llm-d-benchmark | `v0.7.0` | `v0.6.8.1` | Image | Benchmark workload launcher |
| llm-d/llm-d-workload-variant-autoscaler | `v0.8.0` | `v0.7.0` | Helm Chart + Image | CRD migration to llm-d.ai API group, improved observability |
| vllm-project/vllm | `v0.23.0` | `v0.19.1` | Wheel installed in `llm-d` | Confirmed by @Gregory-Pereira and @tessapham |
| kubernetes-sigs/gateway-api-inference-extension | `v1.5.0` | `v1.5.0` | Helm Chart | Charts now published from llm-d-router OCI registry |

### Upstream vLLM Images (replacing llm-d-built images)

> Per PR [#1791](https://github.com/llm-d/llm-d/pull/1791), the following platforms now use upstream vLLM images directly instead of llm-d-built custom images:

| Platform | New Image | Tag | Previous llm-d Image |
|----------|-----------|-----|---------------------|
| GPU (CUDA) | `vllm/vllm-openai` | `v0.23.0` | `ghcr.io/llm-d/llm-d-cuda` (still available for advanced builds) |
| ROCm (AMD) | `vllm/vllm-openai-rocm` | | `ghcr.io/llm-d/llm-d-rocm` |
| CPU | `ghcr.io/llm-d/llm-d-cpu` | `v0.7.0` | Same image, version bump |
| XPU (Intel) | `vllm/vllm-openai` | `v0.23.0` | `ghcr.io/llm-d/llm-d-xpu` |

---

## Infrastructure Changes

| Component | Version | Previous Version | Notes |
|-----------|---------|------------------|-------|
| Gateway API | `v1.5.1` | `v1.5.1` | No change |
| Istio | `1.29.4` | `1.29.1` | Patch update |
| kgateway (agentgateway) | `v2.3.3` | `v2.2.1` | |

---

## Deprecated / Removed Components

| Component | Status | Replaced By |
|-----------|--------|-------------|
| llm-d/llm-d-inference-scheduler | **Renamed** | `ghcr.io/llm-d/llm-d-router-endpoint-picker` |
| llm-d/llm-d-routing-sidecar | **Renamed** | `ghcr.io/llm-d/llm-d-router-disagg-sidecar` |
| llm-d/llm-d-cuda (debug) | **Removed** | N/A |
| llm-d/llm-d-cuda-gb200 | **Removed** | N/A |
| llm-d/llm-d-xpu | **Removed** | `vllm/vllm-openai` |
| llm-d/llm-d-rocm | **Removed** | `vllm/vllm-openai-rocm` |

---

## New Capabilities in This Release

| Capability | Component(s) | Status |
|------------|--------------|--------|
| Multi-modal serving (production) | llm-d-router, llm-d-inference-sim | Graduated |
| Batch gateway (production) | llm-d-router | Graduated |
| Flow control (production) | llm-d-router | Graduated |
| Non-Kubernetes mode (RL/Slurm) | llm-d-router (FileDiscovery plugin) | New |
| Responses API support | llm-d-router | New |
| Multi-tier KV offloading (CPU → storage) | llm-d-kv-cache | New |
| HMA (Heterogeneous Memory Allocation) support | llm-d-kv-cache, fs-connector | New |
| DP-Aware scheduling | llm-d-router | Graduating |
| Mooncake connector | llm-d-kv-cache | New |
| Predicted latency scheduling | llm-d-router | New |
| Agentic workload routing | llm-d-router | New |
| TPU nightly tests | CI/CD | New |

## What's Changed
* Point to patch v0.8.1 by @maugustosilva in commit d6ffb5c7cff80e3953c62f464c08984ccd6a6096
* Updated the branch to clone in the guides to release-0.8 branch by @ahg-g in https://github.com/llm-d/llm-d/pull/1958
* Pin inference-perf version by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1946

**Full Changelog**: https://github.com/llm-d/llm-d/compare/v0.8.0...v0.8.1

## v0.9.0 (2026-08-17)

# llm-d v0.9.0 Release

Release goal and issues tracked here: https://github.com/llm-d/llm-d/issues/1945, although not all of that was accomplished. Thank you to all our new and old contributors.

## LLM-D v0.9.0 Component Summary

| Component | Version | Previous Version | Type |
|-----------|---------|------------------|------|
| llm-d/llm-d-router-endpoint-picker | `v0.10.0` | `v0.9.0` | Image + Helm Chart |
| llm-d/llm-d-router-disagg-sidecar | `v0.10.0` | `v0.9.0` | Image |
| llm-d/llm-d-uds-tokenizer | — | `v0.9.0` | Image |
| llm-d/llm-d-kv-cache | `v0.9.0` | `v0.8.0` | Library |
| llm-d/llm-d-inference-sim | `v0.10.2` | `v0.9.2` | Image |
| llm-d/llm-d-cuda | `v0.9.0` | `v0.8.1` | Image |
| llm-d/llm-d-aws (EFA) | `v0.9.0` | `v0.8.1` | Image |
| llm-d/llm-d-rocm | `v0.9.0` | `v0.8.1` | Image |
| llm-d/llm-d-xpu | `v0.9.0` | `v0.8.1` | Image |
| llm-d/llm-d-xpu-sglang | `v0.9.0` | — | Image |
| llm-d/llm-d-cpu | `v0.9.0` | `v0.8.1` | Image |
| llm-d/llm-d-kv-cache/llmd-fs-connector | `0.23` | `0.23` | Wheel installed in `llm-d` |
| llm-d/llm-d-benchmark | `v0.8.0` | `v0.6.8.1` | Image |
| llm-d/llm-d-workload-variant-autoscaler | `v0.9.0` | `v0.8.0` | Helm Chart + Image |
| llm-d/llm-d-async | `v0.9.0` | `v0.8.0` | Helm Chart + Image |
| llm-d/llm-d-batch-gateway | `v0.5.0` | — | Image + Helm Chart |
| llm-d/llm-d-latency-predictor | `0.9.0` | — | Image |
| llm-d/mooncake-master-store | `v0.8.0` | `v0.8.0` | Image |
| vllm-project/vllm | `v0.26.0` | `v0.23.0` | Wheel installed in `llm-d` |
| kubernetes-sigs/gateway-api-inference-extension | `v1.5.0` | `v1.5.0` | Helm Chart + CRDs |
| kubernetes-sigs/inference-perf | `v0.6.1` | `v0.6.0` | Tool |

### Upstream Model Server Images

| Engine | Image | Tag | Previous Tag |
|--------|-------|-----|--------------|
| vLLM | `docker.io/vllm/vllm-openai` | `v0.26.0` | `v0.23.0` |
| vLLM Omni | `docker.io/vllm/vllm-omni` | `v0.26.0` | — |
| vLLM TPU | `docker.io/vllm/vllm-tpu` | `v0.26.0` | `v0.25.0` |
| vLLM XPU | `docker.io/vllm/vllm-openai-xpu` | `v0.26.0` | `v0.23.0` |
| vLLM ROCm | `docker.io/vllm/vllm-openai-rocm` | `v0.26.0` | `v0.23.0` |
| vLLM ROCm Omni | `docker.io/vllm/vllm-omni-rocm` | `v0.24.1` | — |
| vLLM CPU | `docker.io/vllm/vllm-openai-cpu` | `v0.26.0` | `v0.23.0` |
| SGLang | `docker.io/lmsysorg/sglang` | `v0.5.16` | `v0.5.13.post1` |
| TRT-LLM | `nvcr.io/nvidia/tensorrt-llm/release` | `1.3.0rc23` | — |

---

## Infrastructure Changes

| Component | Version | Previous Version |
|-----------|---------|------------------|
| Gateway API CRDs | `v1.5.1` | `v1.5.1` |
| GAIE CRDs | `v1.5.0` | `v1.5.0` |
| Istio | `1.29.4` | `1.29.4` |
| AgentGateway | `v1.1.0` | `v2.3.3` (as kgateway) |
| Envoy Gateway / Envoy AI Gateway | `v1.8.1` / `v0.7.0` | — |

## What's Changed
* bump wide-ep images by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1937
* Add benchmark results for SGLang with tiered prefix cache by @rahulgurnani in https://github.com/llm-d/llm-d/pull/1921
* pin inference-perf version by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1946
* Add Intel XPU vLLM support for multimodal optimized-baseline by @joshuayao in https://github.com/llm-d/llm-d/pull/1772
* docs: list founders inline instead of logos on getting-started intro by @Ibrahim2595 in https://github.com/llm-d/llm-d/pull/1960
* Create skeleton for sig-llm-d-inference-payload-processor by @petecheslock in https://github.com/llm-d/llm-d/pull/1499
* Add cleanup parameter to slash command by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1961
* update-badge parameter by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1951
* docs: add Deploy section to batch-gateway well-lit path by @lioraron in https://github.com/llm-d/llm-d/pull/1965
* Update links in kv-offloader documentation to point to the GitHub repo for deployment manifests by @petecheslock in https://github.com/llm-d/llm-d/pull/1962
* fix: Add missing `update_badge` parameters to ci workflows by @amirfr3 in https://github.com/llm-d/llm-d/pull/1969
* docs: fix broken well-lit-path links in README by @Ibrahim2595 in https://github.com/llm-d/llm-d/pull/1975
* Fix metric names for SGLang in Grafana Dashboards by @rahulgurnani in https://github.com/llm-d/llm-d/pull/1970
* docs(flowcontrol): map shutdown-drained requests to 503 by @LukeAVanDrie in https://github.com/llm-d/llm-d/pull/1801
* Add Snowflake as a user of llm-d by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/1978
* [Docs] Update PD flow to include KV lease extension by @NickLucche in https://github.com/llm-d/llm-d/pull/1543
* deps(actions): bump actions/checkout from 6 to 7 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/1976
* fix: correct the typos in the project by @AayushSaini101 in https://github.com/llm-d/llm-d/pull/1971
* Add sig-batch-inference to SIGS.md by @jtechapps in https://github.com/llm-d/llm-d/pull/1922
* proposal: Observability integration across the llm-d stack by @gyliu513 in https://github.com/llm-d/llm-d/pull/1685
* docs: add XPU WideEP guide backend by @yao531441 in https://github.com/llm-d/llm-d/pull/1925
* Add Novita as a user of llm-d  by @UranusSeven in https://github.com/llm-d/llm-d/pull/1986
* [ROCm] Docker AMD ROCm image update by @vcave in https://github.com/llm-d/llm-d/pull/1977
* fix(ci): fix dry_run default value for wide-ep-lws update-badge jobs by @weizhoublue in https://github.com/llm-d/llm-d/pull/1955
* fix: xpu rdma deviceclass name by @poussa in https://github.com/llm-d/llm-d/pull/1811
* Support tiered prefix cache on Intel XPU with LMCache connector by @XinyuYe-Intel in https://github.com/llm-d/llm-d/pull/1731
* Update version badge to v0.8 by @chcost in https://github.com/llm-d/llm-d/pull/1989
* [Autoscaling]: Update autoscaling guide OWNERS file by @lionelvillard in https://github.com/llm-d/llm-d/pull/1990
* [Autoscaling] Unpin WVA release 0.8 by @lionelvillard in https://github.com/llm-d/llm-d/pull/1979
* chore: Remove superfluous nightly prefix. by @lionelvillard in https://github.com/llm-d/llm-d/pull/1991
* [Fix] Add new config required by `actions/checkout@v7` by @maugustosilva in https://github.com/llm-d/llm-d/pull/1992
* [Fix] Add `allow-unsafe-pr-checkout: true` to all instances of `actions/checkout` by @maugustosilva in https://github.com/llm-d/llm-d/pull/1993
* docs(ipp): add Inference Payload Processor documentation by @yehuditkerido in https://github.com/llm-d/llm-d/pull/1884
* docs: fix broken links and script paths in flow control guide by @ishwar170695 in https://github.com/llm-d/llm-d/pull/1997
* Add DigitalOcean as an adopter in ADOPTERS.md by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/2004
* docs(wva): add KEDA support and shared-cluster setup by @omerap12 in https://github.com/llm-d/llm-d/pull/1792
* Fix return type annotation by @diegocastanibm in https://github.com/llm-d/llm-d/pull/2005
* docs: fix typo for vllm attribute by @zdtsw in https://github.com/llm-d/llm-d/pull/2000
* update: add GH nightly for optimized baseline on SGLang by @zdtsw in https://github.com/llm-d/llm-d/pull/1999
* feat(monitoring): ship default EPP Prometheus alerting rules by @sudoalok in https://github.com/llm-d/llm-d/pull/1972
* Add license scan report and status by @fossabot in https://github.com/llm-d/llm-d/pull/2013
* Resync nightly matrix by @diegocastanibm in https://github.com/llm-d/llm-d/pull/2018
* Add engine-type: sglang label to optimized-baseline kustomization by @Amit-Berman in https://github.com/llm-d/llm-d/pull/2012
* docs(agentic-serving): add TPU v7 disaggregated P/D benchmark results and manifests by @yangspirit in https://github.com/llm-d/llm-d/pull/1903
* Add new adopter of llm-d by @robertgshaw2-redhat in https://github.com/llm-d/llm-d/pull/2028
* Docs: add menu-config.json to control the documentation sidebar by @Ibrahim2595 in https://github.com/llm-d/llm-d/pull/2021
* Docs: fix broken multimodal guide link in EPP HTTP APIs reference by @Ibrahim2595 in https://github.com/llm-d/llm-d/pull/2031
* Prevent Incorrect Load-Aware Routing for AMD SGLang Backends by @weizhoublue in https://github.com/llm-d/llm-d/pull/2025
* Update README.md with two Docs links by @Ibrahim2595 in https://github.com/llm-d/llm-d/pull/2007
* fix(wva): migrate nightly + guide from Prometheus Adapter to KEDA by @mamy-CS in https://github.com/llm-d/llm-d/pull/2038
* docs(autoscaling): convert EPP autoscaling guide to KEDA by @nourey in https://github.com/llm-d/llm-d/pull/1981
* fix(wva): authenticate KEDA to Thanos and assert the metric path by @mamy-CS in https://github.com/llm-d/llm-d/pull/2039
* Initial Details for sig-agentic-inference by @petecheslock in https://github.com/llm-d/llm-d/pull/1868
* feat(guides): add GKE A4X (GB200) P/D disaggregation overlay by @huaxig in https://github.com/llm-d/llm-d/pull/2043
* refactor(a4x): update A4X kustomization without gib and patching by @huaxig in https://github.com/llm-d/llm-d/pull/2058
* support ipv6 setting by @eating-chen in https://github.com/llm-d/llm-d/pull/1974
* fix: Move the router's grafana dashboard to llm-d/llm-d by @gyliu513 in https://github.com/llm-d/llm-d/pull/1984
* fix: CI dry-run and optimized-baseline guide by @zdtsw in https://github.com/llm-d/llm-d/pull/2035
* update(CI): convert wva dry-run job to do recursive find for kustomization by @zdtsw in https://github.com/llm-d/llm-d/pull/2063
* predicted-latency-routing: add the P/D disaggregated deployment and its benchmark by @kaushikmitr in https://github.com/llm-d/llm-d/pull/2048
* refactor(gke): restructure GKE overlays to gke/base and gke/a4x by @liu-cong in https://github.com/llm-d/llm-d/pull/2062
* Optimized Baseline Architectural Shift & Updated Benchmarks by @kaushikmitr in https://github.com/llm-d/llm-d/pull/1651
* [Minor] Update machine types in GKE README by @seanhorgan in https://github.com/llm-d/llm-d/pull/2056
* feat(a4xmax): add GKE A4X Max / GB300 optimized DRA recipe for vLLM m… by @huaxig in https://github.com/llm-d/llm-d/pull/2068
* deps(actions): bump actions/setup-go from 6 to 7 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/2082
* docs(guides): point async-processing guide at the llm-d org by @shimib in https://github.com/llm-d/llm-d/pull/2077
* deps(actions): bump actions/setup-python from 6 to 7 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/2083
* feat: added video setting for approximate prefix cache in e-disaggregation guide by @capri-xiyue in https://github.com/llm-d/llm-d/pull/2080
* [ROCM] CI e2e configs by @vcave in https://github.com/llm-d/llm-d/pull/1875
* Add async-processor operations guide by @shimib in https://github.com/llm-d/llm-d/pull/1865
* Update router images and manifests to point to main by @ahg-g in https://github.com/llm-d/llm-d/pull/2065
* docs/guides: replace deprecated maxPrefixBlocksToMatch and blockSize with supported token alternatives by @liu-cong in https://github.com/llm-d/llm-d/pull/2070
* docs(guides): remove IPP image tag workaround by @noalimoy in https://github.com/llm-d/llm-d/pull/2075
* deps(actions): bump peter-evans/repository-dispatch from 3 to 4 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/2046
* Rearrange FOSSA Status badge in README by @davidgs in https://github.com/llm-d/llm-d/pull/2036
* [ROCM] Enable predicted latency routing guide + CI badges by @vcave in https://github.com/llm-d/llm-d/pull/2090
* Minor: update TPU version references in documentation by @seanhorgan in https://github.com/llm-d/llm-d/pull/2030
* docs(guides): fix prerequisite ordering and add pod readiness check in quickstart by @haitwang-cloud in https://github.com/llm-d/llm-d/pull/2085
* feat: Update PD guide for sglang with GKE DRA and RDMA config by @rahulgurnani in https://github.com/llm-d/llm-d/pull/2059
* docs(menu): add Async Processor Operations Guide to the operations menu by @shimib in https://github.com/llm-d/llm-d/pull/2092
* pd-disaggregation: adopt token-based routing, refresh benchmark report by @kaushikmitr in https://github.com/llm-d/llm-d/pull/2072
* [ROCM] add update_badge input to precise and predicted nightly by @vcave in https://github.com/llm-d/llm-d/pull/2096
* [ROCM] adjust predicted guide to llm-d-benchmarks by @vcave in https://github.com/llm-d/llm-d/pull/2094
* FMA guide by @diegocastanibm in https://github.com/llm-d/llm-d/pull/1779
* predicted-latency-routing: add multimodal serving case by @kaushikmitr in https://github.com/llm-d/llm-d/pull/2078
* docs(guides): add multi-tenant async-processing sub-guide (team × tier × model) by @shimib in https://github.com/llm-d/llm-d/pull/2047
* fix: correct the name of status workflow for wide ep lws by @rahulgurnani in https://github.com/llm-d/llm-d/pull/2108
* feat: updated video guide by @capri-xiyue in https://github.com/llm-d/llm-d/pull/2091
* feat(sglang): add managed lustre L3 offloading support by @tyuchn in https://github.com/llm-d/llm-d/pull/2093
* Update async-processor architecture docs by @jtechapps in https://github.com/llm-d/llm-d/pull/2079
* update(agentic-serving): enable VLLM_PREFIX_CACHE_RETENTION_INTERVAL=0 for Nemotron-3-Ultra by @zdtsw in https://github.com/llm-d/llm-d/pull/2034
* Update the Overview of the FMA well-lit path by @MikeSpreitzer in https://github.com/llm-d/llm-d/pull/2100
* Adding FMA nightly using well lit path by @aavarghese in https://github.com/llm-d/llm-d/pull/2101
* ci: add Intel XPU wide-ep-lws nightly coverage by @yao531441 in https://github.com/llm-d/llm-d/pull/2087
* Add .editorconfig for consistent formatting by @arijitroy003 in https://github.com/llm-d/llm-d/pull/2103
* deps(actions): bump actions/checkout from 6 to 7 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/2127
* Verification scripts for ci workflows by @amirfr3 in https://github.com/llm-d/llm-d/pull/1987
* [feat] Structured Guides for Machine and Human Readable Format by @Vezio in https://github.com/llm-d/llm-d/pull/1988
* fix: FMA guide fixes for benchmark nightly errors by @aavarghese in https://github.com/llm-d/llm-d/pull/2132
* multimodal-serving: adopt token-based routing, refresh benchmark report by @kaushikmitr in https://github.com/llm-d/llm-d/pull/2081
* precise-prefix-cache-routing: adopt token-based routing, refresh benchmarks by @kaushikmitr in https://github.com/llm-d/llm-d/pull/2071
* guides: add SLO-driven autoscaling (KEDA + predicted latency) by @kaushikmitr in https://github.com/llm-d/llm-d/pull/2011
* docs(guides): add KEDA + EPP Pool-Level Saturation Metrics autoscaling guide by @asm582 in https://github.com/llm-d/llm-d/pull/2051
* docs: fixed typo in multimodal aggregation guide by @capri-xiyue in https://github.com/llm-d/llm-d/pull/2136
* [docs] Add DisaggregatedSet variant of the P/D disaggregation guide by @BenjaminBraunDev in https://github.com/llm-d/llm-d/pull/2052
* Enable token load routing with pd-disaggregation in agentic serving by @cheng-hsiang-chiu in https://github.com/llm-d/llm-d/pull/2024
* Fix: Bind In-Flight Token Accounting to the Precise Prefix Cache Producer by @weizhoublue in https://github.com/llm-d/llm-d/pull/2148
* [ROCM] optimized-baseline: persist model cache for AMD vllm via component by @PrateekKumar1709 in https://github.com/llm-d/llm-d/pull/2153
* Agentic Serving: GLM-5.2 Integration Guide by @elvircrn in https://github.com/llm-d/llm-d/pull/1947
* Support tiered prefix cache with lmcache connector with file system on XPU by @XinyuYe-Intel in https://github.com/llm-d/llm-d/pull/2159
* docs(observability): add per-guide troubleshooting for workload autoscaling by @gyliu513 in https://github.com/llm-d/llm-d/pull/2130
* docs(observability): add per-guide troubleshooting for P/D disaggregation by @gyliu513 in https://github.com/llm-d/llm-d/pull/2128
* Inject HF_TOKEN into optimized-baseline trtllm decode pods by @BenjaminBraunDev in https://github.com/llm-d/llm-d/pull/2167
* chore: remove explicit --vllm-port=8200 from sidecar configs by @zdtsw in https://github.com/llm-d/llm-d/pull/2116
* [guide] Mooncake pd integration by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/1511
* docs: fix broken README links by @breno-costa in https://github.com/llm-d/llm-d/pull/2179
* docs(autoscaling): move KEDA+EPP queue guide under optimized-baseline-autoscaling by @mamy-CS in https://github.com/llm-d/llm-d/pull/2181
* fix(autoscaling): repair OpenShift overlay for the KEDA+EPP saturation guide by @mamy-CS in https://github.com/llm-d/llm-d/pull/2183
* new release matrix by @diegocastanibm in https://github.com/llm-d/llm-d/pull/2016
* ci: collapse duplicated platform-parsing steps in build-image by @diegocastanibm in https://github.com/llm-d/llm-d/pull/2173
* Enable "guide-specific" workload (`guide_optimized-baseline_1`) for `optimized-baseline` by @maugustosilva in https://github.com/llm-d/llm-d/pull/1827
* feat(autoscaling): add OpenShift support to the KEDA+EPP queue guide by @mamy-CS in https://github.com/llm-d/llm-d/pull/2182
* feat(precise): Serve render from the model server pods by @albertoperdomo2 in https://github.com/llm-d/llm-d/pull/2188
* feat(precise): enable KV event replay buffer for index recovery by @RishabhSaini in https://github.com/llm-d/llm-d/pull/2196
* docs(wide-ep-lws): document aiperf command for GLM-5.2 benchmarks by @elvircrn in https://github.com/llm-d/llm-d/pull/2202
* ci: Fix XPU wide-ep failure by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/2164
* feat(autoscaling): add queue-based KEDA+EPP autoscaling nightly (OCP GPU) by @mamy-CS in https://github.com/llm-d/llm-d/pull/2192
* docs(pd-disaggregation): document TP-ratio and NIXL-cache-staleness caveats by @roytman in https://github.com/llm-d/llm-d/pull/2187
* fix: batch-gateway guide by @zdtsw in https://github.com/llm-d/llm-d/pull/2205
* feat: added tpu support for multimodal serving by @capri-xiyue in https://github.com/llm-d/llm-d/pull/2199
* Add DisaggregatedSet deployment path for wide-ep by @panpan0000 in https://github.com/llm-d/llm-d/pull/1633
* autoscaling: recommend scaling path by @lionelvillard in https://github.com/llm-d/llm-d/pull/2178
* docs(optimized-baseline): fix helm values file variable expansion by @asm582 in https://github.com/llm-d/llm-d/pull/2177
* docs: add notes for Gemma4 when using tiered offloading by @zdtsw in https://github.com/llm-d/llm-d/pull/2172
* Fix Stale Kustomize Reference Left Behind by AMD vLLM Base Directory Relocation by @weizhoublue in https://github.com/llm-d/llm-d/pull/2163
* fix(ci): correct workflow name queried by precise-prefix-cache GKE TPU status job by @sudoalok in https://github.com/llm-d/llm-d/pull/2158
* fix(autoscaling): make the queue-based KEDA+EPP nightly deploy and validate reliably by @mamy-CS in https://github.com/llm-d/llm-d/pull/2208
* [ROCM] PD disaggregation guide with moriio by @vcave in https://github.com/llm-d/llm-d/pull/2147
* [ROCm] Fix nightly optimize baseline provider to use 'base' by @vcave in https://github.com/llm-d/llm-d/pull/2211
* Update nightly matrix by @diegocastanibm in https://github.com/llm-d/llm-d/pull/2197
* docs(e-disaggregation): rebalance E/P/D worker counts and TP, add TP=2 to encode workers by @roytman in https://github.com/llm-d/llm-d/pull/2189
* [Observability][Feature]: Add TPU metrics PodMonitor by @bzsuni in https://github.com/llm-d/llm-d/pull/2190
* fix(flow-control): repair user-facing guide breakages by @LukeAVanDrie in https://github.com/llm-d/llm-d/pull/2209
* deps(actions): bump github/codeql-action from 4 to 4.37.4 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/2169
* docs: use GAIE-conformant proxy terminology by @k21993 in https://github.com/llm-d/llm-d/pull/2171
* fix: align multimodal modelServers selector with multimodal-aggregation guide label by @weizhoublue in https://github.com/llm-d/llm-d/pull/2222
* Update llm-d-xpu image to 0.8.1 by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/2219
* Update feature table by @asm582 in https://github.com/llm-d/llm-d/pull/2175
* Update cron job to run at 3AM UTC daily by @diegocastanibm in https://github.com/llm-d/llm-d/pull/2195
* docs(artifacts): add Async Processor artifacts and fix its repo URL by @shimib in https://github.com/llm-d/llm-d/pull/2155
* docs(guides): Fix prerequisite ordering and improve readability in optimized-baseline guide by @haitwang-cloud in https://github.com/llm-d/llm-d/pull/2141
* docs(async/multitenant): render prometheusURL, drop the MODEL_A/MODEL_B placeholders by @shimib in https://github.com/llm-d/llm-d/pull/2145
* [SIGS] update SIG autoscaling info by @lionelvillard in https://github.com/llm-d/llm-d/pull/2144
* Fix: Prevent SGLang GKE Pods from Stalling on Missing PVCs by @weizhoublue in https://github.com/llm-d/llm-d/pull/2143
* docs(SIGS): update async repo links to llm-d/llm-d-async by @shimib in https://github.com/llm-d/llm-d/pull/2120
* docs(async): fix unconsumable quickstart payload in the async guides by @shimib in https://github.com/llm-d/llm-d/pull/2133
* docs(guides): make the multitenant publish() helper burst by @shimib in https://github.com/llm-d/llm-d/pull/2146
* chore(typos): clear nightly typo-scan false positives by @zdtsw in https://github.com/llm-d/llm-d/pull/2117
* docs(SIGS): fix public meeting calendar link by @petecheslock in https://github.com/llm-d/llm-d/pull/2227
* fix: quote variable expansion and remove broken link in guides/ by @arijitroy003 in https://github.com/llm-d/llm-d/pull/2102
* docs(gke): Add managed OTel instruction for cluster creation by @JeffLuoo in https://github.com/llm-d/llm-d/pull/2006
* docs(router): correct EPP running request metric references by @nourey in https://github.com/llm-d/llm-d/pull/2008
* docs: surface agentgateway as a supported proxyType in standalone router guides by @abhay1999 in https://github.com/llm-d/llm-d/pull/1719
* docs(async/multitenant): make the saturation divisor a rendered SAT_CAP placeholder by @shimib in https://github.com/llm-d/llm-d/pull/2135
* docs(guides): point async guide at the renamed chart (charts/llm-d-async) by @shimib in https://github.com/llm-d/llm-d/pull/2099
* docs(operations): add LiteLLM and Kong AI Gateway guides for serving external APIs by @nicolexin in https://github.com/llm-d/llm-d/pull/2156
* feat(autoscaling): add scale-event validation to the queue-based KEDA+EPP nightly by @mamy-CS in https://github.com/llm-d/llm-d/pull/2228
* Updated llm-d router metrics names, labels and descriptions by @ahg-g in https://github.com/llm-d/llm-d/pull/2231
* Exclude non-serving requester pods from the InferencePool by @diegocastanibm in https://github.com/llm-d/llm-d/pull/2212
* deps(actions): bump actions/checkout from 6 to 7 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/2236
* deps(actions): bump actions/setup-python from 5 to 7 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/2237
* deps(actions): bump github/codeql-action from 4.37.4 to 4.37.6 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/2235
* deps(actions): bump peter-evans/create-pull-request from 7 to 8 by @dependabot[bot] in https://github.com/llm-d/llm-d/pull/2234
* Moved disagg operational guides to docs/operations by @ahg-g in https://github.com/llm-d/llm-d/pull/2238
* docs(release): snapshot release testing matrix for v0.9.0-rc.1 by @github-actions[bot] in https://github.com/llm-d/llm-d/pull/2232
* docs(release): document the human sign-off step for release matrix PRs by @diegocastanibm in https://github.com/llm-d/llm-d/pull/2242
* Fix broken links by @davidgs in https://github.com/llm-d/llm-d/pull/2244
* docs: One last fix of broken links by @davidgs in https://github.com/llm-d/llm-d/pull/2245
* consolidate and remove llm-d image overrides by @liu-cong in https://github.com/llm-d/llm-d/pull/1898
* fixed file patch name by @ahg-g in https://github.com/llm-d/llm-d/pull/2247
* Updated all guides to ensure namespaces can be OPTIONALLY deleted on CI/CD by @maugustosilva in https://github.com/llm-d/llm-d/pull/2243
* fix: WVA HPA guide fails to install in non-default namespaces by @willmj in https://github.com/llm-d/llm-d/pull/1994
* Well-lit path and guide: P2P KV cache sharing by @nilig in https://github.com/llm-d/llm-d/pull/2067
* build(xpu): use official vLLM v0.26.0 image by @xiaojun-zhang in https://github.com/llm-d/llm-d/pull/2251
* guides(pd-disaggregation): add provider overlays, placement policy details, and HPA to the DS guide by @BenjaminBraunDev in https://github.com/llm-d/llm-d/pull/2214
* multimodal-serving-guide-E/PD-heterogeneous-gpu-xpu-using-sglang by @xiaojun-zhang in https://github.com/llm-d/llm-d/pull/2113
* [ci/test]: Update gke workflows to use the cluster in us east5  by @rahulgurnani in https://github.com/llm-d/llm-d/pull/2250
* Support tiered prefix cache on Intel XPU with offloading connector by @XinyuYe-Intel in https://github.com/llm-d/llm-d/pull/1230
* Revert #2250 by @rahulgurnani in https://github.com/llm-d/llm-d/pull/2256
* ci: Remove Redundant  modelserver_kustomize_path  Input by @weizhoublue in https://github.com/llm-d/llm-d/pull/2254
* docs: fix broken link in tiered-prefix-cache guide by @michalmalka in https://github.com/llm-d/llm-d/pull/2241
* feat(guides): add ModelExpress P2P weight-loading guide by @wseaton in https://github.com/llm-d/llm-d/pull/1608
* guides(p2p): clarify block-size requirements by @nilig in https://github.com/llm-d/llm-d/pull/2255
* Update ROCm baseline nightly to use amd-ci provider by @vcave in https://github.com/llm-d/llm-d/pull/2226
* Add davidgs to the OWNERS file by @davidgs in https://github.com/llm-d/llm-d/pull/2042
* guides for inference in RL/Verl by @ezrasilvera in https://github.com/llm-d/llm-d/pull/2055
* docs: remove monitoring values from default router install commands by @RahilOp in https://github.com/llm-d/llm-d/pull/2138
* Add performance benchmarks for service mode high availability by @rlakhtakia in https://github.com/llm-d/llm-d/pull/2185
* Upgrade FMA to release v0.6.4 by @aavarghese in https://github.com/llm-d/llm-d/pull/2259
* Fix guides typo by @lxy-alexander in https://github.com/llm-d/llm-d/pull/2257
* add routing name by @diegocastanibm in https://github.com/llm-d/llm-d/pull/2258
* update nightly matrix by @diegocastanibm in https://github.com/llm-d/llm-d/pull/2262
* docs(workload-autoscaling): restructure guides into per-variant subdirs by @mamy-CS in https://github.com/llm-d/llm-d/pull/2264
* docs: use official XPU SGLang image by @xiaojun-zhang in https://github.com/llm-d/llm-d/pull/2261
* guides(workload-autoscaling): fix saturation guide EPP flow control enablement by @asm582 in https://github.com/llm-d/llm-d/pull/2252
* Image component resturcture and v0.26.0 bump by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/2260
* fix: Disable USE_SCCACHE when the sccache fallback kicks in by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/2224
* refactor(recipes): add shared KEDA OCP metrics-reader auth component by @mamy-CS in https://github.com/llm-d/llm-d/pull/2265
* feat(workload-autoscaling): add guide.yaml for keda-epp-queue and keda-epp-saturation by @mamy-CS in https://github.com/llm-d/llm-d/pull/2273
* docs(contributing): Add CNCF license policy requirement for new dependencies by @davidgs in https://github.com/llm-d/llm-d/pull/2275
* Stale workflow filename left behind in TPU consolidate-status after nightly rename by @weizhoublue in https://github.com/llm-d/llm-d/pull/2268
* feat(workload-autoscaling): add guide.yaml for wva; retire optimized-baseline-autoscaling/ by @mamy-CS in https://github.com/llm-d/llm-d/pull/2274
* updating images preparing for v0.9.0 release by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/2206
* feat(workload-autoscaling): guide.yaml for slo-aware + multi-inference-pool; scale-event verify for keda-epp-queue by @mamy-CS in https://github.com/llm-d/llm-d/pull/2278
* install CRDs + fix patch + declare which directories we skip by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/2267
* fix artifact downloads canceling jobs + workflowcall run ids by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/2279
* revert artifact upload version bump by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/2282
* docs(p2p): apply #2067 review follow-ups by @nilig in https://github.com/llm-d/llm-d/pull/2277
* fix(ci): stop tiered-prefix-cache GKE GPU nightly lanes from cancelling each other by @sudoalok in https://github.com/llm-d/llm-d/pull/2161
* Fixing WVA Namespace Overrides: Point the Controller's Watch Target at the Install Namespace - #2253 by @lionelvillard in https://github.com/llm-d/llm-d/pull/2283
* fix(autoscaling): set WVA --watch-namespace in guide.yaml, not just README by @mamy-CS in https://github.com/llm-d/llm-d/pull/2284
* [Guides] Update dsv-4 guides by @ilmarkov in https://github.com/llm-d/llm-d/pull/2057
* reorganize the rollouts docs as a guide by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/2266
* Add Grafana dashboard setup documentation for flow control by @alexagriffith in https://github.com/llm-d/llm-d/pull/1629
* Updating llm-d router metrics across guides by @ahg-g in https://github.com/llm-d/llm-d/pull/2288
* guides(wide-ep-lws): precise prefix-cache routing variant by @nilig in https://github.com/llm-d/llm-d/pull/2203
* Coordinator's guide by @roytman in https://github.com/llm-d/llm-d/pull/2119
* docs: update flow control configuration and observability by @alexagriffith in https://github.com/llm-d/llm-d/pull/2249
* Fix nightly typos by @Geun-Oh in https://github.com/llm-d/llm-d/pull/2291
* fix: wrong KEDA_VERSION format in download URL by @weizhoublue in https://github.com/llm-d/llm-d/pull/2290
* docs(observability): add per-guide troubleshooting for the optimizedbaseline by @gyliu513 in https://github.com/llm-d/llm-d/pull/2129
* Fix oneCCL init failure for tiered-prefix-cache on Intel XPU by @yuanwu2017 in https://github.com/llm-d/llm-d/pull/2270
* docs(flow-control): make use-case verification observable and fix guide friction by @LukeAVanDrie in https://github.com/llm-d/llm-d/pull/2213
* fix(xpu): use llm-d-xpu main image by @xiaojun-zhang in https://github.com/llm-d/llm-d/pull/2289
* fix(workload-autoscaling): remove obsolete CRD step by @mamy-CS in https://github.com/llm-d/llm-d/pull/2287
* Organized the batch guides similar to other workload-centric ones by @ahg-g in https://github.com/llm-d/llm-d/pull/2295
* component bumps by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/2285
* ci: restore bespoke flow-control nightly e2e by @LukeAVanDrie in https://github.com/llm-d/llm-d/pull/1918
* Add variables `GATEWAY_API_URL`, `GAIE_URL` and `ROUTER_RELEASE_URL` automatically calculated from `guides/env.sh` by @maugustosilva in https://github.com/llm-d/llm-d/pull/2299
* Update image tags by @diegocastanibm in https://github.com/llm-d/llm-d/pull/2294
* Harden P2P cache-sharing guide and update GLM results by @nilig in https://github.com/llm-d/llm-d/pull/2296
* precommit linting by @Gregory-Pereira in https://github.com/llm-d/llm-d/pull/2301

## New Contributors
* @joshuayao made their first contribution in https://github.com/llm-d/llm-d/pull/1772
* @NickLucche made their first contribution in https://github.com/llm-d/llm-d/pull/1543
* @AayushSaini101 made their first contribution in https://github.com/llm-d/llm-d/pull/1971
* @jtechapps made their first contribution in https://github.com/llm-d/llm-d/pull/1922
* @yao531441 made their first contribution in https://github.com/llm-d/llm-d/pull/1925
* @UranusSeven made their first contribution in https://github.com/llm-d/llm-d/pull/1986
* @XinyuYe-Intel made their first contribution in https://github.com/llm-d/llm-d/pull/1731
* @yehuditkerido made their first contribution in https://github.com/llm-d/llm-d/pull/1884
* @ishwar170695 made their first contribution in https://github.com/llm-d/llm-d/pull/1997
* @fossabot made their first contribution in https://github.com/llm-d/llm-d/pull/2013
* @yangspirit made their first contribution in https://github.com/llm-d/llm-d/pull/1903
* @nourey made their first contribution in https://github.com/llm-d/llm-d/pull/1981
* @eating-chen made their first contribution in https://github.com/llm-d/llm-d/pull/1974
* @noalimoy made their first contribution in https://github.com/llm-d/llm-d/pull/2075
* @davidgs made their first contribution in https://github.com/llm-d/llm-d/pull/2036
* @haitwang-cloud made their first contribution in https://github.com/llm-d/llm-d/pull/2085
* @tyuchn made their first contribution in https://github.com/llm-d/llm-d/pull/2093
* @MikeSpreitzer made their first contribution in https://github.com/llm-d/llm-d/pull/2100
* @aavarghese made their first contribution in https://github.com/llm-d/llm-d/pull/2101
* @arijitroy003 made their first contribution in https://github.com/llm-d/llm-d/pull/2103
* @cheng-hsiang-chiu made their first contribution in https://github.com/llm-d/llm-d/pull/2024
* @PrateekKumar1709 made their first contribution in https://github.com/llm-d/llm-d/pull/2153
* @breno-costa made their first contribution in https://github.com/llm-d/llm-d/pull/2179
* @albertoperdomo2 made their first contribution in https://github.com/llm-d/llm-d/pull/2188
* @RishabhSaini made their first contribution in https://github.com/llm-d/llm-d/pull/2196
* @panpan0000 made their first contribution in https://github.com/llm-d/llm-d/pull/1633
* @bzsuni made their first contribution in https://github.com/llm-d/llm-d/pull/2190
* @k21993 made their first contribution in https://github.com/llm-d/llm-d/pull/2171
* @JeffLuoo made their first contribution in https://github.com/llm-d/llm-d/pull/2006
* @abhay1999 made their first contribution in https://github.com/llm-d/llm-d/pull/1719
* @github-actions[bot] made their first contribution in https://github.com/llm-d/llm-d/pull/2232
* @willmj made their first contribution in https://github.com/llm-d/llm-d/pull/1994
* @michalmalka made their first contribution in https://github.com/llm-d/llm-d/pull/2241
* @RahilOp made their first contribution in https://github.com/llm-d/llm-d/pull/2138
* @lxy-alexander made their first contribution in https://github.com/llm-d/llm-d/pull/2257
* @Geun-Oh made their first contribution in https://github.com/llm-d/llm-d/pull/2291

**Full Changelog**: https://github.com/llm-d/llm-d/compare/v0.8.0...v0.9.0
