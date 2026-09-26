source: https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/fine-tuning/index.html

# Use ROCm for fine-tuning LLMs[#](https://rocm.docs.amd.com#use-rocm-for-fine-tuning-llms)

2026-02-19

1 min read time

Fine-tuning is an essential technique in machine learning, where a pre-trained model, typically trained on a large-scale dataset, is further refined to achieve better performance and adapt to a particular task or dataset of interest.

With AMD GPUs, the fine-tuning process benefits from the parallel processing capabilities and efficient resource management, ultimately leading to improved performance and faster model adaptation to the target domain.

The ROCm™ software platform helps you optimize this fine-tuning process by supporting various optimization techniques tailored for AMD GPUs. It empowers the fine-tuning of large language models, making them accessible and efficient for specialized tasks. ROCm supports the broader AI ecosystem to ensure seamless integration with open frameworks, models, and tools.

Throughout the following topics, this guide discusses the goals and [challenges of fine-tuning a large language
model](https://rocm.docs.amd.com/overview.html#fine-tuning-llms-concept-challenge) like Llama 2. In the
sections that follow, you’ll find practical guides on libraries and tools to accelerate your fine-tuning.

The AI Developer Hub contains [AMD ROCm tutorials](https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/) for
training, fine-tuning, and inference. It leverages popular machine learning frameworks on AMD GPUs.

[Fine-tuning and inference](https://rocm.docs.amd.com/fine-tuning-and-inference.html)using a[single-accelerator](https://rocm.docs.amd.com/single-gpu-fine-tuning-and-inference.html)or[multi-accelerator](https://rocm.docs.amd.com/multi-gpu-fine-tuning-and-inference.html)system.