source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/kubernetes-deployment/start-here/minikube-setup
lastmod: 2026-09-23T23:30:39.914Z

# Minikube Setup

Sets up a local Minikube cluster with GPU support and Istio for running the Dynamo Kubernetes Platform.

Don’t have a Kubernetes cluster? No problem! You can set up a local development environment using Minikube. This guide walks through the set up of everything you need to run Dynamo Kubernetes Platform locally.

## 1. Install Minikube

First things first! Start by installing Minikube. Follow the official [Minikube installation guide](https://minikube.sigs.k8s.io/docs/start/) for your operating system.

## 2. Configure GPU Support (Optional)

Planning to use GPU-accelerated workloads? You’ll need to configure GPU support in Minikube. Follow the [Minikube GPU guide](https://minikube.sigs.k8s.io/docs/tutorials/nvidia/) to set up NVIDIA GPU support before proceeding.

Make sure to configure GPU support before starting Minikube if you plan to use GPU workloads!

## 3. Start Minikube

Time to launch your local cluster!

## 4. Verify Installation

Let’s make sure everything is working correctly!

## Next Steps

Once your local environment is set up, you can proceed with the [Dynamo Kubernetes Platform installation guide](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/start-here/installation-guide) to deploy the platform to your local cluster.