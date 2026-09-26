source: https://docs.nvidia.com/cupti/api/group__CUPTI__CHECKPOINT__API.html

# 6.3. CUPTI Checkpoint API[#](https://docs.nvidia.com#cupti-checkpoint-api)

Functions, types, and enums that implement the CUPTI Checkpoint API.

## 6.3.1. Data Structures[#](https://docs.nvidia.com#data-structures)

[NV::Cupti::Checkpoint::CUpti_Checkpoint](https://docs.nvidia.com/structNV_1_1Cupti_1_1Checkpoint_1_1CUpti__Checkpoint.html#structnv_1_1cupti_1_1checkpoint_1_1cupti__checkpoint)Configuration and handle for a CUPTI Checkpoint.


## 6.3.2. Macros[#](https://docs.nvidia.com#macros)

## 6.3.3. Enumerations[#](https://docs.nvidia.com#enumerations)

[NV::Cupti::Checkpoint::CUpti_CheckpointOptimizations](https://docs.nvidia.com#group__cupti__checkpoint__api_1ga4d49e28d43be23e549b827292271b56d)Specifies optimization options for a checkpoint, may be OR'd together to specify multiple options.


## 6.3.4. Functions[#](https://docs.nvidia.com#functions)

- CUptiResult
[NV::Cupti::Checkpoint::cuptiCheckpointFree](https://docs.nvidia.com#group__cupti__checkpoint__api_1ga8aaeedd9f88919cdc35baa0a10492c09)(CUpti_Checkpoint *const handle) Free the backing data for a checkpoint.

- CUptiResult
[NV::Cupti::Checkpoint::cuptiCheckpointRestore](https://docs.nvidia.com#group__cupti__checkpoint__api_1ga21cdc23dcb04894c0a59cb1fd4da430f)(CUpti_Checkpoint *const handle) Restore a checkpoint to the device associated with its context.

- CUptiResult
[NV::Cupti::Checkpoint::cuptiCheckpointSave](https://docs.nvidia.com#group__cupti__checkpoint__api_1ga90ea5f5068de6135df6b409fa09f947b)(CUpti_Checkpoint *const handle) Initialize and save a checkpoint of the device state associated with the handle context.


## 6.3.5. Macros[#](https://docs.nvidia.com#id1)

-
CUpti_Checkpoint_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Checkpoint_STRUCT_SIZE)

## 6.3.6. Enumerations[#](https://docs.nvidia.com#id2)

-
enum
[NV](https://docs.nvidia.com/namespaceNV.html#_CPPv42NV)::[Cupti](https://docs.nvidia.com/namespaceNV_1_1Cupti.html#_CPPv4N2NV5CuptiE)::[Checkpoint](https://docs.nvidia.com/namespaceNV_1_1Cupti_1_1Checkpoint.html#_CPPv4N2NV5Cupti10CheckpointE)::CUpti_CheckpointOptimizations[#](https://docs.nvidia.com#_CPPv4N2NV5Cupti10Checkpoint29CUpti_CheckpointOptimizationsE) Specifies optimization options for a checkpoint, may be OR’d together to specify multiple options.

*Values:*-
enumerator CUPTI_CHECKPOINT_OPT_NONE
[#](https://docs.nvidia.com#_CPPv4N2NV5Cupti10Checkpoint29CUpti_CheckpointOptimizations25CUPTI_CHECKPOINT_OPT_NONEE) Default behavior.


-
enumerator CUPTI_CHECKPOINT_OPT_TRANSFER
[#](https://docs.nvidia.com#_CPPv4N2NV5Cupti10Checkpoint29CUpti_CheckpointOptimizations29CUPTI_CHECKPOINT_OPT_TRANSFERE) Determine which mem blocks have changed, and only restore those. This optimization is cached, which means cuptiCheckpointRestore must always be called at the same point in the application when this option is enabled, or the result may be incorrect.


-
enumerator CUPTI_CHECKPOINT_OPT_NONE

## 6.3.7. Functions[#](https://docs.nvidia.com#id3)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)[NV](https://docs.nvidia.com/namespaceNV.html#_CPPv42NV)::[Cupti](https://docs.nvidia.com/namespaceNV_1_1Cupti.html#_CPPv4N2NV5CuptiE)::[Checkpoint](https://docs.nvidia.com/namespaceNV_1_1Cupti_1_1Checkpoint.html#_CPPv4N2NV5Cupti10CheckpointE)::cuptiCheckpointFree( ,[CUpti_Checkpoint](https://docs.nvidia.com/structNV_1_1Cupti_1_1Checkpoint_1_1CUpti__Checkpoint.html#_CPPv4N2NV5Cupti10Checkpoint16CUpti_CheckpointE)*const handleFree the backing data for a checkpoint.

Frees all associated device, host memory and filesystem storage used for this context. After freeing a handle, it may be re-used as if it was new - options may be re-configured and will take effect on the next call to

`cuptiCheckpointSave`

.- Parameters:
**handle**– A pointer to a previously saved[CUpti_Checkpoint](https://docs.nvidia.com/structNV_1_1Cupti_1_1Checkpoint_1_1CUpti__Checkpoint.html#structnv_1_1cupti_1_1checkpoint_1_1cupti__checkpoint)object- Return values:
**CUPTI_SUCCESS**– if the handle was successfully freed**CUPTI_ERROR_INVALID_PARAMETER**– if the handle was already freed or appears invalid**CUPTI_ERROR_INVALID_CONTEXT**– if the context is no longer valid



[#](https://docs.nvidia.com#_CPPv4N2NV5Cupti10Checkpoint19cuptiCheckpointFreeEPC16CUpti_Checkpoint)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)[NV](https://docs.nvidia.com/namespaceNV.html#_CPPv42NV)::[Cupti](https://docs.nvidia.com/namespaceNV_1_1Cupti.html#_CPPv4N2NV5CuptiE)::[Checkpoint](https://docs.nvidia.com/namespaceNV_1_1Cupti_1_1Checkpoint.html#_CPPv4N2NV5Cupti10CheckpointE)::cuptiCheckpointRestore( ,[CUpti_Checkpoint](https://docs.nvidia.com/structNV_1_1Cupti_1_1Checkpoint_1_1CUpti__Checkpoint.html#_CPPv4N2NV5Cupti10Checkpoint16CUpti_CheckpointE)*const handleRestore a checkpoint to the device associated with its context.

Restores device, pinned, and allocated memory to the state when the checkpoint was saved

- Parameters:
**handle**– A pointer to a previously saved[CUpti_Checkpoint](https://docs.nvidia.com/structNV_1_1Cupti_1_1Checkpoint_1_1CUpti__Checkpoint.html#structnv_1_1cupti_1_1checkpoint_1_1cupti__checkpoint)object- Return values:
**CUTPI_SUCCESS**– if the checkpoint was successfully restored**CUPTI_ERROR_NOT_INITIALIZED**– if the checkpoint was not previously initialized**CUPTI_ERROR_INVALID_CONTEXT**–**CUPTI_ERROR_INVALID_PARAMETER**– if the handle appears invalid**CUPTI_ERROR_UNKNOWN**– if the restore or optimization operation fails



[#](https://docs.nvidia.com#_CPPv4N2NV5Cupti10Checkpoint22cuptiCheckpointRestoreEPC16CUpti_Checkpoint)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)[NV](https://docs.nvidia.com/namespaceNV.html#_CPPv42NV)::[Cupti](https://docs.nvidia.com/namespaceNV_1_1Cupti.html#_CPPv4N2NV5CuptiE)::[Checkpoint](https://docs.nvidia.com/namespaceNV_1_1Cupti_1_1Checkpoint.html#_CPPv4N2NV5Cupti10CheckpointE)::cuptiCheckpointSave( ,[CUpti_Checkpoint](https://docs.nvidia.com/structNV_1_1Cupti_1_1Checkpoint_1_1CUpti__Checkpoint.html#_CPPv4N2NV5Cupti10Checkpoint16CUpti_CheckpointE)*const handleInitialize and save a checkpoint of the device state associated with the handle context.

Uses the handle options to configure and save a checkpoint of the device state associated with the specified context.

- Parameters:
**handle**– A pointer to a[CUpti_Checkpoint](https://docs.nvidia.com/structNV_1_1Cupti_1_1Checkpoint_1_1CUpti__Checkpoint.html#structnv_1_1cupti_1_1checkpoint_1_1cupti__checkpoint)object- Return values:
**CUPTI_SUCCESS**– if a checkpoint was successfully initialized and saved**CUPTI_ERROR_INVALID_PARAMETER**– if`handle`

does not appear to refer to a valid[CUpti_Checkpoint](https://docs.nvidia.com/structNV_1_1Cupti_1_1Checkpoint_1_1CUpti__Checkpoint.html#structnv_1_1cupti_1_1checkpoint_1_1cupti__checkpoint)**CUPTI_ERROR_INVALID_CONTEXT**–**CUPTI_ERROR_INVALID_DEVICE**– if device associated with context is not compatible with checkpoint API**CUPTI_ERROR_INVALID_OPERATION**– if Save is requested over an existing checkpoint, but`allowOverwrite`

was not originally specified**CUPTI_ERROR_OUT_OF_MEMORY**– if as configured, not enough backing storage space to save the checkpoint



[#](https://docs.nvidia.com#_CPPv4N2NV5Cupti10Checkpoint19cuptiCheckpointSaveEPC16CUpti_Checkpoint)