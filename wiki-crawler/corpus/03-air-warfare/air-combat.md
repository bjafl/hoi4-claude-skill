---
title: Air Combat
category: mechanics
tags: [air, air-combat, detection, disruption, agility, air-attack, air-defense, anti-air, aces, carrier-air, experience]
game_version: "1.19"
dlc: []
sources:
  - https://hoi4.paradoxwikis.com/Air_combat
  - https://hoi4.paradoxwikis.com/Air_warfare
  - https://hoi4.paradoxwikis.com/Air_missions
---

## Summary

Air combat ticks **every 8 hours** (08:00, 16:00 and 24:00 local time). Each tick runs three phases in order — air-to-air combat, escort/loss tallying, and the ground mission — and each phase is fully resolved from one country's perspective before the next country's. Understanding which stat matters in which sub-phase is what tells you whether to build agility, speed, attack or defense on a given airframe.

---

## Phase order

1. **Air-to-air combat** — detection → damage → disruption
2. **Escort and equipment loss** — escort protection → plane losses
3. **Ground mission** — state AA → naval/divisional AA → disruption negation → mission effect

---

## Phase 1 — Air to air combat

Own wings attack every enemy wing operating in the same air region: directly damaging them, and additionally **disrupting** those on ground missions. "Enemy" includes anyone this country (or the host country of its air volunteers) is at war with.

### Sub-phase 1: Detection

**Friendly planes that can attack are capped at 3× the number of detected enemy planes.** Poor detection therefore idles most of a large air force, especially when the enemy is few in number.

Detection chance = the percentage of enemy planes in the region that are visible.

**Additive sources:**

| Source | Maximum contribution |
|---|---|
| Occupation — controlling land in the strategic region (ground spotting) | +10% at full control |
| Radar coverage | +50% at full coverage |
| Own planes operating in the region | +80% at 3000 planes; **non-fighters count at only 50% efficiency** |

**Then multiplied down by time of day and weather:**

| Source | Effect |
|---|---|
| Night-time | −20% detection |
| Bad weather | up to −90% detection |

**Situational visibility adjustments to the enemy side:**

- If the enemy fields both ground-mission planes and superiority/escort fighters, the **fighters are fully visible** regardless of detection. They need not belong to the same country as the bombers.
- Regular bombers on **strategic bombing** and **carrier-based bombers** cut their own visibility via the **Strategic bombing visibility** modifier (e.g. the **Infiltration Bombing** air doctrine).
- Planes on **close air support are 2× as visible** (capped at 100%).
- Planes on **port strike are 10× as visible** (capped at 100%).

**Sortie ordering.** Wings sortie in **descending order of air attack and agility**. When enemy visibility limits the number of attacking slots, your best wings fly and your worst sit out.

**Allocation.** Each sortieing wing's planes are allocated against enemy wings **proportional to those wings' visibility** — for damage against all wings, and for disruption against ground-mission wings.

> Worked example from the wiki: eight full fighter wings plus one CAS wing (double visibility) face an equal opponent at full detection. Each wing sends 10 planes against each enemy fighter wing and 20 against the enemy CAS wing. At lower detection the CAS wing receives fewer attackers while escorting fighters keep full visibility. At roughly 30% detection, visibility is low enough that some planes cannot attack at all — the CAS wing drops out first, then the fighter wings with the worst stats.

### Sub-phase 2: Damage

Unless the defender's air defense is zero:

```
Planes destroyed = max(
    (base damage − agility mitigation + bonus from relative speed + bonus from absolute speed)
    × 0.01 × carrier factor / air defense,
    0.001 )
```

| Term | Formula |
|---|---|
| base damage | `number of attackers × air attack × 0.2` |
| agility mitigation | `round( base damage × 0.45 × max( min(defender agility / attacker agility, 4) − 1, 0 ) )` |
| bonus from relative speed | `round( base damage × 0.65 × max( min(attacker speed / defender speed, 3.5) − 1, 0 ) )` |
| bonus from absolute speed | `round( base damage × 0.025 × min(attacker speed, 800 km/h) / 100 km/h )` — **only if attacker speed > defender speed**, otherwise 0 |
| carrier factor | **5** if both attacker and defender are carrier-based, otherwise **1** |

