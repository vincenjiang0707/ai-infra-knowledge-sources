# high-throughput-structure-prediction-with-bionemo-inference-runtime

source: https://developer.nvidia.com/blog/high-throughput-structure-prediction-with-bionemo-inference-runtime/

Biomolecular structure prediction is now often run at proteome scale, where the goal is to move an entire worklist through the pipeline efficiently.

[NVIDIA BioNeMo Inference Runtime](https://docs.nvidia.com/bionemo/inference-runtime/overview/) (BioIR) helps accelerate supported biomolecular structure-prediction models on NVIDIA GPUs while keeping the familiar PyTorch workflow. It uses optimized kernels and, where applicable, CUDA Graphs to speed model execution. For large batches of independent inputs, Ray can run a complete model replica on each GPU in a single node to increase overall throughput.

BioIR has also been used in real proteome-scale work, including the [recent expansion of the AlphaFold Database](https://doi.org/10.64898/2026.03.27.714458) (AFDB), accelerating the generation of protein-complex structures across 4,777 proteomes, about 31 million candidate complexes in total, with 1.81 million released as high-confidence predictions.

You can use it in two ways (see Figure 1, below):

- The end-to-end processor moves an InputRequest through parsing, tokenization, feature generation, GPU inference, and PDB or mmCIF writing.
- Direct PyTorch integration lets you construct a supported model (torch.nn.Module) or reuse selected modules in custom code.

This tutorial walks through BioIR’s end-to-end processor, from input preparation to GPU inference and PDB or mmCIF output, and shows how to track structures per hour and resource efficiency.

## Prerequisites

- Python 3.12 or later
- A compatible NVIDIA GPU and driver, plus a BioIR wheel or supported development environment
- A
[staged model checkpoint](https://www.google.com/url?q=https://docs.nvidia.com/bionemo/inference-runtime/references/dev/&sa=D&source=docs&ust=1788374353897146&usg=AOvVaw14PU3b1hx9Ph1E05tQBeXy)(in the below example, Boltz-2) and required chemical metadata - Each protein chain requires an A3M MSA. For inputs with multiple non-identical protein chains, paired or unpaired MSA are accepted
- For Ray throughput scaling, use several visible GPUs on the same node and more independent records than replicas

The wheel contains precompiled CUBINs, so runtime use does not require `nvcc`

, CUDA source, CMake, or the CUDA toolkit.

## Step 1. Choose a supported structure-prediction workflow

In the following, we demonstrate the end-to-end workflow for Boltz2 in BioIR. Use `model_source="boltz-2"`

. Protein chains require an MSA; paired or unpaired MSAs are accepted for inputs with multiple non-identical protein chains. You can optionally supply templates yourself because BioIR does not run HHsearch or HMMsearch. The end-to-end processor supports ligand structure prediction, but not ligand-affinity prediction.

`from` `bionemo_ir.data.schemas ` `import` `InputRequest, MSARecord, Polymer` ` ` `request ` `=` `InputRequest(` ` ` `input_id` `=` `"demo"` `,` ` ` `polymers` `=` `[` ` ` `Polymer(` ` ` `polymer_type` `=` `"protein"` `,` ` ` `chain_id` `=` `[` `"A"` `],` ` ` `sequence` `=` `"GSHMSL..."` `,` ` ` `msas` `=` `[MSARecord(path` `=` `"msa.a3m"` `, ` `format` `=` `"a3m"` `)],` ` ` `paired_msas` `=` `[],` ` ` `templates` `=` `None` `,` ` ` `)` ` ` `],` `)` ` ` `rows ` `=` `[{` `"record"` `: request, ` `"__record_id"` `: request[` `"input_id"` `]}]` |

Replace the truncated sequence and MSA path with valid values. For Ray tests, build rows from a real worklist with more records than replicas; do not repeat one row as evidence of useful scaling.

## Step 2. Validate one prediction with the serial processor

BioIR has two executor backends for the end-to-end processor workflow: serial and Ray. The serial backend runs each stage in sequence for one input, completing the full workflow before moving to the next input. This makes it useful for checking your setup before using the Ray backend to process independent inputs concurrently in Step 3.

`import` `json` ` ` `from` `bionemo_ir.pipeline.processor.engine_proc ` `import` `(` ` ` `EngineProcessorConfig,` ` ` `build_processor,` `)` `from` `bionemo_ir.pipeline.stages.configs ` `import` `(` ` ` `FeatureGeneratorStageConfig,` ` ` `WriterStageConfig,` `)` ` ` `serial_config ` `=` `EngineProcessorConfig(` ` ` `model_source` `=` `"boltz-2"` `,` ` ` `executor_backend` `=` `None` `, ` `# None mean the serial processor` ` ` `runtime_args` `=` `{` ` ` `"recycling_steps"` `: ` `3` `,` ` ` `"num_sampling_steps"` `: ` `50` `,` ` ` `"diffusion_samples"` `: ` `1` `,` ` ` `},` ` ` `feature_generator_stage` `=` `FeatureGeneratorStageConfig(` ` ` `init_context` `=` `{` `"random_seed"` `: ` `42` `},` ` ` `),` ` ` `writer_stage` `=` `WriterStageConfig(` ` ` `output_path` `=` `"output/serial"` `,` ` ` `format` `=` `"cif"` `,` ` ` `),` ` ` `engine_kwargs` `=` `{` `"profile_inference"` `: ` `True` `},` `)` ` ` `serial_processor ` `=` `build_processor(serial_config)` `serial_outputs ` `=` `serial_processor(rows)` ` ` `for` `row ` `in` `serial_outputs:` ` ` `scores ` `=` `json.loads(row[` `"scores"` `])` ` ` `print` `(row[` `"output_path"` `])` ` ` `print` `(row[` `"model_inference_time"` `])` ` ` `print` `(scores.get(` `"confidence_score"` `))` |

`model_inference_time`

is BioIR’s CUDA-synchronized folding-model forward measurement. It excludes parsing, tokenization, feature generation, postprocessing, and writing. Set the seed through the feature generator’s `init_context`

. The `scores`

field must be decoded, because it is a JSON string.

## Step 3. Scale independent inputs with Ray replicas

The Ray backend can be selected as follows, for the default replica layout:

`from` `bionemo_ir.pipeline.processor.engine_proc ` `import` `EngineProcessorConfig` ` ` `ray_config ` `=` `EngineProcessorConfig.create_default_replica_mode_config(` ` ` `model_source` `=` `"boltz-2"` `,` ` ` `output_dir` `=` `"output/ray"` `,` ` ` `output_format` `=` `"cif"` `,` `)` |

This configuration places one complete model replica on each visible GPU on the current node, and sizes CPU stages from `torch.cuda.device_count()`

. Below is an alternative configuration that controls four GPUs explicitly:

`import` `ray` ` ` `from` `bionemo_ir.pipeline.processor.engine_proc ` `import` `(` ` ` `EngineProcessorConfig,` ` ` `build_processor,` `)` `from` `bionemo_ir.pipeline.stages.configs ` `import` `(` ` ` `EngineStageConfig,` ` ` `FeatureGeneratorStageConfig,` ` ` `ParallelismMode,` ` ` `ParserStageConfig,` ` ` `TokenizerStageConfig,` ` ` `WriterStageConfig,` `)` ` ` `ray_config ` `=` `EngineProcessorConfig(` ` ` `model_source` `=` `"boltz-2"` `,` ` ` `executor_backend` `=` `"ray"` `, ` `# selects the ray backend` ` ` `parser_stage` `=` `ParserStageConfig(compute` `=` `4` `),` ` ` `tokenizer_stage` `=` `TokenizerStageConfig(compute` `=` `4` `, num_cpus` `=` `2` `),` ` ` `feature_generator_stage` `=` `FeatureGeneratorStageConfig(` ` ` `compute` `=` `8` `,` ` ` `num_cpus` `=` `4` `,` ` ` `init_context` `=` `{` `"random_seed"` `: ` `42` `},` ` ` `),` ` ` `engine_stage` `=` `EngineStageConfig(` ` ` `parallelism_mode` `=` `ParallelismMode.REPLICA,` ` ` `compute` `=` `4` `,` ` ` `num_gpus` `=` `1.0` `,` ` ` `num_cpus` `=` `4` `,` ` ` `),` ` ` `writer_stage` `=` `WriterStageConfig(` ` ` `compute` `=` `4` `,` ` ` `output_path` `=` `"output/ray"` `,` ` ` `format` `=` `"cif"` `,` ` ` `),` `)` ` ` `ray_processor ` `=` `build_processor(ray_config)` `dataset ` `=` `ray.data.from_items(rows)` `ray_outputs ` `=` `list` `(ray_processor(dataset).materialize().iter_rows())` |

The capacity rule is `engine_stage.compute × engine_stage.num_gpus ≤ visible GPUs`

. This four-replica example is a single-node configuration that assumes four visible GPUs. This tutorial does not cover multi-node deployment. Here Ray creates four engine actors and reserves one GPU for each. Every actor loads the full model. `build_processor`

initializes Ray if needed. Actual throughput depends on input distribution, stage balance, storage, scheduling, and failures, so measure it.

## Step 4. Balance the five processor stages

In the ray end-to-end processor, the five processor stages consume inputs in this dependency order: Parser → Tokenizer → Feature generator → Folding engine → Writer. Configure each stage with its matching *StageConfig; the Step 3 example shows the relevant fields. The `enabled`

field is not a public skip control. Each stage exposes `compute`

; relevant stages also expose `num_cpus`

, `memor`

y, and `batch_size`

. The Ray engine adds `max_concurrent_batches`

, `accelerator_type`

, and `num_gpus`

.

To tune the Ray pipeline, start with `EngineProcessorConfig.create_default_replica_mode_config(...)`

. Increase a stage’s `compute`

to add workers; use `num_cpus`

, `memory`

, and, for engine actors, `num_gpus`

to set resource reservations. Add parser, tokenizer, or feature workers if engines wait for inputs. Reduce concurrency or separate large inputs when GPU or object-store memory causes failures.

Ray is designed to overlap CPU stages with inference, but whether this improves the target workload depends on the run time cost of the parsing, feature generation, and output writing stages for a given input on a given hardware configuration. Refer to Figure 4 at [ScaleFold](https://arxiv.org/pdf/2404.11068) to see the diversity in pre-processing times for OpenFold.

## Step 5. Separate per-replica acceleration from pipeline scaling

BioIR provides optimization at three distinct layers:

**Kernel selection:**Supported operations select compatible BioIR custom, cuEquivariance, or PyTorch fallback implementations based on the model configuration, GPU, data type, and tensor shape.**Module optimization:**Where supported, the separate optimize() mechanism enables CUDA Graph capture for compatible modules.**Pipeline scaling:**The Ray executor places complete model replicas on GPUs and distributes independent inputs among them.

These layers target different bottlenecks. Kernel and module optimizations reduce model-forward time within a replica. Ray can increase worklist throughput by overlapping CPU stages with GPU folding and by running full-model replicas on separate GPUs for independent inputs. Ray does not split a single model forward pass across GPUs. Figure 1, above, distinguishes the processor and direct-integration paths; Ray scaling applies only to the processor path.

Our early benchmarking with BioNeMo Inference Runtime estimated the following model-forward accelerations:

Speedups measured using 1 warmup run (discarded) and 1 measurement call across 17 inputs spanning 29–1,734 residues. OpenFold3 and Boltz2 OSS baselines used `torch.compile`

with `dynamic=None`

, `fullgraph=False`

, `recompile_limit=128`

, `accumulated_recompile_limit=256`

, `fail_on_recompile_limit_hit=True`

. Boltz2 OSS used cuEq; OpenFold3 OSS used `use_cuequivariance=True`

and `use_deepspeed=True`

.

These results quantify acceleration within one model replica. They do not measure parsing, feature generation, output writing, Ray scheduling, multi-GPU throughput, or complete-worklist wall time. Figure 3, below, shows why model-forward and end-to-end measurements must remain separate.

To determine what additional GPUs unlock for a real deployment, measure the same representative worklist with one, two, and four Ray replicas on a single node. Step 6 defines the required metrics and comparison method.

## Step 6. Benchmark folding-stage efficiency and end-to-end delivery: AFDB – A Case Study

To make these measurements concrete, we ran a matched benchmark on 1,000 human dimer targets with combined sequence lengths below 2,800 residues, representing a large collection of independent biomolecular structure-prediction tasks [similar to the recently added dataset in the AlphaFold Database](https://doi.org/10.64898/2026.03.27.714458).

This representative folding-stage benchmark compares BioIR-accelerated Boltz-2 with a torch compiled open-source Boltz-2 implementation, on 8xH100 GPUs. Both implementations used the same targets, staged MSAs, inference recipe, and GPU configuration; throughput metrics and other results are specific to this configuration and should not be generalized to all BioIR-supported models, datasets, or hardware.

The workflow used three recycles, 200 sampling steps, and five diffusion samples per target. BioIR completed all 1,000 targets and delivered 58.5K successfully folded residues per allocated GPU-hour, compared with 20.2K for the public implementation—a 2.90× improvement in residue-normalized throughput; the open-source implementation ran out of memory on 29 targets.

The left panel of Figure 3, above, compares the model-forward times of the BioIR and torch-compiled open-source implementations and directly shows the lower model-forward time delivered by BioIR. The right panel of Figure 3 compares the throughput delivered by BioIR with the open-source implementation, where throughput is the total number of residues in the predicted structures normalized by allocated GPU-hours. The right panel of Figure 3 shows the speedup delivered by the kernel-level, module-level, and pipeline-level optimizations in BioIR. The left panel of Figure 3 shows the speedup delivered by the kernel-level and module-level implementations.

Similar to Boltz2 accelerations, BIR also enables faster inference for other biomolecular cofolding models, such as OpenFold2 and OpenFold3. An early version of BIR contributed accelerated modules to an NVIDIA-internal version of OpenFold2-MM, which enabled protein structure predictions at scale for the AFDB with 31 million protein complex structures.

We linearly extrapolated the 1000-target matched benchmark from Figure 3 to one million comparable targets using rated-power equivalents for an 8 x H100 80GB HBM3 node (see Figure 4, below).

BioIR is estimated to require 11 MWh versus 35 MWh for the public implementation using 8-GPU TDP (Thermal Design Power) equivalents, and 21 MWh versus 64 MWh using full-node maximum-power equivalents. These are folding-only estimates for IT equipment, not metered energy measurements, and exclude data center overhead, such as power usage effectiveness (PUE).

The controlled comparison measures folding throughput with the same inputs and MSAs for each implementation; it excludes MSA generation, preprocessing CPU allocations, storage, data transfer, retries, and engineering overhead. Report end-to-end pipeline performance metrics as distinct from model-forward metrics, including completed structures per hour, GPU and CPU utilization, peak GPU memory, completion rate, failures, and retries.

## Troubleshooting

**Only one GPU is active:**Confirm Ray,`REPLICA`

, more than one replica, several visible GPUs, and enough independent records.**Processor construction raises `ValueError`:**Check that`compute * num_gpus`

doesn’t exceed visible GPUs.**Protein input fails:**Check the required unpaired A3M and worker-visible paths.**GPUs wait:**Inspect CPU stages, CPU reservations, queueing, and Ray object-store capacity before adding replicas.**Rows wait after inference:**Inspect writer concurrency and destination throughput.**Ray cannot place actors:**Check CPU, GPU, memory, and`accelerator_type`

labels.**One record stops the job:**The fail-fast default raises`FoldingPredictionError`

. Set`should_continue_on_error=True`

only for intended row-level continuation, then`inspect __inference_error__`

.

## Get started

Explore BioNeMo Inference Runtime (BioIR) and integrate it into your structure prediction workflows at scale: [http://github.com/NVIDIA-BioNeMo/BioNeMo-Inference-Runtime](http://github.com/NVIDIA-BioNeMo/BioNeMo-Inference-Runtime)

To further accelerate drug discovery workflows with agentic orchestration, check out NVIDIA [BioNeMo Agent Toolkit (BAT)](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit).

For the latest acceleration numbers, consult the [API reference](https://docs.nvidia.com/bionemo/inference-runtime/references/api/) and [support matrix](https://docs.nvidia.com/bionemo/inference-runtime/references/support-matrix/).

## Start the discussion at forums.developer.nvidia.com
