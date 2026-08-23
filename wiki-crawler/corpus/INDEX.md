# Routing Index

"A question about X → read file Y." Use this before grepping blind. Full per-file byte sizes and
exact source pages are in `_tooling/manifest.tsv`; this file is for topic routing, not inventory.

## Countries, focus trees, achievements — routing is the filename

These three categories are flat and large; there's no per-file table below, just the naming rule:

- **`05-countries/<common-name>.md`** — one file per 1936-start country (`germany.md`,
  `soviet-union.md`, `united-kingdom.md`, `nationalist-spain.md`-style names). Covers 1936 starting
  stats, government, national spirits, unique mechanics, neighbours. Plus non-country-named group
  files: `formable-nations-<region>.md`, `releasable-countries-<region>.md`,
  `indian-princely-states.md`, `indonesian-princely-states.md`, `amerindian-nations.md`,
  `horn-of-africa-nations.md`, `reichskommissariats.md`, `releasable-political-parties-and-leaders.md`.
- **`06-focus-trees/<common-name>.md`** — same naming as `05-countries/`, one file per nation's
  focus tree (cross-links back to the matching `05-countries/` profile). Exceptions:
  `china-warlords.md` (shared by the ~12 minor Chinese warlord factions — their own country files
  link here instead of repeating it) and `shared-and-joint-branches.md` (ABDACOM, Austro-Hungarian,
  Baltic, Congo, Indonesia, Liangguang, Ma Clique, Nordic, Paraguay/Uruguay, Saadabad, Trial of
  Allegiance — cross-country branches unlockable by specific groups together).
- **`07-achievements/<dlc-name>.md`** — one file per DLC group (`base-game.md`,
  `man-the-guns.md`, `no-step-back.md`, etc.) plus `_index.md` for a flat name→condition lookup
  table across all of them.

## `01-mechanics/`

| Question about... | Read |
|---|---|
| Ideologies, party popularity, elections, coups, political power economy, country-leader traits | `politics-ideology-government.md` |
| Laws, advisors, high command, national spirits (generic) | `laws-and-advisors.md` |
| Focus duration/cost/prerequisites, the generic tree, continuous focuses | `national-focus.md` |
| Internal factions / balance of power systems | `internal-factions-and-balance-of-power.md` |
| Civil war, occupation laws, resistance/compliance, puppets, exile | `civil-war-and-occupation.md` |
| Guarantees, NAPs, factions, world tension, war goals, peace conferences | `diplomacy-factions-and-war.md` |
| Research slots, speed modifiers, engineering/industry tech trees | `research-and-technology.md` |
| Factory output, efficiency, licensed production, lend-lease | `production-and-equipment.md` |
| Buildings: cost, slots, effects, bombing vulnerability | `construction-and-buildings.md` |
| Resources, trade laws, convoys, fuel | `trade-resources-and-market.md` |
| Military Industrial Organizations (mechanic, not roster) | `military-industrial-organizations.md` |
| Special projects, nuclear/rocket research, scientists (full roster) | `special-projects-and-scientists.md` |
| Supply hubs, railways, trucks, terrain/weather tables | `supply-and-logistics.md` |
| Manpower, conscription, XP sources, attrition & accidents | `manpower-and-experience.md` |
| Officer Corps, command power, commander traits (mechanic, not roster) | `officer-corps-and-commanders.md` |
| Intel, spy agencies, operatives, operations | `espionage-and-operations.md` |
| Nukes, missiles, raids | `nuclear-missiles-and-raids.md` |

## `02-land-warfare/`

| Question about... | Read |
|---|---|
| Theaters, command groups, strategic redeployment, invasion caps | `land-warfare-overview.md` |
| Division template rules, XP costs, armor/piercing formulas | `division-designer.md` |
| Battalion/support-company base stats by tech year | `land-units-and-stats.md` |
| Combat width, damage rolls, entrenchment, terrain/weather combat effects | `land-combat.md` |
| Combat tactics (all six phases, triggers/counters) | `combat-tactics.md` |
| Historical division templates, doctrine sample divisions | `historical-divisions.md` |
| Land doctrine (post-1.17 Mastery system) | `land-doctrine.md` |
| Special forces doctrine | `special-forces-doctrine.md` |
| Tank designer, worked builds | `tank-designer.md` |
| Armor technology tree (both NSB and legacy) | `armor-technology.md` |
| Infantry/motorized/mechanized/support-company tech | `infantry-and-support-technology.md` |
| Artillery, AA, AT, rocket artillery | `artillery-technology.md` |

## `03-air-warfare/`

| Question about... | Read |
|---|---|
| Air bases, wings, mission efficiency, air superiority, mission types | `air-warfare-overview.md` |
| Air combat resolution, losses, AA interaction | `air-combat.md` |
| Aircraft designer, worked builds | `aircraft-designer.md` |
| Air technology tree (BBA and legacy) | `air-technology.md` |
| Air doctrine (post-1.17 Mastery system) | `air-doctrine.md` |

## `04-naval-warfare/`

| Question about... | Read |
|---|---|
| Task forces, fleets, theaters, all 9 naval missions, London Naval Treaty | `naval-warfare-overview.md` |
| Screening, target selection, hit/damage formulas, naval strikes, carriers | `naval-combat.md` |
| Ship designer, hull types, modules, worked builds | `ship-designer.md` |
| Naval technology tree (MtG modular and legacy) | `naval-technology.md` |
| Batteries, torpedoes, fire control, mine warfare | `naval-support-technology.md` |
| Naval doctrine (post-1.17 Mastery system) | `naval-doctrine.md` |

## `08-strategy/` (mostly `**Inferred:**` synthesis, not wiki transcription)

| Question about... | Read |
|---|---|
| New-player onboarding, first decisions | `beginners-guide.md` |
| Difficulty levels / custom difficulty sliders | `difficulty-settings.md` |
| Opening focus/construction/research priority | `opening-build-orders.md` |
| Current-meta division templates by era | `division-template-meta.md` |
| Which Grand Doctrine to pick, by branch/playstyle | `doctrine-choice-guide.md` |
| Current-meta aircraft and air strategy | `air-strategy-meta.md` |
| Current-meta fleet composition and naval strategy | `naval-strategy-meta.md` |
| Military vs civilian factory ratio guidance | `economy-factory-ratios.md` |
| Common new-player mistakes | `common-mistakes.md` |
| How multiplayer strategy differs from singleplayer | `multiplayer-vs-singleplayer.md` |

## `00-meta/`

| Question about... | Read |
|---|---|
| What each DLC adds (headline features + pointer to the deep-dive file) | `dlc-overview.md` |
| Patch/version history (best-effort, not exhaustive) | `patch-history.md` |
| Console commands | `console-commands.md` |
| Default keybinds | `hotkeys.md` |
| Community slang/abbreviations (DEI, FTM, NF, ...) | `jargon.md` |
| UI screen orientation | `user-interface.md` |

## `09-reference/`

| Question about... | Read |
|---|---|
| Any specific modifier's effect | `list-of-modifiers.md` |
| A specific state (owner, region, resources) | `list-of-states.md` |
| Named generals/admirals/theorists/advisors roster | `list-of-commanders.md` |
| Named flying aces | `list-of-aces.md` |
| Named Military Industrial Organizations roster | `list-of-mios.md` |

Not here — check these instead: Factions list → `01-mechanics/diplomacy-factions-and-war.md`;
scientists roster → `01-mechanics/special-projects-and-scientists.md`; operations/operatives/
intelligence-agency rosters → `01-mechanics/espionage-and-operations.md`.
