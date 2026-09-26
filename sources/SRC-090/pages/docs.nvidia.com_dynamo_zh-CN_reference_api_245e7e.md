source: https://docs.nvidia.com/dynamo/zh-CN/reference/api
lastmod: 2026-09-23T23:30:39.914Z

# API Reference

Language-by-language public surface for Dynamo, discovered from the source tree

The API Reference is a machine-generated view of Dynamo’s public surface, kept
honest by static analysis of the source tree. Each module page lists every
class and function, expands into per-symbol signatures and public methods,
and deep-links to the exact file and line on `main`

.

## Coverage

**Python**— the[Python API landing page](https://docs.nvidia.com/dynamo/reference/api/python)indexes every curated module. Class methods and function signatures are pulled directly from the source; there are no hand-maintained tables.**Rust**— see the publishedand the`ai-dynamo`

crates on crates.io[release artifact inventory](https://docs.nvidia.com/dynamo/general/release-artifacts.mdx)for currently shipped crate versions.**Kubernetes**— the[Kubernetes API reference](https://docs.nvidia.com/dynamo/reference/api/kubernetes/full-api-reference)documents the full DynamoGraphDeployment / DynamoComponentDeployment custom-resource surface. Trimmed per-CRD references (DGD, DGDR, DCD) live as siblings under the same section so every deep link resolves.

**These pages are generated** and carry a `do not edit`

marker. Python and Rust
come from docstrings read by [griffe](https://mkdocstrings.github.io/griffe/): edit the source, then rerun
`gen_python_api.py`

or `gen_rust_api.py`

in `docs/fern/scripts/`

. Kubernetes
takes one more hop — `make generate-api-docs`

in `deploy/operator/`

turns the
CRD Go types into `api-reference-k8s.md`

, which `gen_kubernetes_api.py`

then
renders, so editing a Go type and rerunning the renderer alone changes nothing.
The `Generated API References`

pre-merge job runs all three with `--check`

,
scoped to the branch’s own changes on a pull request and strict on `main`

.