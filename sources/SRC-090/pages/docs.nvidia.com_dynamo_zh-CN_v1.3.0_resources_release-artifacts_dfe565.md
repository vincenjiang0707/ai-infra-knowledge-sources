source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/resources/release-artifacts
lastmod: 2026-09-23T23:30:39.914Z

# Release Artifacts

This document provides a comprehensive inventory of all Dynamo release artifacts including container images, Python wheels, Helm charts, and Rust crates.


See also:[Support Matrix]for hardware and platform compatibility |[Feature Matrix]for backend feature support

Release history in this document begins at v0.6.0.

## Current Release: Dynamo v1.3.0


Early access:model-specific early access builds (`vX.Y.Z-<model>-dev.N`

) are tracked in[Model Early Access Builds]. Full-platform previews (`vX.Y.Z-dev.N`

) are listed under[Early Access Artifacts].

### Container Images

### Python Wheels

For TensorRT-LLM, use the NGC container — not the `ai-dynamo[trtllm]`

PyPI extra.
See the [NGC container collection](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/collections/ai-dynamo).

### Helm Charts

The `dynamo-crds`

Helm chart is deprecated as of v1.0.0; CRDs are now managed by the Dynamo Operator. The `dynamo-graph`

Helm chart is deprecated as of v0.9.0.

### Rust Crates

## Quick Install Commands

### Container Images (NGC)

