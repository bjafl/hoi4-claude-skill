---
title: Danish National Focus Tree
category: focus-trees
tags: [denmark, national focus tree, balance of power, welfare vs warfare, nordic]
game_version: "1.19"
dlc: [Arms Against Tyranny]
sources:
  - https://hoi4.paradoxwikis.com/Danish_national_focus_tree
---

## Summary

Denmark's unique focus tree (requires Arms Against Tyranny DLC) centers on choosing between **Welfare and Warfare** via a balance-of-power mechanic. When Denmark is independent, it branches into industrial development or military preparation, with political paths toward democracy, monarchy, or fascism. As a puppet, Denmark can seek independence or align with its overlord. The Nordic Council joint-focus system allows coordination with Finland, Iceland, Norway, and Sweden.

See [Denmark](../05-countries/denmark.md) for the country's 1936 starting profile.

## Welfare vs Warfare Balance of Power

The political branches use a shared balance-of-power meter accessible only when Denmark is independent and has completed **Reaffirm Neutrality**. This meter determines which political-branch focuses become available and which locks:

- **Welfare side:** Favors civilian industry, infrastructure, and democracy; reached by taking welfare-oriented focuses.
- **Warfare side:** Favors military production and preparation; reached by taking military-focused focuses.

Completing certain focuses shifts the balance +/−10.0% in either direction. Crossing the midline may unlock new focus chains and invalidate others. All balance shifts are marked in the tables below.

## Continue the Kanslergadeforlig / Fortify Our Borders Branch

The industrial branch allows Denmark to develop domestic industry (mainland and overseas territories like Greenland, Faroe Islands) and negotiate trade deals with the United Kingdom or German Reich. The mutual exclusive at the start sets the tone: welfare-oriented development vs. wartime preparation.

