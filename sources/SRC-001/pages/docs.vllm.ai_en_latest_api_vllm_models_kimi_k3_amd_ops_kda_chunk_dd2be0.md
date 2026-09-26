source: https://docs.vllm.ai/en/latest/api/vllm/models/kimi_k3/amd/ops/kda_chunk/
lastmod: 2026-09-24

#

`vllm.models.kimi_k3.amd.ops.kda_chunk`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_chunk)

ROCm entry point for the fused Kimi-K3 KDA chunk kernel.

The kernel in `csrc/libtorch_stable/kimi_k3/fused_kda_chunk_kernel_rocm.cu`

replaces the chunk-state recurrence and the output GEMM of the Triton chunk path with a single launch that keeps the per-chunk state in registers, so the `[chunks, H, V, K]`

state tensor and the recomputed values never reach HBM.

Functions:

-
–[fused_kda_chunk](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_chunk.fused_kda_chunk)Run the chunk recurrence and the output projection in one launch.

-
–[fused_kda_prologue](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_chunk.fused_kda_prologue)Run the whole chunk-path prologue in one launch.


##

`_chunk_groups(chunks_per_seq, num_seqs, num_heads)`

`cached`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_chunk._chunk_groups)

How many parallel chunk groups to cut each sequence into.

The scan composes the group operators with the exact transfer `M_g = prod_c (diag(d_c) - w_c^T kg_c)`

, so the composition error does not grow with group length and the choice is purely a machine fit:

`fill1`

/`fill2`

: the largest G whose pass-one / pass-two grid still fits in one scheduling batch. Rows are launched in blocks of at most`kBV = 128`

, so pass one (`kV + kK`

rows) needs two blocks per`(n, h, g)`

and pass two one. Past a pass's fill point its block count grows as fast as its depth shrinks and the rung stops paying.`_DEEP_LEN`

: unless the groups are still long, where pass two's halving is worth letting pass one spill to a second batch.`_MIN_LEN`

: below this many chunks per group the per-group fixed cost exceeds what the shorter walk saves.

`G == 2`

is depth-neutral -- two passes of `nt/2`

-- and only doubles staging, so the split is taken only from `G >= 4`

.

## Source code in `vllm/models/kimi_k3/amd/ops/kda_chunk.py`


##

`_kda_group_workspace(groups, nh, device)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_chunk._kda_group_workspace)

One fp32 buffer the kernel carves into bg / sin_ / ag / mgT.

Kept caller-owned so the memory stays inside the caching allocator and vLLM's memory profiling accounts for it; the kernel's carve order must match the layout here.

## Source code in `vllm/models/kimi_k3/amd/ops/kda_chunk.py`


##

`fused_kda_chunk(qg, w, u, kg_t, aqk, decay, out, scale, cu_seqlens, initial_state, output_final_state, chunk_offsets=None, checkpoint_state=None, checkpoint_offsets=None, checkpoint_state_indices=None, state_cache=None, state_indices=None, has_initial_state=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_chunk.fused_kda_chunk)

Run the chunk recurrence and the output projection in one launch.

Parameters:

-

(`qg`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_chunk.fused_kda_chunk(qg))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`q * exp2(gk_cumsum)`

,`[1, T, H, 128]`

. -

(`w`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_chunk.fused_kda_chunk(w))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)chunk-local WY representation of the gated keys.

-

(`u`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_chunk.fused_kda_chunk(u))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)chunk-local WY representation of the values.

-

(`kg_t`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_chunk.fused_kda_chunk(kg_t))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)chunk-major transposed gated keys,

`[chunks, H, 128, 64]`

. -

(`aqk`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_chunk.fused_kda_chunk(aqk))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)intra-chunk query-key attention,

`[chunks, H, 64, 64]`

. -

(`decay`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_chunk.fused_kda_chunk(decay))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`exp2`

of each chunk's last gate row,`[chunks, H, 128]`

. -

(`out`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_chunk.fused_kda_chunk(out))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)output buffer,

`[1, T, H, 128]`

; may alias`u`

's source. -

(`scale`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_chunk.fused_kda_chunk(scale))

) –[float](https://docs.python.org/3/builtins/functions.html#float)scale applied to the query-key products.

-

(`cu_seqlens`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_chunk.fused_kda_chunk(cu_seqlens))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)int32 cumulative sequence lengths.

-

(`initial_state`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_chunk.fused_kda_chunk(initial_state))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| Nonefp32 per-sequence initial recurrent state, or

`None`

. -

(`output_final_state`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_chunk.fused_kda_chunk(output_final_state))

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)whether to return the final recurrent state.

-

(`chunk_offsets`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_chunk.fused_kda_chunk(chunk_offsets))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –int32 per-sequence first chunk index.

-

(`checkpoint_state`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_chunk.fused_kda_chunk(checkpoint_state))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –destination for the mid-prefill state snapshots, fp32

`[rows, H, 128, 128]`

. Without`checkpoint_state_indices`

it is a staging buffer indexed by sequence; with them it can be the paged state cache itself. -

(`checkpoint_offsets`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_chunk.fused_kda_chunk(checkpoint_offsets))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –int32

`[N]`

token offsets, each relative to its sequence's first query token, at which to snapshot the recurrent state.`0`

disables the export for that sequence. A non-zero offset must be a multiple of :data:`KDA_CHECKPOINT_ALIGNMENT`

; the kernel skips any that is not, so the caller has to filter rather than rely on the store happening. -

(`checkpoint_state_indices`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_chunk.fused_kda_chunk(checkpoint_state_indices))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –optional int32

`[N]`

destination row per sequence. A negative row disables the export for that sequence. -

(`state_cache`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_chunk.fused_kda_chunk(state_cache))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –the paged recurrent state, fp32

`[slots, H, 128, 128]`

. When given, the walk reads sequence`n`

's initial state from row`state_indices[n]`

and writes its final state back to the same row, which removes the gather and the scatter that otherwise bracket this kernel. Replaces`initial_state`

/`output_final_state`

, and the returned final state is then`None`

because it is already in the cache. -

(`state_indices`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_chunk.fused_kda_chunk(state_indices))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –int32

`[N]`

cache row per sequence. -

(`has_initial_state`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_chunk.fused_kda_chunk(has_initial_state))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –bool

`[N]`

; a false entry starts that sequence from a zero state and its cache row is read only, never before the walk writes it.

## Source code in `vllm/models/kimi_k3/amd/ops/kda_chunk.py`


|
|

##

`fused_kda_prologue(q, k, v, raw_g, raw_beta, A_log, dt_bias, scale, lower_bound, cu_seqlens, conv_weight=None, conv_state=None, conv_state_indices=None, conv_has_initial_state=None, chunk_indices=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_chunk.fused_kda_prologue)

Run the whole chunk-path prologue in one launch.

Replaces the two L2 norms, the gate cumsum, both intra-chunk passes and the w/u recompute. Returns the operands the fused chunk kernel consumes.

The kernel can also apply the depthwise conv and its silu, in which case `q`

/`k`

/`v`

are the three raw bands of the QKV projection and `conv_state`

is updated in place. This path is currently not used.