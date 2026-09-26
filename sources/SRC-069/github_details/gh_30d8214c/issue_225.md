# [Issue #225] [BUG] install.sh bug when try to reinstall the deepgemm

source: https://github.com/deepseek-ai/DeepGEMM/issues/225
state: closed | updated: 2025-12-05T09:07:01Z
labels: 

## 正文

if use the same version the .whl will not be updated, need to change the script to
```
pip install dist/*.whl --force-reinstall
```

full script：
```
# Change current directory into project root
original_dir=$(pwd)
script_dir=$(realpath "$(dirname "$0")")
cd "$script_dir"

# Remove old dist file, build files, and install
rm -rf build dist
rm -rf *.egg-info
python setup.py bdist_wheel
pip install dist/*.whl --force-reinstal

# Open users' original directory
cd "$original_dir"
```

## 评论 (1)

### LyricZhao · 2025-12-05

Thanks for the comments, fixed in https://github.com/deepseek-ai/DeepGEMM/commit/9b680f428484625f4f35dc3617f134187c6bcd4a.
