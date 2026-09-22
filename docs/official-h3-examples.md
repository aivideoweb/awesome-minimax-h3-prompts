# Official MiniMax H3 Example Gallery

> Selected media hosted by the official [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) repository. This project links or hotlinks the original files for education and model-workflow comparison; it does not re-upload, rename, or claim authorship of them.

[部署指南](./deployment-guide.md) · [Deployment guide](./deployment-guide.md#english-deployment-reference) · [Prompt library](../prompts/README.md)

## Official skill previews

Each preview links back to its source in the official repository.

| Product advertising | 3D animation |
|---|---|
| [![Official MiniMax H3 minimalist product advertisement preview](https://raw.githubusercontent.com/MiniMax-AI/MiniMax-H3/main/assets/minimalist-product-ad-generator.gif)](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/assets/minimalist-product-ad-generator.gif) | [![Official MiniMax H3 3D animation short preview](https://raw.githubusercontent.com/MiniMax-AI/MiniMax-H3/main/assets/3d-animation-short-generator.gif)](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/assets/3d-animation-short-generator.gif) |
| Official source: [minimalist product ad skill](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills/minimalist-product-ad-generator) | Official source: [3D animation short skill](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills/3d-animation-short-generator) |

| Paper stop-motion explainer | Brand promotion |
|---|---|
| [![Official MiniMax H3 papercraft stop-motion explainer preview](https://raw.githubusercontent.com/MiniMax-AI/MiniMax-H3/main/assets/papercraft-stop-motion-explainer.gif)](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/assets/papercraft-stop-motion-explainer.gif) | [![Official MiniMax H3 brand promotion preview](https://raw.githubusercontent.com/MiniMax-AI/MiniMax-H3/main/assets/brand-promo-video-generator.gif)](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/assets/brand-promo-video-generator.gif) |
| Official source: [papercraft stop-motion skill](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills/papercraft-stop-motion-explainer) | Official source: [brand promotion skill](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills/brand-promo-video-generator) |

| Music video subtitles | Co-op game intro |
|---|---|
| [![Official MiniMax H3 music-video subtitle preview](https://raw.githubusercontent.com/MiniMax-AI/MiniMax-H3/main/assets/music-video-subtitle-generator.gif)](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/assets/music-video-subtitle-generator.gif) | [![Official MiniMax H3 co-op game intro preview](https://raw.githubusercontent.com/MiniMax-AI/MiniMax-H3/main/assets/co-op-game-intro-generator.gif)](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/assets/co-op-game-intro-generator.gif) |
| Official source: [music-video subtitle skill](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills/mv-subtitle-skill-confirmed) | Official source: [co-op game intro skill](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills/co-op-game-intro-generator) |

## Reproducible 768p outputs

These official examples pair a request script with an MP4 produced by the documented H3-Base workflow.

| Mode | What it demonstrates | Official request | Official output |
|---|---|---|---|
| T2VA | Text-to-video with native audio | [Request script](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/scripts/readme/reproducible-768p-t2va-request.sh) | [Watch t2va.mp4](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/assets/t2va.mp4) |
| FL2VA | First/last-frame-conditioned generation | [Request script](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/scripts/readme/reproducible-768p-fl2va-request.sh) | [Watch fl2va.mp4](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/assets/fl2va.mp4) |
| Ref2VA | Multimodal image/video/audio references | [Request script](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/scripts/readme/reproducible-768p-ref2va-request.sh) | [Watch ref2va.mp4](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/assets/ref2va.mp4) |

## Official 2K workflow comparisons

These examples help separate local H3-Base output from the hybrid Context-IR and Regenerate-2K path.

| Case | Local/base result | Regenerated or direct 2K result | Full official table |
|---|---|---|---|
| T2VA | [768p base](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/assets/t2va.mp4) | [Regenerate-2K](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/assets/t2va_2k.mp4) · [Direct API 2K](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/assets/h3_direct_2k.mp4) | [T2VA workflow](https://github.com/MiniMax-AI/MiniMax-H3#case-t2va) |
| I2VA | [768p base](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/assets/i2va.mp4) | [Regenerate-2K](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/assets/i2va_2k.mp4) · [Direct API 2K](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/assets/i2va_direct_2k.mp4) | [I2VA workflow](https://github.com/MiniMax-AI/MiniMax-H3#case-i2va) |
| Ref2VA | [768p base](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/assets/r2va.mp4) | [Hybrid/API 2K](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/assets/r2va_2k.mp4) · [Direct API 2K](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/assets/r2va_direct_2k.mp4) | [Ref2VA workflow](https://github.com/MiniMax-AI/MiniMax-H3#case-ref2va) |

## How to use these examples with this cookbook

Use official examples as capability and workflow references, not as prompt text to copy.

| Study | Observe in the official output | Apply in this repository |
|---|---|---|
| T2VA | Shot timing, native soundscape, subject continuity | Start with [T01](../templates/README.md#t01-text-to-video-single-readable-shot) and a matching original recipe |
| FL2VA | Whether the supplied image is preserved as an actual endpoint | Use [T03](../templates/README.md#t03-first-and-last-frame-transition) and specify start/end invariants |
| Ref2VA | Which visual, motion, and sound properties transfer semantically | Use [T08](../templates/README.md#t08-multimodal-reference-map) to give each reference one role |
| Dialogue | Voice ownership, mouth motion, silence and turn-taking | Use [T11](../templates/README.md#t11-multilingual-dialogue-and-speaker-contract) |
| Local versus 2K | Detail changes between H3-Base and regenerated output | Record both stages with [T12](../templates/README.md#t12-open-weightlocal-generation-record) |

Do not copy characters, branding, dialogue, shot design, music, or complete prompt expression from the official examples into a new “original” recipe. Create a new scene and use only the technical lesson being studied.

## Media and attribution policy

- Media ownership and licensing remain with MiniMax and the terms attached to the official H3 release.
- Every preview and MP4 link points to the official MiniMax-AI repository.
- No official MP4 or GIF is stored in this repository.
- If an upstream asset is renamed or removed, update or remove the reference rather than mirroring it without permission.
- Do not use official samples as evidence that every local hardware/runtime combination will produce identical results.
- Before commercial reuse, review the [MiniMax H3 Community License Agreement](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE) and obtain any additional rights required for depicted people, voices, music, brands, or source media.

Return to the [deployment guide](./deployment-guide.md), [H3 overview](./minimax-h3-overview.md), or [main README](../README.md).
