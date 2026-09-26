# [Issue #68] 卡在模型加载

source: https://github.com/Ascend/pytorch/issues/68
state: open | updated: 2025-07-04T01:17:10Z
labels: 

## 正文

使用transformers的model = AutoModelForCausalLM.from_pretrained(model_name_or_path, device_map='npu:0')
加载模型时卡住了：
/data/miniconda3/envs/env-3.10/lib/python3.10/site-packages/torch_npu/utils/collect_env.py:58: UserWarning: Warning: The /usr/local/Ascend/ascend-toolkit/latest owner does not match the current owner.
  warnings.warn(f"Warning: The {path} owner does not match the current owner.")
/data/miniconda3/envs/env-3.10/lib/python3.10/site-packages/torch_npu/utils/collect_env.py:58: UserWarning: Warning: The /usr/local/Ascend/ascend-toolkit/8.0.T13/x86_64-linux/ascend_toolkit_install.info owner does not match the current owner.
  warnings.warn(f"Warning: The {path} owner does not match the current owner.")
[2025-06-26 15:39:55,161] [INFO] [real_accelerator.py:239:get_accelerator] Setting ds_accelerator to npu (auto detect)
Sliding Window Attention is enabled but not implemented for `sdpa`; unexpected results may be encountered.
Loading checkpoint shards:   0%|                                                                                                          | 0/4 [00:00<?, ?it/s]
检查npu状态：
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc2.2               Version: 24.1.rc2.2                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 4     910B2C              | OK            | 93.7        52                0    / 0             |
| 0                         | 0000:DA:00.0  | 0           0    / 0          32446/ 65536         |
+===========================+===============+====================================================+
| 5     910B2C              | OK            | 98.7        55                0    / 0             |
| 0                         | 0000:99:00.0  | 0           0    / 0          3336 / 65536         |
+===========================+===============+====================================================+
| 6     910B2C              | OK            | 91.9        51                0    / 0             |
| 0                         | 0000:B8:00.0  | 0           0    / 0          3336 / 65536         |
+===========================+===============+====================================================+
| 7     910B2C              | OK            | 91.0        53                0    / 0             |
| 0                         | 0000:C8:00.0  | 0           0    / 0          3335 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 4       0                 | 154983        | pt_main_thread           | 29166                   |
+===========================+===============+====================================================+
| No running processes found in NPU 5                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 6                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 7                                                            |
+===========================+===============+====================================================+
这是什么原因导致的？

我的环境：
torch 2.4.0
torch-npu 2.4.0.post4
transformers 4.51.3
python 3.10.18



## 评论 (1)

### yunyiyun · 2025-07-04

卡住时可以采集堆栈，看下卡在哪里，
c++堆栈通过gdb采集
apt-get install gdb
gdb attach {pid}

python堆栈通过py-spy采集
pip3 install py-spy
py-spy dump -p {pid}
