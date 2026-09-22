# Architecture, Interiors and Real-Estate Video Prompts

Original MiniMax H3 prompts for spatial reveals, property walkthroughs, renovation concepts, and interior product stories. Do not fabricate amenities, dimensions, views, or regulatory claims.

## ARC-001 Honest Small-Apartment Walkthrough

**Status:** Concept — not independently tested

**Use it for:** A continuous property tour that preserves the real floor plan and avoids deceptive wide-angle distortion.

**Mode:** Floor plan + room reference images + optional path video  \
**Format:** 9:16, target 15 seconds  \
**Reference map:** Image 1 = verified floor plan; Images 2–5 = exact finishes and fixed features; Video 1 = walking route and camera height only.

```text
Create a vertical, single-path walkthrough of the documented studio apartment. Follow Image 1 exactly: enter through the short hall, pass the bathroom door on screen right, reveal the kitchenette on screen left, then finish at the living area window. Preserve wall openings, ceiling height, built-in storage, flooring, fixtures, and the actual exterior view from Images 2–5.

Camera moves at natural adult walking height with a moderate field of view and gentle stabilization. Pause briefly at the kitchenette so counter depth is readable; continue without passing through furniture or walls. At the window, rotate no more than 45 degrees to show the living/sleeping zone and end with a truthful wide frame. Keep daylight direction and object positions consistent.

Sound intent: room tone, soft footsteps, distant street ambience, no sales voiceover. Avoid stretching rooms, removing columns, adding furniture that changes usable area, inventing a balcony or skyline, opening impossible doors, generated price text, logos, agents, or watermark.
```

**Review:** Floor-plan fidelity, lens honesty, exterior view, route continuity, and absence of invented amenities.

## ARC-002 Courtyard Cafe Morning-to-Evening Study

**Status:** Concept — not independently tested

**Use it for:** An architecture mood film showing how one space changes with light and occupancy.

**Mode:** Site images + material board + optional sun-path diagram  \
**Format:** 16:9, target 12 seconds  \
**Reference map:** Images 1–3 = courtyard geometry; Image 4 = exact materials; Image 5 = verified sun direction only.

```text
Create a time-compressed spatial portrait of a fictional courtyard café while preserving architecture. Begin at opening time with cool daylight entering from the east, empty oak tables, folded canvas awnings, and staff placing ceramic cups. Camera makes one slow lateral move along the arcade. Use seamless light changes at fixed spatial anchors: a brick pier, the central olive tree, and the fountain edge.

At midday, soft leaf shadows travel across lime plaster; a small, varied group occupies only the documented seating. By early evening, practical wall lights turn on one by one and the same move concludes at the fountain, now reflecting warm light. People must appear and leave through plausible paths rather than popping into place.

Sound intent: morning broom and birds evolving into low conversation and evening water; no recognizable song. Preserve materials, table count, door positions, tree scale, sun direction, and accessible circulation. Avoid fantasy renovation, impossible sunlight, crowd duplication, fabricated signage, lifestyle stereotypes, or watermark.
```

**Review:** Geometry, sun logic, occupancy continuity, acoustic progression, accessibility, and material fidelity.

## ARC-003 Renovation Concept With Before/After Boundary

**Status:** Concept — not independently tested

**Use it for:** A design concept film that makes proposed changes visually clear without presenting them as completed work.

**Mode:** Existing-room images + approved concept render + material references  \
**Format:** 4:5, target 10 seconds  \
**Reference map:** Image 1 = surveyed existing room; Image 2 = approved proposal; Images 3–4 = specified material appearance only.

```text
Create a clearly labeled-in-post renovation concept for a small community reading room. Start with the existing condition from Image 1: fixed windows, radiator, structural beam, worn floor, and current door remain exact. Camera is locked on a measured corner view.

A moving vertical light boundary travels from left to right. Behind the boundary only approved proposal elements from Image 2 appear: repaired timber floor, low movable shelves, acoustic ceiling panels, two reading lamps, and accessible clear circulation. Structural openings, room dimensions, exterior view, and radiator do not change. Once the boundary reaches the right edge, hold the proposed-state visualization for two seconds with empty top-left space for “concept” labeling added in post.

Sound intent: quiet paper movement and one restrained transition sweep. Avoid demolition spectacle, extra windows, luxury furniture, increased room size, hidden radiator, invented accessibility certification, generated labels, people, or watermark.
```

**Review:** Existing/proposed distinction, scope fidelity, fixed elements, material match, and disclosure space.

## ARC-004 Smart-Home Evening Sequence

**Status:** Concept — not independently tested

**Use it for:** A connected-home demonstration where each physical action produces one visible, verifiable state change.

**Mode:** Room images + device images + approved interaction map  \
**Format:** 16:9, target 12 seconds  \
**Reference map:** Images 1–2 = room and lighting layout; Images 3–5 = exact devices; Text 1 = approved input-to-state mapping.

```text
Produce an evening smart-home demonstration in a fictional living room. Preserve the exact lamp, blind motor, wall control, and room geometry from the references. Show three causal beats only.

Beat 1: close view of an adult hand pressing the upper wall-control button once; the ceiling light smoothly dims from neutral white to 30 percent warm light. Beat 2: medium room view as the lower button is pressed; the existing blinds close evenly from their current position, with outdoor light reducing naturally. Beat 3: a small tabletop control is rotated clockwise; the floor lamp turns on and stops at the approved amber level. End on a wide room state matching the approved interaction map.

Camera cuts only after each input is visible. Sound intent: tactile clicks, quiet blind motor, room ambience, no voice assistant or claims. Keep button identity, hand anatomy, light direction, device count, cable placement, and state order stable. Avoid invented automation, surveillance implication, floating interfaces, brand logos, readable generated text, or watermark.
```

**Review:** Input/output causality, device geometry, lighting continuity, privacy framing, and claim accuracy.
