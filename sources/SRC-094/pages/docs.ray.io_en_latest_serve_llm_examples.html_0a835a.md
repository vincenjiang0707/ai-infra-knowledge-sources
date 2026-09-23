source: https://docs.ray.io/en/latest/serve/llm/examples.html
lastmod: 

# Examples[#](https://docs.ray.io#examples)

End-to-end tutorials for deploying LLMs with Ray Serve. Each one walks through configuration, deployment, and querying for a representative model. For the minimal path, start with the [Quickstart](https://docs.ray.io/quick-start.html).

## By model size[#](https://docs.ray.io#by-model-size)

[Deploy a small-sized LLM](https://docs.ray.io/_collections/serve/tutorials/deployment-serve-llm/small-size-llm/README.html): serve a model that fits on a single GPU. The best starting point.[Deploy a medium-sized LLM](https://docs.ray.io/_collections/serve/tutorials/deployment-serve-llm/medium-size-llm/README.html): shard a model across multiple GPUs on one node with tensor parallelism.[Deploy a large-sized LLM](https://docs.ray.io/_collections/serve/tutorials/deployment-serve-llm/large-size-llm/README.html): span a model across multiple nodes with cross-node parallelism.

## By capability[#](https://docs.ray.io#by-capability)

[Deploy a vision LLM](https://docs.ray.io/_collections/serve/tutorials/deployment-serve-llm/vision-llm/README.html): serve a vision-language model that accepts image inputs.[Deploy a reasoning LLM](https://docs.ray.io/_collections/serve/tutorials/deployment-serve-llm/reasoning-llm/README.html): serve a reasoning model and handle its reasoning output.[Deploy a hybrid reasoning LLM](https://docs.ray.io/_collections/serve/tutorials/deployment-serve-llm/hybrid-reasoning-llm/README.html): serve a model that can switch reasoning on and off per request.[Deploy gpt-oss](https://docs.ray.io/_collections/serve/tutorials/deployment-serve-llm/gpt-oss/README.html): deploy OpenAI’s open-weight gpt-oss model.