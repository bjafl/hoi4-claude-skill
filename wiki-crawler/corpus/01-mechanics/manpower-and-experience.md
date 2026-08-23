---
title: Manpower and Experience
category: mechanics
tags: [manpower, conscription, recruitable-population, experience, veterancy, attrition, accidents, medals]
game_version: "1.19"
dlc: []
sources:
  - https://hoi4.paradoxwikis.com/Manpower
  - https://hoi4.paradoxwikis.com/Recruitable_population
  - https://hoi4.paradoxwikis.com/Experience
  - https://hoi4.paradoxwikis.com/Attrition_and_accidents
---

## Summary

Manpower is drawn from the recruitable-population fraction of the states a country controls; conscription law sets that fraction, non-core and occupation penalties gut it, and mobilization speed makes every change take months. Experience exists at three levels: national (army/navy/air XP, capped at 500 each), commander, and unit veterancy. Attrition costs equipment and organisation but never manpower; air and naval units suffer accidents instead of attrition.

## Manpower

### Free manpower

Free manpower pays for training and deploying divisions, air wings and ships, and for reinforcements. It is normally the sum of recruitable population across all controlled states; a country can also hold free manpower **off-map** when states are at capacity.

Ways to increase it:
- Enact a higher conscription law or otherwise raise the recruitable population ratio (biggest lever, but slow — see Mobilization).
- Turn states into cores (focuses/decisions such as the USA granting statehood to Alaska) to remove the non-core penalty.
- Hire a **Prince of Terror** political advisor: non-core recruitable-population penalty goes from −98% to −96%.
- Choose gentler occupation policies to raise recruitable population in occupied non-core states.
- Monthly population growth adds a small amount each month.
- Take control of more states, especially cores.
- Flat grants from events and focuses.
- Disband, delete or downsize units to instantly recover manpower.

Manpower from flat grants or disbanding is stored in controlled states, or off-map if states are full. Recruitable manpower in a state is lost if the enemy captures it.

### Used manpower

**Army.** "Manpower in the field" (used as a focus condition, e.g. Danzig or War requires 950k in the field) counts all deployed divisions that are not volunteers. "In training" counts undeployed divisions. Manpower usable for training new divisions is capped at **75% of manpower in the field, or 100,000, whichever is higher**. Divisions can begin training with only a fraction of the required manpower.

Examples of per-unit manpower needs:

| Unit element | Manpower at full strength |
|---|---|
| Infantry battalion | 1,000 |
| Engineer support company | 300 |

The division designer shows the template's total manpower requirement.

**Air force and navy** use separate service-manpower pools. Ships and air wings can only be deployed if the required service manpower is available.

| Example unit | Service manpower |
|---|---|
| Destroyer 1s (1922) | 250 naval |
| Carrier 3s (1940) | 5,500 naval |
| Tactical bomber | 40 air per plane |
| Fighter | 20 air per plane |

**Total manpower** in the tooltip = off-map free manpower + every controlled state's recruitable-population cap, itemised by core/non-core. It is not the sum of any other manpower figure and has no gameplay use.

### Manpower loss and reinforcement

- Casualties from combat or accidents are removed from the unit's manpower pool immediately, reducing combat effectiveness.
- A division **overrun or destroyed in an encirclement returns 20% of its remaining manpower**; the rest is lost.
- Understrength divisions request reinforcements from the free pool **as long as they have a supply line to the capital**. Reinforcements arrive in **increments of 10% of the division's full manpower**.
- Ships replenish lost crew at **5% per day**.
- **Exercising divisions, air wings or task forces causes no casualties**, and attrition on divisions never costs manpower.

## Recruitable population

Recruitable population is a *ratio* applied to state population. Ignoring mobilization lag:

```
Recruitable ratio = Σ(Recruitable Population modifiers)
                  × Σ(Recruitable Population Factor modifiers)
                  × Σ(non-core modifier)
                  × Σ(occupation modifier)
```

Recruitable Population modifiers stack **additively**; Recruitable Population Factor modifiers are **multiplicative** with that sum.

### Conscription laws

