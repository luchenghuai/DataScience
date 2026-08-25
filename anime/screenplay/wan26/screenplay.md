# 《分寸》Wan 2.6 R2V 制作包（原 32 镜 → 21 个生成单元）

本包把相邻短镜合并为 4–6 秒为主的 Wan 2.6 生成单元，同时在需要改变说话者特写、机位或构图时保留明确硬切。每个提示词均映射原始镜号并给出相对时间节拍。

## 全局制作规则

- 对白单元：`enable_audio: true`，Wan 原生生成并同步画面内精确普通话；不得改词、复述、加词、串角色或添加画外音。
- 非对白单元：`enable_audio: false`，完全静音，不得杜撰台词或口型。
- 外部 TTS 仅在原生对白未通过逐字/角色/同步质检时作为替换式后备，不得与通过质检的原生音轨叠加。
- 每个请求最多 4 个媒体输入，模型固定 `wan2.6-r2v`，分辨率固定 `720P`，时长不超过 6 秒。
- 全程不得出现酒、瓶、饮料、杯子、饮用玻璃杯或任何饮品道具。
- 开场必须恰好六人，座位与 KTV 连续性严格沿用参考图；单元 001 唯一对白为闺蜜甲：“如烟，你输了！”，绝不是“粉红色。”。
- 每个单元末尾保留约 0.4 秒稳定画面，用作下一单元首帧。

## Generation Unit 001

- 原始镜号：001
- 时间：`00:00–00:03`
- 时长：`3s`
- 对白：闺蜜甲：如烟，你输了！
- 音频：`enable_audio: true`
- 内部硬切前原始镜号：无
- 媒体输入（4/4）：
  - `first_frame`: `references/staging/shot_001.jpg` — baseline opening frame with the exact complete six-person KTV composition
  - `reference_image`: `references/setting/ktv-continuity-sheet.jpg` — KTV set, exact six-person seating, furniture, camera axis, lighting, and empty-table continuity
  - `reference_image`: `references/characters/guimi-1.jpg` — identity and wardrobe for opening speaker 闺蜜甲
  - `reference_image`: `references/characters/liuruyan.jpg` — identity and wardrobe for principal reactor 柳如烟
- Prompt:

```text
WAN 2.6 REFERENCE-TO-VIDEO — GENERATION UNIT 001 (00:00–00:03)

ORIGINAL SHOT MAP:
This generation unit maps original canonical shot IDs: 001. Preserve every mapped story beat in this order. Only the boundaries explicitly marked HARD CUT may cut; all boundaries marked CONTINUE remain one continuous camera take.

REFERENCE MAP — EXACTLY FOUR MEDIA INPUTS:
The supplied first frame is the literal baseline opening composition. Preserve all six named people, their exact seats, poses, wardrobe, KTV set, props, lighting, camera height, lens feel, axis and screen direction before motion begins. Do not add, remove, duplicate, merge or replace anyone.
Image 1 is the consolidated six-character identity sheet. Bind each portrait to the person already present in the first frame; portraits are identity evidence only and must never appear as panels, borders, labels or extra people in the video. Grid map: top-left = 季伯达 (black suit, swept black hair); top-center = 柳如烟 (long wavy black hair, navy business suit and white blouse); top-right = 伊藤诚 (very pale young man, slick black hair, black suit and dark red tie); bottom-left = 闺蜜甲, the speaker (long straight black hair, red blazer, red drop earrings); bottom-center = 闺蜜乙 (short brown bob, round glasses, green cardigan); bottom-right = 闺蜜丙 (high curly brown ponytail with teal streak, denim jacket, yellow top). Preserve each face shape, eyes, hair, skin tone, apparent age, body proportions and wardrobe exactly.
Image 2 is the KTV set and continuity sheet. Use it only for furniture, exact six-person seating geography, empty-table state, warm amber/cool blue lighting, camera axis and screen direction. Do not copy collage repetition, labels or additional figures from it.
Image 3 is the close identity and wardrobe reference for opening speaker 闺蜜甲. Bind it only to the existing bottom-left-sheet identity already seated as 闺蜜甲; it is not an additional person. Prioritize her facial fidelity and stable synchronized mouth movement while she speaks. If any reference conflicts, priority is: first-frame composition/headcount, Image 1 identities, Image 2 set continuity, then Image 3 speaker detail.

AUDIO POLICY:
Native audio is required because this unit contains dialogue. Generate only the exact Mandarin lines specified in TIMED BEATS, in that order, synchronized to the named on-screen speaker. No narration, translation, ad-libs, repeated words, overlapping speech, lyrics, or invented speech. Non-speakers do not mouth dialogue. Keep ambience minimal and never include music or off-screen voices. External Mandarin TTS is fallback-only if native generation fails exact-wording or sync QC; do not pre-mix TTS into a successful native-audio render.

OUTPUT:
Create one 3-second cinematic 2D anime generation unit, 16:9, 720P, restrained realistic acting, stable faces and hands, natural breathing and blinks, and subtle hair/fabric response. Model: wan2.6-r2v. Keep timing exact. Do not add montage, transitions, subtitles, labels, logos, watermarks, or visible prompt text.

GLOBAL CONTINUITY AND IDENTITY PRIORITY:
Portrait fidelity is the highest visual priority after preserving the literal first-frame composition. Match the consolidated portrait sheet as faithfully as possible throughout every frame: exact facial structure, eye shape and color, eyebrows, nose, lips, hairstyle and color, skin tone, apparent age, body proportions, and character-specific wardrobe. Do not beautify, average, reinterpret, gender-swap, face-swap, or blend identities. Faces must remain stable and recognizable during speech, blinks, head turns, and the camera push-in. If decorative detail conflicts with identity fidelity, reduce decorative detail and preserve the portraits.
Modern high-rise KTV/lounge at night with warm amber practical light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table, cards, and small snack plates. The table and room contain no alcohol, bottles, drinks, beverages, cups, drinking glasses, or beverage props at any time. Keep every named actor in the established seat and on the established camera-axis side unless a timed beat explicitly changes framing. Never swap, merge, duplicate, omit, or replace identities. Show exactly six people total: exactly two males—季伯达 and 伊藤诚—and exactly four females—柳如烟, 闺蜜甲, 闺蜜乙, 闺蜜丙. No additional male, background man, male silhouette, waiter, patron, reflection, poster figure, duplicate male face, or partially visible extra person may appear anywhere in the room, windows, mirrors, doorways, or background. No additional females or other people either. Opening unit 001 must begin with all six already seated: screen-left 柳如烟 then 伊藤诚; central sofa 闺蜜甲, 闺蜜乙, 闺蜜丙; far screen-right 季伯达 facing the group.

TIMED BEATS:
0.0s–3.0s — ORIGINAL SHOT 001 — OPEN ON THE SUPPLIED FIRST FRAME.
Framing/staging: Wide ensemble establishing shot, eye level, preserving the full seating geography and coffee table. exactly six named people only—柳如烟, 伊藤诚, 闺蜜甲, 闺蜜乙, 闺蜜丙, 季伯达. No background guests, extras, duplicates, or missing people. Position continuity: screen-left seating—柳如烟 at far left and 伊藤诚 immediately to her right; central sofa—闺蜜甲 at left seat, 闺蜜乙 at center seat, 闺蜜丙 at right seat; screen-right seating—季伯达 at far right facing the group.
Action/story beat: During the wide party tableau, 闺蜜甲 turns toward 柳如烟, leans forward slightly, raises one hand to claim attention, and delivers the assigned opening Mandarin line with playful excitement; 柳如烟 shifts her gaze toward her while the others quiet down and watch.
Camera: Very slow 3% push-in with subtle parallax across the coffee table. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 0.3s–2.7s: only 闺蜜甲 says “如烟，你输了！” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

PERFORMANCE GUARDRAILS:
Dialogue belongs only to the named speaker during its exact time window. Preserve the line wording, punctuation-level phrasing, speaker assignment, and order. Do not paraphrase, shorten, expand, repeat, overlap, or move a line to another beat. During silent intervals and the non-dialogue unit, generate no speech and no word-shaped mouth movement. Preserve restrained reactions and a stable final 0.4 seconds for the next unit's first-frame extraction.
```

- Negative prompt:

```text
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, wrong speaker, listener mouthing dialogue, invented speech, extra dialogue, paraphrased dialogue, alcohol, bottles, drinks, beverages, cups, drinking glasses, prop movement, background morphing, camera shake, unplanned cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_001.json`](shot-requests/shot_001.json)

## Generation Unit 002

- 原始镜号：002, 003, 004
- 时间：`00:03–00:09`
- 时长：`6s`
- 对白：闺蜜甲：选真心话还是大冒险？；柳如烟：真心话。；闺蜜乙：那就说说，你今天穿的内裤是什么颜色？
- 音频：`enable_audio: true`
- 内部硬切前原始镜号：003, 004
- 媒体输入（4/4）：
  - `first_frame`: `frames/shot_001_last_frame.jpg` — literal accepted final rendered frame of generation unit 001
  - `reference_image`: `references/staging/shot_002.jpg` — composition/blocking anchor for original shot 002
  - `reference_image`: `references/setting/ktv-continuity-sheet.jpg` — KTV seating, furniture, camera axis, lighting, and empty-table continuity
  - `reference_image`: `references/staging/shot_004.jpg` — composition/blocking anchor for original shot 004 and the later beat(s)
- Prompt:

```text
WAN 2.6 REFERENCE-TO-VIDEO — GENERATION UNIT 002 (00:03–00:09)

ORIGINAL SHOT MAP:
This generation unit maps original canonical shot IDs: 002, 003, 004. Preserve every mapped story beat in this order. Only the boundaries explicitly marked HARD CUT may cut; all boundaries marked CONTINUE remain one continuous camera take.

REFERENCE MAP:
The supplied first frame is the literal accepted final rendered frame of generation unit 001. Preserve identities, poses, expressions, wardrobe, seats, props, lighting, camera axis and screen direction before the first timed beat.
Image 1 is the composition/blocking anchor for original shot 002. Use it only for that role; the timed beat instructions control motion and cuts.
Image 2 is the KTV seating, furniture, camera axis, lighting, and empty-table continuity. Use it only for that role; the timed beat instructions control motion and cuts.
Image 3 is the composition/blocking anchor for original shot 004 and the later beat(s). Use it only for that role; the timed beat instructions control motion and cuts.

AUDIO POLICY:
Native audio is required because this unit contains dialogue. Generate only the exact Mandarin lines specified in TIMED BEATS, in that order, synchronized to the named on-screen speaker. No narration, translation, ad-libs, repeated words, overlapping speech, lyrics, or invented speech. Non-speakers do not mouth dialogue. Keep ambience minimal and never include music or off-screen voices. External Mandarin TTS is fallback-only if native generation fails exact-wording or sync QC; do not pre-mix TTS into a successful native-audio render.

OUTPUT:
Create one 6-second cinematic 2D anime generation unit, 16:9, 720P, restrained realistic acting, stable faces and hands, natural breathing and blinks, and subtle hair/fabric response. Model: wan2.6-r2v. Keep timing exact. Do not add montage, transitions, subtitles, labels, logos, watermarks, or visible prompt text.

GLOBAL CONTINUITY:
Modern high-rise KTV/lounge at night with warm amber practical light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table, cards, and small snack plates. The table and room contain no alcohol, bottles, drinks, beverages, cups, drinking glasses, or beverage props at any time. Keep every named actor in the established seat and on the established camera-axis side unless a timed beat explicitly changes framing. Never swap, merge, duplicate, omit, or replace identities. For any wide ensemble view, show exactly these six people and no others: 柳如烟, 伊藤诚, 闺蜜甲, 闺蜜乙, 闺蜜丙, 季伯达. Opening unit 001 must begin with all six already seated: screen-left 柳如烟 then 伊藤诚; central sofa 闺蜜甲, 闺蜜乙, 闺蜜丙; far screen-right 季伯达 facing the group.

TIMED BEATS:
0.0s–2.0s — ORIGINAL SHOT 002 — OPEN ON THE SUPPLIED FIRST FRAME.
Framing/staging: Medium three-shot of the three girlfriends across the sofa; 闺蜜甲 is the visual lead. exactly three named people only—闺蜜甲, 闺蜜乙, 闺蜜丙. No fourth person, background guest, duplicate, or seat swap. Position continuity: 闺蜜甲 at frame-left/sofa-left; 闺蜜乙 at frame-center/sofa-center; 闺蜜丙 at frame-right/sofa-right.
Action/story beat: 闺蜜甲 remains leaning forward after announcing the loss, keeps her attention on 柳如烟, and asks the assigned truth-or-dare question with playful excitement; 闺蜜乙 turns to listen and 闺蜜丙 relaxes with empty hands.
Camera: Gentle 2% push-in toward 闺蜜甲; no pan. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 0.2s–1.8s: only 闺蜜甲 says “选真心话还是大冒险？” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

2.0s–3.0s — ORIGINAL SHOT 003 — HARD CUT AT THIS EXACT BOUNDARY.
Framing/staging: Tight medium close-up on 柳如烟 at frame left; 伊藤诚 remains partially visible beside/behind her. exactly two named people only—柳如烟 and 伊藤诚. No friend, guest, extra, duplicate, or unnamed background person. Position continuity: 柳如烟 at frame-left; 伊藤诚 immediately beside her at frame-right. No friend or other person may appear in foreground or background.
Action/story beat: 柳如烟 answers promptly and evenly, a tiny nod and confident eye contact.
Camera: Near-locked shot with a tiny 1% push-in. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 2.1s–2.9s: only 柳如烟 says “真心话。” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

3.0s–6.0s — ORIGINAL SHOT 004 — HARD CUT AT THIS EXACT BOUNDARY.
Framing/staging: Medium three-shot of the girlfriends; center emphasis on 闺蜜乙. exactly three named people only—闺蜜甲, 闺蜜乙, 闺蜜丙. No fourth person, background guest, duplicate, or seat swap. Position continuity: 闺蜜甲 at frame-left/sofa-left; 闺蜜乙 at frame-center/sofa-center; 闺蜜丙 at frame-right/sofa-right.
Action/story beat: 闺蜜乙 taps/indicates the table lightly and teases; 闺蜜甲 turns toward her; 闺蜜丙 watches 柳如烟.
Camera: Slow 3% push toward 闺蜜乙; keep all three faces stable. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 3.3s–5.7s: only 闺蜜乙 says “那就说说，你今天穿的内裤是什么颜色？” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

PERFORMANCE GUARDRAILS:
Dialogue belongs only to the named speaker during its exact time window. Preserve the line wording, punctuation-level phrasing, speaker assignment, and order. Do not paraphrase, shorten, expand, repeat, overlap, or move a line to another beat. During silent intervals and the non-dialogue unit, generate no speech and no word-shaped mouth movement. Preserve restrained reactions and a stable final 0.4 seconds for the next unit's first-frame extraction.
```

