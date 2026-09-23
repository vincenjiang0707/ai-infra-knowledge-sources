source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/transformers/pooling/
lastmod: 2026-09-23

#

`vllm.model_executor.models.transformers.pooling`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.pooling)

Transformers modeling backend mixins for pooling models.

Classes:

-
–[ClassifierWithReshape](https://docs.vllm.ai#vllm.model_executor.models.transformers.pooling.ClassifierWithReshape)Token extraction has already been applied in

`pooler.pooling`

.

##

`ClassifierWithReshape`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.pooling.ClassifierWithReshape)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Token extraction has already been applied in `pooler.pooling`

.

Add dim to match expected input shape of `classifier.forward`

.