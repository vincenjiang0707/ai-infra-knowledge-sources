# [Issue #2779] [Bug] StormServices in two namespaces seem to affect each other when they share a selector (deleting one kills the other's Pods)

source: https://github.com/vllm-project/aibrix/issues/2779
state: open | updated: 2026-09-23T10:22:12Z
labels: kind/bug, area/orchestration

## 正文

### 🐛 Describe the bug

I'm new to AIBrix. I was following the quickstart on a local kind cluster and wanted to deploy one StormService in each of two namespaces. Nothing came up in the second namespace, and later, when I deleted it, it killed the Pods that were running in the first namespace.

I spent a while assuming I had written something wrong. Then I looked at the code and started suspecting `getRoleSetList` (`pkg/controller/stormservice/rolesetoperations.go:37`):

```go
err = r.List(ctx, roleSetList, client.MatchingLabelsSelector{Selector: roleSetSelector})
```

This only filters by label, with no `client.InNamespace(...)`, so I think it lists RoleSets across the whole cluster. And `sync` (deciding how many to create), `rollout`, `finalize` (cleanup on delete) and `revision` all call it, so wouldn't counting and deleting reach into other namespaces too? I'm not sure whether this is intentional — please correct me if I'm misreading it.

At first I assumed I had reused the same labels in both namespaces by accident, but it turns out following the samples leads to this: `samples/quickstart/pd-model.yaml` and `samples/disaggregation/vllm/1p1d.yaml` both use the selector `app: vllm-1p1d`, both use the same StormService name, and neither sets a namespace. So two people each running the quickstart with `kubectl apply -n <their own namespace>` end up colliding.

I tried it in the quickstart shape first (`replicas: 1`, no mode, no PodAutoscaler at all), creating qa first and qb second:

```
20:47:31 qa: rolesets=1 pods=2 | qb: rolesets=0 pods=0
20:48:22 qa: rolesets=1 pods=2 | qb: rolesets=0 pods=0
```

qb brought up nothing, yet it reported `replicas=1 ready=1 currentReplicas=1`. Then I deleted qb — the StormService that actually owns nothing — and over 70 seconds qa's RoleSet was deleted 5 times and its Pods were killed 10 times, while qb itself never finished deleting.

To see it more clearly I tried a more obvious configuration (team-a / team-b, `mode: Replica`, `replicas: 2`, both with the selector `app: shared-label`). The four things below, and the reproduction steps, use that configuration.

First, the one created second does nothing at all. team-a is created first and takes 2 RoleSets; when team-b lists, it sees 2 already there, decides the work is done, and creates none:

```
team-a rolesets: 2, pods: 2
team-b rolesets: 0, pods: 0
```

Second, the status is wrong. svc-b has zero Pods but reports `replicas=2 ready=2`. The status is computed from the same cross-namespace listing, so `kubectl get` gives no hint that anything is off.

Third, and this is the scary one: deleting svc-b repeatedly destroys what team-a is running. It looks like svc-b's finalize cleans up "its own" RoleSets and ends up cleaning team-a's; team-a's controller recreates them, and they get deleted again. Over two minutes team-a's RoleSets were deleted 16 times and recreated 16 times, and its Pods were killed 25 times (another run gave 18 and 16, depending on how fast the environment is). The logs show the deletes landing right after a sync of team-b, deleting team-a's objects:

```
I0922 08:50:29.304571 stormservice_controller.go:101] Started syncing stormservice team-b/svc-b
I0922 08:50:29.304665 rolesetoperations.go:131] [rolesetoperation] delete roleset svc-a-roleset-vln6l
I0922 08:50:44.321573 stormservice_controller.go:101] Started syncing stormservice team-b/svc-b
I0922 08:50:44.321628 rolesetoperations.go:131] [rolesetoperation] delete roleset svc-a-roleset-khw2t
```

