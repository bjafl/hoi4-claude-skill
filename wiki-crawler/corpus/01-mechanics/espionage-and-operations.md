---
title: Espionage and Operations
category: mechanics
tags: [espionage, intel, intelligence-agency, operatives, operations, missions, cryptology, spy-network, collaboration, resistance, counter-intelligence]
game_version: "1.19"
dlc: [La Résistance]
sources:
  - https://hoi4.paradoxwikis.com/Intel
  - https://hoi4.paradoxwikis.com/Intelligence_agency
  - https://hoi4.paradoxwikis.com/Operatives
  - https://hoi4.paradoxwikis.com/Operations
  - https://hoi4.paradoxwikis.com/Missions
  - https://hoi4.paradoxwikis.com/List_of_operations
  - https://hoi4.paradoxwikis.com/List_of_operatives
  - https://hoi4.paradoxwikis.com/List_of_intelligence_agencies
---

## Summary

Intel exists in four independent pools — civilian, army, navy and air — each tracked per target country from 0% to 100%, fed by ideology, trade law, combat, radar, and (with La Résistance) intelligence agencies, spy networks, operations, decryption, captured operatives and air recon. An intelligence agency costs 5 civilian factories for 30 days, unlocks operatives, and can be upgraded across five branches. Operatives run continuous **missions** on the map and one-off **operations** against target countries. Base-game intel exists without La Résistance, but everything involving agencies, operatives, missions and operations requires it.

## Intel types

| Type | Covers | Direct bonus |
|---|---|---|
| Civilian intel | Production, laws, trade, resources, manpower, logistics; engineering and industry technologies | None — information only |
| Army intel | Land units, special forces, stockpiles (including variants and tank designs), land doctrines, army officer-corps spirits; infantry/support/armor/artillery technologies | Land combat bonus to the side with more army intel |
| Navy intel | Ships and designs, naval bases, active naval missions, naval doctrines, navy spirits; naval and naval-support technologies | Low navy intel penalises contesting naval supremacy; higher navy intel gives spotting and mine-damage benefits |
| Air intel | Aircraft and designs, air bases, active air missions, air doctrines, air spirits; air technologies | Earlier detection of incoming raids |

Intel is read in the **Intel Ledger** (diplomacy menu → Intel Ledger tab). All laws, national spirits, design companies, officer-corps selections and military high command are **always visible** regardless of intel.

## Intel sources

### Ideology and trade law (what the *target* leaks)

| Ideology | Civilian intel | Army intel | Navy intel | Air intel |
|---|---|---|---|---|
| Democratic | +20% | +5% | +20% | +5% |
| Communist | +10% | +7.5% | +12.5% | +7.5% |
| Fascist | +15% | +10% | +10% | +10% |
| Non-Aligned | +20% | +10% | +20% | +10% |

| Trade law | Civilian intel | Navy intel |
|---|---|---|
| Free Trade | +40% | +20% |
| Export Focus | +20% | +10% |
| Limited Exports | +10% | +5% |
| Closed Economy | +0% | +0% |
| Embargoed Economy | +40% | +40% |
| Autarky | +0% | +0% |
| Special Economic Zones | +80% | +30% |

Intel given away can be cut by national spirits and political advisors — notably Germany's **MEFO Bills** spirit and the Soviet **Do Not Blab** decision (unlocked by SMERSH). The officer-corps spirits **Best of the Best** (army, navy) and **Branch Independence Spirit** (air) also reduce intel given away.

**Faction sharing:** an observer in a faction with an ally who has more intel of a given type on the target receives **30% of the difference** as bonus intel of that type.

### Intel from combat

Each combat source has an **effective cap** (the most it can actually add) and a **hard cap** (a buffer that absorbs decay first, without contributing directly).

| Source | Intel type | Effective cap | Hard cap | Decay |
|---|---|---|---|---|
| Raiding trade convoys | Civilian | +10% | +15% | 0.985× per day |
| Land battles | Army | +30% | +40% | 0.985× per day |
| Naval battles | Navy | +40% | +45% | 0.985× per day |
| Air combat | Air | +25% | +30% | 0.985× per day |
| Land battles with enemy aircraft | Air | +10% | +15% | 0.985× per day |
| Naval battles with enemy aircraft | Air | +20% | +25% | 0.985× per day |

**Civilian (convoy raiding):** base **+1% per trade convoy per day**.

**Army (land battles):** base daily rate = (**+1% per active land battle** + **0.5% per enemy division actively fighting** + **0.1% per enemy division in reserve** + **0.2% per enemy division retreating**) × **0.01**. The base is then multiplied by **1.075× per point of reconnaissance** the observer or its allies have in the battle (raised further by the **Aggressive Reconnaissance** officer-corps spirit, No Step Back). Applied gain:

```
Daily intel gain = 0.25 × ln(1 + base intel gain) + base intel gain / 10
```

**Navy (naval battles):** base daily rate = **+1% per naval battle**, **+0.2% per enemy submarine**, **+0.5% per enemy screen ship**, **+1% per enemy capital ship**, **+0.05% per aircraft hosted on carriers**. Applied gain:

```
Daily intel gain = 0.02 × ln(1 + base intel gain) + base intel gain / 200
```

**Air (air combat):** base = (**+1% per strategic region with air combat** + **0% per enemy plane**) × **0.2**. Applied gain:

```
Daily intel gain = 1 × ln(1 + base intel gain) + base intel gain / 2
```

**Air from land battles:** base = (**+1% per land battle with ≥1 enemy aircraft** + **0.1% per enemy plane**) × **0.01**, then modified by the land-battle dynamic rate and recon.
**Air from naval battles:** base = (**+1% per naval battle with ≥1 enemy aircraft** + **0% per enemy carrier aircraft** + **0.01% per enemy non-carrier aircraft**) × **1**.

### Radar stations

Radar intel is **static** — gained and lost instantly. Maximum contribution overall: **+10% civilian, +10% army, +20% navy, +20% air**.

- **Intel gathering efficiency** depends on radar level: **125% at level 6**, decreasing linearly to about **20.833% at level 1**. Extra stations covering the same province each count at **0.5×**.
- At **100% radar coverage of a country's controlled land provinces**: **+9% civilian, +9% army, +0% navy, +18% air**, scaled by station efficiency and by the fraction of provinces covered.
- Per station, by land provinces of the target it covers: up to **+5% civilian, +5% army, +0% navy, +12% air**, × station efficiency × (target-controlled land provinces covered ÷ total provinces covered).
- Over sea provinces, by ship type in the strategic region: **submarine +5%, screen +10%, capital ship +20%, carrier +30% navy intel**, × radar coverage of the region × station efficiency.
- Over convoy routes (trade, supply, troop transport): baseline **+0% civilian, +0% army, +280% navy, +0% air** per station per strategic region, × fraction of the target's convoys through that region × efficiency × coverage.

### Intelligence agency sources (La Résistance)

- **Intelligence branch upgrades** give a **multiplicative** bonus to all gathered intel of their type (+25% each).
- **Intel networks** cap at **+30% civilian, +30% army, +40% navy, +30% air**, scaled by **2× the network's coverage** of the target country. Active and quiet networks both count. Boosted by the **Invisible Ink** upgrade. Navy intel is based on **naval base coverage** instead of state coverage, with a **15× state-coverage multiplier** if no naval bases are covered (still capped at +40%).
- **Infiltration operations** each give **+10%** of their matching intel type while the infiltration lasts. **Make Resistance Contacts** gives **+5% army intel** while resistance operations are available. (Known bug: infiltrations are removed on save reload and must be redone.)
- **Cryptology:** passive decryption gives **+10% of each intel type**; **revealing** cracked ciphers raises this to **+60% of each type for 30 days**.
- **Captured operatives:** base **+0.3% of each intel type per day**, multiplied by a random **10×–35×** factor. Raised by **Interrogation techniques**, reduced if the operative has the **Tough** trait. Applied gain uses `1 × ln(1 + base) + base/2`. Decays at **0.95× per day** once no captured operatives remain.

