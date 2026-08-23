---
title: Console commands
category: meta
tags: [console, debug, cheats, scripting, commands]
game_version: "1.19"
dlc: []
sources:
  - https://hoi4.paradoxwikis.com/Console_commands
---

## Summary

Console commands are debugging codes entered via the console window (accessed by pressing Shift+2, §, ~, \, `, ", º, ^ or ALT+2+1 depending on keyboard layout) on non-ironman games. Many commands can be toggled by repeating them; others require a reload or exit to disable. Commands often change between patches and may not work in ironman mode.

## Console access

Press **Shift+2**, **§**, **~**, **\**, **`**, **"**, **º**, **^** or **ALT+2+1** (or **Shift+3** on some layouts) to access the console. Key varies by keyboard layout.

## Internal IDs

Console commands use internal IDs for countries, focuses, technologies, and other game entities. The easiest way to find these is debug mode:

- `debug` — toggles debug mode, which shows IDs on hover for focuses, national spirits, laws, designers, technologies, provinces, and states.
- Use **Search in files** in text editors (Notepad++, Sublime Text, VS Code) to find localisation values in `/Hearts of Iron IV/localisation/english/` folder.

## Command syntax

- **Regular brackets** `(alias)` show aliases — e.g. `instantconstruction(ic)` means both `instantconstruction` and `ic` work identically.
- **Square brackets** `[optional]` mark optional arguments.
- **Angle brackets with square** `[<mandatory>]` mark required arguments.

## MIOs

MIOs is an acronym for **Military Industrial Organizations**.

## Useful commands

| Command | Effect | Example/Comment |
|---|---|---|
| `help [command name]` | Print all console commands or description of a specific command | — |
| `tag [<Country tag>]` | Change player control to a different country | — |
| `event [<event id>] [Target country tag]` | Execute an event | Event pages show ID and trigger conditions met/unmet |
| `finish_decision [<decision id>]` or `"all"` | Finish timed missions instantly | — |
| `add_ideas [<idea name>]` | Add ideas or national ideas to country | Can also replace laws |
| `remove_ideas [<idea name>]` | Remove national idea | — |
| `energy_ratio (er) [<ratio>]` | Set energy ratio 0–1 for factories without coal consumption | — |
| `FI [amount]` | Add faction initiative | `FI 5` adds 5 faction initiative |
| `mastery [<mastery amount>], [track name]` | Give doctrine mastery globally or to specific track | — |
| `gain_xp [<amount>]` | Add experience to selected leader/general/admiral | `gain_xp 100000` (level capped at 9) |
| `gain_xp [<trait>]` | Add trainable trait to selected leader/general/admiral | `gain_xp seawolf`; requires special save format for generic admirals |
| `cp [<amount>]` | Add command power | `cp 100` (capped at 100) |
| `st [<amount>]` | Add stability | `st 100` (capped at 100) |
| `add_war_support(ws) [<amount>]` | Add war support | `ws 100` (capped at 100) |
| `reduce_opinion [<country tag>]` | Reduce opinion to/from target tag | — |
| `allowtraits` | Allow free assignment of general traits | — |
| `add_equipment(ae) [<equipment amount>] [<equipment name>]` | Add equipment | Use basic name, e.g. `ae 1000 infantry_equipment_1`; only researched equipment; no naval equipment except convoy. Use `instantconstruction(ic)` or `instanttraining(it)` for ships. Custom variants use given name, e.g. `ae 1000 Matilda LP Mk. IV` |
| `add_latest_equipment(ale) [<equipment amount>]` | Give amount of latest equipment variants | Use given name for specific types, e.g. `ale 1000 Matilda LP Mk. IV` |
| `addfunds` | Add funds to all MIOs | Adds 1000 to every MIO |
| `addTaskCapacity [number]` | Add task capacity to all MIOs or specific MIO | Defaults to 1; find MIO id in `\Hearts of Iron IV\common\military_industrial_organization\organizations\<country tag>.txt` |
| `addSize [number]` | Add trait points to all MIOs or specific MIO | Defaults to 1; find MIO id in `\Hearts of Iron IV\common\military_industrial_organization\organizations\<country tag>.txt` |
| `add_cic_bank [number]` | Add economic capacity surplus to international market | Defaults to 1 |
| `whitepeace(wp) [<country tags>]` | Make white peace with specified countries | — |
| `teleport(tp)` | Activate teleportation tool | Right-click provinces with selected units to teleport them |
| `allowdiplo(adiplo,nocb)` | Allow all diplomatic actions regardless of rules | Can declare war without justification; most effective way to start wars instantly |
| `instant_wargoal` | Instant justification of war goals | Alternative to `allowdiplo` if only justification is needed |
| `debug_crash(crash)` | Crash the game | — |
| `instantconstruction(ic)` | Toggle instant construction cheat | Affects AI; ships also constructed instantly |
| `research [<slot id>]` or `"all"` | Research a technology from slot or all techs | `research all` instant-researches all technologies |
| `research_on_icon_click(roic)` | Research technology when clicking tech tree icon | Allows research without prerequisites; allows mutually exclusive techs |
| `toggle_hidden_techs(tht)` | Toggle show/hide all hidden techs | — |
| `sp_breakthrough [<number>]` | Add special project breakthrough points | `sp_br 20 specialization_land`; specializations: `specialization_land`, `specialization_air`, `specialization_naval`, `specialization_nuclear` |
| `sp_fast` | Skip prototyping stage and progress iteration stage for special projects | — |
| `sp_instant` | Autocomplete current special projects | — |
| `sp_available` | Unlock/lock all special projects with unfulfilled research prerequisites | E.g., unlocks nuclear projects without "Atomic Research" |
| `sp_unlock_all` | All special projects always visible and available | Ignores triggers and parent completion |
| `sp_research_all(sp_ra)` | Research all special projects | Creates scientist if none exists |
| `sp_prototype_reward` | Trigger specified prototype reward during project | — |
| `sp_add_scientist` | Add generic scientist | `sp_add_scientist 3 nuclear` or `sp_add_scientist 1` (optional level and specialization) |
| `sp_add_mastermind` | Add generic scientist with all specializations and max level | — |
| `sp_set_selected_scientist_level [<level>]` | Set scientist level | Facility view GUI must be open |
| `sp_add_selected_scientist_trait [<trait>]` | Add trait to scientist | `sp_add_selected_scientist_trait scientist_trait_brilliant_theorist`; facility view must be open; traits in `Hearts of Iron IV\common\scientist_traits\00_traits.txt` |
| `annex [<Target Country Tag>]` or `"all"` | Begin annexation | `annex USA` or `annex d01` or `annex all` |
| `puppet [<Puppeteer Country Tag>] [<Puppet Target Country Tag>]` | Turn target country into puppet | `puppet GER CZE` (Czechoslovakia becomes German puppet) |
| `manpower [amount]` | Add manpower to player | Defaults to 10 million if unspecified |
| `add_opinion [<Country tag>]` | Add opinion to/from target tag | Adds 100 (hardcoded); appears as `cheat_opinion_modified_good` in diplomacy screen |
| `add_legitimacy [<Country tag>] [<value>]` | Add legitimacy to specified tag | `add_legitimacy POL 22` |
| `observe(spectator)` | Switch to play no country; no messages or pauses | Interferes with AI performance; not reliable AI indicator |
| `tdebug` | Toggle debug info | Helpful for finding nation tags and IDs |
| `occupationpaint(op)` | Toggle occupation painting or occupy all uncontrolled land | `op JAP` occupies Japan's owned but not controlled land |
| `setowner [<country tag>]` | Set state owner | Select state by clicking (not state ID) |
| `setcontroller [<country tag>] [province id]` | Set province controller | — |
| `xp [<XP amount>]` | Give army, navy, and air experience to player | Can be used once per day |
| `pp(fuhrer_mana,political_power) [PP amount]` | Give or remove political power | Defaults to 1000 if unset |
| `fuel [<amount>]` | Add fuel | `fuel 100000` (capped at deposit capacity) |
| `civilwar [<ideology>] [<target country tag>]` | Spawn civil war | Valid ideologies: `fascism`, `communism`, `democratic`, `neutrality`; e.g. `civilwar fascism ENG` |
| `add_party_popularity [ideology group] [value]` | Add party popularity | Ideology shortcuts: `d`=democratic, `f`=fascism, `n`=neutrality, `c`=communism |
| `set_ruling_party [ideology group]` | Set ruling party | Ideology shortcuts: `d`, `f`, `n`, `c` |
| `Focus.AutoComplete(fa)` | Instantly finish national focuses | Affects AI |
| `Focus.NoChecks` | Ignore focus requirements | Affects AI |
| `Focus.IgnorePrerequisites` | Ignore focus prerequisites | Allows starting focus mid-tree; affects AI |
| `freefocuses(ff)` | Enable freely activating any focuses | Combination of `Focus.AutoComplete`, `Focus.NoChecks`, `Focus.IgnorePrerequisites` |
| `Decision.FastRemove` | Shorten decisions to 1 day | — |
| `Decision.NoChecks` | Ignore decision requirements | Disables cost; affects AI |
| `instant_prepare` | Instantly prepare naval invasions | Only works in debug mode |
| `instanttraining(it)` | Instantly train divisions and ships | Affects AI |
| `nuke [number]` | Add nukes | E.g. `nuke 100` or `nuke 1000` |
| `ai_accept(yesman)` | AI accepts all diplomatic offers | — |
| `add_core [<state_id>]` | Add cores | — |
| `Agency.Instant` | Make everything regarding agencies instant | Combination of `Operation.Instant`, `IntelNetwork.Instant`, `Agency.InstantSlotUnlock`, `Agency.Autocomplete` |
| `Agency.InstantSlotUnlock` | Remove wait time between agent recruits | — |
| `Agency.Autocomplete` | Instantly complete agency upgrades | — |
| `prevent_operative_detection` | Operatives/spies won't be detected | — |
| `force_operative_detection` | Operatives/spies will be detected | — |
| `Operation.instant` | Instantly finish all operations | Affects AI |
| `agency.keepexcessoperatives` | — | — |
| `deleteallunits(delall) [country]` | Delete all armies and fleets of specified countries | `deleteallunits SPR` |
| `deleteallunitsbut(delallbut) [country]` | Delete all countries' armies/fleets except one | `delallbut SPR` |
| `add_autonomy [<Target Country Tag>] [num]` | Change country autonomy level | `add_autonomy PHI -200` |
| `resistance` | Increase resistance in selected province | `resistance 100` (selects one province in clicked region) |
| `compliance` | Increase compliance in selected province | `compliance 100` (selects one province in clicked region) |
| `add_intel [<Country tag 1>] [Country tag 2] [type]=[number]` | Set intel one country has against another | `add_intel FRA` (max intel vs France); `add_intel GER USA army=20` (20% army intel); `add_intel JAP airforce=90 civilian=76` (90% air, 76% civilian) |
| `add_mines` | Maximize player-owned naval mines in selected regions | — |
| `acclimization [<climate type>] [<number>]` | Set division acclimization to climate and percentage | `acclimization cold_climate 75`; reduces cold/hot weather penalties; opposite climate resets to 0% |
| `debug_smooth` | Toggle frame smoothing | Can increase game speed 10–35% depending on system |

## Modding-useful commands

| Command | Effect | Example/Comment |
|---|---|---|
| `guibounds(gui)` | Toggle GUI bounds debug for testing window sizes | Shows sprite name and interface element on hover; search `/Hearts of Iron IV/interface/*.gfx` files to find images |
| `set_var [<variable>] [<value>]` | Change variable value | — |
| `get_var [<variable>]` | Show variable value in console | — |
| `list_vars` | List variables in selected scope and their values | — |
| `set_country_flag [<Country Flag>]` | Add country flag to currently played nation | Does not work if specifying another nation's tag |
| `set_global_flag [<Global Flag>]` | Add global flag | — |
| `list_flags` | List currently active flags in console | Context-sensitive: global_flag (none selected), country_flag (country selected), state_flag (state selected) |
| `fast_forward [<amount of days>]` | Fast forward specified days | — |
| `list_hidden_focuses` | List all hidden focuses from a country | — |
| `show_focuses` | Show all hidden focuses | — |
| `trigger [<scripted_trigger_name>]` | Check if scripted trigger is true | — |
| `eval_trigger [<trigger code block>]` | Check if trigger code is true in selected scope | `eval_trigger OR = { has_completed_focus = GER_remilitarize_the_rhineland has_war_support > 0.5 }` |
| `effect(e) [<scripted_effect_name>]` | Execute scripted effect in selected scope | `e POL_remove_danzig_effect` on a state |
| `eval_effect [<effect code block>]` | Execute effect code in selected scope | `eval_effect load_focus_tree = german_focus` switches selected country to German tree |
| `ai [country tag...]` | Toggle AI on or off | No parameters toggles AI for all; parameters toggle exceptions for those countries; useful for confirming crashes are AI-related |
| `aiview` | Enable AI debug info | — |
| `human_ai` | AI controls player-led country while player retains control | Logs to `/Hearts of Iron IV/logs/scripted_ai.log` |
| `set_cosmetic_tag [<country tag>] [<cosmetic tag>]` | Change country name and flag | `set_cosmetic_tag USA SOV` |
| `reload [<type>]` or `[filename]` | Reload files of given type or specific interface file | `reload loc` (localisation); `reload focus` (focuses); `reload landcombat.gui` (interface) |
| `reloadoob [<Target Country Tag>]` | Reload orders of battle | — |
| `reloadinterface` | Reload entire interface | — |
| `reloadtechnologies` | Reload technology database | — |
| `updateequipments` | Update equipment database | — |
| `updatesubunits` | Update subunit database | — |
| `update_loc [localization tag]` | Update localization tag file | — |
| `error` | Open error log file | Equivalent to error dog if debug mode enabled; fails if path contains special characters |
| `imgui` | Control ImGui UIs | `imgui show` lists subcommands; covers script profiling, AI debugging, character listing |
| `goto_province [province id]` | Move camera to specified province | — |
| `goto_state [state id]` | Move camera to specified state | — |

## Other in-game commands

| Command | Effect | Example/Comment |
|---|---|---|
| `province_ids(pid)` | Show province IDs on map | — |
| `ShowTechBonus` | Show tech bonuses (developer-only) | Likely tech-bonus related |
| `normals` | Unknown (developer-only) | — |
| `rendertype` | Report render backend used | — |
| `tweakergui` | Spawn tweaker GUI | — |
| `time` | Show current game time | — |
| `reloadfx [map/mapname/postfx or *.fx filename]` | Reload shader | — |
| `particle_editor` | Spawn particle editor | — |
| `analyzetheatres(anth)` | Analyze theatres for errors | — |
| `massconquer(massc)` | Mass conquer tool (developer-only) | Requires direct province names |
| `aircombat(airc) [<scenario>] [<result>] [<prov id>] [<state id>] [<state id>] [<equip type>] [<equip type>] [<country>] [<country>]` | Spawn air combat in desired location (developer-only) | — |
| `fronts` | Toggle foreign fronts visibility | — |
| `ai_front_dump(aifrontdump)` | Dump AI front data to log; requires unit selected | — |
| `traderoutes` | Toggle trade routes visibility | — |
| `debug_tactics` | Toggle visibility of tactics debug tooltip | — |
| `reloadsupply(relsup)` | Reinitialize supply systems | — |
| `deltat [<speed factor>]` | Control animation speeds | — |
| `building_health(bhealth) [<building type>] [<state or prov id>] [<building level>] [<health to add>]` | Change specified building health | — |
| `nomapicons` | Toggle map icons | — |
| `nopausetext` | Toggle pause banner for screenshots | — |
| `nextsong` | Change currently playing soundtrack | — |
| `combatsound` | Set random sound frequency for combat view | 0–50 |
| `morehumans(humans) [num]` | Add more humans | — |
| `window(wnd) [open/close] [window gui name]` | Open or close specified window | — |
| `poll` | Poll valid events | — |
| `pause_in_hours` | Pause game after X hours | — |
| `testevent [<Event ID>] [<Character ID>]` | Test event without triggering | — |
| `resign` | Resign from game | — |
| `add_interest [<Country tag>]` | Add country tag to your interest | — |
| `remove_interest [<Country tag>]` | Remove country tag from your interest | — |
| `add_diplo` | Add diplomatic entouté | — |
| `PrintSynchStuff` | Print random count and seed | — |
| `SetRandomCount` | Set random count to 0 or arg | — |
| `ai_invasion` | Toggle AI naval invasions | — |
| `ai_pp_log` | Print AI use of political power to log | — |
| `ai_idea_desire_log` | Print AI desire for ideas to log; current country only | — |
| `ai_force_template` | Force AI to only spend army XP on template design | — |
| `ai_force_equipment` | Force AI to only spend army XP on equipment design | — |
| `ai_front_id` | Get address of selected group's front debug ID | — |
| `fow(debug_fow) [Province ID]` | Turn off fog of war; optionally only within specified province | — |
| `collision(debug_collision)` | Toggle debug display of normals/bounding boxes/collision | — |
| `savegame` | Create savefile | — |
| `savecheck` | Create, load, and verify savefile integrity | Makes Test_01, loads it, makes Test_02; files should match |
| `IP` | Show your IP | — |
| `requestgamestate` | Request gamestate from host | — |
| `nudge` | Go to nudge tool | — |
| `mapmode [Mapmode type (int)]` | Change mapmode | — |
| `fullscreen` | Toggle fullscreen | — |
| `prices` | Show price info | — |
| `remove_core [<State ID>] [<Country Tag>]` | Remove core | Command does not work |
| `debug_zoom` | Zoom in game | — |
| `debug_types` | Print data types for all dynamic reference objects (RTTI only) | — |
| `debug_show_event_ID` | Show event ID | — |
| `debug_commands` | Print command count to message.log | — |
| `debug_events` | Start counting events | — |
| `debug_dumpevents` | Dump event data to game log | — |
| `debug_diploactions` | Start counting diplomatic actions | — |
| `debug_dumpdiploactions` | Dump diplomatic action data to game log | — |
| `debug_assert` | Toggle asserts on/off | — |
| `debug_nomouse` | Toggle mouse scrollwheel on/off | — |
| `debug_terrain` | Toggle terrain on/off | — |
| `debug_cities` | Toggle cities painting mode on/off | — |
| `debug_water` | Toggle water on/off | — |
| `debug_fronts` | Toggle interpolated fronts debug | — |
| `debug_off_front_snap(dbg_fsnap)` | Toggle offensive fronts snapping debug | — |
| `debug_borders` | Toggle borders on/off | — |
| `debug_trees` | Toggle trees on/off | — |
| `debug_rivers` | Toggle rivers on/off | — |
| `debug_postfx` | Toggle PostFX on/off | — |
| `debug_sky` | Toggle sky on/off | — |
| `debug_bloom` | Toggle bloom on/off | — |
| `debug_tooltip` | Toggle tooltips on/off | — |
| `debug_nuking` | Allow nuking every province without conditions (removed patch 1.15.1) | — |
| `flagsoutput [<path>]` | Create texture atlas files from memory | — |
| `cityreload` | Reload cities | — |
| `version` | Show current game version | — |
| `debug_nogui` | Toggle GUI on/off | — |
| `debug_volume [<Volume Delta>]` | Modify music volume | — |
| `debug_lockcamera` | Toggle camera lock on/off | — |
| `debug_lines` | Toggle debug lines | — |
| `debug_entities` | Toggle debug entities | — |
| `debug_info` | Toggle debug info | — |
| `debug_particle` | Toggle particles debug info | — |
| `debug_ai_budget [CountryTag]` | Show AI budget data | — |
| `debug_textures` | Write texture info to application debug log | — |
| `debug_texture` | Draw textures like bloom | — |
| `debug_wireframe` | Toggle forced wireframe on/off | — |
| `debug_achievements_clear` | Clear all achievements and user stats (developer-only) | — |
| `moveunit [<Unit ID>] [<Province ID>]` | Move unit to province | — |
| `spawnactor [<Actorname>] [<Province ID>] [<Animation> OPTIONAL]` | Spawn actor with optional animation | — |
| `cameraclamp` | Toggle camera clamping | — |
| `provtooltipdebug(tdebug)` | Toggle debug info in province tooltip | — |
| `reloadweather [<randomseed>]` | Reload and regenerate weather | — |
| `weather` | Toggle weather simulation | — |
| `debug_air_vs_land(dbg_cas)` | Toggle debug mode for air vs land combat | — |
| `mapnames` | Toggle map names | — |
| `gbreload` | Reload gradient borders (developer-only) | — |
| `gbpaint [layer] [channel]` | Toggle gradient border painting | — |
| `profilelog` | Print profiling information to time.log | — |
| `run` | Run specified file with list of commands | — |
| `oos` | Out of sync (developer-only) | — |
| `trigger_docs(effect_docs,scripting_docs,docs)` | Print docs for triggers, effects, variables to game.log | — |
| `threat [Threat amount]` | Add/show threat level (world tension generated by tag) | Positive values add to world tension; negative subtract; `threat 999999999` resets to 0; use tag-switching to adjust any country's tension |
| `3dstats` | Toggle 3D stats | — |
| `hdr` | Toggle HDR | — |
| `hdr_debug` | Toggle HDR debugging | — |
| `srgb` | Toggle sRGB | — |
| `bloom` | Toggle bloom | — |
| `PostEffectVolumes.Default [posteffect_values name]` | Toggle default posteffect values | — |
| `night` | Toggle night (developer-only as of 1.01; emulate via toolbar shortcut N) | — |
| `filewatcher` | Toggle filewatcher | — |
| `createlean` | Create LEAN textures | — |
| `helplog` | Print all console commands to game.log | — |
| `helphelp` | Double rainbow help | — |
| `hsv` | Convert RGB to HSV | — |
| `tag_color` | Test setting country color | — |
| `browser [url]` | Show browser window | — |
| `browser_base_url [url]` | Set browser base URL | — |
| `airealism` | Enable realistic AI (easter egg) | AI smacktalk in chats; useless in multiplayer or singleplayer without chat |
| `instant_wargoal` | Allow instant justification of war goals on countries | — |
| `allowideas` | Allow picking any idea even if normally unavailable | Overrides available/visible triggers; not allowed trigger |
| `release [<country tag>]` | Release country or releasable nation | `release slv` releases Slovenia |
| `InternationalMarket.AddSubsidyForTags [<economic capacity>] [<equipment>] [<country tag>]` | Add subsidy for player to buy from specified country | `InternationalMarket.AddSubsidyForTags 5000 light_tank_chassis GER` (5k EC for German light tanks) |
| `random_seed` | Randomize current game seed | AI uses seed to decide focuses and decisions; useful for generating favorable AI outcomes |
| `eval_effect [<country tag>] = { create_faction = "[faction name]" }` | Create faction with specified name | Inserted tag becomes faction leader |
| `eval_effect [<country tag>] = { dismantle_faction = yes }` | Delete faction of specified country | — |
| `eval_effect [<country tag>] = { add_to_faction = [<country tag>] }` | Add country to faction | Second tag joins first tag's faction |
| `eval_effect [<country tag>] = { remove_from_faction = [<country tag>] }` | Remove country from faction | Second tag removed from first tag's faction |
| `eval_effect [<country tag>] = { set_faction_name = "[faction name]" }` | Rename faction of specified country | — |
| `toggle_silhouette_portraits` | Enable/disable silhouette portraits (developer-only) | — |
| `armageddon` | Deal 100% damage to all state/shared/provincial buildings every state in all countries | Plays nuke detonation animation but does not apply Nuclear Fallout modifier |

## Commands that no longer work

> ⚠️ These commands are documented as removed in specific patches:
>
> - `winwars` — removed patch 1.9.1
> - `debug_nuking` — removed patch 1.15.1
