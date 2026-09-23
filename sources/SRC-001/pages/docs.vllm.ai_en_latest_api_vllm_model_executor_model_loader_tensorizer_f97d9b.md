source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/tensorizer/
lastmod: 2026-09-23

#

`vllm.model_executor.model_loader.tensorizer`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.tensorizer)

Classes:

##

`TensorizerArgs`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.tensorizer.TensorizerArgs)

Methods:

-
–[add_cli_args](https://docs.vllm.ai#vllm.model_executor.model_loader.tensorizer.TensorizerArgs.add_cli_args)Tensorizer CLI arguments.


## Source code in `vllm/model_executor/model_loader/tensorizer.py`


|
|

###

`add_cli_args(parser)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.tensorizer.TensorizerArgs.add_cli_args)

Tensorizer CLI arguments.

## Source code in `vllm/model_executor/model_loader/tensorizer.py`


##

`TensorizerConfig`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.tensorizer.TensorizerConfig)

Bases: [MutableMapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping)

## Source code in `vllm/model_executor/model_loader/tensorizer.py`


|
|

###

`_keys`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.tensorizer.TensorizerConfig._keys)

Configuration class for Tensorizer settings.

These settings configure the behavior of model serialization and deserialization using Tensorizer.

Attributes:

-
–`tensorizer_uri`

Path to serialized model tensors. Can be a local file path or a S3 URI. This is a required field unless lora_dir is provided and the config is meant to be used for the

`tensorize_lora_adapter`

function. Unless a`tensorizer_dir`

or`lora_dir`

is passed to this object's initializer, this is a required argument. -
–`tensorizer_dir`

Path to a directory containing serialized model tensors, and all other potential model artifacts to load the model, such as configs and tokenizer files. Can be passed instead of

`tensorizer_uri`

where the`model.tensors`

file will be assumed to be in this directory. -
–`vllm_tensorized`

If True, indicates that the serialized model is a vLLM model. This is used to determine the behavior of the TensorDeserializer when loading tensors from a serialized model. It is far faster to deserialize a vLLM model as it utilizes tensorizer's optimized GPU loading. Note that this is now deprecated, as serialized vLLM models are now automatically inferred as vLLM models.

-
–`verify_hash`

If True, the hashes of each tensor will be verified against the hashes stored in the metadata. A

`HashMismatchError`

will be raised if any of the hashes do not match. -
–`num_readers`

Controls how many threads are allowed to read concurrently from the source file. Default is

`None`

, which will dynamically set the number of readers based on the number of available resources and model size. This greatly increases performance. -
–`encryption_keyfile`

File path to a binary file containing a


binary key to use for decryption.`None`

(the default) means no decryption. See the example script in examples/features/tensorize_vllm_model.py. -
–`s3_access_key_id`

The access key for the S3 bucket. Can also be set via the S3_ACCESS_KEY_ID environment variable.

-
–`s3_secret_access_key`

The secret access key for the S3 bucket. Can also be set via the S3_SECRET_ACCESS_KEY environment variable.

-
–`s3_endpoint`

The endpoint for the S3 bucket. Can also be set via the S3_ENDPOINT_URL environment variable.

-
–`lora_dir`

Path to a directory containing LoRA adapter artifacts for serialization or deserialization. When serializing LoRA adapters this is the only necessary parameter to pass to this object's initializer.


##

`_resize_lora_embeddings(model)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.tensorizer._resize_lora_embeddings)

Modify LoRA embedding layers to use bigger tensors to allow for adapter added tokens.

## Source code in `vllm/model_executor/model_loader/tensorizer.py`


##

`is_vllm_tensorized(tensorizer_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.tensorizer.is_vllm_tensorized)

Infer if the model is a vLLM model by checking the weights for a vLLM tensorized marker.

Parameters:

-

(`tensorizer_config`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.tensorizer.is_vllm_tensorized(tensorizer_config))

) –[TensorizerConfig](https://docs.vllm.ai#vllm.model_executor.model_loader.tensorizer.TensorizerConfig)The TensorizerConfig object containing the tensorizer_uri to the serialized model.


Returns:

-
(`bool`


) –[bool](https://docs.python.org/3/builtins/functions.html#bool)True if the model is a vLLM model, False otherwise.


## Source code in `vllm/model_executor/model_loader/tensorizer.py`


##

`tensorize_lora_adapter(lora_path, tensorizer_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.tensorizer.tensorize_lora_adapter)

Uses tensorizer to serialize a LoRA adapter. Assumes that the files needed to load a LoRA adapter are a safetensors-format file called adapter_model.safetensors and a json config file called adapter_config.json.

Serializes the files in the tensorizer_config.tensorizer_dir

## Source code in `vllm/model_executor/model_loader/tensorizer.py`


##

`tensorize_vllm_model(engine_args, tensorizer_config, generate_keyfile=True)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.tensorizer.tensorize_vllm_model)

Utility to load a model and then serialize it with Tensorizer.

Intended to be used separately from running a vLLM server since it creates its own Engine instance.