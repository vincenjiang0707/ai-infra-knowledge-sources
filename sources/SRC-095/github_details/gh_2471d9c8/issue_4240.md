# [Issue #4240] How to automatically run `ray serve start` with custom host/port after RayCluster head pod starts?

source: https://github.com/ray-project/kuberay/issues/4240
state: open | updated: 2026-09-22T16:57:29Z
labels: stale

## 正文

Hi team,

I'd like to configure Ray Serve in a KubeRay cluster to listen on `0.0.0.0:8100` instead of the default `127.0.0.1:8000`. The desired command is:

```bash
serve start --http-host 0.0.0.0 --http-port 8100
```

However, I’m struggling to automatically  run this **after** the Ray head process has fully started, within the KubeRay-managed `RayCluster`.

### What I’ve tried (and why it doesn’t work):

I attempted to set a custom `command` in the head container like this:

```yaml
headGroupSpec:
  template:
    spec:
      containers:
        - name: ray-head
          command:
            - /bin/bash
            - -lc
            - --
            - 'serve start --http-host 0.0.0.0 --http-port 8100'
```

But KubeRay **automatically appends** its own `ray start --head ...` command (including auto-generated flags like `--num-cpus`, `--memory`, `--dashboard-host=0.0.0.0`, etc.) to the end of my custom command. So the final executed command becomes effectively:

```bash
serve start --http-host 0.0.0.0 --http-port 8100 && ulimit -n 65536; ray start --head ...
```

Since `serve start` runs **before** `ray start`, Ray isn’t ready yet, and the Serve command fails silently or has no effect.

### Other approaches considered:

- **Manually writing the full `ray start` command**: If I override the entire command to include both `ray start` and `serve start` in the correct order, I lose KubeRay’s automatic parameter injection (e.g., CPU/memory/GPU limits from the CRD), which forces me to hardcode values—something I’d prefer to avoid.
  
- **Using a `postStart` lifecycle hook**: This could run `serve start` after the container starts, but there’s no guarantee that the Ray runtime is fully initialized. Without polling for Ray readiness (e.g., checking GCS or dashboard health), the `serve` command may still fail.

### Question:

Is there a recommended or elegant way in KubeRay to **automatically launch Ray Serve with custom HTTP settings (`--http-host`, `--http-port`) only after the Ray head node is fully ready**, while still preserving KubeRay’s automatic management of `ray start` arguments?

Ideally, it would be great if the RayCluster CRD supported a declarative Serve configuration (e.g., under headGroupSpec.serveConfig), but even a reliable workaround would be very helpful.


## 评论 (2)

### win5923 · 2025-12-07

Hi @tingjun-cs, `serveConfigV2` is the field used in RayService to configure Ray Serve applications. You can try this:
```
apiVersion: ray.io/v1
kind: RayService
metadata:
  name: rayservice-sample
spec:
  serveConfigV2: |
    applications:
      - name: fruit_app
        import_path: fruit.deployment_graph
        route_prefix: /fruit
        runtime_env:
          working_dir: "https://github.com/ray-project/test_dag/archive/78b4a5da38796123d9f9ffff59bab2792a043e95.zip"
        deployments:
          - name: MangoStand
            num_replicas: 1
            user_config:
              price: 3
            ray_actor_options:
              num_cpus: 0.1
          - name: OrangeStand
            num_replicas: 1
            user_config:
              price: 2
            ray_actor_options:
              num_cpus: 0.1
          - name: PearStand
            num_replicas: 1
            user_config:
              price: 1
            ray_actor_options:
              num_cpus: 0.1
          - name: FruitMarket
            num_replicas: 1
            ray_actor_options:
              num_cpus: 0.1
    http_options:
      port: 8100
      host: 0.0.0.0
```

Ref: https://github.com/ray-project/kuberay/blob/master/ray-operator/config/samples/ray-service.different-port.yaml

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
