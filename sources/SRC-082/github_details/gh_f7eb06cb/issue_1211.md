# [Issue #1211] [BUG] HF HUB auto-upload (push_to_hub) compat

source: https://github.com/ModelCloud/GPTQModel/issues/1211
state: closed | updated: 2026-03-31T03:34:58Z
labels: bug

## 正文

The quantization config JSON file is not pushed to the hub when running:
```
model.push_to_hub
```

The quantization config should be added to the config.json before the upload and when the model is saved locally. 

Currently, without the quantization config, Transformers can run the model anyway but the output will be very bad. Once I added the quantization config to the config.json, it worked as expected.

## 评论 (5)

### Qubitium · 2025-02-04

@benjamin-marie  Can you point me or provide the content of the `config.json` auto-pushed to HF? We need to check the json content. Also the exact cli you executed to push your uploaded model.

### benjamin-marie · 2025-02-04

I don't do CLI. I only do this:
```
quant_config = QuantizeConfig(bits=b, group_size=128)

  model = GPTQModel.load(m, quant_config)

  model.quantize(calibration_dataset, batch_size=2)
  model.save(quant_path)
  model.push_to_hub(myrepo)
```

This doesn't upload the quantization config. The config.json is the standard one serialized with the model. It must be edited. Here is one that works (manually modified to add the quantization_config):
```
https://huggingface.co/kaitchup/Qwen2.5-7B-Instruct-gptqmodel-8bit/blob/main/config.json
```

### Qubitium · 2025-02-04

@benjamin-marie  Ha! I noticed you uploaded all those gptqmodel quants to HF and I did see they were all missing quant_config. Now I know the reason why. =)

We never ci-tested this feature (hf_hub) integration. Now I see where the exact problem is. Will fix this in `main` soon.



### Qubitium · 2025-02-04

@benjamin-marie  Fixed in PR #1216

Due to compat issues which we may never fix or even worth fixing since it requires ugly hacks to transformer code, we will not allow `model.push_to_hub()` (model instance call). If you call this now, it will just log an error but not crash. 

Instead we are offering a `static` api call using `GPTQModel.push_to_hub()` with same api params you are used to with additional required `quantized_path`:

```py
 GPTQModel.push_to_hub(
      repo_id="ModelCloud/CiUploadTest",
      quantized_path=path_to_saved_quantized_model,
      private=True,
  )
```

### djaffer · 2026-03-31

This doesn't work it keep throwing error.  GPTQModel.push_to_hub fails. due to token not being passed. Looks like no one tested it or was using env variables.

HfHubHTTPError: Client error '401 Unauthorized' for url 'https://huggingface.co/api/repos/create' (Request ID: Root=1-69cb3964-6d83573c136795bd0d12086a;19ffaf14-2475-4f1e-b862-8f204f6e89bc)
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401
Invalid username or password

New Issue created for tracking:
https://github.com/ModelCloud/GPTQModel/issues/2632

**Solution**

There is bug when otherwise upload_large_folder fails.
https://github.com/ModelCloud/GPTQModel/blob/8fb2e3154cf1d9b18969c231a990eeb8763d2648/gptqmodel/models/auto.py#L579

api = HfApi()
should be
api = HfApi(token=token)
