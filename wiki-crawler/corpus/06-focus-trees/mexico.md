---
title: Mexican National Focus Tree
category: focus-trees
tags: [mexico, national focus tree, economic, political, military, industrial, oil, fascism, communism, democracy]
game_version: "1.19"
dlc: [Arms Against Tyranny]
sources:
  - https://hoi4.paradoxwikis.com/Mexican_national_focus_tree
---

## Summary

Mexico has a unique national focus tree split into two major branches: the **National Bank Branch** (industrial, caudillo, communist paths) and the **Plan of Agua Prieta Branch** (political ideology shifts and regional conquest). The tree emphasizes balancing economic development, church influence, and political ideology, with distinct paths toward Democracy (historical), Fascism (Synarchist or Gold Shirt), or Communism. See [Mexico](../05-countries/mexico.md) for the country's 1936 starting profile.

See [National Focus and Continuous Focus](../01-mechanics/national-focus.md) for generic/continuous focuses and focus mechanics.

## National Bank Branch

The industrial, infrastructure, and communist-leaning branch focusing on economic development and managing caudillo tensions.

### Main Industrial Chain

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **National Bank** | None | — | Banco de México available as Industrial Concern (+15% Industrial Research Speed, −25% Economy Laws Cost) |
| **Agricultural Credit Bank** | National Bank | Liberalize the Banking Sector | Alberto J. Pani advisor available (Captain of Industry: +10% Infrastructure, +10% Civilian factory, +10% Refinery construction speed) |
| **Confederation of Mexican Workers** | Agricultural Credit Bank | — | +120 Political Power; Vicente Lombardo advisor available (Ambitious Union Boss: −15% Consumer Goods Factories, +0.10 daily communism support) |
| **Rent Freeze** | Confederation of Mexican Workers | — | +120 Political Power, +5.00% Stability |
| **Ejido Worker Militias** | Rent Freeze; requires Atheist State, Weak Church, or Assertive Church | — | Stages Church Power transitions (Catholic State → Powerful Church → Assertive Church → Weak Church → Atheist State); varying Stability and Factory output modifiers; Recruitable Population +2.00%, +0.10 daily Communism support |
| **Party of the Revolution** | Ejido Worker Militias; >40% PCM support; not in civil war; hasn't completed Institutional Revolution, Catholic Politics, Crusade Against Atheism, Revanchist Revolution, or Communist Revolution | — | Communism support +10.00%, Stability +5.00%, War support +5.00%; if Lázaro Cárdenas leads: Infrastructure & Civilian factory construction +10.00%; otherwise Plutarcho E. Calles becomes Non-Aligned leader; PCM becomes ruling party |
| **Rural Infrastructure** | Agricultural Credit Bank | — | Add 1 Infrastructure to each of: Veracruz (477), Guerrero (485), Jalisco (478), Tamaulipas (479), Coahuila (480), Durango (481) if controlled |
| **Peripheral Infrastructure** | Rural Infrastructure | — | Add 1 Infrastructure to each of: Oaxaca (476), Chiapas (475), Yucatan (474), Baja California (484), Chihuahua (482), Sonora (483) if controlled |
| **Rural Schools** | Peripheral Infrastructure | — | Gain 1 Research Slot |
| **Liberalize the Banking Sector** | National Bank | Agricultural Credit Bank | Luis Montes de Oca advisor available (Financial Expert: −15% Consumer Goods Factories); reduces Caudillo Tensions (Very High → High → Moderate → Low progression, each with Stability bonuses) |
| **Strike Breaking** | Liberalize the Banking Sector | — | National spirit Strike Breaking (+10.00% Factory output) |
| **Urban Development** | Strike Breaking | — | Add 2 Infrastructure to Mexico City (277), 1 each to Veracruz (477), Jalisco (478), Guerrero (485) |
| **Científico Camarilla** | Urban Development | — | Gain 1 Research Slot |
| **End Land Reform** | Liberalize the Banking Sector | — | −5.00% Stability, +200 Political Power; reduces Caudillo Tensions |
| **Privatization** | End Land Reform | — | Add 1 Building Slot each to Mexico City (277), Veracruz (477), Guerrero (485), Jalisco (478), Tamaulipas (479), Coahuila (480); reduces Caudillo Tensions |
| **Caudillo Private Armies** | Privatization | — | National spirit Caudillo Private Armies (+1.00% Recruitable Population, +5.00% War support); reduces Caudillo Tensions |
| **Support General Cedillo** | Caudillo Private Armies | Arrest General Cedillo (mutually exclusive); requires General Cedillo not revolted | Saturnino Cedillo Martínez becomes Field Marshal (Chief of Army, Army Offense Expert: +10.0% Division Attack); removes Caudillo Tensions national spirit |
| **Arrest General Cedillo** | Purge the Bureaucracy | Support General Cedillo (mutually exclusive); requires General Cedillo not revolted | War support +5.00%; removes Caudillo Tensions national spirit |