Fourth, svc-b itself cannot be deleted. finalize only removes the finalizer once the listing comes back empty, but the other side keeps recreating, so that never happens. I watched svc-b's deletion hang for more than two minutes and ended up removing the finalizer by hand. Deleting a whole namespace behaves the same way: another time I deleted a namespace that held a StormService and it sat in Terminating for eight minutes until I removed the finalizer.

I only hit this while playing around locally, but if two teams share a cluster, one person deleting their own service would restart another person's Pods. From the affected side all you see is a stream of `Killing` events, so it would be hard to track down — it took me a while of reading controller logs, and noticing that the deletes follow a sync of the other namespace, before it clicked.


### Steps to Reproduce

Prerequisite: AIBrix controller-manager installed with `stormservice-controller` enabled. Replace `IMAGE` with any image that starts in your environment — the workload itself doesn't matter.

```bash
export IMAGE=busybox:1.36   # any image available in your environment

kubectl create ns team-a
kubectl create ns team-b

cat <<EOF | kubectl apply -f -
apiVersion: orchestration.aibrix.ai/v1alpha1
kind: StormService
metadata:
  name: svc-a
  namespace: team-a
spec:
  mode: Replica
  replicas: 2
  updateStrategy: {type: RollingUpdate}
  selector: {matchLabels: {app: shared-label}}
  template:
    metadata: {labels: {app: shared-label}}
    spec:
      roles:
      - name: worker
        replicas: 1
        template:
          spec:
            terminationGracePeriodSeconds: 0
            containers:
            - name: c
              image: $IMAGE
              command: ["sh", "-c", "sleep 100000"]
---
# identical to the one above, only the name and namespace differ;
# the selector label is deliberately the same
apiVersion: orchestration.aibrix.ai/v1alpha1
kind: StormService
metadata:
  name: svc-b
  namespace: team-b
spec:
  mode: Replica
  replicas: 2
  updateStrategy: {type: RollingUpdate}
  selector: {matchLabels: {app: shared-label}}
  template:
    metadata: {labels: {app: shared-label}}
    spec:
      roles:
      - name: worker
        replicas: 1
        template:
          spec:
            terminationGracePeriodSeconds: 0
            containers:
            - name: c
              image: $IMAGE
              command: ["sh", "-c", "sleep 100000"]
EOF

sleep 30
```

**Step 1, check whether team-b created anything:**

```bash
echo "team-a rolesets: $(kubectl -n team-a get roleset --no-headers | wc -l), pods: $(kubectl -n team-a get pod --no-headers | wc -l)"
echo "team-b rolesets: $(kubectl -n team-b get roleset --no-headers 2>/dev/null | wc -l), pods: $(kubectl -n team-b get pod --no-headers 2>/dev/null | wc -l)"
```

On my side team-b is empty:

```
team-a rolesets: 2, pods: 2
team-b rolesets: 0, pods: 0
```

**Step 2, look at what svc-b reports:**

```bash
kubectl -n team-b get stormservice svc-b -o jsonpath='replicas={.status.replicas} ready={.status.readyReplicas}'; echo
```

It has no Pods at all, yet claims to be healthy:

```
replicas=2 ready=2
```

**Step 3, delete svc-b and watch team-a:**

```bash
kubectl -n team-b delete stormservice svc-b --wait=false

for i in $(seq 1 6); do
  echo "$(date +%T) team-a rolesets: $(kubectl -n team-a get roleset -o jsonpath='{range .items[*]}{.metadata.name} {end}') | svc-b still present: $(kubectl -n team-b get stormservice svc-b --no-headers 2>/dev/null | wc -l)"
  sleep 10
done
```

The RoleSet names change every round, so they are being deleted and recreated; svc-b also never goes away:

```
21:07:19 team-a rolesets: svc-a-roleset-l9nh8 svc-a-roleset-td4qg  | svc-b still present: 1
21:07:29 team-a rolesets: svc-a-roleset-9r78m svc-a-roleset-h5sf9  | svc-b still present: 1
21:07:39 team-a rolesets: svc-a-roleset-gswh5 svc-a-roleset-kcm2n  | svc-b still present: 1
21:07:49 team-a rolesets: svc-a-roleset-gswh5 svc-a-roleset-kcm2n  | svc-b still present: 1
21:07:59 team-a rolesets: svc-a-roleset-5jz8k svc-a-roleset-7bwhv  | svc-b still present: 1
21:08:09 team-a rolesets: svc-a-roleset-4k7hg svc-a-roleset-5n2gs  | svc-b still present: 1
```

**Step 4, confirm who is doing it and how much damage:**

```bash
kubectl -n aibrix-system logs deploy/aibrix-controller-manager --since=3m \
  | grep -A2 "syncing stormservice team-b/svc-b" | grep "delete roleset"

echo "team-a RoleSets deleted: $(kubectl -n aibrix-system logs deploy/aibrix-controller-manager --since=3m | grep -c 'delete roleset svc-a-roleset')"
echo "team-a Pods killed:      $(kubectl -n team-a get events --field-selector reason=Killing --no-headers | wc -l)"
```

Every deleted object belongs to team-a (these log lines come from inside the container and use UTC, nine hours behind the local time in the shell output above). The counts depend on how fast your environment is — other runs gave 16/25 and 18/16, so roughly the same magnitude:

```
I0922 12:06:52.068041 rolesetoperations.go:131] [rolesetoperation] delete roleset svc-a-roleset-sn2hh
I0922 12:07:07.088879 rolesetoperations.go:131] [rolesetoperation] delete roleset svc-a-roleset-wcdjk
I0922 12:07:19.088980 rolesetoperations.go:131] [rolesetoperation] delete roleset svc-a-roleset-4rjbm
I0922 12:07:19.092496 rolesetoperations.go:131] [rolesetoperation] delete roleset svc-a-roleset-c68ks
I0922 12:07:22.103210 rolesetoperations.go:131] [rolesetoperation] delete roleset svc-a-roleset-td4qg
I0922 12:07:37.111012 rolesetoperations.go:131] [rolesetoperation] delete roleset svc-a-roleset-h5sf9
I0922 12:07:52.118967 rolesetoperations.go:131] [rolesetoperation] delete roleset svc-a-roleset-gswh5
I0922 12:08:07.135679 rolesetoperations.go:131] [rolesetoperation] delete roleset svc-a-roleset-5jz8k

team-a RoleSets deleted: 14
team-a Pods killed:      12
```

**Cleanup.** Note that svc-b's finalizer has to be removed by hand, otherwise the namespace stays in Terminating:

```bash
kubectl -n team-b patch stormservice svc-b --type=json -p '[{"op":"remove","path":"/metadata/finalizers"}]'
kubectl delete ns team-a team-b
```

### Expected behavior

A StormService should only manage RoleSets in its own namespace: two namespaces shouldn't affect each other even if their selector labels collide, status should only count its own, and deleting one should only clean up its own and be able to finish.

I'm not sure whether this counts as a bug, but looking around the repo this seems to be how it's done elsewhere:

- The parallel `RayClusterFleet` path passes `client.InNamespace(fleet.Namespace)` when listing both ReplicaSets and RayClusters.
- **StormService itself does it too**: `revision.go` lists ControllerRevisions with `client.InNamespace(obj.GetNamespace())`. Only the RoleSet listing leaves it out.
- Across `pkg/controller/` there are 20 List calls with a namespace restriction; the ones without are mostly cluster-scoped resources or filter some other way.

