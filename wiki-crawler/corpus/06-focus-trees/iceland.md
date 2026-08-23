---
title: Icelandic National Focus Tree
category: focus-trees
tags: [iceland, focus tree, arms against tyranny, nordic, industrial, political]
game_version: "1.19"
dlc: [Arms Against Tyranny]
sources:
  - https://hoi4.paradoxwikis.com/Icelandic_national_focus_tree
---

## Summary

Iceland gains a unique focus tree with the Arms Against Tyranny DLC; without it, Iceland uses the generic tree. The tree offers six major branches: industrial development (fishing, minerals, shipping, heavy industry, technology), international trade and economy, political identity and independence from Denmark (choices between monarchism, democracy, fascism, and communism), military modernization, and—as a Nordic nation—access to the joint Nordic Council branch when allied with other Nordic countries.

See [Iceland](../05-countries/iceland.md) for the country's 1936 starting profile.

## Expand the Fishing Industry / Mineral Prospecting Branch

The industrial core of Iceland's development. Mutually exclusive opening choice between fishing (production cost −10% for convoys, consumer goods −10%, supply efficiency +5%) and mineral prospecting (adds building slot, civilian factory, +10 steel production, +6 aluminum production to a random state). Hydroelectric Power requires one of either; subsequent branches (shipping, heavy industry, advanced technology) are mutually exclusive at Hydroelectric Power level.

| Focus | Prerequisites | Mutually Exclusive | Effects | Notes |
|---|---|---|---|---|
| Expand the Fishing Industry | None | Mineral Prospecting | Gain national spirit: −10% production cost for convoys, −10% consumer goods factories factor, +5% supply efficiency | Starting choice |
| Mineral Prospecting | None | Expand the Fishing Industry | Random owned state: +1 building slot, +1 civilian factory; +10 steel and +6 aluminum production to state 100 | Starting choice |
| Agricultural Expansion | Expand the Fishing Industry | None | Stability +5.00%; 2 random states +3 building slots each, 1 random state +1 civilian factory | Farming modernization |
| Hydroelectric Power | Expand the Fishing Industry OR Mineral Prospecting | None | Random state +1 building slot, +1 civilian factory; modifies national spirit with construction +10.00%, production efficiency cap +5.0%, dockyard output +5.00%, factory output +5.00% | Gateway focus |
| Off Shore Oil Drilling | Mineral Prospecting | None | Unlocks decisions to drill for oil around Iceland | Oil exploration |
| Develop Icelandic Shipping | Hydroelectric Power | Heavy Industry, Advanced Technology | 2× 50% research bonus for Ships; 1× 50% research bonus for Naval Doctrine; Eimskip (Shipping Concern) available; convoy production cost −5.00%, ship repair speed +10%, naval dockyard construction +10.00% | Naval specialization |
| Heavy Industry | Hydroelectric Power | Develop Icelandic Shipping, Advanced Technology | 2× 50% research bonus for Industry | Industrial specialization |
| Advanced Technology | Hydroelectric Power | Develop Icelandic Shipping, Heavy Industry | 2× 50% research bonus for Electronics | High-tech specialization |
| Reykjavik Dockyards | Develop Icelandic Shipping (requires state 100 owned/controlled; bypasses if 0 more naval dockyards buildable) | None | State 100: +2 building slots, +2 naval dockyards | Shipping branch only |
| Expand the Harbor | Develop Icelandic Shipping OR Heavy Industry (requires state 100 owned/controlled) | None | State 100: +1 building slot, +1 naval dockyard; if <10 naval bases, +2 naval bases | Harbor upgrade |
| Local Arms Industry | Heavy Industry | None | Random state: +2 building slots, +2 military factories | Heavy industry only |
| Infrastructure Development | Heavy Industry OR Advanced Technology (state 100 fully controlled) | None | Random state: +1 building slot, +1 infrastructure; build level-1 railway in state 100; 2 random states +2 building slots | Multi-path |
| Iceland Air | Advanced Technology (state 100 fully controlled) | None | 2× 50% cost reduction for Air Doctrine; +500 production cost subsidy for Fighters and Tactical Bombers (any allied); if <10 air bases, +1 air base | High-tech only |
| Expand the Civilian Fleet | Reykjavik Dockyards | None | +50 convoy units in stockpile; national spirit: convoy production cost −20.00%, troop convoy requirements −10% | Naval production focus |
| Industrial Research School | Local Arms Industry OR Reykjavik Dockyards OR Iceland Air | None | +1 research slot | Research bonus |
| Hrafninn Flýgur | Iceland Air | None | 2× 25% research bonus for Aircraft; 1× 50% cost reduction for Air Doctrine; +50 air experience; random state: +1 building slot, +1 military factory | Advanced airpower |

