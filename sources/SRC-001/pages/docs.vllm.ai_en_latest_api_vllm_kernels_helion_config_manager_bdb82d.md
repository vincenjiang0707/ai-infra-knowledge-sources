source: https://docs.vllm.ai/en/latest/api/vllm/kernels/helion/config_manager/
lastmod: 2026-09-23

#

`vllm.kernels.helion.config_manager`

[¶](https://docs.vllm.ai#vllm.kernels.helion.config_manager)

Configuration management for Helion kernels.

This module provides centralized configuration file management for Helion custom operations, including naming conventions, directory resolution, and file I/O.

### Config File Structure[¶](https://docs.vllm.ai#vllm.kernels.helion.config_manager--config-file-structure)

Each kernel has a directory: {kernel_name}/ Inside, each GPU platform has its own JSON file: {kernel_name}/{platform}.json

Platform files store config entries as a JSON array::

```
[
{"key": {}, "config": {...}},
{"key": {"intermediate": 2048, "numtokens": 256}, "config": {...}},
...,
]
```


Config keys are `CaseKey`

instances mapping parameter names to values. The default config uses `CaseKey.default()`

.

Classes:

-
–[ConfigManager](https://docs.vllm.ai#vllm.kernels.helion.config_manager.ConfigManager)File-level configuration management for Helion kernels (global singleton).

-
–[ConfigSet](https://docs.vllm.ai#vllm.kernels.helion.config_manager.ConfigSet)In-memory collection of Helion configs with lookup/query capabilities.


##

`ConfigManager`

[¶](https://docs.vllm.ai#vllm.kernels.helion.config_manager.ConfigManager)

File-level configuration management for Helion kernels (global singleton).

Methods:

-
–[reset_instance](https://docs.vllm.ai#vllm.kernels.helion.config_manager.ConfigManager.reset_instance)For testing purposes only.

-
–[save_configs](https://docs.vllm.ai#vllm.kernels.helion.config_manager.ConfigManager.save_configs)Save configs for a kernel/platform, merging with existing.


## Source code in `vllm/kernels/helion/config_manager.py`


|
|

###

`reset_instance()`

`classmethod`

[¶](https://docs.vllm.ai#vllm.kernels.helion.config_manager.ConfigManager.reset_instance)

###

`save_configs(kernel_name, platform, configs)`

[¶](https://docs.vllm.ai#vllm.kernels.helion.config_manager.ConfigManager.save_configs)

Save configs for a kernel/platform, merging with existing.

## Source code in `vllm/kernels/helion/config_manager.py`


##

`ConfigSet`

[¶](https://docs.vllm.ai#vllm.kernels.helion.config_manager.ConfigSet)

In-memory collection of Helion configs with lookup/query capabilities.

Configs are stored keyed by `CaseKey`

. The default config uses `CaseKey.default()`

as its key.

Methods:

-
–[to_config_entries](https://docs.vllm.ai#vllm.kernels.helion.config_manager.ConfigSet.to_config_entries)Serialize to config entries format for JSON output.

-
–[to_dict](https://docs.vllm.ai#vllm.kernels.helion.config_manager.ConfigSet.to_dict)Return configs as a nested dict (platform -> key -> config).


## Source code in `vllm/kernels/helion/config_manager.py`


|
|

###

`to_config_entries()`

[¶](https://docs.vllm.ai#vllm.kernels.helion.config_manager.ConfigSet.to_config_entries)

Serialize to config entries format for JSON output.

## Source code in `vllm/kernels/helion/config_manager.py`


###

`to_dict()`

[¶](https://docs.vllm.ai#vllm.kernels.helion.config_manager.ConfigSet.to_dict)

Return configs as a nested dict (platform -> key -> config).