| Captured-operative intel | Effective cap | Hard cap |
|---|---|---|
| Civilian | +50% | +50% |
| Army | +40% | +40% |
| Navy | +40% | +40% |
| Air | +30% | +30% |

### Air Recon

The **Air Recon** air mission gathers all four intel types over the countries flown over. Dedicated **scout planes** can fly it over neutral *and* enemy countries and need wings of only **10 aircraft**. With **By Blood Alone**, any aircraft with a **Recon Camera** module can fly it, but non-scout planes give intel on **enemies only**.

| Air Recon intel | Effective cap | Hard cap |
|---|---|---|
| Civilian | +25% | +30% |
| Army | +20% | +25% |
| Navy | +30% | +35% |
| Air | +20% | +25% |

- Base **+0.02% per plane per strategic region**.
- Per land strategic region: up to **+10% civilian, +6% army, +0% navy, +3% air**.
- Per sea strategic region: up to **+0% civilian, +0% army, +10% navy, +0% air**.
- Applied gain: `0.05 × ln(1 + base) + base/200`. Decays at **0.995× per day** when the mission is not maintained.

### Legacy cryptology (without La Résistance)

Decryption vs encryption levels (mainly from computing technologies). Matching levels give **+15% of each intel type** — unless the observer's decryption level is 0, which gives nothing.

```
Final intel bonus = base intel bonus × (1 + observer decryption level) / (1 + target encryption level)
```

## Intel effects

### Army intel combat bonus

If the observer has more army intel than the target has on them, from a difference of **at least 5 percentage points**, the observer gets **+0.3% soft attack, hard attack, defense and breakthrough per percentage point of difference**, capped at **+15% at a 50-point difference**.

### Navy intel effects

- Too little navy intel penalises naval supremacy against that country (see the naval-invasion section of [Officer corps and commanders](officer-corps-and-commanders.md): at ≤10% intel supremacy is halved, improving linearly to no penalty at 40%).
- From a **≥5 point** navy intel lead: **+0.25% spotting speed per point**, capped at **+10% at a 40-point lead**; the target takes a mirrored **−0.25% per point**, capped at **−10%**.
- With **Man the Guns**, from a ≥5-point lead: **−1.25% damage from the target's naval mines per point**, capped at **−50% at a 40-point lead**.

### Air intel effects

- **10% air intel** is the minimum to be told when a raid has launched.
- Every additional percentage point of air intel lets a raid be detected **one percentage point earlier in its preparation**: 30% intel → detected at 70% preparation; 50% → 50%; 70% → 30%.
- Air intel gives **no air-combat bonus**; decrypted ciphers do (La Résistance).

### Civilian intel ledger thresholds

| Civilian intel | What becomes visible |
|---|---|
| 0% | Resources produced and traded; building counts by state (±70%, narrowing) |
| 10% | Factory counts and distribution, manpower, convoy count, trucks, trains, supply ranges (all ±50%, narrowing); trade partners |
| 30% | Fuel reserves (±50%); factories graph; building counts by state tighten to ±49%; anti-air damage reduction |
| 50% | **Exact** factory counts and distribution, exact trucks, exact trains, exact supply ranges; resource origins; completed focuses; number of completed engineering and industry technologies; trucks and trains graphs |
| 70% | **Exact** fuel reserves and manpower reserves; trade partners **and convoy routes**; active focus with progress; full list of completed engineering and industry technologies; convoys graph |
| 80% | Currently-researching engineering and industry technologies; bombers graph |
| 90% | Resource origins **and convoy routes** |
| 100% | **Exact** convoy count |

### Army intel ledger thresholds

| Army intel | What becomes visible |
|---|---|
| 0% | Total special forces battalion count (±70%, narrowing) |
| 5% | Total fielded division count (±80%, narrowing) |
| 10% | Fielded manpower (±50%, narrowing) |
| 30% | Basic division template info; equipment stockpiles (±50%); number of completed infantry / support / armor / artillery technologies and land doctrines |
| 50% | Division count by template (±100%, narrowing); supply convoy routes |
| 70% | **Exact** division count, exact fielded manpower, exact division count by template; **exact** equipment stockpiles and overall division equipped ratio; full completed-technology list; exact supply convoy information |
| 80% | **Exact** template info; **exact equipment variant stats** including tank designs *(NSB)* and aircraft designs *(BBA)*; currently-researching technologies; **cannot be targeted by Plant False Intelligence** from the target |
| 90% | **Reveals existing Fake Intel divisions** |
| 100% | Exact total special forces battalion count |

### Navy intel ledger thresholds

| Navy intel | What becomes visible |
|---|---|
| 0% | Nearby naval bases |
| 5% | Deployed naval manpower (±50%, narrowing) |
| 10% | Total fleet count and total ship count (±50%); deployed ship types; nearby naval bases **with levels** |
| 30% | **Exact** total fleet count; total task force count (±50%); ship types with counts (±50%); all naval bases with levels and task force counts (±50%); number of completed naval technologies, naval support technologies and naval doctrines |
| 50% | Assigned naval missions; ship variant and design **types and names** |
| 70% | **Exact** task force count, exact ship-type counts, exact naval manpower, exact task force counts per base; full completed-technology list |
| 80% | **Exact** total ship count; naval missions **with task force counts**; naval bases with details; **full ship variant and design details**; currently-researching technologies |

### Air intel ledger thresholds

| Air intel | What becomes visible |
|---|---|
| 0% | Total air wing count (±50%, narrowing); nearby air bases |
| 10% | Deployed air wing manpower (±50%, narrowing) |
| 30% | Deployed air wing types; air missions with plane counts (±50%); all air bases with plane counts (±50%); number of completed air technologies and air doctrines |
| 50% | Air wing types **with counts** (±50%) |
| 60% | Air missions with **exact** plane counts |
| 70% | **Exact** air wing count, exact types with counts, exact air wing manpower, exact plane counts per base; full completed-technology list |
| 80% | Air bases with details; **aircraft variants and designs**; currently-researching air technologies |

## Intelligence agency

- Cost to found: **5 civilian factories for 30 days**.
- Each upgrade: a variable number of civilian factories for **30 days**, cut by **−15% (to 25 days)** with an **Illusive Gentleman** advisor.
- Five branches: Intelligence, Defense, Operations, Operative Training, Cryptology Department.

### Intelligence branch

| Upgrade | Effect | Civilian factory cost |
|---|---|---|
| Economy/civilian | Civilian intelligence +25% | 5 |
| Army Department | Army intelligence +25% | 5 |
| Naval Department | Naval intelligence +25% | 5 |
| Airforce Department | Air intelligence +25% | 5 |

### Defense branch

| Upgrade | Effect | Civilian factory cost |
|---|---|---|
| Passive defense | Counter intelligence: **+1.5** (1st upgrade), **+1.25** (2nd), **+1** (3rd and 4th) | 5 |
| Anti-partisan | Root Out Resistance mission effects **+25%** (1st and 2nd upgrades) | 5 |

Counter intelligence increases the execution time of hostile operations on your territory and the chance of stopping enemy operatives.

### Operations branch

