# 《分寸》Dreamina Omni Reference 制作包（32 镜详细时间轴版）

本目录把制作级 Seedance 镜头提示词适配为 Dreamina `AI Video → Omni reference`。每镜保留逐时间段演员动作、精确对白、听者反应、摄影机运动、连续性和负面约束。

## 使用规则

- 每个镜头单独生成；按该镜 `References to upload` 的顺序上传图片，提示词中的 `Image 1`、`Image 2` 等严格对应该顺序。
- `Image 1`：构图和演员调度；`Image 2`：KTV 场景/灯光/家具连续性；后续图片：该镜可见角色身份和服装。
- 模式：`AI Video → Omni reference`；推荐 16:9、1080p、24fps、低或中低运动强度。
- 连续性是 **best effort（尽力保持）**，不是模型保证。镜头 002 起，如界面允许 First Frame 与所需参考一起使用，优先上传上一镜真实末帧并保持开头 0.3–0.5 秒；如不能组合，则留在 Omni Reference 模式，用固定角色/场景参考和本镜构图图近似衔接。
- 冲突时优先级：角色身份 → 座位/调度与机位轴线 → 服装/道具/灯光 → 微小姿势完全匹配。每镜结尾保留 0.3–0.5 秒稳定剪辑余量。
- 故事板图中的镜头标签和字幕只作构图参考，不得生成到视频里；中文字幕后期合成。

