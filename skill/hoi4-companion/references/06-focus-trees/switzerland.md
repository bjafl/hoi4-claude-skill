---
title: Swiss National Focus Tree
category: focus-trees
tags: [switzerland, national focus, alpine, neutrality, democracy, fascism, military, defense]
game_version: "1.19"
dlc: [By Blood Alone]
sources:
  - https://hoi4.paradoxwikis.com/Swiss_national_focus_tree
---

## Summary

Switzerland has a unique national focus tree (requires *By Blood Alone* DLC; without it uses the generic tree). The tree is organized around a central **Swiss Guiding Principles** branch that forks into 10 ideological and strategic sub-branches: democratic paths (anti-Nazi propaganda, Allied Gold, espionage), neutralist/expansionist paths (Gotthardbund), military/defense paths (Henri Guisan, Federal Police), and fascist collaboration paths (German planes, closer ties to Germany). The tree heavily features a **Balance of Power** slider (Cantons ↔ Council) that gates many focuses, allowing Switzerland to navigate toward democracy, fascism, communism, or non-aligned status. Key mechanic: the *Spirit of Helvetia* national spirit shifts between Passive (peace), Defensive (armed neutrality), and Aggressive (war/alliance) states depending on choices.

See [Switzerland](../05-countries/switzerland.md) for the country's 1936 starting profile.

See [National Focus and Continuous Focus](../01-mechanics/national-focus.md) for generic/continuous focuses.

## Swiss Guiding Principles Branch

**Starting branch.** All paths begin here.

| Focus | Prerequisites | Effects |
|---|---|---|
| **Swiss Guiding Principles** | None | Political Power +100. Balance of Power slider appears (starts at 100% towards Cantons). Event: Swiss Guiding Principles. Flags start date before 1936.01.02. |
| **Increase Defense Budget** | Swiss Guiding Principles | Random state: Add 2 building slots, 2 military factories. If has "War Bonds" spirit, replace with "Ongoing Rearmament" (Consumer Goods −5%, Military factory construction +10%, Civilian factory +15%). Gets "Increase Defense Budget" spirit (Military/Civilian factory construction +10%/+10%). |
| **National Defense Fund** | Swiss Guiding Principles | Random state: Add 3 building slots, 3 military factories. If has "Increase Defense Budget" spirit, replace with "Ongoing Rearmament" (−5%/+10%/+15%). Otherwise if lacks "Ongoing Rearmament" and "War Bonds", get "War Bonds" (−5%). |
| **Reaffirm Spiritual Defense** | Increase Defense Budget OR National Defense Fund | Enables "Spirit of Helvetia" passive form: if not at war, gain "Passive Spirit of Helvetia" (Political Power daily +0.20, Recruitable Population −15%, War support −20%, Military factory −5%, Civilian factory +15%); if at war, gains penalties to organization, manpower, stability, war support. |
| **Fortify Border with Italy** | Reaffirm Spiritual Defense | Add 2 land forts in every Italian border province. Italy gains "Fortified their border with us" opinion −25. Balance nations gain "Mild Appeasement" opinion +25 (if not Italy-aligned). |
| **Fortify Border with Germany** | Reaffirm Spiritual Defense | Add 2 land forts in every German border province. Germany gains opinion −25. Balance nations gain opinion +25. |
| **Fortify Border with France** | Reaffirm Spiritual Defense | Add 2 land forts in every French border province. France gains opinion −25. Balance nations gain opinion +25. |
| **Armed Neutrality** | Fortify Border with Italy/Germany/France AND (Has Swiss Citizen Militias OR Expanded Swiss Citizen Militias conscription) | Spirit of Helvetia becomes Defensive: +5% factory output, +30 max entrenchment, +0.10 daily command power, +15% military factory construction, +20% land fort construction (if at war). If not at war, adds Recruitable Population +25%, entrenchment speed +0, War support +30%, Division Defense +25%, max entrenchment +50%, command power maximum +20, defensive stability +50%. Adds "Citizen Militias in Reserve" template (heavily nerfed), cap 20. Suspicious nations gain opinion −10. |

