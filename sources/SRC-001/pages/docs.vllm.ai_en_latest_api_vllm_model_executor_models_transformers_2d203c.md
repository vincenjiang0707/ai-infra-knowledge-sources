source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/transformers/
lastmod: 2026-09-24

#

`vllm.model_executor.models.transformers`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers)

Wrapper around `transformers`

models.

Modules:

-
–[base](https://docs.vllm.ai/base/#vllm.model_executor.models.transformers.base)Transformers modeling backend base class.

-
–[causal](https://docs.vllm.ai/causal/#vllm.model_executor.models.transformers.causal)Transformers modeling backend mixin for causal language models.

-
–[fuser](https://docs.vllm.ai/fuser/#vllm.model_executor.models.transformers.fuser)Fuser detection for the Transformers modeling backend.

-
–[fusers](https://docs.vllm.ai/fusers/#vllm.model_executor.models.transformers.fusers)Concrete fusers for the Transformers modeling backend.

-
–[fx_utils](https://docs.vllm.ai/fx_utils/#vllm.model_executor.models.transformers.fx_utils)fx tracing and forward-source rewriting for the Transformers backend fusers.

-
–[layers](https://docs.vllm.ai/layers/#vllm.model_executor.models.transformers.layers)Layer provider resolution for the Transformers modeling backend.

-
–[legacy](https://docs.vllm.ai/legacy/#vllm.model_executor.models.transformers.legacy)Transformers modeling backend mixin for legacy models.

-
–[moe](https://docs.vllm.ai/moe/#vllm.model_executor.models.transformers.moe)Transformers modeling backend mixin for Mixture of Experts (MoE) models.

-
–[multimodal](https://docs.vllm.ai/multimodal/#vllm.model_executor.models.transformers.multimodal)Transformers modeling backend mixin for multi-modal models.

-
–[pooling](https://docs.vllm.ai/pooling/#vllm.model_executor.models.transformers.pooling)Transformers modeling backend mixins for pooling models.

-
–[utils](https://docs.vllm.ai/utils/#vllm.model_executor.models.transformers.utils)Transformers modeling backend utilities.


Functions:

-
–[__getattr__](https://docs.vllm.ai#vllm.model_executor.models.transformers.__getattr__)Handle imports of non-existent classes with a helpful error message.

-
–[check_sinks](https://docs.vllm.ai#vllm.model_executor.models.transformers.check_sinks)Fail loudly if the model applies a sink the attention layer will not.


##

`__getattr__(name)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.__getattr__)

Handle imports of non-existent classes with a helpful error message.

## Source code in `vllm/model_executor/models/transformers/__init__.py`


##

`check_sinks(module, self_attn, s_aux)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.check_sinks)

Fail loudly if the model applies a sink the attention layer will not.

Only the attention impl can fold a sink into the softmax denominator, so a sink that never reached `Attention`

is dropped and every softmax is subtly wrong.