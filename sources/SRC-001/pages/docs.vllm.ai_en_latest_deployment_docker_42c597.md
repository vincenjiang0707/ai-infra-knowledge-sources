source: https://docs.vllm.ai/en/latest/deployment/docker/
lastmod: 2026-09-23

# Using Docker[¶](https://docs.vllm.ai#using-docker)

## Pre-built images[¶](https://docs.vllm.ai#pre-built-images)

vLLM offers an official Docker image for deployment. The image can be used to run OpenAI compatible server and is available on Docker Hub as [vllm/vllm-openai](https://hub.docker.com/r/vllm/vllm-openai/tags).

docker run --runtime nvidia --gpus all \
-v ~/.cache/huggingface:/root/.cache/huggingface \
--env "HF_TOKEN=$HF_TOKEN" \
-p 8000:8000 \
--ipc=host \
vllm/vllm-openai:latest \
--model Qwen/Qwen3-0.6B


This image can also be used with other container engines such as [Podman](https://podman.io/).

podman run --device nvidia.com/gpu=all \
-v ~/.cache/huggingface:/root/.cache/huggingface \
--env "HF_TOKEN=$HF_TOKEN" \
-p 8000:8000 \
--ipc=host \
docker.io/vllm/vllm-openai:latest \
--model Qwen/Qwen3-0.6B


You can add any other [engine-args](https://docs.vllm.ai/configuration/engine_args/) you need after the image tag (`vllm/vllm-openai:latest`

).

Note

You can either use the `ipc=host`

flag or `--shm-size`

flag to allow the container to access the host's shared memory. vLLM uses PyTorch, which uses shared memory to share data between processes under the hood, particularly for tensor parallel inference.

Note

Optional dependencies are not included in order to avoid licensing issues (e.g. [ Issue #8030](https://github.com/vllm-project/vllm/issues/8030)).

If you need to use those dependencies (having accepted the license terms), create a custom Dockerfile on top of the base image with an extra layer that installs them:

Tip

Some new models may only be available on the main branch of [HF Transformers](https://github.com/huggingface/transformers).

To use the development version of `transformers`

, create a custom Dockerfile on top of the base image with an extra layer that installs their code from source:

#### Running on Systems with Older CUDA Drivers[¶](https://docs.vllm.ai#running-on-systems-with-older-cuda-drivers)

vLLM's Docker image comes with [CUDA compatibility libraries](https://docs.nvidia.com/deploy/cuda-compatibility/index.html) pre-installed. This allows you to run vLLM on systems with NVIDIA drivers that are older than the CUDA Toolkit version used in the image, but only supports select professional and datacenter NVIDIA GPUs.

For CUDA 13 images, the minimum host kernel is Linux 4.15 when running normally because CUDA 13 requires an R580 or newer driver. Compatibility mode supports R535 and R570 host drivers; R535 lowers the minimum host kernel to Linux 3.10, while R570 still requires Linux 4.15. Upgrading the container userland to Ubuntu 24.04 does not raise these driver-defined kernel requirements. See NVIDIA's [forward compatibility matrix](https://docs.nvidia.com/deploy/cuda-compatibility/forward-compatibility.html#use-the-right-cuda-forward-compatibility-package), [R535 requirements](https://download.nvidia.com/XFree86/Linux-x86_64/535.104.05/README/minimumrequirements.html), and [R580 requirements](https://download.nvidia.com/XFree86/Linux-x86_64/580.76.05/README/minimumrequirements.html).

To enable this feature, set the `VLLM_ENABLE_CUDA_COMPATIBILITY`

environment variable to `1`

or `true`

when running the container:

docker run --runtime nvidia --gpus all \
-v ~/.cache/huggingface:/root/.cache/huggingface \
-p 8000:8000 \
--env "HF_TOKEN=<secret>" \
--env "VLLM_ENABLE_CUDA_COMPATIBILITY=1" \
vllm/vllm-openai <args...>


This will automatically configure `LD_LIBRARY_PATH`

to point to the compatibility libraries before loading PyTorch and other dependencies.

vLLM offers official Docker images for deployment. The images can be used to run OpenAI compatible server and are available on Docker Hub as [vllm/vllm-openai-rocm](https://hub.docker.com/r/vllm/vllm-openai-rocm/tags).

`vllm/vllm-openai-rocm:latest`

— stable release`vllm/vllm-openai-rocm:nightly`

— preview build from the latest development branch, use this if you want the latest features and fixes

docker run --rm \
--group-add=video \
--cap-add=SYS_PTRACE \
--security-opt seccomp=unconfined \
--device /dev/kfd \
--device /dev/dri \
-v ~/.cache/huggingface:/root/.cache/huggingface \
--env "HF_TOKEN=$HF_TOKEN" \
-p 8000:8000 \
--ipc=host \
vllm/vllm-openai-rocm:<tag> \
--model Qwen/Qwen3-0.6B


To use the docker image as base for development, you can launch it in interactive session through overriding the entrypoint.

## Commands

docker run --rm -it \
--group-add=video \
--cap-add=SYS_PTRACE \
--security-opt seccomp=unconfined \
--device /dev/kfd \
--device /dev/dri \
-v ~/.cache/huggingface:/root/.cache/huggingface \
--env "HF_TOKEN=$HF_TOKEN" \
--network=host \
--ipc=host \
--entrypoint /bin/bash \
vllm/vllm-openai-rocm:<tag>


#### Use AMD's Docker Images (Deprecated)[¶](https://docs.vllm.ai#use-amds-docker-images-deprecated)

Deprecated

AMD's Docker images (`rocm/vllm`

and `rocm/vllm-dev`

) are deprecated in favor of the official vLLM Docker images above (`vllm/vllm-openai-rocm`

). Please migrate to the official images.

Prior to January 20th, 2026 when the official docker images became available on [upstream vLLM docker hub](https://hub.docker.com/v2/repositories/vllm/vllm-openai-rocm/tags/), the [AMD Infinity hub for vLLM](https://hub.docker.com/r/rocm/vllm/tags) offered a prebuilt, optimized docker image designed for validating inference performance on the AMD Instinct MI300X™ accelerator. AMD also offered nightly prebuilt docker image from [Docker Hub](https://hub.docker.com/r/rocm/vllm-dev), which has vLLM and all its dependencies installed. The entrypoint of this docker image is `/bin/bash`

(different from the vLLM's Official Docker Image).

Tip

Please check [LLM inference performance validation on AMD Instinct MI300X](https://rocm.docs.amd.com/en/latest/how-to/performance-validation/mi300x/vllm-benchmark.html) for instructions on how to use this prebuilt docker image.

vLLM offers official Docker images for deployment. The images can be used to run OpenAI compatible server and are available on Docker Hub as [vllm/vllm-openai-xpu](https://hub.docker.com/r/vllm/vllm-openai-xpu/tags).

`vllm/vllm-openai-xpu:latest`

— stable release, available starting from v0.26.0`vllm/vllm-openai-xpu:nightly`

— preview build from the latest development branch, use this if you want the latest features and fixes

docker run --rm \
--network=host \
--device /dev/dri:/dev/dri \
-v /dev/dri/by-path:/dev/dri/by-path \
-v ~/.cache/huggingface:/root/.cache/huggingface \
--env "HF_TOKEN=$HF_TOKEN" \
--ipc=host \
--privileged \
vllm/vllm-openai-xpu:<tag> \
--model Qwen/Qwen3-0.6B


To use the docker image as base for development, you can launch it in interactive session through overriding the entrypoint.

## Run a vLLM Recipes configuration[¶](https://docs.vllm.ai#run-a-vllm-recipes-configuration)

[vLLM Recipes](https://recipes.vllm.ai/) can be converted into `config.yaml`

and `env.sh`

. See the [ Recipes conversion tool README](https://github.com/vllm-project/vllm/blob/main/tools/recipes/README.md) for usage.

For Docker, mount both files and source `env.sh`

inside the container before starting vLLM:

docker run --rm --gpus all \
-v ~/.cache/huggingface:/root/.cache/huggingface \
-v "$PWD/config.yaml:/recipe/config.yaml:ro" \
-v "$PWD/env.sh:/recipe/env.sh:ro" \
-p 8000:8000 \
--ipc=host \
--entrypoint /bin/bash \
vllm/vllm-openai:latest \
-lc 'source /recipe/env.sh && exec vllm serve --config /recipe/config.yaml'


## Persist the compile cache across containers[¶](https://docs.vllm.ai#persist-the-compile-cache-across-containers)

Mounting the Hugging Face cache keeps model weights across containers, but each new container still starts with an empty `VLLM_CACHE_ROOT`

(default `~/.cache/vllm`

) and recompiles the model's `torch.compile`

artifacts. Mount a named volume at that path to reuse the inductor, Triton, and AOT artifacts from the second container onward:

docker run --rm --gpus all \
-v ~/.cache/huggingface:/root/.cache/huggingface \
-v vllm-cache:/root/.cache/vllm \
-p 8000:8000 \
vllm/vllm-openai:latest \
meta-llama/Llama-3.1-8B-Instruct


See [Faster Startup](https://docs.vllm.ai/configuration/optimization/#faster-startup) for the mechanism and for what invalidates the cache.

## Run as a non-root user[¶](https://docs.vllm.ai#run-as-a-non-root-user)

The CUDA `vllm/vllm-openai`

image runs as root by default for backward compatibility. It is also prepared to run as the built-in `vllm`

user (UID 2000, GID 0):

docker run --rm --gpus all \
--user 2000:0 \
-p 8000:8000 \
vllm/vllm-openai:latest \
meta-llama/Llama-3.1-8B-Instruct


When mounting model or cache volumes for a non-root container, mount writable paths under `/home/vllm`

instead of `/root`

. For example, mount the Hugging Face cache at `/home/vllm/.cache/huggingface`

and make the mounted directory writable by group 0.

docker run --rm --gpus all \
--user 2000:0 \
-v ~/.cache/huggingface:/home/vllm/.cache/huggingface \
-p 8000:8000 \
vllm/vllm-openai:latest \
meta-llama/Llama-3.1-8B-Instruct


To build an image that defaults to the non-root `vllm`

user, use the opt-in `vllm-openai-nonroot`

target:

docker build --target vllm-openai-nonroot \
-t vllm-openai-nonroot:local \
-f docker/Dockerfile .
docker run --rm --gpus all \
-p 8000:8000 \
vllm-openai-nonroot:local \
meta-llama/Llama-3.1-8B-Instruct


The `vllm-openai-nonroot`

target also supports OpenShift-style arbitrary UIDs when the runtime UID is a member of group 0. In Kubernetes manifests, set the container security context accordingly and keep mounted cache/model paths writable by group 0:

Runtime UIDs outside group 0 are not part of the documented support matrix because they may be unable to write to `/home/vllm`

or `/opt/uv/cache`

.

## Build image from source[¶](https://docs.vllm.ai#build-image-from-source)

You can build and run vLLM from source via the provided [docker/Dockerfile](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile). To build vLLM:

# optionally specifies: --build-arg max_jobs=8 --build-arg nvcc_threads=2
DOCKER_BUILDKIT=1 docker build . \
--target vllm-openai \
--tag vllm/vllm-openai \
--file docker/Dockerfile


Note

By default vLLM will build for all GPU types for widest distribution. If you are just building for the current GPU type, you can add `--build-arg torch_cuda_arch_list=""`

to delegate architecture selection to PyTorch. This requires the GPU to be visible to the container build; standard Docker BuildKit builds do not expose it and PyTorch instead falls back to its common architecture list.

If you are using Podman instead of Docker, you might need to disable SELinux labeling by adding `--security-opt label=disable`

when running `podman build`

command to avoid certain [existing issues](https://github.com/containers/buildah/discussions/4184).

Note

If you have not changed any C++ or CUDA kernel code, you can use precompiled wheels to significantly reduce Docker build time.

**Enable the feature**by adding the build argument:`--build-arg VLLM_USE_PRECOMPILED="1"`

.**How it works**: By default, vLLM automatically finds the correct wheels from our[Nightly Builds](https://docs.vllm.ai/contributing/ci/nightly_builds/)by using the merge-base commit with the upstream`main`

branch.**Override commit**: To use wheels from a specific commit, provide the`--build-arg VLLM_PRECOMPILED_WHEEL_COMMIT=<commit_hash>`

argument.

For a detailed explanation, refer to the documentation on 'Set up using Python-only build (without compilation)' part in [Build wheel from source](https://docs.vllm.ai/contributing/ci/nightly_builds/#precompiled-wheels-usage), these args are similar.

#### Building vLLM's Docker Image from Source for Arm64/aarch64[¶](https://docs.vllm.ai#building-vllms-docker-image-from-source-for-arm64aarch64)

A docker container can be built for aarch64 systems such as the Nvidia Grace-Hopper and Grace-Blackwell. Using the flag `--platform "linux/arm64"`

will build for arm64.

Note

Multiple modules must be compiled, so this process can take a while. Recommend using `--build-arg max_jobs=`

& `--build-arg nvcc_threads=`

flags to speed up build process. However, ensure your `max_jobs`

is substantially larger than `nvcc_threads`

to get the most benefits. Keep an eye on memory usage with parallel jobs as it can be substantial (see example below).

## Command

# Example of building on Nvidia GH200 server. (Memory usage: ~15GB, Build time: ~1475s / ~25 min, Image size: 6.93GB)
DOCKER_BUILDKIT=1 docker build . \
--file docker/Dockerfile \
--target vllm-openai \
--platform "linux/arm64" \
-t vllm/vllm-gh200-openai:latest \
--build-arg max_jobs=66 \
--build-arg nvcc_threads=2 \
--build-arg BUILD_BASE_IMAGE=pytorch/manylinuxaarch64-builder:cuda13.0-78e737ad29420ffc4800e677c51e2a852caf8359 \
--build-arg torch_cuda_arch_list="9.0 10.0+PTX"


For (G)B300, we recommend using CUDA 13, as shown in the following command.

## Command

DOCKER_BUILDKIT=1 docker build \
--build-arg CUDA_VERSION=13.0.2 \
--build-arg BUILD_BASE_IMAGE=pytorch/manylinuxaarch64-builder:cuda13.0-78e737ad29420ffc4800e677c51e2a852caf8359 \
--build-arg max_jobs=256 \
--build-arg nvcc_threads=2 \
--build-arg torch_cuda_arch_list='9.0 10.0+PTX' \
--platform "linux/arm64" \
--tag vllm/vllm-gb300-openai:latest \
--target vllm-openai \
-f docker/Dockerfile \
.


Note

If you are building the `linux/arm64`

image on a non-ARM host (e.g., an x86_64 machine), you need to ensure your system is set up for cross-compilation using QEMU. This allows your host machine to emulate ARM64 execution.

Run the following command on your host machine to register QEMU user static handlers:

After setting up QEMU, you can use the `--platform "linux/arm64"`

flag in your `docker build`

command.

#### [Preview] Building vLLM's Docker Image from Source for NVIDIA Rubin GPU Architecture[¶](https://docs.vllm.ai#preview-building-vllms-docker-image-from-source-for-nvidia-rubin-gpu-architecture)

Set `INSTALL_RUBIN_PRERELEASE=true`

to enable the Rubin build path.

Triton must currently be installed from source for Rubin compatibility. Specify its repository with `TRITON_INSTALL_FROM_SOURCE_REPO`

; an empty `TRITON_INSTALL_FROM_SOURCE_REVISION`

selects the repository's latest `main`

, while a commit, branch, or tag selects that revision. The tested revision lowers SM107 through LLVM's SM100 target and uses the final CUDA image's version-matched `ptxas`

for SM107 assembly. This enables vLLM's default compiled mode on VR200 and R100.

BuildKit does not automatically invalidate cached layers when a mutable Git ref changes. Use `--no-cache-filter extensions-build`

to refresh an empty, branch, or tag revision.

For `FINAL_BASE_IMAGE`

, use the public, multi-arch `nvcr.io/nvidia/cuda-dl-base:26.08-cuda13.4-devel-ubuntu24.04`

image. For `BUILD_BASE_IMAGE`

, use:

`pytorch/manylinux2_28-builder:cuda13.4`

for x86_64 CPUs.`pytorch/manylinuxaarch64-builder:cuda13.4`

for ARM64/AArch64 CPUs.

## ARM64/AArch64 build command

docker buildx build --progress=plain --load \
--file docker/Dockerfile \
--target vllm-openai \
--platform "linux/arm64" \
--tag "vllm/vllm-rubin-openai:prerelease-cu134-public-arm64" \
--build-arg max_jobs="$(nproc)" \
--build-arg nvcc_threads=2 \
--build-arg RUN_WHEEL_CHECK=false \
--build-arg INSTALL_RUBIN_PRERELEASE=true \
--build-arg TRITON_INSTALL_FROM_SOURCE_REPO=https://github.com/triton-lang/triton.git \
--build-arg TRITON_INSTALL_FROM_SOURCE_REVISION=3f6e41132b5edf639bfb872ad73d4688765e08b8 \
--build-arg CUDA_VERSION=13.4 \
--build-arg BUILD_BASE_IMAGE="pytorch/manylinuxaarch64-builder:cuda13.4" \
--build-arg FINAL_BASE_IMAGE="nvcr.io/nvidia/cuda-dl-base:26.08-cuda13.4-devel-ubuntu24.04" \
.


## x86_64 build command

docker buildx build --progress=plain --load \
--file docker/Dockerfile \
--target vllm-openai \
--platform "linux/amd64" \
--tag "vllm/vllm-rubin-openai:prerelease-cu134-public-amd64" \
--build-arg max_jobs="$(nproc)" \
--build-arg nvcc_threads=2 \
--build-arg RUN_WHEEL_CHECK=false \
--build-arg INSTALL_RUBIN_PRERELEASE=true \
--build-arg TRITON_INSTALL_FROM_SOURCE_REPO=https://github.com/triton-lang/triton.git \
--build-arg TRITON_INSTALL_FROM_SOURCE_REVISION=3f6e41132b5edf639bfb872ad73d4688765e08b8 \
--build-arg CUDA_VERSION=13.4 \
--build-arg BUILD_BASE_IMAGE="pytorch/manylinux2_28-builder:cuda13.4" \
--build-arg FINAL_BASE_IMAGE="nvcr.io/nvidia/cuda-dl-base:26.08-cuda13.4-devel-ubuntu24.04" \
.


Note

Keep the default explicit `torch_cuda_arch_list`

. GPU-less BuildKit builds cannot inspect the host GPU. R100 and VR200 report compute capability 10.7, for which the generic `10.0`

target provides family-compatible kernels. The Ubuntu `devel`

final image is also required: the corresponding `base`

image lacks the CUDA runtime/JIT package closure used by vLLM and the prerelease PyTorch wheel.

`RUN_WHEEL_CHECK=false`

disables only the PyPI publication-size guard for this private staging image.

#### Use the custom-built vLLM Docker image**[¶](https://docs.vllm.ai#use-the-custom-built-vllm-docker-image)

To run vLLM with the custom-built Docker image:

docker run --runtime nvidia --gpus all \
-v ~/.cache/huggingface:/root/.cache/huggingface \
-p 8000:8000 \
--env "HF_TOKEN=<secret>" \
vllm/vllm-openai <args...>


The argument `vllm/vllm-openai`

specifies the image to run, and should be replaced with the name of the custom-built image (the `-t`

tag from the build command).

Note

**For version 0.4.1 and 0.4.2 only** - the vLLM docker images under these versions are supposed to be run under the root user since a library under the root user's home directory, i.e. `/root/.config/vllm/nccl/cu12/libnccl.so.2.18.1`

is required to be loaded during runtime. If you are running the container under a different user, you may need to first change the permissions of the library (and all the parent directories) to allow the user to access it, then run vLLM with environment variable `VLLM_NCCL_SO_PATH=/root/.config/vllm/nccl/cu12/libnccl.so.2.18.1`

.

You can build and run vLLM from source via the provided [docker/Dockerfile.rocm](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm).

## (Optional) Build an image with ROCm software stack

Build a docker image from [docker/Dockerfile.rocm_base](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm_base) which setup ROCm software stack needed by the vLLM. **This step is optional as this rocm_base image is usually prebuilt and store at Docker Hub under tag rocm/vllm-dev:base to speed up user experience.** If you choose to build this rocm_base image yourself, the steps are as follows.


It is important that the user kicks off the docker build using buildkit. Either the user put `DOCKER_BUILDKIT=1`

as environment variable when calling docker build command, or the user needs to set up buildkit in the docker daemon configuration `/etc/docker/daemon.json`

as follows and restart the daemon:

To build vllm on ROCm 7.0 for MI200 and MI300 series, you can use the default:

First, build a docker image from [docker/Dockerfile.rocm](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm) and launch a docker container from the image. It is important that the user kicks off the docker build using buildkit. Either the user put `DOCKER_BUILDKIT=1`

as environment variable when calling docker build command, or the user needs to set up buildkit in the docker daemon configuration /etc/docker/daemon.json as follows and restart the daemon:

[docker/Dockerfile.rocm](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm) uses ROCm 7.0 by default, but also supports ROCm 5.7, 6.0, 6.1, 6.2, 6.3, and 6.4, in older vLLM branches. It provides flexibility to customize the build of docker image using the following arguments:

`BASE_IMAGE`

: specifies the base image used when running`docker build`

. The default value`rocm/vllm-dev:base`

is an image published and maintained by AMD. It is being built using[docker/Dockerfile.rocm_base](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm_base)`ARG_PYTORCH_ROCM_ARCH`

: Allows to override the gfx architecture values from the base docker image

Their values can be passed in when running `docker build`

with `--build-arg`

options.

To build vllm on ROCm 7.0 for MI200 and MI300 series, you can use the default (which build a docker image with `vllm serve`

as entrypoint):

To run vLLM with the custom-built Docker image:

docker run --rm \
--group-add=video \
--cap-add=SYS_PTRACE \
--security-opt seccomp=unconfined \
--device /dev/kfd \
--device /dev/dri \
-v ~/.cache/huggingface:/root/.cache/huggingface \
--env "HF_TOKEN=$HF_TOKEN" \
-p 8000:8000 \
--ipc=host \
vllm/vllm-openai-rocm <args...>


The argument `vllm/vllm-openai-rocm`

specifies the image to run, and should be replaced with the name of the custom-built image (the `-t`

tag from the build command).

To use the docker image as base for development, you can launch it in interactive session through overriding the entrypoint.