| Focus | Prerequisites | Mutual Exclusivity | Effects | Notes |
|-------|---------------|--------------------|---------|-------|
| **Continue the Kanslergadeforlig** | None (start of branch) | Fortify Our Borders | Balance +10.0% towards Welfare; Stability +10.00%; Political Power Gain +5%; Consumer Goods Factories −15.0%; Democracy Support +0.05 daily; Unlocks Political Advisor Karl Kristian Steincke | Welfare path: industrial focus, removes Economic Crisis threat |
| **Fortify Our Borders** | None (start of branch) | Continue the Kanslergadeforlig | Balance +10.0% towards Warfare; Military factory construction speed +10.00%; Naval dockyard construction speed +10.00%; Air base construction speed +10.00%; Naval base construction speed +10.00% | Warfare path: military readiness |
| **Agricultural Subsidies** | Continue the Kanslergadeforlig | — | Modifies Danish Produce (Supply Efficiency +5%, Supply Combat Penalties −5.0%, Non-Combat Out of Supply Penalties −5.0%); Population +10.0 monthly; Unaligned Support −0.02 daily; If Jylland (99) controlled: +2 building slots, +1 civilian factory, +2 Max Factories; otherwise random state (prioritize Sjaelland/Fyn) +1 building slot +1 factory | Welfare branch industrial expansion |
| **Support the Schleswigian Farmers** | Agricultural Subsidies; Sønderjylland (912) controlled | — | Replaces Danish Produce with improved version (Supply Efficiency +10%, Supply Combat Penalties −10.0%, Non-Combat Out of Supply Penalties −10.0%, Division Attrition −5.0%, Supply Consumption −5.0%); Unaligned Support −0.02 daily; Sønderjylland: +2 building slots; other state: +1 building slot | South Jutland (Sønderjylland) development |
| **Industrial Investments** | Continue the Kanslergadeforlig | — | If Sjaelland (37) controlled: +2 building slots, +1 civilian factory, factories construction speed +10.00%, infrastructure construction speed +10.00%; otherwise random state (prioritize Fyn/Jylland) +2 building slots, +1 factory | Capital region industrial boost |
| **Public Works** | Agricultural Subsidies OR Industrial Investments; Sjaelland/Fyn/Jylland/Sønderjylland partially controlled | Bypasses if not in full control of any core state | If Sjaelland controlled and <5 infrastructure: +1 infrastructure; else +2000 economic capacity. Same for Fyn, Jylland, Sønderjylland. | Infrastructure via bridge-building |
| **Devalue the Krone** | Continue the Kanslergadeforlig OR Fortify Our Borders | — | Stability −5.00%; Consumer Goods Factories −10.0%; Weekly Stability +0.10%; removes Economic Crisis in 730 days | Devaluation to boost agricultural exports; impacts stability short-term |
| **Trade with Britain** | Devalue the Krone; at peace with UK; fully independent; UK exists | — | UK receives event Denmark Offers Trade Proposal. If accepted: Denmark gains +1 offmap civilian factory; UK gains Danish Produce (Supply Efficiency +5%, Supply Combat Penalties −5.0%, Non-Combat Out of Supply −5.0%, Consumer Goods Factories +10.0%). War breaks the deal; unlocks Danish Trade Deals Decisions | Restores WWI-era agricultural export relationship |
| **Trade with Germany** | Devalue the Krone; at peace with GER; fully independent; GER exists | — | GER receives event Denmark Offers Trade Proposal. If accepted: Denmark gains +1 offmap civilian factory; GER gains Danish Produce. War breaks deal; unlocks Danish Trade Deals Decisions | Alternative to UK trade (historical competitive route) |
| **Build a Modern Dannevirke** | Fortify Our Borders | — | If independent and control Sønderjylland: +2 building slots, +1 military factory, +2 land forts in border provinces, military project construction speed +10.00%. Else if independent and control Jylland (99): +2 building slots, +1 military factory, +2 land forts; else random state: +2 building slots, +1 military factory | Rebuilds historic southern fortifications |
| **Fortify the Islands** | Build a Modern Dannevirke OR Refortify Tunestillingen; any core coastal state controlled | — | Unlocks Decision: Coastal Fortification Efforts. If control Sjaelland: +1 coastal fort in every province. If control Fyn: +2 building slots, +1 military factory, +1 coastal fort every province, military project speed +10.00%. Else: +2 building slots, +1 military factory | Island defense (Eastern Denmark archipelago) |
| **Refortify Tunestillingen** | Fortify Our Borders | — | If independent and control Sjaelland: +3 building slots, +2 military factories, +2 land forts border provinces, +1 anti-air, military project speed +10.00%; else random state: +3 building slots, +2 military factories | Rebuilds WWI-era Copenhagen defenses |
| **Secure Our Supply Lines** | Refortify Tunestillingen | — | Modifies Economic Crisis (Population +10.0 monthly, Democracy Support +0.05 daily); Gains Improved Logistics (Division Attrition −5.0%, Supply Efficiency +5%, Supply Combat Penalties −7.5%, Non-Combat Out of Supply −7.5%, Supply Range +10%, Supply Hub construction speed +25.00%); If Jylland controlled: +2 building slots, military project speed +10.00%; else random state: +1 building slot | Supply-side defensive preparation |
| **Connect the Islands** | Public Works OR Fortify the Islands; full control of at least one core state (Sjaelland/Fyn/Jylland/Sønderjylland) | Bypasses if not in full control of any | If Sjaelland controlled and <5 infrastructure: +1; else +2000 economic capacity surplus (same for Fyn, Jylland, Sønderjylland) | Bridge infrastructure linking islands |

> ⚠️ broken wiki template reconstructed: `[{{{1}}}]` markers in the original wiki (appearing before "Democratic Denmark", "Monarchist", "Fascist") indicate dynasty/government form but lack clear rendering; interpreted as government ideology labels from context.

## Samarbejdsregering Branch (Puppet-only)

Available only when Denmark is a puppet of another nation. Split into three sub-branches: independence resistance, sabotage cooperation, or alignment with overlord.

### Seek Independence Sub-branch

Focuses on resisting the overlord via balance-of-power resistance and foreign military support.

| Focus | Prerequisites | Mutual Exclusivity | Effects |
|-------|---------------|--------------------|---------|
| **Seek Independence** | Denmark is puppet | Align with German Denmark; Sanction Sabotages | Unlocks sub-branch focuses |
| **Our Overlord's Rivals** | Seek Independence | — | Gets event: Seek military support from overlord's enemies. Can lead to military access and support |
| **Home Guard Forces** | Seek Independence | — | Home Guard Divisions (subject-nation troops) gain experience; division training time −10.00% |
| **Overlord Influence** | Seek Independence | — | Continuous focus-like effect: Weekly balance of power +1.00% towards independence when active; interacts with "Undermine Overlord Influence" continuous focus (mechanics note) |
| **Liberation War** | Home Guard Forces | — | Releases Denmark as independent nation; gain war goal against overlord; if overlord is in faction, faction receives war goal against Denmark. Marks end of puppet path |

### Sanction Sabotages Sub-branch

Builds militias for sabotage and ultimately leads to independence with overlord's enemy support.

