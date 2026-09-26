source: https://docs.nvidia.com/dynamo/zh-CN/kubernetes/installation/managed-kubernetes/eks/eks-setup
lastmod: 2026-09-24T19:58:16.636Z

Amazon Elastic Kubernetes Service (EKS)


Amazon Elastic Kubernetes Service (EKS)

Deploys the Dynamo platform on Amazon EKS, including cluster creation, GPU node groups, and add-ons.

This guide demonstrates the Dynamo platform on Amazon Elastic Kubernetes Service (EKS).

### Clone the repository and set working directory

Manifest and template paths in this guide are relative to `examples/deployments/EKS/`

in the Dynamo repository.

### Setup environment variables

We will use those environment variables throughout this guide.
If you would like to use a different region, modify the `AWS_REGION`

variable

### Install CLIs

### Install AWS CLI ([AWS CLI installation guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html))

### Install Kubernetes CLI ([kubectl installation guide for EKS](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html))

### Install Eksctl CLI ([eksctl installation guide](https://eksctl.io/installation/))

### Install Helm CLI ([Helm setup for EKS](https://docs.aws.amazon.com/eks/latest/userguide/helm.html))

### Create an EKS Auto Mode cluster

Creating an EKS Auto Mode cluster using Eksctl with `eksctl.yaml`

.
This will create an EKS Auto Mode cluster with the Amazon EFS CSI Driver installed as an addon, we will later use Amazon EFS to store model weights and compilation to be used by Dynamo.

*Note: eksctl will automatically configure kubeconfig context for you, if not you can run: aws eks update-kubeconfig --region $AWS_REGION --name $CLUSTER_NAME*

### Create an EKS Auto Mode GPU NodePool

Creating a GPU NodePool that targets the **g5,g6,g6e,g7e,p5,p5e,p5en** instance families.

### Create a default StorageClass

Create a default StorageClass to use the storage capability of EKS Auto Mode, this will make the default StorageClass to use EBS volumes for Stateful workloads needed by NATS that is used with Dynamo.

### Install Dynamo Kubernetes Platform

### Install Dynamo Platform

### Setup HuggingFace TOKEN

### Verify installation

Validate that the Dynamo platform pods are running, you should see an output similar to output below.

Validate that the Dynamo CRDs were installed

### Deploy a Dynamo DynamoGraphDeployment (DGD)

### Cache Models on EFS

Before deploying an inference graph, download the model weights onto the shared EFS file system. Each Dynamo recipe includes a `model-cache/model-download.yaml`

Job manifest that downloads the model from HuggingFace.

Copy the recipe’s download manifest into the local kustomize directory and apply it:

The recipe manifests don’t set any memory resources on the download container. Without a memory request, the Job pod can get OOMKilled during download — especially for large models. The `kustomization.yaml`

in `manifests/model-download/`

patches in a memory request to prevent this. By default it adds `4Gi`

.

For larger models (e.g. DeepSeek-R1, Nemotron-3-Super-120B) increase this value in `manifests/model-download/kustomization.yaml`

before applying:

Then apply:

Monitor the download Job:

To re-run a download (e.g. after changing the model or fixing an OOM), delete the previous Job first:

Then copy the new recipe’s manifest and apply again.

### Disaggregated Serving

This example deploys a disaggregated prefill/decode Dynamo Inference Graph that uses NIXL with the LIBFABRIC backend using [Elastic Fabric Adapter (EFA)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html) for high-throughput KV-cache transfer between workers.

It targets `g7e.12xlarge`

instances, which support GPUDirect RDMA, and uses the Dynamo EFA-enabled vLLM container `nvcr.io/nvidia/ai-dynamo/vllm-runtime:1.4.0-efa`

that ships with the [EFA Installer](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-changelog.html) pre-installed.

*Note: For a full list of EFA-supported instance types, see the AWS EC2 Docs.*

