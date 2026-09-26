source: https://github.com/customer-stories/x15

Enterprises are often compared to aircraft carriers and freight trains, since it can be difficult, if not impossible, for businesses of their size to quickly change course or stop an in-progress motion. On one hand, these giants are sturdy and reliable. But a lack of agility can make them prone to disruption if they can’t pounce on new opportunities or quickly react to changes in the market.

Founded in 1911, the Commonwealth Bank of Australia has grown to become the country’s leading bank, with more than 15 million customers, 800,000 shareholders, and 52,000 employees. It stays nimble with the help of x15ventures, a venture scaler firm spun out of the bank’s innovation lab in 2020. x15 builds, buys, and invests in digital solutions and startups that have the potential to reimagine existing banking products and services, or extend CommBank’s relationship and relevance with its customers into new areas. For example, [Unloan](https://www.unloan.com.au/) reimagines home loans for a digital world, while [Credit Savvy](https://www.creditsavvy.com.au/) helps Australians access, better understand, and protect their credit reputation.

Operating on a separate technology stack from the bank means x15 can rapidly build, launch, and iterate ventures at a pace that feels closer to that of a startup, but with the scale and reach of one of Australia's best-known organizations behind them.

However, as a subsidiary of CommBank, speed cannot come at the cost of security. Operating with fewer organizational resources than its parent, x15 relies on a combination of specially designed governance and risk processes and technology solutions, including [GitHub Enterprise](https://github.com/enterprise), to meet its obligations—meaning its ventures can experiment and innovate in a 'bank safe' environment.

GitHub offers a lean platform solution, with CI/CD automation and security under one roof, that increases velocity and scale without adding complexity or sacrificing security. x15 unified its various units under a single GitHub Enterprise account and assigned each to a separate [organization](https://resources.github.com/learn/pathways/administration-governance/essentials/strategies-for-using-organizations-github-enterprise-cloud/)—a structural unit of GitHub Enterprise. With this structure, x15 preserves visibility into each of its ventures and enforces enterprise-wide policies to meet its regulatory requirements, while also providing autonomy.

“GitHub gives us the controls and oversight we need without placing a burden on our developers or hampering their ability to innovate,” says Soc Sieng, chief engineer at x15.

“GitHub gives us the controls and oversight we need without placing a burden on our developers or hampering their ability to innovate.”


Automation on GitHub Enterprise plays an increasingly important role in boosting both efficiency and security at x15, as the company taps the power of [GitHub Actions](https://github.com/features/actions), GitHub Advanced Security, and GitHub Apps. For example, x15 ingests GitHub event data into a custom-built platform called xGraph, helping ensure decentralized modern DevOps teams are meeting the obligations associated with being part of a regulated entity.

“Anything that we can automate helps with consistency, and consistency is good for compliance. Before GitHub Actions, we had to review style and check for antipatterns through manual code reviews,” says Sieng. “Now, we can bake these checks into the build pipeline so we don’t have to worry about it anymore. By deferring to the build pipeline, we spend less time on review and more on solving the business problem at hand.”

With these automated reviews, they estimate they’ve saved an hour with every deployment. At six ventures (at time of writing), each deploying twice daily, that saves up to around 84 hours a week, or nearly 14 days in a month.

“GitHub Actions enables each of our ventures to deploy multiple times a day and deliver value to customers sooner. They’re also better positioned to experiment with new features and pivot if the features don’t have the desired impact,” says Sieng.

Seeing the savings offered by GitHub’s platform, when x15 acquires a new company, it now swaps their existing tools for GitHub Actions. And the move comes with an added benefit: With CI/CD in the same platform as the company’s source code, Sieng says that more developers are exposed to the details of automation.

GitHub Actions enables each of our ventures to deploy multiple times a day and deliver value to customers sooner. They’re also better positioned to experiment with new features and pivot if the features don’t have the desired impact.”


“If you need to troubleshoot a failure in the build pipeline, you can look at what's actually happening and fix it by updating the code. It broadens the skills of the engineers and the team so that they're more accountable for how the software is built ,” he says.

Beyond CI/CD, Sieng says GitHub Actions also solves unique challenges, like licensing for embedded fonts. The company built a custom action to check repositories for unregistered embedded fonts, which can cause builds to fail. The action not only protects against licensing violations, but also saves time that would otherwise be spent manually checking for these violations.

Automation within GitHub’s platform doesn’t end with GitHub Actions or GitHub Apps, however. [GitHub Advanced Security](https://github.com/features/security) bakes security directly into developers’ workflows, rather than relegating security to after-the-fact motions across disparate tools and separate teams. With GitHub Advanced Security, x15 achieves a transparent security posture that guarantees its software is secure and compliant.

“With GitHub Advanced Security, we spot insecure practices early on in the development cycle. This allows us to take action before we have to deal with any of the downstream effects.”


For example, Push Protection blocks developers from pushing secrets into code, so security teams and developers can both rest easy knowing they won’t need to spend time later revoking and remediating leaked secrets. What’s more, when x15 onboards new acquisitions, Push Protection quickly finds secrets during the migration process that would have otherwise gone unnoticed. Meanwhile, CodeQL automates code scanning for vulnerabilities and other errors, and Depandabot notifies developers of potential software supply chain vulnerabilities as they appear, offering actionable steps for remediation.

“With GitHub Advanced Security, we spot insecure practices early on in the development cycle,” says Sieng. “This allows us to take action before we have to deal with any of the downstream effects.”

"GitHub provides a holistic platform for us to store, automate, and secure our code, while offering our ventures the autonomy they need to operate and iterate efficiently.”


x15’s success relies on maintaining a constant, careful balance between speed and security and GitHub’s platform provides a single, collaborative ecosystem where each individual venture can operate securely with the agility of a startup.

“GitHub provides a holistic platform for us to store, automate, and secure our code, while offering our ventures the autonomy they need to operate and iterate efficiently,” says Sieng.