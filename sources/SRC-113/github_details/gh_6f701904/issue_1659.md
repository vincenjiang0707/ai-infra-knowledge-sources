# [Issue #1659] [Text-to-image] Run benchmark section failed to execute due to various errors

source: https://github.com/mlcommons/inference/issues/1659
state: closed | updated: 2026-05-06T00:40:55Z
labels: Stale

## 正文

Hi @arjunsuresh and @gfursin,

I facing errors in the run benchmark section in the text-to-image section. 

```
user@AIMLPerf-NVMe:~/CM/repos/local/cache/57064143a0ce4ff2/inference/text_to_image/model$ cd $SD_FOLDER
user@AIMLPerf-NVMe:~/CM/repos/local/cache/57064143a0ce4ff2/inference/text_to_image$ python3 main.py --dataset "coco-1024" --dataset-path coco2014 --profile stable-diffusion-xl-pytorch --model-path model/ --device cuda --scenario Offline
/home/user/.local/lib/python3.10/site-packages/transformers/utils/generic.py:311: UserWarning: torch.utils._pytree._register_pytree_node is deprecated. Please use torch.utils._pytree.register_pytree_node instead.
  torch.utils._pytree._register_pytree_node(
INFO:main:Namespace(dataset='coco-1024', dataset_path='coco2014', profile='stable-diffusion-xl-pytorch', scenario='Offline', max_batchsize=1, threads=1, accuracy=False, find_peak_performance=False, backend='pytorch', model_name='stable-diffusion-xl', output='output', qps=None, model_path='model/', dtype='fp32', device='cuda', latent_framework='torch', mlperf_conf='mlperf.conf', user_conf='user.conf', audit_conf='audit.config', ids_path='tools/sample_ids.txt', time=None, count=None, debug=False, performance_sample_count=5000, max_latency=None, samples_per_query=8)
/home/user/.local/lib/python3.10/site-packages/transformers/utils/generic.py:311: UserWarning: torch.utils._pytree._register_pytree_node is deprecated. Please use torch.utils._pytree.register_pytree_node instead.
  torch.utils._pytree._register_pytree_node(
Traceback (most recent call last):
  File "/home/user/.local/lib/python3.10/site-packages/huggingface_hub/utils/_errors.py", line 304, in hf_raise_for_status
    response.raise_for_status()
  File "/usr/lib/python3/dist-packages/requests/models.py", line 943, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: https://huggingface.co/model/checkpoint_scheduler/resolve/main/scheduler/scheduler_config.json

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/user/.local/lib/python3.10/site-packages/diffusers/configuration_utils.py", line 370, in load_config
    config_file = hf_hub_download(
  File "/home/user/.local/lib/python3.10/site-packages/huggingface_hub/utils/_validators.py", line 118, in _inner_fn
    return fn(*args, **kwargs)
  File "/home/user/.local/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 1403, in hf_hub_download
    raise head_call_error
  File "/home/user/.local/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 1261, in hf_hub_download
    metadata = get_hf_file_metadata(
  File "/home/user/.local/lib/python3.10/site-packages/huggingface_hub/utils/_validators.py", line 118, in _inner_fn
    return fn(*args, **kwargs)
  File "/home/user/.local/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 1667, in get_hf_file_metadata
    r = _request_wrapper(
  File "/home/user/.local/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 385, in _request_wrapper
    response = _request_wrapper(
  File "/home/user/.local/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 409, in _request_wrapper
    hf_raise_for_status(response)
  File "/home/user/.local/lib/python3.10/site-packages/huggingface_hub/utils/_errors.py", line 352, in hf_raise_for_status
    raise RepositoryNotFoundError(message, response) from e
huggingface_hub.utils._errors.RepositoryNotFoundError: 401 Client Error. (Request ID: Root=1-65e96225-562004e91bbbf85d6a9b2fe4;706ba79e-e90e-4bee-8edf-b3d24abb0a58)

Repository Not Found for url: https://huggingface.co/model/checkpoint_scheduler/resolve/main/scheduler/scheduler_config.json.
Please make sure you specified the correct `repo_id` and `repo_type`.
If you are trying to access a private or gated repo, make sure you are authenticated.
Invalid username or password.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/user/CM/repos/local/cache/57064143a0ce4ff2/inference/text_to_image/main.py", line 498, in <module>
    main()
  File "/home/user/CM/repos/local/cache/57064143a0ce4ff2/inference/text_to_image/main.py", line 344, in main
    model = backend.load()
  File "/home/user/CM/repos/local/cache/57064143a0ce4ff2/inference/text_to_image/backend_pytorch.py", line 78, in load
    self.scheduler = EulerDiscreteScheduler.from_pretrained(
  File "/home/user/.local/lib/python3.10/site-packages/diffusers/schedulers/scheduling_utils.py", line 140, in from_pretrained
    config, kwargs, commit_hash = cls.load_config(
  File "/home/user/.local/lib/python3.10/site-packages/diffusers/configuration_utils.py", line 384, in load_config
    raise EnvironmentError(
OSError: model/checkpoint_scheduler is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'
If this is a private repository, make sure to pass a token having permission to this repo with `use_auth_token` or log in with `huggingface-cli login`.

```

## 评论 (4)

### gfursin · 2024-03-07

Thank you for your feedback @willamloo3192 . We are very busy with the inference v4.0 release and will check it as soon as it's done. 

### arjunsuresh · 2024-03-07

If the model path is incorrect, the MLPerf implementation tries to download the model from huggingface. Due to the proxy issue, it might be failing here. 

### willamloo3192 · 2024-03-08

@arjunsuresh noted. But for the huggingface part, it seems the link is having issue. I tried access manually from my side, it shows error 404. Can I give suggestion that possible that we clone the model from primary repo to the git repo, so it opened to all company that have proxy issue. 

### github-actions[bot] · 2026-05-06

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
