# Awesome MiniMax H3 视频提示词 — VideoWeb AI

为广告、产品、人物故事和短视频挑选提示词，查看真实发布案例，再按你的镜头需求修改。

**84 条提示词 · 24 个分类 · 15 条社区视频案例**

**[挑选提示词](#choose-a-prompt) · [看视频与提示词](#watch-examples) · [试做 5 秒镜头](#try-a-shot)**

**语言：** [English](./README.md) · [简体中文](./README_zh.md) · [日本語](./README_ja.md) · [한국어](./README_ko.md) · [Español](./README_es.md) · [Français](./README_fr.md) · [Deutsch](./README_de.md) · [Português](./README_pt.md)

更多内容：[全部 24 个分类](#full-catalog) · [11 张参考图](#reference-images) · [制作模板](./templates/README.md) · [部署指南](./docs/deployment-guide.md)

**参与共建：** [提交提示词](https://github.com/aivideoweb/awesome-minimax-h3-prompts/issues/new?template=prompt-proposal.yml) · [改进文档](https://github.com/aivideoweb/awesome-minimax-h3-prompts/issues/new?template=documentation.yml) · [发起合并请求](https://github.com/aivideoweb/awesome-minimax-h3-prompts/pulls)

<img src="./assets/hero-minimax-h3-video-prompts.webp" alt="VideoWeb AI MiniMax H3 提示词库封面" width="960">

提示词正文以英文为主；[多语言示例](./docs/multilingual-prompting.md)提供中文等 8 种语言。84 条提示词与 11 张参考图继承自源库，VideoWeb 新增品牌封面及使用指南，详见[来源说明](./UPSTREAM.md)。

84 条配方由源库独立创作；15 条 X 社区案例作为外部学习材料单独收录，不计入这 84 条配方或本库的 12 张视觉素材。

## 这份提示词库能帮你做什么

- 按广告、商品、角色、旅行等目标选取完整提示词，替换项目内容后使用。
- 为图片、视频和音频参考分别指定用途，写清时间线、镜头运动和声音要求。
- 用人物、产品与场景约束减少前后不一致，再按检查清单逐项修改。
- 对照真实社区案例学习写法，区分作者要求、抽帧观察和仍需验证的效果。
- 用制作模板整理交付要求；已有测试结果也可以按[贡献指南](./CONTRIBUTING.md)分享。

<a id="choose-a-prompt"></a>

## 按你要做的视频找提示词

先查看配方标注的时长、输入素材及各素材用途。许多配方需要参考图或视频，且时长超过 5 秒；使用免费体验工具时，应按其支持的输入和时长改写，不能直接照搬。

| 制作目标 | 起点（英文） | 先关注什么 |
|---|---|---|
| 产品与广告 | [BRD-001](./prompts/01-brand-advertising.md#brd-001-midnight-observatory-tea-launch) | 产品亮相、材质与形状保持一致 |
| 人物与生活短片 | [UGC-001](./prompts/03-ugc-lifestyle.md#ugc-001-desk-lamp-honest-first-impression) | 先安排一个清楚的产品演示动作 |
| 旅行与场景 | [TRV-001](./prompts/04-travel-hospitality.md#trv-001-rain-washed-canal-town-morning) | 场景气氛与缓慢运镜 |
| 动画角色 | [ANI-002](./prompts/08-animation-stylized.md#ani-002-clay-repair-robot-finds-a-button) | 角色外观、动作和道具连续性 |
| 动态海报 | [MOG-001](./prompts/22-motion-graphics-dynamic-posters.md#mog-001-night-market-poster-builds-on-the-beat) | 画面逐步出现，结尾留出阅读时间 |
| 多参考与运镜迁移 | [MRF-002](./prompts/20-multireference-camera-transfer.md#mrf-002-radial-cork-speaker-transfer-motion-grammar-not-content) | 先确认工具支持所需的视频参考 |

[本页全部 24 个分类](#full-catalog) · **[浏览完整 84 条提示词](./prompts/README.md)** · [按制作目标和难点选择](./docs/use-case-matrix.md)

<a id="try-a-shot"></a>

## 试做第一个 5 秒镜头

| 你要做什么 | VideoWeb 入口 |
|---|---|
| 免注册试一个镜头 | [免费 MiniMax H3](https://videoweb.ai/free-minimax-h3/)：页面标注 480p、5 秒，可输入文字或选传首尾两图 |
| 日常制作，选择更多设置 | [MiniMax H3 模型页](https://videoweb.ai/model/minimax-h3/)：生成前确认可用设置、积分及使用条件 |

先打开免费工具，不上传图片，复制下方示例并选择画面比例。生成后检查瓶形和运镜，再一次修改一个问题。

```text
5 秒连续单镜头：一只虚构、无品牌的蓝色玻璃瓶放在深色摄影台上。0–1 秒：中近景静止展示，瓶身完整入画。1–4 秒：镜头缓慢推进，柔和侧光显出玻璃质感，瓶子始终不动。4–5 秒：镜头停稳，留下清楚的产品画面。瓶形、瓶盖、颜色和背景保持一致。不切镜头，不旋转瓶身，不增加物体、文字或标志。声音意图：安静的室内环境声，不要人声或音乐。
```

这是未经生成测试的入门示例，不计入 84 条源库提示词。页面信息核对于 2026-09-22，设置和排队情况可能变化。若用图片引导，请准备首尾两张图；复杂的视频或音频参考需要工具明确支持。详见[操作指南与常见问题](./docs/videoweb-quick-start.md)。

<a id="watch-examples"></a>

## 看视频，读作者提示词

以下是外部作者作品，不是本库提示词的测试结果，也不是 VideoWeb 生成证明。点击预览打开 X 视频；每条另有 MP4、原始提示词与解析入口。

各组末尾的“练习类似效果”链接指向本库独立配方与模板，并非对应视频的原提示词。每条视频旁的“作者提示词”链接则指向作者原文。练习前请确认所需参考素材及工具是否支持。

**按用途看案例：** [产品与时尚广告](#examples-products) · [人物与表演](#examples-characters) · [动作与运镜](#examples-motion) · [文字与界面](#examples-graphics) · [剪辑与叙事](#examples-storytelling)

<a id="examples-products"></a>

### 产品与时尚广告

| 耳机广告：从材质微距到结构拆解 | 蓝色摄影棚时尚片：三参考同场 | 护肤广告：夜晚到清晨的连续性 |
|---|---|---|
| [![耳机广告：从材质微距到结构拆解](https://pbs.twimg.com/ext_tw_video_thumb/2082783299395538944/pu/img/DXW1Eq1OUCaY8ssH.jpg)](https://x.com/LudovicCreator/status/2082783319075291312/video/1) | [![蓝色摄影棚时尚片：三参考同场](https://pbs.twimg.com/amplify_video_thumb/2083300689606852608/img/vviCnuLIJP17YlBx.jpg)](https://x.com/egeberkina/status/2083301476206588086/video/1) | [![护肤广告：夜晚到清晨的连续性](https://pbs.twimg.com/amplify_video_thumb/2083012032279064576/img/QvG1RJ-3ZOfkL6S9.jpg)](https://x.com/AIwithJessica/status/2083013658230317082/video/1) |
| [@LudovicCreator](https://x.com/LudovicCreator) · [▶ MP4](https://video.twimg.com/ext_tw_video/2082783299395538944/pu/vid/avc1/1280x720/2lMmYGBjYKPRAZ8M.mp4?tag=12) · [作者提示词](https://x.com/LudovicCreator/status/2082783319075291312) · [解析](./docs/x-community-showcase.md#xh3-002) | [@egeberkina](https://x.com/egeberkina) · [▶ MP4](https://video.twimg.com/amplify_video/2083300689606852608/vid/avc1/2560x1440/fI84aXKhdEk3Fhp-.mp4?tag=29) · [作者提示词](https://x.com/egeberkina/status/2083301476206588086) · [解析](./docs/x-community-showcase.md#xh3-004) | [@AIwithJessica](https://x.com/AIwithJessica) · [▶ MP4](https://video.twimg.com/amplify_video/2083012032279064576/vid/avc1/2560x1440/vfNGJZk54lKChkX4.mp4?tag=29) · [作者提示词](https://x.com/AIwithJessica/status/2083013658230317082) · [解析](./docs/x-community-showcase.md#xh3-008) |
| **学什么：** 四段时间线连接材质细节、产品旋转、零件分离和重新组装；重点学习几何形状的连续性约束。 | **学什么：** 提示词为每张参考图指定不同主体，再结合编舞与图形叠加；仅有文字不足以完整复现，还需要身份素材。 | **学什么：** 观察同一人物和产品如何跨越光线、景别与地点变化；对照开头与结尾的产品外观。 |
| **注意：** 生成的内部结构不代表真实产品构造。 | **注意：** 复现需要获得授权的人物参考素材。 | **注意：** 灯光是广告创意表现，不是护肤功效证明。 |

**练习类似效果（英文）:** [产品材质展示](./prompts/02-product-ecommerce.md#prd-002-ceramic-diffuser-material-film) · [时尚片运镜](./prompts/06-fashion-beauty.md#fsh-001-wind-study-eyewear-editorial)


<a id="examples-characters"></a>

### 人物与表演

| 角色登场：从局部揭示到完整轮廓 | 竹林悬疑：用近景与正反打建立张力 | 日语动画预告：身份与表情控制 |
|---|---|---|
| [![角色登场：从局部揭示到完整轮廓](https://pbs.twimg.com/amplify_video_thumb/2086412141729402880/img/8hxZX-hc394yGe7P.jpg)](https://x.com/aimikoda/status/2086412223061135392/video/1) | [![竹林悬疑：用近景与正反打建立张力](https://pbs.twimg.com/amplify_video_thumb/2083131917797556224/img/7PDZpzJGurMtyH6Q.jpg)](https://x.com/sipteaandcoffee/status/2083132770650571041/video/1) | [![日语动画预告：身份与表情控制](https://pbs.twimg.com/amplify_video_thumb/2082945330925240322/img/v7Ke-e6Pa0EJnv3G.jpg)](https://x.com/haruuraeadss/status/2082945363431080299/video/1) |
| [@aimikoda](https://x.com/aimikoda) · [▶ MP4](https://video.twimg.com/amplify_video/2086412141729402880/vid/avc1/2160x2294/FS1GToZV1NqxgwuP.mp4?tag=29) · [作者提示词](https://x.com/aimikoda/status/2086412223061135392) · [解析](./docs/x-community-showcase.md#xh3-003) | [@sipteaandcoffee](https://x.com/sipteaandcoffee) · [▶ MP4](https://video.twimg.com/amplify_video/2083131917797556224/vid/avc1/2560x1440/IwY2cFJMAMZcOWT2.mp4?tag=29) · [作者提示词](https://x.com/sipteaandcoffee/status/2083132770650571041) · [解析](./docs/x-community-showcase.md#xh3-005) | [@haruuraeadss](https://x.com/haruuraeadss) · [▶ MP4](https://video.twimg.com/amplify_video/2082945330925240322/vid/avc1/2560x1440/pitGJm9RtfP57PFJ.mp4?tag=29) · [作者提示词](https://x.com/haruuraeadss/status/2082945363431080299) · [解析](./docs/x-community-showcase.md#xh3-015) |
| **学什么：** 用一个身份参考贯穿局部、身体、表情和全身轮廓的逐步揭示；复现时需要准备角色参考图。 | **学什么：** 以色彩、景深、布光和正反打组织戏剧张力；原文限制时代环境，但没有提供带时间点的对白脚本。 | **学什么：** 把人物外观固定项与允许变化的表情、动作分开；镜头变化对应发现线索的时刻。 |
| **注意：** 发布版附带角色设定图，不能把它的尺寸当成模型原生比例。 | **注意：** 原文给出场景方向，没有带时间点的对白脚本。 | **注意：** 复现需要角色设定图；全分辨率检查身份一致性与标题拼写。 |

**练习类似效果（英文）:** [细微表情](./prompts/21-character-dialogue-performance.md#chr-002-the-first-new-root) · [对白与反应](./prompts/21-character-dialogue-performance.md#chr-003-bilingual-radio-repair-handoff)


<a id="examples-motion"></a>

### 动作与运镜

| 日常影像与不可能事件：值得研究的偏差 | 游泳片段：区分四种动作 | 悬崖追逐：连续运镜的空间路线 |
|---|---|---|
| [![日常影像与不可能事件：值得研究的偏差](https://pbs.twimg.com/amplify_video_thumb/2086878515744669696/img/-jjYBSEiZo_2M_eS.jpg)](https://x.com/cocktailpeanut/status/2086879654116495564/video/1) | [![游泳片段：区分四种动作](https://pbs.twimg.com/amplify_video_thumb/2082798728948125696/img/cgvj4miYM0jtq8zu.jpg)](https://x.com/johnAGI168/status/2082798969499832514/video/1) | [![悬崖追逐：连续运镜的空间路线](https://pbs.twimg.com/amplify_video_thumb/2082499279680405504/img/sccNuuy1xWEtEzVo.jpg)](https://x.com/umesh_ai/status/2082499539735588916/video/1) |
| [@cocktailpeanut](https://x.com/cocktailpeanut) · [▶ MP4](https://video.twimg.com/amplify_video/2086878515744669696/vid/avc1/832x480/SWq-SdbO4yoiFzOO.mp4?tag=29) · [作者提示词](https://x.com/cocktailpeanut/status/2086879654116495564) · [解析](./docs/x-community-showcase.md#xh3-006) | [@johnAGI168](https://x.com/johnAGI168) · [▶ MP4](https://video.twimg.com/amplify_video/2082798728948125696/vid/avc1/2560x1440/jPepLvnPJuANFMKx.mp4?tag=29) · [作者提示词](https://x.com/johnAGI168/status/2082798969499832514) · [解析](./docs/x-community-showcase.md#xh3-010) | [@umesh_ai](https://x.com/umesh_ai) · [▶ MP4](https://video.twimg.com/amplify_video/2082499279680405504/vid/avc1/2560x1440/Zho0yGTsy043Peo5.mp4?tag=29) · [作者提示词](https://x.com/umesh_ai/status/2082499539735588916) · [解析](./docs/x-community-showcase.md#xh3-013) |
| **学什么：** 通过日常活动铺垫再引出不可能事件，适合研究伏笔、突变，以及模型是否按指定物理事件执行。 | **学什么：** 重点研究动作能否看清：检查泳姿切换，以及分配的时间是否足够辨认动作。 | **学什么：** 观察障碍如何推动重新构图，同时让运动主体持续吸引视线；结尾从追逐转为开阔空间展示。 |
| **注意：** 抽帧显示街道与云墙，并非原文要求的后院与下坠固体天空。 | **注意：** 抽帧不能证明泳姿正确，不宜当作教学。 | **注意：** 完整播放检查障碍穿越与运镜连续性。 |

**练习类似效果（英文）:** [连续镜头路线](./prompts/20-multireference-camera-transfer.md#mrf-001-three-biome-museum-rail-in-one-take) · [单镜头模板](./templates/README.md#t01-text-to-video-single-readable-shot)


<a id="examples-graphics"></a>

### 文字与界面

| 动态文字：让一句话变成视觉叙事 | 游戏界面：让回合过程清楚可读 | 动态海报：逐步组装但不破坏版式 |
|---|---|---|
| [![动态文字：让一句话变成视觉叙事](https://pbs.twimg.com/amplify_video_thumb/2083909175646785536/img/jQZFhoydpvrJNuCW.jpg)](https://x.com/umesh_ai/status/2083909535593644291/video/1) | [![游戏界面：让回合过程清楚可读](https://pbs.twimg.com/amplify_video_thumb/2082909305062273024/img/pdZ3rfdrDzNEZ6md.jpg)](https://x.com/AllaAisling/status/2082909383424446745/video/1) | [![动态海报：逐步组装但不破坏版式](https://pbs.twimg.com/ext_tw_video_thumb/2083628836285984768/pu/img/qvO3Ra84RHxRQhEy.jpg)](https://x.com/LudovicCreator/status/2083628852165672988/video/1) |
| [@umesh_ai](https://x.com/umesh_ai) · [▶ MP4](https://video.twimg.com/amplify_video/2083909175646785536/vid/avc1/2560x1440/L_Hs2kX2rOJqYZ8F.mp4?tag=29) · [作者提示词](https://x.com/umesh_ai/status/2083909535593644291) · [解析](./docs/x-community-showcase.md#xh3-001) | [@AllaAisling](https://x.com/AllaAisling) · [▶ MP4](https://video.twimg.com/amplify_video/2082909305062273024/vid/avc1/2560x1440/YHAv0vy5R_uIZnls.mp4?tag=29) · [作者提示词](https://x.com/AllaAisling/status/2082909383424446745) · [解析](./docs/x-community-showcase.md#xh3-011) | [@LudovicCreator](https://x.com/LudovicCreator) · [▶ MP4](https://video.twimg.com/ext_tw_video/2083628836285984768/pu/vid/avc1/720x1280/GfseYcSENCN1XmIr.mp4?tag=12) · [作者提示词](https://x.com/LudovicCreator/status/2083628879407632890) · [解析](./docs/x-community-showcase.md#xh3-014) |
| **学什么：** 为各段文字分配时间、字号变化与转场，最后留出静止阅读时间。 | **学什么：** 沿状态变化阅读：发牌、选择、执行、资源更新、对方回合；检查镜头变化时界面是否固定。 | **学什么：** 把海报拆成按顺序进入的图层，再留出阅读停顿；保持视觉层级，不让所有区域同时运动。 |
| **注意：** 检查逐字拼写与结尾阅读停顿。 | **注意：** 部分画面将卡牌与场景分栏，需核对是否符合完整游戏界面的目标。 | **注意：** 全尺寸检查小字与版式漂移；要求时长与上传时长不同。 |

**练习类似效果（英文）:** [海报逐层组装](./prompts/22-motion-graphics-dynamic-posters.md#mog-001-night-market-poster-builds-on-the-beat) · [功能卡片排版](./prompts/22-motion-graphics-dynamic-posters.md#mog-002-modular-product-feature-cards)


<a id="examples-storytelling"></a>

### 剪辑与叙事

| 西部片头：让剪辑服从节拍 | 悬疑短片：对白、反应与声音反转 | 街头美食：环境、制作与人物反应 |
|---|---|---|
| [![西部片头：让剪辑服从节拍](https://pbs.twimg.com/amplify_video_thumb/2085599599801077760/img/koDdEvAQb0L9RUpH.jpg)](https://x.com/doctorwasif/status/2085599659326935100/video/1) | **含突袭惊吓与闪屏**<br>[![悬疑短片：对白、反应与声音反转 — 含突袭惊吓与闪屏](https://pbs.twimg.com/amplify_video_thumb/2082668962203230208/img/qTeIl8rcO_BopQxq.jpg)](https://x.com/drjoetw/status/2082669221222207488/video/1) | [![街头美食：环境、制作与人物反应](https://pbs.twimg.com/amplify_video_thumb/2085233539185061888/img/ZAkMSVzHz9ihLPyD.jpg)](https://x.com/nawalsehar/status/2085233880353915217/video/1) |
| [@doctorwasif](https://x.com/doctorwasif) · [▶ MP4](https://video.twimg.com/amplify_video/2085599599801077760/vid/avc1/1920x1080/aQ8Mx5ImZmjNxrZR.mp4?tag=29) · [作者提示词](https://x.com/doctorwasif/status/2085599659326935100) · [解析](./docs/x-community-showcase.md#xh3-007) | [@drjoetw](https://x.com/drjoetw) · [▶ MP4 — 含突袭惊吓与闪屏](https://video.twimg.com/amplify_video/2082668962203230208/vid/avc1/2560x1440/PQbFC3v78uE88LdE.mp4?tag=29) · [作者提示词](https://x.com/drjoetw/status/2082669221222207488) · [解析](./docs/x-community-showcase.md#xh3-009) | [@nawalsehar](https://x.com/nawalsehar) · [▶ MP4](https://video.twimg.com/amplify_video/2085233539185061888/vid/avc1/2560x1440/jgQLrvA-NHvBJBx_.mp4?tag=29) · [作者提示词](https://x.com/nawalsehar/status/2085233880353915217) · [解析](./docs/x-community-showcase.md#xh3-012) |
| **学什么：** 学习静止姿态与短动作交替，并让标题落在音乐重拍上。 | **学什么：** 先制造疑问，再跟随指向动作揭示目标，用反应镜头收束；声音变化承担气氛反转。 | **学什么：** 对比环境全景、制作细节和试吃反应，理解三者不同的叙事作用。 |
| **注意：** 抽帧标题字形异常；需修字，并完整播放核对节拍。 | **注意：** 含惊吓与闪屏。提示词要求 9:16，上传视频实际为 16:9。 | **注意：** 生成地点与人物反应不能充当纪实证据或真实评价。 |

**练习类似效果（英文）:** [多镜头规划](./templates/README.md#t06-multi-shot-sequence-plan) · [节奏驱动剪辑](./templates/README.md#t10-audio--or-rhythm-guided-sequence)


完整来源、设定与中英解析见[15 条案例详情](./docs/x-community-showcase.md)。

来源记录分别核对于 2026-09-20 和 2026-09-22，采用公开帖子读取及视频抽帧，未独立生成、未试听音频。外部作品不纳入仓库 MIT 许可。[核对方法与来源](./docs/x-community-showcase.md#reading-the-evidence)

## MiniMax 官方视频示例

以下预览通过远程链接引用自 MiniMax-H3 官方仓库，并直接链接回官方 Skill。媒体文件没有复制到本项目，也不会被描述成本提示词库的生成结果。

| 产品广告 | 3D 动画 | 音乐视频 |
|---|---|---|
| [![MiniMax H3 官方极简产品广告示例](https://raw.githubusercontent.com/MiniMax-AI/MiniMax-H3/main/assets/minimalist-product-ad-generator.gif)](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills/minimalist-product-ad-generator) | [![MiniMax H3 官方 3D 动画短片示例](https://raw.githubusercontent.com/MiniMax-AI/MiniMax-H3/main/assets/3d-animation-short-generator.gif)](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills/3d-animation-short-generator) | [![MiniMax H3 官方音乐视频字幕示例](https://raw.githubusercontent.com/MiniMax-AI/MiniMax-H3/main/assets/music-video-subtitle-generator.gif)](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills/mv-subtitle-skill-confirmed) |

在[带来源标注的官方示例画廊](./docs/official-h3-examples.md)中，可以继续查看可复现的 T2VA、FL2VA、Ref2VA 请求脚本、768p MP4 输出和 2K 流程对照。

<a id="reference-images"></a>

## 选择参考图

点击图片查看原图，点击下方链接打开提示词。图片用于首帧、结束画面或氛围参考，不是 H3 生成效果证明；所需的其他素材见各配方。

<table width="100%">
<tr>
<th width="33%" align="center"><strong>品牌与产品</strong></th>
<th width="33%" align="center"><strong>UGC 与生活方式</strong></th>
<th width="33%" align="center"><strong>旅行与酒店</strong></th>
</tr>
<tr>
<td width="33%" align="center"><a href="./assets/gallery/midnight-observatory-tea.webp"><img src="./assets/gallery/midnight-observatory-tea.webp" alt="日出前山顶观测站中的虚构瓶装茶饮" width="280"></a></td>
<td width="33%" align="center"><a href="./assets/gallery/honest-desk-lamp-demo.webp"><img src="./assets/gallery/honest-desk-lamp-demo.webp" alt="成人创作者在家庭工作室体验原创折叠台灯" width="200"></a></td>
<td width="33%" align="center"><a href="./assets/gallery/rain-washed-canal-morning.webp"><img src="./assets/gallery/rain-washed-canal-morning.webp" alt="雨后虚构水乡街区、自行车与石桥" width="280"></a></td>
</tr>
<tr>
<td width="33%" align="center"><a href="./prompts/01-brand-advertising.md#brd-001-midnight-observatory-tea-launch">BRD-001 提示词</a></td>
<td width="33%" align="center"><a href="./prompts/03-ugc-lifestyle.md#ugc-001-desk-lamp-honest-first-impression">UGC-001 提示词</a></td>
<td width="33%" align="center"><a href="./docs/fictional-canal-starter.md#简体中文">虚构水乡练习</a></td>
</tr>
</table>

<table width="100%">
<tr>
<th width="50%" align="center"><strong>动画与角色</strong></th>
<th width="50%" align="center"><strong>动作与运动</strong></th>
</tr>
<tr>
<td width="50%" align="center"><a href="./assets/gallery/clay-repair-robot.webp"><img src="./assets/gallery/clay-repair-robot.webp" alt="微缩木工作台中的原创黄色黏土维修机器人" width="280"></a></td>
<td width="50%" align="center"><a href="./assets/gallery/indoor-climbing-final-hold.webp"><img src="./assets/gallery/indoor-climbing-final-hold.webp" alt="配备安全装备、正在室内黄色线路攀爬的虚构成年运动员" width="280"></a></td>
</tr>
<tr>
<td width="50%" align="center"><a href="./prompts/08-animation-stylized.md#ani-002-clay-repair-robot-finds-a-button">ANI-002 提示词</a></td>
<td width="50%" align="center"><a href="./prompts/09-action-sports.md#act-001-indoor-climbing-final-move">ACT-001 提示词</a></td>
</tr>
</table>

<table width="100%">
<tr>
<th width="33%" align="center"><strong>运镜迁移产品</strong></th>
<th width="33%" align="center"><strong>角色对白</strong></th>
<th width="33%" align="center"><strong>多参考长镜头</strong></th>
</tr>
<tr>
<td width="33%" align="center"><a href="./assets/gallery/radial-cork-speaker.webp"><img src="./assets/gallery/radial-cork-speaker.webp" alt="原创虚构石墨灰与软木便携音箱" width="280"></a></td>
<td width="33%" align="center"><a href="./assets/gallery/paper-birds-storm-shelter.webp"><img src="./assets/gallery/paper-birds-storm-shelter.webp" alt="暴雨温室中的原创靛蓝和藏红纸艺鸟角色" width="280"></a></td>
<td width="33%" align="center"><a href="./assets/gallery/three-biome-museum-rail.webp"><img src="./assets/gallery/three-biome-museum-rail.webp" alt="跨越三种桌面生态的原创微缩博物馆轨道" width="280"></a></td>
</tr>
<tr>
<td width="33%" align="center"><a href="./prompts/20-multireference-camera-transfer.md#mrf-002-radial-cork-speaker-transfer-motion-grammar-not-content">MRF-002 提示词</a></td>
<td width="33%" align="center"><a href="./prompts/21-character-dialogue-performance.md#chr-001-paper-birds-plan-for-the-storm">CHR-001 提示词</a></td>
<td width="33%" align="center"><a href="./prompts/20-multireference-camera-transfer.md#mrf-001-three-biome-museum-rail-in-one-take">MRF-001 提示词</a></td>
</tr>
</table>

<table width="100%">
<tr>
<th width="33%" align="center"><strong>动态海报</strong></th>
<th width="33%" align="center"><strong>实拍超现实</strong></th>
<th width="33%" align="center"><strong>直播演示</strong></th>
</tr>
<tr>
<td width="33%" align="center"><a href="./assets/gallery/dynamic-night-market-poster.webp"><img src="./assets/gallery/dynamic-night-market-poster.webp" alt="带空白文字区域的原创纸艺夜市动态海报" width="141"></a></td>
<td width="33%" align="center"><a href="./assets/gallery/topographic-map-archive.webp"><img src="./assets/gallery/topographic-map-archive.webp" alt="从档案地图升起的原创手工微缩地形" width="280"></a></td>
<td width="33%" align="center"><a href="./assets/gallery/modular-lunch-jar-kit.webp"><img src="./assets/gallery/modular-lunch-jar-kit.webp" alt="包含五个组件的原创无品牌模块化午餐罐" width="200"></a></td>
</tr>
<tr>
<td width="33%" align="center"><a href="./prompts/22-motion-graphics-dynamic-posters.md#mog-001-night-market-poster-builds-on-the-beat">MOG-001 提示词</a></td>
<td width="33%" align="center"><a href="./prompts/23-surreal-physics-optical-illusions.md#srl-001-the-map-rises-into-a-landscape">SRL-001 提示词</a></td>
<td width="33%" align="center"><a href="./prompts/24-vertical-series-live-creator.md#ver-001-honest-modular-lunch-jar-live-demo">VER-001 提示词</a></td>
</tr>
</table>

制作自己的参考图：[参考图制作提示词](./assets/minimax-h3-reference-image-prompts.md) · [素材制作记录](./assets/README.md)

水乡图对应单图练习；[原版 TRV-001](./prompts/04-travel-hospitality.md#trv-001-rain-washed-canal-town-morning) 需要三张核实过的地点图。另见 [VideoWeb 封面制作记录](./assets/videoweb-cover-prompt.md)。

<a id="full-catalog"></a>

## 全部 24 个实用分类

| 分类 | 数量 | 重点场景 |
|---|---:|---|
| [品牌与广告](./prompts/01-brand-advertising.md) | 3 | 新品发布、本地活动、多比例适配 |
| [产品与电商](./prompts/02-product-ecommerce.md) | 3 | 功能演示、材质片、商品旋转展示 |
| [UGC 与生活方式](./prompts/03-ugc-lifestyle.md) | 3 | 真实体验、生活流程、装包测试 |
| [旅行与酒店](./prompts/04-travel-hospitality.md) | 3 | 目的地、客房、夜市动线 |
| [美食与饮料](./prompts/05-food-beverage.md) | 3 | 烘焙、出餐、饮料微距 |
| [时尚与美妆](./prompts/06-fashion-beauty.md) | 3 | 眼镜大片、唇妆材质、换装转场 |
| [电影叙事](./prompts/07-cinematic-storytelling.md) | 3 | 未寄信件、车站告别、屋顶悬疑 |
| [动画与风格化影像](./prompts/08-animation-stylized.md) | 3 | 剪纸科普、黏土角色、水墨变形 |
| [动作与运动](./prompts/09-action-sports.md) | 3 | 攀岩、雨地骑行、乒乓球 |
| [奇幻、科幻与 VFX](./prompts/10-fantasy-scifi-vfx.md) | 3 | 玻璃花房、微缩城市、光点礼服 |
| [UI、游戏与数字体验](./prompts/11-ui-game-digital.md) | 3 | App 演示、硬件 UI、游戏背包 |
| [转场、喜剧与社交内容](./prompts/12-transitions-comedy-social.md) | 3 | 匹配剪辑、办公室植物、洗衣房外星人 |
| [音乐、表演与声音驱动视频](./prompts/13-music-performance-audio.md) | 4 | 现场音乐、多语言对唱、舞蹈、声音可视化 |
| [教育、纪录与科学](./prompts/14-education-documentary-science.md) | 4 | 科普、博物馆、操作安全、显微世界 |
| [建筑、室内与房地产](./prompts/15-architecture-interiors-real-estate.md) | 4 | 房产漫游、光照、改造、智能家居 |
| [汽车与出行](./prompts/16-automotive-mobility.md) | 4 | 汽车内饰、货运自行车、卧铺列车、配送机器人 |
| [自然、动物与宠物](./prompts/17-nature-animals-pets.md) | 4 | 野生动物、宠物、植物生长、潮池微距 |
| [工业、商业与公共服务](./prompts/18-industry-business-public-service.md) | 4 | 装配、冷链、疏散、双语服务 |
| [视频编辑、续写与本地化](./prompts/19-editing-continuation-localization.md) | 4 | 背景清理、镜头续写、本地化、重布光 |
| [多参考与运镜迁移](./prompts/20-multireference-camera-transfer.md) | 4 | 微缩长镜头、运镜语法、工艺匹配剪辑、教程 |
| [角色、对白与表演](./prompts/21-character-dialogue-performance.md) | 4 | 纸艺角色、克制情绪、双语维修、群像叙事 |
| [动态图形与动态海报](./prompts/22-motion-graphics-dynamic-posters.md) | 4 | 海报组装、功能卡片、展览片头、材质标识 |
| [超现实物理与视觉错觉](./prompts/23-surreal-physics-optical-illusions.md) | 4 | 地图隆起、影子预演、未来水洼、材质球体 |
| [竖屏系列与直播创作](./prompts/24-vertical-series-live-creator.md) | 4 | 直播演示、邻里短剧、维修系列、创作者答疑 |

## 继续学习与本地部署

| 需求 | 文档 |
|---|---|
| 改写镜头、声音与人物细节 | [提示词指南](./docs/prompting-guide.md) · [12 个制作模板](./templates/README.md) |
| 用中文等语言开始 | [多语言提示词](./docs/multilingual-prompting.md) |
| 理解模型与接口 | [H3 模型说明](./docs/minimax-h3-overview.md) · [接口使用流程](./docs/api-workflow.md) |
| 在自己的设备上运行 | [九语言部署指南](./docs/deployment-guide.md) |
| 找图片参考与制作记录 | [参考图简报](./assets/minimax-h3-reference-image-prompts.md) · [素材记录](./assets/README.md) |
| 比较其他使用入口 | [其他 H3 工具](./docs/other-h3-tools.md) |

## 如何编写和检查 H3 提示词

MiniMax 官方 H3 资料强调三类能力：文字、图片、音频、视频的原生多模态理解与生成；对人物、物体、场景、声音和节奏的多维编辑控制；面向影视、广告、电商、数字体验、游戏和动画的商用内容生成。详见 [MiniMax 官方 H3 亮点示例](https://platform.minimaxi.com/docs/guides/video-prompt)。

本项目将这些能力整理为可复用的提示词结构：

```text
参考素材映射：每张图、视频或音频允许控制什么
交付要求：渠道、比例、目标时长、受众、目标
创意方向：场景、主体、故事、风格、光线、色彩
时间线：开场状态 → 动作节拍 → 结束状态
镜头：景别、屏幕方向、运镜、剪辑和转场规则
连续性锁定：身份、产品、服装、环境、UI、道具
声音意图：环境音、音效、对白或音乐的职责
编辑范围：允许修改什么、必须保持什么
避免：视觉、物理、连续性、法律和品牌风险
```

仓库不会编造接口参数。请先阅读 [H3 模型说明与官方资源](./docs/minimax-h3-overview.md)，当前模型标识、支持输入、限制、API 字段、模型许可和可下载版本能力以 MiniMax 官方文档及模型卡为准。

### 检查步骤

1. 按最终交付物和主要制作风险选择配方。
2. 只上传真正需要的参考素材，并为每个素材标记职责。
3. 替换所有 `[方括号变量]`，使用虚构设定或获得授权的真实素材。
4. 根据 H3 当前工作流支持的时长调整时间线。
5. 先生成结构版本，再增加复杂声音、文字或特效。
6. 每次只修复一个问题：动作、身份、产品、镜头、文字或声音。
7. 以正常速度、逐帧、静音和最终展示尺寸分别检查。

多语言制作应从英文规范源开始，完整翻译动作、镜头、声音和约束，而不是只翻译风格词。[多语言指南](./docs/multilingual-prompting.md)提供简体中文、日语、韩语、西班牙语、法语、德语、葡萄牙语和阿拉伯语完整示例。

## 官方资源与本地部署范围

- **H3 官方仓库：** [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3)
- **H3 模型卡与开放权重：** [MiniMaxAI/MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)
- **本地部署：** [九语言开源部署指南](./docs/deployment-guide.md)
- **官方视频和 Skill：** [带来源标注的官方示例画廊](./docs/official-h3-examples.md)
- **H3 官方能力与提示词示例：** [MiniMax 视频提示词指南](https://platform.minimaxi.com/docs/guides/video-prompt)
- **托管视频生成流程：** [MiniMax 视频生成文档](https://platform.minimaxi.com/docs/guides/video-generation)

当前开放版本提供 H3-Base FL2VA 与 Ref2VA 权重，可在本地生成 768p 原生音视频；H3-Context-IR 与 H3-Regenerate-2K 仍是托管组件，完整 2K 流程需要本地生成与官方 API 配合。部署或商用前，请核对最新 Community License、支持任务、硬件/运行时要求和实际发布文件。

## 原创、版权与安全

- 只提交原创提示词以及拥有必要权利的输入和输出；
- 不仿制受保护角色、在世艺术家、私人个体、广告活动、商品或界面；
- 口碑、评分、价格、日期、性能、地图与历史事实必须经过核验；
- 确保身份、声音、音乐、品牌、场地和素材获得必要同意与授权；
- 在法律或平台要求的场景中标注生成或大幅修改的媒体；
- 发布示例时保存模型/工具、输入、设置、日期、人工修改和已知缺陷。

详细规则见[原创与来源政策](./docs/originality-policy.md)、[CONTRIBUTING.md](./CONTRIBUTING.md)和[素材制作规范](./assets/README.md)。

## 欢迎提交你的原创 H3 工作流

如果某条提示词帮你解决了真实制作问题，欢迎通过[结构化提示词提案](https://github.com/aivideoweb/awesome-minimax-h3-prompts/issues/new?template=prompt-proposal.yml)提交。成片不是必需项；高质量提案应说明交付目标、参考素材职责、可见动作、时间线、连续性锁定、声音意图、易错点，以及内容是概念版还是已测试版本。

适合首次参与的任务包括：测试现有配方、补充真实场景缺口、改进审查清单、增加母语适配，或报告已经失效的官方文档。提交前请阅读[贡献指南](./CONTRIBUTING.md)；内容必须原创、权利清晰、可复核，并且不能包含隐藏推广或追踪链接。

[改进文档](https://github.com/aivideoweb/awesome-minimax-h3-prompts/issues/new?template=documentation.yml) · [发起 Pull Request](https://github.com/aivideoweb/awesome-minimax-h3-prompts/pulls)

## 关于 VideoWeb AI

[VideoWeb AI](https://videoweb.ai) 提供在线 AI 视频与图片创作工具。本仓库作为面向实际多模态视频制作的开源资源进行维护。

这是独立社区项目，未获得 MiniMax 官方背书。相关产品名称归各自权利人所有。

## VideoWeb AI 联盟推广计划

VideoWeb AI 面向开发者、创作者、测评者、教育工作者和 AI 社区提供 [Affiliate Program](https://videoweb.ai/affiliate-program/)。完成资料并确认联盟协议后，可以分享专属推荐链接，并从正确归因的合格付费订单中获得佣金。当前官方公开方案为：被推荐用户的首笔有效付费订单佣金 20%，注册后 60 天归因期内的后续有效付费订单佣金 10%。具体费率、订单资格、归因、退款与结算均以现行联盟协议为准，参与计划不代表保证获得订单或收益。

加入步骤、合规推广规则以及九种语言的披露语见[多语言联盟推广指南](./docs/affiliate-program.md)。

## 许可证

[MIT](./LICENSE) © 2026 Flaq AI; VideoWeb AI adaptations © 2026 aivideoweb · [Upstream](./UPSTREAM.md)
