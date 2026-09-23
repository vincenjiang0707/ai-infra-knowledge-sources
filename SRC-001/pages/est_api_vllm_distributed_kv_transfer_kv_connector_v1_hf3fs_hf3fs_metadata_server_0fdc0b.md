source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server/
lastmod: 2026-09-23

#

`vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server)

HF3FS Metadata Server with key-based organization.

Classes:

-
–[GlobalMetadataState](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.GlobalMetadataState)Manages global metadata state across all ranks and keys.

-
–[Hf3fsGlobalMetadataClient](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsGlobalMetadataClient)Global HTTP metadata client for HF3FS.

-
–[Hf3fsMetadataInterface](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataInterface)Interface for HF3FS metadata operations.

-
–[Hf3fsMetadataServer](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer)HF3FS Metadata Server with improved key-based organization.

-
–[KeyMetadata](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.KeyMetadata)Manages metadata for a single key across multiple ranks.

-
–[RankFileMetadata](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.RankFileMetadata)Manages file page allocation for a single rank.


Functions:

-
–[run_metadata_server](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.run_metadata_server)Run the improved HF3FS metadata server.


##

`GlobalMetadataState`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.GlobalMetadataState)

Manages global metadata state across all ranks and keys.

Methods:

-
–[allocate_pages_for_keys](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.GlobalMetadataState.allocate_pages_for_keys)Allocate one page for each key on the specified rank.

-
–[batch_key_exists](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.GlobalMetadataState.batch_key_exists)Check if keys exist in metadata and all ranks have confirmed writes.

-
–[clear](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.GlobalMetadataState.clear)Clear all metadata state.

-
–[confirm_write_for_keys](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.GlobalMetadataState.confirm_write_for_keys)Confirm write operations for keys and update metadata.

-
–[get_key_locations](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.GlobalMetadataState.get_key_locations)Get page indices for keys on a specific rank.

-
–[initialize_rank](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.GlobalMetadataState.initialize_rank)Initialize a new rank with specified number of pages.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


|
|

###

`allocate_pages_for_keys(rank, keys)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.GlobalMetadataState.allocate_pages_for_keys)

Allocate one page for each key on the specified rank.

Parameters:

-

(`rank`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.GlobalMetadataState.allocate_pages_for_keys(rank))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Rank ID to allocate pages on

-

(`keys`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.GlobalMetadataState.allocate_pages_for_keys(keys))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[str](https://docs.python.org/3/builtins/stdtypes.html#str)]]List of keys to allocate pages for


Returns:

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


###

`batch_key_exists(keys)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.GlobalMetadataState.batch_key_exists)

Check if keys exist in metadata and all ranks have confirmed writes.

Parameters:

Returns:

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


###

`clear()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.GlobalMetadataState.clear)

Clear all metadata state.

###

`confirm_write_for_keys(rank, key_confirmations, pages_to_release=None)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.GlobalMetadataState.confirm_write_for_keys)

Confirm write operations for keys and update metadata.

Parameters:

-

(`rank`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.GlobalMetadataState.confirm_write_for_keys(rank))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Rank ID that confirmed the writes

-

(`key_confirmations`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.GlobalMetadataState.confirm_write_for_keys(key_confirmations))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[int](https://docs.python.org/3/builtins/functions.html#int)]]List of (key, page_index) tuples

-

(`pages_to_release`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.GlobalMetadataState.confirm_write_for_keys(pages_to_release))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | None`None`

) –List of page indices to release back to free pool


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


###

`get_key_locations(rank, keys)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.GlobalMetadataState.get_key_locations)

Get page indices for keys on a specific rank.

Parameters:

Returns:

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


###

`initialize_rank(rank, num_pages)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.GlobalMetadataState.initialize_rank)

Initialize a new rank with specified number of pages.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


##

`Hf3fsGlobalMetadataClient`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsGlobalMetadataClient)

Bases: [Hf3fsMetadataInterface](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataInterface)

Global HTTP metadata client for HF3FS.

Methods:

-
–[allocate_pages_for_keys](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsGlobalMetadataClient.allocate_pages_for_keys)Allocate pages for keys on the specified rank.

-
–[batch_key_exists](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsGlobalMetadataClient.batch_key_exists)Check if keys exist and are complete across all ranks.

-
–[confirm_write_for_keys](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsGlobalMetadataClient.confirm_write_for_keys)Confirm write operations for keys and optionally release pages.

-
–[get_key_locations](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsGlobalMetadataClient.get_key_locations)Get page indices for keys on a specific rank.

-
–[initialize](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsGlobalMetadataClient.initialize)Initialize a rank with specified number of pages.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


|
|

###

`_post(endpoint, json_data)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsGlobalMetadataClient._post)

Make POST request to metadata server.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


###

`allocate_pages_for_keys(rank, keys)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsGlobalMetadataClient.allocate_pages_for_keys)

Allocate pages for keys on the specified rank.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


###

`batch_key_exists(keys)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsGlobalMetadataClient.batch_key_exists)

Check if keys exist and are complete across all ranks.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


###