KV-cache transfer between workers uses [NIXL](https://github.com/ai-dynamo/nixl) with the LIBFABRIC backend. Enable it by passing the following argument to vLLM:

`--kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both","kv_connector_extra_config": {"backends": ["LIBFABRIC"]}}'`


*Note: On instance types without EFA support, NIXL’s libfabric backend falls back to TCP automatically. However, vLLM’s NixlConnector defaults to cuda as the buffer device, so you must add "kv_buffer_device":"cpu" to the kv-transfer-config argument for disaggregated serving to work without EFA.*




Request an EFA device for each worker pod using the `vpc.amazonaws.com/efa`

extended resource:

*Note: EKS Auto Mode includes the EFA device plugin making vpc.amazonaws.com/efa extended resource available.*

All workers (prefill and decode) must be co-located in the same availability zone, since EFA traffic does not cross AZ boundaries. Use a pod affinity rule to enforce this:

*Note: manifests/vllm/disagg-tcp.yaml provides an alternative example that uses TCP instead of EFA, targeting g6e.2xlarge instances.*


Verify that all pods reach `Running`

status:

You should see output similar to below

*Note: The initial request for each worker will occur increased latency, this is due to the NIXL backend handshake and initialization overhead, this operation is only for the very first transfer*

Watch logs

Cleanup

### Aggregated Serving

Your pods should be running like below output, making sure they are in status “Running”.

Watch logs

You should see output similar to below

Cleanup

## Using On-Demand Capacity Reservations (ODCR) and Capacity Blocks (CBs) for ML

GPU instances can be difficult to acquire on-demand. AWS provides two reservation mechanisms to guarantee capacity for ML workloads:

[On-Demand Capacity Reservations (ODCRs)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html)reserve capacity in a specific AZ for any duration. You pay for the reserved capacity whether or not you use it.[Capacity Blocks for ML](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-blocks.html)reserve GPU instances for a fixed time window (hours to days). Instances are placed in EC2 UltraClusters for low-latency networking. Capacity Blocks have a defined end time, and EC2 will terminate instances before the block expires.

EKS Auto Mode uses Karpenter under the hood, which models reserved capacity as `karpenter.sh/capacity-type: reserved`

and prioritizes it over on-demand and spot.

By default, EKS Auto Mode can launch into open ODCRs automatically, but does not prioritize them. Capacity Blocks are never used automatically. Both require explicit `capacityReservationSelectorTerms`

configuration on a NodeClass to be prioritized and labeled as `reserved`

.

### Create a NodeClass with Capacity Reservation

Create a NodeClass that references your ODCR or Capacity Block reservation. You can select by reservation ID or by tags.

First, extract the subnet, security group, and role configuration from the `default`

NodeClass that EKS Auto Mode already created:

Replace `<CR ID>`

with your actual reservation ID from the EC2 console.

Wait until the status of the capacityReservation state is `active`

.

### Create a NodePool for Reserved Capacity

Create a NodePool that references the `gpu-reserved`

NodeClass and uses the `reserved`

capacity type. You can optionally include `on-demand`

and `spot`

as a fallback when the reservation is exhausted.

Validate that the `gpu-reserved`

NodePool is ready

When configuring `capacityReservationSelectorTerms`

on any NodeClass in the cluster, EKS Auto Mode will stop automatically using open ODCRs for all NodeClasses. Make sure all NodeClasses that should use ODCRs have explicit selector terms configured.

### Targeting Reserved Nodes from Workloads

Pods are scheduled onto reserved nodes through the existing NodePool requirements and taints. If you want to ensure a workload only runs on reserved capacity, add a node selector:

### Capacity Blocks Considerations

Capacity Blocks have a fixed end time. EC2 begins terminating instances 30 minutes before the block expires (60 minutes for UltraServer types). Karpenter will start draining nodes 10 minutes before EC2 termination begins, giving your workloads time to gracefully shut down.

Plan your inference workloads accordingly, and consider using `on-demand`

as a fallback capacity type in the NodePool if you need continuity beyond the Capacity Block window.

## Cleanup

Delete all DynamoGraphDeployment

Uninstall Dynamo platform

Clean leftover PVCs related to NATS

Delete the AutoMode GPU nodepool

Cleanup EFS related resources, follow the [EFS setup guide](https://docs.nvidia.com/dynamo/kubernetes/installation/model-storage/efs#cleanup) cleanup section

Delete the EKS Auto Mode cluster using Eksctl