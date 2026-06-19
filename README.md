<div align="center">

# NovelReel

### Turn web novels into consistent, cinematic AI short dramas

An open-source, end-to-end production pipeline powered by LLMs and visual
generative models.

<p>
  <img src="https://img.shields.io/badge/status-work_in_progress-F59E0B?style=flat-square" alt="Status: work in progress">
  <img src="https://img.shields.io/badge/pipeline-fully_automated-2EA44F?style=flat-square" alt="Fully automated pipeline">
  <img src="https://img.shields.io/badge/consistency-visual_%2B_voice-8250DF?style=flat-square" alt="Visual and voice consistency">
  <img src="https://img.shields.io/badge/content-web_novels-0969DA?style=flat-square" alt="Designed for web novels">
</p>

<p>
  <a href="README.md"><img src="https://img.shields.io/badge/English-0969DA?style=for-the-badge" alt="English"></a>
  <a href="README_zh-CN.md"><img src="https://img.shields.io/badge/中文-D73A49?style=for-the-badge" alt="中文"></a>
</p>

[Introduction](#introduction) · [Workflow](#workflow) · [Examples](#examples) · [Voice Comparison](#character-voice-consistency-comparison)

</div>

---

## Introduction

**NovelReel** is an AI short-drama production pipeline designed specifically
for web novels. It transforms novels into complete AI short dramas while
maintaining consistent characters (appearance and voice), props, and scenes.
The entire production process requires no manual intervention.

### Highlights

<table>
  <tr>
    <td width="50%"><b>Automated Adaptation</b><br>Extracts story elements, structures screenplays, and generates continuous short-drama episodes.</td>
    <td width="50%"><b>Visual Consistency</b><br>Maintains character appearance, props, and scene identity across chapters and shots.</td>
  </tr>
  <tr>
    <td width="50%"><b>Character Voice Consistency</b><br>Assigns and calibrates a stable voice for every character across the full story.</td>
    <td width="50%"><b>End-to-End Production</b><br>Connects story analysis, reference generation, storyboarding, video generation, and final audio.</td>
  </tr>
</table>

## Workflow

<div align="center">
  <img src="assets/method.jpg" width="100%" alt="NovelReel video generation and voice consistency pipeline">
  <br>
  <sub>NovelReel video generation and character voice consistency pipeline.</sub>
</div>

<br>

1. Parse the novel and extract characters, locations, events, and timelines.
2. Build global character and prop references shared across chapters.
3. Adapt the source text into screenplays, storyboards, and camera directions.
4. Generate video shots while preserving character, prop, and scene consistency.
5. Separate dialogue, align speakers, unify character voices, and produce final audio.

---

## Examples

Each example contains two character reference sheets and two consecutive
chapters. Click a video thumbnail to watch the generated chapter with audio.

### 1. The Lost Tomb

<table>
  <tr>
    <th></th>
    <th align="center">Chapter 1</th>
    <th align="center">Chapter 2</th>
  </tr>
  <tr>
    <th align="center">Character Design</th>
    <td align="center"><img src="assets/characters_image/盗墓笔记_1.jpg" width="360" alt="The Lost Tomb Chapter 1 character design"></td>
    <td align="center"><img src="assets/characters_image/盗墓笔记_2.jpg" width="360" alt="The Lost Tomb Chapter 2 character design"></td>
  </tr>
  <tr>
    <th align="center">Generated Video Clip</th>
    <td align="center"><a href="https://youtu.be/ba7dlY-buiY"><img src="assets/youtube_thumbnails/ba7dlY-buiY.jpg" width="360" alt="Watch The Lost Tomb Chapter 1 on YouTube"></a></td>
    <td align="center"><a href="https://youtu.be/npjA1qq8AhM"><img src="assets/youtube_thumbnails/npjA1qq8AhM.jpg" width="360" alt="Watch The Lost Tomb Chapter 2 on YouTube"></a></td>
  </tr>
</table>

### 2. Maoshan Ghost Hunter

<table>
  <tr>
    <th></th>
    <th align="center">Chapter 1</th>
    <th align="center">Chapter 2</th>
  </tr>
  <tr>
    <th align="center">Character Design</th>
    <td align="center"><img src="assets/characters_image/茅山捉鬼人_1.jpg" width="360" alt="Maoshan Ghost Hunter Chapter 1 character design"></td>
    <td align="center"><img src="assets/characters_image/茅山捉鬼人_2.jpg" width="360" alt="Maoshan Ghost Hunter Chapter 2 character design"></td>
  </tr>
  <tr>
    <th align="center">Generated Video Clip</th>
    <td align="center"><a href="https://youtu.be/GVt8tebEKvA"><img src="assets/youtube_thumbnails/GVt8tebEKvA.jpg" width="360" alt="Watch Maoshan Ghost Hunter Chapter 1 on YouTube"></a></td>
    <td align="center"><a href="https://youtu.be/mdMaMKaI8Bc"><img src="assets/youtube_thumbnails/mdMaMKaI8Bc.jpg" width="360" alt="Watch Maoshan Ghost Hunter Chapter 2 on YouTube"></a></td>
  </tr>
</table>

### 3. Scavenging at the End of the World

<table>
  <tr>
    <th></th>
    <th align="center">Chapter 1</th>
    <th align="center">Chapter 2</th>
  </tr>
  <tr>
    <th align="center">Character Design</th>
    <td align="center"><img src="assets/characters_image/我在末日扫垃圾_1.jpg" width="360" alt="Scavenging at the End of the World Chapter 1 character design"></td>
    <td align="center"><img src="assets/characters_image/我在末日扫垃圾_2.jpg" width="360" alt="Scavenging at the End of the World Chapter 2 character design"></td>
  </tr>
  <tr>
    <th align="center">Generated Video Clip</th>
    <td align="center"><a href="https://youtu.be/9-AosqKD1IE"><img src="assets/youtube_thumbnails/9-AosqKD1IE.jpg" width="360" alt="Watch Scavenging at the End of the World Chapter 1 on YouTube"></a></td>
    <td align="center"><a href="https://youtu.be/JrzBbX469sA"><img src="assets/youtube_thumbnails/JrzBbX469sA.jpg" width="360" alt="Watch Scavenging at the End of the World Chapter 2 on YouTube"></a></td>
  </tr>
</table>

### 4. Stellar Transformations

<table>
  <tr>
    <th></th>
    <th align="center">Chapter 1</th>
    <th align="center">Chapter 2</th>
  </tr>
  <tr>
    <th align="center">Character Design</th>
    <td align="center"><img src="assets/characters_image/星辰变_1.jpg" width="360" alt="Stellar Transformations Chapter 1 character design"></td>
    <td align="center"><img src="assets/characters_image/星辰变_2.jpg" width="360" alt="Stellar Transformations Chapter 2 character design"></td>
  </tr>
  <tr>
    <th align="center">Generated Video Clip</th>
    <td align="center"><a href="https://youtu.be/OesS29j5fVw"><img src="assets/youtube_thumbnails/OesS29j5fVw.jpg" width="360" alt="Watch Stellar Transformations Chapter 1 on YouTube"></a></td>
    <td align="center"><a href="https://youtu.be/AsaULb0MdGM"><img src="assets/youtube_thumbnails/AsaULb0MdGM.jpg" width="360" alt="Watch Stellar Transformations Chapter 2 on YouTube"></a></td>
  </tr>
</table>

---

## Character Voice Consistency Comparison

NovelReel calibrates each character's voice across shots and chapters, keeping
the voice consistent throughout a continuous storyline. Click a thumbnail to
compare the complete videos before and after voice consistency processing.

### Comparison 1

<table>
  <tr>
    <th align="center">Before Voice Consistency</th>
    <th align="center">After Voice Consistency</th>
  </tr>
  <tr>
    <td align="center"><a href="https://youtu.be/LO2K_PX2f_s"><img src="assets/youtube_thumbnails/LO2K_PX2f_s.jpg" width="420" alt="Watch the video before character voice consistency"></a></td>
    <td align="center"><a href="https://youtu.be/9-AosqKD1IE"><img src="assets/youtube_thumbnails/9-AosqKD1IE.jpg" width="420" alt="Watch the video after character voice consistency"></a></td>
  </tr>
</table>

### Comparison 2

<table>
  <tr>
    <th align="center">Before Voice Consistency</th>
    <th align="center">After Voice Consistency</th>
  </tr>
  <tr>
    <td align="center"><a href="https://youtu.be/nrP3PAaMTfA"><img src="assets/youtube_thumbnails/nrP3PAaMTfA.jpg" width="420" alt="Watch the video before character voice consistency"></a></td>
    <td align="center"><a href="https://youtu.be/mdMaMKaI8Bc"><img src="assets/youtube_thumbnails/mdMaMKaI8Bc.jpg" width="420" alt="Watch the video after character voice consistency"></a></td>
  </tr>
</table>
you have permission to use any source novel, generated media, voices, music,
and third-party models included in your production.
