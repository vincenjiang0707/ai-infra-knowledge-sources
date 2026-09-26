source: https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/training/scale-model-training.html

# Scaling model training[#](https://rocm.docs.amd.com#scaling-model-training)

2026-02-19

4 min read time

To train a large-scale model like OpenAI GPT-2 or Meta Llama 2 70B, a single GPU cannot store all the model parameters required for training. This immense scale presents a fundamental challenge: no single GPU can simultaneously store and process the entire model’s parameters during training. PyTorch provides an answer to this computational constraint through its distributed training frameworks.

## PyTorch distributed[#](https://rocm.docs.amd.com#pytorch-distributed)

Features in `torch.distributed`

are categorized into three main components:

In this topic, the focus is on the distributed data-parallelism strategy as it’s the most popular. To get started with DDP, you need to first understand how to coordinate the model and its training data across multiple GPUs.

The DDP workflow on multiple GPUs is as follows:

Split the current global training batch into small local batches on each GPU. For instance, if you have 8 GPUs and the global batch is set at 32 samples, each of the 8 GPUs will have a local batch size of 4 samples.

Copy the model to every device so each can process its local batches independently.

Run a forward pass, then a backward pass, and output the gradient of the weights with respect to the loss of the model for that local batch. This happens in parallel on multiple devices.

Synchronize the local gradients computed by each device and combine them to update the model weights. The updated weights are then redistributed to each device.


In DDP training, each process or worker owns a replica of the model and processes a batch of data, and then the reducer uses
`allreduce`

to sum up gradients over different workers.

See the following developer blogs for more in-depth explanations and examples.

### PyTorch FSDP[#](https://rocm.docs.amd.com#pytorch-fsdp)

As noted in [PyTorch distributed](https://rocm.docs.amd.com#rocm-for-ai-pytorch-distributed), DDP model weights and optimizer states
are evenly replicated across all workers. Fully Sharded Data Parallel (FSDP) is a type of data parallelism that shards
model parameters, optimizer states, and gradients across DDP ranks.

When training with FSDP, the GPU memory footprint is smaller than when training with DDP across all workers. This makes training some very large models feasible by allowing larger models or batch sizes to fit on-device. However, this comes with the cost of increased communication volume. The communication overhead is reduced by internal optimizations like overlapping communication and computation.

For a high-level overview of how FSDP works, review [Getting started with Fully Sharded Data Parallel](https://pytorch.org/tutorials/intermediate/FSDP_tutorial.html#how-fsdp-works).

For detailed training steps, see [PyTorch FSDP examples](https://github.com/pytorch/examples/tree/main/distributed/FSDP).

### DeepSpeed[#](https://rocm.docs.amd.com#deepspeed)

[DeepSpeed](https://deepspeed.ai) offers system innovations that make large-scale deep learning training effective,
efficient, and easy to use. Innovations such as ZeRO, 3D-Parallelism, DeepSpeed-MoE, ZeRO-Infinity, and so on fall under
the training pillar.

See [Pre-training a large language model with Megatron-DeepSpeed on multiple AMD GPUs](https://rocm.blogs.amd.com/artificial-intelligence/megatron-deepspeed-pretrain/README.html) for a detailed example of
training with DeepSpeed on an AMD GPU.

### Automatic mixed precision (AMP)[#](https://rocm.docs.amd.com#automatic-mixed-precision-amp)

As models increase in size, so do the time and memory needed to train them; their cost also increases. Any measure we
can take to reduce training time and memory usage through [automatic mixed precision](https://pytorch.org/docs/stable/amp.html) (AMP) is highly beneficial for most use cases.

See [Automatic mixed precision in PyTorch using AMD GPUs — ROCm Blogs](https://rocm.blogs.amd.com/artificial-intelligence/automatic-mixed-precision/README.html#automatic-mixed-precision-in-pytorch-using-amd-gpus)
for more information about running AMP on an AMD Instinct-Series GPU.

## Fine-tuning your model[#](https://rocm.docs.amd.com#fine-tuning-your-model)

ROCm supports multiple techniques for [optimizing fine-tuning](https://rocm.docs.amd.com/fine-tuning/overview.html#fine-tuning-llms-concept-optimizations), for
example, LoRA, QLoRA, PEFT, and FSDP.

Learn more about challenges and solutions for model fine-tuning in [Use ROCm for fine-tuning LLMs](https://rocm.docs.amd.com/fine-tuning/index.html).

The following developer blogs showcase examples of fine-tuning a model on an AMD GPU.

Fine-tuning Llama2 with LoRA

Fine-tuning Llama2 with QLoRA

Fine-tuning a BERT-based LLM for a text classification task using JAX

Fine-tuning StarCoder using PEFT

Recipes for fine-tuning Llama2 and 3 with

`llama-recipes`