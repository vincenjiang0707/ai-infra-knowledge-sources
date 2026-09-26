source: https://github.com/vllm-project/tpu-inference

| [ Documentation](https://docs.vllm.ai/projects/tpu/en/latest/) |

[|](https://blog.vllm.ai/)

**Blog**[|](https://discuss.vllm.ai/c/hardware-support/google-tpu-support/27)

**User Forum**[(#sig-tpu) |](https://slack.vllm.ai)

**Developer Slack**
**🤝 Contribute to the Project**

*Looking to help? Click a badge below to find issues that need your attention.*

[Announcing Gemma 4 on vLLM](https://vllm.ai/blog/gemma4)Byte for byte, the most capable open models - available on TPUs on Day 0!

*Previous News* 🔥

[Pytorch Conference](https://pytorchconference.sched.com/event/27QCh/sponsored-session-everything-everywhere-all-at-once-vllm-hardware-optionality-with-spotify-and-google-brittany-rockwell-google-shireen-kheradpey-spotify)Learn how Spotify uses vLLM with both GPUs and TPUs to drive down costs and improve user experience.[Ray Summit, November 3-5](https://www.anyscale.com/ray-summit/2025)in San Francisco![JAX DevLab on November 18th](https://rsvp.withgoogle.com/events/devlab-fall-2025)in Sunnyvale!- [2025/10]
[vLLM TPU: A New Unified Backend Supporting PyTorch and JAX on TPU](https://blog.vllm.ai/2025/10/16/vllm-tpu.html)

vLLM TPU is now powered by `tpu-inference`

, an expressive and powerful new hardware plugin unifying JAX and PyTorch under a single lowering path within the vLLM project. The new backend now provides a framework for developers to:

- Push the limits of TPU hardware performance in open source.
- Provide more flexibility to JAX and PyTorch users by running PyTorch model definitions performantly on TPU without any additional code changes, while also extending native support to JAX.
- Retain vLLM standardization: keep the same user experience, telemetry, and interface.

Although vLLM TPU’s new unified backend makes out-of-the-box high performance serving possible with any model supported in vLLM, the reality is that we're still in the process of implementing a few core components.

For this reason, we’ve provided ** Recommended Models** and

**pages detailing the models and features that are validated through unit, integration, and performance testing.**

[Recommended Features](https://docs.vllm.ai/projects/tpu/en/latest/recommended_features/)Get started with vLLM on TPUs by following the [quickstart guide](https://docs.vllm.ai/projects/tpu/en/latest/getting_started/quickstart/).

Visit our [documentation](https://docs.vllm.ai/projects/tpu/en/latest/) to learn more.

**Compatible TPU Generations**

- Recommended: v7x, v5e, v6e
- Experimental: v3, v4, v5p

Below is the live status of our supported models, features, and kernels. Click on any category to expand the detailed support table. It is automatically updated from our detailed [Support Matrices](https://github.com/vllm-project/tpu-inference/tree/main/support_matrices).

*Last Updated: 2026-08-27 07:02 AM UTC*

## **🚦 ***Status Legend*

*Status Legend*


- ✅
Passing:Tested and works as expected. Ready for use.- ❌
Failing:Known to be broken or not functional. Help is wanted to fix this!- 🧪
Experimental:Works, but unoptimized or pending community validation.- 📝
Planned:Not yet implemented, but on the official roadmap.- ⛔️
Unplanned:There is no benefit to adding this.- ❓
Untested:The functionality exists but has not been recently or thoroughly verified.

📐View Matrix Aggregation Rules (v6e/v7x & C+P)


🛠️ Correctness + Performance (C + P)

- ❌
Failing: If either check fails.- ✅
Passing: IfBOTHchecks pass successfully.- ❓
Untested: If any check is untested (and neither fails).

🌐 Hardware Rollups (v6e + v7x)

- ❌
Failing: If the feature fails oneitherv6e or v7x.- ✅
Passing: If the feature passes onBOTHv6e and v7x.- ❓
Untested: If either generation is untested (and neither fails).

**Click to expand support matrices**


Stable support status for official releases and production deployments.

✅ Tested Models

🚀 Advanced Capabilities## Core Features


Feature Flax Torchax Default async scheduler ✅ ✅ ✅ Chunked Prefill ✅ ✅ ✅ DCN-based P/D disaggregation ✅ ✅ ✅ KV Cache Offload ✅ ✅ ✅ LoRA_Torch ✅ ✅ ✅ Multimodal Inputs ✅ ✅ ✅ Out-of-tree model support ✅ ✅ ✅ Prefix Caching ✅ ✅ ✅ Single Program Multi Data ✅ ✅ ✅ Speculative Decoding: Eagle3 ✅ ✅ ✅ Speculative Decoding: Ngram ✅ ✅ ✅ Speculative Decoding: DFlash ✅ ❓ ✅ hybrid kv cache ❓ ❓ ❓ multi-host ❓ ❓ ❓ runai_model_streamer_loader ❓ ❓ ❓ sampling_params ❓ ❓ ❓ Step Pooling (Embedding) ❓ ❓ ❓ structured_decoding ❓ ❓ ❓ ## Parallelism Techniques


Feature Flax Torchax Single-host Multi-host Single-host Multi-host PP ✅ ✅ ✅ ✅ DP ✅ ❓ ✅ ❓ EP ✅ ❓ ✅ ❓ TP ✅ ❓ ✅ ❓ CP ❓ ❓ ❓ ❓ SP ( [vote to prioritize])❓ ❓ ❓ ❓ ## Quantization Methods


Checkpoint dtype Method Supported

Hardware AccelerationFlax Torchax FP4 W4A16 mxfp4 v7 ❓ ❓ FP8 W8A16 compressed-tensor v7 ❓ ❓ FP8 W8A8 compressed-tensor v7 ❓ ❓ INT4 W4A16 awq v5, v6 ❓ ❓ INT8 W8A8 compressed-tensor v5, v6 ❓ ❓ NVFP4 W4A16 modelopt_fp4 v7 ❓ ❓

Note:

This table only tests checkpoint loading compatibility.

🔬 Microbenchmark Kernel Support

Category Test W16A16 W8A8 W8A16 W4A4 W4A8 W4A16 MoeFused MoE ❓ ❓ ❓ ❓ ❓ ❓ gmm ❓ ❓ ❓ ❓ ❓ ❓ DenseAll‑gather matmul ❓ ❓ ❓ ❓ ❓ ❓ AttentionGeneric Ragged Paged

Attention V3*❓ ❓ ❓ ❓ ❓ ❓ MLA ❓ ❓ ❓ ❓ ❓ ❓ Ragged Paged

Attention V3 Head_Dim

64*❓ ❓ ❓ ❓ ❓ ❓

Note:

For attention kernels, W[x]A[y] denotes KV cache as W, A as compute, and x, y as bit precision.

**Click to expand support matrices**


Support status for the latest nightly/main branch developments.

✅ Tested Models

🚀 Advanced Capabilities## Core Features


Feature Flax Torchax Default async scheduler ✅ ✅ ✅ Chunked Prefill ✅ ✅ ✅ DCN-based P/D disaggregation ✅ ✅ ✅ KV Cache Offload ✅ ✅ ✅ LoRA_Torch ✅ ✅ ✅ Multimodal Inputs ✅ ✅ ✅ Out-of-tree model support ✅ ✅ ✅ Prefix Caching ✅ ✅ ✅ Single Program Multi Data ✅ ✅ ✅ Speculative Decoding: Eagle3 ✅ ✅ ✅ Speculative Decoding: DFlash ✅ ✅ ✅ Speculative Decoding: Ngram ✅ ✅ ✅ hybrid kv cache ❓ ❓ ❓ multi-host ❓ ❓ ❓ runai_model_streamer_loader ❓ ❓ ❓ sampling_params ❓ ❓ ❓ Step Pooling (Embedding) ❓ ❓ ❓ structured_decoding ❓ ❓ ❓ ## Parallelism Techniques


Feature Flax Torchax Single-host Multi-host Single-host Multi-host PP ✅ ✅ ✅ ✅ DP ✅ ❓ ✅ ❓ EP ✅ ❓ ✅ ❓ TP ✅ ❓ ❌ ❓ CP ❓ ❓ ❓ ❓ SP ( [vote to prioritize])❓ ❓ ❓ ❓ ## Quantization Methods


Checkpoint dtype Method Supported

Hardware AccelerationFlax Torchax FP4 W4A16 mxfp4 v7 ❓ ❓ FP8 W8A16 compressed-tensor v7 ❓ ❓ FP8 W8A8 compressed-tensor v7 ❓ ❓ INT4 W4A16 awq v5, v6 ❓ ❓ INT8 W8A8 compressed-tensor v5, v6 ❓ ❓ NVFP4 W4A16 modelopt_fp4 v7 ❓ ❓

Note:

This table only tests checkpoint loading compatibility.

🔬 Microbenchmark Kernel Support

Category Test W16A16 W8A8 W8A16 W4A4 W4A8 W4A16 MoeFused MoE ❓ ❓ ❓ ❓ ❓ ❓ gmm ❓ ❓ ❓ ❓ ❓ ❓ DenseAll‑gather matmul ❓ ❓ ❓ ❓ ❓ ❓ AttentionGeneric Ragged Paged

Attention V3*❓ ❓ ❓ ❓ ❓ ❓ MLA ❓ ❓ ❓ ❓ ❓ ❓ Ragged Paged

Attention V3 Head_Dim

64*❓ ❓ ❓ ❓ ❓ ❓

Note:

For attention kernels, W[x]A[y] denotes KV cache as W, A as compute, and x, y as bit precision.

We're thrilled you're interested in contributing to the vLLM TPU project! Your help is essential for making our tools better for everyone. There are many ways to get involved, even if you're not ready to write code.

**Ways to Contribute:**

**🐞 Submit Bugs & Suggest Features:**See an issue or have an idea? Open a[new issue](https://github.com/vllm-project/tpu-inference/issues/new/choose)to let us know.**👀 Provide Feedback on Pull Requests:**Lend your expertise by reviewing[open pull requests](https://github.com/vllm-project/tpu-inference/pulls)and helping us improve the quality of our codebase.**📚 Improve Our Documentation:**Help us make our guides clearer. Fix a typo, clarify a confusing section, or write a new recipe.

If you're ready to contribute code, our ** Contributing Guide** is the best place to start. It covers everything you need to know, including:

**Tips for finding an issue to work on**(we recommend starting with our!.[good-first issues](https://github.com/vllm-project/tpu-inference/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)

A huge thank you to everyone who has helped build and improve `vllm-project/tpu-inference`

!

**🌟 ***Contribution Type Legend & Ranking*

*Contribution Type Legend & Ranking*


Emoji Contribution Meaning 💻 CodeSubmitted merged pull requests or code changes. 🐛 IssuesOpened valid issues or bug reports. 👀 ReviewsReviewed pull requests and provided feedback.

**🏆 Ranking:** Contributors are sorted from highest to lowest based on their total effort score (`Total Commits + Unique Issues Opened + PRs Reviewed`

). If there is a tie, contributors are displayed alphabetically.

**...and more! Click to view all contributors.**

- For technical questions and feature requests, open a GitHub
[Issue](https://github.com/vllm-project/tpu-inference/issues) - For feature requests, please open one on Github
[here](https://github.com/vllm-project/tpu-inference/issues/new/choose) - For discussing with fellow users, use the
[TPU support topic in the vLLM Forum](https://discuss.vllm.ai/c/hardware-support/google-tpu-support/27) - For coordinating contributions and development, use the
[Developer Slack](https://join.slack.com/share/enQtOTY2OTUxMDIyNjY1OS00M2MxYWQwZjAyMGZjM2MyZjRjNTA0ZjRkNjkzOTRhMzg0NDM2OTlkZDAxOTAzYmJmNzdkNDc4OGZjYTUwMmRh) - For collaborations and partnerships, contact us at
[vllm-tpu@google.com](mailto:vllm-tpu@google.com)