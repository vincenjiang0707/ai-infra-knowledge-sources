# [Issue #835] [Bug]: TypeError: list indices must be integers or slices, not str

source: https://github.com/ROCm/rocprofiler-compute/issues/835
state: closed | updated: 2025-07-30T13:40:05Z
labels: bug, triage

## 正文

### Describe the bug

Using 6885cb068d61f5112f276dbfc7d90f3007726fbc and https://github.com/ROCm/rocprofiler-sdk/commit/3954cedd253a6b370cba9018edfe03291875d3aa on MI355. It used to work a week or two ago...

```
Traceback (most recent call last):
  File "/felmarty/repos/rocprofiler-compute/build/install2/3.1.1/bin/rocprof-compute", line 170, in <module>
    main()
  File "/felmarty/repos/rocprofiler-compute/build/install2/3.1.1/bin/rocprof-compute", line 158, in main
    rocprof_compute.run_profiler()
  File "/felmarty/repos/rocprofiler-compute/build/install2/3.1.1/libexec/rocprofiler-compute/utils/logger.py", line 48, in wrap_function
    result = function(*args, **kwargs)
  File "/felmarty/repos/rocprofiler-compute/build/install2/3.1.1/libexec/rocprofiler-compute/rocprof_compute_base.py", line 239, in run_profiler
    self.load_soc_specs()
  File "/felmarty/repos/rocprofiler-compute/build/install2/3.1.1/libexec/rocprofiler-compute/utils/logger.py", line 48, in wrap_function
    result = function(*args, **kwargs)
  File "/felmarty/repos/rocprofiler-compute/build/install2/3.1.1/libexec/rocprofiler-compute/rocprof_compute_base.py", line 146, in load_soc_specs
    self.__mspec = generate_machine_specs(self.__args, sysinfo)
  File "/felmarty/repos/rocprofiler-compute/build/install2/3.1.1/libexec/rocprofiler-compute/utils/specs.py", line 226, in generate_machine_specs
    soc_obj = soc_class(args, specs)
  File "/felmarty/repos/rocprofiler-compute/build/install2/3.1.1/libexec/rocprofiler-compute/rocprof_compute_soc/soc_gfx950.py", line 37, in __init__
    super().__init__(args, mspec)
  File "/felmarty/repos/rocprofiler-compute/build/install2/3.1.1/libexec/rocprofiler-compute/rocprof_compute_soc/soc_base.py", line 75, in __init__
    self.populate_mspec()
  File "/felmarty/repos/rocprofiler-compute/build/install2/3.1.1/libexec/rocprofiler-compute/rocprof_compute_soc/soc_base.py", line 173, in populate_mspec
    amd_smi_mclk = amd_smi_mclk["gpu_data"][0]["clock"]["mem"]["frequency_levels"]
TypeError: list indices must be integers or slices, not str
```

### Linux Distribution

Ubuntu 22.04.5 LTS (Jammy Jellyfish)

### ROCm Compute Profiler Version

3.2.0 (release)

### GPU

AMD MI355

### ROCm Version

rocm-6.5.0

### Cluster name (if applicable)

_No response_

### Reproducer

```
import torch

a = torch.rand(5, 5, device="cuda")

res = a * a
```

and `CUDA_VISIBLE_DEVICES=0 ROCPROF=rocprofiler-sdk ROCPROFCOMPUTE_LOGLEVEL=debug rocprof-compute profile --rocprofiler-sdk-library-path /felmarty/repos/rocprofiler-sdk/rocprofiler-sdk-build/lib/librocprofiler-sdk.so --name foo --device 0 -- python bidon.py`

### Expected behavior

No error.

### Relevant log output

```shell

```

### Screenshots

_No response_

### Additional Context

_No response_

## 评论 (4)

### fxmarty-amd · 2025-07-28

This bug is probably caused by https://github.com/ROCm/rocprofiler-compute/pull/824 cc @vedithal-amd 

### vedithal-amd · 2025-07-28

@fxmarty-amd could you attach the output of amd-smi --clock --json on the machine where this issue was found

### fxmarty-amd · 2025-07-28

