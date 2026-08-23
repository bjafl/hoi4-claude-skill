---
title: Brazilian national focus tree
category: focus-trees
tags: [brazil, focus tree, communist, democratic, monarchist, fascist, estado novo]
game_version: "1.19"
dlc: [Trial of Allegiance]
sources:
  - https://hoi4.paradoxwikis.com/Brazilian_national_focus_tree
---

## Summary

Brazil's unique focus tree (requires Trial of Allegiance DLC) branches into four main ideological paths: Communist (Second Intentona Comunista), Democratic (Repeal the National Security Laws), Monarchist (Romanticize Imperial History), and Historical/Fascist (Tribunal de Segurança Nacional), plus an industrial branch (Aftermath of the Coffee Crisis). Each path unlocks different military and economic bonuses, though the Communist path triggers a civil war. The tree also includes shared military branches for all ideologies and regional ambitions in South America.

See [Brazil](../05-countries/brazil.md) for the country's 1936 starting profile.

## Second Intentona Comunista Branch

Communist ideology branch, ending in civil war if >60% support; Democratic civil war if <60%.

| Focus | Prerequisites | Effect |
|---|---|---|
| **Second Intentona Comunista** | Mutually exclusive: Tribunal de Segurança Nacional, End the State of Emergency | State of Emergency: Daily Communism +0.05, Stability −5%. Political Power +120 |
| **Infiltrate the Military** | Second Intentona Comunista; >30% PCB support; not Launch the Revolution | Military units join revolution (higher ratio in civil war). Stability +5% |
| **Radicalize the Proletariat** | Second Intentona Comunista | 365-day spirit: Stability −10%, Daily Communism +0.03. Unlock Proletarian Equality units |
| **Free Prestes from Prison** | Infiltrate the Military OR Radicalize the Proletariat; mutually exclusive: Revive the Aliança; at peace with Soviet Union; not Launch the Revolution | Communism +10%. Receive 2 extra communist militia divisions in civil war; Soviet advisors available post-revolution |
| **Revive the Aliança Nacional Libertadora** | Infiltrate the Military OR Radicalize the Proletariat; mutually exclusive: Free Prestes; not Launch the Revolution | Communism +5%, Stability +5%. Receive 2 extra communist militia divisions in civil war |
| **Seek Soviet Support** | Free Prestes from Prison; at peace with Soviet Union; Current ruling party is Communist; >30% PCB support | Political Power +150. Soviet Union event (Aid Brazilian Communists): −30% lend-lease tension, +3 max volunteer divisions, −100% volunteer divisions cost |
| **Launch the Revolution** | Free Prestes from Prison OR Revive the Aliança; >35% PCB support; bypass if ruling party already Communist | Triggers civil war (amount of opposing forces based on Communism popularity). If Communism >60%: Immediate Communist coup, no civil war. Radio Nacional spirit (Stability +5%, Research Speed +4%, Ideology drift defense +30%) if completed. Creates Guarda Vermelha/Cangaço/National Militia divisions based on completed focuses |
| **Sway the Cangaço to our Cause** | Revive the Aliança Nacional Libertadora; not Deal With the Cangaço | Army experience +50. Removes Legacy of the Cangaço decisions. Gain 3 Cangaço Militia units when civil war triggers or Communism takes power |
| **Align with Moscow** | Free Prestes from Prison; Launch the Revolution; mutually exclusive: Prevent a Personality Cult, Cangaço Coup; not in civil war | Political Power +50. Luís Carlos Prestes becomes leader (Communist). Aligned with Stalin spirit: Stability +5%, Same ideology opinion +100%, Ideology drift defense +25%, Daily Communism +0.03. Removes Weak Government |
| **Prevent a Personality Cult** | Launch the Revolution; Revive the Aliança; mutually exclusive: Align with Moscow, Cangaço Coup; not in civil war | Council of Aliança Nacional Libertadora becomes leader. Council of the ANL spirit: Stability −5%, War support +15%, Daily Communism +0.03. Factory construction speed +10%. Removes Weak Government |
| **Cangaço Coup** | Launch the Revolution; Sway the Cangaço; mutually exclusive: Align with Moscow, Prevent a Personality Cult; not in civil war | Lampião becomes leader. Bandit Revolutionary spirit: Recruitable population +5%, Out of Supply penalties −10%, Stability −10%, War support +20%. Communist party renamed Cangaço. Removes Weak Government. Removes Cangaço Active In State modifiers |
| **Soviet Economic Aid** | Align with Moscow; at peace with Soviet Union; Soviet Union exists; Current ruling party Communist; Soviet opinion of Brazil ≥50 | +2 offmap civilian factories. Mutual opinion increase: Brazil/Soviet Union +25 each |
| **Purchase Soviet Equipment** | Soviet Economic Aid; mutually exclusive: License Agreements with the Soviet Union; Soviet opinion ≥50; at peace with Soviet Union | *Arms Against Tyranny DLC:* Equipment subsidy 1000 production cost for Infantry Equipment, Towed Artillery, Support Equipment (all Soviet). *Base game:* 2000 Soviet Infantry Equipment, 500 Soviet Towed Artillery added to stockpile |
| **License Agreements with the Soviet Union** | Soviet Economic Aid; mutually exclusive: Purchase Soviet Equipment; Soviet opinion ≥50; at peace with Soviet Union | Soviet Union gets event to negotiate license production deal in Brazil (more likely with high Soviet opinion) |
| **Invite Soviet Arms Industry** | Purchase Soviet Equipment OR License Agreements; Soviet opinion ≥50 | *Arms Against Tyranny:* Foreign MiO invitations to Rubin Design Bureau (Naval +3), MiG Design Bureau (Air +3), GAZ Automotive (+3). *Base game:* Design companies available with Naval Research Speed +15%, Air Research Speed +15%, Motorization Research Speed +15% |
| **International Brigades** | Align with Moscow OR Prevent a Personality Cult OR Cangaço Coup | Enable send volunteers. International Brigades spirit: Send volunteers tension −20%, Max volunteer divisions +3, Volunteer division cost −25% |
| **Form the EICI** | Align with Moscow OR Prevent a Personality Cult OR Cangaço Coup | *La Résistance:* Create intelligence agency, add operatives Robert Ivanov and Nadiya Morozova. *Base game:* +2 ×100% research bonus for Electronics. *By Blood Alone:* Add Photo Reconnaissance tech |
| **Sway the Neighbors** | Form the EICI | *No La Résistance:* Unlock Sway the Neighbors decisions to promote Communism in South America, set flag. *La Résistance:* Sway the Neighbors Intelligence Campaign spirit (Operative slots +1), operative Julieta Soria added |
| **The People's University of Brazil** | Align with Moscow OR Prevent a Personality Cult OR Cangaço Coup | +1 research slot |
| **Nationalization of Industry** | Align with Moscow OR Prevent a Personality Cult OR Cangaço Coup | Random owned controlled state: +2 building slots, +2 civilian factories |
| **Rapid Industrialization** | Nationalization of Industry | Two random owned fully controlled non-Amazon states (not yet industrialized): +1 building slot each, +1 military factory each, set state flag |
| **An Atheist State** | Rapid Industrialization; mutually exclusive: Embrace Socialist Aligned Theologians | An Atheist State spirit: Political Power gain −10%, Stability −10%, Research Speed +15% |
| **Embrace Socialist Aligned Theologians** | Rapid Industrialization; mutually exclusive: An Atheist State | Collaboration with the Church spirit: Political Power gain +20%, Stability +10%, Research Speed −5% |
| **Proletarian Equality** | An Atheist State OR Embrace Socialist Aligned Theologians | Proletarian Equality spirit: Recruitable population +10%, Stability −5%, Daily Communism +0.03. Unlock Olga Benário Prestes as unit leader |
| **Collectivization of Agriculture** | Nationalization of Industry | Collectivized Agriculture spirit: Consumer goods −10%, Factory output +10%, Daily Communism +0.01 |
| **Collectivization of Transport** | Collectivization of Agriculture | +30 Brazilian Train to stockpile. +1 ×100% research bonus for Trains and Railways. Collectivized Mass Transit spirit: Division speed +10% |

