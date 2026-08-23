---
title: Civil War, Occupation, Puppets and Exile
category: mechanics
tags: [civil war, occupation, resistance, compliance, garrison, occupation laws, puppet, autonomy, collaboration government, government in exile]
game_version: "1.19"
dlc: [La Résistance, Man the Guns, By Blood Alone, Together for Victory]
sources:
  - https://hoi4.paradoxwikis.com/Civil_war
  - https://hoi4.paradoxwikis.com/Occupation
  - https://hoi4.paradoxwikis.com/Puppet
  - https://hoi4.paradoxwikis.com/Governments_in_exile
---

## Summary

Four related systems for controlling land and people you do not fully own. A **civil war** splits a country in two in proportion to the rebel ideology's support, dividing armies, ships, planes and stockpiles by the same percentage. **Occupied states** run on resistance and compliance, shaped by the occupation law you assign and the garrison you pay for. **Puppets** sit on an autonomy ladder measured in autonomy points, with different ladders for democratic, fascist and Japanese overlords. A capitulated country can survive as a **government in exile** whose legitimacy (0–100) feeds resistance in its occupied cores.

## Civil war

### Triggering a civil war

- Support for a non-ruling ideology growing too large produces demands for a change of government; refusing raises the chance of civil war. It begins with an event that lets the player choose a side. The same rising ideology may instead produce a **coup**, which changes government peacefully. Exact popularity thresholds and event timings are in [Politics, ideology and government](politics-ideology-government.md).
- Appointing an ideology-promoting minister triggers the choice between **internal support** (favours a coup) and **popular support** (favours faster ideology growth and makes the civil-war event more likely to fire before a coup).
- Foreign powers can push another country's ideology: with **La Résistance** through the intelligence agency's *Boost party popularity* mission, or without the DLC through a political-power diplomatic action. **Ideology drift defence** from national spirits and ministers reduces the efficiency of these actions.
- A foreign-funded coup requires the relevant intelligence operation (La Résistance) or a diplomatic action costing **200 political power (0.5 PP/day)** without the DLC, plus a shipment of infantry equipment. The equipment required scales with the target's civilian population.

### What each side gets

- The country splits in two according to a **pre-scripted ratio** or, for unscripted wars, according to relative ideological support. Known scripted splits: the **French Civil War 80/20**; the **Soviet Civil War 82/18, 70/30 or 50/50** depending on circumstances.
- **Divisions, ships, aircraft, stockpiled equipment and divisions in training are split by that same percentage.**
- **Both** sides inherit all completed and in-progress focuses and all research.
- One side is the **original** nation and keeps the country tag (even with a new ideology and name); the other is the **splinter** and gets a new tag.
- The **original** keeps all hired political advisors, research and military staff, all accumulated political power, army/navy/air experience, and unspent research bonuses. **Generals and admirals are split in half or along party lines**, depending on the country.
- Both sides immediately go to war for total annexation. The war then behaves like any other, ending in capitulation via victory points — **the only difference is that occupied territory owned by the other side has no occupation laws**.
- Boosting party popularity before staging a coup directly enlarges the breakaway state, since land is allocated by ideological support.

### Intervening in someone else's civil war

- **Lend-lease**: the country that supplied the rebels' initial infantry equipment can keep supporting them with further lend-lease, including tanks and artillery.
- **Volunteers**: the sender must be at peace with the side it supports (not necessarily with the other side) and must not be in a faction with that side.
  - **1 volunteer division per 20 active divisions**, rounded down; a division counts the same whether it has 1 or 25 battalions.
  - **The sender needs at least 30 divisions to send volunteers at all.** 176 active divisions allow 8 volunteer divisions; 181 allow 9.
  - Add **one further division per 20 provinces** in the destination country.
- **Attachés** are a third, tension-free option — see [Politics, ideology and government](politics-ideology-government.md).

