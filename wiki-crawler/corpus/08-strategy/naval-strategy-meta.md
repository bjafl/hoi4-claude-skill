---
title: Naval Strategy Meta
category: strategy
tags: [naval-strategy, fleet-composition, grand-doctrine, screening, capital-ships, carriers, submarines, trade-interdiction]
game_version: "1.19"
dlc: [Man the Guns]
sources:
  - ../04-naval-warfare/naval-warfare-overview.md
  - ../04-naval-warfare/naval-combat.md
  - ../04-naval-warfare/ship-designer.md
  - ../04-naval-warfare/naval-doctrine.md
---

## Summary

Naval power in HOI4 splits into two distinct archetypes: comprehensive fleet battles (for industrial powers with enough steel/fuel budget) and commerce raiding or coastal defense (for resource-constrained nations). Fleet composition hinges on screening efficiency (3 screen ships per capital/carrier for 100% protection, 0.5 per convoy), which determines whether capital ships can survive. Grand Doctrine choice locks in strategic direction—Fleet In Being for battleships, Trade Interdiction for submarines and commerce, Base Strike for carriers—and switching costs all accumulated doctrine Mastery. **Inferred:** the optimal path depends on industrial capacity: majors should commit early to one doctrine and maximize that track; smaller navies benefit more from submarines (low steel cost, high raiding output) or focused carrier fleets (high damage per ship) than expensive battleships.

## Nation types and naval capacity

**Inferred:** Naval strategy splits sharply by industrial tier:

### Major powers (United Kingdom, Germany, Japan, United States, Soviet Union, Italy, France)

These nations have sufficient steel and fuel to field multiple fleets with mixed composition. The key constraint is **time to build**: a single battleship costs 3200–5500 production at base cost, while a destroyer costs 400–600. 

**Inferred:** Major powers should:
- Commit to one Grand Doctrine at game start and stack all four Doctrine Tracks toward that archetype (do not split between, e.g., Fleet In Being and Trade Interdiction; switching wipes all Mastery and costs 100 Navy experience each time).
- Field task forces large enough to reach 100% screening efficiency: a task force defending a sea zone should have at least 3 screen ships (destroyers, light cruisers) per capital ship or carrier to prevent torpedo bypass.
- Diversify within the chosen doctrine: Fleet In Being navies still need some submarine escort (2–3 units for minelaying/detection); Base Strike navies need screening to protect carriers.

### Secondary powers with coastal defense (Poland, Greece, Romania, Yugoslavia, smaller nations)

These nations begin with minimal naval capacity and should not race into capital ship construction.

**Inferred:** Coastal defense doctrine is optimal:
- Research the **Coastal Defense Fleet** subdoctrine track (under Capital Ships). It reduces naval max range by 10% (irrelevant for regional defense) and naval supply consumption by 15% (highly relevant for poor supply), and unlocks Coastal Defense Ships (1936 hull, 20 kn max speed, 100 HP, 80% reliability, 3500 production cost).
- Build 2–4 Coastal Defense Ships or heavy cruisers for regional defense at 1/3 the cost of a battleship. A Coastal Defense Ship with Heavy Battery I (14 heavy attack, 31 piercing) and Battleship Armor I (30 armor) costs ~6000 production, half a battleship's cost, and dominates unescorted transports in its theater.
- Use destroyers for convoy escort and minelaying (1–2 per navy to block enemy landing zones).
- Skip battleships until mid-late war (1942+).

### Minor powers with trade focus (Norway, Netherlands, Denmark, smaller colonial powers)

These nations exist to transfer resources via sea trade; their navies are defensive.

**Inferred:** Patrol and merchant protection is the only viable role:
- Research **Convoy Escort** subdoctrine (under Screens). Base bonus: +10% convoy speed while retreating, +10% escort efficiency.
- Build destroyer-based convoy escort task forces (6–12 destroyers per major sea zone, 1–2 regions per task force).
- Do not commit to any capital ships; convoys are too small (0.5 screen ships per convoy for 100% screening) to justify battleships.

## Fleet composition by nation type

### Major navy: Fleet In Being (battleship-centric)

**Inferred:** A **Fleet In Being** grand doctrine fleet maximizes battleship armor (+10% immediate, +10% at Capital Ships Mastery 500) and battleship organization (+15% immediate). This archetype sacrifices speed (battleships max 20–30 kn) for firepower (22–27 heavy attack) and armor (30–55 armor).

**Core composition per task force:**
- **Screening group:** 3 light cruisers or destroyers per battleship/battlecruiser.
  - Recommended: 1940+ Cruisers with Cruiser Armor III (10 armor, −10% speed), Light Cruiser Battery III (6 light attack/8 piercing), Torpedo Launcher III (30 torpedo attack), Depth Charge III (17 depth charges).
  - Cost per screen ship: ~3500 production. Three per battleship = 10,500 production.
- **Capital group:** 2–4 battleships or 1 battlecruiser per capital ship slot.
  - Recommended: 1940+ Heavy Ship hull with Heavy Engine II/III (+35–45% speed, -25–30 production cost), Heavy Battery III (22 heavy attack/40 piercing), Secondary Battery II (4 light attack/7 piercing), Battleship Armor II/III (36–40 armor), Fire Control 0 (+2.5% accuracy).
  - Cost: ~6000–9000 production per battleship. Total per battleline: 12,000–18,000 production for 2 battleships + 6 screens.
- **Carrier group (optional):** 1–2 carriers + 3–4 additional screen cruisers.
  - Carrier screening efficiency requires 1 capital ship per carrier (not counting the screens protecting the capital line). If fielding 2 battleships + 1 carrier, add 1 additional heavy cruiser for carrier screening to avoid 100% carrier screening efficiency penalty (−20% retreat speed, greater torpedo bypass).

**Inferred reasoning:** Battleships have 370–450 HP (1936–1944 hulls) and 30–40 armor. With 3 screens per battleship, each screen absorbs a percentage of incoming fire (40% hit chance bonus at 100% screening efficiency). A single battleship without screening faces 100% enemy hit chance on torpedoes, which ignore armor; with 3 screens, only 50% of enemy torpedoes bypass screening. Armor reduces non-torpedo gun damage by 60–90% depending on enemy piercing vs. your armor value. Cost per HP with armor is high (~10–15 production per HP), so commitment to battleships is capital-intensive.

**Grand Doctrine track priorities (order of investment):**
1. **Capital Ships** (battleships gain +5% heavy attack at Mastery 200, +10% at Mastery 500).
2. **Screens** (escort efficiency +15% at Mastery 500, reducing time escorts respond to torpedo attacks).
3. **Carriers** (if present: +60 organization at Mastery 300, +35% anti-air at Mastery 500).
4. **Submarines** (lower priority: minelaying +20% at Mastery 100 but utility is secondary to capital battles).

### Major navy: Base Strike (carrier-centric)

**Inferred:** A **Base Strike** grand doctrine fleet maximizes port strikes (+40% immediate), carrier organization (+20% immediate), and sortie efficiency (+30% at Mastery 500 for Capital Ships, +30% at Mastery 300 for Carriers if also mastering Massed Carrier Fleet). Carriers deal 10× normal damage if aircraft are based on a carrier in the same battle, making concentrated air power devastatingly effective. Sortie efficiency starts at base 50%; at 100% sortie, half the carrier deck can fly; at 200% sortie (achievable with Floating Airfields +10% base, Carrier Primacy +20% from tech, Floating Airfield runway +30, Massed Carrier Fleet Mastery 300 +30%), 100% of the deck flies even if overcrowded.

**Core composition per task force:**
- **Screening group:** 4–6 destroyers or light cruisers (1 per carrier, then 1–2 additional for capital ships if any).
  - Recommended: 1940+ Destroyers with Light Engine III (+20% speed), Light Battery III (2 light attack/2.5 piercing), Torpedo Launcher III (30 torpedo attack), Anti-Air III (4.5 anti-air), Depth Charge III (17 depth charges).
  - Cost: ~1000 production per destroyer. Three destroyers = 3000 production.
