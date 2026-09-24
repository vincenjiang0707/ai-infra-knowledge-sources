# using-ai-agents-to-secure-google-infrastructure

source: https://cloud.google.com/blog/topics/systems/using-ai-agents-to-secure-google-infrastructure

# Changing the game: Using agentic AI to secure infrastructure code

##### Andrés Lagar-Cavilla

Distinguished Engineer, Google

##### Parthasarathy Ranganathan

VP, Engineering Fellow

AI is accelerating software development at an unprecedented pace. But as code generation scales, so do the challenges of securing the code, especially emerging AI-based vulnerability exploitations. To meet these challenges, the Google AI and Infrastructure team is transforming how we approach security. In this article, we discuss new AI-native agentic methods that we’ve developed that systematically embed high-precision, pervasive vulnerability scanning and patching directly into Google’s software development lifecycle. By continuously scanning every code change across hundreds of millions of lines of code that we deploy onto our infrastructure, we are preventing hundreds of vulnerabilities per month from ever reaching our code base or production, defending our global network, AI infrastructure and our users.

**Solution architecture and implementation **

Pervasive pre-submit agentic scanning: security as part of ongoing software development

Traditionally, the technology industry relies on large one-off security scans that are slow and lack sufficient context. As a result, they often find vulnerabilities too late. Our approach instead focuses on pre-submit scanning, where we evaluate each code check-in (across every layer of the stack) in real-time using AI agents. By integrating the pre-submit scan into the tools developers already use, security becomes a continuous routine process, similar to rule checkers, readability reviews or other software development tools. Also, from an AI perspective, scanning each individual code change requires much less context than performing a large one-off scan, significantly improving the scan’s effectiveness.

### The importance of localized threat models

For this initiative, we evolved [Mantis](https://github.com/google/mantis), our open-source multi-agent review harness, to increase the precision of our security agents by matching them with a cohort of robust localized threat models. Rather than relying on static decoupled documents, the threat models use live codebase metadata. The scanning agent improves its accuracy further using a dependence call graph across packages and libraries to expand and refine its threat model context. Making threat models part of our ongoing vulnerability scanning encourages developers to continuously update threats and dependencies, keeping the models up-to-date. Using localized and precise threat model data translates to dramatic accuracy improvements, bringing our false-positive rates down to 3% in some cases.

### Specialized triage agents speed up development

Vulnerability scanning as part of code check-in requires it to respond quickly to the developer or agents generating the code, so as not to impede engineering productivity. To get responses with low latency, we run a two-step validation process. First, we run a quick lightweight scan that validates its findings against a specialized triage agent. This agent programmatically checks the actual structure of the code (using abstract syntax tree parsing, call-graph traversal, and pre-indexed domain safety rules) to prove that the vulnerable path is actually reachable by an attacker. This agent gets over 92% precision and completes its work in less than a minute. Then, a post-submit scan as part of nightly integration testing serves as a second layer of defense, using off-peak cycles to test for vulnerabilities that may have been introduced across multiple changes.

### Bug fix agents close the loop

Finding vulnerabilities is only half the battle. The last component of our solution is an automated bug-fix agent that uses the scan results and generated proofs (snippet of code that demonstrates how the vulnerability is exercised) to autonomously construct precise fixes that are consistent with our internal coding standards. The agent submits the fixes for human review as part of the original change request’s review, further reducing the time between detection and resolution.

### Learnings and call to action

Embedding continuous scanning directly into the software development lifecycle has been a game changer at Google; its suggestions are widely adopted, and it’s prevented a multitude of vulnerabilities from being introduced into the codebase. But any organization wishing to improve security can adopt a similar AI-native approach, following these principles:

-
**Keep systems separate:**To prevent bias, keep the harnesses, rules, and context for each of your development, scanning, triage agents separate. Pair lightweight AI scans with deterministic, structural validation to drive down latency and improve accuracy. -
**Use context wisely:**Feed your agents your existing threat models. Precise context is the answer to reducing false positives, and up-to-date threat models set a high floor on a team's security posture by improving the rate of true positives in presubmit scanning. -
**Build a good harness:**While the choice of the underlying model is important, using a multi-agent harness can have substantial impact, by helping compensate for variability in model choice. -
**Automate the fix:**Use agents to also propose human-in-the-loop fixes, to further reduce time-to-resolution.

If you want to get started on your own AI-native security transformation, [Mantis](https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs?e=48754805) is now available as open source for you to use and benefit from. You can also [learn more about the fundamentals of cybersecurity](https://cloud.google.com/learn/security/mandiant-academy-courses/fcs?e=48754805) and the other platforms that power this agentic pipeline: Google Cloud, Gemini Enterprise and Gemini models running on Trillium and Ironwood TPUs. And you can get inspiration from how agentic vulnerability scanning and remediation defends Google Cloud customers as an integral part of [Google Cloud’s secure software development lifecycle (SDLC) effort](https://cloud.google.com/blog/products/identity-security/cloud-ciso-perspectives-how-google-cloud-security-uses-ai-internally).

With special recognition to critical team members who made this delivery possible: Stella Voutsina (Lead Program Manager), Yulong Zhang (Senior Staff Security Engineer, Mantis), and Nick Galloway (Staff Security Engineer, Mantis).
