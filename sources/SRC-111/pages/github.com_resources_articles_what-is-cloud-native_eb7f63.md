source: https://github.com/resources/articles/what-is-cloud-native

# What is cloud native?

Cloud native is an approach to designing and building applications for dynamic cloud environments. By prioritizing rapid development and frequent updates, organizations are able to innovate faster and reduce operational complexity.

## Cloud native defined

Cloud native refers to a set of [software development](https://github.com/resources/articles/what-is-software-development) practices that take advantage of the flexibility of cloud computing. Unlike traditional software, applications built using this method are highly modular, scalable, and easy to update. This empowers organizations to quickly respond to changing customer demands.

## Why adopt cloud native?

Adopting cloud-native development has significant advantages for both businesses and development teams.

### Business and operational benefits

**Increased flexibility and speed:**Cloud native allows businesses to respond to customer needs faster than traditional software development methods.**Lower infrastructure costs:**Companies avoid large upfront investments in hardware and instead use cloud infrastructure on-demand, which reduces capital expenditures and operational costs.**Business continuity and resilience**: Cloud-native applications are designed for high availability and fault tolerance. They can automatically recover from failures, which helps ensure that business-critical applications remain available even during disruptions.

### Developer benefits

**Enhanced collaboration**: The cloud-native approach promotes collaboration among development, operations, and quality assurance teams.**Easier updates and maintenance**: Microservices architecture allows teams to independently update various components without disrupting the entire application. This makes it easier to fix bugs, add features, and scale individual services.**Optimized developer productivity**: Because developers don’t have worry about infrastructure and deployment issues, cloud-native tools and frameworks allow them to focus on writing code.

## What are cloud-native applications?

As opposed to traditional applications that are built as a single large block of code, cloud-native applications are made up of small, independent components, called microservices. These services run independently, making the application more flexible and scalable.

The most common characteristics include:

**Modularity:**Cloud-native applications are built with microservices that developers mix and match to form diverse applications.**Scalability:**To optimize resource utilization, cloud-native applications scale up and down based on demand.**Resilience:**Engineered to be fault-tolerant and self-healing, cloud-native applications help organizations minimize downtime.**Manageability:**Automation makes it easier to monitor, maintain, and frequently update cloud-native applications.**Observability:**Cloud-native applications support data analysis across logs, users, and traces, offering critical insights into application performance and health.

## Cloud native versus cloud hosted

Although similar in name, cloud-native applications aren't the same as cloud-hosted applications. Cloud-hosted applications are applications that were originally built for on-premises and later migrated to the cloud. These apps tend to be more rigid and harder to update and scale.

## Cloud-native application development

Developing cloud-native applications requires a shift in culture and methods. To meet faster development cycles, many organizations have adopted [DevOps](https://github.com/resources/articles/what-is-devops), a modern approach to building software that combines people, technologies, and processes across development and operations. Testers, developers, operations engineers, and security professionals collaborate to deliver high-quality applications, quickly. Practices include:

**Agile methodologies:**Agile is an approach to software development that quickly responds to changing customer needs by prioritizing the continuous release of small software components rather than waiting for the entire application to be completed.**Automation:**Teams use automation for tasks such as deployment, scaling, and monitoring.**Microservices:**To create more flexible, scalable and easier-to-maintain applications, teams build them as a collection of small, independent services that each handle a specific business function.**CI**is a software development practice where developers frequently merge their code changes into a shared repository, triggering automated builds and tests to help ensure the integrated code is working correctly.**Continuous delivery (CD):**In cloud-native development, code changes are automatically built, tested, and prepared for production, allowing for predictable, frequent releases of new features.**Serverless:**Developers build and run applications without managing servers, allowing automatic scaling and cost efficiency because they only pay for the actual resource usage.

## Cloud native vs. traditional application development

While cloud-native application development assumes that requirements are always changing, traditional application development takes a slower, more methodical approach. These projects typically include detailed, documented requirements and a thorough quality assurance phase.

### Benefits of the traditional approach

Traditional application development offers stability and structure. The requirements and schedule are clear and predictable, and the lengthy quality assurance phase helps reduce bugs and other issues before the application is launched.

### Challenges of the traditional approach

Because traditional application development is so methodical, it’s also slow and expensive. If requirements change in the middle of the project, it’s difficult for the team to react. These are some of the reasons many development teams have switched to a cloud-native approach.

## Cloud-native tools and technologies

Cloud-native tools are designed to optimize the development, deployment, and management of applications in cloud environments. These are some of the most common.

### Containerization tools

Developers typically package an application and its dependencies into a standardized unit called a container, which can be deployed anywhere. These tools are crucial for cloud-native applications, especially when working with microservices.

**Examples:**

**Docker**is used to create, deploy, and run applications in containers.**Podman**is a container management tool that’s compatible with Docker but operates without requiring a daemon.**Kubernetes**is primarily a container orchestration tool but also handles the deployment, scaling, and management of containers and is often a key part of containerization in the cloud.

### Container orchestration tools

Orchestration tools automate the deployment, scaling, and operation of containerized applications. In production, these tools manage clusters of containers and help ensure that the desired state of the application is maintained.

**Examples:**

**Kubernetes**is the most widely used container orchestration tool and is known for its scalability and flexibility in managing containerized applications across clusters.**Docker Swarm**is Docker's native clustering and orchestration tool, suitable for smaller-scale applications.**Apache Mesos**is a general-purpose orchestration system that supports containers but can also manage non-containerized workloads.

### Service mesh tools

Service meshes manage communication between microservices, providing features like traffic routing, security, observability, and resilience to improve microservice-based application performance.

**Examples:**

**Istio**is a popular service mesh that provides traffic management, observability, and security for microservices deployed in Kubernetes environments.**Linkerd**is another service mesh that focuses on simplicity and performance, providing features like service discovery and load balancing.**Consul**is a tool for service discovery, configuration, and segmentation, often combined with HashiCorp’s other tools.

### CI/CD tools

[CI/CD](https://github.com/resources/articles/ci-cd) tools automate the process of code integration, testing, and deployment, ensuring frequent and reliable delivery of updates to cloud-native applications. Platforms like GitHub integrate with a variety of CI/CD tools to make it easier for teams to build, test, and deploy applications.

**Examples:**

is a cloud-based service for CI/CD that automates the process of building, testing, and deploying applications across Linux, macOS, and Windows environments.**Azure Pipelines****Jenkins**is an open-source automation server that supports CI/CD.**GitLab CI**is a CI/CD tool integrated into GitLab, which supports automated pipelines and deployment strategies.**GitHub Actions**is a feature provided by GitHub that allows teams to automate software workflows directly within the GitHub repository.**CircleCI**is a cloud-native CI/CD platform that automates the process of building, testing, and deploying software applications.**Argo CD**is a Kubernetes-native CD tool designed for declarative GitOps workflows.

### Monitoring and observability tools

Monitoring tools track the performance and health of cloud-native applications, while observability tools provide deeper insights into the behavior of applications, focusing on metrics, logs, and traces.

**Examples:**

tracks the performance, health, and availability of applications and infrastructure in the cloud. It provides insights into operations that help organizations maintain visibility over their cloud resources and applications, diagnose issues, and improve overall performance.**Azure Monitor****Prometheus**is an open-source monitoring and alerting toolkit used for collecting and storing metrics in real-time, particularly in Kubernetes and microservices environments.**Grafana**is a visualization tool often paired with Prometheus to create dashboards and monitor metrics.**Jaeger**is a distributed tracing tool for microservices-based applications, often used for observability.**Elasticsearch, Logstash, Kibana (ELK Stack)**is a suite of tools for managing logs, analyzing data, and visualizing metrics.

### Infrastructure-as-code tools

Infrastructure-as-code tools allow developers to use code to define, provision, and manage infrastructure, improving consistency and [version control](https://github.com/resources/articles/what-is-version-control) for infrastructure resources.

**Examples:**

is a management layer that allows software developers to deploy, manage, and organize Azure resources.**Azure Resource Manager****Terraform**is a widely used tool from HashiCorp that allows teams to define and provision infrastructure in the cloud using a declarative configuration language.**AWS CloudFormation**is a tool that helps AWS users define and deploy AWS infrastructure using templates.**Pulumi**is a modern infrastructure-as-code tool that uses general-purpose programming languages like Python, Go, and TypeScript to define cloud resources.

### Security tools

Cloud-native security tools help secure applications, networks, and data in cloud environments. They focus on managing access, encrypting data, and ensuring compliance.

**Examples:**

is a suite of features designed to improve the security of an organization’s codebase. It includes several key tools for scanning and identifying vulnerabilities in code and dependencies.**GitHub Advanced Security****Kube-bench**is a tool that follows best practices to check the security compliance of Kubernetes clusters.**Aqua Security**is a security platform for containers and Kubernetes that provides features like vulnerability scanning, runtime protection, and compliance monitoring.**HashiCorp Vault**is a tool for managing secrets, such as API keys and passwords, across a cloud-native infrastructure.

### Serverless computing tools

Serverless computing allows developers to focus on code instead of managing infrastructure.

**Examples:**

is a service from Microsoft that offers tools for managing containers and microservices.**Azure Serverless****AWS Lambda**is a serverless computing service that automatically manages servers.**Google Cloud Functions**is Google’s serverless offering for running and managing servers.**Knative**is an open-source framework for building, deploying, and managing serverless workloads on Kubernetes.

## AI in cloud-native development

AI is playing an increasingly important role in cloud-native development. AI-powered tools can further accelerate development cycles by assisting in automated coding, debugging, and testing. AI is also helping teams optimize cloud resources, improve performance, and reduce costs.

## Best practices for cloud-native application development

Some best practices for successful cloud-native development include:

**Adopt a DevOps mindset.**Encourage collaboration between development and operations teams.**Use microservices.**Break applications into small, loosely coupled services that can be developed, deployed, and scaled independently.**Optimize resources.**Build cloud-native applications to maximize resource efficiency and scale up or down as needed.**Automate the release pipeline.**Use container orchestration and CI/CD to simplify development, testing, and deployment of software.**Improve monitoring and observability.**Use distributed tracing tools, centralized logging, service health checks, metrics, and alerts to identify potential issues and improve performance.**Continuously learn.**Stay up to date on the latest trends and tools in cloud-native development.

## Cloud-native applications use cases

Cloud-native applications have empowered businesses across a range of industries to scale more efficiently and innovate faster. Some common use cases include:

**Finance.**The financial industry uses cloud-native applications to handle real-time transaction processing, fraud detection, and customer data management.**Healthcare.**The healthcare industry is deploying scalable systems for patient data management, telemedicine, and healthcare analytics.**E-commerce.**Retailers are creating cloud-native applications that provide personalized shopping experiences, recommendation engines, and dynamic inventory management.

These are just a few examples of how organizations are using cloud-native development to transform their products and services. To begin incorporating a cloud-native approach into your own organization, take a look at this article about [DevOps](https://github.com/resources/articles/what-is-devops) and explore DevOps platforms like [GitHub Enterprise](https://github.com/account/enterprises/new).

## Explore other resources

## Frequently asked questions

### What is cloud native?


Cloud native refers to an approach for building and running applications that fully take advantage of cloud computing. It uses tools like microservices, containers, continuous integration, and continuous delivery to create scalable, flexible, and resilient software.

### What is a cloud-native application?


A cloud-native application is one that is built and optimized for cloud environments. Developer utilize microservices, containers, and orchestration tools to build highly scalable, resilient, and easy to deploy applications.

### What is cloud-native application development?


Cloud-native application development is a set of practices that uses automation, microservices, and containerization to build modular, scalable applications.

### What is the difference between cloud native and cloud enabled?


Cloud-native applications are designed from the ground up to take advantage of cloud resources, while cloud-enabled applications are traditional, on-premises applications that have been adapted for the cloud.

### Does cloud native mean serverless?


Cloud native refers to an approach for building and running applications that fully take advantage of cloud computing. Developers often build cloud-native applications using serverless, which is a service for building and running applications without managing servers. But serverless services aren’t the only tool in cloud-native development. Others include microservices, containerization, continuous integration, and continuous delivery.

### Is cloud native the same as microservices?


Cloud native refers to an approach for building and running applications that fully take advantage of cloud computing. Developers often build cloud-native applications using microservices, which are small, independent services that each handle a specific business function. But microservices aren’t the only method or tool in cloud-native development. Others include serverless services, containerization, continuous integration, and continuous delivery.