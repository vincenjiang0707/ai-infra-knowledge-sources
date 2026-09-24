# how-full-stack-nim-optimizations-deliver-2-5x-more-users-on-nemotron-3-ultra

source: https://developer.nvidia.com/blog/how-full-stack-nim-optimizations-deliver-2-5x-more-users-on-nemotron-3-ultra/

Deploying a large language model is only the first step toward production-ready serving. Production teams also need to serve as many concurrent users as possible on available GPU infrastructure while preserving the interactivity that keeps applications responsive.

That tradeoff matters even more for agentic AI workloads, where prompts can be long, context can be reused across steps, and applications often stream extended responses back to users.

NVIDIA NIM packages model- and GPU-aware serving choices into a deployable microservice. Instead of starting from a blank runtime configuration, developers get a validated serving configuration and a supported deployment path, while retaining the ability to benchmark the NIM against their own traffic.

## What NIM adds: Performance engineering and production readiness

Inference performance is a system property. Precision and kernels, parallelism, scheduling, batching, memory allocation, prefix reuse, model-specific state caches, and decoding strategy all interact. A configuration is useful only if it improves throughput while staying within the application latency target.

NIM turns this optimization work into a tested starting point. NVIDIA engineers validate configurations for supported model, GPU, and precision combinations, then package the runtime and model artifacts behind standard APIs. For production deployments, NIM Certified adds regular inference-stack updates, CVE handling, broader hardware validation, and commercial support through NVIDIA AI Enterprise.

NIM delivers two benefits in one deployment path: validated performance engineering plus an enterprise-ready container lifecycle and support model.

## Case study: Nemotron 3 Ultra NIM delivers up to 2.5x higher throughput for agentic workloads

The benchmark definition used throughout this article is:

- Hardware: 4xB200
- Agentic workload: 64K/400/76% KV reuse/50 TPS/user (20 ms ITL)

This Pareto chart compares the open-source baseline serving stack (NIM Off) against the fully optimized NIM 2.0.12 serving stack (NIM On).

| Configuration | Native 256K max context | What it represents |
|---|---|---|
| NIM Off baseline | 718 tok/s | No NIM optimizations |
| NIM On (2.0.12) optimized serving stack | 1,997 tok/s 2.5x v. Baseline | Optimized NIM stack: cache/state reuse, MTP speculative decoding and associated fixes, autotuned kernels, partial-prefix matching, scheduler, batching, memory, and parallelism tuning |

*Table 1.*


*System output-token throughput across four B200 GPUs at the 50 TPS/User target*

## How NIM 2.0.12 optimized serving stack works

The measured gains come from interacting configuration bundles, not independent switches whose percentages can simply be added. The main optimization layers are:

**Precision and autotuned model-aware kernels.**Autotuned mixture-of-experts and Mamba kernels map the hybrid architecture efficiently to NVIDIA Blackwell GPUs.**Parallel execution.**Tensor parallelism distributes the model across four GPUs, while expert-aware execution improves utilization for the mixture-of-experts layers.**Prefix and model-state reuse.**Prefix caching avoids recomputing repeated context, partial-prefix matching recovers reuse when only part of a prefix matches, and Mamba state-cache settings are tuned for the model architecture.**Scheduler, batching, and memory tuning.**Concurrent-sequence limits, batched-token limits, block size, and GPU-memory allocation keep more work in flight without crossing the latency target.**MTP speculative decoding.**NIM 2.0.12 optimized serving stack (including MTP) adds MTP and its associated fixes to the same optimized serving stack. The incremental benefit depends on acceptance rate and available memory headroom.

## Benchmark the NIM on your own workload

The published curves are a starting point, not a promise that every application will see the same result. The fastest way to determine fit is to replay representative traffic and build a Pareto curve for the latency metric that matters to your users.

**Deploy the exact software versions.**Use NIM 2.0.12 (or newer version), and pin the image tag or digest for every run.**Prepare representative traffic.**Use a Mooncake-format JSONL trace or capture controlled NIM requests, with appropriate access controls and sanitization for sensitive data.**Measure performance.**Use NVIDIA AIPerf to replay representative traffic and get perf benchmarks**Select the Pareto point that meets the SLO.**Compare output throughput among points that satisfy the SLO/latency constraints and determine fit for deployment:

