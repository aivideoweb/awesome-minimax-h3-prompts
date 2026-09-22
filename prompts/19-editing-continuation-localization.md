# Editing, Continuation and Localization Video Prompts

Original MiniMax H3 prompts for narrow-scope video edits, natural continuation, relighting, and multilingual adaptation. Treat the source video as protected material: name exactly what may change, repeat what must stay fixed, and review the result against the source frame by frame.

## EDT-001 Clear the Background, Preserve the Lead

**Status:** Concept — not independently tested

**Use it for:** Removing distracting background people from an otherwise approved performance take without changing the lead or camera.

**Mode:** Source video + optional clean location plate + lead identity reference  
**Format:** Preserve source aspect ratio, duration, frame rate, and audio sync  
**Reference map:** Video 1 = immutable lead performance, timing, framing, and camera path; Image 1 = clean empty location geometry; Image 2 = consenting adult lead identity and wardrobe.

```text
Edit Video 1 by removing only the five background pedestrians who cross behind the lead performer. Reconstruct the newly exposed pavement, tiled wall, closed kiosk, and reflections from Image 1. Preserve the lead performer pixel-consistently in position, identity, face, hair, wardrobe, body shape, gestures, walking cadence, gaze, lip movement, contact shadows, and occlusions. Preserve the original camera path, focal behavior, motion blur, exposure, crop, duration, edit points, and every foreground prop.

The lead walks from screen left to screen right and pauses beside the blue bench exactly as in Video 1. Do not retime or regenerate this action. When a removed pedestrian briefly overlaps the lead's coat edge, restore the coat from adjacent source frames and Image 2; keep the original fabric motion and edge softness. Rebuild only the vacated background region with temporally stable texture and matching parallax.

Audio scope: keep the original lead dialogue, footsteps, music, and room tone. Attenuate only identifiable background speech associated with the removed pedestrians, then fill the gap with matched ambient tone. Avoid changing the lead voice, inventing words, freezing background texture, duplicating passersby, warping the bench, shifting shadows, adding signs, beautifying the face, or introducing a watermark.
```

**Review:** Difference-mask the lead and fixed foreground, inspect every former occlusion edge, and compare camera motion, shadows, lip sync, and audio continuity with the source.

## EDT-002 Extend a Repair-Café Closing Moment

**Status:** Concept — not independently tested

**Use it for:** Continuing an approved clip into a resolved ending while preserving its cast, setting, sound field, and camera logic.

**Mode:** Source video + character references + object detail images + approved continuation beats  
**Format:** Match source ratio; generate an 8-second continuation clip beginning from the last source frame  
**Reference map:** Video 1 = immutable opening footage and continuation boundary; Images 1–2 = consenting adult identities and wardrobe; Images 3–4 = exact fictional tabletop radio and tool tray; Audio 1 = source room tone only.

```text
Generate a continuation clip beginning exactly from Video 1's final frame; do not regenerate or replace the existing source clip. Match the locked camera height, slow handheld drift, warm practical lighting, repair-café tables, window reflections, people, wardrobe, radio geometry, tool positions, grain, exposure, and Audio 1 room tone.

Continuation beat 1, first 2 seconds: the technician releases the same tuning knob, moves both hands away, and looks toward the customer. The radio remains in the same place and orientation. Beat 2, next 3 seconds: the customer leans in, presses the single top button once, and the existing amber indicator turns on; a quiet fictional instrumental station fades in with no recognizable song. The technician listens and gives one restrained nod. Beat 3, final 3 seconds: the customer smiles, slides the radio into the existing padded tote, and closes the tote flap. The camera eases back by a few centimeters and holds on the now-clear work mat.

Keep hand ownership, radio scale, button location, tool count, eyelines, screen direction, and sound perspective continuous across the source boundary. Do not add dialogue, brand marks, readable station data, new customers, extra tools, impossible electronics, a second radio, a camera cut, a lighting jump, or a watermark.
```

**Review:** Source-to-extension seam, face and wardrobe identity, object mechanics, hand contact, indicator causality, room-tone match, and final-state clarity.

## EDT-003 Localize a Product Tutorial Without Re-Shooting

**Status:** Concept — not independently tested

**Use it for:** Adapting an approved talking tutorial to another language while retaining the demonstrator, product action, timing, and truthful claims.

**Mode:** Source video + authorized voice reference + approved translated script + clean graphic plates  
**Format:** Preserve source format and duration; target language selected at delivery  
**Reference map:** Video 1 = immutable presenter, product, hands, framing, and step timing; Audio 1 = authorized presenter voice identity; Text 1 = approved target-language script; Images 1–3 = exact clean graphic plates for later compositing.

```text
Create a localized version of Video 1 using the complete approved script in Text 1. Preserve the adult presenter's identity, age, skin texture, hair, wardrobe, body position, gestures, product geometry, hand-object contact, step order, camera, cuts, background, exposure, and total duration. Replace only the spoken language and the mouth movement needed to match it. Use Audio 1 only for the authorized speaker's vocal identity; keep a natural pace and pronunciation for the target locale.

The three product actions must still land on their original moments: unfold the handle, rotate the selector one click clockwise, and place the device on its base. Do not change or imply any feature beyond the approved script. Remove the source-language lower thirds cleanly and leave the three supplied graphic areas blank for exact typography to be composited from Images 1–3 after generation.

Mix the new dialogue at the same perceived distance as the source; preserve room tone and action sounds. Duck background music only when needed for intelligibility. Do not translate brand names, serial numbers, legal copy, or units unless Text 1 explicitly supplies the approved form. Avoid voice swapping, a second speaker, extra claims, paraphrased safety instructions, lip jitter, altered hands, baked-in generated text, new cuts, or watermark.
```

**Review:** Native-speaker approval, word-for-word script match, lip sync, action timing, claim scope, units, graphic safe areas, and preserved product mechanics.

## EDT-004 Relight an Office Demo, Change Nothing Else

**Status:** Concept — not independently tested

**Use it for:** Turning a daytime smart-light demonstration into an evening version through a tightly bounded environmental edit.

**Mode:** Source video + approved evening lighting plate + device-state reference  
**Format:** Preserve source ratio and duration, target 12 seconds  
**Reference map:** Video 1 = immutable room, actor, action, camera, and geometry; Image 1 = approved evening exterior and color temperature; Image 2 = exact device on/off states.

```text
Edit only the lighting and verified device states in Video 1. Keep the office architecture, furniture, window geometry, adult actor identity, wardrobe, posture, gestures, hand contacts, camera movement, lens, focus pulls, timing, crop, and every object unchanged.

Transform the exterior from overcast afternoon to the approved blue-hour view in Image 1. Dim the existing daylight gradually while keeping physically consistent window reflections and shadow directions. At the exact source moment when the actor presses the wall control, switch the two desk lamps from off to the warm state in Image 2; their light must affect nearby surfaces and the actor naturally. Keep the ceiling fixture off for the entire clip. End with the same composition and object positions as Video 1, now balanced between cool window light and warm desk lamps.

Preserve original dialogue, button click, room tone, and music. Do not move the sun visibly, change weather, add city landmarks, alter the interface, invent an energy-saving claim, change furniture, beautify the actor, add new light fixtures, reshape reflections, retime the press, or add text, logos, and watermark.
```

**Review:** Edit boundary, geometry lock, switch-to-light causality, shadow direction, reflections, skin tone, dialogue sync, and absence of invented performance claims.
