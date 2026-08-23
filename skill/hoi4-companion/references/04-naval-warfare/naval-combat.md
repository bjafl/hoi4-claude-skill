---
title: Naval Combat
category: naval-warfare
tags: [naval battle, screening, capital ships, carriers, submarines, torpedoes, hit chance, armor, critical hit, naval strike, sortie efficiency]
game_version: "1.19"
dlc: [Man the Guns, No Step Back]
sources:
  - https://hoi4.paradoxwikis.com/Naval_battle
---

## Summary

A naval battle starts when two task forces occupy the same province. One side is the attacker (reduced efficiency unless already defending), one the defender (always full efficiency). The battle resolves in continuous 1-hour cycles: each ship independently selects up to three targets (one per weapon type) and fires if weapons are off cooldown. Battles end when one side fully retreats or is destroyed. This file covers fleet composition (screening, capitals, carriers, subs), damage and hit formulas, critical hits, carrier mechanics, and naval strikes.

## Fleet composition and layout

A naval battle field divides into four functional groups:

- **Screening group:** Screen ships that protect capital ships and carriers from torpedoes.
- **Battle-line:** Capital ships (battleships, battlecruisers, heavy cruisers) except carriers. They deal heavy firepower and screen the carrier group from torpedoes.
- **Carrier group:** Carriers and any convoys under attack. Carriers strike from long range via aircraft.
- **Submarine wolfpack:** Submarines, which evade detection and threaten battleline and carriers if insufficiently screened.

The **attacker** may join with reduced efficiency (depends on circumstances); the **defender** always joins at full efficiency.

## Screening efficiency

The **screening ratio** is the count of screen ships vs capital ships + carriers + convoys. With good positioning (100% positioning), **100% screening efficiency** is reached at:

- **3 screen ships per capital ship or carrier**
- **0.5 screen ship per convoy**

Example: 4 carriers + 4 battleships = 24 screen ships needed for 100% screening. Or: 16 convoys under submarine attack = 8 screen ships needed for 100% screening.

At 100% screening efficiency:

- **+40% hit chance** against screening group
- **+20% retreat speed**

The **carrier screening ratio** is capital ships vs carriers + convoys. For 100% **carrier screening efficiency**:

- **1 capital ship per carrier**
- **0.25 capital ship per convoy**

At 100% carrier screening efficiency:

- **+10% sortie efficiency**
- **+20% retreat speed**
- Further reduces enemy torpedo attacks against carriers (stacking diminishingly)

**Positioning penalty:** bad positioning applies a penalty scaling up to **−50%** at 0% positioning, effectively increasing the screening ratio required to reach 100% by up to **2×**.

## Weapon cooldown and attack rate

Weapons fire on this schedule:

| Weapon type | Cooldown | Reduction available |
|---|---|---|
| Heavy attack guns | 1 hour | — |
| Light attack guns | 1 hour | — |
| Torpedoes | 4 hours | −25% (Loading Drill Master admiral trait) |
| Depth charges | — | — |

Each ship with offensive weapons (not carriers/convoys) can target up to three enemies per combat hour if weapons are off cooldown: one target per weapon type (depth charges, light guns, heavy guns, torpedoes).

## Target selection

Targeting rules depend on weapon type and enemy positioning:

| Weapon | Target restrictions |
|---|---|
| **Depth charges** | Only submarines, and only if revealed |
| **Light guns** | Closest non-empty group only; carriers/convoys cannot target carriers/convoys |
| **Heavy guns** | First two non-empty groups |
| **Torpedoes** | Probability to bypass screening = 100% − screening efficiency; to reach carrier group = 100% − carrier screening efficiency |

### Submarine targeting (by engagement rule)

- **High risk:** only targets screens when actually revealed, but will target capitals
- **Medium risk or higher:** will target capitals
- **Low risk:** does not target screens

### Target weighting when ship is engaged

When a firing ship is not escaping, targets are weighted by type (light guns weights in parentheses):

| Target | Weight |
|---|---|
| Capitals | 30 (2) |
| Screens | 3 (6) |
| Submarines | 4 |
| Carriers | 15 (1) |
| Submarine vs Convoy | 600 (40) |
| Non-sub vs Convoy | 60 (4) |

Weights are further modified:

- **Target below full strength:** up to **+100%**
- **Target escaping:** **−50%**
- **Target actively fighting:** **+50%**

When the firing ship is escaping, only targets actively fighting are considered, and the highest-scoring target is chosen (no randomization).

## Submarine mechanics

Submarines are **completely immune to targeting while hidden**, indicated by a crossed-out eye. A hidden submarine reveals for **20 hours** before hiding again.

### Submarine reveal conditions

**1. Defender-side spawn:** if the submarine starts the battle on the defending side (e.g., spotted by enemy patrol), it is **initially revealed for 16 hours**. This is the primary window for anti-submarine ships to be effective.

**2. Reveal on attack (active detection):**

The formula is:
```
reveal_chance = (100% + torpedo_reveal_chance_factor) × 3.5% × max(sub_visibility, 0) / 100 × (300% − 2 × positioning)
```

Sources of **−torpedo reveal chance:** Electric Torpedo technology, Silent Hunter admiral trait, Convoy Interdiction or Submarine Operations naval doctrines. Bad positioning increases the visibility effect by up to 200%.

**3. Passive hourly reveal:**

The game includes a **passive hourly reveal chance** depending on enemy sub detection:
```
hourly_passive_reveal = 0.001% × max(round((min(detection_factor, 2) × 11)³), 1)
detection_factor = 0% × enemy_air_sub_detection + average_enemy_ship_sub_detection / 100 
                   + max(sub_visibility, 0) / 100 × (300% − 2 × positioning)
```

**Known issue:** this chance is extremely small in practice. With average enemy sub detection of 45 (near-maximum for a destroyer fleet) vs 25 sub visibility (early submarines), the hourly chance is only **0.457%**, averaging **~152 hours** (~6 days) to reveal one hidden sub. Aerial sub detection contributes **0%** to passive reveal (code bug).

## Hit chance and hit profile

### Base hit chance

| Weapon | Base | |
|---|---|---|
| Guns (heavy/light) | 10% | Reduced −25% if ship lacking manpower, −50% if lacking organization |
| Torpedoes | 10% | Same penalties |
| Depth charges | 11% | Same penalties |

### Ship hit profile

```
hit_profile_ship = 100 × visibility / (0.5 × speed + 20)
```

Submarines use **sub visibility** (even when revealed). Convoys always have **hit_profile = 85**.

### Weapon hit profiles

| Weapon | Hit profile |
|---|---|
| Light Guns | 45 |
| Heavy Guns | 70 |
| Torpedoes | 100 |
| Depth Charges | 100 |

### Final hit chance calculation

```
hit_chance = max(base_hit_chance × modifiers × min((hit_profile_ship / hit_profile_weapon)², 1.0), 2%)
```

A weapon suffers penalties against ships with smaller hit profiles. Modifiers come from: weather, night (−25% naval hit), screening efficiency, fire control modules, radar, military industrial traits, officer corps spirits, admiral skill level and traits (Torpedo Expert, Destroyer Leader, etc.).

**Practical scaling:** +4% speed ≈ +1% effective HP; −1% visibility ≈ +1.1% effective HP.

### Worked example

1936 light cruiser, 15 surface visibility, 32.0 kn speed:
- **Hit profile:** 100 × 15 / (0.5 × 32 + 20) = 41.7
- Fired upon by another 1936 LC with light battery, basic fire control, no other mods
- **Base hit chance:** 10% × (41.7/45)² = **8.6%** (floor 2% minimum applies)
- With Night Fighting spirit (−5% visibility = 14.25 visibility, profile 39.6): **7.7%** hit chance

## Armor and piercing

Armor and piercing affect damage multiplier and critical hit chance for gun attacks (heavy and light). Torpedoes ignore armor entirely but some armor modules reduce torpedo damage and critical hit chance.

| Piercing:Armor ratio | Damage multiplier | Critical hit chance multiplier |
|---|---|---|
| ≥ 2.0 | 1.0× | 2.0× |
| 1.0 ≤ ratio < 2.0 | 1.0× | 1.0× |
| 0.75 ≤ ratio < 1.0 | 0.7× | 0.75× |
| 0.5 ≤ ratio < 0.75 | 0.4× | 0.5× |
| 0.1 ≤ ratio < 0.5 | 0.3× | 0.1× |
| < 0.1 | 0.1× | 0.0× |

## Damage

### Damage formula

Weapon-type damage is modified by:

- Doctrines
- Naval terrain
- Weather
- Pride of the Fleet (if present)
- Admiral skills and traits
- Bad positioning: up to **−50%**
- Enemy admiral Defense: further reduction

If armor cannot be pierced, damage is reduced by up to **−90%**.

Damage is **randomized with ±2.5% to +47.5%** modifier.

### HP and organization damage split

- **60% to HP (strength)**
- **100% to organization**

Ships start **immune to organization damage**, scaling up to nominal value as HP decreases. Example: ship with 100/50 HP/Org receives multiple 50-damage hits:
- Hit 1: 30 HP, 0 Org damage
- Hit 2: 30 HP, 15 Org damage
- Hit 3: 30 HP, 30 Org damage
- Hit 4: 30 HP, 45 Org damage (sinks)

