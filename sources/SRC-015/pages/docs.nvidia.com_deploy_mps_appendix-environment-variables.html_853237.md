source: https://docs.nvidia.com/deploy/mps/appendix-environment-variables.html

# Appendix: Environment Variables[#](https://docs.nvidia.com#appendix-environment-variables)

The following environment variables apply identically to [Legacy MPS v2](https://docs.nvidia.com/mpsv2-interface.html#mpsv2-interface) and
[MPS v3](https://docs.nvidia.com/mpsv3-interface.html#mpsv3-interface) clients and servers, except where a MPS v3-specific
note is called out below.

## CUDA_VISIBLE_DEVICES[#](https://docs.nvidia.com#cuda-visible-devices)

`CUDA_VISIBLE_DEVICES`

is used to specify which GPU’s should be visible to a CUDA
application. Only the devices whose index or UUID is present in the sequence are visible
to CUDA applications and they are enumerated in the order of the sequence.

When `CUDA_VISIBLE_DEVICES`

is set before launching the control daemon, the
devices will be remapped by the MPS server. This means that if your system has devices
0, 1 and 2, and if `CUDA_VISIBLE_DEVICES`

is set to `0,2`

, then when a client connects
to the server it will see the remapped devices – device 0 and a device 1. Therefore,
keeping `CUDA_VISIBLE_DEVICES`

set to `0,2`

when launching the client would lead
to an error.

To avoid this ambiguity, we recommend using UUIDs instead of indices. These can be
viewed by launching `nvidia-smi -q`

. When launching the server, or the application,
you can set `CUDA_VISIBLE_DEVICES`

to `UUID_1,UUID_2`

, where `UUID_1`

and
`UUID_2`

are the GPU UUIDs. It will also work when you specify the first few characters
of the UUID (including `GPU-`

) rather than the full UUID.

The MPS server will fail to start if incompatible devices are visible after the application
of `CUDA_VISIBLE_DEVICES`

.

## CUDA_MPS_PIPE_DIRECTORY[#](https://docs.nvidia.com#cuda-mps-pipe-directory)

The MPS control daemon, the MPS server, and the associated MPS clients communicate
with each other via named pipes and UNIX domain sockets. The default directory for
these pipes and sockets is `/tmp/nvidia-mps`

. The environment variable,
`CUDA_MPS_PIPE_DIRECTORY`

, can be used to override the location of these pipes and
sockets. The value of this environment variable should be consistent across all MPS
clients sharing the same MPS server, and the MPS control daemon.

The recommended location for the directory containing these named pipes and domain
sockets is local folders such as `/tmp`

. If the specified location exists in a shared, multi-node
filesystem, the path must be unique for each node to prevent multiple MPS servers
or MPS control daemons from using the same pipes and sockets. When provisioning
MPS on a per-user basis, the directory should be set to a location such that
different users will not end up using the same directory.

On Tegra platforms, there is no default directory setting for pipes and sockets. Users must set this environment variable such that only intended users have access to this location.

## CUDA_MPS_LOG_DIRECTORY[#](https://docs.nvidia.com#cuda-mps-log-directory)

The MPS control daemon maintains a `control.log`

file which contains the status of
its MPS servers, user commands issued and their result, and startup and shutdown
notices for the daemon. The MPS server maintains a `server.log`

file containing its
startup and shutdown information and the status of its clients.

By default these log files are stored in the directory `/var/log/nvidia-mps`

. The
`CUDA_MPS_LOG_DIRECTORY`

environment variable can be used to override the default
value. This environment variable should be set in the MPS control daemon’s
environment and is automatically inherited by any MPS servers launched by that control daemon.

On Tegra platforms, there is no default directory setting for storing the log files. MPS will remain operational without the user setting this environment variable; however, in such instances, MPS logs will not be available. If logs are required to be captured, then the user must set this environment variable such that only intended users have access to this location.

## CUDA_DEVICE_MAX_CONNECTIONS[#](https://docs.nvidia.com#cuda-device-max-connections)

When encountered in the MPS client’s environment,
`CUDA_DEVICE_MAX_CONNECTIONS`

sets the preferred number of compute and
copy engine concurrent connections (work queues) from the host to the device for that
client. The number actually allocated by the driver may differ from what is requested
based on hardware resource limitations or other considerations. Under MPS, each
server’s clients share one pool of connections, whereas without MPS each CUDA context
would be allocated its own separate connection pool. Volta MPS clients exclusively
owns the connections set aside for the client in the shared pool, so setting this
environment variable under Volta MPS may reduce the number of available clients. The
default value is 2 for Volta MPS clients.

## CUDA_MPS_ACTIVE_THREAD_PERCENTAGE[#](https://docs.nvidia.com#cuda-mps-active-thread-percentage)

On Volta GPUs, this environment variable sets the portion of the available threads that can be used by the client contexts. The limit can be configured at different levels:

Setting this environment variable in an MPS control’s environment will configure the default active thread percentage when the MPS control daemon starts. All the MPS servers spawned by the MPS control daemon will observe this limit. Once the MPS control daemon has started, changing this environment variable cannot affect the MPS servers.


Setting this environment variable in an MPS client’s environment will configure the active thread percentage when the client process starts. The new limit will only further constrain the limit set by the control daemon (via

`set_default_active_thread_percentage`

or`set_active_thread_percentage`

control daemon commands or this environment variable at the MPS control daemon level). If the control daemon has a lower setting, the control daemon setting will be obeyed by the client process instead.All the client CUDA contexts created within the client process will observe the new limit. Once the client process has started, changing the value of this environment variable cannot affect the client CUDA contexts.


By default, configuring the active thread percentage at the client CUDA context level is disabled. User must explicitly opt-in via environment variable

`CUDA_MPS_ENABLE_PER_CTX_DEVICE_MULTIPROCESSOR_PARTITIONING`

. Refer to[CUDA_MPS_ENABLE_PER_CTX_DEVICE_MULTIPROCESSOR_PARTITIONING](https://docs.nvidia.com#cuda-mps-enable-per-ctx-device-multiprocessor-partitioning)for more details.Setting this environment variable within a client process will configure the active thread percentage when creating a new client CUDA context. The new limit will only further constraint the limit set at the control daemon level and the client process level. If the control daemon or the client process has a lower setting, the lower setting will be obeyed by the client CUDA context instead. All the client CUDA contexts created afterwards will observe the new limit. Existing client CUDA contexts are not affected.


Note

Under MPS v3, if the client’s namespace has an active thread percentage set (see
[MPS v3 Interface](https://docs.nvidia.com/mpsv3-interface.html#mpsv3-interface)), that value overrides the client-process-level setting
from this environment variable, rather than only further constraining it as the
control-daemon-level setting does under Legacy MPS v2.

## CUDA_MPS_ENABLE_PER_CTX_DEVICE_MULTIPROCESSOR_PARTITIONING[#](https://docs.nvidia.com#cuda-mps-enable-per-ctx-device-multiprocessor-partitioning)

By default, users can only partition the available threads uniformly. An explicit opt-in via this environment variable is required to enable non-uniform partitioning capability. To enable non-uniform partitioning capability, this environment variable must be set before the client process starts.

When non-uniform partitioning capability is enabled in an MPS client’s environment,
client CUDA contexts can have different active thread percentages within the same
client process via setting `CUDA_MPS_ACTIVE_THREAD_PERCENTAGE`

before
context creations. The device attribute `cudaDevAttrMultiProcessorCount`

will
reflect the active thread percentage and return the portion of available SMs that can be
used by the client CUDA context current to the calling thread.

## CUDA_MPS_PINNED_DEVICE_MEM_LIMIT[#](https://docs.nvidia.com#cuda-mps-pinned-device-mem-limit)

The pinned memory limit control limits the amount of GPU memory that is allocatable
by CUDA APIs by the client process. On Volta GPUs, this environment variable sets a
limit on pinned device memory that can be allocated by the client contexts. Setting this
environment variable in an MPS client’s environment will set the device’s pinned
memory limit when the client process starts. The new limit will only further constrain
the limit set by the control daemon (via `set_default_device_pinned_mem_limit`

or `set_device_pinned_mem_limit control`

daemon commands or this environment
variable at the MPS control daemon level). If the control daemon has a lower value, the
control daemon setting will be obeyed by the client process instead. This environment
variable will have the same semantics as `CUDA_VISIBLE_DEVICES`

i.e. the value string
can contain comma-separated device ordinals and/or device UUIDs with per device
memory limit separated by an equals. Example usage:

```
$ export CUDA_MPS_PINNED_DEVICE_MEM_LIMIT=''0=1G,1=512MB''
```

The following example highlights the hierarchy and usage of the MPS memory limiting functionality.

```
# Set the default device pinned mem limit to 3G for device 0. The default limit constrains the memory allocation limit of all the MPS clients of future MPS servers to 3G on device 0.
$ nvidia-cuda-mps-control set_default_device_pinned_mem_limit 0 3G
# Start daemon in background process
$ nvidia-cuda-mps-control -d
# Set device pinned mem limit to 2G for device 0 for the server instance of the
# given PID. All the MPS clients on this server will observe this new limit of 2G
# instead of the default limit of 3G when allocating pinned device memory on device 0.
# Note -- users are allowed to specify a server limit (via set_device_pinned_mem_limit)
# greater than the default limit previously set by set_default_device_pinned_mem_limit.
$ nvidia-cuda-mps-control set_device_pinned_mem_limit <pid> 0 2G
# Further constrain the device pinned mem limit for a particular MPS client to 1G for
# device 0. This ensures the maximum amount of memory allocated by this client is capped
# at 1G.
# Note - setting this environment variable to a value greater than value observed by the
# server for its clients (through set_default_device_pinned_mem_limit/ set_device_pinned_mem_limit)
# will not set the limit to the higher value and thus will be ineffective and the eventual
# limit observed by the client will be that observed by the server.
$ export CUDA_MPS_DEVICE_MEM_LIMIT="0=1G"
```

Note

Under MPS v3, the enforced limit is sourced from the client’s namespace
(`--pinned-memory-limit=`

, see [MPS v3 Interface](https://docs.nvidia.com/mpsv3-interface.html#mpsv3-interface)) instead of a single
daemon-wide default and per-server override. This environment variable still
works identically on the client side, further constraining whatever limit the
namespace has set.

## CUDA_MPS_CLIENT_PRIORITY[#](https://docs.nvidia.com#cuda-mps-client-priority)

The client priority level variable controls the initial default server value for the MPS Control Daemon if used to launch that, or the client priority level value for a given client if used in a client launch. The following examples demonstrate both usages.

```
# Set the default client priority level for new servers and clients to Below Normal
$ export CUDA_MPS_CLIENT_PRIORITY=1
$ nvidia-cuda-mps-control -d
# Set the client priority level for a single program to Normal without changing the priority level for future clients
$ CUDA_MPS_CLIENT_PRIORITY=0 <program>
```

Note

CUDA priority levels are not guarantees of execution order – they are only a performance hint to the CUDA driver.

Note

Under MPS v3, if a client leaves this environment variable unset, its namespace’s
client priority (`--client-priority=`

, see [MPS v3 Interface](https://docs.nvidia.com/mpsv3-interface.html#mpsv3-interface)) is used as the
default instead of the daemon-wide default. If the client does set this
environment variable, it takes effect the same way as under Legacy MPS v2.