**Inferred:** starting a civil war in a country you plan to invade splits the conquest into two wars — the breakaway state keeps its territory and is a separate entity, so a peace conference against the original government cannot take rebel-held land.

### Pre-scripted civil wars

Historical civil wars fire at their historical dates — the **Spanish Civil War** is currently the only fully historical example — and use historically-based territory splits, but can still be swung by foreign support, volunteers and expeditionary forces.

## Occupation

States are **core** (national territory), **occupied** (resistance enabled) or **colony** (no resistance). A core state with resistance force-enabled is listed as occupied but keeps core benefits (no manpower or building-slot penalties).

A state that has no resistance at game start keeps it disabled unless it changes hands or a mechanic enables it. Once resistance exists, the game re-checks daily that:

- the state is not impassable;
- the state is not a core of the controller;
- some country has a core on it, **or** it was Spanish-owned at game start and is occupied by a country originating from Spain after the civil war.

### Resistance strength

Starts at **1%** when the state is captured, then moves toward the resistance target. If the state should no longer have resistance it decays toward 0 at **−0.25%/day**. Strength is clamped to **0.01%–100%**.

| Threshold | Level | Effect |
|---|---|---|
| 25% | Organized Resistance | Garrison penetration chance +50% |
| 50% | Emboldened Resistance | Damage to garrisons +100% |
| 75% | Uprising | Controller only: divisions speed −50%, strategic redeployment disabled, local supplies −50%, division attrition +30% |
| 90% | Rebellion | Local factories −3%; resistance declares independence on occupied core states (rebellion event within 1 hour). Occupied states switch control to the rebelling country (re-established if it does not exist or is at peace with the occupier) and it receives **2–6 divisions per state**, based on factory count |

### Resistance target

| Source | Value |
|---|---|
| Base | +35% |
| Target country has capitulated | +10% |
| Target country has a government in exile | +2%, plus +0.18% per point of legitimacy (up to +20% at 100 legitimacy) |
| Controller has a claim | −5% |
| Controller is at peace | −10% |
| Victory points in state | 0–4 VP: 0%; 5–19 VP: +5%; 20–49 VP: +10%; 50+ VP: +20% |
| Compliance in state | −0.5% per 1% compliance, up to −50% |
| Controller stability | −0.2% per 1% of stability below 100% (so up to +20% at 0% stability) |
| State population under 1000 | −50% |
| State population 1000–10000 | −20% |
| Compassionate Gentleman advisor | −5% |
| Root out resistance intelligence mission | Base −10%, better with agency upgrades and more agents; each extra agent is only 50% as efficient as the previous |
| Occupation laws | −75% to +40% |
| Continuous focus Resistance Suppression | −5% |
| Enemy Strengthen Resistance operation | +10%, or +20% with bonus (+25% if the operator completed *Export Saboteurs* and has no bonus) |
| Enemy Make Resistance Contacts operation | +10% with bonus |
| Spread from a neighbouring state with a higher target | +0.5 × the difference, from the single highest neighbour |

Spread example: a 10% state next to a 70% state ends at 40%; a third 10% state bordering that 40% state ends at 20% (half the difference between its 10% base and the 30% of spread).

**Floor:** all modifiers except compliance can only push the target down to **10%**; only compliance drives it below that to 0. If resistance reaches 0, it re-enables only when the target returns to 10%.

### Resistance growth, decay and activity

- Base growth **+0.2%/day**, base decay **−0.1%/day**; further modifiers are multiplicative.
- Controller has a claim on the state: decay **+25%**.
- Below 10 strength: decay **−50%**. Below 20 strength: decay **−25%**.
- *Weapons for the Resistance* (government-in-exile spirit): resistance growth **+10%** in that country's cores.
- *Guerrilla Warfare* land doctrine (Mass Assault branch): resistance growth **+25%** in that country's cores.
- *Brutal Oppression* occupation law (fascist): resistance decay **+100%** where applied.

