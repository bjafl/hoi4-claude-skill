---
name: hoi4-companion
description: "Always use this skill for any Hearts of Iron IV (HOI4) gameplay question, even simple-sounding ones — HOI4 numbers change every patch, so this skill looks up curated, version-tagged wiki data instead of answering from memory. Trigger for: focus-tree or build-order picks (\"what to rush as Germany\", \"no idea what focuses to pick\"); division templates and combat width (\"40w template\"); why a land, air, or naval battle was lost (screening ratios, org, breakthrough vs defense); which DLC unlocks a feature like the ship or tank designer; exact numbers for political power, stability, war support, supply hub range, autonomy, or manpower; equipment/tech stats; national spirits; peace conferences; achievements. A country name, focus, division, ship, or battle is enough signal even without the word \"HOI4\". Skip for Steam pricing, other Paradox/strategy games, real WWII history, fan fiction, or non-gameplay issues (crashes, installs, mods, performance)."
---

# HOI4 Companion

## Overview

Hearts of Iron IV changes frequently (patches, DLC, focus tree rewrites), so
answers from memory alone go stale. This skill pairs general HOI4 knowledge
with a curated snapshot of wiki data under `references/`, so lookups are
grounded in an explicit, versioned source instead of guessed from training
data.

## When to Use

- Questions about a specific country's focus tree, national spirits, or
  starting situation
- Equipment/technology stats and research lines (infantry gear, tanks,
  aircraft, naval hulls, etc.)
- Division template design and combat width questions
- Core game mechanics: stability, war support, supply, army/navy/air
  experience, political power, autonomy levels, peace conferences
- Achievement conditions and how to get them
- General strategy questions where citing the specific mechanic matters

## How Reference Data Is Organized

`references/` is split by topic so only the relevant file needs to be read
for a given question — keep this skill file itself short, and let Claude
pull in a specific reference file on demand instead of loading everything
up front. Only this file's frontmatter (name + description) sits in context
by default; the body below loads when the skill triggers; everything under
`references/` loads only when a specific file is actually read for a
specific question — so the directory can hold hundreds of files without
costing anything until one of them is relevant.

The directory names mirror the build corpus this skill is sourced from
(`wiki-crawler/corpus/` at the repo root — see its `LEDGER.md` for
build status and `_tooling/STYLE.md` for the authoring rules every file
here follows) so content can be synced over without renaming:

| Directory | Contents |
|---|---|
| `references/00-meta/` | Game overview, DLC list, patch-history timeline, glossary |
| `references/01-mechanics/` | Core systems: politics, economy, research, supply, espionage, manpower, nukes, laws/spirits, etc. |
| `references/02-land-warfare/` | Divisions, combat, tactics, land doctrine, tank designer, unit stats |
| `references/03-air-warfare/` | Air missions, air combat, aircraft designer, air doctrine |
| `references/04-naval-warfare/` | Fleets, naval combat, ship designer, naval doctrine |
| `references/05-countries/` | Starting stats, ideology, spirits, unique mechanics, neighbours. One file per country that has its own focus tree; countries using the generic tree are grouped regionally (`minor-europe.md`, `minor-middle-east-africa.md`, `minor-americas.md`, `minor-asia-and-china-warlords.md`, `other-formable-releasable-entities.md`) — grep the directory for a specific minor country/entity |
| `references/06-focus-trees/` | Full national focus tree breakdowns (name → prereqs → mutually exclusive → effects → typical path) |
| `references/07-achievements/` | Achievement list + per-DLC-group strategy notes (not one file per achievement — see condensing rule below) |
| `references/08-strategy/` | Build orders, doctrine-choice guidance, meta by era — much of this is `**Inferred:**`, not scraped |
| `references/09-reference/` | Modifier lists, states, commanders, MIOs, scientists, console commands, hotkeys |

Each reference file should note the **game version / patch** and **DLC**
it reflects, and the wiki page(s) it was sourced from, so stale data is
easy to spot and re-scraped later.

### Keep reference files lean

A file that gets *read* costs context, even though the directory listing it
lives in doesn't. When condensing corpus content into a reference file here:
- Prefer one file per natural group (e.g. one file per DLC's achievements)
  over one file per individual item, unless that item genuinely needs its
  own page (a major country's 100+ focus tree does; a 3-step achievement
  usually doesn't).
- For anything with a shared generic version (e.g. most minor countries'
  focus trees are close to the generic tree already covered in
  `01-mechanics/national-focus.md`), reference the shared file and only
  document the deltas, rather than re-writing the whole thing per country.
- Depth is fine — a 100+ KB focus-tree file is a reasonable size for a
  reference that's read once when relevant. Breadth-for-its-own-sake
  (writing a full page for something with nothing distinct to say) is
  the thing to avoid.

## Workflow

1. Identify which topic the question falls under (see table above).
2. Check whether a relevant file already exists in `references/`.
3. If it exists, read it and answer from that data — cite the version/patch
   noted in the file.
4. If it doesn't exist yet, say so explicitly rather than answering from
   possibly-outdated memory, and suggest the topic for the next wiki-data
   pass.

## Status

Complete. All 10 categories copied over from `wiki-crawler/corpus/` (191 files, ~6.9 MB) —
see that directory's `LEDGER.md` for build history and known data-quality notes, and
`INDEX.md` there for the same "question about X → read file Y" routing table.
`05-countries/` was restructured on 2026-08-23 (117 → 58 files, minor countries merged into 5
regional files) to keep `hoi4-companion.skill` under claude.ai's 200-file zip cap — see
`LEDGER.md`'s "packaging restructure" entry.
