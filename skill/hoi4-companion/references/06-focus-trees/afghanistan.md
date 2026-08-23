---
title: Afghanistan National Focus Tree
category: focus-trees
tags: [afghanistan, focus tree, graveyard of empires, communism, monarchy, fascism]
game_version: "1.19"
dlc: [Graveyard of Empires]
sources:
  - https://hoi4.paradoxwikis.com/Afghan_national_focus_tree
---

## Summary

Afghanistan has a unique national focus tree added by the Graveyard of Empires DLC (base game uses the generic tree). The tree contains 5 main branches and 11 sub-branches, offering political paths ranging from communist revolution via Soviet support to monarchy preservation, fascist alternate leaders, neutral balancing between Allies and Axis, and military development. Many focuses enable expansion into Central Asia, Iran, India, and other regional territories depending on the chosen path.

See [Afghanistan](../05-countries/afghanistan.md) for the country's 1936 starting profile.

> **Note:** See [01-mechanics/national-focus.md](../01-mechanics/national-focus.md) for generic/continuous focuses available to all countries.

## Expand the Telegraph Network Branch

Industrial branch focused on economy development and improving the Subsistence Economy national spirit. Unlocks research slots, factories, and railroads; opens paths to Soviet aid (leading to Socialist Coup sub-branch) or foreign investment (Look to Other Partners path).

