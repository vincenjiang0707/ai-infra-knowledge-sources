source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/diffusion_gemma/
lastmod: 2026-09-27

#

`vllm.model_executor.models.diffusion_gemma`

[¶](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma)

DiffusionGemma model, ModelState, and Sampler for vLLM.

Single Gemma4 backbone run in two modes (like YOCO): - encoder mode: causal attention, writes KV cache - decoder mode: bidirectional attention, reads encoder KV, doesn't write

Same weights, same layers. The only decoder-unique component is a self-conditioning MLP.

Multimodal support: the model always includes a vision tower (shared with Gemma4). Images are encoded through the vision tower and projected into the LM embedding space via Gemma4MultimodalEmbedder.

Classes:

-
–[DiffusionGemmaForConditionalGeneration](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionGemmaForConditionalGeneration)DiffusionGemma for vLLM.

-
–[DiffusionGemmaModelState](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionGemmaModelState)ModelState for DiffusionGemma.

-
–[DiffusionGemmaProcessingInfo](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionGemmaProcessingInfo)Processing info for DiffusionGemma.

-
–[DiffusionGemmaRequestStates](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionGemmaRequestStates)Pre-allocated GPU tensors for DiffusionGemma per-request state.

-
–[DiffusionGemmaSelfConditioning](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionGemmaSelfConditioning)Gated MLP that processes soft embeddings from the previous denoising step.

-
–[DiffusionSampler](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionSampler)Batched accept/renoise sampler for DiffusionGemma.


##

`DiffusionGemmaForConditionalGeneration`

[¶](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionGemmaForConditionalGeneration)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsMultiModal](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal)[SupportsQuant](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsQuant)

DiffusionGemma for vLLM.

Single Gemma4 backbone that switches between encoder and decoder mode. The encoder path uses standard Gemma4 layers (causal attention, KV write). The decoder path uses the same weights with bidirectional attention and KV read-only, plus self-conditioning.

Always includes a vision tower (same as Gemma4) for image understanding.

In practice, the model's forward() dispatches based on the `mode`

kwarg set by DiffusionGemmaModelState.prepare_inputs().

Methods:

-
–[get_mm_mapping](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionGemmaForConditionalGeneration.get_mm_mapping)Get the module prefix mapping for multimodal models.


## Source code in `vllm/model_executor/models/diffusion_gemma.py`


|
|

###

`get_mm_mapping()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionGemmaForConditionalGeneration.get_mm_mapping)

Get the module prefix mapping for multimodal models.

## Source code in `vllm/model_executor/models/diffusion_gemma.py`


##

`DiffusionGemmaModelState`

[¶](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionGemmaModelState)

Bases: [ModelState](https://docs.vllm.ai/v1/worker/gpu/model_states/interface/#vllm.v1.worker.gpu.model_states.interface.ModelState)

ModelState for DiffusionGemma.

Single Gemma4 backbone in two modes: - encoder mode (num_draft_tokens == 0): causal attention, writes KV - decoder mode (num_draft_tokens > 0): bidirectional attention, reads KV

## Source code in `vllm/model_executor/models/diffusion_gemma.py`


|
|

##

`DiffusionGemmaProcessingInfo`

[¶](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionGemmaProcessingInfo)

Bases: [Gemma4ProcessingInfo](https://docs.vllm.ai/gemma4_mm/#vllm.model_executor.models.gemma4_mm.Gemma4ProcessingInfo)

Processing info for DiffusionGemma.

Overrides `get_hf_config`

to accept `DiffusionGemmaConfig`

(which inherits from `PreTrainedConfig`

, not `Gemma4Config`

). Supports image and video modalities.

## Source code in `vllm/model_executor/models/diffusion_gemma.py`


##

`DiffusionGemmaRequestStates`

[¶](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionGemmaRequestStates)

Pre-allocated GPU tensors for DiffusionGemma per-request state.

Follows the indexed-slot pattern used by `RequestState`

.

Methods:

-
–[allowed_tensor](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionGemmaRequestStates.allowed_tensor)`ids`

as an int64 tensor on the device, built once per tuple. -
–[apply_seed_canvases](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionGemmaRequestStates.apply_seed_canvases)Replace the canvas of every seeded slot among

`slots_gpu`

. -
–[batch_allowed](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionGemmaRequestStates.batch_allowed)The allowed ids shared by every one of

`slots`

, or None. -
–[init_canvas](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionGemmaRequestStates.init_canvas)Initialize canvas with random tokens for the given slots.

-
–[set_pins](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionGemmaRequestStates.set_pins)Hold

`positions`

of the slot's seed canvas through every denoise -
–[set_seed_canvas](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionGemmaRequestStates.set_seed_canvas)`ids`

covers the slot's canvas width; positions past it are never

## Source code in `vllm/model_executor/models/diffusion_gemma.py`


|
|

###

`allowed_tensor(ids)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionGemmaRequestStates.allowed_tensor)

`ids`

as an int64 tensor on the device, built once per tuple.

## Source code in `vllm/model_executor/models/diffusion_gemma.py`


###

