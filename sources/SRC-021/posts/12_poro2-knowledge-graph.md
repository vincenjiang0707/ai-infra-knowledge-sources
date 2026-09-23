# poro2-knowledge-graph

source: https://rocm.blogs.amd.com/artificial-intelligence/poro2-knowledge-graph/README.html

# Knowledge Graph Integration With Poro2 For Enriching Medical Text Processing[#](https://rocm.blogs.amd.com#knowledge-graph-integration-with-poro2-for-enriching-medical-text-processing)

Medical documentation contains specialized terminology, such as terms like “hepatomegalia” or “bilateraalinen pleuraeffuusio”, that healthcare professionals understand but patients struggle to comprehend. Making these documents accessible to patients improves healthcare outcomes, yet general-purpose LLMs often lack the specialized vocabulary needed for accurate simplifications.

In this post, we demonstrate a two-stage agentic architecture that addresses this challenge. Using Model Context Protocol (MCP) tools to query a medical knowledge graph and a hand-curated terminology dictionary, [GLM-4.7-Flash](https://arxiv.org/abs/2508.06471), a 30B model selected for its strong tool-calling capabilities, enriches medical terminology. Then [Poro2](https://huggingface.co/LumiOpen/Llama-Poro-2-70B-Instruct), a 70-billion-parameter model with exceptional Finnish language capabilities, uses the enriched context from the previous step to generate patient-friendly Finnish translations that preserve clinical accuracy. To get you rolling on deploying this on AMD, we provide Kubernetes deployment manifests and a ready-to-use pipeline developed for MI300X GPUs.

This work was developed in collaboration with [Lingsoft](https://lingsoft.ai/), a Finnish language technology company. Their expertise in Finnish medical terminology and clinical language guided the design of the terminology dictionary and the evaluation methodology.

Note

Throughout this post, we use the word “translate” to describe converting medical terminology into patient-friendly language (both remain in Finnish). This is text simplification rather than language translation (e.g., Finnish to English). However, healthcare professionals often describe this paraphrasing as “translating medical jargon into lay-term language”, reflecting how specialized medical terminology can feel like a foreign language to patients.

In this post, you’ll learn how to:

Deploy Poro2 and a tool-calling LLM on AMD Instinct MI300X GPUs using vLLM

Set up MCP servers providing medical terminology tools

Configure a two-stage inference pipeline for tool-augmented translation

Compare results with and without knowledge graph enrichment, including a quantitative evaluation showing improved accuracy and fluency


All the code for this post, including the pipeline script, the MCP server, and the Kubernetes deployment manifests, is available in the [GitHub folder](https://github.com/ROCm/rocm-blogs/tree/release/blogs/artificial-intelligence/poro2-knowledge-graph/src).

## Why Agentic AI?[#](https://rocm.blogs.amd.com#why-agentic-ai)

Patient comprehension of medical information directly impacts healthcare outcomes. When patients understand their diagnoses, treatment plans, and test results, they make better decisions about their care. However, medical documents are written for healthcare professionals, not patients.

This is where agentic AI patterns become valuable. Rather than relying solely on the model’s pre-trained knowledge, we can connect it to external knowledge sources at inference time. The Model Context Protocol (MCP) provides a standardized way to do this. MCP enables LLMs to call external tools, query databases, and access structured knowledge during the generation process.

This approach differs from Retrieval-Augmented Generation (RAG), which retrieves document chunks based on similarity to the input. With MCP tools, the model actively decides when to query external sources and what specific terms to look up. Rather than receiving a batch of potentially relevant text, the model makes targeted requests for precise information, such as looking up a specific medical term’s definition, resulting in more focused and accurate context enrichment.

Moreover, the entire agentic pipeline, both LLMs and the knowledge graph, can be deployed on-premises, so no patient data needs to leave the institution.

## Architecture Overview[#](https://rocm.blogs.amd.com#architecture-overview)

The system uses a two-stage architecture that separates tool-based knowledge extraction from Finnish language generation:

**Flow:**

The client sends a medical report to GLM-4.7-Flash (Stage 1)

GLM-4.7-Flash analyzes the text and calls MCP tools to look up medical terminology

Tool results provide term definitions and enriched context

The enriched context is passed to Stage 2 along with the original report

Poro2 generates the final patient-friendly translation.


This two-stage architecture provides several benefits:

**Separation of concerns**- Medical knowledge is maintained separately from the model**Updateability**- Knowledge sources can be updated without retraining**Auditability**- Tool calls provide transparency into the translation process. Every tool call is logged in the output JSONL (see[Data Formats](https://rocm.blogs.amd.com#data-formats)), so reviewers can trace exactly which terms were looked up and what the knowledge graph returned**Modularity**- Different knowledge sources can be swapped as needed

### Stage 1: Knowledge Graph-Driven Term Resolution[#](https://rocm.blogs.amd.com#stage-1-knowledge-graph-driven-term-resolution)

In our implementation, Stage 1 uses [GLM-4.7-Flash](https://arxiv.org/abs/2508.06471), a 30B model selected for its strong function-calling capabilities. It employs a three-tier strategy to resolve medical terminology, with the MeSH knowledge graph at its core. Rather than relying on parametric knowledge, the model grounds term translations in verified, structured sources:

**Hand-curated dictionary**: A curated dictionary of domain-specific term pairs is embedded in the system prompt as the first-priority lookup. These cover the most common and critical terms in the target medical domain (e.g., upper-abdomen medical terminology). While the dictionary provides the highest-quality mappings, maintaining hand-picked lists becomes increasingly difficult as the system scales to new specialties or as medical terminology evolves.**MeSH Knowledge Graph**: For terms not covered by the dictionary, the model autonomously issues MCP tool calls to a Dockerized[FinMeSH](https://finto.fi/mesh/en/)knowledge graph. FinMeSH is the Finnish extension of the Medical Subject Headings (MeSH) vocabulary maintained by the U.S. National Library of Medicine. The knowledge graph exposes two tools:`full_text_search`

for term lookup and`sparql_query`

for exploring relationships between medical concepts. This tier becomes especially valuable in long-term deployments: as hand-curated lists inevitably grow stale or encounter unfamiliar terms, the knowledge graph provides a broad, actively maintained terminology base that the model can query on demand, without requiring manual updates to the dictionary.**Rule-based fallback**: When MCP tool calls return empty results, a rule-based fallback scans the text against the MeSH index using Finnish morphology-aware suffix stripping (`-ssa`

,`-llä`

,`-sta`

) and Latin pattern recognition (`-itis`

,`-oma`

,`-osis`

).

The Stage 1 output is a structured JSON containing key terms, abbreviation expansions, and patient-friendly Finnish translations. The model is explicitly instructed not to invent translations for terms absent from both the dictionary and the knowledge graph, reducing the risk of hallucination.

## Results: With and Without Terminology Help[#](https://rocm.blogs.amd.com#results-with-and-without-terminology-help)

To illustrate the value of MCP tool integration, consider a sample medical sentence:

**Original (Finnish medical terminology):**

“Maksassa todetaan lievä hepatomegalia ilman fokaalisia muutoksia.”


(EN: “Mild hepatomegaly is observed in the liver without focal changes.”)

**Translation WITHOUT terminology help:**

“Maksassa havaitaan lievä hepatomegalia.”


(EN: “Mild hepatomegaly is observed in the liver.”)

The model preserves the medical term “hepatomegalia” without explanation, assuming the reader understands it. Furthermore, important context is lost at the end of the sentence.

**Translation WITH terminology help (using knowledge graph lookup):**

“Maksa on hieman suurentunut (hepatomegalia), mutta siinä ei näy paikallisia poikkeavuuksia.”


(EN: “The liver is slightly enlarged (hepatomegaly), but no local abnormalities are seen.”)

With access to the knowledge graph of medical terminology, the model:

Looked up “hepatomegalia” and found it means “liver enlargement”

Incorporated the plain-language explanation while preserving the medical term

Translated “fokaalisia muutoksia” (focal changes) to “paikallisia poikkeavuuksia” (local abnormalities)


The enriched translation also keeps the closing clause that the version without terminology help dropped, so the reader still learns that no local abnormalities were found.

This example demonstrates how tool access enables more informative translations without sacrificing accuracy: jargon is glossed and context survives.

### Evaluation on Finnish Medical Example Findings[#](https://rocm.blogs.amd.com#evaluation-on-finnish-medical-example-findings)

We evaluated the system on 117 pseudonymized Finnish-language upper-abdomen medical findings extracted from 6 radiology reports focused on pancreatic cysts, produced in collaboration with radiologists from [Tampere University Hospital](https://www.tays.fi/en-US) and [Lingsoft](https://lingsoft.ai/). The findings contain dense terminology mixing Finnish, Latin, and abbreviations.

Here is a more complex example where Stage 1 extracts five medical-to-layperson mappings using `full_text_search`

and `sparql_query`

tools:

**Original (Finnish):**

“

Haimaparenkyymissäei ole merkittävääatrofiaa, muttadiffuusia rasvainfiltraatiotajaTT-tutkimuksessa on ollutparenkyymikalkkeja.”

(EN: “In thepancreatic parenchymathere is no significantatrophy, butdiffuse fat infiltrationand onCTthere have beenparenchymal calcifications.”)

**Patient-friendly output:**

“

Haimakudoksessaei ole merkittävääkutistumista, mutta onlevinnyttä rasvan kertymistäjatietokonetomografiassaon havaittukudoksen sisäisiä kalkkeutumia.”

(EN: “In thepancreatic tissuethere is no significantshrinkage, butwidespread fat accumulationand oncomputed tomographythere have been observedcalcifications within the tissue.”)

In this example, five terms were successfully mapped: *haimaparenkyymi* → *haimakudos* (pancreatic tissue), *atrofia* → *kutistuminen* (shrinkage), *diffuusi rasvainfiltraatio* → *levinnyt rasvan kertyminen* (widespread fat accumulation), *TT-tutkimus* → *tietokonetomografia* (computed tomography), and *parenkyymikalkit* → *kudoksen sisäiset kalkkeutumat* (calcifications within the tissue).

### Quantitative Comparison[#](https://rocm.blogs.amd.com#quantitative-comparison)

We compared the system against a previous version developed by Lingsoft that also employed an agentic architecture with LLMs and medical terminologies, but did not use Poro2, MCP, or knowledge graphs. A human reviewer rated each system’s output across the 117 findings:

Criterion |
Previous system wins |
New system wins |
Tie |
Improvement |
|---|---|---|---|---|
Medical accuracy |
10 |
28 |
72 |
22.0% |
Layperson fluency |
7 |
58 |
52 |
86.4% |

The new system shows a modest improvement in medical accuracy and a substantial improvement in layperson fluency. The large gain in fluency reflects Poro2’s strong Finnish language capabilities, while the accuracy improvements come from the combined effect of the hand-curated dictionary, the MeSH knowledge grounding, and Poro2’s ability to incorporate verified terminology into natural Finnish.

## Deployment Guide[#](https://rocm.blogs.amd.com#deployment-guide)

This section covers the hardware, software, and configuration needed to deploy the two-stage pipeline.

### Hardware Requirements[#](https://rocm.blogs.amd.com#hardware-requirements)

Running Poro2 (70B parameters) requires substantial GPU resources. For this deployment, we use:

Component |
Specification |
|---|---|
GPU |
2x AMD Instinct MI300X |
GPU Memory |
384GB HBM3 (192GB per GPU) |
Shared Memory |
32GB (for tensor parallel communication) |
Storage |
256GB ephemeral storage |

The 70B model requires tensor parallelism across two GPUs. The MI300X’s 192GB HBM3 memory provides sufficient capacity for the model weights, KV cache, and intermediate activations.

Both stages use this same two-GPU profile, each deployed as a separate vLLM service in the [Kubernetes Deployment](https://rocm.blogs.amd.com#kubernetes-deployment) section below.

### Software Stack[#](https://rocm.blogs.amd.com#software-stack)

The deployment uses the following components:

**Inference Server:**

`rocm/vllm:latest`

- vLLM with ROCm support for AMD GPUsOpenAI-compatible API endpoint


**MCP Integration:**

`pydantic-ai`

- Agent framework for LLM tool calling`mcp`

- Model Context Protocol client library`fastmcp`

- MCP server framework

**Additional Dependencies:**

`httpx`

- Async HTTP client

Install the Python dependencies:

```
pip install -r requirements.txt
```

### Kubernetes Deployment[#](https://rocm.blogs.amd.com#kubernetes-deployment)

For production deployments on Kubernetes, we recommend following the patterns described in [AI Inference Orchestration with Kubernetes on Instinct MI300X](https://rocm.blogs.amd.com/artificial-intelligence/k8s-orchestration-part1/README.html). That series covers cluster setup, GPU operator configuration, and vLLM deployment in detail.

The pipeline runs two vLLM services: Stage 1 serves GLM-4.7-Flash for tool calling, and Stage 2 serves Poro2 for Finnish generation. Each stage is deployed independently.

**Stage 1: GLM-4.7-Flash (tool calling).** The Stage 1 manifest ([ k8s/deployment-glm-4.7-flash-vllm.yaml](https://github.com/ROCm/rocm-blogs/tree/release/blogs/artificial-intelligence/poro2-knowledge-graph/src/k8s/deployment-glm-4.7-flash-vllm.yaml)) turns on vLLM’s tool-calling support:

```
# Copyright © Advanced Micro Devices, Inc., or its affiliates.
#
# SPDX-License-Identifier: MIT
apiVersion: apps/v1
kind: Deployment
metadata:
name: glm-4-7-flash-vllm-deployment
spec:
replicas: 1
template:
spec:
containers:
- name: vllm-server
image: rocm/vllm-dev:nightly
command:
- "/bin/bash"
- "-c"
- |
pip install git+https://github.com/huggingface/transformers.git && \
python -m vllm.entrypoints.openai.api_server \
--model zai-org/GLM-4.7-Flash \
--host 0.0.0.0 \
--port 8042 \
--tensor-parallel-size 2 \
--enable-auto-tool-choice \
--tool-call-parser glm47 \
--reasoning-parser glm45 \
--max-model-len 200000 \
--gpu-memory-utilization 0.90
ports:
- containerPort: 8042
name: http
resources:
requests:
amd.com/gpu: 2
limits:
amd.com/gpu: 2
volumeMounts:
- mountPath: /dev/shm
name: shm
volumes:
- emptyDir:
medium: Memory
sizeLimit: 16Gi
name: shm
```

The highlighted lines are what make Stage 1 work: `--enable-auto-tool-choice`

, `--tool-call-parser glm47`

, and `--reasoning-parser glm45`

enable GLM-4.7-Flash’s function calling and reasoning output, and the model needs a recent `transformers`

build, installed at container start. Deploy it with:

```
kubectl apply -f k8s/deployment-glm-4.7-flash-vllm.yaml
```

**Stage 2: Poro2 (Finnish generation).** The Stage 2 manifest ([ k8s/deployment-poro2-vllm.yaml](https://github.com/ROCm/rocm-blogs/tree/release/blogs/artificial-intelligence/poro2-knowledge-graph/src/k8s/deployment-poro2-vllm.yaml)) highlights the key configuration:

```
# Copyright © Advanced Micro Devices, Inc., or its affiliates.
#
# SPDX-License-Identifier: MIT
apiVersion: apps/v1
kind: Deployment
metadata:
name: poro2-vllm-deployment
spec:
replicas: 1
template:
spec:
containers:
- name: vllm-server
image: rocm/vllm:latest
command:
- "python"
- "-m"
- "vllm.entrypoints.openai.api_server"
- "--model"
- "LumiOpen/Llama-Poro-2-70B-Instruct"
- "--tensor-parallel-size"
- "2"
- "--max-model-len"
- "8192"
- "--gpu-memory-utilization"
- "0.9"
resources:
requests:
amd.com/gpu: 2
limits:
amd.com/gpu: 2
volumeMounts:
- mountPath: /dev/shm
name: shm
volumes:
- emptyDir:
medium: Memory
sizeLimit: 32Gi
name: shm
```

Key configuration points:

**tensor-parallel-size: 2**- Distributes the model across both GPUs**gpu-memory-utilization: 0.9**- Uses 90% of available GPU memory**shared memory volume**- Required for tensor parallel communication between GPUs**max-model-len: 8192**- Matches Poro2’s context window, accommodating system prompts with terminology dictionaries and tool definitions

Deploy the Poro2 model for Stage 2 inference with:

```
kubectl apply -f k8s/deployment-poro2-vllm.yaml
```

For enterprise deployments, see the [AMD Enterprise AI Suite](https://rocm.blogs.amd.com/artificial-intelligence/enterprise-ai-suite/README.html) documentation for production-ready infrastructure patterns.

## Setting Up the MCP Server[#](https://rocm.blogs.amd.com#setting-up-the-mcp-server)

MCP servers provide tools that the Stage 1 LLM can call during the context enrichment phase. We configure a knowledge graph for medical terminology lookup.

### RDF Knowledge Graph Explorer[#](https://rocm.blogs.amd.com#rdf-knowledge-graph-explorer)

The RDF Knowledge Graph Explorer ([mcp-rdf-explorer](https://github.com/emekaokoye/mcp-rdf-explorer)) is a Dockerized service that provides access to [FinMeSH](https://finto.fi/mesh/en/), the Finnish extension of the Medical Subject Headings (MeSH) vocabulary. FinMeSH provides structured, verified medical terminology in Finnish, making it an ideal knowledge source for grounding medical term translations.

The MCP server exposes two tools:

: Searches the MeSH index for medical terms and returns their Finnish definitions, synonyms, and broader/narrower concepts`full_text_search`

: Executes SPARQL queries against the RDF/SKOS (Resource Description Framework / Simple Knowledge Organization System) graph to explore hierarchical term structures and navigate related concepts`sparql_query`


When the Stage 1 model encounters specialized terminology, it autonomously decides which tool to use: simple lookups use `full_text_search`

, while exploring term relationships uses `sparql_query`

.

### MCP Configuration[#](https://rocm.blogs.amd.com#mcp-configuration)

The [ mcp_config.json](https://github.com/ROCm/rocm-blogs/tree/release/blogs/artificial-intelligence/poro2-knowledge-graph/src/mcp/rdf-explorer/mcp_config.json) file specifies which MCP servers to connect:

```
{
"mcpServers": {
"rdf_knowledge_graph": {
"command": "docker",
"args": ["run", "-i", "--rm", "mcp-rdf-explorer:latest"],
"description": "RDF Knowledge Graph for structured medical data queries"
}
}
}
```

The server runs as a subprocess and communicates via stdio using the MCP protocol. The RDF Knowledge Graph enables rich queries when the Stage 1 model needs to look up medical terminology or understand relationships between medical concepts.

The `mcp-rdf-explorer:latest`

image referenced above is built from the [Dockerfile](https://github.com/ROCm/rocm-blogs/tree/release/blogs/artificial-intelligence/poro2-knowledge-graph/src/mcp/rdf-explorer/Dockerfile) we provide, which clones [mcp-rdf-explorer](https://github.com/emekaokoye/mcp-rdf-explorer) and bundles the FinMeSH data so the server runs without extra setup.

## Running the Two-Stage Pipeline[#](https://rocm.blogs.amd.com#running-the-two-stage-pipeline)

### Basic Usage[#](https://rocm.blogs.amd.com#basic-usage)

With both deployments running (see [Kubernetes Deployment](https://rocm.blogs.amd.com#kubernetes-deployment)), forward each vLLM service to a local port:

```
kubectl port-forward deployment/glm-4-7-flash-vllm-deployment 8042:8042 &
kubectl port-forward deployment/poro2-vllm-deployment 8000:8000 &
```

Then run the workflow ([ medical_reports_agentic_workflow.py](https://github.com/ROCm/rocm-blogs/tree/release/blogs/artificial-intelligence/poro2-knowledge-graph/src/medical_reports_agentic_workflow.py)):

```
python medical_reports_agentic_workflow.py \
--input medical_reports.json \
--output results.jsonl
```

### Data Formats[#](https://rocm.blogs.amd.com#data-formats)

The client accepts JSON input and produces JSONL output (one record per line) with tool call information:

```
[
{
"case": "0",
"text": "Maksassa todetaan hepatomegalia..."
}
]
```

```
{
"case": "0",
"text": "Maksassa todetaan hepatomegalia...",
"completion": "Maksa on suurentunut...",
"tool_calls": [
{
"tool_name": "lookup_term",
"args": {"term": "hepatomegalia"}
}
],
"status": "ok"
}
```

The `tool_calls`

array in each output record shows which tools the Stage 1 model invoked, providing transparency into the context enrichment process.

### Performance Considerations[#](https://rocm.blogs.amd.com#performance-considerations)

MCP tools increase the latency of the inference pipeline because each tool call requires:

Generating the actual tool call (model inference)

Executing the tool (typically fast for local lookups)

Incorporating results and generating final response (model inference)


In practice, medical text translation tasks like this are typically not latency-critical. After a medical report is written by a healthcare professional, the patient-friendly version does not need to be available immediately. The natural delay in clinical workflows means reports can be processed in batches, and the additional round-trips for tool calls have minimal impact. The focus is on translation quality rather than speed.

That said, the AMD MI300X’s high memory bandwidth (5.3 TB/s) keeps inference passes fast. For batch processing, concurrent request handling in the client (`--concurrency 10`

) maintains good throughput despite the multi-turn nature of tool-augmented generation.

## Next Steps and Variations[#](https://rocm.blogs.amd.com#next-steps-and-variations)

### Scaling Considerations[#](https://rocm.blogs.amd.com#scaling-considerations)

For production workloads:

Deploy multiple vLLM replicas behind a load balancer (see

[K8s Orchestration Part 2](https://rocm.blogs.amd.com/artificial-intelligence/k8s-orchestration-part2/README.html)for MetalLB setup and scaling)Use persistent storage for model weights (see

[K8s Orchestration Part 1](https://rocm.blogs.amd.com/artificial-intelligence/k8s-orchestration-part1/README.html))Add Prometheus/Grafana monitoring (see

[K8s Orchestration Part 3](https://rocm.blogs.amd.com/artificial-intelligence/k8s-orchestration-part3/README.html))

### Alternative Knowledge Sources[#](https://rocm.blogs.amd.com#alternative-knowledge-sources)

The MCP architecture supports various knowledge backends beyond the RDF Knowledge Graph shown here:

**Medical term dictionaries**- Simple keyword-based lookups for terminology definitions**Vector databases**- Similarity search over medical literature**REST APIs**- Connect to external terminology services**Custom knowledge bases**- Domain-specific data sources for specialized fields

### Known Limitations[#](https://rocm.blogs.amd.com#known-limitations)

Our evaluation revealed several limitations worth noting:

**Instruction adherence**: The Stage 1 model does not always follow the instruction to avoid inventing translations. When MCP tool calls return empty results, the model sometimes generates plausible-sounding but unverified mappings from its parametric knowledge.**Knowledge graph coverage**: MeSH coverage of Finnish radiology terminology is limited, causing frequent fallback to parametric generation. While the current coverage is sufficient to illustrate the advantages of integrating knowledge graphs with agentic systems, expanding the terminology base would further improve the system’s accuracy.**Fluency trade-offs**: While individual term mappings are correct, the overall sentence fluency can sometimes suffer when multiple terms are replaced simultaneously.

These findings underscore that professional human review remains essential for clinical deployment. The tool call logs provide transparency that makes such review efficient: reviewers can quickly verify which terms were looked up and what sources were used.

## Summary[#](https://rocm.blogs.amd.com#summary)

This post demonstrated a two-stage approach to medical text processing on AMD Instinct MI300X GPUs. The key components are:

**GLM-4.7-Flash**- A 30B model with strong tool-calling capabilities for context enrichment**Poro2**- A 70B model with exceptional Finnish language capabilities for final translation**MCP**- Standard protocol for connecting LLMs to external knowledge sources**vLLM**- High-performance inference server with ROCm support**AMD Instinct MI300X**- GPU infrastructure with 192GB HBM3 memory per GPU

By separating tool-based knowledge extraction from Finnish language generation, we leverage Poro2’s linguistic strengths while enriching the context with structured medical terminology. This results in more accurate and more readable patient-friendly translations. This pattern extends beyond medical text to any domain where combining specialized knowledge with language expertise enhances LLM outputs. We expect this domain-agnostic architecture to transfer to other safety-critical, terminology-dense domains.

Two design choices equip this architecture for clinical work. First, safety is built into the pipeline: medical terms are looked up in structured sources (the curated dictionary, the MeSH knowledge graph, or the rule-based fallback), and unconstrained generation is the last resort. Second, both models and the knowledge graph run on-premises, so sensitive hospital records stay inside the institution, as patient data protection regulations require.

This work was partially funded by Business Finland through the Medallion project, with funding awarded to AMD Silo AI and Lingsoft Group. The system was developed in collaboration with Tampere University Hospital and Lingsoft.

For organizations deploying AI at scale, AMD provides comprehensive infrastructure through the [AMD Enterprise AI Suite](https://rocm.blogs.amd.com/artificial-intelligence/enterprise-ai-suite/README.html), including production-ready inference services and orchestration tools.

## Additional Resources[#](https://rocm.blogs.amd.com#additional-resources)

### AMD Resources[#](https://rocm.blogs.amd.com#amd-resources)

[AI Inference Orchestration with Kubernetes on Instinct MI300X, Part 1](https://rocm.blogs.amd.com/artificial-intelligence/k8s-orchestration-part1/README.html)- Kubernetes cluster setup[AI Inference Orchestration with Kubernetes on Instinct MI300X, Part 2](https://rocm.blogs.amd.com/artificial-intelligence/k8s-orchestration-part2/README.html)- vLLM deployment and scaling[AI Inference Orchestration with Kubernetes on Instinct MI300X, Part 3](https://rocm.blogs.amd.com/artificial-intelligence/k8s-orchestration-part3/README.html)- Monitoring and visualization[AMD Enterprise AI Suite: Open Infrastructure for Production AI](https://rocm.blogs.amd.com/artificial-intelligence/enterprise-ai-suite/README.html)- Enterprise deployment patterns[Inferencing and Serving with vLLM on AMD GPUs](https://rocm.blogs.amd.com/artificial-intelligence/vllm/README.html)- vLLM fundamentals

### External Resources[#](https://rocm.blogs.amd.com#external-resources)

[LumiOpen/Llama-Poro-2-70B-Instruct](https://huggingface.co/LumiOpen/Llama-Poro-2-70B-Instruct)- Model on Hugging Face[Model Context Protocol Specification](https://modelcontextprotocol.io/)- MCP documentation[pydantic-ai](https://github.com/pydantic/pydantic-ai)- Agent framework[FastMCP](https://github.com/jlowin/fastmcp)- MCP server framework[vLLM Project](https://github.com/vllm-project/vllm)- Inference engine[mcp-rdf-explorer](https://github.com/emekaokoye/mcp-rdf-explorer)- MCP server for RDF/SKOS knowledge graphs[FinMeSH (Finto)](https://finto.fi/mesh/en/)- Finnish extension of Medical Subject Headings[GLM-4.5 (ARC) Foundation Models](https://arxiv.org/abs/2508.06471)- Agentic, reasoning, and coding models

## Disclaimers[#](https://rocm.blogs.amd.com#disclaimers)

Performance results are specific to the test system configuration. Your results may vary based on hardware, software versions, and workload characteristics. Medical AI applications require proper clinical validation before deployment in healthcare settings. This demonstration is for educational purposes and is not a substitute for professional medical advice, diagnosis, or treatment. The example translations shown are illustrative and may not reflect actual clinical translation requirements.

Third-party content is licensed to you directly by the third party that owns the content and is not licensed to you by AMD. ALL LINKED THIRD-PARTY CONTENT IS PROVIDED “AS IS” WITHOUT A WARRANTY OF ANY KIND. USE OF SUCH THIRD-PARTY CONTENT IS DONE AT YOUR SOLE DISCRETION AND UNDER NO CIRCUMSTANCES WILL AMD BE LIABLE TO YOU FOR ANY THIRD-PARTY CONTENT. YOU ASSUME ALL RISK AND ARE SOLELY RESPONSIBLE FOR ANY DAMAGES THAT MAY ARISE FROM YOUR USE OF THIRD-PARTY CONTENT.

AMD, the AMD Arrow logo, Instinct, ROCm, and combinations thereof are trademarks of Advanced Micro Devices, Inc. Docker and the Docker logo are trademarks or registered trademarks of Docker, Inc. Hugging Face is a registered trademark of Hugging Face, Inc. Kubernetes is a registered trademark of The Linux Foundation. Python is a trademark of the Python Software Foundation. Other product names used in this publication are for identification purposes only and may be trademarks of their respective owners.
