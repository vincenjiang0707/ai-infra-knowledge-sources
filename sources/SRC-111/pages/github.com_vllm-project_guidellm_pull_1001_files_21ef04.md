source: https://github.com/vllm-project/guidellm/pull/1001/files

-
[Notifications](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm)You must be signed in to change notification settings -
[Fork 238](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm)

# docs: added end2end examples for users (optimal concurrency and custo… #1001

## New issue

**Have a question about this project?** Sign up for a free GitHub account to open an issue and contact its maintainers and the community.

By clicking “Sign up for GitHub”, you agree to our [terms of service](https://docs.github.com/terms) and
[privacy statement](https://docs.github.com/privacy). We’ll occasionally send you account related emails.

Already on GitHub?
[Sign in](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm%2Fissues%2Fnew%2Fchoose)
to your account

Open

[cmiyai](https://github.com/cmiyai)wants to merge 4 commits into

[vllm-project:main](https://github.com/vllm-project/guidellm/tree/main)

##
*base:*
main

Could not load branches

Branch not found:

**{{ refName }}**
Loading

Could not load tags

Nothing to show

Loading

### Are you sure you want to change the base?

Some commits from the old base branch may be removed from the timeline,
and old review comments may become outdated.

[cmiyai:docs/e2e-use-case-examples](https://github.com/cmiyai/guidellm/tree/docs/e2e-use-case-examples)

+316
−0

Open

## Changes from **all commits**

Commits

[
](https://github.com/vllm-project/guidellm/pull/1001/files)

Show all changes

4 commits
Select commit
Hold shift + click to select a range

##
**
File filter
**

### Filter by extension

## **Conversations**

Failed to load comments.

Loading

## **Jump to**

Jump to file

Failed to load files.

Loading

##### Diff view

##### Diff view

## There are no files selected for viewing

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)| Original file line number | Diff line number | Diff line change |
|---|---|---|
| @@ -0,0 +1,140 @@ | ||
| # Benchmarking Different Workload Shapes | ||
|
|
||
| Not all LLM workloads are the same. A chatbot, a summarization pipeline, and a code generator stress your server in completely different ways. This guide shows how to configure GuideLLM for specific workload type and explains why metrics behave differently. | ||
|
|
||
| ## Prerequisites | ||
|
|
||
| - A running OpenAI-compatible server ([setup guide](../getting-started/server.md)) | ||
| - GuideLLM installed ([install guide](../getting-started/install.md)) | ||
|
|
||
| ## Why Workload Shape Matters | ||
|
|
||
| LLM requests have two phases: | ||
|
|
||
| - **Prefill**: the server processes all input tokens at once. This determines time-to-first-token (TTFT). | ||
| - **Decode**: the server generates output tokens one at a time. This determines inter-token latency (ITL) and overall throughput. | ||
|
|
||
| The ratio of input to output tokens shifts which phase dominates. A workload with long prompts and short responses is prefill-bound. A workload with short prompts and long responses is decode-bound. Each has different bottlenecks and different metrics to watch. | ||
|
|
||
| ## The Four Common Shapes | ||
|
|
||
| **NOTE:** _Current workloads gear towards a **heavy prefill** (tokens in) due to multiple files, longer system prompts, multiturn etc... so these may not reflect real-world use cases. If you have custom workload, then configure these to your specific use-case_ | ||
|
|
||
| ### 1. Chat / Conversational | ||
|
|
||
| A user sends a short message and expects a medium-length response **(decode-bound)**. Typical of chatbots, customer support, and Q&A interfaces. | ||
|
|
||
| ```bash | ||
| guidellm run \ | ||
| --backend kind=openai_http,target=http://localhost:8000 \ | ||
| --data kind=synthetic_text,prompt_tokens=256,output_tokens=512 \ | ||
| --profile kind=sweep,sweep_size=10 \ | ||
| --constraint kind=max_duration,seconds=120 \ | ||
| --seed kind=static,value=42 \ | ||
| --output kind=json,path=chat_workload.json | ||
| ``` | ||
|
|
||
| **What to watch:** Both TTFT and ITL matter. Users are waiting for the response to start streaming (TTFT) and then reading it as it arrives (ITL). If either is too slow, the experience feels laggy. | ||
|
|
||
| ### 2. Summarization / RAG | ||
|
|
||
| A retrieval-augmented generation pipeline stuffs a large context into the prompt and expects a concise answer. Long input, short output. **(prefill-bound)** | ||
|
|
||
| ```bash | ||
| guidellm run \ | ||
| --backend kind=openai_http,target=http://localhost:8000 \ | ||
| --data kind=synthetic_text,prompt_tokens=2048,output_tokens=128 \ | ||
| --profile kind=sweep,sweep_size=10 \ | ||
| --constraint kind=max_duration,seconds=120 \ | ||
| --seed kind=static,value=42 \ | ||
| --output kind=json,path=summarization_workload.json | ||
| ``` | ||
|
|
||
| **What to watch:** TTFT dominates. The server spends most of its time processing the long prompt before generating a short answer. ITL matters less because there are so few output tokens. Throughput (tokens/sec) will look lower than chat because prefill is the bottleneck. | ||
|
|
||
| ### 3. Code Generation | ||
|
|
||
| A developer gives a short instruction and expects a long block of generated code. Short input, long output. **(prefill-bound)** | ||
|
|
||
| ```bash | ||
| guidellm run \ | ||
| --backend kind=openai_http,target=http://localhost:8000 \ | ||
| --data kind=synthetic_text,prompt_tokens=128,output_tokens=1024 \ | ||
| --profile kind=sweep,sweep_size=10 \ | ||
| --constraint kind=max_duration,seconds=120 \ | ||
| --seed kind=static,value=42 \ | ||
| --output kind=json,path=codegen_workload.json | ||
| ``` | ||
|
|
||
| **What to watch:** ITL dominates. TTFT will be fast (short prompt to prefill), but the server spends most of its time decoding a long output. High ITL means the code takes forever to stream in. Throughput (tokens/sec) is the key metric here. | ||
|
|
||
| ### 4. Balanced / General Purpose | ||
|
|
||
| Equal input and output lengths **(balanced)**. A good starting point when you are not sure what your workload looks like, or when you want a general performance baseline. | ||
|
|
||
| ```bash | ||
| guidellm run \ | ||
| --backend kind=openai_http,target=http://localhost:8000 \ | ||
| --data kind=synthetic_text,prompt_tokens=1000,output_tokens=1000 \ | ||
| --profile kind=sweep,sweep_size=10 \ | ||
| --constraint kind=max_duration,seconds=120 \ | ||
| --seed kind=static,value=42 \ | ||
| --output kind=json,path=balanced_workload.json | ||
| ``` | ||
|
|
||
| **What to watch:** Both phases contribute roughly equally. This gives the most balanced view of your server's capabilities but may not reflect your actual production workload. | ||
|
|
||
| ## Comparing Results Across Shapes | ||
|
|
||
| Run all four shapes on the same server and compare the results side by side. | ||
|
|
||
| **Recommended**: _Change shapes to your custom workload_ | ||
|
|
||
| | Workload | Tokens (in/out) | Throughput (tok/s) | TTFT p50 (ms) | ITL p50 (ms) | Bottleneck | | ||
| | ------------- | --------------- | ------------------ | ------------- | ------------ | -------------- | | ||
| | Chat | 256 / 512 | 1850 | 35 | 12 | Mixed | | ||
| | Summarization | 2048 / 128 | 920 | 180 | 9 | Prefill (TTFT) | | ||
| | Code gen | 128 / 1024 | 2100 | 18 | 14 | Decode (ITL) | | ||
| | Balanced | 1000 / 1000 | 1350 | 95 | 13 | Mixed | | ||
|
|
||
|
|
||
|
|
||
| Key observations: | ||
|
|
||
| - **Summarization has the highest TTFT** because the server processes 2048 input tokens before generating the first output token **(prefill-bound)**. But ITL is the lowest because there are very few tokens to decode. | ||
| - **Code gen has the highest throughput** because the short prompt prefills quickly, and the server spends most of its time in the efficient decode phase. But requests take the longest end-to-end because of 1024 output tokens. | ||
| - **Chat is the most balanced** — neither phase dominates, so both TTFT and ITL need to be within SLO. | ||
| - **Throughput numbers are not directly comparable** across shapes because total tokens per request differ. Use `output_tokens_per_second` for an apples-to-apples decode throughput comparison. | ||
|
|
||
| ## Choosing Your Benchmark Configuration | ||
|
|
||
| If you know your workload: | ||
|
|
||
| | Your application | Recommended config | Primary metric | | ||
| | ------------------------------ | --------------------------------------- | ---------------------- | | ||
| | Chatbot, Q&A | `prompt_tokens=256,output_tokens=512` | TTFT p99 and ITL p50 | | ||
| | RAG, summarization, search | `prompt_tokens=2048,output_tokens=128` | TTFT p99 | | ||
| | Code gen, writing, translation | `prompt_tokens=128,output_tokens=1024` | ITL p50 and throughput | | ||
| | Unknown or mixed | `prompt_tokens=1000,output_tokens=1000` | All metrics | | ||
|
|
||
| If you have real production data, use it instead of synthetic. GuideLLM supports custom datasets via JSONL files or HuggingFace datasets — see the [Datasets guide](../guides/datasets.md) for details. | ||
|
|
||
| ## Tuning Your Server for a Workload Shape | ||
|
|
||
| The benchmark results can guide server configuration: | ||
|
|
||
| **Prefill-bound (high TTFT):** | ||
|
|
||
| - Enable chunked prefill (`--enable-chunked-prefill`) to overlap prefill with decode | ||
| - Increase tensor parallelism to spread the prefill computation across GPUs | ||
| - Consider a shorter `--max-model-len` if your prompts don't need the full context window | ||
|
|
||
| **Decode-bound (high ITL):** | ||
|
|
||
| - Check if you are memory-bandwidth limited — larger batch sizes help divide memory reads | ||
| - Try quantized models (FP8, W4A16) to reduce memory bandwidth pressure | ||
| - Consider speculative decoding for latency-sensitive workloads | ||
|
|
||
| ## Next Steps | ||
|
|
||
| - [Finding Your Server's Optimal Concurrency Limit](optimal_concurrency.md) to optimize the load level for your chosen workload shape |

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)| Original file line number | Diff line number | Diff line change |
|---|---|---|
| @@ -0,0 +1,59 @@ | ||
| # [Title: What the user is trying to accomplish] | ||
|
|
||
| [One or two sentences describing the scenario and why someone would need this.] | ||
|
|
||
| ## Prerequisites | ||
|
|
||
| - A running OpenAI-compatible server ([setup guide](../getting-started/server.md)) | ||
| - GuideLLM installed ([install guide](../getting-started/install.md)) | ||
| - [Any additional prerequisites specific to this example] | ||
|
|
||
| ## Step 1: [Setup / Configure] | ||
|
|
||
| [Brief explanation of what this step does and why.] | ||
|
|
||
| ```bash | ||
| guidellm run \ | ||
| --backend kind=openai_http,target=http://localhost:8000 \ | ||
| --data kind=synthetic_text,prompt_tokens=___,output_tokens=___ \ | ||
| --profile kind=___,___=___ \ | ||
| --constraint kind=max_duration,seconds=___ \ | ||
| --seed kind=static,value=42 \ | ||
| --output kind=json,path=___.json | ||
| ``` | ||
|
|
||
| \[Explain what each non-obvious flag does in the context of this example. Don't repeat what the getting-started docs already cover. **Focus on why these specific values were chosen** for this use case.\] | ||
|
|
||
| ## Step 2: [Run / Execute] | ||
|
|
||
| [If the example requires multiple runs (e.g. comparing two configs), show the second command here. If it's a single run, this step is about what happens during execution — what to watch for in the console output.] | ||
|
|
||
| ## Step 3: [Interpret the Results] | ||
|
|
||
| [Explain how to interpret the metrics/results, highlighting what to take away (good and the bad)] | ||
|
|
||
| | Metric | What to look for | | ||
| | ------------- | ----------------------------------------------- | | ||
| | `metric_name` | [What a good/bad value means for this use case] | | ||
| | `metric_name` | [What a good/bad value means for this use case] | | ||
|
|
||
| ## Step 4: [Make a Decision / Take Action] | ||
|
|
||
| [How to go from the numbers to a concrete deployment decision. This separates an example from a reference doc.] | ||
|
|
||
| ## Example Output | ||
|
|
||
| [A realistic (ideally real) table or snippet showing what the results look like, with annotations pointing out the key takeaway.] | ||
|
|
||
| | Parameter | Value | Interpretation | | ||
| | --------- | ----- | -------------- | | ||
| | ... | ... | ... | | ||
|
|
||
| [One or two sentences summarizing the conclusion from this example data.] | ||
|
|
||
| ## Next Steps | ||
|
|
||
| [The user finds other helpful guides] | ||
|
|
||
| - [Link to relevant guide](../guides/relevant_guide.md) for deeper coverage of a feature used here | ||
| - [Link to another example](another_example.md) for a related workflow |

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)| Original file line number | Diff line number | Diff line change |
|---|---|---|
| @@ -0,0 +1,117 @@ | ||
| # Finding Your Server's Optimal Concurrency Limit | ||
|
|
||
| Determine the maximum number of concurrent users your LLM server can handle before latency degrades, and identify the optimal operating point for your deployment. | ||
|
|
||
| ## Prerequisites | ||
|
|
||
| - A running OpenAI-compatible server ([setup guide](../getting-started/server.md)) | ||
| - GuideLLM installed ([install guide](../getting-started/install.md)) | ||
| - How to run a benchmark ( [benchmark guide](../getting-started/benchmark.md)) | ||
|
|
||
| ## Step 1: Run a Sweep | ||
|
|
||
| The [`sweep`](https://docs.vllm.ai/en/stable/benchmarking/sweeps/) profile automatically tests increasing load levels — starting from a single sequential request, ramping up to maximum throughput, and interpolating several rates in between. It stops automatically when it detects the server is over-saturated. | ||
|
|
||
| ```bash | ||
| guidellm run \ | ||
| --backend kind=openai_http,target=http://localhost:8000 \ | ||
| --data kind=synthetic_text,prompt_tokens=512,output_tokens=256 # change this to your desired | ||
| --profile kind=sweep,sweep_size=10 \ | ||
| --constraint kind=max_duration,seconds=120 \ | ||
| --seed kind=static,value=42 \ | ||
| --output kind=json,path=sweep_results.json | ||
| ``` | ||
|
|
||
| This runs up to 10 strategies (synchronous baseline, throughput ceiling, and 8 interpolated rates) for 120 seconds each. The over-saturation detector will skip remaining strategies once the server can no longer keep up. | ||
|
|
||
| Adjust `prompt_tokens` and `output_tokens` to match your actual workload. A chat application might use `prompt_tokens=256,output_tokens=512`, while a summarization pipeline might use `prompt_tokens=2048,output_tokens=128`. | ||
|
|
||
| ## Step 2: Read the Results | ||
|
|
||
| Open the console output or JSON report. For each strategy, look at these metrics: | ||
|
|
||
| | Metric | What it tells you | | ||
| | --------------------------------- | ---------------------------------------------------------- | | ||
| | `output_tokens_per_second` (mean) | Server throughput — how much work is getting done | | ||
| | `time_to_first_token_ms` (p50) | Median user-perceived wait before they receive a response | | ||
| | `time_to_first_token_ms` (p99) | Worst-case wait — important for tail latency SLOs | | ||
| | `inter_token_latency_ms` (p50) | How smooth the streaming experience feels | | ||
| | `request_latency` (p50) | Total end-to-end time per request | | ||
cmiyai marked this conversation as resolved.
|
||
|
|
||
| ## Step 3: Identify the Three Zones | ||
|
|
||
| As load increases across the sweep strategies, your server will pass through three zones: | ||
|
|
||
| **Underutilized**: Throughput scales linearly with load. Latency stays flat. Adding more concurrent users makes the server do proportionally more work with no penalty. You are leaving capacity on the table. | ||
|
|
||
| **Sweet spot**: Throughput is still climbing but gains are shrinking. TTFT p50 is creeping up but still acceptable. The server is efficiently batching requests. **This is where you want to operate.** | ||
|
|
||
| **Over-saturated**: Throughput plateaus or drops. TTFT p99 spikes sharply. The request queue is growing faster than the server can handle. GuideLLM's over-saturation detector will stop the sweep here. | ||
|
|
||
| Look for the transition between the first and second zone — the point where TTFT p99 starts rising noticeably while throughput is still increasing. The strategy just before that transition is your optimal operating point. | ||
|
|
||
| ## Step 4: Validate with a Focused Run | ||
|
|
||
| Once you have identified a target concurrency (for example, 32 streams from the sweep results), run a longer benchmark at that specific level to confirm the metrics are stable: | ||
|
|
||
| ```bash | ||
| guidellm run \ | ||
| --backend kind=openai_http,target=http://localhost:8000 \ | ||
| --data kind=synthetic_text,prompt_tokens=512,output_tokens=256 \ | ||
| --profile kind=concurrent,streams=32 \ | ||
| --constraint kind=max_duration,seconds=300 \ | ||
| --seed kind=static,value=42 \ | ||
| --output kind=json,path=validation_run.json | ||
| ``` | ||
|
|
||
| A 5-minute run at fixed concurrency gives more reliable metrics than the shorter sweep strategies. Compare the validation results to what the sweep predicted — they should be consistent. If TTFT p99 is higher than expected, drop down one concurrency level and re-validate. | ||
|
|
||
| ## Step 5: Test Around the Boundary | ||
|
|
||
| To get a precise answer, run a few concurrency levels around your candidate: | ||
|
|
||
| ```bash | ||
| guidellm run \ | ||
| --backend kind=openai_http,target=http://localhost:8000 \ | ||
| --data kind=synthetic_text,prompt_tokens=512,output_tokens=256 \ | ||
| --profile kind=concurrent \ | ||
| --override profile.streams 24,28,32,36,40 \ | ||
| --constraint kind=max_duration,seconds=180 \ | ||
| --seed kind=static,value=42 \ | ||
| --output kind=json,path=boundary_test.json | ||
| ``` | ||
|
|
||
| This runs 5 sub-benchmarks at tightly spaced concurrency levels. Compare throughput and TTFT p99 across them to pinpoint exactly where the performance degrades. | ||
|
|
||
| ## Making the Decision | ||
|
|
||
| How you pick the final number depends on your deployment goal: | ||
|
|
||
| **Latency-sensitive (chat, real-time)**: Choose the highest concurrency where TTFT p99 stays under your SLO. If your SLO is 500ms TTFT, and TTFT p99 at 32 streams is 480ms but at 36 streams is 720ms, run at 32. | ||
|
|
||
| **Throughput-optimized (batch, offline)**: Choose the concurrency where `output_tokens_per_second` plateaus. Latency matters less here, so you can push further into the sweet spot. | ||
|
|
||
| **Production with headroom**: Take your chosen concurrency and multiply by 0.8. If your sweet spot is 40 streams, operate at 32. This gives room for traffic spikes without hitting over-saturation. | ||
|
|
||
| ## Example: Interpreting a Sweep | ||
|
|
||
| Here is what a real sweep looks like. | ||
|
|
||
| Results collected using **meta-llama/Llama-3.1-8B-Instruct** on a single **NVIDIA A100 80GB** GPU, served by vLLM with chunked prefill enabled. Workload: 1000 input tokens, 1000 output tokens. | ||
|
|
||
| | Strategy | Concurrency (mean) | Req/s (mean) | Output Tokens/s | TTFT p50 (ms) | TTFT p95 (ms) | ITL p50 (ms) | ITL p95 (ms) | Zone | | ||
| | ----------- | ------------------ | ------------ | --------------- | ------------- | ------------- | ------------ | ------------ | -------------- | | ||
| | synchronous | 1.0 | 0.1 | 90.2 | 79.5 | 115.2 | 11.0 | 11.1 | Under-utilized | | ||
| | constant | 3.8 | 0.3 | 327.7 | 95.0 | 100.1 | 11.5 | 11.6 | Under-utilized | | ||
| | constant | 7.1 | 0.5 | 569.7 | 97.7 | 102.8 | 12.3 | 12.4 | Under-utilized | | ||
| | constant | 10.8 | 0.8 | 809.4 | 100.4 | 105.8 | 13.3 | 13.4 | Under-utilized | | ||
| | constant | 14.7 | 1.0 | 1047.9 | 100.4 | 108.4 | 14.0 | 14.1 | Sweet spot | | ||
| | constant | 21.0 | 1.2 | 1274.9 | 107.8 | 115.9 | 16.6 | 16.7 | Sweet spot | | ||
| | constant | 27.8 | 1.4 | 1496.5 | 117.7 | 126.6 | 19.2 | 19.3 | Sweet spot | | ||
| | constant | 33.7 | 1.6 | 1728.6 | 123.5 | 133.9 | 19.8 | 19.9 | Sweet spot | | ||
| | constant | 46.0 | 1.7 | 1911.7 | 132.6 | 146.6 | 25.0 | 25.5 | Over-saturated | | ||
| | throughput | 509.8 | 2.1 | 3217.6 | 9947.7 | 21961.3 | 84.1 | 106.8 | Over-saturated | | ||
|
|
||
| In this example, throughput scales linearly from concurrency 1 through ~11 (under-utilized). Between concurrency 15 and 34, throughput is still climbing but TTFT and ITL are creeping up (sweet spot). At concurrency 46, throughput gains flatten while latency continues rising — and the throughput strategy shows TTFT exploding to ~10 seconds, confirming over-saturation. | ||
|
|
||
| The optimal operating point here is around **concurrency 28-34** — throughput is near 1500-1700 tok/s with TTFT p50 still under 135ms and ITL under 20ms. For production with headroom, target concurrency 24-28. |

Oops, something went wrong.

Add this suggestion to a batch that can be applied as a single commit.
This suggestion is invalid because no changes were made to the code.
Suggestions cannot be applied while the pull request is closed.
Suggestions cannot be applied while viewing a subset of changes.
Only one suggestion per line can be applied in a batch.
Add this suggestion to a batch that can be applied as a single commit.
Applying suggestions on deleted lines is not supported.
You must change the existing code in this line in order to create a valid suggestion.
Outdated suggestions cannot be applied.
This suggestion has been applied or marked resolved.
Suggestions cannot be applied from pending reviews.
Suggestions cannot be applied on multi-line comments.
Suggestions cannot be applied while the pull request is queued to merge.
Suggestion cannot be applied right now. Please check back later.

cmiyaimarked this conversation as resolved.## Uh oh!

There was an error while loading. Please reload this page.