---
title: Siamese National Focus Tree
category: focus-trees
tags: [siam, focus tree, thunder at our gates, khana ratsadon, civil war, monarchy, democracy, military]
game_version: "1.19"
dlc: [Thunder at Our Gates]
sources:
  - https://hoi4.paradoxwikis.com/Siamese_national_focus_tree
---

## Summary

Siam gains a unique focus tree with the Thunder at Our Gates DLC; without it, Siam uses the generic tree. The tree revolves around the Khana Ratsadon (The People's Party), which is split into Military and Civilian wings, each competing for approval. Player decisions determine the balance of power, leading to either a royalist-military civil war, a democratic-civilian civil war, or the democratic government consolidating power without conflict. The final outcome determines the regency choice (absolutist Boworadej, soldier Songsuradet, or constitutionalist Rangsit) and government form (absolute monarchy vs. constitutional monarchy).

See [Siam](../05-countries/siam.md) for the country's 1936 starting profile.

## Foundation Focus

| Focus | Prerequisites | Effects |
|---|---|---|
| The Khana Ratsadon | None | +35 political power; gains national spirits "Military Wing: Neutral" and "Civilian Wing: Neutral"; Khana Ratsadon becomes the leading party and is divided into Army Wing (favors fascism and militarization) and Civilian Wing (favors democracy and civilian industry); approval states are Rebellious, In Opposition, Neutral, Slight Support, Full Support |

## Civilian Wing Path

The civilian-focused route emphasizes democratic governance, infrastructure, research, and civilian industry. Increases civilian approval, decreases military approval. Opens the democratic civil war route if civilian support reaches Full Support.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| Strengthening the Civilian Wing Position | The Khana Ratsadon | None | Moves Pridi Banomyong from Minister of Foreign Affairs to Minister of Interior (if active); +8% political power gain daily, +0.02 daily democracy support, +10.00% infrastructure construction speed, +5.00% civilian factory construction speed; increase civilian approval and decrease military approval; anti-fascist raids now increase civilian wing approval and reduce military wing approval |
| Civil Nationalism | Strengthening the Civilian Wing Position | None | +5.00% stability, +3% war support, +8% democratic party popularity; one random core state gains 1 free building slot and 1 civilian factory |
| The True Heirs of 1932 | Strengthening the Civilian Wing Position | None | +5% democratic party popularity; 1× 50% research bonus for Electronics; decrease military approval and increase civilian approval |
| Thammasat University | Strengthening the Civilian Wing Position | None | +1 research slot |
| Dominate Public Symbols | Civil Nationalism OR The True Heirs of 1932 | None | One random core state with <4 infrastructure: +3 building slots, +2 infrastructure; +3% stability, +10% democratic party popularity |
| Civil Service Heroism | The True Heirs of 1932 | None | 1× 50% research bonus for Electronics; gains national spirit "Civil Service Heroism" (+4.00% research speed) |
| Spread Democratic Sentiment in Universities | Thammasat University AND Civil Service Heroism | None | 1× 33% research bonus for Industry; modifies "Civil Service Heroism" to +8.00% research speed, +0.02 daily democracy support, −20% political advisor cost; increase civilian approval and decrease military approval |
| Defenders of Constitutional Liberty | Spread Democratic Sentiment in Universities | None | Replaces "Civil Service Heroism" with "Defenders of Constitutional Liberty" national spirit: +15.0% division defense on core territory, +10.00% research speed, +0.1 daily democracy support, +10.00% infrastructure construction speed, +5.00% civilian factory construction speed, −20% political advisor cost; opens democratic civil war route |

## Military Wing Path

The military-focused route emphasizes army experience, militarization, and fascist ideology. Increases military approval, decreases civilian approval. Leads to the royalist-military civil war.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| Consolidate Military Wing Control | The Khana Ratsadon | None | One random core state (prioritizing Bangkok) gains 1 free building slot and 1 military factory; 1× 33% research bonus for Infantry Weapons; increase military approval and decrease civilian approval; anti-democratic raids increase military approval and reduce civilian approval |
| The Peoples Day | Consolidate Military Wing Control | Hold Military Parades | +12% stability, +5% democratic party popularity; decrease military approval and increase civilian approval |
| Hold Military Parades | Consolidate Military Wing Control | The Peoples Day | +3% war support, +5% fascism party popularity; gives certain generals "Media Personality" trait; +100.0% army reassignment duration for affected leaders; increase military approval and decrease civilian approval |
| Embed Technocrats in Civilian Institutions | Consolidate Military Wing Control | Military Academies Indoctrination | Gains "Civilian Technocrats" national spirit: +10.00% resource gain efficiency, −15% political advisor cost, +5.00% coal gain efficiency |
| Military Academies Indoctrination | Consolidate Military Wing Control | Embed Technocrats in Civilian Institutions | +5% fascism party popularity, +35 army experience; increase military approval and decrease civilian approval |
| Sideline Disloyal Officers | Strengthening the Civilian Wing Position | None | Two random generals gain "Reassigned" trait for 4 years (cannot give bonuses); two random generals without Reassigned gain +1 skill level and a random positive trait; increase civilian approval and decrease military approval |
| Direct Funds from the Military Towards Development | Strengthening the Civilian Wing Position | None | Gains "Redirected Military Funds" national spirit for 1 year: −15.0% consumer goods factories factor, −15.00% factory output, −15.00% military factory construction speed, +15.00% civilian factory construction speed, +15.00% infrastructure construction speed; decrease military approval and increase civilian approval |
| Support Songsuradets Military Clique | Sideline Disloyal Officers OR Direct Funds from the Military Towards Development | None | Phraya Songsuradet gains +1 attack, +1 logistics, +1 defense; gains "Politically Connected" and "Skilled Staffer" traits; −10.0% leader experience gain, −50.0% promotion cost; +6 general max army size, +35 army experience; if civil war occurs, Songsuradet supports your side with 3 extra divisions (warning: strengthening him then executing The Songsuradet Rebellion will cause him to resist) |
| The Royal Police | Sideline Disloyal Officers OR Direct Funds from the Military Towards Development | None | Gains "The Royal Police Allegiance" national spirit: +2.00% non-core manpower, −5% resistance target, +0.25 counter intelligence; if civil war occurs, Royal Police supports your side with 2 extra divisions; Adul Aduldejajaras becomes available as political advisor and becomes a general |

## Military-Civilian Branching

Focuses that branch from both military and civilian wings, leading to the starting point of civil war paths.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| The King of the White Elephant | The Peoples Day OR Hold Military Parades | None | +10% democratic party popularity, +8% stability, +80 political power, −3% war support; unlocks propaganda campaign "The King of the White Elephant" at Sala Chaloem Thai Movie Theater for +0.45% weekly stability for 180 days |
| Drum Up Irredentism | Embed Technocrats in Civilian Institutions OR Military Academies Indoctrination | None | Can send volunteer forces; gains "Thai Irredentism" national spirit: −75.0% generate war goal tension limit, −100.0% send volunteers tension limit, +2 max volunteer force divisions, −25.0% justify war goal time, −15.0% annex cost, +5.00% war support, +0.02 daily fascism support; Luang Wichitwathakan available as fascist agitator advisor; increase military approval and decrease civilian approval |
| War Fervor | Drum Up Irredentism | None | Gains "War Fervor" national spirit: +0.50% weekly war support (increases until war is declared, then spirit is removed); if war support stays >95% without declaring war for too long, civil war starts; upon war declaration, gains "Blood-lusted Irredentism" for 90 days: +10.0% division attack, +10.00% breakthrough; unlocks "Urge Restraint" decision |
| Sell Privy Purse Lands | Military Academies Indoctrination OR Embed Technocrats in Civilian Institutions | None | Gains "Sold Privy Purse Lands" national spirit for 270 days: −15.0% consumer goods factories factor, +5.00% construction speed; if civil war does not occur, Field Marshal Phraya Phahon is embroiled in scandal (allowing bypass of fascism requirement for Phibuns Premiership) |

## Royalist-Military Civil War Route

Initiated by Support Songsuradets Military Clique and The Midnight Meeting. Leads to civil war between the regime and royalists. Ends with regency and monarchy choices.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| The Midnight Meeting | Support Songsuradets Military Clique | To Lay the Bait, Phibuns Premiership | Gains "An Uneasy Alliance" national spirit: +0.05 daily support for unaligned; sets fascism party name to "Khana Ratsadon - Military Wing", neutrality party name to "Royalists"; Plaek Phibunsongkhram becomes leader and will seize power (you must unseat him); +75% fascism party popularity, set ruling party to fascist; Songsuradet and other royalist generals will support civil war if you are loyal to them; unlock "Appeal for Support" decisions |
| Meet with King Prajadhipok | The Midnight Meeting | None | +10% neutrality party popularity; Sri Dharmathibhet becomes available as political advisor: +10% command power gain multiplier, −5% resistance target, +0.1 daily support for unaligned, −25% political advisor cost |
| Prajadhipok Audience with [ENG.GetLeader] | Meet with King Prajadhipok | Facilitate Prajadhipoks Move to Japan | Upon civil war: +1500 UK Basic Infantry Equipment, +250 UK Towed Artillery, +100 UK Basic Small Airframe (or +100 UK Fighter I if By Blood Alone not enabled) |
| Facilitate Prajadhipoks Move to Japan | Meet with King Prajadhipok | Prajadhipok Audience with [ENG.GetLeader] | Upon civil war: 3 Ranger divisions from Japan support your side |
| The Kings Gambit | Prajadhipok Audience with [ENG.GetLeader] OR Facilitate Prajadhipoks Move to Japan (requires >50% neutrality popularity, not in civil war) | None | Starts a fascist civil war; Songsuradet, Rangsit Prayurasakdi, and Prince Boworadej become non-aligned; current leader is retired; Prajadhipok becomes non-aligned leader; civil war support depends on various clique appeals and royalist support decisions; if appealed to rural cliques, gains "Rural Support" national spirit for 40 days (+15.0% non-combat out of supply penalties reduction, +168.0 supply grace) and unlocks Militias technology; if appealed to industrialists, receives equipment stockpiles; if appealed to navy clique, fleet is transferred to royalists and Marines I technology is added |
| Restore Order | The Kings Gambit (requires not in civil war) | None | Gains "Restoring Order" national spirit for 1 year: −20.0% consumer goods factories factor, +10.00% construction speed, +50.00% free repair |
| To Forge a King | Restore Order (requires King Ananda ≥12 years old) | None | Unlocks event "To Forge A King" in 2-4 hours; can influence future studies of King Ananda until age 15; each study topic grants different bonuses when he ascends at age 15+ (Scholar topics: research speed bonuses; Military topics: division attack bonuses; Administrator topics: supply consumption reductions; Industry topics: construction speed bonuses) |
| Ascend the Throne | To Forge a King (requires King Ananda ≥15 years old) | None | Current leader is retired; Ananda Mahidol becomes non-aligned leader; receives traits based on what topics he studied (Scholar King: +10.00% research speed; Learned Prince: +5.00% research speed; Military Prodigy: +10.00% army organization regain, +15.0% division attack; etc.); production efficiency cap +10.00% |
| The Provincial Council of State | The Kings Gambit | None | Multiple political advisors become available: Damrong Rajanubhab (Royalist Reformer, construction +5.00%, research +4.00%, conscription/trade/economy law costs −25%), Paribatra Sukhumbandhu (Prince, +0.10 army/naval experience gain, +15.00% dockyard output), Wan Waithayakon (Ambassador, −5.0% consumer goods, +30.00% trade deal opinion, +0.1 daily democracy support), Dhani Nivat (Courtier, +15% political power gain, +5.00% stability), Rambai Barni (Queen Regent, +5.00% stability, +200 weekly manpower), Prince Boworadej (Bulldog, +10.00% war support, +0.1% weekly war support from bombing, +0.1 daily unaligned support) |
| The Regency of Boworadej | The Provincial Council of State (bypassed if Ananda Mahidol is leader) | The Regency of Rangsit, The Regency of Songsuradet | Retires current leader; Prince Boworadej becomes non-aligned leader with "The Absolutist Regent" trait: +10.0% division organization, −5.00% construction speed, +6.0% division attack, −5.00% research speed, −40.0% generate war goal tension limit, −30.0% justify war goal time |
| The Sacred Hierarchy | The Regency of Boworadej | None | Gains "The Sacred Hierarchy" national spirit: +1.00% recruitable population, −15.0% experienced soldier losses, −10.0% justify war goal time, +10% compliance growth speed |
| The Regency of Songsuradet | The Provincial Council of State (bypassed if Ananda Mahidol is leader) | The Regency of Boworadej, The Regency of Rangsit | Retires current leader; Phraya Songsuradet becomes non-aligned leader with "The Soldier Regent" trait: +10.00% army organization regain, −25.0% grant medal cost, +10% land doctrine mastery gain, +6.00% military factory construction speed |
| Order Discipline and Unity | The Regency of Songsuradet | None | Gains "Order, Discipline and Unity" national spirit: +10.0% division organization, +5.00% war support, +10% land doctrine mastery gain |
| The Regency of Rangsit | The Provincial Council of State (bypassed if Ananda Mahidol is leader) | The Regency of Boworadej, The Regency of Songsuradet | Retires current leader; Rangsit Prayurasakdi becomes non-aligned leader with "The Constitutionalist Regent" trait: +5.00% construction speed, +6.00% research speed, +5.00% stability |
| Constitutional Virtue | The Regency of Rangsit | None | Gains "Constitutional Virtue" national spirit: +10.00% research speed, +25% resistance growth speed in enemy-occupied states |
| An Absolute Monarchy | The Sacred Hierarchy OR Order Discipline and Unity | A Constitutional Monarchy | Gains "An Absolute Monarchy" national spirit: −6.0% division attrition, +1.00% recruitable population, −10.0% justify war goal time, +2.00% non-core manpower, +2.50% weekly stability; −60% stability, −5% war support, −10% neutrality popularity; if supported constitutional monarchists, additional −10% stability |
| A Constitutional Monarchy | Order Discipline and Unity OR Constitutional Virtue | An Absolute Monarchy | Gains "A Constitutional Monarchy" national spirit: +5% political power gain, +8.00% research speed, +10.00% stability, +0.15 daily democracy support; if supported absolutist monarchists, −10% stability, −5% war support, −15% neutrality popularity |

## Democratic Civil War Route

Initiated by Defenders of Constitutional Liberty and To Lay the Bait. The civilian government fabricates and leaks an economic reform plan to provoke the military into rebellion. Success depends on civilian support reaching Full Support and democratic popularity thresholds.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| To Lay the Bait | Defenders of Constitutional Liberty (requires >25% democratic popularity, has Civilian Wing Full Support or Slight Support) | The Midnight Meeting, Phibuns Premiership | Leaks forged radical draft to antagonize military; sets variable for predicting civil war support; the longer you delay "And Spring the Trap", the greater the backlash against the military and the stronger your support grows (military criticism increases democratic civil war support up to 75%, plus 25% from total democratic party popularity scaling); unlock event "siam_dem.1" in 1-2 hours |
| And Spring the Trap | To Lay the Bait (requires >50% democratic popularity, has Civilian Wing Full Support, not in civil war; AI requires >80% predicted support) | None | Closes the trap on the military conspiracy; if total predicted support >80%, avoids civil war and instantly deposes military (removes Khana Ratsadon, sets ruling party to democratic); otherwise starts fascist civil war with calculated support percentage; support scales from civilian wing approval events and total democratic party popularity (max 0.8 scaling factor) |
| The Purge | And Spring the Trap (requires not in civil war) | Military Oversight Bureau | Retires: Luang Chawengsaksongkhram, Mangkorn Phromyothi, Luang Haansongkhram, Phichit Kriangsakphichit, Jira Wichitsongkhram; gains "Purged Military" national spirit for 1 year: −15.0% leader experience gain, −15.0% division organization, −5.0% reinforce rate, −0.06 daily fascism support; after expiration, gains "Rehabilitated Military" (+10.0% leader experience gain, +10.0% division organization, +2.0% reinforce rate, −10.00% land doctrine cost) |
| Military Oversight Bureau | And Spring the Trap (requires not in civil war) | The Purge | Creates oversight system for military (details not fully covered on wiki); likely provides alternative military restructuring bonus |

## Government Form (Final Choice)

After civil war resolution, choose between absolute and constitutional monarchy.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| An Absolute Monarchy | The Sacred Hierarchy OR Order Discipline and Unity | A Constitutional Monarchy | National spirit: −6.0% division attrition, +1.00% recruitable population, −10.0% justify war goal time, +2.00% non-core manpower, +2.50% weekly stability; initial −60% stability, −5% war support, −10% neutrality popularity |
| A Constitutional Monarchy | Order Discipline and Unity OR Constitutional Virtue | An Absolute Monarchy | National spirit: +5% political power gain, +8.00% research speed, +10.00% stability, +0.15 daily democracy support |

## Other Focuses

Additional military-themed focuses available through the tree (not directly tied to the main civil war branches).

| Focus | Prerequisites | Effects |
|---|---|---|---|
| Phibuns Premiership | Not fully detailed in available data | Unlocked when Plaek Phibunsongkhram consolidates power through military/political maneuvers |

See [National Focus and Continuous Focus](../01-mechanics/national-focus.md) for generic/continuous focuses shared by all nations.
