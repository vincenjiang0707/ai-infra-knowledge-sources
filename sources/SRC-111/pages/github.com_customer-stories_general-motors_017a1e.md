source: https://github.com/customer-stories/general-motors

From advanced safety controls to engine management and driver assistance technologies, software now powers a vehicle’s most critical systems. At General Motors, almost 20,000 developers, collaborating across 150,000 repositories with 80+ technological partners, make this possible, accelerating software development and the vehicles that depend on it.

But at this scale and the speed of innovation today, GM’s legacy developer ecosystem couldn't keep pace. Fragmented across more than 40 tools, this complex infrastructure created friction for developers and slowed the entire development process. This sprawl of disconnected tools also made it difficult to enforce consistent security policies, creating unknown risks across the software supply chain.

By consolidating onto [GitHub Enterprise Cloud ](https://github.com/enterprise)and adopting GitHub Advanced Security and GitHub Copilot, GM eliminated bottlenecks, embedded security into daily workflows, and empowered its developers to accelerate delivery of critical work. The results include **significant annual savings**, **build times cut from hours to minutes**, **and** **engineers empowered to focus more on meaningful work**.

## Choosing a modern foundation for the future

To power the next generation of software-driven vehicles, General Motors’ DevOps Tool team knew they needed to overhaul their developer experience, starting by consolidating their fragmented toolchain and choosing a single, modern platform that could support secure access to internal networks, elastic on-demand scaling, and accelerated developer velocity. They evaluated their options, including standardizing on existing tools like Azure DevOps, but ultimately chose GitHub. “Transitioning to GitHub was a straightforward decision," says Mario Parisi, Software Development Manager, General Motors. "Our teams were spread across too many tools and inconsistent workflows. Today, we operate within a unified ecosystem that supports all of our developers.”

Transitioning to GitHub was a straightforward decision. Our teams were spread across too many tools and inconsistent workflows. Today, we operate within a unified ecosystem that supports all of our developers.


With the decision made, the team executed the massive consolidation to GitHub Enterprise Cloud, unifying ~150,000 repositories and nearly 20,000 developers with zero production impact during migration.

"It was like landing planes on a runway while the runway was still being built, and we stuck the landing," says Parisi, who attributes the success to a deep, hands-on partnership with [GitHub's Expert Services ](https://github.com/services)and R&D teams.

With the foundational challenges solved, GM could shift its focus from managing infrastructure complexity to delivering new features.

## A new threshold for developer velocity

In GM's previous on-premises environment, developer productivity was routinely constrained by infrastructure limitations. Teams frequently found themselves waiting in lengthy build queues, dependent on a small pool of permanent, non‑elastic shared runners. Because these environments were not ephemeral, configuration changes made by one team could inadvertently affect another team’s builds, introducing instability across the organization. These constraints led to inconsistent builds and unexpected failures, pulling developers away from writing code and into system troubleshooting. For Parisi, it often meant stepping in to resolve failures late into the night.

The move to [GitHub Actions ](https://github.com/features/actions)on a modern cloud-based system fundamentally improved the process. A key to their success was the implementation of VNet-injected runners, a solution that provided full, elastic cloud scale while maintaining secure, firewalled access to GM's private network. This enabled teams to provision thousands of fresh, ephemeral runners on demand: a level of speed and flexibility that was not feasible in their previous environment.

The impact on performance was significant. A critical build that once took four to six hours in the on-premises environment now completes in as little as 27 minutes on GitHub. This new platform also accelerated the creation of custom development environments. Previously, the wait for a unique runner image, a complete, self-contained software toolkit, could be months. Today, teams can simply add tools to a standard base image, reducing that wait time to under three days.

Parisi notes that the platform's improved reliability and performance reduced the need for reactive support, creating a more seamless and dependable developer experience. This shift allows developers to focus on delivering value. "That's the real productivity gain," says Parisi. "The time our developers get back by not waiting for a build is more valuable to us than just the hardware savings."

## From proactive defense to a security-first culture

The [Log4j vulnerability](https://www.ncsc.gov.uk/information/log4j-vulnerability-what-everyone-needs-to-know), which caused a widespread security crisis that impacted millions of applications and required urgent global remediation efforts, was a wakeup call to the GM team and a catalyst to update their fragmented and legacy ecosystem. Their goal: to be able to answer, “How safe are we?” easily. But at their current state, it was a "monumental effort," says Parisi.

The move to GitHub’s single unified platform and the adoption of [GitHub Advanced Security](https://github.com/security/advanced-security) provided that strategic visibility, enabling GM to evolve their security posture. The results of the initial scans were informative, surfacing more than 22,000 exposed secrets and over 1.2 million potential vulnerabilities from CodeQL and dependency scanning. They immediately implemented policies to block new commits containing secrets, stopping the problem at the source, and remediated 100% of leaked secrets.

Today, security is a seamless part of the daily workflow, not an afterthought. “GitHub Advanced Security means vulnerabilities are fixed in pull requests, not after release," says Parisi. "We can deliver faster without compromising security.” This workflow is powered by CodeQL and dependency scanning, which automatically flag vulnerabilities, and an AI-accelerated remediation process driven by Copilot Autofix.

Copilot Autofix has significantly reduced our remediation time. It flags a vulnerability, suggests a fix inline, and developers can just click to accept." — Mario Parisi, Software Development Manager, General Motors


This technical transformation also drove a significant cultural one. As Parisi puts it, "We now develop software with a security-first mindset." Plus, the ability to provide quick, accurate security reporting to leadership is now standard practice, ensuring that security and development goals are fully aligned.

## An engine for AI-powered innovation

Next, General Motors looked to deploy AI to tackle two major challenges: boosting developer productivity and modernizing critical legacy systems. Across the organization, over 8,000 developers began using [GitHub Copilot](https://github.com/features/copilot) across more than 55 languages and in a wide variety of IDEs, including VS Code, Visual Studio, and the JetBrains suite.

Copilot provided a powerful new solution for one of the most difficult challenges in a long-standing enterprise: safely updating legacy code where institutional knowledge had been lost over time. For years, GM had critical systems running on older languages like COBOL and Fortran, with "not much documentation and not much understanding of what the code does," says Parisi.

Using Copilot, developers reverse-engineered documentation for code written in older languages. Then, they leveraged it to convert this legacy code to modern languages. According to Parisi, this AI-assisted approach was a significant efficiency gain, accomplishing work that could have otherwise taken a year if done with external suppliers.

With the Copilot Coding Agent, our developers skip repetitive work. Copilot Code Review handles the PR reviews and summaries, allowing teams to focus on more complex tasks. — Suvarna Rane, Software Development Manager, General Motors


By unifying 99% of its source code and nearly 20,000 developers on a single platform, embedding security into daily workflows, and accelerating development with AI, General Motors has transformed its software practice into a strategic advantage. The company is now positioned to meet the challenges of a rapidly evolving industry, with an engineering culture built for speed, security, and innovation. As Parisi puts it, "By consolidating on GitHub, our developers can innovate faster and deliver secure software at the speed our business and customers demand."