# [Issue #4752] [Feature] RayService incremental upgrade: support gatewayAddresses in ClusterUpgradeOptions for bare-metal deployments

source: https://github.com/ray-project/kuberay/issues/4752
state: open | updated: 2026-09-23T04:42:46Z
labels: enhancement, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

The `NewClusterWithIncrementalUpgrade` strategy creates a Gateway at runtime via `createGateway()`, but the generated Gateway spec has no `addresses` field and  `ClusterUpgradeOptions` provides no way to pass one through. 

On bare-metal clusters (e.g MetalLB + Envoy Gateway), a Gateway only becomes `PROGRAMMED=true` when `spec.addresses` is explicitly set — without it, Envoy Gateway reports `NoResources` and the proxy pod is never scheduled, meaning traffic never shifts to the new cluster.                                                                                                                                           

Pre-creating the Gateway with the desired address does not work because the reconciler performs a full `Update` that overwrites the spec, stripping any fields it does not  own (confirmed via testing).                                                                                                                                                               
                                                                                                                                                                                             
  **Proposed fix:** add an optional `GatewayAddresses` field to `ClusterUpgradeOptions`:                                                                                                     
   
```go                                                                                                                                                                                          
  type ClusterUpgradeOptions struct {                                                                                                                                                        
      GatewayClassName string                                                                                                                                                                
      GatewayAddresses []gatewayv1.GatewayAddress `json:"gatewayAddresses,omitempty"`
      ...                                                                            
  }                                                                                                                                                                                          
 ```
and pass it through in `createGateway()` when present. 

### Use case

Running RayService on a bare-metal Kubernetes cluster with MetalLB as the loadbalancer and Envoy Gateway as the Gateway API implementation. MetalLB assigns IPs from a pre-configured pool, but Envoy Gateway on bare-metal requires a static `spec.addresses` on the Gateway resource to become PROGRAMMED. Without this field, the Gateway remains in a non-programmed state indefinitely and incremental traffic shifting never starts, making `NewClusterWithIncrementalUpgrade` unusable on bare-metal. 

### Related issues

#3209 

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (5)

### SowmyaaDixit · 2026-04-22

I tried solving this issue in my PR https://github.com/ray-project/kuberay/pull/4754
PTAL and review when you get a chance. Thanks

### xakaitetoia · 2026-04-22

> I tried solving this issue in my PR [#4754](https://github.com/ray-project/kuberay/pull/4754) PTAL and review when you get a chance. Thanks

cool thanks a lot. THough there is some dependencies that need to be fixed? https://github.com/ray-project/kuberay/issues/4752#issuecomment-4296457261 

it has changed to `GatewaySpecAddress` 

### Future-Outlier · 2026-04-22

cc @ryanaoleary to take a look, tks!

### SowmyaaDixit · 2026-04-22

Thanks for pointing it out. Fixed it to use GatewaySpecAddress

### github-actions[bot] · 2026-09-23

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