## Critical hits

### Critical hit chance

- **Torpedoes:** 10% base
- **Guns (heavy/light):** 5% base, scaled down to 0% at 100% reliability; increased if armor cannot be pierced

Marksman and Crisis Magician admiral traits modify critical hit chances independently of weapon type.

### Critical hit damage

If a critical hit occurs, there is a **10% chance** it damages a critical part (10% for aerial attacks as well). This chance is **inversely scaled by reliability**: at 25% reliability, the chance becomes 10% ÷ 25% = 40%.

If a critical part is not hit, a regular critical occurs with damage bonus **1×** (at 100% reliability) to **5×** (at 0% reliability), scaling linearly. **Torpedoes always have 2× bonus regardless of reliability.**

### Critical parts table

| Critical part | Prerequisite | Weight | Damage modifier | Status effects |
|---|---|---|---|---|
| Magazine Hit | — | 0.1 | 10× Org, 10× HP | Heavy −70%, Light −70%, Torpedo −70% |
| Heavy Fires | — | 1 | 2× Org, +5 Org | Org −50%, Recovery −80% |
| Broken Propeller | — | 0.5 | 0.5× Org, 0.5× HP | Speed −90% |
| Rudder Jammed | Not Carrier | 0.25 | 0.25× Org, 0.25× HP | Retreat decision −90%, Speed −50% |
| Ballast Tanks Inoperable | Submarine | 1 | 0.25× Org, 0.25× HP | Sub visibility +66% |
| Main Battery Turret Destroyed | Has heavy batteries | 1 per battery | — | Heavy attack −50% |
| Main Battery Mount Disabled | Screen/deck gun | 1 per gun | — | Light attack −50% |
| Torpedo Tubes Disabled | Has torpedoes | 1 per tube | 1.25× Org, 1.25× HP | Torpedo attack −50% |
| Secondaries Knocked Out | Has secondary batteries | 1 per battery | — | Light attack −25% |

## Naval strike (air attack phase)

Every 8 hours (04:00, 12:00, 20:00), planes can sortie. **Carrier-based planes sortie every 6 hours**, with **−100% carrier traffic at night** unless mitigated (e.g., CAG Night Fighting officer corps spirit).

Maximum external planes eligible:
```
external_planes = min(sum_of_enemy_current_HP × 0.05 × (1 + 0.2 × combat_days), 20)
```

(At least 20 planes always eligible.)

### Phase 0: Air combat and disruption

If enemy fighters are present, they engage the bombers and can disrupt them before reaching targets. See Air combat article.

### Phase 1: Naval strike target selection

The bombers' target is randomly selected from a weighted distribution:

**Base weight = each ship's maximum HP** (excludes hidden submarines). Scaled by ship type:

| Ship type | Multiplier |
|---|---|
| Submarine | 10× |
| Screen | 10× |
| Capital ship | 50× |
| Carrier | 200× |

**Damaged ships:** weight increases by up to **+500%** as they approach 0% HP.

**Anti-air penalty:** if a ship's AA attack < 5, weight increases by **(5 × (5 − AA))×**. Example: convoys (0.2 AA) get +24× multiplier, making them attractive targets that draw fire from more valuable ships.

### Phase 2: Ship anti-air defense

A targeted ship can preemptively retaliate. Against non-kamikaze air wings:

```
preemptive_retaliation_chance = 20% × max(0.9 − 0.02 × average_air_wing_agility, 0.01)
```

If successful, ship destroys **AA × 1%** of the planes (rounded stochastically). Plane speed and air defense stats do not affect this.

**Kamikaze attacks:** ship **always** succeeds, gets **+2 AA**, and plane losses are **×4**.

Note: only the targeted ship can retaliate with AA. This makes AA much less valuable on screening ships expected not to be targeted.

### Phase 3: Naval strike attack and damage

**Hit ratio:**
```
hit_ratio = (naval_targeting / 10) × 30%, capped 0–100%
```

**Damage reduction formula:**
```
damage_reduction = max(−18% × (target_ship_AA + 0.25 × sum_all_ally_AA)^0.225, −75%)
```

For convoys: target_ship_AA = 0, but convoy AA is included in the sum.

**Carrier bonus:** if planes are based on a carrier in the same naval battle, damage is **×10**.

Critical hits are calculated as for torpedoes. If the battle was a **port strike**, naval base damage is proportional to ship damage dealt.

**Note:** targeted ship's AA counts **5× more** than fleet AA for damage reduction; the −18% coefficient scales very slowly with additional AA, making AA much less valuable on ships not expected to be targeted (e.g., screens in a carrier fleet).

