source: https://docs.vllm.ai/projects/recipes/en/stable/Qwen/Qwen2.5-VL.html
lastmod: 2026-04-27

# Qwen2.5-VL Usage Guide[¶](https://docs.vllm.ai#qwen25-vl-usage-guide)

This guide describes how to run Qwen2.5-VL series on the targeted accelerated stack. Since BF16 is the commonly used precision type for Qwen2.5-VL training, using BF16 in inference ensures the best accuracy.

## TPU Deployment[¶](https://docs.vllm.ai#tpu-deployment)

## GPU Deployment[¶](https://docs.vllm.ai#gpu-deployment)

### Installing vLLM[¶](https://docs.vllm.ai#installing-vllm)

Note: The vLLM wheel for ROCm requires Python 3.12, ROCm 7.0, and glibc >= 2.35. If your environment does not meet these requirements, please use the Docker-based setup as described in the

[documentation].

### Running Qwen2.5-VL-72B with BF16[¶](https://docs.vllm.ai#running-qwen25-vl-72b-with-bf16)

There are two ways to parallelize the model over multiple GPUs: (1) Tensor-parallel (TP) or (2) Data-parallel (DP). Each one has its own advantages, where tensor-parallel is usually more beneficial for low-latency / low-load scenarios, and data-parallel works better for cases where there is a lot of data with heavy loads.

To launch the online inference server for Qwen2.5-VL-72B:

#### Tips[¶](https://docs.vllm.ai#tips)

- You can set
`--max-model-len`

to preserve memory. By default the model's context length is 128K, but`--max-model-len=65536`

is usually good for most scenarios. - You can set
`--tensor-parallel-size`

and`--data-parallel-size`

to adjust the parallel strategy. But TP should be larger than 2 for A100-80GB devices to avoid OOM. - You can set
`--limit-mm-per-prompt`

to limit how many multimodal data instances to allow for each prompt. This is useful if you want to control the incoming traffic of multimodal requests. `--mm-encoder-tp-mode`

is set to "data", so as to deploy the multimodal encoder in DP fashion for better performance. This is because the multimodal encoder is very small compared to the language decoder (ViT 675M v.s. LM 72B in Qwen2.5-VL-72B), thus TP on ViT provides little gain but incurs significant communication overhead.- vLLM conservatively uses 90% of GPU memory. You can set
`--gpu-memory-utilization=0.95`

to maximize KVCache.

For medium-size models like Qwen2.5-VL-7B, data parallelism usually provides better performance since it boosts throughput without the heavy communication costs seen in tensor parallelism. Here is an example of how to launch the server using DP=4:

### Qwen2.5-VL-7B-Instruct with DP=4[¶](https://docs.vllm.ai#qwen25-vl-7b-instruct-with-dp4)

### Benchmarking[¶](https://docs.vllm.ai#benchmarking)

For benchmarking, you first need to launch the server with prefix caching disabled by adding `--no-enable-prefix-caching`

to the server command.

#### Qwen2.5VL-72B Benchmark on VisionArena-Chat Dataset[¶](https://docs.vllm.ai#qwen25vl-72b-benchmark-on-visionarena-chat-dataset)

Once the server for the 72B model is running, open another terminal and run the benchmark client:

vllm bench serve \
--host 0.0.0.0 \
--port 8000 \
--backend openai-chat \
--endpoint /v1/chat/completions \
--model Qwen/Qwen2.5-VL-72B-Instruct \
--dataset-name hf \
--dataset-path lmarena-ai/VisionArena-Chat \
--num-prompts 128


- Test different batch sizes by changing
`--num-prompts`

, e.g., 1, 16, 32, 64, 128, 256, 512

##### Expected Output[¶](https://docs.vllm.ai#expected-output)

============ Serving Benchmark Result ============
Successful requests: 128
Benchmark duration (s): 33.40
Total input tokens: 9653
Total generated tokens: 14611
Request throughput (req/s): 3.83
Output token throughput (tok/s): 437.46
Total Token throughput (tok/s): 726.48
---------------Time to First Token----------------
Mean TTFT (ms): 13715.73
Median TTFT (ms): 13254.17
P99 TTFT (ms): 26364.39
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms): 171.89
Median TPOT (ms): 157.20
P99 TPOT (ms): 504.86
---------------Inter-token Latency----------------
Mean ITL (ms): 150.41
Median ITL (ms): 56.96
P99 ITL (ms): 614.47
==================================================


