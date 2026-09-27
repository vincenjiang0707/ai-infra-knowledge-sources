# CUDA-Device-Max-Connections

source: https://leimao.github.io/blog/CUDA-Device-Max-Connections/#more

To maximize GPU utilization, it is common to have multiple workers processing tasks concurrently on GPU. However, by default, the GPU hardware concurrency is limited, no matter how much software concurrency is implemented. As a consequence, GPU might still be under utilized, even if at the software level the concurrency appears high in the implementation. CUDA_DEVICE_MAX_CONNECTIONS is an environment variable that can be set to control the number of hardware concurrency on GPU.

In this blog post, I would like to quickly discuss the importance of setting CUDA_DEVICE_MAX_CONNECTIONS for maximizing GPU concurrency and overall utilization.

CUDA Device Max Connections

In CUDA programming, a CUDA stream is an abstraction which allows the programmer to express a sequence of operations. The developer could create multiple streams to enable concurrent execution of different tasks on the GPU, thereby improving overall utilization and performance. CUDA kernels launched in different streams can run concurrently, subject to hardware limitations and resource availability, such as the number of available Streaming Multiprocessors. There is one key factor that the developer might overlook, which is the CUDA_DEVICE_MAX_CONNECTIONS environment variable that controls the maximum number of concurrent connections to the GPU. If this variable is not set appropriately, no matter how many CUDA streams are created, how lightweight the kernels are on each stream, the GPU concurrency will still be limited.

In the following example, we created 32 CUDA streams to run concurrent tasks on GPU. The inference performances are benchmarked and profiling traces are collected.

for (auto& worker : profile_workers) { worker.join(); }

std::this_thread::sleep_for(std::chrono::milliseconds(500)); auto profiler_result = torch::autograd::profiler::disableProfiler();

for (cudaStream_t stream : streams) { CHECK_CUDA_ERROR(cudaStreamSynchronize(stream)); }

if (profiler_result) { profiler_result->save(trace_filename); std::cout << "Saved PyTorch Profiler trace to: " << trace_filename << std::endl; }

for (cudaStream_t stream : streams) { CHECK_CUDA_ERROR(cudaStreamDestroy(stream)); }

return0; }

By varying CUDA_DEVICE_MAX_CONNECTIONS, we can control the maximum number of concurrent connections to the GPU device, which affects the performance of multi-stream workloads.

$ for connections in 1 2 4 8 16 32; do CUDA_DEVICE_MAX_CONNECTIONS="$connections" ./build/multi_stream \ --trace-file "build/max_conn_${connections}.json" done CUDA_DEVICE_MAX_CONNECTIONS = 1

--- Phase 1: Measuring Pure System Throughput (QPS) --- Total Queries Processed : 6400 Elapsed Time : 1.66418 seconds Pure System Throughput : 3845.73 queries/second

--- Phase 1: Measuring Pure System Throughput (QPS) --- Total Queries Processed : 6400 Elapsed Time : 1.13147 seconds Pure System Throughput : 5656.38 queries/second

--- Phase 1: Measuring Pure System Throughput (QPS) --- Total Queries Processed : 6400 Elapsed Time : 0.438797 seconds Pure System Throughput : 14585.3 queries/second

--- Phase 1: Measuring Pure System Throughput (QPS) --- Total Queries Processed : 6400 Elapsed Time : 0.35048 seconds Pure System Throughput : 18260.7 queries/second

--- Phase 1: Measuring Pure System Throughput (QPS) --- Total Queries Processed : 6400 Elapsed Time : 0.142692 seconds Pure System Throughput : 44851.8 queries/second

--- Phase 1: Measuring Pure System Throughput (QPS) --- Total Queries Processed : 6400 Elapsed Time : 0.0756491 seconds Pure System Throughput : 84601.2 queries/second

The system throughputs benchmarked and the profiling traces collected for different values of CUDA_DEVICE_MAX_CONNECTIONS are summarized in the table below.

We could see that the system throughput nearly doubles as CUDA_DEVICE_MAX_CONNECTIONS is doubled, indicating a strong correlation between the number of allowed CUDA connections and the overall system performance. By examining the Perfetto traces, we could see that despite the very lightweight kernel, there are lots of bubbles in CUDA stream which are not caused by CPU launch overhead, if CUDA_DEVICE_MAX_CONNECTIONS is not the same as the number of CUDA streams.

Technically, each CUDA stream is associated with a hardware queue on GPU, and the number of hardware queues is configured by the CUDA_DEVICE_MAX_CONNECTIONS environment variable. By default, CUDA_DEVICE_MAX_CONNECTIONS is set to 8. Therefore, in our application, if CUDA_DEVICE_MAX_CONNECTIONS is not set, the system will be significantly underutilized.

We could check what hardware queue each CUDA stream is mapped to by examining the stream and the channel attributes of CUDA kernels. For example, in the Perfetto trace of CUDA_DEVICE_MAX_CONNECTIONS=1, all CUDA streams are mapped to the same hardware queue 0.

Miscellaneous

AMD GPUs have similar concepts of hardware queues and stream-to-queue mapping, which can be controlled through environment variables specific to the ROCm platform. In the case of AMD GPUs, GPU_MAX_HW_QUEUES specifies the maximum number of hardware queues available for mapping streams and hsa_queue is the hardware queue associated with a particular stream that can be checked from the Perfetto trace attributes. Note that the default value of GPU_MAX_HW_QUEUES is 4, which means the maximum GPU concurrency is very limited unless this environment variable is increased.
