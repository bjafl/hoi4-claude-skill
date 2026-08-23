---
title: New Zealand national focus tree
category: focus-trees
tags: [new-zealand, political, naval, air, industrial, army, commonwealth, independence]
game_version: "1.19"
dlc: []
sources:
  - https://hoi4.paradoxwikis.com/New_Zealand_national_focus_tree
---

## Summary

New Zealand has a unique focus tree with five branches: a political tree offering Commonwealth loyalty or independence paths (democratic/fascist/communist), naval expansion, air force development, industrial capacity building, and army modernization. The tree emphasizes colonial naval heritage, Pacific regional interests, and the option to pursue independence from the British Commonwealth while offering technology-sharing bonuses with allies.

See [New Zealand](../05-countries/new-zealand.md) for the country's 1936 starting profile. For generic/continuous focuses all nations may access, see [National Focus and Continuous Focus](../01-mechanics/national-focus.md).

## The First Labour Government branch

Political branch. Deals with internal governance, Commonwealth relations, and independence paths.

| Focus | Prerequisites | Mutually Exclusive | Effects |
|---|---|---|---|
| **The First Labour Government** | None | — | National spirit **First Labour Government**: consumer goods factories −2%, stability +5.00%, production efficiency growth +2.00%, factory output +2.00%, dockyard output +2.00% |
| **Ratana Alliance** | The First Labour Government | — | National spirit **Ratana Alliance**: daily political power cost +0.20, stability +5.00%, war support +5.00% |
| **Maori Affairs Act** | Ratana Alliance + controls Wellington (284) and Canterbury (723) | — | Wellington (284): +1 building slot; Canterbury (723): +1 building slot; stability −5.00% |
| **Social Security Act** | Ratana Alliance | — | National spirit **Social Security Act**: recruitable population +2.00%, stability +5.00%, war support +5.00% |
| **The Manpower Act** | Maori Affairs Act **or** Social Security Act | — | National spirit **The Manpower Act**: recruitable population factor +7% |
| **Amend the Maori Affairs Act** | The Manpower Act | Waitangi Tribunal | Wellington (284): +2 building slots; Canterbury (723): +2 building slots; stability −5.00% |
| **Maori Conscription** | Amend the Maori Affairs Act | — | National spirit **Maori Conscription**: recruitable population +1.00%, stability −5.00% |
| **Waitangi Tribunal** | The Manpower Act | Amend the Maori Affairs Act | National spirit **Waitangi Tribunal**: recruitable population +2.00%, consumer goods factories −2% |
| **Maori Volunteers** | Waitangi Tribunal | — | Unlocks decision to request control of Pacific Islands; creates Maori Volunteers unit in random state |
| **Strengthen the Commonwealth** | The First Labour Government | Statute of Westminster | Technology sharing bonus from Commonwealth +5%, political power +100; United Kingdom gets opinion bonus +25 (Strengthened Ties) |
| **2NZEF** | Strengthen the Commonwealth | — | National spirit **2NZEF**: send volunteers tension limit −50.0%, max volunteer force divisions +1, divisions required for sending volunteer force −100.0%; can send volunteer forces |
| **Arrest Pacifist Leaders** | 2NZEF | — | National spirit **Stomp Out Pacifism**: recruitable population factor +5%, foreign subversive activities efficiency −50%, stability −5.00%, war support +5.00% |
| **Technology Sharing With Britain** | Arrest Pacifist Leaders + United Kingdom same ruling party + United Kingdom in Commonwealth Research | — | Technology sharing bonus from Commonwealth +5% |
| **Statute of Westminster** | The First Labour Government + Britain has not enforced loyalty; requires Britain has not enforced loyalty | Strengthen the Commonwealth | Political power +120, autonomy +500.00 |
| **In the Darkness** | Statute of Westminster + Britain has not enforced loyalty | The Lee Affair, Constitution Amendment Act | Replaces **First Labour Government** with **In the Darkness**: daily autonomy progress +1.0, daily fascism support +0.01, construction speed +10.00%; removes **British Commonwealth Loyalty**; must be at peace with Japan, Japan fascist, fully independent |
| **Befriend Japan** | In the Darkness + at peace with Japan + Japan fascist + fully independent + Japan not enforced loyalty | Rule Them All | Japan gets event 'New Zealand wants to join our cause' |
| **Technology Sharing With Japan** | Befriend Japan + Japan fascist + in faction with Japan + fully independent | — | Japan joins Japanese Research technology sharing group with New Zealand |
| **Rule Them All** | In the Darkness + fully independent | Befriend Japan | Can create factions; if Australia is not fascist, gain annex war goal on Australia; otherwise political power +50 |
| **The Lee Affair** | Statute of Westminster + Britain has not enforced loyalty | In the Darkness, Constitution Amendment Act | Replaces **First Labour Government** with **The Worker's Party**: daily autonomy progress +1.0, daily communism support +0.02 |
| **Empower the Working Class** | The Lee Affair + fully independent + communist + not fighting on UK's side + Britain has not enforced loyalty | — | Political power +100; leaves Allies faction; becomes free; modifies **The Worker's Party**: daily autonomy progress +1.0, daily communism support +0.02, construction speed +10.00%; removes **British Commonwealth Loyalty** |
| **Join Comintern** | Empower the Working Class + fully independent + communist + Soviet Union communist + Soviet Union faction leader + at peace with Soviet Union + Britain has not enforced loyalty | — | Soviet Union gets event 'New Zealand requests Membership in the Comintern' |
| **Technology Sharing With Soviet Union** | Join Comintern + communist + Soviet Union communist + fully independent + in faction with Soviet Union | — | Soviet Union joins Comintern Research technology sharing group with New Zealand |
| **Constitution Amendment Act** | Statute of Westminster + any country not fighting on NZ's side and not in faction + Britain has not enforced loyalty | In the Darkness, The Lee Affair | Political power +70, autonomy +1000.00 |
| **Independent New Zealand** | Constitution Amendment Act + any country not fighting on NZ's side and not in faction + Britain has not enforced loyalty | — | Can create factions; leaves Allies faction; removes **British Commonwealth Loyalty** |