### Military Budget Review Sub-branch

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Military Budget Review** | National Bank | — | 1× 100% research bonus Infantry Weapons & Support Artillery; Manuel Ávila Camacho advisor (War Industrialist: +10% Military factory, +10% Naval dockyard, +10% Fuel silo construction, −25% Conscription Laws Cost) |
| **Gulf Coast Naval Yards** | Military Budget Review | — | Add 1 Building Slot + 1 Naval dockyard each to Tamaulipas (479), Veracruz (477); if Arms Against Tyranny enabled: ASTIMAR Golfo available (Battle Line Ship Builders, +500 Funds, Carrier Armor +50% HP +10%, Capital Ship Armor +10% Heavy Attack +10%) |
| **Pacific Coast Naval Yards** | Military Budget Review | — | Add 1 Building Slot + 1 Naval dockyard each to Guerrero (485), Jalisco (478); if Arms Against Tyranny enabled: ASTIMAR Pacifico available (Task Force Ship Builders, +500 Funds, Carrier Deck Size +25% Armor −15% Max Range +25%, Capital Ship Max Range +25%, Screen Max Range +25%, Submarine Max Range +25%) |
| **Brown Water Navy** | Gulf Coast Naval Yards OR Pacific Coast Naval Yards | — | National spirit Brown Water Navy (+10.0% Escort efficiency); 1× 50% Naval Doctrine cost reduction, 1× 100% Cruiser models research bonus |
| **Blue Water Navy** | Brown Water Navy | Raiding Navy (mutually exclusive) | Replace Brown Water Navy with Blue Water Navy (+10.0% Escort efficiency, targeting surface power); 1× 50% Naval Doctrine cost reduction, 1× 100% Heavy Cruiser & Battleship research bonus |
| **Raiding Navy** | Brown Water Navy | Blue Water Navy (mutually exclusive) | Replace Brown Water Navy with Raiding Navy (+10.0% Convoy Raiding efficiency); 1× 50% Naval Doctrine cost reduction, 1× 100% Submarine & Battlecruiser research bonus |
| **Heroic Military College** | Military Budget Review | — | +30 Army experience; 1× 50% Land Doctrine cost reduction; Manuel Pérez Treviño theorist available (Superior Firepower Expert: −15% Army experience gain, +0.05% daily Army experience) |
| **Weapons Modernization** | Heroic Military College | — | 1× 100% Infantry Weapons research bonus, 1× 100% Support Artillery research bonus |
| **Tank Workshops** | Weapons Modernization | — | 1× 100% Armor technology research bonus; +50.00% Land Warfare breakthrough progress; if Arms Against Tyranny enabled: Talleres Generales de Arma available (Standardized Production, +500 Funds, Armor Reliability +5%) |
| **Aviation Workshops** | Heroic Military College | — | 1× 100% Aircraft research bonus, 1× 50% Air Doctrine cost reduction; +25.00% Aerodynamics and Avionics breakthrough; if Arms Against Tyranny enabled: Talleres Nacionales de Construcciones available (General Aircraft Designer, +500 Funds, Fighter/Carrier Fighter Agility +10% Max Speed +10%) |
| **Military Aviation Specialists** | Aviation Workshops | — | 1× 100% Aircraft research bonus, 1× 50% Air Doctrine cost reduction; +50.00% Aerodynamics and Avionics breakthrough |
| **Army Expansion Program** | Tank Workshops AND Military Aviation Specialists | — | Add 1 Building Slot + 1 Military factory each to Jalisco (478), Mexico City (277), Veracruz (477); if not at war: −5.00% Stability |
| **Heavy Artillery** | Army Expansion Program | Aerial Artillery (mutually exclusive) | National spirit Heavy Artillery (+10% Towed Artillery Soft Attack, +10% Towed Rocket Artillery Soft Attack) |
| **Aerial Artillery** | Army Expansion Program | Heavy Artillery (mutually exclusive) | National spirit Aerial Artillery (+15% Close Air Support Ground Attack, +15% Tactical Bomber Ground Attack) |

### Oil Field Expansion Sub-branch

Foreign relations and oil policy branch, with paths toward US/UK alignment or nationalization.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Oil Field Expansion** | Rural Schools OR Científico Camarilla | — | Add 4 Oil production each to: Oaxaca (476), Veracruz (477), Tamaulipas (479), Coahuila (480) |
| **Royal Dutch Shell** | Oil Field Expansion; at peace with UK | Nationalize the Oil Fields | Add 4 Oil to Coahuila (480); 2× 100% Synthetic resources research bonus; Royal Dutch Shell available (Refining Concern: +5% Industrial Research Speed, +10% Synthetic Resources Research Speed, −25% Trade Laws Cost); UK loses resource rights to Coahuila |
| **Community of Nations** | Royal Dutch Shell; fully independent; at peace with UK; bypasses if UK doesn't exist or is subject | — | Opinion modifiers with UK (±15); if UK faction leader: Mexican Entry into Allies event; if UK in faction: faction leader gets "Mexico seeks to join" event; otherwise creates Community of Nations faction with UK |
| **Purchase Belize** | Community of Nations; fully independent; at peace with UK; UK owns British Honduras (311); bypasses if Mexico already owns it | — | UK receives "Sale of British Honduras" event |
| **Oil Revenue Reinvestment** | Royal Dutch Shell OR Nationalize the Oil Fields | — | Add 1 Building Slot + 1 Civilian factory each to Veracruz (477), Tamaulipas (479) |
| **Capital Reserves** | Oil Revenue Reinvestment | — | National spirit Capital Reserves (−50% License purchase cost, +25% License production speed) |
| **Nationalize the Oil Fields** | Oil Field Expansion | Royal Dutch Shell | If UK or US not at war with/subject to Mexico: −50 Trade relations; "Mexican Oil Nationalized" event; removes Oil Concessions spirit; Pemex available (Refining Concern: +5% Industrial Research Speed, +10% Synthetic Resources Research Speed, +10% Infrastructure construction); US loses resource rights to Tamaulipas, Coahuila, Veracruz, Oaxaca |
| **Compensation** | Nationalize the Oil Fields | German Resource Exchange, Oppose Yanqui Imperialism | +5.00% Stability; "Mexican Compensation" event if UK/US not at war/subject |
| **Liberty and Justice For All** | Compensation; fully independent; at peace with US; US in faction with UK; bypasses if US doesn't exist or is subject | — | Opinion modifiers with US (±15) |
| **Aztec Eagles** | Liberty and Justice For All; at peace with US; US at war | — | Can send volunteer forces rule; 1× 100% Aircraft research bonus, 1× 50% Air Doctrine cost reduction; Aztec Eagles opinion modifiers (Mexico +10 to US, US +10 to Mexico) |
| **International Peacekeepers** | Purchase Belize OR Aztec Eagles; not in offensive war | — | Can send volunteer forces rule; National spirit International Peacekeepers (−100.0% Divisions required for volunteer forces, +100.0% Justify War goal time); +0.10 daily Democracy support |
| **Oppose Yanqui Imperialism** | Nationalize the Oil Fields | German Resource Exchange, Compensation | +5.00% War support |
| **German Resource Exchange** | Nationalize the Oil Fields | Oppose Yanqui Imperialism, Compensation | — |

