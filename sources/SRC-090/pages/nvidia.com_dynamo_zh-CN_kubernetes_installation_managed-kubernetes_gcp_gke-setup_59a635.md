source: https://docs.nvidia.com/dynamo/zh-CN/kubernetes/installation/managed-kubernetes/gcp/gke-setup
lastmod: 2026-09-24T19:58:16.636Z

Google Kubernetes Engine (GKE)


Google Kubernetes Engine (GKE)

## Pre-requisites

### Clone Dynamo GitHub repository

**Note:** Please make sure GitHub branch/commit version matches with Dynamo platform and VLLM container.

### Deploy Inference Graph

We will deploy a LLM model to the Dynamo platform. Here we use `Qwen/Qwen3-0.6B`

model with VLLM and disaggregated deployment as an example.

In the deployment yaml file, some adjustments have to/ could be made:

**(Required)**Add args to change`LD_LIBRARY_PATH`

and`PATH`

of decoder container, to enable GKE find the correct GPU driver- Change VLLM image to the desired one on NGC
- Add namespace to metadata
- Adjust GPU/CPU request and limits
- Change model to deploy

More configurations please refer to [https://github.com/ai-dynamo/dynamo/tree/v1.4.2/examples/deployments/GKE/vllm](https://github.com/ai-dynamo/dynamo/tree/v1.4.2/examples/deployments/GKE/vllm)

### Highlighted configurations in yaml file

Please note that `LD_LIBRARY_PATH`

needs to be set properly in GKE as per [Run GPUs in GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/gpus)

The following snippet needs to be present in the `args`

field of the deployment `yaml`

file:

For example, refer to the [ release/1.4.0 disaggregated manifest](https://github.com/ai-dynamo/dynamo/blob/release/1.4.0/examples/deployments/GKE/vllm/v1beta1/disagg.yaml):