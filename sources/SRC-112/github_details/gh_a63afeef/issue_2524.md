# [Issue #2524] [tilert] Open questions for PR #2523: dgxc infrastructure + runner access / PR #2523 待确认问题：dgxc 基础设施与 runner 资源

source: https://github.com/SemiAnalysisAI/InferenceX/issues/2524
state: closed | updated: 2026-09-07T09:10:48Z
labels: 

## 正文

## English

Tracking issue for the open questions on **#2523**.

We're the TileRT team (tile-ai/TileRT). PR #2523 is a draft adding
`framework: tilert` for GLM-5.1 FP8 on 8×B200, running PD-disaggregated: stock vLLM prefill
(`TileRTConnector` as `kv_producer`) → NIXL → TileRT `decode_server`, with an OpenAI-compatible
`pd_router` in front. No vLLM fork or patch. 584 insertions, 0 deletions — no existing line is
modified anywhere in the repo.

Already validated on our own 2×8×B200: 8k/1k at conc=1 gives **313.6 tok/s/user** (mean TPOT
3.19 ms), and the official gsm8k eval config gives **strict-match 0.9773 / flexible-extract
0.9757** against the 0.93 threshold.

**Two blockers are written up in the PR description** (GLM-5.1 is currently retired per
`MODELS.md:143`, and CODEOWNER ownership since our entry lands in `configs/nvidia-master.yaml`).

### Questions we cannot answer ourselves, having no cluster access

**1. GLM-5.1-FP8 weight path.** What is the exact path on dgxc? We currently guess
`/lustre/fsw/models/GLM-5.1-FP8`, by analogy with the existing `GLM-5-FP8` and `GLM-5-NVFP4`
entries in `launch_b200-dgxc.sh`. Since GLM-5.1 was retired in July, the weights may have been
cleaned up — if so, can they be re-staged?

**2. Converted-weight storage (~700 GiB) — and could you pre-stage it?** TileRT decode consumes
`weight_converter`'s 8-shard output, not the HF checkpoint. On our hardware that conversion took
**136 minutes and produced 153 files / 715 GB**. It is pure CPU work, so running it inside an
exclusive 16-GPU allocation is a significant waste of runner time. We currently write to
`/lustre/fsw/gharunners/models/<prefix>-<precision>-tilert-8shard` — chosen because
`/lustre/fsw/models` is SRE root-owned and `$GITHUB_WORKSPACE` is wiped per job by
`clean: true`, the same reasoning as the MiniMax-M3 precedent at `launch_b200-dgxc.sh:71-73`.

- Is that tree writable, and does it have ~700 GB free?
- **Strongly preferred:** if you can pre-stage the 8-shard directory once, our cache check
  (`model.safetensors.index.json` present) hits immediately and conversion is skipped entirely
  on every run. Happy to provide the exact conversion command.

**3. `flock` on the dgxc lustre mount.** Our conversion step takes a cross-node write lock so two
concurrent sweeps cannot corrupt the shared output directory. Lustre does not enable `flock` by
default — with no mount option the call can succeed without actually locking, and `localflock`
only works within a single node. Is the dgxc lustre mounted with `-o flock`? If not, the guard is
a silent no-op and two concurrent sweeps could both start a 700 GB write into the same directory.
(This becomes moot if you pre-stage the weights per question 2.)

**4. RDMA capabilities under enroot/pyxis.** NIXL moves KV across nodes over RDMA, which needs
(a) the verbs device nodes `/dev/infiniband/uverbs*` visible inside the container and
(b) unlimited memlock, since RDMA pins memory. Under docker we pass `--device /dev/infiniband`
and `--cap-add CAP_IPC_LOCK`. What is the equivalent on your pyxis setup — are both already
available inside benchmark containers, or does something need enabling cluster-side? Our script
runs a preflight that **warns rather than aborts**, so a misconfiguration would surface as a slow
or failing KV transfer rather than a clear error.

**5. UCX NIC pinning on `b200-multinode`.** We set
`UCX_NET_DEVICES=mlx5_0:1,mlx5_1:1,mlx5_2:1,mlx5_3:1,mlx5_4:1,mlx5_5:1,mlx5_10:1,mlx5_11:1`,
copied verbatim from the in-tree recipes referenced by `dsv4-fp4-b200-dynamo-vllm` — same
`runner: b200-multinode`, same `kv-p2p-transfer: nixl`, same disagg shape. Can you confirm that
NIC list is correct for the machines behind that label? Left unpinned, UCX may pick the
management NIC and KV transfer collapses.

