---
title: British National Focus Tree
category: focus-trees
tags: [focus tree, Britain, unique tree, empire, democracy, ideology]
game_version: "1.19"
dlc: [La Résistance, Arms Against Tyranny]
sources:
  - https://hoi4.paradoxwikis.com/British_national_focus_tree
---

## Summary

The United Kingdom's unique focus tree offers five major branches reflecting the historical path of staying democratic, retaking an empire focus, decolonizing, or ideological shifts toward monarchy, fascism, or communism. The tree emphasizes industrial rearmament, naval and air power, colonial development, and political choices that can reshape the nation's ideology and war goals. See [United Kingdom](../05-countries/united-kingdom.md) for the country's 1936 starting profile.

> ⚠️ Broken wiki template reconstructed: text marked `[{{{1}}}]` in source was replaced with context-appropriate terms (Democratic/Fascist/Communist/Monarchist) based on surrounding text, as the wiki template data was corrupted.

## Generic and Continuous Focuses

See [National Focus and Continuous Focus](../01-mechanics/national-focus.md) for the generic focus tree all countries share and continuous focuses available after 10 completed focuses.

---

## Cryptologic Bomb / Limited Rearmament Branch

The industrial and technological rearmament path: research bonuses for decryption, radar, nuclear technology, factories, air bases, and dockyards. Branches into intelligence services (La Résistance only), general rearmament (air and naval), and motorization.

| Focus | Prerequisites | Bypass Conditions | Effects |
|---|---|---|---|
| **Cryptologic Bomb** | None | Poland in faction with Germany; at war with Germany and US in faction | If La Résistance: +10 Decryption Speed. Otherwise: 3× 100% research bonus for Decryption Methods or Computing Technology |
| **Limited Rearmament** | None | Not enough building slots for civilian factories | 2 random owned cored states each get +2 building slots, +2 civilian factories |
| **Air Defense** | Limited Rearmament; world tension >5% OR at war OR ruling party not democratic OR has "No Further Appeasement" spirit | Insufficient building slots for anti-air | +25 air experience; max anti-air added to South-West England (123), East Anglia (125), Sussex (127); overflow to random British Isle state |
| **RADAR** | Air Defense | — | +25 air experience; 75% breakthrough in Aerodynamics and Avionics; 1× 100% research bonus for RADAR |
| **The Tizard Mission** | Cryptologic Bomb AND RADAR; ruling party democratic; at peace with USA; USA ruling party democratic AND not in isolation | — | US gets event "The Tizard mission"; if accept: both sides get 75% breakthrough in Aerodynamics and Avionics; UK gets 1× 50% research bonus for Fighter; USA gets same |
| **The MAUD Committee** | The Tizard Mission; in faction with USA | — | 75% breakthrough in Nuclear Research; 1× 75% research bonus for Nuclear Technology |
| **The Shadow Scheme** | Limited Rearmament; world tension >5% OR at war OR ruling party not democratic OR has "No Further Appeasement" spirit | — | When entering war: 4 building slots and 4 military factories total across 2 states. If not have "Prepare for the Inevitable": gain "Wartime Industry" spirit (civilian-to-military conversion −50%). If already have: replace with upgraded version (conversion −50%, factory output +5%, military factory construction speed +10%) |
| **Industrial Effort** | The Shadow Scheme | — | 2× 100% research bonus for Industry |
| **Royal Ordnance Factories** | Industrial Effort; world tension >20% OR at war OR Germany completed Remilitarize the Rhineland OR ruling party not democratic OR has "No Further Appeasement" OR any country at war with UK OR >30 factories | Not enough military factory slots | 3 random Home-area states each get +2 building slots, +2 military factories |
| **Secret Weapons** | The MAUD Committee AND Royal Ordnance Factories | — | 1× 50% research bonus for Rocketry; 1× 50% research bonus for Nuclear Technology |
| **BSA Company** | Royal Ordnance Factories | — | National spirit "Birmingham Small Arms Company": infantry equipment production cost −10% |
| **Extra Research Slot** | Industrial Effort | — | +1 research slot |
| **Vickers Experimental Facilities** | Industrial Effort; full control of Greater London (126) | — | 50% breakthrough in Aerodynamics and Avionics; 50% breakthrough in Land Warfare; if no other facility in Greater London: +1 Aerodynamics and Avionics facility in Greater London |
| **A Motorized Army** | Limited Rearmament | — | 1× 100% research bonus for Motorized |
| **Royal Tank Regiment** | A Motorized Army | — | 1× 100% research bonus for Armor |

### Expand the Secret Intelligence Service (requires La Résistance)

Intelligence agency and espionage focus.

| Focus | Prerequisites | Effects |
|---|---|---|
| **Expand the Secret Intelligence Service** | Limited Rearmament; La Résistance enabled | Create intelligence agency; national spirit "MI6": stability +5%, operative slots +1, intel network strength gain +10%, enemy operative detection +0.05%, enemy operative capture +5%, civilian intelligence to others −5% |

### General Rearmament Sub-branch

Air force and navy rearmament, air bases, dockyards, naval doctrine, special forces.

| Focus | Prerequisites | Mutual Exclusive | Effects |
|---|---|---|---|
| **General Rearmament** | Limited Rearmament; world tension >10% OR at war OR ruling party not democratic OR has "No Further Appeasement" | — | National spirit "British Austerity": consumer goods factories −5% |
| **Air Rearmament** | General Rearmament | — | +25 air experience; 5 random British Isle states each get +2 air bases |
| **Special Air Service** | General Rearmament | — | National spirit "Special Air Service": special forces capacity +5%, special forces division training −10%; available advisor David Stirling (special forces attack +20%, defense +20%) |
| **Airborne Forces Depot** | Special Air Service; Arms Against Tyranny enabled | — | +1 free special forces branch specialism; 2× 25% cost reduction for Special Forces Doctrine |
| **Naval Rearmament** | General Rearmament | — | +50 navy experience; 3 random cored states each get +1 building slot, +1 naval dockyard |
| **Fighter Command** | Air Rearmament | — | +25 air experience; 2× 100% research bonus for Fighter and Heavy Fighter (if By Blood Alone: adds 1× 50% air doctrine cost reduction) |
| **Bomber Command** | Air Rearmament | — | +25 air experience; 2× 100% research bonus for Strategic Bomber and Tactical Bomber (if By Blood Alone: adds 1× 50% air doctrine cost reduction) |
| **Coastal Command** | Air Rearmament | — | +25 air experience; 2× 100% research bonus for Naval Bomber and Close Air Support (if By Blood Alone: adds 1× 50% air doctrine cost reduction) |
| **Aircraft Production Group** | Fighter Command OR Bomber Command OR Coastal Command | — | National spirit "Aircraft production group": fighter production cost −10% |
| **Jet Aircraft** | Aircraft Production Group | — | 100% breakthrough in Aerodynamics and Avionics; 2× 100% research bonus for Jet Technology |
| **Chiefs of Staff Committee** | Air Rearmament AND Naval Rearmament | — | +10 army, navy, air experience each; national spirit "Chiefs of Staff Committee": planning speed +10%, max command power +25%, daily command power gain +10% |
| **Destroyer Focus** | Naval Rearmament | — | 2× 100% research bonus for Destroyer |
| **Convoy Escort Focus** | Destroyer Focus | — | National spirit "Convoy system priority": light hull production cost −10%, trade convoy production cost −10% |
| **Anti-Submarine Training School** | Convoy Escort Focus | — | +25% mastery bonus for 180 days on all active Screens tracks; national spirit "Anti-Submarine Training School": destroyer training experience +10%, destroyer combat experience gain +10% |
| **A/S Warfare** | Destroyer Focus | — | Next 2 researches of Anti-Submarine Warfare Technology: −2.0 years AoT, 100% research bonus |
| **Amphibious Warfare** | Naval Rearmament | — | 1× 100% research bonus for Marine Technology; 2× 100% research bonus for Transport |
| **Britannia Rules the Waves** | Naval Rearmament | — | 3× 50% cost reduction for Naval Doctrine |
| **Carrier Focus** | Britannia Rules the Waves | Battleship Focus | +25 navy experience; 2× 100% research bonus for Carrier |
| **Battleship Focus** | Britannia Rules the Waves | Carrier Focus | +25 navy experience; 2× 100% research bonus for Battleship |
| **Expand the Repair Yards** | Carrier Focus OR Battleship Focus | — | +2 building slots, +2 naval dockyards in random cored state; national spirit "Expand the Repair Yards": refitting speed +10%, refitting cost −10%, ship repair speed +10% |
| **Vanguard** | Battleship Focus; date ≥1944.1.1; has 1944 Heavy Ship Hull tech; full control of Lanark (133) | — | +25 navy experience; create HMS Vanguard capital ship variant |
| **Anti-Non-Contact Committee** | Naval Rearmament | — | 1× 100% research bonus for Naval Minelaying; 2× 100% research bonus for Naval Minesweeping |
| **Secure the Imperial Shipping Routes** | Naval Rearmament AND Service Overseas | — | 2× 100% research bonus for Cruiser; national spirit "Secure the Imperial Shipping Routes": cruiser production cost −10% |

---

## Reinforce the Empire Branch

Colonial development and expansion: industrial investment in colonies, fortification of key territories, war goals against China/Japan/Italy, imperial federation merging dominions.

| Focus | Prerequisites | Mutual Exclusive | Bypass Conditions | Effects |
|---|---|---|---|---|
| **Reinforce the Empire** | Current ruling party not communist; >0 subject nations | Revisit Colonial Policy | — | +10% stability (locked if decolonization not completed within 2 years of becoming communist: civil war) |
| **Service Overseas** | Reinforce the Empire | — | — | +5 army experience, +25 navy experience, +25 air experience; national spirit "Service Overseas": hot acclimatization gain +10% |

### Encourage Colonial Elite Sub-branch

Dominion development and Fortify East Asia path: autonomy reduction, war goals, Chinese influence, Japanese war goal, Imperial Federation, Fortified East Asia.

| Focus | Prerequisites | Mutual Exclusive | Effects |
|---|---|---|---|
| **Encourage Colonial Elite** | Reinforce the Empire | Revisit Colonial Policy (blocks entire Dominions side) | Various dependent on path taken |
| **Autonomy of the Dominions** | Encourage Colonial Elite | Commonwealth Ties | Random dominion: −10% autonomy progress gain for 365 days |
| **Dominion Status** | Autonomy of the Dominions OR Commonwealth Ties | — | British Raj: −10% autonomy progress for 365 days (if independent: −20 to −30 opinion toward UK) |
| **Restored Ambitions** | Dominion Status | Concessions to the War Office | Casus belli on France (Restore the Alsatian Borders); event triggers with Portugal |
| **Fortify East Asia** | Encourage Colonial Elite | Commonwealth Ties | Various province modifiers and infrastructure in Asia |
| **British Intervention in China** | Fortify East Asia | — | Opinion factor +50 toward China; if China communist and faction leader: event to join faction |
| **Exploit the War** | British Intervention in China | — | Chinese states gain modifiers; if China non-aligned: war goal to control multiple Chinese states |
| **Subjugate China** | Exploit the War | — | War goal against China; various Chinese state annexations/puppets possible |
| **Prepare for Conflict** | Fortify East Asia | — | War goal against Japan; various strategic preparations |
| **Commonwealth Ties** | Encourage Colonial Elite | Autonomy of the Dominions | Various dominion-focused effects, autonomy changes |
| **Imperial Federation** | Commonwealth Ties | — | Annexation of dominions, gaining cores on their territories, +25% stability |

### Mediterranean Bastion Sub-branch

Mediterranean colonial development, expansion toward Turkey, Greece, Italy war goal, North Africa development.

| Focus | Prerequisites | Effects |
|---|---|---|
| **Mediterranean Bastion** | Reinforce the Empire OR Service Overseas | Various Mediterranean infrastructure/strategic benefits |
| **Expand the Suez Canal** | Mediterranean Bastion | +2 building slots, +1 infrastructure in Suez Canal state |
| **Dominance in the Mediterranean** | Expand the Suez Canal | Naval superiority bonuses in Mediterranean; opinion and influence effects |
| **Cyprus Bases** | Dominance in the Mediterranean | +2 air bases, +1 naval dockyard in Cyprus |
| **Greek Guarantees** | Dominance in the Mediterranean | Guarantee Greece; guarantee war participation |
| **Coerce Turkey** | Greek Guarantees | War goal against Turkey (if successful: annexation possible) |
| **War with Italy** | Mediterranean Bastion OR Dominance in Mediterranean | War goal against Italy |

---

## Revisit Colonial Policy Branch

Decolonization: independence for colonies, repatriation to UK homeland, manpower and industry gains, concentration on European affairs.

| Focus | Prerequisites | Mutual Exclusive | Effects |
|---|---|---|---|
| **Revisit Colonial Policy** | Current ruling party not at least one of { communist, non-aligned if monarchy path }; <100% fascism OR ruling party democratic | Reinforce the Empire | Freedom for colonies; manpower/industry transferred to UK |
| **Guide the Colonies** | Revisit Colonial Policy | — | Colonial autonomy progress reductions; gradual independence |
| **Towards Dominion Independence** | Guide the Colonies | — | Dominion autonomy modified; moving toward independence |
| **Independence for the Jewel in the Crown** | Towards Dominion Independence | — | British Raj autonomy further reduced; civil war triggers depending on ideology |
| **Prepare for Decolonization** | Guide the Colonies | — | Infrastructure and building slots added to UK core territory; industrial preparation |

---

## Steady As She Goes Branch

Democratic path: stay democratic, maintain government structure, place Churchill, end appeasement, global defense, and home defense against European threats.

| Focus | Prerequisites | Mutual Exclusive | Bypass/Effects |
|---|---|---|---|
| **Steady As She Goes** | Ruling party democratic | A Change in Course | +10% stability; maintain democratic governance |
| **No War is as Just as Ours** | Steady As She Goes | — | Political power +120 |

### Global Defense Sub-branch

Churchill ascendancy, appeasement removal, war goals against oil-producing states and hostile European powers.

| Focus | Prerequisites | Effects |
|---|---|---|
| **Global Defense** | Steady As She Goes OR Renounce Appeasement | +25 political power; removes "Appeasement" and "Pacifism" spirits if present |
| **Renounce Appeasement** | Steady As She Goes | Removes Neutral Foreign Policy; political power +150 |
| **Put Churchill in Power** | Global Defense OR Renounce Appeasement | Replace ruling party leader with Winston Churchill (if not already) |
| **End Appeasement** | Put Churchill in Power | Removes "Appeasement" spirit; political power +150; removes "Pacifism" if present |
| **Anti-Appeasement Efforts** | End Appeasement | War goal against any fascist or non-aligned major; removes "Pacifism" |
| **War with Japan** | Global Defense (must be democratic) | War goal against Japan; +25% war support |
| **War with Italy** | Global Defense (must be democratic) | War goal against Italy |
| **War with Germany** | Global Defense (must be democratic) | War goal against Germany |
| **War on Oil** | Global Defense | War goal against Saudi Arabia, Iraq, Iran, Venezuela (any oil producer); +25% war support |
| **Allow Volunteer Forces** | Global Defense | Sets rule: can send volunteer forces |

### Home Defense Sub-branch

Intervention in Scandinavia, Low Countries, North Africa, Iraq, Iran; eventual war with Soviet Union and Germany.

| Focus | Prerequisites | Mutual Exclusive | Effects |
|---|---|---|---|
| **Home Defense** | Steady As She Goes OR Renounce Appeasement | — | Various defensive preparations; +25 political power |
| **Fortress Britain** | Home Defense | — | Coastal fort construction speed +15%; anti-air construction speed +15%; radar station construction speed +15% |
| **Secure the Mediterranean** | Home Defense | — | Guarantee Iraq and Iran; opinion toward Middle East nations |
| **Secure the North Sea** | Home Defense | — | Guarantee Norway, Denmark, Netherlands; naval presence |
| **Puppet the Dutch** | Secure the North Sea | — | Netherlands autonomy reduction; eventual puppeting possible |
| **The Suez Crisis** | Secure the Mediterranean | — | Guarantee Sudan; opinion effects |
| **War with Germany** | Home Defense | — | War goal against Germany |
| **War with Soviet Union** | Home Defense OR Secure the Mediterranean | — | War goal against Soviet Union |
| **War on Democracy's Enemies** | Home Defense | — | War goals against fascist and communist majors; political power +150 |

---

## A Change in Course Branch

Ideological paths: shift to Monarchism, Fascism, or Communism. Each offers distinct alliances, war goals, and political changes.

### Monarchist Path

Restore absolute monarchy under Edward VIII, ally with Germany, war goals against Italy and Soviet Union, gain American war goal to restore monarchy in USA.

