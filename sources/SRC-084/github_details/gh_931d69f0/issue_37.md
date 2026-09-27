# [Issue #37] Reuse Huggingface model cache directory as standard

source: https://github.com/dropbox/hqq/issues/37
state: closed | updated: 2024-05-06T16:30:41Z
labels: bug

## 正文

As the idea is it seems (or should be?) minimizing the compute resources needed for these models, one useful optimization is to avoid unnecessarily re-downloading models from Huggingface (when for instance they have already been downloaded with the `huggingface_hub` API to the standard cache directory such as `~/.cache/huggingface/hub/`)
```
diff --git a/hqq/models/base.py b/hqq/models/base.py
index e305391..2ba7fa1 100755
--- a/hqq/models/base.py
+++ b/hqq/models/base.py
@@ -282,7 +283,10 @@ class BaseHQQModel:
         save_dir = pjoin(cache_dir, save_dir_or_hub)
 
         if not os.path.exists(save_dir):
-            save_dir = snapshot_download(repo_id=save_dir_or_hub, cache_dir=cache_dir)
+            if cache_dir == "":
+                save_dir = snapshot_download(repo_id=save_dir_or_hub)
+            else:
+                save_dir = snapshot_download(repo_id=save_dir_or_hub, cache_dir=cache_dir)
             save_dir = pjoin(save_dir)
 
         # Check
```

may need some adjustment according to how you were intending it should work; for instance, I think my code would not create a (new) copy in a directory more local to the cwd (though it should? handle older files downloaded to such locations), you may think you need to add that for the sake of matching the original functionality

## 评论 (8)

### mobicham · 2024-04-02

Hi @MarkBenjamin , does it re-download the model if you pass the cache_dir as a parameter ?
```Python
model  = HQQModelForCausalLM.from_pretrained(model_id, cache_dir=cache_path, torch_dtype=compute_dtype, attn_implementation=attn_imp)
```

### MarkBenjamin · 2024-04-02

It seems to try to
`HQQModelForCausalLM.from_quantized('mobiuslabsgmbh/Llama-2-7b-chat-hf_1bitgs8_hqq', cache_dir='/home/mark/.cache/huggingface/hub/')` for instance

### MarkBenjamin · 2024-04-02

it looks as though `cache_dir` isn't being passed from `HQQWrapper.from_quantized()` to `BaseHQQModel.try_snapshot_download()`
```
diff --git a/hqq/engine/base.py b/hqq/engine/base.py
index 27b3050..e2f4acf 100755
--- a/hqq/engine/base.py
+++ b/hqq/engine/base.py
@@ -74,12 +74,12 @@ class HQQWrapper:
         cls,
         save_dir_or_hub,
         compute_dtype: torch.dtype = float16,
-        device="cuda",
-        cache_dir: str = "",
+        device=torch.device('cuda' if torch.cuda.is_available() else 'cpu'),
+        cache_dir: str | None = "",
         adapter: str = None,
     ):
         # Both local and hub-support
-        save_dir = BaseHQQModel.try_snapshot_download(save_dir_or_hub)
+        save_dir = BaseHQQModel.try_snapshot_download(save_dir_or_hub, cache_dir=cache_dir)
         arch_key = cls._get_arch_key_from_save_dir(save_dir)
         cls._check_arch_support(arch_key)
``` 
however even after that change, `HQQModelForCausalLM.from_quantized('mobiuslabsgmbh/Llama-2-7b-chat-hf_1bitgs8_hqq', cache_dir=None)` is trying to re-download the model

### mobicham · 2024-04-02

You need to put here as well: https://github.com/mobiusml/hqq/blob/master/hqq/models/base.py#L303 
That part in ```/hqq/engine/base.py``` is not supposed to download the whole repo, only the ```config.json``` to figure out which architecture the model is, but somehow forgot to change it. 

I actually don't see this issue. Just use a fixed ```cache_dir```, like ```cache_dir=''``` and it should work just fine. 

### MarkBenjamin · 2024-04-02

I seem to have it working now (possibly the most necessary change is the passing of the `cache_dir` value from `HQQWrapper.from_quantized()` to `BaseHQQModel.try_snapshot_download()`), whether I specify the huggingface cache path or specifically send `None` (that then needs guarding the `pjoin()` call); the diff (plus some type hints allowing specifically passing `None`; including in `BaseHQQModel.from_quantized()` as you suggest) cleaned of the torch cpu code would be
```
diff --git a/hqq/engine/base.py b/hqq/engine/base.py
index 27b3050..a767fad 100755
--- a/hqq/engine/base.py
+++ b/hqq/engine/base.py
@@ -75,11 +75,11 @@ class HQQWrapper:
         save_dir_or_hub,
         compute_dtype: torch.dtype = float16,
         device="cuda",
-        cache_dir: str = "",
+        cache_dir: str | None = "",
         adapter: str = None,
     ):
         # Both local and hub-support
-        save_dir = BaseHQQModel.try_snapshot_download(save_dir_or_hub)
+        save_dir = BaseHQQModel.try_snapshot_download(save_dir_or_hub, cache_dir=cache_dir)
         arch_key = cls._get_arch_key_from_save_dir(save_dir)
         cls._check_arch_support(arch_key)
 
diff --git a/hqq/models/base.py b/hqq/models/base.py
index e305391..7ba9494 100755
--- a/hqq/models/base.py
+++ b/hqq/models/base.py
@@ -278,8 +278,11 @@ class BaseHQQModel:
         cls.save_weights(weights, save_dir)
 
     @classmethod
-    def try_snapshot_download(cls, save_dir_or_hub: str, cache_dir: str = ""):
-        save_dir = pjoin(cache_dir, save_dir_or_hub)
+    def try_snapshot_download(cls, save_dir_or_hub: str, cache_dir: str | None = ""):
+        if cache_dir is None:
+            save_dir = pjoin("", save_dir_or_hub)
+        else:
+            save_dir = pjoin(cache_dir, save_dir_or_hub)
 
         if not os.path.exists(save_dir):
             save_dir = snapshot_download(repo_id=save_dir_or_hub, cache_dir=cache_dir)
@@ -305,13 +308,11 @@ class BaseHQQModel:
         save_dir_or_hub,
         compute_dtype: torch.dtype = float16,
         device="cuda",
-        cache_dir: str = "",
+        cache_dir: str | None = "",
         adapter: str = None,
     ):
         # Get directory path
         save_dir = cls.try_snapshot_download(save_dir_or_hub, cache_dir)
-
-        # Load model from config
         model = cls.create_model(save_dir)
 
         # Track save directory
```

I guess you wouldn't see it unless you have already (or subsequently?) directly called
```
from huggingface_hub import snapshot_download
snapshot_download('mobiuslabsgmbh/Llama-2-7b-chat-hf_1bitgs8_hqq')
```
unless your envvars have altered the `HF_HUB_CACHE` or (legacy) `HUGGINGFACE_HUB_CACHE` or (climbing the tree) `HF_HOME` or `XDG_CACHE_HOME` values, or more generally some coincidence between the substitution for "" as `cache_dir` (your working directory?) / `HF_HUB_CACHE` value

### mobicham · 2024-04-09

Sorry @MarkBenjamin , I missed this. 

In general, if you specify the cache directory when you load via `from_pretrained` this problem doesn't happen. At least, no one has reported this issue before. 

I can try using the logic you mentioned in ```try_snapshot_download``` or you can do a pull request if you want, happy to review it !

### MarkBenjamin · 2024-04-09

Will do 🙂

Best regards

Mark

### mobicham · 2024-05-06

Closing since this was merged, thanks!
