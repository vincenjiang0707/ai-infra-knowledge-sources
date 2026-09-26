# [Issue #1983] UCX SRD backend: NIXL_ERR_REMOTE_DISCONNECT

source: https://github.com/ai-dynamo/nixl/issues/1983
state: closed | updated: 2026-09-14T13:15:26Z
labels: Network

## 正文

When using through sglang, seeing NIXL_ERR_REMOTE_DISCONNECT when a prefill container tries to connect with a newly started decode container via UCX SRD backend (Amazon EFA) on B200 instances. This error causes the remote agent to be deregistered and all subsequent transfers to that decode container to fail (even though the container is eventually reachable by this and other prefill containers).

Prefill log:

```
[2026-07-21 08:04:41] Processing ChatCompletion request a04107cc-ff53-49ba-b428-03eb77df5cd5 from workspace 6051921418418893, priority=REQUEST_PRIORITY_TYPE_DEFAULT, no images, has_json_schema=False, has_tools=False
[2026-07-21 08:04:41 TP0 EP0] Prefill batch, #new-seq: 1, #new-token: 64, #cached-token: 10048, token usage: 0.00, #running-req: 0, #queue-req: 0, #pending-token: 0, #bootstrap-req: 0, #inflight-req: 1, cuda graph: False, input throughput (token/s): 178.18, est. prefill TFLOPS/s (per GPU): 9.90, fwd occupancy: nan%
[1784621081.896649] [kimi-k2-7-disagg-on-sp-v1-prefill-92c6hc-07210529-x04q3qgn-pod:537  :1]       srd_iface.c:221  UCX  ERROR send completion[0] with error on rdmap132s0/0x55cf4425cfb0: Work Request Flushed Error, vendor_err 0x1 wr_id 0x7f8b20022480
[1784621081.896667] [kimi-k2-7-disagg-on-sp-v1-prefill-92c6hc-07210529-x04q3qgn-pod:532  :0]       srd_iface.c:221  UCX  ERROR send completion[0] with error on rdmap96s0/0x55f989790220: Work Request Flushed Error, vendor_err 0x1 wr_id 0x7f676c7db240
[1784621081.896648] [kimi-k2-7-disagg-on-sp-v1-prefill-92c6hc-07210529-x04q3qgn-pod:537  :0]       srd_iface.c:221  UCX  ERROR send completion[0] with error on rdmap133s0/0x55cf44182010: Work Request Flushed Error, vendor_err 0x1 wr_id 0x7f8b1c0f6b00
[1784621081.896690] [kimi-k2-7-disagg-on-sp-v1-prefill-92c6hc-07210529-x04q3qgn-pod:537  :1]       srd_iface.c:221  UCX  ERROR send completion[0] with error on rdmap133s0/0x55cf4426f190: Work Request Flushed Error, vendor_err 0x1 wr_id 0x7f8b2002f640
[1784621081.896698] [kimi-k2-7-disagg-on-sp-v1-prefill-92c6hc-07210529-x04q3qgn-pod:535  :0]       srd_iface.c:221  UCX  ERROR send completion[0] with error on rdmap114s0/0x56115409a620: Work Request Flushed Error, vendor_err 0x1 wr_id 0x7edf1c0f7100
[1784621081.896699] [kimi-k2-7-disagg-on-sp-v1-prefill-92c6hc-07210529-x04q3qgn-pod:535  :2]       srd_iface.c:221  UCX  ERROR send completion[0] with error on rdmap113s0/0x56116b616690: Work Request Flushed Error, vendor_err 0x1 wr_id 0x7ef0e402c040
[1784621081.896698] [kimi-k2-7-disagg-on-sp-v1-prefill-92c6hc-07210529-x04q3qgn-pod:535  :1]       srd_iface.c:221  UCX  ERROR send completion[0] with error on rdmap113s0/0x561163328810: Work Request Flushed Error, vendor_err 0x1 wr_id 0x7edf2802b380
[1784621081.896738] [kimi-k2-7-disagg-on-sp-v1-prefill-92c6hc-07210529-x04q3qgn-pod:535  :2]       srd_iface.c:221  UCX  ERROR send completion[0] with error on rdmap114s0/0x56116b628470: Work Request Flushed Error, vendor_err 0x1 wr_id 0x7ef0e402d480
[1784621081.896743] [kimi-k2-7-disagg-on-sp-v1-prefill-92c6hc-07210529-x04q3qgn-pod:532  :1]       srd_iface.c:221  UCX  ERROR send completion[0] with error on rdmap97s0/0x55f978df56e0: Work Request Flushed Error, vendor_err 0x1 wr_id 0x7f67600f8780
[1784621081.896721] [kimi-k2-7-disagg-on-sp-v1-prefill-92c6hc-07210529-x04q3qgn-pod:535  :3]       srd_iface.c:221  UCX  ERROR send completion[0] with error on rdmap114s0/0x5611541fd5d0: Work Request Flushed Error, vendor_err 0x1 wr_id 0x7edf14037240
[1784621081.896749] [kimi-k2-7-disagg-on-sp-v1-prefill-92c6hc-07210529-x04q3qgn-pod:535  :1]       srd_iface.c:221  UCX  ERROR send completion[0] with error on rdmap114s0/0x56116333a910: Work Request Flushed Error, vendor_err 0x1 wr_id 0x7edf28015a00
[1784621081.896764] [kimi-k2-7-disagg-on-sp-v1-prefill-92c6hc-07210529-x04q3qgn-pod:532  :1]       srd_iface.c:221  UCX  ERROR send completion[0] with error on rdmap96s0/0x55f978d95460: Work Request Flushed Error, vendor_err 0x1 wr_id 0x7f67600eabc0
[1784621081.896780] [kimi-k2-7-disagg-on-sp-v1-prefill-92c6hc-07210529-x04q3qgn-pod:532  :2]       srd_iface.c:221  UCX  ERROR send completion[0] with error on rdmap97s0/0x55f978d08980: Work Request Flushed Error, vendor_err 0x1 wr_id 0x7f676803a380
[1784621081.896783] [kimi-k2-7-disagg-on-sp-v1-prefill-92c6hc-07210529-x04q3qgn-pod:531  :0]       srd_iface.c:221  UCX  ERROR send completion[0] with error on rdmap80s0/0x55a46edd9270: Work Request Flushed Error, vendor_err 0x1 wr_id 0x7fc1d80e6980
[1784621081.896792] [kimi-k2-7-disagg-on-sp-v1-prefill-92c6hc-07210529-x04q3qgn-pod:532  :3]       srd_iface.c:221  UCX  ERROR send completion[0] with error on rdmap96s0/0x55f9b8315540: Work Request Flushed Error, vendor_err 0x1 wr_id 0x7f677c070340
[1784621081.896803] [kimi-k2-7-disagg-on-sp-v1-prefill-92c6hc-07210529-x04q3qgn-pod:531  :0]       srd_iface.c:221  UCX  ERROR send completion[0] with error on rdmap79s0/0x55a484e8fb30: Work Request Flushed Error, vendor_err 0x1 wr_id 0x7fc1d80e3300
[1784621081.896845] [kimi-k2-7-disagg-on-sp-v1-prefill-92c6hc-07210529-x04q3qgn-pod:532  :4]       srd_iface.c:221  UCX  ERROR send completion[0] with error on rdmap97s0/0x55f9afe62400: Work Request Flushed Error, vendor_err 0x1 wr_id 0x7f6764057500
[2026-07-21 08:04:41 TP1 EP1] NIXL transport error for room 6555093254675405189: NIXL_ERR_REMOTE_DISCONNECT
[2026-07-21 08:04:41 TP2 EP2] NIXL transport error for room 6555093254675405189: NIXL_ERR_REMOTE_DISCONNECT
[2026-07-21 08:04:41 TP7 EP7] NIXL transport error for room 6555093254675405189: NIXL_ERR_REMOTE_DISCONNECT
[2026-07-21 08:04:41 TP5 EP5] NIXL transport error for room 6555093254675405189: NIXL_ERR_REMOTE_DISCONNECT
[2026-07-21 08:04:41 TP7 EP7] Prefill transfer failed for request rank=7 req.rid='a04107cc-ff53-49ba-b428-03eb77df5cd5' req.bootstrap_room=6555093254675405189 with exception NIXL_ERR_REMOTE_DISCONNECT
[2026-07-21 08:04:41 TP5 EP5] Prefill transfer failed for request rank=5 req.rid='a04107cc-ff53-49ba-b428-03eb77df5cd5' req.bootstrap_room=6555093254675405189 with exception NIXL_ERR_REMOTE_DISCONNECT
[2026-07-21 08:04:41 TP2 EP2] Prefill transfer failed for request rank=2 req.rid='a04107cc-ff53-49ba-b428-03eb77df5cd5' req.bootstrap_room=6555093254675405189 with exception NIXL_ERR_REMOTE_DISCONNECT
[2026-07-21 08:04:41 TP1 EP1] Prefill transfer failed for request rank=1 req.rid='a04107cc-ff53-49ba-b428-03eb77df5cd5' req.bootstrap_room=6555093254675405189 with exception NIXL_ERR_REMOTE_DISCONNECT
```

