# MiniMax H3: Capabilities, Official Resources and Prompting Strategy

> Last verified: 2026-08-06. Model access, licenses, input limits, model identifiers, and API fields can change. Treat the official repository, model card, and platform documentation as the source of truth.

## What MiniMax H3 is

MiniMax presents H3 as a general-purpose audiovisual generation system built around native understanding and generation across text, images, audio, and video. Its official examples emphasize coordinated control of people, objects, scenes, sound, rhythm, and editing intent rather than visual style alone.

That makes an effective H3 prompt closer to a production brief than a keyword pile. It should state:

- which input controls identity, product, location, motion, rhythm, or sound;
- what happens at the beginning, during each beat, and at the end;
- which geometry, identity, wardrobe, props, UI, and screen direction cannot change;
- what dialogue, ambience, effects, or music should be heard—and who owns each voice;
- what must be excluded for continuity, safety, factual, rights, or brand reasons.

The [official MiniMax-H3 repository](https://github.com/MiniMax-AI/MiniMax-H3) documents the open-weight architecture, task variants, input limits, local deployment, hybrid 2K workflow, bundled skills, and reproducible videos. The [official H3 prompt examples](https://platform.minimaxi.com/docs/guides/video-prompt) and [video-generation guide](https://platform.minimaxi.com/docs/guides/video-generation) cover the hosted product and API surface.

## Official open-weight and developer links

| Resource | Official address | Use it for |
|---|---|---|
| H3 official repository | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | Read the architecture, deployment commands, reproducible scripts, skills, and official example media |
| H3 model card and open weights | [MiniMaxAI/MiniMax-H3 on Hugging Face](https://huggingface.co/MiniMaxAI/MiniMax-H3) | Check model files, license, intended use, hardware/runtime notes, supported tasks, and release updates |
| H3 prompt-writing skill | [skills/h3-prompt-writing](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills/h3-prompt-writing) | Review official guidance for text/keyframe and full-reference modes |
| MiniMax model hub | [MiniMaxAI on Hugging Face](https://huggingface.co/MiniMaxAI) | Verify that a model page belongs to the official publisher and find related releases |
| MiniMax open-source organization | [MiniMax-AI on GitHub](https://github.com/MiniMax-AI) | Find official SDKs, tools, research projects, and integration repositories |
| Official command-line tool | [MiniMax-AI/cli](https://github.com/MiniMax-AI/cli) | Explore MiniMax's public tool for text, image, video, speech, and music workflows |
| Official MCP server | [MiniMax-AI/MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP) | Connect supported MiniMax generation APIs to MCP-compatible clients |
| Platform documentation | [MiniMax Open Platform](https://platform.minimaxi.com/docs) | Confirm hosted API models, parameters, limits, authentication, and billing behavior |

### Open weights are not the same as every hosted feature

This repository uses **open weights/model release** for H3-Base and **hosted components** for services that are not included in the current release. The official repository states that H3-Context-IR and H3-Regenerate-2K are hosted and not currently open-sourced; the initial public release also uses full attention rather than the future sparse-attention implementation.

Before local or commercial use:

1. read the current model card and license;
2. confirm which checkpoint and task match your inputs;
3. check runtime and hardware requirements;
4. verify that the downloadable path exposes the same behavior your recipe needs;
5. record the exact checkpoint, revision, workflow, inputs, and post-processing.

## Verified release profile

| Item | Official release information |
|---|---|
| Local checkpoints | FL2VA and Ref2VA, BF16 |
| Local task values | t2va, fl2va and ref2va |
| Local H3-Base output | 768-pixel short edge, native video and stereo audio |
| Full system output | Up to 2K through the hosted Regenerate-2K stage |
| Duration | 4–15 seconds |
| Frame rate | 24 FPS |
| Audio | 32 kHz stereo |
| Stable dialogue languages | Arabic, Chinese, English, French, German, Italian, Japanese, Korean, Portuguese, Russian and Spanish |
| FL2VA inputs | Zero, one or two images for text, first frame, last frame, or first-and-last-frame generation |
| Ref2VA inputs | Up to 9 images, 3 videos and 3 audio clips; no more than 12 mixed files; audio cannot be the sole input |

See the [multilingual deployment guide](./deployment-guide.md) for installation, SGLang serving, request examples, hardware notes, output checks and the hybrid 2K flow.

## H3-oriented workflow patterns

The exact names available in a product or API may differ. These patterns describe creative input roles, not invented request parameters.

| Pattern | Best for | Prompt emphasis | Main review risk |
|---|---|---|---|
| Text-led audiovisual generation | Original scenes without fixed source media | Subject, action, timeline, camera, sound, ending | Ambiguity, overload, continuity drift |
| First-frame-guided motion | Animating a controlled composition | What moves, what stays fixed, motion path, end state | Geometry drift, unwanted reframing |
| First-and-last-frame transition | Planned transformation or passage | Start/end invariants, intermediate causality, timing | Teleportation, early morph, weak arrival |
| Subject or identity reference | Recurring people, pets, products, characters | Identity priority, wardrobe, angles, occlusion rules | Face, marking, costume, or shape drift |
| Video-guided movement | Choreography, camera behavior, physical action | Transfer only motion/camera; reject source identity/style | Copying unwanted source details |
| Audio- or rhythm-guided sequence | Performance, dialogue, edits, visualizers | Beat map, speaker ownership, event-to-sound mapping | Desynchronization, voice swap, added audio |
| Multimodal combination | Ads, narrative, education, product films | Explicit reference map and conflict priority | Inputs fighting each other |
| Precise revision | Fixing one failed dimension | Change one target; repeat all invariants | Broad unintended rewrite |

## A practical H3 prompt contract

~~~text
Deliverable
State the channel, audience, aspect ratio, duration target, and communication goal.

Reference map
Image 1 = identity only.
Image 2 = exact product geometry and label placement.
Video 1 = movement timing only; do not copy performer, setting, or wardrobe.
Audio 1 = rhythm and energy only; do not add lyrics.

Opening state
Describe the subject, environment, light, spatial relationships, and camera.

Timeline
0–4 s: first visible action and camera behavior.
4–8 s: causal development, reaction, or state change.
8–12 s: resolved final state with a usable hold.

Continuity locks
Repeat every identity, product, wardrobe, prop, UI, geography, and screen-direction invariant.

Sound intent
Assign dialogue to named speakers; specify ambience, effects, music role, and silence.

Avoid
List the most likely visual, physical, continuity, factual, safety, rights, and delivery failures.
~~~

## Prompting decisions that matter most

### Give every reference one job

“Use all references” leaves conflict resolution to the model. Prefer narrow roles and a priority order:

~~~text
Priority 1: preserve the product silhouette and label from Image 1.
Priority 2: preserve the adult performer's identity from Image 2.
Priority 3: borrow only the warm/cool color relationship from Image 3.
Video 1 controls hand movement timing only.
Audio 1 controls edit accents only.
~~~

### Write visible causality

Replace a result such as “the room becomes cozy” with observable events:

~~~text
The hand presses the upper switch once. The ceiling light dims smoothly.
Only after the light reaches warm amber do the blinds close from top to bottom.
~~~

### Bound camera motion in time

One controlled move per short beat is easier to review than a chain of competing moves. Describe start framing, direction, speed, subject relationship, and stop point.

### Treat audio as a timeline

Name the source and timing of dialogue, ambience, effects, and music. For multilingual dialogue, identify the language and speaker on every line, and explicitly state who remains silent.

### Generate for editing

Ask for clean negative space, a stable final hold, or a loop seam. Add critical typography, verified data, captions, legal copy, prices, and interface text in post unless the workflow can preserve them exactly.

## Responsible use

- Obtain consent for identity and voice references.
- Use licensed music, footage, images, brands, locations, and datasets.
- Do not fabricate testimonials, evidence, prices, safety certification, health outcomes, historical facts, or product performance.
- Label interpretive reconstruction, time compression, concept visualization, or generated media when appropriate.
- Review anatomy, physics, dialogue attribution, cultural context, accessibility, privacy, and final text before release.

Continue with the [deployment guide](./deployment-guide.md), [official example gallery](./official-h3-examples.md), [H3 prompting guide](./prompting-guide.md), [84-prompt library](../prompts/README.md), [multilingual guide](./multilingual-prompting.md), or [API workflow](./api-workflow.md).
