source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/chatglm/
lastmod: 2026-09-24

#

`vllm.model_executor.models.chatglm`

[¶](https://docs.vllm.ai#vllm.model_executor.models.chatglm)

Inference-only ChatGLM model compatible with THUDM weights.

Classes:

-
–[GLMBlock](https://docs.vllm.ai#vllm.model_executor.models.chatglm.GLMBlock)A single transformer layer.

-
–[GLMMLP](https://docs.vllm.ai#vllm.model_executor.models.chatglm.GLMMLP)MLP.

-
–[GLMTransformer](https://docs.vllm.ai#vllm.model_executor.models.chatglm.GLMTransformer)Transformer class.


##

`GLMBlock`

[¶](https://docs.vllm.ai#vllm.model_executor.models.chatglm.GLMBlock)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

A single transformer layer.

Transformer layer takes input with size [s, b, h] and returns an output of the same size.

## Source code in `vllm/model_executor/models/chatglm.py`


##

`GLMMLP`

[¶](https://docs.vllm.ai#vllm.model_executor.models.chatglm.GLMMLP)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

MLP.

MLP will take the input with h hidden state, project it to 4*h hidden dimension, perform nonlinear transformation, and project the state back into h hidden dimension.

## Source code in `vllm/model_executor/models/chatglm.py`


##

`GLMTransformer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.chatglm.GLMTransformer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Transformer class.