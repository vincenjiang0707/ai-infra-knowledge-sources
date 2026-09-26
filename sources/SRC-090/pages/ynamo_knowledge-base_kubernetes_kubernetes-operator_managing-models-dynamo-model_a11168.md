source: https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/managing-models-dynamo-model
lastmod: 2026-09-24T19:58:16.636Z

# Managing Models with DynamoModel

## Overview

`DynamoModel`

is a Kubernetes Custom Resource that represents a machine learning model deployed on Dynamo. It enables you to:

**Deploy LoRA adapters**on top of running base models**Track model endpoints**and their readiness across your cluster**Manage model lifecycle**declaratively with Kubernetes

DynamoModel works alongside `DynamoGraphDeployment`

(DGD) or `DynamoComponentDeployment`

(DCD) resources. While DGD/DCD deploy the inference infrastructure (pods, services), DynamoModel handles model-specific operations like loading LoRA adapters.

## Quick Start

### Prerequisites

Before creating a DynamoModel, you need:

- A running
`DynamoGraphDeployment`

or`DynamoComponentDeployment`

- Components configured with
`modelRef`

pointing to your base model - Pods are ready and serving your base model

For complete setup including DGD configuration, see [Integration with DynamoGraphDeployment](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/managing-models-dynamo-model#integration-with-dynamographdeployment).

### Deploy a LoRA Adapter

**1. Create your DynamoModel:**

**2. Apply and verify:**

**Expected output:**

That’s it! The operator automatically discovers endpoints and loads the LoRA.

For detailed status monitoring, see [Monitoring & Operations](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/managing-models-dynamo-model#monitoring--operations).

## Understanding DynamoModel

### Model Types

DynamoModel supports three model types:

Most users will use ** lora** to deploy fine-tuned models on top of their base model deployments.

### How It Works

When you create a DynamoModel, the operator:

**Discovers endpoints**: Finds all pods running your`baseModelName`

(by matching`modelRef.name`

in DGD/DCD)**Creates service**: Automatically creates a Kubernetes Service to track these pods**Loads LoRA**: Calls the LoRA load API on each endpoint (for`lora`

type)**Updates status**: Reports which endpoints are ready

**Key linkage:**

## Configuration Overview

DynamoModel requires just a few key fields to deploy a model or adapter:

**Example minimal LoRA configuration:**

**For complete field specifications, validation rules, and all options, see:**
📖 [DynamoModel API Reference](https://docs.nvidia.com/dynamo/reference/api/kubernetes/full-api-reference#dynamomodel)

### Status Summary

The status shows discovered endpoints and their readiness:

**Key status fields:**

`totalEndpoints`

/`readyEndpoints`

: Counts of discovered vs ready endpoints`endpoints[]`

: List with addresses, pod names, and ready status`conditions`

: Standard Kubernetes conditions (EndpointsReady, ServicesFound)

For detailed status usage, see the [Monitoring & Operations](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/managing-models-dynamo-model#monitoring--operations) section below

## Common Use Cases

### Use Case 1: S3-Hosted LoRA Adapter

Deploy a LoRA adapter stored in an S3 bucket.

**Prerequisites:**

- S3 bucket accessible from your pods (IAM role or credentials)
- Base model
`meta-llama/Llama-3.3-70B-Instruct`

running via DGD/DCD

**Verification:**

### Use Case 2: HuggingFace-Hosted LoRA

Deploy a LoRA adapter from HuggingFace Hub.

**Prerequisites:**

- HuggingFace Hub accessible from your pods
- If private repo: HF token configured as secret and mounted in pods
- Base model
`Qwen/Qwen3-0.6B`

running via DGD/DCD

**With HuggingFace token:**

### Use Case 3: Local / Shared-Volume LoRA Adapter

Deploy a LoRA adapter from a path that is already present on the worker pods, for
example a shared volume (NFS, PVC, hostPath) mounted into the serving containers.
Use the `file:///`

scheme with an absolute path (note the three slashes,
followed by the absolute path). Only the `file:///`

form is supported.

**Prerequisites:**

- The path must be
**mounted and readable from the serving worker pods**. The operator does not copy the adapter — each worker loads it directly from the given path, so the volume must be mounted at the same path on every pod that serves`baseModelName`

. - Base model
`Qwen/Qwen3-0.6B`

running via DGD/DCD.

**Mounting the volume:** Add the volume and mount to your DGD/DCD worker so the
adapter path exists inside the container:


Note:Because no remote fetch happens, the path in`source.uri`

must match the in-container mount path exactly, and the files must be readable by every worker replica. If a replica cannot see the path, that endpoint will fail to become ready.

### Use Case 4: Multiple LoRAs on Same Base Model

Deploy multiple LoRA adapters on the same base model deployment.

Both LoRAs will be loaded on all pods serving `Qwen/Qwen3-0.6B`

. Your application can then route requests to the appropriate adapter.

## Monitoring & Operations

### Checking Status

**Quick status check:**

**Example output:**

**Detailed status:**

**Example output:**

### Understanding Readiness

An endpoint is **ready** when:

- The pod is running and healthy
- The LoRA load API call succeeded

**Condition states:**

`EndpointsReady=True`

: All endpoints are ready (full availability)`EndpointsReady=False, Reason=NotReady`

: Not all endpoints ready (check message for counts)`EndpointsReady=False, Reason=NoEndpoints`

: No endpoints found

When `readyEndpoints < totalEndpoints`

, the operator automatically retries loading every 30 seconds.

### Viewing Endpoints

**Get endpoint addresses:**

**Output:**

**Get endpoint pod names:**

**Check readiness of each endpoint:**

**Output:**

### Updating a Model

To update a LoRA (e.g., deploy a new version):

The operator will detect the change and reload the LoRA on all endpoints.

### Deleting a Model

For LoRA models, the operator will:

- Unload the LoRA from all endpoints
- Clean up associated resources
- Remove the DynamoModel CR

The base model deployment (DGD/DCD) continues running normally.

## Troubleshooting

### No Endpoints Found

**Symptom:**

**Common Causes:**

-
**Base model deployment not running****Solution:**Deploy your DGD/DCD first, wait for pods to be ready. -
`baseModelName`

mismatch**Solution:**Ensure`baseModelName`

in DynamoModel exactly matches`modelRef.name`

in DGD. -
**Pods not ready****Solution:**Wait for pods to reach`Running`

and`Ready`

state. -
**Wrong namespace****Solution:**Ensure DynamoModel is in the same namespace as your DGD/DCD.

### LoRA Load Failures

**Symptom:**

**Common Causes:**

-
**Source URI not accessible****Solution:**- For S3: Verify bucket permissions, IAM role, credentials
- For HuggingFace: Verify token is valid, repo exists and is accessible
- For
`file:///`

(local/shared volume): Verify the path is mounted and readable on every worker pod, the mount path matches the URI exactly, and the volume is attached to all worker replicas

-
**Invalid LoRA format****Solution:**Ensure your LoRA weights are in the format expected by your backend framework (SGLang, vLLM, etc.) -
**Endpoint API errors****Solution:**Check the backend framework’s logs in the worker pods: -
**Out of memory****Solution:**LoRA adapters require additional memory. Increase memory limits in your DGD:

### Status Shows Not Ready

**Symptom:**
Some endpoints remain not ready for extended periods.

**Diagnosis:**

**Common Causes:**

**Network issues**: Pod can’t reach S3/HuggingFace**Resource constraints**: Pod is OOMing or being throttled**API endpoint not responding**: Backend framework isn’t serving the LoRA API

**When to wait vs investigate:**

**Wait**: If readyEndpoints is increasing over time (LoRAs loading progressively)**Investigate**: If stuck at same readyEndpoints for >5 minutes

### Viewing Events and Logs

**Check events:**

**View operator logs:**

**Common events and messages:**

## Integration with DynamoGraphDeployment

This section shows the complete end-to-end workflow for deploying base models and LoRA adapters together.

DynamoModel and DynamoGraphDeployment work together to provide complete model deployment:

**DGD**: Deploys the infrastructure (pods, services, resources)**DynamoModel**: Manages model-specific operations (LoRA loading)

### Linking Models to Components

The connection is established through the `modelRef`

field in your DGD:

**Complete example:**

### Deployment Workflow

**Recommended order:**

**What happens behind the scenes:**

The operator automatically handles all service discovery - you don’t configure services, labels, or selectors manually.

## API Reference

For complete field specifications, validation rules, and detailed type definitions, see:

## Summary

DynamoModel provides declarative model management for Dynamo deployments:

✅ **Simple**: 2-step deployment of LoRA adapters
✅ **Automatic**: Endpoint discovery and loading handled by operator
✅ **Observable**: Rich status reporting and conditions
✅ **Integrated**: Works seamlessly with DynamoGraphDeployment

**Next Steps:**

- Try the
[Quick Start](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/managing-models-dynamo-model#quick-start)example - Explore
[Common Use Cases](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/managing-models-dynamo-model#common-use-cases) - Check the
[API Reference](https://docs.nvidia.com/dynamo/reference/api/kubernetes/full-api-reference#dynamomodel)for advanced configuration