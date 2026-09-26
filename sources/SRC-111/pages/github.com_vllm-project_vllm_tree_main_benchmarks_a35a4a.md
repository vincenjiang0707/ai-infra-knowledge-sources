source: https://github.com/vllm-project/vllm/tree/main/benchmarks

This directory used to contain vLLM's benchmark scripts and utilities for performance testing and evaluation.

**Serving benchmarks**: Scripts for testing online inference performance (latency, throughput)**Throughput benchmarks**: Scripts for testing offline batch inference performance**Specialized benchmarks**: Tools for testing specific features like structured output, prefix caching, long document QA, request prioritization, and multi-modal inference**Dataset utilities**: Framework for loading and sampling from various benchmark datasets (ShareGPT, HuggingFace datasets, synthetic data, etc.)

For detailed usage instructions, examples, and dataset information, see the [Benchmark CLI documentation](https://docs.vllm.ai/en/latest/benchmarking/cli/#benchmark-cli).

For full CLI reference see: