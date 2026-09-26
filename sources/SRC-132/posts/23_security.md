# security

source: https://aws.amazon.com/security/?nc2=h_dsc_aa_sec

# AWS Cloud Security

Proven security to accelerate innovation

## Move fast, stay secure

Strong security at the core of an organization enables digital transformation and innovation. AWS helps organizations to develop and evolve security, identity, and compliance into key business enablers. At AWS, [security is our top priority](https://aws.amazon.com/security/culture-of-security). AWS is architected to be the most secure [global cloud infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/?pg=WIAWS) on which to build, migrate, and manage applications and workloads. This is backed by the trust of our millions of customers, including the most security sensitive organizations like government, healthcare, and financial services.

## Benefits

Build, run, and scale your applications on infrastructure architected to be the most secure cloud computing environment available today. As organizations migrate and build on cloud, they need assurance that they have a secure foundation. AWS has the most proven operational experience of any cloud provider. Our cloud infrastructure is highly trusted and secure-by-design, giving customers the confidence to accelerate innovation.

Move fast and stay secure by confidently integrating and automating security into every part of your organization. Building securely should be the path of least resistance – with no tradeoff between security with speed. With security automation, teams spend their limited time on the highest value tasks, reduce human error, and scale security best practices across the organization.

Innovate with a wide portfolio of security services and partner solutions to help achieve end-to-end security for your organization. Organizations require powerful capabilities, designed and built by experts, which encode years of experience, knowledge and best practices, all available at their fingertips. They don’t want to navigate this changing threat and compliance landscape alone.

## Strategic Security

AWS is your guide in understanding and executing best practices to manage and reduce security risk, and protect your networks and data. Built by experts, AWS security, identity, and compliance services give you the confidence to keep building and innovating.

Understand and manage risk with deep visibility and automation.

Define user permissions and identities, infrastructure protection and data protection measures for a smooth and planned AWS adoption strategy.

Gain visibility into your organization’s security posture with logging and monitoring services. Ingest this information into a scalable platform for event management, testing, and auditing.

Automated incident response and recovery to help shift the primary focus of security teams from response to analyzing root cause.

Leverage event driven automation to quickly remediate and secure your AWS environment in near real-time.

## Customers

## Partners

[APN Partners](https://aws.amazon.com/security/partner-solutions/) offer hundreds of industry-leading security solutions that help customers improve their security and compliance. The scalability, visibility, and affordability our partners inherit with the cloud enables them to create world-class offerings for customers. Learn about [products and solutions](https://aws.amazon.com/security/partner-solutions/) pre-qualified by the AWS Partner Competency Program to support you in multiple areas, including: infrastructure security, policy management, identity management, security monitoring, vulnerability management, data protection, and consulting services.

These products complement existing AWS services to help you deploy a comprehensive security architecture and a more seamless experience across your cloud and on-premises environments. To learn more about the [NIST framework and our Cybersecurity Partners, click here](https://aws.amazon.com/partners/featured/cybersecurity-with-aws-partners/). In addition, refer to our [Security Solutions in AWS Marketplace](https://aws.amazon.com/marketplace/solutions/security) for a broad selection of security offerings from hundreds of independent software vendors.

## Learning

Browse resources to learn more about cloud security.

## What's new in Security, Identity, & Compliance?

[2026-09-22](https://aws.amazon.com/about-aws/whats-new/2026/09/security-hub-ai-inventory-azure-support/)

### AWS Security Hub AI Inventory adds Azure self-hosted instance support

AWS Security Hub AI Inventory now supports discovering and cataloging AI assets running on self-hosted instances in Microsoft Azure. This expansion extends Security Hub's existing self-hosted discovery capabilities beyond AWS, enabling central security teams to gain a continuously updated, organization-wide view of AI assets and their security posture across multi-cloud environments.

Security Hub leverages the software bill of materials (SBOM) analysis from Amazon Inspector, which has been enhanced to identify inference endpoints, models, and AI agents installed on Azure virtual machines, including frameworks such as Ollama, vLLM, Hugging Face TGI, and others. Each discovered AI asset is mapped to its underlying infrastructure and correlated with security findings, enabling teams to filter, group, and query their AI inventory across both AWS and Azure environments.

This capability is included with Security Hub Essentials at no additional cost. It is available in all AWS commercial Regions where Security Hub is offered. To learn more, see the [AWS Security Hub User Guide](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-v2-ai-inventory.html) and the [AWS Security Hub product page](https://aws.amazon.com/security-hub/).

[2026-09-16](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-workspaces-nvidia-blackwell-gpu-instances/)

### Amazon WorkSpaces adds support for NVIDIA Blackwell GPU instances

Amazon WorkSpaces Personal and Amazon WorkSpaces Core now support Graphics G7 bundles, built on NVIDIA RTX PRO 4500 Blackwell Server Edition GPUs and Intel Xeon 6 processors. Graphics G7 delivers up to 2.1x better performance for graphics-intensive workloads compared to previous generation Graphics G6 bundles. Four bundle sizes are available, ranging from 8 vCPUs, 32 GB of memory, and one GPU up to 48 vCPUs, 192 GB of memory, and two GPUs.

With Graphics G7, you can run demanding professional applications such as CAD/CAM, 3D rendering, scientific visualization, video editing, and AI-assisted design workflows at higher fidelity and frame rates. Each GPU provides 32 GB of GDDR7 memory, enabling larger and more complex 3D scenes and models. Graphics G7 bundles are available with Windows, including bring-your-own-license, and support both AlwaysOn and AutoStop running modes.

Graphics G7 bundles are available for both WorkSpaces Personal and WorkSpaces Core in US East (N. Virginia), US East (Ohio), and US West (Oregon). Additional Regions will be added as availability expands.

To get started, select a Graphics G7 bundle when creating a workspace in the [Amazon WorkSpaces console](https://aws.amazon.com/console/), or through your Workspaces Core partner solution. For more information on available instance types, see [WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/bundle-options.html)[ Personal Instance ](https://docs.aws.amazon.com/workspaces/latest/adminguide/bundle-options.html)[Families](https://docs.aws.amazon.com/workspaces/latest/adminguide/bundle-options.html). To learn more about G7 GPU capabilities, visit the [EC2 G7 Instance Types page](https://aws.amazon.com/ec2/instance-types/g7/). For pricing details, see [Amazon WorkSpaces Personal Pricing](https://aws.amazon.com/workspaces/desktop-as-a-service/pricing/) or [Core Bundles Pricing](https://aws.amazon.com/workspaces/vdi-partners/pricing/).

[2026-09-15](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-sts/)

### AWS STS simplifies session token size limits and adds session token size monitoring

AWS Security Token Service (STS) now enforces a single 4,096-byte size limit on session tokens. Previously, STS enforced separate limits on session token size and passed-in parameters (i.e., inline policies, managed policies, and session tags). STS has removed that separation, providing more flexibility for larger combinations of session policies and session tags.

Additionally, STS now returns response elements indicating session token size and percentage utilization relative to the token size limit. STS logs these values in AWS CloudTrail and publishes corresponding metrics in Amazon CloudWatch. A new optional API parameter also lets you generate larger session tokens (up to the 4,096-byte limit) to test whether your applications and infrastructure can handle them.

These capabilities are available in all commercial AWS Regions, the AWS GovCloud (US) Regions, and the AWS European Sovereign Cloud Region.

To learn more, please read the [AWS Security Blogpost](https://aws.amazon.com/blogs/security/aws-sts-simplifies-session-token-size-limits-and-adds-session-token-size-monitoring/), [AWS IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html), and [AWS STS API Reference](https://docs.aws.amazon.com/STS/latest/APIReference/Welcome.html).

[2026-09-14](https://aws.amazon.com/about-aws/whats-new/2026/09/root-user-regional-resiliency/)

### AWS improves regional resiliency for root user sign-in

AWS root user sign-in is now served across US East (N. Virginia), US East (Ohio), and US West (Oregon), with sign-in traffic distributed across all three Regions. This change reduces reliance on US East (N. Virginia) and improves resiliency during service disruptions. AWS automatically routes your root user sign-in to a supported Region without requiring you to select a Region or change how you sign in. This improvement is available now for all AWS accounts.

In AWS CloudTrail, ConsoleLogin events for root user sign-ins are recorded in the Region that processed the sign-in request. To maintain full visibility into root user sign-in activity, update your monitoring and alerting to cover US East (N. Virginia), US East (Ohio), and US West (Oregon).

To learn more, see the [AWS Sign-In documentation](https://docs.aws.amazon.com/signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.html) and the [CloudTrail ConsoleLogin event reference](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-aws-console-sign-in-events.html#cloudtrail-event-reference-aws-console-sign-in-events-root).

[2026-09-09](https://aws.amazon.com/about-aws/whats-new/2026/09/private-ca-eks-addon-ad-govcloud/)

### AWS Private CA EKS add-on and Connector for AD now available in AWS GovCloud (US)

AWS Private Certificate Authority (AWS Private CA) announces the availability of the AWS Private CA Connector for Kubernetes as a managed Amazon EKS add-on and the AWS Private CA Connector for Active Directory in AWS GovCloud (US-East) and AWS GovCloud (US-West) Regions. These launches expand certificate automation capabilities available to AWS GovCloud (US) customers managing government workloads.

The AWS Private CA Connector for Kubernetes EKS add-on provides simplified installation, configuration, and lifecycle management through the EKS console, CLI, and API. The connector works with cert-manager to automate certificate requests, distribution to Kubernetes secrets, and renewal, enabling TLS for ingress controllers and securing service-to-service communication in service meshes such as Istio and Linkerd.

The AWS Private CA Connector for Active Directory enables AWS GovCloud (US) customers to use AWS Private CA as their certificate authority for Active Directory-enrolled objects. The connector provides automatic certificate issuance to domain-joined users, computers, and other objects through familiar Microsoft certificate enrollment interfaces, supporting enterprise scenarios including smart card authentication, LDAPS, and network device authentication (802.1x).

AWS Private CA secures private key material using FIPS 140-3 Level 3 hardware security modules (HSMs).

To get started, see the [AWS Private CA product page](https://aws.amazon.com/private-ca/), the [Amazon EKS add-ons user guide](https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html), and the [AWS Private CA Connector for Active Directory documentation](https://docs.aws.amazon.com/privateca/latest/userguide/connector-for-ad.html).

[2026-09-08](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-builder-id-recovery-mfa-third-party/)

### AWS Builder ID adds recovery options and multi-factor authentication for third-party logins

AWS Builder ID, your personal profile for accessing AWS applications including AWS Builder Center, AWS Training and Certification, Amazon Quick and Kiro, now offers new ways to protect and recover your profile. You can add a recovery email and use new self-service options to regain access if you're locked out. You can also register multi-factor authentication (MFA) devices for any sign-in method, including third-party logins such as Google or Apple.

With these enhancements, you have more self-service options to recover your AWS Builder ID. Adding a recovery email provides a second verification factor that makes self-service recovery possible for more scenarios without the need to contact AWS Support. You can reset a forgotten password using a link sent to your primary or recovery email. If you lose access to your MFA device, you can regain access by verifying both your primary and recovery emails. If you use Google, Apple, GitHub or Amazon to sign in to Builder ID, you can now register MFA devices directly in AWS Builder ID, bringing the same strong account protection previously available to email and password users, and you can permanently switch your sign-in method to an email address and password if you lose access to the third-party account.

To learn more about AWS Builder ID and how to set up account recovery and MFA, visit the [AWS Builder ID documentation](https://docs.aws.amazon.com/signin/latest/userguide/sign-in-builder-id.html).

[2026-09-04](https://aws.amazon.com/about-aws/whats-new/2026/09/guardduty-optional-detection-rules/)

### Amazon GuardDuty adds optional threat detection rules

Amazon GuardDuty now offers Custom Detection Rules, a library of 35 prebuilt, opt-in rules for CloudTrail management events that let you extend threat detection coverage to match your environment. Custom Detection Rules produces 26 unique finding types mapped to 10 MITRE ATT&CK® tactics, without the heavy lifting of log ingestion, normalization, or storage.

Some threat techniques, such as sharing an AMI externally, disabling flow logs, or signing in without MFA, could be meaningful indicators of compromise in some accounts but routine in others. Custom Detection Rules lets you enable these detections only where the activity is unexpected — expanding your TTP coverage tailored to your environment.

To get started, browse Custom Detection Rules via the GuardDuty console or API, and enable rules in dry-run mode to evaluate detection efficacy before going live.

Custom Detection Rules is available in all AWS commercial Regions and the AWS GovCloud (US) Regions. To learn more, see [Amazon GuardDuty Custom Detection Rules](https://docs.aws.amazon.com/guardduty/latest/ug/custom-detection-rules.html). To receive programmatic updates on new Amazon GuardDuty features and threat detections, subscribe to the [Amazon GuardDuty SNS topic](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_sns.html).

[2026-09-03](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-workspaces-applications-nvidia-blackwell-gpu-instances/)

### Amazon WorkSpaces Applications adds support for NVIDIA Blackwell GPU instances

Amazon WorkSpaces Applications now supports Graphics G7 instances, powered by NVIDIA RTX PRO 4500 Blackwell Server Edition GPUs and Intel Xeon Scalable (6th Gen) processors. G7 instances deliver up to 2.1× better performance for graphics-intensive workloads compared to previous generation G6 instances.

With Graphics G7, customers can stream demanding professional applications such as CAD/CAM, 3D rendering, scientific visualization, video editing, and AI-assisted design workflows at higher fidelity and frame rates. G7 instances feature 32 GB of GDDR7 GPU memory per GPU and 2.67× faster memory bandwidth, enabling streaming of larger, more complex 3D scenes and models. Six instance sizes are available, with 1 to 8 GPUs, vCPUs ranging from 8 to 192, and system memory from 32 GB to 768 GB.

Graphics G7 instances are available in US East (N. Virginia), US East (Ohio), and US West (Oregon). Additional regions will be added as availability expands.

To get started, select a Graphics G7 instance when launching an image builder or creating a new fleet in the [Amazon WorkSpaces Applications console](https://aws.amazon.com/console/). For more information on available instance types, see [WorkSpaces Applications Instance Families](https://docs.aws.amazon.com/appstream2/latest/developerguide/instance-types.html). To learn more about G7 GPU capabilities, visit the [EC2 G7 Instance Types page](https://aws.amazon.com/ec2/instance-types/g7/). For pricing details, see [Amazon WorkSpaces Applications Pricing](https://aws.amazon.com/workspaces/applications/pricing/).

## AWS Security, Identity, & Compliance Events

## Found something suspicious?

Learn about our practice for addressing potential vulnerabilities in any aspect of our cloud services.
