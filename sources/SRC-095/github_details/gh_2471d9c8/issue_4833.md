# [Issue #4833] Question: what's the definition of a "live" ray cluster?

source: https://github.com/ray-project/kuberay/issues/4833
state: open | updated: 2026-09-23T04:43:06Z
labels: stale

## 正文

Hi team, when I was checking ray cluster history status, I found after RayJob has completed, the cluster still show `live`.

<img width="3409" height="452" alt="Image" src="https://github.com/user-attachments/assets/c162c116-7bb2-4255-8432-17bc56de5a4e" />

Checking through the source code, I found `liveClusters` are returned as long as the k8s custom resource (CR) still lives in etcd.
https://github.com/ray-project/kuberay/blob/b110189e7b656d8c5ae6ca709befa3818bc865a6/historyserver/pkg/historyserver/reader.go#L49

I'm wondering if it's better to use different status to tell apart "completed" and "live" ones?
Example change
```diff
--- a/historyserver/pkg/historyserver/reader.go
+++ b/historyserver/pkg/historyserver/reader.go
@@ -50,6 +50,11 @@ func (s *ServerHandler) listClusters(limit int) []utils.ClusterInfo {
        liveClusterNames := []string{}
        liveClusterInfos := []utils.ClusterInfo{}
        for _, liveCluster := range liveClusters {
+               if liveCluster.Status.Head.ServiceName == "" {
+                       logrus.Debugf("Skipping RayCluster %s/%s from live list: head service not ready (cluster is terminated or suspended)",
+                               liveCluster.Namespace, liveCluster.Name)
+                       continue
+               }
                liveClusterInfo := utils.ClusterInfo{
```

## 评论 (1)

### github-actions[bot] · 2026-09-23

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
