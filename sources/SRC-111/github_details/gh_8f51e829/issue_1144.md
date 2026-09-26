# [Issue #1144] The metric labelled TPOT in CSV / console / plot / HTML is `time_per_output_token_ms`, whose formula matches no other benchmarking tool

source: https://github.com/vllm-project/guidellm/issues/1144
state: closed | updated: 2026-09-14T19:52:27Z
labels: 

## 正文

**TL;DR** — Nothing guidellm reports can be quoted directly against a vLLM / SGLang / evalscope **TPOT**. The field *labelled* TPOT uses a formula no other tool uses, and the field that *does* carry the industry formula is aggregated token-weighted rather than request-equal-weighted. The per-request values are already computed and serialized, so closing the gap needs no new measurement.

## The request

**Can guidellm report a TPOT that matches the industry definition — the per-request value, aggregated request-equal-weighted — so a guidellm number can be quoted directly next to a vLLM / SGLang / evalscope one?**

It would not have to replace anything: the existing weighted aggregation can stay exactly as it is.

For reference, that definition is `TPOT = (e2e latency − TTFT) / (output tokens − 1)`, one value per request, aggregated with **every request weighted equally** — vLLM, SGLang and evalscope all compute it that way.

## Why today's numbers don't line up

| What a user wants | Closest guidellm field | Status |
| --- | --- | --- |
| TPOT, per-request value | `inter_token_latency_ms` | ✅ formula matches exactly |
| Avg TPOT | `inter_token_latency_ms.mean` | ❌ token-weighted, not request-equal-weighted |
| p99 TPOT | `inter_token_latency_ms.percentiles.p99` | ❌ token-weighted CDF |
| — | `time_per_output_token_ms` *(the column labelled TPOT)* | ❌ different formula |

Two separate problems, detailed below.

## Problem 1 — the field labelled TPOT uses a formula no other tool uses

[`time_per_output_token_ms`](https://github.com/vllm-project/guidellm/blob/d07502b5/src/guidellm/schemas/base/request_stats.py#L259-L276):

```python
return 1000 * (last_token - start) / output_tokens   # start = request_start
```

Two departures from the industry definition:

- the clock starts at `request_start`, so the value **includes TTFT** — prefill and queue wait get billed to the decode loop
- it divides by `n`, not `n − 1`, counting an interval that does not exist

I could not find this formula in vLLM, SGLang, evalscope, genai-perf or the TensorRT-LLM docs.

It is nevertheless the field behind every TPOT label outside the UI:

| Output | Label | Backed by |
| --- | --- | --- |
| [CSV](https://github.com/vllm-project/guidellm/blob/d07502b5/src/guidellm/benchmark/outputs/csv.py#L450) | `Time per Output Token` | `time_per_output_token_ms` |
| [console](https://github.com/vllm-project/guidellm/blob/d07502b5/src/guidellm/benchmark/outputs/console.py#L469) | `Time per Output Token` | `time_per_output_token_ms` |
| [plot](https://github.com/vllm-project/guidellm/blob/d07502b5/src/guidellm/benchmark/outputs/plot.py#L181) | `tpot_median_ms` / `tpot_p95_ms` | `time_per_output_token_ms` |
| [HTML](https://github.com/vllm-project/guidellm/blob/d07502b5/src/guidellm/benchmark/outputs/html.py#L442) | `tpot_p95_ms` / `tpot_p99_ms` | `time_per_output_token_ms` |

**How far off is it?** The relative gap against the industry TPOT is:

```
time_per_output_token / TPOT − 1  =  TTFT / (n × TPOT) − 1/n
```

It grows with TTFT and shrinks with output length. At TPOT = 150 ms:

| TTFT | Output tokens | guidellm's "TPOT" reads |
| --- | --- | --- |
| 1 s | 128 | +4% |
| 1 s | 16 | +35% |
| 11 s *(a saturated disaggregated run we measured)* | 128 | **+57%** |

TTFT is precisely what grows under load, so the two diverge most in the regime people run benchmarks for.

## Problem 2 — the field with the industry formula is aggregated token-weighted

[`inter_token_latency_ms`](https://github.com/vllm-project/guidellm/blob/d07502b5/src/guidellm/schemas/base/request_stats.py#L280-L297) computes `(last_token − first_token) / (n − 1)` — numerically **exactly** the industry TPOT, since `e2e − TTFT` is `last_token − first_token`. Its per-request value is directly comparable with vLLM's.

Its aggregation is not. [`metrics.py#L1140-L1148`](https://github.com/vllm-project/guidellm/blob/d07502b5/src/guidellm/benchmark/schemas/metrics.py#L1140-L1148):

```python
inter_token_latency_ms=StatusDistributionSummary.from_values_function(
    function=lambda req: (
        req.inter_token_latency_ms or 0.0,
        (req.output_tokens or 1.0) - 1.0,      # <-- weight
    ),
    ...
)
```

With weight `nᵢ − 1`, the mean becomes:

```
Σ(TPOTᵢ × (nᵢ−1)) / Σ(nⱼ−1)  =  (sum of all gaps) / (number of gaps)
```

That is NVIDIA's Avg **ITL**, not Avg TPOT. TensorRT-LLM's deployment guide separates the two explicitly:

> Across different requests, average TPOT is the mean of each request's TPOT (all requests weighted equally), while average ITL is token-weighted (all tokens weighted equally).

The two coincide only when every request has the same output length. On ShareGPT-style traffic the weighted figure leans toward long requests.

## Why this is a reporting gap, not a measurement gap

`inter_token_latency_ms` is a [`@computed_field`](https://github.com/vllm-project/guidellm/blob/d07502b5/src/guidellm/schemas/base/request_stats.py#L278-L280), so **every serialized request already carries its own correct per-request value**. A consumer can recompute a request-equal-weighted TPOT today by iterating `benchmarks[i].requests.*`.

The data is collected and correct — it is just only ever aggregated one way. Adding a request-equal-weighted aggregation is the same `from_values_function` call with the weight tuple dropped.

<details>
<summary><b>Background: how the TPOT column ended up in the non-UI outputs</b></summary>

[#386](https://github.com/vllm-project/guidellm/pull/386) settled the naming for the UI, concluding *"No use of TPOT in the UI"*. The non-UI outputs were not part of that change, and the outputs added afterwards reintroduced a TPOT column backed by the other field:

| Date | Change |
| --- | --- |
| 2025-10-03 | #386 merged — UI unified on ITL |
| 2025-10-31 | Refactor introduced the CSV `Time per Output Token` column |
| 2026-07-15 | [#923](https://github.com/vllm-project/guidellm/pull/923) added `tpot_median_ms` / `tpot_p95_ms` to plots |
| 2026-08-26 | [#1032](https://github.com/vllm-project/guidellm/pull/1032) added `tpot_p95_ms` / `tpot_p99_ms` to the HTML report |

So a user reading a CSV or HTML report today still gets a "TPOT" number, and it is not the one #386 decided the project reports.

</details>

---

#1145 asks the same question for ITL.


## 评论 (1)

### sjmonson · 2026-09-14

Wrong, TPOT is a legacy name. It was originally defined before the industry had started measuring per-token events. We keep it for cases where token streaming is disabled since ITL cannot be calculated in those cases.
