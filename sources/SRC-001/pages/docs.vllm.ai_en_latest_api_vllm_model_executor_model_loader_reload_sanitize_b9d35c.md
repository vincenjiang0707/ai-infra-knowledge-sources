source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/reload/sanitize/
lastmod: 2026-09-24

#

`vllm.model_executor.model_loader.reload.sanitize`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.sanitize)

Functions:

-
–[restore_layer_refs](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.sanitize.restore_layer_refs)Restores references to layer held by tensor attributes.

-
–[sanitize_layer_refs](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.sanitize.sanitize_layer_refs)Removes references to layer held by tensor attributes. Specifically, removes the


##

`restore_layer_refs(tensor, layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.sanitize.restore_layer_refs)

Restores references to layer held by tensor attributes.

Used by `restore_layer_on_meta`

to add back layer references, allowing for proper weight loading.

Parameters:

-

(`tensor`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.sanitize.restore_layer_refs(tensor))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)tensor to be sanitized

-

(`layer`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.sanitize.restore_layer_refs(layer))

) –[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)layer whose references should be removed


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)sanitized tensor


## Source code in `vllm/model_executor/model_loader/reload/sanitize.py`


##

`sanitize_layer_refs(tensor, layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.sanitize.sanitize_layer_refs)

Removes references to layer held by tensor attributes. Specifically, removes the `__self__`

attribute of weight loader methods attached to the tensor.

Used by `capture_layer_to_meta`

to avoid circular references to layers in `LAYERWISE_INFO`

, leading to modules never being cleaned up. Without sanitation, tensors will reference layers, and the WeakKeyDictionary will never evict entries, even when the model is deleted.

Parameters:

-

(`tensor`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.sanitize.sanitize_layer_refs(tensor))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)tensor to be sanitized

-

(`layer`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.reload.sanitize.sanitize_layer_refs(layer))

) –[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)layer whose references should be removed


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)sanitized tensor