# HOI4 Knowledge Base — Build Ledger

**Status as of this snapshot:** 250 content files, 7.0 MB — all planned categories complete
(00-meta through 09-reference). Remaining work is the Finishing pass only (see below).
Source: `hoi4.paradoxwikis.com` (game version 1.19 unless a file's front matter says otherwise).

---

## How this is being built

Pages are pulled from the wiki's MediaWiki API through a browser tab, rendered HTML is converted
to markdown by a colspan/rowspan-aware converter, and a writer agent distills each page set into a
topic file. Tooling and rules live in `_tooling/`:

| File | Purpose |
|---|---|
| `_tooling/FETCH-HOWTO.md` | The extraction snippet + how to run it. Reusable for any Paradox wiki. |
| `_tooling/STYLE.md` | Front-matter schema, authoring rules, manifest convention. |
| `_tooling/manifest.tsv` | `relpath ⇥ title ⇥ bytes ⇥ source wiki pages` — appended by each writer. |

Every file carries YAML front matter with `title`, `category`, `tags`, `game_version`, `dlc`,
and `sources` (wiki URLs), so a plugin can route queries on metadata alone.

---

## ✅ Done

### `01-mechanics/` — 17 files, 739 KB

| File | KB | Covers |
|---|---|---|
| `politics-ideology-government.md` | 134 | Ideologies & sub-ideologies, party popularity, elections, coups, PP economy, full 828-row country-leader-trait table |
| `laws-and-advisors.md` | 74 | Every law with exact modifiers/PP cost/requirements, advisor slots, high command, theorists, design companies, national spirits |
| `national-focus.md` | 19 | Focus duration/cost, prerequisites & mutual exclusion, generic tree, joint/shared trees, all continuous focuses |
| `internal-factions-and-balance-of-power.md` | 23 | Which countries use which system, influence gain/loss, BoP scales |
| `civil-war-and-occupation.md` | 33 | Civil-war split rules, occupation laws with resistance/compliance numbers, garrisons, autonomy ladders, exile |
| `diplomacy-factions-and-war.md` | 46 | Guarantees, NAPs, faction rules, world-tension thresholds, justification cost/time, war score, peace-conference bidding |
| `research-and-technology.md` | 36 | Research slots per country, speed modifiers, ahead-of-time penalty, full engineering + industry trees |
| `production-and-equipment.md` | 38 | Factory output, efficiency base/cap/growth, retention, licensed production, variants, conversion, lend-lease |
| `construction-and-buildings.md` | 25 | Every building: cost, slots, effects, caps, bombing vulnerability, repair, landmarks |
| `trade-resources-and-market.md` | 20 | All seven resources, trade laws, convoy cost, international market, fuel |
| `military-industrial-organizations.md` | 12 | MIO funds, size, traits, policies, task capacity (AAT) |
| `special-projects-and-scientists.md` | 61 | Facilities, prototypes, all four project + outcome tables, scientist traits, full scientist list (GD) |
| `supply-and-logistics.md` | 22 | Supply hubs, railways, trucks, supply grades, ports, naval/air supply, consumption |
| `manpower-and-experience.md` | 33 | Conscription fractions, non-core manpower, all XP sources/sinks, unit XP levels, attrition & accidents |
| `officer-corps-and-commanders.md` | 62 | Army/navy/air spirits with costs, command power, commander skills & full trait table, unit limits, battle-plan bonus (NSB) |
| `espionage-and-operations.md` | 58 | Agency upgrades, operative traits, every operation with cost/time/effect, intel levels, decryption, collaboration (LaR) |
| `nuclear-missiles-and-raids.md` | 24 | Reactor/bomb rates, drop effects, rocket & missile tech, every raid type |

### `02-land-warfare/` — 12 files, 368 KB

| File | KB | Covers |
|---|---|---|
| `land-warfare-overview.md` | 20 | Theaters, command groups & caps, strategic redeployment, naval transport, invasion caps, border wars |
| `division-designer.md` | 23 | Template rules, XP cost table, armor/piercing/hardness formulas, understrength scaling, 20w vs 40w theory |
| `land-units-and-stats.md` | 67 | Every battalion & support company, full base stats per tech year, equipment needs, costs |
| `land-combat.md` | 25 | Combat width & terrain frontage, reinforcement, damage rolls, entrenchment, encirclement, weather/night/river/fort |
| `combat-tactics.md` | 14 | All six phases, every tactic with trigger/weight/counter/modifiers, initiative & preferred tactics |
| `historical-divisions.md` | 21 | Eleven historical templates with stat blocks + doctrine sample divisions |
| `land-doctrine.md` | 37 | **Post-1.17 system**: 4 Grand Doctrines, 27 subdoctrines, all Mastery milestones, playstyle comparison |
| `special-forces-doctrine.md` | 22 | SF cap formula, SFBS country table, 2 Grand Doctrines, 8 subdoctrines |
| `tank-designer.md` | 33 | All chassis & modules with stats/costs, Land Cruiser, designer companies, 9 worked builds (NSB) |
| `armor-technology.md` | 27 | Both NSB chassis tree and legacy pre-NSB tree |
| `infantry-and-support-technology.md` | 35 | Infantry weapons, motorized/mechanized, amtracs, armored cars, special forces, all support-company lines, secret techs |
| `artillery-technology.md` | 14 | Artillery, AA, AT, rocket artillery + equipment stats + tank-gun lookup |

### `03-air-warfare/` — 5 files, 144 KB

| File | KB | Covers |
|---|---|---|
| `air-warfare-overview.md` | 24 | Air bases & capacity, wings, mission efficiency, air-superiority formula, all 15 mission types, aces |
| `air-combat.md` | 17 | Three-phase resolution with every formula, stat roles, losses, AA interaction, carrier air |
| `aircraft-designer.md` | 34 | All airframes, engines, weapon/special/electronics modules, designer traits, 4 worked builds (BBA) |
| `air-technology.md` | 29 | BBA airframe tree + full legacy tree with plane stat tables |
| `air-doctrine.md` | 28 | **Post-1.17 system**: 3 Grand Doctrines, 25 subdoctrines, all Mastery milestones, branch-selection guide |

### `04-naval-warfare/` — 6 files, 124 KB

| File | KB | Covers |
|---|---|---|
| `naval-warfare-overview.md` | 12 | Task force/fleet/theater hierarchy, all 9 naval missions, London Naval Treaty limits |
| `naval-combat.md` | 18 | Screening, target selection, submarine reveal, hit/damage formulas, naval strikes, carrier sortie mechanics |
| `ship-designer.md` | 27 | All hull types, modules, worked builds (MtG modular system) |
| `naval-technology.md` | 23 | Both MtG modular tree and legacy fixed-model tree |
| `naval-support-technology.md` | 11 | Batteries, torpedoes, damage control, fire control, transports, mine warfare |
| `naval-doctrine.md` | 26 | **Post-1.17 system**: 3 Grand Doctrines, 4 doctrine tracks, all Mastery milestones |

Built via the Playwright-driven fetch pipeline (`wiki-crawler/fetcher/`, replacing the interactive
claude-in-chrome tab) as 6 parallel Haiku writer agents — first large-scale test of that combo;
quality held up (spot-checked, tables intact, doctrine-system self-correction worked as intended).

### `05-countries/` — 99 files, ~1.1 MB

One profile per 1936-start country: 1936 stats (states/research slots/population/factories/
resources/victory points from the `Countries` master table), government/political situation,
national spirits, unique mechanics, neighbours/diplomatic position. Does not attempt focus trees
(separate, pending `06-focus-trees/`).

Built via 5 parallel Playwright+Haiku Workflow runs (99 agents total). All 99 succeeded on the
first pass, 0 missing source pages. One harmless issue found and fixed: 14 files had their
manifest line double-appended (byte-identical duplicates, not conflicting writes) — deduped.

Formable nations (6), releasable countries (6), and the princely-states/regional group pages are
NOT yet done — exact wiki page titles still need to be looked up (see item 1 below, now scoped
down to just this remainder).

---

### `05-countries/` remainder — 18 files, ~1.1 MB combined with the base 99
Formable nations (6 regions), releasable countries (6 regions), Indian/Indonesian Princely States,
Amerindian Nations, Horn of Africa nations, Reichskommissariats, releasable political parties —
built as 18 parallel Haiku agents, all succeeded (one retry round after a mid-run session-limit
pause, cached results replayed instantly on resume). `05-countries/` total: **117 files**.

### `05-countries/` — packaging restructure, 117 → 58 files (2026-08-23)

claude.ai rejects `.skill` uploads with more than 200 files in the zip; the packaged skill (see
`skill/hoi4-companion.skill`) hit 252. `05-countries/` was the biggest contributor at 117 files,
65 of which are minor countries with no dedicated `06-focus-trees/` page (generic tree only) —
individually 3-10 KB each.

Merged those 65 minus the already-regional group files, plus the pre-existing
`formable-nations-<region>.md` (6), `releasable-countries-<region>.md` (6), and
`indian-/indonesian-princely-states.md` (2), into 5 regional files: `minor-europe.md`,
`minor-middle-east-africa.md`, `minor-americas.md`, `minor-asia-and-china-warlords.md`,
`other-formable-releasable-entities.md`. 64 source files → 5, each country/entity kept as its own
`##` section (original `##` headings demoted to `###`+ so they nest correctly). Pure
concatenation via a one-off script — no content rewritten, no facts touched.
`releasable-political-parties-and-leaders.md` (132 KB) was left standalone; it's already a single
coherent topic. Countries with a dedicated focus tree (Germany, USSR, majors, etc.) were not
touched. `05-countries/` total: **58 files**. Corpus total: 250 → 191 content files. Both
`wiki-crawler/corpus/_tooling/manifest.tsv` and `skill/hoi4-companion/references/05-countries/`
were updated to match; see `skill/hoi4-companion/SKILL.md` for the updated routing note.

### `06-focus-trees/` — 54 files, ~3 MB
Condensed from the raw 88-page category listing: base-game variants and sub-branch pages folded
into their country's single file (Germany's 3 source pages → 1 file), 15 minor Chinese warlord
factions' 4 generic-tree pages → 1 shared `china-warlords.md` (their `05-countries/` profiles link
here instead of repeating it), 13 joint/shared cross-country branch pages → 1
`shared-and-joint-branches.md`. Every file cross-links to its matching `05-countries/` profile.
Built as 4 parallel workflow runs (54 agents total, 2 retry rounds after session-limit pauses).

### `07-achievements/` — 18 files
The master `Achievements` page (fetched once, saved to `_tooling/achievements-master-raw.md`) was
already organized by DLC with a `## <DLC name>` heading per group and a name/condition table under
each — matched the condensing plan exactly, no restructuring needed. 17 DLC-group files + one
`_index.md` lookup table. Selective-fetch worked as intended: writers pulled individual achievement
pages only when the master table's condition text was too terse, not for all ~100.

### `08-strategy/` — 10 files
Opening build orders, division-template meta, doctrine-choice guide, air/naval strategy meta,
economy/factory ratios, common mistakes, MP vs SP differences, beginner's guide, difficulty
settings. Mostly synthesis across the already-written `01-mechanics/02-land-warfare/03-air-warfare/
04-naval-warfare` files, labelled `**Inferred:**` throughout per the style rules rather than cited
to a specific wiki page.

### `00-meta/` (6 files) + `09-reference/` (5 files) — condensed down from an original ~25-file estimate
Redundancy check against already-written categories cut three originally-planned reference lists
that turned out to already be fully covered elsewhere, so they were dropped rather than re-fetched
as duplicates: ~~List of Factions~~ (in `01-mechanics/diplomacy-factions-and-war.md`),
~~List of scientists~~ (in `01-mechanics/special-projects-and-scientists.md`, 319-row table),
~~List of operations/operatives/intelligence agencies~~ (in `01-mechanics/espionage-and-operations.md`).
`00-meta/dlc-overview.md` condenses all 17 DLC pages into one file (name/date/headline features +
pointer to where the deep mechanics already live in the corpus) instead of 15 separate deep-dives
that would have mostly duplicated content already written. `00-meta/patch-history.md` is explicit
best-effort only — the full 39-page patch-by-patch history was out of scope (low value for a
gameplay companion), gaps are noted rather than forced. Also built: `console-commands.md`,
`hotkeys.md`, `jargon.md`, `user-interface.md`, and `09-reference/`'s `list-of-modifiers.md`,
`list-of-states.md`, `list-of-commanders.md` (6 leadership-roster pages folded together, links to
`01-mechanics/officer-corps-and-commanders.md` for trait definitions rather than repeating them),
`list-of-aces.md`, `list-of-mios.md`.

