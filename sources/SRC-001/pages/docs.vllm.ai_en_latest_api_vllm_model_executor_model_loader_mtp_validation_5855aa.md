source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/mtp_validation/
lastmod: 2026-09-23

#

`vllm.model_executor.model_loader.mtp_validation`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.mtp_validation)

Scoped controls for MTP checkpoint completeness validation.

Functions:

-
–[disable_mtp_completeness_check](https://docs.vllm.ai#vllm.model_executor.model_loader.mtp_validation.disable_mtp_completeness_check)Temporarily disable MTP completeness validation for one weight load.

-
–[is_mtp_completeness_check_enabled](https://docs.vllm.ai#vllm.model_executor.model_loader.mtp_validation.is_mtp_completeness_check_enabled)Return whether MTP completeness validation is enabled in this scope.