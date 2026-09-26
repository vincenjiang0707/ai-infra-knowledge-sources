source: https://github.com/customer-stories/opn

In the years since Opn launched its first product, the Omise payment gateway, online commerce has grown to more than 2 billion people making purchases online annually. As with any payment provider, Opn’s top priority was the security of its customers’ confidential information: credit card numbers, account information, and more. But now, the company is focused on diversifying its product line to meet the demands of the future, and has expanded its offerings to include features like Opn Tag, which creates customer digital touchpoints, and services to expand its customers’ e-commerce offerings.

Opn not only provides its clients—including McDonald’s Thailand, Japanese drug store chain Tsuruha, and insurance company Allianz Ayudhya—with the tools they need to connect with millions of potential customers and accept secure payments across multiple devices, it also enables them to connect with those customers through custom-built digital storefronts with online menus and ordering.

Opn first adopted GitHub in 2015 to meet financial regulations. Since Opn handles the data of branded credit cards, including Visa, Mastercard, and JCB, they must obtain and hold a Payment Card Industry (PCI) Standard. This standard was created to increase controls around cardholder data and reduce potential fraud over multiple devices, including phones, tablets, and computers. In other words: make sure credit card numbers don’t end up in the wrong hands.

The PCI Standard prohibited Opn from hosting code on shared servers, so the company chose to self host GitHub Enterprise, enabling them to make pull requests and create issues, boosting developer collaboration while keeping customer data secure. GitHub Enterprise also helped Opn with the PCI audit process, as it can operate on existing infrastructure with established information security controls, allowing the team to determine the specific merge conditions necessary to stay compliant and make audits smoother.

As the company grew from five developers to more than 360, it also evolved its business, including the addition of a professional services team. This team, free from strict PCI requirements, had unique development needs and desired a nimble solution that would limit the burden of maintaining infrastructure and increase developer velocity. They opted for GitHub Enterprise Cloud. This enabled them to free up developer resources and expand its offerings, thanks in large part to GitHub’s compliance, automation, and security features. The professional services team, for example, includes a lean security team which can operate at scale thanks to using both [GitHub Advanced Security](https://github.com/features/security) and [GitHub Actions](https://github.com/features/actions). Now, entire workflows have been automated, and security is embedded within the developer workflow.

Warachet Samtalee, Senior Engineering Manager with the infrastructure team at Opn, says that before Actions, the company maintained and operated its own CI server, but this often meant that the team was distracted with keeping the server running, rather than focusing on the code. “With GitHub Actions, we don’t have to think about the hidden costs of maintaining the CI/CD servers. The workflows are so smooth that the automation works as it should, so developers can focus on communicating with customers and developing new innovations.”

The team had previously tried other tools to automate processes, but “GitHub Actions is easy to use and developers can debug the workflows by themselves, rather than relying on the infrastructure or DevOps teams,” explains Samtalee.

With GitHub Actions, we don’t have to think about the hidden costs of maintaining the CI/CD servers. The workflows are so smooth that the automation works as it should, so developers can focus on communicating with customers and developing new innovations.


Actions quickly became one of the most utilized tools at Opn. “We’ve built an automated CI/CD workflow for any new professional services project,” Samtalee says. “For CI, we offer testing, and for CD we do some environment and workflow approval before deployment.”

In addition to CI/CD, Actions helps the team take security into their own hands. For example, Opn stores container images in AWS using OpenID Connect (OIDC), a keyless method that allows GitHub to connect with AWS using Actions, instead of storing secrets in a GitHub repository.

When it came to selecting a security solution, the choice to use GitHub Advanced Security was a no-brainer, as GitHub was already a central component of Opn’s developer workflow, says Samtalee. “Because our developers already use GitHub for their day-to-day, introducing security scanning as part of the usual workflow was seamless.”

Now, Opn’s developers find security vulnerabilities before they ever have a chance to reach production using both code scanning and features like Dependabot, which examines supply chain vulnerabilities in dependencies. “With GitHub Advanced Security, developers can help themselves,” says Samtalee. “They have the freedom to inherit the organization’s security policy, work and define their project policy standards and decide what level of code scanning they want directly in the repository based on the requirement from the project.”

Because our developers already use GitHub for their day-to-day, introducing security scanning as part of the usual workflow was seamless.


In terms of hiring, the global presence of GitHub has facilitated Opn’s processes in Thailand, Singapore, Japan, and Europe. “A lot of developers already have a lot of experience with GitHub,” says Samtalee. “Everybody knows how it works.” New engineers can get up to speed in less than a day because the GitHub Enterprise virtual appliance includes all required software. “It makes onboarding a piece of cake.”

Once hired, employees from all corners of the world need to efficiently collaborate. With GitHub, engineers can easily work asynchronously. “You just change the code that’s needed and get their approval,” Samtalee says. “Merge, deploy, done.”

For Opn, GitHub is exactly what they needed to meet strict regulations, as well as empower a small team to work more efficiently and focus on delivering a secure and reliable ecommerce experience to its consumers. As the company grows, GitHub has scaled to meet their evolving needs and support a global, distributed workforce. “None of the existing products in the market answered all our development needs,” says Samtalee. “Without GitHub, the developer experience would not be as smooth as it is today.”