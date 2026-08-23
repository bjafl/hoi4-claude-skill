---
title: Uruguayan national focus tree
category: focus-trees
tags: [uruguay, focus tree, trial of allegiance, democratic, fascist, industrial]
game_version: "1.19"
dlc: [Trial of Allegiance]
sources:
  - https://hoi4.paradoxwikis.com/Uruguayan_national_focus_tree
---

## Summary

Uruguay gets a unique national focus tree with the Trial of Allegiance expansion. Without it, Uruguay uses the generic tree. The tree offers three main political paths: continuing Gabriel Terra's industrial dictatorship (pivoting toward fascism or maintaining authoritarian rule), or choosing between the rural-focused Blancos or export-oriented Colorados (both democratic). A factory-building economy and alliance choices define the early-to-mid game.

See [Uruguay](../05-countries/uruguay.md) for the country's 1936 starting profile.

See [National Focus and Continuous Focus](../01-mechanics/national-focus.md) for generic/continuous focuses.

## Terra's Dictatorship Branch

The foundation of the tree: industrial buildup and institutional control under Gabriel Terra (seized power via self-coup 1933). Branches into either the fascist path (Break Relations with the Soviet Union sub-branch) or authoritarian-neutral rule (Women's Vote, Statism).

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Terra's Dictatorship** | — | — | National spirit: **The Terra Dictatorship** (+20% PP gain, +15% stability, −10% war support, +10% ideology drift defense, −60 acceptance of democratic diplomacy). Represents Gabriel Terra's consolidation after the March 31, 1933 revolution. |
| **Prohibition of Usury** | Terra's Dictatorship | — | National spirit: **Prohibition of Usury** (+15% infrastructure construction speed, +8% civilian factory construction speed). Anti-lending regulation. |
| **Revaluation Law** | Prohibition of Usury | — | National spirit for 620 days: **Revaluation Law** (−15% consumer goods factory factor, +0.20% weekly stability). Central bank monopolizes banking. |
| **BROU** | Revaluation Law | — | Available as Design Company: BROU (Central Bank) (+20% industrial research speed, −5% consumer goods factory factor). Bank of the Eastern Republic of Uruguay. |
| **Pay Off All External Debts** | BROU | — | Removes national spirits "Low Amounts of External Debts" and "Expired Debts". Settles all foreign debts. |
| **Ministry of Public Works Assistance** | Prohibition of Usury | — | National spirit for 480 days: **Ministry of Public Works Assistance** (+40% industrial research speed, +5% construction speed). Road and housing program. |
| **Rapid Industrialization** | Ministry of Public Works Assistance | — | National spirit for 720 days: **Rapid Industrialization** (−25% consumer goods factory factor, +20% construction speed). Major industrial acceleration. |
| **La Teja Refinery** | Rapid Industrialization | — | Random controlled cored state (prioritize Paysandú 946, Cerro Largo 945): add 8 oil production, 2 building slots, 2 synthetic refineries. Modern oil refinery. |
| **Pluna** | Rapid Industrialization | — | Air experience +25, aerodynamics and avionics breakthrough +25%, 40 transport plane I added to stockpile; random cored state adds 2 building slots, 1 civilian factory. Flag carrier airline. |
| **Conaprole** | Rapid Industrialization | — | 2× 20% research bonus for construction technology; random cored state (prioritize Paysandú, Cerro Largo) adds 1 building slot, 1 civilian factory. Dairy monopoly. |
| **Mercado Modelo** | Rapid Industrialization; controls Montevideo (300) | — | Montevideo (300): add 1 building slot, 1 civilian factory. Random other cored state: add 2 building slots. Largest agricultural market. |
| **Import Substitution** | Ministry of Public Works Assistance | — | National spirit: **Import Substitution** (+35% trade deal opinion factor, −25% trade law cost, +20% excavation tech research, +20% synthetic resources research). Belgian-model economic autarky. |
| **Women's Vote** | Terra's Dictatorship | — | Gain base +8% stability, +10% democracy support. Women's suffrage. |
| **Statism** | Terra's Dictatorship | — | National spirit: **Statism** (−8% consumer goods factory factor, −8% stability, +5% military factory construction speed). Centralized state control. |
| **Right to Food, Housing and Health** | Statism | — | Gain base +5% stability; random cored state adds 1 building slot; state category upgraded (cascade: Tiny Island → Small Island → ... → Megalopolis, each tier adds 1–2 building slots). Constitutional social rights. |

> ⚠️ Broken wiki template reconstructed: Several focuses reference `[{{{1}}}]` ideology tags in original source; these are reconstructed as ideology references (fascism, democracy, etc.) based on branch context.

## Break Relations With the Soviet Union Sub-branch

Fascist path: building fascism and Axis alignment. Unlocks after Statism. Multiple focuses converge toward **Acción Revisionista del Uruguay** (mutual exclusion with democratic paths), then toward either **The Fuhrmann Plan** (German-allied) or other fascist institutional focuses.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Break Relations With the Soviet Union** | Statism | — | National spirit for 45 days: **Fascist Influence** (−25% ideology drift defense, +0.25 daily fascism support, +150 fascist diplomacy acceptance). Embargoes Soviet Union, Mongolia, Tannu Tuva if By Blood Alone enabled. Anti-Soviet posturing. |
| **Tour to Italy** | Break Relations with the Soviet Union | — | If Arms Against Tyranny: add 500 construction cost equipment subsidy for light tanks to Germany, Italy, Hungary, Romania. Otherwise grants 100 Italian great-war or inter-war tank chassis units. National spirit for 45 days: **Fascist Influence**. Diplomatic ties to Italy. |
| **Recognize Francoist Spain** | Break Relations with the Soviet Union | Bypassed if Spain is communist, democratic, or Franco not leader, or Civil War over | National spirit: **Volunteer Force** (−100% send volunteers tension limit, +2 max volunteer divisions, −100% divisions required, +2 air volunteer cap, +0.01 daily fascism support). Every other country with Spain flags gains 70 PP and "Deepening Partnership" (Uruguay opinion +5). Gains "Can send volunteer forces" rule. Fascist Spain alignment. |
| **Merge Falangist Movements** | Recognize Francoist Spain | — | +2.5% fascism popularity; national spirit: **Mandatory Pre-Military Training** (+2% recruitable population, −10% training time, −10% minimum training level, +0.01 daily fascism support). Consolidates Uruguayan fascist factions. |
| **Rincón del Bonete Power Station** | Break Relations with the Soviet Union; Paysandú (946) fully controlled | — | +5% fascism popularity; national spirit: **Electrification of the Country** (−10% consumer goods factory factor, +6% research speed). Paysandú (946) adds 1 dam with state modifiers: +15% max factories, −65% energy consumption, +10% resources, +15% construction speed. German-funded power project. |
| **German-Uruguayan Nazi Movements** | Rincón del Bonete Power Station | — | +5% fascism popularity; random cored state (prioritize Paysandú, Cerro Largo) adds 2 building slots, 2 military factories. Harnesses German-Uruguayan Nazi minority. |
| **Acción Revisionista del Uruguay** | Requires one of: Merge Falangist Movements, German-Uruguayan Nazi Movements | Mutually exclusive with: Blanco's Election Victory, Colorado Election Victory | Available as Political Advisor: Adolfo Agorio (+75 weekly manpower, −35% justify war goal time, +0.10 daily fascism support). Available as Political Advisor: Teodomiro Varela de Andrade (+5% PP gain, +5% factory output, +0.05 daily fascism support). |
| **Force Through Corporatism** | Acción Revisionista del Uruguay | — | Gain base −8% stability; national spirit: **Corporatism** (−15% PP gain, −3.5% research speed, +15% factory output, +15% dockyard output, +30% ideology drift defense, −20% resistance growth, +0.02 daily fascism support). Authoritarian economic restructuring. |
| **Empower Fuhrmann's Cultural Center** | Acción Revisionista del Uruguay | — | +15% fascism popularity, gain base +10% war support, +14,000 manpower. German-Uruguayan cultural propaganda. |
| **The Fuhrmann Plan** | Empower Fuhrmann's Cultural Center; Uruguay fully independent, >40% fascism support | — | **Uruguay**: Ideology becomes fascist, elections cancelled. Gains inter-war or great-war tank technology if not researched; creates 1 German Militia Machine-Gunner unit in random state (prioritize Montevideo 300); creates 4 Tractor Tank units; 700 units German Tractor Tank (inter-war chassis) added to stockpile. National spirit for 365 days: **Political Turmoil** (−10% stability, −10% war support). **Germany** (if fascist, independent, not in faction with Uruguay, hasn't capitulated) receives event "Uruguay seeks to join the Axis". German-Uruguayan union. |
| **Food for the War-machine** | The Fuhrmann Plan | — | Every faction member: gains national spirit **Uruguayan food for the war-machine** (−10% supply consumption, +48 hour supply grace). Uruguay gains same spirit. Agricultural support to Axis. |

