# Wan 2.6 R2V production package

Canonical production package for Alibaba Cloud Model Studio `wan2.6-r2v` in the U.S. Virginia region. The canonical 32 source shots are preserved in order and optimized into **21 sequential generation units**. Each unit is at most 6 seconds; 19 of 21 are 4–6 seconds.

## Canonical files

- `screenplay.md`: complete human-readable 21-unit prompts with original-shot mapping and timed beats.
- `wan26-r2v-manifest.json`: 21-unit orchestration manifest.
- `shot-requests/`: exactly 21 canonical Wan request bodies (`shot_001.json`–`shot_021.json`).
- `dialogue-tts-manifest.json`: unit-aligned **fallback-only** external Mandarin TTS handoff.
- `references/`: source staging, character, and KTV continuity assets; original staging filenames remain keyed to the canonical 32 source shots.
- `frames/`: accepted generation-unit final-frame continuity assets.
- `video/`: generated outputs retained for evaluation; drafts are not automatically approved finals.

## Merge map

| Unit | Original shot IDs | Duration | Preserved internal hard cut before | Exact dialogue / beat |
|---|---|---:|---|---|
| 001 | 001 | 3s | 无 | 闺蜜甲：如烟，你输了！ |
| 002 | 002, 003, 004 | 6s | 003, 004 | 闺蜜甲：选真心话还是大冒险？ / 柳如烟：真心话。 / 闺蜜乙：那就说说，你今天穿的内裤是什么颜色？ |
| 003 | 005, 006 | 5s | 无 | 伊藤诚：粉红色。 / 伊藤诚：如烟一直拿我当姐妹。她的内裤，我以前都帮她洗过。 |
| 004 | 007, 008 | 4s | 008 | 柳如烟：你胡说什么呢？ / 闺蜜甲：姐夫，你可别多想。他们从小一起长大。 |
| 005 | 009, 010 | 4s | 无 | 闺蜜乙：就是，伊藤诚在我们眼里根本不算男人。 / 闺蜜丙：他们是纯友谊，关系好才这样。 |
| 006 | 011 | 4s | 无 | 季伯达：小伊，不是我说你。一个大男人，洗什么内裤？ |
| 007 | 012 | 5s | 无 | 季伯达：我的内裤，都是我女闺蜜帮我洗的。你下次也让如烟替你洗。 |
| 008 | 013 | 5s | 无 | 柳如烟：季伯达，你恶不恶心？你怎么能让别的女人给你洗内裤？ |
| 009 | 014, 015 | 5s | 无 | 闺蜜甲：这也太过分了吧？ / 闺蜜乙：你都有女朋友了，怎么一点边界感都没有？ |
| 010 | 016, 017 | 6s | 017 | 季伯达：怎么了？她是我女闺蜜啊。 / 伊藤诚：女闺蜜也不行。男女之间得有分寸。 |
| 011 | 018 | 6s | 无 | 季伯达：奇怪了。刚才你说自己替柳如烟洗过内裤，你们不是也说只是姐妹吗？ |
| 012 | 019, 020 | 4s | 020 | 柳如烟：那不一样。 / 季伯达：哪里不一样？ |
| 013 | 021 | 5s | 无 | 柳如烟：我和伊藤诚只是纯友谊。我拿他当闺蜜，他也拿我当兄弟。 |
| 014 | 022, 023 | 6s | 023 | 伊藤诚：对，我们之间根本没有男女之情。 / 闺蜜甲：他们从小就这样，你一个大男人别这么小气。 |
| 015 | 024, 025 | 6s | 无 | 闺蜜乙：如烟要是真和伊藤诚有什么，还会和你在一起吗？ / 闺蜜丙：情侣之间最重要的是信任。 |
| 016 | 026 | 6s | 无 | 季伯达：所以，伊藤诚可以紧挨着我的女朋友，可以知道她内裤的颜色，还可以替她洗——因为他们是纯友谊。 |
| 017 | 027 | 4s | 无 | 季伯达：但我的女闺蜜替我洗内裤，就是没有分寸？ |
| 018 | 028, 029 | 5s | 029 | 柳如烟：季伯达！你故意的是不是？ / 季伯达：怎么会？ |
| 019 | 030 | 4s | 无 | 季伯达：我只是按照你们的规矩做了一遍。 |
| 020 | 031 | 4s | 无 | 季伯达：怎么轮到你们，规矩就变了？ |
| 021 | 032 | 3s | 无 | 无对白；后期片尾字卡 |

The two short-duration exceptions are deliberate: Unit 001 is the untouched 3-second six-person opening, and Unit 021 is the 3-second silent ensemble/end-card beat. All other units are 4–6 seconds.

## Non-negotiable production rules

- **Unit 001:** opening ensemble contains exactly six people in the established seats. Only 闺蜜甲 says `如烟，你输了！`. `粉红色。` occurs later in Unit 003 (original shot 005), never in Unit 001. Its four media inputs are the literal staging frame, the consolidated 2×3 cast sheet (with every grid position explicitly mapped in the prompt), the KTV continuity sheet, and a close 闺蜜甲 identity reference.
- Dialogue units set `enable_audio: true`. Wan must generate each listed Mandarin line exactly once, in order, from the named visible speaker, synchronized to the in-shot mouth performance. No paraphrase, repeats, overlap, narration, translation, off-screen voice, or invented speech.
- Every dialogue beat carries an explicit `SPEAKER` and `TARGET / ADDRESSEE` lock in the request prompt and a `target` field in the manifest. The visible speaker looks toward the target when composition permits and is the only character allowed to articulate during that timed window; the target reacts silently, and any character with a later line stays silent until its own window. Voice and lip motion must never transfer to the addressee, nearest face, another character, or an off-screen source, and simultaneous talking mouths are forbidden.
- Unit 021 is non-dialogue and sets `enable_audio: false`; no one speaks or mouths words. Its exact end-card text is added visually in post-production.
- External TTS is fallback-only after a native audio render fails exact-wording, speaker, or synchronization QC. It replaces the failed native dialogue and is never layered over a passing native track.
- Every request uses model `wan2.6-r2v`, resolution `720P`, duration ≤6 seconds, and no more than four media inputs.
- No alcohol, bottles, drinks, beverages, cups, drinking glasses, or beverage props may appear anywhere. The low table remains limited to cards and small snack plates.
- Internal hard cuts listed above preserve required speaker/camera/staging changes. Boundaries marked `CONTINUE` in prompts are intentionally merged compatible staging.
- Runtime replaces `{{asset_base_url}}` with accessible URLs or Base64 data URIs and `{{previous_shot_last_frame_url}}` with the preceding accepted generation unit's extracted final frame. Model, API key, and endpoint must belong to the same region. U.S. Virginia API base: `https://dashscope-us.aliyuncs.com/api/v1`.
