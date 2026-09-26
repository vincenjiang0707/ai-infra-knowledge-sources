# [PR #2] Consolidate repository licensing under CC BY-NC 4.0

source: https://github.com/NVlabs/kda/pull/2
state: closed | updated: 2026-09-10T02:45:09Z
labels: 

## 正文

This updates the repository to use a single CC BY-NC 4.0 license for all content, including source code, repository files, documentation, and prompts. It removes the prior split-license setup so the licensing model is unambiguous from the repo root.

- **License consolidation**
  - Replaced the root `LICENSE` contents with the CC BY-NC 4.0 license text
  - Removed the separate `LICENSE-CC-BY-NC-4.0` file

- **Documentation alignment**
  - Updated `README.md` to state that the entire repository is covered by `LICENSE`
  - Removed references to the previous Apache-2.0 / CC BY-NC split

- **Result**
  - The repository now presents a single licensing source of truth at the root

```md
## License

All source code, repository content, documentation, and prompt content in this repository are licensed under CC BY-NC 4.0. See `LICENSE`.
```

## 评论 (0)

## Review (1)

### Lyken17 · 2026-09-10 · APPROVED

(no text)