- Negative prompt:

```text
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, wrong speaker, listener mouthing dialogue, invented speech, extra dialogue, paraphrased dialogue, alcohol, bottles, drinks, beverages, cups, drinking glasses, prop movement, background morphing, camera shake, unplanned cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_002.json`](shot-requests/shot_002.json)

## Generation Unit 003

- 原始镜号：005, 006
- 时间：`00:09–00:14`
- 时长：`5s`
- 对白：伊藤诚：粉红色。；伊藤诚：如烟一直拿我当姐妹。她的内裤，我以前都帮她洗过。
- 音频：`enable_audio: true`
- 内部硬切前原始镜号：无
- 媒体输入（4/4）：
  - `first_frame`: `frames/shot_002_last_frame.jpg` — literal accepted final rendered frame of generation unit 002
  - `reference_image`: `references/staging/shot_005.jpg` — composition/blocking anchor for original shot 005
  - `reference_image`: `references/setting/ktv-continuity-sheet.jpg` — KTV seating, furniture, camera axis, lighting, and empty-table continuity
  - `reference_image`: `references/characters/yitengcheng.jpg` — identity and wardrobe for speaking character 伊藤诚
- Prompt:

```text
WAN 2.6 REFERENCE-TO-VIDEO — GENERATION UNIT 003 (00:09–00:14)

ORIGINAL SHOT MAP:
This generation unit maps original canonical shot IDs: 005, 006. Preserve every mapped story beat in this order. Only the boundaries explicitly marked HARD CUT may cut; all boundaries marked CONTINUE remain one continuous camera take.

REFERENCE MAP:
The supplied first frame is the literal accepted final rendered frame of generation unit 002. Preserve identities, poses, expressions, wardrobe, seats, props, lighting, camera axis and screen direction before the first timed beat.
Image 1 is the composition/blocking anchor for original shot 005. Use it only for that role; the timed beat instructions control motion and cuts.
Image 2 is the KTV seating, furniture, camera axis, lighting, and empty-table continuity. Use it only for that role; the timed beat instructions control motion and cuts.
Image 3 is the identity and wardrobe for speaking character 伊藤诚. Use it only for that role; the timed beat instructions control motion and cuts.

AUDIO POLICY:
Native audio is required because this unit contains dialogue. Generate only the exact Mandarin lines specified in TIMED BEATS, in that order, synchronized to the named on-screen speaker. No narration, translation, ad-libs, repeated words, overlapping speech, lyrics, or invented speech. Non-speakers do not mouth dialogue. Keep ambience minimal and never include music or off-screen voices. External Mandarin TTS is fallback-only if native generation fails exact-wording or sync QC; do not pre-mix TTS into a successful native-audio render.

OUTPUT:
Create one 5-second cinematic 2D anime generation unit, 16:9, 720P, restrained realistic acting, stable faces and hands, natural breathing and blinks, and subtle hair/fabric response. Model: wan2.6-r2v. Keep timing exact. Do not add montage, transitions, subtitles, labels, logos, watermarks, or visible prompt text.

GLOBAL CONTINUITY:
Modern high-rise KTV/lounge at night with warm amber practical light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table, cards, and small snack plates. The table and room contain no alcohol, bottles, drinks, beverages, cups, drinking glasses, or beverage props at any time. Keep every named actor in the established seat and on the established camera-axis side unless a timed beat explicitly changes framing. Never swap, merge, duplicate, omit, or replace identities. For any wide ensemble view, show exactly these six people and no others: 柳如烟, 伊藤诚, 闺蜜甲, 闺蜜乙, 闺蜜丙, 季伯达. Opening unit 001 must begin with all six already seated: screen-left 柳如烟 then 伊藤诚; central sofa 闺蜜甲, 闺蜜乙, 闺蜜丙; far screen-right 季伯达 facing the group.

TIMED BEATS:
0.0s–1.0s — ORIGINAL SHOT 005 — OPEN ON THE SUPPLIED FIRST FRAME.
Framing/staging: Tight two-shot favoring 伊藤诚 beside 柳如烟; keep 柳如烟 visible for reaction. exactly two named people only—柳如烟 and 伊藤诚. No friend, guest, extra, duplicate, or unnamed background person. Position continuity: 柳如烟 at frame-left; 伊藤诚 immediately beside her at frame-right. No friend or other person may appear in foreground or background.
Action/story beat: 伊藤诚 answers too quickly with casual certainty; 柳如烟 registers immediate discomfort.
Camera: Near-locked 1% push-in for comic timing. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 0.1s–0.9s: only 伊藤诚 says “粉红色。” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

1.0s–5.0s — ORIGINAL SHOT 006 — CONTINUE IN THE SAME SHOT; NO CUT.
Framing/staging: Tight two-shot favoring 伊藤诚 beside 柳如烟, with 闺蜜甲 softly present in deep background. exactly three named people only—柳如烟, 伊藤诚, and 闺蜜甲. No other friend, guest, extra, duplicate, or unnamed background person. Position continuity: 柳如烟 at frame-left; 伊藤诚 immediately beside her at frame-right; 闺蜜甲 remains in her established central-sofa seat in deep background.
Action/story beat: 伊藤诚 continues matter-of-factly with a small explanatory hand gesture; 柳如烟 stiffens while 闺蜜甲 watches from deep background.
Camera: Slow 2% push-in, no reframing. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 1.4s–4.6s: only 伊藤诚 says “如烟一直拿我当姐妹。她的内裤，我以前都帮她洗过。” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

PERFORMANCE GUARDRAILS:
Dialogue belongs only to the named speaker during its exact time window. Preserve the line wording, punctuation-level phrasing, speaker assignment, and order. Do not paraphrase, shorten, expand, repeat, overlap, or move a line to another beat. During silent intervals and the non-dialogue unit, generate no speech and no word-shaped mouth movement. Preserve restrained reactions and a stable final 0.4 seconds for the next unit's first-frame extraction.
```

- Negative prompt:

```text
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, wrong speaker, listener mouthing dialogue, invented speech, extra dialogue, paraphrased dialogue, alcohol, bottles, drinks, beverages, cups, drinking glasses, prop movement, background morphing, camera shake, unplanned cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_003.json`](shot-requests/shot_003.json)

## Generation Unit 004

- 原始镜号：007, 008
- 时间：`00:14–00:18`
- 时长：`4s`
- 对白：柳如烟：你胡说什么呢？；闺蜜甲：姐夫，你可别多想。他们从小一起长大。
- 音频：`enable_audio: true`
- 内部硬切前原始镜号：008
- 媒体输入（4/4）：
  - `first_frame`: `frames/shot_003_last_frame.jpg` — literal accepted final rendered frame of generation unit 003
  - `reference_image`: `references/staging/shot_007.jpg` — composition/blocking anchor for original shot 007
  - `reference_image`: `references/setting/ktv-continuity-sheet.jpg` — KTV seating, furniture, camera axis, lighting, and empty-table continuity
  - `reference_image`: `references/staging/shot_008.jpg` — composition/blocking anchor for original shot 008 and the later beat(s)
- Prompt:

```text
WAN 2.6 REFERENCE-TO-VIDEO — GENERATION UNIT 004 (00:14–00:18)

ORIGINAL SHOT MAP:
This generation unit maps original canonical shot IDs: 007, 008. Preserve every mapped story beat in this order. Only the boundaries explicitly marked HARD CUT may cut; all boundaries marked CONTINUE remain one continuous camera take.

REFERENCE MAP:
The supplied first frame is the literal accepted final rendered frame of generation unit 003. Preserve identities, poses, expressions, wardrobe, seats, props, lighting, camera axis and screen direction before the first timed beat.
Image 1 is the composition/blocking anchor for original shot 007. Use it only for that role; the timed beat instructions control motion and cuts.
Image 2 is the KTV seating, furniture, camera axis, lighting, and empty-table continuity. Use it only for that role; the timed beat instructions control motion and cuts.
Image 3 is the composition/blocking anchor for original shot 008 and the later beat(s). Use it only for that role; the timed beat instructions control motion and cuts.

AUDIO POLICY:
Native audio is required because this unit contains dialogue. Generate only the exact Mandarin lines specified in TIMED BEATS, in that order, synchronized to the named on-screen speaker. No narration, translation, ad-libs, repeated words, overlapping speech, lyrics, or invented speech. Non-speakers do not mouth dialogue. Keep ambience minimal and never include music or off-screen voices. External Mandarin TTS is fallback-only if native generation fails exact-wording or sync QC; do not pre-mix TTS into a successful native-audio render.

OUTPUT:
Create one 4-second cinematic 2D anime generation unit, 16:9, 720P, restrained realistic acting, stable faces and hands, natural breathing and blinks, and subtle hair/fabric response. Model: wan2.6-r2v. Keep timing exact. Do not add montage, transitions, subtitles, labels, logos, watermarks, or visible prompt text.

GLOBAL CONTINUITY:
Modern high-rise KTV/lounge at night with warm amber practical light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table, cards, and small snack plates. The table and room contain no alcohol, bottles, drinks, beverages, cups, drinking glasses, or beverage props at any time. Keep every named actor in the established seat and on the established camera-axis side unless a timed beat explicitly changes framing. Never swap, merge, duplicate, omit, or replace identities. For any wide ensemble view, show exactly these six people and no others: 柳如烟, 伊藤诚, 闺蜜甲, 闺蜜乙, 闺蜜丙, 季伯达. Opening unit 001 must begin with all six already seated: screen-left 柳如烟 then 伊藤诚; central sofa 闺蜜甲, 闺蜜乙, 闺蜜丙; far screen-right 季伯达 facing the group.

TIMED BEATS:
0.0s–2.0s — ORIGINAL SHOT 007 — OPEN ON THE SUPPLIED FIRST FRAME.
Framing/staging: Tight medium close-up on 柳如烟, with 伊藤诚 partly visible beside her. exactly two named people only—柳如烟 and 伊藤诚. No friend, guest, extra, duplicate, or unnamed background person. Position continuity: 柳如烟 at frame-left; 伊藤诚 immediately beside her at frame-right. No friend or other person may appear in foreground or background.
Action/story beat: 柳如烟 snaps her gaze toward 伊藤诚, brows tightening; brief embarrassed protest.
Camera: Brief 2% push-in synchronized to the protest. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 0.2s–1.8s: only 柳如烟 says “你胡说什么呢？” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

2.0s–4.0s — ORIGINAL SHOT 008 — HARD CUT AT THIS EXACT BOUNDARY.
Framing/staging: Medium three-shot of the girlfriends; 闺蜜甲 leads from sofa left. exactly three named people only—闺蜜甲, 闺蜜乙, 闺蜜丙. No fourth person, background guest, duplicate, or seat swap. Position continuity: 闺蜜甲 at frame-left/sofa-left; 闺蜜乙 at frame-center/sofa-center; 闺蜜丙 at frame-right/sofa-right.
Action/story beat: 闺蜜甲 raises a calming palm toward 季伯达 and explains earnestly; the other two listen.
Camera: Gentle 2% push toward 闺蜜甲. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 2.2s–3.8s: only 闺蜜甲 says “姐夫，你可别多想。他们从小一起长大。” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

PERFORMANCE GUARDRAILS:
Dialogue belongs only to the named speaker during its exact time window. Preserve the line wording, punctuation-level phrasing, speaker assignment, and order. Do not paraphrase, shorten, expand, repeat, overlap, or move a line to another beat. During silent intervals and the non-dialogue unit, generate no speech and no word-shaped mouth movement. Preserve restrained reactions and a stable final 0.4 seconds for the next unit's first-frame extraction.
```

- Negative prompt:

```text
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, wrong speaker, listener mouthing dialogue, invented speech, extra dialogue, paraphrased dialogue, alcohol, bottles, drinks, beverages, cups, drinking glasses, prop movement, background morphing, camera shake, unplanned cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_004.json`](shot-requests/shot_004.json)

## Generation Unit 005

- 原始镜号：009, 010
- 时间：`00:18–00:22`
- 时长：`4s`
- 对白：闺蜜乙：就是，伊藤诚在我们眼里根本不算男人。；闺蜜丙：他们是纯友谊，关系好才这样。
- 音频：`enable_audio: true`
- 内部硬切前原始镜号：无
- 媒体输入（4/4）：
  - `first_frame`: `frames/shot_004_last_frame.jpg` — literal accepted final rendered frame of generation unit 004
  - `reference_image`: `references/staging/shot_009.jpg` — composition/blocking anchor for original shot 009
  - `reference_image`: `references/setting/ktv-continuity-sheet.jpg` — KTV seating, furniture, camera axis, lighting, and empty-table continuity
  - `reference_image`: `references/staging/shot_010.jpg` — composition/blocking anchor for original shot 010 and the later beat(s)
- Prompt:

