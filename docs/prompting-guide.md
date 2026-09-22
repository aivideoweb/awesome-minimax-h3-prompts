# Video Prompting Guide

This guide treats a MiniMax H3 video prompt as a compact production specification. The goal is not to accumulate cinematic adjectives; it is to make reference roles, action, time, camera, sound, edit scope, and invariants unambiguous enough to review.

MiniMax's official H3 examples describe native understanding and generation across text, image, audio, and video inputs; precise editing of people, objects, scenes, sound, and rhythm; and commercial coverage across advertising, drama, e-commerce, UI, games, and animation. This guide translates those capabilities into a provider-safe writing method without inventing API parameters. See the [official H3 capability page](https://platform.minimaxi.com/docs/guides/video-prompt) and the repository's [H3 overview, open-weight links, and workflow map](./minimax-h3-overview.md).

## 0. Map references before writing the story

Multimodal input is useful only when every reference has a narrow job:

```text
Image 1: character identity and wardrobe only
Image 2: product geometry, material, and label only
Image 3: location layout and lighting direction only
Video 1: action path and camera tempo only
Audio 1: rhythm and emotional intensity only
Do not copy: people, brands, text, props, story, or edits outside those roles
```

If two references conflict, state the priority. Identity and product references should normally outrank style and movement references. Avoid “combine everything from all references,” which gives no rule for resolving contradictions.

## 1. Start with the deliverable

Define where the video will be used, who will see it, and what the clip must communicate. A six-second product reveal and a six-second narrative scene need different pacing even when they share the same visual style.

```text
Weak: A premium cinematic coffee commercial, beautiful, 8K.

Stronger: A six-second 9:16 launch clip for a neighborhood cold-brew bottle. The bottle must be recognizable in the first second; condensation forms as the camera makes one slow push-in; finish on a stable hero frame with clean upper space for approved copy.
```

## 2. Write motion as a state change

For every shot, describe:

1. The visible start state;
2. One primary action;
3. The visible end state.

Avoid stacking multiple unrelated actions into a short clip. “Walks, turns, runs, jumps, opens a door, enters another room, and sits” is a sequence, not one readable shot.

## 3. Give the camera one job

Name the framing, angle, and a motivated movement:

```text
Medium close-up at eye level. The camera makes a slow 20-degree arc to reveal the product label while maintaining the subject at the same scale.
```

Combine movements only when their geometry is compatible. If the camera should stay fixed, say `locked-off camera` and describe motion inside the frame.

## 4. Separate motion sources

Distinguish subject, object, environment, and camera movement:

```text
Subject: the cyclist rides steadily from left to right.
Object: the jacket fabric responds lightly to speed.
Environment: foreground grass bends in intermittent wind.
Camera: lateral tracking at the cyclist's speed, stable horizon.
```

This makes it easier to diagnose a failure without rewriting the whole prompt.

## 5. Lock continuity explicitly

Repeat the visible properties that must not drift:

- Character identity, age range, face, hair, body proportions;
- Wardrobe construction, colors, accessories, and prop hand;
- Product silhouette, materials, label, color, and controls;
- Location geometry, time of day, weather, and lighting direction;
- Screen direction, position, pose, and state at edit points.

“The same person” or “the same product” is weaker than a short list of visible invariants.

## 6. Use timing as beats, not frame-level choreography

Unless a workflow gives precise timeline control, use approximate semantic beats:

```text
Opening beat: recognize the closed package.
Middle beat: the lid opens and one item rises into view.
Final beat: movement settles on the complete product arrangement.
```

Ask for a stable opening or ending when the clip must loop, cut cleanly, or hold a call to action.

## 7. For image-to-video, describe change

The source image already defines composition and appearance. Focus on what begins moving, how much it moves, how the camera behaves, and what must remain untouched. Re-describing the entire image with different adjectives can unintentionally request a redesign.

## 8. Treat text and audio as separate production risks

Only request on-screen text when necessary. Supply approved copy exactly, preserve safe space, and verify every character after generation. For high-stakes text, plan to add typography during editing.

Audio capabilities vary by model and workflow. Write `Audio intent` as creative direction, not a guarantee that the selected video model will generate usable dialogue, music, or sync.

When audio is supplied as a reference, say whether it controls rhythm, ambience, performance intensity, dialogue timing, or another narrow property. Do not request copying a protected recording, melody, lyrics, or voice identity. For synchronized action, map a few structural beats rather than forcing a visual cut on every transient.

## 9. Use precise editing as a change contract

An edit prompt should be shorter and stricter than a generation prompt:

```text
Change only: the desk lamp angle from 30° to 50° during 3.0–4.5s.
Match: the existing hinge pivot, hand contact, exposure, shadow, and room tone.
Preserve exactly: creator identity, lamp design, camera path, timing, desk, window, all other motion and sound.
Success: the lamp reaches 50° and settles without redesign or a new cut.
```

Do not restate the entire creative brief with new adjectives during an edit; that invites a global restyle.

## 10. Make negative constraints observable

Prefer failure-specific constraints:

```text
Avoid: face drift, extra fingers, hand-product fusion, mirrored labels, changing bottle geometry, flickering jewelry, sliding contact points, sudden exposure shifts, duplicate subjects, new text, logos, watermark.
```

Avoid vague instructions such as “no AI look” or “make it perfect.”

## 11. Iterate one failure class at a time

| Pass | Change | Review |
|---|---|---|
| V1 | Subject, action, and composition | Is the idea readable? |
| V2 | Camera and timing | Is movement coherent and motivated? |
| V3 | Continuity and physics | Does identity, geometry, contact, and light stay stable? |
| V4 | Delivery adaptation | Are crop, safe areas, copy space, and playback speed correct? |

Record the prompt, model/tool, settings, date, input assets, seed when available, and manual edits for each published example.

## 12. Multilingual prompting

Translate action, timing, camera, sound, continuity, and negative constraints together. Keep uploaded asset numbering stable and review screen direction separately from text direction. Required copy should remain quoted and be checked by a native speaker. See the [multilingual sampler](./multilingual-prompting.md).

## 13. Final review

- Watch once at normal speed without pausing: is the intended beat clear?
- Watch frame-by-frame: check faces, hands, labels, edges, contact, reflections, and sudden object changes;
- Watch muted and at phone size: verify visual comprehension and crop;
- Verify every claim, number, subtitle, logo, and disclosure;
- Confirm consent, licenses, publicity rights, music/voice rights, and platform policies;
- Export a clean final frame or thumbnail and keep the generation record.

Return to the [main README](../README.md) or use a [production template](../templates/README.md).
