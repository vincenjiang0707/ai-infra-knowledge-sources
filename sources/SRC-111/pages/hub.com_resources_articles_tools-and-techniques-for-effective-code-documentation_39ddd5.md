source: https://github.com/resources/articles/tools-and-techniques-for-effective-code-documentation

# Tools and techniques for effective code documentation

Get a comprehensive overview of code documentation and learn why it’s essential for delivering quality software. Gain valuable insights into best practices, strategies, and tools for well-documented code, including how AI helps developers write code documentation more efficiently.

## Introduction to code documentation

Code documentation is written information that accompanies software source code to help developers understand its purpose, how it works, and how to use it. Good code documentation makes it easier for developers to maintain and update code and collaborate on [software development](https://resources.github.com/software-development/what-is-software-development/) projects.

There are different types of code documentation:

**Inline code comments**describe what the line or block of code does. Inline comments are added next to or within the code and are typically written in the same language as the code itself. They also describe what a specific method or function does, and its parameters, and return values.

**High-level documentation**includes project specifications, system architecture, business logic, user manuals, and other project-level resources.

**Walkthrough documentation**is designed for developers who contribute to the code and need information about the codebase, such as its patterns and flaws.


## Code documentation benefits

It's important for developers to document their code accurately, consistently, and clearly to help ensure software quality. Good coding documentation:

**Helps development teams understand, improve, and maintain the software.**Code documentation is key to the

[software development lifecycle (SDLC)](https://resources.github.com/software-development/what-is-sdlc/). Developers and testers use code documentation to help them optimize performance, refractor the code, troubleshoot problems, and test and update the code. Code documentation also simplifies the debugging process by providing a reference point to help developers pinpoint the cause.**Improves collaboration.**Good code documentation makes it easier for the development team to communicate more effectively and share code externally with customers and partners. It also makes it easier for the team to onboard and train new hires.

**Saves time.**While poorly documented code might raise questions and cause misunderstandings, well-documented code helps developers save time clarifying, explaining, and supporting the codebase. Well-documented code is also more reusable than poorly documented code, so it helps speed software development.

**Supports compliance.**Organizations use code documentation to help them demonstrate the completeness of the code and how it meets standards, complies with regulations, and aligns to industry best practices.


## Fundamentals of code documentation

**Writing clean, quality code**

A key step to creating good code documentation is to write clean, quality code. Clean code is simple and concise, and easy to read, understand, and modify. The cleaner the code, the less documentation is needed to explain the code and how it works.

**The "Don't repeat yourself" (DRY) principle**

This clean code principle emphasizes that code should not include redundant or duplicated information. The core concept of DRY is to have a single, authoritative representation of knowledge within each system. By eliminating duplicated code documentation, the DRY principle makes the codebase easier to understand and maintain.

**Descriptive naming**

To write clean code, it's important to clearly and descriptively name functions and variables. As a best practice, developers should choose descriptive variable names that accurately represent the purpose of each variable. Developers shouldn't need to leave comments in the code to describe or explain the variable names.

**Logical codebase architecture**

A logical codebase architecture helps developers write clean code by separating the codebase into distinct layers, each with its own responsibilities. This keeps the codebase organized and makes it easier for developers to understand its dependencies and structure.

## Code documentation tools and techniques

**Choosing the right code documentation tools**

Development teams can choose from various frameworks and tools to help them generate and maintain code documentation. Some tools offer automated document generation, which extracts information from source code to generate code documentation and automatically update it after code changes.

It's important for development teams to choose a tool that works with their codebase. For example, Javadoc is a popular documentation tool for Java codebases and Sphinx is a documentation tool that's primarily used for Python codebases.

Choosing the right tool to share code documentation is another key decision. Development teams might use code repositories, shared files with annotated code snippets, or a static site hosting service such as [GitHub Pages](https://github.blog/2016-08-22-publish-your-project-documentation-with-github-pages/).

GitHub Pages is an excellent choice for developers whose code lives in GitHub because their documentation will live alongside their code. Developers can automatically deploy code documentation to GitHub Pages with [GitHub Actions](https://github.com/features/actions), a continuous integration and continuous delivery [(CI/CD)](https://resources.github.com/ci-cd/) platform that automates the build, test, and deployment pipelines. Developers might also use [GitHub code review tools](https://github.com/features/code-review), including Issues and Pull Requests, to create review processes that improve the quality of their code.

**Documenting while coding**

Documentation as Code (Docs as Code) is a practice where developers use the same tools for both writing and documenting code. For example, [GitHub Copilot](https://github.com/features/copilot) is an AI-powered tool that helps developers write both code and documentation more efficiently. When writing code, Copilot provides suggestions for function definitions, code snippets, and even entire classes based on the context of the code. Developers also use Copilot to get autocomplete style suggestions when they're writing documentation.

Here's a Copilot code documentation example with the suggestion shown in gray font.

To see how to write documentation with Copilot suggestions, [watch the short demo video.](https://learn.microsoft.com/en-us/shows/introduction-to-github-copilot/how-to-write-documentation-with-copilot-suggestions-5-of-6)

To learn more about GitHub Copilot and AI, visit the [GitHub Copilot Trust Center.](https://resources.github.com/copilot-trust-center/)

**Utilizing code comments**

The purpose of code comments is to make the source code easier to understand by adding more context or providing an explanation. Developers also use comments to help them with code reviews, maintenance, fixing bugs, and refactoring.

It's important that developers write clear, concise comments and avoid personal remarks and jargon. Developers should also avoid writing redundant and unnecessary comments, which make the code more difficult for others to read and understand.

## Best practices in code documentation

**Write detailed, clear documentation**that's easy to understand, uses simple language, and illustrates concepts with code snippets or examples. Avoid complex explanations and technical terms that other developers don't understand.**Use consistent naming conventions,**especially for classes, functions, variables, files, and directories. This makes it easier for several developers to work on the same codebase., which is a guide to the project that provides a project description, instructions to help users get started, and guidelines for contributing to the project.**Include a README file****Explain coding decisions**and how they impact the codebase. Helping other developers understand the reasoning behind coding choices proactively answers their questions and reduces the possibility of misunderstandings.

## Strategies and methodologies

**Develop a code documentation strategy.**This includes identifying the audience for the documentation and understanding their needs, choosing tools for creating and managing the documentation, and defining standards such as naming conventions. In addition, it's important to define how code documentation is integrated into the software development process, and how the documentation will be maintained and updated.**Incorporate****agile****practices in documentation**. Agile is a process for software development that focuses on meeting customer business requirements by building a minimum viable product. Although the agile method values working software over comprehensive documentation, it emphasizes that projects should provide the key information needed to understand how the software was developed and how it should be used. Agile also emphasizes that code documentation should be developed during the project lifecycle, not after the software is completed.**Write for humans first.**Humans are the most important audience for code documentation. When documenting code, developers should ask themselves if their comments will help others better understand the code and make it easier to maintain. If not, they should revisit their code comments to make them clearer and more concise.**Encourage collaboration and feedback.**Developers should be expected to review and provide feedback on each other's code documentation. Adding documentation review sessions to the software development process, especially code reviews, will help improve the quality of documentation and help ensure that all developers have the same understanding of the codebase.

## Maintaining and updating code documentation

Keeping documentation up to date is critical for maintaining code quality. If the documentation doesn't reflect the current state of the codebase, then it needs to be updated, either manually or automatically. Strategies that make it easier to accomplish this include:

Using a documentation generation tool that automatically updates documentation after code changes.

Adding documentation review to the code review process.

Taking advantage of version control systems like

[GitHub](https://github.com/)to track changes to the codebase and documentation.

## Conclusion

We've discussed why documenting code should be as important to development teams as writing code. Good code documentation makes it easier for developers to maintain and update code and collaborate with each other on software projects. Best practices include writing clean, quality code, utilizing code comments, and choosing the right tools, such as [GitHub Copilot](https://github.com/features/copilot) to provide AI-powered suggestions,[GitHub code review tools](https://github.com/features/code-review) to automate the code review process, and [GitHub Actions](https://github.com/features/actions), a CI/CD platform that automates the build, test, and deployment pipelines.

## Explore other resources

## Frequently asked questions

### What is code documentation?


Code documentation is written information that accompanies software code to help developers understand its purpose, how it works, and how to use it. Good code documentation makes it easier for developers to maintain, update, and modify code, and collaborate on software projects.

### What is an example of code documentation?


An inline comment is a code documentation example. Inline comments reside within the code and describe what the line or block of code does and its purpose. Method or function inline comments describe what the specific method or function does, and its inputs and outputs.

### Does code documentation change based on programing languages?


Yes, code documentation typically changes based on the programming language used in the codebase. Some programming languages have their own practices and tools and for documenting code, including Javadoc for Java code and docstrings for Python code. For example, docstrings use triple quotes for describing the purpose of a function, class, method, or module while Javadoc uses comments that begin with /** and end with */.