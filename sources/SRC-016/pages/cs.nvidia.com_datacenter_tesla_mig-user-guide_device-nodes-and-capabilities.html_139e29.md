source: https://docs.nvidia.com/datacenter/tesla/mig-user-guide/device-nodes-and-capabilities.html

# Device Nodes and Capabilities[#](https://docs.nvidia.com#device-nodes-and-capabilities)

Currently, the NVIDIA kernel driver exposes its interfaces through a few system-wide device nodes. Each physical GPU
is represented by its own device node - for example, `nvidia0`

, `nvidia1`

and so on. This is shown below for a 2-GPU system.

```
/dev
├── nvidiactl
├── nvidia-modeset
├── nvidia-uvm
├── nvidia-uvm-tools
├── nvidia-nvswitchctl
├── nvidia0
└── nvidia1
```

Starting with CUDA 11/R450, a new abstraction known as `nvidia-capabilities`

has been introduced. The idea being that access
to a specific capability is required to perform certain actions through the driver. If a user has access to the capability,
the action will be carried out. If a user does not have access to the capability, the action will fail. The one exception
being if you are the root-user (or any user with `CAP_SYS_ADMIN`

privileges). With `CAP_SYS_ADMIN`

privileges, you
implicitly have access to all `nvidia-capabilities`

.

For example, the `mig-config`

capability allows one to create and destroy MIG instances on any MIG-capable GPU (for example,
the A100 GPU). Without this capability, all attempts to create or destroy a MIG instance will fail. Likewise, the `fabric-mgmt`

capability allows one to run the Fabric Manager as a non-root but privileged daemon. Without this capability, all attempts
to launch the Fabric Manager as a non-root user will fail.

The following sections walk through the system level interface for managing these new `nvidia-capabilities`

, including the
steps necessary to grant and revoke access to them.

## System Level Interface[#](https://docs.nvidia.com#system-level-interface)

There are two different system-level interfaces available to work with `nvidia-capabilities`

. The first is via `/dev`

and
the second is via `/proc`

. The `/proc`

based interface relies on user-permissions and mount namespaces to limit access to
a particular capability, while the `/dev`

based interface relies on *cgroups*. Technically, the `/dev`

based interface
also relies on user-permissions as a second-level access control mechanism (on the actual device node files themselves), but
the primary access control mechanism is cgroups. The current CUDA 11/R450 GA (Linux driver 450.51.06) supports both mechanisms,
but going forward the `/dev`

based interface is the preferred method and the /proc based interface is deprecated. For now, users
can choose the desired interface by using the `nv_cap_enable_devfs`

parameter on the `nvidia.ko`

kernel module:

When

`nv_cap_enable_devfs=0`

, the`/proc`

based interface is enabled.When

`nv_cap_enable_devfs=1`

, the`/dev`

based interface is enabled.A setting of

`nv_cap_enable_devfs=0`

is the default for the R450 driver (as of Linux 450.51.06).All future NVIDIA datacenter drivers will have a default of

`nv_cap_enable_devfs=1`

.

The following is an example of loading the `nvidia`

kernel module with this parameter set:

```
$ modprobe nvidia nv_cap_enable_devfs=1
```

### /dev Based nvidia-capabilities[#](https://docs.nvidia.com#dev-based-nvidia-capabilities)

The system level interface for interacting with `/dev`

based capabilities is actually through a combination of `/proc`

and `/dev`

.

First, a new major device is now associated with nvidia-caps and can be read from the standard `/proc/devices`

file.

```
$ cat /proc/devices | grep nvidia-caps
508 nvidia-caps
```

Second, the exact same set of files exist under `/proc/driver/nvidia/capabilities`

. These files no longer control access to
the capability directly and instead, the contents of these files point at a device node under `/dev`

, through which cgroups
can be used to control access to the capability.

This can be seen in the following example:

```
$ cat /proc/driver/nvidia/capabilities/mig/config
DeviceFileMinor: 1
DeviceFileMode: 256
DeviceFileModify: 1
```