| Conscription law | Recruitable population | Prerequisites |
|---|---|---|
| Disarmed Nation | 1.00% | — |
| Volunteer Only | 1.50% | Economy law is not Undisturbed Isolation or Isolation |
| Limited Conscription | 2.50% | Not Undisturbed Isolation/Isolation economy law; >10% war support |
| Extensive Conscription | 5.00% | Ruling party is Fascist or Communist; OR (at war AND an enemy has estimated army strength ratio ≥50% AND >20% war support) |
| Service by Requirement | 10.00% | Ruling party is Fascist or Communist; OR (at war AND estimated enemy strength ratio ≥60% AND (>60% war support OR >0% surrender progress)) |
| All Adults Serve | 20.00% | At war AND (>70% war support OR >0% surrender progress OR estimated enemy strength ratio ≥75%) |
| Scraping the Barrel | 25.00% | At war AND (>85% war support OR >25% surrender progress OR estimated enemy strength ratio ≥100%) |
| The Chitet (Ethiopia) | 4.50% | — |
| The Chitet, peace time (Ethiopia) | 0.50% | — |
| Swiss Citizen Militias | 10.00% | — |
| Expanded Swiss Citizen Militias | 20.00% | — |

### Economy law

| Economy law | Recruitable population | Prerequisites |
|---|---|---|
| Total Mobilization | −3.00% | At war, >80% war support, >50% of enemy's total factory count |

### Land doctrines

| Doctrine node | Recruitable population | Branch |
|---|---|---|
| Volkssturm | +2.00% | Mobile Warfare |
| Non-Discriminatory Conscription | +3.00% | Mobile Warfare |
| Human Wave Offensive | +5.00% | Mass Assault |

### National spirits — Recruitable population (additive)

| National spirit | Recruitable population | Source |
|---|---|---|
| Militarism | +5.00% | Generic focus: Militarism |
| Military Youth | +2.00% | Generic focus: Military Youth |
| Victors of the Great War | −0.30% | France, starting spirit |
| National Mobilization | +1.00% | France focus (non-La Résistance version) |
| Spiritual Mobilization | +2.50% | Japan focus |
| Militarized Schools | +0.50% | Soviet focus |
| Socialist Science | +3.00% | Soviet focus |
| Women's Armed Service Integration Act | +2.00% | USA focus |
| Polish Militarism | +2.50% | Poland focus |
| Military Youth | +2.00% | Poland focus |
| Send in the Zombies | +1.00% | Canada focus |
| Swastika Clubs | +2.00% | Canada, modified by focus Support the Blue Shirts |
| Social Security Act | +2.00% | New Zealand focus |
| Maori Conscription | +1.00% | New Zealand focus |
| Waitangi Tribunal | +2.00% | New Zealand focus |
| Voortrekker Monument | +0.50% | South Africa, modified by focus Commemorate the Battle of Blood River |
| Black Volunteers | +1.00% | South Africa focus: Repeal the Native Representation Act |
| Divided Nation | −0.50% | Czechoslovakia, starting spirit |
| Fortification focus | +0.30% / +0.60% / +0.90% / +1.20% | Czechoslovakia: Fortification Studies → Sudetenland Early / Advanced / Final Fortifications |
| Communism with a Human Face | +3.00% | Czechoslovakia focus |
| Czech Fascism | −0.50% | Czechoslovakia: Divided Nation modified by Czech Consolidation |
| Treaty of Trianon | −0.50% | Hungary, starting spirit |
| The Hungarian Red Army | +5.00% | Hungary focus |
| Secret Rearmament | +0.25% | Hungary focus |
| A Deal with the Devil | +1.00% | Romania focus: Form Peasant Militias |
| The Sentinel of the Motherland | +1.00% → +2.00% | Romania: Revise the Constitution → Militarize the Sentinels |
| All-Yugoslavian Regiments | +1.00% | Yugoslavia focus |
| Local Militias | +2.00% | Yugoslavia focus |
| National Revitalization | +0.50% | Germany, modified by focus Fan Prussian Militarism |
| Red Brigades | +2.00% | Japan focus |
| Forced Conscription | +2.00% | China focus |
| Five People Armies | +2.00% | Manchukuo focus |
| Labor Reform | +0.50% | Chinese warlord focus |
| Rural Militias | +1.00% | Chinese warlord focus |
| Armed Forces Desegregation | +2.00% | USA focus (Man the Guns) |
| Ejido Worker Militias | +2.00% | Mexico focus (Man the Guns) |
| Caudillo Private Armies | +1.00% | Mexico focus (Man the Guns) |
| Synarchist Youth | +1.00% | Mexico focus (Man the Guns) |
| De Jeugdstorm | +1.00% | Netherlands focus (Man the Guns) |
| Implement the "Program" | +1.00% | Netherlands focus (Man the Guns) |
| Mobilize the Masses | +3.00% | Netherlands focus (Man the Guns) |
| Enemies on All Fronts | +5.00% | Netherlands focus (Man the Guns) |
| Depillarization | +1.00% | Netherlands focus (Man the Guns) |
| De Vaarplicht | +2.50% | Netherlands focus (Man the Guns) |
| Responsibility For Our Own Defense | +1.00% | Netherlands focus (Man the Guns) |
| Le Déluge | +3.00% | France focus (La Résistance) |
| Carlism | +1.00% | Nationalist Spain, modified by Integrate the Requetés (La Résistance) |
| Expand Conscription | +2.00% | Nationalist Spain focus (La Résistance) |
| Mandatory Pre-Military Training | +2.00% | Nationalist Spain, modified by All Shall Serve (La Résistance) |
| Crusade Against Democracy | +3.00% → +5.00% | Nationalist Spain: Expand the Requetés → Militarize the Masses (La Résistance) |
| Anarchist Society | +3.00% → +8.00% | Republican Spain: Mujeres Libres → All Must Bear the Torch (La Résistance) |
| The Threats Abound | +2.00% | Republican Spain, modified by Militarize the People (La Résistance) |
| Class War | +2.00% → +5.00% | Republican Spain: Class War → The Red Tide (La Résistance) |
| An Army of All Classes | +3.00% | Republican Spain focus (La Résistance) |
| Professional Military | +1.00% | Republican Spain focus: Re-professionalize the Military (La Résistance) |
| Government Reforms | +2.00% | Bulgaria (Battle for the Bosporus) |
| Military Dictatorship | +1.00% | Bulgaria (Battle for the Bosporus) |
| The Hellenic Army | +0.20% | Greece (Battle for the Bosporus) |
| The Byzantine Army | +0.40% | Greece (Battle for the Bosporus) |
| Red Militias / Red Army | +2.00% | Greece (Battle for the Bosporus) |
| Red Enforcers | +3.00% | Greece (Battle for the Bosporus) |
| The Redshirts | +2.00% | Turkey (Battle for the Bosporus) |
| Turkish Workers' Militia | +1.00% | Turkey (Battle for the Bosporus) |

### National spirits — Recruitable population **factor** (multiplicative)

Example: the USA's Great Depression gives −50%, so with Volunteer Only the effective ratio is 1.5% × 50% = 0.75%.

| National spirit | Factor | Source |
|---|---|---|
| Full Employment | −25% | France, starting spirit |
| Worker Shortage | −25% | France, gained on moving to Extensive Conscription or beyond |
| Defeatism | −50% | France, on capitulation |
| Agricultural Collectivization | +15% | France focus |
| Le Déluge | +25% | France focus |
| The War to End All Wars | −30% | United Kingdom, starting spirit |
| The Great Depression | −50% | USA, starting spirit |
| Slow Recovery | −40% | USA, Great Depression modified by focuses |
| Slow Economic Growth | −20% | USA, Slow Recovery modified by focuses |
| Full Desegregation | +20% | USA focus |
| Spirit of Rebellion | +25% | USA, if the Confederacy forms |
| Australian Women's Army Service | +10% | Australia focus |
| Agrarian Society | −69% | British Raj, starting spirit |
| Marginalized Muslim Community | −20% → −10% | British Raj, starting spirit → modified by Two-Nation Theory |
| Famine | −10% | British Raj, if famine strikes |
| Princely States | +5% | British Raj, modified by Imperial Service Troops |
| Indian Gurkhas | +2% | British Raj focus |
| Lions of the Great War | +2% | British Raj focus |
| Conscription Crisis among French Canadians | −30% → −10% | Canada, starting spirit → Compromise with Quebec |
| National Resources Mobilization Act | +5% | Canada focus |
| Commit to the War | +5% | Canada focus |
| Send in the Zombies | +15% | Canada focus |
| The Manpower Act | +7% | New Zealand focus |
| Stomp out Pacifism | +5% | New Zealand focus: Arrest Pacifist Leaders |
| History of Segregation | −55% → −40% | South Africa, starting spirit → Reconstitute the Cape Corps |
| Cheap Labor | −5% | South Africa focus: Native Laws Amendment Act |
| Reserve Divisions | +7% | Romania focus |
| Ineffective Bureaucracy | −35% | China, starting spirit |
| Shell-shocked Spectator of the Great War | −50% | Netherlands, starting spirit (Man the Guns) |
| Unreliable Army | −25% | Portugal, starting spirit (La Résistance) |
| Colonial Assimilation Policy | +15% → +30% | Portugal, via overseas colony integration decisions (La Résistance) |
| Nation in Arms | +10% | Portugal focus (La Résistance) |
| Portuguese Legion | +5% | Portugal focus (La Résistance) |
| Camisas Azuis | +5% | Portugal focus (La Résistance) |
| Crusade Against Democracy | +20% | Nationalist Spain, modified by Cultivate Fanaticism (La Résistance) |

