# Multilingual MiniMax H3 Prompting

The 84 English recipes are the canonical source. This sampler demonstrates how to localize a complete creative specification—not only translate style keywords—across eight additional languages.

**Languages in this sampler:** 简体中文 · 日本語 · 한국어 · Español · Français · Deutsch · Português · العربية

## Localization rules

1. Keep reference labels stable: `Image 1`, `Video 1`, and `Audio 1` should match the uploaded asset order.
2. Translate creative direction, action, camera, timing, sound, continuity, and negative constraints together.
3. Keep required on-screen copy in quotes and identify its intended language explicitly.
4. Do not translate model identifiers, file names, product geometry, or approved brand spelling.
5. For right-to-left output, define reading direction and UI mirroring separately from scene direction.
6. Review culturally specific clothing, gestures, food, architecture, geography, and legal disclosure with a knowledgeable human.

## 简体中文：山顶观测站茶饮发布片

```text
为虚构茶饮品牌“NORTH WINDOW”制作一支 16:9 高级新品发布短片。图1只用于锁定瓶身：烟灰色高挑玻璃瓶、浅石色标签、深绿色瓶盖，标签位置与拼写必须保持不变；图2只用于观测站的圆形建筑、望远镜结构与蓝调黎明色彩。

开场：一束狭窄星光滑过桌面，逐渐显露瓶身轮廓，镜头水平缓慢推进。中段：瓶壁自然凝结水汽，一滴水沿真实曲面下滑；观测站屋顶打开，冷色天光进入。结尾：产品保持静止，远方地平线从靛蓝转为一条克制的暖金色，镜头停在留有上方文案安全区的英雄画面。

声音意图：屋顶机械声、远处风声、一记低沉玻璃音，不要旁白。避免漂浮原料、液体爆炸、标签变化、夸张光晕、额外文字、第三方品牌和水印。
```

## 日本語：デスクライトの自然なファーストインプレッション

```text
夕暮れの小さなホームオフィスで、縦型9:16の自然な商品体験動画を作る。画像1の成人クリエイターの顔・髪型・服装を維持する。画像2の「FOLDLINE」デスクライトは、細い黒い支柱、楕円形ベース、暖色のライトバー、真鍮色のヒンジを正確に保つ。これは架空のデモであり、実在する顧客の証言として見せない。

冒頭：撮影はすでに始まっており、クリエイターがライトをノートの横に置く。中盤：片手でヒンジを開き、ベースを一度タップし、スケッチを光の下へ滑らせる。露出は一度だけ自然に調整され、その後安定する。最後：画面への映り込みが減るようにライトの角度を変え、小さくうなずく。

音：ヒンジ、タップ、紙、遠い街の環境音。過剰な美肌、手と商品の融合、誇張した販売字幕、架空の評価、ロゴ追加、透かしを避ける。
```

## 한국어：화이트 피치 로즈메리 스파클링 티 광고

```text
가상의 음료 “MEADOW FIZZ” 화이트 피치 로즈메리 티를 위한 9:16 세로형 매크로 광고를 만든다. 이미지 1의 투명한 세로 골 유리병, 옅은 금빛 액체, 크림색 라벨, 세이지색 캡을 정확히 유지하고 라벨 문구나 효능 표현을 새로 만들지 않는다. 이미지 2는 실제 로즈메리 가지와 흰 복숭아 조각의 형태만 참고한다.

시작은 차가운 병 표면의 클로즈업이다. 작은 탄산 기포가 액체 안에서 올라오고 병 어깨에 응결 방울 하나가 생긴다. 중간에는 캡이 절제된 소리와 함께 열리고, 음료가 투명한 긴 잔에 한 번에 부어진다. 기포가 로즈메리와 복숭아 주변에 자연스럽게 모인다. 마지막에는 카메라가 잔을 조금 돌아 병 라벨과 위쪽 여백을 함께 보여준다.

과일 폭발, 떠다니는 재료, 과도한 거품, 병 형태 변화, 거울처럼 뒤집힌 라벨, 추가 슬로건과 워터마크를 피한다.
```

## Español：Revelación de una casa de huéspedes en una isla volcánica

```text
Crear un video horizontal de 10 segundos para una casa de huéspedes ficticia situada en una isla volcánica. La Imagen 1 define la habitación: paredes encaladas, cama baja de roble, cabecero tejido, suelo de piedra negra y cortinas de lino. La Imagen 2 solo define la costa de lava oscura y el horizonte oceánico. La Imagen 3 fija la posición de la puerta y la ventana.

Comenzar con un primer plano de una llave de latón sobre una repisa. La cámara retrocede mientras la puerta se abre y revela, en un único movimiento, la cama y la ventana. Las cortinas reaccionan suavemente al aire marino. La cámara continúa a altura humana y termina en la terraza, donde dos sillas vacías miran hacia la costa.

La exposición cambia de forma natural entre el interior cálido y el exterior frío. Sonido: llave, pestillo, tela y oleaje distante. No añadir piscina, servicios, valoraciones, texto promocional, geometría imposible ni marcas de agua.
```

## Français：Éditorial lunettes — étude du vent

