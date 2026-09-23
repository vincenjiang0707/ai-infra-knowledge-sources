# 2026-07-30-sglang-google-tpu

source: https://lmsys.org/blog/2026-07-30-sglang-google-tpu

# RadixArk Joins Forces with Google to Bring Full SGLang Features to TPUs

RadixArk and Google Cloud are partnering to bring [SGLang](https://github.com/sgl-project/sglang) to TPUs, giving developers ultimate flexibility for running workloads on their choice of hardware.

SGLang is an open source inference framework built for high throughput and low latency at production scale. With more than 30,000 GitHub stars and over 1,700 contributors, it runs on hundreds of thousands of GPUs worldwide and generates trillions of tokens in production every day. [RadixArk](https://www.radixark.com) is a maintainer of the SGLang project.

Currently, developers can run SGLang on the latest TPU generations through [SGL-JAX](https://github.com/sgl-project/sglang-jax), with support for major large language model and multimodal families including Gemma, Qwen, DeepSeek, GLM, Mimo, Kimi, Ling, MiniMax, and Grok, as well as diffusion models for video and image generation including Wan and Flux. Later this year, RadixArk will roll out SGL-torchtpu as an additional PyTorch-native TPU backend, featuring eager execution, PyTorch ecosystem compatibility, and MPMD support. It will let any AI researcher or engineer in the industry run LLMs with SGLang on Google's TPUs using standard PyTorch tooling, with high performance, scalability, and state-of-the-art features. These include the leading open models at full size on multi-host TPUs, with quality matched to published baselines, plus parallelism (data, tensor, expert, context, and pipeline), Radix Cache, HiCache, quantization, and speculative decoding — powered by TPU Pallas kernels built by RadixArk, Google, and the SGLang community.

Going forward, SGLang will enable new open models to run on TPU the same day they run on GPU, with that Day 0 support extending to every new TPU generation.

These make TPUs a drop-in, cost-efficient path to frontier inference. Teams run the same SGLang API and features they use on GPUs, with the freedom to choose hardware based on workload needs and price-performance.

"RadixArk's mission is to make frontier AI infrastructure open and accessible to every builder. SGLang embodies that, and we're excited to work with Google Cloud to bring its performance and flexibility to the TPU ecosystem," said **Ying Sheng**, CEO of RadixArk.

"To truly accelerate the frontier AI innovation, developers must have the freedom to choose and use AI training and serving platforms with better performance, reliability, scalability, and cost," said **Bill Jia**, Vice President of Engineering, Core ML/AI, Google. "Our collaboration with RadixArk is a critical step in delivering on our vision of programmable heterogeneity, where software serves as an open bridge rather than a lock-in mechanism. By bringing SGLang's high-throughput serving framework to Google TPUs, we are effectively eliminating the 'migration tax' for developers, allowing them to run their production workloads seamlessly across their choices of hardware (e.g. GPU, TPU) and AI framework (e.g. PyTorch, JAX) using the exact same SGLang inference APIs."

SGL-JAX, a joint effort by RadixArk and the SGLang community, is available today at [github.com/sgl-project/sglang-jax](https://github.com/sgl-project/sglang-jax).

The SGL family always welcomes new contributors to help build an open, high-performance serving engine together!