**If the defender's air defense is zero, all planes are destroyed.**

**What each stat does:**

| Stat | Role |
|---|---|
| **Air attack** | linear driver of base damage — the primary offensive stat |
| **Agility** | purely defensive in this formula; mitigates incoming damage. Capped benefit at **4× the attacker's agility** (i.e. 4:1 ratio gives the max −45%×3 = −135% of base damage reduction term) |
| **Speed** | purely offensive: two separate bonuses. Relative-speed bonus caps at a **3.5× ratio**; absolute-speed bonus caps at **800 km/h** |
| **Air defense** | divides all incoming damage — the primary survivability stat, and dominant for bombers |

**Practical reading:**
- Against *bombers* (slow, unagile), your **speed** ratio is large and their **agility** is low → guns/air attack and speed dominate. This is why heavy fighters and cannon-armed interceptors do well versus bombers.
- Against *fighters*, agility ratios matter far more, and mutual speed cancels out.
- **Carrier vs. carrier combat multiplies damage 5×** — carrier air battles are extremely lethal and resolve fast.

### Sub-phase 3: Disruption

Wings on **air superiority** or **interception** mission disrupt enemy wings on ground missions.

```
Disruption = number of attackers
           × (1 + agility factor) × (1 + attack factor)
           × (1 + speed factor)   × (1 + detection factor)
           × carrier factor
```

| Component | Value |
|---|---|
| agility factor | attacker's agility × **0** (i.e. no effect) |
| attack factor | attacker's attack × **0** (i.e. no effect) |
| speed factor | attacker's speed ÷ 800 |
| detection factor | detection chance × 1 |
| carrier factor | **4** normally, **6** if both attacker and defender are carrier wings |

Which reduces in practice to:

```
Disruption = number of attackers × (1 + speed/800) × (1 + detection chance) × carrier factor
```

**Only plane count, speed and detection matter for disruption.** Detection is doubly critical: it both raises the number of fighters allowed to act and multiplies each one's disruption effect.

---

## Phase 2 — Escort and equipment loss

### Sub-phase 1: Protection from escorts

Fighters on **air superiority/escort** mission cancel disruption inflicted on your bombers. **Bombers of allied countries are not escorted** — only your own.

```
disruption reduction ratio =
    2 × number of escorts × (1 + speed/800) × (1 + agility/100) × (1 + attack/100) × (1 + detection)
    ÷ total disruption amount
```

| Component | Value |
|---|---|
| base | 2 |
| speed factor | speed ÷ 800 |
| agility factor | agility ÷ 100 |
| attack factor | attack ÷ 100 |
| detection | detection chance |

This ratio is removed from the disruption received by **all** your bomber wings.

> ⚠️ Wiki notes a quirk: the number of active escort planes is **not recalculated** for this phase — it is reused from wherever the previous phase's last-processed country left it, so some countries get arbitrarily worse escort efficiency. Treat escort strength as unreliable at the margins.

### Sub-phase 2: Losses from air-to-air combat

