# [Issue #940] Support structured chat content for google/translategemma-12b-it

source: https://github.com/vllm-project/guidellm/issues/940
state: closed | updated: 2026-07-29T15:02:09Z
labels: feature

## 正文

## Problem

Models like `google/translategemma-12b-it` require structured content objects with additional metadata fields in `/v1/chat/completions` requests. TranslateGemma specifically expects `source_lang_code` and `target_lang_code` in each content item:

```json
{
  "role": "user",
  "content": [{
    "type": "text",
    "text": "The quick brown fox jumps over the lazy dog.",
    "source_lang_code": "en",
    "target_lang_code": "es"
  }]
}
```

GuideLLM's chat handler currently only constructs:

```json
{
  "type": "text",
  "text": "..."
}
```

This causes requests to `/v1/chat/completions` to fail with errors like `'dict object' has no attribute ...` (HTTP 400) because the model's chat template expects the language metadata fields.

## Current Workaround

Using `/v1/completions` endpoint works for raw throughput benchmarking but does not exercise the model's intended translation workflow.

## Expected Behavior

GuideLLM should support passing additional metadata fields in structured chat content objects, either via:

1. A custom dataset where each prompt can include the required structured object, with GuideLLM preserving extra fields like `source_lang_code` and `target_lang_code` when constructing the chat request.
2. A CLI option or config to specify extra fields to include in content objects (e.g. `--content-fields '{"source_lang_code": "en", "target_lang_code": "es"}'`).

## Reproduction

```bash
guidellm benchmark \
    --target 'http://localhost:8000' \
    --model google/translategemma-12b-it \
    --data='{"prompt_tokens":1000,"output_tokens":1000}' \
    --rate-type concurrent \
    --rate 1 \
    --max-seconds 60 \
    --request-format /v1/chat/completions
```

This fails because the generated chat messages are missing the required language metadata fields.

## 评论 (3)

### Pragadeesh122 · 2026-07-20

 Hey guys @aas008 @dbutenhof 👋 — I'd like to pick this up and work on it. I'll open a PR referencing the issue.

### Prasannajaga · 2026-07-22

/assign 

### Prasannajaga · 2026-07-22

Hey @aas008  I have raised a PR for this! I didn't run a live model server for testing since the request formatting and preprocessors are covered through unit test cases. Unfortunately, I don't have a GPU in my local setup to run TranslateGemma locally (sorry about that!). Could you checkout this [gemma-payload-upgrade](https://github.com/Prasannajaga/guidellm/tree/bug/gemma-payload-upgrade) branch and let me know whether this is working on your setup?


