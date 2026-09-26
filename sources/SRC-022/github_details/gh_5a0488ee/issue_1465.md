# [Issue #1465] [Feature]: Remove hipify as a build dependency.

source: https://github.com/ROCm/rccl/issues/1465
state: closed | updated: 2026-01-22T01:59:56Z
labels: enhancement, Under Investigation

## 正文

### Suggestion Description

hipify is only needed to run when the nccl codebase is updated.
Can hipify be moved to a maintainers options and a ci system generate/commit the hipified code ?
This would reduce the complexity and speed up the build. 


### Operating System

ALL

### GPU

ALL

### ROCm Component

RCCL

## 评论 (5)

### IMbackK · 2024-12-17

yeah i second this, its pretty silly having to use hipify at compiletime on a first party lib.

### nileshnegi · 2024-12-17

we'll look into this hipified-code-only approach.
however, most of the build time is spent in the linking stage... let us know if you measured something different.
also, you can reduce build time by building only for local GPU architecture using `./install.sh -l`

### IMbackK · 2024-12-17

For me this would be more about the benefit of a lessened dependency and the complexity of having to debug the hipifyed code while going back and forth between the original cuda and the generated hip.

The compile time is not a factor for me.

### systems-assistant[bot] · 2026-01-22

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/2780

### ammallya · 2026-01-22

Imported to ROCm/rocm-systems
