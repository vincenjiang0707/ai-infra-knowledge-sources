source: https://rocm.docs.amd.com/projects/ai-ecosystem/en/latest/inference/sglang.html

# SGLang inference and serving on ROCm[#](https://rocm.docs.amd.com#sglang-inference-and-serving-on-rocm)

[SGLang](https://docs.sglang.io/) is an open-source library for fast,
memory-efficient LLM inference and serving. This page describes how to set up
and run SGLang on AMD GPUs using either a prebuilt Docker image (recommended)
or pip. It applies to [supported AMD GPUs and platforms](https://rocm.docs.amd.com/en/latest/about/release-notes.html#ai-ecosystem-support).

## Prerequisites[#](https://rocm.docs.amd.com#prerequisites)

For Instinct and Radeon devices, ensure your host system has the AMD GPU Driver (amdgpu) installed. See the

[ROCm compatibility matrix (ROCm 10.0.0)](https://rocm.docs.amd.com/en/docs-10.0.0/compatibility/compatibility-matrix.html)for driver support information. For installation instructions, see the[AMD GPU Driver documentation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.1/index.html).

For Instinct and Radeon devices, ensure your host system has the AMD GPU Driver (amdgpu) installed. See the

[ROCm compatibility matrix (ROCm 7.14.1)](https://rocm.docs.amd.com/en/docs-7.14.1/compatibility/compatibility-matrix.html)for driver support information. For installation instructions, see the[AMD GPU Driver documentation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.1/index.html).

For Instinct and Radeon devices, ensure your host system has the AMD GPU Driver (amdgpu) installed. See the

[ROCm compatibility matrix (ROCm 7.14.0)](https://rocm.docs.amd.com/en/docs-7.14.0/compatibility/compatibility-matrix.html)for driver support information. For installation instructions, see the[AMD GPU Driver documentation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.1/index.html).

Ensure the host system has

[Docker Engine](https://docs.docker.com/engine/install/)installed.

## Get started[#](https://rocm.docs.amd.com#get-started-rocm-ver-10-0-0-i-docker)

Pull the ROCm SGLang 0.5.15 Docker image.

docker pull rocm/sgl-dev:v0.5.15.post1-ubuntu24.04-py3.14-rocm10.0.0

Start the Docker container.

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ -v <path/to/your/models>:/app/models \ -e HF_HOME="/app/models" \ rocm/sgl-dev:v0.5.15.post1-ubuntu24.04-py3.14-rocm10.0.0 \ bash


Pull the ROCm SGLang 0.5.15 Docker image.

docker pull rocm/sgl-dev:v0.5.15.post1-ubuntu24.04-py3.14-rocm10.0.0

Start the Docker container.

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ -v <path/to/your/models>:/app/models \ -e HF_HOME="/app/models" \ rocm/sgl-dev:v0.5.15.post1-ubuntu24.04-py3.14-rocm10.0.0 \ bash


Pull the ROCm SGLang 0.5.15 Docker image.

docker pull rocm/sgl-dev:v0.5.15.post1-ubuntu24.04-py3.14-rocm10.0.0

Start the Docker container. On Radeon GPUs, disable AITER by unsetting

`SGLANG_USE_AITER`

and`SGLANG_ROCM_FUSED_DECODE_MLA`

. See the[known issue](https://rocm.docs.amd.com#sglang-aiter-ki)for more information.docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ -v <path/to/your/models>:/app/models \ -e HF_HOME="/app/models" \ -e SGLANG_USE_AITER=false \ -e SGLANG_ROCM_FUSED_DECODE_MLA=false \ rocm/sgl-dev:v0.5.15.post1-ubuntu24.04-py3.14-rocm10.0.0 \ bash


See also

## Get started[#](https://rocm.docs.amd.com#get-started-rocm-ver-7-14-1-i-docker)

Pull the ROCm SGLang 0.5.13post1 Docker image.

docker pull rocm/sgl-dev:v0.5.13.post1-ubuntu24.04-py3.14-rocm7.14.1

Start the Docker container.

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ -v <path/to/your/models>:/app/models \ -e HF_HOME="/app/models" \ rocm/sgl-dev:v0.5.13.post1-ubuntu24.04-py3.14-rocm7.14.1 \ bash


Pull the ROCm SGLang 0.5.13post1 Docker image.

docker pull rocm/sgl-dev:v0.5.13.post1-ubuntu24.04-py3.14-rocm7.14.1

Start the Docker container.

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ -v <path/to/your/models>:/app/models \ -e HF_HOME="/app/models" \ rocm/sgl-dev:v0.5.13.post1-ubuntu24.04-py3.14-rocm7.14.1 \ bash


Pull the ROCm SGLang 0.5.13post1 Docker image.

docker pull rocm/sgl-dev:v0.5.13.post1-ubuntu24.04-py3.14-rocm7.14.1

Start the Docker container. On Radeon GPUs, disable AITER by unsetting

`SGLANG_USE_AITER`

and`SGLANG_ROCM_FUSED_DECODE_MLA`

. See the[known issue](https://rocm.docs.amd.com#sglang-aiter-ki)for more information.docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ -v <path/to/your/models>:/app/models \ -e HF_HOME="/app/models" \ -e SGLANG_USE_AITER=false \ -e SGLANG_ROCM_FUSED_DECODE_MLA=false \ rocm/sgl-dev:v0.5.13.post1-ubuntu24.04-py3.14-rocm7.14.1 \ bash


See also

## Get started[#](https://rocm.docs.amd.com#get-started-rocm-ver-7-14-0-i-docker)

Pull the ROCm SGLang 0.5.13post1 Docker image.

docker pull rocm/sgl-dev:v0.5.13.post1-ubuntu24.04-py3.14-rocm7.14

Start the Docker container.

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ -v <path/to/your/models>:/app/models \ -e HF_HOME="/app/models" \ rocm/sgl-dev:v0.5.13.post1-ubuntu24.04-py3.14-rocm7.14 \ bash


Pull the ROCm SGLang 0.5.13post1 Docker image.

docker pull rocm/sgl-dev:v0.5.13.post1-ubuntu24.04-py3.14-rocm7.14

Start the Docker container.

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ -v <path/to/your/models>:/app/models \ -e HF_HOME="/app/models" \ rocm/sgl-dev:v0.5.13.post1-ubuntu24.04-py3.14-rocm7.14 \ bash


Pull the ROCm SGLang 0.5.13post1 Docker image.

docker pull rocm/sgl-dev:v0.5.13.post1-ubuntu24.04-py3.14-rocm7.14

Start the Docker container. On Radeon GPUs, disable AITER by unsetting

`SGLANG_USE_AITER`

and`SGLANG_ROCM_FUSED_DECODE_MLA`

. See the[known issue](https://rocm.docs.amd.com#sglang-aiter-ki)for more information.docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ -v <path/to/your/models>:/app/models \ -e HF_HOME="/app/models" \ -e SGLANG_USE_AITER=false \ -e SGLANG_ROCM_FUSED_DECODE_MLA=false \ rocm/sgl-dev:v0.5.13.post1-ubuntu24.04-py3.14-rocm7.14 \ bash


See also

## Known issues[#](https://rocm.docs.amd.com#known-issues-rocm-ver-10-0-0-rocm-ver-7-14-1-rocm-ver-7-14-0-rocm-ver-10-0-0-i-docker-fam-all-fam-instinct-fam-radeon-fam-ryzen-rocm-ver-7-14-1-i-docker-fam-all-fam-instinct-fam-radeon-fam-ryzen-rocm-ver-7-14-0-i-docker-fam-all-fam-instinct-fam-radeon-fam-ryzen-fam-radeon)

ROCm 7.14 introduces initial SGLang support for AMD Radeon GPUs. Radeon GPU
users should disable AITER and unset `SGLANG_ROCM_FUSED_DECODE_MLA`

, as
both are enabled by default in the SGLang Docker image and may cause some
workloads to fail. See the [SGLang environment variables reference](https://docs.sglang.io/docs/references/environment_variables#environment-variables)
for more details.

```
export SGLANG_USE_AITER=false
export SGLANG_ROCM_FUSED_DECODE_MLA=false
```

Additionally, some models may not function correctly on Radeon GPUs, including certain Mixture-of-Experts (MoE) models (such as GPT-OSS-20B and MiniMax-M2.7) and Qwen3-ASR models. Users experiencing these issues are recommended to use the latest upstream SGLang versions, which will include the necessary fixes once they are merged.

SGLang inference workloads using the default AITER attention backend might fail on some AMD Radeon graphics products, such as the Radeon PRO W7900, Radeon AI PRO R9700, and Radeon RX 9070 XT. As a workaround, configure SGLang to use the Triton attention backend (

`--attention-backend triton`

) or disable AITER:export SGLANG_USE_AITER=0 export SGLANG_USE_AITER_AR=0