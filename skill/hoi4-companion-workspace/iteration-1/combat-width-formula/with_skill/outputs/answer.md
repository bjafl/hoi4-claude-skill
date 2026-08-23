# Combat Width Formula and Forest Terrain's Effect

*(Source data reflects game version 1.19, per `land-combat.md`)*

## What sets combat width

Combat width for a battle is **not** a fixed number — it's set by the **terrain of the province being attacked**, and it scales up with flanking:

- Each terrain type has a **base combat width**.
- Each **additional province the attackers come from** ("flanking") adds extra width, at a per-terrain rate.
- **Paradrops and naval invasions each count as an extra flanking direction** too.

The relevant terrain rows from the file's combat-width table:

| Terrain | Base combat width | + per extra attack direction |
|---|---|---|
| Plains | 70 | +35 |
| Desert | 70 | +35 |
| Hills | 70 | +35 |
| **Forest** | **60** | **+30** |
| Jungle | 60 | +30 |
| Marsh | 50 | +25 |
| Mountain | 50 | +25 |
| Urban | 80 | +40 |

## Forest's exact reduction

Comparing Forest to the most common baseline (Plains, 70 / +35):

- **Base combat width:** Forest = **60** vs. Plains = **70** → Forest is **10 lower** (a **~14.3% reduction** relative to Plains).
- **Per extra attack direction:** Forest = **+30** vs. Plains = **+35** → **5 less per flanking direction** (also **~14.3%** lower).

Forest ties with Jungle at 60/+30 for base width; only Marsh and Mountain (50/+25) are narrower.

Forest also carries other combat-relevant modifiers listed in the same table row: **+50% movement cost**, **−15% attacker attack adjuster**, **−10% enemy air superiority reduction**, **max fort level 4**, **0.08 supply flow penalty**, **0.2 truck attrition**, and **−1 °C temperature bias**. (No terrain attrition/equipment-loss value or sickness flag is listed for Forest.)

## Division width and the over-width penalty formula

Each division's total width is the sum of its battalions' widths:

| Battalion type | Width |
|---|---|
| Infantry, armoured, cavalry, motorized, mechanized, tank destroyers | 2 |
| Artillery, rocket artillery (incl. motorized and self-propelled) | 3 |
| Anti-tank and anti-air (incl. motorized) | 1 |
| Support companies | 0 |

If the total width of divisions committed to a battle exceeds the battle's combat width, an **over-width penalty** applies, per the file's exact formula:

```
combat width penalty = -100% × (total_width − battle_width) / battle_width
```

At the start of a battle and on every reinforcement, divisions are added from reserve **unless** the combat width is already filled **or** the resulting width penalty would exceed **−33%**.

Worked examples from the file:
- **80-width Urban battle:** 106 total width is allowed (penalty ≈ −32.5%); 107 is not (≈ −33.75%).
- **70-width Plains battle:** with 10-width divisions, the 8th division stays in reserve because width is already **filled** at 70 — even though the resulting penalty would only be about −14.29%.

## Files consulted

- `/mnt/data/bjarte/source/hoi-claude-skill/.claude/skills/hoi4-companion/SKILL.md` (routing table)
- `/mnt/data/bjarte/source/hoi-claude-skill/.claude/skills/hoi4-companion/references/02-land-warfare/land-combat.md` (source of all figures/formula above)
