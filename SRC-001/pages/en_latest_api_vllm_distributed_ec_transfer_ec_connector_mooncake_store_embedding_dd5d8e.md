source: https://docs.vllm.ai/en/latest/api/vllm/distributed/ec_transfer/ec_connector/mooncake_store_embedding/
lastmod: 2026-09-23

#

`vllm.distributed.ec_transfer.ec_connector.mooncake_store_embedding`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.mooncake_store_embedding)

Mooncake Store support for cross-Encoder output reuse.

Modules:

-
–[backend](https://docs.vllm.ai/backend/#vllm.distributed.ec_transfer.ec_connector.mooncake_store_embedding.backend)Encoder-side Mooncake Store resolver and publisher.

-
–[data](https://docs.vllm.ai/data/#vllm.distributed.ec_transfer.ec_connector.mooncake_store_embedding.data)Content identities and output contracts for the shared Encoder Store.

-
–[store_client](https://docs.vllm.ai/store_client/#vllm.distributed.ec_transfer.ec_connector.mooncake_store_embedding.store_client)Thin Mooncake Store client for embedding objects.