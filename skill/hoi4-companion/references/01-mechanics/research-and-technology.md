---
title: Research and Technology
category: mechanics
tags: [research, technology, research-slots, ahead-of-time, engineering, industry, doctrine, xp]
game_version: "1.19"
dlc: []
sources:
  - https://hoi4.paradoxwikis.com/Research
  - https://hoi4.paradoxwikis.com/Engineering_technology
  - https://hoi4.paradoxwikis.com/Industry_technology
---

## Summary

Research is done by assigning one of a country's research slots to a technology for a number of days. Base research times are multiples of 110 days, modified additively by research-speed bonuses and multiplicatively worsened by the ahead-of-time (AOT) penalty if the tech's year has not arrived. Slot count is set per country (2, 3 or 4 base) and expanded by national focuses. This file covers slot mechanics, all speed modifiers, the AOT formula, and the complete Engineering and Industry technology trees.

## Technology categories

| Group | Trees |
|---|---|
| Land | Infantry technology, Artillery technology, Support Companies technology, Armor technology (differs without No Step Back), Land doctrine, Special forces doctrine |
| Naval | Naval technology (differs without Man the Guns), Naval support technology (Man the Guns), Naval doctrine |
| Air | Air technology (differs without By Blood Alone), Air doctrine |
| Industry | Engineering technology, Industry technology |
| Special Projects | Technologies unlocked only by completing special projects (requires Götterdämmerung) |

- Infantry technology also covers motorized, mechanized and special forces (marines, mountaineers, paratroopers).
- Artillery technology covers artillery, anti-tank, anti-air and rocket artillery.
- Support Companies technology covers Engineer, Recon, Military Police, Maintenance, Field Hospital, Logistics, Signal companies.
- Armor technology covers light/medium/heavy/super-heavy chassis plus tank destroyer, SPG and SPAA variants.
- Engineering technology covers electronics (computers, radios, radar, cryptography), fortifications, rockets and atomic research. Encryption/decryption techs are part of it only **without** La Résistance.
- Industry technology covers production efficiency, factory output, construction, excavation, and synthetic refineries.

## Research slots

A technology is unlocked by assigning a research slot to it for the required number of days.

- Base slot counts are defined per country. Countries without an explicit definition get **3 if European, 2 if non-European**.
- National focus trees grant **1–3 extra slots** depending on the country. Most countries cannot take all of them in one game because they sit on mutually exclusive branches.
- Some slot focuses have conditions — commonly "has 50+ factories", or "has fewer than 5 research slots". Commonwealth countries must become fully independent to reach their maximum.
- Each research slot can bank up to **30 points of "Days Saved"** while unassigned. Days Saved are added to research progress once a tech is selected, and are themselves scaled by research-speed modifiers.

### Base and maximum slots by country

