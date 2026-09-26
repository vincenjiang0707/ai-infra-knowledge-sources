source: https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/inference/benchmark-docker/pytorch-inference.html

# PyTorch inference performance testing[#](https://rocm.docs.amd.com#pytorch-inference-performance-testing)

2026-02-19

8 min read time

The [ROCm PyTorch Docker](https://hub.docker.com/r/rocm/pytorch/tags) image offers a prebuilt,
optimized environment for testing model inference performance on AMD Instinct™ MI300X Series
GPUs. This guide demonstrates how to use the AMD Model Automation and Dashboarding (MAD)
tool with the ROCm PyTorch container to test inference performance on various models efficiently.

## Supported models[#](https://rocm.docs.amd.com#supported-models)

The following models are supported for inference performance benchmarking with PyTorch and ROCm. Some instructions, commands, and recommendations in this documentation might vary by model – select one to get started.

Note

See the [CLIP model card on Hugging Face](https://huggingface.co/laion/CLIP-ViT-B-32-laion2B-s34B-b79K) to learn more about your selected model.
Some models require access authorization before use via an external license agreement through a third party.

Note

See the [Chai-1 model card on Hugging Face](https://huggingface.co/chaidiscovery/chai-1) to learn more about your selected model.
Some models require access authorization before use via an external license agreement through a third party.

Note

See the [Mochi 1 model card on Hugging Face](https://huggingface.co/genmo/mochi-1-preview) to learn more about your selected model.
Some models require access authorization before use via an external license agreement through a third party.

Note

See the [Wan2.1 model card on Hugging Face](https://huggingface.co/Wan-AI/Wan2.1-T2V-14B) to learn more about your selected model.
Some models require access authorization before use via an external license agreement through a third party.

Note

See the [Janus Pro 7B model card on Hugging Face](https://huggingface.co/deepseek-ai/Janus-Pro-7B) to learn more about your selected model.
Some models require access authorization before use via an external license agreement through a third party.

Note

See the [Hunyuan Video model card on Hugging Face](https://huggingface.co/tencent/HunyuanVideo) to learn more about your selected model.
Some models require access authorization before use via an external license agreement through a third party.

## System validation[#](https://rocm.docs.amd.com#system-validation)

Before running AI workloads, it’s important to validate that your AMD hardware is configured correctly and performing optimally.

To optimize performance, disable automatic NUMA balancing. Otherwise, the GPU
might hang until the periodic balancing is finalized. For more information,
see the [system validation steps](https://rocm.docs.amd.com/system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization).

```
# disable automatic NUMA balancing
sh -c 'echo 0 > /proc/sys/kernel/numa_balancing'
# check if NUMA balancing is disabled (returns 0 if disabled)
cat /proc/sys/kernel/numa_balancing
0
```

To test for optimal performance, consult the recommended [System health benchmarks](https://rocm.docs.amd.com/system-setup/system-health-check.html#rocm-for-ai-system-health-bench). This suite of tests will help you verify and fine-tune your
system’s configuration.

## Pull the Docker image[#](https://rocm.docs.amd.com#pull-the-docker-image)

Use the following command to pull the [ROCm PyTorch Docker image](https://hub.docker.com/layers/rocm/pytorch/rocm6.2.3_ubuntu22.04_py3.10_pytorch_release_2.3.0_triton_llvm_reg_issue/images/sha256-b736a4239ab38a9d0e448af6d4adca83b117debed00bfbe33846f99c4540f79b) from Docker Hub.

```
docker pull rocm/pytorch:rocm6.2.3_ubuntu22.04_py3.10_pytorch_release_2.3.0_triton_llvm_reg_issue
```

Note

The Chai-1 benchmark uses a specifically selected Docker image using ROCm 6.2.3 and PyTorch 2.3.0 to address an accuracy issue.

Use the following command to pull the [ROCm PyTorch Docker image](https://hub.docker.com/layers/rocm/pytorch/latest/images/sha256-05b55983e5154f46e7441897d0908d79877370adca4d1fff4899d9539d6c4969) from Docker Hub.

```
docker pull rocm/pytorch:latest
```

## Benchmarking[#](https://rocm.docs.amd.com#benchmarking)

To simplify performance testing, the ROCm Model Automation and Dashboarding
([ROCm/MAD](https://github.com/ROCm/MAD)) project provides ready-to-use scripts and configuration.
To start, clone the MAD repository to a local directory and install the required packages on the
host machine.

```
git clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [CLIP](https://huggingface.co/laion/CLIP-ViT-B-32-laion2B-s34B-b79K) model
using one GPU with the `float16`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
madengine run \
--tags pyt_clip_inference \
--keep-model-dir \
--live-output \
--timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_clip_inference`

. The latency and throughput reports of the
model are collected in `perf_pyt_clip_inference.csv`

.

Note

For improved performance, consider enabling TunableOp. By default,
`pyt_clip_inference`

runs with TunableOp disabled (see
[ROCm/MAD](https://github.com/ROCm/MAD/blob/develop/models.json)). To enable
it, include the `--tunableop on`

argument in your run.

Enabling TunableOp triggers a two-pass run – a warm-up followed by the performance-collection run. Although this might increase the initial training time, it can result in a performance gain.

To simplify performance testing, the ROCm Model Automation and Dashboarding
([ROCm/MAD](https://github.com/ROCm/MAD)) project provides ready-to-use scripts and configuration.
To start, clone the MAD repository to a local directory and install the required packages on the
host machine.

```
git clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [Chai-1](https://huggingface.co/chaidiscovery/chai-1) model
using one GPU with the `float16`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
madengine run \
--tags pyt_chai1_inference \
--keep-model-dir \
--live-output \
--timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_chai1_inference`

. The latency and throughput reports of the
model are collected in `perf_pyt_chai1_inference.csv`

.

Note

For improved performance, consider enabling TunableOp. By default,
`pyt_chai1_inference`

runs with TunableOp disabled (see
[ROCm/MAD](https://github.com/ROCm/MAD/blob/develop/models.json)). To enable
it, include the `--tunableop on`

argument in your run.

Enabling TunableOp triggers a two-pass run – a warm-up followed by the performance-collection run. Although this might increase the initial training time, it can result in a performance gain.

To simplify performance testing, the ROCm Model Automation and Dashboarding
([ROCm/MAD](https://github.com/ROCm/MAD)) project provides ready-to-use scripts and configuration.
To start, clone the MAD repository to a local directory and install the required packages on the
host machine.

```
git clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [Mochi 1](https://huggingface.co/genmo/mochi-1-preview) model
using one GPU with the `float16`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
madengine run \
--tags pyt_mochi_video_inference \
--keep-model-dir \
--live-output \
--timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_mochi_video_inference`

. The latency and throughput reports of the
model are collected in `perf_pyt_mochi_video_inference.csv`

.

Note

For improved performance, consider enabling TunableOp. By default,
`pyt_mochi_video_inference`

runs with TunableOp disabled (see
[ROCm/MAD](https://github.com/ROCm/MAD/blob/develop/models.json)). To enable
it, include the `--tunableop on`

argument in your run.

Enabling TunableOp triggers a two-pass run – a warm-up followed by the performance-collection run. Although this might increase the initial training time, it can result in a performance gain.

To simplify performance testing, the ROCm Model Automation and Dashboarding
([ROCm/MAD](https://github.com/ROCm/MAD)) project provides ready-to-use scripts and configuration.
To start, clone the MAD repository to a local directory and install the required packages on the
host machine.

```
git clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [Wan2.1](https://huggingface.co/Wan-AI/Wan2.1-T2V-14B) model
using one GPU with the `bfloat16`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
madengine run \
--tags pyt_wan2.1_inference \
--keep-model-dir \
--live-output \
--timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_wan2.1_inference`

. The latency and throughput reports of the
model are collected in `perf_pyt_wan2.1_inference.csv`

.

Note

For improved performance, consider enabling TunableOp. By default,
`pyt_wan2.1_inference`

runs with TunableOp disabled (see
[ROCm/MAD](https://github.com/ROCm/MAD/blob/develop/models.json)). To enable
it, include the `--tunableop on`

argument in your run.

Enabling TunableOp triggers a two-pass run – a warm-up followed by the performance-collection run. Although this might increase the initial training time, it can result in a performance gain.

To simplify performance testing, the ROCm Model Automation and Dashboarding
([ROCm/MAD](https://github.com/ROCm/MAD)) project provides ready-to-use scripts and configuration.
To start, clone the MAD repository to a local directory and install the required packages on the
host machine.

```
git clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [Janus Pro 7B](https://huggingface.co/deepseek-ai/Janus-Pro-7B) model
using one GPU with the `bfloat16`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
madengine run \
--tags pyt_janus_pro_inference \
--keep-model-dir \
--live-output \
--timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_janus_pro_inference`

. The latency and throughput reports of the
model are collected in `perf_pyt_janus_pro_inference.csv`

.

To simplify performance testing, the ROCm Model Automation and Dashboarding
([ROCm/MAD](https://github.com/ROCm/MAD)) project provides ready-to-use scripts and configuration.
To start, clone the MAD repository to a local directory and install the required packages on the
host machine.

```
git clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to run the performance benchmark test on the [Hunyuan Video](https://huggingface.co/tencent/HunyuanVideo) model
using one GPU with the `float16`

data type on the host machine.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
madengine run \
--tags pyt_hy_video \
--keep-model-dir \
--live-output \
--timeout 28800
```

MAD launches a Docker container with the name
`container_ci-pyt_hy_video`

. The latency and throughput reports of the
model are collected in `perf_pyt_hy_video.csv`

.

Note

For improved performance, consider enabling TunableOp. By default,
`pyt_hy_video`

runs with TunableOp disabled (see
[ROCm/MAD](https://github.com/ROCm/MAD/blob/develop/models.json)). To enable
it, include the `--tunableop on`

argument in your run.

Enabling TunableOp triggers a two-pass run – a warm-up followed by the performance-collection run. Although this might increase the initial training time, it can result in a performance gain.

## Further reading[#](https://rocm.docs.amd.com#further-reading)

To learn more about MAD and the

`madengine`

CLI, see the[MAD usage guide](https://github.com/ROCm/MAD?tab=readme-ov-file#usage-guide).To learn more about system settings and management practices to configure your system for AMD Instinct MI300X Series GPUs, see

[AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html).For application performance optimization strategies for HPC and AI workloads, including inference with vLLM, see

[AMD Instinct MI300 Series / MI350 Series workload optimization](https://rocm.docs.amd.com/inference-optimization/workload.html).To learn how to run LLM models from Hugging Face or your model, see

[Running models from Hugging Face](https://rocm.docs.amd.com/hugging-face-models.html).To learn how to optimize inference on LLMs, see

[Inference optimization](https://rocm.docs.amd.com/inference-optimization/index.html).To learn how to fine-tune LLMs, see

[Fine-tuning LLMs](https://rocm.docs.amd.com/fine-tuning/index.html).