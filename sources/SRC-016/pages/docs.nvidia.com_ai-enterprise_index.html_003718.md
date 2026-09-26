source: https://docs.nvidia.com/ai-enterprise/index.html

NVIDIA AI Enterprise is a complete software platform for developing, deploying, and managing AI applications across cloud, data center, and edge environments. It delivers AI frameworks, NIM microservices, and SDKs through its Application Layer, and GPU drivers, Kubernetes operators, and cluster management tools through its Infrastructure Layer. Each layer has independent release branches and lifecycles, plus enterprise support backed by SLAs.



## Highlights

**🆕 Infrastructure 8.2 (Production Branch)**- Released August 2026. The latest Production Branch release of NVIDIA AI Enterprise infrastructure software. See the release notes for the full component list and what's new.

[Infra 8.2 Release Notes →](https://docs.nvidia.com/ai-enterprise/release-8/latest/overview/release-notes.html)

**🆕 Infrastructure 7.8 (LTSB)**- Released August 2026. The latest Long-Term Support Branch (LTSB) release, providing extended support for stable production deployments. See the release notes for the full component list and what's new.

[Infra 7.8 Release Notes →](https://docs.nvidia.com/ai-enterprise/release-7/latest/overview/release-notes.html)

NVIDIA AI Enterprise is a composable stack - assemble the Application Development and Infrastructure Management layers based on your use case:

## Where to Go Next

Find the right documentation based on where you are in your journey:

| If you need to… | Go to | Why |
|---|---|---|
Start: Set up your account, install drivers, and run your first workload |
|

**Discover**: Browse the software components included in your license[NVIDIA AI Enterprise Software](https://docs.nvidia.com/ai-enterprise/software/latest/index.html)**Research**: Choose a release branch, review support timelines, and validate version compatibility[NVIDIA AI Enterprise Lifecycle Policy](https://docs.nvidia.com/ai-enterprise/lifecycle/latest/index.html)·[Interactive Lifecycle and Compatibility Explorer](https://docs.nvidia.com/ai-enterprise/lifecycle/latest/infrastructure-software.html#lifecycle-explorer)**Plan**: Design your deployment for bare metal, virtualized, or cloud[Planning & Deployment](https://docs.nvidia.com/ai-enterprise/index.html#nvidiatab-planning-deployment-guides)**Serve**: Deploy models and configure inference and training runtimes[NVIDIA NIM](https://docs.nvidia.com/nim/)·[NVIDIA NeMo](https://docs.nvidia.com/nemo-framework/user-guide/latest/)·[NVIDIA NGC Catalog](https://catalog.ngc.nvidia.com/)**Build**: Develop physical AI and industrial digital twin applications with NVIDIA Omniverse[NVIDIA Omniverse](https://docs.nvidia.com/omniverse/index.html)**Orchestrate**: Deploy and manage GPU, network, and DPU operators in Kubernetes[NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/overview.html)·[NVIDIA Network Operator](https://docs.nvidia.com/networking/software/cloud-orchestration/index.html)·[NVIDIA DOCA Platform Framework (DPF)](https://networking-docs.nvidia.com/dpf/26.4.0)**Schedule**: Manage GPU workloads and resource allocation with NVIDIA Run:ai[NVIDIA Run:ai Self-Hosted](https://run-ai-docs.nvidia.com/self-hosted/)·[NVIDIA Run:ai SaaS](https://run-ai-docs.nvidia.com/saas/)**Support**: Check licensing or open a technical support case[Support](https://docs.nvidia.com/ai-enterprise/index.html#nvidiatab-support)


Start here to onboard, explore, and plan your NVIDIA AI Enterprise deployment.

[Quick Start Guide](https://docs.nvidia.com/ai-enterprise/release-8/latest/getting-started/quick-start-guide.html)

Walks you through the end-to-end onboarding process for NVIDIA AI Enterprise - from receiving your entitlement certificate and registering your NVIDIA Enterprise Account, to accessing the NGC Catalog and installing software components on bare metal, virtualized, or public cloud infrastructure. Includes steps for linking evaluation accounts, generating NGC API keys, and verifying GPU-accelerated containers are operational.

[Browse ›](https://docs.nvidia.com/ai-enterprise/release-8/latest/getting-started/quick-start-guide.html)

[NVIDIA AI Enterprise Software](https://docs.nvidia.com/ai-enterprise/software/latest/index.html)

Catalogs the Application Layer and Infrastructure Layer components included in your NVIDIA AI Enterprise license, linking each to its NGC Catalog entry and product documentation. Explains the two-layer architecture, independent release cadences, and provides infrastructure support matrices for verifying hardware and software compatibility across deployment types.

[Browse ›](https://docs.nvidia.com/ai-enterprise/software/latest/index.html)

[Lifecycle Policy](https://docs.nvidia.com/ai-enterprise/lifecycle/latest/index.html)

Defines the release branch strategy, support timelines, and end-of-life schedule for every NVIDIA AI Enterprise component - from choosing between Feature Branch (FB), Production Branch (PB), and Long-Term Support Branch (LTSB) releases, to validating cross-stack compatibility using the Interactive Lifecycle and Compatibility Explorer. Includes infrastructure stack alignment diagrams, EOL notices with migration paths, and archived branch references.

[Browse ›](https://docs.nvidia.com/ai-enterprise/lifecycle/latest/index.html)



Application software includes AI frameworks, NVIDIA NIMs, domain SDKs, NVIDIA Omniverse, and pre-trained models - all included in your NVIDIA AI Enterprise license. Production Branches (PB) deliver production-ready AI frameworks with 9-month support. Long-Term Support Branches (LTSB) provide 36 months of API stability for highly regulated industries. Refer to the [Lifecycle Policy](https://docs.nvidia.com/ai-enterprise/lifecycle/latest/index.html), including the [Choosing the Right Release Branch](https://docs.nvidia.com/ai-enterprise/lifecycle/latest/choosing-a-branch.html) section, for more information.

For the full list of Application Layer components with NGC Catalog links and version details, refer to the [Application Layer Software](https://docs.nvidia.com/ai-enterprise/software/latest/application-software.html) page.

## Active Release Branches

| Software Branch | Compatible Infra | First Release | Last Release | Planned EOL |
|---|---|---|---|---|
|

[Long-Term Support Branch 2 (LTSB 2)](https://docs.nvidia.com/ai-enterprise/lifecycle/latest/application-software.html#long-term-support-branch-2-ltsb-2)[Omniverse Production Branch (PB 26h1)](https://docs.omniverse.nvidia.com/dev-overview/latest/branches/production.html#production-branch-pb)[Omniverse Production Branch (PB 25h2)](https://docs.omniverse.nvidia.com/dev-overview/latest/branches/production.html#production-branch-december-2025-pb-25h2)### Archived Release Branches

| Software Branch | Compatible Infra | First Release | Last Release | Status |
|---|---|---|---|---|
| Production Branch (PB 25h2) | Infra Release 7 and 8 | October 2025 | June 2026 | End of Support (July 2026) |
| Omniverse Production Branch (PB 25h1) | - | June 2025 | March 2026 | End of Support (April 2026) |
| Production Branch (PB 25h1) | Infra Release 6 and 7 | May 2025 | December 2025 | End of Support (January 2026) |
| Production Branch (PB 24h2) | Infra Release 5 and 6 | October 2024 | June 2025 | End of Life (July 2025) |
| Production Branch (PB 24h1) | Infra Release 4 and 5 | May 2024 | December 2024 | End of Life (January 2025) |
| Production Branch (PB 23h2) | Infra Release 3 | October 2023 | June 2024 | End of Life (July 2024) |
| Long-Term Support Branch 1 (LTSB 1) | Infra Release 1 | August 2021 | February 2024 | End of Life (June 2024) |



Infrastructure software includes GPU drivers, Kubernetes operators (NVIDIA GPU Operator, NVIDIA Network Operator, NVIDIA NIM Operator), NVIDIA Container Toolkit, NVIDIA Run:ai (both self-hosted and SaaS), and cluster management tools - all included in your NVIDIA AI Enterprise license. Infrastructure Branches provide regular updates with 1-year support windows. Branches designated as Long-Term Support (LTSB) receive extended 3-year support. NVIDIA Run:ai SaaS follows a separate, NVIDIA-managed cloud-service lifecycle. Refer to the [Lifecycle Policy](https://docs.nvidia.com/ai-enterprise/lifecycle/latest/index.html), including the [Choosing the Right Release Branch](https://docs.nvidia.com/ai-enterprise/lifecycle/latest/choosing-a-branch.html) section, for more information.

For the full list of Infrastructure Layer components with NGC Catalog links, version details, and the stack alignment diagram, refer to the [Infrastructure Layer Software](https://docs.nvidia.com/ai-enterprise/software/latest/infrastructure-software.html) page.

**Interactive Support Matrix**- Check supported configurations and compatibility across all NVIDIA AI Enterprise infrastructure releases (4.4 through 8.2) - filter by deployment type, OS, hypervisor, orchestration platform, GPU architecture, Kubernetes distribution, or cloud provider. →

[Infrastructure Support Matrix](https://docs.nvidia.com/ai-enterprise/support-matrix/latest/index.html)

**Interactive Lifecycle and Compatibility Explorer**- Validate cross-stack compatibility between GPU drivers, NVIDIA GPU Operator, NVIDIA Network Operator, and NVIDIA Run:ai versions before deploying or upgrading. →

[Lifecycle and Compatibility Explorer](https://docs.nvidia.com/ai-enterprise/lifecycle/latest/infrastructure-software.html#lifecycle-explorer)

## Active Release Branches

| Software Branch | Driver | Latest Release | Latest Update | Planned EOL |
|---|---|---|---|---|
|

[NVIDIA AI Enterprise Infra 7](https://docs.nvidia.com/ai-enterprise/release-7/latest/index.html)(LTSB)### Archived Release Branches

| Software Branch | Driver | Last Release | Last Update | EOL Date |
|---|---|---|---|---|
| NVIDIA AI Enterprise Infra 6 (FB, PB) | R570 (570.211.01) | 6.7 | January 2026 | March 2026 |
| NVIDIA AI Enterprise Infra 5 (FB, PB) | R550 (550.144.02) | 5.3 | January 2025 | April 2025 |
| NVIDIA AI Enterprise Infra 4 (LTSB) | R535 (535.309.01) | 4.10 | May 2026 | July 2026 |
| NVIDIA AI Enterprise Infra 3 (FB, PB) | R525 (525.147.05) | 3.3 | November 2023 | December 2023 |
| NVIDIA AI Enterprise Infra 2 (FB) | R520 (520.61.05) | 2.3 | October 2022 | November 2022 |
| NVIDIA AI Enterprise Infra 1 (LTSB) | R470 (470.256.02) | 1.9 | July 2024 | September 2024 |



## Deployment Guides

Step-by-step deployment instructions for installing NVIDIA AI Enterprise on your target infrastructure - whether bare metal, virtualized, cloud, or co-engineered partner platforms. Each guide covers prerequisites, driver and software installation, validation steps, and environment-specific configuration. Select the guide that matches your deployment environment.

[Bare Metal Deployment Guide](https://docs.nvidia.com/ai-enterprise/deployment/bare-metal/latest/overview.html)

Deploy NVIDIA AI Enterprise directly on bare metal servers with step-by-step instructions covering prerequisites, driver installation, licensing, Docker setup, and AI framework configuration. Includes GPU partitioning options, Kubernetes deployment, and GPUDirect Storage setup.

[Browse ›](https://docs.nvidia.com/ai-enterprise/deployment/bare-metal/latest/overview.html)

[VMware vSphere Deployment Guide](https://docs.nvidia.com/ai-enterprise/deployment/vmware/latest/overview.html)

Deploy NVIDIA AI Enterprise on VMware vSphere with end-to-end instructions covering ESXi, vCenter, NVIDIA host software, vGPU configuration, and VM creation. Includes Docker setup, AI framework installation, and a CPU-only deployment path.

[Browse ›](https://docs.nvidia.com/ai-enterprise/deployment/vmware/latest/overview.html)

[Cloud Deployment Guide](https://docs.nvidia.com/ai-enterprise/deployment/cloud/latest/overview.html)

Deploy NVIDIA AI Enterprise in the cloud with instructions for supported CSPs, instance types, and licensing options. Covers standard instances, NVIDIA Virtual Machine Images, managed Kubernetes, and Red Hat OpenShift across AWS, Google Cloud, Azure, Oracle Cloud, and more.

[Browse ›](https://docs.nvidia.com/ai-enterprise/deployment/cloud/latest/overview.html)

[Red Hat AI Factory with NVIDIA](https://docs.nvidia.com/ai-enterprise/deployment/red-hat-ai-factory/latest/overview.html)

Deploy the co-engineered Red Hat AI Factory with NVIDIA solution covering hardware requirements, network configuration, NVIDIA AI Enterprise Software integration, and Red Hat OpenShift AI installation. Includes end-to-end guidance through deploying NVIDIA NIM microservices.

[Browse ›](https://docs.nvidia.com/ai-enterprise/deployment/red-hat-ai-factory/latest/overview.html)

[NVIDIA Omniverse Platform Guide](https://docs.omniverse.nvidia.com/dev-overview/latest/index.html)

Build and deploy 3D applications and services at scale using OpenUSD, RTX rendering, and modular Omniverse SDKs, APIs, and Libraries. Covers platform architecture, development paths, and key use cases including virtual facility integration and synthetic data generation.

[Browse ›](https://docs.omniverse.nvidia.com/dev-overview/latest/index.html)

[NVIDIA Run:ai Self-Hosted Deployment Guide](https://run-ai-docs.nvidia.com/self-hosted/getting-started/installation)

Install the NVIDIA Run:ai self-hosted control plane and cluster components on Kubernetes for GPU orchestration and workload scheduling in on-premises or private cloud environments. Supports both connected and air-gapped deployment types.

[Browse ›](https://run-ai-docs.nvidia.com/self-hosted/getting-started/installation)

[NVIDIA Run:ai SaaS Deployment Guide](https://run-ai-docs.nvidia.com/saas/getting-started/installation/install-using-helm/system-requirements)

Connect your Kubernetes cluster to the NVIDIA-managed Run:ai SaaS control plane for GPU orchestration and workload scheduling. Covers system requirements, cluster installation with Helm, authentication, and onboarding.

[Browse ›](https://run-ai-docs.nvidia.com/saas/getting-started/installation/install-using-helm/system-requirements)

## Reference Architectures

Validated hardware and software blueprints for designing production-grade AI infrastructure before deployment. Use these reference architectures to determine compute node specifications, networking topologies, and software stack configurations for your target workloads and scale requirements.

[NVIDIA Omniverse Reference Architecture Diagrams](https://docs.omniverse.nvidia.com/arch-diagrams/latest/ref-arch-diagrams/factory-dt-diagram.html)

Hardware specifications, GPU configurations, and infrastructure requirements for deploying industrial facility digital twins, physical AI, and autonomous robotics workflows. Covers scalable data center deployments and NVIDIA-Certified Workstations using RTX PRO 6000 Blackwell Series GPUs.

[Browse ›](https://docs.omniverse.nvidia.com/arch-diagrams/latest/ref-arch-diagrams/factory-dt-diagram.html)

## White Papers

Technical white papers covering security, compliance, and architecture guidance for deploying NVIDIA AI Enterprise in government, regulated, and enterprise environments. Use these resources to understand container security practices, VM optimization strategies, and partner integration patterns before finalizing your deployment architecture.

[NVIDIA AI Factory for Government Reference Design](https://docs.nvidia.com/ai-enterprise/planning-resource/ai-factory-reference-design-for-government-white-paper/latest/index.html)

A purpose-built, full-stack architecture that enables federal agencies to deploy secure, scalable AI in mission-critical environments. Integrates NVIDIA accelerated computing, high-performance networking, NVIDIA-Certified Systems, Nemotron models, and government-ready software with a broad partner ecosystem.

[Browse ›](https://docs.nvidia.com/ai-enterprise/planning-resource/ai-factory-reference-design-for-government-white-paper/latest/index.html)

[NVIDIA AI Software for Regulated Environments](https://docs.nvidia.com/ai-enterprise/planning-resource/ai-software-regulated-environments-white-paper/latest/index.html)

A security and compliance framework that introduces a new "Government Ready" baseline for NVIDIA AI Enterprise software, enabling deployment in FedRAMP High and equivalent sovereign environments. Covers hardened containers, distroless images, and Red Hat UBI-STIG images for regulated AI workloads.

[Browse ›](https://docs.nvidia.com/ai-enterprise/planning-resource/ai-software-regulated-environments-white-paper/latest/index.html)

[NVIDIA AI Enterprise Security](https://docs.nvidia.com/ai-enterprise/planning-resource/ai-enterprise-security-white-paper/latest/introduction.html)

A comprehensive overview of the security development lifecycle that protects the NVIDIA AI Enterprise software stack from development through production deployment. Covers container image security, vulnerability scanning, NIM microservice security controls, and continuous monitoring.

[Browse ›](https://docs.nvidia.com/ai-enterprise/planning-resource/ai-enterprise-security-white-paper/latest/introduction.html)

[NVIDIA Enterprise AI Factory Design Guide](https://docs.nvidia.com/ai-enterprise/planning-resource/ai-factory-white-paper/latest/index.html)

A full-stack reference architecture for deploying single-tenant AI solutions from infrastructure provisioning through agentic AI workloads. Covers accelerated computing platforms, high-performance networking, Kubernetes-based deployment, observability, security, and partner integrations.

[Browse ›](https://docs.nvidia.com/ai-enterprise/planning-resource/ai-factory-white-paper/latest/index.html)

[Optimizing VM Configuration for AI Inference](https://docs.nvidia.com/ai-enterprise/planning-resource/optimizing-vm-configuration-ai-inference/latest/introduction.html)

A practitioner's guide for configuring virtual machines on HGX systems to achieve near bare-metal performance for ML training and AI inference. Covers NUMA-aware VM topology, GPU and NIC passthrough, PCIe and NVLink device mapping, and day-2 best practices for RHEL KVM.

[Browse ›](https://docs.nvidia.com/ai-enterprise/planning-resource/optimizing-vm-configuration-ai-inference/latest/introduction.html)

[NVIDIA NIM LLM with Run:ai and Vanilla Kubernetes](https://docs.nvidia.com/enterprise-reference-architectures/nim-llm-runai-vanilla-kubernetes/latest/index.html)

A deployment, scale, and sizing guide for optimizing NVIDIA NIM LLM inference workloads using Run:ai on an Enterprise Reference Architecture. Covers intelligent GPU scheduling, fractional GPU allocation, dynamic scaling, and performance benchmarking for LLM inference services.

[Browse ›](https://docs.nvidia.com/enterprise-reference-architectures/nim-llm-runai-vanilla-kubernetes/latest/index.html)

[NVIDIA AI Enterprise Infrastructure Software](https://docs.nvidia.com/ai-enterprise/planning-resource/ai-enterprise-infrastructure-software/latest/index.html)

A suite of software that enhances traditional Kubernetes environments with hardware acceleration, dynamic GPU orchestration, network optimization, and secure virtualization, transforming data center infrastructure into scalable and efficient Enterprise AI Factories.

[Browse ›](https://docs.nvidia.com/ai-enterprise/planning-resource/ai-enterprise-infrastructure-software/latest/index.html)



NVIDIA AI Enterprise support resources cover enterprise-level support services, product-specific licensing terms, and version lifecycle policies. All NVIDIA AI Enterprise components are covered under the same support services and SLAs.

## Enterprise Support and Services

Access NVIDIA Enterprise Support, including support tiers, response times, escalation processes, and how to open a support case. These resources apply to all NVIDIA AI Enterprise licensed products.

[Enterprise Support and Services](https://docs.nvidia.com/enterprise-services/index.html)

Access support tiers, response-time SLAs, escalation processes, and instructions for opening a technical support case. Covers all NVIDIA AI Enterprise licensed products.

[Browse ›](https://docs.nvidia.com/enterprise-services/index.html)

[Enterprise Services](https://resources.nvidia.com/en-us-enterprise-services/nvaie-datasheet-nvid)

Explore available enterprise service offerings, including onboarding assistance, deployment guidance, and strategic advisory services for NVIDIA AI Enterprise environments.

[Browse ›](https://resources.nvidia.com/en-us-enterprise-services/nvaie-datasheet-nvid)

**Business Standard**- Access to NVIDIA AI experts during local business hours with SLA-backed response times**Business Critical**(add-on) - 24/7 support coverage with accelerated response times for production issues**Technical Account Manager**(add-on) - Dedicated NVIDIA expert for strategic guidance and deployment planning

## Product Support and Licensing

Product-specific licensing agreements, support policies, and version lifecycle timelines for NVIDIA AI Enterprise, NVIDIA Omniverse, and NVIDIA Run:ai. Review these to understand support levels, end-of-support dates, and license terms for individual products.

[Licensing Guide](https://docs.nvidia.com/ai-enterprise/planning-resource/licensing-guide/latest/index.html)

Covers NVIDIA AI Enterprise licensing models, entitlement activation, license server configuration, and subscription management for all deployment types.

[Browse ›](https://docs.nvidia.com/ai-enterprise/planning-resource/licensing-guide/latest/index.html)

[NVIDIA Omniverse Licensing](https://docs.omniverse.nvidia.com/enterprise/latest/common/NVIDIA_Omniverse_License_Agreement.html)

Explains the NVIDIA Software License Agreement and Product-Specific Terms for NVIDIA Omniverse, governing use for both individuals and enterprises.

[Browse ›](https://docs.omniverse.nvidia.com/enterprise/latest/common/NVIDIA_Omniverse_License_Agreement.html)

[NVIDIA Run:ai Self-Hosted Product Support Policy](https://run-ai-docs.nvidia.com/self-hosted/support-policy/product-support-policy)

Explains NVIDIA Run:ai self-hosted product support levels and lifecycle policies, covering full support, extended support, bug fix policies for critical and important issues, and versioning information.

[Browse ›](https://run-ai-docs.nvidia.com/self-hosted/support-policy/product-support-policy)

[NVIDIA Run:ai Self-Hosted Product Version Life Cycle](https://run-ai-docs.nvidia.com/self-hosted/support-policy/product-version-life-cycle)

Outlines the NVIDIA Run:ai self-hosted product version lifecycle, including support phases (Full Support, Extended Support, End of Support), version-specific timelines, and upgrade planning guidance.

[Browse ›](https://run-ai-docs.nvidia.com/self-hosted/support-policy/product-version-life-cycle)

[NVIDIA Run:ai SaaS Product Support Policy](https://run-ai-docs.nvidia.com/saas/support-policy/product-support-policy)

Explains NVIDIA Run:ai SaaS product support levels and lifecycle policies for the NVIDIA-managed cloud service, covering full support, extended support, bug fix policies for critical and important issues, and versioning information.

[Browse ›](https://run-ai-docs.nvidia.com/saas/support-policy/product-support-policy)

[NVIDIA Run:ai SaaS Product Version Life Cycle](https://run-ai-docs.nvidia.com/saas/support-policy/product-version-life-cycle)

Outlines the NVIDIA Run:ai SaaS product version lifecycle, including support phases (Full Support, Extended Support, End of Support), version-specific timelines, and upgrade planning guidance for the NVIDIA-managed cloud service.

[Browse ›](https://run-ai-docs.nvidia.com/saas/support-policy/product-version-life-cycle)