## Blanco's Election Victory / Colorado Election Victory Branch

Democratic paths chosen after the 1938 election, mutually exclusive with each other and with fascism (Acción Revisionista del Uruguay). Blancos pursue rural development and ideological flexibility; Colorados pursue neutrality, constitutional reform, and foreign investment.

### Blanco's Path

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Blanco's Election Victory** | Election of 1938 happened; has not completed Acción Revisionista del Uruguay | Mutually exclusive with: Colorado Election Victory, Acción Revisionista del Uruguay | +15% non-aligned popularity, +5% democracy popularity. Blancos win 1938 election. |
| **Herrerismo** | Blanco's Election Victory | — | National spirit: **Herrerismo** (+15% resource gain efficiency, +25% ideology drift defense, +10% infrastructure construction speed). Mix of nationalism, conservatism, populism under Luis Alberto de Herrera. |
| **Traditionalism** | Blanco's Election Victory | — | National spirit: **Traditionalism** (−10% PP gain, −8% consumer goods factory factor, +5% stability, −10% armor research, −10% air research, +15% artillery research, +15% weapons & equipment research, +15% motorization research). Traditionalist conservatism. |
| **Ruralism** | Requires one of: Herrerismo, Traditionalism | — | Cerro Largo (945): add Ruralism (+50% resource gain efficiency, +200% local manpower, +50% max factories, +25% construction speed). Paysandú (946): same Ruralism modifiers. Montevideo (300): −10% local construction speed. Rural development focus. |
| **Americanism** | Traditionalism | — | National spirit: **Americanism** (+5% PP gain, +30% trade deal opinion factor, +15% ideology drift defense, −25% trade law cost, +0.05 daily democracy support). If at peace with USA and no NAP: USA (if AI, independent) enacts guarantee independence, grants mutual military access. If Arms Against Tyranny enabled: +300 economic capacity. South American solidarity. |
| **Anti-Centralism** | Ruralism | — | Cerro Largo (945): Ruralism upgraded to +100% resource gain efficiency, +300% local manpower, +75% max factories, +35% construction speed. Paysandú (946): same upgrades. Montevideo (300): −18% local construction speed. Decentralization against Montevideo dominance. |
| **Anti-Imperialism** | Americanism | — | National spirit: **Anti-Imperialism** (−80% generate war goal tension limit, −30% justify war goal time, +10% attack vs major countries, +10% defense vs major countries). Unlocks rules: can declare war on same ideology without war goal, justify on non-world-tension countries, join factions led by other ideologies. Anti-colonial stance. |
| **Join the Allies** | Requires one of: Anti-Centralism, Break Diplomatic Relations with Axis | Must be fully independent | +15% democracy popularity. If UK is faction leader, democratic, at peace: UK receives event "Uruguay seeks to join Allies". Otherwise if USA is faction leader, democratic, at peace: USA receives same event. Otherwise any major democratic faction leader receives event. Allied integration. |

