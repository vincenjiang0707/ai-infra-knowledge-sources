source: https://docs.nvidia.com/dynamo/zh-CN/reference/releases/deprecations
lastmod: 2026-09-23T23:30:39.914Z

# Deprecations

This page is the ledger of breaking changes, behavioral changes, and deprecations and removals for each Dynamo release, mirrored verbatim from the GitHub release notes. Each entry carries a badge: Removed means the surface is gone, Deprecated means it still works but emits warnings, and Behavioral means defaults or behavior changed.

Upgrading? Pick the version you run today to see the dependency migration and the exact reading list.

Upgrade to v1.5.0

Pins shown from v1.4.2, the latest release on the v1.4.x line.

Pins shown from v1.3.1, the latest release on the v1.3.x line.

Pins shown from v1.2.1, the latest release on the v1.2.x line.

Pins shown from v1.1.1, the latest release on the v1.1.x line.

Pins shown from v1.0.2, the latest release on the v1.0.x line.


## v1.5.0 — Sep 18, 2026

Deprecated **KVBM (KV Block Manager) is deprecated in v1.5.0 and removal is targeted for v1.6.0; the kvbm wheel and the vLLM KVBM launch and deploy examples ship unchanged for this release**.


Migrate:Use the engine’s native KV offloading for host and disk tiering. Cross-node KV cache sharing is the scope of the separate, early-stage KV Cache Runner (KVCR) project, which does not replace KVBM.

