source: https://docs.nvidia.com/cuda/npp/core_npp.html

# Core NPP Functions[](https://docs.nvidia.com#core-npp-functions)

Basic functions for library management, in particular library version and device property query functions.

Functions

-
const
[NppLibraryVersion](https://docs.nvidia.com/nppdefs.html#c.NppLibraryVersion)*nppGetLibVersion(void)[](https://docs.nvidia.com#c.nppGetLibVersion)

-
Get the NPP library version.

- Returns
-
A struct containing separate values for major and minor revision and build number.