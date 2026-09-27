# [Issue #83] python binding  process smutilization always return 2147483632

source: https://github.com/NVIDIA/DCGM/issues/83
state: open | updated: 2025-02-26T20:07:38Z
labels: 

## 正文

hi，i wangt to use this function "dcgmGroup.stats.GetPidInfo(pid).summary.smUtilization.average"  by dcgm python binding, but it always return 2147483632。then i use dcgm cli tool “dcgmi stats --host  [localhost](http://localhost/) -g 11 -p   3671430  -v”，sm
 util value is 12. i don't know why
![image](https://github.com/NVIDIA/DCGM/assets/30197785/16f41431-bcbd-4264-989f-1e91bbc7d13e)


## 评论 (8)

### bstollenvidia · 2023-06-12

A couple debugging steps:
Can you share the output from the following commands:
1. dcgmi --version
2. dcgmi discovery -l



### optyang · 2023-10-23

I am having the same issue. Below is the info. Thanks!

`dcgmi --version` -> `dcgmi  version: 3.2.6`
`dcgmi discovery -l` ->
```
8 GPUs found.
+--------+----------------------------------------------------------------------+
| GPU ID | Device Information                                                   |
+--------+----------------------------------------------------------------------+
| 0      | Name: NVIDIA A100-SXM4-80GB                                          |
|        | PCI Bus ID: 00000000:10:1C.0                                         |
|        | Device UUID: GPU-ac4c2353-f2d7-cd06-3688-ed038e2677e9                |
+--------+----------------------------------------------------------------------+
| 1      | Name: NVIDIA A100-SXM4-80GB                                          |
|        | PCI Bus ID: 00000000:10:1D.0                                         |
|        | Device UUID: GPU-a70eaebf-9595-7999-af91-83219cd4343b                |
+--------+----------------------------------------------------------------------+
| 2      | Name: NVIDIA A100-SXM4-80GB                                          |
|        | PCI Bus ID: 00000000:20:1C.0                                         |
|        | Device UUID: GPU-78461f8f-4504-c074-125d-a9ae7b3290cd                |
+--------+----------------------------------------------------------------------+
| 3      | Name: NVIDIA A100-SXM4-80GB                                          |
|        | PCI Bus ID: 00000000:20:1D.0                                         |
|        | Device UUID: GPU-58ef2f70-f0c8-ac34-1de3-b8275d460031                |
+--------+----------------------------------------------------------------------+
| 4      | Name: NVIDIA A100-SXM4-80GB                                          |
|        | PCI Bus ID: 00000000:90:1C.0                                         |
|        | Device UUID: GPU-d70d542c-a1ed-31d4-00d6-9c441b517676                |
+--------+----------------------------------------------------------------------+
| 5      | Name: NVIDIA A100-SXM4-80GB                                          |
|        | PCI Bus ID: 00000000:90:1D.0                                         |
|        | Device UUID: GPU-9d36e951-a78e-40ee-c40f-d83caa418995                |
+--------+----------------------------------------------------------------------+
| 6      | Name: NVIDIA A100-SXM4-80GB                                          |
|        | PCI Bus ID: 00000000:A0:1C.0                                         |
|        | Device UUID: GPU-ff69ea16-ce74-810c-5d4f-541bf991b24b                |
+--------+----------------------------------------------------------------------+
| 7      | Name: NVIDIA A100-SXM4-80GB                                          |
|        | PCI Bus ID: 00000000:A0:1D.0                                         |
|        | Device UUID: GPU-59e925d1-5f83-fc83-c0e5-a80a31d2ddf3                |
+--------+----------------------------------------------------------------------+
0 NvSwitches found.
+-----------+
| Switch ID |
+-----------+
+-----------+
```

### optyang · 2023-10-25

> I am having the same issue. Below is the info. Thanks!
> 
> `dcgmi --version` -> `dcgmi version: 3.2.6` `dcgmi discovery -l` ->
> 
> ```
> 8 GPUs found.
> +--------+----------------------------------------------------------------------+
> | GPU ID | Device Information                                                   |
> +--------+----------------------------------------------------------------------+
> | 0      | Name: NVIDIA A100-SXM4-80GB                                          |
> |        | PCI Bus ID: 00000000:10:1C.0                                         |
> |        | Device UUID: GPU-ac4c2353-f2d7-cd06-3688-ed038e2677e9                |
> +--------+----------------------------------------------------------------------+
> | 1      | Name: NVIDIA A100-SXM4-80GB                                          |
> |        | PCI Bus ID: 00000000:10:1D.0                                         |
> |        | Device UUID: GPU-a70eaebf-9595-7999-af91-83219cd4343b                |
> +--------+----------------------------------------------------------------------+
> | 2      | Name: NVIDIA A100-SXM4-80GB                                          |
> |        | PCI Bus ID: 00000000:20:1C.0                                         |
> |        | Device UUID: GPU-78461f8f-4504-c074-125d-a9ae7b3290cd                |
> +--------+----------------------------------------------------------------------+
> | 3      | Name: NVIDIA A100-SXM4-80GB                                          |
> |        | PCI Bus ID: 00000000:20:1D.0                                         |
> |        | Device UUID: GPU-58ef2f70-f0c8-ac34-1de3-b8275d460031                |
> +--------+----------------------------------------------------------------------+
> | 4      | Name: NVIDIA A100-SXM4-80GB                                          |
> |        | PCI Bus ID: 00000000:90:1C.0                                         |
> |        | Device UUID: GPU-d70d542c-a1ed-31d4-00d6-9c441b517676                |
> +--------+----------------------------------------------------------------------+
> | 5      | Name: NVIDIA A100-SXM4-80GB                                          |
> |        | PCI Bus ID: 00000000:90:1D.0                                         |
> |        | Device UUID: GPU-9d36e951-a78e-40ee-c40f-d83caa418995                |
> +--------+----------------------------------------------------------------------+
> | 6      | Name: NVIDIA A100-SXM4-80GB                                          |
> |        | PCI Bus ID: 00000000:A0:1C.0                                         |
> |        | Device UUID: GPU-ff69ea16-ce74-810c-5d4f-541bf991b24b                |
> +--------+----------------------------------------------------------------------+
> | 7      | Name: NVIDIA A100-SXM4-80GB                                          |
> |        | PCI Bus ID: 00000000:A0:1D.0                                         |
> |        | Device UUID: GPU-59e925d1-5f83-fc83-c0e5-a80a31d2ddf3                |
> +--------+----------------------------------------------------------------------+
> 0 NvSwitches found.
> +-----------+
> | Switch ID |
> +-----------+
> +-----------+
> ```

@bstollenvidia Could you please kindly have a look? Thank you.

### dbeer · 2023-10-25

@optyang can you post the Python code you're using that isn't working correctly? 

### optyang · 2023-10-25

> @optyang can you post the Python code you're using that isn't working correctly?

Hi @dbeer, I am running `dcgm_example.py` in `/usr/local/dcgm/bindings` (dcgmi  version: 3.2.6), with the modification to get `pid` from command line. The code is below:
```
# Copyright (c) 2022, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import sys
import argparse

sys.path.insert(0, "/usr/local/dcgm/bindings/python3")
try:
    from dcgm_structs import dcgmExceptionClass
    import pydcgm
    import dcgm_structs
    import dcgm_fields
    import dcgm_agent
    import dcgmvalue
except:
    pass
    print("Unable to find python bindings, please refer to the exmaple below: ")
    print("PYTHONPATH=/usr/local/dcgm/bindings python dcgm_example.py")
    sys.exit(1)

## Look at __name__ == "__main__" for entry point to the script

## Helper method to convert DCGM value to string
def convert_value_to_string(value):
    v = dcgmvalue.DcgmValue(value)

    try:
        if (v.IsBlank()):
            return "N/A"
        else:
            return v.__str__()
    except:
        ## Exception is generally thorwn when int32 is
        ## passed as an input. Use additional methods to fix it
        sys.exc_clear()
        v = dcgmvalue.DcgmValue(0)
        v.SetFromInt32(value)

        if (v.IsBlank()):
            return "N/A"
        else:
            return v.__str__()

## Helper method to investigate the status handler
def helper_investigate_status(statusHandle):
    """
    Helper method to investigate status handle
    """
    errorCount = 0
    errorInfo = dcgm_agent.dcgmStatusPopError(statusHandle)

    while (errorInfo != None):
        errorCount += 1
        print("Error%d" % errorCount)
        print(("  GPU Id: %d" % errorInfo.gpuId))
        print(("  Field ID: %d" % errorInfo.fieldId))
        print(("  Error: %d" % errorInfo.status))
        errorInfo = dcgm_agent.dcgmStatusPopError(statusHandle)


## Helper method to convert enum to system name
def helper_convert_system_enum_to_sytem_name(system):
    if system & (1 << dcgm_structs.DCGM_HEALTH_WATCH_PCIE):
        return "PCIe"

    if system & (1 << dcgm_structs.DCGM_HEALTH_WATCH_NVLINK):
        return "NvLink"
    
    if system & (1 << dcgm_structs.DCGM_HEALTH_WATCH_PMU):
        return "PMU"

    if system & (1 << dcgm_structs.DCGM_HEALTH_WATCH_MCU):
        return "MCU"
    
    if system & (1 << dcgm_structs.DCGM_HEALTH_WATCH_MEM):
        return "MEM"
    
    if system & (1 << dcgm_structs.DCGM_HEALTH_WATCH_SM):
        return "SM"
    
    if system & (1 << dcgm_structs.DCGM_HEALTH_WATCH_INFOROM):
        return "Inforom"
    
    if system & (1 << dcgm_structs.DCGM_HEALTH_WATCH_THERMAL):
        return "Thermal"
    
    if system & (1 << dcgm_structs.DCGM_HEALTH_WATCH_POWER):
        return "Power"   
    
    if system & (1 << dcgm_structs.DCGM_HEALTH_WATCH_DRIVER):
        return "Driver"
    
    
## helper method to convert helath return to a string for display purpose        
def convert_overall_health_to_string(health):
    if health == dcgm_structs.DCGM_HEALTH_RESULT_PASS:
        return "Pass"
    elif health == dcgm_structs.DCGM_HEALTH_RESULT_WARN:
        return "Warn"
    elif  health == dcgm_structs.DCGM_HEALTH_RESULT_FAIL:
        return "Fail"
    else :
        return "N/A"

def nvvs_installed():
    return os.path.isfile('/usr/share/nvidia-validation-suite/nvvs')

def dcgm_diag_test_didnt_pass(rc):
    if rc == dcgm_structs.DCGM_HEALTH_RESULT_FAIL or rc == dcgm_structs.DCGM_HEALTH_RESULT_WARN:
        return True
    else:
        return False

def dcgm_diag_test_index_to_name(index):
    if index == dcgm_structs.DCGM_SWTEST_DENYLIST:
        return "denylist"
    elif index == dcgm_structs.DCGM_SWTEST_NVML_LIBRARY:
        return "nvmlLibrary"
    elif index == dcgm_structs.DCGM_SWTEST_CUDA_MAIN_LIBRARY:
        return "cudaMainLibrary"
    elif index == dcgm_structs.DCGM_SWTEST_CUDA_RUNTIME_LIBRARY:
        return "cudaRuntimeLibrary"
    elif index == dcgm_structs.DCGM_SWTEST_PERMISSIONS:
        return "permissions"
    elif index == dcgm_structs.DCGM_SWTEST_PERSISTENCE_MODE:
        return "persistenceMode"
    elif index == dcgm_structs.DCGM_SWTEST_ENVIRONMENT:
        return "environment"
    elif index == dcgm_structs.DCGM_SWTEST_PAGE_RETIREMENT:
        return "pageRetirement"
    elif index == dcgm_structs.DCGM_SWTEST_GRAPHICS_PROCESSES:
        return "graphicsProcesses"
    elif index == dcgm_structs.DCGM_SWTEST_INFOROM:
        return "inforom"
    else:
        raise dcgm_structs.DCGMError(dcgm_structs.DCGM_ST_BADPARAM)

# Returns true if the error here should be ignored
def should_ignore_error(diagException):
    if diagException.info:
        if diagException.info.find("MIG configuration is incompatible with the diagnostic because it prevents access to the entire GPU."
    ) != -1:
            return True

        if diagException.info.find("Cannot run diagnostic: CUDA does not support enumerating GPUs with MIG mode enabled") == 0:
            return True

    return False

def main(manualOpMode=False, embeddedHostengine=True, pid=0):
    
    if manualOpMode:
        ## Initialize the DCGM Engine as manual operation mode. This implies that it's execution is 
        ## controlled by the monitoring agent. The user has to periodically call APIs such as 
        ## dcgmEnginePolicyTrigger and dcgmEngineUpdateAllFields which tells DCGM to wake up and 
        ## perform data collection and operations needed for policy management.
        ## Manual operation mode is only possible on an "embedded" hostengine.
        opMode = dcgm_structs.DCGM_OPERATION_MODE_MANUAL
    else:
        ## Initialize the DCGM Engine as automatic operation mode. This is required when connecting
        ## to a "standalone" hostengine (one that is running separately) but can also be done on an 
        ## embedded hostengine.  In this mode, fields are updated
        ## periodically based on their configured frequency.  When watching new fields you must still manually
        ## trigger an update if you wish to view these new fields' values right away.
        opMode = dcgm_structs.DCGM_OPERATION_MODE_AUTO
    
    if embeddedHostengine:
        print(("Running an embedded hostengine with %s opmode..." % 
              ('manual' if manualOpMode else 'auto')))
        
        ## create embedded hostengine by leaving ipAddress as None
        dcgmHandle = pydcgm.DcgmHandle(opMode=opMode)
    
    else:
        print(("Connecting to a standalone hostengine with %s opmode..." % 
              ('manual' if manualOpMode else 'auto')))
        
        dcgmHandle = pydcgm.DcgmHandle(ipAddress='127.0.0.1', opMode=opMode)
    print("")

    ## Get a handle to the system level object for DCGM
    dcgmSystem = dcgmHandle.GetSystem()
    supportedGPUs = dcgmSystem.discovery.GetAllSupportedGpuIds()
    
    
    ## Create an empty group. Let's call the group as "one_gpus_group". 
    ## We will add the first supported GPU in the system to this group. 
    dcgmGroup = pydcgm.DcgmGroup(dcgmHandle, groupName="one_gpu_group", groupType=dcgm_structs.DCGM_GROUP_EMPTY)
    
    #Skip the test if no supported gpus are available
    if len(supportedGPUs) < 1:
        print("Unable to find supported GPUs on this system")
        sys.exit(0)
        
    dcgmGroup.AddGpu(supportedGPUs[0])

    ## Invoke method to get gpu IDs of the members of the newly-created group
    groupGpuIds = dcgmGroup.GetGpuIds()
    
    ## Trigger field updates since we just started DCGM (always necessary in MANUAL mode to get recent values)
    dcgmSystem.UpdateAllFields(waitForUpdate=True)

    ## Get the current configuration for the group
    config_values = dcgmGroup.config.Get(dcgm_structs.DCGM_CONFIG_CURRENT_STATE)
    
    ## Display current configuration for the group
    for x in range(0, len(groupGpuIds)):
        print("GPU Id      : %d" % (config_values[x].gpuId))
        print("Ecc  Mode   : %s" % (convert_value_to_string(config_values[x].mEccMode)))
        print("Sync Boost  : %s" % (convert_value_to_string(config_values[x].mPerfState.syncBoost)))
        print("Mem Clock   : %s" % (convert_value_to_string(config_values[x].mPerfState.targetClocks.memClock)))
        print("SM  Clock   : %s" % (convert_value_to_string(config_values[x].mPerfState.targetClocks.smClock)))
        print("Power Limit : %s" % (convert_value_to_string(config_values[x].mPowerLimit.val)))
        print("Compute Mode: %s" % (convert_value_to_string(config_values[x].mComputeMode)))
        print("\n")

    ## Add the health watches
    dcgmGroup.health.Set(dcgm_structs.DCGM_HEALTH_WATCH_ALL)
    
    ## Ensure that the newly watched health fields are updated since we wish to access them right away.
    ## Needed in manual mode and only needed in auto mode if we want to see the values right away
    dcgmSystem.UpdateAllFields(waitForUpdate=True)

    ## Invoke Health checks
    try:
        group_health = dcgmGroup.health.Check()
        print("Overall Health for the group: %s" % convert_overall_health_to_string(group_health.overallHealth))

        for index in range (0, group_health.incidentCount):
            print("GPU ID : %d" % group_health.incidents[index].entityInfo.entityId)

            print("system tested     : %d" % group_health.incidents[index].system)
            print("system health     : %s" % convert_overall_health_to_string(group_health.incidents[index].health))
            print("system health err : %s" % group_health.incidents[index].error.msg)
            print("\n")
    except dcgm_structs.DCGMError as e:
        errorCode = e.value
        print("dcgmHealthCheck returned error %d: %s" % (errorCode, e))
        sys.exc_clear()

    print("")
        
    if nvvs_installed():
        ## This will go ahead and perform a "prologue" diagnostic 
        ## to make sure everything is ready to run
        ## currently this calls an outside diagnostic binary but eventually
        ## that binary will be merged into the DCGM framework 
        ## The "response" is a dcgmDiagResponse structure that can be parsed for errors. 
        try:
            response = dcgmGroup.action.RunDiagnostic(dcgm_structs.DCGM_DIAG_LVL_SHORT)
        except dcgmExceptionClass(dcgm_structs.DCGM_ST_NOT_CONFIGURED):
            print("One of the GPUs on your system is not supported by NVVS")
        except dcgmExceptionClass(dcgm_structs.DCGM_ST_GROUP_INCOMPATIBLE):
            print("GPUs in the group are not compatible with each other for running diagnostics")
        except dcgmExceptionClass(dcgm_structs.DCGM_ST_NVVS_ERROR) as e:
            if not should_ignore_error(e):
               raise(e)
            else:
                print(str(e))
        else:
            isHealthy = True
            
            for i in range(0, response.levelOneTestCount):
                if dcgm_diag_test_didnt_pass(response.levelOneResults[i].result):
                    print("group failed validation check for %s" % dcgm_diag_test_index_to_name(i))
                    isHealthy = False
                
            if not isHealthy:
                print("System is not healthy")
    else:
        print("not running short group validation because NVIDIA Validation Suite is not installed")
    print("")
    
    ## Add process watches so that DCGM can start watching process info
    dcgmGroup.stats.WatchPidFields(1000000, 3600, 0)
    
    ####################################################################
    # Start a CUDA process at this point and get the PID for the process
    ## Wait until it completes
    ## dcgmGroup.health.Check() is a low overhead check and can be performed 
    ## in parallel to the job without impacting application's performance
    ####################################################################

    try:
        pidInfo = dcgmGroup.stats.GetPidInfo(pid)
    
        ## Display some process statistics (more may be desired)
        print("Process ID      : %d" % pid)
        print("Start time      : %d" % pidInfo.summary.startTime)
        print("End time        : %d" % pidInfo.summary.endTime)
        print("Energy consumed : %d" % pidInfo.summary.energyConsumed)
        print("Max GPU Memory  : %d" % pidInfo.summary.maxGpuMemoryUsed)
        print("Avg. SM util    : %d" % pidInfo.summary.smUtilization.average)
        print("Min. SM util    : %d" % pidInfo.summary.smUtilization.minValue)
        print("Avg. mem util   : %d" % pidInfo.summary.memoryUtilization.average)
        print("Min. mem util   : %d" % pidInfo.summary.memoryUtilization.minValue)
        print("Avg. mem clock  : %d" % pidInfo.summary.memoryClock.average)
        print("Min. mem clock  : %d" % pidInfo.summary.memoryClock.minValue)
        print("Avg. SM Clock   : %d" % pidInfo.summary.smClock.average)
        print("Min. SM Clock   : %d" % pidInfo.summary.smClock.minValue)
        print("low util time   : %d" % pidInfo.summary.lowUtilizationTime)

    except:
        print("There was no CUDA job running to collect the stats")
        pass
    
    # Nvidia Validation Suite is required when performing "validate" actions
    if nvvs_installed():
        ## Now that the process has completed we perform an "epilogue" diagnostic that will stress the system
        try:
            response = dcgmGroup.action.RunDiagnostic(dcgm_structs.DCGM_DIAG_LVL_MED)
        except dcgmExceptionClass(dcgm_structs.DCGM_ST_NOT_CONFIGURED):
            print("One of the GPUs on your system is not supported by NVVS")
        except dcgmExceptionClass(dcgm_structs.DCGM_ST_NVVS_ERROR) as e:
            if not should_ignore_error(e):
               raise(e)
            else:
                print(str(e))
        else:
            ## Check the response and do any actions desired based on the results. 
            pass
        
    else:
        print("not running medium group validation because NVIDIA Validation Suite is not installed")
    print("")
    
    ## Delete the group
    dcgmGroup.Delete()
    del(dcgmGroup)
    dcgmGroup = None

    ## disconnect from the hostengine by deleting the DcgmHandle object
    del(dcgmHandle)
    dcgmHandle = None

## Entry point for this script
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script for showing off how to use DCGM python bindings')
    parser.add_argument('-o', '--opmode', 
                        choices=['manual', 'auto'], 
                        default='manual',
                        help='Operation mode for the hostengine. Must be auto if a standalone hostengine ' +
                              'is used. Defaults to auto.')
    
    parser.add_argument('-t', '--type',
                        choices=['embedded', 'standalone'], 
                        default='standalone',
                        help='Type of hostengine.  Embedded mode starts a hostengine within the ' +
                             'same process. Standalone means that a separate hostengine process ' +
                             'is already running that will be connected to. '
                        )
   
    parser.add_argument('-p', '--pid',
			type=int,
                        help='pid'
                        )
 
    args = parser.parse_args()
    manualOpMode = args.opmode == 'manual'
    embeddedHostengine = args.type == 'embedded'
    if args.pid is None:
        raise ValueError("pid is None!")
    
    main(manualOpMode, embeddedHostengine, args.pid)

```
1. `python3 python_toy_script.py` (a toy example to get GPU running)
2. `nvidia-smi` (to get PID, which is 3518784 in my case)
3. `python3 dcgm_example.py -p 3518784 `

`python_toy_script.py` is like this:
```
import torch

x = torch.randn([1024, 1024], device="cuda", dtype=torch.float16)
while True:
    x @ x
```

Results:
```
Connecting to a standalone hostengine with manual opmode...
GPU Id      : 0
Ecc  Mode   : 1
Sync Boost  : 2147483634
Mem Clock   : 1593
SM  Clock   : 1410
Power Limit : 400
Compute Mode: 0
Overall Health for the group: Pass
Process ID      : 3518784
Start time      : 1698234697304910
End time        : 0
Energy consumed : 43644267
Max GPU Memory  : 473956352
Avg. SM util    : 2147483632
Min. SM util    : 2147483632
Avg. mem util   : 2147483632
Min. mem util   : 2147483632
Avg. mem clock  : 2147483632
Min. mem clock  : 2147483632
Avg. SM Clock   : 2147483632
Min. SM Clock   : 2147483632
low util time   : 0
```

Alternatively, when I try to get the job statistics from cli, it seems working:
```
yangyang22@workers-st-p4de-318:~/projects/xformers/xformers/profiler$ dcgmi group -c pybindings
yangyang22@workers-st-p4de-318:~/projects/xformers/xformers/profiler$ dcgmi group -l
+-------------------+----------------------------------------------------------+
| GROUPS                                                                       |
| 3 groups found.                                                              |
+===================+==========================================================+
| Groups            |                                                          |
| -> 0              |                                                          |
|    -> Group ID    | 0                                                        |
|    -> Group Name  | DCGM_ALL_SUPPORTED_GPUS                                  |
|    -> Entities    | GPU 0, GPU 1, GPU 2, GPU 3, GPU 4, GPU 5, GPU 6, GPU 7   |
| -> 1              |                                                          |
|    -> Group ID    | 1                                                        |
|    -> Group Name  | DCGM_ALL_SUPPORTED_NVSWITCHES                            |
|    -> Entities    | None                                                     |
| -> 111            |                                                          |
|    -> Group ID    | 111                                                      |
|    -> Group Name  | pybindings                                               |
|    -> Entities    | GPU 0                                                    |
+-------------------+----------------------------------------------------------+
yangyang22@workers-st-p4de-318:~/projects/xformers/xformers/profiler$ dcgmi stats -g 111 --enable
Successfully started process watches.
yangyang22@workers-st-p4de-318:~/projects/xformers/xformers/profiler$ nvidia-smi
Wed Oct 25 17:10:27 2023       
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.54.03              Driver Version: 535.54.03    CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA A100-SXM4-80GB          On  | 00000000:10:1C.0 Off |                    0 |
| N/A   64C    P0             358W / 400W |  54906MiB / 81920MiB |    100%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   1  NVIDIA A100-SXM4-80GB          On  | 00000000:10:1D.0 Off |                    0 |
| N/A   29C    P0              59W / 400W |      5MiB / 81920MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   2  NVIDIA A100-SXM4-80GB          On  | 00000000:20:1C.0 Off |                    0 |
| N/A   31C    P0              58W / 400W |      5MiB / 81920MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   3  NVIDIA A100-SXM4-80GB          On  | 00000000:20:1D.0 Off |                    0 |
| N/A   29C    P0              56W / 400W |      5MiB / 81920MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   4  NVIDIA A100-SXM4-80GB          On  | 00000000:90:1C.0 Off |                    0 |
| N/A   31C    P0              60W / 400W |      5MiB / 81920MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   5  NVIDIA A100-SXM4-80GB          On  | 00000000:90:1D.0 Off |                    0 |
| N/A   30C    P0              59W / 400W |      5MiB / 81920MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   6  NVIDIA A100-SXM4-80GB          On  | 00000000:A0:1C.0 Off |                    0 |
| N/A   70C    P0             313W / 400W |  36737MiB / 81920MiB |     91%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   7  NVIDIA A100-SXM4-80GB          On  | 00000000:A0:1D.0 Off |                    0 |
| N/A   60C    P0             339W / 400W |  36737MiB / 81920MiB |    100%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|    0   N/A  N/A   3518784      C   python3                                     452MiB |

yangyang22@workers-st-p4de-318:~/projects/xformers/xformers/profiler$ dcgmi stats --pid 3518784 -v
Successfully retrieved process info for PID: 3518784. Process ran on 1 GPUs.
+------------------------------------------------------------------------------+
| GPU ID: 0                                                                    |
+====================================+=========================================+
|-----  Execution Stats  ------------+-----------------------------------------|
| Start Time                     *   | Wed Oct 25 11:51:37 2023                |
| End Time                       *   | Still Running                           |
| Total Execution Time (sec)     *   | Still Running                           |
| No. of Conflicting Processes   *   | 1                                       |
| Conflicting Compute PID            | 4084755                                 |
+-----  Performance Stats  ----------+-----------------------------------------+
| Energy Consumed (Joules)           | 1249175                                 |
| Max GPU Memory Used (bytes)    *   | 473956352                               |
| SM Clock (MHz)                     | Avg: 1410, Max: 1410, Min: 1410         |
| Memory Clock (MHz)                 | Avg: 1593, Max: 1593, Min: 1593         |
| SM Utilization (%)                 | Avg: 100, Max: 100, Min: 100            |
| Memory Utilization (%)             | Avg: 3, Max: 31, Min: 0                 |
| PCIe Rx Bandwidth (megabytes)      | Avg: N/A, Max: N/A, Min: N/A            |
| PCIe Tx Bandwidth (megabytes)      | Avg: N/A, Max: N/A, Min: N/A            |
+-----  Event Stats  ----------------+-----------------------------------------+
| Double Bit ECC Errors              | 0                                       |
| PCIe Replay Warnings               | 0                                       |
| Critical XID Errors                | 0                                       |
+-----  Slowdown Stats  -------------+-----------------------------------------+
| Due to - Power (%)                 | 0                                       |
|        - Thermal (%)               | 0                                       |
|        - Reliability (%)           | 0                                       |
|        - Board Limit (%)           | 0                                       |
|        - Low Utilization (%)       | 0                                       |
|        - Sync Boost (%)            | 0                                       |
+-----  Process Utilization  --------+-----------------------------------------+
| PID                                | 3518784                                 |
|     Avg SM Utilization (%)         | 82                                      |
|     Avg Memory Utilization (%)     | 1                                       |
+-----  Overall Health  -------------+-----------------------------------------+
| Overall Health                     | Healthy                                 |
+------------------------------------+-----------------------------------------+
(*) Represents a process statistic. Otherwise device statistic during 
    process lifetime listed.
```
Please kindly let me know what you think. Thank you!

### nikkon-dev · 2023-11-30

@optyang,  

The value that you observe is 0x7ffffff0, which is DCGM_INT32_BLANK. In our tools, that usually leads to 'N/A' output.
Please, take a look at this code: https://github.com/NVIDIA/DCGM/blob/cc3fe64d966d956cebba3e3ff1334786dd767d35/testing/python3/dcgmvalue.py#L45

### Shuofeng-Wang · 2025-02-25

@nikkon-dev Hi Nik, 214748363**4** is actually 0x7FFFFFF**2**, instead of 0x7FFFFFF**0** (DCGM_INT32_BLANK=214748363**2**). I'm facing the same issue using the [latest example.py](https://github.com/NVIDIA/DCGM/blob/master/sdk_samples/scripts/dcgm_example.py) with dcgmi version 4.1.1. 

[Nvidia Official doc](https://docs.nvidia.com/datacenter/dcgm/latest/dcgm-api/dcgm-api-structs.html#_CPPv429dcgmConfigPerfStateSettings_t) said "_**Sync Boost Mode (0: Disabled, 1 : Enabled, DCGM_INT32_BLANK : Ignored).**_" but now I think it is a typo: Ignored value should be 0x7FFFFFF2 instead of 0x7FFFFFF0 (INT32_BLANK). Or maybe 0x7FFFFFF2 means not-supported, which is missing in the sdk doc? 

This is the raw data output when printing `dcgmGroup.config.Get(dcgm_structs.DCGM_CONFIG_CURRENT_STATE)[7]`
```
DEBUG: c_dcgmDeviceConfig_v2(version: 33554504, gpuId: 7, mEccMode: 1, mComputeMode: 0, mPerfState: c_dcgmConfigPerfStateSettings_t(syncBoost: 2147483634, targetClocks: c_dcgmClockSet_v1(version: 16777228, memClock: 877, smClock: 1312)), mPowerLimit: c_dcgmConfigPowerLimit(type: 0, val: 300), mWorkloadPowerProfiles: <dcgm_structs.c_uint_Array_8 object at 0x7a81789eb140>)
```

```
GPU Id      : 7
Ecc  Mode   : 1
Sync Boost  : 2147483634
Mem Clock   : 877
SM  Clock   : 1312
Power Limit : 300
Compute Mode: 0
```

### nikkon-dev · 2025-02-26

@Shuofeng-Wang,

Please take a look at the BLANK costs [here](https://github.com/NVIDIA/DCGM/blob/d47c0b77920f8dbfef588eaac2cbbea3401ef463/dcgmlib/dcgm_structs.h#L55)

DCGM_INT32_BLANK is a base value; other special values are DCGM_INT32_BLANK + N, where N is 1, 2, 3...
DCGM_INT32_BLANK + 2 is DCGM_INT32_NOT_SUPPORTED