The combination of the device major for `nvidia-caps`

and the value of `DeviceFileMinor`

in this file indicate that
the `mig-config`

capability (which allows a user to create and destroy MIG devices) is controlled by the device node with
a `major:minor`

of `238:1`

. As such, one will need to use `cgroups`

to grant a process read access to this device in
order to configure MIG devices. The purpose of the `DeviceFileMode`

and `DeviceFileModify`

fields in this file are explained
later on in this section.

The standard location for these device nodes is under `/dev/nvidia-caps`

:

```
$ ls -l /dev/nvidia-caps
total 0
cr-------- 1 root root 508, 1 Nov 21 17:16 nvidia-cap1
cr--r--r-- 1 root root 508, 2 Nov 21 17:16 nvidia-cap2
...
```

Unfortunately, these device nodes cannot be automatically created/deleted by the NVIDIA driver at the same time it creates/deletes
files under `/proc/driver/nvidia/capabilities`

(due to GPL compliance issues). Instead, a user-level program called `nvidia-modprobe`

is provided, that can be invoked from user-space in order to do this. For example:

```
$ nvidia-modprobe \
-f /proc/driver/nvidia/capabilities/mig/config \
-f /proc/driver/nvidia/capabilities/mig/monitor
$ ls -l /dev/nvidia-caps
total 0
cr-------- 1 root root 508, 1 Nov 21 17:16 nvidia-cap1
cr--r--r-- 1 root root 508, 2 Nov 21 17:16 nvidia-cap2
```

`nvidia-modprobe`

looks at the `DeviceFileMode`

in each capability file and creates the device node with the permissions
indicated (for example, `+ur`

from a value of 256 (o400) from our example for `mig-config`

).

Programs such as `nvidia-smi`

will automatically invoke `nvidia-modprobe`

(when available) to create these device nodes
on your behalf. In other scenarios it is not necessarily required to use nvidia-modprobe to create these device nodes, but
it does make the process simpler.

If you actually want to prevent `nvidia-modprobe`

from ever creating a particular device node on your behalf, you can do the following:

```
# Give a user write permissions to the capability file under /proc
$ chmod +uw /proc/driver/nvidia/capabilities/mig/config
# Update the file with a "DeviceFileModify" setting of 0
$ echo "DeviceFileModify: 0" > /proc/driver/nvidia/capabilities/mig/config
```

You will then be responsible for managing creation of the device node referenced by `/proc/driver/nvidia/capabilities/mig/config`

going forward. If you want to change that in the future, simply reset it to a value of `DeviceFileModify: 1`

with the same command sequence.

This is important in the context of containers because we may want to give a container access to a certain capability even
if it doesn’t exist in the `/proc`

hierarchy yet.

For example, granting a container the `mig-config`

capability implies that we should also grant it capabilities to access all
possible gis and cis that could be created for any GPU on the system. Otherwise the container will have no way of working with
those gis and cis once they have actually been created.

One final thing to note about `/dev`

based capabilities is that the minor numbers for all possible capabilities are
predetermined and can be queried under various files of the form:

```
/proc/driver/nvidia-caps/*-minors
```

For example, all capabilities related to MIG can be looked up as:

```
$ cat /proc/driver/nvidia-caps/mig-minors
config 1
monitor 2
gpu0/gi0/access 3
gpu0/gi0/ci0/access 4
gpu0/gi0/ci1/access 5
gpu0/gi0/ci2/access 6
...
gpu31/gi14/ci6/access 4321
gpu31/gi14/ci7/access 4322
```

The format of the content is: `GPU<deviceMinor>/gi<GPU instance ID>/ci<compute instance ID>`


Note that the GPU device minor number can be obtained by using either of these mechanisms:

The NVML API

`nvmlDeviceGetMinorNumber()`

so it returns the device minor numberOr use the PCI BDF available under

`/proc/driver/nvidia/gpus/domain:bus:device:function/information`

. This file contains a “Device Minor” field.

Note

