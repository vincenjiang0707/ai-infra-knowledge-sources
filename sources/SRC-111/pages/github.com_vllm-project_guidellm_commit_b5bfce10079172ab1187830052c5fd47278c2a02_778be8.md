source: https://github.com/vllm-project/guidellm/commit/b5bfce10079172ab1187830052c5fd47278c2a02

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert

Copy file name to clipboardExpand all lines: docs/guides/trace_replay.md

+1-1Lines changed: 1 addition & 1 deletion

Display the source diff

Display the rich diff

Original file line number

Diff line number

Diff line change

@@ -160,7 +160,7 @@ Replay against `/v1/chat/completions` (the backend default). OTEL stores chat-co

160

160

161

161

Recorded tool loops are pre-split onto GuideLLM's client tool-call pipeline. An LLM span whose output messages contain `tool_calls` (or `gen_ai.response.finish_reasons` of `tool_calls` / `tool_call` / `tool_use` / `function_call`) becomes `client_tool_call`. The next span is consumed as `tool_response_injection` when its new messages after `input[i] + output[i]` are only `role=tool` results. Recorded result strings are rebound to **live**`tool_call_id`s by the chat handler. `gen_ai.tool.definitions` supplies `tools_column` on those turns (otherwise the default synthetic tool is used); definitions alone do not classify a turn. Injection parents always use `history_context=full`, including `history=trace`. Missing-tool policy stays `--backend tool_call_missing_behavior=...`.

162

162

163

-

If the next span cannot be parsed as tool results, a placeholder injection is synthesized (using a following `execute_tool` span's result when present) and that next spanis still replayed.

163

+

If the next span cannot be parsed as tool results, a placeholder injection is synthesized and that next span is still replayed. A following `execute_tool` span supplies the injection text and pacing when it is a descendant of the tool-call LLM span, or a sibling sharing a non-null `parent_span_id` until the next LLM with that parent. Otherwise the synthetic placeholder is used at the call timestamp.

164

164

165

165

Completed request stats merge response usage over the request's expected token counts, so a dedicated expected-vs-actual MAE is not reported. Compare `request.input_metrics` / `output_metrics` (span counts) with response usage before that merge if you need the deviation.

## 0 commit comments