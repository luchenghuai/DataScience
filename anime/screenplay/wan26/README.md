# Wan 2.6 R2V production package

Canonical source-faithful 26-unit production package for Alibaba Cloud Model Studio `wan2.6-r2v` in the U.S. Virginia region.

## Canonical files

- `screenplay.md`: 26 generation units rebuilt from `anime/screenshotwithdesc/complete-script.md`.
- `wan26-r2v-manifest.json`: orchestration manifest for all 26 units.
- `shot-requests/`: canonical Wan 2.6 request bodies using 4–6 second units.
- `dialogue-tts-manifest.json`: exact Mandarin dialogue for external TTS.
- `references/`: character, setting, continuity, and staging assets used by this package.
- `frames/`: generated final-frame continuity assets; create during sequential production.
- `video/`: generated video outputs; create during production.

Source-document timestamps are intentionally ignored. Production timestamps are newly designed and cumulative. Each unit begins from its own staging image; the previous accepted unit's final frame is a continuity and axis reference, not the literal opening frame. Generate units sequentially and approve each before extracting its final frame for the following unit.

Every request uses at most four media inputs. Wan generation is silent (`enable_audio: false`). Generate exact Mandarin dialogue separately with controlled TTS, then apply optional lip-sync and final ambience/music mixing.

Runtime must replace `{{asset_base_url}}` with accessible URLs or Base64 data URIs and `{{previous_shot_last_frame_url}}` with the preceding accepted unit's extracted final frame. Model, API key, and endpoint must belong to the same region. U.S. Virginia API base: `https://dashscope-us.aliyuncs.com/api/v1`.

The superseded 32-shot package and its generated Shots 001–003 are archived outside this repository at `~/src_code/backup/DataScience-anime-wan27-32shot-20260825/`.