| Focus | Prerequisites | Mutual Exclusive | Effects |
|---|---|---|---|
| **A Change in Course** | None | Steady As She Goes (blocks democratic consolidation) | Political path unlocked |
| **The King's Party** | A Change in Course | — | Support for King Edward VIII increases; monarchist support +20% daily |
| **Support the Abdicated** | The King's Party | Oppose the King | Event to restore Edward VIII; if successful: ruling party becomes non-aligned (monarchy), Edward becomes leader |
| **God Save the King** | Support the Abdicated | — | Stability +5%; political power +150; war goal against each Dominion |
| **Oppose the King** | The King's Party | Support the Abdicated | Democratic support increases; blocks Edward restoration |
| **An Anglo-German Alliance** | Support the Abdicated (OR King already in power) | — | Opinion toward Germany +100; can guarantee/join German faction; removes Neutral Foreign Policy |
| **War with Italy** | An Anglo-German Alliance | — | War goal against Italy |
| **War with Soviet Union** | An Anglo-German Alliance | — | War goal against Soviet Union |
| **Reinstate the Monarchy in America** | An Anglo-German Alliance | — | War goal against USA (50% US occupation, install monarchy, puppet USA) |
| **Reclaim the Dominions** | God Save the King | — | War goal against each independent dominion (Australia, Canada, New Zealand, South Africa); annexation |

### Fascist Path

Shift to fascism, secure European alliances against Germany, coercive measures.

| Focus | Prerequisites | Mutual Exclusive | Effects |
|---|---|---|---|
| **Fascist Britain** | A Change in Course | Communist path | Fascism support +20% daily; ruling party shift to fascism (if successful) |
| **Secure German Cooperation** | Fascist Britain | — | Opinion toward Germany; can align with German faction or negotiate mutual defense |
| **Alliance Against Germany** | Fascist Britain | — | Coerce other fascist nations into faction; war preparation against Germany |
| **War with Germany** | Fascist Britain | — | War goal against Germany |

### Communist Path (Concessions to the Trade Unions Sub-branch)

Shift to communism, choose between Soviet alliance or independent communist faction, spread communism across Europe.

| Focus | Prerequisites | Mutual Exclusive | Bypass/Effects |
|---|---|---|---|
| **Concessions to the Trade Unions** | A Change in Course | Democratic/Monarchist/Fascist | Communism support +20% daily; ruling party shift to communism (if successful); **mandatory decolonization within 2 years or civil war** |
| **Comrade Attlee** | Concessions to the Trade Unions | — | Clement Attlee becomes political advisor (communist support +0.1) |
| **Work with the Comintern** | Concessions to the Trade Unions | Internationalist Socialism | Join Soviet faction or align with communism globally; opinion toward Soviet Union +100 |
| **Internationalist Socialism** | Concessions to the Trade Unions | Work with the Comintern | Create independent communist faction; form communist international alliance |
| **Spread the Revolution** | Work with Comintern OR Internationalist Socialism | — | War goals against European nations; communist conversion attempts; puppet regimes |
| **War with Germany** | Communist path focus | — | War goal against Germany |
| **War with United States** | Communist path focus | — | War goal against USA; puppet regime possible |

---

## Establish the ABDACOM Branch

Joint branch (requires coordinated play with Netherlands East Indies, Australia, USA). Establishes ABDACOM (American-British-Dutch-Australian Command) for coordinated Pacific War operations.

> ⚠️ The wiki page for this branch is marked incomplete ("XXX" in source); detailed focus data not yet available on wiki.

---

## Summary of DLC Requirements

- **La Résistance**: Expand the Secret Intelligence Service sub-branch (intelligence agency, MI6 national spirit)
- **Arms Against Tyranny**: Airborne Forces Depot focus (additional special forces doctrines)
- **By Blood Alone**: Enhanced bonuses on Fighter Command, Bomber Command, Coastal Command (includes air doctrine cost reductions)
- All other focuses are available in base game

---

## Strategic Notes

- **Industrial path**: Prioritize Cryptologic Bomb → RADAR → Tizard Mission for tech sharing with USA, or The Shadow Scheme → Industrial Effort for factory growth
- **Naval dominance**: General Rearmament → Naval Rearmament; choose between Carrier/Battleship doctrines based on strategy (Carrier more modern, Battleship traditional)
- **Empire consolidation**: Reinforce the Empire → Encourage Colonial Elite for Commonwealth ties and Imperial Federation (annexes dominions)
- **Decolonization**: Revisit Colonial Policy provides alternative manpower and industry gains, frees UK for European focus
- **Ideological shifts**: A Change in Course can lead to communist (forces decolonization and civil war risk), monarchist (war with dominions, US), or fascist paths; each blocks democratic consolidation
- **Churchill path**: Steady As She Goes → Put Churchill in Power enables democratic war support and removes appeasement penalties; conflicts with ideological shifts
