source: https://docs.vllm.ai/en/latest/contributing/ci/nightly_builds/
lastmod: 2026-09-24

# Nightly Builds of vLLM Wheels[¶](https://docs.vllm.ai#nightly-builds-of-vllm-wheels)

vLLM maintains a per-commit wheel repository (commonly referred to as "nightly") at `https://wheels.vllm.ai`

that provides pre-built wheels for every commit on the `main`

branch since `v0.5.3`

. This document explains how the nightly wheel index mechanism works.

## Build and Upload Process on CI[¶](https://docs.vllm.ai#build-and-upload-process-on-ci)

### Wheel Building[¶](https://docs.vllm.ai#wheel-building)

Wheels are built in the `Release`

pipeline (`.buildkite/release-pipeline.yaml`

) after a PR is merged into the main branch. Regular builds produce the CUDA 13.0 wheels for x86_64 and aarch64. Additional wheel variants and ROCm builds can be unblocked on demand and run automatically when `NIGHTLY=1`

:

**Backend variants**:`cpu`

and`cuXXX`

(e.g.,`cu129`

,`cu130`

).**Architecture variants**:`x86_64`

and`aarch64`

.

Each build step:

- Builds the wheel in a Docker container.
- Renames the wheel filename to use the correct manylinux tag (currently
`manylinux_2_28`

) for PEP 600 compliance. - Uploads the wheel to S3 bucket
`vllm-wheels`

under`/{commit_hash}/`

.

### Index Generation[¶](https://docs.vllm.ai#index-generation)

After uploading each wheel, the `.buildkite/scripts/upload-wheels.sh`

script:

**Lists all existing wheels**in the commit directory from S3**Generates indices**using`.buildkite/scripts/generate-nightly-index.py`

:- Parses wheel filenames to extract metadata (version, variant, platform tags).
- Creates HTML index files (
`index.html`

) for PyPI compatibility. - Generates machine-readable
`metadata.json`

files.

**Uploads indices**to multiple locations (overriding existing ones):`/{commit_hash}/`

- Always uploaded for commit-specific access.`/nightly/`

- Only for commits on`main`

branch (not PRs).`/{version}/`

- Only for release wheels (no`dev`

in its version).


Handling Concurrent Builds

The index generation script can handle multiple variants being built concurrently by always listing all wheels in the commit directory before generating indices, avoiding race conditions.

## Directory Structure[¶](https://docs.vllm.ai#directory-structure)

The S3 bucket structure follows this pattern:

s3://vllm-wheels/
├── {commit_hash}/ # Commit-specific wheels and indices
│ ├── vllm-*.whl # All wheel files
│ ├── index.html # Project list (default variant)
│ ├── vllm/
│ │ ├── index.html # Package index (default variant)
│ │ └── metadata.json # Metadata (default variant)
│ ├── cu129/ # Variant subdirectory
│ │ ├── index.html # Project list (cu129 variant)
│ │ └── vllm/
│ │ ├── index.html # Package index (cu129 variant)
│ │ └── metadata.json # Metadata (cu129 variant)
│ ├── cu130/ # Variant subdirectory
│ ├── cpu/ # Variant subdirectory
│ └── .../ # More variant subdirectories
├── nightly/ # Latest main branch wheels (mirror of latest commit)
└── {version}/ # Release version indices (e.g., 0.11.2)


All built wheels are stored in `/{commit_hash}/`

, while different indices are generated and reference them. This avoids duplication of wheel files.

For example, you can specify the following URLs to use different indices:

`https://wheels.vllm.ai/nightly/cu130`

for the latest main branch wheels built with CUDA 13.0.`https://wheels.vllm.ai/{commit_hash}`

for wheels built at a specific commit (default variant).`https://wheels.vllm.ai/0.12.0/cpu`

for 0.12.0 release wheels built for CPU variant.

Please note that not all variants are present on every commit. The available variants are subject to change over time, e.g., changing cu130 to cu131.

### Variant Organization[¶](https://docs.vllm.ai#variant-organization)

Indices are organized by variant:

**Default variant**: Wheels without variant suffix (i.e., built with the current`VLLM_MAIN_CUDA_VERSION`

) are placed in the root.**Variant subdirectories**: Wheels with variant suffixes (e.g.,`+cu130`

,`.cpu`

) are organized in subdirectories.**Alias to default**: The default variant can have an alias (e.g.,`cu129`

for now) for consistency and convenience.

