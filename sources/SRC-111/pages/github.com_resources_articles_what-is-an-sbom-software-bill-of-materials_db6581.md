source: https://github.com/resources/articles/what-is-an-sbom-software-bill-of-materials

# What is a software bill of materials (SBOM)?

Software is built in layers. An SBOM shows what’s inside—so you can secure it.

It’s hard to secure what you can’t see. Most applications rely on open-source libraries, vendor packages, and hidden dependencies—sometimes hundreds of them. A software bill of materials (SBOM) lists every component in your code so you can see what it’s built from and keep it more secure.

A good SBOM can tell you the:

**Component name:**log4j, openssl.**Version used:**log4j 2.14.1.**Supplier name:**Who created it, like the Apache Software Foundation.**License type:**MIT, Apache 2.0.**Dependency relationships:**How components rely on one another.**Unique identifiers:**Elements such as SWID tags or Package URLs (purl).

These details are structured using open standards like SPDX, CycloneDX, or SWID to keep them machine-readable and easy to integrate with security tools.

**Why SBOMs matter**

Recent high-profile security incidents (such as SolarWinds and Codecov) have exposed just how risky hidden dependencies can be. One vulnerable library deep in your stack can open the door to attackers. With an SBOM, team can:

Scan for vulnerabilities against known threat databases.

Verify license compliance and assess risk.

Respond quickly when new threats emerge.

Document audit trails for regulatory requirements.

Analyze supply chain risk and vendor assessments.


