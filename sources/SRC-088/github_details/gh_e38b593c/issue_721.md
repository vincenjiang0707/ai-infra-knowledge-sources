# [Issue #721] Support running speculator training jobs on Kubernetes

source: https://github.com/vllm-project/speculators/issues/721
state: open | updated: 2026-07-10T18:24:58Z
labels: 

## 正文

AFAIK (I might be wrong here) there is no support for running speculator training jobs on Kubernetes.
Right now, the training pipeline (data preparation, hidden state generation, and training with torchrun) looks like it only works on a local machine with GPUs.
I think Kubernetes support could be helpful for two reasons:
1. Training at larger scale - Kubernetes is a common way to run GPU training jobs. Since multi-node training is planned, Kubernetes could work well with that in the future.
2. Development without local GPUs - Some contributors do not have a local GPU. They may use a remote Kubernetes cluster with GPU nodes to test changes, but at the moment there does not seem to be an easy way to do this because there is no Docker image or Kubernetes example.

Maybe the project could add a Dockerfile for the training environment (Python dependencies, CUDA, and torchrun) and an example Kubernetes Job manifest or Helm chart to start a training job?

I'm new to the project, so I may have missed something. If this is already supported, or if it does not match the project's plans, feel free to close it :)

## 评论 (1)

### orestis-z · 2026-07-06

Thanks for the suggestion! A few related things on our side:

- We have an internal interactive dev environment ("devenv") that runs on OpenShift with GPU support, torchrun, and Ray — but it's an interactive tool, not batch job submission like you're describing.
- We also have currently public [llm-compressor-evaluation](https://github.com/Ryfernandes/llm-compressor-evaluation), a Kubeflow Pipelines project for automated model evaluation on RHOAI — closer in spirit to what you're asking for, but for evaluation rather than training.

What you're describing (a training Dockerfile + K8s Job manifest in the speculators repo itself) makes sense as a standalone addition. The evaluation pipeline could serve as a reference for the pattern.

cc @dsikka  @Ryfernandes — thoughts on this? Worth adding a training pipeline to speculators?
