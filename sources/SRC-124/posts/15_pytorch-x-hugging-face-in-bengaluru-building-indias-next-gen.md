# pytorch-x-hugging-face-in-bengaluru-building-indias-next-generation-of-ml-systems-contributors

source: https://pytorch.org/blog/pytorch-x-hugging-face-in-bengaluru-building-indias-next-generation-of-ml-systems-contributors/

### Featured projects

### TL;DR

More than 170 students, engineers, researchers, and open-source contributors gathered in Bengaluru for a technical evening hosted by Red Hat and Hugging Face around PyTorch, large-scale inference, reinforcement learning environments, distributed training, and next-generation communication primitives. With three speakers from Hugging Face and two from the Red Hat PyTorch engineering team, the event was less a general AI meetup than a working session on the infrastructure, abstractions, and systems ideas shaping the future of the open ML stack.

What stood out most was not only the technical range of the talks, but the shared conviction behind them. India has no shortage of talent using AI and ML systems. The deeper opportunity now is to help more students and practitioners become builders and maintainers of those systems: the people shaping profilers, runtimes, training abstractions, RL tooling, kernels, and distributed communication layers that the rest of the ecosystem depends on.

## Setting the Tone: From AI Users to AI Infrastructure Builders

[Sudhir Dharanendraiah](https://www.linkedin.com/in/sudhir-dharanendraiah-80a0867/) opened the evening by framing a challenge that resonated across the room: India should not remain merely a large consumer base for AI and ML technologies. It has the talent, the research energy, and the engineering maturity to become a serious contributor to the core software stack itself.

That framing mattered. It shifted the event away from product demos and toward systems thinking. The conversation was not just about how to call an API or fine-tune a model, but about how the underlying machinery works: what makes inference efficient, what makes reinforcement learning trainable at scale, what makes distributed training composable rather than fragile, and what has to change in communication libraries as clusters become larger and more heterogeneous.

For students, early-career engineers, and startup teams in the room, this was an important signal. The next wave of innovation in AI will not belong only to those consuming models. It will also belong to those improving the compiler paths, the kernel libraries, the serving engines, the reward frameworks, and the distributed systems that make modern ML viable in production.

## Profiling in PyTorch: Making Performance Visible

[Aritra Roy Gosthipaty](https://www.linkedin.com/in/arig23498/) from Hugging Face opened the technical program with a practical talk on profiling in PyTorch built around a simple but durable principle: what you cannot profile, you cannot optimize

Rather than treating performance as a vague outcome, the session broke profiling into a repeatable workflow. Aritra showed how to annotate regions of interest with `torch.profiler.record_function`, wrap execution with `torch.profiler.profile`, and use schedules to separate wait, warmup, and active collection phases. From there, he walked through exporting traces, generating aggregate tables, and reading them well enough to distinguish between CPU overhead and actual GPU work.

One particularly useful thread in the talk was the idea of being “overhead bound.” Small workloads can easily create the illusion that GPU acceleration is underperforming, when in reality the CPU-side launch and orchestration costs dominate the run. By scaling the workload up and comparing how much time is actually spent on CUDA kernels, the session illustrated a lesson that every practitioner eventually learns the hard way: not every slowdown is a model problem, and not every optimization starts in the model code.

For an audience full of people building or debugging real systems, this was a strong starting point. Profiling is often the difference between disciplined optimization and superstition.

Slides can be found [here](https://drive.google.com/file/d/11ZAxSbV6sB1nrEstA-dxS5xrLNTRhqDB/view?usp=sharing). More reading materials can be found [here](https://huggingface.co/blog/torch-profiler).

## SGLang, Transformers, and Kernels: The New Shape of Inference

The next Hugging Face talk by [Adarsh](https://www.linkedin.com/in/adarshxs/) focused on modern LLM inference through the lens of SGLang, the Transformers backend, and the emerging kernels ecosystem. The core message was simple and timely: single-user demos are easy; serving thousands of concurrent requests efficiently is where systems design begins.

The talk unpacked why inference is structurally difficult in large language models. Prefill is compute-bound and highly parallel, while decode is sequential, memory-sensitive, and dominated by the cost of repeatedly interacting with KV cache. From there, the session introduced SGLang as a high-performance serving framework whose design choices are centered on that reality.

A major concept in the presentation was RadixAttention. Instead of discarding KV cache state once a request is complete, SGLang keeps previously seen prefixes in a radix-tree-based cache with LRU behavior. That design is especially compelling in workloads with shared prompts, repeated prefixes, or high request concurrency, because it turns repeated structure in user traffic into an actual systems advantage.

The talk also highlighted a productive division of labor between Hugging Face Transformers and serving engines like SGLang. Transformers remains the source of truth for model definitions, configuration parsing, tokenizers, templates, and weight formats. SGLang then builds the fast path around that world: scheduling, continuous batching, attention backends, and scalable serving behavior. In practical terms, this lowers the barrier to serving the long tail of Hub models without requiring every one of them to be hand-ported into a bespoke runtime first.

The final segment on Hugging Face Kernels widened the picture further. As custom operators and accelerator-specific kernels become more central to ML performance, build fragmentation has become a real problem. Different toolchains, backend combinations, and compatibility constraints often make kernel development harder to share than it should be. The kernels effort presented a path toward more reproducible builds, cleaner packaging, better PyTorch compatibility, and easier community distribution.

Together, these ideas showed how inference is evolving: not as a single monolithic stack, but as a layered collaboration between model definitions, serving runtimes, compiler-friendly execution paths, and reusable kernel infrastructure. Slides can be found [here](https://drive.google.com/file/d/14J1SVW70qNCtPfJzjTGd2aCeXlcydD_J/view?usp=sharing).

## RL Environments 101: Why the Next Scaling Axis Is the Environment

[Adithya S Kolavi](https://www.linkedin.com/in/adithya-s-kolavi/)’s session on RL environments brought the post-training story into focus. The talk traced a familiar arc from pretraining to supervised fine-tuning to RLHF, and then to the current moment in which programmatically verifiable rewards are becoming central to how frontier models are improved.

The key insight of the talk was that once a task can be graded by a program, it can become an environment in which a model learns. That shift sounds abstract, but the presentation made it concrete. An RL environment was described not as a black box, but as a structured combination of tasks, state, tools, observations, reward logic, execution backend, and episode control. In other words, the environment is the training substrate that determines what the model can try, what it can observe, and how success is measured.

This framing helps explain why reinforcement learning for LLMs is both powerful and difficult. Classical RL environments standardized interaction for control problems years ago, but agentic LLM training introduces many more moving parts. A model may need tools, sandboxes, datasets, prompts, verifiers, and multi-turn state. Standardizing that complexity is the difference between one-off experiments and scalable training infrastructure.

That is where [OpenEnv](https://github.com/huggingface/OpenEnv) entered the discussion. Presented as a common shape for LLM environments, OpenEnv extends the spirit of Gym-style APIs into the post-training era. The talk walked through how environments can expose tools through MCP, serve tasks, embed reward rubrics directly, and then be plugged into training libraries such as TRL with relatively little glue code. This is important because it converts environment-building from an ad hoc engineering exercise into something composable and shareable.

The later sections of the talk pushed on the ecosystem implication: if better environments lead to better models, then generating many high-quality environments becomes a strategic advantage. Coding tasks are especially attractive because they are verifiable, deterministic, and economically valuable. That makes repositories, tests, issues, and execution sandboxes a rich source of training problems. The introduction of `Repo2RLEnv` captured exactly that direction: turning public repositories into scalable, verifiable RL environments.

This was one of the most energizing talks of the evening because it gave students and practitioners a tangible frontier to contribute to. Not everyone will build a foundation model, but many can help create the environments, verifiers, tools, and benchmarks that make model improvement more grounded in the real world. Slides can be found [here](https://drive.google.com/file/d/1i4Th8dGvWWQ8SSbdeGoSlzgR1yjddog3/view?usp=drive_link).

## Scaling Up, One Dimension at a Time

[Mansi Agarwal](https://www.linkedin.com/in/mansi-agarwal-a72bbab2/) from the Red Hat PyTorch engineering team brought the audience into the heart of modern distributed training with a talk on DeviceMesh, DTensor, and FSDP2.

The talk began by naming a pain point that anyone who has worked on large training jobs will recognize: combining different forms of parallelism has historically required too much manual plumbing. Data parallelism, tensor parallelism, and pipeline parallelism often came with separate APIs, separate group management, and separate failure modes. Extending a training stack from one dimension of parallelism to two or three could easily mean rewriting the surrounding logic instead of simply scaling the system.

The promise of the newer PyTorch abstractions, as Mansi argued, is composability. DeviceMesh lets engineers describe a cluster as an n-dimensional topology. DTensor makes tensors aware of how they are distributed across that topology. FSDP2 then rebuilds sharded data parallelism on top of those primitives, turning sharding into an in-place transform rather than a special wrapper that breaks model ergonomics.

This matters because it changes the developer experience as much as the runtime behavior. Instead of hand-crafting process groups and injecting custom communication into model code, engineers can reason in terms of mesh dimensions and placement rules. Adding tensor parallelism, pipeline parallelism, or context parallelism starts to look more like extending a grid than rewriting a training stack from scratch.

The session also did not hide the trade-offs. DTensor’s eager-mode overhead, incomplete operator coverage, and the limits of greedy sharding propagation are real constraints. But that honesty made the overall message stronger: composability in distributed training is no longer a research dream or framework marketing line. It is becoming a practical design direction in PyTorch, and one that will matter increasingly as model sizes and hardware topologies continue to grow.

For many attendees, this talk was a window into a level of systems design they may not encounter in day-to-day model usage, but absolutely will encounter if they choose to contribute to the core stack. Slides can be found [here](https://drive.google.com/file/d/1IeZ4VxjP-sl4AnhMfrs-VRVg9Y58DYdW/view?usp=sharing)

## Zero-Copy GPU-to-GPU Communication in PyTorch

[Arkadip Maitra](https://www.linkedin.com/in/arkadip-maitra/) closed the evening with a deep systems talk on zero-copy GPU-to-GPU communication in PyTorch, moving the discussion down to the communication substrate that underpins large-scale training.

The talk began with `c10d`, PyTorch’s default distributed communication layer, and why it served the ecosystem well for a long time. It offered a general-purpose abstraction across CPU and GPU backends and fit the era in which most distributed workloads were bulk-synchronous, collective-heavy, and comparatively modest in scale.

But the assumptions around communication are changing. Network interfaces have evolved, GPUDirect RDMA has matured, NVLink paths have strengthened, and training fabrics have become more topology-aware and specialized. As cluster sizes and communication patterns change, the cost of intermediate copies and thread overhead becomes more visible.

That is why the zero-copy path discussed in the talk is so important. By avoiding unnecessary copy steps, PyTorch can reduce thread-block consumption and deliver meaningful communication speedups, especially in message-size regimes that matter in real training and serving systems. The reported gains in the presentation, including reductions in copy tax and faster medium-message communication, point to a broader theme: scaling ML systems is increasingly a matter of shaving inefficiencies out of the invisible layers below the training loop.

This was a fitting close to the event because it reinforced a recurring lesson from the evening: high-level model performance often depends on low-level engineering choices that most users never see. Helping more practitioners understand those layers is part of what matures an ecosystem. The slides for this can be found [here](https://drive.google.com/file/d/1rdtIDEUM-pX73TQkONHLmHnCQaVWvKJT/view?usp=drive_link)

## Why This Collaboration Matters

What made the event distinctive was not just that it featured speakers from both Red Hat and Hugging Face, but that the collaboration surfaced a coherent view of the stack.

Hugging Face brought perspectives from profiling, inference infrastructure, and RL post-training workflows. Red Hat’s PyTorch engineering team brought perspectives from distributed training internals and communication primitives. Put together, the talks formed a connected story: measure the system well, serve models efficiently, build stronger training environments, scale training compositionally, and keep improving the communication substrate underneath it all.

For Indian students and AI practitioners, that kind of ecosystem view is invaluable. It shortens the distance between “using AI” and “contributing to AI systems.” It shows that open-source contribution is not confined to model releases or application demos. There is meaningful work to be done in profilers, kernels, runtime backends, reward infrastructure, checkpointing, sharding semantics, and distributed communication libraries. That is precisely the kind of work that can keep practitioners not only engaged and ahead of the curve, but motivated to help shape what comes next.

At a time when many people are asking how India can participate more deeply in the future of AI, this event offered a credible answer: by joining the communities that build the core layers, and by treating technical collaboration as a way to widen the pipeline from student curiosity to serious open-source stewardship.

## Looking Ahead

With more than 170 attendees, the evening made one thing clear: there is real appetite in India for technically serious, systems-oriented ML community events. The energy in the room suggested that students want more than introductions, practitioners want more than surface-level best practices, and the ecosystem is ready for conversations that connect model behavior to the infrastructure beneath it.

If this event is any indication, collaborations between Red Hat, Hugging Face, and the wider PyTorch community can do more than host good meetups. They can help build a local culture of contribution around the open ML stack itself, one where the next generation of innovators does not simply adopt tools built elsewhere, but helps design, maintain, and improve them for everyone.