`apply_seed_canvases(slots_np, slots_gpu)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionGemmaRequestStates.apply_seed_canvases)

Replace the canvas of every seeded slot among `slots_gpu`

.

## Source code in `vllm/model_executor/models/diffusion_gemma.py`


###

`batch_allowed(slots)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionGemmaRequestStates.batch_allowed)

The allowed ids shared by every one of `slots`

, or None.

None means the step runs over the full vocabulary. The sampler then masks each constrained slot's logit rows to its own set, so a constrained request reads the same way whoever shares its batch.

## Source code in `vllm/model_executor/models/diffusion_gemma.py`


###

`init_canvas(slot_indices)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionGemmaRequestStates.init_canvas)

Initialize canvas with random tokens for the given slots.

`slot_indices`

must already be on device to avoid a cpu->gpu sync.

## Source code in `vllm/model_executor/models/diffusion_gemma.py`


###

`set_pins(slot_idx, positions)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionGemmaRequestStates.set_pins)

Hold `positions`

of the slot's seed canvas through every denoise step. Validated against the request's canvas width upstream.

## Source code in `vllm/model_executor/models/diffusion_gemma.py`


###

`set_seed_canvas(slot_idx, ids)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionGemmaRequestStates.set_seed_canvas)

`ids`

covers the slot's canvas width; positions past it are never scheduled.

## Source code in `vllm/model_executor/models/diffusion_gemma.py`


##

`DiffusionGemmaSelfConditioning`

[¶](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionGemmaSelfConditioning)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Gated MLP that processes soft embeddings from the previous denoising step.

Structurally identical to Gemma4MLP but with self_conditioning_size and post_norm without learned scale.

## Source code in `vllm/model_executor/models/diffusion_gemma.py`


##

`DiffusionSampler`

[¶](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionSampler)

Batched accept/renoise sampler for DiffusionGemma.

Follows the same structure as `vllm.v1.worker.gpu.sample.sampler.Sampler`

: decomposed into named methods, all GPU state in pre-allocated buffers, no GPU→CPU syncs on the hot path.

## Source code in `vllm/model_executor/models/diffusion_gemma.py`


|
|

###

`_build_output(input_batch, sampled, num_sampled, per_req_nlogits_np, device, logprobs_tensors=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionSampler._build_output)

Compute num_rejected and build SamplerOutput.

## Source code in `vllm/model_executor/models/diffusion_gemma.py`


###

`_finish_prefills(input_batch, prefill_indices_np)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma.DiffusionSampler._finish_prefills)

Transition requests whose prompt completes this step to denoising.

Initializes their canvas, seeds draft tokens, and flips is_encoder_phase to False. Mid-chunk requests (prompt longer than the token budget) are left untouched so is_encoder_phase stays True and prepare_attn keeps causal attention for their remaining chunks.

## Source code in `vllm/model_executor/models/diffusion_gemma.py`


##

`_compiled_sample_step(new_tokens, argmax_tokens, token_entropy, probs, decode_slots, decode_idx, all_slots, valid_canvas_len, canvas, argmax_canvas, step_tensor, is_encoder_phase, confident_tensor, sc_embeds, embed_weight, normalizer, history, history_len_tensor, max_steps_tensor, pin_mask, seed_canvas, read_only, sampled, num_sampled, draft_tokens, confidence_threshold, vocab_size, CL, ST, entropy_bound, sc_vocab_start, sc_vocab_end, tp_size, tp_group_name, compute_sc=True)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma._compiled_sample_step)

Compiled decode step: confidence → accept/renoise → convergence, as vectorized PyTorch ops over [num_decode, CL] tensors. The per-position statistics (argmax, Gumbel-max sample, entropy, softmax) come from one pass over the logits in `sample_row_stats`

.

## Source code in `vllm/model_executor/models/diffusion_gemma.py`


|
|

##

`_concat_logprob_stashes(parts, cu_num_generated_tokens)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma._concat_logprob_stashes)

Join the logprobs stashed for the requests committing this step.

Each stash is as wide as the widest logprobs request in the batch at the step that request converged, so stashes from different steps can differ in width. Pad the narrow ones the way compute_topk_scores pads a mixed batch: token id 0 at -inf, which the output processor never reports.

## Source code in `vllm/model_executor/models/diffusion_gemma.py`


##

`_denoise_temperature(step_tensor, slots, max_denoising_steps, t_min, t_max)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma._denoise_temperature)

The schedule's temperature for each slot at its current step.

## Source code in `vllm/model_executor/models/diffusion_gemma.py`


##

`_mask_rows_to_allowed(logits, row_starts, row_lens, allowed_per_row)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma._mask_rows_to_allowed)

Mask every column outside a request's allowed ids on that request's rows. Request i owns rows [row_starts[i], +row_lens[i]); None leaves its rows alone. Returns a copy when any row is masked, so the caller's tensor (possibly the runner's) is never written.

Softmax over a masked row equals the K-space distribution the shared fast path computes, so both paths give the same reads. The mask value is a large finite negative rather than -inf: the entropy is probs times log-probs, and 0 * -inf is NaN, while 0 * -1e20 is 0. It stays finite after the greedy temperature clamp (1e-10) scales it by 1e10.