**Resistance activity** is rolled daily: chance **+0.312% per 1% of resistance**, up to **31.2% at 100%**. Each event destroys **2% of the state garrison's equipment and 1.6% of its manpower** (equipment losses hit all equipment types in use, scaled by the garrison's fulfilment rate and rounded up). Emboldened Resistance raises both. **Garrison template hardness reduces both by −1% per 1% hardness, capped at −90% at 90%+ hardness**, applied whether or not the country actually has the hard equipment; it stacks additively with other garrison-damage reductions to a **maximum total of −90%**, so extra hardness is wasted once other sources fill the cap. Each activity also has a **2% base chance to penetrate the garrison** and damage local infrastructure, civilian factories or military factories; Organized Resistance raises it, certain spirits and advisors lower it.

### Compliance

Compliance is the share of the local population loyal to the occupier.

- Starts at **0%** in a newly occupied state. Non-core states owned at game start begin at **70%**.
- If a state changes owner, the new owner inherits **0.5×** the old owner's compliance.
- If a collaboration government was prepared before capitulation/annexation, starting compliance in all of that country's states equals the **collaboration percentage**.
- Base gain **+0.075%/day**, modified by occupation laws, spirits and leader traits. The previous controller who has (temporarily) lost the state suffers **−0.05%/day**. Occupation laws give **−0.11% to +0.03% per day**; the **No Garrison** law disables compliance change entirely.
- Compliance **growth modifiers** (applied to gain): controller has a claim **+5%**; controller is at peace **+10%**; Compassionate Gentleman advisor **+2%**.
- Compliance **decay** (applied after growth modifiers): **−0.00083%/day per point of existing compliance** (−0.083%/day at 100%); if the state is a core of a country with a government in exile, a further **−0.00015%/day per legitimacy** (−0.015%/day at 100 legitimacy).

Installing a collaboration government converts the occupied states into a puppet and removes resistance, making compliance moot.

#### What compliance yields

```
Factories available  = 100% − 75% + 65% × compliance
Resources available  = 100% − 65% + 65% × compliance
Manpower available   = 100% − 98% + 18% × compliance
```

Refineries and fuel silos ignore this and always produce their full amount. At **100% compliance** a state provides **100% of its factories, 105% of its resources and 40.5% of its manpower** by default. Fractional factories and resources are rounded down per type (the first days of a save use a different grouping/rounding, corrected once occupation factories are recalculated).

Average compliance across occupied states grants:

| Threshold | Name | Effect |
|---|---|---|
| 15% | Informants | Enemy operative detection chance offset +25% |
| 25% | Local Police Force | Required garrisons −25%; additional recruitable population +0.5% |
| 40% | Reorganized Workforce | Local resources +10%; local factories +10% |
| 60% | Volunteer Program | Recruitable population +20% |
| 80% | A New Regime | Triggers the event to establish a collaboration government |

Other sources: Prince of Terror advisor +2% manpower from non-core states; occupation laws give local factories −35% to +60%, local resources −35% to +60%, local manpower +0% to +8%. Laws such as **Secret Police**, communist **Liberated Workers** and Italian **Colonial Police** combine extra industry with small enough compliance-gain penalties that extra compliance sources can still push compliance upward.

### Garrisons and suppression

- Garrison divisions are assigned in the Occupied Territories tab, are invisible on the map, and draw equipment automatically (allocation set in Recruit & Deploy).
- **Suppression needed: 0.75 suppression per 1 point of resistance in each state.** Resistance below 10% is treated as 10% for this purpose, and above 50% the requirement is capped as if it were 50%.
- If garrison reinforcement is unfulfilled, **all occupation-law effects are scaled** by:

```
Modifier = 100% − max( (manpower requirement)² ; (equipment requirement)³ )
```

Garrison templates trade suppression against hardness and cost — hardness is what cuts resistance damage (see the resistance-activity rules above), while suppression comes from the units' suppression stat (see the Land units mechanic).

### Occupation laws

Assignable country-wide, per occupied country, or per state.

