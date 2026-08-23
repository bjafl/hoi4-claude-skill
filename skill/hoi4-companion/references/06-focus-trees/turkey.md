---
title: Turkish National Focus Tree
category: focus-trees
tags: [turkey, national focus, montreux convention, political, military, hava okulu]
game_version: "1.19"
dlc: [Battle for the Bosporus]
sources:
  - https://hoi4.paradoxwikis.com/Turkish_national_focus_tree
---

## Summary

Turkey's unique focus tree (requires Battle for the Bosporus) comprises two main branches: the Montreux Convention Branch handles Turkey's internal politics and foreign alignment, whilst the Learning From the Great War / Hava Okulu Branch covers military modernization and defensive infrastructure. Without the DLC, Turkey uses the generic focus tree. A joint Saadabad Pact branch is shared with Afghanistan, Iraq, and Iran (when Graveyard of Empires is enabled).

See [Turkey](../05-countries/turkey.md) for the country's 1936 starting profile.

## Montreux Convention Branch

Turkey's political branch, covering economic policy, democratization, and regime type selection.

### Root Focuses

| Focus | Prerequisites | Duration | Effects |
|---|---|---|---|
| **The Montreux Convention** | Fully independent | Bypass if Edirne (341), Istanbul (797), or Bursa (340) are not demilitarized | Political power +0; UK gains event "The Montreux Convention"; Turkey signals remilitarization of Dardanelles & Bosporus Strait |
| **Fully Integrate the İş Bank** | The Montreux Convention; Mutually exclusive with "Continue the Policy of Etatism"; ruling party Non-Aligned | — | Political power +120; gain Celâl Bayar (PM): daily PP +0.05, trade opinion +15%; change law to Free Trade: construction speed +15%, research speed +10%, factory output +15%, dockyard output +15%, resources to market +80%, civilian/navy intelligence +40% each. Sanayiciler industrial projects cheaper. |
| **Continue the Policy of Etatism** | The Montreux Convention; Mutually exclusive with "Fully Integrate the İş Bank"; ruling party Non-Aligned | — | National spirit Etatism: consumer goods factories −7%, infrastructure construction +10%, military factory construction +5%, civilian factory construction +15%, naval dockyard construction +5%. Gain İsmet İnönü (PM): stability +5%, factory output +5%, ideology drift defense +25%, civilian factory construction +5%. Sanayiciler projects more expensive. |
| **Millet Mektepleri** | Fully Integrate the İş Bank OR Continue the Policy of Etatism | — | Political power +50; remove national spirit "Widespread Illiteracy" if owned |
| **Ratify the Six Arrows** | Fully Integrate the İş Bank OR Continue the Policy of Etatism | — | Unlocks Law No. 3115 decisions |
| **Continue the Sümerbank Industrialization Scheme** | Fully Integrate the İş Bank OR Continue the Policy of Etatism | — | Industrial Concern: Sümerbank: consumer goods factories −10%, civilian factory construction +5%. Various state effects on Kastamonu, Izmir, Malatya, Kayseri depending on whether Birinci Beş Yıllık Sanayi Planı is active: adds building slots, civilian factories, or steel production. |
| **Revive Turkish Revolutionism** | Ratify the Six Arrows AND Continue the Policy of Etatism; Mutually exclusive with "Peace at Home"; İsmet İnönü or Fevzi Çakmak is/was leader | — | War support +5%, stability −5%; unlocks decision "Revolutionism" |

### Privatize the Anadolu Agency Sub-branch

Democratic path enabling multi-party elections and liberal reform.

| Focus | Prerequisites | Duration | Effects |
|---|---|---|---|
| **Privatize the Anadolu Agency** | Fully Integrate the İş Bank AND Ratify the Six Arrows | — | Democracy popularity +7%, stability +5%; removes "Institute Press Censorship" decision |
| **Lift the Ban on Other Political Parties** | Privatize the Anadolu Agency | — | Democracy popularity +10%, war support +5% |
| **Hold Our First Multi-Party Election** | Lift the Ban on Other Political Parties; official opposition party organized | — | Triggers event "Election Day" |
| **Achieving Atatürk's Dream** | Hold Our First Multi-Party Election AND Utilize Foreign Capital | — | If Celâl Bayar is leader: stability +10%. If Adnan Menderes is leader: triggers Turkish Civil War if as leader; Fascist party renamed Çakmak Rejimi; Fevzi Çakmak becomes Fascist leader; PP +250; democracy popularity +10%. |
| **Expand Our Armaments** | Achieving Atatürk's Dream | — | Add 2× (1 building slot + 1 military factory to random state); national spirit Prepared Rearmament Scheme (180 days): military factory construction +15% |
| **Permit Regional Elections** | Achieving Atatürk's Dream | — | Unlocks occupation law "Reconciliation"; unlocks "Integrate Kurdish State" decisions; Traditionalists cease opposition; if has Sectarian Woes: replace with same spirit at −10% stability, −5% war support; otherwise remove it; Kemalist Officers lose 1 loyalty |
| **Privatize Our Infrastructure** | Expand Our Armaments OR Permit Regional Elections | — | Add 3× (1 building slot + 1 infrastructure to random state); national spirit Privatized Infrastructure (360 days): PP gain +25%, consumer goods −5%, infrastructure construction −10% |
| **Looking Outwards** | Privatize Our Infrastructure AND Peace in the World | — | If Adnan Menderes is leader: triggers Turkish Civil War, war support +20%; otherwise war support +10%, stability +5% |

