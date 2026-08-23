---
title: Horn of Africa Nations National Focus Tree
category: focus-trees
tags: [horn of africa, focus tree, aussa, oromia, tigray, sidamo, harar, qemant, benishangul-gumuz, gambela, shared tree]
game_version: "1.19"
dlc: [By Blood Alone]
sources:
  - https://hoi4.paradoxwikis.com/Horn_of_Africa_nations_national_focus_tree
---

## Summary

The Horn of Africa nations (Sultanate of Aussa, Benishangul-Gumuz Nation, Gambela, Emirate of Harar, Oromia, Qemant State, Kingdom of Sidamo, and Tigray) share a single focus tree (requires By Blood Alone). Only Aussa is playable from game start; others are released from Ethiopia. The tree is divided into three main branches: **Develop Capital State** (industrial development, resources, naval/air bases), **The Armed Forces** (military doctrine, irregular forces, armored/artillery paths), and **The Nation** (puppet autonomy and independence paths with regional war goals).

See [01-mechanics/national-focus.md](../01-mechanics/national-focus.md) for generic/continuous focuses.

## Develop Capital State branch

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| Develop [Capital] | None | — | Capital State becomes Developed Rural Region; +1 building slot; +1 civilian factory |
| The State Bank | Develop [Capital] | — | National spirit **State Bank of [Nation]**: Consumer Goods Factories −2.0%, Factory output +10.00% |
| The [Nation] Regional Development Fund | The State Bank | The [Nation] Industrial Fund | Every owned state: Local Construction Speed +15%, Max factories +15% |
| The [Nation] Industrial Fund | The State Bank | The [Nation] Regional Development Fund | Two random owned controlled states: each gets +1 building slot, +1 civilian factory |
| Support the Agrarians | Regional Development Fund | — | Every owned state: Local Construction Speed +10%, Max factories +10% |
| Promote Local Crafts | Regional Development Fund OR Industrial Fund | — | 2× 25% research bonus: Industry; 2× 25% research bonus: Support technology |
| Use the Natural Harbors | Promote Local Crafts | Capital Airport | Requires a coastal controlled state. Random owned controlled coastal state: +1 building slot, +1 naval dockyard |
| The [Capital] Airport | Promote Local Crafts | Use the Natural Harbors | +2 air bases in capital; +10 Transport Plane to stockpile |
| A Steamboat Fleet | Use the Natural Harbors | — | 2× 50% research bonus: Destroyer models; Navy experience +25 |
| Improved Irrigation Systems | Use the Natural Harbors OR Airport | — | Every owned state: Local Construction Speed +15%, Max factories +15% |
| The [Nation] Air Fleet | Airport | — | Air experience +20; 1× 50% research bonus: Light aircraft; 1× 50% research bonus: Medium aircraft; 1× 50% research bonus: Heavy aircraft |
| State-Funded Projects | Steamboat Fleet OR Irrigation OR Air Fleet | — | National spirit **State-Funded Projects**: Construction Speed +15.00% |
| The Grand University of [Capital] | State-Funded Projects | — | +1 research slot |
| Pave the Roads | Develop [Capital] | — | Two random owned controlled states: each gets +1 infrastructure |
| The Steam Locomotive | Pave the Roads | — | Gain technology: Civilian Train (if not already); +10 Ethiopian Civilian Train to stockpile |
| Exploit National Resources | The Steam Locomotive (+ nation-specific state control conditions) | — | Nation-specific resources: Sultanate of Aussa: +8 oil in Afar (908); Oromia: +8 oil in Bale (836); Qemant State: +8 steel in Begemder (841); Tigray: +8 aluminum in Tigray (842); Benishangul-Gumuz: +8 steel in Gojjam (840); Emirate of Harar: +8 oil in Hararghe (835); Kingdom of Sidamo: +8 rubber in Sidamo (837); Gambela: +8 rubber in Illubabor-Kaffa (838) |

