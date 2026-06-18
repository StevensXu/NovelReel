<div align="center">

# NovelReel

### 使用 LLM 和视觉生成模型将网络小说转化为电影级视频

一个面向网络小说的开源 AI 短剧制作流程，将长篇小说自动转化为剧本、
角色、分镜、配音和完整视频。

<a href="README.md"><img src="https://img.shields.io/badge/English-0969DA?style=for-the-badge" alt="English"></a>
<a href="README_zh-CN.md"><img src="https://img.shields.io/badge/中文-D73A49?style=for-the-badge" alt="中文"></a>

[项目介绍](#项目介绍) · [工作流程](#工作流程) · [角色展示](#角色展示) · [视频案例](#视频案例)

</div>

## 项目介绍

**NovelReel** 是一个专为网络小说设计的 AI 短剧制作流水线。它可以将小说
转化为完整的 AI 短剧，并保持角色（形象与音色）、道具和场景的一致性。
整个制作过程无需人工介入。

### 核心功能

#### 1. 自动化小说转 AI 短剧

- 自动提取角色、道具和场景，并生成对应的参考图
- 保持跨章节角色、道具和场景的一致性
- 自动编排剧本并生成剧情连续的视频

#### 2. 智能配音

- 为每个角色分配统一的音色
- 校准并保持角色跨镜头的音色一致性


## 工作流程

```mermaid
flowchart LR
    A[网络小说] --> B[故事分析]
    B --> C[影视剧本]
    C --> D[角色与世界观设计]
    D --> E[分镜设计]
    E --> F[图像与视频生成]
    C --> G[配音与音频]
    F --> H[剪辑与字幕]
    G --> H
    H --> I[最终影片]
```

1. 解析小说，提取角色、地点、事件和故事时间线。
2. 将原文改编为场景、对白、旁白和镜头描述。
3. 生成可重复使用的角色设定图和分镜画面。
4. 在保持角色与视觉风格一致的前提下生成视频镜头。
5. 添加配音、音乐、音效和字幕，导出最终影片。

## 案例展示

每个案例包含两张角色设定图和两个连续章节。点击章节按钮即可观看带音频的视频。

### 1. 盗墓笔记

<table>
  <tr>
    <td align="center" width="50%"><img src="assets/characters_image/盗墓笔记_1.jpg" width="420" alt="盗墓笔记角色设定图一"><br><b>角色设定图 1</b></td>
    <td align="center" width="50%"><img src="assets/characters_image/盗墓笔记_2.jpg" width="420" alt="盗墓笔记角色设定图二"><br><b>角色设定图 2</b></td>
  </tr>
  <tr>
    <td align="center"><a href="assets/video_example/盗墓笔记_1.mp4"><b>观看第 1 章</b></a></td>
    <td align="center"><a href="assets/video_example/盗墓笔记_2.mp4"><b>观看第 2 章</b></a></td>
  </tr>
</table>

### 2. 茅山捉鬼人

<table>
  <tr>
    <td align="center" width="50%"><img src="assets/characters_image/茅山捉鬼人_1.jpg" width="420" alt="茅山捉鬼人角色设定图一"><br><b>角色设定图 1</b></td>
    <td align="center" width="50%"><img src="assets/characters_image/茅山捉鬼人_2.jpg" width="420" alt="茅山捉鬼人角色设定图二"><br><b>角色设定图 2</b></td>
  </tr>
  <tr>
    <td align="center"><a href="assets/video_example/茅山捉鬼人_1.mp4"><b>观看第 1 章</b></a></td>
    <td align="center"><a href="assets/video_example/茅山捉鬼人_2.mp4"><b>观看第 2 章</b></a></td>
  </tr>
</table>

### 3. 我在末日扫垃圾

<table>
  <tr>
    <td align="center" width="50%"><img src="assets/characters_image/我在末日扫垃圾_1.jpg" width="420" alt="我在末日扫垃圾角色设定图一"><br><b>角色设定图 1</b></td>
    <td align="center" width="50%"><img src="assets/characters_image/我在末日扫垃圾_2.jpg" width="420" alt="我在末日扫垃圾角色设定图二"><br><b>角色设定图 2</b></td>
  </tr>
  <tr>
    <td align="center"><a href="assets/video_example/我在末日扫垃圾_1.mp4"><b>观看第 1 章</b></a></td>
    <td align="center"><a href="assets/video_example/我在末日扫垃圾_2.mp4"><b>观看第 2 章</b></a></td>
  </tr>
</table>

### 4. 星辰变

<table>
  <tr>
    <td align="center" width="50%"><img src="assets/characters_image/星辰变_1.jpg" width="420" alt="星辰变角色设定图一"><br><b>角色设定图 1</b></td>
    <td align="center" width="50%"><img src="assets/characters_image/星辰变_2.jpg" width="420" alt="星辰变角色设定图二"><br><b>角色设定图 2</b></td>
  </tr>
  <tr>
    <td align="center"><a href="assets/video_example/星辰变_1.mp4"><b>观看第 1 章</b></a></td>
    <td align="center"><a href="assets/video_example/星辰变_2.mp4"><b>观看第 2 章</b></a></td>
  </tr>
</table>
