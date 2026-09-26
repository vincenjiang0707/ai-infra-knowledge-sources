# [Issue #4356] [Bug] Head pod will OOM in TestRayClusterAuthOptions

source: https://github.com/ray-project/kuberay/issues/4356
state: closed | updated: 2026-09-23T07:03:39Z
labels: bug, stale

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.


### KubeRay Component

ci

### What happened + What you expected to happen

```
➜  ~ k get raycluster -A
NAMESPACE       NAME                       DESIRED WORKERS   AVAILABLE WORKERS   CPUS   MEMORY   GPUS   STATUS   AGE
test-ns-5msxm   raycluster-auth-token      1                                     600m   2G       0               9s
test-ns-5q7cf   fail-jbgwb                 1                 1                   600m   2G       0               3m49s
test-ns-7r5v9   raycluster-embed-grafana   1                 1                   2      3G       0               175m
➜  ~ k get po -n test-ns-5msxm
NAME                                             READY   STATUS     RESTARTS   AGE
raycluster-auth-token-head-vbjrq                 0/1     Running    0          15s
raycluster-auth-token-small-group-worker-ksgpt   0/1     Init:0/1   0          15s
➜  ~ k get po -n test-ns-5msxm
NAME                                             READY   STATUS    RESTARTS   AGE
raycluster-auth-token-head-vbjrq                 0/1     Running   0          19s
raycluster-auth-token-small-group-worker-ksgpt   0/1     Running   0          19s
➜  ~ k get po -n test-ns-5msxm
NAME                                             READY   STATUS    RESTARTS   AGE
raycluster-auth-token-head-vbjrq                 0/1     Running   0          20s
raycluster-auth-token-small-group-worker-ksgpt   0/1     Running   0          20s
➜  ~ k get po -n test-ns-5msxm
NAME                                             READY   STATUS    RESTARTS   AGE
raycluster-auth-token-head-vbjrq                 0/1     Running   0          21s
raycluster-auth-token-small-group-worker-ksgpt   0/1     Running   0          21s
➜  ~ k get po -n test-ns-5msxm
NAME                                             READY   STATUS    RESTARTS   AGE
raycluster-auth-token-head-vbjrq                 0/1     Running   0          22s
raycluster-auth-token-small-group-worker-ksgpt   0/1     Running   0          22s
➜  ~ k get po -n test-ns-5msxm
NAME                                             READY   STATUS    RESTARTS   AGE
raycluster-auth-token-head-vbjrq                 0/1     Running   0          23s
raycluster-auth-token-small-group-worker-ksgpt   0/1     Running   0          23s
➜  ~ k get po -n test-ns-5msxm
NAME                                             READY   STATUS    RESTARTS   AGE
raycluster-auth-token-head-vbjrq                 0/1     Running   0          24s
raycluster-auth-token-small-group-worker-ksgpt   0/1     Running   0          24s
➜  ~ k get po -n test-ns-5msxm
NAME                                             READY   STATUS    RESTARTS   AGE
raycluster-auth-token-head-vbjrq                 0/1     Running   0          26s
raycluster-auth-token-small-group-worker-ksgpt   1/1     Running   0          26s
➜  ~ k get po -n test-ns-5msxm
NAME                                             READY   STATUS    RESTARTS   AGE
raycluster-auth-token-head-vbjrq                 0/1     Running   0          27s
raycluster-auth-token-small-group-worker-ksgpt   1/1     Running   0          27s
➜  ~ k get po -n test-ns-5msxm
NAME                                             READY   STATUS    RESTARTS   AGE
raycluster-auth-token-head-vbjrq                 0/1     Running   0          28s
raycluster-auth-token-small-group-worker-ksgpt   1/1     Running   0          28s
➜  ~ k get po -n test-ns-5msxm
NAME                                             READY   STATUS    RESTARTS   AGE
raycluster-auth-token-head-vbjrq                 0/1     Running   0          29s
raycluster-auth-token-small-group-worker-ksgpt   1/1     Running   0          29s
➜  ~ k get po -n test-ns-5msxm
NAME                                             READY   STATUS    RESTARTS   AGE
raycluster-auth-token-head-vbjrq                 0/1     Running   0          30s
raycluster-auth-token-small-group-worker-ksgpt   1/1     Running   0          30s
➜  ~ k get po -n test-ns-5msxm
NAME                                             READY   STATUS      RESTARTS   AGE
raycluster-auth-token-head-vbjrq                 0/1     OOMKilled   0          31s
raycluster-auth-token-small-group-worker-ksgpt   1/1     Running     0          31s
➜  ~ k get po -n test-ns-5msxm
NAME                                             READY   STATUS    RESTARTS     AGE
raycluster-auth-token-head-vbjrq                 0/1     Running   1 (2s ago)   32s
raycluster-auth-token-small-group-worker-ksgpt   1/1     Running   0            32s
➜  ~ k get po -n test-ns-5msxm raycluster-auth-token-head-vbjrq -oyaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    ray.io/ft-enabled: "false"
  creationTimestamp: "2026-01-08T08:06:40Z"
  generateName: raycluster-auth-token-head-
  generation: 1
  labels:
    app.kubernetes.io/created-by: kuberay-operator
    app.kubernetes.io/name: kuberay
    ray.io/cluster: raycluster-auth-token
    ray.io/group: headgroup
    ray.io/identifier: raycluster-auth-token-head
    ray.io/is-ray-node: "yes"
    ray.io/node-type: head
  name: raycluster-auth-token-head-vbjrq
  namespace: test-ns-5msxm
  ownerReferences:
  - apiVersion: ray.io/v1
    blockOwnerDeletion: true
    controller: true
    kind: RayCluster
    name: raycluster-auth-token
    uid: d8040107-8c3f-4d38-99d9-e76f547df547
  resourceVersion: "155444"
  uid: e7806229-e3c3-442c-b710-b58c7a5cb2dc
spec:
  containers:
  - args:
    - 'ulimit -n 65536; ray start --head  --block  --dashboard-agent-listen-port=52365  --dashboard-host=0.0.0.0  --memory=2000000000  --metrics-export-port=8080  --num-cpus=1 '
    command:
    - /bin/bash
    - -c
    - --
    env:
    - name: RAY_AUTH_MODE
      value: token
    - name: RAY_AUTH_TOKEN
      valueFrom:
        secretKeyRef:
          key: auth_token
          name: raycluster-auth-token
    - name: RAY_CLUSTER_NAME
      valueFrom:
        fieldRef:
          apiVersion: v1
          fieldPath: metadata.labels['ray.io/cluster']
    - name: RAY_CLOUD_INSTANCE_ID
      valueFrom:
        fieldRef:
          apiVersion: v1
          fieldPath: metadata.name
    - name: RAY_NODE_TYPE_NAME
      valueFrom:
        fieldRef:
          apiVersion: v1
          fieldPath: metadata.labels['ray.io/group']
    - name: KUBERAY_GEN_RAY_START_CMD
      value: 'ray start --head  --block  --dashboard-agent-listen-port=52365  --dashboard-host=0.0.0.0  --memory=2000000000  --metrics-export-port=8080  --num-cpus=1 '
    - name: RAY_PORT
      value: "6379"
    - name: RAY_ADDRESS
      value: 127.0.0.1:6379
    - name: RAY_USAGE_STATS_KUBERAY_IN_USE
      value: "1"
    - name: RAY_USAGE_STATS_EXTRA_TAGS
      value: kuberay_version=v1.5.1;kuberay_crd=RayCluster
    - name: RAY_DASHBOARD_ENABLE_K8S_DISK_USAGE
      value: "1"
    image: rayproject/ray:2.46.0
    imagePullPolicy: IfNotPresent
    livenessProbe:
      exec:
        command:
        - bash
        - -c
        - wget --tries 1 -T 2 -q -O- http://localhost:52365/api/local_raylet_healthz
          | grep success && wget --tries 1 -T 10 -q -O- http://localhost:8265/api/gcs_healthz
          | grep success
      failureThreshold: 120
      initialDelaySeconds: 30
      periodSeconds: 5
      successThreshold: 1
      timeoutSeconds: 5
    name: ray-head
    ports:
    - containerPort: 6379
      name: gcs-server
      protocol: TCP
    - containerPort: 8000
      name: serve
      protocol: TCP
    - containerPort: 8265
      name: dashboard
      protocol: TCP
    - containerPort: 10001
      name: client
      protocol: TCP
    - containerPort: 8080
      name: metrics
      protocol: TCP
    readinessProbe:
      exec:
        command:
        - bash
        - -c
        - wget --tries 1 -T 2 -q -O- http://localhost:52365/api/local_raylet_healthz
          | grep success && wget --tries 1 -T 10 -q -O- http://localhost:8265/api/gcs_healthz
          | grep success
      failureThreshold: 10
      initialDelaySeconds: 10
      periodSeconds: 5
      successThreshold: 1
      timeoutSeconds: 5
    resources:
      limits:
        cpu: 500m
        memory: 2G
      requests:
        cpu: 300m
        memory: 1G
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: File
    volumeMounts:
    - mountPath: /dev/shm
      name: shared-mem
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-7hwcc
      readOnly: true
  dnsPolicy: ClusterFirst
  enableServiceLinks: true
  nodeName: cn-hongkong.10.83.23.72
  preemptionPolicy: PreemptLowerPriority
  priority: 0
  restartPolicy: Always
  schedulerName: default-scheduler
  securityContext: {}
  serviceAccount: default
  serviceAccountName: default
  terminationGracePeriodSeconds: 30
  tolerations:
  - effect: NoExecute
    key: node.kubernetes.io/not-ready
    operator: Exists
    tolerationSeconds: 300
  - effect: NoExecute
    key: node.kubernetes.io/unreachable
    operator: Exists
    tolerationSeconds: 300
  volumes:
  - emptyDir:
      medium: Memory
      sizeLimit: 2G
    name: shared-mem
  - name: kube-api-access-7hwcc
    projected:
      defaultMode: 420
      sources:
      - serviceAccountToken:
          expirationSeconds: 3607
          path: token
      - configMap:
          items:
          - key: ca.crt
            path: ca.crt
          name: kube-root-ca.crt
      - downwardAPI:
          items:
          - fieldRef:
              apiVersion: v1
              fieldPath: metadata.namespace
            path: namespace
status:
  conditions:
  - lastProbeTime: null
    lastTransitionTime: "2026-01-08T08:06:41Z"
    observedGeneration: 1
    status: "True"
    type: PodReadyToStartContainers
  - lastProbeTime: null
    lastTransitionTime: "2026-01-08T08:06:40Z"
    observedGeneration: 1
    status: "True"
    type: Initialized
  - lastProbeTime: null
    lastTransitionTime: "2026-01-08T08:06:40Z"
    message: 'containers with unready status: [ray-head]'
    observedGeneration: 1
    reason: ContainersNotReady
    status: "False"
    type: Ready
  - lastProbeTime: null
    lastTransitionTime: "2026-01-08T08:06:40Z"
    message: 'containers with unready status: [ray-head]'
    observedGeneration: 1
    reason: ContainersNotReady
    status: "False"
    type: ContainersReady
  - lastProbeTime: null
    lastTransitionTime: "2026-01-08T08:06:40Z"
    observedGeneration: 1
    status: "True"
    type: PodScheduled
  containerStatuses:
  - allocatedResources:
      cpu: 300m
      memory: 1G
    containerID: containerd://930c9cb005df40d6b72a612b350c4cdf6148c59ccb9a1bd95c6980be3c0740ce
    image: docker.io/rayproject/ray:2.46.0
    imageID: docker.io/rayproject/ray@sha256:764d7d4bf276143fac2fe322fe41593bb36bbd4dbe7fe9a2d94b67acb736eae3
    lastState:
      terminated:
        containerID: containerd://87c2882d5a85261f012fa2a6a487533362857da187a6c89b1bc7a28ff99551bc
        exitCode: 137
        finishedAt: "2026-01-08T08:07:10Z"
        reason: OOMKilled
        startedAt: "2026-01-08T08:06:41Z"
    name: ray-head
    ready: false
    resources:
      limits:
        cpu: 500m
        memory: 1953125Ki
      requests:
        cpu: 300m
        memory: 1G
    restartCount: 1
    started: true
    state:
      running:
        startedAt: "2026-01-08T08:07:10Z"
    user:
      linux:
        gid: 100
        supplementalGroups:
        - 27
        - 100
        uid: 1000
    volumeMounts:
    - mountPath: /dev/shm
      name: shared-mem
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-7hwcc
      readOnly: true
      recursiveReadOnly: Disabled
  hostIP: 10.83.23.72
  hostIPs:
  - ip: 10.83.23.72
  observedGeneration: 1
  phase: Running
  podIP: 172.20.0.57
  podIPs:
  - ip: 172.20.0.57
  qosClass: Burstable
  startTime: "2026-01-08T08:06:40Z"

```

### Reproduction script

KUBERAY_TEST_ARCH=amd64 go test -v ./e2e/ -run TestRayClusterAuthOptions

sometimes happen, not always

### Anything else

_No response_

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (2)

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

### KunWuLuan · 2026-09-23

Closing this issue — it was specific to my local test environment and is no longer reproducing or blocking. If it resurfaces, I'll reopen with fresh details.