| Focus | Prerequisites | Effects |
|---|---|---|
| Expand the Telegraph Network | None | Every owned state: Local Construction Speed +5%, Local Available Resources +5%, Infrastructure construction speed +5% |
| Clear Malarial Swamps | Expand the Telegraph Network; At least 4 Civilian factories; Excavation I researched | Herat (415): +3 Building slots; Stability +5% |
| Construct the Qargha Dam | Clear Malarial Swamps; At least 6 Civilian factories; Kabul (267) owned and controlled (bypass if lost) | Kabul (267): +1 Dam; Dam modifiers: Max Factories +15%, Factories Energy Consumption −65%, Available Resources +10%, Construction Speed +15% |
| Establish Helmand Valley Authority | Construct the Qargha Dam; At least 10 Civilian factories; Farah (1009) owned and controlled | Farah (1009): +1 Dam with same modifiers; National spirit Helmand River Projects (Consumer Goods Factories −15%, Stability +10%); Event chain may trigger war with Kerman (414) state owner |
| Expand Copper and Tin Mines | Establish Helmand Valley Authority; Khyber Pass (1006) owned and controlled | Khyber Pass (1006): +16 Steel production |
| Establish Chromite Mines | Establish Helmand Valley Authority; Qandahar (1008) owned and controlled | Qandahar (1008): +24 Chromium production |
| A Modern Economy | Expand Copper and Tin Mines OR Establish Chromite Mines; At least 20 Civilian factories | Remove Subsistence Economy spirit; National spirit Emerging Economy (Construction Speed +10%, Production efficiency growth +10%, Factory output +10%, Infrastructure construction speed +10%); +2 Military factories in random state; +2 Building slots in random state |
| Infrastructure Investment | Expand the Telegraph Network; At least 3 Civilian factories | National spirit Infrastructure Investment (Infrastructure construction speed +5%, Supply Hub construction speed +10%, Railway construction speed +5%, Dockyard construction speed +10%); 1× +60% bonus for Trains and Railways; Capital state: +1 Infrastructure if less than 5 |
| Afghanistan Ring Road | Infrastructure Investment; At least 5 Civilian factories | Every fully controlled owned cored state: +2 Infrastructure; Remove Economic Regionalism modifier |
| Establish Afghan Railway Company | Afghanistan Ring Road; At least 8 Civilian factories; Civilian Train researched | Afghan Railway Company available as Industrial Concern (Train Production cost −25%, Armor +15%, Supply Hub construction speed +15%, Railway construction speed +15%); +10 UK Trains to stockpile; Kabul-Herat railway level 1; Herat: +1 Supply Hub |
| Electrification Initiatives | Infrastructure Investment; At least 5 Civilian factories | Kabul (267): +Electrification (Max Factories +20%, Available Resources +20%, Construction Speed +20%, Infrastructure construction speed +20%); Spreads to new core state every 2 months; Kabul Electronics Company available (Electronics Research Speed +15%) |
| Modernize Radio Kabul | Electrification Initiatives | National spirit Radio Kabul (Stability +5%, Research Speed +4%, Ideology drift defense +30%); Add Radio technology if not researched |
| Expand Kabul University | Establish Afghan Railway Company AND Modernize Radio Kabul; At least 10 Civilian factories | +1 Research Slot; Mission: Graduates becoming radicalized due to unemployment (must be managed) |
| Establish Military Industries | Expand Kabul University | Decisions to establish Military Industrial Organizations; Extends time limit on graduates unemployment mission; +2 Military factories in random state; +2 Building slots in random state |
| Invest in Spinzar Cotton Factories | Expand the Telegraph Network | Random owned controlled cored state (prioritize Maymanah 1007): +2 Building slots; +2 Civilian factories |
| Fruit Processing | Expand the Telegraph Network | 1× +50% Research bonus for Industry; Random state: +1 Building slot, +1 Civilian factory; Modify Subsistence Economy: Production efficiency growth +10%, Production efficiency cap +10%, Factory output +10%, Stability −5% |
| Look to Other Partners | Fruit Processing [Mutually Exclusive] Renew Soviet Trade-Agreement | Major nations investment opportunity; Trade relations with Soviet Union +25; Unlock decisions for foreign investment |
| Offer 75 Year Oil Concessions | Look to Other Partners | Unlock decisions to extract oil resources in collaboration with foreign power |
| Baghlan Sugar Factory | Expand the Telegraph Network | Random state: +1 Building slot, +1 Civilian factory; Modify Subsistence Economy with same bonuses as Fruit Processing |
| Expand Karakul Lambskin Industry | Fruit Processing AND Baghlan Sugar Factory | Random state: +1 Building slot, +1 Civilian factory; 1× +50% Research bonus for Industry; Modify Subsistence Economy |
| Renew Soviet Trade-Agreement | Baghlan Sugar Factory [Mutually Exclusive] Look to Other Partners; Soviet Union exists, at peace, not Fascist | +2 offmap Civilian factories; National spirit Renew Soviet Trade-Agreement (Research Speed +2%, Daily Communism Support +0.02, Communist Diplomacy acceptance +25, Soviet license purchase −30%, Soviet license production +10%, Soviet trade cost −20%); Nisar Muhammad Yousafzai available (War support +10%, War goal justification −10%, Daily Communism Support +0.10); Sets Soviet flag for aid request |
| Salang Pass Tunnel | Renew Soviet Trade-Agreement; Qataghan (1005) owned and controlled | Qataghan (1005): +1 Building slot, +1 Civilian factory, +2 Infrastructure; Military access granted to Soviet Union; Soviet Ideology Influence on the Rise (+0.02 daily) |
| Janagalak Truck Factory | Renew Soviet Trade-Agreement | (requires Arms Against Tyranny) GAZ (Automotive Manufacturer) as foreign MIO (+3 Sizes); Random state: +1 Building slot, +1 Civilian factory; Communism popularity +7.5%; Sets Soviet aid flag |
| Ministry of Supply | Expand the Telegraph Network; Farah (1009) owned and controlled | Farah (1009): +1 Supply Hub; Kabul-Farah railway level 1; 1× +30% Research bonus for Synthetic resources |
| Da Afghanistan Bank | Ministry of Supply | Modify Subsistence Economy; Da Afghanistan Bank available (Central Bank concern, Consumer Goods Factories −15%) |

### Socialist Coup Sub-branch

Communist sub-branch triggered via Soviet aid path (Renew Soviet Trade-Agreement, Salang Pass Tunnel, or Janagalak Truck Factory). Installs pro-Soviet communist government; grants army, propaganda, and industry bonuses; enables conquest of Central Asian territories and Iran.

| Focus | Prerequisites | Effects |
|---|---|---|
| Socialist Coup | Janagalak Truck Factory OR Salang Pass Tunnel OR Promote the Counter Elite; Not in civil war; 20%+ Communist support; Fully independent OR overlord exists; (Bypasses if already Communist) | Civil war if Communist support <60%; Politics change to Communist (100%); Create Pashtun and Loyalist Militia templates; Nur Muhammad Taraki available (Political Power Gain +5%, Recruitable population +5%, Daily Communism Support +0.06); +100 Political Power |
| Request Soviet Aid | Socialist Coup; In civil war; Current ruling party is Communist; Soviet Union exists and Communist | Soviet Union event; if accepts: Soviet Union gets +3 Max volunteer force divisions, −100 divisions required, volunteers enabled; Gains opinion +25 with Afghanistan; +2,000 Soviet Infantry Equipment, +500 Soviet Support Equipment to stockpile; National spirit Aid the Afghan Communists (Lend-lease tension limit −30%, Max volunteer divisions +3) for 730 days |
| State Atheism | Socialist Coup; Not in civil war; Current ruling party is Communist | National spirit State Atheism (Stability −5%, Research Speed +10%, Political Advisor Cost −25%) |
| Support Soviets In Asia | State Atheism OR Soviet Research Cooperation; Fully independent; Communist; Soviet Union exists and Communist; (Bypasses if subject or in Soviet faction) | Soviet Union: Set rule Can Create Factions, Can send volunteer forces; Afghanistan seeks to join Comintern |
| Topple the Shah of Iran | Support Soviets In Asia; In faction with Soviet Union; Iran exists and Communist, no NAP with Soviet Union, not Soviet puppet | War goal (Puppet casus belli) against Iran |
| Soviet Research Cooperation | Socialist Coup; Communist; Not in civil war; Soviet Union exists and Communist | Soviet Union event for Technology Sharing proposal; if accepted, joins tech sharing group |
| Communist Industrialization | State Atheism OR Soviet Research Cooperation | National spirit Rapid Industrialization (Consumer Goods Factories −25%, Construction Speed +20%) for 720 days |
| Ministry of Propaganda | Communist Industrialization; Radio researched | Unlock decisions to boost stability, war support, and Communist party popularity via Afghan National Radio |
| Defender of Central Asia | Communist Industrialization OR Support Soviets In Asia; In faction with Soviet Union; Ashkhabad, Tashauz, Khiva, Karakalpakstan, Bukhara, Navoi, Tashkent, Stalinabad all owned by Soviet Union | Soviet Union event for Central Asian Unification; if accepts: All Turkmenistan, Tajikistan, Uzbekistan cores become Afghan; Afghanistan renamed Kingdom of Darya |
| Develop Uzbekistan | Defender of Central Asia; Bukhara (830) owned and controlled | Bukhara: +8 Oil, +8 Tungsten, +1 Building slot, +1 Civilian factory |
| Develop Tajikistan | Defender of Central Asia; Stalinabad (742) owned and controlled | Stalinabad: +8 Aluminum, +2 Building slots, +2 Civilian factories |
| Develop Turkmenistan | Defender of Central Asia; Ashkhabad (584) owned and controlled | Ashkhabad: +8 Oil, +2 Building slots, +2 Civilian factories |
| Central Asian Unification | Develop Uzbekistan OR Develop Turkmenistan OR Develop Tajikistan; Any owned state is Tajikistan core and controlled by Afghanistan | Unlock Development of Central Asia decisions to gain cores on Central Asian Soviet states transferred to Afghanistan; Remove Disgruntled Minority modifier from all states |

### International Brigades Sub-branch

Shared communist/democratic sub-branch available during civil war or active war. Recruits international volunteers for manpower support.

| Focus | Prerequisites | Effects |
|---|---|---|
| International Brigades | Socialist Coup OR Parliamentary Democracy; In civil war OR at war; Communist OR Democratic ruling party | National spirit International Brigades (Weekly Manpower +500) for 730 days |

## Support King Zahir Branch

Non-aligned historical branch focused on preserving King Zahir Shah's monarchy. Opens sub-branches for democratic modernization (Expand the King's Power-base), neutrality balancing (Biding Our Time), and visits to foreign capitals.

| Focus | Prerequisites | Effects |
|---|---|---|
| Support King Zahir | [Mutually Exclusive] Against Kabul; Non-Aligned ruling party; Has national spirit King Zahir Shah | King Zahir Shah gains Political Power Gain +5%, Daily Unaligned Support +0.02; Replace King Zahir Shah spirit with King Zahir Shah (1) variant (Stability +10%); +100 Political Power |

### Expand the King's Power-base Sub-branch

Democratic sub-branch under King Zahir. Ousts the King's uncles, promotes counter-elite, and transitions to parliamentary democracy or maintains Islamic traditionalism.

