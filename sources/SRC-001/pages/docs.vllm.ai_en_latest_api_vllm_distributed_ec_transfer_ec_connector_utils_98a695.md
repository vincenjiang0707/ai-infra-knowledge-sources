source: https://docs.vllm.ai/en/latest/api/vllm/distributed/ec_transfer/ec_connector/utils/
lastmod: 2026-09-24

#

`vllm.distributed.ec_transfer.ec_connector.utils`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.utils)

EC connector helper utilities.

Classes:

-
–[ECOutputAggregator](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.utils.ECOutputAggregator)Merge every worker's EC connector output onto the single

-
–[PlaceholderMetadataResolver](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.utils.PlaceholderMetadataResolver)Resolves which processed keys a model needs published per modality.


Functions:

-
–[collect_ec_item_metadata](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.utils.collect_ec_item_metadata)Build one

`ec_transfer_params`

entry per feature for`request_finished()`

.

##

`ECOutputAggregator`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.utils.ECOutputAggregator)

Merge every worker's EC connector output onto the single ModelRunnerOutput that reaches the scheduler.

Mirrors KVOutputAggregator: only `output_rank`

's output is returned to the scheduler, but the EC connector may have run on any rank.

## Source code in `vllm/distributed/ec_transfer/ec_connector/utils.py`


##

`PlaceholderMetadataResolver`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.utils.PlaceholderMetadataResolver)

Resolves which processed keys a model needs published per modality.

Reads `MultiModalDataParser.embedding_fields`

, the same declaration the consumer's parser requires, so the two cannot drift. An empty set means the modality cannot be delivered out of band, and the consumer will process the media itself.

## Source code in `vllm/distributed/ec_transfer/ec_connector/utils.py`


##

`collect_ec_item_metadata(mm_features, resolver)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.utils.collect_ec_item_metadata)

Build one `ec_transfer_params`

entry per feature for `request_finished()`

.

Keyed by mm_hash, each entry carries a `metadata`

dict with whatever placeholder fields `resolver`

says this model needs published for its modality, so a consumer can skip media preprocessing. `item_indices`

identifies every occurrence in `mm_features`

, including repeated hashes. Audio token counts come from the placeholder; other metadata requires `data`

and falls back to raw media when it is unavailable on cache hits. A connector that also has transfer coordinates to report (e.g. NIXL peer_host/peer_port/size_bytes) merges those in alongside `metadata`

, not into it.