### Colorado's Path

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **Colorado Election Victory** | Election of 1938 happened; has not completed Acción Revisionista del Uruguay | Mutually exclusive with: Blanco's Election Victory, Acción Revisionista del Uruguay | +15% democracy popularity. Colorados continue ruling. |
| **A New Constitution** | Colorado Election Victory | — | +10% democracy popularity; national spirit: **Constitutional Guarantees** (+5% factory output, +5% dockyard output). Constitutional renewal. |
| **The "Good" Coup** | A New Constitution | — | Leader gains trait "Wielder of Emergency Powers" (−10% consumer goods factory factor, +5% military factory construction, +5% naval dockyard construction). +15% democracy popularity. National spirit for 240 days: **Political Turmoil** (−10% stability, −10% war support). Bloodless self-coup. |
| **Legalize the Pool** | Colorado Election Victory | — | Gain base +5% stability; random fully controlled cored state (prioritize Paysandú, Cerro Largo): add 1 building slot, 1 civilian factory. Legalized gambling. |
| **Declare Neutrality** | Colorado Election Victory | — | +150 PP; national spirit: **Neutral Foreign Policy** (+100% join faction tension, +20% send volunteers tension, +100% guarantee tension, +250% embargo tension, −100 AI desire for faction, +1% AI threat receptivity). Strict non-involvement. |
| **Legacy of Batlle** | Colorado Election Victory | — | National spirit: **Legacy of Batlle** (+5% PP gain, +10% party popularity stability modifier, +8% research speed, +0.10 daily democracy support). Honors José Batlle y Ordóñez's social-justice legacy. |
| **Law No. 9914** | Declare Neutrality; Finland at war with major country | — | +120 PP; Finland gains national spirit for 365 days: **Uruguayan food for the war-machine** (−10% supply consumption, +48 hour supply grace). Winter War aid (historical 1939). |
| **Investigate German and Italian Organizations** | Declare Neutrality | — | −30% fascism popularity, −30% non-aligned popularity. Surveillance of axis cultural groups. |
| **Law No. 9943** | Declare Neutrality | — | National spirit: **Law No. 9943** (+5% recruitable population, +10% training time). Conscription preparation. |
| **American Air Bases** | Requires one of: Investigate German and Italian Organizations, Law No. 9943; has full control Montevideo (300); at peace with USA | — | Montevideo (300): add 3 air bases. If By Blood Alone: add P-36A and B-10 fighter/bomber variants, 110 P-36A + 60 B-10 to stockpile. Otherwise: 130 fighter I + 100 tactical bomber I to stockpile. If Arms Against Tyranny: add equipment subsidies (1000 construction cost each) for fighter, strategic bomber, tactical bomber from USA/UK/France/Canada. US military cooperation. |
| **Break Diplomatic Relations With the Axis** | Requires one of: Investigate German and Italian Organizations, Law No. 9943 | — | Removes national spirit **Neutral Foreign Policy** if held. If By Blood Alone and Germany fascist: embargo Germany, embargo all Axis faction members, gain base +12% war support. Anti-Axis pivot. |
| **Join the Allies** | Requires one of: Anti-Centralism (Blanco path), Break Diplomatic Relations with Axis; fully independent | — | +15% democracy popularity. Triggers event to UK or USA faction leader (if democratic): "Uruguay seeks to join the [faction]". Allied integration. |

## Paraguay/Uruguay Shared Branches

See [Paraguay national focus tree](../06-focus-trees/paraguay.md) for the shared branches: expansion opportunities, industrial buildings, and research bonuses applicable to both nations.

## Trial of Allegiance Shared Military Branches

See [Trial of Allegiance shared military national focus tree branches](shared-and-joint-branches.md) for shared military focuses and nation-specific variants based on alliance choice.

---

**Notes:**

- The fascist path (**Acción Revisionista del Uruguay** and beyond) is mutually exclusive with both democratic paths.
- All democratic focuses converge toward **Join the Allies** (from either Blanco's Anti-Imperialism or Colorado's Break Diplomatic Relations), ending in Allied faction membership.
- Without Trial of Allegiance DLC, Uruguay defaults to the generic focus tree.
- Several focuses reference conditional DLC (By Blood Alone, Arms Against Tyranny, No Step Back) for equipment subsidies and unit variants; effects listed reflect the DLC-conditional branches.
