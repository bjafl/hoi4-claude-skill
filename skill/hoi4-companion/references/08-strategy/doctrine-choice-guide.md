---
title: Doctrine Choice Guide
category: strategy
tags: [doctrine, grand-doctrine, strategy, decision-tree, land-doctrine, air-doctrine, naval-doctrine, special-forces]
game_version: "1.19"
dlc: [Man the Guns, Arms Against Tyranny, No Compromise No Surrender]
sources:
  - https://hoi4.paradoxwikis.com/Land_doctrine
  - https://hoi4.paradoxwikis.com/Air_doctrine
  - https://hoi4.paradoxwikis.com/Naval_doctrine
  - https://hoi4.paradoxwikis.com/Special_forces_doctrine
  - ../02-land-warfare/land-doctrine.md
  - ../03-air-warfare/air-doctrine.md
  - ../04-naval-warfare/naval-doctrine.md
  - ../02-land-warfare/special-forces-doctrine.md
---

## Summary

Doctrine is the deepest strategic commitment in HOI4: switching a Grand Doctrine resets all Mastery in that branch, forcing every subdoctrine to be re-earned at a severe cost. This guide maps doctrine picks to playstyles and nation profiles, covering land, air, naval, and special forces doctrines as an integrated system. **Inferred:** Decide doctrine early (by 1937 for air; by 1939 for land/naval) and commit — the game assumes you stay with your choice.

---

## Land Doctrine: Grand Doctrine Decision Tree

**Inferred:** Pick based on your army's structure: what units actually exist determines what track fills fastest and where your Brigade Size +1 bonus lands.

| Your army structure | Pick | Why |
|---|---|---|
| **Tank-heavy** (30%+ tanks) | Mobile Warfare | Brigade Size +1 on Armor track (4.0× Mastery rate). Speed bonus (+10% division speed, +20% planning) breaks through quickly. Enables Blitz tactic for shock tactics. |
| **Artillery-focused** (multiple line artillery per division) | Superior Firepower | Brigade Size +1 on Artillery & Combat Support track (10.0× rate — fastest). Baseline +10% artillery soft attack locks in firepower superiority early. Army Recovery Rate bonuses (+0.10/+0.20) sustain grinding offensives. |
| **Infantry-only** (40%+ of deployed battalions are leg infantry) | Grand Battleplan or Mass Assault | **Grand Battleplan:** Brigade Size +1 on Infantry track. Max planning +10% suits wide-front play. Command Power +0.25/day + 30-point max bonus fills roles for army spirits/orders. **Mass Assault:** Brigade Size +1 also on Infantry; supply penalty -10% (-5% more than Grand Battleplan) turns logistics into an asset. |
| **Low-industry nation** (cannot sustain artillery or tanks) | Mass Assault | Out-of-supply penalty -10%, Supply Grace +48h, Minimum Training Level -5% (×2) turn cheap troops into quantity-focused attacks. Pairs with Irregulars, People's Militia, Desperate Defense. |
| **Uncertain/flexible early** (no war before 1938, unsure army shape) | Superior Firepower | Lowest risk. Artillery & Combat Support track gains Mastery fastest (10.0×), unlocking Brigade Size +1 earliest without committing to tanks. Soft attack bonuses apply broadly. |

**Inferred:** Do not switch Grand Doctrine mid-war — recovery from Mastery reset takes 12+ months of intensive combat.

### Subdoctrine picks within your chosen Grand Doctrine

**Inferred:** After choosing Grand Doctrine, select subdoctrines to maximize Mastery gain and exploit your unit composition.

