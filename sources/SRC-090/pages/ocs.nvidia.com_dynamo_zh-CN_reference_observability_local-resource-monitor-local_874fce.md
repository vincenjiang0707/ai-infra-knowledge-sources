source: https://docs.nvidia.com/dynamo/zh-CN/reference/observability/local-resource-monitor-local
lastmod: 2026-09-23T23:30:39.914Z

Local Resource Monitor (Local)


Local Resource Monitor (Local)

Host-side per-process VRAM / PCIe / CPU exporter for engine-startup profiling — metrics and CLI flags.

This tool is **local-only**. [ dynamo_local_resource_monitor.py](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/dev/observability/dynamo_local_resource_monitor.py) runs on the host machine (not inside a container) and attributes GPU/CPU/IO usage to individual Dynamo processes by PID. It is not part of a Kubernetes deployment. For the setup walkthrough and design rationale, see the

[Local Resource Monitor guide](https://docs.nvidia.com/dynamo/reference/observability/local-resource-monitor-guide.md).

The monitor samples per-process resource usage (VRAM, GPU utilization, PCIe bandwidth, CPU, disk I/O, network I/O) for Dynamo inference processes, labeled by GPU, PID, and process name. It always exposes Prometheus metrics at `/metrics`

; when the dashboard dependencies are installed, the same endpoint also serves a WebSocket dashboard at `/`

.

Run it on the host:

## Metrics

All metrics use the `dynamo_`

prefix. Unlike the runtime’s `dynamo_component_*`

families, these are host-side gauges labeled by physical GPU and OS process.

### GPU metrics

GPU memory used by a process, in GiB. Labeled by `gpu`

, `pid`

, and `process_name`

.

Total GPU memory, in GiB. Labeled by `gpu`

.

GPU utilization, as a percentage. Labeled by `gpu`

.

GPU temperature, in degrees Celsius. Labeled by `gpu`

.

GPU PCIe transmit throughput, in GB/s. Labeled by `gpu`

.

GPU PCIe receive throughput, in GB/s. Labeled by `gpu`

.

### CPU metrics

Overall CPU utilization, as a percentage.

CPU usage by process-name group, as a percentage. Labeled by `process_name`

.

### Network metrics

Network bytes sent, in MB/s.

Network bytes received, in MB/s.

### Disk metrics

Disk read throughput, in MB/s.

Disk write throughput, in MB/s.

## CLI flags

Port for the `/metrics`

exporter (and the dashboard at `/`

when dependencies are installed).

Host address to bind.

Main collection interval in milliseconds, covering CPU, GPU memory/utilization/temperature, and network (5 samples/s).

Disk I/O collection interval in milliseconds (1 sample/s).

Dashboard rolling window in seconds (default 900 = 15 minutes).

Dashboard process-series limit per chart.

## Related

[Local Resource Monitor guide](https://docs.nvidia.com/dynamo/reference/observability/local-resource-monitor-guide.md)— setup, Prometheus profile gating, and the WebSocket dashboard.[Metrics Catalog](https://docs.nvidia.com/dynamo/reference/observability/metrics-catalog)— the runtime’s`dynamo_*`

metrics.[Environment Variables](https://docs.nvidia.com/dynamo/reference/observability/environment-variables)— runtime observability configuration.