```
root@smci355-ccs-aus-m06-05:/felmarty/repos/gemms_lib# amd-smi static --clock --json
[
    {
        "gpu": 0,
        "clock": {
            "sys": {
                "current level": 1,
                "frequency_levels": {
                    "Level 0": "500 MHz",
                    "Level 1": "160 MHz",
                    "Level 2": "2400 MHz"
                }
            },
            "mem": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "2000 MHz"
                }
            },
            "df": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "1250 MHz"
                }
            },
            "soc": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "43 MHz",
                    "Level 1": "1200 MHz"
                }
            },
            "dcef": "N/A",
            "vclk0": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "59 MHz"
                }
            },
            "vclk1": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "59 MHz"
                }
            },
            "dclk0": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "48 MHz"
                }
            },
            "dclk1": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "48 MHz"
                }
            }
        }
    },
    {
        "gpu": 1,
        "clock": {
            "sys": {
                "current level": 1,
                "frequency_levels": {
                    "Level 0": "500 MHz",
                    "Level 1": "160 MHz",
                    "Level 2": "2400 MHz"
                }
            },
            "mem": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "2000 MHz"
                }
            },
            "df": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "1250 MHz"
                }
            },
            "soc": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "42 MHz",
                    "Level 1": "1200 MHz"
                }
            },
            "dcef": "N/A",
            "vclk0": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "59 MHz"
                }
            },
            "vclk1": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "59 MHz"
                }
            },
            "dclk0": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "48 MHz"
                }
            },
            "dclk1": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "48 MHz"
                }
            }
        }
    },
    {
        "gpu": 2,
        "clock": {
            "sys": {
                "current level": 1,
                "frequency_levels": {
                    "Level 0": "500 MHz",
                    "Level 1": "158 MHz",
                    "Level 2": "2400 MHz"
                }
            },
            "mem": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "2000 MHz"
                }
            },
            "df": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "1250 MHz"
                }
            },
            "soc": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "42 MHz",
                    "Level 1": "1200 MHz"
                }
            },
            "dcef": "N/A",
            "vclk0": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "59 MHz"
                }
            },
            "vclk1": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "59 MHz"
                }
            },
            "dclk0": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "48 MHz"
                }
            },
            "dclk1": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "48 MHz"
                }
            }
        }
    },
    {
        "gpu": 3,
        "clock": {
            "sys": {
                "current level": 1,
                "frequency_levels": {
                    "Level 0": "500 MHz",
                    "Level 1": "162 MHz",
                    "Level 2": "2400 MHz"
                }
            },
            "mem": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "2000 MHz"
                }
            },
            "df": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "1250 MHz"
                }
            },
            "soc": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "42 MHz",
                    "Level 1": "1200 MHz"
                }
            },
            "dcef": "N/A",
            "vclk0": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "59 MHz"
                }
            },
            "vclk1": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "59 MHz"
                }
            },
            "dclk0": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "48 MHz"
                }
            },
            "dclk1": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "48 MHz"
                }
            }
        }
    },
    {
        "gpu": 4,
        "clock": {
            "sys": {
                "current level": 1,
                "frequency_levels": {
                    "Level 0": "500 MHz",
                    "Level 1": "2407 MHz",
                    "Level 2": "2400 MHz"
                }
            },
            "mem": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "2000 MHz"
                }
            },
            "df": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "1250 MHz"
                }
            },
            "soc": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "42 MHz",
                    "Level 1": "1200 MHz"
                }
            },
            "dcef": "N/A",
            "vclk0": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "59 MHz"
                }
            },
            "vclk1": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "59 MHz"
                }
            },
            "dclk0": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "48 MHz"
                }
            },
            "dclk1": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "48 MHz"
                }
            }
        }
    },
    {
        "gpu": 5,
        "clock": {
            "sys": {
                "current level": 1,
                "frequency_levels": {
                    "Level 0": "500 MHz",
                    "Level 1": "2410 MHz",
                    "Level 2": "2400 MHz"
                }
            },
            "mem": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "2000 MHz"
                }
            },
            "df": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "1250 MHz"
                }
            },
            "soc": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "45 MHz",
                    "Level 1": "1200 MHz"
                }
            },
            "dcef": "N/A",
            "vclk0": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "59 MHz"
                }
            },
            "vclk1": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "59 MHz"
                }
            },
            "dclk0": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "48 MHz"
                }
            },
            "dclk1": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "48 MHz"
                }
            }
        }
    },
    {
        "gpu": 6,
        "clock": {
            "sys": {
                "current level": 1,
                "frequency_levels": {
                    "Level 0": "500 MHz",
                    "Level 1": "2404 MHz",
                    "Level 2": "2400 MHz"
                }
            },
            "mem": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "2000 MHz"
                }
            },
            "df": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "1250 MHz"
                }
            },
            "soc": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "42 MHz",
                    "Level 1": "1200 MHz"
                }
            },
            "dcef": "N/A",
            "vclk0": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "59 MHz"
                }
            },
            "vclk1": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "59 MHz"
                }
            },
            "dclk0": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "48 MHz"
                }
            },
            "dclk1": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "48 MHz"
                }
            }
        }
    },
    {
        "gpu": 7,
        "clock": {
            "sys": {
                "current level": 1,
                "frequency_levels": {
                    "Level 0": "500 MHz",
                    "Level 1": "2405 MHz",
                    "Level 2": "2400 MHz"
                }
            },
            "mem": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "2000 MHz"
                }
            },
            "df": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "1250 MHz"
                }
            },
            "soc": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "42 MHz",
                    "Level 1": "1200 MHz"
                }
            },
            "dcef": "N/A",
            "vclk0": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "59 MHz"
                }
            },
            "vclk1": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "59 MHz"
                }
            },
            "dclk0": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "48 MHz"
                }
            },
            "dclk1": {
                "current level": 0,
                "frequency_levels": {
                    "Level 0": "48 MHz"
                }
            }
        }
    }
]
```

### LionOfJewdah · 2025-07-29

I'm also affected by this issue
