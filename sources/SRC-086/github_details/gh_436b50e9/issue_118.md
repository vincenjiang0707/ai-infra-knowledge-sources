# [Issue #118] Training code is not working

source: https://github.com/FasterDecoding/Medusa/issues/118
state: open | updated: 2024-08-30T08:08:27Z
labels: 

## 正文

When I am trying to use the example given to train the vicuna 7B model on colab. I am getting the following error. 
```
2024-08-25 17:30:20.138324: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
2024-08-25 17:30:20.171315: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
2024-08-25 17:30:20.181626: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
2024-08-25 17:30:20.202813: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 AVX512F FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
2024-08-25 17:30:21.530445: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
/usr/local/lib/python3.10/dist-packages/transformers/training_args.py:1494: FutureWarning: `evaluation_strategy` is deprecated and will be removed in version 4.46 of 🤗 Transformers. Use `eval_strategy` instead
  warnings.warn(
Loading checkpoint shards:  50% 1/2 [00:49<00:49, 49.97s/it]E0825 17:31:27.240000 139795859210880 torch/distributed/elastic/multiprocessing/api.py:826] failed (exitcode: -9) local_rank: 0 (pid: 8158) of binary: /usr/bin/python3
Traceback (most recent call last):
  File "/usr/local/bin/torchrun", line 8, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.10/dist-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 347, in wrapper
    return f(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/distributed/run.py", line 879, in main
    run(args)
  File "/usr/local/lib/python3.10/dist-packages/torch/distributed/run.py", line 870, in run
    elastic_launch(
  File "/usr/local/lib/python3.10/dist-packages/torch/distributed/launcher/api.py", line 132, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/usr/local/lib/python3.10/dist-packages/torch/distributed/launcher/api.py", line 263, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
=====================================================
medusa/train/train.py FAILED
-----------------------------------------------------
Failures:
  <NO_OTHER_FAILURES>
-----------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2024-08-25_17:31:27
  host      : 4b1a9e8a140f
  rank      : 0 (local_rank: 0)
  exitcode  : -9 (pid: 8158)
  error_file: <N/A>
  traceback : Signal 9 (SIGKILL) received by PID 8158
=====================================================
```

I am not sure why its getting signal kill. 

I tried to run the train with the following code 
```
torchrun --nproc_per_node=1 medusa/train/train.py --model_name_or_path lmsys/vicuna-7b-v1.3 \
    --data_path ShareGPT_Vicuna_unfiltered/ShareGPT_V4.3_unfiltered_cleaned_split.json \
    --bf16 False \
    --output_dir test \
    --num_train_epochs 1 \
    --per_device_train_batch_size 8 \
    --per_device_eval_batch_size 8 \
    --gradient_accumulation_steps 4 \
    --evaluation_strategy "no" \
    --save_strategy "no" \
    --learning_rate 1e-3 \
    --weight_decay 0.0 \
    --warmup_ratio 0.1 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --tf32 False \
    --model_max_length 2048 \
    --lazy_preprocess True \
    --medusa_num_heads 3 \
    --medusa_num_layers 1
```
    
I was not able to run the legacy_train file on the main branch and saw in one issue that backup branch was mentioned with train command so tried this and got it working to this point but after this point its failing. 

## 评论 (2)

### ksajan · 2024-08-25

