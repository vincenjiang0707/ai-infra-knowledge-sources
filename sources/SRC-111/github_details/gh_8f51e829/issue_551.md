# [Issue #551] Documentation and Extension Points for Custom Backends

source: https://github.com/vllm-project/guidellm/issues/551
state: open | updated: 2026-06-08T16:47:55Z
labels: priority-low

## 正文

**Is your feature request related to a problem? Please describe.**

I'm trying to extend `guidellm` with a custom backend, formatters, and response handlers for an internal benchmarking use case. The goal is to use the client with a FastAPI-based server, that has a different contract from your typical OpenAI-based service.

While I've managed to make it work, the current approach requires several workarounds that feel unecessary and fragile. I'd like to understand the recommended way to extend guidellm with my custom components. If there is no such a pathway existing, I'd like to start a conversation to add this feature.

Having read the codebase and documentation (especially relevant here is https://github.com/vllm-project/guidellm/blob/main/docs/guides/backends.md), I have the feeling that the support for adding custom backends is still WiP.

**Describe the solution you'd like**

It is evident from the codebase, as well as expected from my experience working with your tools (🍷 ), that the `RegistryMixin` is very much the pattern, that should be utilized to register custom components. And it works well:

```python
from guidellm.backends.backend import Backend

@Backend.register("my_custom_backend")
class MyCustomBackend(Backend):
    def __init__(self, target: str, ...):
        super().__init__(type_="my_custom_backend")
        # ...
```

Similarly for formatters and response handlers:

```python
@PreprocessorRegistry.register("my_custom_backend")
class MyCustomRequestFormatter(GenerativeTextCompletionsRequestFormatter):
    # ...

@GenerationResponseHandlerFactory.register("my_custom_backend")
class MyCustomResponseHandler(TextCompletionsResponseHandler):
    # ...
```

However, it feels that I cannot find an elegant way to make use of the registry pathway.
 The CLI uses `click.Choice(list(get_literal_vals(BackendType)))` to validate the `--backend` flag. This extracts allowed values from the `Literal` type annotation at parse time, *before* checking the runtime registry.

**Describe alternatives you've considered**
As a workaround I have to monkey-patch the type annotations before importing guidellm's CLI:

```python
from typing import Literal, Union
import guidellm.backends as _backends_module

# Patch BackendType to include my custom backend
_NewBackendType = Union[_backends_module.BackendType, Literal["my_custom_backend"]]
_backends_module.BackendType = _NewBackendType
```

The same is needed for `GenerativeRequestType` (patching both `guidellm.schemas` and `guidellm.schemas.request`).

Since guidellm doesn't have a plugin loading mechanism, I need a wrapper script that imports my patches before running guidellm:

```python
# my_guidellm.py
import my_extension.guidellm_patches  # patches + registrations
import runpy

def main():
    runpy.run_module("guidellm", run_name="__main__")
```

**Questions / Feature Requests**

1. What is the recommended way to add custom backends?

2. Could the CLI accept perhaps any registered backend name and validate it later?

3. Would you consider adding a plugin loading mechanism? For example: `GUIDELLM_PLUGINS=my_extension.guidellm` environment variable
   
4. Once such feature is in place, let's document it properly!

**Additional context**
- guidellm version: v0.5.0
- Python: 3.10


## 评论 (3)

### sjmonson · 2026-01-26

We had intended to support this use-case but never really finalized the design. I think your proposal makes sense. If we replace `BackendType` and other similar literals with a runtime check, that will eliminate the need to patch type annotations. For loading plugins, putting a dynamic import helper in `__main__` (after imports and before any calls) should currently be sufficient to populate the registry. The one caveat is we will eventually need to move worker procs from `fork` to `forkserver` (see #559) and some registries (like `Backend`) will need to have the same import steps in code that the workers run.

### dtransposed · 2026-02-18

Hey @sjmonson any rough idea if this will be on your roadmap in the nearest future?

### sjmonson · 2026-02-18

I have dropped it into v0.7.0 for now which is currently targeting June. I'll look into it sooner if I get the chance. Mostly what is blocking this is bandwidth on our side.
