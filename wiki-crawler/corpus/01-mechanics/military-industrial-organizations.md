---
title: Military Industrial Organizations
category: mechanics
tags: [mio, arms-against-tyranny, design-company, production, research, traits, policies]
game_version: "1.19"
dlc: [Arms Against Tyranny]
sources:
  - https://hoi4.paradoxwikis.com/Military_industrial_organization
---

## Summary

Military Industrial Organizations (MIOs) replace the base game's design companies when Arms Against Tyranny is active. A MIO can be attached to a production line, to a research task, and as the designer of an equipment variant; each task earns it **funds**, which raise its **size**, which grants **trait points**, and at size 6 unlocks **policies**. Unlike design companies, **several MIOs of the same category can be used simultaneously**, and a MIO producing a piece of equipment need not be the one that designed it. Industrial concerns are unchanged by the DLC.

## The three MIO tasks

| Task | Cost to the country | What the MIO gives | Funds earned |
|---|---|---|---|
| Assigned to a **production line** | **0 political power per day** (free) | Production bonuses from traits/policies (if any). Even with no bonuses the assignment still earns funds | **0.1 funds per production cost produced per day, capped at 100 funds/day** |
| Assigned to **research** a technology | **0.1 political power per day**, only while the tech is actively researching | Research speed bonus: **base +5%**, usually higher from starting traits, and raisable by traits, policies, political advisors and national focuses | **500 funds × (technology base cost / 110 days)**, paid on completion |
| Assigned as **designer** of equipment | Experience (see below) | Stat bonuses and sometimes maluses from traits/policies | – |

### Research funds detail

Funds on completing research = `500 × base cost / 110`:

| Technology base cost | Funds |
|---|---|
| 99 days | 450 |
| 110 days | 500 |
| 165 days | 750 |
| 220 days | 1000 |
| 275 days | 1250 |
| 330 days | 1500 |
| 550 days | 2500 |

- If research was already partly done before the MIO was attached, funds are **scaled to the fraction completed with the MIO assigned**.
- Funds depend only on **base** cost, not actual days spent — so researching technologies with big speed bonuses (especially naval and naval-support technologies that accept navy experience for a one-time bonus) is the fastest way to grow a MIO.
- **Researching ahead of time gives no extra funds**, so AOT research burns far more political power per fund gained.

Various political advisors, national focuses and MIO traits increase funds gained; some focuses add funds directly or raise a MIO's size outright.

### Designer assignment

- A MIO becomes the designer automatically for any equipment unlocked by a technology it researched.
- For other technologies, or to use a different MIO's bonuses, create a **new variant from the production screen**.
- MIOs can be attached to equipment variants and, where applicable, to armor designs (No Step Back), ship designs (Man the Guns) and aircraft designs (By Blood Alone).
- Adding, changing or re-applying a MIO designer costs army experience (land), navy experience (naval), or air experience (air). The cost can be discounted by some MIO traits and national focuses.
- **Newly unlocked trait/policy bonuses are not applied retroactively.** To benefit, re-apply the MIO to the variant (paying the experience cost again), switch production lines to the new variant, then **convert** existing land/air equipment or **refit** existing ships.
- A MIO assigned to a production line does **not** have to be the MIO that designed the equipment. Pairing a stat-focused designer MIO with a production-focused manufacturing MIO is a strong (if expensive) setup for important equipment.
- With Arms Against Tyranny, **MIOs cannot be attached to production lines of foreign (licensed/captured) equipment**, so those lines get no MIO bonuses and generate no funds or experience for a MIO.

> ⚠️ The wiki renders the political-power and experience define lookups for MIO assignment as `0` — production-line assignment at 0 PP/day appears genuine, but the experience cost for changing a research MIO or an equipment designer also shows as 0 in all four places, which is likely a broken `Defines` template rather than the real value. Verify in-game before planning around free designer swaps.

## Size and funds

Funds accumulate and raise the MIO's **size**. Each size increase grants **1 trait point**. **Policies unlock at size 6.**

```
Funds required for next size = 100 × (current size + 1)^1.8 + 700
```

| MIO size | Funds for next size | Cumulative funds to reach this size |
|---|---|---|
| 0 | 800 | 0 |
| 1 | 1048 | 800 |
| 2 | 1422 | 1848 |
| 3 | 1912 | 3270 |
| 4 | 2511 | 5182 |
| 5 | 3215 | 7693 |
| 6 | 4020 | 10908 |
| 7 | 4922 | 14928 |
| 8 | 5919 | 19850 |
| 9 | 7009 | 25769 |
| 10 | 8190 | 32778 |
| 11 | 9460 | 40968 |
| 12 | 10818 | 50428 |

## Categories and archetypes

MIOs fall into four categories — **Material Equipment, Planes, Ships, Tanks** — matching the old design company categories. Each MIO follows an **archetype**, which supplies most or all of its trait tree; in-game the archetype name is usually the MIO's descriptor. Many nations have unique traits layered onto the standard tree.

| Category | Archetypes |
|---|---|
| Material Equipment | Artillery Manufacturer; Infantry Weapons Manufacturer; Support Equipment Manufacturer; Automotive Manufacturer; Armored Car Designer; Helicopter Development |
| Planes | General Aircraft Designer; Light Aircraft Designer; Medium Aircraft Designer; Heavy Aircraft Designer; CAS Aircraft Designer; Naval Aircraft Designer; Multi-Role Aircraft Designer; High Agility Fighter Designer; Range Focused Aircraft Designer |
| Ships | Task Force Ship Builders; Battle Line Ship Builders; Escort Ship Builders; Raiding Ship Builders; Submarine Builders; Black Sea Fleet Designer; Refurbishment Repair Manufacturer |
| Tanks | Standardized Production; Infantry Tank Designer; Assault Guns Manufacturer; Fast Tank Designer; Medium Tank Designer; Heavy Tank Designer; Tank Refurbishment Plant; Light Armored Manufacturer |

### Archetype variants

Some MIOs carry a descriptor differing from their archetype, usually because they apply traits to additional or different equipment.

| Archetype | Variants |
|---|---|
| Infantry Weapons Manufacturer | Small Arms Manufacturer |
| Support Equipment Manufacturer | Ammunition and Weapons Works |
| Automotive Manufacturer | Fast Automotive Manufacturer; Attack Focused Automotive Manufacturer |
| Armored Car Designer | Minerva Imperia Armored Cars |
| Light Aircraft Designer | Standardized Production; Robust Light Aircraft Designer |
| Medium Aircraft Designer | Medium Long-Range Aircraft |
| CAS Aircraft Designer | Army Aircraft Manufacturer |
| Multi-Role Aircraft Designer | Aircraft Production Plant |
| Range Focused Aircraft Designer | Light Long-Range Aircraft |
| Task Force Ship Builders | Carrier Specialists |
| Escort Ship Builders | Merchant and Escort Ship Builders |
| Raiding Ship Builders | Carrier Focused Raiding Fleet; Coastal Defense Production |
| Submarine Builders | Advanced Submarine Designer |
| Standardized Production (tanks) | Dedicated Tank Factory |
| Infantry Tank Designer | Multi Role Tank Designer; Heavy Machinery Workshop |
| Fast Tank Designer | Mobile Tank Destroyers |
| Medium Tank Designer | Medium Tank Manufacturer |

## Traits

- Every MIO **starts with at least one always-on trait** that gives a bonus (or a penalty).
- Extra traits are bought with trait points earned from size increases. **Purchases cannot be undone.**
- A notification appears near the top of the screen whenever a MIO has an unspent trait point.
- The same MIO archetype in different countries usually shares starting traits and the basic tree, with country-unique traits grafted on.
- Traits can be **mutually exclusive** and can have **prerequisites** — usually other traits, sometimes technologies, and for country-specific traits often a completed national focus.
- **Shift-click** a trait icon to queue it instead of buying it. When the MIO gains trait points it automatically spends them on queued traits. The queue can be viewed and reordered from the trait queue button; dequeue with the X button or by shift-clicking the icon again.
- **Inferred:** it is often right to leave trait points unspent. Some traits carry maluses that outweigh their bonuses — infantry equipment MIOs are the classic case, where small breakthrough bonuses come with substantial production cost penalties.

