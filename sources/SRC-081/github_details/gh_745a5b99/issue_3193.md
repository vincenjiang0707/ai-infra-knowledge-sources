# [Issue #3193] [Bug]: import_from_path cannot load a preprocessing function from a file path

source: https://github.com/vllm-project/llm-compressor/issues/3193
state: open | updated: 2026-09-23T18:46:07Z
labels: 

## 正文

### Describe the bug

`import_from_path` documents three accepted forms, and
`TextGenerationDataset.preprocessing_func` repeats the first one in its own comment
(`# load func_name from "/path/to/file.py:func_name"`):

```
"/path/to/file.py:func_or_class_name"
"/path/to/file:focn"
"path.to.file:focn"
```

Only the third one works. Pointing `preprocessing_func` at a file — the documented way
to supply a custom calibration preprocessing function — always fails.

### Expected behavior

All three documented forms resolve the object.

### Steps to reproduce

```python
from pathlib import Path
from llmcompressor.utils import import_from_path

Path("myprep.py").write_text("def preprocess(example):\n    return example\n")

import_from_path(f"{Path('myprep.py').resolve()}:preprocess")   # absolute path
import_from_path("llmcompressor.pytorch.utils.helpers:get_quantized_layers")
```

Actual:

```
TypeError: the 'package' argument is required to perform a relative import for '.tmp.lcrepro.myprep'
AttributeError: Cannot find get_quantized_layers in llmcompressor.pytorch.utils.helpers
```

(the symbol does exist: `importlib.import_module("llmcompressor.pytorch.utils.helpers")`
resolves it fine)

### Cause

`importlib.import_module` takes dotted module names, not file system paths, so the
function first rewrites the path:

```python
path = original_path.split(".py")[0]
path = re.sub(r"/+", ".", path)
```

- A leading `/` becomes a leading `.`, so an absolute path becomes a relative import and
  raises `TypeError`. That is not an `ImportError`, so the surrounding handler does not
  catch it and the intended `Cannot find module with path ...` message never appears.
- `split(".py")` cuts at the first `.py` substring anywhere, not at the extension, so a
  dotted path is truncated at any package starting with `py`.
  `llmcompressor.pytorch.utils.helpers` becomes `llmcompressor`, which imports fine — so
  the wrong module is searched and the failure surfaces as a misleading `AttributeError`.
- Separately, `path.split(":")` raises `too many values to unpack` on a Windows drive
  letter such as `C:/models/prep.py:preprocess`.

### Proposed fix

Load the module from the file when the path points at one
(`importlib.util.spec_from_file_location`), falling back to `importlib.import_module`
for dotted names, and split the object name with `rsplit(":", 1)`.

`import_from_path` currently has no test coverage; I would add tests for the three
documented forms and both error paths.

### Environment

`main` at 6693441, Python 3.12.

---

I have this ready and would like to open the PR if the approach looks right.


## 评论 (3)

### kylesayrs · 2026-09-23

Thanks for reporting the issue! Given that we have [examples](https://github.com/vllm-project/llm-compressor/blob/main/examples/custom_dataset_example.py) on how do custom and advanced dataset processing for calibration, it would be best to remove the `preprocessing_func` feature entirely.

It's better to have LLM Compressor focus on the actual application of algorithms: any advanced dataset processing beyond basic cases can be handled natively outside of the library.

Let me know what you think of this approach. Would you be interested in helping to deprecate and remove this feature? 

### Evihut · 2026-09-23

That makes sense to me, and I’d be happy to help with the deprecation and removal. I can take a first pass at the code, tests, and migration docs, and close #3194 as superseded. If you have a preferred way to stage the change, I’d be glad to follow your guidance.

### kylesayrs · 2026-09-23

@Evihut I think that plan sounds great! Feel free to message me or any of the other maintainers of the project to add the `ready` label so that our CI will run and verify that tests pass
