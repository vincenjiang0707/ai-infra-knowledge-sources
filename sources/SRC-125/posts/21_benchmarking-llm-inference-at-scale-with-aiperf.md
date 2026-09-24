# benchmarking-llm-inference-at-scale-with-aiperf

source: https://developer.nvidia.com/blog/benchmarking-llm-inference-at-scale-with-aiperf/

You’re deploying a model on a system. It starts up, prompts are getting responses. Now the hard question: Is this fast?

Your instincts might lead you to send curl commands, hand-roll an asyncio script, or vibe code yet another one-off load generator. All of these paths have the same problem: single-process performance limits, Python’s GIL capping concurrency, or numbers measured against a reference you built yourself. Either way, you end up with results you can’t fully trust, attached to tooling you’ll have to rewrite the moment requirements change.

What you need is a load client that can saturate a real server without becoming the bottleneck, produce output you can act on, and take five minutes to configure, not five hours. That’s NVIDIA AIPerf.

## What AIPerf does differently

AIPerf is the designated successor to GenAI-Perf and is a ground-up rewrite. The design choices reflect hard lessons from running LLM benchmarks at scale:

**A clean break from the old architecture.**AIPerf doesn’t run on top of Perf Analyzer the way GenAI-Perf did. It’s a clean architectural break and the reason AIPerf can scale the way it does. If you’re porting an existing workflow, the[migration guide](https://github.com/ai-dynamo/aiperf/blob/main/docs/migrating.md)covers the key deltas.**The client shouldn’t be the bottleneck.**Most benchmarkers, GenAI-Perf included, use a single-process architecture that becomes GIL-bound under real concurrency or request rate. AIPerf is a multiprocessed system: worker processes generate load, separate record-processor services handle results, and everything is coordinated over ZMQ.. This structure allows for more accurate server benchmarking by preventing AIPerf from becoming a client-side bottleneck.**Workload breadth that matches what you actually run.**AIPerf supports 15+ endpoint types: chat, responses, NIM rankings, image generation, and more — along with public datasets like ShareGPT and trace replay formats from Mooncake, Baseten, WEKA (AgentX), and others. Whether you’re running a quick synthetic smoke test or replaying captured production traffic, you don’t need a different tool.**Load shape you actually control.**AIPerf supports constant, Poisson, and gamma arrival patterns with tunable burstiness, gradual ramping for concurrency and request rate, and synthetic distributions including vLLM/SGLang range-ratio for variable ISL/OSL. You control the shape of the load, not just the volume.

## Your maiden benchmark: Synthetic ISL/OSL on vLLM

For this walkthrough we’ll use Qwen3-0.6B served through vLLM. The model choice is deliberate; it’s small enough to run on a single GPU and fast enough to iterate on without waiting. The point isn’t to benchmark Qwen3-0.6B specifically; it’s to establish the measurement loop. Once you have that, swapping in a different model or endpoint is a one-flag change.

**Start the Server**

Pull and start vLLM with the reasoning parser enabled:

`docker pull vllm` `/vllm-openai` `:latest` `docker run --gpus all -p 8000:8000 -e HF_TOKEN vllm` `/vllm-openai` `:latest \` ` ` `--model Qwen` `/Qwen3-0` `.6B \` ` ` `--reasoning-parser qwen3 \` ` ` `--host 0.0.0.0 --port 8000` |

## Install AIPerf

We can use uv to install a central copy:

`uv tool ` `install` `aiperf` |


Or for a virtual environment:

`uv venv venv` `source` `venv` `/bin/activate` `uv pip ` `install` `aiperf` |

One platform note: on aarch64, the `crick`

dependency ships as source-only and requires a C toolchain (`build-essential`

on Debian/Ubuntu, `Development Tools`

on RHEL). If the install stalls on that package, that’s why.

## Running the benchmark

With the server up and AIPerf installed, we can now run our first profile:

`aiperf profile \` ` ` `--model Qwen` `/Qwen3-0` `.6B \` ` ` `--endpoint-` `type` `chat \` ` ` `--streaming \` ` ` `--url localhost:8000 \` ` ` `--synthetic-input-tokens-mean 128 \` ` ` `--synthetic-input-tokens-stddev 0 \` ` ` `--output-tokens-mean 128 \` ` ` `--output-tokens-stddev 0 \` ` ` `--extra-inputs min_tokens:128 \` ` ` `--extra-inputs ignore_eos:` `true` |

A few flags here are doing more work than they look like:

`--synthetic-input-tokens-stddev 0`

and `--output-tokens-stddev 0`

pin the workload to exactly 128 input and 128 output tokens per request. This reproduces a commonly used static benchmark that holds request and output lengths constant.

`--extra-inputs min_tokens:128`

and `--extra-inputs ignore_eos:true`

tell the model to actually emit 128 tokens rather than stopping early. Without these, the output token count is a suggestion. The model stops whenever it naturally finishes, which can be well short of your target OSL. Throughput numbers end up lower than they should be, and they’re not reproducible across runs.

`--streaming`

is not optional if you want to measure TTFT and ITL. Without streaming, the server batches the full response before sending it, and there are no first- or decode-token events to measure.

## What you’ll see

We’ll walk through how to read these numbers in the next section. For now, notice the shape of the output in Figure 2, below: latency broken down by percentile, throughput in tokens per second, and request-level statistics all in one place. That’s the baseline you’ll be comparing everything else against.

## Reading the numbers: What AIPerf surfaces

Once a run completes, AIPerf prints a metrics table to the console and writes the full results to CSV and JSON. Here’s what you’re looking at.

**The core four:**

**TTFT (Time to First Token)**— How long from request sent to first token received. The primary latency signal for interactive use cases.**ITL (Inter-Token Latency)**— Time between successive tokens during generation. High ITL means the decode phase is struggling, even if TTFT looks healthy.**Request Latency**— End-to-end time for the full response. Combines prefill and decode cost into a single number.**Output Token Throughput**— Tokens generated per second across all concurrent requests. The primary throughput signal for capacity planning.

For full definitions of these and every other metric AIPerf reports, see the[ Metrics Reference](https://github.com/ai-dynamo/aiperf/blob/main/docs/metrics-reference.md).

**Getting the full picture.** Each of the above is reported in percentile breakdowns (p25, p50, p75, p90, p95, p99) alongside their minimums, maximums, averages, and standard deviations. These breakdowns matter because they can highlight long tail distributions; a server with a healthy mean TTFT and an outlier p99 looks fine in aggregate and fails in production.

**Beyond the core four.** With DCGM or pynvml available, AIPerf also pulls GPU power draw, utilization, and memory consumption into the same run output. Correlating a latency spike with a memory pressure event doesn’t require a separate profiling session, the telemetry is already there.

## Going further: Configuring a traffic pattern

Now that our feet are wet with a static benchmark, we can start exploring something more dynamic. The section above provided an extremely fixed traffic pattern, but real inference traffic doesn’t follow a static pattern. To benchmark with a scenario that’s less rigid, we can use some of AIPerf’s synthetic workload knobs to introduce variability to our requests.

`aiperf profile \` ` ` `--model Qwen` `/Qwen3-0` `.6B \` ` ` `--endpoint-` `type` `chat \` ` ` `--streaming \` ` ` `--url localhost:8000 \` ` ` `--request-rate 10 \` ` ` `--arrival-pattern poisson \` ` ` `--synthetic-input-tokens-mean 512 \` ` ` `--synthetic-input-tokens-stddev 128 \` ` ` `--output-tokens-mean 128 \` ` ` `--output-tokens-stddev 32 \` ` ` `--random-seed 42 \` ` ` `--request-count 200` |

A few things changed from the static benchmark above.

`--arrival-pattern poisson`

with `--request-rate 10`

means requests arrive at an average of 10 per second, with inter-arrival times drawn from an exponential distribution. The server now experiences bursts and gaps rather than a single user stream, which is what queuing actually looks like under real traffic.

`--synthetic-input-tokens-stddev 128`

introduces variance around the 512-token mean, producing a mix of short and long prompts. The server has to handle variable prompt lengths during prefill rather than identical ones.

`--output-tokens-stddev 32`

adds variance on the output side. Notice that `min_tokens`

and `ignore_eos`

are gone from this command. In the static benchmark those flags pinned outputs to exactly 128 tokens to keep the baseline clean; we’re deliberately releasing that constraint so the output distribution can vary.

`--random-seed 42`

makes the Poisson timing and synthetic length draws reproducible. Rerunning this command produces the same sequence of requests.

`--streaming`

is not optional. Without streaming, the server batches the full response before sending it, and there’s no first- or decode-token events to measure.

Looking at the LLM metrics from this run, the distributions are noticeably wider than the static baseline — which is expected when more requests are simultaneously competing for GPU access and prefill lengths vary per request.

Looking at the graphs in Figure 4, below, you can see that the Poisson command line introduced a request rate centered, but not exactly matching, around 10 requests/second. This arrival rate emulates jitter around when requests arrive compared to the constant mode which guarantees a fixed 10 requests/second.

You can see in Figure 5, below, that there is a variation in the request length centered around the mean of 512 tokens, with input sequence lengths ranging 154 to 818 tokens.

Comparing TTFT between the two runs, you can see that the Poisson run shows a much wider spread. More requests are simultaneously competing for GPU access, prefill lengths vary, and prefill and decode operations overlap. The single-concurrency case is an idealized scenario which runs one request at a time presenting the lowest possible TTFT, at the cost of throughput.

In Figure 6, above, you can see that the single user run experiences less TTFT variability than the much more varied workload in the Poisson experiment.

## There’s more to explore

This walkthrough covers the basics, but AIPerf is also built for more complex scenarios.

The same tool handles [multi-node Kubernetes deployments](https://github.com/ai-dynamo/aiperf/tree/main/docs/kubernetes), [KV cache reuse warm up mechanics](https://github.com/ai-dynamo/aiperf/blob/main/docs/reference/cache-bust.md), trace replay from production traffic, prefix synthesis, custom datasets, and sweep configurations across concurrency levels.

If you’re running distributed inference at scale, see[ How NVIDIA Dynamo 1.0 Powers Multi-Node Inference at Production Scale](https://developer.nvidia.com/blog/nvidia-dynamo-1-production-ready/).

The[ tutorials in the AIPerf repo](https://github.com/ai-dynamo/aiperf/tree/main/docs/tutorials) are the fastest way in. The[ AIPerf repo](https://github.com/ai-dynamo/aiperf) and[ docs](https://docs.nvidia.com/aiperf) are the canonical reference for new features and contributions.

### Acknowledgments

*AIPerf is a collaborative effort between NVIDIA and external contributors. Thank you to the following: Loki Ravi, Dan Ferguson, and Sheng Moua (AWS) for the continual collaboration, cross-company validation, and efforts to standardize on AIPerf; Aaron Batilo (Coreweave) for the Weights & Biases exporter, acceptance-length spec-decode datasets, and hardening sweep/credit-dispatch reliability under concurrency; Shounak Ray (Baseten) for faithful Baseten trace replay support; Michael Feil (Baseten) for faster trace loading, and session affinity headers. Cristian Lopez (Pinterest) for his close collaboration on the DAG benchmarking methodology. We’re grateful to Ben Hamm for his product guidance while we designed, planned, and implemented AIPerf.*

## Start the discussion at forums.developer.nvidia.com
