---
title: Latvian National Focus Tree
category: focus-trees
tags: [national focus, Latvia, no step back, baltic, political decision trees]
game_version: "1.19"
dlc: [No Step Back]
sources:
  - https://hoi4.paradoxwikis.com/Latvian_national_focus_tree
---

## Summary

Latvia's unique focus tree (requires No Step Back DLC) divides into three main branches: **Suspend the Constitution of Latvia** (governing path), **Formalize the Baltic Entente / Beyond the Baltic** (democratic alliance), and **Empower the Paramilitarists** (fascist), plus **The Threat on Our Border** (military readiness). These interconnect with shared Baltic industrial and communist branches that also appear in Lithuania and Estonia. The tree offers distinct paths to democracy, fascism, or military dictatorship, with options for Baltic unification or alignment with major powers.

See [Latvia](../05-countries/latvia.md) for the country's 1936 starting profile.

## Generic/Continuous focuses

See [National Focus and Continuous Focus](../01-mechanics/national-focus.md) for generic/continuous focuses that all countries share or that unlock after 10 completed focuses.

## Suspend the Constitution of Latvia Branch

This branch determines Latvia's domestic governance under Ulmanis' dictatorship, offering paths toward democracy, military dictatorship, or fascism.

| Focus | Prerequisites | Mutually Exclusive | Effects | Notes |
|---|---|---|---|---|
| **Suspend the Constitution of Latvia** | None | Restore the Worker's Republic | +100 political power; Activates: *Pērkonkrusts Uprising* mission | Initiates domestic governance path |
| **Appease the Democrats** | Suspend the Constitution of Latvia | — | National spirit *The Saeima*: +10% stability, +10% war support, +0.10 daily democracy support | Guides toward democratic restoration |
| **Renew Kviesis' Term** | Appease the Democrats | A Martial Prime Minister | +15% political power gain; +0.10 daily democracy support, +0.10 daily unaligned support; −10% political advisor cost; replaces *The Saeima* with *Democratic Saeima*: +10% stability, +10% war support, +0.20 daily democracy support | Consolidates democratic opposition control |
| **Restore the Saeima** | Renew Kviesis' Term | — | +100 political power; if *Farmer's Party* not present, modifies *Democratic Saeima* to: +15% stability, +15% war support, +0.30 daily democracy support | Reinstates advisory parliament |
| **Latvian Socialism** | Restore the Saeima | — | Every owned cored state: +1 infrastructure; Two random owned controlled states: each gets +1 building slot, +1 civilian factory | Economic concessions to socialist movement |
| **State Capitalism** | Renew Kviesis' Term + Establish the Chambers of Professions | — | Changes trade law to Free Trade: +15% construction speed, +10% research speed, +15% factory output, +15% dockyard output, +80% resources to market, +40% civilian intel to others, +20% navy intel to others; national spirit *State Capitalism*: +10% construction speed, +5% production efficiency growth, +5% production efficiency base | Corporatist economic model |
| **Establish the Chambers of Professions** | Renew Kviesis' Term OR A Martial Prime Minister | — | National spirit *Chamber of Professions*: −5% consumer goods factories | Professional-sector representation |
| **A Martial Prime Minister** | Appease the Democrats | Renew Kviesis' Term | Jānis Balodis available as political advisor: +10% army experience gain, +20 max command power, +10% daily command power gain, −15% high command cost; replaces *The Saeima* with *Authoritarian Saeima*: +0.02 daily army experience, +5% stability, +5% war support, +0.10 daily unaligned support | Empowers military influence |
| **Renew the Constitution of Latvia** | Latvian Socialism + State Capitalism + >45% democracy support | Integrate the Farmer's Party | LDSP becomes ruling party; elections held every 4 years; Fricis Menders leads democracy party; loses *Low Democratic Opposition*; +10% democracy popularity | Restores democratic republic |
| **Integrate the Farmer's Party** | Latvian Socialism + State Capitalism | Renew the Constitution of Latvia | Loses *Low Democratic Opposition*; national spirit *The Farmer's Party* (if had *Democratic Saeima*), or acquires it; −20% join faction tension limit; +85 acceptance of democratic diplomacy; +0.10 daily unaligned support | Authoritarian democratic consolidation |
| **Nationalised Industry** | Establish the Chambers of Professions + A Martial Prime Minister | — | Increases economy law; national spirit *Nationalised Industry*: −25% economy law cost, −25% trade law cost | State control of key industries |
| **Improve Military Life** | A Martial Prime Minister | — | Replaces *Authoritarian Saeima* with *Military Saeima*: +0.02 daily army experience, +5% stability, +5% war support, +0.20 daily unaligned support | Strengthens military political base |
| **A Military Diarchy** | Improve Military Life | — | Modifies *Military Saeima* to: +0.05 daily army experience, +5% stability, +10% war support, +0.30 daily unaligned support | Balodis and Ulmanis share power formally |
| **Merge the Presidential Titles** | Nationalised Industry | A Military Dictatorship | If Ulmanis is leader: +10% stability, +10% war support, +0.10 daily unaligned support; if fascist ruling party: Military Dictator bonuses (+0.20 daily unaligned support, −10% conscription cost); loses *Democratic Opposition* | Consolidates civilian dictatorship |
| **A Military Dictatorship** | A Military Diarchy + not fascist | Merge the Presidential Titles | Jānis Balodis becomes non-aligned leader; Latvian Militant: +10% war support, +10% daily command power gain; −10% conscription cost; modifies *Military Saeima* to: +0.05 daily army experience, +10% stability, +20% war support, +0.30 daily unaligned support, −25% conscription cost; becomes *Latvian Military Directorate* (unless already Baltic Federation/Ostland); loses *Democratic Opposition*; Ulmanis available as advisor: +10% stability, +10% war support, +0.10 daily unaligned support | Establishes pure military rule |

