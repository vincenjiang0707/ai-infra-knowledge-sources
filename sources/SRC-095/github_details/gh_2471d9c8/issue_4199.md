# [Issue #4199] [Bug] SidecarMode: submitter not wait RayCluster Running (Ready)

source: https://github.com/ray-project/kuberay/issues/4199
state: open | updated: 2026-09-22T16:57:23Z
labels: bug, 1.6.0, stale

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.


### KubeRay Component

ray-operator

### What happened + What you expected to happen

```yaml
NAME             JOB STATUS   DEPLOYMENT STATUS   RAY CLUSTER NAME       START TIME             END TIME   AGE
job-43n6os1dxr                Initializing        job-43n6os1dxr-2tzsh   2025-11-17T13:53:34Z              10s
```
```yaml
job-43n6os1dxr-2tzsh-head-nbhr9            2/2     Running            0             3m58s
job-43n6os1dxr-2tzsh-worker-worker-w5qqz   0/1     Running            1 (14s ago)   3m58s
```

KubeRay Operator：v1.5.0

The Worker was unable to access the Head due to a domain name resolution issue, but the submitter had already submitted the task, and the task ran in the Head. After the task finished, RayJob did not change to SUCCEEDED.

### Reproduction script

Perhaps we could try modifying the DNS resolution file mounted by the Worker.

### Anything else

_No response_

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (4)

### Future-Outlier · 2025-11-18

Hi, @sunran1203 can you provide a reproduce script?

### sunran1203 · 2025-11-18

```yaml
apiVersion: ray.io/v1
kind: RayJob
metadata:
  name: rayjob-sample
spec:
  backoffLimit: 0
  # submissionMode specifies how RayJob submits the Ray job to the RayCluster.
  # The default value is "K8sJobMode", meaning RayJob will submit the Ray job via a submitter Kubernetes Job.
  # The alternative value is "HTTPMode", indicating that KubeRay will submit the Ray job by sending an HTTP request to the RayCluster.
  submissionMode: "SidecarMode"
  entrypoint:  python /home/ray/samples/sample_code.py
  # shutdownAfterJobFinishes specifies whether the RayCluster should be deleted after the RayJob finishes. Default is false.
  shutdownAfterJobFinishes: true

  # ttlSecondsAfterFinished specifies the number of seconds after which the RayCluster will be deleted after the RayJob finishes.
  ttlSecondsAfterFinished: 30
  # deletionPolicy: DeleteSelf
  deletionStrategy:
    onFailure: 
      policy: "DeleteSelf"
    onSuccess:
      policy: "DeleteSelf"

  # activeDeadlineSeconds is the duration in seconds that the RayJob may be active before
  # KubeRay actively tries to terminate the RayJob; value must be positive integer.
  # activeDeadlineSeconds: 120

  # RuntimeEnvYAML represents the runtime environment configuration provided as a multi-line YAML string.
  # See https://docs.ray.io/en/latest/ray-core/handling-dependencies.html for details.
  # (New in KubeRay version 1.0.)
  runtimeEnvYAML: |
    env_vars:
      counter_name: "test_counter"

  # Suspend specifies whether the RayJob controller should create a RayCluster instance.
  # If a job is applied with the suspend field set to true, the RayCluster will not be created and we will wait for the transition to false.
  # If the RayCluster is already created, it will be deleted. In the case of transition to false, a new RayCluster will be created.
  # suspend: false

  # rayClusterSpec specifies the RayCluster instance to be created by the RayJob controller.
  rayClusterSpec:
    rayVersion: '2.46.0' # should match the Ray version in the image of the containers
    # Ray head pod template
    headGroupSpec:
      # The `rayStartParams` are used to configure the `ray start` command.
      # See https://github.com/ray-project/kuberay/blob/master/docs/guidance/rayStartParams.md for the default settings of `rayStartParams` in KubeRay.
      # See https://docs.ray.io/en/latest/cluster/cli.html#ray-start for all available options in `rayStartParams`.
      rayStartParams: {}
        # dashboard-host: 0.0.0.0
      #pod template
      template:
        spec:
          containers:
          - name: ray-head
            image: rayproject/ray:2.46.0
            ports:
            - containerPort: 6379
              name: gcs-server
            - containerPort: 8265
              name: dashboard
            - containerPort: 10001
              name: client
            env:
            resources:
              limits:
                cpu: "1"
                memory: 2Gi
              requests:
                cpu: "200m"
                memory: 2Gi
            volumeMounts:
            - mountPath: /home/ray/samples
              name: code-sample
          volumes:
          # You set volumes at the Pod level, then mount them into containers inside that Pod
          - name: code-sample
            configMap:
              # Provide the name of the ConfigMap you want to mount.
              name: ray-job-code-sample
              # An array of keys from the ConfigMap to create as files
              items:
              - key: sample_code.py
                path: sample_code.py
    workerGroupSpecs:
    # the pod replicas in this group typed worker
    - replicas: 1
      minReplicas: 1
      maxReplicas: 5
      # logical group name, for this called small-group, also can be functional
      groupName: small-group
      # The `rayStartParams` are used to configure the `ray start` command.
      # See https://github.com/ray-project/kuberay/blob/master/docs/guidance/rayStartParams.md for the default settings of `rayStartParams` in KubeRay.
      # See https://docs.ray.io/en/latest/cluster/cli.html#ray-start for all available options in `rayStartParams`.
      rayStartParams: {}
      #pod template
      template:
        spec:
          containers:
          - name: ray-worker # must consist of lower case alphanumeric characters or '-', and must start and end with an alphanumeric character (e.g. 'my-name',  or '123-abc'
            image: rayproject/ray:2.46.0
            env:
            resources:
              limits:
                cpu: "1"
                memory: 2Gi
              requests:
                cpu: "200m"
                memory: 2Gi
                # SubmitterPodTemplate is the template for the pod that will run the `ray job submit` command against the RayCluster.
                # If SubmitterPodTemplate is specified, the first container is assumed to be the submitter container.
                # submitterPodTemplate:
                #   spec:
                #     restartPolicy: Never
                #     containers:
                #       - name: my-custom-rayjob-submitter-pod
                #         image: rayproject/ray:2.46.0
                #         # If Command is not specified, the correct command will be supplied at runtime using the RayJob spec `entrypoint` field.
                #         # Specifying Command is not recommended.
                #         # command: ["sh", "-c", "ray job submit --address=http://$RAY_DASHBOARD_ADDRESS --submission-id=$RAY_JOB_SUBMISSION_ID -- echo hello world"]


######################Ray code sample#################################
# this sample is from https://docs.ray.io/en/latest/cluster/job-submission.html#quick-start-example
# it is mounted into the container and executed to show the Ray job at work
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: ray-job-code-sample
data:
  sample_code.py: |
    import ray
    import time
    from datetime import datetime

    # Initiate a driver.
    ray.init()

    @ray.remote
    def task_print():
        task_id = ray.get_runtime_context().get_task_id()
        for i in range(1, 60):
          current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
          print(f"[Task ID: {task_id}] [{current_time}] 第 {i+1} 次循环")
          time.sleep(1)  # 每秒打印一次

    ray.get(task_print.remote())
    exit(1)

```


It's just a simple script; this phenomenon was triggered by a DNS resolution issue.

### EagleLo · 2025-11-18

Hi @Future-Outlier , may I take on this?

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
