source: https://github.com/resources/articles/what-is-an-api

# What is an API?

An API (application programming interface) is a defined set of rules that allows one piece of software to request data or actions from another. It specifies how requests are made, what information is exchanged, and how responses are returned, so systems can interact without exposing their internal code.

## API defined

API stands for *application programming interface*. An API is a set of rules and definitions that let software systems communicate with each other.

Think of an API as a common language between programs. Instead of one application needing to know how another is built internally, it uses the API to ask for data or trigger a process. This interface defines *what’s possible* between systems—what can be requested, how, and what the response should look like.

In [software development](https://github.com/resources/articles/what-is-software-development), APIs help apps, services, and systems work together efficiently. They're used in everything from mobile weather apps to ecommerce payment systems.

## Key takeaways

APIs are the standard way systems communicate across services, platforms, and devices, making them foundational to modern software architecture.

APIs come in several types based on access (open, internal, partner, composite) and protocol (REST, SOAP, GraphQL, gRPC, and others), each with different trade-offs.

APIs also play a critical role in AI systems, where they connect models to external tools and data sources—a pattern formalized by standards such as Model Context Protocol (MCP).

Securing APIs requires both authentication (verifying identity) and authorization (controlling access), along with input validation, encryption, and rate limiting.

Regular testing, versioning, and documentation are essential to keeping APIs reliable and usable over time.


## Why APIs matter

APIs matter because they let different software systems communicate, share data, and trigger actions automatically without requiring people to manually move information between applications. That automation is what allows modern apps, services, and platforms to work together in real time across devices and systems.

### APIs make it easier to:

**Connect different systems**without tightly coupling them.**Reuse functionality**instead of rebuilding it from scratch.**Speed up development**by integrating with existing services.**Scale applications**by distributing responsibilities across services.

APIs form the foundation of modern [software engineering](https://github.com/resources/articles/what-is-software-engineering) and [software architecture](https://github.com/resources/articles/what-is-software-architecture), enabling microservices, [cloud-native ](https://github.com/resources/articles/what-is-cloud-native)apps, and third-party integrations across platforms.

## The role of APIs in software architecture

In software architecture, APIs define the boundaries and contracts between system components. Each API specifies how a service can be used—what requests it accepts, what responses it returns, and how it handles errors, authentication, and version changes—so systems can interact predictably without exposing internal logic.

APIs also shape how components coordinate work. In some systems, APIs follow a request–response pattern, where one service calls another and waits for a result. In others, APIs support event-driven or orchestration patterns, where multiple services exchange data or trigger actions as part of a larger workflow. These patterns influence how systems handle latency, scaling, and coordination.

Because APIs sit at the interaction layer, they also affect runtime behavior. Decisions such as how to handle retries, timeouts, rate limits, caching, and fallback responses determine how systems behave under load or failure conditions.

APIs also provide a structured way to manage change. With clear contracts and versioning strategies, teams can update individual services without breaking existing integrations, allowing systems to evolve over time while maintaining stability.

Together, these roles make APIs a foundational building block of modern software architecture.

### History of APIs

APIs date back to the early 2000s, when companies like Salesforce and eBay began exposing web-based interfaces that let external developers interact with their platforms programmatically. The release of the representational state transfer (REST) architectural style in the year 2000 and the rise of public APIs from companies such as Amazon, Google, and X (formerly Twitter) helped establish APIs as a standard building block of modern software.

### How APIs support AI in modern systems

APIs are the integration layer that lets AI systems interact with external data, services, and tools. They allow AI to retrieve information, trigger actions, and connect outputs to real-world systems. This is the foundation of how [AI agents](https://github.com/resources/articles/what-are-ai-agents) operate—they use APIs to read data, call services, and take action on a user's behalf.

To make this interaction more standardized at scale, a related concept is the [model context protocol (MCP)](https://github.com/resources/articles/what-is-mcp-model-context-protocol). MCP defines how AI models discover and interact with external tools and data through a single, consistent interface. While APIs define how software systems exchange requests and responses, MCP standardizes how AI models find and use those APIs—acting as a structured layer on top of them.

## API benefits and impact

APIs play a critical role in modern software. By standardizing connections between applications, they reduce complexity, speed up development, and make it easier to innovate at scale.

Here are the key advantages of APIs:

### Enable digital transformation

APIs connect legacy systems with cloud services, helping organizations modernize without starting over. They bridge the gap between old and new tech stacks, making transformation practical and incremental.

### Accelerate innovation

Developers can experiment, prototype, and deploy faster by building on top of existing services. APIs make it easy to tap into advanced capabilities such as maps, messaging, or AI-assisted tools, without completely rebuilding them.

### Simplify integration

APIs define clear, consistent rules for how different systems interact, speeding up integration between internal services, third-party tools, and partner platforms.

### Support scalability and expansion

In [enterprise application development](https://github.com/resources/articles/what-is-enterprise-application-development), APIs help teams split applications into smaller, more manageable services. This makes it easier to scale parts of an app independently and extend functionality without disrupting the rest of the system.

### Reduce maintenance overhead

With APIs, each system can evolve independently as long as the interface stays stable. This isolation makes it easier to update, secure, and maintain code without breaking things downstream.

APIs are at the heart of modern software development. They’re how mobile apps talk to servers, how services share data, and how platforms grow through partnerships and [open source software](https://github.com/resources/articles/what-is-open-source-software) collaboration.

## How APIs work

At a basic level, an application programming interface acts as a messenger. It delivers requests from one system to another and brings back the response. APIs provide structure to those interactions so that software components can communicate clearly, consistently, and securely.

Let’s say that you want to use your mobile app to check the weather. When you click, the app sends a request to a weather service API, which receives that request, processes it, and returns the current forecast. The app then displays the data to you. This exchange happens over the internet, often within milliseconds.

Most APIs use HTTP to handle these requests and responses.

### The HTTP process usually includes:

**1. A request**

A request is sent from a client (such as a mobile app or frontend) to a server.

**2. An endpoint**

An endpoint defines the specific URL path that tells the API what data or action is needed.

**3. A method**

A method such as GET (to retrieve data), POST (to send data), PUT (to update), or DELETE specifies the type of request.

**4. A response **

A response is returned, usually in JSON or XML, containing the result of the request.

### What happens behind the scenes

APIs sit between layers of a system. They decouple the frontend from the backend, enabling each part to evolve independently. For example, a frontend app might talk to a payment API, which then coordinates with a third-party processor—all without exposing sensitive implementation details.

In distributed systems and microservices, APIs keep everything connected. Services talk to each other over internal APIs, passing data, triggering actions, or synchronizing updates in real time.

Beyond enabling connections, APIs establish clear expectations: how systems should interact, what inputs are valid, and how to handle failures.

## Types of APIs

APIs come in many forms, depending on how they’re designed, who uses them, and what they’re used for. Understanding the distinct API types can help you choose the right tool for the job or design one that fits your needs.

### APIs based on availability and access

#### Open APIs

Also called external or public APIs, open APIs are available to developers outside the organization. Open APIs power integrations, foster innovation, and support platform growth.

#### Open API examples

The [Stripe API](https://docs.stripe.com/apis) lets an ecommerce app send payment details to Stripe, verify whether a card payment succeeds, and return a confirmation to the customer in real time. [Google Maps API](https://developers.google.com/maps/apis-by-platform) lets apps request directions, convert addresses into coordinates, and display nearby businesses based on a user’s location. [GitHub REST API](https://docs.github.com/en/rest?apiVersion=2026-03-10) allows developers to create issues, retrieve repository data, trigger workflows, and manage pull requests programmatically.

#### Internal APIs

Internal APIs are used within a single organization. Typically unavailable to external users, internal APIs help teams manage data flow and service interactions behind the scenes.

#### Internal API examples

A retailer might use an internal API to send inventory updates from its warehouse system to its ecommerce storefront so product availability stays accurate. A streaming platform could use internal APIs to verify a user subscription, retrieve viewing history, and load personalized recommendations when the app opens.

#### Partner APIs

Partner APIs are shared with specific external developers or partners. These offer more control than open APIs and often involve authentication, usage limits, and agreements.

#### Partner API examples

The Amazon Selling Partner API lets third-party sellers retrieve order information, update shipping status, and sync product catalog data directly with Amazon’s marketplace systems. A travel booking platform might use airline and hotel partner APIs to retrieve seat availability, pricing, and reservation details, then complete the booking from a single interface.

#### Composite APIs

Composite APIs allow a single call to access multiple services or data sources and are useful in microservice architecture where multiple operations must happen together.

#### Composite API examples

An ecommerce checkout flow might use a composite API to submit a shipping address, calculate taxes, process payment, create the order, and return a confirmation in one request. A banking app could use a composite API to retrieve account balances, recent transactions, and fraud alerts from multiple internal services before displaying a customer dashboard.

### APIs based on where they run

#### Web APIs

Web APIs are the most common API type and are designed to work over the internet using HTTP. Web APIs connect web apps, mobile apps, servers, and cloud services.

#### Remote APIs

Remote APIs allow communication between software components located on different machines or networks. Web APIs are a subset of remote APIs.

## How APIs relate to web services and microservices

A web service is a software system that communicates over the internet using standardized protocols such as HTTP. Microservices are an architectural approach where an application is built as a collection of small, independent services, with each microservice being responsible for a specific function.

APIs connect all of it. They define how web services expose their functionality to the outside world and how microservices talk to each other internally. In practice, most web services are accessed through APIs, and most microservice architectures depend on APIs to coordinate work across services.

### API protocols and styles

APIs can also be grouped by how they exchange data and structure requests. This table explains the main differences between common API styles and where each one fits best.

|
|
|
|
| Uses standard HTTP methods such as GET, POST, PUT, and DELETE to work with resources. | Widely used, flexible, and easy to work with using common web tools. | Web APIs, mobile apps, and general-purpose integrations |
| Uses a strict XML-based messaging format with defined standards for requests and responses. | More structured than REST and often paired with built-in security and transaction controls. | Enterprise systems, financial services, and other environments with strict compliance requirements |
| Lets clients request exactly the fields they need from a single endpoint. | Reduces over-fetching, but requires a well-designed schema and query controls. | Apps that need to combine or tailor data from multiple sources |
| Calls a function on another system as if it were a local function call. | Focuses on actions or procedures rather than resources. | Internal systems and service-to-service communication |
| A lightweight form of RPC that uses JSON for requests and responses. | Easier to read than XML-based protocols and useful for lightweight services. | Simple remote function calls between systems |
| Uses HTTP/2 and Protocol Buffers to send structured data quickly between services. | Fast and efficient, but less human-readable than REST or JSON-based APIs. | High-performance microservices and internal distributed systems |
| Keeps a persistent two-way connection open so client and server can send data at any time. | Best when updates need to happen continuously without repeated requests. | Real-time apps such as chat, live dashboards, and collaborative tools |

Each API type and style has trade-offs. The right choice depends on your goals, systems, software architecture, and users.

## API examples and use cases

APIs power much of the digital world, often behind the scenes. APIs make services—like checking into a flight or sharing a playlist—feel seamless by connecting systems, platforms, and data.

In everyday apps, APIs power:

### Social media platforms:

APIs let apps post to your feed, pull in friend lists, or authenticate with your account. For example, logging in with GitHub or Facebook uses an API call to confirm your identity.

### Travel and booking:

When a travel site shows you flights from different airlines, it’s pulling real-time data from multiple APIs. Payment processing and booking confirmations are also API-driven.

### Weather and mapping services:

APIs provide up-to-date weather forecasts, GPS directions, and location-based search. They help mobile apps deliver timely, location-aware experiences.

### In development and DevOps, APIs support:

#### Cloud services:

Cloud services such as AWS, Azure, and Google Cloud offer APIs that let developers spin up servers, manage storage, and configure networks programmatically. APIs also underpin practices such as [infrastructure as code](https://github.com/resources/articles/what-is-infrastructure-as-code) and [containerization](https://github.com/resources/articles/containerization), where teams define and deploy environments through code rather than manual setup.

#### CI/CD pipelines:

Build tools and deployment systems use APIs to check code, run tests, and deploy updates. [Continuous integration](https://github.com/resources/articles/continuous-integration) and [continuous deployment](https://github.com/resources/articles/continuous-deployment) ([CI/CD](https://github.com/resources/articles/ci-cd)) [pipelines](https://github.com/resources/articles/pipeline) rely on APIs to connect each stage of the workflow, from code commit to production release, with services such as [GitHub Actions](https://github.com/features/actions).

#### AI-assisted development:

Tools such as GitHub Copilot use APIs to access AI models that generate or suggest code. These interactions happen in real time as you write.

### In connected systems, APIs facilitate:

#### Internet of Things (IoT):

APIs connect smart home devices, industrial sensors, and wearable tech. They allow apps to collect data, issue commands, and control devices remotely.

#### SaaS integrations:

Business tools such as customer relationship management systems (CRMs), marketing platforms, and analytics dashboards use APIs to synchronize data, automate workflows, and create unified user experiences.

APIs function as the connective tissue of software and aren’t limited to one industry or use case, so they continue to evolve.

## How to create an API

Most APIs follow a similar workflow. They plan what the API should do, build the endpoints and logic, test how it behaves, and deploy it for others to use. While the implementation details vary, the goal is to create a reliable way for systems to exchange data and trigger actions consistently.

Here's what the typical process looks like when building an API:

### 1. Define your endpoints

Start by deciding what data or actions the API should expose and how users will access them. Clear endpoint design helps developers understand what the API does and keeps requests consistent across applications.

### 2. Write request handlers

Request handlers contain the logic that processes incoming requests and returns responses. This is where the API validates data, runs actions, retrieves information, and determines what the client receives back.

### 3. Add authentication

Authentication controls who can access the API and protects sensitive systems and data. Common approaches include API keys, OAuth, and token-based authentication, each suited for different security and access requirements.

### 4. Validate inputs

Input validation checks that incoming data matches expected formats before it reaches the application logic or database. This reduces errors, improves reliability, and helps prevent common security issues such as injection attacks.

### 5. Test

Testing confirms the API behaves as expected under normal and unexpected conditions. Functional, performance, and security testing help identify issues before the API is released to production.

### 6. Deploy and document

Once the API is stable, it can be deployed for other systems or developers to use. Clear documentation helps consumers understand available endpoints, authentication requirements, request formats, and expected responses.

Learn how to build a REST API with GitHub Copilot

## API testing and maintenance

APIs are foundational to how systems interact, so ensuring they work correctly is essential. In the context of the [software development lifecycle (SDLC)](https://github.com/resources/articles/what-is-sdlc), [software testing](https://github.com/resources/articles/what-is-software-testing) and maintenance help developers catch issues early, improve reliability, and keep services running smoothly over time.

### Testing APIs

Before and after an API goes live, it needs to be tested. Common types of API testing include:

#### Functional testing

Confirms that the API performs the intended actions and returns expected results. This also supports [regression testing](https://github.com/resources/articles/regression-testing-definition-types-and-tools), where previously passing tests are re-run after changes to confirm nothing is broken.

#### Integration testing

Ensures the API works as expected when connected with other services or systems.

#### Performance testing

Measures how the API behaves under load—how fast it responds, and whether it scales.

#### Security testing

Validates authentication, authorization, and protection against threats such as injection attacks.

Tools such as Postman, Insomnia, and command-line utilities such as cURL or HTTPie make it easier to run tests manually or as part of a CI/CD pipeline.

### Maintaining APIs

Once an API is in production, keeping it stable and up to date is an ongoing task. Good maintenance practices include:

#### Versioning

This helps developers update functionality without breaking existing integrations. It’s common to manage versions via the URL path (such as /v1/) or headers.

#### Monitoring and logging

Used to track API performance, uptime, and errors in real time, monitoring and logging are useful for debugging and capacity planning.

#### Deprecation policies

Communicating clearly when older versions will be phased out gives developers time to adapt and keeps the ecosystem healthy.

#### Documentation updates

As APIs evolve, keeping documentation current and accurate is essential to ensure usability and drive adoption.

Reliable APIs build trust with users, developers, and partners. Regular testing and maintenance help ensure stability and usability over time.

## How to use an API

Using an API typically involves reading documentation, authenticating requests, sending data to an endpoint, and handling the response the API returns. While the exact process varies by platform, most APIs follow a similar workflow designed to help applications exchange data and trigger actions consistently and securely.

### 1. Read the documentation

Documentation explains what the API can do, which endpoints are available, what data each request requires, and what responses to expect. Understanding this first helps developers avoid errors and structure requests correctly.

### 2. Get your credentials

Most APIs require authentication before they accept requests. API keys, OAuth tokens, or access tokens verify the calling application and help control permissions, usage limits, and security.

### 3. Make a request

Requests are sent to an API endpoint using tools such as cURL, Postman, or application code. This step is what actually retrieves data, updates records, triggers workflows, or performs another action on the target system.

### 4. Handle the response

The API returns a response, often in JSON format, containing data, status codes, or error messages. Parsing and validating the response helps applications react correctly when requests succeed or fail.

### 5. Monitor your usage

Many APIs enforce rate limits, quota restrictions, or usage-based billing. Monitoring requests, errors, and latency helps developers maintain reliability and avoid disruptions as usage grows.

## API security risks

Because APIs are entry points to systems and data, they’re a common target for attacks. If an API isn’t secured properly, it can expose sensitive information, allow unauthorized access, or provide an entry point to larger breaches. Securing APIs is not optional, but critical.

Authentication confirms *who* is making the request, for example, verifying identity through an API key or OAuth token. Authorization determines *what* that identity is allowed to do—which endpoints, data, or actions the request can access. When either one is weak or misconfigured, vulnerabilities come into play.

### Common API vulnerabilities

#### Broken authentication:

If authentication isn’t properly implemented, attackers can impersonate users or access restricted endpoints.

#### Lack of rate limiting:

Without rate limits, APIs can be overwhelmed by brute-force attacks or misuse that leads to denial of service.

#### Insecure data exposure:

APIs that return too much data—or include sensitive information without proper filtering—can leak user or system data.

#### Improper authorization checks:

APIs must verify *what* a user is allowed to do, not just *who they are*. Skipping this step can let attackers access or modify data they shouldn’t.

#### Injection attacks:

APIs that accept user input without validation can be vulnerable to SQL, command, or script injection.

## Best practices for API security

### 1. Use authentication and authorization standards

Implement OAuth 2.0, token-based authentication, and fine-grained access controls.

### 2. Encrypt data in transit

Always use HTTPS to protect sensitive data as it moves between systems.

### 3. Validate inputs and sanitize outputs

Never trust user input. Validate everything before it reaches your logic or database.

### 4. Apply rate limiting and throttling

Set thresholds to prevent abuse, spam, or accidental overuse.

### 5. Monitor and log

Track all API activity to detect unusual behavior, debug issues, and respond quickly to incidents.

### 6. Keep documentation private when needed

Internal or sensitive APIs shouldn’t be exposed in public documentation or open developer portals.

Ensuring API security requires a lifecycle approach, with protections built in from initial design through deployment and eventual deprecation. This aligns with broader [application security](https://github.com/resources/articles/what-is-application-security) and [DevSecOps](https://github.com/resources/articles/what-is-devsecops) practices, where security is a continuous part of the development process rather than a final checkpoint.

## APIs at GitHub

At GitHub, APIs are how you connect, customize, and automate. Whether you're building internal tools, public integrations, or developer-focused products, GitHub APIs give you consistent, reliable access to the data and workflows that power software development.

One of the most widely used is the **GitHub Actions REST API**. It gives you programmatic control over workflows—so you can manage automation, deployments, and build [pipelines](https://github.com/resources/articles/pipeline) directly from your code or external systems.

### The GitHub Actions REST API enables you to:

**Trigger or cancel workflows**remotely.**Check the status of runs**and retrieve logs.**Manage artifacts**created during a build.**Control workflow permissions**and runner settings.**Monitor performance**and usage across your organization.

These endpoints are designed for flexibility. Whether you’re automating repetitive tasks, building dashboards, or integrating with third-party services, GitHub APIs provides a consistent way to interact with your repositories and CI/CD processes.

GitHub APIs are open, actively maintained, and supported by rich documentation. You can explore them, try out requests, and see how they fit into your stack.

Learn more in the [GitHub REST API docs](https://docs.github.com/rest/actions/workflows).

## Explore other resources

## Frequently asked questions

### What is an API key?


An API key is a unique identifier used to authenticate a client or application when it interacts with an API. It’s like a password issued by the API provider to track and control how the interface is used.

API keys help manage access by identifying who’s making the request and enforcing rate limits, permissions, or usage quotas. They're often included in the request header or URL and are commonly used in open or partner APIs.

While API keys offer basic authentication, they’re usually combined with other methods—such as OAuth or token-based systems—for more robust security.

### What is an API call?


An API call is a request sent from one system to another through an application programming interface. It asks the API to perform an action such as retrieving data, updating information, or starting a process, and then waits for a response.

Every time an app checks your notifications, fetches weather data, or sends a message through a third-party service, it’s making an API call. These calls typically include the endpoint being requested, the method (such as GET or POST), and any required authentication or parameters.

In most systems, hundreds or thousands of API calls happen behind the scenes to keep things running efficiently and smoothly.

### What does API stand for?


API stands for application programming interface. An API is a set of rules that lets software systems talk to each other.

APIs define how requests are made, what data is exchanged, and how systems respond, making it easier for developers to build on top of existing tools and services.

### What is API integration?


API integration is the process of connecting two or more systems using APIs so they can share data or trigger actions automatically.

It’s how apps and services work together—such as syncing customer data between a CRM and a marketing tool or pulling product info from an inventory system into an online store. API integrations reduce manual work, improve accuracy, and create more connected user experiences.

They’re common in SaaS platforms, internal tools, and modern development workflows.

### What is REST API?


A REST API is an application programming interface that follows the principles of REST, short for representational state transfer. It uses standard HTTP methods such as GET, POST, PUT, and DELETE to request and manage data.

REST APIs are stateless, meaning each request contains all the information needed to process it. They’re widely used because they’re simple, scalable, and easy to work with using common tools such as browsers or command-line utilities.

Most modern web APIs, including those on GitHub, follow REST conventions.

### What are microservices?


Microservices are an architectural approach where an application is built as a collection of small, independent services, each responsible for a specific function. Instead of deploying one large codebase, teams build, test, and deploy each service separately.

Services communicate with each other through APIs, which define how they exchange data and trigger actions. This structure makes it easier to update, scale, or replace individual parts of an application without affecting the rest of the system.

### What is the difference between MCP and API?


An API defines how two software systems send requests and receive responses from each other. MCP (Model Context Protocol) is an open standard that defines how AI models discover and interact with external tools, data, and services through a single, consistent interface. In short, APIs are the connections. MCP is how AI models find and use them.