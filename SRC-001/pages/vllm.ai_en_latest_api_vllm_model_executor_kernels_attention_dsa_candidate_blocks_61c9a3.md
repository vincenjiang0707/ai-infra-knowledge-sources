source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/attention/dsa/candidate_blocks/
lastmod: 2026-09-23

#

`vllm.model_executor.kernels.attention.dsa.candidate_blocks`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.candidate_blocks)

Functions:

-
–[apply_candidate_mask](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.candidate_blocks.apply_candidate_mask)Mask packed logits outside causal bounds and request-local candidates.

-
–[select_candidate_blocks](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.candidate_blocks.select_candidate_blocks)Select local block IDs by maximum score, pinning each row's newest block.


##

`apply_candidate_mask(logits, row_ks, row_ke, candidate_blocks, block_size, row_repeat=1)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.candidate_blocks.apply_candidate_mask)

Mask packed logits outside causal bounds and request-local candidates.

## Source code in `vllm/model_executor/kernels/attention/dsa/candidate_blocks.py`


##

`select_candidate_blocks(logits, row_ks, row_ke, topk_blocks, block_size, out, row_repeat=1)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.attention.dsa.candidate_blocks.select_candidate_blocks)

Select local block IDs by maximum score, pinning each row's newest block.

Row bounds are in packed column space; absent starts mean zero. Decode rows share bounds in groups of `row_repeat`

. Output is -1 padded.