## Expand the Revolution Sub-branch

Communist expansion into South America; requires >60% war support and 200K+ manpower in field.

| Focus | Prerequisites | Effect |
|---|---|---|
| **Expand the Revolution** | Invite Soviet Arms Industry OR Proletarian Equality; >60% war support; >200K manpower in field; Current ruling party Communist | 1460-day Expanding the Revolution spirit: Recruitable population +5%, Supply consumption −25%, Division attack +10% |
| **Join the Comintern** | Expand the Revolution; mutually exclusive: Latin American Socialist Cooperative; fully independent; not in Comintern; bypass if already in faction with Soviet Union | Soviet Union event: Brazil seeks to join the Comintern. Requirements: Soviet Union is Communist, faction leader, at peace with Brazil, >50 opinion of Brazil |
| **The Latin American Socialist Cooperative** | Expand the Revolution; mutually exclusive: Join the Comintern; fully independent; bypass if already in faction; Current ruling party Communist | Enable create factions. Create faction: The Latin American Socialist Cooperative |
| **Smash South American Fascism** | Join the Comintern OR Latin American Socialist Cooperative | War goals against all Fascist South American nations (excludes El Salvador, Mexico, Dominican Republic, Panama) |
| **Oust the Empires** | Join the Comintern OR Latin American Socialist Cooperative | Unlock South American Anti-Colonialism decisions to liberate non-factional colonies |
| **Establish ULASR** | Join the Comintern OR Latin American Socialist Cooperative | Rename to Union of Latin American Socialist Republics. All South American states become cores of Brazil |
| **Jaguar Diplomacy** | Join the Comintern OR Latin American Socialist Cooperative | Unlock Jaguar Diplomacy decisions to establish non-aggression pacts with major powers opposed to Communism |
| **End South American Capitalism** | Join the Comintern OR Latin American Socialist Cooperative | War goals against all Democratic and Non-Aligned South American nations (excludes El Salvador, Mexico, Dominican Republic, Panama) |

## End the State of Emergency Branch

Main branch: removes State of Emergency spirit, leads to Democratic or Monarchist paths.

| Focus | Prerequisites | Effect |
|---|---|---|
| **End the State of Emergency** | Mutually exclusive: Second Intentona Comunista, Tribunal de Segurança Nacional | Remove State of Emergency national spirit |

## Repeal the National Security Laws Sub-branch

Democratic path: centralization vs. federalism, military cooperation, foreign volunteers.

| Focus | Prerequisites | Effect |
|---|---|---|
| **Repeal the National Security Laws** | End the State of Emergency; mutually exclusive: Romanticize Imperial History | Armando de Sales Oliveira becomes Democratic leader. Democratic Reformer spirit: Daily Democracy +0.10. Democratic party renamed União Democrática Brasileira |
| **Greater Federalism** | Repeal the National Security Laws; mutually exclusive: Promote Centralization | Embracing Federalism spirit: Political Power gain −10%, Stability +10%, Surrender limit +10%, Daily Democracy +0.03 |
| **Promote Centralization** | Repeal the National Security Laws; mutually exclusive: Greater Federalism | Centralized Power spirit: Political Power gain +10%, Construction speed +5%, Daily Democracy +0.03 |
| **Compromise with the Military** | Greater Federalism OR Promote Centralization; mutually exclusive: Collaborate with the Military | Compromise with the Military spirit: Stability +5%, Army experience gain +10%, Recruitable population −2% |
| **Collaborate with the Military** | Greater Federalism OR Promote Centralization; mutually exclusive: Compromise with the Military | Collaborate with the Military spirit: Stability −5%, Factory output +5%, Army research speed +10% |
| **Allow Volunteers for Foreign Wars** | Compromise with the Military OR Collaborate with the Military; Current ruling party Democratic | Enable send volunteers |
| **Invite Foreign Military Industrialists** | Allow Volunteers for Foreign Wars; Current ruling party Democratic; requires: Compromise with the Military OR Collaborate with the Military | Foreign MiO invitations (varies by DLC): US/UK companies for industrial/design improvements, or corresponding nations based on DLC |
| **Reclaim the Amazon** | Repeal the National Security Laws; Current ruling party Democratic | Receive war goal against all nations controlling Amazon states; +10% war support if war is declared against former owner |
| **Industrialize the Sertão** | Compromise with the Military OR Collaborate with the Military; Current ruling party Democratic | Random non-Amazon state: +2 building slots, +1 military factory, +1 civilian factory. Set state flag to prevent repeat |