- **Capital group (optional):** 1–2 heavy cruisers if budget permits.
  - Recommended only if the main battleline is elsewhere (i.e., two separate fleets). Heavy cruisers screen the carrier from aircraft and capital ships but cost 2000+ production, which delays carrier construction.
- **Carrier group:** 3–6 carriers (1944+ Carriers preferred: 350 HP, 80% reliability, 26 kn, 2600 production cost each).
  - **Critical:** Load each carrier with aircraft **before deployment**. A fresh 1944 Carrier has 80 deck space; fill it with, e.g., 40 naval bombers + 40 fighters (researched separately under Air doctrine; see Air warfare files). Pre-train the air wings to at least Regular experience before combat by running exercises for 2–3 weeks.
  - Carrier air wings start at Green veterancy and lose experience fast in combat (large losses relative to wing size); pre-trained wings (Regular or Veteran) survive losses better and maintain hit rate. Without pre-training, sortie efficiency can drop to 20–30% by battle's end as planes die and green replacements spawn at 0% hit chance.

**Inferred reasoning:** A single carrier with 80 deck space and 40 naval bombers achieves +10× damage multiplier (based-on-carrier bonus) and 30% hit ratio (base naval strike formula: 30% × naval targeting / 10; Base Strike doctrine gives +40% port strikes, which scales to ~12–15% sortie hit ratio in fleet battles). In a 4-carrier task force attacking a port (port strike orders, which auto-activate when fleets are in adjacent provinces), if 120 bombers sortie (50% sortie × 240 deck capacity), at 12% hit ratio, 14 hits per cycle lands damage equivalent to ~5 heavy battery shots from a capital ship. Carriers are force-multipliers; a 4-carrier fleet costs ~10,000 production (4 × 2600) but deals damage equivalent to 8+ battleships without the cost of screens.

**Grand Doctrine track priorities:**
1. **Carriers** (sortie efficiency +10% base, +30% at Mastery 300 with Massed Carrier Fleet, +30% more with Floating Airfields).
2. **Screens** (escort efficiency for protecting carriers; +15% at Mastery 500).
3. **Capital Ships** (optional; naval targeting +10% at Mastery 500 if also running Base Strike trade milestone).
4. **Submarines** (low priority).

### Major navy: Trade Interdiction (submarine + commerce raiding)

**Inferred:** A **Trade Interdiction** grand doctrine fleet maximizes convoy raiding efficiency (+15% immediate, +10% at Mastery 500 under Capital Ships milestone), submarine surface detection (+10% immediate), organization (+10% immediate), and submarine attack (+0.1 at Mastery 500 under Submarines milestone). Submarines cost 320–1150 production (Early to Nuclear hulls) and deal damage via single-target torpedo attacks (14–44 torpedo attack depending on hull and tubes). A single 1944 Submarine with 28 torpedo attack costs 550 production; at 10% hit ratio (base torpedo hit), 2.8 expected damage per attack cycle (1 per 4 hours). Over a 30-day naval battle, that is ~180 attacks = 504 expected damage. A battleship with 400 HP takes one such submarine to wear it down over a month-long engagement.

**Core composition:**
- **Raiding submarines:** 10–15 submarines in a convoy raiding task force.
  - Recommended: 1940–1944 Submarines with Submarine Engine III/IV (−5% to −10% visibility, +15–20% speed), Torpedo Tubes III/IV (22–28 attack), Snorkel (−7% to −13% visibility).
  - Cost: ~1500–2000 production for a fully-equipped raiding submarine. Fifteen raiders = 22,500–30,000 production total (equivalent to 3–5 battleships).
  - **Placement:** Deploy raiding submarines in enemy sea zones running convoy escort missions (not on patrol; patrols spot incoming convoys too fast for submarines to respond). Submarines on "Convoy Raiding" mission within the fleet's assigned region automatically hunt for enemy convoys. Each raiding task force covers ~1.5 strategic regions efficiently; if the region is too large or raiding task forces too few, efficiency drops dramatically.
