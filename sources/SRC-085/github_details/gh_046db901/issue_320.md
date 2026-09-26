# [Issue #320] [Question]Why do hidden states extracted from numerical data typically lead to suboptimal performance?

source: https://github.com/SafeAILab/EAGLE/issues/320
state: closed | updated: 2026-01-27T12:30:25Z
labels: 

## 正文

First, I'd like to extend my sincere thanks for sharing this excellent algorithm. While extracting hidden states from data using this model, I have observed a statistical trend: the hidden states generated for numerical tokens consistently show significantly lower accuracy in downstream tasks compared to those for textual tokens. I was wondering if you could shed some light on the potential reasons behind this phenomenon.


Below are the hidden states I extracted from proprietary autonomous driving dataset with Qwen2.5vl-3B-SFT model(ourself)：
```
Reading cache: /mnt/data_0.ckpt ...
Target ID  | Rank  | Prob       | Top-3 Predictions
------------------------------------------------------------
assistant  | 55602 | -29.3750 | ['\n', '<|im_end|>', '<|im_start|>'] ❌

          | 14    | -7.2500 | ['|{\n', '>{"', '>{\n'] ❌
{'         | 0     | -0.0000 | ["{'", '{"', '{}'] ⭐
objects    | 0     | -0.0000 | ['objects', 'hum', 'object'] ⭐
':[        | 0     | -0.0000 | ["':[", "':{'", '":[{"'] ⭐
{'         | 0     | -0.0000 | ["{'", " {'", "({'"] ⭐
object     | 0     | -0.0000 | ['object', 'category', ' object'] ⭐
_id        | 0     | -0.0000 | ['_id', 'ID', 'id'] ⭐
':         | 0     | -0.0000 | ["':", "':'", "':["] ⭐
1          | 0     | -0.0004 | ['1', '2', '3'] ⭐
,'         | 0     | -0.0000 | [",'", ',', ',"'] ⭐
category   | 0     | -0.0000 | ['category', ' category', '_category'] ⭐
':'        | 0     | -0.0000 | ["':'", '\':"', "':"] ⭐
bag        | 1     | -1.0547 | ['cloth', 'bag', 'shirt'] ❌
','        | 0     | -0.0000 | ["','", "','.", " ','"] ⭐
bbox       | 0     | -0.0000 | ['bbox', ' bbox', 'box'] ⭐
':[        | 0     | -0.0000 | ["':[", "':", ".':"] ⭐
3          | 3     | -7.8125 | ['5', '4', '6'] ❌
7          | 3     | -2.3438 | ['9', '6', ','] ❌
7          | 3     | -2.2656 | ['8', '0', '4'] ❌
2          | 0     | -0.9609 | ['2', '3', '1'] ⭐
4          | 5     | -2.9219 | ['8', '5', '7'] ❌
5          | 9     | -2.5312 | ['7', '8', '9'] ❌
4          | 2     | -1.7344 | ['5', '6', '4'] ❌
5          | 5     | -3.0000 | ['3', '2', '0'] ❌
6          | 5     | -2.3281 | ['1', '0', '2'] ❌
3          | 0     | -0.5508 | ['3', '2', '4'] ⭐
7          | 6     | -2.5000 | ['2', '0', '1'] ❌
1          | 8     | -2.6094 | ['8', '9', '6'] ❌
2          | 0     | -0.0058 | ['2', '3', '1'] ⭐
4          | 2     | -2.3750 | ['5', '6', '4'] ❌
4          | 2     | -2.5469 | ['3', '2', '4'] ❌
2          | 2     | -2.1406 | ['0', '1', '2'] ❌
2          | 2     | -2.5938 | ['4', '3', '2'] ❌
0          | 2     | -2.6719 | ['9', '8', '0'] ❌
4          | 3     | -2.2656 | ['1', '2', '3'] ❌
5          | 1     | -1.3750 | ['7', '5', '6'] ❌
0          | 2     | -3.3750 | ['9', '8', '0'] ❌
4          | 0     | -2.1250 | ['4', '0', '1'] ⭐
2          | 0     | -0.2637 | ['2', '3', '4'] ⭐
5          | 4     | -2.2031 | ['7', '8', '6'] ❌
9          | 4     | -2.2500 | ['8', '0', '2'] ❌
3          | 0     | -0.0008 | ['3', '4', '5'] ⭐
3          | 3     | -4.0000 | ['5', '6', '4'] ❌
0          | 9     | -4.2188 | ['7', '6', '8'] ❌
9          | 6     | -2.2969 | ['8', '0', '2'] ❌
2          | 0     | -0.8125 | ['2', '1', '3'] ⭐
8          | 8     | -3.0469 | ['5', '0', '4'] ❌
3          | 8     | -2.5000 | ['4', '7', '0'] ❌
4          | 1     | -1.6484 | ['3', '4', '5'] ❌
0          | 0     | -1.6406 | ['0', '1', '2'] ⭐
7          | 6     | -2.3906 | ['0', '1', '2'] ❌
3          | 0     | -0.1533 | ['3', '4', '5'] ⭐
8          | 4     | -2.2656 | ['7', '5', '6'] ❌
1          | 1     | -2.1094 | ['0', '1', '2'] ❌

==================================================
Numerical tokens acc: 39.58%

==================================================

========================= Report =========================
Effective Token len: 144
----------------------------------------------------------------
Top-1 Accuracy: 75.69%
Top-5 Accuracy: 90.97%
Cross-Entropy Loss: 0.9219
Perplexity (PPL): 2.5156
KL Divergence: 0.9219

========================= VS =========================
--------------------(Ground Truth) --------------------
assistant
{'objects':[{'object_id':1,'category':'bag','bbox':[377,245,456,371],'relation':{'human_id':'none','position':'middle_left','storage_id':'none'}},{'object_id':2,'category':'cloth','bbox':[442,204,504,259],'relation':{'human_id':'none','position':'none','storage_id':'none'}},{'object_id':3,'category':'cloth','bbox':[309,283,407,381],'relation':{'human_id':'none','position':'middle_left','storage_id':'none'}}]}


--------------------  (From Hidden States) ---------------

|{
{'objects':[{'object_id':1,'category':'cloth','bbox':[598,287,531,328],'relation':{'human_id':'none','position':'middle_left','storage_id':'none'}},{'object_id':2,'category':'cloth','bbox':[530,491,794,278],'relation':{'human_id':'none','position':'middle','storage_id':'none'}},{'object_id':3,'category':'cloth','bbox':[578,254,300,370],'relation':{'human_id':'none','position':'none_left','storage_id':'none'}]}

================================================================

```

