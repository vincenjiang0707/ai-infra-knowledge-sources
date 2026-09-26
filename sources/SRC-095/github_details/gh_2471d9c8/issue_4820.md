# [Issue #4820] [Bug] History Server GetContent with Aliyun OSS backend misses root dir in path key

source: https://github.com/ray-project/kuberay/issues/4820
state: open | updated: 2026-09-23T04:43:00Z
labels: bug, stale

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.


### KubeRay Component

historyserver

### What happened + What you expected to happen

When starting ray history server with `--runtime-class-name=aliyunoss --ray-root-dir=tmp`
It lists the objects just fine, as List() builds the prefix correctly with `path.Join(r.OssRootDir, clusterId, dir)`
However, GetContent passes fileName directly as the OSS key without root dir:
```bash
time="2026-05-09T02:41:11Z" level=info msg="[ListFiles]Returned objects in tmp/dlc1hphloqj7jax0_quotaf5jxu1uzuel/session_2026-05-08_18-35-06_774618_1/logs/. length of Contents: 0, length of CommonPrefixes: 2"
time="2026-05-09T02:41:11Z" level=info msg="[ListFiles]Returned objects in tmp/dlc1hphloqj7jax0_quotaf5jxu1uzuel/session_2026-05-08_18-35-06_774618_1/logs/1d7bb25c423b77f0e574527a9a6cc7c15563bd7e3b4f858f1c2087ad/events/. length of Contents: 3, length of CommonPrefixes: 0"
time="2026-05-09T02:41:11Z" level=info msg="Prepare to get object session_2026-05-08_18-35-06_774618_1/logs/1d7bb25c423b77f0e574527a9a6cc7c15563bd7e3b4f858f1c2087ad/events/event_CORE_WORKER_256.log info ..."
time="2026-05-09T02:41:11Z" level=error msg="Failed to get object session_2026-05-08_18-35-06_774618_1/logs/1d7bb25c423b77f0e574527a9a6cc7c15563bd7e3b4f858f1c2087ad/events/event_CORE_WORKER_256.log: operation error GetObject: Error returned by Service. \nHttp Status Code: 404. \nError Code: NoSuchKey. \nRequest Id: 69FE9EC7DA49ED3535648D9A. \nMessage: The specified key does not exist..\nEC: 0026-00000001.\nTimestamp: 2026-05-09 02:41:11 +0000 UTC.\nRequest Endpoint: GET https://pai-automation-test-hangzhou.oss-cn-hangzhou-internal.aliyuncs.com/session_2026-05-08_18-35-06_774618_1/logs/1d7bb25c423b77f0e574527a9a6cc7c15563bd7e3b4f858f1c2087ad/events/event_CORE_WORKER_256.log."
```

### Reproduction script

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: historyserver-demo
  labels:
    app: historyserver
spec:
  replicas: 1
  selector:
    matchLabels:
      app: historyserver
  template:
    metadata:
      labels:
        app: historyserver
    spec:
      containers:
      - name: historyserver
        env:
          - name: LOCAL_TEST
            value: "true"
          - name: ALIBABA_CLOUD_ACCESS_KEY_ID
            value: XXX
          - name: ALIBABA_CLOUD_ACCESS_KEY_SECRET
            value: XXX
          - name: OSS_ENDPOINT
            value: oss-cn-hangzhou-internal.aliyuncs.com
          - name: OSS_BUCKET
            value: pai-automation-test-hangzhou
          - name: OSS_REGION
            value: cn-hangzhou
        image: historyserver:v0.1.0
        imagePullPolicy: Always
        command:
        - historyserver
        - --runtime-class-name=aliyunoss
        - --ray-root-dir=tmp
        ports:
        - containerPort: 8080
        resources:
          limits:
            cpu: "500m"
```

### Anything else

_No response_

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (2)

### JiangJiaWei1103 · 2026-05-23

cc @KunWuLuan to take a look, thx!

### github-actions[bot] · 2026-09-23

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
