# [Issue #346] SSL options not passed for OpenAI backend

source: https://github.com/triton-inference-server/perf_analyzer/issues/346
state: open | updated: 2025-10-29T04:19:45Z
labels: 

## 正文

SSL parameters are not passed to the OpenAI backend for perf_analyzer and it looks like those are used only by GRPC. The docs make it look like it's a global flag and used by all backends

## 评论 (9)

### the-david-oy · 2025-03-26

Thanks for sharing this, Niraj. We'll look into the best path forward for this.

### the-david-oy · 2025-03-26

Can you provide more details about what you're referring to? The [GitHub docs](https://github.com/triton-inference-server/perf_analyzer/blob/main/docs/cli.md#--ssl-grpc-use-ssl) include all of the flags, and the naming themselves include GRPC and HTTP. If it does not already, I suppose PA could add more error checking if using `ssl-grpc-*` flags when not using GRPC or `ssl-http-*` flags when not using HTTP.

CC: @matthewkotila 

### Nirajn2311 · 2025-04-04

We were running PA with `--ssl-https-verify-peer` and `--ssl-https-verify-host` flags with both value as 0 as the endpoint for analyzing was using a self signed certificate but the command would fail due to SSL error which should not be the case as we're telling it to skip the ssl verification. Only after I hardcoded the values for the above two curl options in the code directly and rebuilt the binary then only it ran successfully. This is in the OpenAI backend.

### the-david-oy · 2025-04-04

Thanks for explaining. It sounds like the zero values aren't being parsed properly for some reason. I created a ticket for us to investigate.

Ref: TPA-1059

### ksmaze · 2025-10-28

I believe that `--ssl-https-verify-peer` and `--ssl-https-verify-host` flags are only applied to HTTP protocol, for gRPC in c++, there is no flag to ignore. 

The only way I found is using [SetSslTargetNameOverride](https://github.com/grpc/grpc/blob/master/include/grpcpp/support/channel_arguments.h#L62), and pass that from https://github.com/triton-inference-server/perf_analyzer/blob/3c0bc9efa1844a82dfcc911f094f5026e6dd9214/src/client_backend/triton/triton_client_backend.cc#L74, all the way to here: https://github.com/triton-inference-server/client/blob/fdfa5cd8d893bbbb99b926612dd459b8005518f1/src/c%2B%2B/library/grpc_client.cc#L454-L475

will be great if the team can help add this option, thank you!

### the-david-oy · 2025-10-28

Thanks for identifying the root cause and updating this thread. This benchmarking is now moved to AIPerf, with GenAI-Perf being deprecated. Can you please make this request there? https://github.com/ai-dynamo/aiperf

CC: @ajcasagrande @debermudez 

### ksmaze · 2025-10-28

Thanks for the response! unfortunately my case is only focusing on triton grpc instead llm for general model serving, so don't have enough knowledge of the newer project's information.

### the-david-oy · 2025-10-28

Thanks for letting us know!

@ganeshku1 There is a request for SSL gRPC option support in Perf Analyzer to match the SSL HTTP options.

### ksmaze · 2025-10-29

Actually I realized my reported issue is different from this one, filed https://github.com/triton-inference-server/perf_analyzer/issues/447 instead

If this one is for OpenAI backend, I think it makes sense to go to the new project.
