# [Issue #2584] speech2text data download script broken

source: https://github.com/mlcommons/inference/issues/2584
state: closed | updated: 2026-06-04T07:33:48Z
labels: 

## 正文

Following the readme in inference/speech2text, this command:
```
bash <(curl -s https://raw.githubusercontent.com/mlcommons/r2-downloader/refs/heads/main/mlc-r2-downloader.sh) -d whisper/dataset https://inference.mlcommons-storage.org/metadata/whisper-dataset.uri
```

Reports:
```
Checking if authentication is required...
Error: Network or connection issue while checking authentication requirements
Please check your network connection and the provided URL, then try again.
```

Seems to be an issue with the headers in the response from https://inference.mlcommons-storage.org/metadata/whisper-dataset.uri


## 评论 (3)

### hanyunfan · 2026-06-03

@anandhu-eng Could you help to take a look?

### anandhu-eng · 2026-06-03

Hi @hanyunfan , the command worked for me. Im attaching the last few lines here:

```
LibriSpeech/dev-all/5849/50873/5849-50873-0016.flac: OK
LibriSpeech/dev-other/5849/50873/5849-50873-0016.flac: OK
LibriSpeech/dev-all/1701/141760/1701-141760-0011.flac: OK
LibriSpeech/dev-other/1701/141760/1701-141760-0011.flac: OK
LibriSpeech/dev-all/174/168635/174-168635-0011.flac: OK
LibriSpeech/dev-clean/174/168635/174-168635-0011.flac: OK
LibriSpeech/dev-all/8288/274150/8288-274150-0008.flac: OK
LibriSpeech/dev-other/8288/274150/8288-274150-0008.flac: OK
LibriSpeech/dev-all/1686/142278/1686-142278-0005.flac: OK
LibriSpeech/dev-other/1686/142278/1686-142278-0005.flac: OK
LibriSpeech/dev-all/251/137823/251-137823-0002.flac: OK
LibriSpeech/dev-clean/251/137823/251-137823-0002.flac: OK
dev-all/8254/84205/8254-84205-0050.wav: OK
LibriSpeech/dev-all/251/137823/251-137823-0023.flac: OK
LibriSpeech/dev-clean/251/137823/251-137823-0023.flac: OK
dev-all/1650/167613/1650-167613-0017.wav: OK
dev-all/6467/56885/6467-56885-0010.wav: OK
LibriSpeech/dev-all/1919/142785/1919-142785-0037.flac: OK
LibriSpeech/dev-clean/1919/142785/1919-142785-0037.flac: OK
dev-all-repack/7641-96670_4.wav: OK
LibriSpeech/dev-all/174/50561/174-50561-0014.flac: OK
LibriSpeech/dev-clean/174/50561/174-50561-0014.flac: OK
dev-all/1272/141231/1272-141231-0030.wav: OK
dev-all/1919/142785/1919-142785-0026.wav: OK
Checksum verification completed successfully!
All files have been downloaded and verified in: whisper/dataset
```

@almayne are you still facing this issue. If yes, are you using any VPN? 

Tagging @BarnacleBob for visibility

### almayne · 2026-06-04

Thanks for taking a look @anandhu-eng. I just tried this again and it seems to have been resolved. Happy to close!
