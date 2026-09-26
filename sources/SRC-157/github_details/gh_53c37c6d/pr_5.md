# [PR #5] Add Ampere (sm_80/sm_86) extension

source: https://github.com/mit-han-lab/KernelWiki/pull/5
state: open | updated: 2026-08-05T08:07:43Z
labels: 

## 正文

Adds an Ampere layer so the same knowledge base is usable on A100 (sm_80) and GA10x cards (sm_86: RTX 3090/3080, RTX A6000, A40).

Everything is additive. Upstream files are touched only to register the new vocabulary, so future merges stay trivial.

**New pages**

* `wiki/migration/hopper-to-ampere-backport.md`, the entry point: instruction replacement table, capacity re-planning, scheduling paradigm, ncu checklist
* `wiki/hardware/`: `cp-async`, `mma-sync-ampere`, `ampere-memory-model`
* `sources/docs/`: Ampere tuning guide, GA102 whitepaper, PTX ISA for Ampere, CUTLASS SM80 support

**Vocabulary and tooling**

* `data/tags.yaml`: architectures `sm80`, `sm86`; hardware features `cp-async`, `mma-sync`, `l2-persistence`
* `data/aliases.yaml`: alias groups for the same terms
* `scripts/query.py` now also scores `architectures`, `from_arch` and `to_arch`, so `--architecture sm86` and the migration page are actually reachable

**Verification**

`scripts/validate.py` passes on the full tree (2795 files). Snippets compile under `nvcc -arch=sm_86` on a 4x RTX 3090 machine. Facts come from the NVIDIA Ampere tuning guide (CC 8.0/8.6 table), the GA102 whitepaper v2.1, the PTX ISA and CUTLASS.

The Blackwell-first rule is untouched, since it constrains Hopper-only pages, and every new page carries the frontmatter its type requires.

Happy to adjust the naming or split this up if it does not fit the direction you want for the repo.


## 评论 (0)
