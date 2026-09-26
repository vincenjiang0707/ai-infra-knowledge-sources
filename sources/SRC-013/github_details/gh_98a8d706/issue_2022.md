# [Issue #2022] Agentic workloads: Tokenspeed model server support

source: https://github.com/llm-d/llm-d/issues/2022
state: open | updated: 2026-09-21T20:44:18Z
labels: 

## 正文

**What?**
Add Kimi k2 for agentic workload on GPUs and aim to publish a well-lit path together with tokenspeed optimizations.

Tokenspeed model server has kernels optimized for [agentic inference](https://lightseek.org/blog/lightseek-tokenspeed.html#fn1). Agentic serving guide can be updated with the support for tokenspeed.

**How?**
The config for llm-d-router [using the pluggable metric extractor](https://github.com/llm-d/llm-d-router/blob/4ef251c713be08cac892ceab450b9da28648f5e0/pkg/epp/framework/plugins/datalayer/extractor/metrics/README.md) can be leveraged for optimized routing.

Tokenspeed exports [vllm style metrics](https://github.com/lightseekorg/tokenspeed/tree/main/python/tokenspeed/runtime/metrics) from the /metrics endpoint.

Sample llm-d-router config for optimized baseline may look like (to be validated):

```
router:
  extraServicePorts:
    - name: http
      port: 80
      protocol: TCP
      targetPort: 8081

  epp:
    pluginsConfigFile: "optimized-baseline-plugins.yaml"
    pluginsCustomConfig:
      optimized-baseline-plugins.yaml: |
        apiVersion: llm-d.ai/v1alpha1
        kind: EndpointPickerConfig
        plugins:
        - type: queue-scorer
        - type: kv-cache-utilization-scorer
        - type: prefix-cache-scorer
        - type: no-hit-lru-scorer
        schedulingProfiles:
        - name: default
          plugins:
          - pluginRef: queue-scorer
            weight: 2
          - pluginRef: kv-cache-utilization-scorer
            weight: 2
          - pluginRef: prefix-cache-scorer
            weight: 3
          - pluginRef: no-hit-lru-scorer
            weight: 2

    # Metric endpoint for tokenspeed:
    metricsDataSource:
      path: /metrics # For example vLLM's path is /metrics
 
  modelServers:
    type: tokenspeed
    matchLabels:
      llm-d.ai/guide: "optimized-baseline"

```



## 评论 (3)

### 0z5a · 2026-09-19

Hi @rahulgurnani , I'd be interested in helping with the TokenSpeed model-server integration.

I'd like to keep the first step focused on the llm-d contract rather than claiming full optimized Kimi K2 support before the serving environment is validated.

### 0z5a · 2026-09-21

C1 status: work on our side is complete and published as llm-d-router#2939 (ready for review).

- The engine type now binds to the core metrics extractor. Before this change a config using it made EPP fail to start with `defaultEngine %q not found in engineConfigs`, which is why the sample configuration in this issue was marked "to be validated".
- Contract details pinned by tests: `kv_cache_usage_perc` is a 0–1 ratio (not a percentage) despite the vLLM-style name; `/metrics` only exists with `--enable-metrics`; a failed scrape keeps the last known metrics instead of zeroing them.

Real-engine E2E remains blocked on hardware: the published TokenSpeed wheels ship only `sm_100a` / `compute_103a` / `sm_103a` binaries with no lower-arch PTX fallback, so this cannot run on the Li40S/L20-class cards we have.


### rahulgurnani · 2026-09-21

thanks for sending out the change @0z5a . we can test/bechmark and a guide here once the changes are in llm-d-router.