## Romanticize Imperial History Sub-branch

Monarchist path: restore Portuguese imperial line (Pedro de Alcântara or Pedro Henrique), unite with Portugal, imperial ambitions.

| Focus | Prerequisites | Effect |
|---|---|---|
| **Romanticize Imperial History** | End the State of Emergency; mutually exclusive: Repeal the National Security Laws | Monarchist support increased. Hidden effect: Armando de Sales Oliveira retires; new Democratic leader assigned. Democratic party renamed. Initial ideological direction toward Monarchism |
| **Restore the Monarchy** | Romanticize Imperial History; mutually exclusive: Install the Integralists | Pedro de Alcântara or Pedro Henrique becomes leader. Monarchist government established |
| **Petrópolis or Vassouras** | Restore the Monarchy | Mutually exclusive choice: Install Pedro de Alcântara (Petrópolis branch) or Pedro Henrique (Vassouras branch) of House of Orléans-Braganza. Each unlocks different downstream focuses |
| **Crown the Chosen One (Petrópolis)** | Petrópolis branch selected | Pedro de Alcântara officially crowned. Legitimist Claim spirit: Stability +10%, Daily Monarchism +0.05. Gain claims on Portugal |
| **Crown the Chosen One (Vassouras)** | Vassouras branch selected | Pedro Henrique officially crowned. Legitimist Claim spirit: Stability +10%, Daily Monarchism +0.05. Gain claims on Portugal |
| **Seek Portuguese Support** | Restore the Monarchy; at peace with Portugal; not in faction with Portugal; Current ruling party Monarchist | Portugal event to support Brazilian Monarchy. If accepted: Portugal gains mutual opinion +50, defensive pact offer |
| **The Iberian Union** | Crown the Chosen One; Seek Portuguese Support accepted; at peace with Portugal | Vassalize or annex Portugal (via focus outcome). Form Iberian Union faction if not already in one; Portugal joins if vassalized |
| **Recover the Colonies** | The Iberian Union OR Seek Portuguese Support (if Portugal refused/failed) | War goals to recover former Portuguese colonies in Africa (Angola, Mozambique, etc.) |
| **Establish the Empire** | The Iberian Union | Rename to Empire of Brazil or Empire of Brazil and Portugal (depending on whether Portugal was annexed/vassalized). Gain prestige and claims on additional territories |
| **Restore the Hierarchy** | Restore the Monarchy | Gain national spirit reducing political power gain but increasing stability. Support for Monarchism increases |
| **Support the Church** | Restore the Hierarchy; Current ruling party Monarchist | Church Influence spirit: Political Power gain +10%, Stability +5%, Research Speed −5%, Ideology drift defense +10% |
| **Military Regeneration** | Restore the Hierarchy; Current ruling party Monarchist | Army experience +100, Military Research Speed +10%, +1 ×100% research bonus for Land Doctrine |

## Claim the French Throne Sub-branch

Unlocks when Pedro de Alcântara installed and dies after Jan 1, 1940; Pedro Gastão becomes leader.

| Focus | Prerequisites | Effect |
|---|---|---|
| **Claim the French Throne** | Pedro de Alcântara installed; died after Jan 1, 1940; Pedro Gastão becomes leader | War goal and claims against France from Orléans line succession. Emboldened by Gaspers spirit (temporary) if activated during France civil war |
| **Support French Royalists** | Claim the French Throne; at peace with France; Current ruling party Monarchist | Unlock French Royalist support focuses/decisions. Can send volunteers to French Royalist factions if civil war occurs |
| **Restore French Monarchy** | Support French Royalists; French civil war active; Brazilian forces substantial in war | War goal and claims on French throne. Potential to enforce restoration of French monarchy via peace deal |

