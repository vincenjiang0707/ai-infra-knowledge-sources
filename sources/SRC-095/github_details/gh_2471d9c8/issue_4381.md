# [Issue #4381] [Feature][history server] support endpoint `/api/cluster_status`

source: https://github.com/ray-project/kuberay/issues/4381
state: open | updated: 2026-09-22T16:57:58Z
labels: stale

## 正文

(empty)

## 评论 (10)

### Future-Outlier · 2026-01-13

Hi, @justinyeh1995 do you want to try this?

### justinyeh1995 · 2026-01-13

Yes, I would love to work on this. Thank you!

### justinyeh1995 · 2026-01-19

While developing the endpoint, I ran into a discrepancy between Ray Dashboard’s `/api/cluster_status` and `ray status`

### Context 

we would like to reconstruct dead cluster session to be as close as the live session.
for the live session, we expect historyserver to redirect request to ray dashboard.
so understanding what ray dashboard response with is important to understand how to reconstruct the status.

### Environment 
Ray: 2.52.0
kuberay commit commit 0da1deae098d4656d7cd695930d26f1a75d1a843

### How I tested it
Enable autoscaling for a RayCluster via:
spec.enableInTreeAutoscaling: true
spec.autoscalerOptions:...

I created a yaml file `historyserver/config/raycluster_autoscaler.yaml`; full YAML below.
```yaml
apiVersion: ray.io/v1
kind: RayCluster
metadata:
  labels:
    ray.io/cluster: raycluster-historyserver
  name: raycluster-historyserver
  namespace: default
spec:
  rayVersion: "2.52.0"
  enableInTreeAutoscaling: true # <--- autoscaling
  autoscalerOptions:
    upscalingMode: Default
    idleTimeoutSeconds: 60
    imagePullPolicy: IfNotPresent
    env: []
    envFrom: []
    resources:
      limits:
        cpu: "500m"
        memory: "512Mi"
      requests:
        cpu: "500m"
        memory: "512Mi"
  headGroupSpec:
    rayStartParams:
      dashboard-host: 0.0.0.0
      num-cpus: "0"
    serviceType: ClusterIP
    template:
      metadata:
        labels:
          test: raycluster-historyserver
      spec:
        imagePullSecrets:
        affinity:
        containers:
        - env:
          - name: RAY_enable_ray_event
            value: "true"
          - name: RAY_enable_core_worker_ray_event_to_aggregator
            value: "true"
          - name: RAY_DASHBOARD_AGGREGATOR_AGENT_EVENTS_EXPORT_ADDR
            value: "http://localhost:8084/v1/events"
            # in ray 2.52.0, we need to set RAY_DASHBOARD_AGGREGATOR_AGENT_EXPOSABLE_EVENT_TYPES
            # in ray 2.53.0 (not yet done). we need to set RAY_DASHBOARD_AGGREGATOR_AGENT_PUBLISHER_HTTP_ENDPOINT_EXPOSABLE_EVENT_TYPES
          - name: RAY_DASHBOARD_AGGREGATOR_AGENT_EXPOSABLE_EVENT_TYPES
            value: "TASK_DEFINITION_EVENT,TASK_LIFECYCLE_EVENT,ACTOR_TASK_DEFINITION_EVENT,
                    TASK_PROFILE_EVENT,DRIVER_JOB_DEFINITION_EVENT,DRIVER_JOB_LIFECYCLE_EVENT,
                    ACTOR_DEFINITION_EVENT,ACTOR_LIFECYCLE_EVENT,NODE_DEFINITION_EVENT,NODE_LIFECYCLE_EVENT"
          image: rayproject/ray:2.52.0
          imagePullPolicy: IfNotPresent
          command:
          - 'echo "=========================================="; [ -d "/tmp/ray/session_latest" ] && dest="/tmp/ray/prev-logs/$(basename $(readlink /tmp/ray/session_latest))/$(cat /tmp/ray/raylet_node_id)" && echo "dst is $dest" && mkdir -p "$dest" && mv /tmp/ray/session_latest/logs "$dest/logs"; echo "========================================="'
          securityContext:
            allowPrivilegeEscalation: true
            privileged: true
          name: ray-head
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
          resources:
            limits:
              cpu: "5"
              memory: 10G
            requests:
              cpu: "50m"
              memory: 1G
          volumeMounts:
          - name: historyserver
            mountPath: /tmp/ray
        - name: collector
          image: collector:v0.1.0
          imagePullPolicy: IfNotPresent
          env:
          - name: S3DISABLE_SSL
            value: "true"
          - name: AWS_S3ID
            value: minioadmin
          - name: AWS_S3SECRET
            value: minioadmin
          - name: AWS_S3TOKEN
            value: ""
          - name: S3_BUCKET
            value: "ray-historyserver"
          - name: S3_ENDPOINT
            value: "minio-service.minio-dev:9000"
          - name: S3_REGION
            value: "test"
          - name: S3FORCE_PATH_STYLE
            value: "true"
          command:
          - collector
          - --role=Head
          - --runtime-class-name=s3
          - --ray-cluster-name=raycluster-historyserver
          - --ray-root-dir=log
          - --events-port=8084
          volumeMounts:
          - name: historyserver
            mountPath: /tmp/ray
        tolerations:
        - key: ray
          operator: Equal
          value: cpu
        volumes:
        - name: historyserver
          emptyDir: {}
  workerGroupSpecs:
  - groupName: cpu
    maxReplicas: 10
    minReplicas: 0
    numOfHosts: 1
    rayStartParams: {}
    replicas: 0
    template:
      metadata:
        labels:
          test: raycluster-historyserver
      spec:
        imagePullSecrets:
        containers:
        - env:
          - name: RAY_enable_ray_event
            value: "true"
          - name: RAY_enable_core_worker_ray_event_to_aggregator
            value: "true"
          - name: RAY_DASHBOARD_AGGREGATOR_AGENT_EVENTS_EXPORT_ADDR
            value: "http://localhost:8084/v1/events"
            # in ray 2.52.0, we need to set RAY_DASHBOARD_AGGREGATOR_AGENT_EXPOSABLE_EVENT_TYPES
            # in ray 2.53.0 (not yet done). we need to set RAY_DASHBOARD_AGGREGATOR_AGENT_PUBLISHER_HTTP_ENDPOINT_EXPOSABLE_EVENT_TYPES
          - name: RAY_DASHBOARD_AGGREGATOR_AGENT_EXPOSABLE_EVENT_TYPES
            value: "TASK_DEFINITION_EVENT,TASK_LIFECYCLE_EVENT,ACTOR_TASK_DEFINITION_EVENT,
                    TASK_PROFILE_EVENT,DRIVER_JOB_DEFINITION_EVENT,DRIVER_JOB_LIFECYCLE_EVENT,
                    ACTOR_DEFINITION_EVENT,ACTOR_LIFECYCLE_EVENT,NODE_DEFINITION_EVENT,NODE_LIFECYCLE_EVENT"
          image: rayproject/ray:2.52.0
          command:
          - 'echo "=========================================="; [ -d "/tmp/ray/session_latest" ] && dest="/tmp/ray/prev-logs/$(basename $(readlink /tmp/ray/session_latest))/$(cat /tmp/ray/raylet_node_id)" && echo "dst is $dest" && mkdir -p "$dest" && mv /tmp/ray/session_latest/logs "$dest/logs"; echo "========================================="'
          imagePullPolicy: IfNotPresent
          name: ray-worker
          securityContext:
            allowPrivilegeEscalation: true
            privileged: true
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
          resources:
            limits:
              cpu: "2"
              memory: 2G
            requests:
              cpu: "50m"
              memory: 1G
          volumeMounts:
          - name: historyserver
            mountPath: /tmp/ray
        - name: collector
          image: collector:v0.1.0
          imagePullPolicy: IfNotPresent
          env:
          - name: AWS_S3ID
            value: minioadmin
          - name: AWS_S3SECRET
            value: minioadmin
          - name: AWS_S3TOKEN
            value: ""
          - name: S3_BUCKET
            value: "ray-historyserver"
          - name: S3_ENDPOINT
            value: "minio-service.minio-dev:9000"
          - name: S3_REGION
            value: "test"
          - name: S3FORCE_PATH_STYLE
            value: "true"
          - name: S3DISABLE_SSL
            value: "true"
          command:
          - collector
          - --role=Worker
          - --runtime-class-name=s3
          - --ray-cluster-name=raycluster-historyserver
          - --ray-root-dir=log
          - --events-port=8084
          volumeMounts:
          - name: historyserver
            mountPath: /tmp/ray
        tolerations:
        - key: ray
          operator: Equal
          value: cpu
        volumes:
        - name: historyserver
          emptyDir: {}
```


