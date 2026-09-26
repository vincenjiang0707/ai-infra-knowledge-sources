source: https://github.com/vllm-project/guidellm/commit/291a6e609c3eb52d6eadcedecc7a056e396cd5eb

# Commit 291a6e6

committed

Bound token events by when they occur (

Modify the request bounding code to use different event bounds for each latency event. See [#1079](https://github.com/vllm-project/guidellm/pull/1079))[#1078](https://github.com/vllm-project/guidellm/issues/1078)for more details. Run a benchmark with warmup and verify differences in collected ttft, token throughput, etc. Note that when running a shorter concurrent run with rampup+warmup vs a longer run with no rampup+warmup the results of the shorter run should be closer than without this patch. ```sh guidellm run \ --backend kind=openai_http,target=

[http://127.0.0.1:8000](http://127.0.0.1:8000)--profile kind=concurrent,rampup_duration=45,warmup=75 \ --override profile.streams 200 --data "kind=synthetic_text,prompt_tokens=500,output_tokens=512" \ --constraint kind=max_duration,seconds=275 ``` - Resolves

[#1078](https://github.com/vllm-project/guidellm/issues/1078)--- - [x] "I certify that all code in this PR is my own, except as noted below." - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`](

[https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md](https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md)) file. --- commit

[Author: Samuel Monson <smonson@redhat.com> Date: Tue Sep 1 21:06:45 2026 +0000 Clip metrics by start/stop Only count thoughput that falls within start/stop and only count TTFTs that fall fully inside start/stop. Assisted-by: Codex Signed-off-by: Samuel Monson <smonson@redhat.com> commit](https://github.com/vllm-project/guidellm/commit/202b75d8b2837de269801aee34c8c4577257e6a3)

`202b75d`[Author: Samuel Monson <smonson@redhat.com> Date: Mon Sep 14 18:01:01 2026 -0400 Bound token latency events by when they occur TTFT, TTFOT, and ITL are all events the occur during the part of the request. When calculating which events are inside the main phase (happen after warmup and before cooldown) we want to bound by the event itself rather than the request. For first token also be a bit more strict and ensure that the whole event is within latency bounds. Signed-off-by: Samuel Monson <smonson@redhat.com> commit](https://github.com/vllm-project/guidellm/commit/efb83142c3dbc2b1fcc0b28c7788393e9f358aa9)

`efb8314`[Author: Samuel Monson <smonson@redhat.com> Date: Tue Sep 15 12:00:18 2026 -0400 Switch TTFT and TTFOT to open range When getting prefill events within the main range switch to including requests that partially overlap the main phase. This matches how other metrics are handled. It is still debatable which approch is better, since we are on a bit of a time crunch to get this out stick with this approch for now and do more testing in post. Signed-off-by: Samuel Monson <smonson@redhat.com> commit](https://github.com/vllm-project/guidellm/commit/b70695cebb03dafcb725545ea3a6a4e7e5830666)

`b70695c`[Author: Samuel Monson <smonson@redhat.com> Date: Tue Sep 15 17:48:30 2026 +0000 Fix and add tests Generated-by: Cursor Signed-off-by: Samuel Monson <smonson@redhat.com> commit](https://github.com/vllm-project/guidellm/commit/308d051cdc81ab2b545c53a04b834cd8f1c29a54)

`308d051`[Author: Samuel Monson <smonson@redhat.com> Date: Tue Sep 15 18:25:59 2026 +0000 Add a little documentation for warmup/cooldown Assisted-by: Cursor Signed-off-by: Samuel Monson <smonson@redhat.com> commit](https://github.com/vllm-project/guidellm/commit/91637e5655c83f6d5d10e593988c925e34eef141)

`91637e5`[Author: Samuel Monson <smonson@redhat.com> Date: Tue Sep 15 16:21:12 2026 -0400 Address review Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: Codex Assisted-by: Cursor Generated-by: Cursor Signed-off-by: Samuel Monson <smonson@redhat.com>](https://github.com/vllm-project/guidellm/commit/72fc6d5728d2c8bef60d492bf607b92beec69a16)

`72fc6d5`1 parent[67c2993]commit 291a6e6

5 files changed

Lines changed: 198 additions & 28 deletions

## File tree

- docs/guides
- src/guidellm
- benchmark/schemas
- schemas

- tests/unit/benchmark/schemas

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
| `75` | `+` | |
| `76` | `+` | |
| `77` | `+` | |
| `78` | `+` | |
| `79` | `+` | |
| `80` | `+` | |
| `81` | `+` | |
| `82` | `+` | |
| `83` | `+` | |
| `84` | `+` | |
| `85` | `+` | |
| `86` | `+` | |
| `87` | `+` | |
| `88` | `+` | |
| `89` | `+` | |
| `90` | `+` | |
| `91` | `+` | |
| `92` | `+` | |
| `93` | `+` | |
| `94` | `+` | |
| `95` | `+` | |
| `96` | `+` | |
| `97` | `+` | |
| `98` | `+` | |
| `99` | `+` | |
| `100` | `+` | |
`74` | `101` |
| |
`75` | `102` |
| |
`76` | `103` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`14` | `14` |
| |
`15` | `15` |
| |
`16` | `16` |
| |
| `17` | `+` | |
`17` | `18` |
| |
`18` | `19` |
| |
`19` | `20` |
| |
| |||
`615` | `616` |
| |
`616` | `617` |
| |
`617` | `618` |
| |
`618` |
| `-` | |
| `619` | `+` | |
| `620` | `+` | |
| `621` | `+` | |
| `622` | `+` | |
| `623` | `+` | |
| `624` | `+` | |
| `625` | `+` | |
| `626` | `+` | |
| `627` | `+` | |
| `628` | `+` | |
`619` | `629` |
| |
`620` | `630` |
| |
`621` | `631` |
| |
`622` | `632` |
| |
`623` |
| `-` | |
`624` |
| `-` | |
| `633` | `+` | |
| `634` | `+` | |
| `635` | `+` | |
| `636` | `+` | |
| `637` | `+` | |
| `638` | `+` | |
| `639` | `+` | |
| `640` | `+` | |
| `641` | `+` | |
`625` | `642` |
| |
`626` | `643` |
| |
`627` |
| `-` | |
`628` |
| `-` | |
`629` |
| `-` | |
`630` |
| `-` | |
`631` |
| `-` | |
`632` |
| `-` | |
`633` |
| `-` | |
`634` |
| `-` | |
`635` |
| `-` | |
`636` |
| `-` | |
`637` |
| `-` | |
`638` |
| `-` | |
`639` |
| `-` | |
`640` |
| `-` | |
`641` |
| `-` | |
| `644` | `+` | |
| `645` | `+` | |
| `646` | `+` | |
| `647` | `+` | |
| `648` | `+` | |
| `649` | `+` | |
| `650` | `+` | |
| `651` | `+` | |
| `652` | `+` | |
| `653` | `+` | |
| `654` | `+` | |
| `655` | `+` | |
| `656` | `+` | |
| `657` | `+` | |
| `658` | `+` | |
| `659` | `+` | |
| `660` | `+` | |
| `661` | `+` | |
| `662` | `+` | |
| `663` | `+` | |
| `664` | `+` | |
| `665` | `+` | |
| `666` | `+` | |
`642` | `667` |
| |
`643` | `668` |
| |
`644` | `669` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`933` | `933` |
| |
`934` | `934` |
| |
`935` | `935` |
| |
| `936` | `+` | |
| `937` | `+` | |
`936` | `938` |
| |
`937` | `939` |
| |
`938` |
| `-` | |
`939` |
| `-` | |
`940` |
| `-` | |
| `940` | `+` | |
| `941` | `+` | |
| `942` | `+` | |
| `943` | `+` | |
| `944` | `+` | |
| `945` | `+` | |
| `946` | `+` | |
| `947` | `+` | |
| `948` | `+` | |
| `949` | `+` | |
| `950` | `+` | |
| `951` | `+` | |
| `952` | `+` | |
| `953` | `+` | |
| `954` | `+` | |
`941` | `955` |
| |
`942` | `956` |
| |
`943` | `957` |
| |
`944` |
| `-` | |
`945` |
| `-` | |
`946` |
| `-` | |
| `958` | `+` | |
| `959` | `+` | |
| `960` | `+` | |
| `961` | `+` | |
| `962` | `+` | |
| `963` | `+` | |
| `964` | `+` | |
| `965` | `+` | |
| `966` | `+` | |
| `967` | `+` | |
| `968` | `+` | |
| `969` | `+` | |
| `970` | `+` | |
| `971` | `+` | |
| `972` | `+` | |
`947` | `973` |
| |
`948` | `974` |
| |
`949` | `975` |
| |
| |||
`959` | `985` |
| |
`960` | `986` |
| |
`961` | `987` |
| |
`962` |
| `-` | |
`963` |
| `-` | |
`964` |
| `-` | |
| `988` | `+` | |
| `989` | `+` | |
| `990` | `+` | |
| `991` | `+` | |
| `992` | `+` | |
| `993` | `+` | |
| `994` | `+` | |
| `995` | `+` | |
| `996` | `+` | |
| `997` | `+` | |
| `998` | `+` | |
| `999` | `+` | |
| `1000` | `+` | |
| `1001` | `+` | |
| `1002` | `+` | |
`965` | `1003` |
| |
`966` | `1004` |
| |
`967` | `1005` |
| |
`968` | `1006` |
| |
`969` | `1007` |
| |
`970` | `1008` |
| |
| `1009` | `+` | |
| `1010` | `+` | |
`971` | `1011` |
| |
`972` | `1012` |
| |
`973` | `1013` |
| |
`974` | `1014` |
| |
`975` | `1015` |
| |
`976` | `1016` |
| |
| `1017` | `+` | |
| `1018` | `+` | |
`977` | `1019` |
| |
`978` | `1020` |
| |
`979` | `1021` |
| |
`980` | `1022` |
| |
`981` | `1023` |
| |
`982` | `1024` |
| |
| `1025` | `+` | |
| `1026` | `+` | |
`983` | `1027` |
| |
`984` | `1028` |
| |
`985` | `1029` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`237` | `237` |
| |
`238` | `238` |
| |
`239` | `239` |
| |
`240` |
| `-` | |
| `240` | `+` | |
`241` | `241` |
| |
`242` | `242` |
| |
`243` | `243` |
| |
| |||
`279` | `279` |
| |
`280` | `280` |
| |
`281` | `281` |
| |
| `282` | `+` | |
| `283` | `+` | |
| `284` | `+` | |
| `285` | `+` | |
| `286` | `+` | |
| `287` | `+` | |
| `288` | `+` | |
`282` | `289` |
| |
`283` | `290` |
| |
`284` | `291` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`153` | `153` |
| |
`154` | `154` |
| |
`155` | `155` |
| |
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
| `222` | `+` |

## 0 commit comments