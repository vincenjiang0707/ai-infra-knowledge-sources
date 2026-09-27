# [Issue #3196] confuse about log_samples : Option to preserve thinking/reasoning traces in model outputs when using --log_samples

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3196
state: open | updated: 2026-09-26T16:32:42Z
labels: 

## 正文

# Problem Description
When using DeepSeek-R1 and other reasoning models that generate thinking chains, the framework automatically strips <think> content from the outputs. Specifically:

In the vLLM backend, it calls the postprocess_generated_text function
This function removes thinking content based on the think_end_token parameter:
Similarly, the HuggingFace backend has the same processing:

# Desired Feature
I would like to request adding an option (such as --preserve_thinking or a sub-option within --log_samples) that allows users to choose to retain the complete model output, including chain-of-thought content, maily for academia research :Analyzing model reasoning processes, Studying thought chain quality,Debugging and enhancing prompt engineering
# Potential Solutions

Add a new command-line parameter to control whether thought content is preserved
Save both raw and processed outputs when logging samples
Provide an option to not set the think_end_token parameter


Definition of think_end_token parameter: vllm_causallms.py:140
Post-processing function: utils.py:857-883

## 评论 (13)

### hhh2210 · 2025-07-31

If possible, I can write the code myself, just make sure there's no other way to solve the COT trace issue

### baberabb · 2025-07-31

> If possible, I can write the code myself, just make sure there's no other way to solve the COT trace issue

Hi! This does sound like something we should support, though the integration is a bit tricky with the current architecture. A quick workaround could be to cache the original generations [here](https://github.com/EleutherAI/lm-evaluation-harness/blob/4f8195f18fbc1b6d212314509d7525e1178e036c/lm_eval/models/huggingface.py#L1486) (use with `--use_cache`), rather than after they are truncated. Similar logic for `vllm`. Cache is a simple sqlitedict defined [here](https://github.com/EleutherAI/lm-evaluation-harness/blob/4f8195f18fbc1b6d212314509d7525e1178e036c/lm_eval/api/model.py#L226), and you can use the tuple of the args from the sample file as keys to map them back.

### hhh2210 · 2025-08-01

Thanks for your reply!
I can test this solution on weekends.
> Hi! This does sound like something we should support, though the integration is a bit tricky with the current architecture. A quick workaround could be to cache the original generations [here](https://github.com/EleutherAI/lm-evaluation-harness/blob/4f8195f18fbc1b6d212314509d7525e1178e036c/lm_eval/models/huggingface.py#L1486) (use with --use_cache), rather than after they are truncated. Similar logic for vllm. Cache is a simple sqlitedict defined [here](https://github.com/EleutherAI/lm-evaluation-harness/blob/4f8195f18fbc1b6d212314509d7525e1178e036c/lm_eval/api/model.py#L226), and you can use the tuple of the args from the sample file as keys to map them back.

But also want to ask, if I directly use the old version of lm_eval or delete the "strip" related functions, would this affect the model evaluation results(e.g., Exact Match metrics)?
@baberabb 

### hhh2210 · 2025-08-03

I found the“ --cache” option a bit inconvenient as it involves databases handling. I modified the code using a different jsonl approach. The details are at:
https://github.com/EleutherAI/lm-evaluation-harness/pull/3204
How about that?

### hhh2210 · 2025-08-08

Hello, sorry to bother you, any updates or advice?
@baberabb 
I'd like to know what the developer team thinks about this issue, and I'm very eager to participate in the subsequent feature development and implementation

### Co-Cl2 · 2025-11-02

Hello everyone,
@baberabb  @hhh2210 
I'd also like to express my support for developing this feature. May I ask if there are any plans to add this to the development schedule in the near future?

### hhh2210 · 2025-11-03

nope, i develop a hf-transformer version kind of works, you can check it at https://github.com/EleutherAI/lm-evaluation-harness/pull/3204

### Co-Cl2 · 2025-11-04

@hhh2210 Thank you! But I have temporarily implemented this logic on my own at the moment, because I also need to solve another problem revealed in #3382 at the same time.

### hhh2210 · 2025-11-04

@Co-Cl2 ok, what's your solution? i think you can make the folk public and maybe raise a PR(no matter the code owner have the time to review)

### Co-Cl2 · 2025-11-07

@hhh2210 #3386 This is the PR of the solution I have conceived. Thank you for your suggestions.

### hhh2210 · 2025-11-08

@Co-Cl2 
Got it! Could you share a few more details on how you handled the logging behavior fix? Super curious about what approach you took and whether it affects metrics caculatro or caching interacts with the outputs.

### Co-Cl2 · 2025-11-09

@hhh2210 Here is a description of the changes I made, as detailed in my PR:

I have deprecated the original think_end_token parameter. Instead, I now pass both think_start_token and think_end_token into the task's config via metadata.

The logic for stripping the Chain-of-Thought (CoT) is now executed within the filter section, using these parameters from the config.

As a result of this implementation:

filtered_resp now holds the result after the CoT stripping and the answer-extraction filter have been applied.

resp remains in its state before the filter logic is executed. (If the original think_end_token parameter was not set, resp is just the raw model output).

This implementation is just for reference; I don't think it's a very good approach 🙂.

In addition, since this behavior is implemented directly within the filter logic, I don't believe it will affect how caching interacts with the outputs.

Regarding the metrics calculator, it is based on the filtered_resp. Based on my observations, the filtered_resp is being generated in the correct format, so the calculations should be accurate.

### mgillr · 2026-09-26

Fix in #4250.

**Diagnosis confirmed:** the stripping happens inside the backends (vLLM and TRT-LLM call `postprocess_generated_text` with `think_end_token` before the response ever reaches the logging layer), so `--log_samples` could only ever see the cleaned output — the raw trace was discarded at generation time.

**Fix:** `Instance` now carries a `raw_resps` field alongside `resps`. The vLLM backend captures the unmodified generation before stripping and attaches it to the request; the evaluator includes it in logged samples whenever present. Your three proposed options are covered by the second shape you suggested — both outputs are saved; nothing is lost, no new flag needed.

Companion PR #4249 adds a `strip_think` filter at the task layer (backend-independent trace removal for extraction), which together with this closes the reasoning-model analysis loop.
