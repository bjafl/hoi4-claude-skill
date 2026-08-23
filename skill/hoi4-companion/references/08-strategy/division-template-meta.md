---
title: Division Template Meta and Era Archetypes
category: strategy
tags: [division template, 20-width, 40-width, early war, mid war, late war, template design, meta]
game_version: "1.19"
dlc: []
sources:
  - ../02-land-warfare/division-designer.md
  - ../02-land-warfare/historical-divisions.md
  - ../02-land-warfare/land-combat.md
  - ../02-land-warfare/land-doctrine.md
---

## Summary

Optimal division templates change dramatically across the game timeline, driven by how combat mechanics reward attack concentration and how technology shifts pierce requirements and unit composition. The fundamental tension between 20-width and 40-width divisions comes down to organization scaling (averaged, not additive) versus attack additivity: 40-width excels at breakthrough attack once it wins the defence race, while 20-width survives with higher org-per-width and defends efficiently. Templates within each era can be optimized for specific doctrine branches and front roles.

## 20-width vs 40-width fundamentals

**The core asymmetry:** Attack stats (soft, hard, breakthrough) are **additive** — a 40-width division has twice the attack of a 20-width. However, organization is **averaged** across all battalions, meaning adding low-org units (artillery, tanks) **reduces** division org even as it boosts attack. In combat, this creates a critical inflection point: only 10% of attacks land against enemy defence, but 40% land after defence is exhausted. An attacker that drains the defender's defence threshold faster (higher attack relative to defence) deals four times the damage per excess attack point.

| Metric | 20-width | 40-width |
|---|---|---|
| **Organization per width** | Higher — fewer low-org speciality battalions per unit of width | Lower — same spec mix costs more width |
| **Attack output** | Half of 40-width absolute value | 2× 20-width absolute value |
| **Defence breaking** | Slower to overcome enemy defence | Faster drain; concentrates force |
| **Survival in equal fights** | Better — higher org means longer time-to-break | Worse — same org spread over more width |
| **Encirclement capacity** | More divisions available for flanking and holding wider fronts | Fewer divisions; poor for line-stretching |
| **Support company efficiency** | 5 support per division means more versatility at equal width | Fewer support companies per width; non-weapon companies waste slot space |
| **Doctrine synergy** | Superior Firepower easier to scale (fewer support per width) | Mobile Warfare breakthrough multiplication benefits; Grand Battleplan's planning bonus multiplies per-division | |

**Inferred: When to use each size:**

- **20-width:** Defence-heavy playstyles, wide fronts with limited manpower, nations relying on entrenchment bonuses (Grand Battleplan, Defensive Postures). More divisions allow better encirclement pressure and garrison/garrison-flip coverage.
- **40-width:** Concentrated offensives in narrow sectors, doctrines that reward speed and breakthrough (Mobile Warfare + Armor), games where you have the industry to push superior numbers. Planning bonus and stacking bonus accumulate faster.

**Historical reference:** The historical-divisions corpus shows that **1939–1944 real divisions averaged 20–27 width** with heavy reliance on infantry and artillery. The German 1940 Infantry Division is 27 width (10 infantry + 2 artillery + 2 anti-tank in 5 combat regiments), and the Polish 1939 division is 22 width. Neither comes close to 40-width by real-world scale. **Inferred:** 40-width templates are an *optimization* for the game's combat system, not a historical playstyle.

## Combat mechanics that drive template selection

**Combat width allocation.** Each terrain sets a hard combat width cap: Plains and Desert are 70 width, Mountains and Marsh 50 width. Flanking adds width (+35 per direction on Plains), but stacking penalties kick in immediately: **−1% attack/defence per 1% of width over capacity, capped at −33%**. A 70-width Plains battle fits roughly three 20-width divisions at full width with a 9.5% penalty, or one 40-width division at −42.8% penalty (hard cap). **Inferred:** In low-width terrain and early-war low-income scenarios, multiple 20-width divisions are often forced; 40-width templates shine on Plains/Urban with multiple attackers feeding from different flanks.

