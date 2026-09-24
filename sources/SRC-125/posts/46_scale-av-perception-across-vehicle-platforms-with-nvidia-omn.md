# scale-av-perception-across-vehicle-platforms-with-nvidia-omniverse-nurec

source: https://developer.nvidia.com/blog/scale-av-perception-across-vehicle-platforms-with-nvidia-omniverse-nurec/

A perception stack is shaped by the vehicle that carries it. Move the same software to a new carline—for example, from an SUV to a sedan or another vehicle variant in the portfolio—and its perception of the world changes. The sensor placement, calibration, fields of view, occlusions, body geometry, timing, and coverage all shift. A traffic light may appear in a different part of the frame. A curb can become harder to see. A pedestrian near the edge of coverage may become ambiguous. As an autonomous driving stack expands to new carlines and variants, developers must account for these differences even when the underlying perception stack remains the same.

Collecting and labeling a new real-world dataset for every carline is expensive and may not be possible early in vehicle development. New fleets may not be available, and rare conditions can’t always be captured. Real-world driving data remains essential for grounding and validating system performance, but synthetic data can help teams adapt models before a full target-carline dataset exists.

The carline adaptation challenge is to prepare perception software for a vehicle that may not exist yet, and scale that software across platform variants without collecting and labeling a large dataset for each one.

NVIDIA Omniverse NuRec makes this process more practical. It starts with recorded real-world drives, reconstructs each scene, and renders new camera views for a target vehicle configuration.

Developers can reuse real-world data to ask questions such as:

- What would this scenario look like from the target rig?
- Which existing drives cover the new vehicle well?
- Where do geometry changes create weak spots?
- Which gaps require real collection?

This post shows how to adapt a perception stack to a new sensor rig using existing drive data by following these four steps:

- Pairing a reconstructed drive with a target rig configuration.
- Rendering the target views.
- Refining the frames with NVIDIA Harmonizer.
- Training a perception model on the output.