### Steps

```
kubectl apply -f historyserver/config/raycluster_autoscaler.yaml
kubectl apply -f historyserver/config/rayjob.yaml

kubectl port-forward svc/raycluster-historyserver-head-svc 8265:8265
curl -sS http://localhost:8265/api/cluster_status
```
```
kubectl get pods
NAME                                        READY   STATUS     RESTARTS       AGE
historyserver-demo-cccd46d8c-trhpw          1/1     Running    3 (72m ago)    47h
kuberay-operator-55c5876776-cf9cw           1/1     Running    40 (47m ago)   31d
raycluster-historyserver-cpu-worker-qwkwk   0/2     Init:0/1   0              8s
raycluster-historyserver-head-89mls         3/3     Running    0              4m32s
rayjob-mtksj                                1/1     Running    0              17s
```

### Observed behavior

`/api/cluster_status` returns null autoscaling fields:

```
{"result": true, "msg": "Got cluster status.", "data": {"autoscalingStatus": null, "autoscalingError": null, "clusterStatus": null}}%
```

But ray status from inside the head pod shows autoscaler activity and worker terminations:
```
kubectl exec raycluster-historyserver-head-89mls -c ray-head -- ray status
```
shows

```
======== Autoscaler status: 2026-01-19 07:33:01.779772 ========
Node status
---------------------------------------------------------------
Active:
 (no active nodes)
Idle:
 1 headgroup
Pending:
 (no pending nodes)
Recent failures:
 cpu: NodeTerminated (instance_id: raycluster-historyserver-cpu-worker-qwkwk)
 cpu: NodeTerminated (instance_id: raycluster-historyserver-cpu-worker-ws2nx)

Resources
---------------------------------------------------------------
Total Usage:
 0B/9.31GiB memory
 0B/1.27GiB object_store_memory

From request_resources:
 (none)
Pending Demands:
 (no resource demands)
```

