source: https://docs.nvidia.com/cupti/library-support/library-support.html

# 3. Library support[#](https://docs.nvidia.com#library-support)

CUPTI can be used to profile CUDA applications, as well as applications that use CUDA via NVIDIA or third-party libraries. For most such libraries, the behavior is expected to be identical to applications using CUDA directly. However, for certain libraries, CUPTI has certain restrictions, or alternate behavior.

## 3.1. OptiX[#](https://docs.nvidia.com#optix)

CUPTI supports profiling of OptiX applications, but with certain restrictions.

Tracing

OptiX kernels are now grouped into a commandlist. CUPTI provides the tracing information for this commandlist.
CUPTI sets the `launchType`

field as `CUPTI_ACTIVITY_LAUNCH_TYPE_CBL_COMMANDLIST`

in the kernel activity record for the commandlist.
CUPTI also provides the name to the commandlist which is assigned by OptiX module during its creation.

Profiling

CUPTI can profile both internal and user kernels using the Profiling APIs. In the auto range mode, range names will be numeric values starting from 0 to total number of kernels including internal and user defined kernels or maximum number of range set while calling set config API, whichever is minimum.

It is suggested to create the profiling session and enable the profiling at resource allocation time (e.g. context creation) and disable the profiling at the context destruction time.

Limitations

CUPTI doesn’t issue any driver or runtime API callback for user kernels.

The PC sampling APIs are not supported for OptiX applications.