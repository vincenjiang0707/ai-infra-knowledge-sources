source: https://docs.vllm.ai/en/latest/examples/observability/opentelemetry/
lastmod: 2026-09-23

# Setup OpenTelemetry POC[¶](https://docs.vllm.ai#setup-opentelemetry-poc)

Source [https://github.com/vllm-project/vllm/tree/main/examples/observability/opentelemetry](https://github.com/vllm-project/vllm/tree/main/examples/observability/opentelemetry).


Note:The core OpenTelemetry packages (`opentelemetry-sdk`

,`opentelemetry-api`

,`opentelemetry-exporter-otlp`

,`opentelemetry-semantic-conventions-ai`

) are bundled with vLLM. Manual installation is not required.

-
Start Jaeger in a docker container:

[# From: https://www.jaegertracing.io/docs/1.57/getting-started/](https://docs.vllm.ai#__codelineno-0-1)[docker run --rm --name jaeger \](https://docs.vllm.ai#__codelineno-0-2)[-e COLLECTOR_ZIPKIN_HOST_PORT=:9411 \](https://docs.vllm.ai#__codelineno-0-3)[-p 6831:6831/udp \](https://docs.vllm.ai#__codelineno-0-4)[-p 6832:6832/udp \](https://docs.vllm.ai#__codelineno-0-5)[-p 5778:5778 \](https://docs.vllm.ai#__codelineno-0-6)[-p 16686:16686 \](https://docs.vllm.ai#__codelineno-0-7)[-p 4317:4317 \](https://docs.vllm.ai#__codelineno-0-8)[-p 4318:4318 \](https://docs.vllm.ai#__codelineno-0-9)[-p 14250:14250 \](https://docs.vllm.ai#__codelineno-0-10)[-p 14268:14268 \](https://docs.vllm.ai#__codelineno-0-11)[-p 14269:14269 \](https://docs.vllm.ai#__codelineno-0-12)[-p 9411:9411 \](https://docs.vllm.ai#__codelineno-0-13)[jaegertracing/all-in-one:1.57](https://docs.vllm.ai#__codelineno-0-14) -
In a new shell, export Jaeger IP:

[export JAEGER_IP=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' jaeger)](https://docs.vllm.ai#__codelineno-1-1)[export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=grpc://$JAEGER_IP:4317](https://docs.vllm.ai#__codelineno-1-2)Then set vLLM's service name for OpenTelemetry, enable insecure connections to Jaeger and run vLLM:

-
In a new shell, send requests with trace context from a dummy client

-
Open Jaeger webui:

[http://localhost:16686/](http://localhost:16686/)In the search pane, select

`vllm-server`

service and hit`Find Traces`

. You should get a list of traces, one for each request. -
Clicking on a trace will show its spans and their tags. In this demo, each trace has 2 spans. One from the dummy client containing the prompt text and one from vLLM containing metadata about the request.


## Exporter Protocol[¶](https://docs.vllm.ai#exporter-protocol)

OpenTelemetry supports either `grpc`

or `http/protobuf`

as the transport protocol for trace data in the exporter. By default, `grpc`

is used. To set `http/protobuf`

as the protocol, configure the `OTEL_EXPORTER_OTLP_TRACES_PROTOCOL`

environment variable as follows:

export OTEL_EXPORTER_OTLP_TRACES_PROTOCOL=http/protobuf
export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=http://$JAEGER_IP:4318/v1/traces
vllm serve facebook/opt-125m --otlp-traces-endpoint="$OTEL_EXPORTER_OTLP_TRACES_ENDPOINT"


## Instrumentation of FastAPI[¶](https://docs.vllm.ai#instrumentation-of-fastapi)

OpenTelemetry allows automatic instrumentation of FastAPI.

-
Install the instrumentation library

-
Run vLLM with

`opentelemetry-instrument`

-
Send a request to vLLM and find its trace in Jaeger. It should contain spans from FastAPI.


## Example materials[¶](https://docs.vllm.ai#example-materials)

## dummy_client.py

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
import requests
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.trace import SpanKind, set_tracer_provider
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator
trace_provider = TracerProvider()
set_tracer_provider(trace_provider)
trace_provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter()))
trace_provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))
tracer = trace_provider.get_tracer("dummy-client")
url = "http://localhost:8000/v1/completions"
with tracer.start_as_current_span("client-span", kind=SpanKind.CLIENT) as span:
prompt = "San Francisco is a"
span.set_attribute("prompt", prompt)
headers = {}
TraceContextTextMapPropagator().inject(headers)
payload = {
"model": "facebook/opt-125m",
"prompt": prompt,
"max_tokens": 10,
"n": 3,
"use_beam_search": "true",
"temperature": 0.0,
# "stream": True,
}
response = requests.post(url, headers=headers, json=payload)