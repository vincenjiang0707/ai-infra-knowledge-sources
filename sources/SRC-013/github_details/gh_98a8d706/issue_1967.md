# [Issue #1967] [sglang]: Tiered prefix cache support for lustre

source: https://github.com/llm-d/llm-d/issues/1967
state: closed | updated: 2026-09-16T21:42:50Z
labels: 

## 正文

This issue tracks the documentation, deployment configuration, and performance benchmarking for enabling Tiered Prefix Caching (TPC) backed by a Lustre high-performance parallel file system (e.g.,      
Google Cloud Parallelstore / Lustre CSI) for SGLang model servers managed by llm-d.                                                                                                                       
                                                                                                                                                                                                        
By leveraging Lustre as an L3 distributed filesystem tier alongside GPU memory (L1) and host DRAM (L2), llm-d clusters can maintain high prefix cache affinity across multi-node GPU pools, significantly 
reducing Time to First Token (TTFT) and increasing overall cache hit rates for heavy shared-prefix workloads.                                                                                             
──────                                                                                                                                                                                                    
## 🎯 Objectives & Tasks                                                                                                                                                                                  
                                                                                                                                                                                                        
### 1. 📖 Guide & Deployment Documentation                                                                                                                                                                
                                                                                                                                                                                                        
• Tiered Prefix Cache Configuration Guide:                                                                                                                                                                
• Update the llm-d documentation with step-by-step instructions on setting up Lustre-backed L3 prefix caching with SGLang deployments.                                                                
• Document required Kubernetes storage manifests (PersistentVolumeClaim, StorageClass, and CSI driver configurations for Lustre / Parallelstore).                                                     
• Detail SGLang server launch parameters and environment variables required for hierarchical/filesystem KV cache offloading.                                                                          
• Document interaction with the Endpoint Picker Proxy (EPP) for prefix-affinity routing across model pods.                                                                                            
                                                                                                                                                                                                        
                                                                                                                                                                                                        
### 2. 📊 Benchmarking & Performance Validation                                                                                                                                                           
                                                                                                                                                                                                        
• Run benchmark workloads using llm-d-benchmark / inference-perf under shared-prefix workloads (e.g., long system prompts, multi-turn chat, or multimodal contexts).                                      
• Publish comprehensive performance comparison metrics covering:                                                                                                                                          
• Cache Hit Rate (%)
• Time to First Token (TTFT)
• Time Per Output Token (TPOT)
• Request Throughput (req/s) & Token Throughput (tok/s)
• E2E Latency comparison (Direct-to-Pod vs. EPP + Lustre Tiered Cache)
• Include hardware details (GPU instance types, Lustre read/write throughput specs).
                                                                                          
──────                                                                                                                                                                                                    
## ✅ Acceptance Criteria                                                                                                                                                                                 
                                                                                                                                                                                                        
[ ] Tiered Prefix Cache guide published in llm-d documentation, detailing SGLang + Lustre deployment setups.                                                                                              
[ ] End-to-end benchmarking report added with metrics and latency graphs comparing baseline vs. Lustre-backed tiered caching.   

## 评论 (1)

### tyuchn · 2026-07-07

Noted that I have a [pending PR](https://github.com/sgl-project/sglang/pull/29716) to add a client-side metadata cache to reduce Lustre (L3 filesystem) lookup latency. We could wait until it is merged and released by sglang before adding it to llmd.