Here is the error that I get from using the latest method that is given in training using axotl
```
!accelerate launch -m axolotl.cli.train /content/axolotl/examples/medusa/vicuna_7b_qlora_stage1.yml
```
Error
```
/usr/local/lib/python3.10/dist-packages/transformers/utils/generic.py:311: FutureWarning: `torch.utils._pytree._register_pytree_node` is deprecated. Please use `torch.utils._pytree.register_pytree_node` instead.
  torch.utils._pytree._register_pytree_node(
The following values were not passed to `accelerate launch` and had defaults used instead:
	`--num_processes` was set to a value of `1`
	`--num_machines` was set to a value of `1`
	`--mixed_precision` was set to a value of `'no'`
	`--dynamo_backend` was set to a value of `'no'`
To avoid this warning pass in values for each of the problematic parameters or run `accelerate config`.
/usr/local/lib/python3.10/dist-packages/transformers/utils/generic.py:311: FutureWarning: `torch.utils._pytree._register_pytree_node` is deprecated. Please use `torch.utils._pytree.register_pytree_node` instead.
  torch.utils._pytree._register_pytree_node(
2024-08-25 18:01:11.306106: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
2024-08-25 18:01:11.325953: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
2024-08-25 18:01:11.332370: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
2024-08-25 18:01:12.537581: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
/usr/local/lib/python3.10/dist-packages/transformers/utils/generic.py:311: FutureWarning: `torch.utils._pytree._register_pytree_node` is deprecated. Please use `torch.utils._pytree.register_pytree_node` instead.
  torch.utils._pytree._register_pytree_node(
Traceback (most recent call last):
  File "/usr/lib/python3.10/runpy.py", line 187, in _run_module_as_main
    mod_name, mod_spec, code = _get_module_details(mod_name, _Error)
  File "/usr/lib/python3.10/runpy.py", line 110, in _get_module_details
    __import__(pkg_name)
  File "/content/axolotl/src/axolotl/cli/__init__.py", line 21, in <module>
    from axolotl.common.cli import TrainerCliArgs, load_model_and_tokenizer
  File "/content/axolotl/src/axolotl/common/cli.py", line 11, in <module>
    from axolotl.utils.models import load_model, load_tokenizer
  File "/content/axolotl/src/axolotl/utils/models.py", line 11, in <module>
    from peft import PeftConfig, prepare_model_for_kbit_training
  File "/usr/local/lib/python3.10/dist-packages/peft/__init__.py", line 22, in <module>
    from .auto import (
  File "/usr/local/lib/python3.10/dist-packages/peft/auto.py", line 31, in <module>
    from .config import PeftConfig
  File "/usr/local/lib/python3.10/dist-packages/peft/config.py", line 24, in <module>
    from .utils import CONFIG_NAME, PeftType, TaskType
  File "/usr/local/lib/python3.10/dist-packages/peft/utils/__init__.py", line 21, in <module>
    from .loftq_utils import replace_lora_weights_loftq
  File "/usr/local/lib/python3.10/dist-packages/peft/utils/loftq_utils.py", line 26, in <module>
    from huggingface_hub.errors import HFValidationError
ModuleNotFoundError: No module named 'huggingface_hub.errors'
Traceback (most recent call last):
  File "/usr/local/bin/accelerate", line 8, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.10/dist-packages/accelerate/commands/accelerate_cli.py", line 47, in main
    args.func(args)
  File "/usr/local/lib/python3.10/dist-packages/accelerate/commands/launch.py", line 986, in launch_command
    simple_launcher(args)
  File "/usr/local/lib/python3.10/dist-packages/accelerate/commands/launch.py", line 628, in simple_launcher
    raise subprocess.CalledProcessError(returncode=process.returncode, cmd=cmd)
subprocess.CalledProcessError: Command '['/usr/bin/python3', '-m', 'axolotl.cli.train', '/content/axolotl/examples/medusa/vicuna_7b_qlora_stage1.yml']' returned non-zero exit status 1.
```

### tamaghna-dutta · 2024-08-30

I updated huggingface_hub to `0.24.6` after which it told me that it required `tensorflow>=2.17.0`. Then I was getting error 

`module 'tensorflow._api.v2.compat.v2.__internal__' has no attribute 'register_load_context_function'`

So I went and changed the call as per https://github.com/keras-team/tf-keras/issues/257#issuecomment-2016598363

Now I am getting

