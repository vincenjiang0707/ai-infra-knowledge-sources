# [Issue #155] dcgm-exporter crashes hostengine.

source: https://github.com/NVIDIA/DCGM/issues/155
state: closed | updated: 2025-01-16T06:17:37Z
labels: 

## 正文

Running a [`3.3.5-3.4.0` exporter ](https://github.com/NVIDIA/dcgm-exporter/releases/tag/3.3.5-3.4.0) on a 3.3.5 host-engine as shipped via nvidia-ubuntu-repos SEGFAULTs the Host-engine.

Is there something I can do?
Shour that be reported to the exporter instead?

Logs:


<details><summary>dmesg crash info</summary>

```
Feb28 16:22] nvidia-nvswitch5: open (major=510)
[  +0,042810] nvidia-nvswitch4: open (major=510)
[  +0,042606] nvidia-nvswitch0: open (major=510)
[  +0,042409] nvidia-nvswitch2: open (major=510)
[  +0,042448] nvidia-nvswitch1: open (major=510)
[  +0,042372] nvidia-nvswitch3: open (major=510)
[Feb28 16:29] nv-hostengine[1280071]: segfault at 28 ip 00007f09f65c74b2 sp 00007f09f61e2ba0 error 6 in libdcgmmodulenvswitch.so.3.3.5[7f09f658c000+f8000]
[  +0,000008] Code: 7d b8 44 88 6d b0 e8 7d 0a ff ff 48 8b 45 a8 48 8b 73 18 48 89 45 c0 48 3b 73 20 0f 84 df 00 00 00 66 0f 6f 45 b0 48 83 c6 18 <0f> 11 46 e8 48 8b 45 c0 48 89 46 f8 48 89 73 18 48 8d 65 d8 5b 41
[  +0,155916] nvidia-nvswitch3: release (major=510)
[  +0,000005] nvidia-nvswitch1: release (major=510)
[  +0,000002] nvidia-nvswitch2: release (major=510)
[  +0,000003] nvidia-nvswitch0: release (major=510)
[  +0,000002] nvidia-nvswitch4: release (major=510)
[  +0,000002] nvidia-nvswitch5: release (major=510)
```

</details>


<details><summary>journal for exporter and hostengine</summary>

```
Feb 28 16:21:57 gx01 systemd[1]: Started NVIDIA DCGM service.
Feb 28 16:21:58 gx01 nv-hostengine[1280055]: DCGM initialized
Feb 28 16:21:58 gx01 nv-hostengine[1280055]: Started host engine version 3.3.5 using port number: 5555
Feb 28 16:29:08 gx01 systemd[1]: Started DCGM Exporter.
Feb 28 16:29:08 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:08+01:00" level=info msg="Starting dcgm-exporter"
Feb 28 16:29:08 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:08+01:00" level=info msg="Attemping to connect to remote hostengine at localhost:5555"
Feb 28 16:29:08 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:08+01:00" level=info msg="DCGM successfully initialized!"
Feb 28 16:29:09 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:09+01:00" level=info msg="Collecting DCP Metrics"
Feb 28 16:29:09 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:09+01:00" level=info msg="Falling back to metric file '/net/mgmtdelab/pool/html/dcgm/current/counters.csv'"
Feb 28 16:29:09 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:09+01:00" level=info msg="Initializing system entities of type: GPU"
Feb 28 16:29:11 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:11+01:00" level=info msg="Initializing system entities of type: NvSwitch"
Feb 28 16:29:11 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:11+01:00" level=info msg="Initializing system entities of type: NvLink"
Feb 28 16:29:11 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:11+01:00" level=info msg="Initializing system entities of type: CPU"
Feb 28 16:29:11 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:11+01:00" level=info msg="Not collecting CPU metrics; Error retrieving DCGM MIG hierarchy: This request is serviced by a module of DCGM that is not currently loaded"
Feb 28 16:29:11 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:11+01:00" level=info msg="Initializing system entities of type: CPU Core"
Feb 28 16:29:11 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:11+01:00" level=info msg="Not collecting CPU Core metrics; Error retrieving DCGM MIG hierarchy: This request is serviced by a module of DCGM that is not currently loaded"
Feb 28 16:29:14 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:14+01:00" level=warning msg="can not destroy group" error="Error destroying group: Host engine connection invalid/disconnected" groupID="{21}"
Feb 28 16:29:14 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:14+01:00" level=warning msg="Cannot destroy field group." error="Host engine connection invalid/disconnected"
Feb 28 16:29:14 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:14+01:00" level=fatal msg="Failed to watch metrics: Error watching fields: Host engine connection invalid/disconnected"
Feb 28 16:29:14 gx01 systemd[1]: dcgm-exporter.service: Main process exited, code=exited, status=1/FAILURE
Feb 28 16:29:14 gx01 systemd[1]: dcgm-exporter.service: Failed with result 'exit-code'.
Feb 28 16:29:14 gx01 systemd[1]: nvidia-dcgm.service: Main process exited, code=killed, status=11/SEGV
Feb 28 16:29:14 gx01 systemd[1]: nvidia-dcgm.service: Failed with result 'signal'.
```

</details>



<details><summary>Versions</summary>

```
# dcgm-exporter -v --debug
DCGM Exporter version 3.3.5-3.4.0
# dcgmi -v
Version : 3.3.5
Build ID : 14
Build Date : 2024-02-24
Build Type : Release
Commit ID : 93088b0e1286c6e7723af1930251298870e26c19
Branch Name : rel_dcgm_3_3
CPU Arch : x86_64
Build Platform : Linux 4.15.0-180-generic #189-Ubuntu SMP Wed May 18 14:13:57 UTC 2022 x86_64
CRC : 08a0d9624b562a1342bf5f8828939294
```

</details>



<details><summary>apt-cache policy datacenter-gpu-manager</summary>

```
# apt-cache policy datacenter-gpu-manager
datacenter-gpu-manager:
  Installed: 1:3.3.5
  Candidate: 1:3.3.5
  Version table:
 *** 1:3.3.5 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
        100 /var/lib/dpkg/status
     1:3.3.3 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     1:3.3.1 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     1:3.3.0 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     1:3.2.6 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     1:3.2.5 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     1:3.2.3 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     1:3.1.8 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     1:3.1.7 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     1:3.1.6 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     1:3.1.3 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     1:3.0.4 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     1:2.4.8 600
        600 https://repo.download.nvidia.com/baseos/ubuntu/focal/x86_64 focal-updates/common amd64 Packages
     1:2.4.7 600
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
        600 https://repo.download.nvidia.com/baseos/ubuntu/focal/x86_64 focal-updates/common amd64 Packages
     1:2.4.6 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     1:2.4.5 600
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
        600 https://repo.download.nvidia.com/baseos/ubuntu/focal/x86_64 focal-updates/common amd64 Packages
     1:2.3.6 600
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
        600 https://repo.download.nvidia.com/baseos/ubuntu/focal/x86_64 focal-updates/common amd64 Packages
     1:2.3.5 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     1:2.3.4 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     1:2.3.2 600
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
        600 https://repo.download.nvidia.com/baseos/ubuntu/focal/x86_64 focal-updates/common amd64 Packages
     1:2.3.1 600
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
        600 https://repo.download.nvidia.com/baseos/ubuntu/focal/x86_64 focal-updates/common amd64 Packages
     1:2.2.9 600
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
        600 https://repo.download.nvidia.com/baseos/ubuntu/focal/x86_64 focal-updates/common amd64 Packages
     1:2.2.8 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     1:2.2.3 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     1:2.1.8 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     1:2.1.7 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     1:2.1.4 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     1:2.0.15 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     1:2.0.14 600
        600 https://repo.download.nvidia.com/baseos/ubuntu/focal/x86_64 focal-updates/common amd64 Packages
     1:2.0.13 600
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
        600 https://repo.download.nvidia.com/baseos/ubuntu/focal/x86_64 focal/common amd64 Packages
```

</details>


<details><summary>OS info</summary>

```
# cat /etc/dgx-release
DGX_NAME="DGX Server"
DGX_PRETTY_NAME="NVIDIA DGX Server"
DGX_SWBUILD_DATE="2020-10-26-11-53-11"
DGX_SWBUILD_VERSION="5.0.0"
DGX_COMMIT_ID="7501dff"
DGX_PLATFORM="DGX Server for DGX A100"
DGX_SERIAL_NUMBER="XXXXXXXXXXXX"

DGX_OTA_VERSION="5.0.5"
DGX_OTA_DATE="XXXXXXXXXXXXXXXXX"

DGX_OTA_VERSION="5.1.1"
DGX_OTA_DATE="XXXXXXXXXXXXXXXXX"

DGX_OTA_VERSION="5.2.0"
DGX_OTA_DATE="XXXXXXXXXXXXXXXXX"

DGX_OTA_VERSION="5.3.1"
DGX_OTA_DATE="XXXXXXXXXXXXXXXXX"

DGX_OTA_VERSION="5.5.1"
DGX_OTA_DATE="XXXXXXXXXXXXXXXXX"
```

</details>



## 评论 (41)

### superg · 2024-02-28

Hi @krono,
Thank you for the report.
Is the issue easily reproducible?
Would it be possible to request nv-hostengine core dump?

EDIT: follow up questions
Do you get any syslog kernel error messages for NVLink in 16:21 - 16:29 timeframe?

### krono · 2024-03-01

Hi @superg  (somehow I don't get gh mails anymore, sorry)

<details><summary>kernel syslog messages in timeframe</summary>

```
root@gx01:/var/log# grep '^Feb 28 16:[23]' syslog.1
Feb 28 16:20:50 gx01 kernel: [103278.185814] audit: type=1400 audit(1709133650.187:1080): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/1278914/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:21:20 gx01 kernel: [103308.432689] audit: type=1400 audit(1709133680.436:1081): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/1279373/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:21:30 gx01 kernel: [103318.719235] audit: type=1400 audit(1709133690.720:1082): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/1279512/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:21:31 gx01 kernel: [103319.282115] audit: type=1400 audit(1709133691.284:1083): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/1279555/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:21:31 gx01 kernel: [103319.491742] audit: type=1400 audit(1709133691.492:1084): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/1279656/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:21:57 gx01 systemd[1]: Started NVIDIA DCGM service.
Feb 28 16:21:57 gx01 kernel: [103345.680201] nvidia-nvswitch5: open (major=510)
Feb 28 16:21:57 gx01 kernel: [103345.723011] nvidia-nvswitch4: open (major=510)
Feb 28 16:21:57 gx01 kernel: [103345.765617] nvidia-nvswitch0: open (major=510)
Feb 28 16:21:57 gx01 kernel: [103345.808026] nvidia-nvswitch2: open (major=510)
Feb 28 16:21:57 gx01 kernel: [103345.850474] nvidia-nvswitch1: open (major=510)
Feb 28 16:21:57 gx01 kernel: [103345.892846] nvidia-nvswitch3: open (major=510)
Feb 28 16:21:58 gx01 nv-hostengine: DCGM initialized
Feb 28 16:21:58 gx01 nv-hostengine[1280055]: Started host engine version 3.3.5 using port number: 5555
Feb 28 16:22:03 gx01 kernel: [103351.124025] audit: type=1400 audit(1709133723.125:1085): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/1280110/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:22:32 gx01 systemd[1]: Started DCGM Exporter.
Feb 28 16:22:32 gx01 kernel: [103380.216261] audit: type=1400 audit(1709133752.217:1086): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/28026/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:22:32 gx01 dcgm-exporter[1280577]: /net/mgmtdelab/pool/html/dcgm/3.3.5/x86_64/bin/dcgm-exporter: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.32' not found (required by /net/mgmtdelab/pool/html/dcgm/3.3.5/x86_64/bin/dcgm-exporter)
Feb 28 16:22:32 gx01 dcgm-exporter[1280577]: /net/mgmtdelab/pool/html/dcgm/3.3.5/x86_64/bin/dcgm-exporter: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.34' not found (required by /net/mgmtdelab/pool/html/dcgm/3.3.5/x86_64/bin/dcgm-exporter)
Feb 28 16:22:32 gx01 systemd[1]: dcgm-exporter.service: Main process exited, code=exited, status=1/FAILURE
Feb 28 16:22:32 gx01 systemd[1]: dcgm-exporter.service: Failed with result 'exit-code'.
Feb 28 16:23:02 gx01 systemd[1]: dcgm-exporter.service: Scheduled restart job, restart counter is at 3.
Feb 28 16:23:02 gx01 systemd[1]: Stopped DCGM Exporter.
Feb 28 16:23:02 gx01 systemd[1]: Started DCGM Exporter.
Feb 28 16:23:02 gx01 dcgm-exporter[1280963]: /net/mgmtdelab/pool/html/dcgm/3.3.5/x86_64/bin/dcgm-exporter: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.32' not found (required by /net/mgmtdelab/pool/html/dcgm/3.3.5/x86_64/bin/dcgm-exporter)
Feb 28 16:23:02 gx01 dcgm-exporter[1280963]: /net/mgmtdelab/pool/html/dcgm/3.3.5/x86_64/bin/dcgm-exporter: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.34' not found (required by /net/mgmtdelab/pool/html/dcgm/3.3.5/x86_64/bin/dcgm-exporter)
Feb 28 16:23:02 gx01 systemd[1]: dcgm-exporter.service: Main process exited, code=exited, status=1/FAILURE
Feb 28 16:23:02 gx01 systemd[1]: dcgm-exporter.service: Failed with result 'exit-code'.
Feb 28 16:23:07 gx01 systemd[1]: Stopped DCGM Exporter.
Feb 28 16:24:11 gx01 kernel: [103479.881565] audit: type=1400 audit(1709133851.887:1087): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/1281838/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:24:12 gx01 kernel: [103480.388663] audit: type=1400 audit(1709133852.395:1088): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/1281885/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:24:12 gx01 kernel: [103480.539563] audit: type=1400 audit(1709133852.543:1089): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/1281908/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:24:13 gx01 kernel: [103481.137739] audit: type=1400 audit(1709133853.143:1090): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/1281946/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:24:13 gx01 kernel: [103481.651807] audit: type=1400 audit(1709133853.655:1091): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/1281992/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:24:13 gx01 kernel: [103481.804767] audit: type=1400 audit(1709133853.811:1092): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/1282016/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:24:54 gx01 systemd[1]: tmp-.esp_tmp-nvme1n1p1.mount: Succeeded.
Feb 28 16:24:54 gx01 systemd[1]: tmp-.esp_tmp-nvme2n1p1.mount: Succeeded.
Feb 28 16:25:01 gx01 kernel: [103529.974717] audit: type=1400 audit(1709133901.980:1093): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/1282647/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:25:01 gx01 CRON[1282648]: (root) CMD (command -v debian-sa1 > /dev/null && debian-sa1 1 1)
Feb 28 16:25:01 gx01 kernel: [103529.976017] audit: type=1400 audit(1709133901.984:1094): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/1282648/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:25:52 gx01 kernel: [103580.650881] audit: type=1400 audit(1709133952.657:1095): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/1284754/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:26:22 gx01 kernel: [103610.898676] audit: type=1400 audit(1709133982.906:1096): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/1285172/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:28:11 gx01 kernel: [103719.026823] audit: type=1400 audit(1709134091.036:1097): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/1297267/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:28:11 gx01 kernel: [103719.579399] audit: type=1400 audit(1709134091.588:1098): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/1297309/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:28:11 gx01 kernel: [103719.755666] audit: type=1400 audit(1709134091.764:1099): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/1297333/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:29:08 gx01 systemd[1]: Started DCGM Exporter.
Feb 28 16:29:08 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:08+01:00" level=info msg="Starting dcgm-exporter"
Feb 28 16:29:08 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:08+01:00" level=info msg="Attemping to connect to remote hostengine at localhost:5555"
Feb 28 16:29:08 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:08+01:00" level=info msg="DCGM successfully initialized!"
Feb 28 16:29:09 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:09+01:00" level=info msg="Collecting DCP Metrics"
Feb 28 16:29:09 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:09+01:00" level=info msg="Falling back to metric file '/net/mgmtdelab/pool/html/dcgm/current/counters.csv'"
Feb 28 16:29:09 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:09+01:00" level=info msg="Initializing system entities of type: GPU"
Feb 28 16:29:11 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:11+01:00" level=info msg="Initializing system entities of type: NvSwitch"
Feb 28 16:29:11 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:11+01:00" level=info msg="Initializing system entities of type: NvLink"
Feb 28 16:29:11 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:11+01:00" level=info msg="Initializing system entities of type: CPU"
Feb 28 16:29:11 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:11+01:00" level=info msg="Not collecting CPU metrics; Error retrieving DCGM MIG hierarchy: This request is serviced by a module of DCGM that is not currently loaded"
Feb 28 16:29:11 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:11+01:00" level=info msg="Initializing system entities of type: CPU Core"
Feb 28 16:29:11 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:11+01:00" level=info msg="Not collecting CPU Core metrics; Error retrieving DCGM MIG hierarchy: This request is serviced by a module of DCGM that is not currently loaded"
Feb 28 16:29:13 gx01 kernel: [103781.951727] nv-hostengine[1280071]: segfault at 28 ip 00007f09f65c74b2 sp 00007f09f61e2ba0 error 6 in libdcgmmodulenvswitch.so.3.3.5[7f09f658c000+f8000]
Feb 28 16:29:13 gx01 kernel: [103781.951735] Code: 7d b8 44 88 6d b0 e8 7d 0a ff ff 48 8b 45 a8 48 8b 73 18 48 89 45 c0 48 3b 73 20 0f 84 df 00 00 00 66 0f 6f 45 b0 48 83 c6 18 <0f> 11 46 e8 48 8b 45 c0 48 89 46 f8 48 89 73 18 48 8d 65 d8 5b 41
Feb 28 16:29:14 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:14+01:00" level=warning msg="can not destroy group" error="Error destroying group: Host engine connection invalid/disconnected" groupID="{21}"
Feb 28 16:29:14 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:14+01:00" level=warning msg="Cannot destroy field group." error="Host engine connection invalid/disconnected"
Feb 28 16:29:14 gx01 dcgm-exporter[1298060]: time="2024-02-28T16:29:14+01:00" level=fatal msg="Failed to watch metrics: Error watching fields: Host engine connection invalid/disconnected"
Feb 28 16:29:14 gx01 kernel: [103782.107651] nvidia-nvswitch3: release (major=510)
Feb 28 16:29:14 gx01 kernel: [103782.107656] nvidia-nvswitch1: release (major=510)
Feb 28 16:29:14 gx01 kernel: [103782.107658] nvidia-nvswitch2: release (major=510)
Feb 28 16:29:14 gx01 kernel: [103782.107661] nvidia-nvswitch0: release (major=510)
Feb 28 16:29:14 gx01 kernel: [103782.107663] nvidia-nvswitch4: release (major=510)
Feb 28 16:29:14 gx01 kernel: [103782.107665] nvidia-nvswitch5: release (major=510)
Feb 28 16:29:14 gx01 systemd[1]: dcgm-exporter.service: Main process exited, code=exited, status=1/FAILURE
Feb 28 16:29:14 gx01 systemd[1]: dcgm-exporter.service: Failed with result 'exit-code'.
Feb 28 16:29:14 gx01 systemd[1]: nvidia-dcgm.service: Main process exited, code=killed, status=11/SEGV
Feb 28 16:29:14 gx01 systemd[1]: nvidia-dcgm.service: Failed with result 'signal'.
Feb 28 16:29:14 gx01 systemd[1]: nvidia-dcgm.service: Scheduled restart job, restart counter is at 1.
Feb 28 16:29:14 gx01 systemd[1]: Stopped NVIDIA DCGM service.
Feb 28 16:29:14 gx01 systemd[1]: Started NVIDIA DCGM service.
Feb 28 16:29:14 gx01 kernel: [103782.832440] nvidia-nvswitch5: open (major=510)
Feb 28 16:29:14 gx01 kernel: [103782.875110] nvidia-nvswitch4: open (major=510)
Feb 28 16:29:14 gx01 kernel: [103782.918412] nvidia-nvswitch0: open (major=510)
Feb 28 16:29:14 gx01 kernel: [103782.961611] nvidia-nvswitch2: open (major=510)
Feb 28 16:29:15 gx01 kernel: [103783.004035] nvidia-nvswitch1: open (major=510)
Feb 28 16:29:15 gx01 kernel: [103783.046633] nvidia-nvswitch3: open (major=510)
Feb 28 16:29:15 gx01 nv-hostengine: DCGM initialized
Feb 28 16:29:15 gx01 nv-hostengine[1298239]: Started host engine version 3.3.5 using port number: 5555
Feb 28 16:29:24 gx01 systemd[1]: Stopped DCGM Exporter.
Feb 28 16:29:24 gx01 systemd[1]: Stopping NVIDIA DCGM service...
Feb 28 16:29:24 gx01 kernel: [103792.219790] nvidia-nvswitch3: release (major=510)
Feb 28 16:29:24 gx01 kernel: [103792.219989] nvidia-nvswitch1: release (major=510)
Feb 28 16:29:24 gx01 kernel: [103792.220182] nvidia-nvswitch2: release (major=510)
Feb 28 16:29:24 gx01 kernel: [103792.220374] nvidia-nvswitch0: release (major=510)
Feb 28 16:29:24 gx01 kernel: [103792.220575] nvidia-nvswitch4: release (major=510)
Feb 28 16:29:24 gx01 kernel: [103792.220761] nvidia-nvswitch5: release (major=510)
Feb 28 16:29:24 gx01 systemd[1]: nvidia-dcgm.service: Succeeded.
Feb 28 16:29:24 gx01 systemd[1]: Stopped NVIDIA DCGM service.
Feb 28 16:29:32 gx01 slurmd[27067]: slurmd: launch task StepId=838896.12 request from UID:12211 GID:5101 HOST:172.20.26.64 PORT:39002
Feb 28 16:29:32 gx01 kernel: [103800.729913] audit: type=1400 audit(1709134172.738:1100): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/27067/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:29:32 gx01 slurmd[27067]: slurmd: task/affinity: lllp_distribution: JobId=838896 implicit auto binding: cores, dist 1
Feb 28 16:29:32 gx01 slurmd[27067]: slurmd: task/affinity: _task_layout_lllp_cyclic: _task_layout_lllp_cyclic
Feb 28 16:29:32 gx01 slurmd[27067]: slurmd: task/affinity: _lllp_generate_cpu_bind: _lllp_generate_cpu_bind jobid [838896]: mask_cpu, 0x0000000000000001000000000000000000000000000000010000000000000000
Feb 28 16:29:54 gx01 systemd[1]: tmp-.esp_tmp-nvme1n1p1.mount: Succeeded.
Feb 28 16:29:54 gx01 systemd[1]: tmp-.esp_tmp-nvme2n1p1.mount: Succeeded.
Feb 28 16:30:55 gx01 kernel: [103883.096874] audit: type=1400 audit(1709134255.111:1101): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/1299484/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:31:25 gx01 kernel: [103913.358790] audit: type=1400 audit(1709134285.372:1102): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/1299958/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:32:28 gx01 kernel: [103976.699653] audit: type=1400 audit(1709134348.713:1103): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/28026/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:34:54 gx01 systemd[1]: tmp-.esp_tmp-nvme1n1p1.mount: Succeeded.
Feb 28 16:34:54 gx01 systemd[1]: tmp-.esp_tmp-nvme2n1p1.mount: Succeeded.
Feb 28 16:35:01 gx01 CRON[1302542]: (root) CMD (command -v debian-sa1 > /dev/null && debian-sa1 1 1)
Feb 28 16:35:01 gx01 kernel: [104129.968910] audit: type=1400 audit(1709134501.985:1104): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/1302541/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:35:01 gx01 kernel: [104129.970106] audit: type=1400 audit(1709134501.985:1105): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/1302542/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:35:57 gx01 kernel: [104185.572325] audit: type=1400 audit(1709134557.590:1106): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/1303272/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:36:27 gx01 kernel: [104215.823679] audit: type=1400 audit(1709134587.842:1107): apparmor="ALLOWED" operation="open" profile="/usr/sbin/sssd" name="/proc/1303523/cmdline" pid=27038 comm="sssd_nss" requested_mask="r" denied_mask="r" fsuid=0 ouid=0
Feb 28 16:39:54 gx01 systemd[1]: tmp-.esp_tmp-nvme1n1p1.mount: Succeeded.
Feb 28 16:39:54 gx01 systemd[1]: tmp-.esp_tmp-nvme2n1p1.mount: Succeeded.
root@gx01:/var/log#
```

</details>

Reproducible? for me everytime.
Coredump:
<details><summary>coredumpctl</summary>

```
# coredumpctl dump nv-hostengine >nv-hostengine.core
           PID: 3124092 (nv-hostengine)
           UID: 0 (root)
           GID: 0 (root)
        Signal: 11 (SEGV)
     Timestamp: Fri 2024-03-01 10:07:47 CET (59s ago)
  Command Line: /usr/bin/nv-hostengine -n --service-account nvidia-dcgm
    Executable: /usr/bin/nv-hostengine
 Control Group: /system.slice/nvidia-dcgm.service
          Unit: nvidia-dcgm.service
         Slice: system.slice
       Boot ID: 35a3b73c95c04716880c91638ed46a93
    Machine ID: 5b05d12040d24d8e9c8d38117ab12eba
      Hostname: gx01
       Storage: /var/lib/systemd/coredump/core.nv-hostengine.0.35a3b73c95c04716880c91638ed46a93.3124092.1709284067000000000000.lz4
       Message: Process 3124092 (nv-hostengine) of user 0 dumped core.

                Stack trace of thread 3124104:
                #0  0x00007fc97150a4b2 n/a (libdcgmmodulenvswitch.so.3 + 0x594b2)
                #1  0x00007fc9711c5456 n/a (libnvidia-nscq.so.2 + 0x9d456)
                #2  0x00007fc9711760a3 n/a (libnvidia-nscq.so.2 + 0x4e0a3)
                #3  0x00007fc9711756bf n/a (libnvidia-nscq.so.2 + 0x4d6bf)
                #4  0x00007fc97117eb80 nscq_session_path_observe (libnvidia-nscq.so.2 + 0x56b80)
                #5  0x00007fc9715530e7 n/a (libdcgmmodulenvswitch.so.3 + 0xa20e7)
                #6  0x00007fc97152038f n/a (libdcgmmodulenvswitch.so.3 + 0x6f38f)
                #7  0x00007fc9714eb19d n/a (libdcgmmodulenvswitch.so.3 + 0x3a19d)
                #8  0x00007fc9714d6e9f n/a (libdcgmmodulenvswitch.so.3 + 0x25e9f)
                #9  0x00007fc9714d7834 n/a (libdcgmmodulenvswitch.so.3 + 0x26834)
                #10 0x00007fc9714dafd8 n/a (libdcgmmodulenvswitch.so.3 + 0x29fd8)
                #11 0x00007fc9714dc4a4 n/a (libdcgmmodulenvswitch.so.3 + 0x2b4a4)
                #12 0x00007fc9714e43b6 n/a (libdcgmmodulenvswitch.so.3 + 0x333b6)
                #13 0x00007fc9714dabb1 n/a (libdcgmmodulenvswitch.so.3 + 0x29bb1)
                #14 0x00007fc971561e5b n/a (libdcgmmodulenvswitch.so.3 + 0xb0e5b)
                #15 0x00007fc9715623a9 n/a (libdcgmmodulenvswitch.so.3 + 0xb13a9)
                #16 0x00007fc97417a609 start_thread (libpthread.so.0 + 0x8609)
                #17 0x00007fc973f2f353 __clone (libc.so.6 + 0x11f353)

                Stack trace of thread 3124101:
                #0  0x00007fc973f2895d syscall (libc.so.6 + 0x11895d)
                #1  0x00007fc971598791 n/a (libdcgmmodulenvswitch.so.3 + 0xe7791)
                #2  0x00007fc9714d8a74 n/a (libdcgmmodulenvswitch.so.3 + 0x27a74)
                #3  0x00007fc97152a408 n/a (libdcgmmodulenvswitch.so.3 + 0x79408)
                #4  0x00007fc974201343 n/a (libdcgm.so.3 + 0x6c343)
                #5  0x00007fc9742c742e n/a (libdcgm.so.3 + 0x13242e)
                #6  0x00007fc974326025 n/a (libdcgm.so.3 + 0x191025)
                #7  0x00007fc974334e9c n/a (libdcgm.so.3 + 0x19fe9c)
                #8  0x00007fc974321438 n/a (libdcgm.so.3 + 0x18c438)
                #9  0x00007fc9742c9aa7 n/a (libdcgm.so.3 + 0x134aa7)
                #10 0x00007fc9742c9d2d n/a (libdcgm.so.3 + 0x134d2d)
                #11 0x00007fc9742c9f1f n/a (libdcgm.so.3 + 0x134f1f)
                #12 0x00007fc9742a71fe n/a (libdcgm.so.3 + 0x1121fe)
                #13 0x00007fc974348871 n/a (libdcgm.so.3 + 0x1b3871)
                #14 0x00007fc974352ad8 n/a (libdcgm.so.3 + 0x1bdad8)
                #15 0x00007fc9743530a4 n/a (libdcgm.so.3 + 0x1be0a4)
                #16 0x00007fc974231de6 n/a (libdcgm.so.3 + 0x9cde6)
                #17 0x00007fc974356192 n/a (libdcgm.so.3 + 0x1c1192)
                #18 0x00007fc9744111c8 n/a (libdcgm.so.3 + 0x27c1c8)
                #19 0x00007fc97417a609 start_thread (libpthread.so.0 + 0x8609)
                #20 0x00007fc973f2f353 __clone (libc.so.6 + 0x11f353)

                Stack trace of thread 3124092:
                #0  0x00007fc973eed23f clock_nanosleep (libc.so.6 + 0xdd23f)
                #1  0x00007fc973ef2ec7 __nanosleep (libc.so.6 + 0xe2ec7)
                #2  0x000000000040736b n/a (nv-hostengine + 0x736b)
                #3  0x00007fc973e34083 __libc_start_main (libc.so.6 + 0x24083)
                #4  0x00000000004079bc n/a (nv-hostengine + 0x79bc)
```

</details>


[core.nv-hostengine.0.35a3b73c95c04716880c91638ed46a93.3124092.1709284067000000000000.lz4.zip](https://github.com/NVIDIA/DCGM/files/14458883/core.nv-hostengine.0.35a3b73c95c04716880c91638ed46a93.3124092.1709284067000000000000.lz4.zip)



### superg · 2024-03-01

Thank you for the dumps, I am currently looking into it. Will share my findings here.

### superg · 2024-03-04

I narrowed the search down to one of the NSCQ observe callbacks in:
[https://github.com/NVIDIA/DCGM/blob/master/modules/nvswitch/DcgmNvSwitchManager.cpp#L851C45-L851C53](url)

To understand more I would like to request debug level logs when the crash happen, here's how to do it:
Make sure nvidia-dcgm service is running (nv-hostengine), execute `dcgmi set --logging-severity DEBUG`, that will set nv-hostengine logging level to DEBUG. 
Next, reproduce the crash and share /var/nv-hostengine.log (feel free to clear it beforehand if needed).


### krono · 2024-03-05

Hi, here's the log
[nv-hostengine.log](https://github.com/NVIDIA/DCGM/files/14492590/nv-hostengine.log)


### krono · 2024-03-05

I do not see the log point ` log_debug("Attaching to NvSwitches");` being hit…

### superg · 2024-03-05

Thank you for the logs. indeed it crashed in another NSCQ observe callback: https://github.com/NVIDIA/DCGM/blob/master/modules/nvswitch/FieldDefinitions.cpp#L164

I am currently looking into the chain of events that led into this, will reply once I have more information.

### superg · 2024-04-01

Unfortunately we aren't able to reproduce this issue internally. However we've added better debugging to help diagnose such issues in the future and at some point it will be merged to GitHub.

### superg · 2024-04-01

Unfortunately we aren't able to reproduce this issue internally. However we've added better debugging to help diagnose such issues in the future and at some point it will be merged to GitHub.

### krono · 2024-04-01

Is there any way _i_ can debug that?
Like a step through debugger?

### superg · 2024-04-01

Yes, basically you will have to build debug DCGM with symbols. Then you will be able to use GDB, step through code and inspect variables etc. Put a breakpoint here: https://github.com/NVIDIA/DCGM/blob/master/modules/nvswitch/FieldDefinitions.cpp#L164
Just want to mention that this is pretty advanced and involves using ./build.sh script and docker dcgmbuild container (our build is containerized) and running nv-hostengine locally.

### krono · 2024-04-02


So here we are.

Debuggin around this:

```
    auto cb = [](const indexTypes... indicies,
                 nscq_rc_t rc,
                 TempData<nscqFieldType, storageType, is_vector, indexTypes...>::cbType in,
                 NscqDataCollector<TempData<nscqFieldType, storageType, is_vector, indexTypes...>> *dest) {
        if (dest == nullptr)
        {
            log_error("NSCQ passed dest = nullptr");

            return;
        }

        dest->callCounter++;

        if (NSCQ_ERROR(rc))
        {
            log_error("NSCQ {} passed error {}", dest->nscqPath, (int)rc);

            TempData<nscqFieldType, storageType, is_vector, indexTypes...> item;

            item.CollectFunc(dest, indicies...);

            return;
        }

        TempData<nscqFieldType, storageType, is_vector, indexTypes...> item; /* BREAKPOINT HERE */

        item.CollectFunc(dest, in, indicies...);
    };
```
shows:

### Normal behavior for stuff like tempreatures or throughput:

<details><summary>gdb debug output for `*dest`: normal stuff</summary>

```
Thread 5 "nv-hostengine" hit Breakpoint 2, DcgmNs::DcgmNvSwitchManager::UpdateFields<nscq_link_throughput_t, DcgmNs::FieldIdStorageType<(unsigned short)862>, false, nscq_uuid_t*>(unsigned short, DcgmFvBuffer&, std::vector<dcgm_field_update_info_t, std::allocator<dcgm_field_update_info_t> > const&, long)::{lambda(nscq_uuid_t*, signed char, nscq_link_throughput_t, DcgmNs::NscqDataCollector<DcgmNs::TempData<nscq_link_throughput_t, DcgmNs::FieldIdStorageType<(unsigned short)862>, false, nscq_uuid_t*> >*)#1}::operator()(nscq_uuid_t*, signed char, nscq_link_throughput_t, DcgmNs::NscqDataCollector<DcgmNs::TempData<nscq_link_throughput_t, DcgmNs::FieldIdStorageType<(unsigned short)862>, false, nscq_uuid_t*> >*) const (__closure=0x0, indicies#0=0x564fc0, rc=0 '\000', in=..., dest=0x7ffff4afb290) at /srv/DCGM/modules/nvswitch/FieldDefinitions.cpp:162
162	        TempData<nscqFieldType, storageType, is_vector, indexTypes...> item;
$64 = {
  callCounter = 6,
  fieldId = 862,
  nscqPath = 0x7ffff4fedcc0 <nscq_nvswitch_nvlink_throughput_counters> "/{nvswitch}/nvlink/throughput_counters",
  data = std::vector of length 5, capacity 8 = {{
      index = std::tuple containing = {
        [1] = 0x564ef0
      },
      data = {
        <DcgmNs::NvSwitch::Data::Uint64Data> = {
          value = 0
        },
        members of DcgmNs::FieldIdStorageType<862>:
        static fieldId = 862
      }
    }, {
      index = std::tuple containing = {
        [1] = 0x564d50
      },
      data = {
        <DcgmNs::NvSwitch::Data::Uint64Data> = {
          value = 0
        },
        members of DcgmNs::FieldIdStorageType<862>:
        static fieldId = 862
      }
    }, {
      index = std::tuple containing = {
        [1] = 0x564e20
      },
      data = {
        <DcgmNs::NvSwitch::Data::Uint64Data> = {
          value = 0
        },
        members of DcgmNs::FieldIdStorageType<862>:
        static fieldId = 862
      }
    }, {
      index = std::tuple containing = {
        [1] = 0x53df00
      },
      data = {
        <DcgmNs::NvSwitch::Data::Uint64Data> = {
          value = 0
        },
        members of DcgmNs::FieldIdStorageType<862>:
        static fieldId = 862
      }
    }, {
      index = std::tuple containing = {
        [1] = 0x565090
      },
      data = {
        <DcgmNs::NvSwitch::Data::Uint64Data> = {
          value = 0
        },
        members of DcgmNs::FieldIdStorageType<862>:
        static fieldId = 862
      }
    }}
}
```

</details>

This is more or less expected.

### It seems something breaks for "physical id":

1. We see the backtrace requests `"/{nvswitch}/id/phys_id"`
  
<details><summary>gdb bt at that point for `phys id</summary>

```
(gdb) bt
#0  DcgmNs::DcgmNvSwitchManager::UpdateFields<unsigned long, DcgmNs::FieldIdStorageType<(unsigned short)863>, false, nscq_uuid_t*, unsigned char>(unsigned short, DcgmFvBuffer&, std::vector<dcgm_field_update_info_t, std::allocator<dcgm_field_update_info_t> > const&, long)::{lambda(nscq_uuid_t*, unsigned char, signed char, unsigned long, DcgmNs::NscqDataCollector<DcgmNs::TempData<unsigned long, DcgmNs::FieldIdStorageType<(unsigned short)863>, false, nscq_uuid_t*, unsigned char> >*)#1}::operator()(nscq_uuid_t*, unsigned char, signed char, unsigned long, DcgmNs::NscqDataCollector<DcgmNs::TempData<unsigned long, DcgmNs::FieldIdStorageType<(unsigned short)863>, false, nscq_uuid_t*, unsigned char> >*) const (__closure=0x0, indicies#0=0x564ef0, indicies#1=0 '\000', rc=11 '\v', in=140737298543232, dest=0x716a20) at /srv/DCGM/modules/nvswitch/FieldDefinitions.cpp:162
#1  0x00007ffff4eeb858 in DcgmNs::DcgmNvSwitchManager::UpdateFields<unsigned long, DcgmNs::FieldIdStorageType<(unsigned short)863>, false, nscq_uuid_t*, unsigned char>(unsigned short, DcgmFvBuffer&, std::vector<dcgm_field_update_info_t, std::allocator<dcgm_field_update_info_t> > const&, long)::{lambda(nscq_uuid_t*, unsigned char, signed char, unsigned long, DcgmNs::NscqDataCollector<DcgmNs::TempData<unsigned long, DcgmNs::FieldIdStorageType<(unsigned short)863>, false, nscq_uuid_t*, unsigned char> >*)#1}::_FUN(nscq_uuid_t*, unsigned char, signed char, unsigned long, DcgmNs::NscqDataCollector<DcgmNs::TempData<unsigned long, DcgmNs::FieldIdStorageType<(unsigned short)863>, false, nscq_uuid_t*, unsigned char> >*) () at /srv/DCGM/modules/nvswitch/FieldDefinitions.cpp:138
#2  0x00007ffff4b9b456 in ?? () from /lib/x86_64-linux-gnu/libnvidia-nscq.so.2
#3  0x00007ffff4b4c0a3 in ?? () from /lib/x86_64-linux-gnu/libnvidia-nscq.so.2
#4  0x00007ffff4b4b6bf in ?? () from /lib/x86_64-linux-gnu/libnvidia-nscq.so.2
#5  0x00007ffff4b54b80 in nscq_session_path_observe () from /lib/x86_64-linux-gnu/libnvidia-nscq.so.2
#6  0x00007ffff4f636ca in nscq_session_path_observe (session=0x7681b0, path=0x7ffff4fed8d0 <nscq_nvswitch_phys_id> "/{nvswitch}/id/phys_id", callback=0x7ffff4eeb813 <DcgmNs::DcgmNvSwitchManager::UpdateFields<unsigned long, DcgmNs::FieldIdStorageType<(unsigned short)863>, false, nscq_uuid_t*, unsigned char>(unsigned short, DcgmFvBuffer&, std::vector<dcgm_field_update_info_t, std::allocator<dcgm_field_update_info_t> > const&, long)::{lambda(nscq_uuid_t*, unsigned char, signed char, unsigned long, DcgmNs::NscqDataCollector<DcgmNs::TempData<unsigned long, DcgmNs::FieldIdStorageType<(unsigned short)863>, false, nscq_uuid_t*, unsigned char> >*)#1}::_FUN(nscq_uuid_t*, unsigned char, signed char, unsigned long, DcgmNs::NscqDataCollector<DcgmNs::TempData<unsigned long, DcgmNs::FieldIdStorageType<(unsigned short)863>, false, nscq_uuid_t*, unsigned char> >*)>, data=0x7ffff4afb280, flags=0) at /srv/DCGM/sdk/nvidia/nscq/dlwrap/dlwrap.c:131
#7  0x00007ffff4eeb98d in DcgmNs::DcgmNvSwitchManager::UpdateFields<unsigned long, DcgmNs::FieldIdStorageType<(unsigned short)863>, false, nscq_uuid_t*, unsigned char> (this=0x53cb10, fieldId=863, buf=..., entities=std::vector of length 1, capacity 1 = {...}, now=1712069504430580) at /srv/DCGM/modules/nvswitch/FieldDefinitions.cpp:167
#8  0x00007ffff4ec28a5 in DcgmNs::DcgmNvSwitchManager::UpdateFields (this=0x53cb10, nextUpdateTime=@0x7ffff4afb528: 1712069518487312) at /srv/DCGM/modules/nvswitch/DcgmNvSwitchManager.cpp:592
#9  0x00007ffff4ea9b6a in DcgmNs::DcgmModuleNvSwitch::RunOnce (this=0x53c970) at /srv/DCGM/modules/nvswitch/DcgmModuleNvSwitch.cpp:400
#10 0x00007ffff4ea9d6d in DcgmNs::DcgmModuleNvSwitch::TryRunOnce (this=0x53c970, forceRun=true) at /srv/DCGM/modules/nvswitch/DcgmModuleNvSwitch.cpp:419
#11 0x00007ffff4ea8428 in operator() (__closure=0x7fffd4036cf0) at /srv/DCGM/modules/nvswitch/DcgmModuleNvSwitch.cpp:273
#12 0x00007ffff4eaadae in std::__invoke_impl<void, DcgmNs::DcgmModuleNvSwitch::ProcessMessageFromTaskRunner(dcgm_module_command_header_t*)::<lambda()>&>(std::__invoke_other, struct {...} &) (__f=...) at /opt/cross/x86_64-linux-gnu/include/c++/11.2.0/bits/invoke.h:61
#13 0x00007ffff4eaabdb in std::__invoke_r<void, DcgmNs::DcgmModuleNvSwitch::ProcessMessageFromTaskRunner(dcgm_module_command_header_t*)::<lambda()>&>(struct {...} &) (__fn=...) at /opt/cross/x86_64-linux-gnu/include/c++/11.2.0/bits/invoke.h:111
#14 0x00007ffff4eaa937 in std::_Function_handler<void(), DcgmNs::DcgmModuleNvSwitch::ProcessMessageFromTaskRunner(dcgm_module_command_header_t*)::<lambda()> >::_M_invoke(const std::_Any_data &) (__functor=...) at /opt/cross/x86_64-linux-gnu/include/c++/11.2.0/bits/std_function.h:291
#15 0x00007ffff4ebb3f4 in std::function<void ()>::operator()() const (this=0x7fffd4036cf0) at /opt/cross/x86_64-linux-gnu/include/c++/11.2.0/bits/std_function.h:560
#16 0x00007ffff4eb92ad in std::__invoke_impl<void, std::function<void ()> const&>(std::__invoke_other, std::function<void ()> const&) (__f=...) at /opt/cross/x86_64-linux-gnu/include/c++/11.2.0/bits/invoke.h:61
#17 0x00007ffff4eb646b in std::__invoke<std::function<void ()> const&>(std::function<void ()> const&) (__fn=...) at /opt/cross/x86_64-linux-gnu/include/c++/11.2.0/bits/invoke.h:96
#18 0x00007ffff4eb1267 in std::invoke<std::function<void ()> const&>(std::function<void ()> const&) (__fn=...) at /opt/cross/x86_64-linux-gnu/include/c++/11.2.0/functional:97
#19 0x00007ffff4eada36 in DcgmNs::Task<void>::Task(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::function<void ()>)::{lambda()#1}::operator()() const (__closure=0x7fffd4036cf0) at /srv/DCGM/common/Task.hpp:215
#20 0x00007ffff4ebb46a in std::__invoke_impl<int, DcgmNs::Task<void>::Task(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::function<void ()>)::{lambda()#1}&>(std::__invoke_other, DcgmNs::Task<void>::Task(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::function<void ()>)::{lambda()#1}&) (__f=...) at /opt/cross/x86_64-linux-gnu/include/c++/11.2.0/bits/invoke.h:61
#21 0x00007ffff4eb9474 in std::__invoke_r<std::optional<int>, DcgmNs::Task<void>::Task(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::function<void ()>)::{lambda()#1}&>(std::optional<int>&&, (DcgmNs::Task<void>::Task(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::function<void ()>)::{lambda()#1}&)...) (__fn=...) at /opt/cross/x86_64-linux-gnu/include/c++/11.2.0/bits/invoke.h:114
#22 0x00007ffff4eb6538 in std::_Function_handler<std::optional<int> (), DcgmNs::Task<void>::Task(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::function<void ()>)::{lambda()#1}>::_M_invoke(std::_Any_data const&) (__functor=...) at /opt/cross/x86_64-linux-gnu/include/c++/11.2.0/bits/std_function.h:291
#23 0x00007ffff4ec08da in std::function<std::optional<int> ()>::operator()() const (this=0x76bdf0) at /opt/cross/x86_64-linux-gnu/include/c++/11.2.0/bits/std_function.h:560
#24 0x00007ffff4ec0522 in std::__invoke_impl<std::optional<int>, std::function<std::optional<int> ()>&>(std::__invoke_other, std::function<std::optional<int> ()>&) (__f=...) at /opt/cross/x86_64-linux-gnu/include/c++/11.2.0/bits/invoke.h:61
#25 0x00007ffff4ec028e in std::__invoke<std::function<std::optional<int> ()>&>(std::function<std::optional<int> ()>&) (__fn=...) at /opt/cross/x86_64-linux-gnu/include/c++/11.2.0/bits/invoke.h:96
#26 0x00007ffff4ebffd0 in std::invoke<std::function<std::optional<int> ()>&>(std::function<std::optional<int> ()>&) (__fn=...) at /opt/cross/x86_64-linux-gnu/include/c++/11.2.0/functional:97
#27 0x00007ffff4ebfc4f in DcgmNs::NamedBasicTask<int, void>::Run (this=0x76bde0) at /srv/DCGM/common/Task.hpp:155
#28 0x00007ffff4eaeca9 in DcgmNs::TaskRunner::Run (this=0x53ca58, oneIteration=true) at /srv/DCGM/common/TaskRunner.hpp:432
#29 0x00007ffff4ea9e2c in DcgmNs::DcgmModuleNvSwitch::run (this=0x53c970) at /srv/DCGM/modules/nvswitch/DcgmModuleNvSwitch.cpp:433
#30 0x00007ffff4f6bba4 in DcgmThread::RunInternal (this=0x53c9b8) at /srv/DCGM/common/DcgmThread/DcgmThread.cpp:308
#31 0x00007ffff4f6a7c5 in dcgmthread_starter (parm=0x53c9b8) at /srv/DCGM/common/DcgmThread/DcgmThread.cpp:34
#32 0x00007ffff7bfa609 in start_thread () from /lib/x86_64-linux-gnu/libpthread.so.0
#33 0x00007ffff79af353 in clone () from /lib/x86_64-linux-gnu/libc.so.6
```

</details>

2. From that we would expect [`fieldId` to be `863`](https://github.com/NVIDIA/DCGM/blob/18b87c715750d0d44b185dfeb9a7d8e2597443a4/dcgmlib/dcgm_fields.h#L1765), but it is proabbly garbage:  "32767"

<details><summary>gdb debug output for `*dest`: strange stuff</summary>

```
Thread 5 "nv-hostengine" hit Breakpoint 2, DcgmNs::DcgmNvSwitchManager::UpdateFields<unsigned long, DcgmNs::FieldIdStorageType<(unsigned short)863>, false, nscq_uuid_t*, unsigned char>(unsigned short, DcgmFvBuffer&, std::vector<dcgm_field_update_info_t, std::allocator<dcgm_field_update_info_t> > const&, long)::{lambda(nscq_uuid_t*, unsigned char, signed char, unsigned long, DcgmNs::NscqDataCollector<DcgmNs::TempData<unsigned long, DcgmNs::FieldIdStorageType<(unsigned short)863>, false, nscq_uuid_t*, unsigned char> >*)#1}::operator()(nscq_uuid_t*, unsigned char, signed char, unsigned long, DcgmNs::NscqDataCollector<DcgmNs::TempData<unsigned long, DcgmNs::FieldIdStorageType<(unsigned short)863>, false, nscq_uuid_t*, unsigned char> >*) const (__closure=0x0, indicies#0=0x564ef0, indicies#1=0 '\000', rc=11 '\v', in=140737298543232, dest=0x716a20) at /srv/DCGM/modules/nvswitch/FieldDefinitions.cpp:162
162	        TempData<nscqFieldType, storageType, is_vector, indexTypes...> item;
$65 = {
  callCounter = 4108821041,
  fieldId = 32767,
  nscqPath = 0x712960 "SWX-F8F7054E-5993-EB8D-786D-B59D5303DB16",
  data = std::vector of length 0, capacity -1
}
```

</details>

  The `callCounter` looks goofy, too.
  Most important, the `nscqPath` is _not_ the expected `"/{nvswitch}/id/phys_id"` but rather the value?
  
-=-=-=-

It seem that there's something wrong in my `/usr/lib/x86_64-linux-gnu/libnvidia-nscq.so.2`, because it looks like the library is just calling this with
broken info.

Lib info:
<details><summary>apt policy libnvidia-nscq-535</summary>

``` 
libnvidia-nscq-535:
  Installed: 535.154.05-0ubuntu0.20.04.1
  Candidate: 535.161.07-0ubuntu0.20.04.1
  Version table:
     535.161.08-1 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     535.161.07-1 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     535.161.07-0ubuntu0.20.04.1 600
        500 http://de.archive.ubuntu.com/ubuntu focal-updates/multiverse amd64 Packages
        500 http://security.ubuntu.com/ubuntu focal-security/multiverse amd64 Packages
     535.154.05-1 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
 *** 535.154.05-0ubuntu0.20.04.1 100
        100 /var/lib/dpkg/status
     535.129.03-1 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     535.104.12-1 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     535.104.05-1 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     535.86.10-1 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
     535.54.03-1 580
        580 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
```

</details>

-----------

So the promblem is probably _not_ DCGM but rahter lib NSCQ?

### superg · 2024-04-04

Hi, thank you for the details!
Let me process this information and get back to you.

### superg · 2024-04-10

@krono , I apologize for the long wait. We've managed to reproduce the issue on our side. While our call stack is different, the source of the problem is very likely to be the same and your observations on std::vector<> with garbage supports it. I believe that the fix that we're working on will resolve it.

### krono · 2024-04-11

thanks :)

### krono · 2024-05-13

Hi @superg , any news or any place I can read up on the issue here?

### superg · 2024-05-15

Hi @krono,
We have an internal tracking ticket for this issue and an assigned developer, this is still work in progress.

The issue is with the callback signature (after all the template instantiations), we use:
`void callback(const nscq_uuid_t* device, nscq_rc_t rc, std::vector<nscq_error_t>, void *data)`
whereas NSCQ expects:
`void callback(const nscq_uuid_t* device, nscq_rc_t rc, const nscq_error_t error, void* data)`
for a given path type.
Callback code has to be rewritten for the second signature.

### krono · 2024-05-15

oh my. 

Which component will need updat? DCGM or NSCQ?

### superg · 2024-05-15

That's in DCGM.

### krono · 2024-05-15

Thanks! I'll keep watching this space

### krono · 2024-06-05

I have now a second machine that fell victim to that problem:
HGX-Bases system, similarly configured.


### krono · 2024-07-01

Hey, any news?

### superg · 2024-07-01

@krono, the issue is identified and we are working on a fix. The current ETA is August.

### krono · 2024-09-10

@superg Is this included in #189 or #180 ?

### krono · 2024-09-11

To answer my own question: NO.

### krono · 2024-09-27

@superg any news?

### superg · 2024-09-27

Hi @krono ,
I'm sorry I moved to another project some time ago, I will enquire.

### krono · 2024-10-07

@dshaiknvidia Do you know somethinge about this?

### superg · 2024-10-21

@krono, can you please replace UpdateNvSwitchVectorFieldType with UpdateNvSwitchScalarFieldType in:
https://github.com/NVIDIA/DCGM/blob/master/modules/nvswitch/FieldDefinitions.h#L235
and:
https://github.com/NVIDIA/DCGM/blob/master/modules/nvswitch/FieldDefinitions.h#L257

Recompile and see if it fixes the issue?


### krono · 2024-10-25

Hi, no that does not help.
```
          PID: 594197 (nv-hostengine)
           UID: 0 (root)
           GID: 0 (root)
        Signal: 11 (SEGV)
     Timestamp: Fri 2024-10-25 16:09:44 CEST (3min 18s ago)
  Command Line: ./nv-hostengine -n --service-account nvidia-dcgm
    Executable: /root/src/DCGM/_out/Linux-amd64-release/bin/nv-hostengine
 Control Group: /system.slice/ssh.service
          Unit: ssh.service
         Slice: system.slice
       Boot ID: 29946ddac20b47daad75d76a4a42d326
    Machine ID: 5b05d12040d24d8e9c8d38117ab12eba
      Hostname: gx01
       Storage: /var/lib/systemd/coredump/core.nv-hostengine.0.29946ddac20b47daad75d76a4a42d326.594197.1729865384000000000000.lz4
       Message: Process 594197 (nv-hostengine) of user 0 dumped core.

                Stack trace of thread 594206:
                #0  0x00007f9088d49272 n/a (/root/src/DCGM/_out/Linux-amd64-release/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x59272)
                #1  0x00007f9088a044a6 n/a (libnvidia-nscq.so.2 + 0x9d4a6)
                #2  0x00007f90889b50f3 n/a (libnvidia-nscq.so.2 + 0x4e0f3)
                #3  0x00007f90889b470f n/a (libnvidia-nscq.so.2 + 0x4d70f)
                #4  0x00007f90889bdbd0 nscq_session_path_observe (libnvidia-nscq.so.2 + 0x56bd0)
                #5  0x00007f9088d923c7 n/a (/root/src/DCGM/_out/Linux-amd64-release/lib/libdcgmmodulenvswitch.so.3.3.8 + 0xa23c7)
                #6  0x00007f9088d5f15f n/a (/root/src/DCGM/_out/Linux-amd64-release/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x6f15f)
                #7  0x00007f9088d2a19d n/a (/root/src/DCGM/_out/Linux-amd64-release/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x3a19d)
                #8  0x00007f9088d15e9f n/a (/root/src/DCGM/_out/Linux-amd64-release/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x25e9f)
                #9  0x00007f9088d16834 n/a (/root/src/DCGM/_out/Linux-amd64-release/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x26834)
                #10 0x00007f9088d19fd8 n/a (/root/src/DCGM/_out/Linux-amd64-release/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x29fd8)
                #11 0x00007f9088d1b4a4 n/a (/root/src/DCGM/_out/Linux-amd64-release/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x2b4a4)
                #12 0x00007f9088d233b6 n/a (/root/src/DCGM/_out/Linux-amd64-release/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x333b6)
                #13 0x00007f9088d19bb1 n/a (/root/src/DCGM/_out/Linux-amd64-release/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x29bb1)
                #14 0x00007f9088da113b n/a (/root/src/DCGM/_out/Linux-amd64-release/lib/libdcgmmodulenvswitch.so.3.3.8 + 0xb113b)
                #15 0x00007f9088da1689 n/a (/root/src/DCGM/_out/Linux-amd64-release/lib/libdcgmmodulenvswitch.so.3.3.8 + 0xb1689)
                #16 0x00007f908b9ba609 start_thread (libpthread.so.0 + 0x8609)
                #17 0x00007f908b76f353 __clone (libc.so.6 + 0x11f353)

                Stack trace of thread 594197:
                #0  0x00007f908b72d23f clock_nanosleep (libc.so.6 + 0xdd23f)
                #1  0x00007f908b732ec7 __nanosleep (libc.so.6 + 0xe2ec7)
                #2  0x000000000040736b n/a (/root/src/DCGM/_out/Linux-amd64-release/bin/nv-hostengine + 0x736b)
                #3  0x00007f908b674083 __libc_start_main (libc.so.6 + 0x24083)
                #4  0x00000000004079bc n/a (/root/src/DCGM/_out/Linux-amd64-release/bin/nv-hostengine + 0x79bc)
```

### superg · 2024-10-25

Huh, maybe the root cause for your situation is different then. I will try to reproduce it on our side.

### krono · 2024-10-25

Am 25. Oktober 2024 16:30:45 MESZ schrieb Hennadiy Brych ***@***.***>:
>Huh, maybe the root cause for your situation is different then. I will try to reproduce it on our side.
>

maybe i didn't do it right, I'll try one more time
-- 
Sent from a mobile device


### superg · 2024-10-25

It would be nice if you could build a debug version so we see a full stack trace and in this case I could also check your core dump if you share it.

### krono · 2024-10-25

<details>
<summary>dump</summary>

```
          PID: 725475 (nv-hostengine)
           UID: 0 (root)
           GID: 0 (root)
        Signal: 11 (SEGV)
     Timestamp: Fri 2024-10-25 17:52:21 CEST (3min 9s ago)
  Command Line: bin/nv-hostengine -n --service-account nvidia-dcgm
    Executable: /root/src/DCGM/_out/Linux-amd64-debug/bin/nv-hostengine
 Control Group: /system.slice/ssh.service
          Unit: ssh.service
         Slice: system.slice
       Boot ID: 29946ddac20b47daad75d76a4a42d326
    Machine ID: 5b05d12040d24d8e9c8d38117ab12eba
      Hostname: gx01
       Storage: /var/lib/systemd/coredump/core.nv-hostengine.0.29946ddac20b47daad75d76a4a42d326.725475.1729871541000000000000.lz4
       Message: Process 725475 (nv-hostengine) of user 0 dumped core.

                Stack trace of thread 725483:
                #0  0x00007f676f0fc68a n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x8668a)
                #1  0x00007f676f0fc6d5 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x866d5)
                #2  0x00007f676f0f0d6a n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x7ad6a)
                #3  0x00007f676f0e8d56 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x72d56)
                #4  0x00007f676f0da751 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x64751)
                #5  0x00007f676f0da7c4 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x647c4)
                #6  0x00007f676ed8a4a6 n/a (libnvidia-nscq.so.2 + 0x9d4a6)
                #7  0x00007f676ed3b0f3 n/a (libnvidia-nscq.so.2 + 0x4e0f3)
                #8  0x00007f676ed3a70f n/a (libnvidia-nscq.so.2 + 0x4d70f)
                #9  0x00007f676ed43bd0 nscq_session_path_observe (libnvidia-nscq.so.2 + 0x56bd0)
                #10 0x00007f676f15256c n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0xdc56c)
                #11 0x00007f676f0da8f9 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x648f9)
                #12 0x00007f676f0b18a5 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x3b8a5)
                #13 0x00007f676f098b6a n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x22b6a)
                #14 0x00007f676f098d6d n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x22d6d)
                #15 0x00007f676f097428 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x21428)
                #16 0x00007f676f099dae n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x23dae)
                #17 0x00007f676f099bdb n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x23bdb)
                #18 0x00007f676f099937 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x23937)
                #19 0x00007f676f0aa3f4 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x343f4)
                #20 0x00007f676f0a82ad n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x322ad)
                #21 0x00007f676f0a546b n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x2f46b)
                #22 0x00007f676f0a0267 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x2a267)
                #23 0x00007f676f09ca36 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x26a36)
                #24 0x00007f676f0aa46a n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x3446a)
                #25 0x00007f676f0a8474 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x32474)
                #26 0x00007f676f0a5538 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x2f538)
                #27 0x00007f676f0af8da n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x398da)
                #28 0x00007f676f0af522 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x39522)
                #29 0x00007f676f0af28e n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x3928e)
                #30 0x00007f676f0aefd0 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x38fd0)
                #31 0x00007f676f0aec4f n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x38c4f)
                #32 0x00007f676f09dca9 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x27ca9)
                #33 0x00007f676f098e2c n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x22e2c)
                #34 0x00007f676f15aa46 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0xe4a46)
                #35 0x00007f676f159667 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0xe3667)
                #36 0x00007f67725eb609 start_thread (libpthread.so.0 + 0x8609)
                #37 0x00007f67723a0353 __clone (libc.so.6 + 0x11f353)

                Stack trace of thread 725477:
                #0  0x00007f677239995d syscall (libc.so.6 + 0x11895d)
                #1  0x00007f676f1a59f9 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x12f9f9)
                #2  0x00007f676f0a4cf5 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x2ecf5)
                #3  0x00007f676f09c228 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x26228)
                #4  0x00007f676f0a697d n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x3097d)
                #5  0x00007f676f0a22c2 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x2c2c2)
                #6  0x00007f676f097336 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x21336)
                #7  0x00007f676f11d098 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0xa7098)
                #8  0x00007f676f098fd7 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgmmodulenvswitch.so.3.3.8 + 0x22fd7)
                #9  0x00007f6772749997 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x131997)
                #10 0x00007f677274679e n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x12e79e)
                #11 0x00007f6772645f86 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x2df86)
                #12 0x00007f6772652f90 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x3af90)
                #13 0x00007f677265207c n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x3a07c)
                #14 0x00007f677274f5fa n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1375fa)
                #15 0x00007f67727e7ce3 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1cfce3)
                #16 0x00007f67727e107e n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1c907e)
                #17 0x00007f67727e0682 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1c8682)
                #18 0x00007f67727e0a5b n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1c8a5b)
                #19 0x00007f6772749997 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x131997)
                #20 0x00007f677274679e n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x12e79e)
                #21 0x00007f6772746bd3 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x12ebd3)
                #22 0x00007f6772746e27 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x12ee27)
                #23 0x00007f6772746fe5 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x12efe5)
                #24 0x00007f677273569e n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x11d69e)
                #25 0x00007f6772733815 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x11b815)
                #26 0x00007f6772731a21 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x119a21)
                #27 0x00007f67728083a1 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1f03a1)
                #28 0x00007f677280032f n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1e832f)
                #29 0x00007f677280054e n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1e854e)
                #30 0x00007f67728039ac n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1eb9ac)
                #31 0x00007f67728037c9 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1eb7c9)
                #32 0x00007f677280360e n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1eb60e)
                #33 0x00007f6772800586 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1e8586)
                #34 0x00007f6772804032 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1ec032)
                #35 0x00007f6772803ded n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1ebded)
                #36 0x00007f6772803b96 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1ebb96)
                #37 0x00007f677280dc20 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1f5c20)
                #38 0x00007f677280b793 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1f3793)
                #39 0x00007f6772808d60 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1f0d60)
                #40 0x00007f6772805d7e n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1edd7e)
                #41 0x00007f677280488a n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1ec88a)
                #42 0x00007f677280dd66 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1f5d66)
                #43 0x00007f677280b956 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1f3956)
                #44 0x00007f6772808f60 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1f0f60)
                #45 0x00007f677281339c n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1fb39c)
                #46 0x00007f6772813305 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1fb305)
                #47 0x00007f677281326d n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1fb26d)
                #48 0x00007f67728131bd n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1fb1bd)
                #49 0x00007f67728130a3 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1fb0a3)
                #50 0x00007f677267fa81 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x67a81)
                #51 0x00007f6772804f7e n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1ecf7e)
                #52 0x00007f6772804dd3 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1ecdd3)
                #53 0x00007f6772813367 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1fb367)
                #54 0x00007f67728132e2 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1fb2e2)
                #55 0x00007f677281323c n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1fb23c)
                #56 0x00007f677281319a n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1fb19a)
                #57 0x00007f6772813068 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x1fb068)
                #58 0x00007f67728bbd14 n/a (/root/src/DCGM/_out/Linux-amd64-debug/lib/libdcgm.so.3.3.8 + 0x2a3d14)
```

</details>

I think the error is the same as last time.

Where could I put the coredump?


### superg · 2024-10-28

I think you can zip it and attach directly to the ticket. There might be file size limit though.
Let me know if that doesn't work.

### krono · 2024-11-04

Hey, I was on vacation. Here's the core dump, zip-compressed
[core_d.zip](https://github.com/user-attachments/files/17616851/core_d.zip)


### krono · 2024-11-15

Hi, I saw 3.3.9 shipped.
I tired it and it died again. here's a fresh dump, but not from a debug build, since apparenlty the 3.3.9 sources are not here yet?

[dcgm_3.3.9_2024-11-15.dump.zip](https://github.com/user-attachments/files/17772444/dcgm_3.3.9_2024-11-15.dump.zip)



### krono · 2024-11-15

Btw: this is the `--collectors` file im using to trigger the problem:

```csv
DCGM_FI_DEV_NVSWITCH_TEMPERATURE_CURRENT, gauge, NVSwitch current temperature (in C)
DCGM_FI_DEV_NVSWITCH_THROUGHPUT_TX, counter,NVSwitch throughput Tx.
DCGM_FI_DEV_NVSWITCH_THROUGHPUT_RX, counter,NVSwitch throughput Rx.
DCGM_FI_DEV_NVSWITCH_PHYS_ID, label, NVSwitch Physical ID
DCGM_FI_DEV_NVSWITCH_LINK_ID, label, NvSwitch NvLink ID
DCGM_FI_DEV_NVSWITCH_LINK_THROUGHPUT_TX, counter, NVSwitch Tx Throughput Counter for ports 0-17
DCGM_FI_DEV_NVSWITCH_LINK_THROUGHPUT_RX, counter,  NVSwitch Rx Throughput Counter for ports 0-17.
DCGM_FI_DEV_NVSWITCH_LINK_FATAL_ERRORS, counter, NvSwitch fatal_errors for ports 0-17.
DCGM_FI_DEV_NVSWITCH_LINK_NON_FATAL_ERRORS, counter, NvSwitch non_fatal_errors for ports 0-17.
DCGM_FI_DEV_NVSWITCH_LINK_REPLAY_ERRORS, counter, NvSwitch replay_count_errors for ports 0-17.
DCGM_FI_DEV_NVSWITCH_LINK_RECOVERY_ERRORS, counter,NvSwitch recovery_count_errors for ports 0-17.
DCGM_FI_DEV_NVSWITCH_LINK_FLIT_ERRORS, counter, NvSwitch filt_err_count_errors for ports 0-17.
DCGM_FI_DEV_NVSWITCH_LINK_CRC_ERRORS, counter, NvLink lane_crs_err_count_aggregate_errors for ports 0-17.
DCGM_FI_DEV_NVSWITCH_LINK_ECC_ERRORS, counter, NvLink lane ecc_err_count_aggregate_errors for ports 0-17.
```

### krono · 2025-01-09

Hi I see 4.0.0 shipped.
is this fixed?

### superg · 2025-01-15

Hi @krono ,
I'm sorry I was on a long vacation and right now is busy with another project. Depending on my availability I might check this out later.


### krono · 2025-01-16

Yeah I see this is making less and less sense for me.
DCGM is getting more and more in our way than it is helping us.

I'll close this, you can track that internally, the reproducer is above :)
@superg thanks for taking care and I hope you had a great holiday.
