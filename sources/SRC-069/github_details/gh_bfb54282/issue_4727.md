# [Issue #4727] [RFC] Support multiple MegaMOE workspace capacities for the same layer

source: https://github.com/flashinfer-ai/flashinfer/issues/4727
state: open | updated: 2026-09-25T02:12:58Z
labels: feature request, needs-triage, priority: should have (P1)

## 正文

### Before submitting

- [x] I have searched existing issues and this request has not been filed yet.

### Problem

## Summary

We propose allowing a MegaMOE layer to use multiple workspace capacities while reusing the same weights and kernel configuration.

This is needed by serving systems where prefill and decode run on the same GPU but have very different `max_tokens_per_rank` requirements. Currently, `FleetParams.max_tokens_per_rank` is fixed when constructing the MegaMOE layer, and the Mega workspace is allocated according to that capacity.

Sizing it for prefill can therefore make decode use a much larger workspace and reduction capacity than necessary. This is especially expensive when `in_kernel_fc2_reduce` is disabled and FC2 reduction is performed by a separate kernel.

## Motivation

SGLang is integrating FlashInfer MegaMOE in:

https://github.com/sgl-project/sglang/pull/31470

In aggregate or co-located serving, prefill and decode may execute on the same GPU/rank:

- Prefill can have a large number of tokens per rank.
- Decode normally has a much smaller number of tokens per rank.
- Both modes reuse the same model weights and MegaMOE configuration.

The current integration passes one value through:

```python
FleetParams(
    num_experts=num_experts,
    max_tokens_per_rank=max_tokens_per_rank,
    token_hidden_size=hidden_size,
)
```

Because this value determines the Mega symmetric workspace capacity, the layer must currently be configured for the larger prefill workload.

For example:

```text
prefill max_tokens_per_rank: 4096
decode  max_tokens_per_rank: 256
configured capacity:         4096
```

Decode then uses the prefill-sized workspace and reduction configuration even though its actual token count is much smaller. We have observed a significant decode latency regression in this configuration.

A process-wide environment variable cannot solve this because prefill and decode coexist in the same process and may alternate at runtime.

## Goals

- Reuse the same MegaMOE layer weights for different token capacities.
- Allocate and retain separate workspaces for different capacity profiles.
- Select the appropriate workspace for each forward call.
- Keep workspace addresses stable for CUDA Graph capture.
- Preserve the existing single-capacity API and behavior.

## Non-goals

- FlashInfer does not need to understand `prefill` or `decode`.
- This proposal does not require reallocating a workspace on every forward.
- This proposal does not change routing, MoE computation, or reduction numerics.

## Proposed API

Our preferred API is to expose explicit, reusable workspace handles:

```python
layer = MoEEpLayer(
    bootstrap=bootstrap,
    fleet_params=FleetParams(
        num_experts=num_experts,
        max_tokens_per_rank=default_capacity,
        token_hidden_size=hidden_size,
    ),
    weights=weights,
    backend=backend,
)

prefill_workspace = layer.create_workspace(
    max_tokens_per_rank=prefill_capacity,
)

decode_workspace = layer.create_workspace(
    max_tokens_per_rank=decode_capacity,
)

prefill_output = layer.forward(
    prefill_inputs,
    workspace=prefill_workspace,
)

decode_output = layer.forward(
    decode_inputs,
    workspace=decode_workspace,
)
```

A workspace should be compatible with the layer only when all workspace-shaping properties other than `max_tokens_per_rank` match, including:

- World size
- Hidden size
- Intermediate size
- Number of experts
- Top-k
- Dtype
- Backend configuration

FlashInfer should validate:

```text
actual_tokens_per_rank <= workspace.max_tokens_per_rank
```

The existing API should remain unchanged:

```python
output = layer.forward(inputs)
```

When no workspace is provided, FlashInfer continues to lazily create and use the default workspace derived from `FleetParams.max_tokens_per_rank`.

## Alternative API

If explicit workspace ownership is undesirable, the layer could maintain an internal cache keyed by capacity:

```python
output = layer.forward(
    inputs,
    max_tokens_per_rank=decode_capacity,
)
```

Conceptually:

```python
workspace = self._workspaces.get_or_create(
    max_tokens_per_rank=max_tokens_per_rank,
)
```

However, explicit workspace handles may provide clearer lifetime management, more predictable memory use, and better CUDA Graph integration.

## SGLang Integration

SGLang would map serving modes to workspace capacities:

```python
workspace = (
    prefill_workspace
    if forward_mode.is_prefill()
    else decode_workspace
)

output = mega_moe_layer.forward(
    inputs,
    workspace=workspace,
)
```

SGLang could expose separate configuration values while retaining the existing value as a fallback:

```text
SGLANG_FLASHINFER_MEGAMOE_MAX_TOKENS_PER_RANK
SGLANG_FLASHINFER_MEGAMOE_PREFILL_MAX_TOKENS_PER_RANK
SGLANG_FLASHINFER_MEGAMOE_DECODE_MAX_TOKENS_PER_RANK
```

The FlashInfer API itself would remain workload-agnostic. The same mechanism could support:

- Speculative decoding
- CUDA Graph batch-size buckets
- Different scheduling profiles
- Other workloads with distinct token-capacity requirements

## Expected Behavior

- Creating a second workspace does not duplicate or preprocess weights.
- Workspace allocation happens once per capacity/profile, not per forward.
- Each workspace can be independently captured by CUDA Graphs.
- Selecting a smaller workspace reduces decode reduction and workspace overhead.
- Existing users see no API or behavior change.
- Destroying the layer cleans up all internally owned workspaces.
- Externally owned workspace handles have a clearly documented lifetime.

## Testing

Suggested test coverage:

1. Run the same inputs with default and explicit workspaces and compare outputs.
2. Alternate between large and small workspaces on the same layer.
3. Verify that exceeding a workspace capacity produces a clear error.
4. Verify that weights are transformed only once.
5. Capture separate CUDA Graphs for large and small capacity profiles.
6. Benchmark the out-of-kernel FC2 reduction path when the actual token count is much smaller than the configured prefill capacity.

## Open Questions

1. Should workspaces be caller-owned handles or internally cached by the layer?
2. Can a smaller-capacity workspace share any allocations with a larger one without making reduction work scale with the larger capacity?
3. Which workspace-shaping fields should be included in compatibility checks?
4. Should FlashInfer expose workspace memory size for serving-framework memory planning?
5. Does the current Mega kernel ABI permit selecting the workspace at forward time, or would this require separating workspace state from the backend instance?

## Related Links

- SGLang FlashInfer MegaMOE integration: https://github.com/sgl-project/sglang/pull/31470
- FlashInfer MoE EP architecture: https://github.com/flashinfer-ai/flashinfer/blob/main/docs/design_docs/moe_ep_architecture.md


### Requested outcome

Expose an API that allows the same MegaMOE layer and transformed weights to use multiple reusable workspace capacities.

The serving framework should be able to create or select a workspace using a runtime-specific `max_tokens_per_rank`, for example:

```python
prefill_workspace = layer.create_workspace(
    max_tokens_per_rank=prefill_capacity,
)
decode_workspace = layer.create_workspace(
    max_tokens_per_rank=decode_capacity,
)

output = layer.forward(inputs, workspace=decode_workspace)
```
 The requested behavior is:

- Reuse the same layer, weights, and preprocessed weights across workspaces.
- Allocate each workspace once and retain it for later calls.
- Allow workspace selection at forward time.

The API does not need to expose prefill/decode concepts directly. A generic caller-managed workspace or capacity-profile API would let serving frameworks map different workloads to appropriate capacities.

### Target hardware

SM100 (B200, GB200)

### Inference engine

SGLang

### Affected model or model family

DSV4

### Workload and configuration