## Formalize the Baltic Entente / Beyond the Baltic Sub-branch

Democratic alliance and Nordic cooperation paths, unlocked after settling the Saeima question.

| Focus | Prerequisites | Mutually Exclusive | Requirements | Effects | Notes |
|---|---|---|---|---|---|
| **Formalize the Baltic Entente** | One of: Renew Constitution / Integrate Farmer's Party / Merge Titles / Military Dictatorship | Beyond the Baltic | Fully independent, not in faction; at least one Baltic ally (Estonia/Lithuania) exists and not in faction; allies must not have completed this focus; bypasses if already in faction with Estonia or Lithuania | If Estonia/Lithuania exists and not in faction: sends *Latvia Seeks Baltic Cooperation* event; unlocks decisions *Formalize the Baltic Entente*, *Abandon the Entente* | Initiates Baltic bloc formation |
| **The Baltic Economic Union** | Renew Constitution + Formalize Baltic Entente; faction leader | — | — | +1 offmap civilian factory; Latvia and all Baltic faction members: national spirit *Baltic Economic Pact*: −2.5% consumer goods factories, +5% factory output | Economic integration layer |
| **Look North** | Formalize Baltic Entente + agreed to entente + faction leader; one of Nordic states (Norway/Sweden/Finland/Denmark) not in faction | — | — | Sends *Latvia Seeks Baltic Cooperation* event to Nordic nations (or *The Lone Wolf* block check for Finland) | Scandinavian expansion attempt |
| **The Pan-Baltic Bank** | Baltic Economic Union; faction leader | — | — | Latvia and all Baltic members modify *Baltic Economic Pact* to: −5% consumer goods factories, +10% factory output | Monetary union |
| **Baltic Defense Army** | Baltic Economic Union; faction leader | — | — | +1 offmap military factory; Latvia and all Baltic members: national spirit *Baltic Defense Army*: +30% recruitable population factor, −10% training time | Unified military command |
| **Propose a Baltic Union** | Pan-Baltic Bank + Baltic Defense Army; faction leader | — | — | Latvia and all Baltic members lose *Baltic Defense Army* and *Baltic Economic Pact*; gain national spirit *The Baltic Union*: +30% recruitable population factor, −7.5% consumer goods factories, +15% factory output, −15% training time | Complete political union |
| **Baltic Unification** | Propose Baltic Union | United but Separate | Faction leader | Every Baltic member in faction with Latvia: annexes them; every Baltic nation outside faction: gains annexation war goal | Political consolidation into single state |
| **United but Separate** | Propose Baltic Union | Baltic Unification | Faction leader | Latvia and Baltic members modify *Baltic Union* to: +3% recruitable population, +30% recruitable population factor, −10% consumer goods factories, +20% factory output, −20% training time; 4 units with 9 infantry battalions created in random owned state per Baltic ally; non-faction Baltic states: gain topple-government war goals | Military alliance without merger |
| **Beyond the Baltic** | One of: Renew Constitution / Integrate Farmer's Party / Merge Titles / Military Dictatorship | Formalize Baltic Entente | Fully independent; any major democratic nation at peace with Latvia exists not in UK faction; must be or become faction leader for bypass; bypasses if already in Allied faction with UK or any major democratic faction leader | If UK is democratic faction leader at peace with Latvia: UK gets *Latvia Seeks Guarantees* event; otherwise most qualified democratic faction leader gets the event | Seeks Allied protection |
| **Join the Allies** | Beyond the Baltic + fully independent + not in faction; major democratic leader (UK) at peace and not in faction with Latvia; faction leader prerequisite or bypass | — | — | If UK is democratic leader at peace with Latvia: UK gets *Latvia Seeks to Join the Allies* event; otherwise most qualified democratic faction leader gets event | Formalizes Allied alliance |