## International Trade Branch

Economy and diplomatic path independent of the fishing/minerals split. Opens automatically if Iceland is fully independent. Bypasses if economy law is not Isolation.

| Focus | Prerequisites | Effects | Requirements |
|---|---|---|---|
| International Trade | Iceland fully independent (bypasses if not Isolation economy law) | +100 political power; if Isolation: replace with Civilian Economy (−5.0% expected consumer goods factories, −10% conversion costs both ways); war goal/join faction/lend-lease/send volunteers/guarantee tensions all −20.0% to −100.0%; fuel +10.00%, fuel capacity +10.00%; agency upgrade −80.0%; military/civilian factory/naval dockyard construction +10.00/+10.00/+40.00%; gains Free Trade (construction +15.00%, research +10.00%, factory output +15.00%, dockyard output +15.00%, resources to market +80%, civilian/navy intel to others +40.0%/+20.0%) | Fully independent |
| Banking on the Future | International Trade | Modifies national spirit: consumer goods factories −15.0%; +1 offmap military factory, +1 offmap civilian factory; every major country same ideology as Iceland or Non-Aligned: trade relations +25 | Trade benefits |
| Infiltration | International Trade (requires La Résistance DLC enabled) | Create intelligence agency if not present; apply Form Department upgrade if not applied; +10 decryption speed | La Résistance DLC only |

## The Kingdom of Iceland Branch

Democratic/monarchist path emphasizing partnership with Denmark or neutrality. Mutually exclusive with Not Our King (communist/fascist).

### Main Path: The Kingdom of Iceland → United We Stand

| Focus | Prerequisites | Effects | Requirements |
|---|---|---|---|
| The Kingdom of Iceland | None | Mutually exclusive with Not Our King; Non-Aligned +10.00%; +100 political power; available advisors: Björn Þórðarson (Traditionalist, +15% PP gain) and Hermann Jónasson (Democratic Reformer, +0.10 daily democracy support) | None |
| United We Stand | The Kingdom of Iceland; >5% world tension (mutually exclusive with Declare Absolute Neutrality) | Replace Isolation with Early Mobilization (−10.0% consumer goods, −40.00% conversion costs, war goal/join faction/lend-lease/send volunteers/guarantee tensions −20.0% to −100.0%, fuel +25.00%, fuel capacity +35.00%, factory/naval dockyard construction +30.00/+40.00%); Denmark gains Offered Support (+25 opinion) | Democratic or Non-Aligned ruling party, or subject of Denmark; Denmark completed Start the Rearmament or Unify the Right |
| Joint Shipbuilding Program | United We Stand (Democratic or Non-Aligned) | +25 navy experience; random coastal state: +1 building slot, +1 naval dockyard; create Ægir Class coastal defense ship; Denmark gains same building bonuses | Naval cooperation |
| Patrolling the Atlantic | Joint Shipbuilding Program (Democratic or Non-Aligned) | +25 navy experience; 2× 25% research bonus for Destroyer Models; if not fully independent, overlord gains 1× 25% research bonus for Destroyer Models | Destroyer specialization |
| Industrial Cooperation | Patrolling the Atlantic (Democratic or Non-Aligned; subject of or in faction with Denmark) | 1× 20% research bonus for Industry; random state +1 building slot; available industrial concern: Aalborg Portland (excavation +15%, infrastructure construction +10.00%, railway construction +10.00%) | Economic cooperation |
| Royal Marines | United We Stand (Democratic or Non-Aligned) | +50 navy experience; national spirit Víkingasveitin: special forces minimum capacity +24, special forces non-combat out of supply −25.00%, marines attack +5.00%; 1× 50% research bonus for Landing Craft | Military specialization |
| Joint Military Training | Royal Marines (Democratic or Non-Aligned) | +25 army experience; 1× 25% cost reduction for Land Doctrine; overlord gains same doctrine cost reduction | Army cooperation |
| Not Standing Idly By | Patrolling the Atlantic OR Joint Military Training (>15% world tension, Democratic or Non-Aligned) | If Disarmed Nation: replace with Limited Conscription; if Volunteer Only, replace with Limited Conscription; national spirit Home Guard: +2.50% recruitable population | War readiness |
| Fighting as Equals | Not Standing Idly By (Democratic or Non-Aligned; subject of Denmark; at war; bypasses if fully independent or subject of non-Denmark) | Denmark receives event "Equal Partners"; Iceland declares independence | Equality declaration |
| Compensation | Fighting as Equals (Greenland 101 owned by Denmark OR Faroe Islands 337 owned by Denmark) | Denmark receives event "[Leader] Wants Compensation" | Territorial concessions |
| The Icelandic Police Force | United We Stand OR Declare Absolute Neutrality (Democratic or Non-Aligned) | +25 army experience; 1× 20% cost reduction for land doctrine; +2000 manpower | Alternative military |
| Expand the Industrial Complexes | Patrolling the Atlantic OR Joint Military Training OR Garður Airfield OR The Merchant Fleet (Democratic or Non-Aligned) | Every military industrial organization: +200 funds; +1 offmap military factory | Military expansion |
| Expanding the University of Reykjavik | Not Standing Idly By OR Political Unity (Democratic or Non-Aligned) | +1 research slot; modifies national spirit: research speed +10.0% | Education focus |
| Modernizing the Island | Expanding the University of Reykjavik (Democratic or Non-Aligned) | Modifies national spirit: production efficiency cap +10.0%, construction speed +15.0%, dockyard output +10.0%, factory output +10.0% | Modernization |
| State Owned Enterprises | Modernizing the Island (Democratic or Non-Aligned) | Owned controlled cored state: +4 building slots, +2 civilian factories; modifies national spirit: production efficiency cap +10.0% | Industrialization |

