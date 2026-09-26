# [Issue #4654] [Feature][History Server] Declutter history server manifest with alternative solution for lifecycle hook

source: https://github.com/ray-project/kuberay/issues/4654
state: open | updated: 2026-09-22T16:59:13Z
labels: enhancement, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

Currently for history server, users will have this segment: 
```
lifecycle:
  postStart:
    exec:
      command:
      - /bin/sh
      - -lc
      - --
      - |
        GetNodeId(){
          while true;
          do
            nodeid=$(ps -ef | grep raylet | grep node_id | grep -v grep | grep -oP '(?<=--node_id=)[^ ]*')
            if [ -n "$nodeid" ]; then
              echo "$(date) raylet started: \"$(ps -ef | grep raylet | grep node_id | grep -v grep | grep -oP '(?<=--node_id=)[^ ]*')\" => ${nodeid}" >> /tmp/ray/init.log
              echo $nodeid > /tmp/ray/raylet_node_id
              break
            else
              echo "$(date) raylet not start >> /tmp/ray/init.log"
              sleep 1
            fi
          done
        }
        GetNodeId
```
in the manifest. Can we find a better solution for this so its less clutter also less hacky.

### Use case

N/A

### Related issues

N/A

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (9)

### tobby168 · 2026-04-04

Hi @chiayi @andrewsykim , I'd like to work on this issue. I've spent some time investigating approaches and testing them in a real K8s cluster. Here's what I found.

## Investigation: Can the Collector discover node ID on its own?

I tested four approaches from inside a **sidecar container** (simulating the Collector) on kind + Ray 2.44.0.

| Approach | Result | Why |
|----------|--------|-----|
| Scan `/proc/*/cmdline` in Go | **Not viable** | K8s isolates PID namespaces per container (`shareProcessNamespace` defaults to `false`). The Collector sidecar cannot see the Ray container's processes. |
| Extract node ID from port filenames | **Not viable on Ray 2.44+** | Ray no longer writes individual `{port_name}_{node_id}` files. It uses a single `ports_by_node.json` that does not contain the node ID. |
| Query Ray Dashboard API | **Viable but has gaps** | Works for initial discovery. However, when the Ray container is OOMKilled, only that container restarts — the Collector sidecar stays alive with the stale node ID. Nobody rewrites `raylet_node_id`, so `EventCollector.watchNodeIDFile()` never detects the change. |
| Upstream Ray change | **Cleanest long-term** | Have raylet write node ID to a file at startup. But this requires a change in `ray-project/ray`. |

The core difficulty: any Collector-side solution must handle the OOMKill case where the Ray container restarts but the Collector doesn't. The current `postStart` hook naturally solves this because it runs again on every container restart.

## Alternative proposal: Operator auto-injection

Instead of replacing the `postStart` hook mechanism, what if we eliminate the **user burden** of writing it?

The main pain point isn't that the shell script exists — it's that users must copy ~60 lines of boilerplate (postStart hook + Collector sidecar + shared volume + event env vars) into every RayCluster manifest, for both head and worker groups.

I prototyped an approach where the operator auto-injects everything when it sees an annotation. Here's what the user's YAML looks like:

**Before (current):** users manually add ~120 lines across head + worker specs — postStart hook, Collector container, shared volume, event env vars.

**After:** users add one annotation per pod template:
```yaml
template:
  metadata:
    annotations:
      ray.io/inject-history-server-collector: "true"
```

The operator automatically injects:
1. **postStart lifecycle hook** — same node ID extraction logic, but using `awk` instead of `grep -oP` for portability
2. **Collector sidecar container** with default resource limits
3. **Shared `/tmp/ray` emptyDir volume** on both containers
4. **Ray event export env vars** (`RAY_enable_ray_event`, etc.)

I verified this end-to-end on kind + KubeRay operator (built from master) + Ray 2.44.0. Both head and worker pods had the Collector injected, and `/tmp/ray/raylet_node_id` was correctly written.

### Why this approach

- **Zero change to the node ID discovery mechanism** — the postStart hook is proven and handles OOMKill naturally
- **Fixes the portability issue** — `awk` works on all base images, unlike `grep -oP`
- **Eliminates user boilerplate** — one annotation instead of ~120 lines of YAML
- **Hook script maintained in one place** — inside the operator, not scattered across user manifests
- **No upstream Ray dependency** — works today

### Prototype code

