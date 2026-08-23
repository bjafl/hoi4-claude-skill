---
title: Canadian National Focus Tree
category: focus-trees
tags: [Canada, national focus, political, industrial, military, naval, air, patriation, commonwealth, fascism, communism]
game_version: "1.19"
dlc: [Arms Against Tyranny, Götterdämmerung, La Résistance]
sources:
  - https://hoi4.paradoxwikis.com/Canadian_national_focus_tree
---

## Summary

Canada begins 1936 weakened by the Great Depression and conscription crisis, but its massive industrial potential and late-game mobilization make it a late bloomer. Six main branches (Industrial, Army, Commonwealth, Patriation, Air, Naval) can overlap but are gated by war/world tension. Key strategic choice: Patriation locks out Commonwealth ties, forcing selection between Allies (historical) or independence (democratic/fascist/communist).

See [Canada](../05-countries/canada.md) for the country's 1936 starting profile. See [National Focus and Continuous Focus](../01-mechanics/national-focus.md) for generic/continuous focuses.

## Industrial and Internal Politics Branch

The foundational branch for economic recovery and war production. Unlocks industrial capacity, resource extraction, and Depression relief. Most focuses gated by >20% World Tension (Defense of Canada Regulations) or active war (War Bonds); enables industrial expansion and conscription paths.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| Rowell-Sirois Commission | None | — | Political Power: +120 |
| Crown Corporations | None | — | Political Advisor: C.D. Howe (Captain of Industry). Infrastructure/Civilian Factory/Railway/Synthetic Refinery construction: +10.0% |
| National Housing Act | Rowell-Sirois Commission + Crown Corporations | — | Bypasses if no civilian factory slots. Random state: +3 Building slots, +1 Civilian Factory. If Mackenzie King leads: Stability: +10.0%, Civilian Factory construction: +5.0% |
| Dollar-A-Year Men | National Housing Act | — | National spirit (Political Advisor Cost: −33%). 1× 100% Industry research bonus |
| Canadian Pacific Railway | Rowell-Sirois Commission | — | Bypasses if no British Columbia (473) or Prince Rupert (471). Two random states: +1 Infrastructure. Railway level 1 from BC to Prince Rupert. Industrial Concern: Canadian Pacific Railway (Railway Company). Industrial Research Speed: +5%, Train production cost: −25.0%, Armor: +15%, Supply Hub/Railway construction: +15.0% |
| Maritime Colonial Railway | Canadian Pacific Railway + controls Nova Scotia (464), New Brunswick (465), Saint Lawrence (468) | — | Railway level 1 in Saint Lawrence, Nova Scotia, New Brunswick. Random state: +2 Building slots, +2 Civilian Factories |
| Retool Angus Shops | Canadian Pacific Railway + Bits and Pieces Program | — | Bypasses if no military factory slots. Random state (priority New South Wales/Victoria): +2 Building slots, +2 Military Factories |
| Imperial Oil | Retool Angus Shops + controls Alberta (470), Prince Rupert (471), N.W Territories (472), Nunavut (683) | — | Alberta: +2 Oil. Prince Rupert/N.W Territories/Nunavut: +4 Oil each |
| Defense of Canada Regulations | >20% World Tension | — | National spirit (Foreign Subversive activities: −50%; opposing ideology daily support: −0.01 each). Varies by ruling party ideology |
| War Bonds | At war | — | National spirit (Consumer Goods Factories factor: −10.0%) |
| Department of Munitions and Supply | Crown Corporations + Defense of Canada Regulations + War Bonds | — | Bypasses if no military factory slots. Two random states: +1 Building slot, +1 Military Factory each |
| National Resources Mobilization Act | Defense of Canada Regulations | — | National spirit (Recruitable Population: +5%, Stability: −5.0%, Factory/Dockyard output: +2.0%) |
| Wartime Prices and Trade Board | Defense of Canada Regulations | — | National spirit (Max Factories in State: +10%, Resources to Market: −5%) |
| Bits and Pieces Program | Department of Munitions and Supply | — | National spirit (Production efficiency growth/base: +5.0%, Factory/Dockyard output: +4.0%) |
| Fund the National Research Council | Department of Munitions and Supply + National Resources Mobilization Act | — | Gain 1 Research Slot |
| Mine the Shield | National Resources Mobilization Act | — | Bypasses if no state connected to capital. Random state (priority Prince Rupert, N.W Territories, Nunavut): 2 Steel, 1 Chromium |
| Canada Wheat Board | Wartime Prices and Trade Board | — | Modifies Great Depression spirit: Consumer Goods Factories: −25.0%, Factory/Dockyard output: +10.0% (or grants Booming Economy if already modified) |
| Victory Aircraft Limited | Department of Munitions and Supply | — | Bypasses if no military factory slots. Two random states (priority Southern/Northern Ontario): +2/+1 Building slots, +2/+1 Military Factories |
| Alberta Coal Towns | Mine the Shield + Canada Wheat Board | — | Bypasses if no civilian factory slots. Alberta (470): +3 Building slots, +3 Civilian Factories, +8 Coal production |
| Commit to the War | Canada Wheat Board + At war | — | National spirit (Recruitable Population: +5.0%). Necessary for any conscription law above Volunteer Only |
| John Inglis and Company | Bits and Pieces Program | — | Bypasses if no military factory slots. Two random states: +2/+1 Building slots, +2/+1 Military Factories |
| Polymer Corporation | Victory Aircraft Limited + Fund the National Research Council | — | Bypasses if no synthetic refinery slots. If Synthetic Oil Experiments not researched: instant research + 2.0 AoT reduction. Otherwise: 100% bonus (next 1). Two random states: +1 Building slot, +1 Synthetic Refinery each |
| National Steel Car | Alberta Coal Towns | — | Bypasses if no civilian factory slots. Two random states: +2 Building slots, +2 Civilian Factories each |
| Send in the Zombies | Commit to the War | — | National spirit (Recruitable Population: +1.0%, Recruitable Population Factor: +15.0%) |
| If Day | John Inglis and Company + Victory Aircraft Limited | — | Modifies War Bonds spirit (unchanged effects). Winnipeg occupation simulation |
| Defense Research Grants | If Day + independent + >50 Factories | — | Gain 1 Research Slot |
| Uranium Mining | Polymer Corporation OR National Steel Car | — | If Atomic Research 2× not researched: 2× 50% Nuclear technology bonus, +25% Nuclear Research breakthrough. Otherwise: +75% Nuclear Research breakthrough |
| Long Branch Arsenal | Send in the Zombies | — | 1× 100% Infantry Weapons and Support Artillery research bonus |
| Independent Command | Send in the Zombies + Red Deer Training Camp | — | Army experience: +50. 1× 50% Land Doctrine cost reduction |
| Forced Quebec Conscription | Long Branch Arsenal + Independent Command | **Compromise With Quebec** | Removes Conscription Crisis among French Canadians spirit. Triggers MTTH events tfv_canada.50-53 |
| Compromise With Quebec | Long Branch Arsenal | **Forced Quebec Conscription** | Replaces Conscription Crisis with Conscription Crisis Mended (Recruitable Population: +20.0%) |
| War Fueled Economy | National Steel Car + If Day | — | Modifies Great Depression: Consumer Goods Factories: −25.0%, Factory/Dockyard output: +10.0% (or Booming Economy). Three random states: +1 Building slot, +1 Military Factory each |

## Army Modernization Branch

Ground forces research and training bonuses. Earlier tiers independent; later tiers gate on Send in the Zombies from industrial branch.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| Army Modernization | None | Army experience +50, 1× 50% Land Doctrine cost reduction | Entry focus |
| Canadian Infantry Corps | Army Modernization | 1× 100% Infantry Weapons and Support Artillery research bonus | Corps formation |
| CMP Truck | Army Modernization | 2.0 year AoT reduction + 200% research bonus for Truck (next 1 research) | Canadian truck design |
| The Walkie-Talkie | Canadian Infantry Corps | 1× 100% Electronics research bonus, 1× 100% Signal Company I–IV research bonus | Radio communication |
| Royal Regiment of Canadian Artillery | Canadian Infantry Corps | Land Warfare breakthrough +15.00%, 1× 100% Support Artillery research bonus | Artillery modernization |
| A Motorized Army | CMP Truck | 1× 100% Field Hospital I–IV, Logistics Company I–IV, Signal Company I–IV, Truck research bonus | Motorized warfare |
| Red Deer Training Camp | Royal Regiment of Canadian Artillery **or** A Motorized Army | Army experience +30, 1× 50% Land Doctrine cost reduction | Main training center |
| 1st Canadian Parachute Battalion | The Plan **or** A Motorized Army | 1× 100% Airborne technology research bonus; if Arms Against Tyranny DLC: 2× 50% Special Forces Doctrine cost reduction | Airborne forces (requires Arms Against Tyranny for doctrine discount) |
| The Black Devils | Red Deer Training Camp | 1× 100% Marine technology and Airborne technology research bonus | Special commando unit |
| The Rocky Mountain Rangers | Red Deer Training Camp | 1× 100% Mountaineers technology research bonus | Western home defense |
| The Valentine Tank | Red Deer Training Camp | Land Warfare breakthrough +50.00%, 1× 100% Armour technology research bonus, 2.0 year AoT reduction + 100% Medium Tank research bonus (next 1) | British tank license |

## Strengthen the Commonwealth Ties Branch

The historical path: maintains Commonwealth ties, unlocks shared research, and builds industrial/resource production with allied support.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| Strengthen the Commonwealth Ties | Mutually exclusive with Patriation; UK ruled party aligned with Canada; Canada in Commonwealth Research tech-sharing group | Technology sharing bonus from Commonwealth Research +3.00%; UK gains Opinion +35 toward Canada | Historical pro-British path |
| Shadow Factories | Strengthen the Commonwealth Ties; >5% world tension | Three random states: +1 building slot, +1 military factory each | Bypassed if no military factory slots |
| Montreal Laboratory Collaboration | Strengthen the Commonwealth Ties; in faction with UK; member of Commonwealth Research group | Technology sharing bonus from Commonwealth Research +5.00% | Scientific cooperation |
| The Plan | Shadow Factories | National spirit: Ace generation chance +10.00%; all aircraft types (fighters, CAS, naval bombers, tactical/strategic bombers, transports): Air Range +10%, Attack/Bombing +5% | Air training cooperation |
| Camp X | Montreal Laboratory Collaboration + Permanent Joint Defense Board | If La Résistance DLC: +10 Decryption Speed; else 1× 100% Decryption methods **or** Computing technology research bonus | Spy training near Oshawa |
| Supply the Empire | The Plan + Camp X | 3× 100% Excavation technologies research bonus | Raw material export |
| Aluminium Company of Canada | Supply the Empire; controls Saint Lawrence (468), Northern Ontario (682), Maurice (863) | Saint Lawrence: +8 aluminum; Northern Ontario: +20 aluminum; Maurice: +8 aluminum | Aluminum production |
| Turner Valley Oilfield | Supply the Empire; controls Alberta (470) | Alberta: +36 oil | Oil field development |

## Patriation Branch

Independence path: Canada severs UK ties and chooses its political direction (democratic, fascist, or communist). Multiple sub-paths with distinct focuses.

### Democratic (North American Alliance)

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| Patriation | Mutually exclusive with Strengthen the Commonwealth Ties; Britain not enforced loyalty | National spirit: Daily autonomy progress +1.00%; UK gains Opinion −40; hidden news event triggers after 3 hours | Independence declaration |
| Permanent Joint Defense Board | Patriation; mutually exclusive with Burn the Royal Portraits and Swastika Clubs; independent; not at war with USA; US ruling party aligned with Canada; not at war with UK; Britain not enforced loyalty | Leave Allies faction; Opinion +25 with USA; Guarantee USA | Requires USA as ally |
| North American Alliance | Permanent Joint Defense Board; independent; Britain not enforced loyalty; bypassed if in faction with USA | Event to US: if faction leader, Canada seeks alliance; else if same ideology, Canada requests alliance | North American bloc |
| Habakkuk Carrier | North American Alliance; Britain not enforced loyalty | Naval Engineering breakthrough +50.00%; if Götterdämmerung DLC: 1× 50% Pykrete Tech research bonus; else 1× **or** 2× 100% Carrier models research bonus. National spirit: Ice Aircraft Carrier research speed +100, Ice Carrier production cost −15.00% | Anti-submarine carrier project |
| Refuge for Scientists | North American Alliance; in faction with USA; Britain not enforced loyalty | Canada + USA join 'US Research' tech-sharing group; National spirit Secret Weapons Initiatives: Special Project Speed +5.00% | Scientific collaboration |
| The Canadian Citizenship Act | Supply the Empire + North American Alliance | National spirit: Recruitable population Factor +10%, Surrender Limit +15.00%, Research Speed +5.00%, Daily autonomy progress +0.1 | Establish independent citizenship |
| The Newfoundland Act | The Canadian Citizenship Act; Newfoundland (331) and Labrador (332) owned by overlord (Canada or UK) or US faction member with opinion ≥51 | Event to overlord/UK: Canada wishes union with Newfoundland | Annex eastern territories |

### Fascist (Join Germany/Mexico Route)

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| Swastika Clubs | Patriation + independent + Britain not enforcing loyalty | **Burn the Royal Portraits, Permanent Joint Defense Board** | Autonomy: +100. National spirit (Daily Democracy support: −0.10, Fascism support: +0.20) |
| Support the Blue Shirts | Swastika Clubs + independent + ruling party fascist + Britain not enforcing loyalty | — | Modifies Swastika Clubs (Recruitable Population: +2.0%, War support: +5.0%) |
| Join Germany | Support the Blue Shirts + ruling party fascist + not at war with Germany + no war goals vs Germany + Britain not enforcing loyalty + Germany not a subject + Germany fascist | **Support a Synarchist Baja** | Germany gets event "Canada Seeks Alliance" |
| Support a Synarchist Baja | Support the Blue Shirts + ruling party fascist | **Join Germany** | Modifies Swastika Clubs (Max volunteer force divisions: +1, Divisions required for volunteers: −100%). Mexico gets Synarchist Support Surge spirit for 720 days (Stability: −5.0%, Daily Fascism support: +0.1) |
| Pinion the Eagle | Join Germany + Britain not enforcing loyalty | — | Instantly builds level 3 Land forts along non-faction borders. Instantly builds level 3 Coastal forts along coasts |
| Skewer the Eagle | Support a Synarchist Baja + ruling party fascist + Mexico fascist + not at war with Mexico + Britain not enforcing loyalty | — | Set rule: Can Create Factions. If Mexico fascist, Mexico gets "A Plan for Dominance" event |
| Concessions for Labrador and Newfoundland | Skewer the Eagle OR Pinion the Eagle OR Introspective Communism + at peace with UK + BC owned/controlled + UK owns Newfoundland/Labrador + Britain not enforcing loyalty | **Demand Labrador and Newfoundland** | UK gets "Canada Offers Concessions for Newfoundland" event. More likely if UK at war, high opinion of CA, or >25% surrender. If accept: UK gains rights to all BC resources |
| Demand Labrador and Newfoundland | Skewer the Eagle OR Pinion the Eagle OR Introspective Communism + UK owns Newfoundland/Labrador + Britain not enforcing loyalty | **Concessions for Labrador and Newfoundland** | UK gets "Canada Demands Labrador and Newfoundland" event. Very unlikely unless desperate |
| Defense Scheme No. 1 | Skewer the Eagle OR Pinion the Eagle OR Introspective Communism + independent + Britain not enforcing loyalty + USA not subject + USA not in CA faction | — | If ruling party fascist: Gains Annex war goal vs USA. Otherwise: Gains Topple Government war goal vs USA |

### Communist (Revolution + Soviet Alliance)

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| Burn the Royal Portraits | Patriation + Britain not enforcing loyalty | **Permanent Joint Defense Board, Swastika Clubs** | Autonomy: +100. National spirit (Daily Democracy support: −0.10, Communism support: +0.20) |
| Communist Labor Total War Committee | Burn the Royal Portraits + independent + ruling party communist + Britain not enforcing loyalty | — | Modifies Communist Ideals (Factory/Dockyard output: +2.0%, Daily Democracy support: −0.10, Communism support: +0.20) |
| Mend Relations with the Trotskyites | Communist Labor Total War Committee + Britain not enforcing loyalty | **Defense Scheme No. 2, Supply the Red Army** | National spirit (Recruitable Population: +15%, Stability: +15.0%). If Soviet leader is Trotsky: Soviet opinion +50. Otherwise: Soviet opinion −30 |
| Reactivate the Farmer's Unity League | Mend Relations with the Trotskyites + at war + not in civil war + full control of Manitoba (467), Saskatchewan (469), Alberta (470) | — | Saskatchewan: +2 Building slots. Alberta: +2 Building slots. Manitoba: +1 Building slot. Modifies Great Depression (Consumer Goods Factories: −15.0%, Factory/Dockyard output: +10.0%) or grants Booming Economy |
| Introspective Communism | Mend Relations with the Trotskyites + Britain not enforcing loyalty | — | If not at war and in faction: leaves faction. Set rule: Cannot join factions. Modifies Communist Ideals (Subversive activities cost: −50%, Factory/Dockyard output: +10.0%, Daily Democracy support: −0.10, Communism support: +0.25) |
| Spirit of the True Revolution | Introspective Communism + Britain not enforcing loyalty | — | National spirit (Non-core Manpower: +5.0%, Training time: −20.0%, Resistance Target: −5%, Land Doctrine Cost: −10.0%) |
| Defense Scheme No. 2 | Communist Labor Total War Committee + Britain not enforcing loyalty + (USA at war with Japan OR USA has war goal vs Japan OR USA justifying vs Japan OR Japan has/justifying vs USA) | **Mend Relations with the Trotskyites, Supply the Red Army** | Instantly builds level 3 Land forts along non-faction borders. Instantly builds level 3 Coastal forts along coasts |
| Canada United | Defense Scheme No. 2 + Britain not enforcing loyalty | — | Set rule: Can Create Factions |
| Supply the Red Army | Communist Labor Total War Committee + not at war with USSR + no war goals vs USSR + not justifying vs USSR + ≥500 Infantry Equipment in stockpile + Britain not enforcing loyalty + USSR exists + USSR communist | **Mend Relations with the Trotskyites, Defense Scheme No. 2** | Cannot be manually cancelled. Immediately sends 500 Infantry Equipment to USSR. CA opinion of USSR: +25; +200 to AI strategy. USSR opinion of CA: +25; receives 500 Infantry Equipment. All non-communist nations: Trade relation with CA −50 |
| Join Comintern | Supply the Red Army + ruling party communist + independent + not at war with USSR + no war goals vs USSR + not justifying vs USSR + Britain not enforcing loyalty + major communist faction leader exists | — | USSR gets event "Canada Seeks Membership in the Comintern" |
| Support the World Revolution | Canada United OR Join Comintern + Britain not enforcing loyalty | — | Modifies Communist Ideals (Subversive activities cost: −50%, Factory/Dockyard output: +4.0%, Daily Democracy support: −0.10, Communism support: +0.20). Set rule: Can send volunteer forces |

## RCAF Station Borden Branch

Air force research, air bases, and radar/doctrine bonuses. Independent from other branches early; some focuses connect to earlier army/commonwealth tiers.

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| RCAF Station Borden | None | Air experience +25; random state with air base: +2 air bases; 1× 50% Air Doctrine cost reduction | Air corps establishment |
| We Have the Hurricane | RCAF Station Borden | 1× 100% Fighter models research bonus | British fighter license |
| The Pacific Coast Air Defense Radar System | RCAF Station Borden | Aerodynamics and Avionics breakthrough +25.00%, 1× 100% RADAR technology research bonus; if Radar project complete: random state with radar slot (priority British Columbia): +1 radar station; another random state with slot: +1 radar station | West coast radar chain |
| Commonwealth Air Training Plan | The Pacific Coast Air Defense Radar System **or** We Have the Hurricane | Air experience +25; random state with air base: +2 air bases; 1× 50% Air Doctrine cost reduction | Allied air training coordination |
| Fund Fairchild's Development | Commonwealth Air Training Plan | 1× 100% Tactical Bomber and Close Air Support models research bonus; if Arms Against Tyranny: unlock Fairchild Aircraft Ltd. (Naval Aircraft Designer) with +2500 funds; else unlock Fairchild Aircraft Ltd. (Aircraft Designer): Air Research Speed +15%, Naval Bomber/CV Naval Bomber/Carrier Fighter/Carrier CAS Range +10%, Attack/Naval Attack/Agility +10% | Quebec bomber production |
| Cookie Carriers | Commonwealth Air Training Plan | 1× 100% Strategic Bomber models research bonus; if Arms Against Tyranny: unlock Handley Page (Heavy Aircraft Designer) +1 size, +500 funds; else unlock Handley Page (Aircraft Designer): Air Research Speed +15%, Strategic Bomber: Strategic Bombing +10% | Heavy bomber program |
| The Sabre Project | Cookie Carriers + Fund Fairchild's Development | Aerodynamics and Avionics breakthrough +50.00%, 2.0 year AoT reduction for Rocketry and Jet technology | Jet aircraft development |

## Halifax Shipyards Branch

Naval production, dockyards, and naval research bonuses. Two sub-paths: Escort Fleet (convoy defense) or Fleet in Being (large surface fleet threat).

| Focus | Prerequisites | Effects | Notes |
|---|---|---|---|
| Halifax Shipyards | None | Navy experience +25; random coastal state with ≥3 building slots (priority Nova Scotia 464): +3 building slots, +3 naval dockyards | Naval establishment |
| Destroyer Effort | Halifax Shipyards | Navy experience +25, 2.0 year AoT reduction + 100% research bonus for Destroyer models | Submarine hunting |
| Light Cruiser Effort | Destroyer Effort; mutually exclusive with Heavy Cruiser Effort | 2.0 year AoT reduction + 50% research bonus for Cruiser Models, 1× 50% Light Batteries research bonus | Cruiser-centric fleet |
| Heavy Cruiser Effort | Destroyer Effort; mutually exclusive with Light Cruiser Effort | 1.0 year AoT reduction + 100% research bonus for Heavy Cruiser Models, 1× 50% Heavy Batteries research bonus | Capital cruiser fleet |
| Escort Fleet | Light Cruiser Effort **or** Heavy Cruiser Effort; mutually exclusive with Fleet In Being | Navy experience +25, Naval Engineering breakthrough +15.00%; if has Screen subdoctrine Convoy Escort: +20.00% Mastery for 180 days; else +10.00% Mastery for Screens track; 2× 25% Naval Doctrine cost reduction | Convoy protection focus |
| Fleet In Being | Light Cruiser Effort **or** Heavy Cruiser Effort; mutually exclusive with Escort Fleet | Navy experience +25, Naval Engineering breakthrough +15.00%, +10.00% Mastery for all Fleet in Being tracks for 180 days, 2× 25% Naval Doctrine cost reduction | Large fleet threat doctrine |
| Degauss Ship Hulls | Escort Fleet | If Degaussing not researched: instantly research; else 1× 50% Mine warfare research bonus | Magnetic mine protection |
| Trade Fleet | Escort Fleet | National spirit Trade Fleet: Convoy production cost −25.00% | Merchant marine expansion |
| United Shipyards | Trade Fleet **or** Degauss Ship Hulls | Navy experience +25; random coastal state with ≥4 building slots: +4 building slots, +4 naval dockyards | Montreal shipyard expansion |

