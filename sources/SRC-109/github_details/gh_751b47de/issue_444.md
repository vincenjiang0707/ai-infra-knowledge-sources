# [Issue #444] [BUG] Plot need load config.yaml but not found this file

source: https://github.com/triton-inference-server/perf_analyzer/issues/444
state: open | updated: 2025-10-17T05:50:01Z
labels: 

## 正文

`genai_perf` Plot need load `config.yaml`  but not found this file

## 评论 (1)

### zzz3bbb3 · 2025-10-17

> Plot need load `config.yaml` but not found this file

Solution：
need modify `Profile` class `create_plots` function, modify folder path like this
```python
    def create_plots(self) -> None:
        # TMA-1911: support plots CLI option
        objectives = self._create_objectives_based_on_stimulus()
        log_base = self._create_perf_analyzer_config(objectives).get_artifact_directory()
        plot_dir = log_base / "plots"
        # plot_dir = self._config.output.artifact_directory / "plots"
        PlotConfigParser.create_init_yaml_config(
            filenames=[log_base / self._config.output.profile_export_file],  # single run
            output_dir=plot_dir,
        )
        config_parser = PlotConfigParser(plot_dir / "config.yaml")
        plot_configs = config_parser.generate_configs(self._config)
        plot_manager = PlotManager(plot_configs)
        plot_manager.generate_plots()
```