**Organization collapse cascade.** When one division in a multi-division stack breaks (hits 0 org), reserves do not automatically reinforce: they enter at only **2% per hour base rate**, modified by Signal Company initiative (each 1% initiative = +0.25% reinforce rate). Defenders should **feed very low-org defenders one at a time to a rear province** so they recover while reserves slot in; otherwise all frontline divisions hit 0 org at once and the defender cannot recover. **Inferred:** For defence, many smaller divisions means more flexibility in rotating out broken units; for attack, fewer large divisions simplify the reserve-reinforcement math.

**Attack concentration and piercing.** Hard attack is affected by target hardness; soft attack is not. Piercing determines the armour bonus: insufficient piercing (less than 50% of enemy armour) cuts your damage in half. Historical infantry-only templates have 18–43 piercing from AT battalions and infantry equipment, sufficient against unarmoured targets but decimated by armoured divisions. **Inferred:** From 1943 onward, piercing becomes a mandatory template stat if the enemy has any significant tank presence; the anti-tank battalion or support company that supplies it is no longer optional.

## Early war (1936–1939): Limited armour, high organization baseline

**Tech context:** Infantry Equipment 1, Artillery 1936, Anti-Tank 1, Light Tanks 1, Horse-drawn transport standard.

**Archetype: 20–24w Pure Infantry + Support**

| Component | Ratio | Notes |
|---|---|---|
| Combat width | 22–24w | 9–10 infantry battalions in 4–5 regiments |
| Support | Engineer, Field Hospital, Support Artillery, Support Anti-Tank | 4 companies; Recon optional |
| Org (base) | 42–46 | High — 10 infantry at base org 45 each |
| Piercing | 14–22 (from rifle AT + AT battalion) | Sufficient against unarmoured targets; useless vs early armour |
| Cost (production per div) | 600–800 | Low; manpower 11k–14k |

**Why this template:** No nation has significant armour production before 1939. The historical-divisions corpus shows the Polish 1939 infantry (22w, defence 285.2, piercing 18.8) and German 1940 infantry (27w, defence 300.2, piercing 43.9) both rely entirely on infantry and AT guns for defence. Organization is the only effective survivability stat. These divisions hold the line and counterattack in narrow sectors; they avoid head-to-head attack against other infantry.

**Doctrine interaction:** Mobile Warfare's +20% planning speed and Org Loss when Moving −15% milestone make early-war infantry slightly more mobile. Superior Firepower's +10% line artillery is wasted if you only have one artillery battalion. Grand Battleplan's entrenchment bonuses start yielding returns with 2–3 points invested per division. **Inferred:** Early war favours defensive postures (Mobile Warfare + Mobile Infantry for light mobile counter-attacks, or Grand Battleplan + Defensive Postures for fortified lines).

## Mid war (1939–1942): Increased armour threat, support company standardization

**Tech context:** Infantry Equipment 1936, Artillery 1937, Medium Tanks 1939, Radio coordination 1939–1940. Armour begins appearing in significant numbers.

**Archetype A: 20w Infantry-Heavy Baseline**

| Component | Ratio | Notes |
|---|---|---|
| Combat width | 20w | 8–9 infantry battalions in 4 regiments |
| Support | Engineer, Field Hospital, Support Artillery, Support Anti-Tank, Recon (motorized) | 5 companies maxed |
| Org (base) | 42–46 | 8–9 infantry at base org 45 |
| Piercing | 25–35 (AT battalion + Support Anti-Tank) | Against early medium tanks (70–100 armour) still insufficient; −35% damage penalty |
| Hardness | 0% (no tanks) | Soft units; full damage from soft attacks |
| Cost | 800–1100 | Manpower 12k–13k; support equipment needs mounting |

**Archetype B: 24w Tank-Supported Breakthrough**

| Component | Ratio | Notes |
|---|---|---|
| Combat width | 24w | 4–5 light/medium tanks + 4 motorized infantry + 2 motorized artillery |
| Support | Engineer, Recon (Armored Car), Signal, Logistics | 4 companies |
| Org (base) | 30–38 | Tanks 20–25, motorized 35–40; average tanks down heavily |
| Piercing | 20–30 (from tanks + motorized AT) | Medium tanks start at ~90 armour; still underpierced vs own armour |
| Hardness | 15–25% (light/medium tank mix) | 40% average rule: 0.40 × highest (70 armour light tank) + 0.60 × average (lower) |
| Cost | 1800–2200 | Manpower 10k–12k; fuel ~5 per div; equipment more diverse |

