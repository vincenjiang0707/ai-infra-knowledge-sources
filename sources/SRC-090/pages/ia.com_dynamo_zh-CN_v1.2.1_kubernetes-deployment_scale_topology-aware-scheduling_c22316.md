source: https://docs.nvidia.com/dynamo/zh-CN/v1.2.1/kubernetes-deployment/scale/topology-aware-scheduling
lastmod: 2026-09-23T23:30:39.914Z

# Topology Aware Scheduling

Topology Aware Scheduling (TAS) lets you control where Dynamo places inference workload pods relative to the cluster’s network topology. By packing related pods within the same rack, block, or other topology domain, you reduce inter-node latency and improve throughput — especially for disaggregated serving where prefill, decode, and routing components communicate frequently.

TAS is **opt-in**. Existing deployments without topology constraints continue to work unchanged.

TAS controls pod placement. To constrain or bias the Dynamo router’s prefill-to-decode handoff after pods are already running, see [Topology-Aware KV Transfer](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/operate/topology-aware-kv-transfer).

## Prerequisites

## Topology Domains

Topology domains are **free-form** identifiers defined by the cluster admin in the `ClusterTopology`

CR. Common examples include `region`

, `zone`

, `datacenter`

, `block`

, `rack`

, `host`

, and `numa`

, but any name matching the pattern `^[a-z0-9]([a-z0-9-]*[a-z0-9])?$`

is valid (no leading or trailing hyphens).

Domain names must match exactly what is configured in the `ClusterTopology`

CR referenced by `topologyProfile`

. During DGD creation, the Dynamo webhook validates that every `packDomain`

exists in the referenced `ClusterTopology`

.

When you specify a `packDomain`

, the scheduler packs all replicas of the constrained component within a single instance of that domain. For example, `packDomain: rack`

means “place all pods within the same rack.”

## Topology Profile

Every DGD that uses topology constraints must reference a `ClusterTopology`

CR by name via the `topologyProfile`

field. This field is set at `spec.topologyConstraint`

(the deployment level) and is inherited by all services — services must not set `topologyProfile`

themselves.

The `topologyProfile`

tells the Dynamo operator and the underlying framework which topology hierarchy to use for scheduling and validation.

## Enabling TAS on a DGD

Add a `topologyConstraint`

field to your `DynamoGraphDeployment`

at the deployment level, at the service level, or both. The deployment level must include a `topologyProfile`

. Each constraint specifies a `packDomain`

.

### Example 1: Deployment-Level Constraint (Services Inherit)

All services inherit the deployment-level constraint. This is the simplest configuration when you want uniform topology packing.

### Example 2: Service-Level Constraint Only

Only the specified service gets topology packing. Other services are scheduled without topology constraints. The deployment level must still set `topologyProfile`

.

### Example 3: Mixed (Deployment-Level Default + Per-Service Override)

Set a broad constraint at the deployment level and a narrower override on specific services. Service-level constraints must be **equal to or narrower than** the deployment-level constraint (determined by the ordering in the `ClusterTopology`

CR).

## Hierarchy Rules

When **both** a deployment-level and a service-level `topologyConstraint`

are set, the service’s `packDomain`

must be **equal to or narrower** than the deployment-level `packDomain`

. “Narrower” is determined by the ordering of levels in the referenced `ClusterTopology`

CR — levels appearing later in the `spec.levels`

array are considered narrower.

The Dynamo webhook rejects the DGD at creation time if a service constraint is broader than the deployment constraint (when validating against a `ClusterTopology`

CR).

When only one level is set (deployment-level only or service-level only), no hierarchy check applies.

## Field Reference

## Multinode Considerations

For multinode services (services with a `multinode`

section), the topology constraint is applied at the **scaling group** level rather than on individual worker pods. This is important because a multinode service spawns `replicas × nodeCount`

pods — for example, 2 replicas with `nodeCount: 4`

produces 8 pods across 8 nodes. Applying the constraint at the scaling group level means the scheduler packs each replica’s set of nodes within the requested domain, without over-constraining individual pods to a single host.

For example, with this configuration:

Each replica’s 4 nodes are packed within a single rack. The two replicas may land in different racks (the constraint applies per-replica, not across all replicas).

**Recommendation:** For multinode services, use `rack`

or `block`

as the `packDomain`

to keep workers within a high-bandwidth domain while still allowing the scheduler to spread them across hosts within that domain. Avoid `host`

for multinode services, as packing multiple nodes onto one host is not meaningful.

## Immutability

Topology constraints **cannot be changed after the DGD is created**. This includes:

- Adding a topology constraint to a DGD or service that did not have one
- Removing an existing topology constraint
- Changing the
`topologyProfile`

value - Changing the
`packDomain`

value

To change topology constraints, **delete and recreate** the DGD. This matches the behavior of the underlying framework, which enforces immutability on topology constraints for generated resources.

## Monitoring Topology Enforcement

When any topology constraint is set, the DGD status includes a `TopologyLevelsAvailable`

condition that reports whether the topology levels referenced by your constraints still exist in the cluster topology.

**Healthy state:**

**Degraded state** (e.g., an admin removed a topology level from the `ClusterTopology`

CR after deployment):

When topology levels become unavailable, Dynamo emits a **Warning** event on the DGD. The deployment may still appear `Ready`

because the underlying framework keeps pods running, but topology placement is no longer guaranteed.

## Troubleshooting

### DGD rejected: “ClusterTopology not found”

The Dynamo webhook validates that the `ClusterTopology`

CR referenced by `topologyProfile`

exists when any topology constraint is set. If it cannot read the `ClusterTopology`

CR:

- Verify that the cluster admin has created the
`ClusterTopology`

resource named in`topologyProfile`

. See the[Grove documentation](https://github.com/NVIDIA/grove)for setup. - Verify that the Dynamo operator has RBAC to read
`clustertopologies.grove.io`

(included in the default Helm chart).

### DGD rejected: “packDomain not found in cluster topology”

The specified `packDomain`

does not exist as a level in the referenced `ClusterTopology`

CR. Check which domains are defined:

Ensure the domain you are requesting (e.g., `rack`

) is configured in the `ClusterTopology`

with a corresponding node label.

### DGD rejected: “topologyProfile is required”

Any DGD that has a topology constraint (at the spec or service level) must set `spec.topologyConstraint.topologyProfile`

to the name of a `ClusterTopology`

CR. Add the `topologyProfile`

field to `spec.topologyConstraint`

.

### Pods stuck in Pending

The scheduler cannot satisfy the topology constraint. Common causes:

- Not enough nodes within a single instance of the requested domain (e.g., requesting 8 GPUs packed in one rack, but no rack has 8 available GPUs).
- Node labels do not match the
`ClusterTopology`

configuration.

Inspect scheduler events for details:

### TopologyLevelsAvailable is False

The DGD was deployed successfully, but the topology definition has since changed. The underlying framework detected that one or more required topology levels are no longer available.

- Check the condition message for specifics.
- Inspect the
`ClusterTopology`

CR to see if a domain was removed or renamed. - If the topology was intentionally changed, delete and recreate the DGD to pick up the new topology.

### DGD rejected: hierarchy violation

A service-level `packDomain`

is broader than the deployment-level `packDomain`

. “Broader” and “narrower” are determined by the order of levels in the `ClusterTopology`

CR — levels appearing earlier in `spec.levels`

are broader.

Ensure service-level constraints are equal to or narrower than the deployment-level constraint.