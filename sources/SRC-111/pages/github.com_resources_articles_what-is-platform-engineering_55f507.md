source: https://github.com/resources/articles/what-is-platform-engineering

# What is Platform engineering?

Learn what platform engineering is and how it empowers developers by creating internal developer platforms, improving workflows, and reducing operational bottlenecks. Explore the benefits for developers and IT managers alike.

## Platform engineering defined

Platform engineering is a discipline in [software development](https://github.com/resources/articles/what-is-software-development) focused on creating and maintaining a shared platform that helps development teams build, deploy, and manage applications. The goal of platform engineering is to streamline the software development process by providing standardized tools, infrastructure, and workflows that support faster and more reliable software delivery.

Key aspects of platform engineering include: **Automation**. Automating repetitive tasks—such as infrastructure provisioning, deployment, and monitoring—is central to platform engineering.

**Improved developer experience.** Improving the developer experience by providing easy-to-use, reliable, and scalable systems is a critical component.

**Self-service with guardrails.** Self-service with guardrails is the principle of empowering development teams to make their own decisions within a set of well-defined parameters, or guardrails. With self-service with guardrails, development teams retain autonomy to independently make development decisions, but automation and policy help are in place to make sure that security, compliance, operations, standards, and costs are properly managed.

**Standardization.** Creating consistent tooling and infrastructure for the entire organization reduces the complexity of operations and allows developers to focus on building and deploying their applications.

Platform engineering is essentially a bridge between development and operations with a specific focus on creating efficient and scalable environments for application development and operations.

## What led to the evolution of platform engineering?

Platform engineering has developed as a response to the growing complexity of modern software development environments. It evolved from traditional system administration, which led to [DevOps](https://github.com/resources/articles/what-is-devops) and then to platform engineering.

**Traditional system administration.** In the past, a traditional system administrator role included manually managing servers, networks, and storage. Administrators were responsible for provisioning hardware, setting up servers, configuring software, and ensuring uptime.

**DevOps.** In 2009, the emergence of cloud computing and automation toolsledto the rise of DevOps, which aimed to eliminate the barriers between development and operations. DevOps methods include collaboration between teams, continuous integration/continuous deployment ([CI/CD](https://github.com/resources/articles/ci-cd)), automation, and infrastructure as code.

Traditional system administrators began to evolve into DevOps engineers by adopting tools like Ansible, Puppet, Chef, and later, Kubernetes and Docker. They automated infrastructure management and used cloud platforms to scale operations.

**Platform engineering.** Platform engineering emerged as an evolution of DevOps, addressing the limitations of DevOps and offering a different approach. Instead of having DevOps teams manage infrastructure requests directly, platform engineering provides a self-service model.

## What are the core principles of platform engineering?

At the heart of platform engineering are several key components: self-service developer platforms, golden paths, and reduced cognitive load. Together, these elements empower development teams to work autonomously while providing consistency, reliability, and scalability across the organization.

**Self-service developer platforms. **Internal developer platforms allow developers to provision infrastructure, deploy applications, and manage resources without having to rely on operations teams. The platform abstracts the underlying complexity, providing pre-configured environments and easy-to-use APIs or user interfaces (UIs). Using a self-service developer platform, developers access the resources and tools they need without waiting for approval or assistance from other teams, improving speed and efficiency. These platforms also provide guardrails by supporting best practices and standardized configurations.

**Golden paths.** This term refers to pre-defined workflows or processes that guide developers toward using best practices for building, deploying, and managing software. This concept is based on the idea of providing guidance to help developers use the most efficient, reliable, and standardized way to achieve a particular task.

**Reduced cognitive load**. To help developers work more effectively and efficiently, platform engineering creates an environment that reduces their cognitive load so they are free to focus on writing code and delivering features. When developers don’t have to worry about configuring servers, managing Kubernetes clusters, or setting up CI/CD pipelines from scratch, they focus more on building features and solving business problems.

## What are key responsibilities of a platform engineer?

A platform engineer plays a critical role in building and maintaining the internal developer platforms that software development teams use to increase efficiency and reduce toil throughout the entire software delivery lifecycle. Their primary focus is creating a stable, scalable, and efficient platform, application frameworks, and standard pipelines, enabling developers to deliver software more effectively.

The key responsibilities of a platform engineer include:

Designing, building, maintaining and monitoring self-service platforms that provide development teams with easy access to resources like development environments, CI/CD pipelines, and deployment tools.

Developing automation for infrastructure provisioning using infrastructure as code tools.

Automating CI/CD pipelines to streamline code integration, testing, and deployment processes.

Working with experts in networking, DNS, and Kubernetes to create predefined workflows or golden paths, that guide developers toward best practices.

Working closely with DevOps teams, site reliability engineers, and developers to ensure smooth integration between the platform and development processes.

Embedding security and compliance requirements into the platform, such as secure pipelines, role-based access control, and encryption.


## What skills are needed to be a platform engineer?

A successful platform engineer requires a diverse set of soft and technical skills, as their role bridges both development and operations.

The following soft skills are helpful:

**Collaboration and communication. **Platform engineers must beable to work closely with software developers, DevOps, and site reliability engineering (SRE) teams to understand their needs and translate those into platform features.

**Problem-solving**. Strong problem-solving skills are required to tackle infrastructure challenges and continuously improve the platform’s capabilities.

**Empathy for developers. **Developers are their primary customers so platform engineers must have a focus on developer experience, ensuring that the platform reduces friction and supports productivity.

Key technical skills include at least some familiarity and experience with:

**Infrastructure as code. **Engineers should beproficient in tools like Terraform, CloudFormation, Ansible, or Pulumi for automating infrastructure provisioning.

**Containerization**** and orchestration.** Engineers need expertise in Docker and Kubernetes for managing containers, deploying microservices, and automating scalability.

**CI/CD pipelines.** Experience building and maintaining continuous integration and delivery pipelines using tools like GitLab CI or Azure Pipelines is required.

**Monitoring and observability**. Engineers should have familiarity with monitoring tools to ensure platform health and troubleshoot issues.

**Security practices**. A solid grasp of security principles, such as encryption, access control, and vulnerability management, is key creating a secured platform.

## What are the benefits of platform engineering?

Platform engineering offers a transformative approach to software development and operations by creating a unified, automated, and self-service platform that enhances developer productivity, operational efficiency, security, and compliance. The benefits of platform engineering include:

**Improved efficiency and productivity. **Efficiency is one of the core advantages of platform engineering, allowing development teams to focus on building and shipping features rather than managing infrastructure or operations. By centralizing and automating common development processes, platform engineering reduces manual work and improves consistency. These efficiency gains result in shortening the time-to-market for new features and products.

**Enhanced security. **Using platform engineering,security is embedded into platform engineering by design, rather than as an afterthought. Platform engineering also supports DevSecOps principles, allowing security practices to be embedded in the development lifecycle from the beginning. This proactive approach helps reduce security risks while fostering a culture of security awareness.

**Support for demonstrating compliance. **In highly regulated industries such as healthcare, finance, and government, compliance is critical. Platform engineering simplifies the process of supporting compliance by embedding compliance requirements directly into templates and workflows. Platforms also often integrate logging, monitoring, and auditing tools that track every action taken in the system. This makes it easier to generate reports, trace issues, and help processes align with regulatory standards.

**How is platform engineering different from DevOps and SRE?** Platform engineering, DevOps, and SRE are closely related practices, but they have distinct focuses and methodologies for managing and improving software delivery, infrastructure, and operations. Here's an overview of each practice and suggestions for when to choose one over the others.

**DevOps Focus: **Bridging the gap between developers and operations helps teams deliver faster, more reliable releases. **Goal:** Automate and streamline the software development lifecycle, including code integration, testing, deployment, and infrastructure management. **Practices/tools:** CI/CD pipelines, infrastructure as code, monitoring, automation, configuration management, and continuous feedback loops. **When to use it: **DevOps is for teams or organizations that need faster release cycles, automation, and integration between development and operations.

**SRE Focus: **Improving the reliability, stability, and uptime of applications and services. **Goal:** Use engineering approaches to maintain high availability and performance of systems. SRE teams are often tasked with balancing the speed of development with the reliability of systems. **Practices/tools:** Error budgets, service level indicators, service level objectives, monitoring, incident management, automation. **When to use it:** SRE is appropriate when the primary concern is system reliability, scalability, and uptime. It’s also useful in environments where the cost of downtime or instability is high, or when the organization wants to measure and enforce reliability goals using quantifiable data.

**Platform engineering Focus: **Building internal developer platforms to abstract and automate infrastructure and operational complexities for development teams.** Goal:** Provide self-service capabilities to developers so they are able to manage infrastructure and environments independently, speeding up development without involving operations teams for every change.** Practices/tools:** Internal developer platforms, automation, API-driven infrastructure, platform as a service, self-service interfaces, and Kubernetes.** When to use it: **Platform engineering is a good choice fororganizations that have a mature DevOps culture but need further scalability and efficiency. It’s also appropriate when the complexity of managing infrastructure for many teams or services becomes burdensome.

## When is it appropriate to begin implementing platform engineering principles?

You should consider adopting platform engineering practices when: **Scale and complexity increase.** As organizations grow, platform engineering can be helpful. Building a platform that abstracts infrastructure complexity allows teams to focus more on development while ensuring consistency over security and governance needs. **Developers require more autonomy.** Platform engineering empowers developers with self-service tools, removing the dependency on operations teams for provisioning infrastructure or deploying applications. **Teams need more consistency.** If multiple development teams need a consistent environment or standardized tooling, platform engineering provides this in a scalable, unified way. **When greater efficiency is needed. **When managing a large number of microservices or applications, it’s more efficient to provide a unified platform for developers rather than each team handling infrastructure separately.

## What are the best practices when adopting platform engineering?

Here are a few best practices to keep in mind when beginning a platform engineering practice.

**Understand developer needs.** Engage with development teams to understand their pain points and identify common development bottlenecks. They might struggle with complex CI/CD pipelines, environment configuration, or managing microservices.

**Adopt a product mindset.** Treat the platform like you would a product and establish clear goals, roadmaps, and metrics. Ensure that the platform evolves to meet the changing needs of its users.

**Focus on self-service capabilities.** Automate tasks like provisioning infrastructure, deploying services, and monitoring, reducing reliance on operations teams. Build clear abstractions around infrastructure components to empower developers to perform tasks without needing to understand the underlying complexity.

**Balance consistency with flexibility.** Provide standards for core services, such as logging, monitoring, and deployment, but allow teams to customize workflows when necessary.

**Invest in developer experience.** The goal of platform engineering is to improve the developer experience by reducing friction in their processes. Platform engineering methodologies can do this by improving onboarding, simplifying toolchains, and creating consistent environments across development, staging, and production.

## Explore other resources

## Frequently asked questions

### What is platform engineering in simple terms?


A good platform engineering definition is that it’s the practice of building and managing a system—or platform—that makes it easier for software developers to create, test, and deploy their applications. The platform automates many repetitive tasks and provides consistent, reliable environments for development and production.

### What does a platform engineer do?


A platform engineer plays a critical role in building and maintaining the internal platforms that software development teams use to deploy, monitor, and manage applications. Their primary focus is creating a stable, scalable, and efficient platform that abstracts the complexity of infrastructure, allowing developers to deliver software more effectively.

### How does platform engineering differ from DevOps?


Platform engineering focuses on building and maintaining an internal platform that provides self-service tools for developers, automating infrastructure management and enhancing the developer experience. DevOps, on the other hand, is a broader cultural practice aimed at improving collaboration between development and operations teams, with an emphasis on automating the entire software delivery process.

### Is platform engineering the same as SRE?


Platform engineering and SRE aren’t the same, though they are related. Platform engineering focuses on building internal platforms to provide self-service tools and infrastructure for developers, streamlining their workflows. SRE is a discipline that applies software engineering principles to ensure the reliability, availability, and scalability of systems in production, often focusing on operational tasks like monitoring, incident response, and performance optimization.

### Why is platform engineering important for enterprises?


Platform engineering is important for enterprises because it streamlines development by providing self-service tools and standardized infrastructure, so teams deploy and manage applications more efficiently.