```text
WAN 2.6 REFERENCE-TO-VIDEO — GENERATION UNIT 005 (00:18–00:22)

ORIGINAL SHOT MAP:
This generation unit maps original canonical shot IDs: 009, 010. Preserve every mapped story beat in this order. Only the boundaries explicitly marked HARD CUT may cut; all boundaries marked CONTINUE remain one continuous camera take.

REFERENCE MAP:
The supplied first frame is the literal accepted final rendered frame of generation unit 004. Preserve identities, poses, expressions, wardrobe, seats, props, lighting, camera axis and screen direction before the first timed beat.
Image 1 is the composition/blocking anchor for original shot 009. Use it only for that role; the timed beat instructions control motion and cuts.
Image 2 is the KTV seating, furniture, camera axis, lighting, and empty-table continuity. Use it only for that role; the timed beat instructions control motion and cuts.
Image 3 is the composition/blocking anchor for original shot 010 and the later beat(s). Use it only for that role; the timed beat instructions control motion and cuts.

AUDIO POLICY:
Native audio is required because this unit contains dialogue. Generate only the exact Mandarin lines specified in TIMED BEATS, in that order, synchronized to the named on-screen speaker. No narration, translation, ad-libs, repeated words, overlapping speech, lyrics, or invented speech. Non-speakers do not mouth dialogue. Keep ambience minimal and never include music or off-screen voices. External Mandarin TTS is fallback-only if native generation fails exact-wording or sync QC; do not pre-mix TTS into a successful native-audio render.

OUTPUT:
Create one 4-second cinematic 2D anime generation unit, 16:9, 720P, restrained realistic acting, stable faces and hands, natural breathing and blinks, and subtle hair/fabric response. Model: wan2.6-r2v. Keep timing exact. Do not add montage, transitions, subtitles, labels, logos, watermarks, or visible prompt text.

GLOBAL CONTINUITY:
Modern high-rise KTV/lounge at night with warm amber practical light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table, cards, and small snack plates. The table and room contain no alcohol, bottles, drinks, beverages, cups, drinking glasses, or beverage props at any time. Keep every named actor in the established seat and on the established camera-axis side unless a timed beat explicitly changes framing. Never swap, merge, duplicate, omit, or replace identities. For any wide ensemble view, show exactly these six people and no others: 柳如烟, 伊藤诚, 闺蜜甲, 闺蜜乙, 闺蜜丙, 季伯达. Opening unit 001 must begin with all six already seated: screen-left 柳如烟 then 伊藤诚; central sofa 闺蜜甲, 闺蜜乙, 闺蜜丙; far screen-right 季伯达 facing the group.

TIMED BEATS:
0.0s–2.0s — ORIGINAL SHOT 009 — OPEN ON THE SUPPLIED FIRST FRAME.
Framing/staging: Medium three-shot of the girlfriends; 闺蜜乙 leads from sofa center. exactly three named people only—闺蜜甲, 闺蜜乙, 闺蜜丙. No fourth person, background guest, duplicate, or seat swap. Position continuity: 闺蜜甲 at frame-left/sofa-left; 闺蜜乙 at frame-center/sofa-center; 闺蜜丙 at frame-right/sofa-right.
Action/story beat: 闺蜜乙 turns toward 季伯达 and adds reassurance; 闺蜜甲 settles back; 闺蜜丙 gives a restrained nod.
Camera: Tiny lateral ease from left to center, ending on 闺蜜乙. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 0.2s–1.8s: only 闺蜜乙 says “就是，伊藤诚在我们眼里根本不算男人。” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

2.0s–4.0s — ORIGINAL SHOT 010 — CONTINUE IN THE SAME SHOT; NO CUT.
Framing/staging: Medium three-shot of the girlfriends; 闺蜜丙 leads from sofa right. exactly three named people only—闺蜜甲, 闺蜜乙, 闺蜜丙. No fourth person, background guest, duplicate, or seat swap. Position continuity: 闺蜜甲 at frame-left/sofa-left; 闺蜜乙 at frame-center/sofa-center; 闺蜜丙 at frame-right/sofa-right.
Action/story beat: 闺蜜丙 lowers her hand and concludes calmly; the other two turn to her.
Camera: Tiny ease right to favor 闺蜜丙. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 2.2s–3.8s: only 闺蜜丙 says “他们是纯友谊，关系好才这样。” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

PERFORMANCE GUARDRAILS:
Dialogue belongs only to the named speaker during its exact time window. Preserve the line wording, punctuation-level phrasing, speaker assignment, and order. Do not paraphrase, shorten, expand, repeat, overlap, or move a line to another beat. During silent intervals and the non-dialogue unit, generate no speech and no word-shaped mouth movement. Preserve restrained reactions and a stable final 0.4 seconds for the next unit's first-frame extraction.
```

- Negative prompt:

```text
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, wrong speaker, listener mouthing dialogue, invented speech, extra dialogue, paraphrased dialogue, alcohol, bottles, drinks, beverages, cups, drinking glasses, prop movement, background morphing, camera shake, unplanned cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_005.json`](shot-requests/shot_005.json)

## Generation Unit 006

- 原始镜号：011
- 时间：`00:22–00:26`
- 时长：`4s`
- 对白：季伯达：小伊，不是我说你。一个大男人，洗什么内裤？
- 音频：`enable_audio: true`
- 内部硬切前原始镜号：无
- 媒体输入（4/4）：
  - `first_frame`: `frames/shot_005_last_frame.jpg` — literal accepted final rendered frame of generation unit 005
  - `reference_image`: `references/staging/shot_011.jpg` — composition/blocking anchor for original shot 011
  - `reference_image`: `references/setting/ktv-continuity-sheet.jpg` — KTV seating, furniture, camera axis, lighting, and empty-table continuity
  - `reference_image`: `references/characters/jiboda.jpg` — identity and wardrobe for speaking character 季伯达
- Prompt:

```text
WAN 2.6 REFERENCE-TO-VIDEO — GENERATION UNIT 006 (00:22–00:26)

ORIGINAL SHOT MAP:
This generation unit maps original canonical shot IDs: 011. Preserve every mapped story beat in this order. Only the boundaries explicitly marked HARD CUT may cut; all boundaries marked CONTINUE remain one continuous camera take.

REFERENCE MAP:
The supplied first frame is the literal accepted final rendered frame of generation unit 005. Preserve identities, poses, expressions, wardrobe, seats, props, lighting, camera axis and screen direction before the first timed beat.
Image 1 is the composition/blocking anchor for original shot 011. Use it only for that role; the timed beat instructions control motion and cuts.
Image 2 is the KTV seating, furniture, camera axis, lighting, and empty-table continuity. Use it only for that role; the timed beat instructions control motion and cuts.
Image 3 is the identity and wardrobe for speaking character 季伯达. Use it only for that role; the timed beat instructions control motion and cuts.

AUDIO POLICY:
Native audio is required because this unit contains dialogue. Generate only the exact Mandarin lines specified in TIMED BEATS, in that order, synchronized to the named on-screen speaker. No narration, translation, ad-libs, repeated words, overlapping speech, lyrics, or invented speech. Non-speakers do not mouth dialogue. Keep ambience minimal and never include music or off-screen voices. External Mandarin TTS is fallback-only if native generation fails exact-wording or sync QC; do not pre-mix TTS into a successful native-audio render.

OUTPUT:
Create one 4-second cinematic 2D anime generation unit, 16:9, 720P, restrained realistic acting, stable faces and hands, natural breathing and blinks, and subtle hair/fabric response. Model: wan2.6-r2v. Keep timing exact. Do not add montage, transitions, subtitles, labels, logos, watermarks, or visible prompt text.

GLOBAL CONTINUITY:
Modern high-rise KTV/lounge at night with warm amber practical light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table, cards, and small snack plates. The table and room contain no alcohol, bottles, drinks, beverages, cups, drinking glasses, or beverage props at any time. Keep every named actor in the established seat and on the established camera-axis side unless a timed beat explicitly changes framing. Never swap, merge, duplicate, omit, or replace identities. For any wide ensemble view, show exactly these six people and no others: 柳如烟, 伊藤诚, 闺蜜甲, 闺蜜乙, 闺蜜丙, 季伯达. Opening unit 001 must begin with all six already seated: screen-left 柳如烟 then 伊藤诚; central sofa 闺蜜甲, 闺蜜乙, 闺蜜丙; far screen-right 季伯达 facing the group.

TIMED BEATS:
0.0s–4.0s — ORIGINAL SHOT 011 — OPEN ON THE SUPPLIED FIRST FRAME.
Framing/staging: Over-shoulder/medium close-up favoring 季伯达 at the right foreground, facing left toward 伊藤诚. exactly three named people only—柳如烟, 伊藤诚, 季伯达. No friend, guest, extra, duplicate, or unnamed background person. Position continuity: 柳如烟 at frame-left background; 伊藤诚 at center-left background immediately to 柳如烟’s right; 季伯达 at frame-right foreground, seated and facing left toward them.
Action/story beat: 季伯达 begins controlled and faintly incredulous, looking toward 伊藤诚; one restrained open-palm gesture.
Camera: Slow 3% push-in; stable eyeline. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 0.4s–3.6s: only 季伯达 says “小伊，不是我说你。一个大男人，洗什么内裤？” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

PERFORMANCE GUARDRAILS:
Dialogue belongs only to the named speaker during its exact time window. Preserve the line wording, punctuation-level phrasing, speaker assignment, and order. Do not paraphrase, shorten, expand, repeat, overlap, or move a line to another beat. During silent intervals and the non-dialogue unit, generate no speech and no word-shaped mouth movement. Preserve restrained reactions and a stable final 0.4 seconds for the next unit's first-frame extraction.
```

- Negative prompt:

```text
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, wrong speaker, listener mouthing dialogue, invented speech, extra dialogue, paraphrased dialogue, alcohol, bottles, drinks, beverages, cups, drinking glasses, prop movement, background morphing, camera shake, unplanned cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_006.json`](shot-requests/shot_006.json)

## Generation Unit 007

- 原始镜号：012
- 时间：`00:26–00:31`
- 时长：`5s`
- 对白：季伯达：我的内裤，都是我女闺蜜帮我洗的。你下次也让如烟替你洗。
- 音频：`enable_audio: true`
- 内部硬切前原始镜号：无
- 媒体输入（4/4）：
  - `first_frame`: `frames/shot_006_last_frame.jpg` — literal accepted final rendered frame of generation unit 006
  - `reference_image`: `references/staging/shot_012.jpg` — composition/blocking anchor for original shot 012
  - `reference_image`: `references/setting/ktv-continuity-sheet.jpg` — KTV seating, furniture, camera axis, lighting, and empty-table continuity
  - `reference_image`: `references/characters/jiboda.jpg` — identity and wardrobe for speaking character 季伯达
- Prompt:

```text
WAN 2.6 REFERENCE-TO-VIDEO — GENERATION UNIT 007 (00:26–00:31)

ORIGINAL SHOT MAP:
This generation unit maps original canonical shot IDs: 012. Preserve every mapped story beat in this order. Only the boundaries explicitly marked HARD CUT may cut; all boundaries marked CONTINUE remain one continuous camera take.

REFERENCE MAP:
The supplied first frame is the literal accepted final rendered frame of generation unit 006. Preserve identities, poses, expressions, wardrobe, seats, props, lighting, camera axis and screen direction before the first timed beat.
Image 1 is the composition/blocking anchor for original shot 012. Use it only for that role; the timed beat instructions control motion and cuts.
Image 2 is the KTV seating, furniture, camera axis, lighting, and empty-table continuity. Use it only for that role; the timed beat instructions control motion and cuts.
Image 3 is the identity and wardrobe for speaking character 季伯达. Use it only for that role; the timed beat instructions control motion and cuts.

AUDIO POLICY:
Native audio is required because this unit contains dialogue. Generate only the exact Mandarin lines specified in TIMED BEATS, in that order, synchronized to the named on-screen speaker. No narration, translation, ad-libs, repeated words, overlapping speech, lyrics, or invented speech. Non-speakers do not mouth dialogue. Keep ambience minimal and never include music or off-screen voices. External Mandarin TTS is fallback-only if native generation fails exact-wording or sync QC; do not pre-mix TTS into a successful native-audio render.

OUTPUT:
Create one 5-second cinematic 2D anime generation unit, 16:9, 720P, restrained realistic acting, stable faces and hands, natural breathing and blinks, and subtle hair/fabric response. Model: wan2.6-r2v. Keep timing exact. Do not add montage, transitions, subtitles, labels, logos, watermarks, or visible prompt text.

GLOBAL CONTINUITY:
Modern high-rise KTV/lounge at night with warm amber practical light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table, cards, and small snack plates. The table and room contain no alcohol, bottles, drinks, beverages, cups, drinking glasses, or beverage props at any time. Keep every named actor in the established seat and on the established camera-axis side unless a timed beat explicitly changes framing. Never swap, merge, duplicate, omit, or replace identities. For any wide ensemble view, show exactly these six people and no others: 柳如烟, 伊藤诚, 闺蜜甲, 闺蜜乙, 闺蜜丙, 季伯达. Opening unit 001 must begin with all six already seated: screen-left 柳如烟 then 伊藤诚; central sofa 闺蜜甲, 闺蜜乙, 闺蜜丙; far screen-right 季伯达 facing the group.

TIMED BEATS:
0.0s–5.0s — ORIGINAL SHOT 012 — OPEN ON THE SUPPLIED FIRST FRAME.
Framing/staging: Matching medium close-up on 季伯达 from the same axis. exactly three named people only—柳如烟, 伊藤诚, 季伯达. No friend, guest, extra, duplicate, or unnamed background person. Position continuity: 柳如烟 at frame-left background; 伊藤诚 at center-left background immediately to 柳如烟’s right; 季伯达 at frame-right foreground, seated and facing left toward them.
Action/story beat: 季伯达 delivers the mirror example with deliberate calm, then subtly points the logic back toward 柳如烟.
Camera: Slow 3% push-in, matching shot 011 axis. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 0.4s–4.6s: only 季伯达 says “我的内裤，都是我女闺蜜帮我洗的。你下次也让如烟替你洗。” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

PERFORMANCE GUARDRAILS:
Dialogue belongs only to the named speaker during its exact time window. Preserve the line wording, punctuation-level phrasing, speaker assignment, and order. Do not paraphrase, shorten, expand, repeat, overlap, or move a line to another beat. During silent intervals and the non-dialogue unit, generate no speech and no word-shaped mouth movement. Preserve restrained reactions and a stable final 0.4 seconds for the next unit's first-frame extraction.
```

- Negative prompt:

```text
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, wrong speaker, listener mouthing dialogue, invented speech, extra dialogue, paraphrased dialogue, alcohol, bottles, drinks, beverages, cups, drinking glasses, prop movement, background morphing, camera shake, unplanned cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_007.json`](shot-requests/shot_007.json)

## Generation Unit 008

- 原始镜号：013
- 时间：`00:31–00:36`
- 时长：`5s`
- 对白：柳如烟：季伯达，你恶不恶心？你怎么能让别的女人给你洗内裤？
- 音频：`enable_audio: true`
- 内部硬切前原始镜号：无
- 媒体输入（4/4）：
  - `first_frame`: `frames/shot_007_last_frame.jpg` — literal accepted final rendered frame of generation unit 007
  - `reference_image`: `references/staging/shot_013.jpg` — composition/blocking anchor for original shot 013
  - `reference_image`: `references/setting/ktv-continuity-sheet.jpg` — KTV seating, furniture, camera axis, lighting, and empty-table continuity
  - `reference_image`: `references/characters/liuruyan.jpg` — identity and wardrobe for speaking character 柳如烟
- Prompt:

```text
WAN 2.6 REFERENCE-TO-VIDEO — GENERATION UNIT 008 (00:31–00:36)

ORIGINAL SHOT MAP:
This generation unit maps original canonical shot IDs: 013. Preserve every mapped story beat in this order. Only the boundaries explicitly marked HARD CUT may cut; all boundaries marked CONTINUE remain one continuous camera take.

REFERENCE MAP:
The supplied first frame is the literal accepted final rendered frame of generation unit 007. Preserve identities, poses, expressions, wardrobe, seats, props, lighting, camera axis and screen direction before the first timed beat.
Image 1 is the composition/blocking anchor for original shot 013. Use it only for that role; the timed beat instructions control motion and cuts.
Image 2 is the KTV seating, furniture, camera axis, lighting, and empty-table continuity. Use it only for that role; the timed beat instructions control motion and cuts.
Image 3 is the identity and wardrobe for speaking character 柳如烟. Use it only for that role; the timed beat instructions control motion and cuts.

AUDIO POLICY:
Native audio is required because this unit contains dialogue. Generate only the exact Mandarin lines specified in TIMED BEATS, in that order, synchronized to the named on-screen speaker. No narration, translation, ad-libs, repeated words, overlapping speech, lyrics, or invented speech. Non-speakers do not mouth dialogue. Keep ambience minimal and never include music or off-screen voices. External Mandarin TTS is fallback-only if native generation fails exact-wording or sync QC; do not pre-mix TTS into a successful native-audio render.

OUTPUT:
Create one 5-second cinematic 2D anime generation unit, 16:9, 720P, restrained realistic acting, stable faces and hands, natural breathing and blinks, and subtle hair/fabric response. Model: wan2.6-r2v. Keep timing exact. Do not add montage, transitions, subtitles, labels, logos, watermarks, or visible prompt text.

GLOBAL CONTINUITY:
Modern high-rise KTV/lounge at night with warm amber practical light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table, cards, and small snack plates. The table and room contain no alcohol, bottles, drinks, beverages, cups, drinking glasses, or beverage props at any time. Keep every named actor in the established seat and on the established camera-axis side unless a timed beat explicitly changes framing. Never swap, merge, duplicate, omit, or replace identities. For any wide ensemble view, show exactly these six people and no others: 柳如烟, 伊藤诚, 闺蜜甲, 闺蜜乙, 闺蜜丙, 季伯达. Opening unit 001 must begin with all six already seated: screen-left 柳如烟 then 伊藤诚; central sofa 闺蜜甲, 闺蜜乙, 闺蜜丙; far screen-right 季伯达 facing the group.

TIMED BEATS:
0.0s–5.0s — ORIGINAL SHOT 013 — OPEN ON THE SUPPLIED FIRST FRAME.
Framing/staging: Tight medium close-up on 柳如烟, 伊藤诚 partly visible beside her. exactly two named people only—柳如烟 and 伊藤诚. No friend, guest, extra, duplicate, or unnamed background person. Position continuity: 柳如烟 at frame-left; 伊藤诚 immediately beside her at frame-right. No friend or other person may appear in foreground or background.
Action/story beat: 柳如烟 recoils slightly, anger and disgust rising; she turns sharply toward 季伯达 and emphasizes the accusation.
Camera: Controlled 3% push-in as anger rises. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 0.4s–4.6s: only 柳如烟 says “季伯达，你恶不恶心？你怎么能让别的女人给你洗内裤？” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

PERFORMANCE GUARDRAILS:
Dialogue belongs only to the named speaker during its exact time window. Preserve the line wording, punctuation-level phrasing, speaker assignment, and order. Do not paraphrase, shorten, expand, repeat, overlap, or move a line to another beat. During silent intervals and the non-dialogue unit, generate no speech and no word-shaped mouth movement. Preserve restrained reactions and a stable final 0.4 seconds for the next unit's first-frame extraction.
```

- Negative prompt:

```text
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, wrong speaker, listener mouthing dialogue, invented speech, extra dialogue, paraphrased dialogue, alcohol, bottles, drinks, beverages, cups, drinking glasses, prop movement, background morphing, camera shake, unplanned cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_008.json`](shot-requests/shot_008.json)

## Generation Unit 009

- 原始镜号：014, 015
- 时间：`00:36–00:41`
- 时长：`5s`
- 对白：闺蜜甲：这也太过分了吧？；闺蜜乙：你都有女朋友了，怎么一点边界感都没有？
- 音频：`enable_audio: true`
- 内部硬切前原始镜号：无
- 媒体输入（4/4）：
  - `first_frame`: `frames/shot_008_last_frame.jpg` — literal accepted final rendered frame of generation unit 008
  - `reference_image`: `references/staging/shot_014.jpg` — composition/blocking anchor for original shot 014
  - `reference_image`: `references/setting/ktv-continuity-sheet.jpg` — KTV seating, furniture, camera axis, lighting, and empty-table continuity
  - `reference_image`: `references/staging/shot_015.jpg` — composition/blocking anchor for original shot 015 and the later beat(s)
- Prompt:

```text
WAN 2.6 REFERENCE-TO-VIDEO — GENERATION UNIT 009 (00:36–00:41)

ORIGINAL SHOT MAP:
This generation unit maps original canonical shot IDs: 014, 015. Preserve every mapped story beat in this order. Only the boundaries explicitly marked HARD CUT may cut; all boundaries marked CONTINUE remain one continuous camera take.

REFERENCE MAP:
The supplied first frame is the literal accepted final rendered frame of generation unit 008. Preserve identities, poses, expressions, wardrobe, seats, props, lighting, camera axis and screen direction before the first timed beat.
Image 1 is the composition/blocking anchor for original shot 014. Use it only for that role; the timed beat instructions control motion and cuts.
Image 2 is the KTV seating, furniture, camera axis, lighting, and empty-table continuity. Use it only for that role; the timed beat instructions control motion and cuts.
Image 3 is the composition/blocking anchor for original shot 015 and the later beat(s). Use it only for that role; the timed beat instructions control motion and cuts.

AUDIO POLICY:
Native audio is required because this unit contains dialogue. Generate only the exact Mandarin lines specified in TIMED BEATS, in that order, synchronized to the named on-screen speaker. No narration, translation, ad-libs, repeated words, overlapping speech, lyrics, or invented speech. Non-speakers do not mouth dialogue. Keep ambience minimal and never include music or off-screen voices. External Mandarin TTS is fallback-only if native generation fails exact-wording or sync QC; do not pre-mix TTS into a successful native-audio render.

OUTPUT:
Create one 5-second cinematic 2D anime generation unit, 16:9, 720P, restrained realistic acting, stable faces and hands, natural breathing and blinks, and subtle hair/fabric response. Model: wan2.6-r2v. Keep timing exact. Do not add montage, transitions, subtitles, labels, logos, watermarks, or visible prompt text.

GLOBAL CONTINUITY:
Modern high-rise KTV/lounge at night with warm amber practical light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table, cards, and small snack plates. The table and room contain no alcohol, bottles, drinks, beverages, cups, drinking glasses, or beverage props at any time. Keep every named actor in the established seat and on the established camera-axis side unless a timed beat explicitly changes framing. Never swap, merge, duplicate, omit, or replace identities. For any wide ensemble view, show exactly these six people and no others: 柳如烟, 伊藤诚, 闺蜜甲, 闺蜜乙, 闺蜜丙, 季伯达. Opening unit 001 must begin with all six already seated: screen-left 柳如烟 then 伊藤诚; central sofa 闺蜜甲, 闺蜜乙, 闺蜜丙; far screen-right 季伯达 facing the group.

TIMED BEATS:
0.0s–2.0s — ORIGINAL SHOT 014 — OPEN ON THE SUPPLIED FIRST FRAME.
Framing/staging: Medium three-shot of the girlfriends, favoring 闺蜜甲 at left. exactly three named people only—闺蜜甲, 闺蜜乙, 闺蜜丙. No fourth person, background guest, duplicate, or seat swap. Position continuity: 闺蜜甲 at frame-left/sofa-left; 闺蜜乙 at frame-center/sofa-center; 闺蜜丙 at frame-right/sofa-right.
Action/story beat: 闺蜜甲 leans forward with a frown and challenges him; 闺蜜乙 watches his reaction; 闺蜜丙 raises one brow.
Camera: Gentle 2% push toward 闺蜜甲. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 0.2s–1.8s: only 闺蜜甲 says “这也太过分了吧？” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

2.0s–5.0s — ORIGINAL SHOT 015 — CONTINUE IN THE SAME SHOT; NO CUT.
Framing/staging: Medium three-shot of the girlfriends, favoring 闺蜜乙 at center. exactly three named people only—闺蜜甲, 闺蜜乙, 闺蜜丙. No fourth person, background guest, duplicate, or seat swap. Position continuity: 闺蜜甲 at frame-left/sofa-left; 闺蜜乙 at frame-center/sofa-center; 闺蜜丙 at frame-right/sofa-right.
Action/story beat: 闺蜜乙 sits upright and stresses “边界感”; 闺蜜甲 nods once; 闺蜜丙 shows agreement.
Camera: Slow 3% push toward 闺蜜乙. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 2.3s–4.7s: only 闺蜜乙 says “你都有女朋友了，怎么一点边界感都没有？” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

PERFORMANCE GUARDRAILS:
Dialogue belongs only to the named speaker during its exact time window. Preserve the line wording, punctuation-level phrasing, speaker assignment, and order. Do not paraphrase, shorten, expand, repeat, overlap, or move a line to another beat. During silent intervals and the non-dialogue unit, generate no speech and no word-shaped mouth movement. Preserve restrained reactions and a stable final 0.4 seconds for the next unit's first-frame extraction.
```

- Negative prompt:

```text
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, wrong speaker, listener mouthing dialogue, invented speech, extra dialogue, paraphrased dialogue, alcohol, bottles, drinks, beverages, cups, drinking glasses, prop movement, background morphing, camera shake, unplanned cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_009.json`](shot-requests/shot_009.json)

## Generation Unit 010

- 原始镜号：016, 017
- 时间：`00:41–00:47`
- 时长：`6s`
- 对白：季伯达：怎么了？她是我女闺蜜啊。；伊藤诚：女闺蜜也不行。男女之间得有分寸。
- 音频：`enable_audio: true`
- 内部硬切前原始镜号：017
- 媒体输入（4/4）：
  - `first_frame`: `frames/shot_009_last_frame.jpg` — literal accepted final rendered frame of generation unit 009
  - `reference_image`: `references/staging/shot_016.jpg` — composition/blocking anchor for original shot 016
  - `reference_image`: `references/setting/ktv-continuity-sheet.jpg` — KTV seating, furniture, camera axis, lighting, and empty-table continuity
  - `reference_image`: `references/staging/shot_017.jpg` — composition/blocking anchor for original shot 017 and the later beat(s)
- Prompt:

```text
WAN 2.6 REFERENCE-TO-VIDEO — GENERATION UNIT 010 (00:41–00:47)

ORIGINAL SHOT MAP:
This generation unit maps original canonical shot IDs: 016, 017. Preserve every mapped story beat in this order. Only the boundaries explicitly marked HARD CUT may cut; all boundaries marked CONTINUE remain one continuous camera take.

REFERENCE MAP:
The supplied first frame is the literal accepted final rendered frame of generation unit 009. Preserve identities, poses, expressions, wardrobe, seats, props, lighting, camera axis and screen direction before the first timed beat.
Image 1 is the composition/blocking anchor for original shot 016. Use it only for that role; the timed beat instructions control motion and cuts.
Image 2 is the KTV seating, furniture, camera axis, lighting, and empty-table continuity. Use it only for that role; the timed beat instructions control motion and cuts.
Image 3 is the composition/blocking anchor for original shot 017 and the later beat(s). Use it only for that role; the timed beat instructions control motion and cuts.

AUDIO POLICY:
Native audio is required because this unit contains dialogue. Generate only the exact Mandarin lines specified in TIMED BEATS, in that order, synchronized to the named on-screen speaker. No narration, translation, ad-libs, repeated words, overlapping speech, lyrics, or invented speech. Non-speakers do not mouth dialogue. Keep ambience minimal and never include music or off-screen voices. External Mandarin TTS is fallback-only if native generation fails exact-wording or sync QC; do not pre-mix TTS into a successful native-audio render.

OUTPUT:
Create one 6-second cinematic 2D anime generation unit, 16:9, 720P, restrained realistic acting, stable faces and hands, natural breathing and blinks, and subtle hair/fabric response. Model: wan2.6-r2v. Keep timing exact. Do not add montage, transitions, subtitles, labels, logos, watermarks, or visible prompt text.

GLOBAL CONTINUITY:
Modern high-rise KTV/lounge at night with warm amber practical light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table, cards, and small snack plates. The table and room contain no alcohol, bottles, drinks, beverages, cups, drinking glasses, or beverage props at any time. Keep every named actor in the established seat and on the established camera-axis side unless a timed beat explicitly changes framing. Never swap, merge, duplicate, omit, or replace identities. For any wide ensemble view, show exactly these six people and no others: 柳如烟, 伊藤诚, 闺蜜甲, 闺蜜乙, 闺蜜丙, 季伯达. Opening unit 001 must begin with all six already seated: screen-left 柳如烟 then 伊藤诚; central sofa 闺蜜甲, 闺蜜乙, 闺蜜丙; far screen-right 季伯达 facing the group.

TIMED BEATS:
0.0s–3.0s — ORIGINAL SHOT 016 — OPEN ON THE SUPPLIED FIRST FRAME.
Framing/staging: Matching medium close-up on 季伯达 at right foreground. exactly three named people only—柳如烟, 伊藤诚, 季伯达. No friend, guest, extra, duplicate, or unnamed background person. Position continuity: 柳如烟 at frame-left background; 伊藤诚 at center-left background immediately to 柳如烟’s right; 季伯达 at frame-right foreground, seated and facing left toward them.
Action/story beat: 季伯达 gives a mild shrug and repeats their premise without losing composure.
Camera: Near-locked shot, tiny 2% pull-back after the shrug. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 0.3s–2.7s: only 季伯达 says “怎么了？她是我女闺蜜啊。” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

3.0s–6.0s — ORIGINAL SHOT 017 — HARD CUT AT THIS EXACT BOUNDARY.
Framing/staging: Tight two-shot favoring 伊藤诚 beside 柳如烟. exactly two named people only—柳如烟 and 伊藤诚. No friend, guest, extra, duplicate, or unnamed background person. Position continuity: 柳如烟 at frame-left; 伊藤诚 immediately beside her at frame-right. No friend or other person may appear in foreground or background.
Action/story beat: 伊藤诚 turns serious, gives a small head shake, and lectures about boundaries; 柳如烟 watches.
Camera: Slow 2% push-in toward 伊藤诚. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 3.3s–5.7s: only 伊藤诚 says “女闺蜜也不行。男女之间得有分寸。” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

PERFORMANCE GUARDRAILS:
Dialogue belongs only to the named speaker during its exact time window. Preserve the line wording, punctuation-level phrasing, speaker assignment, and order. Do not paraphrase, shorten, expand, repeat, overlap, or move a line to another beat. During silent intervals and the non-dialogue unit, generate no speech and no word-shaped mouth movement. Preserve restrained reactions and a stable final 0.4 seconds for the next unit's first-frame extraction.
```

