# [Issue #1110] NIXL ep doesn't work on GB200 with cuda_ipc disabled

source: https://github.com/ai-dynamo/nixl/issues/1110
state: closed | updated: 2026-06-25T09:09:11Z
labels: Network, NIXL EP

## 正文

**Brief:**<br>When running nixl_ep's [elastic.py](<http://elastic.py>) benchmark from a machine with GB200 we get an error:<br>"UCX  ERROR failed to select lane for local device GPU0"

Note that out of the box, the project's docker image is created with UCX_TLS set to *^cuda_ipc*.

Do note that after unsetting UCX_TLS (or setting it to *all*) and making sure it doesn't get set elsewhere in the code (e.g. in nixl_ep's [buffer.py](<http://buffer.py>)) the benchmark completes successfully.

**Environment:**

* oci-hsg cluster machine
* GPU: GB200
* Container created by running:<br>*sudo contrib/build-container.sh --build-nixl-ep --arch aarm64*

**Once mounted run:**<br>*cd /workspace/nixl**<br>**HOST_IP=$(hostname -I | awk '{print $1}')**<br>**etcd --listen-client-urls *[*http://0.0.0.0:2379*](<http://0.0.0.0:2379>)* --advertise-client-urls *[*http://$*](<http://$>)*{HOST_IP}:2379 &**<br>**sleep 2**<br>**python examples/cpp/nixl_ep/tests/elastic/elastic.py *<br>*--plan examples/cpp/nixl_ep/tests/elastic/no_expansion.json *<br>*--num-processes 4 *<br>*--nvlink-backend ipc*

**Error:**<br>*1765457011.052824\] \[nvl72119-T17:1222683:0\]      ucp_device.c:415  UCX  ERROR failed to select lane for local device GPU0**<br>**\[1765457011.052846\] \[nvl72119-T17:1222683:0\]      ucp_device.c:593  UCX  ERROR failed to create handle: No such device**<br>**E1211 04:43:31.052893 1222683 ucx_backend.cpp:1665\] Failed to create device memory list for GPU transfer: Failed to create device memory list: No such device**<br>**\[1765457011.054378\] \[nvl72119-T17:1222681:0\]      ucp_device.c:415  UCX  ERROR failed to select lane for local device GPU0**<br>**\[1765457011.054394\] \[nvl72119-T17:1222681:0\]      ucp_device.c:593  UCX  ERROR failed to create handle: No such device**<br>**\[1765457011.054399\] \[nvl72119-T17:1222682:0\]      ucp_device.c:415  UCX  ERROR failed to select lane for local device GPU0**<br>**\[1765457011.054413\] \[nvl72119-T17:1222682:0\]      ucp_device.c:593  UCX  ERROR failed to create handle: No such device**<br>**E1211 04:43:31.054431 1222681 ucx_backend.cpp:1665\] Failed to create device memory list for GPU transfer: Failed to create device memory list: No such device**<br>**E1211 04:43:31.054454 1222682 ucx_backend.cpp:1665\] Failed to create device memory list for GPU transfer: Failed to create device memory list: No such device**<br>**\[1765457011.056767\] \[nvl72119-T17:1222680:0\]      ucp_device.c:415  UCX  ERROR failed to select lane for local device GPU0**<br>**\[1765457011.056782\] \[nvl72119-T17:1222680:0\]      ucp_device.c:593  UCX  ERROR failed to create handle: No such device**<br>**E1211 04:43:31.056817 1222680 ucx_backend.cpp:1665\] Failed to create device memory list for GPU transfer: Failed to create device memory list: No such device*

## 评论 (2)

### linear[bot] · 2025-12-12

from mikhailb:
> can it be due to missing  nv_peermem module?

### dfarge · 2025-12-14

To my understanding, nv_peermem is deprecated on GB200