| Law | Resistance target | Compliance gain | Required garrisons | Damage to garrisons | Local resources | Local factories | Additional effects | Availability |
|---|---|---|---|---|---|---|---|---|
| No Garrison | +40% | – | −100% | – | – | – | Compliance change disabled | All |
| Civilian Oversight | – | – | −25% | −25% | – | – | – | All |
| Local Police Force | −15% | −0.025% | −35% | −50% | – | – | – | All |
| Secret Police | −30% | −0.04% | −15% | −15% | +5% | +5% | Enemy intel network strength gain −25%; enemy operative detection chance offset +1% | All |
| Military Governor | −35% | −0.045% | – | – | +10% | – | Local manpower +8% | All |
| Forced Labor | −40% | −0.08% | +15% | +30% | +40% | +5% | Civilian factory repair speed +25%; resource sabotage chance −25%; resource sabotage duration −25% | All |
| Harsh Quotas | −40% | −0.08% | +15% | +50% | +5% | +25% | Military and civilian factory repair speed +25%; military and civilian factory sabotage chance −25% | All |
| Martial Law | −60% | −0.055% | – | – | +10% | – | – | All |
| Brutal Oppression | −75% | −0.11% | +25% | +100% | +10% | – | Resistance decay speed +100% | Fascist only |
| Liberated Workers | −15% | −0.025% | −15% | +25% | +30% | +20% | – | Communist only |
| Local Autonomy | +10% | +0.02% | −40% | −25% | – | – | – | Democratic only |
| Reconciliation | – | +0.03% | −50% | −30% | – | – | Resistance decay speed +50% | Turkey (Battle for the Bosporus) on Kurdish core states, after *A Common Destiny for All of Turkey* or *Permit Regional Elections* |
| Colonial Police | −30% | −0.02% | −30% | −40% | – | – | – | Italy (By Blood Alone) on African states after *Ministry of Italian Africa*; also Albanian cores after *Albanian Fascist Militia* |
| Colonial Police (Improved) | −35% | −0.015% | −35% | −45% | +25% | +25% | – | Italy (By Blood Alone) after *Regional Development* |
| Colonial Police (Final) | −45% | −0.010% | −40% | −55% | +25% | +25% | Local manpower +5% | Italy (By Blood Alone) after *Polizia dell'Africa Italiana* |
| Secretaries General | −30% | −0.020% | −30% | −40% | – | – | – | Occupiers of Belgium (Götterdämmerung) on Belgian cores after *Secretaries General* |
| Independent Rule | −10% | +0.03% | −50% | −50% | −35% | −35% | – | British Raj (Graveyard of Empires) on princely states after *Princely States Policy* |
| Princely Subjugation | +60% | −0.10% | +15% | −10% | +60% | +60% | – | British Raj (Graveyard of Empires) on princely states after *Princely States Policy* |
| Senbu | −20% | +0.01% | +5% | −35% | −10% | −10% | – | Japan (No Compromise, No Surrender) on Chinese states after *Invest in Senbu* |
| East Asian Exploitation | −40% | −0.08% | +30% | +60% | +60% | +20% | Military and civilian factory repair speed +25%; military and civilian factory sabotage chance −25% | Japan (No Compromise, No Surrender) on Asian states after *The Greater East Asia Co-Prosperity Sphere*, "Emperor's supreme authority" option |
| East Asian Prosperity | −15% | – | +5% | −25% | +5% | +10% | – | Japan (No Compromise, No Surrender) on Asian states after *The Greater East Asia Co-Prosperity Sphere*, "Prosperity for all Asian states" option |

### Collaboration government (requires La Résistance)

Collaboration is built with the **create a collaboration government** covert operation:

- Each successful use raises the starting compliance of that country's occupied states by **30–45%**, up to **100% collaboration** (70% collaboration = 70% starting compliance).
- It also lowers the surrender-progress threshold needed for the target to capitulate.
- Progress is visible in the "collaboration governments" tab.