- Negative prompt:

```text
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, wrong speaker, listener mouthing dialogue, invented speech, extra dialogue, paraphrased dialogue, alcohol, bottles, drinks, beverages, cups, drinking glasses, prop movement, background morphing, camera shake, unplanned cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_010.json`](shot-requests/shot_010.json)

## Generation Unit 011

- 原始镜号：018
- 时间：`00:47–00:53`
- 时长：`6s`
- 对白：季伯达：奇怪了。刚才你说自己替柳如烟洗过内裤，你们不是也说只是姐妹吗？
- 音频：`enable_audio: true`
- 内部硬切前原始镜号：无
- 媒体输入（4/4）：
  - `first_frame`: `frames/shot_010_last_frame.jpg` — literal accepted final rendered frame of generation unit 010
  - `reference_image`: `references/staging/shot_018.jpg` — composition/blocking anchor for original shot 018
  - `reference_image`: `references/setting/ktv-continuity-sheet.jpg` — KTV seating, furniture, camera axis, lighting, and empty-table continuity
  - `reference_image`: `references/characters/jiboda.jpg` — identity and wardrobe for speaking character 季伯达
- Prompt:

```text
WAN 2.6 REFERENCE-TO-VIDEO — GENERATION UNIT 011 (00:47–00:53)

ORIGINAL SHOT MAP:
This generation unit maps original canonical shot IDs: 018. Preserve every mapped story beat in this order. Only the boundaries explicitly marked HARD CUT may cut; all boundaries marked CONTINUE remain one continuous camera take.

REFERENCE MAP:
The supplied first frame is the literal accepted final rendered frame of generation unit 010. Preserve identities, poses, expressions, wardrobe, seats, props, lighting, camera axis and screen direction before the first timed beat.
Image 1 is the composition/blocking anchor for original shot 018. Use it only for that role; the timed beat instructions control motion and cuts.
Image 2 is the KTV seating, furniture, camera axis, lighting, and empty-table continuity. Use it only for that role; the timed beat instructions control motion and cuts.
Image 3 is the identity and wardrobe for speaking character 季伯达. Use it only for that role; the timed beat instructions control motion and cuts.

AUDIO POLICY:
Native audio is required because this unit contains dialogue. Generate only the exact Mandarin lines specified in TIMED BEATS, in that order, synchronized to the named on-screen speaker. No narration, translation, ad-libs, repeated words, overlapping speech, lyrics, or invented speech. Non-speakers do not mouth dialogue. Keep ambience minimal and never include music or off-screen voices. External Mandarin TTS is fallback-only if native generation fails exact-wording or sync QC; do not pre-mix TTS into a successful native-audio render.

OUTPUT:
Create one 6-second cinematic 2D anime generation unit, 16:9, 720P, restrained realistic acting, stable faces and hands, natural breathing and blinks, and subtle hair/fabric response. Model: wan2.6-r2v. Keep timing exact. Do not add montage, transitions, subtitles, labels, logos, watermarks, or visible prompt text.

GLOBAL CONTINUITY:
Modern high-rise KTV/lounge at night with warm amber practical light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table, cards, and small snack plates. The table and room contain no alcohol, bottles, drinks, beverages, cups, drinking glasses, or beverage props at any time. Keep every named actor in the established seat and on the established camera-axis side unless a timed beat explicitly changes framing. Never swap, merge, duplicate, omit, or replace identities. For any wide ensemble view, show exactly these six people and no others: 柳如烟, 伊藤诚, 闺蜜甲, 闺蜜乙, 闺蜜丙, 季伯达. Opening unit 001 must begin with all six already seated: screen-left 柳如烟 then 伊藤诚; central sofa 闺蜜甲, 闺蜜乙, 闺蜜丙; far screen-right 季伯达 facing the group.

TIMED BEATS:
0.0s–6.0s — ORIGINAL SHOT 018 — OPEN ON THE SUPPLIED FIRST FRAME.
Framing/staging: Medium close-up on 季伯达, same right-side axis. exactly three named people only—柳如烟, 伊藤诚, 季伯达. No friend, guest, extra, duplicate, or unnamed background person. Position continuity: 柳如烟 at frame-left background; 伊藤诚 at center-left background immediately to 柳如烟’s right; 季伯达 at frame-right foreground, seated and facing left toward them.
Action/story beat: 季伯达 calmly reconstructs the contradiction, gaze moving from 伊藤诚 to the group; gestures stay economical.
Camera: Sustained 4% push-in over the full line. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 0.4s–5.6s: only 季伯达 says “奇怪了。刚才你说自己替柳如烟洗过内裤，你们不是也说只是姐妹吗？” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

PERFORMANCE GUARDRAILS:
Dialogue belongs only to the named speaker during its exact time window. Preserve the line wording, punctuation-level phrasing, speaker assignment, and order. Do not paraphrase, shorten, expand, repeat, overlap, or move a line to another beat. During silent intervals and the non-dialogue unit, generate no speech and no word-shaped mouth movement. Preserve restrained reactions and a stable final 0.4 seconds for the next unit's first-frame extraction.
```

- Negative prompt:

```text
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, wrong speaker, listener mouthing dialogue, invented speech, extra dialogue, paraphrased dialogue, alcohol, bottles, drinks, beverages, cups, drinking glasses, prop movement, background morphing, camera shake, unplanned cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_011.json`](shot-requests/shot_011.json)

## Generation Unit 012

- 原始镜号：019, 020
- 时间：`00:53–00:57`
- 时长：`4s`
- 对白：柳如烟：那不一样。；季伯达：哪里不一样？
- 音频：`enable_audio: true`
- 内部硬切前原始镜号：020
- 媒体输入（4/4）：
  - `first_frame`: `frames/shot_011_last_frame.jpg` — literal accepted final rendered frame of generation unit 011
  - `reference_image`: `references/staging/shot_019.jpg` — composition/blocking anchor for original shot 019
  - `reference_image`: `references/setting/ktv-continuity-sheet.jpg` — KTV seating, furniture, camera axis, lighting, and empty-table continuity
  - `reference_image`: `references/staging/shot_020.jpg` — composition/blocking anchor for original shot 020 and the later beat(s)
- Prompt:

```text
WAN 2.6 REFERENCE-TO-VIDEO — GENERATION UNIT 012 (00:53–00:57)

ORIGINAL SHOT MAP:
This generation unit maps original canonical shot IDs: 019, 020. Preserve every mapped story beat in this order. Only the boundaries explicitly marked HARD CUT may cut; all boundaries marked CONTINUE remain one continuous camera take.

REFERENCE MAP:
The supplied first frame is the literal accepted final rendered frame of generation unit 011. Preserve identities, poses, expressions, wardrobe, seats, props, lighting, camera axis and screen direction before the first timed beat.
Image 1 is the composition/blocking anchor for original shot 019. Use it only for that role; the timed beat instructions control motion and cuts.
Image 2 is the KTV seating, furniture, camera axis, lighting, and empty-table continuity. Use it only for that role; the timed beat instructions control motion and cuts.
Image 3 is the composition/blocking anchor for original shot 020 and the later beat(s). Use it only for that role; the timed beat instructions control motion and cuts.

AUDIO POLICY:
Native audio is required because this unit contains dialogue. Generate only the exact Mandarin lines specified in TIMED BEATS, in that order, synchronized to the named on-screen speaker. No narration, translation, ad-libs, repeated words, overlapping speech, lyrics, or invented speech. Non-speakers do not mouth dialogue. Keep ambience minimal and never include music or off-screen voices. External Mandarin TTS is fallback-only if native generation fails exact-wording or sync QC; do not pre-mix TTS into a successful native-audio render.

OUTPUT:
Create one 4-second cinematic 2D anime generation unit, 16:9, 720P, restrained realistic acting, stable faces and hands, natural breathing and blinks, and subtle hair/fabric response. Model: wan2.6-r2v. Keep timing exact. Do not add montage, transitions, subtitles, labels, logos, watermarks, or visible prompt text.

GLOBAL CONTINUITY:
Modern high-rise KTV/lounge at night with warm amber practical light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table, cards, and small snack plates. The table and room contain no alcohol, bottles, drinks, beverages, cups, drinking glasses, or beverage props at any time. Keep every named actor in the established seat and on the established camera-axis side unless a timed beat explicitly changes framing. Never swap, merge, duplicate, omit, or replace identities. For any wide ensemble view, show exactly these six people and no others: 柳如烟, 伊藤诚, 闺蜜甲, 闺蜜乙, 闺蜜丙, 季伯达. Opening unit 001 must begin with all six already seated: screen-left 柳如烟 then 伊藤诚; central sofa 闺蜜甲, 闺蜜乙, 闺蜜丙; far screen-right 季伯达 facing the group.

TIMED BEATS:
0.0s–2.0s — ORIGINAL SHOT 019 — OPEN ON THE SUPPLIED FIRST FRAME.
Framing/staging: Tight reaction close-up on 柳如烟. exactly two named people only—柳如烟 and 伊藤诚. No friend, guest, extra, duplicate, or unnamed background person. Position continuity: 柳如烟 at frame-left; 伊藤诚 immediately beside her at frame-right. No friend or other person may appear in foreground or background.
Action/story beat: 柳如烟 answers defensively, lips tightening and eyes briefly averting.
Camera: Near-locked shot with a 2% push-in. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 0.2s–1.8s: only 柳如烟 says “那不一样。” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

2.0s–4.0s — ORIGINAL SHOT 020 — HARD CUT AT THIS EXACT BOUNDARY.
Framing/staging: Tight medium close-up on 季伯达. exactly three named people only—柳如烟, 伊藤诚, 季伯达. No friend, guest, extra, duplicate, or unnamed background person. Position continuity: 柳如烟 at frame-left background; 伊藤诚 at center-left background immediately to 柳如烟’s right; 季伯达 at frame-right foreground, seated and facing left toward them.
Action/story beat: 季伯达 asks a clean follow-up, slight head tilt, then holds eye contact.
Camera: Tiny 2% push-in, then hold. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 2.2s–3.8s: only 季伯达 says “哪里不一样？” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

PERFORMANCE GUARDRAILS:
Dialogue belongs only to the named speaker during its exact time window. Preserve the line wording, punctuation-level phrasing, speaker assignment, and order. Do not paraphrase, shorten, expand, repeat, overlap, or move a line to another beat. During silent intervals and the non-dialogue unit, generate no speech and no word-shaped mouth movement. Preserve restrained reactions and a stable final 0.4 seconds for the next unit's first-frame extraction.
```

- Negative prompt:

```text
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, wrong speaker, listener mouthing dialogue, invented speech, extra dialogue, paraphrased dialogue, alcohol, bottles, drinks, beverages, cups, drinking glasses, prop movement, background morphing, camera shake, unplanned cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_012.json`](shot-requests/shot_012.json)

## Generation Unit 013

- 原始镜号：021
- 时间：`00:57–01:02`
- 时长：`5s`
- 对白：柳如烟：我和伊藤诚只是纯友谊。我拿他当闺蜜，他也拿我当兄弟。
- 音频：`enable_audio: true`
- 内部硬切前原始镜号：无
- 媒体输入（4/4）：
  - `first_frame`: `frames/shot_012_last_frame.jpg` — literal accepted final rendered frame of generation unit 012
  - `reference_image`: `references/staging/shot_021.jpg` — composition/blocking anchor for original shot 021
  - `reference_image`: `references/setting/ktv-continuity-sheet.jpg` — KTV seating, furniture, camera axis, lighting, and empty-table continuity
  - `reference_image`: `references/characters/liuruyan.jpg` — identity and wardrobe for speaking character 柳如烟
- Prompt:

```text
WAN 2.6 REFERENCE-TO-VIDEO — GENERATION UNIT 013 (00:57–01:02)

ORIGINAL SHOT MAP:
This generation unit maps original canonical shot IDs: 021. Preserve every mapped story beat in this order. Only the boundaries explicitly marked HARD CUT may cut; all boundaries marked CONTINUE remain one continuous camera take.

REFERENCE MAP:
The supplied first frame is the literal accepted final rendered frame of generation unit 012. Preserve identities, poses, expressions, wardrobe, seats, props, lighting, camera axis and screen direction before the first timed beat.
Image 1 is the composition/blocking anchor for original shot 021. Use it only for that role; the timed beat instructions control motion and cuts.
Image 2 is the KTV seating, furniture, camera axis, lighting, and empty-table continuity. Use it only for that role; the timed beat instructions control motion and cuts.
Image 3 is the identity and wardrobe for speaking character 柳如烟. Use it only for that role; the timed beat instructions control motion and cuts.

AUDIO POLICY:
Native audio is required because this unit contains dialogue. Generate only the exact Mandarin lines specified in TIMED BEATS, in that order, synchronized to the named on-screen speaker. No narration, translation, ad-libs, repeated words, overlapping speech, lyrics, or invented speech. Non-speakers do not mouth dialogue. Keep ambience minimal and never include music or off-screen voices. External Mandarin TTS is fallback-only if native generation fails exact-wording or sync QC; do not pre-mix TTS into a successful native-audio render.

OUTPUT:
Create one 5-second cinematic 2D anime generation unit, 16:9, 720P, restrained realistic acting, stable faces and hands, natural breathing and blinks, and subtle hair/fabric response. Model: wan2.6-r2v. Keep timing exact. Do not add montage, transitions, subtitles, labels, logos, watermarks, or visible prompt text.

GLOBAL CONTINUITY:
Modern high-rise KTV/lounge at night with warm amber practical light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table, cards, and small snack plates. The table and room contain no alcohol, bottles, drinks, beverages, cups, drinking glasses, or beverage props at any time. Keep every named actor in the established seat and on the established camera-axis side unless a timed beat explicitly changes framing. Never swap, merge, duplicate, omit, or replace identities. For any wide ensemble view, show exactly these six people and no others: 柳如烟, 伊藤诚, 闺蜜甲, 闺蜜乙, 闺蜜丙, 季伯达. Opening unit 001 must begin with all six already seated: screen-left 柳如烟 then 伊藤诚; central sofa 闺蜜甲, 闺蜜乙, 闺蜜丙; far screen-right 季伯达 facing the group.

TIMED BEATS:
0.0s–5.0s — ORIGINAL SHOT 021 — OPEN ON THE SUPPLIED FIRST FRAME.
Framing/staging: Tight two-shot favoring 柳如烟 with 伊藤诚 beside her. exactly two named people only—柳如烟 and 伊藤诚. No friend, guest, extra, duplicate, or unnamed background person. Position continuity: 柳如烟 at frame-left; 伊藤诚 immediately beside her at frame-right. No friend or other person may appear in foreground or background.
Action/story beat: 柳如烟 explains quickly and defensively, indicating herself then 伊藤诚 without touching him.
Camera: Slow 3% push-in, no pan. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 0.4s–4.6s: only 柳如烟 says “我和伊藤诚只是纯友谊。我拿他当闺蜜，他也拿我当兄弟。” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

PERFORMANCE GUARDRAILS:
Dialogue belongs only to the named speaker during its exact time window. Preserve the line wording, punctuation-level phrasing, speaker assignment, and order. Do not paraphrase, shorten, expand, repeat, overlap, or move a line to another beat. During silent intervals and the non-dialogue unit, generate no speech and no word-shaped mouth movement. Preserve restrained reactions and a stable final 0.4 seconds for the next unit's first-frame extraction.
```

