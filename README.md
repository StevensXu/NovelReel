<div align="center">

# NovelReel

### Turn web novels into cinematic videos with AI

An open-source pipeline for adapting long-form web fiction into scripts,
consistent characters, visual shots, narration, and finished videos.

<a href="README.md"><img src="https://img.shields.io/badge/English-0969DA?style=for-the-badge" alt="English"></a>
<a href="README_zh-CN.md"><img src="https://img.shields.io/badge/中文-D73A49?style=for-the-badge" alt="中文"></a>

[Introduction](#introduction) · [Workflow](#workflow) · [Characters](#character-showcase) · [Examples](#video-examples)

</div>

## Introduction

**NovelReel** is an AI movie production toolkit designed for web novels.
It transforms chapters into structured scenes, maintains character and visual
consistency, generates shots and voices, and assembles everything into a
complete video.

The project is built for creators and developers who want a reproducible,
editable, and extensible novel-to-video workflow.

### Highlights

- Long-form novel and chapter parsing
- Automatic screenplay and shot-list generation
- Consistent character and scene design
- Image-to-video and text-to-video generation
- Multi-character dialogue, narration, music, and sound effects
- Automated editing, subtitles, and final video export

## Workflow

```mermaid
flowchart LR
    A[Web Novel] --> B[Story Analysis]
    B --> C[Screenplay]
    C --> D[Character & World Design]
    D --> E[Storyboard]
    E --> F[Image / Video Generation]
    C --> G[Voice & Audio]
    F --> H[Editing & Subtitles]
    G --> H
    H --> I[Final Movie]
```

1. Parse the novel and extract characters, locations, events, and timelines.
2. Adapt the source text into scenes, dialogue, narration, and camera directions.
3. Generate reusable character references and storyboard frames.
4. Produce video shots while preserving visual consistency.
5. Add voices, music, sound effects, subtitles, and export the final movie.

## Character Showcase

<table>
  <tr>
    <td align="center"><img src="assets/characters/character-01.jpg" width="240" alt="Mystery character"><br><b>Mystery</b></td>
    <td align="center"><img src="assets/characters/character-02.jpg" width="240" alt="Fantasy character"><br><b>Fantasy</b></td>
  </tr>
  <tr>
    <td align="center"><img src="assets/characters/character-03.jpg" width="240" alt="Apocalypse character"><br><b>Apocalypse</b></td>
    <td align="center"><img src="assets/characters/character-04.jpg" width="240" alt="Cultivation character"><br><b>Cultivation</b></td>
  </tr>
</table>

## Video Examples

Click a preview image to open the video with audio.

<table>
  <tr>
    <td align="center">
      <a href="assets/examples/example-01.mp4">
        <img src="assets/characters/character-01.jpg" width="360" alt="Mystery video example">
      </a>
      <br><b>Mystery Adventure</b>
    </td>
    <td align="center">
      <a href="assets/examples/example-02.mp4">
        <img src="assets/characters/character-02.jpg" width="360" alt="Fantasy video example">
      </a>
      <br><b>Supernatural Fantasy</b>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="assets/examples/example-03.mp4">
        <img src="assets/characters/character-03.jpg" width="360" alt="Apocalypse video example">
      </a>
      <br><b>Post-apocalyptic Story</b>
    </td>
    <td align="center">
      <a href="assets/examples/example-04.mp4">
        <img src="assets/characters/character-04.jpg" width="360" alt="Cultivation video example">
      </a>
      <br><b>Eastern Cultivation</b>
    </td>
  </tr>
</table>
This project will be released under an open-source license. Please verify that
you have permission to use any source novel, generated media, voices, music,
and third-party models included in your production.