| Focus | Prerequisites | Mutual Exclusivity | Effects |
|-------|---------------|--------------------|---------|
| **Sanction Sabotages** | Denmark is puppet | Seek Independence; Align with German Denmark | Unlocks sub-branch |
| **Sabotage Support** | Sanction Sabotages | — | Gain national spirit: Sabotage Support (Resistance decay rate +10.0%); allows sabotage actions in occupied/controlled territory |
| **Strengthen Our Militias** | Sanction Sabotages | — | Militia divisions gain combat effectiveness; Division attack +5%, Division defense +5% |
| **Secret Police** | Sabotage Support | — | Gain Secret Police national spirit (Resistance target −10.0%, Compliance growth speed +25.0%); helps suppress enemy occupation if roles reverse |
| **Armed Uprising** | Strengthen Our Militias | — | Releases Denmark as independent; gain war goal against overlord; civil war mechanics if overlord fights back |

### Align with German Denmark Sub-branch

Aligns Denmark with overlord (typically Germany) for negotiated independence and Nordic expansion.

| Focus | Prerequisites | Mutual Exclusivity | Effects |
|-------|---------------|--------------------|---------|
| **Align with German Denmark** | Denmark is puppet; overlord is Germany | Seek Independence; Sanction Sabotages | Unlocks alignment sub-branch; presumes German overlord |
| **Economic Integration** | Align with German Denmark | — | Trade Agreement auto-created with overlord; Overlord Influence decreases as economic ties deepen; overlord may grant industrial concessions |
| **Contribute to the War Effort** | Align with German Denmark | — | Overlord receives military support; send volunteer army/lend-lease. If overlord accepts: Denmark may be released as independent aligned state, gaining overlord's faction invitation |
| **Nordic Alignment** | Contribute to the War Effort | — | Gain claims and war goals on Sweden, Norway, Finland (neighboring Nordic states); prepares for Nordic expansion if independent |
| **Negotiate Our Position** | Economic Integration | — | Can request overlord release Denmark as independent puppet or faction member; affects autonomy & faction positioning |

## Reaffirm Neutrality Branch (Independent-only)

The main political branch, available only when Denmark is fully independent. **Reaffirm Neutrality** is the gate: completing it unlocks the Welfare vs Warfare balance-of-power mechanic and all downstream political sub-branches.

| Focus | Prerequisites | Effects |
|---------|---------------|---------| 
| **Reaffirm Neutrality** | Denmark is independent | Unlocks balance-of-power mechanics; unlocks all downstream political branches |

### Political Unity Sub-branch

Bridge branch that sets the initial political direction. Completion invalidates focuses on the opposite side (Welfare/Warfare).

| Focus | Prerequisites | Effects |
|---------|---------------|---------| 
| **Political Unity** | Reaffirm Neutrality | Choice point: leads to Welfare path (Import Machinery) or Warfare path (National Unity) or shared path (Social Stability) |

### Welfare Path Sub-branches (Civilian Industrial / Aristocratic Democracy)

Emphasizes civilian industry, infrastructure, and democratic governance.

#### Import Machinery and Material Sub-branch

Historical Welfare path focused on civilian goods production.

| Focus | Prerequisites | Balance Shift | Effects |
|---------|---------------|---------------|---------|
| **Import Machinery and Material** | Political Unity; Balance ≥−25% (Welfare-leaning) | +10.0% Welfare | Civilian factory construction speed +15.00%; Consumer Goods factories −10.0%; Infrastructure construction speed +10.00% |
| **Establish Free Trade** | Import Machinery | +10.0% Welfare | Trade volume +10%; reduces trade cost for imports; improves balance of trade |
| **Agricultural Expansion** | Import Machinery | — | Manpower +0.50 daily; Agriculture efficiency +5%; produces surplus food for trade |

#### Social Stability Sub-branch

Shared path building infrastructure and social programs.

| Focus | Prerequisites | Balance Shift | Effects |
|---------|---------------|---------------|---------|
| **Social Stability** | Political Unity | +10.0% Welfare | Stability +5.00%; Resistance decay +5.0%; social spending maintains order |
| **Improve Railroads** | Social Stability | — | Infrastructure in all controlled states +1; Railway construction speed +20.00%; Supply efficiency +5% |
| **Welfare Housing** | Social Stability | +10.0% Welfare | Population +0.25 daily; Stability +2.00%; improves living standards |
| **Worker Cooperatives** | Welfare Housing | +10.0% Welfare | Consumer Goods Factories −5.0%; Factory efficiency +2.5%; worker management model |

### Warfare Path Sub-branch (Military Preparation)

Emphasizes military production and armament; invalidates civilian-focused focuses.

