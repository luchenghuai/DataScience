# Wan 2.6 R2V production package

Canonical thirty-two-shot production package for Alibaba Cloud Model Studio `wan2.6-r2v` in the U.S. Virginia region.

## Canonical files

- `screenplay.md`: human-readable 32-shot production prompts.
- `wan26-r2v-manifest.json`: orchestration manifest with runtime continuity placeholders.
- `shot-requests/`: 32 canonical Wan 2.6 API request bodies.
- `dialogue-tts-manifest.json`: exact Mandarin dialogue handoff.
- `references/`: self-contained staging, character, and KTV continuity assets.
- `frames/`: accepted final-frame continuity assets.
- `video/`: generated outputs retained for evaluation; generated drafts are not automatically approved finals.

Shot 001 is the 3-second opening ensemble shot. 闺蜜甲 says the exact line `如烟，你输了！`. The later line `粉红色。` is not Shot 001.

Every prompt contains an explicit `START-FRAME CHARACTER LOCATIONS` block that locks each visible named character to a screen position, depth plane, seat, and facing direction before motion begins. Each request uses at most four media inputs. Shot 001 uses its staging first frame, KTV continuity sheet, speaker identity, and principal reactor identity. Shots 002–032 use the preceding rendered final frame, shot staging, KTV continuity sheet, and speaker identity.

Runtime must replace `{{asset_base_url}}` with accessible URLs or Base64 data URIs and `{{previous_shot_last_frame_url}}` with the preceding accepted shot's extracted final frame. Model, API key, and endpoint must belong to the same region. U.S. Virginia API base: `https://dashscope-us.aliyuncs.com/api/v1`.
