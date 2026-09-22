# Reusable Video Prompt Templates

These twelve templates are production skeletons, not model-specific API presets. They reflect H3's official emphasis on multimodal references, audiovisual coordination, and precise editing control while avoiding unverified request parameters. Replace every `[variable]`, delete irrelevant fields, and keep the final prompt internally consistent.

## T01 Text-to-video: single readable shot

```text
Use case: [deliverable]
Generation mode: text-to-video
Deliverable: [platform], [aspect ratio], target [duration]
Goal: [one communication goal]
Scene and subject: [specific setting, time, subject, wardrobe, props]
Start state: [what the first frame establishes]
Primary action: [one continuous action]
End state: [what resolves or changes]
Camera: [shot size and angle], [one motivated camera movement]
Timing: [beat 1] → [beat 2] → [beat 3]
Visual style: [observable photographic or animation qualities]
Lighting and color: [source, direction, contrast, palette]
Continuity locks: [identity, wardrobe, object geometry, environment]
Constraints: one continuous shot; stable subject; plausible motion; clear ending
Avoid: scene cuts, competing actions, flicker, warping, duplicate subjects, text, logos, watermark
```

## T02 Image-to-video: animate the source image

```text
Generation mode: image-to-video
Input image: the visual source of truth for identity, composition, product geometry, wardrobe, background, and color
Motion request: [subject movement] while [environment movement]
Camera: [static / push-in / pull-back / pan / orbit], subtle and physically plausible
Depth behavior: preserve foreground, subject, and background separation; maintain occlusion and perspective
Start state: match the input image exactly
End state: [clear final pose or scene state]
Preserve: facial identity, body proportions, product shape, labels, architecture, crop, palette, and lighting direction
Avoid: redesign, new objects, disappearing objects, face drift, label mutation, melting edges, sudden camera jump
```

## T03 First-and-last-frame transition

```text
Generation mode: first-and-last-frame video
First frame: use Image 1 exactly as the opening state
Last frame: arrive naturally at Image 2 as the closing state
Transition logic: [physical or narrative steps connecting the states]
Subject path: [position, direction, speed, and pose progression]
Camera path: [start framing] → [movement] → [end framing]
Continuity locks: [identity, product, wardrobe, scene, weather, lighting]
Timing: settle on the first frame, perform one readable transition, settle on the last frame
Constraints: no cut; preserve screen direction; end composition aligns with Image 2
Avoid: teleportation, identity blending, unexplained object changes, mid-transition reset, overshooting the final frame
```

## T04 Product advertisement

```text
Use case: product-advertising
Deliverable: [platform and ratio], target [duration]
Product lock: [silhouette, dimensions, materials, colors, cap/controls, label and logo placement]
Opening: [clean product recognition beat]
Feature action: [one truthful, visible property or use]
Hero ending: [final composition with safe space for approved copy]
Camera: [lens feel, angle, path, focus behavior]
Environment: [surface, backdrop, supporting props]
Lighting: [key, fill, rim, reflections]
Material behavior: [condensation, fabric, metal, liquid, particles]
Text on screen: "[approved exact copy]"
Constraints: preserve product geometry and label; do not invent claims, certification, price, or packaging text
Avoid: warped logo, mirrored label, duplicate product, floating prop, impossible reflection, unrelated text, watermark
```

## T05 Vertical creator/UGC clip

```text
Use case: creator-style product demonstration
Deliverable: 9:16 vertical, target [duration], mobile-safe framing
Creator: [fictional or consented adult description; wardrobe and setting]
Performance: [natural expression and one simple action]
Camera: handheld phone at [distance], mild micro-movement, stable exposure and focus
Lighting: believable [window / room / outdoor] light
Beat 1 hook: [visually clear setup]
Beat 2 proof: [show the product or action]
Beat 3 close: [reaction, result, or safe-space ending]
Dialogue intent: [optional; exact approved words if supported]
Continuity locks: same person, hands, product, room, wardrobe, and time of day
Constraints: fictional demonstration; no unsupported testimonial or health/financial claim
Avoid: beauty-filter skin, overproduced commercial lighting, gaze drift, hand-product fusion, lip-sync promise, platform watermark
```

## T06 Multi-shot sequence plan

