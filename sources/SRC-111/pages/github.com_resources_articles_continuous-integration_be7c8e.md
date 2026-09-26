source: https://github.com/resources/articles/continuous-integration

# The fundamentals of continuous integration in DevOps

What is continuous integration in DevOps? Continuous integration (CI) is a foundational DevOps practice where development teams integrate code changes from multiple contributors into a shared repository.

## Continuous integration defined

What is continuous integration in DevOps? Continuous integration (CI) is a foundational DevOps practice where development teams integrate code changes from multiple contributors into a [shared repository](https://github.com/resources/articles/what-are-code-repositories). Automation is used throughout this process to merge, build, and test code to facilitate a higher speed of software development. This process is often called a CI pipeline. When implemented properly, CI enables organizations to quickly identify defects and ship higher-quality software faster.

At its core, DevOps seeks to increase the speed of software releases while ensuring a reliable and secure end product—and CI is integral in accomplishing this.

CI is a cultural practice that encourages developers to regularly merge their code into a shared repository. But CI is also a technical process, where a mixture of automation and tooling are used to increase the speed that code changes are integrated, tested, and prepared for deployment.

## This guide will cover:

Why continuous integration is needed

Continuous integration best practices

The benefits of continuous integration

How a continuous integration pipeline works

How to build a successful continuous integration pipeline


## Why is continuous integration needed?

CI seeks to encourage faster and more efficient development cycles by solving a key problem in software development: managing code integration challenges in a shared repository with multiple contributors.

When a developer begins working on a software update or fixing a bug, they make a copy of the codebase to work from. This is done via a [version control system such as Git](https://github.com/git-guides), which enables developers to create a copy of, or “fork,” the codebase.

As more developers create codebase copies, integrating the changes from multiple contributors can become challenging—especially when the codebase that one developer started working from becomes dated and no longer matches the main repository.

In a worst-case scenario, it can take longer to successfully integrate code changes than to make the changes themselves as each developer tries to untangle where their code is not matching up. Developers often call this “integration hell.”

CI seeks to prevent this by encouraging developers to integrate changes as they make them. CI also leverages automation to increase the speed at which code is integrated and tested to ensure no additional changes are needed, reducing the burden for a developer. This combination of more frequent code integrations and automated builds and testing helps speed up the software development process.

## Best practices when adopting continuous integration

Every company will define its CI practice per its unique needs. Some companies may introduce more rigorous automated [security tests](https://github.com/resources/articles/what-is-security-testing); others may prioritize fast code merges and reserve more time-consuming automated tests for later in the software development lifecycle (SDLC).

Despite this, effective CI pipelines share a set of common [tools](https://resources.github.com/devops/tools/) and best practices. These include:

### A shared code repository

A shared code repository in a [version control](https://github.com/resources/articles/what-is-version-control) system is foundational to creating an effective CI practice. Beyond serving as a place to store code, scripts, automated tests, and everything in between, version control systems also enable developers to create multiple branches from which to work.

### Regular code commits

Automation, testing, and tooling are important to creating an effective [pipeline](https://resources.github.com/devops/pipeline)—but without a team cultural shift that prioritizes committing code changes often, you’re unlikely to get very far. There are no hard and fast rules for how often developers should be committing code. A good rule of thumb, however, is that the more often individuals commit changes, the more productive the development environment will be.

### Build automation

Build automation is a critical component of a CI pipeline and enables teams to standardize their software builds. A typical build process includes compiling source code, generating software installers, and ensuring that all the necessary items are in place to support a successful deployment. In a CI practice, this process is automated to help integrate incremental code commits into the codebase.

### Automated testing

You can make lots of code commits and have a fully automated build process. But just because a program runs, it doesn’t mean it’s running correctly. That’s where testing comes in. Automated testing is a key part of CI pipelines. Each commit triggers a set of tests to identify bugs, security flaws, and commit issues. These tests are meant to keep the main code branch operational, or “green,” and give rapid feedback to developers about the efficacy of their code changes.

## The benefits of continuous integration

At its most effective, CI enables organizations to build software faster, release more reliable software, and improve overall business health.

But those are high-level advantages for an organization overall. In practice, you can expect several material benefits when you adopt CI. These include:

### Faster code changes

Since CI prioritizes frequent code commits, organizations often see an improvement in the speed of work from their development teams. Each developer is working on a smaller part of a given piece of software in tandem with other team members. And since CI calls for regular, small code changes instead of larger code updates, this makes it simpler to integrate, test, and ultimately ship code to end users.

### Improved testing reliability

Organizations that successfully adopt CI typically report greater testing reliability. This is because testing becomes a continuous and routine part of their software development lifecycle. When tests fail, it either indicates flaws with the software or that the test itself needs to be rewritten. By having more reliable tests, CI pipelines can better facilitate a faster speed of development, code integration, and software releases.

### Fault isolations

Fault isolation is a technical concept where developers build systems that minimize the scope and damage of any potential problems. The use of fault isolations in CI pipelines is a common practice and benefit. Developers will often combine automated testing with fault isolation and system [monitoring](https://resources.github.com/devops/tools/monitoring) to prevent larger software failures in the build stage, and make each issue easier to fix.

### Improved mean time to resolution (MTTR)

MTTR is a measurement of how long it takes to fix a coding error. Teams practicing good [DevOps](https://resources.github.com/devops/fundamentals/) procedures can use MTTR to gauge how successful they are in maintaining uptime and resolving issues that lead to system failures. Since CI practices favor small, incremental code changes, businesses that adopt CI pipelines often see improved MTTR measurements and improved uptime performance (typically in conjunction with automation deployments).

### Faster software release rates

With improved testing, MTTR, and the use of fault isolations to limit the scope of potential errors, CI pipelines typically result in faster software release rates. To truly guarantee this however, organizations need to successfully implement CI both culturally by encouraging more frequent code commit rates and technologically by automating testing and creating a full CI pipeline. Part of this is creating a production environment identical to what customers will be using to test individual software releases.

### Shorter backlogs of non-critical bugs

CI pipelines can reduce the number of non-critical bugs that hit production by identifying them via automated testing before a software release. In doing so, developers have an opportunity to fix these bugs as well as reduce future bug backlogs and [technical debt](https://github.com/resources/articles/what-is-technical-debt). This allows developers to focus more on larger feature updates instead of backlogged issues.

### Better team communication

The best CI pipelines leverage continuous testing, monitoring, and reporting to generate a stream of continuous feedback, which is used to improve software stability. Continuous feedback also helps improve team communication and lines of accountability to solve issues as they arise.

### Lower organizational costs

CI pipelines rely extensively on automation, which typically results in reduced organizational costs. A common saying in DevOps circles is whatever can be automated, should be automated. As a cultural and technical practice, automation in CI pipelines reduces the risk of human error. It also frees up organizational resources to work on building code instead of testing existing code.

## How does a continuous integration pipeline work?

A CI pipeline focuses on the first three stages of the [software development lifecycle](https://github.com/resources/articles/what-is-sdlc) (SDLC): build, test, and release. By introducing automation and monitoring to these first three stages, CI speeds up the SDLC and helps organizations deploy more reliable software.

Of course, it is possible to *manually* build, test, and release software. The true advantage of CI, however, is that it applies automation to each of these steps.

## Stages of a CI pipeline

### 1. Build

This is the stage at which an application is compiled. In a CI pipeline, automation is used to trigger a build cycle once a developer commits code changes to the main repository. From here, a CI tool will query a project’s build tools to begin compiling the application in a clean staging environment. [Containers](https://github.com/resources/articles/containerization) are a popular and lightweight way organizations often use to spin up fresh build environments at this stage.

### 2. Test

After an application is compiled, a series of tests are run to ensure the code works and there are no bugs or critical issues. Organizations will configure their CI tool to automate these tests to begin once the application compiles. Unit tests, which are a way of testing small units of code, are a popular type of test at this stage due to the ease it takes to write them and their low cost to run and maintain. The goal at this stage of the CI pipeline is to ensure that the codebase passes inspection.

### 3. Package

Next, an organization will begin packaging its code. In a CI pipeline, these steps are automated and triggered once unit testing is complete. The way each organization will package its code will depend on the programming language and production environment. An organization that is using JavaScript and Docker containers, for instance, might use npm and Docker images to package its code.

## How to start building a successful continuous integration pipeline

First, a truism: No two CI models are alike. Every organization will implement CI according to its unique needs and team requirements.

There are, however, some common steps every organization needs to take to implement CI successfully. These break down into seven practices:

### 1. Create a testing strategy

Every CI practice starts with a cogent and clear testing strategy. You’ll need to consider what types of tests you’re running, what triggers you use to build your automated testing sequences, and which tests you apply to each coding branch your development teams will work on.

There are three types of tests that are commonly used in a CI pipeline:

#### Unit tests

Unit tests are simple tests that validate whether individual functions work within a piece of code.

#### Integration tests

Integration tests ensure that code changes integrate cleanly with the larger codebase.

#### Acceptance tests

Acceptance tests verify that an application meets functional requirements. Some of these tests are more narrowly called UI tests, which validate expected UI functionalities a user will encounter.

You don’t need to start with all three types of tests. Most organizations will start with unit and integration testing and build up to writing acceptance tests.

### 2. Choose a CI tool

Choosing a CI platform is a critical part of building a CI model in any organization. This is the tool that will trigger your automated builds, tests, packages, and releases.

You’ll want to ask several questions when selecting a CI platform. These include:

#### How well does it integrate with your current technology stack?

From your programming languages to your version control system to your third-party tools, a CI platform should easily integrate with everything in your stack. It’s also worth considering any future technologies you might adopt and look for a platform that can grow with you.

#### Does it offer native support for containers?

Containers are a critical part of a DevOps and CI practice, and making sure your CI platform has native support for [container](https://github.com/resources/articles/containerization) applications such as Docker is critical. You might not leverage containers today, but as you grow your DevOps practice there’s a good chance you will end up using containers in some capacity.

#### Does it enable matrix build testing capabilities?

Matrix builds enable you to simultaneously test builds across multiple operating systems and runtime versions. Look for a CI tool that has native support for matrix builds, which help streamline your testing and ensure your application will work for all of your end users.

#### Does it offer built-in code coverage and testing visualization?

Code coverage and testing visualization give you a simple way to see how much of your codebase is currently being tested and how existing tests are running in real time and have run historically.

#### How does it map to your security requirements?

Security is a critical consideration with any technology investment—especially if that investment will end up deeply integrated with your codebase and core services.

### 3. Integrate code as soon as possible

Successfully adopting CI starts with making sure your developers are integrating their code as soon as possible to a shared repository.

#### There are two benefits to this:

You avoid larger integration conflicts that can arise when merging older branches back to the main repository.

You end up regularly integrating smaller code changes, which helps with knowledge transfer between your teams and simplifies your testing regimen.


You should also consider what your existing SDLC looks like today, and what changes you might want to make procedurally moving forward as you implement a CI pipeline. This isn’t a conversation about whether feature branching or trunk-based development is better either. Instead, it’s about making sure you have an organized development workflow that facilitates a steady stream of coding, testing, merging, and reviewing.

### 4. Fix your main branch as soon as it breaks

Here’s a good rule of thumb: You should fix your main branch as soon as it breaks.

In a CI model, your developers should be integrating code changes as soon as possible. That’s a good thing. But if a code change breaks your main branch and your developers keep adding more changes, it becomes difficult to identify what caused the initial failure.

To do this, write tests that immediately notify developers when one of their code changes breaks the main branch. This helps create a feedback loop, which is an important DevOps practice.

Make sure to balance testing speed with testing coverage when it comes to keeping your builds green, or operational. If your tests take too long to run, it becomes harder to pinpoint what code change led to a failure. The best testing suites start with simple tests to start such as build and integration tests before advancing to more time-consuming tests.

### 5. Build new tests for every new feature you introduce

Under a CI model, your testing suite should grow with your software or application. That means that as you build new features and prepare larger updates, you should also be building tests to validate these features.

Consider writing tests as you build new features and fix bugs. This might feel time consuming—but going back after the fact will almost certainly take longer than writing tests as you build code.