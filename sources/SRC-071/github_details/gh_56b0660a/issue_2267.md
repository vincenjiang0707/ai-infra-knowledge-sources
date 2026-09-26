# [Issue #2267] [CI] Windows wheel build is much slower as ccache is not effectively used

source: https://github.com/tile-ai/tilelang/issues/2267
state: closed | updated: 2026-09-02T07:36:31Z
labels: enhancement, help wanted, windows

## 正文

### Required prerequisites

- [x] I have searched the [Issue Tracker](https://github.com/tile-ai/tilelang/issues) that this hasn't already been reported. (comment there if it has.)

### Motivation

## Problem

The Windows dist/wheel build in the `Dist` workflow takes significantly longer  than the other platforms.

Example from run:
https://github.com/tile-ai/tilelang/actions/runs/26380636948

Build wheel step duration:

- macOS Metal: ~2m13s
- Linux CUDA x86_64: ~5m02s
- Linux CUDA arm64: ~5m01s
- Windows CUDA 13.0: ~39m54s


### Solution

_No response_

### Alternatives

_No response_

### Additional context

_No response_

## 评论 (2)

### LeiWang1999 · 2026-05-25

would you mind taking a look? @sepcnt 

### sepcnt · 2026-05-25

The Windows job appears to be ccache-thrashing because embedded MSVC PDB debug info makes the .obj files much larger, so I suggest increasing the Windows ccache size from 200MB to 1GB, which should keep enough objects cached and likely resolve the slowdown.
