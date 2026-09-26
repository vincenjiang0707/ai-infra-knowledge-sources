# [Issue #228] __version__ doesn't match Git tags for post-releases, breaking build tools

source: https://github.com/deepseek-ai/DeepGEMM/issues/228
state: closed | updated: 2026-04-30T06:23:13Z
labels: 

## 正文

## Problem

When building from post-release tags (e.g., `v2.1.1.post3`), the `__version__` in `deep_gemm/__init__.py` contains only the base version (`2.1.1`), not the full post-release version.

This causes:
- Our build tool failures when validating wheel version with expected version from the tag
- Dependency resolution issues for packages requiring specific post-release versions
- PEP 440/427/517 compliance violations

## Example

```bash
git checkout v2.1.1.post3
grep __version__ deep_gemm/__init__.py
# Shows: __version__ = '2.1.1'  (missing .post3)

DG_USE_LOCAL_VERSION=0 python -m build --wheel
ls dist/
# Produces: deep_gemm-2.1.1-*.whl
# Expected: deep_gemm-2.1.1.post3-*.whl
```

## Affected Tags

- v2.1.1.post1
- v2.1.1.post2
- v2.1.1.post3

## PEP Violations

### PEP 440 (Version Identification and Dependency Specification):
Post-releases are defined as versions like X.Y.Z.postN to address minor errors in final releases. The Git tags correctly use post-release format (v2.1.1.post3), but the package metadata reports only the
base version (2.1.1), making it impossible for users to install or depend on specific post-release versions. This breaks the semantic meaning of post-releases in the Python packaging ecosystem.

### PEP 427 (The Wheel Binary Package Format):
The wheel filename format is strictly defined as {distribution}-{version}-{python}-{abi}-{platform}.whl. Building from tag v2.1.1.post3 produces deep_gemm-2.1.1-*.whl instead of the correct
deep_gemm-2.1.1.post3-*.whl. This filename mismatch breaks tools that verify artifact provenance, security scanners that match versions, and package managers that rely on filename-based version
identification.

### PEP 517 (Build-System Independent Format):
Build backends must create .dist-info directories with accurate metadata. When building from v2.1.1.post3, the resulting .dist-info/METADATA file contains Version: 2.1.1 instead of Version: 2.1.1.post3.
This causes build frontends (pip, build, etc.) to receive incorrect version information, breaking dependency resolution and violating the expectation that build metadata accurately reflects the source
version.

## Proposed Solution

For future post-release tags, update __version__ in deep_gemm/__init__.py to match the tag:

When creating tag v2.1.1.post4:
__version__ = '2.1.1.post4'  # Include the .postN suffix

Alternatively, consider migrating to https://setuptools-scm.readthedocs.io/ which automatically derives version from Git tags, eliminating manual version management.

 I am happy to submit a PR with either solution if you're interested in fixing this for future releases.

---


## 评论 (1)

### pavank63 · 2025-11-25

ping @LyricZhao @ko3n1g 
