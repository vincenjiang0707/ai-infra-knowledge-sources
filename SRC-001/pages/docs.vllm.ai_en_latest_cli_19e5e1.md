source: https://docs.vllm.ai/en/latest/cli/
lastmod: 2026-09-23

# vLLM CLI Guide[¶](https://docs.vllm.ai#vllm-cli-guide)

The vllm command-line tool is used to run and manage vLLM models. You can start by viewing the help message with:

Available Commands:

## serve[¶](https://docs.vllm.ai#serve)

Starts the vLLM OpenAI Compatible API server.

Start with a model:

Specify the port:

Serve over a Unix domain socket:

Check with --help for more options:

# To list all flags
vllm serve --help=all
# To view an argument group
vllm serve --help=ModelConfig
# To view a single argument
vllm serve --help=max-num-seqs
# To search by keyword or flag name
vllm serve --help=max


Human-readable integer arguments

Many integer arguments accept human-readable suffixes for convenience. For example:

`1k`

= 1,000 (decimal kilo)`1K`

= 1,024 (binary kibibyte)`1m`

= 1,000,000 (decimal mega)`1M`

= 1,048,576 (binary mebibyte)`1g`

/`1G`

= 1 billion / 1 gibibyte`1t`

/`1T`

= 1 trillion / 1 tebibyte

Decimal suffixes (`k`

, `m`

, `g`

, `t`

) also accept floating point: `25.6k`

= 25,600. Binary suffixes (`K`

, `M`

, `G`

, `T`

) require integers: `32K`

= 32,768.

Supported arguments include: `--max-model-len`

, `--max-num-batched-tokens`

, `--max-num-scheduled-tokens`

, `--kv-cache-memory-bytes`

, `--safetensors-prefetch-block-size`

.

See [vllm serve](https://docs.vllm.ai/serve/) for the full reference of all available arguments.

## launch[¶](https://docs.vllm.ai#launch)

Launch individual vLLM components.

# Launch the rendering server component
vllm launch render meta-llama/Llama-3.2-1B-Instruct
# Inspect all available flags for the render component
vllm launch render --help=all


See [vllm launch render](https://docs.vllm.ai/launch/render/) for the current launch component reference.

## chat[¶](https://docs.vllm.ai#chat)

Generate chat completions via the running API server.

# Directly connect to localhost API without arguments
vllm chat
# Specify API url
vllm chat --url http://{vllm-serve-host}:{vllm-serve-port}/v1
# Quick chat with a single prompt
vllm chat --quick "hi"
# Print TTFT and throughput statistics after each response
vllm chat --stats


See [vllm chat](https://docs.vllm.ai/chat/) for the full reference of all available arguments.

## complete[¶](https://docs.vllm.ai#complete)

Generate text completions based on the given prompt via the running API server.

# Directly connect to localhost API without arguments
vllm complete
# Specify API url
vllm complete --url http://{vllm-serve-host}:{vllm-serve-port}/v1
# Quick complete with a single prompt
vllm complete --quick "The future of AI is"
# Print TTFT and throughput statistics after each response
vllm complete --stats


See [vllm complete](https://docs.vllm.ai/complete/) for the full reference of all available arguments.

## bench[¶](https://docs.vllm.ai#bench)

Run benchmark tests for latency online serving throughput and offline inference throughput.

To use benchmark commands, please install with extra dependencies using `pip install vllm[bench]`

.

Available Commands:

### latency[¶](https://docs.vllm.ai#latency)

Benchmark the latency of a single batch of requests.

vllm bench latency \
--model meta-llama/Llama-3.2-1B-Instruct \
--input-len 32 \
--output-len 1 \
--enforce-eager \
--load-format dummy


See [vllm bench latency](https://docs.vllm.ai/bench/latency/) for the full reference of all available arguments.

### serve[¶](https://docs.vllm.ai#serve_1)

Benchmark the online serving throughput.

vllm bench serve \
--model meta-llama/Llama-3.2-1B-Instruct \
--host server-host \
--port server-port \
--random-input-len 32 \
--random-output-len 4 \
--num-prompts 5


See [vllm bench serve](https://docs.vllm.ai/bench/serve/) for the full reference of all available arguments.

### throughput[¶](https://docs.vllm.ai#throughput)

Benchmark offline inference throughput.

vllm bench throughput \
--model meta-llama/Llama-3.2-1B-Instruct \
--input-len 32 \
--output-len 1 \
--enforce-eager \
--load-format dummy


See [vllm bench throughput](https://docs.vllm.ai/bench/throughput/) for the full reference of all available arguments.

## collect-env[¶](https://docs.vllm.ai#collect-env)

Start collecting environment information.

## run-batch[¶](https://docs.vllm.ai#run-batch)

Run batch prompts and write results to file.

Running with a local file:

vllm run-batch \
-i examples/features/openai_batch/openai_example_batch.jsonl \
-o results.jsonl \
--model meta-llama/Meta-Llama-3-8B-Instruct


Using remote file:

vllm run-batch \
-i https://raw.githubusercontent.com/vllm-project/vllm/main/examples/features/openai_batch/openai_example_batch.jsonl \
-o results.jsonl \
--model meta-llama/Meta-Llama-3-8B-Instruct


See [vllm run-batch](https://docs.vllm.ai/run-batch/) for the full reference of all available arguments.

## More Help[¶](https://docs.vllm.ai#more-help)

For detailed options of any subcommand, use: