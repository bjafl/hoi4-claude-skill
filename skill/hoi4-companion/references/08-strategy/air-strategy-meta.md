---
title: Air Strategy Meta
category: strategy
tags: [air, strategy, aircraft-design, air-superiority, interception, meta, design-patterns, cost-efficiency]
game_version: "1.19"
dlc: [By Blood Alone]
sources:
  - https://hoi4.paradoxwikis.com/Air_warfare
  - https://hoi4.paradoxwikis.com/Air_combat
  - https://hoi4.paradoxwikis.com/Aircraft_designer
  - ../03-air-warfare/air-warfare-overview.md
  - ../03-air-warfare/air-combat.md
  - ../03-air-warfare/aircraft-designer.md
---

## Summary

Air superiority is won by controlling detection and disruption, not by building expensive designs. Fighter-to-fighter combat is dominated by air attack (not agility), and bombers are countered either by interceptors with speed/cannons or by high air defense on the bombers themselves. The meta shifts by war era: early games reward cheap, numerous fighter wings to seize detection advantage; mid-war favours agile designs with extra fuel tanks; late war enables stacking of specialized modules and high-end engines to overcome state AA and fighter opposition.

---

## The detection problem and its solution

**Inferred:** The single most consequential mechanic is the detection cap: *friendly planes that can attack are capped at 3× the number of detected enemy planes*. A player with 500 fighters facing a defender with 100 enemy fighters can only use 300 of their own planes, leaving 200 idle and granting no advantage. This is why detection and large, cheap wings matter more than perfect designs.

Detection sources (additive, capped after weather):

| Source | Maximum | Notes |
|---|---|---|
| Occupying the strategic region | +10% | Requires full control of all land in the region |
| Radar coverage | +50% | Available from early game via tech tree |
| Own planes operating there | +80% | Non-fighters count at only 50% efficiency |

At night, detection is reduced by 20%; in bad weather, up to 90%. **Inferred:** Early-war players should rush radar techs — a fighter player can go from 0% to 50% detection alone, then add ground occupation and any friendly planes present. This immediately makes a 300-plane wing worth flying when previously only 100 were effective.

---

## Air attack vs. agility: the damage formulas matter

Air-to-air damage formula (simplified):

```
Planes destroyed = max(
    (base damage − agility mitigation + speed bonuses) × 0.01 / air defense,
    0.001 )
```

where `base damage = attackers × air attack × 0.2`.

Agility only mitigates incoming damage; it does **not** improve damage you deal. **Inferred:** in fighter-vs-fighter dogfights, this matters less than it seems — air attack is the primary offensive stat. The ratio `attacker agility / defender agility` is capped at 4:1, and mitigation maxes out at `−45% × 3 = −135%` of base damage (scaled back).

**Inferred:** against *bombers*, agility is nearly worthless because:
- Bombers are slow (200–400 km/h base); your speed ratio is large (3.5× ratio bonus caps).
- Bombers are unagile (20–40 agility); the agility ratio is large but capped.
- Your speed bonus dominates their agility mitigation.

This is why interceptors with guns and speed beat strategic bombers, and why building a "fast, agile interceptor" wastes points on agility.

**Inferred:** Speed bonuses are purely offensive and come from:
- Relative speed ratio (attacker speed / defender speed, capped at 3.5×).
- Absolute speed bonus (capped at 800 km/h).

On a 1936 fighter with a 400 km/h base speed, a 1936 interceptor also at 400 km/h sees your speed bonus drop to zero. On a 1940 interceptor at 500 km/h, the bonus is `round( base damage × 0.65 × min(500/400, 3.5) − 1 ) = round( base damage × 0.65 × 0.25 )` — large. **Inferred:** Speed tiers matter enormously in specific matchups; always check what you are fighting.

---

## Carrier air is a separate game

Carrier combat multiplies damage by **5× when both attacker and defender are carrier-based**, compared to 1× for land-based combat. Carrier disruption is multiplied by **6× (both carrier) vs. 4× (normal)**. **Inferred:** carrier air battles resolve in 1–2 sorties instead of 10+. This means:

- **Carrier wings are lethal in pure carrier-vs-carrier duels.** A single wing of 10 planes can deal fatal damage in one sortie.
- **Carrier air defense is therefore critical.** The difference between 22 and 54 air defense on a carrier fighter wing determines whether you lose 3 planes or 7 in a duel.
- **Ace stacking on tiny carrier wings is broken.** A 2-plane carrier wing gets **50× ace bonus** (inverse of size), turning a "Good" ace's +3% Air Attack into +150%.

**Inferred:** If pursuing a strong carrier navy, hire a Naval Aircraft Designer company early; it buffs carrier fighters (+10% Agility, +10% Range), carrier CAS, carrier naval bombers, and carrier NAV simultaneously. A Medium Aircraft Designer is the alternative (buffs reliability), but Naval is stronger because the range and agility directly feed combat output.

---

## War era designs: 1936–1944

### Early war (1936–1938): Cheap, numerous fighters

**Inferred:** The early game is dominated by who can field the most fighters fastest. Production is cheap (5–10 production cost per plane), and research is fast. The standard build is:

| Slot | Module | Rationale |
|---|---|---|
| Frame | Basic Small Airframe | 40 agility, 9 air defense; cheapest viable path |
| Engine | 1x Engine II | +20% Max Speed; costs 14, unlocked by Engines II tech |
| Primary | 4x Heavy Machine Gun | +18 air attack, no agility penalty; costs 2 production |
| Special | Self Sealing Fuel Tanks | +6 air defense for 1 weight; frontloads survivability |

**Stats: Agility 40, Air Attack 18, Air Defense 15, Speed +20%.**

**Production: 5 (frame) + 14 (engine) + 3 (guns) + 1 (tanks) = 23 production cost.**

**Inferred:** Do not build canon planes yet; MG guns are cheaper and the air attack difference is small (+20 vs +18). Self Sealing Fuel Tanks are the best armor value (6 air defense per weight) and cost only 1 production and 1 rubber. Skip agility — the 45 agility of Improved Small Airframe is not worth the cost.

Build 8–12 wings (800–1200 planes) by late 1937, then begin transitioning to Improved Small Airframe designs with 1x Engine III once the tech lands. A player who fields 1000 fighters early on will detect enemy bombers and control air superiority through sheer volume.

### Mid-war (1938–1942): Fuel tanks and agility

Once Improved and Advanced Small Airframe tech land, add Extra Fuel Tanks to extend range. **Inferred:** Range shortfall cuts mission efficiency multiplicatively (proportional to uncovered provinces in the strategic region). A fighter whose range does not cover the whole region is effectively grounded in the centre.

| Slot | Module | Rationale |
|---|---|---|
| Frame | Improved Small Airframe (agility 45) or Advanced (agility 50) | +5 agility per jump; Extra Fuel Tanks fit here |
| Engine | 1x Engine III → IV | +30% → +45% Max Speed |
| Primary | 2x Cannon I or 4x Heavy MG | Cannon I: +20 air attack, −2 agility (net agility 43–48). MG: +18, no penalty |
| Special | Self Sealing Fuel Tanks | +6 air defense |
| Special | Extra Fuel Tanks | +50% range; −2 air defense but usually worth it |

**Inferred:** Cannon I starts to pay off here. The −2 agility is a small cost when your frame agility has climbed to 45+. Medium Airframe heavy fighters (25–40 agility) also start production around 1939–1940, enabling a separate air-superiority role specialized in bomber interception: frame at 30–40 agility means cannon penalties hurt less, and the frame's higher air defense (18–24) makes them harder to kill.

### Late war (1943–1945): High air defense and specialization

**Inferred:** By 1943, state AA and enemy fighters are abundant enough that generic "good at everything" designs become liabilities. Specialize:

**Anti-bomber interceptor (Modern Small Airframe + Cannon II):**

| Component | Value | Rationale |
|---|---|---|
| Frame | Modern Small Airframe | 55 agility, 18 air defense; range 900 km |
| Engine | 1x Axial Jet Engine | +70% Max Speed, −30% range; 900 km / 0.7 = 1286 km net range |
| Primary | 2x Cannon II | +24 air attack, −1 agility; best attack-per-agility-loss ratio in the game |
| Electronics | Air-Air Radar II | Night penalty −40%; applies on Interception |
| Special | Self Sealing Fuel Tanks | +6 air defense |
| Special | Armor Plates | +4 air defense, −10% range |
| Turret | Cannon Defense Turret | +4 air defense, +3 air attack, −3.7% Max Speed |

**Final stats: Agility 54, Air Attack 27, Air Defense 35 + 4 + 6 = 45, Range ~1100 km, Production cost ~70.**

Against 1940 bombers (Agility 30, Air Defense 35), this fighter's 54 agility reduces incoming damage by `min(54/30, 4) − 1 = 1.8×`, and the cannon air attack of 27 drives base damage up 35% vs earlier designs. Radar ensures interception works at night.

**Strategic bomber (Advanced Large Airframe):**

Strategic bombers should maximize air defense to survive state AA. The state AA hit formula floors damage at 1 plane, but high air defense makes this floor hit less often: `damage ≈ 0.4 × anti-air factor × planes ÷ air defense`. An air defense of 50 reduces damage by 50×.

| Component | Value | Rationale |
|---|---|---|
| Frame | Advanced Large Airframe | 35 agility, 50 air defense; weight 22 |
| Engine | 4x Engine IV | +45% Max Speed, Thrust 75; heaviest bombers need this |
| Primary | Large Bomb Bay | +15 Strategic Bombing, −15 agility; weight 2 (8 on mission) |
| Slot | Self Sealing Fuel Tanks | +10 air defense |
| Slot | Bomb Sights II | +6 Strategic Bombing; no weight |
| Slot | Radio Navigation II | +6 Strategic Bombing, −20% night penalty |
| Turret | Cannon Defense Turret 2x | +8 air defense |

**Final stats: Air Defense 50 + 10 + 8 = 68, Strategic Bombing 15 + 6 + 6 = 27, Production cost ~130.**

Against enemy state AA with level 5 (anti-air factor = 1.0), damage is `0.4 × 1.0 × planes ÷ 68 ≈ 0.006 × planes`, so 100 bombers lose 0.6 planes per 8-hour tick. A wing of 50 bombers loses ~0.3 planes per sortie — manageable. Reduce air defense to 30 and the wing loses 1 plane per sortie.

**Inferred:** High air defense on strategic bombers is not optional in late war. It is the only stat that protects against state AA.

---

## Close air support: cheap and numerous

The CAS damage formula is `ground attack × number of planes × 0.035 to organisation and strength`. **Inferred:** CAS damage scales linearly with plane count, not quadratically. A 100-plane CAS wing deals twice the damage of a 50-plane wing, but also costs twice as much. Divisional AA cannot be designed around (no plane attribute affects it), so the correct strategy is maximum ground attack for minimum cost.

**Rocket Rails meta (1936+):**

| Slot | Module | Cost | Ground Attack | Agility penalty |
|---|---|---|---|---|
| Primary | Heavy Bomb Locks | 1 production | +8 | −20 on mission |
| Slot 2 | Rocket Rails | 1 production | +4 | none |
| Slot 3 | Rocket Rails | 1 production | +4 | none |

**Basic Small Airframe + Heavy Bomb Locks + 2x Rocket Rails = 6 + 1 + 1 + 1 = 9 production cost, Ground Attack 8 + 4 + 4 = 16 on mission.**

**Inferred:** This is the cost-optimal CAS plane. Do not use Anti-Tank Cannons (weight 8, +8 ground attack) when two Rocket Rails (weight 0, +4 each = +8 total) cost the same production and save weight. Build dozens of these, not single wings of expensive medium bombers.

---

## The interception trap

**Inferred:** Interception is not a winning strategy; it is a holding pattern. Interceptors take off only when enemy bombers are detected, take far fewer losses than air superiority wings, but **contribute zero to regional air superiority**. If the enemy has air superiority, their land forces get −7% defense / breakthrough (at 60% enemy superiority), and interception alone cannot remove this.

Use interception only when:
- You are losing the air superiority contest and cannot afford more wings.
- The enemy is flying unescorted bombers that you can detect reliably.
- You are defending specific high-value targets (a strategically bombed region).

Otherwise, fly air superiority. If detection is the problem, upgrade radar instead of switching missions.

---

## Doctrine and research priorities

**Inferred:** Air doctrine multiplies final air support penalty by `(1 + doctrine bonus)`. The **Battlefield Support** line gives +30% air superiority bonus to air combat, multiplying the −7% (60% superiority) defense penalty to −9.1%. This is significant but not gamechanging; prioritize production and design over doctrine early.

For **By Blood Alone** aircraft designers:
- **Light Aircraft Designer** is the default for fighter-heavy nations (agility +10%, Max Speed +10% on fighters and carrier fighters).
- **Heavy Aircraft Designer** (+10% Strategic Bombing) is only worth hiring if you are committing to 200+ strategic bombers.
- **Naval Aircraft Designer** is strongest for carrier navies; it buffs three plane types at once.

---

## The momentum problem: how air wars end

**Inferred:** Air superiority compounds. A player with 60% air superiority accumulates experience faster, fields more veteran aces, and researches air techs faster. A player with 40% superiority loses planes faster and falls further behind.

To break an enemy's air momentum:
1. **Upgrade radar tech** to +50% detection; even 50% is huge.
2. **Build cheap wings in parallel** while transitioning frame designs; double production output for one turn.
3. **Rebase closer to contested regions** if you control air bases inside them; range shortfall is crippling.
4. **Switch to a superior matchup** if possible — late-war interceptors beat mid-war fighters despite the fighter being newer.
5. **Upgrade to a new engine generation** (Engine III → IV, or any jet engines) in one design at a time; each wing refit costs only 3 air XP per plane, not 6.

**Inferred:** Once a player is behind 3+ air wings on design tech, climbing back is nearly impossible in active warfare. Prioritize air early and often.

---

## See also

- [Air warfare overview](../03-air-warfare/air-warfare-overview.md) — bases, wings, missions, air superiority, aces
- [Air combat](../03-air-warfare/air-combat.md) — combat resolution, damage formulas, anti-air interaction
- [Aircraft designer](../03-air-warfare/aircraft-designer.md) — modular plane design (requires By Blood Alone)
