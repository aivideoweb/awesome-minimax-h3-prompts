# MiniMax Video API Workflow

This page records the stable, high-level integration flow needed to connect prompt recipes to MiniMax's video platform. MiniMax now publishes an official H3 capability page, while model identifiers and request fields remain provider-controlled and changeable. Creative H3 reference maps are therefore kept separate from API configuration.

See the [official H3 capability examples](https://platform.minimaxi.com/docs/guides/video-prompt) for multimodal creative workflows and the [official video generation guide](https://platform.minimaxi.com/docs/guides/video-generation) for currently documented request modes and fields.

For downloadable use, start with the official [MiniMax-AI/MiniMax-H3 repository](https://github.com/MiniMax-AI/MiniMax-H3), [model card and open weights](https://huggingface.co/MiniMaxAI/MiniMax-H3), and this project's [multilingual deployment guide](./deployment-guide.md). Open-weight checkpoints and hosted product/API features are separate integration surfaces; do not assume identical task coverage, preprocessing, acceleration, limits, or outputs.

## Official workflow

MiniMax's official guide documents four video generation modes:

1. Text-to-video;
2. Image-to-video using a first frame;
3. First-and-last-frame video;
4. Subject-reference video.

Generation is asynchronous:

1. Submit a generation request and store the returned task ID;
2. Poll the task-status endpoint at a reasonable interval;
3. On success, use the returned file ID to retrieve the output;
4. Download and archive the video together with its generation record.

The H3 product experience can accept richer combinations of text, image, audio, and video references than the four API examples above. Do not assume that a capability shown in a product interface uses the same request schema as the public API; verify the current integration surface before implementation.

## Keep prompt content separate from API configuration

Store these as two layers:

```text
Creative specification
- prompt text
- image, video, and audio reference roles
- reference conflict priority
- continuity and safety constraints
- precise edit scope
- delivery intent

Request configuration
- current official model identifier
- supported generation mode
- duration and resolution
- input asset URLs or encoded data
- provider-specific optional fields
```

This separation lets the cookbook remain useful when model identifiers or API fields change.

## Hosted API versus open-weight workflow

| Concern | Hosted MiniMax workflow | Open-weight/local workflow |
|---|---|---|
| Source of truth | Current platform and API docs | Current H3 model card, release files, license and runtime docs |
| Identifier | Exact API model string | Exact checkpoint/task variant and revision |
| Inputs | Only fields accepted by the endpoint | Only modalities supported by the selected checkpoint and pipeline |
| Infrastructure | Provider-managed | User-managed hardware, storage, dependencies and optimization |
| Record | Task ID, file ID, request settings | Checkpoint, revision, runtime, hardware, settings and output hashes |
| Capability claims | What the current endpoint documents | What the downloaded release and tested runtime actually demonstrate |

Use [T12](../templates/README.md#t12-open-weightlocal-generation-record) to make local examples reproducible.

## Suggested generation record

```yaml
recipe_id: BRD-001
recipe_version: 1
generated_at: YYYY-MM-DD
provider: MiniMax
model: <exact model identifier returned/accepted by the API>
mode: text-to-video
duration: <requested value>
resolution: <requested value>
aspect_ratio: <delivery ratio>
input_assets:
  - <file name, URL, or content hash>
prompt: |
  <exact submitted prompt>
result:
  task_id: <optional; remove before public sharing if sensitive>
  file_name: <local artifact name>
review:
  status: pass | needs-revision
  notes:
    - <observed issue or manual edit>
```

Never commit API keys, authorization headers, private input URLs, personal data, or expiring download URLs.

## Version and capability policy

- Copy model identifiers and accepted parameters from the current official documentation;
- Record the exact model used for every tested prompt;
- Label untested prompt recipes as concepts;
- Treat limits, prices, duration, resolution, and available modes as changeable provider data;
- Link H3 capability claims to the official capability page;
- Add H3 request examples only when model identifiers and parameters can be verified against the official integration surface being used.
- Keep hosted and open-weight results clearly labeled; do not attribute one workflow's behavior to the other.

Return to the [main README](../README.md), read the [H3 overview](./minimax-h3-overview.md), or follow the [deployment guide](./deployment-guide.md).
