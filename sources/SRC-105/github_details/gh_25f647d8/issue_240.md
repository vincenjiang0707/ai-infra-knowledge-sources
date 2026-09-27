# [Issue #240] Can't use build.sh to build DCGM

source: https://github.com/NVIDIA/DCGM/issues/240
state: open | updated: 2025-08-29T02:30:25Z
labels: 

## 正文

The `build.sh` is failing with the following error:

```bash
target dcgmbuild-x86_64: failed to solve: dcgm/toolchain-x86_64:4.0.0-gcc14-5ae63b: failed to resolve source metadata for docker.io/dcgm/toolchain-x86_64:4.0.0-gcc14-5ae63b: pull access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed
```

~My guess is that docker is not building dependencies correctly. So when a command is run `docker compose build --with-dependencies dcgmbuild-x86_64`, it does not build the `dcgm-toolchain-x86_64` before.~

Buildkit with docker-compose is trying to refer to the `TOOLCHAIN_BASE_IMAGE` from docker hub instead of the local build, even though there are images built and available locally:

```bash
✗  docker images
REPOSITORY                            TAG               IMAGE ID       CREATED         SIZE
dcgm/common-host-software             latest            0d7a6ad2d691   7 minutes ago   2.95GB
dcgmbuild-dcgm-common-host-software   latest            0d7a6ad2d691   7 minutes ago   2.95GB
moby/buildkit                         buildx-stable-1   72a94020693f   6 weeks ago     216MB
```


**Steps to reproduce:**

```bash
git checkout 6e947dcac9b3160d61d98fea4741d51d4bec5c1f
cd dcgmbuild
./build.sh
```

**Full output:**

```bash
✗  bash -x ./build.sh
+ set -o errexit -o pipefail -o nounset
+ [[ '' -eq 1 ]]
+ ARCHITECTURES=("x86_64" "aarch64")
+ [[ 0 -gt 0 ]]
+ [[ ! -v TAG ]]
++ scripts/toolchain-sha256sum
++ head -c6
+ TAG=4.0.0-gcc14-5ae63b
+ export BASE_IMAGE=ubuntu:24.04
+ BASE_IMAGE=ubuntu:24.04
+ export TAG
+ for ARCHITECTURE in "${ARCHITECTURES[@]}"
+ docker compose build --with-dependencies dcgmbuild-x86_64
[+] Building 1.0s (10/13)
 => [internal] load local bake definitions                                                                                                        0.0s
 => => reading from stdin 2.04kB                                                                                                                  0.0s
 => [dcgm-common-host-software internal] load build definition from common-host-software.Dockerfile                                               0.1s
 => => transferring dockerfile: 1.90kB                                                                                                            0.0s
 => [dcgm-toolchain-x86_64 internal] load build definition from target-toolchain.Dockerfile                                                       0.1s
 => => transferring dockerfile: 2.86kB                                                                                                            0.0s
 => [dcgmbuild-x86_64 internal] load build definition from dcgmbuild.Dockerfile                                                                   0.1s
 => => transferring dockerfile: 1.90kB                                                                                                            0.0s
 => ERROR [dcgmbuild-x86_64 internal] load metadata for docker.io/dcgm/toolchain-x86_64:4.0.0-gcc14-5ae63b                                        0.4s
 => [dcgm-common-host-software internal] load metadata for docker.io/library/ubuntu:24.04                                                         0.5s
 => ERROR [dcgm-toolchain-x86_64 internal] load metadata for docker.io/dcgm/common-host-software:4.0.0-gcc14-5ae63b                               0.4s
 => [dcgm-common-host-software internal] load .dockerignore                                                                                       0.0s
 => => transferring context: 143B                                                                                                                 0.0s
 => [dcgm-common-host-software 1/4] FROM docker.io/library/ubuntu:24.04@sha256:440dcf6a5640b2ae5c77724e68787a906afb8ddee98bf86db94eea8528c2c076   0.2s
 => => resolve docker.io/library/ubuntu:24.04@sha256:440dcf6a5640b2ae5c77724e68787a906afb8ddee98bf86db94eea8528c2c076                             0.2s
 => [dcgm-common-host-software internal] load build context                                                                                       0.0s
------
 > [dcgmbuild-x86_64 internal] load metadata for docker.io/dcgm/toolchain-x86_64:4.0.0-gcc14-5ae63b:
------
------
 > [dcgm-toolchain-x86_64 internal] load metadata for docker.io/dcgm/common-host-software:4.0.0-gcc14-5ae63b:
------
dcgmbuild.Dockerfile:18
--------------------
  16 |     ARG BASE_IMAGE=dcgm/toolchain-x86_64:latest
  17 |
  18 | >>> FROM $BASE_IMAGE AS builder
  19 |
  20 |     RUN set -ex; \
--------------------
target dcgmbuild-x86_64: failed to solve: dcgm/toolchain-x86_64:4.0.0-gcc14-5ae63b: failed to resolve source metadata for docker.io/dcgm/toolchain-x86_64:4.0.0-gcc14-5ae63b: pull access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed
```

## 评论 (3)

### wangywy · 2025-07-25

Encountered the same problem.

### shaochen0 · 2025-07-29

I also encountered the same problem.

### malkir · 2025-08-29

@surajssd @wangywy @shaochen0 You build this image locally via dcgmbuild, it's not hosted. Please see the README and close the issue.

```
Creating the build image

The build image is stored in ./dcgmbuild.

The image can be built by:

    ensuring Docker is installed and running
    navigating to ./dcgmbuild
    running ./build.sh
```
