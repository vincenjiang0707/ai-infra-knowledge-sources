# [Issue #126] Batched speculation benchmarks? (incl. with compilation)

source: https://github.com/SafeAILab/EAGLE/issues/126
state: closed | updated: 2025-11-13T12:12:56Z
labels: 

## 正文

Hello, and thank you for pushing the boundary on speculative generation!

Question 1: In Eagle-1 paper, table 7 reports throughput figures for Vicuna-7B at 1.97x. How exactly was this measured? (GPU, batch size, testing code). How would this be different if generating with temperature==1 ?

Question 2: Is Eagle-2 compatible with batch generation? Specifically including _tree attention_ and temperature == 1?
If so, please share the code example like in Eagle-1 and the benchmarks like in Eagle-1 paper section4.4, table 7.

Question 3: Were there any tests of Eagle/Eagle2 in setups with compilation or some faster frameworks, or with TensorRT, how would speedup figures change vs. the ones reported in the papers? Especially in the batched setup



## 评论 (4)

### Liyuhui-12 · 2024-08-28

> Question 1: In Eagle-1 paper, table 7 reports throughput figures for Vicuna-7B at 1.97x. How exactly was this measured? (GPU, batch size, testing code). How would this be different if generating with temperature==1 ?

The specific settings can be found in Section 4.4 of our paper, and the code is on the v1 branch. As with other speculative sampling methods, the performance of temperature=1 will be slightly worse than temperature=0.

> Question 2: Is Eagle-2 compatible with batch generation? Specifically including _tree attention_ and temperature == 1? If so, please share the code example like in Eagle-1 and the benchmarks like in Eagle-1 paper section4.4, table 7.

EAGLE-2 currently does not support batch generation.

> Question 3: Were there any tests of Eagle/Eagle2 in setups with compilation or some faster frameworks, or with TensorRT, how would speedup figures change vs. the ones reported in the papers? Especially in the batched setup

Integration with other frameworks is a significant amount of work, and it is part of our future plans.

### Siegfried-qgf · 2024-09-02

Hello，I wanna ask if EAGLE2 method can generate in batches. Is this method itself not suitable for batch generation？

### LESSSE · 2025-11-13

Hello, I come to ask about this topic related to EAGLE3. I see there is an ablation study in EAGLE3 paper on batched results (Table 3 and Table 5). Can this code reproduce those results? 

Also for TABLE 1, what was the hardware setting that you used (single GPU? A100, H100 or RTX3090? you mention these 3 in the paper). 

Thanks 

### hongyanz · 2025-11-13

Batched results were run on the SGLang inference engine.

A100.
