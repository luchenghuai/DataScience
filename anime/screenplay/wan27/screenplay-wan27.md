# 《分寸》Wan 2.7 Reference-to-Video 制作包（32 镜）

本包把 Dreamina 的 32 镜提示词转换为 Alibaba Cloud Model Studio `wan2.7-r2v-2026-06-12` 新协议。每镜包含 Wan R2V prompt、`first_frame`、最多 5 个 `reference_image`、负面提示和生成参数。

## 全局 API 规则

- Singapore workspace endpoint: `POST https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/api/v1/services/aigc/video-generation/video-synthesis`
- Required headers: `Authorization: Bearer $DASHSCOPE_API_KEY`, `Content-Type: application/json`, `X-DashScope-Async: enable`.
- Poll: `GET https://{WorkspaceId}.ap-southeast-1.maas.aliyuncs.com/api/v1/tasks/{task_id}` about every 15 seconds.
- Model, workspace, API key and endpoint must be in the same region. Output URLs expire after 24 hours; download immediately.
- Shot 001 uses its staging image as the baseline `first_frame`. Shot 002–032 use the previous completed shot’s literal extracted final frame.
- Reference identifiers count only `reference_image` entries: first reference image is `Image 1`. The `first_frame` is described separately.
- Wan limit: 1 first frame plus 1–5 reference images/videos. Character reference images contain one character each.
- `prompt_extend` is false to protect exact dialogue/timing. Test at 720P; change to 1080P only after approval.

