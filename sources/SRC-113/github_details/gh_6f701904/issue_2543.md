# [Issue #2543] Where's Whisper's calibration dataset?

source: https://github.com/mlcommons/inference/issues/2543
state: open | updated: 2026-04-14T16:28:38Z
labels: 

## 正文

Hi,

https://docs.mlcommons.org/inference/benchmarks/speech_to_text/get-whisper-data/ mentions that this will download the "validation and calibration datasets and do the necessary preprocessing", but it's not obvious to me which part of this is meant to be used for calibration.
My data directory contains:
```
LibriSpeech  dev-all  dev-all-repack  dev-all-repack.json  dev-all.json  whisper-dataset.md5
```

Any pointers are very appreciated!

## 评论 (9)

### cfRod · 2026-02-18

@pgmpablo157321 

### fadara01 · 2026-02-20

bump

### hanyunfan · 2026-02-25

We are provided both preprocessed and unprocessed dataset, if you downloaded the preprocessed one, you don’t need to preprocess it again. Detail information can be found here: https://github.com/mlcommons/inference/tree/master/speech2text#get-dataset



### fadara01 · 2026-02-26

Hi @hanyunfan 
Thanks for your comment,
I appreciate the fact that preprocessed and unprocessed datasets are provided and I know how to download them.

This link, https://docs.mlcommons.org/inference/benchmarks/speech_to_text/get-whisper-data/ mentions that it will download the "validation and calibration datasets and do the necessary preprocessing", but it's not obvious to me which part of this is meant to be used for calibration vs validation.
I'm looking for a calibration dataset to use when quantizing the model, the documentation indicates that a calibration dataset is included, but I don't see it.


### hanyunfan · 2026-03-03

@keithachorn-intel Could you help to take a look?

### keithachorn-intel · 2026-03-10

Hi @fadara01 - During the original task force, we found the model accuracy to be high, even after quantization.  Combined with the 99% criteria (of reference), no one noted difficulties in meeting the accuracy threshold post-quantization and we did not select a 'calibration' dataset.

Are you experiencing trouble meeting the accuracy criteria (99% of ~97.9%)?  If not, we would recommend that the wording in that reference be changed to reflect that no calibration dataset exists.  If there is a need however, it is possible for one to be selected.

### hanyunfan · 2026-03-23

Thanks Keith. @fadara01 Does that answered your question, if yes feel free to close this issue.

### cfRod · 2026-04-01

@keithachorn-intel as per the mlperf WG discussion - a calibration dataset can be provided. 

### cfRod · 2026-04-14

Hi @keithachorn-intel is there an update on this?
