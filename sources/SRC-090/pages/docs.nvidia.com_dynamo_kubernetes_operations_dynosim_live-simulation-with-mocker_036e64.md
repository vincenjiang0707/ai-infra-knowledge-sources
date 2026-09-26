source: https://docs.nvidia.com/dynamo/kubernetes/operations/dynosim/live-simulation-with-mocker
lastmod: 2026-09-25T12:26:00.485Z

# Simulate a Kubernetes Deployment with Mocker

Mocker is a simulated Dynamo backend. It registers workers, publishes KV events, and returns mock responses while exercising the same frontend and routing path as a model-serving deployment.

Use this tutorial to deploy Mocker with a `DynamoGraphDeployment`

(DGD). For local development, see
[Simulate a Local Deployment](https://docs.nvidia.com/dynamo/cli/operations/dynosim/mocker-live-simulation). For configuration details, see the
[Mocker CLI Reference](https://docs.nvidia.com/dynamo/reference/components/mocker-cli-reference). For implementation details,
see [Mocker Engine Architecture](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/mocker/mocker-engine-architecture).

## Prerequisites

Before you begin:

- Install the Dynamo Kubernetes Platform.
- Set
`NAMESPACE`

to the namespace where you deploy Dynamo resources. - Set
`PLANNER_IMAGE`

to a released or locally built`dynamo-planner`

image. - Configure cluster access with
`kubectl`

.

Mocker runs in the planner image and does not request GPU resources.

### Deploy an aggregated simulation

Create `mocker-agg.yaml`

:

Replace `${PLANNER_IMAGE}`

with the image URI, and then apply the DGD:

The checked-in
[aggregated Mocker example](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/examples/backends/mocker/deploy/agg.yaml)
contains the complete deployment manifest.

### Send a request

Forward the frontend service to port 8000:

In another terminal, send an OpenAI-compatible request:

A successful response confirms that the frontend discovered the Mocker worker and routed the request through the deployment.

### Simulate disaggregated serving

Start from the checked-in
[disaggregated Mocker example](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/examples/backends/mocker/deploy/disagg.yaml).
It defines separate prefill and decode components. The prefill worker uses:

The decode worker uses:

Apply the manifest, repeat the port-forward and request steps, and inspect the worker logs:

Use the logs to confirm that both worker stages registered and that requests moved from prefill to decode.

### Try another simulation

Change one setting at a time and repeat the request:

- Increase
`replicas`

to exercise routing across more workers. - Add Mocker scheduling or KV-cache flags from the
[Mocker CLI Reference](https://docs.nvidia.com/dynamo/reference/components/mocker-cli-reference). - Enable the Planner to test scaling behavior with simulated workers.
- Compare the simulation with a real-GPU deployment by using
[Benchmarking with AIPerf](https://docs.nvidia.com/dynamo/kubernetes/operations/benchmarking-with-ai-perf).

DynoSim helps test control-plane behavior and shortlist configurations. Validate performance conclusions on the target GPU hardware before production use.