## Empower the Paramilitarists Sub-branch

Fascist and nationalist paramilitaries path, enabling multiple branching routes.

| Focus | Prerequisites | Mutually Exclusive | Requirements | Effects | Notes |
|---|---|---|---|---|---|
| **Empower the Paramilitarists** | Suspend the Constitution of Latvia | — | — | National spirit *Latvian Paramilitarists*: +10% recruitable population factor | Opens paramilitary track |
| **The Sun Shines Equally** | Empower Paramilitarists | Latvia for Latvians | — | −10% fascism popularity; modifies *Pērkonkrusts* to: −10% recruitable population factor, −10% stability, −5% land doctrine cost, +0.05 daily fascism support, +25% conscription cost; national spirit *The Sun Shines Equally*: +5% recruitable population factor, +10% stability, −0.10 daily fascism support | Anti-fascist democratic path |
| **Banish Celmiņš** | The Sun Shines Equally; <10% fascism support | — | — | Removes *Pērkonkrusts Uprising* mission; loses *Përkonkrusts* spirit; −10% fascism popularity | Crushes ultranationalist threat |
| **Fund the Aizsargi** | Banish Celmiņš | — | — | Replaces *Latvian Paramilitarists* with *Patriotic Paramilitaries*: +20% recruitable population factor | Supports government paramilitaries |
| **Expand the Women's Aizsargi** | Fund Aizsargi | — | — | Modifies *Patriotic Paramilitaries* to: +20% recruitable population factor, −2.5% consumer goods factories, +10% factory output | Gender-inclusive militarization |
| **The Forest Brothers** | Fund Aizsargi OR Anti-German Propaganda | — | — | National spirit *Forest Brothers*: +10% division attack on core, +10% division defense on core | Anti-Soviet guerrilla support |
| **A Multicultural Latvia** | Expand Women's Aizsargi + Forest Brothers | — | — | National spirit *A Multicultural Latvia*: +5% division attack on core, +5% division defense on core | Diversity in defense |
| **Latvia for Latvians** | Empower Paramilitarists | The Sun Shines Equally | >10% fascism support | +10% fascism popularity; unlocks *Fight the Përkonkrusts* decisions (must keep Përkonkrusts <55% to avoid civil war) | Opens ultranationalist track |
| **Lift the Ban on Pērkonkrusts** | Latvia for Latvians; >10% fascism support | — | — | +5% fascism popularity; modifies *Përkonkrusts* to: −10% recruitable population factor, −25% stability, −5% land doctrine cost, +0.15 daily fascism support, +25% conscription cost; Gustavs Celmiņš available as advisor: +7.5% division attack on core, +7.5% division defense on core, +0.15 daily fascism support | Legalizes fascist party |
| **Recruit Fanatics** | Latvia for Latvians; >10% fascism support | — | — | +5% fascism popularity; replaces *Latvian Paramilitarists* with *Fascist Paramilitaries*: +1% recruitable population, +20% recruitable population factor | Fascist militia integration |
| **Latvian Military Complex** | Lift Ban + Recruit Fanatics; >20% fascism support | — | — | +5% fascism popularity; three random owned controlled states: each gains +1 building slot (+1 civilian factory, +1 military factory, or +1 military factory); national spirit *Latvian Militarism*: +10% military factory construction speed | Intensive militarization |
| **The Old Ways** | Lift Ban + Recruit Fanatics; >35% fascism support | — | — | +5% fascism popularity; national spirit *Dievturība* (revival of ancient Baltic faith): +10% war support, +0.10 daily fascism support | Pagan nationalist identity |
| **Anti-German Propaganda** | Latvian Military Complex OR The Old Ways | Seek Alignment with Germany / The Thunder Roars Alone | >50% fascism support; not fascist ruling party | Removes *Përkonkrusts Uprising* mission; −20% fascism popularity; replaces *Përkonkrusts* with *Anti-German Propaganda*: +10% recruitable population factor, +10% war support, −0.10 daily fascism support | Independent fascist stance |
| **Seek Alignment with Germany** | Latvian Military Complex OR The Old Ways | Anti-German Propaganda / The Thunder Roars Alone | >40% fascism support; at peace with Germany; fully independent; not in faction; Germany not in faction (check via Hungary at peace); fascist ruling party; fully independent; not democratic | Përkonkrusts becomes ruling party; elections stop; +15% fascism popularity; removes *Përkonkrusts Uprising* mission; loses *Përkonkrusts* spirit; if Germany exists, not capitulated, fascist, and faction leader: Germany gets *Latvia Seeks to Join the Axis* event; otherwise most qualified fascist faction leader gets event | Joins Axis |
| **The Thunder Roars Alone** | Latvian Military Complex + The Old Ways | Anti-German Propaganda / Seek Alignment with Germany | >40% fascism support; fully independent; not democratic | Përkonkrusts becomes ruling party; elections stop; +15% fascism popularity; removes *Përkonkrusts Uprising* mission; loses *Përkonkrusts* spirit; Germany less likely to allow faction entry | Independent fascist state |
| **Free the Ugunskrusts** | Seek Alignment with Germany OR The Thunder Roars Alone; fascist ruling party | — | — | 6 militia divisions created in random owned controlled state | Mobilizes fascist base |
| **Support Baltic Fascists** | Free Ugunskrusts | The Lightning Strikes | Not already fascist (Lithuania/Estonia); must exist and be independent; bypasses if already fascist, doesn't exist, or is subject | If Estonia/Lithuania not fascist: sends *Latvia Supports Estonian/Lithuanian Nationalism* events; unlocks *Promote Baltic Fascism* decisions | Spreads fascism to neighbors |
| **The Lightning Strikes** | Free Ugunskrusts | Support Baltic Fascists | Lithuania/Estonia exist, fully independent, not in faction with Latvia (one must be true) | If Lithuania/Estonia not subject: sends *Latvia Demands Lithuanian/Estonian Annexation* event; otherwise gains claims on cored states and annexation war goals against them | Conquers Baltic neighbors |
| **Consecrate the Brotherhood** | Support Baltic Fascists; fully independent; faction leader or not in faction; Lithuania/Estonia fascist or doesn't exist or is subject (at least one true per nation); bypasses if either nation doesn't exist or is subject | — | — | Set rule: can create factions; if not in faction and (NSB DLC enabled: create *Baltic Brotherhood* faction with 1 initiative point; else create faction); if Estonia/Lithuania fascist: sends invitation event; else gains puppet war goals | Creates fascist Baltic bloc |
| **Reorganize the Forest Brothers** | Seek Alignment with Germany OR The Thunder Roars Alone | — | — | National spirit *Reorganized Forest Brothers*: +10% division attack on core, +10% division defense on core, +0.05 daily fascism support | Realigns guerrillas to fascist cause |
| **Diev's Keepers** | Seek Alignment or Thunder Roars Alone; has *Dievturība* | — | — | Modifies *Dievturība* to: +10% political power gain, +5% attack, +5% defense, +10% war support, +0.15 daily fascism support | Militarizes pagan faith |
| **State Paganism** | The Thunder Roars Alone + Diev's Keepers; has *Dievturība* | — | — | Modifies *Dievturība* to: +10% political power gain, +10% division organization, +5% attack, +5% defense, +10% war support, +0.15 daily fascism support | Dievturība becomes state religion |
| **The Wrath of the Old Gods** | State Paganism; has *Dievturība* | — | — | Modifies *Dievturība* to: +10% political power gain, +10% division organization, +5% attack, +5% defense, +10% division recovery rate, +10% war support, −40% generate war goal tension limit, −25% justify war goal time, +0.15 daily fascism support | Anti-Christian crusade ideology |
| **Ostland** | Support Baltic Fascists OR The Lightning Strikes | A United Baltic Empire | In faction with or subject of Germany | Becomes *Ostland*; gains cores on all Estonia/Lithuania states (11 total) and 4 eastern Polish states (Wilno, Wilejka, Nowogródek, Polesie); if Lithuania/Estonia in faction with Latvia: sends *Latvia Seeks Baltic Unification* event; if other faction members control all Baltic+ states, Germany gets *Kārlis Ulmanis Seeks Ostland Unification* event (acceptance annexes Baltic nations and Latvia controls Polish states) | German-aligned Baltic state |
| **A United Baltic Empire** | Support Baltic Fascists OR The Lightning Strikes | Ostland | Not Baltic Federation yet; controls all Estonia/Lithuania states OR (those nations fascist or subject); bypasses if Baltic Federation formed | Latvian Military Directorate becomes *Baltic Assembly* (if conditions met); gains cores on all Estonia/Lithuania states (11 total) and 4 eastern Polish states; if Lithuania/Estonia in faction: sends *Latvia Seeks Baltic Unification* event; annexation takes effect if accepted | Independent Baltic empire |
| **Avenge the Ancestors** | A United Baltic Empire + State Paganism; major power; fascist ruling party; fully independent | — | — | Gains puppet war goals against Germany, Sweden, Denmark, Finland | Launches expansionist crusade |

