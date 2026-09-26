# [Issue #3161] [Feature] Replace nested tensor logic with pytree

source: https://github.com/vllm-project/llm-compressor/issues/3161
state: open | updated: 2026-09-18T06:39:36Z
labels: enhancement, good first issue, good follow-up issue

## 正文

## Background ##
LLM Compressor and Compressed Tensors both use logic which flattens and unflattens nested structures with tensors in them. The two examples which come to mind are below. I believe these are the only examples
* [IntermediatesCache](https://github.com/vllm-project/llm-compressor/blob/main/src/llmcompressor/pipelines/cache.py#L33)
* [send_tensors](https://github.com/vllm-project/compressed-tensors/blob/a2a210e9001d6ac45b6f294f8a66a87384c7da55/src/compressed_tensors/offload/utils.py#L30)

`torch.utils._pytree` does a very similar thing, it may be possible to leverage this module to perform these operations in a more robust way.

## Suggested Steps ##
1. Find all examples of nested flattening/unflattening of tensor structures
2. Try using `torch.utils._pytree` to do the flattening/unflattening
3. Add additional tests to determine edge case behavior

## 评论 (10)

### aayush7511 · 2026-09-10

@kylesayrs can I work on this? 

### amacharla15 · 2026-09-11

Hi @kylesayrs , I did a quick survey of both repos for step 1 before starting any implementation.

_**compressed-tensors: send_tensors appears to be the only generic recursive tensor-container walker. I found no existing torch.utils._pytree usage in this repo, and no dedicated tests for send_tensors' nested-container behavior.**_

llm-compressor: besides IntermediatesCache, I found two more production walkers in pytorch/utils/helpers.py: tensors_to_device, which is used from pipelines/basic/pipeline.py, and tensors_to_precision, which I couldn't find a production caller for. Both recurse over OrderedDict / Mapping / tuple / Iterable. Not sure if you want those included in scope.

Inside IntermediatesCache, _offload_value and _onload_value transform and rebuild the structure, while _pin_intermediate and _size_helper only traverse it.

One compatibility issue I checked: on torch 2.10.0, a plain @dataclass containing a tensor is treated by tree_flatten as a single leaf (spec: *), so tensors inside it are not visited unless the dataclass is registered. Since the current walkers explicitly handle dataclasses, that behavior would need to be preserved. OrderedDict, dict, and list traverse as expected; None is a leaf.

The current helpers also have slightly different fallback behavior: send_tensors passes unknown leaves through, IntermediatesCache wraps/warns, and the helpers in pytorch/utils/helpers.py raise. I’d preserve those semantics unless there’s a reason to standardize them.

**_If this is still available, I’d be interested in taking it on to work further._**

### kylesayrs · 2026-09-11

@amacharla15 Great call outs! The functions you mentioned all seem like they could benefit from the pytree abstraction

### kylesayrs · 2026-09-11

I'm going to assign to @aayush7511, but @aayush7511 please let me know if you want support at any time from myself or @amacharla15 

### amacharla15 · 2026-09-11

Thanks @kylesayrs  ! Since tensors_to_device and tensors_to_precision live in a separate module and have somewhat different fallback behavior from IntermediatesCache_**, would you prefer those stay part of #3161 or be split into a follow-up issue? If you'd rather split them out, I'd be happy to take that piece.**_

One thing that might matter for scoping: I couldn't find a production caller for tensors_to_precision, so it may be worth confirming whether that helper is still intended to be kept and refactored.

### aayush7511 · 2026-09-13

Thanks @kylesayrs, I'll do some research and get back to you!

### aayush7511 · 2026-09-13

Hey @kylesayrs, the only other flattening and unflattening use cases I found are in helpers.py. 

https://github.com/vllm-project/llm-compressor/blob/main/src/llmcompressor/pytorch/utils/helpers.py#L88-L124

https://github.com/vllm-project/llm-compressor/blob/main/src/llmcompressor/pytorch/utils/helpers.py#L38-L85

I'll start with the implementation, but if you want me to continue looking for more use-cases, feel free to let me know. 




### kylesayrs · 2026-09-14

@amacharla15 Yeah, `tensors_to_precision` can probably be removed. I agree that there's no use case for it. w.r.t. `tensors_to_device`, it makes sense to keep it on one PR.

### amacharla15 · 2026-09-15

Thanks @kylesayrs , that makes sense. Just to confirm, if you think it would be useful, I can make a small follow-up PR to remove tensors_to_precision. Please let me know if you'd prefer that. Just confused about the previous comment. Happy to do anything.

### kylesayrs · 2026-09-18

@amacharla15 No need to create a follow up PR for now, let's see what @aayush7511 finds
