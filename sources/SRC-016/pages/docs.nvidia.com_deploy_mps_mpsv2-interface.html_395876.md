source: https://docs.nvidia.com/deploy/mps/mpsv2-interface.html

# Legacy MPS v2 Interface[#](https://docs.nvidia.com#legacy-mps-v2-interface)

The following describes the commands, environment variables and utilities available to configure and interact with the MPS execution environment.

## nvidia-cuda-mps-control[#](https://docs.nvidia.com#nvidia-cuda-mps-control)

The control daemon executable has the following options:

`-d`

– Start daemon in background process`-f`

– Start daemon in foreground.`-v`

– Print version of control daemon executable`-S`

or`--static-partitioning`

– Start daemon with static partitioning mode enabled.

The control daemon has an interactive shell, which can accept the following commands:

`get_server_list`

– prints out a list of all PIDs of server instances.`get_server_status <PID>`

– this will print out the status of the server with the given <PID>.`start_server -uid <user id> [-mlopart]`

– manually starts a new instance of nvidia-cuda-mps-server with the given user ID. If`mlopart`

is specified, then clients will create MLOPart devices if supported.`get_client_list <PID>`

– lists the PIDs of client applications connected to a server instance assigned to the given PID.`quit`

– terminates the`nvidia-cuda-mps-control`

daemon.`get_device_client_list [<PID>]`

– lists the devices and PIDs of client applications that enumerated this device. It optionally takes the server instance PID.`set_default_active_thread_percentage <percentage>`

– overrides the default active thread percentage for MPS servers. If there is already a server spawned, this command will only affect the next server. The set value is lost if a`quit`

command is executed. The default is 100.`get_default_active_thread_percentage`

– queries the current default available thread percentage.`set_active_thread_percentage <PID> <percentage>`

– overrides the active thread percentage for the MPS server instance of the given PID. All clients created with that server afterwards will observe the new limit. Existing clients are not affected.`get_active_thread_percentage <PID>`

– queries the current available thread percentage of the MPS server instance of the given PID.`set_default_device_pinned_mem_limit <dev> <value>`

– sets the default device pinned memory limit for each MPS client. If there is already a server spawned, this command will only affect the next server. The set value is lost if a`quit`

command is executed. The dev argument may be a device UUID string or an integer ordinal. The value must be in the form of an integer followed by a qualifier, either “G” or “M” that specifies the value in Gigabyte or Megabyte respectively. For example, to set a limit of 10 gigabytes for device 0, use the following command:`set_default_device_pinned_mem_limit 0 10G`

By default, there is no memory limit set.

Note that for this command, the dev argument is not validated against available devices in the MPS server. Therefore, it is possible to set two memory limits for the same device: one by device UUID and another by ordinal. When an MPS server is started, whichever limit was set last will take effect. A limit set with an invalid device UUID or ordinal will be ignored when starting the MPS server.

`get_default_device_pinned_mem_limit <dev>`

– queries the current default pinned memory limit for the device. The`dev`

argument may be device UUID string or an integer ordinal.Note that this command does not translate between device UUIDs or ordinals and will return the limit that was set for each device identifier via the

`set_default_device_pinned_mem_limit`

command.`set_device_pinned_mem_limit <PID> <dev> <value>`

- overrides the device pinned memory limit for MPS servers. This sets the device pinned memory limit for each client of MPS server instance of the given PID for the device dev. All clients created with that server afterwards will observe the new limit. Existing clients are not affected. The`dev`

argument may be a device UUID string or an integer ordinal. For example, to set a limit of 900MB for the server with pid 1024 for device 0, use the following command:`set_device_pinned_mem_limit 1024 0 900M`

`get_device_pinned_mem_limit <PID> <dev>`

– queries the current device pinned memory limit of the MPS server instance of the given PID for the device`dev`

. The`dev`

argument may be a device UUID string or an integer ordinal.`terminate_client <server PID> <client PID>`

– terminates all the outstanding GPU work of the MPS client process`<client PID>`

running on the MPS server denoted by`<server PID>`

. For example, to terminate the outstanding GPU work for an MPS client process with PID 1024 running on an MPS server with PID 123, use the following command:`terminate_client 123 1024`

`ps [-p PID]`

– reports a snapshot of the current client processes. It optionally takes the server instance PID. It displays the PID, the unique identifier assigned by the server, the partial UUID of the associated device, the PID of the connected server, the namespace PID, and the command line of the client.`set_default_client_priority [priority]`

– sets the default client priority that will be used for new clients. The value is not applied to existing clients. Priority values should be considered as hints to the CUDA Driver, not guarantees. Allowed values are`0 [NORMAL]`

and 1`[BELOW NORMAL]`

. The set value is lost if a`quit`

command is executed. The default is`0 [NORMAL]`

.`get_default_client_priority`

– queries the current priority value that will be used for new clients.`device_query [<server PID>] [--csv]`

– Queries the devices that are available to MPS clients. If a server PID is specified, then the command will output the device information for that server and ignore other servers. If`csv`

is specified, then the command will output the device information in a comma-separated format.`sm_partition add <device UUID> <number of chunks>`

– creates an SM partition with the specified number of chunks on the given device. Upon successful creation, the full partition ID is displayed. This command accepts unique partial UUIDs of devices.`sm_partition rm <device UUID> <partition>`

– removes the specified SM partition from the given device.`lspart`

– displays the current SM partitioning configuration. The output includes the device UUID, partition IDs, free and used chunks, free and used SMs, and whether the partition is in use. The display uses unique partial UUIDs of devices.

## Environment Variables[#](https://docs.nvidia.com#environment-variables)

Refer to [Appendix: Environment Variables](https://docs.nvidia.com/appendix-environment-variables.html#environment-variables) for the full list of environment variables used
to configure Legacy MPS v2 (and MPS v3).