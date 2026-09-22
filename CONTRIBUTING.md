# Contributing

Thank you for helping build Awesome MiniMax H3 Video Prompts. The project accepts original, reusable, reviewable material with clear provenance.

## Good first contributions

- Test an existing original recipe and submit a complete generation record;
- Propose an original fourth recipe in a category with a clear production gap;
- Improve a production template or failure-mode checklist;
- Add a verified link to primary MiniMax documentation;
- Fix unclear language, broken links, or inconsistent IDs;
- Submit an original example with a complete generation record.

Use an issue before making a large taxonomy change, adding many media files, or introducing a new language edition.

## Three ways to contribute

1. **Propose:** use the [guided prompt proposal](https://github.com/aivideoweb/awesome-minimax-h3-prompts/issues/new?template=prompt-proposal.yml) when you have a complete original idea but do not want to edit repository files.
2. **Test:** run an existing recipe, then submit the exact model/tool, inputs, settings, date, edits, defects, and rights-cleared output record.
3. **Build:** open a pull request for a finished recipe, translation, checklist, documentation correction, or original media package.

Concept recipes are welcome; a generated video is not required. Tested status is awarded only when the execution record is complete enough for another contributor to understand what was actually run.

## Prompt requirements

For an external X example, use the separate [community showcase](./docs/x-community-showcase.md) and [provenance policy](./docs/originality-policy.md#attributed-community-showcase). Supply the original post, creator, video, prompt location and verification notes. Use a short quotation with a full-prompt source link; label editorial analysis and missing references. External examples must not be submitted as original recipes or added to their counts.

### Original recipe route

Every prompt recipe must include:

1. A unique ID using the category prefix;
2. A clear English title and one-sentence delivery goal;
3. Generation mode, format, and concept/tested status;
4. A complete copy-ready prompt rather than a keyword list;
5. Start state, primary action, end state, camera, and timing;
6. Continuity locks, constraints, and likely failure modes;
7. Production notes and input assumptions;
8. For tested entries, the exact model/tool, settings, date, and material edits.

Use the canonical format in [prompts/README.md](./prompts/README.md#canonical-recipe-format).

### Attributed community example route

Use the external-showcase change type in the pull-request template. Provide the creator, original post, prompt location, media URLs, retrieval method, check date, missing inputs and observed limitations. Keep quotations short and link the full prompt at its source. Preserve attribution; do not claim ownership or blanket redistribution rights over linked works. The original-recipe identity restrictions below do not apply to this route. Never include unlicensed media files, private data or credentials.

## ID policy

| Prefix | Category |
|---|---|
| `BRD` | Brand and advertising |
| `PRD` | Product and e-commerce |
| `UGC` | UGC and lifestyle |
| `TRV` | Travel and hospitality |
| `FNB` | Food and beverage |
| `FSH` | Fashion and beauty |
| `CIN` | Cinematic storytelling |
| `ANI` | Animation and stylized video |
| `ACT` | Action and sports |
| `VFX` | Fantasy, sci-fi and VFX |
| `DIG` | UI, game and digital experience |
| `SOC` | Transitions, comedy and social formats |
| `MUS` | Music, performance and audio-driven video |
| `EDU` | Education, documentary and science |
| `ARC` | Architecture, interiors and real estate |
| `MOB` | Automotive and mobility |
| `NAT` | Nature, animals and pets |
| `IND` | Industry, business and public service |
| `EDT` | Editing, continuation and localization |
| `MRF` | Multi-reference and camera transfer |
| `CHR` | Character, dialogue and performance |
| `MOG` | Motion graphics and dynamic posters |
| `SRL` | Surreal physics and optical illusions |
| `VER` | Vertical series and live creator |

IDs are assigned sequentially and never reused. Ask a maintainer to confirm the next ID when another pull request could conflict.

## Content excluded from original recipe submissions

- Prompts copied or lightly rewritten from another repository, social account, course, or paid pack;
- Content retaining another author's name, handle, watermark, tracking link, or promotion;
- Unauthorized celebrity, private-person, protected-character, brand, voice, or campaign imitation;
- Deceptive testimonials, fake evidence, fraudulent ads, or misleading medical/financial claims;
- Vague keyword piles with no executable motion, camera, time, or continuity specification;
- Media with unclear ownership, consent, or redistribution rights;
- Claims about model capabilities that cannot be verified from a primary source.

Common use cases are not owned by a prompt collection, but wording, story details, reference mappings, characters, brands, shot design, examples, and media can be protected or attributable. Contributions must independently author all of those expressive elements.

## Tested examples

A tested example must be original and must document:

- Exact submitted prompt;
- Exact model identifier and tool/provider;
- Generation mode and supported settings;
- Input assets, ownership, and consent;
- Date generated and useful iteration notes;
- Manual editing, compositing, typography, audio, or cleanup;
- Known defects and review result.

Follow [assets/README.md](./assets/README.md). Never commit credentials, private URLs, personal data, or unlicensed media.

## Pull request checklist

Complete the items applicable to your contribution route; mark unrelated items as not applicable. Linking an external work does not mean you own it.

- [ ] For original recipes and owned assets: I have the rights and consent needed to submit my original material under MIT;
- [ ] For original recipes and owned assets: the contribution is independently authored and does not reuse external author/platform identity;
- [ ] For external showcases: creator attribution, original source, prompt location and verification limits are recorded; third-party works are not presented as original recipes or MIT assets;
- [ ] Facts and capability claims link to reliable primary sources;
- [ ] The prompt is understandable without hidden conversation context;
- [ ] Original recipes use the correct category, ID, status and recipe structure; external examples use the separate source manifest and showcase;
- [ ] Required text, claims, product details, and safety constraints were checked;
- [ ] New files are linked from an index and all relative Markdown links work;
- [ ] Tested examples disclose model/tool, inputs, settings, edits, and known limitations.

Your original contribution text, code and owned assets are submitted under this repository’s MIT License. Linked or quoted third-party prompts and media retain their owners’ rights and are not relicensed by your submission. Do not claim rights you do not hold.

## Before opening a pull request

Run `python3 scripts/check_content.py` and `git diff --check` from the repository root. Keep recipe IDs, category counts, README entries and source records in sync. For X examples, update both the JSON manifest and the bilingual showcase, link the author’s actual prompt location, and preserve playback notices.

Review the rendered page and images after the automated checks. Source imports follow [UPSTREAM.md](./UPSTREAM.md); content checks do not establish video generation quality.