- Negative prompt:

```text
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, wrong speaker, listener mouthing dialogue, invented speech, extra dialogue, paraphrased dialogue, alcohol, bottles, drinks, beverages, cups, drinking glasses, prop movement, background morphing, camera shake, unplanned cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_013.json`](shot-requests/shot_013.json)

## Generation Unit 014

- 原始镜号：022, 023
- 时间：`01:02–01:08`
- 时长：`6s`
- 对白：伊藤诚：对，我们之间根本没有男女之情。；闺蜜甲：他们从小就这样，你一个大男人别这么小气。
- 音频：`enable_audio: true`
- 内部硬切前原始镜号：023
- 媒体输入（4/4）：
  - `first_frame`: `frames/shot_013_last_frame.jpg` — literal accepted final rendered frame of generation unit 013
  - `reference_image`: `references/staging/shot_022.jpg` — composition/blocking anchor for original shot 022
  - `reference_image`: `references/setting/ktv-continuity-sheet.jpg` — KTV seating, furniture, camera axis, lighting, and empty-table continuity
  - `reference_image`: `references/staging/shot_023.jpg` — composition/blocking anchor for original shot 023 and the later beat(s)
- Prompt:

```text
WAN 2.6 REFERENCE-TO-VIDEO — GENERATION UNIT 014 (01:02–01:08)

ORIGINAL SHOT MAP:
This generation unit maps original canonical shot IDs: 022, 023. Preserve every mapped story beat in this order. Only the boundaries explicitly marked HARD CUT may cut; all boundaries marked CONTINUE remain one continuous camera take.

REFERENCE MAP:
The supplied first frame is the literal accepted final rendered frame of generation unit 013. Preserve identities, poses, expressions, wardrobe, seats, props, lighting, camera axis and screen direction before the first timed beat.
Image 1 is the composition/blocking anchor for original shot 022. Use it only for that role; the timed beat instructions control motion and cuts.
Image 2 is the KTV seating, furniture, camera axis, lighting, and empty-table continuity. Use it only for that role; the timed beat instructions control motion and cuts.
Image 3 is the composition/blocking anchor for original shot 023 and the later beat(s). Use it only for that role; the timed beat instructions control motion and cuts.

AUDIO POLICY:
Native audio is required because this unit contains dialogue. Generate only the exact Mandarin lines specified in TIMED BEATS, in that order, synchronized to the named on-screen speaker. No narration, translation, ad-libs, repeated words, overlapping speech, lyrics, or invented speech. Non-speakers do not mouth dialogue. Keep ambience minimal and never include music or off-screen voices. External Mandarin TTS is fallback-only if native generation fails exact-wording or sync QC; do not pre-mix TTS into a successful native-audio render.

OUTPUT:
Create one 6-second cinematic 2D anime generation unit, 16:9, 720P, restrained realistic acting, stable faces and hands, natural breathing and blinks, and subtle hair/fabric response. Model: wan2.6-r2v. Keep timing exact. Do not add montage, transitions, subtitles, labels, logos, watermarks, or visible prompt text.

GLOBAL CONTINUITY:
Modern high-rise KTV/lounge at night with warm amber practical light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table, cards, and small snack plates. The table and room contain no alcohol, bottles, drinks, beverages, cups, drinking glasses, or beverage props at any time. Keep every named actor in the established seat and on the established camera-axis side unless a timed beat explicitly changes framing. Never swap, merge, duplicate, omit, or replace identities. For any wide ensemble view, show exactly these six people and no others: 柳如烟, 伊藤诚, 闺蜜甲, 闺蜜乙, 闺蜜丙, 季伯达. Opening unit 001 must begin with all six already seated: screen-left 柳如烟 then 伊藤诚; central sofa 闺蜜甲, 闺蜜乙, 闺蜜丙; far screen-right 季伯达 facing the group.

TIMED BEATS:
0.0s–3.0s — ORIGINAL SHOT 022 — OPEN ON THE SUPPLIED FIRST FRAME.
Framing/staging: Tight two-shot favoring 伊藤诚 with 柳如烟 beside him. exactly two named people only—柳如烟 and 伊藤诚. No friend, guest, extra, duplicate, or unnamed background person. Position continuity: 柳如烟 at frame-left; 伊藤诚 immediately beside her at frame-right. No friend or other person may appear in foreground or background.
Action/story beat: 伊藤诚 nods and supports her claim, measured but slightly tense.
Camera: Slow 2% push toward 伊藤诚. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 0.3s–2.7s: only 伊藤诚 says “对，我们之间根本没有男女之情。” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

3.0s–6.0s — ORIGINAL SHOT 023 — HARD CUT AT THIS EXACT BOUNDARY.
Framing/staging: Medium three-shot of girlfriends, favoring 闺蜜甲. exactly three named people only—闺蜜甲, 闺蜜乙, 闺蜜丙. No fourth person, background guest, duplicate, or seat swap. Position continuity: 闺蜜甲 at frame-left/sofa-left; 闺蜜乙 at frame-center/sofa-center; 闺蜜丙 at frame-right/sofa-right.
Action/story beat: 闺蜜甲 opens both hands as if the conclusion is obvious; 闺蜜乙 listens; 闺蜜丙 observes.
Camera: Gentle 2% push toward 闺蜜甲. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 3.3s–5.7s: only 闺蜜甲 says “他们从小就这样，你一个大男人别这么小气。” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

PERFORMANCE GUARDRAILS:
Dialogue belongs only to the named speaker during its exact time window. Preserve the line wording, punctuation-level phrasing, speaker assignment, and order. Do not paraphrase, shorten, expand, repeat, overlap, or move a line to another beat. During silent intervals and the non-dialogue unit, generate no speech and no word-shaped mouth movement. Preserve restrained reactions and a stable final 0.4 seconds for the next unit's first-frame extraction.
```

- Negative prompt:

```text
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, wrong speaker, listener mouthing dialogue, invented speech, extra dialogue, paraphrased dialogue, alcohol, bottles, drinks, beverages, cups, drinking glasses, prop movement, background morphing, camera shake, unplanned cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_014.json`](shot-requests/shot_014.json)

## Generation Unit 015

- 原始镜号：024, 025
- 时间：`01:08–01:14`
- 时长：`6s`
- 对白：闺蜜乙：如烟要是真和伊藤诚有什么，还会和你在一起吗？；闺蜜丙：情侣之间最重要的是信任。
- 音频：`enable_audio: true`
- 内部硬切前原始镜号：无
- 媒体输入（4/4）：
  - `first_frame`: `frames/shot_014_last_frame.jpg` — literal accepted final rendered frame of generation unit 014
  - `reference_image`: `references/staging/shot_024.jpg` — composition/blocking anchor for original shot 024
  - `reference_image`: `references/setting/ktv-continuity-sheet.jpg` — KTV seating, furniture, camera axis, lighting, and empty-table continuity
  - `reference_image`: `references/staging/shot_025.jpg` — composition/blocking anchor for original shot 025 and the later beat(s)
- Prompt:

```text
WAN 2.6 REFERENCE-TO-VIDEO — GENERATION UNIT 015 (01:08–01:14)

ORIGINAL SHOT MAP:
This generation unit maps original canonical shot IDs: 024, 025. Preserve every mapped story beat in this order. Only the boundaries explicitly marked HARD CUT may cut; all boundaries marked CONTINUE remain one continuous camera take.

REFERENCE MAP:
The supplied first frame is the literal accepted final rendered frame of generation unit 014. Preserve identities, poses, expressions, wardrobe, seats, props, lighting, camera axis and screen direction before the first timed beat.
Image 1 is the composition/blocking anchor for original shot 024. Use it only for that role; the timed beat instructions control motion and cuts.
Image 2 is the KTV seating, furniture, camera axis, lighting, and empty-table continuity. Use it only for that role; the timed beat instructions control motion and cuts.
Image 3 is the composition/blocking anchor for original shot 025 and the later beat(s). Use it only for that role; the timed beat instructions control motion and cuts.

AUDIO POLICY:
Native audio is required because this unit contains dialogue. Generate only the exact Mandarin lines specified in TIMED BEATS, in that order, synchronized to the named on-screen speaker. No narration, translation, ad-libs, repeated words, overlapping speech, lyrics, or invented speech. Non-speakers do not mouth dialogue. Keep ambience minimal and never include music or off-screen voices. External Mandarin TTS is fallback-only if native generation fails exact-wording or sync QC; do not pre-mix TTS into a successful native-audio render.

OUTPUT:
Create one 6-second cinematic 2D anime generation unit, 16:9, 720P, restrained realistic acting, stable faces and hands, natural breathing and blinks, and subtle hair/fabric response. Model: wan2.6-r2v. Keep timing exact. Do not add montage, transitions, subtitles, labels, logos, watermarks, or visible prompt text.

GLOBAL CONTINUITY:
Modern high-rise KTV/lounge at night with warm amber practical light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table, cards, and small snack plates. The table and room contain no alcohol, bottles, drinks, beverages, cups, drinking glasses, or beverage props at any time. Keep every named actor in the established seat and on the established camera-axis side unless a timed beat explicitly changes framing. Never swap, merge, duplicate, omit, or replace identities. For any wide ensemble view, show exactly these six people and no others: 柳如烟, 伊藤诚, 闺蜜甲, 闺蜜乙, 闺蜜丙, 季伯达. Opening unit 001 must begin with all six already seated: screen-left 柳如烟 then 伊藤诚; central sofa 闺蜜甲, 闺蜜乙, 闺蜜丙; far screen-right 季伯达 facing the group.

TIMED BEATS:
0.0s–3.0s — ORIGINAL SHOT 024 — OPEN ON THE SUPPLIED FIRST FRAME.
Framing/staging: Medium three-shot of girlfriends, favoring 闺蜜乙. exactly three named people only—闺蜜甲, 闺蜜乙, 闺蜜丙. No fourth person, background guest, duplicate, or seat swap. Position continuity: 闺蜜甲 at frame-left/sofa-left; 闺蜜乙 at frame-center/sofa-center; 闺蜜丙 at frame-right/sofa-right.
Action/story beat: 闺蜜乙 leans in and challenges 季伯达 rhetorically; the other two track her.
Camera: Gentle 3% push toward 闺蜜乙. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 0.3s–2.7s: only 闺蜜乙 says “如烟要是真和伊藤诚有什么，还会和你在一起吗？” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

3.0s–6.0s — ORIGINAL SHOT 025 — CONTINUE IN THE SAME SHOT; NO CUT.
Framing/staging: Medium three-shot of girlfriends, favoring 闺蜜丙. exactly three named people only—闺蜜甲, 闺蜜乙, 闺蜜丙. No fourth person, background guest, duplicate, or seat swap. Position continuity: 闺蜜甲 at frame-left/sofa-left; 闺蜜乙 at frame-center/sofa-center; 闺蜜丙 at frame-right/sofa-right.
Action/story beat: 闺蜜丙 sits straighter and delivers a summarizing maxim; the others go still to listen.
Camera: Slow 2% push toward 闺蜜丙. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 3.3s–5.7s: only 闺蜜丙 says “情侣之间最重要的是信任。” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

PERFORMANCE GUARDRAILS:
Dialogue belongs only to the named speaker during its exact time window. Preserve the line wording, punctuation-level phrasing, speaker assignment, and order. Do not paraphrase, shorten, expand, repeat, overlap, or move a line to another beat. During silent intervals and the non-dialogue unit, generate no speech and no word-shaped mouth movement. Preserve restrained reactions and a stable final 0.4 seconds for the next unit's first-frame extraction.
```

- Negative prompt:

```text
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, wrong speaker, listener mouthing dialogue, invented speech, extra dialogue, paraphrased dialogue, alcohol, bottles, drinks, beverages, cups, drinking glasses, prop movement, background morphing, camera shake, unplanned cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_015.json`](shot-requests/shot_015.json)

## Generation Unit 016

- 原始镜号：026
- 时间：`01:14–01:20`
- 时长：`6s`
- 对白：季伯达：所以，伊藤诚可以紧挨着我的女朋友，可以知道她内裤的颜色，还可以替她洗——因为他们是纯友谊。
- 音频：`enable_audio: true`
- 内部硬切前原始镜号：无
- 媒体输入（4/4）：
  - `first_frame`: `frames/shot_015_last_frame.jpg` — literal accepted final rendered frame of generation unit 015
  - `reference_image`: `references/staging/shot_026.jpg` — composition/blocking anchor for original shot 026
  - `reference_image`: `references/setting/ktv-continuity-sheet.jpg` — KTV seating, furniture, camera axis, lighting, and empty-table continuity
  - `reference_image`: `references/characters/jiboda.jpg` — identity and wardrobe for speaking character 季伯达
- Prompt:

