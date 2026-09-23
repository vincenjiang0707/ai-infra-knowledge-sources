# Deploy Hugging Face models on Amazon SageMaker AI with coding agents

source: https://aws.amazon.com/blogs/machine-learning/deploy-hugging-face-models-on-amazon-sagemaker-ai-with-coding-agents/
published: Fri, 18 Sep 2026 15:25:23 +0000

[Artificial Intelligence](https://aws.amazon.com/blogs/machine-learning/)

# Deploy Hugging Face models on Amazon SageMaker AI with coding agents

Deploying a Hugging Face model to production means making a dozen decisions: choosing the right serving container for the model’s architecture, confirming the current image tag for your AWS Region, and matching an instance type to the model’s memory footprint. Beyond infrastructure, you must wire autoscaling so you don’t burn GPU hours on an idle endpoint. You also set Amazon CloudWatch alarms that catch silent failures before your users do. After you’ve made those decisions, [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ai/) collapses that work into hours.

This kind of structured, repeatable work is exactly what coding agents, like [Kiro](https://kiro.dev/) and [Claude Code](https://www.anthropic.com/claude-code), are built for. It’s tempting to describe a model to deploy in a coding agent, walk away, and come back to a working endpoint. In practice, an unguided coding agent might make wrong decisions, producing endpoints that are fragile, costly, or quietly wrong. The problem gets worse for newer models, since their training data might not include the latest deployment knowledge.

In this post, you learn how to deploy production-ready Hugging Face models on SageMaker AI using agent skills. You install six skills from [Hugging Face Skills](https://github.com/huggingface/skills), point a coding agent at a Hugging Face model, and get back a real-time endpoint with autoscaling, [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) alarms, the correct serving container from the [AWS Deep Learning Containers (DLC)](https://aws.github.io/deep-learning-containers/reference/available_images/) catalog, and a verified teardown path. Real-time endpoint is the default, but the skills also support real-time with scale-to-zero, serverless inference, asynchronous inference, batch transform, and Amazon Bedrock Custom Model Import. The skills are open source, use only Python and the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/), and work unchanged on macOS, Linux, and Windows.

## The problem with an unguided coding agent

To show what the skills actually prevent, it helps to watch what a capable agent does without them. We tested both Kiro (with Auto or Claude Fable 5) and Claude Code (with Opus 4.8) for the request:

Both coding agents initially chose Text Generation Inference (TGI) as the serving container to deploy, an understandable choice given that TGI was the default for years and model training data is full of tutorials that reach it. But the TGI build available in the Region predated Qwen3’s architecture and couldn’t load the model. The endpoint failed its health check. The agent bumped the TGI version, redeployed, failed again, and pivoted to vLLM. This resulted in multiple deployment failures, each of which billed GPU time as it started and then crashed.

The second request failed more quietly. We asked the same agent to deploy a multimodal mixture-of-experts (MoE) diffusion model released only weeks before the test. The coding agents confirmed it existed, and again wrote a script built on TGI, a text-generation server with no backend for a discrete-diffusion image-text model. Nothing failed loudly. You would find out only when the endpoint refused to come up.

The two runs share the same root cause: missing deployment facts, not reasoning failure. The agent planned and debugged well. What it lacked was current, specific knowledge. Recent Qwen models need vLLM. Python 3.13 has no working wheels for much of the machine learning (ML) stack. Container images should be resolved from the published AWS Deep Learning Containers catalog. This knowledge changes faster than model weights get updated. So we make it into editable skill files rather than rely on the latest release of a model to absorb it.

Table 1 compares the model deployment made by the unguided agent against the agent with skills installed.

Deployment concerns |
Unguided agent |
With skills |
| Serving container | TGI first → health-check failure → vLLM | vLLM, chosen before any resource was created |
| Image URI | Discovered by trial and error | Resolved from the AWS DLC catalog, with fallback when the registry query was denied |
| Autoscaling | None | Target tracking, 1–2 instances |
| Monitoring | None | Three CloudWatch alarms (latency, errors, overhead) |
| Documentation | README recommended TGI, the SageMaker SDK, and Python 3.13 | Plan and scripts matched what actually ran |
| Region, role, environment | Correct natively | Correct by rule |
| Teardown | A script you could run | Run, then verified the resources were gone |

*Table 1: The same request, run by the agent without and with the skills installed*

The rest of this post shows how we deploy Hugging Face models on SageMaker AI endpoints (the right-hand column of Table 1) using agent skills.

## Agent skills for deploying Hugging Face models on SageMaker AI

Six skills from the [Hugging Face Skills](https://github.com/huggingface/skills) GitHub repo cover the end-to-end deployment workflow. The planner skill orchestrates the other five, as shown in the following diagram.

## An agent skill example

An [agent skill](https://agentskills.io/home) is an open standard package consisting of a folder with a required SKILL.md file. This file includes metadata (name and description, at minimum) and instructions that tell an agent how to perform a specific task. Skills load through progressive disclosure. An agent reads a skill on demand when the current task matches its description. The following is a trimmed version of the `hf-cloud-serving-image-selection`

skill.

## End-to-end model deployment phases

The skills drive five AWS services. [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ai/) hosts the endpoint, [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) provides the execution role. [Amazon Elastic Container Registry (Amazon ECR)](https://aws.amazon.com/ecr/) and [AWS Deep Learning Containers](https://aws.github.io/deep-learning-containers/reference/available_images/) supply the serving image, while [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) powers the alarms. All helper scripts in skills call these services through Boto3 and the AWS Command Line Interface (AWS CLI), which retains full control over what gets created. The SageMaker Python SDK works too, but the skills default to Boto3.

The deployment follows six phases:

- Discover the AWS context (profile, Region, account, and caller identity) with read-only calls.
- Set up an isolated Python environment with a supported Python version and a current
`boto3`

. - Find an existing SageMaker AI execution role and create one only if none exists and you have permission.
- Select the serving container family and resolve a current image URI from the AWS DLC catalog.
- Create the model, endpoint configuration, and endpoint, and then attach autoscaling and Amazon CloudWatch alarms.
- Run a smoke test against the live endpoint and report the result.

## Prerequisites

To follow along, you need the following:

- An
**AWS account**with permission to use Amazon SageMaker AI, including an existing SageMaker AI execution role. The skills can find one automatically or create one if none exists and your credentials allow it. **AWS CLI v2**, configured with credentials for that account.**Python 3.10, 3.11, or 3.12**. Python 3.13 or later isn’t supported because much of the ML stack does not yet publish wheels for these versions.- A
**coding agent**that supports skills. This post uses[Kiro IDE](https://kiro.dev/ide/). - Git, to clone the skills repository.

This post deploys `Qwen/Qwen3-0.6B`

to a single `ml.g5.xlarge`

real-time inference instance in `US East (N. Virginia) Region (us-east-1)`

. Confirm your account has available quota for this instance type before you start.

Note that a real-time endpoint bills continuously whether it serves traffic, so delete the endpoint when you’re done or follow the teardown steps at the end of this post.

## Install the skills

Kiro supports two skill scopes: workspace and global. The workspace skills reside in your project under .kiro/skills/ and apply only to project-specific workflows. The global skills reside under ~/.kiro/skills/ and are available across all workspaces.

To install the six skills from the [Hugging Face Skills](https://github.com/huggingface/skills) GitHub repo in the current workspace, enter the following request in a Kiro default agent chat session:

Kiro summarizes the installed files as shown in Figure 1. Note that this post tested and used the repo with a specific SHA: `f3186efbbc322121eb5d0f31e8a1d669ee961159`

.

To confirm all six skill directories are present, enter `/`

in the Kiro chat session to see available skills as slash commands, as shown in Figure 2.

## Deploy a model with Kiro

With the skills installed, you describe the model to the agent in plain language, and the planner skill takes over. You don’t specify which container family to use, how to find the execution role, or which production defaults to attach, because those decisions live in the skills.

Enter the following request in the Kiro chat session:

To deploy the model, complete the following steps:

**Review the plan.** The agent writes a deployment plan to a file and waits for your approval before creating any billable resources.

**AWS context discovery and container selection.** The agent discovers the AWS context (profile, Region, account). The `hf-cloud-serving-image-selection`

skill selects vLLM for Qwen3 and resolves the image URI from the AWS DLC catalog.

**Approve the deployment** when the agent asks. The `hf-cloud-sagemaker-production-defaults`

skill creates the model, endpoint configuration, and endpoint as a unit, then attaches autoscaling and CloudWatch alarms.

**Verify.** Review the smoke-test result the agent reports after the endpoint reaches `InService`

.

The following lines come from the deployment log the agent kept during the run:

For a gated model, add a `HUGGING_FACE_HUB_TOKEN`

environment variable.

## Resolve the execution role

Deployments often stop at the execution role when calling `iam:CreateRole`

fails on a corporate account whose AWS IAM Identity Center session has no IAM write access. The `hf-cloud-sagemaker-iam-preflight`

skill reverses the order: find first, create only as a last resort.

Its `check_role.py`

script searches the account for existing roles that match patterns such as `AmazonSageMaker-ExecutionRole-*`

and `*SageMaker*Execution*`

, and ranks them by last-used date. It also validates the trust policy and returns the Amazon Resource Name (ARN). It creates a role only when none exists and the caller has `iam:CreateRole`

permission. Note that the created role carries `AmazonSageMakerFullAccess`

. We recommend updating the role to grant only the permissions it needs, following the principle of least privilege.

## Apply production defaults

The `hf-cloud-sagemaker-production-defaults`

skill turns an endpoint from a demo into a production deployment. It applies the defaults in Table 2 to every endpoint, establishing an operational baseline. For production deployment, you need to add user-specific configurations, such as Amazon Virtual Private Cloud and AWS Key Management Service configurations.

Resource |
Name |
Billing |
| Model | `qwen3-06b-internal` |
none |
| Endpoint config | `qwen3-06b-internal-20260904-1913-config` |
none |
Endpoint |
`qwen3-06b-internal-20260904-1913` |
$1.408/hr per instance |
| Autoscaling target + policy | `endpoint/.../variant/AllTraffic` , min 1 max 4 |
none |
| CloudWatch alarms x3 | `<endpoint>-Invocation5XXErrors` , `-ModelLatencyP99` , `-OverheadLatencyP99` |
negligible |

*Table 2: Production defaults the skill applies to every endpoint*

## Decisions the coding agent made on its own

Agent skills define the workflow, but the coding agent still makes judgment calls within it. In one case, when the agent queried Amazon ECR for the newest image tag, the call was denied because the IAM Identity Center role lacked ecr-public:DescribeImages permission. Rather than fail the deployment, the agent fell back to the known-good tag the skill ships as a safety net and recorded the reason in the log. In another case, after the smoke test returned HTTP 200, the agent noticed that the actual answer was never emitted. This is because the model’s reply was truncated at max_tokens while still inside the Qwen3 reasoning block. The agent flagged this in the log as a configuration issue: the calling application should raise the token limit rather than treat the test as a pass.

## Clean up

A real-time endpoint bills for its instance the entire time it exists. Delete the resources you created to avoid ongoing charges. The `sagemaker-production-defaults`

skill includes a `teardown.py`

script that removes the deployment resources and then confirms they’re gone.

To clean up, complete the following steps:

- Ask the agent to tear down the deployment or run
`teardown.py`

directly with the endpoint name and Region. - Confirm the script reports the endpoint, endpoint configuration, and model as deleted. The script verifies the deletion.
- Check that the autoscaling policy and CloudWatch alarms have been removed. Delete any that remain.

## Conclusion

Six reusable agent skills turn an unguided coding agent into one that deploys Hugging Face models on SageMaker AI endpoints with production-ready features. Each deployment includes the proper container, autoscaling, CloudWatch alarms, and a verified teardown path. Without these skills, agents reach for outdated containers, skip production safeguards, and leave misleading documentation. This post walks through each skill: AWS context discovery, Python environment setup, IAM role resolution, container selection from the AWS DLC catalog, and deployment with production defaults.

To get started, install the skills from the [Hugging Face Skills](https://github.com/huggingface/skills) GitHub repo and deploy your first model. The skills are open source and contributions are welcome.

Teams can also use Amazon SageMaker JumpStart to deploy a set of popular Hugging Face models directly from the console, and Inference Recommendations to automatically benchmark and select the optimal instance type for their workload.

## Learn more

[Amazon SageMaker AI Developer Guide – Real-time inference](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html)

[AWS Deep Learning Containers documentation](https://docs.aws.amazon.com/deep-learning-containers/latest/devguide/what-is-dlc.html)