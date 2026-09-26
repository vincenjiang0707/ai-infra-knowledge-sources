# [Issue #2433] [Bug :bug:]: SGLang PD guide (prefill TP1 / decode TP4) fails on gpt-oss-120b; GKE SGLang nightly has never passed

source: https://github.com/llm-d/llm-d/issues/2433
state: closed | updated: 2026-09-10T17:53:24Z
labels: 

## 正文

### What happened?

The nightly "PD Disaggregation E2E (GKE GPU SGLang)" has never passed. https://github.com/llm-d/llm-d/actions/workflows/nightly-e2e-pd-disaggregation-gke-acc-gpu-sglang-x.yaml 

The guide config (guides/pd-disaggregation/modelserver/gpu/sglang, prefill TP1 x8, decode TP4 x2) uses different TP sizes for prefill and decode, and sglang rejects this combination for gpt-oss-120b at KV transfer time (log below). The error is only returned to the sidecar, so the client sees a hang instead of an error.

Verified on a GKE H200 cluster with a minimal 1P1D deployment of the same guide: with prefill TP1 / decode TP1 the same request completes in ~5s through the EPP, including cross-node KV transfer.

### Version
modelserver image docker.io/lmsysorg/sglang:v0.5.16

### Area

Prefill/Decode Disaggregation

### Relevant log output

```
# prefill pod
Unexpected transfer worker error for room 1788380104266545413
Traceback (most recent call last):
  File "/sgl-workspace/sglang/python/sglang/srt/disaggregation/nixl/conn.py", line 1153, in transfer_worker
    state_xfer_handles = self.maybe_send_extra(
  File "/sgl-workspace/sglang/python/sglang/srt/disaggregation/nixl/conn.py", line 2062, in maybe_send_extra
    raise RuntimeError(
RuntimeError: PD Disaggregation does NOT support PD different TP sizes for non-MLA SWA hybrid models yet.
Prefill transfer failed for request rank=0 req.rid='5b02aee35dae49aba98a333ce89964e6' with exception PD Disaggregation does NOT support PD different TP sizes for non-MLA SWA hybrid models yet.
INFO: 10.60.17.27:54838 - "POST /v1/completions HTTP/1.1" 500 Internal Server Error

# decode pod, ~70s later, all 4 ranks
Decode transfer failed for request rank=0 decode_req.req.rid='a1af5d2d90324da292ed07c52b30467b' decode_req.req.bootstrap_room=1788380104266545413 with exception KVTransferError(bootstrap_room=1788380104266545413): Aborted by AbortReq.
```


## 评论 (3)

### capri-xiyue · 2026-09-03

@rahulgurnani As you work on sglang, can you help fix this?

### rahulgurnani · 2026-09-03

/assign

### rahulgurnani · 2026-09-10

subsequent run seems to have passed: https://github.com/llm-d/llm-d/actions/runs/34371511899
