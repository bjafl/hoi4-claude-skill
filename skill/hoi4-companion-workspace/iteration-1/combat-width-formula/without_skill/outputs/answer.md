# HOI4 Combat Width: Formula and Forest Terrain Reduction

*(Answered from training knowledge only, no external lookup performed. Exact numeric constants have shifted across HOI4 patches — treat the numbers below as approximate/best recollection rather than a guaranteed-current value.)*

## What "combat width" actually is

There are two related but distinct concepts that both get called "combat width":

1. **Division/template combat width** — a property of a division template, equal to the sum of the width contributions of its combat battalions (support companies generally contribute 0 width). For example, an infantry battalion typically contributes a fixed width value, and larger templates (more battalions) have a higher total width. This determines how much "space" a division takes up in a battle.

2. **Battle (terrain) combat width** — the amount of total width available in a specific engagement, which caps how many divisions' worth of width each side can commit to the front line simultaneously. This is determined primarily by the **terrain of the province(s)** where the fighting occurs, not by the divisions themselves.

## The general formula/mechanic

There isn't a single clean algebraic "formula" published as such; the mechanic works roughly like this:

- Each **terrain type** has a base combat-width value (with a small random range/variance rolled per-battle rather than one fixed constant — i.e., the effective width for a given battle is randomized within a band around the terrain's base value).
- When a battle involves **multiple attacking directions** (divisions attacking the same province from more than one adjacent province), each additional attacking direction adds extra combat width capacity to the battle (this is part of what makes encirclement/multi-pronged attacks effective — it lets more total divisions fight at once and grants a flanking bonus).
- The total width available to a side in the battle is compared against the summed combat width of the divisions trying to fight there. Divisions beyond what the available width can support are held as **reserves**, which rotate in over time (or during casualties/retreats) rather than all fighting simultaneously.
- Certain national/tech modifiers (e.g., dedicated "combat width" or encirclement-related technologies, and some doctrine/spirit effects) can modify the effective combat width of battles a country is engaged in.

So conceptually:

```
Available battle width (per side, per province) =
    Base terrain combat width (with per-battle random variance)
    + bonus width per additional attacking direction beyond the first
    + any national tech/modifier bonuses to combat width

Divisions actually fighting = however many divisions' summed template widths
    fit inside the Available battle width; the rest sit in reserve.
```

## Forest terrain's effect

Forest is one of the terrains that **reduces the available combat width** relative to open terrain like plains — reflecting that dense woodland constrains how many units can physically engage across the front at once. From what I recall of the terrain tables, forest's base combat width sits roughly **15–20% lower than plains'** baseline value (plains being one of the highest, alongside desert/urban terrain, with hills/marsh/jungle/mountain generally lower still, mountain typically being the most restrictive).

In practical terms: fighting in a forest tile means fewer divisions per side can be actively engaged in the battle at the same time compared to fighting the same encounter in plains — extra divisions queue up as reserves instead of contributing combat power immediately.

## Caveat

HOI4's combat-width system was substantially reworked in a past major patch (moving from a single fixed per-terrain number toward the randomized-range/attacking-direction model described above), and terrain base values have been tuned since. I'm confident in the *mechanism* (terrain sets available width, forest is meaningfully lower than plains, multiple attack directions add width, excess divisions become reserves), but I'd treat any precise numeric value (e.g., "forest = 70," "plains = 90," "forest is exactly 20% less") as approximate recollection rather than a verified current-patch figure. For an exact current number, the in-game terrain tooltip or the HOI4 wiki's terrain table would be the authoritative source.
