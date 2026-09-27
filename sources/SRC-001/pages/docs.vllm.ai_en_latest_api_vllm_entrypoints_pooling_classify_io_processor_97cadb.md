source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/pooling/classify/io_processor/
lastmod: 2026-09-27

Skip to content
vLLM
io_processor
Initializing search
GitHub
Home
User Guide
Developer Guide
Benchmarking
API Reference
CLI Reference
Community
vLLM
GitHub
Home
User Guide
User Guide
Getting Started
Getting Started
Quickstart
Installation
Installation
GPU
CPU
TPU
Examples
Examples
Applications
Applications
API Server
Chatbot
Rag
Basic
Basic
Offline Inference
Online Serving
Deployment
Deployment
Async LLM Streaming
Helm Charts
LLM Engine Example
Sagemaker-Entrypoint
Disaggregated
Disaggregated
Disaggregated Encoder
Disaggregated Serving
Ec Both Encoder
Disaggregated Prefill V1
Flexkv Connector
KV Load Failure Recovery Test
LMCache Examples
Mooncake Connector
Features
Features
Automatic Prefix Caching
Batch Invariance
Context Extension
Data Parallel
Kv Events
Logging Configuration
Custom Logits Processors
LoRA
Offline Inference with the OpenAI Batch file format
Pause Resume
Profiling
Prompt Embed
Reset Kv
Sharded State
Speculative Decoding
Structured reads on DiffusionGemma
Structured Outputs
Tensorize vLLM Model
Torchrun
Generate
Generate
Batched Chat Completions Online
Multimodal
Qwen 1M Offline
Trace Replay Offline
Observability
Observability
Monitoring Dashboards
Metrics
Setup OpenTelemetry POC
Prometheus and Grafana
Pooling
Pooling
Classify
Embed
Plugin
Reward
Score
Token Classify
Token Embed
Ray Serving
Ray Serving
Batch LLM Inference
Elastic Ep
Multi-Node-Serving
Ray Serve Deepseek
Run Cluster
Reasoning
Reasoning
OpenAI Chat Completion Tool Calls With Reasoning
OpenAI Chat Completion With Reasoning
OpenAI Chat Completion With Reasoning Streaming
OpenAI Responses Client
RL
RL
Rdt vLLM Serve
Rdt Weight Source
RLHF Async New APIs
RLHF Http IPC
RLHF Http NCCL
RLHF IPC Fsdp Ep
RLHF M2N
RLHF NCCL Fsdp Ep
RLHF Sharded Rdt Small Ep
RLHF Sparse NCCL
Routed Experts E2E
Skip Loading Weights In Engine Init
Scale Out
Scale Out
Init
Example Mm Serve
Token Generation Client
Speech To Text
Speech To Text
OpenAI
Realtime
Tool Calling
Tool Calling
Chat With Tools Offline
OpenAI Chat Completion Client With Tools
OpenAI Chat Completion Client With Tools Required
OpenAI Chat Completion Client With Tools Xlam
OpenAI Chat Completion Client With Tools Xlam Streaming
OpenAI Responses Client With Mcp Tools
OpenAI Responses Client With Tools
General
General
vLLM V1
Frequently Asked Questions
Production Metrics
Reproducibility
Security
Troubleshooting
Usage Stats Collection
Inference and Serving
Inference and Serving
Offline Inference
Online Serving
Online Serving
Derenderer APIs
Generative Scoring
OpenAI-Compatible Server
Renderer APIs
Speech to Text APIs
Trace Replay
Context Parallel Deployment
Data Parallel Deployment
Troubleshooting distributed deployments
Expert Parallel Deployment
Parallelism and Scaling
Integrations
Integrations
Claude Code
Codex
LangChain
LlamaIndex
Deployment
Deployment
Using Docker
Using Kubernetes
Using Nginx
Frameworks
Frameworks
Anyscale
AnythingLLM
AutoGen
BentoML
Cerebrium
Chatbox
Crusoe
Dify
dstack
Haystack
Helm
Hugging Face Inference Endpoints
LiteLLM
Lobe Chat
LWS
Modal
Nebius Serverless AI
Open WebUI
Retrieval-Augmented Generation
RunPod
SkyPilot
Streamlit
NVIDIA Triton
Integrations
Integrations
AIBrix
NVIDIA Dynamo
KAITO
KServe
Kthena
KubeAI
KubeRay
Llama Stack
llm-d
llmaz
Production stack
Training
Training
Async Reinforcement Learning
What is Layerwise (Re)loading?
Reinforcement Learning from Human Feedback
Sampling Mask (Distribution Replay)
Transformers Reinforcement Learning
Weight Transfer
Weight Transfer
Base Classes and Custom Engines
IPC Engine
NCCL M2N Engine
NCCL Engine
Sharded RDT Engine
Configuration
Configuration
Conserving Memory
Engine Arguments
Environment Variables
Model Resolution
Optimization and Tuning
Server Arguments
TPU
Models
Models
Supported Models
Generative Models
Pooling Models
Pooling Models
Classification Usages
Embedding Usages
Reward Usages
Scoring Usages
Specific Model Examples
Token Classification Usages
Token Embedding Usages
Extensions
Extensions
Loading model weights with fastsafetensors
Loading Model Weights with InstantTensor
Loading models with Run:ai Model Streamer
Loading models with CoreWeave's Tensorizer
Hardware Supported Models
Hardware Supported Models
CPU - Intel® Xeon®
XPU - Intel® GPUs
TPU
Features
Features
Automatic Prefix Caching
Batch Invariance
Context Extension
Cross-Encoder Output Reuse
Custom Arguments
Custom Logits Processors
Disaggregated Encoder
Disaggregated Prefilling (experimental)
CPU EC Connector Usage Guide
Engram: conditional memory via n-gram lookups
IndexCache
Initialized engine snapshots
Interleaved Thinking
KV Offloading Usage Guide
LoRA Adapters
MooncakeConnector Usage Guide
MooncakeStoreConnector Usage Guide
MoRIIOConnector Usage Guide
Multimodal Inputs
NixlConnector Compatibility Matrix
NixlConnector Usage Guide
Per-Request Metrics
Preload
Prompt Embedding Inputs
Reasoning Outputs
Sleep Mode
Structured Outputs
Tool Calling
Text watermarking
Quantization
Quantization
AutoAWQ
b12x Linear and MoE Backends
BitsAndBytes
FP8 ViT Encoder Attention
GGUF
GPTQModel
Intel Quantization Support
NVIDIA Model Optimizer
Online Quantization
Quantized KV Cache
AMD Quark
TorchAO
LLM Compressor
LLM Compressor
FP8 W8A8
INT4 W4A16
INT8 W4A8
INT8 W8A8
Speculative Decoding
Speculative Decoding
Per-Request Acceptance Metrics
Adaptive Verification
Draft Models
Dynamic Speculative Decoding
EAGLE Draft Models
Hidden State Extraction
LiLiCorr
MLP Draft Models
MTP (Multi-Token Prediction)
N-Gram Speculation
Parallel Draft Models
vLLM-Project/Speculators
Suffix Decoding
Developer Guide
Developer Guide
General
General
Deprecation Policy
Dockerfile
Editing Agent Instructions
Incremental Compilation Workflow
JIT Kernel Warmup
Labels
Profiling vLLM
Releasing vLLM
Vulnerability Management
Model Implementation
Model Implementation
Basic Model
Registering a Model
Unit Testing
Multi-Modal Support
Speech-to-Text (Transcription/Translation) Support
CI
CI
CI Failures
Nightly Builds of vLLM Wheels
Update PyTorch version on vLLM OSS CI/CD
Design Documents
Design Documents
Plugins
Plugins
Endpoint Plugins
IO Processor Plugins
LoRA Resolver Plugins
Plugin System
Architecture Overview
Attention Backend Feature Support
CUDA Graphs
Vision Encoder (ViT) CUDA Graphs
CustomOp
Dual Batch Overlap
How to debug the vLLM-torch.compile integration
Fused MoE Modular Kernel
Fusion torch.compile passes
HiSparse local KV offload architecture
Integration with Hugging Face
Hybrid KV Cache Manager
Logits Processors
Metrics
Multi-Modal Data Processing
Model Runner V2 Design Document
Fused MoE Kernel Features
Python Multiprocessing
NIXL KV Cache Lease Renewal
NIXL push-mode KV transfer
Optimization Levels
Paged Attention
Automatic Prefix Caching
torch.compile integration
torch.compile with Multimodal Encoders
vLLM IR: Functional Intermediate Representation
Benchmarking
Benchmarking
Benchmark CLI
Parameter Sweeps
Performance Dashboard
API Reference
API Reference
vllm
vllm
collect_env
connections
env_override
envs
exceptions
forward_context
logger
logits_process
logprobs
model_inspection
outputs
pooling_params
sampling_params
scalar_type
scripts
sequence
tasks
version
assets
assets
audio
base
image
video
benchmarks
benchmarks
latency
mm_processor
plot
serve
startup
throughput
datasets
datasets
create_txt_slices_dataset
datasets
utils
lib
lib
endpoint_request_func
ready_checker
utils
sweep
sweep
cli
param_sweep
plot
plot_pareto
serve
serve_workload
server
startup
utils
compilation
compilation
backends
base_static_graph
breakable_cudagraph
caching
codegen
compiler_interface
counter
cuda_graph
decorators
monitor
partition_rules
piecewise_backend
wrapper
passes
passes
fx_utils
inductor_pass
pass_manager
vllm_inductor_pass
fusion
fusion
act_quant_fusion
add_rms_fusion
allreduce_rms_fusion
attn_quant_fusion
collective_fusion
matcher_utils
mla_attn_quant_fusion
mla_rope_kvcache_cat_fusion
qk_norm_rope_fusion
qk_norm_rope_kvcache_fusion
rms_quant_fusion
rocm_aiter_fusion
rope_kvcache_fusion
sequence_parallelism
ir
ir
clone_elimination
inplace_functionalization
lowering_pass
utils
utility
utility
fix_functionalization
noop_elimination
post_cleanup
scatter_split_replace
split_coalescing
config
config
attention
aux_output
cache
compilation
device
diffusion
ec_manager_config
ec_transfer
engram
fault_tolerance
kernel
kv_events
kv_transfer
load
logging
lora
mamba
model
model_arch
multimodal
observability
offload
parallel
pooler
profiler
quantization
reasoning
scheduler
speculative
speech_to_text
structured_outputs
utils
vllm
watermarking
weight_transfer
cute_utils
cute_utils
cvt
mbarrier
device_allocator
device_allocator
alloc_conf
cumem
sleep_mode_backend
xpumem
distributed
distributed
communication_op
kv_events
mooncake_store
nixl_utils
parallel_state
stateless_coordinator
utils
aux_output_connector
aux_output_connector
connector
routed_experts
store
worker
device_communicators
device_communicators
aiter_custom_all_reduce
all2all
all_reduce_utils
base_device_communicator
cpu_communicator
cuda_communicator
cuda_wrapper
custom_all_reduce
flashinfer_all_reduce
flashinfer_pcie_ipc_all_reduce
mnnvl_compat
pynccl
pynccl_allocator
pynccl_wrapper
quick_all_reduce
ray_communicator
shm_broadcast
shm_object_storage
symm_mem
xpu_communicator
ec_transfer
ec_transfer
ec_transfer_state
ec_connector
ec_connector
base
example_connector
factory
metrics
mooncake_ec_connector
utils
cpu
cpu
common
connector
ec_shared_region
protocol
session
utils
control
control
base
zmq
data
data
base
nixl
scheduler
scheduler
embedding_cache
worker
worker
descriptor_buffers
mooncake
mooncake
config
control
memory
metadata
producer
reservation
scheduler
state
transfer
worker
mooncake_store_embedding
mooncake_store_embedding
backend
data
store_client
elastic_ep
elastic_ep
elastic_execute
elastic_state
standby_state
eplb
eplb
async_worker
eplb_communicator
eplb_state
eplb_utils
rebalance_execute
policy
policy
abstract
default
kv_transfer
kv_transfer
kv_transfer_state
kv_connector
kv_connector
base
factory
utils
v1
v1
base
decode_bench_connector
example_connector
example_hidden_states_connector
flexkv_connector
lmcache_connector
lmcache_mp_connector
metrics
multi_connector
offloading_connector
simple_cpu_offload_connector
ssm_conv_transfer_utils
hf3fs
hf3fs
hf3fs_client
hf3fs_connector
hf3fs_metadata_server
utils
utils
common
gather_scatter_helper
hf3fs_mock_client
hisparse
hisparse
connector
stats
worker
lmcache_integration
lmcache_integration
multi_process_adapter
utils
vllm_v1_adapter
mooncake
mooncake
mooncake_connector
mooncake_utils
rdma_utils
stats
store
store
connector
coordinator
data
metrics
protocol
scheduler
worker
moriio
moriio
moriio_common
moriio_connector
moriio_engine
moriio_layout
nixl
nixl
base_scheduler
base_worker
connector
metadata
pull_scheduler
pull_worker
push_scheduler
push_worker
scheduler
stats
tp_mapping
utils
worker
offloading
offloading
canonical_mapping
common
config
events
metrics
scheduler
worker
weight_transfer
weight_transfer
base
clients
factory
ipc_engine
m2n_common
m2n_engine
m2n_layout
m2n_source
m2n_trainer
nccl_common
nccl_engine
packed_tensor
sharded_rdt_common
sharded_rdt_engine
sharded_rdt_fake
sharded_rdt_trainer
sparse_nccl_engine
engine
engine
arg_utils
async_llm_engine
llm_engine
protocol
entrypoints
entrypoints
chat_utils
grpc_server
llm
offline_utils
anthropic
anthropic
api_router
protocol
serving
cli
cli
collect_env
launch
main
openai
preload
run_batch
serve
snapshot
types
benchmark
benchmark
base
latency
main
mm_processor
serve
startup
sweep
throughput
cohere
cohere
api_router
cohere_chat_message
protocol
serving
generate
generate
api_router
factories
base
base
protocol
serving
beam_search
beam_search
offline
online
utils
generative_scoring
generative_scoring
api_router
serving
launchers
launchers
app
cli_args
dp_supervisor
grpc_server
launcher
run_batch
api_server
api_server
app_state
entry
routers
render
render
app_state
entry
utils
utils
constants
server_utils
ssl
mcp
mcp
tool
tool_server
openai
openai
api_server
run_batch
chat_completion
chat_completion
api_router
batch_serving
protocol
serving
completion
completion
api_router
protocol
serving
models
models
api_router
protocol
serving
parser
parser
harmony_utils
responses
responses
api_router
context
harmony
protocol
serving
streaming_events
utils
pooling
pooling
factories
offline
typing
utils
base
base
io_processor
protocol
serving
classify
classify
api_router
io_processor
protocol
serving
embed
embed
api_router
io_processor
protocol
serving
pooling
pooling
api_router
io_processor
protocol
serving
scoring
scoring
api_router
io_processor
protocol
serving
typing
utils
scale_out
scale_out
factories
derender
derender
api_router
serving
render
render
api_router
serving
token_in_token_out
token_in_token_out
api_router
mm_features
mm_serde
protocol
serving
serve
serve
dev
dev
cache
cache
api_router
rlhf
rlhf
api_router
rpc
rpc
api_router
server_info
server_info
api_router
sleep
sleep
api_router
elastic_ep
elastic_ep
api_router
middleware
engine
engine
protocol
serving
typing
exception_handling
exception_handling
error_response
register
utils
handlers
handlers
exception
http
validation
vllm_error
fault_tolerance
fault_tolerance
api_router
instrumentator
instrumentator
basic
health
metrics
offline_docs
lora
lora
api_router
protocol
middleware
middleware
authenticate
log_response
register
x_request_id
profile
profile
api_router
sagemaker
sagemaker
api_router
tokenize
tokenize
api_router
protocol
serving
utils
utils
api_utils
fingerprint
orca_metrics
request_logger
sse_keep_alive
tool_calls_utils
speech_to_text
speech_to_text
factories
base
base
protocol
serving
utils
realtime
realtime
api_router
connection
metrics
protocol
serving
transcription
transcription
api_router
protocol
serving
translation
translation
api_router
protocol
serving
inputs
inputs
engine
llm
ir
ir
op
tolerances
util
ops
ops
activation
layernorm
kernels
kernels
aiter_ops
oink_ops
vllm_c
helion
helion
case_key
config_manager
register
utils
ops
ops
dynamic_per_token_scaled_fp8_quant
fused_qk_norm_rope
per_token_group_fp8_quant
rms_norm_dynamic_per_token_quant
rms_norm_per_block_quant
silu_and_mul_per_block_quant
silu_mul_fp8
triton
triton
activation
qkv_padded_fp8_quant
logging_utils
logging_utils
access_log_filter
dump_input
formatter
lazy
log_time
torch_tensor
lora
lora
lora_model
lora_weights
model_manager
peft_helper
request
resolver
utils
worker_manager
layers
layers
base
base_linear
classifier
column_parallel_linear
fused_moe
logits_processor
replicated_linear
row_parallel_linear
utils
vocab_parallel_embedding
ops
ops
torch_ops
torch_ops
lora_ops
triton_ops
triton_ops
fp8_kernel_utils
fused_moe_lora_fp8_op
fused_moe_lora_op
kernel_utils
lora_expand_fp8_op
lora_expand_op
lora_kernel_metadata
lora_shrink_fp8_op
lora_shrink_op
utils
xpu_ops
xpu_ops
lora_ops
punica_wrapper
punica_wrapper
punica_base
punica_cpu
punica_gpu
punica_selector
punica_xpu
utils
model_executor
model_executor
custom_op
parameter
utils
determinism
determinism
batch_invariant
batch_invariant_configs
hw_agnostic
hw_agnostic
custom_op
layers
layers
activation
layernorm
kernels
kernels
attention
attention
dsa
dsa
candidate_blocks
dcp_indexer_cutedsl
sparse_mqa_logits
linear
linear
base
zentorch_utils
cute_dsl
cute_dsl
gemm_rs_ar
ll_bf16
skinny_gemm
mixed_precision
mixed_precision
conch
cpu
cutlass
dynamic_4bit
exllama
humming
MPLinearKernel
machete
marlin
rdna3_w4a16
rdna_hybrid_w4a16
triton_w4a16
xpu
zentorch
mxfp4
mxfp4
aiter
b12x
base
emulation
flashinfer
humming
marlin
xpu
mxfp6
mxfp6
base
emulation
humming
mxfp8
mxfp8
b12x
deep_gemm
emulation
flashinfer
humming
Mxfp8LinearKernel
marlin
rocm_block32_gemm
rocm_native