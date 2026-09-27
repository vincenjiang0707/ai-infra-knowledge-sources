# [Issue #170] [Question] Amount of lag expected for metrics

source: https://github.com/NVIDIA/DCGM/issues/170
state: open | updated: 2025-01-10T16:02:44Z
labels: 

## 正文

I'm drawing a timeline of DCGM metrics (gathered with `DcgmReader` and update interval 10 ms) together with Python application-level metrics like the number of running requests at each moment. DCGM metrics have their own microsecond timestamp, and I gathered the timestamp of appilcation-level metrics with `time.time_ns() // 1000`.

I see that in the beginning of the application, the SM activity metric (which I'm taking as "at least one kernel is running on the GPU") becomes non-zero something like 300 ms after dispatching the first batch of computations to the GPU. That delay is way too long for any kernel launch overhead or the Python interpreter overhead. I don't think it would be cache misses either since the DRAM activity metric goes up at the same moment SM activity goes up.

1. In general, how long of a lag should I expect for DCGM metrics?
2. Can different metrics have different amounts of lag, if any? Largely, can the lag be different for the `DCGM_FI_DEV_*` group and the `DCGM_FI_PROF_*` group?

## 评论 (3)

### george-kuanli-peng · 2024-06-12

I also observe a lag ~ 40 seconds of the metrics reported by DCGM-Exporter. I do not observe such a long lagging of the metrics reported by cAdvisor on the same platform ,though.

### george-kuanli-peng · 2024-07-03

I found the lag could be reduced by setting its time of metric collection interval (`$DCGM_EXPORTER_INTERVAL`, or `-c`). The default is `30000` ms.

https://docs.nvidia.com/datacenter/cloud-native/gpu-telemetry/latest/dcgm-exporter.html

### dtamienER · 2025-01-10

I can confirm that modifying the metric collection interval is indeed an effective way to reduce lag when using the NVIDIA DCGM Exporter. In my setup, I adjusted the interval using Helm by setting the following values in the deployment configuration:

```
dcgmExporter:
  env:
    - name: DCGM_EXPORTER_INTERVAL
      value: "1000"  # In ms
```

For reference, the default value is 30,000 ms as @george-kuanli-peng said (confirmed by `/usr/bin/dcgm-exporter --help`).

If you're deploying without Helm, you can achieve the same effect by setting the DCGM_EXPORTER_INTERVAL environment variable in your container runtime configuration.