- **Capital surface raiders (optional):** 1–2 heavy cruisers for independent raiding when submarines are insufficient.
  - Recommended: Panzerschiff (1933 hull, 220 HP, 4 armor, 7500 km range, 3500 production; excellent long-range raider) or Armored Raiders subdoctrine Capital Ship design (see Naval Doctrine for raiding efficiency bonuses).
  - Cost: 3500–5000 production. Slower but higher firepower than submarines; effective against defended convoys or light merchant escort.

**Inferred reasoning:** Trade Interdiction doctrine provides 15% convoy raiding efficiency immediately. In practice, raiding efficiency determines how fast a raiding task force converges on a spotted convoy. With 15% base raiding efficiency, 10 submarines in a raiding task force can cover 1.5 strategic regions (each region is ~15 'activity slots'; raiding task forces can manage ~1.5 slots per ship at 100% efficiency). As raiding efficiency drops below 100%, more submarines are needed or fewer regions can be covered. Over a full war (5 years), 15 well-placed raiders in the North Atlantic can destroy 1000+ enemy convoys, starving the opponent of oil, rubber, and supplies. This is cheaper and requires less micro than maintaining a full battlefleet.

**Grand Doctrine track priorities:**
1. **Submarines** (surface detection +30% at Mastery 100 under Fleet Operations, +20% at Mastery 200 under Wolfpacks, enabling faster convoy interception).
2. **Screens** (if convoy escort task forces also run; escort efficiency +15% at Mastery 500 under Integrated Operations).
3. **Capital Ships** (low priority; raiding efficiency +15–25% at Mastery 400–500 under Armored Raiders).
4. **Carriers** (skip entirely unless also defending against aircraft).

### Minor power: Coastal Defense

**Inferred:** The **Coastal Defense Fleet** subdoctrine is almost always optimal for nations without heavy industry (Romania, Yugoslavia, Poland, Greece, etc.). The subdoctrine unlocks Coastal Defense Ships (3500 production vs. 3000–5500 for proper battleships), reduces supply consumption by 15% (critical for minor nations with poor logistics), and unlocks special tech Coastal Defense Ships. A Romanian Coastal Defense fleet defending the Black Sea needs 2 Coastal Defense Ships (7000 production) instead of 1 full battleship (5000 production) to achieve comparable firepower for the same cost, with lower supply drain.

**Core composition:**
- 2–4 Coastal Defense Ships in a capital group.
  - Each fitted with Heavy Battery I (14 heavy attack/31 piercing), Battleship Armor I (30 armor), Anti-Air I/II (2.5–3.5 anti-air), Fire Control 0.
  - Cost: ~4500–5000 production per ship. Total for 2 ships: ~9000 production.
- 4–6 destroyers in a screening group for anti-submarine defense and minesweeping.
  - 1936–1940 Destroyers with Depth Charge II/III (13–17 depth charges), Minesweeping Gear (2, −2% speed).
  - Cost: ~500–600 per destroyer; 6 destroyers = 3000–3600 production.

**Inferred reasoning:** A nation with 1000 production/month total and 30% allocated to naval construction (300 naval production/month) can field 2 Coastal Defense Ships (7000 production = 23 months) and 6 destroyers (3600 = 12 months) in one year. The fleet sits in a home sea zone on "Hold" orders, projecting naval supremacy and providing shore bombardment (−0.05% per heavy gun damage to enemy attack and defense, −0.025% per light gun damage, capped at −33%). If an enemy attempts a naval invasion of that region, the Coastal Defense fleet can deal +10% damage (via doctrinal bonuses) to enemy transports and block supply/reinforcement for 2–3 days, allowing land forces to mobilize. This is cost-effective deterrence.

## Fleet composition optimization: Screening and carrier screening

### The screening ratio formula

**Inferred:** Screening efficiency is the **single most important mechanic** in naval battles. At 100% screening efficiency:
- Screens gain +40% hit chance against enemy screens.
- All ships gain +20% retreat speed.
- Screens block 100% of enemy torpedo attacks (50% − 100% carrier screening efficiency) against capital ships and carriers.

The formula is:
- **Screening ratio** = (screen ships) / (capital ships + carriers + convoys)
- **100% screening efficiency** = 3 screen ships per capital/carrier, 0.5 screen ships per convoy.