Explicitly deferred, not forgotten: the ~24 country-specific decision pages originally estimated for
this category substantially overlap with each country's own "Unique mechanics" section in
`05-countries/` — skipped for this pass, revisit only if the eval pass below finds a real gap.

---

## ⏳ Remaining

Finishing pass, in progress:
- [x] `README.md` + `INDEX.md` with routing hints ("query about X → read file Y").
- [x] Cross-link repair: scanned all 374 relative `.md` links corpus-wide. Found and fixed 16 broken
      targets (typos, wrong relative-path prefixes, one dangling reference to a page that was folded
      into another file) plus 52 stale `06-focus-trees/ (pending)` placeholders left over from when
      `05-countries/` was written before `06-focus-trees/` existed — repointed each to its matching
      focus-tree file, or to `china-warlords.md` / `01-mechanics/national-focus.md` for the minor
      factions and generic-tree-only countries that don't have their own focus-tree file. 0 broken
      links remain.
- [x] Consistency check on the ⚠️ contradictions: spot-verified the flagging discipline held —
      98 files carry 303 `⚠️` flags corpus-wide, both-readings-recorded pattern confirmed intact
      (e.g. the guarantee-cost contradiction in `diplomacy-factions-and-war.md`).
- [ ] Condensing pass: the redundancy checks already done during the build (dropped 3 duplicate
      reference-list categories, folded warlord/joint-branch focus trees) cover the major cases;
      no further pass planned unless the eval pass below surfaces a specific gap.
