# tensorrt-edge-llm-completes-the-mlperf-edge-agentic-benchmark-6-4x-faster-on-jetson-agx-thor

source: https://developer.nvidia.com/blog/tensorrt-edge-llm-completes-the-mlperf-edge-agentic-benchmark-6-4x-faster-on-jetson-agx-thor/

AI agents are moving from cloud data centers to vehicles, robots, and other edge devices. Unlike a chatbot that answers a single prompt, an agent works through a sequence of steps. It selects tools, evaluates their results, and continues reasoning within an increasingly long conversation.

This workflow places new demands on edge inference. The model must generate tokens quickly, process long shared histories efficiently, and produce valid tool calls within a limited power and memory envelope.

In the MLPerf Inference v6.1 Edge Agentic benchmark, NVIDIA [TensorRT Edge-LLM](https://github.com/NVIDIA/TensorRT-Edge-LLM) ran Qwen3.6-27B on a single NVIDIA Jetson AGX Thor Developer Kit. The system achieved 52.33 tokens per second and completed all 1,007 turns of the performance workload in 24 minutes and 36 seconds, 6.4x faster than the llama.cpp reference submission of 2 hours and 37 minutes. The result uses NVFP4 quantization, tree-based multi-token prediction (MTP), and KV cache reuse.

## How MLPerf measures end-to-end agentic AI performance

[MLPerf Edge Agentic](https://github.com/mlcommons/inference/tree/master/language/edge-agentic) measures an OpenAI-compatible model endpoint in two phases: performance and accuracy.

The performance phase replays recorded software-engineering agent trajectories. The model receives a user request, generates a tool call, observes the tool result, and continues the same conversation. The workload contains 20 conversations and 1,007 generated turns. Input length grows across turns and reaches approximately 23.5K tokens, making long-context processing an important part of the measurement. Intersection of Union (IoU) based inline accuracy is also measured to ensure the performance phase is running the agent correctly.

The accuracy phase uses Berkeley Function Calling Leaderboard (BFCL) v4 prompts with single-turn only and reasoning off to balance accuracy and evaluation time on edge devices. It evaluates whether the model selects the correct function, generates valid arguments, and avoids calling a tool when no tool is required.

## MLPerf Edge Agentic benchmark results on Jetson AGX Thor

The TensorRT Edge-LLM submission used Qwen3.6-27B in SingleStream mode on one Jetson AGX Thor Developer Kit with 128 GB of unified memory at the MAXN power mode..

| Metric | Result |
|---|---|
| Output throughput | 52.33 tokens per second |
| Median time to first token | 247.12 ms |
| Median time per output token | 14.68 ms |
| BFCL overall accuracy | 87.94% |

*Table 1. MLPerf v6.1 NVIDIA Edge Agentic submission result summary*

The [MLCommons Edge Agentic example](https://github.com/mlcommons/endpoints/tree/main/examples/11_Edge_Agentic_Example) also publishes a llama.cpp reference run on Jetson AGX Thor, which uses Qwen3.6-27B with Q4_K_M quantization and completes in 2 hours and 37 minutes. The TensorRT Edge-LLM submission completes the workload in 24 minutes and 36 seconds, or 6.4x less time.

## Using NVFP4 quantization to accelerate Qwen3.6-27B inference

Low-batch LLM decoding on edge platforms is known to be heavily bounded by DRAM bandwidth. Reducing the size of both weights and activations reduces the memory footprint of the kernels and therefore boosts decoding performance.

The submitted Qwen3.6-27B model uses NVFP4 for weights and activations, including the language-model head, and FP8 for the KV cache. NVFP4 is a 4-bit floating-point format supported by the NVIDIA Blackwell GPU in Jetson AGX Thor. TensorRT Edge-LLM uses optimized kernels to accelerate the quantized model while maintaining the accuracy required by MLPerf.

The smaller model representation also leaves more of the 128 GB unified memory available for the long context, speculative decoding state, and application workloads. Developers can start from a published, calibrated [Qwen3.6-27B NVFP4 checkpoint](https://huggingface.co/centml/Qwen3.6-27B-NVFP4-W4A4-mlpinf). A deployment team can use a published quantized checkpoint or perform post-training quantization once on any development system before deploying the model.

## Reusing KV cache across agent turns

Each new request in an agent trajectory contains most of the preceding conversation plus a new model response or tool result. Without reuse, the model must prefill the shared history again on every turn. The cost increases as the conversation grows.

TensorRT Edge-LLM identifies reusable prompt prefixes and restores their cached attention KV pages. Qwen3.6 uses a hybrid model architecture, so the runtime also restores the recurrent state and partial KV-page state required to continue execution correctly. It then prefills only the new suffix of the conversation.

KV cache and recurrent-state reuse reduce repeated long-context computation across the complete agent trajectory. This optimization complements tree-based MTP: cache reuse reduces the cost before generation begins, while MTP reduces the number of target-model steps during generation.

On this workload, ~96% of the prompt tokens are served with hot cache. The runtime only prefills ~0.5M of the total 13.6M prompt tokens across the turns.

## Using tree-based multi-token prediction to accelerate LLM inference

Standard autoregressive decoding generates one token for each model invocation. Multi-token prediction uses a draft model to predict several future tokens, which the target model then verifies together. Recent models typically have official MTP weights trained and shipped together with the main model.

In addition to traditional linear MTP, TensorRT Edge-LLM implements a tree-based MTP implementation. Instead of keeping only one predicted continuation, the runtime organizes high-probability candidates into a tree. The target model verifies the candidates in one forward pass, and the runtime accepts the matching path. If multiple candidates are accepted, the system advances generation by several tokens.

You can adjust drafting parameters when launching the server. The MLPerf server configuration uses 8 draft steps, the top-2 candidates at each drafting depth, and a 16-node verification tree. Tree-based verification is useful for function calling because tool names, JSON syntax, and common argument structures are often predictable, while multiple branches can preserve likely alternatives for individual argument values. Compared with a linear MTP with 3 draft steps, tree-based MTP could achieve an additional ~40% decoding performance gain for this workload.

## How to run the MLPerf Edge Agentic benchmark

The implementation used for this submission is available on the [TensorRT Edge-LLM release/0.9.1-mlpinf branch](https://github.com/NVIDIA/TensorRT-Edge-LLM/tree/release/0.9.1-mlpinf). The branch includes the model export settings, TensorRT engine build commands, server configuration, and MLPerf client configuration

1. Clone TensorRT Edge-LLM and initialize its submodules.

`git clone --branch release` `/0` `.9.1-mlpinf \` ` ` `https:` `//github` `.com` `/NVIDIA/TensorRT-Edge-LLM` `.git` `cd` `TensorRT-Edge-LLM` `git submodule update --init --recursive` |

2. Download the calibrated NVFP4 checkpoint.

`huggingface-cli download \` ` ` `centml` `/Qwen3` `.6-27B-NVFP4-W4A4-mlpinf \` `--` `local` `-` `dir` `"$WORK/Qwen3.6-27B-NVFP4-W4A4-mlpinf"` |

3. Follow `mlperf/README.md`

to build TensorRT Edge-LLM, export the checkpoint with the tree-MTP interface, and build the base and draft TensorRT engines.

`$VENV` `/bin/python` `-m tensorrt_edgellm.scripts.` `export` `\` ` ` `"$WORK/Qwen3.6-27B-NVFP4-W4A4-mlpinf"` `\` ` ` `"$WORK/onnx"` `\` `--mtp-tree-base --skip-visual` |

4. Launch the OpenAI-compatible TensorRT Edge-LLM server.

`export` `REPO=` `"$PWD"` `export` `VENV=` `/path/to/venv-edgellm-export` `export` `WORK=` `/path/to/mlperf-artifacts` `bash` `mlperf` `/serve_edgellm` `.sh` |

5. Clone the MLCommons endpoint harness, install its BFCL dependencies, update the model and tokenizer paths in `mlperf/config.yaml`

, and run the benchmark.

`git clone https:` `//github` `.com` `/mlcommons/endpoints` `.git` `cd` `endpoints` `python3.12 -m venv .venv` `source` `.venv` `/bin/activate` `pip ` `install` `-e ` `".[dev,bfcl]"` `inference-endpoint benchmark from-config \` `--config ` `"$REPO/mlperf/config.yaml"` |

The supplied configuration runs the performance and accuracy phases with temperature 0, seed 42, reasoning disabled, and concurrency 1. Use the `--accuracy-only`

option to run only the BFCL accuracy phase. For more information about the dataset and client configuration, see the [MLCommons Edge Agentic example](https://github.com/mlcommons/endpoints/tree/main/examples/11_Edge_Agentic_Example).

For full MLPerf Inference v6.1 results across all submissions, see the MLCommons [announcement](http://mlcommons.org/2026/09/mlperf-inference-v6-1-results/). For server-scale Vera Rubin performance, see [NVIDIA Vera Rubin NVL72 Delivers Leading Performance in MLPerf Inference v6.1 Debut](https://blogs.nvidia.com/blog/vera-rubin-nvl72-mlperf-inference/).

*Acknowledgments**This work represents contributions from the TensorRT Edge-LLM, ModelOpt, Jetson, and MLPerf teams at NVIDIA, especially Zihao Kong, Xiang Guo, Yoco Xiao, Qikai Li and Ashwin Nanjappa. Thanks to the MLCommons community for developing the Edge Agentic benchmark and endpoint harness.*

## Start the discussion at forums.developer.nvidia.com