### Non-core states

- Base penalty **−98%** — a country's manpower comes almost entirely from cores.
- **Prince of Terror** advisor gives **+2%**, reducing the penalty to **−96%**.
- Creating **puppets** sidesteps the penalty: a puppet has full access to its own cores' manpower.

### Occupation

An occupied non-core state takes a **further −98%**, mitigated by compliance:

```
Manpower available = 100% − 98% + 18% × Compliance level
```

Average compliance across an occupied nation's states unlocks flat bonuses:

| Name | Compliance needed | Effect |
|---|---|---|
| Local Police Force | 25% | Additional Recruitable Population +0.5% |
| Volunteer Program | 60% | Recruitable Population +20% |

Maximum occupied-state pool:

```
Manpower available = (100% − 98% + 18%) × (100% + 20%) × (conscription law + 0.5%)
```

### Mobilization

- Changes to recruitable population and its factor **do not apply instantly** — the value drifts toward the new target at the mobilization speed.
- **Base mobilization speed: 0.01% per day.**
- Example: at 50% war support it takes **250 days** to fully shift from Limited to Extensive Conscription.
- The ratio only changes in steps of 0.1%/day, so new manpower first appears between roughly a week and a month after the law change, depending on mobilization speed.
- War support and some national spirits modify the base mobilization speed.

## National experience

Three separate pools, each **capped at 500**: Army experience, Navy experience, Air experience.

Sources: combat, training/exercises, attachés, volunteer forces, lend-leased equipment, military chief advisors and some political advisors (fixed amount per day), and certain national focuses and ideas.

| Pool | Spent on |
|---|---|
| Army experience | Division templates; land doctrines; land equipment variants; some decisions; tank designer *(No Step Back)*; Army officer-corps spirits *(No Step Back)*; Mountaineer special forces doctrines *(Arms Against Tyranny)* |
| Navy experience | Naval doctrines; single-use research bonuses for naval and naval-support technologies; some decisions; ship designer *(Man the Guns)* or ship variants otherwise; Navy officer-corps spirits *(No Step Back)*; Marine special forces doctrines *(Arms Against Tyranny)* |
| Air experience | Air doctrines; some decisions; aircraft designer *(By Blood Alone)* or aircraft variants otherwise; Air force officer-corps spirits *(No Step Back)*; Paratrooper special forces doctrines *(Arms Against Tyranny)* |

Commander experience is covered in [Officer corps and commanders](officer-corps-and-commanders.md). There are no air commanders; air combat instead produces **aces**, who buff the wing they are assigned to for as long as they live.

## Unit experience (veterancy)

| Level | Min XP (land & navy) | Min XP (air) | Land modifier | Navy modifier | Air modifier |
|---|---|---|---|---|---|
| Green / Fresh / Rookies | 0% | 0% | −25% | Damage −10%, Defense −10%, Fighter sortie efficiency −10% | Air attack −15%, Agility −15%, Night operations penalty +15%, Air accident chance +10% |
| Trained | 10% | 10% | 0% | 0% | 0% |
| Regular | 30% | 30% | +25% | Damage +9.90%, Defense +6.60%, Fighter sortie efficiency +6.60% | Air attack +4%, Agility +6%, Night operations penalty −4%, Air accident chance −20% |
| Seasoned | 75% | 70% | +50% | Damage +19.90%, Defense +13.30%, Fighter sortie efficiency +13.30% | Air attack +14%, Agility +21%, Night operations penalty −14%, Air accident chance −70% |
| Veterans | 90% | 90% | +75% | Damage +30%, Defense +20%, Fighter sortie efficiency +20% | Air attack +20%, Agility +30%, Night operations penalty −20%, Air accident chance −100% |

("Green" is the land label, "Fresh" the naval label, "Rookies" the air label for the same bottom tier.)

