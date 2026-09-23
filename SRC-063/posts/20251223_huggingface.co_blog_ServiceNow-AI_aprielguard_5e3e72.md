# AprielGuard: A Guardrail for Safety and Adversarial Robustness in Modern LLM Systems

source: https://huggingface.co/blog/ServiceNow-AI/aprielguard
published: Tue, 23 Dec 2025 14:07:35 GMT

Text Generation • 8B • Updated • 3.31k • 20

#
[
](https://huggingface.co#aprielguard-a-guardrail-for-safety-and-adversarial-robustness-in-modern-llm-systems)
AprielGuard: A Guardrail for Safety and Adversarial Robustness in Modern LLM Systems

[Enterprise Article](https://huggingface.co/blog)

*agentic*systems capable of performing multi-step reasoning, calling external tools, retrieving memory, and executing code. With this evolution comes an increasingly sophisticated threat landscape: not only traditional content safety risks, but also multi-turn jailbreaks, prompt injections, memory hijacking, and tool manipulation.

In this work, we introduce **AprielGuard**, an 8B parameter safety–security safeguard model designed to detect:

**16 categories of safety risks**, spanning toxicity, hate, sexual content, misinformation, self-harm, illegal activities, and more.**Wide range of adversarial attacks**, including prompt injection, jailbreaks, chain-of-thought corruption, context hijacking, memory poisoning, and multi-agent exploit sequences.**Safety violations and adversarial attacks in agentic workflows**, including tool calls and model reasoning traces.

AprielGuard is available in both **reasoning** and **non-reasoning** modes, enabling explainable classification when needed and low-latency classification for production pipelines.

- Model:
[https://huggingface.co/ServiceNow-AI/AprielGuard](https://huggingface.co/ServiceNow-AI/AprielGuard) - Technical Paper:
[https://arxiv.org/abs/2512.20293](https://arxiv.org/abs/2512.20293)

#
[
](https://huggingface.co#table-of-contents)
Table of Contents

[Motivation](https://huggingface.co#motivation)[AprielGuard Overview](https://huggingface.co#overview)[Taxonomy](https://huggingface.co#taxonomy)[Training Dataset](https://huggingface.co#training_dataset)[Model Architecture](https://huggingface.co#architecture)[Training Setup](https://huggingface.co#training)[Evaluation](https://huggingface.co#evaluation)[Conclusion](https://huggingface.co#conclusion)[Limitations](https://huggingface.co#limitations)

##
[
](https://huggingface.co#motivation)
Motivation

Traditional safety classifiers primarily focus on a limited classification spectrum (e.g., toxicity or self-harm), assume short inputs, and evaluate single user messages. Modern deployments, however, feature:

**Multi-turn conversations****Long contexts****Structured reasoning steps producing chains of thought****Tool-assisted multi-step workflows (agents)****A growing class of adversarial attacks exploiting reasoning, tools, or memory**

As a result, production teams increasingly rely on workarounds: multiple guard models for different stages, regex filters, static rules, or hand-crafted heuristics. These approaches are brittle and do not scale.

AprielGuard addresses these issues with a **unified model** and a **unified safety + adversarial taxonomy**, built specifically for modern LLM agent ecosystems.

##
[
](https://huggingface.co#aprielguard-overview)
AprielGuard Overview

AprielGuard operates across three input formats:

**Standalone Prompt****Multi-turn Conversation****Agentic Workflow**(tool calls, reasoning traces, memory, system context)

It outputs:

- Safety classification and a list of violated categories from the taxonomy
- Adversarial attack classification
- Optional structured
**reasoning**explaining the decision

##
[
](https://huggingface.co#taxonomy)
Taxonomy

###
[
](https://huggingface.co#a-safety-taxonomy)
**A. Safety Taxonomy**

| Category | Description |
|---|---|
| O1 | Toxic Content |
| O2 | Unfair Representation |
| O3 | Adult Content |
| O4 | Erosion of Trust in Public Information |
| O5 | Propagating Misconceptions/False Beliefs |
| O6 | Risky Financial Practices |
| O7 | Trade and Compliance |
| O8 | Dissemination of Dangerous Information |
| O9 | Privacy Infringement |
| O10 | Security Threats |
| O11 | Defamation |
| O12 | Fraud or Deceptive Action |
| O13 | Influence Operations |
| O14 | Illegal Activities |
| O15 | Persuasion and Manipulation |
| O16 | Violation of Personal Property |

*(These 16 categories are inspired from SALAD-Bench)*

###
[
](https://huggingface.co#b-adversarial-attack-taxonomy)
**B. Adversarial Attack Taxonomy**

The model detects and evaluates a wide range of adversarial prompt patterns designed to manipulate model behavior or evade safety mechanisms. The model outputs a binary classification (e.g., adversarial / non_adversarial) rather than fine-grained attack categories.

The training data covers diverse adversarial types such as role-playing, world-building, persuasion, and stylization, among many other complex prompt manipulation strategies. These examples represent only a subset of the broader adversarial scenarios incorporated in the training data.

##
[
](https://huggingface.co#training-dataset)
Training Dataset

**Synthetic data**: AprielGuard is trained on a synthetically generated training dataset. The training data points are generated at a sub-topic level of the taxonomy for better coverage. We leverage Mixtral-8x7B and internally developed uncensored models to generate unsafe content for training purposes. Models were prompted with higher temperature to induce output variation. Prompting templates are meticulously tailored to ensure accurate data generation. Adversarial attacks are constructed using a combination of synthetic data points, diverse prompt templates, and rule-based generation techniques. We leveraged[NVIDIA NeMo Curator](https://github.com/NVIDIA-NeMo/Curator)to generate large-scale, multi-turn conversational datasets featuring complex, realistic scenarios with iterative and evolving attacks through context switches. This approach enabled us to systematically synthesize diverse interaction patterns, improving the robustness of the model to long-horizon reasoning, adversarial turns, and evolving user intent. We also used[SyGra](https://github.com/ServiceNow/SyGra)framework for synthetic data generation processes for harmful prompts and attacks generation. The training dataset encompasses diverse content formats such as conversational dialogues, forum posts, tweets, instructional prompts, questions, and how-to guides.**Data augmentation**: To enhance model robustness, a range of data augmentation techniques were applied to the training data. These augmentations are designed to expose the model to natural variations and perturbations that commonly occur in real-world scenarios. Specifically, the dataset includes transformations such as character-level noise, insertion of typographical errors, leetspeak substitutions, word-level paraphrasing, and syntactic reordering. Such augmentations help the model generalize better by reducing sensitivity to superficial variations in input, thereby improving resilience against adversarial manipulations and non-standard text representations.**Agentic workflows**: Agentic workflows represent real-world scenarios where autonomous agents execute multi-step tasks involving planning, reasoning, and interaction with tools, APIs, and other agents. These workflows often include sequences of user prompts, system messages, intermediate reasoning steps, and tool invocations, making them susceptible to diverse attack vectors. To construct these training data points, we synthetically generate a wide range of scenarios across multiple domains, capturing realistic agentic interactions between a user and an agentic system. Each data point is enriched with detailed contextual elements—including tool definitions, tool invocation logs, agent roles and policies, execution traces, conversation history, memory states, and scratch-pad reasoning. For malicious or adversarial examples, we corrupt the relevant segment of the workflow to reflect a specific attack vector. Depending on the scenario, this may involve modifying user prompts, altering intermediate reasoning traces, modifying the tool outputs, injecting false memory states, or disrupting inter-agent communication. By systematically perturbing different components of the agentic workflow, we produce high-fidelity examples that expose a model to a diverse spectrum of realistic and challenging attack patterns. Each data point was simulated to reflect realistic executions, incorporating both benign and adversarial sequences.**Long context use cases**: We curated a specialized long context dataset composed of diverse, high-length use cases such as Retrieval-Augmented Generation (RAG) work-flows, multi-turn conversational threads, incident details, and operational reports containing detailed communications. These examples simulate real-world environments where large text contexts are typical.

*Synthetic data generation flow*

##
[
](https://huggingface.co#model-architecture)
Model Architecture

AprielGuard is built on top of an **Apriel-1.5 Thinker Base variant**, downscaled to an 8B configuration for efficient deployment.

**Causal decoder-only transformer****Dual-mode operation**:**Reasoning Mode**→ emits structured explanations**Fast Mode**→ classification only


###
[
](https://huggingface.co#training-setup)
Training Setup

| Parameter | Value |
|---|---|
| Base Model | Apriel 1.5 Thinker Base (downscaled) |
| Model Size | 8B parameters |
| Precision | bfloat16 |
| Batch Size | 1 with grad-accumulation = 8 |
| LR | 2e-4 |
| Optimizer | Adam (β1=0.9, β2=0.999) |
| Epochs | 3 |
| Sequence Length | Up to 32k |
| Reasoning Mode | Enabled/Disabled via instruction template |

##
[
](https://huggingface.co#evaluation-summary)
Evaluation Summary

AprielGuard is evaluated across:

- Public safety benchmarks
- Public adversarial benchmarks
- Internal Agentic workflow benchmarks
- internal Long-context use case benchmarks (up to 32k)
- Multilingual evaluation (8 languages)

##
[
](https://huggingface.co#safety-benchmark-results)
**Safety Benchmark Results**

AprielGuard performance on the public safety benchmarks.

| Source | Precision | Recall | F1-score | FPR |
|---|---|---|---|---|
|

[AyaRedteaming](https://huggingface.co/datasets/CohereLabs/aya_redteaming)[BeaverTails](https://huggingface.co/datasets/PKU-Alignment/BeaverTails)[SafeRLHF](https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF)[xstest-response](https://huggingface.co/datasets/allenai/xstest-response)[toxic-chat](https://huggingface.co/datasets/lmsys/toxic-chat)[openai-moderation-api-evaluation](https://huggingface.co/datasets/mmathys/openai-moderation-api-evaluation)[Aegis-AI-Content-Safety-Dataset-1.0](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-1.0)[Aegis-AI-Content-Safety-Dataset-2.0](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0)[HarmBench](https://huggingface.co/datasets/walledai/HarmBench)[XSTest](https://huggingface.co/datasets/walledai/XSTest)

*A comparative assessment of model performance using aggregated results from safety benchmarks.*

##
[
](https://huggingface.co#adversarial-detection-results)
**Adversarial Detection Results**

AprielGuard performance on the public adversarial benchmarks.

| Source | Precision | Recall | F1-score | FPR |
|---|---|---|---|---|
|

[Salad-Data](https://huggingface.co/datasets/OpenSafetyLab/Salad-Data)[in-the-wild-jailbreak-prompts](https://huggingface.co/datasets/TrustAIRLab/in-the-wild-jailbreak-prompts)[wildguardmix](https://huggingface.co/datasets/allenai/wildguardmix)[wildjailbreak](https://huggingface.co/datasets/allenai/wildjailbreak)[prompt-injections](https://huggingface.co/datasets/deepset/prompt-injections)[jailbreak-classification](https://huggingface.co/datasets/jackhhao/jailbreak-classification)[prompt-injections-benchmark](https://huggingface.co/datasets/qualifire/prompt-injections-benchmark)[ChatGPT-Jailbreak-Prompts](https://huggingface.co/datasets/rubend18/ChatGPT-Jailbreak-Prompts)[safe-guard-prompt-injection](https://huggingface.co/datasets/xTRam1/safe-guard-prompt-injection)

*A comparative assessment of model performance using aggregated results from adversarial benchmarks.*

##
[
](https://huggingface.co#agentic-workflow-evaluation)
Agentic Workflow Evaluation

We curated an internal benchmark dataset aimed at evaluating the detection of Safety Risks and Adversarial Attacks within agentic workflows. To construct this benchmark, we systematically designed multiple attack scenarios targeting different components of the workflow—such as prompt inputs, reasoning traces, tool parameters, memory states, and inter-agent communications. Each instance was annotated according to the taxonomy of vulnerabilities. Each workflow was simulated to reflect realistic executions, incorporating both benign and adversarial sequences. The dataset captures granular attack points across various stages such as planning, reasoning, execution, and response generation to provide fine-grained evaluation of model robustness. Overall, the dataset comprises a balanced mixture of safety risks and adversarial attacks.


**Safety** performance of different models on the agentic benchmark.


**Adversarial** performance of different models on the agentic benchmark..

##
[
](https://huggingface.co#long-context-robustness-upto-32k-tokens)
Long-Context Robustness (Upto 32k Tokens)

Many real world safety or adversarial risks do not manifest in short, isolated text snippets, but rather emerge across use cases such as Retrieval-Augmented Generation (RAG) workflows, multi-turn conversational threads, organizational incident details, and operational reports containing detailed communications. A guardian model must therefore detect subtle or "needle-in-a-haystack" cases, where malicious or manipulative content is sparsely distributed, embedded across multiple references, or intentionally obscured within benign text.

To evaluate AprielGuard’s long-context reasoning capabilities, we curated a specialized test dataset composed of diverse, high-length use cases. We considered the data upto 32k tokens for this evaluation. The baseline data was initially constructed from benign content representative of these domains. Malicious elements were then systematically injected to simulate adversarial or unsafe scenarios while maintaining the overall coherence of the text. For example, in an incident case summarization, an injection could be embedded within the case description, hidden in a metadata section, or inserted as part of a comment thread. Similarly, in multi-turn dialogue data, adversarial content might appear mid-conversation, near the end or at the beginning to test long range dependency tracking.

**Safety Risks performance**

| Model | Reasoning | Precision ↑ | Recall ↑ | F1 ↑ | FPR ↓ |
|---|---|---|---|---|---|
| AprielGuard-8B | Without | 0.99 | 0.96 | 0.97 | 0.01 |
| AprielGuard-8B | With | 0.92 | 0.98 | 0.95 | 0.11 |

**Adversarial Attacks performance**

| Model | Reasoning | Precision ↑ | Recall ↑ | F1 ↑ | FPR ↓ |
|---|---|---|---|---|---|
| AprielGuard-8B | Without | 1.00 | 0.78 | 0.88 | 0.00 |
| AprielGuard-8B | With | 0.93 | 0.94 | 0.94 | 0.10 |

##
[
](https://huggingface.co#multilingual-evaluation)
Multilingual evaluation

A major limitation in the current landscape of content moderation research is the scarcity of high- quality multilingual benchmarks. To address this gap and comprehensively assess the multilingual capabilities of AprielGuard, we extended the Safety Risks benchmarks and Adversarial Attack benchmarks into multiple non-English languages. The translation process was conducted using the [MADLAD400-3B-MT](https://huggingface.co/google/madlad400-3b-mt) model, a multilingual machine translation model based on the T5 architecture.

For this study, we selected eight of the most widely used non-English languages to ensure broad linguistic and geographical coverage: French, French-Canadian, German, Japanese, Dutch, Spanish, Portuguese-Brazilian, and Italian. Each instance from the English Safety and Adversarial benchmarks was translated into the eight target languages. During translation, we preserved the original English role identifiers, such as *User:* and *Assistant:*, while translating only the conversational content. This design choice ensures alignment with AprielGuard’s moderation framework, where the role context plays a crucial part in evaluating safety and adversarial intent.


*Multilingual performance of AprielGuard*

##
[
](https://huggingface.co#conclusion)
Conclusion

- AprielGuard unifies safety, security, and agentic robustness into a single guardian model capable of handling:
- Comprehensive safety risk classification
- Adversarial attack detection, including prompt injection and jailbreak attempts
- Various input modalities, such as standalone prompts, multi-turn conversations, and full agentic workflows
- Long-context inputs
- Multilingual inputs
- Explainable reasoning


As LLMs move toward deeply integrated agentic systems, the need for unified pipelines becomes more critical. AprielGuard is a step toward that future — reducing complexity, improving coverage, and offering a scalable foundation for trustworthy AI deployments.

##
[
](https://huggingface.co#limitations)
Limitations

Language Coverage: While AprielGuard has been primarily trained on English data, limited testing indicates it performs reasonably well across several languages, including: English, German, Spanish, French, French (Canada), Italian, Dutch, and Portuguese (Brazil). However, thorough testing and calibration are strongly recommended before deploying the model for production use in non-English settings.

Adversarial Robustness: Despite targeted training on adversarial and manipulative behaviors, the model may still exhibit vulnerability to complex or unseen attack strategies.

Domain Sensitivity: AprielGuard may underperform on highly specialized or technical domains (e.g., legal, medical, or scientific contexts) that require nuanced contextual understanding.

Latency–Interpretability Trade-off: Enabling reasoning traces enhances explainability but increases latency and compute cost. For low-latency or large-scale use cases, non-reasoning mode is recommended.

Reasoning Mode Sensitivity: The model exhibits occasional inconsistencies in classification outcomes between reasoning-enabled and non-reasoning inference modes.

Intended use: AprielGuard is intended strictly for use as a safeguard and risk assessment model. It classifies potential safety risks and adversarial threats according to the AprielGuard unified taxonomy. Any deviation from the prescribed inference may lead to unintended, unsafe, or unreliable behavior.