#### National Unity Sub-branch

Military-industrial buildup path.

| Focus | Prerequisites | Balance Shift | Effects |
|---------|---------------|---------------|---------|
| **National Unity** | Political Unity; Balance ≤+25% (Warfare-leaning) | +10.0% Warfare | Military factory construction speed +15.00%; Military factory output +5%; Manpower +0.25 daily |
| **Armament Expansion** | National Unity | +10.0% Warfare | Military factory construction speed +10.00%; Equipment research speed +10.00% |
| **Military Innovation** | National Unity | — | Army experience +25; Army research speed +5.00% |

### Seek Protection Sub-branch (Shared)

Requests military and industrial support from foreign powers (available to both Welfare and Warfare sides after crossing the midline multiple times).

| Focus | Prerequisites | Availability | Effects |
|---------|---------------|---------------|---------|
| **Seek Protection** | Political Unity; Balance at extremes (±40%+) | Shared (both sides) | Can request military support from United Kingdom or German Reich; if accepted: lend-lease equipment, division volunteers, or military access |
| **Request German Support** | Seek Protection | — | Requests German Reich support; if accepted: German volunteers, military access, potential faction invitation |
| **Request British Support** | Seek Protection | — | Requests United Kingdom support; if accepted: British volunteers, naval access, protection guarantee (if UK guarantees) |

### Monarchy Path (The King Assumes Power Sub-branch)

Monarchist government under Christian X or Frederik IX; allows Nordic expansion and closer German ties.

| Focus | Prerequisites | Balance Shift | Mutual Exclusivity | Effects |
|---------|---------------|---------------|--------------------|---------| 
| **Unify the Right** | Political Unity OR Social Stability; Balance ≤−10% (Monarchy-inclined) | — | March on the Capital | Bridge focus preparing for monarchist government |
| **The King Assumes Power** | Unify the Right; Denmark not fascist | +15.0% Welfare OR +15.0% Warfare (depending on route) | March on the Capital | Government becomes Monarchist; Christian X or Frederik IX becomes leader; stability changes; monarchy-aligned ministers |
| **Nordic Monarchy** | The King Assumes Power | — | — | Gain claims on Sweden, Norway, Finland; can pursue Nordic union; prestige +10 |
| **Nordic Union** | Nordic Monarchy; control key Nordic territories | — | — | Unite Nordic states under Danish monarchy; integrates Sweden/Norway if achievable (historical alternate path) |

### Fascist Path (March on the Capital Sub-branch)

Fascist government with German support; focuses on war goals against Britain and Nordic expansion.

| Focus | Prerequisites | Balance Shift | Mutual Exclusivity | Effects |
|---------|---------------|---------------|--------------------|---------| 
| **Unify the Right** | Political Unity OR National Unity; Balance ≥+10% (Fascism-inclined) | — | (same as monarchy path) | Bridge focus preparing for authoritarian government |
| **March on the Capital** | Unify the Right; requires German support event; Germany exists | +15.0% Warfare | The King Assumes Power | Government becomes Fascist; NSDAP-aligned ministers; gains war goal against United Kingdom; Germany gains faction invitation event |
| **German Alignment** | March on the Capital | — | — | Trade agreement with Germany; German volunteers; potential military access; faction alignment |
| **Nordic Domination** | German Alignment | — | — | Gain war goals on Sweden, Norway, Finland; pursue fascist Nordic hegemony under German patronage |

## Sign Forsvarsforliget Branch (Military Modernization)

Available only when Denmark is not a puppet, or has completed **Contribute to the War Effort** (puppet-to-independent transition) and overlord accepts inclusion in faction. Upgrades Denmark's three armed services and modifies their national spirits.

| Focus | Prerequisites | Mutual Exclusivity | Effects |
|-------|---------------|--------------------|---------|
| **Sign Forsvarsforliget** | Denmark independent OR (puppet + Contribute to War Effort + overlord approval) | — | Unlocks military modernization sub-branches |

### Hæren Reorganization Sub-branch (Army)

Upgrades land forces and modifies Hæren national spirit.

| Focus | Prerequisites | Effects |
|---------|---------------|---------| 
| **Hæren Reorganization** | Sign Forsvarsforliget | Modifies Hæren national spirit (Infantry attack +5%, Infantry defense +5%, Manpower +0.25 daily) |
| **Officer Training** | Hæren Reorganization | Army experience +50; Officer quality +10.0% |
| **Mechanized Infantry** | Hæren Reorganization | Mechanized Infantry research speed +25.00%; division speed +5% for motorized divisions |
| **Defensive Positions** | Hæren Reorganization | Fort construction speed +25.00%; entrenchment bonus +10%; land fort building slots +2 |
| **Modern Artillery** | Hæren Reorganization | Support Artillery research speed +25.00%; artillery combat efficiency +5% |