```text
WAN 2.6 REFERENCE-TO-VIDEO — GENERATION UNIT 016 (01:14–01:20)

ORIGINAL SHOT MAP:
This generation unit maps original canonical shot IDs: 026. Preserve every mapped story beat in this order. Only the boundaries explicitly marked HARD CUT may cut; all boundaries marked CONTINUE remain one continuous camera take.

REFERENCE MAP:
The supplied first frame is the literal accepted final rendered frame of generation unit 015. Preserve identities, poses, expressions, wardrobe, seats, props, lighting, camera axis and screen direction before the first timed beat.
Image 1 is the composition/blocking anchor for original shot 026. Use it only for that role; the timed beat instructions control motion and cuts.
Image 2 is the KTV seating, furniture, camera axis, lighting, and empty-table continuity. Use it only for that role; the timed beat instructions control motion and cuts.
Image 3 is the identity and wardrobe for speaking character 季伯达. Use it only for that role; the timed beat instructions control motion and cuts.

AUDIO POLICY:
Native audio is required because this unit contains dialogue. Generate only the exact Mandarin lines specified in TIMED BEATS, in that order, synchronized to the named on-screen speaker. No narration, translation, ad-libs, repeated words, overlapping speech, lyrics, or invented speech. Non-speakers do not mouth dialogue. Keep ambience minimal and never include music or off-screen voices. External Mandarin TTS is fallback-only if native generation fails exact-wording or sync QC; do not pre-mix TTS into a successful native-audio render.

OUTPUT:
Create one 6-second cinematic 2D anime generation unit, 16:9, 720P, restrained realistic acting, stable faces and hands, natural breathing and blinks, and subtle hair/fabric response. Model: wan2.6-r2v. Keep timing exact. Do not add montage, transitions, subtitles, labels, logos, watermarks, or visible prompt text.

GLOBAL CONTINUITY:
Modern high-rise KTV/lounge at night with warm amber practical light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table, cards, and small snack plates. The table and room contain no alcohol, bottles, drinks, beverages, cups, drinking glasses, or beverage props at any time. Keep every named actor in the established seat and on the established camera-axis side unless a timed beat explicitly changes framing. Never swap, merge, duplicate, omit, or replace identities. For any wide ensemble view, show exactly these six people and no others: 柳如烟, 伊藤诚, 闺蜜甲, 闺蜜乙, 闺蜜丙, 季伯达. Opening unit 001 must begin with all six already seated: screen-left 柳如烟 then 伊藤诚; central sofa 闺蜜甲, 闺蜜乙, 闺蜜丙; far screen-right 季伯达 facing the group.

TIMED BEATS:
0.0s–6.0s — ORIGINAL SHOT 026 — OPEN ON THE SUPPLIED FIRST FRAME.
Framing/staging: Sustained medium close-up on 季伯达, right foreground, addressing the sofa group. exactly three named people only—柳如烟, 伊藤诚, 季伯达. No friend, guest, extra, duplicate, or unnamed background person. Position continuity: 柳如烟 at frame-left background; 伊藤诚 at center-left background immediately to 柳如烟’s right; 季伯达 at frame-right foreground, seated and facing left toward them.
Action/story beat: 季伯达 enumerates each allowance with controlled hand beats and increasing precision, not shouting.
Camera: Sustained 4% push-in, no cuts or axis change. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 0.4s–5.6s: only 季伯达 says “所以，伊藤诚可以紧挨着我的女朋友，可以知道她内裤的颜色，还可以替她洗——因为他们是纯友谊。” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

PERFORMANCE GUARDRAILS:
Dialogue belongs only to the named speaker during its exact time window. Preserve the line wording, punctuation-level phrasing, speaker assignment, and order. Do not paraphrase, shorten, expand, repeat, overlap, or move a line to another beat. During silent intervals and the non-dialogue unit, generate no speech and no word-shaped mouth movement. Preserve restrained reactions and a stable final 0.4 seconds for the next unit's first-frame extraction.
```

- Negative prompt:

```text
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, wrong speaker, listener mouthing dialogue, invented speech, extra dialogue, paraphrased dialogue, alcohol, bottles, drinks, beverages, cups, drinking glasses, prop movement, background morphing, camera shake, unplanned cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_016.json`](shot-requests/shot_016.json)

## Generation Unit 017

- 原始镜号：027
- 时间：`01:20–01:24`
- 时长：`4s`
- 对白：季伯达：但我的女闺蜜替我洗内裤，就是没有分寸？
- 音频：`enable_audio: true`
- 内部硬切前原始镜号：无
- 媒体输入（4/4）：
  - `first_frame`: `frames/shot_016_last_frame.jpg` — literal accepted final rendered frame of generation unit 016
  - `reference_image`: `references/staging/shot_027.jpg` — composition/blocking anchor for original shot 027
  - `reference_image`: `references/setting/ktv-continuity-sheet.jpg` — KTV seating, furniture, camera axis, lighting, and empty-table continuity
  - `reference_image`: `references/characters/jiboda.jpg` — identity and wardrobe for speaking character 季伯达
- Prompt:

```text
WAN 2.6 REFERENCE-TO-VIDEO — GENERATION UNIT 017 (01:20–01:24)

ORIGINAL SHOT MAP:
This generation unit maps original canonical shot IDs: 027. Preserve every mapped story beat in this order. Only the boundaries explicitly marked HARD CUT may cut; all boundaries marked CONTINUE remain one continuous camera take.

REFERENCE MAP:
The supplied first frame is the literal accepted final rendered frame of generation unit 016. Preserve identities, poses, expressions, wardrobe, seats, props, lighting, camera axis and screen direction before the first timed beat.
Image 1 is the composition/blocking anchor for original shot 027. Use it only for that role; the timed beat instructions control motion and cuts.
Image 2 is the KTV seating, furniture, camera axis, lighting, and empty-table continuity. Use it only for that role; the timed beat instructions control motion and cuts.
Image 3 is the identity and wardrobe for speaking character 季伯达. Use it only for that role; the timed beat instructions control motion and cuts.

AUDIO POLICY:
Native audio is required because this unit contains dialogue. Generate only the exact Mandarin lines specified in TIMED BEATS, in that order, synchronized to the named on-screen speaker. No narration, translation, ad-libs, repeated words, overlapping speech, lyrics, or invented speech. Non-speakers do not mouth dialogue. Keep ambience minimal and never include music or off-screen voices. External Mandarin TTS is fallback-only if native generation fails exact-wording or sync QC; do not pre-mix TTS into a successful native-audio render.

OUTPUT:
Create one 4-second cinematic 2D anime generation unit, 16:9, 720P, restrained realistic acting, stable faces and hands, natural breathing and blinks, and subtle hair/fabric response. Model: wan2.6-r2v. Keep timing exact. Do not add montage, transitions, subtitles, labels, logos, watermarks, or visible prompt text.

GLOBAL CONTINUITY:
Modern high-rise KTV/lounge at night with warm amber practical light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table, cards, and small snack plates. The table and room contain no alcohol, bottles, drinks, beverages, cups, drinking glasses, or beverage props at any time. Keep every named actor in the established seat and on the established camera-axis side unless a timed beat explicitly changes framing. Never swap, merge, duplicate, omit, or replace identities. For any wide ensemble view, show exactly these six people and no others: 柳如烟, 伊藤诚, 闺蜜甲, 闺蜜乙, 闺蜜丙, 季伯达. Opening unit 001 must begin with all six already seated: screen-left 柳如烟 then 伊藤诚; central sofa 闺蜜甲, 闺蜜乙, 闺蜜丙; far screen-right 季伯达 facing the group.

TIMED BEATS:
0.0s–4.0s — ORIGINAL SHOT 027 — OPEN ON THE SUPPLIED FIRST FRAME.
Framing/staging: Matching medium close-up on 季伯达; hold the rhetorical challenge. exactly three named people only—柳如烟, 伊藤诚, 季伯达. No friend, guest, extra, duplicate, or unnamed background person. Position continuity: 柳如烟 at frame-left background; 伊藤诚 at center-left background immediately to 柳如烟’s right; 季伯达 at frame-right foreground, seated and facing left toward them.
Action/story beat: 季伯达 lands the contrast, palm open in a restrained “then why?” gesture, holding the group’s gaze.
Camera: Slow 3% push-in that stops on the final question. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 0.4s–3.6s: only 季伯达 says “但我的女闺蜜替我洗内裤，就是没有分寸？” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

PERFORMANCE GUARDRAILS:
Dialogue belongs only to the named speaker during its exact time window. Preserve the line wording, punctuation-level phrasing, speaker assignment, and order. Do not paraphrase, shorten, expand, repeat, overlap, or move a line to another beat. During silent intervals and the non-dialogue unit, generate no speech and no word-shaped mouth movement. Preserve restrained reactions and a stable final 0.4 seconds for the next unit's first-frame extraction.
```

- Negative prompt:

```text
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, wrong speaker, listener mouthing dialogue, invented speech, extra dialogue, paraphrased dialogue, alcohol, bottles, drinks, beverages, cups, drinking glasses, prop movement, background morphing, camera shake, unplanned cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_017.json`](shot-requests/shot_017.json)

## Generation Unit 018

- 原始镜号：028, 029
- 时间：`01:24–01:29`
- 时长：`5s`
- 对白：柳如烟：季伯达！你故意的是不是？；季伯达：怎么会？
- 音频：`enable_audio: true`
- 内部硬切前原始镜号：029
- 媒体输入（4/4）：
  - `first_frame`: `frames/shot_017_last_frame.jpg` — literal accepted final rendered frame of generation unit 017
  - `reference_image`: `references/staging/shot_028.jpg` — composition/blocking anchor for original shot 028
  - `reference_image`: `references/setting/ktv-continuity-sheet.jpg` — KTV seating, furniture, camera axis, lighting, and empty-table continuity
  - `reference_image`: `references/staging/shot_029.jpg` — composition/blocking anchor for original shot 029 and the later beat(s)
- Prompt:

```text
WAN 2.6 REFERENCE-TO-VIDEO — GENERATION UNIT 018 (01:24–01:29)

ORIGINAL SHOT MAP:
This generation unit maps original canonical shot IDs: 028, 029. Preserve every mapped story beat in this order. Only the boundaries explicitly marked HARD CUT may cut; all boundaries marked CONTINUE remain one continuous camera take.

REFERENCE MAP:
The supplied first frame is the literal accepted final rendered frame of generation unit 017. Preserve identities, poses, expressions, wardrobe, seats, props, lighting, camera axis and screen direction before the first timed beat.
Image 1 is the composition/blocking anchor for original shot 028. Use it only for that role; the timed beat instructions control motion and cuts.
Image 2 is the KTV seating, furniture, camera axis, lighting, and empty-table continuity. Use it only for that role; the timed beat instructions control motion and cuts.
Image 3 is the composition/blocking anchor for original shot 029 and the later beat(s). Use it only for that role; the timed beat instructions control motion and cuts.

AUDIO POLICY:
Native audio is required because this unit contains dialogue. Generate only the exact Mandarin lines specified in TIMED BEATS, in that order, synchronized to the named on-screen speaker. No narration, translation, ad-libs, repeated words, overlapping speech, lyrics, or invented speech. Non-speakers do not mouth dialogue. Keep ambience minimal and never include music or off-screen voices. External Mandarin TTS is fallback-only if native generation fails exact-wording or sync QC; do not pre-mix TTS into a successful native-audio render.

OUTPUT:
Create one 5-second cinematic 2D anime generation unit, 16:9, 720P, restrained realistic acting, stable faces and hands, natural breathing and blinks, and subtle hair/fabric response. Model: wan2.6-r2v. Keep timing exact. Do not add montage, transitions, subtitles, labels, logos, watermarks, or visible prompt text.

GLOBAL CONTINUITY:
Modern high-rise KTV/lounge at night with warm amber practical light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table, cards, and small snack plates. The table and room contain no alcohol, bottles, drinks, beverages, cups, drinking glasses, or beverage props at any time. Keep every named actor in the established seat and on the established camera-axis side unless a timed beat explicitly changes framing. Never swap, merge, duplicate, omit, or replace identities. For any wide ensemble view, show exactly these six people and no others: 柳如烟, 伊藤诚, 闺蜜甲, 闺蜜乙, 闺蜜丙, 季伯达. Opening unit 001 must begin with all six already seated: screen-left 柳如烟 then 伊藤诚; central sofa 闺蜜甲, 闺蜜乙, 闺蜜丙; far screen-right 季伯达 facing the group.

TIMED BEATS:
0.0s–3.0s — ORIGINAL SHOT 028 — OPEN ON THE SUPPLIED FIRST FRAME.
Framing/staging: Tight medium close-up on 柳如烟; 伊藤诚 remains partly visible. exactly two named people only—柳如烟 and 伊藤诚. No friend, guest, extra, duplicate, or unnamed background person. Position continuity: 柳如烟 at frame-left; 伊藤诚 immediately beside her at frame-right. No friend or other person may appear in foreground or background.
Action/story beat: 柳如烟 erupts, leans forward and glares toward 季伯达; anger replaces embarrassment.
Camera: Sharper but still smooth 4% push-in. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 0.3s–2.7s: only 柳如烟 says “季伯达！你故意的是不是？” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

3.0s–5.0s — ORIGINAL SHOT 029 — HARD CUT AT THIS EXACT BOUNDARY.
Framing/staging: Tight medium close-up on 季伯达. exactly three named people only—柳如烟, 伊藤诚, 季伯达. No friend, guest, extra, duplicate, or unnamed background person. Position continuity: 柳如烟 at frame-left background; 伊藤诚 at center-left background immediately to 柳如烟’s right; 季伯达 at frame-right foreground, seated and facing left toward them.
Action/story beat: 季伯达 answers softly with a tiny innocent head tilt, almost dryly amused.
Camera: Near-locked shot; tiny 1% pull-back for dry irony. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 3.2s–4.8s: only 季伯达 says “怎么会？” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

PERFORMANCE GUARDRAILS:
Dialogue belongs only to the named speaker during its exact time window. Preserve the line wording, punctuation-level phrasing, speaker assignment, and order. Do not paraphrase, shorten, expand, repeat, overlap, or move a line to another beat. During silent intervals and the non-dialogue unit, generate no speech and no word-shaped mouth movement. Preserve restrained reactions and a stable final 0.4 seconds for the next unit's first-frame extraction.
```

- Negative prompt:

```text
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, wrong speaker, listener mouthing dialogue, invented speech, extra dialogue, paraphrased dialogue, alcohol, bottles, drinks, beverages, cups, drinking glasses, prop movement, background morphing, camera shake, unplanned cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_018.json`](shot-requests/shot_018.json)

## Generation Unit 019

