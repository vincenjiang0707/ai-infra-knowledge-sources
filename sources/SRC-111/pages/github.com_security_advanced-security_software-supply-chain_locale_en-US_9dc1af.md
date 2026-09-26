source: https://github.com/security/advanced-security/software-supply-chain?locale=en-US

# Secure your software supply chain

Manage open source risks with GitHub’s supply chain security. Detect and fix threats early with automated scanning, updates, and policy enforcement—keeping your software resilient.

## Secure your dependencies

Automatically detect vulnerabilities and get trusted updates with Dependabot.

### Prioritize what matters

Dependabot surfaces the top 10% of your most critical alerts first using exploitation likelihood, severity scores, and triage rules.

### Distribute what you build

Easily sign and verify your builds with artifact attestations—simplifying security and compliance.

## From dependencies to deployment, lock down your supply chain.

Identify critical risks faster with EPSS scores and automated alerts. Map dependencies and dependents, including transitive ones, with one-click SBOMs.

[Explore supply chain security](https://docs.github.com/code-security/supply-chain-security/understanding-your-software-supply-chain/about-supply-chain-security)

Stay secure with automatic pull requests for the latest dependencies. Dependabot groups updates for faster reviews and merges.

[Explore Dependabot](https://docs.github.com/code-security/dependabot/dependabot-alerts/about-dependabot-alerts)

Enforce security and license compliance on pull requests with the dependency review action (available with GitHub Code Security).

[Explore the Dependency Review Action](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review)

Easily sign and verify builds with artifact attestations. Meet external compliance frameworks like SOC2 or strengthen internal security with SLSA—up to Build Level 3.

[Explore artifact attestations](https://docs.github.com/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds)

### Secure software from the start

Whether you’re contributing to an open source project or choosing new tools for your team, your security needs are covered with GitHub.

[Contact sales](https://github.com/security/contact-sales?ref_cta=Contact+sales&ref_loc=footer&ref_page=%2Fsupply_chain_lp&locale=en-US)

## Best practices for more secure software

[Securing your end-to-end supply chain](https://docs.github.com/en/enterprise-cloud@latest/code-security/supply-chain-security/end-to-end-supply-chain/end-to-end-supply-chain-overview)

Protect your entire GitHub workflow, from personal accounts to code and builds.

[Explore the DevSecOps guide](https://github.com/resources/whitepapers/the-enterprise-guide-to-ai-powered-devsecops?locale=en-US)

Learn how to write more secure code from the start with DevSecOps.

[Avoid AppSec pitfalls](https://github.com/resources/whitepapers/three-appsec-pitfalls-security?locale=en-US)

Explore common application security pitfalls and how to avoid them.

### Frequently Asked Questions

#### What is supply chain security?


When developing a software project, you likely use other software to build and run your application, such as open-source libraries, frameworks or other tools. These resources are collectively referred to as your “dependencies”, because your project depends on them to function properly. Your project could rely on hundreds of these dependencies, forming what is known as your "supply chain".

Your supply chain can pose a security risk. If one of your dependencies has a known security weakness or a bug, malicious actors could exploit this vulnerability to, for example, insert malicious code (malware), steal sensitive data, or cause some other type of disruption to your project. This type of threat is called a "supply chain attack". Having vulnerable dependencies in your supply chain compromises the security of your own project, and you put your users at risk, too.

One of the most important things you can do to protect your supply chain is to patch your vulnerable dependencies.

Attackers don’t just target dependencies you use; they will also target user accounts and build processes as well. It’s important to secure both to ensure that the code you distribute hasn’t been tampered with.

GitHub offers a range of features to help you understand the dependencies and secure the dependencies in your environment, and to secure your GitHub accounts and build system.

#### Why choose GitHub’s supply chain features instead of third-party products?


Unlike third-party security add-ons, GitHub’s supply chain features operate entirely in the native GitHub workflows that developers already know and love. By making it easier for developers to remediate vulnerabilities as they go, GitHub frees time for security teams to focus on critical strategies that protect businesses, customers, and communities from application-based vulnerabilities.

#### What is SLSA and SLSA level 3?


Supply-chain Levels for Software Artifacts (SLSA) is a framework for improving the end-to-end integrity of a software artifact throughout its development lifecycle. It provides a comprehensive, step-by-step methodology for building integrity and provenance guarantees into your software supply chain. SLSA Level 3 signifies a significantly hardened software supply chain where builds are highly isolated, source code history is verified, and provenance is strictly controlled, providing a strong guarantee against tampering and ensuring the integrity of software artifacts. GitHub Actions and Artifact Attestations greatly simplify the journey to SLSA Level 3.

#### Can GitHub create software bill of materials or SBOMs?


You can export a software bill of materials or SBOM for your repository from the GitHub dependency graph. SBOMs allow transparency into your open source usage and help expose supply chain vulnerabilities, reducing supply chain risks.

#### Are GitHub’s supply chain features paid or free?


Most of GitHub’s supply chain features are available for free to all users. A select few advanced features are available to private repos only in GitHub Code Security. See pricing.