| Grand Doctrine | First subdoctrine pick | Second/Third picks | Late-game pivots |
|---|---|---|---|
| **Mobile Warfare** | **Mobile Infantry** (Infantry track) — enables Overwhelming Fire tactic immediately, +10% breakthrough on infantry | **Armored Spearhead** (Armor track) — feeds Brigade Size +1 milestone, +10% Breakthrough on armor by M200 | **Streamlined Deployment** (Armor) if you've built Medium/Mechanized; **Mission-Type Tactics** (Operations) for command power flexibility |
| **Superior Firepower** | **Fire Concentration** (Artillery & Combat Support) — enables Overwhelming Fire, feeds Brigade Size +1 fastest | **Assault Infantry** (Infantry) — organic fire support, combines with artillery baseline to multiply soft attack | **Large Unit Tactics** (Infantry) — M200 grants Infantry Unit Design Cost -100%, freeing army XP for division editing; **Infiltration Tactics** (Operations) for nighttime attacks (-25%) |
| **Grand Battleplan** | **Mission-Type Tactics** (Operations) — +0.02 command power gain early, +15 org on infantry, feeds planning bonuses | **Fire Concentration** (Artillery & Combat Support) — locks in Overwhelming Fire tactic, feeds coordination bonuses | **Infiltration Tactics** (Operations) for night attacks; **Grand Assault** (Operations) if you've built paratroopers or need air/coordination bonuses |
| **Mass Assault** | **Irregulars** (Infantry) if low-industry; **People's Militia** (Infantry, requires Communism) for identical value but tighter narrative; else **Defensive Postures** (Infantry) | **Field Engineering** (Artillery & Combat Support) — bridges river/forest movement penalties, Smoke Projector Training M400 gives +50% Breakthrough | **Desperate Defense** (Operations, only in defensive war) unlocks Supply Grace +72h on top of Mass Assault's +48h |

**Inferred:** Subdoctrine choice is loose — what matters is that track selection matches your army and you keep those units in combat to build Mastery.

---

## Air Doctrine: Grand Doctrine Decision Tree

**Inferred:** Air doctrine choice determines where your air experience is spent first and lasts your entire air war (switching resets all Air Mastery). Decide by researching what aircraft you will build.

| Your air strategy | Pick Grand Doctrine | Fighter subdoctrine | Strike subdoctrine | Medium subdoctrine | Heavy subdoctrine |
|---|---|---|---|---|---|
| **Blitzkrieg / fast ground war** | **Battlefield Support** | **Airspace Dominance** (Air Sup Eff +10%, seize the skies) or **Medium-Range Escort** (range to reach army) | **Pinpoint Strikes** (CAS Ground Attack +10%, maximize ground damage) | **Tactical Battlefield Support** (TAC Ground Attack +10%, pave the way) | _Leave unselected or pick **Deep Air Raids** for long-range interdiction_ |
| **Win air superiority, then operationally dominate** | **Operational Integrity** | **Airspace Dominance** (Air Sup Eff +10%, Interception Detection +20% milestones) or **Knights of the Air** (Ace Generation +10%, experience gains) | **Pinpoint Strikes** or **Flying Artillery** (CAS Air Defense +15%, tank killers) | **Operational Air Support** (Air Mission Eff +5%, broad survivability) — milestone grants Air Superiority +10% | **Carpet Bombing** or **Deep Air Raids** (raw damage, range) |
| **Strategic bombing campaign** | **Strategic Destruction** | **Medium-Range Escort** (Fighter Range +10%, bomber escort) or **Airspace Dominance** (dogfight wins if bomber coverage is weak) | **Flying Artillery** or **Ground-Naval Coordination** (flexible) | **Theater Interdiction** (Strategic Bombing +15%, range) or **Heavy Interceptors** (if enemy has strategic bombers) | **Carpet Bombing** (Strategic Bombers Strat. Bombing +20%, +10% more at M300) or **Deep Air Raids** (Range +10%) |
| **Carrier navy** | **Base Strike** | **Naval Aviation** (Sortie Eff +15%, Carrier fighter agility +10%) | **Sea-To-Shore Air Power** (Carrier CAS Range +10%, Carrier Naval Bombers Range +10%) or **Precision Naval Bombing** (Naval Mission Eff +12%, survivability) | _Leave unselected; use Medium for escorting heavy aircraft only_ | **Deep Ocean Air Patrol** (Maritime Patrol Bombers Range +15%, Naval Attack +10%) or **Coastal Air Patrol** (Naval Attack +10%) |
| **Minor / limited production** | **Battlefield Support** | **Fighter-Bombers** (Fighter Ground Attack +10%, one plane does two jobs) | **Flying Artillery** (robust, defensive) | _Leave unselected if no heavy fighters_ | _Do not pick; let heavy auto-complete_ |

**Inferred:** Mastery only accrues when aircraft types actually fly. Selecting a Heavy Aircraft subdoctrine with no strategic bombers in your air force wastes nothing — up to 200 Mastery banks (at 25% rate if unselected) and can be spent later once you build heavy bombers.

**Inferred:** Detection bonuses (Fighter/Interception Detection +20%, +15%) are undervalued. They convert idle friendly aircraft into fighting aircraft because enemy planes above the detection cap cannot engage. Often worth more than a +5% stat percentage.

---

## Naval Doctrine: Grand Doctrine Decision Tree

Requires **Man the Guns** DLC.

| Your navy composition | Pick Grand Doctrine | Submarine subdoctrine | Screens subdoctrine | Capital Ships subdoctrine | Carrier subdoctrine |
|---|---|---|---|---|---|
| **Battleship-heavy, defensive** | **Fleet In Being** | **Capital Hunters** (Torpedo hit chance +15%, sink capital ships) or **Long Range Submarines** (support battlefleet) | **Convoy Escort** (protect trade) or **Hunter Killer Groups** (anti-submarine, if enemy has subs) | **Line of Battle** (Navy Fuel -5%, big-gun doctrine) or **Fast Battleships** (mobility and critical hits +3%) | **Carrier Battlegroups** (Port strikes +20%, carrier AA +35% at M500) if you have carriers; else leave unselected |
| **Submarine raider, commerce destruction** | **Trade Interdiction** | **Wolfpacks** (Organization +10, Retreat Speed +15%, raiding +20% at M200) or **Coastal Minelaying** (naval mines damage +25%, minesweeping becomes destroyers' job) | **The New School** (Convoy Raiding Eff +30%, swarm tactics) | **Armored Raiders** (Supply -10%, Raiding Eff +25% at M400) — if you also have capital ships raiding | **Generalized Support** (Repair/Support ships boost, if special projects) |
| **Carrier-centric strike navy** | **Base Strike** | **Naval Targeting** (Torpedo reveal -10%), any subdoctrine; **Long Range Submarines** if supporting strikes | **Integrated Operations** or **Hunter Killer Groups** (fleet coordination) | **Naval Gunfire Support** (if shore bombardment; else leave unselected or pick **Anti-Aircraft Battleships** if you fear enemy air) | **Floating Airfields** (Sortie Eff +10%, Carrier Overcrowding -20%, Air Group Attack +15%) or **Massed Carrier Fleet** (Carrier Traffic +30% at M500, Range +20%) |
| **Fleet battle (all types together)** | **Fleet In Being** | **Fleet Operations** (integrate subs into battle line, Torpedo screen penetration +5%) | **Integrated Operations** (speed as armor, fast cruisers matter) | **Line of Battle** (fuel efficiency, organization) | **Carrier Battlegroups** (milestones grant Naval Targeting +10%, Sortie Eff +30%) or **Massed Carrier Fleet** (screen bonus +30% at M200, carrier traffic +30%) |

**Inferred:** Naval Mastery accrues slowly because ship combat is rare and decisive. Focus subdoctrines on units you actually deploy; leave low-priority tracks unselected so Mastery banks at 25% for future pivots.

**Inferred:** **Base Strike** grand doctrine's Port Strikes +40% only matters if your enemy fleet sits in ports regularly. Against an active enemy fleet at sea, it provides little value; switch to **Fleet In Being** or **Trade Interdiction** instead.

---

## Special Forces Doctrine

Requires **Arms Against Tyranny**; Rangers require **No Compromise, No Surrender**. (Without AAT, use Special Forces Concentration tech line.)

### When to pick a branch

**Inferred:** You start with exactly one **Special Forces Branch Specialization (SFBS)** and it is permanently spent. Decide based on war plan, not flavour.

| Planned war activity | Pick SFBS for | Why |
|---|---|---|
| Naval invasions across sea or large rivers | **Marines** | +50% amphibious attack on Marines is the single biggest invasion modifier. Expeditionary Units M240 adds +20% invasion planning and +15% shore bombardment. |
| Fighting in Alps, Caucasus, Balkans, China, Norway, Spain | **Mountaineers** | Mountains and hills are where infantry attacks stall. Mountain Infantry +35% attack, +10% defense in mountains unblocks fronts. Cold Weather Specialists adds +15% snow movement and attack. |
| Airfield/port seizure, encirclement cutoff, need speed/surprise | **Paratroopers** | Only unit type that can paradrop. Constraints: needs transport planes, air superiority, pure paratrooper division template. AI never paradrops, so this is solo-play only. |
| Broad/balanced, unsure of war plan | **Marines** | Most flexible. Naval invasions are the easiest special-forces operation to execute (just move to coast, assault). Marines unlock Pioneers and Amphibious designs. |

**Inferred:** A major country gets a second SFBS from **Diversify Elite Forces** decision (1 Jan 1940+). Minors do not; pick carefully.

### Grand Doctrine and cap strategy

| Goal | Pick Grand Doctrine | Track strategy |
|---|---|---|
| Field as many special forces as possible (50+ battalions) | **Expanded Special Forces** | Master both tracks to get +4% capacity per track (8% total); pick subdoctrines with -50% cap contribution reductions (all have them). |
| Elite small force (24-battalion minimum cap, never more) | **Elite Special Forces** | Leave tracks unselected; bonuses are flat (Org +10, Supply Grace +24h). You get Breakthrough +5%, Soft Attack +5% on milestones without spending Mastery on Expanded's +4% capacity per track. |
| Hybrid (moderate cap, strong units) | **Expanded Special Forces** | Master only the first track to reach +4% capacity. Leave second track unselected. You get +5% soft attack and +5 org on first-track milestone, enough to be effective without committing to double Mastery. |

**Inferred:** With cap-contribution reductions stacking (-50% per type, doubled if you pick two subdoctrines of different types with both at -50% cap-contribution reduction each), you can field roughly double the battalion count your raw cap suggests. Example: 48-battalion-cap AAT nation with two -50% reduction types fielding effectively 96 battalions across deployed divisions.

---

## Cross-Branch Synergies

**Inferred:** Grand doctrine picks across land, air, and naval branches do not interact mechanically, but they telegraph strategy to the AI and player.

| Strategy | Land Grand Doctrine | Air Grand Doctrine | Naval Grand Doctrine | Why this combo |
|---|---|---|---|---|
| **Aggressive early conquest (Blitzkrieg)** | Mobile Warfare | Battlefield Support | Trade Interdiction (raiding supply) or Base Strike (if you have carriers) | Speed and air support synergize; naval pressure via supply denial or carrier strikes. Land doctrine enables Blitz tactic; air doctrine gives CAS bonus +20%; naval doctrine disrupts enemy logistics. |
| **Slow methodical front grinding** | Grand Battleplan or Mass Assault | Operational Integrity | Fleet In Being | Planning bonuses and command-power depth suit meticulous play. Operational Integrity's Interception Detection +20% denies enemy air cover; Fleet In Being defends your coast while you grind. |
| **Economic strangulation** | Mass Assault (cheap, manpower-focused) | Strategic Destruction | Trade Interdiction | Combine manpower spam with strategic bombing (destroy factories) and commerce raiding (destroy convoys). Starve enemy of both production and supplies. |
| **Defensive holdout until superior tech** | Grand Battleplan or Mass Assault | Operational Integrity | Fleet In Being | Max planning and supply-denial focus on sustaining defense. Operational Integrity's Interception Detection +20% denies enemy air. Fleet In Being holds the line at sea. |
| **Carrier-centric power projection** | Mobile Warfare (speed for fleet mobility) | Battlefield Support or Operational Integrity | Base Strike | Speed to reposition fleet; air support for island invasions; carriers as primary striking force. |

---

## Practical Decision Framework

### Early war (1936–1937)

1. **Decide Grand Doctrine for air:** by early 1937. Air experience accrues slowly; committing early frees experience for subdoctrines by 1938–1939.
2. **Decide Grand Doctrine for land:** by mid-1937 if you expect war by 1939; by late 1937 if you expect to be at peace until 1940+.
3. **Naval and special forces:** defer to mid-1939 unless you are building a navy or planning invasions immediately.

**Inferred:** Delaying Grand Doctrine pick costs nothing until you research the first doctrine (land at 100 army XP, air at 100 air XP, naval at 100 navy XP). But delaying leaves you at default doctrine bonuses (none) longer.

### Mid war (1938–1940)

1. **First subdoctrine:** pick for your dominant unit type (tanks → Armor track; artillery → Artillery & Combat Support; infantry → Infantry or Operations).
2. **Mastery accumulation:** combat generates Mastery. Keep those unit types engaged to fill the first milestone (100 Mastery).
3. **Special forces (AAT nations only):** decide SFBS by early 1940 if you want a second branch from Diversify Elite Forces decision.

### Late war (1941+)

1. **Do not switch Grand Doctrines.** Mastery reset is catastrophic; losing months of buildup is not worth fixing a 1938 decision.
2. **Pivot subdoctrines:** low cost (Mastery reset only), but still takes weeks to re-earn first milestones.
3. **Special projects:** if you reach Siege Artillery (Super-heavy Howitzer), Air Cavalry (Helicopter), Escort Carrier, or Support Ships, these open new high-value subdoctrine options.

---

## Mastery Accumulation Rates and Timelines

**Inferred:** These are rough estimates based on typical mid-sized division compositions.

| Track | Multiplier | Typical gain rate (full combat) | Time to M100 (first milestone) | Notes |
|---|---|---|---|---|
| **Land: Infantry** | 1.0× | 2–5 per day | 20–50 days | Depends on number of infantry battalions in combat; more divisions = faster. |
| **Land: Artillery & Combat Support** | 10.0× | 20–50 per day | 2–5 days | Fastest track. One line artillery battalion in combat earns 1 Mastery/day; ten earn 10. |
| **Land: Armor** | 4.0× | 8–20 per day | 5–12 days | Faster than infantry but slower than artillery; typical mid-tank forces. |
| **Land: Operations** | 0.7× | 1–3 per day | 33–100 days | Slowest; fed by everything but at 70% rate. Fills in the background during grinding. |
| **Air: All tracks** | _variable_ | 1–3 per day (combat) | 30–100 days | Highly dependent on air combat frequency. Training accrues at ~10% of combat rate. |
| **Naval: All tracks** | _variable_ | <1 per day | 100+ days | Naval combat is rare; expect weeks between milestones unless you are in full war. |
| **Special Forces: All types** | _variable_ | 2–5 per day | 12–30 days | Faster than land tracks; fed by elite unit combat. |

**Inferred:** In a land war at full intensity (multiple fronts, daily fighting), you will complete land Grand Doctrine milestones (500 Mastery) in 2–6 months depending on which track you emphasize. Naval doctrines take 2–3 years if your navy sees regular action.

---

## Common Mistakes and How to Avoid Them

| Mistake | Consequence | How to avoid |
|---|---|---|
| **Switching Grand Doctrine mid-war** | Lose all Mastery; start from zero on all tracks. Recovery takes 6–12 months. | Commit early (by 1937 for air, by 1938 for land). If you pick wrong, push through — switching costs more than staying. |
| **Picking Grand Doctrine for infantry when you build tanks** | Brigade Size +1 is locked behind a track (Armor, Artillery & Combat Support, or Infantry) that does not fill. You never master it and lose a stat point. | Match Grand Doctrine to your army: tank-heavy → Mobile Warfare (Armor track carries Brigade Size); artillery-heavy → Superior Firepower (Artillery & Combat Support carries it). |
| **Leaving a track selected with zero relevant units** | Mastery does not bank; you waste gains that could have banked at 25% for later use. | If you pick a subdoctrine but have no units of that type (e.g., Heavy Aircraft subdoctrine but no strategic bombers), leave it unselected until you build them. |
| **Picking naval doctrine when you have no navy** | Navy experience accrues slowly (~0.5 per day without combat). You waste experience on a doctrine that will not see use. | Defer naval doctrine until your navy exists (usually mid-1939+). Early game, leave naval experience unspent; redirect it to army/air. |
| **Picking Paratroopers (special forces) without transport planes or air superiority** | Paradrop operations fail (need air superiority and transport planes). You spend an SFBS on a unit type you cannot deploy. | If you lack air force or transport capacity by 1940, do not pick Paratroopers. Pick Marines (always deployable via amphibious assault) or Mountaineers (always deployable on foot). |
| **Mastery banking misunderstanding** | You pick a subdoctrine that does not match your unit composition. Mastery fills slowly; you delay milestone unlocks. | Match subdoctrine to units in combat. Mobile Infantry on an artillery-heavy division fills slowly (gains from Mot/Mech only, not line artillery). Pick **Assault Infantry** instead (gains from Support Artillery). |

---

## See also

- [Land doctrine](../02-land-warfare/land-doctrine.md) — subdoctrine details, Mastery formulas
- [Air doctrine](../03-air-warfare/air-doctrine.md) — aircraft types, mission modifiers
- [Naval doctrine](../04-naval-warfare/naval-doctrine.md) — ship types, combat mechanics
- [Special forces doctrine](../02-land-warfare/special-forces-doctrine.md) — elite units, cap system
- [Officer Corps](../01-mechanics/officer-corps-and-commanders.md) — how experience is earned and spent