- 原始镜号：030
- 时间：`01:29–01:33`
- 时长：`4s`
- 对白：季伯达：我只是按照你们的规矩做了一遍。
- 音频：`enable_audio: true`
- 内部硬切前原始镜号：无
- 媒体输入（4/4）：
  - `first_frame`: `frames/shot_018_last_frame.jpg` — literal accepted final rendered frame of generation unit 018
  - `reference_image`: `references/staging/shot_030.jpg` — composition/blocking anchor for original shot 030
  - `reference_image`: `references/setting/ktv-continuity-sheet.jpg` — KTV seating, furniture, camera axis, lighting, and empty-table continuity
  - `reference_image`: `references/characters/jiboda.jpg` — identity and wardrobe for speaking character 季伯达
- Prompt:

```text
WAN 2.6 REFERENCE-TO-VIDEO — GENERATION UNIT 019 (01:29–01:33)

ORIGINAL SHOT MAP:
This generation unit maps original canonical shot IDs: 030. Preserve every mapped story beat in this order. Only the boundaries explicitly marked HARD CUT may cut; all boundaries marked CONTINUE remain one continuous camera take.

REFERENCE MAP:
The supplied first frame is the literal accepted final rendered frame of generation unit 018. Preserve identities, poses, expressions, wardrobe, seats, props, lighting, camera axis and screen direction before the first timed beat.
Image 1 is the composition/blocking anchor for original shot 030. Use it only for that role; the timed beat instructions control motion and cuts.
Image 2 is the KTV seating, furniture, camera axis, lighting, and empty-table continuity. Use it only for that role; the timed beat instructions control motion and cuts.
Image 3 is the identity and wardrobe for speaking character 季伯达. Use it only for that role; the timed beat instructions control motion and cuts.

AUDIO POLICY:
Native audio is required because this unit contains dialogue. Generate only the exact Mandarin lines specified in TIMED BEATS, in that order, synchronized to the named on-screen speaker. No narration, translation, ad-libs, repeated words, overlapping speech, lyrics, or invented speech. Non-speakers do not mouth dialogue. Keep ambience minimal and never include music or off-screen voices. External Mandarin TTS is fallback-only if native generation fails exact-wording or sync QC; do not pre-mix TTS into a successful native-audio render.

OUTPUT:
Create one 4-second cinematic 2D anime generation unit, 16:9, 720P, restrained realistic acting, stable faces and hands, natural breathing and blinks, and subtle hair/fabric response. Model: wan2.6-r2v. Keep timing exact. Do not add montage, transitions, subtitles, labels, logos, watermarks, or visible prompt text.

GLOBAL CONTINUITY:
Modern high-rise KTV/lounge at night with warm amber practical light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table, cards, and small snack plates. The table and room contain no alcohol, bottles, drinks, beverages, cups, drinking glasses, or beverage props at any time. Keep every named actor in the established seat and on the established camera-axis side unless a timed beat explicitly changes framing. Never swap, merge, duplicate, omit, or replace identities. For any wide ensemble view, show exactly these six people and no others: 柳如烟, 伊藤诚, 闺蜜甲, 闺蜜乙, 闺蜜丙, 季伯达. Opening unit 001 must begin with all six already seated: screen-left 柳如烟 then 伊藤诚; central sofa 闺蜜甲, 闺蜜乙, 闺蜜丙; far screen-right 季伯达 facing the group.

TIMED BEATS:
0.0s–4.0s — ORIGINAL SHOT 030 — OPEN ON THE SUPPLIED FIRST FRAME.
Framing/staging: Matching medium close-up on 季伯达, calm and controlled. exactly three named people only—柳如烟, 伊藤诚, 季伯达. No friend, guest, extra, duplicate, or unnamed background person. Position continuity: 柳如烟 at frame-left background; 伊藤诚 at center-left background immediately to 柳如烟’s right; 季伯达 at frame-right foreground, seated and facing left toward them.
Action/story beat: 季伯达 remains composed, one measured hand gesture marking “your rules,” then lets the point sit.
Camera: Slow 3% push-in. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 0.4s–3.6s: only 季伯达 says “我只是按照你们的规矩做了一遍。” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

PERFORMANCE GUARDRAILS:
Dialogue belongs only to the named speaker during its exact time window. Preserve the line wording, punctuation-level phrasing, speaker assignment, and order. Do not paraphrase, shorten, expand, repeat, overlap, or move a line to another beat. During silent intervals and the non-dialogue unit, generate no speech and no word-shaped mouth movement. Preserve restrained reactions and a stable final 0.4 seconds for the next unit's first-frame extraction.
```

- Negative prompt:

```text
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, wrong speaker, listener mouthing dialogue, invented speech, extra dialogue, paraphrased dialogue, alcohol, bottles, drinks, beverages, cups, drinking glasses, prop movement, background morphing, camera shake, unplanned cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_019.json`](shot-requests/shot_019.json)

## Generation Unit 020

- 原始镜号：031
- 时间：`01:33–01:37`
- 时长：`4s`
- 对白：季伯达：怎么轮到你们，规矩就变了？
- 音频：`enable_audio: true`
- 内部硬切前原始镜号：无
- 媒体输入（4/4）：
  - `first_frame`: `frames/shot_019_last_frame.jpg` — literal accepted final rendered frame of generation unit 019
  - `reference_image`: `references/staging/shot_031.jpg` — composition/blocking anchor for original shot 031
  - `reference_image`: `references/setting/ktv-continuity-sheet.jpg` — KTV seating, furniture, camera axis, lighting, and empty-table continuity
  - `reference_image`: `references/characters/jiboda.jpg` — identity and wardrobe for speaking character 季伯达
- Prompt:

```text
WAN 2.6 REFERENCE-TO-VIDEO — GENERATION UNIT 020 (01:33–01:37)

ORIGINAL SHOT MAP:
This generation unit maps original canonical shot IDs: 031. Preserve every mapped story beat in this order. Only the boundaries explicitly marked HARD CUT may cut; all boundaries marked CONTINUE remain one continuous camera take.

REFERENCE MAP:
The supplied first frame is the literal accepted final rendered frame of generation unit 019. Preserve identities, poses, expressions, wardrobe, seats, props, lighting, camera axis and screen direction before the first timed beat.
Image 1 is the composition/blocking anchor for original shot 031. Use it only for that role; the timed beat instructions control motion and cuts.
Image 2 is the KTV seating, furniture, camera axis, lighting, and empty-table continuity. Use it only for that role; the timed beat instructions control motion and cuts.
Image 3 is the identity and wardrobe for speaking character 季伯达. Use it only for that role; the timed beat instructions control motion and cuts.

AUDIO POLICY:
Native audio is required because this unit contains dialogue. Generate only the exact Mandarin lines specified in TIMED BEATS, in that order, synchronized to the named on-screen speaker. No narration, translation, ad-libs, repeated words, overlapping speech, lyrics, or invented speech. Non-speakers do not mouth dialogue. Keep ambience minimal and never include music or off-screen voices. External Mandarin TTS is fallback-only if native generation fails exact-wording or sync QC; do not pre-mix TTS into a successful native-audio render.

OUTPUT:
Create one 4-second cinematic 2D anime generation unit, 16:9, 720P, restrained realistic acting, stable faces and hands, natural breathing and blinks, and subtle hair/fabric response. Model: wan2.6-r2v. Keep timing exact. Do not add montage, transitions, subtitles, labels, logos, watermarks, or visible prompt text.

GLOBAL CONTINUITY:
Modern high-rise KTV/lounge at night with warm amber practical light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table, cards, and small snack plates. The table and room contain no alcohol, bottles, drinks, beverages, cups, drinking glasses, or beverage props at any time. Keep every named actor in the established seat and on the established camera-axis side unless a timed beat explicitly changes framing. Never swap, merge, duplicate, omit, or replace identities. For any wide ensemble view, show exactly these six people and no others: 柳如烟, 伊藤诚, 闺蜜甲, 闺蜜乙, 闺蜜丙, 季伯达. Opening unit 001 must begin with all six already seated: screen-left 柳如烟 then 伊藤诚; central sofa 闺蜜甲, 闺蜜乙, 闺蜜丙; far screen-right 季伯达 facing the group.

TIMED BEATS:
0.0s–4.0s — ORIGINAL SHOT 031 — OPEN ON THE SUPPLIED FIRST FRAME.
Framing/staging: Matching medium close-up on 季伯达; strongest direct challenge. exactly three named people only—柳如烟, 伊藤诚, 季伯达. No friend, guest, extra, duplicate, or unnamed background person. Position continuity: 柳如烟 at frame-left background; 伊藤诚 at center-left background immediately to 柳如烟’s right; 季伯达 at frame-right foreground, seated and facing left toward them.
Action/story beat: 季伯达’s expression hardens slightly; he asks the final question directly and holds still afterward.
Camera: Slow 4% push-in, ending in a firm hold. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
Native synchronized Mandarin audio 0.4s–3.6s: only 季伯达 says “怎么轮到你们，规矩就变了？” exactly once. Match visible mouth motion precisely to this line; all other mouths remain closed except natural breathing.

PERFORMANCE GUARDRAILS:
Dialogue belongs only to the named speaker during its exact time window. Preserve the line wording, punctuation-level phrasing, speaker assignment, and order. Do not paraphrase, shorten, expand, repeat, overlap, or move a line to another beat. During silent intervals and the non-dialogue unit, generate no speech and no word-shaped mouth movement. Preserve restrained reactions and a stable final 0.4 seconds for the next unit's first-frame extraction.
```

- Negative prompt:

```text
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, wrong speaker, listener mouthing dialogue, invented speech, extra dialogue, paraphrased dialogue, alcohol, bottles, drinks, beverages, cups, drinking glasses, prop movement, background morphing, camera shake, unplanned cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_020.json`](shot-requests/shot_020.json)

## Generation Unit 021

- 原始镜号：032
- 时间：`01:37–01:40`
- 时长：`3s`
- 对白：无对白（后期片尾字卡）
- 音频：`enable_audio: false`
- 内部硬切前原始镜号：无
- 媒体输入（3/4）：
  - `first_frame`: `frames/shot_020_last_frame.jpg` — literal accepted final rendered frame of generation unit 020
  - `reference_image`: `references/staging/shot_032.jpg` — composition/blocking anchor for original shot 032
  - `reference_image`: `references/setting/ktv-continuity-sheet.jpg` — KTV seating, furniture, camera axis, lighting, and empty-table continuity
- Prompt:

```text
WAN 2.6 REFERENCE-TO-VIDEO — GENERATION UNIT 021 (01:37–01:40)

ORIGINAL SHOT MAP:
This generation unit maps original canonical shot IDs: 032. Preserve every mapped story beat in this order. Only the boundaries explicitly marked HARD CUT may cut; all boundaries marked CONTINUE remain one continuous camera take.

REFERENCE MAP:
The supplied first frame is the literal accepted final rendered frame of generation unit 020. Preserve identities, poses, expressions, wardrobe, seats, props, lighting, camera axis and screen direction before the first timed beat.
Image 1 is the composition/blocking anchor for original shot 032. Use it only for that role; the timed beat instructions control motion and cuts.
Image 2 is the KTV seating, furniture, camera axis, lighting, and empty-table continuity. Use it only for that role; the timed beat instructions control motion and cuts.

AUDIO POLICY:
This is a non-dialogue unit. Generate a completely silent video with no speech, narration, music, ambience, vocalization, or lip sync. No character mouths words. No invented speech is permitted. The end card is post-production only.

OUTPUT:
Create one 3-second cinematic 2D anime generation unit, 16:9, 720P, restrained realistic acting, stable faces and hands, natural breathing and blinks, and subtle hair/fabric response. Model: wan2.6-r2v. Keep timing exact. Do not add montage, transitions, subtitles, labels, logos, watermarks, or visible prompt text.

GLOBAL CONTINUITY:
Modern high-rise KTV/lounge at night with warm amber practical light, cool blue city windows, dark curtains, neutral sofa, low dark coffee table, cards, and small snack plates. The table and room contain no alcohol, bottles, drinks, beverages, cups, drinking glasses, or beverage props at any time. Keep every named actor in the established seat and on the established camera-axis side unless a timed beat explicitly changes framing. Never swap, merge, duplicate, omit, or replace identities. For any wide ensemble view, show exactly these six people and no others: 柳如烟, 伊藤诚, 闺蜜甲, 闺蜜乙, 闺蜜丙, 季伯达. Opening unit 001 must begin with all six already seated: screen-left 柳如烟 then 伊藤诚; central sofa 闺蜜甲, 闺蜜乙, 闺蜜丙; far screen-right 季伯达 facing the group.

TIMED BEATS:
0.0s–3.0s — ORIGINAL SHOT 032 — OPEN ON THE SUPPLIED FIRST FRAME.
Framing/staging: Wide ensemble bookend matching shot 001, all positions and table geography preserved. exactly six named people only—柳如烟, 伊藤诚, 闺蜜甲, 闺蜜乙, 闺蜜丙, 季伯达. No background guests, extras, duplicates, or missing people. Position continuity: screen-left seating—柳如烟 at far left and 伊藤诚 immediately to her right; central sofa—闺蜜甲 at left seat, 闺蜜乙 at center seat, 闺蜜丙 at right seat; screen-right seating—季伯达 at far right facing the group.
Action/story beat: The room falls awkwardly quiet; smiles fade, gazes shift, and no one offers an answer. End on unresolved group tension.
Camera: Very slow 2% pull-back, echoing the opening while increasing emotional distance. Maintain one continuous subtle move with no reframe, shake, zoom pumping or axis change.
No one speaks or mouths words. Hold the unresolved silence, then add the exact end-card text “有些人要求的不是分寸，而是特权。” only in post-production, never inside the generated frames.

PERFORMANCE GUARDRAILS:
Dialogue belongs only to the named speaker during its exact time window. Preserve the line wording, punctuation-level phrasing, speaker assignment, and order. Do not paraphrase, shorten, expand, repeat, overlap, or move a line to another beat. During silent intervals and the non-dialogue unit, generate no speech and no word-shaped mouth movement. Preserve restrained reactions and a stable final 0.4 seconds for the next unit's first-frame extraction.
```

- Negative prompt:

```text
extra people, missing people, duplicated people, identity drift, face swap, wardrobe change, seat swap, wrong eyeline, axis change, malformed anatomy, extra limbs, warped hands, lip-sync error, wrong speaker, listener mouthing dialogue, invented speech, extra dialogue, paraphrased dialogue, alcohol, bottles, drinks, beverages, cups, drinking glasses, prop movement, background morphing, camera shake, unplanned cuts, transitions, text, subtitles, logo, watermark, UI
```

- Request JSON: [`shot-requests/shot_021.json`](shot-requests/shot_021.json)
