---
title: Paraguayan National Focus Tree
category: focus-trees
tags: [paraguay, focus tree, trial of allegiance, land reforms, american intervention, fascism, communism]
game_version: "1.19"
dlc: [Trial of Allegiance]
sources:
  - https://hoi4.paradoxwikis.com/Paraguayan_national_focus_tree
---

## Summary

Paraguay's unique national focus tree (requires Trial of Allegiance) guides the country through a civil war between communist and fascist factions, with options to side with democratic interventionists or fascist leadership. The tree features two mutually exclusive early paths: **Febrerista Land Reforms** (communist-leaning under Rafael Franco) or **Reach out to American Contacts for Aid** (democratic intervention during civil war). Shared branches exist with Uruguay and the Trial of Allegiance military focuses. Without the DLC, Paraguay uses the generic tree.

See [Paraguay](../05-countries/paraguay.md) for the country's 1936 starting profile. See [01-mechanics/national-focus.md](../01-mechanics/national-focus.md) for generic/continuous focuses.

---

## Febrerista Land Reforms Branch

Historical communist-leaning path. Mutually exclusive with **Reach out to American Contacts for Aid** at the root.

| Focus | Prerequisites | Effects |
|---|---|---|
| **Febrerista Land Reforms** | None; ME with Reach out to American Contacts for Aid; Rafael Franco is current leader | National spirit **Febrerista Land Reforms**: +10.00% resource gain efficiency, −5.0% consumer goods factor, −10.00% stability, +15.00% construction speed, −0.03 daily democracy support |
| **Ban Vouchers as Payment** | Febrerista Land Reforms | National spirit **Banned White Vouchers**: +5.00% stability, +6.00% production efficiency cap |
| **Allow Unions to Strike** | Febrerista Land Reforms | +10.00% stability, +5.00% communism support |
| **Central Bank of the Republic of Paraguay** | Ban Vouchers as Payment | +75 political power; available as industrial concern (Central Bank): +15% industrial research speed, −10.0% consumer goods factor |
| **Allow Female Workers** | Ban Vouchers as Payment OR Allow Unions to Strike | National spirit **Women in the Industry**: +5.00% construction speed, +10.00% factory/dockyard output |
| **A Great Charter** | Central Bank OR Allow Female Workers | +150 political power, +60 command power, +5.00% communism support, +5.00% non-aligned support |
| **Invite Japanese Settlers** | A Great Charter | Chaco Boreal (688) or random controlled core state: +4 building slots |
| **Military Pensions** | Febrerista Land Reforms | +5.00% stability, +5.00% war support, +40 army experience, +10.00% communism support, +5.00% non-aligned support |
| **Chaco War Decorations** | Military Pensions | Every army leader: +1 skill level, +2 attack, +1 logistics, +1 defense; +20 army experience; every unit officer gains 2000 field commander XP |

---

## Pull Back Troops From the Chaco (Fascist Sub-branch)

Fascist path: ousting Rafael Franco and joining the Axis. Requires **A Great Charter** to proceed.

| Focus | Prerequisites | Effects |
|---|---|---|
| **Pull Back Troops From the Chaco** | A Great Charter; ME with Revenge for the Chaco War; Bolivia at peace; Paraguay not in civil war; controls Chaco Boreal (688); Higinio Morinigo not leader (bypasses if Morinigo is leader) | Event 'The Army Revolts'; −5.00% stability; Gobierno de Morínigo becomes ruling party; elections cancelled; +20.00% non-aligned support, +10.00% fascism support; removes **Febrerista Land Reforms** spirit; Rafael Franco exiled; event 'Higinio Morinigo Takes Power in Paraguay' |
| **Discipline, Hierarchy and Order** | Pull Back Troops From the Chaco | National spirit **Discipline, Hierarchy and Order**: +8.0% division organization, +8.00% stability modifier, +0.10 daily command power |
| **Suspend Elections** | Pull Back Troops From the Chaco | National spirit **Turmoil** (270 days): −0.10% weekly stability, +5% resistance target, +3.0% resistance activity chance → upgrades to **Cemented Control**: +40 max command power, −5% resistance target, −10.0% resistance activity chance |
| **Get Rid of Colonel Paredes** | Suspend Elections | Retire Ramón Paredes; current leader gains **Dictator** trait: +25% political power gain, +20.0% AI desired divisions factor, +0.10% weekly war support (combat casualties) |
| **Ban the Liberal Party** | Suspend Elections | +5.00% war support; +25.00% non-aligned support, +10.00% fascism support; −25.00% democracy/communism support |
| **Align with the Guión Rojo** | Suspend Elections | National spirit **Guión Rojo**: +15.00% stability modifier, +3.00% war support, +15.00% recruitable population |
| **Ensure Army Loyalty** | Get Rid of Colonel Paredes OR Ban the Liberal Party; requires min 20K manpower in divisions (AI: 10K) and infantry equipment in stockpile; requires Extensive Conscription or higher; requires Partial Mobilization or higher economy | Generals gain bonus stats and random trait; national spirit **Very High Military Spending** (1460 days): +0.20 daily army experience, +200 weekly manpower, +20.0% consumer goods factor, +15% daily command power gain; 45% GDP reserved for military; event 'Officers support the government' |
| **Radicalize the Police** | Ensure Army Loyalty | National spirit **Radicalized Police Force**: +4.00% non-core manpower, −5% resistance target, −10.0% resistance activity chance; available political advisor Mutshuito Villasboa Barboza (Prince of Terror): +2.00% non-core manpower, −30% foreign subversive activities efficiency, −25.00% damage to garrisons |
| **Nazify the Army** | Ensure Army Loyalty | +15.00% fascism support; 2× 35% cost reduction for Land Doctrine; unlocks decision 'Flip to Fascism' (Guión Rojo becomes ruling party, elections cancelled) |
| **Join the Axis** | Ensure Army Loyalty; ME with Join The Allies / Join the Comintern; fully independent; Germany/Japan/other major faction leader at war and at peace with Paraguay; not in faction and not already accepted American investment | Event to requesting faction membership (varies by faction leader) |

