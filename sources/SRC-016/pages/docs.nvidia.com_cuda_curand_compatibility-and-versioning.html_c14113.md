source: https://docs.nvidia.com/cuda/curand/compatibility-and-versioning.html

# Compatibility and Versioning[](https://docs.nvidia.com#compatibility-and-versioning)

The host API of cuRAND is intended to be backward compatible at the source level with future releases (unless stated otherwise in the release notes of a specific future release). In other words, if a program uses cuRAND, it should continue to compile and work correctly with newer versions of cuRAND without source code changes.

cuRAND is not guaranteed to be backward compatible at the binary level.
Using different versions of the `curand.h`

header file and the shared
library is not supported. Using different versions of cuRAND and the
CUDA runtime is not supported.

The device API should be backward compatible at the source level for public functions in most cases.