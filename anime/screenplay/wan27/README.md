# Wan 2.7 R2V production package

Generated from the 32-shot Dreamina package for Alibaba Cloud Model Studio Wan 2.7 reference-to-video.

- `screenplay-wan27.md`: human-readable 32-shot production prompts.
- `wan27-r2v-manifest.json`: orchestration manifest with runtime continuity placeholders.
- `shot-requests/`: 32 API request bodies.
- `references/`: self-contained staging, character, and KTV assets.

Runtime must replace `{{asset_base_url}}` with publicly accessible URLs (or convert local files to supported Base64 data URIs) and `{{previous_shot_last_frame_url}}` with the preceding generated shot's extracted final frame.
