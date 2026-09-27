# [Issue #3129] Qwen3-32B results with GSM8K and GSM8K_cot worse than paper

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3129
state: open | updated: 2026-09-26T16:24:03Z
labels: 

## 正文

I tried multiple versions, and all gave me at maximum 0.7 accuracy while the paper states 0.92..

I am calling the script like this:

````
lm_eval \
  --model hf \
  --model_args "pretrained=$QWEN_3_32B,dtype=bfloat16,device_map=auto" \
  --tasks gsm8k_cot \
  --num_fewshot 4 \
  --batch_size auto 
```

but getting these results:

````
|  Tasks  |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|---------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|gsm8k_cot|      3|flexible-extract|     4|exact_match|↑  |0.7074|±  |0.0125|
|         |       |strict-match    |     4|exact_match|↑  |0.6277|±  |0.0133|
``` 

I tried multiple suggested fixes from previous issues and PR's but nothing worked (tried for gsm8k and gsm8k_cot):
- system_instruct with \think tag and reason prompt ❌
- changing text_to_doc:
doc_to_text: 'Q: {{question}}
  Please reason step by step and summarize the result at the end with the format of ''The answer is xxx'', where xxx is the result.
  A:' ❌
- adding apply_chat_template ❌

Nothing helped. Can someone help?



## 评论 (16)

### SamuelMoor-Smith · 2025-07-16

+1

### dipta007 · 2025-07-18

+1

### Avelina9X · 2025-07-19

The `apply_chat_template` and `fewshot_as_multiturn` switches should *always* be enabled for templated chat models. Does enabling both switches improve things?

### jvonrad · 2025-07-20

> The `apply_chat_template` and `fewshot_as_multiturn` switches should _always_ be enabled for templated chat models. Does enabling both switches improve things?

No it gets even worse.. unfortunately

### jvonrad · 2025-07-22

> The `apply_chat_template` and `fewshot_as_multiturn` switches should _always_ be enabled for templated chat models. Does enabling both switches improve things?

