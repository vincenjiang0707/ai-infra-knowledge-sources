source: https://github.com/vllm-project/guidellm/pull/919

# Add package `disdantic`

to handle Pydantic polymorphic registries - #919

[SkiHatDuckie](https://github.com/SkiHatDuckie)wants to merge 13 commits into

[SkiHatDuckie](https://github.com/SkiHatDuckie) wants to merge 13 commits into

[SkiHatDuckie](https://github.com/SkiHatDuckie)wants to merge 13 commits into

## Conversation

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

…odel with disdantic versions Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>


[dbutenhof](https://github.com/dbutenhof)added

[dependencies](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Adependencies)

[internal](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Ainternal)

[cleanup](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Acleanup)

Jul 9, 2026


**requested changes**

[dbutenhof](https://github.com/dbutenhof)Jul 9, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

Well *that's* interesting. I pulled this an ran a few tests. Something in this (I'm not quite sure what) has broken Sam's discovery-based CLI help code. A normal GuideLLM run works fine, but `guidellm run --help`

generates this less than helpful message:

```
$ uv run guidellm run --help
usage: guidellm [-h] [--disdantic_.project_root Path] [--disdantic_.default_schema_discriminator str] [--disdantic_.registry_auto_discovery bool] [--disdantic_.auto_packages list[str]] [--disdantic_.auto_ignore_modules list[str]]
[--disdantic_.enable_schema_rebuilding bool] [--disdantic_.schema_rebuild_parents bool] [--disdantic_.info_exclude_keys list[str]]
Central configuration store and validation schema for the disdantic package.
This class serves as the single source of truth for runtime configurations,
defining default options and loading overrides dynamically across modules.
It integrates with Pydantic's BaseSettings to enforce type validation,
coercion, and environment prefixing.
Example:
.. code-block:: python
from disdantic.settings import Settings, get_settings
# Initialize a localized settings instance
settings = Settings(default_schema_discriminator="custom_type")
assert settings.default_schema_discriminator == "custom_type"
# Retrieve the global settings singleton instance
global_settings = get_settings()
print(global_settings.project_root)
options:
-h, --help show this help message and exit
--disdantic_.project_root Path
Maps the file system paths and resolves relative configuration files. (default factory: method)
--disdantic_.default_schema_discriminator str
Maps and retrieves model types within Pydantic registries using this key name. (default: model_type)
--disdantic_.registry_auto_discovery bool
Enables automatic scanning and loading of subclasses during registry initialization. (default: False)
--disdantic_.auto_packages list[str]
Configures target package namespaces to scan, enabling dynamic model discovery across submodules. (default factory: list)
--disdantic_.auto_ignore_modules list[str]
Configures submodule import paths to skip, mapping excluded modules during dynamic scanning. (default factory: list)
--disdantic_.enable_schema_rebuilding bool
Enables dynamic rebuilding of validation schemas, triggering Pydantic model schema rebuilds. (default: True)
--disdantic_.schema_rebuild_parents bool
Enables parent propagation, mapping validation schema updates up the subclass MRO hierarchy. (default: True)
--disdantic_.info_exclude_keys list[str]
Maps specific fields to skip and exclude during InfoMixin logging. (default factory: Settings.<lambda>)
```


**reviewed**

[sjmonson](https://github.com/sjmonson)Jul 9, 2026


There was a problem hiding this comment.

I am not really seeing a benefit to this change. Looking at the `disdantic`

package upstream it hasn't really bench touched outside the initial code dump and it doesn't look like anyone else is using it yet. The other project I know of that has this code is [speculators](https://github.com/vllm-project/speculators/blob/73ec09f604f962f22f40859e86a39fd5b6ec1ba3/src/speculators/utils/registry.py) and they still carry the code in-tree.

Not going to block but I think if we do merge (assuming Dave's comment is fixed). We likely want someone from GuideLLM to have maintainer access on that project.

I had much the same thought after looking through the repo. Doesn't necessarily mean it's a bad idea to use a package -- but you've got a good point about maintainer access to disdantic, and that power comes with the implication that we have to be willing to actually maintain our dependencies there given the lack of any real community around it. I'm not convinced that's a good idea. |

|
I'm personally fine with us sitting on this PR just to see if anything changes. As for the issue with --help getting hijacked: I've been doing some debugging and seems to be caused by disdantic's Pydantic |

### This branch has not been deployed

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Adds the disdantic package to supply the functionality for Pydantic subclass registries, dynamic polymorphism unions and automatic model discovery. This replaces multiple Pydantic utility classes that are currently GuideLLM's responsibility to maintain.

The motive for these changes was to assist in making GuideLLM simpler for maintainers and community members to contribute to by offloading functionality that is not necessarily the point of the software to elsewhere.

Many files have been changed, but many of those changes are just the switching around of imports. Files with substantial changes are mentioned in Details.

## Details

pyproject.toml & tests/unit/test_settings.py

`disdantic`

as a dependencyschemas/base.py

`PydanticClassRegistryMixin`

. Replaced with a subclass of the same name which inherits`disdantic.PydanticClassRegistryMixin`

, imported as`BasePydanticClassRegistryMixin`

. Includes a couple methods that portions of GuideLLM expect which disdantic's version currently does not support:`ReloadableBaseModel`

. Replaced with`disdantic.ReloadableBaseModel`

utils/registry.py

`RegistryMixin`

. Replaced with`disdantic.RegistryMixin`

`RegisterT`

and`RegistryObjT`

remain. Although disdantic has equivalents to these, they are not included in`__all__`

which makes me think they're not intended to be public facingtests/unit/schemas/test_base.py & tests/unit/utils/registry.py

benchmark/benchmarker.py

`BenchmarkerMeta`

. This solely exists to avoid a metaclass conflict between`disdantic.SingletonMeta`

and`ABCMeta`

in`Benchmarker`

`Benchmarker`

scheduler/scheduler.py & tests/integration/scheduler/test_scheduler.py & tests/unit/scheduler/test_scheduler.py

`ThreadSafeSingletonMixin`

with`disdantic.SingletonMeta`

in`Scheduler`

`Scheduler`

Removed files:

`disdantic.InfoMixin`

)`disdantic.AutoImporterMixin`

)`disdantic.SingletonMeta`

)Misc

## Test Plan

`uv sync --frozen`

, or some other means to update the local venv`tox`

## Related Issues

## Use of AI

## git log

commit

e9c993fAuthor: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Thu Jul 2 09:24:46 2026 -0400

commit

42fc629Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Thu Jul 2 09:26:01 2026 -0400

commit

7fb7ea0Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Thu Jul 2 09:50:35 2026 -0400

commit

c0cf7a4Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Thu Jul 2 09:56:22 2026 -0400

commit

8118bd6Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Mon Jul 6 14:28:51 2026 -0400

commit

98f5880Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Tue Jul 7 10:39:55 2026 -0400

commit

cad523eAuthor: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Tue Jul 7 15:26:02 2026 -0400

commit

de57e93Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Wed Jul 8 14:32:40 2026 -0400

commit

a758165Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Wed Jul 8 15:05:20 2026 -0400

commit

11f66ffAuthor: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Wed Jul 8 16:30:03 2026 -0400

commit

a14b49fAuthor: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Wed Jul 8 16:42:34 2026 -0400

commit

511699cAuthor: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Thu Jul 9 10:41:49 2026 -0400

Signed-off-by: SkiHatDuckie SkiHatDuckie@gmail.com