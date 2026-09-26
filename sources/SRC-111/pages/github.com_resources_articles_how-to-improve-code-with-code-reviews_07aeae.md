source: https://github.com/resources/articles/how-to-improve-code-with-code-reviews

# How to improve code with code reviews

Learn about code reviews and gain insights into how they’re essential to increasing code quality. See how code review tools, including AI-powered tools, help development teams streamline the code review process, identify issues, and help developers ship great software faster.

## What is a code review?

A code review is a process where one or more developers review code that another developer wrote. During code review, developers evaluate the code to make sure that it's ready to merge into the codebase. On GitHub, this evaluation happens through [pull requests](https://docs.github.com/pull-requests/reference/pull-requests), which let reviewers comment on and approve proposed changes before they merge. To help ensure quality, there must be at least one code reviewer who didn't participate in authoring the code.

The purpose of a code review in [software development](https://resources.github.com/software-development/what-is-software-development/) is to help ensure that the code meets the organization's standards and requirements, is of high quality, and is maintainable. In addition to identifying errors and bugs, code reviews also promote a culture of learning and collaboration among the development team.

## Benefits of code reviews

Also known as peer reviews, code reviews help development teams:

### Increase code quality

Identifying defects in the code and issues such as [security vulnerabilities](https://docs.github.com/code-security/concepts/code-scanning/code-scanning) and performance problems—before developers merge the code into an upstream branch.

### Ensure compliance

Ensure compliance with organizational standards, regulations, and the team's code style.

### Save time and money

Detect issues earlier in the software development process before they become more complex and expensive to fix.

### Boost collaboration, communication, and knowledge sharing

Boost collaboration, communication, and knowledge sharing among developers by providing a forum to discuss code and ask questions, share ideas and best practices, and learn from each other.

### Ensure that the code is maintainable

Identifying any software maintenance issues and suggesting improvements.

## Code review challenges

Although many development teams successfully conduct code reviews, there are some challenges. Code reviews can be:

### Time-consuming

Code reviews can be time-consuming especially if the codebase is large. Code reviewers need to spend time reading and understanding the code, which might impact their other projects.

### Subjective

Code reviews can be subjective, since different reviewers might have different opinions on what constitutes good code. Negative feedback might lead to conflicts between team members.

### Costly

Code reviews can be costly especially if developers manually review the code without using any [code review tools](https://github.com/resources/articles/what-is-code-scanning). Code reviews might be expensive for small teams or startups.

## Code review process

Code reviews typically take place before the testing phase of the [software development lifecycle](https://resources.github.com/software-development/what-is-sdlc/). Common steps in the code review process include:

### 1. Preparing code:

The code author prepares the code for review by making sure that it's complete, [well-documented](https://github.com/resources/articles/tools-and-techniques-for-effective-code-documentation), and complies with the organization's coding standards.

### 2. Requesting peer reviews:

The code author submits the code for review to one or more code reviewers. Code review best practices require that more senior developers review code written by junior developers. In large development teams, several developers might be dedicated to code reviews.

### 3. Reviewing code:

Code reviewers examine the code, point out any bugs, issues, or architectural flaws, and suggest improvements, typically by adding comments to the code. Reviewers can also rely on [secret scanning](https://docs.github.com/en/code-security/getting-started/github-security-features) to catch hardcoded credentials before they merge into the codebase. They may use checklists that might include some of these questions:

1. Is the code clear and easy to understand?

2. Does the code follow the team's coding standards and guidelines?

3. Are there any potential:

Performance issues?

Maintainability issues?

Compatibility issues?

Scalability issues?

Usability issues?

Accessibility issues?

Localization issues?

Legal or compliance issues?

Testability issues?

Documentation issues?


### 4. Discussing comments:

The code author and code reviewers discuss any comments left by reviewers. When code authors don't agree with a specific comment, they need to successfully defend their position or correct the code to resolve the issue.

### 5. Approving code:

After all the comments are addressed, the reviewers approve the code, and it's merged into the codebase.

## Types of code reviews

Code review practices vary depending on the size of the development team and the team's tools, workflow, and processes. Formal code reviews involve detailed processes with several participants and phases, including meetings where every line of code is reviewed. Also known as Fagan inspections, these detailed group reviews are highly effective in finding code issues and defects.

Development teams might use other processes for code reviews, such as:

### Over-the-shoulder code reviews

Also known as synchronous code reviews, over-the-shoulder code reviews take place when a code reviewer and the code author look at the code together by reviewing it on the screen at the same time.

### Pair programming

Also known as instant code review, pair programming takes place when two developers work together—one writes code and the other checks it as it's written to give instant feedback.

### Asynchronous code reviews

These allow reviewers to review the code independently at their own pace. The review request might be passed around by emails sent by the code author or the source code management system. This type of code review is well-suited for teams working remotely or in different time zones.

### QA code reviews

These include one or more quality assurance team members. The quality analyst doesn't need to have coding experience to participate. It's helpful to pair the quality analyst with an experienced developer, so they can review the code together.

### Tool-assisted code reviews

These take place when the team uses one or more code review tools to help improve code quality and reduce the time spent on reviews.

## Code review tools

There are several code review tools available that help development teams streamline and improve a manual code review process. For example, [GitHub code review tools](https://github.com/features/code-review) include lightweight tools built into GitHub, such as:

### Pull requests.

Developers use pull requests to propose new features or changes to existing code. The pull request becomes a base for the team to refine changes and discuss implementation details before changing the source code.

### Code update tools.

These tools empower developers to see a history of changes related to a pull request, preview code changes side-by-side with the original code to make it easy to identify the differences, and see what a file looked like before a particular change.

### Code discussion tools.

A comments tool allows developers to ask questions about structure inline and leave detailed comments about code syntax. A review requests tool makes it easy for code authors to add code reviewers to their pull request. With the reviews tool, developers can bundle their comments into one cohesive review and specify whether comments, changes, or suggestions are required.

### Merge conflicts.

A merge conflict happens when competing changes are made to the same line of a file. The GitHub conflict editor resolves simple merge conflicts, so developers don't need to use the [command line](https://github.com/resources/articles/what-is-a-cli) to resolve the conflict.

### Taking code review to the next level with AI

AI-powered [code review](https://github.com/resources/articles/ai-code-reviews) tools help automate and speed code review processes by analyzing code and identifying issues. They also help improve code quality by highlighting issues that the code reviewers might have missed.

[AI coding tools](https://resources.github.com/artificial-intelligence/ai-coding-tools/) give developers AI-based suggestions in real-time as they're writing code. For example, as developers type, [GitHub Copilot](https://github.com/features/copilot) suggests code completions and turns natural language prompts into coding suggestions based on style conventions and context. In addition, [GitHub Copilot for Pull Requests](https://githubnext.com/projects/copilot-for-pull-requests) helps developers write better pull request descriptions and helps development teams review and merge pull requests faster.

## Summary

Code reviews identify defects in the code and issues such as security vulnerabilities and performance problems. They are a critical part of [collaborative software development](https://github.com/resources/articles/innersource) because they help developers merge the highest quality code into the code base. In addition to improving code quality, code reviews help ensure compliance with standards and promote learning and collaboration among development team members.

By identifying issues early in the software development process when they're easier to fix, code reviews help development teams save time and money. Development teams use code review tools, including AI-powered tools, to improve the process and help them deliver better code faster. Code review tools streamline code review and identify issues that the code reviewers might have missed.

## Explore other resources

## Frequently asked questions

### How are code reviews done?


The code author prepares the code for review and makes sure that it’s complete, well-documented, and complies with the organization’s coding standards. One or more code reviewers examine the code, suggest improvements, and point out any bugs, issues, or architectural flaws. The code author and code reviewers discuss the issues and once they’re resolved, the code is merged into the codebase.

### What are the different types of code review?


Formal code reviews involve detailed processes with several participants and phases, including meetings where every line of code is reviewed. Development teams might opt for using specific tools or processes for their code reviews, which are also effective and take less time and resources. Examples include synchronous or instant code reviews, where the code author and reviewer work together to identify code issues as the code is written, and asynchronous code reviews, where the code author sends the code out for code reviewers to examine independently. With tool-assisted code reviews, the team uses software tools to help improve code quality and reduce the time spent on reviews.

### What is a QA code review?


A QA code review includes a quality assurance team member. The QA team member does not need to have coding experience to participate. It’s helpful to pair the quality analyst with an experienced developer, so they can review the code together.

### What are code review best practices?


Some examples of best practices that can be implemented for code review include having senior developers review code written by more junior developers, using a code review checklist, and taking advantage of code review tools to streamline the process and help developers merge the highest quality code into the codebase. Development teams might also take code review to the next level with AI-powered tools that review code as it’s written, provide suggestions for improvement ,and highlight issues that the code reviewers might have missed.