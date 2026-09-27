# [Issue #169] Abnormal result for qwen3 32b.

source: https://github.com/dropbox/hqq/issues/169
state: closed | updated: 2026-07-20T09:43:02Z
labels: 

## 正文

hqq worked all well with qwen3 until it came to the 32b one. Table below shows the result. Did you happen to run it before? 

Model | FP16 PPL | HQQ PPL | Increase | Pattern
-- | -- | -- | -- | --
0.6B | 26.16 | 32.22 | +6.06 
8B | 12.19 | 12.51 | +0.32 
14B | 10.78 | 11.09 | +0.31 
32B | 9.31 | 11.32 | +2.01 

Here is the cli to get ppl:
CUDA_VISIBLE_DEVICES=2,3 VLLM_WORKER_MULTIPROC_METHOD=spawn python -m lm_eval   --num_fewshot 0 --seed 42 --model vllm   --model_args pretrained=/models/Qwen3-32B-hqq/,dtype=half,tensor_parallel_size=2,enforce_eager=True,gpu_memory_utilization=0.8 --tasks wikitext   --batch_size 2


## 评论 (3)

### mobicham · 2025-11-05

Strange indeed, the error should go down as the model becomes larger. 
I wouldn't rely on wikitext perplexity btw,  a bit higher perplexity doesn't say much about the ability of the model to accomplish tasks, it just means that the generation is a bit different from the ground-truth token-by-token. You should rather use more reliable metrics like MMLU, Winogrande, etc.

```
task=winogrande
num_fewshot=5
VLLM_WORKER_MULTIPROC_METHOD=spawn VLLM_DISABLE_COMPILE_CACHE=1 python3 -m lm_eval --num_fewshot $num_fewshot --tasks $task --model vllm --model_args pretrained=$model,dtype=half --batch_size 2
```

### notfreemanliu-bot · 2025-11-06

Well, most of the papers, like AWQ, use PPL, at least as one of the metric, likely the major one. HQQ did the same in the blog. That aside, I found it really unexplanable. I wonder if there is other similar cases to show some pattern, or just leave the monkey on back for a while. 

### mobicham · 2025-11-06

Yes, PPL on wikitext is a popular approach simply because it's fast and simple to run, it only requires access to the logits (no annotations), but it doesn't mean that it's the correct metric to properly measure accuracy. 
PPL only measures how close the next token prediction is to the ground-truth, it doesn't tell you anything about the ability of the model to actually solve tasks. In fact, if you use sampling with instruct/thinking models, you'd getting totally different generated texts using the exact same model.

A more accurate approach is to run various task benchmarks and average the accuracy results. A popular target is 99%>= of the reference performance/recovery. I like to use the Hugging Face leaderboard metrics:
https://huggingface.co/dropbox-dash/Llama-3.1-8b-instruct_4bitgs64_hqq_calib#performance
Other people use similar metrics too:
https://huggingface.co/neuralmagic/Llama-3.2-3B-Instruct-quantized.w8a8#accuracy
-> People skip this step because it takes a lot of time to run, but it's the actual correct way to properly measure performance.
