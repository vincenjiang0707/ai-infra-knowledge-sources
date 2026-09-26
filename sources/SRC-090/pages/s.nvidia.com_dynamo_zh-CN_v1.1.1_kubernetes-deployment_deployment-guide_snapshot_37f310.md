source: https://docs.nvidia.com/dynamo/zh-CN/v1.1.1/kubernetes-deployment/deployment-guide/snapshot
lastmod: 2026-09-23T23:30:39.914Z

# Snapshot

⚠️

Experimental Feature: Dynamo Snapshot is currently in preview and may only be functional in some cluster setups. The`snapshot-agent`

DaemonSet runs in privileged mode to perform CRIU operations. See[Limitations]for details.

**Dynamo Snapshot** is infrastructure for fast-starting GPU applications in Kubernetes using CRIU (Checkpoint/Restore in Userspace) and NVIDIA’s `cuda-checkpoint`

utility. The usual flow is:

- start a worker once and checkpoint its initialized state
- store that checkpoint on a namespace-local snapshot volume
- restore later workers from that checkpoint instead of cold-starting again

⚠️ Restore time depends on storage bandwidth, GPU model, and whether the restore stays on the same node.


## Prerequisites

- x86_64 (
`amd64`

) GPU nodes - NVIDIA driver 580.xx or newer on the target GPU nodes (590.xx or newer if testing multi-GPU snapshots)
- vLLM backend today, with limited preview support
`ReadWriteMany`

storage for cross-node restore**CRI-O / OpenShift:**set`runtime.type=crio`

on the snapshot chart (and`openshift.enabled=true`

on OpenShift). Defaults are for containerd; see the chart README for sockets and Helm flags.

## Quick Start via `DynamoCheckpoint`

CR

- Build a placeholder image
- Install the snapshot chart
- Create a
`DynamoCheckpoint`

and wait for it to become ready - Deploy a
`DynamoGraphDeployment`

that restores from the corresponding`checkpointRef`


### 1. Build and push a placeholder image

Snapshot-enabled workers must use a placeholder image that wraps the normal runtime image with restore tooling. If you do not already have one, build it and push it to a registry your cluster can pull from:

The placeholder image preserves the normal runtime entrypoint/command contract and adds the `criu`

, `cuda-checkpoint`

, and `nsrestore`

tooling needed for checkpoint and restore.

To build either snapshot image against a custom CRIU fork or ref, pass
`CRIU_REPO`

and `CRIU_REF`

through `make`

. If they are unset, the Dockerfile
defaults are used.

### 2. Enable checkpointing in the platform and verify it

Whether you are installing or upgrading `dynamo-platform`

, the operator only needs checkpointing enabled:

If the platform is already installed, verify that the operator config contains the checkpoint block:

Verify that the rendered config includes `enabled: true`

.

### 3. Install the snapshot chart in the workload namespace

Cross-node restore requires shared `ReadWriteMany`

storage. The chart defaults to that mode. If your cluster does not have a default storage class, also set `storage.pvc.storageClass`

.

If you are reusing an existing checkpoint PVC, do not set `storage.pvc.create=true`

; install the chart with `storage.pvc.create=false`

and set `storage.pvc.name`

instead.

CRI-O or OpenShift: append for example `--set runtime.type=crio`

and, on OpenShift, `--set openshift.enabled=true`

(see `deploy/helm/charts/snapshot/README.md`

).

Verify that the PVC and DaemonSet are ready:

### 4. Create a `DynamoCheckpoint`


The checkpoint Job pod template should match the worker container you want to checkpoint. For the snapshot flow, the important parts are the checkpoint identity, a container named `main`

, and the placeholder image; the rest of the pod template should mirror your normal worker config. Extra containers are allowed, but only `main`

is checkpointed.

Leave `spec.gpuMemoryService.enabled`

unset or `false`

. Snapshot plus GPU Memory Service is not yet available, and admission rejects `DynamoCheckpoint`

objects with `spec.gpuMemoryService.enabled: true`

. See [Shadow Engine Failover](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/shadow-engine-failover) for the current GMS support status.

For a full working example, see [deploy/operator/config/samples/nvidia.com_v1alpha1_dynamocheckpoint.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.1.1/deploy/operator/config/samples/nvidia.com_v1alpha1_dynamocheckpoint.yaml).

Apply it:

### 5. Wait for the checkpoint to become ready

The useful status fields are:

`status.phase`

: high-level lifecycle (`Pending`

,`Creating`

,`Ready`

,`Failed`

)`status.identityHash`

: deterministic hash of`spec.identity`

`status.jobName`

: checkpoint Job name`status.createdAt`

: timestamp recorded when the checkpoint became ready`status.message`

: progress or failure detail when available

### 6. Deploy a `DynamoGraphDeployment`

that restores from `checkpointRef`


Once the checkpoint is `Ready`

, restore a worker from it explicitly:

Apply it:

The `VllmDecodeWorker`