- [ ] Copy each finished category into `.claude/skills/hoi4-companion/references/<category>/`.
- [ ] Eval pass on the assembled skill (test cases + description-triggering check via the
      `skill-creator` skill) — confirms the skill actually answers real questions well, not just
      that the corpus is complete.
- [ ] Package as a `.skill` file for claude.ai upload (`skill-creator`'s `scripts.package_skill`).

---

## ⚠️ Issues found so far (carried into the files as inline notes)

**Mechanics changed since much of the wiki was written**
- **Land and air doctrine were reworked in patch 1.17.** The old research-tree doctrines are gone;
  doctrines are now bought from the Officer Corps with Army/Air XP and progressed via *Mastery*.
  Both doctrine files document the current system and explicitly warn that older guides are stale.
- The wiki now lists **seven** strategic resources — coal was added as a factory-powering resource.

**Wiki self-contradictions (both readings recorded, primary source noted)**
- Guarantee cost: 15 PP (`Diplomacy`) vs 25 PP (`Government`).
- War-goal justification: 50 PP + 10/state (`Government`) vs 200 PP + 50/state (`War goal`).
- PP gain from stability: two different ranges on the same page.
- Communist puppeting discount: 35% / 10% / −10% across three pages.
- Regiment size: 5 battalions flat (`Division`) vs 4 raised to 5 by doctrine (`Division designer`).
- Mechanized hard attack: +500% (prose) vs +400% (table).
- Armored support-company combat width: +2.0 vs 3/1 across two pages.
- Aircraft modules: 4× HMG weight/cost and Large Armor Plates weight differ between the designer
  page and the tech page.
- Air experience per plane: 0.0004 in prose vs 0.001 in the page's own worked example.

**Broken wiki templates (reconstructed and flagged, not guessed)**
- `Research` research-slot table has unresolved `Template:Focus` calls for CHI/CZE/AST/MAN.
- `Military industrial organization` renders four XP costs as `0` via failed define lookups.
- Several secret-tech cells leak raw script (`military_police = { max_strength = 5`).

**Genuinely missing from the wiki (marked `_Not covered on the wiki._`)**
- Focus-speed modifiers — no page documents them.
- Aircraft thrust-to-weight → max-speed formula.
- Doctrine XP costs on the `Research` page.
- Completion effects for Escort Carrier, Submarine Carrier, Support Ships (NCNS) and
  Large Caliber Kinetic Energy Sabot (PfOT) special projects.
- Internal-faction DLC mapping; Poland's and the Baltic states' faction descriptions.

**Extractor caveats**
- `<caption>` elements are dropped by the converter — tables whose only label is a caption come out
  unlabelled and need a second pass (already handled for the doctrine sample-division tables).
- JS "tabber" sections render empty and need a raw-text pass (already handled for artillery
  equipment).
- `browser_batch` intermittently reports "failed in the extension"; re-issuing the two actions
  separately always recovers.