**Inferred example:** A task force with 2 battleships and 1 carrier requires 2×3 + 1×3 = 9 screen ships for 100% efficiency. Without screens, a single enemy submarine can torpedo either capital ship freely (torpedoes bypass all defenses if no screens present). With 3 screens per capital, submarines must first break through the screening layer (+40% hit chance vs. screens at 100% efficiency) before penetrating to capitals.

**Inferred consequence:** Any capital ship or carrier deployed without sufficient screens will take catastrophic torpedo damage in the opening hours of a battle. A single battleship without screens, facing enemy submarines, loses 100–200 HP (25–50% of max) to the first coordinated submarine attack. Battleship reliability is 80–95%; damaged ships have −25% to −50% hit chance. A damaged battleship becomes nearly unable to fire back, turning a fleet engagement into a decisive loss.

**Inferred optimization strategy:** Never deploy a task force without reaching 100% screening efficiency for the intended composition. If you have 3 battleships and 2 carriers, you need 3×3 + 2×3 = 15 screen ships minimum. Screening is **not optional**; it is the foundation of naval combat.

### Carrier screening ratio

**Inferred:** Capital ships (battleships, battlecruisers, heavy cruisers) also provide a **carrier screening ratio**:
- **100% carrier screening efficiency** = 1 capital ship per carrier, 0.25 capital ship per convoy.

At 100% carrier screening efficiency:
- Carriers gain +10% sortie efficiency (marginal, since sortie efficiency scales multiplicatively with many other bonuses).
- Retreat speed +20%.
- Carriers suffer reduced enemy torpedo attacks (stacking diminishingly with regular screening efficiency).

**Inferred optimization:** If building a carrier task force, assign 1–2 heavy cruisers or battlecruisers per carrier to satisfy this ratio. Example: 2 carriers + 2 heavy cruisers = 100% carrier screening efficiency. The heavy cruisers also provide 40 HP and secondary firepower (7–8 light attack + 7 piercing) against enemy screens. Cost is high (~2000 production per cruiser vs. 2600 per carrier), so smaller carrier fleets skip this and rely on destroyer screening (destroyers do **not** count toward carrier screening efficiency, only capital ships do).

## Design principles by ship class

### Screens (destroyers, light cruisers): speed and efficiency, not firepower

**Inferred:** Screens are **cheap expendable shields**, not damage dealers. A 1940 Destroyer costs 550 production and has 50 HP; a 1936 Light Cruiser costs 1900 production and has 110 HP. When deployed with capital ships, screens are expected to sink first, absorbing fire meant for battleships.

**Inferred design principle:** Maximize speed and sub-detection, minimize cost.
- **Engine:** Always equip the newest available engine tier (+15–25% speed for destroyers, +30–40% for cruisers). Speed scales linearly with retreat speed; a fast screen can disengage before taking full damage.
- **Torpedo:** Add torpedo launchers to all screens. Destroyer Torpedo Launcher III (30 torpedo attack) costs 150 production; the added attack is useful if a screen is forced into combat with an enemy screen. Light Cruiser Battery III (6 light attack/8 piercing) is inherently included in the hull design.
- **Depth charges:** Mandatory for anti-submarine defense. Depth Charge III (17 depth charges) costs 150 production. Submarines deal massive damage to battleships; screens with no anti-submarine capability are liabilities if enemy submarines are present.
- **Fire control / Radar:** Low priority. Fire Control 0 (+2.5% accuracy) costs 60 production on the first screen; stacking it on all screens is wasteful. One radar per task force (placed on the designated flagship) is sufficient for fleet-wide detection bonuses.
- **Example 1940 Destroyer:** Light Engine III, Light Battery III, Torpedo Launcher III, Depth Charge III, no radar. Cost: ~800–900 production. Role: fast, expendable, adequately anti-sub.

### Capital ships (battleships, heavy cruisers, battlecruisers): armor and firepower tradeoff

**Inferred:** Capital ships deal heavy damage (22–27 heavy attack for battleships, 10–12 for heavy cruisers) but are expensive and slow. A 1940 Battleship costs 3200–4000 production and moves at 25 kn (slower than screens by 5–7 kn). They must be protected with screens (see Screening ratio, above).

