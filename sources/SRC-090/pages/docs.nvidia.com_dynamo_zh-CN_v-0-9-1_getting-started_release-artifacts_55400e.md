source: https://docs.nvidia.com/dynamo/zh-CN/v-0-9-1/getting-started/release-artifacts
lastmod: 2026-09-23T23:30:39.914Z

# Dynamo Release Artifacts

This document provides a comprehensive inventory of all Dynamo release artifacts including container images, Python wheels, Helm charts, and Rust crates.


See also:[Support Matrix]for hardware and platform compatibility |[Feature Matrix]for backend feature support

Release history in this document begins at v0.6.0.

## Current Release: Dynamo v0.9.1

### Container Images

* Multimodal inference on CUDA 13 images: works on AMD64 for all backends; works on ARM64 only for TensorRT-LLM (`vllm-runtime:*-cuda13`

and `sglang-runtime:*-cuda13`

do not support multimodality on ARM64).

### Python Wheels

We recommend using the TensorRT-LLM NGC container instead of the `ai-dynamo[trtllm]`

wheel. See the [NGC container collection](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/collections/ai-dynamo) for supported images.

### Helm Charts


Note:The`dynamo-graph`

Helm chart is deprecated as of v0.9.0. Use the Kubernetes operator for deployment graph management.

### Rust Crates

## Quick Install Commands

### Container Images (NGC)

For detailed run instructions, see the

[Container README]or backend-specific guides:[vLLM]|[SGLang]|[TensorRT-LLM]

### Python Wheels (PyPI)

For detailed installation instructions, see the

[Local Quick Start]in the README.

### Helm Charts (NGC)

For Kubernetes deployment instructions, see the

[Kubernetes Installation Guide].

### Rust Crates (crates.io)

For API documentation, see each crate on

[docs.rs]. To build Dynamo from source, see[Building from Source].

**CUDA and Driver Requirements:** For detailed CUDA toolkit versions and minimum driver requirements for each container image, see the [Support Matrix](https://docs.nvidia.com/dynamo/v-0-9-1/getting-started/support-matrix#cuda-and-driver-requirements).

## Known Issues

For a complete list of known issues, refer to the release notes for each version:

### Known Artifact Issues

## Release History

**v0.9.1**: Updated TRT-LLM to`v1.3.0rc3`

. All other dependencies unchanged from v0.9.0.**v0.9.0.post1**: Fixed`dynamo-platform`

Helm chart operator image tag (Helm chart only, NGC)**v0.9.0**: Updated vLLM to`v0.14.1`

, SGLang to`v0.5.8`

, TRT-LLM to`v1.3.0rc1`

, NIXL to`v0.9.0`

. New`dynamo-tokens`

Rust crate. Deprecated`dynamo-graph`

Helm chart.**v0.8.1.post1/.post2/.post3 Patches**: Experimental patch releases updating TRT-LLM only (PyPI wheels and TRT-LLM container). No other artifacts changed.

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

### Python Wheels


PyPI:[ai-dynamo]|[ai-dynamo-runtime]|[kvbm]To access a specific version:

`https://pypi.org/project/{package}/{version}/`


#### ai-dynamo (wheel)

#### ai-dynamo-runtime (wheel)

#### kvbm (wheel)

### Helm Charts


NGC Helm Registry:[ai-dynamo]Direct download:

`https://helm.ngc.nvidia.com/nvidia/ai-dynamo/charts/{chart}-{version}.tgz`


#### dynamo-crds (Helm chart)

#### dynamo-platform (Helm chart)

#### dynamo-graph (Helm chart) — Deprecated


Note:The`dynamo-graph`

Helm chart is deprecated as of v0.9.0.

### Rust Crates


crates.io:[dynamo-runtime]|[dynamo-llm]|[dynamo-async-openai]|[dynamo-parsers]|[dynamo-memory]|[dynamo-config]|[dynamo-tokens]To access a specific version:

`https://crates.io/crates/{crate}/{version}`