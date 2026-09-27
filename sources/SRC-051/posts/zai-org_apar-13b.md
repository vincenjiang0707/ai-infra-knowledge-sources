# zai-org/apar-13b

source: https://huggingface.co/zai-org/apar-13b

# APAR-13B

<center>
<p>
<a href="https://arxiv.org/abs/2401.06761" target="_blank">[📃Paper: APAR: LLMs Can Do Auto-Parallel Auto-Regressive Decoding]</a>
</p>
</center>

> The massive adoption of large language models (LLMs) demands efficient deployment strategies. However, the auto-regressive decoding process, which is fundamental to how most LLMs generate text, poses challenges to achieve efficient serving. In this work, we introduce a parallel auto-regressive generation method. By instruct-tuning on general domain data that contains hierarchical structures, we enable LLMs to independently plan their generation process and perform auto-parallel auto-regressive (APAR) generation, significantly reducing the number of generation steps. APAR alone can achieve up to 2x speed-up, and when combined with speculative decoding, the speed-up can reach up to 4x. In addition, APAR reduces the key-value cache consumption and attention computation during generation. This leads to a throughput increase of 20-70% and a latency reduce of 20-35% in high-throughput scenarios, compared to state-of-the-art serving frameworks.

**See our [paper](https://arxiv.org/abs/2401.06761) and [Github repo](https://github.com/THUDM/APAR) for details about the APAR-13B model.**