- Air units **interpolate** effects between levels by experience progress: 99% progress at Trained equals 0% progress at Seasoned. Scout planes get significantly smaller bonuses and penalties.
- Land units normally deploy at **Trained**, or at **Green** if deployed early. Naval units always start **Fresh**, air units always **Rookies**.
- **Exercising** raises units only up to **Regular**, costing time, equipment and (for fuel users) fuel. Higher tiers require combat.
- Replacing casualties reduces unit experience. Reduce this with **Field Hospitals** and certain national focuses. **Air units lose 30% less experience over friendly territory.** Some naval terrain increases casualties and therefore XP loss.
- **Template changes**: converting a division loses **0% experience if every battalion is unchanged**, up to an additional **50% experience** for changed battalions — on top of losses from any new manpower required.
- **Naval units lose 75% of their experience when transferred in a peace conference.**

## Medals

Medals are assigned to land divisions with political power after notable battlefield performance.

- Every medal, in addition to its own modifier, gives **+10% experience to divisional commanders** attached to that division and raises the **political power cost of future medals by +25%**.
- Most medals grant **100 experience to that division's divisional commander** on assignment.
- Medal cost is reduced by the **Accomplished Heritage** officer-corps spirit.
- All medals below cost **30 political power** at base.

### Generic ideology medals

Available to countries that are *not* Germany, USA, Soviet Union, United Kingdom, France, Italy, Japan, Ethiopia, Finland, Norway, Chile, Denmark or Hungary (or their successors).

| Ideology | Medal | Unit modifiers |
|---|---|---|
| Democratic | Medal for Gallantry | Recovery Rate +10% |
| Democratic | Legion of Honor | Supply Consumption −15% |
| Democratic | War Cross | Defense +5%, Reconnaissance +10% |
| Democratic | Order of the Lion | Experience loss from casualties −25% |
| Communist | Distinguished Service Medal | Supply Consumption −15%, Fuel Usage −15% |
| Communist | Red Star | Recovery Rate +10%, Defense +5% |
| Communist | Medal of Military Merit | Organization +10% |
| Communist | Hero of the Revolution | HP +10% |
| Fascist | Medal for Bravery | Organization +10% |
| Fascist | Military Merit Cross | Attack +5% |
| Fascist | Order of the Brave | Armor +10%, Reconnaissance +10% |
| Fascist | Cross of Heroism | Breakthrough +10% |
| Non-Aligned | Cross of Bravery | Defense +5%, Max Entrenchment +10% |
| Non-Aligned | The Military Order | Supply Consumption −15%, Recovery Rate +10% |
| Non-Aligned | Order of the Sword | Attack +5% |
| Non-Aligned | Order of Military Virtue | Experience loss from casualties −20%, Recovery Rate +5% |

### Country-specific medals

