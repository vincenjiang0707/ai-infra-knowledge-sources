# [Issue #3171] Datasets with loading scripts - no longer supported

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3171
state: open | updated: 2026-09-08T13:34:01Z
labels: 

## 正文

As of `datasets==4.0`, loading scripts and `trust_remote_code` are no longer supported. Started this thread to track tasks which still rely on the scripts so that the datasets can either be updated upstream in HF or in the task configs.

Just add a comment, if anyone comes across any.

## 评论 (22)

### baberabb · 2025-07-21

afrobench's `masakhapos`: `masakhane/masakhapos`

### Avelina9X · 2025-07-22

Gone through all the `a***` groups. Found remote code, missing datasets, an incorrect name, and some datasets marked as remote code required but have been fixed on the hub to work without code. I may have missed some, but this is what I found so far.

`aclue`: `tyouisen/aclue` (remote code)

`aexams`: `Hennara/aexams` (remote code)

`afrobench`:
- `adr`: `masakhane/diacritics-restoration` (missing)
- `afriqa`: `masakhane/afriqa-gold-passages` (remote code)
- ~~`afrisenti`: `masakhane/afrisenti`~~ (fixed on hub, task needs updating)
- `flores`: `facebook/flores` (remote code)
- ~~`mafand`: `masakhane/mafand`~~ (fixed on hub, task needs updating)
- `masakhaner`: `masakhane/masakhaner-x` (remote code)
- `masakhapos`: `masakhane/masakhapos` (remote code)
- ~~`nollysenti`: `Davlan/nollysenti`~~ (fixed on hub, task needs updating)
- ~~`ntrex`: `masakhane/ntrex_african`~~ (fixed on hub, task needs updating)
- ~~`salt`: `Sunbird/salt`~~ (fixed on hub, task needs updating)
- ~~`xlsum`: `csebuetnlp/xlsum`~~ (fixed on hub, task needs updating)

`anli`: `anli` (should be `facebook/anli`)

`arab_culture_completion`: `boda/arabic_cluture` (missing)

`asdiv`: `EleutherAI/asdiv` (remote code)

### baberabb · 2025-07-22

`super-glue`: added full path in #3169 

### BKHMSI · 2025-07-26

`mgsm`: `juletxara/mgsm` also has a similar issue!

### fzyzcjy · 2025-07-28

mmlu has same issue

### KyleMylonakisProtopia · 2025-09-23

Hey all, is there any current plan to support datasets 4.0 and grater beyond what is discussed in this issue? If we don't run the tests outline above, can the pin at least be removed and moved to some kind of raised error on the remaining tests which have issues?

### jannalulu · 2025-10-21

