# [Issue #2204] LUT-B Support

source: https://github.com/NVIDIA/Model-Optimizer/issues/2204
state: open | updated: 2026-08-18T05:38:13Z
labels: question

## 正文

## How would you like to use ModelOpt

Hi, I am a maintainer of `vllm-project/compressed-tensors`, and we are looking to do some up-front work to benchmark the LUT-B pathways that Vera Rubin will support, as well as solidify the compression format inside compressed-tensors and the load-up pathway in vllm. We are constrained by the limited technical specs we have seen, and wanted to start a discussion here (as suggested by @Edwardf0t1 in today's vllm sig-quant meeting).

I would be very happy to set up a call to discuss further, if the maintainers of modelopt are interested, to try to align our formats as much as possible. But at the moment, this amounts to 3 questions in particular (in order of importance):

1. Ref 1 states "LUT-based representations can retain up to MXFP8 accuracy, adding another precision option to the Rubin inference toolbox". Does this mean each codebook tile will require an associated FP8 e8m0 scale? (See Ref 4 for our current checkpoint, which has weight_packed and weight_codebook, but no weight_scale as of yet)
2. Ref 1 states that Vera Rubin will support a 3-bit lookup table. Just wanted to confirm this isn't configurable beyond 3 bits.
3. Similar to above, are tile sizes configurable or constrained?


Refs:
1. Nvidia dev blog -- https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/
2. WIP compressed-tensors format -- https://github.com/vllm-project/compressed-tensors/pull/801
3. WIP vllm online quant -- https://github.com/vllm-project/vllm/pull/51880
4. WIP checkpoint -- https://huggingface.co/bdellabe/Meta-Llama-3-8B-Instruct-LUTB


### Who can help?

Anyone involved in adding LUT-B compression support to ModelOpt



## 评论 (1)

### Edwardf0t1 · 2026-08-18

cc @Trenton-Starkey 
