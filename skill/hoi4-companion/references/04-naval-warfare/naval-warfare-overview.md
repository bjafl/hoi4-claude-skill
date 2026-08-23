---
title: Naval Warfare Overview
category: naval-warfare
tags: [navy, task force, fleet, theater, naval missions, patrol, strike force, convoy escort, minelaying, naval invasion support, London Naval Treaty]
game_version: "1.19"
dlc: [Man the Guns]
sources:
  - https://hoi4.paradoxwikis.com/Navy
  - https://hoi4.paradoxwikis.com/Naval_warfare
  - https://hoi4.paradoxwikis.com/Naval_missions
  - https://hoi4.paradoxwikis.com/London_Naval_Treaty
---

## Summary

Naval forces are organized hierarchically into task forces (individual ship groups), fleets (collections of task forces), and theaters (groupings of fleets), each receiving bonuses from assigned admirals. Task forces execute missions—patrol, strike force, convoy escort, minelaying, and others—within fleet-assigned strategic regions. The London Naval Treaty (requires Man the Guns) constrains carrier, cruiser, and battleship production costs for major powers but may be withdrawn, cheated (by fascist nations), or escalated as world tension rises.

## Navy hierarchy

| Unit | Contains | Led by | Notes |
|---|---|---|---|
| Task force | Individual ships | — | The atomic naval unit; moves at slowest ship's speed |
| Fleet | One or more task forces | Admiral | Provides bonuses to all task forces within it; defines mission operating regions |
| Theater | One or more fleets | — | Organizational grouping; has reserve fleet for unassigned ships; serves one purpose per theater (e.g., different seas) |

## Task force

Task forces are player-controlled groups of ships that execute missions. Each has a customizable name and insignia.

**Creation and reinforcement:**
- Newly built ships join assigned task force or reserve fleet.
- Existing task forces can be split (half, or custom split) or merged with other task forces.
- Ships can be reassigned between task forces by right-click.
- Automatic reinforcement can be enabled to maintain desired composition from the theater's reserve fleet.

**Repair and engagement:**
- Automatic split-off detaches heavily damaged ships for repairs while the rest continues.
- Repair priority setting governs how severely damaged a task force must be before returning to port.
- Explicit repair order (`Repair now!`) detaches individual ships or groups to return for repairs.
- Engagement rule (from "Never engage" to "Always engage") controls aggressiveness—e.g., whether submarines attack screens or only capital ships.

## Fleet

A fleet is a collection of task forces under one admiral, conferring the admiral's bonuses to all constituent task forces.

**Region assignment:**
- When task forces in a fleet are assigned a mission, the fleet can be assigned to specific strategic regions by right-clicking on the map.
- This determines where task forces may be automatically distributed when executing their mission.
- Assigned regions highlight with a pulsing color fade.

## Theater

Theaters are groupings of fleets, each with its own named naval theater. There is always at least one; additional theaters can be created by selecting a task force, clicking "New Theater", which moves it to a new theater.

- Serve as logical categories (e.g., different seas, different mission types).
- Each theater has a reserve fleet that can accommodate unassigned task forces.
- Alert priority can be set to "normal" or "high"; high priority alerts (e.g., naval battle in progress) display prominently.
- A theater is deleted when all its fleets are moved to other theaters.

## Naval overview screen

Opened with the P hotkey or by clicking the navy icon. Displays:

| Modifier | Base value | Notes |
|---|---|---|
| Escort efficiency | 0% | Global bonus applied to escort efficiency |
| Sortie efficiency | 50% | Ratio of carrier aircraft available for combat |
| Naval targeting | 0% | — |
| Port strikes | 100% | — |
| Carrier overcrowding | 100% | — |
| Convoy raiding efficiency | 100% | — |
| Naval invasion capacity | 0 | — |

Also shows ship counts by type, a list of all task forces with their mission and operating area, lost ships (last two years), and equipment details by class.

### Pride of the Fleet

A single capital ship may be designated Pride of the Fleet (PotF), granting the nation +5% war support. The ship gains -50% vulnerability to critical hits, +25% experience gain, and is less prone to accidents.

- Reassignment costs 100 Political Power (free for non-starting navies that acquire their first capital ship).
- If lost to the enemy, incurs -10% war support for 30 days.
- If captured or destroyed, a replacement can be assigned for the normal 100 PP cost.

## Naval missions

Missions are assigned to task forces; operating regions are defined at the fleet level. Each mission has a hotkey. When a task force is executing a mission in the fleet's assigned region, a mission icon appears in that region with a count of task forces performing it.

### Naval exercises

A task force gains experience by conducting exercises in a region adjacent to the nearest port.

- Gain experience each day until reaching "Regular" level.
- Fuel consumption: 60% of normal.
- Small chance of incurring accident damage.
- Provide navy experience each day.

### Patrol

Searches for enemy ships in a single strategic region. Generates spotting progress as a percentage; at 100%, battle becomes possible.

**Spotting mechanics:**

Spotting progress increases by hourly change. If hourly change is zero or negative, the patrolling task force cannot spot the enemy. For submarine forces, spotting starts with a base spotting chance and increases hourly until 100%.

**Submarine spotting formula:**
```
hourly spotting chance = 5% × (2 × hourly change + 0.5 × (base spotting chance)^1.5)
```