**Why this split:** Germany's 1939 Armor Division (19w, armour 24.3, hardness 37%, piercing 46.6) shows mid-war panzer doctrine: mix light and medium tanks with motorized infantry to maintain speed, accept lower org (21.4 base) in exchange for piercing and armour. The Soviet Union counters with Mekhanizirovaniy Korpus-pattern heavy armour divisions.

**Inferred:** The mid-war split between "infantry line" and "breakthrough spearhead" becomes permanent. The line holds and absorbs attacks; the spearhead exploits breakthroughs and encircles. A typical army might be 60% baseline infantry, 30% medium-heavy tanks, 10% mobile anti-tank/recon. This requires fleet composition thinking, not a single universal template.

**Doctrine interaction:** Mobile Warfare's Armor track Brigade Size +1 is reachable now that tank Mastery accrues (4.0× rate). Superior Firepower's +10% line artillery is mandatory if fielding dedicated artillery battalions. **Inferred:** Mid-war Germany/USSR benefit from Mobile Warfare + Armor track for speed and breakthrough stacking; infantry-heavy nations (UK, USA until 1943) default to Superior Firepower + Artillery track.

## Late war (1943–1945): Armour abundance, piercing arms race, hardness relevance

**Tech context:** Infantry Equipment 1943, Medium Tanks 1943, Heavy Tanks 1943, Mechanized Infantry, Support anti-tank/artillery at higher tiers. Radar/Radio coordination 1943+. Multiple tiers of armour (light 50–80, medium 100–140, heavy 150+).

**Archetype A: 20w Mechanized Infantry (Defence/Holding)**

| Component | Ratio | Notes |
|---|---|---|
| Combat width | 20w | 6–7 mechanized infantry + 2–3 motorized artillery + 1 motorized anti-tank |
| Support | Engineer, Field Hospital, Support Anti-Tank (1943+), Support Artillery, Signal | 5 companies |
| Org (base) | 42–48 | Mechanized infantry high-org (45–50); support companies drag average down |
| Piercing | 40–50 (motorized AT + Support Anti-Tank + Infantry Anti-Tank tech) | Against medium tanks (100–140 armour) now sufficient; no penalty |
| Hardness | 20–35% (some mechanized + motorized) | Mechanized infantry armour 10–15; motorized 0; average raised by armoured cars/recon |
| Cost | 1200–1600 | Manpower 12k–14k; support equipment abundant; reliability concerns for mechanized |

**Archetype B: 40w Breakthrough (Attack)**

| Component | Ratio | Notes |
|---|---|---|
| Combat width | 40w | 4–5 medium/heavy tanks + 4–6 motorized/mechanized + 2 self-propelled artillery or rocket artillery |
| Support | Engineer, Signal, Recon (Armored Car), Maintenance | 4 companies |
| Org (base) | 28–36 | Tanks 18–25; motorized 35–40; SP artillery 20–25; low average |
| Piercing | 60–90 (medium+ tanks + SP AT) | Against all but super-heavy (200+) armour; exceeds enemy piercing for armour bonus |
| Hardness | 35–50% (heavy tank mix) | Heavy tanks 150+ armour; even 40% average rule yields significant bounce |
| Cost | 3000–4000 | Manpower 10k–12k; fuel 12–16; equipment: tanks, SPG, mechanics |

**Archetype C: 20w Anti-Tank Nest (Specialized Defence)**

| Component | Ratio | Notes |
|---|---|---|
| Combat width | 20w | 4–5 anti-tank (towed or SP) + 6–7 infantry in 3 regiments |
| Support | Engineer, Logistics, Signal, Support Anti-Tank (1943+), Maintenance | 5 companies |
| Org (base) | 38–42 | Infantry 45; AT low (15–20); average dragged down |
| Piercing | 80–120 (heavy AT guns + SP variants + milestone bonuses) | Exceeds all tanks; guarantees armour bonus when engaged |
| Hardness | 0–5% (no tank armour) | Pure soft units; full damage from hard attacks |
| Cost | 900–1200 | Manpower 11k–13k; AT guns abundant; no fuel |

