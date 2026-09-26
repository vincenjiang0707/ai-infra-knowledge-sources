source: https://github.com/resources/articles/devops-model

# What is the DevOps Model? Exploring foundational practices in DevOps

DevOps helps teams ship high-quality products faster by reducing the friction between writing, testing, and deploying code. GitHub offers a holistic platform designed to help organizations successfully adopt DevOps, making it easier to continuously ship and improve software.

## What is a DevOps model?

People often ask what a DevOps model is—but this misses the point of [DevOps](https://resources.github.com/devops/fundamentals/). DevOps is an approach to building software that touches the entire development lifecycle. It’s a mix of practices, culture, and technology intended to continuously deliver value to end users.

In short, there is no one-size-fits-all approach to DevOps. Its implementation varies from organization to organization. Despite this, DevOps does have a framework of practices that all organizations leverage in varying forms.

At the core of DevOps is the idea that everyone responsible for a product should collaborate as a unified team. Rather than work in separate development, quality assurance (QA), security, and operations silos, DevOps brings people together to take end-to-end responsibility for planning, building, delivering, and improving software.

How DevOps works varies from one company to the next. But there are three core themes you’ll find in every organization that successfully adopts DevOps.

### Everyone is responsible for quality

DevOps reduces the barriers between the disciplines found in software development teams. Practitioners tend to focus on building end-to-end products instead of completing siloed, incremental projects. This means the same individual will collaborate across the full software development lifecycle from planning to building to [testing](https://github.com/resources/articles/what-is-shift-left-testing) and deploying a product.

### Code ships when it’s ready

Traditional software development practices often bundle many changes into large releases. This means customers typically wait longer for software updates. It also makes it harder to predict the knock-on effect big code changes will have, putting greater pressure on development and operations teams. In contrast, DevOps favors incremental code changes that are easier to build and test—and to ship as soon as they are ready. Once a developer commits code changes to a project, [continuous integration](https://resources.github.com/devops/fundamentals/ci-cd/integration) and [deployment](https://resources.github.com/devops/fundamentals/ci-cd/deployment) ([CI/CD](https://github.com/resources/articles/ci-cd)) tools facilitate automated tests, application builds, and code integration or issue reporting. Many DevOps practitioners extend the concept of continuous improvement to their own work, measuring and adjusting their processes over time.

### Automation improves quality and predictability

In a successful DevOps practice, anything that can be automated should be automated. This reduces the risk of human error and makes products easier to scale. Tools are used to automate the configuration and deployment of infrastructure, while static analysis tools find and highlight security vulnerabilities. DevOps practitioners strive to automate repetitive tasks at every stage.

## What is a DevOps operating model?

Compared to traditional development methods where programming teams write code, testing teams find bugs, and operations teams take care of the infrastructure, DevOps can seem like a radical change. As a practice, DevOps fundamentally seeks to transform organizations by bringing traditionally siloed teams together across every part of the [SDLC](https://github.com/resources/articles/what-is-sdlc).

While that may seem daunting, it’s possible to begin your DevOps journey with relatively small changes. To know where to start, let’s look at some of the operational implications of DevOps.

### Culture

Tooling is often the most visible aspect of DevOps. However, DevOps starts with a cultural change intended to shift how we think about expertise and responsibility.

Consider traditional software development roles such as development, testing, and operations. They encourage people to think in terms of narrowly defined responsibilities and projects rather than looking at the product as a whole.

If writing code is distinct from running it, for example, then the person writing that code is less inclined to think about how to make their work easier to deploy or more resilient in the face of increased demand. In larger organizations, separate programming, QA, and operations teams might not even know each other.

A DevOps culture puts the emphasis on people and product. Distinct roles give way to individuals who share equal responsibility for delivering the product and nobody’s job is done until that software is solving problems in production.

For a DevOps culture to thrive, there are three principles an organization should adhere to:

**Autonomy:**Everyone has what they need to perform their role without blocking their colleagues.**Transparency:**Information flow is the currency of DevOps. Both through automated communication––such as monitoring and instrumentation––and a bias towards raising issues, DevOps culture builds feedback loops that surface and help resolve inefficiencies.**Continuous improvement and learning:**In a DevOps culture, each fix or feature is an opportunity to find better ways of working and a chance for individuals to grow. A culture of sharing means the broader organization becomes more effective over time.

By placing people above process, DevOps creates a culture where the system serves the individuals in helping them make the best possible product. And with hands-on understanding of each part of the development lifecycle rather than only a narrow area of expertise, those individuals can see how each element impacts the next. That insight leads to more thoughtful work that reduces friction across the software development lifecycle.

### Team structure

In non-DevOps organizations, strict role silos separate architects from developers and developers from testers and operations professionals. From one week to the next, an individual might work on several projects without ever engaging in what happens when their job is done.

DevOps shifts the focus from projects and roles to products and people. The same individual or group of people take care of a product from planning through development and on into production. The goal is to remove the barriers between developers and operations professionals and replace that with “engineers” who have an end-to-end perspective with possible specialization. Job titles may vary from one organization to the next, but the central idea is that the reality of building a software product rarely matches up with neatly demarcated job roles.

By taking a product-centric view, DevOps puts practitioners closer to customer needs, saves costly context switching, and provides the agility to solve issues faster.

### Process

In DevOps, the carefully crafted plans, bureaucracy, and wide-reaching releases of traditional software development make way for practices that enable ongoing, collaborative improvement.

In particular, DevOps organizations follow processes and practices that favor:

**Incremental change:**Rather than make large, combined releases, DevOps teams work with smaller, frequent changes that push incremental value into production sooner and are easier to plan, develop, test, and deploy.**Continuous improvement:**Those incremental changes are integrated, built, and deployed via automation as soon as the tests pass, rather than relying on manual processes.

### Tooling

Tooling is a practical manifestation of DevOps culture and process, and touches every part of the software development lifecycle. In DevOps, tools are often used to apply automation wherever possible, create feedback loops, and free up organizational resources.

DevOps tools often broadly fall into four categories:

**Version control:**Most development teams use some form of source code management but in DevOps version control tools such as Git are a foundational tool.**Continuous integration and deployment:**CI/CD tools such as GitHub Actions are used to automate the building, testing, and deployment of code changes, and are usually triggered by a Git commit.**Infrastructure as code:**Tools such as Azure ARM are used to manage and scale virtual machines,[containers](https://github.com/resources/articles/containerization), and serverless code programmatically to meet real-time demand.**Observability:**Testing, monitoring, and reporting tools are used to understand system performance and uptime and create feedback loops to improve services.

## DevOps model advantages and disadvantages

DevOps has proven its value in thousands of software development organizations across the world. [According to Microsoft’s Enterprise DevOps Report](https://azure.microsoft.com/en-us/resources/enterprise-devops-report-20202021/), elite DevOps organizations ship code 4-5x faster than other organizations.

However, before you adopt DevOps in your organization you should be sure that you understand both its advantages and disadvantages.

Specifically, you should consider the following in relation to your products, people, and strategic goals:

The tradeoff between the work to adopt DevOps and the benefits you’ll reap

How your technology teams are structured and culturally interact with one another

The adaptability of the software that you build; for example, some architectures and tech stacks will adapt to DevOps more easily than others


Let’s look at some of the advantages and disadvantages of the DevOps model in a little more detail.

### DevOps model advantages

DevOps can offer measurable improvements across each part of the software development lifecycle. To realize those gains takes a concerted, organization-wide effort to change culture, process, and tooling. In practice, organizations that successfully adopt DevOps typically report the following benefits:

**Faster delivery:**DevOps helps get value to users faster by breaking work into incremental improvements, rather than large releases, and pushing code changes to production as soon as it is ready. Depending on their velocity, some organizations ship multiple code releases every day.**More automation:**DevOps practices apply automation to much of the software development lifecycle to improve and standardize the testing, building, integration, and deployment of code. That reduces organizational costs by reducing the number of repetitive tasks team members work on. It’s also good for the developer experience—developers spend less time doing repetitive tasks and have more time to focus on creative and complicated work.**Increased quality:**Similarly, automation of processes such as testing and[security analysis](https://github.com/resources/articles/what-is-software-composition-analysis)reduce the risk of bugs and vulnerabilities making it into production.**Improved process scalability:**Data-driven process and iterative change improve the organization’s ability to grow. Along with automation, explicitly defined culture, and continuous improvement, they enable smaller teams to deliver more value while making it easier to onboard new team members.**More scalable products:**At the product level, DevOps’ preference for incremental releases makes it easier to scale a product to meet real-time system demand from end users.**Greater resilience:**By encouraging feedback loops through automated monitoring and reporting tools, DevOps helps teams to build more resilient software. And where problems arise, DevOps automation and[tooling](https://resources.github.com/devops/tools/)help get fixes into production faster than traditional software development practices.

### DevOps model disadvantages

Most organizations start slow and build their DevOps culture over time. However, there are those that only partially adopt DevOps and consequently realize only limited benefits. Others implement DevOps processes without adapting them to the specific needs of their people, strategy, and products.

So, what are the possible disadvantages of a poorly designed DevOps strategy?

**DevOps is an ongoing process, not a one-time change:**In successful DevOps organizations, DevOps is the natural way of working. People default to thinking in terms of products, collaboration happens without intervention, and everyone looks for ways to improve the process. Without ongoing reinforcement, it becomes harder to maintain that momentum.**Misaligned tooling:**As the most visible aspect of a DevOps practice, it’s tempting to mistakenly confuse the adoption of DevOps tools as the adoption of DevOps. However, without the right culture and practices, DevOps tooling will grate against existing processes.**Implementations are not maintained:**Even when you have the right tools and the broader context to support them, integrating them into a single[DevOps pipeline](https://resources.github.com/devops/pipeline)requires an ongoing commitment. Without that, a gap can form between process and tooling, requiring manual interventions.

## What about a DevOps maturity model?

Introducing DevOps to your organization is an ongoing journey with different levels of adoption across the many different stages of product delivery. DevOps is as dynamic as a business needs it to be, and its implementation varies from organization to organization.

This means there isn’t one defined DevOps maturity model. At GitHub, we shy away from talking about DevOps maturity models because it implies there’s a checklist any organization can use to achieve “DevOps.” This isn’t true. At its core, DevOps is an ongoing practice. However, there are common steps and markers of success businesses can work towards.

Take, for example, a company that is considering moving towards adopting a DevOps practice. At their starting point, the development and operations teams may be siloed and focused on their individual roles. That means that as the development team builds code, the operations team is forced to react to support that code. A good first step for this organization might involve bringing both teams together to begin planning, building, and shipping code collaboratively.

At the other end of the spectrum are organizations whose entire SDLC is automated and feature deep collaboration. Product-focused teams work together to deliver continual improvements, using automation and specialized DevOps tooling at each stage.

So even though every organization’s DevOps adoption journey is unique, these are key principles that indicate success. Here’s If you do these things you're doing DevOps well—but depending on your industry, you'll have things that are particular and necessary to your DevOps practice.

### Key stages in the DevOps adoption journey

**Experimental DevOps:**One or two teams are exploring DevOps Role-based silos still largely in place Some experimentation with automation but manual intervention needed for each step No formal process**Learned DevOps:**Some parts of the organization have adopted collaborative product teams Those teams are using DevOps tooling to good effect but each team has their own approach Process is forming and largely learned from what other organizations are doing**Proactive DevOps:**All new products start out under the DevOps model Measurements are in place to monitor process effectiveness and feed into improvements Process is starting to become adapted to the needs of the organization Most of the organization is using DevOps tooling**Native DevOps:**DevOps is adopted across the organization The DevOps process is tuned precisely to the organization’s needs, with regular updates as circumstances change Test, build, deployment are automated using DevOps tooling All teams are product-focused, with an easy flow of communication and collaboration across the full organization