## Plan of Agua Prieta Branch

Political ideology and regional conquest branch, with multiple paths toward different government types.

### Main Political Chain

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Plan of Agua Prieta** | None (root of branch) | — | Unlocks political ideology choice branches |
| **Exile Calles** | Plan of Agua Prieta | — | Removes Plutarcho E. Calles from government; Lázaro Cárdenas available as advisor (Democratic Reformer: +10% Construction Speed) |
| **Purge the Bureaucracy** | Exile Calles | — | Removes Caudillo Tensions if present; enables Arrest General Cedillo path |

### Institutional Revolution Path (Historical Democracy)

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Institutional Revolution** | Purge the Bureaucracy; Lázaro Cárdenas (or substitute) current leader; not in civil war | Party of the Revolution, Catholic Politics, Crusade Against Atheism, Revanchist Revolution, Communist Revolution | Democracy support +10.00%, Stability +5.00%, War support +5.00%; if Cárdenas leads: becomes Democratic party leader "Protector of the Republic" (+10% Construction Speed, +5.00% Stability, +10.00% Factory output); Calles becomes Non-Aligned |
| **Jefe Máximo** | Institutional Revolution | Party of the Revolution | Political Power +10% gain, −25% Political Advisor cost; Calles becomes Democratic leader |
| **Ban Political Militias** | Jefe Máximo | — | Stability +5.00%; removes any paramilitary national spirits |
| **Depoliticized Army** | Ban Political Militias | — | Army experience +25, Stability +5.00%; removes Caudillo Tensions; 1× 50% Land Doctrine cost reduction |
| **Escuela Superior de Guerra** | Depoliticized Army | — | Army experience +50 |
| **Revolutionary Women** | Jefe Máximo | — | Recruitable Population +2.00%; available as Political Advisor: Juana Belén Gutiérrez de Mendoza (Politically Connected: +10% Recruitable Population growth) |
| **Reclaim the Revolution** | Institutional Revolution | — | War support +5.00%, Political Power +100 |

### Catholic Politics Path (Democratic Catholic State)

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Catholic Politics** | Purge the Bureaucracy; has Assertive Church or Powerful Church; not in civil war | Party of the Revolution, Institutional Revolution, Crusade Against Atheism, Revanchist Revolution, Communist Revolution | Democracy support +10.00%, Stability +10.00%, War support +5.00% (net stability boost due to church alignment); available advisor (Democratic Reformer) |
| **Catholic Social Teaching** | Catholic Politics | — | Recruitable Population +1.00%, Consumer Goods Factories −5.00%, Stability +5.00% |
| **Christero Commemoration** | Catholic Social Teaching | — | War support +5.00%, Political Power +50 |

### Crusade Against Atheism Path (Synarchist Fascism)

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Crusade Against Atheism** | Purge the Bureaucracy; has Powerful Church or Assertive Church; not in civil war | Party of the Revolution, Institutional Revolution, Catholic Politics, Revanchist Revolution, Communist Revolution | Fascism support +10.00%, War support +5.00%; if current leader becomes Fascist party leader (e.g., "Champion of Christendom"); Calles becomes Non-Aligned |
| **Synarchist State** | Crusade Against Atheism | — | Stability +5.00%, Recruitable Population +2.00%; available advisor with Fascist affiliation |
| **Synarchist Foreign Support** | Synarchist State | — | Opinion modifiers, potential German alignment |

### Revanchist Revolution Path (Gold Shirt Fascism)

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Revanchist Revolution** | Purge the Bureaucracy; has Weak Church or Atheist State; not in civil war | Party of the Revolution, Institutional Revolution, Catholic Politics, Crusade Against Atheism, Communist Revolution | Fascism support +10.00%, War support +5.00%, Stability +5.00%; Gold Shirt paramilitary spirit activated; Fascist leadership available |
| **Gold Shirt Paramilitaries** | Revanchist Revolution | — | National spirit Gold Shirt Paramilitaries (+5.00% War support, paramilitary bonuses); Recruitable Population +3.00% |
| **Paramilitaries to Armed Forces** | Gold Shirt Paramilitaries | — | Converts paramilitary into regular army; Division training time −15.00%, Recruitable Population maintained |

