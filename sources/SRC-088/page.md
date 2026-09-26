source: https://github.com/EleutherAI/lm-evaluation-harness/releases

# Releases: EleutherAI/lm-evaluation-harness

## Release list

## v0.4.13

## v0.4.13 Release Notes

A fix-focused release. The main fixes are for few-shot leakage, a multiple-choice filter bug, and group stderr, alongside two new ONNX backends and eight new benchmark suites. Also updated most configs for datasets>=4, which accounts for much of the diff by volume.

## Highlights

### Bug Fixes

Fixes that may shift previously reported numbers:

**Eval documents leaked into few-shot prompts.**The sampler could draw the document under test into its own demonstrations by[@SiavashShams](https://github.com/SiavashShams)in[#3978](https://github.com/EleutherAI/lm-evaluation-harness/pull/3978), and`gen_prefix`

was resolved against the eval doc rather than the few-shot doc — splicing the evaluated question into every shot for RULER`niah_single_1`

,`humaneval_instruct`

, and`humaneval_64_instruct`

by[@adityasingh2400](https://github.com/adityasingh2400)in[#3979](https://github.com/EleutherAI/lm-evaluation-harness/pull/3979)Regex alternation is leftmost-wins, so a choice that prefixed a longer choice (`MultiChoiceRegexFilter`

prefix-shadowing.`"Guilty"`

vs`"Guilty of Romance"`

) matched inside it and scored correct answers as wrong — visible on BBH`movie_recommendation`

by[@iamsharduld](https://github.com/iamsharduld)in[#3884](https://github.com/EleutherAI/lm-evaluation-harness/pull/3884)**Group stderr with**Groups reported the size-weighted pooled stderr even when the point estimate was an unweighted mean, giving error bars up to ~3x too narrow. Only unequal-sized subtasks change by`weight_by_size: false`

.[@iamsharduld](https://github.com/iamsharduld)in[#3882](https://github.com/EleutherAI/lm-evaluation-harness/pull/3882)`minerva_math`

answer normalization.`sqrt`

shorthand no longer corrupts indexed roots ([#4037](https://github.com/EleutherAI/lm-evaluation-harness/pull/4037)), the thousands-separator strip no longer fuses digit tuples (`0,1`

→`01`

,[#4039](https://github.com/EleutherAI/lm-evaluation-harness/pull/4039)), an answer identical to the gold now scores correct ([#4034](https://github.com/EleutherAI/lm-evaluation-harness/pull/4034)), and the few-shot prompt LaTeX is corrected ([#4045](https://github.com/EleutherAI/lm-evaluation-harness/pull/4045)) by[@feiiiiii5](https://github.com/feiiiiii5)and[@nata2627](https://github.com/nata2627).`putnam_axiom`

shares these helpers and picks up the same fixes.

### New Model Backends

— raw onnxruntime backend for Model Builder ONNX exports by`onnxruntime`

[@amd-sourjya](https://github.com/amd-sourjya)in[#3984](https://github.com/EleutherAI/lm-evaluation-harness/pull/3984)— cross-platform ONNX Runtime GenAI backend, with`onnxruntime-genai`

`winml`

refactored on top of it by[@thiagocrepaldi](https://github.com/thiagocrepaldi)in[#3960](https://github.com/EleutherAI/lm-evaluation-harness/pull/3960)**Megatron-LM v0.18**compatibility by[@oberpierre](https://github.com/oberpierre)in[#3991](https://github.com/EleutherAI/lm-evaluation-harness/pull/3991)

Install with `pip install lm_eval[onnxruntime]`

or `lm_eval[onnxruntime-genai]`

. For non-CPU execution providers install the matching wheel instead — `onnxruntime-gpu`

/ `onnxruntime-rocm`

, or `onnxruntime-genai-cuda`

/ `onnxruntime-genai-directml`

— these are mutually exclusive.

## New Tasks

**LongProc**— long-context procedural reasoning, 6 task types across 16 configs by[@xiye17](https://github.com/xiye17)in[#3544](https://github.com/EleutherAI/lm-evaluation-harness/pull/3544)**Uncheatable Eval**— contamination-resistant evaluation: rolling log-likelihood over recently-published documents from Wikipedia, GitHub, BBC News, arXiv, bioRxiv, and AO3, as 15 category tasks plus a size-weighted group by[@ziqing-huang](https://github.com/ziqing-huang)in[#3442](https://github.com/EleutherAI/lm-evaluation-harness/pull/3442)**TyDiQA Gold Passage**— 9-language multilingual QA by[@bongho](https://github.com/bongho)in[#4044](https://github.com/EleutherAI/lm-evaluation-harness/pull/4044)**LegalBench**— new suite, 19 tasks: the HELM-lite LegalBench subset (5 tasks,[#3860](https://github.com/EleutherAI/lm-evaluation-harness/pull/3860)) and the Contract NLI suite (14 NDA entailment tasks,[#3954](https://github.com/EleutherAI/lm-evaluation-harness/pull/3954)) by[@bongho](https://github.com/bongho)**IndicParam**— MCQ benchmark covering 12 low-resource Indic languages by[@hjoshifonteva](https://github.com/hjoshifonteva)in[#3826](https://github.com/EleutherAI/lm-evaluation-harness/pull/3826)**IndicXNLI Gujarati**(`indicxnli_gu`

) by[@bhaumik611](https://github.com/bhaumik611)in[#4056](https://github.com/EleutherAI/lm-evaluation-harness/pull/4056)**GreekMMLU**— official native-sourced configuration by[@mersinkonomi](https://github.com/mersinkonomi)in[#3581](https://github.com/EleutherAI/lm-evaluation-harness/pull/3581)**Physics GRE**— InflectionAI multiple-choice physics benchmark by[@bongho](https://github.com/bongho)in[#3853](https://github.com/EleutherAI/lm-evaluation-harness/pull/3853)**Putnam Axiom**— competition-level mathematical reasoning by[@baberabb](https://github.com/baberabb)in[#3998](https://github.com/EleutherAI/lm-evaluation-harness/pull/3998)**Portuguese Bench**— ASSIN2 RTE and STS by[@bongho](https://github.com/bongho)in[#3812](https://github.com/EleutherAI/lm-evaluation-harness/pull/3812)**Catalanbench**— cieaCOVA ([#4043](https://github.com/EleutherAI/lm-evaluation-harness/pull/4043)) and Terretaqa ([#3784](https://github.com/EleutherAI/lm-evaluation-harness/pull/3784)) by[@baberabb](https://github.com/baberabb)and[@ivanmartinezmurillo](https://github.com/ivanmartinezmurillo)**MLQA**— a tag to run all variants at once by[@ivanbaldo](https://github.com/ivanbaldo)in[#2977](https://github.com/EleutherAI/lm-evaluation-harness/pull/2977)

## Task Changes

### Correctness & Prompts

**global_piqa**restructured into parallel/non-parallel × cloze/generation variants; the`global_piqa_completions`

and`global_piqa_prompted`

groups are now`global_piqa_cloze`

and`global_piqa_generation`

by[@baberabb](https://github.com/baberabb)in[#3816](https://github.com/EleutherAI/lm-evaluation-harness/pull/3816)**IrokoBench**— repaired`afrimmlu`

/`afrimgsm`

/`afrixnli`

task registration by[@discobot](https://github.com/discobot)in[#3841](https://github.com/EleutherAI/lm-evaluation-harness/pull/3841), fixed the broken`afrisenti`

/`mafand`

prompt_2 group references by[@DaoyuanLi2816](https://github.com/DaoyuanLi2816)in[#3847](https://github.com/EleutherAI/lm-evaluation-harness/pull/3847), and switched`afrixnli`

prompt_1`doc_to_text`

to Jinja braces by[@Solaris-star](https://github.com/Solaris-star)in[#3944](https://github.com/EleutherAI/lm-evaluation-harness/pull/3944)**KorMedMCQA**— answer-choice extraction now follows the paper's Appendix B by[@discobot](https://github.com/discobot)in[#3842](https://github.com/EleutherAI/lm-evaluation-harness/pull/3842)**JSONSchema Bench**— per-sample validation timeout so a pathological schema no longer hangs the whole eval by[@hancheolcho](https://github.com/hancheolcho)in[#3923](https://github.com/EleutherAI/lm-evaluation-harness/pull/3923)**RULER**— every task crashed with`TypeError: unhashable type: 'dict'`

before inference when the tokenizer arrived as anything but a plain string (e.g. under`local-chat-completions`

); the name is now resolved before the cached lookup by[@nata2627](https://github.com/nata2627)in[#4048](https://github.com/EleutherAI/lm-evaluation-harness/pull/4048)**NIAH**— no longer loops forever when`max_seq_lengths < 4096`

by[@vnayakde](https://github.com/vnayakde)in[#3372](https://github.com/EleutherAI/lm-evaluation-harness/pull/3372)**LongBench**—`code_sim_score`

skips a blank leading line before extraction by[@cameronshinn](https://github.com/cameronshinn)in[#3921](https://github.com/EleutherAI/lm-evaluation-harness/pull/3921)**FDA / SWDE / SQuAD_completion**— whitespace stripped from input and target by[@EphraiemSarabamoun](https://github.com/EphraiemSarabamoun)in[#3795](https://github.com/EleutherAI/lm-evaluation-harness/pull/3795)**med_prescriptions**— requires both keys before combining complaints and diagnosis by[@Anai-Guo](https://github.com/Anai-Guo)in[#4041](https://github.com/EleutherAI/lm-evaluation-harness/pull/4041)**HumanEval**—`humaneval_random_span_infilling_light`

was registered under the wrong task name, causing a`KeyError`

by[@jaydeepborkar](https://github.com/jaydeepborkar)in[#3768](https://github.com/EleutherAI/lm-evaluation-harness/pull/3768)**INCLUDE**— stray space removed from North Macedonian task identifiers by[@DaoyuanLi2816](https://github.com/DaoyuanLi2816)in[#3848](https://github.com/EleutherAI/lm-evaluation-harness/pull/3848)**DarijaBench**—`trasnlation`

typo corrected in translation task names by[@DaoyuanLi2816](https://github.com/DaoyuanLi2816)in[#3824](https://github.com/EleutherAI/lm-evaluation-harness/pull/3824)**Unitxt**—`dataset_kwargs`

is now passed through ([#3230](https://github.com/EleutherAI/lm-evaluation-harness/pull/3230)) and`init`

sets the task name ([#3225](https://github.com/EleutherAI/lm-evaluation-harness/pull/3225)) by[@mprahl](https://github.com/mprahl)— normalizes labels only, leaving entity text untouched by`format_span`

filter[@k-dickinson](https://github.com/k-dickinson)in[#3887](https://github.com/EleutherAI/lm-evaluation-harness/pull/3887)**ContextSampler**— no longer crashes when the few-shot pool contains duplicate eval-doc rows by[@Kymi808](https://github.com/Kymi808)in[#3790](https://github.com/EleutherAI/lm-evaluation-harness/pull/3790)— a nested`fewshot_config.split`

`fewshot_config.split`

now takes precedence over the inherited top-level`fewshot_split`

, as documented by[@chuenchen309](https://github.com/chuenchen309)in[#3937](https://github.com/EleutherAI/lm-evaluation-harness/pull/3937)

## Model Backends & APIs

- Chat completions now support
`think_end_token`

by[@yaodong-shen](https://github.com/yaodong-shen)in[#3959](https://github.com/EleutherAI/lm-evaluation-harness/pull/3959) `auto:N`

batch size is parsed correctly in API models by[@AbdullahRasheed45](https://github.com/AbdullahRasheed45)in[#3970](https://github.com/EleutherAI/lm-evaluation-harness/pull/3970), and`batch_size="auto"`

no longer raises on the neuronx backend by[@AbdullahRasheed45](https://github.com/AbdullahRasheed45)in[#3971](https://github.com/EleutherAI/lm-evaluation-harness/pull/3971)- Synchronous API requests honor the configured timeout by
[@SiavashShams](https://github.com/SiavashShams)in[#3995](https://github.com/EleutherAI/lm-evaluation-harness/pull/3995) - Anthropic stop sequences are kept non-empty by
[@he-yufeng](https://github.com/he-yufeng)in[#3822](https://github.com/EleutherAI/lm-evaluation-harness/pull/3822) - HF:
`max_length`

is detected from a nested`text_config`

(Gemma3 multimodal) by[@OrionArchitekton](https://github.com/OrionArchitekton)in[#3916](https://github.com/EleutherAI/lm-evaluation-harness/pull/3916),`max_cpu_memory`

is passed through to accelerate's`max_memory`

by[@Anai-Guo](https://github.com/Anai-Guo)in[#4016](https://github.com/EleutherAI/lm-evaluation-harness/pull/4016), and tokenizers that decode to an empty string fall back to`tokenizer.eos_token`

by[@ganeshr10](https://github.com/ganeshr10)in[#3657](https://github.com/EleutherAI/lm-evaluation-harness/pull/3657) - vLLM warns when it ignores the
`device`

argument by[@Apeironics](https://github.com/Apeironics)in[#3803](https://github.com/EleutherAI/lm-evaluation-harness/pull/3803); sglang argument passing fixed by[@wm901115nwpu](https://github.com/wm901115nwpu)in[#3817](https://github.com/EleutherAI/lm-evaluation-harness/pull/3817)

## Core, CLI & Config

`--metadata`

accepts`key=value`

pairs in addition to JSON by[@baberabb](https://github.com/baberabb)in[#4054](https://github.com/EleutherAI/lm-evaluation-harness/pull/4054)`--use_cache`

keys are hashable for multimodal image/byte requests by[@feiiiiii5](https://github.com/feiiiiii5)in[#4040](https://github.com/EleutherAI/lm-evaluation-harness/pull/4040)- Cache parent directories are created when missing by
[@sdivyanshu90](https://github.com/sdivyanshu90)in[#4047](https://github.com/EleutherAI/lm-evaluation-harness/pull/4047);`delete_cache`

is a no-op when the directory is absent by[@feiiiiii5](https://github.com/feiiiiii5)in[#4035](https://github.com/EleutherAI/lm-evaluation-harness/pull/4035) - A local directory sharing a task's name no longer shadows the registered task by
[@nloughl](https://github.com/nloughl)in[#3670](https://github.com/EleutherAI/lm-evaluation-harness/pull/3670) - Function resolving works for custom tasks by
[@SkyR0ver](https://github.com/SkyR0ver)in[#3992](https://github.com/EleutherAI/lm-evaluation-harness/pull/3992); string dictionary arguments parse correctly by[@tandede](https://github.com/tandede)in[#4020](https://github.com/EleutherAI/lm-evaluation-harness/pull/4020) - A scalar
`seed`

from a config file is normalized the same way the CLI does by[@winklemad](https://github.com/winklemad)in[#4003](https://github.com/EleutherAI/lm-evaluation-harness/pull/4003) - Sample counts no longer depend on metric ordering by
[@arthi-arumugam-git](https://github.com/arthi-arumugam-git)in[#4068](https://github.com/EleutherAI/lm-evaluation-harness/pull/4068) `scripts/requests_caching.py`

entrypoint repaired — bad kwargs and a helper defined after its use by[@Anai-Guo](https://github.com/Anai-Guo)in[#4059](https://github.com/EleutherAI/lm-evaluation-harness/pull/4059)**chrF++**aggregation and metric (`word_order=2`

) by[@KrishVenky](https://github.com/KrishVenky)in[#3780](https://github.com/EleutherAI/lm-evaluation-harness/pull/3780); TER metric direction corrected and the chrF docstring fixed by[@borgr](https://github.com/borgr)in[#3993](https://github.com/EleutherAI/lm-evaluation-harness/pull/3993)- All numpy scalar types serialize to JSON, not just
`int64`

/`int32`

, by[@iamsharduld](https://github.com/iamsharduld)in[#3885](https://github.com/EleutherAI/lm-evaluation-harness/pull/3885)

## Migration Notes

**Few-shot prompts changed**for tasks using a document-specific`gen_prefix`

(RULER`niah_single_1`

,`humaneval_instruct`

,`humaneval_64_instruct`

) and anywhere the sampler previously drew the eval document into its own shots. Prior numbers on those tasks may not be comparable.`minerva_math`

and`leaderboard_math_*`

now diverge.`lm_eval/tasks/leaderboard/math/utils.py`

is deliberately frozen to reproduce Open LLM Leaderboard v2 scoring; the normalization fixes landed in`minerva_math`

only.— see Task Changes above.`global_piqa`

task names changed**If you pinned**to keep script-based tasks working, you can unpin. Out-of-tree task YAMLs pointing at script-based datasets still need the same treatment.`datasets<4`

and pulls in that extra.`winml`

now sits on top of`onnxruntime-genai`


## What's Changed


- feat: 0.4.13.dev0 by
[@baberabb](https://github.com/baberabb)in[#3764](https://github.com/EleutherAI/lm-evaluation-harness/pull/3764) - update global piqa by
[@baberabb](https://github.com/baberabb)in[#3816](https://github.com/EleutherAI/lm-evaluation-harness/pull/3816) - fix for keyerror while running humaneval_infilling by
[@jaydeepborkar](https://github.com/jaydeepborkar)in[#3768](https://github.com/EleutherAI/lm-evaluation-harness/pull/3768) - fix: strip whitespace from input/target for FDA, SWDE, and SQuAD_completion tasks by
[@EphraiemSarabamoun](https://github.com/EphraiemSarabamoun)in[#3795](https://github.com/EleutherAI/lm-evaluation-harness/pull/3795) - Fix "trasnlation" typo in DarijaBench translation task names by
[@DaoyuanLi2816](https://github.com/DaoyuanLi2816)in[#3824](https://github.com/EleutherAI/lm-evaluation-harness/pull/3824) - fix(ruler): replace defunct hotpot dataset host with pinned HF mirror by
[@Anai-Guo](https://github.com/Anai-Guo)in[#3806](https://github.com/EleutherAI/lm-evaluation-harness/pull/3806) - fix: keep Anthropic stop sequences nonempty by
[@he-yufeng](https://github.com/he-yufeng)in[#3822](https://github.com/EleutherAI/lm-evaluation-harness/pull/3822) - fix(vllm): warn when device argument is ignored by
[@Apeironics](https://github.com/Apeironics)in[#3803](https://github.com/EleutherAI/lm-evaluation-harness/pull/3803) - fix sglang args by
[@wm901115nwpu](https://github.com/wm901115nwpu)in ...

[Read more](https://github.com/EleutherAI/lm-evaluation-harness/releases/tag/v0.4.13)

## v0.4.12

New release with four new model backends, tensor parallel support for `transformers`

based models (`hf`

), new benchmarks, a `TaskManager`

refactor, and a long tail of task correctness fixes.

## Highlights

### New Model Backends

**TensorRT-LLM (**— NVIDIA TensorRT-LLM backend for optimized GPU inference by`trt-llm`

)[@Tracin](https://github.com/Tracin)in[#3628](https://github.com/EleutherAI/lm-evaluation-harness/pull/3628)**Megatron-LM (**— Megatron-LM backend with TP/EP/DP support by`megatron-lm`

)[@shangxiaokang](https://github.com/shangxiaokang)in[#3521](https://github.com/EleutherAI/lm-evaluation-harness/pull/3521)(with follow-up hardening in[#3607](https://github.com/EleutherAI/lm-evaluation-harness/pull/3607))**Intel Gaudi**— Gaudi support via`optimum-habana`

by[@12010486](https://github.com/12010486)in[#3550](https://github.com/EleutherAI/lm-evaluation-harness/pull/3550)**LiteLLM AI gateway (**— Use LiteLLM as a unified API gateway for 100+ providers by`litellm`

)[@RheagalFire](https://github.com/RheagalFire)in[#3721](https://github.com/EleutherAI/lm-evaluation-harness/pull/3721)**Native Tensor Parallelism for HF backend**— multi-GPU TP for`transformers`

models via`tp_plan`

by[@YangKai0616](https://github.com/YangKai0616)in[#3692](https://github.com/EleutherAI/lm-evaluation-harness/pull/3692)

`TaskManager`

Refactor ([#3549](https://github.com/EleutherAI/lm-evaluation-harness/pull/3549))

`TaskManager.load(...)`

returns a flat`{tasks, groups}`

dict instead of the legacy nested`{ConfigurableGroup: {name: Task}}`

.`evaluate()`

accepts both shapes;`load_task_or_group(...)`

and`get_task_dict(...)`

are deprecated shims that return the old shape.- New
`Group`

class directly holds its child tasks;`ConfigurableGroup`

is now a deprecated wrapper around it. - Duplicate task/group configs within the same root are skipped with a log message instead of silently overwritten. (Custom
`include_path`

entries still override defaults.)

### Breaking Changes

— update imports if you're using the steering backend by`SteeredHF`

renamed to`SteeredModel`

[@adrian-sauter](https://github.com/adrian-sauter)in[#3592](https://github.com/EleutherAI/lm-evaluation-harness/pull/3592)**vLLM minimum bumped to**as part of the data-parallel-with-Ray fixes by`>=0.18`

[@baberabb](https://github.com/baberabb)in[#3725](https://github.com/EleutherAI/lm-evaluation-harness/pull/3725), and`enable_thinking`

is now disallowed for`multiple_choice`

/ loglikelihood tasks`think_end_token`

is now required when`enable_thinking=True`

. Configurations that combined these previously failed silently by[@fxmarty-amd](https://github.com/fxmarty-amd)in[#3675](https://github.com/EleutherAI/lm-evaluation-harness/pull/3675)

### New Logger

## New Benchmarks & Tasks

**InfiniteBench**— long-context evaluation beyond 100K tokens (12 sub-tasks: code debug/run, KV retrieval, longbook QA/summarization, math find, passkey, etc.) by[@siddhant-rajhans](https://github.com/siddhant-rajhans)in[#3662](https://github.com/EleutherAI/lm-evaluation-harness/pull/3662)**CRUXEval**— Python code reasoning benchmark with input/output prediction variants (incl. CoT and pass@k variants) by[@ThomasHeap](https://github.com/ThomasHeap)in[#3699](https://github.com/EleutherAI/lm-evaluation-harness/pull/3699)**Toksuite**— multilingual tokenization-robustness benchmark (Chinese, English, and more) by[@gsaltintas](https://github.com/gsaltintas)in[#3669](https://github.com/EleutherAI/lm-evaluation-harness/pull/3669)**NEREL-bench**— Russian named-entity / relation-extraction benchmark by[@bond005](https://github.com/bond005)in[#3650](https://github.com/EleutherAI/lm-evaluation-harness/pull/3650)**JFinQA**— Japanese Financial Numerical Reasoning QA (1000 questions, with consistency / numerical / temporal splits) by[@ajtgjmdjp](https://github.com/ajtgjmdjp)in[#3570](https://github.com/EleutherAI/lm-evaluation-harness/pull/3570)

## Fixes & Improvements

### Task Fixes

- Fixed
**GPQA**preprocessing regex that corrupted answer text containing brackets by[@Robby955](https://github.com/Robby955)in[#3691](https://github.com/EleutherAI/lm-evaluation-harness/pull/3691)and[@Chessing234](https://github.com/Chessing234)in[#3735](https://github.com/EleutherAI/lm-evaluation-harness/pull/3735) - Fixed
**MMLU-Pro**and**MMLU-Pro-Plus**few-shot answers leaking into the user role under chat templates by[@kiwaku](https://github.com/kiwaku)in[#3693](https://github.com/EleutherAI/lm-evaluation-harness/pull/3693),[#3747](https://github.com/EleutherAI/lm-evaluation-harness/pull/3747) - Fixed
**RACE**`doc_to_text`

keeping a blank marker and dropping the question body by[@Chessing234](https://github.com/Chessing234)in[#3716](https://github.com/EleutherAI/lm-evaluation-harness/pull/3716) - Fixed
**BigBench**multiple-choice tasks crashing on mixed-format examples (filtered out free-form examples) by[@Chessing234](https://github.com/Chessing234)in[#3702](https://github.com/EleutherAI/lm-evaluation-harness/pull/3702) - Fixed
**HeadQA**`doc_to_decontamination_query`

pointing at a nonexistent`query`

field by[@Chessing234](https://github.com/Chessing234)in[#3718](https://github.com/EleutherAI/lm-evaluation-harness/pull/3718) - Fixed
**french_bench_topic_based_nli**`doc_to_decontamination_query`

pointing at nonexistent`texte`

field by[@Chessing234](https://github.com/Chessing234)in[#3719](https://github.com/EleutherAI/lm-evaluation-harness/pull/3719) - Fixed
**TruthfulQA-gen**`dataset_path`

by[@zhngstl](https://github.com/zhngstl)in[#3723](https://github.com/EleutherAI/lm-evaluation-harness/pull/3723) - Fixed
**NorEval/NorIdiom**`!function`

imports to use absolute module paths by[@Anai-Guo](https://github.com/Anai-Guo)in[#3731](https://github.com/EleutherAI/lm-evaluation-harness/pull/3731) - Fixed
**IFEval**`RephraseChecker.strip_changes`

greedy-regex bug by[@Chessing234](https://github.com/Chessing234)in[#3737](https://github.com/EleutherAI/lm-evaluation-harness/pull/3737) - Fixed correctness issues in
**Arabic**normalization and prompt loading by[@RinZ27](https://github.com/RinZ27)in[#3589](https://github.com/EleutherAI/lm-evaluation-harness/pull/3589) - Updated
**BLiMP**dataset path by[@jmichaelov](https://github.com/jmichaelov)in[#3596](https://github.com/EleutherAI/lm-evaluation-harness/pull/3596) - Replaced all references to the
`CohereForAI`

org with`CohereLabs`

by[@juliafalcao](https://github.com/juliafalcao)in[#3631](https://github.com/EleutherAI/lm-evaluation-harness/pull/3631)

## What's Changed

- refactor(Taskmanager)! by
[@baberabb](https://github.com/baberabb)in[#3549](https://github.com/EleutherAI/lm-evaluation-harness/pull/3549) - fix(cli):
`--cache_requests`

always fails due to argparse`type`

/`choices`

conflict by[@maxidl](https://github.com/maxidl)in[#3588](https://github.com/EleutherAI/lm-evaluation-harness/pull/3588) - feat: Add Megatron-LM backend with TP/EP/DP support by
[@shangxiaokang](https://github.com/shangxiaokang)in[#3521](https://github.com/EleutherAI/lm-evaluation-harness/pull/3521) - Fix:
[#3293](https://github.com/EleutherAI/lm-evaluation-harness/issues/3293)(pybass UnboundLocalError on outputs in Exception Logging) by[@lucafossen](https://github.com/lucafossen)in[#3601](https://github.com/EleutherAI/lm-evaluation-harness/pull/3601) - [fix] Add missing tokenization progress bar by
[@fxmarty-amd](https://github.com/fxmarty-amd)in[#3605](https://github.com/EleutherAI/lm-evaluation-harness/pull/3605) - fix: improve model_args type coercion in handle_arg_string by
[@ManasVardhan](https://github.com/ManasVardhan)in[#3608](https://github.com/EleutherAI/lm-evaluation-harness/pull/3608) - fix: harden Megatron GPT layer spec setup for eval by
[@shangxiaokang](https://github.com/shangxiaokang)in[#3607](https://github.com/EleutherAI/lm-evaluation-harness/pull/3607) - Update vLLM import of
`resolve_hf_chat_template`

by[@DarkLight1337](https://github.com/DarkLight1337)in[#3595](https://github.com/EleutherAI/lm-evaluation-harness/pull/3595) - Add docstring for HFLM
**init**keyword arguments by[@joshuaswanson](https://github.com/joshuaswanson)in[#3630](https://github.com/EleutherAI/lm-evaluation-harness/pull/3630) - Update all mentions of the
`CohereForAI`

organization to`CohereLabs`

by[@juliafalcao](https://github.com/juliafalcao)in[#3631](https://github.com/EleutherAI/lm-evaluation-harness/pull/3631) - Skip caching None responses in async generation path by
[@joshuaswanson](https://github.com/joshuaswanson)in[#3633](https://github.com/EleutherAI/lm-evaluation-harness/pull/3633) - Fix correctness issues in Arabic normalization and prompt loading by
[@RinZ27](https://github.com/RinZ27)in[#3589](https://github.com/EleutherAI/lm-evaluation-harness/pull/3589) - fix(evaluate tests) by
[@baberabb](https://github.com/baberabb)in[#3634](https://github.com/EleutherAI/lm-evaluation-harness/pull/3634) - fix: propagate custom aggregation to dict-valued metric result keys by
[@s-zx](https://github.com/s-zx)in[#3626](https://github.com/EleutherAI/lm-evaluation-harness/pull/3626) - chore(ci-updates) by
[@baberabb](https://github.com/baberabb)in[#3635](https://github.com/EleutherAI/lm-evaluation-harness/pull/3635) - Update BLiMP dataset path by
[@jmichaelov](https://github.com/jmichaelov)in[#3596](https://github.com/EleutherAI/lm-evaluation-harness/pull/3596) - Add jfinqa: Japanese Financial Numerical Reasoning QA (1000 questions) by
[@ajtgjmdjp](https://github.com/ajtgjmdjp)in[#3570](https://github.com/EleutherAI/lm-evaluation-harness/pull/3570) - Rename SteeredHF to SteeredModel in lm_eval/models/
**init**.py by[@adrian-sauter](https://github.com/adrian-sauter)in[#3592](https://github.com/EleutherAI/lm-evaluation-harness/pull/3592) - fix: Update
`WatsonxLLM`

class mapping and errors by[@Rafal-Chrzanowski-IBM](https://github.com/Rafal-Chrzanowski-IBM)in[#3591](https://github.com/EleutherAI/lm-evaluation-harness/pull/3591) - Add Intel Gaudi support by
[@12010486](https://github.com/12010486)in[#3550](https://github.com/EleutherAI/lm-evaluation-harness/pull/3550) - [fix] Disallow
`enable_thinking`

with`output_type: multiple_choice`

tasks / loglikelihood tasks; raise error in case`think_end_token`

is not provided with`enable_thinking=True`

by[@fxmarty-amd](https://github.com/fxmarty-amd)in[#3675](https://github.com/EleutherAI/lm-evaluation-harness/pull/3675) - fix(vllm): fix dp with ray. remove mp distribution; pin vllm >=0.18 by
[@baberabb](https://github.com/baberabb)in[#3725](https://github.com/EleutherAI/lm-evaluation-harness/pull/3725) - refactor(utils): fix mistral tokenizer error; improve doc-strings by
[@baberabb](https://github.com/baberabb)in[#3728](https://github.com/EleutherAI/lm-evaluation-harness/pull/3728) - fix(vllm): fix vllm tokenizer for Mistral; rm default
`gpu_memory_utilization=0.9`

by[@baberabb](https://github.com/baberabb)in[#3732](https://github.com/EleutherAI/lm-evaluation-harness/pull/3732) - Fix GPQA preprocess stripping mathematical bracket expressions by
[@Chessing234](https://github.com/Chessing234)in[#3735](https://github.com/EleutherAI/lm-evaluation-harness/pull/3735) - Guard vLLM tok_encode against prefix_token_id being None by
[@Chessing234](https://github.com/Chessing234)in[#3724](https://github.com/EleutherAI/lm-evaluation-harness/pull/3724) - fix(ifeval): use non-greedy regex in RephraseChecker.strip_changes by
[@Chessing234](https://github.com/Chessing234)in[#3737](https://github.com/EleutherAI/lm-evaluation-harness/pull/3737) - fix: bound request cache filename length by
[@princepal9120](https://github.com/princepal9120)in[#3729](https://github.com/EleutherAI/lm-evaluation-harness/pull/3729) - fix codeowners by
[@baberabb](https://github.com/baberabb)in[#3738](https://github.com/EleutherAI/lm-evaluation-harness/pull/3738) - Fix dataset_path for truthfulqa_gen by
[@zhngstl](https://github.com/zhngstl)in[#3723](https://github.com/EleutherAI/lm-evaluation-harness/pull/3723) - fix(vllm): disallow data_parallel with enable_expert_parallel by
[@FazeelUsmani](https://github.com/FazeelUsmani)in[#3734](https://github.com/EleutherAI/lm-evaluation-harness/pull/3734) - Add Trackio logger with per-sample Trace logging by
[@abidlabs](https://github.com/abidlabs)in[#3733](https://github.com/EleutherAI/lm-evaluation-harness/pull/3733) - Fix headqa doc_to_decontamination_query pointing at nonexistent 'query' field by
[@Chessing234](https://github.com/Chessing234)in[#3718](https://github.com/EleutherAI/lm-evaluation-harness/pull/3718) - Fix french_bench_topic_based_nli doc_to_decontamination_query pointing at nonexistent 'texte' field by
[@Chessing234](https://github.com/Chessing234)in[#3719](https://github.com/EleutherAI/lm-evaluation-harness/pull/3719) - fix(noreval/noridiom): use absolute module paths for !function imports (
[#3624](https://github.com/EleutherAI/lm-evaluation-harness/issues/3624)) by[@Anai-Guo](https://github.com/Anai-Guo)in[#3731](https://github.com/EleutherAI/lm-evaluation-harness/pull/3731) - Fix DummyLM.generate_until printing context as gen_kwargs by
[@Chessing234](https://github.com/Chessing234)in[#3711](https://github.com/EleutherAI/lm-evaluation-harness/pull/3711) - Fix MultiChoiceRegexFilter.find_match IndexError on all-empty capture groups by
[@Chessing234](https://github.com/Chessing234)in[#3708](https://github.com/EleutherAI/lm-evaluation-harness/pull/3708) - fix(model_comparator): fix ImportError from scipy.stats.norm import by
[@Chessing234](https://github.com/Chessing234)in[#3742](https://github.com/EleutherAI/lm-evaluation-harness/pull/3742) - Fix zeno_visualize discarding tasks intersection result by
[@Chessing234](https://github.com/Chessing234)in[#3739](https://github.com/EleutherAI/lm-evaluation-harness/pull/3739) - fix: don't pass task stop sequences to vLLM for reasoning models by
[@jwmacd](https://github.com/jwmacd)in[#3700](https://github.com/EleutherAI/lm-evaluation-harness/pull/3700) - feat: Add [ LiteLLM AI gateway ] as model backend by
[@RheagalFire](https://github.com/RheagalFire)in[#3721](https://github.com/EleutherAI/lm-evaluation-harness/pull/3721) - Fix RACE doc_to_text keeping blank marker and dropping the question body by
[@ch](https://github.com/ch)...

[Read more](https://github.com/EleutherAI/lm-evaluation-harness/releases/tag/v0.4.12)

## v0.4.11

## v0.4.11 Release Notes

Minor release. Stay tuned for bigger changes next release.

### New Platform Support

**Windows ML Backend**— Native Windows ML inference support by[@chapsiru](https://github.com/chapsiru)and[@chemwolf6922](https://github.com/chemwolf6922)in[#3470](https://github.com/EleutherAI/lm-evaluation-harness/pull/3470),[#3564](https://github.com/EleutherAI/lm-evaluation-harness/pull/3564),[#3565](https://github.com/EleutherAI/lm-evaluation-harness/pull/3565)

### New Benchmarks & Tasks

### Task Version Changes

The following tasks have updated versions. Results from a previous task versions may not be directly comparable. See the linked PRs or individual task READMEs for changelogs.


`afrobench_belebele`

(all variants): 2 → 3 in [#3551](https://github.com/EleutherAI/lm-evaluation-harness/pull/3551)

`evalita_llm`

: 0.0 → 0.1 in [#3551](https://github.com/EleutherAI/lm-evaluation-harness/pull/3551)

`include`

(all 90 language variants): 0.0 → 0.1 in [#3551](https://github.com/EleutherAI/lm-evaluation-harness/pull/3551)

`mgsm_direct`

(all 11 language variants): 3.0 → 4.0 by [@LakshyaChaudhry](https://github.com/LakshyaChaudhry) in [#3574](https://github.com/EleutherAI/lm-evaluation-harness/pull/3574)

### Fixes & Improvements

- Fixed
**SQuAD v2**evaluation by[@HydrogenSulfate](https://github.com/HydrogenSulfate)in[#3535](https://github.com/EleutherAI/lm-evaluation-harness/pull/3535) - Fixed
**MasakhaNEWS**tasks — replaced non-existent`headline_text`

field with`headline`

by[@Mr-Neutr0n](https://github.com/Mr-Neutr0n)in[#3567](https://github.com/EleutherAI/lm-evaluation-harness/pull/3567) - Fixed incorrect task configs by
[@baberabb](https://github.com/baberabb)in[#3552](https://github.com/EleutherAI/lm-evaluation-harness/pull/3552) - Replaced
`eval()`

with`ast.literal_eval`

in task configs for safer parsing by[@baberabb](https://github.com/baberabb)in[#3577](https://github.com/EleutherAI/lm-evaluation-harness/pull/3577) - Fixed
**SGLang**duplicate registration error by[@enpimashin](https://github.com/enpimashin)in[#3543](https://github.com/EleutherAI/lm-evaluation-harness/pull/3543) - Restored
import check by`hf_transfer`

[@baberabb](https://github.com/baberabb)in[#3563](https://github.com/EleutherAI/lm-evaluation-harness/pull/3563) - Fixed
`modify_gen_kwargs`

call in**vLLM VLMs**by[@hmellor](https://github.com/hmellor)in[#3573](https://github.com/EleutherAI/lm-evaluation-harness/pull/3573) - Refactored
**vLLM**`gen_kwargs`

normalization inline to`modify_gen_kwargs`

; fixed cached`gen_kwargs`

mutation by[@baberabb](https://github.com/baberabb)in[#3582](https://github.com/EleutherAI/lm-evaluation-harness/pull/3582) - Fixed README for task-listing CLI command by
[@UltimateJupiter](https://github.com/UltimateJupiter)in[#3545](https://github.com/EleutherAI/lm-evaluation-harness/pull/3545) - Updated dependencies by
[@baberabb](https://github.com/baberabb)in[#3546](https://github.com/EleutherAI/lm-evaluation-harness/pull/3546)

## New Contributors

[@HydrogenSulfate](https://github.com/HydrogenSulfate)made their first contribution in[#3535](https://github.com/EleutherAI/lm-evaluation-harness/pull/3535)[@UltimateJupiter](https://github.com/UltimateJupiter)made their first contribution in[#3545](https://github.com/EleutherAI/lm-evaluation-harness/pull/3545)[@enpimashin](https://github.com/enpimashin)made their first contribution in[#3543](https://github.com/EleutherAI/lm-evaluation-harness/pull/3543)[@chapsiru](https://github.com/chapsiru)made their first contribution in[#3470](https://github.com/EleutherAI/lm-evaluation-harness/pull/3470)[@chemwolf6922](https://github.com/chemwolf6922)made their first contribution in[#3565](https://github.com/EleutherAI/lm-evaluation-harness/pull/3565)[@plonerma](https://github.com/plonerma)made their first contribution in[#3496](https://github.com/EleutherAI/lm-evaluation-harness/pull/3496)[@hmellor](https://github.com/hmellor)made their first contribution in[#3573](https://github.com/EleutherAI/lm-evaluation-harness/pull/3573)[@Mr-Neutr0n](https://github.com/Mr-Neutr0n)made their first contribution in[#3567](https://github.com/EleutherAI/lm-evaluation-harness/pull/3567)[@LakshyaChaudhry](https://github.com/LakshyaChaudhry)made their first contribution in[#3574](https://github.com/EleutherAI/lm-evaluation-harness/pull/3574)

**Full Changelog**: `v0.4.10...v0.4.11`

## v0.4.10

## Highlights

The big change this release: the base package no longer installs model backends by default. We've also added new benchmarks and expanded multilingual support.

### Breaking Change: Lightweight Core with Optional Backends

** pip install lm_eval no longer installs the HuggingFace/torch stack by default.** (

[#3428](https://github.com/EleutherAI/lm-evaluation-harness/pull/3428))

The core package no longer includes backends. Install them explicitly:

```
pip install lm_eval # core only, no model backends
pip install lm_eval[hf] # HuggingFace backend (transformers, torch, accelerate)
pip install lm_eval[vllm] # vLLM backend
pip install lm_eval[api] # API backends (OpenAI, Anthropic, etc.)
```

**Additional breaking change:** Accessing model classes via attribute no longer works:

```
# This still works:
from lm_eval.models.huggingface import HFLM
# This now raises AttributeError:
import lm_eval.models
lm_eval.models.huggingface.HFLM
```

### CLI Refactor

The CLI now uses explicit subcommands and supports YAML config files ([#3440](https://github.com/EleutherAI/lm-evaluation-harness/pull/3440)):

```
lm-eval run --model hf --tasks hellaswag # run evaluations
lm-eval run --config my_config.yaml # load args from YAML config
lm-eval ls tasks # list available tasks
lm-eval validate --tasks hellaswag,arc_easy # validate task configs
```

Backward compatible when omitting `run`

still works: `lm-eval --model hf --tasks hellaswag`


See `lm-eval --help`

or the [CLI documentation](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/interface.md) for details.

### Other Improvements

**Decoupled**with new`ContextSampler`

`build_qa_turn`

helper ([#3429](https://github.com/EleutherAI/lm-evaluation-harness/pull/3429))**Normalized**with`gen_kwargs`

`truncation_side`

support for vLLM ([#3509](https://github.com/EleutherAI/lm-evaluation-harness/pull/3509))

## New Benchmarks & Tasks

**PISA**task by[@HallerPatrick](https://github.com/HallerPatrick)in[#3412](https://github.com/EleutherAI/lm-evaluation-harness/pull/3412)**SLR-Bench**(Scalable Logical Reasoning Benchmark) by[@Ahmad21Omar](https://github.com/Ahmad21Omar)in[#3305](https://github.com/EleutherAI/lm-evaluation-harness/pull/3305)**OpenAI Multilingual MMLU**by[@Helw150](https://github.com/Helw150)in[#3473](https://github.com/EleutherAI/lm-evaluation-harness/pull/3473)**ULQA**benchmark by[@keramjan](https://github.com/keramjan)in[#3340](https://github.com/EleutherAI/lm-evaluation-harness/pull/3340)**IFEval**in Spanish and Catalan by[@juliafalcao](https://github.com/juliafalcao)in[#3467](https://github.com/EleutherAI/lm-evaluation-harness/pull/3467)**TruthfulQA-VA**for Catalan by[@sgs97ua](https://github.com/sgs97ua)in[#3469](https://github.com/EleutherAI/lm-evaluation-harness/pull/3469)**Multiple Bangla benchmarks**by[@Ismail-Hossain-1](https://github.com/Ismail-Hossain-1)in[#3454](https://github.com/EleutherAI/lm-evaluation-harness/pull/3454)**NeurIPS E2LM Competition submissions**: Team Shaikespear, Morai, and Noor by[@younesbelkada](https://github.com/younesbelkada)in[#3437](https://github.com/EleutherAI/lm-evaluation-harness/pull/3437),[#3443](https://github.com/EleutherAI/lm-evaluation-harness/pull/3443),[#3444](https://github.com/EleutherAI/lm-evaluation-harness/pull/3444)

## Model Support

**Ministral-3**adapter (`hf-mistral3`

) by[@medhakimbedhief](https://github.com/medhakimbedhief)in[#3487](https://github.com/EleutherAI/lm-evaluation-harness/pull/3487)

## Fixes & Improvements

### Task Fixes

- Fixed leading whitespace leakage in
**MMLU-Pro**by[@baberabb](https://github.com/baberabb)in[#3500](https://github.com/EleutherAI/lm-evaluation-harness/pull/3500) - Fixed
`gen_prefix`

delimiter handling in multiple-choice tasks by[@baberabb](https://github.com/baberabb)in[#3508](https://github.com/EleutherAI/lm-evaluation-harness/pull/3508) - Fixed MGSM stop criteria in Iberian languages by
[@juliafalcao](https://github.com/juliafalcao)in[#3465](https://github.com/EleutherAI/lm-evaluation-harness/pull/3465) - Fixed
`a=0`

as valid answer index in`build_qa_turn`

by[@ezylopx5](https://github.com/ezylopx5)in[#3488](https://github.com/EleutherAI/lm-evaluation-harness/pull/3488) - Fixed
`fewshot_config`

not being applied to fewshot docs by[@baberabb](https://github.com/baberabb)in[#3461](https://github.com/EleutherAI/lm-evaluation-harness/pull/3461) - Updated GSM8K, WinoGrande, and SuperGLUE to use full HF dataset paths by
[@baberabb](https://github.com/baberabb)in[#3523](https://github.com/EleutherAI/lm-evaluation-harness/pull/3523),[#3525](https://github.com/EleutherAI/lm-evaluation-harness/pull/3525),[#3527](https://github.com/EleutherAI/lm-evaluation-harness/pull/3527) - Fixed
`gsm8k_cot_llama`

`target_delimiter`

issue by[@baberabb](https://github.com/baberabb)in[#3526](https://github.com/EleutherAI/lm-evaluation-harness/pull/3526) - Updated LIBRA task utils by
[@bond005](https://github.com/bond005)in[#3520](https://github.com/EleutherAI/lm-evaluation-harness/pull/3520)

### Backend Fixes

- Fixed vLLM off-by-one
`max_length`

error by[@baberabb](https://github.com/baberabb)in[#3503](https://github.com/EleutherAI/lm-evaluation-harness/pull/3503) - Resolved deprecated
`vllm.transformers_utils.get_tokenizer`

import by[@DarkLight1337](https://github.com/DarkLight1337)in[#3482](https://github.com/EleutherAI/lm-evaluation-harness/pull/3482) - Fixed SGLang import and removed duplicate tasks by
[@baberabb](https://github.com/baberabb)in[#3492](https://github.com/EleutherAI/lm-evaluation-harness/pull/3492) - Removed deprecated
`AutoModelForVision2Seq`

by[@baberabb](https://github.com/baberabb)in[#3522](https://github.com/EleutherAI/lm-evaluation-harness/pull/3522) - Fixed Anthropic chat model mapping by
[@lucafossen](https://github.com/lucafossen)in[#3453](https://github.com/EleutherAI/lm-evaluation-harness/pull/3453) - Fixed bug preventing
`=`

sign in checkpoint names by[@mrinaldi97](https://github.com/mrinaldi97)in[#3517](https://github.com/EleutherAI/lm-evaluation-harness/pull/3517) - Fixed
`pretty_print_task`

for external custom configs by[@safikhanSoofiyani](https://github.com/safikhanSoofiyani)in[#3436](https://github.com/EleutherAI/lm-evaluation-harness/pull/3436) - Fixed CLI regressions by
[@fxmarty-amd](https://github.com/fxmarty-amd)in[#3449](https://github.com/EleutherAI/lm-evaluation-harness/pull/3449)

## New Contributors

[@safikhanSoofiyani](https://github.com/safikhanSoofiyani)made their first contribution in[#3436](https://github.com/EleutherAI/lm-evaluation-harness/pull/3436)[@lucafossen](https://github.com/lucafossen)made their first contribution in[#3453](https://github.com/EleutherAI/lm-evaluation-harness/pull/3453)[@Ahmad21Omar](https://github.com/Ahmad21Omar)made their first contribution in[#3305](https://github.com/EleutherAI/lm-evaluation-harness/pull/3305)[@ezylopx5](https://github.com/ezylopx5)made their first contribution in[#3488](https://github.com/EleutherAI/lm-evaluation-harness/pull/3488)[@juliafalcao](https://github.com/juliafalcao)made their first contribution in[#3467](https://github.com/EleutherAI/lm-evaluation-harness/pull/3467)[@medhakimbedhief](https://github.com/medhakimbedhief)made their first contribution in[#3487](https://github.com/EleutherAI/lm-evaluation-harness/pull/3487)[@ntenenz](https://github.com/ntenenz)made their first contribution in[#3489](https://github.com/EleutherAI/lm-evaluation-harness/pull/3489)[@keramjan](https://github.com/keramjan)made their first contribution in[#3340](https://github.com/EleutherAI/lm-evaluation-harness/pull/3340)[@bond005](https://github.com/bond005)made their first contribution in[#3520](https://github.com/EleutherAI/lm-evaluation-harness/pull/3520)[@mrinaldi97](https://github.com/mrinaldi97)made their first contribution in[#3517](https://github.com/EleutherAI/lm-evaluation-harness/pull/3517)[@wogns3623](https://github.com/wogns3623)made their first contribution in[#3523](https://github.com/EleutherAI/lm-evaluation-harness/pull/3523)

**Full Changelog**: `v0.4.9.2...v0.4.10`

## lm-eval v0.4.9.2 Release Notes

This release continues our steady stream of community contributions with a batch of new benchmarks, expanded model support, and important fixes. A notable change: **Python 3.10 is now the minimum required version**.

### New Benchmarks & Tasks

A big wave of new evaluation tasks this release:

**AIME**and**MATH500**math reasoning benchmarks by[@jannalulu](https://github.com/jannalulu)in[#3248](https://github.com/EleutherAI/lm-evaluation-harness/pull/3248),[#3311](https://github.com/EleutherAI/lm-evaluation-harness/pull/3311)**BabiLong**and**Longbench v2**for long-context evaluation by[@jannalulu](https://github.com/jannalulu)in[#3287](https://github.com/EleutherAI/lm-evaluation-harness/pull/3287),[#3338](https://github.com/EleutherAI/lm-evaluation-harness/pull/3338)**GraphWalks**by[@jannalulu](https://github.com/jannalulu)in[#3377](https://github.com/EleutherAI/lm-evaluation-harness/pull/3377)**ZhoBLiMP**,**BLiMP-NL**,**TurBLiMP**,**LM-SynEval**, and**BHS**linguistic benchmarks by[@jmichaelov](https://github.com/jmichaelov)in[#3218](https://github.com/EleutherAI/lm-evaluation-harness/pull/3218),[#3221](https://github.com/EleutherAI/lm-evaluation-harness/pull/3221),[#3219](https://github.com/EleutherAI/lm-evaluation-harness/pull/3219),[#3184](https://github.com/EleutherAI/lm-evaluation-harness/pull/3184),[#3265](https://github.com/EleutherAI/lm-evaluation-harness/pull/3265)**Icelandic WinoGrande**by[@jmichaelov](https://github.com/jmichaelov)in[#3277](https://github.com/EleutherAI/lm-evaluation-harness/pull/3277)**CLIcK**Korean benchmark by[@shing100](https://github.com/shing100)in[#3173](https://github.com/EleutherAI/lm-evaluation-harness/pull/3173)**MMLU-Redux**(generative) and Spanish translation by[@luiscosio](https://github.com/luiscosio)in[#2705](https://github.com/EleutherAI/lm-evaluation-harness/pull/2705)**EsBBQ**and**CaBBQ**bias benchmarks by[@valleruizf](https://github.com/valleruizf)in[#3167](https://github.com/EleutherAI/lm-evaluation-harness/pull/3167)**EQBench**in Spanish and Catalan by[@priverabsc](https://github.com/priverabsc)in[#3168](https://github.com/EleutherAI/lm-evaluation-harness/pull/3168)**Anthropic discrim-eval**by[@Helw150](https://github.com/Helw150)in[#3091](https://github.com/EleutherAI/lm-evaluation-harness/pull/3091)**XNLI-VA**by[@FranValero97](https://github.com/FranValero97)in[#3194](https://github.com/EleutherAI/lm-evaluation-harness/pull/3194)**Bangla MMLU**(Titulm) by[@Ismail-Hossain-1](https://github.com/Ismail-Hossain-1)in[#3317](https://github.com/EleutherAI/lm-evaluation-harness/pull/3317)**HumanEval infilling**by[@its-alpesh](https://github.com/its-alpesh)in[#3299](https://github.com/EleutherAI/lm-evaluation-harness/pull/3299)**CNN-DailyMail 3.0.0**by[@preordinary](https://github.com/preordinary)in[#3426](https://github.com/EleutherAI/lm-evaluation-harness/pull/3426)**Global PIQA**and new`acc_norm_bytes`

metric by[@baberabb](https://github.com/baberabb)in[#3368](https://github.com/EleutherAI/lm-evaluation-harness/pull/3368)

### Fixes & Improvements

**Core Changes:**

**Python 3.10 minimum**by[@jannalulu](https://github.com/jannalulu)in[#3337](https://github.com/EleutherAI/lm-evaluation-harness/pull/3337)**Unpinned**library by`datasets`

[@baberabb](https://github.com/baberabb)in[#3316](https://github.com/EleutherAI/lm-evaluation-harness/pull/3316)**BOS token handling**: Delegate to tokenizer;`add_bos_token`

now defaults to`None`

by[@baberabb](https://github.com/baberabb)in[#3347](https://github.com/EleutherAI/lm-evaluation-harness/pull/3347)- Renamed
`LOGLEVEL`

env var to`LMEVAL_LOG_LEVEL`

to avoid conflicts by[@fxmarty-amd](https://github.com/fxmarty-amd)in[#3418](https://github.com/EleutherAI/lm-evaluation-harness/pull/3418) - Resolve duplicate task names with safeguards by
[@giuliolovisotto](https://github.com/giuliolovisotto)in[#3394](https://github.com/EleutherAI/lm-evaluation-harness/pull/3394)

**Task Fixes:**

- Fixed MMLU-Redux to exclude samples without
`error_type="ok"`

and display summary table by[@fxmarty-amd](https://github.com/fxmarty-amd)in[#3410](https://github.com/EleutherAI/lm-evaluation-harness/pull/3410),[#3406](https://github.com/EleutherAI/lm-evaluation-harness/pull/3406) - Fixed AIME answer extraction by
[@jannalulu](https://github.com/jannalulu)in[#3353](https://github.com/EleutherAI/lm-evaluation-harness/pull/3353) - Fixed LongBench evaluation and group handling by
[@TimurAysin](https://github.com/TimurAysin),[@jannalulu](https://github.com/jannalulu)in[#3273](https://github.com/EleutherAI/lm-evaluation-harness/pull/3273),[#3359](https://github.com/EleutherAI/lm-evaluation-harness/pull/3359),[#3361](https://github.com/EleutherAI/lm-evaluation-harness/pull/3361) - Fixed
`crows_pairs`

dataset by[@jannalulu](https://github.com/jannalulu)in[#3378](https://github.com/EleutherAI/lm-evaluation-harness/pull/3378) - Fixed Gemma tokenizer
`add_bos_token`

not updating by[@DarkLight1337](https://github.com/DarkLight1337)in[#3206](https://github.com/EleutherAI/lm-evaluation-harness/pull/3206) - Fixed
`lambada_multilingual_stablelm`

by[@jmichaelov](https://github.com/jmichaelov),[@HallerPatrick](https://github.com/HallerPatrick)in[#3294](https://github.com/EleutherAI/lm-evaluation-harness/pull/3294),[#3222](https://github.com/EleutherAI/lm-evaluation-harness/pull/3222) - Fixed CodeXGLUE by
[@gsaltintas](https://github.com/gsaltintas)in[#3238](https://github.com/EleutherAI/lm-evaluation-harness/pull/3238) - Pinned correct MMLUSR version by
[@christinaexyou](https://github.com/christinaexyou)in[#3350](https://github.com/EleutherAI/lm-evaluation-harness/pull/3350) - Updated
`minerva_math`

by[@baberabb](https://github.com/baberabb)in[#3259](https://github.com/EleutherAI/lm-evaluation-harness/pull/3259)

**Backend Fixes:**

- Fixed vLLM import errors when not installed by
[@fxmarty-amd](https://github.com/fxmarty-amd)in[#3292](https://github.com/EleutherAI/lm-evaluation-harness/pull/3292) - Fixed vLLM
`data_parallel_size>1`

issue by[@Dornavineeth](https://github.com/Dornavineeth)in[#3303](https://github.com/EleutherAI/lm-evaluation-harness/pull/3303) - Resolved deprecated
`vllm.utils.get_open_port`

by[@DarkLight1337](https://github.com/DarkLight1337)in[#3398](https://github.com/EleutherAI/lm-evaluation-harness/pull/3398) - Fixed GPT series model bugs by
[@zinccat](https://github.com/zinccat)in[#3348](https://github.com/EleutherAI/lm-evaluation-harness/pull/3348) - Fixed PIL image hashing to use actual bytes by
[@tboerstad](https://github.com/tboerstad)in[#3331](https://github.com/EleutherAI/lm-evaluation-harness/pull/3331) - Fixed
`additional_config`

parsing by[@brian-dellabetta](https://github.com/brian-dellabetta)in[#3393](https://github.com/EleutherAI/lm-evaluation-harness/pull/3393) - Fixed batch chunking seed handling with groupby by
[@slimfrkha](https://github.com/slimfrkha)in[#3047](https://github.com/EleutherAI/lm-evaluation-harness/pull/3047) - Fixed no-output error handling by
[@Oseltamivir](https://github.com/Oseltamivir)in[#3395](https://github.com/EleutherAI/lm-evaluation-harness/pull/3395) - Replaced deprecated
`torch_dtype`

with`dtype`

by[@AbdulmalikDS](https://github.com/AbdulmalikDS)in[#3415](https://github.com/EleutherAI/lm-evaluation-harness/pull/3415) - Fixed custom task config reading by
[@SkyR0ver](https://github.com/SkyR0ver)in[#3425](https://github.com/EleutherAI/lm-evaluation-harness/pull/3425)

### Model & Backend Support

**OpenAI GPT-5**support by[@babyplutokurt](https://github.com/babyplutokurt)in[#3247](https://github.com/EleutherAI/lm-evaluation-harness/pull/3247)**Azure OpenAI**support by[@zinccat](https://github.com/zinccat)in[#3349](https://github.com/EleutherAI/lm-evaluation-harness/pull/3349)**Fine-tuned Gemma3**evaluation support by[@LearnerSXH](https://github.com/LearnerSXH)in[#3234](https://github.com/EleutherAI/lm-evaluation-harness/pull/3234)**OpenVINO text2text**models by[@nikita-savelyevv](https://github.com/nikita-savelyevv)in[#3101](https://github.com/EleutherAI/lm-evaluation-harness/pull/3101)**Intel XPU**support for HFLM by[@kaixuanliu](https://github.com/kaixuanliu)in[#3211](https://github.com/EleutherAI/lm-evaluation-harness/pull/3211)**Attention head steering**support by[@luciaquirke](https://github.com/luciaquirke)in[#3279](https://github.com/EleutherAI/lm-evaluation-harness/pull/3279)- Leverage vLLM's
`tokenizer_info`

endpoint to avoid manual duplication by[@m-misiura](https://github.com/m-misiura)in[#3185](https://github.com/EleutherAI/lm-evaluation-harness/pull/3185)

## What's Changed

- Remove
`trust_remote_code: True`

from updated datasets by[@Avelina9X](https://github.com/Avelina9X)in[#3213](https://github.com/EleutherAI/lm-evaluation-harness/pull/3213) - Add support for evaluating with fine-tuned Gemma3 by
[@LearnerSXH](https://github.com/LearnerSXH)in[#3234](https://github.com/EleutherAI/lm-evaluation-harness/pull/3234) - Fix
`add_bos_token`

not updated for Gemma tokenizer by[@DarkLight1337](https://github.com/DarkLight1337)in[#3206](https://github.com/EleutherAI/lm-evaluation-harness/pull/3206) - remove incomplete compilation instructions, solves
[#3233](https://github.com/EleutherAI/lm-evaluation-harness/issues/3233)by[@ceferisbarov](https://github.com/ceferisbarov)in[#3242](https://github.com/EleutherAI/lm-evaluation-harness/pull/3242) - Update utils.py by
[@Anri-Lombard](https://github.com/Anri-Lombard)in[#3246](https://github.com/EleutherAI/lm-evaluation-harness/pull/3246) - Adding support for OpenAI GPT-5 model by
[@babyplutokurt](https://github.com/babyplutokurt)in[#3247](https://github.com/EleutherAI/lm-evaluation-harness/pull/3247) - Add xnli_va dataset by
[@FranValero97](https://github.com/FranValero97)in[#3194](https://github.com/EleutherAI/lm-evaluation-harness/pull/3194) - Add ZhoBLiMP benchmark by
[@jmichaelov](https://github.com/jmichaelov)in[#3218](https://github.com/EleutherAI/lm-evaluation-harness/pull/3218) - Add BLiMP-NL by
[@jmichaelov](https://github.com/jmichaelov)in[#3221](https://github.com/EleutherAI/lm-evaluation-harness/pull/3221) - Add TurBLiMP by
[@jmichaelov](https://github.com/jmichaelov)in[#3219](https://github.com/EleutherAI/lm-evaluation-harness/pull/3219) - Add LM-SynEval Benchmark by
[@jmichaelov](https://github.com/jmichaelov)in[#3184](https://github.com/EleutherAI/lm-evaluation-harness/pull/3184) - Fix unknown group key to tag in yaml config for
`lambada_multilingual_stablelm`

by[@HallerPatrick](https://github.com/HallerPatrick)in[#3222](https://github.com/EleutherAI/lm-evaluation-harness/pull/3222) - update
`minerva_math`

by[@baberabb](https://github.com/baberabb)in[#3259](https://github.com/EleutherAI/lm-evaluation-harness/pull/3259) - feat: Add CLIcK task by
[@shing100](https://github.com/shing100)in[#3173](https://github.com/EleutherAI/lm-evaluation-harness/pull/3173) - Adds Anthropic/discrim-eval to lm-evaluation-harness by
[@Helw150](https://github.com/Helw150)in[#3091](https://github.com/EleutherAI/lm-evaluation-harness/pull/3091) - Add support for OpenVINO text2text generation models by
[@nikita-savelyevv](https://github.com/nikita-savelyevv)in[#3101](https://github.com/EleutherAI/lm-evaluation-harness/pull/3101) - Update MMLU-ProX task by
[@weihao1115](https://github.com/weihao1115)in[#3174](https://github.com/EleutherAI/lm-evaluation-harness/pull/3174) - Support for AIME dataset by
[@jannalulu](https://github.com/jannalulu)in[#3248](https://github.com/EleutherAI/lm-evaluation-harness/pull/3248) - feat(scrolls): delete chat_template from kwargs by
[@slimfrkha](https://github.com/slimfrkha)in[#3267](https://github.com/EleutherAI/lm-evaluation-harness/pull/3267) - pacify pre-commit by
[@baberabb](https://github.com/baberabb)in[#3268](https://github.com/EleutherAI/lm-evaluation-harness/pull/3268) - Fix codexglue by
[@gsaltintas](https://github.com/gsaltintas)in[#3238](https://github.com/EleutherAI/lm-evaluation-harness/pull/3238) - Add BHS benchmark by
[@jmichaelov](https://github.com/jmichaelov)in[#3265](https://github.com/EleutherAI/lm-evaluation-harness/pull/3265) - Add
`acc_norm`

metric to BLiMP-NL by[@jmichaelov](https://github.com/jmichaelov)in[#3272](https://github.com/EleutherAI/lm-evaluation-harness/pull/3272) - Add
`acc_norm`

metric to ZhoBLiMP by[@jmichaelov](https://github.com/jmichaelov)in[#3271](https://github.com/EleutherAI/lm-evaluation-harness/pull/3271) - Add EsBBQ and CaBBQ tasks by
[@valleruizf](https://github.com/valleruizf)in[#3167](https://github.com/EleutherAI/lm-evaluation-harness/pull/3167) - Add support for steering individual attention heads by
[@luciaquirke](https://github.com/luciaquirke)in[#3279](https://github.com/EleutherAI/lm-evaluation-harness/pull/3279) - Add the Icelandic WinoGrande benchmark by
[@jmichaelov](https://github.com/jmichaelov)in[#3277](https://github.com/EleutherAI/lm-evaluation-harness/pull/3277) - Ignore seed when splitting batch in chunks with groupby by
[@slimfrkha](https://github.com/slimfrkha)in[#3047](https://github.com/EleutherAI/lm-evaluation-harness/pull/3047) - [fix][vllm] Avoid import errors in case vllm is not installed by
[@fxmarty-amd](https://github.com/fxmarty-amd)in[#3292](https://github.com/EleutherAI/lm-evaluation-harness/pull/3292) - Fix LongBench Evaluation by
[@TimurAysin](https://github.com/TimurAysin)in[#3273](https://github.com/EleutherAI/lm-evaluation-harness/pull/3273) - add intel xpu support for HFLM by
[@kaixuanliu](https://github.com/kaixuanliu)in[#3211](https://github.com/EleutherAI/lm-evaluation-harness/pull/3211) - feat: Add mmlu-redux and it's spanish transaltion as generative task definitions by
[@luiscosio](https://github.com/luiscosio)in[#2705](https://github.com/EleutherAI/lm-evaluation-harness/pull/2705) - Add BabiLong by
[@jannalulu](https://github.com/jannalulu)in[#3287](https://github.com/EleutherAI/lm-evaluation-harness/pull/3287) - Add AIME to task description by
[@jannalulu](https://github.com/jannalulu)in[#3296](https://github.com/EleutherAI/lm-evaluation-harness/pull/3296) - Add humaneval_infilling task by
[@its-alpesh](https://github.com/its-alpesh)in[#3299](https://github.com/EleutherAI/lm-evaluation-harness/pull/3299) - Add eqbench tasks in Spanish and Catalan by
[@priverabsc](https://github.com/priverabsc)in[#3168](https://github.com/EleutherAI/lm-evaluation-harness/pull/3168) - [fix] add math and longbench to test dependencies by
[@jannalulu](https://github.com/jannalulu)in[#3321](https://github.com/EleutherAI/lm-evaluation-harness/pull/3321) - Fix: VLLM model when data_parallel_size>1 by
[@Dornavineeth](https://github.com/Dornavineeth)in[#3303](https://github.com/EleutherAI/lm-evaluation-harness/pull/3303) - unpin datasets; update pre-commit by
[@baberabb](https://github.com/baberabb)in[#3316](https://github.com/EleutherAI/lm-evaluation-harness/pull/3316) - bump to python 3.10 by
[@jannalulu](https://github.com/jannalulu)in[#3337](https://github.com/EleutherAI/lm-evaluation-harness/pull/3337) - Longbench v2 by
[@jannalulu](https://github.com/jannalulu)in[#3338](https://github.com/EleutherAI/lm-evaluation-harness/pull/3338) - Leverage vllm's
`tokenizer_info`

endpoint to avoid manual duplication by[@m-misiura](https://github.com/m-misiura)in[#3185](https://github.com/EleutherAI/lm-evaluation-harness/pull/3185) - Add support for Titulm Bangla MMLU dataset by
[@Ismail-Hossain-1](https://github.com/Ismail-Hossain-1)in[#3317](https://github.com/EleutherAI/lm-evaluation-harness/pull/3317) - remove duplicate tags/groups by
[@baberabb](https://github.com/baberabb)in[#3343](https://github.com/EleutherAI/lm-evaluation-harness/pull/3343) - Align
`humaneval_64_instruct`

task label in README to name in yaml file by[@jmichaelov](https://github.com/jmichaelov)in[#3344](https://github.com/EleutherAI/lm-evaluation-harness/pull/3344) - Fixes bugs when using gpt series model by
[@zinccat](https://github.com/zinccat)in[#3348](https://github.com/EleutherAI/lm-evaluation-harness/pull/3348) - [fix] aime doesn't extract answers by
[@jannalulu](https://github.com/jannalulu)in[#3353](https://github.com/EleutherAI/lm-evaluation-harness/pull/3353) - add global_piqa; add acc_norm_bytes metric by
[@baberabb](https://github.com/baberabb)in[#3368](https://github.com/EleutherAI/lm-evaluation-harness/pull/3368) - [fix] crows_pairs dataset by
[@jannalulu](https://github.com/jannalulu)in[#3378](https://github.com/EleutherAI/lm-evaluation-harness/pull/3378) - Fix issue 3355 assertion error by
[@marksverdhei](https://github.com/marksverdhei)in[#3356](https://github.com/EleutherAI/lm-evaluation-harness/pull/3356) - fix(gsm8k): align README to yaml file by
[@neoheartbeats](https://github.com/neoheartbeats)in[#3388](https://github.com/EleutherAI/lm-evaluation-harness/pull/3388) - added azure openai support by
[@zinccat](https://github.com/zinccat)in[#3349](https://github.com/EleutherAI/lm-evaluation-harness/pull/3349) - Delegate BOS to the tokenizer;
`add_bos_token`

defaults to`None`

by[@baberabb](https://github.com/baberabb)in[#3347](https://github.com/EleutherAI/lm-evaluation-harness/pull/3347) - fix trust...

[Read more](https://github.com/EleutherAI/lm-evaluation-harness/releases/tag/v0.4.9.2)

## v0.4.9.1

# lm-eval v0.4.9.1 Release Notes

This v0.4.9.1 release is a quick patch to bring in some new tasks and fixes. Looking aheas, we're gearing up for some bigger updates to tackle common community pain points. We'll do our best to keep things from breaking, but we anticipate a few changes might not be fully backward-compatible. We're excited to share more soon!

### Enhanced Reasoning Model Handling

- Better support for reasoning models with a
`think_end_token`

argument to strip intermediate reasoning from outputs for the`hf`

,`vllm`

, and`sglang`

model backends. A related`enable_thinking`

argument was also added for specific models that support it (e.g., Qwen).

## New Benchmarks & Tasks

- EgyMMLU and EgyHellaSwag by
[@houdaipha](https://github.com/houdaipha)in[#3063](https://github.com/EleutherAI/lm-evaluation-harness/pull/3063) - MultiBLiMP benchmark by
[@jmichaelov](https://github.com/jmichaelov)in[#3155](https://github.com/EleutherAI/lm-evaluation-harness/pull/3155) - LIBRA benchmark for long-context evaluation by
[@karimovaSvetlana](https://github.com/karimovaSvetlana)in[#2943](https://github.com/EleutherAI/lm-evaluation-harness/pull/2943) - Multilingual Truthfulqa in Spanish, Basque and Galician by
[@BlancaCalvo](https://github.com/BlancaCalvo)in[#3062](https://github.com/EleutherAI/lm-evaluation-harness/pull/3062)

## Fixes & Improvements

### Tasks & Benchmarks:

- Aligned Humaneval results for Llama-3.1-70B-Instruct with official scores by
[@userljz](https://github.com/userljz),[@baberabb](https://github.com/baberabb),[@idantene](https://github.com/idantene)in ([#3201](https://github.com/EleutherAI/lm-evaluation-harness/pull/3201).[#3092](https://github.com/EleutherAI/lm-evaluation-harness/pull/3092),[#3102](https://github.com/EleutherAI/lm-evaluation-harness/pull/3102)) - Fixed incorrect dataset paths for GLUE and medical benchmarks by
[@Avelina9X](https://github.com/Avelina9X)and[@idantene](https://github.com/idantene). ([#3159](https://github.com/EleutherAI/lm-evaluation-harness/pull/3159),[#3151](https://github.com/EleutherAI/lm-evaluation-harness/pull/3151)) - Removed redundant "Let's think step by step" text from
`bbh_cot_fewshot`

prompts by[@philipdoldo](https://github.com/philipdoldo). ([#3140](https://github.com/EleutherAI/lm-evaluation-harness/pull/3140)) - Increased
`max_gen_toks`

to 2048 for HRM8K math benchmarks by[@shing100](https://github.com/shing100). ([#3124](https://github.com/EleutherAI/lm-evaluation-harness/pull/3124))

### Backend & Stability:

- Reduce CLI loading time from 2.2s to 0.05s by
[@stakodiak](https://github.com/stakodiak). ([#3099](https://github.com/EleutherAI/lm-evaluation-harness/pull/3099)) - Fixed a process hang caused by mp.Pool in bootstrap_stderr and introduced
`DISABLE_MULTIPROC`

envar by[@ankitgola005](https://github.com/ankitgola005)and[@neel04](https://github.com/neel04). ([#3135](https://github.com/EleutherAI/lm-evaluation-harness/pull/3135),[#3106](https://github.com/EleutherAI/lm-evaluation-harness/pull/3106)) - add image hashing and
`LMEVAL_HASHMM`

envar by[@artemorloff](https://github.com/artemorloff)in[#2973](https://github.com/EleutherAI/lm-evaluation-harness/pull/2973) - TaskManager:
`include-path`

precedence handling to prioritize custom dir over default by[@parkhs21](https://github.com/parkhs21)in[#3068](https://github.com/EleutherAI/lm-evaluation-harness/pull/3068)

## Housekeeping:

- Pinned
`datasets < 4.0.0`

temporarily to maintain compatibility with`trust_remote_code`

by[@baberabb](https://github.com/baberabb). ([#3172](https://github.com/EleutherAI/lm-evaluation-harness/pull/3172)) - Removed models from Neural Magic and other unneeded files by
[@baberabb](https://github.com/baberabb). ([#3112](https://github.com/EleutherAI/lm-evaluation-harness/pull/3112),[#3113](https://github.com/EleutherAI/lm-evaluation-harness/pull/3113),[#3108](https://github.com/EleutherAI/lm-evaluation-harness/pull/3108))

## What's Changed

- llama3 task: update README.md by
[@annafontanaa](https://github.com/annafontanaa)in[#3074](https://github.com/EleutherAI/lm-evaluation-harness/pull/3074) - Fix Anthropic API compatibility issues in chat completions by
[@NourFahmy](https://github.com/NourFahmy)in[#3054](https://github.com/EleutherAI/lm-evaluation-harness/pull/3054) - Ensure backwards compatibility in
`fewshot_context`

by using kwargs by[@kiersten-stokes](https://github.com/kiersten-stokes)in[#3079](https://github.com/EleutherAI/lm-evaluation-harness/pull/3079) - [vllm] remove system message if
`TemplateError`

for chat_template by[@baberabb](https://github.com/baberabb)in[#3076](https://github.com/EleutherAI/lm-evaluation-harness/pull/3076) - feat / fix: Properly make use of
`subfolder`

from HF models by[@younesbelkada](https://github.com/younesbelkada)in[#3072](https://github.com/EleutherAI/lm-evaluation-harness/pull/3072) - [HF] fix quantization config by
[@baberabb](https://github.com/baberabb)in[#3039](https://github.com/EleutherAI/lm-evaluation-harness/pull/3039) - FixBug: Align the Humaneval with official results for Llama-3.1-70B-Instruct by
[@userljz](https://github.com/userljz)in[#3092](https://github.com/EleutherAI/lm-evaluation-harness/pull/3092) - Truthfulqa multi harness by
[@BlancaCalvo](https://github.com/BlancaCalvo)in[#3062](https://github.com/EleutherAI/lm-evaluation-harness/pull/3062) - Fix: Reduce CLI loading time from 2.2s to 0.05s by
[@stakodiak](https://github.com/stakodiak)in[#3099](https://github.com/EleutherAI/lm-evaluation-harness/pull/3099) - Humaneval - fix regression by
[@baberabb](https://github.com/baberabb)in[#3102](https://github.com/EleutherAI/lm-evaluation-harness/pull/3102) - Bugfix/hf tokenizer gguf override by
[@ankush13r](https://github.com/ankush13r)in[#3098](https://github.com/EleutherAI/lm-evaluation-harness/pull/3098) - [FIX] Initial code to disable multi-proc for stderr by
[@neel04](https://github.com/neel04)in[#3106](https://github.com/EleutherAI/lm-evaluation-harness/pull/3106) - fix deps; update hooks by
[@baberabb](https://github.com/baberabb)in[#3107](https://github.com/EleutherAI/lm-evaluation-harness/pull/3107) - delete unneeded files by
[@baberabb](https://github.com/baberabb)in[#3108](https://github.com/EleutherAI/lm-evaluation-harness/pull/3108) - Fixed
[#3005](https://github.com/EleutherAI/lm-evaluation-harness/issues/3005): Processes both formats of model_args: string and dictionay by[@DebjyotiRay](https://github.com/DebjyotiRay)in[#3097](https://github.com/EleutherAI/lm-evaluation-harness/pull/3097) - add image hashing and
`LMEVAL_HASHMM`

envar by[@artemorloff](https://github.com/artemorloff)in[#2973](https://github.com/EleutherAI/lm-evaluation-harness/pull/2973) - removal of Neural Magic models by
[@baberabb](https://github.com/baberabb)in[#3112](https://github.com/EleutherAI/lm-evaluation-harness/pull/3112) - Neuralmagic by
[@baberabb](https://github.com/baberabb)in[#3113](https://github.com/EleutherAI/lm-evaluation-harness/pull/3113) - check pil dep when hashing images by
[@baberabb](https://github.com/baberabb)in[#3114](https://github.com/EleutherAI/lm-evaluation-harness/pull/3114) - warning for "chat" pretrained; disable buggy evalita configs by
[@baberabb](https://github.com/baberabb)in[#3127](https://github.com/EleutherAI/lm-evaluation-harness/pull/3127) - fix: remove warning by
[@baberabb](https://github.com/baberabb)in[#3128](https://github.com/EleutherAI/lm-evaluation-harness/pull/3128) - Adding EgyMMLU and EgyHellaSwag by
[@houdaipha](https://github.com/houdaipha)in[#3063](https://github.com/EleutherAI/lm-evaluation-harness/pull/3063) - Added mixed_precision_dtype argument to HFLM to enable autocasting by
[@Avelina9X](https://github.com/Avelina9X)in[#3138](https://github.com/EleutherAI/lm-evaluation-harness/pull/3138) - Fix for hang due to mp.Pool in bootstrap_stderr by
[@ankitgola005](https://github.com/ankitgola005)in[#3135](https://github.com/EleutherAI/lm-evaluation-harness/pull/3135) - when using vllm with lora, it will have some mistakes, now i fix it. by
[@Jacky-MYQ](https://github.com/Jacky-MYQ)in[#3132](https://github.com/EleutherAI/lm-evaluation-harness/pull/3132) - truncate thinking tags in generations by
[@baberabb](https://github.com/baberabb)in[#3145](https://github.com/EleutherAI/lm-evaluation-harness/pull/3145) `bbh_cot_fewshot`

: Removed repeated "Let''s think step by step." text from bbh cot prompts by[@philipdoldo](https://github.com/philipdoldo)in[#3140](https://github.com/EleutherAI/lm-evaluation-harness/pull/3140)- Fix medical benchmarks import by
[@idantene](https://github.com/idantene)in[#3151](https://github.com/EleutherAI/lm-evaluation-harness/pull/3151) - fix request hanging when request api by
[@mmmans](https://github.com/mmmans)in[#3090](https://github.com/EleutherAI/lm-evaluation-harness/pull/3090) - Custom request headers | trust_remote_code param fix by
[@RawthiL](https://github.com/RawthiL)in[#3069](https://github.com/EleutherAI/lm-evaluation-harness/pull/3069) - Bugfix: update path for GLUE by
[@Avelina9X](https://github.com/Avelina9X)in[#3159](https://github.com/EleutherAI/lm-evaluation-harness/pull/3159) - Add the MultiBLiMP benchmark by
[@jmichaelov](https://github.com/jmichaelov)in[#3155](https://github.com/EleutherAI/lm-evaluation-harness/pull/3155) - multiblimp - readme by
[@baberabb](https://github.com/baberabb)in[#3162](https://github.com/EleutherAI/lm-evaluation-harness/pull/3162) - [tests] Added missing fixture in test_unitxt_tasks.py by
[@Avelina9X](https://github.com/Avelina9X)in[#3163](https://github.com/EleutherAI/lm-evaluation-harness/pull/3163) - Fix: extended to max_gen_toks 2048 for HRM8K math benchmarks by
[@shing100](https://github.com/shing100)in[#3124](https://github.com/EleutherAI/lm-evaluation-harness/pull/3124) - feat: Add LIBRA benchmark for long-context evaluation by
[@karimovaSvetlana](https://github.com/karimovaSvetlana)in[#2943](https://github.com/EleutherAI/lm-evaluation-harness/pull/2943) - Added
`chat_template_args`

to vllm by[@Avelina9X](https://github.com/Avelina9X)in[#3164](https://github.com/EleutherAI/lm-evaluation-harness/pull/3164) - Pin datasets < 4.0.0 by
[@baberabb](https://github.com/baberabb)in[#3172](https://github.com/EleutherAI/lm-evaluation-harness/pull/3172) - Remove "device" from vllm_causallms.py by
[@mgoin](https://github.com/mgoin)in[#3176](https://github.com/EleutherAI/lm-evaluation-harness/pull/3176) - remove trust-remote-code in configs; fix escape sequences by
[@baberabb](https://github.com/baberabb)in[#3180](https://github.com/EleutherAI/lm-evaluation-harness/pull/3180) - Fix vllm test issue that call pop() from None by
[@weireweire](https://github.com/weireweire)in[#3182](https://github.com/EleutherAI/lm-evaluation-harness/pull/3182) - [hotfix] vllm: pop
`device`

from kwargs by[@baberabb](https://github.com/baberabb)in[#3181](https://github.com/EleutherAI/lm-evaluation-harness/pull/3181) - Update vLLM compatibility by
[@DarkLight1337](https://github.com/DarkLight1337)in[#3024](https://github.com/EleutherAI/lm-evaluation-harness/pull/3024) - Fix
`mmlu_continuation`

subgroup names to fit Readme and other variants by[@lamalunderscore](https://github.com/lamalunderscore)in[#3137](https://github.com/EleutherAI/lm-evaluation-harness/pull/3137) - Fix humaneval_instruct by
[@idantene](https://github.com/idantene)in[#3201](https://github.com/EleutherAI/lm-evaluation-harness/pull/3201) - Update README.md for mlqa by
[@newme616](https://github.com/newme616)in[#3117](https://github.com/EleutherAI/lm-evaluation-harness/pull/3117) - improve include-path precedence handling by
[@parkhs21](https://github.com/parkhs21)in[#3068](https://github.com/EleutherAI/lm-evaluation-harness/pull/3068) - Bump version to 0.4.9.1 by
[@baberabb](https://github.com/baberabb)in[#3208](https://github.com/EleutherAI/lm-evaluation-harness/pull/3208)

## New Contributors

[@NourFahmy](https://github.com/NourFahmy)made their first contribution in[#3054](https://github.com/EleutherAI/lm-evaluation-harness/pull/3054)[@userljz](https://github.com/userljz)made their first contribution in[#3092](https://github.com/EleutherAI/lm-evaluation-harness/pull/3092)[@BlancaCalvo](https://github.com/BlancaCalvo)made their first contribution in[#3062](https://github.com/EleutherAI/lm-evaluation-harness/pull/3062)[@stakodiak](https://github.com/stakodiak)made their first contribution in[#3099](https://github.com/EleutherAI/lm-evaluation-harness/pull/3099)[@ankush13r](https://github.com/ankush13r)made their first contribution in[#3098](https://github.com/EleutherAI/lm-evaluation-harness/pull/3098)[@neel04](https://github.com/neel04)made their first contribution in https://...

[Read more](https://github.com/EleutherAI/lm-evaluation-harness/releases/tag/v0.4.9.1)

## v0.4.9

# lm-eval v0.4.9 Release Notes

## Key Improvements

-
**Enhanced Backend Support**:**SGLang Generate API**byin[@baberabb](https://github.com/baberabb)[#2997](https://github.com/EleutherAI/lm-evaluation-harness/pull/2997)**vLLM enhancements**: Added support for`enable_thinking`

argument ([#2947](https://github.com/EleutherAI/lm-evaluation-harness/pull/2947)) and data parallel for V1 ([#3011](https://github.com/EleutherAI/lm-evaluation-harness/pull/3011)) byand[@anmarques](https://github.com/anmarques)[@baberabb](https://github.com/baberabb)**Chat template improvements**: Extended vLLM chat template support ([#2902](https://github.com/EleutherAI/lm-evaluation-harness/pull/2902)) and fixed HF chat template resolution ([#2992](https://github.com/EleutherAI/lm-evaluation-harness/pull/2992)) byand[@anmarques](https://github.com/anmarques)[@fxmarty-amd](https://github.com/fxmarty-amd)

-
**Multimodal Capabilities**:**Audio modality support**for Qwen2 Audio models byin[@artemorloff](https://github.com/artemorloff)[#2689](https://github.com/EleutherAI/lm-evaluation-harness/pull/2689)**Image processing improvements**: Added resize images support ([#2958](https://github.com/EleutherAI/lm-evaluation-harness/pull/2958)) and enabled multimodal API usage ([#2981](https://github.com/EleutherAI/lm-evaluation-harness/pull/2981)) byand[@artemorloff](https://github.com/artemorloff)[@baberabb](https://github.com/baberabb)**ChartQA**multimodal task implementation byin[@baberabb](https://github.com/baberabb)[#2544](https://github.com/EleutherAI/lm-evaluation-harness/pull/2544)

-
**Performance & Reliability**:**Quantization support**added via`quantization_config`

byin[@jerryzh168](https://github.com/jerryzh168)[#2842](https://github.com/EleutherAI/lm-evaluation-harness/pull/2842)**Memory optimization**: Use`yaml.CLoader`

for faster YAML loading byin[@giuliolovisotto](https://github.com/giuliolovisotto)[#2777](https://github.com/EleutherAI/lm-evaluation-harness/pull/2777)**Bug fixes**: Resolved MMLU generative metric aggregation ([#2761](https://github.com/EleutherAI/lm-evaluation-harness/pull/2761)) and context length handling issues ([#2972](https://github.com/EleutherAI/lm-evaluation-harness/pull/2972))


## New Benchmarks & Tasks

**Code Evaluation**

**HumanEval Instruct**- Instruction-following code generation benchmark byin[@baberabb](https://github.com/baberabb)[#2650](https://github.com/EleutherAI/lm-evaluation-harness/pull/2650)**MBPP Instruct**- Instruction-based Python programming evaluation byin[@baberabb](https://github.com/baberabb)[#2995](https://github.com/EleutherAI/lm-evaluation-harness/pull/2995)

**Language Modeling**

**C4 Dataset Support**- Added perplexity evaluation on C4 web crawl dataset byin[@Zephyr271828](https://github.com/Zephyr271828)[#2889](https://github.com/EleutherAI/lm-evaluation-harness/pull/2889)

**Long Context Benchmarks**

**Mathematical & Reasoning**

**GSM8K Platinum**- Enhanced mathematical reasoning benchmark byin[@Qubitium](https://github.com/Qubitium)[#2771](https://github.com/EleutherAI/lm-evaluation-harness/pull/2771)**MastermindEval**- Logic reasoning evaluation byin[@whoisjones](https://github.com/whoisjones)[#2788](https://github.com/EleutherAI/lm-evaluation-harness/pull/2788)**JSONSchemaBench**- Structured output evaluation byin[@Saibo-creator](https://github.com/Saibo-creator)[#2865](https://github.com/EleutherAI/lm-evaluation-harness/pull/2865)

**Llama Reference Implementations**

**Llama Reference Implementations**- Added task variants for Multilingual MMLU, MMLU CoT, GSM8K, and ARC Challenge based on Llama evaluation standards byin[@anmarques](https://github.com/anmarques)[#2797](https://github.com/EleutherAI/lm-evaluation-harness/pull/2797),[#2826](https://github.com/EleutherAI/lm-evaluation-harness/pull/2826),[#2829](https://github.com/EleutherAI/lm-evaluation-harness/pull/2829)

**Multilingual Expansion**

**Asian Languages**:

**Korean MMLU (KMMLU)**multiple-choice task byin[@Aprilistic](https://github.com/Aprilistic)[#2849](https://github.com/EleutherAI/lm-evaluation-harness/pull/2849)**MMLU-ProX**extended evaluation byin[@heli-qi](https://github.com/heli-qi)[#2811](https://github.com/EleutherAI/lm-evaluation-harness/pull/2811)**KBL 2025 Dataset**- Updated Korean benchmark evaluation byin[@abzb1](https://github.com/abzb1)[#3000](https://github.com/EleutherAI/lm-evaluation-harness/pull/3000)

**European Languages**:

**African Languages**:

**AfroBench**- Multi-African language evaluation byin[@JessicaOjo](https://github.com/JessicaOjo)[#2825](https://github.com/EleutherAI/lm-evaluation-harness/pull/2825)**Darija tasks**- Moroccan dialect benchmarks (DarijaMMLU, DarijaHellaSwag, Darija_Bench) byin[@hadi-abdine](https://github.com/hadi-abdine)[#2521](https://github.com/EleutherAI/lm-evaluation-harness/pull/2521)

**Arabic Languages**:

**Arab Culture**task for cultural understanding byin[@bodasadallah](https://github.com/bodasadallah)[#3006](https://github.com/EleutherAI/lm-evaluation-harness/pull/3006)

**Domain-Specific Benchmarks**

**CareQA**- Healthcare evaluation benchmark byin[@PabloAgustin](https://github.com/PabloAgustin)[#2714](https://github.com/EleutherAI/lm-evaluation-harness/pull/2714)**ACPBench & ACPBench Hard**- Automated code generation evaluation byin[@harshakokel](https://github.com/harshakokel)[#2807](https://github.com/EleutherAI/lm-evaluation-harness/pull/2807),[#2980](https://github.com/EleutherAI/lm-evaluation-harness/pull/2980)**INCLUDE tasks**- Inclusivity evaluation suite byin[@agromanou](https://github.com/agromanou)[#2769](https://github.com/EleutherAI/lm-evaluation-harness/pull/2769)**Cocoteros VA**dataset byin[@sgs97ua](https://github.com/sgs97ua)[#2787](https://github.com/EleutherAI/lm-evaluation-harness/pull/2787)

**Social & Bias Evaluation**

**Various social bias tasks**for fairness assessment byin[@oskarvanderwal](https://github.com/oskarvanderwal)[#1185](https://github.com/EleutherAI/lm-evaluation-harness/pull/1185)

## Technical Enhancements

**Fine-grained evaluation**: Added`--examples`

argument for efficient multi-prompt evaluation byand[@felipemaiapolo](https://github.com/felipemaiapolo)in[@mirianfsilva](https://github.com/mirianfsilva)[#2520](https://github.com/EleutherAI/lm-evaluation-harness/pull/2520)**Improved tokenization**: Better handling of`add_bos_token`

initialization byin[@baberabb](https://github.com/baberabb)[#2781](https://github.com/EleutherAI/lm-evaluation-harness/pull/2781)**Memory management**: Enhanced softmax computations with`softmax_dtype`

argument for`HFLM`

byin[@Avelina9X](https://github.com/Avelina9X)[#2921](https://github.com/EleutherAI/lm-evaluation-harness/pull/2921)

## Critical Bug Fixes

**Collating Queries Fix**- Resolved error with different continuation lengths that was causing evaluation failures byin[@ameyagodbole](https://github.com/ameyagodbole)[#2987](https://github.com/EleutherAI/lm-evaluation-harness/pull/2987)**Mutual Information Metric**- Fixed acc_mutual_info calculation bug that affected metric accuracy byin[@baberabb](https://github.com/baberabb)[#3035](https://github.com/EleutherAI/lm-evaluation-harness/pull/3035)

## Breaking Changes & Important Updates

**MMLU dataset migration**: Switched to`cais/mmlu`

dataset source byin[@baberabb](https://github.com/baberabb)[#2918](https://github.com/EleutherAI/lm-evaluation-harness/pull/2918)**Default parameter updates**: Increased`max_gen_toks`

to 2048 and`max_length`

to 8192 for MMLU Pro tests byin[@dazipe](https://github.com/dazipe)[#2824](https://github.com/EleutherAI/lm-evaluation-harness/pull/2824)**Temperature defaults**: Set default temperature to 0.0 for vLLM and SGLang backends byin[@baberabb](https://github.com/baberabb)[#2819](https://github.com/EleutherAI/lm-evaluation-harness/pull/2819)

We extend our heartfelt thanks to all contributors who made this release possible, including **43 first-time contributors** who brought fresh perspectives and valuable improvements to the evaluation harness.

## What's Changed

- fix mmlu (generative) metric aggregation by
[@wangcho2k](https://github.com/wangcho2k)in[#2761](https://github.com/EleutherAI/lm-evaluation-harness/pull/2761) - Bugfix by
[@baberabb](https://github.com/baberabb)in[#2762](https://github.com/EleutherAI/lm-evaluation-harness/pull/2762) - fix verbosity typo by
[@baberabb](https://github.com/baberabb)in[#2765](https://github.com/EleutherAI/lm-evaluation-harness/pull/2765) - docs: Fix typos in README.md by
[@ruivieira](https://github.com/ruivieira)in[#2778](https://github.com/EleutherAI/lm-evaluation-harness/pull/2778) - initialize tokenizer with
`add_bos_token`

by[@baberabb](https://github.com/baberabb)in[#2781](https://github.com/EleutherAI/lm-evaluation-harness/pull/2781) - improvement: Use yaml.CLoader to load yaml files when available. by
[@giuliolovisotto](https://github.com/giuliolovisotto)in[#2777](https://github.com/EleutherAI/lm-evaluation-harness/pull/2777) - Consistency Fix: Filter new leaderboard_math_hard dataset to "Level 5" only by
[@perlitz](https://github.com/perlitz)in[#2773](https://github.com/EleutherAI/lm-evaluation-harness/pull/2773) - Fix for mc2 calculation by
[@kdymkiewicz](https://github.com/kdymkiewicz)in[#2768](https://github.com/EleutherAI/lm-evaluation-harness/pull/2768) - New healthcare benchmark: careqa by
[@PabloAgustin](https://github.com/PabloAgustin)in[#2714](https://github.com/EleutherAI/lm-evaluation-harness/pull/2714) - Capture gen_kwargs from CLI in squad_completion by
[@ksurya](https://github.com/ksurya)in[#2727](https://github.com/EleutherAI/lm-evaluation-harness/pull/2727) - humaneval instruct by
[@baberabb](https://github.com/baberabb)in[#2650](https://github.com/EleutherAI/lm-evaluation-harness/pull/2650) - Update evaluator.py by
[@zhuzeyuan](https://github.com/zhuzeyuan)in[#2786](https://github.com/EleutherAI/lm-evaluation-harness/pull/2786) - change piqa dataset path (uses parquet rather than dataset script) by
[@baberabb](https://github.com/baberabb)in[#2790](https://github.com/EleutherAI/lm-evaluation-harness/pull/2790) - use verify_certificate flag in batch requests by
[@daniel-salib](https://github.com/daniel-salib)in[#2785](https://github.com/EleutherAI/lm-evaluation-harness/pull/2785) - add audio modality (qwen2 audio only) by
[@artemorloff](https://github.com/artemorloff)in[#2689](https://github.com/EleutherAI/lm-evaluation-harness/pull/2689) - Add various social bias tasks by
[@oskarvanderwal](https://github.com/oskarvanderwal)in[#1185](https://github.com/EleutherAI/lm-evaluation-harness/pull/1185) - update pre-commit by
[@baberabb](https://github.com/baberabb)in[#2799](https://github.com/EleutherAI/lm-evaluation-harness/pull/2799) - Update Legacy OpenLLM leaderboard to use "train" split for ARC fewshot by
[@Avelina9X](https://github.com/Avelina9X)in[#2802](https://github.com/EleutherAI/lm-evaluation-harness/pull/2802) - Add INCLUDE tasks by
[@agromanou](https://github.com/agromanou)in[#2769](https://github.com/EleutherAI/lm-evaluation-harness/pull/2769) - Add support for token-based auth for watsonx models by
[@kiersten-stokes](https://github.com/kiersten-stokes)in[#2796](https://github.com/EleutherAI/lm-evaluation-harness/pull/2796) - add
**version**by[@baberabb](https://github.com/baberabb)in[#2808](https://github.com/EleutherAI/lm-evaluation-harness/pull/2808) - Add cocoteros_va dataset by
[@sgs97ua](https://github.com/sgs97ua)in[#2787](https://github.com/EleutherAI/lm-evaluation-harness/pull/2787) - Add MastermindEval by
[@whoisjones](https://github.com/whoisjones)in[#2788](https://github.com/EleutherAI/lm-evaluation-harness/pull/2788) - Add loncxt tasks by
[@baberabb](https://github.com/baberabb)in[#2629](https://github.com/EleutherAI/lm-evaluation-harness/pull/2629) - [hf-multimodal] pass kwargs to self.processor by
[@baberabb](https://github.com/baberabb)in[#2667](https://github.com/EleutherAI/lm-evaluation-harness/pull/2667) - [MM] Chartqa by
[@baberabb](https://github.com/baberabb)in[#2544](https://github.com/EleutherAI/lm-evaluation-harness/pull/2544) - Allow writing config to wandb by
[@ksurya](https://github.com/ksurya)in[#2736](https://github.com/EleutherAI/lm-evaluation-harness/pull/2736) - [change] group -> tag on afrimgsm, afrimmlu, afrixnli dataset by
[@jd730](https://github.com/jd730)in[#2813](https://github.com/EleutherAI/lm-evaluation-harness/pull/2813) - Clean up README and pyproject.toml by
[@kiersten-stokes](https://github.com/kiersten-stokes)in[#2814](https://github.com/EleutherAI/lm-evaluation-harness/pull/2814) - Llama3 mmlu correction by
[@anmarques](https://github.com/anmarques)in[#2797](https://github.com/EleutherAI/lm-evaluation-harness/pull/2797) - Add Markdown linter by
[@kiersten-stokes](https://github.com/kiersten-stokes)in[#2818](https://github.com/EleutherAI/lm-evaluation-harness/pull/2818) - Configure the pad tokens for Qwen when using vLLM by
[@zhangruoxu](https://github.com/zhangruoxu)in[#2810](https://github.com/EleutherAI/lm-evaluation-harness/pull/2810) - fix typo in humaneval by
[@baberabb](https://github.com/baberabb)in[#2820](https://github.com/EleutherAI/lm-evaluation-harness/pull/2820) - default temp=0.0 for vllm and slang by
[@baberabb](https://github.com/baberabb)in[#2819](https://github.com/EleutherAI/lm-evaluation-harness/pull/2819) - Fixes to mmlu_pro_llama by
[@anmarques](https://github.com/anmarques)in[#2816](https://github.com/EleutherAI/lm-evaluation-harness/pull/2816) - Add MMLU-ProX task by
[@heli-qi](https://github.com/heli-qi)in[#2811](https://github.com/EleutherAI/lm-evaluation-harness/pull/2811) - Quick fix for mmlu_pro_llama by
[@anmarques](https://github.com/anmarques)in[#2827](https://github.com/EleutherAI/lm-evaluation-harness/pull/2827) - Fix: tj-actions/changed-files is compromised by
[@Tautorn](https://github.com/Tautorn)in[#2828](https://github.com/EleutherAI/lm-evaluation-harness/pull/2828) - Multilingual MMLU for Llama instruct models by
[@anmarques](https://github.com/anmarques)in[#2826](https://github.com/EleutherAI/lm-evaluation-harness/pull/2826) - bbh - changed dataset to parquet version by
[@baberabb](https://github.com/baberabb)in[#2845](https://github.com/EleutherAI/lm-evaluation-harness/pull/2845) - Fix typo in longbench metrics by
[@djwackey](https://github.com/djwackey)in[#2854](https://github.com/EleutherAI/lm-evaluation-harness/pull/2854) - Add kmmlu multiple-choice(accuracy) task
[#2848](https://github.com/EleutherAI/lm-evaluation-harness/issues/2848)by[@Aprilistic](https://github.com/Aprilistic)in[#2849](https://github.com/EleutherAI/lm-evaluation-harness/pull/2849) - Adding ACPBench task by
[@harshakokel](https://github.com/harshakokel)in[#2807](https://github.com/EleutherAI/lm-evaluation-harness/pull/2807) - add Darija (Moroccan dialects) tasks including darijammlu. darijahellaswag and darija_bench by
[@hadi-abdine](https://github.com/hadi-abdine)in[#2521](https://github.com/EleutherAI/lm-evaluation-harness/pull/2521) - Increase default max_gen_toks to 2048 and max_...

[Read more](https://github.com/EleutherAI/lm-evaluation-harness/releases/tag/v0.4.9)

## v0.4.8

# lm-eval v0.4.8 Release Notes

## Key Improvements

-
**New Backend Support**:- Added SGLang as new evaluation backend! by
[@Monstertail](https://github.com/Monstertail) - Enabled model steering with vector support via
`sparsify`

or`sae_lens`

by[@luciaquirke](https://github.com/luciaquirke)and[@AMindToThink](https://github.com/AMindToThink)

- Added SGLang as new evaluation backend! by
-
**Breaking Change**: Python 3.8 support has been dropped as it reached end of life. Please upgrade to Python 3.9 or newer. -
**Added Support for**in config, allowing you to append text after the <|assistant|> token (or at the end of non-chat prompts) - particularly effective for evaluating instruct models`gen_prefix`


## New Benchmarks & Tasks

### Code Evaluation

- HumanEval by
[@hjlee1371](https://github.com/hjlee1371)in[#1992](https://github.com/EleutherAI/lm-evaluation-harness/pull/1992) - MBPP by
[@hjlee1371](https://github.com/hjlee1371)in[#2247](https://github.com/EleutherAI/lm-evaluation-harness/pull/2247) - HumanEval+ and MBPP+ by
[@bzantium](https://github.com/bzantium)in[#2734](https://github.com/EleutherAI/lm-evaluation-harness/pull/2734)

### Multilingual Expansion

-
**Global Coverage**:- Global MMLU (Lite version by
[@shivalika-singh](https://github.com/shivalika-singh)in[#2567](https://github.com/EleutherAI/lm-evaluation-harness/pull/2567), Full version by[@bzantium](https://github.com/bzantium)in[#2636](https://github.com/EleutherAI/lm-evaluation-harness/pull/2636)) - MLQA multilingual question answering by
[@KahnSvaer](https://github.com/KahnSvaer)in[#2622](https://github.com/EleutherAI/lm-evaluation-harness/pull/2622)

- Global MMLU (Lite version by
-
**Asian Languages**: -
**European Languages**: -
**Middle Eastern Languages**:- Arabic MMLU by
[@bodasadallah](https://github.com/bodasadallah)in[#2541](https://github.com/EleutherAI/lm-evaluation-harness/pull/2541) - AraDICE task by
[@firojalam](https://github.com/firojalam)in[#2507](https://github.com/EleutherAI/lm-evaluation-harness/pull/2507)

- Arabic MMLU by

### Ethics & Reasoning

- Moral Stories by
[@upunaprosk](https://github.com/upunaprosk)in[#2653](https://github.com/EleutherAI/lm-evaluation-harness/pull/2653) - Histoires Morales by
[@upunaprosk](https://github.com/upunaprosk)in[#2662](https://github.com/EleutherAI/lm-evaluation-harness/pull/2662)

### Others

- MMLU Pro Plus by
[@asgsaeid](https://github.com/asgsaeid)in[#2366](https://github.com/EleutherAI/lm-evaluation-harness/pull/2366) - GroundCocoa by
[@HarshKohli](https://github.com/HarshKohli)in[#2724](https://github.com/EleutherAI/lm-evaluation-harness/pull/2724)

We extend our thanks to all contributors who made this release possible and to our users for your continued support and feedback.

Thanks, the LM Eval Harness team ([@baberabb](https://github.com/baberabb) and [@lintangsutawika](https://github.com/lintangsutawika))

## What's Changed

- drop python 3.8 support by
[@baberabb](https://github.com/baberabb)in[#2575](https://github.com/EleutherAI/lm-evaluation-harness/pull/2575) - Add Global MMLU Lite by
[@shivalika-singh](https://github.com/shivalika-singh)in[#2567](https://github.com/EleutherAI/lm-evaluation-harness/pull/2567) - add warning for truncation by
[@baberabb](https://github.com/baberabb)in[#2585](https://github.com/EleutherAI/lm-evaluation-harness/pull/2585) - Wandb step handling bugfix and feature by
[@sjmielke](https://github.com/sjmielke)in[#2580](https://github.com/EleutherAI/lm-evaluation-harness/pull/2580) - AraDICE task config file by
[@firojalam](https://github.com/firojalam)in[#2507](https://github.com/EleutherAI/lm-evaluation-harness/pull/2507) - fix extra_match low if batch_size > 1 by
[@sywangyi](https://github.com/sywangyi)in[#2595](https://github.com/EleutherAI/lm-evaluation-harness/pull/2595) - fix model tests by
[@baberabb](https://github.com/baberabb)in[#2604](https://github.com/EleutherAI/lm-evaluation-harness/pull/2604) - update scrolls by
[@baberabb](https://github.com/baberabb)in[#2602](https://github.com/EleutherAI/lm-evaluation-harness/pull/2602) - some minor logging nits by
[@baberabb](https://github.com/baberabb)in[#2609](https://github.com/EleutherAI/lm-evaluation-harness/pull/2609) - Fix gguf loading via Transformers by
[@CL-ModelCloud](https://github.com/CL-ModelCloud)in[#2596](https://github.com/EleutherAI/lm-evaluation-harness/pull/2596) - Fix Zeno visualizer on tasks like GSM8k by
[@pasky](https://github.com/pasky)in[#2599](https://github.com/EleutherAI/lm-evaluation-harness/pull/2599) - Fix the format of mgsm zh and ja. by
[@timturing](https://github.com/timturing)in[#2587](https://github.com/EleutherAI/lm-evaluation-harness/pull/2587) - Add HumanEval by
[@hjlee1371](https://github.com/hjlee1371)in[#1992](https://github.com/EleutherAI/lm-evaluation-harness/pull/1992) - Add MBPP by
[@hjlee1371](https://github.com/hjlee1371)in[#2247](https://github.com/EleutherAI/lm-evaluation-harness/pull/2247) - Add MLQA by
[@KahnSvaer](https://github.com/KahnSvaer)in[#2622](https://github.com/EleutherAI/lm-evaluation-harness/pull/2622) - assistant prefill by
[@baberabb](https://github.com/baberabb)in[#2615](https://github.com/EleutherAI/lm-evaluation-harness/pull/2615) - fix gen_prefix by
[@baberabb](https://github.com/baberabb)in[#2630](https://github.com/EleutherAI/lm-evaluation-harness/pull/2630) - update pre-commit by
[@baberabb](https://github.com/baberabb)in[#2632](https://github.com/EleutherAI/lm-evaluation-harness/pull/2632) - add hrm8k benchmark for both Korean and English by
[@bzantium](https://github.com/bzantium)in[#2627](https://github.com/EleutherAI/lm-evaluation-harness/pull/2627) - New arabicmmlu by
[@bodasadallah](https://github.com/bodasadallah)in[#2541](https://github.com/EleutherAI/lm-evaluation-harness/pull/2541) - Add
`global_mmlu`

full version by[@bzantium](https://github.com/bzantium)in[#2636](https://github.com/EleutherAI/lm-evaluation-harness/pull/2636) - Update KorMedMCQA: ver 2.0 by
[@GyoukChu](https://github.com/GyoukChu)in[#2540](https://github.com/EleutherAI/lm-evaluation-harness/pull/2540) - fix tmlu tmlu_taiwan_specific_tasks tag by
[@nike00811](https://github.com/nike00811)in[#2420](https://github.com/EleutherAI/lm-evaluation-harness/pull/2420) - fixed mmlu generative response extraction by
[@RawthiL](https://github.com/RawthiL)in[#2503](https://github.com/EleutherAI/lm-evaluation-harness/pull/2503) - revise mbpp prompt by
[@bzantium](https://github.com/bzantium)in[#2645](https://github.com/EleutherAI/lm-evaluation-harness/pull/2645) - aggregate by group (total and categories) by
[@bzantium](https://github.com/bzantium)in[#2643](https://github.com/EleutherAI/lm-evaluation-harness/pull/2643) - Fix max_tokens handling in vllm_vlms.py by
[@jkaniecki](https://github.com/jkaniecki)in[#2637](https://github.com/EleutherAI/lm-evaluation-harness/pull/2637) - separate category for
`global_mmlu`

by[@bzantium](https://github.com/bzantium)in[#2652](https://github.com/EleutherAI/lm-evaluation-harness/pull/2652) - Add Moral Stories by
[@upunaprosk](https://github.com/upunaprosk)in[#2653](https://github.com/EleutherAI/lm-evaluation-harness/pull/2653) - add TransformerLens example by
[@nickypro](https://github.com/nickypro)in[#2651](https://github.com/EleutherAI/lm-evaluation-harness/pull/2651) - fix multiple input chat tempalte by
[@baberabb](https://github.com/baberabb)in[#2576](https://github.com/EleutherAI/lm-evaluation-harness/pull/2576) - Add Aggregation for Kobest Benchmark by
[@tryumanshow](https://github.com/tryumanshow)in[#2446](https://github.com/EleutherAI/lm-evaluation-harness/pull/2446) - update pre-commit by
[@baberabb](https://github.com/baberabb)in[#2660](https://github.com/EleutherAI/lm-evaluation-harness/pull/2660) - remove
`group`

from bigbench task configs by[@baberabb](https://github.com/baberabb)in[#2663](https://github.com/EleutherAI/lm-evaluation-harness/pull/2663) - Add Histoires Morales task by
[@upunaprosk](https://github.com/upunaprosk)in[#2662](https://github.com/EleutherAI/lm-evaluation-harness/pull/2662) - MMLU Pro Plus by
[@asgsaeid](https://github.com/asgsaeid)in[#2366](https://github.com/EleutherAI/lm-evaluation-harness/pull/2366) - fix early return for multiple dict in task process_results by
[@baberabb](https://github.com/baberabb)in[#2673](https://github.com/EleutherAI/lm-evaluation-harness/pull/2673) - Turkish mmlu Config Update by
[@ArdaYueksel](https://github.com/ArdaYueksel)in[#2678](https://github.com/EleutherAI/lm-evaluation-harness/pull/2678) - Fix typos by
[@omahs](https://github.com/omahs)in[#2679](https://github.com/EleutherAI/lm-evaluation-harness/pull/2679) - remove cuda device assertion by
[@baberabb](https://github.com/baberabb)in[#2680](https://github.com/EleutherAI/lm-evaluation-harness/pull/2680) - Adding the Evalita-LLM benchmark by
[@m-resta](https://github.com/m-resta)in[#2681](https://github.com/EleutherAI/lm-evaluation-harness/pull/2681) - Delete lm_eval/tasks/evalita_llm/single_prompt.zip by
[@baberabb](https://github.com/baberabb)in[#2687](https://github.com/EleutherAI/lm-evaluation-harness/pull/2687) - Update unitxt task.py to bring in line with recent repo changes by
[@kiersten-stokes](https://github.com/kiersten-stokes)in[#2684](https://github.com/EleutherAI/lm-evaluation-harness/pull/2684) - change ensure_ascii to False for JsonChatStr by
[@artemorloff](https://github.com/artemorloff)in[#2691](https://github.com/EleutherAI/lm-evaluation-harness/pull/2691) - Set defaults for BLiMP scores by
[@jmichaelov](https://github.com/jmichaelov)in[#2692](https://github.com/EleutherAI/lm-evaluation-harness/pull/2692) - Update remaining references to
`assistant_prefill`

in docs to`gen_prefix`

by[@kiersten-stokes](https://github.com/kiersten-stokes)in[#2683](https://github.com/EleutherAI/lm-evaluation-harness/pull/2683) - Update README.md by
[@upunaprosk](https://github.com/upunaprosk)in[#2694](https://github.com/EleutherAI/lm-evaluation-harness/pull/2694) - fix
`construct_requests`

kwargs in python tasks by[@baberabb](https://github.com/baberabb)in[#2700](https://github.com/EleutherAI/lm-evaluation-harness/pull/2700) `arithmetic`

: set target delimiter to empty string by[@baberabb](https://github.com/baberabb)in[#2701](https://github.com/EleutherAI/lm-evaluation-harness/pull/2701)- fix vllm by
[@baberabb](https://github.com/baberabb)in[#2708](https://github.com/EleutherAI/lm-evaluation-harness/pull/2708) - add math_verify to some tasks by
[@baberabb](https://github.com/baberabb)in[#2686](https://github.com/EleutherAI/lm-evaluation-harness/pull/2686) - Logging by
[@lintangsutawika](https://github.com/lintangsutawika)in[#2203](https://github.com/EleutherAI/lm-evaluation-harness/pull/2203) - Replace missing
`lighteval/MATH-Hard`

dataset with`DigitalLearningGmbH/MATH-lighteval`

by[@f4str](https://github.com/f4str)in[#2719](https://github.com/EleutherAI/lm-evaluation-harness/pull/2719) - remove unused import by
[@baberabb](https://github.com/baberabb)in[#2728](https://github.com/EleutherAI/lm-evaluation-harness/pull/2728) - README updates: Added IberoBench citation info in correpsonding READMEs by
[@naiarapm](https://github.com/naiarapm)in[#2729](https://github.com/EleutherAI/lm-evaluation-harness/pull/2729) - add o3-mini support by
[@HelloJocelynLu](https://github.com/HelloJocelynLu)in[#2697](https://github.com/EleutherAI/lm-evaluation-harness/pull/2697) - add Basque translation of ARC and PAWS to BasqueBench by
[@naiarapm](https://github.com/naiarapm)in[#2732](https://github.com/EleutherAI/lm-evaluation-harness/pull/2732) - Add cocoteros_es task in spanish_bench by
[@sgs97ua](https://github.com/sgs97ua)in[#2721](https://github.com/EleutherAI/lm-evaluation-harness/pull/2721) - Fix the import source for eval_logger by
[@kailashbuki](https://github.com/kailashbuki)in[#2735](https://github.com/EleutherAI/lm-evaluation-harness/pull/2735) - add humaneval+ and mbpp+ by
[@bzantium](https://github.com/bzantium)in[#2734](https://github.com/EleutherAI/lm-evaluation-harness/pull/2734) - Support SGLang as Potential Backend for Evaluation by
[@Monstertail](https://github.com/Monstertail)in[#2703](https://github.com/EleutherAI/lm-evaluation-harness/pull/2703) - fix log condition on main by
[@baberabb](https://github.com/baberabb)in[#2737](https://github.com/EleutherAI/lm-evaluation-harness/pull/2737) - fix vllm data parallel by
[@baberabb](https://github.com/baberabb)in[#2746](https://github.com/EleutherAI/lm-evaluation-harness/pull/2746) - [Readme change for SGLang] fix error in readme and add OOM solutions for sglang by
[@Monstertail](https://github.com/Monstertail)in[#2738](https://github.com/EleutherAI/lm-evaluation-harness/pull/2738) - Groundcocoa by
[@HarshKohli](https://github.com/HarshKohli)in[#2724](https://github.com/EleutherAI/lm-evaluation-harness/pull/2724) - fix doc: generate_until only outputs the generated text! by
[@baberabb](https://github.com/baberabb)in[#2755](https://github.com/EleutherAI/lm-evaluation-harness/pull/2755) - Enable steering HF models by
[@luciaquirke](https://github.com/luciaquirke)in[#2749](https://github.com/EleutherAI/lm-evaluation-harness/pull/2749) - Add test for a simple Unitxt task by
[@kiersten-stokes](https://github.com/kiersten-stokes)in[#2742](https://github.com/EleutherAI/lm-evaluation-harness/pull/2742) - add debug log by
[@baberabb](https://github.com/baberabb)in[#2757](https://github.com/EleutherAI/lm-evaluation-harness/pull/2757) - increment version to 0.4.8 by
[@baberabb](https://github.com/baberabb)in[#2760](https://github.com/EleutherAI/lm-evaluation-harness/pull/2760)

## New Contributors...

[Read more](https://github.com/EleutherAI/lm-evaluation-harness/releases/tag/v0.4.8)

## v0.4.7

# lm-eval v0.4.7 Release Notes

This release includes several bug fixes, minor improvements to model handling, and task additions.

⚠️ Python 3.8 End of Support Notice

Python 3.8 support will be dropped in future releases as it has reached its end of life. Users are encouraged to upgrade to Python 3.9 or newer.

## Backwards Incompatibilities

### Chat Template Delimiter Handling (in v0.4.6)

An important modification has been made to how delimiters are handled when applying chat templates in request construction, particularly affecting multiple-choice tasks. This change ensures better compatibility with chat models by respecting their native formatting conventions.

📝 For detailed documentation, please refer to [docs/chat-template-readme.md](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/chat-template-readme.md)

## New Benchmarks & Tasks

- Basque Integration: Added Basque translation of PIQA (piqa_eu) to BasqueBench by
[@naiarapm](https://github.com/naiarapm)in[#2531](https://github.com/EleutherAI/lm-evaluation-harness/pull/2531) - SCORE Tasks: Added new subtask for non-greedy robustness evaluation by
[@rimashahbazyan](https://github.com/rimashahbazyan)in[#2558](https://github.com/EleutherAI/lm-evaluation-harness/pull/2558)

As well as several slight fixes or changes to existing tasks (as noted via the incrementing of versions).

Thanks, the LM Eval Harness team ([@baberabb](https://github.com/baberabb) and [@lintangsutawika](https://github.com/lintangsutawika))

## What's Changed

- Score tasks by
[@rimashahbazyan](https://github.com/rimashahbazyan)in[#2452](https://github.com/EleutherAI/lm-evaluation-harness/pull/2452) - Filters bugfix; add
`metrics`

and`filter`

to logged sample by[@baberabb](https://github.com/baberabb)in[#2517](https://github.com/EleutherAI/lm-evaluation-harness/pull/2517) - skip casting if predict_only by
[@baberabb](https://github.com/baberabb)in[#2524](https://github.com/EleutherAI/lm-evaluation-harness/pull/2524) - make utility function to handle
`until`

by[@baberabb](https://github.com/baberabb)in[#2518](https://github.com/EleutherAI/lm-evaluation-harness/pull/2518) - Update Unitxt task to use locally installed unitxt and not download Unitxt code from Huggingface by
[@yoavkatz](https://github.com/yoavkatz)in[#2514](https://github.com/EleutherAI/lm-evaluation-harness/pull/2514) - add Basque translation of PIQA (piqa_eu) to BasqueBench by
[@naiarapm](https://github.com/naiarapm)in[#2531](https://github.com/EleutherAI/lm-evaluation-harness/pull/2531) - avoid timeout errors with high concurrency in api_model by
[@dtrawins](https://github.com/dtrawins)in[#2307](https://github.com/EleutherAI/lm-evaluation-harness/pull/2307) - Update README.md by
[@baberabb](https://github.com/baberabb)in[#2534](https://github.com/EleutherAI/lm-evaluation-harness/pull/2534) - better doc_to_test testing by
[@baberabb](https://github.com/baberabb)in[#2535](https://github.com/EleutherAI/lm-evaluation-harness/pull/2535) - Support pipeline parallel with OpenVINO models by
[@sstrehlk](https://github.com/sstrehlk)in[#2349](https://github.com/EleutherAI/lm-evaluation-harness/pull/2349) - Super little tiny fix doc by
[@fzyzcjy](https://github.com/fzyzcjy)in[#2546](https://github.com/EleutherAI/lm-evaluation-harness/pull/2546) - [API] left truncate for generate_until by
[@baberabb](https://github.com/baberabb)in[#2554](https://github.com/EleutherAI/lm-evaluation-harness/pull/2554) - Update Lightning import by
[@maanug-nv](https://github.com/maanug-nv)in[#2549](https://github.com/EleutherAI/lm-evaluation-harness/pull/2549) - add optimum-intel ipex model by
[@yao-matrix](https://github.com/yao-matrix)in[#2566](https://github.com/EleutherAI/lm-evaluation-harness/pull/2566) - add warning to readme by
[@baberabb](https://github.com/baberabb)in[#2568](https://github.com/EleutherAI/lm-evaluation-harness/pull/2568) - Adding new subtask to SCORE tasks: non greedy robustness by
[@rimashahbazyan](https://github.com/rimashahbazyan)in[#2558](https://github.com/EleutherAI/lm-evaluation-harness/pull/2558) - batch
`loglikelihood_rolling`

across requests by[@baberabb](https://github.com/baberabb)in[#2559](https://github.com/EleutherAI/lm-evaluation-harness/pull/2559) - fix
`DeprecationWarning: invalid escape sequence '\s'`

for whitespace filter by[@baberabb](https://github.com/baberabb)in[#2560](https://github.com/EleutherAI/lm-evaluation-harness/pull/2560) - increment version to 4.6.7 by
[@baberabb](https://github.com/baberabb)in[#2574](https://github.com/EleutherAI/lm-evaluation-harness/pull/2574)

## New Contributors

[@rimashahbazyan](https://github.com/rimashahbazyan)made their first contribution in[#2452](https://github.com/EleutherAI/lm-evaluation-harness/pull/2452)[@naiarapm](https://github.com/naiarapm)made their first contribution in[#2531](https://github.com/EleutherAI/lm-evaluation-harness/pull/2531)[@dtrawins](https://github.com/dtrawins)made their first contribution in[#2307](https://github.com/EleutherAI/lm-evaluation-harness/pull/2307)[@sstrehlk](https://github.com/sstrehlk)made their first contribution in[#2349](https://github.com/EleutherAI/lm-evaluation-harness/pull/2349)[@fzyzcjy](https://github.com/fzyzcjy)made their first contribution in[#2546](https://github.com/EleutherAI/lm-evaluation-harness/pull/2546)[@maanug-nv](https://github.com/maanug-nv)made their first contribution in[#2549](https://github.com/EleutherAI/lm-evaluation-harness/pull/2549)[@yao-matrix](https://github.com/yao-matrix)made their first contribution in[#2566](https://github.com/EleutherAI/lm-evaluation-harness/pull/2566)

**Full Changelog**: `v0.4.6...v0.4.7`

## v0.4.6

# lm-eval v0.4.6 Release Notes

This release brings important changes to chat template handling, expands our task library with new multilingual and multimodal benchmarks, and includes various bug fixes.

## Backwards Incompatibilities

### Chat Template Delimiter Handling

An important modification has been made to how delimiters are handled when applying chat templates in request construction, particularly affecting multiple-choice tasks. This change ensures better compatibility with chat models by respecting their native formatting conventions.

📝 For detailed documentation, please refer to [docs/chat-template-readme.md](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/chat-template-readme.md)

## New Benchmarks & Tasks

### Multilingual Expansion

**Spanish Bench**: Enhanced benchmark with additional tasks by[@zxcvuser](https://github.com/zxcvuser)in[#2390](https://github.com/EleutherAI/lm-evaluation-harness/pull/2390)**Japanese Leaderboard**: New comprehensive Japanese language benchmark by[@sitfoxfly](https://github.com/sitfoxfly)in[#2439](https://github.com/EleutherAI/lm-evaluation-harness/pull/2439)

### New Task Collections

**Multimodal Unitext**: Added support for multimodal tasks available in unitext by[@elronbandel](https://github.com/elronbandel)in[#2364](https://github.com/EleutherAI/lm-evaluation-harness/pull/2364)**Metabench**: New benchmark contributed by[@kozzy97](https://github.com/kozzy97)in[#2357](https://github.com/EleutherAI/lm-evaluation-harness/pull/2357)

As well as several slight fixes or changes to existing tasks (as noted via the incrementing of versions).

Thanks, the LM Eval Harness team ([@baberabb](https://github.com/baberabb) and [@lintangsutawika](https://github.com/lintangsutawika))

## What's Changed

- Add Unitxt Multimodality Support by
[@elronbandel](https://github.com/elronbandel)in[#2364](https://github.com/EleutherAI/lm-evaluation-harness/pull/2364) - Add new tasks to spanish_bench and fix duplicates by
[@zxcvuser](https://github.com/zxcvuser)in[#2390](https://github.com/EleutherAI/lm-evaluation-harness/pull/2390) - fix typo bug for minerva_math by
[@renjie-ranger](https://github.com/renjie-ranger)in[#2404](https://github.com/EleutherAI/lm-evaluation-harness/pull/2404) - Fix: Turkish MMLU Regex Pattern by
[@ArdaYueksel](https://github.com/ArdaYueksel)in[#2393](https://github.com/EleutherAI/lm-evaluation-harness/pull/2393) - fix storycloze datanames by
[@t1101675](https://github.com/t1101675)in[#2409](https://github.com/EleutherAI/lm-evaluation-harness/pull/2409) - Update NoticIA prompt by
[@ikergarcia1996](https://github.com/ikergarcia1996)in[#2421](https://github.com/EleutherAI/lm-evaluation-harness/pull/2421) - [Fix] Replace generic exception classes with a more specific ones by
[@LSinev](https://github.com/LSinev)in[#1989](https://github.com/EleutherAI/lm-evaluation-harness/pull/1989) - Support for IBM watsonx_llm by
[@Medokins](https://github.com/Medokins)in[#2397](https://github.com/EleutherAI/lm-evaluation-harness/pull/2397) - Fix package extras for watsonx support by
[@kiersten-stokes](https://github.com/kiersten-stokes)in[#2426](https://github.com/EleutherAI/lm-evaluation-harness/pull/2426) - Fix lora requests when dp with vllm by
[@ckgresla](https://github.com/ckgresla)in[#2433](https://github.com/EleutherAI/lm-evaluation-harness/pull/2433) - Add xquad task by
[@zxcvuser](https://github.com/zxcvuser)in[#2435](https://github.com/EleutherAI/lm-evaluation-harness/pull/2435) - Add verify_certificate argument to local-completion by
[@sjmonson](https://github.com/sjmonson)in[#2440](https://github.com/EleutherAI/lm-evaluation-harness/pull/2440) - Add GPTQModel support for evaluating GPTQ models by
[@Qubitium](https://github.com/Qubitium)in[#2217](https://github.com/EleutherAI/lm-evaluation-harness/pull/2217) - Add missing task links by
[@Sypherd](https://github.com/Sypherd)in[#2449](https://github.com/EleutherAI/lm-evaluation-harness/pull/2449) - Update CODEOWNERS by
[@haileyschoelkopf](https://github.com/haileyschoelkopf)in[#2453](https://github.com/EleutherAI/lm-evaluation-harness/pull/2453) - Add real process_docs example by
[@Sypherd](https://github.com/Sypherd)in[#2456](https://github.com/EleutherAI/lm-evaluation-harness/pull/2456) - Modify label errors in catcola and paws-x by
[@zxcvuser](https://github.com/zxcvuser)in[#2434](https://github.com/EleutherAI/lm-evaluation-harness/pull/2434) - Add Japanese Leaderboard by
[@sitfoxfly](https://github.com/sitfoxfly)in[#2439](https://github.com/EleutherAI/lm-evaluation-harness/pull/2439) - Typos: Fix 'loglikelihood' misspellings in api_models.py by
[@RobGeada](https://github.com/RobGeada)in[#2459](https://github.com/EleutherAI/lm-evaluation-harness/pull/2459) - use global
`multi_choice_filter`

for mmlu_flan by[@baberabb](https://github.com/baberabb)in[#2461](https://github.com/EleutherAI/lm-evaluation-harness/pull/2461) - typo by
[@baberabb](https://github.com/baberabb)in[#2465](https://github.com/EleutherAI/lm-evaluation-harness/pull/2465) - pass device_map other than auto for parallelize by
[@baberabb](https://github.com/baberabb)in[#2457](https://github.com/EleutherAI/lm-evaluation-harness/pull/2457) - OpenAI ChatCompletions: switch
`max_tokens`

by[@baberabb](https://github.com/baberabb)in[#2443](https://github.com/EleutherAI/lm-evaluation-harness/pull/2443) - Ifeval: Dowload
`punkt_tab`

on rank 0 by[@baberabb](https://github.com/baberabb)in[#2267](https://github.com/EleutherAI/lm-evaluation-harness/pull/2267) - Fix chat template; fix leaderboard math by
[@baberabb](https://github.com/baberabb)in[#2475](https://github.com/EleutherAI/lm-evaluation-harness/pull/2475) - change warning to debug by
[@baberabb](https://github.com/baberabb)in[#2481](https://github.com/EleutherAI/lm-evaluation-harness/pull/2481) - Updated wandb logger to use
`new_printer()`

instead of`get_printer(...)`

by[@alex-titterton](https://github.com/alex-titterton)in[#2484](https://github.com/EleutherAI/lm-evaluation-harness/pull/2484) - IBM watsonx_llm fixes & refactor by
[@Medokins](https://github.com/Medokins)in[#2464](https://github.com/EleutherAI/lm-evaluation-harness/pull/2464) - Fix revision parameter to vllm get_tokenizer by
[@OyvindTafjord](https://github.com/OyvindTafjord)in[#2492](https://github.com/EleutherAI/lm-evaluation-harness/pull/2492) - update pre-commit hooks and git actions by
[@baberabb](https://github.com/baberabb)in[#2497](https://github.com/EleutherAI/lm-evaluation-harness/pull/2497) - kbl-v0.1.1 by
[@whwang299](https://github.com/whwang299)in[#2493](https://github.com/EleutherAI/lm-evaluation-harness/pull/2493) - Add mamba hf to
`mamba_ssm`

by[@baberabb](https://github.com/baberabb)in[#2496](https://github.com/EleutherAI/lm-evaluation-harness/pull/2496) - remove duplicate
`arc_ca`

tag by[@baberabb](https://github.com/baberabb)in[#2499](https://github.com/EleutherAI/lm-evaluation-harness/pull/2499) - Add metabench task to LM Evaluation Harness by
[@kozzy97](https://github.com/kozzy97)in[#2357](https://github.com/EleutherAI/lm-evaluation-harness/pull/2357) - Nits by
[@baberabb](https://github.com/baberabb)in[#2500](https://github.com/EleutherAI/lm-evaluation-harness/pull/2500) - [API models] parse tokenizer_backend=None properly by
[@baberabb](https://github.com/baberabb)in[#2509](https://github.com/EleutherAI/lm-evaluation-harness/pull/2509)

## New Contributors

[@renjie-ranger](https://github.com/renjie-ranger)made their first contribution in[#2404](https://github.com/EleutherAI/lm-evaluation-harness/pull/2404)[@t1101675](https://github.com/t1101675)made their first contribution in[#2409](https://github.com/EleutherAI/lm-evaluation-harness/pull/2409)[@Medokins](https://github.com/Medokins)made their first contribution in[#2397](https://github.com/EleutherAI/lm-evaluation-harness/pull/2397)[@kiersten-stokes](https://github.com/kiersten-stokes)made their first contribution in[#2426](https://github.com/EleutherAI/lm-evaluation-harness/pull/2426)[@ckgresla](https://github.com/ckgresla)made their first contribution in[#2433](https://github.com/EleutherAI/lm-evaluation-harness/pull/2433)[@sjmonson](https://github.com/sjmonson)made their first contribution in[#2440](https://github.com/EleutherAI/lm-evaluation-harness/pull/2440)[@Qubitium](https://github.com/Qubitium)made their first contribution in[#2217](https://github.com/EleutherAI/lm-evaluation-harness/pull/2217)[@Sypherd](https://github.com/Sypherd)made their first contribution in[#2449](https://github.com/EleutherAI/lm-evaluation-harness/pull/2449)[@sitfoxfly](https://github.com/sitfoxfly)made their first contribution in[#2439](https://github.com/EleutherAI/lm-evaluation-harness/pull/2439)[@RobGeada](https://github.com/RobGeada)made their first contribution in[#2459](https://github.com/EleutherAI/lm-evaluation-harness/pull/2459)[@alex-titterton](https://github.com/alex-titterton)made their first contribution in[#2484](https://github.com/EleutherAI/lm-evaluation-harness/pull/2484)[@OyvindTafjord](https://github.com/OyvindTafjord)made their first contribution in[#2492](https://github.com/EleutherAI/lm-evaluation-harness/pull/2492)[@whwang299](https://github.com/whwang299)made their first contribution in[#2493](https://github.com/EleutherAI/lm-evaluation-harness/pull/2493)[@kozzy97](https://github.com/kozzy97)made their first contribution in[#2357](https://github.com/EleutherAI/lm-evaluation-harness/pull/2357)

**Full Changelog**: `v0.4.5...v0.4.6`