| Focus | Prerequisites | Effects |
|---|---|---|
| Expand the King's Power-base | Support King Zahir [Mutually Exclusive] Biding Our Time; Non-Aligned ruling party | If Stability >100%: Stability −5%; Otherwise: War support −5%; +100 Political Power |
| Retire the Uncles | Expand the King's Power-base; Non-Aligned ruling party | Current leader retires; Mohammed Zahir Shah becomes leader (Popular Figurehead: Political Power Gain +5%, Stability +10%, Daily Unaligned Support +0.02); Sardar Shah Mahmud Khan removed; Ghulam Muhammad Ghobar available (Daily Political Power +0.10, Stability +5%, Daily Communism Support +0.03, Daily Democracy Support +0.05) |
| Promote the Counter Elite | Retire the Uncles; Non-Aligned ruling party | +100 Political Power; National spirit Counter-Elite on the Rise (Political Power Gain +10%, Research Speed +3%, Political Advisor Cost −25%, Daily Democracy Support +0.03); Qiamuddin Khadim available (Political Power Gain +5%, Daily Compliance Gain +0.02%, Daily Communism Support +0.05); Mohammed Daoud Khan becomes advisor (Stability −5%, Production efficiency cap +10%, Production efficiency growth +10%, Research Speed +3%) |
| Ally the Young Afghans | Promote the Counter Elite; Non-Aligned OR Democratic ruling party | National spirit New Young Afghan Movement (Political Power Gain +5%, Research Speed +3%, Daily Democracy Support +0.06) for 480 days; Abdul Hadi Dawi available (Consumer Goods Factories −10%, Economy Laws Cost −10%); Soraya Tarzi available (Research Speed +5%) |
| Parliamentary Democracy | Promote the Counter Elite; Not in civil war; 20%+ Democratic support; Fully independent OR has overlord; (Bypasses if already Democratic) | Civil war if Democratic support <50% (variable AFG_total_anti_democratic_size); Politics change to Democratic (100%); Remove Counter-Elite and King Zahir Shah spirits; Create Loyalist and Pashtun Militia templates; Provisional Government party name; Known as Kingdom of Afghanistan; King Zahir Shah (1) spirit; Provisional Government leader (Political Power Gain +5%, Stability +10%, Daily Unaligned Support +0.02) |
| Hold Elections | Parliamentary Democracy; Not in civil war | Event allows election of new country leader |
| Grant Refuge to Jadidists | Promote the Counter Elite; Non-Aligned OR Democratic ruling party | National spirit Pro-Democratic Influx (Political Power Gain +5%, Weekly Manpower +25, Daily Democracy Support +0.10) for 480 days; Abdurauf Fitrat available (Stability +5%, Research Speed +5%); Fayzulla Xo'jayev available (Political Power Gain +10%, Construction Speed +5%, Daily Democracy Support +0.08) |
| He Who Puts His Trust in God | Promote the Counter Elite; Not Communist; Not in civil war; Provisional Government not leader | +100 Political Power; Current leader gains He Who Puts His Trust in God (Political Power Gain +20%, Stability +5%, Daily Unaligned Support +0.03) |
| Education Reform | Parliamentary Democracy OR He Who Puts His Trust in God; Not in civil war | +1 Research Slot; Abdul Hai Habibi available (Research Speed +5%) |
| Curtail Anti-Democratic Influence | Hold Elections AND Education Reform | National spirit Curtail Anti-Democratic Movements (Daily Democracy Support +0.1) for 720 days |
| Concessions To Pashtuns | Curtail Anti-Democratic Influence | Replace Pashtunwali spirit with Pashtun Democracy (Political Power Gain +10%, Stability +25%, Daily Democracy Support +0.03); Mohammad Gul Khan Momand available (Stability +5%, War support +10%, Division Defense on core territory +5%) |
| Economic Modernization | Education Reform | 2× +50% Research bonus for Industry; Random state: +2 Building slots, +2 Civilian factories |
| Rapprochement with Non-Pashtuns | Economic Modernization | Remove Disgruntled Minority from all states; Stability +10%; Random employed army leader gains Desert Fox trait (Desert Movement +5%, Attack +10%, Defense +10%) |
| Defending the Nation | Rapprochement with Non-Pashtuns; At least 6 Civilian factories | Random state: +2 Building slots, +2 Military factories; National spirit Defending the Nation (Division training time −10%, Military factory construction speed +20%, Land fort construction speed +10%, Dockyard construction speed +20%) for 730 days |
| Recruit Foreign Experts | Education Reform AND He Who Puts His Trust in God | James Smith available (Military factory construction speed +10%, Dockyard construction speed +10%, Fuel silo construction speed +10%); Robert Johnson available (Consumer Goods Factories −5%, Production efficiency cap +5%); John Stevens available (Civilian to Military Factory conversion cost −20%, Supply Hub construction speed +10%) |
| Seek American Aid | Recruit Foreign Experts | Accepts American funds; prevents faction joining for 210 days; National spirit Accepted American Investment (Consumer Goods Factories −15%, Construction Speed +20%; Cannot join factions) for 210 days; if in faction and not UK faction, leave faction |
| Declare a Republic | Concessions To Pashtuns AND Defending the Nation; 50%+ Democratic support | Remove King Zahir Shah spirit; Event The Future of Afghanistan (choose new nation identity, may alter core states) |
| Sinkiang Intervention | Defending the Nation; Sinkiang exists, not Communist, not faction member, not Afghan puppet; (Bypasses if already at war with Sinkiang) | War goal (Puppet casus belli) against Sinkiang |
| Follower of Islam | Defending the Nation AND Seek American Aid | Current leader gains Follower of Islam (Stability +5%, Division Attack on core territory +10%, Division Defense on core territory +10%) |

### Forge a National Identity / Visit Foreign Capitals Sub-branch

Foreign opinion sub-branch shared between democratic and historical paths. Builds national identity and foreign relations.

| Focus | Prerequisites | Effects |
|---|---|---|
| Forge a National Identity | Expand the King's Power-base OR Biding Our Time; Fully independent | National spirit Constructing a National Identity (Political Power Gain −5%, Stability −5%, Ideology drift defense −15%) for 730 days; Upon completion, gain A Nation United (Political Power Gain +10%, Recruitable population +1%, Stability +15%, Division Defense on core territory +10%) |
| Visit Foreign Capitals | Expand the King's Power-base OR Biding Our Time; Fully independent | +100 Political Power; Every major country at peace with Afghanistan: Opinion +25; Democracy popularity +5% |
| Introduce National Service | Visit Foreign Capitals; Completed Maintain Quami OR Adopt Nufus | If has Nufus modifier: Recruitable population +10%; If has Quami modifier: Recruitable population +10% |
| Expand the Royal Guard | Visit Foreign Capitals; Not Communist; Completed Declare a Republic | Enable Royal Guard template editing; Random state: Create 2 Royal Guard units |

### Biding Our Time Sub-branch

Neutrality sub-branch under King Zahir with Mohammad Hashim Khan as leader. Balances between Allies and Axis, with opportunities for modernization without radical reform.

