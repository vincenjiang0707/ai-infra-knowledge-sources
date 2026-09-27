# [Issue #2480] [Feature] Enable GPU offloading for reduced weight movement

source: https://github.com/vllm-project/llm-compressor/issues/2480
state: open | updated: 2026-07-07T18:58:08Z
labels: enhancement, good first issue

## 正文

## Background ##
As of now, LLM Compressor supports and encourages users to offload large models to CPU, then onload each layer onto the GPU sequentially for calibration. This technique ensures that large models do not cause GPU OOM errors. However, this also means that GPU VRAM is under-utilized. We can see a performance benefit for medium-sized models by keeping model weights on GPUs, replacing low-throughput CPU->GPU transfers with faster, PCIe-enabled GPU->GPU transfers.

<img width="541" height="436" alt="Image" src="https://github.com/user-attachments/assets/30618baf-6ba2-4a25-ba07-99ef30065aec" />

Enabling these kinds of work flows was started by [this PR](https://github.com/vllm-project/compressed-tensors/pull/621), but will require additional changes.

## Requested Changes ##
Enable and test GPU offloading. A user will load a model like this:

```python3
model = AutoModelForCausalLM.from_pretrained(..., device_map="auto")  # model is split between GPUs evenly

oneshot(model, ...)
```

Start by enabling this for GPTQ. This will likely require changing the broadcast operation to support updating not only the GPU onload, but the GPU offload (which can now be different devices). Make sure that this function is generic. See also [`finalize_distributed_update`](https://github.com/vllm-project/llm-compressor/pull/2469/changes#diff-b7ef6634599e8e9be330e6a699dc5bac10e6f968e133d82da18d6ac5efb88f26R144-R179). This function should likely live as a compressed-tensors utility
```
def is_device_offload(module):
  return isinstance(module._parameters, DeviceCache) and module._parameters.onload_device != module._parameters.offload_device

for module in modules:
  # update gpu offloads
  if is_device_offload(module):
    for value in module._parameters.offload_values.values():
      dist.broadcast(value, src=assigned_rank[module])

  # update gpu onloads
  if OffloadCache.offloading_disabled:
    for value in module._parameters.values():
      dist.broadcast(value, src=assigned_rank[module])
```

## 评论 (9)

### kylesayrs · 2026-03-17

Assigned to @Etelis

### HDCharles · 2026-03-17

whats the use case here? when will this outperform DDP?

### kylesayrs · 2026-03-17

@HDCharles This feature is orthogonal and composable with DDP. DDP + GPU offloading means that each GPU holds a fraction of the model weights. At loading time, each rank onloads the layer, sourced from whichever GPU holds that fraction of the weights.

### HDCharles · 2026-03-17

oh i see, i thought this was like a dedicated offload gpu

### dzhengAP · 2026-03-20

Hey @kylesayrs @Etelis — happy to collaborate on this. Given my work on distributed broadcast in #2471, I can help with the finalize_distributed_update changes or take the is_device_offload utility migration to compressed-tensors as a standalone piece. Let me know how to best divide the work.

### JINO-ROHIT · 2026-05-27

hey @HDCharles from what i understand, torch splits the model across multi gpu setup. but within llmcompressor, after it processes and updates a layer's weights, it only syncs from one gpu to cpu and disregards if other gpus are present?

if my understanding is  okay, can i pick this up?

### monish-rgb · 2026-07-01

Hi is this issue still available I would like to work on this and will open a PR for this thanks!


### ishrith-gowda · 2026-07-03

Hi @kylesayrs, I see this was assigned to @Etelis in March; if it's gone stale I'd like to pick it up. I did the SmoothQuant mappings in #2174 and have been working in vLLM's weight loading path recently (vllm-project/vllm#47580). Plan per your sketch: add the device-offload predicate to compressed-tensors, extend the distributed update path from #2469 to broadcast to GPU offload devices, scoped to GPTQ first behind device_map="auto", validated with CPU-mockable unit tests plus a calibration wall-time A/B on a multi-GPU node. One question: should offload device selection reuse the accelerate device_map, or do you want an explicit LLM Compressor setting? I can have a draft PR up in a few days.

### ishrith-gowda · 2026-07-07

Following up: the generic update primitive this needs looks like it's being built in compressed-tensors #703 (`update_parameter` / `update_parameter_async` with `update_offload`/`update_onload`), framed around the GPTQ async update case. That seems like the right home for the offload-aware broadcast rather than open-coding it in the modifier.

Happy to do the llm-compressor side once #703 lands: wire GPTQ's `_broadcast_quantized_params` to update the offload copy via that util when `offload_device != onload_device`, GPTQ-first behind `device_map="auto"`, with a multi-GPU calibration A/B. Anything I can do to help move #703 along meanwhile?

