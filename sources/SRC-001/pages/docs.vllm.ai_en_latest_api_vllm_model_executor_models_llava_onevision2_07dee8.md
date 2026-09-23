source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/llava_onevision2/
lastmod: 2026-09-23

#

`vllm.model_executor.models.llava_onevision2`

[¶](https://docs.vllm.ai#vllm.model_executor.models.llava_onevision2)

Inference-only LLaVA-OneVision-2 (OV2) model for vLLM.

Architecture notes:

- LLM backbone is plain Qwen3-8B with 1-D position_ids (no M-RoPE).
- Vision tower removes the CLS token (no class_embedding/class_pos_emb).
- Vision RoPE is 3-D (T:H:W) with a 4:6:6 head_dim split and uses
`patch_positions`

instead of grid_thw to compute per-token freqs. `rotate_half`

is*interleaved*(`(::2, 1::2)`

) rather than split-half.- Vision attention uses windowed
`cu_seqlens`

(`frame_windows_size`

in T-dim); two backends implemented (SDPA + flash_attn varlen). `patch_positions: [total_patches, 3]`

is plumbed as a first-class MM kwarg alongside`pixel_values`

/`image_grid_thw`

.- Video frame-backend and codec-backend both alias to the image path inside the HF processor, so the model implements a single visual code path.

Classes:

-
–[LlavaOnevision2ForConditionalGeneration](https://docs.vllm.ai#vllm.model_executor.models.llava_onevision2.LlavaOnevision2ForConditionalGeneration)vLLM-side OV2 top-level model.

-
–[LlavaOnevision2VideoBackend](https://docs.vllm.ai#vllm.model_executor.models.llava_onevision2.LlavaOnevision2VideoBackend)Frame-sampling backend for LLaVA-OneVision-2.

-
–[LlavaOnevision2VisionAttn](https://docs.vllm.ai#vllm.model_executor.models.llava_onevision2.LlavaOnevision2VisionAttn)Vision self-attention with windowed cu_seqlens.

-
–[LlavaOnevision2VisionRotaryEmbedding](https://docs.vllm.ai#vllm.model_executor.models.llava_onevision2.LlavaOnevision2VisionRotaryEmbedding)3-D rotary frequency constructor with 4:6:6 (T:H:W) split.

-
–[LlavaOnevision2VisionTower](https://docs.vllm.ai#vllm.model_executor.models.llava_onevision2.LlavaOnevision2VisionTower)OV2 vision tower (no CLS token, 3-D RoPE, windowed attention).


Functions:

-
–[prepare_codec_video_input](https://docs.vllm.ai#vllm.model_executor.models.llava_onevision2.prepare_codec_video_input)Wrap a video path for vLLM's MultiModalDataParser + OV2 codec backend.


##

`LlavaOnevision2ForConditionalGeneration`

[¶](https://docs.vllm.ai#vllm.model_executor.models.llava_onevision2.LlavaOnevision2ForConditionalGeneration)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsMultiModal](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal)[SupportsPP](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsPP)

vLLM-side OV2 top-level model.

Weight name rewriting (HF checkpoint → vLLM module tree): Prefix rewrites only (longest match wins). Vision tower attribute names mirror HF names verbatim, so no substring rules are needed. Substring rules would otherwise collide with the Qwen3 text-path `self_attn`

modules and break the language-model loader. `model.language_model.`

→ `language_model.model.`

`model.visual.`

→ `visual.`

`lm_head.`

→ `language_model.lm_head.`

`model.`

(fallback) → `language_model.model.`


## Source code in `vllm/model_executor/models/llava_onevision2.py`


|
|

##

`LlavaOnevision2VideoBackend`

[¶](https://docs.vllm.ai#vllm.model_executor.models.llava_onevision2.LlavaOnevision2VideoBackend)

Bases: [VideoBackend](https://docs.vllm.ai/multimodal/video/#vllm.multimodal.video.VideoBackend)

Frame-sampling backend for LLaVA-OneVision-2.

Selected automatically for OV2 via the `video_processor`

binding (`video_processor_type == "LlavaOnevision2VideoProcessor"`

in the model's `video_preprocessor_config.json`

). Decoding uses the inherited OpenCV / PyAV codecs; only the sampling index policy is overridden to match qwen.

## Source code in `vllm/model_executor/models/llava_onevision2.py`


##

`LlavaOnevision2VisionAttn`

[¶](https://docs.vllm.ai#vllm.model_executor.models.llava_onevision2.LlavaOnevision2VisionAttn)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Vision self-attention with windowed cu_seqlens.

The HF checkpoint ships a *fused* qkv linear (`self_attn.qkv`

), so we load directly into `QKVParallelLinear`

with no stacked_params mapping. (Compare OV1.5, whose checkpoint had separate q/k/v.)

## Source code in `vllm/model_executor/models/llava_onevision2.py`


|
|

###

`_rotate_half_interleaved(x)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.llava_onevision2.LlavaOnevision2VisionAttn._rotate_half_interleaved)

OV2-specific interleaved rotate_half.

Pairs adjacent dims: (x[::2], x[1::2]) -> (-x[1::2], x[::2]). NOT compatible with the split-half rotate used in OV1.5/LLaMA.

## Source code in `vllm/model_executor/models/llava_onevision2.py`


##

`LlavaOnevision2VisionRotaryEmbedding`

[¶](https://docs.vllm.ai#vllm.model_executor.models.llava_onevision2.LlavaOnevision2VisionRotaryEmbedding)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

3-D rotary frequency constructor with 4:6:6 (T:H:W) split.

Mirrors `VisionRotaryEmbedding`

in the HF reference (`modeling_llava_onevision2.py`

L79-L210). The three `inv_freq_*`

buffers are non-persistent — they are *not* in the checkpoint and must be reconstructed at module init time (which we do here).

## Public entry points used by the vision tower

`forward_from_positions(patch_positions)`

— per-patch (t,h,w) positions → per-token freqs [N, half].

Methods:

-
–[forward_from_positions](https://docs.vllm.ai#vllm.model_executor.models.llava_onevision2.LlavaOnevision2VisionRotaryEmbedding.forward_from_positions)[N, 3] (t,h,w) int → [N, half] float frequencies.


## Source code in `vllm/model_executor/models/llava_onevision2.py`


###

`forward_from_positions(patch_positions)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.llava_onevision2.LlavaOnevision2VisionRotaryEmbedding.forward_from_positions)

[N, 3] (t,h,w) int → [N, half] float frequencies.

## Source code in `vllm/model_executor/models/llava_onevision2.py`


##

`LlavaOnevision2VisionTower`

[¶](https://docs.vllm.ai#vllm.model_executor.models.llava_onevision2.LlavaOnevision2VisionTower)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

OV2 vision tower (no CLS token, 3-D RoPE, windowed attention).

Module attribute names mirror HF checkpoint names verbatim so the WeightsMapper only needs prefix rewrites (no substring rules, which would otherwise collide with the Qwen3 text-path `self_attn`

modules): visual.embeddings.patch_embedding visual.layernorm_pre visual.encoder.layers.{i}.self_attn.{qkv,proj} visual.encoder.layers.{i}.layer_norm{1,2} visual.encoder.layers.{i}.mlp.fc{1,2} visual.merger.{ln_q, mlp.{0,2}} visual.rotary_pos_emb (non-persistent inv_freq buffers)

## Source code in `vllm/model_executor/models/llava_onevision2.py`


|
|

###

`_build_window_cu_seqlens(grid_thw)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.llava_onevision2.LlavaOnevision2VisionTower._build_window_cu_seqlens)

Build cu_seqlens that chunk each sample's T-axis into windows of `frame_windows_size`

frames.

Returns an int32 `np.ndarray`

of shape [num_windows+1] (the canonical prefix-sum format). Backend-specific transforms are applied afterwards via `MMEncoderAttention.maybe_recompute_cu_seqlens`

.

## Source code in `vllm/model_executor/models/llava_onevision2.py`


##

`_create_field_factory(spatial_merge_size)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.llava_onevision2._create_field_factory)

Build the per-batch field-config callback.

OV2-specific: also exposes `patch_positions`

as a flat-from-sizes field, sized by the total per-image patch count (T*H*W). The merger and the 3-D RoPE both consume it.

## Source code in `vllm/model_executor/models/llava_onevision2.py`


##

`_expand_video_markers_in_prompt(prompt, per_video_timestamps, *, timestamp_decimals)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.llava_onevision2._expand_video_markers_in_prompt)

Replace each `<|vision_start|><|video_pad|><|vision_end|>`

with a sequence of `<{t:.Nf} seconds><|vision_start|><|image_pad|><|vision_end|>`

blocks -- one per frame -- matching `vllm_hf_chat._build_prompt`

.

Replacement is positional: the *i*-th marker consumes `per_video_timestamps[i]`

.

## Source code in `vllm/model_executor/models/llava_onevision2.py`


##

`_frame_video_to_pil_and_timestamps(item)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.llava_onevision2._frame_video_to_pil_and_timestamps)

Convert a `(frames_ndarray, metadata)`

video item into `(pil_frames, timestamps_seconds)`

.

Both real `video_url`

inputs (decoded + sampled by the registered `LlavaOnevision2VideoBackend`

) and dummy profiling videos arrive here as a `(frames, metadata)`

tuple because the data parser runs with `video_needs_metadata=True`

. `frames`

is a `(T, H, W, C)`

uint8 array; `metadata`

carries `frames_indices`

and the source `fps`

.

Timestamps follow the qwen_vl_utils policy: `frame_index / original_fps`

. The frame count is padded up to `_TEMPORAL_MERGE_SIZE`

(repeating the last frame) because OV2's vision tower merges frames temporally in pairs.

## Source code in `vllm/model_executor/models/llava_onevision2.py`


##

`_ov2_smart_nframes(total_frames, video_fps, *, fps, min_frames, max_frames)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.llava_onevision2._ov2_smart_nframes)

Replicate `qwen_vl_utils.smart_nframes`

(fps branch).

Returns an even frame count in `[min_frames, min(max_frames, total)]`

.

## Source code in `vllm/model_executor/models/llava_onevision2.py`


##

`_validate_video_source(path, model_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.llava_onevision2._validate_video_source)

Confine a codec video path to `--allowed-local-media-path`

.

The codec backend keeps the raw path string alive past vLLM's `MultiModalDataParser`

and hands it to the trust-remote-code codec module, which opens it directly via `cv2.VideoCapture`

/ ffmpeg. That bypasses both `MediaConnector`

's access controls and its redirect handling (`VLLM_MEDIA_URL_ALLOW_REDIRECTS`

), so we restrict the codec backend to **local files only**: remote `http(s)`

/ `data`

URLs are rejected here and must instead go through the frame backend (a registered `VIDEO_LOADER_REGISTRY`

loader), which rides vLLM's connector and its domain/redirect gates.

Returns the *resolved* absolute path so the codec module opens exactly the file that was validated, closing the validate-vs-open (symlink-retarget) window. Mirrors the confinement in `MediaConnector._load_file_url`

.

## Source code in `vllm/model_executor/models/llava_onevision2.py`


##

`prepare_codec_video_input(video_path)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.llava_onevision2.prepare_codec_video_input)

Wrap a video path for vLLM's MultiModalDataParser + OV2 codec backend.

Returns `(dummy_ndarray, metadata)`

where the ndarray satisfies the parser's 4-D shape check and the metadata carries the actual path to our `_apply_hf_processor_main`

. Use as::

```
multi_modal_data = {"video": prepare_codec_video_input("foo.mp4")}
```


The dummy ndarray bytes encode a hash of `video_path`

so distinct codec videos get distinct mm_hashes: the parser drops the metadata dict before hashing (only the ndarray reaches MultiModalHasher), so without this variance every video after the first would collide and skip the encoder.