| Upgrade | Effect | Civilian factory cost | Prerequisite |
|---|---|---|---|
| Blueprint stealing | Steal Blueprint effectiveness +25% | 5 | — |
| Portable radios | Coordinated Strike effectiveness +100% | 8 | Radio technology researched |
| Invisible Ink | Intelligence gained from operatives and infiltrated assets +20%; Steal Blueprint risk −25% | 5 | — |
| Plastic explosives | Targeted Sabotage efficiency +25%; Strengthen Resistance efficiency +25% | 8 | — |
| Suicide pills | Death chance of our operative on capture +10%; own operative detection chance offset −0.05% | 5 | — |

### Operative Training branch

| Upgrade | Effect | Civilian factory cost |
|---|---|---|
| Localized training centers | Enemy nationality recruit chance +25%; occupied friendly nationality recruit chance +25%; operative recruitment choices +1; unlocks Local Agent Recruitment decisions | 10 |
| Commando training | Chance of recruiting an operative with the Commando trait +100%; (hidden) allows operatives to earn experience toward Commando | 5 |
| Interrogation techniques | Enemy operative capture chance +100%; enemy operative intel extraction rate +25% | 5 |
| Diplomatic Training | Control Trade and Diplomatic Pressure mission effects +25% each | 5 |
| Psychological Warfare | Propaganda and Boost Ideology mission effects +25% each | 8 |

### Cryptology Department branch

| Upgrade | Effect | Civilian factory cost | Prerequisite |
|---|---|---|---|
| Form Department | Decryption power +25; Cryptology level +1; unlocks the Cryptology Department | 8 | — |
| Radio Interception Group | Decryption power **+25** (1st), **+10** (2nd) | 5 | Form Department |
| Machine-Assisted Decryption | Decryption power **+25** (1st), **+15** (2nd), **+10** (3rd) | 10 | All Radio Interception Group upgrades; Mechanical Computing researched |
| Government Cypher School | Cryptology level **+1** each (1st, 2nd, 3rd) | 5 | Form Department |
| Machine-Assisted Encryption | Cryptology level **+2** each (1st, 2nd, 3rd) | 15 | All Government Cypher School upgrades; Mechanical Computing researched |

## Cryptology