`confirm_write_for_keys(rank, key_confirmations, pages_to_release=None)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsGlobalMetadataClient.confirm_write_for_keys)

Confirm write operations for keys and optionally release pages.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


###

`get_key_locations(rank, keys)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsGlobalMetadataClient.get_key_locations)

Get page indices for keys on a specific rank.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


###

`initialize(rank, num_pages=0, role='worker')`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsGlobalMetadataClient.initialize)

Initialize a rank with specified number of pages.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


##

`Hf3fsMetadataInterface`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataInterface)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Interface for HF3FS metadata operations.

Methods:

-
–[allocate_pages_for_keys](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataInterface.allocate_pages_for_keys)Allocate one page for each key on the specified rank.

-
–[batch_key_exists](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataInterface.batch_key_exists)Check if keys exist and are complete across all ranks.

-
–[confirm_write_for_keys](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataInterface.confirm_write_for_keys)Confirm write operations for keys and optionally release pages.

-
–[get_key_locations](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataInterface.get_key_locations)Get page indices for keys on a specific rank.

-
–[initialize](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataInterface.initialize)Initialize the metadata service with specified number of pages.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


###

`allocate_pages_for_keys(rank, keys)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataInterface.allocate_pages_for_keys)

Allocate one page for each key on the specified rank.

###

`batch_key_exists(keys)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataInterface.batch_key_exists)

Check if keys exist and are complete across all ranks.

###

`confirm_write_for_keys(rank, key_confirmations, pages_to_release=None)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataInterface.confirm_write_for_keys)

Confirm write operations for keys and optionally release pages.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


###

`get_key_locations(rank, keys)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataInterface.get_key_locations)

###

`initialize(rank, num_pages=0, role='worker')`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataInterface.initialize)

Initialize the metadata service with specified number of pages.

##

`Hf3fsMetadataServer`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer)

HF3FS Metadata Server with improved key-based organization.

Methods:

-
–[batch_allocate_pages_for_keys](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer.batch_allocate_pages_for_keys)Allocate one page for each key on a specific rank.

-
–[batch_key_exists](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer.batch_key_exists)Check if multiple keys exist in metadata.

-
–[clear](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer.clear)Clear the metadata server.

-
–[confirm_write_for_keys](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer.confirm_write_for_keys)Confirm write operations for keys.

-
–[get_key_locations](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer.get_key_locations)Get page indices for keys on a specific rank.

-
–[initialize_rank](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer.initialize_rank)Initialize a rank with specified number of pages.

-
–[run](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer.run)Run the metadata server.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


|
|

###

`_json_response(content)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer._json_response)

Return ORJSONResponse when available to bypass jsonable_encoder.

###

`_read_json(request)`

`async`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer._read_json)

Parse request JSON using orjson if available.

###

`_setup_routes()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer._setup_routes)

Setup FastAPI routes for new API design.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


###

`batch_allocate_pages_for_keys(request)`

`async`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer.batch_allocate_pages_for_keys)

Allocate one page for each key on a specific rank.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


###

`batch_key_exists(request)`

`async`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer.batch_key_exists)

Check if multiple keys exist in metadata.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


###

`clear(request)`

`async`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer.clear)

###

`confirm_write_for_keys(request)`

`async`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer.confirm_write_for_keys)

Confirm write operations for keys.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


###

`get_key_locations(request)`

`async`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer.get_key_locations)

Get page indices for keys on a specific rank.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


###

`initialize_rank(rank, request)`

`async`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer.initialize_rank)

Initialize a rank with specified number of pages.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


###

`run(host='0.0.0.0', port=18000)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.Hf3fsMetadataServer.run)

Run the metadata server.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


##

`KeyMetadata`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.KeyMetadata)

Manages metadata for a single key across multiple ranks.

Methods:

-
–[add_rank_page](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.KeyMetadata.add_rank_page)Add page allocation for a specific rank.

-
–[get_all_pages](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.KeyMetadata.get_all_pages)Get all (rank, page) pairs for this key.

-
–[get_rank_page](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.KeyMetadata.get_rank_page)Get page index for a specific rank.

-
–[is_complete](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.KeyMetadata.is_complete)Check if all ranks in the TP world have allocated pages.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


##

`RankFileMetadata`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.RankFileMetadata)

Manages file page allocation for a single rank.

Methods:

-
–[allocate_pages](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.RankFileMetadata.allocate_pages)Allocate specified number of free pages.

-
–[get_free_page_count](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.RankFileMetadata.get_free_page_count)Get current number of free pages.

-
–[release_pages](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.RankFileMetadata.release_pages)Release pages back to free pool.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


###

`allocate_pages(num_pages)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.RankFileMetadata.allocate_pages)

Allocate specified number of free pages.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


###

`get_free_page_count()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.RankFileMetadata.get_free_page_count)

###

`release_pages(page_indices)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.RankFileMetadata.release_pages)

Release pages back to free pool.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_metadata_server.py`


##

`run_metadata_server(host='0.0.0.0', port=18000)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_metadata_server.run_metadata_server)

Run the improved HF3FS metadata server.