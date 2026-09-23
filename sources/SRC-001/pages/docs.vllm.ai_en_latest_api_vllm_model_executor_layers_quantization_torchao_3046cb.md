source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/torchao/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.quantization.torchao`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.torchao)

Classes:

-
–[TorchAOConfig](https://docs.vllm.ai#vllm.model_executor.layers.quantization.torchao.TorchAOConfig)Config class for torchao.

-
–[TorchAOLinearMethod](https://docs.vllm.ai#vllm.model_executor.layers.quantization.torchao.TorchAOLinearMethod)Linear method for torchao.


Functions:

-
–[should_skip](https://docs.vllm.ai#vllm.model_executor.layers.quantization.torchao.should_skip)Robust skipping logic:

-
–[torchao_quantize_param_data](https://docs.vllm.ai#vllm.model_executor.layers.quantization.torchao.torchao_quantize_param_data)Quantize a Tensor with torchao quantization specified by torchao_config.


##

`TorchAOConfig`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.torchao.TorchAOConfig)

Bases: [QuantizationConfig](https://docs.vllm.ai/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizationConfig)

Config class for torchao.

Methods:

-
–[from_config](https://docs.vllm.ai#vllm.model_executor.layers.quantization.torchao.TorchAOConfig.from_config)Create the quant config from an hf model config.

-
–[from_config_dict_json](https://docs.vllm.ai#vllm.model_executor.layers.quantization.torchao.TorchAOConfig.from_config_dict_json)Initialize class from a config_dict json string, got from

-
–[from_config_file](https://docs.vllm.ai#vllm.model_executor.layers.quantization.torchao.TorchAOConfig.from_config_file)Initialize class from a config file. Example:

-
–[get_config_filenames](https://docs.vllm.ai#vllm.model_executor.layers.quantization.torchao.TorchAOConfig.get_config_filenames)Torchao doesn't require additional config files, we use


## Source code in `vllm/model_executor/layers/quantization/torchao.py`


|
|

###

`from_config(config)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.torchao.TorchAOConfig.from_config)

Create the quant config from an hf model config.

## Source code in `vllm/model_executor/layers/quantization/torchao.py`


###

`from_config_dict_json(config_dict_json)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.torchao.TorchAOConfig.from_config_dict_json)

Initialize class from a config_dict json string, got from torchao_config_object = some AOBaseConfig object json.dumps(config_to_dict(torchao_config_object))

## Source code in `vllm/model_executor/layers/quantization/torchao.py`


###

`from_config_file(config_file)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.torchao.TorchAOConfig.from_config_file)

Initialize class from a config file. Example:

config = Float8DynamicActivationFloat8WeightConfig(granularity=PerRow())
fn = "torchao_config.json"
with open(fn, "w") as f:
f.write(json.dumps(config_to_dict(config)))


## Source code in `vllm/model_executor/layers/quantization/torchao.py`


###

`get_config_filenames()`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.torchao.TorchAOConfig.get_config_filenames)

Torchao doesn't require additional config files, we use `config.json`

from huggingface: `model_config.hf_config`


##

`TorchAOLinearMethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.torchao.TorchAOLinearMethod)

Bases: [LinearMethodBase](https://docs.vllm.ai/linear/#vllm.model_executor.layers.linear.LinearMethodBase)

Linear method for torchao.

Parameters:

-

(`quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.torchao.TorchAOLinearMethod(quant_config))

) –[TorchAOConfig](https://docs.vllm.ai#vllm.model_executor.layers.quantization.torchao.TorchAOConfig)The torchao quantization config, a string that encodes the type of quantization and all relevant arguments.


## Source code in `vllm/model_executor/layers/quantization/torchao.py`


|
|

##

`_check_torchao_fp8_activation_capability(torchao_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.torchao._check_torchao_fp8_activation_capability)

Check if the current GPU supports FP8 activation quantization.

FP8 activation configs (e.g., Float8DynamicActivationFloat8WeightConfig) require GPU compute capability >= 8.9 (Ada Lovelace / Hopper) on NVIDIA, or MI300+ on AMD. This check provides a clear error message before torchao's internal assertion fires with a confusing message.

## Source code in `vllm/model_executor/layers/quantization/torchao.py`


##

`should_skip(prefix, skip_modules)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.torchao.should_skip)

Robust skipping logic: should_skip("model.model.layers.1.q_proj", ["model.model.layers.1.q_proj"]) # True should_skip("model.model.layers.10.o_proj", ["o_proj"]) -> True should_skip("visual.model.layers.1.q_proj", ["visual"]) -> True should_skip("model.model.layers.1.q_proj", ["layers.1"]) -> True should_skip("model.model.layers.11.q_proj", ["layers.1"]) -> False

## Source code in `vllm/model_executor/layers/quantization/torchao.py`


##

`torchao_quantize_param_data(param, torchao_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.torchao.torchao_quantize_param_data)

Quantize a Tensor with torchao quantization specified by torchao_config.

Parameters:

-

(`param`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.torchao.torchao_quantize_param_data(param))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)weight parameter of the linear module

-

(`torchao_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.torchao.torchao_quantize_param_data(torchao_config))

) –[Any](https://docs.python.org/3/library/typing.html#typing.Any)type of quantization and their arguments we want to use to quantize the Tensor