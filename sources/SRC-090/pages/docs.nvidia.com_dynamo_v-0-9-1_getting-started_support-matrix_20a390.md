source: https://docs.nvidia.com/dynamo/v-0-9-1/getting-started/support-matrix
lastmod: 2026-09-24T19:58:16.636Z

# Dynamo Support Matrix

This document provides the support matrix for Dynamo, including hardware, software and build instructions.

**See also:** [Release Artifacts](https://docs.nvidia.com/dynamo/v-0-9-1/getting-started/release-artifacts) for container images, wheels, Helm charts, and crates | [Feature Matrix](https://docs.nvidia.com/dynamo/v-0-9-1/getting-started/feature-matrix) for backend feature support

## Backend Dependencies

The following table shows the backend framework versions included with each Dynamo release:

* Limited experimental releases — only TRT-LLM container and Dynamo PyPI wheels were published.

### Version Labels

**v0.9.1**is the current release.

### Version Compatibility

- Backend versions listed are the only versions tested and supported for each release.
- TensorRT-LLM does not support Python 3.11; installation of the
`ai-dynamo[trtllm]`

wheel will fail on Python 3.11.

### CUDA Versions by Backend

Patch versions (e.g., v0.8.1.post1, v0.7.0.post1) have the same CUDA support as their base version.

For detailed artifact versions and NGC links (including container images, Python wheels, Helm charts, and Rust crates), see the [Release Artifacts](https://docs.nvidia.com/dynamo/v-0-9-1/getting-started/release-artifacts) page.

## Hardware Compatibility

Dynamo provides multi-arch container images supporting both AMD64 (x86_64) and ARM64 architectures. See [Release Artifacts](https://docs.nvidia.com/dynamo/v-0-9-1/getting-started/release-artifacts) for available images.

### GPU Compatibility

If you are using a **GPU**, the following GPU models and architectures are supported:

## Platform Architecture Compatibility

**Dynamo** is compatible with the following platforms:

Wheels are built using a manylinux_2_28-compatible environment and validated on CentOS Stream 9 and Ubuntu (22.04, 24.04). Compatibility with other Linux distributions is expected but not officially verified.

[!Caution] KV Block Manager is supported only with Python 3.12. Python 3.12 support is currently limited to Ubuntu 24.04.


## Software Compatibility

### CUDA and Driver Requirements

Dynamo container images include CUDA toolkit libraries. The host machine must have a compatible NVIDIA GPU driver installed.

Experimental CUDA 13 images are not published for all versions. Check [Release Artifacts](https://docs.nvidia.com/dynamo/v-0-9-1/getting-started/release-artifacts) for availability.

#### CUDA Compatibility Resources

For detailed information on CUDA driver compatibility, forward compatibility, and troubleshooting:

[CUDA Compatibility Overview](https://docs.nvidia.com/deploy/cuda-compatibility/)[Why CUDA Compatibility](https://docs.nvidia.com/deploy/cuda-compatibility/why-cuda-compatibility.html)[Minor Version Compatibility](https://docs.nvidia.com/deploy/cuda-compatibility/minor-version-compatibility.html)[Forward Compatibility](https://docs.nvidia.com/deploy/cuda-compatibility/forward-compatibility.html)[FAQ](https://docs.nvidia.com/deploy/cuda-compatibility/frequently-asked-questions.html)

For extended driver compatibility beyond the minimum versions listed above, consider using `cuda-compat`

packages on the host. See [Forward Compatibility](https://docs.nvidia.com/deploy/cuda-compatibility/forward-compatibility.html) for details.

## Cloud Service Provider Compatibility

### AWS

[!Caution]

AL2023 TensorRT-LLM Limitation:There is a known issue with the TensorRT-LLM framework when running the AL2023 container locally with`docker run --network host ...`

due to a[bug]in mpi4py. To avoid this issue, replace the`--network host`

flag with more precise networking configuration by mapping only the necessary ports (e.g., 4222 for nats, 2379/2380 for etcd, 8000 for frontend).

## Build Support

For version-specific artifact details, installation commands, and release history, see [Release Artifacts](https://docs.nvidia.com/dynamo/v-0-9-1/getting-started/release-artifacts).

**Dynamo** currently provides build support in the following ways:

-
**Wheels**: We distribute Python wheels of Dynamo and KV Block Manager:[ai-dynamo](https://pypi.org/project/ai-dynamo/)[ai-dynamo-runtime](https://pypi.org/project/ai-dynamo-runtime/)[kvbm](https://pypi.org/project/kvbm/)as a standalone implementation.

-
**Dynamo Container Images**: We distribute multi-arch images (x86 & ARM64 compatible) on[NGC](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/collections/ai-dynamo): -
**Helm Charts**:[NGC](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/collections/ai-dynamo)hosts the helm charts supporting Kubernetes deployments of Dynamo:[Dynamo CRDs](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/helm-charts/dynamo-crds)[Dynamo Platform](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/helm-charts/dynamo-platform)[Dynamo Graph](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/helm-charts/dynamo-graph)*(Deprecated in v0.9.0)*

-
**Rust Crates**:

Once you’ve confirmed that your platform and architecture are compatible, you can install **Dynamo** by following the [Local Quick Start](https://github.com/ai-dynamo/dynamo/blob/main/README.md#local-quick-start) in the README.