At **80% average local collaboration** the occupier may install a collaboration government. **Democracies cannot create collaboration governments.** The resulting puppet:

| Rule / modifier | Value |
|---|---|
| May declare wars | No |
| May decline call to war | No |
| Control of deployed units goes to overlord | Yes |
| Can create collaboration governments | No |
| Can be spymaster / contributes operatives | No / No |
| Master can build in subject's territory | Yes |
| Technology sharing bonus | −50% |
| Subject manpower requirement | +100% |
| Extra trade to overlord | +100% |
| Overlord trade cost | −90% |
| Civilian industry to overlord | +75% |
| Military industry to overlord | +75% |
| Peace score transferred to overlord | +20% |
| Lend-lease tension limit from puppet | −10% |
| Autonomy to advance a tier | 1000 |

Behaviour notes:
- It becomes a separate tag with cores on **every** core state of the country it represents, regardless of what it actually controls — so the overlord needs no garrison there and resistance stops forming.
- It uses the generic focus tree, adopts the master's map colour and the master's adjective in its name ("Japanese China"), but inherits the represented country's research. If the represented country no longer exists, the collaboration government takes over its role and focus tree.
- Compliance is tracked from **one tag per state**: the owner if it has a core there, otherwise the leftmost core in the list. Annexing the Chinese warlords directs resistance at China, since China is cored first.
- Tags that are another nation's core (Macedonia, Croatia, Occitania, Algeria …) cannot be made into collaboration governments — only released as ordinary puppets. Releasing one also cedes the releaser's own cored provinces inside its territory.
- A collaboration government cannot be made from an existing puppet. Under AI control it never changes its own autonomy; under player control it can raise autonomy, become a regular puppet, and eventually go free.

## Puppets and autonomy

A puppet's government is replaced with one matching the overlord's ideology. Puppets can be called into the overlord's wars, cannot make peace-conference demands themselves (except high-autonomy types such as dominions and satellites), and cannot puppet other countries. If the overlord capitulates, its puppets capitulate too unless a not-yet-capitulated major remains in the puppet's faction — in which case the puppet **gains autonomy points** instead. Victors can free puppets from a defeated overlord. **Communist countries puppet at a 35% cost reduction** (the wiki also states a 10% peace-deal puppet discount for communists — see the ideology peace-conference table: communist puppet cost −10%).

> ⚠️ The Puppet page gives the communist puppeting discount as both 35% and 10% in different sections; the Ideology page lists −10% puppet cost for communism.

### Why puppets are useful

- **Discounted resource imports:** up to 8 loads of a resource per factory. An Integrated Puppet (e.g. Malaya) gives 80 loads per factory (90% discount), a colony (British Raj) 16 loads (50% discount), a dominion 10 loads (25% discount).
- **Extra trade to overlord** applies on top of the puppet's own trade law, to the resources it did *not* export. Example: a puppet with 200 steel on Free Trade exports 160; a dominion's +25% extra trade adds 25% of the remaining 40, giving the overlord 170 of 200. Integrated puppets can be milked even on Closed Economy.
- Integrated Puppets, Reichskommissariats/Reichsprotektorates and Imperial Associates/Protectorates hand over a share of civilian factories (including refineries) and a large share of military factories; naval dockyards are never transferred.
- Licence production of the puppet's equipment at a discount or free at some autonomy levels, plus a research bonus for that equipment while the licence runs.
- The overlord can request control of puppet divisions, and can raise **colonial divisions** mixing its own and the puppet's manpower (**70% for a Colony, 90% for a Puppet, 100% for an Integrated Puppet**), using templates from the puppet's template list (crown icon in the division designer). A newly released puppet inherits the master's templates.
- Puppets need no garrisons of their own on their cores and can send garrison support.
- Puppeting raises less world tension than annexation, and preserves the puppet's fleet.
- Some autonomy levels transfer war score to the overlord; with La Résistance, Satellites, Dominions, Imperial Subjects and Supervised States can contribute spies to a spymaster.

