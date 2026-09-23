# 2026-01-23-mom-on-amd-gpu

source: https://vllm.ai/blog/2026-01-23-mom-on-amd-gpu

# Building Mixture-of-Models on AMD GPUs with vLLM-SR

## Why System Intelligence for LLMs?

We are working on building the **System Level Intelligence** for Mixture-of-Models (MoM), bringing **Collective Intelligence** into LLM systems.

The core questions we're addressing:

- How to capture the missing signals in request, response, and context?
- How to combine signals to make better routing decisions?
- How to enable efficient collaboration between different models?
- How to secure systems from jailbreaks, PII leaks, and hallucinations?
- How to collect valuable signals and build a self-learning system?

With **vLLM Semantic Router (vLLM-SR) v0.1**, we've deployed a live MoM system on AMD **MI300X/MI355X** GPUs that demonstrates these capabilities in action—routing queries across 6 specialized models using 8 signal types and 11 decision rules with the performance boost.

**🎮 Try it live: https://play.vllm-semantic-router.com**

## Table of Contents

[Mixture-of-Models vs Mixture-of-Experts](https://vllm.ai#mixture-of-models-vs-mixture-of-experts)[The MoM Design Philosophy](https://vllm.ai#the-mom-design-philosophy)[Live Demo on AMD GPUs](https://vllm.ai#live-demo-on-amd-gpus)[Signal-Based Routing](https://vllm.ai#signal-based-routing)[Deploy Your Own](https://vllm.ai#deploy-your-own)

## Mixture-of-Models vs Mixture-of-Experts

Before diving in, let's clarify a common confusion: **MoM is not MoE**.

### Mixture-of-Experts (MoE): Intra-Model Routing

MoE is an **architecture pattern inside a single model**. Models like Mixtral, DeepSeek-V3, and Qwen3-MoE use sparse activation—for each token, only a subset of "expert" layers are activated based on a learned gating function.

**Key characteristics:**

- Routing happens at the
**token level**, inside forward pass - Router is
**learned during training**, not configurable - All experts share the same training objective
- Reduces compute per token while maintaining capacity

### Mixture-of-Models (MoM): Inter-Model Orchestration

MoM is a **system architecture pattern** that orchestrates multiple independent models. Each model can have different architectures, training data, capabilities, and even run on different hardware.

**Key characteristics:**

- Routing happens at the
**request level**, before inference - Router is
**configurable at runtime**via signals and rules - Models can have completely different specializations
- Enables cost optimization, safety filtering, and capability matching

### Why This Distinction Matters

| Aspect | MoE | MoM |
|---|---|---|
Scope | Single model architecture | Multi-model system design |
Routing granularity | Per-token | Per-request |
Configurability | Fixed after training | Runtime configurable |
Model diversity | Same architecture | Any architecture |
Use case | Efficient scaling | Capability orchestration |

**The insight**: MoE and MoM are complementary. You can use MoE models (like Qwen3-30B-A3B) as components within a MoM system—getting the best of both worlds.

## The MoM Design Philosophy

### Why Not Just Use One Big Model?

The "one model to rule them all" approach has fundamental limitations:

**Cost inefficiency**: A 405B model processing "What's 2+2?" wastes 99% of its capacity**Capability mismatch**: No single model excels at everything—math, code, creative writing, multilingual**Latency variance**: Simple queries don't need 10-second reasoning chains**No separation of concerns**: Safety, caching, and routing logic baked into prompts

### The MoM Solution: Collective Intelligence

MoM treats AI deployment like building a **team of specialists** with a smart dispatcher:

**Core Principles:**

**Signal-Driven Decisions**: Extract semantic signals (intent, domain, language, complexity) before routing**Capability Matching**: Route math to math-optimized models, code to code-optimized models**Cost-Aware Scheduling**: Simple queries → small/fast models; Complex queries → large/reasoning models**Safety as Infrastructure**: Jailbreak detection, PII filtering, and fact-checking as first-class routing signals

## Live Demo on AMD GPUs

We've deployed a live demo system powered by **AMD MI300X GPUs** that showcases the full MoM architecture:

**🎮 https://play.vllm-semantic-router.com**

### The Demo System Architecture

The AMD demo system implements a complete MoM pipeline with **6 specialized models** and **11 routing decisions**:

**Models in the Pool:**

| Model | Size | Specialization |
|---|---|---|
Qwen3-235B | 235B | Complex reasoning (Chinese), Math, Creative |
DeepSeek-V3.2 | 320B | Code generation and analysis |
Kimi-K2-Thinking | 200B | Deep reasoning (English) |
GLM-4.7 | 47B | Physics and science |
gpt-oss-120b | 120B | General purpose, default fallback |
gpt-oss-20b | 20B | Fast QA, security responses |

**Routing Decision Matrix:**

| Priority | Decision | Trigger Signals | Target Model | Reasoning |
|---|---|---|---|---|
| 200 | `guardrails` | `keyword: jailbreak_attempt` | gpt-oss-20b | off |
| 180 | `complex_reasoning` | `embedding: deep_thinking` + `language: zh` | Qwen3-235B | high |
| 160 | `creative_ideas` | `keyword: creative` + `fact_check: no_check_needed` | Qwen3-235B | high |
| 150 | `math_problems` | `domain: math` | Qwen3-235B | high |
| 145 | `code_deep_thinking` | `domain: computer_science` + `embedding: deep_thinking` | DeepSeek-V3.2 | high |
| 145 | `physics_problems` | `domain: physics` | GLM-4.7 | medium |
| 140 | `deep_thinking` | `embedding: deep_thinking` + `language: en` | Kimi-K2-Thinking | high |
| 135 | `fast_coding` | `domain: computer_science` + `language: en` | gpt-oss-120b | low |
| 130 | `fast_qa_chinese` | `embedding: fast_qa` + `language: zh` | gpt-oss-20b | off |
| 120 | `fast_qa_english` | `embedding: fast_qa` + `language: en` | gpt-oss-20b | off |
| 100 | `casual_chat` | Any (default) | gpt-oss-20b | off |

### Playground Capabilities

The interactive playground provides real-time visibility into every routing decision:

**Signal Transparency**

After each response, the UI displays:

**Selected Model**: Which model actually processed your request**Selected Decision**: Which routing rule matched**Matched Signals**: Keywords, Embeddings, Domain, Language, Fact-check, User Feedback, Preference, Latency**Reasoning Mode**: Whether chain-of-thought was enabled**Cache Status**: Whether semantic cache was hit

**Safety Indicators**

- Jailbreak blocked (if triggered)
- PII violation detected
- Hallucination warnings
- Fact-check requirements

**Thinking Topology Visualization**

One highlight worth emphasizing: we've implemented a [topology visualization](https://play.vllm-semantic-router.com/topology) capability. Beyond displaying static signal-decision relations, it reveals **real-time thinking chains** triggered by different queries—like watching a giant neural network built from semantics come alive. Each question illuminates different pathways through the model constellation, making the MoM routing logic intuitive and debuggable.

**Settings Panel**

- Custom model override
- System prompt customization
- Multi-turn conversation support

### Example Queries to Try

**Fast QA in English:**

→ Routes to `gpt-oss-20b`

via `fast_qa`

+ `en`

(no reasoning, fast response)

**Deep Thinking in Chinese:**

→ Routes to `Qwen3-235B`

via `deep_thinking`

+ `zh`

(high reasoning effort)

**Complex Code Analysis:**

→ Routes to `DeepSeek-V3.2`

via `computer_science`

+ `deep_thinking`

(high reasoning)

**Math Problem:**

→ Routes to `Qwen3-235B`

via `domain: math`

(high reasoning)

**Creative Writing:**

→ Routes to `Qwen3-235B`

via `creative_ideas`

+ `no_check_needed`

(high reasoning)

**Safety Test:**

→ Blocked by `guardrails`

decision (priority 200)

## Signal-Based Routing

vLLM-SR supports the following signal types:

| Signal Type | Description | Latency |
|---|---|---|
keyword | Pattern matching with keywords/regex | < 1ms |
embedding | Semantic similarity via embeddings | 50-100ms |
domain | MMLU-based academic domain classification | 50-100ms |
language | Multi-language detection (100+ languages) | < 1ms |
fact_check | Identifies queries needing factual verification | 50-100ms |
user_feedback | Detects corrections, satisfaction, clarifications | 50-100ms |
preference | Route preference matching via external LLM | 100-200ms |

### How Signals Work Together

The demo system combines multiple signals with priority-based decisions:

| Priority | Decision | Signals | Model | Use Case |
|---|---|---|---|---|
| 200 | `jailbreak_blocked` | `keyword: jailbreak_attempt` | gpt-oss-20b | Security |
| 180 | `deep_thinking_chinese` | `embedding: deep_thinking` + `language: zh` | Qwen3-235B | Complex reasoning in Chinese |
| 145 | `code_deep_thinking` | `domain: computer_science` + `embedding: deep_thinking` | DeepSeek-V3.2 | Advanced code analysis |
| 140 | `deep_thinking_english` | `embedding: deep_thinking` + `language: en` | Kimi-K2-Thinking | Complex reasoning in English |
| 130 | `fast_qa_chinese` | `embedding: fast_qa` + `language: zh` | gpt-oss-20b | Quick Chinese answers |
| 120 | `fast_qa_english` | `embedding: fast_qa` + `language: en` | gpt-oss-20b | Quick English answers |
| 100 | `default_route` | Any | gpt-oss-120b | General queries |

## How to run it on AMD GPU (MI300X/MI355X)

Want to run vLLM-SR on your own AMD hardware? Here's a quick start guide.

📖 **Full deployment guide**: [deploy/amd/README.md](https://github.com/vllm-project/semantic-router/blob/main/deploy/amd/README.md)

### Step 1: Install vLLM-SR

### Step 2: Initialize Configuration

This generates `config.yaml`

. Edit it to configure your routing logic and model endpoints.

### Step 3: Deploy vLLM on AMD GPU

Pull the AMD ROCm-optimized vLLM image:

Start the container with AMD GPU access:

Launch vLLM with AMD-optimized settings:

### Step 4: Start the Semantic Router

### Step 5: Test It

## What's Next

The live demo shows what's possible with MoM architecture. Key findings from our AMD deployment:

| Query Type | Signal Detection | Reasoning | Optimization |
|---|---|---|---|
| Math/Science | `domain: math` | ✅ Enabled | Step-by-step solutions |
| Simple QA | `embedding: fast_qa` | ❌ Disabled | Fast response |
| Code | `domain: computer_science` | Configurable | Context-aware |
| User Feedback | `user_feedback: wrong_answer` | ✅ Enabled | Re-route to capable model |
| Security | `keyword: jailbreak_attempt` | N/A | Real-time interception |

**Key takeaways:**

**Math/Science queries**: Automatically trigger reasoning mode for step-by-step solutions**Simple QA**: Fast routing to smaller models, no reasoning overhead**User feedback loop**: "That's wrong" triggers re-routing to more capable model with reasoning enabled**Security**: Real-time jailbreak detection before any model processes the request

## Resources

**Live Demo**:[https://play.vllm-semantic-router.com](https://play.vllm-semantic-router.com)**GitHub**:[vllm-project/semantic-router](https://github.com/vllm-project/semantic-router)**Documentation**:[vllm-semantic-router.com](https://vllm-semantic-router.com)**AMD ROCm**:[amd.com/rocm](https://www.amd.com/en/products/software/rocm.html)

## Acknowledgements

We would like to thank the following teams and individuals for their contributions to this work:

**AMD AIG Team**: Andy Luo, Haichen Zhang**vLLM Semantic Router OSS team**: Xunzhuo Liu, Huamin Chen, Senan Zedan, Yehudit Kerido, Hao Wu, and the vLLM Semantic Router OSS team

## Join Us

**Looking for Collaborations!** Calling all passionate community developers and researchers: join us in building the system intelligence on AMD GPUs.

Interested? Reach out to us:

- Haichen Zhang:
[haichzha@amd.com](mailto:haichzha@amd.com) - Xunzhuo Liu:
[xunzhuo@vllm-semantic-router.ai](mailto:xunzhuo@vllm-semantic-router.ai)

Share your use cases and feedback in **#semantic-router** channel on [vLLM Slack](https://vllm-dev.slack.com/archives/C09CTGF8KCN)
