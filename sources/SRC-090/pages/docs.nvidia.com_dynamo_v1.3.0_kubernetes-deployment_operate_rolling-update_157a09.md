source: https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/operate/rolling-update
lastmod: 2026-09-24T19:58:16.636Z

# Rolling Updates

This guide covers how rolling updates work for `DynamoGraphDeployment`

(DGD) resources. Rolling updates allow you to update worker configurations (images, resources, environment variables, etc.) with minimal downtime by gradually replacing old pods with new ones.

The behavior of rolling updates depends on the backing resource type of your deployment. DGDs backed by Kubernetes Deployments benefit from **managed rolling updates** with namespace isolation, while Grove and LWS-backed deployments use their native update mechanisms.

## Example

Consider a disaggregated deployment with separate prefill and decode workers. You want to update the tensor parallelism of the decode worker to 2.

**Before** — original deployment:

**After** — updated with parallelism tuning:

Apply the update:

Monitor rolling update progress:

## Default Behavior (Grove and LWS)

For DGDs backed by **Grove** (PodCliques, PodCliqueSets) or **LWS** (LeaderWorkerSets), the operator does not manage rolling updates directly. Instead, these deployments rely on the native rolling update mechanisms of their underlying resources.

### What Happens

- A modification to the pod spec of a service triggers the rolling update behavior of the backing resource. In the example above, the modification to the pod spec of the decode worker triggers the rolling update of just the decode worker.
- For Grove, PodCliques (PCLQ) and PodCliqueScalingGroups use a static rolling update strategy of
`maxUnavailable: 1`

and`maxSurge: 0`

. LWS follows the same`maxUnavailable: 1`

and`maxSurge: 0`

strategy. **Old and new workers operate within the same Dynamo namespace.**This means old and new workers can discover each other through service discovery.

The following diagram illustrates the rolling update of the decode worker in a Grove PodCliqueSet (PCS). Only the decode PodClique is updated — the frontend and prefill PodCliques are unaffected:

### Grove Update Strategy Annotation

For Grove-backed DGDs, set `nvidia.com/grove-update-strategy`

on the `DynamoGraphDeployment`

metadata to pass a Grove `PodCliqueSet`

update strategy through to the generated `PodCliqueSet`

