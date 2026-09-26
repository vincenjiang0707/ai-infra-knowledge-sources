# [Issue #597] Feature Request: Add Mooncake Trace Data Support

source: https://github.com/vllm-project/guidellm/issues/597
state: closed | updated: 2026-06-30T18:43:49Z
labels: priority-high, internal

## 正文

### Problem Statement

GuideLLM currently lacks support for the Mooncake trace format, which provides real datasets with synthetic tokens and time-based request rates. This gap prevents users from performing proper customer workload simulation using Mooncake traces.

Mooncake traces are becoming an industry standard for KV cache testing and LLM inference benchmarking. Without native support for this trace format, GuideLLM users cannot:

- Replay production-representative workloads that use Mooncake's real dataset with synthetic token distributions
- Leverage Mooncake's time-based request rate patterns for realistic load generation
- Benchmark and demonstrate performance against industry-standard KV cache testing methodologies

This gap directly affects the ability to evaluate and compare LLM deployment performance against widely adopted industry benchmarks.

### Proposed Solution

Add native Mooncake trace format support to GuideLLM's data ingestion pipeline. This would involve:

1. **Trace Parser**: Implement a Mooncake trace parser that can read and interpret Mooncake's trace file format, extracting request timestamps, token counts (input/output), and request metadata.

2. **Data Source Integration**: Add a new `--data` source type (e.g., `--data mooncake:<path_to_trace>`) that allows users to load Mooncake trace files directly as workload definitions.

3. **Time-Based Rate Replay**: Support Mooncake's time-based request rate patterns so that GuideLLM can replay requests at the exact inter-arrival times specified in the trace, enabling faithful production workload reproduction.

4. **Synthetic Token Mapping**: Map Mooncake's synthetic token specifications to GuideLLM's internal token representation, ensuring that input/output token distributions from the trace are accurately reflected in the benchmark requests.

5. **Documentation**: Add documentation and examples showing how to use Mooncake traces with GuideLLM for KV cache performance testing.

### Alternatives Considered

**Manual trace conversion**: Users could manually convert Mooncake trace files into GuideLLM's existing supported formats (e.g., custom JSON or HuggingFace datasets). However, this is error-prone, loses the time-based request rate information that is central to Mooncake's value, and creates a significant barrier for users who want to quickly benchmark with industry-standard traces.

**External preprocessing scripts**: A standalone script could preprocess Mooncake traces into a compatible format. This adds toolchain complexity and maintenance burden, and still loses fidelity in the time-based scheduling that Mooncake traces provide.

**Using other benchmarking tools**: Some other LLM benchmarking tools may support Mooncake traces, but they lack GuideLLM's comprehensive evaluation capabilities such as sweep-based rate testing and rich reporting.

### Usage Examples

```markdown
# Run GuideLLM benchmark using a Mooncake trace file
guidellm benchmark run --target http://localhost:8000/v1 --data mooncake:./traces/mooncake_trace.jsonl

# Use Mooncake trace with time-based request replay
guidellm benchmark run --target http://localhost:8000/v1 --data mooncake:./traces/mooncake_trace.jsonl --rate-type trace

# Combine Mooncake trace with sweep mode to find saturation point
guidellm benchmark run --target http://localhost:8000/v1 --data mooncake:./traces/mooncake_trace.jsonl --rate-type sweep
```

### Additional Context

**Background on Mooncake Traces:**
Mooncake is an open-source LLM serving platform that has published production trace datasets. These traces provide real dataset characteristics with synthetic tokens and time-based request rates, making them valuable for realistic workload simulation and KV cache performance testing.

**Industry Adoption:**
Mooncake traces are increasingly being adopted as a standard benchmark format for evaluating LLM inference performance, particularly for KV cache optimization and disaggregated prefill/decode architectures. Adding support would allow GuideLLM to be used in direct comparisons with results from other tools in the ecosystem.

**Related Work:**
- Mooncake project: https://github.com/kvcache-ai/Mooncake
- The trace format includes fields for request arrival times, input/output token counts, and request metadata that map well to GuideLLM's existing data pipeline concepts.

## 评论 (2)

### VincentG1234 · 2026-02-26

Hi @sjmonson @cemigo114   ,
I’m working on this and have a minimal but functional implementation that addresses most of what’s described here. I’d be happy to open a PR and iterate based on your feedback.
What’s implemented so far:
- Trace parser & time-based replay: A trace file (JSONL/JSON/CSV) with a timestamp column is read, timestamps are converted to relative times (first event = 0), and requests are scheduled at start_time + time_scale * relative_timestamp[i], so inter-arrival times from the trace are preserved.
- Synthetic token mapping: A trace_synthetic deserializer reads timestamp, input_length, and output_length (same field names as the Mooncake trace format) and produces prompts with token counts matching those values (±10%), so Mooncake-style traces work without any conversion.
- Replay profile: A replay profile wires the trace file path to both the dataset (synthetic prompts) and the scheduler (time-based replay). 
- Usage looks like:
--data ./traces/mooncake_trace.jsonl --profile replay
(and optionally --data-args '[{"type_": "trace_synthetic"}]' to force the trace deserializer).

Not done yet:
The mooncake:<path> data source shorthand (would resolve to trace_synthetic + path).
Explicit docs/examples for Mooncake traces (would add once the PR shape is agreed).

If you’re open to it, I can open a PR with the current changes and then add the mooncake. Happy to adjust naming (profile vs rate-type, etc.) to match your conventions. :)

### sjmonson · 2026-03-02

Sure, we would definitely appreciate a PR! Towards the "data source shorthand" don't worry about implementing that format. For the short term I like your `--data-args` solution. Sometime after the upcoming v0.6.0 release we will be redoing `--data` to make deserializer type more explicit. E.g. `--data '{"type": "synthetic", "prompt_tokens": 256, ...}'`
