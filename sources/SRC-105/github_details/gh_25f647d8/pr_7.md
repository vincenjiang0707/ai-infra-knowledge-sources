# [PR #7] Update dcgmbuild image.

source: https://github.com/NVIDIA/DCGM/pull/7
state: closed | updated: 2021-09-01T23:43:10Z
labels: 

## 正文

* Base image is Ubuntu 20.04
* GCC 9.2 -> GCC 9.3 update
* Newer version of crosstool-ng is used to build GCC
* Updated 3rd party libraries versions
* Updated CMake toolchain config to reflect switching from GCC 9.2 to GCC 9.3
* Minor fix in python code to satisfy updated pylint
* Updated Copyright year 2020 -> 2021

Signed-off-by: Nik Konyuchenko <spaun2002mobile@gmail.com>

## 评论 (1)

### nikkon-dev · 2021-09-01

Fixes #6 

## Review (1)

### glowkey · 2021-09-01 · APPROVED

(no text)