| Country | Medal | Unit modifiers | Extra requirements |
|---|---|---|---|
| Norway | Krigskorset | Recovery Rate +10%, XP loss from casualties −7% | — |
| Norway | Haakon VII's Cross of Freedom | Supply Consumption −10%, Reconnaissance +5% | Democratic or Non-Aligned |
| Norway | Krigsmedaljen | Max Entrenchment +10%, Defense +5% | — |
| Norway | Haakon VII's Medal of Freedom | Breakthrough +10%, Attack +5% | Democratic or Non-Aligned |
| Norway | Norwegian Peoples Cross | Organization +8%, XP loss from casualties −10% | Communist |
| Norway | Norgeskors | Organization +10%, Breakthrough +7% | Fascist |
| Norway | Deltagermedaljen | Fuel Usage −10%, Supply Consumption −5% | — |
| Norway | King's 70s Anniversary Medal | Attack +10%, Recovery Rate +5% | Democratic/Non-Aligned, after 3 Aug 1942 |
| Norway | Order of Saint Olav | Equipment Capture Ratio +10% (additive), Breakthrough +5% | Democratic or Non-Aligned |
| Finland | Mannerheim Cross | Organization +10%, Defense +5% | Not Communist |
| Finland | Order of the Red Star | Organization +10%, Defense +5% | Communist |
| Finland | Cross of Liberty | Recovery Rate +10%, XP loss from casualties −20% | — |
| Finland | Order of the White Rose | Attack +10%, Breakthrough +5% | — |
| Finland | Order of the Lion | Max Entrenchment +10%, Reconnaissance while Entrenched +10% | — |
| Sweden | Norwegian Defense Cross of Honor | Defense +16% | Protected and returned Norway's territories |
| Sweden | Medal of Merit | Supply Consumption −15%, Max Entrenchment +5% | — |
| Denmark | Order of the Dannebrog | Organization +10%, Defense +5% | Not Communist |
| Denmark | Hero of the Danish Civil Union | Organization +10%, Defense +5% | Communist |
| German Reich | Iron Cross (2nd Class) | Organization +10% | — |
| German Reich | Knight's Cross | Reconnaissance +15% | — |
| German Reich | Knight's Cross (Oak Leaves) | Fuel Usage −7.5%, Supply Consumption −7.5% | — |
| German Reich | Knight's Cross (Swords & Diamonds) | Breakthrough +7.5% | — |
| United States | Bronze Star | Recovery Rate +5%, Organization +5% | — |
| United States | Silver Star | Supply Consumption −10% | — |
| United States | Distinguished Service Cross | Attack +5% | — |
| United States | Medal of Honor | XP loss from casualties −20% | — |
| Soviet Union | Battle Merit Medal | Recovery Rate +15% | — |
| Soviet Union | Order of Kutuzov | Max Entrenchment +15% | — |
| Soviet Union | Order of the Red Banner | HP +7.5% | — |
| Soviet Union | Hero of the Soviet Union | Organization +10% | — |
| United Kingdom | Oak Leaves (Dispatches) | Reconnaissance while Entrenched +25% | — |
| United Kingdom | Order of the British Empire | HP +10% | — |
| United Kingdom | Distinguished Service Order | Defense +7.5% | — |
| United Kingdom | Victoria Cross | Recovery Rate +15% | — |
| France | Combatant's Cross | Max Entrenchment +10%, Reconnaissance while Entrenched +10% | — |
| France | War Cross | Organization +7.5% | — |
| France | Order of Liberation | Fuel Usage −15% | — |
| France | Distinguished Service Order | Supply Consumption −10%, Defense +5% | — |
| Italy | War Merit Cross | Equipment Capture Ratio +10% (additive), Recovery Rate +7.5% | — |
| Italy | Cross of Valor | Breakthrough +5%, HP +5% | — |
| Italy | Order of Savoy (5th Class) | Supply Consumption −10%, Defense −5% | — |
| Italy | Order of Savoy (1st Class) | Attack +5% | — |
| Japan | Military Medal of Honor | Recovery Rate +7.5% | — |
| Japan | Order of the Sacred Treasure | Recovery Rate +5%, HP +5% | — |
| Japan | Order of the Golden Kite | Supply Consumption −10%, Attack +5% | — |
| Japan | Order of the Chrysanthemum | Breakthrough +10% | — |
| Ethiopia | Military Medal of Merit of the Order of St. George | Organization +10% | Not Communist |
| Ethiopia | Order of the Grand Star of Honour of Socialist Ethiopia | Attack +5% | Communist |
| Ethiopia | Distinguished Military Medal of Haile Selassie the First | Recovery Rate +15% | Non-Aligned |
| Governorate of Ethiopia | Distinguished Military Medal of Haile Selassie Gugsa | Supply Consumption −15% | Fascist, ruler Haile Selassie Gugsa |
| Gojjam | Distinguished Military Medal of King Hailu Tekle Haymanot | Breakthrough +10% | Fascist, ruler Hailu Tekle Haymanot |
| Jimma | Distinguished Military Medal of Sultan Abba Jofir | Reconnaissance +10% | Fascist, ruler Abba Jofir |
| Ethiopia | Distinguished Military Medal | Supply Consumption −15% | Democratic or Communist |
| Ethiopia | Gold Medal | Equipment Capture Ratio +15% (additive) | — |
| Ethiopia | Silver Medal | XP loss from casualties −25% | — |
| Chile | La Medalla Al Valor | Recovery Rate +5%, XP loss from casualties −5% | — |
| Chile | Order of Bernardo O'Higgins | Organization +10%, HP +5% | Has not completed Avenge the Pacification of Araucanía |
| Chile | Grand Officer Grade of the Chilean Order of Merit | Attack +5%, Breakthrough +5%, HP +5% | Has not completed Avenge the Pacification of Araucanía |
| Chile | Medalla Carabineros De Chile | Reconnaissance +15%, XP loss from casualties −10% | Has not completed Avenge the Pacification of Araucanía |
| Chile | Legion de Mérito de Chile | Organization +10%, Recovery Rate +5% | Has not completed Avenge the Pacification of Araucanía |
| Chile | Commander's Cross of the Royal Order of the Steel Crown | Breakthrough +15%, Attack +5% | Not Araucanía focus; has Crown Antoine as Sovereign King |
| Chile | Commander's Cross of the Noble and Royal Order of the Southern Star | Organization +10%, Recovery Rate +5%, Supply Consumption −5% | Not Araucanía focus; has Crown Antoine as Sovereign King |
| Chile | Knight's Cross of the Legion of Medalists of the Southern Constellation | Max Entrenchment +10%, Defense +5% | Not Araucanía focus; has Crown Antoine as Sovereign King |
| Chile | Knight's Cross of Medalists of the Order of the Southern Constellation | XP loss from casualties −20%, Recovery Rate +10% | Not Araucanía focus; has Crown Antoine as Sovereign King |
| Chile | Orden El Sol del Perú | Equipment Capture Ratio +1% (additive), Defense +5%, Attack +5% | Completed Avenge the Pacification of Araucanía OR Crown Antoine as Sovereign King |
| Chile | Medalla Combatiente Weychafe Pu Mapuche | Supply Consumption −15%, Breakthrough +10% | Completed Avenge the Pacification of Araucanía |
| Chile | Medalla Meli Witran Mapu | Defense +10%, Organization +5%, Recovery Rate +5% | Completed Avenge the Pacification of Araucanía |
| Austria | Kruckenkreuz | Defense +2.5%, Organization +5%, Recovery Rate +5% | Fascist or Non-Aligned |
| Hungary | Medal of Bravery | Recovery Rate +5%, Organization +5% | Has not completed End the White Terror or End the Regency |
| Hungary | Magyar Szent István Rend | Defense +5% | — |
| Hungary | Order of Saint Stephen | Attack +2.5%, Breakthrough +2.5% | — |
| Hungary | Order of Merit of Hungary | Defense +2.5%, Organization +2.5% | — |
| Hungary | Military Order of Maria Theresa | XP loss from casualties −10%, Recovery Rate +2.5% | Completed Reinstate the Pragmatic Sanction of 1713 |
| Hungary | Knight of the Golden Spur | XP loss from casualties −10%, Organization +3% | Not Communist |
| Hungary | Transylvania Commemorative Medal | Equipment Capture Ratio +10% (additive), Supply Consumption −10% | Owns North Transylvania (76), Crisana (83), Transylvania (84) or Banat (82) |
| Hungary | Miklos Toldi Silver Medal of Merit | Breakthrough +5% | — |
| Hungary | Hungarian Grand Gold Military Merit Medal | Organization +5%, Attack +1%, Defense +1% | — |
| Hungary | Hungarian Silver Military Merit Medal with swords | Organization +5%, Breakthrough +2.5% | — |
| Yugoslavia | Medal for Extreme Bravery | Max Entrenchment +5 (flat) | Completed Extreme Bravery |

