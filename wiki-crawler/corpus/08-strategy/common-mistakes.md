---
title: Common New-Player Mistakes
category: strategy
tags: [beginner, supply, divisions, manpower, templates, combat, mistakes]
game_version: "1.19"
dlc: []
sources:
  - ../01-mechanics/supply-and-logistics.md
  - ../02-land-warfare/land-combat.md
  - ../01-mechanics/manpower-and-experience.md
---

## Summary

Most early defeats come from supply collapse, division starvation, or manpower bankruptcy rather than tactical failure. Players push armies into unsupplied zones, recruit divisions they cannot sustain, and commit forces that don't fit the battle. This file covers the three most dangerous mistakes and how to avoid them.

## Supply overextension

**Inferred:** The most common death spiral: divide your army into invasion forces that outrun their supply lines, and every province becomes a fight against starvation as much as the enemy.

### The mechanism

From [Supply and Logistics](../01-mechanics/supply-and-logistics.md): a province's supply level comes from three stacked sources — **state supply** (drawn first), **hub supply** (drawn second, travels from supply hubs and ports), and **aerial supply** (last resort). If a province cannot supply the divisions inside it, penalties escalate: reduced speed, attack, defence, organisation regain, and finally equipment attrition once supply drops below **35%**.

Hub supply reaches a province based on the **hub's throughput** (set by the weakest link in the rail/port chain back to the capital) and the **hub's range** (decays with distance, terrain, weather, and infrastructure). A level-1 railway delivers **15 supply** at best; level 5 delivers **35**. That single connection may feed 5–10 divisions depending on how heavy they are.

### Where players fail

1. **Pushing into enemy territory without forward hubs.** Players advance 5–10 provinces into an enemy nation without building a single supply hub, expecting state supply to carry 100k troops. State supply in a typical province is **0.3 supply/infrastructure level** — so a level-5 state gives 1.5 supply to the *entire province*. A single infantry battalion alone draws **0.06** supply; a full 20-battalion division draws over **1.2**. Multiple divisions in one province immediately suffocate.
   
   **Inferred:** Build a supply hub or port within 3–4 provinces of your front line. A level-1 hub costs **20,000 CIC**, but saves you from losing 10,000 troops to starvation. The cost-benefit is absurd.

2. **Using motorized hubs without enough trucks.** A fully motorised hub requires **80 trucks** and extends supply range, but trucks have **attrition scaling by terrain**. Jungle terrain hits trucks with **3.0× attrition**; marsh with **4.0×**. A motorized hub in jungle loses trucks at **12x the base rate**. If you only have 80 trucks and 30% are destroyed in mud, you only get a **partial** supply bonus — capped by the shortfall.
   
   **Inferred:** In rough terrain, either build a new supply hub rather than motorize it, or only motorize as a temporary boost when you have a truck surplus.

3. **Not upgrading railways before pushing through them.** A level-1 connection delivers 15 supply total across all divisions drawing from it. Upgrade to level 5 (**+130 CIC per level, max 2,800 CIC total**) and you get 35 supply — more than double. Players advance into a new region, leave the railway at level 1, then wonder why their divisions starve despite being "connected to supply."
   
   **Inferred:** When capturing a railway, upgrade it to at least level 3 immediately — this is often the single highest-ROI infrastructure spend in the early war.

4. **Ignoring terrain penalties to supply flow.** Mountain provinces reduce hub supply by **0.12 directly**; jungle by **0.16**; marsh by **0.16**. These are not percentages — they are outright subtractions from the supply number. A level-3 hub delivering 25 supply into mountains gives `25 − 0.12 = 24.88` — almost no loss. But a level-1 hub delivering 15 into marsh gives `15 − 0.16 = 14.84`, a **1% loss**. More critically, if you have *multiple* mountain/jungle provinces between the hub and your front, they stack: `25 − 0.16 − 0.16 − 0.12 = 24.56`. With more provinces or rougher terrain, the drop accelerates.
   
   **Inferred:** In mountainous regions, build intermediate supply hubs rather than stretching one hub's range. The cost is lower than losing divisions.

5. **Running supply at full capacity with no margin.** Many players push exactly as many divisions as the supply line can carry and call it done. But weather and terrain volatility can swing supply by **50%**. A blizzard reduces supply flow by **25%**; deep snow by **40%**. Mud happens unexpectedly in spring and autumn.
   
   **Inferred:** Size your army to 70–80% of maximum sustainable supply. This gives you buffer for weather, damaged railways, and enemy Logistical Strike air missions against your trains.

## Division template and combat-width mistakes

**Inferred:** Poorly designed divisions waste combat potential, burn through reinforcements needlessly, and jam up your battle lines.

### The problem

From [Land Combat](../02-land-warfare/land-combat.md): each terrain has a fixed **combat width**, and divisions can only participate if they fit within that width (plus reserves). A plains battle has **70 width**, urban **80 width**. If you field a 36-width division into a 70-width plains battle, only two fit: `36 + 36 = 72 > 70`, so the second division suffers a **−1.1% penalty** and has a **−33% cap**. A third division goes straight to reserve.

Worse: divisions in reserve deal and take **no damage**, do not regain organisation, and do not build entrenchment or planning bonus. If you attack with three 36-width divisions into a 70-width plains, one division is wasted for the entire battle.

### Where players fail

1. **Building 40-width "meta" divisions by default.** A single 40-width division fills **57% of plains width** (40/70). Two fit exactly at `40 + 40 = 80 > 70`, taking a **14% penalty**. Three overflow to reserve. For the same 120 total width, you could field **three 25-width divisions** (25+25+25 = 75 ≈ 70, −7% penalty) or **two 35-width and one 40-width** (35+35 = 70 perfect fit, +40 to reserve). The flexibility matters more than a single "correct" width.
   
   **Inferred:** Design divisions so multiples of them fit your expected terrain. If fighting mountains (50 width), build 25-width divisions. If mostly plains (70 width), build 35s or 20s+15s. Avoid prime-number widths.

2. **Not tracking organisation.** Infantry divisions typically start with **40–50 organisation**. Attacks and casualties drain it; low org means the division can flee or shatter mid-battle. From [Land Combat](../02-land-warfare/land-combat.md), a division at 0 organisation flees or shatters. Players build pure-infantry divisions and throw them at entrenched defenders without planning bonus, expecting to break through.
   
   **Inferred:** Add support companies (Engineer, Signal) to raise organisation caps (+1 to +2.5 each). A 20-battalion all-infantry division with no support starts at ~40 org; with an Engineer and Signal company it reaches ~45–47. This is the difference between recovering from a bad engagement and shattering.

3. **Over-weighting artillery.** Artillery battalions draw **0.21 supply** each and add **3 width**. Tanks draw **0.22–0.40 supply** and add **2 width**. A division heavy in artillery fills width quickly but contributes little directly to the fight — support companies and damage modifiers matter far more. A typical mistake: 5 artillery battalions + 15 infantry = **1.05 + 0.9 = 1.95 supply**, vs. a tighter design of 8 motorized + 8 infantry + 1 support = **0.52 + 0.48 + ~0.06 = 1.06 supply** for better assault ability and maneuverability.
   
   **Inferred:** Treat artillery as a support *multiplier*, not a core element. One 1944 artillery battalion backing eight infantry battalions amplifies their damage by ~15%; more artillery doesn't scale that benefit linearly.

4. **Deploying divisions straight from training at Green.** From [Manpower and Experience](../01-mechanics/manpower-and-experience.md): Green divisions suffer **−25%** to attack and defence. Normally divisions deploy at **Trained** (0% modifier), but if you hit the manpower cap or recruit during active war, new divisions go in at Green. Attacking with green divisions halves your effective strength.
   
   **Inferred:** Exercise divisions to **Regular** (30% threshold, +25% modifier) *before* committing them to major offensives. This costs time and equipment, but saves manpower in the long run by reducing casualty rates.

## Manpower bankruptcy and recruitment mistakes

**Inferred:** Recruiting too many divisions too early leaves you powerless mid-war when conscription laws lag behind your manpower pool.

### The mechanism

From [Manpower and Experience](../01-mechanics/manpower-and-experience.md): recruitable population is a ratio applied to state population, modified by conscription law and by mobilization speed. **Limited Conscription** gives **2.5%** recruitable population; **Extensive Conscription** gives **5.00%**; **All Adults Serve** gives **20.00%**. But changing conscription laws doesn't apply instantly — the value drifts at **mobilization speed: 0.01% per day** base, or **250 days** to shift from Limited to Extensive if you have 50% war support.

An infantry battalion costs **1,000 manpower** to recruit. A small nation like **Poland** (population ~35 million in-game) at Limited Conscription has `35M × 2.5% = 875,000 recruitable manpower`. That pays for 875 divisions *if* they are all infantry. A motorized division or one with armor costs more and depletes the pool faster.

### Where players fail

1. **Recruiting 100+ divisions before the war starts.** A common new-player instinct: "I need a big army to win." They push their conscription law to Extensive and train 100 divisions. By the time they declare war, they've burned **100M+ manpower** leaving only a small surplus in the pool. Three months of war and heavy combat drain the pool to zero. No reinforcements arrive because of the supply line penalty at low manpower. Divisions get weaker as casualties mount without replacement.
   
   **Inferred:** Recruit divisions *during* the war, not before. Start with a small core army (20–50 divisions of good quality, well-trained), improve conscription laws as war support rises, and recruit in batches as the pool refills. This also lets you adjust division design based on what the enemy fields.

2. **Not accounting for non-core manpower penalties.** If you conquer a foreign non-core state, its recruitable population is hit by **−98%**. Example: capturing a 5M-population state gives `5M × 2.5% × (100% − 98%) = 2,500` recruitable manpower instead of 125,000. Occupation compliance can recover some of this via **Volunteer Program** (60% compliance = +20% factor), but it takes months to build.
   
   **Inferred:** Do not expect to conscript your way to victory by occupying enemy territory early. Occupy for resources and VP, but maintain manpower reserves in your core states. Capture nations' capitals and win quickly, or use occupation policies to build compliance *and* infrastructure.

3. **Underestimating casualty rates.** Combat casualties remove manpower immediately and permanently (except 20% trickle-back if a division shatters). From [Land Combat](../02-land-warfare/land-combat.md), a well-coordinated attacker loses maybe **10–20% strength per day** of grinding offense; a poorly-coordinated one loses **30%+**. Over a two-week offensive, that is **70–100% losses** across the entire force. If you start the war with 1M manpower pool and lose 20% in the first month, you need new recruits to flow in. If conscription lags, divisions stay understrength forever.
   
   **Inferred:** Plan for 15–20% monthly casualties in your manpower budget during active war. If you have 1M recruitable pool and field 500k troops, you can sustain ~150k monthly casualties indefinitely (assuming combat, supply and training drain combined). Exceeding this means bankruptcy within months.

4. **Ignoring the gap between "free manpower" and "training capacity."** From [Manpower and Experience](../01-mechanics/manpower-and-experience.md): manpower usable for training new divisions is capped at **75% of manpower in the field, or 100,000, whichever is higher**. If you deploy 1M troops, you can train using up to 750,000 manpower. If you deploy 200k, you can only train using the flat 100,000. Players sometimes have free manpower available but cannot recruit more divisions because of this cap.
   
   **Inferred:** To maximize recruitment rate, keep a healthy buffer of deployed troops. The floor is 133k deployed troops (giving you 100k training capacity); ideal is 700k deployed (giving you 525k training capacity and room to scale).

## Entrenchment and planning bonus misuse

**Inferred:** Attacking entrenched defenders without preparation bonus or overwhelming force is expensive and often fails.

From [Land Combat](../02-land-warfare/land-combat.md): a **planning bonus** starts at 0% and accumulates while a plan is queued (not executing), reaching **+30% base** before tactics/doctrine multiply it further (doctrine can boost it to **+110% or more**). Planning accrues at **2%/day** base, accelerated by **Signal Company** and **Radio** technologies.

Defenders gain **+2% per point of entrenchment**, building while stationary and not in combat. A division defending for one week can reach **7–14 entrenchment points** (14% bonus). A defender with a one-week head start has built-in advantage over an attacker with zero planning.

**Inferred:** Never attack entrenched defenders without planning bonus *and* superiority (air, intel, experience, or numbers). A plan queued for 2–3 weeks builds **40–60% bonus** (after doctrines, **110%+** is achievable), turning a marginal attack into an overwhelming one. The time cost is trivial compared to the casualties saved.

## Terrain ignorance in combat

**Inferred:** Fighting in mountain or forest terrain without specialised units or doctrine adaptation is a hidden manpower drain.

From [Land Combat](../02-land-warfare/land-combat.md): mountains impose **−50% attacker attack** and **−50% attacker breakthrough**; forests impose **−15% attack / −10% breakthrough**; jungle imposes **−30% attack / −25% breakthrough**. These stack multiplicatively with other modifiers.

Example: a standard division attacking mountain terrain with no modifiers, no planning, and no doctrine suffers `1.0 × 0.5 × 0.5 = 0.25` effective attack — **25% of base value**. A division with 200 attack rolls only as if it had 50 attack.

**Inferred:** Before attacking mountains, either (a) accumulate planning bonus to **+100%** to cancel out the penalty, (b) use units with mountain-specific bonuses (Mountaineers naturally excel in peaks), or (c) go around. The detour is faster than a two-month grinding offensive with 4:1 casualty ratios.

---

## Quick checklist

**Supply:** Forward hub within 4 provinces of front. Rails at level 3+. 70–80% capacity utilization. Motorize hubs in plains only.

**Divisions:** Widths divisible by terrain (35s for plains, 25s for mountains, 20s for urban). Organization 40+ via support. No more than 2 heavy-weapons battalions per division.

**Manpower:** Start war with small core (20–50 divisions, Trained). Recruit during war as pool refills. Plan for 15–20% monthly casualties. Check training capacity.

**Combat:** Never attack mountains without planning. Stack 2–3 weeks of plans before offensive. Defend is free — let enemy attack entrenchment. Accept draws if attacker has no advantage.

## Related files

- [Supply and Logistics](../01-mechanics/supply-and-logistics.md) — detailed mechanics: hub throughput, range, terrain penalties, state supply pools
- [Land Combat](../02-land-warfare/land-combat.md) — width tables, damage formulas, reinforcement rules, combat factors
- [Manpower and Experience](../01-mechanics/manpower-and-experience.md) — conscription law tables, mobilization speed, recruitable-population calculation, attrition formulas
- [Division Designer](../02-land-warfare/division-designer.md) — how to build templates that work
