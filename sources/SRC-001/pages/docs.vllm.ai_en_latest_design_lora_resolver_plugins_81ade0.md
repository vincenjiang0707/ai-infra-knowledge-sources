source: https://docs.vllm.ai/en/latest/design/lora_resolver_plugins/
lastmod: 2026-09-24

# LoRA Resolver Plugins[¶](https://docs.vllm.ai#lora-resolver-plugins)

This directory contains vLLM's LoRA resolver plugins built on the [ LoRAResolver](https://docs.vllm.ai/api/vllm/lora/resolver/#vllm.lora.resolver.LoRAResolver) framework. They automatically discover and load LoRA adapters from a specified local storage path, eliminating the need for manual configuration or server restarts.

## Overview[¶](https://docs.vllm.ai#overview)

LoRA Resolver Plugins provide a flexible way to dynamically load LoRA adapters at runtime. When vLLM receives a request for a LoRA adapter that hasn't been loaded yet, the resolver plugins will attempt to locate and load the adapter from their configured storage locations. This enables:

**Dynamic LoRA Loading**: Load adapters on-demand without server restarts**Multiple Storage Backends**: Support for filesystem, S3, and custom backends. The built-in`lora_filesystem_resolver`

requires a local storage path, while the built-in`hf_hub_resolver`

will pull LoRA adapters from Huggingface Hub and proceed in an identical manner. In general, custom resolvers can be implemented to fetch from any source.**Automatic Discovery**: Seamless integration with existing LoRA workflows**Scalable Deployment**: Centralized adapter management across multiple vLLM instances

## Prerequisites[¶](https://docs.vllm.ai#prerequisites)

Before using LoRA Resolver Plugins, ensure the following environment variables are configured:

### Required Environment Variables[¶](https://docs.vllm.ai#required-environment-variables)

-
: Must be set to`VLLM_ALLOW_RUNTIME_LORA_UPDATING`

`true`

or`1`

to enable dynamic LoRA loading -
: Must include the desired resolver plugins (comma-separated list)`VLLM_PLUGINS`

-
: Must be set to a valid directory path for filesystem resolver`VLLM_LORA_RESOLVER_CACHE_DIR`


### Optional Environment Variables[¶](https://docs.vllm.ai#optional-environment-variables)

: If not set, all available plugins will be loaded. If set to empty string, no plugins will be loaded.`VLLM_PLUGINS`


## Available Resolvers[¶](https://docs.vllm.ai#available-resolvers)

### lora_filesystem_resolver[¶](https://docs.vllm.ai#lora_filesystem_resolver)

The filesystem resolver is installed with vLLM by default and enables loading LoRA adapters from a local directory structure.

#### Setup Steps[¶](https://docs.vllm.ai#setup-steps)

-
**Create the LoRA adapter storage directory**: -
**Set environment variables**: -
**Start vLLM server**: Your base model can be`meta-llama/Llama-2-7b-hf`

. Please make sure you set up the Hugging Face token in your env var`export HF_TOKEN=xxx235`

.

#### Directory Structure Requirements[¶](https://docs.vllm.ai#directory-structure-requirements)

The filesystem resolver expects LoRA adapters to be organized in the following structure:

/path/to/lora/adapters/
├── adapter1/
│ ├── adapter_config.json
│ ├── adapter_model.bin
│ └── tokenizer files (if applicable)
├── adapter2/
│ ├── adapter_config.json
│ ├── adapter_model.bin
│ └── tokenizer files (if applicable)
└── ...


Each adapter directory must contain:

-
: Required configuration file with the following structure:`adapter_config.json`

-
: The LoRA adapter weights file`adapter_model.bin`


#### Usage Example[¶](https://docs.vllm.ai#usage-example)

-
**Prepare your LoRA adapter**: -
**Verify the directory structure**: -
**Make a request using the adapter**:

#### How It Works[¶](https://docs.vllm.ai#how-it-works)

- When vLLM receives a request for a LoRA adapter named
`my_sql_adapter`

- The filesystem resolver checks if
`/path/to/lora/adapters/my_sql_adapter/`

exists - If found, it validates the
`adapter_config.json`

file - If the configuration matches the base model and is valid, the adapter is loaded
- The request is processed normally with the newly loaded adapter
- The adapter remains available for future requests

## Advanced Configuration[¶](https://docs.vllm.ai#advanced-configuration)

### Multiple Resolvers[¶](https://docs.vllm.ai#multiple-resolvers)

You can configure multiple resolver plugins to load adapters from different sources:

'lora_s3_resolver' is an example of a custom resolver you would need to implement

All listed resolvers are enabled; at request time, vLLM tries them in order until one succeeds.

### Custom Resolver Implementation[¶](https://docs.vllm.ai#custom-resolver-implementation)

To implement your own resolver plugin:

-
**Create a new resolver class**: -
**Register the resolver**:

## Troubleshooting[¶](https://docs.vllm.ai#troubleshooting)

### Common Issues[¶](https://docs.vllm.ai#common-issues)

**"VLLM_LORA_RESOLVER_CACHE_DIR must be set to a valid directory"**- Ensure the directory exists and is accessible
-
Check file permissions on the directory

-
**"LoRA adapter not found"** - Verify the adapter directory name matches the requested model name
- Check that
`adapter_config.json`

exists and is valid JSON -
Ensure

`adapter_model.bin`

exists in the directory -
**"Invalid adapter configuration"** - Verify
`peft_type`

is set to "LORA" - Check that
`base_model_name_or_path`

matches your base model -
Ensure

`target_modules`

is properly configured -
**"LoRA rank exceeds maximum"** - Check that
`r`

value in`adapter_config.json`

doesn't exceed`max_lora_rank`

setting

### Debugging Tips[¶](https://docs.vllm.ai#debugging-tips)

-
**Enable debug logging**: -
**Verify environment variables**: -
**Test adapter configuration**: