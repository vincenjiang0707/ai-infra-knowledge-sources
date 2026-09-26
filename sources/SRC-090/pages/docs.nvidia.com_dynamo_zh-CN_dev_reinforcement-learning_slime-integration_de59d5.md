source: https://docs.nvidia.com/dynamo/zh-CN/dev/reinforcement-learning/slime-integration
lastmod: 2026-09-23T23:30:39.914Z

# Slime Integration

**Experimental.** This integration connects Slime to a fixed set of SGLang engines that a DynamoGraphDeployment manages.

Slime sends rollout generation through the Dynamo frontend. It sends control and weight-update requests to each SGLang engine.

## Integration Shape

Slime starts an SGLang router to track the external engines. The custom generator sends rollout requests to the Dynamo frontend instead.

The Slime external-engine support lives in the upstream Slime repository. The Dynamo-specific deployment files live in the Dynamo example.

## Prerequisites

- Install the
[Dynamo Kubernetes Platform](https://docs.nvidia.com/dynamo/dev/kubernetes/installation/install-dynamo)on a GPU cluster. - Install the NVIDIA device plugin for the
`nvidia.com/gpu`

resource. - Install
`kubectl`

and`envsubst`

on the deployment host. - Select matching Dynamo frontend and SGLang runtime image versions.
- Allocate two GPUs for the SGLang workers.
- Allocate the additional resources that the Slime training job requires.
- Use a Slime revision that includes
[THUDM/slime#2272](https://github.com/THUDM/slime/pull/2272).

## Prepare the Source

Clone the Slime merge commit that added streaming external rollouts:

Install Slime with the [upstream instructions](https://github.com/THUDM/slime/blob/4c1ab40203952b3dcc8582b653f3a83f2c6e8128/README.md). Keep the checkout path for `SLIME_HOME`

.

Clone Dynamo to get the deployment example:

## Deploy the Worker Set

Set the Dynamo images to the same version. The deployment uses `Qwen/Qwen3-0.6B`

by default.

Each worker Pod runs SGLang and loads `dynamo.sglang.sidecar`

through the SGLang `--sidecar`

option.

The manifest creates these Services:

`slime-sglang-rollout:8000`

exposes the Dynamo frontend.`slime-sglang-engine-0:30000`

exposes the first native SGLang API.`slime-sglang-engine-1:30000`

exposes the second native SGLang API.

Each engine Service selects one worker component. Keep each worker component at one replica.

Restrict access to the engine Services. These Services expose administrative and weight-update APIs.

## Make Sure That the Engines Are Ready

Run these commands from the Slime environment or another Pod in the deployment namespace:

The first two commands show that the SGLang engines are ready. The third command shows that the Dynamo frontend is ready.

## Run Slime

Set the fixed engine addresses and the Dynamo frontend address. Then add the arguments that your training workload requires.

The launcher passes the fixed worker list to Slime. It also enables incremental streaming output.

The `dynamo_generate.generate_streaming`

adapter sends generation to `DYNAMO_ROLLOUT_URL`

. Slime calls each fixed engine for control operations and weight updates.

## Make Sure That the Integration Works

Complete these steps before you increase the workload size:

- Run one rollout with the selected model and weight transport.
- Apply one policy update to both engines.
- Run one rollout after the update.
- Stop one worker during a test run.
- Make sure that Slime stops or reports the worker failure.
- Restart the Slime job after Kubernetes replaces the worker Pod.

The integration does not recover a replaced external engine during a Slime job.

## Current Limitations

- The example uses a fixed worker set.
- The example does not support dynamic endpoint registration.
- Slime must restart after Kubernetes replaces an engine Pod.
- The native engine Services require network isolation.
- The example does not provide a fleet-wide policy-update transaction or automatic rollback.