- **Cryptology level** is defensive (protects your ciphers); **Decryption power** is offensive (accumulates daily toward breaking an enemy's cipher).

```
Total cryptology strength to break = 12000 + 4250 × Cryptology level
```

- Starting cryptology level **0** requires **12,000** accumulated decryption power to break; **level 7** requires **41,750**.
- Decrypting several countries at once **splits decryption power evenly** (50 power against two targets = 25 each). Pausing one target sends the full power to the other.
- **Countries not at war suffer −50% decryption power.**

**Passive bonuses from a cracked cipher:**
- Air detection +5.0%
- Interception mission efficiency +25%
- Decrypted civilian / army / navy / airforce cipher bonus +10% each

**Active bonuses when revealing the cracked codes (30 days):**
- Invasion penalty −15%
- Planning speed +50.0%
- Defense bonus against the country +15.0%
- Invasion preparation speed +50.0%
- Breakthrough bonus against the country +15.0%
- Decrypted civilian / army / navy / airforce cipher bonus +50% each

After 30 days the opponent changes codes and **decryption progress resets to 50%**.

## Spy Master

Requirements: the agency has been **upgraded at least 3 times**, the country is independent or a high-autonomy puppet (Dominion, Satellite, Imperial Subject, Supervised state), and it is in a faction. Cost: **50 political power**. One Spy Master per faction; any member can pay 50 PP to take over.

Extra operative slots from being Spy Master:

| Faction member (independent or high-autonomy puppet) | Extra operative slots |
|---|---|
| 10–49 factories | +0.25 |
| 50+ factories | +0.5 |

Factory count includes military and civilian factories but **not naval dockyards**.

## Operatives

### Slots and hiring

- Founding an agency unlocks **1 operative slot**; **5 agency upgrades** unlock **1 more**.
- Further slots: **Illusive Gentleman** advisor, Spy Master of a large faction, certain national focuses.
- **Maximum 10 active operatives.**
- A vacant slot (new, dismissed or killed operative) requires a **mandatory 30-day wait** before hiring.
- New operatives start at **skill level 1**.

### Skill levels

| Level | Description | Experience required | Build Network intel gain | Counter intelligence | Operation success chance |
|---|---|---|---|---|---|
| 1 | Recruit | 100 | — | — | — |
| 2 | Agent | 1000 | +0.25 | +0.25 | +10% |

> ⚠️ The wiki's operative skill table only lists levels 1–2; higher operative levels exist in game but their thresholds and bonuses are not documented on the wiki.

### Innate traits

Cannot be earned. Operative candidates have a **50% chance of at least one** innate trait and a further **10% chance of a second**.

| Trait | Effect | Starting weight |
|---|---|---|
| Double Agent | Bonus to operating in country of origin; never defects to another country | 0 (only appears on captured operatives who defect) |
| Safe Cracker | Capture Cipher effectiveness +25%; Steal Blueprints risk −25%; Steal Blueprints effectiveness +25% | 0.5 |
| Seducer | Own operative detection chance factor −20%; Infiltration effectiveness +25%; Infiltration risk −25% | 1.0 |
| Tough | Enemy operative intel extraction rate −50% | 1.0 |

### Earnable traits

Candidates also have a **25% chance of at least one** earnable trait at hire, plus **5% for a second**.

| Trait | Effect | Starting weight | Experience gained via | XP required |
|---|---|---|---|---|
| Commando | Targeted Sabotage effectiveness +25%; Capture Cipher effectiveness +25%; Capture Cipher risk −25%; Sabotage risk −25%; own operative detection chance factor −10% | 2.0 with Commando training upgrade, 0.2 without | With Commando training: any operation, plus Counter Intelligence (hostile agents present), Build Network, Boost Ideology, Propaganda, Root Out Resistance, Control Trade, Diplomatic Pressure | 600 |
| Demolition Expert | Targeted Sabotage effectiveness +25%; Targeted Sabotage cost −25%; Strengthen Resistance effectiveness +25% | 1.0 | Sabotage Industry / Infrastructure / Resources operations | 400 |
| Escape Artist | Rescue Captured Operative cost −10%; risk −10% | 1.0 | Rescue Captured Operative operation | 15% chance on completion (chance-based, not XP) |
| Infiltrator | Infiltration effectiveness +25%; Infiltration risk −25% | 0.5 | Infiltrate Air Force / Army / Civilian Administration / Navy, Make Resistance Contacts, Rescue Operative | 400 |
| Linguist | Chance to acquire target nationality on completing an operation +20% | 1.0 | Any operation in a country whose nationality the operative lacks | 400 |
| Master Interrogator | Counter intelligence +0.20 | 1.0 | Counter Intelligence (hostile agents present), Root Out Resistance | 400 |
| Natural Orator | Boost Ideology mission effect +20%; Orchestrate Coup cost −25%; risk −25% | 1.0 | Boost Ideology, Propaganda | 400 |
| Well Groomed | Control Trade mission effect +20%; Diplomatic Pressure mission effect +20% | 1.0 | Control Trade, Diplomatic Pressure | 400 |

### Nationality

By default a randomly generated operative only has the recruiting country's nationality. Other nationalities come from the **Localized Training Centers** upgrade and its decisions, from historical operatives, and from **Double Agent** operatives keeping their original nationalities. New nationalities can otherwise only be gained by first earning **Linguist** and then running operations in a country whose nationality the operative lacks.

| Acting in a country whose nationality the operative has | Bonus |
|---|---|
| On a mission | Build Network intel network strength gain factor +30%; own operative detection chance factor −10% |
| On an operation | Operation effectiveness +10%; operation cost −10% |

### Operative experience gain

Daily experience from missions:

| Mission | Daily XP |
|---|---|
| Build Network | 1 |
| Propaganda | 0.35 |
| Boost Ideology | 0.274 |
| Control Trade | 0.137 |
| Diplomatic Pressure | 0.137 |
| Counter Intelligence | 0.112 (only while hostile agents are present; **+100 XP to a random operative on this mission when a hostile operative is caught**) |
| Root Out Resistance | 0.068 |
| Quiet Network | 0 |

Experience on successful operations (to **all** operatives involved):

| Operation | XP |
|---|---|
| Plant False Intelligence | 9 |
| Infiltrate Civilian Administration / Army / Navy / Airforce | 18 |
| Capture Cipher | 18 |
| Make Resistance Contacts | 18 |
| Instigate Workers Revolution | 18 |
| Prepare Coup | 18 |
| Strengthen Resistance | 27 |
| Prepare Collaboration Government | 27 |
| The Warsaw Uprising | 27 |
| Rescue Captured Operative | 36 (plus 15% chance of Escape Artist) |
| Coordinated Strike | 36 |
| Steal Industrial / Military / Naval / Aviation Industry Blueprints | 36 |
| Sabotage Industry / Infrastructure / Resources | 36 |
| Orchestrate Coup | 45 |
| Operation Gunnerside, Operation Biting, Unternehmen Rösselsprung, Rescue Benito Mussolini, Raid Trotsky's Villa, Subtle Assassination, Infiltrate Atomic Program | 90 |

## Missions

Missions are continuous map assignments. Unless noted, **each extra operative on the same mission in the same country multiplies efficiency by 0.5× per operative already there**.

| Mission | Effect | Key numbers |
|---|---|---|
| **Counter Intelligence** | Default mission of an idle operative. Raises counter intelligence in the country the agent is in — catching enemy spies, blunting enemy spy activity and lengthening enemy operation times | Boosted by **Master Interrogator** operatives and the **Interrogation techniques** upgrade |
| **Build Network** | Builds an intel network of contacts across an area | **+0.4 network strength per operative per day**. A network needs **strength ≥ 10 in a state** before its modifiers apply there. Maximum strength rises with more agents and falls with the host's counter intelligence (including Passive defense upgrades) |
| **Quiet Network** | Puts an existing network into quiet mode: most passive effects stop, coverage grows, capture risk becomes tiny; static intel and operation eligibility remain | The **only** task that earns no operative experience |
| **Boost Ideology** | Pushes the target's popular support toward the spying country's ruling ideology; usable on friendly same-ideology countries too | Base **0.1% ideology drift per day**, maximum **0.25% per day** per operative. Boosted by **Natural Orator** and **Psychological Warfare** |
| **Propaganda** | Reduces the target's stability and war support | Base **0.05% per day** to each. Caps at **−20% stability** and **−20% war support**. Uniquely, efficiency is also halved per **additional country** targeted beyond the first. Boosted by **Psychological Warfare** |
| **Root Out Resistance** | Lowers the resistance **target** in the highlighted states | **−10%** resistance target in the targeted state, **0.5×** that in neighbouring states. Does **not** change resistance decay speed. Boosted by **Anti-partisan** upgrades |
| **Control Trade** | Raises trade influence in the target country, moving you up its export priority list | Maximum **+50 trade influence**; decays **−0.1 per day** with no operative maintaining it. Boosted by **Well Groomed** and **Diplomatic Training** |
| **Diplomatic Pressure** | Increases AI willingness to accept your diplomatic offers and lowers world-tension requirements for requests such as joining your faction | Maximum **+20 AI willingness**; world-tension requirement reduced by up to **−20%**. Boosted by **Well Groomed** and **Diplomatic Training** |

Network passive effects: reduced naval invasion penalty; countering enemy dig-in and planning bonus; faster division planning when entering the network (based on the first enemy state on the path); **+25% local intel advantage in combat**; static intel on the nation (naval intel only if the network covers ports). Networks target victory-point cities and can merge into larger networks. **All operations require a network of some strength in the target country**, and mission efficiency depends on network coverage of the *whole* country — large countries need several agents.

## Operations

Every operation needs at least one operative (many need two or three) and a minimum network strength. Operations run **three phases** — infiltration, execution, exfiltration — each randomly rolled with its own cost; the sum sets the total operation cost, which can scale up on repeat runs. Infiltration and exfiltration draw from shared pools; execution phases are operation-specific.

Exceptions: **Plant False Intelligence** has no infiltration/exfiltration — instead three distinct execution phases. **Orchestrate Coup** and **Coordinated Strike** have no exfiltration — instead an extra execution phase.

Base risk tiers:

| Risk | Operations |
|---|---|
| 0% | Plant False Intelligence |
| 10% (low) | Infiltration operations, Make Resistance Contacts, Prepare Collaboration Government, Rescue operations |
| 20% (medium) | Capture Cipher, Steal Blueprints, Strengthen Resistance, Sabotage operations |
| 30% (high) | Orchestrate Coup, Coordinated Strike |

### Generic operations

| Operation | Operatives | Network | Risk | Days | Additional cost | Requirements | Effect | Bonus (extra-good) effect |
|---|---|---|---|---|---|---|---|---|
| Rescue Captured Operative | 1 | 30 | 10% | 35 | None | Has a captured operative in the target country | Rescues all captured operatives in the target country | None |
| Infiltrate Civilian Administration | 2 | 35 | 10% | 90 | None | — | Gain "Civilian Infiltration" asset | Civilian Infiltration + 25 political power + 10% civilian intel |
| Plant False Intelligence | 2 | 40 | 0% | 60 | None | At war; more than 60 divisions deployed; enemy has <80% intel on you | Creates fake intel units to deceive enemies | None |
| Capture Cipher | 2 | 40 | 20% | 75 | None | Has formed the Cryptology Department; target not fully decrypted; Mechanical Computing researched | +30% decryption against the target | 33%: +50% decryption and +10% intel in a random department; 67%: +50% decryption |
| Infiltrate Army | 2 | 50 | 10% | 75 | None | — | Gain "Army Infiltration" | Army Infiltration + 10 army experience + 10% army intel |
| Infiltrate Navy | 2 | 50 | 10% | 75 | None | Target has an owned coastal state | Gain "Navy Infiltration" | Navy Infiltration + 10 navy experience + 10% navy intel |
| Infiltrate Airforce | 2 | 50 | 10% | 75 | None | — | Gain "Airforce Infiltration" | Airforce Infiltration + 10 air experience + 10% air intel |
| Orchestrate Coup | 2 | 70 | 30% | 180 | 12,000 Infantry Equipment | Your ideology >20% in the target; target minor stability <70% at peace, major <50% at peace, any target <35% at war | Your ideology's supporters start a civil war in the target | None |
| Strengthen Resistance | 2 | 35 | 20% | 50 | None | Has "Resistance Contacts"; target state has resistance | Resistance target +10.0% | 33%: resistance target +20.0% and compliance −10%; 67%: resistance target +20.0% |
| Make Resistance Contacts | 2 | 40 | 10% | 60 | None | Any controlled state of the target has resistance | Gain "Resistance Contacts" | 33%: contacts + resistance target +10.0% for 180 days; 67%: contacts + resistance target +10.0% for 60 days |
| Prepare Collaboration Government | 2 | 50 (visible at 25) | 10% | 90 | 200 Support Equipment, 1000 Infantry Equipment, 10 civilian factories for 60 days | Collaboration on target <100%; allowed to create collaboration governments | **Collaboration +30%** | **Collaboration +45%** |
| Coordinated Strike | 2 | 70 | 30% | 3 | 15 civilian factories for 5 days | Has a war goal on the target; allowed to declare war; not already at war | Declares war via surprise attack; all prepared Port Strike and Strategic Bombing missions in the target region execute multiple times with no air interception | None |
| Steal Industrial Blueprints | 3 | 35 | 20% | 120 | None | "Civilian Infiltration" | 1× 300% research bonus for a random Electronics or Industry technology | 33%: +300%, 2.0 years ahead of time; 67%: +300%, 1.0 year ahead of time |
| Steal Military Blueprints | 3 | 50 | 20% | 120 | None | "Army Infiltration" | 1× 300% research bonus for a random Infantry, Support Equipment, Artillery or Armor technology | 33%: 2.0 years ahead; 67%: 1.0 year ahead |
| Steal Naval Blueprints | 3 | 50 | 20% | 120 | None | "Navy Infiltration" | 1× 300% research bonus for a random Naval technology | 33%: 2.0 years ahead; 67%: 1.0 year ahead |
| Steal Aviation Industry Blueprints | 3 | 50 | 20% | 120 | None | "Airforce Infiltration" | 1× 300% research bonus for a random Air technology | 33%: 2.0 years ahead; 67%: 1.0 year ahead |
| Sabotage Industry | 3 | 35 | 20% | 90 | None | Target has a controlled state with resistance; "Resistance Contacts" | Focuses local resistance on industry and raises attack success chance | Same |
| Sabotage Infrastructure | 3 | 35 | 20% | 90 | None | As above | Focuses local resistance on infrastructure | Same |
| Sabotage Resources | 3 | 35 | 20% | 90 | None | As above | Focuses local resistance on resource extraction | Same |

### Infiltration phases (shared pool)

| Phase | Requirements | Cost |
|---|---|---|
| Infiltration via Parachute | >0 transport planes | 1 transport plane (returned on completion) |
| Deployment via Submarine | Target country has a coastal state | None |
| Infiltration across a neutral border | A neutral country between you and the target (not at war with either) | None |
| Diplomatic Passports | None | 1 civilian factory for 15 days |

### Exfiltration phases (shared pool)

| Phase | Requirements | Cost |
|---|---|---|
| Pickup by Airplane | >0 transport planes | 1 transport plane (returned on completion) |
| Pickup by Submarine | Target has a coastal state; you have ≥1 submarine and ≥1 owned coastal state | None |
| Hiking across the Border | A neutral country between you and the target (not at war with you) | None |
| Going to ground | None | None |

### Execution phases

| Operation | Phase | Additional requirements | Cost | Roll chance |
|---|---|---|---|---|
| Rescue Captured Operative | Free In Transit | — | 200 Infantry Equipment | 33% |
| Rescue Captured Operative | Liberate Camp | — | 200 Infantry Equipment | 33% |
| Rescue Captured Operative | Smuggle in escape gear | — | 50 Support Equipment | 33% |
| Infiltrate Civilian Administration | Offer Bribe | — | 3 civilian factories for 30 days | 25% |
| Infiltrate Civilian Administration | Apply Charms | — | None | 25% |
| Infiltrate Civilian Administration | Contact Ideological Supporter | Target has a different ideology | None | 25% |
| Plant False Intelligence | Decoy Tanks | — | 500 Support Equipment | 33% (Phase I) |
| Plant False Intelligence | Radio Deception | — | 500 Support Equipment | 33% (Phase I) |
| Plant False Intelligence | Deliberate Leaks | — | None | 33% (Phase I) |
| Plant False Intelligence | Press Releases | — | 3 civilian factories for 30 days | 50% (Phase II) |
| Plant False Intelligence | Utilize Double Agents | — | 3 civilian factories for 30 days | 50% (Phase II) |
| Plant False Intelligence | Plant Evidence | — | 250 Support Equipment | 50% (Phase III) |
| Plant False Intelligence | Release POW | — | None | 50% (Phase III) |
| Capture Cipher | Bribe Soldier | Holds Army, Navy or Airforce Infiltration on the target | 3 civilian factories for 30 days | 20% |
| Capture Cipher | Commando Raid | At war with the target | 500 Infantry Equipment, 100 Support Equipment | 20% |
| Capture Cipher | Use Seduction | — | None | 20% |
| Capture Cipher | Smuggle Ciphers | — | 3 civilian factories for 30 days | 20% |
| Capture Cipher | Reverse Engineer | Not at war with the target | 3 civilian factories for 30 days | 20% |
| Infiltrate Army/Navy/Airforce | Offer Bribe | — | 3 civilian factories for 30 days | 25% |
| Infiltrate Army/Navy/Airforce | Apply Charm | — | None | 25% |
| Infiltrate Army/Navy/Airforce | Turn Prisoner of War | At war with the target | None | 25% |
| Infiltrate Army/Navy/Airforce | Contact Ideological Supporter | Target has a different ideology | None | 25% |
| Orchestrate Coup | Pre-Position Units | — | None | 100% (Phase II) |
| Orchestrate Coup | Launch Coup | — | None | 100% (Phase III) |
| Strengthen Resistance | Create Supply Caches | — | 300 Support Equipment, 2000 Infantry Equipment | 25% |
| Strengthen Resistance | Distribute Weapons | — | 5000 Infantry Equipment | 25% |
| Strengthen Resistance | Organize Training Camps | — | 2 civilian factories for 45 days | 25% |
| Strengthen Resistance | Coordinate Resistance Groups | — | 2 civilian factories for 45 days | 25% |
| Make Resistance Contacts | Create Radio Circuits | Radio technology | 150 Support Equipment | 33% |
| Make Resistance Contacts | Distribute Pigeons | — | 50 Support Equipment | 33% |
| Make Resistance Contacts | Strategy Briefings | — | None | 33% |
| Prepare Collaboration Government | Set Up Planning Committees | — | 3 civilian factories for 90 days | 33% |
| Prepare Collaboration Government | Train Paramilitary Forces | — | 1000 Support Equipment | 33% |
| Prepare Collaboration Government | Contact Military Officers | — | 3 civilian factories for 30 days | 33% |
| Coordinated Strike | Scout Targets | — | 100 Support Equipment | 50% (Phase II) |
| Coordinated Strike | Mark Targets | — | 100 Support Equipment | 50% (Phase II) |
| Coordinated Strike | Sabotage Communications | — | 100 Support Equipment | 34% (Phase III) |
| Coordinated Strike | Direct Units | — | 100 Support Equipment | 34% (Phase III) |
| Coordinated Strike | Occupy Bridges | Land border with the target | 1000 Infantry Equipment | 34% (Phase III) |
| Steal Industrial Blueprints | Offer Bribe | — | 3 civilian factories for 30 days | 40% |
| Steal Industrial Blueprints | Apply Charms | — | None | 40% |
| Steal Industrial Blueprints | Infiltrate Middle Management | — | None | 20% |
| Sabotage Industry | Plant Explosives | — | 500 Support Equipment | 90% |
| Sabotage Industry | Organize More Meetings | — | None | 10% |
| Sabotage Infrastructure | Destroy Bridge | — | 500 Support Equipment | 25% |
| Sabotage Infrastructure | Collapse Tunnel | — | 500 Support Equipment | 25% |
| Sabotage Infrastructure | Remove Roadsigns | — | 50 Support Equipment | 25% |
| Sabotage Infrastructure | Immobilize Rolling Stock | — | 250 Support Equipment | 25% |
| Sabotage Resources | Burn Storage | — | 250 Support Equipment | 50% |
| Sabotage Resources | Destroy Mining Equipment | — | 250 Support Equipment | 50% |
| Steal Military Blueprints | Offer Bribe | — | 3 civilian factories for 30 days | 50% |
| Steal Military Blueprints | Apply Charms | — | None | 50% |
| Steal Naval Blueprints | Offer Bribe | — | 3 civilian factories for 30 days | 40% |
| Steal Naval Blueprints | Apply Charms | — | None | 40% |
| Steal Naval Blueprints | Infiltrate Naval Design Office | — | None | 20% |
| Steal Aviation Industry Blueprints | Offer Bribe | — | 3 civilian factories for 30 days | 40% |
| Steal Aviation Industry Blueprints | Apply Charms | — | None | 40% |
| Steal Aviation Industry Blueprints | Steal Prototype | — | 10 Small Airframes | 20% |

### Unique / historical operations

Hand-scripted, gated behind a national focus or decision, usually one-off and single-country. They override the standard risk tiers and use fixed phase sequences (a few still draw generic infiltration/exfiltration steps).

| DLC | Operation | Performed by | Target | Operatives | Network | Risk | Days | Cost | Effect |
|---|---|---|---|---|---|---|---|---|---|
| La Résistance | Operation Gunnerside (Heavy Water Raid) | Any country except Germany | Germany (or Norway if a German subject) | 1 | 50 | 50% | 202 (listed as 90 in the operations table) | 500 Infantry Equipment + 50 Support Equipment | Event "Operation Gunnerside succeeds"; Germany gets "Telemark Heavy Water Plant destroyed", sabotaging German nuclear progress. Requires German heavy-water production, war with Germany, Telemark resistance >50 and network >50 |
| La Résistance | Operation Biting (Bruneval Raid) | Any country except Germany | Germany | 1 | 50 | 20% | 180 | 500 Infantry Equipment + 50 Support Equipment | Captures German radar research. Requires war with Germany, German Radio Detection tech, France capitulated |
| La Résistance | Unternehmen Rösselsprung (Capture Tito) | Germany | Yugoslavia | 1 | 50 | 40% | 90 | 2000 Infantry Equipment | **25% success / 75% failure**; success removes Tito and weakens Yugoslav resistance. Needs a German-controlled Yugoslav core state with resistance >50 (visible at >10) |
| La Résistance | Rescue Benito Mussolini | Germany | Italy | 1 | 35 | 30% | 90 | 2000 Infantry Equipment | **75% success / 25% failure**; success restores Mussolini and enables the Italian Social Republic chain. Germany must be fascist, at war with a no-longer-fascist Italy |
| La Résistance | The Warsaw Uprising | Poland | Occupier of Polish cores | 2 | 50 | 25% (50% in the Operations page's unique table) | 75 | "Resistance Contacts"; base cost multiplier 0.25 (phase costs quartered) | Flips Warsaw and adjacent Polish cores back to Poland, spawns resistance divisions scaled to local industry, teleports allied units to Polish territory, declares war on the occupier if not already at war. **+25% extra-good outcome chance** |
| La Résistance | Instigate Workers Revolution in Britain | France (communist) | United Kingdom | 1 | 25 | 20% | 180 | 5000 Infantry Equipment + 500 Support Equipment | Starts resistance in Scotland, Wales and Northern Ireland (raises each core's resistance target by 50). Requires focus Carry the Revolution North |
| La Résistance | Instigate Workers Revolution in Italy | France (communist) | Italy | 1 | 25 | 20% | 180 | 5000 Infantry Equipment + 500 Support Equipment | Italy +25% communism support. 33%: communist civil war and Italian Union joins your faction; 67%: +25% communism, −10 stability, −10 war support. Requires Carry the Revolution South |
| La Résistance | Instigate Workers Revolution in Spain | France (communist) | Republican Spain | 1 | 25 | 35% | 180 | 5000 Infantry Equipment + 500 Support Equipment | Spain +25% communism support; 33%: civil war and People's Republic of Spain joins your faction. Requires Carry the Revolution West |
| La Résistance | Instigate Workers Revolution in Germany | France (communist) | German Reich | 1 | 25 | 35% | 180 | 5000 Infantry Equipment + 500 Support Equipment | Germany +25% communism support; 33%: civil war and Socialist Republic of Germany joins your faction. Requires Carry the Revolution East |
| La Résistance | Prepare Coup in North Africa | France | Casablanca, Marrakech, Algiers, Tlemcen, Constantine, Tunisia, Gabès (states 458–462, 513, 665) | 1 | 50 | 25% | 90 | 5000 Infantry Equipment + 500 Support Equipment | Become owner and controller of those states; Vichy France gets a notification event |
| La Résistance | Prepare Coup in Syria | France | Aleppo, Deir-az-Zur, Damascus, Lebanon | 1 | 50 | 25% | 90 | 5000 Infantry Equipment + 500 Support Equipment | Become owner and controller of those states |
| La Résistance | Prepare Coup in Indochina | France | Tonkin, Laos, Southern Indochina, Cambodia | 1 | 50 | 35% | 90 | 5000 Infantry Equipment + 500 Support Equipment | Become owner and controller of those states |
| La Résistance | Prepare Coup in Central Africa | France | Middle Congo, Gabon, Cameroon, Equatorial Africa, Chad | 1 | 50 | 35% | 90 | 5000 Infantry Equipment + 500 Support Equipment | Become owner and controller of those states |
| La Résistance | Prepare Coup in West Africa | France | Mauritania, Senegal, Mali, Guinea, Ivory Coast, Upper Volta, Niger, Dahomey | 1 | 50 | 35% | 90 | 5000 Infantry Equipment + 500 Support Equipment | Become owner and controller of those states |
| La Résistance | Prepare Coup in Madagascar | France | Madagascar | 1 | 50 | 25% | 90 | 5000 Infantry Equipment + 500 Support Equipment | Become owner and controller of Madagascar |
| No Step Back | Raid Trotsky's Villa | Soviet Union | Country hosting Trotsky (usually Mexico, Mexico City) | 1 | 50 | 35% | 60 | 50 Infantry Equipment + 50 Support Equipment | Kills Trotsky and swaps out the Trotskyite Plot spirit; on failure Trotsky survives. **+50% extra-good outcome chance.** Requires focus Behead the Snake and network >50 in Mexico City |
| No Step Back | Subtle Assassination (Murder Trotsky) | Soviet Union | Country hosting Trotsky | 1 | 25 | 25% | 270 | None | Kills Trotsky and swaps out the Trotskyite Plot spirit. One-shot; requires Behead the Snake |
| No Step Back | Infiltrate Atomic Program (Nuclear Espionage) | Soviet Union | Any major with Atomic Research not at war with the USSR | 1 | 75 | 25% | 3 | None | Event "Agent returns with nuclear secrets" — accelerates the Soviet atomic bomb project. One-shot per target country; requires focus Soviet Atomic Bomb Project |

> ⚠️ The wiki's Operations and List of operations pages disagree on some values (Warsaw Uprising risk 25% vs 50%; Heavy Water Raid duration 90 vs 202 days). Both are shown above.

## Predefined intelligence agencies

Predefined agencies take precedence over the generic ones. If a country qualifies for more than one, the default is picked randomly.

Generic logos and default names available to everyone: **Rooke** (default), **Tower**, **Snake**, **Stag**, **Golden Lion**, **Arrow**, **Lion Head**, **Golden Eagle**, and **Hammer and Sickle** (communist only). A custom name may be set.

| Country | Agency name | Prerequisites |
|---|---|---|
| Afghanistan | ESS | Created with Shadows of the King |
| Afghanistan | Istikhbarat | Non-aligned or Fascist |
| Afghanistan | KHAD | Communist |
| Afghanistan | National Directorate of Security | Democratic |
| Argentina | S.I. | — |
| Austria | Evidenzbureau | — |
| Austria | Evidenzbureau (democratic variant) | Created with Reform the Evidenzbureau |
| Bangladesh | National Security Intelligence | — |
| Belgium | ADIV / SGRS | Without Götterdämmerung |
| Belgium | Veiligheid van de Staat / GISS | With Götterdämmerung |
| Belgian Congo | Service National d'Identification et de Protection | Not independent |
| Belgian Congo | Service National d'Intelligence et de Protection | Independent |
| Brazil | Departamento de Ordem | Created with Departamento de Ordem Política e Social |
| Brazil | EICI | Created with Form the EICI |
| British Raj | Research and Analysis Wing | — |
| Bulgaria | Natsionalnata Razuznavatelna Sluzhba | — |
| Chile | Policía de Investigaciones de Chile | — |
| China | NBIS | — |
| Communist China | Intelligence Department Central Military Commission | — |
| Dominion of Canada | Royal Canadian Mounted Police | — |
| Denmark | Sikkerhedspolitiet | — |
| Ethiopia | Arbegnoch / Fetno-Derash | Not an Italian subject, not communist |
| Ethiopia | Black Lions / Central Revolutionary Investigation Department | Communist |
| Ethiopia | Servizio Informazioni Militare Etiope | Subject of Italy |
| Finland | PE TIEDOS | — |
| France | Deuxième Bureau | — |
| German Reich | Abwehr | Not communist |
| German Reich | Stasi | Communist, or created with Form the Stasi |
| Greece | Diéfthynsi Eidikís Asfaleías tou Krátous / I Eidikí | — |
| Hungary | VKF 2 | Not communist |
| Hungary | Államvédelmi Hatóság | Communist |
| Hungary | Evidenzbureau | Completed The Lands of the Crown of Saint Stephen |
| Iceland | Lögreglan | — |
| Iraq | Mudiria al-Amn al-'Amm | At peace |
| Iraq | Mudiriyyat al-Istikhabarat al-'Askariyya al-'Amma | At war |
| Italy | Servizio Informazioni Militare | — |
| Japan | G-2 Department / Section 3 | — |
| Manchukuo | Hoankyoku | — |
| Netherlands | Bureau Inlichtingen | — |
| Norway | E-tjenesten | — |
| Norway | Forsvarets Etterretningstjeneste | Created with Forsvarets Intelligence Service |
| Norway | Nasjonal Samlings Overholdelsesbyrå | Created with Secret Police |
| Pakistan | Inter-Services Intelligence | — |
| Persia | SAVAK | Not communist |
| Poland | Dwójka | — |
| Portugal | PIDE | — |
| Romania | Serviciul Special de Informatii | — |
| Soviet Union | NKVD | — |
| Nationalist Spain | SIPM | — |
| Republican Spain | SIM | — |
| Sweden | C-byrån | — |
| Switzerland | Buero Ha | Completed Buero Ha, not fascist |
| Switzerland | Federal Police | Created with Federal Police Intelligence Department |
| Turkey | Millî Emniyet Hizmeti | — |
| United Kingdom | MI6 / SIS | — |
| United States | Office of Strategic Services | — |
| Yugoslavia | OZNA | — |

## Predefined operatives

Historical operatives with fixed traits and nationalities, usually unlocked by a focus or DLC.

| Country | Operative | Traits | Nationalities | Unlock |
|---|---|---|---|---|
| Argentina | Osmar Hellmuth | Infiltrator, Natural Orator, Well Groomed | Argentina, Germany | Trial of Allegiance |
| Austria | Erwin von Lahousen | Double Agent, Commando | Austria, Germany | Götterdämmerung |
| Austria | Heinrich Maier | Infiltrator, Master Interrogator | Austria | Focus Repeal the May Constitution |
| Austria | Wilhelm Ergert | Double Agent, Linguist, Safe Cracker | Austria, Germany, Yugoslavia | Götterdämmerung |
| Belgium | Jozef Raskin | Well Groomed, Commando | Belgium, Mengkukuo | — |
| Brazil | Maximilian Vogel | Double Agent, Infiltrator | Brazil, Argentina, Chile | Focus Expand Operation Bolívar |
| Brazil | Nadiya Morozova | Escape Artist | Soviet Union | Focus Form the EICI |
| Brazil | Robert Ivanov | Tough | Soviet Union | Focus Form the EICI |
| British Raj | Noor Inayat Khan | — | British Raj | — |
| Bulgaria | Vladimir Zaimov | Infiltrator, Commando | Bulgaria | — |
| Chile | Rosita Serrano | Linguist, Seducer, Well Groomed | Chile, Spain, Germany | Trial of Allegiance |
| Czechoslovakia | Paul Thummel | Double Agent, Well Groomed | Czechoslovakia, Germany, Austria | — |
| Denmark (or its supporter) | Flemming Muus | Commando | Denmark | Denmark completes Align with Foreign Powers and Intel Sharing |
| Denmark | Hans Lunding | Safe Cracker | Denmark | Focus Sikkerhedspolitiet |
| Denmark | Monica Wichfeld | Infiltrator | Denmark, United Kingdom | Focus Intel Sharing |
| Denmark | Varinka Wichfeld | Escape Artist | Denmark, United Kingdom | Focus Intel Sharing |
| Finland | Hella Wuolijok | Well Groomed, Escape Artist | Finland, Estonia | Focus The Red Watch or Trade Agreements |
| Finland | Vilho Pentikäinen | Safe Cracker, Master Interrogator | Finland, Soviet Union | Focus The Red Watch |
| France | Gilbert Renault | — | France | — |
| France | Jacques Duclos | Infiltrator, Natural Orator | France | Focus Loyalty To the Cause |
| France | Jeannie Rousseau | Linguist | France | — |
| France | Odette Samson | Tough | France | — |
| France | René Joyeuse | Infiltrator | France, Quebec | Not available to a Spy Master |
| Germany | Achim Hund | Natural Orator | Germany | ~0.16% chance in a fascist civil war with Berlin occupied |
| Germany | Andrea Hund | Seducer, Natural Orator | Germany | ~0.16% chance in a fascist civil war with Berlin occupied |
| Germany | Coco Chanel | Infiltrator, Seducer | France | Focus Subversive Infiltrators + controls Ile de France; not available to a Spy Master |
| Germany | Eleysa Bazna | Infiltrator | Germany, Turkey, Kosovo, Albania | Focus Absorb the Abwehr or Expand SS Security Duties |
| Germany | Erich Gimpel | Infiltrator | Germany | — |
| Germany | Erich Mielke | Commando, Escape Artist, Master Interrogator | Germany | Focus Assemble the Red Orchestra |
| Germany | Ernst Wollweber | Tough | Germany, Soviet Union | Focus Assemble the Red Orchestra |
| Germany | Fritz Duquesne | Commando, Tough, Escape Artist | Germany, Netherlands, South Africa, United States | — |
| Germany | Herbert Hans Haupt | Demolition Expert | Germany, United States | Focus Reorganize Secret Services |
| Germany | Johannes Becker | Natural Orator, Linguist | Germany, Austria, Argentina, Brazil | Focus Challenge the Monroe Doctrine |
| Germany | Marie Luise Hammerstein | Natural Orator | Germany, Soviet Union | Focus Assemble the Red Orchestra |
| Germany | Nikolaus Ritter | Safe Cracker | Germany | — |
| Germany | Norman Stewart | Natural Orator, Tough | United Kingdom, Scotland | Focus Operation Sea Lion |
| Germany | Otto Skorzeny | Commando | Germany, Austria | Focus Anschluss |
| Germany | Rudolf Herrnstadt | Linguist | Germany, Soviet Union | Focus Assemble the Red Orchestra |
| Germany | Otto von Bolschwing | Natural Orator, Well Groomed | Germany, Palestine, Romania | Focus Subversive Infiltrators |
| Germany | Savitri Devi | Natural Orator, Linguist, Well Groomed | Greece, France, British Raj | Focus Propaganda Master |
| Greece | Patrick Leigh Fermor | Tough, Commando | Greece, United Kingdom | Battle for the Bosporus |
| Iran | Hassan Pakravan | Tough, Demolition Expert | Iran | Focus Form SAVAK |
| Iran | Nasser Moghaddam | Tough, Demolition Expert | Iran, France, United Kingdom | Focus Transfer Officers Into Intelligence |
| Iran | Nematollah Nassiri | Infiltrator, Master Interrogator | Iran | Focus Transfer Officers Into Intelligence |
| Iran | Teymur Bakhtiar | Infiltrator, Natural Orator, Well Groomed | Iran, France | Focus Form SAVAK |
| Italy | Carmelo Borg Pisani | Natural Orator, Well Groomed | Italy, United Kingdom | Focus Utilize the Blackshirts or Italian Irredentism |
| Italy | Edgardo Sogno | Linguist, Natural Orator | Italy | Focus Meritocracy or Expand Intelligence Services |
| Italy | Emilio Faldella | Well Groomed, Commando, Double Agent | Italy, Spain | Focus Appease the Military |
| Italy | Francesco de Martini | Commando, Demolition Expert, Linguist | Italy, Syria, Ethiopia | — |
| Italy | Hugh O'Flaherty | Escape Artist, Natural Orator, Linguist | Italy, Ireland | Focus Agents of the Church |
| Italy | Laura Garroni | Demolition Expert, Commando | Italy | Focus Union in the Party or Gappisti |
| Italy | Maurizio Giglio | Infiltrator, Tough, Double Agent | Italy | Focus Common Ground |
| Italy | Padre Ildefonso | Master Interrogator, Natural Orator | Italy | Focus Banda Carità |
| Italy | Paolo Caccia Dominioni | Safe Cracker, Tough, Escape Artist | Italy, Egypt | — |
| Italy | Pietro Koch | Master Interrogator, Tough, Well Groomed | Italy, Germany | Focus Banda Koch |
| Italy | Rosa Dainelli | Commando, Demolition Expert | Italy, Ethiopia | Focus Servizio Informazioni Militare |
| Italy | Stefanina Moro | Infiltrator, Tough | Italy | Focus Gruppi di Difesa della donna |
| Japan | Ignatius Timothy Trebitsch Lincoln | Seducer, Well Groomed, Natural Orator | Hungary, Austria, Tibet, China, Israel | Focus Greater East Asian Co-Prosperity Sphere |
| Japan | John Semer Farnsworth | — | United States | — |
| Japan | Patrick Vaughan Heenan | Tough | United Kingdom, New Zealand, British Malaya, British Raj | Focus Strike South Doctrine |
| Japan | Takeo Yoshikawa | — | Japan | — |
| Japan | Yoshiko Kawashima | — | Japan, Manchukuo, China | — |
| Norway | Astrid Løken | Infiltrator | Norway | Focus Use XU |
| Norway | Kasper Skjeggenes | Escape Artist, Commando | Norway | Focus Use XU |
| Poland | Krystyna Skarbek | Commando, Seducer | Poland | — |
| Poland | Roman Czerniawski | — | Poland | — |
| Poland | Witold Pilecki | Escape Artist, Infiltrator, Commando | Poland, Germany | Focus Expand Polish Intelligence |
| Soviet Union | Alexander Radó | Natural Orator | Soviet Union, Hungary | — |
| Soviet Union | Dmitry Medvedev | Demolition Expert, Commando | Soviet Union | Focus Organization of the Partisans |
| Soviet Union | Kim Philby | Double Agent, Infiltrator | Soviet Union, United Kingdom | — |
| Soviet Union | Nikolay Ivanovich Kuznetsov | Commando, Infiltrator | Soviet Union, Germany, Ukraine | No Step Back; communist; a Ukrainian core state occupied while at war |
| Soviet Union | Ramón Mercader | Tough, Infiltrator | Soviet Union, Spain, Mexico | Focus Behead the Snake |
| Soviet Union | Richard Sorge | Well Groomed | Soviet Union, Germany | — |
| Soviet Union | Ursula Kuczynski | Safe Cracker, Infiltrator | Soviet Union, Germany | Focus Soviet Atomic Bomb Project |
| Soviet Union | Yan Chernyak | Linguist, Infiltrator | Soviet Union, Germany, Hungary, Romania, Czechoslovakia, Slovakia | — |
| Sweden | Jean Blæksprutten | Well Groomed, Natural Orator | Sweden, Denmark | Focus Support Danish Communists |
| Sweden | Jimmy Muldvarp | Well Groomed, Natural Orator | Sweden, Norway | Focus Support Norwegian Communists |
| Sweden | Raoul Wallenberg | Seducer, Infiltrator, Tough | Sweden, Hungary | Arms Against Tyranny |
| Switzerland | Clara Thalmann | Commando | Switzerland | Appointed Clara Thalmann as a political advisor at least once |
| Switzerland | David Frankfurter | Infiltrator | Croatia, Yugoslavia, Germany, Israel | By Blood Alone; has an agency at the March 1936 Frankfurter event and picks a recruiting option |
| Switzerland | Franz Riedweg | Infiltrator | United Kingdom | Focus Infiltrate Federal Police |
| Switzerland | Hans Hausamann | Well Groomed | Switzerland | Focus Buero Ha |
| Switzerland | Rudolf Roessler | Infiltrator | Switzerland, Germany | Focus Buero Ha |
| Turkey | Ruzi Nazar | Tough, Commando | Turkey, Soviet Union, Kazakhstan | Battle for the Bosporus |
| United Kingdom | Diana Rowden | — | United Kingdom | — |
| United Kingdom | Dusko Popov | Double Agent | United Kingdom, Germany, Yugoslavia | — |
| United Kingdom | Juan Pujol | Double Agent | United Kingdom, Germany | — |
| United Kingdom | Nancy Wake | Escape Artist | United Kingdom | — |
| United States | George Musulin | Tough, Infiltrator, Commando | United States, Yugoslavia, Serbia, Croatia | Focus Intervention in Europe |
| United States | Joe Savoldi | Linguist, Infiltrator, Tough, Well Groomed | United States, Italy | Focus War Plan Silver |
| United States | Josephine Baker | Well Groomed | United States | — |
| United States | René Joyeuse | Infiltrator, Commando | United States, France, Switzerland, Quebec | Focus War Plan Gold |
| United States | Serge Obolensky | Tough, Natural Orator | United States, Soviet Union | Focus War Plan White |
| United States | Virginia Hall | Demolition Expert | United States | — |
| United States | William G Sebold | Double Agent, Infiltrator | United States, Germany | Focus War Plan Black |

## Counter-intelligence checklist

To defend against enemy espionage:
- Keep operatives on **Counter Intelligence** (raises enemy operation time and capture chance; each extra agent in the same country counts at 0.5×).
- Take **Passive defense** upgrades (+1.5 / +1.25 / +1 / +1 counter intelligence).
- Take **Interrogation techniques** (+100% enemy operative capture chance, +25% intel extraction).
- Take **Anti-partisan** upgrades and run **Root Out Resistance** against enemy-boosted resistance.
- Raise **Cryptology level** (Government Cypher School +1 each, Machine-Assisted Encryption +2 each) to make your ciphers costlier to break.
- Reduce intel given away with **MEFO Bills** (Germany), the Soviet **Do Not Blab** decision, and the **Best of the Best** / **Branch Independence Spirit** officer-corps spirits.
- Reaching **80% army intel** on an enemy makes you immune to their **Plant False Intelligence**; **90%** reveals their existing Fake Intel divisions.

## Cross-references

- [Officer corps and commanders](officer-corps-and-commanders.md) — naval intel efficiency and naval supremacy for invasions; officer-corps spirits that affect intel.
- [Manpower and experience](manpower-and-experience.md) — resistance-driven attrition and how to suppress it.
