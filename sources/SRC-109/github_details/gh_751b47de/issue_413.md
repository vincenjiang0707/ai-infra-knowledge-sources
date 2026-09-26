# [Issue #413] Using `--streaming` does not respect `--extra-inputs "{\"stream_options\":{\"include_usage\":true}}"`

source: https://github.com/triton-inference-server/perf_analyzer/issues/413
state: open | updated: 2026-04-07T04:39:52Z
labels: 

## 正文

Command:
```
      genai-perf analyze --random-seed ${seed}
      --service-kind openai --endpoint-type chat --streaming
      --url ${llm_host} -m ${model}
      --extra-inputs ignore_eos:true
      --extra-inputs seed:${seed}
      --extra-inputs temperature:0
      --extra-inputs "{\"chat_template_kwargs\":{\"enable_thinking\":false}}"  
      --extra-input"{\"stream_options\":{\"include_usage\":true}}"
      --extra-inputs max_tokens:${output_sequence_length}
      --extra-inputs min_tokens:${output_sequence_length}
      --output-tokens-mean ${output_sequence_length} --output-tokens-stddev ${stddev}
      --synthetic-input-tokens-mean ${input_sequence_length} --synthetic-input-tokens-stddev ${stddev}
      -v --measurement-interval ${duration_msec}
      --warmup-request-count 10
      --num-dataset-entries ${max_number_of_unique_payloads}
      --profile-export-file ${input_sequence_length}_${output_sequence_length}.json
      --sweep-type concurrency --sweep-list ${threads} --generate-plots
```

Error:
```
  File "/usr/local/lib/python3.12/dist-packages/genai_perf/profile_data_parser/llm_profile_data_parser.py", line 441, in _extract_openai_text_output
    completions = data["choices"][0]
                  ~~~~~~~~~~~~~~~^^^
IndexError: list index out of range
```


## 评论 (1)

### khrd · 2026-04-07

## Additional context and proposed fix

We encountered this same issue while benchmarking vLLM (Llama 3.1 8B on NVIDIA H200) using genai-perf 0.0.13 (Triton SDK 25.04).

### Our setup

We use an Envoy-based external processing (ExtProc) proxy (Semantic Router) in front of vLLM for request routing and guardrail evaluation. The proxy automatically injects `stream_options.include_usage=true` into all streaming requests before forwarding them to vLLM. This means even without the user explicitly passing `--extra-inputs`, the upstream server receives `include_usage=true`.

When profiling through this proxy with `--streaming`, genai-perf crashes with:

```
IndexError: list index out of range
  File "llm_profile_data_parser.py", line 467, in _extract_openai_chat_text_output
    completions = data["choices"][0]
```

### Root cause

When `stream_options.include_usage=true` is set, vLLM sends a final SSE chunk per the OpenAI API specification:

```json
data: {"object":"chat.completion.chunk","choices":[],"usage":{"prompt_tokens":45,"total_tokens":65,"completion_tokens":20}}
```

The `choices` array is intentionally empty in this usage-reporting chunk. However, `_extract_openai_chat_text_output` unconditionally accesses `data["choices"][0]`, causing the `IndexError`.

### Impact

This affects not just explicit `--extra-inputs` usage but any deployment where a proxy, gateway, or middleware injects `include_usage=true` — a common pattern in production LLM serving stacks.

### Proposed fix (3 locations in `llm_profile_data_parser.py`)

**1. `_extract_openai_chat_text_output`:**
```diff
-        completions = data["choices"][0]  # type: ignore
+        choices = data.get("choices", [])
+        completions = choices[0] if choices else {}
         ...
         elif data["object"] == "chat.completion":  # non-streaming
-            return completions["message"].get("content", "")
+            if not completions or "message" not in completions:
+                return ""
+            return completions["message"].get("content", "")
         elif data["object"] == "chat.completion.chunk":  # streaming
-            return completions["delta"].get("content", "")
+            if not completions or "delta" not in completions:
+                return ""
+            return completions["delta"].get("content", "")
```

**2. `_extract_openai_completion_text_output`:**
```diff
-        completions = data["choices"][0]  # type: ignore
+        choices = data.get("choices", [])
+        completions = choices[0] if choices else {}
```

**3. `_preprocess_response` (merge block):**
```diff
         if self._response_format == ResponseFormat.OPENAI_COMPLETIONS:
-            data["choices"][0]["text"] = merged_text
+            if data.get("choices"):
+                data["choices"][0]["text"] = merged_text
         else:
-            data["choices"][0]["delta"]["content"] = merged_text
+            if data.get("choices") and "delta" in data["choices"][0]:
+                data["choices"][0]["delta"]["content"] = merged_text
```

We've verified this patch resolves the issue — streaming profiling through our proxy now works correctly and produces valid TTFT/ITL metrics. Happy to open a PR if this approach looks reasonable.
