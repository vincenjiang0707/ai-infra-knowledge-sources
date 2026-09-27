# scaling-moe-reinforcement-learning-on-amazon-eks-with-efa-and-deepep-with-40-more-throughput

source: https://aws.amazon.com/blogs/machine-learning/scaling-moe-reinforcement-learning-on-amazon-eks-with-efa-and-deepep-with-40-more-throughput/

[Artificial Intelligence](https://aws.amazon.com/blogs/machine-learning/)

# Scaling MoE reinforcement learning on Amazon EKS with EFA and DeepEP with 40% more throughput

When you post-train a Mixture-of-Experts (MoE) model with Reinforcement Learning from Human Feedback (RLHF) or Group Relative Policy Optimization (GRPO) at scale, three simultaneous challenges emerge. The first requires coordinating heterogeneous compute for rollout generation and policy training. Second, sustaining high-throughput communication across hundreds of accelerators. And third, dynamically orchestrating every subsystem to keep them in balance. On AWS, you can address these challenges using Amazon Elastic Kubernetes Service (Amazon EKS), Elastic Fabric Adapter (EFA), and DeepEP.

Mixture-of-Experts (MoE) has become a standard architecture for scaling large language models (LLMs) to hundreds of billions or even trillions of parameters, while maintaining efficient inference through sparsity. However, sparsity doesn’t remove infrastructure complexity in training. As part of the standard training pipeline, these models must undergo pre-training, mid-training, supervised fine-tuning (SFT), and reinforcement learning (RL). Among these stages, large-scale RL training places unusual demands on infrastructure because it combines elastic inference work with tightly coupled model training that requires high-bandwidth communication. Reward models, verifiers, and checkpoint updates add further memory, networking, and orchestration pressure. This type of multi-workload optimization reflects a common infrastructure challenge when you run model training, inference, and evaluation on shared resources without creating bottlenecks or leaving capacity idle.

Compared with dense models, post-training MoE models introduce a new infrastructure challenge: as newer MoE architectures become increasingly sparse to reduce inference costs, training becomes constrained more by communication than by compute. A key source of this communication overhead is Expert Parallelism (EP). EP introduces dynamic all-to-all token routing across devices, in addition to the dense, structured communication patterns of Tensor Parallelism (TP), Data Parallelism (DP), and Pipeline Parallelism (PP). In tightly coupled asynchronous RL workloads, the heterogeneous compute and communication demands of MoE training must be balanced with inference-based generation. Slow training steps stall inference workers, while insufficient inference throughput leaves training accelerators idle. This challenge is common across large-scale reinforcement learning workloads, including RLHF pipelines based on Proximal Policy Optimization (PPO) and newer approaches such as GRPO.

PPO typically uses a critic model to estimate value during policy optimization, while GRPO avoids the need for a separate critic model by using group-based relative rewards. Although their algorithmic and model requirements differ, both impose similar infrastructure demands: large-scale rollout generation, tightly coupled policy training, and high-bandwidth inter-node communication.

In this post, we describe an architecture optimized to accelerate MoE training that combines Amazon Elastic Kubernetes Service (Amazon EKS) and EFA to orchestrate and accelerate large-scale RL training and how DeepEP optimizes expert-parallel communication over EFA.

## Challenges of large-scale RL training

Large-scale RL training presents three interrelated challenges:

- Balancing the competing resource demands of rollout generation and policy training.
- Managing accelerator compute, memory, and network bandwidth simultaneously.
- Handling the shift from high-bandwidth intra-node communication to lower-bandwidth inter-node links as jobs scale beyond a single instance.

### The rollout-training loop

Large-scale asynchronous RL jobs have two distinct, simultaneous workloads to optimize: rollout generation and policy training. During rollout generation, the system performs large-scale distributed inference focused on maximizing aggregate throughput rather than minimizing time to first token (TTFT) or inter-token latency. In contrast, policy training requires tightly coupled workers that progress in lockstep, much like pre-training or SFT. Any latency spike or straggling worker can stall the entire job or trigger NVIDIA Collective Communications Library (NCCL) timeouts. RL systems must balance these two workloads because any mismatch in their rates can leave hardware idle or introduce training instability.

### Compute, memory, and bandwidth pressure

RL workloads have heterogeneous compute and communication demands. As a result, any RL system must balance three resource constraints: accelerator compute, memory, and network bandwidth. Policy training is compute-intensive and must keep pace with rollout generation. At the same time, distributed inference must manage KV-cache capacity and token generation. Balancing memory bandwidth and compute is critical for maximum throughput because MoE layers add sparse, dynamic all-to-all communication as tokens are routed across devices. Reward models provide feedback during training, and data movement adds further pressure. All of these subsystems must be balanced jointly to help prevent any one from becoming a bottleneck.

### Intra-node versus inter-node communication

As RL training jobs scale beyond a single instance, model partitions and parallelism groups span multiple nodes, shifting communication from the high-bandwidth intra-node NVLink fabric to lower-bandwidth inter-node links. MoE models intensify this shift: unlike the structured patterns of Tensor Parallelism and Pipeline Parallelism, Expert Parallelism dynamically routes tokens across devices through sparse, fine-grained all-to-all communication traffic that becomes increasingly inter-node as the expert parallelism degree grows.

AWS accelerated computing instances such as P5 and P6 use two primary communication domains: an intra-instance NVLink fabric, typically connected through NVSwitch, and inter-instance networking through EFA. EFA provides high-bandwidth communication traffic between instances. On [supported configurations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html#efa-instance-types), EFA works with NVIDIA GPUDirect RDMA and OS bypass to transfer data directly between GPU memory buffers across instances, reducing CPU and operating-system involvement in the communication path. Optimizing bandwidth utilization in RL workloads requires balancing these two communication domains by determining which operations can run efficiently over EFA and which must remain within the NVLink fabric.

## Architecture overview

To scale RL workloads on AWS, we combine Amazon EKS, EFA, and Amazon Simple Storage Service (Amazon S3) so that orchestration, high-performance communication, and durable storage can scale independently. With Amazon EKS, you can manage the lifecycle and placement of heterogeneous workers. With EFA, you get the inter-node data path for communication-intensive GPU workloads. With Amazon S3, you can store datasets, model checkpoints, and completed training artifacts including the model weights. The following sections describe how to map the distinct layers of the RL system, covering orchestration, high-performance networking, and durable storage, and how each layer scales independently.

### EKS cluster topology

The Amazon EKS cluster contains separate node groups optimized for each stage of the RL workflow. GPU-accelerated instances run rollout generation, reward-model inference, and policy training, while CPU instances execute environments and preprocessing tasks. Memory-optimized instances host experience buffers and checkpoint caches, allowing producers and consumers to exchange data without placing durable storage directly on the critical path.

### RL job topology

During rollout, the model generates samples through interactions with CPU-based environment pods, and the resulting experience flows into a memory-optimized buffer. From there, the policy-training step consumes batches, updates model weights, and publishes new checkpoints that feed back into the next round of rollout generation. Checkpoints and completed training artifacts are also persisted to Amazon S3 for durable storage, recovery, and downstream use. Policy training, weight updates, and new checkpoint generation can all run on the EKS cluster.

### Network and execution layers

EKS provides the control plane for scheduling, scaling, failure recovery, and coordination across different worker groups. Within GPU instances, NVLink and NVSwitch carry high-bandwidth intra-node communication. EFA supports latency-sensitive inter-node communication for distributed policy training and other tightly coupled GPU operations. The experience buffer and Amazon S3 form the data layer, separating high-frequency samples and checkpoint exchange from long-term artifact storage.

## Performance and cost optimizations

This section covers two key optimizations: using DeepEP to reduce expert-parallel communication overhead over EFA, and using Amazon Elastic Compute Cloud (Amazon EC2) Spot Instances to help lower the cost of rollout generation.

### DeepEP over EFA

DeepEP, along with other topology-aware expert-parallel communication techniques, is a common optimization for MoE workloads that aims to reduce communication bottlenecks. Standard all-to-all collectives are most efficient for dense, regular communication, but MoE workloads generate sparse, fine-grained, and imbalanced traffic as tokens are dynamically routed across experts. As Expert Parallelism spans multiple nodes, synchronization and per-message overhead increase, making inter-node communication a dominant bottleneck. DeepEP addresses this by replacing generic all-to-all collectives with specialized dispatch and combining kernels. These kernels use NVLink for intra-node communication and an RDMA-capable backend for inter-node communication.

Amazon has contributed several features to migrate DeepEP’s communication primitives to libfabric. This makes the transport layer portable across libfabric-supported network fabrics and optimizes MoE training over EFA. With these changes, DeepEP v2 gains native EFA support. Additionally, NCCL 2.31 incorporates the latest EFA optimizations for dense collective communication. In the following section, we describe how DeepEP over EFA improves rollout-generation throughput by reducing the communication overhead of expert dispatch and combining operations.

### How DeepEP communicates over EFA

DeepEP replaces standard NCCL all-to-all collectives with two specialized GPU kernels: a dispatch kernel that routes tokens from local GPUs to remote experts, and a combine kernel that gathers processed tokens back. For intra-node transfers, these kernels use NVLink through NVSwitch. For inter-node transfers, DeepEP uses libfabric to send data over EFA. On supported instance types such as P5 and P6, EFA works with NVIDIA GPUDirect RDMA to transfer data directly between GPU memory buffers across instances, bypassing the CPU and operating system. The upstream contributions from Amazon migrate DeepEP’s communication primitives from a CUDA-specific RDMA backend to libfabric. This makes the transport portable across EFA-supported configurations and reduces per-message overhead for the sparse, fine-grained traffic patterns that Expert Parallelism generates.

Across 48 P5en instances (16 dedicated to training, 32 to inference) running a [super-sparse MoE model](https://github.com/radixark/miles/blob/main/scripts/run_glm5_744b_a40b.py), enabling DeepEP over EFA increased aggregate RL rollout throughput by 40 percent. Figure 5 shows the throughput comparison with and without DeepEP.

### Spot Instances for rollout generation

Rollout generation is well suited to Amazon EC2 Spot Instances because it consists of distributed inference tasks that can be partitioned across independent workers. Unlike policy training, where tightly coupled workers must progress together, the interruption of a rollout worker does not require the entire RL job to stop. Unfinished rollout tasks can be returned to the queue and reassigned while the remaining workers continue generating experience.

With Amazon EKS, you can scale Spot-based rollout node groups according to rollout demand and queue depth while maintaining stable capacity for policy training. Rollout workers should process bounded units of work and publish completed samples frequently. When a Spot interruption notice arrives, workers drain active requests and return unfinished tasks to the queue. This separation can help reduce rollout-generation costs. Policy-training workers remain insulated from Spot interruptions, delays, or NCCL timeouts.

## Putting it all together

This section walks through provisioning the infrastructure described in the previous sections, from cluster creation through running an RL job with DeepEP communication enabled.

### Prerequisites

Before running RL on Amazon EKS, verify the following requirements are met:

- AWS account with appropriate AWS Identity and Access Management (IAM) permissions.
- Amazon EKS 1.31 or later.
- EFA installer 1.49 with AWS OFI NCCL plugin.
- DeepEP 2.0.0, NCCL 2.31.2, SGLang 0.5.17, PyTorch 2.12.1 (CUDA 13.0).
- Supported GPU instances, such as p5.48xlarge, p5e.48xlarge, or p6-b200.48xlarge.
- Familiarity with Kubernetes and distributed training concepts.

### EKS cluster setup

This architecture can be deployed on [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) by separating policy training, rollout generation, and supporting services across independently managed node groups. This preserves the isolation between tightly coupled training workloads and more elastic rollout workers while allowing each component to use the capacity model optimized for its execution characteristics.

Managed node groups streamline provisioning, updates, and instance lifecycle management. Policy-training workers can run on stable GPU capacity, while rollout-generation capacity can scale independently and incorporate Spot Instances where interruption tolerance permits. CPU-based services, including orchestration and supporting components, can be placed in separate node groups to avoid competing with GPU workloads for capacity.

The following eksctl ClusterConfig defines a general-purpose CPU node group and a GPU accelerator node group for the cluster:

The listed Ampere, Hopper, and Blackwell instance types (p4d.24xlarge, p4de.24xlarge, p5.48xlarge, p5e.48xlarge, p6-b200.48xlarge, and p6-b300.48xlarge) support large-scale RL training and can be used for either rollout or training workloads.

*Figure 6: Representative EKS deployment topology showing GPU node groups (P5/P6) for* *training and rollout, Spot-backed capacity for inference workers, and CPU node groups for* *orchestration services.*

### Setting up EFA drivers and plugins

To optimize asynchronous RL on Amazon EKS, communicating nodes must be in the same Availability Zone (AZ) and the EFA Kubernetes device plugin must be set up. With EFA, you get fast and efficient model updates, high-performance model training, and low-latency communication. To apply the EKS EFA device plugin, you can use `kubectl`

to apply it directly to the cluster.

For additional instructions and performance testing, see the [EKS EFA setup instructions](https://docs.aws.amazon.com/eks/latest/userguide/node-efa.html).

### Launching DeepEP

The reference implementation combines the CUDA, PyTorch, communication, and inference components required to support the optimizations described in the previous sections. The following table lists the benchmark environment:

- CUDA: 13.0.
- PyTorch: 2.12+cu130.
- NCCL: 2.31.
- EFA: 1.49.
- DeepEP: 2.0.
- SGLang: 0.5.17.
- Miles:
[0.1.0](https://github.com/radixark/miles/releases/tag/v0.1.0).

Keeping these components aligned is critical. GPU kernels, collective communication libraries, and the underlying EFA transport each contribute to end-to-end performance. Using the `763104351884.dkr.ecr.<region>.amazonaws.com/sglang:0.5.17-gpu-py312-cu130-ubuntu24.04-ec2`

image (available in the [SGLang Deep Learning Containers catalog](https://aws.github.io/deep-learning-containers/reference/available_images/#sglang-ubuntu)) is a practical starting point. The following Dockerfile can be used to set up the training stack.

### Launch a job

With TorchX, you can submit RL workloads to Amazon EKS while keeping application configuration separate from infrastructure configuration. TorchX translates job requirements into Kubernetes resources, including compute requests, storage mounts, and runtime configuration. This separation makes it easier to vary model and training configurations without coupling them to cluster provisioning.

The following command uses TorchX to submit an RL training job to your Amazon EKS cluster. The reference `train_rl.py`

script, available in the [Miles repository](https://github.com/radixark/miles), orchestrates the rollout-training loop described earlier, launching rollout workers and policy-training workers as separate Kubernetes pods. The deepseek_v3_moe configuration specifies the MoE model architecture, including the number of experts and parallelism strategy. TorchX keeps application configuration separate from the underlying Kubernetes infrastructure, so you can adjust model parameters, worker counts, and parallelism settings without modifying cluster-level resources.

A RL job can be launched with the following command:

## Clean up

To avoid ongoing charges, delete the resources you created during this walkthrough. First, delete any running training jobs and their associated pods. Next, remove the EKS managed node groups for policy training, rollout generation, and environment workers. Then, delete the EKS cluster itself. Finally, verify that any associated Amazon EC2 Spot capacity, Elastic Network Interfaces for EFA, and Amazon S3 buckets used for checkpoints are also removed or emptied as needed.

For more information about managing Amazon EKS resources, see [Deleting an Amazon EKS cluster](https://docs.aws.amazon.com/eks/latest/userguide/delete-cluster.html) in the Amazon EKS documentation.

## Conclusion and key takeaways

Scaling RLHF and GRPO for MoE models demands infrastructure that balances elastic rollout generation with tightly coupled policy training. In our internal workloads, the architecture improved aggregate rollout throughput by 40 percent (see Figure 5), while also reducing end-to-end policy iteration time and scaling to roughly a thousand accelerators. This comparison uses two configurations on the same 48 P5en instances (16 dedicated to training, 32 to inference) running the same super-sparse MoE model. The baseline used a Slime-based stack (CUDA 12.9, PyTorch 2.9.1, NCCL 2.27, SGLang 0.5.9, Slime 0.2.4) without EFA-accelerated expert parallelism. The improved configuration used the `DeepEP-over-EFA`

stack described in this post (CUDA 13.0, PyTorch 2.12, NCCL 2.31, EFA 1.49, DeepEP 2.0, SGLang 0.5.17, Miles 0.1.0). See Figure 5 for the corresponding throughput comparison.

This post demonstrates how to build and optimize a scalable architecture that combines Amazon EKS, EFA, and Amazon S3 to provide a flexible and cost-effective path for large-scale distributed RL workloads.

### Key takeaways

**Scale components independently:**The heterogeneous nature of RL workloads means different subsystems can scale independently. Cost optimizations such as Spot Instances can therefore be applied selectively.**Balance resource constraints:**RL systems place simultaneous demands on compute, memory, and bandwidth. End-to-end gains require co-design across the stack, combining optimizations from transport and communication primitives to model design.

AWS, in combination with open source components, can help you run large-scale MoE RL workloads with strong performance and cost efficiency. To get started, review the architecture patterns described in this post and adapt them to your own MoE training workloads on Amazon EKS with EFA. For more information, see the [Amazon EKS documentation](https://docs.aws.amazon.com/eks/), the [EFA setup guide for EKS](https://docs.aws.amazon.com/deep-learning-containers/latest/devguide/deep-learning-containers-eks-setup.html), and the [DeepEP repository on GitHub](https://github.com/deepseek-ai/DeepEP). If you have questions or want help adapting this architecture to your workloads, contact your AWS account team or post in the [AWS HPC forum](https://repost.aws/tags/TAi5kkDMNgR-2mY_-UueNRbA/aws-hpc).