- Data type and quantization:
- Batch size or request concurrency:
- Sequence lengths or token counts:
- Parallelism: TP / EP / DP / PP / disaggregated
- Relevant shapes: heads, head dimension, hidden size, experts, top-k, page size, or other
- Environment: output of `python -m flashinfer.collect_env`


### Current workaround

_No response_

### Impact

_No response_

### Acceptance criteria

_No response_

### Related work, dependencies, or suggested scope

_No response_

### Timing or release need

_No response_

## 评论 (8)

### wenscarl · 2026-08-26

cc. @aleozlx 

### kmrao-nv · 2026-08-27

cc @Anerudhan 

### nvpohanh · 2026-09-04

I synced up with @wenscarl . The key request here is that **the reduction kernel latency should shrink with the actual token size when the actual token size is lower than the workspace size**. It is okay to keep the current workspace size as long as the reduction kernel performance makes sense.

### Anerudhan · 2026-09-08

Hi folks,

Can we have do something like

```
prefill_layer = MoEEpLayer(
    bootstrap=bootstrap,
    fleet_params=FleetParams(
        num_experts=num_experts,
        max_tokens_per_rank= prefill_capacity,
        token_hidden_size=hidden_size,
    ),
    weights=weights,
    backend=backend,
)
```

and 

```
decode_layer = MoEEpLayer(
    bootstrap=bootstrap,
    fleet_params=FleetParams(
        num_experts=num_experts,
        max_tokens_per_rank= decode_capacity,
        token_hidden_size=hidden_size,
    ),
    weights=weights,
    backend=backend,
)
```

Basically, instantiate different objects of the same class and call as necessary ?

Thanks

### djns99 · 2026-09-10

> the reduction kernel latency should shrink with the actual token size when the actual token size is lower than the workspace size

Why is this not already the case? It sounds like this is caused by MegaMOE reducing the maximum tokens instead of the actual number of tokens. I would consider this a performance bug.
The workspace here seems like a bit of a red herring unless I am misunderstanding something

### yyihuang · 2026-09-25

@wenscarl Update for this request: [feat(cake_mega_moe): add reusable MegaMoE workspaces and an SM100a reducer](https://github.com/flashinfer-ai/flashinfer/pull/4819) was merged on 2026-09-12 (UTC).

Reusable MegaMoE workspace capacities and the SM100a native terminal reducer are merged.

- MoEEpMegaLayer.create_workspace(max_tokens_per_rank=...) creates a layer-bound profile; forward(..., workspace=handle) reuses the layer's transformed weights.
- The BF16 TopK-6, H4096 native reducer handles live rows within capacities 256/4096, so reduction work follows the actual token count. Unsupported configurations retain the existing reduction path.

Workspace creation/destruction are EP collectives and must be ordered consistently across ranks. Stable borrowed output views are opt-in via return_workspace_view=True.


### yyihuang · 2026-09-25

@wenscarl Update for this request: [perf(cake_megamoe_topk_reduce): regenerate the SM100a reducer from the current Cake exporter](https://github.com/flashinfer-ai/flashinfer/pull/5431) was merged on 2026-09-23 (UTC).

The SM100a reducer export refresh following #4819 is merged.

- Regenerates and re-pins the native reducer source/manifest with the unchanged kernel body, one-symbol ABI and ordered FP32 accumulation.
- The launch remains 4 * num_tokens CTAs with 256 threads, preserving reduction work proportional to live rows.

This is a generated-source maintenance update, not a new workspace API or an additional performance claim.


### yyihuang · 2026-09-25

@wenscarl Update for this request: [feat(cake_megamoe_topk_reduce): publish the SM103a reducer export and enable the native reducer on B300](https://github.com/flashinfer-ai/flashinfer/pull/5509) was merged on 2026-09-24 (UTC).

The native MegaMoE terminal reducer now also supports SM103a/B300.

- Adds a separately targeted SM103a export and extends native-reducer eligibility from CC 10.0 to CC 10.3.
- Selects the JIT module from the partials' device while preserving the existing workspace/reducer API and live-token reduction behavior; the PR includes B300 multi-rank validation.

