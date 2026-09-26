# [Issue #73] [Roadmap] Integration with Open-Source Frameworks

source: https://github.com/ScalingIntelligence/KernelBench/issues/73
state: open | updated: 2026-04-15T14:11:32Z
labels: enhancement, help wanted

## 正文

Here is our plan (thanks @ethanboneh for researching and writing this up) to integrate / test KernelBench with a variety of RL and search environments **this fall**. 
We have a few folks leading this (@ethanboneh on RL) and (@pythonomar22 on search). 
We will link detailed issues and PRs, but we also welcome community contributions to these efforts!

KernelBench could also serve as an **environment to conduct Reinforcement Learning or Evolutionary Search** as we provide ground-truth signals that could be used as verifiable rewards. The community and us have been building / have integrated RL environments with several open-source environment hubs. We plan to add support for KernelBench across these frameworks/environments to  facilitate future RL-centric research on KernelBench. Concretely, for frameworks already including a KernelBench environment, we will verify correctness and run baseline RL/evolutionary experiments.

### Prime Intellect Env Hub
Authors: [Prime Intellect](https://www.primeintellect.ai/) and open-source contributors  
KernelBench Usage: Some datasets pull directly from/augment KernelBench problems  
Description: Prime Intellect supports open-source RL environments through its [verifiers](https://verifiers.readthedocs.io/en/latest/) library. It can be connected to sandboxed environments to support external tool calling.

Relevant environments:  
KernelBench  
Authors: Fido Wang  
Description: Single-turn RL environment which builds prompts from reference KernelBench code, evaluates on a Modal GPU, and computes performance metrics.  
Link: [kernelbench—sandboxed (Modal) environment](https://app.primeintellect.ai/dashboard/environments/popfido/kernelbench) 

PMPP  
Authors: @sinatras on Prime Intellect  
Description: Programming Massively Parallel Processors is a classic reference text for parallel computing, and contains many practice coding problems. This environment specifically contains 53 CUDA kernel tasks. It determines rewards based on performance on a user’s GPU.  
Link: [pmpp (textbook problems) | Prime Intellect](https://app.primeintellect.ai/dashboard/environments/sinatras/pmpp)

BackendBench  
Authors: Prime Intellect Research  
Description: BackendBench is an evaluation suite for testing how well LLMs and humans can write PyTorch backends. It lets developers add custom kernels in an organized directory structure and override PyTorch's operators at runtime. This environment lets you measure performance on a local GPU or Modal GPU.  
Link: [BackendBench (another kernel benchmark)](https://app.primeintellect.ai/dashboard/environments/primeintellect/backend-bench)

### Atropos by Nous Research
Authors: [Nous Research](https://nousresearch.com/)  
KernelBench Usage: KernelBench data used and incorporated into a specific environment  
Description: Atropos is an RL environment microservice framework with many sample environments, including one using KernelBench.  
Links: [Github](https://github.com/NousResearch/atropos), [KernelBench Environment](https://github.com/NousResearch/atropos/tree/main/environments/kernelbench_env)

### PyTorch Forge and OpenEnv
Authors: PyTorch  
KernelBench Usage: Plan to build a KernelBench environment on this framework.  
Description: This is PyTorch’s new RL environments hub. The repo contains a gym-style environment, with utilities to automate spinning up Docker containers to create isolated environments. Support for standard RL tools (TRL, SkyRL, etc) is currently being implemented. While there are some demo environments, there is no main hub for environments built with it right now.  
Link: [OpenEnv Repo](https://github.com/meta-pytorch/OpenEnv), [OpenEnv HuggingFace](https://huggingface.co/openenv)

### Marin Project 
Authors: Stanford CRFM  
KernelBench Usage: Plan to build a KernelBench environment on this framework.  
Description: This is an environment for running open experiments on LLMs. It includes some pretrained foundation models, as well as a reproducible database of experiments to run. We hope to add support for running experiments on KernelBench with Marin’s framework to create reproducible experiments for different RL/evolutionary algorithms.  
Link: [Marin Project](https://marin.community/), [GitHub](https://github.com/marin-community/marin)

### OpenEvolve
Authors: Community Open-Source Project (by [Codelion](https://github.com/codelion))  
KernelBench Usage: Plan to build a KernelBench environment on this framework.  
Description: Open Evolve is the open-source implementation of AlphaEvolve. [AlphaEvolve](https://arxiv.org/abs/2506.13131) begins with an initial algorithm, evaluation function, and guide LLM which proposes changes to the algorithm. It then iteratively applies those changes, measures their performance, and keeps an archive of the  top performing algorithms. This has allowed it to discover novel algorithms across several domains, including within GPU kernels.  
Link: [GitHub](https://github.com/codelion/openevolve)

MLX Kernel Discovery Example:   
Description: OpenEvolve has specifically been applied to [MLX](https://github.com/ml-explore/mlx) kernel generation ([Blog](https://huggingface.co/blog/codelion/openevolve-gpu-kernel-discovery)). MLX is Apple’s framework for ML on Apple Silicon, closely following PyTorch syntax. OpenEvolve was able to discover a novel softmax algorithm and better exploit SIMD operations, as discussed in the blog.  
Link: [GitHub](https://github.com/codelion/openevolve/tree/main/examples/mlx_metal_kernel_opt)

## 评论 (1)

### arielge · 2026-04-15

FYI, worked on adding KernelBench integration (evaluation + kernel database) to open-source code evolution frameworks:
* SkyDiscover - https://github.com/skydiscover-ai/skydiscover/pull/63
* K-Search - https://github.com/caoshiyi/K-Search/pull/5
