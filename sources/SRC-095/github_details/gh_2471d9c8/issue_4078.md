# [Issue #4078] [RayCluster] Pods fail to auto-recover after node failure, requiring manual deletion of Terminating pods (KubeRay v1.2.2)

source: https://github.com/ray-project/kuberay/issues/4078
state: open | updated: 2026-09-22T16:57:01Z
labels: stale

## 正文

RayCluster pods do not automatically recover after a worker node failure, while other pods (including KubeRay Operator) are successfully rescheduled. Manual intervention (deleting Terminating pods) is required to trigger recovery.


Environment:
KubeRay Operator: v1.2.2
RayCluster: 2.34.0


Steps to Reproduce:
Deploy a RayCluster with 2 nodes.
Use kubectl cordon + kubectl drain to simulate node failure on one worker node.
Observe:
All non-Ray pods and KubeRay Operator pod reschedule normally on the healthy node.
RayCluster pods remain in Terminating state on the failed node.
No new Ray pods are created on the healthy node until manual deletion of Terminating pods.

Logs:
`{"level":"info","ts":"2025-09-08T08:41:44.505Z","logger":"controllers.RayCluster","msg":"inconsistentRayClusterStatus","RayCluster":{"name":"raycluster","namespace":"test"},"reconcileID":"80470da1-412a-4d2c-88cb-270fbbbf551f","detect inconsistency":"old ReadyWorkerReplicas: 1, new ReadyWorkerReplicas: 0, old AvailableWorkerReplicas: 2, new AvailableWorkerReplicas: 2, old DesiredWorkerReplicas: 2, new DesiredWorkerReplicas: 2, old MinWorkerReplicas: 2, new MinWorkerReplicas: 2, old MaxWorkerReplicas: 2, new MaxWorkerReplicas: 2"}
{"level":"info","ts":"2025-09-08T08:41:44.505Z","logger":"controllers.RayCluster","msg":"updateRayClusterStatus","RayCluster":{"name":"raycluster","namespace":"test"},"reconcileID":"80470da1-412a-4d2c-88cb-270fbbbf551f","name":"raycluster","old status":{"state":"ready","desiredCPU":"3","desiredMemory":"6Gi","desiredGPU":"0","desiredTPU":"0","lastUpdateTime":"2025-09-08T08:41:43Z","stateTransitionTimes":{"ready":"2025-09-01T15:13:44Z"},"endpoints":{"client":"10001","dashboard":"8265","metrics":"8080","redis":"6379","serve":"8000"},"head":{"podIP":"10.133.100.192","serviceIP":"10.133.100.192","podName":"raycluster-head-d6wh6","serviceName":"raycluster-head-svc"},"readyWorkerReplicas":1,"availableWorkerReplicas":2,"desiredWorkerReplicas":2,"minWorkerReplicas":2,"maxWorkerReplicas":2,"observedGeneration":2},"new status":{"state":"ready","desiredCPU":"3","desiredMemory":"6Gi","desiredGPU":"0","desiredTPU":"0","lastUpdateTime":"2025-09-08T08:41:44Z","stateTransitionTimes":{"ready":"2025-09-01T15:13:44Z"},"endpoints":{"client":"10001","dashboard":"8265","metrics":"8080","redis":"6379","serve":"8000"},"head":{"podIP":"10.133.100.192","serviceIP":"10.133.100.192","podName":"raycluster-head-d6wh6","serviceName":"raycluster-head-svc"},"availableWorkerReplicas":2,"desiredWorkerReplicas":2,"minWorkerReplicas":2,"maxWorkerReplicas":2,"observedGeneration":2}}
{"level":"info","ts":"2025-09-08T08:41:44.603Z","logger":"controllers.RayCluster","msg":"Error updating status","RayCluster":{"name":"raycluster","namespace":"test"},"reconcileID":"80470da1-412a-4d2c-88cb-270fbbbf551f","name":"raycluster","error":"Operation cannot be fulfilled on rayclusters.ray.io \"raycluster\": the object has been modified; please apply your changes to the latest version and try again","RayCluster":{"apiVersion":"ray.io/v1","kind":"RayCluster","namespace":"test","name":"raycluster"}}
{"level":"info","ts":"2025-09-08T08:41:44.603Z","logger":"controllers.RayCluster","msg":"Warning: Reconciler returned both a non-zero result and a non-nil error. The result will always be ignored if the error is non-nil and the non-nil error causes reqeueuing with exponential backoff. For more details, see: https://pkg.go.dev/sigs.k8s.io/controller-runtime/pkg/reconcile#Reconciler","RayCluster":{"name":"raycluster","namespace":"test"},"reconcileID":"80470da1-412a-4d2c-88cb-270fbbbf551f"}
{"level":"error","ts":"2025-09-08T08:41:44.603Z","logger":"controllers.RayCluster","msg":"Reconciler error","RayCluster":{"name":"raycluster","namespace":"test"},"reconcileID":"80470da1-412a-4d2c-88cb-270fbbbf551f","error":"Operation cannot be fulfilled on rayclusters.ray.io \"raycluster\": the object has been modified; please apply your changes to the latest version and try again","stacktrace":"sigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).reconcileHandler\n\t/home/runner/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.17.5/pkg/internal/controller/controller.go:329\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).processNextWorkItem\n\t/home/runner/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.17.5/pkg/internal/controller/controller.go:266\nsigs.k8s.io/controller-runtime/pkg/internal/controller.(*Controller).Start.func2.2\n\t/home/runner/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.17.5/pkg/internal/controller/controller.go:227"}
{"level":"info","ts":"2025-09-08T08:41:44.609Z","logger":"controllers.RayCluster","msg":"Reconciling Ingress","RayCluster":{"name":"raycluster","namespace":"test"},"reconcileID":"c0d67900-76d5-4789-9f01-249fdbb050ff"}
{"level":"info","ts":"2025-09-08T08:41:44.609Z","logger":"controllers.RayCluster","msg":"reconcileHeadService","RayCluster":{"name":"raycluster","namespace":"test"},"reconcileID":"c0d67900-76d5-4789-9f01-249fdbb050ff","1 head service found":"raycluster-head-svc"}
{"level":"info","ts":"2025-09-08T08:41:44.609Z","logger":"controllers.RayCluster","msg":"reconcilePods","RayCluster":{"name":"raycluster","namespace":"test"},"reconcileID":"c0d67900-76d5-4789-9f01-249fdbb050ff","Found 1 head Pod":"raycluster-head-d6wh6","Pod status":"Running","Pod status reason":"","Pod restart policy":"Always","Ray container terminated status":"nil"}`

## 评论 (1)

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
