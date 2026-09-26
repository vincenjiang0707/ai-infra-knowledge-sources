source: https://docs.mlcommons.org/inference/install/

# Installation[¶](https://docs.mlcommons.org#installation)

We use MLCommons MLC Automation framework to run MLPerf inference benchmarks.

MLC needs `git`

, `python3-pip`

and `python3-venv`

installed on your system. Once the dependencies are installed, do the following

## Activate a Virtual ENV for MLCFlow[¶](https://docs.mlcommons.org#activate-a-virtual-env-for-mlcflow)

This step is not mandatory as MLC can use separate virtual environment for MLPerf inference. But the latest `pip`

install requires this or else will need the `--break-system-packages`

flag while installing `mlc-scripts`

.

```
python3 -m venv mlc
source mlc/bin/activate
```


## Install MLC and pulls any needed repositories[¶](https://docs.mlcommons.org#install-mlc-and-pulls-any-needed-repositories)

```
pip install mlc-scripts
```


```
pip install mlcflow && mlc pull repo --url=mlcommons@mlperf-automations --branch=dev
```


`repo`

is in the format `githubUsername@githubRepo`

or you can give any URL
Now, you are ready to use the `mlcr`

commands to run MLPerf inference as given in the [benchmarks](https://docs.mlcommons.org/) page