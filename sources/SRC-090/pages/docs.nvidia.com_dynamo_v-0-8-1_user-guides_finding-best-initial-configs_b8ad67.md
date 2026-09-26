source: https://docs.nvidia.com/dynamo/v-0-8-1/user-guides/finding-best-initial-configs
lastmod: 2026-09-24T19:58:16.636Z

# Finding Best Initial Configs using AIConfigurator

[AIConfigurator](https://github.com/ai-dynamo/aiconfigurator/tree/main) is a performance optimization tool that helps you find the optimal configuration for deploying LLMs with Dynamo. It automatically determines the best number of prefill and decode workers, parallelism settings, and deployment parameters to meet your SLA targets while maximizing throughput.

## Why Use AIConfigurator?

When deploying LLMs with Dynamo, you need to make several critical decisions:

**Aggregated vs Disaggregated**: Which architecture gives better performance for your workload?**Worker Configuration**: How many prefill and decode workers to deploy?**Parallelism Settings**: What tensor/pipeline parallel configuration to use?**SLA Compliance**: How to meet your TTFT and TPOT targets?

AIConfigurator answers these questions in seconds, providing:

- Optimal configurations that meet your SLA requirements
- Ready-to-deploy Dynamo configuration files
- Performance comparisons between different deployment strategies
- Up to 1.7x better throughput compared to manual configuration

## Quick Start

## Example Output

### Custom Configuration

## Common Use Cases

## Supported Configurations

**Models**: GPT, LLAMA2/3, QWEN2.5/3, Mixtral, DEEPSEEK_V3
**GPUs**: H100, H200, A100, B200 (preview), GB200 (preview)
**Backend**: TensorRT-LLM (vLLM and SGLang coming soon)

## Additional Options

## Troubleshooting

**Model name mismatch**: Use exact model name that matches your deployment
**GPU allocation**: Verify available GPUs match `--total_gpus`

**Performance variance**: Results are estimates - benchmark actual deployment