pod should restore from the ready checkpoint instead of creating a new one.

## DGD Auto Flow

`checkpointRef`

is the most explicit path. `mode: Auto`

is the higher-level path: the operator computes the checkpoint identity hash, looks for an equivalent `DynamoCheckpoint`

, and creates one only when no matching checkpoint exists. If a `DynamoCheckpoint`

already exists with the same identity, Auto mode reuses it. If no matching checkpoint exists yet, the first worker cold-starts and the operator creates the checkpoint in the background.

Inside a `DynamoGraphDeployment`

, it looks like this:

Auto mode only hashes `checkpoint.identity`

. GMS-specific checkpoint behavior is not yet available.

Useful inspection commands:

If you want to force a new restore after the checkpoint becomes ready, scale the worker:

## Failover Restore

Failover restore is not yet available. The current Snapshot flow does not support Snapshot plus GMS, so do not use failover restore as a supported checkpoint/restore path. For current GMS and active/passive failover guidance, see [Shadow Engine Failover](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/shadow-engine-failover).

## Lower-Level Testing With `snapshotctl`


It is possible to checkpoint and restore pods without the Dynamo operator via the lower-level `snapshotctl`

utility. However, the snapshot helm chart must be installed, with a running `snapshot-agent`

DaemonSet in the namespace with the checkpoint PVC mounted.

`snapshotctl`

is intended for lower-level debugging and validation workflows, not as the primary user-facing checkpoint interface. For command details and manifest requirements, see [deploy/snapshot/cmd/snapshotctl/README.md](https://docs.nvidia.com/dynamo/v1.1.1/deploy/snapshot/cmd/snapshotctl/README.md).

### Checkpoint from a worker pod manifest

The checkpoint manifest must be for a pod and use a placeholder image. `--container`

names the workload container to checkpoint.

If you do not pass `--checkpoint-id`

, `snapshotctl`

generates one and prints it:

### Restore from a worker pod manifest

This creates a new restore pod and returns after the request is submitted. Observe progress through Kubernetes readiness, events, and logs.

### Restore an existing pod in place

This patches restore metadata onto an existing pod that is already snapshot-compatible and returns after the patch is accepted.

## Checkpoint Identity

Checkpoints are uniquely identified by a **16-character SHA256 hash** (64 bits) of configuration that affects runtime state:

Fields that do **not** change the checkpoint hash include:

- replica count
- node placement (
`nodeSelector`

,`affinity`

,`tolerations`

) - resource requests/limits
- logging or observability configuration

`DynamoCheckpoint`

CRD

The `DynamoCheckpoint`

(shortname: `dckpt`

) is the operator-managed resource for checkpoint lifecycle.

Use it when you want:

- pre-warmed checkpoints before any
`DynamoGraphDeployment`

exists - explicit lifecycle control independent from a DGD
- a stable human-readable name that services can reference with
`checkpointRef`


The operator requires:

`spec.identity`

`spec.job.podTemplateSpec`


`spec.job.backoffLimit`

is deprecated and ignored. Checkpoint Jobs are always single-attempt.

Check status with:

The `status`

block looks like:

## Limitations

**Backend support is limited**: checkpoint/restore currently supports vLLM workers only, and that support is still a limited preview.**Worker coverage is narrow**: specialized workers such as multimodal, embedding, and diffusion are not supported.**Multi-GPU remains preview**: vLLM tensor-parallel configurations have limited validation and are not yet a broadly supported path across clusters.**GMS restore is not yet available**: Snapshot plus GPU Memory Service is blocked by admission.**Network state is sensitive**: restore is sensitive to live TCP socket state. Loopback bootstrap/control sockets are the most reliable path today.**Privileged DaemonSet required**:`snapshot-agent`

must run privileged to execute CRIU and`cuda-checkpoint`

. Workload pods do not need to be privileged.

## Troubleshooting

### Checkpoint Job finishes but the checkpoint never becomes `Ready`


Snapshot only becomes `Ready`

after `snapshot-agent`

confirms the checkpoint contents. A completed Job is not enough by itself.

If the worker template is wrong, the most common causes are using the raw runtime image instead of the placeholder image, or leaving out normal mounts and secrets that the worker needs to start.

### Restore cannot find or mount checkpoint storage

Restore discovers checkpoint storage from the `snapshot-agent`

DaemonSet in the same namespace. That DaemonSet must be ready and must mount the checkpoint PVC.

This is also the path that `snapshotctl`

uses when it resolves checkpoint storage.

`snapshotctl`

manifest is rejected or the restore target is wrong

`snapshotctl`

requires a `Pod`

manifest and a target-container list. Multi-container manifests are supported as long as every name passed via `--container`

or `--containers`

exists in the pod spec.

If the manifest already carries snapshot target metadata, it must agree with the CLI flag; `snapshotctl`

rejects mismatches instead of silently picking one.

## Planned Features

- Stabilize multi-GPU support
- Additional backend support
- Alternative storage backends