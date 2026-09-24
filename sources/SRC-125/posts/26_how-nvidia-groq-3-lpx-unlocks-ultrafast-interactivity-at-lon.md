# how-nvidia-groq-3-lpx-unlocks-ultrafast-interactivity-at-long-context-on-nvidia-vera-rubin

source: https://developer.nvidia.com/blog/how-nvidia-groq-3-lpx-unlocks-ultrafast-interactivity-at-long-context-on-nvidia-vera-rubin/

[NVIDIA Groq 3 LPX](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) is the interactive AI inference accelerator for the [NVIDIA Vera Rubin platform](https://www.nvidia.com/en-us/data-center/technologies/rubin/). At the core of the platform is [NVIDIA Vera Rubin NVL72](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/), the most versatile machine ever built, delivering high throughput and interactivity across the widest range of AI workloads—from small to large models, both open and closed. Groq 3 LPX, when paired with Vera Rubin NVL72, extends the platform’s ability to address the highest-interactivity serving tiers, expanding Vera Rubin’s ability to power user experiences as part of [AI factories](https://www.nvidia.com/en-us/solutions/ai-factories/).

In this post, we report the first third-party benchmark of performance on Groq 3 LPX systems: [Artificial Analysis](https://artificialanalysis.ai/) has run its 100K context benchmark on the Gemma 4 31B model on Groq 3 LPX, measuring a world-class interactivity of 3,431 output tokens/second. The technologies that power this performance unlock the ability of the Vera Rubin platform to serve multiagent systems powered by 2T+ parameter models with high interactivity and long context, through pairing Groq 3 LPX with Vera Rubin NVL72.

## Why is long context at high interactivity important?

Agentic sessions are characterized by multiturn inference. At the end of each turn, the agent’s output is appended to the continually growing context that is fed into all subsequent turns.

As Figure 1 shows, context can grow to hundreds of thousands of tokens across entire agentic sessions, especially as sessions exceed hundreds of turns. That means that, later in the task, the agent must repeatedly process everything it has learned so far.

Without long context, agents can only take into account a fraction of the relevant context of what has come before. No matter how fast or smart the underlying model, limited context means limited agentic capability. The most capable agents must not only deliver speed; they must do so while retaining long context as the session grows.

## Why is serving models at ultrafast interactivity with long context challenging?

Serving a model at more than 3,000 tokens per second per user while managing a KV cache for 100K input tokens creates a distinct systems challenge. In inference systems, divide-and-conquer techniques such as tensor parallelism (TP) can deliver order-of-magnitude speedups—if the system can efficiently manage the coordination required (collective operations). But the highest levels of interactivity require very small batch sizes, where the fixed coordination cost can outweigh the time saved from TP.

TP involves two parts: doing a series of computations in parallel split across multiple chips, and then combining the results. At the very small batch sizes required for high interactivity inference, making TP effective requires tight coordination. Many small tensors must transfer between compute units, with each tensor leaving and arriving exactly where and when it needs to. Time spent communicating and combining results can easily become comparable to—or larger than—the time saved by distributing the computation.

On any system, the interprocessor network must coordinate this series of transfers. As shown in Figure 2, the amount of total time each individual transfer takes has two components:

**First bit latency**: The time spent determining which specific communication link should be used for a transfer, synchronizing the sender and receiver link end points, and arbitrating conflicts (such as two chips wanting to send data over a single link at the same time).**Transfer time**: The actual time to move the data over the network, which is a function of the amount of data being transferred relative to the network bandwidth.

The order-of-magnitude speedups TP can provide require driving down the first bit latency to an absolute minimum. Doing so across an entire forward pass—employing parallelism for both model weights and long-context KV cache—requires an approach designed with both low-latency and long context in mind.

## How does Groq 3 LPX serve models at ultrafast interactivity with long context?

NVIDIA Groq 3 LPX serves models at ultrafast interactivity with long context using its compiler-scheduled workload planning. This includes its chip-to-chip (C2C) within-rack networking and its ability to heavily overlap compute with interprocessor communication.

### Tightly scheduled interchip communication

Groq 3 LPX uses a deterministic execution model. This means the compiler has visibility into:

- The individual compute units in each of the 256 LP30 local processing units (LPUs)
- The 128 GB of total SRAM-based memory collectively in those chips
- The 96 C2C links per chip running at 112 Gbps each

It can use this information to produce a schedule, down-to-the-clock cycle of exactly how the workload will run before it begins.

This has many advantages. Most relevant to high interactivity, it eliminates the need for real-time arbitration of transfers because it can plan when each piece of data will move over each C2C link, producing a data transfer schedule like the one shown in Figure 3, before the workload begins.

Further, this preworkload scheduling enables a fundamental shift in the way data transfers occur. Many systems have several steps for each transfer, even for small pieces of data:

- One chip may make a request to transfer data
- Another chip may confirm the data is available to transfer and locate it
- The data may have to contend with other pieces of data being transferred at the same time

By contrast, the compiler-produced schedule means that LPUs can send data on the clock cycle when it is ready, and consume the data on the clock cycle when it arrives, as shown in Figure 4.

The links are point-to-point between pairs of LPUs and each LPU can act as a router as well as a processor, meaning that if needed, data can be routed to LPUs by way of other LPUs.

This networking design lets LPX drive down the first bit latency from Figure 2 to an absolute minimum. With large batches, this first bit latency time is dwarfed by the time to actually send the bytes over the wire; but for the high interactivity area of the pareto, minimizing the fixed transfer initialization time becomes critical.

### Fine-grained computation-communication overlap

The LPX compiler, in addition to prescheduling the many small C2C transfers necessary for small batch inference, can also overlap those transfers with compute at a very fine granularity.

Overlapping computation and communication is essential for getting optimal performance out of any inference system. LPX can take this a step further: the compiler schedules workloads on its compute and communication units at the level of 320-byte vectors. Taking advantage of the fact that matrix multiplications can be expressed as a series of dot products, as shown in Figure 5, the compiler can schedule individual LPUs to compute 320 columns of an output matrix and send them over the C2C links immediately after they are computed.

This allows Groq 3 LPX to begin the transfer of data as soon as enough of the result to fill a 320-byte vector is ready, instead of waiting for an entire matrix operation to complete. This increases the overlap of computation and communication, which matters especially with small tensors (Figure 6).

Together, these technologies enable order-of-magnitude speedups in the most computationally intensive attention operations of long-context inference. By enabling a tightly coordinated schedule of interchip computations and communications, Groq 3 LPX can leverage the divide-and-conquer approach of tensor parallelism to provide speedups even in the small-batch, high-interactivity part of the Pareto.

## Groq 3 LPX achieves leading interactivity at 100K context on Artificial Analysis benchmark

[Artificial Analysis](https://artificialanalysis.ai/) has standard benchmarking suites for testing the serving speed of different inference providers on those providers’ models, at both 10K and 100K of input context length. Using this suite, Artificial Analysis benchmarked Gemma 4, a 31B-parameter dense model released in April 2026, on its 100K benchmark. An [NVIDIA Groq 3 LPX](https://www.nvidia.com/en-us/data-center/lpx/) system NVIDIA has stood up in its own data centers generated answers at 3,431 output tokens per second (Figure 7).

Median speed across samples with 100K input context length was 3,431 tokens/second. “o200K_basetokens” tokenizer–same across all models and providers–was used.

With low-latency access to SRAM across the rack, we expect to be able to maintain this speed into the multi-hundred thousands of tokens. For agentic coding tasks, where an agent may read hundreds of files easily exceeding 100K context tokens, and incorporate that context when generating 5,000 generated reasoning and output tokens, this is not only context users will benefit from, but also speed that fundamentally changes their experience. At this rate, decoding 5,000 tokens takes about 1.5 seconds versus 50 seconds at 100 tokens per second. Even this comparison is generous, since today’s most popular agentic tools run closer to 60 tokens per second.

Artificial Analysis also benchmarked the same system at 10K context length to check whether LPX could achieve similar performance at that length; they found that Groq 3 LPX answered at a median speed of 3,382 output tokens per second. The combination of the LPUs deterministic architecture and high tensor parallelism leads to minimal variation of latency and output tokens/sec with respect to context length.

Median speed across samples with 10K input context length was 3,382 tokens/second. The same “o200K_basetokens” tokenizer was used.

Testing by Artificial Analysis and NVIDIA confirmed that the NVIDIA configuration for both of these benchmarks had no loss of precision or model quality in its outputs. Learn more about the [Artificial Analysis testing methodology](https://artificialanalysis.ai/methodology).

As a complementary coding-specific measurement, we ran the open-source[ SPEED-Bench](https://huggingface.co/datasets/nvidia/SPEED-Bench) benchmark, because raw generation speed is especially important in agentic coding workflows. Using the same Gemma 4 model, the NVIDIA Groq 3 LPX system produced answers to these coding questions at a median speed of 4,767 output tokens per second and a P80 of 5,520 output tokens per second. This means that 20% of tasks on this dataset completed at over 5,500 tokens per second.

Median output token speed was 4,767 tokens/second; over 20% of problems had solutions generated at a speed of over 5,500 tokens/second.

## How does NVIDIA Groq 3 LPX accelerate long context agentic AI workloads alongside Vera Rubin NVL72?

Pairing this new low latency, deterministic execution capability of Groq 3 LPX with Vera Rubin NVL72 racks enables multiple serving configurations, including:

**Standard prefill-decode disaggregation**: Vera Rubin NVL72 handles prefill and hands off the KV cache once per turn. Groq 3 LPX uses this KV cache, along with weights held in SRAM, to perform the entire decode step.**Attention-FFN disaggregation**: Vera Rubin NVL72 computes attention and holds the KV cache in DRAM, while Groq 3 LPX executes the FFN layers. Only intermediate tokens are sent between racks, once per full-attention layer.**External-drafter speculative decoding**: Groq 3 LPX runs a small draft model ahead of the large target model on Vera Rubin NVL72, which verifies and commits tokens and returns rejected positions for the next chunk. Each rack keeps its own model’s KV cache and only draft tokens cross the link.

All of these enable each rack to focus on the portion of the workload it can best execute. With this fully co-designed solution, LPX is able to push the Vera Rubin platform to new levels of high interactivity and low latency. Figure 11 shows a projection of a scaled-up GPT-OSS model to 2 trillion parameters running on Vera Rubin NVL72 and Groq 3 LPX.

*GPT-OSS 2T is a scaled-up version of the GPT-OSS 120B model.

## Learn more

NVIDIA Groq 3 LPX speed has now been measured by a third-party benchmark, confirming that it delivers leading interactivity at a context length that matters for agentic workloads. NVIDIA has also measured even more extreme performance on an open source benchmark of coding tasks.

To learn more about Groq 3 LPX, see[ Inside NVIDIA Groq 3 LPX: The Low-Latency Inference Accelerator for the NVIDIA Vera Rubin Platform](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/).

## Start the discussion at forums.developer.nvidia.com