Also, the ownerReference on a RoleSet points at the StormService in its own namespace (cross-namespace ownerReferences aren't valid in Kubernetes anyway), so reaching into other namespaces doesn't look intentional — more like a missing argument in the listing.

### I tried a change (not sure if it's right)

Locally I added a namespace parameter to `getRoleSetList` and restricted the List:

```go
-func (r *StormServiceReconciler) getRoleSetList(ctx context.Context, selector *metav1.LabelSelector) ([]*orchestrationv1alpha1.RoleSet, error) {
+func (r *StormServiceReconciler) getRoleSetList(ctx context.Context, namespace string, selector *metav1.LabelSelector) ([]*orchestrationv1alpha1.RoleSet, error) {
...
-	err = r.List(ctx, roleSetList, client.MatchingLabelsSelector{Selector: roleSetSelector})
+	err = r.List(ctx, roleSetList, client.InNamespace(namespace), client.MatchingLabelsSelector{Selector: roleSetSelector})
```

All 5 call sites now pass `stormService.Namespace`.

Re-running the steps above with the patched controller: team-a and team-b each created 2 RoleSets; after deleting svc-b, team-a's RoleSet UIDs stayed unchanged for 60 seconds with 0 deletes and 0 Pods killed, and svc-b was deleted immediately. The two namespaces that had been stuck in Terminating also disappeared as soon as the new controller came up.

I ran the unit tests for `pkg/controller/stormservice` and everything passed except `TestControllers`, which fails because I don't have the envtest etcd binary locally — it fails the same way on unmodified code, so it looks unrelated to this change.

I don't know whether this breaks anything else (is there somewhere that deliberately needs a cluster-wide view?). If the direction looks right I'm happy to open a PR and add a test: with same-labelled RoleSets in two namespaces, `getRoleSetList` should only return the ones from its own namespace.



### Environment

- AIBrix: main at `dcc8aa9a`. I also checked current main on GitHub and `getRoleSetList` still has no namespace restriction
- Cluster: single-node kind v1.30.0, controller-manager built from source with only `stormservice-controller` and `pod-autoscaler-controller` enabled, plus `--disable-webhook`
- Lightweight containers as the workload, no GPU. This path is in the control plane's resource listing, so it has nothing to do with the inference engine

### Area

Orchestration (controllers, CRDs)

## 评论 (4)

### github-actions[bot] · 2026-09-22

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.


### googs1025 · 2026-09-22

Confirmed: this is a real bug, and the reported behavior follows directly from the current code. `getRoleSetList` performs a cluster-wide list using only the user-provided selector, and its results feed scaling, rollout, status calculation, revision retention, and finalization. In particular, `finalize` passes every matching RoleSet to `deleteRoleSet`, so a StormService can delete matching RoleSets from another namespace through the controller-manager's privileges. This is also security-relevant in a multi-tenant cluster because it crosses the namespace authorization boundary.

Adding `client.InNamespace(stormService.Namespace)` at every lookup is the necessary minimum fix, and I do not see a legitimate need for a cluster-wide view: RoleSets are namespaced, the controller creates them in the StormService namespace, and their ownerReferences point to a StormService in that same namespace. The existing ControllerRevision and RayClusterFleet paths already apply namespace scoping.

I would also consider tightening ownership in the same change: have `getRoleSetList` accept the StormService object, list by namespace plus selector, and then retain only RoleSets for which `metav1.IsControlledBy(rs, stormService)` is true. Namespace scoping closes the cross-namespace issue; the owner check additionally prevents two StormServices with overlapping selectors in the same namespace from counting, updating, or deleting each other's RoleSets.

Suggested regression coverage:
- identical selectors in two namespaces return only RoleSets from the requested namespace;
- identical selectors in one namespace return only RoleSets owned by the requested StormService;
- finalizing one StormService does not delete foreign RoleSets and can still remove its finalizer;
- status only counts owned RoleSets.

The proposed direction is correct and should be treated as a high-priority fix.

### btxu-db · 2026-09-22

Thanks! I'll take this. Will add namespace scoping plus the IsControlledBy check, with the tests you listed.

### btxu-db · 2026-09-23

/assign
