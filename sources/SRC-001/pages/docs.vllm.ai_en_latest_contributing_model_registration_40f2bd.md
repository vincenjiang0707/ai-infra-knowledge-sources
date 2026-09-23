source: https://docs.vllm.ai/en/latest/contributing/model/registration/
lastmod: 2026-09-23

# Registering a Model[¶](https://docs.vllm.ai#registering-a-model)

vLLM relies on a model registry to determine how to run each model. A list of pre-registered architectures can be found [here](https://docs.vllm.ai/models/supported_models/).

If your model is not on this list, you must register it to vLLM. This page provides detailed instructions on how to do so.

## Built-in models[¶](https://docs.vllm.ai#built-in-models)

To add a model directly to the vLLM library, start by forking our [GitHub repository](https://github.com/vllm-project/vllm) and then [build it from source](https://docs.vllm.ai/getting_started/installation/gpu/#build-wheel-from-source). This gives you the ability to modify the codebase and test your model.

After you have implemented your model (see [tutorial](https://docs.vllm.ai/basic/)), put it into the [ vllm/model_executor/models](https://github.com/vllm-project/vllm/tree/main/vllm/model_executor/models) directory. Then, add your model class to `_VLLM_MODELS`

in [ vllm/model_executor/models/registry.py](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/registry.py) so that it is automatically registered upon importing vLLM. Finally, update our [list of supported models](https://docs.vllm.ai/models/supported_models/) to promote your model!

Important

The list of models in each section should be maintained in alphabetical order.

## Out-of-tree models[¶](https://docs.vllm.ai#out-of-tree-models)

You can load an external model [using a plugin](https://docs.vllm.ai/design/plugin_system/) without modifying the vLLM codebase.

To register the model, use the following code:

# The entrypoint of your plugin
def register():
from vllm import ModelRegistry
from your_code import YourModelForCausalLM
ModelRegistry.register_model("YourModelForCausalLM", YourModelForCausalLM)


If your model imports modules that initialize CUDA, consider lazy-importing it to avoid errors like `RuntimeError: Cannot re-initialize CUDA in forked subprocess`

:

# The entrypoint of your plugin
def register():
from vllm import ModelRegistry
ModelRegistry.register_model(
"YourModelForCausalLM",
"your_code:YourModelForCausalLM",
)


Important

If your model is a multimodal model, ensure the model class implements the [SupportsMultiModal](https://docs.vllm.ai/api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal) interface. Read more about that [here](https://docs.vllm.ai/multimodal/).