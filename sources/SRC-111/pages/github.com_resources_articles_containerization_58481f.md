source: https://github.com/resources/articles/containerization

# What is containerization?

When it’s successfully implemented, DevOps can transform software reliability by making the software development lifecycle (SDLC) more predictable through a combination of automation and cultural practices that favor deep collaboration and incremental releases. With less chance for variation, fewer code-related issues make it to production.


But it’s not only the code itself where problems can arise. What works on one person’s machine might behave differently on a colleague’s laptop—or worse, on a production server. Containerization is one type of technology that can be used in [DevOps](https://resources.github.com/devops/fundamentals/) practices to ensure that the software environment is consistent from one machine to another during development, testing, and on into production.

At GitHub, we provide tools that help companies adopt and manage containers in their DevOps practice. Through this experience we’ve identified key areas organizations need to consider to successfully integrate containers into their SDLC.

In this guide, we’ll answer the following questions:

What is containerization?

What are the benefits of containerization?

What role does containerization play in DevOps?

What are some common containerization tools?

How does GitHub incorporate containerization tools?


## What is containerization?

Containerization packages software code with dependencies and an operating system in the form of a standalone application that can be run on top of another computer. These virtualized environments are lightweight by design and require comparatively little computing power. They can also be run on any underlying infrastructure and are portable, or are able to be consistently run on any platform.


By bundling application code, configuration files, operating system (OS) libraries, and all dependencies together, containers help solve a common problem in software development: Code that is developed in one environment often exhibits bugs and errors messages when transferred to another environment. A developer may, for instance, build code in a Linux environment and then transfer it to a virtual machine (VM) or Windows computer and find their code no longer works as expected. In contrast, containers stand alone from the host infrastructure and provide consistent development environments.

But what makes containers particularly useful is that they are easy to share. By using container images—files that act as a snapshot of the container’s code, configuration, and other data—you can quickly spin up consistent environments across each stage of the SDLC. This helps organizations create reproducible environments that are fast and easy to work with from development through testing and on into production.

## Application containerization

Ordinarily, a container takes care of just one part of an application and organizations will leverage a number of containers to isolate application components and run them in concert.

That could be as simple as one container for the backend application server, another for the database system, and perhaps another running a [monitoring tool](https://resources.github.com/devops/tools/monitoring). But containers can also be used to build more complex systems. In a microservices architecture, for instance, there can be hundreds or even thousands of containers with each hosting a small part of a larger application. To manage that many containers, teams turn to container orchestration tools such as [Kubernetes](https://github.com/kubernetes/kubernetes) that enable organizations to more easily manage containers in production environments.

Isolating applications in this way can make it easier to develop each part of the application, reduce the risk of programs accessing data without authorization, and scale to meet demand by quickly deploying more containers as needed. And because containers include only what they specifically need, there’s relatively little difference between adding a new container and running the application directly.

## Virtualization vs. containerization: What’s the difference?

Containers are commonly compared to virtual machines (VM) due to similarities in how they abstract operating systems away from the underlying infrastructure—and because they’re sometimes used for similar tasks. But there are fundamental differences in how containers and VMs work.

Virtualization enables organizations to run different operating systems and applications at the same time while drawing on the same infrastructure, or computing resources. An organization might, for instance, use VMs to run Windows and Linux simultaneously on one server. Each VM on the server acts as a standalone, abstracted “computing” environment and draws on all the necessary resources of the underlying server, or computer.

In contrast to VMs, containerization more efficiently utilizes computing resources by bundling code, configuration files, libraries, and dependencies—and not the entire OS. Containerization instead leverages a runtime engine on the host computer which shares the underlying OS across all provisioned containers.

When choosing whether to use containers or VMs, you should weigh up the consequences of those technical differences. For example, long-running monolithic applications might be best suited to a VM thanks to its long-term storage and stability. In contrast, lightweight containers are much better suited to a microservices architecture where the overhead of many VMs would be impractical.

**Containerization:**

Containers use the host OS, meaning all containers must be compatible with that OS.

Containers are lightweight, taking only the resources needed to run the application and the container manager.

Container images are relatively small in size, making them easy to share.

Containers might be isolated only very lightly from each other. A process in one container could access memory used by another container, for example.

Tools such as Kubernetes make it relatively easy to run multiple containers together, specifying how and when containers interact.

Containers are ephemeral, meaning they stay alive only for as long as the larger system needs them. Storage is usually handled outside the container.


**Virtualization:**

VMs are effectively separate computers that run their own OS. For example, a VM can run Windows even if the host OS is Ubuntu.

VMs emulate a full computer, meaning that they replicate much of the host environment. That uses more memory, CPU cycles, and disk space.

VM images are often much larger as they include a full OS.

By running a separate OS, VMs running on the same hardware are more isolated from one another than containers.

Configuration management tools, such as Terraform or Ansible, automate VM deployment and integration.

VMs tend to have longer lives and include a full file system of their own.


## The benefits of containerization in DevOps

At the heart of [DevOps](https://resources.github.com/devops/) are lightweight, repeatable processes that automate the software development process. However, modern applications are increasingly complex, particularly as they grow to include many different services.

Containers help simplify that complexity through greater standardization and repeatability—and that translates to a faster, higher quality, more efficient SDLC.

The benefits of containerization include:

**Portability:**Even seemingly small differences in the underlying environment can impact how code runs. That’s why the saying “It works on my machine” is rarely meaningful—and is often somewhat of a joke. It’s also why the saying “write once, run anywhere” has been a recurring goal for people looking to improve software development practices. Containers help organizations accomplish this by bundling up everything an application needs into consistent and portable environments that make it easier to standardize application performance.**Scalability:**Containers can be deployed and configured to work with one another in a larger system architecture through the use of orchestration management tools such as Kubernetes. These tools can also be used to automate the provisioning of new containerized environments to scale with real-time demand. That means properly configured containerized environments can be rapidly scaled up—or scaled down—with little-to-no human intervention.**Cloud-agnostic:**When configured for portability, containers can run anywhere—whether that’s a laptop, bare metal server, or cloud provider platform. And because containers abstract away underlying platform differences, they mitigate the risk of platform lock in. You can also use containers to run applications across multiple cloud platforms and switch from one provider to another.**Integration into the DevOps****pipeline****:**Containerization platforms are often designed to be inserted into larger automation workflows. That makes them ideally suited to DevOps where CI/CD tools can create and destroy containers automatically for tasks such as testing or even deployment into production.**Efficient use of system resources:**Unlike virtual machines, containers are often more efficient and require less overhead. There’s typically no hypervisor or additional operating system that’s native to a container. Instead, container tools provide just enough structure to make each container a standalone environment that leverages the shared resources of the host system wherever possible—and that includes the underlying operating system, too.**Facilitate faster software releases:**Containers can be used to simplify larger and more complex applications by dividing their underlying codebases into smaller run-time processes that work together. This helps organizations accelerate each step of the SDLC because it enables practitioners to narrow their focus to a specific part of an application rather than working with the entire, wider codebase.**Flexibility:**Containers bring an inherent flexibility to the SDLC by enabling organizations to quickly provision more computing resources to meet real-time demand. They are also often used to create redundancies to support greater application reliability and uptime.**Improved application reliability and security:**By making the application environment part of the DevOps pipeline, containers face the same quality assurance as the rest of the application. And although containers work together, the isolated environment provided by a container makes it easier to isolate issues in one part of the application from impacting the wider system.

### The role of containerization in DevOps

First, a note: DevOps is an organizational transformation that changes the way teams build and deliver value and typically has a software component (although you can do DevOps with just hardware, too). Containers provide a more modern way to develop software more efficiently and at scale.

In short, containers aren’t a requirement for building a successful DevOps practice—but they can be a natural fit depending on your organizational needs and priorities.

That’s because containers can help amplify the benefits of DevOps, in part, by making tests more reliable, creating developer environments that are closer to production environments, and by simplifying the deployment process.

This role of containerization in DevOps often breaks down into the following benefits:

**Greater reliability:**Repeatable, automated processes ensure that tests and security checks run each and every time that code is committed, merged, and deployed. The cultural change of breaking the silos between teams makes quality everyone’s responsibility. Containers run the same everywhere, increasing the reliability of tests.**Faster delivery:**Continuous improvement, microservices architectures, and the automated DevOps pipeline help make sure changes are easier to reason about, faster to develop, simpler to test, and have fewer unintended consequences. By separating parts of an application into individual containers, DevOps practitioners can focus on one aspect of the solution at a time with less concern about the knock-on consequences that changes in one area might have elsewhere.**Improved collaboration:**DevOps does away with role-based teams and brings people together to work towards common product goals. The shareability of containers makes it easy for people to collaborate because they can work with the same application environment no matter what hardware they personally choose. Using a container registry—a centralized directory of containers—makes it easy to publish and find containers in an organization.

### Building containers into the DevOps workflow

Once a container has been built, it should never change. Each time a specific version of a container is deployed, it will behave in the same way as every other time it was deployed.

But things do change—so how do containers incorporate new packages with security fixes and new features? Updating a container means building a new version and explicitly replacing the previous version wherever it’s in use. Even if the new package’s internals have changed, container maintainers work to avoid making changes to how the container interacts with the outside world.

In the context of a DevOps pipeline, that repeatability means that tests running on containers in the CI/CD pipeline will behave just the same as if that container were in production, for example. That makes tests more reliable and reduces the chance of code issues, bugs, and errors reaching end users.

So, how else do containers play a role in the DevOps workflow?

**Code:**Even before a line of code is written, containers bring a level of standardization to the development environment. By specifying the package versions required by an application, containers offer consistent environments from one developer’s laptop and another. That reduces the chance of bugs creeping in due to environmental differences.**Build:**Unlike deploying directly to a VM or bare-metal server where the target must be live and ready to go, a container can be built once and then stored for deployment later. That decouples the build phase from the target environment and means that builds need to happen only when the container changes.**Test:**Containers extend the idea of automated testing by enabling the full environment to be tested—and not just the code itself. This enables higher quality software delivery as the test environment matches the production environment.**Release and deploy:**The repeatability of containers means that to change code in production requires building and deploying a new container. The result is that containers are usually ephemeral, which impacts how organizations architect their applications and lends itself well to a microservices model.**Operate:**Containers reduce the risk of deploying updated code or dependencies to a live application. A change made in one container is isolated there. For example, two microservices in separate containers can depend on different versions of the same JSON encoding/decoding library without the risk that changing one will impact the other.

### How containers work in CI/CD

A CI/CD pipeline can be thought of as the conveyor belt that drives the DevOps workflow. To be effective, a CI/CD pipeline must balance speed with thoroughness. Without speed, a CI/CD flow risks backlogs as commits occur faster than they can make it through the pipeline. Without thoroughness, people will lose faith in the CI/CD pipeline as problems slip into production.

Here’s how containerization boosts both aspects of CI/CD at key stages:

**Integration:**By using containers, you don’t have to start from scratch when integrating code changes to the larger codebase. You can create a base container that already holds the application’s dependencies and modify that during the integration phase.**Test:**Containers can be quickly provisioned and retired as necessary. Rather than needing to manually maintain explicit test environments or wait for configuration scripts to build an environment, a container can be provisioned and deployed automatically at scale. That way, tests run faster and with less need for human intervention to build test environments.**Release:**Once all the tests pass, a CI/CD pipeline’s build phase results in a container image that is then stored in a container registry. Once that image exists, much of the work that would usually take place in the release and deploy phases is already complete. Orchestration tools such as Kubernetes then take care of managing where the containers are deployed and how they interact.

## Microservices and containerization

A microservices architecture splits an application into small units that are tasked with fulfilling a specific function. For example, an online banking application might have a microservice that fetches live currency exchange rates and exposes that data to other microservices through an internal API. Importantly, the inner workings of the microservice don’t need to be public, only the API.

For many organizations, DevOps, microservices, and containers go hand in hand. The DevOps philosophy of continuous improvement fits neatly with the focused scope of microservices. And it’s common for microservices to be stateless—meaning that they don’t store data within themselves and instead rely on specialized data services. This fits with the short-term nature of containers as they can be deployed or destroyed without worrying about how to persist the data they produce and rely on.

In a microservices architecture, there’s a one-to-one relationship between each instance of a microservice and a container. As demand grows, the orchestration tool can be configured to deploy more containers for a particular microservice and retire them when demand ebbs.

## Common containerization tools

The first step to working with containers is to understand the landscape of container tooling. They fall into two broad categories:

**Container platforms:**The tooling that takes care of building and running container images within a host operating system. Docker and LXD are well-known examples.**Container orchestration:**Tools for deploying, scaling, and managing containers that work together to power an application. Kubernetes is a popular container orchestration platform.

Let’s look at them in more detail.

### Container platforms

The container platform is the set of tools that build, run, and distribute the containers themselves. The best known of these is Docker, which provides an end-to-end platform for working with containers. And thanks to a growing suite of open standards, there are alternatives that enable you to pick and choose different tools for different parts of the process. Podman, for example, offers a different way to run containers and Kraken is an open source registry for distributing containers.

Whether you choose an all-in-one solution or pick and choose from different tools, you’ll need:

**Process container manifests:**These are the configuration files that specify the contents of the container, the ports that the container needs to use, and what resources it needs.**Build images:**These are containers at rest that are ready to be deployed.**Store and distribute images:**Often called a container registry, this is a central repository that can be tied into your CI/CD system for automation purposes. It can also be used manually by DevOps practitioners.**Run images:**Create and run an isolated environment for the container. On Linux this is relatively simple. On Windows and macOS this might require a VM to provide a Linux environment from which you can create and run container images.

### Container orchestration

Larger microservices architectures can often have thousands of microservices with each running in one or more containers. Deploying, scaling, and managing the interactions between that many containers isn’t a manual job. Instead, DevOps practitioners set parameters—such as the resources a particular set of containers need, which containers need to communicate with each other, and so on—but it takes an orchestration platform to run all those containers in harmony.

Just as with the containers themselves, several orchestration tools are available and each one takes a slightly different approach. The most common is Kubernetes, which is the closest that the industry has to a standard container orchestration tool. Kubernetes was originally built by Google to manage containers that powered its search engine. However, there are alternatives. On the open source side is Red Hat’s Openshift Container Platform, while on the SaaS side are offerings such as Azure’s Kubernetes Service.