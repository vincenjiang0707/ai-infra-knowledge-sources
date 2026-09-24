# meta-muse-glimmer

source: https://fireworks.ai/blog/meta-muse-glimmer

This model was built with agents in mind. It is designed for "always-on" agents rather than just simple chat interactions. It’s capable of managing many sequential tool calls over multiple turns. It has the ability to recover from failures and retries rather than halting when a tool call fails or returns something unexpected.

Muse Glimmer is a 30B dense model made up of 52 transformer layers, grouped-query attention with 32 query heads and 2 KV heads, and SwiGLU feed-forward layers. A ~1.8B perception encoder gives it native image understanding alongside text, and it supports a 128K+ token context window.

Meta built this to fit in 24 GB. That same design: small KV footprint, sliding-window attention is what makes it affordable to serve at concurrency. And because the weights are released under Apache 2.0, the path is symmetric: prototype against the quantized build on a workstation, deploy the same model on Fireworks when it needs to serve thousands of sessions.

The detail that matters most for agents is the attention pattern: sliding-window attention over 2,048 tokens on most layers, with a full global attention layer every fourth layer. Paired with just two KV heads, that keeps the KV cache small - which is what makes long-context agents economical to serve at high concurrency. The architectural efficiency of this model allows an agent to manage 100K tokens of accumulated tool output more economically than a comparable dense model, with savings that scale across concurrent sessions.

The model also supports DFlash speculative decoding for lower-latency generation.

From end-to-end support resolution to extended autonomous research, this model is built for deep multi-step reasoning, large parallel scale, and reliability across demanding agentic workflows. This model is ideal for the following workloads:

Against Gemma 4 31B and Qwen 3.6 27B, Muse Glimmer leads on the benchmarks that measure tool orchestration and sustained multi-turn work:

| Benchmark | Muse Glimmer 30B (High Reasoning) | Gemma 4 31B (Thinking Mode) | Qwen 3.6 27B (Thinking Mode) |
|---|---|---|---|
Benchmark | Muse Glimmer 30B (High Reasoning) | Gemma 4 31B (Thinking Mode) | Qwen 3.6 27B (Thinking Mode) |
MCP Atlas (Public) | 75.5 | 54.2 | 62.5 |
DeepSearch QA | 74.6 | 61.7 | 71.1 |
Gaia2 | 43.3 | 36.4 | 40.0 |
WildClawBench | 47.6 | 37.6 | 43.2 |
SWE-Bench Pro | 51.2 | 36.9 | 50.2 |

*Note the Muse Glimmer benchmarks are reported by Meta

If your agent lives in a terminal or drives a desktop, benchmark both models. If it orchestrates APIs and MCP tools over long multi-turn sessions, this is the stronger pick at this size.

Muse Glimmer is available on Fireworks on both serverless and on-demand deployments. We shipped a day later than others, on purpose. We took an extra day to launch because we wanted to get this right. That meant correcting the model's shipped generation config and wiring reasoning-effort control all the way through to the model. Great models deserve great execution. Quality is our highest priority, and we wanted to ensure you get the exact performance, control, and reliability you expect from day one.

**Running it well:** Meta recommends using the following settings.

temperature = 1.0, top_p = 0.95, top_k = 64

Reasoning effort is set in the system prompt as Reasoning strength: <value>, with low, medium, high, and xhigh available - use high or xhigh for agentic and coding work. All benchmark numbers in the table above are at high.

The era of agentic AI is here. We encourage you to start building today with Muse Glimmer model on Fireworks. Check out our [documentation ](https://fireworks.ai/models/fireworks/muse-glimmer-30b)and start building!
