# blog

source: https://research.colfax-intl.com/blog/

We present expository-style articles and coding tutorials on our blog.

-
[Optimization diaries: S/P ping-pong for FlashAttention-4 decode](https://research.colfax-intl.com/optimization-diaries-s-p-ping-pong-for-flashattention-4-decode/)LLM Inference is divided into a prefill phase and a decode phase. During prefill, the model processes a large number of input tokens and populates a key-value (KV) cache. During decode, it autoregressively generates one or a few new tokens at a time using the cached keys and values. In this blog post, we discuss an optimization for FlashAttention-4 (FA4)…

[Go to article…](https://research.colfax-intl.com/optimization-diaries-s-p-ping-pong-for-flashattention-4-decode/) -
[Optimization diaries: Improving FlashAttention-4 backward pass kernel design for head dimension 64](https://research.colfax-intl.com/optimization-diaries-improving-flashattention-4-backward-for-head-dimension-64/)In this blog post we discuss the backward pass of FlashAttention-4 (FA4) on NVIDIA Blackwell GPUs. For head dimension 128, FA4 backward is highly performant, achieving 1237 TFLOP/s, or about 55% of peak compute throughput on a B200 GPU. However, at head dimension 64, the same kernel achieves only 30–37% of peak compute throughput for long sequence lengths. This suggests…

[Go to article…](https://research.colfax-intl.com/optimization-diaries-improving-flashattention-4-backward-for-head-dimension-64/) -
[Optimizing an NVFP4 Blockscaled GEMM on RTX PRO 6000 Blackwell GPU (SM120)](https://research.colfax-intl.com/optimizing-an-nvfp4-blockscaled-gemm-on-rtx-pro-6000-blackwell-gpu-sm120/)This article is a continuation of our series on NVFP4 blockscaling on SM12x GPUs. In Part 1, we covered relevant PTX instructions, scale-factor layout details, and implementation details in CuTe DSL, including how to convert a CUTLASS dense GEMM example into an NVFP4 blockscaled GEMM. In this article, we optimize the NVFP4 GEMM from Part 1 for the NVIDIA RTX…

[Go to article…](https://research.colfax-intl.com/optimizing-an-nvfp4-blockscaled-gemm-on-rtx-pro-6000-blackwell-gpu-sm120/) -
[NVFP4 Blockscaled GEMM on NVIDIA RTX Pro Blackwell GPUs (SM12x)](https://research.colfax-intl.com/cutlass-tutorial-nvfp4-blockscaled-gemm-on-nvidia-rtx-pro-blackwell-gpus-sm12x/)In this article, we explore hardware-supported NVFP4 blockscaled GEMM on SM12x GPUs, such as the NVIDIA RTX Pro 6000 Blackwell Server Edition (SM120) or NVIDIA DGX Spark (SM121). We will first discuss features of these GPUs and their kernel programming paradigm, situating them relative to SM10x (e.g. B200 or B300) and SM8x (Ampere/Ada). Then, we will discuss sub-byte blockscaled GEMM on…

[Go to article…](https://research.colfax-intl.com/cutlass-tutorial-nvfp4-blockscaled-gemm-on-nvidia-rtx-pro-blackwell-gpus-sm12x/) -
[Dynamic persistent tile scheduling with Cluster Launch Control (CLC) on NVIDIA Blackwell GPUs](https://research.colfax-intl.com/dynamic-persistent-tile-scheduling-with-cluster-launch-control-clc-on-nvidia-blackwell-gpus/)This blog post discusses Cluster Launch Control (CLC), a hardware-supported feature on NVIDIA Blackwell GPUs that facilitates optimal tile scheduling, in particular with respect to load balancing. To provide context, we first survey a few common scheduling strategies and the deficiencies CLC is designed to address. We then walk through the implementation-level details of using CLC in a CuTe DSL…

[Go to article…](https://research.colfax-intl.com/dynamic-persistent-tile-scheduling-with-cluster-launch-control-clc-on-nvidia-blackwell-gpus/) -
[FlexAttention + FlashAttention-4: Fast and Flexible (External)](https://research.colfax-intl.com/flexattention-flashattention-4-fast-and-flexible-external/)In this PyTorch blog on which we collaborated, we explain the FlexAttention extension to FlashAttention-4 (or from another point of view, the incorporation of FA-4 as an attention backend for the PyTorch FlexAttention API).

[Go to article…](https://research.colfax-intl.com/flexattention-flashattention-4-fast-and-flexible-external/) -
[CUTLASS Tutorial: Hardware-supported Block-scaling with NVIDIA Blackwell GPUs](https://research.colfax-intl.com/cutlass-tutorial-hardware-supported-block-scaling-with-nvidia-blackwell-gpus/)Welcome to part 4 of our series investigating GEMM on the NVIDIA Blackwell architecture. So far we have discussed the capabilities of the new Blackwell Tensor Core UMMA instructions, including handling sub-byte data types, and how to work with them in CUTLASS. In this part, we will continue our exploration of low-precision computation by discussing how to utilize the blockscaling…

[Go to article…](https://research.colfax-intl.com/cutlass-tutorial-hardware-supported-block-scaling-with-nvidia-blackwell-gpus/) -
[FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling](https://research.colfax-intl.com/flashattention-4-algorithm-and-kernel-pipelining-co-design-for-asymmetric-hardware-scaling/)Modern accelerators like Blackwell GPUs continue the trend of asymmetric hardware scaling, where tensor core throughput grows far faster than other resources such as shared memory bandwidth, special function units (SFUs) for transcendental operations like exponential, and general-purpose integer and floating-point ALUs. From the Hopper H100 to the Blackwell B200, for instance, BF16 tensor core throughput increases from 1 to…

[Go to article…](https://research.colfax-intl.com/flashattention-4-algorithm-and-kernel-pipelining-co-design-for-asymmetric-hardware-scaling/) -
[A User’s Guide to FlexAttention in FlashAttention CuTe DSL](https://research.colfax-intl.com/a-users-guide-to-flexattention-in-flash-attention-cute-dsl/)Many variants of attention (Vaswani et al., 2017) have become popular in recent years, for reasons related to performance and model quality. These include: The PyTorch team at Meta recognized that most of these variants (including all of the above) can be unified under one elegant framework, dubbed FlexAttention (Guessous et al., 2024). This simple API allows users to define…

[Go to article…](https://research.colfax-intl.com/a-users-guide-to-flexattention-in-flash-attention-cute-dsl/) -
[Categorical Foundations for CuTe Layouts](https://research.colfax-intl.com/categorical-foundations-for-cute-layouts/)In GPU programming, performance depends critically on how data is stored and accessed in memory. While the data we care about is typically multi-dimensional, the GPU’s memory is fundamentally one-dimensional. This means that when we want to load, store, or otherwise manipulate data, we need to map its multi-dimensional logical coordinates to one-dimensional physical coordinates. This mapping, known as a…

[Go to article…](https://research.colfax-intl.com/categorical-foundations-for-cute-layouts/)