tarte Job 72804 am Mon Jul 21 17:25:48 CEST 2025
Passed argument batch_size = auto. Detecting largest batch size
Determined Largest batch size: 1
hf (pretrained=/home/*/gwb082/LLMs/Qwen/Qwen3-32B,dtype=bfloat16,device_map=auto), gen_kwargs: (None), limit: None, num_fewshot: 4, batch_size: auto
|  Tasks  |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|---------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|gsm8k_cot|      3|flexible-extract|     4|exact_match|↑  |0.2168|±  |0.0114|
|         |       |strict-match    |     4|exact_match|↑  |0.0114|±  |0.0029|


this is with both flags

### wasifmasood · 2025-09-20

I got these results:

| Benchmark                | Metric / Task         | Qwen3-32B |
|---------------------------|-----------------------|-----------|
| **ARC Challenge**| acc                       | 0.5776 |
|                  | acc_norm                  | 0.6084 |
|                  | **Average**               | 0.5930 |
| **GPQA Diamond** | cot_n_shot (flex-ex)      | 0.1313 |
|                  | cot_zeroshot (flex-ex)    | 0.0758 |
|                  | generative_n_shot (flex-ex)| 0.3788 |
|                  | n_shot (acc)              | 0.4394 |
|                  | zeroshot (acc)            | 0.3838 |
|                  | **Average**               | 0.2818 |
| **GPQA Extended**| cot_n_shot (flex-ex)      | 0.2033 |
|                  | cot_zeroshot (flex-ex)    | 0.1117 |
|                  | generative_n_shot (flex-ex)| 0.3864 |
|                  | n_shot (acc)              | 0.4158 |
|                  | zeroshot (acc)            | 0.4121 |
|                  | **Average**               | 0.3059 |
| **GPQA Main**    | cot_n_shot (flex-ex)      | 0.1920 |
|                  | cot_zeroshot (flex-ex)    | 0.1116 |
|                  | generative_n_shot (flex-ex)| 0.3795 |
|                  | n_shot (acc)              | 0.4241 |
|                  | zeroshot (acc)            | 0.4063 |
|                  | **Average**               | 0.3027 |
| **IFEval**       | prompt_strict             | 0.2717 |
|                  | inst_strict               | 0.4365 |
|                  | prompt_loose              | 0.3198 |
|                  | inst_loose                | 0.4712 |
| **BBH CoT Fewshot (Notables)** | boolean_expressions     | 0.7080 |
|                                | causal_judgement        | 0.0374 |
|                                | date_understanding      | 0.0720 |
|                                | disambiguation_qa       | 0.0000 |
|                                | dyck_languages          | 0.4880 |
|                                | formal_fallacies        | 0.1280 |
|                                | geometric_shapes        | 0.3040 |
|                                | hyperbaton              | 0.0440 |
|                                | logical_deduction_5objs | 0.8360 |
|                                | logical_deduction_7objs | 0.6160 |
|                                | logical_deduction_3objs | 0.9000 |
|                                | movie_recommendation    | 0.7680 |
|                                | multistep_arithmetic_2  | 0.0000 |
|                                | navigate                | 0.9880 |
|                                | object_counting         | 0.8760 |
|                                | penguins_in_a_table     | 0.7260 |
|                                | reasoning_colored_objs  | 0.1160 |
|                                | ruin_names              | 0.1320 |
|                                | salient_translation_err | 0.0000 |
|                                | snarks                  | 0.0000 |
|                                | sports_understanding    | 0.6360 |
|                                | temporal_sequences      | 0.1760 |
|                                | tracking_5objs          | 0.9760 |
|                                | tracking_7objs          | 0.9160 |
|                                | tracking_3objs          | 0.9680 |
|                                | web_of_lies             | 1.0000 |
|                                | word_sorting            | 0.2520 |
|                                | **Average (all BBH CoT)** | 0.4312 |
| **GSM8K**        | strict_match              | 0.7407 |
|                  | flexible_extract          | 0.6361 |
|                  | **Average**               | 0.6884 |


#####
Here is my code 


```python
import json 
from gptqmodel.utils.eval import EVAL
import torch  # Import PyTorch for GPU memory management
from lm_eval import evaluator
```



list_models = [ '/models--Qwen--Qwen3-32B/snapshots/9216db5781bf21249d130ec9da846c4624c16137/' ]

list_model_name = [    'Qwen3-32B'       ]


tasks_list = ["ifeval", "gpqa", "arc_challenge", "gsm8k", "bbh"] 

batch_size = 2  



for model_path, model_name in zip(list_models, list_model_name):
    print(f"#######################")
    print(f"#### model name: {model_name} ####")
    print(f"#### model path: {model_path} ####")
    print(f"#######################")

    print(f"#######################")
    print(f"#### tasks list: {', '.join(tasks_list)} ####")
    print(f"#######################")


    results = evaluator.simple_evaluate(
        model="hf",  # Hugging Face model
        cache_requests=False,
        model_args=f"pretrained={model_path}",
        tasks=tasks_list, 
        batch_size=batch_size,
        device="cuda:0" 
    )


    results = results['results']
    json_string = json.dumps(results, indent=4)

    # Save to a file
    json_filename = f"llm-eval-{model_name}.json"
    with open(json_filename, "w") as file:
        file.write(json_string)

    print(f"### Results saved to {json_filename} ###")


    del results
    torch.cuda.empty_cache()
    torch.cuda.synchronize()  # Ensures all GPU processes are finished before the next iteration

    print(f"### GPU memory cleared for next iteration ###")



### fxmarty-amd · 2025-10-20

+1

### fxmarty-amd · 2025-10-21

To clarify: on `transformers==4.57.1`, `torch==2.8.0+rocm6.4`, lm-eval-harness 0c9072191e790204c4dfeb3285925b586a548c2e running on MI325 (but getting very close results on H100 as well):

```bash
export OUT_PATH="."
export TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
export EXP_NAME="${TIMESTAMP}_noquant_lmeval_repro_bs24"
CUDA_VISIBLE_DEVICES=7 nohup lm_eval --model hf \
    --model_args pretrained=Qwen/Qwen3-32B \
    --tasks gsm8k_platinum \
    --device cuda:0 \
    --batch_size 24 \
    --seed 42 &> ${OUT_PATH}/${EXP_NAME}.log &
```

yield

```
|    Tasks     |Version|     Filter     |n-shot|  Metric   |   |Value|   |Stderr|
|--------------|------:|----------------|-----:|-----------|---|----:|---|-----:|
|gsm8k_platinum|      3|flexible-extract|     5|exact_match|↑  |0.684|±  |0.0134|
|              |       |strict-match    |     5|exact_match|↑  |0.794|±  |0.0116|
```

 Apply chat template:

```bash
export OUT_PATH="."
export TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
export EXP_NAME="${TIMESTAMP}_noquant_lmeval_repro_bs24"
CUDA_VISIBLE_DEVICES=7 nohup lm_eval --model hf \
    --model_args pretrained=Qwen/Qwen3-32B \
    --tasks gsm8k_platinum \
    --device cuda:0 \
    --batch_size 24 \
    --apply_chat_template \
    --gen_kwargs "temperature=0.7,top_p=0.8,top_k=20,min_p=0,do_sample=True" \
    --seed 42 &> ${OUT_PATH}/${EXP_NAME}_template.log &
```

yields

```
|    Tasks     |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|gsm8k_platinum|      3|flexible-extract|     5|exact_match|↑  |0.2266|±  |0.0120|
|              |       |strict-match    |     5|exact_match|↑  |0.0141|±  |0.0034|
```

Apply chat template + fewshot_as_multiturn:

```bash
export OUT_PATH="."
export TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
export EXP_NAME="${TIMESTAMP}_noquant_lmeval_repro_bs24"
CUDA_VISIBLE_DEVICES=7 nohup lm_eval --model hf \
    --model_args pretrained=Qwen/Qwen3-32B \
    --tasks gsm8k_platinum \
    --device cuda:0 \
    --batch_size 24 \
    --apply_chat_template \
    --fewshot_as_multiturn \
    #--gen_kwargs "temperature=0.7,top_p=0.8,top_k=20,min_p=0,do_sample=True" \
    --seed 42 &> ${OUT_PATH}/${EXP_NAME}_template_multiturn.log &
```
yields

```
|    Tasks     |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|gsm8k_platinum|      3|flexible-extract|     5|exact_match|↑  |0.2283|±  |0.0121|
|              |       |strict-match    |     5|exact_match|↑  |0.0083|±  |0.0026|
```

Apply chat template + fewshot_as_multiturn + `--gen_kwargs "temperature=0.7,top_p=0.8,top_k=20,min_p=0,do_sample=True"`:

```bash
export OUT_PATH="."
export TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
export EXP_NAME="${TIMESTAMP}_noquant_lmeval_repro_bs24"
CUDA_VISIBLE_DEVICES=7 nohup lm_eval --model hf \
    --model_args pretrained=/models/Qwen_Qwen3-32B \
    --tasks gsm8k_platinum \
    --device cuda:0 \
    --batch_size 24 \
    --apply_chat_template \
    --fewshot_as_multiturn \
    --gen_kwargs "temperature=0.7,top_p=0.8,top_k=20,min_p=0,do_sample=True" \
    --seed 42 &> ${OUT_PATH}/${EXP_NAME}_template_multiturn_genkwargs.log &
```

yields

```
|    Tasks     |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|gsm8k_platinum|      3|flexible-extract|     5|exact_match|↑  |0.2275|±  |0.0121|
|              |       |strict-match    |     5|exact_match|↑  |0.0099|±  |0.0029|
```

This is very surprising as:
- `Qwen/Qwen3-8B` gets more like 0.90 eval metrics.
- the eval metrics are low
- chat template seems to be detrimental

I'll give a try with lighteval and see how it is there.

### wasifmasood · 2025-10-21

If you use temperature > 0.2, you need mutiple runs to average the results out. From the original paper, there is some tricks with the prompting as well which are never publisched. The only results I have been able to validate are of Deepseek only, for the rest, never been able to come closer than ~5% difference. 

Btw, where do you see Qwen/Qwen3-8B claiming 90% on GSMK dataset?

### fxmarty-amd · 2025-10-21

> If you use temperature > 0.2, you need mutiple runs to average the results out. 

By default lm-eval-harness does not use sampling for gsm8k/gsm8k_platinum, see:
https://github.com/EleutherAI/lm-evaluation-harness/blob/e916aa4176aca80b99f39cfc4f017c87002d9995/lm_eval/tasks/gsm8k/gsm8k.yaml#L23-L29
https://github.com/EleutherAI/lm-evaluation-harness/blob/e916aa4176aca80b99f39cfc4f017c87002d9995/lm_eval/tasks/gsm8k_platinum/gsm8k-platinum.yaml#L23-L29

> Btw, where do you see Qwen/Qwen3-8B claiming 90% on GSMK dataset?

It is not that it is claiming it. It is that running

```bash
export OUT_PATH="."
export TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
export EXP_NAME="${TIMESTAMP}_noquant_lmeval_repro_bs24"
CUDA_VISIBLE_DEVICES=7 nohup lm_eval --model hf \
    --model_args pretrained=Qwen/Qwen3-8B \
    --tasks gsm8k_platinum \
    --device cuda:0 \
    --batch_size 24 \
    --seed 42 &> ${OUT_PATH}/${EXP_NAME}.log &
```

yields

```
|    Tasks     |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|gsm8k_platinum|      3|flexible-extract|     5|exact_match|↑  |0.9173|±  |0.0079|
|              |       |strict-match    |     5|exact_match|↑  |0.9156|±  |0.0080|
```

(see https://github.com/EleutherAI/lm-evaluation-harness/issues/3357)

And actually page 7 https://arxiv.org/pdf/2505.09388:
<img width="600" alt="Image" src="https://github.com/user-attachments/assets/12d1b078-509c-4376-ad00-3040d4b29e2a" />


-----

edit: well, lighteval on `161d47cc1c10e3254d9b4144086d6650c1e9da70` and `torch==2.8.0+rocm6.4` and `transformers==4.57.1` yields even worse

```bash
export OUT_PATH="."
export TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
export EXP_NAME="${TIMESTAMP}_noquant_lighteval_bs24_greedy_5shot"
CUDA_VISIBLE_DEVICES=3 nohup lighteval accelerate \
    "model_name=Qwen/Qwen3-32B,generation_parameters={temperature:0},batch_size=24" \
    "lighteval|gsm8k|5" &> ${OUT_PATH}/${EXP_NAME}.log &
```

```
|      Task       |Version|     Metric     |Value |   |Stderr|
|-----------------|-------|----------------|-----:|---|-----:|
|all              |       |extractive_match|0.2388|±  |0.0117|
|lighteval:gsm8k:5|       |extractive_match|0.2388|±  |0.0117|
```

### fxmarty-amd · 2025-10-21

Using vllm @ https://github.com/vllm-project/vllm/commit/ecc3c0940a0993fe93e390f9fcf296b658482c33

```bash
export TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
export EXP_NAME="${TIMESTAMP}_noquant_lmeval_repro_bs24"
CUDA_VISIBLE_DEVICES=0 nohup lm_eval \
	--model vllm \
    --model_args pretrained=/models/Qwen_Qwen3-32B \
    --tasks gsm8k \
    --device cuda:0 \
    --batch_size 24 \
    --seed 42 &> ${EXP_NAME}_vllm.log &
```

gives

```
|Tasks|Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|-----|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|gsm8k|      3|flexible-extract|     5|exact_match|↑  |0.6164|±  |0.0134|
|     |       |strict-match    |     5|exact_match|↑  |0.7346|±  |0.0122|
```

in line with results I got with transformers backend.

```bash
export TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
export EXP_NAME="${TIMESTAMP}_noquant_lmeval_repro_bs24"
CUDA_VISIBLE_DEVICES=0 nohup lm_eval \
	--model vllm \
    --model_args pretrained=/models/Qwen_Qwen3-32B,dtype=auto,max_model_len=8192,tensor_parallel_size=1 \
    --tasks gsm8k \
    --device cuda:0 \
    --batch_size 24 \
	--apply_chat_template \
	--fewshot_as_multiturn \
    --seed 42 &> ${EXP_NAME}_vllm_template_multiturn_maxlen8192.log &
```

gives

```
|Tasks|Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|-----|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|gsm8k|      3|flexible-extract|     5|exact_match|↑  |0.2199|±  |0.0114|
|     |       |strict-match    |     5|exact_match|↑  |0.0099|±  |0.0027|
```

in line with what people above report.

https://huggingface.co/RedHatAI/Qwen3-32B-quantized.w4a16 reports much better gsm8k results for Qwen3-32B, so either there's been a regression in lm-eval-harness/transformers/vllm/torch, or we're missing something.

### jvonrad · 2025-12-09

Any news on this? :/


### fxmarty-amd · 2025-12-09

@jvonrad I have not tried working again on Qwen3-32B, but maybe https://github.com/EleutherAI/lm-evaluation-harness/issues/3417#issuecomment-3557259320 is relevant here? At least it was very relevant for gpt-oss model. Namely:

- make sure num_gen_toks is high enough
- make sure to enable thinking & properly filter out thinking content from answers
- make sure to apply chat template & fewshot as multiturn
- make sure gsm8k instruction is clear https://github.com/EleutherAI/lm-evaluation-harness/pull/3411 (see https://github.com/EleutherAI/lm-evaluation-harness/issues/2707)
- check out answers rated as incorrect / `[invalid]` regex using `--log_samples` / `--output_path` & see if anything looks wrong here.

To be fair, the Qwen3 paper reports results for the base model, and afaik all we have access to are instruct models. So it is not apple to apple either.

### fxmarty-amd · 2026-02-11

FYI:

```bash
export TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
export PRETRAINED_PATH="/shareddata/Qwen_Qwen3-32B"
export TASKS="gsm8k_platinum"
export LOG_PATH=${PRETRAINED_PATH}/${TIMESTAMP}_lm_eval/results.log
export CUDA_VISIBLE_DEVICES="7"

mkdir ${PRETRAINED_PATH}/${TIMESTAMP}_lm_eval
nohup lm_eval \
  --model vllm \
  --model_args '{"pretrained":"'"${PRETRAINED_PATH}"'","dtype":"auto","tensor_parallel_size":1,"enable_thinking": true,"think_end_token":"</think>"}' \
  --device "cuda" \
  --gen_kwargs max_gen_toks=4096 \
  --tasks ${TASKS} \
  --apply_chat_template \
  --fewshot_as_multiturn \
  --log_samples \
  --output_path ${PRETRAINED_PATH}/${TIMESTAMP}_lm_eval \
  --num_fewshot 5 \
  --batch_size "auto" &> ${LOG_PATH} &
```

on https://github.com/EleutherAI/lm-evaluation-harness/compare/main...fxmarty-amd:lm-evaluation-harness:fix-pretrained-metadata-and-others#diff-3fe4dca0c95a50d9c4be1c410a91df17d1bc9288b5a345207bd81e055d32f3fc

gets me

```
vllm ({'pretrained': '/shareddata/Qwen_Qwen3-32B', 'dtype': 'auto', 'tensor_parallel_size': 1, 'enable_thinking': True, 'think_end_token': '</think>'}), gen_kwargs: ({'max_gen_toks': 4096}), limit: None, num_fewshot: 5, batch_size: auto
|    Tasks     |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|gsm8k_platinum|      3|flexible-extract|     5|exact_match|↑  |0.9843|±  |0.0036|
|              |       |strict-match    |     5|exact_match|↑  |0.9843|±  |0.0036|
```

As mentioned before, `"think_end_token":"</think>"` is critical. https://github.com/EleutherAI/lm-evaluation-harness/pull/3411 helps as well

### wasifmasood · 2026-02-12

Just verified it, its working thanks alot!

### mgillr · 2026-09-26

Diagnosis: this is reasoning-trace interference, in two parts — and the extraction half now has a portable fix in #4249.

**Part 1 — truncation (generation-side):** Qwen3 emits a `<think>…</think>` trace before the answer. The task's stop sequences (GSM8K CoT fewshot delimiters include `\n\n`) occur *inside* the trace, so the harness can cut the generation before any answer exists. The `vllm`/`trtllm` backends accept a `think_end_token` model argument that withholds stops from the engine until after the trace ends; the `hf` backend does not yet have that parity.

**Part 2 — extraction (scoring-side):** the strict-match `#### ` regex has to find the answer through or after the trace. #4249 adds a `strip_think` filter at the task layer — backend-independent (works on `hf`, the backend in your command) — that removes complete and unclosed thinking blocks before downstream extraction:

```yaml
filter_list:
  - name: "strip-thinking"
    filter:
      - function: "strip_think"
      - function: "regex"
        regex_pattern: "#### (-?[0-9.,]+)"
```

Practical settings that close most of the gap to the 0.92 figure today: raise `max_gen_toks` generously (traces are long), `--apply_chat_template`, and compare against flexible-extract — the paper's protocol extracts the answer ignoring the reasoning format.
