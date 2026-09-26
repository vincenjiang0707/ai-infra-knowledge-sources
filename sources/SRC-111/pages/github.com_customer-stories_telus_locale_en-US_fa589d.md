source: https://github.com/customer-stories/telus?locale=en-US

What does it take to power wireless connectivity, accessible healthcare, and safe food supply chains for more than 35 million people across the second-largest country in the world? For TELUS, a communications and information technology provider in Canada, it means having a team of more than 78,000 people and nearly 5,000 developers, analysts, and technicians who work everywhere from the heart of Vancouver to the remote areas of Nunavut. With remote work more popular than ever, TELUS bridges the gap to keep Canadians connected.

Tasked with making the future friendler for all Canadians, TELUS faced a core challenge: It had a large, fragmented technology stack with different teams using different tools. The need to manage all these tools, many of which were incompatible with each other, resulted in long development and testing times. To help unify the company under a single platform, TELUS partnered with GitHub.

GitHub provides a central location for all of TELUS’ software development. Having visibility into a project is essential for monitoring progress and changing workflow processes. “With GitHub, we now have a single platform for developer communication throughout TELUS,” explains Justin Watts, Director of Engineering and Productivity. “Developers can propose and discuss ideas through Issues and pull requests, which has really democratized technical conversations.”

[GitHub Issues](https://github.com/features/issues) provide a robust solution for tracking the progress of every repository. For TELUS, this means being able to track changes and provide additional information at each pull request, complete with end-to-end visibility.

When developing in a local environment, developers face challenges that run the gamut from managing dependencies to accessing shared packages at scale. Traditionally, everything from shared package management to libraries and dependencies had to be set up manually before developers could write any code. [GitHub Codespaces](https://github.com/features/codespaces) bypasses many of those problems. TELUS can now create a standardized developer environment for distributed teams of developers, business analysts, and technicians to better develop and collaborate on code—no matter the type of device they are using. “It’s so much easier for developers to use or even contribute to any repo when they can just spin-up a Codespace and immediately start working with the code,” explains Katie Peters, Developer Advocate. “It’s a huge win for innersource collaboration.”

“GitHub shaves off entire days from the new employee onboarding process,” adds Ketan Shah, Manager of Information Services at TELUS. “New developers are up and running within minutes because everything is all in one place.”

GitHub shaves off entire days from the new employee onboarding process. New developers are up and running within minutes because everything is all in one place.


In its software development lifecycle, TELUS relies on [GitHub Actions](https://github.com/features/actions) to automate much of its testing and validation. This allows the company to not only separate deployments from its releases but also to shift left and make its software more secure. TELUS uses Actions to deploy applications and conduct tests before integration, automating several previously manual processes. All told, “GitHub Actions saves each developer at TELUS around two hours per week,” estimates Director of Digital Platforms Steve Tannock. “Multiply that by 48 weeks and 250 developers and it adds up very quickly,” he says.

It’s now much easier for TELUS developers to deploy code multiple times per day without sacrificing testing and code quality. “Verification is automated into the development lifecycle, so Developers get immediate and continuous feedback on their work.” Peters says. “Releasing is decoupled from deploying. Come release day, Developers have confidence in their artifact and it’s just a matter of clicking a button and customers are using it. All the validation occurred weeks, months ago.”

Automation also plays a key role in securing software at TELUS. The company uses a model they call “security by design” as a part of their shift-left strategy. Instead of relying solely on their security team to identify bugs and vulnerabilities, TELUS leverages [GitHub Advanced Security](https://github.com/features/security), enabling developers to spot problems before they make it into production.

“GitHub Actions saves each developer at TELUS around two hours per week. Multiply that by 48 weeks and 250 developers and it adds up very quickly.


Thanks to Secret Scanning, TELUS was able to find and remediate thousands of accidently shared secrets—such as passwords, API keys, or authentication tokens. TELUS found that most of these secrets were shared in repositories that had never been touched—a discovery that ultimately helped them improve their archiving processes.

The most profound impact on security for TELUS came when they implemented push protection across their entire organization. [Push protection](https://github.blog/2022-04-04-push-protection-github-advanced-security/) automatically blocks code from being introduced if secrets are found within the codebase, ensuring that secrets aren’t accidently shared in the first place. “There’s far less room for human error when handling secrets now,” Peters says.

For TELUS, the implementation of push protection was turn-key. “Push protection is such a beautiful workflow,” Watts says. “We’ve never received a single complaint from developers,” says Watts. For an enterprise operating at scale, the importance of a seamless deployment with no hitches can’t be undervalued.

[Dependabot](https://github.com/features/security/software-supply-chain), meanwhile, is always running in the background and monitors for insecure dependencies. When an insecure dependency is found, Dependabot sends an alert and a pull request recommendation for how to remediate the potential issue further.

The improvements TELUS sees in each area—consolidation, automation, and security—could be considered wins on their own. Considered together, they reflect a more integrated way of building and releasing software and enabling the company to expand its customer base.

“The bet we made on GitHub was that it would be a unifying technology that would drive innovation and collaboration throughout the organization,” says Watts. “And as we keep building features, that bet keeps paying off.”