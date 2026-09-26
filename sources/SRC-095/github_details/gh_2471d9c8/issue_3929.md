# [Issue #3929] [Bug] KubeRay Job Executes on Submitter Pod Instead of Cluster with Multiple Entrypoint Commands

source: https://github.com/ray-project/kuberay/issues/3929
state: open | updated: 2026-09-22T16:56:14Z
labels: bug, stale

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.


### KubeRay Component

ray-operator

### What happened + What you expected to happen

Hey everyone!
I wanted to raise a potential bug we encountered while working with KubeRay and would appreciate your insights.

### Issue Summary:
When specifying multiple scripts or chaining several commands in the entrypoint field of a RayJob YAML, the job seems to execute on the jobSubmitterPod itself, rather than being submitted to the Ray cluster’s head node as expected.

### Details:

We are mounting data volumes and setting the entrypoint to run multiple commands/scripts in sequence. This has seemed to work in the past, but unsure if it's considered a best practice.
Instead of the job running on the head node or worker nodes, it runs entirely inside the jobSubmitterPod.

### Questions:

Is this the intended behavior when using multiple commands in the entrypoint?

- Could this be an issue with how we configure volume mounts or entrypoints in the RayJob spec?
- Or is this a possible bug at the KubeRay level?
- Any guidance or similar experiences would be greatly appreciated!

We are running KubeRay v1.4.2 installed via the helm chart.

### Reproduction script

Sharing an example KubeRay job configuration where we attach a data volume to all nodes — but exclude the submitter pod. We did try mounting the volume on the submitter pod, but it caused KubeRay to treat the cluster like a single node, and the scripts couldn’t connect properly.

```yaml
apiVersion: ray.io/v1
kind: RayJob
metadata:
  name: test5
spec:
  rayClusterSpec:
    headGroupSpec:
      rayStartParams:
        dashboard-host: 0.0.0.0
        node-ip-address: $MY_POD_IP
        node-manager-port: '9998'
        num-cpus: '0'
        num-gpus: '0'
        object-manager-port: '9999'
        port: '6379'
      template:
        metadata: {}
        spec:
          containers:
            - env:
                - name: CPU_REQUEST
                  valueFrom:
                    resourceFieldRef:
                      containerName: ray
                      divisor: '0'
                      resource: requests.cpu
                - name: CPU_LIMITS
                  valueFrom:
                    resourceFieldRef:
                      containerName: ray
                      divisor: '0'
                      resource: limits.cpu
                - name: MEMORY_REQUESTS
                  valueFrom:
                    resourceFieldRef:
                      containerName: ray
                      divisor: '0'
                      resource: requests.memory
                - name: MEMORY_LIMITS
                  valueFrom:
                    resourceFieldRef:
                      containerName: ray
                      divisor: '0'
                      resource: limits.memory
                - name: MY_POD_IP
                  valueFrom:
                    fieldRef:
                      fieldPath: status.podIP
                - name: ray_runtime_env_temporary_reference_expiration_s
                  value: '200'
                - name: no_proxy
                  value: '<REDACTED_IP_RANGES_AND_HOSTNAMES>'
                - name: pip_default_timeout
                  value: '5000'
                - name: http_proxy
                  value: '<REDACTED_PROXY_URL>'
                - name: https_proxy
                  value: '<REDACTED_PROXY_URL>'
              image: '<REDACTED_REGISTRY>/ray:2.44.1-py312-cu121-19'
              imagePullPolicy: IfNotPresent
              name: ray
              ports:
                - containerPort: 6379
                  name: gcs
                  protocol: TCP
                - containerPort: 8265
                  name: dashboard
                  protocol: TCP
                - containerPort: 10001
                  name: client
                  protocol: TCP
              resources:
                limits:
                  cpu: '2'
                  memory: '8Gi'
                requests:
                  cpu: '1'
                  memory: '6Gi'
              volumeMounts:
                - mountPath: /dev/shm
                  name: dshm
                - mountPath: /volume/cyan-skink
                  name: cyan-skink
          runtimeClassName: selinux
          serviceAccountName: default-editor
          volumes:
            - emptyDir:
                medium: Memory
              name: dshm
            - name: cyan-skink
              persistentVolumeClaim:
                claimName: cyan-skink
            - configMap:
                name: job-data
              name: job-data
    workerGroupSpecs:
      - groupName: worker
        maxReplicas: 1
        minReplicas: 1
        numOfHosts: 1
        rayStartParams:
          node-ip-address: $MY_POD_IP
        replicas: 1
        scaleStrategy: {}
        template:
          metadata: {}
          spec:
            containers:
              - env:
                  - name: CPU_REQUEST
                    valueFrom:
                      resourceFieldRef:
                        containerName: ray
                        divisor: '0'
                        resource: requests.cpu
                  - name: CPU_LIMITS
                    valueFrom:
                      resourceFieldRef:
                        containerName: ray
                        divisor: '0'
                        resource: limits.cpu
                  - name: MEMORY_REQUESTS
                    valueFrom:
                      resourceFieldRef:
                        containerName: ray
                        divisor: '0'
                        resource: requests.memory
                  - name: MEMORY_LIMITS
                    valueFrom:
                      resourceFieldRef:
                        containerName: ray
                        divisor: '0'
                        resource: limits.memory
                  - name: MY_POD_IP
                    valueFrom:
                      fieldRef:
                        fieldPath: status.podIP
                  - name: no_proxy
                    value: '<REDACTED_IP_RANGES_AND_HOSTNAMES>'
                  - name: pip_default_timeout
                    value: '5000'
                  - name: http_proxy
                    value: '<REDACTED_PROXY_URL>'
                  - name: https_proxy
                    value: '<REDACTED_PROXY_URL>'
                  - name: ray_runtime_env_temporary_reference_expiration_s
                    value: '200'
                image: '<REDACTED_REGISTRY>/ray:2.44.1-py312-cu121-19'
                imagePullPolicy: IfNotPresent
                lifecycle:
                  preStop:
                    exec:
                      command:
                        - /bin/sh
                        - '-c'
                        - ray stop
                name: ray
                ports:
                  - containerPort: 6379
                    name: gcs
                    protocol: TCP
                  - containerPort: 8265
                    name: dashboard
                    protocol: TCP
                  - containerPort: 10001
                    name: client
                    protocol: TCP
                resources:
                  limits:
                    cpu: '2'
                    memory: '8Gi'
                  requests:
                    cpu: '1'
                    memory: '6Gi'
                volumeMounts:
                  - mountPath: /dev/shm
                    name: dshm
                  - mountPath: /volume/cyan-skink
                    name: cyan-skink
            nodeSelector:
            runtimeClassName: selinux
            serviceAccountName: default-editor
            volumes:
              - emptyDir:
                  medium: Memory
                name: dshm
              - name: cyan-skink
                persistentVolumeClaim:
                  claimName: cyan-skink
              - configMap:
                  name: job-data
                name: job-data
  submissionMode: K8sJobMode
  backoffLimit: 0
  submitterPodTemplate:
    metadata:
      labels:
        factory.ai/job-submitter: ray-job-submitter
    spec:
      containers:
        - env:
            - name: http_proxy
              value: '<REDACTED_PROXY_URL>'
            - name: https_proxy
              value: '<REDACTED_PROXY_URL>'
            - name: ray_runtime_env_temporary_reference_expiration_s
              value: '200'
            - name: no_proxy
              value: '<REDACTED_IP_RANGES_AND_HOSTNAMES>'
            - name: pip_default_timeout
              value: '5000'
          image: '<REDACTED_REGISTRY>/ray:2.44.1-py312-cu121-19'
          imagePullPolicy: IfNotPresent
          name: ray-job-submitter
          resources: {}
      restartPolicy: Never
      serviceAccountName: default-editor
  jobId: test-5
  shutdownAfterJobFinishes: true
  ttlSecondsAfterFinished: 10
  # /volume/t.py lives in a data volume attached to head and work nodes, it works fine if entrypoint is one and if the echo command is removed
  entrypoint: echo 'hi' && python /volume/t.py && python /volume/t.py && python /volume/t.py && python /volume/t.py

```

