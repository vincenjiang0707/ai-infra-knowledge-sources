source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/hf3fs_mock_client/
lastmod: 2026-09-23

#

`vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.hf3fs_mock_client`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.hf3fs_mock_client)

Classes:

-
–[Hf3fsClient](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.hf3fs_mock_client.Hf3fsClient)Mock HF3FS client using file backend for debugging and testing.


##

`Hf3fsClient`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.hf3fs_mock_client.Hf3fsClient)

Mock HF3FS client using file backend for debugging and testing.

Methods:

-
–[batch_read](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.hf3fs_mock_client.Hf3fsClient.batch_read)Read data from file at specified offsets into tensors.

-
–[batch_write](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.hf3fs_mock_client.Hf3fsClient.batch_write)Write data from tensors to file at specified offsets.

-
–[close](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.hf3fs_mock_client.Hf3fsClient.close)Close the client (no-op for file backend).

-
–[flush](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.hf3fs_mock_client.Hf3fsClient.flush)Flush any pending writes (no-op for file backend).

-
–[get_size](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.hf3fs_mock_client.Hf3fsClient.get_size)Get the total size of the storage file.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/hf3fs_mock_client.py`


|
|

###

`_convert_buffer_to_tensor(buffer_data, dtype)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.hf3fs_mock_client.Hf3fsClient._convert_buffer_to_tensor)

Convert buffer data to tensor with proper dtype handling.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/hf3fs_mock_client.py`


###

`_ensure_file_exists()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.hf3fs_mock_client.Hf3fsClient._ensure_file_exists)

Create file if it doesn't exist.

###

`_tensor_to_bytes(tensor)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.hf3fs_mock_client.Hf3fsClient._tensor_to_bytes)

Convert tensor to bytes with proper dtype handling.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/hf3fs_mock_client.py`


###

`batch_read(offsets, tensors)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.hf3fs_mock_client.Hf3fsClient.batch_read)

Read data from file at specified offsets into tensors.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/hf3fs_mock_client.py`


###

`batch_write(offsets, tensors, event)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.hf3fs_mock_client.Hf3fsClient.batch_write)

Write data from tensors to file at specified offsets.