### Alternate Path: Declare Absolute Neutrality

| Focus | Prerequisites | Effects | Requirements |
|---|---|---|---|
| Declare Absolute Neutrality | The Kingdom of Iceland (>5% world tension; mutually exclusive with United We Stand; bypasses if fully independent) | If subject: become independent if overlord is declared war upon; Non-Aligned +5.00%; +100 autonomy; national spirit Neutral Foreign Policy: join faction tension +100.0%, send volunteers +20.0%, guarantee tension +100.0%, AI faction desire −100, threat receptivity 1.0%, embargo tension +250.0% | Neutrality commitment |
| Infrastructure Projects | Declare Absolute Neutrality (Democratic or Non-Aligned) | Random state (owned by Iceland or ally): +1 building slot, +1 infrastructure; +1 building slot, +1 naval base | Infrastructure neutral path |
| Garður Airfield | Infrastructure Projects (Democratic or Non-Aligned) | +25 air experience; state 100: +1 air base; 2× 25% research bonus for Aircraft; +25 transport plane units in stockpile | Airfield development |
| Engineering Projects | Declare Absolute Neutrality (Democratic or Non-Aligned; bypasses if subject of Denmark) | Random coastal state: +1 building slot, +1 civilian factory; 2× 25% research bonus for Industry; if subject, overlord gains 1× 25% research bonus | Neutral infrastructure |
| The Merchant Fleet | Engineering Projects (Democratic or Non-Aligned) | +50 convoy units in stockpile; modifies national spirit: consumer goods factories −5.0% | Merchant marine focus |
| Political Unity | Garður Airfield OR The Merchant Fleet (>15% world tension, Democratic or Non-Aligned) | +50 political power; stability +10.00%; available advisors: Ísleifur Högnason (trade unionist, +10% production efficiency cap, −30% lack of resources), Einar Olgeirsson (editor, +5% PP gain, +5.00% stability); daily communism support +0.02 | Unity building |
| Anglo-Icelandic Relations | The Merchant Fleet (Democratic or Non-Aligned) | If completed Expand the Fishing Industry: modify that spirit to add construction +10.00%, supply efficiency +10%, convoy production cost −10.00%; UK gains huge opinion boost (+50); +500 production cost fighter subsidy to UK/Canada | British alliance |
| American Protection | Political Unity (Democratic or Non-Aligned; fully independent or subject of UK; US is democratic, at war) | US receives event "Iceland Requests American Protection"; if accepts, Iceland becomes US puppet | US protection option |
| Keflavík Airbase | American Protection (subject of/in faction with US; Democratic or Non-Aligned; US is democratic, has researched Towed Anti-Air) | State 100: +3 air bases, +3 anti-air; modifies national spirit: consumer goods factories −5.0% | US military base |
| American Investments | Keflavík Airbase (subject of/in faction with US; Democratic or Non-Aligned; US is democratic) | State 100: +2 building slots, +1 civilian factory; modifies national spirit: dockyard/factory output +5.0%; available industrial concerns: Esso (refining, +5% industrial research, +15% synthetic research, +10.00% synthetic oil), Vífilfell (+15.0% consumer goods reduction, +10.00% stability) | Economic integration |
| Host American Soldiers | American Investments (subject of/in faction with US; Democratic or Non-Aligned; US is democratic) | National spirit Hosting American Soldiers: +50 weekly manpower | Troop basing |
| Iceland Defense Force | Host American Soldiers (subject of/in faction with US; Democratic or Non-Aligned; US is democratic) | 1× 25% research bonus for Support Artillery; 3× 25% research bonus for Infantry Weapons; 3× 25% research bonus for Support Technology; 1× 25% research bonus for Electronics; +50 army experience | Defense modernization |
| Trade Relations | Political Unity (Democratic or Non-Aligned) | +500 production cost truck subsidy to any allied; +500 production cost towed artillery subsidy; +500 production cost infantry equipment subsidy | Economic diplomacy |
| Republicanism | Trade Relations (Democratic or Non-Aligned) | +150 political power; stability +10.00%; current leader gains Independence Advocate (stability +15.00%), daily autonomy gain +0.1; all autonomy gain +20.0%; if fully independent, receives event Presidential Elections | Republican transition |

