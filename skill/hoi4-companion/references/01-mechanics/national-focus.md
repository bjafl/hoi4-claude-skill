---
title: National Focus and Continuous Focus
category: mechanics
tags: [national focus, focus tree, continuous focus, generic focus tree, political power, shared focus, joint focus]
game_version: "1.19"
dlc: []
sources:
  - https://hoi4.paradoxwikis.com/National_focus
  - https://hoi4.paradoxwikis.com/Continuous_focus
  - https://hoi4.paradoxwikis.com/Generic_national_focus_tree
---

## Summary

A focus tree is the main way a country directs its development. Only one focus (regular or continuous) can run at a time; a focus costs **1 political power per day for its whole duration**, so the standard 70-day focus costs 70 PP and a 35-day focus costs 35 PP. Countries without a unique tree use the generic tree. Continuous focuses unlock after 10 completed focuses and give ongoing bonuses for −1 PP/day.

## Focus mechanics

- **One at a time.** Regular and continuous focuses share the single slot.
- **Duration and cost.** Progress is 1 day per day and drains **1 PP per day**: a 70-day focus needs 70 PP total, a 35-day focus 35 PP.
- **Carry-over.** After completing a focus you may wait up to **10 days** before picking the next one and still count those days (and their PP) toward the new focus.
- **Stopping.** A running focus can be stopped manually unless explicitly prohibited; at most **10 days of progress is banked**. If a focus is invalidated, PP already spent is lost.
- **Invalidated prerequisites.** If a requirement of a running focus breaks, the focus pauses until it is restored, or is cancelled outright when restoration is not possible.
- **Bypass.** Focuses can carry bypass conditions; when met the focus auto-completes within a few days and shows a golden bracket. Example: *Motorization Effort* is bypassed if Motorized Infantry is already researched.
- **Historical AI.** The "Historical AI Focuses" option on the country-selection screen makes the AI follow historical branches; human players are never bound by it.
- **Focus speed modifiers:** _Not covered on the wiki._ The wiki documents no generic modifier that speeds up focus completion — only fixed per-focus durations and the 1 PP/day drain.

### Reading the tree

| Indicator | Meaning |
|---|---|
| Grey name bracket | Available to pick |
| Brown name bracket | Not yet available |
| Golden name bracket | Completed (or bypassed) |
| Shining overlay | Currently in progress |
| Green connection line | Preceding focus is complete |
| Light-blue connection line | Preceding focus is not complete |
| Solid line | Logical AND — all connected parents required |
| Dotted line | Logical OR — any one connected parent suffices |
| Mutually exclusive icon between two focuses | Only one of the two may ever be taken; everything downstream of the rejected one is also locked out unless re-joined by an OR connection |

Example of AND: *Special Forces* requires all three of its parents. Example of OR: *Technology Sharing* requires only one of its two parents. Example of mutual exclusion: picking *Collectivist Ethos* or *Liberty Ethos* locks the other side's chain until they re-converge at *Technology Sharing*.

Hovering or clicking a focus shows flavour text, requirements, bypass conditions and completion effects.

## Continuous focuses

