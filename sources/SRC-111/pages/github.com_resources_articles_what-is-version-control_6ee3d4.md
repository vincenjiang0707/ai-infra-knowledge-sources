source: https://github.com/resources/articles/what-is-version-control

# What is Version Control?

Learn how version control systems and software help track changes, support collaboration, and ensure code integrity throughout the development process.

Imagine you're a violinist in a 100-piece orchestra, but you and the other musicians can't see the conductor or hear one another. Instead of synchronized instruments playing music, the result is just noise.

This is like developing software without version control. [Git](https://docs.github.com/en/get-started/using-git/about-git) is the most widely used version control system, letting distributed teams track and merge changes to the same code. Developers in decentralized locations working on the same code are blind to one another's changes and why they were made. The team ends up with conflicting edits, slowed progress, and undeployable software.

The solution is software version control. But what is version control, and how does it work?

## Introduction to version control

Version control systems (VCS) give software engineering teams complete visibility to the code history and a single source of documentation for all files, folders, and messages. Version control tools streamline [software development](https://github.com/resources/articles/what-is-software-development) and mitigate lost work and time by tracking code changes from asynchronous and concurrent work, identifying conflicting edits, sparking collaboration, and preventing overwrites.

Version control allows the developer "orchestra" to see every commit and access, review, collaborate, experiment, compare, and undo changes to ensure code integrity and faster releases.

In this article, we'll explore what version control software is and how it improves the software development process, developer experience, and product. We'll define important terms, explore the different types of version control systems available, and the version control tools most used by developers. You'll find guidance on how to evaluate tools for your team and enterprise, and best practices to help developers succeed.

## What is version control?

Version control software helps facilitate continuous software development workflows. As user demands scale up, version control helps developers work smarter together, using time and resources more efficiently.

A foundational tool in the modern developer's toolkit, version control tools keep a historical record of software changes in a specialized database, logging edits made by individual developers. When conflicts emerge, developers can look back and resolve code conflicts, minimizing disruption to the codebase.

Especially useful for [DevOps](https://github.com/resources/articles/what-is-devops) and [DevSecOps](https://github.com/resources/articles/what-is-devsecops) teams in accelerated cloud-based environments, version control systems facilitate collaboration, productivity, and successful software deployments.

## Understanding version control systems

Version control systems help eliminate common development roadblocks—like operating system limitations and siloed tool chains—simplifying and streamlining development and creating space for innovation that can lead to breakthroughs.

In addition to accelerating productivity and reducing errors, version control systems help save enterprises time and money.

Version control is essential to the overall health of the[ software development lifecycle (SDLC)](https://github.com/resources/articles/what-is-sdlc) and improves project management and product development. In fact, failure to adopt version control poses risks like data loss, sluggish development, and reduced code quality, hampering competitiveness. Integrating version control mitigates these risks by helping enterprises scale processes as demand increases. A secure, detailed record of versions and releases creates a hedge against code corruption.

Using a version control tool helps an organization unify operating systems, services, and developer toolkits by tearing down siloes and facilitating coordination across the entire software engineering ecosystem. Greater visibility fosters better communication and infuses buoyancy into the development process by improving project clarity and keeping contributors engaged and aligned.

Version control systems empower developer teams to:

**Create a codebase history:**Version control systems create a complete codebase history, stored in a specialized database, and provide the entire team with a single and secure source of truth.**Ramp up collaboration:**By tracking every change, version control systems help teams avoid conflict and create opportunities to experiment and innovate.**Reduce errors:**Using a version control tool allows developers to find errors fast, roll back to a previous version and correct the problem, mitigating the impact of the error.**Improve code quality:**A version control system encourages developers to follow best practices and write clean code that is easy to access, understand, and maintain.**Recover in a snap:**With version control, every code change is tracked, restorable, and revertible. A version control system acts as a safety net, preventing accidental code deletions and related developer anxiety.**Increase coding confidence:**Developers rely on version control systems to synchronize versions so they can resolve conflicts and safely experiment.**Expand visibility:**Team collaboration and communication improve with version control by providing full visibility to the[code documentation](https://github.com/resources/articles/tools-and-techniques-for-effective-code-documentation)and its history.**Automate tasks:**Efficiency and productivity increase with a version control system by automating testing, analysis, and deployment for fast, consistent results.

## Features of version control software

Let's review some of version control software's capabilities, functions, and features.

**Repository:**Also called a "repo," a repository is the centralized database that stores the complete collection of files and folders for a codebase, along with the revision history.**Pull request:**The mechanism developers use to propose, notate, review, and discuss changes before they merge updates into the main codebase is a pull request. A pull request is also known as a merge request.**Commit:**A commit is a snapshot of changes with a unique "hash" that identifies the proposed changes. A commit can include notes and messages between developers.**Branch:**A code branch is a separate, parallel version of the codebase created by developers to work independently on experiments, regression testing, and debugging without changing the main codebase.**Merge:**When developers combine code edits, they integrate the changes from one branch into another or into the main codebase.**Conflict:**When multiple developers make edits to the code, their changes sometimes conflict. Version control tools help developers identify and resolve conflicts to keep development moving.**Checkout:**When a developer retrieves a file from the version control system it's called a checkout.**Tag:**A tag is a marker used by contributors to label a specific point in the source code history, like the release date. Tags are also used to mark a specific point in the codebase before changes.**Remote:**Remote development allows developers to do some or all their work on their local desktop, on a company server, or on the cloud.**Fork:**A fork is the process of creating a separate and distinct piece of software by copying source code from an existing software package.**Revert:**Developers can revert, or undo, one or more recent changes and return to the previous version.

Now let's look at the various types of version control software systems and tools commonly used in software development.

## Types of version control systems

Deciding which tool is right depends on the needs of the development team, scale of the project, and other factors, but having one is essential to efficient and effective software development.

Some of the distinct types of version control systems are:

**Local**

Stores code changes locally on a user's computer

File changes are stored as patches

Patches are pushed to a single version of the codebase

Not scalable or collaborative, works for smaller projects


**Centralized version control systems (CVCS)**

A single, centralized database, or repository, is stored on a server

All users work with the same repository and commit to the same branch

Users check out the latest version from the server

Some systems "file lock" in the central repository to prevent simultaneous edits to the same file

Contributors push commits to the server and resolve merge conflicts on the repository


**Distributed version control systems (DVCS)**

Users access the repository from any location

Contributors can work on the same codebase without being on the same network

Each developer has a local copy of the entire repository and history on their device

Users can commit, branch, and merge changes locally without reliance on the central server


**Lock-based**

When a user begins work, individual files are locked

Prevents two or more users from making conflicting changes


**Optimistic**

Every user has a private workspace

Users submit server requests to share changes with the team before merging

The server determines which changes can be merged safely


Depending on region and locale, distributed and centralized version control systems are the most widely used types because of their scalability, flexibility, and developers can collaborate on code from anywhere in the world.

## Common version control tools

There are several [DevOps tools](https://resources.github.com/devops/tools/compare/) available for version control, and the most used include:

**Git:**Git is an open-source distributed version control tool preferred by developers for its speed, flexibility, and because contributors can work on the same codebase simultaneously.**Subversion (SVN):**Subversion is a centralized version control tool used by enterprise teams and is known for its speed and scalability.**Azure DevOps Server:**Previously known as Microsoft Team Foundation Server (TFS), Azure DevOps Server is a set of modern development services, a centralized version control, and reporting system hosted on-premises.**Mercurial:**Like Git in scalability and flexibility, Mercurial is a distributed version control system.**Perforce:**Used in large-scale software development projects, Perforce is a centralized version control system valued for its simplicity and ease of use.

## Version Control tool factors

When evaluating the advantages and disadvantages of various version control tools, keep these factors in mind.

**Scalability:**If the project is large with a distributed team, the tool should be able to handle expansive projects with many files and users.**Ease of use:**Version control tools can be complex, so a simple, user-friendly interface can help ensure a manageable learning curve and accelerate adoption.**Collaboration features:**The tool should support multiple contributors working on the same codebase simultaneously and facilitate quick communication to streamline merges.**Integration with existing tools:**Look for a tool that will work with the tools your team already uses, like project management software, continuous software integration solutions, building and editing tools, and integrated development environments.**Supports branching:**A VCS should support branching for efficient workflows so developers can work on distinct parts of the code without conflicting or interfering with one another's work.

## Best practices for version control

Incorporating version control into a software development process is a significant step. After choosing the right version control tool for a project, best practices can help the team get up to speed early.

**The repository setup:**A version control repository should be compliant, and have access control, disaster recovery, and failover plans in place.**Establish workflow alignment:**Productive collaboration is optimized when contributors are on the same workflow page, so seek understanding and agreement early.**Write clear commit messages:**When contributors commit to the repository, including clearly written messages that explain the changes can help mitigate roadblocks.**Commit often:**Encourage the team to make lots of small commits with concise comments to keep development moving. Avoid the tendency to make fewer but more complex changes accompanied by long messages.**Test before committing code:**The adage, "Measure twice, cut once," applies here. To ensure the code works as expected, contributors should test before committing changes to the codebase.**Commit code only when ready:**Like doing many small commits, only completed code should be committed to keep the codebase in good working order.**Avoid conflicts:**Developers can help mitigate conflicts by pulling code from upstream to ensure they work with the most up to date code, and by breaking large files into smaller ones.**Use branches:**Code branches should support multiple versions of software releases and patches.**Limit repository access:**Give access only to contributors who need it, a simple but powerful practice that prevents unauthorized codebase access.

## Conclusion: The benefits of version control

Version control systems help developers keep a complete code history by tracking changes and supporting better collaboration to help ensure code integrity throughout the development process. Crucial for effective DevOps teams working in accelerated cloud-based environments, version control software supports modern software teams so they can work smarter and release software faster.

## Explore other resources

## Frequently asked questions

### What are the different types of version control?


There are several types of version control systems, including local, centralized, distributed, lock-based, and optimistic. Distributed and centralized version control systems are the most used because of their ease of use, scalability, flexibility, and collaborative support.

### Is GitHub a version control system?


No, GitHub is a cloud-based hosting system that works with Git, a distributed version control system offering full-scale developer support. GitHub allows software engineering teams to host Git-based repositories on the cloud.

### What is version control in DevOps? / Is version control part of DevOps?


Version control is integral to DevOps because it helps developers plan smarter, collaborate better, improve code integrity, and deploy software faster.

### What is the difference between version control and a repository?


Version control is software that tracks code changes over time. A repository is the data structure used in version control tools to store the collection of codebase files and history.

### What are the benefits of using version control?


A version control system benefits developers by providing a complete history of code modifications and supporting collaboration and innovation so they work smarter together to release software faster.

### What are some examples of version control systems?


Some of the most widely used version control systems are Git, Subversion (SVS), Azure DevOps Server, and Mercurial.