## Ban Foreign Nazi Propaganda Sub-branch

Democratic appeasement path. Requires one of: Fortify Border with Italy/Germany; Balance of Power right of Strong Council Control range.

| Focus | Prerequisites | Effects |
|---|---|---|
| **Ban Foreign Nazi Propaganda** | (Fortify Border Italy OR Germany) AND Balance right of Strong Council Control | Gets "Banned Foreign Nazi Propaganda" spirit (Fascism Support −0.05 daily). Fascist nations gain opinion −30. |
| **Buero Ha** | Ban Foreign Nazi Propaganda AND Balance >0% Cantons side | **La Résistance DLC:** Create Intelligence Agency if not exists; gain "Buero Ha" spirit (Counter intelligence −0.10, Intel network strength +20%); Hans Hausamann, Rudolf Roessler become operatives. **Otherwise:** Get "Buero Ha" (All intelligence types +20%). |
| **Pro Helvetia** | Buero Ha AND Balance >0% Cantons side | Gets "Pro Helvetia" spirit (Political Power daily +15%, Consumer Goods −5%). Decreases minimum Military Readiness for Citizen Militias by −15. |
| **Spirit of Saint Bernard** | Pro Helvetia AND Balance >0% Cantons side AND has researched Field Hospital I | 1× 150% research bonus for Field Hospitals. Gets "Spirit of Saint Bernard" spirit (Field Hospital trickleback +20%, Exp. Loss Factor −30%). Unlocks "Field Hospital for Militias" decision. |
| **Ban National Movement for Switzerland** | Pro Helvetia AND Balance right of Balance between Council/Cantons | Germany (if Fascist): opinion −25. Italy (if Fascist): opinion −25. Democratic nations gain opinion +15. Fascism popularity −15.00%. Political Power +120. |
| **Seek Allied Trade** | Ban National Movement AND Balance right | Best Democratic Ally gets event to trade with Switzerland. |
| **Fortify the Austrian Border** | Ban National Movement AND Balance right AND Austria does not exist | Eastern Swiss Alps (151): Add 2 land forts (2 separate). Swiss Plateau (3): Add 2 land forts. Vorarlberg owner gains opinion −10. |
| **Case North** | Fortify Austrian Border AND Balance right | Unlocks "Case North" decision. Biggest Fascist gains opinion −20 ("Is planning against us"). |
| **Freeze German Assets** | Case North AND Balance left | Biggest Fascist gets "Assets Frozen by Switzerland" spirit (365 days): Switzerland Civilian industry +10.00%, Military industry +10.00% to target. Fascist gains opinion −75. |
| **Fund Resistance Groups** | Case North AND Balance left AND any European capital at war exists | Unlocks "Fund Resistance Groups in country" decision. |
| **Adopt the Rumantsch Language** | Pro Helvetia AND Balance >0% Cantons side | Balance shifts +10% towards Cantons. Gains modifier "Adopted the Rumantsch language" (Balance daily +0.10%). Fascist nations gain opinion −10. |
| **Patriotic Shooting Clubs** | Pro Helvetia AND Balance >0% Cantons side | Manpower +20000. Maximum Military Readiness +30, increases Military Readiness +30, Minimum Military Readiness −30. Suspicious nations gain opinion −10 (if start before 1936.01.02). |
| **Train Swiss Women** | (Adopt Rumantsch OR Patriotic Shooting Clubs) AND Balance >0% Cantons side | Gets "Swiss Women in the Military" spirit (Recruitable Population +20%). Suspicious nations gain opinion −10. |
| **Aktion Nationaler Widerstand** | Patriotic Shooting Clubs AND Balance >0% Cantons side | Military Readiness +30. Gets "Aktion Nationaler Widerstand" spirit (Recruitable Population +5%, Surrender Limit +10%, Resistance Target in occupied states +25%, Damage to Enemy Garrisons +30%, Democracy Support +0.05 daily). |
| **Heer und Haus** | Aktion Nationaler Widerstand AND Balance >0% Cantons side | Every Swiss core state: Add "Heer und Haus" modifier (Resistance Decay −30%, Resistance Growth +20%, Resistance Activity Chance +30%, Citizen Militias Deployed timeout +20 days). |
| **Ortswehren** | Heer und Haus AND Balance >0% Cantons side AND NOT Citizen Militias professionalized | Every Swiss core state: Add "Ortswehren preparations" (Division Defense +25%, Reinforce Rate +3%, Max Entrenchment +20%, Damage Reduction vs CAS +10%, Fort Combat Damage Chance −20%). Suspicious nations gain opinion −10. |
| **Luftschutz** | Heer und Haus AND completed Radar project AND researched Towed Anti-Air AND Balance >0% Cantons side AND NOT professionalized | Western/Eastern Swiss Alps (847/151): Add 1 radar station each. Every Swiss core: Add 2 anti-air. Manpower −20000. Suspicious nations gain opinion −10. |
| **The Spirit of Resistance** | Ortswehren AND Luftschutz | Gets "Swiss Spirit of Resistance" spirit (Division training time −15%, Stability +10%, Surrender Limit +40%. If militia time >1: reduce by 1 day. Citizen Militias Deployed timeout +30 days. Military Readiness +60). Random state: Add 2 building slots, 1 military factory, 1 civilian factory. |

