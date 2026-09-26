source: https://docs.nvidia.com/aistore

AIStore: High-Performance, Scalable Storage for AI Workloads


AIStore: High-Performance, Scalable Storage for AI Workloads

AIStore (AIS) is a lightweight distributed storage stack tailored for AI applications. It’s an elastic cluster that can grow and shrink at runtime and can be ad-hoc deployed, with or without Kubernetes, anywhere from a single Linux machine to a bare-metal cluster of any size. Built from scratch, AIS provides linear scale-out, consistent performance, and a flexible deployment model.

AIS is a reliable storage cluster that can natively operate on both in-cluster and remote data, without treating either as a cache.

AIS consistently shows [balanced I/O distribution and linear scalability](https://aistore.nvidia.com/blog/2025/07/26/smooth-max-line-speed) across an arbitrary number of clustered nodes. The system supports fast data access, reliability, and rich customization for data transformation workloads.

## Features

- ✅
**Multi-Cloud Access:**Seamlessly access and manage content across multiple[cloud backends](https://docs.nvidia.com/aistore/overview#at-a-glance)(including AWS S3, GCS, Azure, and OCI), with fast-tier performance, configurable redundancy, and namespace-aware bucket identity (same-name buckets can coexist across accounts, endpoints, and providers). - ✅
**Deploy Anywhere:**AIS runs on any Linux machine, virtual or physical. Deployment options range from a[minimal container-based deployment](https://github.com/NVIDIA/aistore/blob/main/deploy/prod/docker/compose/README.md)and[Google Colab](https://aistore.nvidia.com/blog/2024/09/18/google-colab-aistore)to petascale[Kubernetes clusters](https://github.com/NVIDIA/ais-k8s). There are[no built-in limitations](https://github.com/NVIDIA/aistore/blob/main/docs/overview.md#no-limitations-principle)on deployment size or functionality. - ✅
**High Availability:**Redundant control and data planes. Self-healing, end-to-end protection, n-way mirroring, and erasure coding. Arbitrary number of lightweight access points (AIS proxies). - ✅
**HTTP-based API:**A feature-rich, native API (with user-friendly SDKs for Go and Python), and compliant[Amazon S3 API](https://docs.nvidia.com/aistore/s3compat)for running unmodified S3 clients. - ✅
**Monitoring:**Comprehensive observability with integrated Prometheus metrics, Grafana dashboards, detailed logs with configurable verbosity, and CLI-based performance tracking for complete cluster visibility and troubleshooting. See[AIStore Observability](https://docs.nvidia.com/aistore/monitoring-overview)for details. - ✅
**Chunked Objects:**High-performance chunked object representation, with independently retrievable chunks, metadata v2, and checksum-protected manifests. Supports rechunking, parallel reads, and seamless integration with[Get-Batch](https://docs.nvidia.com/aistore/get_batch),[blob-downloader](https://docs.nvidia.com/aistore/blob_downloader), and multipart uploads to supported cloud backends. - ✅
**JWT Authentication and Authorization:**[Validates request JWTs](https://docs.nvidia.com/aistore/auth_validation)to provide cluster- and bucket-level access control using static keys or dynamic OIDC issuer JWKS lookup. - ✅
**Intra-Cluster Request Signing:**Per-node Ed25519 identities sign and verify intra-cluster requests, signed redirects, and transport streams, with verifying keys distributed through the cluster map (enabled in v5.1, following the mandatory[v5.0 compatibility bridge](https://docs.nvidia.com/aistore/relnotes/5.0)). - ✅
**Load-Aware Throttling:**Dynamic request throttling based on a multi-dimensional load vector (CPU, memory, disk, file descriptors, goroutines) to protect AIS clusters under stress. - ✅
**Unified Namespace:**Attach AIS clusters together to provide unified access to datasets across independent clusters, allowing users to reference shared buckets with cluster-specific identifiers. - ✅
**Turn-key Cache:**In addition to robust data protection features, AIS offers a per-bucket configurable LRU-based cache with eviction thresholds and storage capacity watermarks. - ✅
**ETL Offload:**Execute I/O intensive data transformations[close to the data](https://docs.nvidia.com/aistore/etl), either inline (on-the-fly as part of each read request) or offline (batch processing, with the destination bucket populated with transformed results). - ✅
**Get-Batch:**Retrieve multiple objects and/or[archived files](https://docs.nvidia.com/aistore/archive)with a single call. Designed for ML/AI pipelines,[Get-Batch](https://docs.nvidia.com/aistore/get_batch)fetches an entire training batch in one operation, assembling a TAR (or other supported[serialization formats](https://docs.nvidia.com/aistore/archive)) that contains all requested items in the exact user-specified order ([paper](https://arxiv.org/abs/2602.22434)). - ✅
**Data Consistency:**Guaranteed[consistency](https://docs.nvidia.com/aistore/terminology#read-after-write-consistency)across all gateways, with[write-through](https://docs.nvidia.com/aistore/terminology#write-through)semantics in presence of[remote backends](https://docs.nvidia.com/aistore/terminology#backend-provider). - ✅
**Serialization & Sharding:**Native, first-class support for TAR, TGZ, TAR.LZ4, and ZIP[archives](https://docs.nvidia.com/aistore/archive)for efficient storage and processing of small-file datasets. Features include seamless integration with existing unmodified workflows across all APIs and subsystems. - ✅
**Kubernetes:**For production, AIS runs natively on Kubernetes. The dedicated[ais-k8s](https://github.com/NVIDIA/ais-k8s)repository includes the AIS K8s Operator, Ansible playbooks, Helm charts, and deployment guidance. - ✅
**Batch Jobs:**More than 30 cluster-wide[batch operations](https://docs.nvidia.com/aistore/batch)that you can start, monitor, and control otherwise. The list currently includes:

The feature set continues to grow and also includes:

[native bucket inventory (NBI)];[blob-downloader];[AuthN - authentication and authorization server]; runtime management of[TLS certificates]; full support for[adding/removing nodes at runtime]; adaptive[rate limiting]; and more.

For the original

white paperand design philosophy, please see[AIStore Overview], which also includes high-level block diagram, terminology, APIs, CLI, and more. For our 2024 KubeCon presentation, please see[AIStore: Enhancing petascale Deep Learning across Cloud backends].

## CLI

AIS includes an integrated, scriptable [CLI](https://docs.nvidia.com/aistore/cli) for managing clusters, buckets, and objects, running and monitoring batch jobs, viewing and downloading logs, generating performance reports, and more:

## Developer Tools

AIS runs natively on Kubernetes and features open format - thus, the freedom to copy or move your data from AIS at any time using the familiar Linux `tar(1)`

, `scp(1)`

, `rsync(1)`

and similar.

For developers and data scientists, there’s also:

[Go API](https://github.com/NVIDIA/aistore/tree/main/api)used in[CLI](https://docs.nvidia.com/aistore/cli)and[benchmarking tools](https://docs.nvidia.com/aistore/aisloader)[Python SDK](https://github.com/NVIDIA/aistore/tree/main/python/aistore/sdk)+[Reference Guide](https://docs.nvidia.com/aistore/python/aistore/sdk)[PyTorch integration](https://github.com/NVIDIA/aistore/tree/main/python/aistore/pytorch)and usage examples[Boto3 support](https://docs.nvidia.com/aistore/python/aistore/botocore_patch)

## Quick Start

- Read the
[Getting Started Guide](https://docs.nvidia.com/aistore/getting_started)for a 5-minute local install, or - Run a
[minimal container-based](https://github.com/NVIDIA/aistore/tree/main/deploy/prod/docker/compose)AIS cluster consisting of a single gateway and a single storage node, or - Clone the repo and run
`make kill cli aisloader deploy`

followed by`ais show cluster`


## Deployment options

AIS deployment options, as well as intended (development vs. production vs. first-time) usages, are all [summarized here](https://github.com/NVIDIA/aistore/blob/main/deploy/README.md).

Prerequisites essentially boil down to having Linux with a disk.
Deployment options range from a [minimal container-based deployment](https://github.com/NVIDIA/aistore/tree/main/deploy/prod/docker/compose) to petascale bare-metal clusters of any size, and from a single VM to multiple racks of high-end servers.
Practical use cases require, of course, further consideration.

Some of the most popular deployment options include:

For performance tuning, see

[performance]and[AIS K8s Playbooks].

## Existing Datasets

AIS supports multiple ingestion modes:

- ✅
**On Demand:**Transparent cloud access during workloads. - ✅
**PUT:**Locally accessible files and directories. - ✅
**Promote:**Import local target directories and/or NFS/SMB shares mounted on AIS targets. - ✅
**Copy:**Full buckets, virtual subdirectories (recursively or non-recursively), lists or ranges (via Bash expansion). - ✅
**Download:**HTTP(S)-accessible datasets and objects. - ✅
**Prefetch:**Remote buckets or selected objects (from remote buckets), including subdirectories, lists, and/or ranges. - ✅
**Archive:**[Group and store](https://aistore.nvidia.com/blog/2024/08/16/ishard)related small files from an original dataset.

## Install from Release Binaries

You can install the CLI and benchmarking tools using:

The script installs [aisloader](https://docs.nvidia.com/aistore/aisloader) and [CLI](https://docs.nvidia.com/aistore/cli) from the latest or previous GitHub [release](https://github.com/NVIDIA/aistore/releases) and enables CLI auto-completions.

## PyTorch integration

PyTorch integration is a growing set of datasets (both iterable and map-style), samplers, and dataloaders:

[Taxonomy of abstractions and API reference](https://docs.nvidia.com/aistore/python/aistore/pytorch)[AIS plugin for PyTorch: usage examples](https://github.com/NVIDIA/aistore/tree/main/python/aistore/pytorch/README.md)[Jupyter notebook examples](https://github.com/NVIDIA/aistore/tree/main/python/examples/pytorch/)

## AIStore Badge

Let others know your project is powered by high-performance AI storage:

## More Docs & Guides

[Overview and Design](https://docs.nvidia.com/aistore/overview)[Terminology and Core Abstractions](https://docs.nvidia.com/aistore/terminology)[Networking Model](https://docs.nvidia.com/aistore/networking)[Getting Started](https://docs.nvidia.com/aistore/getting_started)[AIS Buckets: Design and Operations](https://docs.nvidia.com/aistore/bucket)[Observability](https://docs.nvidia.com/aistore/monitoring-overview)[Technical Blog](https://aistore.nvidia.com/blog)[S3 Compatibility](https://docs.nvidia.com/aistore/s3compat)[Batch Jobs](https://docs.nvidia.com/aistore/batch)[Performance](https://docs.nvidia.com/aistore/performance)and[CLI: performance](https://docs.nvidia.com/aistore/cli/performance)[CLI Reference](https://docs.nvidia.com/aistore/cli)[Production Deployment: Kubernetes Operator, Ansible Playbooks, Helm Charts, Monitoring](https://github.com/NVIDIA/ais-k8s)

### How to find information

- See
[Extended Index](https://docs.nvidia.com/aistore/docs) - Use CLI
`search`

command, e.g.:`ais search copy`

- Clone the repository and run
`git grep`

, e.g.:`git grep -n out-of-band -- "*.md"`


## License

MIT

## Author

Alex Aizman (NVIDIA)