- **Each point of damage received = one airplane lost.**
- Damage is **rounded statistically**: 1.2 damage → 1 plane lost 80% of the time and 2 planes 20% of the time, averaging 1.2 losses per sortie.
- If a wing lost at least one plane and has an ace, the ace may die (see [Aces](air-warfare-overview.md#aces)).

---

## Phase 3 — Ground mission

Surviving planes on ground missions (CAS, strategic bombing, naval strike, etc.) now execute. **Accumulated disruption reduces their effectiveness.** Wings can take further losses here from state, naval or divisional anti-air.

All ground missions except **paradrop** and **mine planting/sweeping** need a specific target. If multiple missions are selected the game tries them in this order:

1. Close air support
2. Strategic bombing
3. Naval bomber / kamikaze
4. Port strike
5. Air supply

**Only the first category producing a valid target is used**, but a single wing can service multiple targets within that one category in one sortie — so you do **not** need to split wings to support several land combats. Conversely, a large naval bomber wing that used part of itself on a naval strike **cannot** send the remainder on a port strike.

**Night-time** applies a **−50% Ground Bombing Targeting** modifier, giving a corresponding probability that the wing simply fails to find its target. It is still exposed to anti-air.

### Sub-phase 1: State anti-air

Affects **strategic bombing, port strike and air supply** missions.

```
C (chance of a damage event) = 10% × (1 + hit chance modifier) × anti-air factor
```

If a random number R (0.0%–100.0%) is below C, a hit occurs:

```
D (planes destroyed) = max( 1,
      0.8 × anti-air factor × number of planes × R × (1 + damage modifier)
      ÷ (C × air wing's defense) )
```

Averaging R to C/2:

```
D ≈ max( 1, 0.4 × anti-air factor × number of planes × (1 + damage modifier) ÷ air wing's defense )
```

| Component | Value |
|---|---|
| damage base chance | 10% |
| hit chance modifier | "Static Anti Air hit chance factor" — **+20% each** from **Centimetric Radar**, **Phased Array**, **Monopulse Radar** |
| damage factor | 80% |
| anti-air factor (strategic bombing, port strike) | average AA building level in **enemy states in the strategic region** ÷ 5 |
| anti-air factor (air supply) | AA level of the **target's state** (even if friendly) ÷ 5 |
| damage modifier | "Static Anti Air damage factor" — **+10% each** from **Improved Anti-Air** and **Advanced Anti-Air** |
| divisor | the air wing's **air defense** stat |

**Consequence:** because of the `max(1, …)` floor, **small wings and high-defense strategic bombers are frequently reduced to the minimum one loss per hit.** High air defense on bombers is what neutralises state AA.

### Sub-phase 2: Naval and divisional anti-air

- **Close air support** wings face enemy **divisional AA**. Anti-air is averaged over all divisions on the enemy side including reserves; damage reduction caps at **75%**, reached at **4.3 average anti-air attack**. Divisional AA has a **7% chance** to shoot planes down, killing up to **0.5% × (air attack)** of the attackers (random up to that, ≈ half on average) but **always at least one plane**. **No plane attribute affects this** — you cannot design around divisional AA.
- **Naval strike / kamikaze / port strike** wings face **ship anti-air**.

### Sub-phase 3: Disruption negation

The ground-mission wing can negate whatever disruption survived the escort phase, using its own stats.

```
disruption damage factor = 100% − sqrt(
      disruption
    ÷ ( 10 × number of planes × (1 + defense/200) × (1 + attack/200) × (1 + speed/800) ) )
```

| Component | Value |
|---|---|
| disruption | value after the escort phase |
| defense factor | air wing's **air defense** ÷ 200 |
| attack factor | air wing's **air attack** ÷ 200 |
| speed factor | air wing's **speed** ÷ 800 |
| number of planes | wing size, **not** reduced by mission efficiency |

The figure reported as "Planes disrupted" in a region's statistics is `number of planes × (1 − disruption damage factor)`, accumulated over all missions and sorties in the window.

**Guided missiles always have a disruption damage factor of 100%, negating all disruption applied against them.**

**Design consequence:** giving bombers air defense, air attack and speed is not just about surviving — it directly buys back mission output that enemy fighters stripped away.

---

## Anti-air interaction summary

| AA source | Affects | Key numbers |
|---|---|---|
| **State anti-air building** (max level 5) | strategic bombing, port strike, air supply | −5 enemy air power per level (max −25); hit chance 10% × AA level/5; damage scales with AA level and inversely with wing air defense; also absorbs bombs away from factories |
| **Divisional anti-air** (line AA / Support Anti-air) | close air support | up to **−75%** CAS damage at 4.3 average air attack; 7% chance to kill up to 0.5% × air attack of attackers, minimum 1 plane; also cuts hostile air superiority penalties to a floor of 0.25× |
| **Naval anti-air** | naval strike, kamikaze, port strike | resolved in naval battle rules |
| **Radar techs** (Centimetric, Phased Array, Monopulse) | state AA hit chance | +20% each |
| **Improved / Advanced Anti-Air techs** | state AA damage | +10% each |

---

## Carrier air

- Carriers act as floating air bases; capacity = the ship's **deck space** stat. Most carriers take **carrier-capable aircraft only**; **ice carriers** take all types.
- **Carrier wing size is 10 planes** (land wings are 100).
- Planes on a carrier automatically join naval battles when idle and/or when the task force is on a mission. Wings on a carrier **on hold outside port** can fly ordinary air missions like any land-based wing.
- **Carrier factor multipliers:**

| Situation | Multiplier |
|---|---|
| Damage, both attacker and defender carrier-based | **×5** |
| Disruption, normal combat | ×4 |
| Disruption, both attacker and defender carrier-based | **×6** |

- Overcrowding a carrier applies the same −2%-per-1% penalty as a land base, but it is reduced by the **Massed Strikes** naval doctrine and can be offset in naval battles by >100% sortie efficiency.
- Rebasing between land bases and carriers (either direction) costs a **48-hour block on reinforcement**.
- Ace bonuses scale inversely with wing size, so a 10-plane carrier wing gets **10× the ace effect** of a 100-plane land wing. Ace generation chance for a full carrier wing is ≈ **2.0890%** per qualifying sortie versus 2.9775% for a full land wing.

---

## Ground crews and airfield effects

These are the levers that change combat output without changing the planes:

| Lever | Effect |
|---|---|
| **More Ground Crews** (toggle in strategic air map mode) | **+10% mission efficiency** in the region, applied **multiplicatively**; also **+10%** to air supply delivered |
| **Air base level** | 200 plane capacity per level, max level 10 = 2000 planes |
| **Overcrowding** | −2% per 1% over capacity; **−100% at 50% over** — nothing flies |
| **Air base damage** (from strategic bombing) | reduces capacity until repaired, which can push a base into overcrowding |
| **Base position within the region** | wings whose range does not cover the whole region take a penalty proportional to uncovered provinces |
| **Fuel shortage** | reduces mission efficiency **and** proportionally reduces both wing and country experience gain |
| **Weather** | reduces detection and efficiency, raises take-off/landing accident risk; also reduces the number of CAS attacks |

---

## Experience

Wings gain **wing experience** for themselves and **air experience** for the country.

**Wing experience:**

| Source | Gain |
|---|---|
| Taking part in air-to-air combat — **any** wing present, even if not selected to deal damage | 0.8 |
| Completing a ground mission | 0.28 |

Air-to-air wing XP is reduced if there are not enough enemy planes for all your planes to attack.

**Country air experience, per effective plane:**

| Source | Gain per effective plane |
|---|---|
| Air-to-air combat | 0.0004 |
| Close air support | 0.0005 (only planes that actually joined land combats) |
| Strategic bombing | 0.0002 |
| Paradrop | 0.03 (only planes actually needed for the drop) |

A wing in air-to-air combat also gains **the same amount again for each country attacking it** — an air force fought by several countries earns a multiple of the experience.

> ⚠️ The wiki is self-contradictory here: the air-to-air rate is stated as **0.0004 per effective plane**, but the worked example below uses **0.001**. Treat the exact constant as uncertain; the *structure* (one payout for fighting, one more per attacking country) is reliable.

**Fuel:** lacking fuel reduces both wing and country experience proportionally.

**Lend-lease:** if a wing contains aircraft produced by another country and that country currently sends lend-lease, that country gains **up to 50%** as much country air experience, scaled by the proportion of its equipment present. This shared XP is **not** further shared with attachés and does **not** reduce the operating country's own experience.

**Wiki worked example.** The UK flies 100 strategic bombers over West Germany at 90% mission efficiency; 40% are US-made with an active US lend-lease; German and Italian fighters intercept.

| Source | UK air experience |
|---|---|
| Air-to-air fight | 100 × 90% × 0.001 = +0.09 |
| Being attacked by Germany | +0.09 |
| Being attacked by Italy | +0.09 |
| Strategic bombing | 100 × 90% × 0.0002 = +0.018 |
| **Total** | **0.288** |

The USA receives 50% × 40% = **20%** of that, i.e. **0.0576**.

---

## See also

- [Air warfare overview](air-warfare-overview.md) — bases, wings, missions, air superiority, aces
- [Aircraft designer](aircraft-designer.md) — which stats to build for each role
- [Air doctrine](air-doctrine.md) — modifiers that feed these formulas