## Allied Gold / Purchase American Planes Sub-branch

Democratic alliance path. Seeks ties with Allies and purchases US aircraft.

| Focus | Prerequisites | Effects |
|---|---|---|
| **Allied Gold** | Ban Foreign Nazi Propaganda AND Federal Assembly >65% AND Balance left of Full Cantonal Power | Unlocks "Open banks to Democratic Nation" decision. |
| **Purchase American Planes** | Ban Foreign Nazi Propaganda AND Federal Assembly >80% AND (Major Democratic exists with tech OR bypasses if not) | Unlocks decisions to purchase Fighter and Close Air Support from USA or best Democratic ally. 50× Basic Small Airframe, 50× A-17 added to stockpile. **Arms Against Tyranny DLC:** Equipment subsidies (500 construction cost each for Fighter/CAS from USA). Non-democratic sellers gain opinion −25; seller gains +40. |
| **Closer Democratic Ties** | Allied Gold AND Purchase American Planes AND Federal Assembly >70% AND Balance left of Council/Cantons AND **mutually exclusive with Gotthardbund** | All major Democratic nations gain "Close Ties" opinion +60. Major Fascist nations gain opinion −25. Political Power +100. |
| **Connect to the Maginot Line** | Closer Democratic Ties AND Federal Assembly >70% AND Balance left | Jura Mountains (845), Swiss Plateau (3), Eastern Swiss Alps (151): Each Add 8 land forts. Germany gains opinion −25. Balance nations gain opinion +25. |
| **American Industrial Investments** | Closer Democratic Ties AND Federal Assembly >70% AND Balance left AND (USA exists and not Fascist and at peace) | USA Democracy popularity +5%. USA gets event "Switzerland Wants Investment"; if accept: "Foreign Investments" spirit (730 days): Political Power daily +10%, Construction Speed +20%. |
| **Take a Stance** | (Connect to Maginot OR American Industrial Investments) AND Fascism <30% AND Balance left | Political Power +100. "Absolute Neutrality" decisions disabled. "Swiss Neutrality" spirit removed. Unlocks decision "Seize Gold of Fascist Nation" (if Axis Gold completed and 1+ Fascist has "Using Switzerland to trade gold"). |
| **Join France** | (Connect to Maginot AND Take a Stance) AND Federal Assembly >70% AND Balance left of Strong Council AND France exists/not capitulated/Democratic/independent AND **mutually exclusive with Join Alliance, Secret Pact** | Becomes puppet of France. Spirit of Helvetia becomes Aggressive: War support +15% (or +30% if at war), Factory output +7% (or +0% if at war), Command power daily +0.20 (or −10% if at war), Special Forces Capacity +25%, Breakthrough +25% (if at war), Organization +20% (if at war), Manpower Recruitable +25% (if at war), Org loss when moving −15% (if at war). |
| **Join the Alliance** | Take a Stance AND Fascism <30% AND Balance left AND (Major Democratic faction leader exists at peace) AND **mutually exclusive with Join France, Secret Pact** | Best Democratic/UK/suitable Democratic faction leader gets event to invite Switzerland. Spirit of Helvetia becomes Aggressive (same modifiers). Swiss Citizen Militias → Limited Conscription (Recruitable +2.50%), Expanded → Extensive Conscription (Recruitable +5.00%, Training +10%). All militia divisions become Regular Infantry; militia decisions disabled; all templates editable. |
| **The Second Helvetic Republic** | Join France AND Balance at Full Council Control AND Weekly Balance change <1% towards Cantons | Becomes Dominion of France, renamed "République Helvétique". Conscriptions swap (same as Join Alliance). All militia divisions become Regular Infantry. |
| **Alpine Aspirations** | The Second Helvetic Republic AND Balance at Full Council Control AND Weekly change <1% towards Cantons | All non-core Alpine states: Become Swiss cores. France gets event "Switzerland Claims Our Alpine Territories"; if accept, Switzerland gains those Alpine states (likelihood based on Swiss military size and French opinion). |
| **Lay the Groundwork** | (Join France OR Join Alliance OR Secret Pact) AND Federal Assembly >70% AND Balance left of Strong Cantonal Power | Build level 2 railway N. Saskatchewan (865)→Swiss Plateau (3). Build level 1 railway Swiss Plateau (3)→Eastern Swiss Alps (151). Eastern Swiss Alps (151): Add 1 supply hub. Every state with <3 infrastructure: Add 1 infrastructure. |
| **Arsenal of the Alps** | Lay the Groundwork AND Federal Assembly >70% AND Balance left of Strong Cantonal Power | Western Swiss Alps (847), Eastern Swiss Alps (151), Ticino (846): Each add 3 building slots, 3 military factories. |
| **Fighting for the Hills** | Arsenal of the Alps AND Federal Assembly >70% AND Balance left of Strong Cantonal Power | Army experience +100. 2× 100% research bonus for Infantry tech, Infantry Weapons. 2× 50% cost reduction for Land Doctrine. |
| **Thunder in the Valleys** | Arsenal of the Alps AND Federal Assembly >70% AND Balance left of Strong Cantonal Power | Army experience +100. 4× 100% research bonus for Armor tech. |
| **Fly Over the Mountains** | Arsenal of the Alps AND Federal Assembly >70% AND Balance left of Strong Cantonal Power | Air experience +150. 3× 100% research bonus for Aircraft. 2× 50% cost reduction for Air Doctrine. |
| **Weapons of Democracy** | (Fighting for Hills AND Thunder in Valleys AND Fly Over Mountains) AND Federal Assembly >70% AND Balance left of Strong Cantonal Power | +1 research slot. Nuclear Research breakthrough +75%. 1× 50% research bonus for Nuclear tech. |
| **The Alpine Confederation** | (Alpine Aspirations OR Weapons of Democracy) AND Democratic AND any Alpine non-core state exists AND President ideology matches | Renamed "The Alpine Confederation". If puppet: can lead to independence war; overlord gets event (likely based on Swiss military, overlord opinion). |
| **Exiled Government** | Weapons of Democracy AND Federal Assembly >70% AND in faction AND Surrender >50% | Becomes Government in Exile of faction leader. |

