# [Issue #4840] workerGroupSpecs should declare x-kubernetes-list-type: map (keyed on groupName)

source: https://github.com/ray-project/kuberay/issues/4840
state: open | updated: 2026-09-23T04:43:09Z
labels: stale

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.

### KubeRay Component

apiserver, ray-operator

### What happened + What you expected to happen

`RayService.spec.rayClusterConfig.workerGroupSpecs` and `RayCluster.spec.workerGroupSpecs` are declared as plain `type: array` in the CRDs, without `x-kubernetes-list-type` / `x-kubernetes-list-map-keys` markers:

```bash
kubectl get crd rayservices.ray.io -o json \
  | jq '.spec.versions[] | select(.name=="v1") | .schema.openAPIV3Schema.properties.spec.properties.rayClusterConfig.properties.workerGroupSpecs | {type, list_type: .["x-kubernetes-list-type"], map_keys: .["x-kubernetes-list-map-keys"]}'
{
  "type": "array",
  "list_type": null,
  "map_keys": null
}
```

Without these markers, Kubernetes Server-Side Apply (SSA) treats the field as an **atomic list**: any Apply request that touches the field replaces the whole array atomically. Each `workerGroupSpec` has a unique `groupName` (the operator already keys by it for pod naming and reconciliation), so the natural semantics are a **map list keyed on `groupName`**, not atomic.

Concrete consequences of the missing markers:

1. Two SSA clients can't independently own different worker groups in the same `RayCluster` / `RayService`. With map semantics, controller A could own `workerGroupSpecs[name=foo]` and controller B could own `workerGroupSpecs[name=bar]` cleanly; atomic semantics force a single owner of the whole list.
2. `kubectl apply --server-side` patching only one worker group can silently drop fields on others under conflict scenarios.
3. ArgoCD with `ServerSideApply=true` + `RespectIgnoreDifferences=true` and an `ignoreDifferences` path inside one worker group corrupts other fields on the same list during the "respect ignored values" rewrite — see **argoproj/argo-cd#26831** for the upstream-fix-needed side. (The ArgoCD bug is the proximate cause of our outage, but a CRD that declared map-list semantics would let SSA itself handle the merge correctly and would unblock any future ArgoCD fix that goes through OpenAPI-derived PatchMeta.)

### Expected

`workerGroupSpecs` declared as:

```yaml
workerGroupSpecs:
  type: array
  x-kubernetes-list-type: map
  x-kubernetes-list-map-keys:
  - groupName
  items: ...
```

This is the standard CRD shape for lists with a stable, unique key (mirrors `Pod.spec.containers` keyed on `name`, `Deployment.spec.template.spec.containers`, etc.).

### Reproduction script

```bash
# Look at any KubeRay CRD with workerGroupSpecs
kubectl get crd rayservices.ray.io -o json | jq '.spec.versions[] | select(.name=="v1") | .schema.openAPIV3Schema.properties.spec.properties.rayClusterConfig.properties.workerGroupSpecs | keys'
# -> ["items", "type"]   # no x-kubernetes-* markers

# Patching the CRD locally to add the markers (verified safe on v1):
kubectl patch crd rayservices.ray.io --type=json -p='[
  {"op":"add","path":"/spec/versions/0/schema/openAPIV3Schema/properties/spec/properties/rayClusterConfig/properties/workerGroupSpecs/x-kubernetes-list-type","value":"map"},
  {"op":"add","path":"/spec/versions/0/schema/openAPIV3Schema/properties/spec/properties/rayClusterConfig/properties/workerGroupSpecs/x-kubernetes-list-map-keys","value":["groupName"]}
]'
# Subsequent SSA Applies merge by groupName correctly.
```

(Existing `RayService` / `RayCluster` resources continue to validate; the markers don't change validation, only SSA merge semantics.)

### Same change needed on

- `RayService.spec.rayClusterConfig.workerGroupSpecs`
- `RayCluster.spec.workerGroupSpecs`
- Any other field in the project that is a list with a stable unique key (e.g. consider `headGroupSpec` siblings, `volumes`, env-var lists already covered by built-in types — only fields newly defined by KubeRay's own schema need this treatment).

### Versions / Dependencies

KubeRay operator: most recent release (verified against `v1.4.x` chart shipped via kuberay-helm). The CRDs in `ray-project/kuberay` `helm-chart/kuberay-operator/crds/` ship without the markers.

### Reproduction script

See above.

### Anything else

No.

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR! (small, schema-only)


## 评论 (1)

### github-actions[bot] · 2026-09-23

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
