# MiniMax H3 with VideoWeb AI

[English](#english) · [简体中文](#简体中文)

## English

### Choose the right entry

| Your goal | Where to start | What to check |
|---|---|---|
| Try one shot without creating an account | [Free MiniMax H3](https://videoweb.ai/free-minimax-h3/) | The page lists 480p, 5 seconds, text or an optional start/end image pair |
| Use H3 for regular browser-based creation | [VideoWeb AI MiniMax H3](https://videoweb.ai/model/minimax-h3/) | Select the settings currently offered; confirm credits and access before generating |
| Reproduce advanced multi-reference or local workflows | [Deployment guide](./deployment-guide.md), [official examples](./official-h3-examples.md) | Confirm the selected tool supports each required image, video and audio input |

Page information checked September 22, 2026. These are access instructions, not a generation benchmark or an uptime guarantee. No video was generated as part of this adaptation.

### Make a first clip

1. Open the free tool. For a first attempt, leave the image fields empty and use the text below.
2. Choose an available aspect ratio for your destination. The prompt below targets a five-second shot; do not paste a longer recipe unchanged.
3. Generate once and wait for the result. Review the clip before revising.
4. If using image guidance instead, upload both the opening and closing image in that order. A single gallery image is not a complete pair; create a compatible ending frame first.
5. Download the result when available and record the prompt, date, settings and any visible defects using the [generation record](./api-workflow.md#suggested-generation-record).

```text
A five-second single continuous shot of a fictional unbranded blue glass bottle on a dark studio plinth. 0–1 seconds: hold a medium close-up, bottle fully visible. 1–4 seconds: the camera slowly moves closer while a soft side light reveals the glass texture; the bottle remains still. 4–5 seconds: settle into a clean product frame. Keep bottle shape, cap, color and background unchanged. No cuts, rotation, added objects, lettering or logos. Sound intent: quiet studio ambience, no speech or music.
```

This is an untested simplified starter, not a verified output of [BRD-001](../prompts/01-brand-advertising.md#brd-001-midnight-observatory-tea-launch). The full recipe adds a location, more timing detail and reference roles.

### Pick your next recipe

| Need | Starting recipe | First adaptation |
|---|---|---|
| Product reveal | [BRD-001](../prompts/01-brand-advertising.md#brd-001-midnight-observatory-tea-launch) | Keep one reveal; remove extra story beats |
| Creator demonstration | [UGC-001](../prompts/03-ugc-lifestyle.md#ugc-001-desk-lamp-honest-first-impression) | Keep one visible action; omit unsupported dialogue |
| Travel atmosphere | [TRV-001](../prompts/04-travel-hospitality.md#trv-001-rain-washed-canal-town-morning) | Keep one camera move and a stable location |
| Character animation | [ANI-002](../prompts/08-animation-stylized.md#ani-002-clay-repair-robot-finds-a-button) | Keep one gesture and lock character appearance |
| Advanced editing or reference control | [Workflow matrix](./use-case-matrix.md) | Choose a compatible workflow before preparing inputs |

### Fix a failed draft

| Visible problem | Next revision |
|---|---|
| Product changes shape | Remove rotation, simplify the camera move, specify which features stay fixed |
| Too much happens in five seconds | Keep one action and one ending; split the rest into separate clips |
| Text is unreadable | Generate a clean text-free panel and add verified copy in an editor |
| Image pair causes a jump | Match subject scale, viewpoint and lighting between the two images |
| Dialogue is too fast | Shorten or remove dialogue; do not assume audio-upload or lip-sync controls exist |
| No result or queue error | Check the visible status before retrying; save the prompt and any error message |

Review identity, product shape, motion, camera direction, sound and final-frame usefulness. Only call a recipe tested after recording an actual result. Browse [all 84 recipes](../prompts/README.md), [production templates](../templates/README.md), or the [historical directory of other tools](./other-h3-tools.md).

## 简体中文

### 先选入口

- **免注册试用：**打开[免费 MiniMax H3](https://videoweb.ai/free-minimax-h3/)。页面目前标明 480p、5 秒，可输入文字，也可选传首尾两张图片。
- **日常制作：**使用 [VideoWeb AI MiniMax H3](https://videoweb.ai/model/minimax-h3/)，生成前确认页面提供的设置、积分和使用条件。
- **复杂参考或本地运行：**查看[部署指南](./deployment-guide.md)和[官方案例](./official-h3-examples.md)。先确认工具支持所需的视频、音频或图片输入，再准备素材。

以上页面信息核对于 2026 年 9 月 22 日；本次没有实际生成视频，也未测试服务稳定性。

### 做第一个短片

1. 打开免费工具，首次尝试可不上传图片，直接复制下方文字。
2. 选择页面可用的画面比例。先做一个 5 秒单镜头，不要直接粘贴完整的长时间线。
3. 提交后等待结果，先检查成片再修改。
4. 若用图片引导，按顺序上传起始图和结束图。图库里的一张首帧图不等于完整的首尾帧组合，需要另外准备构图相容的结束图。
5. 下载可用结果，记录提示词、日期、设置和缺陷；模板见[制作记录](../templates/README.md)。

```text
5 秒连续单镜头：一只虚构、无品牌的蓝色玻璃瓶放在深色摄影台上。0–1 秒：中近景静止展示，瓶身完整入画。1–4 秒：镜头缓慢推进，柔和侧光显出玻璃质感，瓶子始终不动。4–5 秒：镜头停稳，留下清楚的产品画面。瓶形、瓶盖、颜色和背景保持一致。不切镜头，不旋转瓶身，不增加物体、文字或标志。声音意图：安静的室内环境声，不要人声或音乐。
```

这是未经生成测试的入门示例。完整的[产品广告提示词](../prompts/01-brand-advertising.md)包含更丰富的场景、参考素材职责和时间线；免费短片应先保留一个动作。

产品变形时先取消旋转、简化运镜；5 秒内动作过多时拆成多个镜头；文字不清楚时保留空白区域，在剪辑软件中添加；首尾帧跳变时统一主体大小、视角和光线。出现排队或报错时先读取当前状态，保留提示词和错误信息再决定是否重试。

最后检查主体是否一致、产品是否变形、动作是否连贯、声音是否合适、结尾是否可用。只有保存了实际结果和记录，才把提示词标为已测试。

[返回中文首页](../README_zh.md) · [全部 84 条提示词（英文）](../prompts/README.md) · [多语言提示词](./multilingual-prompting.md)
