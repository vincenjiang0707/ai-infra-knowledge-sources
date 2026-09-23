# [Issue #4743] [Bug] INT4 KV cache (--quant-policy 4) breaks qwen3coder tool call parser for Qwen3-Coder-30B

source: https://github.com/InternLM/lmdeploy/issues/4743
state: closed | updated: 2026-08-04T04:44:49Z
labels: awaiting response, Stale

## 正文

## Describe the bug

When deploying `Qwen3-Coder-30B-A3B-Instruct-AWQ_QuantTrio` with INT4 KV cache quantization (`--quant-policy 4`), the `qwen3coder` tool call parser fails to extract structured tool calls from model output. The same model with INT8 KV cache (`--quant-policy 8`) works perfectly.

## Environment

- LMDeploy: 0.14.0
- Model: Qwen3-Coder-30B-A3B-Instruct-AWQ_QuantTrio
- Hardware: 4xV100-SXM2-16GB (tp=4), CUDA 12.6

## Reproduction

```bash
lmdeploy serve api_server /models/Qwen3-Coder-30B-A3B-Instruct-AWQ_QuantTrio \
  --tp 4 --cache-max-entry-count 0.7 --dtype float16 \
  --enable-prefix-caching --session-len 262144 \
  --tool-call-parser qwen3coder --quant-policy 8  # change to 4 -> broken
```

## Expected vs Actual

| | INT8 (`--quant-policy 8`) | INT4 (`--quant-policy 4`) |
|---|---|---|
| `tool_calls` returned | structured JSON | empty list `[]` |
| `content` field | empty | raw text with XML tags |
| MTCSR chain_success | 5/6 (83.3%) | 0/6 |

## Root cause analysis

INT4 KV cache quantization causes the model to stop emitting the expected XML tool call format. The `qwen3coder` parser expects output in the format `

## 评论 (3)

### windreamer · 2026-07-09

Hi @zambalee 

Thank you for the detailed report!
This behavior is likely **not a framework bug** in LMDeploy, but rather a consequence of **aggressive KV cache quantization severely degrading model quality and instruction-following capability** , which in turn breaks the tool call parser.

## Root Cause Analysis

The qwen3coder tool call parser relies on the model output strictly adhering to expected structured formats (typically specific XML/JSON tags or function call syntax). When KV cache uses INT4 quantization (--quant-policy 4), quantization errors accumulate across long sequences, leading to:

1.  Degraded instruction following: The model may deviate from the tool call format specified in the system prompt, generating incomplete or malformed call blocks
2.  Critical token probability shifts: The logits determining structured output boundaries (e.g., <tool_call>, </tool_call>, etc.) are perturbed, causing the parser to fail to match expected patterns
3.  Reduced long-context stability: With your 262K session length, the error accumulation effect of INT4 becomes more pronounced over extended sequences

## Why INT8 Works

INT8 offers 4× the representational precision compared to INT4 (256 vs. 16 discrete values). The quantization loss on attention Key/Value vectors stored in KV cache is substantially smaller, sufficient to preserve the model's format adherence in tool calling scenarios.

## Recommendations

•  For production tool calling: We recommend keeping --quant-policy 8 or higher precision
•  To verify: You can also run some non-tool-calling complex instruction-following tasks (e.g., long-form summarization, structured output generation) under INT4 and observe if similar quality degradation occurs. This would further confirm that the issue stems from quantization-induced capability loss rather than parser logic


Thank you again for your careful comparative testing across different quantization policies — this kind of controlled experiment is extremely valuable to the community! If you encounter parser anomalies even under INT8, please feel free to follow up and we can investigate the parser logic further.

### github-actions[bot] · 2026-07-30

This issue is marked as stale because it has been marked as invalid or awaiting response for 7 days without any further response. It will be closed in 5 days if the stale label is not removed or if there is no further response.

### github-actions[bot] · 2026-08-04

This issue is closed because it has been stale for 5 days. Please open a new issue if you have similar issues or you have any new updates now.
