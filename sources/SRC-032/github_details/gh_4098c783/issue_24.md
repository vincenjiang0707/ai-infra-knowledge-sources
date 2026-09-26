# [Issue #24] no module named torch_npu._C 

source: https://github.com/Ascend/pytorch/issues/24
state: open | updated: 2024-07-09T08:46:38Z
labels: 

## 正文

torch版本2.1 python版本3.8 执行python3 -c "import torch;import torch_npu; a = torch.randn(3, 4).npu(); print(a + a);"命令时，产生错误：
`Traceback (most recent call last):
  File "/data/package/pytorch/torch_npu/__init__.py", line 14, in <module>
    import torch_npu.npu
  File "/data/package/pytorch/torch_npu/npu/__init__.py", line 111, in <module>
    from .utils import (synchronize, device_count, can_device_access_peer, set_device, current_device, get_device_name,
  File "/data/package/pytorch/torch_npu/npu/utils.py", line 11, in <module>
    import torch_npu._C
ModuleNotFoundError: No module named 'torch_npu._C'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/data/package/pytorch/torch_npu/__init__.py", line 37, in <module>
    import torch_npu.npu.amp
  File "/data/package/pytorch/torch_npu/npu/__init__.py", line 111, in <module>
    from .utils import (synchronize, device_count, can_device_access_peer, set_device, current_device, get_device_name,
  File "/data/package/pytorch/torch_npu/npu/utils.py", line 11, in <module>
    import torch_npu._C
ModuleNotFoundError: No module named 'torch_npu._C'`

## 评论 (3)

### yunyiyun · 2024-03-20

是否是在编译目录下运行了这脚本，请切换到其他目录下运行

### supercz · 2024-04-30

同问。也遇到了No module named 'torch_npu._C'
![image](https://github.com/Ascend/pytorch/assets/7714802/c5e98c5f-f03a-489f-8be4-c46330977e26)


### shink · 2024-07-09

源码安装的话，在其他目录下执行 python 即可解决
