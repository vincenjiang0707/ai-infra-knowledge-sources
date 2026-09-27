# [Issue #253] diag warning after upgrade to 4.2.3

source: https://github.com/NVIDIA/DCGM/issues/253
state: open | updated: 2025-09-04T14:38:14Z
labels: 

## 正文

After upgrading to 4.2.3 I now see a lot of warnings on nodes after reboots.
Additional reboots to reset the GPU do not clear these warning:

```
Executing in Pod nvidia-dcgm-rz9cr on Host 10.0.7.139
Successfully ran diagnostic for group.
+---------------------------+------------------------------------------------+
| Diagnostic                | Result                                         |
+===========================+================================================+
|-----  Metadata  ----------+------------------------------------------------|
| DCGM Version              | 4.2.3                                          |
| Driver Version Detected   | 570.148.08                                     |
| GPU Device IDs Detected   | 26b9, 26b9, 26b9, 26b9                         |
|-----  Deployment  --------+------------------------------------------------|
| software                  | Pass                                           |
|                           | GPU0: Pass                                     |
|                           | GPU1: Pass                                     |
|                           | GPU2: Pass                                     |
|                           | GPU3: Pass                                     |
+-----  Hardware  ----------+------------------------------------------------+
| memory                    | Pass                                           |
|                           | GPU0: Pass                                     |
|                           | GPU1: Pass                                     |
|                           | GPU2: Pass                                     |
|                           | GPU3: Pass                                     |
+-----  Integration  -------+------------------------------------------------+
| pcie                      | Fail                                           |
| Warning                   | There was an internal error during the test:   |
|                           | 'A child process (152) exited with non-zero s  |
|                           | tatus 1' Check DCGM and system logs for error  |
|                           | s. Reset GPU. Restart DCGM. Rerun diagnostics  |
|                           | .                                              |
| Warning                   | There was an internal error during the test:   |
|                           | 'A child process (153) exited with non-zero s  |
|                           | tatus 1' Check DCGM and system logs for error  |
|                           | s. Reset GPU. Restart DCGM. Rerun diagnostics  |
|                           | .                                              |
| Warning                   | There was an internal error during the test:   |
|                           | 'Output of child process (152) couldn't be pa  |
|                           | rsed: '* Line 1, Column 1   Syntax error: val  |
|                           | ue, object or array expected. '' Check DCGM a  |
|                           | nd system logs for errors. Reset GPU. Restart  |
|                           |  DCGM. Rerun diagnostics.                      |
| Warning                   | There was an internal error during the test:   |
|                           | 'Output of child process (153) couldn't be pa  |
|                           | rsed: '* Line 1, Column 1   Syntax error: val  |
|                           | ue, object or array expected. '' Check DCGM a  |
|                           | nd system logs for errors. Reset GPU. Restart  |
|                           |  DCGM. Rerun diagnostics.                      |
|                           | GPU0: Pass                                     |
|                           | GPU1: Pass                                     |
|                           | GPU2: Pass                                     |
|                           | GPU3: Pass                                     |
```

## 评论 (1)

### gmarciani · 2025-09-03

Similar warning returned using DCGM v4.4.1 on B200 when the command is submitted within a slurm job: `sbatch -n 1 --wrap='srun dcgmi diag -r 2'`.

### dcgm output
```
+---------------------------+------------------------------------------------+
| Diagnostic                | Result                                         |
+===========================+================================================+
|-----  Metadata  ----------+------------------------------------------------|
| DCGM Version              | 4.4.1                                          |
| Driver Version Detected   | 570.172.08                                     |
| GPU Device IDs Detected   | 2901, 2901, 2901, 2901, 2901, 2901, 2901, 2901 |
|-----  Deployment  --------+------------------------------------------------|
| software                  | Pass                                           |
|                           | GPU0: Pass                                     |
|                           | GPU1: Pass                                     |
|                           | GPU2: Pass                                     |
|                           | GPU3: Pass                                     |
|                           | GPU4: Pass                                     |
|                           | GPU5: Pass                                     |
|                           | GPU6: Pass                                     |
|                           | GPU7: Pass                                     |
+-----  Hardware  ----------+------------------------------------------------+
| memory                    | Pass                                           |
|                           | GPU0: Pass                                     |
|                           | GPU1: Pass                                     |
|                           | GPU2: Pass                                     |
|                           | GPU3: Pass                                     |
|                           | GPU4: Pass                                     |
|                           | GPU5: Pass                                     |
|                           | GPU6: Pass                                     |
|                           | GPU7: Pass                                     |
+-----  Integration  -------+------------------------------------------------+
| pcie                      | Fail                                           |
| Warning                   | There was an internal error during the test:   |
|                           | 'Output of child process (11167) couldn't be   |
|                           | parsed: '* Line 1, Column 1   Syntax error: v  |
|                           | alue, object or array expected. '' Check DCGM  |
|                           |  and system logs for errors. Reset GPU. Resta  |
|                           | rt DCGM. Rerun diagnostics.                    |
|                           | GPU0: Pass                                     |
|                           | GPU1: Pass                                     |
|                           | GPU2: Pass                                     |
|                           | GPU3: Pass                                     |
|                           | GPU4: Pass                                     |
|                           | GPU5: Pass                                     |
|                           | GPU6: Pass                                     |
|                           | GPU7: Pass                                     |
+---------------------------+------------------------------------------------+
```