`for` `C ` `in` `1 4 8 16 32 64; ` `do` ` ` `aiperf profile \` ` ` `--model nvidia` `/nemotron-3-ultra-550b-a55b` `\` ` ` `--endpoint-` `type` `chat --streaming \` ` ` `--url localhost:8000 \` ` ` `--input-` `file` `.` `/agentic-trace` `.jsonl \` ` ` `--custom-dataset-` `type` `mooncake_trace \` ` ` `--no-fixed-schedule \` ` ` `--concurrency ` `"$C"` ` ` `done` |

**Example AIPerf concurrency sweep.** Replace the trace, request count, and endpoint details with the workload you want to model.

## Download and run Nemotron 3 Ultra NIM

Start from the [Nemotron 3 Ultra NIM page](https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/nemotron-3-ultra-550b-a55b/latest/tags), accept the governing terms, and select the NIM 2.0.12 tag or the exact published digest. After downloading, find and select a profile. The following lists all profiles packaged in the NIM:

`export` `NGC_API_KEY=<your-personal-api-key>` `export` `LOCAL_NIM_CACHE=$HOME/.cache` `/nim` `export` `NIM_TAG=2.0.12` `mkdir` `-p ` `"$LOCAL_NIM_CACHE"` `echo` `"$NGC_API_KEY"` `| docker login nvcr.io \` ` ` `--username ` `'$oauthtoken'` `--password-stdin` `docker run --gpus all --shm-size=16GB \` ` ` `-e NGC_API_KEY \` ` ` `-e NIM_MODEL_PROFILE \` ` ` `-` `v` `"$LOCAL_NIM_CACHE:/opt/nim/.cache"` `\` ` ` `-p 8000:8000 \` ` ` `nvcr.io` `/nim/nvidia/nemotron-3-ultra-550b-a55b` `:$NIM_TAG list-model-profiles` |

To pick an optimized profile for agentic workloads on a four-GPU B200 system, you would set the `NIM_MODEL_PROFILE`

to `vllm-nvidia-b200-nvfp4-tp4-pp1-throughput-90.0`

and enable speculative decoding:

`export` `NGC_API_KEY=<your-personal-api-key>` `export` `LOCAL_NIM_CACHE=$HOME/.cache` `/nim` `export` `NIM_TAG=2.0.12` `export` `NIM_MODEL_PROFILE=vllm-nvidia-b200-nvfp4-tp4-pp1-throughput-90.0` `mkdir` `-p ` `"$LOCAL_NIM_CACHE"` `echo` `"$NGC_API_KEY"` `| docker login nvcr.io \` ` ` `--username ` `'$oauthtoken'` `--password-stdin` `docker run --gpus all --shm-size=16GB \` ` ` `-e NGC_API_KEY \` ` ` `-e NIM_MODEL_PROFILE \` ` ` `-e NIM_SPECDEC_ENABLE=1 \` ` ` `-` `v` `"$LOCAL_NIM_CACHE:/opt/nim/.cache"` `\` ` ` `-p 8000:8000 \` ` ` `nvcr.io` `/nim/nvidia/nemotron-3-ultra-550b-a55b` `:$NIM_TAG` |

## A performance-engineered starting point for production

NVIDIA NIM packages model- and GPU-aware serving optimizations into a deployable microservice. For Nemotron 3 Ultra on a 4xB200 system, these optimizations let organizations serve up to 2.5x more users at 50 TPS/user compared with a NIM-off baseline, while keeping the deployment path practical for real multi-user serving.

NIM combines validated performance engineering with regular inference-stack updates, CVE handling, hardware validation, and commercial support through NVIDIA AI Enterprise. More performance-optimized NIM configurations are planned across a broader range of models, giving developers additional validated starting points for their own latency, throughput, and cost objectives.

## Get started

Download the Nemotron 3 Ultra NIM 2.0.12 from NGC, run it on your NVIDIA GPU infrastructure, and replay representative traffic with NVIDIA AIPerf to select the Pareto point that meets your application target.

**Resources**

## Start the discussion at forums.developer.nvidia.com