```text
Créer un film de mode vertical minimaliste dans un studio gris chaud. Conserver l’identité du modèle adulte de l’Image 1 : même visage, cheveux courts texturés, peau naturelle et col montant anthracite. Reconstruire exactement les lunettes des Images 2 et 3 : monture fumée translucide, verres ovales étroits, charnières argentées et branches droites. La Vidéo 1 sert uniquement de référence pour le rythme du mouvement de tête.

Ouverture en gros plan : le modèle regarde légèrement hors champ pendant qu’un ventilateur contrôlé déplace seulement quelques mèches. La caméra glisse lentement sur le côté tandis que le modèle tourne le visage vers l’objectif. Une lumière traverse une seule fois les verres sans cacher les yeux. Finir sur un gros plan frontal stable, menton légèrement baissé et regard calme.

Éviter toute modification du visage ou de la monture, les reflets opaques, les lunettes dupliquées, la peau plastique, les bijoux ajoutés, les logos et les filigranes.
```

## Deutsch：Produktrundgang für einen Fokus-Timer

```text
Erstelle eine 16:9-Produktdemo für den fiktiven Desktop-Fokus-Timer „QUIET HOUR“. Übernimm ausschließlich die freigegebenen UI-Zustände aus Bild 1 bis 3: dunkles Fenster, helle Timer-Karte, grüner Fortschrittsring, Aufgabenliste und Pausensteuerung. Alle gelieferten Texte müssen exakt erhalten bleiben; keine Kennzahlen, Bewertungen oder Menüpunkte erfinden.

Beginne im Ruhezustand. Der Cursor wählt eine Aufgabe und klickt auf Start. Die Oberfläche wechselt mit einer kurzen, ruhigen Bewegung in den aktiven Zustand; der Ring schreitet leicht voran und die aktive Aufgabe erhält eine grüne Markierung. Eine einzelne Benachrichtigung erscheint. Der Nutzer aktiviert „Silence alerts“, danach klappt die Meldung zusammen. Abschließend herauszoomen und die unveränderte App auf einem realistischen Laptop zeigen.

Nur zwei dezente Klicks und ein gedämpfter Ton. Keine unlesbare Mikroschrift, erfundenen Diagramme, zufälligen Hover-Effekte, zusätzlichen Fenster, Markenlogos oder Wasserzeichen.
```

## Português：Comédia silenciosa em uma lavanderia automática

```text
Criar uma comédia vertical e discreta na lavanderia da Imagem 2. Manter a criatura original da Imagem 1: pele verde-menta, três olhos, capa de chuva azul-marinho, duas mãos e corpo pequeno. A criatura é amigável e fictícia. A Imagem 3 define a ordem correta de uso da máquina.

No início, a criatura observa a porta redonda da lavadora e coloca cuidadosamente uma única meia listrada no tambor. Fecha a porta, insere uma ficha simples e pressiona o botão aprovado. Quando o tambor começa a girar, os três olhos acompanham a meia em perfeita sincronia circular. A criatura abre um caderno, desenha apenas uma espiral sem palavras e então percebe que a meia correspondente já está em seu próprio pé. Ela olha para a câmera, envergonhada, sem falar.

Som: ficha, botão, tambor e tecido. Evitar aparência assustadora, membros extras, uso perigoso da máquina, textos gerados, semelhança com personagens conhecidos, logos ou marca-d’água.
```

## العربية：سوق مسائي من منظور الزائر

```text
أنشئ فيديو عمودياً بنسبة 9:16 من منظور شخص يسير في السوق المسائي الظاهر في الصورتين 1 و2. استخدم الصورة 3 فقط لتحديد المسار: مدخل الفوانيس، ثم بائع الفاكهة، ثم عربة الطعام المطهو بالبخار، ثم منطقة جلوس صغيرة. لا تخترع أسماء متاجر أو أسعاراً قابلة للقراءة.

تتحرك الكاميرا بسرعة مشي مريحة مع ثبات طبيعي، من دون الاصطدام بالناس. عند بائع الفاكهة تتوقف لحظة بينما يزن ثلاث برتقالات. عند عربة الطعام يُرفع غطاء من الخيزران، فيمر البخار أمام العدسة لفترة قصيرة من دون إخفاء الطريق. ينتهي الفيديو بالانعطاف نحو منطقة الجلوس حيث تظهر طاولة فارغة واحدة.

الإضاءة مزيج من دفء الأكشاك وبرودة المساء، مع ألوان بشرة طبيعية. الصوت: ضجيج سوق هادئ، نقرة الميزان، بخار وأدوات. تجنب تكرار الوجوه، القفز المكاني، النصوص المشوهة، الصور النمطية، العلامات التجارية والعلامة المائية.
```

## Human review checklist

- Reference numbering still matches the uploaded assets;
- Required copy, punctuation, names, and reading direction are correct;
- Camera direction was not accidentally mirrored during RTL localization;
- Cultural, geographic, and product details are appropriate;
- Audio and dialogue intent sound natural to a native speaker;
- The localized version preserves every safety and continuity constraint.

Return to the [84-prompt library](../prompts/README.md).