. This annotation does not affect Deployment-backed or LWS-backed DGDs. For the Grove-side design, see [GREP-291: OnDelete update strategy for PodCliqueSet](https://github.com/ai-dynamo/grove/pull/403).


Supported values are:

If the annotation is omitted, Dynamo leaves the Grove update strategy unset and Grove uses its default behavior. Invalid values are rejected. Values must match Grove’s exact spelling, including case.

Inspect the generated Grove strategy:

For `OnDelete`

, delete old Grove-managed pods when you are ready to replace them:

Use `OnDelete`

for updates that require manual coordination, such as incompatible worker versions or maintenance windows. Because old and new workers still share the same Dynamo namespace, `OnDelete`

gives you control over when pods are replaced but does not provide namespace isolation.

### Implications for Disaggregated Deployments

Because old and new workers share the same Dynamo namespace, they are grouped together by the router. In a disaggregated setup, this can lead to cross-generation communication — for example, the router might send a request from a newly deployed prefill worker to an old decode worker (or vice versa). If the old and new versions are incompatible, this can result in errors.

For Grove and LWS deployments with disaggregated prefill/decode workers, be aware that during a rolling update, new workers may communicate with old workers. Ensure that your worker versions are backward-compatible, or consider using Deployment-backed DGDs which provide namespace isolation during updates.

Managed rolling updates with namespace isolation are planned for Grove and LWS-backed deployments in a future release. See [Future Work](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/operate/rolling-update#future-work) for details.

## Managed Rolling Updates (Deployments)

For DGDs backed by Kubernetes **Deployments** (single-node, non-multinode services), the Dynamo operator implements managed rolling updates with namespace isolation. This is tracked in the DGD status and provides stronger guarantees for disaggregated deployments.

### How It Works

-
**Spec change detection**— The operator computes a hash of all worker service specs (prefill, decode, and worker component types). When this hash changes, a rolling update is triggered. -
**Namespace isolation**— New worker`DynamoComponentDeployments`

(DCDs) are created with the spec hash appended to their Dynamo namespace. This means new workers register in a different Dynamo namespace than old workers, preventing cross-generation discovery. A new prefill worker will only discover and route to new decode workers, avoiding compatibility issues. -
**Gradual replacement**— The operator gradually scales up new worker DCDs and scales down old ones, respecting`maxSurge`

and`maxUnavailable`

constraints. When a worker service is updated (all new replicas are ready, all old replicas are terminated), it is marked as completed. -
**Cleanup**— Once all worker services have completed the transition, old worker DCDs are deleted and the rolling update is marked as completed.

Only worker component types (`worker`

, `prefill`

, `decode`

) participate in managed rolling updates. Non-worker components like `frontend`

are updated in-place without namespace isolation.

### Rolling Update Phases

The rolling update progress is tracked in `.status.rollingUpdate`

with the following phases:

The status also tracks:

`startTime`

— When the rolling update began.`endTime`

— When the rolling update completed.`updatedServices`

— List of worker services that have completed the transition.

### Configuring maxSurge and maxUnavailable

You can configure the rolling update strategy per service using annotations:

Values can be absolute integers (e.g., `"1"`

, `"2"`

) or percentages (e.g., `"25%"`

, `"50%"`

). Percentages are resolved against the desired replica count — rounding up for `maxSurge`

and rounding down for `maxUnavailable`

. The operator ensures at least one of `maxSurge`

or `maxUnavailable`

is greater than zero to guarantee forward progress.

**Example** — zero-downtime update with surge capacity:

This ensures that all 4 existing prefill replicas remain available while 1 new replica is brought up at a time.

**Example** — fast update allowing temporary capacity reduction:

This avoids creating extra pods but allows up to 2 decode replicas to be unavailable at a time, speeding up the transition.

### Worker Hash and DCD Naming

Worker DCDs always include a hash suffix derived from the worker specs: `{dgd-name}-{service-name}-{hash}`

(e.g., `vllm-disagg-vllmdecodeworker-a1b2c3d4`

). During a rolling update, the new worker DCDs are created with the new spec hash while the old DCDs retain the previous hash, allowing both generations to coexist:

**Old worker DCD:**`vllm-disagg-vllmdecodeworker-a1b2c3d4`

(previous hash)**New worker DCD:**`vllm-disagg-vllmdecodeworker-f5e6d7c8`

(new hash)

The hash is computed from a SHA-256 digest of all worker service specs (excluding non-pod-template fields like `replicas`

, `autoscaling`

, and `ingress`

). This means:

- Scaling changes (replica count) do
**not**trigger a rolling update. - Pod template changes (image, resources, env vars, volumes, etc.)
**do**trigger a rolling update. - The hash covers
**all**worker services together — changing any single worker’s spec triggers a rolling update for all workers.

The current worker hash is stored as the annotation `nvidia.com/current-worker-hash`

on the DGD resource, and individual worker DCDs are labeled with `nvidia.com/dynamo-worker-hash`

for filtering.

### Status During Rolling Updates

During a rolling update, the DGD status aggregates information from both old and new worker DCDs:

**Replicas**— Total count across old and new.**ReadyReplicas**— Aggregate ready count across old and new.**UpdatedReplicas**— Only new worker replicas.

This provides a holistic view of the deployment’s health during the transition.

## Comparison

## Future Work

The following enhancements are planned for future releases:

**Managed rolling updates for Grove and LWS**— Extending managed rolling updates with namespace isolation to Grove and LWS-backed deployments, providing the same cross-generation discovery protection that Deployment-backed DGDs have today.**Coordinated worker updates**— Currently, prefill and decode workers are updated independently, which can result in an imbalance between old and new sets during the transition. Future releases will coordinate the rollout across worker types.**Partitioned rollouts**— The ability to roll out updates to a percentage of workers (e.g., 30%), pause, observe metrics, and then continue. This enables canary-style deployments for safer rollouts.**DGD-level rolling update configuration**— The ability to configure`maxSurge`

and`maxUnavailable`

at the DGD API level, regardless of the backing resource type.