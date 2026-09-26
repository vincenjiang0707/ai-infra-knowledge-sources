# [Issue #222] What's the '[Model Analyzer] WARNING: Requested top 3 configs, but found only 1. Showing all available configs for this model.' mean?

source: https://github.com/triton-inference-server/perf_analyzer/issues/222
state: closed | updated: 2025-02-06T04:32:28Z
labels: 

## 正文

I started tensorflow savedmodel on cpu in a tritonserver container, the configuration is as follows:
```
max_batch_size: 64
backend: "tensorflow"
platform: "tensorflow_savedmodel"
instance_group [
  {
    count: 3
    kind: KIND_CPU
  }
]

dynamic_batching {
  preferred_batch_size: [64]
  max_queue_delay_microseconds: 2000
}
```

Then I started model-analyzer on sidecar container with the following command:
```
model-analyzer profile  --triton-launch-mode=remote --triton-grpc-endpoint=localhost:10502 --override-output-model-repository --run-config-search-mode quick -f perf.yaml
```

perf.yaml
```
model_repository: triton/models_repo

run_config_search_min_instance_count: 2
run_config_search_max_instance_count: 6

run_config_search_max_concurrency: 300

run_config_search_min_model_batch_size: 32
run_config_search_max_model_batch_size: 128

profile_models:
- bc_1118_502000018:
    constraints:
      perf_latency_p99:
        max: 10
```

However, the following warning is reported during the run, and there is no report related to the number of instances. Why? Increasing the number of instances should result in better performance, right?

```
[Model Analyzer] Using remote Triton Server
[Model Analyzer] WARNING: GPU memory metrics reported in the remote mode are not accurate. Model Analyzer uses Triton explicit model control to load/unload models. Some frameworks do not release the GPU memory even when the memory is not being used. Consider using the "local" or "docker" mode if you want to accurately monitor the GPU memory usage for different models.
[Model Analyzer] No checkpoint file found, starting a fresh run.
[Model Analyzer] WARNING: A model not being profiled (ai) is loaded on the remote Tritonserver. This could impact the profile results.
[Model Analyzer] WARNING: A model not being profiled (na) is loaded on the remote Tritonserver. This could impact the profile results.
[Model Analyzer] Profiling server only metrics...
[Model Analyzer] 
[Model Analyzer] Starting quick mode search to find optimal configs
[Model Analyzer] 
[Model Analyzer] Creating model config: bc_1118_502000018_config_default
[Model Analyzer] 
[Model Analyzer] Profiling bc_1118_502000018_config_default: concurrency=128
[Model Analyzer] Saved checkpoint to /root/aiserver/checkpoints/0.ckpt
[Model Analyzer] Creating model config: bc_1118_502000018_config_0
[Model Analyzer]   Setting instance_group to [{'count': 2, 'kind': 'KIND_GPU'}]
[Model Analyzer]   Setting max_batch_size to 32
[Model Analyzer]   Enabling dynamic_batching
[Model Analyzer] 
[Model Analyzer] Skipping illegal run configuration
[Model Analyzer] No changes made to analyzer data, no checkpoint saved.
[Model Analyzer] 
[Model Analyzer] Done with quick mode search. Gathering concurrency sweep measurements for reports
[Model Analyzer] 
[Model Analyzer] WARNING: Requested top 3 configs, but none satisfied constraints. Showing available constraint failing configs for this model.
[Model Analyzer] WARNING: Requested top 3 configs, but found only 1. Showing all available configs for this model.
[Model Analyzer] Profiling bc_1118_502000018_config_default: concurrency=1
[Model Analyzer] Saved checkpoint to /root/aiserver/checkpoints/0.ckpt
[Model Analyzer] Profiling bc_1118_502000018_config_default: concurrency=2
[Model Analyzer] Saved checkpoint to /root/aiserver/checkpoints/0.ckpt
[Model Analyzer] Profiling bc_1118_502000018_config_default: concurrency=4
[Model Analyzer] Saved checkpoint to /root/aiserver/checkpoints/0.ckpt
[Model Analyzer] Profiling bc_1118_502000018_config_default: concurrency=8
[Model Analyzer] Saved checkpoint to /root/aiserver/checkpoints/0.ckpt
[Model Analyzer] Terminating concurrency sweep - throughput is decreasing
[Model Analyzer] 
[Model Analyzer] Done gathering concurrency sweep measurements for reports
[Model Analyzer] 
[Model Analyzer] Saved checkpoint to /root/aiserver/checkpoints/0.ckpt
[Model Analyzer] Profile complete. Profiled 1 configurations for models: ['bc_1118_502000018']
[Model Analyzer] 
[Model Analyzer] WARNING: GPU output field "gpu_used_memory", has no data
[Model Analyzer] WARNING: GPU output field "gpu_utilization", has no data
[Model Analyzer] WARNING: GPU output field "gpu_power_usage", has no data
[Model Analyzer] WARNING: Server output field "gpu_used_memory", has no data
[Model Analyzer] WARNING: Server output field "gpu_utilization", has no data
[Model Analyzer] WARNING: Server output field "gpu_power_usage", has no data
[Model Analyzer] Exporting inference metrics to /root/aiserver/results/metrics-model-inference.csv
[Model Analyzer] WARNING: Requested top 3 configs, but found only 1. Showing all available configs for this model.
[Model Analyzer] WARNING: Requested top 3 configs, but found only 1. Showing all available configs for this model.
[Model Analyzer] WARNING: Requested top 3 configs, but found only 1. Showing all available configs for this model.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_used_memory' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_used_memory' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_used_memory' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_used_memory' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_used_memory' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_used_memory' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_utilization' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] Exporting Summary Report to /root/aiserver/reports/summaries/bc_1118_502000018/result_summary.pdf
[Model Analyzer] WARNING: Requested top 3 configs, but found only 1. Showing all available configs for this model.
[Model Analyzer] Generating detailed reports for the best configurations bc_1118_502000018_config_default:
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_used_memory' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_used_memory' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_used_memory' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_used_memory' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_used_memory' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_utilization' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_utilization' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_utilization' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_utilization' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_utilization' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_power_usage' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_power_usage' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_power_usage' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_power_usage' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_power_usage' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_used_memory' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_utilization' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_used_memory' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_utilization' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_used_memory' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_utilization' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_used_memory' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_utilization' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_used_memory' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] WARNING: No GPU metric corresponding to tag 'gpu_utilization' found in the model's measurement. Possibly comparing measurements across devices.
[Model Analyzer] Exporting Detailed Report to /root/aiserver/reports/detailed/bc_1118_502000018_config_default/detailed_report.pdf
```
![image](https://github.com/user-attachments/assets/56d56c30-59e8-4a8d-8545-181687265d18)


## 评论 (4)

### the-david-oy · 2025-01-09

CC: @nv-braf 

### nv-braf · 2025-01-09

The issue is that the configuration range you have specified is illegal (see line in the log that mentions "skipping illegal run configuration") and therefore MA cannot find configurations to test.

If you run with "-v" you'll get the debug messages which should illuminate what has gone wrong. Looking at your config, my guess is that the issue is that the preferred batch size is larger than the model batch size.

### nv-hwoo · 2025-02-03

@fighterhit Did the response from @nv-braf resolve your issue? 

### the-david-oy · 2025-02-06

Closing due to inactivity. Please feel free to update this issue. We can reopen it if there are follow-up questions or comments.