### Question

Which one should be treated as the source of truth for autoscaling status?

Is `/api/cluster_status` expected to report autoscaling status when using autoscaling in Ray 2.52.0?

Or is `ray status` the authoritative view, with the dashboard API lagging or unsupported in this configuration?

### machichima · 2026-01-19

I think it’s the problem in ray dashboard API. There’s a TODO comment saying that we should get cluster status from the autoscaler directly with V2: https://github.com/ray-project/ray/blob/04964bc4ca7992c08fc463769284d5daaa65e40c/python/ray/dashboard/modules/reporter/reporter_head.py#L105-L107

When calling ray status, it’s using `GcsClient.get_cluster_status()` rather than `internal_kv_get()` (used in `/api/cluster_status`): https://github.com/machichima/ray/blob/04964bc4ca7992c08fc463769284d5daaa65e40c/python/ray/autoscaler/_private/commands.py#L137-L137

We should modify `/api/cluster_status` to use `GcsClient.get_cluster_status()` for getting cluster status if using autoscaler v2

### Future-Outlier · 2026-01-20

We should support `/api/cluster_status` first until ray dashboard's `/api/cluster_status` endpoint change to V2's behavior.
nice point @justinyeh1995 

actionable steps:
1. support   `/api/cluster_status` (current dashboard implementation)
2. support ray dashboard API with autoscaler V2
3. support  `/api/cluster_status` (V2 status)

### justinyeh1995 · 2026-01-20

Got it! Thanks for all the suggestion. I will first implement the endpoint as-is. Then, raise an issue and address the ray dashboard API TODO comment, and finally update the endpoint to match the fix.

### justinyeh1995 · 2026-01-21

Found out the endpoint actually supports query parameter `format`. `/api/cluster_status?format=1` will return 

```json
{
  "result": true,
  "msg": "Got formatted cluster status.",
  "data": {
    "clusterStatus": "======== Autoscaler status: 2026-01-21 02:05:25.227901 ========\nNode status\n---------------------------------------------------------------\nActive:\n (no active nodes)\nIdle:\n 1 headgroup\nPending:\n (no pending nodes)\nRecent failures:\n cpu: NodeTerminated (instance_id: raycluster-historyserver-cpu-worker-dw6z9)\n\nResources\n---------------------------------------------------------------\nTotal Usage:\n 0B/9.31GiB memory\n 0B/1.35GiB object_store_memory\n\nFrom request_resources:\n (none)\nPending Demands:\n (no resource demands)"
  }
}
```
as it under the hood uses autoscaler V2 when format is 1. 

On the contrary, all the other cases use autoscaler V1. This PR will support both scenarios.

### Future-Outlier · 2026-02-28

todo: add back autoscaler event support

### justinyeh1995 · 2026-04-07

Related PR in ray that supports autoscaler event
https://github.com/ray-project/ray/pull/61859
https://github.com/ray-project/ray/pull/61860
https://github.com/ray-project/ray/pull/61861

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
