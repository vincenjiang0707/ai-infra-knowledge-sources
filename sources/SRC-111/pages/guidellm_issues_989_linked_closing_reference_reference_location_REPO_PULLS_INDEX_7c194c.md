source: https://github.com/vllm-project/guidellm/issues/989/linked_closing_reference?reference_location=REPO_PULLS_INDEX

## Problem Statement

GuideLLM exposes benchmark results and client-side performance metrics, but it does not emit OpenTelemetry traces for benchmark execution.

This makes it difficult to:

- Correlate a GuideLLM request with spans emitted by an instrumented inference server, proxy, gateway, or model-serving stack.
- Investigate where time is spent across scheduling, transport, inference, and streaming.
- Observe benchmark execution using existing OpenTelemetry-compatible tooling.
- Associate failures and latency outliers with a particular GuideLLM run, benchmark, strategy, or request.

This request is separate from:

## Proposed Solution

Add optional OpenTelemetry tracing instrumentation to GuideLLM.

A possible span hierarchy could be:

- One span for a GuideLLM run.
- One child span for each benchmark or scheduling strategy.
- One client span for each inference request, covering the full request lifecycle, including streamed responses.

Request spans should propagate W3C trace context (`traceparent`

and `tracestate`

) through supported HTTP and WebSocket backends. This would allow an instrumented server to attach its work to the same distributed trace.

Useful span attributes could include:

- GuideLLM run and benchmark IDs.
- Backend kind and target.
- Model name.
- Profile and scheduling strategy.
- Endpoint or operation type.
- Request outcome and error type.
- Input, output, and total token counts.
- Time to first token and total request latency where available.

Prompt and response content should not be recorded by default because it may be sensitive and can produce very large traces.

Configuration should follow standard OpenTelemetry environment variables where practical, including:

`OTEL_SERVICE_NAME`

`OTEL_EXPORTER_OTLP_ENDPOINT`

`OTEL_EXPORTER_OTLP_PROTOCOL`

`OTEL_RESOURCE_ATTRIBUTES`

`OTEL_TRACES_SAMPLER`


Instrumentation should be optional and should not require an OTEL exporter dependency or add meaningful overhead when disabled. An optional dependency group such as `guidellm[otel]`

could provide an OTLP exporter.

Where applicable, span names and attributes should follow the OpenTelemetry HTTP and Generative AI semantic conventions.

## Alternatives Considered

GuideLLM can be run under generic HTTP client auto-instrumentation, but that does not capture GuideLLM-specific concepts such as runs, benchmarks, scheduling strategies, request IDs, token counts, or time to first token.

Users can also correlate GuideLLM output with server traces using timestamps or custom headers, but this requires external tooling and does not establish a standard distributed trace relationship.

## Usage Examples

```bash
export OTEL_SERVICE_NAME=guidellm
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
export OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
guidellm run \
--backend kind=openai_http,target=http://localhost:8000 \
--profile kind=constant \
--data kind=synthetic_text,prompt_tokens=256,output_tokens=128 \
--constraint kind=max_requests,count=100
```

With tracing enabled, GuideLLM would export run, benchmark, and request spans. The outbound requests would carry trace context so compatible serving infrastructure could create connected server-side spans.

## Suggested Acceptance Criteria

- OpenTelemetry tracing can be enabled without application code changes.
- GuideLLM emits spans for runs, benchmarks, and individual inference requests.
- Trace context is propagated through supported network backends.
- Request failures are recorded on the corresponding spans.
- Request spans expose useful metadata and token/timing measurements without recording prompt or response content by default.
- Tracing works with multiprocess benchmark execution.
- GuideLLM behaves as it does today when instrumentation is disabled.
- OTLP exporter dependencies remain optional.
- Documentation includes an example using an OTLP collector.

## Additional Context

Related GuideLLM issues:

Relevant OpenTelemetry specifications:

## Problem Statement

GuideLLM exposes benchmark results and client-side performance metrics, but it does not emit OpenTelemetry traces for benchmark execution.

This makes it difficult to:

This request is separate from:

`/metrics`

endpoint #457, which tracks collecting server-side Prometheus metrics.## Proposed Solution

Add optional OpenTelemetry tracing instrumentation to GuideLLM.

A possible span hierarchy could be:

Request spans should propagate W3C trace context (

`traceparent`

and`tracestate`

) through supported HTTP and WebSocket backends. This would allow an instrumented server to attach its work to the same distributed trace.Useful span attributes could include:

Prompt and response content should not be recorded by default because it may be sensitive and can produce very large traces.

Configuration should follow standard OpenTelemetry environment variables where practical, including:

`OTEL_SERVICE_NAME`

`OTEL_EXPORTER_OTLP_ENDPOINT`

`OTEL_EXPORTER_OTLP_PROTOCOL`

`OTEL_RESOURCE_ATTRIBUTES`

`OTEL_TRACES_SAMPLER`

Instrumentation should be optional and should not require an OTEL exporter dependency or add meaningful overhead when disabled. An optional dependency group such as

`guidellm[otel]`

could provide an OTLP exporter.Where applicable, span names and attributes should follow the OpenTelemetry HTTP and Generative AI semantic conventions.

## Alternatives Considered

GuideLLM can be run under generic HTTP client auto-instrumentation, but that does not capture GuideLLM-specific concepts such as runs, benchmarks, scheduling strategies, request IDs, token counts, or time to first token.

Users can also correlate GuideLLM output with server traces using timestamps or custom headers, but this requires external tooling and does not establish a standard distributed trace relationship.

## Usage Examples

With tracing enabled, GuideLLM would export run, benchmark, and request spans. The outbound requests would carry trace context so compatible serving infrastructure could create connected server-side spans.

## Suggested Acceptance Criteria

## Additional Context

Related GuideLLM issues:

`/metrics`

endpoint #457 — Support direct collection of vLLM metrics from PrometheusRelevant OpenTelemetry specifications: