source: https://docs.nvidia.com/deploy/mps/mpsv3-namespaces.html

# MPS v3 Namespaces[#](https://docs.nvidia.com#mps-v3-namespaces)

A namespace subdivides a [server](https://docs.nvidia.com/mpsv3-interface.html#mpsv3-interface)’s resources – pinned memory
limit, active thread percentage, and client priority – for a group of clients. Servers
are typically shared across many clients with different resource needs; namespaces let
those groups of clients be managed independently without requiring a separate server
per group.

Every server has an implicit `default`

namespace, which is used by clients that do
not target a specific namespace. Refer to [MPS v3 Interface](https://docs.nvidia.com/mpsv3-interface.html#mpsv3-interface) for the
`namespace create`

/`delete`

/`list`

/`set`

/`get`

command reference, and to
[MPS v3 Configuration File](https://docs.nvidia.com/mpsv3-configuration-file.html#mpsv3-configuration-file) for configuring namespaces from a TOML file.

## Namespace Routing[#](https://docs.nvidia.com#namespace-routing)

A client selects its namespace by which socket, under the server’s pipe directory, it connects to:

```
$CUDA_MPS_PIPE_DIRECTORY/
├── control # main daemon control socket
├── training/ # server "training"
│ ├── control # server listener socket (routes to the default namespace)
│ ├── default/
│ │ └── control # default namespace socket
│ ├── high_priority/ # custom namespace
│ │ └── control # namespace socket
│ └── batch/
│ └── control
```

`$CUDA_MPS_PIPE_DIRECTORY/training/high_priority/control`

– routes to the`high_priority`

namespace on server`training`

.`$CUDA_MPS_PIPE_DIRECTORY/training/control`

– routes to server`training`

’s`default`

namespace.`$CUDA_MPS_PIPE_DIRECTORY/control`

– UID-based auto-routing, for backward compatibility with Legacy MPS v2 clients.

A client sets `CUDA_MPS_PIPE_DIRECTORY`

to the namespace’s directory to connect
through that namespace’s socket, in the same way Legacy MPS v2 clients set it to a
server’s pipe directory.