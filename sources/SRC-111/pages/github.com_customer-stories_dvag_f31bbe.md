source: https://github.com/customer-stories/dvag

Founded in 1975, Deutsche Vermögensberatung (DVAG) has grown to become Germany’s largest autonomous financial consulting firm, serving over 18,500 full-time advisors who provide tailored financial consulting services to their more than 8 million customers. Since the beginning, DVAG’s business model has set it apart from other financial consulting firms by focusing on interpersonal relationships. Working alongside prominent product partners such as Generali and Deutsche Bank, DVAG employs a holistic financial advisory approach that spans insurance, retirement provision, and financial planning. While some financial firms have moved toward using robo-advisors, DVAG builds tools that enable financial advisors to best serve their customers while offering the human touch that lies at the core of its business.

“One of our main principles is that people need people. While our digital infrastructure enables our financial advisors to give the best services and advice for their customers, there is no replacement for human interaction,” says Pascal Müller, head of IT Application Development & Strategy. “It's all about the person-to-person relationship. Technology is a key lever in enabling DVAG’s financial advisors to focus on this relationship.”

As a company that serves both businesses and their end-customers, DVAG has multiple development teams building unique solutions for each layer of its business. While this approach offered teams self-sufficiency and ensured that each stakeholder enjoyed the best user experience possible, it had also led to inefficiencies. The teams’ infrastructure choices and practices were as individualized as their solutions. They often built from scratch instead of reusing code, and each team handled the maintenance and security for their own tech stacks. For example, teams running Jenkins alongside BitBucket had to not only maintain the software, but also operate the servers and handle disaster recovery, taking their focus away from the customer.

DVAG’s IT team turned to GitHub Enterprise to improve the customer experience across the entire application landscape and to streamline the development cycles across all development teams. The platform team centralized its bundled services (cloud services, Kubernetes, source control, CI/CD, and development tools) as a central platform service provider for developer units throughout DVAG, allowing them to focus on application development instead of maintenance and operations. The comprehensive expansion of these central services, both in breadth and depth, has been DVAG’s most important lever for optimizing application development.

GitHub Enterprise provides DVAG with a single cloud-based development platform, uniting security, automation, and developer tooling under one roof, and enabling DVAG to realize its developer experience vision. With all the modern means and tools required by developers optimally interlinked and offered intuitively in one place, DVAG’s developers can put the personal relationships that the company values back at the forefront of all its efforts.

“Being all in on GitHub makes it easier for our developers because they don’t need to switch tools and can instead focus on delivering value.”


“Being all in on GitHub makes it easier for our developers because they don’t need to switch tools and can instead focus on delivering value,” says Florian Koch, lead developer of the IT platform team tasked with internal developer experience. “They have one platform and UI where they can find everything—the source code, the workflows, the issues—all in one place and aren’t distracted by routine tasks.”

What's more, by moving from Jenkins to GitHub, DVAG reduced its application lifecycle management spend to zero and were able to create a new full-time position focused on driving new opportunities with GitHub automations.

DVAG credits [GitHub’s Expert Services](https://github.com/services/) team for a seamless migration to GitHub Enterprise in the cloud. Koch’s team met with them weekly and collaborated asynchronously to smooth over any pain points and establish best practices in their adoption of additional GitHub products, such as GitHub Actions.

With that guidance, DVAG’s platform team built and automated reusable workflows with [GitHub Actions](https://github.com/features/actions) that can be used across various teams. Now, the team can focus entirely on the overall deployment and testing workflow without having to deal with the implementation details of the various programming languages and Kubernetes APIs. This frees other developer teams at DVAG from needing to build their own workflows individually, saving valuable developer time. In total, this reduced the setup process for workflows from four hours to five minutes, or by roughly 98%. Overall, the team estimates this has saved them 225 days in wait time since implementing reusable workflows.

“Reusable workflows give us a standard way of working that we can easily manage. We can push our artifact repository and download it all in one place,” says Koch. “I cannot imagine how we could standardize our workflows efficiently without GitHub Actions.”

Saving developer time has translated directly into new features and products for DVAG’s customers. For example, DVAG now offers financial advisors an optical character recognition (OCR) solution that automatically digitizes the information in contracts, letting them focus on the person-to-person conversation instead of the manual task of data entry.

DVAG’s developers have similarly come to rely on GitHub Advanced Security’s automations to save them further time and effort, while ensuring the safety of their data. Before GitHub Enterprise, developers could accidentally publish shared credentials, costing them weeks or months to fix. Now, with [GitHub Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security), Secret Scanning detects credentials stored in repositories, while Push Protection prevents developers from publishing credentials in the first place, by prohibiting the pushing of source code with recognized passwords, access tokens, or private keys. Since implementing the feature, the team has seen a 95% decrease in security interventions for secure secret handling on the way to production.

“GitHub Advanced Security has solved the risk of leaked credentials. ”


“GitHub Advanced Security has solved the risk of leaked credentials,” says Koch. “Now, developers are alerted to the problem before they can push code live. They have a direct feedback loop.”

Dependabot has also helped DVAG to ensure the security of its software supply chain, by scanning and alerting developers to upstream security vulnerabilities in dependencies.

“With Dependabot, we see all the necessary updates to our code,” says Koch. “It’s really easy to use. You’ve got the issue and pull request, and with the correct workflows, the tests run automatically, and you can merge the fix.”

From the efficiencies offered by GitHub Actions’ reusable workflows to time saved with GitHub Advanced Security and Dependabot, Koch points to GitHub as key to their developers’ continued success, by empowering them to focus on features rather than trifling with manual, internal processes.

“We consider GitHub to be the most effective lever in providing our development teams with reliable and cutting-edge one-stop services,” says Müller. “This is the sustainable foundation for our software development efforts to prioritize building effective and innovative features that enable our customers to focus on their customers on a person-to-person basis.”