- [`history_server.go`](https://github.com/ray-project/kuberay/blob/master/ray-operator/controllers/ray/common/pod.go) — injection logic (~130 lines), called from `BuildPod()`
- [`history_server_test.go`](https://github.com/ray-project/kuberay/blob/master/ray-operator/controllers/ray/common/pod.go) — 6 unit tests covering: enabled/disabled, custom image, preserves existing hooks, skips existing env vars, custom runtime class

### Open questions

1. Does auto-injection via annotation feel right, or would you prefer a dedicated CRD field (e.g. `spec.historyServerCollector.enabled`)?
2. Storage backend configuration (S3 credentials, bucket, endpoint) still needs to be passed somehow — annotation-based env vars, operator ConfigMap, or a CRD field?
3. Is there any reason the Ray containers need `privileged: true` / `allowPrivilegeEscalation: true` besides the postStart hook? If not, the injection could skip those.

Happy to put up a PR if this direction makes sense.


### chiayi · 2026-04-09

Thank you for taking a look at the issue and the detailed investigation! Overall, operator auto-injection solution looks good to me. 

For the open questions: 1. I would prefer a dedicated field, it's more robust and future-proof. 2. I can't really comment for S3/Azure but since it deals with credentials, I would definitely go with Secrets/ConfigMaps. 3. That can be removed, it was only used for the postStart hook (@KunWuLuan please correct me if I'm wrong). 

@Future-Outlier @KunWuLuan PTAL as well! 

### tobby168 · 2026-04-10

Thanks for the quick feedback, @chiayi! I've addressed all three points in #4689:

1. **CRD field** — added `HistoryServerCollectorOptions` to `RayClusterSpec`, alongside `AutoscalerOptions`. Supports `Image`, `ImagePullPolicy`, `RuntimeClassName`, `Resources`, `Env`, and `EnvFrom`.
2. **Secrets / ConfigMaps** — storage credentials go through `EnvFrom` (both `secretRef` and `configMapRef` supported), so nothing sensitive appears in the RayCluster spec itself. Verified end-to-end that `kubectl describe` shows the Secret/ConfigMap correctly bound to the Collector sidecar.
3. **`privileged: true`** — removed from all three example manifests under `historyserver/config/`. Verified that neither `ray-head` nor `ray-worker` has the flag after injection. @KunWuLuan please flag if there's any other reason it was needed.

PR is verified end-to-end on kind + Ray 2.44.0 (Head + Worker pods both get the sidecar injected, awk-based postStart hook writes `raylet_node_id` correctly). Happy to iterate on anything in the review.

### Future-Outlier · 2026-04-10

Hi, @tobby168 
how did the collector work when you are using Ray 2.44.0?
we didn't support event until Ray 2.49.0

### tobby168 · 2026-04-10

Good question, @Future-Outlier! The initial E2E test on Ray 2.44.0 was only verifying the **operator injection mechanism** — that the sidecar gets injected, the postStart hook writes `raylet_node_id`, the shared volume is mounted, and the env vars are set correctly. I used `rayproject/ray:2.44.0` as a placeholder image for the collector container since I didn't have the real collector image handy at that point.

After your comment, I ran a **full pipeline test** on Ray 2.52.0 with the real collector binary + MinIO as the S3 backend. Results in commit cb00474:

- Built the real `collector:v0.1.0` image from `historyserver/Dockerfile.collector`
- Deployed on kind with MinIO + KubeRay operator + Ray 2.52.0
- Collector started successfully on both Head (`--role=Head`) and Worker (`--role=Worker`) pods
- Collector auto-created the S3 bucket, began watching the logs directory and polling dashboard endpoints
- Submitted a Ray job with tasks and actors
- On graceful cluster deletion, logs and events were flushed to S3 with the correct path structure:
  ```
  {root}/{clusterName}_{namespace}/{sessionID}/logs/{nodeID}/
    dashboard.log, dashboard_agent.log, raylet.out, debug_state.txt,
    events/event_AUTOSCALER.log, event_GCS.log, event_RAYLET.log, ...
  ```

I also found and fixed a few issues during this test (port 8080 conflict with Ray's metrics exporter, missing `--role` / `--ray-cluster-name` flags, missing `Command: ["collector"]` since the Dockerfile has no ENTRYPOINT) — all addressed in the latest push.

I'll update the PR description and example manifests to use Ray 2.52.0 as the minimum tested version.

### KunWuLuan · 2026-04-13

@tobby168 `privileged: true` can be removed, I think it is not necessary.

### tobby168 · 2026-04-14

@Future-Outlier should we have a discussion to see how we want to process this further?

### Future-Outlier · 2026-04-14

> [@Future-Outlier](https://github.com/Future-Outlier) should we have a discussion to see how we want to process this further?

not now, we should keep this as backlog, if you want to contribute kuberay, you can help review PR first

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
