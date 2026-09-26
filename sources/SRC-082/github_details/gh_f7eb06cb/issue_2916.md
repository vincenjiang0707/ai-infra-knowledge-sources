# [Issue #2916] [BUG] Error with latest transformers: module 'transformers.utils.hub' has no attribute 'create_repo'

source: https://github.com/ModelCloud/GPTQModel/issues/2916
state: closed | updated: 2026-06-09T08:37:01Z
labels: bug

## 正文

**Describe the bug**

Heads up: Importing `gptqmodel` with the latest transformers from main (`595721c44cb14db37fa504903e2edd5e9f0eba43`) results in an error:

> AttributeError: module 'transformers.utils.hub' has no attribute 'create_repo'

You should import the function directly from `huggingface_hub`.

**To Reproduce**

`python -c "import gptqmodel"`

**Expected behavior**

No error.

## 评论 (5)

### IlyasMoutawwakil · 2026-06-04

@Qubitium will there be a patch soon ? optimum ci is also failing bcz of this  🙏

### Qubitium · 2026-06-04

@BenjaminBossan  @IlyasMoutawwakil The issue has been fixed in `main` and will push a new release in the next 24 hours.

### selfhypnosis-ai · 2026-06-05

@Qubitium @Anai-Guo Thanks for the quick fix on create_repo!

However, it looks like you missed a few other functions. The latest transformers branch (5.5.0+) dropped the passthrough for several other Hugging Face Hub functions that gptqmodel/utils/hub.py still tries to re-export.

If you pull main right now, the import still crashes on list_repo_tree:


AttributeError: module 'transformers.utils.hub' has no attribute 'list_repo_tree'
To fully fix the transformers >= 5.5.0 compatibility, you'll need to update gptqmodel/utils/hub.py to import these directly from huggingface_hub as well:

list_repo_tree
hf_hub_download
has_file
cached_file (Note: depending on the transformers version, you might need to use huggingface_hub.hf_hub_download or try/except fallbacks for cached_file).

### Anai-Guo · 2026-06-08

@selfhypnosis-ai Thanks for following up! Good news — `list_repo_tree`, `hf_hub_download` (and `snapshot_download`, `create_repo`) are already imported directly from `huggingface_hub` on current `main` of `gptqmodel/utils/hub.py`, so those crashes are resolved.

On `cached_file` and `has_file` — those two are a different case. They aren't huggingface_hub re-exports that transformers dropped; they're transformers-native helpers and are still defined in `transformers.utils.hub` on 5.5.0+ (`cached_file` and `has_file` are real `def`s in that module, not passthroughs). `huggingface_hub` itself has no `cached_file`/`has_file` symbol (it exposes `hf_hub_download` and `file_exists` instead), so re-pointing them at `huggingface_hub` would actually raise `AttributeError` on import. They should keep coming from `transformers.utils.hub`.

If you're still hitting an `AttributeError` on `cached_file`/`has_file` specifically, could you share the transformers version and full traceback? That would point to a genuinely different breakage rather than the re-export drop this issue was about.

### selfhypnosis-ai · 2026-06-09

@Anai-Guo Thanks for the clarification! You're completely right. I just double-checked my local monkey patch, and I only had to patch list_repo_tree, create_repo, and hf_hub_download to get things working. I incorrectly assumed cached_file and has_file were also dropped passthroughs, but since they are native to transformers.utils.hub, I wasn't actually getting an AttributeError for them.

The current fix on main mapping the first three to huggingface_hub covers everything. Thanks for looking into it and getting it resolved so quickly!
