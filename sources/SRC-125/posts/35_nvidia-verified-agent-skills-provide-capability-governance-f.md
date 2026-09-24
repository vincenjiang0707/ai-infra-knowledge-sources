# nvidia-verified-agent-skills-provide-capability-governance-for-ai-agents

source: https://developer.nvidia.com/blog/nvidia-verified-agent-skills-provide-capability-governance-for-ai-agents/

[Autonomous AI agents](https://www.nvidia.com/en-us/glossary/ai-agents/) are becoming more capable. [Open models](https://www.nvidia.com/en-us/glossary/open-models/), [Model Context Protocol (MCP)](https://docs.nvidia.com/nemo/agent-toolkit/1.3/workflows/mcp/index.html)-connected tools, and portable skills are also making agents easier to extend.But scaling agent use with structural transparency and operational integrity requires more than runtime guardrails. Organizations and teams need to understand and trust the skills, or instructions, an agent is using.

[NVIDIA-verified agent skills](https://github.com/NVIDIA/skills) address this gap by helping developers understand capabilities, discover where a skill originated, whether it was scanned for common risks, and whether it was modified after publication. Skill verification matters when skills are reused and deployed in real workflows, rather than treated like individual, opaque bundles.

Verified skills embed transparency, provenance, security validation, and authenticity checks to the agent capability layer, helping developers extend autonomous agents more confidently. Verified means cataloged, scanned, signed, and documented with a [skill card](https://github.com/NVIDIA/Trustworthy-AI/blob/main/Skill%20Card.md). Verified skills build on [agentskills.io](http://agentskills.io) open skills specification, so the same SKILL.md that works in one AI coding agent is designed to work reliably across Claude Code, Codex, and Cursor.

This post explains what NVIDIA agent skills are and how they become verified, how skill cards work, and how you can deploy [agent skills](https://www.nvidia.com/en-us/glossary/agent-skills/) more safely and confidently in your own agent workflows.

## What are NVIDIA agent skills?

NVIDIA agent skills are portable instruction sets that teach AI agents how to use NVIDIA CUDA-X libraries, AI Blueprints, and platform tools correctly. NVIDIA-verified skills published in the [NVIDIA/skills](https://github.com/nvidia/skills/) GitHub repo are:

- Cataloged and synced daily from the NVIDIA product team that owns it
- Scanned for software and agent-native risks before publication
- Signed with a detached skill.oms.sig that can be verified post-download
- Documented with a
[skill card](https://github.com/NVIDIA/Trustworthy-AI/blob/main/Skill%20Card.md)describing ownership, dependencies, limitations, and verification status

Evaluation is the next layer. It will add standardized quality metrics, trigger accuracy, task completion rate, and token efficiency, measured against a common harness as it rolls out.

## How does an agent skill become verified?

An NVIDIA-verified skill starts in a source repository owned by a product team. From there, it moves through a publishing flow that can include both human review and automated policy checks, followed by scanning, evaluation, generation of the skill card, signing, cataloging, and synchronization into the public catalog.

Each verified skill is paired with a skill card, a machine-readable trust record that explains the following:

- What the skill does
- Who built the skill
- How is the skill licensed
- What are the skill dependencies
- What are the known technical limitations, risks, and mitigations of the skill

Over time, evaluation becomes part of the same validation pipeline (Figure 1). This approach preserves the openness and portability of SKILL.md-based skills while embedding the chain-of-trust layers developers can expect. For more details, see the [Skills documentation](https://docs.nvidia.com/skills).

### How do verified skills bring trust to the skill layer?

NVIDIA already embeds trust in agent systems through the [NVIDIA NeMo Guardrails](https://developer.nvidia.com/nemo-guardrails?sortBy=developer_learning_library%2Fsort%2Ffeatured_in.nemo_guardrails%3Adesc%2Ctitle%3Aasc) library, covering control, privacy, and policy-based guardrails. Resources such as [NVIDIA OpenShell](https://github.com/nvidia/openshell) and [NVIDIA NemoClaw](https://github.com/NVIDIA/NemoClaw/) focus on how agents run: sandboxed execution, controlled access to files and networks, and policy enforcement around sensitive actions.

Verified skills extend this AI governance to agent capabilities. Runtime controls help govern agent behavior during execution. Verified skills govern capabilities that enter the workflow and become a common way to extend trust agents across coding tools, registries, and enterprise platforms.

### How does scanning help mitigate risk before skill publication?

Before a verified skill reaches the NVIDIA Skills catalog, NVIDIA runs it through [SkillSpector](https://github.com/nvidia/skillspector) as part of the publication validation pipeline. This approach treats the skill as a deployable agent capability rather than as a static prompt. SkillSpector checks conventional software risks such as vulnerable dependencies, suspicious scripts, dangerous code patterns, credential access, and data exfiltration paths.

SkillSpector also checks agent-specific risks, such as hidden instructions, prompt injection, trigger abuse, excessive agency, tool poisoning, and mismatches between a skill’s declared purpose, requested access, and bundled behavior. The intent layer is important: a skill may look harmless at the file level while steering an agent toward unsafe behavior, requesting broader access than its purpose requires, or describing one task while bundled artifacts enable another.

This process results in a structured review signal that helps NVIDIA block or remediate risky skills prior to publication.

SkillSpector scanning coverage is grounded in recognized AI security governance, including [OWASP guidance for LLM](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/), [agentic AI risks](https://genai.owasp.org/2025/12/09/owasp-genai-security-project-releases-top-10-risks-and-mitigations-for-agentic-ai-security/), and [MITRE ATLAS](https://atlas.mitre.org/pdf-files/MITRE_ATLAS_Fact_Sheet.pdf). The [NVIDIA Skills scanning documentation](https://docs.nvidia.com/skills/scanning-agent-skills/) lists the current coverage and is updated as scan classes and supply-chain checks expand.

### How does cryptographic signing add verifiable provenance for agent skills?

NVIDIA is publicly experimenting with [cryptographic signing](https://docs.nvidia.com/skills/signing-agent-skills/) for agent skills as part of a broader validation roadmap for enterprise-scale deployment. The goal is to make it easier for developers to trust the skills NVIDIA publishes and replicate the same validation and deployment pipeline across environments.

The signature covers every file and subdirectory in the skill directory, giving developers a concrete way to verify that the downloaded skill is authentic and unchanged. This is what distinguishes verified skills from assets that are merely associated with a known publisher or listed in a trusted catalog. Many registries can identify who uploaded an asset; far fewer let developers cryptographically verify the asset itself after download. In the skills ecosystem, trust should come from verifiable integrity and authenticity, not from implied provenance alone.

Certificate retrieval, supported verification tooling, and example verification commands see the signing documentation. For example, you can verify a signed skill locally. To do so, follow these steps:

- Download the NVIDIA Agentic Capabilities root certificate as
[nv-agent-root-cert.pem](https://docs.nvidia.com/skills/signing-agent-skills/) - Install an OpenSSF Model Signing (OMS) verifier, such as
`pip install model-signing`

- Execute the following command to verify the skill signature:

`$ model_signing verify certificate SKILL_DIR \` ` ` `--signature SKILL_DIR\skill.oms.sig \` ` ` `--certificate-chain nv-agent-root-cert.pem \` ` ` `--ignore-unsigned-files` |

## How does a skill card work?

The [skill card template](https://github.com/NVIDIA/Trustworthy-AI/blob/main/Skill%20Card.md) on GitHub explains the schema, how to structure skills and specify data flow, as well as which fields are required versus optional as the spec evolves.

Consider, for example, a developer building a delivery-scheduling agent who wants to know three things before installing the [NVIDIA cuOpt routing skill](https://github.com/NVIDIA/skills/tree/main/skills/cuopt): who authored the skill, what it accesses beyond the cuOpt solver endpoint, and whether the underlying optimizer has been validated against real routing benchmarks. The [cuOpt skill card](https://github.com/NVIDIA/skills/blob/main/skills/cuopt/cuopt-numerical-optimization-api-c/skill-card.md) answers all three questions in a single machine-readable file. The agent loads this file alongside the skill, so no manual auditing per install is required.

### How do skill cards make trust metadata actionable?

The skill card is where trust is centralized. The information in the skill card is useful to both developers and enterprise architects. A developer can review whether a skill is compatible with a target agent, affirm dependencies pre-deployment quickly, and understand how a skill will operate. Furthermore, enterprise teams can review known risks, fail-safe controls, and validation status before allowing broader skill deployment.

At NVIDIA, [Trustworthy AI](https://www.nvidia.com/en-us/ai-trust-center/trustworthy-ai/) begins with transparency, what a skill can do, and how that is communicated to developers for assessment and deployment. To that end, we are also excited to release our skill card template and [skill card generator](https://github.com/NVIDIA/Trustworthy-AI/tree/main/skills/skill-card-generator). All the required fields in the public skill card template can be autonomously generated and human-verified. By making these resources openly available, NVIDIA invites the community to develop transparently for skills, agents, and beyond.

## Get started with NVIDIA-verified agent skills

If you are deploying agents in real environments, trust extends beyond the runtime. You need to know where a capability came from, whether it passed security checks, and whether it was modified after publication. Verified skills help answer those questions in an easily portable way.

To get started with the cuOpt verified skill, for example, follow these steps:

1. Pull the cuOpt verified skill from the catalog:

`git clone github.com/nvidia/skills && cd skills/skills/cuopt` |

2. Verify the signature:

`model_signing verify certificate. --signature skill.oms.sig --certificate-chain nv-agent-root-cert.pem --ignore-unsigned-files` |

3. Open `SKILLCARD.yaml`

to see ownership, dependencies, license, and verification status.

To learn more, visit the [Skills documentation](https://docs.nvidia.com/skills) to review all available skills or browse the [NVIDIA/skills](https://github.com/nvidia/skills/) GitHub repo.

### Acknowledgments

*We’d like to thank Pratyusha Maiti, Alec Evangelista, Mohit Gupta, Isabel Hulseman, Yogesh Dangi, Yashraj Basaravaj Patil, Keshav Pradeep, Narendran Raghavan, Christopher Kevin, Siddharth Itagi, and Pranita Maske for contributing to this work.*

## Start the discussion at forums.developer.nvidia.com
