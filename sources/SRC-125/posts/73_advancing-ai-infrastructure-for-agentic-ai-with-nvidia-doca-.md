# advancing-ai-infrastructure-for-agentic-ai-with-nvidia-doca-in-silicon-security

source: https://developer.nvidia.com/blog/advancing-ai-infrastructure-for-agentic-ai-with-nvidia-doca-in-silicon-security/

The AI era is driving a new class of infrastructure: [AI factories](https://www.nvidia.com/en-us/glossary/ai-factory/) that transform data into intelligence for [autonomous AI agents](https://www.nvidia.com/en-us/glossary/ai-agents/) operating at unprecedented scale. Powered by accelerated computing, AI factories enable enterprises to train, fine-tune, and deploy AI with greater speed and efficiency.

This new class of infrastructure also introduces a fundamentally new attack surface spanning infrastructure, software supply chains, models, data, and autonomous agents with increasing authority to act. As agentic AI adoption accelerates, adversaries are increasingly targeting both AI infrastructure and the applications it powers, creating new risks to the confidentiality, integrity, and availability of mission-critical systems.

Traditional security architectures were not designed for the scale, complexity, and performance demands of AI factories. Securing this new infrastructure requires security that is distributed, full-stack, and accelerated.

This post explains how [NVIDIA BlueField data processing units (DPUs)](https://www.nvidia.com/en-us/networking/products/data-processing-unit/) and [NVIDIA DOCA](https://www.nvidia.com/en-us/networking/products/software/doca) secure AI factories through runtime detection, data access control, and accelerated network enforcement to protect AI infrastructure, workloads, agents, and data at AI scale.

## How does in-silicon security change the traditional security model?

Purpose-built for AI infrastructure, NVIDIA BlueField DPUs combine high-performance networking, programmable compute, hardware acceleration, and advanced security capabilities into a single platform embedded into every AI factory compute node. Unlike traditional security approaches that rely on host system software, BlueField establishes a hardware-enforced, in-silicon, and workload-independent security layer.

Operating within its own trusted execution domain, BlueField isolates infrastructure and security services from the host system. Monitoring, policy enforcement, and telemetry operate even if the host or workloads become compromised. Because security functions remain isolated from the system they protect, attackers cannot tamper with or bypass BlueField-enforced infrastructure security policies.

This architecture fundamentally changes the traditional security model. Conventional endpoint protection shares the same trust boundaries and system resources as the environments it secures, making security software vulnerable to tampering, evasion, or disablement when a host is compromised. By offloading security processing to the BlueField silicon, it delivers resilient, full-stack protection without consuming host computing resources or competing with AI workloads—preserving peak infrastructure efficiency and AI performance.

## How NVIDIA BlueField and DOCA protect the entire AI factory

With the [NVIDIA Vera Rubin platform](https://www.nvidia.com/en-us/data-center/technologies/rubin/), security becomes distributed across the entire AI factory and built directly into the infrastructure layer. NVIDIA BlueField-4 processors are embedded in every compute and storage system—including [NVIDIA Vera Rubin NVL72](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/) compute trays, Vera CPU compute trays, LPX systems, and [Vera BlueField-4 STX storage systems](https://nvidianews.nvidia.com/news/nvidia-vera-bluefield-4-stx-brings-agentic-ai-storage-processing-with-in-silicon-security). This establishes a consistent, hardware-enforced security foundation across the platform.

Built on BlueField-4 silicon, a new class of [NVIDIA DOCA](https://developer.nvidia.com/networking/doca) security capabilities extends protection across the full AI lifecycle and the Vera Rubin platform. Whether safeguarding AI models, context memory, datasets, or runtime interactions, BlueField secures any data type, any workload, and any agent. This includes protecting autonomous agents themselves—and defending the AI factory from increasingly privileged agents operating across inference, training, and emerging agentic AI workflows.

The NVIDIA DOCA security stack provides a unified framework for protecting the entire AI factory. Leveraging BlueField-4 acceleration, DOCA enables runtime threat detection up to 1,000x faster than software-only agentless approaches, while enforcing network and file access policies at speeds up to 800 Gb/s. This enables security to operate at AI speed and scale.

The DOCA security stack includes [DOCA Argus](https://docs.nvidia.com/doca/sdk/doca-argus-service-guide/index.html), DOCA Vault, and [DOCA Flow](https://docs.nvidia.com/doca/sdk/doca-flow/index.html) which provide specialized capabilities spanning runtime threat detection, zero-trust access for file-based storage, and high-speed policy network enforcement. Together, these frameworks establish a robust security architecture for protecting AI infrastructure, workloads, agents, and data across the AI factory.

Integrated with NVIDIA AI, BlueField streams telemetry and security data to GPU-accelerated systems for AI-powered analysis, generating actionable security intelligence that can dynamically adapt protections and enforce policies directly on the DPU. The result is a continuously learning security architecture built for the speed, scale, and complexity of agentic AI.

## How does DOCA Argus detect threats in AI workloads?

[DOCA Argus](https://docs.nvidia.com/doca/sdk/doca-argus-service-guide/index.html) is the runtime threat detection microservice that provides real-time visibility and situational awareness across the AI factory. Argus is the foundation of the DOCA security stack.

Running on BlueField data and storage processors, DOCA Argus continuously observes workload behavior at runtime using advanced memory analysis, enabling organizations to detect threats, monitor integrity, and understand operational state without impacting AI workload performance.

Unlike traditional host-based security approaches, DOCA Argus operates independently from the compute node it protects. By leveraging the BlueField hardware-isolated and attestable execution environment and DOCA direct memory access capabilities, Argus securely accesses specific snippets of volatile host memory—the authoritative source of truth for system activity—without relying on software agents or consuming host CPU resources. Through zero-copy memory access techniques, this inspection occurs without disrupting application or AI performance.

DOCA Argus automatically identifies the Linux kernel version running on the host system and applies kernel-specific memory maps to locate the precise memory structures required for analysis. Supporting both x86 and Arm64 architectures, the platform collects low-level telemetry directly from host memory structures and translates raw memory data into meaningful operational context, including visibility into processes, threads, execution states, workload activity, and system behavior.

A policy engine continuously analyzes collected telemetry to identify meaningful operational and security signals while filtering irrelevant activity. This enables real-time visibility into system behavior, indicators of attack, and anomalous runtime conditions. Security findings are categorized into events, which provide operational awareness and contextual visibility, and alerts, which indicate immediate threats or suspicious behavior requiring investigation or response.

By continuously analyzing memory for state changes and behavioral anomalies, DOCA Argus provides persistent runtime monitoring without relying on traditional host-based agents. Because security controls operate independently from the host, detection capabilities remain intact even if workloads or the operating system become compromised. At the same time, the continued collection of forensics evidence enables investigation of potential incidents and supports post-incident analysis.

### Runtime integrity monitoring for AI

AI applications are commonly deployed as containers, where workloads instantiated from the same image are expected to exhibit consistent and predictable behavior. DOCA Argus leverages this consistency to establish behavioral profiles for AI workloads, enabling real-time monitoring for deviations that may indicate compromise, unauthorized activity, or malicious behavior.

DOCA Argus continuously validates runtime integrity by monitoring what is executing, how it is executing, and what it’s interacting with at runtime. This includes comparing the behavior and properties of binaries against expected runtime manifests, validating integrity through SHA-256 hashes, analyzing execution context such as command-line arguments and execution paths, and monitoring interactions with threads, libraries, the file system, network, and memory to verify workloads are operating as intended.

The platform provides process-level visibility into file access and network activity, continuously monitoring which files are accessed, by which processes, and what actions are performed. Inbound and outbound network connections are analyzed to ensure workloads maintain expected communication patterns and do not exhibit suspicious behavior.

By comparing live runtime activity against established behavioral baselines, DOCA Argus can identify integrity violations and indicators of compromise in real time. Detection capabilities include, for example, unauthorized process execution, unauthorized library usage, drift detection, bash shell execution, reverse shell activity, and other runtime anomalies associated with compromise or malicious behavior.

### AI discovery and exposure management

DOCA Argus also provides a foundational visibility layer for AI discovery and exposure management across the AI factory. The platform continuously identifies, maps, and contextualizes AI infrastructure, workloads, and their relationships in real time.

This includes workload posture awareness across containers (including Kata containers), virtual machines, and bare-metal systems, as well as mapping relationships between infrastructure components such as container-to-POD, container-to-VM, and container-to-operating-system dependencies.

Using container image hashes, DOCA Argus can help identify deployed AI software, models, and autonomous agents by correlating runtime artifacts against publicly available repositories and internal enterprise software inventories. Leveraging DOCA Argus telemetry, organizations gain visibility into which AI components are running, where they are deployed, and how they interact across the environment.

DOCA Argus can also support passive vulnerability management by analyzing the SHA-256 hashes of executed binaries and loaded libraries to help identify potentially vulnerable software components.

### Integration of AI processing into cybersecurity operations

DOCA Argus integrates seamlessly with existing cybersecurity ecosystems through standard telemetry export mechanisms, including Fluent Bit and Vector, enabling organizations to stream security telemetry into SIEM, SOAR, XDR platforms, and enterprise data lakes for enrichment and analysis.

Cybersecurity teams can extend existing analytics, correlation engines, threat intelligence, and automated incident response workflows into AI environments seamlessly, without requiring major architectural changes. Cybersecurity providers can ingest and normalize DOCA Argus telemetry alongside data from their own sensors, enabling AI workloads and accelerated infrastructure to be monitored through the same operational lens as traditional environments for threat detection and investigation.

Importantly, DOCA Argus preserves privacy by restricting extracted telemetry to operational and security-relevant information without exposing personally identifiable information (PII).

Running on a single BlueField processor, DOCA Argus can provide comprehensive runtime monitoring and threat detection for an entire compute node, delivering infrastructure-level visibility and protection with minimal operational overhead. Combined with BlueField in-silicon security architecture, DOCA Argus enables enterprises and cloud AI factory builders to secure any workload at scale without sacrificing performance, efficiency, or AI throughput.

## How does DOCA Vault enable real-time data access control?

DOCA Vault is a data security framework purpose-built for file-based, AI-native storage, enabling real-time control over how data is accessed across the AI factory. DOCA Vault enforces granular authorization policies directly in silicon, independent of the host operating system and storage platform.

This enables a zero-trust access layer for file-based storage, ensuring that only authorized AI workload processes—including agents, training jobs, inference services, and AI applications—can access the specific data required for operation and only with explicitly permitted actions.

Unlike traditional access controls that rely on the host system for enforcement, DOCA Vault operates inline with storage access requests, maintaining policy enforcement even if the host operating system, applications, or storage layer become compromised. This architecture enables enterprises to securely scale multi-agent AI environments while preserving consistent security controls across heterogeneous storage infrastructure.

DOCA Vault is integrated with DOCA Argus and DOCA SNAP (through the DOCA Device Emulation SDK), to provide the visibility and enforcement required for secure, policy-driven storage access. DOCA SNAP presents networked storage as local file system devices to the host system by emulating local drives on the PCIe bus. As a result, operating systems and hypervisors continue using standard storage drivers without awareness that requests are being transparently redirected through a BlueField-accelerated storage framework.

This architecture allows file access requests to be intercepted and evaluated before data access occurs. DOCA Vault enriches storage requests with contextual telemetry gathered from DOCA Argus, creating a detailed understanding of the process initiating the request, the targeted file, and the requested action, such as OPEN, READ, or WRITE. These contextual signals allow DOCA Vault to enforce highly granular authorization policies that ensure only the right workload processes access the right files with the appropriate permissions.

DOCA Vault also extends protection beyond traditional authorization by enforcing runtime integrity controls for AI workloads and storage environments. Fine-grained policies can restrict which programs are allowed to execute, prevent unauthorized file creation, limit runtime drift, and block unauthorized model or data exfiltration. By tightly governing file access behavior, Vault significantly reduces the actions an attacker can perform after gaining initial access to a workload or container.

In multiagent AI systems, where agents increasingly access shared datasets, memory, and models autonomously, this level of control becomes especially important. Unauthorized or unexpected file activity is blocked in real time and can serve as a strong indicator of compromise, helping organizations detect malicious behavior before it propagates across the AI factory.

DOCA Vault embeds storage security directly into the infrastructure layer, enabling enterprises to protect sensitive datasets, AI models, context memory, and intellectual property without sacrificing performance. Running inline on BlueField-4, Vault delivers real-time authorization and protection while preserving maximum AI throughput and application efficiency.

## How does DOCA Flow accelerate advanced security services?

[DOCA Flow](https://docs.nvidia.com/doca/sdk/doca-flow/index.html) is a foundational library within the DOCA software platform that enables developers and cybersecurity providers to create high-performance, hardware-accelerated packet processing pipelines on BlueField processors. Through a programmable API, developers can define packet processing “pipes” that execute directly in networking hardware, offloading networking and security operations from the host CPU while maintaining ultra-low latency and high throughput.

By executing packet inspection, encryption, filtering, and policy enforcement directly in silicon, DOCA Flow enables network security to operate at AI speed and scale without impacting application or AI workload performance.

One of the core uses of DOCA Flow is programming BlueField processors to function as high-performance Layer 4 firewalls with built-in connection tracking, enabling granular control over front-end and back-end traffic across the AI factory. This enables organizations to enforce network segmentation, isolate workloads, and prevent unauthorized communication paths in real time—including for encrypted traffic.

DOCA Flow enables cybersecurity providers to accelerate advanced security services directly on BlueField. This includes Layer 7 firewalls, AI security gateways, application-aware inspection, and policy enforcement services purpose-built for accelerated infrastructure and agentic AI environments.

As AI factories scale to support increasingly distributed and autonomous workloads, network communication becomes a critical attack surface. DOCA Flow enables security policies to be enforced directly within the infrastructure layer, preventing threats from propagating laterally across systems while maintaining the line-speed performance and the efficiency required for large-scale AI training and inference.

## Get started with NVIDIA DOCA for agentic AI factory security

While each component of the [NVIDIA DOCA](https://www.nvidia.com/en-us/networking/products/software/doca) security stack delivers powerful security capabilities independently, together DOCA Argus, DOCA Vault, and DOCA Flow establish a unified, in-silicon security framework for protecting the entire AI factory and agentic AI lifecycle. Combining runtime visibility, zero-trust data protection, and accelerated network enforcement, the stack enables end-to-end security for AI infrastructure, workloads, agents, and data without compromising performance or scalability.

Built to operate together on NVIDIA BlueField processors, these interoperable services share telemetry, policy context, and enforcement capabilities to provide coordinated protection across infrastructure, workloads, data, and network communications.

The result is a secure-by-design architecture for agentic AI: one that continuously verifies trust, enforces policy at infrastructure speed, and protects AI factories at the scale and performance demanded by modern accelerated computing. To learn more, see [Build Secure AI Infrastructure with DOCA](https://resources.nvidia.com/en-us-accelerated-networking-resource-library/gtc26-s81625) and dive deeper into [NVIDIA DOCA and accelerated infrastructure](https://www.nvidia.com/en-us/on-demand/playlist/playList-554e5a6e-b50e-420b-92b4-88d44faef328/).

Join NVIDIA founder and CEO Jensen Huang for the [NVIDIA GTC Taipei 2026 Keynote](https://www.nvidia.com/en-tw/gtc/taipei/keynote/?nvid=nv-int-bnr-823296) to learn more about the future of AI infrastructure.

## Start the discussion at forums.developer.nvidia.com
