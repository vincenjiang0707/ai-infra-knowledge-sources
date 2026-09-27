# [Issue #181] Support for Amazon Linux 2023 (AL2023)

source: https://github.com/NVIDIA/DCGM/issues/181
state: open | updated: 2025-07-25T13:35:40Z
labels: 

## 正文

In your DCGM documentation you indicate that the supported platforms do not include Amazon Linux 2023 (AL2023) [0].

But you do support AL2023 in your CUDA toolkit [1], and have many packages for AL2023 in your repository [2].

We primarily use `dcgm-exporter` and in the past it was possible to build `dcgm-exporter` for the previous version of Amazon Linux 2 (AL2) by installing the RHEL version of the DCGM package from your package repositories. But AL2023 is not compatible with RHEL and therefore the packages in your repositories don't work on AL2023. Ideally I wouldn't have to build `dcgm-exporter` but simply install it from your package repository, like other Linux distributions do easily.

I've tried building DCGM from source on AL2023 and get an error unfortunately. I'm not going to document that error here because the more pertinent question is: why do you provide DCGM packages for other Linux distributions but not AL2023?

I'm officially requesting the following packages be built for AL2023 and provided in your `amzn2023` package repository [2]:

  * `datacenter-gpu-manager`
  * `dcgm-exporter`


Thanks for your support!

-Matt

[0]: https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/getting-started.html#supported-platforms
[1]: https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#amazon-linux-2023
[2]: https://developer.download.nvidia.com/compute/cuda/repos/amzn2023/x86_64/



## 评论 (1)

### limmike · 2025-07-25

Seems that DCGM is adding support for AL2023 soon

Version 4.3.0 of [DCGM release notes](https://docs.nvidia.com/datacenter/dcgm/latest/release-notes/changelog.html) list AL2023 repository support for both x86_64 and arm64 (sbsa)


Install instructions at https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/getting-started.html#amazon-linux-2023

I was able to install it. 

```
[ec2-user@ip-172-31-2-169 ~]$ cat /etc/os-release 
NAME="Amazon Linux"
VERSION="2023"
ID="amzn"
ID_LIKE="fedora"
VERSION_ID="2023"
PLATFORM_ID="platform:al2023"
PRETTY_NAME="Amazon Linux 2023.8.20250721"
ANSI_COLOR="0;33"
CPE_NAME="cpe:2.3:o:amazon:amazon_linux:2023"
HOME_URL="https://aws.amazon.com/linux/amazon-linux-2023/"
DOCUMENTATION_URL="https://docs.aws.amazon.com/linux/"
SUPPORT_URL="https://aws.amazon.com/premiumsupport/"
BUG_REPORT_URL="https://github.com/amazonlinux/amazon-linux-2023"
VENDOR_NAME="AWS"
VENDOR_URL="https://aws.amazon.com/"
SUPPORT_END="2029-06-30"
[ec2-user@ip-172-31-2-169 ~]$ /usr/bin/dcgmi --version

dcgmi  version: 4.3.0
```
