# [Issue #1145] `inter_token_latency_ms` is a per-request average, not an inter-token latency — the per-interval data is never recorded

source: https://github.com/vllm-project/guidellm/issues/1145
state: closed | updated: 2026-09-14T19:52:38Z
labels: 

## 正文

**TL;DR** — What guidellm reports as ITL is a **per-request average**, not an inter-token latency. vLLM, SGLang and evalscope all define ITL as the measured gap between consecutive streamed outputs, one sample per gap. guidellm keeps only the first and last token timestamp per request, so the per-interval data needed for that never exists — and the tail of the gap distribution is the only place a decode stall is visible.

## The request

**Can guidellm report an ITL that matches the industry definition — one sample per measured gap between consecutive streamed outputs, pooled across requests — so a guidellm number can be quoted directly next to a vLLM / SGLang / evalscope one?**

One semantic would need settling first, since the ecosystem differs. For a chunk carrying several tokens (speculative decoding):

| Tool | Rule |
| --- | --- |
| vLLM | records **one** sample — *"the tokens in the same output do not create additional ITL samples"* |
| genai-perf | divides the gap by that chunk's token count |
| SGLang | `use_retokenized_itl` replicates the sample k times |

Whichever guidellm picked would determine whose ITL its number is comparable with.

## What ITL means elsewhere vs. here

| | Sample | Per request |
| --- | --- | --- |
| **Industry ITL** (vLLM / SGLang / evalscope) | one measured gap between streamed outputs | ~n−1 samples |
| **guidellm `inter_token_latency_ms`** | `(last_token − first_token) / (n − 1)` | **1 sample** (an average) |

vLLM's benchmark docs state it directly:

> Inter-token latency (ITL) records the time between consecutive streamed outputs. The reported ITL statistics aggregate these **individual gaps** across all successful requests.

guidellm's [`inter_token_latency_ms`](https://github.com/vllm-project/guidellm/blob/d07502b5/src/guidellm/schemas/base/request_stats.py#L280-L297) is one value per request — a per-request average, which is why it is numerically the industry's *TPOT*, the subject of #1144.

## Why the distinction matters

A request that streams 500 tokens at 10 ms and stalls once for 800 ms:

| | Samples contributed | Value |
| --- | --- | --- |
| per-request average | 1 | `(499×10 + 800)/500` ≈ **11.6 ms** — indistinguishable from healthy |
| per-interval (real ITL) | 500 | 499 × 10 ms **+ one 800 ms sample in the tail** |

**No re-weighting recovers that stall** — it is averaged away *before* the value ever enters the distribution.

This is why llm-d's runbooks alert on `histogram_quantile(0.99, vllm:inter_token_latency_seconds)`, annotated *"High ITL causes choppy output"*. It matters most for prefill/decode-disaggregated deployments, where KV transfer and decode-side scheduling produce exactly this kind of periodic stall — the case we ran into.

Sample size differs by orders of magnitude too: a stage of 509 requests × 128 output tokens yields **509** samples for the per-request metric (its p99 rests on 5 requests) and **~64,000** for a real ITL.

## Why aggregation alone cannot fix it

Only two timestamps are kept per request — `first_token_iteration` and `last_token_iteration` ([`info.py#L22`](https://github.com/vllm-project/guidellm/blob/d07502b5/src/guidellm/schemas/base/info.py#L22)). Everything in between is reconstructed ([`request_stats.py#L445-L451`](https://github.com/vllm-project/guidellm/blob/d07502b5/src/guidellm/schemas/base/request_stats.py#L445-L451)):

```python
# evenly space the iterations since we don't have per-iteration timings
# / we don't know the individual token counts per iteration
iter_times = np.linspace(first_token_iteration, last_token_iteration, num=token_iterations)[1:]
```

Those gaps are constant by construction, so no per-interval statistic can be derived from them.

**The inputs are available, though.** The streaming loop already timestamps every chunk ([`http.py#L352`](https://github.com/vllm-project/guidellm/blob/d07502b5/src/guidellm/backends/openai/http.py#L352)) and knows from `add_streaming_line`'s return value how many tokens it carried. Today that timestamp is only used to overwrite `last_token_iteration` ([`#L384`](https://github.com/vllm-project/guidellm/blob/d07502b5/src/guidellm/backends/openai/http.py#L384)) — so the gaps are **discarded rather than unavailable**.

<details>
<summary><b>Background: this issue questions #386's premise</b></summary>

[#386](https://github.com/vllm-project/guidellm/pull/386) unified the labels on ITL, on the grounds that *"The data we had previously happened to be ITL data"*.

That premise holds **at the mean level only**. The token weighting applied at aggregation ([`metrics.py#L1140-L1148`](https://github.com/vllm-project/guidellm/blob/d07502b5/src/guidellm/benchmark/schemas/metrics.py#L1140-L1148)) does make the mean equal Avg ITL: `Σ(TPOTᵢ × (nᵢ−1)) / Σ(nⱼ−1)` is `(sum of all gaps) / (number of gaps)`.

It does not hold for the percentiles. The weighted CDF sorts **requests** (one value each) and merely sizes each request's slice by its token count, so `.percentiles.p99` is the 99th percentile *of per-request averages*, not of gaps.

</details>

## On the naming

If a per-interval ITL is added, the current `inter_token_latency_ms` would be holding the name of a metric it is not. That question belongs with #1144, since the same field is also the only one carrying the industry's TPOT formula.


## 评论 (1)

### sjmonson · 2026-09-14

While the definition you gave is valid, it is by no means an "industry standard" and has issues of its own. The other well-known client-side tools conform to how we do it ([inference-perf](https://github.com/kubernetes-sigs/inference-perf/blob/1952438c2ec4ad1189290412b4f9cf16ff966120/inference_perf/reportgen/base.py#L659-L664), [aiperf](https://github.com/ai-dynamo/aiperf/blob/7db2ba37a62aa80c882bc90eaf61cc8073e2387b/src/aiperf/metrics/types/inter_token_latency_metric.py#L19)). The issue is when looking from a client-side perspective individual token events are far too noisy to make sense of, even a small blip in packet delay to the client can show up as a large regression since the delays involved in are so minuscule. For larger regressions like the one you gave as example, the delay would should up in E2E latency so the tradeoff of losing request readability is not worth it.

Personally I do wish the industry had settled on a distinct difference for this back in the day. Perhaps AITL (Average Inter-Token Latency) would have made sense. It is on our roadmap to re-introduce per-token latencies into the metrics collector so perhaps we can introduce a "true" ITL down the line, but for now our ITL is staying defined as is.
