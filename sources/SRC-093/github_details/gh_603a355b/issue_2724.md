# [Issue #2724] [Bug] vLLM/TRT-LLM PD paths still re-serialize the request body via map[string]any, breaking prompt_token_ids stability and prefix-cache reuse

source: https://github.com/vllm-project/aibrix/issues/2724
state: closed | updated: 2026-09-17T02:52:31Z
labels: kind/bug, area/gateway, area/kv-cache

## 正文

### 🐛 Describe the bug

#2475 / #2476 fixed the SGLang PD path so that the prefill and decode request
bodies are derived with byte-level `sjson` edits. The same `map[string]any`
round trip still exists on every other PD path on `main` (d16d8245):

1. `prefill.PreparePayload` unmarshals `routingCtx.ReqBody` into
   `map[string]any` for every engine that does not implement
   `RawPrefillPayloadPreparer` (i.e. vLLM and TRT-LLM), mutates the map and
   marshals it back with `sonic.Marshal` to build the prefill body.
   https://github.com/vllm-project/aibrix/blob/d16d8245/pkg/plugins/gateway/algorithms/pd/prefill/payload.go#L44-L79
2. `SHFSAgent.MergePrefillResponse`, `NIXLAgent.MergePrefillResponse` and
   `TRTLLMHandler.MergePrefillResponse` unmarshal `routingCtx.ReqBody` again,
   inject `kv_transfer_params` / `disagg_prefill_resp` /
   `disaggregated_params` and marshal the whole map back as the decode body.
   https://github.com/vllm-project/aibrix/blob/d16d8245/pkg/plugins/gateway/algorithms/pd/transfer/shfs.go#L58-L96
   https://github.com/vllm-project/aibrix/blob/d16d8245/pkg/plugins/gateway/algorithms/pd/transfer/nixl.go#L49-L75
   https://github.com/vllm-project/aibrix/blob/d16d8245/pkg/plugins/gateway/algorithms/pd/engine/trtllm.go#L115-L176
3. `DefaultExecutor.executeHTTP` decodes the prefill response into
   `map[string]any` as well, so for NIXL the whole response is re-serialised
   before being embedded as `disagg_prefill_resp`.
   https://github.com/vllm-project/aibrix/blob/d16d8245/pkg/plugins/gateway/algorithms/pd/prefill/default.go#L236-L296

`sonic` does not sort map keys, so nested objects (`messages[].content[]`,
`tools[].function.parameters`, …) are emitted in a different key order on
every request and, worse, differently in the prefill body and the decode body
of the same request. vLLM's chat template renders the tool schema into the
prompt, so the resulting `prompt_token_ids` differ between:

- the prefill request and the decode request of one call, and
- two identical client requests.

Both defeat prefix-cache reuse (the decode pod's local prefix cache and the
prefill pod's cache across requests). With SHFS/NIXL the decode side also
computes the prompt hash from a body that no longer matches what the prefill
pod saw.

A secondary effect: the `map[string]any` decode goes through `float64` unless
`SonicJSONInt64` is used, which is why `SonicJSONInt64` and the `anySliceForJSON`
reflection helper exist in the TRT-LLM path today.

### Steps to Reproduce

1. Deploy a vLLM PD setup (SHFS or NIXL) or a TRT-LLM PD setup with the
   AIBrix gateway `pd` router.
2. Send the same `/v1/chat/completions` request repeatedly with a `tools`
   array whose function schema has several properties, or a
   multi-modal `messages[].content[]` array.
3. Compare the prefill body and the decode body logged by the engines (or
   compare `prompt_token_ids`): the nested key order differs between them and
   between repetitions, and the reported cached-prefix length fluctuates
   instead of covering the whole shared prefix.

Unit-level reproduction: run `prefill.PreparePayload` or
`SHFSAgent.MergePrefillResponse` 100 times on the same body with unsorted
nested keys and compare the output bytes; on `main` they differ.

### Expected behavior

All PD paths should only add/replace the few top-level gateway-owned fields
(`max_tokens`, `stream`, `kv_transfer_params`, `disaggregated_params`,
`disagg_prefill_resp`, …) and leave every other byte of the client body
untouched, exactly as the SGLang path does since #2476. The prefill body and
the decode body of a request must then agree on all nested fields, and two
identical client requests must produce identical engine requests.

### Environment

- AIBrix version: `main` at d16d8245 (also present in v0.5.x releases that
  include #2476)
- Deployment environment: Kubernetes
- LLM(s) being used: vLLM PD (SHFS / NIXL), TRT-LLM PD
- Client library: any OpenAI-compatible client that sends `tools` or
  multi-part `messages`


## 评论 (1)

### github-actions[bot] · 2026-09-14

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.

