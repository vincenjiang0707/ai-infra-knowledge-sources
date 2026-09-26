source: https://docs.vllm.ai/en/latest/api/vllm/models/dots3_note/nvidia/
lastmod: 2026-09-24

#

`vllm.models.dots3_note.nvidia`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia)

NVIDIA-specific Dots3Note model implementations.

Modules:

-
–[attention](https://docs.vllm.ai/attention/#vllm.models.dots3_note.nvidia.attention)Dots3 NOTE sliding-window MLA attention backends for Hopper.

-
–[audio_encoder](https://docs.vllm.ai/audio_encoder/#vllm.models.dots3_note.nvidia.audio_encoder)Dots-path speech encoder for inference only (single GPU).

-
–[model](https://docs.vllm.ai/model/#vllm.models.dots3_note.nvidia.model)NVIDIA implementation of the Dots3Note language model.

-
–[mtp](https://docs.vllm.ai/mtp/#vllm.models.dots3_note.nvidia.mtp)NVIDIA multi-token predictor for Dots3Note.

-
–[multimodal](https://docs.vllm.ai/multimodal/#vllm.models.dots3_note.nvidia.multimodal)vLLM composition layer for Dots3Note image and audio encoders.

-
–[vision](https://docs.vllm.ai/vision/#vllm.models.dots3_note.nvidia.vision) -
–[vision_attention](https://docs.vllm.ai/vision_attention/#vllm.models.dots3_note.nvidia.vision_attention)Shared vision attention stack for Dots dense / MoE ViT encoders.

-
–[vision_moe](https://docs.vllm.ai/vision_moe/#vllm.models.dots3_note.nvidia.vision_moe)NOTE vision MoE execution matching the native encoder's FP8 semantics.