**Inferred design principle:** Maximize armor first, then firepower, then speed.
- **Armor:** This is **the most important module**. Battleship Armor II (36 armor, +10% HP, −5% speed) vs. Armor III (40 armor, +15% HP, −10% speed) determines survival. At Armor III, a battleship with 400 HP can absorb ~240 HP from gun attacks by non-piercing enemy fire (due to armor reduction). Armor also reduces torpedo critical hit chance (−15% to −20%), which is the primary cause of catastrophic damage (10× damage if a critical hits the magazine).
- **Engine:** Medium priority. Heavy Engine II (+35% speed) vs. III (+45% speed) matters for fleet mobility and retreat speed. Fast battleships (25–26 kn) can stay with battlecruisers (25–27 kn) and screen task forces (31–32 kn), minimizing split formations. Slow battleships (20–23 kn) force all screens to slow down, reducing overall task force speed to 20 kn (speed of slowest ship). Trade speed for range if the battle zone is far from friendly ports.
- **Main battery:** Gun caliber and count scale damage. Heavy Battery III (22 heavy attack/40 piercing) is a significant upgrade from II (18/36) but costs only +100 production and 1 more steel per dockyard. Always research the latest battery tech available at the time of construction.
- **Secondary battery:** Low impact on primary battleship role but adds +4 light attack and +7 piercing against screens. Dual-Purpose Secondary Battery III (4 light attack/7 piercing/2.5 anti-air) is better than pure-gun versions because it provides anti-air, useful against enemy naval strikes. Cost: 300 production.
- **Anti-air:** Stacking multiple Anti-Air IV modules (5.5 anti-air each) is diminishing-return and expensive (170 production each). One Anti-Air IV module per capital ship (~5.5 anti-air) is the minimum. Higher anti-air requires heavy investment; refer to Carrier screen design if optimizing for air defense.
- **Fire control:** Fire Control III (Ballistic Computer, +10% hit chance) costs 225 production but stacks across all guns on the battleship (main + secondary). This is one of the highest ROI upgrades; one Ballistic Computer per battleship is always worth it.
- **Example 1940 Battleship:** Heavy Engine II, Heavy Battery III, Battleship Armor II, Secondary Battery II, Fire Control III, one Anti-Air IV. Cost: ~5500–6000 production. HP: ~440 after armor bonus. Role: high-durability firepower.

### Carriers: deck space and air wing pre-training are the game

**Inferred:** Carrier hulls do not benefit from veterancy (unlike other ships). Instead, the **aircraft stationed on the carrier** provide damage and accuracy via their own veterancy. New aircraft start at Green veterancy (−25% damage, −50% hit chance, very poor sortie efficiency). Aircraft trained to Regular or Veteran retain experience longer in naval battles and are dramatically more effective.

**Inferred design principle:** Maximize deck space, then sortie efficiency, then speed.
- **Hull:** Always research and build the latest carrier hull available (1944 Carrier: 26 kn, 350 HP, 80% reliability, 2600 production; Modern Carrier: 30 kn, 400 HP, 85% reliability, 4250 production). Older hulls (1936 Carrier: 26 kn, 250 HP, 70% reliability, 2094 production) suffer lower reliability and slightly lower damage output.
- **Engine:** Carrier Engine IV (+60% speed) is a luxury; base carrier speed is already 26 kn (roughly equivalent to screens). If budget-constrained, ship engine modules are optional.
- **Hangar space:** Hangar Space modules (+20 deck per module, −5% speed, 1500 production each) are critical. A base 1944 Carrier has 80 deck space; adding two hangars gives 120 deck space, allowing 60 bombers + 60 fighters instead of 40 bombers + 40 fighters. This linearly scales damage output (+50% in the air-to-ship equation). Add hangars until the carrier is 1–10% overcrowded (e.g., 85–87 deck space with 80 max).
- **Deck armor:** Flight Deck Armor (+25 HP, 5 armor, −5% speed, 10% production cost, 1 steel) is marginal; carriers are meant to be protected by screens, not tanked. Skip unless all other modules are optimized.
- **Example 1944 Carrier:** No engine upgrade, Hangar Space ×2 (120 deck space, −10% speed = 23.4 kn), one Fire Control 0 or Light Battery I for detection. Cost: 2600 + 3000 = 5600 production. Load with 60 naval bombers (1944+ variant) + 60 fighters, **pre-trained to Regular experience via exercises in a friendly port for 2–3 weeks before deployment**.

