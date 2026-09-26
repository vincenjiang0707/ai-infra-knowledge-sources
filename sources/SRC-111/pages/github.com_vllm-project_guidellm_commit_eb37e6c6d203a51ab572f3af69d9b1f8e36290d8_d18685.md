source: https://github.com/vllm-project/guidellm/commit/eb37e6c6d203a51ab572f3af69d9b1f8e36290d8

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert

GuideLLM can emit OpenTelemetry spans for benchmark runs, scheduling strategies, and individual inference requests. HTTP requests and WebSocket handshakes propagate the active W3C `traceparent` and `tracestate` context, allowing instrumented model servers and gateways to join the same distributed trace.

4

+

5

+

Tracing is disabled by default and the base installation does not require OpenTelemetry. Install the optional dependencies and configure an OTLP collector:

The OTLP endpoint is the activation signal for GuideLLM's automatic exporter setup. Both `grpc` and `http/protobuf` protocols are supported. Set `OTEL_SDK_DISABLED=true` to explicitly disable tracing.

25

+

26

+

Request spans cover the full streamed response lifecycle and record request IDs, backend and model metadata, outcome, error type, token usage, total request latency, and time to first token when available. GuideLLM never adds prompt or response content to spans.

27

+

28

+

Each worker process initializes tracing from the same environment, so multiprocess benchmarks export request spans without sharing unpickleable SDK objects through the scheduler. As with any high-volume benchmark, use an appropriate sampler and size the collector for the expected span rate.

## 0 commit comments