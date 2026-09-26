source: https://docs.vllm.ai/en/latest/design/io_processor_plugins/
lastmod: 2026-09-24

# IO Processor Plugins[¶](https://docs.vllm.ai#io-processor-plugins)

IO Processor plugins are a feature that allows pre- and post-processing of the model input and output for pooling models. The idea is that users are allowed to pass a custom input to vLLM that is converted into one or more model prompts and fed to the model `encode`

method. One potential use-case of such plugins is that of using vLLM for generating multi-modal data. Say users feed an image to vLLM and get an image in output.

When performing an inference with IO Processor plugins, the prompt type is defined by the plugin and the same is valid for the final request output. vLLM does not perform any validation of input/output data, and it is up to the plugin to ensure the correct data is being fed to the model and returned to the user. As of now these plugins support only pooling models and can be triggered via the `encode`

method in [ LLM](https://docs.vllm.ai/api/vllm/entrypoints/llm/#vllm.entrypoints.llm.LLM) and

[, or in online serving mode via the](https://docs.vllm.ai/api/vllm/v1/engine/async_llm/#vllm.v1.engine.async_llm.AsyncLLM)

`AsyncLLM`

`/pooling`

endpoint.## Writing an IO Processor Plugin[¶](https://docs.vllm.ai#writing-an-io-processor-plugin)

IO Processor plugins implement the [ IOProcessor](https://docs.vllm.ai/api/vllm/plugins/io_processors/interface/#vllm.plugins.io_processors.interface.IOProcessor) interface:

IOProcessorInput = TypeVar("IOProcessorInput")
IOProcessorOutput = TypeVar("IOProcessorOutput")
class IOProcessor(ABC, Generic[IOProcessorInput, IOProcessorOutput]):
"""Abstract interface for pre/post-processing of engine I/O."""
def __init__(self, vllm_config: VllmConfig, renderer: BaseRenderer):
super().__init__()
self.vllm_config = vllm_config
def parse_data(self, data: object) -> IOProcessorInput:
raise NotImplementedError
def merge_sampling_params(
self,
params: SamplingParams | None = None,
) -> SamplingParams:
return params or SamplingParams()
def merge_pooling_params(
self,
params: PoolingParams | None = None,
) -> PoolingParams:
return params or PoolingParams(task="plugin")
@abstractmethod
def pre_process(
self,
prompt: IOProcessorInput,
request_id: str | None = None,
**kwargs,
) -> PromptType | Sequence[PromptType]:
raise NotImplementedError
async def pre_process_async(
self,
prompt: IOProcessorInput,
request_id: str | None = None,
**kwargs,
) -> PromptType | Sequence[PromptType]:
return self.pre_process(prompt, request_id, **kwargs)
@abstractmethod
def post_process(
self,
model_output: Sequence[PoolingRequestOutput],
request_id: str | None = None,
**kwargs,
) -> IOProcessorOutput:
raise NotImplementedError
async def post_process_async(
self,
model_output: AsyncGenerator[tuple[int, PoolingRequestOutput]],
request_id: str | None = None,
**kwargs,
) -> IOProcessorOutput:
# We cannot guarantee outputs are returned in the same order they were
# fed to vLLM.
# Let's sort them by id before post_processing
sorted_output = sorted(
[(i, item) async for i, item in model_output], key=lambda output: output[0]
)
collected_output = [output[1] for output in sorted_output]
return self.post_process(collected_output, request_id=request_id, **kwargs)


The `parse_data`

method is used for validating the user data and converting it into the input expected by the `pre_process*`

methods. The `merge_sampling_params`

and `merge_pooling_params`

methods merge input [ SamplingParams](https://docs.vllm.ai/api/vllm/sampling_params/#vllm.sampling_params.SamplingParams) or

[(if any) with the default one. The](https://docs.vllm.ai/api/vllm/pooling_params/#vllm.pooling_params.PoolingParams)

`PoolingParams`

`pre_process*`

methods take the validated plugin input to generate vLLM's model prompts for regular inference. The `post_process*`

methods take [objects as input and generate a custom plugin output.](https://docs.vllm.ai/api/vllm/outputs/#vllm.outputs.PoolingRequestOutput)

`PoolingRequestOutput`

An example implementation of a plugin that enables generating geotiff images with the PrithviGeospatialMAE model is available [here](https://github.com/IBM/terratorch/tree/main/terratorch/vllm/plugins/segmentation). Please, also refer to our online ([ examples/pooling/plugin/prithvi_geospatial_mae_online.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/plugin/prithvi_geospatial_mae_online.py)) and offline ([ examples/pooling/plugin/prithvi_geospatial_mae_io_processor.py](https://github.com/vllm-project/vllm/blob/main/examples/pooling/plugin/prithvi_geospatial_mae_io_processor.py)) inference examples.

## Using an IO Processor plugin[¶](https://docs.vllm.ai#using-an-io-processor-plugin)

IO Processor plugins are loaded at engine startup and there are two methods for specifying the name of the plugin to be loaded:

- Via vLLM's
: setting the`EngineArgs`

`io_processor_plugin`

argument in theused to initialize the`EngineArgs`

. The same can be achieved by passing the`AsyncLLM`

`io_processor_plugin`

argument toin offline mode, or by passing the`LLM`

`--io-processor-plugin`

argument in serving mode. - Via the model HF configuration: adding an
`io_processor_plugin`

field to the model config (config.json).

The order also determines method priority. i.e., setting the plugin name via [ EngineArgs](https://docs.vllm.ai/api/vllm/engine/arg_utils/#vllm.engine.arg_utils.EngineArgs) will override any plugin name specified in the model HF config (config.json).