### nvvs logs

See full dcgm logs: [dcgm-4.4.1-nvvs-output.txt](https://github.com/user-attachments/files/22126454/dcgm-4.4.1-nvvs-output.txt)

Highlights from the logs:
```
2025-09-03 17:23:01.310 DEBUG [12696:12696] [[pcie]] External command stdout: numa_sched_setaffinity_v2_int() failed: Invalid argument
{
        "GPUs" :
        [
                {
                        "gpuId" : 4,
                        "maxBidirBw" : 101.08203545772291,
                        "maxRxBw" : 55.60305842796847,
                        "maxTxBw" : 57.173431731400029
                },
                {
                        "gpuId" : 5,
                        "maxBidirBw" : 101.07950322417911,
                        "maxRxBw" : 55.615753471098259,
                        "maxTxBw" : 57.176486608408709
                },
                {
                        "gpuId" : 6,
                        "maxBidirBw" : 101.07803969750911,
                        "maxRxBw" : 55.607160567632093,
                        "maxTxBw" : 57.175237860111302
                },
                {
                        "gpuId" : 7,
                        "maxBidirBw" : 101.06620527308152,
                        "maxRxBw" : 55.608770655873094,
                        "maxTxBw" : 57.173234773646818
                }
        ]
}

 [/builds/dcgm/dcgm/nvvs/plugin_src/pcie/PcieMain.cpp:574] [ReadChildOutput]
2025-09-03 17:23:01.310 DEBUG [12696:12696] [[pcie]] External command stdout: {
        "GPUs" :
        [
                {
                        "gpuId" : 0,
                        "maxBidirBw" : 101.08615932058315,
                        "maxRxBw" : 55.613608512459187,
                        "maxTxBw" : 57.179307642405583
                },
                {
                        "gpuId" : 1,
                        "maxBidirBw" : 101.07911991547871,
                        "maxRxBw" : 55.614716134375513,
                        "maxTxBw" : 57.183619641988557
                },
                {
                        "gpuId" : 2,
                        "maxBidirBw" : 101.07961937890471,
                        "maxRxBw" : 55.612434129791573,
                        "maxTxBw" : 57.179842889759129
                },
                {
                        "gpuId" : 3,
                        "maxBidirBw" : 101.07860884173367,
                        "maxRxBw" : 55.61823620357324,
                        "maxTxBw" : 57.183299936940408
                }
        ]
}

 [/builds/dcgm/dcgm/nvvs/plugin_src/pcie/PcieMain.cpp:574] [ReadChildOutput]
2025-09-03 17:23:02.849 DEBUG [12696:12696] Unregistering process 12918 [/builds/dcgm/dcgm/common/HangDetectMonitor.cpp:363] [HangDetectMonitor::RemoveMonitoredTask]
2025-09-03 17:23:02.849 DEBUG [12696:12696] Deleted fingerprint for pid 12918 [/builds/dcgm/dcgm/common/FingerprintStore.cpp:134] [FingerprintStore::Delete]
2025-09-03 17:23:02.849 DEBUG [12696:12696] Unregistering process 12919 [/builds/dcgm/dcgm/common/HangDetectMonitor.cpp:363] [HangDetectMonitor::RemoveMonitoredTask]
2025-09-03 17:23:02.849 DEBUG [12696:12696] Deleted fingerprint for pid 12919 [/builds/dcgm/dcgm/common/FingerprintStore.cpp:134] [FingerprintStore::Delete]
2025-09-03 17:23:02.849 WARN  [12696:12696] Test pcie: There was an internal error during the test: 'Output of child process (12918) couldn't be parsed: '* Line 1, Column 1
  Syntax error: value, object or array expected.
'' Check DCGM and system logs for errors. Reset GPU. Restart DCGM. Rerun diagnostics. (grpId:0, entityId:0) [/builds/dcgm/dcgm/nvvs/src/PluginTest.cpp:179] [PluginTest::AddError]

...

2025-09-03 17:26:26.118 DEBUG [12696:12696] Called; errors = 1, info = 36, results = 8 [/builds/dcgm/dcgm/nvvs/src/PluginLibTest.cpp:228] [PluginLibTest::PopulateEntityResults]
2025-09-03 17:26:26.118 DEBUG [12696:12696] Plugin returned unknown type of aux data. Expected JSON_VALUE_AUX_DATA_TYPE (1), got 0 [/builds/dcgm/dcgm/nvvs/src/PluginLibTest.cpp:280] [PluginLibTest::PopulateEntityResults]
```

So it seems that under some conditions within the PCIe test, the function numa_sched_setaffinity_v2_int() fails, corrupting the output, which is expected to be a JSON.

Does DCGM require a specific version of libnuma?

**UPDATE**
We figured out that the PCIe test failure does not occur when:
1. the command is executed locally on the node, rather than being submitted as a Slurm job.
2. the command is submitted with Slurm scheduler taking the full node (--exclusive option of sbatch command)
