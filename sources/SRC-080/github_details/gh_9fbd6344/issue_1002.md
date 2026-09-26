# [Issue #1002] llm_eval support for NVFP4 post-quant checkpoint

source: https://github.com/NVIDIA/Model-Optimizer/issues/1002
state: closed | updated: 2026-06-19T04:38:03Z
labels: stale, waiting for feedback

## 正文

Hello all,
Can Modelopt enable the wikitext-like task-based accuracy test for the quantized output model for NVFP4?
The export model exists some shape fusion due to the pack mechanism for 2 FP4 into 1 INT8, differing from the original model structure.
How can LLM_eval support the quantized model?

//==================================//
python lm_eval_hf.py 
       --model hf  \
       --model_args pretrained=  \
       --quant_cfg NVFP4_DEFAULT_CFG \   
       --tasks wikitext   \
       --batch_size 4
Does the cmd shown above support the exported model test?

## 评论 (3)

### realAsma · 2026-05-21

> 🤖 Bot-drafted reply

Hi @jimmy-adams, the answer depends on what your `pretrained=...` points to:

- If it points to the **original BF16 / FP16 HF model**, then `--quant_cfg NVFP4_DEFAULT_CFG` will fake-quantize in memory and eval works -- see `examples/llm_eval/README.md`.
- If it points to the **exported NVFP4 HF checkpoint** (the packed FP4 -> uint8 weights), that won't load as a vanilla `transformers` model and the script will fail. The packed format is intended for downstream engines (TensorRT-LLM, vLLM).

So for end-to-end accuracy on the exported checkpoint, deploy it via TRT-LLM or vLLM and run lm_eval against the served endpoint. For pre-export accuracy (sanity check that quantization didn't tank perplexity), the in-memory path with the script above is the right tool.

Could you confirm which case you're in? Marking `waiting for feedback`.

### github-actions[bot] · 2026-06-05

Issue has not received an update in over 14 days. Adding stale label.

### github-actions[bot] · 2026-06-19

This issue was closed because it has been 14 days without activity since it has been marked as stale.