It’s easy to see why SBOMs are gaining traction across industries. Even governments are taking action to strengthen [supply chain security](https://github.com/resources/articles/what-is-software-supply-chain-security). In the United States, Executive Order 14028—issued in May 2021—set the stage for requiring SBOMs in software sold to federal agencies. It’s now considered a key part of the country’s national cybersecurity strategy.

## How it works

Creating and using an SBOM involves three key stages that work together to give you complete visibility into your software supply chain.

**Component Discovery**

During the build or packaging process, tools scan your codebase to identify:

Open-source libraries and frameworks.

Third-party packages and modules.

Internal proprietary components.

Transitive (indirect) dependencies.

Container base images and layers.


**Metadata Collection**

Once components are discovered, the system gathers detailed information to catalog:

Version numbers and release dates.

License types and obligations.

Known vulnerabilities (CVE identifiers).

Digital signatures and checksums.

Supplier and maintainer information.


**SBOM Generation**

The collected data gets structured into a standardized format (such as SPDX or CycloneDX) to create:

Documents with hierarchical dependency relationships.

Timestamps and generation tool information.

Export options for JSON, XML, or YAML formats.


## The SBOM lifecycle

An SBOM has its own lifecycle that runs alongside your software development process. Each time your code changes, the SBOM needs to accurately and consistently reflect those changes. Here’s how that typically works:

Create the SBOM during the build process using tools like Syft, Trivy, or FOSSA.

Validate the SBOM for completeness and accuracy to avoid gaps or outdated entries.

Distribute the SBOM as needed, internally across teams or externally to customers, auditors, or regulators.

Update the SBOM regularly to match changes in your codebase, libraries, or dependencies.


**SBOMs in your day-to-day development**

SBOMs work best when built into your workflow. In a [cloud-native](https://github.com/resources/articles/what-is-cloud-native) or [DevSecOps](https://github.com/resources/articles/what-is-devsecops) environment, SBOM tools automatically:

Generate SBOMs during CI/CD builds.

Feed vulnerability data to scanners.

Block risky components before they reach production (an important aspect of

[security testing](https://github.com/resources/articles/what-is-shift-left-testing)).Update security baselines with every code change.

Trigger alerts when new vulnerabilities affect your stack.


All this makes it easier to build in security as you go—without slowing anything down.

## SBOM formats and standards

For an SBOM to be useful, it needs a shared language. That’s where formats come in. Standardized, machine-readable formats make SBOMs easy to generate, share, and use across tools, teams, and organizations. Without them, automation breaks down and interoperability becomes a challenge.

**Common SBOM formats**

Three open standards are widely used today. Each one was designed with different goals in mind, and each one brings something unique to the table.

**Software Package Data Exchange (SPDX)**

**Developed by:**Linux Foundation**Format type:**Tag-value, JSON, YAML, RDF/XML**Recognized**as an international standard: ISO/IEC 5962:2021**Best for:**License auditing, open-source compliance, due diligence**Example:**Describes a package like*libpng*with its version (1.6.37), license (zlib/libpng), and checksum.

**CycloneDX**

**Developed by:**OWASP Foundation**Format type:**JSON, XML, Protocol Buffers**Best for:**Security-focused SBOMs, DevSecOps pipelines, vulnerability management**Example:**Tracks a component like*log4j-core*, its known vulnerabilities (CVEs), and how it connects to other packages.

CycloneDX includes fields for component pedigree, dependency graphs, and security metadata. It works well with tools like OWASP Dependency-Track, Jenkins, and GitHub Actions.

**Software Identification Tags (SWID)**

**Developed by:**ISO/IEC (Standard 19770-2)**Format type:**XML**Best for:**IT asset management, inventory tracking, enterprise environments**Example:**An SWID tag can identify installed components like Microsoft Office for license validation or audits.

SWID is most common in enterprise IT and government contracting. It’s supported by several inventory and asset tools.

**Why standardization matters**

Standardized SBOM formats make it easier to:

Feed security scanners with consistent data.

Compare software inventories across vendors.

Share metadata with auditors, customers, or regulators.


For example, SPDX could be used with FOSSA to check license compliance, while CycloneDX might feed into Dependency-Track to scan for known vulnerabilities, all from the same codebase.

The National Telecommunications and Information Administration (NTIA) recommends SPDX, CycloneDX, and SWID as baseline formats. That guidance is already shaping how governments and enterprises approach SBOM strategy.

**How SBOM formats stack up**

|
|
|
|
| Licensing, open-source compliance | Security, vulnerability | Inventory, asset management |
| Tag-value, JSON, YAML | JSON, XML, Protobuf | XML |
| Linux Foundation | OWASP | ISO |
| ISO/IEC 5962:2021 | NIST SP 800-218, OWASP | ISO/IEC 19770-2 |
| Open source and audits | DevSecOps and CI/CD | IT asset discovery |

Most teams don’t pick just one. They choose the combination of formats that work for their audience, toolchain, and reporting needs.

## Benefits and challenges of SBOMs

Software systems today are layered, fast-changing, and built from countless moving parts. An SBOM helps you see underlying components in your code, manage risk, and stay compliant. But adoption takes planning—and clearing a few common hurdles.

**Key benefits**

**Stronger security and faster response**

*For security teams. *SBOMs make it easier to spot and fix vulnerabilities. When the Log4Shell vulnerability was disclosed, teams with current SBOMs could find affected Log4j versions fast, while others were left searching through source files and deployment logs.

**Simpler regulatory compliance**

*For compliance teams and legal. *SBOMs support growing regulatory and procurement requirements. In the U.S., software accountability is becoming a condition for doing business. International standards are following suit.

**Faster incident response**

*For security and operations. *Security teams use SBOMs to cross-reference known vulnerabilities. Some integrate with tools like Microsoft Sentinel or Splunk to flag issues in real time and support [security posture management](https://github.com/resources/articles/application-security-posture-management).

**More trust and accountability**

*For leadership and external stakeholders. *Sharing SBOMs with customers and partners shows your commitment to secure, traceable software, especially in regulated sectors.

**Smarter maintenance**

*For developers and engineering leads. *SBOMs highlight outdated or unmaintained components, making it easier to plan upgrades and reduce technical debt.

**Common challenges in implementing SBOMs**

Even with the right intentions, teams often hit roadblocks with:

**Scaling across teams.**Manual SBOMs don’t scale. Tools help, but coverage can be uneven.**CI/CD complexity.**Integrating SBOMs into build pipelines takes time and coordination.**Format inconsistency.**Without a shared standard, SBOMs vary in depth and detail.**Training gaps.**Some teams lack experience with SBOM tools and formats.

## Getting started

To avoid common pitfalls and get value from SBOMs sooner:

**Begin with one app or service.**Use it to test your tools and approach.**Match tools to your stack.**Use Syft and Trivy for containers, FOSSA for scanning, SPDX or CycloneDX based on your goals.**Automate the process into your CI/CD pipeline.**Tools like GitHub Actions or Jenkins can generate SBOMs with each build.**Get everyone aligned.**Share the why—not just the how—with dev, security, and compliance teams.

**SBOM implementation: A step-by-step guide**

Putting a software bill of materials in place means building transparency into your development lifecycle—early, consistently, and across teams. Here’s a practical guide to help you get started and make it stick.

**1. Assess your current environment.**

Take stock of your software landscape:

What do you build or buy?

Which languages, frameworks, or deployment models do you use?

What open-source or third-party components are in play?


*Example:* A financial firm using Java libraries with Dockerized apps might start with tools like Syft or Trivy.

**2. Define your objectives.**

Know why you're creating SBOMs:

**Security:**Catch vulnerabilities earlier in the development process.**Compliance:**Support audits and meet regulatory requirements.**Openness:**Share component details with customers, partners, or internal teams.

*Tip:* Pilot with a single app or high-risk product before scaling.

**3. Choose your format.**

Match your format to your goal:

|
|
Security | CycloneDX |
Open-source compliance | SPDX |
Inventory | SWID |

*Example:* Use CycloneDX for CI integration, and SPDX for contract reviews.

**4. Pick the right tools.**

Look for tools that match your stack:

**Syft or Trivy**for containers and images.**FOSSA, or Anchore**for scanning and policy enforcement.**CycloneDX CLI, SPDX tools, or ORAS**for format-specific use.

*Tip:* Automate with GitHub Actions, Jenkins, or similar.

**5. Generate and validate.**

Create your first SBOMs and make sure:

All components (including transitive ones) are included.

The format is correct and complete.


*Example:*

`syft dir:/my-app --output cyclonedx-json > sbom.json`


**6. Store and share securely.**

Decide where and how to store your SBOMs:

In version control.

With release artifacts or in a registry.

Through secure APIs or SBOM portals.


*Tip:* Use access controls and audit trails when sharing externally.

**7. Monitor and update.**

Keep SBOMs current:

With every build or deployment.

When dependencies change.

When new CVEs are published.


*Example:* GitHub Dependabot links CVEs to SBOM components automatically.

**8. Train and govern.**

Get buy-in across roles:

Educate developers.

Involve legal and compliance teams.

Create clear policies for ownership and review.


*Tip:* Use an internal checklist to stay consistent.

Once your SBOM workflow is in place, the payoff is continuous: faster audits, fewer surprises, and a more resilient development process.

## SBOMs and software security

Securing the software supply chain is now a top priority, and a growing focus of [application security](https://github.com/resources/articles/what-is-application-security). Most applications are built from a mix of third-party and open-source components, making it harder than ever to understand their makeup—and whether they’re secure. A software bill of materials helps by making every component visible, traceable, and easier to secure.

**Making the supply chain visible**

SBOMs map out your software components, including deeply nested libraries. That insight helps security teams find and fix vulnerabilities faster.

*Example:* When the 2024 XZ Utils backdoor came to light, teams with SBOMs knew exactly where to look. Others had to piece things together from scratch.

An SBOM turns a black box into a known quantity. That makes it harder for outdated or unknown components to become attack vectors.

**Connecting to vulnerability management tools**

SBOMs become even more powerful when they’re part of your security workflow. Many tools can scan SBOMs against known vulnerabilities, making them a critical part of [vulnerability scanning](https://github.com/resources/articles/what-is-vulnerability-scanning) workflows:

**OWASP Dependency-Track**checks SBOMs against NVD and OSV databases.**Anchore Enterprise**maps components to policies and threat intel.**GitHub Dependabot**flags vulnerable dependencies and suggest fixes.**Microsoft Defender for DevOps**uses SBOM data to detect risks in GitHub and Azure pipelines.

*Workflow example:*

SBOM is generated during the CI build using Syft or Trivy.

It’s exported in CycloneDX format.

The SBOM is scanned by Dependency-Track.

Security alerts are triggered, and remediation tickets are created.


This tight feedback loop improves both detection and response times.

**Supporting shift-left security**

Integrating SBOMs early in development helps teams catch issues before release. SBOMs help:

Developers choose secure libraries.

Security teams flag risks in real time.

Compliance teams verify content before audit.


*Example:* A team reviewing a new open-source library finds active CVEs and chooses an alternative to avoid future risk.

**Defending against supply chain attacks**

SBOMs also help detect tampered or malicious components before they slip through. These components might be introduced with the following techniques:

**Typosquatting**tricks developers with packages that have lookalike names.**Dependency confusion**swaps internal packages for public ones with the same name.**Trojanized updates**slip harmful code into software that appears safe and familiar.

*Reference:* In the SolarWinds attack, compromised builds introduced malware into signed updates. SBOMs could have flagged the changes earlier by showing unexpected components.

**Showing your work**

Sharing SBOMs helps build confidence:

**Regulators**see proof of responsible supply chain management.**Customers**gain a clearer view of what they’re running.

More agencies and industries are starting to require SBOMs in procurement, especially for high-risk systems.

## Cloud-native applications and SBOMs

Cloud-native architectures, which rely on containers, microservices, and continuous delivery pipelines, are becoming the norm for modern development. As systems grow more complex, it becomes more important to know exactly which components are in play. Traditional static SBOMs often fall short. Modern strategies must account for how ephemeral, layered, and distributed these systems really are.

**How cloud-native architectures are reshaping SBOM needs**

Technologies like Docker, Kubernetes, and serverless platforms break applications into small, independently deployable pieces. These services depend on:

Container images that bundle runtimes, system libraries, and app code.

Packages installed by tools like npm, pip, or Maven.

Base images pulled from public registries such as Alpine Linux or Ubuntu.


*Example:* A single Kubernetes pod might run a Python API container built on Alpine Linux, which includes dozens of underlying packages. Without an SBOM, it’s hard to know what it’s made of or what might be vulnerable.

SBOMs cut through this complexity by cataloging components across every layer.

**Why SBOMs must be dynamic and layered**

Cloud-native apps are:

**Mutable:**rebuilt and redeployed often.**Distributed:**spread across nodes and APIs.**Layered:**built on base images, middleware, and runtime components.

To keep pace, SBOMs must:

Track all container layers, including inherited images.

Separate build-time from runtime dependencies.

Update automatically with every build or deployment.


*Best practice:* Generate SBOMs at build time and store them alongside container images in OCI registries for traceability.

**Tools and practices for cloud-native SBOMs**

**Syft**scans containers and code and integrates with GitHub Actions.**Trivy**combines vulnerability scanning with SBOM generation across image layers.**Tern**performs a deep inspection of Debian-based containers.**GitHub sbom-action**adds SBOMs to build artifacts generated in GitHub Actions.**Kubernetes annotations**are an emerging way to link SBOMs to pods and manifests.

**What’s next**

In DevSecOps workflows, SBOMs are expected to be:

Auto-generated at build.

Embedded in OCI metadata.

Continuously scanned and policy-aware.


*Future direction:* OpenSSF is developing standards to embed SBOMs into container registries and enforce supply chain policies.

## SBOM tools and use cases

Supply chain threats are growing, and organizations are responding by adopting software bills of materials (SBOMs) to improve visibility, strengthen regulatory compliance, and reduce risk. SBOMs are now a standard part of secure development in regulated industries and modern software environments.

**How different industries use SBOMs**

**Healthcare: Philips and the FDA** Medical device makers like Philips use SBOMs to meet cybersecurity expectations set by the FDA.

*Example:* Philips includes SBOMs in its update systems to identify affected devices when vulnerabilities are disclosed, which helps speed up response and secure delivery.

**Financial services: JPMorgan Chase** JPMorgan Chase ingests and consumes SBOMs to track open-source dependencies across its CI/CD pipelines.

*Best practice:* Integrate [software composition analysis](https://github.com/resources/articles/what-is-software-composition-analysis) into early build stages to spot outdated packages before release.

**Government: Department of Homeland Security** The department, through the Cybersecurity and Infrastructure Security Agency (CISA), is helping define how SBOMs are used to strengthen how public agencies secure software development and delivery. Pilot programs have tested how agencies generate, validate, and share SBOMs as part of procurement and vulnerability management.

*Example:* CISA’s SBOM Sharing Lifecycle Report outlines how federal teams can act on SBOM data to detect risks and improve response.

**Technology: GitHub, Google, and Microsoft** Tech companies are leading the way on SBOM tooling.

*Tool highlight:* GitHub’s sbom-action auto-generates SPDX or CycloneDX SBOMs in GitHub Actions, making it easier to track dependencies and flag issues in pull requests.

## Lessons from early adopters

**Start small.**Pilot SBOMs on one app or service before expanding.**Automate early.**Manual SBOMs get stale fast. Use tools like Syft, Trivy, or GitHub Actions to keep builds current.**Make them usable.**Connect SBOMs to scanners, dashboards, and regulatory compliance workflows.**Standardize.**Use formats like SPDX or CycloneDX to reduce friction and improve interoperability.

**GitHub’s role in SBOM adoption**

GitHub makes it easier to generate and use SBOMs with built-in tools and integrations:

Use the sbom-action in GitHub Actions to create SPDX or CycloneDX SBOMs as part of your workflow.

Add SBOMs to packages and containers during the build process to improve traceability.

Flag vulnerabilities via integration with Dependabot and the dependency graph.

Work seamlessly with tools like Syft, Trivy, and OSV.


*Example:* A Node.js app built in GitHub Actions generates an SBOM during CI and includes it in the release to show exactly what is deployed.

SBOMs have moved from best practice to baseline for building secure, trusted software.

## Explore other resources

## Frequently asked questions

### What is an SBOM in security?


In security, a software bill of materials (SBOM) is a detailed list of all components used in a software application, including open-source libraries, third-party packages, and dependencies. It helps security teams identify, assess, and respond to vulnerabilities by showing exactly what’s in the software and where potential risks may lie. SBOMs are a key part of modern software supply chain security strategies recommended by organizations like CISA and the National Institute of Standards and Technology.

### What is an SBOM in SDLC?


In the software development lifecycle (SDLC), an SBOM is generated and updated throughout the build, test, and deployment stages to track components in your application. It supports secure development by making dependency tracking, license compliance, and vulnerability scanning part of your CI/CD pipeline. SBOMs help teams shift security left by integrating transparency early in the SDLC.

### What is the difference between a BOM and an SBOM?


A BOM (bill of materials) is a broad term that refers to a list of parts or components needed to build a product—like in manufacturing. An SBOM (software bill of materials) is a specific type of BOM that lists the software components in an application. While both serve to improve clarity and traceability, an SBOM is tailored to software security, licensing, and supply chain risk management.

### Who requires an SBOM?


In the U.S., federal agencies and their vendors are required to provide SBOMs for software procurement. Other regulatory bodies, including the U.S. Food and Drug Administration, the International Organization for Standardization, and the European Union, are also introducing SBOM requirements in sectors such as healthcare, defense, and critical infrastructure.

### What are the popular SBOM formats?


The most popular SBOM formats are SPDX (for license tracking), CycloneDX (for security and vulnerability analysis), and SWID (for IT asset management). These formats are widely supported and work well with popular tools.