## The Armed Forces branch

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| The [Nation] Armed Forces | None | — | Army experience +25 |
| Warrior Tradition | Armed Forces | — | Create 3 East African Irregular Units in capital |
| Strengthen the Irregulars | Warrior Tradition | Every Man a Warrior | Add units to template East African Irregulars; National spirit **Improved Irregular Tactics**: Irregular Infantry Attack +15.00%, Defense +10.00%, Speed +5.00%, Organization +10.00% |
| Every Man a Warrior | Warrior Tradition | Strengthen the Irregulars | National spirit **Every Man a Warrior**: Recruitable Population +10%; Gain technology: Militias |
| [Nation]'s Finest | Strengthen the Irregulars | — | National spirit **Our Finest**: Division Attack on core territory +5.0% (this appears twice in wiki: +5.0% then +10.0%—interpreted as cumulative +15.0% net) |
| Utilize our Strengths | Irregulars OR Every Man | — | Nation-specific spirits: Sultanate of Aussa, Tigray, or Sidamo: **The Strengths of [Nation]**: Division Attack +10.0%, Defense +5.0%; Oromia, Gambela, or Benishangul-Gumuz: **The Strengths**: Factory output +15.00%, Dockyard output +10.00%; Emirate of Harar or Qemant State: **The Strengths**: Research Speed +10.00% |
| Reform the Conscription | Every Man a Warrior | — | War support +10.00%; if not already having Extensive Conscription, Service by Requirement, All Adults Serve, or Scraping the Barrel: Gain **Extensive Conscription** (Recruitable Population +5.00%, Training time +10.00%) |
| Eyes on the Imperialists | Utilize our Strengths | — | 1× 25% cost reduction: Land Doctrine, Air Doctrine, Naval Doctrine |
| Encourage Local Arms Production | Utilize our Strengths | — | Two random owned controlled states: each gets +1 building slot, +1 military factory |
| Metal Beasts | Eyes on the Imperialists | The Roars of Thunder, Develop Indigenous Models | 2× 50% research bonus: Armor technology |
| The Steel Lions | Metal Beasts | — | Requires: No Step Back DLC: Inter-war Tank Development researched; otherwise: Great War Tank researched. Conditional: if No Step Back and lacks Inter-war Tank, gain technology Inter-War Tank Development (else gain Interwar Tank if missing). Create Steel Lions unit in capital. |
| The Roars of Thunder | Eyes on Imperialists OR Encourage Arms | Metal Beasts, Develop Indigenous Models | 2× 50% research bonus: Support Artillery, Anti-Tank |
| Warfare from Afar | The Roars of Thunder | — | Add units to template East African Irregulars |
| Develop Indigenous Models | Encourage Local Arms Production | Metal Beasts, The Roars of Thunder | 2× 25% research bonus: Infantry Weapons |
| Modern Infantry | Develop Indigenous Models | — | Create 2 Regular Infantry units in capital |

## The Nation branch

The Nation branch splits into two major paths: **puppet autonomy path** (available while subject to another nation) and **independence path** (available when fully independent). The independence path further splits into a **conquest/expansionist path** (regional war goals and Horn of Africa unification) and an **alliance/volunteer path** (international cooperation).