### Expand Ubådsvåbnet Sub-branch (Navy)

Upgrades naval forces and modifies Søværnet national spirit. Requires naval base infrastructure.

| Focus | Prerequisites | Effects |
|---------|---------------|---------| 
| **Expand Ubådsvåbnet** | Sign Forsvarsforliget | Modifies Søværnet national spirit (Submarine attack +10%, Naval base construction speed +10.00%) |
| **Submarine Expansion** | Expand Ubådsvåbnet | Submarine technology research speed +25.00%; naval dockyard output +5%; can build more subs |
| **Mine-layers** | Expand Ubådsvåbnet | Naval mine research speed +25.00%; can lay mines in key waters; naval defense +5% |
| **Coastal Defense** | Expand Ubådsvåbnet | Coastal fort construction speed +25.00%; torpedo boat production +10.00%; light cruiser research +15.00% |
| **Naval Doctrine** | Expand Ubådsvåbnet | Navy experience +50; naval doctrines unlock; submarine/surface combat tactics |

### Domestic Designs / Foreign Designs Sub-branch (Air Force)

Upgrades air forces and modifies Flyvevåbnet national spirit. Split path: develop domestic aircraft or rely on foreign designs (license production).

| Focus | Prerequisites | Effects |
|---------|---------------|---------| 
| **Flyvevåbnet Modernization** | Sign Forsvarsforliget | Modifies Flyvevåbnet national spirit (Fighter attack +10%, Air base construction speed +10.00%) |
| **Domestic Designs** | Flyvevåbnet Modernization | Fighter aircraft research speed +25.00%; enables domestic fighter development; air industrial capacity +2 |
| **Advanced Engine Production** | Domestic Designs | Engine research speed +15.00%; improves domestic aircraft performance |
| **Foreign Designs** | Flyvevåbnet Modernization | License production from foreign powers (Germany/UK); fighter production speed +10.00%; access to foreign fighter tech |
| **Training Expansion** | Flyvevåbnet Modernization | Air experience +50; Pilot quality +10.0%; air combat efficiency +5% |

## Form the Nordic Council Branch (Joint Nordic Focus)

Multi-nation branch for Nordic alliance. Available to Denmark, Finland, Iceland, Norway, and Sweden. When any Nordic nation creates a faction with another Nordic nation, this branch allows **any faction member to complete any other member's Nordic focuses**, enabling coordinated military/industrial decisions.

| Focus | Prerequisites | Requirements | Effects |
|-------|---------------|--------------|---------|
| **Form the Nordic Council** | In faction with another Nordic nation (Finland/Iceland/Norway/Sweden) | — | Unlocks Nordic joint focuses; faction research bonuses if all Nordic nations included |
| **Nordic Defense Pact** | Form Nordic Council | All faction members contribute | +10% army research speed for faction members; allied supply +5% between Nordic nations |
| **Nordic Economic Cooperation** | Form Nordic Council | — | Trade agreements between Nordic nations; civilian factory efficiency +5% within faction; resources shared |
| **Nordic Military Doctrine** | Form Nordic Council | — | Doctrine research speed +10.00% for faction; shared doctrine advances; coordinated land/air operations |

---

## Notable Mechanics

**Continuous Focuses (post-10 focuses):** Denmark can activate **Undermine Overlord Influence** (if puppet) for −1 PP/day with weekly balance-of-power change +1.00% toward independence. See [National Focus and Continuous Focus](../01-mechanics/national-focus.md) for generic and Denmark-specific continuous focuses.

**Balance of Power (Welfare vs Warfare):** The slider at the political branches determines which focuses are available:
- Extreme Welfare (≤−50%): locks warfare-path focuses; unlocks advanced civilian industry.
- Extreme Warfare (≥+50%): locks welfare-path focuses; unlocks advanced military.
- Crossover regions (−40% to +40%) allow both paths and shared sub-branches.

**Puppet State Mechanics:** Denmark's political branches are hidden/locked when a puppet. The Samarbejdsregering branch replaces normal politics; completing any sub-branch path (Independence, Sabotage, or Alignment) releases or repositions Denmark.

**Nordic Faction Sharing:** The Nordic Council focuses are shared between Denmark, Finland, Iceland, Norway, and Sweden when in the same faction; any member can take any other member's Nordic focus if faction prerequisites are met.
