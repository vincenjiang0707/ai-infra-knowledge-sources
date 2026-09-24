# from-wafer-out-to-first-token-codifying-supply-chain-expertise-with-nemotron-and-palantir-foundry

source: https://developer.nvidia.com/blog/from-wafer-out-to-first-token-codifying-supply-chain-expertise-with-nemotron-and-palantir-foundry/

NVIDIA has one of the largest and most [complex supply chains](https://www.nvidia.com/en-us/industries/retail/supply-chain-management/) in the world, and its performance is measured from wafer-out to first token. The interval is in two parts. Time-to-rack runs from silicon leaving the fab to an assembled system arriving on a data center floor. Time-to-token covers everything thereafter: power, cooling, networking, and the software stack that makes the infrastructure productive on day one.

[NVIDIA Grace Blackwell NVL72](https://blogs.nvidia.com/blog/blackwell-ai-inference/) platforms draw on millions of parts and thousands of suppliers spread across the globe, and the final system is built by dozens of OEMs and ODMs. Just one compute tray–one of eighteen in a single rack–requires two NVIDIA Grace CPUs, four NVIDIA Blackwell GPUs, and thirty-two HBM3e stacks. The supply chain we created for Vera Rubin is twice as large as Grace Blackwell. CPUs, GPUs, and memory are all critical components, and the availability of each changes from week to week, so the part holding up a build one week may be freely available the next. Each carries its own bill of materials, its own suppliers, and its own lead times. Multiply that by every sub-assembly in the rack, and the result begins to look less like a supply chain and more like a daunting combinatorics problem.

Contract manufacturers cannot start assembly until every component has arrived from one of three pools: parts from NVIDIA directly, parts that NVIDIA stocks on consignment, and parts from suppliers. Ideally, components all arrive at once, but when they don’t, whatever arrived early waits for everything that’s late. NVIDIA runs the clock from the moment a manufacturing site receives material to the moment it leaves as part of a sub-assembly or product, and that metric is known as Time of Ownership (TOO).

With highly dynamic availability, NVIDIA must decide what and how much material to allocate to each manufacturing site. This is known as the critical material allocation problem, and it is manually reworked every week. The allocation runs through the current quarter and the next with the nearest weeks already committed, so each week’s new data mostly changes what happens further out.

This post is primarily concerned with time-to-rack, and compressing it requires four things:

- Real-time visibility to pinpoint critical operational bottlenecks at any moment
- Redundancy where a single failure may otherwise halt production
- Reliability, so upstream production commits hold
- Codified human expertise, so the judgment behind a complex allocation decision becomes persistent knowledge that compounds over time

While the initial three requirements provide the necessary operational baseline, it is the codification of human expertise where the most significant transformation occurs.

## Building a supply chain command center in Palantir Foundry

The NVIDIA supply chain operations team worked with Palantir to create a unified view of every input to a material allocation decision. The NVIDIA team calls this their Digital Supply Chain Intelligence command center, and it surfaces risks, blockers, and other signals that inform those decisions but may previously have remained buried across disjoint data sources.

Under the hood, Palantir Foundry provides the operating context. The Ontology connects materials, manufacturing sites, commits, capacity, allocations, production outputs, and unstructured, qualitative signals into one governed data layer. Composed of objects and links rather than rows and tables, it forms a complete representation of operational reality.

This representation enables allocation planners to simulate and analyze many different scenarios, giving them much broader access to the decision space and laying the groundwork for an AI flywheel that compounds new knowledge and improves performance over time.

## Solving the quantitative side with NVIDIA cuOpt

Allocating material across multiple manufacturing sites starts as a quantitative problem, and the formulation starts with the decision variables: How much of each constrained material goes to which sites and when over the coming period?Around them sits everything that bounds the answer. This includes every manufacturer capable of building a given Blackwell sub-assembly and the throughput each site can absorb once material lands. It also includes the dependency graph of every required part mapped backward through the chain, so the solver knows that a compute tray is blocked by its scarcest input rather than its average one. That binding constraint is not fixed. It shifts between:

- GPU, CPU, and memory from one week to the next
- Inbound timing across all three supply routes
- Commitments already made to customers, which determine what a shortfall at any one site actually costs
- Thousands of variables and constraints resolve into a single weekly allocation.

NVIDIA cuOpt, an open-source library for GPU-accelerated decision optimization, solves this. It draws its inputs from the Ontology and writes the result back as an allocation decision. Allocation is posed as a mixed-integer linear program, and the objective minimizes Time of Ownership (TOO). cuOpt returns more than the allocation itself. It also reports which constraints are binding, so a planner can see that Taiwan capacity, not memory supply, is what held this week’s number down.

Because the solve is fast, planners can also explore the space around the answer. What happens with ten percent less memory this period? What if a new manufacturing site comes online? Planners stop asking the solver for an answer and start asking it what the tradeoffs are.

### Where the math stops

Quantitative optimization doesn’t tell the whole story. NVIDIA and Palantir back-tested historical allocation decisions against what actually happened, and it revealed a human factor that cuOpt wasn’t capturing.

Planners were working from information the solver could not see: emails exchanged with partners that week, severe weather in the forecast for a key region or an ongoing geopolitical event, the transcript from the last supplier debrief call, and years of accumulated expertise. Those inputs feed an instinct about how to allocate material for the coming period, and that instinct is what makes the human experts better than the math.

With that in mind, NVIDIA and Palantir built this workflow around those human experts. It captures the allocation decision, the rationale behind it, the expected result, and the actual outcome. Institutional knowledge becomes explicit, reviewable decision logic, and because that data lives in the Ontology, it serves as the foundation for training an LLM on expert judgment.

## Codifying decision intelligence

We then post-trained an open-weight LLM to apply that same reasoning and make a recommendation. After evaluating [NVIDIA Nemotron](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/) open models, we chose [Nemotron 3.5 Lightning](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4) because it is purpose-built for the execution layer of an agentic workflow. It performs specialized tasks as part of a system of models that also includes larger variants for orchestration and general tasks.

Its mixture-of-experts architecture lends itself to highly efficient inference, and while the model is lightweight at 30 billion parameters and roughly 3 billion active per forward pass, it’s still large enough to learn a focused policy. This footprint makes the post-training loop practical because smaller models learn faster and need far less compute both to train and to deploy than their larger counterparts.

Because Nemotron is open, it can be post-trained inside your own compute boundary. Any organization can run the same flywheel on their own operational data without exposing it externally. The model learns from the signals planners actually use: how much constrained material was offered to a manufacturing site, what the manufacturer committed to produce, what it ultimately produced, and the qualitative operational evidence available at the time of the decision.

The objective is to codify an allocation policy that can assess production risk, recommend an allocation range, identify the factors behind that recommendation, and explain its reasoning to the supply-chain team.

The same record doubles as the evaluation harness. We replay each decision with only what was knowable that day, hide the outcome, and compare the model’s recommendation against both the planner’s call and what actually happened. The primary question that this evaluation answers is: If this model had been running last month, would it have made the right allocation call?

## From Ontology data to a specialized model

The training process starts with operational history in the Palantir Ontology:

**Anonymization:**[NeMo Anonymizer](https://github.com/NVIDIA-NeMo/Anonymizer)removes personally identifiable information and obfuscates sensitive fields before training.**Synthetic data generation:**[NeMo Data Designer](https://github.com/NVIDIA-NeMo/DataDesigner)expands and balances the examples, so the model sees not only routine weeks but also allocation increases, capacity constraints, and disruption scenarios.**Supervised fine-tuning:**[NeMo AutoModel](https://github.com/NVIDIA-NeMo/AutoModel)trains a small set of LoRA adapter parameters while the base weights stay frozen, which cuts training time, memory requirements, and checkpoint size.**Evaluation:**The point-in-time backtest replays the same historical decisions through both the base and fine-tuned models, isolating what post-training added.

Palantir Autopilot manages the lifecycle end to end, launching each job from Ontology data, monitoring the deployed custom Nemotron model, and keeping lineage intact from data to model version to recommendation.

Once deployed, the model reads the current operational context and returns a recommendation with its rationale and the risks attached. A planner reviews it and makes the final call.

## Closing the loop

Every acceptance, edit, override, and production outcome is written back into Ontology, accumulating until there is enough representative data to justify another governed training run.

In the future that feedback will be used for reinforcement learning. Accepted and overridden recommendations would form preference pairs with rewards covering allocation correctness, policy compliance, and evidence grounding. The model never retrains itself in production.

The result compounds in two ways: Planners spend less time reconstructing routine decisions, so they cover more sites and products; and allocation expertise also becomes institutional knowledge, shortening onboarding and propagating key learnings across the organization.

## What post-training delivered

The NVIDIA supply chain operations team worked with Palantir to specify what the model receives, what it may recommend, and how those recommendations are scored. That workflow became both the application and the allocation decision-intelligence benchmark.

We compared three models on the same task and the same evaluation data:

- Base Nemotron 3.5 Lightning (BF16)
- Nemotron 3 Ultra (NVFP4)
- Our post-trained Nemotron 3.5 Lightning (BF16)

On the development benchmark, the post-trained Lightning model reached **86.7% allocation-decision accuracy**. Ultra reached 55.5% and base Lightning 17.5%. That puts the post-trained model 31.2 percentage points ahead of Ultra and 69.2 ahead of its own base model.

It also leads on the two metrics that weight decision types equally rather than examples. Balanced accuracy averages per-class recall, so rare calls count as much as common ones:

58.6% against Ultra’s 42.0%. Macro-F1 averages per-class F1, folding in precision so a model cannot inflate recall by over-predicting a rare class: 57.5% against 39.5%. Both matter because constrained supply means planners cut allocations far more often than they raise them, so plain accuracy alone would flatter a majority-class guesser.

The lesson is specific but important:

On a bounded allocation task, a specialized 30B model can outperform a general-purpose model that is more than an order of magnitude larger.

This doesn’t mean the smaller model is more capable overall. Its gains are concentrated in the domain it was post-trained on. Future production risk forecasting remained difficult despite fine tuning. Specialization improved the decision task but failed to solve every prediction problem attached to it.

The LoRA run finished on 2x NVIDIA B200 GPUs in minutes, light enough to repeat as feedback accumulates. This is sovereign AI in practice: proprietary supply-chain data, model weights, and inference all remain inside a single governed environment. This AI stack can be deployed on -premises or in the cloud enabling organizations to run AI where their data, systems, and operational requirements demand it.

## A supply chain that learns

The supply chain workflow discussed in this post isn’t unique to semiconductors. Any operation where critical capacity is allocated by experienced people working from fragmented signals can run the same flywheel and tailor it to new domains.

This requires three essential things:

- A governed operational layer
- Decision capture that includes both rationale and outcome
- An open model that can be post-trained inside your own secure compute boundary

Operational data trains the model, the model improves the decision, and the decision becomes new operational data for the next governed training round. That’s how NVIDIA and Palantir compress the time from wafer-out to first token, and that’s how the world’s most reliable AI infrastructure supply chain learns faster than it grows.

[Get started](https://github.com/alph-notebooks/nvidia-nemotron/blob/main/usage-cookbook/Nemotron-3-Super/lora-text2sql/nemo-automodel/automodel_lora_cookbook.ipynb) on customizing efficient, open-weight models for your own agentic workflows.

*Stay up to date on NVIDIA Nemotron by subscribing to NVIDIA news and following NVIDIA AI on LinkedIn, X, YouTube, and the Nemotron channel on Discord.*

*Access open Nemotron Models on Hugging Face and a collection of NIM microservices and Developer Examples on build.nvidia.com.*

## Start the discussion at forums.developer.nvidia.com
