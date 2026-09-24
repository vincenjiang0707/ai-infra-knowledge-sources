# simplifying-model-serving-across-multiple-gpus-with-nvidia-tensorrt-multi-device-integration-in-nvidia-dynamo-triton

source: https://developer.nvidia.com/blog/simplifying-model-serving-across-multiple-gpus-with-nvidia-tensorrt-multi-device-integration-in-nvidia-dynamo-triton/

The compute and memory demands of generative AI increasingly exceed what a single GPU can provide. [NVIDIA TensorRT multi-device inference](https://docs.nvidia.com/deeplearning/tensorrt/latest/inference-library/multi-device-inference.html) is a new capability that enables a single TensorRT network to execute across multiple GPUs using [NCCL](https://github.com/nvidia/nccl)-backed distributed collectives while retaining TensorRT inference optimizations. It is fully supported starting with TensorRT 11.0.

NVIDIA Dynamo-Triton (formerly NVIDIA Triton Inference Server) [release 26.07](https://docs.nvidia.com/deeplearning/triton-inference-server/release-notes/rel-26-07.html#rel-26-07) enables the multi-device inference capability of the TensorRT backend. One Triton` KIND_MODEL`

instance can own multiple GPUs, create per-rank TensorRT execution contexts, CUDA streams, and NCCL communicators, and launch the ranks together for each request. The application calls one named model through a gRPC endpoint instead of coordinating GPU ranks itself.

For organizations deploying generative AI, this closes the gap between multi-GPU acceleration and a consumable inference service. Teams can trade additional GPU resources for shorter request latency, keep the application interface and surrounding workflow stable, package the engine as a versioned Triton model, and keep rank and communicator lifecycle code out of the client. For latency-sensitive generative media workflows, a shorter time to result can reduce user wait time and accelerate review-and-refine cycles.

This post demonstrates the integration using [NVIDIA Cosmos 3 Nano](https://huggingface.co/nvidia/Cosmos3-Nano) video generation, a long-sequence workload featured in the previous post [Scaling AI Inference Across Multiple GPUs Using NVIDIA TensorRT with Multi-Device Inference Support](https://developer.nvidia.com/blog/scaling-ai-inference-across-multiple-gpus-using-nvidia-tensorrt-with-multi-device-inference-support/). Diffusers continue to orchestrate prompts, latents, classifier-free guidance (CFG), scheduling, VAE decode, and frame postprocessing. Dynamo-Triton serves the 36-layer denoising transformer, and TensorRT multi-device inference uses Ulysses context parallelism to distribute its 44,160 video tokens across as many as eight NVIDIA GPUs.

## How does Dynamo-Triton serve TensorRT multi-device models?

The distributed Ulysses graph is compiled into each TensorRT plan before deployment. The Dynamo-Triton TensorRT backend loads the versioned plan, creates the multi-rank execution state, and exposes one gRPC model endpoint. The client sends a transformer request to that endpoint; it does not coordinate the participating GPU ranks.

The Cosmos 3 Nano model provides a practical example of this boundary. The transformer accounts for 93.4% of the single-GPU generation time, making it the highest-impact stage to accelerate. Each of 35 denoising steps requires one negative or unconditional prediction and one prompt-conditioned prediction for CFG. The Diffusers proxy therefore makes two sequential Triton calls per step, for 70 transformer RPCs per generation. Each request carries prepared tensors and returns noise_patches to the application workflow.

### How does Dynamo-Triton activate a context-parallel distributed TensorRT plan?

The distributed graph is compiled into each context-parallel TensorRT plan. Dynamo-Triton configuration activates that plan; it does not convert a single-device engine into a distributed engine. The single-device baseline uses a standard GPU model instance on GPU 0. The two-, four-, and eight-GPU variants use `KIND_MODEL`

, enable the TensorRT backend multi-device path, and identify the participating ranks.

`# Excerpt from the generated CP8 config.pbtxt` `name: "cosmos3_cp8"` `backend: "tensorrt"` `max_batch_size: 0` `instance_group [` ` ` `{ kind: KIND_MODEL count: 1 }` `]` `parameters [` ` ` `{ key: "enable_multi_device" value: { string_value: "true" } },` ` ` `{ key: "multi_device_gpus" value: { string_value: "0,1,2,3,4,5,6,7" } }` `]` |

## Distributing Cosmos 3 with Ulysses context parallelism

The fixed Cosmos 3 Nano profile for this example produces 44,160 video tokens. At context-parallel size eight (CP8), each rank processes 5,520 video tokens outside attention. The shorter 2,992-token text path remains replicated. Within each of the 36 transformer layers, Ulysses changes the partitioning axis around attention so that every rank processes the full video sequence for a nonoverlapping subset of heads.

The engine is exported from PyTorch and compiled with Torch-TensorRT. Three local converters lower export-carrier operations to the TensorRT public distributed-collective layer: reduce-scatter, all-to-all, and all-gather. Each accepted context-parallel plan contains two initial reduce-scatters, three all-to-alls in each of 36 transformer layers, and one final all-gather. The resulting topology is two reduce-scatters plus 108 all-to-alls plus one all-gather.

## Benchmarking end-to-end generation latency

All four variants ran on the same healthy eight-GPU NVIDIA system. The single-device baseline used one GPU; CP2, CP4, and CP8 used two, four, and eight ranks. Every run used 1280×720 output, 189 frames at 24 FPS, and 35 denoising steps.

Each result includes one warm-up followed by five measured complete generations. Timing covers prompt work, the 70 Dynamo-Triton calls, CFG and scheduler updates, VAE decode, and frame postprocessing. Note that model loading and mp4 encoding were excluded.

Table 1 compares SD, CP2, CP4, and CP8 Cosmos 3 runs. End-to-end latency drops from 156.595 seconds on one GPU to 34.183 seconds on eight GPUs, while transformer RPC speedup increases to 6.09 times.

Variant | GPUs | E2E mean | E2E speedup | RPC mean | RPC speedup | RPC share |
|---|---|---|---|---|---|---|
SD | 1 | 156.595 | 1.00x | 146.192 | 1.00x | 93.4% |
CP2 | 2 | 87.999 | 1.78x | 77.548 | 1.89x | 88.1% |
CP4 | 4 | 53.093 | 2.95x | 42.661 | 3.43x | 80.4% |
CP8 | 8 | 34.183 | 4.58x | 23.993 | 6.09x | 70.2% |


*Table 1. Comparison of SD, CP2, CP4, and CP8 Cosmos 3 runs*On one GPU, transformer RPCs account for 93.4% of generation time. At CP8, that share falls to 70.2%. Time outside the measured RPC path remains between 10.2 and 10.5 seconds across configurations, so prompt work, scheduler updates, VAE decode, postprocessing, and other client overhead become a larger fraction of the total.

## Validating generated output before claiming performance

Every variant used the same seed and generation profile. Validation sampled frames 0, 47, 94, 141, and 188, checked format and temporal variation, and compared each context-parallel output with the single-device result. CP2, CP4, and CP8 passed the configured thresholds of mean absolute error (MAE) ≤ 25 and peak signal-to-noise ratio (PSNR) ≥ 18 dB.

The outputs are not claimed to be pixel-identical. CP2 and CP4 measured MAE 12.759 and PSNR 21.111 dB. CP8 measured MAE 16.316 and PSNR 19.400 dB. The contact sheet also shows the same coherent action across the clip: a robot arm cleaning a plate.

## Get started simplifying multi-GPU model serving

For product teams, these results demonstrate a practical option when response time carries more business value than minimizing the GPUs assigned to one request. A complete Cosmos 3 generation that previously took more than two and a half minutes completes in about 34 seconds, while the application continues to use a conventional model-serving interface.

Teams must still decide on the best approach based on a resource-for-latency trade-off. This benchmark does not measure concurrent request throughput, cost per generated video, or total cost of ownership (TCO). Teams should evaluate these metrics against their own SLOs and deployment economics.

To reproduce the results featured in this post in your own environment, download [NVIDIA Dynamo-Triton 26.07](https://docs.nvidia.com/deeplearning/triton-inference-server/release-notes/rel-26-07.html#rel-26-07) from NGC. Then use the TensorRT, Torch-TensorRT, Diffusers, and Cosmos resources linked.

To learn more, check out these related resources:

## Start the discussion at forums.developer.nvidia.com
