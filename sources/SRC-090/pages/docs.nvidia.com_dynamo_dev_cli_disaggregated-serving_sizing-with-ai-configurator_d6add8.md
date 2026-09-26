source: https://docs.nvidia.com/dynamo/dev/cli/disaggregated-serving/sizing-with-ai-configurator
lastmod: 2026-09-24T19:58:16.636Z

# Size a Local Deployment with AIConfigurator

AIConfigurator estimates inference performance across candidate parallelism and deployment layouts. Use it before launching a local Dynamo deployment to choose tensor parallelism (TP), pipeline parallelism (PP), and the number of worker replicas to validate.

AIConfigurator is an analytical performance model and configuration optimizer. It does not start a
Dynamo frontend, simulate request-by-request scheduler or KV-cache behavior, or benchmark a live
endpoint. Use [Mocker Live Simulation](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/local-mocker)
to exercise a live frontend and simulated workers, [DynoSim Replay](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/simulation-runs)
for request-level offline simulation, and
[Benchmarking with AIPerf](https://docs.nvidia.com/dynamo/dev/cli/operations/benchmarking-with-ai-perf) for measurements against the running local endpoint.

## Prerequisites

Use Python 3.11 through 3.13. Install AISimulate, which provides the retained `aiconfigurator`

sizing command:

Collect:

- the model ID or local checkpoint path
- the backend and backend version
- the GPU system
- the total GPU budget
- typical input and output sequence lengths
- Time to First Token (TTFT) and Time Per Output Token (TPOT) targets

Confirm that AIConfigurator supports the combination:

### Generate candidate configurations

Run the optimizer with the local GPU budget and workload targets:

`--total-gpus`

is the budget available to the local deployment. The selected system definition
provides the assumed GPUs per node and communication characteristics. AIConfigurator does not inspect
which GPUs or nodes are currently free.

### Apply a recommendation

Choose a highly ranked row that meets the SLA. Translate its output into the local worker launch:

For example, apply a `tp4pp1`

recommendation to a vLLM worker:

Start additional replicas on separate GPU sets when the recommendation calls for them. All replicas
register with the same frontend. For backend-specific arguments, see the local deployment examples
for [vLLM](https://docs.nvidia.com/dynamo/dev/recipes/cli-templates/v-llm),
[SGLang](https://docs.nvidia.com/dynamo/dev/recipes/cli-templates/sg-lang), and
[TensorRT-LLM](https://docs.nvidia.com/dynamo/dev/recipes/cli-templates/tensor-rt-llm).

If one worker requires more GPUs than a node provides, use a
[Kubernetes multinode deployment](https://docs.nvidia.com/dynamo/dev/kubernetes/installation/multinode-orchestration) instead of treating the GPU budget as one flat local device list.

### Validate the recommendation

AIConfigurator narrows the configurations to test; it does not replace measurement. Launch the
recommended local deployment and use [Benchmarking with AIPerf](https://docs.nvidia.com/dynamo/dev/cli/operations/benchmarking-with-ai-perf) to validate latency and
throughput on the target hardware.

For aggregated versus disaggregated analysis, generated artifacts, output fields, and advanced
options, see the [AIConfigurator Reference](https://docs.nvidia.com/dynamo/dev/additional-resources/ai-configurator-reference).