## Carrier-specific mechanics

### Initial stage (hours 0–6)

When a battle starts:
- Screens attack after **8 hours**
- Capital ships attack after **6 hours**
- **Carriers attack from hour 0**

Modifiers reference a **6-hour "Initial Stage"** (e.g., Surprise Attacks officer corps spirit). Carrier aircraft sortie every 6 hours but **cannot sortie at night** without CAG Night Fighting.

For a fleet with much stronger carrier force, the carrier-only opening can cause devastating alpha strike, snowballing as enemy damage falls with reduced org. However, if the battle starts at night or in storm, this stage is wasted (carrier traffic −100% or severely reduced).

### Carrier light attack restrictions

Carriers cannot use light attack to target enemy carriers or convoys (including enemy convoys), even if equipped with secondary batteries. This makes "battlecarrier" designs (armored, high light attack, low deck space) far less effective than expected, especially for convoy raiding.

### Carrier veterancy

Carriers do **not** gain damage bonuses from veterancy (unlike other ships). Instead they gain **sortie efficiency penalties/bonuses**. The **carrier air wings stationed on carriers** determine damage via their own experience and veterancy. Because new air wings start at Green veterancy and lose veterancy quickly in naval battles (large losses relative to wing size), pre-training carrier air wings before engagement is important. Aces assigned to carrier air wings improve combat performance.

### Sortie efficiency

Sortie efficiency is the **percentage of carrier aircraft that can actually fly** in air missions and naval battles. Base **50%**, raised by:

| Source | Bonus |
|---|---|
| Carrier Primacy doctrine | up to +X% |
| Floating Airfield doctrine | up to +X% |
| Fleet In Being doctrine | up to +30% |
| Trade Interdiction doctrine | up to +30% |
| Base Strike doctrine | +50% |
| Political advisors, national spirits | various |
| Ship veterancy | various |
| Admiral traits (Air Controller, Flight Deck Manager) | various |
| Full carrier screening efficiency | +X% |

Sortie efficiency > 100% does not improve existing planes; it only helps when the carrier is overcrowded.

Carriers have **max aircraft capacity**. For every 1% overcrowded, sortie efficiency is reduced by **−2%** (overcrowding penalty). This can be mitigated:

- **Massed Strikes doctrine:** directly reduces overcrowding penalties
- **High sortie efficiency (>100%):** counteracts and can negate penalties

**Example:** carrier with 80 deck space, 100 aircraft (25% overcrowded = −50% sortie). With 100% base sortie, only 50% of 100 = 50 aircraft fly. With 200% total sortie, it flies 100% of 100 = 100 aircraft (penalties offset).

### Carrier stacking penalty

Each carrier exceeding a threshold (> ⚠️ broken wiki template: unrecognized define "NDefines.NNavy.CARRIER_STACK_PENALTY") per side causes a penalty to carrier wings' ability to target enemy ships. This scales to 100,000% of that side's carrier wings being unable to target. Wings unable to target still fly (subject to interception), but cannot attack ships.

**Carrier fighters are unaffected** and always target enemy aircraft.

Penalty applies from bottom of ship list upward, so carriers at the top have priority targeting. When expecting > (> ⚠️ broken wiki template) carriers, place fighter wings on lower-listed carriers and bombers on higher-listed ones.

**Note:** many cheap escort carriers (1–2 hangar space) suffer the same penalties as full carriers despite far less deck space, discouraging their use.

### Carrier aircraft research

With **Man the Guns:** land-based aircraft model must be researched, then carrier-capable version researched separately (Fighters, CAS, Naval Bombers only). Carrier model has different name, artwork, and stats.

With **By Blood Alone:** researching any light airframe grants its carrier-capable version, from which buildable variants are created.

When a new carrier is produced, default aircraft are customized in naval section via dockyard assignment. Once finished, carrier fills with latest available models. Replacements/reinforcements are produced via military factories and manipulated by selecting the carrier(s) and clicking the airplane button next to their location.

### Carrier deployment

When a fleet is on patrol, carrier wings automatically participate as a **Carrier Air Group** in any naval combat (no specific orders needed). To use carriers as floating air bases with standard air missions, they must be **at sea (not in port)** and **not on naval mission**. Fighter wings may be on interception in one region while bombers target adjacent regions (e.g., supporting an amphibious landing).

## Related files

- [naval-missions.md](naval-warfare-overview.md) — fleet orders and patrol zones
- [ship-designer.md](ship-designer.md) — ship construction and customization
- [naval-doctrine.md](naval-doctrine.md) — doctrine effects on naval combat
- [air-combat.md](../03-air-warfare/air-combat.md) — fighter interception during naval strikes
