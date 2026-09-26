# [Issue #1297] AssertionError: len(continuation_enc) > 0

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/1297
state: open | updated: 2026-08-27T09:01:57Z
labels: bug

## 正文

Hi! thanks for the great work with the harness. I'm running into an issue evaluating models using the [persimmon](https://huggingface.co/adept/persimmon-8b-base) architecture using the harness. I also tried training a smaller model from random init, and the same thing happens with evaluating that. I believe this might be because of the sparse activations/ relu2 it uses?

Below is the error I get, you should be able to replicate using [this colab notebook](https://colab.research.google.com/drive/1Ur5eXXj3OkwQdsXuavJVGTxF4qPiyPNH?usp=sharing) which uses a slightly slimmed down version https://huggingface.co/pszemraj/perSLIMmon-8b-base that is sharded for easier colab loading 

```
2024-01-16:18:32:23,307 INFO     [utils.py:160] NumExpr defaulting to 2 threads.
2024-01-16:18:32:23,616 INFO     [config.py:58] PyTorch version 2.1.0+cu121 available.
2024-01-16:18:32:23,618 INFO     [config.py:108] JAX version 0.4.23 available.
2024-01-16:18:32:25,882 INFO     [__main__.py:156] Verbosity set to INFO
2024-01-16:18:32:30,344 WARNING  [__init__.py:194] Some tasks could not be loaded due to missing dependencies. Run with `--verbosity DEBUG` for full details.
/usr/local/lib/python3.10/dist-packages/datasets/load.py:1429: FutureWarning: The repository for hails/mmlu_no_train contains custom code which must be executed to correctly load the dataset. You can inspect the repository content at https://hf.co/datasets/hails/mmlu_no_train
You can avoid this message in future by passing the argument `trust_remote_code=True`.
Passing `trust_remote_code=True` will be mandatory to load this dataset from the next major release of `datasets`.
  warnings.warn(
2024-01-16:18:33:00,798 WARNING  [__init__.py:194] Some tasks could not be loaded due to missing dependencies. Run with `--verbosity DEBUG` for full details.
2024-01-16:18:33:00,799 INFO     [__main__.py:229] Selected Tasks: ['hellaswag', 'lambada_openai']
2024-01-16:18:33:00,841 INFO     [huggingface.py:148] Using device 'cuda:0'
Loading checkpoint shards: 100% 6/6 [01:13<00:00, 12.27s/it]
2024-01-16:18:34:17,496 WARNING  [big_modeling.py:425] You shouldn't move a model when it is dispatched on multiple devices.
/usr/local/lib/python3.10/dist-packages/datasets/load.py:1429: FutureWarning: The repository for hellaswag contains custom code which must be executed to correctly load the dataset. You can inspect the repository content at https://hf.co/datasets/hellaswag
You can avoid this message in future by passing the argument `trust_remote_code=True`.
Passing `trust_remote_code=True` will be mandatory to load this dataset from the next major release of `datasets`.
  warnings.warn(
2024-01-16:18:34:28,029 WARNING  [task.py:284] has_training_docs and has_validation_docs are False, using test_docs as fewshot_docs but this is not recommended.
2024-01-16:18:34:28,029 WARNING  [task.py:284] has_training_docs and has_validation_docs are False, using test_docs as fewshot_docs but this is not recommended.
2024-01-16:18:34:28,132 INFO     [task.py:337] Building contexts for task on rank 0...
2024-01-16:18:34:35,635 INFO     [task.py:337] Building contexts for task on rank 0...
2024-01-16:18:34:46,635 INFO     [evaluator.py:314] Running loglikelihood requests
  1% 393/45321 [05:48<10:26:47,  1.19it/s]Traceback (most recent call last):
  File "/usr/local/bin/lm_eval", line 8, in <module>
    sys.exit(cli_evaluate())
  File "/content/lm-evaluation-harness/lm_eval/__main__.py", line 231, in cli_evaluate
    results = evaluator.simple_evaluate(
  File "/content/lm-evaluation-harness/lm_eval/utils.py", line 415, in _wrapper
    return fn(*args, **kwargs)
  File "/content/lm-evaluation-harness/lm_eval/evaluator.py", line 150, in simple_evaluate
    results = evaluate(
  File "/content/lm-evaluation-harness/lm_eval/utils.py", line 415, in _wrapper
    return fn(*args, **kwargs)
  File "/content/lm-evaluation-harness/lm_eval/evaluator.py", line 325, in evaluate
    resps = getattr(lm, reqtype)(cloned_reqs)
  File "/content/lm-evaluation-harness/lm_eval/models/huggingface.py", line 774, in loglikelihood
    return self._loglikelihood_tokens(new_reqs)
  File "/content/lm-evaluation-harness/lm_eval/models/huggingface.py", line 909, in _loglikelihood_tokens
    assert len(continuation_enc) > 0
AssertionError
  1% 396/45321 [05:48<10:59:27,  1.14it/s]
```

let me know if any more info is required or what would need to be done to get this integrated!

## 评论 (9)

### haileyschoelkopf · 2024-01-16

Hi, thanks for opening this issue!

This is not related to relu^2 or the sparse activations, but rather seems to be something to do with tokenization (it looks like something is going wrong and actually, because there's an anomalously large token that might encompass both part of the context and the whole target/continuation, there are no tokens allocated to be the target.)

Would you be willing to print, when this error gets thrown, the following: `context_enc, len(context_enc), continuation_enc, len(continuation_enc), self.tok_decode(context_enc), self.tok_decode(continuation_enc)` ? You can quickly get back to it if you first run with `--use_cache ./cachedb` to save the preceding results.



### pszemraj · 2024-01-16

Interesting! Thanks for clarifying that. So yeah I just forked it and added some print statements, and loaded the cachedb like you said. Here's what I get:

[cachedb_rank0.zip](https://github.com/EleutherAI/lm-evaluation-harness/files/13956387/cachedb_rank0.zip)

Does that help?


```
oading checkpoint shards: 100% 6/6 [01:37<00:00, 16.19s/it]
generation_config.json: 100% 124/124 [00:00<00:00, 477kB/s]
2024-01-16:22:33:59,769 WARNING  [big_modeling.py:425] You shouldn't move a model when it is dispatched on multiple devices.
tokenizer_config.json: 100% 789/789 [00:00<00:00, 3.07MB/s]
tokenizer.json: 100% 12.9M/12.9M [00:00<00:00, 45.0MB/s]
special_tokens_map.json: 100% 497/497 [00:00<00:00, 1.87MB/s]
Using cache at ./cachedb_rank0.db
/usr/local/lib/python3.10/dist-packages/datasets/load.py:1429: FutureWarning: The repository for hellaswag contains custom code which must be executed to correctly load the dataset. You can inspect the repository content at https://hf.co/datasets/hellaswag
You can avoid this message in future by passing the argument `trust_remote_code=True`.
Passing `trust_remote_code=True` will be mandatory to load this dataset from the next major release of `datasets`.
  warnings.warn(
Downloading builder script: 100% 4.36k/4.36k [00:00<00:00, 16.0MB/s]
Downloading metadata: 100% 2.53k/2.53k [00:00<00:00, 12.5MB/s]
Downloading readme: 100% 6.84k/6.84k [00:00<00:00, 21.9MB/s]
Downloading data: 47.5MB [00:00, 60.1MB/s]
Downloading data: 11.8MB [00:00, 44.4MB/s]
Downloading data: 12.2MB [00:00, 44.4MB/s]
Generating train split: 100% 39905/39905 [00:06<00:00, 6384.28 examples/s]
Generating test split: 100% 10003/10003 [00:02<00:00, 4620.00 examples/s]
Generating validation split: 100% 10042/10042 [00:01<00:00, 7387.91 examples/s]
Map: 100% 39905/39905 [00:07<00:00, 5254.35 examples/s]
Map: 100% 10042/10042 [00:02<00:00, 4970.72 examples/s]
Downloading data: 100% 1.16M/1.16M [00:00<00:00, 2.82MB/s]
Generating test split: 100% 5153/5153 [00:00<00:00, 351532.11 examples/s]
2024-01-16:22:34:34,945 WARNING  [task.py:284] has_training_docs and has_validation_docs are False, using test_docs as fewshot_docs but this is not recommended.
2024-01-16:22:34:34,945 WARNING  [task.py:284] has_training_docs and has_validation_docs are False, using test_docs as fewshot_docs but this is not recommended.
2024-01-16:22:34:35,044 INFO     [task.py:337] Building contexts for task on rank 0...
2024-01-16:22:34:43,565 INFO     [task.py:337] Building contexts for task on rank 0...
2024-01-16:22:34:56,484 INFO     [evaluator.py:314] Running loglikelihood requests
2024-01-16:22:34:56,502 INFO     [model.py:203] Loading 'loglikelihood' responses from cache './cachedb_rank0.db' where possible...
100% 45321/45321 [00:10<00:00, 4439.42it/s]
  0% 0/44925 [00:00<?, ?it/s]Context Encoded: [65067, 118745, 1469, 1385, 10234, 10159, 38355, 5797, 1375, 12874, 1374, 1312, 1306, 9419, 1392, 62, 1375, 5, 1374, 2365, 1386, 1428, 38355, 5797, 1496, 19565, 1429, 1374, 18, 5391, 1375, 12874, 1420, 38355, 5797, 1721, 19565, 4301, 1374, 2189, 1375, 1410, 38355, 5797, 2168, 8019, 156105, 16715, 5528, 19565, 1375]
Length of Context Encoded: 51
Continuation Encoded: [1003, 1437, 21468, 1413, 1374, 4, 9419, 1392, 118, 1374, 2365, 1386, 1428, 38355, 5797, 1388, 19565, 1429, 6860, 1374, 18, 5391, 1375, 55762, 3646, 1377, 10060, 5310, 1374, 2189, 1445, 25335, 32129, 12598, 1653, 1374, 1312, 1308, 9163, 38355, 5797, 1450, 28512, 1413, 1374, 4, 9419, 1392, 118, 1374, 2365, 1386, 1428, 38355, 5797, 1375]
Length of Continuation Encoded: 56
Decoded Context: Food and Entertaining: How to flavor soy milk. Heat ¼ cup (59.2 ml) of soy milk in the microwave for 15 seconds. Heat the soy milk in a microwave safe container. The soy milk should be steaming when you take it out of the microwave.
Decoded Continuation:  Stir in 1 cup (115 ml) of soy milk and microwave for an additional 15 seconds. Use a heat-safe glass container or gallon jug filled about ¾ full of soy milk to stir in 1 cup (115 ml) of soy milk.
Context Encoded: [65067, 118745, 1469, 1385, 10234, 11757, 44667, 1374, 4432, 1453, 1375, 5883, 5592, 1376, 4659, 1374, 2008, 1489, 11408, 1376, 1374, 1740, 1374, 5, 1374, 1400, 50615, 38654, 1376, 10360, 1474, 1376, 1374, 4432, 1453, 7234, 1376, 1445, 17665, 1480, 1376, 1388, 1374, 34728, 12956, 1375, 1375, 29190, 9610, 1665, 3936, 3646, 15579, 1374, 4, 8068, 1376, 26465, 1450, 31630, 1420, 1374, 40673, 1375, 1375, 42573, 1602, 2867, 1374, 1422, 41544, 1376, 1450, 5448, 1445, 1374, 3193, 1403, 1376, 1388, 28512, 83952, 13398, 1375]
Length of Context Encoded: 84
Continuation Encoded: [1003, 1488, 101333, 1439, 24632, 1644, 12705, 15590, 3573, 1375, 1375, 12874, 27628, 3271, 48606, 11408, 1665, 3936, 2266, 1450, 3936, 3646, 1375]
Length of Continuation Encoded: 23
Decoded Context: Food and Entertaining: How to cook vegetarian chili. Take a large, heavy bottomed pot, add 2 tbsp olive oil, cumin, chili powder, oregano, and cayenne pepper.. Sauté over medium heat for about 1 minute, stirring to toast the spices.. Add the soya crumble, tofu or tvp, and stir well to coat.
Decoded Continuation:  There you go! Remove from the pan and let cool.. Heat vegetable oil in a large pot over medium low to medium heat.
Context Encoded: [65067, 118745, 1469, 1385, 10234, 19871, 33532, 25208, 3436, 6718, 1375, 1374, 8046, 1573, 3212, 1374, 3447, 1388, 1374, 1810, 38220, 1375, 1375, 1374, 3274, 65569, 1509, 2424, 1374, 1512, 1647, 8992, 7162, 1392, 3, 1374, 1376, 1374, 3, 1452, 1375, 1374, 3274, 1374, 3, 8124, 1509, 2424, 1374, 1447, 1647, 8992, 7162, 1392, 4, 1374, 1376, 1374, 3, 1452]
Length of Context Encoded: 60
Continuation Encoded: [1003, 1705, 33532, 25208, 4705, 70830, 49117, 50602, 1376, 59690, 1869, 2161, 15624, 1374, 1541, 6907, 5867, 4521, 104523, 1375, 1375, 1374, 2261, 33532, 25208, 4705, 1413, 1374, 363, 1374, 1312, 1294, 1374, 1422, 1378, 183, 1374, 1312, 1294, 1374, 1416, 1392, 1401, 1374, 1490, 423, 1452]
Length of Continuation Encoded: 47
Decoded Context: Food and Entertaining: How to derive the cosine difference formula. Draw your unit circle and label as needed.. Label the origin as point z with the ordered pair (0 , 0).. Label 0 degrees as point y with the ordered pair (1 , 0).
Decoded Continuation:  Name the cosine equation scientifically integrated into the formula, and use the other cells along with the line to determine how much distance is divided.. Color the cosine equation in 360 ° c/180 ° f (= k420).
Context Encoded: [1374, 1384, 3064, 1687, 1634, 1381, 137428, 1388, 6844, 23824, 1376, 1470, 1381, 1380, 11916, 1381, 62513, 26865, 11503, 3446, 69467, 3949, 1665, 163605, 80451, 1381, 107787, 36637, 89146, 1733, 54470, 1376, 2539, 1381, 124155, 31516, 1375, 1384, 1128, 1128, 1384, 1473, 7964, 11916, 4232, 56978, 1381, 1380, 3261, 12018, 46231, 7739, 1503, 16908, 25179, 4212, 1376, 1388, 22367, 1708, 1687, 1634, 1381, 60867, 3671, 1503, 24907, 2823, 1375, 3279, 1656, 11830, 8722, 28880, 1667, 1687, 1634, 1381, 1380, 1376, 1448, 10408, 2601, 3006, 1375, 1384, 1128, 1128, 1384, 1430, 27719, 4358, 1376, 1384, 24907, 2438, 15637, 1376, 13762, 60787, 17679, 84590, 1688, 1374, 122398, 1420]
Length of Context Encoded: 106
Continuation Encoded: []
Length of Continuation Encoded: 0
Decoded Context: "As Noel's uncle and godfather, it's Stephen's prerogative to have his country house overrun with parents who'll stay for a week and expect to be entertained, children's party or no."

"I suggested Stephen give your mother's sixtieth birthday ball at Montclair instead, and let us have Noel's birthday party at Claymore. Since her birthday is only three days after Noel's, that seemed the best plan."

"Clever girl," Clayton replied, instantly reversing his opinion of who ought to have the
Decoded Continuation: 
Traceback (most recent call last):
  File "/usr/local/bin/lm_eval", line 8, in <module>
    sys.exit(cli_evaluate())
  File "/content/lm-evaluation-harness/lm_eval/__main__.py", line 231, in cli_evaluate
    results = evaluator.simple_evaluate(
  File "/content/lm-evaluation-harness/lm_eval/utils.py", line 415, in _wrapper
    return fn(*args, **kwargs)
  File "/content/lm-evaluation-harness/lm_eval/evaluator.py", line 150, in simple_evaluate
    results = evaluate(
  File "/content/lm-evaluation-harness/lm_eval/utils.py", line 415, in _wrapper
    return fn(*args, **kwargs)
  File "/content/lm-evaluation-harness/lm_eval/evaluator.py", line 325, in evaluate
    resps = getattr(lm, reqtype)(cloned_reqs)
  File "/content/lm-evaluation-harness/lm_eval/api/model.py", line 229, in fn
    rem_res = getattr(self.lm, attr)(remaining_reqs)
  File "/content/lm-evaluation-harness/lm_eval/models/huggingface.py", line 773, in loglikelihood
    return self._loglikelihood_tokens(new_reqs)
  File "/content/lm-evaluation-harness/lm_eval/models/huggingface.py", line 916, in _loglikelihood_tokens
    assert len(continuation_enc) > 0
AssertionError
  0% 0/44925 [00:00<?, ?it/s]
```

I'm guessing that the below is the culprit but dont know much beyond that:

```
Continuation Encoded: []
Length of Continuation Encoded: 0
```


### haileyschoelkopf · 2024-01-19

Thank you for testing this, this is enough to replicate and debug! I'll follow up and look into it.

### haileyschoelkopf · 2024-01-19

@pszemraj for your purposes, a sufficient fix should be to add the following check here: 

https://github.com/EleutherAI/lm-evaluation-harness/blob/b93c3bcbf30109c40cd19ee862161702920b9c27/lm_eval/models/huggingface.py#L753

```
if len(whole_enc) == len(context_enc):
    cont_enc = self.tok_encode(continuation, add_special_tokens=add_special_tokens)
    return context_enc, cont_enc
```

but for a more generalized fix we can merge it'll be quite the headache (and gets back to why we have `_encode_pair()` in the first place...)


### Vectorrent · 2024-11-28

I've been running into the same issue, with a custom architecture and tokenizer (both of which use the HF API).
```
2024-11-28:08:00:20,436 INFO     [huggingface.py:129] Using device 'cuda:0'
2024-11-28:08:00:20,438 INFO     [huggingface.py:463] Overrode HF model backend type, and using type 'causal'
2024-11-28:08:00:20,441 INFO     [huggingface.py:365] Model parallel was set to False, max memory was not set, and device map was set to {'': 'cuda:0'}
2024-11-28:08:00:27,678 INFO     [evaluator.py:164] Setting random seed to 0 | Setting numpy seed to 1234 | Setting torch manual seed to 1234 | Setting fewshot manual seed to 1234
2024-11-28:08:00:27,679 INFO     [evaluator.py:217] Using pre-initialized model
2024-11-28:08:00:29,382 WARN     [evaluator.py:270] Overwriting default num_fewshot of arc_easy from None to 0
2024-11-28:08:00:29,383 INFO     [task.py:415] Building contexts for arc_easy on rank 0...
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2376/2376 [00:02<00:00, 1082.38it/s]
2024-11-28:08:00:31,798 INFO     [evaluator.py:489] Running loglikelihood requests
Running loglikelihood requests:   0%|                                                                                                                                        | 0/9501 [00:00<?, ?it/s]
Running loglikelihood requests:   0%|                                                                                                                              | 1/9501 [00:00<1:26:17,  1.83it/s]
Running loglikelihood requests:   0%|                                                                                                                                | 6/9501 [00:00<13:35, 11.64it/s]
Traceback (most recent call last):
  File "/home/crow/repos/praxis/eval.py", line 34, in <module>
    results = lm_eval.simple_evaluate(
              ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/crow/repos/praxis/.venv/lib/python3.12/site-packages/lm_eval/utils.py", line 397, in _wrapper
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "/home/crow/repos/praxis/.venv/lib/python3.12/site-packages/lm_eval/evaluator.py", line 301, in simple_evaluate
    results = evaluate(
              ^^^^^^^^^
  File "/home/crow/repos/praxis/.venv/lib/python3.12/site-packages/lm_eval/utils.py", line 397, in _wrapper
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "/home/crow/repos/praxis/.venv/lib/python3.12/site-packages/lm_eval/evaluator.py", line 500, in evaluate
    resps = getattr(lm, reqtype)(cloned_reqs)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/crow/repos/praxis/.venv/lib/python3.12/site-packages/lm_eval/api/model.py", line 378, in loglikelihood
    return self._loglikelihood_tokens(new_reqs, disable_tqdm=disable_tqdm)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/crow/repos/praxis/.venv/lib/python3.12/site-packages/lm_eval/models/huggingface.py", line 1040, in _loglikelihood_tokens
    assert len(continuation_enc) > 0
           ^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
Running loglikelihood requests:   0%|                                                                                                                                | 8/9501 [00:00<18:20,  8.63it/s]
```
It looks like `_encode_pair()` was moved to [api/model.py](https://github.com/EleutherAI/lm-evaluation-harness/blob/5680a2e6b5cf1a1621d8ff68d3d0e83e8b2731d3/lm_eval/api/model.py#L340), but sadly - even if I apply the patch - it does not appear to fix the problem.

### chschroeder · 2024-12-05

Same situation as @Vectorrent here. Would be interested in a solution that works for the current main branch.

### LuCeHe · 2024-12-27

Me too!


### eco-bone · 2025-07-18

@Vectorrent the temporary patch does work with this:

`cont_enc = self.tok_encode(continuation, add_special_tokens=False)`

instead of this:

`cont_enc = self.tok_encode(continuation, add_special_tokens=add_special_tokens)`

### nata2627 · 2026-08-27

I'd like to pick up the crash half of this — the `assert len(continuation_enc) > 0` that also shows up in #1053 and, more recently, #3336.

`_encode_pair` has moved to `lm_eval/api/model.py` since this was filed, but the split is unchanged: for the causal backend it is `whole_enc[len(context_enc):]`, which comes out empty whenever a single token spans the context/continuation boundary — the `": C"` case @haileyschoelkopf identified in #1053.

My plan is to do exactly what was suggested above and nothing more: when that split leaves the continuation with no tokens, fall back to encoding the continuation on its own (`add_special_tokens=False`), which is already what the `seq2seq` branch of the same function does. Where the split is valid the tokens stay byte-for-byte what they are today, so no existing benchmark number moves.

Deliberately out of scope: the *partial* merge, where the straddling token leaves the continuation with some tokens but not its own. That one is ambiguous — the straddling token's probability mass genuinely belongs partly to each side — and it looks like a call about published numbers rather than a bug.

@haileyschoelkopf — #1322 is still open as a draft and covers more than this (SPIECE_UNDERLINE / token 29871). Happy to drop this if you'd rather finish that instead.