### Puppet Autonomy Path (Available when subject)

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| [Nation] | None | — | Political Power +100; War support +10.00% |
| A Loyal Subject | [Nation] | — | Requires: is subject of another nation. Autonomy +250.00; Stability +5.00% |
| The [Capital] Railroad | A Loyal Subject | — | Requires: is subject; capital neighbor state owned by overlord exists. Build level 1 railway from overlord neighbor state to capital |
| Invite Foreign Settlers | A Loyal Subject | — | Requires: is subject. Capital state category upgraded (Wasteland → Pastoral → Rural → Developed Rural → Sparse Urban → Urban → Dense Urban); +75,000 Local Population |
| Improving the Educational System | Railroad OR Settlers | — | Requires: is subject. Stability +5.00%; National spirit **Improved Education**: Research Speed +5.00%. Wiki note: conditional ideology support for overlord (±10% to Non-Aligned/Communist/Fascist/Democratic based on overlord's ideology). > ⚠️ broken wiki template reconstructed |
| Foreign Investors | Educational System | — | Requires: is subject. 1× 25% research bonus: Industry; random state that can build factory: +1 civilian factory, +1 building slot |
| Research Exchange Programs | Educational System | — | Requires: is subject. 2× 25% research bonus: Industry, Electronics. Overlord also gains 2× 25% research bonus: Industry, Electronics |
| Foreign Trained Officials | Research Exchange | Loyalist Advisors | Requires: is subject. Political Power +250 |
| The [Capital] School of Technology | Foreign Trained Officials | — | Requires: is subject. +1 research slot |
| [Nation] Loyalist Advisors | Research Exchange | Foreign Trained Officials | Requires: is subject. Autonomy +750.00 |
| Promote [Nation] Nationalism | Loyalist Advisors | — | Requires: is subject. War support +10.00%; Political Power +100; Autonomy +500.00 |

### Independence Path — Stability & Leadership (Mutual Exclusion)

Both focus on Political Stability as prerequisite; thereafter split into **Leader Path** (military expansion) or **Cooperation Path** (alliances).

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| Political Stability | [Nation] | — | Requires: fully independent. Political Power +100; Stability +15.00% |
| [Nation Leader] | Political Stability | Securing the [Nation] Future | Requires: fully independent. War support +10.00%. If current leader is field marshal: +1 Attack Skill. Otherwise: country leader becomes Field Marshal |
| Securing the [Nation] Future | Political Stability | [Nation Leader] | Requires: fully independent. Political Power +75; every major country owning African state gains **African Cooperation** with opinion +75 (mutual) |

### Independence Path — Leader Route (Expansion & War Goals)

| Focus | Prerequisites | Effects |
|---|---|---|
| Construct Great Monuments | [Nation Leader] | Stability +15.00%; adds 2 victory points to various state capitals (state-dependent: Addis Ababa, Dessie, Macalle, Herat, Debre Markos, Asosa, Gambella, Irgalem, Gaba, Dire Dawa, or Aussa depending on nation) |
| That Which is Rightfully Ours | [Nation Leader] | Political Power +75; National spirit **Reclaiming the Empire** (720 days): War goal tension limit −25.0%, Justify War goal time −25.0% |
| Lay Claim to the Danakil | Rightfully Ours | Requires: fully independent. Gain claims on Danakil (273) region; gain **Take claimed state** war goal against fully independent nation with capital in Danakil |
| Push for the Highlands | Rightfully Ours | Requires: fully independent. Gain claims on Ethiopian Highlands (17) region; gain **Take claimed state** war goal against fully independent nation with capital in Highlands |
| Secure the Ogaden | Rightfully Ours | Requires: fully independent. Gain claims on Ogaden (274) region; gain **Take claimed state** war goal against fully independent nation with capital in Ogaden |
| Crowning of the Negusa Nagast | Danakil OR Highlands OR Ogaden | Requires: fully independent, controls all Ethiopian territory. All controlled states that are cores of Ethiopia become cores of [Nation]; Ethiopia loses core status on those states |
| Proclaim East-African Hegemony | Crowning of Negusa Nagast | Requires: fully independent. Unlocks decision: **Unify the Horn of Africa** |

### Independence Path — Cooperation Route (Alliances & Volunteers)

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| The [Nation] Volunteer Force | Securing the [Nation] Future | — | Requires: fully independent. National spirit **The [Nation] Volunteer Force**: Send volunteers tension limit −25.0%, Max volunteer force divisions +5, Divisions required for sending volunteers −75.0%. Sets rule: can send volunteer forces |
| Military Cooperation | Securing the [Nation] Future | — | Requires: fully independent. Command power +50.0; Army experience +100 |
| Commandos | Volunteer Force | — | Requires: fully independent. Gain technology: Special Forces; 2× 25% research bonus: Special Forces |
| A Jagged Alliance | Volunteer Force OR Military Cooperation | — | Requires: fully independent. National spirit **Safety in Alliances**: Join faction tension limit −30.0% |
| Observe and Learn | Military Cooperation | — | Requires: fully independent. 2× 50% cost reduction: Land Doctrine, Air Doctrine, Naval Doctrine |
| Rallying the [Nation] People | A Jagged Alliance | — | Requires: fully independent. National spirit **Rallying the People**: Recruitable Population +25% |

## Nation-Specific Considerations

- **Resource production** (Exploit National Resources) varies by nation: Aussa and Harar produce oil; Oromia produces oil; Qemant and Benishangul-Gumuz produce steel; Tigray produces aluminum; Sidamo and Gambela produce rubber.
- **Combat spirits** (Utilize our Strengths) split into three types: attack/defense bonus (Aussa, Tigray, Sidamo); factory/dockyard output bonus (Oromia, Gambela, Benishangul-Gumuz); research speed bonus (Harar, Qemant).
- **Field Marshal promotion** ([Nation Leader] focus) requires the country leader to either already be a field marshal (then +1 Attack Skill) or become one if not.
- **Reclaiming the Empire** 720-day spirit applies war goal justification benefits across all three regional claims (Danakil, Highlands, Ogaden).
- **Horn of Africa unification** (Proclaim East-African Hegemony) requires controlling all Ethiopian territory and completing Crowning of Negusa Nagast to unlock the decision.
