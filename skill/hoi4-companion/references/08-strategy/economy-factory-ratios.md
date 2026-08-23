---
title: Military vs Civilian Factory Ratios
category: strategy
tags: [economy, production, military-factories, civilian-factories, construction, payback]
game_version: "1.19"
dlc: []
sources:
  - ../01-mechanics/production-and-equipment.md
  - ../01-mechanics/construction-and-buildings.md
  - ../01-mechanics/trade-resources-and-market.md
---

## Summary

The optimal military-to-civilian factory ratio depends on your game phase and war timeline. Early in the game, build civilian factories to develop your economy; later, shift production toward military factories. The payback time for a new civilian factory determines when to stop building them and fully commit to military output.

## Civilian factory payback and build timing

**Inferred:** The payback formula from the construction mechanics shows that a new civilian factory pays for itself through construction speed bonuses. Once this threshold is reached, that factory's output becomes effectively "free" — you should stop building new civilian factories and redirect all available construction capacity to military factories and war production.

Payback time (in days) for a state with infrastructure level *I* and construction speed modifier *S*:

```
Payback = 10800 / ( infrastructure_modifier(I) × 5 × (1 + S) × (1 − consumer_goods / 100) )
```

where `infrastructure_modifier = 1 + 0.2 × I` for levels 0–5.

**Example payback times** for Early Mobilization (30% consumer goods) with no construction speed bonus, at infrastructure level 4 (1.8× modifier):

| Economy law | 0% speed | +10% speed | +20% speed |
|---|---|---|---|
| Undisturbed Isolation (50% CG) | 1333 days | 1111 days | 952 days |
| Civilian Economy (35% CG) | 1143 days | 952 days | 815 days |
| Early Mobilization (30% CG) | 1067 days | 889 days | 762 days |
| Partial Mobilization (25% CG) | 1000 days | 833 days | 714 days |
| War Economy (20% CG) | 942 days | 786 days | 673 days |
| Total Mobilization (10% CG) | 889 days | 741 days | 635 days |

**Inferred:** If your payback time is 800 days and you plan to be ready for war by January 1944 (roughly 2555 days from game start in September 1936), the optimal switch time is:

```
Switch time = target time − (2 / ln 2) × payback time
            = 2555 − 2.885 × 800
            ≈ September 1937 (155 days into the game)
```

A payback time of 1000+ days suggests switching even earlier; a payback of 600–700 days allows building civilian factories deeper into the game (into 1938–1939).

## Consumer goods constraint

**Inferred:** The percentage of total factories consumed by consumer goods cannot be overlooked when calculating ratios. Consumer goods apply to *all* factories (military + civilian + naval dockyards), and this affects your true factory availability.

| Economy law | Consumer goods % | Free factories (at 60 total) | Example: 30 military factories |
|---|---|---|---|
| Undisturbed Isolation | 50% | 30 | 14 civilian, 16 remaining |
| Civilian Economy | 35% | 39 | 20 civilian, 19 remaining |
| Early Mobilization | 30% | 42 | 21 civilian, 21 remaining |
| Partial Mobilization | 25% | 45 | 22 civilian, 23 remaining |
| War Economy | 20% | 48 | 24 civilian, 24 remaining |
| Total Mobilization | 10% | 54 | 27 civilian, 27 remaining |

