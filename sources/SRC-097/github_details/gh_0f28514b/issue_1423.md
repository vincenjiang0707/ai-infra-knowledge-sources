# [Issue #1423] Error in doca_apsh_modules_get sample

source: https://github.com/ai-dynamo/nixl/issues/1423
state: closed | updated: 2026-07-10T14:19:00Z
labels: 

## 正文

[20:26:20:242626][26422][DOCA][ERR][doca_apsh.c:536][doca_apsh_modules_get] can't get modules list
[20:26:20:242651][26422][DOCA][ERR][apsh_modules_get_sample.c:70][modules_get] Failed to get modules of system
[20:26:20:242681][26422][DOCA][INF][doca_buf_inventory.cpp:426][stop] Buf inventory 0xaaaafdaf5940: was stopped
[20:26:20:243286][26422][DOCA][INF][doca_mmap.cpp:838][doca_mmap_stop] Mmap 0xaaaafdaf57c0: mmap was stopped
[20:26:20:243303][26422][DOCA][DBG][doca_mmap.cpp:986][doca_mmap_rm_dev] Mmap 0xaaaafdaf57c0: Removed device=0xaaaafdae7a20 from mmap. curr_device_num=0
[20:26:20:243313][26422][DOCA][INF][doca_dma.cpp:1017][dma_ctx_request_stop] DMA 0xaaaafdaf5380: DMA was requested to stop
[20:26:20:244171][26422][DOCA][INF][doca_pe.cpp:847][priv_doca_pe_unregister_qp_bulk] Progress engine 0xaaaafdaf5740: qp bulk with start index=1 was unregistered from pe
[20:26:20:254905][26422][DOCA][INF][doca_pe.cpp:681][priv_doca_pe_cq_unregister] Progress engine 0xaaaafdaf5740: cq=0xaaaafdae4fc8 was unregistered from pe
[20:26:20:254922][26422][DOCA][INF][doca_ctx.cpp:656][priv_doca_ctx_set_state_to_idle] CTX 0xaaaafdae4f80 has successfully stopped
[20:26:20:254928][26422][DOCA][INF][doca_pe.cpp:115][priv_doca_pe_ctx_destroy] Destroying progress engine ctx=0xaaaafdae4f80
[20:26:20:254934][26422][DOCA][INF][shared_cq_pe_ctx.cpp:89][~shared_cq_wrapper_context] shared_cq_wrapper_context 0xaaaafdae4f80 was destroyed
[20:26:20:255206][26422][DOCA][INF][doca_pe.cpp:847][priv_doca_pe_unregister_qp_bulk] Progress engine 0xaaaafdaf5740: qp bulk with start index=0 was unregistered from pe
[20:26:20:255222][26422][DOCA][INF][doca_dma.cpp:1068][dma_ctx_stop] DMA 0xaaaafdaf5380: DMA was stopped
[20:26:20:255228][26422][DOCA][INF][doca_ctx.cpp:656][priv_doca_ctx_set_state_to_idle] CTX 0xaaaafdaf5380 has successfully stopped
[20:26:20:255412][26422][DOCA][INF][doca_mmap.cpp:838][doca_mmap_stop] Mmap 0xaaaafdaf6b80: mmap was stopped
[20:26:20:255421][26422][DOCA][INF][doca_mmap.cpp:651][doca_mmap_destroy] Mmap 0xaaaafdaf6b80: Destroying mmap
[20:26:20:255425][26422][DOCA][INF][doca_mmap.cpp:838][doca_mmap_stop] Mmap 0xaaaafdaf6b80: mmap was stopped
[20:26:20:255566][26422][DOCA][INF][doca_mmap.cpp:651][doca_mmap_destroy] Mmap 0xaaaafdaf57c0: Destroying mmap
[20:26:20:255577][26422][DOCA][INF][doca_mmap.cpp:838][doca_mmap_stop] Mmap 0xaaaafdaf57c0: mmap was stopped
[20:26:20:255582][26422][DOCA][INF][doca_pe.cpp:115][priv_doca_pe_ctx_destroy] Destroying progress engine ctx=0xaaaafdaf5380
[20:26:20:255587][26422][DOCA][INF][doca_dma.cpp:1275][doca_dma_destroy] DMA 0xaaaafdaf5380: DMA was destroyed
[20:26:20:255593][26422][DOCA][INF][doca_dev.cpp:2993][priv_doca_memory_region_destroy] Destroying memory_region=0xaaaafdaf9700
[20:26:20:255868][26422][DOCA][INF][doca_pe.cpp:61][doca_pe_destroy] Progress engine 0xaaaafdaf5740: Destroying progress engine
[20:26:20:255899][26422][DOCA][INF][doca_pe.cpp:1265][destroy] Progress engine 0xaaaafdaf5740 was destroyed
[20:26:20:612753][26422][DOCA][INF][doca_dev.cpp:1132][doca_dev_rep_close] Device representor 0xaaaafdae5040 was closed
[20:26:20:613331][26422][DOCA][INF][doca_dev.cpp:147][dev_put] Device 0xaaaafdae7a20 was destroyed
[20:26:20:613355][26422][DOCA][INF][doca_dev.cpp:1019][doca_dev_close] Local device 0xaaaafdae7a20 was closed
[20:26:20:613361][26422][DOCA][ERR][apsh_modules_get_main.c:105][main] modules_get() encountered an error: Resource initialization failure
[20:26:20:613370][26422][DOCA][INF][apsh_modules_get_main.c:117][main] Sample finished with errors

## 评论 (1)

### brminich · 2026-07-02

Please describe the issue and how to repro it. This log alone does not say much
