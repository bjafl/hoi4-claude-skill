---
title: Diplomacy, Factions, World Tension and Peace
category: mechanics
tags: [diplomacy, faction, world tension, war goal, justification, peace conference, war score, war participation, guarantee, non-aggression pact]
game_version: "1.19"
dlc: [La Résistance, By Blood Alone]
sources:
  - https://hoi4.paradoxwikis.com/Diplomacy
  - https://hoi4.paradoxwikis.com/Faction
  - https://hoi4.paradoxwikis.com/World_tension
  - https://hoi4.paradoxwikis.com/War_goal
  - https://hoi4.paradoxwikis.com/Peace_conference
  - https://hoi4.paradoxwikis.com/War_participation
  - https://hoi4.paradoxwikis.com/List_of_Factions
---

## Summary

Diplomacy is bilateral and asymmetric — opinions and acceptance chances are computed independently for each side. **World tension** (0–100%, overflow acts as a buffer) gates the aggressive actions of democracies and non-aligned countries and speeds up justification for everyone. A **war goal** is required to declare war and gives a peace-conference discount on its target. Wars are scored by **war participation**, which converts into **war score** in the peace conference, where victors bid on states, ships and other demands over a series of turns.

## Diplomatic actions

| Action | What it does | Requirements | How it ends |
|---|---|---|---|
| Declare war | The only way to start a war | A war goal on the target | Only after 6+ months of war, as faction leader, on the losing side, with the winner's war score at least 50% |
| Justify war goal | Starts justification against another country | Target is not an ally; variable political power that rises with world tension (minimum 2 PP); modified by subversive-activity modifiers | — |
| Guarantee independence | If anyone declares war on the guaranteed nation, it automatically joins the guarantor's faction. If you guarantee both the aggressor and the victim you do not intervene | Same ideology as the target; **15 PP for the first guarantee, +15 for each subsequent one** (30, 45, 60 …); world tension threshold reached | Cancelled if the target does not guarantee you |
| Call to arms | Calls an ally into a war | Same faction | Cannot be cancelled |
| Ask/offer military access | Move troops through another country's territory; automatic between faction members | Target must accept | No troops on the granting country's territory |
| Ask/offer docking rights | Move ships into another country's ports (extends naval range); automatic between faction members | Target must accept | — |
| Improve relations | Raises relations up to +100 over time | Not at war with the target; **10 PP up front, then 0.2 PP/day (same ideology) or 0.4 PP/day (different ideology)** | — |
| Send attaché | Gives the sender army experience, war support and visibility of the receiver's military | Target must be at war; **100 PP plus 50 command power allocated** | — |
| Non-aggression pact | Disables "justify war goal" and "declare war" between the two | Target must accept | Not breakable without a common border or during the first 12 months. **Months 12–18: needs a 2:1 troop ratio on the common border; 18–24: 1:1; after 24: 1:2. NAPs expire after 48 months.** Declaring war on a third country guaranteed by your NAP partner still drags them in. You cannot justify or declare on any member of a faction whose leader you have a NAP with |
| Invite to faction | Adds a country to your faction | Must be faction leader; target must accept; **the inviting country's ideology needs more than 30% popularity in the target** | A kicked country must wait **90 days** before rejoining |
| Request licence production | Produce another country's equipment and research the unlocking technology faster; paid with civilian factories | Target must accept | **30 days minimum** before cancelling |
| Create faction | Found a new faction with an invited country | A focus or rule granting faction creation; same ideology; target must accept | — |
| Join faction | Joins the faction and all its wars | Target is a faction leader; you are factionless; world tension threshold reached; leader must accept | Cannot leave while at war alongside faction members |
| Start lend-lease | Send equipment to any non-enemy country at war — a one-off shipment, a fixed monthly amount, or a percentage of monthly production (not both at once); shipments arrive once a month | Target needs convoys unless there is an unobstructed land path; world tension threshold reached | Editable/cancellable at will |
| Request lend-lease | Ask for specific equipment archetypes | Target must accept; must be at war | — |
| Join wars | Join a faction member's war | Not already at war alongside allies; target is faction leader | Not cancellable |
| Send volunteers | Sends a limited number of divisions; you keep control, but they only come home when you go to war | Target at war; you at peace; not in the same faction as the target; division-count threshold; world tension threshold | — |
| Expeditionary force | Sends unlimited divisions to a faction member; **control transfers** | Fighting a war together; target is an ally and must accept; divisions on land | Donor uses Return Expeditions, or the recipient disbands them |
| Request forces | Take control of some of a puppet's divisions | Target must be your puppet | A disband order returns them |
| Boost party popularity | Raises your ideology's popularity in the target. With La Résistance this becomes the Boost Ideology operative mission | **0.25 PP/day** | — |
| Stage a coup | Prepares a coup, usually starting a civil war. With La Résistance this becomes the Orchestrate Coup operation | **200 PP, accumulating at up to 0.5 PP/day**, modified by subversive-activity modifiers; thousands of infantry equipment (scaling with the target's population) | — |
| Ask/give control of state | Transfer control of an occupied state | Must be in a war together; sufficient war contribution; the state must not be a core of the target | Reversible only via the opposite action |
| Reduce subject autonomy | Demotes a subject a tier | Subject's autonomy low enough; PP cost affordable | Cannot be cancelled |
| Request garrison support | Ask a puppet or faction member for garrison manpower | Target must accept | — |
| Issue trade embargo | Blocks trade with a country (requires By Blood Alone) | Not at war with them; not in the same faction; the target has generated enough world tension; PP cost | — |

Extra notes:
- Granting military access makes the granting nation eligible to claim provinces you capture (see territorial control).
- **Coups** require choosing the state where the civil war starts; the number of states that join the rebellion scales with party popularity when the PP requirement completes, so pair it with Boost Party Popularity. **A coup in a one-state country automatically succeeds at over 40% party popularity**; elsewhere it starts a civil war.
- With La Résistance, the **Diplomatic Pressure** operative mission makes a target more willing to accept faction invitations and NAPs (and less willing to make them with others), and can lower the tension needed for a target to join a faction by **0.001 per operative per day, up to −20% tension**, decaying when unassigned; extra operatives stack at 0.5 efficiency per rank.

> ⚠️ The Government page states guarantees cost 25 PP with +25 per subsequent guarantee, while the Diplomacy page states 15 PP with +15 (30/45/60). The Diplomacy page's figure is the more detailed one.

## World tension

World tension (0–100% displayed) is the sum of every tension event to date, minus decay. **Totals above 100% have no extra effect but act as a buffer** against tension-reducing events.

**Raises tension:** declaring war; annexing non-core territory in a peace treaty (especially without claims); sending volunteers; joining a faction; joining a war as an attacker; justifying a war goal; revoking a guarantee; various focuses, decisions and events.

**Lowers tension:** decay (0.5 per month); concluding a peace treaty; changing a country's government in a peace treaty; annexing your own core territory in a peace treaty; liberating a country in a peace treaty; adding a demilitarized zone (By Blood Alone); a democracy guaranteeing a nation's independence.

**Decay:** each individual event decays toward 0 at **−0.005%/day (−1.825%/year)** — including tension-*reducing* events. **Tension events from countries that are at war do not decay.**

### General effects

- Justification time and cost: **−0.005% per 1% of world tension, up to −50% at 100%**.
- War support for every nation: **+0.4% per 1% of tension, up to +40% at 100%**.
- Calling other countries into an ongoing civil war requires **at least 50% tension**.
- The AI accepts conditional surrender less readily at high tension, avoids factions with high-tension countries, and embargoes them more readily (global tension is weighted 0.2 in its faction calculations).

### Tension thresholds by ideology

| Action | Communist | Democratic | Fascist | Non-Aligned |
|---|---|---|---|---|
| Justify war goal | none | 100% | none | 50% |
| Join faction | none (hidden −0.1 modifier) | 80% (capped at 50% in a defensive war) | none (hidden −0.1 modifier) | 40% |
| Send Lend-Lease | 50% | 50% | 50% | 60% |
| Send volunteers | none | 50% | none | 40% |
| Guarantee independence | none | 25% | none | 40% |

Democracies additionally **cannot justify against another democracy**, nor against a country that has generated no world tension.

Two modifiers shift these thresholds directly and are attached to focuses, spirits and leader traits — they are expressed as a fraction of tension (1.0 = 100%):

- `generate_wargoal_tension` (and `generate_wargoal_tension_against` for a single target): e.g. the generic *expansionist_policies* leader trait gives −0.25; many aggressive traits give −0.5.
- `guarantee_tension`: e.g. Belgium's *le_patron* leader trait gives −0.2.

### Tension generated by joining factions and wars

Joining a faction adds a base of **+4 tension**, multiplied by the joiner's ideology factor (`faction_impact_on_world_tension`, and the global `TENSION_SIZE_FACTOR = 1`):

| Ideology | Faction impact factor | Tension from joining | War declaration factor (`war_impact_on_world_tension`) |
|---|---|---|---|
| Communist | 0.5 | +2.0 | 0.75 |
| Democratic | 0.1 | +0.4 | 0.25 |
| Fascist | 1.0 | +4.0 | 1.0 |
| Non-Aligned | 0.1 | +0.4 | 0.25 |

Joining an ongoing war on the **attacker's** side generates a further base of **+2 tension**.

### Focuses gated behind world tension

Generic tree: **Why We Fight** needs more than 75% tension unless the country is in a defensive war.

| Country | Focus | Tension needed |
|---|---|---|
| Afghanistan | Join the Axis / Align With the Allies / Eliminate Pakistan | >25% / >45% / >50% |
| Argentina, Brazil, Chile | The Department of Propaganda | >49% |
| Australia | Establish Advisory War Council | >20% |
| British Raj | Provincial Elections (if not independent, without Graveyard of Empires) | >10% |
| Bulgaria | Join the Tripartite Pact | >35% |
| Chile | Protect Easter Island | >50% |
| Czechoslovakia | Defensive Preparations | >10% |
| Dominion of Canada | Shadow Factories / Rifle Association (if not independent) / Defense of Canada Regulations | >5% / >15% / >20% |
| Denmark | Reclaim Norway (fascist / non-aligned) / Secure Swedish Steel / Total Krig | >15% or >20% / >20% / >90% |
| Finland | Extra Refresher Exercises / Weapon Caches / Northern Defense Front / The Lone Wolf / Approach Major Democracies / Join the Allies / Operation Kilpapurjehdus / Viron Kansa (if not fascist) | >25% / >35% / >50% / >50% / >55% / >55% / >70% / >70% |
| Germany | Mass Production / Build a Defense Industry | >15% / >30% |
| Iceland | United We Stand, Declare Absolute Neutrality / The Armed Forces of Iceland / Not Standing Idly By, Political Unity | >5% / >10% / >15% |
| Mexico | Rescind the Mexican Cession | >50% |
| Netherlands | Protect Against Britain, Germany is the Greater Threat / Further Reinforce the Ports, Fortress Holland, War on Pacifism, Secret Staff Talks / Expand Curaçao Oil Refineries, Southward Defenses, Modernize the Grebbe Line / Go with Britain | >10% / >15% / >20% / >25% |
| Poland | Join the Allies, Preserve Bourgeoisie Democracy, Trust in the West (if not democratic) | >40% |
| Portugal | Securing the Free World | >40% |
| Romania | King Michael's Coup | >25% |
| South Africa | War Measures Act (if democratic) | >20% |
| Soviet Union | Move Industry To the Urals | >85% |
| Sweden | The Old Enemy Stirs | >10% (or >8% war support) |
| United Kingdom | Air Defense, The Shadow Scheme (if democratic) / General Rearmament (if democratic), Issue Gasmasks / Military Training Act | >5% / >20% / >50% |
| United States | Two Ocean Navy Act and Selective Training Act need more Congress support below 50% tension; The Giant Wakes needs war support that is hard to reach at low tension | — |

**Inferred:** fascist and communist powers benefit from keeping tension low (their enemies rearm and intervene later), while democracies and non-aligned countries want it high so they can rearm and act.

## Factions

### Forming and joining

- A country can create a faction only if it has the corresponding **country rule**. At game start the rule is held by Germany, the United Kingdom, the Soviet Union and the United States; other countries unlock it through focuses (or, on the generic tree, via **Ideological Fanaticism** or **Why We Fight**).
- Joining is gated by ideology-based world tension thresholds (see table above), the faction's own **joining rules**, and the leader's acceptance. Inviting requires the inviter's ideology to have **more than 30% popularity** in the target.
- Faction members automatically share **military access** and **accurate intelligence** on each other in the diplomacy screen.
- Faction rules can override country rules such as justifying against the same ideology and what peace-conference actions are allowed.
- Leaving costs the **faction traitor** modifier (**−75 relations**) and is impossible while fighting a war alongside members. The leader may kick members even during a war, and may disband a faction containing only itself and its subjects. If the leader ceases to exist, the largest remaining member takes over.
- A country fighting alongside major allies **only surrenders once all majors in the faction have capitulated** — Poland in the Allies fights on (or becomes a government in exile) until the UK and France fall, and conversely is forced to surrender if they fall.
- **Assuming leadership** costs **200 PP** and requires meeting the faction's Leadership Change rules (if none are enacted, anyone may take over at any time). After a change, **no other country can claim leadership for 180 days**.

### Faction Power Projection

Computed from members' industrial, army, naval and air power plus completed faction goals. It sets the faction's global ranking, which drives how likely nations are to join and acts as a tiebreaker in peace deals.

### Initiative, manifesto and goals

- Every member holds its own pool of **faction initiative**, generated passively from manifesto fulfilment (spread by influence) and actively by completing faction goals. **Enacting or removing a faction rule costs 1 initiative.**
- Every faction has a **manifesto**: a scaling bonus by fulfilment percentage, plus an extra bonus at **75–100% fulfilment**. Examples:

| Manifesto | Used by (examples) | Progress measured by | Scaling bonus | Bonus at 75%+ |
|---|---|---|---|---|
| Defense of Democracy | American Commonwealth, Alpine Federation, Benelux, Morges Pact | Independent, uncapitulated democracies/dominions out of 40 | Trade deal opinion factor +20.00% | Can guarantee other ideologies; foreign democracy growth from guarantees +0.05 |
| Defense of Democracy (Allies) | Allies, NATO, Commonwealth of Nations | Same, out of 50 | Trade deal opinion +20.00%; guarantee cost −50% | Can guarantee other ideologies; foreign democracy growth +0.08 |
| Containment of World Communism | Coalition of Liberty, Anglo-Italian Pact, The Japanese Sphere | States controlled by non-communists out of all states | Daily communism support −0.08 | Generate war goal tension limit −15.0%; required garrisons −15% |
| Suppress Fascism | Bulwark Pact, Anti-Fascist Bloc | Non-fascist states in the continent | Daily fascism support −0.08 | Weekly war support (combat casualties) +0.60% |
| Suppress Communism in (Continent) | Shield Against the Red Threat, Ma Clique Collective | Non-communist countries in the continent | Daily communism support −0.05 | Weekly war support (combat casualties) +0.30% |
| Suppress Democracy | Iron Pact, Berlin-Moscow Axis | Non-democratic states in the continent | Daily democracy support −0.05 | Weekly war support (combat casualties) +0.30% |
| Generic Expansionism | (generic) | States in capital continent held by the faction out of 67% of them | Party popularity stability modifier +10.00% | Monthly population +15%; generate war goal tension limit −15% |
| Conquest and Domination | Axis | Foreign states occupied by the faction out of total faction core states | Justify war goal time −25.0%; offensive war penalty stability modifier +15.00% | Non-core manpower +3.00%; generate war goal tension limit −25.0% |
| The World Revolution | World Revolution, 4th International, Popular Front Bloc | All communist countries out of all countries | Daily communism support +0.10 | Recruitable population factor 5%; party popularity stability modifier +10.00% |
| Strength in Unity | Regional Defense Pact, European Unity, Pact of Rome | Faction members out of 20 | Trade deal opinion factor +20.00% | Political power gain +10% |
| Protector of Peace | Nations of the Empire, Asian Democratic Compact | Countries at peace out of all countries | Construction speed +10% | Trade deal opinion factor +20.00% |
| African Domination | African Unity | African states controlled out of all African states | Stability +8.00% | Division defense on core territory +5.0% |
| Pan-Americanism | Organization of American States, Mercosul, Hispanic Alliance | American states controlled out of all American states | Stability +10.00% | War support +5.00%; division defense on core territory +10.0% |
| Establish European / Asian Dominance; Control the Middle-East; Between the Seas; Enforce the Paris Peace Treaties; Balkan Security | European Front, Asian Front, Middle-Eastern Pact, Miedzymorze, Little Entente, Balkan Pact | Region-specific state control | Stability +10.00% | War support +5.00%; division/army defense on core territory +10.0% |
| Territorial Integrity | Chinese United Front, Popular Front | Chinese core states held by the leader's ideology out of 76 | Political power gain +10%; war support +10.00%; (inverse-scaling) division defense on core territory +10% | Subject autonomy gain −0.50 |
| Territorial Integrity (Chiang) | Chinese United Front | as above | as above but inverse-scaling defense +20% | Subject autonomy gain −0.50; autonomy gain from war score −10% |
| Chinese Consolidation | Nanjing Front, Chinese United Front | as above | Subject autonomy gain factor −30%; inverse-scaling defense +10% | Civilian and military industry to overlord +50% each |
| Triumph over Imperialism | Nanjing Front | Asian states held by the faction and core holder | Subject autonomy gain factor −30% | Civilian and military industry to overlord +50% each |
| Suppress Asian Communism | New Order in East Asia | Non-communist Asian-capital countries | Daily communism support −0.05 | Political power gain +10.00% |
| Strategic Resource Control | Greater East Asia Co-Prosperity Sphere, Industrial Charter | Faction share of global resource extraction (max at 30%) | Factory output +10.00%; dockyard output +10.00% | Construction speed +10.00% |
| African Decolonization | African Union | African states not held by a colonial power | Political power gain +15% | War support +10% |
| Habsburg Hegemony | Habsburg Alliance | Countries with a Habsburg ruler | Stability +15% | War support +10%; army defense on core territory +10% |
| Liberation of the Americas | Union of American Indigenous People | Faction-controlled American states | War support +15%; recruitable population factor +15% | Army attack and defense on core territory +10% |
| Islamic Brotherhood | Arab League, Saadabad Concordat | Islamic faction members out of potential Islamic countries | Political power gain +10%; army defense on core +10% | Army attack on core territory +10% |
| Baltic Security / Nordic Defense | Baltic Entente, Nordic Council | Faction-controlled Baltic / Nordic states | Attack, breakthrough and defense against major nations +15% each | Compliance growth +10% |
| Mare Nostrum / Pax Romana | Italian League, Imperium Romanum | Mediterranean / former Roman states held | War support +15% | Division attack and defense on core +10% each / compliance growth speed +10% |
| Security Through Expansion | Comintern | Starting border states controlled out of 41 | War penalty stability modifier +10.00% | Generate war goal tension limit −15.0%; can guarantee other ideologies; foreign communism growth from guarantees +0.10 |
| An Iron Curtain | Warsaw Pact | Same-continent communist countries | Civilian and military industry to overlord +15% each; subject autonomy gain −0.50; resources to overlord +15.00% | Generate war goal tension limit −15.0%; can guarantee other ideologies; foreign communism growth +0.12 |

- Each faction can hold one **short-, medium- and long-term goal** (some factions unlock more slots). Completing a goal generally gives **1 faction initiative** plus power projection and a bonus. Two structural goals matter most:
  - **Develop Joint Research Practices** (faction of 3+; research a set percentage more technologies) unlocks **Faction Research**.
  - **Institute a Joint Command Structure** (faction of 3+; 20% more divisions fielded) unlocks **Faction Military Operations**.
  - Other examples: *Expand the faction* (grow past 4 members), *Appoint a Spy Master*, *Convoy Sufficiency* (1000+ convoys), regional resource-development goals (Ploiesti, Baku, Malaya, Indonesia …) that permanently add resources to states, and base-fortification goals (Gibraltar, Suez, Singapore, Panama …).

### Faction rules

Rules are grouped into **Dismissal, Leadership Change, Membership, Joining, Manpower Contribution, Peace Conference, War Declaration and Call to War**. Each costs 1 initiative to enact or remove; several can only be changed at a given manifesto fulfilment. Notable numeric rules:

| Category | Rule | Effect |
|---|---|---|
| Peace Conference | Install Puppets | Puppet demands −20% cost; Take State +5% |
| Peace Conference | Discourage Puppets | Puppet demands +100% cost |
| Peace Conference | Liberate Others | Liberate −20%; Take State +5% |
| Peace Conference | Expand our Ideology | Force Government −20% |
| Peace Conference | Expand our Territory | Take State −10%; Liberate +5% |
| Peace Conference | Recover our Claims | Take State on claimed states −20%; Puppet +5% |
| Peace Conference | Expand China (Japan only) | Take State and Puppet on Chinese cores −5% each |
| War Declaration | Justify wargoal tension reduction 20% / 40% | `generate_wargoal_tension` −0.2 (stability −5%) / −0.4 (stability −10%) |
| War Declaration | World tension is at least 25% / 50% / 75% | Members may only declare war above that tension |
| War Declaration | Target has generated at least 10% / 25% tension | Mobilization speed +0.05 / +0.15 |
| Call to War | Guarantee tension reduction 15% / 40% | Guarantee tension limit −15% (stability −5%) / −40% (stability −10%) |
| Call to War | Faction leader only / Major countries only | Political power gain −10% / −5% for all members |
| Joining | Neighbour countries only | Enemy justify war goal time +0.2 |
| Joining | Same continent / African / American only | Enemy justify war goal time +0.1 |
| Joining | Chinese / Nordic / Balkan / Baltic only | Army core defence factor +0.05 |
| Joining | Islamic countries only | Stability +0.05 |
| Joining | Hispanic countries only | War support +0.05 |
| Joining | Own subjects only | Subject autonomy gain −5% |
| Joining | Countries at peace / not in offensive wars | Improve relations maintain cost −0.1 / defensive war stability +0.15 |
| Leadership Change | Leader cannot change | Members get research sharing −25% and surrender limit −5% |
| Manpower Contribution | Limited / Medium / High garrison requirement | Members must contribute at least 5% / 10% / 15% of monthly manpower |

### Faction research and military operations

- **Joint Research Facilities:** a member converts an Experimental Facility for **1 initiative** (max 3 assigned at a time; unassigning is free). Other members assign scientists as **Supportive Scientists for 25 PP** — they work at **25% effectiveness** at the facility and earn **10% progress** toward a project at home per completed iteration.
- **Technology Sharing:** research bonus starts at 0% and grows **+5% per Supportive Scientist**, multiplied by the number of member countries that already have the technology, **capped at 50%**. The Allies start with Commonwealth Technology Sharing.
- **Doctrine Sharing:** grants mastery on any sub-doctrine where another member has higher mastery. **1 initiative per branch** (land/navy/air); base **10 mastery per month**, **+2 per theatre commander**.
- **Faction Theatres:** up to **4**, each costing 1 initiative, owned by the country that unlocks it. A field marshal or admiral is assigned as **Theatre Commander**; the number of regions and countries covered scales with skill level. The commander's country receives a share of allied mastery earned in the theatre (based on attack/defense skill), and selected countries get land/naval supply-consumption bonuses (from planning/logistics or manoeuvring/coordination; admirals favour naval, field marshals land).
- **Manpower contribution:** members contribute **0%, 5%, 10% or 15%** of monthly manpower gain to a shared garrison pool; a member may request from it (only manpower contributed by others) in proportion to its own contribution level.

### Historical factions

| Faction | Formed by | 1936 members | Later members (1939) |
|---|---|---|---|
| Allies (UK) | Exists at start | United Kingdom, Dominion of Canada, British Raj, Australia, New Zealand, South Africa, British Malaya, British Burma, Mandatory Palestine, Kuwait, Oman | + France, Republic of Syria, Lebanon |
| Axis (Germany) | Exists at start | German Reich | + Slovakia, Protektorat Böhmen-Mähren, Italy |
| Comintern (Soviet Union) | Exists at start | Soviet Union, Tannu Tuva, Mongolia | same |
| American Commonwealth (USA) | Exists at start | United States, Commonwealth of the Philippines | same; dissolves as soon as the USA joins the Allies |
| Chinese United Front | Focuses *One Nation, Undivided*, *Burn the Paper Tigers*, *Declare Opposition*, *Invite Chiang Kai-Shek for Troop Inspections* | China, Chinese Soviet Republic, Qinghai Ma, Gansu Ma, Ningxia Ma, Yunnan, Guangxi Clique, Sinkiang | same |
| New Order in East Asia | Focus *The New Order in East Asia* | Japan, Manchukuo, Mengkukuo | same |
| Greater East Asian Co-Prosperity Sphere | Focus *The Greater East Asia Co-Prosperity Sphere* | Japan, Manchukuo, Mengkukuo, Siam, Philippines, India, Burma, Reorganized National Government | same |
| The Peoples Front | Focus *Prepare for the Inevitable* | Chinese Soviet Republic (1945, when Communist China attacks the rest of China) | — |
| NATO | — | Renames the Allies; no other change | — |
| Warsaw Pact | Focus *Found the Warsaw Pact* | Renames the Comintern, switches its manifesto to *An Iron Curtain* and adds a long-term goal | — |

Custom factions are created from **templates** that set the starting manifesto, rules and goals — e.g. *Defensive Democratic Faction* (democratic; Defense of Democracy), *Coalition of Liberty* (anti-communist), *Bulwark Pact* (anti-fascist), *Iron Pact* (anti-democratic), *World Revolution* (communist), *Regional Defense Pact*, *Industrial Charter*, *African Unity*, *Organization of American States*, *Hispanic Alliance* (leader cannot join other factions), *European Unity*, *European Front* (fascist and monarchist variants), *Asian Front* and *Middle-Eastern Pact*. Dozens of named country factions (Little Entente, Stresa Front, Latin Entente, Mercosul, Danubian Bloc …) reuse these templates — see the wiki's *List of Factions*.

AI-created ad hoc factions draw names from ideology-specific lists, e.g. communist "The \<leader\> Compact" / "\<continent\> Syndicate", democratic "The \<continent\> Entente" / "\<continent\> Coalition", fascist "Brotherhood of \<continent\>" / "The \<continent\> League", non-aligned "\<continent\> Defense League" / "The \<continent\> Alliance".

## War goals

A war goal is required to declare war and gives its holder a discount on the relevant peace-conference action. Justification **costs political power, raises world tension and normally takes 6–9 months**; a completed regular casus belli stays **valid for 2 months**.

| War goal | ID | Acquired by | Justification cost | Expires | Peace conference effect |
|---|---|---|---|---|---|
| Conquer | take_state | Justifying to take non-claimed states (max 5) | **200 PP base + 50 PP per state** | 60 days | −20% cost to take the target states |
| Conquer (Focus) | take_state_focus | National focus | — | 730 days | −20% cost to take the target states |
| Puppet (Focus) | puppet_wargoal_focus | National focus | — | 730 days | −50% cost to puppet the target |
| Take claimed state | take_claimed_state | Justifying to take claimed states (max 5) | **100 PP base + 10 PP per state** | Never | −50% cost to take the target states |
| Retake core state | take_core_state | Justifying to take core states (max 5) | **125 PP** | Never | −80% cost to take the target states |
| Annex | annex_everything | National focus | — | Never | None |
| Civil War | civil_war | Country is in a civil war | — | Never | −75% cost and −90% world tension for annexing the target |
| Topple Government | topple_government | National focus | — | Never | −50% cost to change the target's government |
| Liberate | liberate_wargoal | National focus | — | 730 days | −50% cost to puppet the target |
| Independence | independence_wargoal | National focus | — | Never | None |

Justification also drains **0.2 PP per day** while it runs — a PP shortfall stalls it. Cost and time modifiers:

- World tension: **−0.005% per 1% tension, up to −50%**.
- **−90%** when justifying against a major power that is at war.
- Fascists already at war with a major power justify **80% faster**.
- Subversive-activity modifiers change the cost.

> ⚠️ The Government page quotes much lower justification costs (Conquest 50 PP +10 per extra state, +5 against the Neutral Foreign Policy spirit; Retake core state 25 PP) than the War goal page's table (200 + 50/state; 125). The War goal page is the more detailed and more recent source; treat the Government page figures as outdated.

### Ideology restrictions on war goals

| Ideology | Restrictions and effects |
|---|---|
| Communism | Virtually no restrictions. Can force government. 30% cost reduction when puppeting |
| Democracy | Cannot start a war against another democracy; cannot justify against a country that has generated no world tension; cannot send volunteers; cannot puppet; cannot occupy a country without war (captured neutral territory is returned); +25% cost to take states; +50% cost to annex a country |
| Fascism | Virtually no restrictions; cannot force government; can occupy a country without war; −80% justification time while at war with a major power |
| Non-Aligned | Cannot force government; cannot send volunteers; can puppet |

## War participation

War participation (WP) is each belligerent's share of its own side's contribution: `p = w / s` (own WP points ÷ side's total WP points). The war summary window shows the running calculation with a per-category breakdown.

| Category | Formula |
|---|---|
| Occupation | `w = 4 × (0.2s/p + 0.2v + 1)` — s = state value, p = provinces in the state, v = victory points of the province. First capture only; lake provinces score nothing but still count in p |
| Land combat damage | `w = [1.2] × 0.1c + 0.08i` — c = strength (HP) damage, i = IC cost of destroyed equipment. The 1.2 applies only when the scorer is both attacker and winner. Annihilating a division counts all its remaining equipment, but not its remaining strength |
| Destroyed enemy planes | `w = 0.08i` (IC cost of downed aircraft). Kills by state or divisional AA do not count |
| Strategic bombing | `w = 0.02b − 0.1ft` — b = bombing damage points, f = civilian factories still standing, t = months elapsed |
| Convoy raiding | `w = 0.1i` (IC cost of sunk convoys) |
| Sunk enemy ships | `w = 0.1i + 0.004m` — i = IC cost, m = manpower lost |
| Casualties | `w = 0.5c` per 1000 manpower lost; **halved to 0.25c for a capitulated country**, applied to casualties before and after capitulation (removed if it is freed) |
| Lend-lease | `w = 0.003is − 0.002ir` for equipment IC sent/received, and the same factors per 100 units of fuel |

| Constant | Value |
|---|---|
| WAR_SCORE_PROVINCE_FACTOR | 4.0 |
| VICTORY_POINT_WORTH_FACTOR_WARSCORE | 0.2 |
| PROVINCE_WORTH_FROM_STATE_VALUE_FACTOR_WARSCORE | 0.2 |
| WAR_SCORE_ATTACKER_AND_WINNER_FACTOR | 1.2 |
| WAR_SCORE_LAND_DAMAGE_FACTOR | 0.1 |
| WAR_SCORE_LAND_IC_LOSS_FACTOR | 0.08 |
| WAR_SCORE_AIR_IC_LOSS_FACTOR | 0.08 |
| WAR_SCORE_STRATEGIC_BOMBING_FACTOR | 0.02 |
| WAR_SCORE_STRAT_BOMBING_DECAY_PER_CIVILIAN_FACTORY | 0.1 |
| WAR_SCORE_GAIN_FOR_SUNK_CONVOY | 0.1 |
| WAR_SCORE_GAIN_FOR_SUNK_SHIP_PRODUCTION_COST_FACTOR | 0.1 |
| WAR_SCORE_GAIN_FOR_SUNK_SHIP_MANPOWER_FACTOR | 0.004 |
| WAR_SCORE_LOSSES_RATIO | 0.5 |
| WAR_SCORE_LEND_LEASE_GIVEN_IC_FACTOR | 0.003 |
| WAR_SCORE_LEND_LEASE_RECEIVED_IC_FACTOR | 0.002 |
| WAR_SCORE_LEND_LEASE_GIVEN_FUEL_FACTOR | 0.003 |
| WAR_SCORE_LEND_LEASE_RECEIVED_FUEL_FACTOR | 0.002 |

### Game rules that redistribute war participation

- **Difficulty:** Civilian gives the human player 25% of all AI players' WP points; Recruit gives 10%. (Not achievement-compatible.)
- **Faction Members to Faction Leader** (off by default): 10% of each member's WP to its leader.
- **Redistribute Low Scores** (off by default): WP of AI countries below 5% is divided among countries above 10% (unless none are above 10%). Human players below 5% are exempt.
- **Puppets to Overlord** (on by default): a share of each puppet's WP goes to the overlord:

| Autonomy level | Score % to overlord |
|---|---|
| Nordic Defense Council Member | 50% |
| Collaboration Government, Imperial Protectorate, Integrated Puppet | 20% |
| Supervised State | 15% |
| Austro-Hungarian Vassal, Colony, Imperial Subject, Puppet, Reichskommissariat, Satellite, Volkskommissariat | 10% |
| Dominion, EU Member State, Imperial Associate, Personal Union, Reichsprotectorate | 5% |

The difficulty, puppet and faction rules stack; the low-score rule does not (a low scorer's entire WP is redistributed). Peace score distribution rules are achievement-compatible.

## Peace conference

### Who takes part

The conference opens when the losing side capitulates or conditionally surrenders. The losing side is:

- a single country not in a faction (or whose allies were not in the war), or
- a whole faction once **all its majors have capitulated** (its non-major participants are auto-capitulated; faction members that never joined the war are excluded), or
- winning-faction members that had been occupied by the losers and then had **half or more of their victory points taken by a third-party faction** (historically, Poland).

The winning side is every country that was at war with the loser, even if those winners are at war with each other. On an accepted **conditional surrender**, only the faction leader who received it and its members are on the winning side.

### War score

```
w = s × v × p × c
```
- **s = 1.35** (peace score scale factor from defines)
- **v** = combined state value of all states the enemy controlled at the start of the war
- **p** = the victor's war participation share
- **c** = conditional-surrender factor (the loser's surrender progress at the moment it conditionally surrendered; 1 otherwise)

Distribution rules:
- One victor: **all war score on turn 1**.
- Multiple victors: **20% per turn over five turns**.
- Minimum rate: **5% of the total war score awarded to all countries per turn** — countries below 5% war participation receive at least this until paid out.
- War score cannot be transferred between victors; once fully paid, no further score arrives.

Example: USA (sole victor) vs Cuba, Cuban states worth 120 → 1.35 × 120 × 1.0 = **162**, all on turn 1. Germany/USSR/Lithuania vs Poland (state value 1000, WP 60/36/4%) → 810 / 486 / 54; minimum per turn = 1.35 × 1000 × 0.2 × 0.05 = 13.5, so Lithuania receives 13.5 per turn until its 54 is paid.

### State value

State value = base + manpower + resources + buildings, fixed for the duration of the conference.

- **Base value: 10** per state.
- **Manpower: 1 point per 100,000 population.**
- **Resources:** sum of base resources (building-generated resources such as refinery output excluded).
- **Buildings:** state-category value plus per-building values.

| State category | Value | Building | Value |
|---|---|---|---|
| Wasteland / Enclave / Tiny island | 0 | Civilian factory | 5 |
| Pastoral region / Small island | 4 | Military factory | 8 |
| Rural region | 8 | Naval dockyard | 5 |
| Developed rural region | 16 | Petroleum refinery | 5 |
| Sparse urban region | 20 | Fuel silo | 5 |
| Urban region | 24 | Rocket site | 1 |
| Dense urban region | 32 | Nuclear facility | 10 |
| Metropolis region | 40 | Infrastructure | 1 |
| Megalopolis region | 48 | Air base | 1 |
| | | Anti-air site | 1 |
| | | Radar site | 4 |

Worked example — Rhineland 1936 = **205.5**: base 10 + manpower 61.5 (6,150,000/100,000) + resources 35 (steel) + buildings 99 (Megalopolis 48, 3 military factories 24, 4 civilian factories 20, 4 infrastructure 4, 3 air bases 3).

### Demand types

- **Take State** — annex to the negotiator (or to another victor chosen as beneficiary).
- **Liberate** — hands the state to the scripted core/claim holder, creating the country if needed; its ideology is its original tag's, or its last ideology before occupation.
- **Puppet** — creates or expands a puppet of the negotiator. Democratic negotiators can only create **Supervised States**.
- **Change Government** — creates an independent country with the negotiator's ideology.

With **By Blood Alone**:
- **Take Navy** — takes capital ships (carriers, battleships, heavy cruisers); a proportional share of the loser's screens (light cruisers, destroyers, submarines) comes automatically with each capital ship.
- **Add Demilitarized Zone** — no military forces in that state for five years.
- **Add Resource Rights** — the state's resources go to the negotiator for five years.
- **Add Reparation** — half the state's civilian factories to the negotiator for five years.
- **Add Dismantle Military Industry** — removes the state's military factories.

The last four are only available together with a puppet or change-government demand.

### Turns, contests and refunds

All victors bid simultaneously each turn. Demands that only one victor made are uncontested and effectively granted (until someone contests them later). If two victors demand the **same state (regardless of demand type) or ship**, the demand becomes **contested**: the war score is refunded and the Contested Demands window opens — forfeit and keep the refund, or re-commit it at a higher cost.

**Refund on contest:** full on the first turn of contesting, then **reduced by 8% per additional turn, down to a floor of 76%.**

### Demand costs

`cost = state value × product of all active modifiers`. Cap per demand: **9999 points**. Example: Rhineland (205.5) demanded by democratic France with Ideology 1.3, Influence 0.77, Occupation 0.8 → 0.8 combined → **164.4**.

Generic modifiers:

| Modifier | Effect |
|---|---|
| Influence | 0.7 to 1.0 by pixel distance from your nearest capital (20% weight), core (30%) and controlled state (50%, including states won earlier in this conference). Each directly adjacent controlled state subtracts a further 0.05 (can go below 0.7). Minor countries get 35% less of this discount |
| Contested | Starts at 1.2 when contested, multiplying by 1.2 each further turn, capped at 15 |
| Uncontested | Starts at 1.15 once demanded, growing by ×1.15 plus 0.15 per turn up to 1.6, capped at 15 |

Demand-type-dependent modifiers (Take / Puppet / Force government / Liberate):

| Situation | Take | Puppet | Force | Liberate |
|---|---|---|---|---|
| Core of previous owner ("can be liberated") | 1.05 | 1.05 | 1.05 | — |
| Negotiator occupies state, compliance < 30% | 1.0 | — | — | — |
| Negotiator occupies state, compliance 30–70% | 0.9 | — | — | — |
| Negotiator occupies state, compliance > 70% | 0.8 | — | — | — |
| Loser already puppeted/forced in a previous turn | — | 0.85 | 0.85 | — |
| Core of an independent major on the negotiator's own side | 3 | 3 | 3 | — |
| Negotiator was in a defensive war with the loser | 1.1 | — | 0.95 | 0.95 |
| Claimed by an independent beneficiary | 0.9 | — | — | — |
| Negotiator is Fascist | 0.9 | 0.95 | — | 1.3 |
| Negotiator is Communist | 1.0 | 0.9 | — | 1.3 |
| Negotiator is Democratic | 1.3 | 1.2 | — | 0.9 |
| Negotiator is Democratic and the loser is currently Fascist or Communist | — | — | 0.9 | — |
| Negotiator is a major and the beneficiary; loser is a Democratic or Communist major | 0.8 | 0.8 | 0.8 | 0.8 |
| Negotiator is a democratic major; loser is a major | — | — | 0.7 | — |
| Core of an independent beneficiary | 0.25 | — | — | — |
| Core of a puppeted beneficiary | 0.5 | — | — | — |
| Core of the beneficiary but not of the loser | 0.95 | — | — | — |
| Negotiator occupies the state with compliance > 0 | 0.8 | 0.8 | 0.8 | 0.8 |
| Beneficiary has a dormant national identity (e.g. Ukraine) | — | — | — | 1.25 |
| Not a core of a negotiator who holds an independence war goal against the beneficiary | 1.25 | 1.25 | 1.25 | 1.25 |
| Negotiator was the target of an independence war goal by the loser | 0.5 | — | — | — |

War-goal modifiers:

| War goal held on the loser | Take | Puppet | Force | Liberate |
|---|---|---|---|---|
| Take state | 0.8 | — | — | — |
| Take claimed state | 0.5 | — | — | — |
| Puppet (focus) | — | 0.5 | — | — |
| Take core state | 0.2 | — | — | — |
| Annex everything | 0.5 | — | — | — |
| Civil war | 0.25 | — | — | — |
| Topple government | — | — | 0.5 | — |
| Liberate | — | — | — | 0.5 |
| Independence | 0.5 | — | — | — |

**Take Navy cost** = (capital ship IC × 0.005) + (attached screens' IC × 0.005). Example: a converted-hull carrier (IC ≈ 9000) with 13 destroyers (IC 1000 each) costs 9000 × 0.005 + 13 × 1000 × 0.005 = **110**.

Scripted modifiers exist too — the **Yalta Conference**, if both sides agree, gives western majors −50% on West German states and +400% on East German states (and −50% on liberating Austria), and the Soviet Union the mirror image. These can persist after the conference.

### Tension and after-effects

```
t = 2f × ln(3b + 5v + r + 2) ÷ 20
```
- **f** = 2 annexing a state with no core or claim; 0.5 annexing a claim; 0 annexing a core; 1.25 puppeting; 0.75 changing government
- **b** = civilian factories + military factories + dockyards + rocket sites in the state
- **v** = victory points in the state
- **r** = base resources in the state

Liberating states lowers tension by an amount depending on the negotiator and loser (mostly production buildings) at a factor of −1.0. **Taking ships adds 0.25 tension per capital ship.** DMZ, resource rights, reparations and dismantle-industry demands each generate 0.25 × the state's base threat. All conference tension, positive or negative, is credited to the country the losing faction capitulated to.

Other outcomes: bid-for ships keep **25% of their experience**; defeated countries survive if the victors do not demand all their states; annexed states remain occupied unless they are cores of the new owner, and compliance built up during the war (or via collaboration) carries over; forced-government countries dislike the winners, liberated ones like them.

### AI behaviour

The AI wants: its own cores and claims; states next to states it controls; allies' cores and claims on their behalf; states taken from a different ideology; and demand types matching its ideology (**fascists and non-aligned annex, democracies liberate or force government, communists puppet**).

The AI avoids: cores of countries liberated earlier; contested states; states already demanded; states occupied by a human player; demands benefiting a different ideology; exclaves; states outside its influence (except coastal capitals, a short list of key states — California, Cote Nord, Greater London Area, Tunisia, Suez, Indochina; Gibraltar, Istanbul and Crimea for European takers; and island states); and allies' claims before turn 12. With net desire ≤ 0 it will not bid at all. Puppets bid only on their own cores/claims or for their overlord's. The AI has not been observed demanding ships. Contests lasting beyond two turns are settled by a tiebreaker weighing remaining war score, influence distance and country score equally.

### Strategy

**Inferred / wiki-suggested:**
- Keep unnecessary AI allies out of the war — AI victors are unpredictable in contests and AI puppets waste war score.
- Land combat damage and occupation dominate war participation; naval and air combat are strong for fleets and air forces; **lend-lease has the worst return**.
- Non-democracies should build collaboration before the conference to unlock the compliance cost modifier (typically two collaboration missions).
- Settle the fate of states before buying ships: the war score pool is computed from state value only, so navies, DMZs, reparations and resource rights are paid out of the same budget.
- Against AI contests, hold a demand for at most one or two turns — the refund shrinks 8% per extra turn and the AI eventually digs in.
- Chain the discounts: **Continuous Political Action** makes every later puppet/force-government demand on the same loser 15% cheaper, and **Influence** makes states near what you already hold (including states won earlier this conference) cheaper. Take or puppet a cheap state first, then work outward from cheapest to most expensive.
