# MiniMax H3 Open-Weight Deployment Guide

> 简体中文详细指南 + English reference + 日本語、한국어、Español、Français、Deutsch、Português、العربية 快速说明  
> Detailed Simplified Chinese guide with English reference and localized quick starts in seven additional languages.

[简体中文](#简体中文部署指南) · [English](#english-deployment-reference) · [日本語](#日本語クイックスタート) · [한국어](#한국어-빠른-시작) · [Español](#inicio-rápido-en-español) · [Français](#démarrage-rapide-en-français) · [Deutsch](#deutscher-schnellstart) · [Português](#início-rápido-em-português) · [العربية](#البدء-السريع-بالعربية)

Last verified: 2026-08-06 against the official [MiniMax-AI/MiniMax-H3 repository](https://github.com/MiniMax-AI/MiniMax-H3) and [SGLang MiniMax-H3 cookbook](https://docs.sglang.io/cookbook/diffusion/MiniMax/MiniMax-H3).

## 简体中文部署指南

### 1. 先理解当前开放范围

MiniMax H3 完整系统由三个部分组成：

| 模块 | 当前状态 | 用途 |
|---|---|---|
| H3-Context-IR | 托管服务，未随开源版本提供 | 理解自由形式的文字、图片、视频和音频输入，并生成适合 H3-Base 的结构化上下文 |
| H3-Base | 已开放权重 | 在本地生成 768p 音视频 |
| H3-Regenerate-2K | 托管服务，尚未开放 | 将基础结果结合原始上下文重新生成到 2K |

因此有两条部署路线：

1. **纯本地路线：** 本地运行 H3-Base，生成 768p、24 FPS、32 kHz 立体声音视频。
2. **完整 2K 混合路线：** 官方 H3-Context-IR API → 本地 H3-Base → 官方 H3-Regenerate-2K API。

不要把“权重已开放”理解为完整线上产品已全部开放。本地或商用前必须阅读 [MiniMax H3 Community License Agreement](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE)。

### 2. 选择正确的模型分支

| 权重分支 | 任务 | 什么时候选择 |
|---|---|---|
| FL2VA | t2va、fl2va | 纯文字生成，或将一张图片作为首帧/尾帧，或同时指定首尾帧 |
| Ref2VA | ref2va | 使用图片、视频和音频作为语义参考；视频转视频也属于该任务 |

官方输入边界：

- FL2VA：零张、一张或两张图片；
- Ref2VA：最多 9 张图片；
- Ref2VA：最多 3 段视频，每段 2–15 秒，视频总时长不超过 15 秒；
- Ref2VA：最多 3 段音频，每段 2–15 秒，音频总时长不超过 15 秒；
- 音频不能作为 Ref2VA 的唯一输入，必须同时提供图片或视频；
- 混合参考素材总数最多 12 个文件；
- 输出时长为 4–15 秒；
- 官方稳定支持 11 种对白语言：阿拉伯语、中文、英语、法语、德语、意大利语、日语、韩语、葡萄牙语、俄语和西班牙语。

### 2.1 安装官方提示词 Skill（可选）

官方仓库提供一个 H3 通用提示词 Skill，以及八个广告、动画、解释视频、音乐字幕、游戏片头等风格化视频 Skill。使用兼容 skills CLI 的 Agent 环境时，可安装通用 H3 提示词 Skill：

~~~bash
npx skills add https://github.com/MiniMax-AI/MiniMax-H3 \
  --skill h3-prompt-writing
~~~

它包含 text/keyframe 模式与 Ref2VA 全参考模式的官方英文指南。安装前应审查 Skill 内容和依赖；该 Skill 是提示词辅助工具，不会替代模型权重、GPU 推理服务或许可证检查。

### 3. 硬件与部署预期

H3-Omni-Transformer 是大型稠密模型，本地部署属于多 GPU 或高内存工作负载。不要根据模型名称猜测显存需求，应按实际框架、任务、分辨率、时长、参考素材数量和并行方式进行容量测试。

官方 SGLang 文档当前给出的已验证配置包括：

- 4× H200：常驻权重、Ulysses 4；
- 4× H100 80 GB：TP 2 + Ulysses 2；
- 2× RTX 5090 32 GB：分层卸载，并建议约 384 GiB 级别主机内存；
- B200、B300、MI300X、MI355X 等配置也提供单独验证方案。

如果没有合适硬件，先使用 MiniMax 在线 API 或 ComfyUI 云端节点验证提示词，再决定是否建设本地集群。

### 4. 准备环境

推荐使用 Linux、受支持的 GPU 驱动与独立 Python 环境。SGLang 官方安装命令：

~~~bash
uv pip install "sglang[diffusion]" --prerelease=allow
~~~

同时准备：

- Hugging Face CLI，用于按任务下载权重；
- curl 和 jq，用于调用异步视频接口；
- ffprobe 或其他媒体检查工具，用于核验视频、帧率和音轨；
- 足够的模型缓存、临时文件和输出空间；
- 与所选框架兼容的驱动、CUDA/ROCm、PyTorch 和通信库。

快速检查：

~~~bash
nvidia-smi
python --version
uv --version
hf --help
ffprobe -version
~~~

AMD 环境、容器镜像和特定 GPU 拓扑请直接使用 [SGLang Diffusion 安装文档](https://docs.sglang.io/docs/sglang-diffusion/installation)中与当前版本对应的命令。

### 5. 下载权重

SGLang 和 vLLM 使用原始任务分支时，可按需要下载一个或两个分支。

~~~bash
# 同时下载 FL2VA 和 Ref2VA
hf download MiniMaxAI/MiniMax-H3 \
  --include "model_index.json" "FL2VA/*" "Ref2VA/*" \
  --local-dir MiniMax-H3

# 只下载文字/首尾帧任务
hf download MiniMaxAI/MiniMax-H3 \
  --include "model_index.json" "FL2VA/*" \
  --local-dir MiniMax-H3
~~~

Diffusers 用户可通过 ModularPipeline.from_pretrained("MiniMaxAI/MiniMax-H3") 按流水线加载所需组件，不必预先下载全部任务分支。具体加载方式以 [Diffusers H3 文档](https://github.com/huggingface/diffusers/blob/minimax-h3/docs/source/en/api/pipelines/minimax_h3.md)为准。

中国区也可使用官方 [ModelScope MiniMax 组织页](https://modelscope.cn/organization/minimax)。SGLang 文档给出的方式是在启动命令前设置 SGLANG_USE_MODELSCOPE=true，并将模型路径替换为 MiniMax/MiniMax-H3；模型分支和并行参数保持不变。

建议在生成记录中保存模型来源、权重修订版本、运行框架版本和模型文件哈希，不要只写“MiniMax H3”。

### 6. 使用 SGLang 启动服务

以下命令与官方四卡示例保持一致，但默认只监听本机地址。生产环境不要在没有鉴权、访问控制和反向代理的情况下直接暴露端口。

FL2VA 服务：

~~~bash
sglang serve \
  --model-path MiniMaxAI/MiniMax-H3 \
  --num-gpus 4 \
  --ulysses-degree 4 \
  --performance-mode speed \
  --host 127.0.0.1 \
  --port 30010 \
  --model-variant fl2va
~~~

Ref2VA 服务：

~~~bash
sglang serve \
  --model-path MiniMaxAI/MiniMax-H3 \
  --num-gpus 4 \
  --ulysses-degree 4 \
  --performance-mode speed \
  --host 127.0.0.1 \
  --port 30011 \
  --model-variant ref2va
~~~

四张 H100 80 GB、两张 RTX 5090 或其他拓扑不要直接套用上述并行参数。请从 [SGLang H3 硬件选择器和已验证配置](https://docs.sglang.io/cookbook/diffusion/MiniMax/MiniMax-H3#3-serve-minimax-h3)复制对应命令。

### 7. 发起 T2VA 任务

SGLang 使用异步、OpenAI 兼容的视频任务接口。先创建任务，再轮询状态，最后下载 MP4。

~~~bash
video_id=$(
  curl -sS -X POST http://127.0.0.1:30010/v1/videos \
    -H "Content-Type: application/json" \
    -d '{
      "model": "MiniMaxAI/MiniMax-H3",
      "prompt": "A quiet workshop at dawn. One small repair robot closes a wooden drawer, looks toward the window, and the room fills with natural birdsong. No dialogue, no text, no logo.",
      "seconds": 5,
      "task": "t2va",
      "conditions": [],
      "target": {
        "short_edge": 768,
        "aspect_ratio": "16:9",
        "duration_seconds": 5.0
      },
      "num_outputs_per_prompt": 1,
      "num_inference_steps": 50,
      "flow_shift": 12.0,
      "audio_flow_shift": 3.0,
      "seed": 1101
    }' |
    jq -r '.id'
)

while true; do
  status=$(curl -sS "http://127.0.0.1:30010/v1/videos/${video_id}" | jq -r '.status')
  [ "$status" = "completed" ] && break
  [ "$status" = "failed" ] && exit 1
  sleep 1
done

curl -sS -L \
  "http://127.0.0.1:30010/v1/videos/${video_id}/content" \
  -o minimax-h3-t2va.mp4
~~~

这是最小可读示例。生产代码必须为提交、轮询和下载添加总体超时、指数退避、HTTP 错误处理、失败原因记录与任务取消策略，避免无限轮询。

### 8. 首帧、尾帧与参考素材

FL2VA 的图片是实际关键帧：

- frame_index 为 0：首帧；
- frame_index 为 -1：尾帧；
- 同时提供 0 和 -1：首尾帧。

~~~json
{
  "task": "fl2va",
  "conditions": [
    {
      "type": "image",
      "uri": "file:///data/minimax-h3/first-frame.png",
      "role": "keyframe",
      "frame_index": 0
    }
  ]
}
~~~

Ref2VA 的素材是语义参考，不保证逐像素保持原视频或原图片。它可能重新构图、裁切、重合成动作或调整剪辑顺序。视频转视频也应启动 ref2va 权重，并保持请求任务为 ref2va。

~~~json
{
  "task": "ref2va",
  "conditions": [
    {
      "type": "image",
      "uri": "file:///data/minimax-h3/reference.png",
      "role": "reference"
    },
    {
      "type": "audio",
      "uri": "file:///data/minimax-h3/reference.mp3",
      "role": "reference"
    }
  ]
}
~~~

提示词中的素材标签使用每种模态各自的一基序号，例如 Picture 1、Video 1 和 Audio 1。每个素材只分配一个明确职责，参考本项目的[提示词编写指南](./prompting-guide.md)。

file URI 指向的是推理服务器或容器内部可见的路径，不是发起请求的客户端电脑路径。容器部署时应将素材目录以只读方式挂载到约定位置。

### 9. 验证输出

~~~bash
ffprobe -v error \
  -show_entries stream=index,codec_name,codec_type,width,height,r_frame_rate,sample_rate,channels \
  -of json minimax-h3-t2va.mp4
~~~

至少检查：

- MP4 可以完整播放；
- 视频为 24 FPS；
- 包含 H.264 视频流；
- 包含 AAC 立体声音轨，采样率为 32 kHz；
- 分辨率、比例和时长符合请求；
- 画面、动作、身份、参考素材和声音没有明显漂移；
- 没有未经授权的身份、声音、音乐、商标、隐私数据或误导性声明。

### 10. 完整 2K 混合流程

当前开放权重只覆盖 H3-Base。完整 2K 流程需要：

1. 调用 H3-Context-IR，将自由形式多模态输入整理为结构化上下文；
2. 把该上下文提交给本地 H3-Base，生成 768p 基础音视频；
3. 将基础视频与原始上下文提交给 H3-Regenerate-2K；
4. 轮询任务并下载 2K 结果；
5. 将本地模型版本、API 任务、生成设置和后期处理记录在一起。

官方入口：

- [Create H3-2K（中国区）](https://platform.minimaxi.com/docs/api-reference/video-generation-v2-create)
- [H3-Context-IR（中国区）](https://platform.minimaxi.com/docs/api-reference/video-generation-v2-h3-context-ir)
- [H3-Regenerate-2K（中国区）](https://platform.minimaxi.com/docs/api-reference/video-generation-v2-regeneration)
- [Create H3-2K（全球）](https://platform.minimax.io/docs/api-reference/video-generation-v2-create)
- [H3-Context-IR（全球）](https://platform.minimax.io/docs/api-reference/video-generation-v2-h3-context-ir)
- [H3-Regenerate-2K（全球）](https://platform.minimax.io/docs/api-reference/video-generation-v2-regeneration)
- [MiniMax-H3 官方完整 2K 示例](https://github.com/MiniMax-AI/MiniMax-H3#full-2k-workflow)

不要把 API Token、授权头、私人素材地址、带时效的下载地址或用户隐私信息提交到 Git。

### 11. 其他框架

| 路径 | 适合用户 | 官方或上游文档 |
|---|---|---|
| SGLang | 多 GPU 服务、OpenAI 兼容异步接口、生产验证 | [H3 cookbook](https://docs.sglang.io/cookbook/diffusion/MiniMax/MiniMax-H3) |
| vLLM | 已使用 vLLM 视频推理栈的团队 | [H3 recipes](https://recipes.vllm.ai/MiniMaxAI/MiniMax-H3) |
| Diffusers | Python 流水线、实验和组件级开发 | [H3 pipeline docs](https://github.com/huggingface/diffusers/blob/minimax-h3/docs/source/en/api/pipelines/minimax_h3.md) |
| ComfyUI | 节点式工作流、原型验证和创作者 | [H3 tutorial](https://docs.comfy.org/tutorials/video/minimax/minimax-h3) |

这些框架更新很快。本项目不复制未验证的版本号或依赖锁定；请固定你实际测试过的提交、镜像或发布版本。

### 12. 常见问题

**服务启动后立即显存不足**

检查是否误用了不适合当前 GPU 的并行拓扑；降低参考素材、时长或输出尺寸不能替代正确的权重放置方案。先采用官方已验证的硬件配置。

**首帧被重新构图**

确认使用 FL2VA 和 keyframe，而不是把首帧当作 Ref2VA 的普通参考图。

**视频参考没有逐帧保留**

这是 Ref2VA 的语义参考特性，不是像素对齐编辑接口。不要把它当成带 denoising-strength 的传统视频重绘。

**只有音频参考时请求失败**

Ref2VA 不支持音频作为唯一输入；请同时提供图片或视频。

**本地结果不是 2K**

H3-Base 本地开放流程输出 768p。2K 需要当前官方混合流程中的 H3-Regenerate-2K。

**生成结果与官网不同**

记录权重修订、框架版本、硬件拓扑、Context-IR 来源、步数、flow shift、种子、输入转码和后处理。官网完整系统与纯本地 H3-Base 不是相同的执行路径。

### 13. 生产化检查清单

- 固定模型 revision、推理框架、容器镜像、驱动和依赖版本；
- 将服务监听在内网，使用 TLS、鉴权、请求大小限制、速率限制和队列；
- 参考素材目录以只读方式挂载，拒绝任意服务器路径和未经验证的远程 URL；
- 为提交、轮询、下载设置超时、退避、最大重试次数和取消机制；
- 限制并发任务、单任务参考素材数量、输入总时长和输出保留期限；
- 监控 GPU 显存/利用率、主机内存、模型加载时间、排队时间、推理时间、失败率和磁盘空间；
- 对输入和输出执行权限、隐私、恶意文件、内容安全和许可证检查；
- 记录提示词、素材哈希、模型 revision、任务类型、采样参数、种子、输出哈希和人工编辑；
- 使用少量固定的原创回归提示词做版本升级前后的视听对比；
- 自动清理临时转码、失败任务和过期输出，但保留必要的审计记录；
- 不在公开日志中输出 Token、私人 URL、完整用户提示词或个人数据；
- 在扩大 GPU 拓扑或启用量化、缓存、编译前，分别验证视频和音频质量。

本项目只提供部署说明，不把未经实机验证的 Docker、Kubernetes 或云厂商配置标记为“生产可用”。部署配置必须在目标硬件、驱动和网络环境中重新验证。

## English deployment reference

1. Read the current [Community License](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE).
2. Choose FL2VA for text, first frame, last frame, or first-and-last-frame generation.
3. Choose Ref2VA for semantic image, video, and audio references; V2V is a Ref2VA use case.
4. Install SGLang diffusion dependencies with uv pip install "sglang[diffusion]" --prerelease=allow.
5. Use the verified hardware preset from the [SGLang H3 deployment selector](https://docs.sglang.io/cookbook/diffusion/MiniMax/MiniMax-H3#3-serve-minimax-h3).
6. Serve the appropriate model variant, submit an asynchronous POST request to /v1/videos, poll the returned job ID, and download the completed MP4.
7. Expect local H3-Base output at a 768-pixel short edge. H3-Context-IR and H3-Regenerate-2K are hosted components and are not part of the current open release.
8. Validate frame rate, video/audio streams, prompt fidelity, reference behavior, rights, safety, and reproducibility metadata.

For copy-ready commands and troubleshooting, use the Simplified Chinese sections above; commands and field names are language-independent.

## 日本語クイックスタート

1. 最新の Community License を確認します。
2. テキストまたは開始・終了フレームには FL2VA、画像・動画・音声の意味参照には Ref2VA を選びます。
3. SGLang の公式ハードウェア設定を使用し、独自に GPU 構成を推測しないでください。
4. ローカル H3-Base は主に 768p を生成します。2K にはホスト型 Context-IR と Regenerate-2K が必要です。
5. 出力 MP4 の 24 FPS、ステレオ音声、解像度、権利、再現情報を確認します。

## 한국어 빠른 시작

1. 최신 Community License를 먼저 확인합니다.
2. 텍스트·첫 프레임·마지막 프레임은 FL2VA, 이미지·영상·오디오 의미 참조는 Ref2VA를 사용합니다.
3. SGLang에서 검증된 하드웨어 프리셋을 선택하고 임의의 병렬 구성을 적용하지 마세요.
4. 로컬 H3-Base 출력은 주로 768p이며 2K에는 호스팅 Context-IR 및 Regenerate-2K가 필요합니다.
5. MP4의 24 FPS, 스테레오 오디오, 해상도, 권리 및 재현 기록을 검증합니다.

## Inicio rápido en español

1. Revisa la Community License vigente.
2. Usa FL2VA para texto y fotogramas inicial/final; usa Ref2VA para referencias semánticas de imagen, video y audio.
3. Elige una configuración de hardware validada por SGLang.
4. H3-Base local produce principalmente a 768p; el flujo 2K necesita Context-IR y Regenerate-2K alojados.
5. Verifica 24 FPS, audio estéreo, resolución, derechos y datos de reproducibilidad.

## Démarrage rapide en français

1. Consultez la Community License actuelle.
2. Utilisez FL2VA pour le texte et les images clés de début/fin, Ref2VA pour les références sémantiques image, vidéo et audio.
3. Choisissez une configuration matérielle validée par SGLang.
4. H3-Base local produit principalement en 768p ; le flux 2K requiert Context-IR et Regenerate-2K hébergés.
5. Vérifiez les 24 FPS, l’audio stéréo, la résolution, les droits et les données de reproductibilité.

## Deutscher Schnellstart

1. Prüfen Sie die aktuelle Community License.
2. Verwenden Sie FL2VA für Text und Start-/Endframes, Ref2VA für semantische Bild-, Video- und Audioreferenzen.
3. Wählen Sie eine von SGLang validierte Hardwarekonfiguration.
4. Lokales H3-Base erzeugt hauptsächlich 768p; für 2K werden die gehosteten Module Context-IR und Regenerate-2K benötigt.
5. Prüfen Sie 24 FPS, Stereo-Audio, Auflösung, Rechte und Reproduzierbarkeitsdaten.

## Início rápido em português

1. Leia a Community License atual.
2. Use FL2VA para texto e quadros inicial/final; use Ref2VA para referências semânticas de imagem, vídeo e áudio.
3. Escolha uma configuração de hardware validada pelo SGLang.
4. O H3-Base local gera principalmente em 768p; o fluxo 2K exige Context-IR e Regenerate-2K hospedados.
5. Verifique 24 FPS, áudio estéreo, resolução, direitos e dados de reprodutibilidade.

## البدء السريع بالعربية

1. راجع اتفاقية Community License الحالية.
2. استخدم FL2VA للنص والإطار الأول أو الأخير، واستخدم Ref2VA لمراجع الصور والفيديو والصوت الدلالية.
3. اختر إعداد عتاد تم التحقق منه في وثائق SGLang.
4. ينتج H3-Base المحلي دقة 768p أساسًا، بينما يحتاج مسار 2K إلى Context-IR وRegenerate-2K المستضافين.
5. تحقّق من 24 إطارًا في الثانية والصوت المجسم والدقة والحقوق وبيانات إعادة الإنتاج.

## Primary sources

- [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3)
- [MiniMax H3 model and weights](https://huggingface.co/MiniMaxAI/MiniMax-H3)
- [SGLang MiniMax-H3 cookbook](https://docs.sglang.io/cookbook/diffusion/MiniMax/MiniMax-H3)
- [ComfyUI MiniMax H3 tutorial](https://docs.comfy.org/tutorials/video/minimax/minimax-h3)
- [Official reproducible request scripts](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/scripts/readme)

Continue with the [official example-video index](./official-h3-examples.md), [H3 overview](./minimax-h3-overview.md), [prompt guide](./prompting-guide.md), or [84-prompt library](../prompts/README.md).
