source: https://docs.vllm.ai/en/latest/deployment/frameworks/anyscale/
lastmod: 2026-09-23

# Anyscale[¶](https://docs.vllm.ai#anyscale)

[Anyscale](https://www.anyscale.com) is a managed, multi-cloud platform developed by the creators of Ray.

Anyscale automates the entire lifecycle of Ray clusters in your AWS, GCP, or Azure account, delivering the flexibility of open-source Ray without the operational overhead of maintaining Kubernetes control planes, configuring autoscalers, managing observability stacks, or manually managing head and worker nodes with helper scripts like [ examples/ray_serving/run_cluster.sh](https://github.com/vllm-project/vllm/blob/main/examples/ray_serving/run_cluster.sh).

When serving large language models with vLLM, Anyscale can rapidly provision [production-ready HTTPS endpoints](https://docs.anyscale.com/examples/deploy-ray-serve-llms) or [fault-tolerant batch inference jobs](https://docs.anyscale.com/examples/ray-data-llm).