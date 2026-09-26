source: https://docs.nvidia.com/deploy/mps/mpsv3-configuration-file.html

# MPS v3 Configuration File[#](https://docs.nvidia.com#mps-v3-configuration-file)

MPS v3 can load its full startup configuration from a TOML file with `-a`

/`--apply`

:

```
nvidia-cuda-mps-control -d -p 3 -a /path/to/config.toml
```

Configuration is applied once at startup; there is currently no persistence of subsequent CLI changes back to disk, so servers, namespaces, and partitions created after startup only exist for the lifetime of the daemon unless they are also added to the configuration file.

```
schema_version = "1.0"
[servers.training]
allowed_devices = "GPU-abcd-1234,GPU-efgh-5678"
pinned_memory_limit = "10G"
active_thread_percentage = "50"
client_priority = "0"
uid = 1000
locality_domains = false
[servers.training.namespaces.high_priority]
pinned_memory_limit = "5G"
active_thread_percentage = "25"
[[servers.training.devices]]
uuid = "GPU-74d43ed3-cdf7-e667-3644-bf5b4f46ed65"
[[servers.training.devices.sm_partitions]]
name = "large"
chunks = 4
include_remainder = false
[features.memacct]
enabled = true
audit_log = true
[features.context-share]
enabled = true
default_socket = "on"
```

`[servers.<name>]`

accepts`allowed_devices`

,`pinned_memory_limit`

,`active_thread_percentage`

,`client_priority`

,`uid`

, and`locality_domains`

(boolean only). Any other key is a configuration error.`[servers.<name>.namespaces.<name>]`

accepts only`pinned_memory_limit`

,`active_thread_percentage`

, and`client_priority`

. A namespace named`default`

refers to the server’s built-in default namespace rather than creating a new one. Refer to[MPS v3 Namespaces](https://docs.nvidia.com/mpsv3-namespaces.html#mpsv3-namespaces)for the equivalent CLI commands.`[[servers.<name>.devices]]`

requires`uuid`

and optionally nests`[[servers.<name>.devices.sm_partitions]]`

entries, each requiring`name`

and`chunks`

, with optional`include_remainder`

(default`false`

).`[features.<name>]`

tables are read per-feature; see the Features section in[MPS v3 Interface](https://docs.nvidia.com/mpsv3-interface.html#mpsv3-interface)for the keys each feature accepts.TOML keys use underscores; the equivalent CLI flags use dashes (for example,

`pinned_memory_limit`

in the file corresponds to`--pinned-memory-limit`

on the command line).