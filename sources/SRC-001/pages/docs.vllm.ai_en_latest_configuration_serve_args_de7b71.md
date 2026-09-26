source: https://docs.vllm.ai/en/latest/configuration/serve_args/
lastmod: 2026-09-24

# Server Arguments[¶](https://docs.vllm.ai#server-arguments)

The `vllm serve`

command is used to launch the OpenAI-compatible server.

## CLI Arguments[¶](https://docs.vllm.ai#cli-arguments)

The `vllm serve`

command is used to launch the OpenAI-compatible server. To see the available options, take a look at the [CLI Reference](https://docs.vllm.ai/cli/)!

## Configuration file[¶](https://docs.vllm.ai#configuration-file)

You can load CLI arguments via a [YAML](https://yaml.org/) config file. The argument names must be the long form of those outlined [above](https://docs.vllm.ai/).

For example:

# config.yaml
model: meta-llama/Llama-3.1-8B-Instruct
host: "127.0.0.1"
port: 6379
uvicorn-log-level: "info"


To use the above config file:

### Generate a configuration from vLLM Recipes[¶](https://docs.vllm.ai#generate-a-configuration-from-vllm-recipes)

[vLLM Recipes](https://recipes.vllm.ai/) can be converted into `config.yaml`

and `env.sh`

. See the [ Recipes conversion tool README](https://github.com/vllm-project/vllm/blob/main/tools/recipes/README.md) for usage.

Source the generated environment before starting vLLM:

Note

In case an argument is supplied simultaneously using command line and the config file, the value from the command line will take precedence. The order of priorities is `command line > config file values > defaults`

. e.g. `vllm serve SOME_MODEL --config config.yaml`

, SOME_MODEL takes precedence over `model`

in config file.