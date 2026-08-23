---
title: Dutch National Focus Tree
category: focus-trees
tags: [netherlands, focus tree, colonial, political, military]
game_version: "1.19"
dlc: [Thunder at Our Gates, Arms Against Tyranny]
sources:
  - https://hoi4.paradoxwikis.com/Dutch_national_focus_tree
---

## Summary

The Netherlands has a detailed national focus tree covering colonial development, mainland industrialization, military rearmament, and four distinct political paths (fascist, communist, monarchist, and democratic). The tree is heavily colonial-focused, with options to relocate government to the East Indies if invaded. Multiple branches require DLC; the base game variant provides industrial colonial investment, while Thunder at Our Gates unlocks loyalty guarantees and additional colonial mechanics. See [National Focus and Continuous Focus](../01-mechanics/national-focus.md) for generic/continuous focuses. See [Netherlands](../05-countries/netherlands.md) for the country's 1936 starting profile.

---

## Obtain Foreign Colonial Investments Branch (Base Game)

Available only when Thunder at Our Gates DLC is disabled. Expands Dutch industry in colonies and allows government relocation to Dutch East Indies if capitulated.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| Obtain Foreign Colonial Investments | None | — | Unlocks decisions for temporary Consumer Goods and Construction Speed bonuses; permanent Oil Production +24 (East Indies), +24 (West Indies) |
| The Western Possessions | Obtain Foreign Colonial Investments + full control Curaçao (695), Suriname (309) | — | Curaçao, Suriname: +1 Infrastructure each |
| Expand Curaçao Oil Refineries | The Western Possessions + full control Curaçao + (World Tension >20% OR at war OR faction-specific conditions) + (Free Trade OR Export Focus) | — | Curaçao: +24 Oil, +2 building slots, +1 civilian factory, +1 synthetic refinery; 1×100% Synthetic resources research bonus |
| Open Second Paranam Bauxite Mine | Expand Curaçao Oil Refineries + full control Suriname + (at war OR faction-specific) + (Free Trade OR Export Focus) | — | Suriname: +24 Aluminum, +1 building slot, +1 civilian factory |
| Antilles Defenses | Expand Curaçao Oil Refineries + full control Curaçao | — | Curaçao: +3 Coastal fort, +2 Anti-air, +2 Air base, +2 Naval base (in province) |
| Pre-Empt Venezuelan Aggression | Antilles Defenses + not Shell-shocked/Aloof Neutrality spirits + Venezuela has offered protection | — | War goal vs Venezuela (Puppet Focus) |
| The Crown Jewel Colony | Obtain Foreign Colonial Investments + (full control West Java 335, Sumatra 672 OR is subject controlling them) | — | West Java, Sumatra: +1 Infrastructure each; if DEI is subject: −0.025% autonomy |
| Java | The Crown Jewel Colony + (full control West Java OR is subject) | — | West Java: +1 Infrastructure, +2 building slots, +2 civilian factories; if DEI subject: −0.05% autonomy |
| Reinforce Java | Java + (full control West Java OR is subject) | — | West Java: +3 Coastal fort, +2 Land fort; also add +3 Coastal fort, +2 Land fort; +2 Anti-air; if DEI subject: −0.025% autonomy |
| The "Foundations of Defense" | (Antilles Defenses OR Reinforce Java) + (full control West Java OR is subject OR Curaçao 695) + not Shell-shocked spirit | — | National spirit "The Foundations of Defense" (Light Hull, Cruiser production cost −10%); West Java: set Naval base Soerabaja to max; Curaçao: +2 Naval base (in province) |
| Sumatra | Java + (full control Sumatra OR is subject) | — | Sumatra: +1 Infrastructure, +2 building slots, +2 civilian factories; if DEI subject: −0.05% autonomy |
| Borneo and the Grote Oost | Java + (full control West Nusa Tenggara 667, Kalimantan Barat 334, Moluccas 668, Sulawesi 673 OR is subject) | — | West Nusa Tenggara, Kalimantan Barat, Moluccas, Sulawesi: +1 Infrastructure each; Sulawesi: +1 building slot, +1 civilian factory; if DEI subject: −0.05% autonomy |
| Curtail Colonial Autonomy | The Crown Jewel Colony; mutually exclusive with Continue the Zuiderzee Works; DEI exists, is subject, not completed Oranje Boven! (bypass if DEI doesn't exist or owns Java) | Continue the Zuiderzee Works | National spirit "Curtail Colonial Autonomy" (365d): Netherlands +0.33 PP/day cost; DEI: −2.0 daily autonomy progress (545d) |
| Continue the War in Batavia | (Sumatra AND Borneo and the Grote Oost AND Curtail Colonial Autonomy) + capitulated + not Oranje Boven! + (DEI is subject/integrated puppet with <60% autonomy OR full control Batavia 1058) | — | Activate "Relocate Government to Batavia" decision: remove Curtail Colonial Autonomy spirit; DEI units join Netherlands; annex DEI; set compliance +70%; move capital to Batavia (1058) |
| A Western Capital | Continue the War in Batavia + full control West Java | — | West Java: +2 Infrastructure, +4 building slots, +4 civilian factories |
| Expand the Colonial Army | Continue the War in Batavia | — | National spirit "Expand the Colonial Army": Non-core Manpower +2%, Training time −10%; every DEI core state: Local non-core Manpower +25% |
| Colonial Shipbuilding | The "Foundations of Defense" + A Western Capital + controls West Java, Sumatra, Kalimantan Barat, Sulawesi, Curaçao, Suriname | — | West Java, Sumatra, Kalimantan Barat, Sulawesi, Curaçao, Suriname: +1 building slot, +1 Naval dockyard each |
| The East Indies War Machine | A Western Capital + Expand the Colonial Army + full control West Java | — | West Java: +4 building slots, +4 military factories |
| Prepare for Our Return | (Colonial Shipbuilding AND The East Indies War Machine) (bypass if controls Holland 7, Brabant 35, Friesland 36) | — | West Java, Sumatra: +1 building slot, +1 Naval dockyard each; National spirit "Prepare for Our Return": Convoy production cost −10%; 1×100% Marine Technology research bonus |
| Liberation | Prepare for Our Return + controls Holland 7, Brabant 35, Friesland 36 | — | Move capital to Holland 7; Stability +10%, War support +5%, Manpower +150k; +10k Infantry Equipment, +500 Support Equipment to stockpile; National spirit "Liberation": Division attack/defense on core +10%, Training time −10%; modify De Crisisjaren spirit: Construction Speed +10% |

---

## Obtain Foreign Colonial Investments Branch (TAOG)

Requires Thunder at Our Gates DLC enabled. Similar to base game but with guarantee mechanics and modified continuations.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| Obtain Foreign Colonial (TAOG) | DEI at peace with USA, UK; (original country=NED OR is subject of NED OR full control colony states) | — | Unlocks TAOG colonial investment decisions for temporary bonuses and permanent Oil/Aluminum production |
| Guarantee Colonial Loyalty | Obtain Foreign Colonial (TAOG) + DEI is AI-controlled + before 1936-04-15 | — | PP −100; guarantees DEI will not have revolution; DEI gains 500 autonomy, +250 PP; DEI will attempt peaceful independence (can be stopped by completing follow-up focus requiring heavy investment) |
| The Western Possessions (TAOG) | Obtain Foreign Colonial (TAOG) + full control Curaçao, Suriname | — | Curaçao, Suriname: +1 Infrastructure |
| Expand Curaçao Oil Refineries (TAOG) | The Western Possessions (TAOG) + full control Curaçao + (>20% WT OR at war OR faction-specific) + (Free Trade OR Export Focus) | — | Unlock Royal Dutch Shell as Industrial Concern; Curaçao: +24 Oil, +2 building slots (if space), +1 civilian factory, +1 synthetic refinery; 1×100% Synthetic resources |
| Antilles Defenses (TAOG) | Expand Curaçao (TAOG) + full control Curaçao | — | Curaçao: +3 Coastal fort, +2 Anti-air, +2 Air base, +2 Naval base |
| Pre-Empt Venezuelan Aggression (TAOG) | Expand Curaçao (TAOG) + not Shell-shocked/Aloof Neutrality + Venezuela offered protection | — | War goal vs Venezuela (Puppet Focus) |
| Open Second Paranam Bauxite Mine (TAOG) | The Western Possessions (TAOG) + full control Suriname + (at war OR faction-specific) + (Free Trade OR Export Focus) | — | Suriname: +36 Aluminum, +1 building slot (if space), +1 civilian factory |
| Curtail Colonial Autonomy (TAOG) | Obtain Foreign Colonial (TAOG); mutually exclusive with Continue the Zuiderzee Works; DEI exists, is/not dominion subject, not Oranje Boven!/other independence focuses (bypass if DEI absent or controls Java/Batavia/East Java) | Continue the Zuiderzee Works | National spirit "Curtail Colonial Autonomy" (545d): Netherlands +0.33 PP/day; DEI +0.33 PP/day; triggers country event Netherlands Seeks Colonial Integration |
| Continue the War in Batavia (TAOG) | Curtail Colonial Autonomy (TAOG) + The Industrialized Colony; mutually exclusive with Soetardjo Act; not Oranje Boven!; (DEI is subject/integrated puppet <60% autonomy OR full control Batavia) | Soetardjo Act (unrec.) | Activate "Relocate Government to Batavia": remove Curtail Colonial Autonomy; DEI units join; annex DEI; compliance +70%; move capital to Batavia |
| A Western Capital (TAOG) | Continue the War in Batavia (TAOG) + full control West Java | — | West Java: +2 Infrastructure, +4 building slots (if space) and +4 civilian factories |
| Expand the Colonial Army (TAOG) | Continue the War in Batavia (TAOG) | — | National spirit "Expand the Colonial Army": Non-core Manpower +2%, Training time −10%; every DEI core: local non-core Manpower +25% |
| Colonial Shipbuilding (TAOG) | A Western Capital (TAOG) + controls West Java, Sumatra, Kalimantan Barat, Sulawesi, West Nusa Tenggara, Suriname | — | Each state: +1 building slot (if space), +1 Naval dockyard |
| The East Indies War Machine (TAOG) | A Western Capital (TAOG) + Expand the Colonial Army (TAOG) + full control West Java | — | West Java: +4 building slots (if space), +4 military factories |
| Prepare for Our Return (TAOG) | Colonial Shipbuilding (TAOG) + The East Indies War Machine (TAOG) (bypass if controls Holland, Brabant, Friesland) | — | West Java, Sumatra: +1 building slot (if space), +1 Naval dockyard; National spirit "Prepare for Our Return": Convoy cost −10%; 1×100% Marine Technology |
| Liberation (TAOG) | Prepare for Our Return (TAOG) + controls Holland, Brabant, Friesland | — | Move capital to Holland; Stability +10%, War support +5%, Manpower +150k; 10k Infantry Equipment, 500 Support Equipment; National spirit "Liberation": Div attack/defense core +10%, Training −10%; De Crisisjaren spirit Construction Speed +10% |

---

## Abandon the Gold Standard Branch

Mainland industrialization branch. Removes the De Crisisjaren national spirit through economic policy and public works.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| Abandon the Gold Standard | None | — | Modify De Crisisjaren spirit: Construction Speed +10% (effective gain from starting state) |
| Continue the Public Works | Abandon the Gold Standard + full control Holland (bypass if doesn't control Holland, Brabant, Friesland) | — | 1×100% Industry research; Brabant: +1 building slot, +1 civilian factory; modify De Crisisjaren: Construction Speed +10% |
| Finish the Noordoostpolder | Continue the Public Works + full control Friesland (bypass if missing core control) | — | Friesland: +2 building slots, +1 Infrastructure; modify De Crisisjaren: Construction Speed +10% |
| The Maastunnel | Continue the Public Works + full control Holland, Brabant (bypass if missing core) | — | Holland, Brabant: +1 Infrastructure each; modify De Crisisjaren: Construction Speed +10% |
| Expand the Artillerieinrichtingen | (Finish the Noordoostpolder OR The Maastunnel) + full control Holland (bypass if core lost) | — | Holland: +2 building slots, +2 military factories; if Arms Against Tyranny enabled: unlock H. I. H. Siderius (Artillery MIO, +500 funds); else unlock A. I. Hembrug (Materiel Designer) |
| Continue the Zuiderzee Works | Expand the Artillerieinrichtingen; mutually exclusive with Curtail Colonial Autonomy (base)/TAOG variant; DEI exists, is subject, controls Batavia, East Java, West Java | Curtail Colonial Autonomy | 2×100% Industry research; Holland: +1 building slot, +1 Infrastructure; Friesland: +4 building slots, +1 Infrastructure; modify De Crisisjaren: Construction Speed +10% |
| Develop the Randstad | Continue the Zuiderzee Works; mutually exclusive with Develop the Zandstad; full control Holland | Develop the Zandstad | 1×100% Concentrated Industry research; Holland: +3 building slots, +3 civilian factories; Friesland: +1 building slot, +1 civilian factory |
| Expand the IJmuiden Steel Mill | Develop the Randstad + full control Holland | — | Holland: +16 Steel production; if >1 free slots: +2 building slots, +2 civilian factories |
| Fokker | Expand the IJmuiden Steel Mill + full control Holland | — | If Arms Against Tyranny: Fokker +2 sizes; else unlock Fokker (Light Aircraft Designer, +15% air research, fighter agility/speed +10%); Holland: +4 building slots, +4 military factories |
| Develop the Zandstad | Continue the Zuiderzee Works; mutually exclusive with Develop the Randstad; full control Brabant, Friesland | Develop the Randstad | 1×100% Dispersed Industry research; Brabant, Friesland: +2 building slots, +2 civilian factories each |
| Friesland Agricultural Impetus | Continue the Zuiderzee Works + full control Friesland | — | National spirit "Friesland Agricultural Impetus": Consumer Goods factories −5%; Friesland: +2 building slots, +2 civilian factories |
| DAF | Friesland Agricultural Impetus + full control Brabant | — | If Arms Against Tyranny: DAF +2 sizes; else unlock DAF (Motorization Designer, +15% motorization research); Brabant: +4 building slots, +4 military factories |
| Domestic Innovation | (The East Indies War Machine OR Fokker OR DAF OR TAOG variant) + >50 factories | — | +1 research slot |
| Make Use of Our Riches | Domestic Innovation | — | 2×100% Excavation research; National spirit "Make Use of Our Riches": Resource Gain Efficiency +10% |
| The Ultimate Deterrent | Domestic Innovation | — | Nuclear Research breakthrough +50%; 1×80% Nuclear Technology research |
| Domestic Jet Engine Designs | Fokker | — | Aerodynamics/Avionics breakthrough +50%; 1×75% Jet research; gain/modify "Domestic Aircraft Production" spirit: all aircraft production cost −5% |
| Continental Shipbuilding | (Fokker OR DAF) + controls Holland, Brabant, Friesland | — | Holland, Brabant, Friesland: +2 building slots, +2 Naval dockyard each |
| Domestic Vehicle Designs | DAF | — | 2×100% Motorized research; National spirit "Domestic Vehicle Designs": Motorized, Mechanized production cost −10% |
| Philips | Expand the Artillerieinrichtingen | — | Unlock Philips (Electronics Concern, +15% electronics research); 1×100% Electronics research; 2×100% Electronics (ahead-of-time penalty −2y) |
| Expand R&D Facilities | Philips | — | +1 research slot |

---

## Overturn Military Budget Cuts Sub-branch

Military rearmament branch focusing on defensive preparations, land/air/naval forces, and overcoming pacifism.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| Overturn Military Budget Cuts | Abandon the Gold Standard | — | Army experience +5; War support +10% |
| Prepare the Inundation Lines | Overturn Military Budget Cuts | — | National spirit "Prepare the Inundation Lines": Land fort construction +10%; unlocks Prepare the Inundation Lines decisions for flooding/draining provinces |
| Protect Against Britain | Prepare the Inundation Lines; mutually exclusive with Germany is the Greater Threat; >10% WT; controls Holland, Friesland (bypass if in UK faction or at defensive war with UK, not started Germany focus) | Germany is the Greater Threat | Holland, Friesland: +1 Coastal fort, +1 Land fort each (added twice per province); UK: −50 opinion |
| Further Reinforce the Ports | Protect Against Britain + >15% WT + controls Holland, Friesland | — | Holland, Friesland: +1 Coastal fort, +1 Land fort each (added twice per province) |
| Southward Defenses | Further Reinforce the Ports + >20% WT + controls Holland, Brabant, Friesland | — | Holland: +2 Land fort, +1 Coastal fort, +2 Anti-air; Brabant: +3 Land fort; Friesland: +1 Coastal fort |
| Germany is the Greater Threat | Prepare the Inundation Lines; mutually exclusive with Protect Against Britain; >10% WT; controls Holland, Brabant, Friesland (bypass if in German faction or at defensive war, not started Britain focus) | Protect Against Britain | Holland: +1 Coastal fort; Brabant: +1 Land fort; Friesland: +1 Land fort; Germany: −50 opinion |
| Fortress Holland | Germany is the Greater Threat + >15% WT + controls Holland, Brabant | — | Holland: +2 Coastal fort, +2 Land fort, +1 Land fort, +1 Anti-air; Brabant: +2 Land fort, +1 Anti-air |
| Modernize the Grebbe Line | Fortress Holland + >20% WT + controls Friesland | — | Friesland: +1 Land fort, +1 Anti-air |
| War on Pacifism | (Protect Against Britain OR Germany is the Greater Threat) + >15% WT | — | Unlocks War on Pacifism decisions to reduce/remove Shell-shocked Spectator national spirit |
| Appoint New Supreme Commander | Overturn Military Budget Cuts | — | Army experience +10; 2×50% Land Doctrine cost reduction; remove Izaak Reijinders; unlock Henri Winkelman (Army Defense Expert: Division Defense +10%) as Field Marshal |
| Modernize Our Infantry Equipment | Appoint New Supreme Commander; mutually exclusive with Production Under License | — | 1×100% Infantry Weapons research; 1×100% Support Artillery research; focuses on internal equipment development |
| Production Under License | Appoint New Supreme Commander; mutually exclusive with Modernize Our Infantry Equipment | — | National spirit "Production Under License": License production speed (Infantry, Artillery) from tech diff +50%, base +25%; purchase cost −100%; focuses on license production |
| Light Tanks for the Colonies | (Modernize Our Infantry Equipment OR Production Under License) | — | If Modernize completed: 1×100% Light Tank research; if Production completed: National spirit "Light Tanks for the Colonies" with Light Tank license production bonuses |
| Secret Staff Talks | (Modernize Our Infantry Equipment OR Production Under License) + >15% WT + (Germany, UK, or France caused >10% WT) + at peace | — | Unlocks Secret Staff Talks decisions for Equipment, combat bonuses, Land Doctrine research, Gov-in-exile legitimacy |
| Anti Tank Guns for the Continent | (Modernize Our Infantry Equipment OR Production Under License) | — | If Modernize: 1×100% Anti-Tank research; if Production: National spirit "Anti Tank Guns for the Continent" with Anti-tank license bonuses |
| Lessons from the Last War | (Light Tanks OR Secret Staff Talks OR Anti Tank Guns) | — | Army experience +25; 2×50% Land Doctrine cost reduction |
| Expand the MLD | Overturn Military Budget Cuts + (controls West Java 335 OR is subject controlling it) (bypass if West Java owner not NED/subject) | — | Air experience +25; 1×50% Air Doctrine cost reduction; West Java: +2 Air base |
| Protect the Mainland | Expand the MLD; mutually exclusive with Protect the Colonies (bypass if doesn't control core or started Colonies) | Protect the Colonies | 1×100% Fighter research |
| Protect the Colonies | Expand the MLD; mutually exclusive with Protect the Mainland (bypass if no colonial territory or started Mainland) | Protect the Mainland | 1×100% Naval Bomber research |
| Modernize the Air Fleet | (Protect the Mainland OR Protect the Colonies) | — | National spirit "Modernize the Air Fleet" (365d): all aircraft production cost −20% |
| Strategic Bombing Defense | Modernize the Air Fleet + controls Holland | — | Air experience +25; 1×50% Air Doctrine cost reduction; Holland: +2 Air base, +2 Anti-air |
| Longer Range Models | Strategic Bombing Defense | — | 2×100% Heavy Fighter, Tactical Bomber research |
| Unsinkable Aircraft Carriers | Strategic Bombing Defense; mutually exclusive with Air Cover for the New Fleet; (controls all colony states OR is subject controlling them) (bypass if lost colonial control) | Air Cover for the New Fleet | West Java, Sumatra, Sulawesi, Kalimantan Barat: +2 Air base each; West Nusa Tenggara, Moluccas, Aru Islands, Dutch New Guinea: +1 Air base each |
| Aviatic Aspirations | (Longer Range Models OR Unsinkable Aircraft Carriers) | — | Air experience +25; 2×50% Air Doctrine cost reduction; gain/modify "Domestic Aircraft Production" spirit: aircraft production −5% |
| Prepare Naval Expansion | Overturn Military Budget Cuts + (controls Holland, Brabant, or Friesland) (bypass if core lost) | — | Navy experience +25; random controlled cored state: +3 building slots, +3 Naval dockyard |
| Cornerstone of Colonial Defense | Prepare Naval Expansion | — | 3×50% Naval Doctrine cost reduction |
| Rely on Submarines | Cornerstone of Colonial Defense; mutually exclusive with Modernize the Cruiser Fleet | Modernize the Cruiser Fleet | 2×75% Submarine research |
| Modernize the Cruiser Fleet | Cornerstone of Colonial Defense; mutually exclusive with Rely on Submarines | Rely on Submarines | Cruiser research ahead-of-time −2y, 50% bonus for next 2 researches |
| The Battlecruiser Plan | (Rely on Submarines OR Modernize the Cruiser Fleet OR Join Germany) + Germany independent + opinion ≥75 + (bypass if at war with Germany) | — | Add 1936 Heavy Ship Hull, Anti-Air II, Improved Fire Control, Improved Dual-Purpose Battery; create Battlecruiser design (1047); Germany must approve for bonuses; triggers German event |
| Air Cover for the New Fleet | The Battlecruiser Plan; mutually exclusive with Unsinkable Aircraft Carriers; (bypass if at war with Germany) | Unsinkable Aircraft Carriers | 2×75% Carrier research |
| Escorts for the New Fleet | The Battlecruiser Plan | — | Destroyer research ahead-of-time −2y, 75% bonus for next 2 researches |
| Naval Heritage | (Air Cover for the New Fleet OR Escorts for the New Fleet) | — | Navy experience +50; 2×50% Naval Doctrine cost reduction; National spirit "Naval Heritage": Dockyard output +10% |
| Expand the Amsterdam Petroleum Harbor | Prepare Naval Expansion + controls Holland + (can build 1+ Fuel silo) | — | Holland: +1 building slot, +1 Fuel silo |

---

## Form New Government Branch

Political branch with ideological paths. Each path is mutually exclusive at the "Form New Government" level onwards.

### Base Political (Gateway)

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| Form New Government | None (bypass if capitulated) | — | Event New Government Forms; Dirk Jan de Geer becomes Democratic leader; Defeatist Surrender Limit −25%, War support −10%; remove Weak Government spirit |
| Gateway to Europe | Form New Government (bypass if at war) | — | PP +120; unlocks Gateway to Europe decisions for Trade Influence allocation to Germany/UK |
| Cave to the Germans | Gateway to Europe; mutually exclusive with Maintain Trade Neutrality, Cave to the British; Germany ≥25 TP, ≥15 more than UK (bypass if Germany fascist/gone, at war UK, or completed opposite focus) | Maintain Trade Neutrality, Cave to the British | Change to Free Trade (Construction +15%, Research +10%, Factory output +15%, Dockyard +15%, Resources +80%); National spirit "Caved to the Germans" (1095d): Democracy support −0.02; Germany gains PP equal to all Gateway investments; opinion +15 with Germany, −50 with UK; trade +100 with Germany/DEI, −100 with UK |
| Maintain Trade Neutrality | Gateway to Europe; mutually exclusive with Cave to the Germans, Cave to the British; both Germany and UK ≥50 TP, neither >5 more (bypass if either non-correct ideology) | Cave to the Germans, Cave to the British | PP equal to total Gateway investments; trade +25 with both; both gain opinion −25 "Maintained Trade Neutrality"; trade +25 with both |
| Cave to the British | Gateway to Europe; mutually exclusive with Cave to the Germans, Maintain Trade Neutrality; UK ≥25 TP, ≥15 more than Germany (bypass if UK democratic/gone, at war Germany, or completed opposite) | Cave to the Germans, Maintain Trade Neutrality | Change to Limited Exports (Construction +5%, Research +1%, Factory +5%, Dockyard +5%, Resources +25%); National spirit "Caved to the British" (1095d): Fascism support −0.02; UK gains PP; opinion +15 with UK, −50 with Germany; Germany trade −100 with NED/DEI |

### Volk en Vaderland Sub-branch (Fascist)

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| Volk en Vaderland | Cave to the Germans | — | National spirit "Volk en Vaderland" (1095d): War support +0.20%/week, Fascism support +0.10%/day; unlock Meinout Rost van Tonningen (Fascist Demagogue, +0.10%/day Fascism) |
| Strength Over Blood | Volk en Vaderland + ruling fascist | — | Remove Aloof Neutrality; War support +10%; remove Weak Government |
| Join Germany | Strength Over Blood; mutually exclusive with The Netherlands First; Germany fascist, at peace, not in faction, independent (bypass if in German faction or started The Netherlands First) | The Netherlands First | Germany gets event "The Netherlands seeks to join the Axis" |
| The Netherlands First | Strength Over Blood; mutually exclusive with Join Germany; not in German faction | Join Germany | Enable faction creation; War support +10% |
| German Technological Exchange | Join Germany | — | Netherlands and faction members join German Technological Exchange |
| Beginnings of a Dutch Blitzkrieg | German Technological Exchange; mutually exclusive with Assume the Naval Burden; Germany has Panzer III or Basic Medium Tank | Assume the Naval Burden | Gain Medium Tank license from Germany; if Arms Against Tyranny: +500 PP/month subsidy for Medium Tank (500 cost); add 4 offmap military factories |
| Placate the Japanese | Join Germany + Japan fascist, at peace + (controls colonies OR is subject controlling them) (bypass if at war Japan, or lost colonies) | — | Japan gets event "Japanese Interest in the East Indies" |
| Assume the Naval Burden | Placate the Japanese; mutually exclusive with Beginnings of a Dutch Blitzkrieg; controls Holland, Friesland | Beginnings of a Dutch Blitzkrieg | National spirit "Assume the Naval Burden": Submarine, Light Hull, Cruiser, Heavy Ship, Carrier production cost −10%; Holland, Brabant, Friesland: +2 building slots, +2 Naval dockyard each |
| The United Netherlands | (Join Germany OR The Netherlands First) + not in Belgian/Luxembourg factions + not Shell-shocked spirit (bypass if controls Belgium/Luxembourg) | — | War goal (Annex) vs Belgium, Luxembourg; claims on Vlaanderen, Wallonie, Antwerpen, Ardennes, Luxembourg |
| Taking Back Our Old Colonies | The United Netherlands + not in French/UK/South Africa factions (bypass if controls former colonial territories) | — | Claims on French Caribbean, Leeward Islands, Trinidad, British Guyana, French Guiana, Ghana, Cape, Transvaal, Stanleyville, Ceylon; War goal (Conquer) vs France, UK, South Africa |
| Imperial Ambitions | Taking Back Our Old Colonies + not in US faction (bypass if controls New England) | — | National spirit "Imperial Ambitions": Factory output +10%, Dockyard output +5%; War support +10%; claims on New England, New York, New Jersey, Maryland; War goal (Conquer) vs USA |
| Implement the "Program" | The Netherlands First | — | National spirit "Implement the Program": Recruitable Population +1%; Stability +5%; Fascism popularity +5%; increase Mobilization Law to Service by Requirement; increase Economy Law to War Economy |
| Taking Back French Flanders | Implement the "Program" | — | Claim on Nord-Pas-de-Calais; War goal (Conquer) vs owner |
| De Jeugdstorm | Volk en Vaderland + ruling fascist | — | Fascism popularity +5%; War support +5%; National spirit "De Jeugdstorm": Recruitable Population +1%, Training time −10% |

### Legacy of the "De Zeven Provinciën" Mutiny Sub-branch (Communist)

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| Legacy of the "De Zeven Provinciën" Mutiny | Maintain Trade Neutrality; mutually exclusive with Oranje Boven! | Oranje Boven! | National spirit "Legacy of De Zeven Provinciën Mutiny" (1095d): Communism support +0.10%/day; unlock Saul de Groot (Communist Revolutionary, +0.10%/day Communism) |
| Decolonization | Legacy + ruling communist + (owns/subjects colonies OR DEI is subject) (bypass if lost all colonies, or they're independent) | — | If DEI subject: release Indonesia or complete independence focus; if subsidiary: independence; release Netherlands Antilles, Suriname; Stability −10%; PP +150; Manpower +150k; get "Redirected Investments" spirit (Construction +20%, Factory output +5%); create 8 KNIL (9 Infantry bns) in Holland |
| Red is the New Orange | Legacy + ruling communist | — | Remove Wilhelmina spirit; War support +10%; National spirit "Red is the New Orange": Construction +10%; remove Weak Government |
| Affirm Loyalty To Moscow | (Decolonization AND Red is the New Orange); mutually exclusive with Join the French, Bastion of True Communism; at peace USSR, USSR communist (bypass if in Comintern, completed opposite focuses) | Join the French, Bastion of True Communism | Remove Aloof Neutrality; USSR gets event "The Netherlands seeks to join the Comintern" |
| Join the French | (Decolonization AND Red is the New Orange); mutually exclusive with Affirm Loyalty To Moscow, Bastion of True Communism; at peace France, France (completed Humanité Unie/Loyalty To Cause/Anti-Fascist Coalition OR communist OR faction leader) (bypass if in Comintern, completed opposite) | Affirm Loyalty To Moscow, Bastion of True Communism | Remove Aloof Neutrality; France gets event "The Netherlands seeks to join [French Faction]" |
| Bastion of True Communism | (Decolonization AND Red is the New Orange); mutually exclusive with Affirm Loyalty To Moscow, Join the French; not in Soviet/French factions | Affirm Loyalty To Moscow, Join the French | Enable faction creation; War support +10%; National spirit "Bastion of True Communism": Division defense core +10%, Land fort construction +10%; remove Aloof Neutrality |
| Soviet Technical Teams | Affirm Loyalty To Moscow | — | National spirit "Soviet Technical Teams": Factory output +10% |
| Making the Ends of Europe Meet | Soviet Technical Teams + not in German faction (bypass if at war Germany) | — | War goal (Puppet Focus) vs Germany |
| Socialist Industrial Support | (Affirm Loyalty To Moscow OR Join the French) | — | +4 offmap military factories |
| For the Common Good | Socialist Industrial Support | — | Netherlands and faction members join Communist Technology Exchange |
| Mobilize the Masses | Socialist Industrial Support | — | National spirit "Mobilize the Masses": Recruitable Population +3% |
| French Military Mission | Join the French | — | Army experience +25; 2×50% Land Doctrine cost reduction; National spirit "French Military Mission": Training time −15% |
| Bring Socialism South | (Affirm Loyalty To Moscow OR Join the French OR Bastion of True Communism) + not in Belgian/Luxembourg factions + not Shell-shocked spirit (bypass if controls Belgium) | — | War support +10%; War goal (Puppet Focus) vs Belgium, Luxembourg |
| Enemies on All Fronts | Bastion of True Communism | — | National spirit "Enemies on All Fronts": Recruitable Population +5% |
| Pre-Empt Western Intervention | (French Military Mission OR Enemies on All Fronts) + (UK/France/USA non-communist) + (not in faction with major) | — | If UK not communist: War goal (Puppet Focus) vs UK; if France: vs France; if USA: vs USA |
| Haven of Tolerance | Enemies on All Fronts | — | Stability +10%, War support +5%; National spirit "Haven of Tolerance": Weekly Manpower +500 |

### Oranje Boven! Sub-branch (Monarchist)

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| Oranje Boven! | Maintain Trade Neutrality; mutually exclusive with Legacy of De Zeven Provinciën; not completed Curtail Colonial Autonomy | Legacy of De Zeven Provinciën | National spirit "Oranje Boven!": Daily Unaligned support +0.10% |
| Symbol of Resistance | Oranje Boven! | — | Modify "Oranje Boven!" spirit: Resistance growth in enemy-occupied states +25%, Div attack/defense core +10%, Daily Unaligned support +0.10% |
| Replace the Defeatist Government | (Oranje Boven! OR "Unity Through Democracy") + at war (bypass if non-aligned) | — | Event "The Queen Fires Defeatist Ministers"; Democracy popularity −5%; current leader retires, Pieter Gerbrandy becomes Democratic leader; War support +5%; Resistance in enemy-occupied +15%; remove Weak Government |
| Go with Britain | (Oranje Boven! OR "Unity Through Democracy"); mutually exclusive with Lead the Minor Democracies; UK democratic, >25% WT, not in faction, independent (bypass if in UK faction, started Lead Minor) | Lead the Minor Democracies | Remove Aloof Neutrality; UK gets event "The Netherlands seeks to join the Allies" |
| The Only Man in the Dutch Government | (Symbol of Resistance AND Replace the Defeatist Government) + NVB support >45% + not Curtail Colonial Autonomy | — | Non-Aligned becomes ruling party; no public elections; remove Wilhelmina spirit; Wilhelmina becomes Non-Aligned leader with traits: Stability +15%, Disdain for Politicians PP +5%, Democracy support −0.01, Communism/Fascism support −0.01, Queen of the People War support +10%, Resistance in enemy-occupied +25% |
| De Vernieuwing | The Only Man in the Dutch Government | — | PP +200; remove Communism, Fascism, Democracy popularity; modify Wilhelmina Disdain for Politicians by +5% PP gain, party support adjustments |
| Depillarization | The Only Man in the Dutch Government | — | Stability +10%; National spirit "Depillarization": Recruitable Population +1% |
| Royal Arms Purchases | De Vernieuwing | — | +3 offmap military factories |
| A New Dutch Unity | (De Vernieuwing AND Depillarization) | — | War support +15%, Stability +5% |
| De Vaarplicht | (Replace the Defeatist Government AND Go with Britain) | — | National spirit "De Vaarplicht": Recruitable Population +2.5% |
| Request Allied Favors | De Vaarplicht + in UK faction + at war + (not capitulated OR Legitimacy >40) | — | PP +60; unlocks Request Allied Favors decisions for Offmap resources |
| The Singapore Conferences | Go with Britain + completed "Unity Through Democracy" + ruling democratic + in UK/Australia/British Malaya factions + at peace USA + (British Malaya or UK controls Kuala Lumpur 336) (bypass if at war Japan, not Oranje Boven!) | — | 4×50% Naval Doctrine cost reduction |
| Ship-a-Day Sinking Quotas | (De Vaarplicht OR The Singapore Conferences) + at war | — | 1×100% Submarine research; 1×100% Submarine Operations Doctrine; random unit leader +1 Attack, +2 Maneuvering, +1 Coordination |
| Allied Technological Developments | The Singapore Conferences | — | National spirit "Allied Technological Developments": Research speed +10% |
| American West Indies Protectorate | (Ship-a-Day Sinking Quotas AND Allied Technological Developments) + at war + at peace USA | — | If in US faction: Curaçao, Suriname +1 Coastal fort, +1 Land fort (per location); create Dutch unit; else USA must approve; USA gains opinion/guarantee; triggers event |
| Wilhelminism | A New Dutch Unity + (at war Germany + Germany fascist, OR at peace Germany + not in faction + Germany non-aligned + has Kaiserreich focus + faction leader) (bypass if in German faction, both non-aligned) | — | If multiple conditions: affect opinion/factions; Germany gets event; get "German Defectors" spirit (periodically generate units 7 Infantry, 2 Artillery + support); Germany gets "Pro-Kaiser Defectors" (−1000 manpower/week) |
| Revive the Buffer State Proposal | (A New Dutch Unity AND Request Allied Favors) + in UK faction + at war same side + Belgium, Luxembourg in faction fighting same side + (Belgium capitulated + others not, OR all capitulated but NED higher legitimacy) | — | UK gets event "The Netherlands Proposes United Netherlands" |
| Develop the South | Revive the Buffer State Proposal + controls Vlaanderen, Wallonie, Antwerpen, Ardennes, Luxembourg | — | Antwerpen: +2 building slots, +2 civilian factories; Wallonie: +1 Infrastructure, +1 building slot, +1 military factory; Luxembourg: +1 Infrastructure, +1 building slot, +1 civilian factory |
| Combined Chiefs of Staff Representation | (Request Allied Favors AND American West Indies Protectorate) + in UK/US factions + at war + (not capitulated OR Legitimacy >80) | — | National spirit "Combined Chiefs of Staff Representation": Planning speed +10%, Max Command power +15, Daily Command power +5% |
| The Fourth Ally | Combined Chiefs of Staff Representation + in UK/US factions + at war + at peace USSR + controls West Java, Sumatra | — | West Java, Sumatra: +2 building slots, +2 Naval dockyard; National spirit "The Fourth Ally": Dockyard output +10% |
| Zandery Military Airport | American West Indies Protectorate + in US faction + at war + controls Suriname, Curaçao | — | Suriname: +8 Air base, +2 Infrastructure; Curaçao: +3 Radar station |

### "Unity Through Democracy" Sub-branch (Democratic)

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| "Unity Through Democracy" | Cave to the British | — | Stability +5%; National spirit "Unity Through Democracy" (1095d): Stability +0.10%/week, Democracy support +0.05%/day, Communism/Fascism support −0.02%/day; unlock Willem Schermerhorn (Democratic Reformer, +0.10%/day Democracy) |
| Lead the Minor Democracies | "Unity Through Democracy"; mutually exclusive with Go with Britain; at peace, not in faction, independent | Go with Britain | PP +120; remove Aloof Neutrality; every European democratic non-major gains opinion +25 "Lead the Minor Democracies"; National spirit (1095d): Communism/Fascism support −0.02%/day |
| Form the Benelux | Lead the Minor Democracies + not in Belgian/Luxembourg factions, independent (bypass if they don't exist or controlled) | — | Enable faction creation; create "Benelux" faction; Belgium, Luxembourg get events to invite; remove Weak Government; unlock Benelux Unification decision |
| Responsibility For Our Own Defense | Lead the Minor Democracies | — | War support +5%; National spirit "Responsibility": Recruitable Population +1%, Factory output +5%, Military factory construction +10% |
| Lessons from the Low Countries | (Form the Benelux AND Responsibility For Our Own Defense) | — | National spirit "Lessons from Low Countries": Div defense core +10%, Max entrenchment +10, Land fort construction +10% |
| Foundations for a European Union | Lessons from the Low Countries | — | If faction leader: rename to European Union; else if in faction: leave, create European Union; else create European Union; unlock invitations and development decisions |
| The Continent's Best and Brightest | Foundations for a European Union | — | All faction members join "The Continent's Best and Brightest" cooperation |
| The Best Defense | Foundations for a European Union + not in German/UK factions (bypass if at war Germany/UK) | — | War goal (Puppet Focus) vs Germany, UK |

---

## Reassert Control over the Indies Branch

Cross-reference: This is a joint branch with Dutch East Indies. Refer to Dutch East Indies national focus tree for details.

---

## Establish the ABDACOM Branch

Cross-reference: This is a joint branch (ABDACOM = American-British-Dutch-Australian Command). Requires Thunder at Our Gates DLC. Refer to joint ABDACOM branch documentation for mechanics shared with Australia, DEI, France, UK, USA.

---

## DLC Requirements and Notes

- **Base game**: Obtain Foreign Colonial Investments (Base Game), Abandon the Gold Standard, most political branches, generic military branch structure
- **Thunder at Our Gates**: Obtain Foreign Colonial Investments (TAOG variant), Guarantee Colonial Loyalty, ABDACOM branch, alternative continuations, modified autonomy mechanics
- **Arms Against Tyranny**: Industrial concerns (H. I. H. Siderius, DAF), design company unlocks (A. I. Hembrug, Fokker, DAF, Philips), research bonuses
- **By Blood Alone**: Not applicable to Netherlands focus tree

> ⚠️ Several focuses in this tree contain broken wiki template markers (`[{{{1}}}]`) indicating italicized text/flavor (fascist/communist/monarchist/democratic labels). These have been reconstructed from context and marked in the text where they appear in sub-branch headers and flavor text.

