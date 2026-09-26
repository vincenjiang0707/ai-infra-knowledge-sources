source: https://docs.vllm.ai/en/latest/models/supported_models/
lastmod: 2026-09-24

# Supported Models[¶](https://docs.vllm.ai#supported-models)

vLLM supports [generative](https://docs.vllm.ai/generative_models/) and [pooling](https://docs.vllm.ai/pooling_models/) models across various tasks.

For each task, we list the model architectures that have been implemented in vLLM. Alongside each architecture, we include some popular models that use it.

## Model Implementation[¶](https://docs.vllm.ai#model-implementation)

### vLLM[¶](https://docs.vllm.ai#vllm)

If vLLM natively supports a model, its implementation can be found in [ vllm/model_executor/models](https://github.com/vllm-project/vllm/tree/main/vllm/model_executor/models).

These models are what we list in [supported text models](https://docs.vllm.ai#list-of-text-only-language-models) and [supported multimodal models](https://docs.vllm.ai#list-of-multimodal-language-models).

### Transformers[¶](https://docs.vllm.ai#transformers)

vLLM also supports model implementations that are available in Transformers. We call this feature the "Transformers modeling backend". The performance of models loaded with the Transformers modeling backend should be identical to a dedicated vLLM model implementation.

Currently, the Transformers modeling backend works for the following:

- Modalities: embedding models, language models, vision-language models* and audio-language models
- Architectures: encoder-only, decoder-only, mixture-of-experts
- Attention types: full attention and/or sliding attention

**Vision-language models currently accept only image inputs. Support for video inputs will be added in a future release.*

If the Transformers model implementation follows all the steps in [writing a custom model](https://docs.vllm.ai#writing-custom-models) then, when used with the Transformers modeling backend, it will be compatible with the following features of vLLM:

- All the features listed in the
[compatibility matrix](https://docs.vllm.ai/features/#feature-x-feature) - Any combination of the following vLLM parallelisation schemes:
- Data parallel
- Tensor parallel
- Expert parallel
- Pipeline parallel


Checking if the modeling backend is Transformers is as simple as:

from vllm import LLM
llm = LLM(model=...) # Name or path of your model
llm.apply_model(lambda model: print(type(model)))


If the printed type starts with `Transformers...`

then it's using the Transformers model implementation!

If a model has a vLLM implementation but you would prefer to use the Transformers implementation via the Transformers modeling backend, set `model_impl="transformers"`

for [offline inference](https://docs.vllm.ai/serving/offline_inference/) or `--model-impl transformers`

for the [online serving](https://docs.vllm.ai/serving/online_serving/).

Note

For vision-language models, if you are loading with `dtype="auto"`

, vLLM loads the whole model with config's `dtype`

if it exists. In contrast the native Transformers will respect the `dtype`

attribute of each backbone in the model. That might cause a slight difference in performance.

#### Custom models[¶](https://docs.vllm.ai#custom-models)

If a model is neither supported natively by vLLM nor Transformers, it can still be used in vLLM!

For a model to be compatible with the Transformers modeling backend for vLLM it must:

- be a Transformers compatible custom model (see
[Transformers - Customizing models](https://huggingface.co/docs/transformers/en/custom_models)):- The model directory must have the correct structure (e.g.
`config.json`

is present). `config.json`

must contain`auto_map.AutoModel`

.

- The model directory must have the correct structure (e.g.
- be a Transformers modeling backend for vLLM compatible model (see
[Writing custom models](https://docs.vllm.ai#writing-custom-models)):- Customisation should be done in the base model (e.g. in
`MyModel`

, not`MyModelForCausalLM`

).

- Customisation should be done in the base model (e.g. in

If the compatible model is:

- on the Hugging Face Model Hub, simply set
`trust_remote_code=True`

for[offline-inference](https://docs.vllm.ai/serving/offline_inference/)or`--trust-remote-code`

for the[online serving](https://docs.vllm.ai/serving/online_serving/). - in a local directory, simply pass directory path to
`model=<MODEL_DIR>`

for[offline-inference](https://docs.vllm.ai/serving/offline_inference/)or`vllm serve <MODEL_DIR>`

for the[online serving](https://docs.vllm.ai/serving/online_serving/).

This means that, with the Transformers modeling backend for vLLM, new models can be used before they are officially supported in Transformers or vLLM!

#### Writing custom models[¶](https://docs.vllm.ai#writing-custom-models)

This section details the necessary modifications to make to a Transformers compatible custom model that make it compatible with the Transformers modeling backend for vLLM. (We assume that a Transformers compatible custom model has already been created, see [Transformers - Customizing models](https://huggingface.co/docs/transformers/en/custom_models)).

To make your model compatible with the Transformers modeling backend:

`MyAttention`

must use`ALL_ATTENTION_FUNCTIONS`

to call attention.- It must make exactly one such call. vLLM attaches one
layer per`Attention`

`MyAttention`

module. `MyAttention`

must contain a unique`layer_idx`

. vLLM keys its KV cache using this index.- Pass
`scaling=`

to the interface if your scale is not`head_size**-0.5`

. vLLM reads it from the call to the attention interface.

- It must make exactly one such call. vLLM attaches one
- If your model is encoder-only:
- Add
`is_causal = False`

to`MyAttention`

.

- Add
- If your model is mixture-of-experts (MoE):
- Your sparse MoE block must have an attribute called
`experts`

. - The class of
`experts`

(`MyExperts`

) must either:- Inherit from
`nn.ModuleList`

(naive). - Or contain all 3D
`nn.Parameters`

(packed).

- Inherit from
`MyExperts.forward`

must accept`hidden_states`

,`top_k_index`

,`top_k_weights`

.

- Your sparse MoE block must have an attribute called

Note

`MyModel`

no longer needs `_supports_attention_backend = True`

, and `kwargs`

no longer need to be passed down through every module from `MyModel`

to `MyAttention`

. vLLM reaches its attention layer through `MyAttention`

itself, so all it asks is that `MyAttention`

dispatches through the interface.

## modeling_my_model.py

from transformers import PreTrainedModel
from torch import nn
class MyAttention(nn.Module):
is_causal = False # Only do this for encoder-only models
def __init__(self, config, layer_idx):
...
self.config = config
self.layer_idx = layer_idx
self.scaling = self.head_dim**-0.5
...
def forward(self, hidden_states, **kwargs):
...
attention_interface = ALL_ATTENTION_FUNCTIONS.get_interface(
self.config._attn_implementation, eager_attention_forward
)
attn_output, attn_weights = attention_interface(
self,
query_states,
key_states,
value_states,
scaling=self.scaling,
**kwargs,
)
...
# Only do this for mixture-of-experts models
class MyExperts(nn.ModuleList):
def forward(self, hidden_states, top_k_index, top_k_weights):
...
# Only do this for mixture-of-experts models
class MySparseMoEBlock(nn.Module):
def __init__(self, config):
...
self.experts = MyExperts(config)
...
def forward(self, hidden_states: torch.Tensor):
...
hidden_states = self.experts(hidden_states, top_k_index, top_k_weights)
...
class MyModel(PreTrainedModel):
...


Here is what happens in the background when this model is loaded:

- The config is loaded.
`MyModel`

Python class is loaded from the`auto_map`

in config, and we check that the model`_can_set_attn_implementation()`

.`MyModel`

is loaded into one of the Transformers modeling backend classes in[vllm/model_executor/models/transformers](https://github.com/vllm-project/vllm/tree/main/vllm/model_executor/models/transformers)which sets`self.config._attn_implementation = "vllm"`

so that vLLM's attention layer is used.

That's it!

For your model to be compatible with vLLM's tensor parallel and/or pipeline parallel features, you may need to add `base_model_tp_plan`

and/or `base_model_pp_plan`

to your model's config class:

## configuration_my_model.py

```bash
from transformers import PreTrainedConfig
class MyConfig(PreTrainedConfig):
base_model_tp_plan = {
"layers.*.self_attn.k_proj": "colwise",
"layers.*.self_attn.v_proj": "colwise",
"layers.*.self_attn.o_proj": "rowwise",
"layers.*.mlp.gate_proj": "colwise",
"layers.*.mlp.up_proj": "colwise",
"layers.*.mlp.down_proj": "rowwise",
}
base_model_pp_plan = {
"embed_tokens": (["input_ids"], ["inputs_embeds"]),
"layers": (["hidden_states", "attention_mask"], ["hidden_states"]),
"norm": (["hidden_states"], ["hidden_states"]),
}
```


`base_model_tp_plan`

is a`dict`

that maps fully qualified layer name patterns to tensor parallel styles (currently only`"colwise"`

and`"rowwise"`

are supported).- vLLM infers the tensor parallel style of standard attention (
`q`

/`k`

/`v`

/`o_proj`

) and gated-MLP/experts (`gate`

/`up`

/`down_proj`

) projections if it can fuse them, so these may not need to be listed.`base_model_tp_plan`

is only*required*for layers that do not follow these patterns; any linear that is neither fused nor named in the plan is replicated.

- vLLM infers the tensor parallel style of standard attention (
`base_model_pp_plan`

is a`dict`

that maps direct child layer names to`tuple`

s of`list`

s of`str`

s:- You only need to do this for layers which are not present on all pipeline stages
- vLLM assumes that there will be only one
`nn.ModuleList`

, which is distributed across the pipeline stages - When no
`base_model_pp_plan`

is provided, the Transformers modelling backend infers the split from the text model's sole`nn.ModuleList`

, keeping the parameter-bearing modules around it (input embeddings, final norm) on the first/last stage (depending on declaration order) and parameter-free modules (e.g. rotary embeddings) on every stage - The
`list`

in the first element of the`tuple`

contains the names of the input arguments - The
`list`

in the last element of the`tuple`

contains the names of the variables the layer outputs to in your modeling code


### Plugins[¶](https://docs.vllm.ai#plugins)

Some model architectures are supported via vLLM plugins. These plugins extend vLLM's capabilities through the [plugin system](https://docs.vllm.ai/design/plugin_system/).

| Architecture | Models | Plugin Repository |
|---|---|---|
`BartForConditionalGeneration` | BART |
|

`Florence2ForConditionalGeneration`

[bart-plugin](https://github.com/vllm-project/bart-plugin)For other model architectures not natively supported, in particular for Encoder-Decoder models, we recommend following a similar pattern by implementing support through the plugin system.

## Loading a Model[¶](https://docs.vllm.ai#loading-a-model)

### Hugging Face Hub[¶](https://docs.vllm.ai#hugging-face-hub)

By default, vLLM loads models from [Hugging Face (HF) Hub](https://huggingface.co/models). To change the download path for models, you can set the `HF_HOME`

environment variable; for more details, refer to [their official documentation](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hfhome).

To determine whether a given model is natively supported, you can check the `config.json`

file inside the HF repository. If the `"architectures"`

field contains a model architecture listed below, then it should be natively supported.

Models do not *need* to be natively supported to be used in vLLM. The [Transformers modeling backend](https://docs.vllm.ai#transformers) enables you to run models directly using their Transformers implementation (or even remote code on the Hugging Face Model Hub!).

Tip

The easiest way to check if your model is really supported at runtime is to run the program below:

from vllm import LLM
# For generative models (runner=generate) only
llm = LLM(model=..., runner="generate") # Name or path of your model
output = llm.generate("Hello, my name is")
print(output)
# For pooling models (runner=pooling) only
llm = LLM(model=..., runner="pooling") # Name or path of your model
output = llm.encode("Hello, my name is")
print(output)


If vLLM successfully returns text (for generative models) or hidden states (for pooling models), it indicates that your model is supported.

Otherwise, please refer to [Adding a New Model](https://docs.vllm.ai/contributing/model/) for instructions on how to implement your model in vLLM. Alternatively, you can [open an issue on GitHub](https://github.com/vllm-project/vllm/issues/new/choose) to request vLLM support.

#### Download a model[¶](https://docs.vllm.ai#download-a-model)

If you prefer, you can use the Hugging Face CLI to [download a model](https://huggingface.co/docs/huggingface_hub/guides/cli#hf-download) or specific files from a model repository:

# Download a model
hf download HuggingFaceH4/zephyr-7b-beta
# Specify a custom cache directory
hf download HuggingFaceH4/zephyr-7b-beta --cache-dir ./path/to/cache
# Download a specific file from a model repo
hf download HuggingFaceH4/zephyr-7b-beta eval_results.json


#### List the downloaded models[¶](https://docs.vllm.ai#list-the-downloaded-models)

Use the Hugging Face CLI to [manage models](https://huggingface.co/docs/huggingface_hub/guides/manage-cache#scan-your-cache) stored in local cache:

# List cached models
hf cache list -q
# Show detailed (verbose) output
hf cache list
# Specify a custom cache directory
hf cache list --dir ~/.cache/huggingface/hub


#### Delete a cached model[¶](https://docs.vllm.ai#delete-a-cached-model)

Use the Hugging Face CLI to [delete downloaded model](https://huggingface.co/docs/huggingface_hub/guides/manage-cache#clean-your-cache) from the cache:

#### Using a proxy[¶](https://docs.vllm.ai#using-a-proxy)

Here are some tips for loading/downloading models from Hugging Face using a proxy:

- Set the proxy globally for your session (or set it in the profile file):

- Set the proxy for just the current command:

https_proxy=http://your.proxy.server:port hf download <model_name>
# or use vllm cmd directly
https_proxy=http://your.proxy.server:port vllm serve <model_name>


- Set the proxy in Python interpreter:

import os
os.environ["http_proxy"] = "http://your.proxy.server:port"
os.environ["https_proxy"] = "http://your.proxy.server:port"


### MatrixHub[¶](https://docs.vllm.ai#matrixhub)

[MatrixHub](https://github.com/matrixhub-ai/matrixhub) is a self-hosted model registry and distribution layer that caches models from upstream hubs and serves them over a Hugging Face-compatible API inside your own network.

Since the API is Hugging Face-compatible, you only need to point `HF_ENDPOINT`

at your MatrixHub instance:

vLLM then downloads model weights from MatrixHub over the internal network instead of the public Hugging Face Hub, which is useful for air-gapped clusters and for avoiding repeated downloads across nodes.

See the [MatrixHub guide for vLLM](https://matrixhub.ai/docs/guides/use-with-vllm/) for an end-to-end walkthrough, including Docker and Kubernetes deployment examples.

### ModelScope[¶](https://docs.vllm.ai#modelscope)

To use models from [ModelScope](https://www.modelscope.cn) instead of Hugging Face Hub, set an environment variable:

And use with `trust_remote_code=True`

.

from vllm import LLM
llm = LLM(model=..., revision=..., runner=..., trust_remote_code=True)
# For generative models (runner=generate) only
output = llm.generate("Hello, my name is")
print(output)
# For pooling models (runner=pooling) only
output = llm.encode("Hello, my name is")
print(output)


## Feature Status Legend[¶](https://docs.vllm.ai#feature-status-legend)

-
✅︎ indicates that the feature is supported for the model.

-
🚧 indicates that the feature is planned but not yet supported for the model.

-
⚠️ indicates that the feature is available but may have known issues or limitations.


## List of Text-only Language Models[¶](https://docs.vllm.ai#list-of-text-only-language-models)

### Generative Models[¶](https://docs.vllm.ai#generative-models)

See [this page](https://docs.vllm.ai/generative_models/) for more information on how to use generative models.

#### Text Generation[¶](https://docs.vllm.ai#text-generation)

These models primarily accept the [ LLM.generate](https://docs.vllm.ai/generative_models/#llmgenerate) API. Chat/Instruct models additionally support the

[API.](https://docs.vllm.ai/generative_models/#llmchat)

`LLM.chat`

| Architecture | Models | Example HF Models |
|
|---|

[PP](https://docs.vllm.ai/serving/parallelism_scaling/)

`AfmoeForCausalLM`

`ApertusForCausalLM`

`swiss-ai/Apertus-8B-2509`

, `swiss-ai/Apertus-70B-Instruct-2509`

, etc.`ArceeForCausalLM`

`arcee-ai/AFM-4.5B-Base`

, etc.`AXK1ForCausalLM`

`skt/A.X-K1`

, etc.`BailingMoeForCausalLM`

`inclusionAI/Ling-lite-1.5`

, `inclusionAI/Ling-plus`

, etc.`BailingMoeV2ForCausalLM`

`inclusionAI/Ling-mini-2.0`

, etc.`BailingMoeV2_5ForCausalLM`

`inclusionAI/Ling-2.5-1T`

, `inclusionAI/Ring-2.5-1T`

`BailingMoeV3ForCausalLM`

`inclusionAI/Ling-3.0-flash`

`BloomForCausalLM`

`bigscience/bloom`

, `bigscience/bloomz`

, etc.`ChatGLMModel`

, `ChatGLMForConditionalGeneration`

`zai-org/chatglm2-6b`

, `zai-org/chatglm3-6b`

, `thu-coai/ShieldLM-6B-chatglm3`

, etc.`CohereForCausalLM`

, `Cohere2ForCausalLM`

`CohereLabs/c4ai-command-r-v01`

, `CohereLabs/c4ai-command-r7b-12-2024`

, `CohereLabs/c4ai-command-a-03-2025`

, `CohereLabs/command-a-reasoning-08-2025`

, etc.`Cohere2MoeForCausalLM`

`CohereLabs/North-Mini-Code`

, etc.`CwmForCausalLM`

`facebook/cwm`

, etc.`DbrxForCausalLM`

`databricks/dbrx-base`

, `databricks/dbrx-instruct`

, etc.`DeciLMForCausalLM`

`nvidia/Llama-3_3-Nemotron-Super-49B-v1`

, etc.`DeepseekForCausalLM`

`deepseek-ai/deepseek-llm-67b-base`

, `deepseek-ai/deepseek-llm-7b-chat`

, etc.`DeepseekV2ForCausalLM`

`deepseek-ai/DeepSeek-V2`

, `deepseek-ai/DeepSeek-V2-Chat`

, etc.`DeepseekV3ForCausalLM`

`deepseek-ai/DeepSeek-V3`

, `deepseek-ai/DeepSeek-R1`

, `deepseek-ai/DeepSeek-V3.1`

, etc.`DeepseekV32ForCausalLM`

`deepseek-ai/DeepSeek-V3.2`

, etc.`DeepseekV4ForCausalLM`

`deepseek-ai/DeepSeek-V4-Flash`

, `deepseek-ai/DeepSeek-V4-Pro`

, etc.`DotsOCRForCausalLM`

`rednote-hilab/dots.ocr`

`Ernie4_5ForCausalLM`

`baidu/ERNIE-4.5-0.3B-PT`

, etc.`Ernie4_5_MoeForCausalLM`

`baidu/ERNIE-4.5-21B-A3B-PT`

, `baidu/ERNIE-4.5-300B-A47B-PT`

, etc.`ExaoneForCausalLM`

`LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct`

, etc.`ExaoneMoeForCausalLM`

`LGAI-EXAONE/K-EXAONE-236B-A23B`

, `LGAI-EXAONE/K-EXAONE-2.0-750B-A37B`

, etc.`Exaone4ForCausalLM`

`LGAI-EXAONE/EXAONE-4.0-32B`

, etc.`FalconForCausalLM`

`tiiuae/falcon-7b`

, `tiiuae/falcon-40b`

, `tiiuae/falcon-rw-7b`

, etc.`FalconMambaForCausalLM`

`tiiuae/falcon-mamba-7b`

, `tiiuae/falcon-mamba-7b-instruct`

, etc.`FalconH1ForCausalLM`

`tiiuae/Falcon-H1-34B-Base`

, `tiiuae/Falcon-H1-34B-Instruct`

, etc.`GemmaForCausalLM`

`google/gemma-2b`

, `google/gemma-1.1-2b-it`

, etc.`Gemma2ForCausalLM`

`google/gemma-2-9b`

, `google/gemma-2-27b`

, etc.`Gemma3ForCausalLM`

`google/gemma-3-1b-it`

, etc.`Gemma3nForCausalLM`

`google/gemma-3n-E2B-it`

, `google/gemma-3n-E4B-it`

, etc.`Gemma4ForCausalLM`

`google/gemma-4-E2B-it`

, etc.`GlmForCausalLM`

`zai-org/glm-4-9b-chat-hf`

, etc.`Glm4ForCausalLM`

`zai-org/GLM-4-32B-0414`

, etc.`Glm4MoeForCausalLM`

`zai-org/GLM-4.5`

, etc.`Glm4MoeLiteForCausalLM`

`zai-org/GLM-4.7-Flash`

, etc.`GlmMoeDsaForCausalLM`

`zai-org/GLM-5`

, etc.`GPT2LMHeadModel`

`openai-community/gpt2`

, `openai-community/gpt2-xl`

, etc.`GPTJForCausalLM`

`EleutherAI/gpt-j-6b`

, `nomic-ai/gpt4all-j`

, etc.`GPTNeoXForCausalLM`

`EleutherAI/gpt-neox-20b`

, `EleutherAI/pythia-12b`

, `OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5`

, `databricks/dolly-v2-12b`

, `stabilityai/stablelm-tuned-alpha-7b`

, etc.`GptOssForCausalLM`

`openai/gpt-oss-120b`

, `openai/gpt-oss-20b`

`GraniteForCausalLM`

`ibm-granite/granite-3.0-2b-base`

, `ibm-granite/granite-3.1-8b-instruct`

, `ibm/PowerLM-3b`

, etc.`GraniteMoeForCausalLM`

`ibm-granite/granite-3.0-1b-a400m-base`

, `ibm-granite/granite-3.0-3b-a800m-instruct`

, `ibm/PowerMoE-3b`

, etc.`GraniteMoeHybridForCausalLM`

`ibm-granite/granite-4.0-tiny-preview`

, etc.`GraniteMoeSharedForCausalLM`

`ibm-research/moe-7b-1b-active-shared-experts`

(test model)`GraniteMoeSWAForCausalLM`

`ibm-granite/granite-swash-3b-a600m`

`GraniteSWAForCausalLM`

`ibm-granite/granite-swash-2b`

`HrmTextForCausalLM`

`sapientinc/HRM-Text-1B`

, etc.`HYV3ForCausalLM`

`tencent/Hy3-preview-Base`

, `tencent/Hy3-preview`

, `tencent/Hy3`

, `tencent/Hy3-FP8`

`HYV4ForCausalLM`

`tencent/Hy4-preview`

, `tencent/Hy4-preview-FP8`

`HyperCLOVAXForCausalLM`

`naver-hyperclovax/HyperCLOVAX-SEED-Think-14B`

`InternLM2ForCausalLM`

`internlm/internlm2-7b`

, `internlm/internlm2-chat-7b`

, etc.`InternLM3ForCausalLM`

`internlm/internlm3-8b-instruct`

, etc.`IQuestCoderForCausalLM`

`IQuestLab/IQuest-Coder-V1-40B-Instruct`

, etc.`IQuestLoopCoderForCausalLM`

`IQuestLab/IQuest-Coder-V1-40B-Loop-Instruct`

, etc.`Jais2ForCausalLM`

`inceptionai/Jais-2-8B-Chat`

, `inceptionai/Jais-2-70B-Chat`

, etc.`JambaForCausalLM`

`ai21labs/AI21-Jamba-1.5-Large`

, `ai21labs/AI21-Jamba-1.5-Mini`

, `ai21labs/Jamba-v0.1`

, etc.`K2HorizonForCausalLM`

`IFM/K2-Horizon-7B`

, `IFM/K2-Horizon-375B`

`KimiLinearForCausalLM`

`moonshotai/Kimi-Linear-48B-A3B-Base`

, `moonshotai/Kimi-Linear-48B-A3B-Instruct`

`Lfm2ForCausalLM`

`LiquidAI/LFM2-1.2B`

, `LiquidAI/LFM2-700M`

, `LiquidAI/LFM2-350M`

, etc.`Lfm2MoeForCausalLM`

`LiquidAI/LFM2-8B-A1B-preview`

, etc.`LlamaForCausalLM`

`meta-llama/Meta-Llama-3.1-405B-Instruct`

, `meta-llama/Meta-Llama-3.1-70B`

, `meta-llama/Meta-Llama-3-70B-Instruct`

, `meta-llama/Llama-2-70b-hf`

, `01-ai/Yi-34B`

, etc.`LongcatFlashForCausalLM`

`meituan-longcat/LongCat-Flash-Chat`

, `meituan-longcat/LongCat-Flash-Chat-FP8`

`MambaForCausalLM`

`state-spaces/mamba-130m-hf`

, `state-spaces/mamba-790m-hf`

, `state-spaces/mamba-2.8b-hf`

, etc.`Mamba2ForCausalLM`

`mistralai/Mamba-Codestral-7B-v0.1`

, etc.`MellumForCausalLM`

`JetBrains/Mellum2-12B-A2.5B-Base`

, etc.`MiMoForCausalLM`

`XiaomiMiMo/MiMo-7B-RL`

, etc.`MiMoV2FlashForCausalLM`

`XiaomiMiMo/MiMo-V2-Flash`

, etc.`MiMoV2ForCausalLM`

`XiaomiMiMo/MiMo-V2.5-Pro`

, etc.`MiniCPMForCausalLM`

`openbmb/MiniCPM-2B-sft-bf16`

, `openbmb/MiniCPM-2B-dpo-bf16`

, `openbmb/MiniCPM-S-1B-sft`

, etc.`MiniCPM3ForCausalLM`

`openbmb/MiniCPM3-4B`

, etc.`MiniMaxM2ForCausalLM`

`MiniMaxAI/MiniMax-M2`

, etc.`MiniMaxM3SparseForCausalLM`

`MiniMaxAI/MiniMax-M3`

, `MiniMaxAI/MiniMax-M3-MXFP8`

, etc.`MistralForCausalLM`

`mistralai/Ministral-3-3B-Instruct-2512`

, `mistralai/Mistral-7B-v0.1`

, `mistralai/Mistral-7B-Instruct-v0.1`

, etc.`MistralLarge3ForCausalLM`

`mistralai/Mistral-Large-3-675B-Base-2512`

, `mistralai/Mistral-Large-3-675B-Instruct-2512`

, etc.`MixtralForCausalLM`

`mistralai/Mixtral-8x7B-v0.1`

, `mistralai/Mixtral-8x7B-Instruct-v0.1`

, `mistral-community/Mixtral-8x22B-v0.1`

, etc.`NemotronForCausalLM`

`nvidia/Minitron-8B-Base`

, `mgoin/Nemotron-4-340B-Base-hf-FP8`

, etc.`NemotronHForCausalLM`

`nvidia/Nemotron-H-8B-Base-8K`

, `nvidia/Nemotron-H-47B-Base-8K`

, `nvidia/Nemotron-H-56B-Base-8K`

, etc.`OlmoHybridForCausalLM`

`allenai/Olmo-Hybrid-7B`

`OlmoeForCausalLM`

`allenai/OLMoE-1B-7B-0924`

, `allenai/OLMoE-1B-7B-0924-Instruct`

, etc.`OPTForCausalLM`

`facebook/opt-66b`

, `facebook/opt-iml-max-30b`

, etc.`OrionForCausalLM`

`OrionStarAI/Orion-14B-Base`

, `OrionStarAI/Orion-14B-Chat`

, etc.`PanguEmbeddedForCausalLM`

`FreedomIntelligence/openPangu-Embedded-7B-V1.1`

`PanguProMoEV2ForCausalLM`

`PanguUltraMoEForCausalLM`

`FreedomIntelligence/openPangu-Ultra-MoE-718B-V1.1`

`Param2MoEForCausalLM`

`bharatgenai/Param2-17B-A2.4B-Thinking`

, etc.`PhiForCausalLM`

`microsoft/phi-1_5`

, `microsoft/phi-2`

, etc.`Phi3ForCausalLM`

`microsoft/Phi-4-mini-instruct`

, `microsoft/Phi-4`

, `microsoft/Phi-3-mini-4k-instruct`

, `microsoft/Phi-3-mini-128k-instruct`

, `microsoft/Phi-3-medium-128k-instruct`

, etc.`PhiMoEForCausalLM`

`microsoft/Phi-3.5-MoE-instruct`

, etc.`Plamo3ForCausalLM`

`pfnet/plamo-3-nict-2b-base`

, `pfnet/plamo-3-nict-8b-base`

, etc.`Qwen2ForCausalLM`

`Qwen/QwQ-32B-Preview`

, `Qwen/Qwen2-7B-Instruct`

, `Qwen/Qwen2-7B`

, etc.`Qwen2MoeForCausalLM`

`Qwen/Qwen1.5-MoE-A2.7B`

, `Qwen/Qwen1.5-MoE-A2.7B-Chat`

, etc.`Qwen3ForCausalLM`

`Qwen/Qwen3-8B`

, etc.`Qwen3MoeForCausalLM`

`Qwen/Qwen3-30B-A3B`

, etc.`Qwen3NextForCausalLM`

`Qwen/Qwen3-Next-80B-A3B-Instruct`

, etc.`Rnj1ForCausalLM`

`EssentialAI/rnj-1-instruct`

, etc.`SarvamMoEForCausalLM`

`sarvamai/sarvam2-30b-a3b`

, etc.`SarvamMLAForCausalLM`

`sarvamai/sarvam2-105b-a9b`

, etc.`SeedOssForCausalLM`

`ByteDance-Seed/Seed-OSS-36B-Instruct`

, etc.`SolarForCausalLM`

`upstage/solar-pro-preview-instruct`

, etc.`StableLmForCausalLM`

`stabilityai/stablelm-3b-4e1t`

, `stabilityai/stablelm-base-alpha-7b-v2`

, etc.`Step1ForCausalLM`

`stepfun-ai/Step-Audio-EditX`

, etc.`Step3p5ForCausalLM`

`stepfun-ai/Step-3.5-Flash`

, etc.`TeleChat2ForCausalLM`

`Tele-AI/TeleChat2-3B`

, `Tele-AI/TeleChat2-7B`

, `Tele-AI/TeleChat2-35B`

, etc.`TeleChat3ForCausalLM`

`Tele-AI/TeleChat3-36B-Thinking`

, `Tele-AI/TeleChat3-Coder-36B-Thinking`

, etc.`TeleFLMForCausalLM`

`CofeAI/FLM-2-52B-Instruct-2407`

, `CofeAI/Tele-FLM`

, etc.`Zamba2ForCausalLM`

`Zyphra/Zamba2-7B-instruct`

, `Zyphra/Zamba2-2.7B-instruct`

, `Zyphra/Zamba2-1.2B-instruct`

, etc.Some models are supported only via the [Transformers modeling backend](https://docs.vllm.ai#transformers). The purpose of the table below is to acknowledge models which we officially support in this way. The logs will say that the Transformers modeling backend is being used, and you will see no warning that this is fallback behaviour. This means that, if you have issues with any of the models listed below, please [make an issue](https://github.com/vllm-project/vllm/issues/new/choose) and we'll do our best to fix it!

| Architecture | Models | Example HF Models |
|
|---|

[PP](https://docs.vllm.ai/serving/parallelism_scaling/)

`FlexOlmoForCausalLM`

`allenai/FlexOlmo-7x7B-1T`

, `allenai/FlexOlmo-7x7B-1T-RT`

, etc.`GPTBigCodeForCausalLM`

`bigcode/starcoder`

, `bigcode/gpt_bigcode-santacoder`

, `WizardLM/WizardCoder-15B-V1.0`

, etc.`HunYuanDenseV1ForCausalLM`

`tencent/Hunyuan-7B-Instruct`

`HunYuanMoEV1ForCausalLM`

`tencent/Hunyuan-A13B-Instruct`

, `tencent/Hunyuan-A13B-Pretrain`

, `tencent/Hunyuan-A13B-Instruct-FP8`

, etc.`NanbeigeForCausalLM`

`Nanbeige/Nanbeige4.2-3B`

, etc.`OlmoForCausalLM`

`allenai/OLMo-1B-hf`

, `allenai/OLMo-7B-hf`

, etc.`Olmo2ForCausalLM`

`allenai/OLMo-2-0425-1B`

, etc.`Olmo3ForCausalLM`

`allenai/Olmo-3-7B-Instruct`

, `allenai/Olmo-3-32B-Think`

, etc.`SmolLM3ForCausalLM`

`HuggingFaceTB/SmolLM3-3B`

`Starcoder2ForCausalLM`

`bigcode/starcoder2-3b`

, `bigcode/starcoder2-7b`

, `bigcode/starcoder2-15b`

, etc.`VaultGemmaForCausalLM`

`google/vaultgemma-1b`

Note

Currently, the ROCm version of vLLM supports Mistral and Mixtral only for context lengths up to 4096.

## List of Multimodal Language Models[¶](https://docs.vllm.ai#list-of-multimodal-language-models)

The following modalities are supported depending on the model:

**T**ext**I**mage**V**ideo**A**udio

Any combination of modalities joined by `+`

are supported.

- e.g.:
`T + I`

means that the model supports text-only, image-only, and text-with-image inputs.

On the other hand, modalities separated by `/`

are mutually exclusive.

- e.g.:
`T / I`

means that the model supports text-only and image-only inputs, but not text-with-image inputs.

See [this page](https://docs.vllm.ai/features/multimodal_inputs/) on how to pass multi-modal inputs to the model.

Tip

For hybrid-only models such as Llama-4, Step3, Mistral-3 and Qwen-3.5, a text-only mode can be enabled by setting all supported multimodal modalities to 0 (`--language-model-only`

) so that their multimodal modules will not be loaded to free up more GPU memory for KV cache.

Note

vLLM currently supports adding LoRA adapters to the language backbone for most multimodal models. Additionally, vLLM now experimentally supports adding LoRA to the tower and connector modules for some multimodal models. See [this page](https://docs.vllm.ai/features/lora/).

### Generative Models[¶](https://docs.vllm.ai#generative-models_1)

See [this page](https://docs.vllm.ai/generative_models/) for more information on how to use generative models.

#### Text Generation[¶](https://docs.vllm.ai#text-generation_1)

These models primarily accept the [ LLM.generate](https://docs.vllm.ai/generative_models/#llmgenerate) API. Chat/Instruct models additionally support the

[API.](https://docs.vllm.ai/generative_models/#llmchat)

`LLM.chat`

| Architecture | Models | Inputs | Example HF Models |
|
|---|

[PP](https://docs.vllm.ai/serving/parallelism_scaling/)

`AriaForConditionalGeneration`

+`rhymes-ai/Aria`

`AudioFlamingo3ForConditionalGeneration`

`nvidia/audio-flamingo-3-hf`

, `nvidia/music-flamingo-hf`

`BagelForConditionalGeneration`

+`ByteDance-Seed/BAGEL-7B-MoT`

`BailingMoeV3VLForConditionalGeneration`

E+`inclusionAI/Ling-3.0-flash-VL`

`BeeForConditionalGeneration`

E+`Open-Bee/Bee-8B-RL`

, `Open-Bee/Bee-8B-SFT`

`Blip2ForConditionalGeneration`

E`Salesforce/blip2-opt-2.7b`

, `Salesforce/blip2-opt-6.7b`

, etc.`Cohere2VisionForConditionalGeneration`

+`CohereLabs/command-a-vision-07-2025`

, `CohereLabs/command-a-plus-05-2026`

, etc.`Cosmos3ForConditionalGeneration`

E++ VE+`nvidia/Cosmos3-Nano`

, `nvidia/Cosmos3-Super`

`Cosmos3EdgeForConditionalGeneration`

E++ VE+`nvidia/Cosmos3-Edge`

`DeepseekVLV2ForCausalLM`

+`deepseek-ai/deepseek-vl2-tiny`

, `deepseek-ai/deepseek-vl2-small`

, `deepseek-ai/deepseek-vl2`

, etc.`DeepseekOCRForCausalLM`

+`deepseek-ai/DeepSeek-OCR`

, etc.`DeepseekOCR2ForCausalLM`

+`deepseek-ai/DeepSeek-OCR-2`

, etc.`DeepseekV4ForConditionalGeneration`

+`deepseek-ai/DeepSeek-V4-Flash-Vision-Exp`

`DiffusionGemmaForBlockDiffusion`

++ V+`google/diffusiongemma-26B-A4B-it`

, etc.`Eagle2_5_VLForConditionalGeneration`

E+`nvidia/Eagle2.5-8B`

, etc.`Ernie4_5_VLMoeForConditionalGeneration`

+/ V+`baidu/ERNIE-4.5-VL-28B-A3B-PT`

, `baidu/ERNIE-4.5-VL-424B-A47B-PT`

`Exaone4_5_ForConditionalGeneration`

E+`LGAI-EXAONE/EXAONE-4.5-33B`

, etc.`Gemma3ForConditionalGeneration`

E+`google/gemma-3-4b-it`

, `google/gemma-3-27b-it`

, etc.`Gemma3nForConditionalGeneration`

`google/gemma-3n-E2B-it`

, `google/gemma-3n-E4B-it`

, etc.`Gemma4ForConditionalGeneration`

++ V + A*`google/gemma-4-E2B-it`

, etc.`Gemma4UnifiedForConditionalGeneration`

++ V + A`google/gemma-4-12B-it`

, etc.`GLM4VForCausalLM`

^`zai-org/glm-4v-9b`

, `zai-org/cogagent-9b-20241220`

, etc.`Glm4vForConditionalGeneration`

E++ VE+`zai-org/GLM-4.1V-9B-Thinking`

, etc.`Glm4vMoeForConditionalGeneration`

E++ VE+`zai-org/GLM-4.5V`

, etc.`GlmOcrForConditionalGeneration`

E+`zai-org/GLM-OCR`

, etc.`Granite4VisionForConditionalGeneration`

E+`ibm-granite/granite-4.1-3b-vision`

, etc.`GraniteSpeechForConditionalGeneration`

`ibm-granite/granite-speech-3.3-8b`

`GraniteSpeechPlusForConditionalGeneration`

`ibm-granite/granite-speech-4.1-2b-plus`

`HCXVisionV2ForCausalLM`

++ V+`naver-hyperclovax/HyperCLOVAX-SEED-Think-32B`

`H2OVLChatModel`

E+`h2oai/h2ovl-mississippi-800m`

, `h2oai/h2ovl-mississippi-2b`

, etc.`Idefics3ForConditionalGeneration`

`HuggingFaceM4/Idefics3-8B-Llama3`

, etc.`IsaacForConditionalGeneration`

+`PerceptronAI/Isaac-0.1`

`InternS1ForConditionalGeneration`

E++ VE+`internlm/Intern-S1`

, `internlm/Intern-S1-mini`

, etc.`InternS1ProForConditionalGeneration`

E++ VE+`internlm/Intern-S1-Pro`

, etc.`InternS2MobiusForConditionalGeneration`

E++ VE+`internlm/Intern-S2-Mobius`

`InternS2PreviewForConditionalGeneration`

E++ VE+`internlm/Intern-S2-Preview`

, etc.`InternVLChatModel`

E++ (VE+)`OpenGVLab/InternVL3_5-14B`

, `OpenGVLab/InternVL3-9B`

, `OpenGVLab/InternVideo2_5_Chat_8B`

, `OpenGVLab/InternVL2_5-4B`

, `OpenGVLab/InternVL2-4B`

, etc.`InternVLForConditionalGeneration`

E++ VE+`OpenGVLab/InternVL3-1B-hf`

, etc.`KananaVForConditionalGeneration`

+`kakaocorp/kanana-1.5-v-3b-instruct`

, etc.`KeyeForConditionalGeneration`

E++ VE+`Kwai-Keye/Keye-VL-8B-Preview`

`KeyeVL1_5ForConditionalGeneration`

E++ VE+`Kwai-Keye/Keye-VL-1_5-8B`

`KimiAudioForConditionalGeneration`

+`moonshotai/Kimi-Audio-7B-Instruct`

`KimiK25ForConditionalGeneration`

+`moonshotai/Kimi-K2.5`

`KimiK3ForConditionalGeneration`

+`moonshotai/Kimi-K3`

`KimiVLForConditionalGeneration`

+`moonshotai/Kimi-VL-A3B-Instruct`

, `moonshotai/Kimi-VL-A3B-Thinking`

`LightOnOCRForConditionalGeneration`

+`lightonai/LightOnOCR-1B`

, etc`Lfm2VlForConditionalGeneration`

+`LiquidAI/LFM2-VL-450M`

, `LiquidAI/LFM2-VL-3B`

, `LiquidAI/LFM2-VL-8B-A1B`

, etc.`Llama4ForConditionalGeneration`

+`meta-llama/Llama-4-Scout-17B-16E-Instruct`

, `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8`

, `meta-llama/Llama-4-Maverick-17B-128E-Instruct`

, etc.`Llama_Nemotron_Nano_VL`

E+`nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1`

`LlavaForConditionalGeneration`

E+`llava-hf/llava-1.5-7b-hf`

, `mistral-community/pixtral-12b`

, etc.`LlavaNextForConditionalGeneration`

E+`llava-hf/llava-v1.6-mistral-7b-hf`

, `llava-hf/llava-v1.6-vicuna-7b-hf`

, `ibm-granite/granite-vision-3.3-2b`

, etc.`LlavaNextVideoForConditionalGeneration`

`llava-hf/LLaVA-NeXT-Video-7B-hf`

, etc.`LlavaOnevision2ForConditionalGeneration`

++ V+`lmms-lab-encoder/LLaVA-OneVision-2-8B-Instruct`

`LlavaOnevisionForConditionalGeneration`

++ V+`llava-hf/llava-onevision-qwen2-7b-ov-hf`

, `llava-hf/llava-onevision-qwen2-0.5b-ov-hf`

, etc.`MiDashengLMModel`

+`mispeech/midashenglm-7b`

`MiMoV2OmniForCausalLM`

E++ VE++ A+`XiaomiMiMo/MiMo-V2.5-Omni`

`MiniCPMO`

E++ VE++ AE+`openbmb/MiniCPM-o-2_6`

, etc.`MiniCPMV`

E++ VE+`openbmb/MiniCPM-V-2`

(see note), `openbmb/MiniCPM-Llama3-V-2_5`

, `openbmb/MiniCPM-V-2_6`

, `openbmb/MiniCPM-V-4`

, `openbmb/MiniCPM-V-4_5`

, `openbmb/MiniCPM-V-4_6`

, etc.`MiniMaxM3SparseForConditionalGeneration`

++ V+`MiniMaxAI/MiniMax-M3`

, `MiniMaxAI/MiniMax-M3-MXFP8`

, etc.`MiniMaxVL01ForConditionalGeneration`

E+`MiniMaxAI/MiniMax-VL-01`

, etc.`Mistral3ForConditionalGeneration`

+`mistralai/Mistral-Small-3.1-24B-Instruct-2503`

, etc.`MolmoForCausalLM`

+`allenai/Molmo-7B-D-0924`

, `allenai/Molmo-7B-O-0924`

, etc.`Molmo2ForConditionalGeneration`

+/ V`allenai/Molmo2-4B`

, `allenai/Molmo2-8B`

, `allenai/Molmo2-O-7B`

, `allenai/MolmoWeb-4B`

^,`allenai/MolmoWeb-8B`

^`MossAudioModel`

+`OpenMOSS-Team/MOSS-Audio-4B-Instruct`

, `OpenMOSS-Team/MOSS-Audio-4B-Thinking`

, `OpenMOSS-Team/MOSS-Audio-8B-Instruct`

, `OpenMOSS-Team/MOSS-Audio-8B-Thinking`

`MossTranscribeDiarizeForConditionalGeneration`

`OpenMOSS-Team/MOSS-Transcribe-Diarize`

`Moondream3ForCausalLM`

`moondream/moondream3-preview`

`MuseGlimmerForCausalLM`

, `MuseGlimmerForConditionalGeneration`

++ V+`meta-models/Muse-Glimmer-30B`

`NemotronH_Nano_Omni_Reasoning_V3`

, `NemotronH_Nano_VL_V2`

E++ V++ A*`nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16`

`NVLM_D_Model`

+`nvidia/NVLM-D-72B`

, etc.`OpenCUAForConditionalGeneration`

E+`xlangai/OpenCUA-7B`

`OpenPanguVLForConditionalGeneration`

E++ VE+`FreedomIntelligence/openPangu-VL-7B`

`OpenVLAForActionPrediction`

`openvla/openvla-7b`

`Ovis`

+`AIDC-AI/Ovis2-1B`

, `AIDC-AI/Ovis1.6-Llama3.2-3B`

, etc.`Ovis2_5`

++ V`AIDC-AI/Ovis2.5-9B`

, etc.`Ovis2_6ForCausalLM`

++ V`AIDC-AI/Ovis2.6-2B`

, etc.`Ovis2_6_MoeForCausalLM`

++ V`AIDC-AI/Ovis2.6-30B-A3B`

, etc.`PaddleOCRVLForConditionalGeneration`

+`PaddlePaddle/PaddleOCR-VL`

, etc.`PaliGemmaForConditionalGeneration`

E`google/paligemma-3b-pt-224`

, `google/paligemma-3b-mix-224`

, `google/paligemma2-3b-ft-docci-448`

, etc.`Phi3VForCausalLM`

E+`microsoft/Phi-3-vision-128k-instruct`

, `microsoft/Phi-3.5-vision-instruct`

, etc.`Phi4MMForCausalLM`

+/ T + A+/ I++ A+`microsoft/Phi-4-multimodal-instruct`

, etc.`Phi4ForCausalLMV`

+`microsoft/Phi-4-reasoning-vision-15B`

, etc.`PixtralForConditionalGeneration`

+`mistralai/Ministral-3-3B-Instruct-2512`

, `mistralai/Mistral-Small-3.1-24B-Instruct-2503`

, `mistralai/Mistral-Large-3-675B-Instruct-2512`

`mistralai/Pixtral-12B-2409`

etc.`QianfanOCRForConditionalGeneration`

E+`baidu/Qianfan-OCR`

, etc.`Qwen2AudioForConditionalGeneration`

+`Qwen/Qwen2-Audio-7B-Instruct`

`Qwen2VLForConditionalGeneration`

QE++ VE+`Qwen/QVQ-72B-Preview`

, `Qwen/Qwen2-VL-7B-Instruct`

, `Qwen/Qwen2-VL-72B-Instruct`

, etc.`Qwen2_5_VLForConditionalGeneration`

QE++ VE+`Qwen/Qwen2.5-VL-3B-Instruct`

, `Qwen/Qwen2.5-VL-72B-Instruct`

, etc.`Qwen2_5OmniThinkerForConditionalGeneration`

E++ VE++ A+`Qwen/Qwen2.5-Omni-3B`

, `Qwen/Qwen2.5-Omni-7B`

`Qwen3_5ForConditionalGeneration`

E++ VE+`Qwen/Qwen3.5-9B-Instruct`

, etc.`Qwen3_5MoeForConditionalGeneration`

E++ VE+`Qwen/Qwen3.5-35B-A3B-Instruct`

, etc.`Qwen3VLForConditionalGeneration`

QE++ VE+`Qwen/Qwen3-VL-4B-Instruct`

, etc.`Qwen3VLMoeForConditionalGeneration`

QE++ VE+`Qwen/Qwen3-VL-30B-A3B-Instruct`

, etc.`Qwen3OmniMoeThinkerForConditionalGeneration`

E++ VE++ A+`Qwen/Qwen3-Omni-30B-A3B-Instruct`

, `Qwen/Qwen3-Omni-30B-A3B-Thinking`

`Qwen3ASRForConditionalGeneration`

+`Qwen/Qwen3-ASR-1.7B`

`RForConditionalGeneration`

E+`YannQi/R-4B`

`SkyworkR1VChatModel`

`Skywork/Skywork-R1V-38B`

`SmolVLMForConditionalGeneration`

`SmolVLM2-2.2B-Instruct`

`Step3VLForConditionalGeneration`

+`stepfun-ai/step3`

`StepVLForConditionalGeneration`

+`stepfun-ai/Step3-VL-10B`

`Step3p7ForConditionalGeneration`

+`stepfun-ai/Step-3.7-Flash`

`UltravoxModel`

E+`fixie-ai/ultravox-v0_5-llama-3_2-1b`

`UnlimitedOCRForCausalLM`

+`baidu/Unlimited-OCR`

, etc.Some models are supported only via the [Transformers modeling backend](https://docs.vllm.ai#transformers). The purpose of the table below is to acknowledge models which we officially support in this way. The logs will say that the Transformers modeling backend is being used, and you will see no warning that this is fallback behaviour. This means that, if you have issues with any of the models listed below, please [make an issue](https://github.com/vllm-project/vllm/issues/new/choose) and we'll do our best to fix it!

| Architecture | Models | Inputs | Example HF Models |
|
|---|

[PP](https://docs.vllm.ai/serving/parallelism_scaling/)

`Emu3ForConditionalGeneration`

+`BAAI/Emu3-Chat-hf`

`HunYuanVLForConditionalGeneration`

E+`tencent/HunyuanOCR`

, etc.`VibeVoiceAsrForConditionalGeneration`

+`microsoft/VibeVoice-ASR-HF`

^ You need to set the architecture name via `--hf-overrides`

to match the one in vLLM.

E Pre-computed embeddings can be inputted for this modality.

+ Multiple items can be inputted per text prompt for this modality. * Only specific variants of the model support this modality (see notes below).

Q `Qwen*-VL`

officially uses `qwen_vl_utils`

for image preprocessing, while vLLM uses `transformers`

' `video_processing_qwen*`

, which leads to slightly different results compared to the official Hugging Face repository examples.

Note

For [ Dots3NoteForCausalLM](https://docs.vllm.ai/api/vllm/models/dots3_note/nvidia/multimodal/#vllm.models.dots3_note.nvidia.multimodal.Dots3NoteForCausalLM), the vision and audio towers are only loaded when the corresponding modality is enabled via

`--limit-mm-per-prompt`

. Video inputs are decoded into frames and audio, so they require both towers. The checkpoint also ships one MTP layer, enabled with `--speculative-config '{"method":"mtp","num_speculative_tokens":1}'`

.Note

`Gemma3nForConditionalGeneration`

is only supported on V1 due to shared KV caching and it depends on `timm>=1.0.17`

to make use of its MobileNet-v5 vision backbone.

Performance is not yet fully optimized mainly due to:

- Both audio and vision MM encoders use
`transformers.AutoModel`

implementation. - There's no PLE caching or out-of-memory swapping support, as described in
[Google's blog](https://developers.googleblog.com/en/introducing-gemma-3n/). These features might be too model-specific for vLLM, and swapping in particular may be better suited for constrained setups.

Note

For `Gemma4ForConditionalGeneration`

: - audio input is only supported by the `gemma-4-E2B`

and `gemma-4-E4B`

variants. - The model does not ingest videos directly. However, vLLM’s Gemma 4 implementation supports video inputs by handling video processing internally. Users can send videos directly in the message structure to vLLM, where they are converted into text and image frames before being passed to the model. - Gemma 4 assistant checkpoints for speculative decoding use vLLM’s Gemma 4 MTP path, not generic draft-model speculative decoding. See the [Gemma 4 assistant model MTP example](https://docs.vllm.ai/features/speculative_decoding/mtp/#gemma-4-assistant-models).

Note

For [ Gemma4UnifiedForConditionalGeneration](https://docs.vllm.ai/api/vllm/model_executor/models/gemma4_unified/#vllm.model_executor.models.gemma4_unified.Gemma4UnifiedForConditionalGeneration): - This is the encoder-free Gemma 4 variant (e.g.

`gemma-4-12B-it`

). Unlike the tower-based `Gemma4ForConditionalGeneration`

, it has **no SigLIP vision encoder**and

**no audio encoder**. Raw pixel patches are projected directly into LM space via a Dense+LayerNorm pipeline with factorized positional embeddings, and raw audio waveform frames are projected directly through a multimodal embedder. - All modalities (image, video, audio) are supported. - Gemma 4 Unified assistant checkpoints (

`model_type: gemma4_unified_assistant`

) use the same MTP path as the tower-based variant. See the [Gemma 4 assistant model MTP example](https://docs.vllm.ai/features/speculative_decoding/mtp/#gemma-4-assistant-models).

Note

For `InternVLChatModel`

, only InternVL2.5 with Qwen2.5 text backbone (`OpenGVLab/InternVL2.5-1B`

etc.), InternVL3 and InternVL3.5 have video inputs support currently.

Note

To use `allenai/MolmoWeb-4B`

or `allenai/MolmoWeb-8B`

, serve the checkpoint with the Molmo2 architecture and disable multimodal-prefix attention: `--hf-overrides '{"architectures": ["Molmo2ForConditionalGeneration"], "is_mm_prefix_lm": false}'`

.

Note

[ Moondream3ForCausalLM](https://docs.vllm.ai/api/vllm/model_executor/models/moondream3/#vllm.model_executor.models.moondream3.Moondream3ForCausalLM) uses task-specific prompt templates for

`query`

and `caption`

. The native `detect`

and `point`

skills require custom coordinate decoding and are not exposed by this vLLM implementation. See [Moondream3 prompt recipes](https://docs.vllm.ai/features/multimodal_inputs/#moondream3-prompt-recipes).

Note

Both Muse Glimmer architecture names map to the same vLLM implementation: checkpoints with a vision config accept image and video inputs, while vision-less checkpoints run as a text-only model. Speculative decoding uses the `meta-models/Muse-Glimmer-30B-assistant`

checkpoint, which vLLM serves through its [DFlash](https://docs.vllm.ai/features/speculative_decoding/) path.

Note

Both Nemotron Nano architecture names map to the same vLLM implementation. Audio inputs are only supported by the Omni variants; `NemotronH_Nano_VL_V2`

checkpoints such as `nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-BF16`

accept text, image and video only.

Note

The official `openbmb/MiniCPM-V-2`

doesn't work yet, so we need to use a fork (`HwwwH/MiniCPM-V-2`

) for now. For more details, please see: [ Pull Request #4087](https://github.com/vllm-project/vllm/pull/4087#issuecomment-2250397630)

#### Transcription[¶](https://docs.vllm.ai#transcription)

Speech2Text models trained specifically for Automatic Speech Recognition.

| Architecture | Models | Example HF Models |
|
|---|

[PP](https://docs.vllm.ai/serving/parallelism_scaling/)

`CohereAsrForConditionalGeneration`

`CohereLabs/cohere-transcribe-03-2026`

`FireRedASR2ForConditionalGeneration`

`allendou/FireRedASR2-LLM-vllm`

, etc.`FunASRForConditionalGeneration`

`FunAudioLLM/Fun-ASR-Nano-2512-vllm`

, etc.`Gemma3nForConditionalGeneration`

`google/gemma-3n-E2B-it`

, `google/gemma-3n-E4B-it`

, etc.`GlmAsrForConditionalGeneration`

`zai-org/GLM-ASR-Nano-2512`

`GraniteSpeechForConditionalGeneration`

`ibm-granite/granite-4.0-1b-speech`

, `ibm-granite/granite-speech-3.3-2b`

, etc.`GraniteSpeechPlusForConditionalGeneration`

`ibm-granite/granite-speech-4.1-2b-plus`

`MossTranscribeDiarizeForConditionalGeneration`

`OpenMOSS-Team/MOSS-Transcribe-Diarize`

`Qwen3ASRForConditionalGeneration`

`Qwen/Qwen3-ASR-1.7B`

, etc.`Qwen3OmniMoeThinkerForConditionalGeneration`

`Qwen/Qwen3-Omni-30B-A3B-Instruct`

, etc.`VoxtralForConditionalGeneration`

`mistralai/Voxtral-Mini-3B-2507`

, `mistralai/Voxtral-Small-24B-2507`

, etc.`WhisperForConditionalGeneration`

`openai/whisper-small`

, `openai/whisper-large-v3-turbo`

, etc.Note

`VoxtralForConditionalGeneration`

requires `mistral-common[audio]`

to be installed.

#### Realtime Transcription[¶](https://docs.vllm.ai#realtime-transcription)

Speech models that support streaming transcription via the [ /v1/realtime](https://docs.vllm.ai/serving/online_serving/speech_to_text/#realtime-api) WebSocket endpoint.

| Architecture | Models | Example HF Models |
|
|---|

[PP](https://docs.vllm.ai/serving/parallelism_scaling/)

`VoxtralRealtimeGeneration`

`mistralai/Voxtral-Mini-4B-Realtime-2602`

`Qwen3ASRRealtimeGeneration`

`Qwen/Qwen3-ASR-0.6B`

Note

`VoxtralRealtimeGeneration`

requires `mistral-common[audio]`

to be installed, and must be served with `--tokenizer-mode mistral`

.

`Qwen3ASRRealtimeGeneration`

is not auto-detected from `config.json`

. You must pass `--hf-overrides '{"architectures":["Qwen3ASRRealtimeGeneration"]}'`

when serving.

## Pooling Models[¶](https://docs.vllm.ai#pooling-models)

See [this page](https://docs.vllm.ai/pooling_models/) for more information on how to use pooling models.

Important

Since some model architectures support both generative and pooling tasks, you should explicitly specify `--runner pooling`

to ensure that the model is used in pooling mode instead of generative mode.

See the link below for more information on the models supported for specific pooling tasks.

[Classification Usages](https://docs.vllm.ai/pooling_models/classify/)[Embedding Usages](https://docs.vllm.ai/pooling_models/embed/)[Reward Usages](https://docs.vllm.ai/pooling_models/reward/)[Token Classification Usages](https://docs.vllm.ai/pooling_models/token_classify/)[Token Embedding Usages](https://docs.vllm.ai/pooling_models/token_embed/)[Scoring Usages](https://docs.vllm.ai/pooling_models/scoring/)[Specific Model Examples](https://docs.vllm.ai/pooling_models/specific_models/)

## Model Support Policy[¶](https://docs.vllm.ai#model-support-policy)

At vLLM, we are committed to facilitating the integration and support of third-party models within our ecosystem. Our approach is designed to balance the need for robustness and the practical limitations of supporting a wide range of models. Here’s how we manage third-party model support:

-
**Community-Driven Support**: We encourage community contributions for adding new models. When a user requests support for a new model, we welcome pull requests (PRs) from the community. These contributions are evaluated primarily on the sensibility of the output they generate, rather than strict consistency with existing implementations such as those in transformers.**Call for contribution:**PRs coming directly from model vendors are greatly appreciated! -
**Best-Effort Consistency**: While we aim to maintain a level of consistency between the models implemented in vLLM and other frameworks like transformers, complete alignment is not always feasible. Factors like acceleration techniques and the use of low-precision computations can introduce discrepancies. Our commitment is to ensure that the implemented models are functional and produce sensible results.Tip

When comparing the output of

`model.generate`

from Hugging Face Transformers with the output of`llm.generate`

from vLLM, note that the former reads the model's generation config file (i.e.,[generation_config.json](https://github.com/huggingface/transformers/blob/19dabe96362803fb0a9ae7073d03533966598b17/src/transformers/generation/utils.py#L1945)) and applies the default parameters for generation, while the latter only uses the parameters passed to the function. Ensure all sampling parameters are identical when comparing outputs. -
**Issue Resolution and Model Updates**: Users are encouraged to report any bugs or issues they encounter with third-party models. Proposed fixes should be submitted via PRs, with a clear explanation of the problem and the rationale behind the proposed solution. If a fix for one model impacts another, we rely on the community to highlight and address these cross-model dependencies. Note: for bugfix PRs, it is good etiquette to inform the original author to seek their feedback. -
**Monitoring and Updates**: Users interested in specific models should monitor the commit history for those models (e.g., by tracking changes in the main/vllm/model_executor/models directory). This proactive approach helps users stay informed about updates and changes that may affect the models they use. -
**Selective Focus**: Our resources are primarily directed towards models with significant user interest and impact. Models that are less frequently used may receive less attention, and we rely on the community to play a more active role in their upkeep and improvement.

Through this approach, vLLM fosters a collaborative environment where both the core development team and the broader community contribute to the robustness and diversity of the third-party models supported in our ecosystem.

Note that, as an inference engine, vLLM does not introduce new models. Therefore, all models supported by vLLM are third-party models in this regard.

We have the following levels of testing for models:

**Strict Consistency**: We compare the output of the model with the output of the model in the HuggingFace Transformers library under greedy decoding. This is the most stringent test. Please refer to[models tests](https://github.com/vllm-project/vllm/blob/main/tests/models)for the models that have passed this test.**Output Sensibility**: We check if the output of the model is sensible and coherent, by measuring the perplexity of the output and checking for any obvious errors. This is a less stringent test.**Runtime Functionality**: We check if the model can be loaded and run without errors. This is the least stringent test. Please refer to[functionality tests](https://github.com/vllm-project/vllm/tree/main/tests)and[examples](https://github.com/vllm-project/vllm/tree/main/examples)for the models that have passed this test.**Community Feedback**: We rely on the community to provide feedback on the models. If a model is broken or not working as expected, we encourage users to raise issues to report it or open pull requests to fix it. The rest of the models fall under this category.