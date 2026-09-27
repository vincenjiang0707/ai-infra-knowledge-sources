# [Issue #246] dcgm >= 4.0 installs headers in possible wrong include path

source: https://github.com/NVIDIA/DCGM/issues/246
state: open | updated: 2025-07-16T17:41:42Z
labels: 

## 正文

It appears that starting with dcgm 4.0, dcgm is now installing its headers files in the following location:

```/usr/include/datacenter-gpu-manager-4```

This is mentioned in the release nodes here:

https://docs.nvidia.com/datacenter/dcgm/latest/release-notes/changelog.html#id16

But is a subdirectory really required with FHS 3.0? The way dcgm's own includes are implemented, applications are not able to do:

```#include <datacenter-gpu-manger-4/dcgm_agent.h>```

Because dcgm_agent.h assumes that the files it includes are in the standard search path, and now that is no longer the case. We are forced to add an explicit `-I/usr/include/datacenter-gpu-manager-4` for dcgm's non-standard include path.


## 评论 (1)

### morrone · 2025-07-16

It doesn't look like dcgm includes a pkgconfig file either, which might haven been used by apps to automatically the new path that dcgm now requires.