All Ethiopian medals grant **+75 extra commander experience** when the country has the **Expand the Officer Corps** spirit.

## Attrition

Attrition costs **equipment and organization, never manpower**. Only land units take attrition; air and naval units suffer **accidents** instead.

### Attrition sources

Baseline attrition for on-map units is **0%**.

| Source | Attrition added |
|---|---|
| Training (exercising) | +5% |
| Moving in hostile terrain (Desert, Jungle, Marsh, Mountain) | up to +50% |
| Weather | up to +70% |
| Resistance | up to +30% |
| Border wars | up to +10% |
| Supply status below 35% | up to +20% |
| Unit is moving | ×1.2 |

**Off-map supply trucks** start at a baseline of **0.3%** and multiply all attrition sources by **0.65×**, but are far more exposed to two of them:

| Source (trucks only) | Attrition added |
|---|---|
| Rugged terrain (Hills, Forest, Desert, Jungle, Marsh, Mountain) | up to +400% |
| Adverse weather | up to +500% |

### Organization loss

```
Organization lost per hour = 0.08 × attrition
```

Applies both in and out of combat. Divisions out of supply additionally lose **up to −0.2 recovery rate** (hourly organization gain), scaling with how far out of supply they are and how long — **maximum effect after 30 days**.

### Equipment loss — land units

```
Equipment lost per hour = 0.005 × attrition × number of equipment × (1 − reliability)
```

Simplifying for high equipment counts / low reliability across 24 hours:

```
Average daily attrition rate = 12% × attrition × (1 − reliability)
```

