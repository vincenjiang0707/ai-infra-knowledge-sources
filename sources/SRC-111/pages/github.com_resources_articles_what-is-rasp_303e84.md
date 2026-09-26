source: https://github.com/resources/articles/what-is-rasp

# What is runtime application self-protection (RASP)?

Learn how runtime application self-protection (RASP) safeguards software applications against runtime attacks. Explore the features and benefits of RASP and how it complements other solutions to enhance application security.

Runtime application self-protection, or RASP, is a security technology that operates within software applications to monitor, detect, analyze, and protect against malicious activity automatically in real-time while the application is running.

RASP is part of a comprehensive cloud application security strategy used to help defend against software attacks and resolve vulnerabilities.

## How RASP security works

RASP differs from other [code security tools](https://github.com/features/security/code) like [static application security testing (SAST)](https://github.com/resources/articles/what-is-sast), or web application firewalls (WAFs), by looking beyond static code. RASP analyzes and adapts the application's logic and behavior during runtime to provide more granular, accurate, and comprehensive protection than traditional security solutions.

RASP is embedded inside the software and works like an immune system for the application. RASP security provides real-time contextual monitoring and detection and delivers immediate protection by automatically stopping attacks as they occur.

Here are the key components that make RASP work:

**Integration**

Sensors embedded within an application are activated as soon as the application starts, known as runtime.

**Continuous contextual monitoring **

RASP understands the context in which the application operates and monitors contextual information inside the software during runtime. RASP analyzes traffic and user behavior, incoming requests, data flows, and execution paths to detect abnormality or vulnerability in the code.

**Detection and alerts**

When a security vulnerability or attack is detected, RASP technology issues alerts and can provide security reports on the application’s status and performance.

**Blocking**

RASP simultaneously and automatically blocks the malicious request and virtually patches the application to help prevent further attacks.

**Real-time defense**

Because RASP is embedded within the application, it instantaneously responds to threats as they occur and vulnerabilities as they’re detected.

## How RASP complements traditional security solutions

RASP is complementary to traditional security solutions like web application firewall (WAF) and intrusion prevention systems (IPS) security solutions.

**WAF solutions are an external first line of defense** and function as a perimeter sentinel to monitor, filter, and help prevent incoming malicious requests from breaking through in a user session.

**IPS operates at the network level** as a second layer of defense. An IPS detects and works to block malicious activity within the network by analyzing traffic patterns and responding to anomalies.

**RASP solutions are embedded** within the software application. With contextual deep visibility, RASP protects by identifying and blocking threats inside the app that may have been bypassed on the perimeter by WAF or at the network level by IPS.

**In a rapidly evolving cybersecurity landscape**, [application security](https://resources.github.com/security/what-is-application-security/) is more essential than ever. Combining RASP with WAF and IPS enhances security against emerging threats.

Rapidly evolving technological advancements in the cloud, state actors, and mounting regulations exert increasing pressure on software security. Leveraging the unique capabilities of different solutions can help defend against multiple cyberattack vectors and establish a more robust security posture.

**WAF + RASP creates a holistic defense.**

WAF filters traffic at the perimeter to detect malicious activity.

RASP provides deeper insights and protections unique to each app by detecting threats and vulnerabilities and responding defensively.

**IPS + RASP strengthens interstitial security.**

IPS handles incoming network-based attacks.

RASP is embedded and provides contextual awareness and protection against application-specific vulnerabilities and attacks.

Let’s explore some of the features of RASP security capabilities, and implementation strategies.

## Key features and capabilities of RASP

RASP security tools work to detect and prevent runtime attacks through embedded contextual awareness and real-time monitoring. Defense mechanism features and capabilities of RASP include:

**Application-centric defense:**By operating directly in the application layer, RASP is focused on monitoring, detecting, and protecting vulnerabilities of software components.**Zero-day attack protection:**Unknown vulnerabilities are called zero-day attacks and a top cybersecurity challenge. RASP helps block zero-day attacks before they are patched, providing real-time defense.**Precise granular-level protection:**Because RASP is embedded in an application, it monitors and provides control over an app’s behavior at the granular level and can patch vulnerabilities in real time.**Behavior analysis:**RASP uses behavior awareness and analysis to detect abnormal patterns and identify suspicious activities that might go undetected by traditional security tools.**Rule-based policy enforcement:**Using predefined security rules, RASP identifies abnormal and nefarious patterns and can prevent policy violations.**AI-powered threat detection:**Many RASP solutions use machine learning and AI to learn from an app’s behavior and identify new threats.**Agile and adaptable:**RASP doesn’t require retooling even when the application is updated or redeployed and remains effective without manual rule updates or configuration adjustments.

## Strategies to integrate and deploy RASP

RASP is easy to deploy and reduces the application’s vulnerability to threats and reduces the rate of false-positive alerts.

There are two primary methods for RASP integration and implementation. Both offer flexibility, accuracy, and proactive security for software applications.

**Direct embedding into the application**

RASP is directly embedded within the application code.

Developers don’t need to significantly modify the app’s logic.

There is minimal performance impact.

Direct embedding facilitates deep visibility into an app’s context and behavior.

Protection can be tailored to an app’s specific requirements.


**Agent-based integration**

RASP tools can use lightweight agents that run alongside the app.

Agents continuously monitor and analyze the app’s behavior during runtime.

When an event like a SQL injection violates security rules, the agent acts.

Agents integrate with orchestration tools and existing systems like SIEM or DAST.

Using APIs and web hooks, RASP can incorporate threat intelligence feeds.


Next let’s explore some of the benefits of RASP testing for organizations and software development teams.

## Benefits of RASP testing

RASP offers several real-time threat detection and response benefits for enhanced application security.

**Protection from known and unknown vulnerabilities**

RASP monitors for and detects known threats like SQL injection and cross-site scripting and can control application execution even if perimeter defenses are breached. RASP also helps protect against unknown vulnerabilities by intercepting traffic that indicates malicious activity, blocking exploitation of undiscovered threats or weak points, even if no patch or fix yet exists.

**Simplified security management **

Focusing on a single application, RASP helps simplify security management and improve accuracy using data within the application. RASP can easily integrate with other security tools, like WAF and IPS, improving security while reducing the number of developers needed to monitor the application. Developers have more time for important tasks that require their interaction.

**Lower costs**

RASP blocks attacks quickly, is less expensive than other security tools, and doesn’t require additional servers. RASP reduces infrastructure costs by preventing the unnecessary processing of bad traffic, ensuring the application only handles true requests while blocking malicious activity.

**Reduced false-positive alerts**

RASP’s contextual awareness gives it visibility into the application’s behavior and differentiates true attacks from false positives, decreasing the load on security teams so they can focus on genuine threats.

**Continuous protection in any deployment environment**

RASP dynamically adapts to the application's deployment environment, providing code-level protection in the cloud, on-premises, or in a hybrid environment, and is [DevSecOps](https://resources.github.com/devops/fundamentals/devsecops/) ready to boogie.

## Challenges of RASP implementation

Some considerations and challenges related to implementing RASP include:

**Compatibility with different application frameworks **

RASP solutions must provide consistent protection across platforms, systems, and languages, which can be challenging for organizations with diverse application ecosystems.

**Integration with existing security controls**

Traditional security solutions architecture and design differs from RASP solutions, so implementation may require adjustments.

**Potential latency issues **

RASP mechanisms can cause latency, or time lags, during application execution. Be mindful of potential latency issues when implementing RASP, including:

**Performance impact:**RASP tools can add system resource requirements due to their continuous monitoring and analysis.**Tuning and optimization:**Set tuning policies that align with the application’s specific behavior to optimize RASP and reduce application performance issues.**Vendor considerations:**Evaluate how well a specific RASP solution integrates with the existing application stack and determine if it introduces noticeable delays.**Monitoring and benchmarking:**Regularly monitor for latency introduced by RASP by conducting benchmark tests to assess impact on response times.

**Application health checks **

When implementing RASP, conducting health checks before, during, and after will help ensure app reliability related to these considerations:

**Multi-region deployment:**Each unique region should undergo its own health check to optimize RASP effectiveness.**Latency-based routing:**RASP leverages DNS records with the routing policy for latency. Conducting health checks for each region removes unhealthy regions from the routing, so requests are directed to the nearest healthy region.**Automatic failover:**When a health check detects an unhealthy region, RASP can dynamically adjust routing.**Validate application health:**Health checks ensure the app’s endpoints are reachable. Unhealthy endpoints are automatically excluded from routing.

Organizations can enhance application security and maintain a balance between protection and performance when RASP is thoughtfully implemented.

## RASP best practices

Organizations considering RASP can look to these as some best practices to optimize its effectiveness.

**Adopt a DevSecOps culture **

Taking a DevSecOps approach embeds security at the very beginning of the software development lifecycle (SDLC). Implementing RASP early in the SDLC is optimal.

**Consider the existing tech stack**

Will the RASP solution easily integrate with existing tools? Determine if you need an advanced RASP solution that can integrate with [DAST](https://resources.github.com/security/what-is-dast/), SAST, SIEM, or other systems and tools already in use.

**Choose a solution that’s easy to use**

An easy-to-use RASP solution simplifies implementation so developers can integrate it without extensive training and deploy it faster. Straight-forward RASP solutions don’t require complex configurations, offer reduced maintenance, and add no or low additional overhead.

**Configure the level of protection**

RASP protection can be adjusted to the application’s sensitivity and nature, so look for a solution that offers flexibility, scalability, and the required functionality, like blocking, alerting, and logging, and doesn’t interfere with the application's normal operation.

**Educate and train the team**

RASP works effectively when the team is trained to use it with confidence. Provide guidance on the solution’s capabilities, installation, configuration, monitoring, management, and troubleshooting. Encourage collaboration and feedback to create positive developer sentiment and experiences.

**Regularly test, monitor, and update**

Create a plan to monitor and test the RASP solution prior to full implementation to understand how it affects performance, and regularly test after implementation. Consistently monitor the RASP logs to identify anomalies or suspicious activity and adjust.

## RASP testing tools

RASP testing tools work to help provide continuous protection against software threats and attacks and are an essential component of a comprehensive application security strategy. RASP often works in unison with other security technologies like [GitHub Advanced Security](https://resources.github.com/demo/advanced-security/), WAF, ISP, SAST, and DAST. Learn more about AI-powered native application security testing with [GitHub Security](https://github.com/features/security).

## Explore other resources

## Frequently asked questions

### How does runtime application self-protection work?


Runtime application self-protection (RASP) is a security technology that operates within software applications to monitor, detect, analyze, and block malicious activity automatically while the application is running. RASP works by embedding sensors inside the software which intercept and analyze the requests and responses between the application and its users, data sources, or network services. RASP provides alerts and reports on the application's security status and performance. RASP can detect and block any malicious or abnormal activity, such as SQL injection, cross-site scripting, or unauthorized access, in real time.

### What is OS runtime protection?


OS runtime protection is another name for runtime application self-protection (RASP).

### Is Runtime app self-protection (RASP) enabled on web servers?


RASP can be enabled on web servers to enhance application security. RASP can protect both web and non-web applications because its protection features operate on the server where the application is running.

### What is the difference between WAF and RASP?


RASP differs from other application security solutions such as web application firewalls (WAFs) or [application security testing](https://resources.github.com/security/application-security-testing/) in that it is embedded into the software application. RASP can adapt to the application's logic and context and provide more granular, accurate, and comprehensive protection.

### What are the benefits of RASP in cybersecurity?


RASP offers several real-time threat detection and response benefits for enhanced application security, including:

Protection from known vulnerabilities and zero-day attacks

Application-centric defense

Simplified security management

Lower costs

Reduced false positives

Continuous and protection in any deployment environment

Precise granular-level protection

Rule-based policy enforcement

AI-powered threat detection

Agile, adaptable, flexible, and comprehensive security protection


### How is RASP deployed?


The two most common ways to integrate, implement, and deploy RASP are:

**Direct embedding into the application: **RASP is directly embedded within the application code.Developers don’t need to significantly modify the app’s logic and there is minimal performance impact.Direct embedding facilitates deep visibility into the app’s context and behavior and protection can be tailored to the app’s specific requirements.

**Agent-based integration: **RASP tools can use lightweight agents that run alongside the app to continuously monitor and analyze its behavior during runtime.When an event like a SQL injection violates security rules, the agent acts. RASP can incorporate threat intelligence feeds using APIs and web hooks, and agents can integrate with orchestration tools and existing systems like SIEM or DAST.