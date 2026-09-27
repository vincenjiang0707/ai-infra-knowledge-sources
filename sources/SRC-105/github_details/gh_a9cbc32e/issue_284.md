# [Issue #284] Update Grafana GUI for v2.0 metrics

source: https://github.com/ROCm/rocprofiler-compute/issues/284
state: closed | updated: 2025-08-06T18:33:10Z
labels: enhancement, Grafana GUI, Customer Req

## 正文

**Is your feature request related to a problem? Please describe.**
Customer request to enable Grafana (or more its specifically DB backend) for the metric updates being introduced in v2.0. Currently, the Grafana based metric definitions have fallen behind the yaml based definitions used in CLI/standalone GUI, i.e.
https://github.com/AMDResearch/omniperf/tree/2.x/src/omniperf_soc/analysis_configs

If customer tries to use Grafana with new v2.0 output, the reported metrics will be incorrect.

**Describe the solution you'd like**
Customer is asking we enable Grafana which would mean updating the MongoQL metric definitions for _all_ metrics. This could potentially be time consuming and MongoQL limits the devs we could have working on this

**Describe alternatives you've considered**
In the past, I've wanted to build the DB backend into the CLI/standalone GUI backend which would essentially eliminate the need to keep maintaining (separate) MongoQL based definitions. A separate discussion needs to be had about if this would be a more timely solution, but it's something to consider.

## 评论 (3)

### feizheng10 · 2024-02-29

This should go down the road of adding DB support in standalone gui.

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/66

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