Below are the hidden states I extracted from **sharegpt4o** dataset with Qwen2.5vl-3B-SFT model(ourself)：
```
Reading cache: /mnt/xxxx/data_xxxx.ckpt ...
Target ID  | Rank  | Prob       | Top-3 Predictions
------------------------------------------------------------
assistant  | 31398 | -15.6875 | ['高速', '旅客', '一趟'] ❌

          | 14    | -9.8750 | [':The', ':', ':A'] ❌
The        | 0     | -0.0913 | ['The', 'This', '**'] ⭐
 image     | 0     | -0.0112 | [' image', ' provided', ' given'] ⭐
 depicts   | 0     | -0.2754 | [' depicts', ' shows', ' displays'] ⭐
 a         | 0     | -0.1162 | [' a', ' an', ' the'] ⭐
 train     | 0     | -0.5312 | [' train', ' modern', ' railway'] ⭐
 station   | 0     | -0.0757 | [' station', ' platform', ' at'] ⭐
 platform  | 0     | -0.4316 | [' platform', ' with', ','] ⭐
 with      | 0     | -0.9414 | [' with', ',', '.'] ⭐
 a         | 0     | -0.1982 | [' a', ' an', ' several'] ⭐
 modern    | 0     | -1.4922 | [' modern', ' train', ' high'] ⭐
 passenger | 0     | -1.3516 | [' passenger', ',', ' high'] ⭐
 train     | 0     | -0.0073 | [' train', ' commuter', ' rail'] ⭐
 stationed | 0     | -1.0703 | [' stationed', ' parked', '.'] ⭐
 on        | 0     | -0.9609 | [' on', ' at', ' along'] ⭐
 the       | 0     | -0.2236 | [' the', ' a', ' an'] ⭐
 tracks    | 0     | -0.1865 | [' tracks', ' track', ' right'] ⭐
.          | 0     | -0.0796 | ['.', ' directly', ' beneath'] ⭐
 The       | 0     | -0.2832 | [' The', ' Here', ' This'] ⭐
1          | 0     | -0.0069 | ['1', '2', '0'] ⭐

========================= Report =========================
Effective Token len: 404
----------------------------------------------------------------
Top-1 Accuracy: 97.77%
Top-5 Accuracy: 99.50%
Cross-Entropy Loss: 0.6602
Perplexity (PPL): 1.9375
KL Divergence: 0.6602

========================= VS =========================
-------------------- (Ground Truth) --------------------
assistant
The image depicts a train station platform with a modern passenger train stationed on the tracks. The train is a long, sleek, and streamlined passenger train, painted in a combination of silver, blue, and white colors. The front of the train features the logo of SNCF, the French national railway company, which is prominently displayed in blue and white. The train is positioned on a set of tracks that are elevated above the platform, indicating that this is likely an underground or elevated station.

The platform itself is clean and well-maintained, with a smooth, flat surface. The platform is relatively empty, with no visible passengers or staff. The area around the platform appears to be well-lit, with overhead lighting fixtures providing ample illumination. The station has a modern design, with a concrete structure and metal railings along the edge of the platform.

On the left side of the image, there is a blue informational booth or kiosk. This booth is likely used for ticketing, information, or announcements. The booth has a digital display screen on the top, which is currently not showing any information. The booth is also equipped with a sign that reads "Voie 1," indicating the specific platform or track number.

The background shows part of the station's interior, including a concrete structure with a walkway or overpass. This walkway appears to be used for passengers to move between platforms or to access different areas of the station. The overall atmosphere of the station is clean, organized, and modern, reflecting a well-maintained public transportation facility.

In summary, the image shows a modern train station with a sleek passenger train stationed on elevated tracks. The platform is clean and well-lit, with a blue informational booth on the left side. The station has a modern design with concrete structures and metal railings, and the background includes a walkway or overpass. The train is painted in silver, blue, and white colors, and the logo of SNCF is prominently displayed.


--------------------  (From Hidden States) ---------------
高速:TheThe image depicts a train station platform with a modern passenger train stationed on the tracks. The train is a long, sleek, and streamlined passenger train, painted in a combination of silver, blue, and white colors. The front of the train features the logo of SNCF, the French national railway company, which is prominently displayed in blue and white. The train is a on a set of tracks that are elevated above the platform, indicating that this is likely an underground or elevated station.

The platform itself is clean and well-maintained, with a smooth, flat surface. The platform is relatively empty, with no visible passengers or staff. The lighting around the platform appears to be well-lit, with overhead lighting fixtures providing ample illumination. The station has a modern design, with a concrete structure and metal railings along the edge of the platform.

On the left side of the image, there is a blue informational booth or kiosk. This booth is likely used for ticketing, information, or announcements. The booth has a digital display screen on the top, which is currently not showing any information. There booth is also equipped with a sign that reads "Voie 1," indicating the specific platform or track number.

The background shows part of the station's interior, including a concrete structure and a railingway or overpass. This walkway appears to be used for passengers to move between platforms or to access different areas of the station. The ceiling atmosphere of the station is clean, organized, and modern, reflecting a well-maintained public transportation facility.

In summary, the image shows a modern train station with a sleek passenger train stationed on elevated tracks. The platform is clean and well-lit, with a blue informational booth on the left side. The station has a modern design with concrete structures and metal railings, and the overall includes a walkway or overpass. The train is painted in silver, blue, and white colors, and the logo of SNCF is prominently displayed.

================================================================

```

We sincerely appreciate anyone valuable feedback and will actively incorporate any constructive suggestions！



## 评论 (2)

### hongyanz · 2026-01-10

I think it depends on the training dataset of the EAGLE head: ShareGPT and UltraChat do not contain many math data.

### 330205812 · 2026-01-12

> I think it depends on the training dataset of the EAGLE head: ShareGPT and UltraChat do not contain many math data.

thx
