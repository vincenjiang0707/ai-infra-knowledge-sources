# CUGA on Hugging Face: Democratizing Configurable AI Agents

source: https://huggingface.co/blog/ibm-research/cuga-on-hugging-face
published: Mon, 15 Dec 2025 16:01:04 GMT

🤖 105

#### CUGA Agent

Configurable Generalist Agent, leader in AppWorld Benchmark

**CUGA (Configurable Generalist Agent)** was designed to overcome these limitations. It's an **open-source, AI Agent** that combines flexibility, reliability, and ease of use for enterprise use cases. By abstracting orchestration complexity, CUGA empowers developers to focus on domain requirements rather than the internals of agent building. And now, with its integration into 🚀[Hugging Face Spaces](https://huggingface.co/spaces/ibm-research/cuga-agent)🚀, experimenting with CUGA and open models has never been easier.

CUGA is a **configurable, general-purpose AI agent** that supports complex, multi-step tasks across web and API environments. It has achieved state-of-the-art performance on leading benchmarks:

🥇 [#1 on AppWorld](https://appworld.dev/leaderboard) - a benchmark with 750 real-world tasks across 457 APIs

🥈 [Top-tier on WebArena (#1 from 02/25 - 09/25)](https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ/edit?pli=1&gid=0#gid=0) - showcases CUGA Computer Use capabilities with a complex benchmark for autonomous web agents across application domains

At its core, CUGA offers:

**We're also continuing to innovate with new experimental capabilities, including:**


**Figure 1: CUGA Agentic Architecture**

The CUGA architecture begins with the user's message flowing into a chat layer that interprets intent and constructs the user's goal, based on context. A task planning and control component then decomposes this goal into structured subtasks, tracked programmatically through a dynamic task ledger. This ledger supports re-planning when needed, ensuring robust execution. Subtasks are delegated to specialized agents, such as the API agent, which uses an inner reasoning loop to generate pseudo-code instructions before invoking code in a secure sandbox. The system leverages a tool registry that goes beyond MCP protocols to parse and understand tool capabilities, enabling precise orchestration. Once all steps are completed, the final response is returned to the user, delivering reliable, policy-aligned outcomes.

CUGA works best when inference is fast. When each call takes seconds, delays compound and force a tradeoff between agent capability and user experience. Running on high-performance inference platforms like [Groq](https://groq.com) shows how fast inference fundamentally expands what agent architectures can achieve.

CUGA is fully **open source, under the Apache 2.0 license,** and you can find us at [cuga.dev](https://cuga.dev).

By embracing **open models**, CUGA aligns with the Hugging Face ethos of democratizing AI-giving developers the freedom to choose models that best fit their needs, whether for experimentation or production.

CUGA has been tested with a variety of open models, including gpt-oss-120b and Llama-4-Maverick-17B-128E-Instruct-fp8 (both hosted on Groq). Our Hugging Face Space uses gpt-oss-120b, with the model hosted on Groq, offering a rapid response time for LLM calls

Groq runs open models on its custom‑built LPUs, which are designed for AI inference and optimal for repeated agent inferences required by CUGA's architecture, enabling planning, execution, and validation steps to finish fast. The result is strong cost and performance: open models are ~80-90% cheaper than closed alternatives; Groq's OpenAI-compatible APIs meet production latency needs, and CUGA stays fully configurable across models, providers, and deployment topologies.

To make agent development even more accessible, CUGA integrates with **Langflow**, an open-source visual programming interface for building LLM-powered workflows. Its intuitive drag-and-drop interface reduces the barrier to entry for those who prefer low-code solutions.

Starting with [ Langflow 1.7.0](https://langflow.org), CUGA ships with its own widget, enabling users to assemble complex, multi-tool agents visually and deploy with a click. Give it a try at

We've launched a **CUGA demo on Hugging Face Spaces** to give you a taste of what's possible. This demo showcases a **small CRM system** and equips CUGA with **20 preconfigured tools** for handling sales related data queries and API interactions through the API Agent. To make experimentation even more powerful, the demo provides **access to workspace files**, enabling you to **use predefined policies.**

**Give it a try on** [ Hugging Face Spaces](https://huggingface.co/spaces/ibm-research/cuga-agent) and share your feedback!

CUGA brings a new level of flexibility and openness to AI agent building. To engage with us:

Configurable Generalist Agent, leader in AppWorld Benchmark

Impressive work on CUGA’s architecture and configurability. The structured planning, tool orchestration, and benchmark results demonstrate a strong approach to scalable agent design. Integration with Hugging Face Spaces and Langflow significantly lowers the barrier to experimentation and deployment.

Here is our Website: [https://www.simbainstitute.in/artificial-intelligence-course-in-surat/](https://www.simbainstitute.in/artificial-intelligence-course-in-surat/)