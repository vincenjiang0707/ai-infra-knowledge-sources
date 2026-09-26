# [Issue #2118] [Feature]: Enable RCCL on Strix Halo gfx1151

source: https://github.com/ROCm/rccl/issues/2118
state: closed | updated: 2026-01-22T02:06:48Z
labels: 

## 正文

### Suggestion Description

Hello I have been working with lemonade-server pushing some small changes and fixes. I would like to implement a rccl plugin for thunderbolt 5 / usb4 v2, I have done some initial driver and plugin setup and I need to do a lot of other stuff but I would like to run some tests. on a gfx1151. Can you get rccl enabled for the gfx1151 for being able to use rccl to distribute load for applications such as llamacpp and lemonade-server

https://github.com/Geramy/OdinLink-Five

### Operating System

Ubuntu

### GPU

GFX1151

### ROCm Component

rccl

## 评论 (4)

### manhalt · 2026-01-10

Did you see this PR: https://github.com/ROCm/rccl/pull/2075 - it seems this will make it work. Had a quick check on your TB5 plugin and was wondering what HW you use that on? I tried TB networking on Framework Desktop, but it seems to be limited to 10 GB/s

### Geramy · 2026-01-10

@manhalt you could try to use TB4 or USB4 which should have a macimum rate of i believe 40gbps and that will still be faster with less overhead than thunderbolt-net also the device I have I picked because it had TB5 / USB4 v2 they just cant call it TB5 but it is the intel chip. MINISFORUM MS-S1 is the equipment I have. Once im done running tests i will be adding features to the driver for now it's a basic driver device to device style operation. I could have sworn the only difference between TB4 and 5 was bandwidth and dynamic channel TX/RX but I'll look later if you want to test over TB4 and make any changes necessary.

> Did you see this PR: https://github.com/ROCm/rccl/pull/2075 - it seems this will make it work. Had a quick check on your TB5 plugin and was wondering what HW you use that on? I tried TB networking on Framework Desktop, but it seems to be limited to 10 GB/s



### systems-assistant[bot] · 2026-01-22

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/2788

### ammallya · 2026-01-22

Imported to ROCm/rocm-systems
