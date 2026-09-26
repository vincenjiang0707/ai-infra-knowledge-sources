source: https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/multinode/topology-aware-kv-transfer
lastmod: 2026-09-24T19:58:16.636Z

Topology-Aware KV Transfer


Topology-Aware KV Transfer

Keep disaggregated prefill and decode KV-cache transfers within a selected topology domain

**Experimental.** Topology-aware KV transfer lets a disaggregated NVIDIA Dynamo deployment route decode requests toward workers that share the selected prefill worker’s topology domain, such as zone or rack. This reduces slow cross-domain KV-cache transfers when prefill and decode workers exchange KV data over NIXL.

Use this feature when:

- Your deployment uses separate prefill and decode workers.
- Your cluster exposes useful node labels, such as
`topology.kubernetes.io/zone`

or a rack/block label. - Same-domain KV transfer is required for correctness or strongly preferred for latency and bandwidth.

This page covers the Kubernetes operator path. For router and runtime behavior, see [Router Topology-Aware KV Transfer](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/topology-aware-kv-transfer).
For RDMA/NIXL transport setup, see [Disagg Communication](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/disagg-communication).

## How It Works

Set exactly one topology source in `spec.experimental.kvTransferPolicy`

:

`labelKey`

copies one Kubernetes node label onto the worker pod under the same key.`clusterTopologyName`

uses the domain-to-node-label mappings from a Grove topology resource. The controller copies every topology level onto the worker pod under`nvidia.com/dynamo-topology.<domain>`

labels.

For either source, the operator:

- Annotates worker pods with the selected topology source.
- Runs a topology-label controller that copies node topology values onto the worker pod after scheduling.
- Projects the copied pod labels into
`/etc/dynamo/topology/<domain>`

files with a Downward API volume. - Injects worker environment variables that tell the backend runtime which topology domain and enforcement policy to publish.

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

### Use a Grove Topology Source

To use topology levels defined by Grove, set `clusterTopologyName`

instead of `labelKey`

. The selected `domain`

must exist in the referenced topology resource.

This path requires Grove to be enabled in the operator and for the DGD. The operator projects every topology level from the referenced resource, while the router uses only the selected `domain`

for the KV-transfer constraint.

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

`kvTransferPolicy`

is immutable after the DGD is created. To add, remove, or change the policy, delete and recreate the DGD.

The runtime uses `domain`

, not the Kubernetes label key, when creating routing constraints. For example, `labelKey: topology.kubernetes.io/zone`

and `domain: zone`

produce worker topology metadata like:

## Verify the Deployment

After the DGD creates worker pods, verify the operator pipeline from the selected topology source to the runtime topology files.

For a `labelKey`

source, verify the source annotation and copied label:

For a `clusterTopologyName`

source, verify the source annotation and the canonical label for the selected domain:

For either source, inspect the projected topology files:

Expected results:

- The source annotation contains the configured
`labelKey`

or`clusterTopologyName`

. - The worker pod has the copied topology label or canonical Grove topology labels.
`/etc/dynamo/topology/<domain>`

exists for the selected domain and contains the topology value. The Grove path also projects files for the other topology levels.

Worker logs should include topology config during startup:

## Troubleshooting

### Pod Has No Copied Topology Label

For a `labelKey`

source, check whether the node has the configured label:

For a `clusterTopologyName`

source, verify that the referenced Grove topology resource exists, contains the selected `domain`

, and maps each domain to a label present on the node. Also verify that the DGD does not set `nvidia.com/enable-grove: "false"`

.

If the label is missing, the topology-label controller emits a warning event with reason `TopologyLabelMissing`

and leaves topology metadata unavailable for that worker.

### Worker Exits While Waiting for Topology

When topology is enabled, the worker waits for the transfer-domain file to appear and contain data. If it stays empty, check:

`spec.experimental.kvTransferPolicy.domain`

matches the projected file name.- The configured
`labelKey`

, or the source label for the selected Grove topology domain, exists on the worker’s node. - The worker pod has the source annotation for
`labelKey`

or`clusterTopologyName`

. - The topology-label controller is running and has node
`get`

RBAC.

### Required Policy Fails Requests

With `enforcement: required`

, decode routing fails if no decode worker has the same generated topology taint as the selected prefill worker. Verify both prefill and decode workers publish the same `domain`

, and that each domain where prefill workers can be selected has enough matching decode workers for the expected p/d ratio.

Use `preferred`

while validating a heterogeneous rollout if cross-domain routing is acceptable during partial capacity.

## Relationship to Topology Aware Scheduling

[Topology Aware Scheduling](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/multinode/topology-aware-scheduling) controls where Kubernetes places pods. Topology-aware KV transfer controls how Dynamo routes between already-running prefill and decode workers.

Use them together when possible:

- Topology Aware Scheduling keeps workers placed inside useful topology boundaries.
- Topology-aware KV transfer prevents the router from choosing a decode worker outside the selected prefill worker’s transfer domain.