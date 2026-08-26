# Dreamina production package (32 detailed shots)

- `screenplay-dreamina.md`: 32 Dreamina Omni prompts with timestamped actor choreography.
- `dreamina-omni-prompts.json`: structured prompt manifest.
- `references/characters/`: six character portraits and identity sheet.
- `references/setting/`: KTV continuity/setting sheet.
- `references/staging/`: one composition/staging image per shot.

Each prompt is adapted from the detailed Seedance production prompt. Upload only the references listed for that shot, in the exact order shown.

Every shot includes explicit camera choreography and a boundary decision:

- `BASELINE`: establish the opening composition and continuity anchors.
- `CHAIN`: continuity is required; use the preceding shot’s real final rendered frame as this shot’s First Frame, then execute the specified camera move smoothly.
- `RESET`: an intentional camera/composition change; do not use the preceding final frame. Use this shot’s staging image while preserving character, wardrobe, set, prop, lighting, screen-direction, and axis continuity.

The structured decision, reason, confidence, and optional First Frame path are stored in `transition_from_previous` in `dreamina-omni-prompts.json`.