Costs of being a puppet: reduced factories (resources go to the master), no war justification or declaration, no peace-conference demands, forced calls to war (Imperial Subjects may decline), and the constant autonomy struggle.

### Autonomy ladder — default (democratic/communist/non-aligned overlord)

Within each level autonomy runs **0 to 1000**. At **1000** the subject advances a tier (or goes free from Dominion); at **0** the master may demote it (or annex from Integrated Puppet). **Changing tier costs 50 PP; annexing costs 300 PP; becoming free costs 300 PP.**

| Level | Key rules | Modifiers | Autonomy to advance |
|---|---|---|---|
| Dominion | No wars, no declining calls to war; overlord cannot build; can be spymaster and generates spies | Extra trade for overlord +25%; overlord trade cost −25%; peace score to overlord +5%; lend-lease tension limit −10% | 1000 |
| Colony | As above but overlord can build; no spymaster | Extra trade +50%; overlord trade cost −50%; research sharing −50%; subject manpower requirement +70%; peace score +10%; lend-lease tension limit −30% | 1000 |
| Puppet | Overlord can build; no spymaster | Extra trade +100%; overlord trade cost −90%; research sharing −50%; subject manpower requirement +90%; peace score +10%; lend-lease tension limit −40% | 1000 |
| Integrated Puppet | Deployed units go to the overlord; overlord can build | Extra trade +100%; overlord trade cost −90%; research sharing −50%; subject manpower requirement +100%; civilian industry to overlord +25%; military industry to overlord +75%; peace score +20%; lend-lease tension limit −40% | 1000 (only 150 with an Austro-Hungarian Vassal or Volkskommissariat in the ladder) |

### Autonomy ladder — fascist overlord

Three levels, each running **0 to 1500** (Reichskommissariat 1000), so the same total distance to freedom. PP costs unchanged (50 / 300 / 300).

| Level | Key rules | Modifiers | Autonomy to advance |
|---|---|---|---|
| Satellite | No wars; overlord cannot build; generates spies | Subject manpower requirement +40%; extra trade +40%; overlord trade cost −40%; licence cost between subject and master −100%; all autonomy gain −30%; peace score +10%; lend-lease tension limit −30% | 1500 |
| Reichsprotectorate | Overlord can build | Subject manpower +70%; recruitable population −25%; extra trade +60%; overlord trade cost −60%; civilian industry to overlord +25%; licence cost −100%; peace score +5%; lend-lease tension limit −30%; all autonomy gain −30% | 1500 |
| Reichskommissariat | Units deployed to overlord; overlord can build | Subject manpower +90%; recruitable population −50%; extra trade +100%; overlord trade cost −90%; civilian industry +25%; military industry +65%; licence cost −100%; all autonomy gain −30%; peace score +10%; lend-lease tension limit −30%; resistance target in occupied states −10% | 1000 |

### Autonomy ladder — Imperial Japan

Two base levels plus the Manchukuo-only Imperial Subject. **Imperial Associate** requires the subject to be fascist or non-aligned; **Imperial Protectorate** and **Imperial Subject** require the *overlord* to be fascist or non-aligned. Protectorate → Associate costs **2500** autonomy; Associate → freedom costs **1500**. PP costs unchanged.

| Level | Key rules | Modifiers | Autonomy |
|---|---|---|---|
| Imperial Subject | May declare wars and decline calls to war; overlord can build; generates spies | Subject manpower +50%; extra trade +25%; overlord trade cost −25%; civilian industry +10%; military industry +25%; peace score +1%; lend-lease tension limit −30% | Caps at 1000 and cannot go free (Manchukuo only, via focus *Assertiveness*) |
| Imperial Associate | No wars; overlord can build | Subject manpower +70%; extra trade +60%; overlord trade cost −60%; civilian industry +25%; all autonomy gain −30%; peace score +5%; lend-lease tension limit −20% | 1500 (500 for Manchukuo with *Assertiveness*) |
| Imperial Protectorate | Units deployed to overlord; overlord can build | Subject manpower +90%; extra trade +100%; overlord trade cost −90%; civilian industry +25%; military industry +65%; all autonomy gain −30%; peace score +20%; lend-lease tension limit −10% | 2500 |

