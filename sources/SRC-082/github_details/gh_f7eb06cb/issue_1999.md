# [Issue #1999] Jupyter Notebook Progress Printing

source: https://github.com/ModelCloud/GPTQModel/issues/1999
state: closed | updated: 2025-12-24T09:14:55Z
labels: 

## 正文

I'm using GPTQModel within a Jupyter Notebook (a `.ipynb` file). I access the notebook through VSCode with the respective extensions (Python + Jupyter Notebook).

Now when I use `pip install gptqmodel`, then everything works fine. In particular, when I run `model.quantize(calibration_dataset, batch_size=1)` then it displays a nice table, that gets more and more rows, and on the bottom there is a progress bar which fills slowly.

Now however, I wanted to make some modifications to the repo, so I did:
```
git clone https://github.com/ModelCloud/GPTQModel
cd GPTQModel
pip install -e .
```
This installs the package as a local editable version. And of course it gives me the newest code from GitHub instead of just the latest release.

With this setup, however, I have an issue. When I now run `model.quantize(calibration_dataset, batch_size=1)` then:
- There is no more nice table and filling progress bar.
- Instead, I feel like this "update rendering" mechanism fails and I just see a lot of text (containing the progress bar) being outputted constantly.
- The main problem: This freezes my VSCode. Then I have to terminate the process. So I can't use `model.quantize(...)` at all.

Do you have any ideas what could be the cause of this problem and how to fix it?

(I'm not sure if it's because of the latest GitHub code or because of the local installation.)

## 评论 (8)

### jbirnick · 2025-10-09

I found out that the rendering is based on [LogBar](https://github.com/modelcloud/logbar), so I tested this on its own.

Suprisingly, this simple example here doesn't work properly for me:
```
import time
from logbar import LogBar

log = LogBar.shared()

pb_fetch = log.pb(range(80)).title("Fetch").manual()
pb_train = log.pb(range(120)).title("Train").manual()

for _ in pb_fetch:
    pb_fetch.draw()
    time.sleep(0.01)

for _ in pb_train:
    pb_train.draw()
    time.sleep(0.01)

pb_train.close()
pb_fetch.close()
```
The output for me looks as follows, tested both in VSCode and in Jupyter Lab:

<img width="664" height="912" alt="Image" src="https://github.com/user-attachments/assets/631c116f-e55a-43e0-81f9-c79a9a140ebf" />


### Qubitium · 2025-10-10

-@jbirnick To calrify, logbar sample code is rendering each progress as a new line rather than updating on the same line correct? In vscode, jupyter.

### jbirnick · 2025-10-10

Yes that seems to be what's happening. Both in Jupyter Lab and in VS Code with the Jupyter Notebook extension.

(It works with only a single progress bar, but the example above doesn't work.)

### Qubitium · 2025-10-10

@jbirnick  Fixed. Try installing latest logbar with below. Let me know if it fully fixes your issue.

```bash
pip install git+https://github.com/modelcloud/logbar.git
```

### jbirnick · 2025-10-10

The pure logbar example from above indeed works now. However, **the original problem still persists.** In particular:
- When running `model.quantize(...)` the output is still not formatted properly.
- My VSCode still freezes when running `model.quantize(...)`.

It works for me in commit `db41ae4` (the `v4.2.5` release) but not in the latest commit `835e50e`.
I tried running `git bisect` to find out in which commit the issue was introduced, however, I can't even run `model.quantize(...)` in most commits in-between those two commits because I get:
```
ImportError: cannot import name 'PytorchGELUTanh' from 'transformers.activations' (/usr/local/lib/python3.12/dist-packages/transformers/activations.py)
```

Could you perhaps try to run the following script in a Jupyter Notebook from VSCode (using the Jupyter Notebook extension), on the latest commit? After a couple of seconds it should start to lag, and when you then try to stop the cell it shouldn't work.
```
from datasets import load_dataset
from gptqmodel import GPTQModel, QuantizeConfig

model_id_orig = "meta-llama/Llama-3.2-1B-Instruct"
model_path_quant = "Llama-3.2-1B-Instruct-gptqmodel-4bit"

calibration_dataset = load_dataset(
    "allenai/c4",
    data_files="en/c4-train.00001-of-01024.json.gz",
    split="train"
  ).select(range(1024))["text"]

quant_config = QuantizeConfig(bits=4, group_size=128)
model = GPTQModel.load(model_id_orig, quant_config)


# This freezes my VSCode when running on the latest commit `db41ae4`
# (To be precise, it makes everything extremely laggy, and when I try to stop the cell it doesn't work, and then I have to kill the process.)
model.quantize(calibration_dataset, batch_size=1)
```

Or you could perhaps also tell me how to fix this `ImportError` so that I can run `git bisect`.

### Qubitium · 2025-10-10

@jbirnick The bug is in logbar compat with juptyer. Can you launch junpyter notebook and run your quant code and double check? This may be a bug with vscode juptyer extension.

### jbirnick · 2025-10-11

I checked again, and it doesn't give the lag and the many newlines, both in Jupyter Notebook and in VS Code. (I guess my previous check had some mistake in it like not reloading the kernel or so.)

However, there are other bugs now:
- The table is printed to the output of the _previous_ cell ?!
- in VSCode it somehow creates a new (completely separate) cell output for each log message or so, and empty outputs in between?!

I looked at your fix and it seemed to be quite a few lines, and it seemed a bit hacky (detecting in which environment you're in etc.) If I may suggest, I don't think such a hack is necessary, and I think it would be better to keep things simple. Please note that everything works perfectly in commit `db41ae4` with logbar `v0.0.4`. Maybe it would be better to see what caused the issue and make a clean, non-hacky fix?

### Qubitium · 2025-10-11

@jbirnick I wish it was easier fix too. Jupyter has its own terminal display and it is a hack itself. I will test on notebook to why it would print to prev cell.

You have to keep in mind why juptyer terminal is presenting itself as a terminal display but not actually terminal compliant. I will check how other loggers deal with jupyter display quirks.