**6. `all-evals` for a conc=1 entry.** `mark_eval_entries()` requires `conc >= MIN_EVAL_CONC`
(16), and TileRT decode is bs=1-only so our `conc-list` is `[1]`. A default full-sweep therefore
never schedules evals for this entry. We plan to carry `all-evals` alongside
`full-sweep-fail-fast`. Is that the intended mechanism for a legitimately single-point config, or
would you prefer something else?

**7. Can we use the `b200-multinode` runner pool?** That label maps to three machines
(`b200-dgxc-slurm_7/8/9`) and we need two of them held exclusively. See the timing table below
for how long. Is that acceptable, and is there a window you would prefer we use or avoid?

**Resource footprint, for planning.** Measured on our hardware — 2 nodes held exclusively:

| Phase | Time |
|---|---|
| Weight conversion (first run only, skipped if pre-staged) | ~136 min |
| Model load + PD handshake | ~30 min |
| Throughput bench, both ISL points | ~2 min |
| gsm8k full 1319 samples at conc=1 | 33–53 min |
| **Total, first run** | **~3.5–4 h** |
| **Total, with weights already staged** | **~1.5 h** |

That fits inside the 480-minute `timeout-minutes` on the multinode template, but we wanted to
flag it since `b200-multinode` has only three machines and we occupy two.

---

## 中文

本 issue 用于跟踪 **#2523** 的待确认问题。

我们是 TileRT 团队（tile-ai/TileRT）。PR #2523 是一个 draft PR，为 8×B200 上的
GLM-5.1 FP8 新增 `framework: tilert`，以 PD 分离方式运行：原版 vLLM 负责 prefill
（`TileRTConnector` 作为 `kv_producer`）→ NIXL → TileRT `decode_server`，前面是 OpenAI 兼容的
`pd_router`。不 fork 也不 patch vLLM。584 行新增、0 行删除 —— 全仓没有修改任何既有行。

已在我们自有的 2×8×B200 上验证：8k/1k、conc=1 下 **313.6 tok/s/user**（平均 TPOT 3.19 ms）；
官方 gsm8k eval 配置下 **strict-match 0.9773 / flexible-extract 0.9757**，阈值 0.93 达标。

**两个阻塞项已写在 PR 描述里**（`MODELS.md:143` 记录 GLM-5.1 已退役；以及 CODEOWNER 归属，因为
我们的条目落在 `configs/nvidia-master.yaml`）。

### 我们没有集群访问权、无法自行回答的问题

**1. GLM-5.1-FP8 权重路径。** dgxc 上的确切路径是什么？我们目前填的是猜测值
`/lustre/fsw/models/GLM-5.1-FP8`，依据是 `launch_b200-dgxc.sh` 里既有的 `GLM-5-FP8` 与
`GLM-5-NVFP4` 条目。由于 GLM-5.1 在 7 月已退役，权重可能已被清理 —— 若是如此，能否重新预置？

**2. 转换产物存放（约 700 GiB）—— 能否由你们预置？** TileRT 解码吃的是 `weight_converter`
产出的 8-shard，而不是 HF 原始权重。在我们的机器上这次转换耗时 **136 分钟，产出 153 个文件 /
715 GB**。这是纯 CPU 工作，跑在独占的 16 卡分配里对 runner 时间是明显的浪费。我们目前写到
`/lustre/fsw/gharunners/models/<prefix>-<precision>-tilert-8shard` —— 之所以选这里，是因为
`/lustre/fsw/models` 是 SRE root-owned，而 `$GITHUB_WORKSPACE` 会被 `clean: true` 每个 job
清掉，与 `launch_b200-dgxc.sh:71-73` 处 MiniMax-M3 的先例同理。

- 这个树可写吗？有约 700 GB 空闲吗？
- **我们更希望的方案：** 如果你们能一次性预置好 8-shard 目录，我们的缓存判据
  （存在 `model.safetensors.index.json`）会立即命中，之后每次运行都完全跳过转换。
  可以提供确切的转换命令。

**3. dgxc lustre 挂载的 `flock`。** 我们的转换步骤会取一把跨节点写锁，避免两个并发 sweep
破坏共享产物目录。Lustre 默认**不启用** `flock` —— 不加挂载选项时该调用可能返回成功却并未真正
加锁，而 `localflock` 只在单节点内有效。dgxc 的 lustre 是否以 `-o flock` 挂载？如果不是，这层
保护会静默失效，两个并发 sweep 可能同时向同一目录写入 700 GB。（若按问题 2 预置权重，此问题
自然消失。）

