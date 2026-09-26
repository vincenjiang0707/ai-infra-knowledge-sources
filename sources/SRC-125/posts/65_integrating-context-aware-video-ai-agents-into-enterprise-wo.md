# integrating-context-aware-video-ai-agents-into-enterprise-workflows

source: https://developer.nvidia.com/blog/integrating-context-aware-video-ai-agents-into-enterprise-workflows/

A video analytics [AI agent](https://www.nvidia.com/en-us/ai/) that can perceive, reason, and act based on massive amounts of video footage must be integrated with existing workflows and applications to be useful. These include content management systems, messaging platforms, databases, ticket queue, and escalation paths.

This integration is challenging because video systems, enterprise knowledge bases, and operational tools are usually siloed. Developers need to capture user intent, retrieve the correct organizational context, generate structured reports, and route findings into downstream systems.

In a [previous post](https://developer.nvidia.com/blog/make-sense-of-video-analytics-by-integrating-nvidia-ai-blueprints/), we explained how to enrich video analysis with document knowledge using NVIDIA Blueprints. This post continues with the topic and explains how to unlock the ability to not just analyze video, but to programmatically act on those analyses by introducing NVIDIA NemoClaw. You’ll learn how to:

- Extend VSS for guided, context-aware video analysis
- Orchestrate the VSS and RAG blueprints as a composable service using NVIDIA NemoClaw
- Generate structured reports enriched with organizational and reference knowledge
- Build multistep workflows where video analysis feeds into other business processes
- Deploy and scale this solution across enterprise environments

This approach is the next step in context-aware video AI agents, which involves moving from “What does this video show?” to “What should we do about what this video shows, and how do we coordinate that action at scale?”

## What are NVIDIA NemoClaw and NVIDIA Blueprints?

[NVIDIA NemoClaw](https://www.nvidia.com/en-us/ai/nemoclaw/)** **is a collection of open blueprints for building autonomous agents. It enables the ecosystem to build domain-specialized, always-on agents that are safer, faster, and operate more cost efficiently across digital and physical workflows.

[NVIDIA Blueprints](https://build.nvidia.com/blueprints) are customizable reference workflows for building [agentic AI](https://www.nvidia.com/en-us/glossary/ai-agents/) pipelines at enterprise scale. They combine specialized microservices, optimized models, and composable APIs to accelerate time-to-value while maintaining modularity. In addition to NemoClaw, the main blueprints used in this post are:

[NVIDIA Metropolis Blueprint for Video Search and Summarization (VSS)](https://build.nvidia.com/nvidia/video-search-and-summarization)ingests streaming or archival video, generates captions and visual metadata, and supports semantic search, interactive Q&A, and event summarization.[NVIDIA AI Blueprint for Retrieval-Augmented Generation (RAG)](https://build.nvidia.com/nvidia/build-an-enterprise-rag-pipeline)indexes proprietary enterprise documents—manuals, policies, regulations, SOPs, and reference data—into a GPU-accelerated vector store for fast semantic search.

## How does VSS capture intent, retrieve knowledge, and generate reports from video?

VSS provides guided, context-aware video analysis through a set of tools built into the agent. Human-in-the-loop (HITL) prompts capture what the user wants before any processing begins. The agent retrieves the relevant organizational knowledge and produces a structured, timestamped report.

When combined with [NVIDIA NemoClaw](https://www.nvidia.com/en-us/ai/nemoclaw/) blueprints for building autonomous agents, this system can go beyond simple video analysis to programmatically act on those analyses. This unlocks the ability to generate tickets, compare patterns across multiple sources, draft revised procedures, escalate anomalies, and feed results into downstream workflows.

Three agent tools work together to make this happen:

**Long video summary (LVS)****video understanding tool:**Performs long video summarization with mandatory HITL parameter collection. Users interactively specify the scenario (what the video is about), events of interest (what to detect), objects of focus (what to track), and an optional knowledge-retrieval query.**Knowledge retrieval (frag) tool:**Calls the RAG Blueprint to retrieve organization-specific context from documents, policies, reference data, and knowledge bases. The RAG Blueprint handles embedding, reranking, and vector search internally.**Report generation tool:**Produces a structured report combining the video analysis with the retrieved context, complete with timestamps, narrative analysis, and citations. It can use HITL to let the user confirm or edit the prompt before the report is generated.

Together, these tools collect user intent through HITL, query the RAG Blueprint for contextual knowledge, process the video with that context, and hand off to the report generation tool for formatted output.

## Generating assessments and recommended actions from a video

To demonstrate this process, we will create a “healthy eating coach” that analyzes food videos to assess a user’s eating habits and return concrete, tracked next steps they can act on. The process is detailed in the following sections.

### User uploads a video and specifies what to analyze

To start, a user uploads a meal preparation video through the VSS interface (Figure 1).

NemoClaw then begins the workflow. It reads the vss-generate-video-report-rag skill definition (SKILL.md) to learn which parameters the analysis needs and hands the request to the VSS agent, which walks the user through a short series of HITL prompts in their terminal (Figure 2).

The prompts ask what to analyze, the scenario, the events of interest, the objects to track, and an optional RAG Blueprint query for the reference knowledge to retrieve, such as the nutritional or regulatory guidelines. Capturing this intent up front scopes the analysis to what the user actually cares about before any video is processed. For automated batch runs, these answers can be supplied programmatically instead of interactively.

### NemoClaw orchestrates VSS and the RAG Blueprint

Next, with the parameters confirmed, NemoClaw orchestrates the pipeline. The LVS video understanding tool first queries the RAG Blueprint for the relevant nutritional guidelines, and the RAG Blueprint returns the matching reference documents, handling the vector search internally.

It then passes those parameters, the video, and the retrieved context to the LVS service, which summarizes the video hierarchically and weaves the reference knowledge into its findings. The report generation tool combines the result into a structured, timestamped report that includes detected events with timestamps, a narrative analysis grounded in the reference material, citations to the relevant source documents, and concrete recommended actions.

Figure 3 shows this orchestration in the NemoClaw terminal, including the agent’s reasoning and tool calls.

### NemoClaw creates a Jira ticket

NemoClaw reads the finished report and turns it into coordinated action. It presents the completed analysis with links to the Markdown and PDF reports and the video playback, a summary of why the meal is healthy, and recommended next steps (Figure 4). It then automatically creates a Jira ticket that summarizes the findings and the recommended dietary adjustments, with an appropriate priority and assignment so the action items are tracked to completion (Figure 5).

This downstream step generalizes well beyond Jira. Depending on what the report contains, NemoClaw can also:

- Create tickets for the findings, with the right priority and assignment.
- Escalate or summarize patterns that emerge across multiple runs.
- Bundle supporting evidence for review or compliance.
- Route gaps to the appropriate follow-up workflow.

At this point, the report is no longer a static document. It becomes the trigger for coordinated action across the systems your team already uses.

Figure 6 shows the architecture in four layers:

**Orchestration:**The NemoClaw agent, the vss-generate-video-report-rag skill, and the HITL prompts**VSS agent:**Tools include video I/O, search, understanding, LVS, knowledge retrieval, and report generation. Knowledge retrieval is part of the agent, not a separate extension**RAG Blueprint:**NVIDIA RAG API, Milvus vector database,[NVIDIA Nemotron reranking NIM](https://build.nvidia.com/models?q=rerank), and the indexed reference and organizational documents-
**LLM fusion:**Enrichment of the VSS-provided summary with the context retrieved through the RAG Blueprint

Data flows downward through the system, with the agent’s tools orchestrating calls to the LVS service and the RAG Blueprint, both of which feed into the report generation tool for final output.

## How to deploy the VSS agent with knowledge retrieval

Follow the steps below to implement the solution for your own workflow.

### Prerequisites

- NVIDIA GPU(s) with at least 24 GB VRAM
- Docker Engine plus Docker Compose v2
- NGC API key (
[ngc.nvidia.com](http://ngc.nvidia.com)) - NVIDIA Build API key (
[build.nvidia.com](http://build.nvidia.com)) - RAG Blueprint deployed and reachable from the agent (its server URL accessible), and its collection name
- NemoClaw installed (for programmatic access)

### Step 1: Clone the VSS repo and authenticate with NGC

`git clone ` `cd ~/vss-public` `echo "$NGC_CLI_API_KEY" | docker login nvcr.io --username '$oauthtoken' --password-stdin` |

### Step 2: Configure the environment

Edit the LVS profile .env file, `deploy/docker/developer-profiles/dev-profile-lvs/.env`

. All the variables exist in that file, except the `RAG_ values`

, which the agent’s RAG config reads and you add yourself.

`# Deployment selection` `MODE=2d` `BP_PROFILE=bp_developer_lvs` `HARDWARE_PROFILE=H100 # H100, L40S, RTXPRO4500BW, RTXPRO6000BW, DGX-SPARK, IGX-THOR, AGX-THOR, or OTHER` ` ` `# LLM / VLM placement` `LLM_MODE=local_shared # local_shared runs LLM and VLM on one GPU; use 'local' for separate GPUs` `VLM_MODE=local_shared` `LLM_DEVICE_ID='0'` `VLM_DEVICE_ID='0'` ` ` `# Paths (you MUST set these)` `VSS_APPS_DIR="<PATH>/vss-public/deploy/docker"` `VSS_DATA_DIR="<PATH>/vss-apps-data"` `HOST_IP='<YOUR_IP>'` ` ` `# Agent image + config` `VSS_AGENT_VERSION=3.2.0` `# Enable knowledge retrieval (frag): point at config_rag.yml (default config.yml has it off)` `VSS_AGENT_CONFIG_FILE=./deploy/docker/developer-profiles/dev-profile-lvs/vss-agent/configs/config_rag.yml` ` ` `# Credentials` `NGC_CLI_API_KEY='nvapi-...'` `NVIDIA_API_KEY='nvapi-...'` ` ` `# RAG Blueprint connection (read by config_rag.yml)` `RAG_SERVER_URL='` `RAG_API_KEY='<YOUR_RAG_API_KEY>'` `KNOWLEDGE_COLLECTION='<YOUR_COLLECTION>'` |

Setting `VSS_AGENT_CONFIG_FILE`

to `config_rag.yml`

enables the frag knowledge-retrieval tool. Those three RAG_ values are the only RAG settings the agent needs: it calls the RAG server’s search endpoint, and the RAG Blueprint handles embedding, reranking, and vector search internally. Configure the vector database, embedding, and reranker on the RAG Blueprint deployment itself, following its own documentation.

### Step 3: Deploy the VSS stack

Create the data directories the bind mounts need, then bring up the stack. The compose profile is selected automatically from `COMPOSE_PROFILES`

in the .env file.

`export VSS_DATA_DIR=<PATH>/vss-apps-data` `mkdir -p "$VSS_DATA_DIR"/data_log/{elastic/data,elastic/logs,kafka,redis/data,redis/log}` `chmod -R 777 "$VSS_DATA_DIR/data_log"` ` ` `cd ~/vss-public/deploy/docker` `docker compose \` ` ` `--env-file developer-profiles/dev-profile-lvs/.env \` ` ` `-f compose.yml \` ` ` `up -d` |

The compose stack starts all infrastructure (VST, Redis, Elasticsearch, LVS, NIM) and the agent using the RAG-enabled config. The dev-profile helper, `./deploy/docker/scripts/dev-profile.sh up --profile lvs --hardware-profile H100`

, does the same and creates the data directories for you.

### Step 4: Verify that the services are healthy

Note that the NIM may take 5 to 15 minutes to load.

`docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'` `curl -sS ` `curl -f ` `curl -f ` `curl -f ` |

## NemoClaw setup

NemoClaw acts as the orchestration layer, configuring the sandbox, network policy and skill so it can drive the full workflow.

### Step 1: Run the NemoClaw installer

From the repo root; `NEMOCLAW_PROVIDER`

is required; use `build`

for NVIDIA-hosted models.

`NEMOCLAW_PROVIDER=build \` `NVIDIA_API_KEY="$NVIDIA_API_KEY" \` ` ` `bash deploy/docker/scripts/nemoclaw/init_nemoclaw.sh demo` |

This single command handles the full setup: it onboards NemoClaw, configures the model provider, applies the VSS sandbox policy (which grants the sandbox access to the VSS agent on port 8000), installs the repo skills—including vss-generate-video-report-rag—into the sandbox as an OpenClaw plugin, and prints the OpenClaw UI URL.

To use your own OpenAI-compatible endpoint instead (for example a local vLLM):

`NEMOCLAW_PROVIDER=custom with NEMOCLAW_ENDPOINT_URL and COMPATIBLE_API_KEY` |

### Step 2: Test the end-to-end workflow

`nemoclaw SANDBOX_NAME connect` `openclaw tui` |

The OpenClaw UI is now open. The next two actions happen inside that UI, not in your shell:

- Type /new and press Enter to start a fresh session.
- Type your request as a message and press Enter: I want to generate a video summary report for
`<VIDEO_NAME>`

.

The agent then collects the analysis parameters through the HITL prompts, generates the report with LVS and the RAG Blueprint, and can create a Jira ticket or send notifications based on the results.

## Latency and performance of the end-to-end pipeline

Adding NemoClaw orchestration and HITL parameter collection introduces minimal latency overhead. The HITL phase is asynchronous—NemoClaw and human users interact while the system stands by—so once parameters are confirmed, video processing proceeds.

## How are industries and NVIDIA partners using NemoClaw, VSS 3, and the RAG Blueprint?

The combination of video understanding, knowledge retrieval, and agentic orchestration unlocks new capabilities across industries. Here is how partners are deploying this solution.

**Computacenter**deployed the full DETECT → REASON → ACT pipeline on a Run:AI cluster for predictive maintenance, using VSS 3 to analyze drone, borescope, and thermal inspection footage, RAG Blueprint for OEM context, and NemoClaw to auto-draft Maximo work orders—cutting footage-to-work-order time from 30–45 minutes to roughly 19 seconds across four asset classes.**VAST Data**uses NemoClaw to orchestrate a real-time VSS pipeline on the VAST DataEngine, processing live game streams with VAST RAG over VastDB and vectors; built on the NVIDIA blueprint with cosmos-reason2 and Nemotron, it runs end-to-end on NVIDIA DSX AIR.

## What are the benefits of actionable video AI?

The integration of VSS 3, RAG Blueprint, and NemoClaw represents a fundamental shift in how enterprises can approach video analytics. Video analysis has typically produced static reports. Understanding what happened in a video required manual interpretation and manual action initiation.

With this integrated solution, video understanding is now a starting point. Agentic orchestration translates that understanding into coordinated action—creating tickets, alerting teams, comparing patterns, escalating anomalies, and feeding results into downstream workflows.

The implications are significant:

**Speed:**Response time drops from hours or days to minutes.**Scale:**Analyze thousands of videos across multiple sources and surface enterprise-wide patterns.**Consistency:**Reference knowledge (policies, procedures, regulations, guidelines) is consistently applied.**Accountability:**Every decision is traced back to video evidence and source documents.**Automation:**Routine workflows (alert generation, ticket creation, documentation) run without manual intervention.

This is what enterprise-grade video AI looks like: specialized analysis engines (the VSS and RAG blueprints) composed into general-purpose agentic workflows (NemoClaw) that embed organizational intelligence into every decision.

## Get started with actionable, enterprise-grade video AI

Together, VSS, RAG Blueprint, and NemoClaw illustrate a broader architectural principle: no single model or service is optimal for every problem, but specialized systems composed through clean, well-defined APIs can deliver capabilities that exceed the sum of their parts. This can be done without sacrificing the modularity, scalability, and governance that enterprise deployments demand.

The result reframes what video analytics is for. Rather than terminating in a static report that waits on human interpretation, video understanding becomes the entry point to an orchestrated workflow—one that retrieves the relevant organizational knowledge, grounds every conclusion in evidence, and drives downstream action automatically.

Enterprises can act on video insights as quickly as they can generate them, consistently and at scale. The footage is already being captured. The next opportunity is to turn it into coordinated, accountable action, and the blueprints to do so are now available. Ready to get started? Use the steps presented in this post, swapping in your own video source and reference knowledge, such as inspection footage paired with OEM manuals, retail floor cameras paired with merchandising policies, or live broadcasts paired with a rulebook.

[Clone the VSS repo](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization), deploy the VSS agent with knowledge retrieval (frag) enabled, point the RAG Blueprint at your documents, and connect NemoClaw to the system your team already uses, such as Jira, Slack, a database or a ticket queue. Start with one recurring loop from video to decision to action, pilot it end-to-end, and expand from there.

## Start the discussion at forums.developer.nvidia.com
