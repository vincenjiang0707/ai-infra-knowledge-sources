# [Issue #3749] feat: native Google Cloud Storage (GCS) connector (parity with S3, no NIXL dependency)

source: https://github.com/LMCache/LMCache/issues/3749
state: closed | updated: 2026-09-27T01:56:50Z
labels: stale

## 正文

## Summary

There is no native Google Cloud Storage (GCS) connector in LMCache. AWS has a
first-class `s3_connector.py` (direct `awscrt` SDK), and a native Azure connector
is being added via #3575 / #3686, but GCS users currently have no path to use
LMCache's remote KV cache storage.

I'd like to add a native `GCSConnector` to bring GCS to parity with S3 (and
Azure) — and I'm volunteering to implement it.

## Current State

- **Native S3 exists:** `lmcache/v1/storage_backend/connector/s3_connector.py`
  (+ `s3_adapter.py`), direct `awscrt` SDK, no extra transfer layer.
- **Azure native (in progress):** `azure_connector.py` + `azure_adapter.py`
  being added via #3686, direct `azure-storage-blob` SDK.
- **No GCS support anywhere:** GCS is not a valid NIXL backend
  (`_VALID_NIXL_BACKENDS` = `GDS`, `GDS_MT`, `POSIX`, `HF3FS`, `OBJ`,
  `AZURE_BLOB` — no `GCS` entry). There is no `gcs_connector.py` /
  `gcs_adapter.py` in `lmcache/v1/storage_backend/connector/`.

## Proposed Implementation

Following the exact same pattern as `s3_connector.py` + `s3_adapter.py`:

| File | Purpose |
|---|---|
| `gcs_connector.py` | `GCSConnector(RemoteConnector)` — async get/put/exists/list/close via `google-cloud-storage` SDK |
| `gcs_adapter.py` | `GCSConnectorAdapter` — registers the `gs://` URL scheme (auto-discovered, no manual wiring) |

**Auth support:** Application Default Credentials (ADC), service account JSON
key file, and explicit credentials — matching how GCS SDK works natively.

**Optional dependency:** `google-cloud-storage` lazily imported (same approach
as Azure PR #3686), so it stays optional and doesn't break installs that don't
need GCS.

## Benefits

- **No NIXL dependency** — works out of the box for GCS users without
  installing/configuring NIXL
- **GPU-capable** — native connectors are not bound by NIXL's CPU-only
  constraint (which applies to e.g. `AZURE_BLOB`); future GPU-direct GCS
  transfers become possible without a NIXL dependency
- **Parity with S3 and Azure** — all three major cloud object stores covered
  natively
- **Familiar pattern** — follows existing `s3_connector.py` architecture
  exactly, minimal review overhead

## References

- #2141 — original Azure Blob request (context)
- #3160 — merged PR that added `AZURE_BLOB` to NIXL (implementation context)
- #3575 — Azure native connector feature request (same gap, different cloud)
- #3686 — Azure native connector PR (implementation pattern to follow)

---

I would like to work on this if maintainers are open to it. Happy to submit a PR once this is confirmed. 🙂

cc @maobaolong @sammshen @chunxiaozheng (storage backends)

## 评论 (4)

### maobaolong · 2026-06-24

@ChiragB254 Thank you so much for your willingness to contribute to the GCS backend storage.

However, I would prefer that you prioritize contributing to the GCS Adapter first. Specifically, we want to prioritize support for the MP Mode in LMCache. 

LMCache will be focusing on MP Mode moving forward. Consequently, our maintenance efforts for the previous In-Process Mode will gradually decrease.

### ChiragB254 · 2026-06-28

Hi @maobaolong 

Thank you so much for your response. I'll definitely contribute to GCS Adapter


### github-actions[bot] · 2026-08-27

This issue has been automatically marked as stale because it has not had activity within 60 days. It will be automatically closed if no further activity occurs within 30 days.

### github-actions[bot] · 2026-09-27

This issue has been automatically closed due to inactivity. Please feel free to reopen if you feel it is still relevant!
