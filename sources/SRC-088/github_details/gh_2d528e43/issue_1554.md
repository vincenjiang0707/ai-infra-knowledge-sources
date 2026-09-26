# [Issue #1554] New Task Request: InflectionAI's Physics GRE

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/1554
state: closed | updated: 2026-08-31T12:30:12Z
labels: help wanted, feature request, good first issue

## 正文

There is a new dataset of Physics GRE exams constructed by Inflection AI: https://github.com/InflectionAI/Inflection-Benchmarks?tab=readme-ov-file#physics-gre

Adding this task would be a nice addition :)

## 评论 (3)

### ShayekhBinIslam · 2024-04-01

@haileyschoelkopf I am interested in contributing here by adding this task if possible. 

### bongho · 2026-06-16

Hi @haileyschoelkopf, is this still open? I'd be happy to pick this up.

The dataset is already on the Hub at [`shayekh/physics_gre`](https://huggingface.co/datasets/shayekh/physics_gre) (thanks @ShayekhBinIslam) — I verified it mirrors the original [InflectionAI/Inflection-Benchmarks](https://github.com/InflectionAI/Inflection-Benchmarks) exactly (`input` / `target_scores` / `has_image`, GR8677 as the 100-item scored split plus 300 additional). I'm planning to add it as a `multiple_choice` task with `acc`/`acc_norm`.

One design note: the original only scores image-free questions ("we include only questions without an image in our scoring"), so I'd default to filtering `has_image=True` and expose the full split as a variant. @ShayekhBinIslam, are you still planning to work on this? Happy to collaborate or take it over if not.


### bongho · 2026-06-16

Opened #3853 implementing this as `multiple_choice` tasks (image-free scoring, three exam splits).