## Tribunal de Segurança Nacional Branch

Historical path: Getúlio Vargas stays in power, Estado Novo (quasi-fascist), industrial/military buildup. Splits into Fascist (Estado Moderno) or Non-Aligned (Secure Our Borders) sub-branches.

| Focus | Prerequisites | Effect |
|---|---|---|
| **Tribunal de Segurança Nacional** | Mutually exclusive: Second Intentona Comunista, End the State of Emergency | Getúlio Vargas consolidates power. Tribunal de Segurança Nacional spirit: Stability +15%, Daily Non-Aligned support +0.03, Political Power gain +10%. Removes State of Emergency |
| **Estado Novo** | Tribunal de Segurança Nacional | Suspend democracy (removes political pressure), focus on industry and economy. Estado Novo spirit: Stability +10%, Production efficiency cap +5%, Research Speed +5%, Consumer goods −5% |

## Estado Moderno Sub-branch

Fascist sub-branch: Integralist movement, Plínio Salgado, military modernization.

| Focus | Prerequisites | Effect |
|---|---|---|
| **Estado Moderno** | Tribunal de Segurança Nacional; mutually exclusive: Install Salazar's Regime | Adopt Integralist/Fascist ideology, Estado Moderno government established. Estado Moderno spirit: Fascism popularity +0.05/day, Stability +5%, Army experience gain +10% |
| **Support the Integralists** | Estado Moderno | Gain political power and Integralist support. Hidden effect: Increases Fascism popularity, decreases Democracy/Communism popularity |
| **Oust Vargas** | Estado Moderno; Current ruling party Fascist | Plínio Salgado becomes leader of Fascist party. Optional regime change if desired. Fascist leader secured |
| **Cult of the Leader** | Oust Vargas (optional - can use Vargas or Salgado) | National spirit choice: Personality cult or collective leadership. Affects stability/political power but increases war support |
| **Green Brazil** | Estado Moderno | Fascist expansion ambitions in South America. Unlock Green Brazil decisions to establish fascist hegemony regionally |
| **Militarize our Society** | Estado Moderno | Conscription laws, war support +20%, Recruitable population +5%, Stability −5%. Military bonuses: Army research speed +10%, Division attack +10% |
| **Militarize the Amazon** | Militarize our Society | Amazon states: +2 building slots each, +1 military factory each. Set state flags to prevent stacking |
| **Form the National Guard** | Militarize our Society; Current ruling party Fascist | Create National Guard division template. Army experience +50, Division stats +5% across the board |
| **Embrace Fascist Theology** | Estado Moderno | Fascist religious doctrine. Spirit: Stability +5%, Political Power gain +10%, Daily Fascism +0.03, Research Speed −5% |
| **Establish the Integralist State** | Estado Moderno; Current ruling party Fascist | Full Integralist government consolidation. Stability +15%, Ideology drift defense +25%, Daily Fascism +0.05 |
| **Fascist Youth Indoctrination** | Embrace Fascist Theology; Current ruling party Fascist | Youth indoctrination programs. Spirit: Political Power gain −5%, Recruitable population +10%, War support +15%, Stability −5% |

## Secure Our Borders Sub-branch

Shared historical/non-aligned sub-branch: foreign relations (US, Germany/Italy, or independent), regional hegemony.

