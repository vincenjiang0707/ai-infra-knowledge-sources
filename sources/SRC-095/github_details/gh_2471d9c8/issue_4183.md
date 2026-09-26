# [Issue #4183] [KubeRay DashBoard] No Data from RayJob and RayService in Dashboard

source: https://github.com/ray-project/kuberay/issues/4183
state: open | updated: 2026-09-22T16:57:18Z
labels: stale

## 正文

<img width="1632" height="492" alt="Image" src="https://github.com/user-attachments/assets/d37f4405-5ce3-4314-9da5-0c717515b27d" />
<img width="1674" height="873" alt="Image" src="https://github.com/user-attachments/assets/80dfe22a-2b1f-4d09-9f68-5c141b4e11c8" />
<img width="1665" height="1223" alt="Image" src="https://github.com/user-attachments/assets/1006d65b-c6a0-4d81-9577-a07b3b07be41" />
<img width="1401" height="246" alt="Image" src="https://github.com/user-attachments/assets/5b0d32f3-7ee7-4295-b522-357fd17de607" />
<img width="810" height="315" alt="Image" src="https://github.com/user-attachments/assets/64b51b31-78ff-43e3-97b4-9dde22b112b7" />
<img width="1200" height="171" alt="Image" src="https://github.com/user-attachments/assets/36e7ad00-7f38-44eb-b96f-915d3baea4e2" />

## 评论 (3)

### Future-Outlier · 2025-11-10

Hi, can you provide a yaml file (or manifest) for us to reproduce?

### Qoooooooooooo · 2025-11-14

@Future-Outlier 

All of them use scripts from the official website installation tutoria

cluster.yaml
```yaml
---
# Source: ray-cluster/templates/raycluster-cluster.yaml
apiVersion: ray.io/v1
kind: RayCluster
metadata:
  name: raycluster-kuberay
  namespace: ray-system
  labels:
    helm.sh/chart: ray-cluster-1.4.2
    app.kubernetes.io/instance: raycluster
    app.kubernetes.io/managed-by: Helm
spec:
  headGroupSpec:
    serviceType: ClusterIP
    rayStartParams:
      dashboard-host: '0.0.0.0'
    template:
      metadata:
        labels:
          helm.sh/chart: ray-cluster-1.4.2
          app.kubernetes.io/instance: raycluster
          app.kubernetes.io/managed-by: Helm
      spec:
        containers:
        - name: ray-head
          image: rayproject/ray:2.46.0
          imagePullPolicy: IfNotPresent
          
          volumeMounts:
          - mountPath: /tmp/ray
            name: log-volume
          resources:
            limits:
              cpu: "1"
              memory: 4G
            requests:
              cpu: "1"
              memory: 2G
        volumes:
          - emptyDir: {}
            name: log-volume
  workerGroupSpecs:
  - groupName: workergroup
    replicas: 1
    minReplicas: 1
    maxReplicas: 3
    numOfHosts: 1
    rayStartParams: {}
    template:
      metadata:
        labels:
          helm.sh/chart: ray-cluster-1.4.2
          app.kubernetes.io/instance: raycluster
          app.kubernetes.io/managed-by: Helm
      spec:
        containers:
        - name: ray-worker
          image: rayproject/ray:2.46.0
          imagePullPolicy: IfNotPresent
          volumeMounts:
          - mountPath: /tmp/ray
            name: log-volume
          resources:
            limits:
              cpu: "1"
              memory: 1G
            requests:
              cpu: "1"
              memory: 1G
        volumes:
        - emptyDir: {}
          name: log-volume
```

job-sample.yaml
```yaml
apiVersion: ray.io/v1
kind: RayJob
metadata:
  name: rayjob-sample
spec:
  # submissionMode specifies how RayJob submits the Ray job to the RayCluster.
  # The default value is "K8sJobMode", meaning RayJob will submit the Ray job via a submitter Kubernetes Job.
  # The alternative value is "HTTPMode", indicating that KubeRay will submit the Ray job by sending an HTTP request to the RayCluster.
  # submissionMode: "K8sJobMode"
  entrypoint: python /home/ray/samples/sample_code.py
  # shutdownAfterJobFinishes specifies whether the RayCluster should be deleted after the RayJob finishes. Default is false.
  # shutdownAfterJobFinishes: false

  # ttlSecondsAfterFinished specifies the number of seconds after which the RayCluster will be deleted after the RayJob finishes.
  # ttlSecondsAfterFinished: 10

  # activeDeadlineSeconds is the duration in seconds that the RayJob may be active before
  # KubeRay actively tries to terminate the RayJob; value must be positive integer.
  # activeDeadlineSeconds: 120

  # RuntimeEnvYAML represents the runtime environment configuration provided as a multi-line YAML string.
  # See https://docs.ray.io/en/latest/ray-core/handling-dependencies.html for details.
  # (New in KubeRay version 1.0.)
  runtimeEnvYAML: |
    pip:
      - requests==2.26.0
      - pendulum==2.1.2
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
      rayStartParams: 
        dashboard-host: '0.0.0.0'
      #pod template
      template:
        spec:
          containers:
          - name: ray-head
            image: rayproject/ray:2.46.0
            ports:
            - containerPort: 6379
              name: gcs-server
            - containerPort: 8265 # Ray dashboard
              name: dashboard
            - containerPort: 10001
              name: client
            resources:
              limits:
                cpu: "1"
              requests:
                cpu: "200m"
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
            resources:
              limits:
                cpu: "1"
              requests:
                cpu: "200m"
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
    import os
    import requests

    ray.init()

    @ray.remote
    class Counter:
        def __init__(self):
            # Used to verify runtimeEnv
            self.name = os.getenv("counter_name")
            assert self.name == "test_counter"
            self.counter = 0

        def inc(self):
            self.counter += 1

        def get_counter(self):
            return "{} got {}".format(self.name, self.counter)

    counter = Counter.remote()

    for _ in range(5):
        ray.get(counter.inc.remote())
        print(ray.get(counter.get_counter.remote()))

    # Verify that the correct runtime env was used for the job.
    assert requests.__version__ == "2.26.0"
```

ray-service.no-ray-serve-replica.yaml
```yaml
apiVersion: ray.io/v1
kind: RayService
metadata:
  name: rayservice-no-ray-serve-replica
spec:
  serveConfigV2: |
    applications:
      - name: simple_app
        import_path: ray-operator.config.samples.ray-serve.single_deployment_dag:DagNode
        route_prefix: /basic
        runtime_env:
          working_dir: "https://github.com/ray-project/kuberay/archive/master.zip"
        deployments:
          - name: BaseService
            num_replicas: 2
            max_replicas_per_node: 1
            ray_actor_options:
              num_cpus: 0.1
  rayClusterConfig:
    rayVersion: '2.46.0'
    headGroupSpec:
      rayStartParams:
        object-store-memory: "200000000"  # 200MB
        dashboard-host: '0.0.0.0'
        num-cpus: "0"
      template:
        spec:
          containers:
          - name: ray-head
            image: rayproject/ray:2.46.0
            resources:
              limits:
                cpu: 2
                memory: 6Gi
              requests:
                cpu: 1
                memory: 4Gi
    workerGroupSpecs:
    - replicas: 2
      minReplicas: 1
      maxReplicas: 5
      groupName: small-group
      rayStartParams: {}
      template:
        spec:
          containers:
          - name: ray-worker
            image: rayproject/ray:2.46.0
            resources:
              limits:
                cpu: "2"
                memory: "4Gi"
              requests:
                cpu: "500m"
                memory: "2Gi"
```

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
