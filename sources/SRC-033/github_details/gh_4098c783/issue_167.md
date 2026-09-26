# [Issue #167] torch_npu.profiler 在 warmup → RECORD 跃迁时丢失窗口头部的设备侧数据，实际采集次数少于 active

source: https://github.com/Ascend/pytorch/issues/167
state: open | updated: 2026-09-11T07:55:50Z
labels: 

## 正文

简述:  
  使用 torch_npu.profiler.profile 的 schedule 机制时，输出的执行次数会偶发性低于active次数


环境（请按实际填写）
  - torch_npu 版本：<2.12.0>
  - CANN 版本：<9.2.0_beta.1>
  - 机器:A5, 950PR
  - 是否使用 torch_npu.profiler.tensorboard_trace_handler：是

  ---

  问题描述

  使用 torch_npu.profiler.profile 的 schedule 机制时，宿主侧按 active 次正好进入 RECORD 窗口，但落到 op_summary_*.csv 里的设备侧 task 记录数少于
  active，缺失全部集中在窗口头部（最早的若干次调用），窗口尾部完整。丢失次数不确定，同一份脚本重跑会变。

  复现脚本

  import torch
  import torch_npu

  def run_once():
      a = torch.randn(1024, 1024, dtype=torch.float16).npu()
      b = torch.randn(1024, 1024, dtype=torch.float16).npu()
      torch.matmul(a, b)

  wait, warmup, active, repeat, skip_first = 1, 6, 10, 1, 1
  total_steps = repeat * (wait + warmup + active) + skip_first   # = 18

  with torch_npu.profiler.profile(
      activities=[torch_npu.profiler.ProfilerActivity.NPU],
      schedule=torch_npu.profiler.schedule(
          wait=wait, warmup=warmup, active=active,
          repeat=repeat, skip_first=skip_first),
      on_trace_ready=torch_npu.profiler.tensorboard_trace_handler("./prof_out"),
  ) as prof:
      for _ in range(total_steps):
          torch.npu.synchronize()
          run_once()                      # 每次调用 = 1 个 matmul kernel
          torch.npu.synchronize()
          prof.step()

  预期： op_summary_*.csv 中出现 10 条 matmul 记录（= active）。
  实际： 出现 8 条（偶发 9 条），缺的是最前面 2 条；重复运行结果不稳定。

  关键证据

  1. 宿主侧没丢，设备侧丢了。 同一份 trace 中 host,node,launch 的 Count 恰好等于 active（10），证明宿主确实在 RECORD 窗口内发起了 10 次 kernel 下发；而设备侧 task 记录只有 8 条。
  2. 只丢头部。 缺失的 task_id 是窗口内最小的若干个；两份不同的 trace tail 都结束在相同的 task_id，末尾紧跟一条 PLACE_HOLDER_SQE（时长
     0.007µs）。即：停止边界是干净的，开始边界不是。
  3. 非确定性。 同一目标、同一 shape、同样约 90µs/次的下发节奏，一次丢 0、一次丢 2；换成 fp32（单次耗时更长）丢 0。丢失次数与单次调用耗时呈反相关。

  代码分析

  torch_npu/profiler/profiler_interface.py 中，停止路径与开始路径不对称：

  def stop_trace(self):
      if ProfilerActivity.NPU in self.activities:
          torch.npu.synchronize()          # ← 先等设备排空，再下发停止
      ...
      _stop_profiler()

  def start_trace(self):
      ...
      self.start_cnt = _get_syscnt()
      self.start_monotonic = _get_monotonic()
      _start_profiler(npu_prof_config, self.activities)   # ← 直接下发，无同步

  start_trace 由 _profiler_action_controller.py 的

  (ProfilerAction.WARMUP, ProfilerAction.RECORD): [self.prof_inst.start_trace],

  在 profile.step()（profiler.py 的 step() 内 transit_action(prev_action, self.current_action)）中触发。该调用在宿主线程内同步返回，没有等待设备侧的使能生效回执。

  推测根因： _start_profiler 下发的使能命令与计算流不在同一通道，落地存在延迟。start_trace() 返回后宿主立刻进入下一次迭代并把后续 kernel
  全部下发、执行完成；在使能真正生效之前执行的 task 就没有被记录。丢失次数 ≈ 使能延迟 ÷ 单次调用的设备耗时，因此短 kernel（fp16）丢得多、长
  kernel（fp32）丢得少，且抖动会导致结果不稳定。

  stop_trace 之所以没有这个问题，是因为它在下发前做了 torch.npu.synchronize()——但请注意：单纯在 start_trace 前补一句 synchronize
  未必足够，因为此处设备的任务队列本已排空，真正缺的是"命令落地"而非"任务完成"。

  影响

  - 依赖 sum(durations) / active 或 sum(durations) / 观测条数 的下游统计会系统性偏低（实测偏差 −10% ~ −20%）。
  - 需要按调用次数切分稳态窗口的分析（每次调用独占一段）无法进行，因为头部边界不可知。
  - 用户无法从 trace 中判断 RECORD 窗口的真实起点：record_steps=True 虽然每步会执行 mstx.range_start("ProfilerStep#N", current_stream())，但默认 msprof_tx=False，这些标记不会进入
    trace。

  建议

  1. start_trace 与 stop_trace 对齐：在 _start_profiler 前做流同步，并在其后引入可配置的等待（例如若干百微秒），确保使能已落地。
  2. 更彻底的方案：为 _start_profiler / _stop_profiler 增加设备侧回执，让 start_trace 能阻塞到"使能已生效"，而不是依赖时间猜测。
  3. 若短期无法修改，建议在文档中明确说明"RECORD 窗口起始处可能丢失若干次调用，统计时请以实际观测到的调用次数为准"，并在 msprof_tx=False 时输出告警，提示用户无法从 trace
     校验窗口边界。


## 评论 (1)

### ascend-robot · 2026-09-11

Hello,

This repo is only a mirror with no active development or maintenance.
All bug reports, questions and code contributions should be submitted via the original repository link below.
Thanks for your interest!

Original Repository Link: https://gitcode.com/Ascend/pytorch
