# topology-aware-workload-scheduling-with-nvidia-topograph

source: https://developer.nvidia.com/blog/topology-aware-workload-scheduling-with-nvidia-topograph/

AI factories are power-limited systems that deliver maximum value when fully optimized. GPU workload placement is a key optimization. Poor workload placement fragments topology domains and forces traffic across shared links, reducing throughput, raising job costs, and leaving GPUs consuming provisioned power while waiting on data without advancing the workload.

GPUs exchange data continuously during training and inference, so distributed workloads benefit from communication locality. [NVIDIA NVLink and NVLink Switch](https://www.nvidia.com/en-us/data-center/nvlink/) provide high-bandwidth, all-to-all scale-up connectivity within rack-scale GPU domains, while [NVIDIA Spectrum-X Ethernet](https://www.nvidia.com/en-us/networking/spectrumx/) provides predictable, low-latency scale-out networking across systems and racks.

A scheduler can place workloads efficiently only with a current, accurate view of those GPU and fabric relationships, and keeping that view current as the cluster changes is where placement breaks down in practice.

NVIDIA Topograph solves that problem. It discovers cluster topology from cloud APIs or on-premises fabric systems, normalizes it into a common model, and publishes it in the format each workload manager expects: Kubernetes node labels, Slurm topology configuration, or Slinky ConfigMaps. Within the [NVIDIA DSX OS](https://www.nvidia.com/en-us/data-center/products/dsx/) cluster orchestration layer, Topograph works alongside [Dynamic Resource Allocation (DRA)](https://blogs.nvidia.com/blog/nvidia-at-kubecon-2026/) and KAI Scheduler to enable topology-aware gang scheduling across AI factory infrastructure.

This post walks through deploying Topograph and using it to schedule [topology-aware workloads](https://github.com/dsx-ai-factory/topograph) on Kubernetes, Slurm, and Slinky.

## The core topology problem

Topograph maps how cluster hardware is connected so schedulers can favor nearby resources. Think of the network as a road system: GPUs within the same locality domain have short, high-bandwidth paths, while traffic between domains crosses more shared links and switches. Spreading a tightly coupled workload across distant domains can increase contention and latency, so Topograph helps place workloads in the most efficient locations and avoid these bottlenecks.

Modern [NVIDIA Quantum InfiniBand](https://www.nvidia.com/en-us/networking/products/infiniband/) ports can achieve up to [800 Gb/s](http://nvidia.com/en-us/networking/products/infiniband/quantum-x800), while NVIDIA NVLink provides 1.8 TB/s of bidirectional bandwidth per GPU in its fifth generation (NVIDIA Blackwell, such as GB200/GB300) and 3.6 TB/s per GPU in its sixth generation (Vera Rubin), through a dedicated NVIDIA NVLink Switch fabric. That non-blocking, all-to-all design gives each GPU its own lane rather than sharing bandwidth under load. Schedulers with a current view can favor GPUs in the closest topology domain.

[Slurm](https://github.com/schedmd/slurm) and Kubernetes both support topology-aware allocation, but a scheduler can only act on the topology it observes. Topograph regenerates that view on request and upon watched cluster changes, so the scheduler works from current data rather than a manually maintained snapshot.

### A common model across environments

[Topograph](https://github.com/dsx-ai-factory/topograph) is an open source toolkit that identifies a cluster’s network topology, enabling workload managers to make topology-aware scheduling decisions. It has two concepts: providers and engines. A provider discovers topology from cloud APIs or on-premises systems and normalizes it into a canonical model. An engine translates that model into Slurm configuration, Kubernetes labels, Slinky ConfigMaps, Node Feature Discovery (NFD) resources, or instance-oriented topology JSON.

Cloud providers that have a working integration with Topograph include [Google Cloud](https://github.com/dsx-ai-factory/topograph/blob/main/docs/providers/gcp.md), [Lambda](https://github.com/dsx-ai-factory/topograph/blob/main/docs/providers/lambdai.md), [Nebius](https://github.com/dsx-ai-factory/topograph/blob/main/docs/providers/nebius.md), [Nscale](https://github.com/dsx-ai-factory/topograph/blob/main/docs/providers/nscale.md), and [OCI](https://github.com/dsx-ai-factory/topograph/blob/main/docs/providers/oci.md), with more cloud and colocation providers in development.

When used on-premises, use the [InfiniBand provider](https://github.com/dsx-ai-factory/topograph/blob/main/docs/providers/infiniband.md) with `ibnetdiscover`

, or [NetQ](https://github.com/dsx-ai-factory/topograph/blob/main/docs/providers/netq.md) for [Spectrum-X ](https://www.nvidia.com/en-us/networking/spectrumx/)or [Multi-Node NVLink](https://docs.nvidia.com/multi-node-nvlink-systems/index.html) (MNNVL) domains.

The provider interface is open, so operators can add one for their own environment and contribute it upstream.

### Environment and Engine Support

Environment or provider | Kubernetes | Slurm | Graph | ||
Node labels(k8s) | NFD resources(nfd) | Slinky ConfigMap(slinky) | |||
Cloud and hosted providers | |||||
Crusoe | Yes | Yes | Yes | Yes | Yes |
Google Cloud | Yes | Yes | Yes | Yes | Yes |
Lambda | Yes | Yes | Yes | Yes | Yes |
Nebius | Yes | Yes | Yes | Yes | Yes |
Nscale | Yes | Yes | Yes | Yes | Yes |
Oracle Cloud Infrastructure (OCI) | Yes | Yes | Yes | Yes | Yes |
On-premises deployment models | |||||
InfiniBand in Kubernetes | Yes | Yes | Yes | Yes | Yes |
InfiniBand on bare metal or VMs | No | No | No | Yes | Yes |
On-premises networking and topology | |||||
Spectrum-X or NetQ-managed fabric | Yes | Yes | Yes | Yes | Yes |
MNNVL NVLink partitions (DRA block topology only) | No | No | Yes | No | No |

*Table 1. Supported topology providers by engine*

**Scope and interpretation**. This matrix reflects current upstream main as of September 16, 2026. It shows supported provider-to-engine output combinations; requirements can vary by Topograph version, environment, and provider configuration.

- The Crusoe provider reads fabric and accelerator-domain labels from Crusoe Managed Kubernetes nodes; Topograph therefore runs in Kubernetes for this provider.
- The Slurm engine can run in Kubernetes, but it requires a writable volume for its configured
`topology.conf`

output path. - The NFD engine requires the alpha NodeFeatureGroupAPI feature gate. The Kubernetes engine publishes Node labels instead.

## Staying current as the cluster changes

Five components keep that view current:

**API Server:**Validates requests, aggregates duplicates, and dispatches discovery**Node Observer:**Watches configured Kubernetes node or Pod changes and API readiness, then requests regeneration with retries**Node Data Broker:**Collects per-node attributes and stores them as node annotations**Provider:**Converts cloud or fabric data into the canonical representation**Engine:**Writes the representation in a format the scheduler understands

### How clients query topology

The API server exposes five service endpoints:

`POST /v1/generate`

– submits an asynchronous request and returns its ID with HTTP 202.`GET /v1/topology?uid=<request-id>`

– returns HTTP 202 while processing and HTTP 200 with the result when complete.`POST /v1/lookup`

– returns the cached status or result for the same request body without submitting it again.`GET /healthz`

– is the liveness endpoint.`GET /metrics`

– exposes Prometheus metrics.

The aggregation delay is required; 15 seconds is typical. Repeated identical requests reset a trailing timer and are processed once, reducing redundant work during bursts of cluster events.

For testing without production hardware, simulation models describe node and switch hierarchies. The `kwok-nodes`

utility and Kind/KWOK helpers turn those models into virtual Kubernetes nodes.

## Solving it on Kubernetes (engine: k8s)

The default Kubernetes scheduler doesn’t discover physical interconnect hierarchy. Topograph addresses that gap by publishing provider-reported topology as node labels, which native affinity and topology-aware schedulers can consume.

Prerequisites are Kubernetes 1.27 or later, Helm 3.10+ or 4.x, kubectl permissions, and a supported [provider](https://github.com/dsx-ai-factory/topograph/tree/main/docs/providers). [KAI Scheduler](https://github.com/kai-scheduler/KAI-Scheduler) or [Kueue TAS](https://kueue.sigs.k8s.io/docs/concepts/topology_aware_scheduling/) is optional for topology-aware gang scheduling.

### Deploying Topograph with Helm

Topograph is distributed as a [Helm chart](https://github.com/dsx-ai-factory/topograph/blob/main/charts/topograph/README.md):

`helm repo add topograph https:` `//dsx-ai-factory` `.github.io` `/topograph` `helm repo update` `helm ` `install` `topograph topograph` `/topograph` `\` `--namespace topograph \` `--create-namespace \` `--` `set` `engine.name=k8s \` `--` `set` `provider.name=<provider>` |

Replace `<provider>`

with the value that matches your environment.

The repository includes example Helm values files in `charts/topograph`

, named with a `values.k8s`

prefix and a short scenario description. Each carries inline configuration comments.

After installation, verify that the deployment completed successfully:

`helm ` `test` `topograph --namespace topograph` |

The bundled test hooks query `/healthz`

and `/metrics`

in-cluster and confirm the responses include the `topograph_version`

metric.

Confirm the Pods are running:

`kubectl get pods -n topograph` |

### Verifying topology labels on nodes

Topograph represents fabric locality with a variable-depth label family and accelerator locality with a two-level hierarchy:

`fabric.topograph.run` `/tier-0` `# switch closest to the node` `fabric.topograph.run` `/tier-1` `# next fabric tier outward` `fabric.topograph.run` `/tier-` `<N> ` `# additional discovered tiers` `accelerator.topograph.run` `/domain` `# accelerator domain` `accelerator.topograph.run` `/sub-domain` `# optional nested sub-domain` |

Fabric tier 0 is the leaf switch closest to the compute node, and tier numbers increase outward. Topograph writes only the tiers present in the discovered topology, with no fixed maximum depth. Operators can set the Kubernetes engine’s `fabricLabels`

array and `acceleratorLabel`

parameter to use custom keys; tiers beyond that array are not labeled. The sub-domain key is fixed.

To verify that the labels have been applied, run:

`kubectl get nodes --show-labels | ` `grep` `-E ` `'fabric\.topograph\.run|accelerator\.topograph\.run'` |

If labels are missing, inspect the Topograph logs:

`kubectl logs -n topograph -l app.kubernetes.io` `/name` `=topograph` |

**NOTE:** Topograph reflects reported rather than intended topology. Labels refresh when generation runs, for example, after a watched node or pod change. Visibility of a fabric change depends on the provider and its triggering events.

### Exposing the API

The API is a ClusterIP service by default. With the release and namespace above, its address is: `topograph.topograph.svc.cluster.local:49021`

.

For local debugging:

`kubectl -n topograph port-forward svc` `/topograph` `49021:49021` `curl http:` `//localhost` `:49021` `/healthz` |

### Using standard Kubernetes scheduling

Topology labels can be used as `topologyKey`

values in preferred Pod affinity:

`affinity:` ` ` `podAffinity:` ` ` `preferredDuringSchedulingIgnoredDuringExecution:` ` ` `- weight: 90` ` ` `podAffinityTerm:` ` ` `labelSelector:` ` ` `matchLabels:` ` ` `app: myapp` ` ` `topologyKey: fabric.topograph.run/tier-0` ` ` `- weight: 70` ` ` `podAffinityTerm:` ` ` `labelSelector:` ` ` `matchLabels:` ` ` `app: myapp` ` ` `topologyKey: fabric.topograph.run/tier-1` |

Each matching term contributes to a candidate node’s score, strongly favoring the tier-0 domain of existing `app=myapp`

Pods while also rewarding tier-1 locality. Because the default scheduler places Pods individually, this is a preference rather than globally optimal gang placement.

KAI Scheduler and Kueue can use the same node labels for topology-aware gang placement. Kubernetes 1.36 also introduced alpha [topology-aware workload scheduling](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-aware-scheduling/) through [KEP-5732](https://github.com/kubernetes/enhancements/blob/master/keps/sig-scheduling/5732-topology-aware-workload-scheduling/README.md). Upstream beta work is ongoing; consult the enhancement tracker rather than depending on a specific future release.

### Using KAI Scheduler for Topology-Aware Gang Scheduling

[KAI Scheduler](https://www.cncf.io/projects/kai-scheduler/) (a CNCF Sandbox project donated by NVIDIA) organizes node labels into a [hierarchy](http://github.com/kai-scheduler/KAI-Scheduler/tree/main/docs/topology):

`apiVersion: kai.scheduler/v1alpha1` `kind: Topology` `metadata:` ` ` `name: cluster-topology` `spec:` ` ` `levels:` ` ` `- nodeLabel: topology.kubernetes.io/zone` ` ` `- nodeLabel: fabric.topograph.run/tier-1` ` ` `- nodeLabel: fabric.topograph.run/tier-0` ` ` `- nodeLabel: kubernetes.io/hostname` |

Apply it with `kubectl apply -f cluster-topology.yaml`

, then annotate a multi-Pod Job:

`apiVersion: batch/v1` `kind: Job` `metadata:` ` ` `name: topology-aware-workers` ` ` `annotations:` ` ` `kai.scheduler/topology: cluster-topology` ` ` `kai.scheduler/topology-required-placement: fabric.topograph.run/tier-1` ` ` `kai.scheduler/topology-preferred-placement: fabric.topograph.run/tier-0` `spec:` ` ` `parallelism: 4` ` ` `completions: 4` ` ` `template:` ` ` `metadata:` ` ` `labels:` ` ` `app: inference-worker` ` ` `spec:` ` ` `schedulerName: kai-scheduler` ` ` `restartPolicy: Never` ` ` `containers:` ` ` `- name: worker` ` ` `image: nvcr.io/nvidia/nemo:latest` ` ` `resources:` ` ` `limits:` ` ` `nvidia.com/gpu: 1` |

The required annotation keeps the gang within a single tier-1 domain. The preferred annotation asks KAI to concentrate Pods in a tier-0 domain when feasible, but permits multiple tier-0 domains inside the required boundary.

For more advanced topology-aware scheduling examples, see the documentation for[ Grove](https://github.com/ai-dynamo/grove/blob/main/docs/user-guide/topology-aware-scheduling.md#define-a-cluster-topology) and[ NVIDIA Dynamo](https://docs.nvidia.com/dynamo/dev/knowledge-base/kubernetes/multinode/topology-aware-scheduling).

[Grove](https://github.com/ai-dynamo/grove) provides Kubernetes APIs and an operator for hierarchical gang scheduling, topology-aware placement, and coordinated scaling. [Dynamo](https://github.com/ai-dynamo/dynamo) is an open source distributed inference serving framework that integrates with Grove for Kubernetes workload orchestration.

## Publishing topology through NFD (engine: nfd)

Topograph also supports consumers already using Node Feature Discovery. The `nfd`

engine publishes one NodeFeature per selected topology node and one NodeFeatureGroup for every distinct fabric-tier, XCLR-domain, and XCLR-sub-domain value. The NFD master evaluates those specifications and owns each group’s `status.nodes`

membership.

Install `nfd`

first with its alpha NodeFeatureGroupAPI feature gate enabled; it is off by default. Then select the engine and the namespace where the NFD master runs:

`engine:` ` ` `name: nfd` `nfdNamespace: node-feature-discovery` |

Use this output when a downstream component consumes NodeFeatureGroup objects; it is not a substitute for Kubernetes `topologyKey`

labels. For native Pod affinity, KAI Scheduler, or Kueue TAS, continue to use `engine: k8s`

. The chart scopes NFD permissions to the `nfd`

namespace. The engine deletes stale Topograph-managed objects after reconciliation, but preserves the last published topology if a generation produces none.

## Solving it on Slurm (engine: slurm)

Topograph generates cluster-wide configurations in the [tree and block formats](https://slurm.schedmd.com/topology.conf.html), shown in the top-center and bottom-center panels of Figure 2, below. Slurm 25.05 introduced per-partition configuration in [YAML format](https://slurm.schedmd.com/topology.yaml.html), which Topograph also supports, as shown in the diagram.

### Installing Topograph

Slurm clusters typically run on Linux bare-metal servers or virtual machines, where Topograph is installed via a native package manager. The repository includes Debian and RPM build targets:

`make` `deb ` `# Debian / Ubuntu` `make` `rpm ` `# RHEL / Rocky / SUSE` |

The package installs the service without starting it, so you can review and edit the configuration file `/etc/topograph/topograph-config.yaml`


`http:` `port: 49021` `provider: <provider>` `engine: slurm` `requestAggregationDelay: 15s` |

Replace `<provider>`

with the value that matches your environment.

After updating the configuration, start the service and verify that it is healthy:

`sudo` `systemctl ` `enable` `--now topograph.service` `curl http:` `//localhost` `:49021` `/healthz` |

### Generating Slurm topology configuration

To initiate discovery, POST to Topograph’s `/v1/generate`

endpoint, which regenerates the Slurm topology configuration.

Submit a request and poll its result:

`id` `=$(curl -s -X POST -H ` `'Content-Type: application/json'` `\` ` ` `-d @payload.json http:` `//localhost` `:49021` `/v1/generate` `)` `curl -s ` `"` |

For cluster-wide tree output, use an absolute path:

`{` ` ` `"engine": {` ` ` `"name": "slurm",` ` ` `"params": {` ` ` `"plugin": "topology/tree",` ` ` `"topologyConfigPath": "/etc/slurm/topology.conf",` ` ` `"reconfigure": true` ` ` `}` ` ` `}` `}` |

Use `topology/block`

plus optional `blockSizes`

for block output.

The optional `reconfigure`

parameter runs `scontrol reconfigure`

after a file is written and defaults to false. If `topologyConfigPath`

is omitted, Topograph returns the generated content from the result endpoint instead of writing a file.

`{` ` ` `"engine": {` ` ` `"name": "slurm",` ` ` `"params": {` ` ` `"topologies": {` ` ` `"gpu-block": {` ` ` `"partition": "gpu",` ` ` `"plugin": "topology/block",` ` ` `"blockSizes": [8, 16]` ` ` `},` ` ` `"cpu-tree": {` ` ` `"partition": "cpu",` ` ` `"plugin": "topology/tree"` ` ` `},` ` ` `"default": {` ` ` `"plugin": "topology/flat",` ` ` `"clusterDefault": true` ` ` `}` ` ` `},` ` ` `"topologyConfigPath": "/etc/slurm/topology.yaml",` ` ` `"reconfigure": true` ` ` `}` ` ` `}` `}` |

For node-state-driven refresh with a provider that auto-discovers Slurm node mappings, run the repository’s script as root:

`scripts` `/create-topology-update-script` `.sh -p <provider> -c ` `/etc/slurm/topology` `.conf` |

It registers a permanent `strigger`

for node up and down transitions. It does not detect arbitrary switch rewiring or every inventory change.

## Solving It on Slinky (engine: slinky)

Slinky, developed by SchedMD, runs Slurm on Kubernetes. NVIDIA acquired SchedMD in December 2025. The Topograph Slinky engine maps Kubernetes nodes to `slurmd`

Pods and writes Slurm topology data to a ConfigMap.

The Slinky engine supports cluster-wide `topology/tree`

and `topology/block`

output, as well as multiple-topology YAML for partition-specific configurations.

Install Topograph as a [Helm chart](https://github.com/dsx-ai-factory/topograph/blob/main/charts/topograph/README.md):

`helm repo add topograph https:` `//dsx-ai-factory` `.github.io` `/topograph` `helm repo update` `helm ` `install` `topograph topograph` `/topograph` `\` ` ` `--namespace topograph \` ` ` `--create-namespace \` ` ` `--values my-values.yaml` |

The repository provides ready-to-adapt Helm examples for [tree](https://github.com/NVIDIA/topograph/blob/main/charts/topograph/values.slinky.tree-example.yaml), [block](https://github.com/NVIDIA/topograph/blob/main/charts/topograph/values.slinky.block-example.yaml), [per-partition](https://github.com/NVIDIA/topograph/blob/main/charts/topograph/values.slinky.partition-example.yaml), and [InfiniBand block](https://github.com/NVIDIA/topograph/blob/main/charts/topograph/values.slinky.ib.block-example.yaml) deployments.

Topograph regenerates and updates the ConfigMap when selected `slurmd`

Pods change.

The `dra`

provider is a narrower Slinky block-topology option for MNNVL systems. It reads existing `nvidia.com/gpu.clique`

labels when regenerating the topology configuration.

For dynamic Slurm nodes, the optional `useDynamicNodes`

mode also annotates selected Kubernetes nodes with the current Slurm topology specification. ConfigMap updates and dynamic-node reconciliation are distinct mechanisms, so choose the mode that matches the deployed Slinky configuration.

## Getting started

Placement problems compound at scale and surface as network congestion. Topograph gives schedulers a current, provider-reported map of the physical network, so topology-aware decisions stay consistent across cloud and on-premises environments without manual maintenance.

Through KAI Scheduler, Kueue, and native Kubernetes, the map improves AI factory efficiency, tokens per watt, and cost.

Deploy Topograph from the [dsx-ai-factory/topograph GitHub repo](https://github.com/dsx-ai-factory/topograph), or learn more about the [DSX OS ecosystem](https://docs.nvidia.com/dsx).

## Start the discussion at forums.developer.nvidia.com