### The Sanayiciler Sub-branch

Industrial focus unlocking foreign investment and Debt Council management; ruled party must not be Communist.

| Focus | Prerequisites | Duration | Effects |
|---|---|---|---|
| **The Sanayiciler** | Ratify the Six Arrows; not Communist | — | Unlocks decision "Sponsor Petrol Ofisi's Formation"; allows state to empower industrial class |
| **Cooperate with the Debt Council** | The Sanayiciler; not Communist | — | PP +120; if no Free Trade law: adopt Free Trade (construction +15%, research +10%, factory output +15%, dockyard output +15%, resources to market +80%); UK, France, Italy, USA improve relations +50; Debt Council TPDA becomes industrial concern: PP gain −0.05, resources to market +15%, industrial research +7% |
| **Utilize Foreign Capital** | Cooperate with the Debt Council | — | Gain 1 research slot; unlocks decision "Discuss Investment Possibilities with Turkey" (bonus scales with relations to European powers/USA) |

### Treaty of Saadabad Sub-branch

Saadabad Pact formation (only if Graveyard of Empires DLC not enabled); bypassed if Afghanistan, Iran, or Iraq do not exist or if Turkey is a subject.

| Focus | Prerequisites | Duration | Effects |
|---|---|---|---|
| **Treaty of Saadabad** | Ratify the Six Arrows; Graveyard of Empires DLC not enabled | Bypassed if relevant nations absent or Turkey is subject | If Afghanistan, Egypt, Iran, Iraq, or Syria exist and are not subjects: trigger event "The Saadabad Pact"; war support +5% |

### Assess Our Future Sub-branch

Neutrality-oriented path maintaining Kemalist principles; available if not led by Mustafa Kemal Atatürk and one of Achieving Atatürk's Dream, Peace at Home, Fatherland First!, or Halk ve Devlet is completed.