## Gotthardbund Sub-branch

Centralization/expansionist path. Seeks to unify Alpine states and may shift ideology.

| Focus | Prerequisites | Effects |
|---|---|---|
| **Gotthardbund** | (Fortify Border Italy/Germany/France) AND (Federal Assembly >60% OR Balance right of Strong Council Control) AND **mutually exclusive with Closer Democratic Ties** | Gets "Gotthardbund" spirit. Unlocks "Gotthardbund Movement" decision. Austria/Liechtenstein (if exist): gain opinion −30. |
| **Confederation Ideology** | Gotthardbund AND Balance >50% Council side | Balance +0.05 daily. Political Power +50. Gains "Confederation Ideology" modifier. |
| **Expand Alpine States** | Confederation Ideology | Gain claims on Alpine states (Austria, Liechtenstein, Savoy). |
| **Vorarlberg Claim** | Expand Alpine States | Vorarlberg (Austria 848): Gain claim. |
| **Annex Liechtenstein** | Vorarlberg Claim AND Austria does not exist AND owns Vorarlberg | Liechtenstein: Becomes core, annexed. Liechtenstein owner gains opinion −50. |
| **Promote the Confederation President** | Gotthardbund | Allows ideology shifts: can pick Communist, Non-Aligned, or Democratic president. Each unlocks different paths. |
| **Communist Confederation** | Promote President AND Communist >10% | Becomes Communist. Gets "Communist Confederation" spirit. Forms "Alpine Union" (if non-aligned president) or "Alpine Protectorate" (if non-aligned). Political Power +100. |
| **Neutral Alpine Power** | Promote President AND Neutralism >10% | Becomes Non-Aligned. Gets "Neutral Alpine Power" spirit. Forms "Alpine Protectorate" (if non-aligned). Claims expanded. |
| **Democratic Alpine Confederation** | Promote President AND Democracy >15% | Stays Democratic. Gets spirit, claims expanded. Can form Alpine Confederation. |
| **Centralize the Cantons** | (Communist Confederation OR Neutral Alpine Power OR Democratic Alpine Confederation) AND Balance >60% Council side | Manpower +15000. War support +10% (if Communist/Non-Aligned). Political Power +75. |
| **Alpine Defense League** | Centralize the Cantons AND own alpine states | Defense alliance with Alpine nations. Military coordination bonuses. |
| **Restore the Confederation** | (Communist Confederation OR Neutral Alpine Power) AND several conditions | Can restore to Democratic if stability/support sufficient. Removes faction affiliation, returns to independent status. |
| **The Alpine Union** | (Communist AND own sufficient Alpine territory) | Forms "Alpine Union" tag if Communist and controls territory. Becomes faction leader for Communist bloc in region. |
| **The Alpine Protectorate** | Non-Aligned AND own Alpine territory | Forms "Alpine Protectorate" tag if Non-Aligned. Independent faction status. |
| **(other Gotthardbund branch focuses)** | Various Alpine expansion, economic, and military focuses | [Long list of focuses related to Alpine state management, military buildup, ideology-specific paths to communism/non-aligned/democracy; exact mechanics tied to Balance slider and ideology thresholds] |

