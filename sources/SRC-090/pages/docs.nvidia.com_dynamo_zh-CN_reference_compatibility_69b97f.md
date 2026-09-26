source: https://docs.nvidia.com/dynamo/zh-CN/reference/compatibility
lastmod: 2026-09-24T00:15:31.517Z

# Compatibility

Hardware, platform, feature, and mixed-version support for Dynamo

Compatibility by Version

KVBM deprecated with removal targeted for v1.6.0; CRD storage version promoted to v1beta1 and the v1alpha1 admission webhook endpoints removed; Go EPP removed in favor of the Rust EPP shipped inside the Frontend image; Dynamo Snapshot moved to a standalone operator and chart, dropping the bundled snapshot chart, snapshot-agent image and DynamoCheckpoint CRD; AIConfigurator renamed to AISimulate; unified-backend entry point removed from the vLLM and SGLang workers; UCX 1.21.x.

These are the backend versions tested and supported for this release. TensorRT-LLM does not support Python 3.11.

The card above covers one release at a time. To compare CUDA toolkit and minimum driver requirements across releases per backend, jump to the [Release Support Matrix](https://docs.nvidia.com/dynamo/reference/compatibility#release-support-matrix) at the bottom of this page. For extended driver compatibility beyond the listed minimums, including forward compatibility and `cuda-compat`

packages, see the [CUDA Compatibility documentation](https://docs.nvidia.com/deploy/cuda-compatibility/latest/).

See [Release Artifacts](https://docs.nvidia.com/dynamo/reference/release-artifacts) for the full artifact inventory — container images, wheels, Helm charts, and crates — [Local Installation](https://docs.nvidia.com/dynamo/dev/cli/installation/install-dynamo) for host OS and architecture requirements, and [Model Early Access Builds](https://docs.nvidia.com/dynamo/reference/model-early-access-builds) for per-model early access container builds. For backend-specific runtime workarounds — including the local `docker run --network host`

hang first reported on Amazon Linux 2023 — see [TensorRT-LLM Known Issues](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/backends/tensor-rt-llm/known-issues).

## Mixed-Version Compatibility

Dynamo supports mixed-version operation between frontends and workers across an N-2 window: the current release and the two immediately previous release lines. Any frontend and worker combination within that window is supported in both age directions. For example, a current frontend can serve workers from either previous release, and a frontend from either previous release can serve current workers.

A single frontend can discover worker generations from multiple supported releases for the same logical deployment. N-3 and older combinations are unsupported unless a narrower exception is explicitly documented. An explicitly enabled feature may also reject a mixed-version combination when its semantics cannot be represented safely by the other version.

This guarantee covers the frontend-to-worker discovery metadata and wire protocols owned by Dynamo. It does not establish a compatibility window for direct worker-to-worker protocols, such as prefill-to-decode communication.

### Rolling Update Behavior

In Kubernetes deployments, worker spec changes during a rolling update create generation-specific Dynamo runtime namespaces (service-discovery scopes, not Kubernetes namespaces). The frontend watches the deployment’s base runtime namespace prefix, so it can discover overlapping generations without allowing direct worker-to-worker communication across those generations. In a disaggregated deployment, prefill and decode workers in the same generation share one runtime namespace and remain isolated from other generations.

The frontend excludes incomplete or unready namespaces from routing. When multiple ready WorkerSets are available, it selects a WorkerSet at random with weight proportional to its worker count, then applies the configured routing policy within that WorkerSet.

Worker count is a capacity approximation, not a measurement of end-to-end serving capacity. Selection between WorkerSets also does not provide request stickiness.

## Feature Support

Hover a noted cell or focus it with the keyboard to view its compatibility note.

### Per-Backend Detail

###### vLLM

###### SGLang

###### TensorRT-LLM

vLLM offers the broadest feature coverage in Dynamo, with full support for disaggregated serving, KV-aware routing, KV block management, LoRA adapters, and multimodal inference including video and audio.

*Source: docs/backends/vllm/README.md*

### Feature Interactions

Pairwise feature-by-feature compatibility within each backend. Each cell reports whether the row feature works together with the column feature.

###### vLLM

###### SGLang

###### TensorRT-LLM

| Disaggregated Serving | KV-Aware Routing | SLA-Based Planner | KV Block Manager | Multimodal | Request Migration | Request Cancellation | LoRA | Tool Calling | Speculative Decoding | |
|---|---|---|---|---|---|---|---|---|---|---|
| Disaggregated Serving | ||||||||||
| KV-Aware Routing | ||||||||||
| SLA-Based Planner | ||||||||||
| KV Block Manager | ||||||||||
| Multimodal | ||||||||||
| Request Migration | ||||||||||
| Request Cancellation | ||||||||||
| LoRA | ||||||||||
| Tool Calling | ||||||||||
| Speculative Decoding |

Each cell reports whether the row feature works together with the column feature. Blank cells mirror the populated lower triangle. Hover a noted cell or focus it with the keyboard to view its note.

## Release Support Matrix

Every stable release and patch, grouped by minor line — newest first. Expand a line to see each release’s backend pins, CUDA toolkit, and minimum driver, ordered CUDA 12 before CUDA 13. Releases predating per-release CUDA tracking are listed with their requirements marked “Not recorded” rather than dropped. Platform previews and model-specific builds are excluded; the notes below call out the ones whose toolkit support differs, and the [Releases (machine-readable)](https://docs.nvidia.com/dynamo/reference/releases-data) page has the full inventory.

## 1.5.x

| Release | Backend | Engine | CUDA toolkit | Min driver | NIXL | Note |
|---|---|---|---|---|---|---|
| v1.5.0 | SGLang | 0.5.18 | 13.0 | 580.xx+ | 1.4.0 | — |
| TensorRT-LLM | 1.3.0rc25 | 13.1 | 580.xx+ | 1.3.1 | — | |
| vLLM | 0.28.0 | 13.0 | 580.xx+ | 1.3.2 | — |

## 1.4.x

| Release | Backend | Engine | CUDA toolkit | Min driver | NIXL | Note |
|---|---|---|---|---|---|---|
| v1.4.2 | SGLang | 0.5.16 | 13.0 | 580.xx+ | 1.3.0 | — |
| TensorRT-LLM | 1.3.0rc22 | 13.1 | 580.xx+ | 1.3.1 | — | |
| vLLM | 0.26.0 | 13.0 | 580.xx+ | 1.3.2 | — | |
| v1.4.1 | SGLang | 0.5.16 | 13.0 | 580.xx+ | 1.3.0 | — |
| TensorRT-LLM | 1.3.0rc22 | 13.1 | 580.xx+ | 1.3.1 | — | |
| vLLM | 0.26.0 | 13.0 | 580.xx+ | 1.3.2 | — | |
| v1.4.0 | SGLang | 0.5.16 | 13.0 | 580.xx+ | 1.3.0 | — |
| TensorRT-LLM | 1.3.0rc22 | 13.1 | 580.xx+ | 1.3.1 | — | |
| vLLM | 0.26.0 | 13.0 | 580.xx+ | 1.3.2 | — |

## 1.3.x

| Release | Backend | Engine | CUDA toolkit | Min driver | NIXL | Note |
|---|---|---|---|---|---|---|
| v1.3.1 | SGLang | 0.5.14 | 13.0 | 580.xx+ | 1.3.2 | — |
| TensorRT-LLM | 1.3.0rc19 | 13.1 | 580.xx+ | 1.0.1 | — | |
| vLLM | 0.23.0 | 13.0 | 580.xx+ | 1.1.0 | — | |
| v1.3.0 | SGLang | 0.5.14 | 13.0 | 580.xx+ | 1.3.0 | — |
| TensorRT-LLM | 1.3.0rc19 | 13.1 | 580.xx+ | 1.0.1 | — | |
| vLLM | 0.23.0 | 13.0 | 580.xx+ | 1.1.0 | — |

## 1.2.x

| Release | Backend | Engine | CUDA toolkit | Min driver | NIXL | Note |
|---|---|---|---|---|---|---|
| v1.2.1 | SGLang | 0.5.11 | 12.9 | 575.xx+ | 1.0.1 | — |
| vLLM | 0.20.1 | 12.9 | 575.xx+ | 0.10.1 | — | |
| SGLang | 0.5.11 | 13.0 | 580.xx+ | 1.0.1 | — | |
| TensorRT-LLM | 1.3.0rc14 | 13.1 | 580.xx+ | 0.10.1 | — | |
| vLLM | 0.20.1 | 13.0 | 580.xx+ | 0.10.1 | — | |
| v1.2.0 | SGLang | 0.5.11 | 12.9 | 575.xx+ | 1.0.1 | — |
| vLLM | 0.20.1 | 12.9 | 575.xx+ | 0.10.1 | — | |
| SGLang | 0.5.11 | 13.0 | 580.xx+ | 1.0.1 | — | |
| TensorRT-LLM | 1.3.0rc14 | 13.1 | 580.xx+ | 0.10.1 | — | |
| vLLM | 0.20.1 | 13.0 | 580.xx+ | 0.10.1 | — |

## 1.1.x

| Release | Backend | Engine | CUDA toolkit | Min driver | NIXL | Note |
|---|---|---|---|---|---|---|
| v1.1.1 | SGLang | 0.5.10.post1 | 12.9 | 575.xx+ | 1.0.1 | — |
| vLLM | 0.19.0 | 12.9 | 575.xx+ | 0.10.1 | — | |
| SGLang | 0.5.10.post1 | 13.0 | 580.xx+ | 1.0.1 | — | |
| TensorRT-LLM | 1.3.0rc11 | 13.1 | 580.xx+ | 0.10.1 | — | |
| vLLM | 0.19.0 | 13.0 | 580.xx+ | 0.10.1 | — | |
| v1.1.0 | SGLang | 0.5.10.post1 | 12.9 | 575.xx+ | 1.0.1 | — |
| vLLM | 0.19.0 | 12.9 | 575.xx+ | 0.10.1 | — | |
| SGLang | 0.5.10.post1 | 13.0 | 580.xx+ | 1.0.1 | — | |
| TensorRT-LLM | 1.3.0rc11 | 13.1 | 580.xx+ | 0.10.1 | — | |
| vLLM | 0.19.0 | 13.0 | 580.xx+ | 0.10.1 | — |

## 1.0.x

| Release | Backend | Engine | CUDA toolkit | Min driver | NIXL | Note |
|---|---|---|---|---|---|---|
| v1.0.2 | SGLang | 0.5.9 | 12.9 | 575.xx+ | 0.10.1 | — |
| vLLM | 0.16.0 | 12.9 | 575.xx+ | 0.10.1 | — | |
| SGLang | 0.5.9 | 13.0 | 580.xx+ | 0.10.1 | — | |
| TensorRT-LLM | 1.3.0rc5.post1 | 13.1 | 580.xx+ | 0.10.1 | — | |
| vLLM | 0.16.0 | 13.0 | 580.xx+ | 0.10.1 | — | |
| v1.0.1 | SGLang | 0.5.9 | 12.9 | 575.xx+ | 0.10.1 | — |
| vLLM | 0.16.0 | 12.9 | 575.xx+ | 0.10.1 | — | |
| SGLang | 0.5.9 | 13.0 | 580.xx+ | 0.10.1 | — | |
| TensorRT-LLM | 1.3.0rc5.post1 | 13.1 | 580.xx+ | 0.10.1 | — | |
| vLLM | 0.16.0 | 13.0 | 580.xx+ | 0.10.1 | — | |
| v1.0.0 | SGLang | 0.5.9 | 12.9 | 575.xx+ | 0.10.1 | — |
| vLLM | 0.16.0 | 12.9 | 575.xx+ | 0.10.1 | — | |
| SGLang | 0.5.9 | 13.0 | 580.xx+ | 0.10.1 | — | |
| TensorRT-LLM | 1.3.0rc5.post1 | 13.1 | 580.xx+ | 0.10.1 | — | |
| vLLM | 0.16.0 | 13.0 | 580.xx+ | 0.10.1 | — |

## 0.9.x

| Release | Backend | Engine | CUDA toolkit | Min driver | NIXL | Note |
|---|---|---|---|---|---|---|
| v0.9.1 | SGLang | 0.5.8 | 12.9 | 575.xx+ | 0.9.0 | — |
| vLLM | 0.14.1 | 12.9 | 575.xx+ | 0.9.0 | — | |
| TensorRT-LLM | 1.3.0rc3 | 13.0 | 580.xx+ | 0.9.0 | — | |
| v0.9.0 | SGLang | 0.5.8 | 12.9 | 575.xx+ | 0.9.0 | — |
| vLLM | 0.14.1 | 12.9 | 575.xx+ | 0.9.0 | — | |
| TensorRT-LLM | 1.3.0rc1 | 13.0 | 580.xx+ | 0.9.0 | — |

## 0.8.x

| Release | Backend | Engine | CUDA toolkit | Min driver | NIXL | Note |
|---|---|---|---|---|---|---|
| v0.8.1 | SGLang | 0.5.6.post2 | 12.9 | 575.xx+ | 0.8.0 | — |
| vLLM | 0.12.0 | 12.9 | 575.xx+ | 0.8.0 | — | |
| SGLang | 0.5.6.post2 | 13.0 | 580.xx+ | 0.8.0 | Experimental | |
| TensorRT-LLM | 1.2.0rc6.post1 | 13.0 | 580.xx+ | 0.8.0 | — | |
| vLLM | 0.12.0 | 13.0 | 580.xx+ | 0.8.0 | Experimental | |
| v0.8.0 | SGLang | 0.5.6.post2 | 12.9 | 575.xx+ | 0.8.0 | — |
| vLLM | 0.12.0 | 12.9 | 575.xx+ | 0.8.0 | — | |
| SGLang | 0.5.6.post2 | 13.0 | 580.xx+ | 0.8.0 | Experimental | |
| TensorRT-LLM | 1.2.0rc6.post1 | 13.0 | 580.xx+ | 0.8.0 | — | |
| vLLM | 0.12.0 | 13.0 | 580.xx+ | 0.8.0 | Experimental |

## 0.7.x

| Release | Backend | Engine | CUDA toolkit | Min driver | NIXL | Note |
|---|---|---|---|---|---|---|
| v0.7.1 | SGLang | 0.5.4.post3 | 12.8 | 570.xx+ | 0.8.0 | — |
| vLLM | 0.11.0 | 12.9 | 575.xx+ | 0.8.0 | — | |
| TensorRT-LLM | 1.2.0rc3 | 13.0 | 580.xx+ | 0.8.0 | — | |
| v0.7.0 | SGLang | 0.5.4.post3 | 12.9 | 575.xx+ | 0.8.0 | — |
| vLLM | 0.11.0 | 12.8 | 570.xx+ | 0.8.0 | — | |
| TensorRT-LLM | 1.2.0rc2 | 13.0 | 580.xx+ | 0.8.0 | — |

## 0.6.x

| Release | Backend | Engine | CUDA toolkit | Min driver | NIXL | Note |
|---|---|---|---|---|---|---|
| v0.6.1 | SGLang | 0.5.3.post2 | Not recorded | Not recorded | 0.6.0 | — |
| TensorRT-LLM | 1.1.0rc5 | Not recorded | Not recorded | 0.6.0 | — | |
| vLLM | 0.11.0 | Not recorded | Not recorded | 0.6.0 | — | |
| v0.6.0 | SGLang | 0.5.3.post2 | Not recorded | Not recorded | 0.6.0 | — |
| TensorRT-LLM | 1.1.0rc5 | Not recorded | Not recorded | 0.6.0 | — | |
| vLLM | 0.11.0 | Not recorded | Not recorded | 0.6.0 | — |

- Patch versions (e.g. v0.8.1.post1, v0.7.0.post1) have the same CUDA support as their base version.
- Early access v1.1.0-dev.* images follow the same CUDA matrix as v1.0.2. The v1.2.0-deepseek-v4-dev.3 vLLM container is CUDA 13.0 multi-arch; the SGLang containers split by arch (CUDA 12.9 on amd64, CUDA 13.0 on arm64).
- Experimental CUDA 13 images are not published for all versions.

Driver already installed? Read across from your version — each cell is the newest release that backend can run on it. A driver meeting a higher floor also runs everything below it.