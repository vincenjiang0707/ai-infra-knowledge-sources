# [Issue #1502] why onnx.load("resnet50_v1.pth") when I use pytorch backend?

source: https://github.com/mlcommons/inference/issues/1502
state: closed | updated: 2026-05-11T00:43:16Z
labels: Stale

## 正文

is not onnx.load() with args  "xxx.onnx"?
vision/classification_and_detection/python/backend_pytorch.py line 34:self.model = onnx.load(model_path)
when I run "./run_local.sh pytorch resnet50 cpu"  the backend_pytorch.py is called,but model_path is "resnet50_v1.pth" and it caused bug onnx can not load resnet50_v1.pth

## 评论 (12)

### nv-ananjappa · 2023-10-09

@pgmpablo157321 Please help.

### arjunsuresh · 2023-10-10

I don't think the reference resnet50 implementation supports pytorch backend. 

### qq1243196045 · 2023-10-10

> I don't think the reference resnet50 implementation supports pytorch backend.

OK,I think so too,but I found a "backend_pytorch_native.py",and it use torch.load() rather than onnx.load(),when I use it ,there were some errors and I was working to fix it

### arjunsuresh · 2023-10-20

@qq1243196045 did that work for you? AFAIK that backend is not tested with resnet50. 

### jgeorg02 · 2023-11-01

Hello, has anyone found any solution yet? I was wondering about the same thing

### qq1243196045 · 2023-11-02

> @qq1243196045 did that work for you? AFAIK that backend is not tested with resnet50.

yes,it's work after some fixed

### qq1243196045 · 2023-11-02

> Hello, has anyone found any solution yet? I was wondering about the same thing

I am try to use backend_pytorch_native.py and fixed some code,it's look like worked

### jgeorg02 · 2023-11-02

Has this code been pushed on github or have you done it locally? If you have done it locally, can you maybe share your code with us?
Thank you in advance!

### shata-wh · 2023-11-30

> > Hello, has anyone found any solution yet? I was wondering about the same thing
> 
> I am try to use backend_pytorch_native.py and fixed some code,it's look like worked

Hi, could you share how you fix the backend_pytorch_native.py? Thank you.

### datutu-L · 2024-01-26

> > Hello, has anyone found any solution yet? I was wondering about the same thing
> 
> I am try to use backend_pytorch_native.py and fixed some code,it's look like worked

Can you share how you solved it and your code, I need it badly, thanks!

### jgeorg02 · 2024-01-26

To be honest I saw that they have updated the code (in the repository) for backend_pytorch_native.py 3 months ago, but when I tried using it with the resnext50_32x4d_fpn.pth model I get the following as output (worker_1 is printed because I am running it inside a docker container):
```
worker_1  | Clearing caches.
worker_1  | 3
worker_1  | STARTING RUN AT 2024-01-26 09:50:47 AM
worker_1  | INFO:main:Namespace(accuracy=False, audit_conf='audit.config', backend='pytorch-native', cache=0, cache_dir=None, count=None, data_format=None, dataset='imagenet_pytorch', dataset_list=None, dataset_path='/mlperf/data/imagenet2012', debug=False, find_peak_performance=False, inputs=['image'], max_batchsize=32, max_latency=None, mlperf_conf='./mlperf.conf', model='/mlperf/model/resnext50_32x4d_fpn.pth', model_name='resnet50', output='/mlperf/output/', outputs=['ArgMax:0'], performance_sample_count=None, preprocessed_dir=None, profile='resnet50-pytorch', qps=None, samples_per_query=8, scenario='SingleStream', threads=8, time=60, use_preprocessed_dataset=False, user_conf='user.conf')
worker_1  | INFO:imagenet:Preprocessing 50000 images using 8 threads
worker_1  | /usr/local/lib/python3.6/site-packages/torchvision/transforms/functional.py:405: UserWarning: Argument interpolation should be of type InterpolationMode instead of int. Please, use InterpolationMode enum.
worker_1  |   "Argument interpolation should be of type InterpolationMode instead of int. "
worker_1  | INFO:imagenet:reduced image list, 49000 images not found
worker_1  | INFO:imagenet:loaded 1000 images, cache=0, already_preprocessed=False, took=8.3sec
worker_1  | /usr/local/lib/python3.6/site-packages/torch/serialization.py:604: UserWarning: 'torch.load' received a zip file that looks like a TorchScript archive dispatching to 'torch.jit.load' (call 'torch.jit.load' directly to silence this warning)
worker_1  |   " silence this warning)", UserWarning)
worker_1  | Traceback (most recent call last):
worker_1  |   File "python/main.py", line 626, in <module>
worker_1  |     main()
worker_1  |   File "python/main.py", line 505, in main
worker_1  |     model = backend.load(args.model, inputs=args.inputs, outputs=args.outputs)
worker_1  |   File "/benchmark/python/backend_pytorch_native.py", line 27, in load
worker_1  |     self.model = torch.load(model_path)
worker_1  |   File "/usr/local/lib/python3.6/site-packages/torch/serialization.py", line 606, in load
worker_1  |     return torch.jit.load(opened_file)
worker_1  |   File "/usr/local/lib/python3.6/site-packages/torch/jit/_serialization.py", line 164, in load
worker_1  |     cu, f.read(), map_location, _extra_files
worker_1  | RuntimeError: 
worker_1  | Unknown builtin op: aten::_upsample_nearest_exact1d.
worker_1  | Could not find any similar ops to aten::_upsample_nearest_exact1d. This op may not exist or may not be currently supported in TorchScript.
worker_1  | :
worker_1  |   File "/Users/pablogonzalez/opt/anaconda3/envs/vision/lib/python3.9/site-packages/torch/nn/functional.py", line 3896
worker_1  | 
worker_1  |     if input.dim() == 3 and mode == "nearest-exact":
worker_1  |         return torch._C._nn._upsample_nearest_exact1d(input, output_size, scale_factors)
worker_1  |                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ <--- HERE
worker_1  |     if input.dim() == 4 and mode == "nearest-exact":
worker_1  |         return torch._C._nn._upsample_nearest_exact2d(input, output_size, scale_factors)
worker_1  | Serialized   File "code/__torch__/torch/nn/functional/___torch_mangle_46.py", line 186
worker_1  |           _57 = False
worker_1  |         if _57:
worker_1  |           _60 = torch._upsample_nearest_exact1d(input, output_size2, scale_factors2)
worker_1  |                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ <--- HERE
worker_1  |           _59 = _60
worker_1  |         else:
worker_1  | 'interpolate' is being compiled since it was called from 'FeaturePyramidNetwork.forward'
worker_1  | Serialized   File "code/__torch__/model/feature_pyramid_network.py", line 11
worker_1  |   def forward(self: __torch__.model.feature_pyramid_network.FeaturePyramidNetwork,
worker_1  |     x: Dict[str, Tensor]) -> Dict[str, Tensor]:
worker_1  |     _0 = __torch__.torch.nn.functional.___torch_mangle_46.interpolate
worker_1  |     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ <--- HERE
worker_1  |     names = torch.list(torch.keys(x))
worker_1  |     x0 = torch.list(torch.values(x))
worker_1  | 
worker_1  | ENDING RUN AT 2024-01-26 09:51:20 AM
```

### github-actions[bot] · 2026-05-11

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
