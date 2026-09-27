# [Issue #215] DCGM v4 diag info message count regression

source: https://github.com/NVIDIA/DCGM/issues/215
state: open | updated: 2025-03-12T16:22:56Z
labels: 

## 正文

With prior versions of `dcgmi diag -r 4` we could reliably expect informational messages about each test run on each gpu to be output to an `info` field both in the JSON and text based output. For instance:
```
"info" : "GPU 0 GPU to Host bandwidth:\t\t24.02 GB/s, GPU 0 Host to G
PU bandwidth:\t\t25.93 GB/s, GPU 0 bidirectional bandwidth:\t39.32 GB/s, GPU 0 GPU to Host latency:\t\t3.024 us, GPU 0 Host to GPU la
tency:\t\t3.715 us, GPU 0 bidirectional latency:\t\t5.019 us",
```

When we've run the same tests within DCGM version 4, the number of informational messages returned on a per-diagnostic run is reduced to at most 16 entries.

Tracing through the code, there is an attempt to cap the number of informational messages per test run to `16`, 
https://github.com/NVIDIA/DCGM/blob/master/dcgmlib/dcgm_structs.h#L2318

That cap is then reused/renamed here to cap the maximum number of informational responses:
https://github.com/NVIDIA/DCGM/blob/master/dcgmlib/dcgm_structs.h#L2763

Which is then used here to set the maximum array size for those informational messages
https://github.com/NVIDIA/DCGM/blob/master/dcgmlib/dcgm_structs.h#L2794

Within the version 4 output, this is seen as an info section being truncated early and then just missing from subsequent test results:
```
                                        {
                                                "name" : "diagnostic",
                                                "results" :
                                                [
                                                        {
                                                                "entity_group" : "GPU",
                                                                "entity_group_id" : 1,
                                                                "entity_id" : 0,
                                                                "info" :
                                                                [
                                                                        "Allocated space for 138 output matricies from 76077622886 bytes available.",
                                                                        "Running with precisions: FP64 1, FP32 1, FP16 1",
                                                                        "GPU 0 calculated at approximately 859.08 gigaflops during this test"
                                                                ],
                                                                "status" : "Pass"
                                                        },
                                                        {
                                                                "entity_group" : "GPU",
                                                                "entity_group_id" : 1,
                                                                "entity_id" : 1,
                                                                "info" :
                                                                [
                                                                        "Allocated space for 138 output matricies from 76077622886 bytes available.",
                                                                        "Running with precisions: FP64 1, FP32 1, FP16 1",
                                                                        "GPU 1 calculated at approximately 859.08 gigaflops during this test"
                                                                ],
                                                                "status" : "Pass"
                                                        },
                                                        {
                                                                "entity_group" : "GPU",
                                                                "entity_group_id" : 1,
                                                                "entity_id" : 2,
                                                                "info" :
                                                                [
                                                                        "Allocated space for 138 output matricies from 76077622886 bytes available.",
                                                                        "Running with precisions: FP64 1, FP32 1, FP16 1"
                                                                ],
                                                                "status" : "Pass"
                                                        },
                                                        {
                                                                "entity_group" : "GPU",
                                                                "entity_group_id" : 1,
                                                                "entity_id" : 3,
                                                                "status" : "Pass"
                                                        },
                                                        {
                                                                "entity_group" : "GPU",
                                                                "entity_group_id" : 1,
                                                                "entity_id" : 4,
                                                                "status" : "Pass"
                                                        },
                                                        {
                                                                "entity_group" : "GPU",
                                                                "entity_group_id" : 1,
                                                                "entity_id" : 5,
                                                                "status" : "Pass"
                                                        },
                                                        {
                                                                "entity_group" : "GPU",
                                                                "entity_group_id" : 1,
                                                                "entity_id" : 6,
                                                                "status" : "Pass"
                                                        },
                                                        {
                                                                "entity_group" : "GPU",
                                                                "entity_group_id" : 1,
                                                                "entity_id" : 7,
                                                                "status" : "Pass"
                                                        }
                                                ],
                                                "test_summary" :
                                                {
                                                        "status" : "Pass"
                                                }
                                        },
```

I would expect to be able to see the informational messages on a per-test instance basis.

## 评论 (3)

### shnv2023 · 2025-02-27

Thank you for your report. I can see two potential concerns:

1. The JSON output provided appears to be incomplete - it terminates with a comma, suggesting there should be additional data following this section. Could you confirm if this represents the complete output from DCGM? If not, I recommend checking for any evidence of errors or crashes in your logs.

2. Expected info messages (associated with the PCIe test, for instance) are not appearing. Based on provided output, there should still be room for additional info messages. Regarding this, the current implementation will be reviewed. 

Following our [Reporting An Issue](https://github.com/NVIDIA/DCGM#reporting-an-issue) process would help collect diagnostic information (logs, version information, etc.) that would be valuable for thoroughly investigating both aspects of this behavior.

### adamlambdal · 2025-02-27

I thought that I'd provided enough details to reproduce the issue. Regardless, here are the raw json files:
[dcgmi_diag_r_3_vers_3.json](https://github.com/user-attachments/files/19016086/dcgmi_diag_r_3_vers_3.json)
[dcgmi_diag_r_3_vers_4.json](https://github.com/user-attachments/files/19016088/dcgmi_diag_r_3_vers_4.json)

Compressed `cwd` from each run available here:
_Edit, uploaded the wrong cwd files initially_
[dcgmi_diag_vers3_logs.tar.gz](https://github.com/user-attachments/files/19016226/dcgmi_diag_vers3_logs.tar.gz)
[dcgmi_diag_vers4_logs.tar.gz](https://github.com/user-attachments/files/19016227/dcgmi_diag_vers4_logs.tar.gz)

Here are the nvidia-smi files:
[nvidia-smi-topo.txt](https://github.com/user-attachments/files/19016178/nvidia-smi-topo.txt)
[nvidia-smi_query.txt](https://github.com/user-attachments/files/19016179/nvidia-smi_query.txt)
[nvidia-smi.txt](https://github.com/user-attachments/files/19016180/nvidia-smi.txt)

### shnv2023 · 2025-03-12

Thank you for the additional details. The issue reported here has been reproduced and confirmed. We are exploring potential solutions.
