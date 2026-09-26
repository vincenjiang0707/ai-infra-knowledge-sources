source: https://docs.nvidia.com/deploy/mps/mpsv3-interface.html

# MPS v3 Interface[#](https://docs.nvidia.com#mps-v3-interface)

MPS v3 is a new, opt-in control daemon interface that replaces the interactive shell of
[Legacy MPS v2](https://docs.nvidia.com/mpsv2-interface.html#mpsv2-interface) with a scriptable `module verb`

command
syntax, named servers and namespaces, and file-based configuration. All existing Legacy
MPS v2 functionality continues to work unchanged; MPS v3 is selected explicitly per the
instructions below.

## Enabling MPS v3[#](https://docs.nvidia.com#enabling-mps-v3)

MPS v3 is selected by protocol version. Version `2`

is Legacy MPS and remains the
default; version `3`

selects MPS v3.

`-p 3`

or`--protocol 3`

on the`nvidia-cuda-mps-control`

command line.The

`CUDA_MPS_PROTOCOL_VERSION`

environment variable, set to`3`

. If both the flag and the environment variable are set, the environment variable takes precedence.

```
nvidia-cuda-mps-control -d -p 3
```

```
export CUDA_MPS_PROTOCOL_VERSION=3
nvidia-cuda-mps-control -d
```

If an MPS control daemon is already running, any new `nvidia-cuda-mps-control`

invocation automatically follows that daemon’s protocol version, regardless of its own
`-p`

flag or environment variable.

## Control Daemon Options[#](https://docs.nvidia.com#control-daemon-options)

The control daemon accepts the following top-level options:

`-h`

,`--help`

– Print this message.`-d`

,`--daemon`

– Setup the daemon in the background.`-f`

,`--foreground`

– Setup the daemon in the foreground.`-m`

,`--multiuser`

– Enable multiuser mode.`-a`

,`--apply <file>`

– Apply configuration from a TOML file. Refer to[MPS v3 Configuration File](https://docs.nvidia.com/mpsv3-configuration-file.html#mpsv3-configuration-file).`-p`

,`--protocol <2|3>`

– Protocol 2 (legacy, default) or 3.`-q`

,`--quit`

– Quit and stop the control daemon and all running servers.`-v`

,`--version`

– Print the version.

## CLI Command Structure[#](https://docs.nvidia.com#cli-command-structure)

MPS v3 commands follow a common `module verb [arguments]`

syntax:

```
nvidia-cuda-mps-control <module> <verb> [positional-args] [--key=value ...] [--flag ...]
```

**Modules**:`server`

,`namespace`

,`client`

,`device`

,`sm-partition`

,`feature`

,`memacct`

,`context-share`

.Arguments may be positional (up to 3), or given as

`--key=value`

/`key=value`

, or as valueless flags (`--force`

,`--all`

).Memory limit values use unit suffixes:

`4G`

,`512M`

,`1024K`

.Client priority values are

`0`

(normal) or`1`

(below normal).Server and namespace names must be lowercase letters, digits, and underscores only, up to 64 characters.

`<module> help`

or`<module> <verb> help`

prints detailed usage for that module or verb.

### Server[#](https://docs.nvidia.com#server)

A server is a named, independently managed MPS server process. Unlike Legacy MPS v2, where exactly one server can be active per UID, MPS v3 supports multiple concurrently running named servers.

```
nvidia-cuda-mps-control server create <name> [--uid=<n>] [--allowed-devices=<devices>]
[--locality-domains=<true|false>]
nvidia-cuda-mps-control server delete <name> [--force]
nvidia-cuda-mps-control server list [<name>] [--format=<table|csv>[,noheader]]
nvidia-cuda-mps-control server set <name> [--uid=<n>] [--pinned-memory-limit=<limit>]
[--active-thread-percentage=<pct>]
[--locality-domains=<true|false>]
[--client-priority=<priority>]
nvidia-cuda-mps-control server get <name> <field>
```

`create`

– Creates a named server. Either`<name>`

or`--uid=<n>`

must be provided; if`--uid`

is omitted, the server is owned by the connecting user. In multiuser mode, only`--uid=0`

is allowed and`--uid`

otherwise defaults to the connecting user.`--allowed-devices=<devices>`

– Restrict the server to specific GPUs (default: all). Comma-separated GPU IDs or ordinals, for example`GPU-abc123`

or`0,1`

.`--locality-domains=<true|false>`

– Enable or disable locality domains (see[Locality Domains](https://docs.nvidia.com#mpsv3-locality-domains)).`--uid=<n>`

– Owner UID. Required without`<name>`

; optional with`<name>`

.

`delete`

– Deletes a server by name. Without`--force`

, refuses if active clients remain. With`--force`

, terminates active clients first.`list`

– Lists all servers, or a specific server if`<name>`

is given. Output columns:`name`

,`uid`

,`pid`

,`status`

,`pipe-directory`

,`allowed-devices`

,`context-ids`

.`set`

– Sets server-level limits, applied to the server’s`default`

namespace. At least one option flag is required.`--pinned-memory-limit=<limit>`

– Pinned memory limit.`--active-thread-percentage=<pct>`

– Active thread percentage, 1-100.`--locality-domains=<true|false>`

– Enable or disable locality domains.`--client-priority=<priority>`

– Client priority.

`get`

– Gets a single, unformatted field value from a server. Fields:`name`

,`uid`

,`pid`

,`status`

,`pipe-directory`

,`allowed-devices`

.

```
$ nvidia-cuda-mps-control server create training --allowed-devices=GPU-abcd-1234,GPU-efgh-5678 --uid=1000
$ nvidia-cuda-mps-control server set training --pinned-memory-limit=8G
$ nvidia-cuda-mps-control server list --format=csv,noheader
training,1000,48201,Ready,/run/nvidia-mps/training,GPU-abcd-1234,-
$ nvidia-cuda-mps-control server get training pipe-directory
/run/nvidia-mps/training
$ nvidia-cuda-mps-control server delete training --force
```

### Namespace[#](https://docs.nvidia.com#namespace)

A namespace subdivides a server’s resources for a group of clients. Every server has an
implicit `default`

namespace. Refer to [MPS v3 Namespaces](https://docs.nvidia.com/mpsv3-namespaces.html#mpsv3-namespaces) for more about what
namespaces are for.

```
nvidia-cuda-mps-control namespace create <name> --server=<s>
nvidia-cuda-mps-control namespace delete <name> --server=<s> [--force]
nvidia-cuda-mps-control namespace list [<name>] [--server=<s>]
[--format=<table|csv>[,noheader]]
nvidia-cuda-mps-control namespace set <name> --server=<s> [--pinned-memory-limit=<limit>]
[--active-thread-percentage=<pct>]
[--client-priority=<priority>]
nvidia-cuda-mps-control namespace get <name> <server> <field>
```

`create`

– Creates a namespace under the given server.`delete`

– Deletes a namespace.`--force`

allows deletion even with active clients.`list`

– Lists namespaces. Output columns:`name`

,`server`

,`server-status`

,`pinned-memory-limit`

,`active-thread-percentage`

,`client-priority`

,`pipe-directory`

.`set`

– Sets namespace limits. At least one option flag is required.`get`

– Gets a single field value from a namespace. Fields:`name`

,`server`

,`server-status`

,`pipe-directory`

,`pinned-memory-limit`

,`active-thread-percentage`

,`client-priority`

.

```
$ nvidia-cuda-mps-control namespace create high_priority --server=training
$ nvidia-cuda-mps-control namespace set high_priority --server=training --pinned-memory-limit=4G
$ nvidia-cuda-mps-control namespace get high_priority training pinned-memory-limit
4G
$ nvidia-cuda-mps-control namespace delete high_priority --server=training
```

### Client[#](https://docs.nvidia.com#client)

```
nvidia-cuda-mps-control client list [--server=<s>] [--all] [--format=<table|csv>[,noheader]]
nvidia-cuda-mps-control client get <pid> <field>
nvidia-cuda-mps-control client terminate <pid>
```

`list`

– Lists active clients connected to servers, along with namespace and device information.`--all`

includes clients from all servers;`--server=<s>`

filters to one server.`get`

– Gets a single field value for a client. Fields:`pid`

,`server`

,`device`

,`pci-id`

,`linux-ns`

,`maws-ns`

,`cmd`

.`terminate`

– Terminates a client by PID.

```
$ nvidia-cuda-mps-control client list --server=training --format=csv,noheader
51023,training,0,default,python train.py
51087,training,0,high_priority,python eval.py
$ nvidia-cuda-mps-control client terminate 51023
```

### Device[#](https://docs.nvidia.com#device)

#### list[#](https://docs.nvidia.com#list)

```
nvidia-cuda-mps-control device list [--server=<s>] [--format=<table|csv>[,noheader]]
```

Enumerates devices. `--server=<s>`

scopes the view to one server’s device
enumeration (default: all servers). Output columns: `Ordinal`

, `Server`

,
`PCI ID`

, `Device UUID`

, `Name`

, `Total SMs`

, `Total Chunks`

,
`Attributes`

.

## SM Partitions[#](https://docs.nvidia.com#sm-partitions)

Static SM partitioning in MPS v3 works the same way conceptually as
[Legacy MPS v2 static SM partitioning](https://docs.nvidia.com/when-to-use-mps.html#static-sm-partitioning), using the
`sm-partition`

module instead of the interactive `sm_partition`

command.

Note

The partition ID (the `CUDA_MPS_SM_PARTITION`

value) is encoded differently in
MPS v3 than in Legacy MPS v2, so a partition ID generated by one is not valid in the
other. Always use the ID reported by the version of MPS you are running.

```
nvidia-cuda-mps-control sm-partition create <name> --server=<s> --device=<device>
--chunks=<n> [--include-remainder=<true|false>]
nvidia-cuda-mps-control sm-partition delete <name> --server=<s> --device=<device>
nvidia-cuda-mps-control sm-partition list [--server=<s>] [--device=<device>] [--all]
[--format=<table|csv>[,noheader]]
```

`create`

– Creates an SM partition.`--device`

accepts either a device ordinal or a GPU/MIG UUID.`--chunks`

must be a positive integer.`--include-remainder`

defaults to`false`

. If the target server is not yet running, the partition is recorded and applied the next time the server starts. If the server is already running, the partition is created immediately and its assigned ID is printed.`delete`

– Deletes an SM partition.`list`

– Lists SM partitions. Output columns:`server`

,`device`

,`name`

,`chunks`

,`sm-count`

,`include-remainder`

,`status`

,`visible-uuid`

. A partition’s`status`

is`configured`

if it has been recorded but not yet applied to a running server, or`created`

once it has been carved on the live GPU. Devices with unclaimed capacity also show a synthetic row with status`unallocated`

.

```
$ nvidia-cuda-mps-control sm-partition create large --server=training --device=GPU-74d43ed3-cdf7-e667-3644-bf5b4f46ed65 --chunks=4
SM partition 'large' created on device GPU-74d43ed3-cdf7-e667-3644-bf5b4f46ed65 (sm-count=34)
CUDA_MPS_SM_PARTITION=GPU-74d43ed3-cdf7-e667-3644-bf5b4f46ed65/Kp8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
$ nvidia-cuda-mps-control sm-partition list --server=training --all
SERVER DEVICE NAME CHUNKS SM-COUNT INCLUDE-REMAINDER STATUS VISIBLE-UUID
training GPU-74d43ed3-cdf7-e667-3644-bf5b4f46ed65 large 4 34 false created Kp8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
training GPU-74d43ed3-cdf7-e667-3644-bf5b4f46ed65 - 1 8 - unallocated -
$ nvidia-cuda-mps-control sm-partition delete large --server=training --device=GPU-74d43ed3-cdf7-e667-3644-bf5b4f46ed65
SM partition 'large' deleted from device GPU-74d43ed3-cdf7-e667-3644-bf5b4f46ed65
```

Static partitioning is rejected if the target device already has active clients, if locality domains are enabled on the server (the two features are mutually exclusive), or if the device does not have enough free chunks remaining.

## Locality Domains[#](https://docs.nvidia.com#locality-domains)

Locality domains are the MPS v3 name for the feature formerly called MLOPart in Legacy
MPS v2. Refer to [Locality Domains](https://docs.nvidia.com/when-to-use-mps.html#memory-locality-optimized-partitions) for a conceptual overview.
Enable them per-server, either at creation time or on an existing server:

```
nvidia-cuda-mps-control server create <name> --locality-domains=<true|false>
nvidia-cuda-mps-control server set <name> --locality-domains=<true|false>
```

Locality domains are mutually exclusive with static SM partitions on the same server.

## Features[#](https://docs.nvidia.com#features)

Optional server-side behaviors are exposed as toggleable features through the
`feature`

module. Feature names are given positionally.

```
nvidia-cuda-mps-control feature enable <memacct|context-share>
nvidia-cuda-mps-control feature disable <memacct|context-share>
nvidia-cuda-mps-control feature describe [memacct|context-share] [--format=<table|csv>[,noheader]]
```

`feature describe`

prints, for one or all registered features: `FEATURE`

,
`STATE`

(`enabled`

/`disabled`

, with `(default)`

appended when it matches the
built-in default), `MODULE`

, and `COVERS`

.

```
$ nvidia-cuda-mps-control feature describe
FEATURE STATE MODULE COVERS
memacct enabled (default) memacct -
context-share enabled (default) context-share -
```

### memacct[#](https://docs.nvidia.com#memacct)

The `memacct`

feature governs automatic memory accounting and audit logging.

```
nvidia-cuda-mps-control memacct set audit_log=<true|false>
nvidia-cuda-mps-control memacct describe [--format=<table|csv>[,noheader]]
```

`audit_log`

is the only supported key. It is disabled by default.

## Configuration File[#](https://docs.nvidia.com#configuration-file)

MPS v3 can load its full startup configuration from a TOML file with `-a`

/`--apply`

,
covering servers, namespaces, devices, SM partitions, and features in a single file.
Refer to [MPS v3 Configuration File](https://docs.nvidia.com/mpsv3-configuration-file.html#mpsv3-configuration-file) for the full schema and an example.

```
nvidia-cuda-mps-control -d -p 3 -a /path/to/config.toml
```

## Directories and Environment Variables[#](https://docs.nvidia.com#directories-and-environment-variables)

MPS v3 clients and servers use the same [Appendix: Environment Variables](https://docs.nvidia.com/appendix-environment-variables.html#environment-variables) as
Legacy MPS v2, including `CUDA_VISIBLE_DEVICES`

,
`CUDA_MPS_PIPE_DIRECTORY`

, `CUDA_MPS_LOG_DIRECTORY`

, and
`CUDA_DEVICE_MAX_CONNECTIONS`

. `CUDA_MPS_ACTIVE_THREAD_PERCENTAGE`

,
`CUDA_MPS_PINNED_DEVICE_MEM_LIMIT`

, and `CUDA_MPS_CLIENT_PRIORITY`

also work the
same on the client side, but interact with MPS v3 namespace-level settings
differently than with Legacy MPS v2’s daemon-wide settings; see the notes under each
variable’s entry there.

MPS v3 uses the same pipe directory and log directory defaults as Legacy MPS v2:

`CUDA_MPS_PIPE_DIRECTORY`

– If set, used directly. Otherwise defaults to`/run/nvidia-mps`

when the daemon runs as root, or`/tmp/nvidia-mps`

otherwise. Each server and namespace gets its own subdirectory under the pipe directory containing its`control`

socket; each server’s subdirectory also contains its`log`

pipe.`CUDA_MPS_LOG_DIRECTORY`

– Defaults to`/var/log/nvidia-mps`

. The daemon log is`control.log`

; each server logs to`<server-name>/server.log`

.

At startup, the daemon prints the pipe directory clients should connect through:

```
To connect CUDA applications to this daemon, set CUDA_MPS_PIPE_DIRECTORY=/run/nvidia-mps
```