- A patrol can only spot one enemy task force at a time (and vice versa).
- After reaching 100% spotting, the patrol engages based on its engagement rule; strike forces in the same region may also engage based on theirs.
- If set to "Never engage", the patrol avoids battle until a strike force arrives, then disengages immediately after battle starts.

### Strike force

Intercepts and engages enemy forces spotted by patrolling task forces in the fleet's assigned regions. Does not require same fleet as the patrol. Remains in port when not intercepting (conserving fuel).

- Only engages if engagement rule permits.
- "Never engage" keeps strike force in port indefinitely; "Always engage" allows interception regardless of enemy strength.
- May be manually ordered to stop intercepting and return to port.
- Can be far from the spotted enemy, causing late arrival.
- Passively projects naval supremacy across assigned regions within range.

### Convoy raiding

Searches for enemy convoys in the fleet's operational area. Raiding force must spot convoys before attacking.

- Each raiding task force efficiently covers 1.5 strategic regions.
- If insufficient raiding task forces for the area, efficiency is reduced.

### Convoy escort

Protects player and allied convoys under attack within the fleet's assigned regions.

**Escort efficiency:**
- When escort efficiency is 100%, defending ships instantly respond to convoy attacks.
- If below 100%, defending ships arrive late, increasing convoy losses.
- Must have sufficient ships and task forces to cover all assigned regions.

Troop transfers via naval invasion orders can also be protected with this mission (though naval invasion support is often more appropriate for invasions specifically).

### Minelaying

Ships equipped with minelaying equipment lay mines up to 1000 per assigned strategic region (saturation point). All assigned regions are mined simultaneously.

**Effects by mine count (scaled):**
- Bonus to naval supremacy for the mine owner.
- Penalties to enemy ships only: up to +5% accident chance, up to +50% invasion penalty.
- ⚠️ Note: Wiki previously stated mines reduced ship speed; current patch: speed no longer affected.

Rate of minelaying depends on fleet size and number of assigned regions; additional regions reduce per-region rate.

### Minesweeping

Destroyers equipped with minesweeping gear clear mines from assigned strategic regions during wartime until fully clear.

### Naval invasion support

Task forces escort convoys ferrying friendly troops for a naval invasion. Once convoys arrive, task forces hold position adjacent to the landing site and perform shore bombardment during any land battle. Return to home port after battle ends.

### Hold

Task force returns to nearest friendly port (cancels current mission). Alternatively, holding Ctrl while clicking hold keeps the task force in its current province (does not consume fuel). A task force on hold can block connections between land provinces via the sea, preventing enemy land movement.

**Shore bombardment:**
If surface ships on hold are adjacent to a land battle with enemy divisions, they automatically bombard to reduce enemy attack and defense.

- Heavy gun damage: -0.05% per point to enemy attack and defense.
- Light gun damage: -0.025% per point to enemy attack and defense.
- Total reduction capped at -33%.
- Can critically hit, causing severe damage to forts.
- Increased by Naval Liaison (general trait) and Ground Pounder (admiral trait), though capped at -33%.

## London Naval Treaty

Introduced with Man the Guns. Constrains the major powers—United States, United Kingdom, France, Italy, and Japan—in the maximum production cost of carriers, cruisers, and heavy ships (battlecruisers and battleships), and in the ratio of capital ships to the United Kingdom's capital ships.

**Treaty signatory limits:**

| Ship type | Max production cost |
|---|---|
| Carrier | 9500 |
| Cruiser | 5300 |
| Heavy ship | 10000 |

Countries may design any ship but can only produce within limits.

### Invitation and enforcement

When a non-signatory nation reaches approximately 20% of the United Kingdom's capital ships (weighted toward heavier ships), they receive an invitation to join. If they decline and continue expanding, treaty nations can force disarmament to 80% of capital ships at threat of war. If a signatory exceeds allocated capital ships, they receive a mission to reduce numbers or suffer major stability loss.

### Second London Naval Treaty mission

A 120-day mission runs from January 1st 1936. All participating nations may withdraw during this period:

- Fascist nations: 25 Political Power.
- Non-fascist nations: 150 Political Power.

After the mission ends (or after April 30th 1936), 20% world tension is required to withdraw again.

### Cheating on the treaty

Fascist nations may cheat on the treaty for 50 Political Power, increasing maximum production costs while keeping the treaty in force (non-fascist signatories still bound). Italy starts 1936 already cheating.

**Cheat bonuses:**
| Ship type | Production cost increase |
|---|---|
| Carrier | +750 |
| Cruiser | +400 |
| Heavy ship | +1500 |

This allows fascist nations to build bare-bones super-heavy battleships without withdrawing.

### Escalator Clause Invoked

When world tension reaches 20% or any country withdraws from the treaty, a 365-day mission begins. At completion, the London Naval Treaty Signatory spirit is replaced with Escalator Clause Invoked, increasing production cost limits:

| Ship type | Production cost increase |
|---|---|
| Carrier | +1000 |
| Cruiser | +700 |
| Heavy ship | +2000 |

After any two major powers (except Chinese factions) enter war, or when world tension reaches 75%, the treaty becomes defunct.

## Related files

- [Ship designer](ship-designer.md) — designing and refitting ship classes.
- [Naval battle](naval-combat.md) — naval combat mechanics.
- [Naval technology](naval-technology.md) — naval research.
- [Naval doctrine](naval-doctrine.md) — doctrine bonuses for naval warfare.
