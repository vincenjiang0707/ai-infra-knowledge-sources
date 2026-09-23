# pytorch-ecosystem-landscape-q3-update

source: https://pytorch.org/blog/pytorch-ecosystem-landscape-q3-update/

The PyTorch Ecosystem Working Group is happy to welcome 10 new projects to the PyTorch Ecosystem Landscape including Perforated, AReaL, TorchJD, RLinf, Miles, SMG, FiftyOne, TokenSpeed, VisualTorch, and TorchSurv. The [PyTorch Ecosystem Landscape](https://landscape.pytorch.org/) is a map of the innovative open source AI projects that extend, integrate with, or build upon PyTorch. Welcome to the newest PyTorch Ecosystem Landscape projects!

## New Additions to the PyTorch Ecosystem

### Perforated

Perforated is a data-efficiency library for PyTorch that improves model performance by adding neuron-specific reinforcement learning signals during training. Originally inspired by a breakthrough in neuroscience research, Perforated applies a lightweight modification to backpropagation. This library helps models extract more value from available training data, enabling ML teams to reach target performance with fewer labeled examples and no changes to core model architecture. While broadly applicable across machine learning, Perforated has been most extensively validated on edge AI and computer vision workloads. ML teams that have adopted Perforated reduced error by 70% with existing data, meeting deployment criteria while truncating painful data collection and labeling.

Implemented entirely in Python using standard PyTorch functionality, Perforated is proud to be officially welcomed to the PyTorch ecosystem. Teams can evaluate Perforated against their current models and benchmarks with minimal integration effort, making it easy to assess the impact of improved data efficiency within established development pipelines. We look forward to working with the PyTorch community to advance practical approaches for training higher-performing models.

Learn more at [perforatedai.com](http://perforatedai.com). Find us on [Github](https://github.com/PerforatedAI/PerforatedAI). Join the [Perforated Community Slack](https://join.slack.com/t/perforatedcommunity/shared_invite/zt-469gt412a-rDFGRW1H5eo0mwAf5rrl8Q)

### AReaL

AReaL is an open source, modular RL infrastructure that bridges foundation model training with modern LLM/VLM-based agent applications. Built on a fully asynchronous RL training paradigm, AReaL enables seamless building, deployment, evaluation, and fine tuning of agents through standardized data and execution interfaces. Black-box or online agentic systems can be incorporated into the full RL training loop with minimal integration overhead and no intrusive code changes.

AReaL decomposes RL into independent, composable services, enabling flexible scaling, fault tolerance, and independent optimization of system components. This design also allows broad integration with diverse training and inference backends, including vLLM, SGLang, custom PyTorch-native 5D parallel engines, and other projects within the PyTorch ecosystem. Rather than introducing new components, AReaL focuses on connecting existing ecosystem pieces into a practical, end-to-end loop that supports the full lifecycle of an agentic system – from development to continuous evolution.

Learn more about [AReaL](https://github.com/inclusionAI/AReaL).

### TorchJD

TorchJD is a library to train neural networks with multiple losses. Two main classes of methods are supported:

- scalarization: combine the losses into a single scalar loss, and minimize it with a gradient-based optimizer.
- Jacobian Descent (JD): compute the Jacobian of the vector of losses (one gradient per loss), and aggregate it into a common update direction to feed to the optimizer.

There is a key advantage to Jacobian descent: with the proper aggregation method, the parameter update will decrease all losses simultaneously. In some cases though (e.g. very aligned gradients), scalarization may be enough. Our goal is to provide a comprehensive collection of gradient-based multi-objective optimization methods, making it easy both for experts to compare approaches and for newcomers to start solving multi-loss problems without requiring deep expertise in the field.

We’re joining the PyTorch ecosystem in the hope of gathering a larger community of users and contributors. We have many ideas for the future of TorchJD, and we’re looking forward to building them together with the community as we continue working toward making TorchJD the ideal library for training models with multiple losses.

Learn more about [TorchJD](https://github.com/SimplexLab/TorchJD) or join the [Discord community](https://discord.com/invite/76KkRnb3nk).

### RLinf

RLinf is an open source reinforcement learning framework for embodied and agentic AI, built for a world where models are increasingly trained through complex real-world interactions across robots and sensors, simulators, tools, web environments, code, and multi-agent workflows. RLinf connects these interactive feedback loops with scalable training, offering standard and reusable building blocks for rollout, reward computation, environment execution, and learning, without revealing the intricate details of managing heterogeneous hardware and complex environments. Together with push-button recipes for reproducing state-of-the-art RL algorithms, RLinf helps accelerate the advancement of reinforcement learning in embodied and agentic systems.

As part of the PyTorch ecosystem, RLinf brings a real-world perspective to scalable RL: PyTorch users can prototype with familiar model code while RLinf handles the coordination between learning, acting, sensing, evaluating, and scaling across heterogeneous hardware. By making robots and GPUs first-class citizens in the same workflow, RLinf aims to help the ecosystem push post-training beyond isolated model loops toward reproducible, extensible systems that learn through interaction. Learn more at [RLinf](http://github.com/RLinf/RLinf).

### Miles

Miles is an open source post-training framework for large-scale models, built and maintained by RadixArk. It targets the scale at which post-training actually runs: frontier scale open MoEs, multi-node clusters, and long-running jobs that have to stay up. Miles has deep SGLang integration and first-class support for new model architectures and hardware platforms as they land, along with production capabilities including LoRA, TITO, and low-precision training. It is customizable rather than prescriptive, so teams can modify the training loop, swap components, and adapt algorithms to their own recipes instead of working around the framework.

Miles is already used by research labs and industry teams to post-train open models at that scale. RL post-training is where PyTorch-native training meets high-throughput inference, and Miles is built to connect the two. We are joining the PyTorch Ecosystem Landscape to develop that path in the open, alongside the rest of the PyTorch community.

Learn more about [Miles](https://github.com/radixark/miles).

### SMG

SMG (Shepherd Model Gateway) is an engine-agnostic, high-performance model-routing gateway for large-scale LLM deployments. Written in Rust, SMG sits in front of self-hosted inference engines — vLLM, TensorRT-LLM, TokenSpeed, SGLang, MLX — and cloud providers, unifying them behind a single OpenAI-compatible endpoint. Its cache-aware routing tracks each worker’s KV-cache state in radix trees to maximize prefix reuse and GPU utilization, while a native streaming gRPC pipeline supports prefill/decode disaggregation and data-parallel-aware routing. SMG adds enterprise-grade controls — priority admission scheduling, multi-tenancy, API-key auth with OIDC, WebAssembly plugins, and self-hosted chat history — along with 90+ Prometheus metrics and OpenTelemetry tracing. We’re excited to join the PyTorch Ecosystem and to keep building the serving layer for open source models alongside the community.

Learn more about [SMG](https://lightseek.org/smg/).

### FiftyOne

FiftyOne is the multimodal data platform for physical AI. It helps developers build better models by indexing multimodal data for search, curation, annotation, and model evaluation.That data spans images, video, and sensor streams like LiDAR and radar. FiftyOne gives ML teams the tools to find the failure modes, data quality issues, and edge cases that improve model performance, from initial dataset exploration through production model debugging.

FiftyOne integrates natively with PyTorch across the full development loop. Teams can load pre-trained models directly from PyTorch Hub for inference, embeddings, and evaluation, and they can use FiftyOne datasets inside PyTorch training pipelines without maintaining separate dataset definitions. Thousands of teams already work this way: they train models in PyTorch and use FiftyOne to understand, curate, and improve the data those models learn from. Joining the PyTorch ecosystem allows us to make that workflow even better. As physical AI moves from research to production, we look forward to collaborating with the PyTorch community on the data tooling those systems depend on.

Learn more about [FiftyOne](https://voxel51.com/fiftyone).

### TokenSpeed

TokenSpeed is an open source LLM inference engine and the first to separate the control plane from the execution plane. The control plane is implemented in C++ as a finite-state machine, using the type system to enforce safe resource management, including request lifecycles and KV cache state, at compile time rather than runtime. The execution plane is implemented in Python, enabling fast iteration and lowering the cognitive load for researchers and engineers. This architecture combines strong correctness guarantees in the core scheduling system with the development velocity of a high-level execution layer.

TokenSpeed also treats kernels as a first-class, modular subsystem, separating them from the core engine through a portable public API, centralized registry and selection model, and an extensible plugin mechanism for heterogeneous accelerators. We’re joining the PyTorch Ecosystem to work with the broader community on building high-performance, extensible inference infrastructure for open source models. By making both the scheduler and kernel layers modular and extensible, TokenSpeed aims to make it easier to support new models, hardware platforms, and optimizations in production inference systems.

Learn more about [TokenSpeed](https://github.com/lightseekorg/tokenspeed).

### VisualTorch

VisualTorch is an open source PyTorch model visualization library designed to help researchers and engineers create publication-ready diagrams of neural network architectures. It traces an actual forward pass, so branching architectures and custom forward logic are all captured automatically. It renders in multiple visual styles, including animated GIF reveals that build a model’s structure up layer by layer.

VisualTorch has already been used in published research, including work in Nature, IEEE, Elsevier, and MDPI journals. Joining the PyTorch Ecosystem Landscape puts VisualTorch in front of more PyTorch researchers and engineers who need a reliable way to visualize and communicate their models, and connects the project more directly with the broader PyTorch community as it continues to grow.

Learn more about [VisualTorch](https://visualtorch.readthedocs.io/en/latest/).

### TorchSurv

TorchSurv is a lightweight, PyTorch-native toolkit developed through a cross-institution research collaboration spanning industry, regulatory science, and academia, with a simple goal: bring survival analysis modeling directly into PyTorch. By keeping the package focused, lightweight, and well-tested, TorchSurv gives researchers a reliable tool they need to build, evaluate, and extend deep survival models without introducing a separate framework.

TorchSurv provides fully differentiable survival losses, including Cox proportional hazards and Weibull AFT, alongside evaluation tools such as the concordance index, time-dependent AUC, and Brier score, all designed to work with standard PyTorch training loops and arbitrary neural network architectures.

Since its release, TorchSurv has gained traction across the research community, with its use in published studies spanning oncology, medical imaging, and multimodal AI, including work presented at NeurIPS and published in Nature npj Digital Medicine. TorchSurv has also been published in the Journal of Open Source Software and is included in the[ FDA’s Regulatory Science Tools Catalog](https://cdrh-rst.fda.gov/torchsurv-deep-learning-tools-survival-analysis).

Learn more about [TorchSurv.](https://opensource.nibr.com/torchsurv/index.html)

## How to Join the PyTorch Ecosystem Landscape

If you’re developing a project that supports the PyTorch community, you’re welcome to [apply for inclusion in the Ecosystem Landscape](https://pytorch.org/join-ecosystem/). Please review the [PyTorch Ecosystem Landscape Review Process](https://github.com/pytorch-fdn/tac/blob/main/docs/governance/PyTorch_Ecosystem_Process.md) to ensure that you meet the minimum expectations before applying.