```
(base) jupyter@experimental-2:~/axolotl$ accelerate launch -m src.axolotl.cli.train examples/medusa/vicuna_7b_stage1.yml 
/opt/conda/lib/python3.10/site-packages/transformers/utils/generic.py:311: FutureWarning: `torch.utils._pytree._register_pytree_node` is deprecated. Please use `torch.utils._pytree.register_pytree_node` instead.
  torch.utils._pytree._register_pytree_node(
The following values were not passed to `accelerate launch` and had defaults used instead:
        `--num_processes` was set to a value of `1`
        `--num_machines` was set to a value of `1`
        `--mixed_precision` was set to a value of `'no'`
        `--dynamo_backend` was set to a value of `'no'`
To avoid this warning pass in values for each of the problematic parameters or run `accelerate config`.
/opt/conda/lib/python3.10/site-packages/transformers/utils/generic.py:311: FutureWarning: `torch.utils._pytree._register_pytree_node` is deprecated. Please use `torch.utils._pytree.register_pytree_node` instead.
  torch.utils._pytree._register_pytree_node(
2024-08-30 07:58:48.524788: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
2024-08-30 07:58:48.549171: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
2024-08-30 07:58:48.556724: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
2024-08-30 07:58:48.573877: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
2024-08-30 07:58:49.935488: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
/opt/conda/lib/python3.10/site-packages/transformers/utils/generic.py:311: FutureWarning: `torch.utils._pytree._register_pytree_node` is deprecated. Please use `torch.utils._pytree.register_pytree_node` instead.
  torch.utils._pytree._register_pytree_node(
/opt/conda/lib/python3.10/site-packages/transformers/deepspeed.py:23: FutureWarning: transformers.deepspeed module is deprecated and will be removed in a future version. Please import deepspeed modules directly from transformers.integrations
  warnings.warn(
Traceback (most recent call last):
  File "/opt/conda/lib/python3.10/site-packages/transformers/utils/import_utils.py", line 1282, in _get_module
    return importlib.import_module("." + module_name, self.__name__)
  File "/opt/conda/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/opt/conda/lib/python3.10/site-packages/transformers/pipelines/__init__.py", line 72, in <module>
    from .table_question_answering import TableQuestionAnsweringArgumentHandler, TableQuestionAnsweringPipeline
  File "/opt/conda/lib/python3.10/site-packages/transformers/pipelines/table_question_answering.py", line 26, in <module>
    import tensorflow_probability as tfp
  File "/opt/conda/lib/python3.10/site-packages/tensorflow_probability/__init__.py", line 22, in <module>
    from tensorflow_probability.python import *  # pylint: disable=wildcard-import
  File "/opt/conda/lib/python3.10/site-packages/tensorflow_probability/python/__init__.py", line 152, in <module>
    dir(globals()[pkg_name])  # Forces loading the package from its lazy loader.
  File "/opt/conda/lib/python3.10/site-packages/tensorflow_probability/python/internal/lazy_loader.py", line 57, in __dir__
    module = self._load()
  File "/opt/conda/lib/python3.10/site-packages/tensorflow_probability/python/internal/lazy_loader.py", line 40, in _load
    module = importlib.import_module(self.__name__)
  File "/opt/conda/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "/opt/conda/lib/python3.10/site-packages/tensorflow_probability/python/experimental/__init__.py", line 31, in <module>
    from tensorflow_probability.python.experimental import bayesopt
  File "/opt/conda/lib/python3.10/site-packages/tensorflow_probability/python/experimental/bayesopt/__init__.py", line 17, in <module>
    from tensorflow_probability.python.experimental.bayesopt import acquisition
  File "/opt/conda/lib/python3.10/site-packages/tensorflow_probability/python/experimental/bayesopt/acquisition/__init__.py", line 19, in <module>
    from tensorflow_probability.python.experimental.bayesopt.acquisition.expected_improvement import GaussianProcessExpectedImprovement
  File "/opt/conda/lib/python3.10/site-packages/tensorflow_probability/python/experimental/bayesopt/acquisition/expected_improvement.py", line 19, in <module>
    from tensorflow_probability.python.distributions import normal
  File "/opt/conda/lib/python3.10/site-packages/tensorflow_probability/python/distributions/__init__.py", line 20, in <module>
    from tensorflow_probability.python.distributions.batch_broadcast import BatchBroadcast
  File "/opt/conda/lib/python3.10/site-packages/tensorflow_probability/python/distributions/batch_broadcast.py", line 20, in <module>
    from tensorflow_probability.python.bijectors import bijector as bijector_lib
  File "/opt/conda/lib/python3.10/site-packages/tensorflow_probability/python/bijectors/__init__.py", line 21, in <module>
    from tensorflow_probability.python.bijectors.batch_normalization import BatchNormalization
  File "/opt/conda/lib/python3.10/site-packages/tensorflow_probability/python/bijectors/batch_normalization.py", line 22, in <module>
    from tensorflow_probability.python.internal import tf_keras
  File "/opt/conda/lib/python3.10/site-packages/tensorflow_probability/python/internal/tf_keras.py", line 23, in <module>
    _keras_version_fn = getattr(tf.keras, "version", None)
  File "/opt/conda/lib/python3.10/site-packages/tensorflow/python/util/lazy_loader.py", line 182, in __getattr__
    if self._tfll_keras_version == "keras_3":
  File "/opt/conda/lib/python3.10/site-packages/tensorflow/python/util/lazy_loader.py", line 182, in __getattr__
    if self._tfll_keras_version == "keras_3":
  File "/opt/conda/lib/python3.10/site-packages/tensorflow/python/util/lazy_loader.py", line 182, in __getattr__
    if self._tfll_keras_version == "keras_3":
  [Previous line repeated 811 more times]
  File "/opt/conda/lib/python3.10/site-packages/tensorflow/python/util/lazy_loader.py", line 178, in __getattr__
    if item in ("_tfll_mode", "_tfll_initialized", "_tfll_name"):
RecursionError: maximum recursion depth exceeded in comparison

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/opt/conda/lib/python3.10/runpy.py", line 187, in _run_module_as_main
    mod_name, mod_spec, code = _get_module_details(mod_name, _Error)
  File "/opt/conda/lib/python3.10/runpy.py", line 110, in _get_module_details
    __import__(pkg_name)
  File "/home/jupyter/axolotl/src/axolotl/cli/__init__.py", line 23, in <module>
    from axolotl.train import TrainDatasetMeta
  File "/home/jupyter/axolotl/src/axolotl/train.py", line 22, in <module>
    from axolotl.utils.trainer import setup_trainer
  File "/home/jupyter/axolotl/src/axolotl/utils/trainer.py", line 16, in <module>
    from axolotl.core.trainer_builder import HFCausalTrainerBuilder
  File "/home/jupyter/axolotl/src/axolotl/core/trainer_builder.py", line 26, in <module>
    from axolotl.utils.callbacks import (
  File "/home/jupyter/axolotl/src/axolotl/utils/callbacks.py", line 9, in <module>
    import evaluate
  File "/opt/conda/lib/python3.10/site-packages/evaluate/__init__.py", line 29, in <module>
    from .evaluation_suite import EvaluationSuite
  File "/opt/conda/lib/python3.10/site-packages/evaluate/evaluation_suite/__init__.py", line 10, in <module>
    from ..evaluator import evaluator
  File "/opt/conda/lib/python3.10/site-packages/evaluate/evaluator/__init__.py", line 27, in <module>
    from .audio_classification import AudioClassificationEvaluator
  File "/opt/conda/lib/python3.10/site-packages/evaluate/evaluator/audio_classification.py", line 23, in <module>
    from .base import EVALUATOR_COMPUTE_RETURN_DOCSTRING, EVALUTOR_COMPUTE_START_DOCSTRING, Evaluator
  File "/opt/conda/lib/python3.10/site-packages/evaluate/evaluator/base.py", line 34, in <module>
    from transformers import Pipeline, pipeline
  File "<frozen importlib._bootstrap>", line 1075, in _handle_fromlist
  File "/opt/conda/lib/python3.10/site-packages/transformers/utils/import_utils.py", line 1272, in __getattr__
    module = self._get_module(self._class_to_module[name])
  File "/opt/conda/lib/python3.10/site-packages/transformers/utils/import_utils.py", line 1284, in _get_module
    raise RuntimeError(
RuntimeError: Failed to import transformers.pipelines because of the following error (look up to see its traceback):
maximum recursion depth exceeded in comparison
Traceback (most recent call last):
  File "/opt/conda/bin/accelerate", line 8, in <module>
    sys.exit(main())
  File "/opt/conda/lib/python3.10/site-packages/accelerate/commands/accelerate_cli.py", line 47, in main
    args.func(args)
  File "/opt/conda/lib/python3.10/site-packages/accelerate/commands/launch.py", line 986, in launch_command
    simple_launcher(args)
  File "/opt/conda/lib/python3.10/site-packages/accelerate/commands/launch.py", line 628, in simple_launcher
    raise subprocess.CalledProcessError(returncode=process.returncode, cmd=cmd)
subprocess.CalledProcessError: Command '['/opt/conda/bin/python3.10', '-m', 'src.axolotl.cli.train', 'examples/medusa/vicuna_7b_stage1.yml']' returned non-zero exit status 1.
```

I even set

```
sys.setrecursionlimit(10000)
```

Still getting the same error
