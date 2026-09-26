# [Issue #1538] Stable Diffusion reference implementation is giving error on the accuracy run

source: https://github.com/mlcommons/inference/issues/1538
state: closed | updated: 2026-07-09T00:38:05Z
labels: Stale

## 正文

Please see below for the detailed output. The run is done on Nvidia RTX 4090 GPU. 
```
CMD: /home/arjun/cm/bin/python3 main.py  --scenario SingleStream --profile stable-diffusion-xl-pytorch  --dataset coco-1024 --dataset-path /home/arjun/CM/repos/local/cache/03fbdcf95b3d4104/install --dtype fp16 --device cuda   --mlperf_conf '/home/arjun/CM/repos/local/cache/01e6e649e68a4f4f/inference/mlperf.conf' --threads 1 --user_conf '/home/arjun/CM/repos/ctuning@mlcommons-ck/cm-mlops/script/generate-mlperf-inference-user-conf/tmp/afbce073b18f4a15aaf7a93de4f4573c.conf' --accuracy --output /home/arjun/CM/repos/local/cache/81fdb92a61e14ebf/inference/text_to_image/valid_results/arjun_spr-reference-gpu-pytorch-v2.1.1-default_config/sdxl/singlestream/accuracy 

INFO:main:Namespace(dataset='coco-1024', dataset_path='/home/arjun/CM/repos/local/cache/03fbdcf95b3d4104/install', profile='stable-diffusion-xl-pytorch', scenario='SingleStream', max_batchsize=1, threads=1, accuracy=True, find_peak_performance=False, backend='pytorch', model_name='stable-diffusion-xl', output='/home/arjun/CM/repos/local/cache/81fdb92a61e14ebf/inference/text_to_image/valid_results/arjun_spr-reference-gpu-pytorch-v2.1.1-default_config/sdxl/singlestream/accuracy', qps=None, model_path=None, dtype='fp16', device='cuda', latent_framework='torch', mlperf_conf='/home/arjun/CM/repos/local/cache/01e6e649e68a4f4f/inference/mlperf.conf', user_conf='/home/arjun/CM/repos/ctuning@mlcommons-ck/cm-mlops/script/generate-mlperf-inference-user-conf/tmp/afbce073b18f4a15aaf7a93de4f4573c.conf', audit_conf='audit.config', time=None, count=None, debug=False, performance_sample_count=5000, max_latency=None, samples_per_query=8)
WARNING:backend-pytorch:Model path not provided, running with default hugging face weights
This may not be valid for official submissions
Keyword arguments {'safety_checker': None} are not expected by StableDiffusionXLPipeline and will be ignored.
Loading pipeline components...:   0%|                                                                                                             | 0/7 [00:00<?, ?it/s]2023-12-20 17:06:02.182119: I tensorflow/core/util/port.cc:111] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
2023-12-20 17:06:02.232059: E tensorflow/compiler/xla/stream_executor/cuda/cuda_dnn.cc:9342] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
2023-12-20 17:06:02.232150: E tensorflow/compiler/xla/stream_executor/cuda/cuda_fft.cc:609] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
2023-12-20 17:06:02.232190: E tensorflow/compiler/xla/stream_executor/cuda/cuda_blas.cc:1518] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
2023-12-20 17:06:02.244117: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 AVX512F AVX512_VNNI AVX512_BF16 AVX_VNNI AMX_TILE AMX_INT8 AMX_BF16 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-12-20 17:06:03.163145: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
Loading pipeline components...: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████| 7/7 [00:03<00:00,  1.78it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:03<00:00,  6.33it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.67it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.67it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.67it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.66it/s]
INFO:main:starting TestScenario.SingleStream
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.67it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.66it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.66it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.65it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.64it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.63it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.64it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.64it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.63it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.64it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.63it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.64it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.63it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.63it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.62it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.62it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.62it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.62it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.62it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.62it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.62it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.60it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.62it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.61it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.61it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.61it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.61it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.61it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.60it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.60it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.56it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.52it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.53it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.49it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.50it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.49it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.47it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.45it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.47it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.50it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.49it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.48it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.46it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.48it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.53it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.48it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.49it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.52it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.52it/s]
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 20/20 [00:02<00:00,  7.54it/s]
INFO:root:Loading pretrained ViT-B-32 from OpenAI.
INFO:coco:Accumulating results
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [00:14<00:00,  3.43it/s]
Traceback (most recent call last):
  File "/home/arjun/CM/repos/local/cache/81fdb92a61e14ebf/inference/text_to_image/main.py", line 478, in <module>
    main()
  File "/home/arjun/CM/repos/local/cache/81fdb92a61e14ebf/inference/text_to_image/main.py", line 462, in main
    post_proc.finalize(result_dict, ds, output_dir=args.output)
  File "/home/arjun/CM/repos/local/cache/81fdb92a61e14ebf/inference/text_to_image/coco.py", line 180, in finalize
    fid_score = compute_fid(self.results, self.statistics_path, self.device)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/arjun/CM/repos/local/cache/81fdb92a61e14ebf/inference/text_to_image/tools/fid/fid_score.py", line 359, in compute_fid
    fid_value = calculate_frechet_distance(m1, s1, m2, s2)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/arjun/CM/repos/local/cache/81fdb92a61e14ebf/inference/text_to_image/tools/fid/fid_score.py", line 194, in calculate_frechet_distance
    raise ValueError("Imaginary component {}".format(m))
ValueError: Imaginary component 7.01901254862071e+103
```

## 评论 (6)

### nvyihengz · 2024-01-12

I am getting similar errors with scipy==1.9.1. In my case it seems that the root cause is numpy>=1.23 used. 

### arjunsuresh · 2024-07-08

@nvyihengz that's true. Considering numpy 1.22 is quite old we should fix this for inference 5.0

@anandhu-eng 

### nvyihengz · 2024-07-08

@arjunsuresh so far NVIDIA has been using a separate virtual env for SDXL accuracy testing (https://github.com/mlcommons/inference_results_v4.0/blob/main/closed/NVIDIA/code/stable-diffusion-xl/tensorrt/accuracy_requirements.txt), which is not a very elegant approach. I agree this issue should be looked into in the next round.

### arjunsuresh · 2024-07-08

Thank you @nvyihengz Interestingly there is no `numpy` in the accuracy environment for SDXL whereas the original Nvidia requirements has `numpy==1.22`. We had to install `numpy==1.22` in the accuracy environment to get rid of this error while running Nvidia v4.0 code for SDXL. (We were reproducing this environment in a non-Nvidia docker container).

### nvyihengz · 2024-07-08

@arjunsuresh If I remember correctly, scipy will install numpy as a dependency. The venv is built from bare metal following the reference implementation (https://github.com/mlcommons/inference/blob/master/text_to_image/requirements.txt) so it does not inherit NVIDIA's container packages.

### github-actions[bot] · 2026-07-09

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
