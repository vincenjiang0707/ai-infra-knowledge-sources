source: https://docs.nvidia.com/dynamo/zh-CN/v1.2.1/kubernetes-deployment/operate/topology-aware-kv-transfer
lastmod: 2026-09-23T23:30:39.914Z

Topology-Aware KV Transfer


Topology-Aware KV Transfer

Keep disaggregated prefill and decode KV-cache transfers within a selected topology domain

Topology-aware KV transfer lets a disaggregated Dynamo deployment route decode requests toward workers that share the selected prefill worker’s topology domain, such as zone or rack. This reduces slow cross-domain KV-cache transfers when prefill and decode workers exchange KV data over NIXL.

Use this feature when:

- Your deployment uses separate prefill and decode workers.
- Your cluster exposes useful node labels, such as
`topology.kubernetes.io/zone`

or a rack/block label. - Same-domain KV transfer is required for correctness or strongly preferred for latency and bandwidth.

This page covers the Kubernetes operator path. For router and runtime behavior, see [Router Topology-Aware KV Transfer](https://docs.nvidia.com/dynamo/v1.2.1/components/router/topology-aware-kv-transfer).
For RDMA/NIXL transport setup, see [Disagg Communication](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/operate/disagg-communication).

## How It Works

The operator configures worker pods from `spec.experimental.kvTransferPolicy`

:

- Adds a
`nvidia.com/topology-label-key`

annotation to worker pods. - Runs a topology-label controller that copies the configured node label onto the worker pod after scheduling.
- Projects that pod label into
`/etc/dynamo/topology/<domain>`

with a Downward API volume. - Injects worker environment variables that tell the backend runtime which topology domain and enforcement policy to publish.

The frontend does not read this policy from its own environment. Workers publish the topology metadata in their `ModelRuntimeConfig`

; the router reads it from runtime discovery.

## Prerequisites

Confirm that the label you plan to use exists on worker nodes:

## Required Same-Domain Routing

`enforcement: required`

constrains decode worker selection to workers whose topology value matches the selected prefill worker for the configured domain. If no decode worker satisfies the generated constraint, the router fails the request instead of silently crossing the domain.

`enforcement`

defaults to `required`

when omitted.

`required`

is a decode-routing constraint, not a capacity planner. The `DynamoGraphDeployment`

author or cluster administrator must ensure that every topology domain that can receive prefill workers also has sufficient same-domain decode capacity. If a domain has prefill workers but no matching decode workers, or too little decode capacity, the router cannot spill to another domain without violating the policy.

### Capacity Planning Across Domains

Plan prefill and decode capacity per topology domain before enabling `enforcement: required`

. For example, assume:

- Two availability zones:
`az-1`

and`az-2`

. - The target fleet is 60 prefill workers and 120 decode workers.
- The fleet should be split evenly across the two zones.
- The target prefill-to-decode ratio is 1:2 in each zone.

That means each zone should run 30 prefill workers and 60 decode workers:

In a `DynamoGraphDeployment`

, express this as separate prefill and decode components per zone. Pin each component to its zone and set `kvTransferPolicy.enforcement`

to `required`

so the router refuses cross-zone decode selection. The DGD author or cluster administrator must ensure each zone has enough schedulable capacity for its pinned replicas. Worker command and args are omitted here; configure each worker for prefill or decode mode as in the base disaggregated serving manifest:

## Preferred Same-Domain Routing

`enforcement: preferred`

keeps all decode workers eligible but biases worker selection toward the same topology domain.

`preferredWeight`

is required with `enforcement: preferred`

. It must be between `0`

and `1`

. A higher value creates a stronger same-domain preference, but it is not a probability and does not guarantee same-domain selection.

## Field Reference

The runtime uses `domain`

, not the Kubernetes label key, when creating routing constraints. For example, `labelKey: topology.kubernetes.io/zone`

and `domain: zone`

produce worker topology metadata like:

## Verify the Deployment

After the DGD creates worker pods, verify the operator pipeline from node label to runtime topology file.

Expected results:

- The annotation value is the configured
`labelKey`

. - The worker pod has the copied topology label.
`/etc/dynamo/topology/<domain>`

exists and contains the topology value.

Worker logs should include topology config during startup:

## Troubleshooting

### Pod Has No Copied Topology Label

Check whether the node has the configured label:

If the label is missing, the topology-label controller emits a warning event with reason `TopologyLabelMissing`

and leaves topology metadata unavailable for that worker.

### Worker Exits While Waiting for Topology

When topology is enabled, the worker waits for the transfer-domain file to appear and contain data. If it stays empty, check:

`spec.experimental.kvTransferPolicy.domain`

matches the projected file name.`spec.experimental.kvTransferPolicy.labelKey`

exists on the worker’s node.- The worker pod has the
`nvidia.com/topology-label-key`

annotation. - The topology-label controller is running and has node
`get`

RBAC.

### Required Policy Fails Requests

With `enforcement: required`

, decode routing fails if no decode worker has the same generated topology taint as the selected prefill worker. Verify both prefill and decode workers publish the same `domain`

, and that each domain where prefill workers can be selected has enough matching decode workers for the expected p/d ratio.

Use `preferred`

while validating a heterogeneous rollout if cross-domain routing is acceptable during partial capacity.

## Relationship to Topology Aware Scheduling

[Topology Aware Scheduling](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/scale/topology-aware-scheduling) controls where Kubernetes places pods. Topology-aware KV transfer controls how Dynamo routes between already-running prefill and decode workers.

Use them together when possible:

- Topology Aware Scheduling keeps workers placed inside useful topology boundaries.
- Topology-aware KV transfer prevents the router from choosing a decode worker outside the selected prefill worker’s transfer domain.