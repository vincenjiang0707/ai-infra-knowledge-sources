source: https://docs.vllm.ai/en/latest/api/vllm/models/inkling/nvidia/ops/sconv/
lastmod: 2026-09-23

#

`vllm.models.inkling.nvidia.ops.sconv`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.sconv)

Inkling short-convolution kernels backed by a paged sliding-window state cache.

Each layer's 4 conv streams (K, V, attn-output, mlp-output) share one paged KV cache `[num_blocks, H, N, D]`

(head-major; see `sconv_swa_attn.py`

). A stream occupies the contiguous D-sub-range `[off_s, off_s + ws)`

across all `H`

heads, so its flat per-token width is `H * ws`

and that is the conv channel dim. The cache stores the conv *input* at every absolute position.

`fused_sconv`

is the single-launch path used by the model: per token it writes the current input to its slot and convolves the `W`

taps ending at its absolute position. A tap landing inside the current forward is read from the immutable input `x`

(row `src - pos + pid_t`

); only pre-forward taps are read from the paged cache (window position `src`

-> physical block via `block_table[req, src // N]`

). The just-written slot is never read back this step, so there is no write/read hazard within or across programs -- which is why this needs no decode-vs-prefill split and is valid for prefill / decode / spec alike.

All kernels address the cache purely by `(slot, absolute_position)`

and allocate nothing inside the captured region; their grids depend only on the token count (`fused_sconv`

on a fixed token/channel tiling), so the same path replays correctly under eager, breakable PIECEWISE, and FULL cudagraphs without any data-dependent shape or branch.

Functions:

-
–[fused_sconv](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.sconv.fused_sconv)Single-launch insert + depthwise causal conv1d over the paged cache.

-
–[sconv_seq_metadata](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.sconv.sconv_seq_metadata)Fill static per-token seq_idx / query_start buffers in one launch.


##

`fused_sconv(x, weight, cache, positions, block_table, seq_idx, slot_mapping, query_start, off_s, ws, block_size, activation=None, use_residual=True)`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.sconv.fused_sconv)

Single-launch insert + depthwise causal conv1d over the paged cache.

Reads same-forward taps from `x`

and pre-forward taps from the cache, so it is race-free in one launch for prefill / decode / spec and cudagraph-safe under eager / piecewise / full capture.

## Source code in `vllm/models/inkling/nvidia/ops/sconv.py`


##

`sconv_seq_metadata(query_start_loc, num_reqs, num_actual_tokens, seq_idx_out, query_start_out, num_padded_tokens=None)`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.sconv.sconv_seq_metadata)

Fill static per-token seq_idx / query_start buffers in one launch.

Replaces the arange + searchsorted + clamp + gather + 2x copy chain of the sconv metadata build with a single kernel writing both persistent buffers. Padded rows are filled with zero and must have `slot_mapping == -1`

.