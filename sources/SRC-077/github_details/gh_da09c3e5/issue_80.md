# [Issue #80] How to support multiple files with modal

source: https://github.com/gpu-mode/kernelbot/issues/80
state: closed | updated: 2025-01-06T18:40:27Z
labels: 

## 正文

Just got this working now using Modal mounts - cc @alexzhang13 

We could probably get rid of the execs that we have and instead just use the `modal run` with Mounts command moving forward

```bash
~/Dev/discord-cluster-manager/twofile main*
modal-env ❯ modal run file1.py 
✓ Initialized. View run at https://modal.com/apps/msaroufim/main/ap-Ikjs7J7YEvHpeIbW40Z7ZY
✓ Created objects.
├── 🔨 Created mount /Users/marksaroufim/Dev/discord-cluster-manager/twofile/file1.py
├── 🔨 Created mount /Users/marksaroufim/Dev/discord-cluster-manager/twofile
└── 🔨 Created function run_main.
Running main function from file2
🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
Stopping app - local entrypoint completed.
✓ App completed. View run at https://modal.com/apps/msaroufim/main/ap-Ikjs7J7YEvHpeIbW40Z7ZY

~/Dev/discord-cluster-manager/twofile main*
modal-env ❯ 
```

```python
# file1.py
from modal import App, Mount

mount = Mount.from_local_dir(".", remote_path="/root")
app = App("my-app")

@app.function(mounts=[mount])
def run_main():
    from file2 import main
    main()

if __name__ == "__main__":
    app.run()
```

```python
# file2.py
def main():
    print("Running main function from file2")
    print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")

if __name__ == "__main__":
    main()
```

## 评论 (2)

### alexzhang13 · 2024-12-26

Nice! Is it also easy to import functions from file1 into file2? This is the main thing that needs to be doable, with exec's you can merge all files into 1, but it'd be use imports.

### msaroufim · 2024-12-26

Yep this is what this is example is showing, `if __name__ == "__main__":` is a red herring in file2.py

```
~/Dev/discord-cluster-manager/twofile main*
modal-env ❯ cat file2.py 
 1   │ def main():
 2   │     print("Running main function from file2")
 3   │     print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")

~/Dev/discord-cluster-manager/twofile main*
modal-env ❯ modal run file1.py

✓ Initialized. View run at https://modal.com/apps/msaroufim/main/ap-2hS8hjTBztiBaq5jP3RtuY
✓ Created objects.
├── 🔨 Created mount /Users/marksaroufim/Dev/discord-cluster-manager/twofile/file1.py
├── 🔨 Created mount /Users/marksaroufim/Dev/discord-cluster-manager/twofile
└── 🔨 Created function run_main.
Running main function from file2
🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
Stopping app - local entrypoint completed.
✓ App completed. View run at https://modal.com/apps/msaroufim/main/ap-2hS8hjTBztiBaq5jP3RtuY

~/Dev/discord-cluster-manager/twofile main* 8s
modal-env ❯ 
```