## Strategic Notes

### Early-Game Gating
- **War Bonds** and **Defense of Canada Regulations** (>20% World Tension) gate most high-value industrial focuses, forcing play around war declarations or global conflict.
- **Commit to the War** is a prerequisite for high conscription laws and **Send in the Zombies**, which gates late Army Modernization focuses.
- Early focuses (Rowell-Sirois Commission, Crown Corporations, Army Modernization, RCAF Station Borden, Halifax Shipyards) are immediately available.

### Patriation Mutual Exclusivity
Choosing **Patriation** immediately locks out **Strengthen the Commonwealth Ties**. This is a binary strategic choice: remain in Allies (historical, tech sharing, resources) or pursue independence. Patriation itself has three branches:
- **Democratic (North American Alliance):** Joins USA, collaborative focuses.
- **Fascist (Join Germany/Mexico):** Swastika Clubs → Blue Shirts → Germany/Mexico alliance, can invade USA.
- **Communist (World Revolution):** Revolution → optional Soviet alliance or isolation, can supply Red Army.

### Quebec Conscription
**Long Branch Arsenal** and **Independent Command** unlock two mutually exclusive resolution paths:
- **Forced Quebec Conscription:** Removes the malus but triggers historical events.
- **Compromise With Quebec:** Keeps the malus but gains +20.0% Recruitable Population bonus.

### DLC-Specific Content
- **Arms Against Tyranny:** Modifies **1st Canadian Parachute Battalion** (adds Special Forces Doctrine cost reduction), **Fund Fairchild's Development** (Fairchild as MIO instead of Aircraft Designer), **Cookie Carriers** (Handley Page as MIO), and other air/army focuses.
- **Götterdämmerung:** Modifies **Habakkuk Carrier** to include Pykrete Tech bonus if DLC enabled; otherwise grants dual Carrier model bonuses.
- **La Résistance:** Modifies **Camp X** to grant +10 Decryption Speed if DLC enabled; otherwise grants Decryption/Computing research bonus.

### Political Ideology Prerequisites
Several focuses require specific ruling parties:
- **Support the Blue Shirts:** Requires fascist government.
- **Communist Labor Total War Committee, Supply the Red Army, Join Comintern:** Require communist government.
- Some focuses check ideology alignment with other nations (e.g., **Permanent Joint Defense Board** requires USA ideologically aligned).

### Research and Industrial Payoff
The Industrial branch is the tree's power center: **National Housing Act**, **Victory Aircraft Limited**, **Polymer Corporation**, **National Steel Car**, and **War Fueled Economy** all add building slots. Combined with **Department of Munitions and Supply**, **John Inglis and Company**, and others, a well-played Canada can amass 20+ extra military factories and civilian factories by early-mid game, offsetting its late-game weakness.

### Cross-Branch Dependencies
- **Army Modernization** late tiers (1st Canadian Parachute Battalion) require **The Plan** from the Commonwealth air training branch (OR A Motorized Army).
- **Camp X** requires **Permanent Joint Defense Board** (democratic path only).
- **Defense Research Grants** requires **If Day**, locking advanced research into industrial completion.
