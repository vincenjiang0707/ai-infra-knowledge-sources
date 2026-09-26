source: https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/training/benchmark-docker/primus-megatron.html

# Training a model with Primus and Megatron-LM[#](https://rocm.docs.amd.com#training-a-model-with-primus-and-megatron-lm)

2026-06-30

27 min read time

[Primus](https://github.com/AMD-AGI/Primus) is a unified and flexible
training framework for AMD Instinct GPUs designed to support multiple training
engine backends – including Megatron – to deliver scalable, high-performance
model training. Performance acceleration is powered by [Primus Turbo](https://github.com/AMD-AGI/Primus-Turbo) and ROCm libraries.

Note

The `rocm/pytorch-training`

Docker Hub registry will be deprecated soon in
favor of [rocm/primus](https://hub.docker.com/r/rocm/primus).
The `rocm/primus`

Docker containers will cover PyTorch training ecosystem frameworks,
including Megatron-LM and [torchtitan](https://rocm.docs.amd.com/primus-pytorch.html).

Primus with Megatron is designed to replace the [ROCm Megatron-LM
training](https://rocm.docs.amd.com/megatron-lm.html) workflow. To learn how to migrate workloads from
Megatron-LM to Primus with Megatron, see
[Migrating workloads to Primus (Megatron backend) from Megatron-LM](https://rocm.docs.amd.com/previous-versions/megatron-lm-primus-migration-guide.html).

AMD provides a ready-to-use Docker images for MI355X, MI350X, MI325X, and MI300X GPUs containing essential components for Primus, ROCm, and Megatron-LM.

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

The following models are pre-optimized for performance on AMD Instinct GPUs. Some instructions, commands, and training examples in this documentation might vary by model – select one to get started.

Note

Some models, such as Llama, require an external license agreement through a third party (for example, Meta).

## System validation[#](https://rocm.docs.amd.com#system-validation)

Before running AI workloads, it’s important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you
can skip this step. Otherwise, complete the procedures in the [System validation and
optimization](https://rocm.docs.amd.com/system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization) guide to properly configure your system settings
before starting training.

To test for optimal performance, consult the recommended [System health benchmarks](https://rocm.docs.amd.com/system-setup/system-health-check.html#rocm-for-ai-system-health-bench). This suite of tests will help you verify and fine-tune your
system’s configuration.

## Environment setup[#](https://rocm.docs.amd.com#environment-setup)

Use the following instructions to set up the environment, configure the script to train models, and reproduce the benchmark results on AMD Instinct GPUs.

Pull the Docker image

Pull the

`rocm/primus:v26.4`

Docker image from Docker Hub.docker pull rocm/primus:v26.4

Launch the Docker container.

docker run -it \ --device /dev/dri \ --device /dev/kfd \ --device /dev/infiniband \ --network host --ipc host \ --group-add video \ --cap-add SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:/userHome \ --shm-size 128G \ --name primus_training_env \ rocm/primus:v26.4

Use these commands if you exit the

`primus_training_env`

container and need to return to it.docker start primus_training_env docker exec -it primus_training_env bash


The Docker container hosts the [Primus](https://github.com/AMD-AGI/Primus/tree/release/v26.4) repository at tag `release/v26.4`

.

## Configuration[#](https://rocm.docs.amd.com#configuration)

Primus defines a training configuration in YAML for each model in
[examples/megatron/configs](https://github.com/AMD-AGI/Primus/tree/release/v26.4/examples/megatron/configs).

For example, to update training parameters for Llama 3.3 70B, you can
update `examples/megatron/configs/llama3.3_70B-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for Llama 3.1 8B, you can
update `examples/megatron/configs/llama3.1_8B-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for Llama 3.1 70B, you can
update `examples/megatron/configs/llama3.1_70B-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for Llama 2 7B, you can
update `examples/megatron/configs/llama2_7B-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for Llama 2 70B, you can
update `examples/megatron/configs/llama2_70B-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for Llama 3.1 405B, you can
update `examples/megatron/configs/llama3.1_405B-FP8-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for Zebra-Llama 1B, you can
update `examples/megatron/configs/zebra_llama_1b-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for Zebra-Llama 3B, you can
update `examples/megatron/configs/zebra_llama_3b-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for Zebra-Llama 8B, you can
update `examples/megatron/configs/zebra_llama_8b-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for GPT-OSS-20B, you can
update `examples/megatron/configs/gpt_oss_20B-BF16-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for GPT-OSS-120B, you can
update `examples/megatron/configs/gpt_oss_120B-BF16-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for DeepSeek-V2-Lite, you can
update `examples/megatron/configs/deepseek_v2_lite-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for Mixtral 8x7B, you can
update `examples/megatron/configs/mixtral_8x7B_v0.1-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for Mixtral 8x22B, you can
update `examples/megatron/configs/mixtral_8x22B_v0.1-BF16-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for Qwen 3 32B SFT, you can
update `examples/megatron/configs/qwen3_32b_sft_posttrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for Qwen 3 32B LoRA, you can
update `examples/megatron/configs/qwen3_32b_lora_posttrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for Qwen 3 30B A3B, you can
update `examples/megatron/configs/qwen3_30B_A3B-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for Qwen 2.5 7B, you can
update `examples/megatron/configs/qwen2.5_7B-BF16-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for Qwen 2.5 72B, you can
update `examples/megatron/configs/qwen2.5_72B-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

For example, to update training parameters for Qwen3 235B (A22B), you can
update `examples/megatron/configs/qwen3_235B_A22B-BF16-pretrain.yaml`

. Training
configuration YAML files for other models follow this naming convention.

Note

See [Key options](https://rocm.docs.amd.com/previous-versions/primus-megatron-v25.8.html#amd-primus-megatron-lm-benchmark-test-vars) for more information on configuration options.

### Dataset options[#](https://rocm.docs.amd.com#dataset-options)

You can use either mock data or real data for training.

Mock data can be useful for testing and validation. Use the

`mock_data`

field to toggle between mock and real data. The default value is`true`

for enabled.mock_data: true

If you’re using a real dataset, update the

`train_data_path`

field to point to the location of your dataset.mock_data: false train_data_path: /path/to/your/dataset

Ensure that the files are accessible inside the Docker container.


### Tokenizer[#](https://rocm.docs.amd.com#tokenizer)

Set the `HF_TOKEN`

environment variable with
right permissions to access the tokenizer for each model.

```
# Export your HF_TOKEN in the workspace
export HF_TOKEN=<your_hftoken>
```

## Run training[#](https://rocm.docs.amd.com#run-training)

Use the following example commands to set up the environment, configure
[key options](https://rocm.docs.amd.com/previous-versions/primus-megatron-v25.8.html#amd-primus-megatron-lm-benchmark-test-vars), and run training on
AMD Instinct GPUs using Primus with the Megatron backend.

### Single node training[#](https://rocm.docs.amd.com#single-node-training)

To run training on a single node, navigate to `/workspace/Primus`

and use the following setup command:

```
pip install -r requirements.txt
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to **Llama 3.3 70B**.
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To run pre-training for Llama 3.3 70B BF16, run:

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.3_70B.log \
-- train pretrain \
--config examples/megatron/configs/MI355X/llama3.3_70B-BF16-pretrain.yaml
```

```
# Set the variables for better performance
# only on MI325X and MI300X
export HSA_NO_SCRATCH_RECLAIM=1
export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
export NVTE_CK_IS_V3_ATOMIC_FP32=1
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.3_70B.log \
-- train pretrain \
--config examples/megatron/configs/MI300X/llama3.3_70B-BF16-pretrain.yaml
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to **Llama 3.1 8B**.
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To run pre-training for Llama 3.1 8B FP8, run:

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B_fp8.log \
-- train pretrain \
--config examples/megatron/configs/MI355X/llama3.1_8B-FP8-pretrain.yaml
```

```
# Set the variables for better performance
# only on MI325X and MI300X
export HSA_NO_SCRATCH_RECLAIM=1
export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
export NVTE_CK_IS_V3_ATOMIC_FP32=1
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B_fp8.log \
-- train pretrain \
--config examples/megatron/configs/MI300X/llama3.1_8B-FP8-pretrain.yaml
```

For Llama 3.1 8B BF16, use the following command:

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B.log \
-- train pretrain \
--config examples/megatron/configs/MI355X/llama3.1_8B-BF16-pretrain.yaml
```

```
# Set the variables for better performance
# only on MI325X and MI300X
export HSA_NO_SCRATCH_RECLAIM=1
export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
export NVTE_CK_IS_V3_ATOMIC_FP32=1
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B.log \
-- train pretrain \
--config examples/megatron/configs/MI300X/llama3.1_8B-BF16-pretrain.yaml
```

For Llama 3.1 8B MXFP8 (MI355X and MI350X only), use the following command:

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B_mxfp8.log \
-- train pretrain \
--config examples/megatron/configs/MI355X/llama3.1_8B-MXFP8-pretrain.yaml
```

For Llama 3.1 8B MXFP4 (MI355X and MI350X only), use the following command:

```
NVTE_USE_CAST_TRANSPOSE_TRITON=0 bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B_mxfp4.log \
-- train pretrain \
--config examples/megatron/configs/MI355X/llama3.1_8B-MXFP4-pretrain.yaml
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to **Llama 3.1 70B**.
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To run pre-training for Llama 3.1 70B BF16, run:

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B.log \
-- train pretrain \
--config examples/megatron/configs/MI355X/llama3.1_70B-BF16-pretrain.yaml \
--micro_batch_size 8 \
--global_batch_size 128
```

```
# Set the variables for better performance
# only on MI325X and MI300X
export HSA_NO_SCRATCH_RECLAIM=1
export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
export NVTE_CK_IS_V3_ATOMIC_FP32=1
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B.log \
-- train pretrain \
--config examples/megatron/configs/MI300X/llama3.1_70B-BF16-pretrain.yaml
```

To run the training on a single node for Llama 3.1 70B FP8, use the following command.

Note

The MI300X configuration uses a proxy model. On MI300X GPUs, use two or more nodes to run the full Llama 3.1 70B model with FP8 precision. MI355X and MI350X GPUs can support the full 70B model with FP8 precision on a single node.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B_fp8.log \
-- train pretrain \
--config examples/megatron/configs/MI355X/llama3.1_70B-FP8-pretrain.yaml
```

```
# Set the variables for better performance
# only on MI325X and MI300X
export HSA_NO_SCRATCH_RECLAIM=1
export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
export NVTE_CK_IS_V3_ATOMIC_FP32=1
bash runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B_fp8_proxy.log \
-- train pretrain \
--config examples/megatron/configs/MI300X/llama3.1_70B-FP8-pretrain.yaml \
--train_iters 50 \
--num_layers 40 \
--fp8 hybrid \
--no_fp8_weight_transpose_cache true
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to **Llama 2 7B**.
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To run pre-training for Llama 2 7B FP8, run:

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama2_7B_fp8.log \
-- train pretrain \
--config examples/megatron/configs/MI355X/llama2_7B-FP8-pretrain.yaml
```

```
# Set the variables for better performance
# only on MI325X and MI300X
export HSA_NO_SCRATCH_RECLAIM=1
export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
export NVTE_CK_IS_V3_ATOMIC_FP32=1
bash runner/primus-cli direct \
--log_file /tmp/primus_llama2_7B_fp8.log \
-- train pretrain \
--config examples/megatron/configs/MI300X/llama2_7B-FP8-pretrain.yaml
```

To run pre-training for Llama 2 7B BF16, run:

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama2_7B.log \
-- train pretrain \
--config examples/megatron/configs/MI355X/llama2_7B-BF16-pretrain.yaml
```

```
# Set the variables for better performance
# only on MI325X and MI300X
export HSA_NO_SCRATCH_RECLAIM=1
export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
export NVTE_CK_IS_V3_ATOMIC_FP32=1
bash runner/primus-cli direct \
--log_file /tmp/primus_llama2_7B.log \
-- train pretrain \
--config examples/megatron/configs/MI300X/llama2_7B-BF16-pretrain.yaml
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to **Llama 2 70B**.
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To run pre-training for Llama 2 70B BF16, run:

```
bash runner/primus-cli direct \
--log_file /tmp/primus_llama2_70B.log \
-- train pretrain \
--config examples/megatron/configs/MI355X/llama2_70B-BF16-pretrain.yaml
```

```
# Set the variables for better performance
# only on MI325X and MI300X
export HSA_NO_SCRATCH_RECLAIM=1
export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
export NVTE_CK_IS_V3_ATOMIC_FP32=1
bash runner/primus-cli direct \
--log_file /tmp/primus_llama2_70B.log \
-- train pretrain \
--config examples/megatron/configs/MI300X/llama2_70B-BF16-pretrain.yaml
```

Only multi-node training configurations are currently available for Llama 3.1 405B.
See the
[multi-node training examples](https://rocm.docs.amd.com#amd-primus-megatron-multi-node-examples-v26-4)
for training instructions.

Once setup is complete, run the appropriate training command.
The following run commands are tailored to **DeepSeek-V2-Lite**.
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To run training on a single node for DeepSeek-V2-Lite (MoE with expert parallel) BF16, use the following command:

```
bash runner/primus-cli direct \
--log_file /tmp/primus_deepseek_v2_lite.log \
-- train pretrain \
--config examples/megatron/configs//MI355X/deepseek_v2_lite-BF16-pretrain.yaml \
--use_turbo_grouped_mlp False \
--moe_use_legacy_grouped_gemm True \
--moe_use_fused_router_with_aux_score True \
--moe_permute_fusion True
```

```
# Set the variables for better performance
# only on MI325X and MI300X
export HSA_NO_SCRATCH_RECLAIM=1
export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
export NVTE_CK_IS_V3_ATOMIC_FP32=1
bash runner/primus-cli direct \
--log_file /tmp/primus_deepseek_v2_lite.log \
-- train pretrain \
--config examples/megatron/configs/MI300X/deepseek_v2_lite-BF16-pretrain.yaml
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to **Mixtral 8x7B**.
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To run training on a single node for Mixtral 8x7B (MoE with expert parallel), use the following command:

```
bash runner/primus-cli direct \
--log_file /tmp/primus_mixtral_8x7B.log \
-- train pretrain \
--config examples/megatron/configs/MI355X/mixtral_8x7B_v0.1-BF16-pretrain.yaml
```

```
# Set the variables for better performance
# only on MI325X and MI300X
export HSA_NO_SCRATCH_RECLAIM=1
export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
export NVTE_CK_IS_V3_ATOMIC_FP32=1
bash runner/primus-cli direct \
--log_file /tmp/primus_mixtral_8x7B.log \
-- train pretrain \
--config examples/megatron/configs/MI300X/mixtral_8x7B_v0.1-BF16-pretrain.yaml
```

Only multi-node training configurations are currently available for Mixtral 8x22B.
See the
[multi-node training examples](https://rocm.docs.amd.com#amd-primus-megatron-multi-node-examples-v26-4)
for training instructions.

Once setup is complete, run the appropriate training command.
The following run commands are tailored to post-training **Qwen 3 32B** (LoRA).
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To run training on a single node for Qwen 3 32B BF16 (SFT), use the following command:

```
bash runner/primus-cli direct \
--log_file /tmp/primus_qwen3_32b_lora.log \
-- train posttrain \
--config examples/megatron_bridge/configs/MI355X/qwen3_32b_lora_posttrain.yaml
```

```
# Set the variables for better performance
# only on MI325X and MI300X
export HSA_NO_SCRATCH_RECLAIM=1
export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
export NVTE_CK_IS_V3_ATOMIC_FP32=1
bash runner/primus-cli direct \
--log_file /tmp/primus_qwen3_32b.log \
-- train posttrain \
--config examples/megatron_bridge/configs/MI300X/qwen3_32b_lora_posttrain.yaml
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to post-training **Qwen 3 32B** (SFT).
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To run training on a single node for Qwen 3 32B BF16 (SFT), use the following command:

```
bash runner/primus-cli direct \
--log_file /tmp/primus_qwen3_32b_sft.log \
-- train posttrain \
--config examples/megatron_bridge/configs/MI355X/qwen3_32b_sft_posttrain.yaml
```

```
# Set the variables for better performance
# only on MI325X and MI300X
export HSA_NO_SCRATCH_RECLAIM=1
export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
export NVTE_CK_IS_V3_ATOMIC_FP32=1
bash runner/primus-cli direct \
--log_file /tmp/primus_qwen3_32b_sft.log \
-- train posttrain \
--config examples/megatron_bridge/configs/MI300X/qwen3_32b_sft_posttrain.yaml
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to **Qwen 2.5 7B**.
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To run training on a single node for Qwen 2.5 7B BF16, use the following command:

```
bash runner/primus-cli direct \
--log_file /tmp/primus_qwen2.5_7B.log \
-- train pretrain \
--config examples/megatron/configs/MI355X/qwen2.5_7B-BF16-pretrain.yaml
```

```
# Set the variables for better performance
# only on MI325X and MI300X
export HSA_NO_SCRATCH_RECLAIM=1
export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
export NVTE_CK_IS_V3_ATOMIC_FP32=1
bash runner/primus-cli direct \
--log_file /tmp/primus_qwen2.5_7B.log \
-- train pretrain \
--config examples/megatron/configs/MI300X/qwen2.5_7B-BF16-pretrain.yaml
```

For FP8, use the following command.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_qwen2.5_7B_fp8.log \
-- train pretrain \
--config examples/megatron/configs/MI355X/qwen2.5_7B-FP8-pretrain.yaml
```

```
# Set the variables for better performance
# only on MI325X and MI300X
export HSA_NO_SCRATCH_RECLAIM=1
export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
export NVTE_CK_IS_V3_ATOMIC_FP32=1
bash runner/primus-cli direct \
--log_file /tmp/primus_qwen2.5_7B_fp8.log \
-- train pretrain \
--config examples/megatron/configs/MI300X/qwen2.5_7B-FP8-pretrain.yaml
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to **Qwen 2.5 72B**.
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To run the training on a single node for Qwen 2.5 72B BF16, use the following command.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_qwen2.5_72B.log \
-- train pretrain \
--config examples/megatron/configs/MI355X/qwen2.5_72B-BF16-pretrain.yaml
```

```
# Set the variables for better performance
# only on MI325X and MI300X
export HSA_NO_SCRATCH_RECLAIM=1
export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
export NVTE_CK_IS_V3_ATOMIC_FP32=1
bash runner/primus-cli direct \
--log_file /tmp/primus_qwen2.5_72B.log \
-- train pretrain \
--config examples/megatron/configs/MI300X/qwen2.5_72B-BF16-pretrain.yaml
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to **Zebra-Llama 1B**.
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To run the training on a single node for AMD Zebra-Llama 1B BF16, use the following command.

```
PRIMUS_TRAIN_RUNTIME=legacy bash runner/primus-cli direct \
--log_file /tmp/primus_zebra_llama_1B.log \
-- train pretrain \
--config examples/megatron/configs/MI355X/zebra_llama_1B-pretrain.yaml
```

```
# Set the variables for better performance
# only on MI325X and MI300X
export HSA_NO_SCRATCH_RECLAIM=1
export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
export NVTE_CK_IS_V3_ATOMIC_FP32=1
PRIMUS_TRAIN_RUNTIME=legacy bash runner/primus-cli direct \
--log_file /tmp/primus_zebra_llama_1B.log \
-- train pretrain \
--config examples/megatron/configs/MI300X/zebra_llama_1B-pretrain.yaml
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to **Zebra-Llama 3B**.
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To run the training on a single node for AMD Zebra-Llama 3B BF16, use the following command.

```
PRIMUS_TRAIN_RUNTIME=legacy bash runner/primus-cli direct \
--log_file /tmp/primus_zebra_llama_3B.log \
-- train pretrain \
--config examples/megatron/configs/MI355X/zebra_llama_3B-pretrain.yaml
```

```
# Set the variables for better performance
# only on MI325X and MI300X
export HSA_NO_SCRATCH_RECLAIM=1
export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
export NVTE_CK_IS_V3_ATOMIC_FP32=1
PRIMUS_TRAIN_RUNTIME=legacy bash runner/primus-cli direct \
--log_file /tmp/primus_zebra_llama_3B.log \
-- train pretrain \
--config examples/megatron/configs/MI300X/zebra_llama_3B-pretrain.yaml
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to **Zebra Llama 8B**.
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To run the training on a single node for AMD Zebra-Llama 8B BF16, use the following command.

```
PRIMUS_TRAIN_RUNTIME=legacy bash runner/primus-cli direct \
--log_file /tmp/primus_zebra_llama_8B.log \
-- train pretrain \
--config examples/megatron/configs/MI355X/zebra_llama_8B-pretrain.yaml
```

```
# Set the variables for better performance
# only on MI325X and MI300X
export HSA_NO_SCRATCH_RECLAIM=1
export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
export NVTE_CK_IS_V3_ATOMIC_FP32=1
PRIMUS_TRAIN_RUNTIME=legacy bash runner/primus-cli direct \
--log_file /tmp/primus_zebra_llama_8B.log \
-- train pretrain \
--config examples/megatron/configs/MI300X/zebra_llama_8B-pretrain.yaml
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to **Qwen 3 30B (A3B)**.
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To run training on a single node for Qwen 3 30B (A3B) BF16, use the following command:

```
bash runner/primus-cli direct \
--log_file /tmp/primus_qwen3_30B_A3B.log \
-- train pretrain \
--config examples/megatron/configs/MI355X/qwen3_30B_A3B-BF16-pretrain.yaml
```

```
# Set the variables for better performance
# only on MI325X and MI300X
export HSA_NO_SCRATCH_RECLAIM=1
export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
export NVTE_CK_IS_V3_ATOMIC_FP32=1
bash runner/primus-cli direct \
--log_file /tmp/primus_qwen3_30B_A3B.log \
-- train pretrain \
--config examples/megatron/configs/MI300X/qwen3_30B_A3B-BF16-pretrain.yaml
```

For FP8, use the following command.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_qwen3_30B_A3B_fp8.log \
-- train pretrain \
--config examples/megatron/configs/MI355X/qwen3_30B_A3B-FP8-pretrain.yaml
```

```
# Set the variables for better performance
# only on MI325X and MI300X
export HSA_NO_SCRATCH_RECLAIM=1
export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
export NVTE_CK_IS_V3_ATOMIC_FP32=1
bash runner/primus-cli direct \
--log_file /tmp/primus_qwen3_30B_A3B_fp8.log \
-- train pretrain \
--config examples/megatron/configs/MI300X/qwen3_30B_A3B-FP8-pretrain.yaml
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to **Qwen3 235B (A22B)**.
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To run training on a single node for Qwen3 235B (A22B) BF16, use the following command:

```
bash runner/primus-cli direct \
--log_file /tmp/primus_qwen3_235B_A22B.log \
-- train pretrain \
--config examples/megatron/configs/MI355X/qwen3_235B_A22B-BF16-pretrain.yaml
```

```
# Set the variables for better performance
# only on MI325X and MI300X
export HSA_NO_SCRATCH_RECLAIM=1
export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
export NVTE_CK_IS_V3_ATOMIC_FP32=1
bash runner/primus-cli direct \
--log_file /tmp/primus_qwen3_235B_A22B.log \
-- train pretrain \
--config examples/megatron/configs/MI300X/qwen3_235B_A22B-BF16-pretrain.yaml
```

For FP8, use the following command.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_qwen3_235B_A22B_fp8.log \
-- train pretrain \
--config examples/megatron/configs/MI355X/qwen3_235B_A22B-FP8-pretrain.yaml
```

```
# Set the variables for better performance
# only on MI325X and MI300X
export HSA_NO_SCRATCH_RECLAIM=1
export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
export NVTE_CK_IS_V3_ATOMIC_FP32=1
bash runner/primus-cli direct \
--log_file /tmp/primus_qwen3_235B_A22B_fp8.log \
-- train pretrain \
--config examples/megatron/configs/MI300X/qwen3_235B_A22B-FP8-pretrain.yaml
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to **GPT-OSS-20B**.
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To run training on a single node for GPT-OSS-20B BF16, use the following command:

```
bash runner/primus-cli direct \
--log_file /tmp/primus_gpt_oss_20B.log \
-- train pretrain \
--config examples/megatron/configs/MI355X/gpt_oss_20B-BF16-pretrain.yaml
```

```
# Set the variables for better performance
# only on MI325X and MI300X
export HSA_NO_SCRATCH_RECLAIM=1
export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
export NVTE_CK_IS_V3_ATOMIC_FP32=1
bash runner/primus-cli direct \
--log_file /tmp/primus_gpt_oss_20B.log \
-- train pretrain \
--config examples/megatron/configs/MI300X/gpt_oss_20B-BF16-pretrain.yaml
```

For FP8, use the following command.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_gpt_oss_20B_fp8.log \
-- train pretrain \
--config examples/megatron/configs/MI355X/gpt_oss_20B-FP8-pretrain.yaml
```

```
# Set the variables for better performance
# only on MI325X and MI300X
export HSA_NO_SCRATCH_RECLAIM=1
export PRIMUS_TURBO_ATTN_V3_ATOMIC_FP32=1
export NVTE_CK_IS_V3_ATOMIC_FP32=1
bash runner/primus-cli direct \
--log_file /tmp/primus_gpt_oss_20B_fp8.log \
-- train pretrain \
--config examples/megatron/configs/MI300X/gpt_oss_20B-FP8-pretrain.yaml
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to **GPT-OSS-120B**.
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

Note

GPT-OSS-120B is supported on MI355X and MI350X only.

To run training on a single node for GPT-OSS-120B BF16, use the following command:

```
bash runner/primus-cli direct \
--log_file /tmp/primus_gpt_oss_120B.log \
-- train pretrain \
--config examples/megatron/configs/MI355X/gpt_oss_120B-BF16-pretrain.yaml
```

For FP8, use the following command.

```
bash runner/primus-cli direct \
--log_file /tmp/primus_gpt_oss_120B_fp8.log \
-- train pretrain \
--config examples/megatron/configs/MI355X/gpt_oss_120B-FP8-pretrain.yaml
```

### Multi-node training examples[#](https://rocm.docs.amd.com#multi-node-training-examples)

Refer to [Multi-node setup for AI workloads](https://rocm.docs.amd.com/system-setup/multi-node-setup.html) to configure your environment for multi-node
training.

To run training on multiple nodes, you can use `primus-cli`

(recommended) or the
[run_slurm_pretrain.sh](https://github.com/AMD-AGI/Primus/blob/main/examples/run_slurm_pretrain.sh)
script to launch multi-node workloads. Use the following steps to set up your environment:

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
export HSA_NO_SCRATCH_RECLAIM=1
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
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To train Llama 3.1 8B FP8 on 8 nodes, run:

```
# Adjust the training parameters.
# For example, `global_batch_size: 8 * #single_node_bs` for 8 nodes in this case.
NNODES=8 EXP=examples/megatron/configs/MI300X/llama3.1_8B-FP8-pretrain.yaml \
bash ./examples/run_slurm_pretrain.sh --global_batch_size 1024
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to **Llama 2 7B**.
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To train Llama 2 7B FP8 on 8 nodes, run:

```
# Adjust the training parameters.
# For example, `global_batch_size: 8 * #single_node_bs` for 8 nodes in this case.
NNODES=8 EXP=examples/megatron/configs/MI300X/llama2_7B-FP8-pretrain.yaml \
bash ./examples/run_slurm_pretrain.sh --global_batch_size 2048
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to **Llama 3.1 70B**.
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To train Llama 3.1 70B FP8 on 8 nodes, run:

```
NNODES=8 EXP=examples/megatron/configs/MI300X/llama3.1_70B-FP8-pretrain.yaml \
bash examples/run_slurm_pretrain.sh \
--micro_batch_size 4 --global_batch_size 256 --recompute_num_layers 80
```

To train Llama 3.1 70B BF16 on 8 nodes, run:

```
NNODES=8 EXP=examples/megatron/configs/MI300X/llama3.1_70B-BF16-pretrain.yaml \
bash examples/run_slurm_pretrain.sh \
--micro_batch_size 1 --global_batch_size 256 --recompute_num_layers 12
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to **Llama 2 70B**.
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To train Llama 2 70B FP8 on 8 nodes, run:

```
NNODES=8 EXP=examples/megatron/configs/MI300X/llama2_70B-FP8-pretrain.yaml \
bash examples/run_slurm_pretrain.sh \
--micro_batch_size 10 --global_batch_size 640 --recompute_num_layers 80
```

To train Llama 2 70B BF16 on 8 nodes, run:

```
NNODES=8 EXP=examples/megatron/configs/MI300X/llama2_70B-BF16-pretrain.yaml \
bash ./examples/run_slurm_pretrain.sh \
--micro_batch_size 2 --global_batch_size 1536 --recompute_num_layers 12
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to **Llama 3.3 70B**.
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To train Llama 3.3 70B FP8 on 8 nodes, run:

```
NNODES=8 EXP=examples/megatron/configs/MI300X/llama3.3_70B-FP8-pretrain.yaml \
bash examples/run_slurm_pretrain.sh \
--micro_batch_size 4 --global_batch_size 256 --recompute_num_layers 80
```

To train Llama 3.3 70B BF16 on 8 nodes, run:

```
NNODES=8 EXP=examples/megatron/configs/MI300X/llama3.3_70B-BF16-pretrain.yaml \
bash examples/run_slurm_pretrain.sh \
--micro_batch_size 1 --global_batch_size 256 --recompute_num_layers 12
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to **Mixtral 8x7B**.
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To train Mixtral 8x7B BF16 on 8 nodes, run:

```
NNODES=8 EXP=examples/megatron/configs/MI300X/mixtral_8x7B_v0.1-BF16-pretrain.yaml \
bash examples/run_slurm_pretrain.sh \
--micro_batch_size 2 --global_batch_size 256
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to Mixtral 8x22B.
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To train Mixtral 8x22B BF16 on 4 nodes using `primus-cli`

(recommended), run:

```
# In the Primus directory
./primus-cli slurm srun -N 4 -- train pretrain \
--config examples/megatron/configs/MI355X/mixtral_8x22B_v0.1-BF16-pretrain.yaml \
--micro_batch_size 1 \
--global_batch_size 512 \
--num_virtual_stages_per_pipeline_rank 2 \
--pipeline_model_parallel_size 4 \
--expert_model_parallel_size 8 \
--recompute_num_layers 1 \
--moe_use_legacy_grouped_gemm True \
--gradient_accumulation_fusion True
```

Alternatively, using the legacy script:

```
NNODES=4 EXP=examples/megatron/configs/MI355X/mixtral_8x22B_v0.1-BF16-pretrain.yaml \
bash examples/run_slurm_pretrain.sh \
--micro_batch_size 1 \
--global_batch_size 512 \
--num_virtual_stages_per_pipeline_rank 2 \
--pipeline_model_parallel_size 4 \
--expert_model_parallel_size 8 \
--recompute_num_layers 1 \
--moe_use_legacy_grouped_gemm True \
--gradient_accumulation_fusion True
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to **Qwen 2.5 72B**.
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To train Qwen 2.5 72B FP8 on 8 nodes, run:

```
NNODES=8 EXP=examples/megatron/configs/MI300X/qwen2.5_72B-FP8-pretrain.yaml \
bash examples/run_slurm_pretrain.sh \
--micro_batch_size 8 --global_batch_size 512 --recompute_num_layers 80
```

Once setup is complete, run the appropriate training command.
The following run commands are tailored to Llama 3.1 405B.
See [Supported models](https://rocm.docs.amd.com#amd-primus-megatron-lm-model-support-v26-4) to switch to another available model.

To train Llama 3.1 405B FP8 on 8 nodes using `primus-cli`

(recommended), run:

```
# In the Primus directory
# TP=8 is used for Llama 3.1 405B on 8 nodes. The model has 126 layers which is not
# divisible by 8, so decoder_first_pipeline_num_layers and
# decoder_last_pipeline_num_layers must be set explicitly.
./primus-cli slurm srun -N 8 -- train pretrain \
--config examples/megatron/configs/MI325X/llama3.1_405B-FP8-pretrain.yaml \
--micro_batch_size 1 \
--global_batch_size 256 \
--decoder_first_pipeline_num_layers 15 \
--decoder_last_pipeline_num_layers 15
```

Alternatively, using the legacy script:

```
NNODES=8 EXP=examples/megatron/configs/MI300X/llama3.1_405B-FP8-pretrain.yaml \
bash examples/run_slurm_pretrain.sh \
--micro_batch_size 1 \
--global_batch_size 256 \
--decoder_first_pipeline_num_layers 15 \
--decoder_last_pipeline_num_layers 15
```

Multi-node training instructions are not currently available for DeepSeek-V2-Lite.

Multi-node training instructions are not currently available for Zebra-Llama 1B.

Multi-node training instructions are not currently available for Zebra-Llama 3B.

Multi-node training instructions are not currently available for Zebra-Llama 8B.

Multi-node training instructions are not currently available for GPT-OSS-20B.

Multi-node training instructions are not currently available for GPT-OSS-120B.

Multi-node training instructions are not currently available for Qwen 3 32B SFT.

Multi-node training instructions are not currently available for Qwen 3 32B LoRA.

Multi-node training instructions are not currently available for Qwen 3 30B A3B.

Multi-node training instructions are not currently available for Qwen 2.5 7B.

Multi-node training instructions are not currently available for Qwen3 235B (A22B).

### Key options[#](https://rocm.docs.amd.com#key-options)

The following are key options to take note of

- fp8
`hybrid`

enables FP8 GEMMs.- use_torch_fsdp2
`use_torch_fsdp2: 1`

enables torch fsdp-v2. If FSDP is enabled, set`use_distributed_optimizer`

and`overlap_param_gather`

to`false`

.- profile
To enable PyTorch profiling, set these parameters:

profile: true use_pytorch_profiler: true profile_step_end: 7 profile_step_start: 6

- train_iters
The total number of iterations (default: 50).

- mock_data
True by default.

- micro_batch_size
Micro batch size.

- global_batch_size
Global batch size.

- recompute_granularity
For activation checkpointing.

- num_layers
For using a reduced number of layers as with proxy models.


## Further reading[#](https://rocm.docs.amd.com#further-reading)

For an introduction to Primus, see

[Primus: A Lightweight, Unified Training Framework for Large Models on AMD GPUs](https://rocm.blogs.amd.com/software-tools-optimization/primus/README.html).To learn more about system settings and management practices to configure your system for AMD Instinct MI300X Series GPUs, see

[AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html).For a list of other ready-made Docker images for AI with ROCm, see

[AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models).

## Previous versions[#](https://rocm.docs.amd.com#previous-versions)

See [Megatron-LM training performance testing version history](https://rocm.docs.amd.com/previous-versions/megatron-lm-history.html) to find documentation for previous releases
of the Primus with Megatron-LM training recipe.