# Hearts of Iron IV — Agent Knowledge Base

Markdown corpus scraped and distilled from `hoi4.paradoxwikis.com`, formatted for retrieval by an
LLM agent. Game version 1.19 unless a file's front matter says otherwise.

**Build complete.** 191 content files, 6.9 MB. See `LEDGER.md` for how it was built, what got
condensed and why, and known data-quality issues. See `INDEX.md` for routing hints — "question
about X → read file Y".

## Layout

```
00-meta/          game overview, DLC index, patch history, console commands, hotkeys, jargon, UI   6 files
01-mechanics/     politics, economy, research, supply, espionage, laws/spirits, ...                17 files
02-land-warfare/  divisions, combat, tactics, land doctrine, tank designer, unit stats              12 files
03-air-warfare/   missions, air combat, aircraft designer, air doctrine                              5 files
04-naval-warfare/ fleets, naval combat, ship designer, naval doctrine                                 6 files
05-countries/     one profile per country with its own focus tree + 5 regional group files          58 files
06-focus-trees/   one file per national focus tree, joint/shared branches, Chinese warlords shared  54 files
07-achievements/  per-DLC-group achievement files + index                                            18 files
08-strategy/      build orders, doctrine choice, meta by domain, common mistakes — mostly synthesis  10 files
09-reference/     modifier list, state list, commander/ace/MIO rosters                                5 files
_tooling/         fetch snippet, style guide, manifest, raw master-page snapshots
```

`05-countries/` was originally 117 one-file-per-country profiles; countries without a dedicated
focus tree (generic tree only) were merged into 5 regional files (`minor-europe.md`,
`minor-middle-east-africa.md`, `minor-americas.md`, `minor-asia-and-china-warlords.md`,
`other-formable-releasable-entities.md`) on 2026-08-23 so the packaged `.skill` zip stays under
claude.ai's 200-file cap. Pure concatenation, no content rewritten — see `LEDGER.md`.

This directory is a **build/staging corpus**, not the shipped product. Finished, condensed content
gets copied into `../.claude/skills/hoi4-companion/references/<same category name>/` — see that
skill's `SKILL.md` for the "Keep reference files lean" condensing principle every file here follows,
and don't hand-edit a copy in `references/` to fix a content issue; fix it here and re-copy.

## File contract

Every content file opens with YAML front matter:

```yaml
---
title: Supply and Logistics
category: mechanics
tags: [supply, logistics, railways, trucks, ports, attrition]
game_version: "1.19"
dlc: [No Step Back]
sources:
  - https://hoi4.paradoxwikis.com/Logistics
---
```

- `dlc: []` means base game. A non-empty list means the content described needs that DLC.
- `tags` are the intended retrieval keys.
- `sources` lets the agent cite or re-verify.

Body starts at `##`. Numeric tables are preserved as-is from the wiki; prose is rewritten and
compressed. Uncertain or contradictory wiki data is marked with `> ⚠️` (98 files, 303 flags —
searchable, not silently resolved). Advice that is not on the wiki is labelled `**Inferred:**`
(mainly `08-strategy/`). Data the wiki simply lacks is marked `_Not covered on the wiki._`

## Known data quality notes

Patch 1.17 reworked land, air, and naval doctrine — they are no longer research trees but Officer
Corps purchases with Mastery progression. Any older guide contradicting `02-land-warfare/land-doctrine.md`,
`03-air-warfare/air-doctrine.md`, or `04-naval-warfare/naval-doctrine.md` is stale. Other
contradictions (both readings recorded, primary source noted) are catalogued in `LEDGER.md`.

`00-meta/patch-history.md` is explicitly best-effort — the wiki's full 39-page patch-by-patch
history was out of scope for this pass. Several `09-reference/` lists that would have duplicated
content already covered elsewhere (Factions, scientists, operations/intelligence agencies) were
skipped rather than re-fetched — see `LEDGER.md` for what was dropped and why.

## Attribution

Content derived from the Hearts of Iron 4 Wiki (paradoxwikis.com), which publishes under
Attribution-ShareAlike. Game data is factual; prose has been rewritten. Retain attribution if you
redistribute.
