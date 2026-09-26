source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/design-docs/architecture-flow
lastmod: 2026-09-23T23:30:39.914Z

# Architecture Flow

This diagram shows the NVIDIA Dynamo disaggregated inference system. Color-coded flows indicate different types of operations.

## 🔵 Main Request Flow (Blue)

The primary user journey through the system:

**Request (S1)**: HTTP client sends API request to Frontend (OpenAI-compatible server on port 8000)**Preprocess (S2)**: Frontend preprocesses the request (applies chat template, tokenizes) and validates it**Route to Prefill (S3)**: PrefillRouter selects a prefill worker using KV-aware routing or load balancing

## 🟢 Prefill Flow (Green)

The prefill processing pipeline:

**Prefill (S4)**: Prefill worker executes the prefill computation on the input tokens and generates KV cache**Return Metadata (S5)**: Prefill worker returns`disaggregated_params`

containing backend-specific transfer metadata

## 🟠 Decode Routing Flow (Orange)

Router orchestration to decode phase:

**Route to Decode (S6)**: PrefillRouter injects prefill result into decode request and routes to decode worker**KV Transfer (S7)**: Decode worker coordinates with prefill worker for direct GPU-to-GPU KV cache transfer via NIXL

## 🟣 Completion Flow (Purple)

The response generation and delivery:

**Decode (S8)**: Decode worker generates tokens using the transferred KV cache**Response (S9)**: Generated tokens stream back through Frontend for post-processing (detokenization) and delivery to Client

## 🔗 Infrastructure Connections (Dotted lines)

Coordination and messaging support:

### Service Discovery

**On Kubernetes**(default): Uses native K8s resources (DynamoWorkerMetadata CRD, EndpointSlices). No etcd required.**On bare metal**: Uses etcd or filesystem for service discovery and endpoint registration.

### Request Plane

**TCP**(default): Direct TCP connections between Frontend and Workers for request/response transport.**HTTP/NATS**: Alternative transports configurable via`DYN_REQUEST_PLANE`

.

### NATS Connections (Optional, for KV routing)

**KV Events**: Cache state events for KV-aware routing (can be disabled with`--no-router-kv-events`

)

### Planning Connections (Gold, dotted)

**Frontend → Planner**: Metrics collection for auto-scaling decisions**Planner → Workers**: Resource scaling commands for workers

## Technical Implementation Details

### PrefillRouter Orchestration:

- The
`PrefillRouter`

sits between the Frontend and workers, orchestrating disaggregated serving - Selects prefill workers using KV-aware routing (cache overlap scores + load) or simple load balancing
- Injects transfer metadata into decode requests for KV cache coordination

### NIXL (NVIDIA Interchange Library):

- Enables high-speed GPU-to-GPU data transfers using NVLink, InfiniBand/UCX, or PCIe
- Transfer metadata exchanged via
`disaggregated_params`

in prefill response - Backend-specific coordination: SGLang uses bootstrap connections, TRTLLM uses opaque state, vLLM uses block IDs

### Disaggregated KV Cache:

- Each worker maintains local KV cache in its GPU memory
- No shared storage bottlenecks—transfers are direct worker-to-worker via NIXL
- Non-blocking transfers allow GPU forward passes to continue during KV transfer