### Communist Revolution Paths

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Party of the Revolution** | Ejido Worker Militias (from National Bank branch); >40% PCM support; not in civil war | Institutional Revolution, Catholic Politics, Crusade Against Atheism, Revanchist Revolution, Communist Revolution | See National Bank Branch for details—this is the same focus reachable from either branch |
| **Communist Revolution** | Purge the Bureaucracy; >50% Communism support; not in civil war | Party of the Revolution, Institutional Revolution, Catholic Politics, Crusade Against Atheism, Revanchist Revolution | Communism support +10.00%, War support +5.00%; Red Shirt paramilitary activated; Communist leadership established |
| **Red Shirts** | Communist Revolution | — | National spirit Red Shirts (+5.00% War support, +2.00% Recruitable Population); Communism support +0.20 daily |
| **Leon Trotsky Invited** | Red Shirts; has completed "Invite Leon Trotsky" event/prerequisite | — | Leon Trotsky becomes available as Communist party leader if in exile; offers advanced military and ideological bonuses |

### Control the Army Sub-branch

Manages church power and military alignment.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Control the Army** | Plan of Agua Prieta | — | Army experience +50; enables military control paths |
| **Strengthen Church Authority** | Control the Army | Suppress Church Influence (mutually exclusive) | Replace Weak Church/Atheist State with Assertive/Powerful Church (stability and church power increase); available Advisor: (Church sympathizer) |
| **Suppress Church Influence** | Control the Army | Strengthen Church Authority (mutually exclusive) | Replace Powerful/Assertive Church with Weak Church/Atheist State (+10−20% Factory output; Communism support +0.10 daily) |

### March Southwards Sub-branch

War goals and regional conquest paths.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **March Southwards** | Institutional Revolution OR Catholic Politics OR Crusade Against Atheism OR Revanchist Revolution OR Communist Revolution | — | Unlocks war goal focuses against regional targets |
| **Reclaim Belize** | March Southwards | — | Justify War goal time −50.00% vs. United Kingdom for British Honduras (311) |
| **Reclaim Texas** | March Southwards; not at war with US; not subject to US | — | Justify War goal time −50.00% vs. United States for Texas states (375, 376, 377, 378) (requires deep commitment to expansionist path) |
| **Reclaim Panama** | March Southwards; not at war with US; not subject to US | — | Justify War goal time −50.00% vs. United States for Panama Canal state(s) |
| **Seize Guatemala** | March Southwards | — | Justify War goal time −50.00% vs. Guatemala for Central American states |
| **Conquer Central America** | Seize Guatemala (or similar regional focus chain) | — | War goals against El Salvador, Honduras, Nicaragua if progressed sufficiently |

## Notes on Branching Logic

- **Church Power Mechanics:** Multiple focuses transition Church national spirit state (Catholic State → Powerful Church → Assertive Church → Weak Church → Atheist State). Each state gates different ideological paths; Communism requires low Church power, Synarchist/Catholic paths require high Church power.
- **Caudillo Management:** The Liberalize/Support path vs. Agricultural/Arrest path represents two strategies for managing regional military strongmen; Support reduces Caudillo Tensions gradually, Arrest removes them all at once.
- **Oil Policy Divergence:** Nationalizing oil harms UK/US relations significantly but grants independence and Pemex; Royal Dutch Shell partnership maintains better relations with UK and provides research bonuses.
- **Ideology Locking:** Once a major ideology focus is taken (Institutional Revolution, Catholic Politics, Crusade, Revanchist Revolution, Communist Revolution or Party of the Revolution), other major paths are locked out, representing Mexico's political consolidation.
- **Arms Against Tyranny DLC:** Enables unique military industrial organizations (ASTIMAR, Talleres) with additional stat bonuses if enabled; base-game equivalents are weaker.
