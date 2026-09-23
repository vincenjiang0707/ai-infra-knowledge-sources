source: https://docs.vllm.ai/projects/recipes/en/stable/Qwen/Qwen3-Next.html
lastmod: 2026-04-27

# Qwen3-Next Usage Guide[¶](https://docs.vllm.ai#qwen3-next-usage-guide)

[Qwen3-Next](https://qwen.ai/blog?id=4074cca80393150c248e508aa62983f9cb7d27cd&from=research.latest-advancements-list) is an advanced large language model created by the Qwen team from Alibaba Cloud. It features several key improvements:

- A hybrid attention mechanism
- A highly sparse Mixture-of-Experts (MoE) structure
- Training-stability-friendly optimizations
- A multi-token prediction mechanism for faster inference

## Installing vLLM[¶](https://docs.vllm.ai#installing-vllm)

## Launching Qwen3-Next with vLLM[¶](https://docs.vllm.ai#launching-qwen3-next-with-vllm)

You can use 4x H200/H20 or 4x A100/A800 GPUs to launch this model.

### Basic Multi-GPU Setup[¶](https://docs.vllm.ai#basic-multi-gpu-setup)

vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct \
--tensor-parallel-size 4 \
--served-model-name qwen3-next \
--enable-prefix-caching


If you encounter `torch.AcceleratorError: CUDA error: an illegal memory access was encountered`

, you can add `--compilation_config.cudagraph_mode=PIECEWISE`

to the startup parameters to resolve this issue. This IMA error may occur in Data Parallel (DP) mode.

### For FP8 model[¶](https://docs.vllm.ai#for-fp8-model)

For SM90/SM100 machines:

vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 \
--tensor-parallel-size 4 \
--enable-prefix-caching


We can accelerate the performance on SM100 machines using the FP8 FlashInfer TRTLLM MoE kernel.

VLLM_USE_FLASHINFER_MOE_FP8=1 \
VLLM_FLASHINFER_MOE_BACKEND=latency \
VLLM_USE_DEEP_GEMM=0 \
VLLM_USE_TRTLLM_ATTENTION=0 \
VLLM_ATTENTION_BACKEND=FLASH_ATTN \
vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 \
--tensor-parallel-size 4


### Advanced Configuration with MTP[¶](https://docs.vllm.ai#advanced-configuration-with-mtp)

`Qwen3-Next`

also supports Multi-Token Prediction (MTP in short), you can launch the model server with the following arguments to enable MTP.

vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct \
--tokenizer-mode auto --gpu-memory-utilization 0.8 \
--speculative-config '{"method": "qwen3_next_mtp", "num_speculative_tokens": 2}' \
--tensor-parallel-size 4 --no-enable-chunked-prefill


The `speculative-config`

argument configures speculative decoding settings using a JSON format. The method "qwen3_next_mtp" specifies that the system should use Qwen3-Next's specialized multi-token prediction method. The `"num_speculative_tokens": 2`

setting means the model will speculate 2 tokens ahead during generation.

## Performance Metrics[¶](https://docs.vllm.ai#performance-metrics)

### Benchmarking[¶](https://docs.vllm.ai#benchmarking)

We use the following script to demonstrate how to benchmark `Qwen/Qwen3-Next-80B-A3B-Instruct`

.

vllm bench serve \
--backend vllm \
--model Qwen/Qwen3-Next-80B-A3B-Instruct \
--served-model-name qwen3-next \
--endpoint /v1/completions \
--dataset-name random \
--random-input 2048 \
--random-output 1024 \
--max-concurrency 10 \
--num-prompt 100


## Usage Tips[¶](https://docs.vllm.ai#usage-tips)

### Tune MoE kernel[¶](https://docs.vllm.ai#tune-moe-kernel)

When starting the model service, you may encounter the following warning in the server log(Suppose the GPU is `NVIDIA_H20-3e`

):

(VllmWorker TP2 pid=47571) WARNING 09-09 15:47:25 [fused_moe.py:727] Using default MoE config. Performance might be sub-optimal! Config file not found at ['/vllm_path/vllm/model_executor/layers/fused_moe/configs/E=512,N=128,device_name=NVIDIA_H20-3e.json']


You can use [benchmark_moe](https://github.com/vllm-project/vllm/blob/main/benchmarks/kernels/benchmark_moe.py) to perform MoE Triton kernel tuning for your hardware. Once tuning is complete, a JSON file with a name like `E=512,N=128,device_name=NVIDIA_H20-3e.json`

will be generated. You can specify the directory containing this file for your deployment hardware using the environment variable `VLLM_TUNED_CONFIG_FOLDER`

, like:

VLLM_TUNED_CONFIG_FOLDER=your_moe_tuned_dir vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct \
--tensor-parallel-size 4 \
--served-model-name qwen3-next


You should see the following information printed in the server log. This indicates that the tuned MoE configuration has been loaded, which will improve the model service performance.

(VllmWorker TP2 pid=60498) INFO 09-09 16:23:07 [fused_moe.py:720] Using configuration from /your_moe_tuned_dir/E=512,N=128,device_name=NVIDIA_H20-3e.json for MoE layer.


### Data Parallel Deployment[¶](https://docs.vllm.ai#data-parallel-deployment)

vLLM supports multi-parallel groups. You can refer to [Data Parallel Deployment documentation](https://docs.vllm.ai/en/latest/serving/data_parallel_deployment.html) and try parallel combinations that are more suitable for this model.

### Function calling[¶](https://docs.vllm.ai#function-calling)

vLLM also supports calling user-defined functions. Make sure to run your Qwen3-Next models with the following arguments.

## AMD GPU Support[¶](https://docs.vllm.ai#amd-gpu-support)

Recommended approaches by hardware type are:

MI300X/MI325X/MI355X

Please follow the steps here to install and run Qwen3-Next models on AMD MI300X/MI325X/MI355X GPU.

### Step 1: Installing vLLM (AMD ROCm Backend: MI300X, MI325X, MI355X)[¶](https://docs.vllm.ai#step-1-installing-vllm-amd-rocm-backend-mi300x-mi325x-mi355x)

Note: The vLLM wheel for ROCm requires Python 3.12, ROCm 7.0, and glibc >= 2.35. If your environment does not meet these requirements, please use the Docker-based setup as described in the

[documentation].


### Step 2: Start the vLLM server[¶](https://docs.vllm.ai#step-2-start-the-vllm-server)

Run the vllm online serving

SAFETENSORS_FAST_GPU=1 \
VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 \
vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct \
--tensor-parallel-size 4 \
--max-model-len 32768 \
--no-enable-prefix-caching \
--trust-remote-code


### Step 3: Run Benchmark[¶](https://docs.vllm.ai#step-3-run-benchmark)

Open a new terminal and run the following command to execute the benchmark script inside the container.