**Inferred:** At 100% stability, consumer goods reduce by another 5% (multiplicatively applied to the economy law's percentage), creating additional factory availability. Moving from Civilian Economy (35%) at 50% stability to War Economy (20%) at 100% stability frees approximately 20% more factories than the law change alone suggests.

## Game phases and ratio guidance

### Early game (1936–1938): Civilian focus

**Inferred:** In the opening game phase, your priority is building the civilian factory base that will fund the rest of your war effort. Aim for a **2:1 civilian-to-military ratio** or higher at game start, until payback is achieved.

- Build enough military factories to meet immediate doctrine and equipment needs (replacing export production, filling the gaps left by starting equipment stocks).
- Allocate most available construction to civilian factories and infrastructure in high-value states.
- Upgrade infrastructure to level 3–4 in your industrial core: each level of infrastructure raises construction speed by 20%, which cuts payback time by ~15% per level.
- Research construction technologies (Construction I–V) for an additional +50% construction speed bonus, cutting payback time dramatically.

**Powered output:** If you have reliable coal supplies (most European powers do), prioritize coal allocation to civilian factories; the boost from 4 → 5 daily output (+25%) is worth more than a +10% military factory bonus early on.

### Mid-game (1938–1940): Transition

**Inferred:** Once payback times are achieved, gradually shift toward a **1:1 ratio**, then begin tilting military-heavy as war looms.

- Continue building civilian factories only if your payback time is still short (< 600 days) *and* you have spare construction capacity.
- Begin ramping military factory construction 6–12 months before you expect to enter major conflicts.
- Maintain at least one free civilian factory per 10 military factories for trade, construction emergencies and potential lend-lease.
- If converting existing military factories back to civilian (conversion cost 9000 vs 4000 to reverse), only do so if you have severe resource bottlenecks or are forced into high-consumer-goods economy laws.

### Late game (1940+): Military priority

**Inferred:** Once major war begins, the goal is maximum military production. Target a **1:3 civilian-to-military ratio** or more aggressive.

- All new construction should prioritize military factories and dockyards, except in occupied territories still being integrated.
- Civilian factories are needed for:
  - Consumer goods (automatic, cannot be avoided)
  - Repair (especially of heavily damaged states)
  - Resource trade (if chronically short on tungsten, rubber or chromium)
  - Research speed (minor — only if not at war and research is your bottleneck)
- Naval dockyard construction should scale with fleet production needs; don't build dockyards if you lack oil for fuel or if naval combat is not your priority theatre.

## Powered vs unpowered output: Coal considerations

**Inferred:** Coal is the most abundant strategic resource in the game. Powering factories should be your top priority for any factory with reliable coal supply:

- Civilian factory: 4 → 5 daily output = +25%
- Military factory: 3.5 → 4.5 daily output = +28.6%
- Naval dockyard: 2 → 2.5 daily output = +25%

**Inferred:** If you can guarantee coal supply to both military and civilian factories, military factories have a slightly higher percentage gain (+28.6% vs +25%). However, prioritize civilian factories for coal in the early game to accelerate payback; switch to military-factory coal priority after payback is achieved.

## Trade law effects on factory balance

**Inferred:** Trade law modifiers apply equally to factory output and construction speed:

| Law | Factory output | Construction speed | Best use |
|---|---|---|---|
| Free Trade | +15% | +15% | Late game with naval strength; resource export is 80% |
| Export Focus | +10% | +10% | Balanced (default for most powers); 50% resources exported |
| Limited Exports | +5% | +5% | Early game caution; only 25% resources to market |
| Closed Economy | 0% | 0% | Autarky or total war; no resources exported (requires war or specific spirits) |

**Inferred:** When calculating payback times and switching points, account for your trade law. Export Focus at 10% construction speed gives ~10% faster payback than Limited Exports at 5% — this could move your switch point from September 1937 to August 1937.

## Resource shortage impact on factory efficiency

**Inferred:** Missing strategic resources penalise your lowest-priority production lines at −5% per missing unit per factory, up to −100%. This is not a direct penalty to factory construction or civilian factory output — it only affects equipment production. However, it indirectly constrains military factory usefulness: a military factory under −50% resource penalty produces only as much as a civilian factory running at full speed.

- Keep at least 2–3 free civilian factories on resource trade at all times during war.
- If you are critically short on a resource, temporarily converting military factories to civilian can free up trade capacity — but only if your equipment production can wait.

## Summary decision tree

1. **Are you still in peace?** → Build civilian factories until payback is achieved (~1–1.5 years depending on law and infrastructure).
2. **Is war 6–12 months away?** → Transition to mixed construction: some civilian factories (if payback is still being amortized), priority on military factories, infrastructure in war-adjacent regions.
3. **Are you at war?** → 80%+ of new construction on military factories and naval dockyards; 20%– on civilian replacement/repair and essential construction (forts, supply hubs).
4. **Do you have resource shortages?** → Allocate 1–2 civilian factories to trade to address bottlenecks (especially tungsten, rubber, chromium). Avoid over-trading for a single resource; balance against your war production timeline.
