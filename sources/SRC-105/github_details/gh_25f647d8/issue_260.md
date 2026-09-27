# [Issue #260] dcgmbuild/build.sh error

source: https://github.com/NVIDIA/DCGM/issues/260
state: open | updated: 2025-12-01T03:06:48Z
labels: 

## 正文

Hello,

I found the following error when running the build image [step](https://github.com/NVIDIA/DCGM/blob/ca755f1487915935447be84e70c45d2d7b050f3c/README.md#creating-the-build-image) from the README:

```bash
cd dcgmbuild
./build.sh
# omitting verbose output...
Error response from daemon: No such image: dcgm/dcgmbuild:4.0.0-gcc14-e9ab2c-x86_64
```

I found the issue is fixed when I comment out [this line](https://github.com/NVIDIA/DCGM/blob/ca755f1487915935447be84e70c45d2d7b050f3c/dcgmbuild/build.sh#L56) in the build script. I also noticed the rest of the [build steps](https://github.com/NVIDIA/DCGM/blob/ca755f1487915935447be84e70c45d2d7b050f3c/README.md#generating-a-dcgm-build) run correctly as well.

Maybe the line should just be removed?

## 评论 (2)

### pintohutch · 2025-10-22

Btw this is on version [`v4.4.1`](https://github.com/NVIDIA/DCGM/releases/tag/v4.4.1).

### Along-Ren · 2025-12-01




> Btw this is on version [`v4.4.1`](https://github.com/NVIDIA/DCGM/releases/tag/v4.4.1).

@pintohutch Building this project on Mac is very difficult. Can you push the `dcgmbuild` image to DockerHub? Please share the URL. THX

