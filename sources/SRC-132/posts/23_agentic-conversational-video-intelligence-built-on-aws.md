# agentic-conversational-video-intelligence-built-on-aws

source: https://aws.amazon.com/blogs/machine-learning/agentic-conversational-video-intelligence-built-on-aws/

[Artificial Intelligence](https://aws.amazon.com/blogs/machine-learning/)

# Agentic conversational video intelligence built on AWS

With video intelligence powered by agentic AI, you can ask natural language questions about uploaded videos and get answers within seconds. Organizations across media, security, insurance, and professional services are generating more video than their teams can review. Meeting recordings accumulate in shared drives, and security cameras capture weeks of unreviewed footage. Field inspection videos sit in object storage long after the initial review. The information inside these videos is often valuable: a design decision discussed three weeks ago, the exact moment a person arrived at a door, or the sequence of events leading to a vehicle collision. But accessing it has traditionally required watching hours of content manually. The alternative, building custom machine learning (ML) pipelines for each specific question type, demands significant development effort. Each new use case meant new development work:

- A transcription pipeline for meeting queries.
- A computer vision pipeline for visual search.
- A face-matching integration.

In this post, we walk through the architecture and key patterns for building a video intelligence solution that accepts natural language questions and returns answers from video content. The solution uses an agentic architecture that decides at runtime which AWS services to invoke. For previously analyzed content, responses return in under a second. Initial analysis of new videos takes 5–10 minutes depending on length and services required. The complete implementation is available in the [companion GitHub repository](https://github.com/aws-samples/sample-media-analysis-agent).

Rather than pre-building a fixed pipeline for each question type, we use the Strands Agents SDK to create a single AI agent that orchestrates [Amazon Bedrock](https://aws.amazon.com/bedrock/), [Amazon Rekognition](https://aws.amazon.com/rekognition/), and [Amazon Transcribe](https://aws.amazon.com/transcribe/) based on what the user asks. A major media and entertainment company adopted this approach during an AWS Professional Services engagement. With this solution, their consultants can query recorded discovery session content, extracting design decisions, action items, and stakeholder positions. The result: a reduction in manual review time of approximately 80 percent across a backlog of more than 200 multi-hour recordings, based on the customer’s internal before-and-after comparison of analyst hours per recording (not independently verified).

## Solution overview

The solution is an AI agent that accepts video files and makes their content instantly queryable through natural conversation. A user can upload a 90-minute meeting recording and ask “What decisions were made in this meeting?” or “Did anyone mention the budget timeline?” The agent determines whether to invoke transcription, visual analysis, or both, then synthesizes the results into a coherent answer. The same system handles security footage queries (“Did this person appear?”), content analysis (“Summarize the first 30 minutes”), and investigative questions (“Which vehicle changed lanes before the collision?”). No separate processing pipelines are required for each use case.

The following screenshot shows the interface that provides a chat panel for natural language queries and a sidebar for file uploads and analysis mode selection.

The key insight is that the pipeline is determined at runtime. The agent calls Amazon Transcribe for spoken-content questions, turns to Amazon Rekognition for face matching, and reuses cached results for follow-up questions about previously processed content. The model handles the routing, not application code.

## Prerequisites

To follow along with the implementation in this post, you need:

- An AWS account with access to Amazon Bedrock (Anthropic Claude Sonnet enabled) and
[Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/). For document processing, either Amazon Bedrock Data Automation (BDA) or Amazon Rekognition and Amazon Transcribe is required. See[Supported models by AWS Region in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html). - Python 3.11 or later with the Strands Agents SDK installed (
`pip install strands-agents strands-agents-tools`

). - AWS Command Line Interface (AWS CLI) configured with AWS Identity and Access Management (IAM) permissions for the services listed earlier.
- Basic familiarity with AI agent concepts such as tool use and reasoning loops.

## Architecture

The system consists of an agent orchestrator connected to multiple AWS AI services, with Amazon S3 providing storage for uploaded videos and cached analysis outputs. The agent orchestrator is the reasoning engine. It’s built with the Strands Agents SDK and powered by Amazon Bedrock, using Claude Sonnet or another large language model (LLM) that supports tool use. It receives natural language queries from users and determines which tools to invoke based on the question, sequences multiple service calls when needed, and synthesizes the results into conversational responses. The agent maintains conversation history, so follow-up questions build on prior analysis without reprocessing.

Amazon Rekognition provides visual analysis, including detecting objects, scenes, activities, and faces in video frames. The agent invokes Amazon Rekognition when the user’s question concerns something visible in the video. Amazon Transcribe converts spoken audio to text with automatic language detection across more than 100 languages (see Amazon Transcribe supported languages) and speaker diarization. The agent uses Transcribe when the question relates to spoken content. Amazon Bedrock Data Automation (BDA) offers an alternative analysis path that combines video summary, chapter detection, and full transcription in a single API call. This is useful when the user wants comprehensive analysis in one step, or when Amazon Rekognition or Transcribe aren’t available. All uploaded videos and analysis outputs are stored in Amazon S3 with per-user prefixes for multi-tenant isolation.

These three services are the starting set, not a fixed one. Because the agent selects tools from their descriptions rather than from hard-coded workflow logic, the same architecture accepts additional services as tools. We return to this point in *Extending beyond video*. For production deployments, we recommend adding Amazon Bedrock Guardrails to enforce content filtering and grounding checks on agent responses, particularly for face-matching and surveillance use cases where responsible-AI controls are essential.

## How agentic orchestration works

In a conventional video analysis application, the developer defines a fixed processing pipeline: upload the video, run transcription, perform visual analysis, present results. This approach processes every video through the same steps regardless of the specific query, and users wait for the full pipeline to complete before asking questions. The agentic approach inverts this model. With minimal pre-processing limited to uploading video files to an S3 bucket, the agent reasons about each question independently and calls only the services needed to answer it.

When a user submits a query, the agent first parses the intent: the user wants a transcript summary, a visual search, or a face match? Then it checks whether relevant analysis has already been performed and cached. If not, it selects the appropriate tools, executes them (potentially in sequence when one tool’s output feeds another), and combines the results into a natural language answer. In our testing with 60-minute videos, the first question about a video typically takes 5–10 minutes (while transcription or visual analysis runs). Subsequent questions about the same content return in under a second because the agent reuses cached results. Actual times vary based on video length, resolution, and the AWS services invoked.

### Configuring the agent

The following code shows the complete agent setup. We define the model provider, a system prompt that guides the agent’s reasoning behavior, and the set of available tools. With Strands, the entire orchestration logic (deciding which tools to call, in what order, and how to combine their outputs) is handled by the LLM rather than application code. We show two representative tool implementations (`search_faces_in_video`

and `analyze_with_bda`

). The remaining tools, including `transcribe_video`

and `analyze_video_visuals`

, follow the same pattern and are available in the [GitHub repository](https://github.com/aws-samples/sample-media-analysis-agent).

The production system prompt spans approximately 250 source lines. The following abbreviated example illustrates three representative policies (cache reuse, service fallback, and multi-modal orchestration) rather than reproducing the prompt verbatim:

The rest of the production prompt inventories the available tools and defines workflows for file selection, cache reuse and explicit re-analysis, BDA setup and access-denied fallback, reference-image search, transcription and captions, sports highlights, architecture diagrams, and choosing between BDA and service-specific analysis. It also standardizes unified multi-file responses, requires confirmation before cleanup, reuses prior results for follow-up questions, and applies scope and upload-progress guardrails.

With this configuration, the agent handles the routing, tool sequencing, and response synthesis autonomously. Adding a new capability (for example, detecting on-screen text) requires only defining a new tool function and adding it to the tools list. No workflow logic changes are needed.

### Defining tools with the @tool decorator

Each AWS service is exposed to the agent as a Python function decorated with `@tool`

. The function signature defines the parameters, and the docstring tells the agent when and how to use it. This docstring is critical: It serves as the agent’s instruction manual for the tool. The following example shows the face search tool that wraps Amazon Rekognition:

The following example shows the BDA tool, which provides comprehensive video analysis (summary, chapters, and transcript) in a single API call:

### Multi-step reasoning in action

To illustrate how the agent chains multiple tool calls, consider a user who uploads a reference photo and asks “Did this person appear in my security footage?” The agent must first index the reference face, then search for it in the video. These are two sequential operations that depend on each other. The following trace shows the agent’s internal reasoning:

The agent determined the correct sequence of operations and handled the dependency between them (the face search requires an indexed collection). It then presented the results conversationally. No application code defined this sequence. The model reasoned through it based on the tool descriptions and the user’s question.

For comprehensive analysis (when the user asks “analyze this video” or “summarize this recording”), the agent can invoke Amazon Bedrock Data Automation (BDA) instead of calling Amazon Rekognition and Transcribe separately. BDA produces a video summary, chapter-by-chapter breakdown with timestamps, and full transcript in a single asynchronous API call:

When results are ambiguous, the agent communicates uncertainty explicitly. A borderline confidence score (for example, 62 percent) produces a qualified answer: “I found a possible match at 14:32, but the confidence is low, so you may want to verify manually.” If transcription fails because of poor audio, the agent suggests alternatives: “The audio quality is too low for reliable transcription. Would you like me to try visual analysis of the presentation slides instead?”

## Example use cases

The agentic pattern applies broadly to scenarios where users need to extract specific information from video content without knowing in advance which analysis type is required.

**Meeting intelligence –** A team member joining a project mid-stream uploads prior meeting recordings and asks targeted questions: “What architecture decisions were made in April?”, “When did the team agree to use GraphQL?”, or “Summarize discussions about the authentication approach.” The agent transcribes, searches, and summarizes, returning answers with timestamps that reference the specific moment in the recording.

**Security and access monitoring –** A building manager uploads lobby camera footage with a photo of an expected visitor and asks “Did this person enter the building this week? When?” The agent runs face matching against the video and returns specific timestamps with confidence scores.

**Claims investigation –** An insurance adjuster uploads dash-cam footage and asks “Describe the sequence of events before the collision” or “Which vehicle was in the wrong lane?” The agent combines visual scene analysis with audio (verbal reactions, horns) to reconstruct the event timeline.

## Extending beyond video with a stable tool contract

The three examples above all analyze video, but nothing about the architecture is video-specific. The agent selects tools from their docstrings, so adding a new capability (or a new modality entirely) is a matter of wrapping another service as a `@tool`

function and describing when to use it. No workflow logic changes. The same orchestrator, cache, and per-user isolation apply unchanged.

That makes the pattern a general template for multi-modal AI assistants, using either AWS services or third-party models:

**Document and diagram understanding with Amazon Textract.**A discovery session rarely lives only in video. Add a Textract tool to extract text, tables, and form fields from architecture diagrams and working documents supplied as PDFs, and the agent can cross-reference what was drawn on a whiteboard with what was said in the recording. This enriches the same conversational session that already answers questions about the meeting audio.**Clinical conversations with AWS HealthScribe.**Point the same pattern at a clinician-patient audio file and a HealthScribe tool returns a structured clinical note (a turn-by-turn transcript plus extracted sections such as chief complaint and treatment plan), so a user can ask “What follow-up was recommended?” against the recording.**Entity and sentiment extraction, or a third-party model.**An Amazon Comprehend tool can pull entities, key phrases, and personally identifiable information (PII) from any transcript the agent produces. A model available on Amazon Bedrock (including third-party models) can be wrapped the same way for domain-specific reasoning.

In each case the extension point is the tool contract, not the pipeline. A team that has built the video assistant already has the scaffolding (orchestration, caching, authentication, and per-user isolation) to stand up an AI assistant for a different modality by adding tools.

## Cost considerations

The per-query cost depends on which AWS services the agent invokes. After the initial analysis (transcription or visual processing), follow-up questions about the same video only incur Amazon Bedrock reasoning costs because results are cached. The following table shows approximate costs for a 60-minute video:

Service |
Operation |
Approximate cost |
| Amazon Transcribe | 60-minute audio transcription | $1.44 |
| Amazon Rekognition | Face search (60-min video) | $6.00* |
| Amazon Rekognition | Label detection (60-min video) | $6.00* |
| Amazon Bedrock | Agent reasoning (per turn) | $0.05–$0.15 |
| Amazon S3 | Storage (500 MB, 24 hours) | <$0.01 |

*The $6.00 Amazon Rekognition cost is one-time per-video costs (subsequent queries only incur Bedrock reasoning costs).*

Based on AWS service pricing as of July 2025 and the preceding cost table, a typical transcript-based query on a 60-minute video costs approximately $1.50 for the initial transcription plus Bedrock reasoning. Subsequent questions about the same transcribed content cost only $0.05–$0.15 per turn, covering only the Bedrock inference call. Actual costs depend on model selection, input length, and AWS Region. For current pricing, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/), [Amazon Transcribe pricing](https://aws.amazon.com/transcribe/pricing/), and [Amazon Rekognition pricing](https://aws.amazon.com/rekognition/pricing/).

## Deployment

The solution deploys on Amazon Elastic Container Service (Amazon ECS) with AWS Fargate. The Streamlit application and the agent runtime run in Fargate tasks behind an internal Application Load Balancer, and an Amazon CloudFront distribution is the only public entry point. CloudFront reaches the load balancer through a virtual private cloud (VPC) origin, so the load balancer stays in private subnets with no route to an internet gateway and isn’t directly reachable from the internet. CloudFront also terminates viewer TLS using its default *.cloudfront.net certificate, which provides a publicly trusted HTTPS endpoint without a custom domain or an AWS Certificate Manager certificate. Amazon Cognito handles authentication (invitation-only, with mandatory multi-factor authentication (MFA) through a time-based one-time password (TOTP) by default), and uploads and cached output are stored in Amazon S3 under per-user prefixes with a 24-hour lifecycle policy.

A single script (`./deploy/deploy-ecs.sh`

) builds the container image, pushes it to Amazon Elastic Container Registry (Amazon ECR), and deploys the AWS CloudFormation stacks. Deployment typically completes in 15–20 minutes, most of which is CloudFront propagation. Full deployment prerequisites, the `AllowSelfSignup`

parameter and its trade-offs, and step-by-step instructions are in the repository README.

## Development workflow

Kiro is an AI-powered development environment that supports spec-driven software development by turning high-level ideas into structured requirements, designs, and implementation tasks. We used its spec workflow, persistent project context, and agent hooks to move from concept to a deployable sample while building security into each capability as it took shape.

**Specs defined each capability before implementation.** The face-matching spec defined inputs (reference photo plus video), expected behavior (index the face, search, and return timestamps), and edge cases (no face detected, low-confidence matches). The transcription spec covered multi-language detection, speaker diarization, and cache behavior for repeated queries. Kiro generated implementation tasks from each spec and maintained context across the full feature lifecycle. Based on the team’s prior experience building similar integrations, this compressed what they estimated would typically be a multi-week effort into a focused sprint.

**Threat modeling ran alongside the specs, not after them.** As each capability was specified, we modeled how it could be abused and captured the result in a living threat model (see `docs/threat-model.md`

in the companion repository). The model works through concrete kill chains (authentication bypass, network exposure, agent exploitation through prompt injection, over-privileged IAM, and audit evasion) and assigns each threat a disposition. Every Critical and High finding was remediated in the sample. The items that remain open are recorded there with an explicit decision (accepted residual, or a documented production change). The controls described in the next section are outputs of that process rather than an afterthought.

**Security scanning was embedded in the development loop.** Kiro Hooks ran automated static and infrastructure-as-code scans on changes as they landed, using tooling such as the Automated Security Helper (ASH), and the container image repository is created with scan-on-push enabled. Findings came back as tasks in the same workflow that produced the feature, so a misconfiguration surfaced while the code was being written instead of in a separate review at the end. The net effect is a shift-left posture: A single small team held feature velocity and security rigor in one workflow, and secure-by-design was the default path rather than an extra gate.

## Security considerations

Video often contains sensitive business discussions and identifiable people, so a multi-user deployment must control access, isolate each user’s data, and limit the effect of any one user’s actions.

The reference deployment implements four primary controls:

- Invitation-only Amazon Cognito accounts with mandatory MFA.
- Per-user Amazon S3 prefixes enforced by ownership validation at every tool boundary.
- An internal Application Load Balancer exposed only through CloudFront.
- Per-user upload quotas that limit cross-tenant resource exhaustion.

Production deployments should still decide whether to use a custom domain with a stricter viewer TLS policy, attach AWS WAF, expand audit logging and monitoring, and define data-handling requirements for face collections, transcripts, and cross-Region Amazon Bedrock model inference. Work with your legal and privacy teams to define applicable consent, retention, deletion, and residency requirements. For the full control-by-control analysis, accepted residuals, kill chains, and hardening checklist, see `docs/threat-model.md`

and the README’s Security Considerations for Production in the companion repository.

## Current limitations

Videos longer than two to three hours require several minutes for initial transcription, though subsequent queries return near-instantly from cache. Face-matching accuracy depends on the quality of the reference photo. Clear, well-lit images produce the best results, while blurry crops from group photos might yield lower confidence. Transcription accuracy degrades with heavy background noise or overlapping speakers. The agent surfaces this when it detects quality issues. The web interface accepts MP4, MOV, AVI, and MKV files up to 2 GB, a limit set deliberately below the Fargate task’s memory because Streamlit buffers uploads in memory. For larger media, upload directly to Amazon S3 under your user prefix and ask the agent to analyze the object by its URI (BDA accepts video objects up to 10 GB). Concurrent capacity is bounded by task ephemeral storage and the per-user quota (roughly six concurrent users per task at the defaults), and auto scaling adds tasks under CPU load.

## Clean up

If you deployed this solution and no longer need it, remove the provisioned resources to avoid ongoing charges. Teardown spans three CloudFormation stacks that are connected by parameter values rather than cross-stack exports, so CloudFormation does not enforce their dependency order. After emptying the S3 buckets, delete the stacks in this order: (1) `video-analytic-agent-ecs`

(application), (2) `video-analytic-cognito`

(identity), and (3) `video-object-locator-infra`

(storage). The templates also leave behind the Amazon ECR repository and images, and the AWS Key Management Service (AWS KMS) key remains on its pending-deletion schedule.

Amazon Rekognition face collections require separate cleanup. The application creates them at runtime, so CloudFormation doesn’t own them, and they persist independently of the video bucket’s 24-hour S3 lifecycle. Deleting uploaded objects or stacks does not delete indexed faces. List and delete each collection explicitly. The full teardown sequence, including emptying the versioned S3 buckets first, is in the repository README under Teardown / clean up.

## Conclusion

In this post, we showed the architecture and key patterns for building a conversational video intelligence solution using the Strands Agents SDK, Amazon Bedrock, Amazon Rekognition, and Amazon Transcribe. With this agentic architecture, you no longer need to pre-build processing pipelines for each question type. Instead, a single agent reasons about which services to invoke at runtime based on the user’s natural language query. Adding new capabilities requires only a new `@tool`

function and a prompt update, not a new pipeline.

To apply this pattern to your own use case, start by configuring a Strands agent with Bedrock as the model provider and wrapping each relevant AWS service as a tool function with a descriptive docstring. Then define a system prompt that guides reasoning for your domain and deploy on ECS Fargate for access or run locally for prototyping. The full source code, deployment automation, and all tool implementations are available in the [companion GitHub repository](https://github.com/aws-samples/sample-media-analysis-agent).

To learn more about the services used in this solution, visit:

For related reading, see [Introducing Strands Agents, an Open Source AI Agents SDK](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/) on the AWS Machine Learning Blog.