[longbench v1](https://huggingface.co/datasets/zai-org/LongBench) `zai-org/LongBench` still uses remote code, would not load without trust_remote_code=True

### zoxxxx · 2025-10-26

This problem also occurs with [race](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/race/README.md).

### baberabb · 2025-10-27

updated the race dataset to parquet. btw also discovered the `datasets-cli` utility, which I didn't even know existed but apparently been around for awhile. `datasets-cli convert_to_parquet EleutherAI/race` was pretty quick

### upunaprosk · 2025-10-31

Same issue with crows_pairs

### upunaprosk · 2025-11-04

also same issue with hendrycks ethics 

### jannalulu · 2025-11-04

> also same issue with hendrycks ethics

converted hendrycks_ethics to parquet on [HF](https://huggingface.co/datasets/EleutherAI/hendrycks_ethics/discussions/2), but @baberabb has to merge it

### Bzdss6 · 2026-01-07

cmmlu has same issue

### upunaprosk · 2026-01-07

Other datasets relying on loading scripts:

- mc_taco  (lm_eval/tasks/mc_taco/default.yaml)
- story_cloze  (lm_eval/tasks/storycloze/storycloze_2016.yaml)
- story_cloze  (lm_eval/tasks/storycloze/storycloze_2018.yaml)
- EleutherAI/hendrycks_ethics  (lm_eval/tasks/hendrycks_ethics/commonsense.yaml)
- EleutherAI/arithmetic  (lm_eval/tasks/arithmetic/arithmetic_1dc.yaml)
- baber/logiqa2  (lm_eval/tasks/logiqa2/logieval.yaml)
- social_i_qa  (lm_eval/tasks/siqa/siqa.yaml)
- iwslt2017  (lm_eval/tasks/translation/iwslt2017_en-ar.yaml)
- iwslt2017  (lm_eval/tasks/translation/iwslt2017_ar-en.yaml)
- EleutherAI/sycophancy  (lm_eval/tasks/model_written_evals/sycophancy/sycophancy_on_political_typology_quiz.yaml)
- EleutherAI/sycophancy  (lm_eval/tasks/model_written_evals/sycophancy/sycophancy_on_philpapers2020.yaml)
- EleutherAI/sycophancy  (lm_eval/tasks/model_written_evals/sycophancy/sycophancy_on_nlp_survey.yaml)
- corypaik/prost  (lm_eval/tasks/prost/corypaik_prost.yaml)
- Rakuten/JGLUE  (lm_eval/tasks/japanese_leaderboard/ja_leaderboard_jnli.yaml)
- Rakuten/JGLUE  (lm_eval/tasks/japanese_leaderboard/ja_leaderboard_jsquad.yaml)
- kumapo/JAQKET  (lm_eval/tasks/japanese_leaderboard/ja_leaderboard_jaqket_v2.yaml)
- Rakuten/JGLUE  (lm_eval/tasks/japanese_leaderboard/ja_leaderboard_marc_ja.yaml)
- orai-nlp/basqueGLUE  (lm_eval/tasks/basqueglue/qnli.yaml)
- PlanTL-GOB-ES/wnli-es  (lm_eval/tasks/spanish_bench/wnli_es.yaml)
- EleutherAI/unscramble  (lm_eval/tasks/unscramble/cycle_letters.yaml)
- EleutherAI/unscramble  (lm_eval/tasks/unscramble/anagrams1.yaml)
- EleutherAI/unscramble  (lm_eval/tasks/unscramble/anagrams2.yaml)
- EleutherAI/unscramble  (lm_eval/tasks/unscramble/random_insertion.yaml)
- EleutherAI/unscramble  (lm_eval/tasks/unscramble/reversed_words.yaml)

### DhruvaKashyap · 2026-01-21

`allenai/math_qa` is not supported yet, `regisss/math_qa` may be an alternative

### ayaangazali · 2026-07-18

Hi! I went through every `dataset_path` in `lm_eval/tasks` and probed them all against a clean install (datasets 5.0.0, huggingface_hub 1.24, checked at f4d4b3de). Figured a full sweep might save people from reporting these one at a time. Everything below was verified by actually calling `load_dataset_builder` on each path, not just by looking for `.py` files.

**Script-based datasets that currently fail with `RuntimeError: Dataset scripts are no longer supported`** (36 paths):

| dataset_path | task folder(s) |
|---|---|
| EleutherAI/advanced_ai_risk | model_written_evals/advanced_ai_risk |
| EleutherAI/arithmetic | arithmetic |
| EleutherAI/hendrycks_ethics | hendrycks_ethics |
| EleutherAI/logiqa | logiqa |
| EleutherAI/mutual | mutual |
| EleutherAI/persona | model_written_evals/persona |
| EleutherAI/pile | pile |
| EleutherAI/sycophancy | model_written_evals/sycophancy |
| EleutherAI/unscramble | unscramble |
| allenai/social_i_qa | siqa |
| allenai/qasper | qasper |
| allenai/math_qa (redirect of bare `math_qa`) | mathqa |
| asi/wikitext_fr | french_bench |
| baber/logiqa2 | logiqa2 |
| bigbio/meddialog | meddialog |
| bigbio/mediqa_qa | mediqa_qa2019 |
| bigbio/meqsum | meqsum |
| bigbio/pubmed_qa | pubmedqa (already tracked in #3645) |
| CogComp/mc_taco | mc_taco |
| corypaik/prost | prost |
| csebuetnlp/xlsum | spanish_bench |
| demelin/moral_stories | moral_stories |
| EdinburghNLP/orange_sum (redirect of bare `orange_sum`) | french_bench |
| ErnestSDavis/winograd_wsc (redirect of bare `winograd_wsc`) | wsc273 |
| facebook/mlqa | mlqa |
| HAERAE-HUB/csatqa | csatqa |
| Helsinki-NLP/tatoeba_mt | noreval |
| Hennara/aexams | aexams |
| IWSLT/iwslt2017 | translation |
| kumapo/JAQKET | japanese_leaderboard |
| LSDSem/story_cloze | storycloze (also needs manual data) |
| loubnabnl/humaneval_infilling | humaneval_infilling |
| masakhane/masakhapos | afrobench |
| masakhane/mafand | afrobench |
| orai-nlp/basqueGLUE | basqueglue |
| PlanTL-GOB-ES/wnli-es | spanish_bench |
| Rakuten/JGLUE | japanese_leaderboard |
| tyouisen/aclue | aclue |
| ZoneTwelve/tmmluplus | tmmluplus |

Nine of these live in the EleutherAI org, so those should be fixable in place with `datasets-cli convert_to_parquet` like race was. Also worth noting: the hendrycks_ethics parquet conversion that @jannalulu opened on the Hub back in November still seems to be sitting unmerged (huggingface.co/datasets/EleutherAI/hendrycks_ethics/discussions/2).

**Previously mentioned in this thread, now confirmed working:** juletxara/mgsm, cais/mmlu, EleutherAI/race, masakhane/afrisenti, Davlan/nollysenti, and crows_pairs (task config now points at jannalu/crows_pairs_multilingual).

**A second, separate failure class:** with huggingface_hub 1.24 the remaining bare (un-namespaced) dataset IDs now fail with `HfUriError: Repository id must be 'namespace/name'` before task loading. Same thing #3870 fixed for xnli/xcopa/paws-x/xquad. I opened #3942 for webqs, medmcqa, and the wmt2016 leftover (the ones I could verify end to end). The bare `anli`/`hellaswag`/`winogrande` entries in `benchmarks/t0_eval.yaml` have the same problem, but that config currently does not load anyway (its group entries have no `task` key, so `TaskManager.load` rejects it). The bare math_qa, orange_sum, and winograd_wsc redirect to script-based repos, so namespacing alone will not save those three.

One more small thing: configs that still pass `trust_remote_code: True` through `dataset_kwargs` (e.g. the afrobench mafand ones) now fail with a `BuilderConfig ... doesn't have a 'trust_remote_code' key` ValueError even when the underlying dataset is fine, since recent datasets versions reject the kwarg.

Happy to help chip away at the task-config side of this list if useful.

---

full transparency: i am a college freshman and i leaned on Claude Code to script the probing across all 384 dataset paths, then spot checked the results by hand. if any entry in the table looks wrong please call it out, i would rather learn than be right :)


### shubhangithub · 2026-07-19

Thanks for the full sweep above, that's handy. Claiming three of the script-based ones (config-side path swaps, per [#3870](https://github.com/shubhangithub/collusionguard/issues/3870)'s pattern):

mathqa: math_qa -> regisss/math_qa (the alternative suggested earlier in the thread)
siqa: allenai/social_i_qa -> lighteval/siqa
moral_stories: demelin/moral_stories (config full) -> LabHC/moral_stories (single config, so dataset_name becomes null)
Provenance: I loaded each original with datasets 3.6.0 (trust_remote_code=True) and md5-hashed every split over the columns the tasks consume, then did the same for the mirrors on datasets 5.0.0. All hashes match exactly: math_qa 29837/4475/2985 (all seven columns), siqa 33410/1954, moral_stories 12000. So the mirrors are content-identical to the originals for eval purposes, not just similarly sized.

One find while checking the rest: CogComp/mc_taco and corypaik/prost have no faithful script-less mirror I could locate. corypaik/prost ships its data as jsonl in the repo, so the fix there is probably the author dropping prost.py.

I'll open the PR shortly,  happy to swap any of the mirrors if you'd rather source them differently.

### ayaangazali · 2026-07-21

Picked up wsc273 from the tabled list: #3946 swaps the config to the lighteval/winograd_wsc parquet mirror, with all 273 rows checked byte-for-byte against HF's auto-conversion of the original script dataset.

(Assembled with help from Claude; parity check and eval run verified locally.)

### ayaangazali · 2026-08-03

Small follow up on the script-based list above. For several of these the data itself is still published in the repo next to the dead script, so the task can read it directly with `data_files` and no mirror is needed:

- `EleutherAI/arithmetic` keeps one jsonl per subtask under `data/` -> #3976 (all ten arithmetic tasks)
- `tau/scrolls` keeps one zip per subtask, each holding the jsonl -> #3975 (all seven scrolls tasks)

Worth knowing that this only works if you also reproduce whatever the script did to the fields. The arithmetic script rewrote `context` before yielding it, so reading the jsonl raw would have quietly changed every prompt.

From a quick scan, the same route looks open for `corypaik/prost` (`data/default.jsonl`), `PlanTL-GOB-ES/wnli-es` (per split csv), `ZoneTwelve/tmmluplus` and `HAERAE-HUB/csatqa` (per subject csv/json), `kumapo/JAQKET`, `loubnabnl/humaneval_infilling`, `Helsinki-NLP/tatoeba_mt`, plus `tyouisen/aclue`, `Hennara/aexams`, `asi/wikitext_fr` and `IWSLT/iwslt2017` via their zips. Happy for anyone to take those, I am not working on them.

Ones where it does not help, since the repo only ships the script (or only dummy data): the other EleutherAI datasets in the table, `CogComp/mc_taco`, `EdinburghNLP/orange_sum`, `facebook/mlqa`, `baber/logiqa2`, `Rakuten/JGLUE`, `orai-nlp/basqueGLUE`, the `bigbio/*` ones, and `allenai/qasper` and `csebuetnlp/xlsum`. Those still need a real conversion.

Compiled with AI assistance; the file listings and loads behind it were run and checked here.


### ayaangazali · 2026-08-04

Correction to my note above: I said I was not working on the remaining ones, then picked up `corypaik/prost` a few hours later, so flagging it here rather than leaving a stale claim. That is #3977, a four line config change since the script yielded rows verbatim.

The rest of that list is genuinely untouched by me: `PlanTL-GOB-ES/wnli-es`, `ZoneTwelve/tmmluplus`, `HAERAE-HUB/csatqa`, `kumapo/JAQKET`, `loubnabnl/humaneval_infilling`, `Helsinki-NLP/tatoeba_mt`, plus the zip based ones. Still happy for anyone to take them, and I will say so here if that changes again.

One thing worth passing on from doing three of these: check what the script did to the fields before yielding. For `arithmetic` it rewrote `context`, so reading the jsonl raw would have silently changed every prompt. For `prost` the risk was `label` being declared a `ClassLabel`, which would have broken the gold index had the file stored letters instead of integers. Neither shows up as an error, only as different numbers.

Noted with AI assistance; the checks behind it were run here.


### ayaangazali · 2026-08-06

Updating my position here properly rather than flip-flopping one dataset at a time.

Nobody has picked these up in the three days since I listed them, so I am going to work through the remaining ones myself instead of leaving them sitting. `PlanTL-GOB-ES/wnli-es` is #3982. Still to do, and I will note each here as I open it: `ZoneTwelve/tmmluplus`, `HAERAE-HUB/csatqa`, `kumapo/JAQKET`, `loubnabnl/humaneval_infilling`, `Helsinki-NLP/tatoeba_mt`, plus the zip based `tyouisen/aclue`, `Hennara/aexams`, `asi/wikitext_fr` and `IWSLT/iwslt2017`.

If you were already partway through any of them, say so and I will leave it alone, no hard feelings. I would rather duplicate nothing.

Running tally of what the pattern has fixed so far: #3975 scrolls (7 tasks), #3976 arithmetic (10), #3977 prost, #3982 wnli_es. Common thread in every one: check what the loading script did to the fields before it yielded them. So far that has been a context rewrite in arithmetic, a ClassLabel over letters in prost, and an integer to string to ClassLabel round trip in wnli-es. None of those announce themselves, they just change the numbers.

Written with AI help; the loads and checks behind each were run locally.


### linhongyu510 · 2026-09-08

Picked up `HAERAE-HUB/csatqa` from the script-based list — #4121, all six `csatqa_*` tasks.

It's the "data still ships next to the dead script" route, so no mirror needed. But it turned out to be more than a path swap, in a way that matches the warning @ayaangazali kept flagging above: the script declared **one builder config per category** and filtered on the `Category` column (`elif data["Category"] == self.config.name`). That filter was doing real work — it's how each subject task got only its own questions. `data/csatqa.json` holds all 936 rows, and `dataset_name` stops selecting anything once `dataset_path` is `json`, so reading the file directly would have quietly scored every subject against all 936 rows instead of its own 11–42. No error, just different numbers.

Since `process_docs` only receives the dataset, the per-category selection moved there — one thin wrapper per subject over a shared helper.

Verified on content rather than row counts alone: rebuilt what the script would have yielded and compared the rendered prompt + gold index for every doc in file order, giving identical md5 for all six subjects (`csatqa_wr b7de26368290`, `gr 4703b552002f`, `rcs a88c5bce87e0`, `rcss d2d9b26743a8`, `rch 00736cbc333a`, `li 3e329dc7baab`). Counts land at WR 11 / GR 25 / RCS 37 / RCSS 42 / RCH 35 / LI 37.

Adding one more instance to the running list of field-level gotchas: here `gold` is stored as a **string** in the JSON while the script declared it `int8`. The existing `int(doc["gold"]) - 1` absorbs it, so nothing breaks, but a task comparing `gold` directly would have silently mismatched.

Separately, while sweeping every `dataset_path` in the repo I hit a different failure mode worth recording here — `fixie-ai/endpointing-audio` (used by `common_voice/common_voice_en.yaml`) is gone from the Hub the same way `miulab/tmlu` is (#3985): auth error on the API, and absent from the public search index while public datasets return normally unauthenticated. That's an availability problem rather than a script problem, so it doesn't belong on this list — just noting it so it isn't rediscovered from scratch. I'm not opening a PR for it since, like TMLU, there's no replacement to point at.

Not working on anything else from the list right now, so `kumapo/JAQKET`, `loubnabnl/humaneval_infilling`, `Helsinki-NLP/tatoeba_mt`, `tyouisen/aclue`, `Hennara/aexams`, `asi/wikitext_fr` and `IWSLT/iwslt2017` are all still free as far as I know.

Done with AI assistance; the loads, hashes and the eval run behind the above were all executed locally.
