# article

source: https://research.colfax-intl.com/category/article/

# Category: Article

-
[Optimization diaries: S/P ping-pong for FlashAttention-4 decode](https://research.colfax-intl.com/optimization-diaries-s-p-ping-pong-for-flashattention-4-decode/)LLM Inference is divided into a prefill phase and a decode phase. During prefill, the model processes a large number of input tokens and populates a key-value (KV) cache. During decode, it autoregressively generates one or a few new tokens at a time using the cached keys and values. In this blog post, we discuss…

[Go to article…](https://research.colfax-intl.com/optimization-diaries-s-p-ping-pong-for-flashattention-4-decode/) -
[Optimization diaries: Improving FlashAttention-4 backward pass kernel design for head dimension 64](https://research.colfax-intl.com/optimization-diaries-improving-flashattention-4-backward-for-head-dimension-64/)In this blog post we discuss the backward pass of FlashAttention-4 (FA4) on NVIDIA Blackwell GPUs. For head dimension 128, FA4 backward is highly performant, achieving 1237 TFLOP/s, or about 55% of peak compute throughput on a B200 GPU. However, at head dimension 64, the same kernel achieves only 30–37% of peak compute throughput for…

[Go to article…](https://research.colfax-intl.com/optimization-diaries-improving-flashattention-4-backward-for-head-dimension-64/) -
[Dynamic persistent tile scheduling with Cluster Launch Control (CLC) on NVIDIA Blackwell GPUs](https://research.colfax-intl.com/dynamic-persistent-tile-scheduling-with-cluster-launch-control-clc-on-nvidia-blackwell-gpus/)This blog post discusses Cluster Launch Control (CLC), a hardware-supported feature on NVIDIA Blackwell GPUs that facilitates optimal tile scheduling, in particular with respect to load balancing. To provide context, we first survey a few common scheduling strategies and the deficiencies CLC is designed to address. We then walk through the implementation-level details of using…

[Go to article…](https://research.colfax-intl.com/dynamic-persistent-tile-scheduling-with-cluster-launch-control-clc-on-nvidia-blackwell-gpus/) -
[FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling](https://research.colfax-intl.com/flashattention-4-algorithm-and-kernel-pipelining-co-design-for-asymmetric-hardware-scaling/)Modern accelerators like Blackwell GPUs continue the trend of asymmetric hardware scaling, where tensor core throughput grows far faster than other resources such as shared memory bandwidth, special function units (SFUs) for transcendental operations like exponential, and general-purpose integer and floating-point ALUs. From the Hopper H100 to the Blackwell B200, for instance, BF16 tensor core…

[Go to article…](https://research.colfax-intl.com/flashattention-4-algorithm-and-kernel-pipelining-co-design-for-asymmetric-hardware-scaling/) -
[DeepSeek-R1 and FP8 Mixed-Precision Training](https://research.colfax-intl.com/deepseek-r1-and-fp8-mixed-precision-training/)DeepSeek has shocked the world with the release of their reasoning model DeepSeek-R1. Similar to OpenAI’s o1 and Google Gemini’s Flash Thinking, the R1 model aims to improve the quality of its replies by generating a “chain of thought” before responding to a prompt. The excitement around R1 stems from it achieving parity with o1…

[Go to article…](https://research.colfax-intl.com/deepseek-r1-and-fp8-mixed-precision-training/) -
[CUTLASS Tutorial: Persistent Kernels and Stream-K](https://research.colfax-intl.com/cutlass-tutorial-persistent-kernels-and-stream-k/)Welcome to Part 3 of our tutorial series on GEMM (GEneral Matrix Multiplication). In Parts 1 and 2, we discussed GEMM at length from the perspective of a single threadblock, introducing the WGMMA matmul primitive, pipelining, and warp specialization. In this part, we will examine GEMM from the perspective of the entire grid. At this…

[Go to article…](https://research.colfax-intl.com/cutlass-tutorial-persistent-kernels-and-stream-k/) -
[Epilogue Fusion in CUTLASS with Epilogue Visitor Trees](https://research.colfax-intl.com/epilogue_visitor_tree/)Welcome to a supplemental article for our tutorial series on GEMM (GEneral Matrix Multiplication). Posts in the main series (1, 2) have discussed performant implementations of GEMM on NVIDIA GPUs by looking at the mainloop, the part responsible for the actual GEMM computation. But the mainloop is only a part of the CUTLASS workload. In…

[Go to article…](https://research.colfax-intl.com/epilogue_visitor_tree/) -
[GPU passthrough on Proxmox VE 8.2](https://research.colfax-intl.com/gpu-passthrough-on-proxmox-ve-8/)In this guide, we will walk through the steps to enable GPU passthrough and by extension PCIe passthrough on a virtual machine (VM) deployed through Proxmox. PCIe passthrough provides a path for VMs to directly access underlying PCIe hardware, in the case of this article, an Nvidia® A30 GPU. This setup is ideal for scenarios…

[Go to article…](https://research.colfax-intl.com/gpu-passthrough-on-proxmox-ve-8/) -
[CUTLASS Tutorial: Efficient GEMM kernel designs with Pipelining](https://research.colfax-intl.com/cutlass-tutorial-design-of-a-gemm-kernel/)Welcome to Part 2 of our tutorial series on GEMM (GEneral Matrix Multiplication). In Part 1, we discussed the computational side of GEMM by going over WGMMA, which is the primitive instruction to multiply small matrix tiles on GPUs based on the NVIDIA® Hopper™ architecture. In this part, we turn our focus to the memory…

[Go to article…](https://research.colfax-intl.com/cutlass-tutorial-design-of-a-gemm-kernel/) -
[CUTLASS Tutorial: Fast Matrix-Multiplication with WGMMA on NVIDIA® Hopper™ GPUs](https://research.colfax-intl.com/cutlass-tutorial-wgmma-hopper/)No series of CUDA® tutorials is complete without a section on GEMM (GEneral Matrix Multiplication). Arguably the most important routine on modern GPUs, GEMM constitutes the majority of compute done in neural networks, large language models, and many graphics applications. Despite its ubiquity, GEMM is notoriously hard to implement efficiently. This 3-part tutorial series aims…

[Go to article…](https://research.colfax-intl.com/cutlass-tutorial-wgmma-hopper/)
