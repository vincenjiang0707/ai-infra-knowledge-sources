# building-an-analysis-ai-agent-for-industrial-alarm-management-with-nvidia-nemotron

source: https://developer.nvidia.com/blog/building-an-analysis-ai-agent-for-industrial-alarm-management-with-nvidia-nemotron/

Industrial machinery generates more alarms than technicians can triage. For each important alarm requiring follow-up, the technician pulls historical context, determines the correct procedure, checks whether a specialist signal confirms the failure mode, and writes up a recommendation. This process remains consistent, and is well-suited for an [AI agent](https://www.nvidia.com/en-us/ai/).

This post discusses a per-alarm analysis AI agent built with [NVIDIA NeMo](https://www.nvidia.com/en-us/ai-data-science/products/nemo/) libraries, using [NVIDIA Nemotron](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/) open models for intelligence and the [NVIDIA OpenShell](https://build.nvidia.com/openshell) secure runtime. Given an alarm with its sensor frame, the agent:

- Gathers context (history, playbooks, similar past cases)
- Runs specialist checks (for example, using
[NVIDIA nv-tesseract](https://developer.nvidia.com/blog/advancing-anomaly-detection-for-industry-applications-with-nvidia-nv-tesseract-ad/)for anomaly detection metrics, OCR using[NeMo Retriever](https://developer.nvidia.com/nemo-retriever)for scanned playbooks) - Issues a structured evidence package: observation, root-cause hypothesis, remedy, recommended action

The agent is GPU-accelerated end-to-end and lives behind a single HTTP endpoint. Anything upstream (an in-stream filter, an on-click button in the operator’s UI) calls it the same way. The tools matter as much as the brain.

**Why is industrial and infrastructure per-alarm work challenging?**

Machines are increasingly connected, from cars and trains to elevators and industrial motors. With this interconnection, service personnel and engineering teams face increasing amounts of data available to troubleshoot issues and understand what’s happening in the machine.

At the same time, technical personnel also need to filter and assess the information pushed to them constantly from their SCADA or IoT systems to find the signals that matter. Often there are hundreds of alarms per hour, thousands of sensor readings to consider, and a range of different documentation formats explaining what to do for each of them.

For example, when an alarm is raised, a technician often must go through multiple data sources, tools, and documentation to answer questions such as:

- Has this asset or class hit this alarm before? What was done? What fixed it?
- What does the specific playbook say to do for this error code, factory plant, and location?
- Is the signal real? For a generic alarm alerting of high temperature, is it an anomaly or part of a trend? Is maintenance action going on?

After working through these questions, the technician must then write a recommendation (usually a work order) so that others can act and learn from it.

Altogether, this is an effort-intensive job that requires broad experience and the ability to interact with many different systems. An assistant that addresses the generic steps can therefore accelerate this process substantially. Filtering relevant signals, gathering relevant knowledge, and drafting reusable recommendations frees time, so humans can concentrate on more complex issues and work through the other open events more quickly.

**How does the AI analysis agent help solve these challenges?**

When a human requests context on a specific alarm, the AI analysis agent connects to different systems to gather knowledge, potentially uses specialists for deeper analysis, and ultimately drafts a valid action. The whole agent runs inside a sandbox (Figure 1).

The agent’s job is simple to state and specify:

**In:**One alarm payload, with its sensor frame and asset metadata**Out:**One evidence package (observation, root-cause hypothesis, remedy, recommended action) plus the supporting trace**Latency budget:**Seconds, not minutes; the operator is waiting for this row to turn green, so every step needs to be as fast as possible

To perform the job, the agent needs:

- Instructions on what to do (labeled 1 in Figure 1)
- Intelligence or reasoning capability, which is provided by
[NVIDIA Nemotron](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/)open models (labeled 2 in Figure 1) - The orchestrated tools to interact with other systems (labeled 3-5 in Figure 1)

The instructions are a batch of alarms combined with a prompt formulating the agent goal to send to [Nemotron](https://build.nvidia.com/nvidia/nemotron-3-super-120b-a12b/playground), a family of open models with open weights, training data, and recipes, delivering leading efficiency and accuracy for building specialized AI agents. Specifically, the assistant uses Nemotron 3 Nano for simple orchestration tasks and Nemotron 3 Super for complex reasoning. These models are hosted as optimized NIM containers close to the factory line for low-latency inference or in the cloud.

As instructed by the model, the agent progresses towards its goal. It retrieves information, assesses relevance, filters and analyzes using different tools. To meet the latency budget of the user, it is important that each of these steps is performed as fast as possible.

**What tools does the agent use and how are they accelerated?**

Predominantly, the agent needs to iteratively assemble and reason in a broad context. It therefore has three natural subphases on any given alarm: gather evidence (labeled 3 in Figure 1), run specialist checks (labeled 4 in Figure 1), then generate and validate the action (labeled 5 in Figure 1). Each step uses tools that are accelerated using GPUs using either [CUDA-X Libraries](https://developer.nvidia.com/cuda/cuda-x-libraries) or other specialized models from the Nemotron family.

**Accelerated retrieval of structured information**

By default, the agent retrieves potentially relevant alarms and sensor readings by configuring SQL queries with suitable time-intervals and filters for relevant sensors. These queries typically run against the cleaned inbound stream of recent alarms and sensor frames. For fast responses these frames are aggregated and parsed using [NVIDIA cuDF](https://developer.nvidia.com/topics/ai/data-science/cuda-x-data-science-libraries/cudf), a library that accelerates data handling and filtering on GPUs.

If historical or broader information is required, the agent can use its Text-2-SQL tool to retrieve it from the broader data warehouse. Using [Apache Vanna](https://developer.nvidia.com/blog/accelerating-text-to-sql-inference-on-vanna-with-nvidia-nim-for-faster-analytics/) to manage context on the available tables with a Nemotron model converts questions into queries. For example, “What alarm types were prevalent on assets with a specific serial number group over the last months?” The same approach addresses complex prerequisite questions on the asset hierarchy and sensor topology in terms of parent/child component relationship, typically used for filtering.

**Accelerated RAG with NVIDIA NeMo Retriever**

Much of the relevant information for resolving an alarm is hidden in unstructured data, such as procedure manuals, location-specific playbooks, work-order templates, and operator process instructions. [NVIDIA NeMo Retriever](https://developer.nvidia.com/nemo-retriever) accelerates filtering the relevant information. It orchestrates specialized models like [Nemotron Parse](https://build.nvidia.com/nvidia/nemotron-parse) or [Nemotron RAG](https://huggingface.co/collections/nvidia/nemotron-rag) to accelerate the extraction and indexing of complex information. For more details, see the [NVIDIA AI Blueprint for Retrieval-Augmented Generation](https://build.nvidia.com/nvidia/build-an-enterprise-rag-pipeline).

**Iteratively building resolution knowledge**

Finally, crucial context for the agent is a memory of its own semistructured data—in particular, past remedy tickets and solution strategies. Search in these is accelerated using cuVS. This allows the agent to learn from the past—for example, to answer the question, “Has this signature been seen before, and did the fix work?”

**Specialist analysis**

Often,** **generic alarms (for example, “Temperature High” or “Vibration Spike”) need a specialist’s confirmation in a given context: is the bearing actually failing, or is this a sensor artefact? To accomplish this, domain-specific specialist tools or subagents are deployed alongside the agent.

For example, after retrieving structured sensor timeseries, it may be necessary for the agent to call an analysis agent that performs sampling or a Fourier transform on the data, perform a forecast, or filter for outliers using suitable libraries like [NVIDIA cuFFT](https://docs.nvidia.com/cuda/cufft/), [NV-Tessaract](https://developer.nvidia.com/blog/new-nvidia-nv-tesseract-time-series-models-advance-dataset-processing-and-anomaly-detection/), or[ NVIDIA cuML](https://docs.rapids.ai/api/cuml/stable/).

**Action generation and validation**

Once the information gathering and specialist analysis is done, the Nemotron model iteratively synthesizes the gathered evidence into a structured observation plus root-cause hypothesis plus the remedy plus the recommended action record. After that, the agent tests the output against a policy and confidence gate where it is also scrutinized for safety using [Nemotron 3 Content Safety](https://build.nvidia.com/nvidia/nemotron-3-content-safety). High-confidence and within-policy gets the auto-dispatch flag; low-confidence or out-of-policy escalates to a technician with the evidence preattached.

**Nemotron models provide agent intelligence**

Nemotron models provide intelligence in multiple parts of the agent. They provide the reasoning brain, document parsing in NeMo Retriever, and high-quality embedding for search. They will perform well out of the box when simply using available checkpoints, making a deployment possible in minutes.

Another advantage of using open models is that you can easily tune them to your tasks. For example, using a recipe to fine-tune your Nemotron embedding model to the content of your playbooks and technical field will allow it to retrieve good results even more reliably. In more advanced cases, [fine-tuning](https://docs.nvidia.com/nemo-framework/user-guide/24.07/llms/nemotron/sft.html) will make the reasoning model even more effective to reason on the particular language, industry domain and description used in your alarm context.

Together, this ability to deploy the models anywhere (with a suitable GPU) and to tune them exactly to the agent’s context make Nemotron models the key component of this agent.

## What results does the analysis agent achieve?

The analysis agent described here accelerates every step in providing evidence to the user for alarms. That’s what makes it tractable to call the agent from the user Interface, often a third-party application on an alarm and get an answer in relevant time. To get even more performance out of a given setup, batches of critical events can be sent to the agent for preanalysis automatically. This uses the available capacity and further reduces the alarms that a human otherwise would have to look at or analyze.

## Why are orchestration, security, and agent evolution important?

Tying together the agent with its tools and brain is the orchestration (prompt assembly, tool dispatch, retry, tracing). Also, the agent should learn and improve. By design, it will become more intelligent through the growing “past remedy” knowledge base. However, even with this information increasing, the agent will occasionally select the wrong tools (or select the right tools but pass them bad arguments).

To simplify these tasks, you can use the [NVIDIA NeMo Agent Toolkit](https://docs.nvidia.com/nemo/agent-toolkit/latest/index.html), part of [NVIDIA NeMo](https://docs.nvidia.com/nemo/index.html). It helps expose the agent as a single endpoint, generate traces that can be evaluated with [NeMo Evaluator](https://docs.nvidia.com/nemo/evaluator/latest/), and handle many of those little details that make an agent production ready.

For enterprise deployments like this agent that often work with sensitive data or have access to production-relevant systems, security is key. In particular, it’s necessary to control what actions an agent can perform, what models it can call, and what tools it can use. For any agent, it therefore makes sense to establish a sandbox. NVIDIA OpenShell is a secure runtime for autonomous AI agents and provides sandboxed execution environments that protect your data, credentials, and infrastructure—governed by declarative YAML policies that prevent unauthorized file access, data exfiltration, and uncontrolled network activity.

**Get started building an analysis agent**

If you run machinery at scale, the per-alarm technician work is the agent-shaped part of the job. The process described in this post is what the NVIDIA stack assembles for it: a Nemotron-driven agent, with the OpenShell secure runtime, and GPU-accelerated context and specialist tools, exposed as one HTTP endpoint your existing alarm-management UI or pipeline can call.

You can assemble the solution with NVIDIA Agent Toolkit building blocks:

**NVIDIA AI-Q Blueprint for intelligent agents**: A reference stack that connects, retrieves, and reasons over enterprise data with the same toolchain described above. Start here.**NVIDIA NeMo Agent Toolkit:**The library underneath orchestration. It’s how you author the agent’s tools, trace its calls, and expose it as an HTTP endpoint.**NVIDIA OpenShell**: The runtime for the agent in any deployment where you want gated tool calls and replayable traces.**NVIDIA Nemotron**: The intelligence. Sign up for free developer access on build.nvidia.com and[download the optimized NIM containers](https://build.nvidia.com/nvidia/nemotron-3-nano-30b-a3b)or use the collection of[checkpoints on Hugging Face.](https://huggingface.co/collections/nvidia/nvidia-nemotron-v3)**NVIDIA NeMo Retriever**: A library that transforms enterprise documents into a structured knowledge layer special agents can reason over, delivering grounded, accurate, and fast answers informed by your unique enterprise data.**NVIDIA CUDA-X Libraries**(cuDF, cuVS, cuGraph): Handle the archive, vector, and graph tools.**NVIDIA NeMo Evaluator:**Scores tool-use and answer quality against ground truth; wire it to the NeMo Agent Toolkit trace log on day one.

Ready to get started building your own agent? Following these steps:

- The key components of the Agent require a GPU to run. If you don’t have one available, start with the hosted
[NVIDIA NIM developer endpoints](https://docs.api.nvidia.com/)for Nemotron models and switch to your own later. - Clone the
[NVIDIA AI-Q Blueprint](https://github.com/NVIDIA-AI-Blueprints/aiq)and stand it up against a synthetic alarm stream. - Wire it into the technician’s existing tool first, and build a new UI only if you have to.
- Talk to your NVIDIA account manager about deployment shapes for your sites. Startups can apply to
[NVIDIA Inception](https://www.nvidia.com/en-us/startups/)for credits and support.

This agent is the part of the system that improves in cost and performance as more alarms are put through it.