| Focus | Prerequisites | Duration | Effects |
|---|---|---|---|
| **Assess Our Future** | Ratify the Six Arrows; not led by Mustafa Kemal Atatürk; one of (Achieving Atatürk's Dream, Peace at Home, Fatherland First!, Halk ve Devlet) completed | — | Conditional national spirit "The Legacy of Atatürk": If completed Revive Turkish Revolutionism: stability −5% (failed legacy). If completed Peace at Home without Varlık Vergisi: PP gain +0.05, stability +5% (Kemalist continuity). If completed Peace at Home with Varlık Vergisi: stability −5% (failed legacy). If completed Fully Integrate the İş Bank without Adnan Menderes: PP gain +0.10, stability +15%, democracy support +0.02 (democratic fulfillment). If completed Fully Integrate the İş Bank with Adnan Menderes: stability −5% (failed legacy). |
| **The Hatay Issue** | Assess Our Future; Turkey owns Alexandretta (799) or focus bypasses | Bypasses if Turkey owns Alexandretta | If France owns Alexandretta: France gets event; if Syria owns Alexandretta (as French subject): France gets event; otherwise owning country gets event; war support +5% |
| **Peace in the World** | The Hatay Issue; not at war (focus bypasses if at war) | — | National spirit Kemalist Neutrality: stability +15%, war goal tension limit +100%, join faction tension limit +100%, lend-lease tension limit −25%, send volunteers tension limit +25%, justify war goal time +200%, AI faction desire −100. War support +5%. |

### Peace at Home / Reinvigorate Turkish Nationalism Sub-branch

Authoritarian/Kemalist path vs. ultra-nationalist (Fascist) path; requires Ratify the Six Arrows.

#### Peace at Home Path

| Focus | Prerequisites | Duration | Effects |
|---|---|---|---|
| **Peace at Home** | Ratify the Six Arrows; Mutually exclusive with "Revive Turkish Revolutionism"; İsmet İnönü is leader/advisor OR completed Fully Integrate the İş Bank | — | Stability +10%; unlocks decisions "Initiate Counter-Fundamentalist Operation" and "Offer Conscription Exemptions to Kurdish Groups" |
| **Turkish State Railways** | Peace at Home | — | Industrial Concern: Türkiye Cumhuriyeti Devlet Demiryolları (Linchpin of Infrastructure): industrial research +15%, factory repair +20%, infrastructure construction +15%. Every state with Kemalist Loyalties: +1 infrastructure; every state with Kurdistan core: +2 infrastructure. |
| **The Second Five Year Plan** | Turkish State Railways OR Reinvigorate Turkish Nationalism; İsmet İnönü or Fevzi Çakmak is advisor | — | Remove Birinci Beş Yıllık Sanayi Planı if active. Conditional national spirit (1825 days): If İnönü's Five Year Plan (İnönü leader/advisor): infrastructure +5%, civilian factory +5%. If Çakmak's Five Year Plan (Çakmak leader/advisor): infrastructure +5%, military factory +5%. |
| **The Guardians of Kemalism** | Turkish State Railways AND The Second Five Year Plan | — | War support +5%; assigns state flags TUR_kemalist_state_to_target_1/2; sets random states with TUR_ideological_battleground_state without kemalist_loyalties to receive kemalist_loyalties modifier; Kemalist Officers loyalty set to 3 (highest); Kemalist Officers gain 2 power. Unlocks decision "Entrench Kemalism in State". |
| **Türk Ulusu** | The Hatay Issue; The Guardians of Kemalism OR İnanç Vergisi | — | War support +10%; pacifies Kurdish rebels in owned states with Kurdish agitation/separatism/rebellion |
| **İnanç Vergisi** (Faith Tax - Alternate: Varlık Vergisi / Wealth Tax) | The Guardians of Kemalism OR The Sun Language Theory | — | Conditional national spirit (180 days based on leader): If not Mustafa Kemal Atatürk, Mehmet Recep Peker, or Şevket Süreyya Aydemir: spirit Varlık Vergisi (Wealth Tax): PP gain +15%, manpower −300/week, consumer goods −7%, stability −25%. Unlocks decisions "Repeal the Wealth Tax". Otherwise: spirit İnanç Vergisi (Faith Tax): PP gain +25%, consumer goods −10%, stability −1/week, war support −0.5/week. Unlocks decisions "Repeal the Faith Tax". |
| **Reinvigorate Turkish Nationalism** | Revive Turkish Revolutionism; Mutually exclusive with "Rehabilitate the Kadro Movement" | — | If has İsmet İnönü advisor & not Fevzi Çakmak (Chief of Army): remove İnönü; gain Fevzi Çakmak (PM): mobilization +15%, war support +5%, command power +10%. If has Celâl Bayar advisor (same logic): similar replacement. Otherwise gain Fevzi Çakmak bonus. Quells Traditionalist opposition; increases Kurdish resistance in states with Kurdish insurgency. |

### Rehabilitate the Kadro Movement Sub-branch

Communist/Fascist path; mutually exclusive with Reinvigorate Turkish Nationalism.

| Focus | Prerequisites | Duration | Effects |
|---|---|---|---|
| **Rehabilitate the Kadro Movement** | Revive Turkish Revolutionism; Mutually exclusive with "Reinvigorate Turkish Nationalism" | — | Communist party renamed Cumhuriyet Halk Partisi; Şevket Süreyya Aydemir becomes Communist leader. Grants academic perks & national spirit Political Landscape Shifting (180 days): stability −0.2/week, communism support +0.05/day, fascism support +0.05/day. Consumer goods −3%, production efficiency +5%, factory output +5%. PP gain +10%. |

## Learning From the Great War / Hava Okulu Branch

Military modernization and defensive infrastructure; two parallel starting paths (Hava Okulu for air focus, Learning from the Great War for army focus).

### Root & Modernization

| Focus | Prerequisites | Duration | Effects |
|---|---|---|---|
| **Learning from the Great War** | None | — | Army experience +10. If not completed "Hava Okulu": unlocks decisions "Reforming Our Armed Forces". |
| **Hava Okulu** | None | — | Air experience +5. Available as political advisor: Sabiha Gökçen (Tactical Bombing Genius): ground support +20%. If not completed "Learning from the Great War": unlocks decisions "Reforming Our Armed Forces". |
| **Modernizing the Army** | Learning from the Great War | — | 2× 50% cost reduction for Land Doctrine. Unlocks decisions "Modernize Our Tactics" and "Commence Overhaul of Our Training Methods". |

### Army Modernization Branches

| Focus | Prerequisites | Duration | Effects |
|---|---|---|---|
| **Mechanizing Our Army** | Modernizing the Army; Mutually exclusive with "Embrace Military Tradition" | — | 1× 200% research bonus for Motorized; 2× 300% research bonus for Support technology |
| **The Kırıkkale Tank** | Mechanizing Our Army | — | Ankara (49): +2 building slots, +2 military factories. 1× 100% research bonus for Light Tank models. |
| **Embrace Military Tradition** | Modernizing the Army; Mutually exclusive with "Mechanizing Our Army" | — | 1× 200% research bonus for Support technology; 1× 150% research bonus for Reconaissance technology |
| **Utilizing Our Terrain** | Embrace Military Tradition | — | 2× 100% research bonus for Mountain Infantry I & II; 1× 100% research bonus for Engineers Technology |
| **Superiority of Arms** | Mechanizing Our Army OR Embrace Military Tradition | — | 2× 150% research bonus for Support Artillery |
| **Construct the Çakmak Line** | Superiority of Arms | — | Edirne (341): +3 land forts; +4 land forts; +3 land forts (3 separate province allocations). Defensive line protecting Bosporus Straits. |

### Air Force Branches

| Focus | Prerequisites | Duration | Effects |
|---|---|---|---|
| **Expand the Air Bases** | Hava Okulu | — | Trabzon (354): +2 air bases; Ankara (49): +2 air bases; Malatya (344): +2 air bases; Ankara (49): +3 air bases (5 total in Ankara). Unlocks decisions "Instruct the Proper Use of Modern Infrastructure" and "Legalize New Aircraft Safety Regulations". |
| **Accelerate Native Fighter Designs** | Expand the Air Bases | — | 1× 150% research bonus for Fighter models |
| **Patrol the Seas** | Accelerate Native Fighter Designs; Mutually exclusive with "Invoke the Methods of Mehmed II" | — | 1× 150% research bonus for Naval Bomber models; 2× 50% cost reduction for Air Doctrine |
| **Invoke the Methods of Mehmed II** | Accelerate Native Fighter Designs; Mutually exclusive with "Patrol the Seas" | — | 1× 150% research bonus for Tactical Bomber models; 1× 50% cost reduction for Air Doctrine |
| **Turkish Air Defense Platforms** | Patrol the Seas OR Invoke the Methods of Mehmed II | — | Istanbul (797): +3 air bases; Trabzon (354): +2 air bases; Bursa (340): +2 air bases; 1× 25% cost reduction for Air Doctrine |

### Naval Expansion

| Focus | Prerequisites | Duration | Effects |
|---|---|---|---|
| **Expand the Gölcük Naval Base** | Modernizing the Army AND Expand the Air Bases | — | Bursa (340): +1 building slot, +1 naval dockyard, +2 naval bases, +2 infrastructure. Unlocks decision "Streamline Communication Methods Between Ships". |
| **Relocate from Yıldız Palace** | Expand the Gölcük Naval Base | — | Edirne (341): +1 building slot, +1 naval dockyard. Mersin (345): +2 building slots, +2 naval dockyards, +4 naval bases, +2 infrastructure. Expands Port of Mersin. |
| **The Legacy of the Osmanlı Donanması** | Relocate from Yıldız Palace; Mutually exclusive with "The Path of the Wolf" | — | 1× 150% research bonus for Light Cruiser models; 1× 175% research bonus for Battleship models. Honors Ottoman naval legacy with modern fleet. |
| **The Path of the Wolf** | Relocate from Yıldız Palace; Mutually exclusive with "The Legacy of the Osmanlı Donanması" | — | 1× 100% research bonus for Submarine models; 2× 35% cost reduction for Trade Interdiction Doctrines. Emphasizes wolf-pack submarine tactics. |

### Final Defensive Integration

| Focus | Prerequisites | Duration | Effects |
|---|---|---|---|
| **Fortified Defensive Bases** | Construct the Çakmak Line AND Turkish Air Defense Platforms AND (The Legacy of the Osmanlı Donanması OR The Path of the Wolf) | — | Aerodynamics & Avionics breakthrough +75%; 1× 100% research bonus for RADAR. National spirit Emergency Deployment of Defensive Bases (720 days): air base construction +15%, land fort construction +30%, coastal fort construction +30%, anti-air construction +30%, radar station construction +15%. |
| **Türk Silahlı Kuvvetleri** | Fortified Defensive Bases | — | War support +15%. Remove national spirit "Disorganized Armed Forces" if owned. Otherwise: manpower +125,000. Represents fully modernized armed forces. |

## Notes on Alternate Branches & DLC Interactions

- **Saadabad Pact:** The shared joint branch "The Saadabad Pact Branch" is available through a separate wiki page when Graveyard of Empires DLC is enabled, replacing the Treaty of Saadabad focus and enabling the "Saadabad Pact Requested" route instead.
- **Without Battle for the Bosporus:** Turkey falls back to the generic national focus tree.
- **Civil War Risk:** The "Turkish Civil War" can trigger if Adnan Menderes leads and selects "Looking Outwards" after democratization, reflecting historical political tension.

## See Also

See [National Focus and Continuous Focus](../01-mechanics/national-focus.md) for generic/continuous focuses shared by all nations.