## A Swiss Navy Sub-branch

Naval expansion path (relevant if Switzerland gains coastline, e.g. via Gotthardbund).

| Focus | Prerequisites | Effects |
|---|---|---|
| **A Swiss Navy** | (Switzerland on the Offense OR Neutral Entente) AND Federal Assembly <80% AND FB <20% AND any coastal state exists | Navy experience +100. 2× 100% research bonus for Ships. |
| **Swiss Ship Designs** | A Swiss Navy AND **mutually exclusive with Buy Foreign Surplus Ships** AND Federal Assembly <80% AND any coastal state exists | 1× 200% research bonus for Ships. Gain Werner-Risch (Naval Designer): Naval Research Speed +15%, Screens Max Range +30%, Sub detection +10%, Max Speed +10%. |
| **Buy Foreign Surplus Ships** | A Swiss Navy AND **mutually exclusive with Swiss Ship Designs** AND any coastal state exists | Unlocks decision to purchase surplus ships from foreign navy. |
| **Naval Base Expansion** | (Swiss Ship Designs OR Buy Foreign Surplus Ships) AND any coastal state exists | Coastal states: Add dockyard slots. Dockyard output +10%. |
| **Submarine Program** | A Swiss Navy AND Federal Assembly <80% | 1× 150% research bonus for Submarine tech. Submarine research speed +20%. |
| **Torpedo Development** | Submarine Program | Unlocks naval strike force doctrines. 1× 100% research bonus for Torpedo tech. |