For detailed run instructions, see the backend-specific guides: [vLLM](https://docs.nvidia.com/dynamo/v1.3.0/backends/v-llm) | [SGLang](https://docs.nvidia.com/dynamo/v1.3.0/backends/sg-lang) | [TensorRT-LLM](https://docs.nvidia.com/dynamo/v1.3.0/backends/tensor-rt-llm)

### Python Wheels (PyPI)

For detailed installation instructions, see the [Quickstart](https://docs.nvidia.com/dynamo/getting-started/quickstart) in the docs.

### Helm Charts (NGC)

For Kubernetes deployment instructions, see the [Kubernetes Installation Guide](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/start-here/installation-guide).

### Rust Crates (crates.io)

For API documentation, see each crate on [docs.rs](https://docs.rs/). To build Dynamo from source, see [Building from Source](https://github.com/ai-dynamo/dynamo#building-from-source).

**CUDA and Driver Requirements:** For detailed CUDA toolkit versions and minimum driver requirements for each container image, see the [Support Matrix](https://docs.nvidia.com/dynamo/v1.3.0/resources/support-matrix#cuda-and-driver-requirements).

## Known Issues

For a complete list of known issues, refer to the release notes for each version:

[v1.3.0 Release Notes](https://github.com/ai-dynamo/dynamo/releases/tag/v1.3.0)[v1.2.1 Release Notes](https://github.com/ai-dynamo/dynamo/releases/tag/v1.2.1)[v1.2.0 Release Notes](https://github.com/ai-dynamo/dynamo/releases/tag/v1.2.0)[v1.1.1 Release Notes](https://github.com/ai-dynamo/dynamo/releases/tag/v1.1.1)[v1.1.0 Release Notes](https://github.com/ai-dynamo/dynamo/releases/tag/v1.1.0)[v1.0.2 Release Notes](https://github.com/ai-dynamo/dynamo/releases/tag/v1.0.2)[v1.0.1 Release Notes](https://github.com/ai-dynamo/dynamo/releases/tag/v1.0.1)[v1.0.0 Release Notes](https://github.com/ai-dynamo/dynamo/releases/tag/v1.0.0)[v0.9.0 Release Notes](https://github.com/ai-dynamo/dynamo/releases/tag/v0.9.0)[v0.8.1 Release Notes](https://github.com/ai-dynamo/dynamo/releases/tag/v0.8.1)

### Known Artifact Issues

## Release Artifact History

Each bullet is a **delta** to what ships on NGC / Helm / PyPI / crates.io: net-new crates, removed Helm charts, or image lines that **split** or **appear** on the registry. See the inventory tables above for full matrices.

Grouped by release line, newest first; within each line the stable release precedes its early access tags. **Early access git tags** (`v*-dev.*`

) are summarized below; per-tag images and wheels for platform previews are spelled out in [Early Access Artifacts](https://docs.nvidia.com/dynamo/v1.3.0/resources/release-artifacts#early-access-artifacts), and model-specific builds in [Model Early Access Builds](https://docs.nvidia.com/dynamo/v1.3.0/resources/model-early-access-builds).

For backend version pins, see the version-pins table above and the [GitHub Releases](https://docs.nvidia.com/dynamo/v1.3.0/resources/release-artifacts#github-releases) table below.

**Stable Releases**

**v1.3.0**: Minor release.**Backends:**SGLang`v0.5.14`

(NIXL`v1.3.0`

), TRT-LLM`v1.3.0rc19`

(NIXL`v1.0.1`

), vLLM`v0.23.0`

(NIXL`v1.1.0`

); UCX`v1.20.x`

.**Images:**CUDA 12 container images discontinued — vLLM and SGLang runtimes ship CUDA 13.0, TensorRT-LLM CUDA 13.1; EFA variants published as`-efa`

.**Wheels:**GA wheels published as`1.3.0.post1`

(containers remain`:1.3.0`

).**v1.2.1**: Patch release. Same backend versions as v1.2.0: SGLang`v0.5.11`

(NIXL`v1.0.1`

), TRT-LLM`v1.3.0rc14`

(NIXL`v0.10.1`

), vLLM`v0.20.1`

(NIXL`v0.10.1`

).**v1.2.0**: Minor release (603 PRs from 82 authors since v1.1.1).**Backends:**SGLang`v0.5.11`

(NIXL`v1.0.1`

), TRT-LLM`v1.3.0rc14`

(NIXL`v0.10.1`

), vLLM`v0.20.1`

(NIXL`v0.10.1`

); UCX`v1.20.0`

.**APIs:**DGD/DGDR promoted to`v1beta1`

(migrate from`v1alpha1`

); duration config fields renamed with explicit unit suffixes (e.g.`*_ttl`

→`*_ttl_secs`

).**Routing:**CRTC is the default approximate KV router; Branch-Sharded KV Indexer.**Deploy:**Inter-pod GMS sidecar replaces the per-pod pattern; Dynamo Snapshot on CRI-O / OpenShift.**Models:**DeepSeek-V4 on vLLM; multimodal/diffusion (TRT-LLM text-to-image, SGLang disaggregated video).**Note:**CUDA 12 container images are discontinued starting v1.3.0.**v1.1.1**: Patch release. Same backend versions as v1.1.0: SGLang`v0.5.10.post1`

(NIXL`v1.0.1`

), TRT-LLM`v1.3.0rc11`

(NIXL`v0.10.1`

), vLLM`v0.19.0`

(NIXL`v0.10.1`

).**v1.1.0**:**Images:**Split Planner into its own`dynamo-planner`

image on NGC for Profiler jobs and Planner pods; worker and runtime images no longer bundle Planner (**artifact boundary change**, not a new engine capability).**Crates:**Firstpublication on crates.io for`1.y.z`

(multi-protocol types;`dynamo-protocols`

remains deprecated with final release`dynamo-async-openai`

).`1.0.2`

**v1.0.2 / v1.0.1**: No artifact additions or removals versus v1.0.0.**v1.0.0**:**Images:**`snapshot-agent`

, EFA variants for vLLM and TRT-LLM (AMD64 only).**Crates:**First publish of`dynamo-mocker`

,`dynamo-kv-router`

.**Helm:**Added`snapshot`

(preview); dropped deprecated`dynamo-crds`

from the publish stream (CRDs owned by the Operator).**v0.9.1**: No artifact additions or removals versus v0.9.0.**v0.9.0**:**Crates:**First publish of`dynamo-tokens`

.**Helm:**Dropped deprecated`dynamo-graph`

from the publish stream.**v0.8.0**:**Images:**`dynamo-frontend`

, CUDA 13 variants for vLLM and SGLang.**Crates:**First publish of`dynamo-memory`

,`dynamo-config`

.

**Dynamo Nightlies**

**New as of v1.1.0*:**and`ai-dynamo`

— nightly builds from`ai-dynamo-runtime`

publish wheels tagged`main`

. Install with`*.devYYYYMMDD`

or`pip`

using`uv`

and the same NVIDIA extra-index pattern as`--pre`

[Early Access Artifacts](https://docs.nvidia.com/dynamo/v1.3.0/resources/release-artifacts#early-access-artifacts).

* ** *.devYYYYMMDD** versioning for nightly

**wheels began**

`main`

**Apr 24, 2026**.

**Early Access Git Tags**

Model-specific early access builds (`vX.Y.Z-<model>-dev.N`

— nemotron, kimi, cosmos3, deepseek-v4, minimax, glm, inkling) are tracked in [Model Early Access Builds](https://docs.nvidia.com/dynamo/v1.3.0/resources/model-early-access-builds). Platform previews:

**v1.3.0-dev.1**:**Images:**full runtime matrix —`vllm-runtime`

(cuda12/cuda13/efa),`tensorrtllm-runtime`

(cuda13/efa),`sglang-runtime`

(cuda12/cuda13/efa), plus`dynamo-frontend`

,`dynamo-planner`

,`kubernetes-operator`

,`snapshot-agent`

.**Wheels:**`ai-dynamo`

,`ai-dynamo-runtime`

,`kvbm`

on[pypi.nvidia.com](https://pypi.nvidia.com/).**Crates:**on[crates.io](https://crates.io/)at`1.3.0-dev.1`

.**Helm:**`dynamo-platform`

,`snapshot`

at`1.3.0-dev.1`

(see[below](https://docs.nvidia.com/dynamo/v1.3.0/resources/release-artifacts#v130-dev1)).**v1.1.0-dev.3**:**Images:**`tensorrtllm-runtime:1.1.0-dev.3`

.**Wheels:**`ai-dynamo`

,`ai-dynamo-runtime`

on[pypi.nvidia.com](https://pypi.nvidia.com/)(see[below](https://docs.nvidia.com/dynamo/v1.3.0/resources/release-artifacts#v110-dev3)).**v1.1.0-dev.2**:**Images:**`sglang-runtime:1.1.0-dev.2`

,`tensorrtllm-runtime:1.1.0-dev.2`

.**Wheels:**`ai-dynamo`

,`ai-dynamo-runtime`

on[pypi.nvidia.com](https://pypi.nvidia.com/)(see[below](https://docs.nvidia.com/dynamo/v1.3.0/resources/release-artifacts#v110-dev2)).**v1.1.0-dev.1**:**Images:**vLLM, SGLang, TRT-LLM runtime matrix (CUDA 12 / 13 and EFA variants as listed),`dynamo-frontend`

,`kubernetes-operator`

,`snapshot-agent`

.**Wheels:**`ai-dynamo`

,`ai-dynamo-runtime`

on[pypi.nvidia.com](https://pypi.nvidia.com/).**Helm:**`dynamo-platform`

,`snapshot`

at`1.1.0-dev.1`

(see[below](https://docs.nvidia.com/dynamo/v1.3.0/resources/release-artifacts#v110-dev1)).

**Helm-Only Patches**

**v0.9.0.post1**: Republished`dynamo-platform`

Helm chart only (operator image tag correction).

**Backend-Only Patch Trains**

**v0.8.1.post1 / .post2 / .post3**: Republished TRT-LLM runtime image and PyPI wheels only.

### crates.io Rust Packages

These crates use repository `https://github.com/ai-dynamo/dynamo.git`

. The table lists each crate’s **first non-placeholder** publication on crates.io (excluding reservation uploads named `0.0.0-prerelease.0`

). Dates are from the crates.io registry index.

** dynamo-async-openai** is

**deprecated**;

**is its final crates.io release. Use**

`1.0.2`

**for new dependencies (**

`dynamo-protocols`

[crate](https://crates.io/crates/dynamo-protocols)).

** dynamo-tokenizers** is first published on crates.io at

**(the placeholder reservation**

`1.2.0`

**is omitted here like other reservation uploads).**

`0.0.0-prerelease.0`

### GitHub Releases

### Container Images


NGC Collection:[ai-dynamo]To access a specific version, append

`?version=TAG`

to the container URL:`https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/containers/{container}?version={tag}`


#### vllm-runtime

#### sglang-runtime

#### tensorrtllm-runtime

#### dynamo-frontend

#### kubernetes-operator

#### dynamo-planner

#### snapshot-agent

### Python Wheels


PyPI:[ai-dynamo]|[ai-dynamo-runtime]|[kvbm]To access a specific version:

`https://pypi.org/project/{package}/{version}/`


#### ai-dynamo (wheel)

#### ai-dynamo-runtime (wheel)

#### kvbm (wheel)

### Helm Charts


NGC Helm Registry:[ai-dynamo]Direct download:

`https://helm.ngc.nvidia.com/nvidia/ai-dynamo/charts/{chart}-{version}.tgz`


#### dynamo-crds (Helm chart) — Deprecated

The `dynamo-crds`

Helm chart is deprecated as of v1.0.0. CRDs are now managed by the Dynamo Operator.

#### dynamo-platform (Helm chart)

#### snapshot (Helm chart)

#### dynamo-graph (Helm chart) — Deprecated

`dynamo-graph`

Helm chart is deprecated as of v0.9.0.### Rust Crates


crates.io:[dynamo-runtime]|[dynamo-llm]|[dynamo-protocols]|[dynamo-async-openai](deprecated)|[dynamo-parsers]|[dynamo-memory]|[dynamo-config]|[dynamo-tokens]|[dynamo-tokenizers]|[kvbm-logical]To access a specific version:

`https://crates.io/crates/{crate}/{version}`


#### dynamo-runtime (crate)

#### dynamo-llm (crate)

#### dynamo-protocols (crate)

On crates.io, ** dynamo-protocols** lists

**as its first installable release (placeholder reservation**

`1.1.0`

**omitted here like other**

`0.0.0-prerelease.0`

**uploads). Earlier semver lines for the OpenAI-compatible client shipped under**

`0.0.0-prerelease.*`

**— see**

`dynamo-async-openai`

**below.**

`#### dynamo-async-openai (crate)`

#### dynamo-async-openai (crate)

**Deprecated.** Prefer ** dynamo-protocols**. This crate remains published on crates.io for manifests pinned to the old package name.

#### dynamo-parsers (crate)

#### dynamo-memory (crate)

#### dynamo-config (crate)

#### dynamo-tokens (crate)

#### dynamo-tokenizers (crate)

#### dynamo-mocker (crate)

#### dynamo-kv-router (crate)

#### kvbm-logical (crate)


## Early Access Artifacts

**Early access artifacts do not go through QA validation.** Early access builds are experimental previews intended for early testing and feedback. They may contain bugs, breaking changes, or incomplete features. Use stable releases for production workloads.

This section covers **platform previews** (`vX.Y.Z-dev.N`

— full-platform early access builds spanning all runtimes, wheels, crates, and Helm charts). Model-specific early access builds (`vX.Y.Z-<model>-dev.N`

) are tracked in [Model Early Access Builds](https://docs.nvidia.com/dynamo/v1.3.0/resources/model-early-access-builds).

**Early access Python wheels** are published on the NVIDIA package index at [pypi.nvidia.com](https://pypi.nvidia.com/), not on the public [PyPI](https://pypi.org/) index. Like stable wheels, they are **Linux (manylinux) builds** for the Python versions in the [Support Matrix](https://docs.nvidia.com/dynamo/v1.3.0/resources/support-matrix); `pip`

/`uv`

on macOS or Windows will not find matching wheels. Install on a supported Linux host or inside a Linux container.

Install by adding that URL as an extra index and allowing pre-releases (PEP 440 dev versions):

A GitHub or container tag `v1.1.0-dev.N`

maps to a wheel version `1.1.0.devN`

(for example `v1.1.0-dev.2`

→ `==1.1.0.dev2`

). Optional extras such as `ai-dynamo[vllm]`

use the same flags; pin the version you want from the sections below.

### v1.3.0-dev.1

**Branch:**[release/1.3.0-dev.1](https://github.com/ai-dynamo/dynamo/tree/release/1.3.0-dev.1)**GitHub Tag:**[v1.3.0-dev.1](https://github.com/ai-dynamo/dynamo/releases/tag/v1.3.0-dev.1)**Backends:**SGLang`0.5.12.post1`

| TensorRT-LLM`1.3.0rc17`

| vLLM`0.22.0`

| NIXL`1.1.0`

(vLLM);`1.0.1`

(SGLang);`0.10.1`

(TRT-LLM)**Coverage:**Platform preview of v1.3.0 — all runtime containers (vLLM and SGLang on CUDA 12 + 13 + EFA, TensorRT-LLM on CUDA 13 + EFA) and component containers, plus`ai-dynamo`

/`ai-dynamo-runtime`

/`kvbm`

wheels, Rust crates, and the`dynamo-platform`

and`snapshot`

Helm charts. Cut from`main`

after the TensorRT-LLM`v1.3.0rc17`

upgrade; early access build, not QA-gated.

#### Container Images

#### Python Wheels

`ai-dynamo`

, `ai-dynamo-runtime`

, and `kvbm`

at `1.3.0.dev1`

on [pypi.nvidia.com](https://pypi.nvidia.com/) (prerelease index, not public PyPI):

#### Helm Charts

`dynamo-platform`

and `snapshot`

at `1.3.0-dev.1`

.

#### Rust Crates

Published to [crates.io](https://crates.io/) at `1.3.0-dev.1`

(`dynamo-runtime`

, `dynamo-llm`

, and the dependent workspace crates).

### v1.1.0-dev.3

**Branch:**[release/1.1.0-dev.3](https://github.com/ai-dynamo/dynamo/tree/release/1.1.0-dev.3)**GitHub Tag:**[v1.1.0-dev.3](https://github.com/ai-dynamo/dynamo/releases/tag/v1.1.0-dev.3)**Backends (branch ToT):**SGLang`v0.5.10.post1`

| TensorRT-LLM`v1.3.0rc11`

| vLLM`v0.19.0`

| NIXL`v0.10.1`

**Coverage:**TensorRT-LLM runtime container plusand`ai-dynamo`

wheels on`ai-dynamo-runtime`

[pypi.nvidia.com](https://pypi.nvidia.com/). SGLang and vLLM containers, component containers (`dynamo-frontend`

,`dynamo-planner`

,`kubernetes-operator`

,`snapshot-agent`

),wheel, and Helm charts are not published for this tag.`kvbm`


#### Container Images

#### Python Wheels

Available from [pypi.nvidia.com](https://pypi.nvidia.com/) (pre-release index):

`kvbm==1.1.0.dev3`

is not yet published.

#### Helm Charts

Not published for this dev release. Use the latest stable (`v1.1.0`

) for platform install.

#### Rust Crates

Not shipped for early access builds.

### v1.1.0-dev.2

**Branch:**[release/1.1.0-dev.2](https://github.com/ai-dynamo/dynamo/tree/release/1.1.0-dev.2)**GitHub Tag:**[v1.1.0-dev.2](https://github.com/ai-dynamo/dynamo/releases/tag/v1.1.0-dev.2)**Backends (branch ToT):**SGLang`v0.5.9`

| TensorRT-LLM`v1.3.0rc9`

| vLLM`v0.19.0`

| NIXL`v0.10.1`

**Coverage:**SGLang and TensorRT-LLM runtime containers plusand`ai-dynamo`

wheels on`ai-dynamo-runtime`

[pypi.nvidia.com](https://pypi.nvidia.com/). vLLM runtime container, component containers (`dynamo-frontend`

,`dynamo-planner`

,`kubernetes-operator`

,`snapshot-agent`

),wheel, and Helm charts are not published for this tag.`kvbm`


#### Container Images

#### Python Wheels

Available from [pypi.nvidia.com](https://pypi.nvidia.com/) (pre-release index):

#### Helm Charts

Not published for this dev release. Use the latest stable (`v1.1.0`

) for platform install.

#### Rust Crates

Not shipped for early access builds.

### v1.1.0-dev.1

**Branch:**[release/1.1.0-dev.1](https://github.com/ai-dynamo/dynamo/tree/release/1.1.0-dev.1)**GitHub Tag:**[v1.1.0-dev.1](https://github.com/ai-dynamo/dynamo/releases/tag/v1.1.0-dev.1)**Backends:**SGLang`v0.5.9`

| TensorRT-LLM`v1.3.0rc5.post1`

| vLLM`v0.17.1`

| NIXL`v0.10.1`


#### Container Images

#### Python Wheels

Available from [pypi.nvidia.com](https://pypi.nvidia.com/) (pre-release index):

#### Helm Charts

#### Rust Crates

Not shipped for early access builds.