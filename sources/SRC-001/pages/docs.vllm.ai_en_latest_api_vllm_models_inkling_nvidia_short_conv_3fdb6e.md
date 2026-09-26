source: https://docs.vllm.ai/en/latest/api/vllm/models/inkling/nvidia/short_conv/
lastmod: 2026-09-24

#

`vllm.models.inkling.nvidia.short_conv`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.short_conv)

Inkling short convolution: depthwise causal conv1d (+ residual) over a paged sliding-window conv-state cache.

Each decoder layer owns one `InklingConvState`

(`sconv_swa_attn.py`

) holding the manager-allocated paged cache for the layer's 4 sconv streams (K, V, attn-output, mlp-output), packed head-major into one block. Each `InklingShortConv`

is a stateless weight + kernel launcher that, per forward (positions-addressed, the same path for prefill / decode / mixed), inserts the current tokens' inputs into their paged slot and convolves each token against the `W`

taps ending at its absolute position, reading pre-forward window positions out of the paged cache via the block table.

Per-forward metadata (`block_table`

/ `slot_mapping`

/ `seq_idx`

/ `query_start`

) is built once by `InklingSconvMetadataBuilder`

and published under the owner's prefix in the forward context; the absolute `positions`

are threaded in from the model. The insert + conv run in a single `fused_sconv`

launch (same path for prefill / decode / mixed / spec). All inputs are fixed-address persistent buffers and the grid is fixed, so the conv replays correctly under eager, PIECEWISE, and FULL cudagraphs.