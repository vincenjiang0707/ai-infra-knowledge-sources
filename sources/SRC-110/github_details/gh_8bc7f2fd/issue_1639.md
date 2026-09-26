# [Issue #1639] UI颜色怎么设置正常白色（light）？

source: https://github.com/modelscope/evalscope/issues/1639
state: closed | updated: 2026-08-27T08:30:12Z
labels: 

## 正文

已经设置 light 了

<img width="1422" height="126" alt="Image" src="https://github.com/user-attachments/assets/ab51a5e8-8548-4daa-b4ca-ea0f192e2783" />


但查看完整html报告时，这个位置是 dark 的

<img width="324" height="110" alt="Image" src="https://github.com/user-attachments/assets/c5628594-ef24-416e-8eba-86a7318b6e4a" />

<img width="1202" height="173" alt="Image" src="https://github.com/user-attachments/assets/27106a5b-689e-419f-83ba-a18c9e0d1493" />

## 评论 (2)

### baigongli · 2026-08-27

颜色不统一
<img width="1602" height="360" alt="Image" src="https://github.com/user-attachments/assets/96c67074-0f6c-4e87-b470-e6646525338a" />

### Yunnglin · 2026-08-27

已在 PR #1646 中修复。完整 HTML report 现在支持 light/dark 主题渲染，并会在打开或刷新时继承 Web UI 当前主题。

需要说明的是：当 report 已在 Web UI 中打开时，切换 Web UI 主题不会让当前 iframe 实时联动；刷新 report 页面后会应用新主题。当前支持的是亮暗主题渲染，不属于 HTML report 内的可交互主题切换。
