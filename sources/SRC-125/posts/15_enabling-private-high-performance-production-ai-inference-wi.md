# enabling-private-high-performance-production-ai-inference-with-nvidia-confidential-computing

source: https://developer.nvidia.com/blog/enabling-private-high-performance-production-ai-inference-with-nvidia-confidential-computing/

As large language model (LLM) inference increasingly processes sensitive information and proprietary model context across personal, enterprise, and regulated settings, data must be processed inside a trusted environment. [NVIDIA Confidential Computing (CC)](https://www.nvidia.com/en-us/data-center/solutions/confidential-computing/) provides a pathway for running these workloads securely using memory-encrypted confidential virtual machines (CVMs), confidential GPUs, and encrypted [NVIDIA NVLink](https://www.nvidia.com/en-us/data-center/nvlink/). This enables running production AI inference on trusted hardware.

Inference frameworks such as NVIDIA [TensorRT LLM](https://github.com/NVIDIA/TensorRT-LLM) deliver best-in-class AI inference by combining framework-level optimizations with NVIDIA accelerated computing. However, when these frameworks run in a CC-enabled environment, secure execution changes assumptions behind memory movement, timing, scheduling, and multi-GPU communication. These changes introduce performance overhead if the runtime does not adapt. Maintaining high performance therefore requires the inference framework and the confidential computing environment to be optimized together.

For AI platform engineers evaluating confidential inference on [NVIDIA Blackwell](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/) GPUs, this post examines the CC-aware adaptations that AI inference frameworks like TensorRT LLM use to account for secure execution while helping preserve inference performance. It presents a controlled methodology that teams can apply to quantify CC overhead on their own workloads.

## Selecting a workload to expose CC overhead

Workload characteristics determine how visible CC overhead can be. High request volume can amortize fixed encryption costs by overlapping stalls with other work, making the direct effects harder to observe.

To expose these effects, select a workload with a long input context, extended output generation, and low concurrency. Long context stresses data movement during prefill, extended generation amplifies small per-token CC overhead during decode, and low concurrency limits the opportunity to hide those costs across concurrent requests.

The NVIDIA performance engineering team used these characteristics for the workload evaluated here.

Parameter | Configuration |
|---|---|
Model |
|

**Inference framework****I/O sequence length****Concurrent requests****Parallelism****KV cache**

*Table 1. Workload configuration for the CC on and CC off comparison*## Measuring CC overhead with a controlled CC-on and CC-off comparison

To isolate the performance impact of CC, run the same workload under two conditions: confidential compute disabled (CC off) and confidential compute enabled (CC on) holding the model, hardware, framework version, sequence lengths, parallelism, and concurrency constant so that CC state is the only changing variable.

At each concurrency level:

**Output throughput retained**: 100 x (CC on output tokens/s ÷ CC off output tokens/s)**Latency overhead Time Per Output Token (TPOT):**100 x (CC on TPOT ÷ CC off TPOT − 1)

Performance teams can use these measurements to quantify how much of the CC-off baseline is retained when CC is enabled for the target workload. The NVIDIA performance engineering team applied this comparison using the hardware and software configuration summarized in Table 2.

Component | Version / Detail |
|---|---|
Hardware | 1
|

**Platform****Host OS****Host kernel****Guest OS****Guest kernel****Guest vCPUs****Guest NUMA****NVIDIA driver****VBIOS****GPU power limit****CUDA****TensorRT LLM**[nvcr.io/nvidia/tensorrt-llm/release:1.3.0rc22](https://github.com/NVIDIA/TensorRT-LLM/releases/tag/v1.3.0rc22)**NCCL****OpenSSL****Orchestration**

*Table 2. Hardware and software configuration used for both CC-on and CC-off runs*### Performance results

As shown in Figures 1 and 2, across concurrency 1–16, CC on retained 96.1– 98.2% of CC off output-token throughput, while mean TPOT remained within 1.2% to 4.3% of the baseline.

## Identifying and reducing CC overhead

The NVIDIA Blackwell confidential computing architecture introduces hardware-enforced security paths for protecting data and workloads in use. For a detailed overview of the architecture, see [Hardware-Rooted AI Security That Won’t Slow You Down](https://developer.nvidia.com/blog/hardware-rooted-ai-security-that-wont-slow-you-down/).

For TensorRT LLM users and framework developers, the following details show how these secure paths change common runtime assumptions and how TensorRT LLM adapts to reduce the resulting performance overhead.

### Adapting host-to-device data movement

In the B200 CC, host-to-device transfers pass through a software encrypted bounce buffer because the GPU cannot directly access protected CVM memory. This changes the behavior expected by inference frameworks: pinned memory no longer provides its usual asynchronous-transfer advantage, and some copies can block the calling thread.

**Host-to-device mitigation**: TensorRT LLM uses CC-aware memory selection, choosing pageable memory for affected paths instead of unconditionally using pinned memory.**Device-to-host mitigation**: TensorRT LLM moves repeated token and sampling-data readback to an asynchronous worker, preventing protected copies from blocking the main scheduler during decode. For details, see[TensorRT LLM](https://github.com/NVIDIA/TensorRT-LLM/pull/11573)[PR #11573](https://github.com/NVIDIA/TensorRT-LLM/pull/11573)**.**

### Stabilizing kernel autotuner timing

The kernel autotuner normally uses CUDA events to compare candidate tactics. In the tested CC configuration, CUDA-event timestamps produced an unstable timing signal, which could cause the autotuner to select a slower tactic.

**Mitigation**: TensorRT LLM uses the GPU`%globaltimer`

for tactic measurements under CC while retaining CUDA events outside CC. For details, see[TensorRT LLM](https://github.com/NVIDIA/TensorRT-LLM/pull/11657)[PR #11657](https://github.com/NVIDIA/TensorRT-LLM/pull/11657).

### Choosing CC-aware multi-GPU communication

NVLS (NVLink SHARP) multicast is not available in B200 CC configurations. Without NVLS, NCCL_SYMMETRIC cannot provide its intended multicast benefit but may still incur memory registration and cross-rank synchronization costs before using a non-multicast collective path.

**Mitigation**: Frameworks targeting CC should detect NVLS availability and choose communication algorithms that minimize latency for the given message size, topology, and workload characteristics.

## Get started with NVIDIA Confidential Computing

NVIDIA Confidential Computing extends hardware-enforced protection across confidential VMs, NVIDIA Blackwell GPUs, and encrypted NVLink, protecting proprietary models, enterprise context, and sensitive prompts while they are processed.

Confidential computing does not remove the need for performance engineering—it makes framework awareness even more important. With TensorRT LLM CC-aware adaptations to secure data movement, autotuning, and multi-GPU communication in place, confidential DeepSeek-R1 inference retained more than 96% of CC-off output-token throughput while keeping per-token latency overhead below 5% on eight NVIDIA B200 GPUs.

As organizations move private inference into production, security configuration and inference optimization should be approached as a single deployment problem. Enable confidential computing, attest the environment, and benchmark CC-on and CC-off using the exact workload you intend to serve. For AI platform engineers and TensorRT LLM users moving private inference into production, security configuration and inference optimization should be treated as a full-stack engineering effort.

To start planning your confidential inference deployment, use the [NVIDIA Trusted Computing documentation](https://docs.nvidia.com/nvtrust/index.html) and explore the latest [TensorRT LLM](https://nvidia.github.io/TensorRT-LLM/latest/release-notes.html)[ features and release notes](https://nvidia.github.io/TensorRT-LLM/latest/release-notes.html). To stay up to date with the latest developments, follow [NVIDIA Confidential Compute news](https://developer.nvidia.com/blog/tag/confidential-compute/).

### Acknowledgments

*I would like to thank Dan Hansen, Sheel Pethe, Samuel Mendoza-Jonas, Moein Ghaniyoun, Vidhya Krishnan, Avinash Ahuja, Laikh Tewari, Laura Martinez, and Matheen Raza for their engineering contributions, technical guidance, analysis, and thoughtful review throughout this work.*

## Start the discussion at forums.developer.nvidia.com