and later (due to this agent being deregistered):

```
[2026-07-21 08:06:26 TP0 EP0] Prefill batch, #new-seq: 2, #new-token: 20224, #cached-token: 0, token usage: 0.01, #running-req: 0, #queue-req: 7, #pending-token: 0, #bootstrap-req: 0, #inflight-req: 2, cuda graph: False, input throughput (token/s): 192.82, est. prefill TFLOPS/s (per GPU): 11.68, fwd occupancy: nan%
E0721 08:06:26.781179    4330 nixl_agent.cpp:866] createXferReq: metadata for remote agent 'def7d2f1-d482-4cd2-b6de-f238da5a9c70' not found
E0721 08:06:26.781494    4335 nixl_agent.cpp:866] createXferReq: metadata for remote agent '390c595a-d982-42f8-9cb5-eaaf9e73226a' not found
E0721 08:06:26.781445    4340 nixl_agent.cpp:866] createXferReq: metadata for remote agent '40ed030f-2f55-4d2c-88c7-84f70da8adbb' not found
E0721 08:06:26.781833    4360 nixl_agent.cpp:866] createXferReq: metadata for remote agent '078831fd-5331-4dc5-b9b0-f254af40cc08' not found
[2026-07-21 08:06:26 TP1 EP1] Unexpected transfer worker error for room 5839938415251080346
Traceback (most recent call last):
  File "/databricks/inference_entrypoint.runfiles/_main/model-serving/serving-engine/sglang/python/sglang/srt/disaggregation/nixl/conn.py", line 568, in transfer_worker
    kv_xfer_handle = self.send_kvcache(
                     ^^^^^^^^^^^^^^^^^^
  File "/databricks/inference_entrypoint.runfiles/_main/model-serving/serving-engine/sglang/python/sglang/srt/disaggregation/nixl/conn.py", line 845, in send_kvcache
    return self._send_kvcache_generic(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/databricks/inference_entrypoint.runfiles/_main/model-serving/serving-engine/sglang/python/sglang/srt/disaggregation/nixl/conn.py", line 822, in _send_kvcache_generic
    xfer_handle = self.agent.initialize_xfer(
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/databricks/inference_entrypoint.runfiles/.inference_entrypoint_sglang_0_5.venv/lib/python3.11/site-packages/nixl_cu13/_api.py", line 613, in initialize_xfer
    handle = self.agent.createXferReq(
             ^^^^^^^^^^^^^^^^^^^^^^^^^
nixl_cu13._bindings.nixlNotFoundError: NIXL_ERR_NOT_FOUND
```

This may be a port flapping issue with EFA on container startup (although the decode container is only able to transfer its agent metadata to the prefill after sglang has fully started, so several minutes after container start). It may be worth trying to re-register the failed agent within NIXL instead of immediately deregistering it on a single remote disconnect.

cc @mkhazraee @amitrad-aws 



## 评论 (3)

### amitrad-aws · 2026-07-23

Our recommendation is using LIBFABRIC backend when running over EFA, not the UCX backend.
Maybe @mkhazraee can comment on the UCX backend behavior.

### jjthomas · 2026-07-28

@amitrad-aws Do you know in what cases the "Work Request Flushed Error, vendor_err 0x1" (EFA_IO_COMP_STATUS_FLUSHED) comes from the device? Some documentation seems to suggest that it only happens when the QP is in permanent error state (https://github.com/amzn/amzn-drivers/blob/master/kernel/linux/efa/SRD.txt#L104), but that's not the case here since flows to other destinations are working.

### amitrad-aws · 2026-08-12

Thanks for the information on the repro.
The issue was root caused to an issue in EFA FW with stale SRD connections kept opened.
We have fixed the issue and it is pending deployment in the cloud.
We have also improved the CQE error coding so the error will be clearer next time and that is also pending deployment.
