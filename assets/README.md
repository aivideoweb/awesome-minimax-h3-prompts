# Original Visual Assets and Production Records

This directory contains one new VideoWeb AI cover and eleven generated gallery references inherited from the Flaq AI upstream repository (see [provenance](../UPSTREAM.md)). The gallery images are first-frame and mood references; the VideoWeb cover is editorial artwork. None is an official model benchmark or a verified MiniMax H3 result.

## Asset index

| File | Role | Related recipe | Image brief |
|---|---|---|---|
| `hero-minimax-h3-video-prompts.webp` | VideoWeb AI editorial cover | Main README | [VideoWeb cover brief](./videoweb-cover-prompt.md) |
| `gallery/midnight-observatory-tea.webp` | Brand/product first frame | [BRD-001](../prompts/01-brand-advertising.md#brd-001-midnight-observatory-tea-launch) | [IMG-002](./minimax-h3-reference-image-prompts.md#img-002-brand-and-product-midnight-observatory-tea) |
| `gallery/honest-desk-lamp-demo.webp` | UGC creator/product first frame | [UGC-001](../prompts/03-ugc-lifestyle.md#ugc-001-desk-lamp-honest-first-impression) | [IMG-003](./minimax-h3-reference-image-prompts.md#img-003-ugc-and-lifestyle-honest-desk-lamp-demo) |
| `gallery/rain-washed-canal-morning.webp` | Fictional first frame; mood reference only for TRV-001 | [Fictional single-image practice](../docs/fictional-canal-starter.md) | [IMG-004](./minimax-h3-reference-image-prompts.md#img-004-travel-rain-washed-canal-morning) |
| `gallery/clay-repair-robot.webp` | Animation character/environment reference | [ANI-002](../prompts/08-animation-stylized.md#ani-002-clay-repair-robot-finds-a-button) | [IMG-005](./minimax-h3-reference-image-prompts.md#img-005-animation-clay-repair-robot-workshop) |
| `gallery/indoor-climbing-final-hold.webp` | Sports athlete/route reference | [ACT-001](../prompts/09-action-sports.md#act-001-indoor-climbing-final-move) | [IMG-006](./minimax-h3-reference-image-prompts.md#img-006-sports-indoor-climbing-final-hold) |
| `gallery/radial-cork-speaker.webp` | Fictional product identity/material reference | [MRF-002](../prompts/20-multireference-camera-transfer.md#mrf-002-radial-cork-speaker-transfer-motion-grammar-not-content) | [IMG-007](./minimax-h3-reference-image-prompts.md#img-007-product-radial-cork-speaker) |
| `gallery/paper-birds-storm-shelter.webp` | Paper-craft character/environment reference | [CHR-001](../prompts/21-character-dialogue-performance.md#chr-001-paper-birds-plan-for-the-storm) | [IMG-008](./minimax-h3-reference-image-prompts.md#img-008-character-paper-birds-in-a-storm-shelter) |
| `gallery/three-biome-museum-rail.webp` | Multi-reference one-take first frame | [MRF-001](../prompts/20-multireference-camera-transfer.md#mrf-001-three-biome-museum-rail-in-one-take) | [IMG-009](./minimax-h3-reference-image-prompts.md#img-009-multi-reference-three-biome-museum-rail) |
| `gallery/dynamic-night-market-poster.webp` | Dynamic-poster final frame | [MOG-001](../prompts/22-motion-graphics-dynamic-posters.md#mog-001-night-market-poster-builds-on-the-beat) | [IMG-010](./minimax-h3-reference-image-prompts.md#img-010-motion-graphics-dynamic-night-market-poster) |
| `gallery/topographic-map-archive.webp` | Practical-surreal first frame | [SRL-001](../prompts/23-surreal-physics-optical-illusions.md#srl-001-the-map-rises-into-a-landscape) | [IMG-011](./minimax-h3-reference-image-prompts.md#img-011-surreal-physics-topographic-map-archive) |
| `gallery/modular-lunch-jar-kit.webp` | Live-creator product reference | [VER-001](../prompts/24-vertical-series-live-creator.md#ver-001-honest-modular-lunch-jar-live-demo) | [IMG-012](./minimax-h3-reference-image-prompts.md#img-012-live-creator-modular-lunch-jar-kit) |

## Upstream generation records (gallery assets)

- **Generated:** 2026-08-05
- **Actual tool used:** Codex built-in image generation
- **Source prompts:** Original briefs in [minimax-h3-reference-image-prompts.md](./minimax-h3-reference-image-prompts.md)
- **Post-processing:** Lossy WebP conversion at quality 88; no content retouching or compositing
- **Input images:** None
- **Third-party logos or source-gallery media:** None
- **Intended use:** Repository documentation, visual navigation, and optional first-frame/mood references

### 2026-08-26 expansion batch

- **Generated:** 2026-08-26
- **Actual tool used:** Codex built-in image generation
- **New files:** `radial-cork-speaker.webp`, `paper-birds-storm-shelter.webp`, and `three-biome-museum-rail.webp`
- **Source prompts:** Original briefs [IMG-007–009](./minimax-h3-reference-image-prompts.md#img-007-product-radial-cork-speaker)
- **Post-processing:** Lossy WebP conversion at quality 88; no content retouching or compositing
- **Input images and third-party media:** None
- **Intended use:** Original H3 product, character-dialogue, and multi-reference first frames

### 2026-09-01 expansion batch

- **Generated:** 2026-09-01
- **Actual tool used:** Codex built-in image generation
- **New files:** `dynamic-night-market-poster.webp`, `topographic-map-archive.webp`, and `modular-lunch-jar-kit.webp`
- **Source prompts:** Original briefs [IMG-010–012](./minimax-h3-reference-image-prompts.md#img-010-motion-graphics-dynamic-night-market-poster)
- **Post-processing:** Lossy WebP conversion at quality 88; no content retouching or compositing
- **Input images and third-party media:** None
- **Intended use:** Original H3 motion-graphics, practical-surreal, and live-creator references

The source briefs are model-neutral and intended to produce H3 first-frame, subject, product, location, or mood references. The committed images were created with the recorded tool above and must not be attributed to another model.

## Review notes

- Generated people and products are fictional and should not be treated as real endorsements;
- The canal image is a fictional composite location and must not be labeled as a specific real destination. Use the [fictional single-image practice version](../docs/fictional-canal-starter.md); it does not provide the three verified location references required by TRV-001;
- The climbing image is visual reference material, not safety instruction; qualified supervision and real equipment review remain necessary;
- Image generators can still produce small anatomical, geometric, or material inconsistencies; inspect at full size before commercial reuse;
- Reusing an image as an H3 input can produce different motion, identity, and product details.

## Rules for future assets

- Submit only newly authored concepts and media you have the right to redistribute;
- Record the exact image/video model or tool actually used;
- Include the final prompt, inputs, generation date, post-processing, and known defects;
- Use lowercase English filenames and web-friendly formats;
- Do not preserve external authors, handles, watermarks, logos, campaign copy, or gallery tracking links;
- Do not present generated examples as official performance evidence.

Return to the [main README](../README.md) or the [84-prompt library](../prompts/README.md).

## VideoWeb cover — September 22, 2026

Generated with the Codex built-in image tool, without input images. Converted to WebP at quality 88; no content edits. See the [exact prompt](./videoweb-cover-prompt.md). This is an editorial cover, not a generated H3 video frame or a screenshot. Small decorative lettering is not instructional content.