## Support Allied Espionage Sub-branch

Intelligence and covert operations against fascist powers (**La Résistance DLC**).

| Focus | Prerequisites | Effects |
|---|---|---|
| **Support Allied Espionage** | (Closer Democratic Ties OR Take a Stance) AND La Résistance enabled | Unlocks espionage operations. Gain intelligence operatives. |
| **Establish Safe Houses** | Support Allied Espionage AND La Résistance | Creates spy network infrastructure in Switzerland. Creates covert infrastructure in target regions. |
| **Sabotage German War Machine** | (Establish Safe Houses OR other espionage focus) | Unlocks sabotage missions against German military/industrial targets. Reduces target war production. |
| **Operation Tannenbaum Intelligence** | Espionage focus tree | Gathers intelligence on German "Operation Tannenbaum" (invasion plan). Increases defensive preparedness. |
| **Support Resistance Movements** | Espionage/Allied path | Supports anti-Fascist resistance in German-occupied regions. Increases occupation penalties for Germany. |

## Promote Henri Guisan / Frontier Defense Plan Sub-branch

Military leadership and defensive preparation.

| Focus | Prerequisites | Effects |
|---|---|---|
| **Promote Henri Guisan** | (Armed Neutrality OR Defensive path focus) AND Federal Assembly >40% | Promotes General Henri Guisan as military advisor. Gets "Henri Guisan" trait modifiers: Division Defense +15%, Fort efficiency +20%, Army Experience gain +10%. |
| **Frontier Defense Plan** | Promote Henri Guisan AND Balance right | Unlocks "Frontier Defense Plan" decision. Fortifies all border provinces. Defensive War Penalty modifier −20%. |
| **Reduce Neighboring Nation Tensions** | Frontier Defense Plan | Neighboring major nations gain "Switzerland Fortified" opinion −15. Balance of Power becomes harder to shift. |
| **Rearm the Border Garrisons** | Frontier Defense Plan | Border garrison units receive +30% organization. Fort garrison strength +25%. |
| **Alpine Fortress Strategy** | (Promote Henri Guisan AND own alpine terrain) | Entrenchment speed +30%. Max entrenchment +50. Alpine/Mountain terrain defense bonus +15%. |

## Federal Police Intelligence Department Sub-branch

Internal security, ideology suppression, and domestic intelligence.

| Focus | Prerequisites | Effects |
|---|---|---|
| **Federal Police Intelligence Department** | (Buero Ha OR Pro Helvetia) AND Fascism/Communism >5% | Creates Federal Police Intelligence agency. Enables ideology suppression decisions. Gets "Federal Police" spirit (Fascism Support −0.05, Communism Support −0.05 daily). |
| **Suppress Ideological Movements** | Federal Police Intelligence | Fascism/Communism popularity −3.00%. Political Power +100. |
| **Monitor Foreign Agents** | Federal Police Intelligence | Improves counter-intelligence. Foreign spy networks −50% effectiveness in Switzerland. |
| **Arrest Fascist Sympathizers** | Suppress Ideological Movements AND Fascism <8% | Fascism popularity −5.00%. Political Power +75. Fascist nations gain opinion −20. |
| **Enforce Democratic Order** | (Arrest Fascist Sympathizers OR Federal Police focus chain) | Democracy popularity +3.00%. Stability +5%. War support +10% (if democracy focus path). |

## Purchase German Planes Sub-branch

Fascist appeasement path. Buys German aircraft; appeases Germany and Italy.

