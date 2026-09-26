# [Issue #4787] [Bug]  config map issue, --config file overrides CLI flags with zero values for unset fields

source: https://github.com/ray-project/kuberay/issues/4787
state: open | updated: 2026-09-23T04:42:56Z
labels: bug, stale

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.


### KubeRay Component

ray-operator

### What happened + What you expected to happen

Description:

When the --config flag is used to load a Configuration CR from a file, fields not explicitly set in the config file override their corresponding CLI flags with Go zero values (false for bool, "" for string, 0 for int).

Expected behavior:

CLI flags should take precedence over unset fields in the config file, or unset fields in the config file should not override CLI flags. The config file should only override CLI flags for fields that are explicitly defined in the YAML.

Actual behavior:

The config file is unmarshaled into the Configuration struct, which initializes all fields to their zero values. These zero values then override the CLI flags regardless of whether the field was present in the config file.

### Reproduction script

Steps to reproduce:

Deploy KubeRay operator with the following CLI args:

--enable-metrics=true
--metrics-addr=127.0.0.1:8080
--config /etc/kuberay/config.yaml
Create a ConfigMap with config.yaml containing only:

apiVersion: config.ray.io/v1alpha1
kind: Configuration
defaultContainerEnvs:
- name: MY_ENV
  value: "test"
Observe that:

enableMetrics defaults to false in the struct, overriding --enable-metrics=true
metricsAddr defaults to "" in the struct, overriding --metrics-addr=127.0.0.1:8080
No kuberay_* custom metrics are emitted
Metrics endpoint binds to :8080 (all interfaces) instead of 127.0.0.1:8080

### Anything else

_No response_

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (5)

### abhishekjain1982 · 2026-04-29

Kuberay operator version 1.5.1

### win5923 · 2026-05-02

Hi @abhishekjain1982, I think this issue has resolved in 1.6.0 and 1.5.2. 
https://github.com/ray-project/kuberay/pull/4270

### abhishekjain1982 · 2026-05-02

Issue  #4270 will only helm fix where it make sure same value is passed in configmap when config is enabled.

Expectation is from operator code itself to treat them as some Boolean pointer or string pointer thus if field is missing from config map it will be ignored and cli will be preferred 

### win5923 · 2026-05-02

Hi @abhishekjain1982, 
Because the operator is intentionally designed around a single source of truth: when `--config` is set, the config file is the only source consulted, and CLI flags are ignored. 

https://github.com/ray-project/kuberay/blob/2e4301e4eace2adb93e179fdcc7a477ebf937b33/ray-operator/main.go#L117-L141


We deliberately picked one-or-the-other rather than precedence semantics because we want users to be able to look at one place to understand the full operator configuration, mentally merging multiple sources is complex and error prone.

Could you share more about your deployment?

### github-actions[bot] · 2026-09-23

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