- Unlocked after **10 regular focuses** have been completed; **9 continuous focuses** exist in total.
- Upkeep: **−1 PP per day** while active; deactivating or switching is free and instant.
- Effects last only while the focus is active (unlike regular focuses' one-off effects).
- The control panel sits at the bottom-left of the focus tree; the LEDs at its top-right show how many more regular focuses are needed to unlock the mechanic.

### Unconditioned continuous focuses

| Focus | Effect |
|---|---|
| Air Production | Production cost −10% for: carrier CAS, carrier fighter, carrier naval bomber, close air support, fighter, guided missile, heavy fighter, jet fighter, jet strategic bomber, jet tactical bomber, naval bomber, rocket interceptor, scout plane, strategic bomber, tactical bomber, transport plane |
| Army Training | Division training time −25% |
| Construction Engineering | Construction speed +20% for anti-air, coastal fort, land fort, radar station; +10% for air base, fuel silo, infrastructure, naval base, railway, rocket site, supply hub, nuclear reactor, heavy water nuclear reactor, civilian nuclear reactor (machine-tool-limited buildings such as factories are excluded) |
| Construction Repair | Factory repair speed +50% |
| Naval Production | Dockyard output +20% |
| Resistance Suppression | Resistance target −5% |

### Conditional continuous focuses

| Focus | Prerequisite | Effect |
|---|---|---|
| Increase Autonomy | Is a subject nation | Daily autonomy progress gain +0.5 |
| Suppress Subjects | Has a subject nation | Autonomy in subjects −0.5 |
| Technology Sharing | In a faction with at least 2 members; not already in a technology sharing group | Joins/creates a faction research group: research speed +10% for every nation owning the tech |

### Country-specific continuous focuses

| Focus | Requirements | Effect |
|---|---|---|
| Strengthen the Black Lions (requires By Blood Alone) | Is/was Ethiopia; completed *Anti-Italian Propaganda*; and one of: is a government in exile, leader has the *Imperator Absentis* trait, or an owned state is not controlled by Ethiopia | Compliance growth speed in our states occupied by the enemy −10% |
| Supporting the Arbegnoch (requires By Blood Alone) | Is/was Ethiopia; completed *The Patriots*; same additional condition as above | Resistance growth speed in our states occupied by the enemy +10% |
| Build up Military Readiness (requires By Blood Alone) | Is/was Switzerland; completed *Armed Neutrality* | Activates the "Building up Military Readiness" mission |
| Support Active Militias (requires By Blood Alone) | Is/was Switzerland; has the *Citizen Militias Deployed* modifier | Militia attack +30%, defense +30%, speed +30%, organization +15% |
| Undermine Overlord Influence (requires Arms Against Tyranny) | Is/was Denmark; is a subject; *Overlord Influence* is active | Weekly balance of power change +1.00% |

## The generic focus tree

All nations lacking a unique tree use the generic tree — including nations whose unique tree comes from a DLC that is not enabled. Five branches:

| Branch | Purpose |
|---|---|
| Army Effort | Army experience and army research bonuses |
| Aviation Effort | Air experience, air bases, air research bonuses |
| Naval Effort | Navy experience, dockyards, naval research bonuses |
| Industrial Effort | Civilian/military factories (usually granted even with no free building slots), infrastructure, extra research slots |
| Political Effort | Chooses the country's political path |

### Army Effort branch

| Focus | Prerequisites | Effects |
|---|---|---|
| Army Effort | None | Army experience +25; 1× 50% cost reduction for Land Doctrine |
| Equipment Effort | Army Effort | Land Warfare breakthrough progress +10.00%; 1× 100% research bonus for Infantry Weapons and Support Artillery |
| Equipment Effort II | Equipment Effort | Land Warfare breakthrough progress +10.00%; 1× 100% research bonus for Infantry Weapons and Support Artillery |
| Equipment Effort III | Equipment Effort II | Land Warfare breakthrough progress +10.00%; 1× 2.0 years ahead-of-time penalty reduction for Infantry Weapons and Support Artillery |
| Motorization Effort | Army Effort | 1× 100% research bonus for Truck |
| Mechanization Effort | Motorization Effort | 1× 2.0 years ahead-of-time reduction for Truck; if Truck is researched, 1 unit of Truck added to the stockpile |
| Armor Effort | Mechanization Effort | 2× 100% research bonus for Armor technology |
| Doctrine Effort | Army Effort | Army experience +25; 1× 50% cost reduction for Land Doctrine |
| Doctrine Effort II | Doctrine Effort | Army experience +25; 1× 50% cost reduction for Land Doctrine |
| Special Forces | Equipment Effort III **and** Doctrine Effort II **and** Armor Effort | 1× 100% research bonus for Paratroopers I–II, Marines I–II, Mountaineers I–II; grants the national spirit **Special Forces** (special forces capacity multiplier +2.0%) |

### Aviation Effort branch

| Focus | Prerequisites | Effects |
|---|---|---|
| Aviation Effort | None | Air experience +25; adds 2 air bases in the capital or a random owned controlled state; 1× 50% cost reduction for Air Doctrine |
| Fighter Focus | Aviation Effort (mutually exclusive with Bomber Focus) | 2× 100% research bonus for Interwar Fighter, Fighter I–III, Heavy Fighter I–III |
| Bomber Focus | Aviation Effort (mutually exclusive with Fighter Focus) | 2× 100% research bonus for Strategic Bomber and Tactical Bomber models |
| Aviation Effort II | Bomber Focus **or** Fighter Focus | Air experience +25; adds 2 air bases in the capital or a random owned controlled state; 1× 50% cost reduction for Air Doctrine |
| CAS Effort | Aviation Effort II **and** Motorization Effort | Next 1 research of Close Air Support models: −2.0 years ahead-of-time penalty and 100% research bonus |
| NAV Effort | Aviation Effort II **and** Flexible Navy | Next 1 research of Naval Bomber models: −2.0 years ahead-of-time penalty and 100% research bonus |
| Rocket Effort | Infrastructure Effort **and** Aviation Effort II | Aerodynamics and Avionics breakthrough +50.00%; 1× 2.0 years ahead-of-time reduction for Jet and Rocketry technology |

### Naval Effort branch

| Focus | Prerequisites | Effects |
|---|---|---|
| Naval Effort | Any controlled state is coastal | Navy experience +25; random owned controlled state gets 3 building slots and 3 naval dockyards |
| Flexible Navy | Naval Effort (mutually exclusive with Large Navy) | +10.00% mastery for 240 days on all active Trade Interdiction and Base Strike tracks; 2× 50% cost reduction for Naval Doctrine |
| Large Navy | Naval Effort (mutually exclusive with Flexible Navy) | +10.00% mastery for 240 days on all active Fleet in Being and Base Strike tracks; 2× 25% cost reduction for Naval Doctrine |
| Submarine Effort | Flexible Navy **or** Large Navy | Next 1 research of Submarine models: −2.0 years ahead-of-time penalty and 100% research bonus |
| Destroyer Effort | Submarine Effort | Next 1 research of Destroyer models: −2.0 years ahead-of-time penalty and 100% research bonus |
| Cruiser Effort | Flexible Navy **or** Large Navy | Next 1 research of Cruiser models: −2.0 years ahead-of-time penalty and 100% research bonus |
| Capital Ship Effort | Cruiser Effort | Navy experience +25; next 1 research of Battlecruiser, Battleship and Carrier models: −2.0 years ahead-of-time penalty and 100% research bonus |

### Industrial Effort branch

| Focus | Prerequisites | Effects |
|---|---|---|
| Industrial Effort | None | 1× 100% research bonus for Industry |
| Construction Effort | Industrial Effort (bypassed if no building slots are available anywhere, including locked slots) | Random owned controlled state: +1 building slot, +1 civilian factory |
| Construction Effort II | Construction Effort (same bypass) | Random owned controlled state: +1 building slot, +1 civilian factory |
| Infrastructure Effort | Construction Effort II (bypassed if no infrastructure slots are available) | +1 infrastructure in one random owned controlled state and +2 in another |
| Infrastructure Effort II | Infrastructure Effort (same bypass) | +1 infrastructure in one random owned controlled state and +2 in another |
| Construction Effort III | Infrastructure Effort (bypassed if no building slots available) | Random owned controlled state: +2 building slots, +2 civilian factories |
| Extra Research Slot | Infrastructure Effort II | +1 research slot |
| Extra Research Slot II | Extra Research Slot **and** more than 50 factories | +1 research slot |
| Nuclear Effort | Infrastructure Effort II | Nuclear Research breakthrough +75.00%; 1× 1.0 year ahead-of-time reduction for Nuclear technology |
| Secret Weapons | Infrastructure Effort II | Grants the national spirit **Secret Weapons Initiatives** (special project speed +5.00%) |
| Armament Effort | Industrial Effort (bypassed if no building slots) | Random owned controlled state: +1 building slot, +1 military factory |
| Armament Effort II | Armament Effort (same bypass) | Random owned controlled state: +1 building slot, +1 military factory |
| Armament Effort III | Armament Effort II (same bypass) | Random owned controlled state: +1 building slot, +1 military factory |

### Political Effort branch

| Focus | Prerequisites | Effects |
|---|---|---|
| Political Effort | None | Political power +120 |
| Collectivist Ethos | Political Effort; ruling party is fascist, communist or non-aligned (mutually exclusive with Liberty Ethos) | National spirit **Collectivist Ethos** for 1095 days: daily democracy support −0.02 |
| Nationalism Focus | Collectivist Ethos; ruling party is fascist or non-aligned (mutually exclusive with Internationalism Focus) | National spirit **Nationalism** for 720 days: daily fascism support +0.10 |
| Militarism | Nationalism Focus | Removes Neutral Foreign Policy; national spirit **Militarism** (recruitable population +2.00%, damage to garrisons −10.00%); army experience +20; sets rule: can send volunteer forces |
| Military Youth | Militarism | National spirit **Military Youth** (mobilization speed +25.00%, recruitable population +1.00%); if ruling party is fascist: fascism popularity +20.00%; if communist: communism popularity +20.00% |
| Paramilitarism | Military Youth | National spirit **Paramilitarism** (division training time −10.0%, supply combat penalties on core territory −15.0%) |
| Internationalism Focus | Collectivist Ethos; ruling party is communist or non-aligned (China must be communist) (mutually exclusive with Nationalism Focus) | National spirit **Internationalism** for 720 days: daily communism support +0.10 |
| Political Correctness | Internationalism Focus | Removes Neutral Foreign Policy; political power +200; national spirit **Political Correctness** (foreign subversive activities efficiency −75%) |
| Indoctrination | Political Correctness | Political power +150; national spirit **Indoctrination** (weekly manpower +400, stability +5.00%) |
| Political Commissars | Indoctrination | Political power +200; national spirit **Political Commissars** (division recovery rate +10.0%); if fascist: fascism popularity +20.00%; if communist: communism popularity +20.00% |
| Ideological Fanaticism | Paramilitarism **or** Political Commissars | National spirit **Ideological Fanaticism** (war support +5.00%, division attack on core territory +10%, division defense on core territory +10%); sets rule: can create factions; allows kamikaze strikes |
| Liberty Ethos | Political Effort; ruling party is democratic or non-aligned (mutually exclusive with Collectivist Ethos) | National spirit **Liberty Ethos** (trade deal opinion factor +20.00%) |
| Neutrality Focus | Liberty Ethos (mutually exclusive with Interventionism Focus) | National spirit **Neutral Foreign Policy** (join faction tension limit +100.0%, send volunteers tension limit +20.0%, guarantee tension limit +100.0%, embargo tension limit +250.0%, AI desire to be in/expand a faction −100, AI threat receptivity +1.0%); political power +150 |
| Deterrence | Neutrality Focus | National spirit **Deterrence** (land fort, coastal fort, anti-air and military factory construction speed +20.00% each) |
| Interventionism Focus | Liberty Ethos (mutually exclusive with Neutrality Focus) | Removes Neutral Foreign Policy; sets rule: can send volunteer forces; political power +150 |
| Volunteer Corps | Interventionism Focus | National spirit **Volunteer Corps** (divisions required for sending volunteer force −25.0%) |
| Foreign Expeditions | Volunteer Corps | National spirit **Foreign Expeditions** (divisions required for sending volunteer force −50.0%) |
| Why We Fight | Deterrence **or** Foreign Expeditions **or** more than 75% world tension **or** in a defensive war | National spirit **Why We Fight** (stability +10.00%, war support +10.00%); if it does not have Neutral Foreign Policy, sets rule: can create factions |
| Technology Sharing | Ideological Fanaticism **or** Why We Fight; in a faction; at war; and either more than 50 factories or an ally in the faction with more than 50 factories | If the country started with fewer than 3 research slots: +1 research slot. Otherwise: Aerodynamics and Avionics breakthrough +25.00%, Nuclear Research breakthrough +25.00%, 1× 100% research bonus each for Electronics, Industry, and Infantry Weapons and Support Artillery |

## Which countries have unique trees

The seven great powers plus Poland and Finland have unique trees in the base game; other unique trees ship with DLC. If the relevant DLC is off, the country falls back to the generic tree.

| Source | Countries with a unique tree |
|---|---|
| Base game — majors | France, Germany (industrial/historical and opposition branches), Italy, Japan, Poland, Soviet Union (industrial and political branches), United Kingdom, United States |
| Base game — Commonwealth | Australia, British Raj, Canada, New Zealand, South Africa |
| Base game — Europe | Czechoslovakia, Hungary, Romania, Yugoslavia |
| Base game — China | China, Chinese Soviet Republic, Manchukuo, Warlords (Guangxi Clique, Shanxi, Sinkiang, Xibei San Ma, Yunnan), plus the shared Chinese branches |
| Base game — other | Mexico, Netherlands |
| La Résistance | Free France, Vichy France, Portugal, Nationalist Spain, Republican Spain |
| Battle for the Bosporus | Bulgaria, Greece, Turkey |
| No Step Back | Estonia, Latvia, Lithuania (+ shared Baltic branches) |
| By Blood Alone | Ethiopia, Switzerland, Horn of Africa nations (Aussa, Benishangul-Gumuz, Gambela, Harar, Oromia, Qemant, Sidamo, Tigray) |
| Arms Against Tyranny | Denmark, Finland, Iceland, Norway, Sweden (+ Joint Nordic branches) |
| Trial of Allegiance | Argentina, Brazil, Chile, Paraguay, Uruguay (+ shared military branches, + Paraguay/Uruguay shared) |
| Götterdämmerung | Austria, Belgian Congo, Belgium, Hungary (+ Joint Congo, + Joint Austro-Hungarian) |
| Graveyard of Empires | Afghanistan, British Raj, Iran, Iraq (+ Joint Saadabad Pact) |
| No Compromise, No Surrender | China, Chinese Soviet Republic, Manchukuo, Philippines, the fourteen warlord tags (+ Nationalist/Communist Warlord, Joint Liangguang Incident, Joint Ma Clique, shared Chinese) |
| Peace for Our Time | Czechoslovakia |
| Thunder at Our Gates | Australia, Dutch East Indies, Siam (+ Joint Indonesia, + Joint ABDACOM) |

### Shared and joint trees

- **Shared trees** are one focus-branch file reused by several tags — e.g. the shared Chinese branches used by China, the Chinese Soviet Republic and Manchukuo, or the shared military branch of the Trial of Allegiance South American nations.
- **Joint trees** are cooperative branches appearing in several countries' trees at once (Joint Nordic, Joint Congo, Joint Austro-Hungarian, Joint Saadabad Pact, Joint Liangguang Incident, Joint Ma Clique, Joint Indonesia, Joint ABDACOM). They are documented on their own wiki pages.
- The **Austro-Hungarian minors tree** (requires Götterdämmerung) is available *in addition to* the generic tree for Albania, Bosnia, Croatia, Herzegovina, Lombardy-Venetia, Montenegro, Silesia, Slovenia, Slovakia and Transylvania.

Focus definitions live in `/Hearts of Iron IV/common/national_focus` (one file per country or group); flavour text is in `/localisation/english/focus_l_english.yml` and per-DLC `DLC_focus_l_english.yml`. Continuous focuses are defined in `/common/continuous_focus`.
