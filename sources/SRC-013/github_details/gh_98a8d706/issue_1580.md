# [Issue #1580] [Feature]: Support `LLMD_PRE_START_COMMAND` and `LLMD_EXTRA_VLLM_ARGS` in model server patches

source: https://github.com/llm-d/llm-d/issues/1580
state: open | updated: 2026-09-13T01:22:43Z
labels: enhancement, lifecycle/stale

## 正文

### Feature Area

Deployment / Helm Charts

### Problem Statement

We are working on making diagnosing llm-d networking issues easier. We developed a "preflight checks" approach and implemented it as [llm-d-preflight-checks skill](https://github.com/llm-d/llm-d-pd-utils/blob/main/skills/llm-d-preflight-checks/SKILL.md).

It works but currently requires a two-stage approach - first deploying the model then patching the model server deployment to add preflight-checks script, an environment variable, and a volume containing the script.

It would be great to have a generic mechanism to customize llm-d deployment to modify the entry point and pass parameters, etc.

We think our use case make strong arguments for adding those customizations.

Adding any pre-vLLM startup logic (diagnostics, preflight checks, network validation) currently requires creating a full custom kustomize overlay that:

1. Replaces `command: ["vllm", "serve"]` with `command: ["bash", "-c"]`
2. Reconstructs the entire `vllm serve` arguments as a single shell string (model name, TP size, KV config, etc.)
3. Adds ConfigMap volumes and volume mounts
4. Adds environment variables

This results in **30+ lines of new YAML per deployment** that must duplicate model-specific vLLM arguments from the upstream patch. When upstream changes vLLM args (model name, TP size, flags), these custom overlays silently drift out of sync.

For example, the [P/D disaggregation guide](https://github.com/llm-d/llm-d/tree/main/guides/pd-disaggregation) defines vLLM args in [`patch-prefill.yaml`](https://github.com/llm-d/llm-d/blob/main/guides/pd-disaggregation/modelserver/gpu/vllm/base/patch-prefill.yaml) and [`patch-decode.yaml`](https://github.com/llm-d/llm-d/blob/main/guides/pd-disaggregation/modelserver/gpu/vllm/base/patch-decode.yaml). To add a pre-start command, an operator must create a new overlay that duplicates all of those args inside a `bash -c` string — any upstream change to those patches requires manually updating the overlay.

**Use cases this enables:**
- Run preflight diagnostics before vLLM allocates GPU memory
- Validate networking/RDMA before serving traffic
- Debug pod startup without CrashLoopBackOff (pause mode)
- Append vLLM flags (e.g., `--enable-chunked-prefill`, `--max-model-len`) without reconstructing the entire args array

Related: [llm-d-infra#286](https://github.com/llm-d-incubation/llm-d-infra/issues/286) requests similar Helm-level support (`extraConfigMapVolumes`, `extraEnv`, `preStartCommands`) for the router chart.


### Proposed Solution

The proposed solution is based on investigation with Claude Code - it was just to explore and confirm one possible way to get it working. We are open to any other way of solving the problem described above.

The proposed solution is to add two environment variables recognized by the model server entrypoint that enable pre-start customization **without replacing the command/args structure**:

| Variable | Purpose | Default |
|----------|---------|---------|
| `LLMD_PRE_START_COMMAND` | Shell command(s) executed before `vllm serve` via `&&` chain | unset (no-op) |
| `LLMD_EXTRA_VLLM_ARGS` | Additional vLLM CLI flags appended to the serve command | unset (no-op) |

This follows the same pattern as `MODEL_NAME` — a simple env var that customizes deployment behavior without modifying the underlying YAML structure.

### How it works

Change the guide-level patch files from:

```yaml
# Current: guides/pd-disaggregation/modelserver/gpu/vllm/base/patch-prefill.yaml
containers:
  - name: modelserver
    command: ["vllm", "serve"]
    args:
      - "openai/gpt-oss-120b"
      - "--tensor-parallel-size=1"
      - "--block-size=128"
      - "--kv-transfer-config"
      - '{"kv_connector":"NixlConnector", "kv_role":"kv_both"}'
      - "--no-disable-hybrid-kv-cache-manager"
      - "--gpu-memory-utilization=0.9"
```

To:

```yaml
# Proposed: bash -c wrapper with env var expansion
containers:
  - name: modelserver
    command: ["bash", "-c"]
    args:
      - |
        ${LLMD_PRE_START_COMMAND:+$LLMD_PRE_START_COMMAND &&} \
        exec vllm serve openai/gpt-oss-120b \
          --disable-access-log-for-endpoints=/health,/metrics,/v1/models \
          --tensor-parallel-size=1 \
          --block-size=128 \
          --kv-transfer-config '{"kv_connector":"NixlConnector", "kv_role":"kv_both"}' \
          --no-disable-hybrid-kv-cache-manager \
          --gpu-memory-utilization=0.9 \
          ${LLMD_EXTRA_VLLM_ARGS}
```

Key design points:
- `${VAR:+...}` bash syntax: if unset or empty, expands to nothing (no-op). If set, expands to `<command> &&`
- `exec` replaces bash with vLLM as PID 1 so Kubernetes SIGTERM goes directly to vLLM for graceful shutdown
- The vllm-openai image is Ubuntu 22.04-based and includes `/bin/bash`
- Kubernetes does not evaluate `${...}` in args — only `bash -c` does at runtime

### Files to modify

| Guide | File |
|-------|------|
| P/D disaggregation (prefill) | [`guides/pd-disaggregation/modelserver/gpu/vllm/base/patch-prefill.yaml`](https://github.com/llm-d/llm-d/blob/main/guides/pd-disaggregation/modelserver/gpu/vllm/base/patch-prefill.yaml) |
| P/D disaggregation (decode) | [`guides/pd-disaggregation/modelserver/gpu/vllm/base/patch-decode.yaml`](https://github.com/llm-d/llm-d/blob/main/guides/pd-disaggregation/modelserver/gpu/vllm/base/patch-decode.yaml) |
| Optimized baseline (quickstart) | [`guides/optimized-baseline/modelserver/gpu/vllm/base/patch-vllm.yaml`](https://github.com/llm-d/llm-d/blob/main/guides/optimized-baseline/modelserver/gpu/vllm/base/patch-vllm.yaml) |

The base deployment templates ([`prefill-deployment.yaml`](https://github.com/llm-d/llm-d/blob/main/guides/recipes/modelserver/base/single-host/pd/base/prefill-deployment.yaml)) have `command: []` and `args: []` — they are already designed to be overridden by guide-level patches, so no changes are needed at the base recipe level.

### ConfigMap volume for scripts

Add an optional ConfigMap volume to the base deployment template so pre-start scripts are available when needed:

```yaml
volumes:
  - name: preflight-scripts
    configMap:
      name: llm-d-preflight-checks
      defaultMode: 0755
      optional: true
volumeMounts:
  - name: preflight-scripts
    mountPath: /preflight
```

When the ConfigMap doesn't exist, the volume is simply empty — no error, no impact on existing deployments. Operators create it only when needed:

```bash
kubectl create configmap llm-d-preflight-checks \
  --from-file=llm-d-preflight-checks.py=path/to/script.py -n ${NAMESPACE}
```

### Usage examples

**Enable preflight checks (2 env vars instead of 30+ line overlay):**

```bash
kubectl set env deployment/pd-disaggregation-nvidia-gpu-vllm-prefill \
  LLMD_PRE_START_COMMAND="python3 /preflight/llm-d-preflight-checks.py" \
  LLMD_PREFLIGHT_CHECKS=pause

kubectl set env deployment/pd-disaggregation-nvidia-gpu-vllm-decode \
  LLMD_PRE_START_COMMAND="python3 /preflight/llm-d-preflight-checks.py" \
  LLMD_PREFLIGHT_CHECKS=pause \
  VLLM_INFERENCE_PORT=8200
```

**Add extra vLLM flags without rebuilding args:**

```bash
kubectl set env deployment/pd-disaggregation-nvidia-gpu-vllm-prefill \
  LLMD_EXTRA_VLLM_ARGS="--enable-chunked-prefill --max-model-len=4096"
```

**Minimal kustomize patch:**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: placeholder
spec:
  template:
    spec:
      containers:
        - name: modelserver
          env:
            - name: LLMD_PRE_START_COMMAND
              value: "python3 /preflight/llm-d-preflight-checks.py"
            - name: LLMD_PREFLIGHT_CHECKS
              value: "pause"
```

### Benefits

| Before (current) | After (proposed) |
|-------------------|------------------|
| 30+ line custom kustomize overlay per guide | 2 env vars (`kubectl set env` or 5-line patch) |
| Must duplicate all vLLM args in shell string | vLLM args stay in upstream patch, no duplication |
| Custom overlay drifts when upstream changes | No drift — env vars are additive |
| Different overlay needed per guide | Same env vars work across all guides |
| Hard to audit with `helm diff` / `kubectl diff` | Changes visible as env var diffs |


### Alternatives Considered


| Approach | Why not |
|----------|---------|
| Full custom kustomize overlay (current workaround) | 30+ lines per deployment, duplicates vLLM args, silently drifts with upstream changes |
| Post-deploy JSON patch (`kubectl patch`) | Fragile, races with rollout, must reconstruct exact args array |
| Init containers | Cannot gate vLLM start with `&&` (init runs in separate container), different health probe lifecycle |
| Sidecar with shared PID namespace | Over-engineered for a startup gate, adds operational complexity |
| General `extraVolumes` / `extraVolumeMounts` env var | More flexible but significantly more complex to implement in kustomize (would require a controller or init script to parse JSON env vars into volume specs) |

### Willingness to Contribute

Yes, I can submit a PR

### Additional Context


### Acceptance criteria

- [ ] Guide-level patch files use `bash -c` wrapper with `LLMD_PRE_START_COMMAND` expansion
- [ ] `LLMD_EXTRA_VLLM_ARGS` is appended to vllm serve command when set
- [ ] Deployments work identically when both vars are unset (no behavioral change)
- [ ] Optional ConfigMap volume (`llm-d-preflight-checks`) added to base deployment template
- [ ] P/D disaggregation guide works unchanged with no env vars set
- [ ] Optimized-baseline (quickstart) guide works unchanged with no env vars set
- [ ] Documentation updated showing how to enable pre-start commands

### Feasibility notes

- The `vllm/vllm-openai` image is built on `nvidia/cuda:*-base-ubuntu22.04` — bash is available at `/bin/bash`
- Kubernetes does NOT evaluate `${VAR:+...}` in container args — only `bash -c` interprets it at runtime
- `exec vllm serve` replaces the bash shell as PID 1, ensuring proper signal forwarding for graceful shutdown
- YAML block scalar (`|`) for multiline args works correctly with kustomize strategic merge patches

### Related issues

- [llm-d-infra#286](https://github.com/llm-d-incubation/llm-d-infra/issues/286) — Helm values for mounting ConfigMap scripts and customizing vLLM entrypoint (router chart)
- [llm-d#850](https://github.com/llm-d/llm-d/issues/850) — Modular installation architecture tracking issue (this proposal aligns with making kustomize overlays more composable)
- [llm-d#992](https://github.com/llm-d/llm-d/issues/992) — Local override workflow for guide-based validation (established the env var override pattern for local testing)
- [llm-d#1430](https://github.com/llm-d/llm-d/issues/1430) — CrashLoopBackOff on OpenShift due to unwritable dirs (fixed by adding volumes to patches — this proposal would make such fixes simpler)
- [llm-d#935](https://github.com/llm-d/llm-d/issues/935) — Modular guides folder restructuring (aligns with making customization more accessible)


## 评论 (2)

### Bhimesh1 · 2026-06-14

Hi @aslom, I’m a new contributor and I’d like to help with this issue if it’s still available.

I’m interested in the deployment/YAML side of this. My plan would be to first investigate the three model server patch files listed in the issue and check how the current `command` / `args` are structured:

* `guides/pd-disaggregation/modelserver/gpu/vllm/base/patch-prefill.yaml`
* `guides/pd-disaggregation/modelserver/gpu/vllm/base/patch-decode.yaml`
* `guides/optimized-baseline/modelserver/gpu/vllm/base/patch-vllm.yaml`

Then I can try a small focused PR that wraps the vLLM startup with `bash -c`, supports `LLMD_PRE_START_COMMAND`, appends `LLMD_EXTRA_VLLM_ARGS`, and verifies the rendered manifests still behave the same when both env vars are unset.

Please let me know if it’s okay for me to work on this or collaborate on part of it.

### github-actions[bot] · 2026-09-13

This issue is marked as stale after 90d of inactivity. After an additional 30d of inactivity (15d to become rotten, then 15d more), it will be closed. To prevent this issue from being closed, add a comment or remove the `lifecycle/stale` label.
