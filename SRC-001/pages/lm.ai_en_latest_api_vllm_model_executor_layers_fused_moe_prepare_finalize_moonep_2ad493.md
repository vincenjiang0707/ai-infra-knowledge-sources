source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/prepare_finalize/moonep/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_moe.prepare_finalize.moonep`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.moonep)

MoonEP (https://github.com/MoonshotAI/MoonEP) prepare/finalize.

BF16 correctness-first proof of concept on top of vLLM's modular kernel interface.

MoonEP differs from DeepEP-style backends in two ways that shape this integration:

`dispatch`

returns tokens already grouped by expert*row*(a fixed`[NvS, H]`

layout with`NvS = S x K`

real slots plus padding) together with a`cu_seqlens[E+B]`

segment table and an opaque`plan`

. There is no per-token topk id tensor after dispatch; the expert compute must be a grouped GEMM over`cu_seqlens`

segments.- Rows
`[E, E+B)`

of the weight/segment space are dynamic redundant-expert prefetch slots.`plan.experts_to_copy`

names the source expert of each slot and`Buffer.prefetch_weight`

must run between dispatch and expert compute.

PoC limitations: - BF16 / unquantized only, eager only. - Expert weights are replicated in global-expert order on every rank (memory-heavy). Production Kimi-K3 serving requires sharded symmetric-memory expert ownership, where rows `[0, E)`

physically alias each home rank's parameter memory. - Route weights are applied inside the expert compute and MoonEP's `combine`

performs the K-sum, so `finalize`

requires `TopKWeightAndReduceNoOP`

.

Classes:

-
–[MoonEPBufferPool](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.moonep.MoonEPBufferPool)Lazily creates

`moonep.Buffer`

instances at power-of-two capacities. -
–[MoonEPExpertWeightLayout](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.moonep.MoonEPExpertWeightLayout)Contiguous BF16 expert weights in MoonEP

`[E+B, ...]`

layout. -
–[MoonEPPrepareAndFinalize](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.moonep.MoonEPPrepareAndFinalize)Prepare/Finalize using MoonEP balanced dispatch/combine.


Functions:

-
–[gather_moonep_weight_layout](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.moonep.gather_moonep_weight_layout)Build the replicated

`[E+B, ...]`

layout from this rank's local experts. -
–[make_moonep_weight_layout](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.moonep.make_moonep_weight_layout)Build the replicated

`[E+B, ...]`

PoC weight layout.

##

`MoonEPBufferPool`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.moonep.MoonEPBufferPool)

Lazily creates `moonep.Buffer`

instances at power-of-two capacities.

`Buffer`

fixes its token capacity `S`

at construction, so a single full-capacity buffer would pad every dispatch to `max_num_batched_tokens`

. The pool instead serves the smallest power-of-two capacity that fits the step's token count, so decode-sized batches dispatch a few hundred slots rather than the full capacity.

Selection must be identical on every EP rank (dispatch is collective and `Buffer`

construction is itself a collective): callers derive the token count from `dp_metadata`

(the max across DP ranks) so all ranks create and pick the same buffer at the same step.

Methods:

-
–[get](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.moonep.MoonEPBufferPool.get)Return

`(capacity, buffer)`

for the given step token count.

## Source code in `vllm/model_executor/layers/fused_moe/prepare_finalize/moonep.py`


###

`get(num_tokens)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.moonep.MoonEPBufferPool.get)

Return `(capacity, buffer)`

for the given step token count.

## Source code in `vllm/model_executor/layers/fused_moe/prepare_finalize/moonep.py`


##

`MoonEPExpertWeightLayout`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.moonep.MoonEPExpertWeightLayout)

Bases: [NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple)

Contiguous BF16 expert weights in MoonEP `[E+B, ...]`

layout.

Rows `[0, E)`

hold expert weights in global expert order; rows `[E, E+B)`

are mutable prefetch slots filled by `Buffer.prefetch_weight`

.

The prefetch slots never need re-zeroing between calls: the planner marks unused slots with `-1`

in `plan.experts_to_copy`

(skipped by `prefetch_weight`

) and gives them an empty `cu_seqlens`

segment, so stale slot contents are never read; used slots are fully overwritten.

## Source code in `vllm/model_executor/layers/fused_moe/prepare_finalize/moonep.py`


##

`MoonEPPrepareAndFinalize`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.moonep.MoonEPPrepareAndFinalize)

Bases: [FusedMoEPrepareAndFinalizeModular](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeModular)

Prepare/Finalize using MoonEP balanced dispatch/combine.

`prepare`

pads the batch to the selected buffer's static token capacity, dispatches, runs `prefetch_weight`

for the planned redundant experts, and stashes the `plan`

for `finalize`

(the same pattern DeepEP-HT uses for its handle). Downstream expert compute must consume the expert-grouped `[NvS, H]`

layout via `cu_seqlens`

.

Attributes:

-
([num_dispatched_slots](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.moonep.MoonEPPrepareAndFinalize.num_dispatched_slots)

) –[int](https://docs.python.org/3/builtins/functions.html#int)`NvS`

of the buffer selected by the current step's prepare().

## Source code in `vllm/model_executor/layers/fused_moe/prepare_finalize/moonep.py`


|
|

###

`num_dispatched_slots`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.moonep.MoonEPPrepareAndFinalize.num_dispatched_slots)

`NvS`

of the buffer selected by the current step's prepare().

##

`gather_moonep_weight_layout(w13_local, w2_local, num_global_experts, num_prefetch_slots)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.moonep.gather_moonep_weight_layout)

Build the replicated `[E+B, ...]`

layout from this rank's local experts.

PoC bridge: each EP rank loads only its own experts (linear placement), so all-gather them once at load time into global expert order on every rank. Production MoonEP instead maps rows `[0, E)`

onto each home rank's parameter memory via symmetric memory (RFC #52095 item 5).

## Source code in `vllm/model_executor/layers/fused_moe/prepare_finalize/moonep.py`


##

`make_moonep_weight_layout(w13_weight, w2_weight, num_prefetch_slots)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.moonep.make_moonep_weight_layout)

Build the replicated `[E+B, ...]`

PoC weight layout.

`w13_weight`

must be `[E, 2I, H]`

(gate rows first) and `w2_weight`

`[E, H, I]`

, both BF16 in global expert order.