# [Issue #3572] [Bug]: rl.yml defaults to hardcoded Gemma chat template, causing degenerate loops in LLaMA 3 GRPO

source: https://github.com/AI-Hypercomputer/maxtext/issues/3572
state: closed | updated: 2026-04-28T20:22:10Z
labels: bug

## 正文

### Bug report

When running the GRPO post-training pipeline (configs/post_train/rl.yml) with a non-Gemma model like LLaMA 3.1, the training loop silently fails and results in 0.0 rewards due to a hardcoded chat template.

### Logs/Output

The Problem:
In rl.yml, the chat_template_path defaults to maxtext/examples/chat_templates/gsm8k_rl.json. This JSON file hardcodes Google's <start_of_turn> and <end_of_turn> tokens into the "TEMPLATE" string.

When training a LLaMA 3 model, feeding it <start_of_turn> causes the model to panic, hallucinate its format, and fall into a degenerate repetition loop (e.g., repeatedly outputting <start_of_turn>user until generation is cut off). The reward function fails to extract <answer>, resulting in a 0 reward and a broken actor.

### Environment Information

Hardware: TPU v5e-8 slice via GKE

### Additional Context

The Workaround:
I was able to fix this and successfully train the model by creating a custom llama3_rl.json file using LLaMA's native <|start_header_id|> tokens, and passing it via chat_template_path=/path/to/llama3_rl.json.

Suggested Fixes:

Short term: Add a llama3_gsm8k_rl.json to the examples/chat_templates/ folder and document how to swap it in the RL tutorial.

Long term: Deprecate the hardcoded JSON templates entirely and allow the pipeline to dynamically build the prompts using the model's native tokenizer.chat_template from Hugging Face.

## 评论 (2)

### A9isha · 2026-04-10

Hi @karajendran , thank you for raising this bug. 

Yes, please feel free to add new json as you deem fit - this is the expectation. We had tested with Llama3.1-8b/Llama3.1-70b/Qwen3 and the current template worked fine. 

For rewards, for RL training we have seen that depending on the template for the rewards is insufficient. So, are moving away from it in our latest WIP PR - we would only look for `<answer> </answer>`. But of course in your case it seems like the model's generation is bad, then rewards are meant to become 0 here without fixes to the template.

### A9isha · 2026-04-28

Closing this bug now, @karajendran please feel free to reopen/open a new one if you see further issues.
