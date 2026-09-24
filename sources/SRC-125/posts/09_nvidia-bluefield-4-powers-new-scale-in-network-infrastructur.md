# nvidia-bluefield-4-powers-new-scale-in-network-infrastructure-for-agentic-ai-factories

source: https://developer.nvidia.com/blog/nvidia-bluefield-4-powers-new-scale-in-network-infrastructure-for-agentic-ai-factories/

Traditional cloud infrastructure was designed for predictable, general-purpose workloads and standard interfaces. Agentic AI factories connect diverse users, agents, applications, data sources, and storage systems to massively accelerated compute at multi-terabit bandwidth per server, making dedicated DPU processing essential for line-rate networking, storage, and security. NVIDIA is introducing Scale-In network infrastructure, the fifth pillar of NVIDIA AI networking, bringing purpose-built acceleration to secure, manage, and operate agentic AI factories.

Scale-In evolves north-south networks into a coordinated infrastructure domain for the AI factory. Powered by [NVIDIA BlueField-4](https://www.nvidia.com/en-us/networking/products/data-processing-unit/) and [NVIDIA DOCA](https://www.nvidia.com/en-us/networking/products/software/doca/) and connected over [NVIDIA Spectrum-X Ethernet](https://www.nvidia.com/en-us/networking/spectrumx/), Scale-In accelerates the services that secure the full AI stack and move application, data, and storage traffic across the AI factory. Dedicated, host-independent processing keeps these infrastructure services off host CPUs, helping prevent security, data access, and operations from becoming bottlenecks as AI compute scales. The result is a more secure and efficient shared AI infrastructure with consistent access to AI services and data as demand grows.

This post explores the BlueField-4 architecture and explains how Scale-In delivers secure access, high-performance data movement, tenant isolation, simpler operations, and more predictable performance for agentic AI factories.

## Scale-In accelerates north-south AI factory infrastructure

AI factories have distinct infrastructure requirements at different scales:

**Scale-Up:**[NVIDIA NVLink](https://www.nvidia.com/en-us/data-center/nvlink/)unites GPUs as a coherent accelerator.**Scale-Out:**NVIDIA Spectrum-X Ethernet and[NVIDIA Quantum InfiniBand](https://www.nvidia.com/en-us/networking/products/infiniband/)connect servers across an AI factory.**Scale-Across:**[NVIDIA Spectrum-XGS Ethernet](https://nvidianews.nvidia.com/news/nvidia-introduces-spectrum-xgs-ethernet-to-connect-distributed-data-centers-into-giga-scale-ai-super-factories)connects distributed AI factories.**Context Memory:**[NVIDIA CMX](https://www.nvidia.com/en-us/data-center/ai-storage/cmx/), built on the[NVIDIA STX](https://www.nvidia.com/en-us/data-center/ai-storage/stx/)modular foundation for AI-native storage, provides shared KV-cache storage within the factory.**Scale-In:**NVIDIA BlueField-4, NVIDIA DOCA, and NVIDIA Spectrum-X Ethernet accelerate the access, security, data movement, and infrastructure operations surrounding AI compute.

North-south networks provide the access path into and out of a data center, connecting users, applications, data sources, storage systems, and services to individual systems. Traditional cloud data centers built these networks around software-defined infrastructure, composability, and elasticity, so resources and access could be provisioned and scaled as demand changed.

Agentic AI raises the demand on this infrastructure. Software-defined networking, composability, and elasticity remain essential, but they are no longer sufficient. AI factories bring together massive accelerated compute with growing numbers of users, agents, applications, enterprise data sources, and storage systems, all interacting continuously and at scale.

The infrastructure must be accelerated and co-designed as part of the AI factory. Security, multi-tenant networking, data and storage access, and infrastructure operations can’t rely solely on software running on general-purpose host CPUs or operate as independently managed layers. These functions must work together as a unified infrastructure domain, giving operators consistent control over access, data movement, security, provisioning, and observability across the AI factory.

Scale-In addresses these requirements by evolving north-south access into a unified, accelerated infrastructure domain across the AI factory. BlueField-4 provides host-independent acceleration and offload, DOCA provides a unified model for programming and operating infrastructure services, and Spectrum-X Ethernet provides high-performance Ethernet connectivity across the Scale-In access path, including external storage and data sources. Together, they give operators consistent control over access, data movement, security, provisioning, and observability across the infrastructure that supports accelerated compute and data storage.

AI factories rely on complementary storage infrastructures for persistent data and inference context. Scale-In provides high-performance access to AI-native storage, including AI factory storage for training, inference, and analytics, as well as enterprise AI data systems for retrieval and multimodal indexing. Separately, CMX provides pod-level storage for shared KV cache and reusable inference state inside the factory. BlueField-4 serves as the infrastructure processor for Scale-In and, separately, as the data and storage processor for CMX. Scale-In connects AI factory and enterprise data to AI compute, while CMX preserves and shares context for faster and more efficient inference.

Together, these five infrastructure pillars address distinct requirements across the AI factory. **Scaling GPUs, racks, and data centers delivers value only when data access, storage, cybersecurity, and operations scale with them.**

## BlueField-4 powers Scale-In infrastructure

BlueField-4 accelerates Scale-In services across GPU servers, agentic CPU systems, AI factory storage systems, and cloud services. In [NVIDIA Vera Rubin NVL72](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/), [NVIDIA ConnectX-9 SuperNICs](https://www.nvidia.com/en-us/networking/products/ethernet/supernic/) carry tenant workload traffic over the Scale-Out network, while BlueField-4 runs and accelerates the infrastructure services that connect, secure, and manage each server. BlueField-4 gives operators a separate infrastructure-processing domain outside the tenant host, where they can manage security policies, service state, and telemetry without relying on the host CPU or consuming its resources.

[NVIDIA BlueField Astra](https://developer.nvidia.com/blog/redefining-secure-ai-infrastructure-with-nvidia-bluefield-astra-for-nvidia-vera-rubin-nvl72/) extends trusted control from north-south access into the east-west Scale-Out fabric. Astra gives service providers a unified, host-independent control point for provisioning, tenant isolation, and network policy across both domains. BlueField-4 installs and updates policies and monitors telemetry, while ConnectX-9 enforces those policies directly in the data path. This closed loop provides consistent control across Scale-In and Scale-Out without placing device management in the tenant host.

BlueField-4 combines programmable control-plane processing with accelerated data-path processing. Software makes infrastructure decisions, while inline engines enforce them locally without returning the work to the host CPU. This design enables policies to be coordinated across the factory and enforced locally at line rate. Table 1 summarizes how the primary components support this processing model.

| Component | Role | Benefit |
|---|---|---|
| 64-core NVIDIA Grace CPU | Runs policy, provisioning, telemetry, and infrastructure-orchestration software | Provides 6x more compute than its predecessor, enabling multiple infrastructure services to run concurrently |
| Inline acceleration engines | Process packets, RDMA, storage protocols, encryption, firewall rules, and policy enforcement | Handle operations at up to 800 Gb/s while reducing the processing burden on the Grace CPU and host CPU |
| LPDDR5X memory subsystem | Supplies data and service state to infrastructure software | Provides high memory bandwidth and power-efficient operation without creating a memory bottleneck |
| PCIe Gen6 host connection | Connects BlueField-4 to the host server | Provides a high-bandwidth path between the host and the Scale-In infrastructure-processing domain |
| 800 Gb/s network interface | Connects the server to the Scale-In fabric | Supports high-throughput access, security, data movement, and storage traffic |

*Table 1. BlueField-4 components balance control-plane processing, data-path acceleration, memory access, host I/O, and network bandwidth across the Scale-In processing path.*

Compared with BlueField-3, BlueField-4 provides 4x more memory bandwidth and 2x more network bandwidth. This additional capacity supports more concurrent services, larger policy and telemetry datasets, and greater traffic-processing and security throughput.

### NVIDIA DOCA programs Scale-In services

NVIDIA DOCA turns BlueField-4’s hardware accelerators into programmable and deployable Scale-In services. Production-ready, containerized DOCA microservices can run directly on BlueField-4, while DOCA libraries and SDKs give developers access to accelerated networking, security, storage, and telemetry capabilities for custom services. DOCA Flow programs hardware packet-processing pipelines, DOCA PCC supports programmable congestion behavior, DOCA Telemetry exposes device and service health, and DOCA Platform Framework (DPF) manages provisioning, deployment, and updates. BlueField-4’s multiservice architecture and native service function chaining direct each traffic flow through the required sequence of services. These capabilities give Scale-In a unified software model for operating services across BlueField-4 systems instead of managing separate server pipelines.

### NVIDIA Spectrum-X Ethernet connects the Scale-In fabric

NVIDIA Spectrum-X Ethernet provides the high-performance fabric across the Scale-In access path, including external storage. BlueField-4 processes infrastructure services at each system, while Spectrum-X Ethernet carries traffic between the AI factory and the users, applications, data sources, services, and external storage around it. Spectrum-X Ethernet addresses load-balancing conflicts and congestion at scale, improves resource utilization, helps maintain high effective bandwidth, and isolates concurrent traffic so access and storage flows receive more consistent, predictable performance.

BlueField-4 DPUs, DOCA microservices, and Spectrum-X Ethernet networking are co-designed with NVIDIA Vera Rubin so that processor performance, memory bandwidth, PCIe connections, network bandwidth, acceleration, and software can keep pace with one another. Together, they provide a Scale-In path that handles transport, service processing, and control without consuming resources assigned to AI workloads.

## Key Scale-In use cases for the agentic AI factory

Agentic AI factories must share accelerated infrastructure safely, supply it with enterprise data, bring systems online, and continuously monitor performance. The following use cases show how BlueField-4 acceleration and DOCA services address these production requirements.

### Build isolated AI factory virtual private clouds

An AI factory virtual private cloud (VPC) isolates tenant and application traffic on shared physical infrastructure. DOCA Host-Based Networking (HBN) accelerates north-south Layer 3 routing and multi-tenant isolation on BlueField-4. DOCA Flow programs traffic classification and access-control rules, while DOCA-accelerated Open vSwitch (OVS-DOCA) applies the corresponding policy on east-west interfaces. BlueField Astra extends the same VPC policy across east-west Scale-Out interfaces, so one policy model governs both access and Scale-Out traffic.

In Vera Rubin, this coordinated model spans 7.2 Tb/s of aggregate interface bandwidth, comprising 800 Gb/s on the north-south BlueField-4 path and four 1.6 Tb/s east-west paths per compute tray. This delivers consistent policy coverage across both access and Scale-Out traffic without routing all east-west traffic through the 800 Gb/s interface. Operators centrally provision isolated AI factory VPCs while tenants continue using the accelerated fabric. This architecture provides cloud-like elasticity, consistent isolation, lower host CPU overhead, and more efficient use of shared AI infrastructure.

### Enforce security in silicon

BlueField-4 places the enforcement point in hardware, outside the host operating system. Tenant software cannot disable or bypass these controls, while offloaded security processing preserves host CPU cycles and avoids a separate software hop. BlueField-4 accelerates threat detection and enforces network, file, and object access policies at line rate. DOCA Argus provides runtime threat detection, DOCA Vault enforces file-access policy, and DOCA Flow programs line-rate network enforcement. BlueField Astra coordinates encryption, isolation, and policy across different networks on each server. Astra synchronizes policy, telemetry, keys, and enforcement across north-south and east-west traffic, keeping privileged security control outside tenant hosts, providing consistent protection for shared AI services, and preserving host resources for AI workloads.

### Accelerate storage access

Scale-In connects AI compute to training data, model assets, enterprise knowledge, and application data from external storage. If storage protocol processing, storage virtualization, or data movement cannot keep pace, GPUs wait for data despite having available compute and Scale-Up/Scale-Out network bandwidth.

BlueField-4 accelerates NVMe-oF, file and object storage protocols over RDMA and TCP, storage virtualization, and data movement on dedicated infrastructure. Spectrum-X Ethernet provides the AI-optimized Ethernet fabric across the storage path, where congestion management and performance isolation help sustain high effective bandwidth across concurrent storage flows, up to 1.45x more storage throughput than off-the-shelf Ethernet. This reduces host CPU overhead, helps keep AI compute fed, and provides more consistent access to enterprise data for training, retrieval, and inference. This external-data path complements CMX.

### Run the AI factory control plane

AI factory nodes must be provisioned, configured, secured, and connected before they run AI workloads. BlueField-4 onboards nodes, provisions networking and storage resources, starts servers, and loads the host operating system over the network. Because this control plane operates independently of the host, it establishes policies and provisions resources before tenant software starts. DOCA Platform Framework is a Kubernetes-native orchestration framework that provisions, manages, and scales BlueField DPUs as Kubernetes nodes. It manages DPU discovery, provisioning, service deployment, and updates across the [AI factory](https://www.nvidia.com/en-us/glossary/ai-factory/). This shortens deployment, improves configuration consistency, preserves host CPU resources, and brings new AI capacity online sooner.

### Observe and optimize AI operations

Operating an AI factory at scale requires continuous visibility into network traffic, storage access, service health, performance, and resource utilization. DOCA Telemetry collects and exports this information to network monitoring platforms, while DOCA libraries enable observability providers to integrate the same infrastructure signals into their own tools. By gathering telemetry through BlueField-4, operators retain visibility independent of tenant-host software. When infrastructure telemetry extends to GPU and network utilization, operators can identify constraints related to access, traffic, storage, policy enforcement, or workload placement. This fleet-wide visibility helps detect anomalies, locate bottlenecks, and resolve incidents before they affect AI workloads.

## Scale-In turns scaled compute into AI factory performance

Scale-In evolves north-south networks into a coordinated, accelerated infrastructure domain for data access, security, and operations. NVIDIA BlueField-4 provides networking acceleration, DOCA programs, and operates the services, while Spectrum-X Ethernet delivers high effective bandwidth and performance isolation across the Scale-In access and storage paths. Together, they help turn scaled compute into a secure and operational AI factory platform.

### Next steps

[Explore the NVIDIA BlueField platform](https://www.nvidia.com/en-us/networking/products/data-processing-unit/)for product architecture, specifications, and resources.- Learn more about
[NVIDIA Spectrum-X Ethernet](https://www.nvidia.com/en-us/networking/spectrumx/)and the[NVIDIA DOCA software framework](https://www.nvidia.com/en-us/networking/products/software/doca/). - Start programming BlueField:
[download NVIDIA DOCA](https://developer.nvidia.com/doca-downloads), follow the[DOCA getting-started guide](https://developer.nvidia.com/networking/doca/getting-started), and build the DOCA samples.

## Start the discussion at forums.developer.nvidia.com
