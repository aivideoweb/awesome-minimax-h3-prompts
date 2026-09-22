# Source and maintenance

This VideoWeb AI edition adapts [Flaq AI's MiniMax H3 cookbook](https://github.com/flaqai/awesome-minimax-h3-video-prompts) under its MIT license.

- Imported revision: `9fed21c196ffa5495b8f6d8de29cc77ba71eb66d`
- Import date: September 22, 2026
- Retained: all 84 recipes in 24 categories, production templates, eight README languages, multilingual prompting and deployment guides, official examples and attributed X community sources.
- Adapted: VideoWeb entry links, introductions across all eight README pages, maintainer identity, affiliate guide, repository contribution links and a new editorial cover.
- Eleven unbranded gallery references are reused from upstream. Their production records belong to the upstream project; they are not newly generated VideoWeb examples.
- The upstream cover is replaced. The twelve-asset total now means eleven inherited gallery images plus one VideoWeb cover.
- Expanded the attributed X showcase from six to fifteen cases, with a source manifest and frame-sampling review.
- Historical third-party tool links remain in [other H3 tools](./docs/other-h3-tools.md).

Copyright and permission notices are retained in [LICENSE](./LICENSE). Official and community media keep their own rights and attribution; the repository MIT license does not relicense them. Prompt recipes are concepts unless a specific generation record says otherwise.

## Maintain this edition

1. Compare upstream changes against the revision above; inspect recipe, reference and documentation changes separately from branding.
2. Keep all upstream copyright notices. Preserve authors, source links and recorded verification dates.
3. Update VideoWeb availability and affiliate terms from the linked product pages; do not copy another provider's claims into VideoWeb documentation.
4. Add new recipes to the category file, prompt index and use-case matrix together. Update counts and the cover when totals change.
5. Run `python3 scripts/check_content.py` and `git diff --check` before opening a pull request. Review the rendered README and images as well.
6. Record the imported revision, date, meaningful changes and actual generation tests in this file and the changelog. A content check is not a video quality test.