| Base | Max | Countries | Slot-granting focuses |
|---|---|---|---|
| 2 | 3 | Yunnan, Xibei San Ma, Sinkiang, Shanxi, Guangxi Clique (without No Compromise, No Surrender) | Public Education Reform |
| 2 | 3 | Yunnan, Sinkiang, Shanxi, Guangxi Clique, Guangdong Clique, Sichuan Clique, Northeastern Army, Shandong Clique, Hebei-Chahar, Qinghai Ma, Gansu Ma, Ningxia Ma, Khotan Ma, Kumul Khanate (with No Compromise, No Surrender) | Expand Public Education |
| 2 | 4 | Afghanistan | Expand Kabul University; then Education Reform / Darulaman University (mutually exclusive) |
| 2 | 4 | Argentina | Technical Schools; then University Reforms / Universidad de Buenos Aires / Socialist Researchers / Fascist Researchers (mutually exclusive) |
| 2 | 4 | Brazil | National Technology Fund; then University of São Paulo / Federal University of Rio de Janeiro / The People's University of Brazil / Establish Royal College of Rio de Janeiro (mutually exclusive) |
| 2 | 4 | Chile | Advancements in Telecommunications; then Invite French Academia (Rule by Decree) / Strengthen the Instituto Nacional / Strictly Controlled Education (mutually exclusive) |
| 2 | 4 | Iceland | Industrial Research School; Expanding the University of Reykjavik; International Research Community |
| 2 | 4 | Iran | Educational Reforms; then Imperial Funded Universities / Open Abadan Technical School / Enforce Secularism / Establish Tehran University / Expand Education System |
| 2 | 4 | Aussa, Tigray, Qemant, Benishangul-Gumuz, Gambela, Sidamo, Oromia, Harar | The Grand University of [Capital]; The [Capital] School of Technology |
| 2 | 5 | British Raj (without Graveyard of Empires) | Indian Defense Research; Indian Institute of Science; Research Collaboration |
| 2 | 5 | British Raj (with Graveyard of Empires) | Indo-Centric Curriculum / Education Efforts / To Shake The World; "Form Akhand Bharat" decision (Hindutva); Planned Economy (Netaji); Continue the Five Year Plan; The Five Year Plan. As East India Company: Privatized Tutelage, Mineral Exploitation Institute, Attract Scientists. As Mughal Empire: Halls of Knowledge, Imperial Academies, The Well of Eternal Knowledge |
| 2 | 5 | Philippines | Quezon City Campus; Philippine-American Educational Foundation (after Peg the Peso to the Dollar); Philippine Military Academy |
| 2 | 5 | Australia (without Thunder at Our Gates) | Army Inventions Directorate; Fund Australian Defense Research; Research Collaboration |
| 2 | 5 | Communist China (without No Compromise, No Surrender) | Literacy Programs; China Medical University; Form the Academy of Sciences (last two need <5 slots) |
| 2 | 5 | Communist China (with No Compromise, No Surrender) | Form the Academy of Sciences; The People's Republic; then Lessons of the West (The Unwilling Diarchy) / Reestablish Moscow Sun Yat-sen University (Reclaim the Grasp of Power) / Establish the Yan'an University (The Leadership of Mao Zedong) |
| 2 | 5 | Warlords that have claimed the Chinese Soviet tree | Literacy Programs (needs <5 slots); China Medical University; Form the Academy of Sciences |
| 2 | 5 | China (without No Compromise, No Surrender) | Expand the Academica Sinica; Chemical Research Institute; Rural Schooling (need <5 slots) |
| 2 | 5 | China (with No Compromise, No Surrender) | Expand the Academica Sinica; The National Sun Yat-sen University; Unify the Admissions Process; Championing the Cause of Liberty |
| 2 | 5 | Reorganized National Government of the Republic of China; warlords holding the national-China tree | Expand the Academica Sinica; Chemical Research Institute; Rural Schooling; Reopen the National Assembly |
| 2 | 5 | Belgian Congo | National Institute for Agronomic Study; Socialist Education Reforms (after Invite Kwame Nkrumah to the Capital); African RTD Department (after Liberation by Force); Royal University for Higher Education; Establish Lovanium University (shared); Research Grants (shared) — all need <5 slots |
| 2 | 5 | Dutch East Indies (with Thunder at Our Gates) | Expand the Batavia Institute of Technology; then via The Jewel in the Crown: Expand Batavia Medical School, Economic Integration; via Underground Revolution: Construct Akademi Angkatan Laut, Soviet Economic Integration, Education Reform, Education Subsidies |
| 2 | 5 | Ethiopia | Addis Ababa School of Technology; Ethiopian Industrial Research Institute; Communal Education |
| 2 | 5 | Iraq | Expand the Baghdad Colleges; Modernize Military Doctrines; Kurdish Language Schools (as Kurdistan) |
| 2 | 5 | Manchukuo (without No Compromise, No Surrender) | Law University; Research And Education Department; Social Research Unit / Imperial University (mutually exclusive) |
| 2 | 5 | Manchukuo (with No Compromise, No Surrender) | Law University; Research And Education Department; then Imperial University (Bolster Nationalism) / Beiyang University (The new Beiyang government) / Research Cooperation with the CPC (Zhao Shangzhi's Coup) / Study the Gassakusha (Strengthen the Concordia Association, as Japanese puppet) |
| 2 | 5 | Mexico | Television Innovators; Rural Schools / Científico Camarilla (mutually exclusive); State Education / Church Schools (mutually exclusive) |
| 2 | 5 | Paraguay, Uruguay | National Academy of Sciences; Paraguayan Mechanical University; The South American Higher University |
| 2 | 5 | Portugal (with La Résistance) | Instituto Superior Técnico; Military Research Facilities; Naval Research Institute |
| 2 | 5 | Siam (with Thunder at Our Gates) | Thammasat University; Kasetsart University; Mahidol University |
| 2 | 5 | South Africa | Fund the University of South Africa; The Cape Defense Institute; Defense Collaboration Initiative |
| 2 | 5 | Generic 2-slot countries in 1936: Dutch East Indies (without Thunder at Our Gates), Albania, Bhutan, Bolivia, British Burma, Bulgaria (without Battle for the Bosporus), Colombia, Costa Rica, Cuba, Dominican Republic, Ecuador, El Salvador, Guatemala, Haiti, Honduras, Oman, Jordan, Lebanon, Luxembourg, Mengkukuo, Mongolia, Nepal, Nicaragua, Palestine, Panama, Peru, Saudi Arabia, Siam (without Thunder at Our Gates), Syria, Tannu Tuva, Tibet, Venezuela, Yemen | Extra Research Slot; Extra Research Slot II; Technology Sharing |
| 2 | 5 | Generic 2-slot releasable/non-1936 nations (Altai Republic, Balochistan, Bukharan Republic, Buryatia, Croatia, Kurdistan, Manipur, Mysore, Rajputana, Sindh, Sikkim, Yakutia, Algeria, Angola, Bangladesh, Egypt, Ghana, Israel, Korea, Kuwait, Libya, Nigeria, Pakistan, Somalia, Sri Lanka, Sudan, Tunisia, Wales, Zambia, Zimbabwe, and many others) | Extra Research Slot; Extra Research Slot II; Technology Sharing |
| 2 | 6 | New Zealand | Department of Scientific And Industrial Research; National Defense Institute; Expand the University of Auckland; Research Collaboration |
| 3 | 4 | Norway | Expand Norges Tekniske Høgskole |
| 3 | 5 | Switzerland | "Expand Arms Industry" decision; Weapons of Democracy |
| 3 | 5 | Australia (with Thunder at Our Gates) | Workers' Educational Association; State Research Funding; Big Business Pact; Council for Scientific and Industrial Research; Department of Munitions |
| 3 | 5 | Austria | Volksschule; then Universität Wien / Österreichische Akademie / Universität Graz (mutually exclusive) |
| 3 | 5 | Lithuania, Latvia, Estonia | Unchain Our Education; Technology Sharing |
| 3 | 5 | Belgium | Royal Military Academy; Val-Benoît Institutes |
| 3 | 5 | Bulgaria (with Battle for the Bosporus) | Expand Sofia University; Vasil Levsky National Military University |
| 3 | 5 | Canada | Fund the National Research Council; Defense Research Grants |
| 3 | 5 | Czechoslovakia (without Peace for Our Time) | War College; Czech Technical University; Knowledge Sharing Teams (need <5 slots) |
| 3 | 5 | Czechoslovakia (with Peace for Our Time) | Expand the Land Department of VTÚ; then Expand PRF's Science Facilities / Shrink Educational Disparities (mutually exclusive) |
| 3 | 5 | Denmark | Expand Institut for Teoretisk Fysik; then Welcome Foreign Scientists / Expand Københavns Universitet / Experimental Technology (mutually exclusive) |
| 3 | 5 | Finland | Suomen Akatemia; then Finnish Learned Societies / Joint Scientific Program / Intellectual Elite (mutually exclusive) |
| 3 | 5 | France | Support the Grandes Écoles; Form the National Research Center |
| 3 | 5 | Greece | Academy of Athens; then The Die is Cast! (Byzantium) / The Greek Industrial Revolution / Expansion of Athens University / Cement Greco-German Ties (mutually exclusive) |
| 3 | 5 | Hungary (without Götterdämmerung) | Institute for Industrial Techniques; Expand the Technical University of Budapest / Aeronautic Technology Institute (mutually exclusive) |
| 3 | 5 | Hungary (with Götterdämmerung) | Expand the Hungarian Academy of Sciences; Expand the Technical University of Budapest |
| 3 | 5 | Netherlands | Expand R&D Facilities; Domestic Innovation |
| 3 | 5 | Poland | Polish School of Mathematics; Expand the University of Warsaw |
| 3 | 5 | Romania | Expand the University of Bucharest; The Royal Foundation |
| 3 | 5 | Nationalist Spain | From The Phalanx Ascendant: Develop All Talent, Exemplify the Art And Science of Warfare; Direct the Universities (needs Unify the Nationalist Front); Found the Academia Vázquez De Mella (needs Supremacy of the Communion); Utilize the Intellectuals |
| 3 | 5 | Republican Spain | From Regional Defense Council of Aragon: Literacy Programs, Freedom of Thought. From The Anti-Fascist Worker's Revolution: Invite Socialist Intellectuals, Beacon of Socialism. From Maintain the Second Republic: A Frontline Suited for Intellectuals, Restore Higher Education |
| 3 | 5 | Sweden | The Royal Institute of Technology; Expand the University of Uppsala |
| 3 | 5 | Turkey | Utilize Foreign Capital; then Reinstate the Darülfünûn-u Şahâne (as Ottoman Empire) / Edirne Research Exchange / Expanded Credit on Our Debts / Cooperative Research Centers / The International of Proletarian Freethinkers |
| 3 | 5 | Yugoslavia | Expand the University of Zagreb; Expand the University of Ljubljana / Expand the University of Belgrade (mutually exclusive) |
| 3 | 5 | Japan (without No Compromise, No Surrender) | Fund the RIKEN Institute; then Open Up the Universities / Expand the Showa Research Association / National Research Policy / Research Spending (mutually exclusive) |
| 3 | 5 | Japan (with No Compromise, No Surrender) | Fund the RIKEN Institute; then Overhaul the Education System / Expand the Showa Research Association / Politicize the Education System / Reorganize Tokyo Imperial University (mutually exclusive) |
| 3 | 5 | Generic 3-slot 1936 countries: Ireland, British Malaya, Portugal (without La Résistance) | Extra Research Slot; Extra Research Slot II |
| 3 | 5 | Generic 3-slot releasables (Armenia, Azerbaijan, Bavaria, Belarus, Bosnia, Brittany, Cambodia, Crimea, CSA, Danzig, Far Eastern Republic, Generalgouvernement, Georgia, Hanover, Hyderabad, Kazakhstan, Karelia, Kashmir, Kosovo, Laos, Macedonia, Montenegro, Occitania, Papal States, Prussia, Quebec, all Reichskommissariate, Saxony, Serbia, Silesia, Slovenia, Sardinia-Piedmont, Thuringia, Tuscany, Transylvania, The Two Sicilies, Ukraine, Vietnam, and others) | Extra Research Slot; Extra Research Slot II |
| 3 | 6 | Soviet Union | The USSR Academy of Sciences; Leningrad Polytechnical Institute; Socialist Humanism (requires The Right Opposition) |
| 4 | 5 | Germany | Develop Heraeus Research Facilities |
| 4 | 5 | United Kingdom | Extra Research Slot |
| 4 | 6 | Germany (without Götterdämmerung) | Develop Heraeus Research Facilities; Reverse the Brain Drain |
| 4 | 6 | Italy | Expand National Universities; Il Sol dell'Avvenire; Scientific Cooperation |
| 4 | 6 | United States | Scientist Haven; Scientific Research & Development Office (requires Continue the New Deal); American Institute of Sciences (requires Reestablish the Gold Standard) |
| 4 | 6 | East Germany, West Germany (releasable) | Extra Research Slot; Extra Research Slot II |

> ⚠️ The wiki's research-slot table contains several broken focus templates; focus names for Communist China, China (with No Compromise, No Surrender), Czechoslovakia (Peace for Our Time), Australia (Thunder at Our Gates) and Manchukuo are reconstructed from the raw focus ids and may render differently in-game.

## Research time

Base research cost is a multiple of the standard 110-day cost.

| Base cost (days) | Example technologies |
|---|---|
| 55 | Basic Cruiser Armor Scheme, Small-Caliber Semi-Armor Piercing Shell |
| 82 | Improved Airplane Catapult |
| 110 | Support Equipment, Improved Anti-Air, Fuel storage |
| 137 | Engineer Company I, Cavity Magnatron |
| 165 | Basic Infantry Equipment, Civilian Train, Towed Anti-Tank |
| 192 | Early Heavy Ship, Reinforced Mothership Wings |
| 220 | Infantry Equipment II, Towed Rocket Artillery, Radio |
| 275 | Night Vision I, Mechanical computing, Streamlined line |
| 330 | Mechanized Equipment III, Synthetic oil experiments, Super-Heavy Tank Chassis |
| 550 | Atomic Research |

## Research speed

- Research-speed modifiers stack **additively into a speed bonus**, then divide the cost. 110 days at +15% research speed = ceil(110 / 1.15) = **96 days**.
- "Days Saved" are subtracted from the already-modified day count, so they scale with research speed too.
- The aggregate research bonus is recalculated **every day**; changes apply immediately to all ongoing research (except limited-use bonuses, which lock on assignment).
- **Research speed cannot fall below 10% of default speed.**

### Difficulty modifier

| Difficulty | Research speed |
|---|---|
| Civilian | +15% |
| Recruit | +7% |
| Regular | 0% |
| Veteran | −15% |
| Elite | −30% |

### Trade law modifier

| Trade law | Research speed |
|---|---|
| Free Trade | +10% |
| Export Focus | +5% |
| Limited Exports | +1% |
| Closed Economy | 0% |

### Technologies that increase research speed

| Technology | Year | Research speed |
|---|---|---|
| Electronic mechanical engineering | 1936 | +3% |
| Mechanical computing | 1936 | +4% |
| Computing machine | 1938 | +5% |
| Improved computing machine | 1940 | +8% |
| Atomic research | 1940 | +4% |
| Advanced computing machine | 1942 | +8% |

Total from all six: **+32%**.

### Limited-use (one-time) bonuses

- Granted by national focuses. Activated when a research slot is assigned to an applicable technology; once activated, the bonus locks to that technology even if the slot is reassigned.
- 3-day grace period to move the bonus to a different applicable technology in the same slot.
- A limited-use bonus can also act as an **ahead-of-time bonus**, subtracting its stated value from the AOT penalty.
- Some naval and naval-support technologies let you spend **navy experience** for a one-time research speed bonus; this stacks on top of any focus-granted one-time bonus being spent at the same moment.

### Equipment licensing

Licensing equipment from another country gives **+20% research speed** on that equipment's technology. For designer-based equipment — tanks (No Step Back), ships (Man the Guns), aircraft (By Blood Alone) — the bonus applies only to the chassis/hull/airframe technologies, **not** to module technologies.

### Technology sharing

Members of a research group (technology sharing group) get a research-speed bonus per other member that has already unlocked the technology, **capped at +50%**. It behaves like a limited-use bonus: once applied it is locked to that tech, and later changes only affect future research. Subjects benefit less depending on autonomy level.

### Other sources

National spirits, political advisors and design companies give continuous research-speed bonuses to applicable technology categories. With **Arms Against Tyranny**, military industrial organizations can be assigned to research, giving a research-speed bonus at a daily political power cost — see [Military industrial organizations](military-industrial-organizations.md).

## Ahead-of-time penalty

Every technology has a year it becomes current. Researching before that date applies an ahead-of-time (AOT) penalty of **200% per year ahead** (AOT = 2 by default). Ahead-of-time bonuses from national focuses subtract from this.

Speed multiplier while ahead of time = `1 / (AOT × T + 1)` where `T` = years ahead.

| Years ahead (T) | Speed multiplier, AOT = 2 | With a 50% AOT bonus (AOT = 1.5) |
|---|---|---|
| 1.0 | 1/3 | 1/(2·1 − 0.5 + 1) = 2/5 |
| 0.5 | 1/2 | 1/(2·0.5 − 0.5 + 1) = 2/3 |
| 0 | 1 | 1 |

Because the penalty is recalculated daily, it shrinks continuously while the tech is being researched. Ordinary (additive) research-speed bonuses are applied linearly and therefore **do not** offset the AOT multiplier — only explicit ahead-of-time bonuses do.

Estimated days to complete a technology started `T` years early, with base cost `N` days and aggregate research bonus `B`:

```
t = 365 × (T + 1/AOT) × (1 − exp( −(AOT × N / 365) × 1/(1+B) ))
```

If research spills past the tech's current date (i.e. `t > 365T`), the estimate with AOT = 2 becomes:

```
t = 365 × ( T + N/(365(1+B)) − ln(2T+1)/2 )
```

Day-by-day simulation (equivalent, and what the game actually does):

```python
res_perc = 0.0
time = 0
base = 170     # base cost in days
bonus = 0.34   # aggregate research speed bonus
aot = 0.47     # current AOT penalty value (not years ahead)
base /= 1 + bonus
while res_perc < 1:
    res_perc += 1/base/(1+aot)
    aot -= 2/365
    if aot < 0: aot = 0
    time += 1
print(time)
```

## Doctrine and XP costs

Land, naval and air doctrines are researched in the same slots as other technologies, but many doctrine and designer decisions also consume experience:
- Army experience: division templates, some land doctrine one-time bonuses.
- Navy experience: ship designs, plus one-time research-speed bonuses on some naval and naval-support technologies.
- Air experience: aircraft designs.

_Exact per-doctrine XP figures are not covered on the Research page._ See the doctrine pages for per-branch costs.

---

# Engineering technology

Engineering technology covers computing, radios, radar, fortifications, nuclear weapons, rockets and rocket engines. Its bonuses are country-wide and mostly affect research speed and unit stats rather than the economy. Encryption/decryption technologies are included **only without La Résistance**.

Engineering technologies are heavily interlinked with special projects (requires Götterdämmerung): many require or unlock projects, and some grant breakthrough progress in a project category while being researched. Icons with a **red ribbon** are tied to Aerodynamics/Avionics projects; **yellow ribbon** to Nuclear Research projects; radar technologies carry both.

## Electronic Engineering

| Technology | Year | Base time | Prerequisites | Effects |
|---|---|---|---|---|
| Electronic mechanical engineering | 1936 | 110 days | – | Research speed +3%; enables Central Rangefinding ship module; unlocks the Radar special project |

### Radio Technology

| Technology | Year | Base time | Prerequisites | Effects |
|---|---|---|---|---|
| Radio | 1936 | 220 days | Electronic mechanical engineering | Reinforce rate +2%; Coordination +2%; enables Basic Radio tank module (No Step Back), Radio Navigation I airplane module (By Blood Alone), Basic radio land cruiser module (Götterdämmerung + No Step Back) |
| Improved Radio | 1938 | 220 days | Radio | Reinforce rate +2%; Coordination +2%; enables Improved Radio tank module (NSB), Radio Navigation II airplane module (BBA), Improved radio land cruiser module (Gött+NSB); unlocks Proximity Fuze project (Götterdämmerung) |
| Advanced Radio | 1941 | 220 days | Improved Radio | Reinforce rate +1%; Coordination +2%; enables Advanced Radio tank module (NSB), Advanced radio land cruiser module (Gött+NSB) |

Radio line totals: Reinforce rate +5%, Coordination +6%.

### RADAR Technology

| Technology | Year | Base time | Prerequisites | Effects |
|---|---|---|---|---|
| Cavity Magnatron | 1938 | 137 days | Radar (special project) | Coordination +1%; radar station limit → 2 per state; enables Improved Decimetric Naval Search Radar ship module |
| Centimetric Radar | 1940 | 137 days | Cavity Magnatron | Coordination +2%; static AA hit chance factor +20%; radar station limit → 4 per state; enables Air-Air Radar I and Air-Ground Radar I airplane modules (By Blood Alone) |
| Phased Array | 1941 | 137 days | Centimetric Radar | Coordination +1%; static AA hit chance factor +20%; radar station limit → 5 per state; enables Air-Air Radar II airplane module (BBA), Centimetric Gunnery Radar ship module |
| Monopulse Radar | 1942 | 137 days | Phased Array | Coordination +1%; static AA hit chance factor +20%; radar station limit → 6 per state; enables Air-Ground Radar II airplane module (BBA), Integrated Fire Control Radar ship module |

The base Radio Detection tech (from the Radar special project) sets the radar station limit to 1 per state.

### Computing Technology

| Technology | Year | Base time | Prerequisites | Effects |
|---|---|---|---|---|
| Mechanical Computing | 1936 | 275 days | Electronic mechanical engineering | Research speed +4%; enables Bomb Sights I airplane module (BBA); unlocks Machine-Assisted Decryption and Machine-Assisted Encryption intelligence agency upgrades (La Résistance) |
| Computing Machine | 1938 | 275 days | Mechanical computing | Research speed +5% |
| Improved Computing Machine | 1940 | 275 days | Computing machine | Research speed +8%; enables Stabilizer tank module (NSB), Bomb Sights II airplane module (BBA) |
| Advanced Computing Machine | 1942 | 275 days | Improved computing machine | Research speed +8% |

#### Fire Control Systems

| Technology | Year | Base time | Prerequisites | Effects |
|---|---|---|---|---|
| Basic Fire Control System | 1936 | 110 days | Mechanical computing | Enables Director Fire ship module |
| Improved Fire Control System | 1936 | 110 days | Computing machine | Enables Mechanical Rangekeeper ship module |
| Advanced Fire Control System | 1936 | 110 days | Improved computing machine | Enables Ballistic Computer ship module |

#### Encryption methods (without La Résistance)

| Technology | Year | Base time | Prerequisites | Effects |
|---|---|---|---|---|
| Encryption – Polyalphabetical Ciphers | 1938 | 110 days | Computing machine | Encryption +1 |
| Encryption – Cyclic Permutations | 1940 | 110 days | Improved computing machine | Encryption +1 |
| Encryption – Pulse-code Modulation | 1942 | 110 days | Advanced computing machine | Encryption +1 |

#### Decryption methods (without La Résistance)

| Technology | Year | Base time | Prerequisites | Effects |
|---|---|---|---|---|
| Decryption – Frequency Analysis | 1938 | 165 days | Computing machine | Decryption +1 |
| Decryption – Side-channel Attack | 1940 | 165 days | Improved computing machine | Decryption +1 |
| Decryption – Automated Deduction | 1942 | 165 days | Advanced computing machine | Decryption +1 |

## Fortification Engineering

| Technology | Year | Base time | Prerequisites | Effects |
|---|---|---|---|---|
| Basic Fortification | 1936 | 165 days | – | Max land fort level +1; max coastal fort level +1; unlocks Stronghold Network project (Götterdämmerung) |
| Improved Land Forts | 1938 | 165 days | Basic Fortification | Max land fort level +1; enables Bunker Emplacement land cruiser module (Gött+NSB) |
| Advanced Land Forts | 1940 | 165 days | Improved Land Forts | Max land fort level +1 |
| Improved Coastal Fortifications | 1936 | 165 days | Basic Fortification | Max coastal fort level +1 |
| Advanced Coastal Fortifications | 1940 | 165 days | Improved Coastal Fortifications | Max coastal fort level +1 |

Fully researched: max land fort level +3, max coastal fort level +3 over the base cap.

## Atomic Research

| Technology | Year | Base time | Prerequisites | Effects |
|---|---|---|---|---|
| Atomic research | 1940 | 550 days | – | Research speed +4%; unlocks the Nuclear Reactor special project (gateway to all Nuclear Research projects) |

## Experimental Rockets

| Technology | Year | Base time | Prerequisites | Effects |
|---|---|---|---|---|
| Experimental Rockets | 1942 | 165 days | – | Enables Rocket Site building, limit 3 per state; unlocks Flying Bomb, Ballistic Missile, Rocket Interceptor projects |
| Improved Guidance | 1943 | 110 days | Flying Bomb (project) + Experimental Rockets | Guided Missiles range +25%; Support Rocket Artillery / Rocket Artillery / Truck-Drawn Rocket Artillery / Motorized Rocket Artillery soft attack +10%; enables Guided Anti Ship Missile (By Blood Alone) |
| Dual Chamber Rocket Engines | 1944 | 165 days | Rocket Interceptor (project) + Experimental Rockets | With BBA: Rocket Engine II airplane module. Without BBA: Rocket Interceptor II |
| Advanced Dual Chamber Rocket Engines | 1946 | 165 days | Dual Chamber Rocket Engines | With BBA: Rocket Engine III airplane module. Without BBA: Rocket Interceptor III |
| Rocket Propelled Bombs | 1944 | 110 days | By Blood Alone + Flying Bomb + Experimental Rockets | Enables Rocket-Propelled Bombs airplane module |
| Heavy Rocket Propelled Bombs | 1945 | 110 days | By Blood Alone + Rocket Propelled Bombs | Enables Heavy Rocket-Propelled Bombs airplane module |

## Secret techs

| Technology | Who can get it | Effects |
|---|---|---|
| Decryption Bonus | Argentina, Brazil, Chile, Paraguay, Uruguay via Department of Military Intelligence; Poland via The Cyclometer; Iceland via Infiltration; United Kingdom via Cryptologic Bomb; Dominion of Canada via Camp X | Decryption power +10 |

## Special-project-unlocked techs (requires Götterdämmerung)

| Technology | Unlocked by | Effects |
|---|---|---|
| Radio Detection | Completing the Radar project | Coordination +1%; enables Radar Station building, limit 1 per state |
| Nuclear Bombs | Completing the Nuclear Fission Bomb Project | Nuclear bomb production +0.5/month. As the United States at war with Japan, plays the music track "A Warning to Japan" |
| Thermonuclear Bombs | Completing the Thermonuclear Bomb project | Thermonuclear bomb production +1/month |
| Centrifugal Isotope Separation (`isotope_separation_centrifugal`) | Isotope Separation Facilities project prototype outcome | Nuclear Fission Bomb Project speed +5%; Thermonuclear Bomb project speed +5%; nuclear bomb production rate +50% |

---

# Industry technology

Industry technology covers industrial output, construction speed, repair speed, resource gain efficiency, fuel gain efficiency, and unlocks fuel silos and synthetic refineries. All its bonuses are economic.

## Production (machine tools)

| Technology | Year | Base time | Prerequisites | Modifiers |
|---|---|---|---|---|
| Basic machine tools | 1936 | 165 days | – | Production efficiency cap +10% |
| Improved machine tools | 1937 | 165 days | Basic machine tools | Production efficiency cap +10% |
| Advanced machine tools | 1939 | 220 days | Improved machine tools | Production efficiency cap +10% |
| Assembly line production | 1941 | 220 days | Advanced machine tools | Production efficiency cap +10% |
| Flexible line | 1943 | 275 days | Assembly line production (excludes Streamlined line) | Production efficiency cap +10%; **production efficiency retention +20%** |
| Streamlined line | 1943 | 275 days | Assembly line production (excludes Flexible line) | Production efficiency cap +10%; **production efficiency growth +10%** |
| Pulverized Coal-Firing Boilers | 1937 | 220 days | Improved machine tools | Energy gain per coal +15% |
| High-Efficiency Turbines | 1939 | 220 days | Pulverized Coal-Firing Boilers | Energy gain per coal +15% |

Raising the efficiency cap also speeds up efficiency growth, because daily growth scales with the cap. Relative daily growth versus a 50% cap:

| Cap after tech | Growth vs. 50% cap | Growth vs. previous cap |
|---|---|---|
| 60% (Basic machine tools) | ×1.44 | ×1.44 |
| 70% (Improved machine tools) | ×1.96 | ×1.361 |
| 80% (Advanced machine tools) | ×2.56 | ×1.306 |
| 90% (Assembly line production) | ×3.24 | ×1.265625 |
| 100% (Flexible/Streamlined line) | ×4.00 | ×1.235 |

Flexible line and Streamlined line are mutually exclusive; pick retention (Flexible) if you switch production lines often, growth (Streamlined) if lines are stable.

## Industry — Concentrated vs. Dispersed

Two mutually exclusive branches of 5 levels each (1936, 1937, 1939, 1941, 1943; 220 days each). Switching branches later means researching the other branch from scratch.

| Technology | Year | Base time | Prerequisites | Per-level modifiers |
|---|---|---|---|---|
| Concentrated industry I | 1936 | 220 days | Basic machine tools (excludes Dispersed industry I) | Factory output +15%; Dockyard output +10%; max factories in a state +20% |
| Concentrated industry II | 1937 | 220 days | Concentrated industry I | same as above |
| Concentrated industry III | 1939 | 220 days | Concentrated industry II | same as above |
| Concentrated industry IV | 1941 | 220 days | Concentrated industry III | same as above |
| Concentrated industry V | 1943 | 220 days | Concentrated industry IV | same as above |
| Dispersed industry I | 1936 | 220 days | Basic machine tools (excludes Concentrated industry I) | Factory output +10%; Dockyard output +10%; production efficiency retention +10%; production efficiency base +5%; factory bomb vulnerability −15%; max factories in a state +20% |
| Dispersed industry II | 1937 | 220 days | Dispersed industry I | Factory output +10%; Dockyard output +10%; production efficiency retention +10%; production efficiency base +5%; factory bomb vulnerability −10%; max factories in a state +20% |
| Dispersed industry III | 1939 | 220 days | Dispersed industry II | same as II |
| Dispersed industry IV | 1941 | 220 days | Dispersed industry III | same as II |
| Dispersed industry V | 1943 | 220 days | Dispersed industry IV | same as II |

Fully-researched branch totals:

| Modifier | Concentrated industry | Dispersed industry |
|---|---|---|
| Factory output | +75% | +50% |
| Dockyard output | +50% | +50% |
| Max factories in a state | +100% | +100% |
| Production efficiency retention | – | +50% |
| Production efficiency base | – | +25% |
| Factory bomb vulnerability | – | −55% |

Rule of thumb: concentrated wins after roughly a year to a year and a half of a production line running the same equipment; dispersed wins in the first year to 18 months of a new line, and for the first two to three years of an existing line switched to an upgraded variant of the same equipment.

## Construction technologies

| Technology | Year | Base time | Prerequisites | Modifiers (each level) |
|---|---|---|---|---|
| Construction I | 1936 | 220 days | – | Construction speed +10%; factory repair speed +10% |
| Construction II | 1937 | 220 days | Construction I | Construction speed +10%; factory repair speed +10% |
| Construction III | 1939 | 220 days | Construction II | Construction speed +10%; factory repair speed +10% |
| Construction IV | 1941 | 220 days | Construction III | Construction speed +10%; factory repair speed +10% |
| Construction V | 1943 | 220 days | Construction IV | Construction speed +10%; factory repair speed +10% |

Full line: construction speed +50%, factory repair speed +50%.

## Excavation technologies

| Technology | Year | Base time | Prerequisites | Modifiers (each level) |
|---|---|---|---|---|
| Excavation I | 1936 | 220 days | Construction I | Resource gain efficiency +10% |
| Excavation II | 1937 | 220 days | Construction II | Resource gain efficiency +10% |
| Excavation III | 1939 | 220 days | Construction III | Resource gain efficiency +10% |
| Excavation IV | 1941 | 220 days | Construction IV | Resource gain efficiency +10% |
| Excavation V | 1943 | 220 days | Construction V | Resource gain efficiency +10% |

Full line: resource gain efficiency +50%.

## Synthetic resources

| Technology | Year | Base time | Prerequisites | Effects |
|---|---|---|---|---|
| Fuel storage | 1936 | 110 days | – | Unlocks Fuel Silo building, limit 3 per state |
| Fuel refining I | 1936 | 330 days | Fuel storage | Fuel gain per oil +20%; fuel gain from refineries +10% |
| Fuel refining II | 1937 | 330 days | Fuel refining I | Fuel gain per oil +20%; fuel gain from refineries +10% |
| Fuel refining III | 1939 | 330 days | Fuel refining II | Fuel gain per oil +20%; fuel gain from refineries +10% |
| Fuel refining IV | 1941 | 330 days | Fuel refining III | Fuel gain per oil +20%; fuel gain from refineries +10% |
| Fuel refining V | 1943 | 330 days | Fuel refining IV | Fuel gain per oil +20%; fuel gain from refineries +10% |
| Synthetic oil experiments | 1936 | 330 days | Fuel storage | Unlocks Synthetic Refinery building, limit 3 per state |
| Oil processing | 1937 | 165 days | Synthetic oil experiments | Fuel gain from refineries +50% |
| Improved oil processing | 1939 | 165 days | Oil processing | Fuel gain from refineries +50% |
| Advanced oil processing | 1941 | 165 days | Improved oil processing | Fuel gain from refineries +50% |
| Modern oil processing | 1943 | 165 days | Advanced oil processing | Fuel gain from refineries +50% |
| Rubber processing | 1937 | 165 days | Synthetic oil experiments | Synthetic refinery rubber output +1 |
| Improved rubber processing | 1939 | 165 days | Rubber processing | Synthetic refinery rubber output +1 |
| Advanced rubber processing | 1941 | 165 days | Improved rubber processing | Synthetic refinery rubber output +1 |
| Modern rubber processing | 1943 | 165 days | Advanced rubber processing | Synthetic refinery rubber output +1 |

Full fuel refining line: fuel gain per oil +100%, fuel gain from refineries +50%. Full oil processing line: fuel gain from refineries +200% on top. Full rubber processing line: +4 rubber per synthetic refinery.

See also: [Production and equipment](production-and-equipment.md), [Construction and buildings](construction-and-buildings.md), [Trade, resources and the international market](trade-resources-and-market.md), [Special projects and scientists](special-projects-and-scientists.md).
