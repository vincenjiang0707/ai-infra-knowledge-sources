# [Issue #212] H100 all reduce performance is poor

source: https://github.com/NVIDIA/nccl-tests/issues/212
state: open | updated: 2026-04-13T11:43:33Z
labels: 

## 正文

We test the  `all_reduce_perf` in H100, the algbw is about 250GB/S.  But NV officials claim that the bandwidth of all reduce can reach 450GB/S.
`all_reduce_perf` in H100, about 250GB/S:
![WechatIMG19](https://github.com/NVIDIA/nccl-tests/assets/30917208/2fba6906-2756-4e78-b9bd-18f50a69b2d9)

NV officials 450GB/S:
![WechatIMG16](https://github.com/NVIDIA/nccl-tests/assets/30917208/7fc61b1f-1365-4161-9af3-66b961aa9404)

Why is the measured all reduce bandwidth much smaller than the officially claimed bandwidth by NV?


## 评论 (20)

### sjeaugey · 2024-05-06

450GB/s is the line rate. With the protocol overhead (~20%) NCCL can get an effective NVLink bandwidth of 370GB/s, which you can observe as "BusBw" when running non-allreduce operations, or when running with `NCCL_ALGO=RING`.

Now allreduce uses NVLink SHARP by default, which accelerates the allreduce operation. With NVLink SHARP neither the algbw nor busbw correspond to the bandwidth on the wire though. On 8 GPUs, you should reach a peak busBw of ~480GB/s (algbw ~275GB/s). You need to run on larger sizes though; 256M is too small to reach peak bandwidth.

### liminn · 2024-05-06

@sjeaugey Thank you for your reply. I still have some questions:
(1) The "450GB/s AllReduce BW" in the figure actually means `busbw`, not `algbw`, right?
(2) NV claims that after using SHARP, the bandwidth can be doubled, but why did you say "On 8 GPUs, you should reach a peak busBW of ~480GB/s(algbw ~275GB/s)"?  I didn't see that SHARP has the effect of doubling the bandwidth.

![截屏2024-05-06 19 29 38](https://github.com/NVIDIA/nccl-tests/assets/30917208/2159c234-50d5-486b-987c-0c7be13bd834)


### sjeaugey · 2024-05-07

Thanks for pointing this to my attention. The slides seem wrong. I'll try to get them fixed.

### LearnigF · 2024-05-07

hello，About “ With the protocol overhead (~20%) NCCL can get an effective NVLink bandwidth of 370GB/s,”， What does "protocol" refer to? Is it NCCL_PROTO?

### sjeaugey · 2024-05-07

No, it's just the NVLink protocol (difference between wire speed and effective SM-level load/store speed through NVLink).

### LearnigF · 2024-05-07

so，Can I assume that these latencies are inevitable and cannot be further optimized in software?

### LearnigF · 2024-05-07

And，Can I interpret this 20% performance loss as data encoding loss in the NVLink transport layer?Looking forward to your reply.

### sjeaugey · 2024-05-07

Yes indeed.

### LearnigF · 2024-05-08

Thank you very much. Is there any official documentation describing the issue of performance loss at the transport layer? We have always believed that 450GB/s is the real single-direction bandwidth between cards

### hpettyiii · 2024-05-15

Its says 2x EFFECTIVE bandwidth.  So SHARP operations cut in half the need to send data for collective operations.  So you only need to send half as much data or your bandwidth has EFFECTIVELY doubled.

### QiuBiuBiu · 2024-05-29

> We test the `all_reduce_perf` in H100, the algbw is about 250GB/S. But NV officials claim that the bandwidth of all reduce can reach 450GB/S. `all_reduce_perf` in H100, about 250GB/S: ![WechatIMG19](https://private-user-images.githubusercontent.com/30917208/328117220-2fba6906-2756-4e78-b9bd-18f50a69b2d9.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTY5NzAzNzQsIm5iZiI6MTcxNjk3MDA3NCwicGF0aCI6Ii8zMDkxNzIwOC8zMjgxMTcyMjAtMmZiYTY5MDYtMjc1Ni00ZTc4LWI5YmQtMThmNTBhNjliMmQ5LmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA1MjklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNTI5VDA4MDc1NFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWJhMDE4ZDQ1MTExMzc2NjVlNzNmNTYxMzEwMDFkYmEyMDRkM2U3N2RlNzhlZDYyMjA1MDEzODQ3ZmQzYWMwYmMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.E0S6CLU-nKQpBCerMpB1z67FpQ3UYD5PVh0TiXmpUuI)
> 
> NV officials 450GB/S: ![WechatIMG16](https://private-user-images.githubusercontent.com/30917208/328117324-7fc61b1f-1365-4161-9af3-66b961aa9404.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTY5NzAzNzQsIm5iZiI6MTcxNjk3MDA3NCwicGF0aCI6Ii8zMDkxNzIwOC8zMjgxMTczMjQtN2ZjNjFiMWYtMTM2NS00MTYxLTlhZjMtNjZiOTYxYWE5NDA0LmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA1MjklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNTI5VDA4MDc1NFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTViMmFlYWUwYTJkM2RhNWRjZWI4OWU3MjRmMzBlMDY2MmY0OWUyNTMxOTVlMjFkMjY2YjI0NWFmYWUyNGVmMDImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.iG04qutlEfSN0cSh7dPvy8Fhf4uNOBim1o1rQjMDmKA)
> 
> Why is the measured all reduce bandwidth much smaller than the officially claimed bandwidth by NV?

@liminn Curious if this performance data is a result of the RING or NVLS algorithm on H100? What can be the peak bandwidth (algo & bus) when the data size becomes 1g or larger.

### dearsxx0918 · 2024-07-05

Hi sjeaugey,
        I think nccl-tests bus bandwidth is not correct for NVLS. The relationship between algbw and busbw for ring is algbw = busbw * n / (2 * (n - 1)), for NVLS is algbw = busbw * n / ( n -1).
        Users are more care about algbw improvement since this will affect their E2E performance. Busbw only reflect the hardware link effective bandwidth.
        So NV should clarify this since caused much misunderstanding on E2E performance.
Best regards,
-Edda



### sjeaugey · 2024-07-05

The NVLS formula would actually be algbw = busbw * n / (n+1). [Edited, sorry previous formula busbw * (n+1)/(n-1) was a mistake]

But the NCCL perf tests do not look inside NCCL. They're sitting on top of NCCL, and as such they can't know what the topology is, nor which algorithm/mechanism NCCL is using.

The BusBw was added as a theoretical correction factor over the algorithm bandwidth, to account for the fact that some operations need to exchange more than the size when based on point-to-point exchanges. It also allowed to have a bandwidth that would not change as we scale, and which we could compare to HW values.

But with hierarchical algorithms or hardware-accelerated algorithms, it becomes less and less of a "Bus" bandwidth more like a "Corrected algorithm bandwidth" and became harder to interpret. For hardware-accelerated algorithms, the algorithm bandwidth is the actual bus bandwidth, and the "BusBW" is no longer reflecting any real bandwidth on the system.

It is still a value to compare against algorithms though. Basically, when running with NVLS and getting 480GB/s, the BusBW tells you what NVLink bandwidth you would need to get the same performance if you didn't have NVLS. So you can see that number as the "Bus bandwidth you would need if you connected all GPUs through a flat network and they could only communicate through Send/Recv operations".



### Alice1069 · 2025-05-23

could you elaborate why NVLS formula is like this algbw = busbw * n / (n+1) ? 
I think, it's equal, formula should be algbw=busbw, every gpu just sends all data out to switch and get back the same size of all_reduced data back. 


### qq2046 · 2026-04-13

> The NVLS formula would actually be algbw = busbw * n / (n+1). [Edited, sorry previous formula busbw * (n+1)/(n-1) was a mistake]
> 
> But the NCCL perf tests do not look inside NCCL. They're sitting on top of NCCL, and as such they can't know what the topology is, nor which algorithm/mechanism NCCL is using.
> 
> The BusBw was added as a theoretical correction factor over the algorithm bandwidth, to account for the fact that some operations need to exchange more than the size when based on point-to-point exchanges. It also allowed to have a bandwidth that would not change as we scale, and which we could compare to HW values.
> 
> But with hierarchical algorithms or hardware-accelerated algorithms, it becomes less and less of a "Bus" bandwidth more like a "Corrected algorithm bandwidth" and became harder to interpret. For hardware-accelerated algorithms, the algorithm bandwidth is the actual bus bandwidth, and the "BusBW" is no longer reflecting any real bandwidth on the system.
> 
> It is still a value to compare against algorithms though. Basically, when running with NVLS and getting 480GB/s, the BusBW tells you what NVLink bandwidth you would need to get the same performance if you didn't have NVLS. So you can see that number as the "Bus bandwidth you would need if you connected all GPUs through a flat network and they could only communicate through Send/Recv operations".

@sjeaugey hello, may I ask why "In-Switch Sum" and "In-Switch Multicast" are split into two parts? This result in n+1 Send, if they were combined into one part, wouldn't there only be n Send?

### sjeaugey · 2026-04-13

Having it split allows to insert a network allreduce and cover all cases. But you're right, if we had a fused operation we could win a bit in terms of performance.

### qq2046 · 2026-04-13

> Having it split allows to insert a network allreduce and cover all cases. But you're right, if we had a fused operation we could win a bit in terms of performance.

Thansks for your reply. What's that mean '**to insert a network allreduce**', to insert the next **allreduce** operation?

### sjeaugey · 2026-04-13

Sorry, I meant that having a fused operation would be beneficial for operations on a single NVLink domain, but when you need to do an NVLink + Network allreduce, you need to pipeline 3 operations: the NVLS reduce scatter, the network allreduce and the NVLS allgather. Together those 3 operations form a NVLS+Network allreduce (e.g. NVLSTree).

On a single NVL domain, you remove the network step, and just perform the NVLS Reduce scatter and NVLS Allgather, fused as a single operation.

### qq2046 · 2026-04-13

> Sorry, I meant that having a fused operation would be beneficial for operations on a single NVLink domain, but when you need to do an NVLink + Network allreduce, you need to pipeline 3 operations: the NVLS reduce scatter, the network allreduce and the NVLS allgather. Together those 3 operations form a NVLS+Network allreduce (e.g. NVLSTree).
> 
> On a single NVL domain, you remove the network step, and just perform the NVLS Reduce scatter and NVLS Allgather, fused as a single operation.

So if I'm testing on a single NVL domain, it is still split into two parts, and the algbw = busbw * n / (n+1) is still the same? But it's an  optimization direction to fuse 2 operations, is my understanding correct?

### sjeaugey · 2026-04-13

I haven't given it a lot of thoughts, but I believe you are indeed correct.
