# [Issue #2928] Qwen3_5_MoeQModel is a VL (image-text-to-text) model but only quantizes the language tower — does text-only calibration hurt multimodal task accuracy?

source: https://github.com/ModelCloud/GPTQModel/issues/2928
state: open | updated: 2026-08-11T11:16:10Z
labels: 

## 正文

I'm quantizing a fine-tuned Qwen3.5-MoE checkpoint (multimodal VL, Qwen3_5MoeForConditionalGeneration, loaded via AutoModelForImageTextToText) to GPTQ int4, with the goal of deploying it on cheaper 24GB L4 GPUs. My downstream task is fully multimodal: the model receives a sequence of images (BEV + front-camera frames) plus a text prompt and outputs a classification label.

What I observed in the source
Looking at 
qwen3_5_moe.py
 (v7.1.0):

class Qwen3_5_MoeQModel(BaseQModel):
    loader = AutoModelForImageTextToText
    require_load_processor = True
    ...
    module_tree = [
        "model", "language_model", "layers", "#", { ... }
    ]
Two things stand out:

Qwen3_5_MoeQModel inherits from BaseQModel, which defaults to modality = [MODALITY.TEXT] (in 
base.py
). It does not declare MODALITY.IMAGE_TO_TEXT, unlike base_qwen2_vl.py / base_qwen3_vl.py which set modality = [MODALITY.TEXT, MODALITY.IMAGE_TO_TEXT].

The module_tree only covers model.language_model.*, so the vision tower / visual projector are not part of the quantization graph and are left in their original precision.

As a consequence, in 
model_test.py
 the calibration branch:

is_image_to_text_model = MODALITY.IMAGE_TO_TEXT in model.modality
calibration_dataset = (
    get_calib_dataset(model)          # image+text path
    if is_image_to_text_model
    else self.load_dataset(tokenizer, dataset_size)  # text-only path
)
evaluates is_image_to_text_model = False for Qwen3.5-MoE, so it goes down the text-only calibration path, and 
test_qwen3_5_moe.py
 indeed calibrates with text only.

Questions
Is this intentional? i.e. for Qwen3.5-MoE, is the design to quantize only the language-model Linear layers (experts + attention/MLP projections) and keep the vision tower in full precision?

Does text-only calibration meaningfully hurt accuracy for genuinely multimodal tasks? My concern: the quantized language-model layers were calibrated on activation statistics produced by text-only inputs, but at inference time those same layers consume activations that mix image embeddings (from the un-quantized vision tower) + text tokens. If the image-conditioned activation distribution differs significantly from the text-only calibration distribution, the GPTQ scales/zeros could be mis-fit for the real multimodal workload.

Has this been measured? Is there a recommendation (e.g. include some image-text samples in calibration even though the vision tower isn't quantized, just so the language-model layers see realistic image-conditioned activations)?
Should I instead force the image-text calibration path for this model (e.g. via get_calib_dataset / a multimodal calibration set), so that the language tower is calibrated on activations that include real image embeddings? Or is that unnecessary because the experts/attention statistics are dominated by text and the quality impact is negligible?

Is there any plan to add MODALITY.IMAGE_TO_TEXT support (vision-tower quantization and/or image-aware calibration) for Qwen3_5_MoeQModel?

Environment
gptqmodel 7.1.0
transformers 5.8.0
torch 2.11.0+cu130
triton 3.6.0, fla 0.5.0
Python 3.12.13 (GIL enabled)
Model: fine-tuned Qwen3.5-35B-A3B (MoE, 256 experts, linear-attention + multimodal VL)
Thanks in advance — I want to make sure I'm not silently degrading multimodal accuracy by relying on the default text-only calibration path.



## 评论 (1)

### namgyu-youn · 2026-08-11

Quantizing the vision encoder in a VLM is often skipped, because:
1. The vision encoder holds a small fraction of the total parameters (e.g., 0.42B out of 27.44B in Gemma3-27B), so the compute/memory savings from quantizing it are marginal.
2. Vision-specific calibration data (image-text pairs) is required, adding pipeline complexity.

This isn't limited to GPTQModel. Many open-source tools, like llm-compressor, skip the vision layer entirely: https://github.com/vllm-project/llm-compressor/blob/f68ff8dc2355b4fef2a47fdd9129d41c285aac3b/examples/multimodal_vision/README_internvl3.md?plain=1#L61. They also exclude the attention heads to prevent accuracy drops.