## Transfer the New Zealand Division branch

Naval branch. Develops navy, dockyards, and naval doctrine research.

| Focus | Prerequisites | Mutually Exclusive | Effects | Note |
|---|---|---|---|---|
| **Transfer the New Zealand Division** | None | — | United Kingdom transfers: Light cruiser HMS Achilles, Light cruiser HMS Leander | Bypassed if not UK subject |
| **Form the RNZN** | Transfer the New Zealand Division | — | Navy experience +25; naval engineering breakthrough +25.00%; naval doctrine cost reduction 2× 50% | Forms independent navy |
| **Expand Devonport Naval Base** | Form the RNZN | — | Random coastal state: +2 building slots, +2 naval dockyards; Wellington (284): +3 naval base in Auckland (4543) | Naval headquarters expansion |
| **Destroyer Effort** | Expand Devonport Naval Base | Submarine Effort | Destroyer models: −2.0 years AoT penalty, 1× 100% research bonus; next 1 research | |
| **Submarine Effort** | Expand Devonport Naval Base | Destroyer Effort | Submarine models: −2.0 years AoT penalty, 1× 100% research bonus; next 1 research | |
| **Light Cruiser Effort** | Destroyer Effort **or** Submarine Effort | — | Cruiser models: −2.0 years AoT penalty, 1× 100% research bonus; next 1 research | Mid-size capability |
| **Capital Ship Effort** | Destroyer Effort **or** Submarine Effort | — | Battleship and Carrier models: −2.0 years AoT penalty, 1× 100% research bonus; next 1 research | Major capital ships |
| **Purchase Destroyers and Submarines** | Form the RNZN | — | Unlocks decisions to purchase older ships from great powers | Expansion via trade |
| **Coastal Defense** | Form the RNZN | — | Wellington (284), Canterbury (723): +level 2 coastal forts; every naval base: +level 2 land fort, +level 2 coastal fort | Bypassed if doesn't control Wellington/Canterbury |

## Expand the NZPAF branch

Air research branch. Develops air force independence and aircraft research bonuses.

