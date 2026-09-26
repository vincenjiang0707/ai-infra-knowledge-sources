# [Issue #447] gRPC triton/tfserve cannot handle SSL certificate with another CN

source: https://github.com/triton-inference-server/perf_analyzer/issues/447
state: open | updated: 2025-10-29T04:22:10Z
labels: 

## 正文

I believe that `--ssl-https-verify-peer` and `--ssl-https-verify-host` flags are only applied to HTTP protocol, for gRPC in c++, there is no flag to ignore if SSL cert doesn't match with hosts, which will throw `Peer name XXX is not in peer certificate`

The only way I found is using [SetSslTargetNameOverride](https://github.com/grpc/grpc/blob/master/include/grpcpp/support/channel_arguments.h#L62), and pass that from https://github.com/triton-inference-server/perf_analyzer/blob/3c0bc9efa1844a82dfcc911f094f5026e6dd9214/src/client_backend/triton/triton_client_backend.cc#L74, all the way to here: https://github.com/triton-inference-server/client/blob/fdfa5cd8d893bbbb99b926612dd459b8005518f1/src/c%2B%2B/library/grpc_client.cc#L454-L475



## 评论 (1)

### ksmaze · 2025-10-29

Also create a PR to contribute
