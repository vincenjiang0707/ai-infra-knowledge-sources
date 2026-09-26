source: https://github.com/vllm-project/guidellm/milestones?state=closed

# Milestones

## List view

- No due date•1/1 issues closed
- No due date•3/3 issues closed
- No due date•8/8 issues closed
- No due date•1/1 issues closed
New CLI & UI, initial eval support, etc.

Due by June 3, 2026•28/28 issues closedBugfixes & minor updates

No due date•3/3 issues closed- No due date•10/10 issues closed
Bugfix update

No due date•5/5 issues closed- Due by December 5, 2025•18/18 issues closed
Multiturn, vLLM-python backend, Responses API, etc.

Due by April 1, 2026•25/25 issues closed- Due by October 2, 2025•51/52 issues closed
- Due by August 20, 2025•10/10 issues closed
This release of GuideLLM focuses on finalizing the CI/CD pipelines for full automation, expanding documentation for easier access, enhancing user experience through a web-based report UI, and adding backend support for benchmarking across different hardware configurations. ## Key Features - CI/CD Finalization: Finalize and expand GitHub Actions CI/CD pipelines to enable automated builds, releases, testing, and quality assurance. - Documentation Expansion: Expand the documentation and host it on a dedicated webpage, covering CLI, examples, and architecture for easy discovery. - GuideLLM HTML Report UI: Include an HTML report UI for easier visualization and consumption of benchmark results. - vLLM Python Backend Integration: Integrate the vLLM backend for direct benchmarking, including system hardware reporting. - Standard Dataset Profiles: Standardized Dataset profiles make it easy to run inference perforamnce benchmarks for your expected token input/output profiles across key LLM use cases. - Transformers/Compressed Tensors Backend Support: Add benchmarking support for transformers and compressed tensors with detailed hardware reporting. - vLLM OpenAI Server Expansion: Expand OpenAI server hardware querying to surface system hardware and model specifications. - CLI Output Format Enhancements: Expand and simplify CLI output format options, with support for CSV and more consistent reporting. - Dataset Analysis Pathways: Enable detailed analysis of one or more datasets within the GuideLLM framework. - Model Analysis Pathways: Add support for analyzing one or more models, including accuracy evaluations and detailed reports. - Accuracy Evaluation Enablement: Add infrastructure for supporting common accuracy eval pathways initially targeting LM Eval harness. - Single loop dataset benchmarks: Add support for looping through a dataset once for a given benchmark. - Benchmark warmup: Add support for warmup runs to be done before counting performance benchmarks. ## Expected Improvements - End-to-End Testing Expansion: Enable and expand end-to-end testing for benchmarking workflows. - Integration Testing: Expand integration tests to ensure seamless performance across various backend and CLI pathways. ## Expected Bug Fixes - https://github.com/neuralmagic/guidellm/issues/34 - https://github.com/neuralmagic/guidellm/issues/38 ## Milestones & Timeline - Development: Sept 01, 2024 - Sept 30, 2024 - QA: Sept 30, 2024 - TBD - Feature Freeze: ~Sept 30, 2024 - Documentation Finalization: ~Sept 30, 2024 - Release: ~Sept 30, 2024 ## Testing Requirements - **Unit Tests:** All newly implemented features must have accompanying unit tests that ensure full coverage. Code coverage should remain at 85% or higher. - **Integration Tests:** Ensure all integrations with vLLM, DeepSparse, and other backends are fully tested, covering edge cases and normal workflows. - **End-to-End (E2E) Tests:** Run complete e2e tests for all CLI workflows, including benchmarks, report generation, dataset/model analysis, and output formats. - **Manual Testing:** QA must conduct manual testing on all core features, including the new HTML report UI and dataset analysis workflows, ensuring usability and functionality. ## Documentation Requirements - Docs site released. - Supporting docs/guides for new features including model analysis, dataset analysis, accuracy evals, output formats, HTML report, CI/CD flows. - Docs expansion with CLI guide, examples guide, architecture documentation, API docs.

Due by March 13, 2025•7/7 issues closed