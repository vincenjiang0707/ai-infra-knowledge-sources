source: https://github.com/vllm-project/guidellm/issues/548

In vLLM 0.14.0+, there is now first-class support for a gRPC set of endpoints. It would be great to have the ability to have guidellm optionally use this interface instead of HTTP/S for traffic, I would expect this to be a mutually exclusive mode.

Link to proto: [https://github.com/vllm-project/vllm/blob/69d09fdd6cb66fdfc92f2f2388c4899dfd93d0ad/vllm/grpc/vllm_engine.proto#L2](https://github.com/vllm-project/vllm/blob/69d09fdd6cb66fdfc92f2f2388c4899dfd93d0ad/vllm/grpc/vllm_engine.proto#L2)

In vLLM 0.14.0+, there is now first-class support for a gRPC set of endpoints. It would be great to have the ability to have guidellm optionally use this interface instead of HTTP/S for traffic, I would expect this to be a mutually exclusive mode.

Link to proto: https://github.com/vllm-project/vllm/blob/69d09fdd6cb66fdfc92f2f2388c4899dfd93d0ad/vllm/grpc/vllm_engine.proto#L2