**4. enroot/pyxis 下的 RDMA 能力。** NIXL 通过 RDMA 跨节点搬运 KV，需要两个条件：
(a) 容器内可见 verbs 设备节点 `/dev/infiniband/uverbs*`；(b) memlock 不受限，因为 RDMA 需要
锁页内存。docker 下我们传入 `--device /dev/infiniband` 和 `--cap-add CAP_IPC_LOCK`。在你们的
pyxis 环境中对应配置是什么 —— benchmark 容器内这两项是否已经具备，还是需要集群侧开启？我们脚本
里的 preflight **只告警不中止**，因此配置缺失会表现为 KV 传输很慢或失败，而不是明确报错。

**5. `b200-multinode` 上的 UCX 网卡绑定。** 我们设置
`UCX_NET_DEVICES=mlx5_0:1,mlx5_1:1,mlx5_2:1,mlx5_3:1,mlx5_4:1,mlx5_5:1,mlx5_10:1,mlx5_11:1`，
逐字抄自 `dsv4-fp4-b200-dynamo-vllm` 所引用的在树 recipe —— 同一个 `runner: b200-multinode`、
同样的 `kv-p2p-transfer: nixl`、同样的 disagg 形态。能否确认这份网卡列表对该 label 背后的机器
是正确的？不绑定的话 UCX 可能选到管理网口，KV 传输会崩溃式变慢。

**6. conc=1 条目的 `all-evals`。** `mark_eval_entries()` 要求 `conc >= MIN_EVAL_CONC`（16），
而 TileRT 解码只支持 bs=1，所以我们的 `conc-list` 是 `[1]`。默认 full-sweep 因此永远不会为这个
条目排 eval。我们计划在 `full-sweep-fail-fast` 之外额外打 `all-evals`。对于一个确实只能出单点的
配置，这是你们预期的机制吗，还是更希望我们用别的方式？

**7. 我们能使用 `b200-multinode` runner 资源吗？** 该 label 对应三台机器
（`b200-dgxc-slurm_7/8/9`），我们需要独占其中两台。占用时长见下方时间表。这是否可接受？
有没有希望我们使用或避开的时间窗口？

**资源占用预估，供你们排期参考。** 以下为我们机器上的实测 —— 独占 2 个节点：

| 阶段 | 耗时 |
|---|---|
| 权重转换（仅首次，若已预置则跳过） | 约 136 分钟 |
| 模型加载 + PD 握手 | 约 30 分钟 |
| 吞吐 bench，两个 ISL 点 | 约 2 分钟 |
| gsm8k 全量 1319 题、conc=1 | 33–53 分钟 |
| **首次运行合计** | **约 3.5–4 小时** |
| **权重已预置时合计** | **约 1.5 小时** |

这在多节点模板的 480 分钟 `timeout-minutes` 之内，但考虑到 `b200-multinode` 只有三台机器而我们
要占用两台，还是提前说明一下。


---

🤖 Generated with [Claude Code](https://claude.com/claude-code)


## 评论 (1)

### Oseltamivir · 2026-08-07

1. GLM-5.1-FP8 weight path

July retirement cleaned it up, and the GLM-5-FP8 / GLM-5-NVFP4 paths at launch_b200-dgxc.sh:44,47 are stale too. Should be at `MODEL_PATH=/home/sa-shared/models/GLM-5.1-FP8`. May need `--container-mounts=…,$MODEL_PATH:$MODEL_PATH`

2. Converted-weight storage 

`/lustre/fsw/gharunners/models` is `sa-shared`-writable and already holds this exact kind of tree. But prefer /home/sa-shared/models/…-tilert-8shard: it's a separate Lustre filesystem from /lustre/fsw, currently 8.8T free versus 5.1T, so your 715 GB output doesn't compete with the model tree. Either is writable without root.

3. flock on the dgxc Lustre

Both mounts carry it and the same for `/home`. cluster-wide flock, not localflock

4. RDMA under enroot/pyxis 

Verified inside a pyxis container on an allocated node

 5. UCX NIC pinning

Use:
  `UCX_NET_DEVICES=mlx5_0:1,mlx5_1:1,mlx5_2:1,mlx5_3:1,mlx5_4:1,mlx5_5:1,mlx5_6:1,mlx5_7:1`

6. `all-evals`

Right mechanism, but use the PR label, not the changelog field. You don't have to use it, we'll add it if deemed necessary.

7. Pool usage 

Workable inside the 480-minute timeout. Please avoid stacking it against a full-sweep window; with the weights now pre-staged your first run should be closer to your ~1.5h figure than ~4h, which makes this much easier to fit.
