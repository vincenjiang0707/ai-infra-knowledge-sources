# [Issue #1417] [Feature Request] CMake FindPackage support and version exposure

source: https://github.com/ai-dynamo/nixl/issues/1417
state: closed | updated: 2026-07-02T13:23:38Z
labels: 

## 正文

nvFuser is working to add [support for NIXL](https://github.com/NVIDIA/Fuser/pull/6016). It would be helpful to us to have CMake `find_package` support or at the very least an easy way to parse or query for the installed version of NIXL and the Major CUDA version it was built with.

We can pull the version information with: 
```
NIXL_LOG_LEVEL=INFO python -c "import nixl"
python -c "import nixl; print(nixl._pkg.__name__.split(\"_cu\")[-1])"
```
However evaluating / parsing these outputs is cumbersome / fragile for a dependency check.

Ideally we woudl like find_package to populate the versions so we can so something like:
```
find_package(nixl REQUIRED)
if (nixl_FOUND)
  message(nixl_VERSION) ....
  message(nixl_CUDAToolkit_VERSION) ....
endif()

target_link_libraries(my_lib ... nixl::nixl)
```

## 评论 (1)

### brminich · 2026-07-02

not relevant anymore
