# [Issue #2682] Eval support for DeepSeek-R1 like reasoning models

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/2682
state: open | updated: 2026-09-26T17:25:56Z
labels: 

## 正文

DeepSeek-R1 like models natively using CoT to think of the strategy and then respond with the answer. The current GPQA, MuSR and BBH like reasoning benchmarks, assume the final answer only is returned. What's a good way to add support to evaluate R1 like models which have `<think>...</think> ... solution ...` response format?

## 评论 (8)

### wirthFelix · 2025-03-11

Hi,
Coming late to this issue ; I encountered the same problem while running IFEVAL and quick-fixed it by adding a regexp filtering of the thinking part in the task's utils file:
```
--- a/lm_eval/tasks/ifeval/utils.py
+++ b/lm_eval/tasks/ifeval/utils.py
@@ -1,4 +1,5 @@
 import dataclasses
+import re
 from typing import Dict, Optional, Union
 
 from lm_eval.tasks.ifeval import instructions_registry
@@ -116,7 +117,8 @@ def process_results(doc, results):
         kwargs=doc["kwargs"],
     )
     response = results[0]
-
+    # Reasoning models modification : Remove the thinking part
+    response = re.sub(r".*?<\/think>(\\n)*", "", response, flags=re.DOTALL).strip()
     out_strict = test_instruction_following_strict(inp, response)
     out_loose = test_instruction_following_loose(inp, response)
```

There's likely a better way to fix it but it does the job if you need it to run. You should also increase the number of tokens generated to take into account the thinking process (in ifeval, max_gen_toks=1280 was not enough for some answers ; it is maybe meant to reach the '600 words' instruction) .

### Nithanaroy · 2025-03-11

Yeah, this works. Thanks for sharing. Why not directly change the doc_to_target in the task's YAML?

### wirthFelix · 2025-03-11

I only started using the library yesterday so I'm not aware of how everything works yet ; I noticed the 'filtered resps' field (when using --log_samples) contained the thinking part and found this way to fix it.
Now that you mention it, the doc_to_target field may be a much better way to fix ; How would you do it ?
Edit:
I reviewed the yaml file and it states the results are processed using the utils.process_result functions, which is where I put the modifications so it might actually be similar, just adapted to the ifeval task

### Zane0613 · 2025-03-11

> DeepSeek-R1 like models natively using CoT to think of the strategy and then respond with the answer. The current GPQA, MuSR and BBH like reasoning benchmarks, assume the final answer only is returned. What's a good way to add support to evaluate R1 like models which have `<think>...</think> ... solution ...` response format?

Hi, could you tell me what changes have you made to support deepseek R1? Are you using an API or an on-premises R1 model? Thanks!

### Divjyot · 2025-03-19

I dont see a complete `<think>` component of DeepSeek-R1 model in `resps` parts of output. As per my understanding `resps` is raw output from LM but it seems to have only partial thinking component.

I am using DeepSeek-R1-Distil-Qwen-1.5B and evaluated on `gpqa_diamond_generative_n_shot` dataset @Nithanaroy  

### wirthFelix · 2025-03-19

> I dont see a complete `<think>` component of DeepSeek-R1 model in `resps` parts of output. As per my understanding `resps` is raw output from LM but it seems to have only partial thinking component.
> 
> I am using DeepSeek-R1-Distil-Qwen-1.5B and evaluated on `gpqa_diamond_generative_n_shot` dataset [@Nithanaroy](https://github.com/Nithanaroy)

Following the instruction on https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B#usage-recommendations, you might want to manually add the `<think>\n` component yourself to the prompt.

### mgillr · 2026-09-26

Task-layer contribution toward this: #4249 adds a `strip_think` filter — backend-independent `<think>…</think>` removal before extraction (complete and unclosed blocks, per-draw under repeats, configurable end token) — plus a reasoning-model recipe in the docs (stop-sequence interference, `max_gen_toks`, flexible-extract for paper comparisons). This complements the existing per-backend `think_end_token` handling in `vllm`/`trtllm` by covering `hf` and API backends. Happy to extend toward a fuller reasoning task suite here if maintainers want a direction.

### mgillr · 2026-09-26

Ready-to-run support for your two named benchmarks is up in #4252 (building on the `strip_think` filter from #4249):

```bash
# GPQA (all three subsets)
lm_eval --model hf --model_args pretrained=deepseek-ai/DeepSeek-R1-Distill-Qwen-7B \
        --tasks gpqa_diamond_reasoning --apply_chat_template

# BBH (all 27 subtasks)
lm_eval --model hf ... --tasks bbh_boolean_expressions_reasoning
```

The variants change exactly three things vs. the base CoT templates: the `strip_think` filter prepended to each extraction chain, `max_gen_toks` raised to 32768, and stop sequences restricted to EOS (the `\n\n` and `Q:` stops in the base templates fire *inside* reasoning traces). Prompts, targets, and metrics are untouched — so the same benchmark scored with and without the variant isolates the trace effect, and reasoning/non-reasoning models stay comparable on a leaderboard.

MuSR (the third benchmark you named) needs a from-scratch config rather than a variant — noted in the PR as a follow-up.