Removed **CRD storage version promoted from v1alpha1 to v1beta1, with examples and Profiler output moving with it** ([#11904](https://github.com/ai-dynamo/dynamo/pull/11904), [#12375](https://github.com/ai-dynamo/dynamo/pull/12375), [#12506](https://github.com/ai-dynamo/dynamo/pull/12506)).


Migrate:Upgrade the operator so the built-in CRD migrator converts stored objects.

Removed **v1alpha1 admission webhook endpoints removed, and DGD and DCD validation served only at v1beta1 paths** ([#11177](https://github.com/ai-dynamo/dynamo/pull/11177)).


Migrate:Update any custom Validating/MutatingWebhookConfiguration (not managed by the bundled Helm chart) to point at the v1beta1 DGD admission paths with apiVersions: [v1beta1].

Removed **Go EPP removed, and the Rust EPP shipped inside the Frontend image is the default Endpoint Picker** ([#11355](https://github.com/ai-dynamo/dynamo/pull/11355)).


Migrate:Update EPP deployment manifests and flags to the Rust EPP (LW-EPP) contract.

Deprecated ** eppConfig deprecated; it remains honored so a DynamoGraphDeployment pinned to a 1.4 Go EPP image keeps working after the Operator upgrade** (


[#11355](https://github.com/ai-dynamo/dynamo/pull/11355)).


Migrate:Omit`eppConfig`

to use the Rust EPP; the field goes away with the Go EPP contract in a later release.

Removed **Dynamo Snapshot moved to a standalone operator, removing the bundled chart, PodSnapshot CRDs, and reconciliation from Dynamo Operator** ([#13177](https://github.com/ai-dynamo/dynamo/pull/13177)).


Migrate:Snapshot v0.1.0 now installs as its own operator from`oci://ghcr.io/ai-dynamo/snapshot/snapshot:0.1.0`

. For evaluation, the Dynamo platform chart can install it as a subchart with`global.snapshot.install=true`

, which is off by default. For production, install the Snapshot chart separately before upgrading Dynamo Operator, then set`checkpoint.enabled=true`

on the operator to turn checkpoint and restore back on.

Removed **DynamoCheckpoint CRD, its Helm values, and DYN_SNAPSHOT_RESTORE_STANDBY removed, and checkpointRef now names a PodSnapshot** (


[#14076](https://github.com/ai-dynamo/dynamo/pull/14076)).


Migrate:Delete legacy DynamoCheckpoint resources, create PodSnapshot resources through the Snapshot operator, and point`checkpointRef`

at the PodSnapshot.

Removed **Unified-backend entry point and logits-processing adapters removed from the SGLang and vLLM workers** ([#12792](https://github.com/ai-dynamo/dynamo/pull/12792)).


Migrate:Drop the unified-backend flag from SGLang/vLLM launch commands and use the standard worker invocation shown in the updated CLI templates.

Removed **AIConfigurator renamed to AISimulate: aiconfigurator wheels replaced by the aisimulate package, and the python -m dynamo.replay CLI removed** (


[#13665](https://github.com/ai-dynamo/dynamo/pull/13665)).


Migrate:Install the consolidated`aisimulate`

wheel/`aisimulate-core`

crate instead of the separate`aiconfigurator`

packages (compatibility import namespaces ship inside the AISimulate wheel).

Removed **Planner performance-model and Mocker engine bindings removed from dynamo._core** (

[#12454](https://github.com/ai-dynamo/dynamo/pull/12454),

[#12446](https://github.com/ai-dynamo/dynamo/pull/12446),

[#12525](https://github.com/ai-dynamo/dynamo/pull/12525)).

Removed **Offline replay API returns a single ReplayReport, --report-jsonl renamed to --per-request-jsonl, and per-request capture is opt-in** (



[#12363](https://github.com/ai-dynamo/dynamo/pull/12363)).


Migrate:Update replay invocations/scripts to pass`--per-request-jsonl`

instead of`--report-jsonl`

.

Removed **SGLang call_tokenizer_manager passthrough route and RLMixin export removed** (


[#12246](https://github.com/ai-dynamo/dynamo/pull/12246)).


Migrate:Declare each needed tokenizer-manager or engine method explicitly with`--engine-route`

(or`DYN_SGLANG_ENGINE_ROUTES`

) and call the configured`/engine/<path>`

instead of the generic`call_tokenizer_manager`

endpoint.

Removed **PodSnapshot capture target now comes from the required PodReference.Containers field instead of a pod annotation** (

[#12068](https://github.com/ai-dynamo/dynamo/pull/12068)).


Migrate:Update the PodSnapshot/PodSnapshotContent CRDs and add exactly one entry to spec.source.podRef.containers in any hand-authored manifests, otherwise admission rejects them.

Removed **GMS Snapshot feature gate removed, and IntraPod Snapshot enabled by default under the Checkpoint gate and unsupported combinations rejected** ([#12685](https://github.com/ai-dynamo/dynamo/pull/12685)).


Migrate:Remove the GMS Snapshot feature-gate setting from your operator Helm values/args.

Deprecated **Automatic tokenizer fallback to Hugging Face is deprecated and will stop being the default** ([#12923](https://github.com/ai-dynamo/dynamo/pull/12923)).


Migrate:Set —no-tokenizer-fallback or DYN_TOKENIZER_FALLBACK=false to adopt the future behavior now, and ensure your model’s tokenizer.json is supported by the selected backend.

Removed **Removed nsRestorePath snapshot config/Helm value** (

[#12626](https://github.com/ai-dynamo/dynamo/pull/12626)).


Migrate:Delete any`nsRestorePath`

setting from snapshot chart values/config.

Removed **Shared AWS EFA Kustomize components removed in favor of instance-type template selections** ([#13125](https://github.com/ai-dynamo/dynamo/pull/13125)).


Migrate:Update overlays that referenced the aws-efa-p8d8/p8d16/p16d16 shared Components to select the new instance-type template (e.g. templates/aws-efa/p5.48xlarge) or the local components/efa Component.

Removed **Legacy Nemotron-3-Ultra Day-0 recipe manifests replaced by Refresh profile paths without the nvcr-secret imagePullSecret** (

[#13226](https://github.com/ai-dynamo/dynamo/pull/13226)).


Migrate:Update any references/automation pointing at the old Day-0 recipe directories to the corresponding new Refresh profile paths (SKU + context + serving shape).

Removed **Qwen3.8-2.4T-A95B recipe renamed with an -fp8 suffix, changing the served model name and weight cache key** (

[#13265](https://github.com/ai-dynamo/dynamo/pull/13265)).


Migrate:Re-run the model-download Job to fetch Qwen/Qwen3.8-2.4T-A95B-FP8 and update any client requests to use the new served model name.

Removed **DeepSeek-V4 model-download manifest split and renamed, and the default downloaded checkpoint is now FP8** ([#13034](https://github.com/ai-dynamo/dynamo/pull/13034)).


Migrate:Apply the SKU-specific manifest (model-download-fp8.yaml for H200/most variants, model-download-nvfp4.yaml for B200 agentic variants) instead of the removed model-download.yaml, and update any references to the old Job name.

Behavioral **Guided tool calls stream incrementally by default instead of a single terminal chunk** ([#12576](https://github.com/ai-dynamo/dynamo/pull/12576)).


Migrate:Clients that assumed a single complete tool-call chunk must accumulate incremental tool-call argument deltas, or set DYN_ENABLE_GUIDED_TOOL_STREAMING=0 to restore buffering.

Behavioral **Over-context requests rejected before streaming, and an omitted max_tokens now derives from the engine-published TokenBudget** (

[#12092](https://github.com/ai-dynamo/dynamo/pull/12092)).


Migrate:Update clients and retry/monitoring logic to handle a non-200 HTTP client error for over-context requests instead of an inline streamed error.

Behavioral **Thinking/reasoning controls resolved once with new precedence and written to all three template keys** ([#11739](https://github.com/ai-dynamo/dynamo/pull/11739)).


Migrate:If you relied on the previous per-backend resolution or on only`enable_thinking`

being set, drop manual chat_template_args thinking overrides and rely on the documented precedence order.

Behavioral **Gemma 4 reasoning parsing now requires explicit enable_thinking=true** ([#13061](https://github.com/ai-dynamo/dynamo/pull/13061)).


Migrate:Set`chat_template_args: {"enable_thinking": true}`

in requests to Gemma 4 models to keep receiving parsed reasoning_content.

Behavioral **Embedding tokenization adds special tokens by default and moves to the worker, with Frontend tokenization opt-in** ([#12157](https://github.com/ai-dynamo/dynamo/pull/12157)).


Migrate:Set`add_special_tokens: false`

on embedding requests or export DYN_EMBEDDING_TOKENIZATION_ADD_SPECIAL_TOKENS=false to keep the previous tokenization behavior.

Behavioral **vLLM encode worker embedding cache now disabled by default (gated on —multimodal-embedding-cache-capacity-gb)** ([#14452](https://github.com/ai-dynamo/dynamo/pull/14452)).


Migrate:Set —multimodal-embedding-cache-capacity-gb to a positive value to keep embedding caching in the vLLM encode worker.

Behavioral **DGD, DCD, and DGDR admission requires a main container image, and a non-semver image tag (digest, custom build tag, or :latest) requires runtimeVersionOverride** (


[#10494](https://github.com/ai-dynamo/dynamo/pull/10494)).


Migrate:Set the main container image on every component (`spec.components[*].podTemplate.spec.containers[name=main].image`

in v1beta1,`spec.services.<name>.extraPodSpec.mainContainer.image`

in v1alpha1) and add`runtimeVersionOverride: "<X.Y.Z>"`

wherever the image tag is not a semantic version, including a DGDR whose`spec.image`

is not. The checks are ratcheted: an unchanged existing component stays admissible, but adding or changing an image applies them, so set the override in the same update that changes the tag. Full details are in the[platform chart upgrading notes].

Behavioral **runtimeVersionOverride now participates in worker hash and can trigger rollouts** ([#12633](https://github.com/ai-dynamo/dynamo/pull/12633)).


Migrate:Before upgrading, ensure runtimeVersionOverride matches the image’s actual runtime version and expect a one-time worker rollout when the resolved version (>=1.5.0) changes.

Behavioral **Worker canary health checks enabled by default in operator-rendered pods** ([#11083](https://github.com/ai-dynamo/dynamo/pull/11083)).


Migrate:Set DYN_HEALTH_CHECK_ENABLED=false explicitly in the worker container env if you need the previous behavior.

Behavioral **Worker liveness probe failureThreshold default raised from 1 to 3 for runtime >= 1.5.0** ([#13512](https://github.com/ai-dynamo/dynamo/pull/13512)).


Migrate:No action needed unless you rely on immediate restart on first liveness failure.

Behavioral ** nvidia.com/workload-provider is persisted and immutable, with no fallback to the Component provider when Grove is unavailable** (

[#12942](https://github.com/ai-dynamo/dynamo/pull/12942)).


Migrate:To change the workload provider of an existing DynamoGraphDeployment, delete and recreate the DGD instead of toggling nvidia.com/enable-grove or the Grove feature gate.

Behavioral **Elastic-EP components require an explicit container command, and single-pod components start a Ray head and inject POD_IP and VLLM_DP_M*** (


[#12943](https://github.com/ai-dynamo/dynamo/pull/12943)).


Migrate:If you set —enable-elastic-ep on a single-pod component and relied on it being a no-op, remove the flag.

Behavioral **componentType/type fields are now immutable after being set** ([#13763](https://github.com/ai-dynamo/dynamo/pull/13763)).


Migrate:Delete and recreate the DynamoComponentDeployment/DynamoGraphDeployment (or component) instead of editing its componentType/type field in place.

Behavioral **vLLM STORAGE KV events now indexed on the Disk tier, and REMOTE or unknown-locality events dropped** ([#11571](https://github.com/ai-dynamo/dynamo/pull/11571)).


Migrate:Expect STORAGE offload prefixes to be scored via the Disk tier and non-local (REMOTE/unknown locality) KV events to be ignored.

Behavioral ** DYN_USE_KV_EVENTS renamed to DYN_ROUTER_USE_KV_EVENTS (alias kept), and previously ignored DYN_* Router env vars now honored** (



[#13840](https://github.com/ai-dynamo/dynamo/pull/13840)).


Migrate:Switch to DYN_ROUTER_USE_KV_EVENTS.

Behavioral **DYN_RUNTIME_NUM_WORKER_THREADS / DYN_RUNTIME_MAX_BLOCKING_THREADS now actually apply to the runtime serving traffic** ([#13849](https://github.com/ai-dynamo/dynamo/pull/13849)).


Migrate:Re-check any explicit DYN_RUNTIME_NUM_WORKER_THREADS / DYN_RUNTIME_MAX_BLOCKING_THREADS values (and unset ones relying on the old per-CPU/512 sizing) since they now change frontend thread counts and concurrency.

Behavioral **EPP replica sync validates POD_IP at config-parse time and no longer resolves the port from the replica-agg Service port** (


[#13811](https://github.com/ai-dynamo/dynamo/pull/13811)).


Migrate:Ensure every EPP replica binds the same replica-sync port (9092 by default) and set DYN_EPP_REPLICA_SYNC_PORT if your existing`replica-agg`

targetPort differed.

Behavioral **Standalone router —endpoint namespace now overridden by DYN_NAMESPACE / worker suffix** ([#12160](https://github.com/ai-dynamo/dynamo/pull/12160)).


Migrate:If you relied on the namespace embedded in —endpoint, unset/align DYN_NAMESPACE and DYN_NAMESPACE_WORKER_SUFFIX so the router resolves workers in the intended namespace.

Behavioral **Unsupported tool_call_parser names now rejected at model registration** ([#13828](https://github.com/ai-dynamo/dynamo/pull/13828)).


Migrate:Set —tool-call-parser (or tool_call_parser in runtime config) to one of the parser names listed in the new validation error message before upgrading.

Behavioral **tool_call arguments auto-normalized to JSON object for glm47 tool_call_parser** ([#12332](https://github.com/ai-dynamo/dynamo/pull/12332)).


Migrate:If you rely on the raw JSON-string form of historical tool_call arguments with the glm47 tool_call_parser, explicitly set tool_call_arguments_format: json_string in the model runtime config.

Behavioral **Snapshot saver/loader CLI without —device now fans out to all visible GPUs** ([#13301](https://github.com/ai-dynamo/dynamo/pull/13301)).


Migrate:Pass an explicit —device N to retain single-process behavior.

Behavioral **Planner Prometheus requests now time out after 10s and no longer retry** ([#13245](https://github.com/ai-dynamo/dynamo/pull/13245)).


Migrate:If your Prometheus endpoint is slow, raise the limit via DYN_PLANNER_PROMETHEUS_REQUEST_TIMEOUT_SECONDS or metric_pulling_prometheus_request_timeout_seconds, and expect failed queries to no longer be retried within a collection cycle.

Behavioral **Profiler-generated vLLM worker args no longer pin —max-model-len, and naive fallback now sizes from declared workload isl/osl** ([#14205](https://github.com/ai-dynamo/dynamo/pull/14205)).


Migrate:Re-run the profiler and, if a specific context length is required, set —max-model-len explicitly via DGD overrides since the generated config no longer pins it.

Behavioral **JPEG decoding switches to libjpeg-turbo by default when libturbojpeg is present** ([#11157](https://github.com/ai-dynamo/dynamo/pull/11157)).


Migrate:Set DYN_MM_ENABLE_LIBJPEG=0 to keep the previous pure-Rust image::ImageReader JPEG decode path (pixel output may differ slightly from TurboJPEG).


## v1.4.0 — Aug 14, 2026

51 entries — 43 behavioral changes, 8 deprecated and removed.

Behavioral **Router queueing disabled by default (—router-queue-threshold default removed)** ([#11599](https://github.com/ai-dynamo/dynamo/pull/11599)).


Migrate:Explicitly set —router-queue-threshold=16.0 (or DYN_ROUTER_QUEUE_THRESHOLD=16.0) to keep the previous queueing behavior.

Behavioral **DYN_SELF_HOST_METADATA now defaults to ON** ([#11417](https://github.com/ai-dynamo/dynamo/pull/11417)).


Migrate:Set DYN_SYSTEM_PORT (e.g. 9090) on workers to enable self-hosted MDC serving, or set DYN_SELF_HOST_METADATA=0 to restore the previous shared-storage behavior.

Behavioral **Frontend no longer honors truncation config baked into tokenizer.json** ([#11792](https://github.com/ai-dynamo/dynamo/pull/11792)).


Migrate:If you relied on tokenizer.json’s baked-in truncation to shorten long prompts, truncate client-side or set an explicit context/length limit, since the Frontend now errors on over-length prompts instead of clipping them.

Behavioral **Session affinity now falls back to agent session headers when x-dynamo-session-id is absent** ([#11677](https://github.com/ai-dynamo/dynamo/pull/11677)).


Migrate:Clients sending agent session headers (e.g. Claude Code/Codex/OpenCode) will now be pinned to a worker; omit those headers or set an explicit x-dynamo-session-id if the previous non-affinity routing is desired.

Behavioral **Multimodal load sites no longer force trust_remote_code=True** ([#10738](https://github.com/ai-dynamo/dynamo/pull/10738)).


Migrate:Enable trust-remote-code on the engine (vLLM/SGLang —trust-remote-code, TensorRT-LLM extra_engine_args trust_remote_code: true, or —trust-remote-code for the trtllm mm_router_worker example) when serving multimodal models that require custom remote code.

Behavioral **Policy classes without a busy threshold no longer fall back to 16.0** ([#11599](https://github.com/ai-dynamo/dynamo/pull/11599)).


Migrate:Add an explicit numeric queue threshold to each policy class in the policy-config YAML to retain queueing.

Behavioral **Direct dispatch now bypasses local worker inhibition** ([#11993](https://github.com/ai-dynamo/dynamo/pull/11993)).


Migrate:Remove the worker through service discovery if you depended on inhibited workers being skipped for direct-routed requests; direct dispatch does not consult the local inhibition set.

Behavioral **Decode workers now advertise local indexer support** ([#12084](https://github.com/ai-dynamo/dynamo/pull/12084)).


Migrate:If decode workers should not advertise a local indexer, explicitly disable enable_local_indexer for those workers.

Behavioral **init_weights_update_group now bounded by 30s watchdog that terminates the worker** ([#11418](https://github.com/ai-dynamo/dynamo/pull/11418)).


Migrate:If your RL weight-update rendezvous can take longer than 30 seconds, set DYN_RL_INIT_WEIGHTS_TIMEOUT_S to a larger value on the vLLM worker.

Behavioral **TensorRT-LLM video_url now enforced through shared SSRF/URL validation policy** ([#12002](https://github.com/ai-dynamo/dynamo/pull/12002)).


Migrate:Set DYN_MM_ALLOW_INTERNAL=1 if you rely on internal/private/plaintext-HTTP video URLs with the TensorRT-LLM backend, otherwise switch to HTTPS public URLs.

Behavioral **Omitted/string thinking values now normalized; omitted thinking treated as enabled for kimi_k25 reasoning parsing** ([#11653](https://github.com/ai-dynamo/dynamo/pull/11653)).


Migrate:If you relied on Kimi post-tool output arriving in`content`

(including the`</think>`

marker) or on string values like “false” being treated as truthy, set`chat_template_kwargs.thinking`

explicitly and read reasoning from`reasoning_content`

.

Behavioral **Tokenizer cache byte budget default increased** ([#11078](https://github.com/ai-dynamo/dynamo/pull/11078)).


Migrate:Explicitly set DYN_TOKENIZER_CACHE_BYTES=52428800 to keep the previous 50 MiB budget.

Behavioral **EPP default RUST_LOG changed from debug/kv_router=trace to info** ([#11550](https://github.com/ai-dynamo/dynamo/pull/11550)).


Migrate:Explicitly set RUST_LOG=debug,dynamo_llm::kv_router=trace on the EPP component if verbose KV-router trace logging is still required.

Behavioral **Monitoring scripts now target dynamo-system namespace by default instead of dynamo** ([#10771](https://github.com/ai-dynamo/dynamo/pull/10771)).


Migrate:If your dynamo-platform release is installed in the ‘dynamo’ namespace, export DYNAMO_NAMESPACE=dynamo before running setup-monitoring.sh or cleanup-monitoring.sh.

Behavioral **arrivalIntervalMs default changed from 0.0 to None** ([#12062](https://github.com/ai-dynamo/dynamo/pull/12062)).


Migrate:Explicitly set arrivalIntervalMs (or another arrival controller) instead of relying on the previous 0.0 default and its implicit 1 ms fallback.

Behavioral **Event-plane subjects/keys are now endpoint-scoped with no backward-compatible fallback** ([#11841](https://github.com/ai-dynamo/dynamo/pull/11841)).


Migrate:Upgrade all workers, routers, and planner/consumer components together; mixed old/new versions will not see each other’s events.

Behavioral **Embedding worker now returns pooled, L2-normalized vectors instead of per-token hidden states** ([#10248](https://github.com/ai-dynamo/dynamo/pull/10248)).


Migrate:Update any client code that depended on the previous variable-length, un-normalized embedding payload to expect a single fixed-dimension normalized vector per input.

Behavioral **Audit subsystem migrated into request trace** (`"log_type":"audit"`

records and the `"Audit sinks ready"`

readiness marker -> records carrying `"schema":"dynamo.request.trace.v1"`

and the `"Request trace sinks ready"`

marker). Payload logging is unified under the request-trace pipeline and the standalone audit module is gone ([#9390](https://github.com/ai-dynamo/dynamo/pull/9390), [#11180](https://github.com/ai-dynamo/dynamo/pull/11180)).


Migrate:Update log pipelines that match on the`"Audit sinks ready"`

marker or the`"log_type":"audit"`

field to the new marker and the`"schema":"dynamo.request.trace.v1"`

field. The`DYN_AUDIT_*`

environment variables are still honored as legacy aliases of their request-trace replacements (for example`DYN_AUDIT_SINKS`

->`DYN_REQUEST_TRACE_SINKS`

,`DYN_AUDIT_FORCE_LOGGING`

->`DYN_REQUEST_TRACE_RECORDS=request_payload`

); move configuration to the new names.

Behavioral ** dimensions on /v1/embeddings now validated by vLLM pooler; requires Matryoshka-declared models** (

[#10248](https://github.com/ai-dynamo/dynamo/pull/10248)).


Migrate:Launch embedding workers for non-Matryoshka models (e.g. Qwen3-Embedding) with`--hf-overrides '{"is_matryoshka": true}'`

if clients send the`dimensions`

parameter.

Behavioral **max_tokens: 0 now rejected with HTTP 400 on /v1/chat/completions** ([#11394](https://github.com/ai-dynamo/dynamo/pull/11394)).


Migrate:Send max_tokens >= 1 (or use max_completion_tokens) on /v1/chat/completions requests instead of 0.

Behavioral **Nested chat_template inside chat_template_args/kwargs now rejected with 400** ([#11755](https://github.com/ai-dynamo/dynamo/pull/11755)).


Migrate:Stop sending`chat_template`

inside`chat_template_args`

/`chat_template_kwargs`

; configure the chat template server-side instead.

Behavioral **Bundled NATS subchart disabled by default** ([#11951](https://github.com/ai-dynamo/dynamo/pull/11951)).


Migrate:Set —set global.nats.install=true (or configure dynamo-operator.natsAddr for external NATS) if your deployment relies on NATS transports, otherwise NATS resources and the NATS_SERVER env var are removed on upgrade.

Behavioral **Grove subchart/API dependency now requires v0.1.0-alpha.11 or later; v1.4.0 ships v0.1.0-alpha.12-rc1 (ClusterTopologyBinding API required)** ([#8225](https://github.com/ai-dynamo/dynamo/pull/8225)).


Migrate:Upgrade externally-installed Grove to >= v0.1.0-alpha.11 in lockstep with Dynamo, since older Grove releases using the ClusterTopology API are no longer compatible.

Behavioral **Namespace-restricted installs must set dynamo-operator.upgradeCRD=false** ([#11689](https://github.com/ai-dynamo/dynamo/pull/11689)).


Migrate:Set`--set dynamo-operator.upgradeCRD=false`

for namespace-restricted installations and rely on the cluster-wide Operator for CRDs.

Behavioral **Snapshot chart init container now sets imagePullPolicy explicitly (default Always)** ([#10864](https://github.com/ai-dynamo/dynamo/pull/10864)).


Migrate:If you override daemonset.initContainer.image with a pinned tag and rely on cached images, set daemonset.initContainer.imagePullPolicy: IfNotPresent in your values file.

Behavioral **Dev-pod script ConfigMap must now include managed_state.py key** ([#9790](https://github.com/ai-dynamo/dynamo/pull/9790)).


Migrate:Add a managed_state.py key to the power-agent dev-pod script ConfigMap before upgrading to chart 1.3.0, per templates/dev-pod.yaml header.

Behavioral **Tokenizer L1 prefix cache now enabled by default** ([#11078](https://github.com/ai-dynamo/dynamo/pull/11078)).


Migrate:Set`DYN_TOKENIZER_CACHE=0`

to restore the previous disabled-by-default tokenizer cache behavior.

Behavioral **New required env var DYN_EPP_TOKENIZER_PROTOCOL for standalone EPP** ([#11827](https://github.com/ai-dynamo/dynamo/pull/11827)).


Migrate:Set`DYN_EPP_TOKENIZER_PROTOCOL=vllm-render`

in existing standalone EPP deployments, otherwise config parsing fails at startup.

Behavioral **New required env var DYN_EPP_TOKENIZER_SERVICE_URL for standalone EPP** ([#11827](https://github.com/ai-dynamo/dynamo/pull/11827)).


Migrate:Set`DYN_EPP_TOKENIZER_SERVICE_URL`

to the vLLM render endpoint base URL; validation rejects empty or non-absolute URLs.

Behavioral **HTTP header capture in trace records is an explicit fail-closed allowlist**: request headers appear in `request_payload`

records only when named in `DYN_REQUEST_TRACE_HTTP_HEADER_CAPTURE_LIST`

; when the variable is unset or empty, no headers are captured ([#11386](https://github.com/ai-dynamo/dynamo/pull/11386)).


Migrate:Set`DYN_REQUEST_TRACE_HTTP_HEADER_CAPTURE_LIST`

to the comma-separated header names you need recorded. Captured values are unredacted, so avoid allowlisting credential-bearing headers.

Behavioral **DYN_HTTP_OVERLOAD_STATUS_CODE no longer accepts informational (1xx) status codes** ([#12738](https://github.com/ai-dynamo/dynamo/pull/12738)).


Migrate:If`DYN_HTTP_OVERLOAD_STATUS_CODE`

is set to a 1xx value, change it to a final status code in 200-999 (e.g. 503) or rely on the 529 default.

Behavioral **Decode workers no longer suppress KV event publishing** ([#12084](https://github.com/ai-dynamo/dynamo/pull/12084)).


Migrate:To keep KV event publishing off on decode workers, omit —kv-events-config (or disable prefix caching / set enable_kv_cache_events=false) instead of relying on decode mode.

Behavioral ** --tag default changed from single weights tag to all production GMS tags** (


[#11285](https://github.com/ai-dynamo/dynamo/pull/11285)).


Migrate:Pass`--tag weights`

explicitly to`python -m gpu_memory_service`

if you rely on serving only the weights tag/socket.

Behavioral ** --socket-path now requires exactly one --tag** (


[#11285](https://github.com/ai-dynamo/dynamo/pull/11285)).


Migrate:When using`--socket-path`

, also pass a single`--tag <name>`

.

Behavioral **Implicit 1 ms arrival-interval fallback removed from synthetic replay API/CLI** ([#12062](https://github.com/ai-dynamo/dynamo/pull/12062)).


Migrate:Pass one of —request-rate, —arrival-interval-ms, or —replay-concurrency (or the equivalent Python kwarg) when running synthetic replay.

Behavioral **New —trust-remote-code flag (default off) in trtllm mm_router_worker example** ([#10738](https://github.com/ai-dynamo/dynamo/pull/10738)).


Migrate:Pass —trust-remote-code to the trtllm mm_router_worker example when the model requires custom remote code.

Behavioral **Python binding router_queue_threshold default changed to None** ([#11599](https://github.com/ai-dynamo/dynamo/pull/11599)).


Migrate:Pass router_queue_threshold=16.0 explicitly when constructing the router config to keep queueing enabled.

Behavioral **Missing media decoder now raises RuntimeError (MissingMediaDecoderError) instead of ValueError/ImportError** ([#12725](https://github.com/ai-dynamo/dynamo/pull/12725)).


Migrate:Update callers/handlers that catch ValueError (or expect a 4xx client error) for undecodable media to also catch MissingMediaDecoderError/RuntimeError, which now signals a deployment/decoder-configuration failure.

Behavioral **load_vision_model / load_qwen_grid_params signatures gain trust_remote_code param with False default** ([#10738](https://github.com/ai-dynamo/dynamo/pull/10738)).


Migrate:Callers of these multimodal utility functions that rely on remote code must now pass trust_remote_code=True explicitly.

Behavioral **Synthetic WorkloadSpec now requires exactly one arrival controller** ([#12062](https://github.com/ai-dynamo/dynamo/pull/12062)).


Migrate:Update synthetic workload specs to set exactly one of concurrency, requestRate, or arrivalIntervalMs (remove redundant/duplicate arrival controllers).

Behavioral **Chart 1.3.0 requires agent image v1.2.0 or newer** ([#9790](https://github.com/ai-dynamo/dynamo/pull/9790)).


Migrate:Re-pin image.tag (or image.digest) to the v1.2.0 agent image; older images lack managed_state.py and CrashLoop with ModuleNotFoundError.

Behavioral **Unresolved GMS extraClientContainers names now rejected by admission and reconcile** ([#12580](https://github.com/ai-dynamo/dynamo/pull/12580)).


Migrate:Update DynamoGraphDeployment/DynamoComponentDeployment manifests so every experimental.gpuMemoryService.extraClientContainers entry matches a unique container name declared in podTemplate.spec.containers before upgrading the Operator.

Behavioral **C API now requires an explicit endpoint name** ([#11841](https://github.com/ai-dynamo/dynamo/pull/11841)).


Migrate:Update C API callers to pass the endpoint name explicitly instead of relying on the implicit serving endpoint.

Removed **Removed the deprecated vLLM worker role flags** (`--is-prefill-worker`

/ `--is-decode-worker`

-> `--disaggregation-mode`

) ([#12089](https://github.com/ai-dynamo/dynamo/pull/12089)).


Migrate:Pass`--disaggregation-mode prefill`

or`--disaggregation-mode decode`

instead of the removed boolean flags.

Removed **Removed the deprecated multimodal worker flags** (`--multimodal-worker`

/ `--multimodal-encode-worker`

-> `--enable-multimodal`

with `--disaggregation-mode`

/ `--dedicated-mm-encoder`

) across the vLLM, SGLang, and TensorRT-LLM backends; deprecated in v1.3.0 ([#11887](https://github.com/ai-dynamo/dynamo/pull/11887)).


Migrate:On vLLM and SGLang, replace the removed flags with`--enable-multimodal`

plus the appropriate`--disaggregation-mode`

/`--dedicated-mm-encoder`

combination. On TensorRT-LLM, use`--modality multimodal`

, which remains the supported path.

Removed **Removed bundled software video decoders from the runtime images**: H.264/H.265 video inputs decode in hardware via NVDEC ([#11836](https://github.com/ai-dynamo/dynamo/pull/11836)). Other codecs (or H.264/H.265 where NVDEC is unavailable) fail with an actionable error naming the missing package and installer command instead of decoding in software ([#12725](https://github.com/ai-dynamo/dynamo/pull/12725)).


Migrate:Grant containers the`video`

NVIDIA driver capability for H.264/H.265 input, or install software decoders with`python -m dynamo.common.utils.install_media_decoders <vllm|sglang|trtllm>`

.

Removed **Legacy DGDR Compatibility Retirement:** Stopped emitting legacy per-field `nvidia.com/dgdr-*`

annotations during v1alpha1 to v1beta1 conversion, restoring v1alpha1-only profiling fields through typed API conversion instead ([#11531](https://github.com/ai-dynamo/dynamo/pull/11531)). The remaining read-only annotation compatibility layer and its fixtures moved into dedicated files ([#11598](https://github.com/ai-dynamo/dynamo/pull/11598)), and the legacy annotation readers were then removed, so conversion relies exclusively on the structural `nvidia.com/dgdr-spec`

and `nvidia.com/dgdr-status`

payloads ([#11663](https://github.com/ai-dynamo/dynamo/pull/11663)). Reworked worker hashing to converge lazily to v2, computing the v1alpha1 hash only for incomplete migrations and avoiding an Operator-upgrade-induced rollout for unchanged Dynamo 1.2 worker generations ([#11529](https://github.com/ai-dynamo/dynamo/pull/11529)).


Migrate:Read DGDR state from the structural`nvidia.com/dgdr-spec`

and`nvidia.com/dgdr-status`

annotations. The per-field`nvidia.com/dgdr-*`

annotations are no longer emitted.

Removed **Unified Backend Engine Removal:** Removed the experimental per-backend unified backend engine implementations for vLLM, SGLang, and TensorRT-LLM in favor of the sidecar implementation ([#11831](https://github.com/ai-dynamo/dynamo/pull/11831)). The `--unified`

launch flag, the unified serve configs, and the engine-specific tests are gone, while the Python `common/backend`

and Rust `backend-common`

interfaces remain for the sidecar path. The removal was backported to `release/1.4.0`

, preserving the release-specific vLLM and Fern documentation structure and deleting the stale unified-backend docs ([#12862](https://github.com/ai-dynamo/dynamo/pull/12862)).


Migrate:Launch each backend through its standard entry point (`python -m dynamo.vllm`

,`dynamo.sglang`

, or`dynamo.trtllm`

). The`--unified`

flag no longer exists.

Deprecated **Common backend interfaces are no longer a published integration surface**: the Rust `dynamo-backend-common`

crate is not published for v1.4.0 (last published as 1.2.1). The crate and the Python `dynamo.common.backend`

module remain in-tree solely for the in-development sidecar path following the unified backend engine removal ([#11831](https://github.com/ai-dynamo/dynamo/pull/11831)). Treat these interfaces as internal until the sidecar ships.

Deprecated **Go-based EPP and eppConfig deprecated in favor of the Rust-based EPP**: the Rust ext-proc EPP introduced in v1.3.0 (

[#8783](https://github.com/ai-dynamo/dynamo/pull/8783)) replaces the Go Endpoint Picker under

`deploy/inference-gateway/epp`

(built on gateway-api-inference-extension); the default does not change in v1.4.0. **Compatibility:**upgrading the Operator does not force migration. A

`DynamoGraphDeployment`

— existing or newly created — that keeps `eppConfig`

set and its EPP image pinned to the 1.4 release line keeps the exact Go EPP Pod contract (CLI flags, config volume, Service selector) unchanged after an Operator upgrade.Deprecated **Namespace-restricted Operator mode deprecated**: the mode will be removed in a future release, so run the cluster-wide Operator instead. Namespace-restricted installs already depend on the cluster-wide Operator for CRDs (`dynamo-operator.upgradeCRD=false`

).


## v1.3.0 — Jul 20, 2026

24 entries — 14 behavioral changes, 10 deprecated and removed.

Behavioral **CUDA 12 container images removed — CUDA 13 only** (`vLLM and SGLang runtime images shipped CUDA 12.9 and CUDA 13 variants`

-> `CUDA 13 images only`

).


Migrate:Move all deployments to the CUDA 13 runtime images before upgrading — the CUDA 12.9 variants are no longer published. The bare`vllm-runtime`

/`sglang-runtime`

/`tensorrtllm-runtime`

tags now resolve to CUDA 13, with explicit`-cuda13`

aliases on the same digest.

Behavioral **Multimodal now requires an explicit --enable-multimodal flag** (

`--multimodal-worker / --multimodal-encode-worker`

-> `--enable-multimodal (with --dedicated-mm-encoder / --disaggregation-mode)`

); workers without the flag now raise a RuntimeError on multimodal requests instead of silently processing them as text-only ([#10680](https://github.com/ai-dynamo/dynamo/pull/10680)).


Migrate:Add`--enable-multimodal`

(and`--dedicated-mm-encoder`

for internal encode-worker topologies) to both prefill and decode workers so multimodal requests are accepted rather than rejected.

Behavioral ** disaggregation-mode default changed to agg; prefill_and_decode deprecated** (



`--disaggregation-mode default 'prefill_and_decode' (DisaggregationMode.AGGREGATED)`

-> `--disaggregation-mode default 'agg'; 'prefill_and_decode' deprecated, use 'pd'`

) ([#10690](https://github.com/ai-dynamo/dynamo/pull/10690)).


Migrate:Use`--disaggregation-mode agg`

for aggregated serving and`pd`

for combined prefill+decode; legacy`prefill_and_decode`

still works temporarily.

Behavioral **GPU Memory Service (GMS) DRA now requires Kubernetes 1.34+** — GMS attaches GPUs to workers through the Kubernetes Dynamic Resource Allocation (DRA) API, which must now be the stable `resource.k8s.io/v1`

(Kubernetes 1.34+) instead of the older 1.32+ API group; GMS errors if it is unavailable ([#9454](https://github.com/ai-dynamo/dynamo/pull/9454)).


Migrate:Upgrade the cluster to Kubernetes 1.34+ so`resource.k8s.io/v1`

is available before using GMS`ResourceClaimTemplates`

.

Behavioral **GMS now wires GPUs into your declared client containers instead of a sidecar** — setting `enabled`

used to start a GMS sidecar and swap the main container’s GPUs for a DRA ResourceClaim; it now wires GPUs into the client containers you declare, and the operator no longer auto-creates `gms-loader`

/`gms-saver`

containers ([#9641](https://github.com/ai-dynamo/dynamo/pull/9641)).


Migrate:Because the operator no longer injects`gms-loader`

/`gms-saver`

containers automatically, list the containers that should use GMS-managed GPU memory yourself via`extraClientContainers`

(and`checkpoint.job.gmsClientContainers`

for checkpoint jobs).

Behavioral **GMS “shadow mode” is now enabled only with inter-pod failover** — shadow mode runs the GPU Memory Service alongside the live KV path for validation without serving from it; `DYN_VLLM_GMS_SHADOW_MODE=true`

is now injected only when inter-pod failover is on, not for every standalone inter-pod GMS deployment ([#10378](https://github.com/ai-dynamo/dynamo/pull/10378)).


Migrate:If you rely on shadow mode with standalone inter-pod GMS, enable failover (`mode=interPod`

) to restore`DYN_VLLM_GMS_SHADOW_MODE`

injection.

Behavioral **Router backpressure defaults raised** — queue threshold `4.0 -> 16.0`

and active-prefill-tokens threshold fraction `10.0 -> 64.0`

([#9547](https://github.com/ai-dynamo/dynamo/pull/9547)).


Migrate:Explicitly set`--router-queue-threshold=4.0`

and`--active-prefill-tokens-threshold-frac=10.0`

to retain the previous backpressure and prefill busy-detection behavior.

Behavioral **Removed the forced default of --runner generate in vLLM** (

`runner defaults to "generate" when not explicitly set`

-> `runner defaults to vLLM's own value (auto-detection)`

) ([#9710](https://github.com/ai-dynamo/dynamo/pull/9710)).


Migrate:If you relied on the implicit`runner=generate`

default, pass`--runner generate`

explicitly.

Behavioral **Frontend nvext / admin-API master switches renamed to opt-out** (`DYN_ENABLE_FRONTEND_{NVEXT,ADMIN_API}`

-> `DYN_DISABLE_*`

) ([#11123](https://github.com/ai-dynamo/dynamo/pull/11123)).


Migrate:The`nvext`

and frontend admin-API surfaces are now on by default; disable them with`DYN_DISABLE_FRONTEND_NVEXT`

/`DYN_DISABLE_FRONTEND_ADMIN_API`

instead of enabling with`DYN_ENABLE_*`

.

Behavioral **Requests carrying nvext.agent_context are now rejected** — the

`nvext`

OpenAI-API extension no longer accepts the `agent_context`

object (previously used to pass agent/trajectory identity); it is refused as an unknown field ([#10808](https://github.com/ai-dynamo/dynamo/pull/10808)).


Migrate:Stop sending`agent_context`

in`nvext`

; use trajectory identity headers instead.

Behavioral ** spec.restart.id on DGD create no longer triggers a restart (Creating a DynamoGraphDeployment with spec.restart.id triggered an immediate restart -> spec.restart.id on initial creation is treated as already observed and does not trigger a restart)** (



[#10955](https://github.com/ai-dynamo/dynamo/pull/10955)).


Migrate:Create the DGD without`spec.restart`

, then set`spec.restart.id`

after creation to request a restart.

Behavioral **Snapshot Helm chart defaults changed for live worker checkpointing** — Dynamo checkpoints running workers with CRIU (Checkpoint/Restore In Userspace); the chart now defaults TCP socket handling to `tcpClose=false / tcpEstablished=true`

and points the CRIU `libDir`

at `/usr/local/lib/snapshot/criu-plugins`

instead of leaving it empty ([#10727](https://github.com/ai-dynamo/dynamo/pull/10727)).


Migrate:To preserve prior behavior, set`config.tcpClose=true`

,`config.tcpEstablished=false`

, and`config.libDir=""`

explicitly in your snapshot values.

Behavioral **DGD Auto checkpoint identity and status changes** — the DynamoCheckpoint printer column is renamed `Hash -> CheckpointID`

(`.status.identityHash`

-> `.status.checkpointID`

), Auto checkpoints are no longer reused across DGDs via identity hash (now scoped to the owning DGD/component generation), and Manual mode without `checkpointRef`

or `identity`

now fails fast instead of silently waiting ([#10177](https://github.com/ai-dynamo/dynamo/pull/10177)).


Migrate:Read`.status.checkpointID`

(identityHash remains as a deprecated mirror), set`checkpointRef`

to explicitly reuse a named DynamoCheckpoint, and provide`checkpointRef`

or`identity`

when using Manual mode.

Behavioral **Router enforce-disagg deprecated** (

[#11295](https://github.com/ai-dynamo/dynamo/pull/11295)).


Migrate:Remove`enforce-disagg`

from router configuration; disaggregated routing is selected through the standard router modes.

Removed **Removed the standalone dynamo-gaie Helm chart and gateway CRD install script for the inference gateway (EPP)** — the Endpoint Picker (EPP) inference-gateway extension now installs through the operator, so the standalone chart (

`deploy/inference-gateway/standalone/helm/dynamo-gaie`

) and the `install_gaie_crd_kgateway.sh`

script are removed ([#10001](https://github.com/ai-dynamo/dynamo/pull/10001)).


Migrate:Move off the standalone EPP Helm chart to the operator-managed inference gateway path, and use`agentgateway`

CRD installation instead of the removed`kgateway`

install script.

Removed **Removed clear_kv_blocks endpoint and its router function** (

`POST /clear_kv_blocks`

and `pub fn clear_kv_blocks_router`

removed) ([#10556](https://github.com/ai-dynamo/dynamo/pull/10556)).


Migrate:Stop calling the`/clear_kv_blocks`

HTTP endpoint and remove any callers of`clear_kv_blocks_router`

; both the endpoint and the function/module were deleted.

Removed **Removed nvext.agent_context and its session fields** (

`nvext.agent_context`

request-body field removed; `session_type_id`

and `session_id`

removed from AgentContext, leaving trajectory fields only) ([#10808](https://github.com/ai-dynamo/dynamo/pull/10808)).


Migrate:Remove`agent_context`

from request bodies and supply trajectory identity via`x-dynamo-trajectory-id`

/`x-dynamo-parent-trajectory-id`

/`x-dynamo-trajectory-final`

headers; only trajectory fields remain on AgentContext.

Removed **Removed sticky-session routing and its nvext.session_control surface** — session affinity (pinning a conversation’s requests to one worker) is replaced by trajectory-based KV/radix cache tags; this drops

`nvext.session_control`

, the worker session-lifecycle endpoint, and the `StickySessionRouter / InMemoryAffinityStore / AffinityBinding / AffinityKind`

Rust types ([#10214](https://github.com/ai-dynamo/dynamo/pull/10214)).


Migrate:Stop sending`nvext.session_control`

and migrate to trajectory-based radix cache tags; sticky routing, the worker lifecycle RPC, and the sticky routing types are no longer available.

Removed **Removed DYN_AGENT_TRACE in favor of DYN_REQUEST_TRACE** (


`DYN_AGENT_TRACE`

-> `DYN_REQUEST_TRACE`

) ([#10701](https://github.com/ai-dynamo/dynamo/pull/10701)).


Migrate:Set`DYN_REQUEST_TRACE=1`

instead of`DYN_AGENT_TRACE`

; agent-context enrichment now emits under the unified request-trace path.

Removed **vLLM ModelExpress weight loading moved behind a single --load-format modelexpress** — ModelExpress streams model weights to workers for faster startup; the split

`mx-source`

/`mx-target`

load formats and the `--model-express-url`

/ `MODEL_EXPRESS_URL`

setting are removed in favor of the plugin-owned `--load-format modelexpress`

([#10049](https://github.com/ai-dynamo/dynamo/pull/10049)).


Migrate:Switch vLLM deployments to`--load-format modelexpress`

and rely on the ModelExpress vLLM plugin; stop relying on`--model-express-url`

/`MODEL_EXPRESS_URL`

.

Removed **Removed the diffusion-transformer data-parallel flag --dit-dp-size** — this TensorRT-LLM knob set the data-parallel degree for the DiT (Diffusion Transformer) image/video path; the flag and its

`DYN_TRTLLM_DIT_DP_SIZE`

env var are gone ([#10036](https://github.com/ai-dynamo/dynamo/pull/10036)).


Migrate:Remove`--dit-dp-size`

and`DYN_TRTLLM_DIT_DP_SIZE`

from your diffusion launch configuration.

Deprecated **Deprecated per-backend multimodal flags ( --multimodal-worker / --multimodal-encode-worker / --modality multimodal)** — superseded by a single



`--enable-multimodal`

plus `--disaggregation-mode`

(with `--dedicated-mm-encoder`

for internal encode workers); the old flags still work but emit deprecation warnings ([#10680](https://github.com/ai-dynamo/dynamo/pull/10680),

[#10690](https://github.com/ai-dynamo/dynamo/pull/10690)).


Migrate:Switch to`--enable-multimodal`

plus the appropriate`--disaggregation-mode`

/`--dedicated-mm-encoder`

combination.

Removed **Removed the GMS checkpoint loader/saver override structs** — instead of the built-in


`gpuMemoryService.checkpoint.{loader,saver}`

containers, declare your own GMS client containers via `extraClientContainers`

/ `checkpoint.job.gmsClientContainers`

([#9641](https://github.com/ai-dynamo/dynamo/pull/9641)).


Migrate:Replace the`gpuMemoryService.checkpoint.{loader,saver}`

config with user-declared containers referenced via`extraClientContainers`

/`checkpoint.job.gmsClientContainers`

.

Removed **Fixed the misspelled Planner autoscaling key decode_sacle_up_kv_rate** — this SLA-Planner threshold governs when decode workers scale up under KV-cache pressure; the misspelled alias is removed in favor of the correct

`decode_scale_up_kv_rate`

([#10601](https://github.com/ai-dynamo/dynamo/pull/10601)).


Migrate:Update any configuration using the misspelled`decode_sacle_up_kv_rate`

key to the correct`decode_scale_up_kv_rate`

.


###### v1.2.0 — 5 entries + carryover reminders


**ACTION REQUIRED:** The following changes require updates to your code, configuration, or deployment manifests before upgrading.

Behavioral **DGD/DGDR Promoted to v1beta1 as the Served API** (

[#9235](https://github.com/ai-dynamo/dynamo/pull/9235),

[#9262](https://github.com/ai-dynamo/dynamo/pull/9262)): The

`DynamoGraphDeployment`

, `DynamoComponentDeployment`

, and `DynamoGraphDeploymentRequest`

APIs now serve `v1beta1`

. The `v1alpha1`

↔ `v1beta1`

round-trip conversion is maintained for backward compatibility, but all docs and examples have moved to `v1beta1`

.

Migrate:Update Helm values, Argo manifests, and any inline YAML to reference`v1beta1`

. Existing`v1alpha1`

resources continue to work via the conversion path during the transition; remove`v1alpha1`

references at your next deploy.

Behavioral **Duration Config Fields Suffixed with Units** ([#9246](https://github.com/ai-dynamo/dynamo/pull/9246)): Configuration fields representing durations were renamed to make their units explicit (e.g., `*_ttl`

→ `*_ttl_secs`

).


Migrate:Audit your deployment YAMLs and CLI invocations for any duration field; the new suffix-bearing names are required. The previous unsuffixed names are no longer recognized.

Behavioral **Concurrent Radix Tree is the Default Approximate Router** ([#9219](https://github.com/ai-dynamo/dynamo/pull/9219), [#9007](https://github.com/ai-dynamo/dynamo/pull/9007)): The default approximate KV routing backend switched to the concurrent radix tree with anchor-aware branch sharding.


Migrate:Update any custom router instrumentation that targeted the previous radix-tree internals. No action required for default deployments; routing semantics are equivalent.

Behavioral **Inter-Pod GPU Memory Service Sidecar Model** ([#7777](https://github.com/ai-dynamo/dynamo/pull/7777), [#8829](https://github.com/ai-dynamo/dynamo/pull/8829)): GMS moves to an inter-pod sidecar that multiple workers can share. The Operator gates GMS+Snapshot combinations via Helm config.


Migrate:If you ran the v1.1.0 per-pod GMS deployment pattern, switch to the new shared-sidecar Helm values. The previous topology continues to work but is no longer the recommended path.

Deprecated **CUDA 12 Containers Discontinued in v1.3.0:** v1.2.0 is the last release to publish CUDA 12 container images. Starting with v1.3.0, Dynamo will ship CUDA 13 images only. In v1.2.0 the vLLM and SGLang containers ship both CUDA 12.9 and CUDA 13.0 variants, while TensorRT-LLM is already CUDA 13 only.


Migrate:Move CUDA 12 deployments to the CUDA 13 container variants before upgrading to v1.3.0.

Deprecated The following warnings from v1.1.0 still apply. Migrate before they are removed:

`v1alpha1`

DGDR API: now in active conversion to`v1beta1`

(see above)`enableGpuDiscovery`

CRD field has no effect`ComponentName`

field on`ServiceReplicaStatus`

: migrate to`ComponentNames`

- Router CLI flags without the
`--router-`

prefix - vLLM
`--is-prefill-worker`

/`--is-decode-worker`

: migrate to`--disaggregation-mode`

`--router-durable-kv-events`

: migrate to the event-plane subscriber


###### v1.1.0 — 8 entries + carryover reminders


**ACTION REQUIRED:** The following changes require updates to your code, configuration, or deployment manifests before upgrading.

Behavioral ** enable_nats and use_kv_events Removed from DistributedRuntime** (



[#7265](https://github.com/ai-dynamo/dynamo/pull/7265)): Both parameters are removed from

`DistributedRuntime`

, `create_runtime()`

, and the `dynamo_worker()`

decorator. NATS is now auto-detected from the event plane: enabled when the request plane is NATS or `NATS_SERVER`

is configured.

Migrate:Drop both arguments from your Python entry points and configure NATS via the`DYN_EVENT_PLANE`

and`NATS_SERVER`

environment variables instead.

Behavioral **Experimental nvext.cache_control Cache Pinning Removed** (

[#7790](https://github.com/ai-dynamo/dynamo/pull/7790)): The experimental cache-pinning feature is removed: the

`nvext.cache_control`

request field, the `--enable-cache-control`

flag, and the `DYN_ENABLE_CACHE_CONTROL`

env var are all gone. SGLang upstream chose a different direction, so the v1.0.0 plumbing is being unwound. The Anthropic Messages parser still accepts `cache_control`

blocks for protocol compatibility but no longer derives router-pin TTLs from them.

Migrate:If you depended on cache pinning, track the v1.2.0 sticky-session / session-controller work. There is no drop-in replacement in v1.1.0.

Behavioral **Cargo-Built dynamo-kv-indexer Binary Removed** (

[#7338](https://github.com/ai-dynamo/dynamo/pull/7338)): The Cargo-built

`dynamo-kv-indexer`

binary in `lib/kv-router/target/release/`

is removed; the maturin-built binary shipped via the Python wheel is now the single source.

Migrate:Update launchers and Dockerfiles to point at the wheel-installed`dynamo-kv-indexer`

(on`PATH`

after`pip install ai-dynamo`

).

Behavioral **LLaVA-Specific EPD Path Removed; EPD Now Single-GPU** ([#6674](https://github.com/ai-dynamo/dynamo/pull/6674)): The LLaVA-specific multimodal EPD code path is removed, EPD is now constrained to single-GPU configurations, and the default multimodal example moved from `Llava-Mistral`

to `Qwen/Qwen3-VL-2B-Instruct`

.


Migrate:Switch LLaVA workloads to the aggregated path or to a Qwen3-VL recipe.

Behavioral **Compressed Concurrent Tree Default** ([#7874](https://github.com/ai-dynamo/dynamo/pull/7874)): The KV router defaults to the compressed concurrent radix tree. Improves resource utilization for multi-threaded indexing; node-allocation semantics differ from the previous tree.


Migrate:Update any custom instrumentation that targeted the old radix-tree internals. No action required for default deployments.

Behavioral **MDC Checksum Scoped Per-WorkerSet** ([#7368](https://github.com/ai-dynamo/dynamo/pull/7368)): Model Discovery Card checksum validation moved from per-Model to per-WorkerSet. Different WorkerSets under the same Model can now carry different configuration without forcing workers to drain first.


Migrate:If you relied on the v1.0.0 strict per-Model behavior, audit your WorkerSet configs before upgrading.

Removed **vLLM Auto-Enable KV Events Removed** ([#7591](https://github.com/ai-dynamo/dynamo/pull/7591)): The deprecated automatic KV-events config in vLLM is removed; the `DYN_VLLM_KV_EVENT_PORT`

env var is also no longer supported.


Migrate:Set`--kv-events-config`

explicitly per the v1.0.0 migration note.

Removed **Unused genai-perf Pin Dropped** (

[#8763](https://github.com/ai-dynamo/dynamo/pull/8763)): The unused

`genai-perf==0.0.15`

pin was removed from `container/deps/requirements.benchmark.txt`

. It was not invoked anywhere in the repo.

Migrate:No action required.`aiperf`

is the supported in-container benchmarking tool.

Deprecated The following warnings from v1.0.0 still apply. Migrate before they are removed:

`v1alpha1`

DGDR API: migrate to`v1beta1`

`enableGpuDiscovery`

CRD field has no effect`ComponentName`

field on`ServiceReplicaStatus`

: migrate to`ComponentNames`

- Router CLI flags without the
`--router-`

prefix - vLLM
`--is-prefill-worker`

/`--is-decode-worker`

: migrate to`--disaggregation-mode`

`--router-durable-kv-events`

: migrate to the event-plane subscriber


###### v1.0.0 — 41 entries


**ACTION REQUIRED:** The following changes require updates to your code, configuration, or deployment manifests before upgrading.

Removed **KV Router Flags Renamed** ([#6361](https://github.com/ai-dynamo/dynamo/pull/6361)): All KV router CLI flags and env vars now use the `--router-`

* / `DYN_ROUTER_`

* prefix.


Migrate:Update all CLI invocations, env vars, and deployment YAMLs to use the new names.

Removed **Disagg Flag Inverted** ([#6515](https://github.com/ai-dynamo/dynamo/pull/6515)): `--enforce-disagg`

replaced by `--decode-fallback`

with inverted semantics — disaggregated mode is now enforced by default.


Migrate:Replace`--enforce-disagg`

with`--decode-fallback`

. If you need fallback to aggregated mode, explicitly pass`--decode-fallback`

or`DYN_DECODE_FALLBACK=true`

. In the EPP plugin, update from`DYN_ENFORCE_DISAGG`

to`DYN_DECODE_FALLBACK`

with inverted boolean.

Removed **Migration Limit Moved to Frontend** ([#5918](https://github.com/ai-dynamo/dynamo/pull/5918)): The `--migration-limit`

CLI flag has been removed from all backend workers (vLLM, SGLang, TRT-LLM) and is now set on the Frontend only.


Migrate:Remove`--migration-limit`

from backend launch commands; pass it to the Frontend instead.

Removed **Connector Flag Replaced** ([#6450](https://github.com/ai-dynamo/dynamo/pull/6450)): The `--connector`

flag is removed. Disaggregated prefill workers now require explicit `--kv-transfer-config`

with a JSON value.


Migrate:Replace`--connector nixl`

with`--kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both"}'`

. Update all deployment YAMLs and launch scripts accordingly.

Behavioral **KV Events Now Opt-In** ([#6404](https://github.com/ai-dynamo/dynamo/pull/6404)): KV cache events are no longer auto-created when prefix caching is enabled. Users must explicitly opt in via `--kv-events-config`

.


Migrate:Add`--kv-events-config '{"publisher":"zmq","endpoint":"tcp://*:20080","enable_kv_cache_events":true}'`

to worker launch commands. Replace`DYN_VLLM_KV_EVENT_PORT`

env var with the CLI flag.

Behavioral **Local Indexer Now Default** ([#5941](https://github.com/ai-dynamo/dynamo/pull/5941), [#6073](https://github.com/ai-dynamo/dynamo/pull/6073)): Default event transport changed from JetStream to NATS Core/Event Plane with Local Indexer. The `--enable-local-indexer`

flag is removed.


Migrate:If you relied on JetStream persistence, add`--durable-kv-events`

on both frontend and all workers. Remove any`--enable-local-indexer`

flags.

Removed **Omni Flags Prefixed** ([#6476](https://github.com/ai-dynamo/dynamo/pull/6476)): 14 diffusion/omni CLI flags renamed with `--omni-`

prefix (e.g., `--enforce-eager`

→ `--omni-enforce-eager`

).


Migrate:Update CLI invocations to use the`--omni-`

prefixed names.

Removed **Multimodal Worker Flag Removed** ([#6060](https://github.com/ai-dynamo/dynamo/pull/6060)): `--multimodal-encode-prefill-worker`

removed from vLLM backend.


Migrate:Use`--multimodal-encode-worker`

,`--multimodal-worker`

, or`--multimodal-decode-worker`

instead.

Behavioral **Output Modalities Required** ([#6270](https://github.com/ai-dynamo/dynamo/pull/6270)): vLLM omni mode no longer auto-registers image endpoints; you must pass `--output-modalities image`

explicitly.

Removed **Media URL Flags Unified** ([#6391](https://github.com/ai-dynamo/dynamo/pull/6391)): SGLang/TRT-LLM flags `--image-diffusion-fs-url`

, `--video-generation-fs-url`

, and `--output-dir`

replaced by `--media-fs-url`

and `--media-base-url`

.

Removed **Discovery Backend Simplified** ([#6167](https://github.com/ai-dynamo/dynamo/pull/6167)): `DYN_DISCOVERY_BACKEND`

now accepts `kubernetes`

, `etcd`

, `file`

, `mem`

directly. Remove `DYN_KV_STORE`

; replace `--store-kv`

with `--discovery-backend`

.

Removed **Planner CLI Replaced by Config File** ([#6356](https://github.com/ai-dynamo/dynamo/pull/6356)): All individual Planner CLI flags removed in favor of `--config <path>`

pointing to a JSON/YAML configuration file.

Removed **dynamo-run Removed** ([#6203](https://github.com/ai-dynamo/dynamo/pull/6203)): The `dynamo-run`

CLI tool and all its flags have been removed. Migrate to the Python-based deployment approach.

Removed **Env Var Renames** ([#6358](https://github.com/ai-dynamo/dynamo/pull/6358), [#5882](https://github.com/ai-dynamo/dynamo/pull/5882)):

Removed **KVStats Metrics Removed** ([#5704](https://github.com/ai-dynamo/dynamo/pull/5704)): `dynamo_component_kvstats_`

* metrics removed. Use `dynamo_frontend_inter_token_latency_seconds`

for Decode autoscaling instead of `kvstats_gpu_cache_usage_percent`

.

Removed **Router Metrics Namespace** ([#6227](https://github.com/ai-dynamo/dynamo/pull/6227)): `dynamo_frontend_worker_active_`

* → `dynamo_router_worker_active_`

*, `dynamo_component_router_*`

→ `dynamo_router_*`

. New `router_id`

label added to all Router metrics.

Behavioral **Frontend Request Counter Label** ([#5568](https://github.com/ai-dynamo/dynamo/pull/5568)): `dynamo_frontend_requests_total`

now includes an `error_type`

label. Update PromQL queries to account for the new label.

Removed **SGLang Metric Prefix** ([#5701](https://github.com/ai-dynamo/dynamo/pull/5701)): SGLang metrics now use the native `sglang:`

prefix (colon) instead of `sglang_`

(underscore).

Behavioral **etcd Subchart Disabled** ([#6329](https://github.com/ai-dynamo/dynamo/pull/6329)): Bundled etcd is now disabled by default. Set `global.etcd.install: true`

if your deployment depends on it.

Removed **Webhook Key Removed** ([#6441](https://github.com/ai-dynamo/dynamo/pull/6441)): `webhook.enabled`

removed from Helm values. Remove it from custom values files.

Removed **Helm Values Restructured for Snapshot** ([#5946](https://github.com/ai-dynamo/dynamo/pull/5946)): `storage.signalHostPath`

, `daemonset.criu.`

*, and daemonset.containerRuntimeSocket replaced by config.checkpoint.* and


`config.agent.*`

hierarchy.Behavioral **DGDR Planner Schema** ([#6463](https://github.com/ai-dynamo/dynamo/pull/6463)): `FeaturesSpec.planner`

in DGDR CRD changed from a typed `PlannerSpec`

to the PlannerConfig JSON schema. Review DGDR manifests that set `features.planner`

.

Removed **EPP Discovery Timeout** ([#5770](https://github.com/ai-dynamo/dynamo/pull/5770)): `DYN_DISCOVERY_TIMEOUT_SEC`

no longer works. Use StartupProbe `failureThreshold`

× `periodSeconds`

instead.

Removed **Component/Namespace/CancellationToken Removed** ([#6403](https://github.com/ai-dynamo/dynamo/pull/6403), [#6386](https://github.com/ai-dynamo/dynamo/pull/6386), [#6405](https://github.com/ai-dynamo/dynamo/pull/6405)): `Component`

, `Namespace`

, and `CancellationToken`

classes removed from the Python API.

Removed

Migrate:Replace`runtime.namespace('ns').component('comp').endpoint('ep')`

with`runtime.endpoint('ns.comp.ep')`

. Replace`token.cancel()`

with`HttpService.shutdown()`

. Pass`DistributedRuntime`

directly to service`.run()`

methods.

Behavioral **Frontend Config Refactored** ([#6201](https://github.com/ai-dynamo/dynamo/pull/6201)): Frontend CLI now rejects unknown args unless `--chat-processor vllm`

is set.

Behavioral **ModelManager Checksum Enforcement** ([#6054](https://github.com/ai-dynamo/dynamo/pull/6054)): Mismatched MDC checksums across WorkerSets now raise `ChecksumMismatch`

instead of being silently accepted.

Behavioral **Tool Call Parser Separation** ([#5849](https://github.com/ai-dynamo/dynamo/pull/5849)): `--tool-call-parser`

alone no longer uses Dynamo’s parser. Use `--dyn-tool-call-parser`

for Dynamo’s pipeline.

Behavioral **Custom Backend Metrics Removed** ([#5893](https://github.com/ai-dynamo/dynamo/pull/5893)): `custom_backend_metrics_endpoint`

and `custom_backend_metrics_polling_interval`

removed from `LocalModel`

and frontend config.

Removed **Deprecated Component Removals:** Removed dynamo-run and mistral-rs engine (#6203), standalone FastAPI Router (#5845), media-nixl feature (#5940), and llava-hf recipes (#6961).

Behavioral **Local Indexers On By Default** ([#5941](https://github.com/ai-dynamo/dynamo/pull/5941)): KV event transport now defaults to NATS Core/Event Plane with Local Indexer instead of JetStream. Pass `--durable-kv-events`

on both frontend and workers to restore JetStream behavior.

Behavioral **GPU Memory Utilization** ([#5755](https://github.com/ai-dynamo/dynamo/pull/5755)): `gpu-memory-utilization`

adjusted for vLLM runtime to improve out-of-the-box performance.

Behavioral **Operator Env Vars Documented** ([#6548](https://github.com/ai-dynamo/dynamo/pull/6548)): All environment variables injected by the Operator are now documented.

Deprecated ** dynamo-crds Helm Chart:** The standalone

`dynamo-crds`

Helm chart is deprecated. CRDs are now embedded in the Dynamo Operator image and applied automatically via an init container on the operator Deployment ([#6466](https://github.com/ai-dynamo/dynamo/pull/6466),

[#6780](https://github.com/ai-dynamo/dynamo/pull/6780)). Users should uninstall the

`dynamo-crds`

Helm release; the operator manages CRD lifecycle directly.The following features still work but will be removed in a future release with most targeted to Dynamo v1.1.0.

Deprecated ** v1alpha1 DGDR API** (

[#6352](https://github.com/ai-dynamo/dynamo/pull/6352)): The

`v1alpha1`

DynamoGraphDeploymentRequest API will be removed in a future release. Migrate to `v1beta1`

; automatic conversion maintains backward compatibility during the transition.Deprecated **enableGpuDiscovery CRD Field** ([#6224](https://github.com/ai-dynamo/dynamo/pull/6224)): The `enableGpuDiscovery`

CRD field no longer has any effect and will be removed in a future release. GPU discovery now runs automatically.

Deprecated **ComponentName Field** ([#6110](https://github.com/ai-dynamo/dynamo/pull/6110)): The `ComponentName`

field on `ServiceReplicaStatus`

will be removed in a future release. Migrate to the new `ComponentNames`

list field.

Deprecated **Router Legacy Flag Names** ([#6346](https://github.com/ai-dynamo/dynamo/pull/6346)): Router CLI flags without the `--router-`

prefix (e.g., `--block-size`

, `--kv-events`

) will be removed in a future release. Migrate to the prefixed versions (`--router-block-size`

, `--router-kv-events`

).

Deprecated **vLLM KV Auto-Enable** ([#6404](https://github.com/ai-dynamo/dynamo/pull/6404)): vLLM’s auto-enabling of KV events when prefix caching is active will be removed in a future release. Use `--kv-events-config`

explicitly instead.

Deprecated **Prefill/Decode Worker Flags** ([#6483](https://github.com/ai-dynamo/dynamo/pull/6483)): The `--is-prefill-worker`

and `--is-decode-worker`

boolean flags for the vLLM backend will be removed in a future release. Migrate to `--disaggregation-mode`

.

Deprecated **Durable KV Events** ([#6477](https://github.com/ai-dynamo/dynamo/pull/6477)): The `--router-durable-kv-events`

CLI flag will be removed in a future release. Migrate to the event-plane subscriber (local_indexer mode).