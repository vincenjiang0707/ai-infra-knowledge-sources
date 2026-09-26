source: https://github.com/vllm-project/guidellm/commit/34e8526bb6c39b517a9c4b043b171c03793324ee

# Commit 34e8526

committed

Report confidence intervals for request-level metrics

Every statistic in a report is an estimate from a finite number of requests,
and nothing in the output says how precisely it was measured. The percentiles
are order statistics, so p99 sits at rank ceil(0.99n). Below 100 successful
requests that rank is n, and the reported p99 is the slowest single request,
printed with the same authority as the mean. Across twelve identical ten
second runs against the mock server the reported p99 varied by 23.5% while
the mean varied by 8.5%.
DistributionSummary now carries an interval for the mean and one for each
percentile, at a level set through --metrics and recorded once per benchmark.
A percentile interval is null where the sample cannot place two order
statistics around it, which takes 72 requests for p95, 368 for p99 and 3688
for p999. Reporting null there is the point: it marks the percentiles a short
run cannot support. The console marks such a percentile rather than printing
it as though it were measured.
Intervals are attached only to distributions holding one unweighted
observation per request. Time per output token and inter-token latency stay
point estimates because, in a repeated-run variable-load experiment, their
within-run intervals understated observed run-to-run variation by 1.8x and
3.2x respectively. The measurements were associated with a shared run-level
load condition that a single-run request-sampling interval cannot observe.
Derived rate distributions are excluded separately: their time-weighted
construction does not meet the estimator's request-sample assumption, and
that construction is itself under discussion in [#602](https://github.com/vllm-project/guidellm/issues/602). The estimator rejects any weight other than one, so a later caller cannot opt an unsupported distribution into inference. The quantile functions and interval estimators move to a shared module, which removes an import of approx_t_ppf from a scheduler constraint into a benchmark profile. approx_t_ppf moves unchanged with a re-export left behind, and wilson_interval keeps deriving its quantile from it rather than from the exact normal quantile. The two differ by 2.2e-4, enough to move a Wilson upper bound of exactly 1.0 to just below it and turn a goodput probe that met a 100% attainment target into one that missed it. New inference uses an accurate t quantile, since the approximation is 49% low at one degree of freedom and 6% low at three. Assisted-by: Claude Code claude-opus-5 Signed-off-by: QHarshil <harshil_c@hotmail.com>

1 parent[73608c2]commit 34e8526

20 files changed

Lines changed: 2407 additions & 136 deletions

## File tree

- docs/en/guides
- src/guidellm
- benchmark
- outputs
- profiles
- schemas

- scheduler/constraints
- schemas
- base
- benchmark

- utils

- tests/unit
- benchmark
- schemas

- schemas
- utils


| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`151` | `151` |
| |
`152` | `152` |
| |
`153` | `153` |
| |
| `154` | `+` | |
| `155` | `+` | |
| `156` | `+` | |
| `157` | `+` | |
| `158` | `+` | |
| `159` | `+` | |
| `160` | `+` | |
| `161` | `+` | |
| `162` | `+` | |
| `163` | `+` | |
| `164` | `+` | |
| `165` | `+` | |
| `166` | `+` | |
| `167` | `+` | |
| `168` | `+` | |
| `169` | `+` | |
| `170` | `+` | |
| `171` | `+` | |
| `172` | `+` | |
| `173` | `+` | |
| `174` | `+` | |
| `175` | `+` | |
| `176` | `+` | |
| `177` | `+` | |
| `178` | `+` | |
| `179` | `+` | |
| `180` | `+` | |
| `181` | `+` | |
| `182` | `+` | |
| `183` | `+` | |
`154` | `184` |
| |
`155` | `185` |
| |
`156` | `186` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`71` | `71` |
| |
`72` | `72` |
| |
`73` | `73` |
| |
| `74` | `+` | |
`74` | `75` |
| |
`75` | `76` |
| |
`76` | `77` |
| |
| |||
`91` | `92` |
| |
`92` | `93` |
| |
`93` | `94` |
| |
| `95` | `+` | |
| `96` | `+` | |
`94` | `97` |
| |
`95` | `98` |
| |
`96` | `99` |
| |
| |||
`131` | `134` |
| |
`132` | `135` |
| |
`133` | `136` |
| |
| `137` | `+` | |
`134` | `138` |
| |
`135` | `139` |
| |
`136` | `140` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`559` | `559` |
| |
`560` | `560` |
| |
`561` | `561` |
| |
| `562` | `+` | |
`562` | `563` |
| |
`563` | `564` |
| |
`564` | `565` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`29` | `29` |
| |
`30` | `30` |
| |
`31` | `31` |
| |
`32` |
| `-` | |
| `32` | `+` | |
| `33` | `+` | |
| `34` | `+` | |
| `35` | `+` | |
| `36` | `+` | |
| `37` | `+` | |
| `38` | `+` | |
| `39` | `+` | |
| `40` | `+` | |
| `41` | `+` | |
| `42` | `+` | |
| `43` | `+` | |
| `44` | `+` | |
`33` | `45` |
| |
`34` | `46` |
| |
`35` | `47` |
| |
| |||
`121` | `133` |
| |
`122` | `134` |
| |
`123` | `135` |
| |
`124` |
| `-` | |
| `136` | `+` | |
| `137` | `+` | |
| `138` | `+` | |
`125` | `139` |
| |
`126` | `140` |
| |
`127` | `141` |
| |
`128` | `142` |
| |
`129` | `143` |
| |
| `144` | `+` | |
| `145` | `+` | |
| `146` | `+` | |
| `147` | `+` | |
`130` | `148` |
| |
`131` | `149` |
| |
`132` | `150` |
| |
| |||
`176` | `194` |
| |
`177` | `195` |
| |
`178` | `196` |
| |
`179` |
| `-` | |
`180` |
| `-` | |
| `197` | `+` | |
| `198` | `+` | |
| `199` | `+` | |
| `200` | `+` | |
| `201` | `+` | |
`181` | `202` |
| |
`182` | `203` |
| |
| `204` | `+` | |
| `205` | `+` | |
`183` | `206` |
| |
`184` | `207` |
| |
`185` | `208` |
| |
`186` | `209` |
| |
| `210` | `+` | |
| `211` | `+` | |
`187` | `212` |
| |
`188` | `213` |
| |
`189` | `214` |
| |
| `215` | `+` | |
| `216` | `+` | |
| `217` | `+` | |
| `218` | `+` | |
| `219` | `+` | |
| `220` | `+` | |
| `221` | `+` | |
| `222` | `+` | |
| `223` | `+` | |
| `224` | `+` | |
| `225` | `+` | |
| `226` | `+` | |
| `227` | `+` | |
| `228` | `+` | |
| `229` | `+` | |
| `230` | `+` | |
| `231` | `+` | |
| `232` | `+` | |
| `233` | `+` | |
| `234` | `+` | |
| `235` | `+` | |
| `236` | `+` | |
| `237` | `+` | |
| `238` | `+` | |
| `239` | `+` | |
| `240` | `+` | |
| `241` | `+` | |
| `242` | `+` | |
| `243` | `+` | |
| `244` | `+` | |
| `245` | `+` | |
| `246` | `+` | |
| `247` | `+` | |
| `248` | `+` | |
| `249` | `+` | |
| `250` | `+` | |
| `251` | `+` | |
| `252` | `+` | |
| `253` | `+` | |
| `254` | `+` | |
| `255` | `+` | |
| `256` | `+` | |
| `257` | `+` | |
| `258` | `+` | |
| `259` | `+` | |
| `260` | `+` | |
| `261` | `+` | |
| `262` | `+` | |
| `263` | `+` | |
| `264` | `+` | |
| `265` | `+` | |
| `266` | `+` | |
| `267` | `+` | |
| `268` | `+` | |
| `269` | `+` | |
| `270` | `+` | |
`190` | `271` |
| |
`191` | `272` |
| |
`192` | `273` |
| |
| |||
`459` | `540` |
| |
`460` | `541` |
| |
`461` | `542` |
| |
| `543` | `+` | |
| `544` | `+` | |
| `545` | `+` | |
| `546` | `+` | |
| `547` | `+` | |
| `548` | `+` | |
| `549` | `+` | |
| `550` | `+` | |
`462` | `551` |
| |
`463` | `552` |
| |
`464` | `553` |
| |
`465` | `554` |
| |
| `555` | `+` | |
`466` | `556` |
| |
`467` | `557` |
| |
`468` | `558` |
| |
`469` | `559` |
| |
`470` | `560` |
| |
| `561` | `+` | |
`471` | `562` |
| |
`472` | `563` |
| |
`473` | `564` |
| |
`474` | `565` |
| |
`475` | `566` |
| |
| `567` | `+` | |
`476` | `568` |
| |
`477` | `569` |
| |
`478` | `570` |
| |
`479` | `571` |
| |
`480` | `572` |
| |
| `573` | `+` | |
`481` | `574` |
| |
`482` | `575` |
| |
`483` | `576` |
| |
`484` | `577` |
| |
`485` | `578` |
| |
| `579` | `+` | |
`486` | `580` |
| |
`487` | `581` |
| |
`488` | `582` |
| |
| |||
`491` | `585` |
| |
`492` | `586` |
| |
`493` | `587` |
| |
| `588` | `+` | |
| `589` | `+` | |
| `590` | `+` | |
| `591` | `+` | |
| `592` | `+` | |
| `593` | `+` | |
`494` | `594` |
| |
`495` | `595` |
| |
`496` | `596` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`23` | `23` |
| |
`24` | `24` |
| |
`25` | `25` |
| |
| `26` | `+` | |
`26` | `27` |
| |
`27` | `28` |
| |
`28` | `29` |
| |
| |||
`86` | `87` |
| |
`87` | `88` |
| |
`88` | `89` |
| |
| `90` | `+` | |
| `91` | `+` | |
| `92` | `+` | |
| `93` | `+` | |
| `94` | `+` | |
| `95` | `+` | |
`89` | `96` |
| |
`90` | `97` |
| |
`91` | `98` |
| |
| |||
`147` | `154` |
| |
`148` | `155` |
| |
`149` | `156` |
| |
| `157` | `+` | |
| `158` | `+` | |
| `159` | `+` | |
`150` | `160` |
| |
`151` | `161` |
| |
`152` | `162` |
| |
| |||
`159` | `169` |
| |
`160` | `170` |
| |
`161` | `171` |
| |
| `172` | `+` | |
| `173` | `+` | |
| `174` | `+` | |
| `175` | `+` | |
| `176` | `+` | |
| `177` | `+` | |
| `178` | `+` | |
| `179` | `+` | |
| `180` | `+` | |
| `181` | `+` | |
| `182` | `+` | |
| `183` | `+` | |
| `184` | `+` | |
| `185` | `+` | |
| `186` | `+` | |
| `187` | `+` | |
| `188` | `+` | |
| `189` | `+` | |
| `190` | `+` | |
| `191` | `+` | |
| `192` | `+` | |
| `193` | `+` | |
| `194` | `+` | |
| `195` | `+` | |
| `196` | `+` | |
| `197` | `+` | |
| `198` | `+` | |
| `199` | `+` | |
| `200` | `+` | |
| `201` | `+` | |
| `202` | `+` | |
| `203` | `+` | |
| `204` | `+` | |
| `205` | `+` | |
| `206` | `+` | |
| `207` | `+` | |
| `208` | `+` | |
| `209` | `+` | |
| `210` | `+` | |
| `211` | `+` | |
| `212` | `+` | |
| `213` | `+` | |
| `214` | `+` | |
| `215` | `+` | |
| `216` | `+` | |
| `217` | `+` | |
| `218` | `+` | |
| `219` | `+` | |
| `220` | `+` | |
| `221` | `+` | |
| `222` | `+` | |
| `223` | `+` | |
| `224` | `+` | |
| `225` | `+` | |
| `226` | `+` | |
| `227` | `+` | |
| `228` | `+` | |
| `229` | `+` | |
| `230` | `+` | |
| `231` | `+` | |
| `232` | `+` | |
| `233` | `+` | |
| `234` | `+` | |
| `235` | `+` | |
| `236` | `+` | |
`162` | `237` |
| |
`163` | `238` |
| |
`164` | `239` |
| |
| |||
`319` | `394` |
| |
`320` | `395` |
| |
`321` | `396` |
| |
| `397` | `+` | |
| `398` | `+` | |
| `399` | `+` | |
| `400` | `+` | |
| `401` | `+` | |
| `402` | `+` | |
| `403` | `+` | |
`322` | `404` |
| |
`323` | `405` |
| |
`324` | `406` |
| |
| |||
`817` | `899` |
| |
`818` | `900` |
| |
`819` | `901` |
| |
| `902` | `+` | |
| `903` | `+` | |
| `904` | `+` | |
| `905` | `+` | |
| `906` | `+` | |
| `907` | `+` | |
| `908` | `+` | |
| `909` | `+` | |
| `910` | `+` | |
| `911` | `+` | |
| `912` | `+` | |
| `913` | `+` | |
| `914` | `+` | |
`820` | `915` |
| |
`821` | `916` |
| |
`822` | `917` |
| |
|

## 0 commit comments