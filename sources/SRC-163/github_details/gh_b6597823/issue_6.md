# [Issue #6] cmake error when running "cmake -B build" in swiftTransformer

source: https://github.com/LLMServe/DistServe/issues/6
state: closed | updated: 2024-06-11T09:16:51Z
labels: 

## 正文

-- Using the multi-header code from /home/fx/cql/DistServe/SwiftTransformer/build/_deps/json-src/include/
-- Configuring done (30.8s)
CMake Error at src/csrc/kernel/CMakeLists.txt:23 (add_library):
  No SOURCES given to target: xformers_autogen_impl

## 评论 (1)

### interestingLSY · 2024-06-11

Please run `git submodule update --init --recursive` after cloning the `SwiftTransformer` repository.

By the way, it is encouraged to share your solution for others if you have figured out it for your issue.
