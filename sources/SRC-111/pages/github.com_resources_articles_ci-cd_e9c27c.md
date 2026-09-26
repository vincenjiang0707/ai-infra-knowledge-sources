source: https://github.com/resources/articles/ci-cd

# What is CI/CD?

Building automated workflows for faster releases

## What is CI/CD?

CI/CD stands for Continuous Integration and Continuous Deployment (or Continuous Delivery). It's a set of practices and tools designed to improve the software development process by automating builds, [testing](https://github.com/resources/articles/what-is-software-testing), and deployment, enabling you to ship code changes faster and reliably.

### Continuous integration (CI)

Automatically builds, tests, and integrates code changes within a shared repository

### Continuous delivery (CD)

Automatically delivers code changes to production-ready environments for approval

### Continuous deployment (CD)

Automatically deploys code changes to customers directly

CI/CD comprises of continuous integration and continuous delivery or continuous deployment. Put together, they form a “CI/CD pipeline”—a series of automated workflows that help DevOps teams cut down on manual tasks.

### Example of a CI/CD pipeline

## Continuous delivery vs. continuous deployment

When someone says CI/CD, the “CD” they’re referring to is usually continuous *delivery*, not continuous *deployment*. What’s the difference? In a CI/CD pipeline that uses continuous delivery, automation pauses when developers push to production. A human—your operations, security, or compliance team—still needs to manually sign off before final release, adding more delays. On the other hand, continuous deployment automates the entire release process. Code changes are deployed to customers as soon as they pass all the required tests.

Continuous deployment is the ultimate example of [DevOps automation](https://github.com/resources/articles/what-is-devops-automation). That doesn’t mean it’s the only way to do CI/CD, or the “right” way. Since continuous deployment relies on rigorous testing tools and a mature testing culture, most software teams start with continuous delivery and integrate more automated testing over time.

## Why CI/CD?

The short answer: Speed. The [State of DevOps report](https://cloud.google.com/blog/products/devops-sre/the-2019-accelerate-state-of-devops-elite-performance-productivity-and-scaling) found organizations that have “mastered” CI/CD deploy 208 times more often and have a lead time that is 106 times faster than the rest. While faster development is the most well-known benefit of CI/CD, a continuous integration and continuous delivery pipeline enables much more.

### Development velocity

Ongoing feedback allows developers to commit smaller changes more often, versus waiting for one release.

### Stability and reliability

Automated, continuous testing ensures that codebases remain stable and release-ready at any time.

### Business growth

Freed up from manual tasks, organizations can focus resources on innovation, customer satisfaction, and paying down technical debt.

## Building your CI/CD toolkit

Teams make CI/CD part of their development workflow with a combination of automated process, steps, and tools.

### Version control

CI begins in [shared repositories](https://github.com/resources/articles/what-are-code-repositories), where teams collaborate on code using version control systems (VCS) like Git. A VCS tracks code changes, simplifies reversions, and supports config as code for managing testing and infrastructure. Learn more about [version control](https://github.com/resources/articles/what-is-version-control)

### Builds

CI build tools automatically package up files and components into release artifacts and run tests for quality, performance, and other requirements. After clearing required checks, CD tools send builds off to the operations team for further testing and staging. [Learn more about CI testing](https://github.com/resources/articles/continuous-integration)

### Reviews and approvals

Treating code review as a best practice improves code quality, encourages collaboration, and helps even the most experienced developers make better commits. In a CI/CD workflow, teams review and approve code or leverage integrated development environments for pair programming. [Learn more about code review](https://github.com/resources/articles/how-to-improve-code-with-code-reviews)

### Environments

CI/CD tests and deploys code in environments, from where developers build code to where operations teams make applications publicly available. Environments often have their own specific variables and protection rules to meet security and compliance requirements. [Learn more about protected environments](https://docs.github.com/en/actions/reference/environments)

## Example CI/CD workflow

CI/CD doesn’t have to be complicated, or mean adding a host of tools on top of your current workflow. At [mabl](https://github.com/readme/walking-the-walk-bringing-end-to-end-automation-and-testing-to-internal-teams), developers deploy to production about 80 times a week using only two CI/CD integrations: The mabl testing suite and GitHub Actions. Here’s how it works. ✨

Developers open pull requests to trigger initial builds and unit tests

Approved commits are deployed to a preview environment

Custom-built GitHub Actions install the mabl CLI and run headless tests

GitHub Apps provide live check results within pull requests

Approved commits are merged to the main branch for additional tests or deployed to production


## What makes CI/CD successful

You’ll find different tools and integrations everywhere you look, but effective CI/CD workflows all share the same markers of success.

### Automation

CI/CD *can* be done manually—but that’s not the goal. [A good CI/CD workflow](https://github.com/readme/guides/transforming-productivity-with-a-whole-product-ci-cd-pipeline) automates builds, testing, and deployment so you have more time for code, not more tasks to do.

### Transparency

If a build fails, developers need to be able to quickly assess what went wrong and why. Logs, visual workflow builders, and deeply integrated tooling make it easier for developers to troubleshoot, understand complex workflows, and share their status with the larger team.

### Speed

CI/CD contributes to your overall DevOps performance, particularly speed. DevOps experts gauge speed using two [DORA metrics](https://cloud.google.com/blog/products/devops-sre/another-way-to-gauge-your-devops-performance-according-to-dora): Lead time for changes (how quickly commits are made to code in production) and deployment frequency (how often you commit code).

### Resilience

When used with other approaches like test coverage, observability tooling, and feature flags, CI/CD makes software more resistant to errors. DORA measures this stability by tracking mean time to resolution (how quickly incidents are resolved) and change failure rate (the number of software rollbacks).

### Security

[Automation includes security](https://www.youtube.com/watch?v=G5YQJdOhaZM). With DevSecOps gaining traction, a future-proof CI/CD pipeline has checks in place for code and permissions, and provides a virtual paper trail for auditing failures, security breaches, non-compliance events.

### Scalability

CI/CD isn't just about automation; it's also about ensuring scalability. A robust CI/CD setup should effortlessly expand with your growing development team and project complexity. This means it can efficiently handle increased workloads as your software development efforts grow, maintaining productivity and efficiency.

## See What's Possible with CI/CD: Real Customer Stories

See how DevOps teams put continuous automation into practice.

**Blue Yonder**: Migrating from internal servers to cloud-based CI/CD.[Explore Blue Yonder](https://github.com/customer-stories/blue-yonder)**Plaid**: Improving deployment time and developer productivity.[Explore Plaid](https://github.com/customer-stories/plaid)**3M**: Breaking down silos with shared tooling and automation.[Explore 3M](https://github.com/customer-stories/3m)

## What can you do with CI/CD?

Whether you’re ready to dive in or still have questions, we’ve got you covered.

**Explore best practices**: Explore best practices [Learn more](https://resources.github.com/)

**Get a GitHub demo**: See how world-class CI/CD, automation, and security can support your workflow. [Request a demo](https://resources.github.com/devops/ci-cd/#form)

**Ask the experts**: Build a custom strategy for your business goals in a 1:1 session with GitHub product leaders. [Schedule a virtual briefing](https://github.com/enterprise/contact/)

**Compare DevOps solutions**: See how GitHub compares to other DevOps tools and platforms. [Learn more](https://resources.github.com/devops/tools/compare/)