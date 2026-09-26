source: https://docs.nvidia.com/dynamo/reference/nightly-releases
lastmod: 2026-09-24T19:58:16.636Z

# Nightly Releases

Dynamo publishes nightly builds from `main`

. Nightlies let you try the latest features and backend upgrades before they land in a stable release. This page covers what nightly publishes, how to install it, and which backend versions the current and recent nightlies ship.

**Nightly builds are experimental and are not QA-validated.** They are built from the tip of `main`

and may contain bugs, breaking changes, or incomplete features. Use [stable releases](https://docs.nvidia.com/dynamo/reference/release-artifacts) for production workloads.

## Recent Nightlies

Nightly builds

### Recent pinned wheel builds

Nightly wheels are pinned by date. Runtime containers use rolling NGC tags, so the container buttons always pull the latest nightly image.

Aug 31, 2026

Aug 30, 2026

Aug 29, 2026

## What Gets Published

Every night, the [Nightly CI pipeline](https://github.com/ai-dynamo/dynamo/blob/main/.github/workflows/nightly-ci.yml) builds `main`

and publishes:

**Runtime container images (CUDA 13):**`vllm-runtime-nightly`

,`sglang-runtime-nightly`

, and`tensorrtllm-runtime-nightly`

to NGC, each with an Elastic Fabric Adapter (EFA) variant under a`-efa`

tag suffix.**Component container images:**`kubernetes-operator-nightly`

,`dynamo-planner-nightly`

, and`dynamo-frontend-nightly`

to NGC.**Python wheels:**`ai-dynamo`

,`ai-dynamo-runtime`

, and`kvbm`

to the NVIDIA prerelease index at[pypi.nvidia.com](https://pypi.nvidia.com/).**Helm chart:**to the NGC Helm registry, kept separate from the stable`dynamo-platform-nightly`

`dynamo-platform`

chart.

The runtime images and the wheels gate the release: if any of them fails to build, that night publishes nothing. The component images, the EFA variants, and the Helm chart stage fail-soft, so a flake in one of them skips that artifact for the night without holding back the rest.

Nightly does not publish Rust crates — for those, use a [stable or prerelease build](https://docs.nvidia.com/dynamo/reference/release-artifacts).

## Installing Nightly Containers

Nightly images live in their own `-nightly`

NGC repositories so they cannot be pulled accidentally in place of a stable image. Every nightly build pushes an immutable `YYYYMMDD-<shortsha>`

tag and moves the `latest`

tag to that build.

Pin the dated tag for anything you need to reproduce later: `latest`

moves every night, so the image behind it changes underneath you. The runtime repositories also carry a `nightly`

tag, but it stopped tracking `main`

in July 2026 — use `latest`

or a dated tag instead. The component repositories publish the same dated tags and a `latest`

float, without the `nightly`

alias or the EFA variants.

## Installing Nightly Wheels

Nightly wheels are published to the NVIDIA prerelease index at [pypi.nvidia.com](https://pypi.nvidia.com/), not the public PyPI. They are Linux manylinux builds for the Python versions in [Compatibility](https://docs.nvidia.com/dynamo/reference/compatibility); install on a supported Linux host or inside a Linux container. Nightly versions follow PEP 440 dev versioning, `X.Y.Z.devYYYYMMDD`

.

Backend extras such as `ai-dynamo[vllm]`

and `ai-dynamo[sglang]`

use the same flags. For TensorRT-LLM, use the nightly container rather than a PyPI extra.

## Backend Versions

Nightlies track `main`

, so the backend versions they ship change as `main`

advances. The build selector in [Install Dynamo](https://docs.nvidia.com/dynamo/dev/cli/installation/install-dynamo) lists the last three versions of each backend and the newest nightly that shipped each one, with the exact install command. For Kubernetes image variables, use the selector in the [Kubernetes Quickstart](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart#install-dynamo).

To confirm the exact versions a specific nightly shipped, read them from the pulled image:

## See Also

[Release Artifacts](https://docs.nvidia.com/dynamo/reference/release-artifacts)— stable and prerelease artifact inventory[Compatibility](https://docs.nvidia.com/dynamo/reference/compatibility)— hardware, platform, CUDA, and driver support[Model Early Access Builds](https://docs.nvidia.com/dynamo/reference/model-early-access-builds)— model-specific prerelease container builds