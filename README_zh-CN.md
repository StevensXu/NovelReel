<div align="center">

# NovelReel

### 将网络小说转化为角色一致、电影级的 AI 短剧

一个由 LLM 和视觉生成模型驱动的端到端开源制作流水线。

<p>
  <img src="https://img.shields.io/badge/状态-开发中-F59E0B?style=flat-square" alt="状态：开发中">
  <img src="https://img.shields.io/badge/流程-全自动-2EA44F?style=flat-square" alt="全自动制作流程">
  <img src="https://img.shields.io/badge/一致性-视觉_%2B_音色-8250DF?style=flat-square" alt="视觉和音色一致性">
  <img src="https://img.shields.io/badge/内容-网络小说-0969DA?style=flat-square" alt="面向网络小说">
</p>

<p>
  <a href="README.md"><img src="https://img.shields.io/badge/English-0969DA?style=for-the-badge" alt="English"></a>
  <a href="README_zh-CN.md"><img src="https://img.shields.io/badge/中文-D73A49?style=for-the-badge" alt="中文"></a>
</p>

[项目介绍](#项目介绍) · [工作流程](#工作流程) · [案例展示](#案例展示) · [音色对比](#角色音色一致性对比)

</div>

---

## 项目介绍

**NovelReel** 是一个专为网络小说设计的 AI 短剧制作流水线。它可以将小说
转化为完整的 AI 短剧，并保持角色（形象与音色）、道具和场景的一致性。
整个制作过程无需人工介入。

### 核心能力

<table>
  <tr>
    <td width="50%"><b>自动化小说改编</b><br>提取故事元素、编排剧本，并生成剧情连续的 AI 短剧。</td>
    <td width="50%"><b>视觉一致性</b><br>保持角色形象、道具和场景在跨章节、跨镜头时的一致性。</td>
  </tr>
  <tr>
    <td width="50%"><b>角色音色一致性</b><br>为每个角色分配并校准稳定音色，贯穿完整故事。</td>
    <td width="50%"><b>端到端制作</b><br>串联故事分析、参考图、分镜、视频生成和最终音频制作。</td>
  </tr>
</table>

## 工作流程

<div align="center">
  <img src="assets/method.jpg" width="100%" alt="NovelReel 视频生成与角色音色一致性流水线">
  <br>
  <sub>NovelReel 视频生成与角色音色一致性流水线。</sub>
</div>

<br>

1. 解析小说，提取角色、地点、事件和故事时间线。
2. 建立跨章节共享的全局角色与道具参考。
3. 将原文改编为剧本、分镜和镜头描述。
4. 在保持角色、道具和场景一致的前提下生成视频镜头。
5. 分离对白、对齐说话角色、统一角色音色并生成最终音频。

---

## 案例展示

每个案例包含两张角色设定图和两个连续章节。点击视频封面即可观看带音频的生成结果。

### 1. 盗墓笔记

<table>
  <tr>
    <th></th>
    <th align="center">第一章</th>
    <th align="center">第二章</th>
  </tr>
  <tr>
    <th align="center">角色设定图</th>
    <td align="center"><img src="assets/characters_image/盗墓笔记_1.jpg" width="360" alt="盗墓笔记第一章角色设定图"></td>
    <td align="center"><img src="assets/characters_image/盗墓笔记_2.jpg" width="360" alt="盗墓笔记第二章角色设定图"></td>
  </tr>
  <tr>
    <th align="center">生成视频片段</th>
    <td align="center"><a href="https://youtu.be/ba7dlY-buiY"><img src="assets/youtube_thumbnails/ba7dlY-buiY.jpg" width="360" alt="在 YouTube 观看盗墓笔记第一章"></a></td>
    <td align="center"><a href="https://youtu.be/npjA1qq8AhM"><img src="assets/youtube_thumbnails/npjA1qq8AhM.jpg" width="360" alt="在 YouTube 观看盗墓笔记第二章"></a></td>
  </tr>
</table>

### 2. 茅山捉鬼人

<table>
  <tr>
    <th></th>
    <th align="center">第一章</th>
    <th align="center">第二章</th>
  </tr>
  <tr>
    <th align="center">角色设定图</th>
    <td align="center"><img src="assets/characters_image/茅山捉鬼人_1.jpg" width="360" alt="茅山捉鬼人第一章角色设定图"></td>
    <td align="center"><img src="assets/characters_image/茅山捉鬼人_2.jpg" width="360" alt="茅山捉鬼人第二章角色设定图"></td>
  </tr>
  <tr>
    <th align="center">生成视频片段</th>
    <td align="center"><a href="https://youtu.be/GVt8tebEKvA"><img src="assets/youtube_thumbnails/GVt8tebEKvA.jpg" width="360" alt="在 YouTube 观看茅山捉鬼人第一章"></a></td>
    <td align="center"><a href="https://youtu.be/mdMaMKaI8Bc"><img src="assets/youtube_thumbnails/mdMaMKaI8Bc.jpg" width="360" alt="在 YouTube 观看茅山捉鬼人第二章"></a></td>
  </tr>
</table>

### 3. 我在末日扫垃圾

<table>
  <tr>
    <th></th>
    <th align="center">第一章</th>
    <th align="center">第二章</th>
  </tr>
  <tr>
    <th align="center">角色设定图</th>
    <td align="center"><img src="assets/characters_image/我在末日扫垃圾_1.jpg" width="360" alt="我在末日扫垃圾第一章角色设定图"></td>
    <td align="center"><img src="assets/characters_image/我在末日扫垃圾_2.jpg" width="360" alt="我在末日扫垃圾第二章角色设定图"></td>
  </tr>
  <tr>
    <th align="center">生成视频片段</th>
    <td align="center"><a href="https://youtu.be/9-AosqKD1IE"><img src="assets/youtube_thumbnails/9-AosqKD1IE.jpg" width="360" alt="在 YouTube 观看我在末日扫垃圾第一章"></a></td>
    <td align="center"><a href="https://youtu.be/JrzBbX469sA"><img src="assets/youtube_thumbnails/JrzBbX469sA.jpg" width="360" alt="在 YouTube 观看我在末日扫垃圾第二章"></a></td>
  </tr>
</table>

### 4. 星辰变

<table>
  <tr>
    <th></th>
    <th align="center">第一章</th>
    <th align="center">第二章</th>
  </tr>
  <tr>
    <th align="center">角色设定图</th>
    <td align="center"><img src="assets/characters_image/星辰变_1.jpg" width="360" alt="星辰变第一章角色设定图"></td>
    <td align="center"><img src="assets/characters_image/星辰变_2.jpg" width="360" alt="星辰变第二章角色设定图"></td>
  </tr>
  <tr>
    <th align="center">生成视频片段</th>
    <td align="center"><a href="https://youtu.be/OesS29j5fVw"><img src="assets/youtube_thumbnails/OesS29j5fVw.jpg" width="360" alt="在 YouTube 观看星辰变第一章"></a></td>
    <td align="center"><a href="https://youtu.be/AsaULb0MdGM"><img src="assets/youtube_thumbnails/AsaULb0MdGM.jpg" width="360" alt="在 YouTube 观看星辰变第二章"></a></td>
  </tr>
</table>

---

## 角色音色一致性对比

对同一角色跨镜头、跨章节的音色进行校准，使角色声音在连续剧情中保持一致。
点击封面可观看并对比处理前后的完整视频。

### 对比例子 1

<table>
  <tr>
    <th align="center">角色音色一致化前</th>
    <th align="center">角色音色一致化后</th>
  </tr>
  <tr>
    <td align="center"><a href="https://youtu.be/LO2K_PX2f_s"><img src="assets/youtube_thumbnails/LO2K_PX2f_s.jpg" width="420" alt="观看角色音色一致化前的视频"></a></td>
    <td align="center"><a href="https://youtu.be/9-AosqKD1IE"><img src="assets/youtube_thumbnails/9-AosqKD1IE.jpg" width="420" alt="观看角色音色一致化后的视频"></a></td>
  </tr>
</table>

### 对比例子 2

<table>
  <tr>
    <th align="center">角色音色一致化前</th>
    <th align="center">角色音色一致化后</th>
  </tr>
  <tr>
    <td align="center"><a href="https://youtu.be/nrP3PAaMTfA"><img src="assets/youtube_thumbnails/nrP3PAaMTfA.jpg" width="420" alt="观看角色音色一致化前的视频"></a></td>
    <td align="center"><a href="https://youtu.be/mdMaMKaI8Bc"><img src="assets/youtube_thumbnails/mdMaMKaI8Bc.jpg" width="420" alt="观看角色音色一致化后的视频"></a></td>
  </tr>
</table>