| Focus | Prerequisites | Effects |
|---|---|---|
| **Purchase German Planes** | (Fortify Border Italy/Germany) AND Federal Assembly <40% AND Balance right of Strong Council Control | Unlocks decision to purchase Fighter planes from Germany. 50× Fighter added to stockpile. Germany gains opinion +40. Democratic nations gain opinion −25. Air experience +50. |
| **Closer Ties with Germany** | Purchase German Planes AND Balance right of Strong Council Control | Germany gains "Friendly Switzerland" opinion +50. Unlocks "Trade with Germany" decision (resources for equipment). Trade agreements activated. |
| **German Military Mission** | Closer Ties with Germany | German military advisors arrive. Army Experience +75. 1× 50% research bonus for Land Doctrine. Infantry Weapons research +10%. |
| **German Technical Exchange** | German Military Mission | 1× 75% research bonus for Fighter tech. Air research speed +10%. |
| **German Industrial Partnership** | Closer Ties with Germany AND Balance right | Unlocks "German Economic Pact" decision. Construction speed +15% (while at peace with Germany). Trade route capacity +50 (to Germany). |

## Closer Ties with The German Reich Sub-branch

Fascist alignment path. Becomes fascist and can choose puppet or independence status.

| Focus | Prerequisites | Effects |
|---|---|---|
| **Turn Fascist** | (Balance right of Full Council Control) AND Fascism >30% | Becomes Fascist ideology. Gets "Fascist Confederation" spirit. Embraces Axis ideals. Joins Axis if at war or Germany demands. |
| **Promote Tobler** | Turn Fascist | Promotes Tobler (Fascist leader). **Independent fascist path:** Stays independent. Gains "Tobler's Switzerland" spirit (War support +20%, Factory output +5%). Can form "Alpine Supremacy" faction. Political Power +100. |
| **Promote Henne** | Turn Fascist | Promotes Henne (Nazi sympathizer). **Puppet path:** Joins Germany as puppet → "Schweizerische Reichsprotektorat". Gets German military bonuses. Army receives +100 experience. Joins Axis unconditionally. If becomes puppet, all militia conscription replaced with German-style conscription. |
| **Alpine Supremacy** | (Promote Tobler AND independent fascist path) | If independent fascist: Forms "Alpine Supremacy" faction (fascist alpine alliance). Becomes faction leader. Can invite Austria, Italy, Hungary. Fascist nations gain opinion +50. |
| **Schweizerische Reichsprotektorat** | (Promote Henne AND Puppet of Germany) | Tag changes to "Schweizerische Reichsprotektorat" (German Protectorate). No independence path; integrated into German war effort. German military factories +10% (via protectorate bonuses). Cannot break puppet status without full war. |
| **Expand Axis Presence** | (Promote Tobler OR Promote Henne) | Unlocks "Axis Base Agreement" decision. Allows German troops to stage through Swiss territory (in exchange for resources/protection guarantee, which is revoked easily). War support +15%. |
| **German Occupation Plans** | Closer Ties with Germany (pre-fascist) OR Fascist path | Unlocks "Allow Operation Tannenbaum" decision. Germany can invade if strategic value rises. Removes some defensive preparations unless active defenses completed. |

## Expand Weapons Industry Sub-branch

Military industry and arms production expansion.

| Focus | Prerequisites | Effects |
|---|---|---|
| **Expand Weapons Industry** | (Armed Neutrality OR Defensive path focus) AND military industry >0 | Random state: Add 2 building slots, 2 military factories. Gets "Weapons Industry Expansion" spirit (Military factory construction +15%). |
| **Infantry Weapons Modernization** | Expand Weapons Industry | 1× 150% research bonus for Infantry Weapons. Infantry Weapons production cost −10%. |
| **Artillery Production** | Expand Weapons Industry | 1× 100% research bonus for Support Artillery. Support artillery production cost −15%. |
| **Anti-Tank Production** | (Infantry Weapons OR Artillery Production) | 1× 100% research bonus for Anti-Tank tech. Anti-tank gun production +20%. |
| **Air Force Expansion** | Expand Weapons Industry AND Fascism <20% | Air Base construction speed +25%. Air experience +75. 1× 100% research bonus for Fighter tech. Airplane production cost −10%. |
| **Armor Industry Development** | Expand Weapons Industry AND (Army focuses completed) | 1× 125% research bonus for Armor tech (if researched to certain level). Tank production cost −20%. |
| **Small Arms Innovation** | Infantry Weapons Modernization | Small arms production capacity +30%. Infantry Weapons upgrade cost −15%. |

