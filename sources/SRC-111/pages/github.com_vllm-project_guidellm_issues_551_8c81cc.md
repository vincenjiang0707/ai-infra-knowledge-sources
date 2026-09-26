source: https://github.com/vllm-project/guidellm/issues/551

**Is your feature request related to a problem? Please describe.**

I'm trying to extend `guidellm`

with a custom backend, formatters, and response handlers for an internal benchmarking use case. The goal is to use the client with a FastAPI-based server, that has a different contract from your typical OpenAI-based service.

While I've managed to make it work, the current approach requires several workarounds that feel unecessary and fragile. I'd like to understand the recommended way to extend guidellm with my custom components. If there is no such a pathway existing, I'd like to start a conversation to add this feature.

Having read the codebase and documentation (especially relevant here is [https://github.com/vllm-project/guidellm/blob/main/docs/guides/backends.md](https://github.com/vllm-project/guidellm/blob/main/docs/guides/backends.md)), I have the feeling that the support for adding custom backends is still WiP.

**Describe the solution you'd like**

It is evident from the codebase, as well as expected from my experience working with your tools (🍷 ), that the `RegistryMixin`

is very much the pattern, that should be utilized to register custom components. And it works well:

from guidellm.backends.backend import Backend
@Backend.register("my_custom_backend")
class MyCustomBackend(Backend):
def __init__(self, target: str, ...):
super().__init__(type_="my_custom_backend")
# ...

Similarly for formatters and response handlers:

@PreprocessorRegistry.register("my_custom_backend")
class MyCustomRequestFormatter(GenerativeTextCompletionsRequestFormatter):
# ...
@GenerationResponseHandlerFactory.register("my_custom_backend")
class MyCustomResponseHandler(TextCompletionsResponseHandler):
# ...

However, it feels that I cannot find an elegant way to make use of the registry pathway.

The CLI uses `click.Choice(list(get_literal_vals(BackendType)))`

to validate the `--backend`

flag. This extracts allowed values from the `Literal`

type annotation at parse time, *before* checking the runtime registry.

**Describe alternatives you've considered**

As a workaround I have to monkey-patch the type annotations before importing guidellm's CLI:

from typing import Literal, Union
import guidellm.backends as _backends_module
# Patch BackendType to include my custom backend
_NewBackendType = Union[_backends_module.BackendType, Literal["my_custom_backend"]]
_backends_module.BackendType = _NewBackendType

The same is needed for `GenerativeRequestType`

(patching both `guidellm.schemas`

and `guidellm.schemas.request`

).

Since guidellm doesn't have a plugin loading mechanism, I need a wrapper script that imports my patches before running guidellm:

# my_guidellm.py
import my_extension.guidellm_patches # patches + registrations
import runpy
def main():
runpy.run_module("guidellm", run_name="__main__")

**Questions / Feature Requests**

-
What is the recommended way to add custom backends?

-
Could the CLI accept perhaps any registered backend name and validate it later?

-
Would you consider adding a plugin loading mechanism? For example: `GUIDELLM_PLUGINS=my_extension.guidellm`

environment variable

-
Once such feature is in place, let's document it properly!


**Additional context**

- guidellm version: v0.5.0
- Python: 3.10

Is your feature request related to a problem? Please describe.I'm trying to extend

`guidellm`

with a custom backend, formatters, and response handlers for an internal benchmarking use case. The goal is to use the client with a FastAPI-based server, that has a different contract from your typical OpenAI-based service.While I've managed to make it work, the current approach requires several workarounds that feel unecessary and fragile. I'd like to understand the recommended way to extend guidellm with my custom components. If there is no such a pathway existing, I'd like to start a conversation to add this feature.

Having read the codebase and documentation (especially relevant here is https://github.com/vllm-project/guidellm/blob/main/docs/guides/backends.md), I have the feeling that the support for adding custom backends is still WiP.

Describe the solution you'd likeIt is evident from the codebase, as well as expected from my experience working with your tools (🍷 ), that the

`RegistryMixin`

is very much the pattern, that should be utilized to register custom components. And it works well:Similarly for formatters and response handlers:

However, it feels that I cannot find an elegant way to make use of the registry pathway.

The CLI uses

`click.Choice(list(get_literal_vals(BackendType)))`

to validate the`--backend`

flag. This extracts allowed values from the`Literal`

type annotation at parse time,beforechecking the runtime registry.Describe alternatives you've consideredAs a workaround I have to monkey-patch the type annotations before importing guidellm's CLI:

The same is needed for

`GenerativeRequestType`

(patching both`guidellm.schemas`

and`guidellm.schemas.request`

).Since guidellm doesn't have a plugin loading mechanism, I need a wrapper script that imports my patches before running guidellm:

Questions / Feature RequestsWhat is the recommended way to add custom backends?

Could the CLI accept perhaps any registered backend name and validate it later?

Would you consider adding a plugin loading mechanism? For example:

`GUIDELLM_PLUGINS=my_extension.guidellm`

environment variableOnce such feature is in place, let's document it properly!

Additional context