## The Threat on Our Border Sub-branch

Resistance and government-in-exile preparedness, unlocking after achieving *The Forest Brothers* focus and resolving the Saeima question.

| Focus | Prerequisites | Mutually Exclusive | Requirements | Effects | Notes |
|---|---|---|---|---|---|
| **The Threat on Our Border** | The Forest Brothers; one of: Renew Constitution / Integrate Farmer's Party / Merge Titles / Military Dictatorship; one true: not in Soviet faction OR not in German faction; bypasses if in Soviet or German faction | — | — | Gets event *The True Enemy* | Prompts war preparation decision |
| **Cave to Enemy Pressure** | The Threat on Our Border | Prepare for the Inevitable | Not in faction | In event enemy invades, can choose to become subject instead of fighting | Appeasement/capitulation path |
| **Prepare for the Inevitable** | The Threat on Our Border | Cave to Enemy Pressure | Must have capitulated | +2 offmap military factories, +2 offmap civilian factories | Government-in-exile preparation |
| **Prepare an Industrial Resistance** | Prepare for the Inevitable; capitulated | — | — | National spirit *Influx of Exiles*: +700 weekly exiled-government manpower; +4 offmap military factories | Exiled military production |
| **Prepare a Covert Resistance** | Prepare for the Inevitable; capitulated | — | — | If *La Résistance* DLC enabled: +1 random agency upgrade, +3 offmap civilian factories; else: 2× 75% electronics research bonus | Underground intelligence operations |