Manchukuo can only become free by focus; it raises from Imperial Protectorate to Imperial Associate only after *Strengthen the Concordia Association* or *Obedience*, and reaches Imperial Subject via *Assertiveness* (immediately) or manually after *The Two Emperors* or *Claim Outer Manchuria*.

### Special subject types

| Type | Who / when | Modifiers | Autonomy |
|---|---|---|---|
| Supervised State (democratic) | Created in a peace deal by a member of a faction founded by a democracy. Boosts the overlord's ideology in the subject, blocks ministers that shift ideology, cannot be annexed, drifts to freedom over time | Master ideology drift +0.30; extra trade +25%; overlord trade cost −25%; **daily autonomy progress +2.0**; peace score +15%; lend-lease tension limit −20% | 1250 |
| Collaboration Government | Fascist, communist and non-aligned occupiers at 80% collaboration; sits between Integrated Puppet / Reichskommissariat / Imperial Protectorate and Annexed | See the collaboration-government table above | 1000 |
| Personal Union | One-time creations by Poland, non-aligned Germany and Lithuania via focuses/decisions; cannot be annexed and break free if autonomy rises | Extra trade +50%; overlord trade cost −50%; peace score +5%; lend-lease tension limit −10% | 0 |
| Nordic defense council member | Sweden only, over Denmark, Iceland, Finland, Norway; sits below Integrated Puppet and replaces Annexed (so Sweden can never annex a Nordic nation) | Subject manpower 100%; extra trade +100%; overlord trade cost −80%; civilian industry +35%; military industry +65%; all autonomy gain −30%; peace score +50%; lend-lease tension limit −40% | 1000 |
| Austro-Hungarian Vassal | Austria (*Demand Hungarian Submission* / *Bring Hungary Back Into the Fold*) or Hungary (*The Lands of the Crown of Saint Stephen*) over the Danubian tags; sits between Integrated Puppet and Puppet and drops the Integrated Puppet annexation cost to **125** | Technology sharing −50%; subject manpower 90%; extra trade +100%; overlord trade cost −90%; peace score +10%; lend-lease tension limit −40% | 1000 |
| EU Member State | Belgium (*European Community* / *The Council of Europe*), Austria (*Via the Danube to Europe*), Netherlands (*Foundations for a European Union*) over European tags; sits between Annexed and Integrated Puppet | Technology sharing **+10%**; subject manpower 50%; extra trade +50%; overlord trade cost −45%; peace score +5%; lend-lease tension limit −40%; can be spymaster | 1000 |
| Volkskommissariat | Communist Germany after *Establish Volkskommissariats*; between Integrated Puppet and Puppet, dropping Integrated Puppet cost to **125** | Recruitable population −50%; subject manpower 90%; extra trade +100%; overlord trade cost −90%; civilian industry +50%; military industry +50%; all autonomy gain −30%; licence cost −100%; peace score +10%; lend-lease tension limit −20% | 1000 |
| Warlord Subject | Chinese tags; placement depends on ideology (for non-aligned China it replaces the whole ladder; otherwise it sits between Colony and Dominion, or between Reichsprotectorate and Satellite for fascists) | Technology sharing −10%; subject manpower 50%; extra trade +50%; overlord trade cost −45%; peace score +5%; lend-lease tension limit −40% | 2000 |
| Integrated Warlord Subject | Usually only available to fascist overlords; the tier below Warlord Subject converts into this once the subject reaches Warlord Subject | Technology sharing −10%; subject manpower 90%; extra trade +100%; overlord trade cost −90%; peace score +10%; lend-lease tension limit −40% | 500 |
| Associated Dominion | Australia as a British subject after its late-tree focuses; between free and Dominion | May declare wars, may decline calls to war, can be spymaster; extra trade +25%; overlord trade cost −25%; lend-lease tension limit −10% | 1000 |
| Indonesian Union State | Dutch East Indies over the Indonesian releasables; below Integrated Puppet, replaces Annexed | Subject manpower 100%; extra trade +100%; overlord trade cost −10%; civilian industry +30%; military industry +75%; all autonomy gain −30%; peace score +50%; lend-lease tension limit −40% | 1000 |

