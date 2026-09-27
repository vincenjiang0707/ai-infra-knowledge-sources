# [Issue #199] Data Corruption on dcgm_fi_dev_gpu_util Metric

source: https://github.com/NVIDIA/DCGM/issues/199
state: open | updated: 2025-08-26T07:13:21Z
labels: 

## 正文

Hi all,

Currently using dcgm_fi_dev_gpu_util to monitor GPU utilization but running into an issue where it will occasionally spit out a data point that isn't between 0 and 100. The highest observed value was 4294967295 (max supported by UINT32 which might be a hint), but most often it's in range of 1k to 200k. This appears to happen both in situations where there is load on the GPUs and also in situations where the GPUs are sitting at 0% before and after the erroneous data point. Has anyone else encountered problems with this metric?

I've seen it suggested elsewhere that there's a newer DCGM_FI_PROF_GR_ENGINE_ACTIVE which might replace it, but I don't know whether the root cause here is the metric itself or something in the collection code. Anyone know whether collecting the 'prof' metric would incur a greater performance penalty than the 'dev' metric?

Thanks!

(cross post of https://github.com/NVIDIA/go-dcgm/issues/75 since I'm not sure whether this a problem with the metric itself of the go wrapper being used to extract it)

## 评论 (5)

### TortoiseHam · 2024-11-22

Confirmed that this problem is with dcgmi directly, and not with the go-wrapper translation layer. To reproduce you can run the following script as a background job for a few days:

```
#!/bin/bash

output_file="gpu_high_values.log"

echo "Monitoring GPU utilization..."
echo "Logging anomolies to $output_file"
echo "Monitoring started at $(date)" >> "$output_file"

while true; do
	output=$(dcgmi dmon -e 203 --count 1)

	# Process each line
	echo "$output" | while read -r line; do
		# Extract GPU ID and Value
		if [[ $line =~ GPU[[:space:]]+[0-9]+[[:space:]]+([0-9]+) ]]; then
			value="${BASH_REMATCH[1]}"  # extract numeric value
			if (( value > 100 )); then
				echo "Value > 100 detected at $(date):" >> "$output_file"
				echo "$line" >> "$output_file"
				echo "---" >> "$output_file"
				echo "Value > 100 detected! Logged the output."
				exit 0  # break the loops
			fi
		fi
	done
done
```



### nikkon-dev · 2024-11-27

@TortoiseHam,

Could you check if the values you get are derivative of the [DCGM_INT32_BLANK](https://github.com/NVIDIA/DCGM/blob/b0ec3c624ea21e688b0d93cf9b214ae0eeb6fe52/dcgmlib/dcgm_structs.h#L50)? `DCGM_INT32_NOT_FOUND`, `DCGM_INT32_NOT_SUPPORTED`, etc

### TortoiseHam · 2024-11-27

@nikkon-dev , interesting thought but it seems like the values are more diverse than that. In the past 14 days I'm seeing:

```
345
1980
70281
75902
116170
200000
249389
625512
632707
637317
637805
662389
667418
4294967295
```

The only one that would match something from the list would be `DCGM_INT64_BLANK`

### lethee · 2025-08-26

I have same case.

I'm collecting GPU metric from dcgm-exporter to datadog via datadog-agent with kubernetes environment.

dcgm.gpu_utilization (DCGM_FI_DEV_GPU_UTIL)

Some values like this (metric values greater than 100):
```
$ python check-gpu-util-from-datadog.py

device:nvidia2,host:host124  2025-08-26T14:45:06+09:00  200
device:nvidia2,host:host124  2025-08-26T14:45:20+09:00  200

device:nvidia5,host:host166  2025-08-26T13:48:36+09:00  201635040
device:nvidia5,host:host166  2025-08-26T13:48:52+09:00  201635040

device:nvidia3,host:host039  2025-08-26T11:31:30+09:00  4228166880
device:nvidia3,host:host039  2025-08-26T11:31:46+09:00  4228166880
```

### lethee · 2025-08-26

This related to https://github.com/NVIDIA/dcgm-exporter/issues/418