| Focus | Prerequisites | Effect |
|---|---|---|
| **Secure Our Borders** | Tribunal de Segurança Nacional OR Romanticize Imperial History (Monarchist) | Base foreign relations branch. Stability +5%, Political Power +50. Unlocks access to regional diplomacy focuses |
| **Good Neighbor Policy** | Secure Our Borders; mutually exclusive: Domination of the Americas; Current ruling party Democratic OR Non-Aligned | Align with United States. US opinion bonus +50, diplo tension −20%, receive US offers for design companies |
| **Fascist Trade Alliance** | Secure Our Borders; mutually exclusive: Good Neighbor Policy; Current ruling party Fascist OR Non-Aligned | Align with Germany/Italy. Germany/Italy opinion bonus +50, trade agreements, access to Axis design companies |
| **Independent South American Power** | Secure Our Borders; Current ruling party Non-Aligned | Maintain neutrality, strengthen regional position. Stability +5%, Independence spirit: Diplomatic tension cost −10%, Faction cost −10% |

## Good Neighbor Policy Sub-branch

Democratic/Non-Aligned path: cooperation with US and regional integration (United States of South America).

| Focus | Prerequisites | Effect |
|---|---|---|
| **Economic Cooperation with the USA** | Good Neighbor Policy; Current ruling party Democratic OR Non-Aligned; at peace with USA | Lend-lease treaties, trade agreements. Add civilian/military factories. US opinion +50 |
| **Military Cooperation with the USA** | Economic Cooperation with the USA; Current ruling party Democratic OR Non-Aligned; at peace with USA | US military advisors, design companies, technology sharing. Army research speed +15% |
| **Invite American Investors** | Economic Cooperation with the USA | Random owned state: +2 building slots, +1 civilian factory, +1 military factory. Hidden effect: Increased US economic ties |
| **United States of South America** | Economic Cooperation with the USA OR Military Cooperation; Current ruling party Democratic OR Non-Aligned | Initiate confederation of South American nations (peaceful union via events/decisions). Other democracies/non-aligned nations offered to join Brazil-led federation. Potential to core multiple South American states |
| **Hemisphere Defense** | Military Cooperation with the USA | War support +15%, Army experience +50. US extends defensive umbrella; reduced aggression from regional powers. US opinions drift more positive |

## Domination of the Americas Sub-branch

Fascist/Non-Aligned path: conquest of South America, alliance with Germany/Italy.

| Focus | Prerequisites | Effect |
|---|---|---|
| **Domination of the Americas** | Secure Our Borders; mutually exclusive: Good Neighbor Policy; Current ruling party Fascist OR Non-Aligned | War goals on all non-faction South American nations (except US-aligned). War support +25%, Army experience +50 |
| **Fascist Expansion in South America** | Domination of the Americas; Current ruling party Fascist | Hidden effect: War goals against democratic South American nations. War support +20%, Fascism popularity +0.05/day |
| **German Military Cooperation** | Fascist Trade Alliance (if chosen) OR Domination of the Americas; at peace with Germany; Current ruling party Fascist OR Non-Aligned | Germany military advisors, design companies (Navy, Air, Land). Army research speed +10%, Navy research speed +10%, Air research speed +10% |
| **Italian Military Cooperation** | German Military Cooperation (optional alternative) OR Domination of the Americas; at peace with Italy; Current ruling party Fascist OR Non-Aligned | Italy military advisors, design companies. Factory efficiency +5%, Research speed +5% |
| **South American Hegemony** | Domination of the Americas; controls majority of South American states; Current ruling party Fascist OR Non-Aligned | Rename to South American Empire or similar (pending focus outcome). Gain prestige and cores on South American territories. Unity spirit: Stability +20%, Division defense +10% |
| **Seize the Canal** | South American Hegemony; controls Panama states | War goal against Panama (if independent) or occupation option. Control Panama Canal: Supply +30%, Trade efficiency +15% |

## Aftermath of the Coffee Crisis

Industrial/economic branch: deal with Cangaço banditry, remove neglect modifiers, industrialization.