```text
Story goal: [one sentence]
Total target duration: [duration]
Continuity bible: [character/product, wardrobe, props, location, weather, color script]

Shot 1 — [time range]
- Purpose: [setup]
- Framing/camera: [shot size, angle, motion]
- Action: [one readable beat]
- Exit state: [state passed to next shot]

Shot 2 — [time range]
- Purpose: [development]
- Framing/camera: [shot size, angle, motion]
- Action: [one readable beat]
- Entry/exit continuity: [screen direction, pose, prop, light]

Shot 3 — [time range]
- Purpose: [payoff]
- Framing/camera: [shot size, angle, motion]
- Action: [one readable beat]
- Final state: [clean ending or CTA space]

Global constraints: consistent identity and design; no continuity reset; cuts occur only at specified boundaries
```

## T07 Single-variable revision

```text
Revision target: change only [motion / camera / timing / lighting / one object]
Current failure: [observable problem]
Requested correction: [observable successful behavior]
Preserve exactly: [all approved elements]
Do not change: [identity, composition, product, wardrobe, background, palette, text, duration]
```

## T08 Multimodal reference map

```text
Reference inputs:
- Image 1 — identity only: [face, hair, body proportions]
- Image 2 — product only: [geometry, material, label]
- Image 3 — location only: [architecture, layout, light direction]
- Video 1 — movement only: [action path, tempo, camera behavior]
- Audio 1 — sound only: [rhythm, ambience, emotional intensity]

Priority when references conflict:
1. [identity/product source]
2. [layout source]
3. [movement source]
4. [style or mood source]

Do not copy from references: [people, brands, text, objects, edits, or story elements outside each assigned role]
```

## T09 Precise multimodal edit

```text
Edit target: [Image 1 / Video 1]
Requested change: change only [one person, object, scene element, sound, timing, or effect]
New state: [observable result]
Edit interval/region: [time range or spatial target]
Match: [perspective, scale, motion, occlusion, light, reflection, room tone]
Preserve exactly: [identity, product, camera path, timing, background, wardrobe, UI, dialogue, all other sound]
Success condition: [what a reviewer should observe]
Avoid: global restyling, identity drift, new cuts, timing shift, added objects, removed objects, altered text, sound spill outside the target
```

## T10 Audio- or rhythm-guided sequence

```text
Audio 1 role: timing and intensity reference only; do not copy lyrics, melody, voice identity, or protected recording content
Visual concept: [original scene and subject]
Beat map:
- Beat A [time]: [opening state and restrained movement]
- Beat B [time]: [first visual change]
- Beat C [time]: [largest action or transition]
- Beat D [time]: [settle and final frame]
Synchronization: align [cuts / light pulses / actions] to structural beats, not every transient
Sound intent: [original ambience, effects, dialogue, or new music direction]
Continuity locks: [identity, product, location, color, screen direction]
Avoid: lip-sync claims without testing, copied melody, voice imitation, random beat cuts, strobing, continuity reset
```

## T11 Multilingual dialogue and speaker contract

```text
Cast and authorized voice map:
- Speaker A = [identity reference], [voice reference], speaks [language]
- Speaker B = [identity reference], [voice reference], speaks [language]

Dialogue timeline:
- [time]: Speaker A says, "[approved exact line]"; Speaker B listens without lip movement.
- [time]: Speaker B says, "[approved exact line]"; Speaker A listens without lip movement.

Performance: [emotion, volume, pace, gesture, eyeline]
Sound mix: dialogue foreground; [ambience]; [music or no music]
Preserve: voice-to-face ownership, identity, pronunciation, turn order, breathing, room acoustics
Delivery: create clean subtitle-safe space; add verified subtitles in post
Avoid: voice swapping, both mouths moving, invented words, overlapping lines, fake accent, private data, baked-in text
```

## T12 Open-weight/local generation record

```yaml
recipe_id: <ID>
generated_at: YYYY-MM-DD
model_source: https://huggingface.co/MiniMaxAI/MiniMax-H3
checkpoint: <exact checkpoint or task variant>
revision: <commit hash or release tag>
license_reviewed_at: YYYY-MM-DD
runtime: <project and exact version>
hardware: <accelerator, count, memory>
mode: <supported task>
inputs:
  - file: <local rights-cleared asset>
    role: <identity / first frame / motion / audio / other>
prompt: |
  <exact submitted prompt>
generation_settings:
  <only settings actually supported by the selected runtime>
post_processing:
  - <edit, audio mix, typography, upscale, or none>
review:
  status: pass | needs-revision
  known_issues:
    - <observable issue>
```

Do not assume that every hosted H3 feature exists in the open-weight release. Confirm the model card, license, checkpoint, supported task, and runtime documentation for the exact revision used.

Return to the [prompt library](../prompts/README.md), read the [prompting guide](../docs/prompting-guide.md), or review the [H3 overview and official links](../docs/minimax-h3-overview.md).