## Shot 001｜00:00–00:03
- Speaker/dialogue: **闺蜜甲**：如烟，你输了！
- Duration: `3s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_001.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  4. `Image 4` — [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  5. `Image 5` — [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
  6. `Image 6` — [identity and wardrobe for 闺蜜甲](references/characters/guimi-1.jpg)
  7. `Image 7` — [identity and wardrobe for 闺蜜乙](references/characters/guimi-2.jpg)
  8. `Image 8` — [identity and wardrobe for 闺蜜丙](references/characters/guimi-3.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 001 (00:00–00:03, 3 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 柳如烟: use only for identity and wardrobe for 柳如烟; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 伊藤诚: use only for identity and wardrobe for 伊藤诚; preserve supported visual details exactly.
Image 5 — identity and wardrobe for 季伯达: use only for identity and wardrobe for 季伯达; preserve supported visual details exactly.
Image 6 — identity and wardrobe for 闺蜜甲: use only for identity and wardrobe for 闺蜜甲; preserve supported visual details exactly.
Image 7 — identity and wardrobe for 闺蜜乙: use only for identity and wardrobe for 闺蜜乙; preserve supported visual details exactly.
Image 8 — identity and wardrobe for 闺蜜丙: use only for identity and wardrobe for 闺蜜丙; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 3-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Wide ensemble establishing shot, eye level, preserving the full seating geography and coffee table.
Visible actors and blocking: Visible: 柳如烟 and 伊藤诚 together on the left seating; 闺蜜甲/乙/丙 across the central sofa; 季伯达 at the right side facing them; background guests stay secondary. Everyone remains around the same low coffee table.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
This is the continuity baseline shot. Establish stable character identities, wardrobe, seating, camera axis, furniture, props, city background and warm/cool lighting for later shots. Continuity is a best-effort target, not a guarantee; prioritize correct identity, blocking and readable acting if the model cannot satisfy every visual lock simultaneously. Preserve a stable final 0.3–0.5 seconds as a usable continuity handle for Shot 002.

ACTING DIRECTION:
Primary performance: During the wide party tableau, 闺蜜甲 turns toward 柳如烟, leans forward slightly, raises one hand to claim attention, and says “如烟，你输了！” with playful excitement; 柳如烟 shifts her gaze toward her while the others quiet down and watch.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.4s: hold the established composition; 闺蜜甲 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.4–2.7s: 闺蜜甲 speaks the exact Mandarin line “如烟，你输了！” once, with natural restrained lip sync and the shot-specific performance: During the wide party tableau, 闺蜜甲 turns toward 柳如烟, leans forward slightly, raises one hand to claim attention, and says “如烟，你输了！” with playful excitement; 柳如烟 shifts her gaze toward her while the others quiet down and watch. 2.7–3.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': 'Hold the full seating geography; guests breathe and shift naturally around the coffee table.'} {'start_sec': 1, 'end_sec': 2, 'beat': 'A restrained conversational gesture creates natural group energy; cards and snack plates remain fixed.'} {'start_sec': 2, 'end_sec': 3, 'beat': 'Conversation settles and attention begins to gather toward the game, ready for the cut.'}

CAMERA CHOREOGRAPHY:
Very slow 3% push-in with subtle parallax across the coffee table. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
闺蜜甲: “如烟，你输了！”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 002｜00:03–00:05
- Speaker/dialogue: **闺蜜甲**：选真心话还是大冒险？
- Duration: `2s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_002.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 闺蜜甲](references/characters/guimi-1.jpg)
  4. `Image 4` — [identity and wardrobe for 闺蜜乙](references/characters/guimi-2.jpg)
  5. `Image 5` — [identity and wardrobe for 闺蜜丙](references/characters/guimi-3.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 002 (00:03–00:05, 2 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 闺蜜甲: use only for identity and wardrobe for 闺蜜甲; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 闺蜜乙: use only for identity and wardrobe for 闺蜜乙; preserve supported visual details exactly.
Image 5 — identity and wardrobe for 闺蜜丙: use only for identity and wardrobe for 闺蜜丙; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 2-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Medium three-shot of the three girlfriends across the sofa; 闺蜜甲 is the visual lead.
Visible actors and blocking: Visible: 闺蜜甲 on sofa left, 闺蜜乙 center, 闺蜜丙 right. They remain seated behind the coffee table, shoulders angled toward 季伯达 off-camera/right; no seat swaps.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 001 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 003.

ACTING DIRECTION:
Primary performance: 闺蜜甲 remains leaning forward after announcing the loss, keeps her attention on 柳如烟, and asks “选真心话还是大冒险？” with playful excitement; 闺蜜乙 turns to listen and 闺蜜丙 relaxes with empty hands.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.2s: hold the established composition; 闺蜜甲 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.2–1.8s: 闺蜜甲 speaks the exact Mandarin line “选真心话还是大冒险？” once, with natural restrained lip sync and the shot-specific performance: 闺蜜甲 remains leaning forward after announcing the loss, keeps her attention on 柳如烟, and asks “选真心话还是大冒险？” with playful excitement; 闺蜜乙 turns to listen and 闺蜜丙 relaxes with empty hands. 1.8–2.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '闺蜜甲 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 闺蜜甲 leans forward, lifts one hand and asks with playful excitement; 闺蜜乙 turns to listen; 闺蜜丙 relaxes with empty hands.'} {'start_sec': 1, 'end_sec': 2, 'beat': '闺蜜甲 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Gentle 2% push-in toward 闺蜜甲; no pan. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
闺蜜甲: “选真心话还是大冒险？”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 003｜00:05–00:06
- Speaker/dialogue: **柳如烟**：真心话。
- Duration: `1s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_003.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  4. `Image 4` — [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 003 (00:05–00:06, 1 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 柳如烟: use only for identity and wardrobe for 柳如烟; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 伊藤诚: use only for identity and wardrobe for 伊藤诚; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 1-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Tight medium close-up on 柳如烟 at frame left; 伊藤诚 remains partially visible beside/behind her.
Visible actors and blocking: Visible: 柳如烟 seated at frame left with 伊藤诚 immediately to her right; one or more sofa friends may remain soft in the background exactly as in the source JPG. 柳如烟 does not stand or cross the room.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 002 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 004.

ACTING DIRECTION:
Primary performance: 柳如烟 answers promptly and evenly, a tiny nod and confident eye contact.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.1s: hold the established composition; 柳如烟 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.1–0.9s: 柳如烟 speaks the exact Mandarin line “真心话。” once, with natural restrained lip sync and the shot-specific performance: 柳如烟 answers promptly and evenly, a tiny nod and confident eye contact. 0.9–1.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '柳如烟 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 柳如烟 answers promptly and evenly, a tiny nod and confident eye contact.'}

CAMERA CHOREOGRAPHY:
Near-locked shot with a tiny 1% push-in. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
柳如烟: “真心话。”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 004｜00:06–00:09
- Speaker/dialogue: **闺蜜乙**：那就说说，你今天穿的内裤是什么颜色？
- Duration: `3s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_004.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 闺蜜甲](references/characters/guimi-1.jpg)
  4. `Image 4` — [identity and wardrobe for 闺蜜乙](references/characters/guimi-2.jpg)
  5. `Image 5` — [identity and wardrobe for 闺蜜丙](references/characters/guimi-3.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 004 (00:06–00:09, 3 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 闺蜜甲: use only for identity and wardrobe for 闺蜜甲; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 闺蜜乙: use only for identity and wardrobe for 闺蜜乙; preserve supported visual details exactly.
Image 5 — identity and wardrobe for 闺蜜丙: use only for identity and wardrobe for 闺蜜丙; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 3-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Medium three-shot of the girlfriends; center emphasis on 闺蜜乙.
Visible actors and blocking: Visible: 闺蜜甲 on sofa left, 闺蜜乙 center, 闺蜜丙 right. They remain seated behind the coffee table, shoulders angled toward 季伯达 off-camera/right; no seat swaps.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 003 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 005.

ACTING DIRECTION:
Primary performance: 闺蜜乙 taps/indicates the table lightly and teases; 闺蜜甲 turns toward her; 闺蜜丙 watches 柳如烟.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.4s: hold the established composition; 闺蜜乙 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.4–2.7s: 闺蜜乙 speaks the exact Mandarin line “那就说说，你今天穿的内裤是什么颜色？” once, with natural restrained lip sync and the shot-specific performance: 闺蜜乙 taps/indicates the table lightly and teases; 闺蜜甲 turns toward her; 闺蜜丙 watches 柳如烟. 2.7–3.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '闺蜜乙 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 闺蜜乙 taps/indicates the table lightly and teases; 闺蜜甲 turns toward her; 闺蜜丙 watches 柳如烟.'} {'start_sec': 1, 'end_sec': 2, 'beat': '闺蜜乙 continues the line with coherent restrained lip sync; the primary expression/gesture develops without changing seat or props.'} {'start_sec': 2, 'end_sec': 3, 'beat': '闺蜜乙 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Slow 3% push toward 闺蜜乙; keep all three faces stable. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
闺蜜乙: “那就说说，你今天穿的内裤是什么颜色？”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 005｜00:09–00:10
- Speaker/dialogue: **伊藤诚**：粉红色。
- Duration: `1s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_005.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  4. `Image 4` — [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 005 (00:09–00:10, 1 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 柳如烟: use only for identity and wardrobe for 柳如烟; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 伊藤诚: use only for identity and wardrobe for 伊藤诚; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 1-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Tight two-shot favoring 伊藤诚 beside 柳如烟; keep 柳如烟 visible for reaction.
Visible actors and blocking: Visible: 伊藤诚 seated immediately right of 柳如烟; 柳如烟 remains at frame left and a sofa friend may appear behind. Preserve their close seated spacing without adding contact.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 004 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 006.

ACTING DIRECTION:
Primary performance: 伊藤诚 answers too quickly with casual certainty; 柳如烟 registers immediate discomfort.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.1s: hold the established composition; 伊藤诚 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.1–0.9s: 伊藤诚 speaks the exact Mandarin line “粉红色。” once, with natural restrained lip sync and the shot-specific performance: 伊藤诚 answers too quickly with casual certainty; 柳如烟 registers immediate discomfort. 0.9–1.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '伊藤诚 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 伊藤诚 answers too quickly with casual certainty; 柳如烟 registers immediate discomfort.'}

CAMERA CHOREOGRAPHY:
Near-locked 1% push-in for comic timing. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
伊藤诚: “粉红色。”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 006｜00:10–00:14
- Speaker/dialogue: **伊藤诚**：如烟一直拿我当姐妹。她的内裤，我以前都帮她洗过。
- Duration: `4s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_006.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  4. `Image 4` — [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 006 (00:10–00:14, 4 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 柳如烟: use only for identity and wardrobe for 柳如烟; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 伊藤诚: use only for identity and wardrobe for 伊藤诚; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 4-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Tight two-shot favoring 伊藤诚 beside 柳如烟, with a friend softly present in the background.
Visible actors and blocking: Visible: 伊藤诚 seated immediately right of 柳如烟; 柳如烟 remains at frame left and a sofa friend may appear behind. Preserve their close seated spacing without adding contact.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 005 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 007.

ACTING DIRECTION:
Primary performance: 伊藤诚 continues matter-of-factly, small explanatory hand gesture; 柳如烟 stiffens while the background friend watches.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.5s: hold the established composition; 伊藤诚 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.5–3.6s: 伊藤诚 speaks the exact Mandarin line “如烟一直拿我当姐妹。她的内裤，我以前都帮她洗过。” once, with natural restrained lip sync and the shot-specific performance: 伊藤诚 continues matter-of-factly, small explanatory hand gesture; 柳如烟 stiffens while the background friend watches. 3.6–4.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '伊藤诚 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 伊藤诚 continues matter-of-factly, small explanatory hand gesture; 柳如烟 stiffens while the background friend watches.'} {'start_sec': 1, 'end_sec': 2, 'beat': '伊藤诚 continues the line with coherent restrained lip sync; the primary expression/gesture develops without changing seat or props.'} {'start_sec': 2, 'end_sec': 3, 'beat': '伊藤诚 sustains the next phrase at natural pace; gesture resolves incrementally while listeners respond only with blinks, breath, and micro-expressions.'} {'start_sec': 3, 'end_sec': 4, 'beat': '伊藤诚 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Slow 2% push-in, no reframing. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
伊藤诚: “如烟一直拿我当姐妹。她的内裤，我以前都帮她洗过。”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 007｜00:14–00:16
- Speaker/dialogue: **柳如烟**：你胡说什么呢？
- Duration: `2s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_007.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  4. `Image 4` — [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 007 (00:14–00:16, 2 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 柳如烟: use only for identity and wardrobe for 柳如烟; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 伊藤诚: use only for identity and wardrobe for 伊藤诚; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 2-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Tight medium close-up on 柳如烟, with 伊藤诚 partly visible beside her.
Visible actors and blocking: Visible: 柳如烟 seated at frame left with 伊藤诚 immediately to her right; one or more sofa friends may remain soft in the background exactly as in the source JPG. 柳如烟 does not stand or cross the room.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 006 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 008.

ACTING DIRECTION:
Primary performance: 柳如烟 snaps her gaze toward 伊藤诚, brows tightening; brief embarrassed protest.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.2s: hold the established composition; 柳如烟 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.2–1.8s: 柳如烟 speaks the exact Mandarin line “你胡说什么呢？” once, with natural restrained lip sync and the shot-specific performance: 柳如烟 snaps her gaze toward 伊藤诚, brows tightening; brief embarrassed protest. 1.8–2.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '柳如烟 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 柳如烟 snaps her gaze toward 伊藤诚, brows tightening; brief embarrassed protest.'} {'start_sec': 1, 'end_sec': 2, 'beat': '柳如烟 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Brief 2% push-in synchronized to the protest. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
柳如烟: “你胡说什么呢？”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 008｜00:16–00:18
- Speaker/dialogue: **闺蜜甲**：姐夫，你可别多想。他们从小一起长大。
- Duration: `2s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_008.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 闺蜜甲](references/characters/guimi-1.jpg)
  4. `Image 4` — [identity and wardrobe for 闺蜜乙](references/characters/guimi-2.jpg)
  5. `Image 5` — [identity and wardrobe for 闺蜜丙](references/characters/guimi-3.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 008 (00:16–00:18, 2 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 闺蜜甲: use only for identity and wardrobe for 闺蜜甲; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 闺蜜乙: use only for identity and wardrobe for 闺蜜乙; preserve supported visual details exactly.
Image 5 — identity and wardrobe for 闺蜜丙: use only for identity and wardrobe for 闺蜜丙; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 2-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Medium three-shot of the girlfriends; 闺蜜甲 leads from sofa left.
Visible actors and blocking: Visible: 闺蜜甲 on sofa left, 闺蜜乙 center, 闺蜜丙 right. They remain seated behind the coffee table, shoulders angled toward 季伯达 off-camera/right; no seat swaps.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 007 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 009.

ACTING DIRECTION:
Primary performance: 闺蜜甲 raises a calming palm toward 季伯达 and explains earnestly; the other two listen.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.2s: hold the established composition; 闺蜜甲 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.2–1.8s: 闺蜜甲 speaks the exact Mandarin line “姐夫，你可别多想。他们从小一起长大。” once, with natural restrained lip sync and the shot-specific performance: 闺蜜甲 raises a calming palm toward 季伯达 and explains earnestly; the other two listen. 1.8–2.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '闺蜜甲 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 闺蜜甲 raises a calming palm toward 季伯达 and explains earnestly; the other two listen.'} {'start_sec': 1, 'end_sec': 2, 'beat': '闺蜜甲 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Gentle 2% push toward 闺蜜甲. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
闺蜜甲: “姐夫，你可别多想。他们从小一起长大。”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 009｜00:18–00:20
- Speaker/dialogue: **闺蜜乙**：就是，伊藤诚在我们眼里根本不算男人。
- Duration: `2s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_009.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 闺蜜甲](references/characters/guimi-1.jpg)
  4. `Image 4` — [identity and wardrobe for 闺蜜乙](references/characters/guimi-2.jpg)
  5. `Image 5` — [identity and wardrobe for 闺蜜丙](references/characters/guimi-3.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 009 (00:18–00:20, 2 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 闺蜜甲: use only for identity and wardrobe for 闺蜜甲; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 闺蜜乙: use only for identity and wardrobe for 闺蜜乙; preserve supported visual details exactly.
Image 5 — identity and wardrobe for 闺蜜丙: use only for identity and wardrobe for 闺蜜丙; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 2-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Medium three-shot of the girlfriends; 闺蜜乙 leads from sofa center.
Visible actors and blocking: Visible: 闺蜜甲 on sofa left, 闺蜜乙 center, 闺蜜丙 right. They remain seated behind the coffee table, shoulders angled toward 季伯达 off-camera/right; no seat swaps.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 008 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 010.

ACTING DIRECTION:
Primary performance: 闺蜜乙 turns toward 季伯达 and adds reassurance; 闺蜜甲 settles back; 闺蜜丙 gives a restrained nod.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.2s: hold the established composition; 闺蜜乙 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.2–1.8s: 闺蜜乙 speaks the exact Mandarin line “就是，伊藤诚在我们眼里根本不算男人。” once, with natural restrained lip sync and the shot-specific performance: 闺蜜乙 turns toward 季伯达 and adds reassurance; 闺蜜甲 settles back; 闺蜜丙 gives a restrained nod. 1.8–2.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '闺蜜乙 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 闺蜜乙 turns toward 季伯达 and adds reassurance; 闺蜜甲 settles back; 闺蜜丙 gives a restrained nod.'} {'start_sec': 1, 'end_sec': 2, 'beat': '闺蜜乙 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Tiny lateral ease from left to center, ending on 闺蜜乙. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
闺蜜乙: “就是，伊藤诚在我们眼里根本不算男人。”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 010｜00:20–00:22
- Speaker/dialogue: **闺蜜丙**：他们是纯友谊，关系好才这样。
- Duration: `2s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_010.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 闺蜜甲](references/characters/guimi-1.jpg)
  4. `Image 4` — [identity and wardrobe for 闺蜜乙](references/characters/guimi-2.jpg)
  5. `Image 5` — [identity and wardrobe for 闺蜜丙](references/characters/guimi-3.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 010 (00:20–00:22, 2 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 闺蜜甲: use only for identity and wardrobe for 闺蜜甲; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 闺蜜乙: use only for identity and wardrobe for 闺蜜乙; preserve supported visual details exactly.
Image 5 — identity and wardrobe for 闺蜜丙: use only for identity and wardrobe for 闺蜜丙; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 2-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Medium three-shot of the girlfriends; 闺蜜丙 leads from sofa right.
Visible actors and blocking: Visible: 闺蜜甲 on sofa left, 闺蜜乙 center, 闺蜜丙 right. They remain seated behind the coffee table, shoulders angled toward 季伯达 off-camera/right; no seat swaps.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 009 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 011.

ACTING DIRECTION:
Primary performance: 闺蜜丙 lowers her hand and concludes calmly; the other two turn to her.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.2s: hold the established composition; 闺蜜丙 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.2–1.8s: 闺蜜丙 speaks the exact Mandarin line “他们是纯友谊，关系好才这样。” once, with natural restrained lip sync and the shot-specific performance: 闺蜜丙 lowers her hand and concludes calmly; the other two turn to her. 1.8–2.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '闺蜜丙 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 闺蜜丙 lowers her hand and concludes calmly; the other two turn to her.'} {'start_sec': 1, 'end_sec': 2, 'beat': '闺蜜丙 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Tiny ease right to favor 闺蜜丙. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
闺蜜丙: “他们是纯友谊，关系好才这样。”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 011｜00:22–00:26
- Speaker/dialogue: **季伯达**：小伊，不是我说你。一个大男人，洗什么内裤？
- Duration: `4s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_011.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  4. `Image 4` — [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  5. `Image 5` — [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 011 (00:22–00:26, 4 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 柳如烟: use only for identity and wardrobe for 柳如烟; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 伊藤诚: use only for identity and wardrobe for 伊藤诚; preserve supported visual details exactly.
Image 5 — identity and wardrobe for 季伯达: use only for identity and wardrobe for 季伯达; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 4-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Over-shoulder/medium close-up favoring 季伯达 at the right foreground, facing left toward 伊藤诚.
Visible actors and blocking: Visible: 季伯达 occupies the right foreground in a white shirt, torso turned left toward 柳如烟/伊藤诚 and the opposite sofa; a seated friend may remain soft behind him. He remains seated and does not change sides.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 010 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 012.

ACTING DIRECTION:
Primary performance: 季伯达 begins controlled and faintly incredulous, looking toward 伊藤诚; one restrained open-palm gesture.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.5s: hold the established composition; 季伯达 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.5–3.6s: 季伯达 speaks the exact Mandarin line “小伊，不是我说你。一个大男人，洗什么内裤？” once, with natural restrained lip sync and the shot-specific performance: 季伯达 begins controlled and faintly incredulous, looking toward 伊藤诚; one restrained open-palm gesture. 3.6–4.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '季伯达 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 季伯达 begins controlled and faintly incredulous, looking toward 伊藤诚; one restrained open-palm gesture.'} {'start_sec': 1, 'end_sec': 2, 'beat': '季伯达 continues the line with coherent restrained lip sync; the primary expression/gesture develops without changing seat or props.'} {'start_sec': 2, 'end_sec': 3, 'beat': '季伯达 sustains the next phrase at natural pace; gesture resolves incrementally while listeners respond only with blinks, breath, and micro-expressions.'} {'start_sec': 3, 'end_sec': 4, 'beat': '季伯达 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Slow 3% push-in; stable eyeline. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
季伯达: “小伊，不是我说你。一个大男人，洗什么内裤？”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 012｜00:26–00:31
- Speaker/dialogue: **季伯达**：我的内裤，都是我女闺蜜帮我洗的。你下次也让如烟替你洗。
- Duration: `5s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_012.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  4. `Image 4` — [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  5. `Image 5` — [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 012 (00:26–00:31, 5 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 柳如烟: use only for identity and wardrobe for 柳如烟; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 伊藤诚: use only for identity and wardrobe for 伊藤诚; preserve supported visual details exactly.
Image 5 — identity and wardrobe for 季伯达: use only for identity and wardrobe for 季伯达; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 5-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Matching medium close-up on 季伯达 from the same axis.
Visible actors and blocking: Visible: 季伯达 occupies the right foreground in a white shirt, torso turned left toward 柳如烟/伊藤诚 and the opposite sofa; a seated friend may remain soft behind him. He remains seated and does not change sides.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 011 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 013.

ACTING DIRECTION:
Primary performance: 季伯达 delivers the mirror example with deliberate calm, then subtly points the logic back toward 柳如烟.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.5s: hold the established composition; 季伯达 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.5–4.6s: 季伯达 speaks the exact Mandarin line “我的内裤，都是我女闺蜜帮我洗的。你下次也让如烟替你洗。” once, with natural restrained lip sync and the shot-specific performance: 季伯达 delivers the mirror example with deliberate calm, then subtly points the logic back toward 柳如烟. 4.6–5.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '季伯达 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 季伯达 delivers the mirror example with deliberate calm, then subtly points the logic back toward 柳如烟.'} {'start_sec': 1, 'end_sec': 2, 'beat': '季伯达 continues the line with coherent restrained lip sync; the primary expression/gesture develops without changing seat or props.'} {'start_sec': 2, 'end_sec': 3, 'beat': '季伯达 sustains the next phrase at natural pace; gesture resolves incrementally while listeners respond only with blinks, breath, and micro-expressions.'} {'start_sec': 3, 'end_sec': 4, 'beat': '季伯达 sustains the next phrase at natural pace; gesture resolves incrementally while listeners respond only with blinks, breath, and micro-expressions.'} {'start_sec': 4, 'end_sec': 5, 'beat': '季伯达 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Slow 3% push-in, matching shot 011 axis. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
季伯达: “我的内裤，都是我女闺蜜帮我洗的。你下次也让如烟替你洗。”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 013｜00:31–00:36
- Speaker/dialogue: **柳如烟**：季伯达，你恶不恶心？你怎么能让别的女人给你洗内裤？
- Duration: `5s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_013.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  4. `Image 4` — [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  5. `Image 5` — [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 013 (00:31–00:36, 5 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 柳如烟: use only for identity and wardrobe for 柳如烟; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 伊藤诚: use only for identity and wardrobe for 伊藤诚; preserve supported visual details exactly.
Image 5 — identity and wardrobe for 季伯达: use only for identity and wardrobe for 季伯达; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 5-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Tight medium close-up on 柳如烟, 伊藤诚 partly visible beside her.
Visible actors and blocking: Visible: 柳如烟 seated at frame left with 伊藤诚 immediately to her right; one or more sofa friends may remain soft in the background exactly as in the source JPG. 柳如烟 does not stand or cross the room.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 012 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 014.

ACTING DIRECTION:
Primary performance: 柳如烟 recoils slightly, anger and disgust rising; she turns sharply toward 季伯达 and emphasizes the accusation.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.5s: hold the established composition; 柳如烟 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.5–4.6s: 柳如烟 speaks the exact Mandarin line “季伯达，你恶不恶心？你怎么能让别的女人给你洗内裤？” once, with natural restrained lip sync and the shot-specific performance: 柳如烟 recoils slightly, anger and disgust rising; she turns sharply toward 季伯达 and emphasizes the accusation. 4.6–5.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '柳如烟 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 柳如烟 recoils slightly, anger and disgust rising; she turns sharply toward 季伯达 and emphasizes the accusation.'} {'start_sec': 1, 'end_sec': 2, 'beat': '柳如烟 continues the line with coherent restrained lip sync; the primary expression/gesture develops without changing seat or props.'} {'start_sec': 2, 'end_sec': 3, 'beat': '柳如烟 sustains the next phrase at natural pace; gesture resolves incrementally while listeners respond only with blinks, breath, and micro-expressions.'} {'start_sec': 3, 'end_sec': 4, 'beat': '柳如烟 sustains the next phrase at natural pace; gesture resolves incrementally while listeners respond only with blinks, breath, and micro-expressions.'} {'start_sec': 4, 'end_sec': 5, 'beat': '柳如烟 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Controlled 3% push-in as anger rises. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
柳如烟: “季伯达，你恶不恶心？你怎么能让别的女人给你洗内裤？”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 014｜00:36–00:38
- Speaker/dialogue: **闺蜜甲**：这也太过分了吧？
- Duration: `2s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_014.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 闺蜜甲](references/characters/guimi-1.jpg)
  4. `Image 4` — [identity and wardrobe for 闺蜜乙](references/characters/guimi-2.jpg)
  5. `Image 5` — [identity and wardrobe for 闺蜜丙](references/characters/guimi-3.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 014 (00:36–00:38, 2 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 闺蜜甲: use only for identity and wardrobe for 闺蜜甲; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 闺蜜乙: use only for identity and wardrobe for 闺蜜乙; preserve supported visual details exactly.
Image 5 — identity and wardrobe for 闺蜜丙: use only for identity and wardrobe for 闺蜜丙; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 2-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Medium three-shot of the girlfriends, favoring 闺蜜甲 at left.
Visible actors and blocking: Visible: 闺蜜甲 on sofa left, 闺蜜乙 center, 闺蜜丙 right. They remain seated behind the coffee table, shoulders angled toward 季伯达 off-camera/right; no seat swaps.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 013 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 015.

ACTING DIRECTION:
Primary performance: 闺蜜甲 leans forward with a frown and challenges him; 闺蜜乙 watches his reaction; 闺蜜丙 raises one brow.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.2s: hold the established composition; 闺蜜甲 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.2–1.8s: 闺蜜甲 speaks the exact Mandarin line “这也太过分了吧？” once, with natural restrained lip sync and the shot-specific performance: 闺蜜甲 leans forward with a frown and challenges him; 闺蜜乙 watches his reaction; 闺蜜丙 raises one brow. 1.8–2.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '闺蜜甲 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 闺蜜甲 leans forward with a frown and challenges him; 闺蜜乙 watches his reaction; 闺蜜丙 raises one brow.'} {'start_sec': 1, 'end_sec': 2, 'beat': '闺蜜甲 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Gentle 2% push toward 闺蜜甲. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
闺蜜甲: “这也太过分了吧？”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 015｜00:38–00:41
- Speaker/dialogue: **闺蜜乙**：你都有女朋友了，怎么一点边界感都没有？
- Duration: `3s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_015.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 闺蜜甲](references/characters/guimi-1.jpg)
  4. `Image 4` — [identity and wardrobe for 闺蜜乙](references/characters/guimi-2.jpg)
  5. `Image 5` — [identity and wardrobe for 闺蜜丙](references/characters/guimi-3.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 015 (00:38–00:41, 3 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 闺蜜甲: use only for identity and wardrobe for 闺蜜甲; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 闺蜜乙: use only for identity and wardrobe for 闺蜜乙; preserve supported visual details exactly.
Image 5 — identity and wardrobe for 闺蜜丙: use only for identity and wardrobe for 闺蜜丙; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 3-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Medium three-shot of the girlfriends, favoring 闺蜜乙 at center.
Visible actors and blocking: Visible: 闺蜜甲 on sofa left, 闺蜜乙 center, 闺蜜丙 right. They remain seated behind the coffee table, shoulders angled toward 季伯达 off-camera/right; no seat swaps.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 014 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 016.

ACTING DIRECTION:
Primary performance: 闺蜜乙 sits upright and stresses “边界感”; 闺蜜甲 nods once; 闺蜜丙 shows agreement.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.4s: hold the established composition; 闺蜜乙 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.4–2.7s: 闺蜜乙 speaks the exact Mandarin line “你都有女朋友了，怎么一点边界感都没有？” once, with natural restrained lip sync and the shot-specific performance: 闺蜜乙 sits upright and stresses “边界感”; 闺蜜甲 nods once; 闺蜜丙 shows agreement. 2.7–3.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '闺蜜乙 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 闺蜜乙 sits upright and stresses “边界感”; 闺蜜甲 nods once; 闺蜜丙 shows agreement.'} {'start_sec': 1, 'end_sec': 2, 'beat': '闺蜜乙 continues the line with coherent restrained lip sync; the primary expression/gesture develops without changing seat or props.'} {'start_sec': 2, 'end_sec': 3, 'beat': '闺蜜乙 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Slow 3% push toward 闺蜜乙. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
闺蜜乙: “你都有女朋友了，怎么一点边界感都没有？”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 016｜00:41–00:44
- Speaker/dialogue: **季伯达**：怎么了？她是我女闺蜜啊。
- Duration: `3s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_016.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  4. `Image 4` — [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  5. `Image 5` — [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 016 (00:41–00:44, 3 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 柳如烟: use only for identity and wardrobe for 柳如烟; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 伊藤诚: use only for identity and wardrobe for 伊藤诚; preserve supported visual details exactly.
Image 5 — identity and wardrobe for 季伯达: use only for identity and wardrobe for 季伯达; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 3-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Matching medium close-up on 季伯达 at right foreground.
Visible actors and blocking: Visible: 季伯达 occupies the right foreground in a white shirt, torso turned left toward 柳如烟/伊藤诚 and the opposite sofa; a seated friend may remain soft behind him. He remains seated and does not change sides.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 015 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 017.

ACTING DIRECTION:
Primary performance: 季伯达 gives a mild shrug and repeats their premise without losing composure.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.4s: hold the established composition; 季伯达 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.4–2.7s: 季伯达 speaks the exact Mandarin line “怎么了？她是我女闺蜜啊。” once, with natural restrained lip sync and the shot-specific performance: 季伯达 gives a mild shrug and repeats their premise without losing composure. 2.7–3.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '季伯达 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 季伯达 gives a mild shrug and repeats their premise without losing composure.'} {'start_sec': 1, 'end_sec': 2, 'beat': '季伯达 continues the line with coherent restrained lip sync; the primary expression/gesture develops without changing seat or props.'} {'start_sec': 2, 'end_sec': 3, 'beat': '季伯达 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Near-locked shot, tiny 2% pull-back after the shrug. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
季伯达: “怎么了？她是我女闺蜜啊。”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 017｜00:44–00:47
- Speaker/dialogue: **伊藤诚**：女闺蜜也不行。男女之间得有分寸。
- Duration: `3s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_017.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  4. `Image 4` — [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 017 (00:44–00:47, 3 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 柳如烟: use only for identity and wardrobe for 柳如烟; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 伊藤诚: use only for identity and wardrobe for 伊藤诚; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 3-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Tight two-shot favoring 伊藤诚 beside 柳如烟.
Visible actors and blocking: Visible: 伊藤诚 seated immediately right of 柳如烟; 柳如烟 remains at frame left and a sofa friend may appear behind. Preserve their close seated spacing without adding contact.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 016 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 018.

ACTING DIRECTION:
Primary performance: 伊藤诚 turns serious, gives a small head shake, and lectures about boundaries; 柳如烟 watches.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.4s: hold the established composition; 伊藤诚 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.4–2.7s: 伊藤诚 speaks the exact Mandarin line “女闺蜜也不行。男女之间得有分寸。” once, with natural restrained lip sync and the shot-specific performance: 伊藤诚 turns serious, gives a small head shake, and lectures about boundaries; 柳如烟 watches. 2.7–3.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '伊藤诚 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 伊藤诚 turns serious, gives a small head shake, and lectures about boundaries; 柳如烟 watches.'} {'start_sec': 1, 'end_sec': 2, 'beat': '伊藤诚 continues the line with coherent restrained lip sync; the primary expression/gesture develops without changing seat or props.'} {'start_sec': 2, 'end_sec': 3, 'beat': '伊藤诚 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Slow 2% push-in toward 伊藤诚. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
伊藤诚: “女闺蜜也不行。男女之间得有分寸。”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 018｜00:47–00:53
- Speaker/dialogue: **季伯达**：奇怪了。刚才你说自己替柳如烟洗过内裤，你们不是也说只是姐妹吗？
- Duration: `6s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_018.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  4. `Image 4` — [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  5. `Image 5` — [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 018 (00:47–00:53, 6 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 柳如烟: use only for identity and wardrobe for 柳如烟; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 伊藤诚: use only for identity and wardrobe for 伊藤诚; preserve supported visual details exactly.
Image 5 — identity and wardrobe for 季伯达: use only for identity and wardrobe for 季伯达; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 6-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Medium close-up on 季伯达, same right-side axis.
Visible actors and blocking: Visible: 季伯达 occupies the right foreground in a white shirt, torso turned left toward 柳如烟/伊藤诚 and the opposite sofa; a seated friend may remain soft behind him. He remains seated and does not change sides.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 017 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 019.

ACTING DIRECTION:
Primary performance: 季伯达 calmly reconstructs the contradiction, gaze moving from 伊藤诚 to the group; gestures stay economical.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.5s: hold the established composition; 季伯达 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.5–5.6s: 季伯达 speaks the exact Mandarin line “奇怪了。刚才你说自己替柳如烟洗过内裤，你们不是也说只是姐妹吗？” once, with natural restrained lip sync and the shot-specific performance: 季伯达 calmly reconstructs the contradiction, gaze moving from 伊藤诚 to the group; gestures stay economical. 5.6–6.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '季伯达 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 季伯达 calmly reconstructs the contradiction, gaze moving from 伊藤诚 to the group; gestures stay economical.'} {'start_sec': 1, 'end_sec': 2, 'beat': '季伯达 continues the line with coherent restrained lip sync; the primary expression/gesture develops without changing seat or props.'} {'start_sec': 2, 'end_sec': 3, 'beat': '季伯达 sustains the next phrase at natural pace; gesture resolves incrementally while listeners respond only with blinks, breath, and micro-expressions.'} {'start_sec': 3, 'end_sec': 4, 'beat': '季伯达 sustains the next phrase at natural pace; gesture resolves incrementally while listeners respond only with blinks, breath, and micro-expressions.'} {'start_sec': 4, 'end_sec': 5, 'beat': '季伯达 sustains the next phrase at natural pace; gesture resolves incrementally while listeners respond only with blinks, breath, and micro-expressions.'} {'start_sec': 5, 'end_sec': 6, 'beat': '季伯达 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Sustained 4% push-in over the full line. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
季伯达: “奇怪了。刚才你说自己替柳如烟洗过内裤，你们不是也说只是姐妹吗？”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 019｜00:53–00:55
- Speaker/dialogue: **柳如烟**：那不一样。
- Duration: `2s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_019.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  4. `Image 4` — [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 019 (00:53–00:55, 2 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 柳如烟: use only for identity and wardrobe for 柳如烟; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 伊藤诚: use only for identity and wardrobe for 伊藤诚; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 2-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Tight reaction close-up on 柳如烟.
Visible actors and blocking: Visible: 柳如烟 seated at frame left with 伊藤诚 immediately to her right; one or more sofa friends may remain soft in the background exactly as in the source JPG. 柳如烟 does not stand or cross the room.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 018 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 020.

ACTING DIRECTION:
Primary performance: 柳如烟 answers defensively, lips tightening and eyes briefly averting.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.2s: hold the established composition; 柳如烟 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.2–1.8s: 柳如烟 speaks the exact Mandarin line “那不一样。” once, with natural restrained lip sync and the shot-specific performance: 柳如烟 answers defensively, lips tightening and eyes briefly averting. 1.8–2.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '柳如烟 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 柳如烟 answers defensively, lips tightening and eyes briefly averting.'} {'start_sec': 1, 'end_sec': 2, 'beat': '柳如烟 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Near-locked shot with a 2% push-in. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
柳如烟: “那不一样。”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 020｜00:55–00:57
- Speaker/dialogue: **季伯达**：哪里不一样？
- Duration: `2s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_020.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  4. `Image 4` — [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  5. `Image 5` — [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 020 (00:55–00:57, 2 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 柳如烟: use only for identity and wardrobe for 柳如烟; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 伊藤诚: use only for identity and wardrobe for 伊藤诚; preserve supported visual details exactly.
Image 5 — identity and wardrobe for 季伯达: use only for identity and wardrobe for 季伯达; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 2-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Tight medium close-up on 季伯达.
Visible actors and blocking: Visible: 季伯达 occupies the right foreground in a white shirt, torso turned left toward 柳如烟/伊藤诚 and the opposite sofa; a seated friend may remain soft behind him. He remains seated and does not change sides.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 019 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 021.

ACTING DIRECTION:
Primary performance: 季伯达 asks a clean follow-up, slight head tilt, then holds eye contact.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.2s: hold the established composition; 季伯达 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.2–1.8s: 季伯达 speaks the exact Mandarin line “哪里不一样？” once, with natural restrained lip sync and the shot-specific performance: 季伯达 asks a clean follow-up, slight head tilt, then holds eye contact. 1.8–2.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '季伯达 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 季伯达 asks a clean follow-up, slight head tilt, then holds eye contact.'} {'start_sec': 1, 'end_sec': 2, 'beat': '季伯达 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Tiny 2% push-in, then hold. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
季伯达: “哪里不一样？”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 021｜00:57–01:02
- Speaker/dialogue: **柳如烟**：我和伊藤诚只是纯友谊。我拿他当闺蜜，他也拿我当兄弟。
- Duration: `5s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_021.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  4. `Image 4` — [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 021 (00:57–01:02, 5 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 柳如烟: use only for identity and wardrobe for 柳如烟; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 伊藤诚: use only for identity and wardrobe for 伊藤诚; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 5-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Tight two-shot favoring 柳如烟 with 伊藤诚 beside her.
Visible actors and blocking: Visible: 柳如烟 seated at frame left with 伊藤诚 immediately to her right; one or more sofa friends may remain soft in the background exactly as in the source JPG. 柳如烟 does not stand or cross the room.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 020 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 022.

ACTING DIRECTION:
Primary performance: 柳如烟 explains quickly and defensively, indicating herself then 伊藤诚 without touching him.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.5s: hold the established composition; 柳如烟 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.5–4.6s: 柳如烟 speaks the exact Mandarin line “我和伊藤诚只是纯友谊。我拿他当闺蜜，他也拿我当兄弟。” once, with natural restrained lip sync and the shot-specific performance: 柳如烟 explains quickly and defensively, indicating herself then 伊藤诚 without touching him. 4.6–5.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '柳如烟 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 柳如烟 explains quickly and defensively, indicating herself then 伊藤诚 without touching him.'} {'start_sec': 1, 'end_sec': 2, 'beat': '柳如烟 continues the line with coherent restrained lip sync; the primary expression/gesture develops without changing seat or props.'} {'start_sec': 2, 'end_sec': 3, 'beat': '柳如烟 sustains the next phrase at natural pace; gesture resolves incrementally while listeners respond only with blinks, breath, and micro-expressions.'} {'start_sec': 3, 'end_sec': 4, 'beat': '柳如烟 sustains the next phrase at natural pace; gesture resolves incrementally while listeners respond only with blinks, breath, and micro-expressions.'} {'start_sec': 4, 'end_sec': 5, 'beat': '柳如烟 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Slow 3% push-in, no pan. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
柳如烟: “我和伊藤诚只是纯友谊。我拿他当闺蜜，他也拿我当兄弟。”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 022｜01:02–01:05
- Speaker/dialogue: **伊藤诚**：对，我们之间根本没有男女之情。
- Duration: `3s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_022.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  4. `Image 4` — [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 022 (01:02–01:05, 3 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 柳如烟: use only for identity and wardrobe for 柳如烟; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 伊藤诚: use only for identity and wardrobe for 伊藤诚; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 3-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Tight two-shot favoring 伊藤诚 with 柳如烟 beside him.
Visible actors and blocking: Visible: 伊藤诚 seated immediately right of 柳如烟; 柳如烟 remains at frame left and a sofa friend may appear behind. Preserve their close seated spacing without adding contact.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 021 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 023.

ACTING DIRECTION:
Primary performance: 伊藤诚 nods and supports her claim, measured but slightly tense.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.4s: hold the established composition; 伊藤诚 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.4–2.7s: 伊藤诚 speaks the exact Mandarin line “对，我们之间根本没有男女之情。” once, with natural restrained lip sync and the shot-specific performance: 伊藤诚 nods and supports her claim, measured but slightly tense. 2.7–3.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '伊藤诚 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 伊藤诚 nods and supports her claim, measured but slightly tense.'} {'start_sec': 1, 'end_sec': 2, 'beat': '伊藤诚 continues the line with coherent restrained lip sync; the primary expression/gesture develops without changing seat or props.'} {'start_sec': 2, 'end_sec': 3, 'beat': '伊藤诚 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Slow 2% push toward 伊藤诚. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
伊藤诚: “对，我们之间根本没有男女之情。”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 023｜01:05–01:08
- Speaker/dialogue: **闺蜜甲**：他们从小就这样，你一个大男人别这么小气。
- Duration: `3s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_023.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 闺蜜甲](references/characters/guimi-1.jpg)
  4. `Image 4` — [identity and wardrobe for 闺蜜乙](references/characters/guimi-2.jpg)
  5. `Image 5` — [identity and wardrobe for 闺蜜丙](references/characters/guimi-3.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 023 (01:05–01:08, 3 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 闺蜜甲: use only for identity and wardrobe for 闺蜜甲; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 闺蜜乙: use only for identity and wardrobe for 闺蜜乙; preserve supported visual details exactly.
Image 5 — identity and wardrobe for 闺蜜丙: use only for identity and wardrobe for 闺蜜丙; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 3-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Medium three-shot of girlfriends, favoring 闺蜜甲.
Visible actors and blocking: Visible: 闺蜜甲 on sofa left, 闺蜜乙 center, 闺蜜丙 right. They remain seated behind the coffee table, shoulders angled toward 季伯达 off-camera/right; no seat swaps.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 022 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 024.

ACTING DIRECTION:
Primary performance: 闺蜜甲 opens both hands as if the conclusion is obvious; 闺蜜乙 listens; 闺蜜丙 observes.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.4s: hold the established composition; 闺蜜甲 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.4–2.7s: 闺蜜甲 speaks the exact Mandarin line “他们从小就这样，你一个大男人别这么小气。” once, with natural restrained lip sync and the shot-specific performance: 闺蜜甲 opens both hands as if the conclusion is obvious; 闺蜜乙 listens; 闺蜜丙 observes. 2.7–3.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '闺蜜甲 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 闺蜜甲 opens both hands as if the conclusion is obvious; 闺蜜乙 listens; 闺蜜丙 observes.'} {'start_sec': 1, 'end_sec': 2, 'beat': '闺蜜甲 continues the line with coherent restrained lip sync; the primary expression/gesture develops without changing seat or props.'} {'start_sec': 2, 'end_sec': 3, 'beat': '闺蜜甲 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Gentle 2% push toward 闺蜜甲. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
闺蜜甲: “他们从小就这样，你一个大男人别这么小气。”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 024｜01:08–01:11
- Speaker/dialogue: **闺蜜乙**：如烟要是真和伊藤诚有什么，还会和你在一起吗？
- Duration: `3s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_024.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 闺蜜甲](references/characters/guimi-1.jpg)
  4. `Image 4` — [identity and wardrobe for 闺蜜乙](references/characters/guimi-2.jpg)
  5. `Image 5` — [identity and wardrobe for 闺蜜丙](references/characters/guimi-3.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 024 (01:08–01:11, 3 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 闺蜜甲: use only for identity and wardrobe for 闺蜜甲; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 闺蜜乙: use only for identity and wardrobe for 闺蜜乙; preserve supported visual details exactly.
Image 5 — identity and wardrobe for 闺蜜丙: use only for identity and wardrobe for 闺蜜丙; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 3-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Medium three-shot of girlfriends, favoring 闺蜜乙.
Visible actors and blocking: Visible: 闺蜜甲 on sofa left, 闺蜜乙 center, 闺蜜丙 right. They remain seated behind the coffee table, shoulders angled toward 季伯达 off-camera/right; no seat swaps.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 023 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 025.

ACTING DIRECTION:
Primary performance: 闺蜜乙 leans in and challenges 季伯达 rhetorically; the other two track her.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.4s: hold the established composition; 闺蜜乙 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.4–2.7s: 闺蜜乙 speaks the exact Mandarin line “如烟要是真和伊藤诚有什么，还会和你在一起吗？” once, with natural restrained lip sync and the shot-specific performance: 闺蜜乙 leans in and challenges 季伯达 rhetorically; the other two track her. 2.7–3.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '闺蜜乙 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 闺蜜乙 leans in and challenges 季伯达 rhetorically; the other two track her.'} {'start_sec': 1, 'end_sec': 2, 'beat': '闺蜜乙 continues the line with coherent restrained lip sync; the primary expression/gesture develops without changing seat or props.'} {'start_sec': 2, 'end_sec': 3, 'beat': '闺蜜乙 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Gentle 3% push toward 闺蜜乙. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
闺蜜乙: “如烟要是真和伊藤诚有什么，还会和你在一起吗？”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 025｜01:11–01:14
- Speaker/dialogue: **闺蜜丙**：情侣之间最重要的是信任。
- Duration: `3s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_025.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 闺蜜甲](references/characters/guimi-1.jpg)
  4. `Image 4` — [identity and wardrobe for 闺蜜乙](references/characters/guimi-2.jpg)
  5. `Image 5` — [identity and wardrobe for 闺蜜丙](references/characters/guimi-3.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 025 (01:11–01:14, 3 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 闺蜜甲: use only for identity and wardrobe for 闺蜜甲; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 闺蜜乙: use only for identity and wardrobe for 闺蜜乙; preserve supported visual details exactly.
Image 5 — identity and wardrobe for 闺蜜丙: use only for identity and wardrobe for 闺蜜丙; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 3-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Medium three-shot of girlfriends, favoring 闺蜜丙.
Visible actors and blocking: Visible: 闺蜜甲 on sofa left, 闺蜜乙 center, 闺蜜丙 right. They remain seated behind the coffee table, shoulders angled toward 季伯达 off-camera/right; no seat swaps.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 024 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 026.

ACTING DIRECTION:
Primary performance: 闺蜜丙 sits straighter and delivers a summarizing maxim; the others go still to listen.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.4s: hold the established composition; 闺蜜丙 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.4–2.7s: 闺蜜丙 speaks the exact Mandarin line “情侣之间最重要的是信任。” once, with natural restrained lip sync and the shot-specific performance: 闺蜜丙 sits straighter and delivers a summarizing maxim; the others go still to listen. 2.7–3.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '闺蜜丙 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 闺蜜丙 sits straighter and delivers a summarizing maxim; the others go still to listen.'} {'start_sec': 1, 'end_sec': 2, 'beat': '闺蜜丙 continues the line with coherent restrained lip sync; the primary expression/gesture develops without changing seat or props.'} {'start_sec': 2, 'end_sec': 3, 'beat': '闺蜜丙 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Slow 2% push toward 闺蜜丙. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
闺蜜丙: “情侣之间最重要的是信任。”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 026｜01:14–01:20
- Speaker/dialogue: **季伯达**：所以，伊藤诚可以紧挨着我的女朋友，可以知道她内裤的颜色，还可以替她洗——因为他们是纯友谊。
- Duration: `6s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_026.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  4. `Image 4` — [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  5. `Image 5` — [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 026 (01:14–01:20, 6 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 柳如烟: use only for identity and wardrobe for 柳如烟; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 伊藤诚: use only for identity and wardrobe for 伊藤诚; preserve supported visual details exactly.
Image 5 — identity and wardrobe for 季伯达: use only for identity and wardrobe for 季伯达; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 6-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Sustained medium close-up on 季伯达, right foreground, addressing the sofa group.
Visible actors and blocking: Visible: 季伯达 occupies the right foreground in a white shirt, torso turned left toward 柳如烟/伊藤诚 and the opposite sofa; a seated friend may remain soft behind him. He remains seated and does not change sides.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 025 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 027.

ACTING DIRECTION:
Primary performance: 季伯达 enumerates each allowance with controlled hand beats and increasing precision, not shouting.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.5s: hold the established composition; 季伯达 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.5–5.6s: 季伯达 speaks the exact Mandarin line “所以，伊藤诚可以紧挨着我的女朋友，可以知道她内裤的颜色，还可以替她洗——因为他们是纯友谊。” once, with natural restrained lip sync and the shot-specific performance: 季伯达 enumerates each allowance with controlled hand beats and increasing precision, not shouting. 5.6–6.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '季伯达 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 季伯达 enumerates each allowance with controlled hand beats and increasing precision, not shouting.'} {'start_sec': 1, 'end_sec': 2, 'beat': '季伯达 continues the line with coherent restrained lip sync; the primary expression/gesture develops without changing seat or props.'} {'start_sec': 2, 'end_sec': 3, 'beat': '季伯达 sustains the next phrase at natural pace; gesture resolves incrementally while listeners respond only with blinks, breath, and micro-expressions.'} {'start_sec': 3, 'end_sec': 4, 'beat': '季伯达 sustains the next phrase at natural pace; gesture resolves incrementally while listeners respond only with blinks, breath, and micro-expressions.'} {'start_sec': 4, 'end_sec': 5, 'beat': '季伯达 sustains the next phrase at natural pace; gesture resolves incrementally while listeners respond only with blinks, breath, and micro-expressions.'} {'start_sec': 5, 'end_sec': 6, 'beat': '季伯达 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Sustained 4% push-in, no cuts or axis change. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
季伯达: “所以，伊藤诚可以紧挨着我的女朋友，可以知道她内裤的颜色，还可以替她洗——因为他们是纯友谊。”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 027｜01:20–01:24
- Speaker/dialogue: **季伯达**：但我的女闺蜜替我洗内裤，就是没有分寸？
- Duration: `4s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_027.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  4. `Image 4` — [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  5. `Image 5` — [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 027 (01:20–01:24, 4 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 柳如烟: use only for identity and wardrobe for 柳如烟; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 伊藤诚: use only for identity and wardrobe for 伊藤诚; preserve supported visual details exactly.
Image 5 — identity and wardrobe for 季伯达: use only for identity and wardrobe for 季伯达; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 4-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Matching medium close-up on 季伯达; hold the rhetorical challenge.
Visible actors and blocking: Visible: 季伯达 occupies the right foreground in a white shirt, torso turned left toward 柳如烟/伊藤诚 and the opposite sofa; a seated friend may remain soft behind him. He remains seated and does not change sides.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 026 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 028.

ACTING DIRECTION:
Primary performance: 季伯达 lands the contrast, palm open in a restrained “then why?” gesture, holding the group’s gaze.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.5s: hold the established composition; 季伯达 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.5–3.6s: 季伯达 speaks the exact Mandarin line “但我的女闺蜜替我洗内裤，就是没有分寸？” once, with natural restrained lip sync and the shot-specific performance: 季伯达 lands the contrast, palm open in a restrained “then why?” gesture, holding the group’s gaze. 3.6–4.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '季伯达 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 季伯达 lands the contrast, palm open in a restrained “then why?” gesture, holding the group’s gaze.'} {'start_sec': 1, 'end_sec': 2, 'beat': '季伯达 continues the line with coherent restrained lip sync; the primary expression/gesture develops without changing seat or props.'} {'start_sec': 2, 'end_sec': 3, 'beat': '季伯达 sustains the next phrase at natural pace; gesture resolves incrementally while listeners respond only with blinks, breath, and micro-expressions.'} {'start_sec': 3, 'end_sec': 4, 'beat': '季伯达 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Slow 3% push-in that stops on the final question. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
季伯达: “但我的女闺蜜替我洗内裤，就是没有分寸？”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 028｜01:24–01:27
- Speaker/dialogue: **柳如烟**：季伯达！你故意的是不是？
- Duration: `3s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_028.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  4. `Image 4` — [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  5. `Image 5` — [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 028 (01:24–01:27, 3 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 柳如烟: use only for identity and wardrobe for 柳如烟; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 伊藤诚: use only for identity and wardrobe for 伊藤诚; preserve supported visual details exactly.
Image 5 — identity and wardrobe for 季伯达: use only for identity and wardrobe for 季伯达; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 3-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Tight medium close-up on 柳如烟; 伊藤诚 remains partly visible.
Visible actors and blocking: Visible: 柳如烟 seated at frame left with 伊藤诚 immediately to her right; one or more sofa friends may remain soft in the background exactly as in the source JPG. 柳如烟 does not stand or cross the room.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 027 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 029.

ACTING DIRECTION:
Primary performance: 柳如烟 erupts, leans forward and glares toward 季伯达; anger replaces embarrassment.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.4s: hold the established composition; 柳如烟 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.4–2.7s: 柳如烟 speaks the exact Mandarin line “季伯达！你故意的是不是？” once, with natural restrained lip sync and the shot-specific performance: 柳如烟 erupts, leans forward and glares toward 季伯达; anger replaces embarrassment. 2.7–3.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '柳如烟 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 柳如烟 erupts, leans forward and glares toward 季伯达; anger replaces embarrassment.'} {'start_sec': 1, 'end_sec': 2, 'beat': '柳如烟 continues the line with coherent restrained lip sync; the primary expression/gesture develops without changing seat or props.'} {'start_sec': 2, 'end_sec': 3, 'beat': '柳如烟 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Sharper but still smooth 4% push-in. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
柳如烟: “季伯达！你故意的是不是？”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 029｜01:27–01:29
- Speaker/dialogue: **季伯达**：怎么会？
- Duration: `2s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_029.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  4. `Image 4` — [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  5. `Image 5` — [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 029 (01:27–01:29, 2 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 柳如烟: use only for identity and wardrobe for 柳如烟; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 伊藤诚: use only for identity and wardrobe for 伊藤诚; preserve supported visual details exactly.
Image 5 — identity and wardrobe for 季伯达: use only for identity and wardrobe for 季伯达; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 2-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Tight medium close-up on 季伯达.
Visible actors and blocking: Visible: 季伯达 occupies the right foreground in a white shirt, torso turned left toward 柳如烟/伊藤诚 and the opposite sofa; a seated friend may remain soft behind him. He remains seated and does not change sides.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 028 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 030.

ACTING DIRECTION:
Primary performance: 季伯达 answers softly with a tiny innocent head tilt, almost dryly amused.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.2s: hold the established composition; 季伯达 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.2–1.8s: 季伯达 speaks the exact Mandarin line “怎么会？” once, with natural restrained lip sync and the shot-specific performance: 季伯达 answers softly with a tiny innocent head tilt, almost dryly amused. 1.8–2.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '季伯达 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 季伯达 answers softly with a tiny innocent head tilt, almost dryly amused.'} {'start_sec': 1, 'end_sec': 2, 'beat': '季伯达 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Near-locked shot; tiny 1% pull-back for dry irony. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
季伯达: “怎么会？”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 030｜01:29–01:33
- Speaker/dialogue: **季伯达**：我只是按照你们的规矩做了一遍。
- Duration: `4s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_030.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  4. `Image 4` — [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  5. `Image 5` — [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 030 (01:29–01:33, 4 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 柳如烟: use only for identity and wardrobe for 柳如烟; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 伊藤诚: use only for identity and wardrobe for 伊藤诚; preserve supported visual details exactly.
Image 5 — identity and wardrobe for 季伯达: use only for identity and wardrobe for 季伯达; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 4-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Matching medium close-up on 季伯达, calm and controlled.
Visible actors and blocking: Visible: 季伯达 occupies the right foreground in a white shirt, torso turned left toward 柳如烟/伊藤诚 and the opposite sofa; a seated friend may remain soft behind him. He remains seated and does not change sides.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 029 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 031.

ACTING DIRECTION:
Primary performance: 季伯达 remains composed, one measured hand gesture marking “your rules,” then lets the point sit.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.5s: hold the established composition; 季伯达 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.5–3.6s: 季伯达 speaks the exact Mandarin line “我只是按照你们的规矩做了一遍。” once, with natural restrained lip sync and the shot-specific performance: 季伯达 remains composed, one measured hand gesture marking “your rules,” then lets the point sit. 3.6–4.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '季伯达 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 季伯达 remains composed, one measured hand gesture marking “your rules,” then lets the point sit.'} {'start_sec': 1, 'end_sec': 2, 'beat': '季伯达 continues the line with coherent restrained lip sync; the primary expression/gesture develops without changing seat or props.'} {'start_sec': 2, 'end_sec': 3, 'beat': '季伯达 sustains the next phrase at natural pace; gesture resolves incrementally while listeners respond only with blinks, breath, and micro-expressions.'} {'start_sec': 3, 'end_sec': 4, 'beat': '季伯达 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Slow 3% push-in. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
季伯达: “我只是按照你们的规矩做了一遍。”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 031｜01:33–01:37
- Speaker/dialogue: **季伯达**：怎么轮到你们，规矩就变了？
- Duration: `4s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_031.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  4. `Image 4` — [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  5. `Image 5` — [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 031 (01:33–01:37, 4 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 柳如烟: use only for identity and wardrobe for 柳如烟; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 伊藤诚: use only for identity and wardrobe for 伊藤诚; preserve supported visual details exactly.
Image 5 — identity and wardrobe for 季伯达: use only for identity and wardrobe for 季伯达; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 4-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Matching medium close-up on 季伯达; strongest direct challenge.
Visible actors and blocking: Visible: 季伯达 occupies the right foreground in a white shirt, torso turned left toward 柳如烟/伊藤诚 and the opposite sofa; a seated friend may remain soft behind him. He remains seated and does not change sides.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 030 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds as a continuity handle for Shot 032.

ACTING DIRECTION:
Primary performance: 季伯达’s expression hardens slightly; he asks the final question directly and holds still afterward.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.5s: hold the established composition; 季伯达 takes a subtle breath and acquires the established eyeline while listeners remain attentive. 0.5–3.6s: 季伯达 speaks the exact Mandarin line “怎么轮到你们，规矩就变了？” once, with natural restrained lip sync and the shot-specific performance: 季伯达’s expression hardens slightly; he asks the final question directly and holds still afterward. 3.6–4.0s: the speaker closes the mouth and resolves the gesture; listeners give only the restrained reaction described by the shot, then everyone holds their positions for the cut. Do not overlap, repeat, paraphrase, shorten, or extend the line. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': '季伯达 acquires the established eyeline, inhales subtly, and begins the exact Mandarin line; 季伯达’s expression hardens slightly; he asks the final question directly and holds still afterward.'} {'start_sec': 1, 'end_sec': 2, 'beat': '季伯达 continues the line with coherent restrained lip sync; the primary expression/gesture develops without changing seat or props.'} {'start_sec': 2, 'end_sec': 3, 'beat': '季伯达 sustains the next phrase at natural pace; gesture resolves incrementally while listeners respond only with blinks, breath, and micro-expressions.'} {'start_sec': 3, 'end_sec': 4, 'beat': '季伯达 completes the exact line and final shot-specific gesture; listeners register a restrained reaction, then hold for the cut.'}

CAMERA CHOREOGRAPHY:
Slow 4% push-in, ending in a firm hold. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
季伯达: “怎么轮到你们，规矩就变了？”
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

## Shot 032｜01:37–01:40
- Speaker/dialogue: **—**：—
- Duration: `3s`
- References to upload (exact order):
  1. `Image 1` — [composition and staging](references/staging/shot_032.jpg)
  2. `Image 2` — [KTV setting, lighting, furniture and spatial continuity](references/setting/ktv-continuity-sheet.jpg)
  3. `Image 3` — [identity and wardrobe for 柳如烟](references/characters/liuruyan.jpg)
  4. `Image 4` — [identity and wardrobe for 伊藤诚](references/characters/yitengcheng.jpg)
  5. `Image 5` — [identity and wardrobe for 季伯达](references/characters/jiboda.jpg)
  6. `Image 6` — [identity and wardrobe for 闺蜜甲](references/characters/guimi-1.jpg)
  7. `Image 7` — [identity and wardrobe for 闺蜜乙](references/characters/guimi-2.jpg)
  8. `Image 8` — [identity and wardrobe for 闺蜜丙](references/characters/guimi-3.jpg)
- Detailed Dreamina Omni prompt:

```
DREAMINA / SEEDANCE OMNI REFERENCE — SHOT 032 (01:37–01:40, 3 seconds)

REFERENCE MAP — upload in exactly this order:
Image 1 — composition and staging: use only for composition and staging; preserve supported visual details exactly.
Image 2 — KTV setting, lighting, furniture and spatial continuity: use only for KTV setting, lighting, furniture and spatial continuity; preserve supported visual details exactly.
Image 3 — identity and wardrobe for 柳如烟: use only for identity and wardrobe for 柳如烟; preserve supported visual details exactly.
Image 4 — identity and wardrobe for 伊藤诚: use only for identity and wardrobe for 伊藤诚; preserve supported visual details exactly.
Image 5 — identity and wardrobe for 季伯达: use only for identity and wardrobe for 季伯达; preserve supported visual details exactly.
Image 6 — identity and wardrobe for 闺蜜甲: use only for identity and wardrobe for 闺蜜甲; preserve supported visual details exactly.
Image 7 — identity and wardrobe for 闺蜜乙: use only for identity and wardrobe for 闺蜜乙; preserve supported visual details exactly.
Image 8 — identity and wardrobe for 闺蜜丙: use only for identity and wardrobe for 闺蜜丙; preserve supported visual details exactly.

OUTPUT AND STYLE:
Create one continuous 3-second cinematic 2D anime shot in 16:9 at 1080p/24fps. Restrained realistic acting, coherent facial animation, stable hands, natural breathing and blinks, subtle hair and fabric response. No cut, transition, montage, or shot change.

COMPOSITION AND SET:
Use Image 1 as the shot-specific composition, framing, blocking, pose, eyeline and prop-layout guide, while ignoring/removing every storyboard label and subtitle band. Use Image 2 to preserve the same modern high-rise KTV/lounge at night, neutral sofa, low dark coffee table, dark curtains, warm amber interior practicals and cool blue city-window light. Framing: Wide ensemble bookend matching shot 001, all positions and table geography preserved.
Visible actors and blocking: Visible: 柳如烟 and 伊藤诚 together on the left seating; 闺蜜甲/乙/丙 across the central sofa; 季伯达 at the right side facing them; background guests stay secondary. Everyone remains around the same low coffee table.

IDENTITY AND CONTINUITY:
Use the character portrait reference images in the Reference Map to lock each visible actor’s face, hairstyle, skin tone, wardrobe and body proportions. Never swap, merge, duplicate or replace identities. Keep every actor on the assigned side of the axis and in the assigned seat. For continuity with the preceding shot, preserve the established screen direction, poses, expressions, wardrobe, lighting, camera axis and prop state at the opening; begin movement smoothly without a pose reset, camera jump or prop change. Use this shot’s JPG as the first-frame identity/composition reference. Lock character faces, hair, wardrobe, body proportions, seating side, eyelines, table/card/snack-plate positions, city-night background, and warm/cool lighting to the source JPG and adjacent shots. Do not animate storyboard labels or subtitles: remove/crop/clean all labels and caption bands before image-to-video; composite exact Chinese dialogue or final card afterward in editing.

BEST-EFFORT SHOT-TO-SHOT CONTINUITY:
If the Dreamina workflow permits a First Frame together with the required references, use the literal final rendered frame of Shot 031 as this shot’s First Frame. Hold that supplied frame as closely as possible for the opening 0.3–0.5 seconds—same composition, identities, faces, hair, wardrobe, poses, expressions, seating, props, lighting, camera angle and screen direction—then begin the timestamped action smoothly. If the interface does not permit First Frame and Omni Reference together, remain in Omni Reference mode and use Image 1 plus the fixed setting/portrait references to approximate the preceding final frame. Do not invent a fake exact match. Continuity is a best-effort target, not a guarantee; if constraints conflict, prioritize character identity first, then seating/blocking and camera axis, then wardrobe/props/lighting, then micro-pose matching. Preserve a stable final 0.3–0.5 seconds for the ending cut.

ACTING DIRECTION:
Primary performance: The room falls awkwardly quiet; smiles fade, gazes shift, and no one offers an answer. End on unresolved group tension.
Actors who are not speaking must remain in their established positions and react only as explicitly directed, using restrained eye movement, blinks, breath and micro-expressions; they must not mouth the dialogue or introduce independent gestures.

TIMESTAMPED ACTOR AND DIALOGUE CHOREOGRAPHY:
0.0–0.4s: hold the established composition and eyelines with natural breathing. 0.4–2.7s: perform the shot-specific silent action: The room falls awkwardly quiet; smiles fade, gazes shift, and no one offers an answer. End on unresolved group tension. 2.7–3.0s: resolve the action and hold a stable final pose for the cut. No character speaks and no lip sync is generated. Supporting motion detail: {'start_sec': 0, 'end_sec': 1, 'beat': 'Match the opening tableau; the group absorbs the contradiction and smiles fade.'} {'start_sec': 1, 'end_sec': 2, 'beat': '柳如烟 and the friends exchange uneasy micro-glances while 季伯达 stays composed.'} {'start_sec': 2, 'end_sec': 3, 'beat': 'Begin the very slow pull-back; gestures stop and the room’s social energy drains.'}

CAMERA CHOREOGRAPHY:
Very slow 2% pull-back, echoing the opening while increasing emotional distance. The camera move must remain continuous and subtle for the entire shot, with no reframe, shake, zoom pumping or axis change.

DIALOGUE / AUDIO:
No spoken dialogue; this is a silent visual/card beat.
Perform the exact Mandarin wording once with natural, restrained lip sync by the named speaker only. Do not paraphrase, shorten, expand, repeat, overlap or assign the line to another actor. Keep room tone subdued. Do not render dialogue or any other words on screen; add exact subtitles only in post-production.

FINAL HOLD:
After the dialogue/action resolves, close the speaker’s mouth, settle the gesture, preserve all seats and props, and hold a stable cut-ready composition through the final frame.

NEGATIVE CONSTRAINTS:
No alcohol, wine, beer, champagne, cocktails, liquor bottles, wine bottles, beer bottles, decanters, wine glasses, cocktail glasses, drinking, or toasting; use no beverage props. No new characters, no identity/wardrobe changes, no seat swaps, no duplicated or missing limbs, no warped hands/faces, no lip-sync gibberish, no sudden standing, walking, touching, liquid spill, prop teleportation, background morphing, camera shake, zoom pumping, cuts, transitions, added text, captions, logos, watermarks, or UI.
```

