# scaling-federated-learning-across-docker-kubernetes-and-slurm-with-nvidia-flare

source: https://developer.nvidia.com/blog/scaling-federated-learning-across-docker-kubernetes-and-slurm-with-nvidia-flare/

Federated learning (FL) projects often begin with a straightforward setup: one server, a few clients, and one dataset at each site. As those projects grow, the challenge shifts from running an algorithm to operating shared infrastructure. GPUs must be allocated when jobs need them, multiple research studies must remain separated, and every participating organization must retain control of its own data, secrets, and compute policies.

That operational complexity grows when organizations rely on different environments. One site may use a Docker host, another may run a Kubernetes cluster, and a research center may schedule its GPU workloads with Slurm. Requiring every participant to adopt the same infrastructure can turn platform standardization into a prerequisite for collaboration.

NVIDIA FLARE addresses this challenge by separating the persistent federation from the processes that execute each job.

FLARE’s two-layer architecture separates persistent federation services from job execution, allowing each site in the same federation to use the execution backend that fits its infrastructure—for example, Docker at one site, Kubernetes at another, and Slurm at a third. Each site retains local control over compute allocation and the datasets, images, secrets, and scheduling policies used by each study

Docker and Kubernetes deployment support is available in NVIDIA FLARE 2.8. FLARE 2.9 adds Slurm support.

## Separating federation coordination from job execution

A FLARE deployment has two operational layers. Long-running server and client parent processes maintain the federation, authenticate connections, and coordinate work. Separate server and client job workers execute a submitted FL job.

This separation enables resource-aware execution. The parent processes can remain available without occupying the GPUs required for training. When a data scientist submits a job, each parent launches a worker through its configured execution platform. The worker receives the job, uses the requested resources, returns its results, and exits when its work is complete.

The job describes resource intent separately from platform details. A job can request GPUs, whole schedulable CPU units, and host memory. Each site’s launcher combines those requirements with the local study configuration and translates them into a Docker container, Kubernetes pod, or Slurm allocation.

Together, these layers keep federation services available while job workers and their resources are created on demand at each site.

## Deploy job workers with Docker, Kubernetes, and Slurm

NVIDIA FLARE integrates with standard deployment and scheduling systems. The site operator selects the runtime that matches the local environment and remains responsible for its policies.

| Runtime | Typical environment | Dynamic execution unit | Resource authority |
|---|---|---|---|
| Docker | Workstation or single-host site | Job container | Docker host |
| Kubernetes | Cloud or on-premises cluster | Job pod | Kubernetes scheduler |
| Slurm | HPC or shared GPU cluster | Batch allocation | Slurm scheduler |

*Table 1. Comparison of NVIDIA FLARE deployment runtimes*

### Docker for containerized execution on one host

