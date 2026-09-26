# how-to-choose-full-stack-observability-for-nvidia-ai-factories

source: https://developer.nvidia.com/blog/how-to-choose-full-stack-observability-for-nvidia-ai-factories/

AI infrastructure spans multiple layers, from compute and networking to storage, orchestration, and applications. When performance degrades, identifying the source can be difficult because a symptom observed at one layer may originate elsewhere in the stack.

A full-stack observability strategy connects telemetry across these layers, helping infrastructure and operations teams detect problems, isolate their causes, and maintain reliable AI workloads. This post presents a practical observability framework for NVIDIA AI infrastructure and shows how to apply it to common monitoring and troubleshooting scenarios.

Consider a distributed training job that is three days into execution. GPU utilization and queue wait times remain normal. After six hours of reduced throughput, the team traces the cause to a single InfiniBand link drifting into an elevated bit error rate.

This is a classic [gray failure](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/06/paper-1.pdf). The hardware is degraded, but the system does not report it as “down.” AI training follows the bulk synchronous parallel (BSP) model. These tightly coupled systems are sensitive to stragglers: one slow rank holds back the job. Link-level retransmissions stall a single rank during [synchronous collective operations](https://developer.nvidia.com/blog/advancing-performance-with-nvidia-sharp-in-network-computing) such as NVIDIA Collective Communications Library (NCCL) all-reduce. Throughput then falls to the slowest rank, and the other ranks block. That is a cascading failure.

You see this failure mode often in AI factories. The required telemetry typically already exists; the challenge is selecting the right signals from the right tools early enough to act. Operators do not need every metric from every product. They need a decision path that maps components to tools, tools to a concise alert set, and that alert set into a single triage dashboard.

This post shows that path. You will learn how to:

- Enumerate the failure domains that must be observable before selecting software.
- Map AI infrastructure components to telemetry tools sources using a decision framework derived from NVIDIA DGX deployments.
- Apply the observability framework to an InfiniBand cluster.
- Reduce telemetry to a top-k alert set and correlate signals in a single triage dashboard.

Keep detailed catalogs, protocol matrices, and per-tool enablement guides in product documentation. Here, you’ll focus on how to choose an observability stack. NVIDIA DGX and NVIDIA HGX deployments share the same observability surface, even when hardware configurations differ (Figure 1):

## Identify AI factory failure domains

Before selecting monitoring software, enumerate the domains in which silent failure consumes GPU hours:

**Platform health**: Fans, PSUs, BMC, chassis, CPU, memory, local storage.**GPU health and performance**: Utilization, temperature, power, XID/ECC, and NVIDIA NVLink throughput.**Fabric**: InfiniBand or Ethernet link integrity, congestion, and switch/cable health; rack-scale NVLink where present.**Cluster and jobs**: Scheduling, reservations, idle allocated GPUs, queue wait.**Inference services**: Latency, success rate, and cache behavior when NVIDIA NIM microservices or similar services are in production.

In complex systems, coverage gaps are rarely closed in one pass. They appear later, when [latent failure modes](https://how.complexsystems.fail/) show up [under load](https://how.complexsystems.fail/). Analyzing those modes early shortens discovery. This analysis can help prevent failures from recurring under load.

## Map AI infrastructure components to telemetry tools

Operations teams need a clear mapping from component to telemetry source. Table 1 maps NVIDIA Data Center GPU Manager (DCGM), NVIDIA System Management (NVSM), NVIDIA Unified Fabric Manager (UFM), NVIDIA NetQ, NVIDIA NMX, NVIDIA Base Command Manager (BCM), and NVIDIA Run:ai to those components. Green indicates full support for the domain; yellow indicates partial or indirect coverage. Use the framework to select the minimum tool set that eliminates coverage gaps.

| Component | Redfish / IPMI | DCGM | NVSM | UFM | NetQ | NMX | BCM | Run:ai | NIM |
|---|---|---|---|---|---|---|---|---|---|
Base infrastructure | 🟢 | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | 🟢 | ⚪ | ⚪ |
Compute node | 🟢 | 🟡 | 🟢 | ⚪ | ⚪ | 🟡 | 🟢 | ⚪ | ⚪ |
GPU | ⚪ | 🟢 | 🟢 | ⚪ | ⚪ | ⚪ | 🟢 | 🟡 | ⚪ |
Node interconnects | ⚪ | 🟢 | 🟡 | ⚪ | ⚪ | ⚪ | 🟢 | ⚪ | ⚪ |
Rack-scale NVLink | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | 🟢 | ⚪ | ⚪ | ⚪ |
Ethernet network | ⚪ | ⚪ | ⚪ | ⚪ | 🟢 | ⚪ | 🟢 | ⚪ | ⚪ |
InfiniBand network | ⚪ | 🟡 | ⚪ | 🟢 | ⚪ | ⚪ | 🟢 | ⚪ | ⚪ |
Cluster management | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | 🟢 | ⚪ | ⚪ |
Jobs and workloads | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | 🟢 | 🟢 | ⚪ |
AI inference | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | 🟡 | 🟢 |

*Legend:*🟢 = Full support · 🟡 = Partial/indirect support

*Table 1. Observability decision framework*

Key tradeoffs include:

**DCGM compared to NVSM for GPUs**: Prefer DCGM for utilization, power, temperature, NVLink, and XID/ECC export into Prometheus. Retain NVSM for system health on DGX-class nodes (drives, power, overall health). The tools overlap on GPU metrics; neither substitutes for platform BMC data.**UFM compared to NetQ**: Select by fabric type. InfiniBand uses UFM. Spectrum Ethernet/RoCE uses NetQ. Deploy both only when both fabrics are present.**NMX**: Required for rack-scale NVLink. Omit on classic multi-node NVLink topologies where DCGM already covers node interconnects.**BCM**: Treat BCM as the aggregator and cluster/job plane, not as the source of low-level counters. Specialized tools remain responsible for deep telemetry.**Run:ai and NIM**: Introduce when workload scheduling fairness or inference SLOs are first-class operational requirements. Neither replaces DCGM or fabric monitoring.

A useful rule: cover every required green cell with the fewest tools. Extra exporters without a clear triage path add noise, not observability. That noise leads to alert fatigue.

Teams keep adding metrics and dashboards, yet still cannot answer what is broken and why. The result is “watermelon metrics”: dashboards that look green outside while services fail inside. The corrective principle is the one stated in “[As Simple as Possible, No Simpler](https://sre.google/sre-book/monitoring-distributed-systems/#as-simple-as-possible-no-simpler)”: keep monitoring simple, and remove unused signals rather than accumulate them.

## Apply the observability framework to an InfiniBand cluster

Consider a DGX cluster with InfiniBand, BCM, and Slurm. Most jobs are training; inference is not yet in production. The operational requirement is a single triage dashboard and alerts that detect fabric and GPU health regressions before multi-hour job waste accumulates.

Here’s the decision process:

**Domains in scope**: platform, GPU, InfiniBand fabric, cluster/jobs. Out of scope for the initial deployment: NetQ, NMX, Run:ai, NIM.**Tool selection from the framework**

- Redfish/IPMI on every node for fans, PSU, chassis, and BMC state.
- DCGM on every GPU node for utilization, power, temperature, XID/ECC, and NVLink.
- NVSM on DGX nodes for system health aggregation.
- UFM for InfiniBand port health, BER, congestion, and routing.
- BCM as the cluster aggregator for jobs, reservations, and consolidated hardware alerts.

**Rationale**: DCGM alone would miss the BER regression described in the introduction. This is a[tail-at-scale problem](https://research.google/pubs/pub40801/). When work is synchronized across many ranks, end-to-end throughput follows the slowest rank, not average component health. UFM alone would miss GPU XID storms and node power faults. BCM alone would not generate the low-level counters. Combined, they cover the domains that waste GPU hours in this environment.**Exclusions**: Skip NetQ, NMX, and inference metrics until Ethernet, rack-scale NVLink, or inference services are introduced.

That gives you an initial stack of IPMI, DCGM, NVSM, UFM, and BCM, unified in Prometheus/Grafana.

## Build an actionable AI infrastructure alert set

Most tools expose hundreds of metrics. Prefer a short top-k set tied to **service-level indicators (SLIs)** and **service-level objectives (SLOs)**, not a dump of every hardware counter. Each alert should map to a clear remediation action. UFM Telemetry exposes hundreds of fields; start with the documented [high-frequency telemetry fields](https://docs.nvidia.com/networking/display/ufmenterpriseumv6242/high-frequency-(primary)-telemetry-fields).

For the apply the observability framework to an InfiniBand cluster, begin with:

**Platform**: fan speed, PSU status, key temperatures (`SPD_FAN_*`

,`PWR_*`

,`TEMP_*`

via Redfish/IPMI).**GPU**:`DCGM_FI_DEV_GPU_UTIL`

,`DCGM_FI_DEV_MEM_COPY_UTIL`

,`DCGM_FI_DEV_POWER_USAGE`

,`DCGM_FI_DEV_XID_ERRORS`

, plus NVSM GPU/system health.**InfiniBand**:`PortXmitDataExtended`

,`SymbolErrorCounterExtended`

,`Effective_BER`

,`Total_Raw_BER`

,`Chip_Temp`

.**Jobs**: BCM/Slurm signals for running jobs, GPU reservations, and wait time so fabric or GPU alerts correlate to workload impact.

Expand the set only when an incident demonstrates a coverage gap. Consistent with [Symptoms Versus Causes](https://sre.google/sre-book/monitoring-distributed-systems/#symptoms-versus-causes), alert on symptoms that map to a defined action (drain node, replace cable, open fabric case), not on every counter a collector can emit.

Prefer Prometheus exporters where available: DCGM and NVSM both expose Prometheus endpoints; UFM and BCM can feed the same scrape model via exporters or APIs. This keeps protocol selection simple for the initial deployment and avoids introducing a second control plane before gNMI or SNMP integration is required.

## Build a unified AI infrastructure triage dashboard

With tools and top-k metrics selected, build a unified AI infrastructure triage dashboard (Figure 2):

A practical architecture looks like this:

- Install IPMI and DCGM exporters on every GPU node.
- Run UFM Telemetry where the fabric is reachable; scrape or export into Prometheus.
- Retain BCM as the cluster management and aggregation plane.
- Point Grafana at Prometheus for dashboards and alerts across GPU, node, and fabric signals.
- Add a community
[Slurm dashboard](https://grafana.com/grafana/dashboards/4323-slurm-dashboard/)if job-level context is not already available in BCM.

Use a two-layer monitoring approach. Layer 1 gives a high-level view for triage; Layer 2 keeps the detail needed to inspect individual components. Layer 1 is the Grafana dashboard used first: is the fault in the GPU, node, or fabric? Layer 2 is the vendor UI deep dive (UFM web UI, BCM Base View, and similar tools) once the failing domain is known. Day 2 operations is faster when Layer 1 answers the triage question from one board. Layer 2 stays available for root-cause analysis.

## Define observability acceptance criteria

You’re ready to move on when:

- Every failure domain in scope has at least one full-support tool from the framework.
- Alerts are bound to a short top-k metric list with owners and actions.
- GPU, node, and fabric signals share a common timeline in one view.
- Further tools (Ethernet, rack-scale NVLink, Run:ai, NIM) are added only when needed, not by default.

Don’t measure observability maturity by the number of dashboards. Measure it by whether your signals show the failing component and the next action before significant compute capacity is wasted.

## Expand the NVIDIA AI infrastructure observability stack

After your initial deployment meets the define observability acceptance criteria , expand coverage in this order:

- Enable GPU telemetry with the
[DCGM User Guide](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/)and[GPU Telemetry](https://docs.nvidia.com/datacenter/cloud-native/gpu-telemetry/latest/). - Validate DGX system health paths in the
[NVSM User Guide](https://docs.nvidia.com/datacenter/nvsm/nvsm-user-guide/latest/introduction.html#health-monitor-alerts). - Configure fabric visibility with
[UFM Telemetry](https://docs.nvidia.com/networking/display/ufmtelemetryumv1212)or[NetQ](https://docs.nvidia.com/networking-ethernet-software/cumulus-netq/), depending on the network fabric. - For cluster aggregation and operations, begin with
[Base Command Manager](https://docs.nvidia.com/base-command-manager/)and, where applicable,[NVIDIA Mission Control](https://docs.nvidia.com/mission-control/docs/systems-quick-start-guide/2.3.0/index.html). - For inference services, add NVIDIA NIM Operator observability.

Use the decision framework to justify each addition. Keep detailed metric dictionaries and protocol matrices in runbooks or product docs. Keep the production alert set short enough for on-call use.

A decision framework beats a metric catalog. It’s what gets you to a few well-chosen signals and one triage board instead of fifty dashboards nobody reads.

3-step rollout checklist:

**Establish coverage:**Pick one full-support tool for each in-scope domain (see Table 1).**Integrate exporters:**Wire Redfish/IPMI, DCGM, NVSM, UFM, and BCM into Prometheus, and point Grafana at the unified telemetry endpoint.**Enforce ownership:**Bind every alert to an owner and a playbook action before adding the next exporter.

Don’t measure observability maturity by the number of dashboards. Measure it by whether your signals name the failing component and the next action before significant compute capacity is wasted.

## Start the discussion at forums.developer.nvidia.com