**Why late-war archetypes diverge:** By 1943, armour is ubiquitous and piercing is mandatory. The **Inferred: strategic choice is not "use tank division or infantry division" but "is my infantry fast-enough-and-armoured-enough to survive tank attacks, or do I need dedicated anti-tank?"** Mechanized infantry offers both mobility and a baseline defence against armour via hardness. Pure AT nests are force multipliers against tank-heavy opponents but useless against swarms of soft infantry. Breakthrough divisions commit to heavy tanks and accept low org, knowing the planning bonus and higher attack will break the enemy's defence fast enough.

**Historical reference:** The American 1943 Infantry Division (22w, hardness 0%, piercing 43.4, defence 306.6) and hypothetical 1945 mechanized variant (20w mechanized infantry template) show the late-war infantry evolution: more motorized, higher tech, but org no longer the only stat that matters. Piercing and armour bonus become tied to unit survivability.

**Doctrine interaction:** Superior Firepower's Brigade Size +1 from Artillery track (10.0× Mastery gain, fastest) is already maxed; the doctrine compounds with +10% line artillery and Recovery Rate +0.20 on army. Mobile Warfare's Armor track is near-maxed on tank-heavy armies; Blitz tactic and breakthrough stacking yield major offensive bonuses. Grand Battleplan's +110% max planning and Coordination +10% make massive planned offensives feasible. **Inferred:** Late-war doctrine choice crystallizes: attack-focused armies (Mobile Warfare + Armor) for rapid conquest; defence-focused (Grand Battleplan + Infantry) for holding against numerically superior enemies; supply-constrained empires (Mass Assault) for cheap numerical superiority.

## Template sizing: Width division across terrain

Because combat width is terrain-dependent and over-width penalties are severe (−1% per 1% of width), division width must match the intended front.

| Terrain | Base width | Flanking additions | Recommended single div | Recommended stack (gap-free) |
|---|---|---|---|---|
| **Plains / Urban** | 70–80 | +35–40 per flank | 20w (3–4× fit cleanly) or 35w (fits 2×) | 3× 20w (60w, 14% penalty) |
| **Forest / Jungle** | 60 | +30 per flank | 20w (3× fit cleanly) | 2–3× 20w |
| **Mountain / Marsh** | 50 | +25 per flank | 20w (2–3× fit, last at penalty) | 2× 20w (40w, no penalty) or 1× 40w (no penalty) |
| **Hills** | 70 | +35 per flank | 20w (3× fit cleanly) | 3× 20w |

**Inferred:** 20-width divisions are universally safe (fit in Mountain 50-width at 2× without penalty). 40-width is efficient only on Plains/Urban with multiple attack directions or when the enemy is weak enough that one breakthrough matters more than coverage. Multi-front wars naturally push toward 20-width; single breakthrough-focused campaigns favor 40-width in one army, 20-width holding forces elsewhere.

## Piercing and armour bonus mechanics in template design

From the combat mechanics corpus: insufficient piercing triggers an **armour bonus to the target** — the enemy's organization die upgrades from 1d4 (average 2.5) to 1d6 (average 3.5), a +40% org damage per hit. Additionally, damage is scaled by **−50% / −35% / −20%** based on piercing thresholds.

**Inferred: A division attacking an enemy it cannot pierce is effectively 40–50% weaker per hit.** This makes piercing a binary requirement, not a graduated stat.

**Early war (pre-1939):** No one has significant armour. Piercing is unused.

**Mid war (1939–1942):** Light tanks (50–80 armour) and early medium tanks (100–120 armour) appear. AT battalions provide 20–30 piercing baseline. Insufficient against medium tanks; damage penalty −35%. **Inferred:** Add a dedicated Support Anti-Tank company (1943+ research) or swap to SP AT guns.

**Late war (1943–1945):** Medium tanks 100–140, Heavy tanks 150+, Super-heavy 200+. Infantry equipment anti-tank upgrades (Improved Anti-Tank Rifles, etc.) can double infantry piercing to 30–50. Support Anti-Tank at 1943+ gives 35–50 piercing. Motorized AT and SP AT guns reach 70–90. **Inferred:** Late-war templates **require** either:
- A dedicated anti-tank battalion or support company bringing 40–80 piercing, OR
- A medium+ tank regiment in the division (35–100 piercing depending on tier)

Mixing AT support with line AT can backfire: if the support company has 35 piercing and line AT has 20, the average drops, and the 40% "highest" rule in the piercing formula means the support company's 35 does not fully compensate the line's 20. **Inferred:** Pick one anti-tank source and commit to it; do not mix towed and SP.

## Support company allocation in late-war templates

Each division holds 5 support company slots. Mandatory late-war inclusions:

1. **Engineer** — River crossing −30% penalty becomes −0%, Entrenchment +0.20, fort attack bonus. Nearly mandatory.
2. **Signal** (or Recon) — Initiative stat speeds planning from 2%/day to up to 2.4%/day with +10% Signal; Recon (+Reconnaissance) helps against enemy tactics.
3. **Support Anti-Tank** or **Support Artillery** — Provides attack or piercing; depends on template role.
4. **Support Artillery** (if breakthrough) or **Maintenance** (if tank-heavy) — Soft attack or equipment reliability.
5. **Field Hospital** or **Logistics** — Trickleback or supply reduction.

**Inferred:** Late-war support slots are competed for. A "generic" 20-width division runs Engineer + Signal + Support Anti-Tank + Support Artillery + Field Hospital. A tank-heavy division runs Engineer + Signal + Support Anti-Tank + Maintenance + Recon (Armored Car). An anti-tank nest runs Engineer + Support Anti-Tank + Logistics + Maintenance + Signal.

## Doctrine-specific template archetypes

### Mobile Warfare + Armor track (Breakthrough-focused)

**Brigade Size +1 from Armor track.** Bonus to Organization when moving (−15%), Reinforce Rate +2%, Division speed +10%, Planning Speed +20%.

**Inferred template design:** Minimize support company width-overhead; stack 1–2 heavy tanks + multiple medium/light tanks in the armoured regiments, motorized infantry, and SP artillery. Accept very low org (20–30 base) because organization loss when moving is reduced and the speed enables lightning breakthroughs. Org recovery in rear areas is better than org during the assault.

**Example (late-war):** 6× Medium Tank + 2× Motorized Infantry + 2× Motorized Rocket Artillery + Engineer + Recon (Armored Car) + Signal + Maintenance = 40w, 32 base org, 327 breakthrough (MW L&R from historical-divisions corpus shows template 5 at 376.8 breakthrough for 3 motorized + 7 medium tanks). This excels at forcing through gaps; poor at defending.

### Superior Firepower + Artillery track (Firepower-focused)

**Brigade Size +1 from Artillery track (10.0× Mastery, fastest).** +10% line artillery, +5% support soft attack, −10% supply consumption on infantry, +0.10–+0.20 recovery rate.

**Inferred template design:** Pack multiple line artillery battalions (3–4 per 40-width division is common), supplement with support artillery and rocket artillery. Accept low org from artillery but gain soft attack (one line artillery battalion ≈ three infantry battalions' soft attack at half the width). Pair with any doctrine path that feeds Artillery Mastery (Flying Batteries, Fire Concentration, Self-propelled Support all build Mastery fast).

**Example (mid-war):** 5× Infantry + 3× Line Artillery + Engineer + Support Artillery + Support Anti-Tank = 27w, org drops to ~32 but soft attack ~150+. Paired with Superior Firepower + Fire Concentration for combat width reduction (artillery to 2.2 width) and breakthrough bonuses.

### Grand Battleplan + Infantry track (Entrenchment-focused)

**Brigade Size +1 from Infantry track.** Max planning +10%, +0.25 daily command power, Max Entrenchment +5%, Coordination +10% (×2). Infantry track milestones add +20% entrenchment speed and Interlocking Fields of Fire soft attack +10%.

**Inferred template design:** Maximize infantry content (8–10 per 20-width division) with minimal support. Entrenchment bonus is per-point (+2% defence per point), so a division can reach 25–30 entrenchment and multiply the bonus to ~50–60% defence multiplier on top of base defence. This is a "dug-in" archetype: poor for attack, excellent for defence in rough terrain.

**Example (mid/late-war):** 8× Infantry + Engineer + Field Hospital + Logistics + Support Anti-Tank + Support Artillery = 20w, defence 280+, entrenchment speed 1.5× from milestones. Stationary on a mountain province for 7–10 days reaches 15–20 entrenchment (+30–40% defence) and can hold against 2–3× local superiority.

### Mass Assault + Infantry track (Numerical-focused)

**Brigade Size +1 from Infantry track.** Out-of-supply penalties −10% (−5% more from milestones), Supply Grace +48h, Minimum Training Level −5% (×2). Infantry combat width reduction from Vast Offensives or Human Wave Offensive (−0.4 width per infantry battalion).

**Inferred template design:** Flood with cheap infantry, rely on supply grace to push through low-supply regions (Soviet offensives into Poland, North Africa). Combat width reduction means 10 infantry fit in ~20w instead of 22w, so an extra infantry battalion appears "free" in the same frontage. Pair with Irregulars or People's Militia for minimal unit XP cost and extra recruitment pool.

**Example (Soviet late-game):** 10× Infantry + Support Artillery + Field Hospital + Support Anti-Tank = 20w (technically 18w with width reduction), org 42–46 because no expensive spec units, cost 600 production / 12k manpower. Field dozens of these and accept 50% casualties; the supply grace allows pushing 300km without trucks.

## Common pitfalls and fixes

**Over-specializing.** A pure AT-gun division is useless against pure infantry. A pure tank division breaks into unarmoured terrain where infantry ambushes. **Inferred:** Always include a flexible anti-soft-attack source (infantry or motorized infantry) and soft-attack source (artillery or tanks). Support companies provide the third layer (engineer for forts, signal for coordination, recon for tactics).

**Ignoring organization.** Adding a second artillery battalion to a 20w division drops avg org by 3–5 points. Against high-recovery enemies, the extra soft attack does not compensate for lower org. **Inferred:** Test templates in the designer before committing XP. Watch the org bar; if it drops below 35–38, reconsider the artillery ratio or use Superior Firepower's recovery bonuses.

**Width mismatch to terrain.** A 27w division fits cleanly on Plains (70 width for 2 divs, 49 penalty) but blocks a third. Swapping to 20w lets 3× fit gap-free. **Inferred:** Standardize on 20w or 24w if you fight varied terrain; if locked into one front (e.g., Germany in 1943 defending the West), design for Plains (wide).

**Ignoring support company speed effects.** Recon companies DO affect max speed; if you lack the equipment, the whole division slows to 4 km/h. **Inferred:** Motorized/Armored Car recon for mobile divisions; check the division designer's max speed output before committing to a template.

## Recommended era-based templates for different nations

**Inferred** suggestions based on typical national strengths and doctrine.

| Nation | Early war | Mid-war | Late-war |
|---|---|---|---|
| **Germany** | 9× Infantry + 1× Artillery + support (22w) | 4× Med Tank + 2× Motorized Inf + 1× Motorized Art (Mobile Warfare) | 5× Med/Heavy Tank + 2× Motorized Inf + 2× SP Artillery; backup 8× Mech Inf + 2× AT (Grand Battleplan for defence) |
| **Soviet Union** | 10× Infantry + support (22w) | 4× Light Tank + 3× Motorized Inf + 1× Motorized Art (Armored Spearhead); backup 8× Infantry (line) | 4× Medium/Heavy Tank + 3× Motorized Inf + 1× Motorized Rocket Art; backup 10× Infantry (Mass Assault for width) |
| **USA / UK** | 9× Infantry + 2× Artillery (20w, high defence) | 8× Infantry + 2× Line Artillery + support (20w, Superior Firepower) | 6× Mech Infantry + 2× Medium Tank + 2× SP Artillery + support (20w, Superior Firepower) |
| **Japan** | 9× Infantry + 1× Artillery (20w, light loadout) | 8× Infantry + 1× Light Tank + support (18w, high width) | 7× Infantry + 1× Medium Tank + 1× AT, accept lower piercing, rely on numbers |
| **Minor nation** | 8× Infantry + 1× Support Artillery (18w, cheap) | Stick with infantry, add motorized for mobile doctrine if possible | 8× Infantry + 1× Support Anti-Tank + support, specialize by front (AT nests vs main line) |

These are not prescriptive; national bonuses (Germany's factory efficiency, Soviet tank output, USA's logistics) drive actual builds. **Inferred:** Use these as starting points; measure your templates' org and soft attack against enemy templates to find gaps.