| Focus | Prerequisites | Mutually Exclusive | Effects | Note |
|---|---|---|---|---|
| **Expand the NZPAF** | None | — | If By Blood Alone enabled: adds 116× Bristol Blenheim tactical bomber; else 56× Fairey Swordfish naval bomber + 30× Armstrong Whitworth Whitley/Vickers Wellington tactical bomber; if Arms Against Tyranny enabled: equipment subsidy 1000 cost for Tactical Bomber from UK | Initial air equipment |
| **Form the RNZAF** | Expand the NZPAF | — | Air experience +25; aerodynamics/avionics breakthrough +25.00%; random state +2 air bases; air doctrine cost reduction 1× 50% | Independent air force |
| **Defend Our Islands** | Form the RNZAF **or** Coastal Defense | — | Naval aircraft: 2× 100% research bonus | Coastal defense focus |
| **Fighter Focus** | Form the RNZAF | Bomber Focus | Fighter models: 1× 100% research bonus | |
| **Bomber Focus** | Form the RNZAF | Fighter Focus | Strategic Bomber and Tactical Bomber models: 1× 100% research bonus | |
| **Modern Fighters** | Fighter Focus **or** Bomber Focus | Heavy Bombers | Fighter and Heavy Fighter models: 1× 100% research bonus | Advanced fighters |
| **Heavy Bombers** | Fighter Focus **or** Bomber Focus | Modern Fighters | Strategic Bomber models: 2× 100% research bonus | Strategic capability |
| **British Commonwealth Air Training Plan** | Modern Fighters **or** Heavy Bombers + ally of UK | — | National spirit **The Plan**: ace generation chance +10.00%; fighters air range +10%, air attack +5%; CV fighters air range +10%, air attack +5%; CAS air range +10%, ground attack +5%; CV CAS air range +10%, ground attack +5%; CV NAV bombers air range +10%, naval attack +5%; NAV bombers air range +10%, naval attack +5%; tactical bombers air range +10%, ground attack +5%; heavy fighters air range +10%, air attack +5%; strategic bombers air range +10%, strategic bombing +5%; transport planes air range +10% | Commonwealth training cooperation |

## Bureau of Industry/Ministry of Public Works branch

Industrial branch. Develops civilian/military factories, resource extraction, and infrastructure.

| Focus | Prerequisites | Mutually Exclusive | Effects | Note |
|---|---|---|---|---|
| **Bureau of Industry** | None | — | Random state: +2 building slots, +2 civilian factories | Agrarian economy development |
| **Wairarapa Sheep Farms** | Bureau of Industry | — | National spirit **Wairarapa Sheep Farms**: consumer goods factories −15.0%, industrial research speed +15%, coal gain efficiency +5%; random state (prioritize Canterbury/Wellington): +1 building slot, +1 civilian factory; available as industrial concern; coal +6 | Wool industry focus |
| **Utilize the Meat Industry** | Wairarapa Sheep Farms + at war + in faction | — | +1 offmap civilian factory; every ally +1 offmap civilian factory | Supply lines support |
| **Restart the Onekaka Ironworks** | Bureau of Industry + controls Marlborough (1080) | — | Marlborough (1080): +6 steel production | Domestic steel production |
| **Recycling Campaign** | Restart the Onekaka Ironworks + (at war **or** war support >50%) | — | Canterbury (723): +8 steel, +4 rubber production; synthetic resources: 1× 25% research bonus | Resource efficiency |
| **New Zealand Steel** | National Roads Board + ≥10 civilian factories + controls Wellington (284) and Auckland (1079) | — | Wellington (284): +10 steel; Auckland (1079): +4 steel production | Ironsand exploitation |
| **Department of Scientific And Industrial Research** | New Zealand Steel | — | +1 research slot | Scientific capacity |
| **Project Seal** | Modern Fighters **or** Heavy Bombers **or** Department of Scientific And Industrial Research (any one) | — | If no atomic research: 1× 50% research bonus for Nuclear Technology, nuclear research breakthrough +50.00%; else nuclear research breakthrough +100.00% | Secret weapon research |
| **National Defense Institute** | Project Seal + fully independent | — | +1 research slot | Sovereign research | 
| **Ministry of Public Works** | None | — | Dynamic modifier **Ministry of Public Works**: stability +5.00%, consumer goods factories factor −5.0%, infrastructure construction speed +10.00%, civilian factory construction speed +10.00%, railway construction speed +10.00%, synthetic refinery construction speed +10.00%; available as political advisor Bob Semple | National coordination |
| **Women in the Workforce** | Bureau of Industry + Ministry of Public Works + at war | — | Modifies **Ministry of Public Works**: recruitable population factor +15.0% | Wartime labor |
| **Taranaki Oil** | Bureau of Industry + Ministry of Public Works + controls Wellington (284) | — | Wellington (284): +8 oil production | North Island petroleum |
| **National Roads Board** | Ministry of Public Works | — | Random state (prioritize Wellington): +1 infrastructure; random state (prioritize Canterbury): +1 infrastructure; random state (prioritize Auckland): +1 infrastructure | Highway system |
| **Invest in Vehicle Assembly Plants** | Restart the Onekaka Ironworks + National Roads Board | — | 1× 50% research bonus for Truck; random state (prioritize Wellington/Canterbury): +2 building slots, +2 civilian factories | Vehicle production |
| **National Broadcasting Service** | National Roads Board | — | 1× 50% research bonus for Electronics | Communications infrastructure |
| **Abolish the Railways Board** | Ministry of Public Works | — | Removes **The Government Railways Board**; political power +100; available as industrial concern New Zealand Railways; train production cost −25.00%, armor +15%; supply hub/railway construction speed +15.00% | Railway modernization |
| **Locomotive Standardization** | Abolish the Railways Board | — | If no Civilian Train tech: gain Civilian Train; else 1× 50% research bonus for Trains and Railways; +40 NZR J class | Standard locomotives |
| **Direct the Coal Industry** | Ministry of Public Works + controls Canterbury (723), Wellington (284), Marlborough (1080) | — | Canterbury (723): +3 coal; Wellington (284): +3 coal; Marlborough (1080): +3 coal production | Coal coordination |
| **Establish the National Coal Board** | Direct the Coal Industry | — | Current ruling party popularity +10.00%; national spirit **National Coal Board**: stability −10.00%, coal gain efficiency +15% | Centralized control |
| **Full Employment** | New Zealand Steel + Invest in Vehicle Assembly Plants + Locomotive Standardization + Direct the Coal Industry | — | Removes **The Great Depression**; random state (prioritize Wellington/Canterbury): +2 building slots, +2 civilian factories; random state: +2 building slots, +2 military factories | Depression recovery |
| **Think Big** | Full Employment + Domestic Arms Industry | — | Random state: +2 building slots, +2 civilian factories; random state: +2 building slots, +2 military factories | Industrial ambition |
| **Expand the University of Auckland** | Department of Scientific And Industrial Research + Think Big | — | +1 research slot | Higher education |
| **Expand Power Generation** | Ministry of Public Works + controls/owns Auckland (1079) | — | Auckland (1079): +1 dam; dam state modifiers: max factories +15%, local energy consumption −65%, local resources +10%, construction speed +15%; unlocks decisions Mangahao Power Scheme and Waitaki Power Station | Hydroelectric expansion |

