---
title: Opening Build Orders
category: strategy
tags: [build order, opening strategy, production priorities, research priorities, 1936-1939, major powers, early game]
game_version: "1.19"
dlc: []
sources:
  - ../01-mechanics/production-and-equipment.md
  - ../02-land-warfare/division-designer.md
  - ../02-land-warfare/land-units-and-stats.md
---

## Summary

Opening build orders (1936–1939) establish production and research priorities before war becomes active. The key constraint is **production efficiency growth**: military factories start at 10% efficiency and grow to 50% cap over ~500 days, doubling output over time. Early production lines lock in permanent losses if switched; research feeds technology cascades that unlock battalion types, upgrades and equipment variants. This file covers typical national opening patterns and the reasoning behind them.

## Production efficiency fundamentals

**Inferred:** The opening build order hinges entirely on production efficiency because military factories produce `powered output × efficiency × modifiers`. Base military factory output is 3.5 (4.5 powered with coal), meaning a factory at 10% produces only 0.45 production cost/day — tiny. At 50% cap it produces 2.25/day — five times more. This asymmetry means:

- **Hold your first production lines steady for 300+ days** until they reach ~35% efficiency, unless critical shortfalls demand a switch. A line at 30% efficiency that produces Rifle Equipment 1 will hit its cap after ~500 days and have built 450+ production cost of rifles. Switching to a different equipment type cuts efficiency to 10%, erasing 20 days of growth.
- **Do not add factories to a line unless you have strategic resources to feed them**. Adding 10 factories at 10% to a rifle line at 40% efficiency creates 10 new factories at 10% (the old ones keep theirs), but if you lack the resources, all 10 will hit −100% efficiency and produce nothing, wasting both the factories and the manpower. Have surplus resources *before* expanding.
- **Back-fill low-priority equipment lines with late-game productions.** Rifles, support equipment and basic artillery have minimal resource requirements; heavy tanks and aircraft have high costs. Start with cheap, long-term lines; upgrade factories to armor and air only after reaching 30%+ efficiency and securing resources.

## Generic opening for any country

1. **Days 1–10 (planning phase):** Duplicate the starting infantry and cavalry templates (or equivalent base templates). Assign one duplicate to **Reserves** priority. Set up **5–10 production lines:**
   - **Line 1 (12–15 factories): Infantry Equipment I** → target reinforcements for starting divisions. This grows your manpower sink but keeps deployed units topped up.
   - **Lines 2–3 (6–8 factories each): Support Equipment** → feed all future support companies. Support equipment is cheap (4 production cost) and has no strategic resources, so it reaches its cap quickly (~30–50 days) and then can coast.
   - **Line 4 (6 factories): Trucks** → motorized infantry needs 35 trucks per battalion; a 6-factory line at 50% cap produces 6.75 cost/day and reaches 100 trucks stockpile in ~15 days.
   - **Lines 5+ (6–12 factories each): Towed Artillery, Anti-Tank** → low-resource combat support. These are cheaper than armor (e.g. Artillery at 3.5 cost vs. Light Tank at 8) and don't lock away your industrial base while learning the game.

2. **Days 10–50 (research start):** Begin with **Infantry Weapons** techs to unlock Infantry Equipment II and III (net +soft attack per unit). Parallel-research **Support Companies** tree to unlock Recon, Engineers, and Support Artillery early (unlock dates matter). Research **Construction Tech I** to unlock basic fortifications and extend entrenchment.

3. **Month 2–3 (production stabilization):** Once a rifle line reaches 25–30% efficiency, shift the **Reserves-priority template** to Elite and begin building a **dedicated armor battalion division** (even if light tanks). Do **not** interrupt the main rifle line. The armor line sits in reserves; you can field it without frontline pressure.

4. **Month 4+ (factory cap expansion):** Construct 10–15 **civilian factories** to unlock 2–3 **military factories** (each civilian builds factories at a ratio). Do not build military factories directly; use civilian → military conversion to keep resources flowing. By month 6, you should have 30–40 total factories across all lines.

## Country-specific openings

### Germany

**Months 1–2:** Prioritize **Panzer III and motorized artillery research** alongside Infantry Weapons II. Germany starts with no armor, so the Panzer I tech comes from basic tank research; Panzer III requires Medium Tank I (1938). 

**Inferred:** Germany's early strength is **air and fast divisions**. The medium tanks are expensive (Medium Tank at 12–14 production cost), but motorized artillery (Motorized Artillery at 4 cost) pairs well with motorized infantry (130.5 cost per battalion) to create mobile breakthrough divisions. A 20-width motorized division (4 motorized inf + 2 motorized artillery + recon) costs ~850 production but reaches 12 km/h speed.

**Production:** 
- **Line 1 (16 factories): Infantry I** (reinforcements)
- **Line 2 (12 factories): Support Equipment**
- **Line 3 (10 factories): Motorized Artillery** (feed future mobile divisions)
- **Line 4 (8 factories): Trucks** (motorized has high truck demand: 35 trucks × 4 battalions + 36 × 2 artillery = 212 trucks per 20-width division)

By month 3, research **Motorized Infantry Doctrine** and transition to motorized templates. Month 4, **unlock Medium Tank I and start armor production** once motorized units exist in stockpile.

**Rationale:** Motorized divisions in 1937–1938 can attack low-org countries (Czechoslovakia, Romania) without air support. Medium tanks arrive by 1938 for push into Poland/France.

### Soviet Union

**Months 1–2:** Research **Infantry Weapons II/III** and **Mechanized Infantry** (unlocks via Mechanized I). Soviet Union starts with large manpower and no shortage of rifle equipment.

**Inferred:** The Soviet Union's constraint is *equipment*, not manpower. A **division needs 1000 manpower (1 battalion) but 100 infantry equipment** (if 100% equipped). Massing 200 divisions on a front requires 100k equipment but only 200k manpower (attainable). Instead, focus on **breadth of coverage (many weak divisions) → depth (fewer, better-equipped divisions).**

**Production:**
- **Line 1 (24 factories): Infantry Equipment I** (massive volume)
- **Line 2 (16 factories): Support Equipment** (critical for 200+ divisions on garrison duty)
- **Line 3 (12 factories): Towed Artillery** (Soviet can afford the width penalty; defense is high)
- **Line 4 (12 factories): Mechanized I** (unlock mid-late game breakthrough)

**Rationale:** Soviet doctrines (Mass Assault) reduce infantry width from 2 to 1.5 and allow deeper infiltration. An 80-width division of 40 infantry + artillery is viable here. Quantity covers the vast front; accept low efficiency for critical first year.

### United Kingdom

**Months 1–2:** Research **Naval techs** (capital ships, light cruisers, submarines) and **Radar** (grants air superiority in adjacent provinces, critical for defense). Parallel: **Infantry Weapons II** and **Tank I** (light tank).

**Inferred:** Britain's opening is paradoxical: weak land army (but dominion subjects provide manpower), dominant navy, and need to defend homeland from air. Delay large army buildup; instead, field **divisions in defensive fortifications** around ports and industrial centers. A fortified 2-width garrison (2 infantry battalions) occupies 4 width and is cheap to maintain.

**Production:**
- **Line 1 (10 factories): Infantry Equipment I** (homeland garrisons only)
- **Line 2 (8 factories): Support Equipment**
- **Naval dockyards (all available)**: Submarines and Light Cruisers (convoy raiding and escort countering)
- **Line 3 (6 factories): Light Tanks** (research late, mass-produce if dominion subjects join war)

**Rationale:** Naval dominance prevents invasion. Focus on **air defense radar and fighters**, not army size, in 1936–1937. Garrison the homeland with cheap infantry; build expeditionary forces only for allies or late-war intervention.

### France

**Months 1–2:** Research **Fortifications** (infrastructure into forts), **Infantry Weapons II**, and **Tank I** (light). France starts with medium level industrial capacity and must defend the Maginot Line.

**Inferred:** France's strategy is **delay via fortifications**. Every fort level adds +20 defense (capped at +100 with max level). A 40-width division defending a level 3 fort gets +60 defense from the fort alone, reducing enemy breakthrough. Early production should **feed garrisons along the German border**, not prepare for offensive war.

**Production:**
- **Line 1 (14 factories): Infantry Equipment I** (garrison supply)
- **Line 2 (8 factories): Support Equipment**
- **Line 3 (10 factories): Towed Artillery** (garrisons get support artillery in support companies)
- **CIV factories: Build infrastructure in Alsace, Lorraine, Maginot states** (fort construction requires supply, so prep supply hubs)

**Rationale:** Forts are the anti-tank. Pair a level 3+ fort with 2–3 garrison divisions of 20-width infantry each; the enemy needs 2–3× that to break through, delaying until historical superiority arrives or reinforcements land.

### Japan

**Months 1–2:** Research **Infantry Weapons II** and **Light Tank I**. Japan starts with low industrial capacity and must prioritize manpower-efficient builds.

**Inferred:** Japan's first 18 months are **garrison and recon heavy** — occupy Manchuria and China with minimal equipment losses via militia and low-org divisions. Light tanks (2.4 cost each, 80% hardness) are efficient armor; delay medium tanks (12–14 cost) to 1939+.

**Production:**
- **Line 1 (8 factories): Infantry Equipment I**
- **Line 2 (6 factories): Support Equipment**
- **Line 3 (4 factories): Light Tanks** (120-day training time; start early)
- Research **Militia** to unlock conscript divisions (cheap manpower, low org, no equipment — ideal for garrison occupation)

**Rationale:** Light tanks research by month 4, production starts month 5, first battalions arrive month 10. Parallel occupation with militia divisions keeps MP costs low while armor trains.

## Early research paths (month 1 priorities)

**Every nation** should start one of:
- **Infantry Weapons II** (requires Infantry Weapons I tech, ~100 days): unlocks a +3 soft attack infantry type, but relatively slow payoff
- **Support Companies** (various, ~80–100 days): Engineer Company unlocks first; grants +2 entrenchment immediately, applying to all divisions. Recon early if you plan mobile warfare
- **Light Tank I** (requires Infantry Eq I, ~100 days): unlocks light tanks; cheap but slow armor

**Parallel infrastructure:**
- Construction Tech → unlocks fort construction (50+ days)
- Radar (if you have electronics tech slot) → air superiority in adjacent provinces

**Inferred:** The research slot constraint is *brutal* early game. Most nations have 2–3 research slots at game start. Prioritize **tech that unlocks new battalion types or support companies** (unlock → automatic division templates appear) over **stat upgrades** (Infantry Weapons II is +3 soft attack, a rounding error on a 40-width division). One **Support Company unlock pays for itself** by making 4–5 future support company designs viable.

## Stockpile timing and deployment

**Inferred:** Do **not** deploy divisions until their equipment lines hit 200+ stockpile. A 20-width division needs ~50 cost-equivalent equipment (variable by template); a 40-width needs ~100. At 4–5 production per day per line, that's 25–50 days of pure production. Building divisions before stockpile appears instantly causes:
- **Equipment reroute bottlenecks:** equipment flows to **reinforcements first**, starving stockpile; new divisions sit in the backlog
- **Understrength divisions:** deployed divisions train at low org, taking losses if attacked; understrength reduces combat stats per [Division Designer](../02-land-warfare/division-designer.md)

**Best practice:** Queue all divisions in the recruitment screen as **Reserves** (lowest priority) until stockpile is ready, then **promote them to Elite** (highest priority) to pull equipment in bulk.

## Common mistakes

1. **Switching production lines early.** A rifle line at 30% efficiency has 20 days of "growth advantage" over a fresh line. Switching costs 70% efficiency (to 9%), losing that entire advantage. Do not switch unless facing resource shortage or critical military need.

2. **Adding factories without resources.** Each factory added without sufficient strategic resources hits −5% efficiency per missing resource unit (capped at −100%). A −100% factory produces zero; the factories themselves are wasted. Verify resource surplus in the trade screen **before** expanding.

3. **Building air and navy before land army.** Air wins **territories with active airfields**; navy wins **sea zones**. Neither wins without a land army to hold territory. Prioritize land equipment 1st, air/navy 2nd.

4. **Ignoring support companies.** A support artillery company (4 equipment, 42 cost) gives +15 soft attack per division at **no combat width cost**. A line artillery battalion (24 equipment, 84 cost) gives +25 soft attack at **+3 width**. The support company is 50% the cost for 60% the attack, occupying zero width. They are asymmetrically powerful early game.

5. **Templates that are too weak.** A 10-width division of 5 infantry needs 5000 manpower but has only 100 soft attack. A 20-width division (10 infantry) has 200 soft attack for 10k manpower — *double the attack, double the cost*, but *the defense/breakthrough also double*. Weak templates drain manpower without scaling impact; 20-width is the practical minimum.

## Expansion and the 18-month mark

**Inferred:** By month 18 (mid-1937), your first production lines should be approaching 40–45% efficiency. Rebase your production:

- **Reprioritize old lines:** rifle and support lines shift to **Reserves** (they will reach cap by month 24 anyway; let them tick slowly)
- **Unlock new equipment:** Infantry Equipment II, Basic Tanks, Motorized Inf researches complete; spin up new 1937 lines for the upgraded equipment
- **Expand factories:** by month 18 you should have built 15–25 civilian factories, converting 5–10 to military; your military-factory count should have grown 50–100%
- **Prepare war-economy research:** begin researching **Production techs** (production efficiency gain), **Tank/Aircraft chassis** (designer DLC if relevant), and **War Economy laws** (switching from Civilian Economy to Partial Mobilization)

At month 18, a typical major power should have **45–60 military factories** across 8–15 production lines, research reaching 1937 techs, and war-readiness decisions (alliances, focuses) taking priority.

## Related files

- [Production and Equipment](../01-mechanics/production-and-equipment.md) — factory mechanics, efficiency formulas, resource costs
- [Division Designer](../02-land-warfare/division-designer.md) — XP costs, template structure, support company rules
- [Land Units and Stats](../02-land-warfare/land-units-and-stats.md) — per-battalion stats and equipment requirements
