# [Issue #2439] [Bug :bug:]: wide-ep-lws precise variant renders 404, silently disabling precise routing

source: https://github.com/llm-d/llm-d/issues/2439
state: open | updated: 2026-09-04T16:46:48Z
labels: bug

## 正文

### What happened?

The `wide-ep-lws` precise prefix-cache routing variant deploys a render Service that owns no pods of its own: it selects the prefill model server pods and forwards `/v1/*/render`, which the EPP `token-producer` calls to tokenize every prompt.

vLLM serves those endpoints only when `VLLM_ENABLE_SCALE_OUT_ENDPOINTS=1`. The scale-out endpoints (`/render`, `/derender`, `/inference/v1/generate`) became opt-in in [vllm-project/vllm#54579](https://github.com/vllm-project/vllm/pull/54579), merged 2026-09-02, which is after the v0.28.0 release. The guide deploys `docker.io/vllm/vllm-openai:nightly` through `recipes/modelserver/components/images/gpu-vllm/nightly`, so it picks up the gate.

The result is that every render call returns 404:

```
"failed to prepare per request data",
"error": "DataProducer \"token-producer/token-producer\" failed: tokenization failed: vLLM render returned status 404: {\"detail\":\"Not Found\"}"
```

The failure is silent. No request carries token IDs, so the precise producer never runs and the KV-block index stays empty, but the remaining scorers still answer 200. The deployment looks healthy: pods are Ready, the EPP holds all 24 KV-event subscriptions, and requests succeed. Only the feature the variant exists for is inert.

On a GLM-5.3 cell, the same workload completed 2,269 requests with rendering broken against 2,853 with it working, about 26% less throughput, because routing was effectively cache-blind.

**Expected:** the precise variant tokenizes through the render Service and the precise producer populates the index, or the deployment fails loudly if it cannot.

**Affected:** `guides/wide-ep-lws`, precise variant (`modelserver/gpu/vllm-glm-5.2/deployments/p2w1d1w1-precise` plus `render/`), on any vLLM build after 2026-09-02.

**Not affected:** `guides/precise-prefix-cache-routing` uses the same podless Service pattern, but pins `v0.26.0`, which predates the gate. Its README carries the same now-conditional claim that `vllm serve` already exposes `/v1/*/render`, so it will hit this whenever its pin moves past the gate.

**Proposed fix:** set the opt-in on the prefill pods the Service selects, through a modelserver component applied by the precise overlay, and correct the render manifests and README, which state that no model-server flag is needed. Builds that predate the gate ignore the variable, so it is version-safe. Note that [vllm-project/vllm#55176](https://github.com/vllm-project/vllm/pull/55176) proposes replacing the variable with an `--enable-scale-out` flag, so this may need revisiting.

The guide's existing render verification step already catches the condition, but does not say what a 404 there means.

### Version

`guides/wide-ep-lws` at `080c14d9`, model server image `docker.io/vllm/vllm-openai:nightly` (0.28.1rc1)

### Area

Documentation / Guides

### Relevant log output

```
$ curl -s http://<prefill-pod>:8000/openapi.json | jq '.paths | keys | map(select(contains("render") or contains("tokenize")))'
["/detokenize", "/tokenize"]

$ vllm launch render <model> --port 8999   # same image, render server
["/tokenize","/detokenize","/v1/chat/completions/render","/v1/messages/render","/v1/completions/render", ...]
```

cc @vMaroon @sagearc


## 评论 (1)

### nilig · 2026-09-04

cc @vMaroon @sagearc

Flagging because the failure mode is silent: with the render call returning 404 the precise producer never runs and the index stays empty, but pods are `Ready`, the EPP holds all its KV-event subscriptions, and requests still return 200. A cell looks healthy while routing cache-blind.

The fix is a one-line opt-in (`VLLM_ENABLE_SCALE_OUT_ENDPOINTS=1`) on the prefill pods the render Service selects. PR shortly.
