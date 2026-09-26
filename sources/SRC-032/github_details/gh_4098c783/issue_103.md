# [Issue #103] DataLoader加载数据集时遇到：AttributeError: '_MultiProcessingDataLoaderIter' object has no attribute '_in_order'

source: https://github.com/Ascend/pytorch/issues/103
state: open | updated: 2026-02-13T01:32:37Z
labels: 

## 正文

### 环境信息

<img width="715" height="201" alt="Image" src="https://github.com/user-attachments/assets/41b51b8b-588e-49fa-80d3-e305ed8be68d" />

**CANN版本：**`8.5.0`

### 报错日志

```
Traceback (most recent call last):
  File "/home/BiRefNet/vision_npu_infer_dataloader.py", line 162, in <module>
    main(args)
  File "/home/BiRefNet/vision_npu_infer_dataloader.py", line 135, in main
    inference(
  File "/home/BiRefNet/vision_npu_infer_dataloader.py", line 29, in inference
    warmup_batch = next(iter(data_loader_test))
                        ^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/profiler/_add_mstx_patch.py", line 23, in _custom_dataloader_iter
    out_iter = original_iter(self)
               ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/data/dataloader.py", line 494, in __iter__
    return self._get_iterator()
           ^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torchvision_npu/utils/_dataloader.py", line 60, in _get_iterator
    return _MultiProcessingDataLoaderIter(self)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torchvision_npu/utils/_dataloader.py", line 207, in __init__
    self._reset(loader, first_iter=True)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/data/dataloader.py", line 1270, in _reset
    self._try_put_index()
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/data/dataloader.py", line 1529, in _try_put_index
    if self._in_order:
       ^^^^^^^^^^^^^^
AttributeError: '_MultiProcessingDataLoaderIter' object has no attribute '_in_order'
```


> 已经确定Torch版本自2.6.0开始新增`_in_order`且Torch代码正常执行,但torch_npu转换后出现该报错。具体定位请参考该[issue](https://github.com/pytorch/pytorch/issues/172215)。**求助可行的解决方案**

## 评论 (1)

### yunyiyun · 2026-02-13

感谢您的反馈，目前正在解决中
https://gitcode.com/Ascend/pytorch/issues/1533