[Docker](https://www.docker.com/) is a practical option for a workstation, lab server, edge system, or other single-host environment. The persistent FLARE server or client runs in a parent container built from a parent image. For each submitted job, FLARE dynamically launches a separate job container built from a job image.

The parent image contains the FLARE runtime and the components needed to launch containers. A separate job image can contain the training framework, model code, and application dependencies. Sites can expose requested GPUs to job containers through NVIDIA Container Toolkit and use Docker settings for shared memory, mounts, networking, and other host-specific needs.

Separating parent and job images also makes updates easier. Infrastructure owners can keep the parent environment stable while researchers update their training environment independently, subject to the site’s image and code-approval policy.

### Kubernetes for dynamically scheduled job pods

In [Kubernetes](https://kubernetes.io/), a Helm chart installs each persistent FLARE server or client as a parent pod. For every submitted job, the parent creates a separate server or client job pod. The Kubernetes scheduler places that pod according to its CPU, memory, GPU, storage, and placement requirements.

This approach connects FLARE jobs to familiar Kubernetes capabilities. A site can use namespaces, service accounts, Secrets, persistent volumes, node selectors, tolerations, and admission policies. For example, a study can use a pod template to select H100 nodes while another study uses a different node pool.

Platform operators configure storage classes, registry credentials, network policy, GPU enablement, and role-based access control (RBAC) for their clusters. FLARE uses these services to launch and monitor job pods.

### Slurm for scheduled GPU and multi-node allocations

Many universities, research centers, and enterprise computing environments use [Slurm](https://slurm.schedmd.com/) to share GPU clusters. The FLARE Slurm launcher submits each server or client job worker as a batch job. Slurm selects the compute nodes and enforces the requested GPU, CPU, memory, partition, account, quality of service (QoS), and time limits.

Jobs can request a single node or multiple nodes. FLARE submits the allocation, monitors its state, propagates completion or failure, and cancels it when required. The launcher supports bare execution (no sandbox), Pyxis/Enroot containers, and Apptainer containers.

Slurm remains the resource authority. Its accounts, associations, partitions, QoS rules, cgroups, filesystem permissions, and device controls determine what an allocation can use. This preserves the operational model that cluster administrators already use for non-federated workloads.

NVIDIA FLARE provides participant authentication, secure communication, and authorization, while each site’s execution platform enforces local resource and workload policies. Site operators configure host and cluster security, approved images, secrets, and access controls, and validate workload isolation for their chosen runtime.

## Separating research with studies

Sharing infrastructure introduces another question: How can multiple teams run FL studies without mixing their users, jobs, or data?

FLARE studies provide a logical multi-tenant boundary within one deployment. Each study defines its participating client sites and the admin users who can open a session for that study. Study-aware operations limit job visibility, client status, submission targets, and deployment maps to the active study.

The study boundary continues at each participating site. A site-owned `local/study_runtime.yaml`

file maps a study to the resources that it can use locally. Depending on the runtime, this configuration can define:

- Dataset mounts
- Environment variables
- Secret-backed environment variables and file mounts
- A site-approved default job image
- Kubernetes pod templates
- Docker runtime settings
- Slurm sandbox, partition, account, and QoS policy

A data scientist selects the study by opening a study-scoped session, and jobs submitted from that session inherit the study context. The jobs do not choose arbitrary local dataset paths or supply secret values. The FLARE server verifies study membership before a job reaches a site, while the site operator controls the mapping from that study to local resources.

The following shortened Kubernetes example maps a pathology study to a site-owned data volume and database credentials. The configuration contains references to Secrets, not their values.

`format_version: 2` `studies:` ` ` `pathology:` ` ` `container:` ` ` `image: registry.example.com` `/pathology-trainer` `:1.0` ` ` `datasets:` ` ` `slides:` ` ` `source` `: pathology-data-pvc` ` ` `mode: ro` ` ` `secret_env:` ` ` `DB_USER: {` `source` `: pathology-db, key: username}` ` ` `DB_PASSWORD: {` `source` `: pathology-db, key: password}` |

When a job submitted from a pathology-scoped session reaches this site, the Kubernetes launcher selects the matching `studies.pathology`

entry. The launcher uses the study image as the local default and mounts the pathology-data-pvc volume read-only at `/data/pathology/slides`

inside the job container. The mount path is derived from the study and dataset names as `/data/<study>/<dataset>`

.

The `secret_env`

entries become Kubernetes `secretKeyRef`

references in the pod specification. Kubernetes injects the `username`

and `password`

values from the `pathology-db`

Secret when it starts the pod. This keeps the credential values in the site’s secret store while giving the study worker the environment it needs.

Studies are intended for organizations that share the same FLARE server and public key infrastructure (PKI) but need logical separation between experiments. Organizations that require a separate PKI, infrastructure administrator, or failure blast radius should use separate FLARE deployments.

## Bringing a heterogeneous federation together

In the federation shown in Figure 1, above, a pathology study connects both hospitals and the university, using GPU workers and each site’s approved image datasets. An outcomes study includes only the hospitals and uses CPU workers to analyze structured clinical data.

Both studies share the federation’s persistent services. Study membership determines which sites participate, while each site’s study configuration supplies the datasets, images, secrets, and scheduling settings for its workers. Researchers submit jobs from the appropriate study session, and the local launchers apply those settings.

## Submitting a job

FLARE 2.9 supports portable GPU, CPU, and host-memory requirements in `resource_spec`

within the job’s `meta.json`

. The portable keys are `num_of_gpus`

, `num_of_cpus`

, and `memory`

. CPU values represent whole schedulable CPU units, and memory uses positive integer quantities with Mi, Gi, or Ti units.

The `@default`

entry applies one resource profile to every targeted site, including the server. A named client or server entry provides only the values that differ. In this example, both hospitals inherit one GPU, four CPU units, and 64 GiB of memory. The university overrides the GPU count, while the server overrides the GPU count to zero. Both inherit the same CPU and memory requirements.

`{` ` ` `"resource_spec"` `: {` ` ` `"@default"` `: {` ` ` `"num_of_gpus"` `: 1,` ` ` `"num_of_cpus"` `: 4,` ` ` `"memory"` `: ` `"64Gi"` ` ` `},` ` ` `"server"` `: {` `"num_of_gpus"` `: 0},` ` ` `"university"` `: {` `"num_of_gpus"` `: 8}` ` ` `}` `}` |

Each launcher translates the resolved values into native settings. Docker converts four CPU units to `nano_cpus=4000000000`

, converts 64 GiB to a byte-valued `mem_limit`

, and applies the GPU device request. Kubernetes sets matching CPU and memory requests and limits and adds the GPU request. Slurm emits `--cpus-per-task=4`

, `--mem=65536M`

, and the corresponding GPU `--gres`

value.

A data scientist opens a study-scoped session and submits the job once to the FLARE server, which deploys it to the study’s participants. At each site, the configured launcher applies the study’s local runtime defaults and creates the worker. FLARE coordinates the federated workflow and reports job status while Docker, Kubernetes, and Slurm manage local resources.

Use `launcher_spec`

for backend-specific topology and policy, such as a Slurm node layout or runtime-specific image. The study runtime configuration supplies each site’s approved local defaults for images, datasets, secrets, and execution policy.

## What this enables

Federated learning infrastructure doesn’t need to be uniform across participants. FLARE separates persistent federation services from dynamically launched job workers so that each site can use Docker, Kubernetes, or Slurm. Studies add scoped membership and site-owned mappings for data, secrets, images, and scheduling policy.

Together, these capabilities enable one federation to span on-premises systems and clouds without forcing every organization onto the same platform. Sites can allocate GPUs and other resources when jobs need them, continue using their established operational controls, and run multiple studies over independently governed data. Heterogeneous infrastructure becomes part of the federation’s design rather than a barrier to scaling it.

To get started, explore the [NVIDIA FLARE documentation](https://nvflare.readthedocs.io/en/main/) and the [NVIDIA FLARE GitHub repository](https://github.com/NVIDIA/NVFlare).

## Start the discussion at forums.developer.nvidia.com
