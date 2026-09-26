# [Issue #1707] Query: Target seq type VRAM or DRAM What does it means in GDS

source: https://github.com/ai-dynamo/nixl/issues/1707
state: open | updated: 2026-06-08T15:08:59Z
labels: 

## 正文

What should be Target Seq type while running GDS Backedn , it should be VRAM or DRAM?
what does it means actually in gds backend.?

## 评论 (4)

### linear-code[bot] · 2026-06-01

from mikhailb:
> The NIXL GDS backend supports **both VRAM and DRAM** as target seq types.
> 
> **What FILE, VRAM, DRAM mean in GDS context:**
> 
> * `FILE_SEG` = storage (file on NVMe/disk, identified by a file descriptor)
> * `VRAM_SEG` = GPU memory
> * `DRAM_SEG` = host/CPU memory
> 
> A GDS transfer always goes between a file and a memory buffer:
> 
> * `FILE_SEG ↔ VRAM_SEG` — direct storage↔GPU path (classic GPUDirect, best performance, bypasses CPU entirely)
> * `FILE_SEG ↔ DRAM_SEG` — storage↔host memory via cuFile (no GPU direct path)
> 
> **Both READ and WRITE are supported:**
> 
> * READ: load from storage → GPU/CPU memory
> * WRITE: save GPU/CPU memory → storage
> 
> **Which should you use?** If your data is consumed by the GPU, use **VRAM** — that's where GDS delivers its performance benefit (no CPU bounce buffer). Use **DRAM** only if your target buffer is on the host side.

### alokprasad · 2026-06-02

I had used some old nixlbench it seems it had only VRAM_SEG and DRAM_SEG and below are the results with NVME PCIE G5 x4 ssd
i was expecting if VRAM is target and intiator performace would be best but i dont see that any reason ?

<img width="620" height="378" alt="Image" src="https://github.com/user-attachments/assets/175ac89d-2826-47cb-a286-9f48147979fb" />

### linear-code[bot] · 2026-06-08

from mikhailb:
> **VRAM initiator path:** Data goes VRAM ↔ PCIe ↔ NVMe (the GDS path). Bottlenecked by your PCIe Gen 5 x4 NVMe interface (\~15.75 GB/s theoretical). You're seeing \~11 GB/s — that's the GDS overhead eating \~30% of the interface ceiling. This is expected.
> 
> **DRAM initiator path:** Goes through system memory DMA engines, which can use the full PCIe x16 GPU slot bandwidth (\~63 GB/s Gen 5 x16) or direct DRAM memcpy — bypassing the x4 NVMe bottleneck entirely for some operations.
> 
> #### Why DRAM numbers exceed PCIe Gen 5 x4 limit
> 
> <!-- linear:table-colwidths:200,200,200 -->
> | Path | Peak BW | Explanation |
> | -- | -- | -- |
> | VRAM→VRAM READ | 11.09 GB/s | NVMe PCIe x4 bottleneck + GDS overhead |
> | DRAM→VRAM READ | 17.64 GB/s | PCIe x16 H2D path, **not NVMe** |
> | DRAM→DRAM WRITE | 22.33 GB/s | System DRAM memcpy, no NVMe involved |
> 
> The DRAM results **exceeding 15.75 GB/s** confirm they're not routing through your NVMe at all — they're pure memory copy paths.
> 
> #### Specific Issues with VRAM GDS Path
> 
> 1. **cuFile overhead** — GPU memory registration, pinning, and descriptor management add latency the DRAM path avoids
> 2. **PCIe contention** — VRAM↔NVMe traffic competes for PCIe bandwidth on the same fabric
> 3. **WRITE at 32MB peak vs READ at 64MB** — your NVMe write path saturates at smaller block sizes, possibly SLC cache behavior
> 
> #### What to Check
> 
> * Are you running with `nvidia-smi` confirming GDS is actually active for VRAM transfers?
> * What's the PCIe topology? (`nvidia-smi topo -m`) — if GPU and NVMe are on different PCIe switches, you have extra hop latency
> * The newer nixlbench with `FILE_SEG` would give you cleaner isolation of the actual NVMe↔VRAM GDS path vs memory-to-memory
> 
> The 11 GB/s VRAM result is actually reasonable for a single Gen 5 x4 NVMe with GDS — you'd need multiple NVMe drives in parallel to saturate GPU PCIe bandwidth.

### alokprasad · 2026-06-08

@brminich  i don't see FILE_SEG even in newest nixlbench , is there separate branch ?