| Focus | Prerequisites | Effect |
|---|---|---|
| **Aftermath of the Coffee Crisis** | Tribunal de Segurança Nacional; Current ruling party Non-Aligned OR Fascist | Base industrial focus. Political Power +100, Stability +5%. Unlocks regional economic development |
| **Deal With the Cangaço** | Aftermath of the Coffee Crisis; not Sway the Cangaço to our Cause (Communist path) | Military operations against Cangaço bandits. Northeast regions (affected by Cangaço): Stability +10%, War support +10%, remove Legacy of the Cangaço modifiers |
| **Modernize the Rubber Industry** | Aftermath of the Coffee Crisis | Amazon state (random): +2 building slots, +1 civilian factory. Rubber production efficiency +10% (if affected state has rubber resource) |
| **Invest in Agriculture** | Aftermath of the Coffee Crisis | Food production efficiency +15%, Consumer goods consumption −5%, Recruitable population +3%. Random agricultural state: +1 building slot, +1 civilian factory |
| **Build the Trans-Amazonian Highway** | Modernize the Rubber Industry OR Invest in Agriculture | Amazon infrastructure: Stability +10%, Infrastructure in Amazon states +1 level, Movement speed in Amazon +20% |
| **Move the Capital to Brasília** | Build the Trans-Amazonian Highway; controls Brasília state (941 or equiv) | Capital officially moved to Brasília (Brazil state/region). Prestige +50, Stability +5%, hidden effects: Government relocates, new capital position affects supply network |
| **Establish Petrobrás** | Aftermath of the Coffee Crisis | Oil production efficiency +50%, Oil extraction +25%, Factory output +10% (oil-related). Strategic resources bonus |
| **Steel Production Initiative** | Aftermath of the Coffee Crisis | Steel production +50%, Resource extraction efficiency +15%, Factory output +5%. Random state: +1 building slot, +1 military factory |
| **Expand Our Harbors** | Aftermath of the Coffee Crisis OR Economic Cooperation with the USA (Democratic) | Naval bases: Dockyard output +20%, Convoy efficiency +10%, Trade route capacity +15% |
| **Aviation Industry** | Aftermath of the Coffee Crisis | Aircraft production +20%, Air research speed +10%, Air bases construction speed +20%. Air experience +50 |

## Trial of Allegiance Shared Military Branches

Shared military branches available to all ideologies; grant special spirits and bonuses; some effects depend on which nation player aligns with.

> ⚠️ Broken wiki template reconstructed: The raw wiki source contained incomplete template markers `[{{{1}}}]` for ideology icons/flags. Effects below are reconstructed from context.

| Focus | Prerequisites | Effect |
|---|---|---|
| **Trial of Allegiance** | Secure Our Borders OR Estado Novo OR similar branch leader taken | Military trials to determine strategic alignment. Gains military spirit depending on chosen path. Unlocks specialized military focuses |
| **Fortify Our Coasts** | Trial of Allegiance | Coastal defenses in all Brazilian coastal states. Coastal fort construction speed +50%, Coastal defense +15%, Amphibious assault defense +20% |
| **Expand Naval Capacity** | Trial of Allegiance | Dockyard expansion, naval doctrine flexibility. Navy experience +50, Naval research speed +10%, Dockyard output +10% |
| **Air Superiority Program** | Trial of Allegiance | Fighter aircraft production priority. Air experience +100, Fighter production +30%, Air superiority in contested airspace |
| **Jungle Warfare Doctrine** | Trial of Allegiance | Specialized training for Amazon/jungle terrain combat. Army experience +50, Division defense +25% in jungle/forest terrain, Movement speed +15% in difficult terrain |
| **Military Industrial Complex** | Trial of Allegiance; Current ruling party not Democratic (varies by ideology) | Military factory expansion and efficiency. +3 building slots random states, Military factory construction speed +30%, Production efficiency cap +5% for military goods |
| **Defensive Alliances** | Trial of Allegiance; Current ruling party Non-Aligned | Regional defensive pacts. War support +10%, Faction join cost −25%, Opinion with faction members +50, Defensive pact offers available to regional powers |

---

**Note:** Some effects require Arms Against Tyranny, La Résistance, or By Blood Alone DLCs and are noted inline. Bypass conditions and dynamic modifier handling vary by game state and are typically auto-resolved when requirements are met. Civil war outcomes depend on Communist party popularity (>60% = immediate coup; <60% = civil war) and forces deployed by focuses taken before Launch the Revolution.