- At 100% attrition and 0% reliability: about **12% of equipment lost per day**.
- At 5% attrition and 80% reliability (typical for training infantry): **67 days of training** (Green → Trained) costs about **8.04% of equipment**.
- Reliability above 100% behaves exactly like 100% — no further benefit.
- **Each equipment variant calculates attrition independently.**

### Air accidents

Aircraft take no attrition; they have a base **10% accident chance** per check, modified by a **0.1× balancing factor**, reliability (up to **2× at 0% reliability**), carrier basing (**1.5×**), pilot exercises (**+20%**), veterancy, weather and other modifiers (negative country-level national-spirit modifiers do not apply).

Every game hour all airbases are checked. **At most one accident per hour per airbase**, but it can destroy multiple planes. The accident touches a random 0–100% portion of the wing, of which only **0.7%** is actually destroyed. Sub-plane fractions accumulate country-wide and are added to the next accident.

```
Hourly accident chance         = 10% × accident chance modifiers × (100% − reliability) × 2
Accident effect                = random(0,1) × 0.7%
Average accident effect        = 0.5 × 0.7% = 0.35%
Average aircraft lost per hour per airbase
                               = 10% × (100% − reliability) × 2 × 0.35%
                               = 0.07% × (100% − reliability)
```

| Reliability | Loss per hour per airbase | Per day | Per year |
|---|---|---|---|
| 90% | 0.007% of a wing | 0.168% | 61.32% |
| 80% | 0.014% of a wing | 0.336% | 122.64% |
| 40% | 0.042% of a wing | 1.008% | 367.92% |

All aircraft start with **at least 80% reliability** (except intercontinental bombers with Götterdämmerung), adjustable via variants and military industrial organizations. Because losses are small versus combat losses, combat stats usually beat reliability.

### Naval accidents

Ships take no attrition; reliability instead governs their chance of being critically hit by enemy attacks.

| Accident type | Chance | Effect | Critical chance | Critical multiplier |
|---|---|---|---|---|
| Naval exercise accident | 2% per hour | −30% current organization, −5% max HP, +4 extra strength damage | 30% | ×4 to all org and strength damage |
| Mine strike | Up to 5% depending on sea-zone mine saturation and naval terrain | −50% current organization, 50 strength damage (can outright sink small ships) | 14% | ×5 to all org and strength damage |

- **Prides of the Fleet** scale both accident chance and critical chance by **0.01×**.
- An additional **4% balancing factor** applies to all naval accidents (training and mines), smoothing out lucky/unlucky streaks.
- The game still references naval attrition through some defines, admiral traits such as **Cold Water Expert**, and weather effects such as **Arctic Water**.

## Reducing equipment loss

- Raise reliability: **Maintenance company**; tank variants *(No Step Back)*, ship designs *(Man the Guns)*, aircraft designs *(By Blood Alone)*.
- Low-supply attrition: **Logistics company**, better supply network, or move units out of overloaded provinces.
- Rough terrain: minimise time in Jungle/Mountain etc., especially with low-reliability equipment.
- Extreme heat/cold: acclimatize. Speed it with national spirits, **Winter Logistics** company, special forces doctrines / special forces concentration technologies, and the **Adaptable** and **Winter Specialist** commander traits.
- Temporary weather (Mud, Blizzards, Sandstorms): wait it out. Mud build-up is reduced by higher state **Infrastructure**.
- Resistance: **Martial Law** or **Brutal Oppression** occupation laws, the **Root Out Resistance** operative mission; against enemy resistance-boosting operations use **Counter Intelligence** plus the **Passive defense** and **Interrogation techniques** agency upgrades.
- Truck attrition: lower supply motorization (at the cost of hub range — compensate by building more supply hubs or naval bases).
- Training attrition: restrict which equipment training divisions and exercising air wings may use. Divisions train fine with outdated or no equipment and lose no experience when re-equipped afterwards.
- Global reductions: certain political advisors and military high command, certain national spirits from focuses, and the **People's Army** land doctrine (Mass Mobilization path of Mass Assault).
- Lowering a major's **strength slider** in custom difficulty settings reduces that country's attrition, but disables achievements.

## Cross-references

- [Supply and logistics](supply-and-logistics.md) — supply-based attrition, truck attrition factors by terrain and weather.
- [Officer corps and commanders](officer-corps-and-commanders.md) — commander experience, traits, officer-corps spirits.
- [Land combat](../02-land-warfare/land-combat.md) — terrain attrition values, weather modifiers.
