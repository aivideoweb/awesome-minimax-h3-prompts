# MiniMax H3 Video Prompt Library

> 84 original, production-oriented MiniMax H3 audiovisual prompt recipes across 24 practical categories. These recipes originate from the [Flaq AI upstream cookbook](../UPSTREAM.md) and are designed around multimodal reference roles, controllable motion, continuity, and reviewable delivery.

**Prompt languages:** [English canonical library](./README.md) · [Multilingual ready-to-copy sampler](../docs/multilingual-prompting.md)

## Browse all 84 recipes

| ID range | Collection | Recipes | Typical work |
|---|---|---:|---|
| BRD-001—003 | [Brand and advertising](./01-brand-advertising.md) | 3 | Brand films, launch ads, campaign adaptations |
| PRD-001—003 | [Product and e-commerce](./02-product-ecommerce.md) | 3 | Packshots, feature demos, marketplace clips |
| UGC-001—003 | [UGC and lifestyle](./03-ugc-lifestyle.md) | 3 | Creator demos, routines, credible testimonials |
| TRV-001—003 | [Travel and hospitality](./04-travel-hospitality.md) | 3 | Destinations, hotels, local experiences |
| FNB-001—003 | [Food and beverage](./05-food-beverage.md) | 3 | Preparation, service, texture and restaurant stories |
| FSH-001—003 | [Fashion and beauty](./06-fashion-beauty.md) | 3 | Editorial motion, beauty macro, outfit transitions |
| CIN-001—003 | [Cinematic storytelling](./07-cinematic-storytelling.md) | 3 | Character drama, mystery, emotional narrative |
| ANI-001—003 | [Animation and stylized video](./08-animation-stylized.md) | 3 | Paper, clay, graphic and illustrated motion |
| ACT-001—003 | [Action and sports](./09-action-sports.md) | 3 | Athletic movement, pursuits, physical performance |
| VFX-001—003 | [Fantasy, sci-fi and VFX](./10-fantasy-scifi-vfx.md) | 3 | Transformations, impossible worlds, visual effects |
| DIG-001—003 | [UI, game and digital experience](./11-ui-game-digital.md) | 3 | Product UI, game interfaces, interactive demos |
| SOC-001—003 | [Transitions, comedy and social formats](./12-transitions-comedy-social.md) | 3 | Match cuts, visual jokes, loops and short-form hooks |
| MUS-001—004 | [Music, performance and audio-driven video](./13-music-performance-audio.md) | 4 | Live sessions, multilingual vocals, choreography, visualizers |
| EDU-001—004 | [Education, documentary and science](./14-education-documentary-science.md) | 4 | Science, museum, training and scale explainers |
| ARC-001—004 | [Architecture, interiors and real estate](./15-architecture-interiors-real-estate.md) | 4 | Walkthroughs, light studies, renovation and smart home |
| MOB-001—004 | [Automotive and mobility](./16-automotive-mobility.md) | 4 | Vehicle UI, cycling, rail and delivery robotics |
| NAT-001—004 | [Nature, animals and pets](./17-nature-animals-pets.md) | 4 | Wildlife, pet care, plant growth and marine macro |
| IND-001—004 | [Industry, business and public service](./18-industry-business-public-service.md) | 4 | Assembly, logistics, safety and multilingual service |
| EDT-001—004 | [Editing, continuation and localization](./19-editing-continuation-localization.md) | 4 | Cleanup, extension, localization and relighting |
| MRF-001—004 | [Multi-reference and camera transfer](./20-multireference-camera-transfer.md) | 4 | One-takes, motion grammar, match actions and tutorials |
| CHR-001—004 | [Character, dialogue and performance](./21-character-dialogue-performance.md) | 4 | Exact dialogue, micro-emotion, bilingual and ensemble scenes |
| MOG-001—004 | [Motion graphics and dynamic posters](./22-motion-graphics-dynamic-posters.md) | 4 | Poster builds, feature cards, exhibition openers and idents |
| SRL-001—004 | [Surreal physics and optical illusions](./23-surreal-physics-optical-illusions.md) | 4 | Practical surrealism, time offsets, reflections and material changes |
| VER-001—004 | [Vertical series and live creator](./24-vertical-series-live-creator.md) | 4 | Live demos, micro-drama, recurring formats and audience answers |

## H3-oriented recipe design

MiniMax's official H3 materials emphasize native text/image/audio/video understanding, precise multimodal editing and control, and commercial use across film, advertising, e-commerce, digital experiences, games, and animation. Recipes therefore separate four layers:

1. **Reference map:** what each image, video, or audio input is allowed to control;
2. **Creative brief:** deliverable, audience, story, visual language, and sound intent;
3. **Timeline:** readable beats, camera behavior, and state changes;
4. **Control contract:** identity locks, product locks, edit scope, constraints, and review risks.

The recipes do not invent API parameters. Confirm currently supported input types, model identifiers, limits, and request fields in the [official MiniMax H3 examples](https://platform.minimaxi.com/docs/guides/video-prompt) and [video generation documentation](https://platform.minimaxi.com/docs/guides/video-generation).

## How to use a recipe

1. Pick the closest deliverable, not just the closest visual style.
2. Replace every `[bracketed variable]`; remove unused reference inputs.
3. Keep reference roles narrow: identity, product, location, movement, rhythm, or sound—not “use everything from everything.”
4. Shorten or expand the timeline to match the duration available in your H3 interface.
5. Generate a structure pass first; then revise motion, identity, text, or sound one failure class at a time.
6. Verify the final output at normal speed, frame by frame, muted, and at delivery size.

## Canonical recipe format

````markdown
## BRD-000 English title

**Use it for:** One precise delivery goal.

**Mode:** Text / image / audio / video references as needed

**Format:** Aspect ratio and target duration

**Reference map:** Image 1 = identity; Image 2 = product; Video 1 = movement only; Audio 1 = rhythm only.

```text
[Deliverable]
[Creative direction]
[Timeline]
[Continuity and edit locks]
[Sound intent]
[Avoid]
```

**Review:** The failure modes that matter for this recipe.
````

All entries are creative specifications. A recipe is only marked as tested after its exact model/tool, inputs, settings, date, output, and material edits are recorded.

Use the [model-neutral H3 reference-image briefs](../assets/minimax-h3-reference-image-prompts.md) to create original first frames and references, read the [H3 overview and official links](../docs/minimax-h3-overview.md), or return to the [main README](../README.md).
