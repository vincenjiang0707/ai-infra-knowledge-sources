source: https://github.com/open-telemetry/semantic-conventions-genai

Semantic Conventions for Generative AI (GenAI), including spans, metrics, and events for GenAI clients, MCP (Model Context Protocol), and provider-specific conventions (OpenAI, etc.).

This repository extends the
[OpenTelemetry Semantic Conventions](https://github.com/open-telemetry/semantic-conventions)
with GenAI-specific conventions, using
[Weaver](https://github.com/open-telemetry/weaver) to manage dependencies
on the core semantic conventions.

TODO

The human-readable version of the semantic conventions resides in the
[docs](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs) folder. Major parts of these Markdown documents are generated
from the YAML definitions located in the [model](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/model) folder.

Reference implementations and their tooling live under [reference](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/reference).
For the Python reference compliance matrix and per-signal support reports, see
[reference/README.md](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/reference/README.md).
For contribution guidance specific to that project, see
[reference/CONTRIBUTING.md](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/reference/CONTRIBUTING.md).

See [CONTRIBUTING.md](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/CONTRIBUTING.md).