### Submarines: cheap mass, not individual power

**Inferred:** A single submarine costs 320–1150 production and deals ~3–4 damage per attack cycle (at 10% hit ratio). A battleship is overkill defense against one submarine; but a battleship facing 10 submarines can be worn down in 30 days of engagement. Submarines are force-multipliers via **massing**, not individual stat superiority.

**Inferred design principle:** Minimize cost, maximize visibility reduction and range.
- **Hull:** 1944 Submarine (18 kn, 35 HP, 80% reliability, 15 sub visibility, 550 production) is the sweet spot for cost/performance. 1940 Submarine (18 kn, 30 HP, 75% reliability, 20 sub visibility, 420 production) is cheaper but less stealthy. Fleet Submarine (18 kn, 40 HP, 75% reliability, 18 sub visibility, 650 production) adds range (6500 km vs. 3500 km) for ocean-wide raiding.
- **Engine:** Submarine Engine IV (−10% visibility, +20% speed, 10 production cost) is worth it; reduced visibility is the primary defense against enemy anti-submarine weapons. Always add it.
- **Torpedoes:** Torpedo Tubes IV (28 torpedo attack, +2% hit chance, 140 production) is higher cost but essential for damage output. If budget is tight, Torpedo Tubes III (22 attack, +1.5% hit chance, 120 production) is acceptable.
- **Snorkel:** Improved Schnorkel (−13% visibility, 70 production) should be added to all submarines in hot zones (contested waters with active enemy AA). In safe raiding zones (distant trade routes), snorkels are optional.
- **Anechoic tiles:** Anechoic Tiles (−20% visibility, +25% production cost) are expensive and apply only to the surface visibility rating, which is used for passive detection when the submarine is hidden. Skip unless committed to extreme stealth (e.g., a specialized Capital Hunters doctrine submarine).
- **Example 1944 Submarine (raider):** Submarine Engine IV, Torpedo Tubes IV, Improved Schnorkel. Cost: 550 + 10 + 140 + 70 = 770 production per submarine. Field 15–20 for convoy raiding in a single region. Total cost: 11,550–15,400 production (equivalent to 2–3 battleships, but 15–20 submarines cover an entire sea zone).

## Doctrine selection by nation and game stage

**Inferred:** Grand Doctrine choice is irrevocable until the next war phase (when world tension drops below 20% or a major treaty event occurs; most games see only 1–2 doctrine switches). Commit early.

| Nation | Primary doctrine | Secondary (post-switch) | Rationale |
|---|---|---|---|
| **Germany** | Trade Interdiction | Fleet In Being (late 1942+) | Starts with TI. Rich sub industry (Type VIIC); raiding pays off for 2–3 years. Switch to FIB after U-boat losses mount and surface fleet is ready. |
| **Japan** | Base Strike | Trade Interdiction | Starts with BS. Carrier force (Akagi, Kaga, etc.) is world-class; maximizes native advantage. After Pearl Harbor (early war), enemy air superiority makes carrier battles risky; Trade Interdiction raiding fills the gap. |
| **United Kingdom** | Fleet In Being | Base Strike | Balanced battleship/carrier fleet; FIB supports battleships (KGV-class). After 1943, shift to BS as US joins and brings carrier task forces. |
| **United States** | Base Strike | Trade Interdiction | High carrier production (Essex-class ramp-up). BS maximizes damage output. Switch to TI in Pacific to strangle Japanese logistics. |
| **Soviet Union** | Trade Interdiction | — | Weak carrier industry; strong submarine output via doctrinal bonuses. Stick with TI for entire war; raiding in Black Sea and Arctic. |
| **Italy** | Fleet In Being | — | Limited steel; Regia Marina has modern heavy cruisers. FIB maximizes cruiser armor and firepower for Mediterranean dominance. |
| **France** | Fleet In Being | — | Balanced fleet; FIB is stable choice. Switch to BS only if all battleships are sunk (then commit to carrier development). |
| **Romania, Yugoslavia, Greece, Poland** | Coastal Defense | — | Stick with Coastal Defense for entire war. No need to switch. |