The variant is extracted from the wheel filename (as described in the [file name convention](https://packaging.python.org/en/latest/specifications/binary-distribution-format/#file-name-convention)):

- The variant is encoded in the local version identifier (e.g.
`+cu129`

or`dev<N>+g<hash>.cu130`

). - Examples:
`vllm-0.11.2.dev278+gdbc3d9991-cp38-abi3-manylinux1_x86_64.whl`

→ default variant`vllm-0.10.2rc2+cu129-cp38-abi3-manylinux2014_aarch64.whl`

→`cu129`

variant`vllm-0.11.1rc8.dev14+gaa384b3c0.cu130-cp38-abi3-manylinux1_x86_64.whl`

→`cu130`

variant


## Index Generation Details[¶](https://docs.vllm.ai#index-generation-details)

The `generate-nightly-index.py`

script performs the following:

**Parses wheel filenames**using regex to extract:- Package name
- Version (with variant extracted)
- Python tag, ABI tag, platform tag
- Build tag (if present)

**Groups wheels by variant**, then by package name:- Currently only
`vllm`

is built, but the structure supports multiple packages in the future.

- Currently only
**Generates HTML indices**(compliant with the[Simple repository API](https://packaging.python.org/en/latest/specifications/simple-repository-api/#simple-repository-api)):- Top-level
`index.html`

: Lists all packages and variant subdirectories - Package-level
`index.html`

: Lists all wheel files for that package - Uses relative paths to wheel files for portability

- Top-level
**Generates metadata.json**:- Machine-readable JSON containing all wheel metadata
- Includes
`path`

field with URL-encoded relative path to wheel file - Used by
`setup.py`

to locate compatible pre-compiled wheels during Python-only builds


### Special Handling for AWS Services[¶](https://docs.vllm.ai#special-handling-for-aws-services)

The wheels and indices are directly stored on AWS S3, and we use AWS CloudFront as a CDN in front of the S3 bucket.

Since S3 does not provide proper directory listing, to support PyPI-compatible simple repository API behavior, we deploy a CloudFront Function that:

- redirects any URL that does not end with
`/`

and does not look like a file (i.e., does not contain a dot`.`

in the last path segment) to the same URL with a trailing`/`

- appends
`/index.html`

to any URL that ends with`/`


For example, the following requests would be handled as:

`/nightly`

->`/nightly/index.html`

`/nightly/cu130/`

->`/nightly/cu130/index.html`

`/nightly/index.html`

or`/nightly/vllm.whl`

-> unchanged

AWS S3 Filename Escaping

S3 will automatically escape filenames upon upload according to its [naming rule](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html). The direct impact on vllm is that `+`

in filenames will be converted to `%2B`

. We take special care in the index generation script to escape filenames properly when generating the HTML indices and JSON metadata, to ensure the URLs are correct and can be directly used.

## Usage of precompiled wheels in `setup.py`

[¶](https://docs.vllm.ai#precompiled-wheels-usage)

When installing vLLM with `VLLM_USE_PRECOMPILED=1`

, the `setup.py`

script:

**Determines wheel location**via`precompiled_wheel_utils.determine_wheel_url()`

:- Env var
`VLLM_PRECOMPILED_WHEEL_LOCATION`

(user-specified URL/path) always takes precedence and skips all other steps. - For CUDA, uses
`VLLM_PRECOMPILED_WHEEL_VARIANT`

when specified. Otherwise, an explicitly set`VLLM_MAIN_CUDA_VERSION`

selects the variant; if unset, the CUDA version is detected from PyTorch or nvidia-smi, with the default`VLLM_MAIN_CUDA_VERSION`

used if detection fails. - Determines the
*base commit*(explained later) of this branch (can be overridden with env var`VLLM_PRECOMPILED_WHEEL_COMMIT`

).

- Env var
**For CUDA, fetches metadata**for the selected variant from`https://wheels.vllm.ai/{commit}/{variant}/vllm/metadata.json`

.**Selects compatible wheel**based on:- Package name (
`vllm`

) - Platform tag (architecture match)

- Package name (
**Downloads and extracts**precompiled artifacts from the wheel:- Native extension modules (
`.so`

files) - The
`vllm-rs`

Rust frontend binary - Flash Attention Python modules and Triton/FlashMLA Python files

- Native extension modules (
**Patches package_data**to include extracted files in the installation

What is the base commit?

The base commit is determined by finding the merge-base between the current branch and upstream `main`

, ensuring compatibility between source code and precompiled binaries.

*Note: it's users' responsibility to ensure there is no native code (e.g., C++ or CUDA) changes before using precompiled wheels.*

## Implementation Files[¶](https://docs.vllm.ai#implementation-files)

Key files involved in the nightly wheel mechanism:

: CI pipeline that builds wheels`.buildkite/release-pipeline.yaml`

: Script that uploads wheels and generates indices`.buildkite/scripts/upload-wheels.sh`

: Python script that generates PyPI-compatible indices`.buildkite/scripts/generate-nightly-index.py`

: Contains`setup.py`

`precompiled_wheel_utils`

class for fetching and using precompiled wheels