#### Qwen2.5VL-72B Benchmark on Random Synthetic Dataset[¶](https://docs.vllm.ai#qwen25vl-72b-benchmark-on-random-synthetic-dataset)

Once the server for the 72B model is running, open another terminal and run the benchmark client:

vllm bench serve \
--host 0.0.0.0 \
--port 8000 \
--model Qwen/Qwen2.5-VL-72B-Instruct \
--dataset-name random \
--random-input-len 8000 \
--random-output-len 1000 \
--num-prompts 128


- Test different workloads by adjusting input/output lengths via the
`--random-input-len`

and`--random-output-len`

arguments: **Prompt-heavy**: 8000 input / 1000 output**Decode-heavy**: 1000 input / 8000 output-
**Balanced**: 1000 input / 1000 output -
Test different batch sizes by changing

`--num-prompts`

, e.g., 1, 16, 32, 64, 128, 256, 512

##### Expected Output[¶](https://docs.vllm.ai#expected-output_1)

============ Serving Benchmark Result ============
Successful requests: 128
Benchmark duration (s): 778.74
Total input tokens: 1023598
Total generated tokens: 114351
Request throughput (req/s): 0.16
Output token throughput (tok/s): 146.84
Total Token throughput (tok/s): 1461.27
---------------Time to First Token----------------
Mean TTFT (ms): 305503.01
Median TTFT (ms): 371429.33
P99 TTFT (ms): 730584.33
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms): 308.99
Median TPOT (ms): 337.48
P99 TPOT (ms): 542.26
---------------Inter-token Latency----------------
Mean ITL (ms): 297.63
Median ITL (ms): 60.91
P99 ITL (ms): 558.30
==================================================


#### Qwen2.5VL-7B Benchmark on VisionArena-Chat Dataset[¶](https://docs.vllm.ai#qwen25vl-7b-benchmark-on-visionarena-chat-dataset)

Once the server for the 7B model is running, open another terminal and run the benchmark client:

vllm bench serve \
--host 0.0.0.0 \
--port 8000 \
--backend openai-chat \
--endpoint /v1/chat/completions \
--model Qwen/Qwen2.5-VL-7B-Instruct \
--dataset-name hf \
--dataset-path lmarena-ai/VisionArena-Chat \
--num-prompts 128


##### Expected Output[¶](https://docs.vllm.ai#expected-output_2)

============ Serving Benchmark Result ============
Successful requests: 128
Benchmark duration (s): 9.78
Total input tokens: 9653
Total generated tokens: 14227
Request throughput (req/s): 13.09
Output token throughput (tok/s): 1455.11
Total Token throughput (tok/s): 2442.40
---------------Time to First Token----------------
Mean TTFT (ms): 4432.91
Median TTFT (ms): 4751.45
P99 TTFT (ms): 7575.37
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms): 58.19
Median TPOT (ms): 45.30
P99 TPOT (ms): 354.21
---------------Inter-token Latency----------------
Mean ITL (ms): 43.86
Median ITL (ms): 17.22
P99 ITL (ms): 653.85
==================================================


#### Qwen2.5VL-7B Benchmark on Random Synthetic Dataset[¶](https://docs.vllm.ai#qwen25vl-7b-benchmark-on-random-synthetic-dataset)

Once the server for the 7B model is running, open another terminal and run the benchmark client:

vllm bench serve \
--host 0.0.0.0 \
--port 8000 \
--model Qwen/Qwen2.5-VL-7B-Instruct \
--dataset-name random \
--random-input-len 8000 \
--random-output-len 1000 \
--num-prompts 128


##### Expected Output[¶](https://docs.vllm.ai#expected-output_3)

============ Serving Benchmark Result ============
Successful requests: 128
Benchmark duration (s): 45.30
Total input tokens: 1023598
Total generated tokens: 116924
Request throughput (req/s): 2.83
Output token throughput (tok/s): 2581.01
Total Token throughput (tok/s): 25176.17
---------------Time to First Token----------------
Mean TTFT (ms): 10940.59
Median TTFT (ms): 10560.30
P99 TTFT (ms): 21984.26
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms): 41.64
Median TPOT (ms): 34.41
P99 TPOT (ms): 177.58
---------------Inter-token Latency----------------
Mean ITL (ms): 33.60
Median ITL (ms): 23.14
P99 ITL (ms): 196.22
==================================================