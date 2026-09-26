# [Issue #38] [Issue]: Incorrect Energy Consumption Reported by amdsmi_get_energy_count() Method

source: https://github.com/ROCm/amdsmi/issues/38
state: open | updated: 2026-06-03T12:09:22Z
labels: Under Investigation

## 正文

### Problem Description

## Issue with `amdsmi.amdsmi_get_energy_count()` Method

### Description
When using the `amdsmi.amdsmi_get_energy_count()` method, the change in total energy consumption reported in Joules is much less than what it should be. This is evident when using the AMDSMI CLI tool to query the total energy consumption.

### Observed Behavior
When running `amd-smi metric -pE`, the output is as follows:

GPU: 0
    POWER:
        SOCKET_POWER: 35 W
        GFX_VOLTAGE: N/A mV
        SOC_VOLTAGE: N/A mV
        MEM_VOLTAGE: N/A mV
        POWER_MANAGEMENT: ENABLED
        THROTTLE_STATUS: UNTHROTTLED
    ENERGY:
        TOTAL_ENERGY_CONSUMPTION: 16.43 J
...

After waiting for one second and retrying:

GPU: 0
    POWER:
        SOCKET_POWER: 35 W
        GFX_VOLTAGE: N/A mV
        SOC_VOLTAGE: N/A mV
        MEM_VOLTAGE: N/A mV
        POWER_MANAGEMENT: ENABLED
        THROTTLE_STATUS: UNTHROTTLED
    ENERGY:
        TOTAL_ENERGY_CONSUMPTION: 16.43 J
...

### Expected Behavior
This does not make sense. The formula  E = P * t  means that the total energy consumption should have increased by ~35J after one second. But it does not seem to change.

### Operating System

NAME="Rocky Linux", VERSION="9.1 (Blue Onyx)"

### CPU

AMD EPYC 7V13 64-Core Processor

### GPU

AMD Instinct MI100

### ROCm Version

ROCm 6.1.0

### ROCm Component

amdsmi

### Steps to Reproduce

This shell script can help replicate the issue. It runs `amd-smi metric` and waits 5 seconds:

```bash
#!/bin/bash

# Function to get the total energy consumption of GPU 0
get_energy_consumption() {
    amd-smi metric -pE | awk '/GPU: 0/,/GPU: 1/ { if ($1 == "TOTAL_ENERGY_CONSUMPTION:") print $2 }'
}

# Function to get the socket power of GPU 0
get_socket_power() {
    amd-smi metric -pE | awk '/GPU: 0/,/GPU: 1/ { if ($1 == "SOCKET_POWER:") print $2 }'
}

# Get the initial energy consumption of GPU 0
initial_energy=$(get_energy_consumption)

# Get the socket power of GPU 0
socket_power=$(get_socket_power)

# Wait for five seconds
sleep 5

# Get the energy consumption of GPU 0 after five seconds
final_energy=$(get_energy_consumption)

# Calculate the difference in energy consumption
energy_difference=$(echo "$final_energy - $initial_energy" | bc)

# Calculate the expected energy consumption over five seconds
expected_energy_consumption=$(echo "$socket_power * 5" | bc)

# Print the initial, final, and difference in energy consumption, and expected energy consumption
echo "Initial energy consumed by GPU 0: $initial_energy J"
echo "Final energy consumed by GPU 0: $final_energy J"
echo "Energy consumed by GPU 0 in the last five seconds: $energy_difference J"
echo "Expected energy consumption in last 5 seconds: $expected_energy_consumption J"
```

With my output being:
Initial energy consumed by GPU 0: 19.748 J
Final energy consumed by GPU 0: 19.748 J
Energy consumed by GPU 0 in the last five seconds: 0 J
Expected energy consumption in last 5 seconds: 160 J


### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

