source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/utils/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.utils`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.utils)

Utility methods for model layers.

Functions:

-
–[apply_penalties](https://docs.vllm.ai#vllm.model_executor.layers.utils.apply_penalties)Applies penalties in place to the logits tensor

-
–[warmup_rocm_skinny_gemm_workspaces](https://docs.vllm.ai#vllm.model_executor.layers.utils.warmup_rocm_skinny_gemm_workspaces)Eagerly allocate wvSplitKrc's per-device split-K workspace pool.

-
–[wvsplitkrc_dispatch](https://docs.vllm.ai#vllm.model_executor.layers.utils.wvsplitkrc_dispatch)Pick the K-shard split for wvSplitKrc and say whether the shape fits.


##

`apply_penalties(logits, prompt_tokens_tensor, output_tokens_tensor, presence_penalties, frequency_penalties, repetition_penalties)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.utils.apply_penalties)

Applies penalties in place to the logits tensor logits : The input logits tensor of shape [num_seqs, vocab_size] prompt_tokens_tensor: A tensor containing the prompt tokens. The prompts are padded to the maximum prompt length within the batch using `vocab_size`

as the padding value. The value `vocab_size`

is used for padding because it does not correspond to any valid token ID in the vocabulary. output_tokens_tensor: The output tokens tensor. presence_penalties: The presence penalties of shape (num_seqs, ) frequency_penalties: The frequency penalties of shape (num_seqs, ) repetition_penalties: The repetition penalties of shape (num_seqs, )

## Source code in `vllm/model_executor/layers/utils.py`


##

`warmup_rocm_skinny_gemm_workspaces(device)`

`cached`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.utils.warmup_rocm_skinny_gemm_workspaces)

Eagerly allocate wvSplitKrc's per-device split-K workspace pool.

wvSplitKrc partitions one per-device allocation into `kWvSlots`

slots (csrc/rocm/skinny_gemms.cu) and hands each stream one on first use, so that two streams never share the split-K partials and counters.

The pool is otherwise created lazily on the first qualifying GEMM (csrc/rocm/skinny_gemms.cu), which can be the first real request — after the KV cache backing buffer exists. If it landed in that segment's rounding tail, it would pin the entire segment at engine shutdown; it could also land inside a cudagraph capture, where it would be taken from the graph's private pool and its zero-fill would become a replayed graph node.

## Source code in `vllm/model_executor/layers/utils.py`


##

`wvsplitkrc_dispatch(n, k, m, cu_count)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.utils.wvsplitkrc_dispatch)

Pick the K-shard split for wvSplitKrc and say whether the shape fits.

Mirrors wvSplitKrc() in csrc/rocm/skinny_gemms.cu, which is also where the shard cap is explained. Both must pick the same chunkk or the workspace check here bounds the wrong k_rnd.

Returns:

-

–[int](https://docs.python.org/3/builtins/functions.html#int)The CHUNKK the kernel will dispatch with, and whether the CU budget and

-

–[bool](https://docs.python.org/3/builtins/functions.html#bool)split-K workspace admit the shape at all.