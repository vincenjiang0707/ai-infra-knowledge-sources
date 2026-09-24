# co-designing-ai-models-using-speculative-decoding-for-faster-llm-inference

source: https://developer.nvidia.com/blog/co-designing-ai-models-using-speculative-decoding-for-faster-llm-inference/

This post is the third in a series on AI model co-design. It explores how to accelerate LLM inference while maintaining accuracy using [speculative decoding](https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/) and offers five guidelines for selecting draft length and draft mechanism across the Pareto frontier.

For a discussion of how model design choices impact both throughput and interactivity without sacrificing accuracy, see [AI Model Co-Design: Hardware-Friendly LLM Design](https://developer.nvidia.com/blog/ai-model-co-design-hardware-friendly-llm-design/) (Part 1). For an explanation of how group size (query heads per KV head), head dimension, and sequence length shape the performance of dense attention, see[ Co-Designing AI Model Attention for Fast, Interactive Long-Context Inference](https://developer.nvidia.com/blog/co-designing-ai-model-attention-for-fast-interactive-long-context-inference/) (Part 2).

## What is speculative decoding?

Speculative decoding is a technique for accelerating the autoregressive decoding phase of LLM inference by predicting multiple tokens per iteration. A small draft model first predicts several likely next tokens. These tokens are then verified in parallel with a single pass through the larger target model.

This approach reduces the total number of decoding iterations while increasing the arithmetic intensity of the target model, without requiring higher concurrency. The target model accepts the proposed tokens in sequence until it encounters the first mismatch. The next prediction cycle then resumes from that position. Because only tokens accepted by the target model are retained, speculative decoding produces the same output sequence as standard decoding, unless the acceptance criteria are deliberately relaxed. Figure 2 illustrates this decoding flow.

The *draft length* (*acceptance length* (

The speedup from speculative decoding can be quantified as the ratio of time taken by the target model to sequentially generate

where

## Selecting the optimal draft length

For simplicity, if we ignore draft model latency, speculation provides a speedup when:

During verification, compute scales with (

### Draft length and performance of linear layers

With speculation, the GEMM-

Notably, with [mixture-of-experts (MoE)](https://www.nvidia.com/en-us/glossary/mixture-of-experts/) models become sparser and long-context workloads increase KV capacity pressure, the effective concurrency per expert decreases, making larger draft lengths attractive across the Pareto frontier.

**Guideline 1: **Increase speculative decoding draft length to push GEMMs into the compute-bound region without increasing KV cache capacity pressure.

### Draft length and attention performance

For reasoning and agentic workloads, attention tends to dominate the execution time in the throughput-oriented region. Decode attention has an arithmetic intensity of about [Co-Designing AI Model Attention for Fast, Interactive Long-Context Inference](https://developer.nvidia.com/blog/co-designing-ai-model-attention-for-fast-interactive-long-context-inference/).

Speculation increases this to

Figure 4 shows normalized attention throughput as

**Guideline 2:** When attention dominates decode time, choose

Attention runtime also depends on tile size. Figure 5 shows that runtime increases in steps as

**Guideline 3: **If you choose

The relative weight of Guideline 1 compared to Guidelines 2 and 3 depends on the percentage of runtime spent in FFNs compared to attention at the preferred operating point. Communication also adds verification cost as D increases, although compute and communication overlap can mitigate the overhead.

### Draft length at the far right of the Pareto curve

Moving towards the far right of the Pareto curve,

While MoEs do see more experts activated with increasing draft length, a combination of model sharding strategies and efficient kernels such as Grouped GEMMs can keep this overhead low. Larger draft lengths can therefore help in the low latency region, as long as acceptance remains high.

At very low latency, the number of sequential kernel launches determines workload latency. Because kernel launches scale linearly with layer count, for an autoregressive draft model with a similar layer structure to the target, the speedup can be approximated as:

where

In other words, increasing

**Guideline 4: **At very low latency, increase

## Selecting a draft mechanism

Selecting

A multitude of techniques have been proposed over the years, with different tradeoffs in training, parameter, and runtime costs. External drafting suggests using a small standalone LLM, while MTP, EAGLE-3, DFlash, and DSpark use auxiliary layers combined with information from the target model to predict tokens. Suffix and n-gram methods are model-free and instead reuse patterns already seen in the token stream.

Table 1 compares key drafting methods, including how they generate tokens, their serve-time memory, and their draft overhead.

External draft model | EAGLE-3 | MTP | DFlash | DSpark | Suffix / n-gram | |
Draft architecture | Small LLM | Decoder layer(s) + linear projection | Decoder layer(s) + linear projection | Decoder layer(s) + linear KV fusion | Decoder layer(s) + linear KV fusion + lightweight Markov head | String matching, no model |
Inputs | Token IDs | Previous-token embedding + target hidden states | Target final hidden state | Fused target hidden states used as draft KV | Fused target hidden states used as draft KV | Token stream |
Generation method | Runs the module | Runs the module | Generates | Generates | One lookup | |
Release method | Separate model release | Separate post-training head | Part of the base model checkpoint | Separate post-training head | Separate post-training head | Independent of target |
Training cost | From scratch: 1T-10T+ tokens Distilled: 100B-400B Adapted: 10M-1B | 1-10B additional tokens after target training | Usually trained with the target during pretraining | 1-10B additional tokens after target training | 1-10B additional tokens after target training | None |
Activation memory cost | Draft weights + full KV cache | Weights + small KV cache | Weights + small KV cache | Weights + small KV cache built from target | Weights + small KV cache built from target | None |
Speculation cost per | Full draft model forward | 1 layer, serial | 1 layer, serial | ~5 layers, once | ~5 layers once + lightweight Markov head, serial | O(1) lookup |
Best for | LPU and LPU+GPU Not recommended for GPUs | Not recommended – lower | Best for larger models on GPUs | Smaller models, batch size 1 | Smaller models, batch size 1 | Workloads with high repetition |


*Table 1. Comparison of common draft mechanisms across inputs, generation method, training cost, serve-time memory, and draft cost*To quantify the tradeoff between

Figure 6 shows how AL changes as D increases on [SPEED-Bench](https://huggingface.co/blog/nvidia/speed-bench), with Qwen 3.5 122B A10B as the target. SPEED-Bench is a speculative decoding benchmark developed by NVIDIA with the goal of representing realistic production workloads. It covers multiple task domains such as coding and summarization and has a variety of splits at different input sequence lengths. We recommend SPEED-Bench for

On the 32K split, Qwen 3.5 35B A3B reaches an

Higher

As shown in Figure 6, all external drafts reach higher

Meanwhile, DFlash

For a large target model with many layers, both overheads are negligible, but as

To navigate the tradeoff between [SPEED-Bench](https://huggingface.co/blog/nvidia/speed-bench) for [NVIDIA TensorRT LLM](https://github.com/NVIDIA/TensorRT-LLM) to quantify draft overhead.

Beyond inference performance, draft training scope and costs deserve consideration. While MTP must be co-trained with the target model, EAGLE, DFlash, and DSpark can be added to the final model checkpoint. Similarly, a continuum of options exists for external draft model creation. Training from scratch and distillation from the target yield the highest ALs, while adapting an existing model to the desired target through cross-model adaptation techniques can significantly reduce training costs at the expense of

Fine-tuning the target model can change its output distribution and hidden representations. Learned drafters trained for a particular target checkpoint can therefore lose acceptance even when the target model improves. After changing the target, remeasure

MTP is part of the target model and should continue to be trained during fine-tuning or be realigned in a dedicated follow-up stage. Target-attached drafters such as EAGLE-3, DFlash, and DSpark use the target’s hidden states and will need to be adapted to the updated checkpoint with additional training.

External draft models do not consume target hidden states, but they still approximate the target’s output distribution and may require fine-tuning or distillation. Suffix and n-gram methods have no learned drafter and therefore require no retraining, although their effectiveness still depends on how much repetition appears in the deployed workload.

**Guideline 5: **Choose the draft mechanism that gives the best decode speedup for your workload and hardware, considering

Get started co-designing speculative decoding

Use the five guidelines summarized below as a checklist for selecting

- Increase speculative decoding draft length to push GEMMs into a compute-bound region without increasing KV cache capacity pressure.
- When attention dominates decode time, choose
as a starting point. - For larger draft lengths, prefer values where
is a multiple of 128 to align with the attention kernel tile size. - At very low latency, use a fast draft mechanism and increase
only while the gain in justifies the added draft cost. - Choose the draft mechanism by balancing
and draft overhead for your workload and hardware. Benchmark both under realistic serving conditions and consider training and deployment cost.

For post-trained drafters, ready-to-run training examples are available in [NVIDIA/Model-Optimizer](https://github.com/NVIDIA/Model-Optimizer) for EAGLE-3, DFlash, and DSpark. See how we did this for NVIDIA Nemotron 3.5 Lightning: [fine-tune DSpark](https://github.com/NVIDIA/Model-Optimizer/blob/main/tools/launcher/examples/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16/hf_streaming_dspark_warmstart.yaml), then quantize it to [FP8](https://github.com/NVIDIA/Model-Optimizer/blob/main/tools/launcher/examples/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16/hf_dspark_ptq_fp8.yaml) or [NVFP4](https://github.com/NVIDIA/Model-Optimizer/blob/main/tools/launcher/examples/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16/hf_dspark_ptq_nvfp4.yaml). Use the examples as starting points, then validate AL and end-to-end speed on your own model, workload, and hardware.

### Acknowledgments

*This post is a cross-team NVIDIA effort. We are grateful to Bhargava Gopireddy, Ritika Borkar, Dor Tsur, Andrii Skliar, Benjamin Chislett, Yaniv Galron, Talor Abramovich, Yoav Miron, Rabeeh Karimi Mahabadi, Roger Waleffe, Udi Karpas, Ran Zilberstein, Brian Pharris, and Eduardo Alvarez for their help.*

## Start the discussion at forums.developer.nvidia.com
