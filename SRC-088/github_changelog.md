# Changelog (aggregated from releases.body)

> releases: 19

## v0.0.1 (2021-09-02)

(empty body)

## v0.2.0 (2022-03-07)

Major changes since 0.1.0:

- added blimp (#237)
- added qasper (#264)
- added asdiv (#244)
- added truthfulqa (#219)
- added gsm (#260)
- implemented description dict and deprecated provide_description (#226)
- new `--check_integrity` flag to run integrity unit tests at eval time (#290)
- positional arguments to `evaluate` and `simple_evaluate` are now deprecated
- `_CITATION` attribute on task modules (#292)
- lots of bug fixes and task fixes (always remember to report task versions for comparability!)

## v0.3.0 (2022-12-08)

## HuggingFace Datasets Integration
This release integrates HuggingFace `datasets` as the core dataset management interface, removing previous custom downloaders.

## What's Changed
* Refactor `Task` downloading to use `HuggingFace.datasets` by @jon-tow in https://github.com/EleutherAI/lm-evaluation-harness/pull/300
* Add templates and update docs by @jon-tow in https://github.com/EleutherAI/lm-evaluation-harness/pull/308
* Add dataset features to `TriviaQA` by @jon-tow in https://github.com/EleutherAI/lm-evaluation-harness/pull/305
* Add `SWAG` by @jon-tow in https://github.com/EleutherAI/lm-evaluation-harness/pull/306
* Fixes for using lm_eval as a library by @dirkgr in https://github.com/EleutherAI/lm-evaluation-harness/pull/309
* Researcher2 by @researcher2 in https://github.com/EleutherAI/lm-evaluation-harness/pull/261
* Suggested updates for the task guide by @StephenHogg in https://github.com/EleutherAI/lm-evaluation-harness/pull/301
* Add pre-commit by @Mistobaan in https://github.com/EleutherAI/lm-evaluation-harness/pull/317
* Decontam import fix by @jon-tow in https://github.com/EleutherAI/lm-evaluation-harness/pull/321
* Add bootstrap_iters kwarg by @Muennighoff in https://github.com/EleutherAI/lm-evaluation-harness/pull/322
* Update decontamination.md by @researcher2 in https://github.com/EleutherAI/lm-evaluation-harness/pull/331
* Fix key access in squad evaluation metrics by @konstantinschulz in https://github.com/EleutherAI/lm-evaluation-harness/pull/333
* Fix make_disjoint_window for tail case by @richhankins in https://github.com/EleutherAI/lm-evaluation-harness/pull/336
* Manually concat tokenizer revision with subfolder by @jon-tow in https://github.com/EleutherAI/lm-evaluation-harness/pull/343
* [deps] Use minimum versioning for `numexpr` by @jon-tow in https://github.com/EleutherAI/lm-evaluation-harness/pull/352
* Remove custom datasets that are in HF by @jon-tow in https://github.com/EleutherAI/lm-evaluation-harness/pull/330
* Add `TextSynth` API by @jon-tow in https://github.com/EleutherAI/lm-evaluation-harness/pull/299
* Add the original `LAMBADA` dataset by @jon-tow in https://github.com/EleutherAI/lm-evaluation-harness/pull/357

## New Contributors
* @dirkgr made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/309
* @Mistobaan made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/317
* @konstantinschulz made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/333
* @richhankins made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/336

**Full Changelog**: https://github.com/EleutherAI/lm-evaluation-harness/compare/v0.2.0...v0.3.0

## v0.4.0 (2023-12-04)

## What's Changed
* Replace stale `triviaqa` dataset link by @jon-tow in https://github.com/EleutherAI/lm-evaluation-harness/pull/364
* Update `actions/setup-python`in  CI workflows by @jon-tow in https://github.com/EleutherAI/lm-evaluation-harness/pull/365
* Bump `triviaqa` version by @jon-tow in https://github.com/EleutherAI/lm-evaluation-harness/pull/366
* Update `lambada_openai` multilingual data source by @jon-tow in https://github.com/EleutherAI/lm-evaluation-harness/pull/370
* Update Pile Test/Val Download URLs by @fattorib in https://github.com/EleutherAI/lm-evaluation-harness/pull/373
* Added ToxiGen task by @Thartvigsen in https://github.com/EleutherAI/lm-evaluation-harness/pull/377
* Added CrowSPairs by @aflah02 in https://github.com/EleutherAI/lm-evaluation-harness/pull/379
* Add accuracy metric to crows-pairs by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/380
* hotfix(gpt2): Remove vocab-size logits slice by @jon-tow in https://github.com/EleutherAI/lm-evaluation-harness/pull/384
* Enable "low_cpu_mem_usage" to reduce the memory usage of HF models by @sxjscience in https://github.com/EleutherAI/lm-evaluation-harness/pull/390
* Upstream `hf-causal` and `hf-seq2seq` model implementations by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/381
* Hosting arithmetic dataset on HuggingFace by @fattorib in https://github.com/EleutherAI/lm-evaluation-harness/pull/391
* Hosting wikitext on HuggingFace  by @fattorib in https://github.com/EleutherAI/lm-evaluation-harness/pull/396
* Change device parameter to cuda:0 to avoid runtime error by @Jeffwan in https://github.com/EleutherAI/lm-evaluation-harness/pull/403
* Update README installation instructions by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/407
* feat: evaluation using peft models with CLM by @zanussbaum in https://github.com/EleutherAI/lm-evaluation-harness/pull/414
* Update setup.py dependencies by @ret2libc in https://github.com/EleutherAI/lm-evaluation-harness/pull/416
* fix: add seq2seq peft by @zanussbaum in https://github.com/EleutherAI/lm-evaluation-harness/pull/418
* Add support for load_in_8bit and trust_remote_code model params by @philwee in https://github.com/EleutherAI/lm-evaluation-harness/pull/422
* Hotfix: patch issues with the `huggingface.py` model classes by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/427
* Continuing work on refactor [WIP] by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/425
* Document task name wildcard support in README by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/435
* Add non-programmatic BIG-bench-hard tasks by @yurodiviy in https://github.com/EleutherAI/lm-evaluation-harness/pull/406
* Updated handling for device in lm_eval/models/gpt2.py by @nikhilpinnaparaju in https://github.com/EleutherAI/lm-evaluation-harness/pull/447
* [WIP, Refactor] Staging more changes by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/465
* [Refactor, WIP] Multiple Choice + loglikelihood_rolling support for YAML tasks by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/467
* Configurable-Tasks by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/438
* single GPU automatic batching logic by @fattorib in https://github.com/EleutherAI/lm-evaluation-harness/pull/394
* Fix bugs introduced in #394 #406 and max length bug by @juletx in https://github.com/EleutherAI/lm-evaluation-harness/pull/472
* Sort task names to keep the same order always by @juletx in https://github.com/EleutherAI/lm-evaluation-harness/pull/474
* Set PAD token to EOS token by @nikhilpinnaparaju in https://github.com/EleutherAI/lm-evaluation-harness/pull/448
* [Refactor] Add decorator for registering YAMLs as tasks by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/486
* fix adaptive batch crash when there are no new requests by @jquesnelle in https://github.com/EleutherAI/lm-evaluation-harness/pull/490
* Add multilingual datasets (XCOPA, XStoryCloze, XWinograd, PAWS-X, XNLI, MGSM) by @juletx in https://github.com/EleutherAI/lm-evaluation-harness/pull/426
* Create output path directory if necessary by @janEbert in https://github.com/EleutherAI/lm-evaluation-harness/pull/483
* Add results of various models in json and md format by @juletx in https://github.com/EleutherAI/lm-evaluation-harness/pull/477
* Update config by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/501
* P3 prompt task by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/493
* Evaluation Against Portion of Benchmark Data by @kenhktsui in https://github.com/EleutherAI/lm-evaluation-harness/pull/480
* Add option to dump prompts and completions to a JSON file by @juletx in https://github.com/EleutherAI/lm-evaluation-harness/pull/492
* Add perplexity task on arbitrary JSON data by @janEbert in https://github.com/EleutherAI/lm-evaluation-harness/pull/481
* Update config by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/520
* Data Parallelism by @fattorib in https://github.com/EleutherAI/lm-evaluation-harness/pull/488
* Fix mgpt fewshot by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/522
* Extend `dtype` command line flag to `HFLM` by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/523
* Add support for loading GPTQ models via AutoGPTQ by @gakada in https://github.com/EleutherAI/lm-evaluation-harness/pull/519
* Change type signature of `quantized` and its default value for python < 3.11 compatibility  by @passaglia in https://github.com/EleutherAI/lm-evaluation-harness/pull/532
* Fix LLaMA tokenization issue by @gakada in https://github.com/EleutherAI/lm-evaluation-harness/pull/531
* [Refactor] Make promptsource an extra / not required for installation by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/542
* Move spaces from context to continuation by @gakada in https://github.com/EleutherAI/lm-evaluation-harness/pull/546
* Use max_length in AutoSeq2SeqLM by @gakada in https://github.com/EleutherAI/lm-evaluation-harness/pull/551
* Fix typo by @kwikiel in https://github.com/EleutherAI/lm-evaluation-harness/pull/557
* Add load_in_4bit and fix peft loading by @gakada in https://github.com/EleutherAI/lm-evaluation-harness/pull/556
* Update task_guide.md by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/564
* [Refactor] Non-greedy generation ; WIP GSM8k yaml by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/559
* Dataset metric log [WIP] by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/560
* Add Anthropic support by @zphang in https://github.com/EleutherAI/lm-evaluation-harness/pull/562
* Add MultipleChoiceExactTask by @gakada in https://github.com/EleutherAI/lm-evaluation-harness/pull/537
* Revert "Add MultipleChoiceExactTask" by @StellaAthena in https://github.com/EleutherAI/lm-evaluation-harness/pull/568
* [Refactor] [WIP] New YAML advanced docs by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/567
* Remove the registration of "GPT2" as a model type by @StellaAthena in https://github.com/EleutherAI/lm-evaluation-harness/pull/574
* [Refactor] Docs update by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/577
* Better docs by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/576
* Update evaluator.py cache_db argument str if model is not str by @poedator in https://github.com/EleutherAI/lm-evaluation-harness/pull/575
* Add --max_batch_size and --batch_size auto:N by @gakada in https://github.com/EleutherAI/lm-evaluation-harness/pull/572
* [Refactor] ALL_TASKS now maintained (not static) by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/581
* Fix seqlen issues for bloom, remove extraneous OPT tokenizer check by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/582
* Fix non-callable attributes in CachingLM by @gakada in https://github.com/EleutherAI/lm-evaluation-harness/pull/584
* Add error handling for calling `.to(device)` by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/585
* fixes some minor issues on tasks.  by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/580
* Add - 4bit-related args by @SONG-WONHO in https://github.com/EleutherAI/lm-evaluation-harness/pull/579
* Fix triviaqa task by @seopbo in https://github.com/EleutherAI/lm-evaluation-harness/pull/525
* [Refactor] Addressing Feedback on new docs pages by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/578
* Logging Samples by @farzanehnakhaee70 in https://github.com/EleutherAI/lm-evaluation-harness/pull/563
* Merge master into big-refactor by @gakada in https://github.com/EleutherAI/lm-evaluation-harness/pull/590
* [Refactor] Package YAMLs alongside pip installations of lm-eval by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/596
* fixes for multiple_choice by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/598
* add openbookqa config by @farzanehnakhaee70 in https://github.com/EleutherAI/lm-evaluation-harness/pull/600
* [Refactor] Model guide docs by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/606
* [Refactor] More MCQA fixes by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/599
* [Refactor] Hellaswag by @nopperl in https://github.com/EleutherAI/lm-evaluation-harness/pull/608
* [Refactor] Seq2Seq Models with Multi-Device Support by @fattorib in https://github.com/EleutherAI/lm-evaluation-harness/pull/565
* [Refactor] CachingLM support via `--use_cache` by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/619
* [Refactor] batch generation better for `hf` model ; deprecate `hf-causal` in new release by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/613
* [Refactor] Update task statuses on tracking list by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/629
* [Refactor] `device_map` options for `hf` model type by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/625
* [Refactor] Misc. cleanup of dead code by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/609
* [Refactor] Log request arguments to per-sample json by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/624
* [Refactor] HellaSwag YAML fix by @nopperl in https://github.com/EleutherAI/lm-evaluation-harness/pull/639
* [Refactor] Add caveats to `parallelize=True` docs by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/638
* fixed super_glue and removed unused yaml config by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/645
* [Refactor] Fix sample logging by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/646
* Add PEFT, quantization, remote code, LLaMA fix by @gakada in https://github.com/EleutherAI/lm-evaluation-harness/pull/644
* [Refactor] Handle `cuda:0` device assignment by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/647
* [refactor] Add prost config by @farzanehnakhaee70 in https://github.com/EleutherAI/lm-evaluation-harness/pull/640
* [Refactor] Misc. bugfixes ; edgecase quantized models by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/648
* Update __init__.py by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/650
* [Refactor] Add Lambada Multilingual by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/658
* [Refactor] Add: SWAG,RACE,Arithmetic,Winogrande,PubmedQA by @fattorib in https://github.com/EleutherAI/lm-evaluation-harness/pull/627
* [refactor] Add qa4mre config by @farzanehnakhaee70 in https://github.com/EleutherAI/lm-evaluation-harness/pull/651
* Update `generation_kwargs` by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/657
* [Refactor] Move race dataset on HF to EleutherAI group by @fattorib in https://github.com/EleutherAI/lm-evaluation-harness/pull/661
* [Refactor] Add Headqa by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/659
* [Refactor] Add Unscramble ; Toxigen ; Hendrycks_Ethics ; MathQA by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/660
* [Refactor] Port TruthfulQA (mc1 only) by @nopperl in https://github.com/EleutherAI/lm-evaluation-harness/pull/666
* [Refactor] Miscellaneous fixes by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/676
* [Refactor] Patch to revamp-process by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/678
* Revamp process by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/671
* [Refactor] Fix padding ranks by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/679
* [Refactor] minor edits by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/680
* [Refactor] Migrate ANLI tasks to yaml by @yeoedward in https://github.com/EleutherAI/lm-evaluation-harness/pull/682
* edited output_path and added help to args by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/684
* [Refactor] Minor changes by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/685
* [Refactor] typo by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/687
* [Test] fix test_evaluator.py by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/675
* Fix dummy model not invoking super class constructor  by @yeoedward in https://github.com/EleutherAI/lm-evaluation-harness/pull/688
* [Refactor] Migrate webqs task to yaml by @yeoedward in https://github.com/EleutherAI/lm-evaluation-harness/pull/689
* [Refactor] Fix tests by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/693
* [Refactor] Migrate xwinograd tasks to yaml by @yeoedward in https://github.com/EleutherAI/lm-evaluation-harness/pull/695
* Early stop bug of greedy_until (primary_until should be a list of str) by @ZZR0 in https://github.com/EleutherAI/lm-evaluation-harness/pull/700
* Remove condition to check for `winograd_schema` by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/690
* [Refactor] Use console script by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/703
* [Refactor] Fixes for when using `num_fewshot` by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/702
* [Refactor] Updated anthropic to new API by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/710
* [Refactor] Cleanup for `big-refactor` by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/686
* Update README.md by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/720
* [Refactor] Benchmark scripts by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/612
* [Refactor] Fix Max Length arg by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/723
* Add note about MPS by @StellaAthena in https://github.com/EleutherAI/lm-evaluation-harness/pull/728
* Update huggingface.py by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/730
* Update README.md by @StellaAthena in https://github.com/EleutherAI/lm-evaluation-harness/pull/732
* [Refactor] Port over Autobatching by @fattorib in https://github.com/EleutherAI/lm-evaluation-harness/pull/673
* [Refactor] Fix Anthropic Import and other fixes by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/724
* [Refactor] Remove Unused Variable in Make-Table by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/734
* [Refactor] logiqav2 by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/711
* [Refactor] Fix task packaging by @yeoedward in https://github.com/EleutherAI/lm-evaluation-harness/pull/739
* [Refactor] fixed openai by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/736
* [Refactor] added some typehints by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/742
* [Refactor] Port Babi task by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/752
* [Refactor] CrowS-Pairs by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/751
* Update README.md by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/745
* [Refactor] add xcopa by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/749
* Update README.md by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/764
* [Refactor] Add Blimp by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/763
* [Refactor] Use evaluation mode for accelerate to prevent OOM by @tju01 in https://github.com/EleutherAI/lm-evaluation-harness/pull/770
* Patch Blimp by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/768
* [Refactor] Speedup hellaswag context building by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/774
* [Refactor] Patch crowspairs higher_is_better by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/766
* [Refactor] XNLI by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/776
* [Refactor] Update Benchmark by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/777
* [WIP] Update API docs in README by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/747
* [Refactor] Real Toxicity Prompts by @aflah02 in https://github.com/EleutherAI/lm-evaluation-harness/pull/725
* [Refactor] XStoryCloze by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/759
* [Refactor] Glue by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/761
* [Refactor] Add triviaqa by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/758
* [Refactor] Paws-X by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/779
* [Refactor] MC Taco by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/783
* [Refactor] Truthfulqa by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/782
* [Refactor] fix doc_to_target processing by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/786
* [Refactor] Add README.md by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/757
* [Refactor] Don't always require Perspective API key to run  by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/788
* [Refactor] Added HF model test by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/791
* [Big refactor] HF test fixup by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/793
* [Refactor] Process Whitespace for greedy_until by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/781
* [Refactor] Fix metrics in Greedy Until by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/780
* Update README.md by @Wehzie in https://github.com/EleutherAI/lm-evaluation-harness/pull/803
* Merge Fix metrics branch by @uSaiPrashanth in https://github.com/EleutherAI/lm-evaluation-harness/pull/802
* [Refactor] Update docs by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/744
* [Refactor] Superglue T5 Parity by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/769
* Update main.py by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/817
* [Refactor] Coqa by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/820
* [Refactor] drop by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/821
* [Refactor] Asdiv by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/813
* [Refactor] Fix IndexError by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/819
* [Refactor] toxicity: API inside function by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/822
* [Refactor] wsc273 by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/807
* [Refactor] Bump min accelerate version and update documentation by @fattorib in https://github.com/EleutherAI/lm-evaluation-harness/pull/812
* Add mypy baseline config by @ethanhs in https://github.com/EleutherAI/lm-evaluation-harness/pull/809
* [Refactor] Fix wikitext task by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/833
* [Refactor] Add WMT tasks by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/775
* [Refactor] consolidated tasks tests by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/831
* Update README.md by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/838
* [Refactor] mgsm by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/784
* [Refactor] Add top-level import by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/830
* Add pyproject.toml by @ethanhs in https://github.com/EleutherAI/lm-evaluation-harness/pull/810
* [Refactor] Additions to docs by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/799
* [Refactor] Fix MGSM by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/845
* [Refactor] float16 MPS works in torch nightly by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/853
* [Refactor] Update benchmark by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/850
* Switch to pyproject.toml based project metadata by @ethanhs in https://github.com/EleutherAI/lm-evaluation-harness/pull/854
* Use Dict to make the code python 3.8 compatible by @chrisociepa in https://github.com/EleutherAI/lm-evaluation-harness/pull/857
* [Refactor] NQopen by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/859
* [Refactor] NQ-open by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/798
* Fix "local variable 'docs' referenced before assignment" error in write_out.py by @chrisociepa in https://github.com/EleutherAI/lm-evaluation-harness/pull/856
* [Refactor] 3.8 test compatibility by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/863
* [Refactor] Cleanup dependencies by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/860
* [Refactor] Qasper, MuTual, MGSM (Native CoT) by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/840
* undefined type and output_type when using promptsource fixed by @Hojjat-Mokhtarabadi in https://github.com/EleutherAI/lm-evaluation-harness/pull/842
* [Refactor] Deactivate select GH Actions by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/871
* [Refactor] squadv2 by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/785
* [Refactor] Set python3.8 as allowed version by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/862
* Fix positional arguments in HF model generate by @chrisociepa in https://github.com/EleutherAI/lm-evaluation-harness/pull/877
* [Refactor] MATH by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/861
* Create cot_yaml by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/870
* [Refactor] Port CSATQA to refactor by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/865
* [Refactor] CMMLU, C-Eval port ; Add fewshot config by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/864
* [Refactor] README.md for Asdiv by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/878
* [Refactor] Hotfixes to big-refactor by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/880
* Change Python Version to 3.8 in .pre-commit-config.yaml and GitHub Actions by @chrisociepa in https://github.com/EleutherAI/lm-evaluation-harness/pull/895
* [Refactor] Fix PubMedQA by @tmabraham in https://github.com/EleutherAI/lm-evaluation-harness/pull/890
* [Refactor] Fix error when calling `lm-eval` by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/899
* [Refactor] bigbench by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/852
* [Refactor] Fix wildcards by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/900
* Add transformation filters by @chrisociepa in https://github.com/EleutherAI/lm-evaluation-harness/pull/883
* [Refactor] Flan benchmark by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/816
* [Refactor] WIP: Add MMLU by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/753
* Added notable contributors to the citation block by @StellaAthena in https://github.com/EleutherAI/lm-evaluation-harness/pull/907
* [Refactor] Improve error logging by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/908
* [Refactor] Add _batch_scheduler in greedy_until by @AndyWolfZwei in https://github.com/EleutherAI/lm-evaluation-harness/pull/912
* add belebele by @ManuelFay in https://github.com/EleutherAI/lm-evaluation-harness/pull/885
* Update README.md by @StellaAthena in https://github.com/EleutherAI/lm-evaluation-harness/pull/917
* [Refactor] Precommit formatting for Belebele by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/926
* [Refactor] change all mentions of `greedy_until` to `generate_until` by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/927
* [Refactor] Squadv2 updates by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/923
* [Refactor] Verbose by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/910
* [Refactor] Fix Unit Tests by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/905
* Fix `generate_until` rename by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/929
* [Refactor] Generate_until rename by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/931
* Fix 'tqdm' object is not subscriptable" error in huggingface.py when batch size is auto by @jasonkrone in https://github.com/EleutherAI/lm-evaluation-harness/pull/916
* [Refactor] Fix Default Metric Call by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/935
* Big refactor write out adaption by @MicPie in https://github.com/EleutherAI/lm-evaluation-harness/pull/937
* Update pyproject.toml by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/915
* [Refactor] Fix whitespace warning by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/949
* [Refactor] Update documentation by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/954
* [Refactor]fix two bugs when ran with qasper_bool and toxigen by @AndyWolfZwei in https://github.com/EleutherAI/lm-evaluation-harness/pull/934
* [Refactor] Describe local dataset usage in docs by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/956
* [Refactor] Update README, documentation by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/955
* [Refactor] Don't load MMLU auxiliary_train set by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/953
* [Refactor] Patch for Generation Until by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/957
* [Refactor] Model written eval by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/815
* [Refactor] Bugfix: AttributeError: 'Namespace' object has no attribute 'verbose' by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/966
* [Refactor] Mmlu subgroups and weight avg by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/922
* [Refactor] Remove deprecated `gold_alias` task YAML option by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/965
* [Refactor] Logging fixes by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/952
* [Refactor] fixes for alternative MMLU tasks. by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/981
* [Refactor] Alias fix by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/987
* [Refactor] Minor cleanup on base `Task` subclasses by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/996
* [Refactor] add squad from master by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/971
* [Refactor] Squad misc by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/999
* [Refactor] Fix CI tests by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/997
* [Refactor] will check if group_name is None by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1001
* [Refactor] Bugfixes by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1002
* [Refactor] Verbosity rework by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/958
* add description on task/group alias by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/979
* [Refactor] Upstream ggml from big-refactor branch by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/967
* [Refactor] Improve Handling of Stop-Sequences for HF Batched Generation by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1009
* [Refactor] Update README by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1020
* [Refactor] Remove `examples/` folder by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1018
* [Refactor] vllm support by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1011
* Allow Generation arguments on greedy_until reqs by @uSaiPrashanth in https://github.com/EleutherAI/lm-evaluation-harness/pull/897
* Social iqa by @StellaAthena in https://github.com/EleutherAI/lm-evaluation-harness/pull/1030
* [Refactor] BBH fixup by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1029
* Rename bigbench.yml to default.yml by @StellaAthena in https://github.com/EleutherAI/lm-evaluation-harness/pull/1032
* [Refactor] Num_fewshot process by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/985
* [Refactor] Use correct HF model type for MBart-like models by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1024
* [Refactor] Urgent fix by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1033
* [Refactor] Versioning by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1031
* fixes for sampler by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1038
* [Refactor] Update README.md by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1046
* [refactor] mps requirement by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1037
* [Refactor] Additions to example notebook by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1048
* Miscellaneous documentation updates by @StellaAthena in https://github.com/EleutherAI/lm-evaluation-harness/pull/1047
* [Refactor] add notebook for overview by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1025
* Update README.md by @StellaAthena in https://github.com/EleutherAI/lm-evaluation-harness/pull/1049
* [Refactor] Openai completions by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1008
* [Refactor] Added support for OpenAI ChatCompletions by @DaveOkpare in https://github.com/EleutherAI/lm-evaluation-harness/pull/839
* [Refactor] Update docs ToC by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1051
* [Refactor] Fix fewshot cot mmlu descriptions by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1060

## New Contributors
* @fattorib made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/373
* @Thartvigsen made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/377
* @aflah02 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/379
* @sxjscience made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/390
* @Jeffwan made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/403
* @zanussbaum made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/414
* @ret2libc made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/416
* @philwee made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/422
* @yurodiviy made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/406
* @nikhilpinnaparaju made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/447
* @lintangsutawika made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/438
* @juletx made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/472
* @janEbert made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/483
* @kenhktsui made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/480
* @passaglia made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/532
* @kwikiel made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/557
* @poedator made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/575
* @SONG-WONHO made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/579
* @seopbo made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/525
* @farzanehnakhaee70 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/563
* @nopperl made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/608
* @yeoedward made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/682
* @ZZR0 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/700
* @tju01 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/770
* @Wehzie made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/803
* @uSaiPrashanth made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/802
* @ethanhs made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/809
* @chrisociepa made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/857
* @Hojjat-Mokhtarabadi made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/842
* @AndyWolfZwei made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/912
* @ManuelFay made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/885
* @jasonkrone made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/916
* @MicPie made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/937
* @DaveOkpare made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/839

**Full Changelog**: https://github.com/EleutherAI/lm-evaluation-harness/compare/v0.3.0...v0.4.0

## v0.4.1 (2024-01-31)

## Release Notes

This PR release contains all changes so far since the release of v0.4.0 , and is partially a test of our release automation, provided by @anjor .

At a high level, some of the changes include: 

- Data-parallel inference using vLLM (contributed by @baberabb )
- A major fix to Huggingface model generation--previously, in v0.4.0, due to a bug with stop sequence handling, generations were sometimes cut off too early.
- Miscellaneous documentation updates
- A number of new tasks, and bugfixes to old tasks!
- The support for OpenAI-like API models using `local-completions` or `local-chat-completions` ( Thanks to @veekaybee @mgoin @anjor and others on this)!
- Integration with tools for visualization of results, such as with Zeno, and WandB coming soon!

More frequent (minor) version releases may be done in the future, to make it easier for PyPI users!

We're very pleased by the uptick in interest in LM Evaluation Harness recently, and we hope to continue to improve the library as time goes on. We're grateful to everyone who's contributed, and are excited by how many new contributors this version brings! If you have feedback for us, or would like to help out developing the library, please let us know.

In the next version release, we hope to include
- Chat Templating + System Prompt support, for locally-run models
- Improved Answer Extraction for many generative tasks, making them more easily run zero-shot and less dependent on model output formatting
- General speedups and QoL fixes to the non-inference portions of LM-Evaluation-Harness, including drastically reduced startup times / faster non-inference processing steps especially when num_fewshot is large!
- A new `TaskManager` object and the deprecation of `lm_eval.tasks.initialize_tasks()`, for achieving the easier registration of many tasks and configuration of new groups of tasks

## What's Changed
* Announce v0.4.0 in README by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1061
* remove commented planned samplers in `lm_eval/api/samplers.py` by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1062
* Confirming links in docs work (WIP) by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1065
* Set actual version to v0.4.0 by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1064
* Updating docs hyperlinks  by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1066
* Fiddling with READMEs, Reenable CI tests on `main` by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1063
* Update _cot_fewshot_template_yaml by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1074
* Patch scrolls by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1077
* Update template of qqp dataset by @shiweijiezero in https://github.com/EleutherAI/lm-evaluation-harness/pull/1097
* Change the sub-task name from sst to sst2 in glue by @shiweijiezero in https://github.com/EleutherAI/lm-evaluation-harness/pull/1099
* Add kmmlu evaluation to tasks by @h-albert-lee in https://github.com/EleutherAI/lm-evaluation-harness/pull/1089
* Fix stderr by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1106
* Simplified `evaluator.py` by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1104
* [Refactor] vllm data parallel by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1035
* Unpack group in `write_out` by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1113
* Revert "Simplified `evaluator.py`" by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1116
* `qqp`, `mnli_mismatch`: remove unlabled test sets by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1114
* fix: bug of BBH_cot_fewshot by @Momo-Tori in https://github.com/EleutherAI/lm-evaluation-harness/pull/1118
* Bump BBH version by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1120
* Refactor `hf` modeling code by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1096
* Additional process for doc_to_choice by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1093
* doc_to_decontamination_query can use function by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1082
* Fix vllm `batch_size` type by @xTayEx in https://github.com/EleutherAI/lm-evaluation-harness/pull/1128
* fix: passing max_length to vllm engine args by @NanoCode012 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1124
* Fix Loading Local Dataset by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1127
* place model onto `mps` by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1133
* Add benchmark FLD by @MorishT in https://github.com/EleutherAI/lm-evaluation-harness/pull/1122
* fix typo in README.md by @lennijusten in https://github.com/EleutherAI/lm-evaluation-harness/pull/1136
* add correct openai api key to README.md by @lennijusten in https://github.com/EleutherAI/lm-evaluation-harness/pull/1138
* Update Linter CI Job by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1130
* add utils.clear_torch_cache() to model_comparator by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1142
* Enabling OpenAI completions via gooseai by @veekaybee in https://github.com/EleutherAI/lm-evaluation-harness/pull/1141
* vllm clean up tqdm by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1144
* openai nits by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1139
* Add IFEval / Instruction-Following Eval by @wiskojo in https://github.com/EleutherAI/lm-evaluation-harness/pull/1087
* set `--gen_kwargs` arg to None  by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1145
* Add shorthand flags by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1149
* fld bugfix by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1150
* Remove GooseAI docs and change no-commit-to-branch precommit hook by @veekaybee in https://github.com/EleutherAI/lm-evaluation-harness/pull/1154
* Add docs on adding a multiple choice metric by @polm-stability in https://github.com/EleutherAI/lm-evaluation-harness/pull/1147
* Simplify evaluator by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1126
* Generalize Qwen tokenizer fix by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1146
* self.device in huggingface.py line 210 treated as torch.device but might be a string by @pminervini in https://github.com/EleutherAI/lm-evaluation-harness/pull/1172
* Fix Column Naming and Dataset Naming Conventions in K-MMLU Evaluation by @seungduk-yanolja in https://github.com/EleutherAI/lm-evaluation-harness/pull/1171
* feat: add option to upload results to Zeno by @Sparkier in https://github.com/EleutherAI/lm-evaluation-harness/pull/990
* Switch Linting to `ruff` by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1166
* Error in --num_fewshot option for K-MMLU Evaluation Harness by @guijinSON in https://github.com/EleutherAI/lm-evaluation-harness/pull/1178
* Implementing local OpenAI API-style chat completions on any given inference server by @veekaybee in https://github.com/EleutherAI/lm-evaluation-harness/pull/1174
* Update README.md by @anjor in https://github.com/EleutherAI/lm-evaluation-harness/pull/1184
* Update README.md by @anjor in https://github.com/EleutherAI/lm-evaluation-harness/pull/1183
* Add tokenizer backend by @anjor in https://github.com/EleutherAI/lm-evaluation-harness/pull/1186
* Correctly Print Task Versioning by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1173
* update Zeno example and reference in README by @Sparkier in https://github.com/EleutherAI/lm-evaluation-harness/pull/1190
* Remove tokenizer for openai chat completions by @anjor in https://github.com/EleutherAI/lm-evaluation-harness/pull/1191
* Update README.md by @anjor in https://github.com/EleutherAI/lm-evaluation-harness/pull/1181
* disable `mypy` by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1193
* Generic decorator for handling rate limit errors by @zachschillaci27 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1109
* Refer in README to main branch by @BramVanroy in https://github.com/EleutherAI/lm-evaluation-harness/pull/1200
* Hardcode 0-shot for fewshot Minerva Math tasks by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1189
* Upstream Mamba Support (`mamba_ssm`) by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1110
* Update cuda handling  by @anjor in https://github.com/EleutherAI/lm-evaluation-harness/pull/1180
* Fix documentation in API table by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1203
* Consolidate batching by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1197
* Add remove_whitespace to FLD benchmark by @MorishT in https://github.com/EleutherAI/lm-evaluation-harness/pull/1206
* Fix the argument order in `utils.divide` doc by @xTayEx in https://github.com/EleutherAI/lm-evaluation-harness/pull/1208
* [Fix #1211 ] pin vllm at < 0.2.6 by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1212
* fix unbounded local variable by @onnoo in https://github.com/EleutherAI/lm-evaluation-harness/pull/1218
* nits + fix siqa by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1216
* add length of strings and answer options to Zeno metadata by @Sparkier in https://github.com/EleutherAI/lm-evaluation-harness/pull/1222
* Don't silence errors when loading tasks by @polm-stability in https://github.com/EleutherAI/lm-evaluation-harness/pull/1148
* Update README.md by @anjor in https://github.com/EleutherAI/lm-evaluation-harness/pull/1195
* Update race's README.md by @pminervini in https://github.com/EleutherAI/lm-evaluation-harness/pull/1230
* batch_schedular bug in Collator by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1229
* Update openai_completions.py by @StellaAthena in https://github.com/EleutherAI/lm-evaluation-harness/pull/1238
* vllm: handle max_length better and substitute Collator by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1241
* Remove self.dataset_path post_init process by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1243
* Add multilingual HellaSwag task by @JorgeDeCorte in https://github.com/EleutherAI/lm-evaluation-harness/pull/1228
* Do not escape ascii in logging outputs by @passaglia in https://github.com/EleutherAI/lm-evaluation-harness/pull/1246
* fixed fewshot loading for multiple input tasks by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1255
* Revert citation by @StellaAthena in https://github.com/EleutherAI/lm-evaluation-harness/pull/1257
* Specify utf-8 encoding to properly save non-ascii samples to file by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1265
* Fix evaluation for the belebele dataset by @jmichaelov in https://github.com/EleutherAI/lm-evaluation-harness/pull/1267
* Call "exact_match" once for each multiple-target sample by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1266
* MultiMedQA by @tmabraham in https://github.com/EleutherAI/lm-evaluation-harness/pull/1198
* Fix bug in multi-token Stop Sequences by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1268
* Update Table Printing by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1271
* add Kobest by @jp1924 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1263
* Apply `process_docs()` to fewshot_split by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1276
* Fix whitespace issues in GSM8k-CoT by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1275
* Make `parallelize=True` vs. `accelerate launch` distinction clearer in docs by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1261
* Allow parameter edits for registered tasks when listed in a benchmark by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1273
* Fix data-parallel evaluation with quantized models by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1270
* Rework documentation for explaining local dataset by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1284
* Update CITATION.bib by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1285
* Update `nq_open` / NaturalQs whitespacing by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1289
* Update README.md with custom integration doc by @msaroufim in https://github.com/EleutherAI/lm-evaluation-harness/pull/1298
* Update nq_open.yaml by @Hannibal046 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1305
* Update task_guide.md by @daniellepintz in https://github.com/EleutherAI/lm-evaluation-harness/pull/1306
* Pin `datasets` dependency at 2.15 by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1312
* Fix polemo2_in.yaml subset name by @lhoestq in https://github.com/EleutherAI/lm-evaluation-harness/pull/1313
* Fix `datasets` dependency to >=2.14 by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1314
* Fix group register by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1315
* Update task_guide.md by @djstrong in https://github.com/EleutherAI/lm-evaluation-harness/pull/1316
* Update polemo2_in.yaml by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1318
* Fix: Mamba receives extra kwargs by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1328
* Fix Issue regarding stderr by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1327
* Add `local-completions` support using OpenAI interface by @mgoin in https://github.com/EleutherAI/lm-evaluation-harness/pull/1277
* fallback to classname when LM doesnt have config by @nairbv in https://github.com/EleutherAI/lm-evaluation-harness/pull/1334
* fix a trailing whitespace that breaks a lint job by @nairbv in https://github.com/EleutherAI/lm-evaluation-harness/pull/1335
* skip "benchmarks" in changed_tasks by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1336
* Update migrated HF dataset paths by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1332
* Don't use `get_task_dict()` in task registration / initialization by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1331
* manage default (greedy) gen_kwargs in vllm by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1341
* vllm: change default gen_kwargs behaviour; prompt_logprobs=1 by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1345
* Update links to advanced_task_guide.md by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1348
* `Filter` docs not offset by `doc_id`  by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1349
* Add FAQ on `lm_eval.tasks.initialize_tasks()` to README by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1330
* Refix issue regarding stderr by @thnkinbtfly in https://github.com/EleutherAI/lm-evaluation-harness/pull/1357
* Add causalLM OpenVino models by @NoushNabi in https://github.com/EleutherAI/lm-evaluation-harness/pull/1290
* Apply some best practices and guideline recommendations to code by @LSinev in https://github.com/EleutherAI/lm-evaluation-harness/pull/1363
* serialize callable functions in config by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1367
* delay filter init; remove `*args` by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1369
* Fix unintuitive `--gen_kwargs` behavior by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1329
* Publish to pypi by @anjor in https://github.com/EleutherAI/lm-evaluation-harness/pull/1194
* Make dependencies compatible with PyPI by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1378

## New Contributors
* @shiweijiezero made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1097
* @h-albert-lee made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1089
* @Momo-Tori made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1118
* @xTayEx made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1128
* @NanoCode012 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1124
* @MorishT made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1122
* @lennijusten made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1136
* @veekaybee made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1141
* @wiskojo made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1087
* @polm-stability made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1147
* @seungduk-yanolja made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1171
* @Sparkier made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/990
* @anjor made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1184
* @zachschillaci27 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1109
* @BramVanroy made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1200
* @onnoo made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1218
* @JorgeDeCorte made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1228
* @jmichaelov made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1267
* @jp1924 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1263
* @msaroufim made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1298
* @Hannibal046 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1305
* @daniellepintz made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1306
* @lhoestq made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1313
* @djstrong made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1316
* @nairbv made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1334
* @thnkinbtfly made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1357
* @NoushNabi made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1290
* @LSinev made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1363

**Full Changelog**: https://github.com/EleutherAI/lm-evaluation-harness/compare/v0.4.0...v0.4.1

## v0.4.2 (2024-03-18)

# lm-eval v0.4.2 Release Notes

We are releasing a new minor version of lm-eval for PyPI users! We've been very happy to see continued usage of the lm-evaluation-harness, including as a standard testbench to propel new architecture design (https://arxiv.org/abs/2402.18668), to ease new benchmark creation (https://arxiv.org/abs/2402.11548, https://arxiv.org/abs/2402.00786, https://arxiv.org/abs/2403.01469), enabling controlled experimentation on LLM evaluation (https://arxiv.org/abs/2402.01781), and more!

## New Additions
- Request Caching by @inf3rnus - speedups on startup via caching the construction of documents/requests’ contexts
- Weights and Biases logging by @ayulockin - evals can now be logged to both WandB and Zeno!
- New Tasks
	- KMMLU, a localized - not (auto) translated! - dataset for testing Korean knowledge by @h-albert-lee @guijinSON
	- GPQA by @uanu2002
	- French Bench by @ManuelFay
	- EQ-Bench by @pbevan1 and @sqrkl
	- HAERAE-Bench, readded by @h-albert-lee
	- Updates to answer parsing on many generative tasks  (GSM8k, MGSM, BBH zeroshot) by @thinknbtfly!
	- Okapi (translated) Open LLM Leaderboard tasks by @uanu2002 and @giux78 
	- Arabic MMLU and aEXAMS by @khalil-hennara 
	- And more!
- Re-introduction of `TemplateLM` base class for lower-code new LM class implementations by @anjor
- Run the library with metrics/scoring stage skipped via `--predict_only` by @baberabb
- Many more miscellaneous improvements by a lot of great contributors!

## Backwards Incompatibilities

There were a few breaking changes to lm-eval's general API or logic we'd like to highlight:
### `TaskManager` API 

previously, users had to call `lm_eval.tasks.initialize_tasks()` to register the library's default tasks, or `lm_eval.tasks.include_path()` to include a custom directory of task YAML configs. 

Old usage:
```
import lm_eval

lm_eval.tasks.initialize_tasks() 
# or:
lm_eval.tasks.include_path("/path/to/my/custom/tasks")

 
lm_eval.simple_evaluate(model=lm, tasks=["arc_easy"])
```

New intended usage:
```
import lm_eval

# optional--only need to instantiate separately if you want to pass custom path!
task_manager = TaskManager() # pass include_path="/path/to/my/custom/tasks" if desired

lm_eval.simple_evaluate(model=lm, tasks=["arc_easy"], task_manager=task_manager)
```
`get_task_dict()` now also optionally takes a TaskManager object, when wanting to load custom tasks.

This should allow for much faster library startup times due to lazily loading requested tasks or groups. 

### Updated Stderr Aggregation

Previous versions of the library incorrectly reported erroneously large `stderr` scores for groups of tasks such as MMLU. 

We've since updated the formula to correctly aggregate Standard Error scores for groups of tasks reporting accuracies aggregated via their mean across the dataset -- see #1390 #1427 for more information. 



As always, please feel free to give us feedback or request new features! We're grateful for the community's support. 


## What's Changed
* Add support for RWKV models with World tokenizer by @PicoCreator in https://github.com/EleutherAI/lm-evaluation-harness/pull/1374
* add bypass metric by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1156
* Expand docs, update CITATION.bib by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1227
* Hf: minor egde cases by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1380
* Enable override of printed `n-shot` in table by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1379
* Faster Task and Group Loading, Allow Recursive Groups by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1321
* Fix for https://github.com/EleutherAI/lm-evaluation-harness/issues/1383 by @pminervini in https://github.com/EleutherAI/lm-evaluation-harness/pull/1384
* fix on --task list by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1387
* Support for Inf2 optimum class [WIP] by @michaelfeil in https://github.com/EleutherAI/lm-evaluation-harness/pull/1364
* Update README.md by @mycoalchen in https://github.com/EleutherAI/lm-evaluation-harness/pull/1398
* Fix confusing `write_out.py` instructions in README by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1371
* Use Pooled rather than Combined Variance for calculating stderr of task groupings by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1390
* adding hf_transfer by @michaelfeil in https://github.com/EleutherAI/lm-evaluation-harness/pull/1400
* `batch_size` with `auto` defaults to 1 if `No executable batch size found` is raised by @pminervini in https://github.com/EleutherAI/lm-evaluation-harness/pull/1405
* Fix printing bug in #1390 by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1414
* Fixes https://github.com/EleutherAI/lm-evaluation-harness/issues/1416 by @pminervini in https://github.com/EleutherAI/lm-evaluation-harness/pull/1418
* Fix watchdog timeout by @JeevanBhoot in https://github.com/EleutherAI/lm-evaluation-harness/pull/1404
* Evaluate by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1385
* Add multilingual ARC task by @uanu2002 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1419
* Add multilingual TruthfulQA task by @uanu2002 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1420
* [m_mmul] added multilingual evaluation from alexandrainst/m_mmlu by @giux78 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1358
* Added seeds to `evaluator.simple_evaluate` signature by @Am1n3e in https://github.com/EleutherAI/lm-evaluation-harness/pull/1412
* Fix: task weighting by subtask size ; update Pooled Stderr formula slightly by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1427
* Refactor utilities into a separate model utils file. by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1429
* Nit fix: Updated OpenBookQA Readme by @adavidho in https://github.com/EleutherAI/lm-evaluation-harness/pull/1430
* improve hf_transfer activation by @michaelfeil in https://github.com/EleutherAI/lm-evaluation-harness/pull/1438
* Correct typo in task name in ARC documentation by @larekrow in https://github.com/EleutherAI/lm-evaluation-harness/pull/1443
* update bbh, gsm8k, mmlu parsing logic and prompts (Orca2 bbh_cot_zeroshot 0% -> 42%) by @thnkinbtfly in https://github.com/EleutherAI/lm-evaluation-harness/pull/1356
* Add a new task HaeRae-Bench by @h-albert-lee in https://github.com/EleutherAI/lm-evaluation-harness/pull/1445
* Group reqs by context by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1425
* Add a new task GPQA (the part without CoT) by @uanu2002 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1434
* Added KMMLU evaluation method and changed ReadMe by @h-albert-lee in https://github.com/EleutherAI/lm-evaluation-harness/pull/1447
* Add TemplateLM boilerplate LM class by @anjor in https://github.com/EleutherAI/lm-evaluation-harness/pull/1279
* Log which subtasks were called with which groups by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1456
* PR fixing the issue #1391 (wrong contexts in the mgsm task) by @leocnj in https://github.com/EleutherAI/lm-evaluation-harness/pull/1440
* feat: Add Weights and Biases support by @ayulockin in https://github.com/EleutherAI/lm-evaluation-harness/pull/1339
* Fixed generation args issue affection OpenAI completion model by @Am1n3e in https://github.com/EleutherAI/lm-evaluation-harness/pull/1458
* update parsing logic of mgsm following gsm8k (mgsm en 0 -> 50%) by @thnkinbtfly in https://github.com/EleutherAI/lm-evaluation-harness/pull/1462
* Adding documentation for Weights and Biases CLI interface by @veekaybee in https://github.com/EleutherAI/lm-evaluation-harness/pull/1466
* Add environment and transformers version logging in results dump by @LSinev in https://github.com/EleutherAI/lm-evaluation-harness/pull/1464
* Apply code autoformatting with Ruff to tasks/*.py an *__init__.py by @LSinev in https://github.com/EleutherAI/lm-evaluation-harness/pull/1469
* Setting trust_remote_code to `True` for HuggingFace datasets compatibility by @veekaybee in https://github.com/EleutherAI/lm-evaluation-harness/pull/1467
* add arabic mmlu by @khalil-Hennara in https://github.com/EleutherAI/lm-evaluation-harness/pull/1402
* Add Gemma support (Add flag to control BOS token usage) by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1465
* Revert "Setting trust_remote_code to `True` for HuggingFace datasets compatibility" by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1474
* Create a means for caching task registration and request building. Ad… by @inf3rnus in https://github.com/EleutherAI/lm-evaluation-harness/pull/1372
* Cont metrics by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1475
* Refactor `evaluater.evaluate` by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1441
* add multilingual mmlu eval by @jordane95 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1484
* Update TruthfulQA val split name by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1488
* Fix AttributeError in huggingface.py When 'model_type' is Missing by @richwardle in https://github.com/EleutherAI/lm-evaluation-harness/pull/1489
* Fix duplicated kwargs in some model init by @lchu-ibm in https://github.com/EleutherAI/lm-evaluation-harness/pull/1495
* Add multilingual truthfulqa targets by @jordane95 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1499
* Always include EOS token as stop sequence by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1480
* Improve data-parallel request partitioning for VLLM by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1477
* modify `WandbLogger` to accept arbitrary kwargs by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1491
* Vllm update DP+TP by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1508
* Setting trust_remote_code to True for HuggingFace datasets compatibility by @veekaybee in https://github.com/EleutherAI/lm-evaluation-harness/pull/1487
* Cleaning up unused unit tests by @veekaybee in https://github.com/EleutherAI/lm-evaluation-harness/pull/1516
* French Bench by @ManuelFay in https://github.com/EleutherAI/lm-evaluation-harness/pull/1500
* Hotfix: fix TypeError in `--trust_remote_code` by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1517
* Fix minor edge cases (#951 #1503) by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1520
* Openllm benchmark by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1526
* Add a new task GPQA (the part  CoT and generative) by @uanu2002 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1482
* Add EQ-Bench as per #1459 by @pbevan1 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1511
* Add WMDP Multiple-choice by @justinphan3110 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1534
* Adding new task : KorMedMCQA by @sean0042 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1530
* Update docs on LM.loglikelihood_rolling abstract method by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1532
* Minor KMMLU cleanup by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1502
* Cleanup and fixes (Task, Instance, and a little bit of *evaluate) by @LSinev in https://github.com/EleutherAI/lm-evaluation-harness/pull/1533
* Update installation commands in openai_completions.py and contributing document and, update wandb_args description by @naem1023 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1536
* Add compatibility for vLLM's new Logprob object by @Yard1 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1549
* Fix incorrect `max_gen_toks` generation kwarg default in code2_text. by @cosmo3769 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1551
* Support jinja templating for task descriptions by @HishamYahya in https://github.com/EleutherAI/lm-evaluation-harness/pull/1553
* Fix incorrect `max_gen_toks` generation kwarg default in generative Bigbench by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1546
* Hardcode IFEval to 0-shot by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1506
* add Arabic EXAMS benchmark by @khalil-Hennara in https://github.com/EleutherAI/lm-evaluation-harness/pull/1498
* AGIEval by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1359
* cli_evaluate calls simple_evaluate with the same verbosity. by @Wongboo in https://github.com/EleutherAI/lm-evaluation-harness/pull/1563
* add manual tqdm disabling management by @artemorloff in https://github.com/EleutherAI/lm-evaluation-harness/pull/1569
* Fix README section on vllm integration by @eitanturok in https://github.com/EleutherAI/lm-evaluation-harness/pull/1579
* Fix Jinja template for Advanced AI Risk by @RylanSchaeffer in https://github.com/EleutherAI/lm-evaluation-harness/pull/1587
* Proposed approach for testing CLI arg parsing by @veekaybee in https://github.com/EleutherAI/lm-evaluation-harness/pull/1566
* Patch for Seq2Seq Model predictions by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1584
* Add start date in results.json by @djstrong in https://github.com/EleutherAI/lm-evaluation-harness/pull/1592
* Cleanup for v0.4.2 release by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1573
* Fix eval_logger import for mmlu/_generate_configs.py by @noufmitla in https://github.com/EleutherAI/lm-evaluation-harness/pull/1593

## New Contributors
* @PicoCreator made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1374
* @michaelfeil made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1364
* @mycoalchen made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1398
* @JeevanBhoot made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1404
* @uanu2002 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1419
* @giux78 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1358
* @Am1n3e made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1412
* @adavidho made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1430
* @larekrow made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1443
* @leocnj made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1440
* @ayulockin made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1339
* @khalil-Hennara made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1402
* @inf3rnus made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1372
* @jordane95 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1484
* @richwardle made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1489
* @lchu-ibm made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1495
* @pbevan1 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1511
* @justinphan3110 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1534
* @sean0042 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1530
* @naem1023 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1536
* @Yard1 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1549
* @cosmo3769 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1551
* @HishamYahya made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1553
* @Wongboo made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1563
* @artemorloff made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1569
* @eitanturok made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1579
* @RylanSchaeffer made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1587
* @noufmitla made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1593

**Full Changelog**: https://github.com/EleutherAI/lm-evaluation-harness/compare/v0.4.1...v0.4.2

## v0.4.3 (2024-07-01)

# lm-eval v0.4.3 Release Notes

We're releasing a new version of LM Eval Harness for PyPI users at long last. We intend to release new PyPI versions more frequently in the future.

## New Additions


The big new feature is the often-requested **Chat Templating**, contributed by @KonradSzafer @clefourrier @NathanHB and also worked on by a number of other awesome contributors!

You can now run using a chat template with `--apply_chat_template` and a system prompt of your choosing using `--system_instruction "my sysprompt here"`.  The `--fewshot_as_multiturn` flag can control whether each few-shot example in context is a new conversational turn or not.

This feature is **currently only supported for model types `hf` and `vllm`** but we intend to gather feedback on improvements and also extend this to other relevant models such as APIs.



There's a lot more to check out, including:

- Logging results to the HF Hub if desired using `--hf_hub_log_args`, by @KonradSzafer and team!

- NeMo model support by @sergiopperez !
- Anthropic Chat API support by @tryuman !
- DeepSparse and SparseML model types by @mgoin !

- Handling of delta-weights in HF models, by @KonradSzafer !
- LoRA support for VLLM, by @bcicc !
- Fixes to PEFT modules which add new tokens to the embedding layers, by @mapmeld !

- Fixes to handling of BOS tokens in multiple-choice loglikelihood settings, by @djstrong !
- The use of custom `Sampler` subclasses in tasks, by @LSinev !
- The ability to specify "hardcoded" few-shot examples more cleanly, by @clefourrier !

- Support for Ascend NPUs (`--device npu`) by @statelesshz, @zhabuye, @jiaqiw09 and others!
- Logging of `higher_is_better` in results tables for clearer understanding of eval metrics by @zafstojano !

- extra info logged about models, including info about tokenizers, chat templating, and more, by @artemorloff @djstrong and others!

- Miscellaneous bug fixes! And many more great contributions we weren't able to list here.

## New Tasks

We had a number of new tasks contributed. **A listing of subfolders and a brief description of the tasks contained in them can now be found at `lm_eval/tasks/README.md`**. Hopefully this will be a useful step to help users to locate the definitions of relevant tasks more easily, by first visiting this page and then locating the appropriate README.md within a given `lm_eval/tasks` subfolder, for further info on each task contained within a given folder. Thank you to @AnthonyDipofi @Harryalways317 @nairbv @sepiatone and others for working on this and giving feedback! 


Without further ado, the tasks:
- ACLUE, a benchmark for Ancient Chinese understanding, by @haonan-li
- BasqueGlue and EusExams, two Basque-language tasks by @juletx
- TMMLU+, an evaluation for Traditional Chinese, contributed by @ZoneTwelve
- XNLIeu, a Basque version of XNLI, by @juletx
- Pile-10K, a perplexity eval taken from a subset of the Pile's validation set, contributed by @mukobi
- FDA, SWDE, and Squad-Completion zero-shot tasks by @simran-arora and team
- Added back the `hendrycks_math` task, the MATH task using the prompt and answer parsing from the original Hendrycks et al. MATH paper rather than Minerva's prompt and parsing
- COPAL-ID, a natively-Indonesian commonsense benchmark, contributed by @Erland366
- tinyBenchmarks variants of the Open LLM Leaderboard 1 tasks, by @LucWeber and team!
- Glianorex, a benchmark for testing performance on fictional medical questions, by @maximegmd
- New FLD (formal logic) task variants by @MorishT
- Improved translations of Lambada Multilingual tasks, added by @zafstojano
- NoticIA, a Spanish summarization dataset by @ikergarcia1996
- The Paloma perplexity benchmark, added by @zafstojano
- We've removed the AMMLU dataset due to concerns about auto-translation quality. 
- Added the *localized*, not translated, ArabicMMLU dataset, contributed by @Yazeed7 !
- BertaQA, a Basque cultural knowledge benchmark, by @juletx
- New machine-translated ARC-C datasets by @jonabur !
- CommonsenseQA, in a prompt format following Llama, by @murphybrendan
- ...

## Backwards Incompatibilities

The save format for logged results has now changed.

output files will now be written to 
- `{output_path}/{sanitized_model_name}/results_YYYY-MM-DDTHH-MM-SS.xxxxx.json` if `--output_path` is set, and
- `{output_path}/{sanitized_model_name}/samples_{task_name}_YYYY-MM-DDTHH-MM-SS.xxxxx.jsonl` for each task's samples if `--log_samples` is set.

e.g. `outputs/gpt2/results_2024-06-28T00-00-00.00001.json` and `outputs/gpt2/samples_lambada_openai_2024-06-28T00-00-00.00001.jsonl`.

See https://github.com/EleutherAI/lm-evaluation-harness/pull/1926 for utilities which may help to work with these new filenames.

## Future Plans

In general, we'll be doing our best to keep up with the strong interest and large number of contributions we've seen coming in!


- The official **Open LLM Leaderboard 2** tasks will be landing soon in the Eval Harness main branch and subsequently in `v0.4.4` on PyPI!

- The fact that `group`s of tasks by-default attempt to report an aggregated score across constituent subtasks has been a sharp edge. We are finishing up some internal reworking to distinguish between `group`s of tasks that *do* report aggregate scores (think `mmlu`) versus `tag`s which simply are a convenient shortcut to call a bunch of tasks one might want to run at once (think the `pythia` grouping which merely represents a collection of tasks one might want to gather results on each of all at once but where averaging doesn't make sense).

- We'd also like to improve the API model support in the Eval Harness from its current state.

- More to come!

Thank you to everyone who's contributed to or used the library!

Thanks, @haileyschoelkopf @lintangsutawika

## What's Changed
* use BOS token in loglikelihood by @djstrong in https://github.com/EleutherAI/lm-evaluation-harness/pull/1588
* Revert "Patch for Seq2Seq Model predictions" by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1601
* fix gen_kwargs arg reading by @artemorloff in https://github.com/EleutherAI/lm-evaluation-harness/pull/1607
* fix until arg processing by @artemorloff in https://github.com/EleutherAI/lm-evaluation-harness/pull/1608
* Fixes to Loglikelihood prefix token / VLLM by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1611
* Add ACLUE task by @haonan-li in https://github.com/EleutherAI/lm-evaluation-harness/pull/1614
* OpenAI Completions -- fix passing of unexpected 'until' arg by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1612
* add logging of model args by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1619
* Add vLLM FAQs to README (#1625) by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1633
* peft Version Assertion by @LameloBally in https://github.com/EleutherAI/lm-evaluation-harness/pull/1635
* Seq2seq fix by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1604
* Integration of NeMo models into LM Evaluation Harness library by @sergiopperez in https://github.com/EleutherAI/lm-evaluation-harness/pull/1598
* Fix conditional import for Nemo LM class by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1641
* Fix SuperGlue's ReCoRD task following regression in v0.4 refactoring by @orsharir in https://github.com/EleutherAI/lm-evaluation-harness/pull/1647
* Add Latxa paper evaluation tasks for Basque by @juletx in https://github.com/EleutherAI/lm-evaluation-harness/pull/1654
* Fix CLI --batch_size arg for openai-completions/local-completions by @mgoin in https://github.com/EleutherAI/lm-evaluation-harness/pull/1656
* Patch QQP prompt (#1648 ) by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1661
* TMMLU+ implementation by @ZoneTwelve in https://github.com/EleutherAI/lm-evaluation-harness/pull/1394
* Anthropic Chat API by @tryumanshow in https://github.com/EleutherAI/lm-evaluation-harness/pull/1594
* correction bug EleutherAI#1664 by @nicho2 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1670
* Signpost potential bugs / unsupported ops in MPS backend by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1680
* Add delta weights model loading by @KonradSzafer in https://github.com/EleutherAI/lm-evaluation-harness/pull/1712
* Add `neuralmagic` models for `sparseml` and `deepsparse` by @mgoin in https://github.com/EleutherAI/lm-evaluation-harness/pull/1674
* Improvements to run NVIDIA NeMo models on LM Evaluation Harness by @sergiopperez in https://github.com/EleutherAI/lm-evaluation-harness/pull/1699
* Adding retries and rate limit to toxicity tasks  by @sator-labs in https://github.com/EleutherAI/lm-evaluation-harness/pull/1620
* reference `--tasks list` in README by @nairbv in https://github.com/EleutherAI/lm-evaluation-harness/pull/1726
* Add XNLIeu: a dataset for cross-lingual NLI in Basque by @juletx in https://github.com/EleutherAI/lm-evaluation-harness/pull/1694
* Fix Parameter Propagation for Tasks that have `include`  by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1749
* Support individual scrolls datasets by @giorgossideris in https://github.com/EleutherAI/lm-evaluation-harness/pull/1740
* Add filter registry decorator by @lozhn in https://github.com/EleutherAI/lm-evaluation-harness/pull/1750
* remove duplicated `num_fewshot: 0` by @chujiezheng in https://github.com/EleutherAI/lm-evaluation-harness/pull/1769
* Pile 10k new task by @mukobi in https://github.com/EleutherAI/lm-evaluation-harness/pull/1758
* Fix m_arc choices by @jordane95 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1760
* upload new tasks by @simran-arora in https://github.com/EleutherAI/lm-evaluation-harness/pull/1728
* vllm lora support by @bcicc in https://github.com/EleutherAI/lm-evaluation-harness/pull/1756
* Add option to set OpenVINO config by @helena-intel in https://github.com/EleutherAI/lm-evaluation-harness/pull/1730
* evaluation tracker implementation by @KonradSzafer in https://github.com/EleutherAI/lm-evaluation-harness/pull/1766
* eval tracker args fix by @KonradSzafer in https://github.com/EleutherAI/lm-evaluation-harness/pull/1777
* limit fix by @KonradSzafer in https://github.com/EleutherAI/lm-evaluation-harness/pull/1785
* remove echo parameter in OpenAI completions API by @djstrong in https://github.com/EleutherAI/lm-evaluation-harness/pull/1779
* Fix README: change`----hf_hub_log_args` to `--hf_hub_log_args` by @MuhammadBinUsman03 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1776
* Fix bug in setting until kwarg in openai completions by @ciaranby in https://github.com/EleutherAI/lm-evaluation-harness/pull/1784
* Provide ability for custom sampler for ConfigurableTask by @LSinev in https://github.com/EleutherAI/lm-evaluation-harness/pull/1616
* Update `--tasks list` option in interface documentation by @sepiatone in https://github.com/EleutherAI/lm-evaluation-harness/pull/1792
* Fix Caching Tests ; Remove `pretrained=gpt2` default by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1775
* link to the example output on the hub by @KonradSzafer in https://github.com/EleutherAI/lm-evaluation-harness/pull/1798
* Re-add Hendrycks MATH (no sympy checking, no Minerva hardcoded prompt) variant by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1793
* Logging Updates (Alphabetize table printouts, fix eval tracker bug) (#1774) by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1791
* Initial integration of the Unitxt to LM eval harness by @yoavkatz in https://github.com/EleutherAI/lm-evaluation-harness/pull/1615
* add task for mmlu evaluation in arc multiple choice format by @jonabur in https://github.com/EleutherAI/lm-evaluation-harness/pull/1745
* Update flag `--hf_hub_log_args` in interface documentation by @sepiatone in https://github.com/EleutherAI/lm-evaluation-harness/pull/1806
* Copal task by @Erland366 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1803
* Adding tinyBenchmarks datasets by @LucWeber in https://github.com/EleutherAI/lm-evaluation-harness/pull/1545
* interface doc update by @KonradSzafer in https://github.com/EleutherAI/lm-evaluation-harness/pull/1807
* Fix links in README guiding to another branch by @LSinev in https://github.com/EleutherAI/lm-evaluation-harness/pull/1838
* Fix: support PEFT/LoRA with added tokens by @mapmeld in https://github.com/EleutherAI/lm-evaluation-harness/pull/1828
* Fix incorrect check for task type by @zafstojano in https://github.com/EleutherAI/lm-evaluation-harness/pull/1865
* Fixing typos in `docs` by @zafstojano in https://github.com/EleutherAI/lm-evaluation-harness/pull/1863
* Update polemo2_out.yaml by @zhabuye in https://github.com/EleutherAI/lm-evaluation-harness/pull/1871
* Unpin vllm in dependencies by @edgan8 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1874
* Fix outdated links to the latest links in `docs` by @oneonlee in https://github.com/EleutherAI/lm-evaluation-harness/pull/1876
* [HFLM]Use Accelerate's API to reduce hard-coded CUDA code by @statelesshz in https://github.com/EleutherAI/lm-evaluation-harness/pull/1880
* Fix `batch_size=auto` for HF Seq2Seq models (#1765) by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1790
* Fix Brier Score by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1847
* Fix for bootstrap_iters = 0 case (#1715) by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1789
* add mmlu tasks from pile-t5 by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1710
* Bigbench fix by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1686
* Rename `lm_eval.logging -> lm_eval.loggers` by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1858
* Updated vllm imports in vllm_causallms.py by @mgoin in https://github.com/EleutherAI/lm-evaluation-harness/pull/1890
* [HFLM]Add support for Ascend NPU by @statelesshz in https://github.com/EleutherAI/lm-evaluation-harness/pull/1886
* `higher_is_better` tickers in output table by @zafstojano in https://github.com/EleutherAI/lm-evaluation-harness/pull/1893
* Add dataset card when pushing to HF hub by @KonradSzafer in https://github.com/EleutherAI/lm-evaluation-harness/pull/1898
* Making hardcoded few shots compatible with the chat template mechanism by @clefourrier in https://github.com/EleutherAI/lm-evaluation-harness/pull/1895
* Try to make existing tests run little bit faster by @LSinev in https://github.com/EleutherAI/lm-evaluation-harness/pull/1905
* Fix fewshot seed only set when overriding num_fewshot by @LSinev in https://github.com/EleutherAI/lm-evaluation-harness/pull/1914
* Complete task list from pr 1727 by @anthony-dipofi in https://github.com/EleutherAI/lm-evaluation-harness/pull/1901
* Add chat template by @KonradSzafer in https://github.com/EleutherAI/lm-evaluation-harness/pull/1873
* Multiple Choice Questions and Large Languages Models: A Case Study with Fictional Medical Data by @maximegmd in https://github.com/EleutherAI/lm-evaluation-harness/pull/1867
* Modify pre-commit hook to check merge conflicts accidentally committed by @LSinev in https://github.com/EleutherAI/lm-evaluation-harness/pull/1927
* [add] fld logical formula task by @MorishT in https://github.com/EleutherAI/lm-evaluation-harness/pull/1931
* Add new Lambada translations by @zafstojano in https://github.com/EleutherAI/lm-evaluation-harness/pull/1897
* Implement NoticIA by @ikergarcia1996 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1912
* Add The Arabic version of the PICA benchmark by @khalil-Hennara in https://github.com/EleutherAI/lm-evaluation-harness/pull/1917
* Fix social_iqa answer choices by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1909
* Update basque-glue by @zhabuye in https://github.com/EleutherAI/lm-evaluation-harness/pull/1913
* Test output table layout consistency by @zafstojano in https://github.com/EleutherAI/lm-evaluation-harness/pull/1916
* Fix a tiny typo in `__main__.py` by @sadra-barikbin in https://github.com/EleutherAI/lm-evaluation-harness/pull/1939
* Add the Arabic version with refactor to Arabic pica to be in alghafa … by @khalil-Hennara in https://github.com/EleutherAI/lm-evaluation-harness/pull/1940
* Results filenames handling fix by @KonradSzafer in https://github.com/EleutherAI/lm-evaluation-harness/pull/1926
* Remove AMMLU Due to Translation by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1948
* Add option in TaskManager to not index library default tasks ; Tests for include_path by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1856
* Force BOS token usage in 'gemma' models for VLLM by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1857
* Fix a tiny typo in `docs/interface.md` by @sadra-barikbin in https://github.com/EleutherAI/lm-evaluation-harness/pull/1955
* Fix self.max_tokens in anthropic_llms.py by @lozhn in https://github.com/EleutherAI/lm-evaluation-harness/pull/1848
* `samples` is newline delimited by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/1930
* Fix `--gen_kwargs` and VLLM (`temperature` not respected) by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1800
* Make `scripts.write_out` error out when no splits match by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1796
* fix: add directory filter to os.walk to ignore 'ipynb_checkpoints' by @johnwee1 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1956
* add trust_remote_code  for piqa by @changwangss in https://github.com/EleutherAI/lm-evaluation-harness/pull/1983
* Fix self assignment in neuron_optimum.py by @LSinev in https://github.com/EleutherAI/lm-evaluation-harness/pull/1990
* [New Task] Add Paloma benchmark by @zafstojano in https://github.com/EleutherAI/lm-evaluation-harness/pull/1928
* Fix Paloma Template yaml by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1993
* Log `fewshot_as_multiturn` in results files by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1995
* Added ArabicMMLU by @Yazeed7 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1987
* Fix Datasets `--trust_remote_code` by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1998
* Add BertaQA dataset tasks by @juletx in https://github.com/EleutherAI/lm-evaluation-harness/pull/1964
* add tokenizer logs info by @artemorloff in https://github.com/EleutherAI/lm-evaluation-harness/pull/1731
* Hotfix breaking import by @StellaAthena in https://github.com/EleutherAI/lm-evaluation-harness/pull/2015
* add arc_challenge_mt by @jonabur in https://github.com/EleutherAI/lm-evaluation-harness/pull/1900
* Remove `LM` dependency from `build_all_requests` by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2011
* Added CommonsenseQA task by @murphybrendan in https://github.com/EleutherAI/lm-evaluation-harness/pull/1721
* Factor out LM-specific tests by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/1859
* Update interface.md by @johnwee1 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1982
* Fix `trust_remote_code`-related test failures by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/2024
* Fixes scrolls task bug with few_shot examples by @xksteven in https://github.com/EleutherAI/lm-evaluation-harness/pull/2003
* fix cache by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2037
* Add chat template to `vllm` by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2034
* Fail gracefully upon tokenizer logging failure (#2035) by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/2038
* Bundle `exact_match` HF Evaluate metric with install, don't call evaluate.load() on import by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/2045
* Update package version to v0.4.3 by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/2046

## New Contributors
* @LameloBally made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1635
* @sergiopperez made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1598
* @orsharir made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1647
* @ZoneTwelve made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1394
* @tryumanshow made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1594
* @nicho2 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1670
* @KonradSzafer made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1712
* @sator-labs made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1620
* @giorgossideris made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1740
* @lozhn made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1750
* @chujiezheng made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1769
* @mukobi made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1758
* @simran-arora made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1728
* @bcicc made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1756
* @helena-intel made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1730
* @MuhammadBinUsman03 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1776
* @ciaranby made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1784
* @sepiatone made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1792
* @yoavkatz made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1615
* @Erland366 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1803
* @LucWeber made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1545
* @mapmeld made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1828
* @zafstojano made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1865
* @zhabuye made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1871
* @edgan8 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1874
* @oneonlee made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1876
* @statelesshz made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1880
* @clefourrier made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1895
* @maximegmd made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1867
* @ikergarcia1996 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1912
* @sadra-barikbin made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1939
* @johnwee1 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1956
* @changwangss made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1983
* @Yazeed7 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1987
* @murphybrendan made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1721
* @xksteven made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2003

**Full Changelog**: https://github.com/EleutherAI/lm-evaluation-harness/compare/v0.4.2...v0.4.3

## v0.4.4 (2024-09-05)

# lm-eval v0.4.4 Release Notes

## New Additions

- This release includes the **Open LLM Leaderboard 2** official task implementations! These can be run by using `--tasks leaderboard`. Thank you to the HF team (@clefourrier, @NathanHB , @KonradSzafer, @lozovskaya) for contributing these -- you can read more about their Open LLM Leaderboard 2 release [here](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard). 



- **API support is overhauled!** Now: support for *concurrent requests*, chat templates, tokenization, *batching* and improved customization. This makes API support both more generalizable to new providers and should dramatically speed up API model inference.
    - The url can be specified by passing the `base_url` to `--model_args`, for example, `base_url=http://localhost:8000/v1/completions`; concurrent requests are controlled with the `num_concurrent` argument; tokenization is controlled with `tokenized_requests`. 
    - Other arguments (such as top_p, top_k, etc.) can be passed to the API using `--gen_kwargs` as usual.
    - Note: Instruct-tuned models, not just base models, can be used with `local-completions` using `--apply_chat_template` (either with or without `tokenized_requests`). 
        - They can also be used with `local-chat-completions` (for e.g. with a OpenAI Chat API endpoint), but only the former supports loglikelihood tasks (e.g. multiple-choice). **This is because ChatCompletion style APIs generally do not provide access to logits on prompt/input tokens, preventing easy measurement of multi-token continuations' log probabilities.**
    - example with OpenAI completions API (using vllm serve):
        - `lm_eval --model local-completions --model_args model=meta-llama/Meta-Llama-3.1-8B-Instruct,num_concurrent=10,tokenized_requests=True,tokenizer_backend=huggingface,max_length=4096 --apply_chat_template --batch_size 1 --tasks mmlu`
    - example with chat API:
        - `lm_eval --model local-chat-completions --model_args model=meta-llama/Meta-Llama-3.1-8B-Instruct,num_concurrent=10 --apply_chat_template --tasks gsm8k`
    - We recommend evaluating Llama-3.1-405B models via serving them with vllm then running under `local-completions`!

- **We've reworked the Task Grouping system to make it clearer when and when not to report an aggregated average score across multiple subtasks**. See **#Backwards Incompatibilities** below for more information on changes and migration instructions.

- A combination of data-parallel and model-parallel (using HF's `device_map` functionality for "naive" pipeline parallel) inference using `--model hf` is now supported, thank you to @NathanHB and team!

Other new additions include a number of miscellaneous bugfixes and much more. Thank you to all contributors who helped out on this release!


## New Tasks

A number of new tasks have been contributed to the library.

As a further discoverability improvement, `lm_eval --tasks list` now shows all tasks, tags, and groups in a prettier format, along with (if applicable) where to find the associated config file for a task or group! Thank you to @anthony-dipofi for working on this.

New tasks as of v0.4.4 include:
- Open LLM Leaderboard 2 tasks--see above!
- Inverse Scaling tasks, contributed by @h-albert-lee in #1589
- Unitxt tasks reworked by @elronbandel in #1933
- MMLU-SR, contributed by @SkySuperCat in #2032
- IrokoBench, contributed by @JessicaOjo @IsraelAbebe in #2042
- MedConceptQA, contributed by @Ofir408 in #2010
- MMLU Pro, contributed by @ysjprojects in #1961
- GSM-Plus, contributed by @ysjprojects in #2103
- Lingoly, contributed by @am-bean in #2198
- GSM8k and Asdiv settings matching the Llama 3.1 evaluation settings, contributed by @Cameron7195 in #2215 #2236
- TMLU, contributed by @adamlin120 in #2093
- Mela, contributed by @Geralt-Targaryen in #1970




## Backwards Incompatibilities

### `tag`s versus `group`s, and how to migrate

Previously, we supported the ability to group a set of tasks together, generally for two purposes: 1) to have an easy-to-call shortcut for a set of tasks one might want to frequently run simultaneously, and 2) to allow for "parent" tasks like `mmlu` to aggregate and report a unified score across a set of component "subtasks".


There were two ways to add a task to a given `group` name: 1) to provide (a list of) values to the `group` field in a given subtask's config file:

```yaml
# this is a *task* yaml file.
group: group_name1
task: my_task1
# rest of task config goes here...
```

or 2) to define a "group config file" and specify a group along with its constituent subtasks:

```yaml
# this is a group's yaml file
group: group_name1
task:
  - subtask_name1
  - subtask_name2
  # ...
```

These would both have the same effect of **reporting an averaged metric for group_name1** when calling `lm_eval --tasks group_name1`. However, in use-case 1) (simply registering a shorthand for a list of tasks one is interested in), reporting an aggregate score can be undesirable or ill-defined.

**We've now separated out these two use-cases ("shorthand" groupings and hierarchical subtask collections) into a `tag` and `group` property separately!**

To register a *shorthand* (now called a **`tag`**), simply change the `group` field name within your task's config to be `tag` (`group_alias` keys will no longer be supported in task configs.):

```yaml
# this is a *task* yaml file.
tag: tag_name1
task: my_task1
# rest of task config goes here...
```

Group config files may remain as is if aggregation is not desired. **To opt-in to reporting aggregated scores across a group's subtasks, add the following to your group config file**:

```yaml
# this is a group's yaml file
group: group_name1
task:
  - subtask_name1
  - subtask_name2
  # ...
 ### New! Needed to turn on aggregation ###
 aggregate_metric_list:
  - metric: acc # placeholder. Note that all subtasks in this group must report an `acc` metric key
  - weight_by_size: True # whether one wishes to report *micro* or *macro*-averaged scores across subtasks. Defaults to `True`.
  
```

Please see our documentation [here](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/new_task_guide.md#advanced-group-configs) for more information. We apologize for any headaches this migration may create--however, we believe separating out these two functionalities will make it less likely for users to encounter confusion or errors related to mistaken undesired aggregation. 


### Future Plans

We're planning to make more planning documents public and standardize on (likely) 1 new PyPI release per month! Stay tuned.


Thanks, the LM Eval Harness team (@haileyschoelkopf @lintangsutawika @baberabb)


## What's Changed
* fix wandb logger module import in example by @ToluClassics in https://github.com/EleutherAI/lm-evaluation-harness/pull/2041
* Fix strip whitespace filter by @NathanHB in https://github.com/EleutherAI/lm-evaluation-harness/pull/2048
* Gemma-2 also needs default `add_bos_token=True` by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/2049
* Update `trust_remote_code` for Hellaswag by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/2029
* Adds Open LLM Leaderboard Taks by @NathanHB in https://github.com/EleutherAI/lm-evaluation-harness/pull/2047
* #1442 inverse scaling tasks implementation by @h-albert-lee in https://github.com/EleutherAI/lm-evaluation-harness/pull/1589
* Fix TypeError in samplers.py by converting int to str by @uni2237 in https://github.com/EleutherAI/lm-evaluation-harness/pull/2074
* Group agg rework by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/1741
* Fix printout tests (N/A expected for stderrs) by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/2080
* Easier unitxt tasks loading and removal of unitxt library dependancy  by @elronbandel in https://github.com/EleutherAI/lm-evaluation-harness/pull/1933
* Allow gating EvaluationTracker HF Hub results; customizability by @NathanHB in https://github.com/EleutherAI/lm-evaluation-harness/pull/2051
* Minor doc fix: leaderboard README.md missing mmlu-pro group and task by @pankajarm in https://github.com/EleutherAI/lm-evaluation-harness/pull/2075
* Revert missing utf-8 encoding for logged sample files (#2027) by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/2082
* Update utils.py by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/2085
* batch_size may be str if 'auto' is specified by @meg-huggingface in https://github.com/EleutherAI/lm-evaluation-harness/pull/2084
* Prettify lm_eval --tasks list by @anthony-dipofi in https://github.com/EleutherAI/lm-evaluation-harness/pull/1929
* Suppress noisy RougeScorer logs in `truthfulqa_gen` by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/2090
* Update default.yaml by @waneon in https://github.com/EleutherAI/lm-evaluation-harness/pull/2092
* Add new dataset MMLU-SR tasks by @SkySuperCat in https://github.com/EleutherAI/lm-evaluation-harness/pull/2032
* Irokobench: Benchmark Dataset for African languages by @JessicaOjo in https://github.com/EleutherAI/lm-evaluation-harness/pull/2042
* docs: remove trailing sentence from contribution doc by @nathan-weinberg in https://github.com/EleutherAI/lm-evaluation-harness/pull/2098
* Added MedConceptsQA Benchmark by @Ofir408 in https://github.com/EleutherAI/lm-evaluation-harness/pull/2010
* Also force BOS for `"recurrent_gemma"` and other Gemma model types by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/2105
* formatting by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/2104
* docs: align local test command to match CI by @nathan-weinberg in https://github.com/EleutherAI/lm-evaluation-harness/pull/2100
* Fixed colon in Belebele _default_template_yaml by @jab13x in https://github.com/EleutherAI/lm-evaluation-harness/pull/2111
* Fix haerae task groups by @jungwhank in https://github.com/EleutherAI/lm-evaluation-harness/pull/2112
* fix: broken discord link in CONTRIBUTING.md by @nathan-weinberg in https://github.com/EleutherAI/lm-evaluation-harness/pull/2114
* docs: update truthfulqa tasks by @CandiedCode in https://github.com/EleutherAI/lm-evaluation-harness/pull/2119
* Hotfix `lm_eval.caching` module by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/2124
* Refactor API models by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2008
* bugfix and docs for API by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2139
* [Bugfix] add temperature=0 to logprobs and seed args to API models by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2149
* refactor: limit usage of `scipy` and `skilearn` dependencies by @nathan-weinberg in https://github.com/EleutherAI/lm-evaluation-harness/pull/2097
* Update lm-eval-overview.ipynb by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/2118
* fix typo. by @kargaranamir in https://github.com/EleutherAI/lm-evaluation-harness/pull/2169
* Incorrect URL by @zhabuye in https://github.com/EleutherAI/lm-evaluation-harness/pull/2125
* Dp and mp support by @NathanHB in https://github.com/EleutherAI/lm-evaluation-harness/pull/2056
* [hotfix] API: messages were created twice by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2174
* add okapi machine translated notice. by @kargaranamir in https://github.com/EleutherAI/lm-evaluation-harness/pull/2168
* IrokoBench: Fix incorrect group assignments by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/2181
* Mmlu Pro by @ysjprojects in https://github.com/EleutherAI/lm-evaluation-harness/pull/1961
* added gsm_plus by @ysjprojects in https://github.com/EleutherAI/lm-evaluation-harness/pull/2103
* Fix `revision` kwarg dtype in edge-cases by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/2184
* Small README tweaks by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/2186
* gsm_plus minor fix by @ysjprojects in https://github.com/EleutherAI/lm-evaluation-harness/pull/2191
* keep new line for task description by @jungwhank in https://github.com/EleutherAI/lm-evaluation-harness/pull/2116
* Update README.md by @ysjprojects in https://github.com/EleutherAI/lm-evaluation-harness/pull/2206
* Update citation in README.md by @antonpolishko in https://github.com/EleutherAI/lm-evaluation-harness/pull/2083
* New task: Lingoly by @am-bean in https://github.com/EleutherAI/lm-evaluation-harness/pull/2198
* Created a new task for gsm8k which corresponds to the Llama cot settings… by @Cameron7195 in https://github.com/EleutherAI/lm-evaluation-harness/pull/2215
* Lingoly README update by @am-bean in https://github.com/EleutherAI/lm-evaluation-harness/pull/2228
* Update yaml to adapt to belebele dataset changes by @Uminosachi in https://github.com/EleutherAI/lm-evaluation-harness/pull/2216
* Add TMLU Benchmark Dataset by @adamlin120 in https://github.com/EleutherAI/lm-evaluation-harness/pull/2093
* Update IFEval dataset to official one by @lewtun in https://github.com/EleutherAI/lm-evaluation-harness/pull/2218
* fix the leaderboard doc to reflect the tasks by @NathanHB in https://github.com/EleutherAI/lm-evaluation-harness/pull/2219
* Add multiple chat template by @KonradSzafer in https://github.com/EleutherAI/lm-evaluation-harness/pull/2129
* Update CODEOWNERS by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/2229
* Fix Zeno Visualizer by @namtranase in https://github.com/EleutherAI/lm-evaluation-harness/pull/2227
* mela by @Geralt-Targaryen in https://github.com/EleutherAI/lm-evaluation-harness/pull/1970
* fix the regex string in mmlu_pro template by @lxning in https://github.com/EleutherAI/lm-evaluation-harness/pull/2238
* Fix logging when resizing embedding layer in peft mode by @WPoelman in https://github.com/EleutherAI/lm-evaluation-harness/pull/2239
* fix mmlu_pro typo by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2241
* Fix typos in multiple places by @LSinev in https://github.com/EleutherAI/lm-evaluation-harness/pull/2244
* fix group args of mmlu and mmlu_pro by @eyuansu62 in https://github.com/EleutherAI/lm-evaluation-harness/pull/2245
* Created new task for testing Llama on Asdiv by @Cameron7195 in https://github.com/EleutherAI/lm-evaluation-harness/pull/2236
* chat template hotfix by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2250
* [Draft] More descriptive `simple_evaluate()` LM TypeError by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/2258
* Update NLTK version in `*ifeval` tasks ( #2210 ) by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/2259
* Fix `loglikelihood_rolling` caching ( #1821 ) by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/2187
* API: fix maxlen; vllm: prefix_token_id bug by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2262
* hotfix #2262 by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2264
* Chat Template fix (cont. #2235) by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2269
* Bump version to v0.4.4 ; Fixes to TMMLUplus by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/2280

## New Contributors
* @ToluClassics made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2041
* @NathanHB made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2048
* @uni2237 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2074
* @elronbandel made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1933
* @pankajarm made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2075
* @meg-huggingface made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2084
* @waneon made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2092
* @SkySuperCat made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2032
* @JessicaOjo made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2042
* @nathan-weinberg made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2098
* @Ofir408 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2010
* @jab13x made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2111
* @jungwhank made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2112
* @CandiedCode made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2119
* @kargaranamir made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2169
* @ysjprojects made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1961
* @antonpolishko made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2083
* @am-bean made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2198
* @Cameron7195 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2215
* @Uminosachi made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2216
* @adamlin120 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2093
* @lewtun made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2218
* @namtranase made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2227
* @Geralt-Targaryen made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1970
* @lxning made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2238
* @WPoelman made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2239
* @eyuansu62 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2245

**Full Changelog**: https://github.com/EleutherAI/lm-evaluation-harness/compare/v0.4.3...v0.4.4

## v0.4.5 (2024-10-08)

# lm-eval v0.4.5 Release Notes

## New Additions

### Prototype Support for Vision Language Models (VLMs)

We're excited to introduce prototype support for Vision Language Models (VLMs) in this release, using model types `hf-multimodal` and `vllm-vlm`.  This allows for evaluation of models that can process text and image inputs and produce text outputs. Currently we have added support for the MMMU (`mmmu_val`) task and we welcome contributions and feedback from the community!

#### New VLM-Specific Arguments

VLM models can be configured with several new arguments within `--model_args` to support their specific requirements:

- `max_images` (int): Set the maximum number of images for each prompt.
- `interleave` (bool): Determines the positioning of image inputs. When `True` (default) images are interleaved with the text. When `False` all images are placed at the front of the text. This is model dependent.

`hf-multimodal` specific args:
- `image_token_id` (int) or `image_string` (str): Specifies a custom token or string for image placeholders. For example, Llava models expect an `"<image>"` string to indicate the location of images in the input, while Qwen2-VL models expect an `"<|image_pad|>"` sentinel string instead. This will be inferred based on model configuration files whenever possible, but we recommend confirming that an override is needed when testing a new model family
- `convert_img_format` (bool): Whether to convert the images to RGB format.

#### Example usage:

- `lm_eval --model hf-multimodal --model_args pretrained=llava-hf/llava-1.5-7b-hf,attn_implementation=flash_attention_2,max_images=1,interleave=True,image_string=<image> --tasks mmmu_val --apply_chat_template`

- `lm_eval --model vllm-vlm --model_args pretrained=llava-hf/llava-1.5-7b-hf,max_images=1,interleave=True --tasks mmmu_val --apply_chat_template`

#### Important considerations

1. **Chat Template**: Most VLMs require the `--apply_chat_template` flag to ensure proper input formatting according to the model's expected chat template.
2. Some VLM models are limited to processing a single image per prompt. For these models, always set `max_images=1`. Additionally, certain models expect image placeholders to be non-interleaved with the text, requiring `interleave=False`.
3. Performance and Compatibility: When working with VLMs, be mindful of potential memory constraints and processing times, especially when handling multiple images or complex tasks.

#### Tested VLM Models

We have currently most notably tested the implementation with the following models:

- llava-hf/llava-1.5-7b-hf
- llava-hf/llava-v1.6-mistral-7b-hf
- Qwen/Qwen2-VL-2B-Instruct
- HuggingFaceM4/idefics2 (requires the latest `transformers` from source)


## New Tasks

Several new tasks have been contributed to the library for this version!


New tasks as of v0.4.5 include:
- Open Arabic LLM Leaderboard tasks, contributed by @shahrzads @Malikeh97 in #2232
- **MMMU (validation set), by @haileyschoelkopf @baberabb @lintangsutawika in #2243**
- TurkishMMLU by @ArdaYueksel in #2283
- PortugueseBench, SpanishBench, GalicianBench, BasqueBench, and CatalanBench aggregate multilingual tasks in #2153 #2154 #2155 #2156 #2157 by @zxcvuser and others


As well as several slight fixes or changes to existing tasks (as noted via the incrementing of versions).


## Backwards Incompatibilities

### Finalizing `group` versus `tag` split

We've now fully deprecated the use of `group` keys directly within a task's configuration file. The appropriate key to use is now solely `tag` for many cases. See the [v0.4.4 patchnotes](https://github.com/EleutherAI/lm-evaluation-harness/releases/tag/v0.4.4) for more info on migration, if you have a set of task YAMLs maintained outside the Eval Harness repository.

### Handling of Causal vs. Seq2seq backend in HFLM

In HFLM, logic specific to handling inputs for Seq2seq (encoder-decoder models like T5) versus Causal (decoder-only autoregressive models, and the vast majority of current LMs) models previously hinged on a check for `self.AUTO_MODEL_CLASS == transformers.AutoModelForCausalLM`. Some users may want to use causal model behavior, but set `self.AUTO_MODEL_CLASS` to a different factory class, such as `transformers.AutoModelForVision2Seq`.

As a result, those users who subclass HFLM but do not call `HFLM.__init__()` may now also need to set the `self.backend` attribute to either `"causal"` or `"seq2seq"` during initialization themselves.

While this should not affect a large majority of users, for those who subclass HFLM in potentially advanced ways, see https://github.com/EleutherAI/lm-evaluation-harness/pull/2353 for the full set of changes.

### Future Plans

We intend to further expand our multimodal support to a wider set of vision-language tasks, as well as a broader set of model types, and are actively seeking user feedback!

Thanks, the LM Eval Harness team (@baberabb @haileyschoelkopf @lintangsutawika)



## What's Changed
* Add Open Arabic LLM Leaderboard Benchmarks (Full and Light Version) by @Malikeh97 in https://github.com/EleutherAI/lm-evaluation-harness/pull/2232
* Multimodal prototyping by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/2243
* Update README.md by @SYusupov in https://github.com/EleutherAI/lm-evaluation-harness/pull/2297
* remove comma by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2315
* Update neuron backend by @dacorvo in https://github.com/EleutherAI/lm-evaluation-harness/pull/2314
* Fixed dummy model by @Am1n3e in https://github.com/EleutherAI/lm-evaluation-harness/pull/2339
* Add a note for missing dependencies by @eldarkurtic in https://github.com/EleutherAI/lm-evaluation-harness/pull/2336
* squad v2: load metric with `evaluate` by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2351
* fix writeout script by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2350
* Treat tags in python tasks the same as yaml tasks by @giuliolovisotto in https://github.com/EleutherAI/lm-evaluation-harness/pull/2288
* change group to tags in task `eus_exams` task configs by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2320
* change glianorex to test split by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2332
* mmlu-pro: add newlines to task descriptions (not leaderboard) by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2334
* Added TurkishMMLU to LM Evaluation Harness by @ArdaYueksel in https://github.com/EleutherAI/lm-evaluation-harness/pull/2283
* add mmlu readme by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2282
* openai: better error messages; fix greedy matching by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2327
* fix some bugs of mmlu by @eyuansu62 in https://github.com/EleutherAI/lm-evaluation-harness/pull/2299
* Add new benchmark: Portuguese bench by @zxcvuser in https://github.com/EleutherAI/lm-evaluation-harness/pull/2156
* Fix missing key in custom task loading. by @giuliolovisotto in https://github.com/EleutherAI/lm-evaluation-harness/pull/2304
* Add new benchmark: Spanish bench by @zxcvuser in https://github.com/EleutherAI/lm-evaluation-harness/pull/2157
* Add new benchmark: Galician bench by @zxcvuser in https://github.com/EleutherAI/lm-evaluation-harness/pull/2155
* Add new benchmark: Basque bench by @zxcvuser in https://github.com/EleutherAI/lm-evaluation-harness/pull/2153
* Add new benchmark: Catalan bench by @zxcvuser in https://github.com/EleutherAI/lm-evaluation-harness/pull/2154
* fix tests by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2380
* Hotfix! by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2383
* Solution for CSAT-QA tasks evaluation by @KyujinHan in https://github.com/EleutherAI/lm-evaluation-harness/pull/2385
* LingOly - Fixing scoring bugs for smaller models by @am-bean in https://github.com/EleutherAI/lm-evaluation-harness/pull/2376
* Fix float limit override by @cjluo-omniml in https://github.com/EleutherAI/lm-evaluation-harness/pull/2325
* [API] tokenizer: add trust-remote-code by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2372
* HF: switch conditional checks to `self.backend` from `AUTO_MODEL_CLASS` by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2353
* max_images are passed on to vllms `limit_mm_per_prompt` by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2387
* Fix Llava-1.5-hf ; Update to version 0.4.5 by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/2388
* Bump version to v0.4.5 by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/2389

## New Contributors
* @Malikeh97 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2232
* @SYusupov made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2297
* @dacorvo made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2314
* @eldarkurtic made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2336
* @giuliolovisotto made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2288
* @ArdaYueksel made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2283
* @zxcvuser made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2156
* @KyujinHan made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2385
* @cjluo-omniml made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2325

**Full Changelog**: https://github.com/EleutherAI/lm-evaluation-harness/compare/v0.4.4...v0.4.5

## v0.4.6 (2024-11-25)

# lm-eval v0.4.6 Release Notes

This release brings important changes to chat template handling, expands our task library with new multilingual and multimodal benchmarks, and includes various bug fixes.

## Backwards Incompatibilities

### Chat Template Delimiter Handling

An important modification has been made to how delimiters are handled when applying chat templates in request construction, particularly affecting multiple-choice tasks. This change ensures better compatibility with chat models by respecting their native formatting conventions.

📝 For detailed documentation, please refer to [docs/chat-template-readme.md](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/chat-template-readme.md)

## New Benchmarks & Tasks

### Multilingual Expansion
- **Spanish Bench**: Enhanced benchmark with additional tasks by @zxcvuser in #2390
- **Japanese Leaderboard**: New comprehensive Japanese language benchmark by @sitfoxfly in #2439

### New Task Collections
- **Multimodal Unitext**: Added support for multimodal tasks available in unitext by @elronbandel in #2364
- **Metabench**: New benchmark contributed by @kozzy97 in #2357

As well as several slight fixes or changes to existing tasks (as noted via the incrementing of versions).

Thanks, the LM Eval Harness team (@baberabb and @lintangsutawika)



## What's Changed
* Add Unitxt Multimodality Support by @elronbandel in https://github.com/EleutherAI/lm-evaluation-harness/pull/2364
* Add new tasks to spanish_bench and fix duplicates by @zxcvuser in https://github.com/EleutherAI/lm-evaluation-harness/pull/2390
* fix typo bug for minerva_math by @renjie-ranger in https://github.com/EleutherAI/lm-evaluation-harness/pull/2404
* Fix: Turkish MMLU Regex Pattern by @ArdaYueksel in https://github.com/EleutherAI/lm-evaluation-harness/pull/2393
* fix storycloze datanames by @t1101675 in https://github.com/EleutherAI/lm-evaluation-harness/pull/2409
* Update NoticIA prompt by @ikergarcia1996 in https://github.com/EleutherAI/lm-evaluation-harness/pull/2421
* [Fix] Replace generic exception classes with a more specific ones by @LSinev in https://github.com/EleutherAI/lm-evaluation-harness/pull/1989
* Support for IBM watsonx_llm by @Medokins in https://github.com/EleutherAI/lm-evaluation-harness/pull/2397
* Fix package extras for watsonx support by @kiersten-stokes in https://github.com/EleutherAI/lm-evaluation-harness/pull/2426
* Fix lora requests when dp with vllm by @ckgresla in https://github.com/EleutherAI/lm-evaluation-harness/pull/2433
* Add xquad task by @zxcvuser in https://github.com/EleutherAI/lm-evaluation-harness/pull/2435
* Add verify_certificate argument to local-completion by @sjmonson in https://github.com/EleutherAI/lm-evaluation-harness/pull/2440
* Add GPTQModel support for evaluating GPTQ models by @Qubitium in https://github.com/EleutherAI/lm-evaluation-harness/pull/2217
* Add missing task links by @Sypherd in https://github.com/EleutherAI/lm-evaluation-harness/pull/2449
* Update CODEOWNERS by @haileyschoelkopf in https://github.com/EleutherAI/lm-evaluation-harness/pull/2453
* Add real process_docs example by @Sypherd in https://github.com/EleutherAI/lm-evaluation-harness/pull/2456
* Modify label errors in catcola and paws-x by @zxcvuser in https://github.com/EleutherAI/lm-evaluation-harness/pull/2434
* Add Japanese Leaderboard by @sitfoxfly in https://github.com/EleutherAI/lm-evaluation-harness/pull/2439
* Typos: Fix 'loglikelihood' misspellings in api_models.py by @RobGeada in https://github.com/EleutherAI/lm-evaluation-harness/pull/2459
* use global `multi_choice_filter` for mmlu_flan by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2461
* typo by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2465
* pass device_map other than auto for parallelize by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2457
* OpenAI ChatCompletions: switch `max_tokens` by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2443
* Ifeval: Dowload `punkt_tab` on rank 0 by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2267
* Fix chat template; fix leaderboard math by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2475
* change warning to debug by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2481
* Updated wandb logger to use `new_printer()` instead of `get_printer(...)` by @alex-titterton in https://github.com/EleutherAI/lm-evaluation-harness/pull/2484
* IBM watsonx_llm fixes & refactor by @Medokins in https://github.com/EleutherAI/lm-evaluation-harness/pull/2464
* Fix revision parameter to vllm get_tokenizer by @OyvindTafjord in https://github.com/EleutherAI/lm-evaluation-harness/pull/2492
* update pre-commit hooks and git actions by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2497
* kbl-v0.1.1 by @whwang299 in https://github.com/EleutherAI/lm-evaluation-harness/pull/2493
* Add mamba hf to `mamba_ssm` by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2496
* remove duplicate `arc_ca` tag by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2499
* Add metabench task to LM Evaluation Harness by @kozzy97 in https://github.com/EleutherAI/lm-evaluation-harness/pull/2357
* Nits by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2500
* [API models] parse tokenizer_backend=None properly by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2509

## New Contributors
* @renjie-ranger made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2404
* @t1101675 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2409
* @Medokins made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2397
* @kiersten-stokes made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2426
* @ckgresla made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2433
* @sjmonson made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2440
* @Qubitium made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2217
* @Sypherd made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2449
* @sitfoxfly made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2439
* @RobGeada made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2459
* @alex-titterton made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2484
* @OyvindTafjord made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2492
* @whwang299 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2493
* @kozzy97 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2357

**Full Changelog**: https://github.com/EleutherAI/lm-evaluation-harness/compare/v0.4.5...v0.4.6

## v0.4.7 (2024-12-17)

# lm-eval v0.4.7 Release Notes

This release includes several bug fixes, minor improvements to model handling, and task additions.

## ⚠️ Python 3.8 End of Support Notice
Python 3.8 support will be dropped in future releases as it has reached its end of life. Users are encouraged to upgrade to Python 3.9 or newer.

## Backwards Incompatibilities

### Chat Template Delimiter Handling (in v0.4.6)

An important modification has been made to how delimiters are handled when applying chat templates in request construction, particularly affecting multiple-choice tasks. This change ensures better compatibility with chat models by respecting their native formatting conventions.

📝 For detailed documentation, please refer to [docs/chat-template-readme.md](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/chat-template-readme.md)

## New Benchmarks & Tasks

- Basque Integration: Added Basque translation of PIQA (piqa_eu) to BasqueBench by @naiarapm in #2531
- SCORE Tasks: Added new subtask for non-greedy robustness evaluation by @rimashahbazyan in #2558

As well as several slight fixes or changes to existing tasks (as noted via the incrementing of versions).

Thanks, the LM Eval Harness team (@baberabb and @lintangsutawika)


## What's Changed
* Score tasks by @rimashahbazyan in https://github.com/EleutherAI/lm-evaluation-harness/pull/2452
* Filters bugfix; add `metrics` and `filter` to logged sample by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2517
* skip casting if predict_only by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2524
* make utility function to handle `until` by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2518
* Update Unitxt task to  use locally installed unitxt and not download Unitxt code from Huggingface by @yoavkatz in https://github.com/EleutherAI/lm-evaluation-harness/pull/2514
* add Basque translation of PIQA (piqa_eu) to BasqueBench by @naiarapm in https://github.com/EleutherAI/lm-evaluation-harness/pull/2531
* avoid timeout errors with high concurrency in api_model by @dtrawins in https://github.com/EleutherAI/lm-evaluation-harness/pull/2307
* Update README.md by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2534
* better doc_to_test testing by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2535
* Support pipeline parallel with OpenVINO models by @sstrehlk in https://github.com/EleutherAI/lm-evaluation-harness/pull/2349
* Super little tiny fix doc by @fzyzcjy in https://github.com/EleutherAI/lm-evaluation-harness/pull/2546
* [API] left truncate for generate_until by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2554
* Update Lightning import by @maanug-nv in https://github.com/EleutherAI/lm-evaluation-harness/pull/2549
* add optimum-intel ipex model by @yao-matrix in https://github.com/EleutherAI/lm-evaluation-harness/pull/2566
* add warning to readme by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2568
* Adding new subtask to SCORE tasks: non greedy robustness by @rimashahbazyan in https://github.com/EleutherAI/lm-evaluation-harness/pull/2558
* batch `loglikelihood_rolling` across requests by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2559
* fix `DeprecationWarning: invalid escape sequence '\s'` for whitespace filter by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2560
* increment version to 4.6.7 by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2574

## New Contributors
* @rimashahbazyan made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2452
* @naiarapm made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2531
* @dtrawins made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2307
* @sstrehlk made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2349
* @fzyzcjy made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2546
* @maanug-nv made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2549
* @yao-matrix made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2566

**Full Changelog**: https://github.com/EleutherAI/lm-evaluation-harness/compare/v0.4.6...v0.4.7

## v0.4.8 (2025-03-05)

# lm-eval v0.4.8 Release Notes

## Key Improvements

* **New Backend Support**: 
  * Added SGLang as new evaluation backend! by @Monstertail
  * Enabled model steering with vector support via `sparsify` or `sae_lens` by @luciaquirke and @AMindToThink 

* **Breaking Change**: Python 3.8 support has been dropped as it reached end of life. Please upgrade to Python 3.9 or newer.
* **Added Support for `gen_prefix`** in config, allowing you to append text after the <|assistant|> token (or at the end of non-chat prompts) - particularly effective for evaluating instruct models

## New Benchmarks & Tasks

### Code Evaluation
* HumanEval by @hjlee1371 in #1992
* MBPP by @hjlee1371 in #2247
* HumanEval+ and MBPP+ by @bzantium in #2734

### Multilingual Expansion
* **Global Coverage**:
  * Global MMLU (Lite version by @shivalika-singh in #2567, Full version by @bzantium in #2636)
  * MLQA multilingual question answering by @KahnSvaer in #2622

* **Asian Languages**:
  * HRM8K benchmark for Korean and English by @bzantium in #2627
  * Updated KorMedMCQA to version 2.0 by @GyoukChu in #2540
  * Fixed TMLU Taiwan-specific tasks tag by @nike00811 in #2420

* **European Languages**:
  * Added Evalita-LLM benchmark by @m-resta in #2681
  * BasqueBench with Basque translations of ARC and PAWS by @naiarapm in #2732
  * Updated Turkish MMLU configuration by @ArdaYueksel in #2678

* **Middle Eastern Languages**:
  * Arabic MMLU by @bodasadallah in #2541
  * AraDICE task by @firojalam in #2507

### Ethics & Reasoning
* Moral Stories by @upunaprosk in #2653
* Histoires Morales by @upunaprosk in #2662

### Others
* MMLU Pro Plus by @asgsaeid in #2366
* GroundCocoa by @HarshKohli in #2724

We extend our thanks to all contributors who made this release possible and to our users for your continued support and feedback.

Thanks, the LM Eval Harness team (@baberabb and @lintangsutawika)

## What's Changed
* drop python 3.8 support by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2575
* Add Global MMLU Lite by @shivalika-singh in https://github.com/EleutherAI/lm-evaluation-harness/pull/2567
* add warning for truncation by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2585
* Wandb step handling bugfix and feature by @sjmielke in https://github.com/EleutherAI/lm-evaluation-harness/pull/2580
* AraDICE task config file by @firojalam in https://github.com/EleutherAI/lm-evaluation-harness/pull/2507
* fix extra_match low if batch_size > 1 by @sywangyi in https://github.com/EleutherAI/lm-evaluation-harness/pull/2595
* fix model tests by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2604
* update scrolls by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2602
* some minor logging nits by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2609
* Fix gguf loading via Transformers by @CL-ModelCloud in https://github.com/EleutherAI/lm-evaluation-harness/pull/2596
* Fix Zeno visualizer on tasks like GSM8k by @pasky in https://github.com/EleutherAI/lm-evaluation-harness/pull/2599
* Fix the format of mgsm zh and ja. by @timturing in https://github.com/EleutherAI/lm-evaluation-harness/pull/2587
* Add HumanEval by @hjlee1371 in https://github.com/EleutherAI/lm-evaluation-harness/pull/1992
* Add MBPP by @hjlee1371 in https://github.com/EleutherAI/lm-evaluation-harness/pull/2247
* Add MLQA by @KahnSvaer in https://github.com/EleutherAI/lm-evaluation-harness/pull/2622
* assistant prefill  by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2615
* fix gen_prefix by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2630
* update pre-commit by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2632
* add hrm8k benchmark for both Korean and English by @bzantium in https://github.com/EleutherAI/lm-evaluation-harness/pull/2627
* New arabicmmlu by @bodasadallah in https://github.com/EleutherAI/lm-evaluation-harness/pull/2541
* Add `global_mmlu` full version by @bzantium in https://github.com/EleutherAI/lm-evaluation-harness/pull/2636
* Update KorMedMCQA: ver 2.0 by @GyoukChu in https://github.com/EleutherAI/lm-evaluation-harness/pull/2540
* fix tmlu tmlu_taiwan_specific_tasks tag by @nike00811 in https://github.com/EleutherAI/lm-evaluation-harness/pull/2420
* fixed mmlu generative response extraction by @RawthiL in https://github.com/EleutherAI/lm-evaluation-harness/pull/2503
* revise mbpp prompt by @bzantium in https://github.com/EleutherAI/lm-evaluation-harness/pull/2645
* aggregate by group (total and categories) by @bzantium in https://github.com/EleutherAI/lm-evaluation-harness/pull/2643
* Fix max_tokens handling in vllm_vlms.py by @jkaniecki in https://github.com/EleutherAI/lm-evaluation-harness/pull/2637
* separate category for `global_mmlu` by @bzantium in https://github.com/EleutherAI/lm-evaluation-harness/pull/2652
* Add Moral Stories by @upunaprosk in https://github.com/EleutherAI/lm-evaluation-harness/pull/2653
* add TransformerLens example by @nickypro in https://github.com/EleutherAI/lm-evaluation-harness/pull/2651
* fix multiple input chat tempalte by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2576
* Add Aggregation for Kobest Benchmark by @tryumanshow in https://github.com/EleutherAI/lm-evaluation-harness/pull/2446
* update pre-commit by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2660
* remove `group` from bigbench task configs by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2663
* Add Histoires Morales task by @upunaprosk in https://github.com/EleutherAI/lm-evaluation-harness/pull/2662
* MMLU Pro Plus by @asgsaeid in https://github.com/EleutherAI/lm-evaluation-harness/pull/2366
* fix early return for multiple dict in task process_results by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2673
* Turkish mmlu Config Update by @ArdaYueksel in https://github.com/EleutherAI/lm-evaluation-harness/pull/2678
* Fix typos by @omahs in https://github.com/EleutherAI/lm-evaluation-harness/pull/2679
* remove cuda device assertion by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2680
* Adding the Evalita-LLM benchmark by @m-resta in https://github.com/EleutherAI/lm-evaluation-harness/pull/2681
* Delete lm_eval/tasks/evalita_llm/single_prompt.zip by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2687
* Update unitxt task.py to bring in line with recent repo changes by @kiersten-stokes in https://github.com/EleutherAI/lm-evaluation-harness/pull/2684
* change ensure_ascii to False for JsonChatStr by @artemorloff in https://github.com/EleutherAI/lm-evaluation-harness/pull/2691
* Set defaults for BLiMP scores by @jmichaelov in https://github.com/EleutherAI/lm-evaluation-harness/pull/2692
* Update remaining references to `assistant_prefill` in docs to `gen_prefix` by @kiersten-stokes in https://github.com/EleutherAI/lm-evaluation-harness/pull/2683
* Update README.md by @upunaprosk in https://github.com/EleutherAI/lm-evaluation-harness/pull/2694
* fix `construct_requests` kwargs in python tasks by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2700
* `arithmetic`: set target delimiter to empty string by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2701
* fix vllm by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2708
* add math_verify to some tasks by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2686
* Logging by @lintangsutawika in https://github.com/EleutherAI/lm-evaluation-harness/pull/2203
* Replace missing `lighteval/MATH-Hard` dataset with `DigitalLearningGmbH/MATH-lighteval` by @f4str in https://github.com/EleutherAI/lm-evaluation-harness/pull/2719
* remove unused import by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2728
* README updates: Added IberoBench citation info in correpsonding READMEs by @naiarapm in https://github.com/EleutherAI/lm-evaluation-harness/pull/2729
* add o3-mini support by @HelloJocelynLu in https://github.com/EleutherAI/lm-evaluation-harness/pull/2697
* add Basque translation of ARC and PAWS to BasqueBench by @naiarapm in https://github.com/EleutherAI/lm-evaluation-harness/pull/2732
* Add cocoteros_es task in spanish_bench by @sgs97ua in https://github.com/EleutherAI/lm-evaluation-harness/pull/2721
* Fix the import source for eval_logger by @kailashbuki in https://github.com/EleutherAI/lm-evaluation-harness/pull/2735
* add humaneval+ and mbpp+ by @bzantium in https://github.com/EleutherAI/lm-evaluation-harness/pull/2734
* Support SGLang as Potential Backend for Evaluation by @Monstertail in https://github.com/EleutherAI/lm-evaluation-harness/pull/2703
* fix log condition on main by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2737
* fix vllm data parallel by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2746
* [Readme change for SGLang] fix error in readme and add OOM solutions for sglang by @Monstertail in https://github.com/EleutherAI/lm-evaluation-harness/pull/2738
* Groundcocoa by @HarshKohli in https://github.com/EleutherAI/lm-evaluation-harness/pull/2724
* fix doc: generate_until only outputs the generated text! by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2755
* Enable steering HF models by @luciaquirke in https://github.com/EleutherAI/lm-evaluation-harness/pull/2749
* Add test for a simple Unitxt task by @kiersten-stokes in https://github.com/EleutherAI/lm-evaluation-harness/pull/2742
* add debug log by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2757
* increment version to 0.4.8 by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2760

## New Contributors
* @shivalika-singh made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2567
* @sjmielke made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2580
* @firojalam made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2507
* @CL-ModelCloud made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2596
* @pasky made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2599
* @timturing made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2587
* @hjlee1371 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1992
* @KahnSvaer made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2622
* @bzantium made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2627
* @bodasadallah made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2541
* @GyoukChu made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2540
* @nike00811 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2420
* @RawthiL made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2503
* @jkaniecki made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2637
* @upunaprosk made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2653
* @nickypro made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2651
* @asgsaeid made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2366
* @omahs made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2679
* @m-resta made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2681
* @f4str made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2719
* @HelloJocelynLu made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2697
* @sgs97ua made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2721
* @kailashbuki made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2735
* @Monstertail made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2703
* @HarshKohli made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2724
* @luciaquirke made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2749

**Full Changelog**: https://github.com/EleutherAI/lm-evaluation-harness/compare/v0.4.7...v0.4.8

## v0.4.9 (2025-06-19)

# lm-eval v0.4.9 Release Notes

## Key Improvements

* **Enhanced Backend Support**:
   * **SGLang Generate API** by **@baberabb** in #2997
   * **vLLM enhancements**: Added support for `enable_thinking` argument (#2947) and data parallel for V1 (#3011) by **@anmarques** and **@baberabb**
   * **Chat template improvements**: Extended vLLM chat template support (#2902) and fixed HF chat template resolution (#2992) by **@anmarques** and **@fxmarty-amd**

* **Multimodal Capabilities**:
   * **Audio modality support** for Qwen2 Audio models by **@artemorloff** in #2689
   * **Image processing improvements**: Added resize images support (#2958) and enabled multimodal API usage (#2981) by **@artemorloff** and **@baberabb**
   * **ChartQA** multimodal task implementation by **@baberabb** in #2544

* **Performance & Reliability**:
   * **Quantization support** added via `quantization_config` by **@jerryzh168** in #2842
   * **Memory optimization**: Use `yaml.CLoader` for faster YAML loading by **@giuliolovisotto** in #2777
   * **Bug fixes**: Resolved MMLU generative metric aggregation (#2761) and context length handling issues (#2972)

## New Benchmarks & Tasks

### **Code Evaluation**
* **HumanEval Instruct** - Instruction-following code generation benchmark by **@baberabb** in #2650
* **MBPP Instruct** - Instruction-based Python programming evaluation by **@baberabb** in #2995

### **Language Modeling**
* **C4 Dataset Support** - Added perplexity evaluation on C4 web crawl dataset by **@Zephyr271828** in #2889

### **Long Context Benchmarks**
* **RULER and Longbench** - Long-context evaluation suites added by **@baberabb** in #2629

### **Mathematical & Reasoning**
* **GSM8K Platinum** - Enhanced mathematical reasoning benchmark by **@Qubitium** in #2771
* **MastermindEval** - Logic reasoning evaluation by **@whoisjones** in #2788
* **JSONSchemaBench** - Structured output evaluation by **@Saibo-creator** in #2865

### **Llama Reference Implementations**
* **Llama Reference Implementations** - Added task variants for Multilingual MMLU, MMLU CoT, GSM8K, and ARC Challenge based on Llama evaluation standards by **@anmarques** in #2797, #2826, #2829

### **Multilingual Expansion**

**Asian Languages**:
* **Korean MMLU (KMMLU)** multiple-choice task by **@Aprilistic** in #2849
* **MMLU-ProX** extended evaluation by **@heli-qi** in #2811
* **KBL 2025 Dataset** - Updated Korean benchmark evaluation by **@abzb1** in #3000

**European Languages**:
* **NorEval** - Comprehensive Norwegian benchmark by **@vmkhlv** in #2919

**African Languages**:
* **AfroBench** - Multi-African language evaluation by **@JessicaOjo** in #2825
* **Darija tasks** - Moroccan dialect benchmarks (DarijaMMLU, DarijaHellaSwag, Darija_Bench) by **@hadi-abdine** in #2521

**Arabic Languages**:
* **Arab Culture** task for cultural understanding by **@bodasadallah** in #3006

### **Domain-Specific Benchmarks**
* **CareQA** - Healthcare evaluation benchmark by **@PabloAgustin** in #2714
* **ACPBench & ACPBench Hard** - Automated code generation evaluation by **@harshakokel** in #2807, #2980
* **INCLUDE tasks** - Inclusivity evaluation suite by **@agromanou** in #2769
* **Cocoteros VA** dataset by **@sgs97ua** in #2787

### **Social & Bias Evaluation**
* **Various social bias tasks** for fairness assessment by **@oskarvanderwal** in #1185

## Technical Enhancements

* **Fine-grained evaluation**: Added `--examples` argument for efficient multi-prompt evaluation by **@felipemaiapolo** and **@mirianfsilva** in #2520
* **Improved tokenization**: Better handling of `add_bos_token` initialization by **@baberabb** in #2781
* **Memory management**: Enhanced softmax computations with `softmax_dtype` argument for `HFLM` by **@Avelina9X** in #2921

## Critical Bug Fixes

* **Collating Queries Fix** - Resolved error with different continuation lengths that was causing evaluation failures by **@ameyagodbole** in #2987
* **Mutual Information Metric** - Fixed acc_mutual_info calculation bug that affected metric accuracy by **@baberabb** in #3035

## Breaking Changes & Important Updates

* **MMLU dataset migration**: Switched to `cais/mmlu` dataset source by **@baberabb** in #2918
* **Default parameter updates**: Increased `max_gen_toks` to 2048 and `max_length` to 8192 for MMLU Pro tests by **@dazipe** in #2824
* **Temperature defaults**: Set default temperature to 0.0 for vLLM and SGLang backends by **@baberabb** in #2819

We extend our heartfelt thanks to all contributors who made this release possible, including **43 first-time contributors** who brought fresh perspectives and valuable improvements to the evaluation harness.

## What's Changed
* fix mmlu (generative) metric aggregation by @wangcho2k in https://github.com/EleutherAI/lm-evaluation-harness/pull/2761
* Bugfix by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2762
* fix verbosity typo by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2765
* docs: Fix typos in README.md by @ruivieira in https://github.com/EleutherAI/lm-evaluation-harness/pull/2778
* initialize tokenizer with `add_bos_token` by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2781
* improvement: Use yaml.CLoader to load yaml files when available. by @giuliolovisotto in https://github.com/EleutherAI/lm-evaluation-harness/pull/2777
* Consistency Fix: Filter new leaderboard_math_hard dataset to "Level 5" only  by @perlitz in https://github.com/EleutherAI/lm-evaluation-harness/pull/2773
* Fix for mc2 calculation by @kdymkiewicz in https://github.com/EleutherAI/lm-evaluation-harness/pull/2768
* New healthcare benchmark: careqa by @PabloAgustin in https://github.com/EleutherAI/lm-evaluation-harness/pull/2714
* Capture gen_kwargs from CLI in squad_completion by @ksurya in https://github.com/EleutherAI/lm-evaluation-harness/pull/2727
* humaneval instruct by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2650
* Update evaluator.py by @zhuzeyuan in https://github.com/EleutherAI/lm-evaluation-harness/pull/2786
* change piqa dataset path (uses parquet rather than dataset script) by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2790
* use verify_certificate flag in batch requests by @daniel-salib in https://github.com/EleutherAI/lm-evaluation-harness/pull/2785
* add audio modality (qwen2 audio only) by @artemorloff in https://github.com/EleutherAI/lm-evaluation-harness/pull/2689
* Add various social bias tasks by @oskarvanderwal in https://github.com/EleutherAI/lm-evaluation-harness/pull/1185
* update pre-commit by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2799
* Update Legacy OpenLLM leaderboard to use "train" split for ARC fewshot by @Avelina9X in https://github.com/EleutherAI/lm-evaluation-harness/pull/2802
* Add INCLUDE tasks by @agromanou in https://github.com/EleutherAI/lm-evaluation-harness/pull/2769
* Add support for token-based auth for watsonx models by @kiersten-stokes in https://github.com/EleutherAI/lm-evaluation-harness/pull/2796
* add __version__ by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2808
* Add cocoteros_va dataset by @sgs97ua in https://github.com/EleutherAI/lm-evaluation-harness/pull/2787
* Add MastermindEval by @whoisjones in https://github.com/EleutherAI/lm-evaluation-harness/pull/2788
* Add loncxt tasks by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2629
* [hf-multimodal] pass kwargs to self.processor by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2667
* [MM] Chartqa by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2544
* Allow writing config to wandb by @ksurya in https://github.com/EleutherAI/lm-evaluation-harness/pull/2736
* [change] group -> tag on afrimgsm, afrimmlu, afrixnli dataset by @jd730 in https://github.com/EleutherAI/lm-evaluation-harness/pull/2813
* Clean up README and pyproject.toml by @kiersten-stokes in https://github.com/EleutherAI/lm-evaluation-harness/pull/2814
* Llama3 mmlu correction by @anmarques in https://github.com/EleutherAI/lm-evaluation-harness/pull/2797
* Add Markdown linter by @kiersten-stokes in https://github.com/EleutherAI/lm-evaluation-harness/pull/2818
* Configure the pad tokens for Qwen when using vLLM by @zhangruoxu in https://github.com/EleutherAI/lm-evaluation-harness/pull/2810
* fix typo in humaneval by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2820
* default temp=0.0 for vllm and slang by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2819
* Fixes to mmlu_pro_llama by @anmarques in https://github.com/EleutherAI/lm-evaluation-harness/pull/2816
* Add MMLU-ProX task by @heli-qi in https://github.com/EleutherAI/lm-evaluation-harness/pull/2811
* Quick fix for mmlu_pro_llama by @anmarques in https://github.com/EleutherAI/lm-evaluation-harness/pull/2827
* Fix: tj-actions/changed-files is compromised by @Tautorn in https://github.com/EleutherAI/lm-evaluation-harness/pull/2828
* Multilingual MMLU for Llama instruct models by @anmarques in https://github.com/EleutherAI/lm-evaluation-harness/pull/2826
* bbh - changed dataset to parquet version by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2845
* Fix typo in longbench metrics by @djwackey in https://github.com/EleutherAI/lm-evaluation-harness/pull/2854
* Add kmmlu multiple-choice(accuracy) task #2848 by @Aprilistic in https://github.com/EleutherAI/lm-evaluation-harness/pull/2849
* Adding ACPBench task by @harshakokel in https://github.com/EleutherAI/lm-evaluation-harness/pull/2807
* add Darija (Moroccan dialects) tasks including darijammlu. darijahellaswag and darija_bench by @hadi-abdine in https://github.com/EleutherAI/lm-evaluation-harness/pull/2521
* Increase default max_gen_toks to 2048 and max_length to 8192 for MMLU Pro tests by @dazipe in https://github.com/EleutherAI/lm-evaluation-harness/pull/2824
* doc by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2857
* Fix: ACPBench Link by @harshakokel in https://github.com/EleutherAI/lm-evaluation-harness/pull/2860
* Adds MMLU CoT, gsm8k and arc_challenge for llama instruct by @anmarques in https://github.com/EleutherAI/lm-evaluation-harness/pull/2829
* [leaderboard] math - sync with repo by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2817
* Update supported models by @danielholanda in https://github.com/EleutherAI/lm-evaluation-harness/pull/2866
* Add JSONSchemaBench: A Benchmark for Evaluating Structured Output from LLMs by @Saibo-creator in https://github.com/EleutherAI/lm-evaluation-harness/pull/2865
* leaderboard - add subtask scores by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2867
* Fix the deps of longbench from jeiba to jieba by @houseroad in https://github.com/EleutherAI/lm-evaluation-harness/pull/2873
* Optimization for evalita-llm rouge computation by @m-resta in https://github.com/EleutherAI/lm-evaluation-harness/pull/2878
* Update authentications methods, add support for deployment_id for IBM watsonx_ai by @Medokins in https://github.com/EleutherAI/lm-evaluation-harness/pull/2877
* Add GSM8K Platinum by @Qubitium in https://github.com/EleutherAI/lm-evaluation-harness/pull/2771
* Add `--examples` Argument for Fine-Grained Task Evaluation in `lm-evaluation-harness`. This feature is the first step towards efficient multi-prompt evaluation with PromptEval [1,2] by @felipemaiapolo in https://github.com/EleutherAI/lm-evaluation-harness/pull/2520
* Extend support for chat template in vLLM by @anmarques in https://github.com/EleutherAI/lm-evaluation-harness/pull/2902
* tasks README: fix dead link by @dtrifiro in https://github.com/EleutherAI/lm-evaluation-harness/pull/2899
* Add support for quantization_config by @jerryzh168 in https://github.com/EleutherAI/lm-evaluation-harness/pull/2842
* Fix a typo in README for tasks by @eldarkurtic in https://github.com/EleutherAI/lm-evaluation-harness/pull/2910
* fix resolve_hf_chat_template version by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2917
* mmlu - switch dataset to cais/mmlu; fix tests by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2918
* init pixels before tokenizer creation by @artemorloff in https://github.com/EleutherAI/lm-evaluation-harness/pull/2911
* Longbench bugfix by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2895
* Added softmax_dtype argument to HFLM to coerce log_softmax computations by @Avelina9X in https://github.com/EleutherAI/lm-evaluation-harness/pull/2921
* [bbh] use np.nan for numpy > 2.0 by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2937
* Add support for enable_thinking argument in vllm model by @anmarques in https://github.com/EleutherAI/lm-evaluation-harness/pull/2947
* Added NorEval, a novel Norwegian benchmark by @vmkhlv in https://github.com/EleutherAI/lm-evaluation-harness/pull/2919
* Fix import error for eval_logger in score utils by @annafontanaa in https://github.com/EleutherAI/lm-evaluation-harness/pull/2940
* Include all test files in sdist by @booxter in https://github.com/EleutherAI/lm-evaluation-harness/pull/2634
* Change citation name by @StellaAthena in https://github.com/EleutherAI/lm-evaluation-harness/pull/2956
* [vllm] add warning on truncation by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2962
* fix: type error while checking context length by @llsj14 in https://github.com/EleutherAI/lm-evaluation-harness/pull/2972
* Fix import error for deepcopy by @kiersten-stokes in https://github.com/EleutherAI/lm-evaluation-harness/pull/2969
* Pin unitxt to most recent minor version to avoid test failures by @kiersten-stokes in https://github.com/EleutherAI/lm-evaluation-harness/pull/2970
* mmlu pro generation_kwargs until Q: -> Question: by @yoonniverse in https://github.com/EleutherAI/lm-evaluation-harness/pull/2945
* AfroBench: How Good are Large Language Models on African Languages? by @JessicaOjo in https://github.com/EleutherAI/lm-evaluation-harness/pull/2825
* Added C4 Support by @Zephyr271828 in https://github.com/EleutherAI/lm-evaluation-harness/pull/2889
* Fixed a bug that in MMLU-Pro utils.py that throw index error if one choice was removed by @sleepingcat4 in https://github.com/EleutherAI/lm-evaluation-harness/pull/2870
* Add question suffix before the <|assistant|> tag by @TingchenFu in https://github.com/EleutherAI/lm-evaluation-harness/pull/2876
* Add device arg to model_args passed to LLM object in VLLM model class by @momentino in https://github.com/EleutherAI/lm-evaluation-harness/pull/2879
* paws-x fix formatting by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2759
* Delete scripts/cost_estimate.py by @StellaAthena in https://github.com/EleutherAI/lm-evaluation-harness/pull/2985
* Adding ACPBench Hard tasks by @harshakokel in https://github.com/EleutherAI/lm-evaluation-harness/pull/2980
* [SGLANG] Add the SGLANG generate API by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2997
* fix example notebook by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2998
* Log tokenized request warning only once by @RobGeada in https://github.com/EleutherAI/lm-evaluation-harness/pull/3002
* [Add Dataset Update] KBL 2025 by @abzb1 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3000
* Output path fix by @Niccolo-Ajroldi in https://github.com/EleutherAI/lm-evaluation-harness/pull/2993
* use images with api models by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2981
* Adding resize images support by @artemorloff in https://github.com/EleutherAI/lm-evaluation-harness/pull/2958
* Revert "feat: add question suffix (#2876)" by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3007
* [hotfix] modify multimodal check in evaluate by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3013
* [Fix] Update `resolve_hf_chat_template` arguments by @fxmarty-amd in https://github.com/EleutherAI/lm-evaluation-harness/pull/2992
* Fix error due in Collating queries with different continuation lengths (fixes #2984) by @ameyagodbole in https://github.com/EleutherAI/lm-evaluation-harness/pull/2987
* [vllm] data parallel for V1 by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3011
* add arab_culture task by @bodasadallah in https://github.com/EleutherAI/lm-evaluation-harness/pull/3006
* chore: clean up and extend .gitignore rules by @e1washere in https://github.com/EleutherAI/lm-evaluation-harness/pull/3030
* Enable text-only evals for VLM models by @ysulsky in https://github.com/EleutherAI/lm-evaluation-harness/pull/2999
* [Fix] acc_mutual_info metric calculation bug by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3035
* Fix: fix vllm issue with DP>1 by @younesbelkada in https://github.com/EleutherAI/lm-evaluation-harness/pull/3025
* add Mbpp instruct by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2995
* remove prints by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3041
* [longbench] fix metric calculation by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/2983
* Fallback to super implementation in `fewshot_context` for Unitxt tasks by @kiersten-stokes in https://github.com/EleutherAI/lm-evaluation-harness/pull/3023
* Fix Typo in README and Comment in utils_mcq.py by @vtjl10 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3057
* fix longbech citation by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3061
* mmlu task: update README.md by @annafontanaa in https://github.com/EleutherAI/lm-evaluation-harness/pull/3070
* Fix typos in docstrings in instructions.py by @maximevtush in https://github.com/EleutherAI/lm-evaluation-harness/pull/3060
* bump version to `0.4.9` by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3073

## New Contributors
* @wangcho2k made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2761
* @ruivieira made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2778
* @perlitz made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2773
* @kdymkiewicz made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2768
* @PabloAgustin made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2714
* @ksurya made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2727
* @zhuzeyuan made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2786
* @daniel-salib made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2785
* @oskarvanderwal made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/1185
* @Avelina9X made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2802
* @agromanou made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2769
* @whoisjones made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2788
* @jd730 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2813
* @anmarques made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2797
* @zhangruoxu made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2810
* @heli-qi made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2811
* @Tautorn made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2828
* @djwackey made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2854
* @Aprilistic made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2849
* @harshakokel made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2807
* @hadi-abdine made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2521
* @dazipe made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2824
* @danielholanda made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2866
* @Saibo-creator made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2865
* @houseroad made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2873
* @felipemaiapolo made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2520
* @dtrifiro made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2899
* @jerryzh168 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2842
* @vmkhlv made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2919
* @annafontanaa made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2940
* @booxter made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2634
* @llsj14 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2972
* @yoonniverse made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2945
* @Zephyr271828 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2889
* @sleepingcat4 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2870
* @TingchenFu made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2876
* @momentino made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2879
* @abzb1 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3000
* @Niccolo-Ajroldi made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2993
* @fxmarty-amd made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2992
* @ameyagodbole made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2987
* @e1washere made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3030
* @ysulsky made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2999
* @younesbelkada made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3025
* @vtjl10 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3057
* @maximevtush made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3060

**Full Changelog**: https://github.com/EleutherAI/lm-evaluation-harness/compare/v0.4.8...v0.4.9

## v0.4.9.1 (2025-08-04)

# lm-eval v0.4.9.1 Release Notes

This v0.4.9.1 release is a quick patch to bring in some new tasks and fixes. Looking aheas, we're gearing up for some bigger updates to tackle common community pain points. We'll do our best to keep things from breaking, but we anticipate a few changes might not be fully backward-compatible. We're excited to share more soon!

### Enhanced Reasoning Model Handling
* Better support for reasoning models with a `think_end_token` argument to strip intermediate reasoning from outputs for the `hf`, `vllm`, and `sglang` model backends. A related `enable_thinking` argument was also added for specific models that support it (e.g., Qwen).

## New Benchmarks & Tasks
* EgyMMLU and EgyHellaSwag by @houdaipha in https://github.com/EleutherAI/lm-evaluation-harness/pull/3063
* MultiBLiMP benchmark by @jmichaelov in https://github.com/EleutherAI/lm-evaluation-harness/pull/3155
* LIBRA benchmark for long-context evaluation by @karimovaSvetlana in https://github.com/EleutherAI/lm-evaluation-harness/pull/2943
* Multilingual Truthfulqa in Spanish, Basque and Galician by @BlancaCalvo in https://github.com/EleutherAI/lm-evaluation-harness/pull/3062

## Fixes & Improvements
### Tasks & Benchmarks:
* Aligned Humaneval results for Llama-3.1-70B-Instruct with official scores by @userljz, @baberabb, @idantene in (https://github.com/EleutherAI/lm-evaluation-harness/pull/3201. [#3092](https://github.com/EleutherAI/lm-evaluation-harness/pull/3092), [#3102](https://github.com/EleutherAI/lm-evaluation-harness/pull/3102))
* Fixed incorrect dataset paths for GLUE and medical benchmarks by @Avelina9X and @idantene. ([#3159](https://github.com/EleutherAI/lm-evaluation-harness/pull/3159), [#3151](https://github.com/EleutherAI/lm-evaluation-harness/pull/3151))
* Removed redundant "Let's think step by step" text from `bbh_cot_fewshot` prompts by @philipdoldo. ([#3140](https://github.com/EleutherAI/lm-evaluation-harness/pull/3140))
* Increased `max_gen_toks` to 2048 for HRM8K math benchmarks by @shing100. ([#3124](https://github.com/EleutherAI/lm-evaluation-harness/pull/3124))

### Backend & Stability:
* Reduce CLI loading time from 2.2s to 0.05s by @stakodiak. ([#3099](https://github.com/EleutherAI/lm-evaluation-harness/pull/3099))
* Fixed a process hang caused by mp.Pool in bootstrap_stderr and introduced `DISABLE_MULTIPROC` envar by @ankitgola005 and @neel04. ([#3135](https://github.com/EleutherAI/lm-evaluation-harness/pull/3135), [#3106](https://github.com/EleutherAI/lm-evaluation-harness/pull/3106))
* add image hashing and `LMEVAL_HASHMM` envar by @artemorloff in https://github.com/EleutherAI/lm-evaluation-harness/pull/2973
* TaskManager: `include-path` precedence handling to prioritize custom dir over default by @parkhs21 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3068

## Housekeeping:
* Pinned `datasets < 4.0.0` temporarily to maintain compatibility with `trust_remote_code` by @baberabb. ([#3172](https://github.com/EleutherAI/lm-evaluation-harness/pull/3172))
* Removed models from Neural Magic and other unneeded files by @baberabb. ([#3112](https://github.com/EleutherAI/lm-evaluation-harness/pull/3112), [#3113](https://github.com/EleutherAI/lm-evaluation-harness/pull/3113), [#3108](https://github.com/EleutherAI/lm-evaluation-harness/pull/3108))

## What's Changed
* llama3 task: update README.md by @annafontanaa in https://github.com/EleutherAI/lm-evaluation-harness/pull/3074
* Fix Anthropic API compatibility issues in chat completions by @NourFahmy in https://github.com/EleutherAI/lm-evaluation-harness/pull/3054
* Ensure backwards compatibility in `fewshot_context` by using kwargs by @kiersten-stokes in https://github.com/EleutherAI/lm-evaluation-harness/pull/3079
* [vllm] remove system message if `TemplateError` for chat_template by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3076
* feat / fix: Properly make use of `subfolder` from HF models by @younesbelkada in https://github.com/EleutherAI/lm-evaluation-harness/pull/3072
* [HF] fix quantization config by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3039
* FixBug: Align the Humaneval with official results for Llama-3.1-70B-Instruct by @userljz in https://github.com/EleutherAI/lm-evaluation-harness/pull/3092
* Truthfulqa multi harness by @BlancaCalvo in https://github.com/EleutherAI/lm-evaluation-harness/pull/3062
* Fix: Reduce CLI loading time from 2.2s to 0.05s by @stakodiak in https://github.com/EleutherAI/lm-evaluation-harness/pull/3099
* Humaneval - fix regression by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3102
* Bugfix/hf tokenizer gguf override by @ankush13r in https://github.com/EleutherAI/lm-evaluation-harness/pull/3098
* [FIX] Initial code to disable multi-proc for stderr by @neel04 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3106
* fix deps; update hooks by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3107
* delete unneeded files by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3108
* Fixed #3005: Processes both formats of model_args: string and dictionay by @DebjyotiRay in https://github.com/EleutherAI/lm-evaluation-harness/pull/3097
* add image hashing and `LMEVAL_HASHMM` envar by @artemorloff in https://github.com/EleutherAI/lm-evaluation-harness/pull/2973
* removal of Neural Magic models by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3112
* Neuralmagic by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3113
* check pil dep when hashing images by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3114
* warning for "chat" pretrained; disable buggy evalita configs by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3127
* fix: remove warning by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3128
* Adding EgyMMLU and EgyHellaSwag by @houdaipha in https://github.com/EleutherAI/lm-evaluation-harness/pull/3063
* Added mixed_precision_dtype argument to HFLM to enable autocasting by @Avelina9X in https://github.com/EleutherAI/lm-evaluation-harness/pull/3138
* Fix for hang due to mp.Pool in bootstrap_stderr by @ankitgola005 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3135
* when using vllm with lora, it will have some mistakes, now i fix it. by @Jacky-MYQ in https://github.com/EleutherAI/lm-evaluation-harness/pull/3132
* truncate thinking tags in generations by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3145
* `bbh_cot_fewshot`: Removed repeated "Let''s think step by step." text from bbh cot prompts by @philipdoldo in https://github.com/EleutherAI/lm-evaluation-harness/pull/3140
* Fix medical benchmarks import by @idantene in https://github.com/EleutherAI/lm-evaluation-harness/pull/3151
* fix request hanging when request api by @mmmans in https://github.com/EleutherAI/lm-evaluation-harness/pull/3090
* Custom request headers |  trust_remote_code param fix by @RawthiL in https://github.com/EleutherAI/lm-evaluation-harness/pull/3069
* Bugfix: update path for GLUE by @Avelina9X in https://github.com/EleutherAI/lm-evaluation-harness/pull/3159
* Add the MultiBLiMP benchmark by @jmichaelov in https://github.com/EleutherAI/lm-evaluation-harness/pull/3155
* multiblimp - readme by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3162
* [tests] Added missing fixture in test_unitxt_tasks.py by @Avelina9X in https://github.com/EleutherAI/lm-evaluation-harness/pull/3163
* Fix: extended to max_gen_toks 2048 for HRM8K math benchmarks by @shing100 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3124
* feat: Add LIBRA benchmark for long-context evaluation by @karimovaSvetlana in https://github.com/EleutherAI/lm-evaluation-harness/pull/2943
* Added `chat_template_args` to vllm by @Avelina9X in https://github.com/EleutherAI/lm-evaluation-harness/pull/3164
* Pin datasets < 4.0.0 by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3172
* Remove "device" from vllm_causallms.py by @mgoin in https://github.com/EleutherAI/lm-evaluation-harness/pull/3176
* remove trust-remote-code in configs; fix escape sequences by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3180
* Fix vllm test issue that call pop() from None by @weireweire in https://github.com/EleutherAI/lm-evaluation-harness/pull/3182
* [hotfix] vllm: pop `device` from kwargs by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3181
* Update vLLM compatibility by @DarkLight1337 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3024
* Fix ```mmlu_continuation``` subgroup names to fit Readme and other variants by @lamalunderscore in https://github.com/EleutherAI/lm-evaluation-harness/pull/3137
* Fix humaneval_instruct by @idantene in https://github.com/EleutherAI/lm-evaluation-harness/pull/3201
* Update README.md for mlqa by @newme616 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3117
* improve include-path precedence handling by @parkhs21 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3068
* Bump version to 0.4.9.1 by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3208

## New Contributors
* @NourFahmy made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3054
* @userljz made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3092
* @BlancaCalvo made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3062
* @stakodiak made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3099
* @ankush13r made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3098
* @neel04 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3106
* @DebjyotiRay made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3097
* @houdaipha made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3063
* @ankitgola005 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3135
* @Jacky-MYQ made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3132
* @philipdoldo made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3140
* @idantene made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3151
* @mmmans made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3090
* @shing100 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3124
* @karimovaSvetlana made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2943
* @weireweire made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3182
* @DarkLight1337 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3024
* @lamalunderscore made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3137
* @newme616 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3117
* @parkhs21 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3068

**Full Changelog**: https://github.com/EleutherAI/lm-evaluation-harness/compare/v0.4.9...v0.4.9.1

## v0.4.9.2 (2025-11-26)

This release continues our steady stream of community contributions with a batch of new benchmarks, expanded model support, and important fixes. A notable change: **Python 3.10 is now the minimum required version**.

### New Benchmarks & Tasks

A big wave of new evaluation tasks this release:

* **AIME** and **MATH500** math reasoning benchmarks by @jannalulu in #3248, #3311
* **BabiLong** and **Longbench v2** for long-context evaluation by @jannalulu in #3287, #3338
* **GraphWalks** by @jannalulu in #3377
* **ZhoBLiMP**, **BLiMP-NL**, **TurBLiMP**, **LM-SynEval**, and **BHS** linguistic benchmarks by @jmichaelov in #3218, #3221, #3219, #3184, #3265
* **Icelandic WinoGrande** by @jmichaelov in #3277
* **CLIcK** Korean benchmark by @shing100 in #3173
* **MMLU-Redux** (generative) and Spanish translation by @luiscosio in #2705
* **EsBBQ** and **CaBBQ** bias benchmarks by @valleruizf in #3167
* **EQBench** in Spanish and Catalan by @priverabsc in #3168
* **Anthropic discrim-eval** by @Helw150 in #3091
* **XNLI-VA** by @FranValero97 in #3194
* **Bangla MMLU** (Titulm) by @Ismail-Hossain-1 in #3317
* **HumanEval infilling** by @its-alpesh in #3299
* **CNN-DailyMail 3.0.0** by @preordinary in #3426
* **Global PIQA** and new `acc_norm_bytes` metric by @baberabb in #3368

### Fixes & Improvements

**Core Changes:**
* **Python 3.10 minimum** by @jannalulu in #3337
* **Unpinned `datasets`** library by @baberabb in #3316
* **BOS token handling**: Delegate to tokenizer; `add_bos_token` now defaults to `None` by @baberabb in #3347
* Renamed `LOGLEVEL` env var to `LMEVAL_LOG_LEVEL` to avoid conflicts by @fxmarty-amd in #3418
* Resolve duplicate task names with safeguards by @giuliolovisotto in #3394

**Task Fixes:**
* Fixed MMLU-Redux to exclude samples without `error_type="ok"` and display summary table by @fxmarty-amd in #3410, #3406
* Fixed AIME answer extraction by @jannalulu in #3353
* Fixed LongBench evaluation and group handling by @TimurAysin, @jannalulu in #3273, #3359, #3361
* Fixed `crows_pairs` dataset by @jannalulu in #3378
* Fixed Gemma tokenizer `add_bos_token` not updating by @DarkLight1337 in #3206
* Fixed `lambada_multilingual_stablelm` by @jmichaelov, @HallerPatrick in #3294, #3222
* Fixed CodeXGLUE by @gsaltintas in #3238
* Pinned correct MMLUSR version by @christinaexyou in #3350
* Updated `minerva_math` by @baberabb in #3259

**Backend Fixes:**
* Fixed vLLM import errors when not installed by @fxmarty-amd in #3292
* Fixed vLLM `data_parallel_size>1` issue by @Dornavineeth in #3303
* Resolved deprecated `vllm.utils.get_open_port` by @DarkLight1337 in #3398
* Fixed GPT series model bugs by @zinccat in #3348
* Fixed PIL image hashing to use actual bytes by @tboerstad in #3331
* Fixed `additional_config` parsing by @brian-dellabetta in #3393
* Fixed batch chunking seed handling with groupby by @slimfrkha in #3047
* Fixed no-output error handling by @Oseltamivir in #3395
* Replaced deprecated `torch_dtype` with `dtype` by @AbdulmalikDS in #3415
* Fixed custom task config reading by @SkyR0ver in #3425

### Model & Backend Support

* **OpenAI GPT-5** support by @babyplutokurt in #3247
* **Azure OpenAI** support by @zinccat in #3349
* **Fine-tuned Gemma3** evaluation support by @LearnerSXH in #3234
* **OpenVINO text2text** models by @nikita-savelyevv in #3101
* **Intel XPU** support for HFLM by @kaixuanliu in #3211
* **Attention head steering** support by @luciaquirke in #3279
* Leverage vLLM's `tokenizer_info` endpoint to avoid manual duplication by @m-misiura in #3185

## What's Changed
* Remove `trust_remote_code: True` from updated datasets by @Avelina9X in https://github.com/EleutherAI/lm-evaluation-harness/pull/3213
* Add support for evaluating with fine-tuned Gemma3 by @LearnerSXH in https://github.com/EleutherAI/lm-evaluation-harness/pull/3234
* Fix `add_bos_token` not updated for Gemma tokenizer by @DarkLight1337 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3206
* remove incomplete compilation instructions, solves #3233 by @ceferisbarov in https://github.com/EleutherAI/lm-evaluation-harness/pull/3242
* Update utils.py by @Anri-Lombard in https://github.com/EleutherAI/lm-evaluation-harness/pull/3246
* Adding support for OpenAI GPT-5 model by @babyplutokurt in https://github.com/EleutherAI/lm-evaluation-harness/pull/3247
* Add xnli_va dataset by @FranValero97 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3194
* Add ZhoBLiMP benchmark by @jmichaelov in https://github.com/EleutherAI/lm-evaluation-harness/pull/3218
* Add BLiMP-NL by @jmichaelov in https://github.com/EleutherAI/lm-evaluation-harness/pull/3221
* Add TurBLiMP by @jmichaelov in https://github.com/EleutherAI/lm-evaluation-harness/pull/3219
* Add LM-SynEval Benchmark by @jmichaelov in https://github.com/EleutherAI/lm-evaluation-harness/pull/3184
* Fix unknown group key to tag in yaml config for `lambada_multilingual_stablelm` by @HallerPatrick in https://github.com/EleutherAI/lm-evaluation-harness/pull/3222
* update `minerva_math` by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3259
* feat: Add CLIcK task by @shing100 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3173
* Adds Anthropic/discrim-eval to lm-evaluation-harness by @Helw150 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3091
* Add support for OpenVINO text2text generation models  by @nikita-savelyevv in https://github.com/EleutherAI/lm-evaluation-harness/pull/3101
* Update MMLU-ProX task by @weihao1115 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3174
* Support for AIME dataset by @jannalulu in https://github.com/EleutherAI/lm-evaluation-harness/pull/3248
* feat(scrolls): delete chat_template from kwargs by @slimfrkha in https://github.com/EleutherAI/lm-evaluation-harness/pull/3267
* pacify pre-commit by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3268
* Fix codexglue by @gsaltintas in https://github.com/EleutherAI/lm-evaluation-harness/pull/3238
* Add BHS benchmark by @jmichaelov in https://github.com/EleutherAI/lm-evaluation-harness/pull/3265
* Add `acc_norm` metric to BLiMP-NL by @jmichaelov in https://github.com/EleutherAI/lm-evaluation-harness/pull/3272
* Add `acc_norm` metric to ZhoBLiMP by @jmichaelov in https://github.com/EleutherAI/lm-evaluation-harness/pull/3271
* Add EsBBQ and CaBBQ tasks by @valleruizf in https://github.com/EleutherAI/lm-evaluation-harness/pull/3167
* Add support for steering individual attention heads by @luciaquirke in https://github.com/EleutherAI/lm-evaluation-harness/pull/3279
* Add the Icelandic WinoGrande benchmark by @jmichaelov in https://github.com/EleutherAI/lm-evaluation-harness/pull/3277
* Ignore seed when splitting batch in chunks with groupby by @slimfrkha in https://github.com/EleutherAI/lm-evaluation-harness/pull/3047
* [fix][vllm] Avoid import errors in case vllm is not installed by @fxmarty-amd in https://github.com/EleutherAI/lm-evaluation-harness/pull/3292
* Fix LongBench Evaluation by @TimurAysin in https://github.com/EleutherAI/lm-evaluation-harness/pull/3273
* add intel xpu support for HFLM by @kaixuanliu in https://github.com/EleutherAI/lm-evaluation-harness/pull/3211
* feat: Add mmlu-redux and it's spanish transaltion as generative task definitions by @luiscosio in https://github.com/EleutherAI/lm-evaluation-harness/pull/2705
* Add BabiLong by @jannalulu in https://github.com/EleutherAI/lm-evaluation-harness/pull/3287
* Add AIME to task description by @jannalulu in https://github.com/EleutherAI/lm-evaluation-harness/pull/3296
* Add humaneval_infilling task by @its-alpesh in https://github.com/EleutherAI/lm-evaluation-harness/pull/3299
* Add eqbench tasks in Spanish and Catalan by @priverabsc in https://github.com/EleutherAI/lm-evaluation-harness/pull/3168
* [fix] add math and longbench to test dependencies by @jannalulu in https://github.com/EleutherAI/lm-evaluation-harness/pull/3321
* Fix: VLLM model when data_parallel_size>1 by @Dornavineeth in https://github.com/EleutherAI/lm-evaluation-harness/pull/3303
* unpin datasets; update pre-commit by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3316
* bump to python 3.10 by @jannalulu in https://github.com/EleutherAI/lm-evaluation-harness/pull/3337
* Longbench v2 by @jannalulu in https://github.com/EleutherAI/lm-evaluation-harness/pull/3338
* Leverage vllm's `tokenizer_info` endpoint to avoid manual duplication  by @m-misiura in https://github.com/EleutherAI/lm-evaluation-harness/pull/3185
* Add support for Titulm Bangla MMLU dataset by @Ismail-Hossain-1 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3317
* remove duplicate tags/groups by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3343
* Align `humaneval_64_instruct` task label in README to name in yaml file by @jmichaelov in https://github.com/EleutherAI/lm-evaluation-harness/pull/3344
* Fixes bugs when using gpt series model by @zinccat in https://github.com/EleutherAI/lm-evaluation-harness/pull/3348
* [fix] aime doesn't extract answers by @jannalulu in https://github.com/EleutherAI/lm-evaluation-harness/pull/3353
* add global_piqa; add acc_norm_bytes metric by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3368
* [fix] crows_pairs dataset by @jannalulu in https://github.com/EleutherAI/lm-evaluation-harness/pull/3378
* Fix issue 3355 assertion error by @marksverdhei in https://github.com/EleutherAI/lm-evaluation-harness/pull/3356
* fix(gsm8k): align README to yaml file by @neoheartbeats in https://github.com/EleutherAI/lm-evaluation-harness/pull/3388
* added azure openai support by @zinccat in https://github.com/EleutherAI/lm-evaluation-harness/pull/3349
* Delegate BOS to the tokenizer; `add_bos_token` defaults to `None` by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3347
* fix trust_remote_code=True for longbench by @jannalulu in https://github.com/EleutherAI/lm-evaluation-harness/pull/3361
* [feat] add graphwalks by @jannalulu in https://github.com/EleutherAI/lm-evaluation-harness/pull/3377
* Longbench group fix by @jannalulu in https://github.com/EleutherAI/lm-evaluation-harness/pull/3359
* Resolve deprecation of `vllm.utils.get_open_port` by @DarkLight1337 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3398
* Trim whitespace in remove_whitespace filter by @ziqing-huang in https://github.com/EleutherAI/lm-evaluation-harness/pull/3408
* Fixes #3391 avoid error on no-output by @Oseltamivir in https://github.com/EleutherAI/lm-evaluation-harness/pull/3395
* Fix PIL image hashing to use actual bytes instead of object repr by @tboerstad in https://github.com/EleutherAI/lm-evaluation-harness/pull/3331
* [MMLU redux] Do not use samples which do not have `error_type="ok"` by @fxmarty-amd in https://github.com/EleutherAI/lm-evaluation-harness/pull/3410
* fix: resolve duplicate task names and add safeguards. by @giuliolovisotto in https://github.com/EleutherAI/lm-evaluation-harness/pull/3394
* Add MATH500 by @jannalulu in https://github.com/EleutherAI/lm-evaluation-harness/pull/3311
* [bugfix] additional_config parsing by @brian-dellabetta in https://github.com/EleutherAI/lm-evaluation-harness/pull/3393
* fix(tasks):pin correct MMLUSR version by @christinaexyou in https://github.com/EleutherAI/lm-evaluation-harness/pull/3350
* Fix `lambada_multilingual_stablelm` by @jmichaelov in https://github.com/EleutherAI/lm-evaluation-harness/pull/3294
* Fix descriptions in the Moral Stories and Histoires Morales tasks. by @upunaprosk in https://github.com/EleutherAI/lm-evaluation-harness/pull/3374
* Replace deprecated torch_dtype parameter with dtype by @AbdulmalikDS in https://github.com/EleutherAI/lm-evaluation-harness/pull/3415
* [fix] Fix mmlu_redux not displaying summary table + display to the user the tasks / yaml that are actually pulled by @fxmarty-amd in https://github.com/EleutherAI/lm-evaluation-harness/pull/3406
* Rename the conflicting environment variable `LOGLEVEL` to `LMEVAL_LOG_LEVEL` by @fxmarty-amd in https://github.com/EleutherAI/lm-evaluation-harness/pull/3418
* Update SGLang installation and documentation links by @Bobchenyx in https://github.com/EleutherAI/lm-evaluation-harness/pull/3422
* Fix reading custom task configs by @SkyR0ver in https://github.com/EleutherAI/lm-evaluation-harness/pull/3425
* New Task: Add CNN-DailyMail (3.0.0) by @preordinary in https://github.com/EleutherAI/lm-evaluation-harness/pull/3426

## New Contributors
* @LearnerSXH made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3234
* @ceferisbarov made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3242
* @Anri-Lombard made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3246
* @babyplutokurt made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3247
* @FranValero97 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3194
* @HallerPatrick made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3222
* @Helw150 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3091
* @nikita-savelyevv made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3101
* @weihao1115 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3174
* @jannalulu made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3248
* @slimfrkha made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3267
* @gsaltintas made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3238
* @valleruizf made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3167
* @TimurAysin made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3273
* @kaixuanliu made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3211
* @its-alpesh made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3299
* @priverabsc made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3168
* @Dornavineeth made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3303
* @m-misiura made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3185
* @Ismail-Hossain-1 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3317
* @zinccat made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3348
* @marksverdhei made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3356
* @neoheartbeats made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3388
* @ziqing-huang made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3408
* @Oseltamivir made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3395
* @tboerstad made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3331
* @brian-dellabetta made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3393
* @christinaexyou made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3350
* @AbdulmalikDS made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3415
* @Bobchenyx made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3422
* @SkyR0ver made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3425
* @preordinary made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3426

**Full Changelog**: https://github.com/EleutherAI/lm-evaluation-harness/compare/v0.4.9.1...v0.4.9.2

## v0.4.10 (2026-01-27)

## Highlights

The big change this release: the base package no longer installs model backends by default. We've also added new benchmarks and expanded multilingual support.

### Breaking Change: Lightweight Core with Optional Backends

**`pip install lm_eval` no longer installs the HuggingFace/torch stack by default.** (#3428)

The core package no longer includes backends. Install them explicitly:

```bash
pip install lm_eval          # core only, no model backends
pip install lm_eval[hf]      # HuggingFace backend (transformers, torch, accelerate)
pip install lm_eval[vllm]    # vLLM backend
pip install lm_eval[api]     # API backends (OpenAI, Anthropic, etc.)
```

**Additional breaking change:** Accessing model classes via attribute no longer works:

```python
# This still works:
from lm_eval.models.huggingface import HFLM

# This now raises AttributeError:
import lm_eval.models
lm_eval.models.huggingface.HFLM
```

### CLI Refactor

The CLI now uses explicit subcommands and supports YAML config files (#3440):

```bash
lm-eval run --model hf --tasks hellaswag      # run evaluations
lm-eval run --config my_config.yaml           # load args from YAML config
lm-eval ls tasks                               # list available tasks
lm-eval validate --tasks hellaswag,arc_easy   # validate task configs
```

Backward compatible when omitting `run` still works: `lm-eval --model hf --tasks hellaswag`

See `lm-eval --help` or the [CLI documentation](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/interface.md) for details.

### Other Improvements

* **Decoupled `ContextSampler`** with new `build_qa_turn` helper (#3429)
* **Normalized `gen_kwargs`** with `truncation_side` support for vLLM (#3509)

## New Benchmarks & Tasks

* **PISA** task by @HallerPatrick in #3412
* **SLR-Bench** (Scalable Logical Reasoning Benchmark) by @Ahmad21Omar in #3305
* **OpenAI Multilingual MMLU** by @Helw150 in #3473
* **ULQA** benchmark by @keramjan in #3340
* **IFEval** in Spanish and Catalan by @juliafalcao in #3467
* **TruthfulQA-VA** for Catalan by @sgs97ua in #3469
* **Multiple Bangla benchmarks** by @Ismail-Hossain-1 in #3454
* **NeurIPS E2LM Competition submissions**: Team Shaikespear, Morai, and Noor by @younesbelkada in #3437, #3443, #3444

## Model Support

* **Ministral-3** adapter (`hf-mistral3`) by @medhakimbedhief in #3487

## Fixes & Improvements

### Task Fixes

* Fixed leading whitespace leakage in **MMLU-Pro** by @baberabb in #3500
* Fixed `gen_prefix` delimiter handling in multiple-choice tasks by @baberabb in #3508
* Fixed MGSM stop criteria in Iberian languages by @juliafalcao in #3465
* Fixed `a=0` as valid answer index in `build_qa_turn` by @ezylopx5 in #3488
* Fixed `fewshot_config` not being applied to fewshot docs by @baberabb in #3461
* Updated GSM8K, WinoGrande, and SuperGLUE to use full HF dataset paths by @baberabb in #3523, #3525, #3527
* Fixed `gsm8k_cot_llama` `target_delimiter` issue by @baberabb in #3526
* Updated LIBRA task utils by @bond005 in #3520

### Backend Fixes

* Fixed vLLM off-by-one `max_length` error by @baberabb in #3503
* Resolved deprecated `vllm.transformers_utils.get_tokenizer` import by @DarkLight1337 in #3482
* Fixed SGLang import and removed duplicate tasks by @baberabb in #3492
* Removed deprecated `AutoModelForVision2Seq` by @baberabb in #3522
* Fixed Anthropic chat model mapping by @lucafossen in #3453
* Fixed bug preventing `=` sign in checkpoint names by @mrinaldi97 in #3517
* Fixed `pretty_print_task` for external custom configs by @safikhanSoofiyani in #3436
* Fixed CLI regressions by @fxmarty-amd in #3449

## New Contributors
* @safikhanSoofiyani made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3436
* @lucafossen made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3453
* @Ahmad21Omar made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3305
* @ezylopx5 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3488
* @juliafalcao made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3467
* @medhakimbedhief made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3487
* @ntenenz made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3489
* @keramjan made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3340
* @bond005 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3520
* @mrinaldi97 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3517
* @wogns3623 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3523

**Full Changelog**: https://github.com/EleutherAI/lm-evaluation-harness/compare/v0.4.9.2...v0.4.10

## v0.4.11 (2026-02-13)

## v0.4.11 Release Notes

Minor release. Stay tuned for bigger changes next release.

### New Platform Support

* **Windows ML Backend** — Native Windows ML inference support by @chapsiru and @chemwolf6922 in #3470, #3564, #3565

### New Benchmarks & Tasks

* **BEAR** knowledge probe by @plonerma in #3496

### Task Version Changes

> The following tasks have updated versions. Results from a previous task versions may not be directly comparable. See the linked PRs or individual task READMEs for changelogs.

`afrobench_belebele` (all variants): 2 → 3 in #3551
`evalita_llm`: 0.0 → 0.1 in #3551
`include` (all 90 language variants): 0.0 → 0.1 in #3551
`mgsm_direct` (all 11 language variants): 3.0 → 4.0 by @LakshyaChaudhry in #3574

### Fixes & Improvements

* Fixed **SQuAD v2** evaluation by @HydrogenSulfate in #3535
* Fixed **MasakhaNEWS** tasks — replaced non-existent `headline_text` field with `headline` by @Mr-Neutr0n in #3567
* Fixed incorrect task configs by @baberabb in #3552
* Replaced `eval()` with `ast.literal_eval` in task configs for safer parsing by @baberabb in #3577
* Fixed **SGLang** duplicate registration error by @enpimashin in #3543
* Restored **`hf_transfer`** import check by @baberabb in #3563
* Fixed `modify_gen_kwargs` call in **vLLM VLMs** by @hmellor in #3573
* Refactored **vLLM** `gen_kwargs` normalization inline to `modify_gen_kwargs`; fixed cached `gen_kwargs` mutation by @baberabb in #3582
* Fixed README for task-listing CLI command by @UltimateJupiter in #3545
* Updated dependencies by @baberabb in #3546

## New Contributors
* @HydrogenSulfate made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3535
* @UltimateJupiter made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3545
* @enpimashin made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3543
* @chapsiru made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3470
* @chemwolf6922 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3565
* @plonerma made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3496
* @hmellor made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3573
* @Mr-Neutr0n made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3567
* @LakshyaChaudhry made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3574

**Full Changelog**: https://github.com/EleutherAI/lm-evaluation-harness/compare/v0.4.10...v0.4.11

## v0.4.12 (2026-05-11)

New release with four new model backends, tensor parallel support for `transformers` based models (`hf`), new benchmarks, a `TaskManager` refactor, and a long tail of task correctness fixes.

## Highlights

### New Model Backends

* **TensorRT-LLM (`trt-llm`)** — NVIDIA TensorRT-LLM backend for optimized GPU inference by @Tracin in #3628
* **Megatron-LM (`megatron-lm`)** — Megatron-LM backend with TP/EP/DP support by @shangxiaokang in #3521 (with follow-up hardening in #3607)
* **Intel Gaudi** — Gaudi support via `optimum-habana` by @12010486 in #3550
* **LiteLLM AI gateway (`litellm`)** — Use LiteLLM as a unified API gateway for 100+ providers by @RheagalFire in #3721
* **Native Tensor Parallelism for HF backend** — multi-GPU TP for `transformers` models via `tp_plan` by @YangKai0616 in #3692

### `TaskManager` Refactor (#3549)

* `TaskManager.load(...)` returns a flat `{tasks, groups}` dict instead of the legacy nested `{ConfigurableGroup: {name: Task}}`. `evaluate()` accepts both shapes; `load_task_or_group(...)` and `get_task_dict(...)` are deprecated shims that return the old shape.
* New `Group` class directly holds its child tasks; `ConfigurableGroup` is now a deprecated wrapper around it.
* Duplicate task/group configs within the same root are skipped with a log message instead of silently overwritten. (Custom `include_path` entries still override defaults.)

### Breaking Changes

* **`SteeredHF` renamed to `SteeredModel`** — update imports if you're using the steering backend by @adrian-sauter in #3592
* **vLLM minimum bumped to `>=0.18`** as part of the data-parallel-with-Ray fixes by @baberabb in #3725
* **`enable_thinking` is now disallowed for `multiple_choice` / loglikelihood tasks**, and `think_end_token` is now required when `enable_thinking=True`. Configurations that combined these previously failed silently by @fxmarty-amd in #3675

### New Logger

* **Trackio logger** with per-sample `Trace` logging by @abidlabs in #3733

## New Benchmarks & Tasks

* **InfiniteBench** — long-context evaluation beyond 100K tokens (12 sub-tasks: code debug/run, KV retrieval, longbook QA/summarization, math find, passkey, etc.) by @siddhant-rajhans in #3662
* **CRUXEval** — Python code reasoning benchmark with input/output prediction variants (incl. CoT and pass@k variants) by @ThomasHeap in #3699
* **Toksuite** — multilingual tokenization-robustness benchmark (Chinese, English, and more) by @gsaltintas in #3669
* **NEREL-bench** — Russian named-entity / relation-extraction benchmark by @bond005 in #3650
* **JFinQA** — Japanese Financial Numerical Reasoning QA (1000 questions, with consistency / numerical / temporal splits) by @ajtgjmdjp in #3570

## Fixes & Improvements

### Task Fixes

* Fixed **GPQA** preprocessing regex that corrupted answer text containing brackets by @Robby955 in #3691 and @Chessing234 in #3735
* Fixed **MMLU-Pro** and **MMLU-Pro-Plus** few-shot answers leaking into the user role under chat templates by @kiwaku in #3693, #3747
* Fixed **RACE** `doc_to_text` keeping a blank marker and dropping the question body by @Chessing234 in #3716
* Fixed **BigBench** multiple-choice tasks crashing on mixed-format examples (filtered out free-form examples) by @Chessing234 in #3702
* Fixed **HeadQA** `doc_to_decontamination_query` pointing at a nonexistent `query` field by @Chessing234 in #3718
* Fixed **french_bench_topic_based_nli** `doc_to_decontamination_query` pointing at nonexistent `texte` field by @Chessing234 in #3719
* Fixed **TruthfulQA-gen** `dataset_path` by @zhngstl in #3723
* Fixed **NorEval/NorIdiom** `!function` imports to use absolute module paths by @Anai-Guo in #3731
* Fixed **IFEval** `RephraseChecker.strip_changes` greedy-regex bug by @Chessing234 in #3737
* Fixed correctness issues in **Arabic** normalization and prompt loading by @RinZ27 in #3589
* Updated **BLiMP** dataset path by @jmichaelov in #3596
* Replaced all references to the `CohereForAI` org with `CohereLabs` by @juliafalcao in #3631


## What's Changed
* refactor(Taskmanager)! by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3549
* fix(cli): `--cache_requests` always fails due to argparse `type`/`choices` conflict by @maxidl in https://github.com/EleutherAI/lm-evaluation-harness/pull/3588
* feat: Add Megatron-LM backend with TP/EP/DP support by @shangxiaokang in https://github.com/EleutherAI/lm-evaluation-harness/pull/3521
* Fix: #3293 (pybass UnboundLocalError on outputs in Exception Logging) by @lucafossen in https://github.com/EleutherAI/lm-evaluation-harness/pull/3601
* [fix] Add missing tokenization progress bar by @fxmarty-amd in https://github.com/EleutherAI/lm-evaluation-harness/pull/3605
* fix: improve model_args type coercion in handle_arg_string by @ManasVardhan in https://github.com/EleutherAI/lm-evaluation-harness/pull/3608
* fix: harden Megatron GPT layer spec setup for eval by @shangxiaokang in https://github.com/EleutherAI/lm-evaluation-harness/pull/3607
* Update vLLM import of `resolve_hf_chat_template` by @DarkLight1337 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3595
* Add docstring for HFLM __init__ keyword arguments by @joshuaswanson in https://github.com/EleutherAI/lm-evaluation-harness/pull/3630
* Update all mentions of the `CohereForAI` organization to `CohereLabs` by @juliafalcao in https://github.com/EleutherAI/lm-evaluation-harness/pull/3631
* Skip caching None responses in async generation path by @joshuaswanson in https://github.com/EleutherAI/lm-evaluation-harness/pull/3633
* Fix correctness issues in Arabic normalization and prompt loading by @RinZ27 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3589
* fix(evaluate tests) by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3634
* fix: propagate custom aggregation to dict-valued metric result keys by @s-zx in https://github.com/EleutherAI/lm-evaluation-harness/pull/3626
* chore(ci-updates) by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3635
* Update BLiMP dataset path by @jmichaelov in https://github.com/EleutherAI/lm-evaluation-harness/pull/3596
* Add jfinqa: Japanese Financial Numerical Reasoning QA (1000 questions) by @ajtgjmdjp in https://github.com/EleutherAI/lm-evaluation-harness/pull/3570
* Rename SteeredHF to SteeredModel in lm_eval/models/__init__.py by @adrian-sauter in https://github.com/EleutherAI/lm-evaluation-harness/pull/3592
* fix: Update `WatsonxLLM` class mapping and errors by @Rafal-Chrzanowski-IBM in https://github.com/EleutherAI/lm-evaluation-harness/pull/3591
* Add Intel Gaudi support by @12010486 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3550
* [fix] Disallow  `enable_thinking` with `output_type: multiple_choice` tasks / loglikelihood tasks; raise error in case `think_end_token` is not provided with `enable_thinking=True` by @fxmarty-amd in https://github.com/EleutherAI/lm-evaluation-harness/pull/3675
* fix(vllm): fix dp with ray. remove mp distribution; pin vllm >=0.18 by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3725
* refactor(utils): fix mistral tokenizer error; improve doc-strings by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3728
* fix(vllm): fix vllm tokenizer for Mistral; rm default `gpu_memory_utilization=0.9` by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3732
* Fix GPQA preprocess stripping mathematical bracket expressions by @Chessing234 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3735
* Guard vLLM tok_encode against prefix_token_id being None by @Chessing234 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3724
* fix(ifeval): use non-greedy regex in RephraseChecker.strip_changes by @Chessing234 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3737
* fix: bound request cache filename length by @princepal9120 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3729
* fix codeowners by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3738
* Fix dataset_path for truthfulqa_gen by @zhngstl in https://github.com/EleutherAI/lm-evaluation-harness/pull/3723
* fix(vllm): disallow data_parallel with enable_expert_parallel by @FazeelUsmani in https://github.com/EleutherAI/lm-evaluation-harness/pull/3734
* Add Trackio logger with per-sample Trace logging by @abidlabs in https://github.com/EleutherAI/lm-evaluation-harness/pull/3733
* Fix headqa doc_to_decontamination_query pointing at nonexistent 'query' field by @Chessing234 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3718
* Fix french_bench_topic_based_nli doc_to_decontamination_query pointing at nonexistent 'texte' field by @Chessing234 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3719
* fix(noreval/noridiom): use absolute module paths for !function imports (#3624) by @Anai-Guo in https://github.com/EleutherAI/lm-evaluation-harness/pull/3731
* Fix DummyLM.generate_until printing context as gen_kwargs by @Chessing234 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3711
* Fix MultiChoiceRegexFilter.find_match IndexError on all-empty capture groups by @Chessing234 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3708
* fix(model_comparator): fix ImportError from scipy.stats.norm import by @Chessing234 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3742
* Fix zeno_visualize discarding tasks intersection result by @Chessing234 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3739
* fix: don't pass task stop sequences to vLLM for reasoning models by @jwmacd in https://github.com/EleutherAI/lm-evaluation-harness/pull/3700
* feat: Add  [ LiteLLM AI gateway ] as model backend by @RheagalFire in https://github.com/EleutherAI/lm-evaluation-harness/pull/3721
* Fix RACE doc_to_text keeping blank marker and dropping the question body by @Chessing234 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3716
* Fix BigBench multiple-choice crash on mixed-format tasks by @Chessing234 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3702
* Fix GPQA preprocessing: remove bracket-stripping regex that corrupts answer text by @Robby955 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3691
* Fix mmlu_pro fewshot answers leaking into user role under chat template by @kiwaku in https://github.com/EleutherAI/lm-evaluation-harness/pull/3693
* fix(mmlu_pro_plus): sync fixes from `mmlu_pro` by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3747
* chore: cleap up deps; fix ci lint by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3748
* Fix DummyLM.generate_until write_out printing context as gen_kwargs by @Chessing234 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3714
* Fix median aggregation returning arbitrary element instead of median by @Chessing234 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3696
* fix(api): chat payload leaking top-level text type by @felixmr1 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3745
* [BUGFIX] Consistent handling of None answers and cache by @RawthiL in https://github.com/EleutherAI/lm-evaluation-harness/pull/3656
* Adding Cruxeval by @ThomasHeap in https://github.com/EleutherAI/lm-evaluation-harness/pull/3699
* [Task] NEREL-bench by @bond005 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3650
* Added Toksuite Benchmark by @gsaltintas in https://github.com/EleutherAI/lm-evaluation-harness/pull/3669
* Add InfiniteBench: long-context evaluation beyond 100K tokens by @siddhant-rajhans in https://github.com/EleutherAI/lm-evaluation-harness/pull/3662
* fix: Reset batch_sizes cache before each _loglikelihood_tokens call by @nevertmr in https://github.com/EleutherAI/lm-evaluation-harness/pull/3654
* feat: add TRT-LLM backend. by @Tracin in https://github.com/EleutherAI/lm-evaluation-harness/pull/3628
* [Feat] Add native Tensor Parallelism support for HF backend by @YangKai0616 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3692
* feat(release): 0.4.12 by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3763

## New Contributors
* @maxidl made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3588
* @shangxiaokang made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3521
* @ManasVardhan made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3608
* @joshuaswanson made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3630
* @RinZ27 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3589
* @s-zx made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3626
* @ajtgjmdjp made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3570
* @adrian-sauter made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3592
* @Rafal-Chrzanowski-IBM made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3591
* @12010486 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3550
* @Chessing234 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3735
* @princepal9120 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3729
* @zhngstl made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3723
* @FazeelUsmani made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3734
* @abidlabs made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3733
* @Anai-Guo made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3731
* @jwmacd made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3700
* @RheagalFire made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3721
* @Robby955 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3691
* @kiwaku made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3693
* @felixmr1 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3745
* @ThomasHeap made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3699
* @siddhant-rajhans made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3662
* @nevertmr made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3654
* @Tracin made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3628
* @YangKai0616 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3692

**Full Changelog**: https://github.com/EleutherAI/lm-evaluation-harness/compare/v0.4.11...v0.4.12

## v0.4.13 (2026-08-31)

## v0.4.13 Release Notes

A fix-focused release. The main fixes are for few-shot leakage, a multiple-choice filter bug, and group stderr, alongside two new ONNX backends and eight new benchmark suites. Also updated most configs for datasets>=4, which accounts for much of the diff by volume.

## Highlights

### Bug Fixes

Fixes that may shift previously reported numbers:

* **Eval documents leaked into few-shot prompts.** The sampler could draw the document under test into its own demonstrations by @SiavashShams in #3978, and `gen_prefix` was resolved against the eval doc rather than the few-shot doc — splicing the evaluated question into every shot for RULER `niah_single_1`, `humaneval_instruct`, and `humaneval_64_instruct` by @adityasingh2400 in #3979
* **`MultiChoiceRegexFilter` prefix-shadowing.** Regex alternation is leftmost-wins, so a choice that prefixed a longer choice (`"Guilty"` vs `"Guilty of Romance"`) matched inside it and scored correct answers as wrong — visible on BBH `movie_recommendation` by @iamsharduld in #3884
* **Group stderr with `weight_by_size: false`.** Groups reported the size-weighted pooled stderr even when the point estimate was an unweighted mean, giving error bars up to ~3x too narrow. Only unequal-sized subtasks change by @iamsharduld in #3882
* **`minerva_math` answer normalization.** `sqrt` shorthand no longer corrupts indexed roots (#4037), the thousands-separator strip no longer fuses digit tuples (`0,1` → `01`, #4039), an answer identical to the gold now scores correct (#4034), and the few-shot prompt LaTeX is corrected (#4045) by @feiiiiii5 and @nata2627. `putnam_axiom` shares these helpers and picks up the same fixes.

### New Model Backends

* **`onnxruntime`** — raw onnxruntime backend for Model Builder ONNX exports by @amd-sourjya in #3984
* **`onnxruntime-genai`** — cross-platform ONNX Runtime GenAI backend, with `winml` refactored on top of it by @thiagocrepaldi in #3960
* **Megatron-LM v0.18** compatibility by @oberpierre in #3991

Install with `pip install lm_eval[onnxruntime]` or `lm_eval[onnxruntime-genai]`. For non-CPU execution providers install the matching wheel instead — `onnxruntime-gpu` / `onnxruntime-rocm`, or `onnxruntime-genai-cuda` / `onnxruntime-genai-directml` — these are mutually exclusive.

## New Tasks

* **LongProc** — long-context procedural reasoning, 6 task types across 16 configs by @xiye17 in #3544
* **Uncheatable Eval** — contamination-resistant evaluation: rolling log-likelihood over recently-published documents from Wikipedia, GitHub, BBC News, arXiv, bioRxiv, and AO3, as 15 category tasks plus a size-weighted group by @ziqing-huang in #3442
* **TyDiQA Gold Passage** — 9-language multilingual QA by @bongho in #4044
* **LegalBench** — new suite, 19 tasks: the HELM-lite LegalBench subset (5 tasks, #3860) and the Contract NLI suite (14 NDA entailment tasks, #3954) by @bongho
* **IndicParam** — MCQ benchmark covering 12 low-resource Indic languages by @hjoshifonteva in #3826
* **IndicXNLI Gujarati** (`indicxnli_gu`) by @bhaumik611 in #4056
* **GreekMMLU** — official native-sourced configuration by @mersinkonomi in #3581
* **Physics GRE** — InflectionAI multiple-choice physics benchmark by @bongho in #3853
* **Putnam Axiom** — competition-level mathematical reasoning by @baberabb in #3998
* **Portuguese Bench** — ASSIN2 RTE and STS by @bongho in #3812
* **Catalanbench** — cieaCOVA (#4043) and Terretaqa (#3784) by @baberabb and @ivanmartinezmurillo
* **MLQA** — a tag to run all variants at once by @ivanbaldo in #2977

## Task Changes

### Correctness & Prompts

* **global_piqa** restructured into parallel/non-parallel × cloze/generation variants; the `global_piqa_completions` and `global_piqa_prompted` groups are now `global_piqa_cloze` and `global_piqa_generation` by @baberabb in #3816
* **IrokoBench** — repaired `afrimmlu` / `afrimgsm` / `afrixnli` task registration by @discobot in #3841, fixed the broken `afrisenti` / `mafand` prompt_2 group references by @DaoyuanLi2816 in #3847, and switched `afrixnli` prompt_1 `doc_to_text` to Jinja braces by @Solaris-star in #3944
* **KorMedMCQA** — answer-choice extraction now follows the paper's Appendix B by @discobot in #3842
* **JSONSchema Bench** — per-sample validation timeout so a pathological schema no longer hangs the whole eval by @hancheolcho in #3923
* **RULER** — every task crashed with `TypeError: unhashable type: 'dict'` before inference when the tokenizer arrived as anything but a plain string (e.g. under `local-chat-completions`); the name is now resolved before the cached lookup by @nata2627 in #4048
* **NIAH** — no longer loops forever when `max_seq_lengths < 4096` by @vnayakde in #3372
* **LongBench** — `code_sim_score` skips a blank leading line before extraction by @cameronshinn in #3921
* **FDA / SWDE / SQuAD_completion** — whitespace stripped from input and target by @EphraiemSarabamoun in #3795
* **med_prescriptions** — requires both keys before combining complaints and diagnosis by @Anai-Guo in #4041
* **HumanEval** — `humaneval_random_span_infilling_light` was registered under the wrong task name, causing a `KeyError` by @jaydeepborkar in #3768
* **INCLUDE** — stray space removed from North Macedonian task identifiers by @DaoyuanLi2816 in #3848
* **DarijaBench** — `trasnlation` typo corrected in translation task names by @DaoyuanLi2816 in #3824
* **Unitxt** — `dataset_kwargs` is now passed through (#3230) and `init` sets the task name (#3225) by @mprahl
* **`format_span` filter** — normalizes labels only, leaving entity text untouched by @k-dickinson in #3887
* **ContextSampler** — no longer crashes when the few-shot pool contains duplicate eval-doc rows by @Kymi808 in #3790
* **`fewshot_config.split`** — a nested `fewshot_config.split` now takes precedence over the inherited top-level `fewshot_split`, as documented by @chuenchen309 in #3937

## Model Backends & APIs

* Chat completions now support `think_end_token` by @yaodong-shen in #3959
* `auto:N` batch size is parsed correctly in API models by @AbdullahRasheed45 in #3970, and `batch_size="auto"` no longer raises on the neuronx backend by @AbdullahRasheed45 in #3971
* Synchronous API requests honor the configured timeout by @SiavashShams in #3995
* Anthropic stop sequences are kept non-empty by @he-yufeng in #3822
* HF: `max_length` is detected from a nested `text_config` (Gemma3 multimodal) by @OrionArchitekton in #3916, `max_cpu_memory` is passed through to accelerate's `max_memory` by @Anai-Guo in #4016, and tokenizers that decode to an empty string fall back to `tokenizer.eos_token` by @ganeshr10 in #3657
* vLLM warns when it ignores the `device` argument by @Apeironics in #3803; sglang argument passing fixed by @wm901115nwpu in #3817

## Core, CLI & Config

* `--metadata` accepts `key=value` pairs in addition to JSON by @baberabb in #4054
* `--use_cache` keys are hashable for multimodal image/byte requests by @feiiiiii5 in #4040
* Cache parent directories are created when missing by @sdivyanshu90 in #4047; `delete_cache` is a no-op when the directory is absent by @feiiiiii5 in #4035
* A local directory sharing a task's name no longer shadows the registered task by @nloughl in #3670
* Function resolving works for custom tasks by @SkyR0ver in #3992; string dictionary arguments parse correctly by @tandede in #4020
* A scalar `seed` from a config file is normalized the same way the CLI does by @winklemad in #4003
* Sample counts no longer depend on metric ordering by @arthi-arumugam-git in #4068
* `scripts/requests_caching.py` entrypoint repaired — bad kwargs and a helper defined after its use by @Anai-Guo in #4059
* **chrF++** aggregation and metric (`word_order=2`) by @KrishVenky in #3780; TER metric direction corrected and the chrF docstring fixed by @borgr in #3993
* All numpy scalar types serialize to JSON, not just `int64`/`int32`, by @iamsharduld in #3885

## Migration Notes

* **Few-shot prompts changed** for tasks using a document-specific `gen_prefix` (RULER `niah_single_1`, `humaneval_instruct`, `humaneval_64_instruct`) and anywhere the sampler previously drew the eval document into its own shots. Prior numbers on those tasks may not be comparable.
* **`minerva_math` and `leaderboard_math_*` now diverge.** `lm_eval/tasks/leaderboard/math/utils.py` is deliberately frozen to reproduce Open LLM Leaderboard v2 scoring; the normalization fixes landed in `minerva_math` only.
* **`global_piqa` task names changed** — see Task Changes above.
* **If you pinned `datasets<4`** to keep script-based tasks working, you can unpin. Out-of-tree task YAMLs pointing at script-based datasets still need the same treatment.
* **`winml` now sits on top of `onnxruntime-genai`** and pulls in that extra.

<details>

<summary><h2>What's Changed</h2></summary>

* feat: 0.4.13.dev0 by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3764
* update global piqa by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3816
* fix for keyerror while running humaneval_infilling  by @jaydeepborkar in https://github.com/EleutherAI/lm-evaluation-harness/pull/3768
* fix: strip whitespace from input/target for FDA, SWDE, and SQuAD_completion tasks by @EphraiemSarabamoun in https://github.com/EleutherAI/lm-evaluation-harness/pull/3795
* Fix "trasnlation" typo in DarijaBench translation task names by @DaoyuanLi2816 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3824
* fix(ruler): replace defunct hotpot dataset host with pinned HF mirror by @Anai-Guo in https://github.com/EleutherAI/lm-evaluation-harness/pull/3806
* fix: keep Anthropic stop sequences nonempty by @he-yufeng in https://github.com/EleutherAI/lm-evaluation-harness/pull/3822
* fix(vllm): warn when device argument is ignored by @Apeironics in https://github.com/EleutherAI/lm-evaluation-harness/pull/3803
* fix sglang args by @wm901115nwpu in https://github.com/EleutherAI/lm-evaluation-harness/pull/3817
* feat(legalbench): add HELM-lite LegalBench subset (5 tasks) by @bongho in https://github.com/EleutherAI/lm-evaluation-harness/pull/3860
* Fix space in North Macedonian task identifiers (INCLUDE suite) by @DaoyuanLi2816 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3848
* fix(kormedmcqa): extract answer choice per paper Appendix B by @discobot in https://github.com/EleutherAI/lm-evaluation-harness/pull/3842
* Fix dataset paths for xnli, xcopa, paws-x, and xquad by @Chessing234 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3870
* Add IndicParam: MCQ benchmark for 12 low-resource Indic languages by @hjoshifonteva in https://github.com/EleutherAI/lm-evaluation-harness/pull/3826
* feat(portuguese_bench): add ASSIN2 RTE and STS tasks by @bongho in https://github.com/EleutherAI/lm-evaluation-harness/pull/3812
* fix(prost): load PROST without the removed dataset script by @ayaangazali in https://github.com/EleutherAI/lm-evaluation-harness/pull/3977
* fix(spanish_bench): load wnli_es without the removed dataset script by @ayaangazali in https://github.com/EleutherAI/lm-evaluation-harness/pull/3982
* fix(tests): pass dataset_kwargs in test_download by @ayaangazali in https://github.com/EleutherAI/lm-evaluation-harness/pull/3980
* fix(tasks): use namespaced dataset path for wsc273 by @ayaangazali in https://github.com/EleutherAI/lm-evaluation-harness/pull/3946
* fix(tasks): use namespaced dataset paths for webqs, medmcqa, and wmt16 by @ayaangazali in https://github.com/EleutherAI/lm-evaluation-harness/pull/3942
* fix(arithmetic): load arithmetic tasks without the removed dataset script by @ayaangazali in https://github.com/EleutherAI/lm-evaluation-harness/pull/3976
* fix(mmlusr): restore dataset loading for all 171 MMLU-SR tasks by @ayaangazali in https://github.com/EleutherAI/lm-evaluation-harness/pull/3972
* fix(scrolls): load SCROLLS without the removed dataset script by @ayaangazali in https://github.com/EleutherAI/lm-evaluation-harness/pull/3975
* fix(tasks): use script-less parquet mirrors for mathqa, siqa, and moral_stories by @shubhangithub in https://github.com/EleutherAI/lm-evaluation-harness/pull/3943
* fix(tmmluplus): use ikala/tmmluplus so the task loads on datasets>=4 by @gowtham-sai-yadav in https://github.com/EleutherAI/lm-evaluation-harness/pull/3950
* Fix broken afrobench group task references (afrisenti/mafand prompt_2) by @DaoyuanLi2816 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3847
* fix(longbench): skip blank leading line in code_sim_score extraction by @cameronshinn in https://github.com/EleutherAI/lm-evaluation-harness/pull/3921
* fix(afrixnli): use Jinja braces in prompt_1 doc_to_text by @Solaris-star in https://github.com/EleutherAI/lm-evaluation-harness/pull/3944
* fix(jsonschema_bench): add per-sample validation timeout to prevent eval hangs by @hancheolcho in https://github.com/EleutherAI/lm-evaluation-harness/pull/3923
* Fix fewshot_config.split precedence in TaskConfig by @chuenchen309 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3937
* Exclude eval docs from first-n few-shot samples by @SiavashShams in https://github.com/EleutherAI/lm-evaluation-harness/pull/3978
* fix: prevent ValueError when batch_size="auto" is passed to neuronx model by @AbdullahRasheed45 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3971
* fix: prevent ValueError when batch_size="auto:N" is passed to API models by @AbdullahRasheed45 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3970
* fix: resolve fewshot gen_prefix against the fewshot doc, not the eval doc by @adityasingh2400 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3979
* Putnam Axiom by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3998
* feat(legalbench): add Contract NLI suite (14 NDA entailment tasks) by @bongho in https://github.com/EleutherAI/lm-evaluation-harness/pull/3954
* Fix `megatron_lm` backend against Megatron-LM `core_v0.18+`: argument parsing moved out of `initialize_megatron()` by @oberpierre in https://github.com/EleutherAI/lm-evaluation-harness/pull/3991
* chore(ci): update pre-commit hooks and workflow packages by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/4023
* fix(hf): pass max_cpu_memory through to accelerate's max_memory by @Anai-Guo in https://github.com/EleutherAI/lm-evaluation-harness/pull/4016
* chore(megatron): run linter by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/4024
* fix(huggingface): detect max_length from nested text_config (Gemma3 multimodal) by @OrionArchitekton in https://github.com/EleutherAI/lm-evaluation-harness/pull/3916
* Honor configured timeout for synchronous API requests by @SiavashShams in https://github.com/EleutherAI/lm-evaluation-harness/pull/3995
* fix(api): support think_end_token for chat completions by @yaodong-shen in https://github.com/EleutherAI/lm-evaluation-harness/pull/3959
* feat(models): add cross-platform onnxruntime-genai backend + refactor winml by @thiagocrepaldi in https://github.com/EleutherAI/lm-evaluation-harness/pull/3960
* Enable function resolving for custom tasks by @SkyR0ver in https://github.com/EleutherAI/lm-evaluation-harness/pull/3992
* fix(config): parse dictionary strings from YAML configs by @tandede in https://github.com/EleutherAI/lm-evaluation-harness/pull/4020
* fix: normalize scalar `seed` from a config file the way the CLI does by @winklemad in https://github.com/EleutherAI/lm-evaluation-harness/pull/4003
* fix(filters): format_span only normalizes labels, not entity text by @k-dickinson in https://github.com/EleutherAI/lm-evaluation-harness/pull/3887
* fix: make delete_cache a no-op when the cache directory is absent by @feiiiiii5 in https://github.com/EleutherAI/lm-evaluation-harness/pull/4035
* Add Terretaqa task into Catalanbench by @ivanmartinezmurillo in https://github.com/EleutherAI/lm-evaluation-harness/pull/3784
* Add make_table regression coverage by @aryanputta in https://github.com/EleutherAI/lm-evaluation-harness/pull/3788
* Add cieaCOVA task into catalan bench by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/4043
* fix(irokobench): repair afrimmlu/afrimgsm/afrixnli task registration and update READMEs by @discobot in https://github.com/EleutherAI/lm-evaluation-harness/pull/3841
* fix: fall back to tokenizer.eos_token when decode returns empty string by @ganeshr10 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3657
* fix(med_prescriptions): require both keys before combining complaints and diagnosis by @Anai-Guo in https://github.com/EleutherAI/lm-evaluation-harness/pull/4041
* fix: local directory with task name no longer shadows registered task by @nloughl in https://github.com/EleutherAI/lm-evaluation-harness/pull/3670
* feat(models): add raw onnxruntime backend for Model Builder ONNX exports by @amd-sourjya in https://github.com/EleutherAI/lm-evaluation-harness/pull/3984
* Align pubmedqa task name in README with yaml by @jmichaelov in https://github.com/EleutherAI/lm-evaluation-harness/pull/4025
* Serialize all numpy scalar types in JSON output, not just int64/int32 by @iamsharduld in https://github.com/EleutherAI/lm-evaluation-harness/pull/3885
* Fix TER metric direction (higher_is_better) and correct chrF docstring by @borgr in https://github.com/EleutherAI/lm-evaluation-harness/pull/3993
* test(registry): add tests for `higher_is_better` directions by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/4050
* Fix ContextSampler crash when few-shot pool contains duplicate eval_doc rows by @Kymi808 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3790
* Fix group stderr to match weight_by_size=False (unweighted) aggregation by @iamsharduld in https://github.com/EleutherAI/lm-evaluation-harness/pull/3882
* Fix MultiChoiceRegexFilter prefix-shadowing of choice text by @iamsharduld in https://github.com/EleutherAI/lm-evaluation-harness/pull/3884
* MMLU Task Name by @Teddygat0r in https://github.com/EleutherAI/lm-evaluation-harness/pull/3660
* Add mlqa tag to run all variants. by @ivanbaldo in https://github.com/EleutherAI/lm-evaluation-harness/pull/2977
* Create missing request-cache parent directories by @sdivyanshu90 in https://github.com/EleutherAI/lm-evaluation-harness/pull/4047
* Fix the Unitxt init method to set the task name by @mprahl in https://github.com/EleutherAI/lm-evaluation-harness/pull/3225
* Pass dataset_kwargs for Unitxt tasks by @mprahl in https://github.com/EleutherAI/lm-evaluation-harness/pull/3230
* feat: add chrf++ aggregation and metric (word_order=2) by @KrishVenky in https://github.com/EleutherAI/lm-evaluation-harness/pull/3780
* feat(tasks): add LongProc benchmark (6 task types, 16 configs) by @xiye17 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3544
* feat(tydiqa): add TyDiQA Gold Passage tasks (9 languages) by @bongho in https://github.com/EleutherAI/lm-evaluation-harness/pull/4044
* add GreekMMLU (official native-sourced benchmark) task configuration by @mersinkonomi in https://github.com/EleutherAI/lm-evaluation-harness/pull/3581
* feat(cli): allow key=value to be passed to `--metadata`; linting by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/4054
* Fix: Prevent infinite loop when max_seq_lengths < 4096 in prepare_niah.py by @vnayakde in https://github.com/EleutherAI/lm-evaluation-harness/pull/3372
* fix(minerva_math): correct few-shot prompt LaTeX by @Ben3892 in https://github.com/EleutherAI/lm-evaluation-harness/pull/4045
* fix(minerva_math): score an answer identical to the gold as correct by @nata2627 in https://github.com/EleutherAI/lm-evaluation-harness/pull/4034
* fix(minerva_math): thousands-separator comma strip fuses bare digit tuples ("0,1" -> "01") by @feiiiiii5 in https://github.com/EleutherAI/lm-evaluation-harness/pull/4039
* fix(minerva_math): stop sqrt shorthand normalization from corrupting indexed roots by @feiiiiii5 in https://github.com/EleutherAI/lm-evaluation-harness/pull/4037
* fix(ruler): resolve the tokenizer name before the cached lookup by @nata2627 in https://github.com/EleutherAI/lm-evaluation-harness/pull/4048
* chore(pre-commit) by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/4060
* fix(scripts): repair requests_caching.py entrypoint (bad kwargs + helper defined after use) by @Anai-Guo in https://github.com/EleutherAI/lm-evaluation-harness/pull/4059
* Add Uncheatable Eval by @ziqing-huang in https://github.com/EleutherAI/lm-evaluation-harness/pull/3442
* Add IndicXNLI Gujarati task (indicxnli_gu) by @bhaumik611 in https://github.com/EleutherAI/lm-evaluation-harness/pull/4056
* feat(physics_gre): add InflectionAI Physics GRE multiple-choice task by @bongho in https://github.com/EleutherAI/lm-evaluation-harness/pull/3853
* fix(evaluator): report a sample count that does not depend on metric order by @arthi-arumugam-git in https://github.com/EleutherAI/lm-evaluation-harness/pull/4068
* Fix/indicparam citation  by @viveks-codes in https://github.com/EleutherAI/lm-evaluation-harness/pull/4066
* fix: make --use_cache keys hashable for multimodal image/byte requests by @feiiiiii5 in https://github.com/EleutherAI/lm-evaluation-harness/pull/4040

</details>

## New Contributors
* @jaydeepborkar made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3768
* @EphraiemSarabamoun made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3795
* @DaoyuanLi2816 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3824
* @he-yufeng made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3822
* @Apeironics made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3803
* @wm901115nwpu made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3817
* @bongho made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3860
* @discobot made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3842
* @hjoshifonteva made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3826
* @ayaangazali made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3977
* @shubhangithub made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3943
* @gowtham-sai-yadav made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3950
* @cameronshinn made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3921
* @Solaris-star made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3944
* @hancheolcho made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3923
* @chuenchen309 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3937
* @SiavashShams made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3978
* @AbdullahRasheed45 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3971
* @adityasingh2400 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3979
* @oberpierre made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3991
* @OrionArchitekton made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3916
* @yaodong-shen made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3959
* @thiagocrepaldi made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3960
* @tandede made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/4020
* @winklemad made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/4003
* @k-dickinson made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3887
* @feiiiiii5 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/4035
* @ivanmartinezmurillo made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3784
* @aryanputta made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3788
* @ganeshr10 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3657
* @nloughl made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3670
* @amd-sourjya made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3984
* @iamsharduld made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3885
* @borgr made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3993
* @Kymi808 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3790
* @Teddygat0r made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3660
* @ivanbaldo made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2977
* @sdivyanshu90 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/4047
* @mprahl made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3225
* @KrishVenky made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3780
* @xiye17 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3544
* @mersinkonomi made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3581
* @vnayakde made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3372
* @Ben3892 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/4045
* @nata2627 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/4034
* @bhaumik611 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/4056
* @arthi-arumugam-git made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/4068
* @viveks-codes made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/4066

**Full Changelog**: https://github.com/EleutherAI/lm-evaluation-harness/compare/v0.4.12...v0.4.13

## What's Changed
* feat: 0.4.13.dev0 by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3764
* update global piqa by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3816
* fix for keyerror while running humaneval_infilling  by @jaydeepborkar in https://github.com/EleutherAI/lm-evaluation-harness/pull/3768
* fix: strip whitespace from input/target for FDA, SWDE, and SQuAD_completion tasks by @EphraiemSarabamoun in https://github.com/EleutherAI/lm-evaluation-harness/pull/3795
* Fix "trasnlation" typo in DarijaBench translation task names by @DaoyuanLi2816 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3824
* fix(ruler): replace defunct hotpot dataset host with pinned HF mirror by @Anai-Guo in https://github.com/EleutherAI/lm-evaluation-harness/pull/3806
* fix: keep Anthropic stop sequences nonempty by @he-yufeng in https://github.com/EleutherAI/lm-evaluation-harness/pull/3822
* fix(vllm): warn when device argument is ignored by @Apeironics in https://github.com/EleutherAI/lm-evaluation-harness/pull/3803
* fix sglang args by @wm901115nwpu in https://github.com/EleutherAI/lm-evaluation-harness/pull/3817
* feat(legalbench): add HELM-lite LegalBench subset (5 tasks) by @bongho in https://github.com/EleutherAI/lm-evaluation-harness/pull/3860
* Fix space in North Macedonian task identifiers (INCLUDE suite) by @DaoyuanLi2816 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3848
* fix(kormedmcqa): extract answer choice per paper Appendix B by @discobot in https://github.com/EleutherAI/lm-evaluation-harness/pull/3842
* Fix dataset paths for xnli, xcopa, paws-x, and xquad by @Chessing234 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3870
* Add IndicParam: MCQ benchmark for 12 low-resource Indic languages by @hjoshifonteva in https://github.com/EleutherAI/lm-evaluation-harness/pull/3826
* feat(portuguese_bench): add ASSIN2 RTE and STS tasks by @bongho in https://github.com/EleutherAI/lm-evaluation-harness/pull/3812
* fix(prost): load PROST without the removed dataset script by @ayaangazali in https://github.com/EleutherAI/lm-evaluation-harness/pull/3977
* fix(spanish_bench): load wnli_es without the removed dataset script by @ayaangazali in https://github.com/EleutherAI/lm-evaluation-harness/pull/3982
* fix(tests): pass dataset_kwargs in test_download by @ayaangazali in https://github.com/EleutherAI/lm-evaluation-harness/pull/3980
* fix(tasks): use namespaced dataset path for wsc273 by @ayaangazali in https://github.com/EleutherAI/lm-evaluation-harness/pull/3946
* fix(tasks): use namespaced dataset paths for webqs, medmcqa, and wmt16 by @ayaangazali in https://github.com/EleutherAI/lm-evaluation-harness/pull/3942
* fix(arithmetic): load arithmetic tasks without the removed dataset script by @ayaangazali in https://github.com/EleutherAI/lm-evaluation-harness/pull/3976
* fix(mmlusr): restore dataset loading for all 171 MMLU-SR tasks by @ayaangazali in https://github.com/EleutherAI/lm-evaluation-harness/pull/3972
* fix(scrolls): load SCROLLS without the removed dataset script by @ayaangazali in https://github.com/EleutherAI/lm-evaluation-harness/pull/3975
* fix(tasks): use script-less parquet mirrors for mathqa, siqa, and moral_stories by @shubhangithub in https://github.com/EleutherAI/lm-evaluation-harness/pull/3943
* fix(tmmluplus): use ikala/tmmluplus so the task loads on datasets>=4 by @gowtham-sai-yadav in https://github.com/EleutherAI/lm-evaluation-harness/pull/3950
* Fix broken afrobench group task references (afrisenti/mafand prompt_2) by @DaoyuanLi2816 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3847
* fix(longbench): skip blank leading line in code_sim_score extraction by @cameronshinn in https://github.com/EleutherAI/lm-evaluation-harness/pull/3921
* fix(afrixnli): use Jinja braces in prompt_1 doc_to_text by @Solaris-star in https://github.com/EleutherAI/lm-evaluation-harness/pull/3944
* fix(jsonschema_bench): add per-sample validation timeout to prevent eval hangs by @hancheolcho in https://github.com/EleutherAI/lm-evaluation-harness/pull/3923
* Fix fewshot_config.split precedence in TaskConfig by @chuenchen309 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3937
* Exclude eval docs from first-n few-shot samples by @SiavashShams in https://github.com/EleutherAI/lm-evaluation-harness/pull/3978
* fix: prevent ValueError when batch_size="auto" is passed to neuronx model by @AbdullahRasheed45 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3971
* fix: prevent ValueError when batch_size="auto:N" is passed to API models by @AbdullahRasheed45 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3970
* fix: resolve fewshot gen_prefix against the fewshot doc, not the eval doc by @adityasingh2400 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3979
* Putnam Axiom by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/3998
* feat(legalbench): add Contract NLI suite (14 NDA entailment tasks) by @bongho in https://github.com/EleutherAI/lm-evaluation-harness/pull/3954
* Fix `megatron_lm` backend against Megatron-LM `core_v0.18+`: argument parsing moved out of `initialize_megatron()` by @oberpierre in https://github.com/EleutherAI/lm-evaluation-harness/pull/3991
* chore(ci): update pre-commit hooks and workflow packages by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/4023
* fix(hf): pass max_cpu_memory through to accelerate's max_memory by @Anai-Guo in https://github.com/EleutherAI/lm-evaluation-harness/pull/4016
* chore(megatron): run linter by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/4024
* fix(huggingface): detect max_length from nested text_config (Gemma3 multimodal) by @OrionArchitekton in https://github.com/EleutherAI/lm-evaluation-harness/pull/3916
* Honor configured timeout for synchronous API requests by @SiavashShams in https://github.com/EleutherAI/lm-evaluation-harness/pull/3995
* fix(api): support think_end_token for chat completions by @yaodong-shen in https://github.com/EleutherAI/lm-evaluation-harness/pull/3959
* feat(models): add cross-platform onnxruntime-genai backend + refactor winml by @thiagocrepaldi in https://github.com/EleutherAI/lm-evaluation-harness/pull/3960
* Enable function resolving for custom tasks by @SkyR0ver in https://github.com/EleutherAI/lm-evaluation-harness/pull/3992
* fix(config): parse dictionary strings from YAML configs by @tandede in https://github.com/EleutherAI/lm-evaluation-harness/pull/4020
* fix: normalize scalar `seed` from a config file the way the CLI does by @winklemad in https://github.com/EleutherAI/lm-evaluation-harness/pull/4003
* fix(filters): format_span only normalizes labels, not entity text by @k-dickinson in https://github.com/EleutherAI/lm-evaluation-harness/pull/3887
* fix: make delete_cache a no-op when the cache directory is absent by @feiiiiii5 in https://github.com/EleutherAI/lm-evaluation-harness/pull/4035
* Add Terretaqa task into Catalanbench by @ivanmartinezmurillo in https://github.com/EleutherAI/lm-evaluation-harness/pull/3784
* Add make_table regression coverage by @aryanputta in https://github.com/EleutherAI/lm-evaluation-harness/pull/3788
* Add cieaCOVA task into catalan bench by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/4043
* fix(irokobench): repair afrimmlu/afrimgsm/afrixnli task registration and update READMEs by @discobot in https://github.com/EleutherAI/lm-evaluation-harness/pull/3841
* fix: fall back to tokenizer.eos_token when decode returns empty string by @ganeshr10 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3657
* fix(med_prescriptions): require both keys before combining complaints and diagnosis by @Anai-Guo in https://github.com/EleutherAI/lm-evaluation-harness/pull/4041
* fix: local directory with task name no longer shadows registered task by @nloughl in https://github.com/EleutherAI/lm-evaluation-harness/pull/3670
* feat(models): add raw onnxruntime backend for Model Builder ONNX exports by @amd-sourjya in https://github.com/EleutherAI/lm-evaluation-harness/pull/3984
* Align pubmedqa task name in README with yaml by @jmichaelov in https://github.com/EleutherAI/lm-evaluation-harness/pull/4025
* Serialize all numpy scalar types in JSON output, not just int64/int32 by @iamsharduld in https://github.com/EleutherAI/lm-evaluation-harness/pull/3885
* Fix TER metric direction (higher_is_better) and correct chrF docstring by @borgr in https://github.com/EleutherAI/lm-evaluation-harness/pull/3993
* test(registry): add tests for `higher_is_better` directions by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/4050
* Fix ContextSampler crash when few-shot pool contains duplicate eval_doc rows by @Kymi808 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3790
* Fix group stderr to match weight_by_size=False (unweighted) aggregation by @iamsharduld in https://github.com/EleutherAI/lm-evaluation-harness/pull/3882
* Fix MultiChoiceRegexFilter prefix-shadowing of choice text by @iamsharduld in https://github.com/EleutherAI/lm-evaluation-harness/pull/3884
* MMLU Task Name by @Teddygat0r in https://github.com/EleutherAI/lm-evaluation-harness/pull/3660
* Add mlqa tag to run all variants. by @ivanbaldo in https://github.com/EleutherAI/lm-evaluation-harness/pull/2977
* Create missing request-cache parent directories by @sdivyanshu90 in https://github.com/EleutherAI/lm-evaluation-harness/pull/4047
* Fix the Unitxt init method to set the task name by @mprahl in https://github.com/EleutherAI/lm-evaluation-harness/pull/3225
* Pass dataset_kwargs for Unitxt tasks by @mprahl in https://github.com/EleutherAI/lm-evaluation-harness/pull/3230
* feat: add chrf++ aggregation and metric (word_order=2) by @KrishVenky in https://github.com/EleutherAI/lm-evaluation-harness/pull/3780
* feat(tasks): add LongProc benchmark (6 task types, 16 configs) by @xiye17 in https://github.com/EleutherAI/lm-evaluation-harness/pull/3544
* feat(tydiqa): add TyDiQA Gold Passage tasks (9 languages) by @bongho in https://github.com/EleutherAI/lm-evaluation-harness/pull/4044
* add GreekMMLU (official native-sourced benchmark) task configuration by @mersinkonomi in https://github.com/EleutherAI/lm-evaluation-harness/pull/3581
* feat(cli): allow key=value to be passed to `--metadata`; linting by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/4054
* Fix: Prevent infinite loop when max_seq_lengths < 4096 in prepare_niah.py by @vnayakde in https://github.com/EleutherAI/lm-evaluation-harness/pull/3372
* fix(minerva_math): correct few-shot prompt LaTeX by @Ben3892 in https://github.com/EleutherAI/lm-evaluation-harness/pull/4045
* fix(minerva_math): score an answer identical to the gold as correct by @nata2627 in https://github.com/EleutherAI/lm-evaluation-harness/pull/4034
* fix(minerva_math): thousands-separator comma strip fuses bare digit tuples ("0,1" -> "01") by @feiiiiii5 in https://github.com/EleutherAI/lm-evaluation-harness/pull/4039
* fix(minerva_math): stop sqrt shorthand normalization from corrupting indexed roots by @feiiiiii5 in https://github.com/EleutherAI/lm-evaluation-harness/pull/4037
* fix(ruler): resolve the tokenizer name before the cached lookup by @nata2627 in https://github.com/EleutherAI/lm-evaluation-harness/pull/4048
* chore(pre-commit) by @baberabb in https://github.com/EleutherAI/lm-evaluation-harness/pull/4060
* fix(scripts): repair requests_caching.py entrypoint (bad kwargs + helper defined after use) by @Anai-Guo in https://github.com/EleutherAI/lm-evaluation-harness/pull/4059
* Add Uncheatable Eval by @ziqing-huang in https://github.com/EleutherAI/lm-evaluation-harness/pull/3442
* Add IndicXNLI Gujarati task (indicxnli_gu) by @bhaumik611 in https://github.com/EleutherAI/lm-evaluation-harness/pull/4056
* feat(physics_gre): add InflectionAI Physics GRE multiple-choice task by @bongho in https://github.com/EleutherAI/lm-evaluation-harness/pull/3853
* fix(evaluator): report a sample count that does not depend on metric order by @arthi-arumugam-git in https://github.com/EleutherAI/lm-evaluation-harness/pull/4068
* Fix/indicparam citation  by @viveks-codes in https://github.com/EleutherAI/lm-evaluation-harness/pull/4066
* fix: make --use_cache keys hashable for multimodal image/byte requests by @feiiiiii5 in https://github.com/EleutherAI/lm-evaluation-harness/pull/4040

## New Contributors
* @jaydeepborkar made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3768
* @EphraiemSarabamoun made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3795
* @DaoyuanLi2816 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3824
* @he-yufeng made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3822
* @Apeironics made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3803
* @wm901115nwpu made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3817
* @bongho made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3860
* @discobot made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3842
* @hjoshifonteva made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3826
* @ayaangazali made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3977
* @shubhangithub made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3943
* @gowtham-sai-yadav made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3950
* @cameronshinn made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3921
* @Solaris-star made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3944
* @hancheolcho made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3923
* @chuenchen309 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3937
* @SiavashShams made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3978
* @AbdullahRasheed45 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3971
* @adityasingh2400 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3979
* @oberpierre made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3991
* @OrionArchitekton made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3916
* @yaodong-shen made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3959
* @thiagocrepaldi made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3960
* @tandede made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/4020
* @winklemad made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/4003
* @k-dickinson made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3887
* @feiiiiii5 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/4035
* @ivanmartinezmurillo made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3784
* @aryanputta made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3788
* @ganeshr10 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3657
* @nloughl made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3670
* @amd-sourjya made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3984
* @iamsharduld made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3885
* @borgr made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3993
* @Kymi808 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3790
* @Teddygat0r made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3660
* @ivanbaldo made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/2977
* @sdivyanshu90 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/4047
* @mprahl made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3225
* @KrishVenky made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3780
* @xiye17 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3544
* @mersinkonomi made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3581
* @vnayakde made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/3372
* @Ben3892 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/4045
* @nata2627 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/4034
* @bhaumik611 made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/4056
* @arthi-arumugam-git made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/4068
* @viveks-codes made their first contribution in https://github.com/EleutherAI/lm-evaluation-harness/pull/4066

**Full Changelog**: https://github.com/EleutherAI/lm-evaluation-harness/compare/v0.4.12...v0.4.13
