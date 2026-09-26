source: https://docs.nvidia.com/dynamo/zh-CN/v1.2.1/kubernetes-deployment/cloud-provider-guides/aws/efs
lastmod: 2026-09-23T23:30:39.914Z

# Amazon EFS Setup for EKS

This guide walks through creating an Amazon EFS file system and connecting it to your EKS cluster. The EFS CSI Driver was already installed as an addon via `eksctl.yaml`

during cluster creation. Now we need to create the actual file system and make it available to Kubernetes workloads.

This filesystem will be used by Dynamo to store shared model weights and compilation cache across nodes.

## Prerequisites

- EKS cluster created following the
[EKS guide](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/cloud-provider-guides/aws/eks-setup) - Environment variables set:

## Retrieve VPC and Subnet Information

Get the VPC ID associated with your EKS cluster:

Get the CIDR range for the VPC (used for the security group rule):

## Create a Security Group for EFS

Create a security group that allows NFS traffic (port 2049) from within the VPC:

Add an inbound rule to allow NFS traffic from the VPC CIDR:

## Create the EFS File System

Wait for the file system to become available:

You should see `available`

before proceeding.

## Create Mount Targets

Mount targets allow your EKS nodes to access the EFS file system. You need one mount target per subnet where your nodes run.

Get the subnet IDs used by your EKS cluster:

Create a mount target in each subnet:

EFS allows only one mount target per Availability Zone. If multiple subnets are in the same AZ, the command will fail for the duplicates, which is expected and safe to ignore.

Verify mount targets are available:

Wait until all mount targets show `available`

in the State column before proceeding.

## Create Kubernetes StorageClass

Create a StorageClass that uses the EFS CSI driver with dynamic provisioning:

## Create a PersistentVolumeClaim

We create three separate PVCs because different Dynamo recipe examples reference each one individually:

`model-cache`

stores downloaded model weights (e.g. from HuggingFace).`compilation-cache`

stores vLLM/TRT-LLM compilation artifacts.`perf-cache`

stores benchmark traces and performance results.

EFS is elastic, the `storage`

value in the PVC is required by Kubernetes but does not limit the actual storage. EFS will grow and shrink automatically.

## Verify

Confirm the PVC is bound:

You should see output similar to:

## Cleanup

To delete the EFS resources when no longer needed: