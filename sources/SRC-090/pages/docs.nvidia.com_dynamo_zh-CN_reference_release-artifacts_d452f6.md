source: https://docs.nvidia.com/dynamo/zh-CN/reference/release-artifacts
lastmod: 2026-09-23T23:30:39.914Z

# Release Artifacts

This page lists the published NVIDIA Dynamo release artifacts for the current stable release and where to find each one. Container images live on NVIDIA NGC under `nvcr.io/nvidia/ai-dynamo/`

; every tag and install command below is click-to-copy.

See [Compatibility](https://docs.nvidia.com/dynamo/reference/compatibility) for hardware, platform, and backend feature support, [Dynamo Enterprise Support](https://docs.nvidia.com/dynamo/dev/reference/enterprise/overview) for coverage terms, and [Model Early Access Builds](https://docs.nvidia.com/dynamo/reference/model-early-access-builds) for per-model early access container builds.

## Current Release

Release artifacts

### 35 artifacts for v1.5.06 container images for v1.5.03 Python wheels for v1.5.01 Helm charts for v1.5.025 Rust crates for v1.5.0

Runtime containers

vLLM backend runtime · vLLM v0.28.0 · CUDA 13.0 · AMD64/ARM64

SGLang backend runtime · SGLang v0.5.18 · CUDA 13.0 · AMD64/ARM64

TensorRT-LLM backend runtime · TRT-LLM v1.3.0rc25 · CUDA 13.1 · AMD64/ARM64

Component containers

OpenAI-compatible API gateway with Endpoint Prediction Protocol (EPP) · AMD64/ARM64

Standalone Planner used by Profiler jobs and Planner pods · AMD64/ARM64

Operator that manages Dynamo deployments and CRDs · AMD64/ARM64

Python wheels

Main package with backend integrations (vLLM, SGLang, TRT-LLM) · Python 3.10–3.12 · Linux (glibc v2.28+)

Core Python bindings for the Dynamo runtime · Python 3.10–3.12 · Linux (glibc v2.28+)

KV Block Manager for disaggregated KV cache · Python 3.10–3.12 · Linux (glibc v2.28+)

Helm charts

Platform services (etcd, NATS) and the Dynamo Operator for a Dynamo cluster

Dynamo Rust crates

Core distributed runtime library · MSRV Rust v1.82

LLM inference engine · MSRV Rust v1.82

[dynamo-async-openai](https://crates.io/crates/dynamo-async-openai/1.0.2)Deprecated

Legacy OpenAI client; use dynamo-protocols · MSRV Rust v1.82 · final release

Memory management utilities · MSRV Rust v1.82

Configuration management · MSRV Rust v1.82

Tokenizer bindings for LLM inference · MSRV Rust v1.82

Inference engine simulator for benchmarking · MSRV Rust v1.82

KV-aware request routing library · MSRV Rust v1.82

Logical layer for the KV Block Manager · MSRV Rust v1.82

Request-to-lineage-hash contract for KV cache identity · MSRV Rust v1.82

Schemas and primitives for Dynamo data generation and replay traces · MSRV Rust v1.82

Dynamo RL worker discovery API · MSRV Rust v1.82

Lightweight HTTP benchmarks for Dynamo endpoints · MSRV Rust v1.82

Canonical truthy/falsy boolean flag parsing · MSRV Rust v1.82

Shared types for the KV Block Manager · MSRV Rust v1.82

KVBM configuration for Tokio, Rayon, and Messenger runtimes · MSRV Rust v1.82

CUDA kernels for the KV Block Manager · MSRV Rust v1.82

Physical block layer for the KV Block Manager · MSRV Rust v1.82

Distributed coordination primitives for KVBM · MSRV Rust v1.82

Frontend crate dependencies (independently versioned)

Async OpenAI-compatible API client · Independently versioned

Protocol parsers (SSE, JSON streaming) · Independently versioned

Tokenizer library for LLM inference · Independently versioned

Chat-template rendering used by the Dynamo Frontend · Independently versioned

Successor parser line to dynamo-parsers, consumed by the Frontend · Independently versioned

Rust BPE tokenizer backend consumed by the Frontend · Independently versioned

Every tag and command is click-to-copy. For TensorRT-LLM use the NGC container — not the ai-dynamo[trtllm] wheel.

**CUDA and driver requirements:** for the CUDA toolkit versions and minimum drivers per release, see the [Release Support Matrix](https://docs.nvidia.com/dynamo/reference/compatibility#release-support-matrix) on the Compatibility page.

### Pinned Environment

One copy-paste block that pins every install path — the backend runtime container, frontend and operator images, Helm chart, and wheel — to the same release.

Pinned environment

### Everything pinned to v1.5.0

docker pull nvcr.io/nvidia/ai-dynamo/sglang-runtime:1.5.0 docker pull nvcr.io/nvidia/ai-dynamo/dynamo-frontend:1.5.0 docker pull nvcr.io/nvidia/ai-dynamo/kubernetes-operator:1.5.0 helm install dynamo-platform https://helm.ngc.nvidia.com/nvidia/ai-dynamo/charts/dynamo-platform-1.5.0.tgz uv pip install "ai-dynamo[sglang]==1.5.0"

docker pull nvcr.io/nvidia/ai-dynamo/tensorrtllm-runtime:1.5.0 docker pull nvcr.io/nvidia/ai-dynamo/dynamo-frontend:1.5.0 docker pull nvcr.io/nvidia/ai-dynamo/kubernetes-operator:1.5.0 helm install dynamo-platform https://helm.ngc.nvidia.com/nvidia/ai-dynamo/charts/dynamo-platform-1.5.0.tgz # TensorRT-LLM ships via the NGC container

docker pull nvcr.io/nvidia/ai-dynamo/vllm-runtime:1.5.0 docker pull nvcr.io/nvidia/ai-dynamo/dynamo-frontend:1.5.0 docker pull nvcr.io/nvidia/ai-dynamo/kubernetes-operator:1.5.0 helm install dynamo-platform https://helm.ngc.nvidia.com/nvidia/ai-dynamo/charts/dynamo-platform-1.5.0.tgz uv pip install "ai-dynamo[vllm]==1.5.0"

Assembled from the current release's artifact inventory.

## Known Issues

Known issues are tracked on the [Known Issues](https://docs.nvidia.com/dynamo/reference/releases/known-issues) reference page, including artifact-specific issues for older releases.


## Early Access Artifacts

**Early access artifacts do not go through QA validation.** They are experimental previews intended for early testing and feedback, and may contain bugs, breaking changes, or incomplete features. Use stable releases for production workloads.

Model-specific early access builds (`vX.Y.Z-<model>-dev.N`

) are tracked in [Model Early Access Builds](https://docs.nvidia.com/dynamo/reference/model-early-access-builds). Full-platform previews (`vX.Y.Z-dev.N`

) are summarized here.

###### Installing early access wheels (pypi.nvidia.com)


**Early access Python wheels** are published on the NVIDIA package index at [pypi.nvidia.com](https://pypi.nvidia.com/), not on the public [PyPI](https://pypi.org/) index. Like stable wheels, they are Linux (manylinux) builds for the Python versions in [Compatibility](https://docs.nvidia.com/dynamo/reference/compatibility); `pip`

/`uv`

on macOS or Windows will not find matching wheels. A git tag `v1.3.0-dev.N`

maps to a wheel version `1.3.0.devN`

:

**Nightlies:** `ai-dynamo`

and `ai-dynamo-runtime`

nightly builds from `main`

publish wheels tagged `*.devYYYYMMDD`

(since Apr 24, 2026); `kvbm`

joined the nightly train on Aug 2, 2026. Install with the same `--pre`

+ extra-index pattern. See [Nightly Releases](https://docs.nvidia.com/dynamo/reference/nightly-releases) for the full artifact list and container tags.

### v1.3.0-dev.1

Full-platform preview of v1.3.0, cut from `main`

after the TensorRT-LLM `1.3.0rc17`

upgrade (Jun 9, 2026) and superseded by the v1.3.0 GA release. Backends: SGLang `0.5.12.post1`

| TensorRT-LLM `1.3.0rc17`

| vLLM `0.22.0`

.

Complete runtime and component container matrix, `ai-dynamo`

/ `ai-dynamo-runtime`

/ `kvbm`

wheels at `1.3.0.dev1`

on pypi.nvidia.com, Rust crates at `1.3.0-dev.1`

on crates.io, and the `dynamo-platform`

and `snapshot`

Helm charts.

### Tag Lookup

Reverse lookup for any tag on this page or in [Model Early Access Builds](https://docs.nvidia.com/dynamo/reference/model-early-access-builds): pick a tag to see the release or build it belongs to, the runtimes it applies to, and its status.

Tag lookup

### Have a tag? Look it up.

13 known tags · current release + early access

Select a tag.

[v1.5.0 release notes](https://docs.nvidia.com/dynamo/dev/reference/releases/v1-5-0)

[v1.5.0 release notes](https://docs.nvidia.com/dynamo/dev/reference/releases/v1-5-0)

[Inkling recipe (main)](https://github.com/ai-dynamo/dynamo/blob/main/docs/recipes/inkling.mdx)

[GLM-5 NVFP4 recipe](https://docs.nvidia.com/dynamo/dev/recipes/glm-5-nvfp4)

[Recipe on release branch](https://github.com/ai-dynamo/dynamo/tree/release/1.3.0-minimax-m3-dev.1/recipes/minimax-m3)

[recipes/deepseek-v4 (main)](https://github.com/ai-dynamo/dynamo/tree/main/recipes/deepseek-v4)

[Nemotron-3-Ultra recipe](https://docs.nvidia.com/dynamo/dev/recipes/nemotron-3-ultra)

[Nemotron-3-Super recipe](https://docs.nvidia.com/dynamo/dev/recipes/nemotron-3-super)

[Kimi-K2.6 recipe](https://docs.nvidia.com/dynamo/dev/recipes/kimi-k2-6)

[Launch scripts (branch)](https://github.com/ai-dynamo/dynamo/tree/release/1.3.0-cosmos3-dev.1/examples/backends/vllm/launch)

[Release tag on GitHub](https://github.com/ai-dynamo/dynamo/releases/tag/v1.2.0-deepseek-v4-dev.3)

[Release tag on GitHub](https://github.com/ai-dynamo/dynamo/releases/tag/v1.2.0-deepseek-v4-dev.2)

[Release tag on GitHub](https://github.com/ai-dynamo/dynamo/releases/tag/v1.2.0-sglang-deepseek-v4-dev.1)

For the full release history — every release newest-first with its notes — see [Releases](https://docs.nvidia.com/dynamo/reference/releases).

###### Crates on crates.io — first publication


| Crate | First version | Published |
|---|---|---|
| dynamo-runtime | 0.1.0 | 2025-03-18 |
| dynamo-llm | 0.2.0 | 2025-05-01 |
| dynamo-async-openai | 0.4.1 | 2025-08-27 |
| dynamo-parsers | 0.5.0 | 2025-09-18 |
| dynamo-memory | 0.8.0 | 2026-01-15 |
| dynamo-config | 0.8.0 | 2026-01-15 |
| dynamo-tokens | 0.9.0 | 2026-02-12 |
| dynamo-mocker | 1.0.0 | 2026-03-13 |
| dynamo-kv-router | 1.0.0 | 2026-03-13 |
| dynamo-protocols | 1.1.0 | 2026-05-04 |
| dynamo-tokenizers | 1.2.0 | 2026-06-02 |

dynamo-async-openai is deprecated; 1.0.2 is its final release. Use dynamo-protocols for new dependencies.