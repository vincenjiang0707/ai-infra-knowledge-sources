# [Issue #133] torch_npu profiler 输出的 trace JSON 与 Perfetto 不兼容：ts 为字符串类型 + 绝对时间戳导致精度丢失

source: https://github.com/Ascend/pytorch/issues/133
state: open | updated: 2026-08-07T07:04:07Z
labels: 

## 正文

* 严格来说这个不算是bug,只是把我发现的问题+分析结论+解决方案贴在这里,供遇到类似问题的同学/AI索引解决类似的问题 *  

问题描述                                                                                                                                                                                    
                                                                                                                                                                                              
  torch_npu profiler 导出的 trace_view.json 在 Perfetto (ui.perfetto.dev) 中打开时显示异常：                                                                                                  
  1. GPU 算子缺失（约 20% 的 NPU kernel 被错误嵌套为其他算子的子事件）                                                                                                                        
  2. Flow 箭头连接错误（一个 CPU 算子连接到多个不相关的 GPU 算子）                                                                                                                            
                                                                                                                                                                                              
  同一文件在 MindStudio Insight 中显示正常。                                                                                                                                                  
                                                                                                                                                                                              
  根因分析                                                                                                                                                                                    
                                                                                                                                                                                              
  trace_view.json 的格式与 https://docs.google.com/document/d/1CvAClvFfyA5R-PhYUmn5OOQtYMH4h6I0nSsKchNAySU 存在三处不兼容：                                                                   
                                                                                                                                                                                              
  1. ts 字段是字符串类型（应为数字）                                                                                                                                                          
                                                                                                                                                                                              
  // 当前输出                                                                                                                                                                                 
  "ts": "1778655624745710.730"                                                                                                                                                                
                                                                                                                                                                                              
  // Chrome Trace Format 规范                                                                                                                                                                 
  "ts": 1778655624745710.730                                                                                                                                                                  
                                                                                                                                                                                              
  2. ts 使用绝对时间戳（epoch 微秒），数值在 10^15 量级                                                                                                                                       
                                                                                                                                                                                              
  在此量级下 float64 的精度步长为 0.5 微秒。Perfetto 的 JSON parser 将字符串 ts 解析为 double 后，亚微秒精度丢失，导致相邻算子的时间区间产生虚假重叠。          
    
<img width="935" height="331" alt="Image" src="https://github.com/user-attachments/assets/99129022-3b5e-4540-b42b-ab708a3c2118" />

<img width="1400" height="868" alt="Image" src="https://github.com/user-attachments/assets/7e06d732-8935-4279-b0dd-e52efaf52a02" />

<img width="1288" height="926" alt="Image" src="https://github.com/user-attachments/assets/c518a4cc-d60b-43b4-8c8d-e05fd4c36bb9" />

<img width="1568" height="732" alt="Image" src="https://github.com/user-attachments/assets/611ad11c-1466-4359-89a1-afa4a9bbc5ce" />
                          
                                                                                                                                                                                                                                                                                                                                                                            
  原始数据：                                                                                                                                                                          
    RmsNorm:  ts=1778655624745710.730, dur=5.16  → end=1778655624745715.890                                                                                                                   
    MatMul:   ts=1778655624745715.910            → gap=0.020µs（无重叠）                                                                                                                      
                                                                                                                                                                                              
  经 float64 解析后（Perfetto 实际行为）：                                                                                                                                                    
    RmsNorm:  ts=1778655624745710848ns, dur=5160ns → end=1778655624745716008ns                                                                                                                
    MatMul:   ts=1778655624745715968ns             → overlap=40ns（虚假重叠！）                                                                                                               
                                                            
  Perfetto 将重叠的 slice 视为父子关系（nested），导致后面的算子"消失"在前面算子的折叠层中。                                                                                                  
  
  实测：修复前 GPU track 有 22,085 个 slice 被错误嵌套（depth>0），修复后全部 133,652 个 slice 正确平铺在 depth=0。                                                                           
                                                            
  3. Flow event 的 id 超过 2^53                                                                                                                                                               
                                                            
  "id": 1778655624745710730   // > 9007199254740992 (2^53)                                                                                                                                    
                                                                                                                                                                                              
  超过 JavaScript Number 安全整数范围，在 Perfetto UI（TypeScript）中可能产生精度丢失。                                                                                                       
                                                                                                                                                                                              
  可以执行的修复方案                                                                                                                                                                                
                                                            
  1. ts 使用数字类型，不要加引号                                                                                                                                                              
  2. 使用相对时间戳（减去 profiling 起始时间），使数值降到 10^6~10^9 量级，彻底避免 float64 精度问题
  3. Flow id 控制在 2^53 以内，或使用字符串类型 id（Perfetto 支持 "id": "string_id"）                                                                                                         
                                                                                                                                                                                              
  环境信息                                                                                                                                                                                    
                                                                                                                                                                                              
  - 硬件：Ascend 910C                                                                                                                                                                         
  - torch_npu 版本：（填写你的版本）                        
  - CANN 版本：（填写你的版本）                                                                                                                                                               
  - 复现方式：使用 torch.profiler 导出 trace，用 Perfetto 打开                                                                                                                                
                                                                                                                                                                                              
  Workaround                                                                                                                                                                                  
                                                                                                                                                                                              
  在打开 Perfetto 之前，对 JSON 做预处理：将 ts 字符串转为数字并减去基准时间戳，将超大 flow id 重映射为小整数。  
附:json fix code:https://github.com/JiaryCoder/Ascend-Profile/blob/main/fix_ascend_trace.py

## 评论 (2)

### JiaryCoder · 2026-05-14

不过,还是希望能兼容,作为 PyTorch的后端扩展，用户会期待输出与上游一致.

### JiaryCoder · 2026-05-14

另外还发现有时钟漂移的问题,导致CPU launch晚于GPU kernel

<img width="417" height="354" alt="Image" src="https://github.com/user-attachments/assets/83e117f4-3daf-410e-9b95-8f3c0987a3df" />