## Not Our King Branch

Communist/fascist path breaking independence from Denmark. Mutually exclusive with The Kingdom of Iceland. Leads to either worker's revolution (Embrace the Workers' Revolution → communist path) or state corporatism (State Corporatism → fascist path), both mutually exclusive.

| Focus | Prerequisites | Mutually Exclusive | Effects | Requirements |
|---|---|---|---|---|
| Not Our King | None | The Kingdom of Iceland | +75 political power; fascism +10.00%, communism +5.00%; modifies national spirit Christian X: stability −15.00%, division defense on core territory +5.0% | Anti-monarchist opening |
| Expand the Industrial Base | Not Our King | None | Random state +1 building slot, +1 civilian factory; modifies national spirit: consumer goods −5.0% | Industrial expansion |
| International Relations | Expand the Industrial Base (>20% communist support) | None | +1 offmap civilian factory; if Isolation: replace with Civilian Economy (−5.0% consumer goods, −10% conversion costs, war goal/join/lend/volunteers/guarantee −20% to −100%, fuel +10.00%, capacity +10.00%, factory/naval construction +10.00/+40.00%) | Communist alignment |
| Rally the Workers of Reykjavik | Expand the Industrial Base (>10% communist or fascist support, not completed Break With the Crown) | None | Non-Aligned −5.00%, democracy −10.00%; when completing Break With the Crown: modifies national spirit with dockyard/factory output +5.0% | Worker mobilization |
| General Strike | Rally the Workers of Reykjavik (>15% communist support, not Break With the Crown) | None | National spirit General Strike (30 days): consumer goods +50.0%, construction −50.00%, factory output −50.00%; after expires, national spirit Dissent in Working Class (365 days): PP gain −5%, stability −1.00% weekly, communism support +0.02 daily | Labor action |
| Anti-Capitalist Propaganda | Not Our King | None | +100 political power; available advisors: Gísli Sigurbjörnsson (Nazi sympathizer, +75% same ideology opinion, +0.10 daily fascism), Brynjólfur Bjarnason (Marxist philosopher, +10% PP gain, +5.00% research, +0.05 daily communism) | Ideological preparation |
| State Visits | Anti-Capitalist Propaganda (>20% fascist support) | None | Fascism +5.00%; 1× 25% research bonus each: armor, light aircraft, infantry weapons; available advisor: Werner Gerlach (German consul, +50 weekly manpower, +15% same ideology opinion, +5% research, +50 fascist diplomacy acceptance) | Fascist cooperation |
| Prepare for the Revolution | Anti-Capitalist Propaganda (>10% communist or fascist support, not Break With the Crown) | None | When completing Break With the Crown: +5000 manpower, war support +15.00%, stability +5.00% | Revolutionary preparation |
| Organize a March | Prepare for the Revolution (>20% fascist support, not Break With the Crown) | None | Fascism +5.00%, democracy −10.00%, stability −5.00% | Fascist mobilization |
| Break With the Crown | General Strike OR Organize a March (<50% stability, >30% fascist or communist support; bypasses if fully independent or subject of non-Denmark) | None | Iceland becomes independent; if completed Rally Workers: modifies national spirit dockyard/factory +5.0%; if completed Prepare: +5000 manpower, war support +15.00%, stability +5.00%; removes Christian X national spirit; if subject overlord receives event | Independence declaration |
| Embrace the Workers' Revolution | Break With the Crown (mutually exclusive with State Corporatism) | State Corporatism | Stability +5.00%, war support +10.00%; communism +15.00%; Kommúnistaflokkur becomes ruling party; if has Dissent in Working Class, remove it | Communist victory |
| International Brigades | International Relations + Embrace the Workers' Revolution | None | National spirit International Brigades: +50 weekly manpower, max volunteer divisions +4, volunteer requirements −200.0%; deletes Icelandic Expeditionary Force template and recreates it with divisions in state 100 | Communist internationalism |
| Infiltrating the British Isles | International Brigades (UK not communist) | None | Unlocks decisions to start communist uprisings in Wales, Scotland, Northern Ireland; if La Résistance DLC: create intelligence agency (if not present), apply Diplomatic Training and Localized training center upgrades | British subversion |
| State Owned Industry | Embrace the Workers' Revolution | None | Random state +2 building slots, +2 civilian factories; available industrial concern: Landsvirkjun (electronics, +10% electronics research, +5% industrial research) | Communist industry |
| Transformation of Nature | State Owned Industry | None | State 100: +2 building slots; Efficient Energy Production: local factories +15%, available resources +10%, construction +15% | Energy control |
| Recruiting International Workers | Transformation of Nature OR Infiltrating the British Isles | None | +15000 manpower; state 100 +10000 population; every non-100 owned state controlled by Iceland/ally: +5000 population | Workforce expansion |
| International Research Community | Transformation of Nature | None | +1 research slot; modifies national spirit: research speed +5.0%; every communist country not in faction or in faction with Iceland: joins Reykjavik International Research Community research group | Scientific collectivism |
| State Corporatism | Break With the Crown (mutually exclusive with Embrace the Workers' Revolution) | Embrace the Workers' Revolution | Fascism +5.00%; Þjóðernissinna becomes ruling party; random state +2 building slots, +1 military factory, +1 civilian factory; modifies national spirit: dockyard/factory output +5.0% | Fascist state |
| Research Cooperation | State Corporatism + State Visits | None | Every fascist country not at war with Iceland or is major: joins Icelandic Research Organization; modifies national spirit: research +5.0%; available industrial concern: Siemens Iceland (electronics, +15% electronics research) | Fascist research pact |
| Organize the Greyshirts | State Corporatism | None | National spirit Greyshirts: recruitable population +2.50%, recruitable population factor +10% | Militia training |
| The Viking Spirit | Organize the Greyshirts | None | National spirit Ásatrú: PP gain +0.15 daily, war support +5.00%, justify war goal −10.0%; unlocks decision to improve Viking Spirit | Nordic fascism |
| Reclaiming the Empire | The Viking Spirit (does not own Greenland 101, any country owns it and at peace) | None | Claim on Greenland (101); owner receives event "Iceland Demands we Return Greenland"; bypasses if Iceland owns Greenland (101) | Territorial claim |
| Securing the North Sea Passage | The Viking Spirit | None | Claims gained: Faroe Islands (337), Shetland (933), Jan Mayen (914); owners of these provinces receive event "Iceland Declares Protector of North Sea Passage" | Regional claims |
| Vinland | Reclaiming the Empire + Securing the North Sea Passage | None | Claims gained: Newfoundland (331), St Pierre and Miquelon (730), Labrador (332), Côte-Nord (860) | Transatlantic ambitions |

## The Armed Forces of Iceland Branch

Military modernization path available to all ideologies after >10% world tension. Leads to choice between air (Flying Boats) or naval (Mine Iceland) specialization; both converge at Modernizing the Coast Guard.

| Focus | Prerequisites | Mutually Exclusive | Effects | Notes |
|---|---|---|---|---|
| The Armed Forces of Iceland | >10% world tension (bypasses if not Disarmed Nation conscription) | None | If Disarmed Nation: replace with Volunteer Only (+1.50% recruitable) | Military startup |
| An Airbase in the Sea | The Armed Forces of Iceland | A Naval Hub in the Atlantic | 2× 25% cost reduction for Air Doctrine; 1× 25% research bonus for Naval Bomber; +20 air experience | Air specialization |
| A Naval Hub in the Atlantic | The Armed Forces of Iceland | An Airbase in the Sea | 2× 20% cost reduction for Naval Doctrine; 2× 20% research bonus for Ship Modules; +20 navy experience | Naval specialization |
| Flying Boats | An Airbase in the Sea | None | If By Blood Alone DLC: 2× 25% research bonus for Heavy Aircraft, +25 air experience; else: 2× 25% research bonus for Tactical Bomber, +25 air experience | Air-path focus |
| Modernizing the Coast Guard | An Airbase in the Sea OR A Naval Hub in the Atlantic | None | 2× 20% research bonus for Infantry Weapons; 2× 20% cost reduction for Land Doctrine; +25 army experience, +10 navy experience | Convergence focus |
| Mine Iceland | A Naval Hub in the Atlantic | None | 2× 20% research bonus for Mine Warfare Technologies; +25 navy experience | Naval-path focus |
| Low Cost Aircraft | Flying Boats + Modernizing the Coast Guard | None | +75 air experience; if Aircraft Construction not researched and By Blood Alone enabled: gain Aircraft Construction technology | Air efficiency |
| Emergency Conversions | Mine Iceland + Modernizing the Coast Guard | None | Unlocks decisions to convert convoys into destroyers or cruisers | Naval improvisation |
| Support Equipment | Modernizing the Coast Guard | None | 2× 20% research bonus for Support Technology; random state: +1 building slot, +1 military factory | Support weaponry |
| Professionalize the Army | Support Equipment (mutually exclusive with Herþjónustu) | Herþjónustu | National spirit Víkingasveitin: division attack +10.0%, division defense +15.0%, training time +20.00% | Professional soldiers |
| Herþjónustu | Support Equipment (mutually exclusive with Professionalize) | Professionalize the Army | National spirit Herþjónustu: mobilization +10.00%, recruitable population +2.50%, training time +20.00% | Conscription program |
| Doctrinal Studies | Professionalize the Army | None | +25 army experience; 2× 33% cost reduction for Land Doctrine | Doctrine mastery |
| Civil Defense | Herþjónustu | None | National spirit Civil Defense Organization: air detection +10.0%, recruitable population factor +10%, spotting speed +5%, anti-air bombing damage reduction −2.00%, factory repair speed +15.00%, static anti-air hit chance +20.00% | Civilian readiness |
| Þungur Hnífur | Professionalize the Army OR Herþjónustu | None | 2× 25% cost reduction for Special Forces Doctrine; national spirit Elite Forces: special forces capacity multiplier +25.0% | Elite soldiers |
| Death From Above | Þungur Hnífur (mutually exclusive with We Shall Defend / Taking the Fight) | We Shall Defend Our Island, Taking the Fight to Our Enemies | Modifies national spirit Elite Forces: paratroopers attack +5.00%, paratroopers organization +5.00%; +15 air experience | Airborne specialization |
| We Shall Defend Our Island | Þungur Hnífur (mutually exclusive with Death From Above / Taking the Fight) | Death From Above, Taking the Fight to Our Enemies | Modifies national spirit Elite Forces: mountaineers defense +5.00%, mountaineers speed +5.00%; +15 army experience | Defensive specialization |
| Taking the Fight to Our Enemies | Þungur Hnífur (mutually exclusive with Death From Above / We Shall Defend) | Death From Above, We Shall Defend Our Island | Modifies national spirit Elite Forces: marines attack +5.00%, marines defense +5.00%; +15 navy experience | Amphibious specialization |

## Form the Nordic Council Branch

Joint focus branch shared by Denmark, Finland, Iceland, Norway, and Sweden. When any two Nordic nations are in a faction together, faction members can complete any focus from this joint branch.

See the [Form the Nordic Council](shared-and-joint-branches.md) entry for the shared Nordic focus tree details.

## Generic focuses

See [National Focus and Continuous Focus](../01-mechanics/national-focus.md) for the generic focus tree (used if Arms Against Tyranny DLC is disabled) and continuous focus mechanics.