t.py script:
```python
import ray
import os

# Connect to the Ray cluster (use address if needed)
ray.init()

# Get and print cluster resources
resources = ray.cluster_resources()
print("Cluster resources:")
for resource, amount in resources.items():
    print(f"  {resource}: {amount}")
```

Job Logs:
```
2025-08-09 07:10:39,437 INFO cli.py:39 -- Job submission server address: http://test-5-dfbxw-head-svc.test.svc.cluster.local:8265
2025-08-09 07:10:39,924 SUCC cli.py:63 -- -----------------------------------
2025-08-09 07:10:39,924 SUCC cli.py:64 -- Job 'test-5' submitted successfully
2025-08-09 07:10:39,924 SUCC cli.py:65 -- -----------------------------------
2025-08-09 07:10:39,924 INFO cli.py:289 -- Next steps
2025-08-09 07:10:39,924 INFO cli.py:290 -- Query the logs of the job:
2025-08-09 07:10:39,924 INFO cli.py:292 -- ray job logs test-5
2025-08-09 07:10:39,924 INFO cli.py:294 -- Query the status of the job:
2025-08-09 07:10:39,924 INFO cli.py:296 -- ray job status test-5
2025-08-09 07:10:39,924 INFO cli.py:298 -- Request the job to be stopped:
2025-08-09 07:10:39,924 INFO cli.py:300 -- ray job stop test-5
python: can't open file '/volume/t.py': [Errno 2] No such file or directory # THIS IS THE LINE and works fine if a single entrypoint script is present
2025-08-09 07:10:42,205 INFO cli.py:39 -- Job submission server address: http://test-5-dfbxw-head-svc.test.svc.cluster.local:8265
2025-08-09 07:10:39,507 INFO job_manager.py:531 -- Runtime env is setting up.
hi
2025-08-09 07:10:47,237 SUCC cli.py:63 -- ----------------------
2025-08-09 07:10:47,237 SUCC cli.py:64 -- Job 'test-5' succeeded
2025-08-09 07:10:47,237 SUCC cli.py:65 -- ----------------------
```

Again, only specifying one entrypoint submits it to the Ray head and then the code is accessible since the head node has a data volume

### Anything else

Running KubeRay v1.4.2

Thank you for your time!

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (3)

### peterghaddad · 2025-08-19

Hey @kevin85421, was curious if you had any initial thoughts on this.

### Future-Outlier · 2025-10-11

do you mind try light weight job submitter?
this might solve your problem!
https://github.com/ray-project/kuberay/pull/3943

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
