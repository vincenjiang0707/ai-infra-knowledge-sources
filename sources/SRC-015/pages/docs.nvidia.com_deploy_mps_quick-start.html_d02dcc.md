source: https://docs.nvidia.com/deploy/mps/quick-start.html

# Quick Start[#](https://docs.nvidia.com#quick-start)

For an in-depth guide on MPS usage, refer to [Common Tasks](https://docs.nvidia.com/common-tasks.html#common-tasks).

For an in-depth guide on commands, environment variables, and more, refer to [Legacy MPS v2 Interface](https://docs.nvidia.com/mpsv2-interface.html#mpsv2-interface).

## Starting the MPS controller[#](https://docs.nvidia.com#starting-the-mps-controller)

To start the MPS controller as a daemon (recommended):

```
nvidia-cuda-mps-control -d
```

Protocol version 3 can be selected with the `-p`

/`--protocol`

flag:

```
nvidia-cuda-mps-control -d -p 3
```

Or with the `CUDA_MPS_PROTOCOL_VERSION`

environment variable:

```
export CUDA_MPS_PROTOCOL_VERSION=3
nvidia-cuda-mps-control -d
```

## Launching an application under MPS[#](https://docs.nvidia.com#launching-an-application-under-mps)

When the MPS controller is active, CUDA applications will use MPS:

```
./cuda_application
```

This can be verified with the `ps`

command while the application is running:

```
echo ps | nvidia-cuda-mps-control
```

```
nvidia-cuda-mps-control client list --all
```

This can also be verified by using `nvidia-smi`

after the application is launched to verify the existence of the `nvidia-cuda-mps-server`

process. While the application is running, it will also appear in `nvidia-smi`

with the `M+C`

type specified.

## Quitting MPS[#](https://docs.nvidia.com#quitting-mps)

To quit the MPS controller and any associated MPS servers:

```
echo quit | nvidia-cuda-mps-control
```

```
nvidia-cuda-mps-control -q
```

## Explicitly starting an MPS server[#](https://docs.nvidia.com#explicitly-starting-an-mps-server)

To explicitly start an MPS server for user `$UID`

:

```
echo start_server -uid $UID | nvidia-cuda-mps-control
```

```
nvidia-cuda-mps-control server create --uid=$UID
```

Note that servers are started implicitly when a CUDA application is launched while the MPS controller is active.

## Starting multiple control/server pairs[#](https://docs.nvidia.com#starting-multiple-control-server-pairs)

To start multiple MPS servers for the same user, you can use different CUDA MPS directories to start different controllers.

```
export CUDA_MPS_PIPE_DIRECTORY=/tmp/nvidia-mps-0 # Select a location that's accessible to the given $UID
export CUDA_MPS_LOG_DIRECTORY=/tmp/nvidia-log-0 # Select a location that's accessible to the given $UID
nvidia-cuda-mps-control -d # Start an MPS controller on pipe 0
```

```
export CUDA_MPS_PIPE_DIRECTORY=/tmp/nvidia-mps-1 # Select a location that's accessible to the given $UID
export CUDA_MPS_LOG_DIRECTORY=/tmp/nvidia-log-1 # Select a location that's accessible to the given $UID
nvidia-cuda-mps-control -d # Start an MPS controller on pipe 1
```

A single MPS v3 daemon manages multiple named servers directly, so there is no need to start multiple control daemons on separate pipe directories:

```
nvidia-cuda-mps-control server create pipe0
nvidia-cuda-mps-control server create pipe1
```

Each server gets its own pipe directory automatically:

```
$ nvidia-cuda-mps-control server get pipe0 pipe-directory
/run/nvidia-mps/pipe0
$ nvidia-cuda-mps-control server get pipe1 pipe-directory
/run/nvidia-mps/pipe1
```

To start an application under one of the controllers, the same CUDA_MPS_PIPE_DIRECTORY must be set for the application as the controller.

```
CUDA_MPS_PIPE_DIRECTORY=/tmp/nvidia-mps-0 CUDA_MPS_LOG_DIRECTORY=/tmp/nvidia-log-0 ./cuda_application # This will use the MPS controller on pipe 0
CUDA_MPS_PIPE_DIRECTORY=/tmp/nvidia-mps-1 CUDA_MPS_LOG_DIRECTORY=/tmp/nvidia-log-1 ./cuda_application # This will use the MPS controller on pipe 1
```

```
# This will use the "pipe0" server
CUDA_MPS_PIPE_DIRECTORY=/run/nvidia-mps/pipe0 ./cuda_application
# This will use the "pipe1" server
CUDA_MPS_PIPE_DIRECTORY=/run/nvidia-mps/pipe1 ./cuda_application
```

## Starting an MPS server with Locality Domains[#](https://docs.nvidia.com#starting-an-mps-server-with-locality-domains)

To start a server configured to use MLOPart on supported devices for user `$UID`

:

```
echo start_server -uid $UID -mlopart | nvidia-cuda-mps-control
```

MLOPart is renamed to locality domains in MPS v3, and is enabled per-server instead of per-server-start:

```
nvidia-cuda-mps-control server create --uid=$UID --locality-domains=true
```

For more information, refer to [Locality Domains](https://docs.nvidia.com/when-to-use-mps.html#memory-locality-optimized-partitions) and
[Locality Domains](https://docs.nvidia.com/mpsv3-interface.html#mpsv3-locality-domains).

## Enabling static SM partitioning[#](https://docs.nvidia.com#enabling-static-sm-partitioning)

Static SM partitioning must be enabled at MPS controller start time:

```
nvidia-cuda-mps-control -d -S
```

MPS v3 does not require a daemon-startup flag; SM partitions are created
per-device once the daemon and server are running. The default UID-based server
(auto-named `uid_$UID`

) can be used directly:

```
nvidia-cuda-mps-control -d -p 3
nvidia-cuda-mps-control server create --uid=$UID
nvidia-cuda-mps-control sm-partition create large --server=uid_$UID --device=0 --chunks=4
```

For more information, refer to [Static SM Partitioning](https://docs.nvidia.com/when-to-use-mps.html#static-sm-partitioning) and
[SM Partitions](https://docs.nvidia.com/mpsv3-interface.html#mpsv3-static-partitions).