| Focus | Prerequisites | Effects |
|---|---|---|
| Biding Our Time | Support King Zahir [Mutually Exclusive] Expand the King's Power-base; Mohammad Hashim Khan is current leader; (Bypasses if Mohammad Hashim Khan not leader) | Mohammad Hashim Khan gains Cautious Modernizer (Stability +10%, Democratic Diplomacy acceptance −50, Fascist Diplomacy acceptance +50, Infrastructure construction speed +10%) |
| Secure German Investment | Biding Our Time; Not completed Seek British Investments OR completed Expel Allied Nationals; Germany exists, not at war; (Bypasses if Germany doesn't exist or at war) | Germany event for investment; if accepts: Random state: +1 Building slot, +1 Civilian factory and +1 Military factory; German Ideology Influence on the Rise (+0.02 daily) |
| Seek British Investments | Biding Our Time; Not completed Secure German Investment OR completed Expel Axis Nationals; UK exists, not at war; (Bypasses if UK doesn't exist or at war) | UK event for investment; if accepts: Random state: +1 Building slot, +1 Civilian factory and +1 Military factory; British Ideology Influence on the Rise (+0.02 daily) |
| Construct the Chak Dam | Secure German Investment OR Seek British Investments; Khyber Pass (1006) owned and controlled; (Bypasses if Khyber Pass lost) | Khyber Pass: +1 Dam (Max Factories +15%, Factories Energy Consumption −65%, Available Resources +10%, Construction Speed +15%) |
| Secure the Dynasty | Construct the Chak Dam | Unlock decision A Royal Successor; If has Sardar Shah Mahmud Khan: becomes advisor (Political Power Gain −20%, Stability +10%, Daily Unaligned Support +0.02); If has Sardar Shah Wali Khan: becomes advisor (Military factory construction speed +10%, Land fort construction speed +10%, Coastal fort construction speed +10%, Anti-air construction speed +10%, Synthetic refinery construction speed +10%) |
| Maintain Neutrality | Secure the Dynasty; Fully independent; Not in faction | National spirit Neutral Foreign Policy (Join faction tension limit +100%, Send volunteers tension limit +20%, Guarantee tension limit +100%, Embargo Tension Limit +250%; AI: Faction desire −100, Threat receptivity +1%) for permanent duration; Stability +20% |
| Expel Axis Nationals | Maintain Neutrality; Completed Secure German Investment; Not Fascist; Not ally of Germany | Every Axis member: Opinion −50; Every Allied member at peace: Stability +5%; Remove Fascism on the Rise spirit if present |
| Expel Allied Nationals | Maintain Neutrality; Completed Seek British Investments; Not Democratic; Not ally of UK or USA | If UK is Democratic faction leader or USA is Democratic faction leader: Every Allied member: Opinion −50; Stability +5%; Remove Democracy on the Rise spirit if present |

## Against Kabul Branch

Opposition branch exploring alternate monarchist and Islamic leadership paths. Mutually exclusive with Support King Zahir.

| Focus | Prerequisites | Effects |
|---|---|---|
| Against Kabul | [Mutually Exclusive] Support King Zahir; Non-Aligned ruling party | Fascism popularity +10%; +100 Political Power; Modify King Zahir Shah spirit to King Zahir Shah (Negative) variant (Stability +5%, Political Advisor Cost +25%) |

### Contact Amanullah Loyalists Sub-branch

Fascist monarchist sub-branch bringing back reformist Amanullah Khan as leader. Enables aggressive expansion into India, Central Asia, Iran, Iraq, and Middle East with goal of becoming savior of Islam and achieving Pashtunistan Ascendancy.

| Focus | Prerequisites | Effects |
|---|---|---|
| Contact Amanullah Loyalists | Against Kabul; [Mutually Exclusive] Remember the Khost Rebellion | Requires unlock via event chain | Opens path to reformist Amanullah Khan; Enables modernization and aggressive expansion |

#### Request German Support / Contact Rural Maliks Sub-branch

Offers German support or rallies rural leaders in event of civil war.

#### Remember the Khost Rebellion Sub-branch

Alternative leader path to Amanullah Khan via other regional leaders. Creates Middle Eastern faction and calls Japan for aid.

| Focus | Prerequisites | Effects |
|---|---|---|
| Remember the Khost Rebellion | Against Kabul; [Mutually Exclusive] Contact Amanullah Loyalists | Offers alternative leaders to Amanullah Khan; Creates faction with Middle Eastern nations; Japan aid available |

##### Crown the Golden Emir Sub-branch

Crowns Faqir of Ipi as Emir of Afghanistan. Supports Central Asian rebels, demands North Western India, forms Emirate of Pashtunistan, grants war goals for Islamic states.

##### Crown the Bukharan Emir / Invite the Mughal Prince Sub-branch

Options to crown Sayyid Mir Muhammad Alim Khan (Bukharan Emir) or Mizra Khurshid Jah Bahadur (Mughal Emir). Enables Second Afghan Empire (Soviet expansion) or Timurid Empire reformation (reclaim historical borders).

## Maintain Quami / Adopt Nufus Branch

Military branch focused on army development and national spirit improvement.

| Focus | Prerequisites | Effects |
|---|---|---|
| Maintain Quami | (Mutually exclusive with Adopt Nufus) | Focuses on cavalry, irregular infantry, equipment capture |
| Adopt Nufus | (Mutually exclusive with Maintain Quami) | Enables infantry equipment, armor, plane purchases |

Both sides enable intelligence agency development and mountain battalion strengthening.

### Establish New Naval Bases Sub-branch

Provides dockyard and naval expansion upon gaining coastline.

| Focus | Prerequisites | Effects |
|---|---|---|
| Establish New Naval Bases | (conditional on gaining coastline) | Dockyard and naval expansion |

## Align With the Allies / Pursue Our Own Agenda / Seek Alternative Partnerships Branch

Foreign policy branch enabling configuration of international alignment and partnerships with Allies and Axis.

**Allied Path:** Enables Operation Countenance participation, expansion into Iran, Khorasan buffer state establishment, territory gains from Pakistan.

**Central Path:** Choice between confederating with or conquering Pakistan.

**Axis Path:** German and Italian military bonuses; culminates in Kabul Conference.

## The Saadabad Pact Branch

Joint branch shared with Iraq, Iran, and Turkey. Builds up The Saadabad Pact national spirit with industry and military bonuses through coordinated regional development.