## Policies

Unlocked at **MIO size 6**. Unlike traits, policies can be changed later.

- Assigning a new policy costs **25 political power**.
- **One policy active per MIO at a time.**
- A new policy can be chosen only after **at least 180 days** since the last policy assignment.
- Policies **cannot be queued**. Queuing 5 traits per MIO is a practical trick: any unspent-trait-point notification then belongs to a size-6+ MIO, reminding you to also pick a policy.

### All policies

| Policy | Effect | Availability |
|---|---|---|
| Ruthless Contracts | Funds gain +10% | All MIOs |
| Assembly Line Optimisers | All MIO equipment: production efficiency cap +5%; production efficiency growth +5% | Not available to ship-only MIOs |
| Vertical Integration | All MIO equipment: production resources need −10%; production resource penalty +10% | All MIOs |
| Mechanical Genius | All MIO equipment: reliability +10% | All MIOs |
| Experimental Development Team | MIO research bonus +20% | All MIOs |
| Permanent Industrial Revolution | MIO research bonus +10%; all MIO equipment production resource need −10% | Norway, after Norwegian Engineering |
| Ordnance Factory Board | All MIO equipment: production efficiency cap +10%; production efficiency growth +10%; reliability −10% | British Raj or its inheritors, after The Ordnance Factories Board |
| Armor Welding Specialists | All MIO equipment: armor +5% | Tank MIOs only |
| Casting Specialists | All MIO equipment: hardness +2% | Tank MIOs only |
| Heavy Gantry Cranes (land) | Train, Railway Artillery and Heavy Tank: production efficiency cap +5% each (and each is added to the MIO's supported equipment list) | Train and Tank MIOs only |
| Factory Applied Camouflage | All MIO equipment: defense +2%; breakthrough +2% | Tank MIOs specializing in medium and heavy chassis |
| Cutting Corners | All MIO equipment: production cost −10%; reliability −5%; soft attack −5%; hard attack −5%; armor −5% | Tank MIOs only |
| Welding Specialists | All MIO equipment: production cost −5% | Ship MIOs only |
| Space Efficient Design | Carrier deck size +1 (carrier added to supported equipment); all MIO equipment max range +25% | Ship MIOs only |
| Stable Gunnery Platforms | All MIO equipment: light battery hit chance factor +10%; heavy battery hit chance factor +10% | Ship MIOs only |
| Great Sea Keeping | All MIO equipment: weather penalty −50% | Ship MIOs only |
| Coastal Battlefleet | All MIO equipment: production cost −10%; max range −25% | Ship MIOs only |
| Perfect Finish | All MIO equipment: max speed +5%; production cost +5% | Plane MIOs only |
| Heavy Gantry Cranes (air) | All medium planes, strategic bombers and naval patrol bombers: production efficiency cap +10% each (each added to supported equipment) | Plane MIOs specializing in medium and large airframes |
| Propulsion Experimenters | MIO research bonus +20% | Plane MIOs only |
| Wind Tunnel Pioneers | All MIO equipment: agility +5% | Plane MIOs only |
| Modular Assembly | All MIO equipment: production cost −5% | Plane MIOs only |

Note that **Vertical Integration** and **Permanent Industrial Revolution** reduce strategic resource requirements for all MIO equipment; Vertical Integration also *increases* the penalty for lacking those resources.

## Per-country MIO lists

_Not covered here._ The wiki keeps them on separate pages: List of Tank MIOs, List of Ship MIOs, List of Plane MIOs, List of Material Equipment MIOs.

See also: [Production and equipment](production-and-equipment.md), [Research and technology](research-and-technology.md).
