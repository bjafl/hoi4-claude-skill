---
title: Combat Tactics
category: land-warfare
tags: [combat tactics, initiative, preferred tactics, phases, counters, land battle, command power]
game_version: "1.19"
dlc: []
sources:
  - https://hoi4.paradoxwikis.com/Combat_tactics
---

## Summary

Combat tactics are picked automatically by each side's commanding general every **12 hours** from a weighted list, and modify tactic damage, combat width and movement in land battles. Battles run through **phases** — Default, Close combat, Tactical withdrawal, Seize bridge, Hold bridge, Street fighting — each with its own tactic pool, and some tactics push the battle into a new phase. This file lists every tactic in every phase with its trigger, weight, counters, and modifiers.

## Tactic selection

- Tactics are **re-selected every 12 hours** from a weighted list available to each side's commander.
- A battle can be in different **phases**, each with a different available pool. Battles always start in **Default**.

### Initiative

The side with **Initiative** (golden frame around its commander's portrait, with chevrons underneath) **picks its tactic second** and has a raised chance to counter the enemy's pick.

**How Initiative is decided:**

1. Compare the leading generals' **skill levels**.
2. If either side has a **higher reconnaissance value** in any of its divisions (**including reserves**), that side gets **+5 skill levels** for this comparison — flat, regardless of how large the recon difference is.
3. The side with the higher effective skill level gets Initiative. **Ties favour the defender.**

The loser of that comparison must pick first. The Initiative side can then respond with a countering tactic, whose weight gets a bonus of **+35% per point of advantage in the skill comparison**. Note that Initiative does **not** reduce the weights of tactics that would be countered — the Initiative side can still pick something that gets countered.

### Preferred tactics

Preferred tactics can be set at three levels, and their effects **stack**.

| Level | Where set | Weight bonus | Notes |
|---|---|---|---|
| **Country** | Officer corps | **+25%** for all commanders of that country | Changeable at any time; each change costs command power |
| **Field marshal** | Commander details screen, requires **skill ≥ 5** | **+25%** for all battles commanded by them or by generals in their army group | **Cannot be changed once selected** |
| **General** | Commander details screen, requires **skill ≥ 5** | **+50%** for battles they command | **Cannot be changed once selected** |

- **Cost: 20 command power**, one time. Reduced by the **Flexible Organization** officer corps spirit.
- Certain officer corps spirits amplify specific preferred tactics across all three levels — e.g. **Static Warfare** with **Elastic Defense**, **Aggressive Reconnaissance** with **Infiltration Assault**. Some national spirits do the same (e.g. **I Am Death** for the British Raj).
- **Not all tactics can be preferred.** Basic tactics such as **Assault** or **Counter-Attack** cannot be, and neither can tactics that exist only in special phases such as **Recapture Bridge** or **Evade**.

## Effects

- **Attacker/defender tactic damage do NOT change soft/hard attack** (i.e. not the number of attacks), despite what in-battle tooltips suggest. They **directly change the damage a successful hit causes**.
- **Tactics combat width** modifies the **base** combat width of the battle, **not** the flanking width.
- Attacking units carry a default **−67% movement penalty**. Tactic movement modifiers offset or worsen it, **stacking additively**.
- When a tactic is **countered**, **all** of its effects are negated — including its own negative ones.

## Phase: Default

Columns: Atk dmg = attacker tactic damage, Def dmg = defender tactic damage, Atk org / Def org = attacker/defender tactic organization damage, Width = tactics combat width, Move = tactics movement.

| Tactic | Trigger | Weight | Counters | Countered by | Atk dmg | Def dmg | Atk org | Def org | Width | Move | Starts phase | Requires doctrine |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Attack** | — | 4 | — | Counter-Attack | +5% | — | — | — | — | — | — | — |
| **Assault** | Division artillery ratio > 10% | 2 in urban terrain, else 0.4. **4** if commanding general has **Aggressive Assaulter** and in urban terrain, else 0.8 | — | Counter-Attack | +25% | — | — | — | — | — | **Close combat** | — |
| **Encirclement** | Frontage filled; has reserves; **and** at least one of: skill advantage > 0, trait **Panzer Leader**, trait **Trickster** | 4; **8** if trait **Panzer Expert** or **Combined Arms Expert** | — | Tactical Withdrawal | +25% | +5% | — | — | +50% | — | — | — |
| **Shock** | — | 4; **8** if general has **Aggressive Assaulter** | Delay | Ambush | — | −25% | — | — | — | — | — | — |
| **Breakthrough** | Hardness > 50% **or** skill advantage > 1 | 4 | Ambush | Backhand Blow | +25% | −15% | — | — | — | +50% | — | Blitzkrieg / Combined Arms / Shock and Awe / Assault Breakthrough / Breakthrough Priority |
| **Blitz** | Hardness > 50%; does **not** have Soviet focus **The Glory of the Red Army**; and at least one of: skill > 2, trait **Panzer Leader**, skill advantage > 1 | 4; **8** if trait **Panzer Leader** or **Combined Arms Expert** | — | Elastic Defense | +15% | −15% | — | — | — | +50% | — | Armored Spearhead / Mechanized Offensive / Armored Operations / Deep Operations |
| **Masterful Blitz** | Hardness > 50%; **has** Soviet focus **The Glory of the Red Army**; and at least one of: skill > 2, trait **Panzer Leader**, skill advantage > 1 | 4; **8** if trait **Panzer Leader** or **Combined Arms Expert** | — | Elastic Defense | +20% | −20% | — | — | +10% | +50% | — | — |
| **Seize Bridge** | Has combat modifier **River Crossing**; and either skill > 3, or (**Offensive Doctrine** trait and skill > 2) | 2 | — | — | +20% | −5% | — | — | −25% | +10% | **Seize bridge** | — |
| **Mass Charge** | Frontage filled; has reserves | 4 | — | — | +10% | +10% | — | — | +50% | — | — | People's Army |
| **Banzai Charge** | Country is **Japan** | 4 | — | Overwhelming Fire | +25% | +10% | — | — | — | +10% | — | — |
| **Infiltration Assault** | — | 4 | — | — | +10% | −5% | — | — | — | — | — | Infantry Offensive |
| **Well-Planned Attack** | — | 4 | — | — | +15% | — | — | — | — | — | — | Grand Assault |
| **Relentless Assault** | — | 4 | — | — | +20% | +5% | — | — | — | +15% | — | Large Front Operations |
| **Unexpected Thrust** | — | 4 | — | — | +15% | — | — | — | — | +15% | — | Mobile Warfare |
| **Suppressive Barrage** | — | 4 | — | — | +10% | −20% | — | — | — | — | — | Superior Firepower |
| **Defend** | — | 4 | — | — | — | +5% | — | — | — | — | — | — |
| **Counter-Attack** | Skill advantage > 0 | 4; **8** if general has **Unyielding Defender** | Attack, Assault | — | — | +25% | — | — | — | — | — | — |
| **Delay** | — | 4 | — | Shock | −25% | −15% | — | — | — | −25% | — | Delay |
| **Tactical Withdrawal** | Skill advantage > 0 **or** trait **Trickster** | 4 | Encirclement | — | −25% | −5% | — | — | −25% | — | **Tactical withdrawal** | Tactical Control / Advanced Firebases |
| **Ambush** | Skill advantage > 1, **or** skill > 2, **or** trait **Trickster** | 4 | Shock | Breakthrough | −25% | — | — | — | — | — | — | — |
| **Elastic Defense** | Trait **Defensive Doctrine** **or** skill > 2 | 4 | Blitz, Masterful Blitz | — | −15% | +10% | — | — | — | −25% | — | Elastic Defense / Mobile Defense / Mechanized Offensive / Armored Operations / Operational Concentration |
| **Backhand Blow** | Skill > 4, **or** (trait **Defensive Doctrine** and skill > 3) | 4 | Breakthrough | — | −20% | +25% | — | — | — | −30% | — | Backhand Blow / Continuous Offensive |
| **Hold Bridge** | Has combat modifier **River Crossing**; and skill > 2 **or** trait **Defensive Doctrine** | 2 | — | — | +20% | −5% | — | — | −25% | +10% | **Hold bridge** | — |
| **Guerrilla Tactics** | Skill > 2 **or** trait **Trickster** | 4 | — | — | **−70%** | **−60%** | — | — | −50% | — | — | Guerrilla Warfare / Werwolf Guerrillas |
| **Overwhelming Fire** | — | 2 | Banzai Charge | — | −10% | +10% | — | — | — | — | — | Kampfgruppe / Overwhelming Firepower / Regimental Combat Teams / Assault Concentration / Vast Offensives |
| **Urban Defense** | In urban terrain | 4 if province VP value > 5, else 2. **×3** with trait **Urban Assault Specialist**; **×1.5** with trait **Engineer** | — | — | −5% | +5% | −5% | — | — | −5% | **Street fighting** | — |

## Phase: Close combat

Entered from **Assault**. Exited back to Default by **Close Quarters Withdraw**.

| Tactic | Trigger | Weight | Atk dmg | Def dmg | Starts phase |
|---|---|---|---|---|---|
| **Close Quarters Attack** | — | 4 | +10% | +5% | — |
| **Close Quarters Storm** | — | 2 | +20% | +20% | — |
| **Close Quarters Withdraw** | — | 1 | −5% | −5% | **Default** |
| **Close Quarters Defense** | — | 4 | +5% | +10% | — |
| **Close Quarters Local Strongpoint** | — | 2 | −20% | — | — |

None of these counter or are countered, and none modify width, movement or org damage.

## Phase: Tactical withdrawal

Entered from **Tactical Withdrawal**. Exited back to Default by **Intercept**.

| Tactic | Weight | Atk dmg | Def dmg | Width | Starts phase |
|---|---|---|---|---|---|
| **Tactical Withdrawal Attack** | 4 | −25% | −10% | −25% | — |
| **Pursuit** | 4 | −15% | −5% | −25% | — |
| **Intercept** | 4 | −5% | −10% | — | **Default** |
| **Withdrawal** | 4 | −30% | −5% | −25% | — |
| **Evade** | 4 | −40% | −10% | −25% | — |

No triggers, counters or movement modifiers. **Evade** cannot be set as a preferred tactic.

## Phase: Seize bridge

Entered from **Seize Bridge** (Default phase). All tactics in this phase apply **−25% combat width**.

| Tactic | Trigger | Weight | Counters | Countered by | Atk dmg | Def dmg | Starts phase |
|---|---|---|---|---|---|---|---|
| **Hold Bridge** | — | 4 | — | — | +20% | — | — |
| **Defend Bridge** | Skill > 4 | 4 | Recapture Bridge | — | +20% | −10% | — |
| **Assault Bridge** | — | 4 | — | — | — | −5% | — |
| **Reckless Assault** | Skill < 3 | 4 | — | — | +25% | −10% | — |
| **Recapture Bridge** | Skill > 2 **or** trait **Trickster** | 4 | — | Defend Bridge | +10% | −5% | **Hold bridge** |

**Recapture Bridge** cannot be set as a preferred tactic.

## Phase: Hold bridge

Entered from **Hold Bridge** (Default phase) or **Recapture Bridge**. All tactics in this phase apply **−25% combat width**.

| Tactic | Trigger | Weight | Counters | Countered by | Atk dmg | Def dmg | Starts phase |
|---|---|---|---|---|---|---|---|
| **Attack** | — | 4 | — | — | +10% | — | — |
| **Rush Bridge** | Skill > 4 | 4 | — | — | +20% | — | — |
| **Storm Bridge** | — | 2 | — | Defend Bridge | +20% | +5% | **Seize bridge** |
| **Hold Bridge** | Skill < 3 | 2 | — | — | +20% | −10% | — |
| **Defend Bridge** | Skill > 2 **or** trait **Trickster** | 2 | Storm Bridge | — | +10% | +5% | — |

## Phase: Street fighting

Entered from **Urban Defense** (Default phase, urban terrain only).

| Tactic | Trigger | Weight | Counters | Countered by | Atk dmg | Def dmg | Atk org | Def org | Width | Move |
|---|---|---|---|---|---|---|---|---|---|---|
| **Street Fighting** | — | 2 | — | — | +5% | +10% | — | −5% | +5% | — |
| **Street by Street Barrage** | Division artillery ratio > 10% | 2 | — | — | +10% | −5% | — | −10% | −5% | — |
| **Armour Supported Urban Assault** | Has a **Light / Medium / Heavy Flame Tank Company** | 2 | — | — | +15% | — | — | −10% | −10% | — |
| **Mouse Holing** | Has an **Engineer Company** or **Pioneers** | 2 | Fortified Defense | — | — | −10% | — | −10% | — | −5% |
| **Defend City** | — | 2 | — | — | −5% | +10% | −10% | — | — | — |
| **Fortified Defense** | — | 2 | — | Mouse Holing | −10% | +5% | −15% | — | — | — |
| **Urban Ambush Tactics** | — | 2 | — | — | — | +25% | −10% | — | — | — |

## Counter chains at a glance

| Tactic | Counters | Is countered by |
|---|---|---|
| Attack | — | Counter-Attack |
| Assault | — | Counter-Attack |
| Counter-Attack | Attack, Assault | — |
| Shock | Delay | Ambush |
| Delay | — | Shock |
| Ambush | Shock | Breakthrough |
| Breakthrough | Ambush | Backhand Blow |
| Backhand Blow | Breakthrough | — |
| Blitz / Masterful Blitz | — | Elastic Defense |
| Elastic Defense | Blitz, Masterful Blitz | — |
| Encirclement | — | Tactical Withdrawal |
| Tactical Withdrawal | Encirclement | — |
| Banzai Charge | — | Overwhelming Fire |
| Overwhelming Fire | Banzai Charge | — |
| Mouse Holing | Fortified Defense | — |
| Fortified Defense | — | Mouse Holing |
| Defend Bridge (Seize bridge phase) | Recapture Bridge | — |
| Recapture Bridge | — | Defend Bridge |
| Defend Bridge (Hold bridge phase) | Storm Bridge | — |
| Storm Bridge | — | Defend Bridge |

**Inferred:** the practical levers on this system are (a) always keep a recon company somewhere in the stack — the flat **+5 skill levels** for a recon edge is usually the cheapest route to Initiative; (b) high-skill generals both unlock the strong tactics (Backhand Blow at skill > 4, Ambush at skill > 2) and win the Initiative comparison; and (c) preferred tactics stack to **+100%** weight (25 country + 25 field marshal + 50 general) on a single tactic, which is enough to make one tactic dominate a general's picks.

## Related files

- [land-combat.md](land-combat.md) — how tactic damage multipliers enter the damage formula
- [division-designer.md](division-designer.md) — recon and signal companies, artillery ratio
- [land-units-and-stats.md](land-units-and-stats.md) — recon and initiative values per company