## Shared Baltic Branches

The wiki documents two additional branches that are shared with Lithuania and Estonia:

- **Rejoin the Railways Branch**: Industrial upgrades for the Baltic region; details linked from Estonian focus tree (shared industrial branch).
- **Restore the Worker's Republic Branch**: Communist path, allows conversion to Soviet puppet or independence; also shared with Estonia and Lithuania; enables expansion to Scandinavia.

Refer to the equivalent Estonian or Lithuanian focus tree files for details on these shared branches.

## Notes

- The tree's core branching point occurs at **Suspend the Constitution of Latvia** (vs. the communist path).
- Multiple focus prerequisites/blocks demand resolving the Saeima question first (Renew Constitution, Integrate Farmer's Party, Merge Titles, or Military Dictatorship).
- **Fascist path** supports internal paramilitaries (*Përkonkrusts*), requiring >10% fascism support to unlock later focuses; player can keep party <55% to avoid civil war or allow it.
- **Baltic unity options**: Democratic path offers entente/union with bonus factories; fascist path offers Baltic Brotherhood faction or forced annexation.
- **Resistance focuses** require capitulation and allow government-in-exile with offmap factory bonuses.
- **Dievturība** (ancient Baltic faith) modifiers stack across *The Old Ways*, *Diev's Keepers*, and *State Paganism* focuses, each adding layers to war support, political power gain, and fascism support.
- The forest brothers can be either patriotic resistors (democratic path) or reorganized fascist militia (fascist path).