---

## Revenge for the Chaco War (Communist Sub-branch)

Communist path: military aggression toward Bolivia and Chile. Requires **Chaco War Decorations** to proceed.

| Focus | Prerequisites | Effects |
|---|---|---|
| **Revenge for the Chaco War** | Chaco War Decorations; ME with Pull Back Troops From the Chaco; Bolivia exists and at peace; Paraguay not in civil war; Higinio Morinigo not leader (bypasses if Bolivia doesn't exist) | Annex war goal against Bolivia; removes **The Toll of the Chaco War** national spirit (if held) |
| **Get Rid of Obsolete Guns** | Revenge for the Chaco War; at least 3500 infantry equipment in stockpile | −3.50K infantry equipment; −1.0 years ahead-of-time penalty and 100% research bonus for next 2 Infantry Weapons researches |
| **Neuter the Guión Rojo** | Revenge for the Chaco War | +10.00% stability; −25.00% fascism/non-aligned support |
| **Liga Nacional Independiente** | Neuter the Guión Rojo | +5.00% communism support, +5.00% stability, +5.00% war support |
| **Partido Revolucionario Febrerista** | Neuter the Guión Rojo | +5.00% communism support, +150 political power |
| **Access the Sea** | Revenge for the Chaco War; Peru OR Chile exists and at peace; Paraguay not in civil war | Annex war goal against Chile (if exists); annex war goal against Peru (if exists) |

---

## The Permanent Leader / Mythologize the Father of the Nation / Cult of Personality (Shared Fascist/Communist Sub-branch)

Shared focuses between the Fascist and Communist branches, providing leader traits and national spirits.

| Focus | Prerequisites | Effects |
|---|---|---|
| **The Permanent Leader** | Pull Back Troops From the Chaco OR Revenge for the Chaco War | Current leader gains **The Permanent Leader** trait: +15% recruitable population factor, +20.00% surrender limit, +5.00% war support, −5% resistance target |
| **Mythologize the Father of the Nation** | Align with the Guión Rojo OR Liga Nacional Independiente | National spirit **Father of the Nation: Francisco Solano López**: +15% recruitable population factor, +5.0% consumer goods factor, +20% resistance growth speed in enemy-occupied core states |
| **Cult of Personality** | Align with the Guión Rojo OR Liga Nacional Independiente OR Partido Revolucionario Febrerista | Current leader gains **Cult of Personality** trait: +5.00% stability, +5.00% war support, +10.0% division attack on core territory, +15.0% division defense on core territory |

---

## Reach out to American Contacts for Aid Branch

Democratic intervention path during civil war. Mutually exclusive with **Febrerista Land Reforms** at root; requires Paraguay to be in a civil war and at peace with USA.

| Focus | Prerequisites | Effects |
|---|---|---|
| **Reach out to American Contacts for Aid** | ME with Febrerista Land Reforms; in civil war; at peace with USA; bypasses if Febrerista not taken and after Jun 1, 1937 | +150 political power; current leader gains **Cornered Fox** trait: +10.0% division recovery, +15.0% division defense; +5.00% democracy support |
| **A Call-Out For Aid** | Reach out to American Contacts for Aid; at peace with France | National spirit **French volunteers** (1080 days): +2500 weekly manpower |
| **Ask For Bankroll** | A Call-Out For Aid | Random controlled core state: +3 building slots, +1 civilian factory, +2 military factories |
| **Request Weapons from United States** | Reach out to American Contacts for Aid; at peace with USA | +2000 American M1903 Springfield, +650 American 75 mm Gun M1897, +500 American Support Equipment |
| **To Cross a River** | Reach out to American Contacts for Aid; at peace with USA | Add technology Marines I; random army leader gains Trickster (+25.0% reconnaissance) or Improvisation Expert (+10.0% movement); random owned controlled state creates 3 Paraguayan units |
| **Specialized Terrain Training** | To Cross a River | National spirit **Specialized Terrain Training**: +10.00% division speed, +10.0% terrain penalty reduction, −20.00% river crossing speed penalty |
| **Emergency Powers** | Ask For Bankroll | −10.00% stability, +15.00% war support; rules: can declare war without war goal against same ideology, can justify war goals without tension, can join factions led by another ideology; national spirit **Country under emergency powers**: −15.00% training time, −100.0% war goal tension limit, −20.0% faction join limit, −25.0% justify war goal time, +20.0% ideology drift defense, −15% resistance target |
| **By All Means Which To Win** | Ask For Bankroll | Adopt **Total Mobilization** economy (−3.00% recruitable population, ~10% expected consumer goods, −30.00% factory conversion cost, +30.00% military factory construction); +40.00% war support, −25.00% stability; activates decision 'Women in the Workforce' (−100 PP; +3.00% recruitable population, −5.00% stability) |
| **Assassinate Rafael Franco** | By All Means Which To Win; ME with Goad Bolivia; in civil war; at peace with UK | Rafael Franco dies; national spirit **Chaos and confusion**: −75.00% surrender limit, −15.0% division defense; if La Résistance DLC enabled: creates intelligence agency and applies upgrades (Upgrade Army Department, Plastic explosives, Commando training) |
| **Goad Bolivia** | By All Means Which To Win; ME with Assassinate Rafael Franco; in civil war; at peace with UK | Bolivia gains annex war goal against communist Paraguay; Paraguay gains annex war goals against Bolivia |
| **Put Estigarribia on a pedestal** | Assassinate Rafael Franco OR Goad Bolivia; not in civil war | National spirit **Co-Rule with Jose Félix Estigarribia**: +15.0% army experience gain, −10.0% supply consumption, +10.0% max planning, +0.01 daily unaligned support; current leader loses **Unpopular** trait; José Félix Estigarribia gains +1 skill, +1 attack, +1 planning, +1 defense; gains **Media Personality** trait (+100.0% army reassignment duration); unlocks decision 'Appoint Estigarribia as leader' |
| **Purge the military of Dissent** | Put Estigarribia on a pedestal; not in civil war | National spirit **Officers Purged** (230 days): −15.0% division organization, −6.00% factory output, +15.00% training time, −38.0% max volunteer force divisions, +3.00% land/naval/air doctrine cost → upgrades to: +24000 manpower, 2× 50% cost reduction for Land Doctrine; José Félix Estigarribia gains +1 skill, +1 planning, +2 defense |
| **Aftermath of the Civil War** | Purge the military of Dissent | +8.00% war support; +20.00% ruling party popularity; −2.15K Paraguayan Basic Infantry Equipment; national spirit **Devastation** (210 days): −20.00% stability, −15.00% factory/dockyard output → upgrades to **Recovering Economy** (180 days): −5.00% stability, +5.00% factory/dockyard output → upgrades to **Flourishing Economy**: −10.0% consumer goods factor, +15.00% construction speed, +15.00% factory/dockyard output |
| **Prisoners as Soldiers** | Purge the military of Dissent | +6 Penal Battalions with full manpower; unlocks **Penal Battalions** unit type; +16000 manpower |

---

## Order Italian Planes / Urbanization / Rebuild Humaitá (Shared Sub-branch)

Shared across Febrerista Land Reforms and Reach out to American Contacts branches.

| Focus | Prerequisites | Effects |
|---|---|---|
| **Order Italian Planes** | Febrerista Land Reforms OR Reach out to American Contacts for Aid; at peace with Italy (bypasses if at war with Italy) | Depends on DLC: **By Blood Alone**: Creates CR.32 Fighter and SM.81 Tactical Bomber variants; +60 Inter-War Small Airframe, +50 Basic Medium Airframe. **Otherwise**: If Italy researched Macchi C.200: +100 Italian Macchi C.200; if Fiat BR.20 researched: +80 Italian Fiat BR.20. **Arms Against Tyranny**: Adds equipment subsidies for Fighter, Strategic Bomber, and Tactical Bomber from Italy |
| **Urbanization** | Febrerista Land Reforms OR Reach out to American Contacts for Aid | Random controlled core state: +1 building slot, +1 civilian factory; if any core state is coastal, random coastal state gets +1 building slot and +1 naval dockyard; otherwise random core state gets +1 building slot and +1 military factory |
| **Rebuild Humaitá** | Febrerista Land Reforms OR Reach out to American Contacts for Aid; controls Fortress Humaitá (2173) in Paraguay (301) | Sets Fortress Humaitá victory points to 5; Paraguay (301): if flag `increased_humaita_spending` not set, +5 land forts in a province; otherwise +7 land forts in one province and +2 land forts in another; +2 building slots |

---

## Nationalize Foreign Companies / Adopt Minority Languages (Communist/Foreign Intervention Shared Sub-branch)

Shared between the Communist and foreign intervention branches.

| Focus | Prerequisites | Effects |
|---|---|---|
| **Nationalize Foreign Owned Companies** | Partido Revolucionario Febrerista OR Emergency Powers | Random controlled core state: +2 building slots, +1 military factory, +1 civilian factory |
| **Adopt Minority Languages** | Liga Nacional Independiente OR Emergency Powers | National spirit **Guaraní in the Army**: +5.0% division organization, +10.0% division recovery, −0.25% civilian intelligence to others, −25.0% army/navy/air force intelligence to others |
| **Free Secondary Schools** | Adopt Minority Languages | National spirit **Free Secondary Schools**: +6.00% research speed |
| **Mass Drafts** | Adopt Minority Languages | National spirit **Mass Drafts**: +2.50% recruitable population |

---

## Accept American Loans (Foreign Alliance Sub-branch)

Shared across Ensure Army Loyalty (Fascist), Liga Nacional Independiente (Communist), and Emergency Powers (Democratic) branches.

| Focus | Prerequisites | Effects |
|---|---|---|
| **Accept American Loans** | Ensure Army Loyalty OR Liga Nacional Independiente OR Emergency Powers; at peace with USA; either (not in faction) OR (in faction with USA); if in faction with UK and UK is democratic: must not have **Accepted American Investment**; rule: cannot join factions initially | Will accept American funds for 210 days, preventing other faction joins; national spirit **Accepted American Investment** (210 days): −15.0% consumer goods factor, +20.00% construction speed, rule: cannot join factions; if conditions allow, leaves non-USA faction |
| **Agricultural and Medical Technical Assistance** | Accept American Loans; at peace with USA; same faction conditions as Accept American Loans | Will accept American funds for 210 days; national spirit **Accepted American Investment** (210 days); random controlled core state: +2 building slots and +1 building slot (separate); technologies granted: Support Equipment (if not researched), Motorized Infantry (if not researched), Field Hospital I/II/III (if not researched); leaves non-USA faction if applicable |
| **Brazilian Road Finance** | Agricultural and Medical Technical Assistance; at peace with USA; same faction conditions | Will accept American funds for 210 days; national spirit **Accepted American Investment** (210 days); Chaco Boreal (688): +2 building slots, +1 supply hub; builds level 3 railway from Paraguay (301) to Chaco Boreal (688); leaves non-USA faction if applicable |
| **Join the Allies** | Brazilian Road Finance; ME with Join the Axis / Join the Comintern; fully independent; either (USA faction leader, democratic, at peace with Paraguay) OR (UK faction leader, democratic, at peace with Paraguay) | Event to request faction membership (varies by faction leader) |
| **Join the Comintern** | Accept American Loans; ME with Join the Axis / Join The Allies; fully independent; at peace with USSR; not already accepted American investment | Event to request faction membership from USSR or Communist China (varies by faction leader) |

---

## Paraguay/Uruguay Shared Branches

This tree includes branches shared with Uruguay's national focus tree that provide expansion opportunities, industrial buildings, and research bonuses. For details, see the Paraguay/Uruguay shared national focus tree branches page.

---

## Trial of Allegiance Shared Military Branches

This tree includes military branches shared across Trial of Allegiance nations that provide special national spirits and military bonuses. The military benefits vary depending on whether Paraguay is fascist or communist. For details, see the Trial of Allegiance shared military national focus tree branches page.

> ⚠️ Broken wiki templates: Focus descriptions contained `[{{{1}}}]` placeholders (intended for ideology icons). These have been reconstructed contextually (e.g., Communist leaning → communism ideology).
