source: https://docs.nvidia.com/cupti/api/namespaceNV_1_1Cupti_1_1Checkpoint.html

# 8.2.1.1. Checkpoint[#](https://docs.nvidia.com#checkpoint)

Fully qualified name: `NV::Cupti::Checkpoint`


-
namespace Checkpoint
[#](https://docs.nvidia.com#_CPPv4N2NV5Cupti10CheckpointE)

## 8.2.1.1.2. Data Structures[#](https://docs.nvidia.com#data-structures)

[CUpti_Checkpoint](https://docs.nvidia.com/structNV_1_1Cupti_1_1Checkpoint_1_1CUpti__Checkpoint.html#structnv_1_1cupti_1_1checkpoint_1_1cupti__checkpoint)Configuration and handle for a CUPTI Checkpoint.


## 8.2.1.1.3. Enumerations[#](https://docs.nvidia.com#enumerations)

[CUpti_CheckpointOptimizations](https://docs.nvidia.com/group__CUPTI__CHECKPOINT__API.html#group__cupti__checkpoint__api_1ga4d49e28d43be23e549b827292271b56d)Specifies optimization options for a checkpoint, may be OR'd together to specify multiple options.


## 8.2.1.1.4. Functions[#](https://docs.nvidia.com#functions)

- CUptiResult
[cuptiCheckpointFree](https://docs.nvidia.com/group__CUPTI__CHECKPOINT__API.html#group__cupti__checkpoint__api_1ga8aaeedd9f88919cdc35baa0a10492c09)(CUpti_Checkpoint *const handle) Free the backing data for a checkpoint.

- CUptiResult
[cuptiCheckpointRestore](https://docs.nvidia.com/group__CUPTI__CHECKPOINT__API.html#group__cupti__checkpoint__api_1ga21cdc23dcb04894c0a59cb1fd4da430f)(CUpti_Checkpoint *const handle) Restore a checkpoint to the device associated with its context.

- CUptiResult
[cuptiCheckpointSave](https://docs.nvidia.com/group__CUPTI__CHECKPOINT__API.html#group__cupti__checkpoint__api_1ga90ea5f5068de6135df6b409fa09f947b)(CUpti_Checkpoint *const handle) Initialize and save a checkpoint of the device state associated with the handle context.