The NVML device numbering (such as through `nvidia-smi)`

is not the device minor number.

For example, if the MIG geometry was created as below:

```
+-----------------------------------------------------------------------------+
| MIG devices: |
+------------------+----------------------+-----------+-----------------------+
| GPU GI CI MIG | Memory-Usage | Vol| Shared |
| ID ID Dev | BAR1-Usage | SM Unc| CE ENC DEC OFA JPG|
| | | ECC| |
|==================+======================+===========+=======================|
| 0 1 0 0 | 19MiB / 40192MiB | 14 0 | 3 0 3 0 3 |
| | 0MiB / 65535MiB | | |
+------------------+ +-----------+-----------------------+
| 0 1 1 1 | | 14 0 | 3 0 3 0 3 |
| | | | |
+------------------+ +-----------+-----------------------+
| 0 1 2 2 | | 14 0 | 3 0 3 0 3 |
| | | | |
+------------------+----------------------+-----------+-----------------------+
```

Then the corresponding device nodes: `/dev/nvidia-cap12`

, `/dev/nvidia-cap13`

, `/dev/nvidia-cap14`

, and `/dev/nvidia-cap15`

would be created.

### /proc based nvidia-capabilities (**Deprecated**)[#](https://docs.nvidia.com#proc-based-nvidia-capabilities-deprecated)

The system level interface for interacting with `/proc`

based nvidia-capabilities is rooted at `/proc/driver/nvidia/capabilities`

.
Files underneath this hierarchy are used to represent each capability, with read access to these files controlling whether a user
has a given capability or not. These files have no content and only exist to represent a given capability.

For example, the `mig-config`

capability (which allows a user to create and destroy MIG devices) is represented as follows:

```
/proc/driver/nvidia/capabilities
└── mig
└── config
```

Likewise, the capabilities required to run workloads on a MIG device once it has been created are represented as follows (namely as access to the GPU Instance and Compute Instance that comprise the MIG device):

```
/proc/driver/nvidia/capabilities
└── gpu0
└── mig
├── gi0
│ ├── access
│ └── ci0
│ └── access
├── gi1
│ ├── access
│ └── ci0
│ └── access
└── gi2
├── access
└── ci0
└── access
```

And the corresponding file system layout is shown below with read permissions:

```
$ ls -l /proc/driver/nvidia/capabilities/gpu0/mig/gi*
/proc/driver/nvidia/capabilities/gpu0/mig/gi1:
total 0
-r--r--r-- 1 root root 0 May 24 17:38 access
dr-xr-xr-x 2 root root 0 May 24 17:38 ci0
/proc/driver/nvidia/capabilities/gpu0/mig/gi2:
total 0
-r--r--r-- 1 root root 0 May 24 17:38 access
dr-xr-xr-x 2 root root 0 May 24 17:38 ci0
```

For a CUDA process to be able to run on top of MIG, it needs access to the Compute Instance capability and its parent GPU Instance. Thus a MIG device is identified by the following format:

```
MIG-<GPU-UUID>/<GPU instance ID>/<compute instance ID>
```

As an example, having read access to the following paths would allow one to run workloads on
the MIG device represented by `<gpu0, gi0, ci0>`

:

```
/proc/driver/nvidia/capabilities/gpu0/mig/gi0/access
/proc/driver/nvidia/capabilities/gpu0/mig/gi0/ci0/access
```

Note that there is no access file representing a capability to run workloads on gpu0 (only on gi0 and ci0 that sit underneath gpu0). This is because the traditional mechanism of using cgroups to control access to top level GPU devices (and any required meta devices) is still required. As shown earlier in the document, the cgroups mechanism applies to:

```
/dev/nvidia0
/dev/nvidiactl
/dev/nvidiactl-uvm
...
```

In the context of containers, a new mount namespace should be overlaid on top of the path for `/proc/driver/nvidia/capabilities`

,
and only those capabilities a user wishes to grant to a container should be **bind-mounted** in. Since the host’s
user/group information is retained across the bind-mount, it must be ensured that the correct user permissions are
set for these capabilities on the host before injecting them into a container.