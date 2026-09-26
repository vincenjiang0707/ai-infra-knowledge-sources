# [Issue #871] Note that hipify-perl needs to be present when building 

source: https://github.com/ROCm/rccl/issues/871
state: closed | updated: 2024-01-17T18:16:44Z
labels: 

## 正文

When building on the latest 5.6.1 release, I notice that if `hipify-perl` is not present when building, the process of hipify-ing the source code will silently fail during CMake setup and produce confusing errors like those that appear in #672. Perhaps it would be a good idea to mention in the README that `hipify-perl` needs to be installed when building, or let CMake fail when `hipify-perl` cnanot be found.

## 评论 (1)

### BertanDogancay · 2024-01-17

hipify-perl comes with ROCm by default (I believe since 5.5.1) and even if it's not present in the system for any reason, errors when building RCCL are clear and indicate that the hipify-perl executable not found. If you can attach the build logs, we can take a closer look.
