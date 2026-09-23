# AWS Neuron

source: https://awsdocs-neuron.readthedocs-hosted.com/en/latest/

# AWS Neuron Documentation[#](https://awsdocs-neuron.readthedocs-hosted.com#aws-neuron-documentation)

[AWS Neuron](https://awsdocs-neuron.readthedocs-hosted.com/about-neuron/what-is-neuron.html#what-is-neuron) is the software development kit for deep learning and generative AI on [AWS Inferentia](https://aws.amazon.com/ai/machine-learning/inferentia/) and [AWS Trainium](https://aws.amazon.com/ai/machine-learning/trainium/) instances. Neuron supports multiple development paths: serving large language models with vLLM, training and inference with PyTorch and JAX, authoring custom kernels with NKI, and direct use of the Neuron Graph Compiler and Runtime.

## Who Neuron is for[#](https://awsdocs-neuron.readthedocs-hosted.com#who-neuron-is-for)

**ML engineers deploying production models**— Deploy prepared[Neuron Deep Learning AMIs (DLAMIs)](https://awsdocs-neuron.readthedocs-hosted.com/deploy/environments/dlami.html)and[Deep Learning Containers (DLCs)](https://awsdocs-neuron.readthedocs-hosted.com/deploy/environments/index.html)on Amazon EC2 Trainium and Inferentia instances. Start with the[DLAMI setup guide](https://awsdocs-neuron.readthedocs-hosted.com/deploy/environments/dlami.html)or the[DLC quickstart](https://awsdocs-neuron.readthedocs-hosted.com/deploy/environments/quickstart-deploy-dlc.html).**Serving LLMs**— Use vLLM Neuron to serve open-source LLMs with minimal code changes. Start with the[online serving quickstart](https://awsdocs-neuron.readthedocs-hosted.com/vllm-neuron/docs/getting-started/quickstart-online-serving.html)or[offline serving quickstart](https://awsdocs-neuron.readthedocs-hosted.com/vllm-neuron/docs/getting-started/quickstart-offline-serving.html).

**ML researchers and model developers**— Use native PyTorch on Trainium with eager mode,`torch.compile`

, and standard distributed APIs. Start with[Native PyTorch on Neuron](https://awsdocs-neuron.readthedocs-hosted.com/frameworks/torch/pytorch-native-overview.html).**Performance engineers optimizing kernels**— Use NKI to write custom kernels with direct NeuronCore access, or pick from the NKI Library’s pre-optimized kernels. Start with the[NKI quickstart](https://awsdocs-neuron.readthedocs-hosted.com/nki/get-started/quickstart-implement-run-kernel.html)and[NKI Library](https://awsdocs-neuron.readthedocs-hosted.com/nki/library/index.html).

## Start here[#](https://awsdocs-neuron.readthedocs-hosted.com#start-here)

Pick the task that matches what you want to do.

Launch a Trainium or Inferentia EC2 instance with a pre-configured **Neuron Deep Learning AMI (DLAMI)** and PyTorch. The DLAMI bundles the Neuron SDK, framework virtual environments (PyTorch, JAX, vLLM), and the system tools — no manual install required. See [Install PyTorch via Deep Learning AMI](https://awsdocs-neuron.readthedocs-hosted.com/setup/pytorch/dlami.html) and get started!

## Neuron SDK Organization[#](https://awsdocs-neuron.readthedocs-hosted.com#neuron-sdk-organization)

The Neuron SDK includes:

**Frameworks**— Native PyTorch on Trainium (TorchNeuron), PyTorch NeuronX (`torch-neuronx`

), and JAX NeuronX.**Serving integrations**— vLLM Neuron and the earlier vLLM integration through NxD Inference, both for OpenAI-compatible LLM serving.**NeuronX Distributed (NxD) libraries**— PyTorch libraries for distributed training and inference, including NxD Training, NxD Inference, and NxD Core.**Neuron Kernel Interface (NKI)**— Python programming interface for custom kernels on NeuronCores, plus the NKI Library of pre-optimized kernels.**Neuron Graph Compiler**(`neuronx-cc`

) — Compiles model graphs and NKI kernels into Neuron Executable File Format (NEFF) files.**Neuron Runtime**— Loads NEFFs and executes them on NeuronCores, handling device allocation, memory management, and collective communications.**Developer tools**— Neuron Explorer and the Neuron system tools for profiling and debugging across every component.

**Frameworks and serving**

Write training and inference code with PyTorch or JAX. Serve LLMs with vLLM Neuron.

**Neuron Developer Tools and Agent Support**

Use Neuron Explorer to profile and optimize your kernels. Use our Agentic Development skills to accelerate your kernel development.

**NKI — Neuron Kernel Interface**

Programming interface for custom kernels on NeuronCores. Used by the modern framework and serving integrations. Ships with a library of pre-optimized kernels.

**Neuron Graph Compiler and Runtime**

The compiler (`neuronx-cc`

) transforms model graphs into NEFF files. The runtime loads NEFFs and executes them on NeuronCores, handling device allocation, memory management, and collective communications. Both framework graphs and NKI kernels compile to NEFF.

## Learn more[#](https://awsdocs-neuron.readthedocs-hosted.com#learn-more)

*AWS and the AWS logo are trademarks of Amazon Web Services, Inc. or its affiliates. All rights reserved.*