## Tactical fleet arrangements

**Inferred:** Task force arrangement matters less than fleet composition, but certain setups reduce micro and improve outcomes.

### Multi-task-force layouts for Fleet In Being

**Arrangement 1: Concentrated battleline**
- **Fleet:** Main Fleet (Fleet In Being doctrine, Capital Ships mastery).
- **Task force 1 (Battleline):** 3–4 battleships + 9–12 screen ships. Assigned to major theater (Atlantic, Mediterranean, North Sea). Mission: Strike force (intercepts enemy fleets).
- **Task force 2 (Cruiser force):** 4–6 heavy/light cruisers + 6 destroyers. Assigned to secondary theater. Mission: Patrol (detects enemy raiders) + Strike force (interception backup).
- **Task force 3 (Escort):** 8–12 destroyers. Assigned to friendly shipping lanes. Mission: Convoy escort (protects trade route).
- Reasoning: Battleline handles major engagements; cruisers handle raiders; destroyers protect supply. Low micro required; assign regions once and watch.

### Multi-task-force layouts for Base Strike

**Arrangement 1: Separated strike forces**
- **Fleet:** Carrier Fleet (Base Strike doctrine, Carriers mastery).
- **Task force 1 (Carriers):** 3–4 carriers + 6–9 destroyers. Assigned to active theater (near ports or enemy fleet). Mission: Strike force (intercepts enemy fleets) or Port strike (attacks stationary targets).
- **Task force 2 (Backup):** 2–3 carriers + 4–6 destroyers. Assigned to secondary region. Mission: On hold (reserves) until Task force 1 is damaged or defeated.
- **Task force 3 (Surface raiding):** 2–4 heavy cruisers + 4 destroyers. Assigned to trade routes. Mission: Convoy raiding or patrol.
- Reasoning: Concentrated carrier force maximizes alpha strike (air drop damage is 10× if aircraft are based on a carrier in the battle). Backup prevents total fleet loss. Raiding task force handles logistics disruption. Carrier-only fleets are vulnerable to early-war surface engagements before air superiority is established; include 1–2 heavy cruisers in the main carrier task force to trade fire with enemy capital ships.

### Multi-task-force layouts for Trade Interdiction

**Arrangement 1: Distributed raiding**
- **Fleet:** Raiding Fleet (Trade Interdiction doctrine, Submarines mastery).
- **Task force 1 (Atlantic raiders):** 12–15 submarines. Assigned to Atlantic (multiple zones). Mission: Convoy raiding.
- **Task force 2 (Pacific raiders):** 8–10 submarines. Assigned to Far East. Mission: Convoy raiding.
- **Task force 3 (Capital surface raiders):** 2–3 Panzerschiff or heavy cruisers + 4 destroyers. Assigned to major shipping routes (North Atlantic, convoy SL lines). Mission: Convoy raiding + patrol (detects high-value targets).
- Reasoning: Submarines are cheap and can cover vast ocean. Surface raiders are rare but devastating against undefended convoys. 20–25 submarines distributed across key trade routes can destroy 800–1200+ convoys over a 3-year period, inflicting 5,000+ attrition on enemy production via supply disruption. This is cheaper than building a 15-ship battlefleet and requires less micro (submarines auto-engage raiding once assigned to a region).

## Related files

- [Naval warfare overview](../04-naval-warfare/naval-warfare-overview.md) — fleet organization and missions
- [Naval combat](../04-naval-warfare/naval-combat.md) — damage formulas and mechanics
- [Ship designer](../04-naval-warfare/ship-designer.md) — building ships to your doctrine
- [Naval doctrine](../04-naval-warfare/naval-doctrine.md) — doctrine bonuses and mastery tracks