We are using the [AMD HPC cluster](https://amdresearch.github.io/hpcfund/).

## 评论 (28)

### marifamd · 2024-06-10

@parthraut Can you give me the output of `amd-smi version`. 

I believe that https://github.com/ROCm/amdsmi/issues/22 sees the same thing. We had an issue with updating our internal tables within the same instance of amd-smi. If that is the case the 6.1.X branch has this fix.

### parthraut · 2024-06-10

$ amd-smi version
AMDSMI Tool: 24.5.1+c5106a9 | AMDSMI Library version: 24.5.2.0 | ROCm version: 6.1.2

### jaywonchung · 2024-06-10

To chime in, this happens when the GPU is idle -- the energy counter does not change at all.
On the other hand, when I'm running compute on the GPU, the energy counter will actually increase (in both the Python interface and `amd-smi`), but at an extremely slow rate. I feel like the unit of `counter_resolution` field could be wrong.

(The issue reported by #22 was mostly resolved by the update to ROCm 6.1.2. Especially, the `average_socket_power` field updates correctly and we can measure energy by sampling it repetitively and integrating over time. But we also wanted to get the energy counter working.)

### jaywonchung · 2024-07-11

Hi @marifamd, I was wondering about the status of this issue. Will this be fixed on the next ROCm version?

### jaywonchung · 2024-08-03

I just discovered that with the same ROCm and amd-smi versions, energy counters work correctly on MI210 and MI250 GPUs, whereas the exact same amdsmi script doesn't work on MI100. So I think this is a not an issue of amd-smi or rocm-smi. Then would this be a ROCm problem? Or are there more layers in between? @marifamd 

### marifamd · 2024-08-06

@jaywonchung You are correct, thanks for the debug support. 

@parthraut We will look into this with our driver team and reach back out, I'm not seeing these issues on mi200, mi210 nor mi300X.

This is how the expected output should look:

```
$ amd-smi static --asic --gpu 0 1
GPU: 0
    ASIC:
        MARKET_NAME: Aldebaran/MI200 [Instinct MI210
        VENDOR_ID: 0x1002
        VENDOR_NAME: Advanced Micro Devices Inc. [AMD/ATI]
        SUBVENDOR_ID: 0x1002
        DEVICE_ID: 0x740f
        REV_ID: 0x2
        ASIC_SERIAL: 0xXXXXXXXXXXXXXX
        OAM_ID: 1

GPU: 1
    ASIC:
        MARKET_NAME: Instinct MI210
        VENDOR_ID: 0x1002
        VENDOR_NAME: Advanced Micro Devices Inc. [AMD/ATI]
        SUBVENDOR_ID: 0x1002
        DEVICE_ID: 0x740f
        REV_ID: 0x2
        ASIC_SERIAL: 0xXXXXXXXXXXXXXX
        OAM_ID: 0


$ amd-smi metric -E -w 1 --gpu 0 1 --csv
'CTRL' + 'C' to stop watching output:
timestamp,gpu,total_energy_consumption
1722959154,0,20909145.914
1722959154,1,21111595.33

timestamp,gpu,total_energy_consumption
1722959155,0,20909188.578
1722959155,1,21111638.458

timestamp,gpu,total_energy_consumption
1722959156,0,20909231.286
1722959156,1,21111681.647

timestamp,gpu,total_energy_consumption
1722959157,0,20909273.989
1722959157,1,21111724.835
```


### jaywonchung · 2024-08-06

Yep, our output on MI210 are as expected:

```
$ amd-smi version
AMDSMI Tool: 24.5.1+c5106a9 | AMDSMI Library version: 24.5.2.0 | ROCm version: 6.1.2

$ amd-smi static --asic
GPU: 0
    ASIC:
        MARKET_NAME: Instinct MI210
        VENDOR_ID: 0x1002
        VENDOR_NAME: Advanced Micro Devices Inc. [AMD/ATI]
        SUBVENDOR_ID: 0x1002
        DEVICE_ID: 0x740f
        REV_ID: 0x2
        ASIC_SERIAL: REDACTED
        OAM_ID: N/A

GPU: 1
    ASIC:
        MARKET_NAME: Instinct MI210
        VENDOR_ID: 0x1002
        VENDOR_NAME: Advanced Micro Devices Inc. [AMD/ATI]
        SUBVENDOR_ID: 0x1002
        DEVICE_ID: 0x740f
        REV_ID: 0x2
        ASIC_SERIAL: REDACTED
        OAM_ID: N/A

$ amd-smi metric -E -w 1 --gpu 0 1 --csv
'CTRL' + 'C' to stop watching output:
timestamp,gpu,total_energy_consumption
1722967684,0,18946473.99
1722967684,1,18792487.17

timestamp,gpu,total_energy_consumption
1722967685,0,18946517.783
1722967685,1,18792529.47

timestamp,gpu,total_energy_consumption
1722967686,0,18946561.581
1722967686,1,18792571.726

timestamp,gpu,total_energy_consumption
1722967687,0,18946605.343
1722967687,1,18792614.024

timestamp,gpu,total_energy_consumption
1722967688,0,18946649.076
1722967688,1,18792656.326
```

Now this is no longer a blocker for us. Please kindly keep us posted on the MI100 driver issue. Thanks.

### charis-poag-amd · 2024-08-06

Could you try rebooting your MI100? Would like to check if this also fixes your issue.


I am seeing the counters update on my system - after a reboot. Before rebooting, I observed the same behavior as you. We're talking with the driver team to see if there is a limitation for MI100 energy counters, will keep you updated as we learn more.

```
$ /opt/rocm-6.3.0-14535/bin/amd-smi metric --energy && /opt/rocm-6.3.0-14535/bin/rocm-smi --showenergycount && hexdump -C /sys/cla              ss/drm/card1/device/gpu_metrics && sleep 10 && /opt/rocm-6.3.0-14535/bin/amd-smi metric --energy && /opt/rocm-6.3.0-14535/bin/rocm-smi --showenergycount && hex              dump -C /sys/class/drm/card1/device/gpu_metrics
GPU: 0
    ENERGY:
        TOTAL_ENERGY_CONSUMPTION: 1.004 J

GPU: 1
    ENERGY:
        TOTAL_ENERGY_CONSUMPTION: 0.906 J




============================ ROCm System Management Interface ============================
==================================== Consumed Energy =====================================
GPU[0]          : Energy counter: 65628
GPU[0]          : Accumulated Energy (uJ): 1004108.41
GPU[1]          : Energy counter: 59230
GPU[1]          : Accumulated Energy (uJ): 906219.01
==========================================================================================
================================== End of ROCm SMI Log ===================================
00000000  78 00 01 03 2d 00 31 00  2d 00 2e 00 2d 00 2a 00  |x...-.1.-...-.*.|
00000010  00 00 00 00 00 00 24 00  5f e7 00 00 00 00 00 00  |......$._.......|
00000020  20 f4 f4 6c 81 01 00 00  2c 01 e8 03 b0 04 bb 00  | ..l....,.......|
00000030  bb 00 ff ff ff ff 2c 01  00 00 00 00 00 00 00 00  |......,.........|
00000040  ff ff ff ff 00 00 00 00  00 00 10 00 a0 00 ff ff  |................|
00000050  ff ff ff ff ff ff ff ff  ff ff ff ff ff ff ff ff  |................|
*
00000070  00 00 00 00 00 00 00 00                           |........|
00000078
GPU: 0
    ENERGY:
        TOTAL_ENERGY_CONSUMPTION: 1.01 J

GPU: 1
    ENERGY:
        TOTAL_ENERGY_CONSUMPTION: 0.912 J




============================ ROCm System Management Interface ============================
==================================== Consumed Energy =====================================
GPU[0]          : Energy counter: 66039
GPU[0]          : Accumulated Energy (uJ): 1010396.71
GPU[1]          : Energy counter: 59601
GPU[1]          : Accumulated Energy (uJ): 911895.31
==========================================================================================
================================== End of ROCm SMI Log ===================================
00000000  78 00 01 03 2d 00 31 00  2d 00 2e 00 2d 00 2b 00  |x...-.1.-...-.+.|
00000010  00 00 00 00 00 00 23 00  d1 e8 00 00 00 00 00 00  |......#.........|
00000020  a9 21 04 d2 83 01 00 00  2c 01 e8 03 b0 04 bb 00  |.!......,.......|
00000030  bb 00 ff ff ff ff 2c 01  00 00 00 00 00 00 00 00  |......,.........|
00000040  ff ff ff ff 00 00 00 00  00 00 10 00 a0 00 ff ff  |................|
00000050  ff ff ff ff ff ff ff ff  ff ff ff ff ff ff ff ff  |................|
*
00000070  00 00 00 00 00 00 00 00                           |........|
00000078

```

### jaywonchung · 2024-08-07

I see. We actually do not own the nodes; we're using those generously provided by the [AMD HPC Fund](https://www.amd.com/en/corporate/hpc-fund.html). I've posted a request there: https://github.com/AMDResearch/hpcfund/issues/25. 

### jaywonchung · 2024-08-14

@charis-poag-amd We were just now able to try it out on a freshly rebooted node, but unfortunately it seems like the issue persists.

```
[jaywonchung@t006-009 workspace]$ amd-smi version
AMDSMI Tool: 24.5.1+c5106a9 | AMDSMI Library version: 24.5.2.0 | ROCm version: 6.1.2

[jaywonchung@t006-009 workspace]$ rocm-smi --version
ROCM-SMI version: 2.2.0+193294b
ROCM-SMI-LIB version: 7.2.0

[jaywonchung@t006-009 workspace]$ amd-smi metric --energy --gpu 0 1 && rocm-smi --showenergycount -d 0 1 && sleep 10 && amd-smi metric --energy --gpu 0 1 && rocm-smi --showenergycount -d 0 1
GPU: 0
    ENERGY:
        TOTAL_ENERGY_CONSUMPTION: 0.861 J

GPU: 1
    ENERGY:
        TOTAL_ENERGY_CONSUMPTION: 0.864 J




============================ ROCm System Management Interface ============================
==================================== Consumed Energy =====================================
GPU[0]		: Energy counter: 56279
GPU[0]		: Accumulated Energy (uJ): 861068.71
GPU[1]		: Energy counter: 56460
GPU[1]		: Accumulated Energy (uJ): 863838.01
==========================================================================================
================================== End of ROCm SMI Log ===================================
GPU: 0
    ENERGY:
        TOTAL_ENERGY_CONSUMPTION: 0.867 J

GPU: 1
    ENERGY:
        TOTAL_ENERGY_CONSUMPTION: 0.869 J




============================ ROCm System Management Interface ============================
==================================== Consumed Energy =====================================
GPU[0]		: Energy counter: 56651
GPU[0]		: Accumulated Energy (uJ): 866760.31
GPU[1]		: Energy counter: 56832
GPU[1]		: Accumulated Energy (uJ): 869529.61
==========================================================================================
================================== End of ROCm SMI Log ===================================
```

### AdithyaRaman · 2024-08-23

Hi, 
I am facing a similar issue when I am using the amdsmi python library to track the energy consumption. I wrote a python script that reads the energy counter value using `amdsmi_get_energy_count(device_handler)` before and after sleeping for 2 minutes. In the same python script, I also read the start and end counter values for the same device using the amd-smi CLI and rocm-smi CLI. 

```
[0]:Time Taken:120.00874137878418
[0]:	Energy reported by AMD SMI PY: 690439604676 - 690097322004 = 0.342282672 (in Kj)
[0]:	Energy reported by ROCM SMI CLI: 10563725562865.4 - 10558494170505.68 = 5.231 (in Kj)
[0]:	Energy reported by AMD SMI CLI: 10563719.914 - 10558509.57 = 5.210344 (in Kj)
```
Both CLIs (`rocm-smi `and `amd-smi`) report similar and correct energy consumption values. However,  Not only does the python method from the amdsmi library under-reports the energy consumption but, It also looks like the energy accumulator  reported by `amdsmi.amdsmi_get_energy_count(..)` does not seem to match the accumulator values reported by both the ROCM-SMI CLI and the AMD-SMI CLI.

This experiment was performed on an _Instinct  MI210_ and we are using ROCm version 6.1.3

### jaywonchung · 2024-08-23

Regarding the discrepancy between AMD SMI PY and AMD SMI CLI -- Did you multiply the energy counter and counter resolution when using the raw Python bindings? I figured the multiplication has to be done from the following:

https://github.com/ROCm/amdsmi/blob/f4506cfd65efeb47db910f5f27e8d9ff61a6f598/amdsmi_cli/amdsmi_commands.py#L1878-L1897

### AdithyaRaman · 2024-08-26

THIS IS IT! I had to multiply the the counter with the resolution and now the result matches the reported energy from both AMD-SMI CLI and ROCM-SMI CLI, passing the multiple sanity checks.

This does make question what `energy_dict['power']` means and why the` amdsmi_get_energy_count(..)` does not directly report the energy counter.

### gabrpham · 2024-08-28

@AdithyaRaman @jaywonchung Thank you for bringing this to our attention. 

We've determined that energy_dict['power'] is indeed misleading so we will update the value to say energy_accumulator instead.

### jaywonchung · 2024-08-28

Thanks @gabrpham, I think that will improve the API. After the change, it would be nice if there's a way to maintain backwards compatibility w.r.t. the AMDSMI version with some simple logic. For example:

```python
if "energy_counter" in energy_dict:  # New API
    energy = energy_dict["energy_counter"]
elif "power" in energy_dict and "counter_resolution" in energy_dict:  # Old API
    energy = energy_dict["power"] * energy_dict["counter_resolution"]
else:
    raise ValueError
```

### marifamd · 2024-08-28

@jaywonchung It would be more like:

```
if "energy_counter" in energy_dict and "counter_resolution" in energy_dict:  # New API
    energy = energy_dict["energy_counter"] * energy_dict["counter_resolution"]
elif "power" in energy_dict and "counter_resolution" in energy_dict:  # Old API
    energy = energy_dict["power"] * energy_dict["counter_resolution"]
else:
    raise ValueError
```

We were incorrectly labeling the "energy_counter" as "power". This change will be in the C library and the Python API. We'll update the full breadth in the changelog. However the values are not changing.

### jaywonchung · 2024-09-30

@marifamd @charis-poag-amd Hi, I was just wondering if we have some updates regarding this issue. Thanks.

### marifamd · 2024-09-30

@jaywonchung We are currently testing a FW update for the mi100 internally. After we confirm that it's working we will get you an ETA on when it's publicly available.

### jaywonchung · 2024-09-30

That's awesome, thanks a lot! I'm assuming FW means firmware; it is something that can be patched with a ROCm driver update, or is it something that has to be deployed separately?

### kentrussell · 2024-09-30

FW is firmware. It would come in the "amdgpu-dkms-firmware" package, which is paired with the "amdgpu-dkms" package, both of which are considered the "ROCm kernel" package. It gets installed with --usecase=rocm, --usecase=graphics and --usecase=dkms 

### jaywonchung · 2025-05-01

Hi, I was wondering if there are updates to this issue. If it was fixed, what would be the minimal version of components that contains the fix?

### dmitrii-galantsev · 2025-06-19

pinned since it's been here a while and lots of people are asking

### dmitrii-galantsev · 2025-06-19

seeing on 2x NV21 system
```
./test.sh
Initial energy consumed by GPU 0: 2520.517 J
Final energy consumed by GPU 0: 2521.258 J
Energy consumed by GPU 0 in the last five seconds: .741 J
Expected energy consumption in last 5 seconds: 85 J
```

not seeing on MI300:
```
./test.sh
Initial energy consumed by GPU 0: 19798215.065 J
Final energy consumed by GPU 0: 19799099.239 J
Energy consumed by GPU 0 in the last five seconds: 884.174 J
Expected energy consumption in last 5 seconds: 695 J
```

### dmitrii-galantsev · 2025-06-19

rewrote script to use jq, should be a bit more robust between versions/systems.

```bash
#!/usr/bin/env bash

set -e
set -u
set -o pipefail

get_json() {
    amd-smi metric -pE --json | jq '(.gpu_data? //.) | [.[] | {gpu, power: (.power.socket_power?.value? // 0), energy: (.energy.total_energy_consumption?.value? // 0)}]'
}

get_energy_consumption() {
    echo "$1" | jq -r '.[0].energy'
}

get_socket_power() {
    echo "$1" | jq -r '.[0].power'
}

# Populate json so power and energy are collected at the same time
initial_json=$(get_json)
initial_energy=$(get_energy_consumption "$initial_json")
socket_power=$(get_socket_power "$initial_json")

# Wait for five seconds
sleep 5

final_json=$(get_json)
final_energy=$(get_energy_consumption "$final_json")
energy_difference=$(echo "$final_energy - $initial_energy" | bc)
expected_energy_consumption=$(echo "$socket_power * 5" | bc)

echo "Initial energy consumed by GPU 0: $initial_energy J"
echo "Final energy consumed by GPU 0: $final_energy J"
echo "Energy consumed by GPU 0 in the last five seconds: $energy_difference J"
echo "Expected energy consumption in last 5 seconds: $expected_energy_consumption J"
```

### dmitrii-galantsev · 2025-06-19

ok i have no idea what's going on, going to ask @marifamd to investigate.

if you multiply by 100 is it still off?

### jaywonchung · 2025-06-19

Hey @dmitrii-galantsev, thanks a lot for actively looking into this.

Unfortunately we no longer have access to any AMD GPU, so we can't really confirm more details than what's on the issue right now. But I believe it was off by a lot. For instance, in [the comment above](https://github.com/ROCm/amdsmi/issues/38#issuecomment-2289193496), total energy consumption increased by only 0.006 J and 0.005 J in 10 seconds, so even if we multiply it by 100, I'd say it's still off.

### jaywonchung · 2025-11-10

Hi, I was wondering if by any chance there was some progress on this issue. Thanks a lot.

### 9VZZH7 · 2026-06-03

More than half a year has passed since the last update here. The issue is still marked as "open", due to good reason.
`amd_smi_get_energy_count() ` is still not behaving the same on different systems...

I am using the c version of the method but internally, this should not make a difference. 

```
float resolution_o, resolution_n;
uint64_t timestamp_o, timestamp_n;
uint64_t energy_acc_o, energy_acc_n;

amdsmi_get_energy_count(processor_handle, &energy_acc_o, &resolution_o, &timestamp_o);
work(...);
amdsmi_get_energy_count(processor_handle, &energy_acc_n, &resolution_n, &timestamp_n);
```

Running on a MI300A:
I need the formula **power = resolution_o * 1000 * (energy_acc_n -energy_acc_o) / (timestamp_n - timestamp_o)** and get the exact power that is also reported in amd-smi CLI.

Running on a MI300X:
The same formula as above.

Running on a MI210:
The same formula as above.

Running on a MI100:
Here, the formula breaks and is off by 5 orders of magnitude. Instead, the correct power can be computed by: **power = 1e9 * (energy_acc_n -energy_acc_o) / (timestamp_n - timestamp_o)** 
The resolution (which in all cases is 15.3) plays no role here and the units seem to be different as well.

Running on a RX 6900 XT:
While again the resolution is not important for computing  the power, some value, likely the energy_accumulator, is scaled differently, as the formula now is **power =  1e6 * (energy_acc_n -energy_acc_o) / (timestamp_n - timestamp_o)**

Software versions are as follows:
```
AMDSMI Tool: 26.2.2+97f5574fe2 | AMDSMI Library version: 26.2.2 | ROCm version: 7.2.4 | amdgpu version: 6.16.13 | hsmp version: 2.0
ROCM-SMI version: 4.0.0+97f5574fe2
ROCM-SMI-LIB version: 7.8.0
```

Is there an update to this issue or at least some way of software-detecting which formula will work on the current GPU?
Most of them are gfx9XX but there are still differences . Is the MI100 just too old to care anymore?