This tutorial uses reconstructed scenes from the NVIDIA [Physical AI NuRec Dataset to complete](https://huggingface.co/datasets/nvidia/PhysicalAI-Autonomous-Vehicles-NuRec) the four steps.

## How NuRec supports carline adaptation

NuRec uses 3D Gaussian splatting to reconstruct real-world environments from sensor data and render them for simulation. For carline adaptation, NuRec reconstructs a real-world drive captured by an existing vehicle and renders new camera streams from the viewpoints of the target vehicle.

Two NuRec capabilities are especially useful for carline adaptation.

**Novel-view synthesis:**NuRec can render the scene with gsplat, which projects the Gaussians through the specified camera model. This capability enables users to change camera extrinsics, intrinsics, field of view, and lens model, including pinhole, fisheye, and f-theta configurations.**Reusable scene data and annotations:**The reconstructed scene retains the original rig trajectories, per-camera calibration, dynamic object tracks, and map data. These assets can be used to align or adapt labels such as objects, lanes, traffic lights, and road boundaries in the newly rendered views.

## Adapt a perception model to a new carline with NuRec

The following workflow shows how development teams can render an existing reconstructed drive through a target camera rig, refine the resulting frames, and prepare the data for perception-model training.

**Step 1. Download a reconstructed scene **

The Physical AI NuRec Dataset on Hugging Face includes more than 1,500 neural-reconstructed driving scenes. Each scene is about 20 seconds long and was reconstructed from six camera views: a 120-degree front-wide view**, a 30-degree front-telephoto view, 120-degree cross-left and cross-right views, and 70-degree rear-left and rear-right views**.

The NuRec Dataset is gated. Accept the license, authenticate with a Hugging Face token, and download one scene.

`import` `os` `from` `huggingface_hub ` `import` `login, snapshot_download` `login(token` `=` `os.getenv(` `"HF_TOKEN"` `))` `# Download one reconstructed scene (USDZ) from the 26.04 release` `snapshot_download(` ` ` `repo_id` `=` `"nvidia/PhysicalAI-Autonomous-Vehicles-NuRec"` `,` ` ` `repo_type` `=` `"dataset"` `,` ` ` `allow_patterns` `=` `"sample_set/26.04_release/<scene-uuid>/*"` `,` `)` |

If using a coding agent, clone the [NVIDIA/nurec-skills](https://github.com/NVIDIA/nurec-skills) repository. It includes skills for downloading Physical AI datasets, rendering with NuRec, and refining output frames.

`git clone https:` `//github` `.com` `/NVIDIA/nurec-skills` `.git` |

**Step 2. Render from the target carline’s sensor rig**

This tutorial uses a synthetic target camera rig included with the public sample. Its camera name, pose, resolution, and lens parameters are illustrative.

The supplied synthetic rig contains one target camera, so this tutorial generates one target-camera stream. In the rig file, each sensor entry defines a colon-delimited camera name, image resolution, an F-Theta lens model, intrinsic parameters, and a camera-to-rig pose.

NRE converts the colon-delimited name to a logical camera ID. For example, it converts camera:front:synthetic:120fov to camera_front_synthetic_120fov. To add another target camera, add another entry to rig.sensors. Give it a unique name and provide its own width, height, lens model, intrinsic parameters, and nominalSensor2Rig_FLU transform.

Set the input and output locations:

`export` `SCENE_DIR=` `/absolute/path/to/scene` `export` `SCENE_FILE=<SCENE_UUID>.usdz` `export` `RIG_DIR=` `/absolute/path/to/rig` `export` `RIG_FILE=minimal-synthetic-target-rig.json` `export` `OUTPUT_DIR=` `/absolute/path/to/output` `mkdir` `-p ` `"$OUTPUT_DIR"` |

Pin the public NuRec container to its immutable digest and pull the image:

`export` `NUREC_IMAGE=` `'nvcr.io/nvidia/nre/nre-ga:26.04.01@sha256:97f43e7130c5636ce3e80ea3184d97f56a87fdd989b05cce42230881dbdea284'` `docker pull ` `"$NUREC_IMAGE"` `docker image inspect ` `"$NUREC_IMAGE"` `--` `format` `'{{range .RepoDigests}}{{println .}}{{end}}'` |

Run trajectory export and rendering as separate container operations. Export the target-camera trajectory:

`docker run --rm --gpus all --shm-size=64g \` ` ` `-v "$SCENE_DIR":/inputs/scene:ro \` ` ` `-v "$RIG_DIR":/inputs/rig:ro \` ` ` `-v "$OUTPUT_DIR":/outputs \` ` ` `"$NUREC_IMAGE" export-custom-rig-trajectory \` ` ` `--artifact-path="/inputs/scene/$SCENE_FILE" \` ` ` `--rig-json="/inputs/rig/$RIG_FILE" \` ` ` `--output=/outputs/custom_rig_trajectories.json` |

Next, run a sparse render of one target camera to validate the setup. In this example, select the target camera camera_front_synthetic_120fov because the example target rig defines a front-facing camera. The render command loads the exported trajectory file and then uses –camera-id to select the camera to render.

The USDZ scene was reconstructed using six source cameras: **a** 120-degree front-wide camera, **a** 30-degree front-telephoto camera, 120-degree cross-left and cross-right cameras, **and **70-degree rear-left and rear-right cameras. A target camera does not need to correspond one-on-one with any of these source cameras. It can use a different position, orientation, resolution, field of view, or calibration, provided that its pose is expressed in the same rig coordinate frame and its lens model is supported by the exporter. Cameras placed far outside the observed trajectory or aimed toward areas with limited source-camera coverage may produce lower-quality renders.

This tutorial uses a front-facing target camera, to adapt another view, for example a rear-left camera, first add a rear-left sensor to the target rig JSON, give it rear-left camera-to-rig extrinsics, export the trajectory again, and pass its normalized logical ID to –camera-id.

`docker run --rm --gpus all --shm-size=64g \` ` ` `-v "$SCENE_DIR":/inputs/scene:ro \` ` ` `-v "$OUTPUT_DIR":/outputs \` ` ` `"$NUREC_IMAGE" render \` ` ` `--artifact-path="/inputs/scene/$SCENE_FILE" \` ` ` `--output-dir=/outputs/smoke \` ` ` `--custom-rig-trajectory=/outputs/custom_rig_trajectories.json \` ` ` `--no-replicate-training-views \` ` ` `--renderer=default \` ` ` `--image-format=png \` ` ` `--frame-step=30 \` ` ` `--image-scale=1 \` ` ` `--frame-naming=frame-end-timestamp \` ` ` `--camera-id=camera_front_synthetic_120fov` |

Review the frames to ensure that the pose, field of view, and timestamps are correct. After the sparse render passes review, render the full sequence with `–frame-step=1` for all target cameras. Repeat –camera-id for each validated camera in the target rig.

**Step 3. Refine the rendered frames **

Neural rendering can leave view-dependent artifacts, inconsistent color or tone, and poorly reconstructed dynamic objects. [NVIDIA Harmonizer](https://github.com/NVIDIA/harmonizer) is a public, temporally aware post-processing model that corrects artifacts in NuRec and related neural renderings. It improves visual quality, but it doesn’t repair incorrect calibration, recover scene coverage that was never reconstructed, or replace target-camera validation.

The *nurec-fixer* skill in [NVIDIA/nurec-skills](https://github.com/NVIDIA/nurec-skills/tree/main/skills/nurec-fixer) covers setup, inference, evaluation, and optional Harmonizer fine-tuning. First, validate the host before downloading the model.

`git clone https:` `//github` `.com` `/NVIDIA/nurec-skills` `.git` `python nurec-skills` `/skills/nurec-fixer/scripts/validate_setup` `.py` |

Accept the model licenses on Hugging Face, clone the Harmonizer repository, build its runtime image, and download the released checkpoints:

`git clone https:` `//github` `.com` `/NVIDIA/harmonizer` `.git` `cd` `harmonizer` `docker build -t harmonizer-cosmos-` `env` `-f Dockerfile.cosmos .` `hf auth login` `.` `/download_checkpoints` `.sh` `test` `-f models` `/diffusion_harmonizer` `.pkl` `test` `-d src` `/checkpoints/nvidia/Cosmos-Predict2-0` `.6B-Text2Image` |

Run one camera sequence at a time. Mount the parent render directory so that the output—which is written beside the input directory—persists on the host:

`export` `HARMONIZER_DIR=` `/absolute/path/to/harmonizer` `export` `RENDER_ROOT=` `/absolute/path/to/output/render` `export` `CAMERA_ID=camera_front_synthetic_120fov` `docker run --` `rm` `--gpus all --ipc=host \` ` ` `--entrypoint python \` ` ` `-` `v` `"$HARMONIZER_DIR"` `:` `/work` `\` ` ` `-` `v` `"$RENDER_ROOT"` `:` `/frames` `\` ` ` `-w ` `/work/src` `\` ` ` `harmonizer-cosmos-` `env` `\` ` ` `inference_pix2pix_turbo_harmonizer.py \` ` ` `--input_image=` `"/frames/$CAMERA_ID"` `\` ` ` `--model_path=` `/work/models/diffusion_harmonizer` `.pkl \` ` ` `--model_identifier=harmonized \` ` ` `--timestep=250 \` ` ` `--resolution=1024 \` ` ` `--use_sched` |

**Step 4. Train the perception model **

After creating NuRec-rendered datasets for a new carline, validate the output before incorporating it into a perception-training pipeline. Treat this new dataset similarly to real camera data collected from vehicles. Then, prepare it for use based on the perception model’s needs.

## Carline adaptation program

NVIDIA evaluated this workflow in an internal automated driving program that needed to support a new camera configuration. The team had an existing library of drives from a different vehicle, but the target carline data was not yet available.

## Automate the workflow with NuRec agentic skills

The [NVIDIA/nurec-skills](https://github.com/NVIDIA/nurec-skills) repository packages the main steps as agent skills. A coding agent can use physical-ai-datasets to locate and download scenes, nre to render them, and nurec-fixer to refine the output.

For an end-to-end example, watch the neural-reconstruction agent-skills livestream.

The public [NVIDIA/nurec-skills](https://github.com/NVIDIA/nurec-skills) repository contains skills for locating Physical AI datasets, using NCore, running NuRec, and applying DiffusionHarmonizer. The `nurec-carline-adaptation`

skill adds a thin compatibility and provenance layer; it does not redistribute NuRec source or models.

`git clone https:` `//github` `.com` `/NVIDIA/nurec-skills` `.git` |

After cloning the repository, ask a compatible coding agent:

*Use the $nurec-carline-adaptation skill to validate this USDZ and sanitized target rig, show me the exact local Docker commands, run a sparse one-camera smoke test, and stop before the full render if any camera or windshield check fails.*

## Apply NuRec to existing drive data

Reconstructing a captured drive requires synchronized videos from the recording rig and the corresponding metadata from the same recording. The source data must then be organized into a consistent layout:

`clip/` `└── raw/` ` ` `├── generated/` ` ` `│ ├── front_wide.mp4` ` ` `│ ├── front_tele.mp4` ` ` `│ ├── cross_left.mp4` ` ` `│ ├── cross_right.mp4` ` ` `│ ├── rear_left.mp4` ` ` `│ ├── rear_right.mp4` ` ` `│ └── rear.mp4` ` ` `└── clipgt/parquets/` ` ` `├── calibration_estimate.parquet` ` ` `├── egomotion_estimate.parquet` ` ` `└── object_fused.parquet` |

MP4s come from the vehicle’s camera recorder. The Parquet files contain metadata shared by the complete camera rig.

Input | What it contains | Typical source |
|---|---|---|
`calibration_estimate.parquet` | Camera lens parameters and mounting positions | Camera-calibration or rig-configuration export |
`egomotion_estimate.parquet` | Vehicle position and orientation over time | Localization, odometry, VIO, or SLAM |
`object_fused.parquet` | Moving objects, classes, dimensions, and track IDs | Perception or labeling pipeline |


*Table 1.**Required metadata files, their contents, and typical sources*All three Parquet files are required by the companion converter and reconstruction recipe used in this tutorial. Other NuRec workflows may support reconstruction without object tracks. These filenames and Parquet serialization are not NCore requirements. If the same information is stored in JSON, a database, or another format, the public NCore converter template can be adapted to read the source.

This workflow assumes that the selected videos are synchronized and span the same recording interval. Calibration data must identify every selected camera, egomotion data must span the sequence from its first exposure through its last, and the object tracks required by this recipe must overlap that interval and use the same world coordinate system. The semantic validator runs after conversion and checks these relationships in the generated NCore sequence.

### Map the source data to NCore

The companion converter in the next section supports the seven-video and three-table layout shown above. When the files follow this schema, the workflow can continue directly with **Run the companion converter**.

Unsupported source formats require a customized copy of the public converter template that reads the source files and writes the data to NCore.

`export` `CONVERTER_DIR=` `"$WORK_DIR/cosmos-clipgt-converter"` `cp` `-R ` `"$NUREC_SKILLS_REPO/skills/ncore/ncore_template"` `"$CONVERTER_DIR"` |

The template is a code skeleton, not a general-purpose converter. Its source reader must map equivalent information into these NCore components:

Source data | NCore V4 |
|---|---|
| Encoded camera images and per-frame exposure intervals | One `CameraSensorComponent` per logical camera |
| Camera lens models and intrinsics | `IntrinsicsComponent` |
| Camera-to-rig extrinsics | `PosesComponent` : `T_sensor_rig` |
| Metric egomotion | `PosesComponent` : `T_rig_world` |
| Optional global reference | `PosesComponent` : `T_world_world_global` |
| Ego masks | `MasksComponent` |
| Object observations and tracks | `CuboidsComponent` |


*Table 2. Source-data mappings to NCore V4 components*Follow the public NCore coordinate conventions:

- Rig:
`+X`

forward,`+Y`

left,`+Z`

up - Camera:
`+X`

right,`+Y`

down,`+Z`

forward - Timestamps: integer microseconds
- Distances: meters; poses: valid SE(3) transforms

Keep pose computation in float64. Rebase the local `world` frame so that the first rig pose is identity. For synchronized constant-frame-rate video without recorded frame timestamps, the nominal timestamp for frame `i` is:

`frame_timestamp_us = anchor_timestamp_us + i * 1,000,000 / fps` |

Use recorded exposure timestamps when available. The nominal formula assumes that the MP4 streams are synchronized. The converter writes the sequence with the NCore `separate-sensors` profile. This profile creates one camera-component archive per converted camera and a shared archive for poses, intrinsics, masks, and cuboids. The converter preserves each camera’s actual resolution and color interpretation.

### Run the companion converter

When the source-specific converter is distributed with the tutorial repository, run it as follows:

`export` `COSMOS_CONVERTER=` `"$TUTORIAL_REPO/tools/cosmos_ncore/build_cosmos_ncore_v4.py"` `test` `-f ` `"$COSMOS_CONVERTER"` `env` `-u PYTHONPATH ` `"$NCORE_PYTHON"` `"$COSMOS_CONVERTER"` `\` ` ` `--root ` `"$INPUT_ROOT"` `\` ` ` `--anchor-us ` `"$ANCHOR_TIMESTAMP_US"` `\` ` ` `--sequence-` `id` `"$SEQUENCE_ID"` `\` ` ` `--fps ` `"$FPS"` `\` ` ` `--store-` `type` `itar` |

### Validate the NCore sequence

Set the generated paths according to the converter’s output contract:

`export` `NCORE_DIR=` `"$INPUT_ROOT/ncore/$SEQUENCE_ID"` `export` `NCORE_MANIFEST=` `"$NCORE_DIR/$SEQUENCE_ID.json"` `export` `NCORE_VALIDATOR=` `"$TUTORIAL_REPO/tools/cosmos_ncore/validate_cosmos_ncore_v4.py"` `test` `-s ` `"$NCORE_MANIFEST"` `python3 -m json.tool ` `"$NCORE_MANIFEST"` `> ` `/dev/null` |

Run the source-specific validator:

`env -u PYTHONPATH "$NCORE_PYTHON" "$NCORE_VALIDATOR" \` ` ` `--root "$INPUT_ROOT" \` ` ` `--sequence-id "$SEQUENCE_ID"` |

Then inspect the sequence using the public NCore viewer and open http://localhost:8080.

`export` `NCORE_REPO=` `/absolute/path/to/ncore` `export` `NCORE_MANIFEST=` `/absolute/path/to/sequence/` `<sequence-` `id` `>.json` ` ` `(` ` ` `cd` `"$NCORE_REPO"` ` ` `bazel run ` `//tools/ncore_vis` `-- \` ` ` `v4 \` ` ` `--component-group=` `"$NCORE_MANIFEST"` ` ` `)` |

### Expected output

A separate-sensors NCore V4 sequence commonly contains:

`<sequence-id>/` `├── <sequence-id>.json` `├── build_manifest.json` `├── <sequence-id>.ncore4.zarr.itar` `├── <sequence-id>.ncore4-<camera-id>.zarr.itar` `└── ... one camera archive per converted camera` |

The shared `<sequence-id>.ncore4.zarr.itar` archive contains components such as poses, intrinsics, masks, and cuboids. Each `<sequence-id>.ncore4-<camera-id>.zarr.itar` archive contains the frames for one converted camera. The JSON manifest and all referenced archives form one logical sequence; they must remain together.

### Generate NuRec auxiliary data

The converted NCore sequence contains recorded sensor measurements, calibration, poses, and object tracks. It doesn’t yet include the inferred semantic segmentation, depth, and ego masks required for this camera-only reconstruction workflow. The public [skills/nre](https://github.com/NVIDIA/nurec-skills/tree/main/skills/nre) instructions describe this stage, and the [NuRec auxiliary-data documentation](https://docs.nvidia.com/nurec/nurec/nurec-aux-data.html) defines the data products. The public [nre-tools-ga NGC container](https://catalog.ngc.nvidia.com/orgs/nvidia/nre/containers/nre-tools-ga) on NGC provides the inference application.

The workflow uses `NRE_AUX_IMAGE`

to identify auxiliary-data containers and distinguish them from the separate `nre-ga`

training and rendering image. The 26.04 GA image exposes several tools through one entry point, so the workflow explicitly selects the ncore-aux-data subcommand:

`export` `NUREC_AUX_IMAGE=nvcr.io` `/nvidia/nre/nre-tools-ga` `:26.04.00` `python3 ` `"$NUREC_SKILLS_REPO/skills/nre/scripts/validate_setup.py"` `--strict` `docker pull ` `"$NUREC_AUX_IMAGE"` `docker run --` `rm` `--gpus all --shm-size=2g \` ` ` `--` `env` `NGC_API_KEY \` `--volume ` `"$NCORE_DIR:/workdir/dataset"` `\` ` ` `"$NUREC_AUX_IMAGE"` `ncore-aux-data \` ` ` `--dataset-path=` `"/workdir/dataset/$SEQUENCE_ID.json"` `\` ` ` `--output-` `dir` `=` `/workdir/dataset` `\` ` ` `--segmentation-backend=mask2former \` ` ` `--depth-backend=depthanythingv2 \` ` ` `--max-depth-m=80 \` ` ` `--ego-mask \` ` ` `--no-lidar-seg-camvis \` ` ` `--no-seg-logits \` ` ` `--zarr-store-` `type` `=itar \` ` ` `--store-meta \` ` ` `--num-threads=auto` |

The selected options have explicit roles. Table 3 summarizes the output generated by each selected option.

Option | Generated product |
|---|---|
`--segmentation-backend=mask2former` | `<sequence-id>.aux.sseg.zarr.itar` : per-frame semantic class masks |
`--depth-backend=depthanythingv2` | `<sequence-id>.aux.depth.zarr.itar` : metric depth |
`--ego-mask` | `<sequence-id>.aux.egomask.zarr.itar` : per-camera ego-vehicle exclusion masks |
`--store-meta` | `<sequence-id>.aux-meta.json` : resolved auxiliary settings from the pinned image |
`--no-lidar-seg-camvis` | Disables LiDAR segmentation because the workflow does not include LiDAR data |


*Table 3.**Auxiliary-data options and generated products*Omitting `--camera-id`

processes every camera declared in `NCORE_SEQUENCE_JSON. Selecting specific cameras requires one`

`--camera-id=<logical-camera-id>`

argument for each, using the logical camera IDs from the manifest.

After auxiliary data generation, the reconstruction input directory contains the following structure:

`<sequence-id>/` `├── <sequence-id>.json` `├── build_manifest.json` `├── <sequence-id>.ncore4.zarr.itar` `├── <sequence-id>.ncore4-<camera-id>.zarr.itar` `└── ... one camera archive per converted camera` `├── <sequence-id>.aux.sseg.zarr.itar` `├── <sequence-id>.aux.depth.zarr.itar` `├── <sequence-id>.aux.egomask.zarr.itar` `└── <sequence-id>.aux-meta.json` |

## Get started

Use the following resources to begin adapting a reconstructed scene to a target carline.

- Download a USDZ scene and the included sample target rig from the
[Physical AI NuRec Dataset](https://huggingface.co/datasets/nvidia/PhysicalAI-Autonomous-Vehicles-NuRec). - Render the scene through the sample rig, replace the rig JSON with the target carline configuration, and render the scene again.
- Review the
[NuRec documentation](https://docs.nvidia.com/nurec/)for setup requirements, supported hardware, validation, and rendering instructions. - To reconstruct recorded drives, follow
[Reconstruct an AV Scene](https://docs.nvidia.com/nurec/nurec/model.html)and the NCore conversion and auxiliary-data guidance in[NVIDIA/nurec-skills](https://github.com/NVIDIA/nurec-skills). - Use
[NVIDIA Harmonizer](https://github.com/NVIDIA/harmonizer)for temporally consistent sequence postprocessing.

The public software, containers, datasets, and model artifacts require the applicable NVIDIA NGC or Hugging Face accounts and acceptance of their licenses. The NuRec runtime is available in the [nre-ga container on NGC](https://catalog.ngc.nvidia.com/orgs/nvidia/nre/containers/nre-ga).

## Start the discussion at forums.developer.nvidia.com
