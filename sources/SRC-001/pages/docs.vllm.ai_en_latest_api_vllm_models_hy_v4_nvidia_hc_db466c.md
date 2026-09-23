source: https://docs.vllm.ai/en/latest/api/vllm/models/hy_v4/nvidia/hc/
lastmod: 2026-09-23

#

`vllm.models.hy_v4.nvidia.hc`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc)

iHC (independent Hyper-Connections) layers for HY V4 (NVIDIA).

iHC replaces the single residual stream of a standard transformer with `hc_mult`

parallel residual channels. Each decoder sub-block reduces the channels to one hidden state (`HYV4HCPreLayer`

), runs the sub-block, then scatters the result back over the channels (`HYV4HCPostLayer`

). The final `HYV4HCHeadLayer`

merges the channels before the model's output norm.

NOTE: Each of the three steps has an optional single-kernel HPC replacement (`HpcIHCPre`

/ `HpcIHCPost`

/ `HpcIHCHead`

). Pre and post fall back to in-tree Triton kernels on CUDA when HPC is unavailable, then to the eager path. TODO: port the cross-layer post+pre fusion (`HpcIHCPostPre`

) as well; it requires restructuring the decoder-layer forward scheduling.

Classes:

-
–[HYV4HCHeadLayer](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCHeadLayer)iHC head layer (2D-activation adaptation).

-
–[HYV4HCLayer](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCLayer)Wrapper owning one iHC boundary (pre + post) of a decoder sub-block.

-
–[HYV4HCPostLayer](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCPostLayer)iHC post-processing layer (2D-activation adaptation).

-
–[HYV4HCPreLayer](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCPreLayer)iHC pre-processing layer (2D-activation adaptation).


##

`HYV4HCHeadLayer`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCHeadLayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

iHC head layer (2D-activation adaptation).

Merges the iHC channels back into a single hidden state before the final layer norm, using an RMS-normed projection plus sigmoid-gated reduction.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCHeadLayer.forward)Merge the iHC channels into a single hidden state.

-
–[reset_parameters](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCHeadLayer.reset_parameters)Initialize the head gate scale and per-channel gate bias.


## Source code in `vllm/models/hy_v4/nvidia/hc.py`


|
|

###

`forward(x)`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCHeadLayer.forward)

Merge the iHC channels into a single hidden state.

Parameters:

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The merged hidden state

`[num_tokens, d]`

.

## Source code in `vllm/models/hy_v4/nvidia/hc.py`


###

`reset_parameters(init_std=0.006, base_noise_std=0.0)`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCHeadLayer.reset_parameters)

Initialize the head gate scale and per-channel gate bias.

## Source code in `vllm/models/hy_v4/nvidia/hc.py`


##

`HYV4HCLayer`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCLayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Wrapper owning one iHC boundary (pre + post) of a decoder sub-block.

Methods:

-
–[post](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCLayer.post)Apply post-gating and add the residual.

-
–[pre](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCLayer.pre)Reduce the iHC channels and produce the post gates.

-
–[prepare_input](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCLayer.prepare_input)Normalize the sub-block input to 3D when iHC is enabled.


## Source code in `vllm/models/hy_v4/nvidia/hc.py`


|
|

###

`_prepare_input_to_3d(hidden_states)`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCLayer._prepare_input_to_3d)

Reshape the iHC input to `[num_tokens, hc, h]`

.

Accepted inputs are `[num_tokens, hc, h]`

(no-op), `[num_tokens, h]`

(broadcast over the channels) and `[num_tokens, hc * h]`

(reshape).

## Source code in `vllm/models/hy_v4/nvidia/hc.py`


###

`post(output_with_bias, residual, post_gates)`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCLayer.post)

Apply post-gating and add the residual.

## Source code in `vllm/models/hy_v4/nvidia/hc.py`


###

`pre(hidden_states)`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCLayer.pre)

Reduce the iHC channels and produce the post gates.

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)A tuple of the reduced hidden states

`[num_tokens, d]`

, the post -

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| Nonegates

`[num_tokens, hc]`

(`None`

when iHC is disabled) and the -

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)residual (the untouched input).


## Source code in `vllm/models/hy_v4/nvidia/hc.py`


###

`prepare_input(hidden_states)`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCLayer.prepare_input)

Normalize the sub-block input to 3D when iHC is enabled.

##

`HYV4HCPostLayer`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCPostLayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

iHC post-processing layer (2D-activation adaptation).

Applies post-gating to the sub-block output and adds the multi-channel residual (no comb mixing)::

```
y[n, i, d] = post[n, i] * x[n, d] + residual[n, i, d]
```


Methods:

-
–[forward](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCPostLayer.forward)Scatter the sub-block output back onto the iHC channels.


## Source code in `vllm/models/hy_v4/nvidia/hc.py`


###

`forward(x, residual, post)`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCPostLayer.forward)

Scatter the sub-block output back onto the iHC channels.

Parameters:

-

(`x`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCPostLayer.forward(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Attention/MLP output of shape

`[num_tokens, d]`

. -

(`residual`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCPostLayer.forward(residual))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Multi-channel residual

`[num_tokens, hc, d]`

. -

(`post`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCPostLayer.forward(post))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Post gates

`[num_tokens, hc]`

from`HYV4HCPreLayer`

.

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The updated residual channels

`[num_tokens, hc, d]`

.

## Source code in `vllm/models/hy_v4/nvidia/hc.py`


##

`HYV4HCPreLayer`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCPreLayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

iHC pre-processing layer (2D-activation adaptation).

## Steps

- RMS-normalize the flattened
`[num_tokens, hc * d]`

input. - Project to the pre/post gating logits.
- Turn the logits into sigmoid gates.
- Reduce over the channel dim with the pre gates.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCPreLayer.forward)Reduce the iHC channels and emit the post gates.

-
–[reset_parameters](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCPreLayer.reset_parameters)Initialize the gate scale and per-channel gate bias.


## Source code in `vllm/models/hy_v4/nvidia/hc.py`


|
|

###

`forward(x)`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCPreLayer.forward)

Reduce the iHC channels and emit the post gates.

Parameters:

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)A tuple of the pre-gated reduction

`[num_tokens, d]`

and the post -

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)gates

`[num_tokens, hc]`

consumed by`HYV4HCPostLayer`

.

## Source code in `vllm/models/hy_v4/nvidia/hc.py`


###

`reset_parameters(init_std, base_noise_std=0.0)`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.hc.HYV4HCPreLayer.reset_parameters)

Initialize the gate scale and per-channel gate bias.