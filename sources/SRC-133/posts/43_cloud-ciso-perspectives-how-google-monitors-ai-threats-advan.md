# cloud-ciso-perspectives-how-google-monitors-ai-threats-advances-ai-defenses

source: https://cloud.google.com/blog/products/identity-security/cloud-ciso-perspectives-how-google-monitors-ai-threats-advances-ai-defenses

# Cloud CISO Perspectives: How Google monitors AI threats and advances AI defenses

##### Sandra Joyce

VP, Google Threat Intelligence

##### Get original CISO insights in your inbox

The latest on security from Google Cloud's Office of the CISO, twice a month.

[Subscribe](https://go.chronicle.security/cloudciso-newsletter-signup?utm_source=cgc-blog&utm_medium=blog&utm_campaign=FY23-Cloud-CISO-Perspectives-newsletter-blog-rail-CTA&utm_content=-&utm_term=-)

Welcome to the first Cloud CISO Perspectives for September 2026. Today, Sandra Joyce shares the latest details on Google’s visibility into how attackers are using AI, and how we’re using AI to stop them.

As with all Cloud CISO Perspectives, the contents of this newsletter are posted to the [Google Cloud blog](https://cloud.google.com/blog/products/identity-security/). If you’re reading this on the website and you’d like to receive the email version, you can [subscribe here](https://cloud.google.com/resources/google-cloud-ciso-newsletter-signup).

**‘Spellcheck for cybersecurity’ and beyond: How Google monitors AI threats and advances AI defenses**

*By Sandra Joyce, VP, Google Threat Intelligence*

Anyone operating in security knows that speculation is a major liability during periods of technological disruption. While there is plenty of hype and understandable concern around how threats might use and target AI, a CISO’s AI security strategy has to be anchored in ground truth.

Google operates at a rare intersection as both a frontier AI lab and a security company with a frontline view of global incidents. This dual vantage point allows us to understand how AI is built, and exactly how AI is being targeted in the wild. To provide the operational realities that security and business leaders need in the AI era, Google Threat Intelligence Group (GTIG) recently released our [latest AI Threat Tracker](https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai).

When we strip away the noise and look at the telemetry, the real threat landscape boils down to three structural shifts that CISOs must address:

-
AI is reshaping how software is built.

-
AI is expanding the attack surface.

-
AI is enhancing threat capabilities.


Today, we’re sharing details on Google’s visibility into these three challenges, and our approach for solving them.

**Building securely in the AI era **

AI has fundamentally altered software development velocity. Across the industry, autonomous agents and AI workflows now push code into production at unprecedented speed. This creates exciting opportunities for innovation, yet CISOs are faced with the difficult task of mitigating enterprise risk while maintaining business momentum.

We’re seeing threat actors turn our greatest engineering shortcut against us by contaminating upstream packages that AI assistants are trained to suggest and trust. GTIG believes that malicious contamination of AI-assisted coding practices has been contributing to the significant growth in large-scale, open-source software supply chain compromises we [observed in 2025 and early 2026](https://cloud.google.com/blog/topics/threat-intelligence/mitigation-guidance-for-supply-chain-compromise).

#### The solution to a machine-speed threat landscape isn't slowing developers down — it’s building security natively into the AI pipeline. Part of this process involves in-editor guardrails for developers that create a real-time 'spellcheck for cybersecurity.'

We’re also monitoring adversaries targeting agents. The financially-motivated threat actor TeamPCP (UNC6780) has implemented more than half a dozen methods to exploit AI tools and open-source software development practices, including hijacking AI toolkits, prompt injection, and blinding AI scanners with toxic prompts to obfuscate malicious payloads.

The solution to a machine-speed threat landscape isn't slowing developers down — it’s building security natively into the AI pipeline. Part of this process involves in-editor guardrails for developers that create a real-time “spellcheck for cybersecurity.”

Just as word processors underline typos without forcing the writer to stop, security controls must sit natively inside the developer’s editor and agentic workflows, instantly flagging poisoned packages, toxic prompts, and misconfigured toolkits.

Crucially, this can’t stop at the editor. Traditional security suffers from context blindness: Code editors can’t see cloud configurations, delivery pipelines miss runtime exposure, and production teams can’t easily patch root-cause blueprints.

Bridging this gap requires an integrated code-to-cloud approach — the exact design principle behind platforms like [Wiz Code](https://www.wiz.io/platform/wiz-code). The underlying approach is to ensure code is continuously verified against live cloud realities before it ships.

When organizations think about AI-driven code analysis, the default assumption is to pick one frontier model and point it at their repository. However, our research and telemetry show that single-model security creates a dangerous monoculture: No single AI model can discover every vulnerability, and threat actors are already testing inputs that can blind specific LLM safety filters and scanners.

#### To secure this expanding attack surface, CISOs should avoid the trap of managing AI through disconnected silos... The future of cloud and AI defense needs to be built on a unified and dynamic graph that connects your code, your models, your data lineage, and your runtime identities into a single living map.

To solve this, Google takes a [deliberate multi-model approach](https://cloud.google.com/blog/products/identity-security/cloud-ciso-perspectives-next-26-why-we-re-multicloud-and-multi-ai). By orchestrating several foundation models — including Gemini, commercial, and open-source — we cross-validate findings, strip out false positives, remediate code, and identify complex logic flaws that a single model misses. We’re smarter with more than one “brain.”

**Securing AI **

Securing the development lifecycle is only half the battle. We also need to prevent adversaries from exploiting AI attack surfaces and weaponizing over-privileged agents. Threat actors are targeting AI workloads with techniques that include:

-
**LLMJacking**: Cybercriminals and state-sponsored groups target GPU access to support running their AI models and agentic workflows. In one notable intrusion Mandiant investigated in April, a threat actor gained initial access to a victim’s cloud environment from an exposed personal access token, and used it to deploy unauthorized AI infrastructure and scale high-performance compute resources, leaving the victim to absorb the hardware and platform costs. -
**Targeting of AI data and access**: Cybercriminals now recognize that your custom prompts, agent instructions, and fine-tuned models represent high-value crown jewels. In Q2 2026, Mandiant investigated multiple data theft extortion operations where threat actors stole proprietary AI data, including models, skills, prompts, source code, and related research. Demand is also surging for AI account credentials in underground marketplace forums, with some sellers offering steep discounts for consumer accounts at up to 99% off retail prices.

To secure this expanding attack surface, CISOs should avoid the trap of managing AI through disconnected silos. Don’t treat agent access policies, model inventories (AI-BOMs) and shadow AI as separate challenges because these risks are deeply connected. The future of cloud and AI defense needs to be built on a unified and dynamic graph that connects your code, your models, your data lineage, and your runtime identities into a single living map.

Pioneered by the [Wiz Security Graph](https://www.wiz.io/lp/wiz-security-graph), this approach serves as the contextual engine for [Google AI Threat Defense](https://cloud.google.com/security/ai-threat-defense) (AITD) — our broader autonomous security framework that fuses the reasoning power of Gemini and other frontier models, the contextual risk prioritization of Wiz, the code remediation capabilities of CodeMender, and the frontline expertise of Mandiant to stay ahead of AI-driven attacks. Crucially, this context is not siloed; it directly feeds [Google Security Operations](https://cloud.google.com/security/products/security-operations), ensuring that security operations teams can continuously identify, prioritize, and sever toxic attack paths at machine speed.

**Defending against AI threats**

Threat actors are rapidly moving beyond simple prompt generation toward fully-automated, multi-agent attack pipelines.

In one notable intrusion investigated by Mandiant, a financially-motivated actor compromised an organization's cloud infrastructure and deployed an autonomous agent framework. The threat actor used an AI coding chatbot, a prompt, and a set of agent instructions to plan, build, and execute a mass credential harvesting campaign in less than six hours.

We’re also tracking adversaries using AI as an intelligent orchestrator across the entire attack lifecycle. GTIG recently observed a PRC-nexus espionage group experimenting with a tool called CC Switch to cycle across multiple accounts and swap AI models — like Claude, Codex, and Gemini — picking the best model for specific tasks, such as writing exploit scripts and drafting lures. While the underlying hacking tools aren’t new, AI turned what had been a disjointed manual process into a smooth and automated workflow.

#### To take advantage of your deep context, it’s imperative to shift from manual, human-scale incident response to machine-speed security operations. We can no longer rely on human analysts manually triaging endless backlogs of static alerts.

While these machine-speed attacks sound daunting, defenders actually hold an asymmetric advantage. Even when armed with autonomous AI, an attacker operates from the outside with limited context — probing in the dark, guessing connections, and hoping a compromised credential leads to a useful asset.

Defenders, on the other hand, [possess deep context](https://cloud.google.com/blog/products/identity-security/cloud-ciso-perspectives-how-ai-leverages-deep-context-defenders-advantage) that attackers don’t have. You know your code, cloud configurations, user identities, deployment realities, and internal architecture better than anyone. When you feed this rich, multi-dimensional internal observability into security models, AI defense becomes inherently faster and more accurate than AI offense.

To take advantage of your deep context, it’s imperative to shift from manual, human-scale incident response to machine-speed security operations. We can no longer rely on human analysts manually triaging endless backlogs of static alerts.

By codifying our frontline threat intelligence directly into these AI models, these autonomous agents can continuously monitor for, investigate, prioritize, and remediate attacks.

**How Google is helping defend the ecosystem**

As adversaries adopt AI, we have a unique opportunity to disrupt them at the source. As a major security and AI provider, we take this responsibility seriously, using multiple levers to stay ahead.

-
**Disabling malicious infrastructure**. If you use Google tools to facilitate an attack, you lose access to those tools. We proactively disable the projects, accounts, and assets of known bad actors. -
**Hardening our AI models and classifiers**. We operate a continuous feedback loop for our AI models. By feeding threat intelligence directly back into product development, our models learn to recognize and refuse malicious requests before an attack can even be generated. -
**Automating vulnerability hunting and patching also disrupt adversaries**. We are moving from manual patching to AI-driven hunting. Tools like[CodeMender automatically fix critical vulnerabilities](https://cloud.google.com/blog/products/identity-security/find-and-fix-software-vulnerabilities-with-codemender)in the code itself. -
**Developing advanced defenses and threat models**. Our teams at Google DeepMind are building specialized defenses for generative AI — deploying active monitoring across our entire ecosystem to identify misuse in real-time.

Securing the AI era can’t be achieved with the disconnected, manual tools of the past, and you can only defend against an AI-powered threat with an AI-powered defense. To tip the scales back in favor of defenders, we must transition to a continuous, machine-speed model of protection — and at Google, we are committed to building that secure future alongside you.

To learn more about our approach to securing the AI era, please check out our new [Mandiant AI Risk and Resilience report](https://cloud.google.com/security/resources/ai-risk-and-resilience-2026).

**In case you missed it**

Here are the latest updates, products, services, and resources from our security teams so far this month:

**A manufacturing blueprint for secure agentic AI**: AI and agents have arrived on the factory floor. Today’s CISOs and business leaders must balance innovation with precision, physical safety, and operational resilience..**Read more****Proactive cyber defense for governments and enterprises**: Our new Fairwind Program is a limited access program for governments and trusted partners to use our most advanced cyber defense capabilities..**Read more****Getting started with the Mantis harness to find and fix bugs**: Mantis is part of how Google finds and fixes vulnerabilities at machine-speed. The open-source AI harness creates a more effective repository analysis..**Read more****Breaking into Google's GFile for $100,000**: Learn about how a vulnerability — that was not exploited and has now been patched — could have allowed attackers to chain unauthenticated, undocumented internal APIs with overly-permissive shared file libraries to achieve unrestricted data access across core infrastructure..**Read more****Introducing new session management tools with native, granular controls**: New Google Cloud session controls are deeply integrated and a granular feature of Context-Aware Access. Here’s what you need to know..**Read more****How Blackline prevents data exfiltration with VPC Service Controls**: We’re excited to share new policy intelligence capabilities in VPC-SC that help drive operational simplicity: Violation analyzer and violation dashboard..**Read more****Introducing Continuous Vulnerability Assessment**: You can detect exposure to new vulnerabilities the moment they’re published with Wiz CVA..**Read more****How developers prevent production risk at the source**: Fixing security vulnerabilities in code takes seconds, while patching in production creates high operational costs and risk. Discover how empowering developers as your first line of defense eliminates exposure across every phase of your software pipeline..**Read more****Wiz achieves GovRAMP High authorization**: Delivering unified cloud security and accelerating secure modernization to protect citizen data and critical infrastructure..**Read more**

Please visit the Google Cloud blog for more security stories [published this month](https://cloud.google.com/blog/products/identity-security).

**Threat Intelligence news**

**AI Threat Tracker: From prompting to autonomy**: In the newest Google Threat Intelligence Group (GTIG) report on the adversarial misuse of AI, we’ve observed adversaries transition from basic prompting to agentic AI workflows and AI-enabled automation, including threat actors compromise a cloud resource, then plan, build, and execute an agent-enabled mass credential harvesting campaign in under six hours..**Read more****Financially-motivated threat actor BREEZE COMET targets Brazil**: Learn about BREEZE COMET’s tactics and toolkit, and our mitigation recommendations and detections to support organizations in defending against this active and developing threat..**Read more****JFrog Artifactory under attack**: Wiz Research has identified active, in-the-wild exploitation of three critical and high-severity vulnerabilities impacting JFrog Artifactory. Attackers are chaining these vulnerabilities to bypass authentication and gain administrative control..**Read more**

Please visit the Google Cloud blog for more threat intelligence stories [published this month](https://cloud.google.com/blog/topics/threat-intelligence/).

**Now hear this: Podcasts from Google Cloud**

**Cloud Security Podcast: Patching browsers with AI, agents, Rust, and your tabs**: Jasika Bawa and Doug Turner of Chrome Security explore how Google Chrome now uses AI agents to autonomously identify and patch security vulnerabilities at an unprecedented scale, significantly accelerating the browser's update cadence..**Listen here****Cloud Security Podcast: All about Project Atlas, Wiz's AI vulnerability research**: Nir Orfeld, head of vulnerability research, Wiz, discusses how his team uses multi-agent AI systems for discovering high-impact zero-day vulnerabilities in cloud infrastructure..**Listen here****Cloud Security Podcast: How Google eliminates classes of vulnerabilities at scale**: How do you build the foundations for a secure Google-scale enterprise that stays secure even if an AI is writing the code and nobody has time to review it? Christoph Kern, principal security engineer, Google, explores what secure-by-design really means in the AI era..**Listen here**

To have our Cloud CISO Perspectives post delivered twice a month to your inbox, [sign up for our newsletter](https://cloud.google.com/resources/google-cloud-ciso-newsletter-signup). We’ll be back in a few weeks with more security-related updates from Google Cloud.
