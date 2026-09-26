# [Issue #2511] [CI] Nightly E2E GKE Tests started failing with guide error

source: https://github.com/llm-d/llm-d/issues/2511
state: closed | updated: 2026-09-17T18:38:15Z
labels: 

## 正文

# GKE Nightly E2E Test Regressions (`guide-error`)

## Overview

Seven GKE nightly E2E test workflows on the [release status matrix](https://github.com/llm-d/llm-d/tree/main/release) were failing with `"message": "guide-error"`. Investigation traced these failures to **3 primary root causes** across `llm-d-benchmark` and `llm-d-infra`, introduced by specific recent PRs.

| Affected GKE Nightly Workflow | Root Cause | Introducing PR(s) |
| :--- | :--- | :--- |
| 1. `nightly-e2e-tiered-prefix-cache-gke-cpu-gpu-vllm-native.yaml`<br>2. `nightly-e2e-tiered-prefix-cache-gke-cpu-gpu-vllm-lmcache.yaml` | **Issue 1**: Duplicated `${CONNECTOR}` path segment in `GuideVariableResolver` | [llm-d-benchmark#1892](https://github.com/llm-d/llm-d-benchmark/pull/1892) (`600c9f7`, Sep 9)<br>[llm-d-benchmark#1904](https://github.com/llm-d/llm-d-benchmark/pull/1904) (`a855991`, Sep 11) |
| 3. `nightly-e2e-pd-disaggregation-gke-acc-gpu-sglang-x.yaml`<br>4. `nightly-e2e-pd-disaggregation-gke-acc-gpu-vllm-x.yaml`<br>5. `nightly-e2e-wide-ep-lws-gke-acc-gpu-vllm-x.yaml` | **Issue 2**: Unconditional `cluster_resource_resolver` fails when GKE GPU node pools scale to zero | [llm-d-benchmark#1514](https://github.com/llm-d/llm-d-benchmark/pull/1514) (`d3281c8`, Jul 30)<br>[llm-d-benchmark#1907](https://github.com/llm-d/llm-d-benchmark/pull/1907) (`284ffc8`, Sep 11) |
| 6. `nightly-e2e-multimodal-serving-aggregation-gke-acc-gpu-vllm-x.yaml`<br>7. `nightly-e2e-multimodal-serving-e-disaggregation-gke-acc-gpu-vllm-x.yaml` | **Issue 3**: Nested guide path (`multimodal-serving/*`) breaks scenario lookup, `GUIDE_NAME`, and `INFRA_PROVIDER` | [llm-d#2286](https://github.com/llm-d/llm-d/pull/2286) (`7c08d4c2`, Aug 18)<br>`llm-d-infra` commit `b81e88d` |

---

## Detailed Breakdown of GKE Issues & Regressions

### Issue 1: Duplicated `${CONNECTOR}` Segment in Kustomize Path
**Affected GKE Workflows:**
- `nightly-e2e-tiered-prefix-cache-gke-cpu-gpu-vllm-native.yaml`
- `nightly-e2e-tiered-prefix-cache-gke-cpu-gpu-vllm-lmcache.yaml`
*(Also impacts `nightly-e2e-tiered-prefix-cache-gke-cpu-tpu-vllm-native.yaml`)*

#### Failure Log
```text
Error: accumulating resources: accumulation err='accumulating resources from 'cpu/gke': evalsymlink failure on '.../guides/tiered-prefix-cache/modelserver/gpu/vllm/lmcache-connector/lmcache-connector/cpu/gke' : lstat .../guides/tiered-prefix-cache/modelserver/gpu/vllm/lmcache-connector/lmcache-connector: no such file or directory'
```

#### How the Regression Was Introduced
1. **[llm-d-benchmark#1892](https://github.com/llm-d/llm-d-benchmark/pull/1892)** (`600c9f7`, merged Sep 9, 2026: *"Splice the connector into the guide path"*) added `GuideVariableResolver.effective_backend()` in `llmdbenchmark/kustomize/variable_resolver.py` to fold `connector` into `acceleratorBackend` (`gpu/vllm` $\rightarrow$ `gpu/vllm/{connector}`). Initially, this only read `kustomize.connector`, which CI did not set.
2. **[llm-d-benchmark#1904](https://github.com/llm-d/llm-d-benchmark/pull/1904)** (`a855991`, merged Sep 11, 2026: *"fix(kustomize): read connector from guideVariableOverrides.CONNECTOR"*) updated `effective_backend()` to read `kustomize.guideVariableOverrides.CONNECTOR` (which the nightly CI workflow sets).
3. In `guides/tiered-prefix-cache/README.md`, the kustomize command template already explicitly includes `${CONNECTOR}`:
   ```bash
   kubectl apply -k "modelserver/gpu/vllm/${CONNECTOR}/${VARIANT}/${INFRA_PROVIDER}"
   ```
   When `GuideVariableResolver.resolve()` executes:
   - Step 1 (`_substitute_variables`) replaces `${CONNECTOR}` $\rightarrow$ `modelserver/gpu/vllm/lmcache-connector/cpu/gke`.
   - Step 2 (`_apply_accelerator_backend`) replaces `modelserver/gpu/vllm` with `modelserver/{effective_backend}` (`modelserver/gpu/vllm/lmcache-connector`), duplicating the connector segment into `modelserver/gpu/vllm/lmcache-connector/lmcache-connector/cpu/gke`.

#### Fix
Updated `GuideVariableResolver._apply_accelerator_backend` (`llmdbenchmark/kustomize/variable_resolver.py`) to check if `modelserver/gpu/vllm/{connector}` is already present in the string before replacing, preventing duplication while also enforcing path-boundary regex matching (`(?=/|\s|$|"|')`).

---

### Issue 2: `cluster_resource_resolver` Fails When GKE GPU Node Pools Scale to Zero
**Affected GKE Workflows (on cluster `llm-d-e2e-us-south1-2`):**
- `nightly-e2e-pd-disaggregation-gke-acc-gpu-sglang-x.yaml`
- `nightly-e2e-pd-disaggregation-gke-acc-gpu-vllm-x.yaml`
- `nightly-e2e-wide-ep-lws-gke-acc-gpu-vllm-x.yaml`

#### Failure Log
```text
RuntimeError: Could not auto-detect the following cluster resources: accelerator.resource, accelerator.profile, decode.acceleratorType.labelValue, prefill.acceleratorType.labelValue.
```

#### How the Regression Was Introduced
1. **[llm-d-benchmark#1514](https://github.com/llm-d/llm-d-benchmark/pull/1514)** (`d3281c8`, merged Jul 30, 2026: *"Enable Intel XPU via accelerator auto-detect"*) added `self.cluster_resource_resolver.resolve_all(merged_values)` in `RenderPlans._render()` (`llmdbenchmark/parser/render_plans.py`) whenever `not is_nok8s`.
2. **[llm-d-benchmark#1907](https://github.com/llm-d/llm-d-benchmark/pull/1907)** (`284ffc8`, merged Sep 11, 2026: *"feat: separate standup and run phases"*) refactored CLI execution so `RenderPlans._render()` runs unconditionally upfront during both `teardown` ("Cleanup target cloud") and `standup` for all deployment methods, including `kustomize`.
3. On GKE cluster `llm-d-e2e-us-south1-2`, GPU node pools autoscale down to `0` nodes when idle between runs. When `teardown` or `standup` starts, `kubectl get nodes` shows no GPU nodes. `cluster_resource_resolver.resolve_all()` immediately raises `RuntimeError` trying to auto-detect Helm values (`accelerator.*`, `decode/prefill.acceleratorType.*`) that `kustomize` mode completely ignores—aborting before `kustomize` can apply the workload manifests that trigger the GKE cluster autoscaler to provision GPU nodes.

#### Fix
Updated `RenderPlans._render()` (`llmdbenchmark/parser/render_plans.py`) and `step_03_workload_monitoring.py` to skip `cluster_resource_resolver.resolve_all()` and Helm resource validation when running in `kustomize` mode.

---

### Issue 3: Nested Guide Path (`multimodal-serving/*`) Breaks Scenario Lookup, `GUIDE_NAME`, and `INFRA_PROVIDER`
**Affected GKE Workflows:**
- `nightly-e2e-multimodal-serving-aggregation-gke-acc-gpu-vllm-x.yaml`
- `nightly-e2e-multimodal-serving-e-disaggregation-gke-acc-gpu-vllm-x.yaml`
*(Also impacts `nightly-e2e-multimodal-serving-aggregation-gke-acc-tpu-vllm-x.yaml`)*

#### Failure Log
```text
stat /workspace/llm-d-benchmark/config/scenarios/guides/multimodal-serving/aggregation.yaml: no such file or directory
```

#### How the Regression Was Introduced
1. **[llm-d#2286](https://github.com/llm-d/llm-d/pull/2286)** (`7c08d4c2`, merged Aug 18, 2026: *"Add multimodal-serving nightlies"*) added the GKE multimodal workflows with nested guide paths: `standup_scenario: multimodal-serving/aggregation` and `standup_scenario: multimodal-serving/e-disaggregation`.
2. In `llm-d-infra` (`reusable-ci-nightly-benchmark.yaml`, commit `b81e88d`), the workflow constructs:
   - `LLMDBENCH_CICD_SCENARIO_FILE="$LLMDBENCH_CICD_BENCHMARK_PATH/config/scenarios/guides/$LLMDBENCH_CICD_SCENARIO.yaml"`, which looks for a nested subdirectory `config/scenarios/guides/multimodal-serving/aggregation.yaml`. However, `llm-d-benchmark` stores scenario files flat with hyphens (`config/scenarios/guides/multimodal-serving-aggregation.yaml`), and `multimodal-serving-e-disaggregation.yaml` (plus the Jinja specification templates in `config/specification/guides/`) were never created.
   - `kustomize.guideVariableOverrides.GUIDE_NAME="multimodal-serving/aggregation"`. Inside `guides/multimodal-serving/aggregation/README.md`, `${GUIDE_NAME}` is used both in paths (`guides/multimodal-serving/${GUIDE_NAME}/...`, which duplicated `multimodal-serving/`) and as the Helm release name (`helm install ${GUIDE_NAME}`, where `/` is illegal).
   - For `e-disaggregation`, the workflow passes `infra_provider: e-pd/gke` so CI kustomize discovery finds `modelserver/gpu/vllm/e-pd/gke`, but `README.md` defines `MODEL_SERVER_PATH` as `modelserver/gpu/vllm/${TOPOLOGY}/${INFRA_PROVIDER}`. Passing `INFRA_PROVIDER=e-pd/gke` without splitting `TOPOLOGY` produced `modelserver/gpu/vllm/e-p-d/e-pd/gke`.

#### Fix
- **In `llm-d-infra` (`reusable-ci-nightly-benchmark.yaml`)**: Added fallback replacing `/` with `-` when resolving `LLMDBENCH_CICD_SCENARIO_FILE`, and set `guideVariableOverrides.GUIDE_NAME` to the leaf guide name (`${LLMDBENCH_CICD_EFFECTIVE_GUIDE_NAME##*/}`).
- **In `llm-d-benchmark`**: Added missing specification (`multimodal-serving-aggregation.yaml.j2`, `multimodal-serving-e-disaggregation.yaml.j2`) and scenario (`multimodal-serving-e-disaggregation.yaml`) files, updated `resolve_specification_file` to map nested slashes to hyphens, and updated `GuideVariableResolver` to strip path prefixes from `GUIDE_NAME` and split `INFRA_PROVIDER` (`e-pd/gke` $\rightarrow$ `TOPOLOGY=e-pd`, `INFRA_PROVIDER=gke`).


## 评论 (5)

### jtechapps · 2026-09-16

/assign @jtechapps 

### maugustosilva · 2026-09-17

This problem was fixed in PR https://github.com/llm-d/llm-d-benchmark/pull/1934

### jtechapps · 2026-09-17

@maugustosilva I don't think this issue can be closed yet because the other causes have not been addressed.

### rlakhtakia · 2026-09-17

@maugustosilva I am testing changes for issue 3. Fix will introduce a PR in llm-d-benchmark and llm-d-infra.

### LukeAVanDrie · 2026-09-17

Wide EP GKE and Wide EP CKS have been failing at model detection since June because their overlays now render a DisaggregatedSet and the workflow only knows how to read Deployments and LeaderWorkerSets. I'm opening an llm-d-infra PR that adds the missing probe. Wide EP GKE will then still fail in its Teardown step until benchmark https://github.com/llm-d/llm-d-benchmark/pull/1927 lands: the benchmark's cluster resource auto-detect raises when the GPU pool is scaled to zero, and https://github.com/llm-d/llm-d-benchmark/pull/1927 skips it in kustomize mode.

