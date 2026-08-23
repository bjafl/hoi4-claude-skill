---
title: Greek National Focus Tree
category: focus-trees
tags: [greece, national focus, battle for the bosporus, megali idea, metaxism, communist, democratic, fascist]
game_version: "1.19"
dlc: [Battle for the Bosporus]
sources:
  - https://hoi4.paradoxwikis.com/Greek_national_focus_tree
---

## Summary

Greece's unique national focus tree (requires Battle for the Bosporus DLC) reflects four decades of political turmoil and competing ideologies. The tree spans four main branches—ideological consolidation, monarchism, economic stabilization, and military expansion—with multiple sub-branches supporting Communist, Democratic, Byzantine-Fascist, and Metaxist paths. Key focus chains pursue the Megali Idea (Greek expansion into Turkey and the Balkans), economic ties to major powers, and military modernization.

See [Greece](../05-countries/greece.md) for the country's 1936 starting profile.

## Bring Home the Exiled Republicans Branch

The foundational Democratic-ideological branch, unlocked when Eleftherios Venizelos returns from exile, allowing Greece to adopt Democratic, Byzantine-Fascist, or Communist ideologies.

| Focus | Prerequisites | Mutually exclusive | Effect | Note |
|---|---|---|---|---|
| **Bring Home the Exiled Republicans** | None | The King's Government | +120 PP; +5.00% Democracy support; +3.00% Communism support; Romania loses guarantee on Greece; all Balkan Pact members lose the pact and gain -25 opinion. | Pivots Greece away from monarchism. |
| **Compromise with the Monarchists** | Bring Home the Exiled Republicans | Request Communist Support | +10.00% Stability; George II becomes constitutional monarch (+5.00% Stability); Monarchists friendly, Communists hostile. | Consolidates Democratic-Monarchist coalition. |
| **Remembering the Anatolian Catastrophe** | Compromise with the Monarchists | – | Gains national spirit Martyrs of the Anatolian Catastrophe (+10% manpower, +5.00% war support). | Justifies expansion into Turkey. |
| **Restoring Our Home** | Remembering the Anatolian Catastrophe; not completed Bolster the Schachtplan | – | Removes Schachtplan national spirit; if UK or France is Democratic, gains +15 opinion with both; Germany gains -50 opinion (or -100 if Greece's debt ≥ 2.5). | Breaks economic ties with Germany, courts Western Allies. |
| **Venerate the Ancient Hellenes** | Remembering the Anatolian Catastrophe | – | Gains national spirit Venerate the Ancient Hellenes (+5.00% Stability); +120 PP. | Unlocks cultural-themed focuses (Theban Warriors, Athenian Thinkers, Macedonian Generals). |
| **The Birthplace of Democracy** | Remembering the Anatolian Catastrophe; current ruling party is Democratic | – | +10.00% Stability; +5.00% Democracy popularity; modifies Political Instability national spirit (−5% PP gain but +5.00% construction speed). | Reinforces Democratic legitimacy. |
| **Theban Warriors** | Venerate the Ancient Hellenes | – | Modifies Venerate the Ancient Hellenes spirit: +5.00% Stability, +5.0% Division Defense on core territory; further upgrades add Research Speed +5.00% and Command Power +5%. | Progressive path emphasizing military cleverness. |
| **Athenian Thinkers** | Venerate the Ancient Hellenes | – | Modifies Venerate the Ancient Hellenes: +5.00% Stability, +5.00% Research Speed; further upgrades add Division Defense +5.0% and Command Power +5%. | Progressive path emphasizing science. |
| **Macedonian Generals** | Venerate the Ancient Hellenes | – | Modifies Venerate the Ancient Hellenes: +5.00% Stability, +5% Command Power; further upgrades add Division Defense +5.0% and Research Speed +5.00%. | Progressive path emphasizing command. |
| **The Anatolian Refugees** | One of: Theban Warriors, Athenian Thinkers, Macedonian Generals | – | +120 PP; triggers event Negotiations with the EEE. | Transitions to Megali Idea chain. |
| **Resurrecting the Megali Idea** | The Anatolian Refugees; one of: Turkey exists, Heraklion Convention failed, or Greece is fully independent | – (bypasses if all major powers + Turkey gone) | +10.00% War support; triggers event The Heraklion Convention; invitations to Megali Convention dispatched. | Launches the Megali Idea mega-goal. |
| **Horror and Fear** | Resurrecting the Megali Idea; fully independent; not Megali Idea Approved | The Gordian Knot | Greece declares war on Turkey. | Aggressive path: unilateral conquest. |
| **The Gordian Knot** | Resurrecting the Megali Idea; fully independent; Megali Idea Approved | Horror and Fear | +10.00% War support; all non-Italian signatories declare war on Turkey alongside Greece (bypasses if Turkey gone). | Diplomatic path: allies join the crusade. |
| **Reviving the Double-Headed Eagle** | Horror and Fear; current ruling party is Fascist | – | +5.00% War support; gains national spirit Reviving the Spirit of the Double-Headed Eagle (+10.00% War support, +15% PP gain); unlocks decision Revive Byzantium. | Transforms Megali Idea into Byzantine restoration. Requires Greece to pivot Fascist first. |
| **Phoideratoi** | Reviving the Double-Headed Eagle | – | Modifies Reviving the Spirit of the Double-Headed Eagle: +10.00% Non-core Manpower, +10.00% War support; if has Political Instability, replaces it with State of the Nation. | Recruits non-Greek populations into Byzantine military. |
| **Nenikikamen** | Horror and Fear or The Gordian Knot; controls Istanbul, Edirne, Izmit, Bursa, Izmir; Turkey gone/capitulated/subject; same ruling party as Greece | – | If Democratic: unlocks decision Form Greater Greece; replaces Martyrs of the Anatolian Catastrophe with The Megali Idea Triumphant (+5% manpower, +15.00% Stability, +5.00% War support). | Victory condition: Constantinople reconquered. |
| **The Die is Cast!** | Nenikikamen | – | +1 Research Slot; rule Can Create Factions enabled. | Transitions to post-victory imperial consolidation. |
| **Byzantine Themata** | Phoideratoi; The Die is Cast! | – | +10.00% War support; unlocks decisions Restore the Byzantine Empire. | Administers restored Byzantine territories. |

### Request Communist Support Sub-branch

Communist path, available as alternative to Compromise with the Monarchists.

| Focus | Prerequisites | Mutually exclusive | Effect | Note |
|---|---|---|---|---|
| **Request Communist Support** | Bring Home the Exiled Republicans | Compromise with the Monarchists | +5.00% Communism support; loses George II national spirit; Communists friendly, Monarchists hostile; Communist generals/ministers become available. | Pivots to Soviet-aligned communism. |
| **A Socialist Economy** | Request Communist Support | – | Gains national spirit Greek Socialism (+0.05 daily Communism support, +5.00% civilian factory construction speed). | Early-stage collectivization. |
| **Nationalized Banks** | A Socialist Economy | – | Modifies Greek Socialism: +5% PP gain; if has Schachtplan, replaces with Command Economy (−5.0% Consumer Goods, −15% Resources to Market); Germany gains -50 opinion. | Breaks German economic control. |
| **The Greek Industrial Revolution** | Nationalized Banks | – (bypasses if insufficient building slots) | +1 Research Slot; two random owned states each gain +2 building slots and +2 civilian factories. | Rapid industrialization via collectivization. |
| **Soviet Subsidized Railways** | A Socialist Economy; Soviet Union is Communist, at peace, controls Attica | – (bypasses if Soviet gone or non-Communist) | If Greece fully controls Peloponnese, Epirus, Central Macedonia: builds level-1 railways connecting them; builds railway from Central Macedonia to Thrace; unlocks decision Host Soviet Bureaucrats in the Kingdom of Greece. | Soviet economic integration. |
| **Red Militias** | Soviet Subsidized Railways | – | Gains national spirit Red Militias (+5% PP gain, +2.00% manpower, +0.10 daily Communism support). | Communist paramilitary organization. |
| **Agricultural Communes** | A Socialist Economy | – | If has Agrarian Society: replaces with Collectivised Agriculture (+38% manpower, −5.0% Consumer Goods, +30.00% factory output) plus 280-day Rural Exodus debuff; if has Industrializing Society: replaces and grants +2% manpower, +5.00% Stability for 280 days. | Collectivizes farming sector. |
| **Clearing Land for Industrial Expansion** | Agricultural Communes | – | Every owned cored state (except Aegean Islands, Crete) gains +1 building slot. | Clears farmland for factories. |
| **Depose the Reactionaries** | The Greek Industrial Revolution; Red Militias; Clearing Land for Industrial Expansion; fully independent | – (bypasses if already Communist) | KKE becomes ruling party; Dimitris Glinos available as political advisor (+5% PP gain, +0.10 daily Communism support); Communism support +15.00%; Political Instability replaced with State of the Nation; Republicans become inconsequential, Communists loyal. | Communist takeover. |
| **Prepare for the Great Anti-Fascist War** | Depose the Reactionaries; fully independent | Toe the Stalinist Line | Markos Vafiadis becomes leader (Guerilla Warfare Expert); replaces Red Militias with Red Army (+8.0% Division Recovery Rate); Political Instability becomes State of the Nation; Soviet Union gains -50 opinion as Greek Turncoats. | Anti-Stalinist communist path: independent Marxism. |
| **Ally Tito** | Prepare for the Great Anti-Fascist War; Yugoslavia exists, not puppet of Greece, fully independent | – (bypasses if Tito dead or already in faction with Greece) | Rule Can Create Factions; creates Balkan Federation of Socialist Republics (Corfu Cooperative); if Yugoslavia is Communist or has completed Recognize the Soviet Union, Yugoslavia receives event Greece invites Yugoslavia to Corfu Cooperative; otherwise receives event The Greeks Incite a Communist Rebellion in the South! | Balkan communist bloc formation. |
| **Secure the Aegean** | Ally Tito; Turkey has >30% Fascism or is Fascist; Turkey caused >5% world tension or is Fascist; fully independent | – (bypasses if owns Edirne, Bursa, Izmir, Antalya and Turkey gone/puppet) | Cores on Edirne; claims on Bursa, Izmir, Antalya, Dodecaneso; puppet (focus) war goal vs. Turkey; −5.00% War support. | Communist claim to Turkish territories. |
| **Dominate the Bulgarians** | Prepare for the Great Anti-Fascist War; Bulgaria exists, not puppet, fully independent | – (bypasses if Bulgaria gone or puppet) | Puppet (focus) war goal vs. Bulgaria. | Subjugates Bulgaria. |
| **Attack the Fascists** | Dominate the Bulgarians; fully independent | – | If Italy is Fascist: puppet (focus) war goal vs. Italy; if Germany is Fascist: puppet (focus) war goal vs. Germany; if Hungary is Fascist: puppet (focus) war goal vs. Hungary; if Yugoslavia is Fascist: puppet (focus) war goal vs. Yugoslavia; if Romania is Fascist: puppet (focus) war goal vs. Romania; replaces Greek Socialism with Greek Communism (+0.05 daily Communism, +10.00% infrastructure construction, +5.00% civilian factory construction). | Anti-fascist crusade. |
| **Toe the Stalinist Line** | Depose the Reactionaries; fully independent | Prepare for the Great Anti-Fascist War | Replaces Greek Socialism with Greek Stalinism (−5% PP gain, +10.00% War support, +5.00% infrastructure construction); hidden effect: becomes Union of Greek Soviet Republics; if Turkey exists/not allied/not allied with Soviets, Turkey receives event Communists Seize Power in Greece and gains -75 opinion (mutual strategic enemies with Greece). | Pro-Soviet communist path: subordinate to Stalin. |
| **Stage an Incident in the Bosporus** | Toe the Stalinist Line; fully independent; Soviet Union supported ambitions vs. Turkey | – | Triggers event The Bosporus Gamble; +5.00% War support. | Joint Soviet-Greek seizure of Bosporus. |
| **Revolutionaries of the South** | Toe the Stalinist Line | – | Replaces Red Militias with Red Enforcers (+4.0% Division Organization, +1.00% manpower); Political Instability becomes State of the Nation; rule Can Create Factions. | Maintains Greek independence from Soviet control. |

## The King's Government Branch

Monarchist branch, alternative to Bring Home the Exiled Republicans.

| Focus | Prerequisites | Mutually exclusive | Effect | Note |
|---|---|---|---|---|
| **The King's Government** | None | Bring Home the Exiled Republicans | +10.00% Stability (when focus is selected). | Establishes royal supremacy. |
| **The Right to Rule** | The King's Government | Metaxism | −15.00% Stability; +120 PP; triggers event The King Dissolves the Hellenic Parliament; abandons debts with France and Italy; civil war begins in Peloponnese, Thrace, Central Macedonia, Aegean Islands; Venezelists and Communists become rebellious. | Absolute monarchy path: triggers civil war. |
| **Reorganize the Royal Guard** | The Right to Rule | – | +2,500 manpower; creates 2 Greek units in random fully controlled owned cored states. | Military cadre mobilization. |
| **Petition the British for Aid!** | The Right to Rule; civil war over George II's Absolute rule has started | – (bypasses if UK gone/Communist/subject or Germany non-Aligned) | If UK not Communist: UK receives event The Monarchists in Greece Request Our Aid!; if Germany is Non-Aligned: Germany receives event The Monarchists in Greece Request Our Aid!; if Germany is Fascist: removes Schachtplan and Germany gains -50 opinion. | Calls in foreign powers to suppress rebellion. |
| **Utilize British Capital** | Petition the British for Aid!; at peace with UK; UK not Communist | – (bypasses if insufficient building slots) | +75 PP; Attica gains +1 building slot, +1 infrastructure, +1 civilian factory; all fully controlled owned cored states gain +1 building slot. | British economic reconstruction aid. |
| **Metaxism** | The King's Government | The Right to Rule | Ioannis Metaxas becomes leader (Arkhigos); Division Defense on core territory +5.0%; daily Democracy support −0.02; daily Communism support −0.02; Fascist Diplomacy acceptance +35; gains national spirit Metaxism (+5.00% Stability, tension limits boosted, +50.0% ideology drift defense); loses Political Instability, gains modified Political Instability (−5% PP gain but +5.00% construction speed). | Corporatist-authoritarian middle path. |
| **The Hellenic Spirit** | Metaxism | – | +120 PP; modifies Metaxism to Metaxism (2): +5.00% Stability, tension limits slightly reduced. | Nationalist-cultural consolidation. |
| **The National Youth Organisation** | The Hellenic Spirit | – | Gains national spirit The National Youth Organization (+10.00% War support, −10.00% training time, +0.01 daily Fascism support, +0.03 daily Non-Aligned support). | Youth mobilization, Fascist leaning. |
| **Crack Down on the Republicans** | Petition the British for Aid! or The National Youth Organisation | – | +10.00% Stability; unlocks decision Crush the Republicans. | Suppresses Venezelist opposition. |

### Use the Military Sub-branch

Non-aligned royal path balancing between Central Powers and Allies.

| Focus | Prerequisites | Mutually exclusive | Effect | Note |
|---|---|---|---|---|
| **Use the Military** | Crack Down on the Republicans | Recruit the Fascists | If has Political Instability: loses it, gains State of the Nation; two random owned controlled states each gain +1 building slot and +1 military factory (second state gains +2 slots and +2 factories). | Militarization via royal authority. |
| **Realign Ourselves with the Central Powers** | Use the Military; fully independent; George II is leader | Receive Schachtplan if applicable | Requires complex conditions (Götterdämmerung-dependent): Germany must complete Revive the Kaiserreich or be faction leader; Hungary must complete The Lands of the Crown of Saint Stephen or be faction leader; Austria-Hungary must be formed. If Germany completes Mitteleuropa/The Central Powers: Germany receives event Greece seeks to join the Central Powers; various faction-creation scenarios follow. | Central Powers alignment path. |
| **Reclaiming The Wayward Ally** | Realign Ourselves with the Central Powers; fully independent | – (bypasses if Turkey completed Pivot to the Past) | Puppet (focus) war goal vs. Turkey. | Targets Turkey on behalf of Central Powers. |
| **Our Traditional Allies in the Aegean** | Use the Military; fully independent | Realign Ourselves with the Central Powers | – (bypasses if already in faction with UK or Romania completed The Cordon Sanitaire) | If UK hasn't completed Concessions to the Trade Unions: UK receives event Greece seeks to join the Allies; if Romania completed The Cordon Sanitaire: Romania receives event Greece seeks to join the Cordon Sanitaire; otherwise +120 PP, +10.00% War support, and if hasn't completed reforms: loses Metaxism. | British/Allied alignment path. |
| **Achieving Enosis** | Our Traditional Allies in the Aegean | – (bypasses if Cyprus independent or UK doesn't own it) | If Cyprus exists: Cyprus receives event Greece Suggests Enosis; if UK owns Cyprus: UK receives event Greece Requests Enosis With Cyprus. | Union of Cyprus with Greece. |
| **Prepare Against the Mediterranean Threat** | Use the Military | – | If Metaxas is leader: builds Metaxas Line forts; otherwise builds Leonidas Line forts; gains national spirit Modernizing the Leonidas Line for 720 days (+30.00% land fort and coastal fort construction speed); adds level-1 and level-2 land forts to Epirus, Central Macedonia, Thrace. | Defensive fortification program. |
| **Securing the Bulgarian Menace** | Our Traditional Allies in the Aegean or Prepare Against the Mediterranean Threat; fully independent | – (bypasses if Bulgaria is Democratic) | Puppet (focus) war goal vs. Bulgaria (if not Democratic). | Secures Bulgarian alignment. |
| **Expansion of Athens University** | Reclaiming The Wayward Ally, Achieving Enosis, or Securing the Bulgarian Menace | – | +1 Research Slot. | Academic prestige-building. |
| **Protectors of the Mediterranean** | Expansion of Athens University | – | +120 PP; gains national spirit Defenders of the Mediterranean (Light Hull production cost −5.00%, Division Defense on core territory +5.0%). Central Powers variant: Champions of the Mediterranean (same bonuses, different flavor). | Mediterranean hegemonic role. |

### An Orthodox State Sub-branch

Orthodox-nationalist Metaxism enhancement path.

| Focus | Prerequisites | Mutually exclusive | Effect | Note |
|---|---|---|---|---|
| **An Orthodox State** | Use the Military or Recruit the Fascists; one of: Metaxas is leader + not in faction + has Metaxism, or George II is leader | – | Conditional effects: if hasn't completed The Right to Rule or Metaxism: gains An Orthodox State national spirit (+15% Stability, +15.00% War support, +5.0% Division Attack/Defense on core territory, −15% PP gain); if Metaxism completed: modifies Metaxism to Metaxism (3) (−15.0% Consumer Goods, +15.00% Stability, tension limits adjusted, +75.0% ideology drift defense); if The Right to Rule completed: gains An Orthodox State spirit. | Religious-nationalist consolidation. |
| **The Third Hellenic Civilization** | An Orthodox State; Metaxas is leader; not in faction; has Metaxism | – | Modifies Metaxism (3) to Metaxism (4): same modifiers, slightly reduced War support (+10.00%). | Ideological culmination: modern Hellenic supremacy. |
| **Defending Our Kingdom** | The Third Hellenic Civilization; Metaxas is leader; not in faction; has Metaxism | – | Modifies Metaxism (4) to Metaxism (5): adds +10.0% Division Defense on core territory. | Military-focused Metaxism. |
| **Reviving the Spartan Warrior Spirit** | Defending Our Kingdom; Metaxas is leader; not in faction; has Metaxism | – | Modifies Metaxism (5) to Metaxism (6): adds +15% recruitable population factor, +5.00% daily Non-Aligned support, +100.0% ideology drift defense. | Martial ultra-nationalism. |

### Recruit the Fascists Sub-branch

Fascist path, available as alternative to Use the Military.

| Focus | Prerequisites | Mutually exclusive | Effect | Note |
|---|---|---|---|---|
| **Recruit the Fascists** | Crack Down on the Republicans; The National Youth Organisation | Use the Military | +5.00% Fascism support; Fascist Faction becomes active and friendly; Romania cancels guarantee on Greece. | Opens fascist collaboration path. |
| **Following in the Footsteps of Giants** | Recruit the Fascists | – | +10.00% Fascism support; if Germany is Fascist: Germany gains +35 Fascist opinion; if Italy is Fascist: Italy gains +35 Fascist opinion; if has Metaxism (6): modifies to Metaxism (+15% recruitable population, +15% Stability, +15.00% War support, +10.0% Division Defense, +100.0% ideology drift defense, +0.05 daily Fascism support). | Accelerates Fascist consolidation. |
| **The Modern Movement** | Following in the Footsteps of Giants; >40% Fascism support | – | Triggers event The Grand Fascist Boulē of Halicarnassus; loses Political Instability, gains modified Political Instability (−5% PP gain but +5.00% construction speed). | Establishes fascist corporatist state. |
| **Hellenoturkism** | The Modern Movement; fully independent | Greece and Turkey Together in the Axis! | – (bypasses if Turkey in faction with Germany/Italy or puppet of Greece) | Turkey receives event Greece Suggests Joint Applications for Joining the Axis! | Greco-Turkish fascist alignment. |
| **Cement Greco-German Ties** | The Modern Movement; completed Bolster the Schachtplan | – (bypasses if no Schachtplan variant, Germany gone/Democratic/Communist) | Replaces Schachtplan with The Gotzamanis-Schachtplan (+5% PP gain, +10.00% Stability, +10% Resources to Market, −5.00% military factory construction speed, −15.00% civilian factory construction speed); +1 Research Slot. | German economic control becomes Greek partnership. |
| **Subjugating the Bulgarians** | Hellenoturkism; Cement Greco-German Ties; fully independent | – (bypasses if Bulgaria gone or puppet) | Annex war goal vs. Bulgaria. | Territorial expansion into Bulgaria. |
| **Greece and Turkey Together in the Axis!** | Subjugating the Bulgarians; fully independent; Greco-Turkish Friendship Pact signed | The Last Country Standing | – (bypasses if in faction) | If Germany not Fascist: Italy receives event Greece and Turkey Suggest a Strategic Partnership; if Germany Fascist: Germany receives event Greece and Turkey Apply for Axis Membership. | Axis membership with Turkish ally. |
| **The Last Country Standing** | Subjugating the Bulgarians; fully independent; not Greco-Turkish Friendship Pact signed | Greece and Turkey Together in the Axis! | +5.00% War support; Annex war goal vs. Turkey. | Unilateral Turkish conquest path. |
| **Molding the New World Order** | Greece and Turkey Together in the Axis! or The Last Country Standing | – | Loses Political Instability, gains State of the Nation; rule Can Create Factions; gains national spirit Security Batallions (−25% Resistance Decay Speed in occupied enemy territories, −25% Damage to Garrisons). | Authoritarian occupation regime. |

### The Four Year Plan Sub-branch

Economic management and foreign investment path.

| Focus | Prerequisites | Mutually exclusive | Effect | Note |
|---|---|---|---|---|
| **The Four Year Plan** | Metaxism; before 1938-01-01 | – (bypasses if after 1938-01-01) | Gains national spirit The Four Year Plan for duration scaled by selection date (1460 days if 1936–1937, 1095 days if 1937–1938): −10% PP gain, +5.00% infrastructure construction, +15.00% military factory construction, +25.00% civilian factory construction, +10.00% naval dockyard construction. | Corporatist industrial mobilization. |
| **Open Up the Country** | The Four Year Plan or Extracting More From Our Soil | – | Unlocks decisions Investment Schemes. | Invites foreign investment. |
| **Bolster the Schachtplan** | Open Up the Country; has Schachtplan; not German investment repudiated | British Docking Rights, Renegotiate Our Debt with France | – (bypasses if no Schachtplan or German investment repudiated) | Unlocks decision Exploit Errata in the Schachtplan; modifies Schachtplan: +5.0% Consumer Goods, −20% Resources to Market, +5.00% military factory construction, −25% Economy Laws cost, −25% Trade Laws cost. | Negotiates better German terms. |
| **Rapprochement with the Italians** | Bolster the Schachtplan; not Italian investment repudiated | – (bypasses if Italian investment repudiated) | Unlocks decision Request Assistance With Industrialization; if Arms Against Tyranny enabled: Fiat available as MIO (+2 Sizes). | Italian industrial partnership. |
| **British Docking Rights** | Open Up the Country; not British investment repudiated | Bolster the Schachtplan, Renegotiate Our Debt with France | – (bypasses if British investment repudiated) | Unlocks decision Trade Manufactured Ship Parts for Investment; enacts Docking Rights with UK. | British port access and trade. |
| **Renegotiate Our Debt with France** | Open Up the Country; not French investment repudiated | Bolster the Schachtplan, British Docking Rights | – (bypasses if French investment repudiated) | Unlocks decision Bribe French Trade Unions to Harass Their Government; voids any Debt to the I.F.C. held by France. | Debt forgiveness from France. |
| **Appeal to the Soviet Union** | British Docking Rights or Renegotiate Our Debt with France; not Soviet investment repudiated | – (bypasses if Soviet investment repudiated) | Unlocks decision Attend Talks With the Presidium; if Arms Against Tyranny enabled: Grabin Design Bureau available as MIO (+2 Sizes). | Soviet economic and military aid. |

## Devaluating the Drachma Branch

Economic and industrial development branch, open to all ideological paths.

| Focus | Prerequisites | Mutually exclusive | Effect | Note |
|---|---|---|---|---|
| **Devaluating the Drachma** | None | – | +120 PP; unlocks decisions Managing the Debt to the I.F.C. (allows downgrading and eventually eliminating the Debt to the I.F.C. national spirit). | Currency management and debt restructuring. |
| **Lignite Liquefaction** | Devaluating the Drachma | – | Random owned controlled state (prioritize Peloponnese) gains +1 building slot and +1 synthetic refinery; Public Petroleum Corporation available as industrial concern (+10% Synthetic Resources Research Speed, +15.00% Fuel Gain from Refineries). | Fuel self-sufficiency via coal liquefaction. |
| **Extracting More From Our Soil** | Lignite Liquefaction | – | Attica: +12 aluminum; Peloponnese: +8 aluminum, +15 steel, +5 tungsten; Aegean Islands: +21 aluminum, +9 steel. | Resource extraction programs. |
| **The Rich Macedonian Farmlands** | Extracting More From Our Soil; Central Macedonia fully controlled and cored | – | Gains national spirit The Macedonian Farmlands (−5.0% Division Attrition, −5.0% Consumer Goods Factories, +5% Supply Efficiency, +10% Supply Range, −10.0% Supply Combat Penalty on Core Territory). | Agrarian logistics optimization. |
| **Utilize Our Strengths** | Devaluating the Drachma | Force the Farmers into Factories | If has Agrarian Society: replaces with Farmer-Focused Culture (+5% PP gain, +30% recruitable population, −5.0% Consumer Goods, +10.00% Stability, +30.00% factory output); if has Collectivized Agriculture: replaces with 280-day Rural Exodus debuff (−25% PP gain, +5.00% infrastructure construction, +5.00% military factory construction, +15.00% civilian factory construction, +10.00% naval dockyard construction, −5.00% Stability). | Prioritizes agricultural exports over industrialization. |
| **Force the Farmers into Factories** | Devaluating the Drachma | Utilize Our Strengths | If has Agrarian Society: replaces with Industrializing Society (+38% recruitable population, +35.00% factory output, −15.00% Stability); if has Collectivized Agriculture: gains 280-day Rural Exodus debuff with variations (−25% PP gain, +5.00% infrastructure, +5.00% military factory, +15.00% civilian factory, +10.00% naval dockyard, −10.00% Stability). | Rapid industrialization through collectivization. |
| **Open Foreign Subsidized Factories** | Utilize Our Strengths | – (bypasses if major powers gone) | Gain +1 military factory and +1 civilian factory for each of: France, UK, Germany, Soviet Union (if opinion of Greece >80). | Foreign industrial investment. |
| **Paying Back Our Debts in Bulk** | Force the Farmers into Factories | – (bypasses if debt-free or defaulted or insufficient debt progress) | +5.00% Stability; unlocks decisions Large Debt Repayment to British/French/Italians. | Accelerates debt repayment. |
| **Connecting Our Prefectures** | Open Foreign Subsidized Factories; one of: full control of Peloponnese, Attica, or Epirus | – (bypasses if those states can't build more infrastructure) | +10.00% Stability; Attica, Peloponnese, Epirus each gain +1 infrastructure. | Transportation infrastructure. |
| **Exporting More Luxury Commodities** | Open Foreign Subsidized Factories | – | Modifies Foreign Monopolies: −5.0% Consumer Goods; changes Trade Law to Free Trade (+15.00% construction speed, +10.00% research speed, +15.00% factory output, +15.00% dockyard output, +80% Resources to Market, +40.0% Civilian/Navy Intelligence to others); +120 PP. | Luxury export economy. |
| **Greek Autarky** | Paying Back Our Debts in Bulk | – | Modifies Foreign Monopolies: −5.0% Consumer Goods; changes Trade Law to Limited Exports (+5.00% construction speed, +1.00% research speed, +5.00% factory/dockyard output, +25% Resources to Market, +10.0% Civilian Intelligence to others, +5.0% Navy Intelligence to others); +10.00% Stability. | Self-sufficient autarky model. |
| **Fiscal Responsibility** | Paying Back Our Debts in Bulk; one of: partially/fully paid off Debt to the I.F.C. or current ruling party is Communist | – (bypasses if defaulted or non-Communist with insufficient debt progress) | Conditional: if not Communist + <3 advisors: +120 PP, Emmanouil Tsouderos available (−5.0% Consumer Goods); if not Communist + <2 advisors: Tsouderos available; otherwise: +250 PP, +10.00% Stability. Communist variant: Widespread Wealth Redistribution. | Financial equilibrium and stability. |
| **Sophistry and Science** | Connecting Our Prefectures | – | Gains national spirit Sophistry and Science (+5% PP gain, +5.00% Research Speed). | Science and technological development. |
| **Expand Our Tobacco Industry** | Exporting More Luxury Commodities or Greek Autarky; fully independent | Increase Our Mining Operations | Modifies Foreign Monopolies: −5.0% Consumer Goods; Central Macedonia gains +3 building slots and +3 civilian factories; Thrace gains +1 building slot and +1 civilian factory; France, UK, Germany, USA each gain +25 opinion (Tobacco Exports). | Specializes in tobacco production. |
| **Increase Our Mining Operations** | Exporting More Luxury Commodities or Greek Autarky; fully independent | Expand Our Tobacco Industry | Modifies Foreign Monopolies: −5.0% Consumer Goods; Attica gains +2 building slots and +2 military factories; Epirus gains +1 building slot and +1 military factory; 2x 100% research bonus for Excavation Technologies. | Specializes in mineral extraction. |
| **The Bedrock of Balkan Financial Stability** | Fiscal Responsibility | – | +200 PP; receives off-map civilian factories based on opinion (>50) from Western Balkans, Eastern Balkans, Northern Balkans countries, plus Austria, Czechoslovakia, Turkey: Albania, Bulgaria, Hungary, Yugoslavia (1 each if >50 opinion); Austria, Romania, Turkey (2 each if >75); Czechoslovakia (3 if >85). | Regional financial supremacy. |
| **Encourage Tourism** | Expand Our Tobacco Industry or Increase Our Mining Operations | Mobilize the Economy | Modifies Foreign Monopolies: −5.0% Consumer Goods; +5.00% Stability; gains national spirit Booming Tourism Industry (+15% PP gain, −5.0% Consumer Goods, +10.00% Stability). **Warning: tourism lost upon entering war.** | Wartime risk to economy. |
| **Mobilize the Economy** | Expand Our Tobacco Industry or Increase Our Mining Operations; >20% War support | Encourage Tourism | Modifies Foreign Monopolies: −5.0% Consumer Goods; +5.00% War support; changes economy law conditional on current state (to Partial Mobilization or War Economy if not already at those levels, else +150 PP). | War economy transition. |
| **Rejuvenating Athens** | Encourage Tourism or Mobilize the Economy | Making Use of Our Islands, Clear the Slums | Attica gains +4 building slots, +2 civilian factories, +1 military factory. | Capital-focused development. |
| **Making Use of Our Islands** | Encourage Tourism or Mobilize the Economy | Rejuvenating Athens, Clear the Slums | If Aegean Islands fully controlled: +2 building slots, +1 naval dockyard; if Crete fully controlled: +3 building slots, +2 civilian factories; if Cyprus fully controlled: +3 building slots, +2 military factories; if Dodecaneso fully controlled: +1 building slot, +1 naval dockyard; cores Cyprus if owned but not cored. | Island development and Cypriot integration. |
| **Clear the Slums** | Encourage Tourism or Mobilize the Economy | Rejuvenating Athens, Making Use of Our Islands | Random states (prioritize Thrace, Central Macedonia, Peloponnese, Epirus) each gain building slots (2, 1, 1, 1 respectively); +66,750 manpower. | Slum clearance and labor mobilization. |
| **Cooperate with Foreign Monopolies** | Sophistry and Science; one of: Rejuvenating Athens, Making Use of Our Islands, Clear the Slums | Crack Down on Foreign Monopolies | +120 PP; replaces Foreign Monopolies with Cooperative Foreign Monopolies (−20.0% Consumer Goods, +5.00% Research Speed, +5.00% Trade deal opinion, −50% Economy Laws cost, −100% Trade Laws cost). | Accommodation with foreign capital. |
| **Crack Down on Foreign Monopolies** | The Bedrock of Balkan Financial Stability; one of: Rejuvenating Athens, Making Use of Our Islands, Clear the Slums | Cooperate with Foreign Monopolies | +5.00% Stability; removes Foreign Monopolies national spirit; if Arms Against Tyranny enabled: Biamax, Pyrkal, Petropoulos available as MIOs (each +1 Size). | Nationalistic economic independence. |
| **Academy of Athens** | Cooperate with Foreign Monopolies or Crack Down on Foreign Monopolies | – | +1 Research Slot. | Academic research hub. |

## Hellenic Armed Forces Branch

Military modernization and doctrine branch, available to all ideologies.

| Focus | Prerequisites | Mutually exclusive | Effect | Note |
|---|---|---|---|---|
| **Hellenic Armed Forces** | None | – | +30 Army experience, +30 Navy experience, +30 Air experience; unlocks Hellenic Academy Battleplans. | Military modernization launch point. |
| **The Hellenic Air Force** | Hellenic Armed Forces; one of: full control of Crete, Epirus, or Attica | – | +50 Air experience; Crete gains +4 air bases, Epirus gains +3, Attica gains +4. | Air force expansion. |
| **Destroying Our Foes** | The Hellenic Air Force | Protecting Our Skies | 2x 50% Air Doctrine cost reduction; +10.00% Mastery bonus for 240 days to all active Strategic Destruction tracks; 1x 100% research bonus for Strategic Bomber and Tactical Bomber models. | Strategic bombing doctrine. |
| **Escorts For Our Bombers** | Destroying Our Foes | – | 1x 25% Air Doctrine cost reduction; 1x 100% research bonus for Heavy Fighter models. | Fighter escort specialization. |
| **Protecting Our Skies** | The Hellenic Air Force | Destroying Our Foes | 2x 25% Air Doctrine cost reduction; +10.00% Mastery bonus for 240 days to all active Battlefield Support tracks; 1x 100% research bonus for Fighter models. | Air defense doctrine. |
| **Defending Our Seas** | Protecting Our Skies | – | 2x 50% Air Doctrine cost reduction; 1x 100% research bonus for Naval Bomber models. | Naval air support. |
| **Fund the Hellenic Air Force Academy** | Escorts For Our Bombers or Defending Our Seas | – | +10 Air experience; gains national spirit The Hellenic Air Force Academy (−5.00% Fighter production cost, +10.00% Ace Generation Chance, −10.00% Air Accidents Chance). | Pilot training professionalization. |
| **The Double-Headed Aquila** | Fund the Hellenic Air Force Academy; completed Reviving the Double-Headed Eagle; Byzantium restored | – | Reduces ahead-of-time penalty by 1.0 years; 100% research bonus for next 2 Fighter Models and Heavy Fighter Models researches. | Byzantine imperial air force. |
| **The Hellenic Army** | Hellenic Armed Forces | – | +15 Army experience; 2x 50% Land Doctrine cost reduction; 1x 100% research bonus for Engineers Technology. | Army modernization. |
| **The Backbone of the Army** | The Hellenic Army | – | 1x 50% Land Doctrine cost reduction; 1x 100% research bonus for Infantry Weapons; gains or modifies Hellenic Army national spirit (+0.20% recruitable population). | Conscription and equipment modernization. |
| **Embracing Modern Warfare** | The Backbone of the Army | New Weapons, Old Tricks | 1x 100% research bonus for Light Tank models; 1x 100% research bonus for Motorized. | Tank warfare adoption. |
| **Hellenic Armored Corp** | Embracing Modern Warfare | – | Reduces ahead-of-time penalty by 1.0 years; 100% research bonus for next 2 Light Tank Models and Medium Tank Models researches. | Armored divisions. |
| **A Legacy of War** | The Hellenic Army | – | 1x 50% Land Doctrine cost reduction; gains or modifies Hellenic Army national spirit (+10.0% Division Recovery Rate). | Historical military tradition. |
| **New Weapons, Old Tricks** | A Legacy of War | Embracing Modern Warfare | +10 Army experience; 1x 100% research bonus for Recon Company I/II/III; 2x 50% research bonus for Support Artillery. | Recon and artillery specialization. |
| **Greek Mechanization** | New Weapons, Old Tricks | – | 1x 100% research bonus for Mechanized models. | Mechanized infantry. |
| **A Land of Mountains** | Hellenic Armored Corp or Greek Mechanization | – | 2x 50% research bonus for Mountain Infantry I and II; enables Mountain Warfare Training for Infantry (+5% Mountains Defense/Movement), Marines (+5% Mountains Attack, +10% Movement), Mountaineers (+5% Attack/Defense, +10% Movement), Paratroopers (+5% Attack, +10% Movement). | Mountain combat specialization. |
| **Modern Cataphracts** | A Land of Mountains; completed Reviving the Double-Headed Eagle; Byzantium restored | – | 1x 100% research bonus for Mechanized Equipment I; reduces ahead-of-time penalty by 2.0 years; 50% research bonus for next 1 Heavy Tank Models research; replaces Hellenic Army national spirit with The Byzantine Army (+0.20% recruitable population, +5.0% Reinforce Rate). | Byzantine armored renaissance. |
| **The Hellenic Navy** | Hellenic Armed Forces | – | +15 Navy experience; two random owned controlled states gain +2 building slots and +2 naval dockyards; one random gains +1 building slot and +1 naval dockyard. | Naval expansion program. |
| **Scrap the Greco-Turkish Naval Treaty** | The Hellenic Navy | A Modern Navy | Aligning with UK or Germany allows rebuilding old heavy ships; Turkey gains -15 opinion (Aegean Troublemakers). | Battleship capital-ship doctrine. |
| **A Fleet Fit for the Aegean** | Scrap the Greco-Turkish Naval Treaty | – | 1x 100% research bonus for Battleship and Battlecruiser models; 2x 35% Naval Doctrine cost reduction. | Capital-ship focus. |
| **The Cannon** | A Fleet Fit for the Aegean | – | 1x 100% research bonus for Battleship models; 3x 50% research bonus for Ships. | Battleship gun specialization. |
| **A Long and Proud Tradition** | A Fleet Fit for the Aegean or Disrupting the Great Powers | – | +5.00% Stability; +20 Navy experience; gains national spirit Ancient Talents (−50.0% Navy Leader Cost, new leaders start +1 level, +2 Defense skill, +2 Maneuvering skill). | Maritime heritage excellence. |
| **Thema Nautikon** | A Long and Proud Tradition; completed Reviving the Double-Headed Eagle; Byzantium restored | – | 2x 35% Naval Doctrine cost reduction; 2x 100% research bonus for Battleship models. | Byzantine naval theme system. |
| **A Modern Navy** | The Hellenic Navy | Scrap the Greco-Turkish Naval Treaty | Gains 25.00% Naval Engineering breakthrough progress; gains national spirit Long Range Hunters (Cruiser Submarine Research Speed +100%, −10.00% Cruiser Submarine production cost); 1x 75% research bonus for Destroyer Models and Submarine Models. | Submarine-focused commerce raiding. |
| **Disrupting the Great Powers** | A Modern Navy | – | 1x 75% research bonus for Submarine Models; 2x 50% Naval Doctrine cost reduction. | Supply-line interdiction. |
| **The Torpedo** | Disrupting the Great Powers | – | 2x 50% research bonus for Submarine Models; 1x 100% research bonus for Ships. | Submarine torpedo specialization. |

> ⚠️ Broken wiki template reconstructed: The Bring Home the Exiled Republicans focus displays `[{{{1}}}]` icons representing government ideology labels; these are rendered as Democratic, Communist, and Byzantine options in-game.

## Footnote: Generic and Continuous Focuses

Greece uses the standard national focus mechanics (1 PP per day cost, 70-day standard duration). See [National Focus and Continuous Focus](../01-mechanics/national-focus.md) for generic focus tree branches (Army/Aviation/Naval/Industrial/Political Effort) and continuous focuses all nations can unlock after 10 completed focuses.

This Greek tree represents ~100+ unique focuses branching across ideological, economic, and military dimensions, with multiple endpoint scenarios reflecting the nation's historical political fragmentation and Balkans geopolitical positioning.