### Changing autonomy — the numbers

| Action | Autonomy change |
|---|---|
| Overlord lend-leases equipment to the subject | **−1 per 100 production cost** transferred (1000 Infantry Weapons I at 0.5 each = −5). Equipment must be at least as good as the best the subject can build itself, and must not be foreign-made |
| Subject lend-leases equipment to the overlord | **+1 per 20 production cost** transferred; must be at least as good as the best the overlord can build |
| Overlord constructs in the subject | **−0.7 per 100 industrial capacity** invested (a 7200-cost military factory = −50.4). Some subject types block overlord construction unless they share a faction |
| Overlord trades for the subject's resources | **+0.005 per day per resource exported** to the overlord |
| Subject fights in the overlord's wars | roughly **+60% of the war score it generates** (exact formula unknown) |
| Continuous focus *Suppress Subjects* | −0.5 per day to all subjects |
| Continuous focus *Increase Autonomy* | +0.5 per day (cancels out against *Suppress Subjects*) |
| Overlord capitulates | Every subject instantly gains **50% of the autonomy needed for its next tier** — normally 500, and much more under fascist overlords with their larger ranges |
| Overlord sends an attaché to the puppet | −0.05 per day |
| Puppet sends an attaché to the overlord | +0.05 per day |

Country-specific focuses and spirits also move autonomy — currently the United Kingdom, Commonwealth nations, the Netherlands, Italy and Manchukuo.

**Routes to independence:** raise autonomy to the cap and pay 300 PP, or start a civil war (boost another ideology with advisors) and beat both the loyalist government and the overlord — a victorious rebel puppet may end up controlling its former overlord.

Puppet naming is heavily scripted (British, German, Soviet, Italian, Japanese, French, Yugoslav, Ethiopian, Hungarian, Swedish and generic name sets, e.g. Reichskommissariat Ukraine, Ukrainian SSR, Dominion of Canada, Vichy France); the full list is on the wiki's Puppet page.

## Governments in exile

Introduced in **Man the Guns** and expanded in **By Blood Alone**. A defeated country can survive hosted by another country, normally a faction partner. Originally only democracies annexed by Germany; By Blood Alone added non-aligned Ethiopia.

- **Legitimacy runs 0 to 100** and is derived from the exiled country's war score before capitulation — the higher the war score, the higher the legitimacy. Legitimacy raises manpower and unlocks exiled generals and veteran divisions.
- Governments in exile can still take focuses and decisions; many unlock only after going into exile.
- Effects on their occupied core states:
  - **Compliance gain −0.00015% per day per legitimacy** (−0.015%/day at 100 legitimacy).
  - **Resistance target +2%, plus +0.18% per legitimacy**, to a total of **+20% at 100 legitimacy**.
- The *Weapons for the Resistance* spirit adds resistance growth +10% in those cores.
- The exile only functions while the country is occupied, not annexed: total annexation (including in a peace conference) ends the game for that country.

Scripting hooks: `become_exiled_in = { target = <tag> legitimacy = <0-100> }`, `add_legitimacy`, `set_legitimacy`, `end_exile`; triggers `has_legitimacy > X`, `is_exile_host`, `is_hosting_exile = TAG`, `is_government_in_exile`, `is_exiled_in = TAG` (all added in 1.6).
