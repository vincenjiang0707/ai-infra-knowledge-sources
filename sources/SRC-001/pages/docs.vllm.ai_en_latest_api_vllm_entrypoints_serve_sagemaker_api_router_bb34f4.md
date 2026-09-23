source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/sagemaker/api_router/
lastmod: 2026-09-23

#

`vllm.entrypoints.serve.sagemaker.api_router`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.sagemaker.api_router)

Functions:

-
–[attach_router](https://docs.vllm.ai#vllm.entrypoints.serve.sagemaker.api_router.attach_router)Attach the SageMaker hosting endpoints to the API server.

-
–[sagemaker_standards_bootstrap](https://docs.vllm.ai#vllm.entrypoints.serve.sagemaker.api_router.sagemaker_standards_bootstrap)Bootstrap the app with the SageMaker hosting standards.


##

`_attach_router(app, supported_tasks, model_config=None)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.sagemaker.api_router._attach_router)

Register the SageMaker hosting routes (/ping, /invocations) on the app.

## Source code in `vllm/entrypoints/serve/sagemaker/api_router.py`


##

`_restore_handler_levels(snapshot)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.sagemaker.api_router._restore_handler_levels)

Restore handler levels from a snapshot.

##

`_snapshot_handler_levels()`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.sagemaker.api_router._snapshot_handler_levels)

Snapshot handler levels for loggers that may be affected by third-party logging configuration side effects (e.g. model_hosting_container_standards calling configure_root_logger() at import time).

## Source code in `vllm/entrypoints/serve/sagemaker/api_router.py`


##

`attach_router(app, supported_tasks, model_config=None)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.sagemaker.api_router.attach_router)

Attach the SageMaker hosting endpoints to the API server.

Handler levels are snapshotted and restored because importing model_hosting_container_standards may reconfigure root logging.

## Source code in `vllm/entrypoints/serve/sagemaker/api_router.py`


##

`sagemaker_standards_bootstrap(app)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.sagemaker.api_router.sagemaker_standards_bootstrap)

Bootstrap the app with the SageMaker hosting standards.

Handler levels are restored right after the import because importing model_hosting_container_standards may reconfigure root logging, and bootstrap must run with the original levels.