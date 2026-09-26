source: https://docs.nvidia.com/dynamo/v1.2.1/resources/support-matrix
lastmod: 2026-09-24T19:58:16.636Z

# Support Matrix

**See also:** [Release Artifacts](https://docs.nvidia.com/dynamo/v1.2.1/resources/release-artifacts) for container images, wheels, Helm charts, and crates | [Feature Matrix](https://docs.nvidia.com/dynamo/v1.2.1/resources/feature-matrix) for backend feature support

## At a Glance

**Latest stable release:** [v1.2.0](https://github.com/ai-dynamo/dynamo/releases/tag/v1.2.0) — SGLang `0.5.11`

(NIXL `1.0.1`

) | TensorRT-LLM `1.3.0rc14`

(NIXL `0.10.1`

) | vLLM `0.20.1`

(NIXL `0.10.1`

)

**Experimental release:** [v1.3.0-dev.1](https://github.com/ai-dynamo/dynamo/tree/release/1.3.0-dev.1) *(full-platform preview of v1.3.0 — all runtime + component containers, wheels, crates, Helm)* — SGLang `0.5.12.post1`

| TensorRT-LLM `1.3.0rc17`

| vLLM `0.22.0`

| NIXL `1.1.0`

(vLLM); `1.0.1`

(SGLang); `0.10.1`

(TRT-LLM)

**On this page:** [Backend Dependencies](https://docs.nvidia.com/dynamo/v1.2.1/resources/support-matrix#backend-dependencies) | [CUDA and Drivers](https://docs.nvidia.com/dynamo/v1.2.1/resources/support-matrix#cuda-and-driver-requirements) | [Hardware](https://docs.nvidia.com/dynamo/v1.2.1/resources/support-matrix#hardware-compatibility) | [Platform](https://docs.nvidia.com/dynamo/v1.2.1/resources/support-matrix#platform-architecture-compatibility) | [Cloud](https://docs.nvidia.com/dynamo/v1.2.1/resources/support-matrix#cloud-service-provider-compatibility) | [Build Support](https://docs.nvidia.com/dynamo/v1.2.1/resources/support-matrix#build-support)

## Backend Dependencies

Driver requirements differ by backend — see

[CUDA and Driver Requirements]below.

The following table shows the backend framework versions included with each Dynamo release:

For **v1.1.0-dev.2**, **v1.1.0-dev.3**, **v1.2.0-deepseek-v4-dev.2**, and **v1.2.0-deepseek-v4-dev.3**, the cells above match `container/context.yaml`

on the corresponding release branch (pins used to build images). Those lines are **partial releases**: not every backend has a published Dynamo runtime container for that tag. See [Pre-Release Artifacts](https://docs.nvidia.com/dynamo/v1.2.1/resources/release-artifacts#pre-release-artifacts) for what actually shipped. The `v1.2.0-deepseek-v4-dev.2`

and `v1.2.0-deepseek-v4-dev.3`

SGLang containers are built on the upstream `lmsysorg/sglang:deepseek-v4-blackwell`

preview image rather than a tagged SGLang release; TensorRT-LLM is not part of those dev releases.

### Version Labels

**1.3.0 (main / ToT)**reflects the current development branch.- Releases marked
*(experimental, partial)*are pre-releases: the table shows branch build pins, which may include backends with no NGC image for that dev tag yet. - Releases marked
*(in progress)*or*(planned)*show target versions that may change before final release.

### Version Compatibility

- Backend versions listed are the only versions tested and supported for each release.
- TensorRT-LLM does not support Python 3.11; installation of the
`ai-dynamo[trtllm]`

wheel will fail on Python 3.11.

### CUDA and Driver Requirements

Dynamo container images include CUDA toolkit libraries. The host machine must have a compatible NVIDIA GPU driver installed.

Patch versions (e.g., v0.8.1.post1, v0.7.0.post1) have the same CUDA support as their base version.

Experimental `v1.1.0-dev.*`

images follow the same CUDA matrix as `v1.0.2`

. The `v1.2.0-deepseek-v4-dev.3`

vLLM container is CUDA 13.0 multi-arch; the SGLang containers split by arch (CUDA 12.9 on `amd64`

, CUDA 13.0 on `arm64`

).

Experimental CUDA 13 images are not published for all versions. Check [Release Artifacts](https://docs.nvidia.com/dynamo/v1.2.1/resources/release-artifacts) for availability.

For detailed artifact versions and NGC links (including container images, Python wheels, Helm charts, and Rust crates), see the [Release Artifacts](https://docs.nvidia.com/dynamo/v1.2.1/resources/release-artifacts) page.

#### CUDA Compatibility Resources

For detailed information on CUDA driver compatibility, forward compatibility, and troubleshooting:

[CUDA Compatibility Overview](https://docs.nvidia.com/deploy/cuda-compatibility/)[Why CUDA Compatibility](https://docs.nvidia.com/deploy/cuda-compatibility/why-cuda-compatibility.html)[Minor Version Compatibility](https://docs.nvidia.com/deploy/cuda-compatibility/minor-version-compatibility.html)[Forward Compatibility](https://docs.nvidia.com/deploy/cuda-compatibility/forward-compatibility.html)[FAQ](https://docs.nvidia.com/deploy/cuda-compatibility/frequently-asked-questions.html)

For extended driver compatibility beyond the minimum versions listed above, consider using `cuda-compat`

packages on the host. See [Forward Compatibility](https://docs.nvidia.com/deploy/cuda-compatibility/forward-compatibility.html) for details.

## Hardware Compatibility

Dynamo provides multi-arch container images supporting both AMD64 (x86_64) and ARM64 architectures. See [Release Artifacts](https://docs.nvidia.com/dynamo/v1.2.1/resources/release-artifacts) for available images.

### GPU Compatibility

If you are using a **GPU**, the following GPU models and architectures are supported:

## Platform Architecture Compatibility

**Dynamo** is compatible with the following platforms:

Wheels are built using a manylinux_2_28-compatible environment and validated on CentOS Stream 9 and Ubuntu (22.04, 24.04). Compatibility with other Linux distributions is expected but not officially verified.

## Cloud Service Provider Compatibility

### AWS

**AL2023 TensorRT-LLM Limitation:** There is a known issue with the TensorRT-LLM framework when running the AL2023 container locally with `docker run --network host ...`

due to a [bug](https://github.com/mpi4py/mpi4py/discussions/491#discussioncomment-12660609) in mpi4py. To avoid this issue, replace the `--network host`

flag with more precise networking configuration by mapping only the necessary ports (e.g., 4222 for nats, 2379/2380 for etcd, 8000 for frontend).

## Build Support

For version-specific artifact details, installation commands, and release history, see [Release Artifacts](https://docs.nvidia.com/dynamo/v1.2.1/resources/release-artifacts).

**Dynamo** currently provides build support in the following ways:

-
**Wheels**: We distribute Python wheels of Dynamo and KV Block Manager:[ai-dynamo](https://pypi.org/project/ai-dynamo/)[ai-dynamo-runtime](https://pypi.org/project/ai-dynamo-runtime/)[kvbm](https://pypi.org/project/kvbm/)as a standalone implementation.

-
**Dynamo Container Images**: We distribute multi-arch images (x86 & ARM64 compatible) on[NGC](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/collections/ai-dynamo):[Dynamo Frontend](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/containers/dynamo-frontend)*(New in v0.8.0)*[SGLang Runtime](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/containers/sglang-runtime)[SGLang Runtime (CUDA 13)](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/containers/sglang-runtime-cu13)[TensorRT-LLM Runtime](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/containers/tensorrtllm-runtime)[TensorRT-LLM Runtime (EFA)](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/containers/tensorrtllm-runtime)*(New in v1.0.0, Experimental, AMD64 only)*[vLLM Runtime](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/containers/vllm-runtime)[vLLM Runtime (CUDA 13)](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/containers/vllm-runtime-cu13)[vLLM Runtime (EFA)](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/containers/vllm-runtime)*(New in v1.0.0, Experimental, AMD64 only)*[Kubernetes Operator](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/containers/kubernetes-operator)[Snapshot Agent](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/containers/snapshot-agent)*(New in v1.0.0, Preview)*

-
**Helm Charts**:[NGC](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/collections/ai-dynamo)hosts the helm charts supporting Kubernetes deployments of Dynamo:[Dynamo Platform](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/helm-charts/dynamo-platform)(now includes CRDs)[Snapshot](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/helm-charts/snapshot)*(New in v1.0.0, Preview)*[Dynamo CRDs](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/helm-charts/dynamo-crds)*(Deprecated in v1.0.0, CRDs managed by Operator)*[Dynamo Graph](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/helm-charts/dynamo-graph)*(Deprecated in v0.9.0)*

-
**Rust Crates**:[dynamo-runtime](https://crates.io/crates/dynamo-runtime/)[dynamo-llm](https://crates.io/crates/dynamo-llm/)[dynamo-protocols](https://crates.io/crates/dynamo-protocols/)[dynamo-parsers](https://crates.io/crates/dynamo-parsers/)[dynamo-config](https://crates.io/crates/dynamo-config/)*(New in v0.8.0)*[dynamo-memory](https://crates.io/crates/dynamo-memory/)*(New in v0.8.0)*[dynamo-tokens](https://crates.io/crates/dynamo-tokens/)*(New in v0.9.0)*[dynamo-mocker](https://crates.io/crates/dynamo-mocker/)*(New in v1.0.0)*[dynamo-kv-router](https://crates.io/crates/dynamo-kv-router/)*(New in v1.0.0)*


Once you’ve confirmed that your platform and architecture are compatible, you can install **Dynamo** by following the [Quickstart](https://docs.nvidia.com/dynamo/getting-started/quickstart) in the docs.