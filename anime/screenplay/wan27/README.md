# Wan 2.6 R2V production package

Thirty-two-shot production package for Alibaba Cloud Model Studio `wan2.6-r2v` in the U.S. Virginia region.

- `screenplay-wan27.md`: human-readable 32-shot production prompts (directory/name retained for compatibility).
- `wan27-r2v-manifest.json`: orchestration manifest with runtime continuity placeholders.
- `shot-requests/`: 32 Wan 2.6 API request bodies.
- `dialogue-tts-manifest.json`: exact Mandarin post-production dialogue handoff.
- `references/`: self-contained staging, character, and KTV continuity assets.

Every prompt contains an explicit `START-FRAME CHARACTER LOCATIONS` block that locks each visible named character to a screen position, depth plane, seat, and facing direction before motion begins. Each request uses at most four media inputs. Shot 001 uses its staging first frame, KTV continuity sheet, speaker identity, and principal reactor identity. Shots 002–032 use the preceding rendered final frame, shot staging, KTV continuity sheet, and speaker identity.

Wan video generation is silent (`enable_audio: false`). Generate exact Mandarin dialogue separately with controlled TTS, then apply optional lip-sync and final ambience/music mixing.

Runtime must replace `{{asset_base_url}}` with accessible URLs or Base64 data URIs and `{{previous_shot_last_frame_url}}` with the preceding generated shot's extracted final frame. Model, API key, and endpoint must belong to the same region. U.S. Virginia API base: `https://dashscope-us.aliyuncs.com/api/v1`.