---

## Key Mechanics

### Balance of Power Slider

Switzerland's tree is gated by a "Balance of Power" slider between **Federal Council (left) and Cantons (right)**:
- Many focuses require the slider to be in a specific zone (e.g., "right of Strong Council Control", "left of Full Cantonal Power").
- Some focuses shift the slider (e.g., Adopt the Rumantsch Language moves it +10% right).
- Modifiers grant ongoing slider movement (e.g., "+0.10% daily").

### Spirit of Helvetia

A core mechanic that shifts based on path and war status:
- **Passive Spirit of Helvetia** (peace default): Political Power daily +0.20, Recruitable −15%, War support −20%, Military factory −5%, Civilian factory +15%.
- **Defensive Spirit of Helvetia** (Armed Neutrality + defensive focus): Factory output +5%, Max Entrenchment +30, Command power daily +0.10, Military factory +15%, Fort construction +20%; if at war, Recruitable +25%, War support +30%, Division Defense +25%, Entrenchment +50%, Defensive War Penalty +50%.
- **Aggressive Spirit of Helvetia** (Join Alliance/France or offensive): War support +15% (or +30% at war), Factory output +7%, Command power daily +0.20, Special Forces +25%, Organization +20% (at war), Recruitable +25% (at war), Breakthrough +25% (at war).

### Continuous Focus (requires 10 regular focuses)

**Build up Military Readiness** (requires By Blood Alone): Swiss-specific, unlocks "Building up Military Readiness" mission (−1 PP daily while active).

**Support Active Militias** (requires By Blood Alone): Requires Citizen Militias Deployed modifier active: Militia Attack +30%, Defense +30%, Speed +30%, Organization +15%.

### Conscription Laws

- **Swiss Citizen Militias** (default): Low recruitable population, high manpower recovery, militia-focused.
- **Expanded Swiss Citizen Militias**: Increased recruitment cap.
- **Limited Conscription** (if Join Alliance): Recruitable +2.50%.
- **Extensive Conscription** (if Join Alliance): Recruitable +5.00%, Training +10%.

All militia divisions convert to Regular Infantry if alliance/puppet path taken.

---

## DLC Notes

- **By Blood Alone** required to unlock the unique Swiss tree; without it, Switzerland uses the generic tree.
- **La Résistance**: Enables "Buero Ha" to create an Intelligence Agency (Hans Hausamann operative) instead of just intelligence bonuses; enables "Support Allied Espionage" sub-branch fully.
- **Arms Against Tyranny**: Adds equipment subsidy decisions for purchasing planes.

---

## Strategic Notes

- **Democratic path (Ban Foreign Nazi Propaganda chain)**: Heavy military readiness/militia focus; defensive; suitable for armed neutrality.
- **Allied path (Allied Gold chain)**: Join faction, convert militia to conscription, access industrial tech from allies.
- **Gotthardbund**: Expansionist, can pivot to any ideology; risky if surrounded by major powers.
- **Fascist path**: Vulnerable to becoming German puppet; independent fascism (Tobler) weaker but free.
- **Navy path**: Only viable if gaining coastline (Gotthardbund or conquest); otherwise economical drain.

> **⚠️ Note:** Some wiki templates contained broken syntax like `[{{{1}}}]` which was reconstructed from context as ideology/faction references. Balance of Power slider exact thresholds and some conditional effects may shift with patches post-wiki documentation date.
