---
title: Chilean National Focus Tree
category: focus-trees
tags: [chile, focus tree, non-aligned, democratic, fascist, monarchist, mapuche, civil war]
game_version: "1.19"
dlc: [Trial of Allegiance]
sources:
  - https://hoi4.paradoxwikis.com/Chilean_national_focus_tree
---

## Summary

Chile has a unique national focus tree with the Trial of Allegiance DLC. Without it, Chile uses the generic focus tree. The Chilean tree spans four main ideological branches (Non-Aligned via Ibáñez's dictatorship, Democratic under Alessandri, Fascist coup, and a shared industrial branch) plus military-focused shared focuses. Notable features include the Mapuche civil war, installing a European monarchy, regional conquest, and communist unification of the Americas.

See [Chile](../05-countries/chile.md) for the country's 1936 starting profile. For the generic tree and continuous focuses available to all nations, see [National Focus and Continuous Focus](../01-mechanics/national-focus.md).

## Overview

The Chilean focus tree divides into five major segments:

1. **Look to Tradition** — Non-Aligned branch: Ibáñez's dictatorship (1927-1931), Monarchist path installing King Antoine III of Araucanía and Patagonia, or Mapuche civil war path
2. **Endorse the Constitution of 1925** — Democratic branch: Arturo Alessandri's policies, 1938 election, presidential reforms, or communist unification path
3. **Denounce the State of Near Anarchy** — Fascist coup path: counter-revolution, Axis alignment or Pan-Hispanic model, regional conquest
4. **Dissolve COVENSA / Public Works Projects** — Industrial/economic branch: resource extraction, trade, currency devaluation, factory construction
5. **Trial of Allegiance Shared Military** — Special military national spirits and country-specific bonuses (choice-gated)

The tree begins with Ibáñez's Coup as a shared root focus that opens all ideological paths.

## Look to Tradition Branch (Non-Aligned)

Starts the Non-Aligned path by installing Carlos Ibáñez del Campo as President. Opens into Monarchist (Antoine III) and Mapuche civil war variants, with various shared economic/military focuses.

| Focus | Prereq | Exclusive | Effects |
|---|---|---|---|
| **Look to Tradition** | None | Endorse the Constitution of 1925, Denounce the State of Near Anarchy | Non-Aligned popularity +5.00%; Political power +35 |
| **Ibáñez's Coup** | Look to Tradition | — | Stability -10.00%; Event: General Carlos Ibáñez del Campo's Coup d'etat (Partido Ibáñista ruling); Gain trait The General President; Division attack core +10.0%, defense core +10.0%; Daily command power +15%; Resistance growth -5%. Party popularity: Non-Aligned +60.00%, Fascism +15.00%. Carlos Ibáñez del Campo leads Democratic party. |

### Rule by Decree Sub-branch (Monarchist path)

Installs Antoine III as King of Araucanía and Patagonia with French nobility advisors; either keeps Ibáñez as PM (constitutional) or makes it an absolute monarchy.

| Focus | Prereq | Exclusive | Effects |
|---|---|---|---|
| **Rule by Decree** | Ibáñez's Coup | Address the Mapuche Conflict | Dictator trait; Political power gain +25%; AI desired divisions +20.0%; War support (combat casualties) +0.10%; Stability -15.00%; Remove Near Anarchic Society spirit. Set flag CHL_no_more_anarchy_flag. |
| **Alianza Popular Libertadora** | Rule by Decree (ruling party must be Non-Aligned) | — | Gain Alianza Popular Libertadora spirit: War support +10.00%, Democratic diplomacy acceptance +30, Fascist diplomacy acceptance +30, daily unaligned support +0.04, unaligned diplomacy acceptance +60 |
| **Increase Spending on Public Works** | Rule by Decree (non-aligned) | — | Modify The Chilean Economy dynamic: construction speed +5.00%, factory output +5.0%. Random state: add 1 infrastructure. War support -5.00%. |
| **Utilize National-Populism** | Increase Spending on Public Works | — | War support +5.00%; Non-Aligned popularity +10.00%, Fascism +5.00%. Available advisors: Francisco Antonio Encina (Agr. Nat. Socialist, consumer goods -10%, trade laws -50%, economy laws -50%, daily Fascism +0.05, daily unaligned +0.02); Tancredo Pinochet (University Fascist, research speed +10%, daily Fascism +0.06); Guillermo Paulino Izquierdo Araya (Agrarian Nationalist, PP gain +5%, consumer goods -10%, max factories +10%). ⚠️ Triggers civil war if combined with Sell Arica to Peru. |
| **Sell Arica to Peru** | Rule by Decree (Arica y Tarapacá owned/controlled) | — | Event: Chile wishes to sell Arica (Peru accepts/rejects). If accept: Peru gets +75 PP; Chile gains Payments from Peru spirit (720 days): consumer goods -15.0%, construction speed +5.00%. Arica y Tarapacá becomes Peruvian core. ⚠️ Triggers civil war if combined with Outlaw Socialism or Utilize National-Populism. |
| **Seek Foreign Investments** | Rule by Decree | — | Random cored state: add 1 building slot and 1 civilian factory. Gain Foreign Economic Investments spirit (365 days): Political power gain -20%, consumer goods -20%. |
| **Outlaw Socialism** | Seek Foreign Investments | — | Political power +50. Ban communism (variable-based removal from popularity). Set flag banned_communism_flag. ⚠️ Triggers civil war if combined with Sell Arica to Peru. |
| **Strengthen the Carabineros de Chile** | Rule by Decree | — | Gain Carabineros de Chile spirit: Recruitable population +5%, division attack core +5.0%, division defense core +7.0%, ideology drift defense +20.0%. |
| **Crown Antoine as Sovereign King** | Requires one of: Utilize National-Populism, Outlaw Socialism, Sell Arica to Peru; non-aligned; approached by Antoine during civil war | — | War support +5.00%. Event: The Crowning of Antoine III. Antoine III becomes Non-Aligned leader: -10.00% stability, -10.00% war support, +5.0% division defense core. Gain French Investments spirit (360 days): consumer goods -15.0%, production efficiency growth +10.00%. Claims gained on Río Negro, Chubut, Santa Cruz. Remove The Republican Guard spirit. Events: Popular Resistance Forms, Veteran Legionaries Arrives, The New Kingdom of Araucanía and Patagonia. |
| **Mobilize the Veteran Legionaries** | Crown Antoine | At war | Delete Légion Étrangère template (disband units). Create new template. Random controlled cored states: create 2 Légion Étrangère divisions. |
| **Request Assistance in the War** | Crown Antoine | Civil war | Events sent to eligible nations; if accepted, they send volunteers. Targets: Communist/Democratic nations (except Chile), at peace with Chile, not subjects/in faction, or Spain. |
| **Strike a Deal with the Mapuche** | Crown Antoine | — | Remove The Mapuche Conflict spirit. Flag: CHL_no_more_mapuche_conflict. Delete Guerreros Mapuche and Guerreros Abajinos templates. Create new Guerreros templates. Random controlled states: create Mapuche units in Santiago/Araucanía. Available advisors: Rayén Quitral (Famous Soprano, stability +20%); Manuel Manquilef (Defender, defense core +5.0%, factory output +8%, ideology drift +30%); Venancio Coñuepán Huenchual (Army Offense, experience gain +0.30, attack +100%); Esteban Romero Sandoval (Economist, consumer goods -20%, daily unaligned +0.05); Manuel Antonio Neculmán (Educational Reformer, research speed +15%, daily unaligned +0.05); Carlos Huayquiñir (Journalist, PP gain +10%, stability +5%, resistance -10%); Manuel Aburto Panguilef (Traditionalist, stability +10%, war support +10%, research speed -2%, daily unaligned +0.08). |
| **Ibáñez as Prime Minister** | Strike a Deal with the Mapuche | An Absolute Monarchy | Ibáñez loses Ibañismo trait, gains The Father of Ibañismo. Political power gain -20%, division attack +10.0%, defense +10.0%, daily command power +15%, daily unaligned +0.06. Hire Ibáñez as advisor if <3 advisors. Blocks Je Suis Le Deluge. |
| **An Absolute Monarchy** | Strike a Deal with the Mapuche | Ibáñez as Prime Minister | Political power +50. If leader Antoine III: modify trait adding stability -5.00%, war support -5.00%, division defense core +5.0%, daily unaligned +0.06. Blocks Treading the Straight Line. |
| **Approach the Moderates** | Ibáñez as Prime Minister | — | Political power +50. Available advisors: Juan Bautista Rossetti (Socialist Economist, consumer goods -7%, factory output +5%, daily Communism +0.05); Emilio Bello Codesido (Minister of Defense, defense core +6%, military factory speed +10%); Radomiro Tomic Romero (Influential Christian Democrat, PP gain +10%, stability +5%, daily Democracy +0.06); Bernardo Leighton (The National Falange, recruitable population +10%, research speed +3%, daily Democracy +0%); [table data truncated for length] |

### Address the Mapuche Conflict Sub-branch

Allows Mapuche to overthrow Chile in civil war, then reconquer the Americas and create native-ruled states or keep as puppets.

| Focus | Prereq | Exclusive | Effects |
|---|---|---|---|
| **Address the Mapuche Conflict** | Ibáñez's Coup | Rule by Decree | Stability -10.00%; Event: The Mapuche Conflict Begins (civil war). Gain The Mapuche Conflict spirit: War support -15%, recruitable population -15%, consumer goods factories +15%. |
| **Support the Guerreros Mapuche** | Address the Mapuche Conflict; civil war ongoing | — | Event sent to allies; if accepted, they send volunteers. Creates Guerreros Mapuche and Guerreros Abajinos division templates. Random controlled states (Santiago/Araucanía): create Mapuche units. |
| **The Indigenous Republic** | Address the Mapuche Conflict (civil war) | — | Event: The Indigenous Republic (Mapuche win/peace). Flag: CHL_mapuche_republic. Changes country color and mechanics toward indigenous themes. Gain advisors and national spirits tied to indigenous leadership. |
| **Reconquer the Americas** | The Indigenous Republic | — | Event: Reconquer the Western Hemisphere. Casus belli vs. non-core American nations. Gain various country-specific events and spirits for territories conquered. |
| **Keep them as Puppets** | Reconquer the Americas | Create the Mapuche Empire | Create puppet Mapuche states in conquered Americas. Mapuche Unity spirit: daily unaligned +0.05%, puppet autonomy -0.05%. |
| **Create the Mapuche Empire** | Reconquer the Americas | Keep them as Puppets | Annex all Mapuche states; core them all. Gain Mapuche Empire spirit: war support +5%, recruitable population +5%, daily unaligned +0.10. |

### Shared Sub-branches (Monarchist/Mapuche convergence)

Focuses available to both Monarchist and Mapuche paths after their initial civil-war choice.

| Focus | Prereq | Effect |
|---|---|---|
| **Enlarge the Textile Industries** | Rule by Decree or Address the Mapuche (shared) | Random cored state: add 1 civilian factory. Gain The Textile Industry spirit: factory output +5%, production efficiency growth +3%. |
| **The Patagonian Giants** | Enlarge the Textile Industries (shared) | War support +5%; Manpower +10%; Declare war on Argentina for claimed Patagonian territory. |
| **An Imperial Capital** | The Patagonian Giants (shared) | Opportunity to move capital. Create puppet Inca Empire, Suriname, Haiti; declare war on neighboring nations. Option to ally France or conquer it. Invade Mexico. Keep Antoine III as king and conquer Quebec, or overthrow him to make Ibáñez "King" and form El Reino de la Patria Nueva. |
| **A New South American Order** | An Imperial Capital | Form hegemony over South American states; gain regional bonuses and claims. |

## Endorse the Constitution of 1925 Branch (Democratic)

Begins the Democratic branch via Arturo Alessandri's policies. Contains the 1938 election sub-branch, presidential reform path, and communist unification sub-branch.

| Focus | Prereq | Exclusive | Effects |
|---|---|---|---|
| **Endorse the Constitution of 1925** | None | Look to Tradition, Denounce the State of Near Anarchy | Democratic popularity +5%; Political power +35. |
| **Enact Alessandri's Policies** | Endorse Constitution | — | Democracy popularity +10%; Stability +5%; Political power gain +10%. Gain Alessandri's Policies spirit: democratic diplomacy acceptance +50, factory output +5%. |
| **Elección Presidencial de Chile de 1938** | Enact Alessandri | — | Event: Chilean Presidential Election of 1938. Branches into three leadership choices: Arturo Alessandri (Democratic), Gustavo Ross (Conservative/Democratic), Radical Alliance (varies). |
| **Increase Presidential Powers** | Elección Presidencial (various paths) | Reapproach America, Return to Parliamentary Era | Stability -5%; War support +10%; Political power gain +15%. Executive authority increased. |
| **Reapproach America** | Elección Presidencial | Increase Presidential Powers, Return to Parliamentary Era | Join the Allies (faction). Diplomatic cooperation +25%; Allied trade agreement bonus +10%. Can request Pacific islands for protection. |
| **Return to the Parliamentary Era** | Elección Presidencial | Increase Presidential Powers, Reapproach America | Return to parliamentary system. Stability +10%; War support -5%. Democratic institutions strengthened. |
| **Bring Communist Advisors** | Any presidential path | — | Communist popularity +15%; Political power gain -10%; daily Communism support +0.08. Advisors become available from communist parties. |
| **Alliance with Argentina** | Reapproach America or Return to Parliamentary Era (optional) | War on Argentina | Join Argentina to Allies. Combined diplomatic weight. Option to form South American Democratic bloc. |
| **War on Argentina** | Reapproach America or Return to Parliamentary Era (optional) | Alliance with Argentina | Declare war on Argentina for Tierra del Fuego. Casus belli and war goals. Rivalry with regional powers. |
| **The Future of Chile** | Bring Communist Advisors | — | Convert Chile to Communist ideology. Event: The Future of Chile (Communist revolution). Communist popularity +30%; stability -10%; war support +15%. |
| **The Federation of Hispanic Republics** | The Future of Chile | — | Event: Unify Latin American Communist nations. Form faction with regional communist states. Gain regional bonuses and unit experience. |

## Denounce the State of Near Anarchy Branch (Fascist)

The Fascist coup path. Begins with choosing focuses to mitigate stability/war support debuffs before the coup, then builds the nation for warfare. Two sub-paths: Axis alignment (Operation Bolívar) or Pan-Hispanic model.

| Focus | Prereq | Exclusive | Effects |
|---|---|---|---|
| **Denounce the State of Near Anarchy** | None | Look to Tradition, Endorse Constitution | Fascist popularity +5%; Political power +35. |
| **The Reactionary Movement** | Denounce State | — | Fascist popularity +10%; Stability -5%; War support +5%. Available fascist advisors. |
| **Land Reform** | Denounce State | — | Stability +5%; Recruitable population +5%. Random state: add 1 military factory. Gain Land Reform spirit. |
| **Nationalize Key Industries** | Denounce State | — | Political power +75; War support +5%; Factory output +10%. Consumer goods -10%. |
| **Commence the Counter-Revolution** | Requires one of: Land Reform, Nationalize Key Industries, The Reactionary Movement; fascist ruling party | — | Event: The Fascist Coup. Stability -20%; War support -15%. Remove The Mapuche Conflict spirit (temporarily removes Araucanía 950). Gain Fascist Regime spirit: war support +20%, recruitable population +5%, ideology drift +30%. |
| **Cooperate with Operation Bolívar** | Commence Counter-Revolution | — | Event: Operation Bolívar (align with Germany). Germany joins Axis if not already. Bring regional Fascist nations (Argentina, Brazil) to Axis. Gain Germany's tech sharing and alliance. War support +10%. |
| **Abide by the Francoist Model** | Commence Counter-Revolution | Cooperate with Operation Bolívar (partial) | Create Pan-Hispanic faction instead of pure Axis. Ally with Hispanic/Latin nations. Portugal and Spain join faction. Fascist popularity +15%; War support +5%. Regional cultural bonuses. |
| **Revoke the Treaty of Lima** | Commence Counter-Revolution | — | War on Argentina (shared with others if chosen). Form Kingdom of Chile. Casus belli on regional states. Create Pacific empire (territorial claims on western Americas). |
| **Form the Kingdom of Chile** | Revoke Treaty of Lima | — | Become Kingdom of Chile (government type shifts). Stability -10%; War support +10%; Political power +50. Claims on Argentina, Bolivia, Peru. |

## Dissolve COVENSA / Public Works Projects Branch (Industrial/Economic)

Industrial branch split into three sections: left (resource extraction, trade), right (construction, infrastructure), bottom (currency devaluation for industrial buildup).

| Focus | Prereq | Effect |
|---|---|---|
| **Dissolve COVENSA** | None | Can take independently; leads into left/right industrial paths. Event: Dissolve COVENSA (mining consortium). Gain mining/resource bonuses. |
| **Prioritize Copper Production** | Dissolve COVENSA (left path) | Copper production +20%; Export value +15%. Gain Copper Industry spirit: civilian factory output +5%, trade deal bonus +10%. |
| **Strengthen Trade Agreements** | Dissolve COVENSA (left path) | Trade efficiency +10%; Trade deals cost -25%; Gain allies' trade resources +10%. |
| **Infrastructure Expansion** | Dissolve COVENSA (right path) | Random state: add 2 infrastructure. Construction speed +10%. Gain Infrastructure Expansion spirit: air base/naval base/railway/fort construction speed +15%. |
| **Factory Construction Program** | Dissolve COVENSA (right path) | Random state: add 1 military factory and 1 civilian factory. Factory output +5%. Can use building slots in states at reduced cost. |
| **Devalue Currency** | Dissolve COVENSA (bottom path) | Stability -10%; Inflation penalty; Export price -15% (incoming trade cheaper, outgoing more expensive). Consumer goods -5%; Industrial capacity +10%. Gain Devaluation Period spirit: factory output +10%, construction speed +5%. |

## Trial of Allegiance Shared Military Branches

Special military-focused national spirits and unit bonuses. Choice-gated depending on diplomatic alignment or ideological path taken.

| Focus | Prereq | Requirements | Effect |
|---|---|---|---|
| **Strengthen the Army** | One of: Look to Tradition, Endorse Constitution, Denounce State (start of any path) | — | Army experience +25; 1× 100% research bonus for Land Doctrine. Division attack +5%, defense +5%. |
| **Expand Naval Forces** | Strengthen Army (or independent start) | — | Navy experience +25; 1× 100% research bonus for Naval Doctrine. Dockyard output +10%; Naval factory construction speed +10%. |
| **Air Superiority Program** | Strengthen Army | — | Air experience +25; 1× 100% research bonus for Air Doctrine. Fighter production +15%; Fighter speed +5%; Air base construction speed +10%. |
| **Conscription Push** | Strengthen Army | Stability >20% | Recruitable population +10%; Mobilization speed +5%. Gain National Service spirit: manpower +15%, recruitable +10%, war support +10% when at war. |
| **Professional Officer Corps** | Strengthen Army | — | Army experience +40; Division training time -15%; Officer recruitment speed +20%. Available military advisors (Chief of Staff, Army/Navy/Air commanders). |
| **Purchase Foreign Equipment** | Expand Naval Forces or Air Superiority | — | Available equipment trade deals +50%; Import price -10%. Can purchase foreign-designed divisions/aircraft. PP cost -20% for import agreements. |

### Country-Specific Military Focuses (Choice-Gated)

These focuses appear or become available only if specific earlier ideological focuses were taken.

| Focus | Unlock Condition | Effect |
|---|---|---|
| **Monarchist Military Training** | Crown Antoine as Sovereign King | Division training time -15%; Monarchist ideology bonus: morale +10%, organization +10%. Gain Légion Étrangère veteran units (French Foreign Legion). |
| **Mapuche Guerrilla Tactics** | Strike a Deal with the Mapuche | Guerrilla warfare bonuses (enemy attack -15% in mountainous/forested terrain). Mapuche unit templates gain +20% defense in rough terrain. Daily resistance suppression -10% in Mapuche territories. |
| **Democratic Alliance Training** | Reapproach America focus | Alliance bonus: division attack +8%, organization recovery +10% when fighting same enemy as ally. Shared tank/air research with Allies +5%. |
| **Fascist Militarism** | Commence Counter-Revolution | Army experience gain +1.0 daily; War support gain +5% per division attacking enemy; Consumer goods factories -15% (converted to military). Parade videos available for morale. |

## Key National Spirits Acquired Through Tree

| Spirit | Source Focus(es) | Effects | Duration |
|---|---|---|---|
| Alianza Popular Libertadora | Alianza Popular Libertadora | War support +10%, democratic diplomacy +30, fascist diplomacy +30, daily unaligned +0.04, unaligned diplomacy +60 | Permanent |
| Carabineros de Chile | Strengthen Carabineros | Recruitable population +5%, division attack core +5%, defense core +7%, ideology drift defense +20% | Permanent |
| Payments from Peru | Sell Arica to Peru (if accepted) | Consumer goods -15%, construction speed +5% | 720 days |
| Foreign Economic Investments | Seek Foreign Investments | Political power gain -20%, consumer goods -20% | 365 days |
| French Investments | Crown Antoine | Consumer goods -15%, production efficiency growth +10% | 360 days |
| The Mapuche Conflict | Address the Mapuche Conflict | War support -15%, recruitable population -15%, consumer goods +15% | Until peace/resolution |
| The Textile Industry | Enlarge Textile Industries | Factory output +5%, production efficiency growth +3% | Permanent |
| Fascist Regime | Commence Counter-Revolution | War support +20%, recruitable population +5%, ideology drift +30% | Permanent (while Fascist) |
| Copper Industry | Prioritize Copper Production | Civilian factory output +5%, trade deal bonus +10% | Permanent |
| Infrastructure Expansion | Infrastructure Expansion | Air base/naval base/railway/fort construction +15% | Permanent |
| Devaluation Period | Devalue Currency | Factory output +10%, construction speed +5% | Until reverted |
| National Service | Conscription Push | Manpower +15%, recruitable +10%, war support +10% (when at war) | Permanent |

## Civil War Mechanics

Several focus chains can trigger a civil war:
- **Ibáñist vs. Anti-Ibáñist**: Triggered if conflicting monarchist/economic focuses (e.g., Crown Antoine + industrial choices)
- **Mapuche Uprising**: Triggered by Address the Mapuche Conflict focus; Chile vs. Mapuche for control
- **Fascist Coup**: Triggered by Commence Counter-Revolution; Chile (Fascist) vs. Chile (Anti-Fascist) forces
- During civil wars, both sides can request foreign volunteers and aid; participation factors in postwar politics and spirit modifiers

## Mutual Exclusions and Blocking Effects

- Look to Tradition ↔ Endorse Constitution ↔ Denounce State (choose one root branch)
- Rule by Decree ↔ Address the Mapuche Conflict (Monarchist vs. Mapuche paths)
- Ibáñez as Prime Minister ↔ An Absolute Monarchy (constitutional vs. absolute after Antoine)
- Increase Presidential Powers ↔ Reapproach America ↔ Return to Parliamentary Era (post-1938 election choices)
- Cooperate with Operation Bolívar (partial overlap) with Abide by Francoist Model (Axis vs. Pan-Hispanic)
- Alliance with Argentina ↔ War on Argentina (Democratic path)
- Keep Mapuche as Puppets ↔ Create Mapuche Empire (integration approach)
- Ibáñez as Prime Minister blocks Je Suis Le Deluge (later focus)
- An Absolute Monarchy blocks Treading the Straight Line (later focus)

## Notes

- The Chilean tree is heavily branching; many paths are mutually exclusive and lead to civil wars if contradictory focuses are attempted.
- All political branches (Non-Aligned, Democratic, Fascist) are viable through their respective root focuses and sub-paths.
- The industrial branch (Dissolve COVENSA) is semi-independent and can run in parallel with ideological paths.
- Regional conflicts (Argentina, Peru, Bolivia) are choice-gated and often come with territorial claims and war goals.
- Foreign support (France, Germany, Allies, communist nations) varies by path chosen; some focuses trigger events requesting aid.
- The Mapuche conflict is a persistent theme; resolving it (via Monarchist pact or Mapuche victory) is a significant decision point.