## Shot 001｜00:00–00:03
- Speaker/dialogue: **闺蜜甲**：如烟，你输了！
- Screenplay duration: `3s`; Wan request: `3s`
- Transition: `BASELINE`
- Media array order:
  - `first_frame`: [baseline staging frame containing the complete six-person composition and KTV set](references/staging/shot_001.jpg)
  - `reference_image` / Image 1: [identity and wardrobe for 闺蜜甲](references/characters/guimi-1.jpg)
  - `reference_image` / Image 2: [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
  - `reference_image` / Image 5: [identity and wardrobe for 闺蜜乙](references/characters/guimi-2.jpg)
- Five-reference-limit note: omitted separate anchors: 闺蜜丙; identity remains anchored by the first frame/staging reference.
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 001 (00:00–00:03)

REFERENCE MAP:
The supplied first frame is baseline staging frame containing the complete six-person composition and KTV set. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the identity and wardrobe for 闺蜜甲. Use it only for that role and preserve supported visual details.
Image 2 is the identity and wardrobe for 柳如烟. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 伊藤诚. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 季伯达. Use it only for that role and preserve supported visual details.
Image 5 is the identity and wardrobe for 闺蜜乙. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 3-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Wide ensemble establishing shot, eye level, preserving the full seating geography and coffee table.
Visible actors: Visible: exactly six people—柳如烟 and 伊藤诚 together on the left seating; 闺蜜甲/乙/丙 across the central sofa in fixed order; 季伯达 at the right facing them. Four women and two men total; no background guests, no extra, duplicated, or missing people.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
During the wide party tableau, 闺蜜甲 turns toward 柳如烟, leans forward slightly, raises one hand to claim attention, and says “如烟，你输了！” with playful excitement; 柳如烟 shifts her gaze toward her while the others quiet down and watch.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.4s: hold the established composition; 闺蜜甲 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.4–2.7s: 闺蜜甲 speaks the exact Mandarin line “如烟，你输了！” once, with natural restrained lip sync and the shot-specific performance: During the wide party tableau, 闺蜜甲 turns toward 柳如烟, leans forward slightly, raises one hand to claim attention, and says “如烟，你输了！” with playful excitement; 柳如烟 shifts her gaze toward her while the others quiet down and watch. 2.7–3.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Very slow 3% push-in with subtle parallax across the coffee table. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 闺蜜甲 speaks: “如烟，你输了！”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_001.json`](shot-requests/shot_001.json)

## Shot 002｜00:03–00:05
- Speaker/dialogue: **闺蜜甲**：选真心话还是大冒险？
- Screenplay duration: `2s`; Wan request: `2s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 001](frames/shot_001_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_002.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 闺蜜甲](references/characters/guimi-1.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 闺蜜乙](references/characters/guimi-2.jpg)
  - `reference_image` / Image 5: [identity and wardrobe for 闺蜜丙](references/characters/guimi-3.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 002 (00:03–00:05)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 001. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 闺蜜甲. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 闺蜜乙. Use it only for that role and preserve supported visual details.
Image 5 is the identity and wardrobe for 闺蜜丙. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 2-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Medium three-shot of the three girlfriends across the sofa; 闺蜜甲 is the visual lead.
Visible actors: Visible: exactly the same three girlfriends only—闺蜜甲 on sofa left, 闺蜜乙 center, 闺蜜丙 right. No fourth person, no background guests, and no seat swaps.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
闺蜜甲 remains leaning forward after announcing the loss, keeps her attention on 柳如烟, and asks “选真心话还是大冒险？” with playful excitement; 闺蜜乙 turns to listen and 闺蜜丙 relaxes with empty hands.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.2s: hold the established composition; 闺蜜甲 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.2–1.8s: 闺蜜甲 speaks the exact Mandarin line “选真心话还是大冒险？” once, with natural restrained lip sync and the shot-specific performance: 闺蜜甲 remains leaning forward after announcing the loss, keeps her attention on 柳如烟, and asks “选真心话还是大冒险？” with playful excitement; 闺蜜乙 turns to listen and 闺蜜丙 relaxes with empty hands. 1.8–2.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Gentle 2% push-in toward 闺蜜甲; no pan. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 闺蜜甲 speaks: “选真心话还是大冒险？”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_002.json`](shot-requests/shot_002.json)

## Shot 003｜00:05–00:06
- Speaker/dialogue: **柳如烟**：真心话。
- Screenplay duration: `1s`; Wan request: `2s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 002](frames/shot_002_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_003.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 003 (00:05–00:06)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 002. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 柳如烟. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 伊藤诚. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 2-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Tight medium close-up on 柳如烟 at frame left; 伊藤诚 remains partially visible beside/behind her.
Visible actors: Visible: 柳如烟 seated at frame left with 伊藤诚 immediately to her right; one or more sofa friends may remain soft in the background exactly as in the source JPG. 柳如烟 does not stand or cross the room.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
柳如烟 answers promptly and evenly, a tiny nod and confident eye contact.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.1s: hold the established composition; 柳如烟 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.1–0.9s: 柳如烟 speaks the exact Mandarin line “真心话。” once, with natural restrained lip sync and the shot-specific performance: 柳如烟 answers promptly and evenly, a tiny nod and confident eye contact. 0.9–1.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Near-locked shot with a tiny 1% push-in. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 柳如烟 speaks: “真心话。”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_003.json`](shot-requests/shot_003.json)

## Shot 004｜00:06–00:09
- Speaker/dialogue: **闺蜜乙**：那就说说，你今天穿的内裤是什么颜色？
- Screenplay duration: `3s`; Wan request: `3s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 003](frames/shot_003_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_004.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 闺蜜甲](references/characters/guimi-1.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 闺蜜乙](references/characters/guimi-2.jpg)
  - `reference_image` / Image 5: [identity and wardrobe for 闺蜜丙](references/characters/guimi-3.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 004 (00:06–00:09)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 003. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 闺蜜甲. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 闺蜜乙. Use it only for that role and preserve supported visual details.
Image 5 is the identity and wardrobe for 闺蜜丙. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 3-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Medium three-shot of the girlfriends; center emphasis on 闺蜜乙.
Visible actors: Visible: exactly the same three girlfriends only—闺蜜甲 on sofa left, 闺蜜乙 center, 闺蜜丙 right. No fourth person, no background guests, and no seat swaps.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
闺蜜乙 taps/indicates the table lightly and teases; 闺蜜甲 turns toward her; 闺蜜丙 watches 柳如烟.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.4s: hold the established composition; 闺蜜乙 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.4–2.7s: 闺蜜乙 speaks the exact Mandarin line “那就说说，你今天穿的内裤是什么颜色？” once, with natural restrained lip sync and the shot-specific performance: 闺蜜乙 taps/indicates the table lightly and teases; 闺蜜甲 turns toward her; 闺蜜丙 watches 柳如烟. 2.7–3.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Slow 3% push toward 闺蜜乙; keep all three faces stable. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 闺蜜乙 speaks: “那就说说，你今天穿的内裤是什么颜色？”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_004.json`](shot-requests/shot_004.json)

## Shot 005｜00:09–00:10
- Speaker/dialogue: **伊藤诚**：粉红色。
- Screenplay duration: `1s`; Wan request: `2s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 004](frames/shot_004_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_005.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 005 (00:09–00:10)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 004. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 柳如烟. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 伊藤诚. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 2-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Tight two-shot favoring 伊藤诚 beside 柳如烟; keep 柳如烟 visible for reaction.
Visible actors: Visible: 伊藤诚 seated immediately right of 柳如烟; 柳如烟 remains at frame left and a sofa friend may appear behind. Preserve their close seated spacing without adding contact.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
伊藤诚 answers too quickly with casual certainty; 柳如烟 registers immediate discomfort.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.1s: hold the established composition; 伊藤诚 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.1–0.9s: 伊藤诚 speaks the exact Mandarin line “粉红色。” once, with natural restrained lip sync and the shot-specific performance: 伊藤诚 answers too quickly with casual certainty; 柳如烟 registers immediate discomfort. 0.9–1.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Near-locked 1% push-in for comic timing. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 伊藤诚 speaks: “粉红色。”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_005.json`](shot-requests/shot_005.json)

## Shot 006｜00:10–00:14
- Speaker/dialogue: **伊藤诚**：如烟一直拿我当姐妹。她的内裤，我以前都帮她洗过。
- Screenplay duration: `4s`; Wan request: `4s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 005](frames/shot_005_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_006.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 006 (00:10–00:14)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 005. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 柳如烟. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 伊藤诚. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 4-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Tight two-shot favoring 伊藤诚 beside 柳如烟, with a friend softly present in the background.
Visible actors: Visible: 伊藤诚 seated immediately right of 柳如烟; 柳如烟 remains at frame left and a sofa friend may appear behind. Preserve their close seated spacing without adding contact.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
伊藤诚 continues matter-of-factly, small explanatory hand gesture; 柳如烟 stiffens while the background friend watches.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.5s: hold the established composition; 伊藤诚 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.5–3.6s: 伊藤诚 speaks the exact Mandarin line “如烟一直拿我当姐妹。她的内裤，我以前都帮她洗过。” once, with natural restrained lip sync and the shot-specific performance: 伊藤诚 continues matter-of-factly, small explanatory hand gesture; 柳如烟 stiffens while the background friend watches. 3.6–4.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Slow 2% push-in, no reframing. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 伊藤诚 speaks: “如烟一直拿我当姐妹。她的内裤，我以前都帮她洗过。”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_006.json`](shot-requests/shot_006.json)

## Shot 007｜00:14–00:16
- Speaker/dialogue: **柳如烟**：你胡说什么呢？
- Screenplay duration: `2s`; Wan request: `2s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 006](frames/shot_006_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_007.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 007 (00:14–00:16)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 006. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 柳如烟. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 伊藤诚. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 2-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Tight medium close-up on 柳如烟, with 伊藤诚 partly visible beside her.
Visible actors: Visible: 柳如烟 seated at frame left with 伊藤诚 immediately to her right; one or more sofa friends may remain soft in the background exactly as in the source JPG. 柳如烟 does not stand or cross the room.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
柳如烟 snaps her gaze toward 伊藤诚, brows tightening; brief embarrassed protest.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.2s: hold the established composition; 柳如烟 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.2–1.8s: 柳如烟 speaks the exact Mandarin line “你胡说什么呢？” once, with natural restrained lip sync and the shot-specific performance: 柳如烟 snaps her gaze toward 伊藤诚, brows tightening; brief embarrassed protest. 1.8–2.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Brief 2% push-in synchronized to the protest. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 柳如烟 speaks: “你胡说什么呢？”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_007.json`](shot-requests/shot_007.json)

## Shot 008｜00:16–00:18
- Speaker/dialogue: **闺蜜甲**：姐夫，你可别多想。他们从小一起长大。
- Screenplay duration: `2s`; Wan request: `2s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 007](frames/shot_007_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_008.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 闺蜜甲](references/characters/guimi-1.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 闺蜜乙](references/characters/guimi-2.jpg)
  - `reference_image` / Image 5: [identity and wardrobe for 闺蜜丙](references/characters/guimi-3.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 008 (00:16–00:18)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 007. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 闺蜜甲. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 闺蜜乙. Use it only for that role and preserve supported visual details.
Image 5 is the identity and wardrobe for 闺蜜丙. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 2-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Medium three-shot of the girlfriends; 闺蜜甲 leads from sofa left.
Visible actors: Visible: exactly the same three girlfriends only—闺蜜甲 on sofa left, 闺蜜乙 center, 闺蜜丙 right. No fourth person, no background guests, and no seat swaps.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
闺蜜甲 raises a calming palm toward 季伯达 and explains earnestly; the other two listen.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.2s: hold the established composition; 闺蜜甲 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.2–1.8s: 闺蜜甲 speaks the exact Mandarin line “姐夫，你可别多想。他们从小一起长大。” once, with natural restrained lip sync and the shot-specific performance: 闺蜜甲 raises a calming palm toward 季伯达 and explains earnestly; the other two listen. 1.8–2.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Gentle 2% push toward 闺蜜甲. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 闺蜜甲 speaks: “姐夫，你可别多想。他们从小一起长大。”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_008.json`](shot-requests/shot_008.json)

## Shot 009｜00:18–00:20
- Speaker/dialogue: **闺蜜乙**：就是，伊藤诚在我们眼里根本不算男人。
- Screenplay duration: `2s`; Wan request: `2s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 008](frames/shot_008_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_009.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 闺蜜甲](references/characters/guimi-1.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 闺蜜乙](references/characters/guimi-2.jpg)
  - `reference_image` / Image 5: [identity and wardrobe for 闺蜜丙](references/characters/guimi-3.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 009 (00:18–00:20)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 008. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 闺蜜甲. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 闺蜜乙. Use it only for that role and preserve supported visual details.
Image 5 is the identity and wardrobe for 闺蜜丙. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 2-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Medium three-shot of the girlfriends; 闺蜜乙 leads from sofa center.
Visible actors: Visible: exactly the same three girlfriends only—闺蜜甲 on sofa left, 闺蜜乙 center, 闺蜜丙 right. No fourth person, no background guests, and no seat swaps.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
闺蜜乙 turns toward 季伯达 and adds reassurance; 闺蜜甲 settles back; 闺蜜丙 gives a restrained nod.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.2s: hold the established composition; 闺蜜乙 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.2–1.8s: 闺蜜乙 speaks the exact Mandarin line “就是，伊藤诚在我们眼里根本不算男人。” once, with natural restrained lip sync and the shot-specific performance: 闺蜜乙 turns toward 季伯达 and adds reassurance; 闺蜜甲 settles back; 闺蜜丙 gives a restrained nod. 1.8–2.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Tiny lateral ease from left to center, ending on 闺蜜乙. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 闺蜜乙 speaks: “就是，伊藤诚在我们眼里根本不算男人。”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_009.json`](shot-requests/shot_009.json)

## Shot 010｜00:20–00:22
- Speaker/dialogue: **闺蜜丙**：他们是纯友谊，关系好才这样。
- Screenplay duration: `2s`; Wan request: `2s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 009](frames/shot_009_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_010.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 闺蜜甲](references/characters/guimi-1.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 闺蜜乙](references/characters/guimi-2.jpg)
  - `reference_image` / Image 5: [identity and wardrobe for 闺蜜丙](references/characters/guimi-3.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 010 (00:20–00:22)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 009. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 闺蜜甲. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 闺蜜乙. Use it only for that role and preserve supported visual details.
Image 5 is the identity and wardrobe for 闺蜜丙. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 2-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Medium three-shot of the girlfriends; 闺蜜丙 leads from sofa right.
Visible actors: Visible: exactly the same three girlfriends only—闺蜜甲 on sofa left, 闺蜜乙 center, 闺蜜丙 right. No fourth person, no background guests, and no seat swaps.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
闺蜜丙 lowers her hand and concludes calmly; the other two turn to her.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.2s: hold the established composition; 闺蜜丙 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.2–1.8s: 闺蜜丙 speaks the exact Mandarin line “他们是纯友谊，关系好才这样。” once, with natural restrained lip sync and the shot-specific performance: 闺蜜丙 lowers her hand and concludes calmly; the other two turn to her. 1.8–2.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Tiny ease right to favor 闺蜜丙. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 闺蜜丙 speaks: “他们是纯友谊，关系好才这样。”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_010.json`](shot-requests/shot_010.json)

## Shot 011｜00:22–00:26
- Speaker/dialogue: **季伯达**：小伊，不是我说你。一个大男人，洗什么内裤？
- Screenplay duration: `4s`; Wan request: `4s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 010](frames/shot_010_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_011.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  - `reference_image` / Image 5: [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 011 (00:22–00:26)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 010. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 柳如烟. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 伊藤诚. Use it only for that role and preserve supported visual details.
Image 5 is the identity and wardrobe for 季伯达. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 4-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Over-shoulder/medium close-up favoring 季伯达 at the right foreground, facing left toward 伊藤诚.
Visible actors: Visible: 季伯达 occupies the right foreground in a white shirt, torso turned left toward 柳如烟/伊藤诚 and the opposite sofa; a seated friend may remain soft behind him. He remains seated and does not change sides.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
季伯达 begins controlled and faintly incredulous, looking toward 伊藤诚; one restrained open-palm gesture.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.5s: hold the established composition; 季伯达 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.5–3.6s: 季伯达 speaks the exact Mandarin line “小伊，不是我说你。一个大男人，洗什么内裤？” once, with natural restrained lip sync and the shot-specific performance: 季伯达 begins controlled and faintly incredulous, looking toward 伊藤诚; one restrained open-palm gesture. 3.6–4.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Slow 3% push-in; stable eyeline. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 季伯达 speaks: “小伊，不是我说你。一个大男人，洗什么内裤？”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_011.json`](shot-requests/shot_011.json)

## Shot 012｜00:26–00:31
- Speaker/dialogue: **季伯达**：我的内裤，都是我女闺蜜帮我洗的。你下次也让如烟替你洗。
- Screenplay duration: `5s`; Wan request: `5s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 011](frames/shot_011_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_012.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  - `reference_image` / Image 5: [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 012 (00:26–00:31)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 011. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 柳如烟. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 伊藤诚. Use it only for that role and preserve supported visual details.
Image 5 is the identity and wardrobe for 季伯达. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 5-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Matching medium close-up on 季伯达 from the same axis.
Visible actors: Visible: 季伯达 occupies the right foreground in a white shirt, torso turned left toward 柳如烟/伊藤诚 and the opposite sofa; a seated friend may remain soft behind him. He remains seated and does not change sides.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
季伯达 delivers the mirror example with deliberate calm, then subtly points the logic back toward 柳如烟.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.5s: hold the established composition; 季伯达 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.5–4.6s: 季伯达 speaks the exact Mandarin line “我的内裤，都是我女闺蜜帮我洗的。你下次也让如烟替你洗。” once, with natural restrained lip sync and the shot-specific performance: 季伯达 delivers the mirror example with deliberate calm, then subtly points the logic back toward 柳如烟. 4.6–5.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Slow 3% push-in, matching shot 011 axis. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 季伯达 speaks: “我的内裤，都是我女闺蜜帮我洗的。你下次也让如烟替你洗。”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_012.json`](shot-requests/shot_012.json)

## Shot 013｜00:31–00:36
- Speaker/dialogue: **柳如烟**：季伯达，你恶不恶心？你怎么能让别的女人给你洗内裤？
- Screenplay duration: `5s`; Wan request: `5s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 012](frames/shot_012_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_013.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  - `reference_image` / Image 5: [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 013 (00:31–00:36)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 012. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 柳如烟. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 伊藤诚. Use it only for that role and preserve supported visual details.
Image 5 is the identity and wardrobe for 季伯达. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 5-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Tight medium close-up on 柳如烟, 伊藤诚 partly visible beside her.
Visible actors: Visible: 柳如烟 seated at frame left with 伊藤诚 immediately to her right; one or more sofa friends may remain soft in the background exactly as in the source JPG. 柳如烟 does not stand or cross the room.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
柳如烟 recoils slightly, anger and disgust rising; she turns sharply toward 季伯达 and emphasizes the accusation.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.5s: hold the established composition; 柳如烟 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.5–4.6s: 柳如烟 speaks the exact Mandarin line “季伯达，你恶不恶心？你怎么能让别的女人给你洗内裤？” once, with natural restrained lip sync and the shot-specific performance: 柳如烟 recoils slightly, anger and disgust rising; she turns sharply toward 季伯达 and emphasizes the accusation. 4.6–5.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Controlled 3% push-in as anger rises. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 柳如烟 speaks: “季伯达，你恶不恶心？你怎么能让别的女人给你洗内裤？”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_013.json`](shot-requests/shot_013.json)

## Shot 014｜00:36–00:38
- Speaker/dialogue: **闺蜜甲**：这也太过分了吧？
- Screenplay duration: `2s`; Wan request: `2s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 013](frames/shot_013_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_014.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 闺蜜甲](references/characters/guimi-1.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 闺蜜乙](references/characters/guimi-2.jpg)
  - `reference_image` / Image 5: [identity and wardrobe for 闺蜜丙](references/characters/guimi-3.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 014 (00:36–00:38)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 013. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 闺蜜甲. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 闺蜜乙. Use it only for that role and preserve supported visual details.
Image 5 is the identity and wardrobe for 闺蜜丙. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 2-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Medium three-shot of the girlfriends, favoring 闺蜜甲 at left.
Visible actors: Visible: exactly the same three girlfriends only—闺蜜甲 on sofa left, 闺蜜乙 center, 闺蜜丙 right. No fourth person, no background guests, and no seat swaps.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
闺蜜甲 leans forward with a frown and challenges him; 闺蜜乙 watches his reaction; 闺蜜丙 raises one brow.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.2s: hold the established composition; 闺蜜甲 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.2–1.8s: 闺蜜甲 speaks the exact Mandarin line “这也太过分了吧？” once, with natural restrained lip sync and the shot-specific performance: 闺蜜甲 leans forward with a frown and challenges him; 闺蜜乙 watches his reaction; 闺蜜丙 raises one brow. 1.8–2.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Gentle 2% push toward 闺蜜甲. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 闺蜜甲 speaks: “这也太过分了吧？”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_014.json`](shot-requests/shot_014.json)

## Shot 015｜00:38–00:41
- Speaker/dialogue: **闺蜜乙**：你都有女朋友了，怎么一点边界感都没有？
- Screenplay duration: `3s`; Wan request: `3s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 014](frames/shot_014_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_015.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 闺蜜甲](references/characters/guimi-1.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 闺蜜乙](references/characters/guimi-2.jpg)
  - `reference_image` / Image 5: [identity and wardrobe for 闺蜜丙](references/characters/guimi-3.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 015 (00:38–00:41)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 014. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 闺蜜甲. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 闺蜜乙. Use it only for that role and preserve supported visual details.
Image 5 is the identity and wardrobe for 闺蜜丙. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 3-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Medium three-shot of the girlfriends, favoring 闺蜜乙 at center.
Visible actors: Visible: exactly the same three girlfriends only—闺蜜甲 on sofa left, 闺蜜乙 center, 闺蜜丙 right. No fourth person, no background guests, and no seat swaps.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
闺蜜乙 sits upright and stresses “边界感”; 闺蜜甲 nods once; 闺蜜丙 shows agreement.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.4s: hold the established composition; 闺蜜乙 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.4–2.7s: 闺蜜乙 speaks the exact Mandarin line “你都有女朋友了，怎么一点边界感都没有？” once, with natural restrained lip sync and the shot-specific performance: 闺蜜乙 sits upright and stresses “边界感”; 闺蜜甲 nods once; 闺蜜丙 shows agreement. 2.7–3.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Slow 3% push toward 闺蜜乙. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 闺蜜乙 speaks: “你都有女朋友了，怎么一点边界感都没有？”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_015.json`](shot-requests/shot_015.json)

## Shot 016｜00:41–00:44
- Speaker/dialogue: **季伯达**：怎么了？她是我女闺蜜啊。
- Screenplay duration: `3s`; Wan request: `3s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 015](frames/shot_015_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_016.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  - `reference_image` / Image 5: [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 016 (00:41–00:44)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 015. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 柳如烟. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 伊藤诚. Use it only for that role and preserve supported visual details.
Image 5 is the identity and wardrobe for 季伯达. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 3-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Matching medium close-up on 季伯达 at right foreground.
Visible actors: Visible: 季伯达 occupies the right foreground in a white shirt, torso turned left toward 柳如烟/伊藤诚 and the opposite sofa; a seated friend may remain soft behind him. He remains seated and does not change sides.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
季伯达 gives a mild shrug and repeats their premise without losing composure.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.4s: hold the established composition; 季伯达 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.4–2.7s: 季伯达 speaks the exact Mandarin line “怎么了？她是我女闺蜜啊。” once, with natural restrained lip sync and the shot-specific performance: 季伯达 gives a mild shrug and repeats their premise without losing composure. 2.7–3.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Near-locked shot, tiny 2% pull-back after the shrug. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 季伯达 speaks: “怎么了？她是我女闺蜜啊。”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_016.json`](shot-requests/shot_016.json)

## Shot 017｜00:44–00:47
- Speaker/dialogue: **伊藤诚**：女闺蜜也不行。男女之间得有分寸。
- Screenplay duration: `3s`; Wan request: `3s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 016](frames/shot_016_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_017.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 017 (00:44–00:47)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 016. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 柳如烟. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 伊藤诚. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 3-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Tight two-shot favoring 伊藤诚 beside 柳如烟.
Visible actors: Visible: 伊藤诚 seated immediately right of 柳如烟; 柳如烟 remains at frame left and a sofa friend may appear behind. Preserve their close seated spacing without adding contact.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
伊藤诚 turns serious, gives a small head shake, and lectures about boundaries; 柳如烟 watches.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.4s: hold the established composition; 伊藤诚 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.4–2.7s: 伊藤诚 speaks the exact Mandarin line “女闺蜜也不行。男女之间得有分寸。” once, with natural restrained lip sync and the shot-specific performance: 伊藤诚 turns serious, gives a small head shake, and lectures about boundaries; 柳如烟 watches. 2.7–3.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Slow 2% push-in toward 伊藤诚. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 伊藤诚 speaks: “女闺蜜也不行。男女之间得有分寸。”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_017.json`](shot-requests/shot_017.json)

## Shot 018｜00:47–00:53
- Speaker/dialogue: **季伯达**：奇怪了。刚才你说自己替柳如烟洗过内裤，你们不是也说只是姐妹吗？
- Screenplay duration: `6s`; Wan request: `6s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 017](frames/shot_017_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_018.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  - `reference_image` / Image 5: [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 018 (00:47–00:53)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 017. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 柳如烟. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 伊藤诚. Use it only for that role and preserve supported visual details.
Image 5 is the identity and wardrobe for 季伯达. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 6-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Medium close-up on 季伯达, same right-side axis.
Visible actors: Visible: 季伯达 occupies the right foreground in a white shirt, torso turned left toward 柳如烟/伊藤诚 and the opposite sofa; a seated friend may remain soft behind him. He remains seated and does not change sides.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
季伯达 calmly reconstructs the contradiction, gaze moving from 伊藤诚 to the group; gestures stay economical.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.5s: hold the established composition; 季伯达 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.5–5.6s: 季伯达 speaks the exact Mandarin line “奇怪了。刚才你说自己替柳如烟洗过内裤，你们不是也说只是姐妹吗？” once, with natural restrained lip sync and the shot-specific performance: 季伯达 calmly reconstructs the contradiction, gaze moving from 伊藤诚 to the group; gestures stay economical. 5.6–6.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Sustained 4% push-in over the full line. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 季伯达 speaks: “奇怪了。刚才你说自己替柳如烟洗过内裤，你们不是也说只是姐妹吗？”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_018.json`](shot-requests/shot_018.json)

## Shot 019｜00:53–00:55
- Speaker/dialogue: **柳如烟**：那不一样。
- Screenplay duration: `2s`; Wan request: `2s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 018](frames/shot_018_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_019.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 019 (00:53–00:55)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 018. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 柳如烟. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 伊藤诚. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 2-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Tight reaction close-up on 柳如烟.
Visible actors: Visible: 柳如烟 seated at frame left with 伊藤诚 immediately to her right; one or more sofa friends may remain soft in the background exactly as in the source JPG. 柳如烟 does not stand or cross the room.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
柳如烟 answers defensively, lips tightening and eyes briefly averting.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.2s: hold the established composition; 柳如烟 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.2–1.8s: 柳如烟 speaks the exact Mandarin line “那不一样。” once, with natural restrained lip sync and the shot-specific performance: 柳如烟 answers defensively, lips tightening and eyes briefly averting. 1.8–2.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Near-locked shot with a 2% push-in. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 柳如烟 speaks: “那不一样。”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_019.json`](shot-requests/shot_019.json)

## Shot 020｜00:55–00:57
- Speaker/dialogue: **季伯达**：哪里不一样？
- Screenplay duration: `2s`; Wan request: `2s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 019](frames/shot_019_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_020.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  - `reference_image` / Image 5: [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 020 (00:55–00:57)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 019. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 柳如烟. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 伊藤诚. Use it only for that role and preserve supported visual details.
Image 5 is the identity and wardrobe for 季伯达. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 2-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Tight medium close-up on 季伯达.
Visible actors: Visible: 季伯达 occupies the right foreground in a white shirt, torso turned left toward 柳如烟/伊藤诚 and the opposite sofa; a seated friend may remain soft behind him. He remains seated and does not change sides.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
季伯达 asks a clean follow-up, slight head tilt, then holds eye contact.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.2s: hold the established composition; 季伯达 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.2–1.8s: 季伯达 speaks the exact Mandarin line “哪里不一样？” once, with natural restrained lip sync and the shot-specific performance: 季伯达 asks a clean follow-up, slight head tilt, then holds eye contact. 1.8–2.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Tiny 2% push-in, then hold. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 季伯达 speaks: “哪里不一样？”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_020.json`](shot-requests/shot_020.json)

## Shot 021｜00:57–01:02
- Speaker/dialogue: **柳如烟**：我和伊藤诚只是纯友谊。我拿他当闺蜜，他也拿我当兄弟。
- Screenplay duration: `5s`; Wan request: `5s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 020](frames/shot_020_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_021.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 021 (00:57–01:02)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 020. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 柳如烟. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 伊藤诚. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 5-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Tight two-shot favoring 柳如烟 with 伊藤诚 beside her.
Visible actors: Visible: 柳如烟 seated at frame left with 伊藤诚 immediately to her right; one or more sofa friends may remain soft in the background exactly as in the source JPG. 柳如烟 does not stand or cross the room.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
柳如烟 explains quickly and defensively, indicating herself then 伊藤诚 without touching him.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.5s: hold the established composition; 柳如烟 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.5–4.6s: 柳如烟 speaks the exact Mandarin line “我和伊藤诚只是纯友谊。我拿他当闺蜜，他也拿我当兄弟。” once, with natural restrained lip sync and the shot-specific performance: 柳如烟 explains quickly and defensively, indicating herself then 伊藤诚 without touching him. 4.6–5.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Slow 3% push-in, no pan. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 柳如烟 speaks: “我和伊藤诚只是纯友谊。我拿他当闺蜜，他也拿我当兄弟。”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_021.json`](shot-requests/shot_021.json)

## Shot 022｜01:02–01:05
- Speaker/dialogue: **伊藤诚**：对，我们之间根本没有男女之情。
- Screenplay duration: `3s`; Wan request: `3s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 021](frames/shot_021_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_022.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 022 (01:02–01:05)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 021. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 柳如烟. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 伊藤诚. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 3-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Tight two-shot favoring 伊藤诚 with 柳如烟 beside him.
Visible actors: Visible: 伊藤诚 seated immediately right of 柳如烟; 柳如烟 remains at frame left and a sofa friend may appear behind. Preserve their close seated spacing without adding contact.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
伊藤诚 nods and supports her claim, measured but slightly tense.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.4s: hold the established composition; 伊藤诚 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.4–2.7s: 伊藤诚 speaks the exact Mandarin line “对，我们之间根本没有男女之情。” once, with natural restrained lip sync and the shot-specific performance: 伊藤诚 nods and supports her claim, measured but slightly tense. 2.7–3.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Slow 2% push toward 伊藤诚. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 伊藤诚 speaks: “对，我们之间根本没有男女之情。”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_022.json`](shot-requests/shot_022.json)

## Shot 023｜01:05–01:08
- Speaker/dialogue: **闺蜜甲**：他们从小就这样，你一个大男人别这么小气。
- Screenplay duration: `3s`; Wan request: `3s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 022](frames/shot_022_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_023.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 闺蜜甲](references/characters/guimi-1.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 闺蜜乙](references/characters/guimi-2.jpg)
  - `reference_image` / Image 5: [identity and wardrobe for 闺蜜丙](references/characters/guimi-3.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 023 (01:05–01:08)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 022. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 闺蜜甲. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 闺蜜乙. Use it only for that role and preserve supported visual details.
Image 5 is the identity and wardrobe for 闺蜜丙. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 3-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Medium three-shot of girlfriends, favoring 闺蜜甲.
Visible actors: Visible: exactly the same three girlfriends only—闺蜜甲 on sofa left, 闺蜜乙 center, 闺蜜丙 right. No fourth person, no background guests, and no seat swaps.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
闺蜜甲 opens both hands as if the conclusion is obvious; 闺蜜乙 listens; 闺蜜丙 observes.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.4s: hold the established composition; 闺蜜甲 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.4–2.7s: 闺蜜甲 speaks the exact Mandarin line “他们从小就这样，你一个大男人别这么小气。” once, with natural restrained lip sync and the shot-specific performance: 闺蜜甲 opens both hands as if the conclusion is obvious; 闺蜜乙 listens; 闺蜜丙 observes. 2.7–3.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Gentle 2% push toward 闺蜜甲. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 闺蜜甲 speaks: “他们从小就这样，你一个大男人别这么小气。”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_023.json`](shot-requests/shot_023.json)

## Shot 024｜01:08–01:11
- Speaker/dialogue: **闺蜜乙**：如烟要是真和伊藤诚有什么，还会和你在一起吗？
- Screenplay duration: `3s`; Wan request: `3s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 023](frames/shot_023_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_024.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 闺蜜甲](references/characters/guimi-1.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 闺蜜乙](references/characters/guimi-2.jpg)
  - `reference_image` / Image 5: [identity and wardrobe for 闺蜜丙](references/characters/guimi-3.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 024 (01:08–01:11)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 023. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 闺蜜甲. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 闺蜜乙. Use it only for that role and preserve supported visual details.
Image 5 is the identity and wardrobe for 闺蜜丙. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 3-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Medium three-shot of girlfriends, favoring 闺蜜乙.
Visible actors: Visible: exactly the same three girlfriends only—闺蜜甲 on sofa left, 闺蜜乙 center, 闺蜜丙 right. No fourth person, no background guests, and no seat swaps.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
闺蜜乙 leans in and challenges 季伯达 rhetorically; the other two track her.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.4s: hold the established composition; 闺蜜乙 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.4–2.7s: 闺蜜乙 speaks the exact Mandarin line “如烟要是真和伊藤诚有什么，还会和你在一起吗？” once, with natural restrained lip sync and the shot-specific performance: 闺蜜乙 leans in and challenges 季伯达 rhetorically; the other two track her. 2.7–3.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Gentle 3% push toward 闺蜜乙. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 闺蜜乙 speaks: “如烟要是真和伊藤诚有什么，还会和你在一起吗？”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_024.json`](shot-requests/shot_024.json)

## Shot 025｜01:11–01:14
- Speaker/dialogue: **闺蜜丙**：情侣之间最重要的是信任。
- Screenplay duration: `3s`; Wan request: `3s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 024](frames/shot_024_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_025.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 闺蜜甲](references/characters/guimi-1.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 闺蜜乙](references/characters/guimi-2.jpg)
  - `reference_image` / Image 5: [identity and wardrobe for 闺蜜丙](references/characters/guimi-3.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 025 (01:11–01:14)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 024. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 闺蜜甲. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 闺蜜乙. Use it only for that role and preserve supported visual details.
Image 5 is the identity and wardrobe for 闺蜜丙. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 3-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Medium three-shot of girlfriends, favoring 闺蜜丙.
Visible actors: Visible: exactly the same three girlfriends only—闺蜜甲 on sofa left, 闺蜜乙 center, 闺蜜丙 right. No fourth person, no background guests, and no seat swaps.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
闺蜜丙 sits straighter and delivers a summarizing maxim; the others go still to listen.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.4s: hold the established composition; 闺蜜丙 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.4–2.7s: 闺蜜丙 speaks the exact Mandarin line “情侣之间最重要的是信任。” once, with natural restrained lip sync and the shot-specific performance: 闺蜜丙 sits straighter and delivers a summarizing maxim; the others go still to listen. 2.7–3.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Slow 2% push toward 闺蜜丙. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 闺蜜丙 speaks: “情侣之间最重要的是信任。”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_025.json`](shot-requests/shot_025.json)

## Shot 026｜01:14–01:20
- Speaker/dialogue: **季伯达**：所以，伊藤诚可以紧挨着我的女朋友，可以知道她内裤的颜色，还可以替她洗——因为他们是纯友谊。
- Screenplay duration: `6s`; Wan request: `6s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 025](frames/shot_025_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_026.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  - `reference_image` / Image 5: [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 026 (01:14–01:20)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 025. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 柳如烟. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 伊藤诚. Use it only for that role and preserve supported visual details.
Image 5 is the identity and wardrobe for 季伯达. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 6-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Sustained medium close-up on 季伯达, right foreground, addressing the sofa group.
Visible actors: Visible: 季伯达 occupies the right foreground in a white shirt, torso turned left toward 柳如烟/伊藤诚 and the opposite sofa; a seated friend may remain soft behind him. He remains seated and does not change sides.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
季伯达 enumerates each allowance with controlled hand beats and increasing precision, not shouting.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.5s: hold the established composition; 季伯达 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.5–5.6s: 季伯达 speaks the exact Mandarin line “所以，伊藤诚可以紧挨着我的女朋友，可以知道她内裤的颜色，还可以替她洗——因为他们是纯友谊。” once, with natural restrained lip sync and the shot-specific performance: 季伯达 enumerates each allowance with controlled hand beats and increasing precision, not shouting. 5.6–6.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Sustained 4% push-in, no cuts or axis change. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 季伯达 speaks: “所以，伊藤诚可以紧挨着我的女朋友，可以知道她内裤的颜色，还可以替她洗——因为他们是纯友谊。”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_026.json`](shot-requests/shot_026.json)

## Shot 027｜01:20–01:24
- Speaker/dialogue: **季伯达**：但我的女闺蜜替我洗内裤，就是没有分寸？
- Screenplay duration: `4s`; Wan request: `4s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 026](frames/shot_026_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_027.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  - `reference_image` / Image 5: [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 027 (01:20–01:24)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 026. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 柳如烟. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 伊藤诚. Use it only for that role and preserve supported visual details.
Image 5 is the identity and wardrobe for 季伯达. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 4-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Matching medium close-up on 季伯达; hold the rhetorical challenge.
Visible actors: Visible: 季伯达 occupies the right foreground in a white shirt, torso turned left toward 柳如烟/伊藤诚 and the opposite sofa; a seated friend may remain soft behind him. He remains seated and does not change sides.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
季伯达 lands the contrast, palm open in a restrained “then why?” gesture, holding the group’s gaze.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.5s: hold the established composition; 季伯达 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.5–3.6s: 季伯达 speaks the exact Mandarin line “但我的女闺蜜替我洗内裤，就是没有分寸？” once, with natural restrained lip sync and the shot-specific performance: 季伯达 lands the contrast, palm open in a restrained “then why?” gesture, holding the group’s gaze. 3.6–4.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Slow 3% push-in that stops on the final question. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 季伯达 speaks: “但我的女闺蜜替我洗内裤，就是没有分寸？”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_027.json`](shot-requests/shot_027.json)

## Shot 028｜01:24–01:27
- Speaker/dialogue: **柳如烟**：季伯达！你故意的是不是？
- Screenplay duration: `3s`; Wan request: `3s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 027](frames/shot_027_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_028.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  - `reference_image` / Image 5: [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 028 (01:24–01:27)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 027. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 柳如烟. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 伊藤诚. Use it only for that role and preserve supported visual details.
Image 5 is the identity and wardrobe for 季伯达. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 3-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Tight medium close-up on 柳如烟; 伊藤诚 remains partly visible.
Visible actors: Visible: 柳如烟 seated at frame left with 伊藤诚 immediately to her right; one or more sofa friends may remain soft in the background exactly as in the source JPG. 柳如烟 does not stand or cross the room.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
柳如烟 erupts, leans forward and glares toward 季伯达; anger replaces embarrassment.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.4s: hold the established composition; 柳如烟 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.4–2.7s: 柳如烟 speaks the exact Mandarin line “季伯达！你故意的是不是？” once, with natural restrained lip sync and the shot-specific performance: 柳如烟 erupts, leans forward and glares toward 季伯达; anger replaces embarrassment. 2.7–3.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Sharper but still smooth 4% push-in. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 柳如烟 speaks: “季伯达！你故意的是不是？”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_028.json`](shot-requests/shot_028.json)

## Shot 029｜01:27–01:29
- Speaker/dialogue: **季伯达**：怎么会？
- Screenplay duration: `2s`; Wan request: `2s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 028](frames/shot_028_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_029.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  - `reference_image` / Image 5: [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 029 (01:27–01:29)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 028. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 柳如烟. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 伊藤诚. Use it only for that role and preserve supported visual details.
Image 5 is the identity and wardrobe for 季伯达. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 2-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Tight medium close-up on 季伯达.
Visible actors: Visible: 季伯达 occupies the right foreground in a white shirt, torso turned left toward 柳如烟/伊藤诚 and the opposite sofa; a seated friend may remain soft behind him. He remains seated and does not change sides.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
季伯达 answers softly with a tiny innocent head tilt, almost dryly amused.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.2s: hold the established composition; 季伯达 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.2–1.8s: 季伯达 speaks the exact Mandarin line “怎么会？” once, with natural restrained lip sync and the shot-specific performance: 季伯达 answers softly with a tiny innocent head tilt, almost dryly amused. 1.8–2.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Near-locked shot; tiny 1% pull-back for dry irony. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 季伯达 speaks: “怎么会？”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_029.json`](shot-requests/shot_029.json)

## Shot 030｜01:29–01:33
- Speaker/dialogue: **季伯达**：我只是按照你们的规矩做了一遍。
- Screenplay duration: `4s`; Wan request: `4s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 029](frames/shot_029_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_030.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  - `reference_image` / Image 5: [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 030 (01:29–01:33)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 029. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 柳如烟. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 伊藤诚. Use it only for that role and preserve supported visual details.
Image 5 is the identity and wardrobe for 季伯达. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 4-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Matching medium close-up on 季伯达, calm and controlled.
Visible actors: Visible: 季伯达 occupies the right foreground in a white shirt, torso turned left toward 柳如烟/伊藤诚 and the opposite sofa; a seated friend may remain soft behind him. He remains seated and does not change sides.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
季伯达 remains composed, one measured hand gesture marking “your rules,” then lets the point sit.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.5s: hold the established composition; 季伯达 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.5–3.6s: 季伯达 speaks the exact Mandarin line “我只是按照你们的规矩做了一遍。” once, with natural restrained lip sync and the shot-specific performance: 季伯达 remains composed, one measured hand gesture marking “your rules,” then lets the point sit. 3.6–4.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Slow 3% push-in. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 季伯达 speaks: “我只是按照你们的规矩做了一遍。”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_030.json`](shot-requests/shot_030.json)

## Shot 031｜01:33–01:37
- Speaker/dialogue: **季伯达**：怎么轮到你们，规矩就变了？
- Screenplay duration: `4s`; Wan request: `4s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 030](frames/shot_030_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_031.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  - `reference_image` / Image 5: [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 031 (01:33–01:37)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 030. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 柳如烟. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 伊藤诚. Use it only for that role and preserve supported visual details.
Image 5 is the identity and wardrobe for 季伯达. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 4-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Matching medium close-up on 季伯达; strongest direct challenge.
Visible actors: Visible: 季伯达 occupies the right foreground in a white shirt, torso turned left toward 柳如烟/伊藤诚 and the opposite sofa; a seated friend may remain soft behind him. He remains seated and does not change sides.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
季伯达’s expression hardens slightly; he asks the final question directly and holds still afterward.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.5s: hold the established composition; 季伯达 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.5–3.6s: 季伯达 speaks the exact Mandarin line “怎么轮到你们，规矩就变了？” once, with natural restrained lip sync and the shot-specific performance: 季伯达’s expression hardens slightly; he asks the final question directly and holds still afterward. 3.6–4.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line.

CAMERA:
Slow 4% push-in, ending in a firm hold. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
Only 季伯达 speaks: “怎么轮到你们，规矩就变了？”
Speak the exact Mandarin wording once with natural restrained lip sync. Do not paraphrase, shorten, expand, repeat, overlap or give it to another actor. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_031.json`](shot-requests/shot_031.json)

## Shot 032｜01:37–01:40
- Speaker/dialogue: **—**：—
- Screenplay duration: `3s`; Wan request: `3s`
- Transition: `CHAIN`
- Media array order:
  - `first_frame`: [literal final rendered frame of Shot 031](frames/shot_031_last_frame.jpg)
  - `reference_image` / Image 1: [shot-specific composition, blocking and camera guide](references/staging/shot_032.jpg)
  - `reference_image` / Image 2: [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  - `reference_image` / Image 3: [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  - `reference_image` / Image 4: [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  - `reference_image` / Image 5: [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
- Five-reference-limit note: omitted separate anchors: identity and wardrobe for 闺蜜甲, identity and wardrobe for 闺蜜乙, identity and wardrobe for 闺蜜丙; identity remains anchored by the first frame/staging reference.
- Wan 2.7 prompt:

```
WAN 2.7 REFERENCE-TO-VIDEO — SHOT 032 (01:37–01:40)

REFERENCE MAP:
The supplied first frame is literal final rendered frame of Shot 031. Preserve its opening composition, identities, poses, expressions, wardrobe, seating, props, lighting, camera angle and screen direction, then begin the new action smoothly without a pose reset.
Image 1 is the shot-specific composition, blocking and camera guide. Use it only for that role and preserve supported visual details.
Image 2 is the KTV setting, lighting, furniture and spatial continuity. Use it only for that role and preserve supported visual details.
Image 3 is the identity and wardrobe for 柳如烟. Use it only for that role and preserve supported visual details.
Image 4 is the identity and wardrobe for 伊藤诚. Use it only for that role and preserve supported visual details.
Image 5 is the identity and wardrobe for 季伯达. Use it only for that role and preserve supported visual details.

OUTPUT:
Create one continuous 3-second cinematic 2D anime shot, 16:9, restrained realistic acting, stable faces and hands, natural breathing and blinks, subtle hair and fabric response, and synchronized Mandarin dialogue/audio. No cut, montage or transition.

COMPOSITION AND BLOCKING:
Framing: Wide ensemble bookend matching shot 001, all positions and table geography preserved.
Visible actors: Visible: exactly six people—柳如烟 and 伊藤诚 together on the left seating; 闺蜜甲/乙/丙 across the central sofa in fixed order; 季伯达 at the right facing them. Four women and two men total; no background guests, no extra, duplicated, or missing people.
Set and lighting: Modern high-rise KTV/lounge at night: warm amber practical lamps and ceiling light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table with cards and small snack plates. Preserve source-JPG object placement and warm/cool contrast; do not invent a new location.
Keep every actor in the assigned seat and on the established side of the camera axis. Never swap, merge, duplicate or replace identities. The table has no alcohol or beverage props.

ACTING:
The room falls awkwardly quiet; smiles fade, gazes shift, and no one offers an answer. End on unresolved group tension.
Non-speaking actors remain in position and react only with directed eyelines, breathing, blinks and restrained micro-expressions. They must not mouth the dialogue or add independent gestures.

TIMELINE:
0.0–0.4s: hold the established composition and eyelines with natural breathing. 0.4–2.7s: perform the shot-specific silent action: The room falls awkwardly quiet; smiles fade, gazes shift, and no one offers an answer. End on unresolved group tension. 2.7–3.0s: resolve the action and hold a stable final pose for the cut. No character speaks and no lip sync is generated.

CAMERA:
Very slow 2% pull-back, echoing the opening while increasing emotional distance. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.

DIALOGUE AND AUDIO:
No one speaks. The narrative/end-card intent is “有些人要求的不是分寸，而是特权。”, but do not render this or any other text in the generated video; add the exact end card only in post-production. Keep room tone subdued. Generate no visible text or subtitles.

CONTINUITY:
Continuity is best effort, not guaranteed. Prioritize identity, then seating/blocking and camera axis, then wardrobe/props/lighting, then exact micro-pose matching. Preserve a stable final 0.3–0.5 seconds for extraction as the next shot's first frame.
```

- Negative prompt:

```
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, listener mouthing dialogue, alcohol, bottles, glasses, drinks, prop movement, background morphing, camera shake, cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_032.json`](shot-requests/shot_032.json)

