source: https://github.com/resources/articles/pipeline

# What is a DevOps pipeline? A complete guide

A DevOps pipeline combines processes, tooling, and automation to enable organizations and software teams to build, test, and deliver high-quality software quickly to end users.


## What is a DevOps pipeline?

A DevOps pipeline is a combination of automation, tools, and practices across the [SDLC](https://github.com/resources/articles/what-is-sdlc) to facilitate the development and deployment of software into the hands of end users. Critically, there is no one-size-fits-all approach to building a DevOps pipeline and they often vary in design and implementation from one organization to another. Most DevOps pipelines, however, involve automation, [continuous integration](https://github.com/resources/articles/continuous-integration) and [continuous deployment](https://github.com/resources/articles/continuous-deployment) (CI/CD), automated testing, reporting, and monitoring.

Important concepts in any successful DevOps pipeline are that it's repeatable, continuous, and always on. Nothing in a DevOps pipeline should be an isolated event but instead comprise a larger system where each step is defined by its repeatability.

Importantly, building a DevOps pipeline is often one of the most tangible elements for organizations looking to adopt [DevOps](https://github.com/resources/articles/what-is-devops), which is defined as much by its cultural dimension that favors deep collaboration as it is by automation and specific tooling.

With the right technology and investments in people and processes, any organization can build an always-on DevOps pipeline—even if it’s a simple one to start. But without fully adopting a DevOps culture that prioritizes incremental development work and deep, cross-functional collaboration across the SDLC, organizations are unlikely to realize the full value of a DevOps pipeline.

## What are the benefits of a DevOps pipeline?

At its most basic, a DevOps pipeline utilizes automated processes and tooling to enable organizations to quickly build, test, and deliver software to end users—and that means the primary benefit of a DevOps pipeline is speed to deployment.

But the best DevOps pipelines also include automated testing suites to balance the speed to deployment with ensuring organizations are shipping high-quality, secure software. This highlights the primary goal of any DevOps practice: to deliver better software faster to end users.

In practice, organizations that successfully design and implement a DevOps pipeline will also commonly experience the following benefits:

### Faster software delivery

A DevOps pipeline is designed to facilitate the faster delivery of value (typically software) to end users through a set of automated processes. through the SDLC, tools that enable organizations to build, test, and ship software at speed, and practices that favor high-pace, incremental code changes. The most common example of this comes via [CI/CD](https://resources.github.com/ci-cd/), which automates the builds, testing, and delivery of software in a DevOps pipeline to enable faster software delivery.

### More reliable and higher-quality software

DevOps pipelines typically apply automated tests throughout the SDLC both for functionality and security—particularly in the case of organizations that embrace [DevSecOps](https://github.com/resources/articles/what-is-devsecops), which builds upon DevOps by prioritizing security. While the end result depends on the level of testing an organization automates and applies to their pipeline, the common benefit you can expect to see after standing up a DevOps pipeline is more reliable and higher-quality software that has been subjected to a consistent set of tests before deployment. **

### Reduced risk

By prioritizing consistently applied, automated testing throughout the SDLC, a DevOps pipeline enables organizations to reduce the risk of issues and bugs making their way into production software. Automation also is often applied to repetitive tasks, which can reduce the risk of human error. This benefit is primarily driven by practices such as CI/CD, which leverage automation to expedite the delivery of software and automated tests to detect potential issues as soon as code changes have been committed to the codebase.

### Automation reduces the need for manual efforts

A core element of any DevOps pipeline is automating tedious tasks that can be better handled by computers. This introduces greater efficiency by reducing the need for manual effort on otherwise time-consuming and repetitive tasks. It also enables organizations to direct resources towards building and shipping software by freeing up one of the most precious asset software teams have: time.

### Shorter review times (and faster resolution times)

In a DevOps pipeline, automated tests are applied at key points within the SDLC—both to assess the functionality and security profile of code changes. Each organization will implement its own unique testing suite, but the net benefit is a DevOps pipeline often results in shorter review times for new code. DevOps pipelines also commonly lead to faster resolution times when issues are identified within code via a combination of continuous monitoring and reporting.

## Stages of the DevOps pipeline

A common way people often explain a DevOps pipeline is by comparison to an assembly line. Each part of the DevOps Lifecycle is analyzed to establish a consistent set of automated and manual processes. The result is improved efficiency and consistency in terms of the overall output.

But unlike an assembly line, DevOps isn’t an end-to-end process with a definite beginning and end. Instead, DevOps is a cycle of continuous improvement where even after software is shipped improvement continues.

In practice, that means that even as a new software feature might take a linear path through stages of development, the overall system (and even that feature) goes through a continuous cycle of iteration.

To understand this, it helps to break down the stages of a DevOps pipeline—and how they feed back into one another.

**1. Plan**

Every DevOps pipeline starts in the planning stage where new features or fixes are introduced and scheduled. At this stage, the primary goal is to ensure people who play different roles within the larger DevOps practice are collaborating from the start—and that means working together to understand user needs, design a solution, understand the implications of the change, and ensure it fits smoothly into the existing system.

**2. Code**

In the coding stage, organizations begin writing code according to the plan and track their work via a version control system such as Git. At this point in a DevOps pipeline, developers may use a number of tools in their development environment to introduce consistency in code styling and identify any potential security flaws. This might include utilizing tools such as a cloud-hosted IDE (integrated development environment), which are often used to introduce consistency across development workflows and increase the speed at which coding environments can be spun up.

**3. Build**

The build stage is when a DevOps pipeline fully kicks into gear and begins once a developer commits code changes to a shared repository. At this point, a developer may submit a pull request to merge their code changes with the codebase. This will alert someone else on the team to review their code before approving the merge. At the same time, a typical DevOps pipeline will initiate an automated build process that merges the codebase and begins a series of integration and unit tests. If any of these tests or the build itself fails, the pull request will also fail and the developer will get a notification about the issue. This level of workflow automation in a DevOps pipeline helps organizations mitigate any potential build integration problems and identify any bugs or security issues at an earlier point in the SDLC.

**4. Test**

After a build is approved, the testing stage in a DevOps pipeline begins and the build will be deployed to a testing environment that closely mirrors the production environment. Some organizations may elect to adopt infrastructure-as-code (IaC) in their DevOps pipeline to automate the provisioning of a testing environment for staging. Others may have dedicated, pre-built testing environments ready for any new build—the choice largely depends on an organization’s needs and computing resources. Once the build is deployed to the test environment, it will be subject to a number of automated and manual tests. This may include automated security tests such as dynamic application security testing (DAST) and interactive application security testing (IAST) to identify any vulnerabilities or risk areas. It can also include manual user acceptance testing (UAT) where team members will use the application and notate any potential problems or bugs a customer may encounter. Every organization will have its own unique automated and manual testing suite and strategy during the test stage in their DevOps pipeline. But this stage, critically, provides a space for organizations to apply their tests without disrupting the development workflow.

**5. Release**

The release stage marks the point in a DevOps pipeline where a new build has been fully tested and is ready to be deployed. In addition to the code itself having been tested, its operational performance has also been cleared leaving organizations confident that it will successfully run in production without being affected by any undiscovered bugs or issues. At this stage, some organizations will elect to automatically deploy code when it reaches this stage in a practice commonly called continuous deployment. This is how some software teams deploy several code changes a day. Others may instead decide to manually release a new build into production and include a final approval stage. And still others will schedule automated releases to happen on certain days or at certain times. CI/CD platforms and other DevOps tools enable organizations to build a release cadence that best works for them—and apply automation throughout the release stage in their DevOps pipeline.

**6. Deploy**

Once a build has been released, it should be ready to deploy into production. At this stage in a DevOps pipeline, organizations will leverage a number of tools to automate the deployment process by provisioning new production environments via IaC or orchestrating a blue-green deployment (this is where code changes are slowly rolled out to a percentage of users in a new environment while the old codebase remains operational for other users in a separate environment). A blue-green deployment strategy also enables organizations to quickly migrate users back to an old build in the event that anything goes wrong.

**7. Operate**

A DevOps pipeline doesn’t end once an application is deployed—that’s when the operational stage begins and organizations need to make sure everything is running smoothly. This stage includes infrastructure orchestration and configuration settings that will enforce rules to automatically scale resources to meet real-time demand. It also will often include mechanisms to capture user activity within the application such as behavioral logging and customer feedback forms. The goal in the operations stage is implied by the name of the stage itself: To successfully operate the application and underlying infrastructure and search out ways to improve the operational profile of the software itself.

**8. Monitor**

Building upon the operational stage of a DevOps pipeline, organizations will set up automated [monitoring tools](https://github.com/resources/articles/monitoring-tools) to identify potential performance bottlenecks, applications issues, and user behavior. This stage requires implementing tooling to collect data on application and infrastructure performance, and then pass actionable items back to the product teams to either resolve outstanding issues or develop new features to support existing user behaviors in the application.
Even though this is the ‘last’ stage of a DevOps pipeline, it’s important to understand that the process itself is continuous—ie, monitoring tools help organizations identify areas for additional planning and iteration to feed back through the DevOps pipeline.

## How do you build a DevOps pipeline? Understanding the core practices

No two DevOps pipelines look precisely the same. That’s because each one reflects the particular needs of the organization it serves. However, there are elements of tooling and process that tend to feature in typical DevOps pipelines.

Those core elements are a mix of process, culture, and tooling and include the following core practice areas:

**Continuous integration (CI)**

When many people work on the same codebase, the difference between each person’s branch of the code grows more and more as they continue to work. The bigger the change, the harder it is to merge it back into the main codebase. CI encourages each person to merge their work frequently back into the main branch. That way, conflicts are easy to spot and each person’s work has less chance of diverging from what their colleagues are doing.

**Continuous deployment**

Continuous deployment builds upon continuous integration by automatically pushing new changes down the pipeline into various environments–shared developer, test, UAT, and yes even production environments–in an automated fashion using a common set of tools. Considered one of the more advanced examples of automations in a DevOps practice, continuous deployment makes it simple for any code commits to move right to production once they pass all necessary pre-defined tests.

**Continuous testing**

When a code commit is made, most DevOps pipelines initiate some form of automatic testing. Regression tests check that the change doesn’t break existing functionality. Unit tests ensure that the code change provides the expected outputs. Functional testing might ask a person to intervene and use the new version of the code. A failed test will halt the pipeline and prevent the code from being merged or deployed.

**Continuous monitoring**

Data is the lifeblood of the DevOps pipeline. Monitoring tools help at each stage but are primarily used in production to give a picture of the application’s health.

Specific DevOps tools enable organizations to stand up these practice areas—for instance, a CI/CD platform is used to build automated workflows to support continuous integration and continuous delivery (or continuous deployment).

But tools alone do not create a successful DevOps pipeline. That requires dedicated resources to plan out the ideal SDLC, determine key areas that can be automated to improve the speed and quality of deployments, a strategic automated testing suite, and a culture that prioritizes deep collaboration between different roles throughout the SDLC.

[DevOps automation](https://github.com/resources/articles/what-is-devops-automation), delivered

Spend more time on the code that matters—and less on the tasks that slow your developers down. With tools like GitHub Actions and Packages, GitHub makes powerful CI/CD and automation part of your entire DevOps pipeline.

#### PLAN

Coordinate, manage, and update your work in one place with GitHub issues, discussions, and project boards. Then stay organized and on track by integrating the planning and project management tools you already use.

[Explore project management tools](https://github.com/marketplace?category=project-management)

#### CODE

Collaborate, create, store code, and accelerate development with GitHub and Codespaces. Add in code quality integrations to automate [code reviews](https://github.com/resources/articles/how-to-improve-code-with-code-reviews) for style, quality, security, and test‑coverage checks when you need them.

#### BUILD

Ship faster with automated continuous integration powered by [GitHub Actions and Packages](https://github.com/features/actions). Trigger workflows based on GitHub events and publish your packages wherever you like, all with native tooling commands.

Explore [mobile CI](https://github.com/marketplace?category=mobile-ci), [container CI](https://github.com/marketplace?category=container-ci), or all [CI tools](https://github.com/marketplace?category=continuous-integration)

#### TEST

Stop bugs from getting to production by adding testing to your Actions workflows—including testing integrations from our partners and community.

#### DEPLOY

Automate continuous delivery with Actions or trigger deployment integrations from common CI/CD providers and major public clouds with GitHub any event.

#### MANAGE

Connect your code to the management, logging, alerting, and monitoring tools your team uses in production. Easily measure impact, analyze performance, and monitor the impact of your code on your systems and users.

[Explore analytics, alerting, logging and monitoring tools](https://github.com/marketplace?category=monitoring)

#### SECURE

Know your code stays secure at every step with [CodeQL](https://securitylab.github.com/tools/codeql), [Dependabot](https://docs.github.com/en/free-pro-team@latest/github/managing-security-vulnerabilities/configuring-github-dependabot-security-updates), and the security tools you use today.

Explore [security](https://github.com/marketplace?category=security) and [dependency management](https://github.com/marketplace?category=dependency-management) tools

## Join the world’s best teams