## Army Reforms branch

Army branch. Develops infantry weapons, domestic arms production, and armor research.

| Focus | Prerequisites | Mutually Exclusive | Effects | Note |
|---|---|---|---|---|
| **Army Reforms** | None | — | Army experience +25; land doctrine cost reduction 1× 50% | Military modernization |
| **Charlton Automatic Rifle** | Army Reforms | — | Infantry Weapons: 1× 100% research bonus | Domestic innovation |
| **Domestic Arms Industry** | Charlton Automatic Rifle | — | Random state: +2 building slots, +2 military factories | Small arms production |
| **Long Range Patrol** | Domestic Arms Industry | — | Marine technology: 2× 100% research bonus | Special ops development |
| **Bob Semple Tank** | Army Reforms | — | Land warfare breakthrough +10.00%; national spirit **Bob Semple Tank**: division organization +2.0%, division defense on core territory +5.0%; if No Step Back enabled: 1× 100% research bonus for Basic Light Tank Chassis; else 1× 100% research bonus for Bob Semple "Tank" | Light tank prototype | Bypassed if Bob Semple or Basic Light Tank already researched |
| **Schofield Tank** | Bob Semple Tank | — | Land warfare breakthrough +15.00%; Light Tank models: 1× 100% research bonus | Improved design |
| **Artillery Focus** | Schofield Tank | — | Land warfare breakthrough +25.00%; Support Artillery: 1× 100% research bonus | Support weapons |
| **Big Bob Tank** | Artillery Focus | — | Land warfare breakthrough +25.00%; if No Step Back enabled: Big Bob super heavy tank −2.0 years AoT + 1× 100% research bonus; else Big Bob super heavy tank chassis −2.0 years AoT + 1× 100% research bonus | Super-heavy armor |
| **Research Collaboration** | Big Bob Tank + Think Big + fully independent + at war + in faction + (>50 factories **or** any faction member >50 factories) | — | +1 research slot | Wartime cooperation |

## DLC and Equipment Notes

- **By Blood Alone:** If enabled, **Expand the NZPAF** adds 116× Bristol Blenheim instead of Fairey Swordfish/Armstrong Whitworth; **Bob Semple Tank** grants Basic Light Tank Chassis research.
- **Arms Against Tyranny:** If enabled, **Expand the NZPAF** adds equipment subsidy (cost 1000) for Tactical Bomber from UK.
- **No Step Back:** Affects tank research options in **Bob Semple Tank** and **Big Bob Tank**.
