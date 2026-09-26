# [Issue #44] Support on Huggingface transformers

source: https://github.com/AI-Hypercomputer/JetStream/issues/44
state: closed | updated: 2024-04-26T09:35:54Z
labels: 

## 正文

Hi, great work! Do you have any future plans on supporting the Flax/Jax implemented Huggingface transformer models?

## 评论 (2)

### vipannalla · 2024-04-25

JetStream is agnostic to particular model frameworks and should work for all LLM models if the engine supports it. Currently, we have two reference engine implementations -- one for [JAX](https://github.com/google/JetStream/blob/main/docs/online-inference-with-maxtext-engine.md) models and one for [Pytorch](https://github.com/google/jetstream-pytorch/blob/main/README.md) models. 

Can you try/check if your model is supported in Maxtext repo? 

### ImKeTT · 2024-04-26

Thanks for your reply, seems that we might need a lot more efforts if we want to use LLMs that are currently not supported in Maxtext.
