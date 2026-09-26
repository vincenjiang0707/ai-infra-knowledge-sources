source: https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/advanced-platform/shadow-engine-failover
lastmod: 2026-09-24T19:58:16.636Z

# Shadow Engine Failover

Keeps a standby engine attached to GPU-resident model weights so process failures recover without reloading the model.

⚠️

Experimental Feature: Shadow Engine Failover is an opt-in preview feature. It depends on GPU Memory Service (GMS), Dynamic Resource Allocation (DRA), and backend-specific support. Its API shape and behavior may change, and the failover state machine is still settling. Use it only for non-production evaluation unless you have validated the exact backend, topology, and failure mode in your cluster.

## Overview

Use Shadow Engine Failover when you want a standby engine to take over after an unknown backend engine or software-process failure while the GPU and node remain healthy. The goal is to avoid paying a full model weight reload after a same-node process failure.

Shadow Engine Failover is the Kubernetes workflow. GPU Memory Service is the enabling mechanism underneath it: GMS owns the GPU-resident model weights, and the active and standby engines attach to those weights through DRA.

This is separate from [Dynamo Snapshot](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/advanced-platform/snapshot). Snapshot captures and
restores a process image with CRIU and `cuda-checkpoint`

. Shadow Engine Failover
keeps model weights resident in GPU memory so a standby or replacement engine
can attach after selected process-level failures. They both target recovery
latency, but they solve different problems and are not interchangeable.

## Failure Recovery Flow

The following diagram illustrates same-node process-level recovery:

**How it works:**

- The operator creates active and standby engine containers or pods for the worker, depending on the selected failover mode.
- The engines share GPU access through DRA and attach to model weights owned by GMS.
- An unknown software or engine failure terminates the active engine, while the GMS process, GPU, and node remain healthy.
- The standby or replacement engine takes over and attaches to the resident GMS-owned weights instead of performing a full weight reload.
- In-flight requests and KV cache state are not preserved. If the GPU, node, or GMS process is lost, the replacement worker must use the normal rescheduling and model-load path.

## When to Use It Today

- Use it to evaluate same-node recovery from unknown vLLM engine or software-process failures.
- Use it when the cost you are trying to avoid is loading another independent copy of model weights into GPU memory.
- Use the GMS-only examples to validate backend weight loading through GMS, not as a complete failover workflow.
- Do not use it for hardware failure, GPU loss, node loss, cross-node recovery, in-flight request recovery, or KV-cache recovery.
- Do not combine it with Snapshot restore. Snapshot plus GMS is not yet available.

## GPU Memory Service

GMS moves ownership of GPU-resident model weights out of the engine process and into a separate GPU memory service. In the failover workflow, this lets the active and standby engines share the same weight memory boundary instead of loading independent copies.

Direct GMS enablement is useful for backend integration testing and
pause/resume-style lifecycle experiments. By itself, it does not configure
active/passive failover; use the `failover`

field for the shadow engine flow.

## Prerequisites

- Kubernetes 1.34 or newer with DRA v1 (
`resource.k8s.io/v1`

) enabled. - NVIDIA GPU DRA driver installed.
- A matching DRA
`DeviceClass`

, defaulting to`gpu.nvidia.com`

. - A supported backend image. The current failover examples are vLLM-focused.
- Backend command-line support for GMS loading, such as
`--load-format gms`

. - Enough GPU memory for the GMS processes and active or standby engines sharing the device.

## Limitations

- It is not a general checkpoint/restore system.
- It is not a hardware fault tolerance mechanism for GPU, node, or rack loss.
- It does not diagnose or fix the backend failure.
- It does not preserve in-flight requests, network sockets, or KV cache state.
- It does not make Snapshot restore supported for GPU memory workloads.
- Snapshot plus GMS is temporarily blocked by admission because of known GPU driver restore issues.
- It is not covered by the normal v1beta1 compatibility guarantees while it
lives under
`experimental`

.

## API Placement

For `v1alpha1`

`DynamoGraphDeployment`

, GMS and failover are service-level
fields:

For `v1beta1`

, preview fields are grouped under `experimental`

to make the
stability contract explicit:

See the [API reference](https://docs.nvidia.com/dynamo/v1.3.0/additional-resources/api-reference-k-8-s) for the exact schema supported by your
CRD version.

## Basic Shadow Engine Failover Example

Failover builds on GMS. In intra-pod mode, the operator clones the worker’s main container into active and standby engine containers that share GPUs through DRA and the GMS sidecar. The standby engine takes over when the active engine fails.

See the [vLLM failover example](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/examples/backends/vllm/deploy/agg_failover.yaml)
for the full manifest.

## Basic GMS Example

The worker must request GPUs through the normal Dynamo service resources, enable
`gpuMemoryService`

, and run a backend command that can load from GMS.

Working GMS-only examples: