source: https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/training/benchmark-docker/primus-pytorch.html

# Training a model with Primus and PyTorch[#](https://rocm.docs.amd.com#training-a-model-with-primus-and-pytorch)

2026-06-30

19 min read time

[Primus](https://github.com/AMD-AGI/Primus) is a unified and flexible
LLM training framework designed to streamline training. It streamlines LLM
training on AMD Instinct GPUs using a modular, reproducible configuration paradigm.
Primus now supports the PyTorch torchtitan backend.

Note

For a unified training solution on AMD GPUs with ROCm, the [rocm/pytorch-training](https://hub.docker.com/r/rocm/pytorch-training/) Docker Hub registry will be
deprecated soon in favor of [rocm/primus](https://hub.docker.com/r/rocm/primus).
The `rocm/primus`

Docker containers will cover PyTorch training ecosystem frameworks,
including torchtitan and [Megatron-LM](https://rocm.docs.amd.com/primus-megatron.html).

Primus with the PyTorch torchtitan backend is designed to replace the
[ROCm PyTorch training](https://rocm.docs.amd.com/pytorch-training.html) workflow. See
[Training a model with PyTorch on ROCm](https://rocm.docs.amd.com/pytorch-training.html) to see steps to run workloads without Primus.

AMD provides a ready-to-use Docker image for MI355X, MI350X, MI325X, and MI300X GPUs containing essential components for Primus and PyTorch training with Primus Turbo optimizations.

Software component |
Version |
|---|---|
ROCm |
7.14.0a20260608 |
PyTorch |
2.12.0+git7e98855 |
Python |
3.12.3 |
Transformer Engine |
2.14.0.dev0+e6ede467 |
Flash Attention |
2.8.3 |
hipBLASLt |
1.4.0-c2fafc16 |
Triton |
3.7.0+gitb4e20bbe |
RCCL |
2.28.9 |

## Supported models[#](https://rocm.docs.amd.com#supported-models)

The following models are pre-optimized for performance on the AMD Instinct MI325X and MI300X GPUs. Some instructions, commands, and training recommendations in this documentation might vary by model – select one to get started.

See also

For additional workloads, including Llama 3.3, Llama 3.2, Llama 2, GPT OSS, Qwen, and Flux models,
see the documentation [Training a model with PyTorch on ROCm](https://rocm.docs.amd.com/pytorch-training.html) (without Primus)

## System validation[#](https://rocm.docs.amd.com#system-validation)

Before running AI workloads, it’s important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you
can skip this step. Otherwise, complete the procedures in the [System validation and
optimization](https://rocm.docs.amd.com/system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization) guide to properly configure your system settings
before starting training.

To test for optimal performance, consult the recommended [System health benchmarks](https://rocm.docs.amd.com/system-setup/system-health-check.html#rocm-for-ai-system-health-bench). This suite of tests will help you verify and fine-tune your
system’s configuration.

This Docker image is optimized for specific model configurations outlined below. Performance can vary for other training workloads, as AMD doesn’t test configurations and run conditions outside those described.

## Pull the Docker image[#](https://rocm.docs.amd.com#pull-the-docker-image)

Use the following command to pull the Docker image from Docker Hub.

```
docker pull rocm/primus:v26.4
```

## Run training[#](https://rocm.docs.amd.com#run-training)

Once the setup is complete, choose between the following two workflows to start benchmarking training.
For fine-tuning workloads and multi-node training examples, see [Training a model with PyTorch on ROCm](https://rocm.docs.amd.com/pytorch-training.html) (without Primus).
For best performance on MI325X, MI350X, and MI355X GPUs, you might need to
tweak some configurations (such as batch sizes).

The following run commands are tailored to Llama 3.1 8B.
See [Supported models](https://rocm.docs.amd.com#amd-primus-pytorch-model-support-v26-4) to switch to another available model.

Download the Docker image and required packages

Pull the

`rocm/primus:v26.4`

Docker image from Docker Hub.docker pull rocm/primus:v26.4

Run the Docker container.

docker run -it \ --device /dev/dri \ --device /dev/kfd \ --network host \ --ipc host \ --group-add video \ --cap-add SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ -v $HOME/.ssh:/root/.ssh \ --shm-size 64G \ --name training_env \ rocm/primus:v26.4

Use these commands if you exit the

`training_env`

container and need to return to it.docker start training_env docker exec -it training_env bash

The Docker container hosts the

[Primus](https://github.com/AMD-AGI/Primus/tree/release/v26.4)repository at tag`release/v26.4`

.

Setup

The following benchmarking examples require downloading models and datasets
from Hugging Face. To ensure successful access to gated repos, set your
`HF_TOKEN`

.

```
export HF_TOKEN=$your_personal_hugging_face_access_token
```

To get started, navigate to the `Primus`

directory in your container.

```
cd /workspace/Primus
```

Now, to start the pretraining benchmark, use the `run_pretrain.sh`

script
included with Primus with the appropriate options.

Pretraining examples

Use the following command to run train Llama 3.1 8B with BF16 precision using Primus torchtitan.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_8B-BF16-pretrain.yaml
```

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_8B-BF16-pretrain.yaml
```

To train Llama 3.1 8B with FP8 precision, use the following command.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_8B-FP8-pretrain.yaml
```

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_8B-FP8-pretrain.yaml
```

Use the following command to run train Llama 3.1 70B with BF16 precision using Primus torchtitan.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_70B-BF16-pretrain.yaml
```

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_70B-BF16-pretrain.yaml
```

To train Llama 3.1 70B with FP8 precision, use the following command.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_70B-FP8-pretrain.yaml
```

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_70B-FP8-pretrain.yaml
```

Only multi-node training configurations are currently available for Llama 3.1 405B.
See the
[multi-node training examples](https://rocm.docs.amd.com#amd-primus-pytorch-multi-node-examples-v26-4)
for training instructions.

Use the following command to run train DeepSeek V3 16B with BF16 precision using Primus torchtitan.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_deepseek_v3_16b.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/deepseek_v3_16b-pretrain.yaml
```

```
bash runner/primus-cli direct \
--log_file /tmp/primus_deepseek_v3_16b.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/deepseek_v3_16b-pretrain.yaml
```

The following run commands are tailored to Llama 3.1 70B.
See [Supported models](https://rocm.docs.amd.com#amd-primus-pytorch-model-support-v26-4) to switch to another available model.

Download the Docker image and required packages

Pull the

`rocm/primus:v26.4`

Docker image from Docker Hub.docker pull rocm/primus:v26.4

Run the Docker container.

docker run -it \ --device /dev/dri \ --device /dev/kfd \ --network host \ --ipc host \ --group-add video \ --cap-add SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ -v $HOME/.ssh:/root/.ssh \ --shm-size 64G \ --name training_env \ rocm/primus:v26.4

Use these commands if you exit the

`training_env`

container and need to return to it.docker start training_env docker exec -it training_env bash

The Docker container hosts the

[Primus](https://github.com/AMD-AGI/Primus/tree/release/v26.4)repository at tag`release/v26.4`

.

Setup

The following benchmarking examples require downloading models and datasets
from Hugging Face. To ensure successful access to gated repos, set your
`HF_TOKEN`

.

```
export HF_TOKEN=$your_personal_hugging_face_access_token
```

To get started, navigate to the `Primus`

directory in your container.

```
cd /workspace/Primus
```

Now, to start the pretraining benchmark, use the `run_pretrain.sh`

script
included with Primus with the appropriate options.

Pretraining examples

Use the following command to run train Llama 3.1 8B with BF16 precision using Primus torchtitan.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_8B-BF16-pretrain.yaml
```

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_8B-BF16-pretrain.yaml
```

To train Llama 3.1 8B with FP8 precision, use the following command.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_8B-FP8-pretrain.yaml
```

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_8B-FP8-pretrain.yaml
```

Use the following command to run train Llama 3.1 70B with BF16 precision using Primus torchtitan.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_70B-BF16-pretrain.yaml
```

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_70B-BF16-pretrain.yaml
```

To train Llama 3.1 70B with FP8 precision, use the following command.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_70B-FP8-pretrain.yaml
```

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_70B-FP8-pretrain.yaml
```

Only multi-node training configurations are currently available for Llama 3.1 405B.
See the
[multi-node training examples](https://rocm.docs.amd.com#amd-primus-pytorch-multi-node-examples-v26-4)
for training instructions.

Use the following command to run train DeepSeek V3 16B with BF16 precision using Primus torchtitan.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_deepseek_v3_16b.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/deepseek_v3_16b-pretrain.yaml
```

```
bash runner/primus-cli direct \
--log_file /tmp/primus_deepseek_v3_16b.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/deepseek_v3_16b-pretrain.yaml
```

The following run commands are tailored to Llama 3.1 405B.
See [Supported models](https://rocm.docs.amd.com#amd-primus-pytorch-model-support-v26-4) to switch to another available model.

Download the Docker image and required packages

Pull the

`rocm/primus:v26.4`

Docker image from Docker Hub.docker pull rocm/primus:v26.4

Run the Docker container.

docker run -it \ --device /dev/dri \ --device /dev/kfd \ --network host \ --ipc host \ --group-add video \ --cap-add SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ -v $HOME/.ssh:/root/.ssh \ --shm-size 64G \ --name training_env \ rocm/primus:v26.4

Use these commands if you exit the

`training_env`

container and need to return to it.docker start training_env docker exec -it training_env bash

The Docker container hosts the

[Primus](https://github.com/AMD-AGI/Primus/tree/release/v26.4)repository at tag`release/v26.4`

.

Setup

The following benchmarking examples require downloading models and datasets
from Hugging Face. To ensure successful access to gated repos, set your
`HF_TOKEN`

.

```
export HF_TOKEN=$your_personal_hugging_face_access_token
```

To get started, navigate to the `Primus`

directory in your container.

```
cd /workspace/Primus
```

Now, to start the pretraining benchmark, use the `run_pretrain.sh`

script
included with Primus with the appropriate options.

Pretraining examples

Use the following command to run train Llama 3.1 8B with BF16 precision using Primus torchtitan.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_8B-BF16-pretrain.yaml
```

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_8B-BF16-pretrain.yaml
```

To train Llama 3.1 8B with FP8 precision, use the following command.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_8B-FP8-pretrain.yaml
```

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_8B-FP8-pretrain.yaml
```

Use the following command to run train Llama 3.1 70B with BF16 precision using Primus torchtitan.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_70B-BF16-pretrain.yaml
```

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_70B-BF16-pretrain.yaml
```

To train Llama 3.1 70B with FP8 precision, use the following command.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_70B-FP8-pretrain.yaml
```

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_70B-FP8-pretrain.yaml
```

Only multi-node training configurations are currently available for Llama 3.1 405B.
See the
[multi-node training examples](https://rocm.docs.amd.com#amd-primus-pytorch-multi-node-examples-v26-4)
for training instructions.

Use the following command to run train DeepSeek V3 16B with BF16 precision using Primus torchtitan.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_deepseek_v3_16b.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/deepseek_v3_16b-pretrain.yaml
```

```
bash runner/primus-cli direct \
--log_file /tmp/primus_deepseek_v3_16b.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/deepseek_v3_16b-pretrain.yaml
```

The following run commands are tailored to DeepSeek V3 16B.
See [Supported models](https://rocm.docs.amd.com#amd-primus-pytorch-model-support-v26-4) to switch to another available model.

Download the Docker image and required packages

Pull the

`rocm/primus:v26.4`

Docker image from Docker Hub.docker pull rocm/primus:v26.4

Run the Docker container.

docker run -it \ --device /dev/dri \ --device /dev/kfd \ --network host \ --ipc host \ --group-add video \ --cap-add SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ -v $HOME/.ssh:/root/.ssh \ --shm-size 64G \ --name training_env \ rocm/primus:v26.4

Use these commands if you exit the

`training_env`

container and need to return to it.docker start training_env docker exec -it training_env bash

The Docker container hosts the

[Primus](https://github.com/AMD-AGI/Primus/tree/release/v26.4)repository at tag`release/v26.4`

.

Setup

The following benchmarking examples require downloading models and datasets
from Hugging Face. To ensure successful access to gated repos, set your
`HF_TOKEN`

.

```
export HF_TOKEN=$your_personal_hugging_face_access_token
```

To get started, navigate to the `Primus`

directory in your container.

```
cd /workspace/Primus
```

Now, to start the pretraining benchmark, use the `run_pretrain.sh`

script
included with Primus with the appropriate options.

Pretraining examples

Use the following command to run train Llama 3.1 8B with BF16 precision using Primus torchtitan.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_8B-BF16-pretrain.yaml
```

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_8B-BF16-pretrain.yaml
```

To train Llama 3.1 8B with FP8 precision, use the following command.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_8B-FP8-pretrain.yaml
```

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_8B-FP8-pretrain.yaml
```

Use the following command to run train Llama 3.1 70B with BF16 precision using Primus torchtitan.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_70B-BF16-pretrain.yaml
```

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_70B-BF16-pretrain.yaml
```

To train Llama 3.1 70B with FP8 precision, use the following command.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_70B-FP8-pretrain.yaml
```

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_70B-FP8-pretrain.yaml
```

Only multi-node training configurations are currently available for Llama 3.1 405B.
See the
[multi-node training examples](https://rocm.docs.amd.com#amd-primus-pytorch-multi-node-examples-v26-4)
for training instructions.

Use the following command to run train DeepSeek V3 16B with BF16 precision using Primus torchtitan.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_deepseek_v3_16b.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/deepseek_v3_16b-pretrain.yaml
```

```
bash runner/primus-cli direct \
--log_file /tmp/primus_deepseek_v3_16b.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/deepseek_v3_16b-pretrain.yaml
```

The following run command is tailored to Llama 3.1 8B.
See [Supported models](https://rocm.docs.amd.com#amd-primus-pytorch-model-support-v26-4) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.git clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Llama 3.1 8B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags primus_pyt_train_llama-3.1-8b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-primus_pyt_train_llama-3.1-8b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to Llama 3.1 70B.
See [Supported models](https://rocm.docs.amd.com#amd-primus-pytorch-model-support-v26-4) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.git clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Llama 3.1 70B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags primus_pyt_train_llama-3.1-70b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-primus_pyt_train_llama-3.1-70b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to Llama 3.1 405B.
See [Supported models](https://rocm.docs.amd.com#amd-primus-pytorch-model-support-v26-4) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.git clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Llama 3.1 405B model using one node with the FP8 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags primus_pyt_train_llama-3.1-405b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-primus_pyt_train_llama-3.1-405b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to DeepSeek V3 16B.
See [Supported models](https://rocm.docs.amd.com#amd-primus-pytorch-model-support-v26-4) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.git clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the DeepSeek V3 16B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags primus_pyt_train_deepseek-v3-16b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-primus_pyt_train_deepseek-v3-16b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

## Multi-node training examples[#](https://rocm.docs.amd.com#multi-node-training-examples)

Refer to [Multi-node setup for AI workloads](https://rocm.docs.amd.com/system-setup/multi-node-setup.html) to configure your environment for multi-node
training.

To run training on multiple nodes, use `primus-cli`

to launch multi-node workloads. Use the following steps to set up your environment:

Important

**Verify NCCL / network environment first.** The `primus-cli`

launcher sets sensible
`NCCL_*`

defaults via `base_env.sh`

, but auto-detection can pick the wrong device
on multi-NIC nodes. Always confirm `NCCL_IB_HCA`

, `NCCL_IB_GID_INDEX`

,
`NCCL_SOCKET_IFNAME`

, and `GLOO_SOCKET_IFNAME`

(set to the same value as
`NCCL_SOCKET_IFNAME`

) are correct for your fabric. If necessary, export these
environment variables before running.

```
git clone --recurse-submodules https://github.com/AMD-AGI/Primus.git
cd Primus/
git checkout v26.4.0
git submodule update --init --recursive
export DOCKER_IMAGE=rocm/primus:v26.4
export HF_TOKEN=<your_HF_token>
export NCCL_IB_HCA=<your_NCCL_IB_HCA> # specify which RDMA interfaces to use for communication
export NCCL_SOCKET_IFNAME=<your_NCCL_SOCKET_IFNAME> # your Network Interface
export GLOO_SOCKET_IFNAME=<your_GLOO_SOCKET_IFNAME> # your Network Interface
export NCCL_IB_GID_INDEX=3 # Set InfiniBand GID index for NCCL communication. Default is 3 for ROCE
# MI300/MI325X only -- for better performance
export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
export NVTE_CK_IS_V3_ATOMIC_FP32=1
```

For clusters using AMD AINIC, also set the following:

```
export USING_AINIC=1
export NCCL_PXN_DISABLE=0
export NCCL_IB_GID_INDEX=1
```

Note

Make sure correct network drivers are installed on the nodes. If inside a Docker, either install the drivers inside the Docker container or pass the network drivers from the host while creating the Docker container.

If

`NCCL_IB_HCA`

and`NCCL_SOCKET_IFNAME`

are not set, Primus will try to auto-detect. However, since NICs can vary across different clusters, it is encouraged to explicitly export your NCCL parameters for the cluster.To find your network interface, you can use

`ip a`

.To find RDMA interfaces, you can use

`ibv_devices`

to get the list of all the RDMA/IB devices.

Once setup is complete, run the appropriate training command.
The following run commands are tailored to **Llama 3.1 8B**.
See [Supported models](https://rocm.docs.amd.com#amd-primus-pytorch-model-support-v26-4) to switch to another available model.

To train Llama 3.1 8B FP8 on 8 nodes, run:

```
./primus-cli slurm srun -N 8 -- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_8B-FP8-pretrain.yaml
```

To train Llama 3.1 8B BF16 on 8 nodes, run:

```
./primus-cli slurm srun -N 8 -- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_8B-BF16-pretrain.yaml
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to **Llama 3.1 70B**.
See [Supported models](https://rocm.docs.amd.com#amd-primus-pytorch-model-support-v26-4) to switch to another available model.

To train Llama 3.1 70B FP8 on 4 nodes using `primus-cli`

(recommended), run:

```
# In the Primus directory
./primus-cli slurm srun -N 4 -- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_70B-FP8-pretrain.yaml \
--training.local_batch_size 6 \
--training.global_batch_size 192 \
--training.mock_data True
```

Alternatively, using the legacy script:

```
NNODES=4 EXP=examples/torchtitan/configs/MI355X/llama3.1_70B-FP8-pretrain.yaml \
bash examples/run_slurm_pretrain.sh \
--training.local_batch_size 6 \
--training.global_batch_size 192 \
--training.mock_data True
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to **DeepSeek V3 16B**.
See [Supported models](https://rocm.docs.amd.com#amd-primus-pytorch-model-support-v26-4) to switch to another available model.

To train DeepSeek V3 16B BF16 on 8 nodes, run:

```
./primus-cli slurm srun -N 8 -- train pretrain \
--config examples/torchtitan/configs/MI300X/deepseek_v3_16b-pretrain.yaml
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to Llama 3.1 405B.
See [Supported models](https://rocm.docs.amd.com#amd-primus-pytorch-model-support-v26-4) to switch to another available model.

To train Llama 3.1 405B FP8 on 8 nodes using `primus-cli`

(recommended), run:

```
# In the Primus directory
./primus-cli slurm srun -N 8 -- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_405B-FP8-pretrain.yaml \
--training.local_batch_size 3 \
--training.global_batch_size 192 \
--training.mock_data True
```

Alternatively, using the legacy script:

```
NNODES=8 EXP=examples/torchtitan/configs/MI355X/llama3.1_405B-FP8-pretrain.yaml \
bash examples/run_slurm_pretrain.sh \
--training.local_batch_size 3 \
--training.global_batch_size 192 \
--training.mock_data True
```

## Further reading[#](https://rocm.docs.amd.com#further-reading)

For an introduction to Primus, see

[Primus: A Lightweight, Unified Training Framework for Large Models on AMD GPUs](https://rocm.blogs.amd.com/software-tools-optimization/primus/README.html).To learn more about MAD and the

`madengine`

CLI, see the[MAD usage guide](https://github.com/ROCm/MAD?tab=readme-ov-file#usage-guide).To learn more about system settings and management practices to configure your system for AMD Instinct MI300X Series GPUs, see

[AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html).For a list of other ready-made Docker images for AI with ROCm, see

[AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models).

## Previous versions[#](https://rocm.docs.amd.com#previous-versions)

See [PyTorch training performance testing version history](https://rocm.docs.amd.com/previous-versions/pytorch-training-history.html) to find documentation for previous releases
of the Primus with torchtitan training recipe.