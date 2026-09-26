# [Issue #4538] [Feature][operator] Support customizing autoscaler container command and args

source: https://github.com/ray-project/kuberay/issues/4538
state: open | updated: 2026-09-22T16:58:37Z
labels: enhancement, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

The autoscaler container's startup command is hardcoded:

```go
Args: []string{
    "ray kuberay-autoscaler --cluster-name $(RAY_CLUSTER_NAME) --cluster-namespace $(RAY_CLUSTER_NAMESPACE)",
},
```

Propose adding `Command` and `Args` fields to `AutoscalerOptions` so users can customize the autoscaler startup behavior.


### Use case

I want to customize the autoscaler startup command for:
1. Debugging purposes (e.g., adding custom logging, diagnostics)
2. Using a custom autoscaler image with different entrypoint

Example:

```yaml
autoscalerOptions:
  command: ["/bin/bash", "-c"]
  args:
    - |
      echo "Cluster: $(RAY_CLUSTER_NAME)"
      ray kuberay-autoscaler \
        --cluster-name $(RAY_CLUSTER_NAME) \
        --cluster-namespace $(RAY_CLUSTER_NAMESPACE)
```


### Related issues

None.

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (1)

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
