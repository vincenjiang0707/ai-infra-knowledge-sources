source: https://github.com/vllm-project/guidellm/commit/85be37fbdd0f038f76244ca2a5e4c2dc2d27bbc6

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert

| Unknown or mixed |`prompt_tokens=1000,output_tokens=1000`| All metrics|

113

113

114

114

If you have real production data, use it instead of synthetic. GuideLLM supports custom datasets via JSONL files or HuggingFace datasets — see the [Datasets guide](../guides/datasets.md) for details.

115

115

@@ -118,15 +118,17 @@ If you have real production data, use it instead of synthetic. GuideLLM supports

118

118

The benchmark results can guide server configuration:

119

119

120

120

**Prefill-bound (high TTFT):**

121

+

121

122

- Enable chunked prefill (`--enable-chunked-prefill`) to overlap prefill with decode

122

123

- Increase tensor parallelism to spread the prefill computation across GPUs

123

124

- Consider a shorter `--max-model-len` if your prompts don't need the full context window

124

125

125

126

**Decode-bound (high ITL):**

127

+

126

128

- Check if you are memory-bandwidth limited — larger batch sizes help divide memory reads

Copy file name to clipboardExpand all lines: docs/examples/example_template.md

+8-6Lines changed: 8 additions & 6 deletions

Display the source diff

Display the rich diff

Original file line number

Diff line number

Diff line change

@@ -22,7 +22,7 @@ guidellm run \

22

22

--output kind=json,path=___.json

23

23

```

24

24

25

-

[Explain what each non-obvious flag does in the context of this example. Don't repeat what the getting-started docs already cover. **Focus on why these specific values were chosen** for this use case.]

25

+

\[Explain what each non-obvious flag does in the context of this example. Don't repeat what the getting-started docs already cover. **Focus on why these specific values were chosen** for this use case.\]

26

26

27

27

## Step 2: [Run / Execute]

28

28

@@ -32,8 +32,8 @@ guidellm run \

32

32

33

33

[Explain how to interpret the metrics/results, highlighting what to take away (good and the bad)]

|`output_tokens_per_second` (mean) | Server throughput — how much work is getting done |

36

+

|`time_to_first_token_ms` (p50) | Typical user-perceived wait before they receive a response |

37

+

|`time_to_first_token_ms` (p99) | Worst-case wait — important for tail latency SLOs|

38

+

|`inter_token_latency_ms` (p50) | How smooth the streaming experience feels|

39

+

|`request_latency` (p50) | Total end-to-end time per request|

40

40

41

41

## Step 3: Identify the Three Zones

42

42

@@ -98,18 +98,18 @@ Here is what a real sweep looks like.

98

98

99

99

Results collected using **meta-llama/Llama-3.1-8B-Instruct** on a single **NVIDIA A100 80GB** GPU, served by vLLM with chunked prefill enabled. Workload: 1000 input tokens, 1000 output tokens.

In this example, throughput scales linearly from concurrency 1 through ~11 (under-utilized). Between concurrency 15 and 34, throughput is still climbing but TTFT and ITL are creeping up (sweet spot). At concurrency 46, throughput gains flatten while latency continues rising — and the throughput strategy shows TTFT exploding to ~10 seconds, confirming over-saturation.

## 0 commit comments