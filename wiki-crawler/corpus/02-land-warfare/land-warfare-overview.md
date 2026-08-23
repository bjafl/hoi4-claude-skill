---
title: Land Warfare Overview
category: land-warfare
tags: [land warfare, theater, command group, strategic redeployment, naval transport, naval invasion, border war, volunteers, expeditionary forces, capitulation, province control]
game_version: "1.19"
dlc: []
sources:
  - https://hoi4.paradoxwikis.com/Land_warfare
  - https://hoi4.paradoxwikis.com/Warfare
  - https://hoi4.paradoxwikis.com/Border_war
---

## Summary

Land warfare is fought by divisions, organised bottom-up into command groups (armies), which are in turn grouped into player-defined theaters. This file covers the organisational layer above combat itself — theaters, command groups, strategic redeployment, moving troops by sea, naval-invasion caps, volunteers and expeditionary forces, capitulation and province/state control, and the full border-war mechanic. For the actual battle resolution see [land-combat.md](land-combat.md); for building the divisions see [division-designer.md](division-designer.md).

## Command hierarchy

| Level | Contains | Led by | Notes |
|---|---|---|---|
| Division | Battalions + support companies | — | The atomic combat unit |
| Command group (army) | Divisions | General | Receives battle-plan orders |
| Army group | Up to 5 command groups | Field Marshal | 7 with the **Expert Delegator** trait |
| Theater | Command groups | — | Player-defined, purely organisational/UI |

**Command limits (stacking penalty thresholds):**

| Situation | Divisions a general can command without penalty |
|---|---|
| Default | 24 |
| With **Skilled Staffer** trait | 30 |
| Under an **Area Defense** order | 72 |

A Field Marshal can lead 5 armies without penalty (7 with **Expert Delegator**). Exceeding these caps applies a stacking penalty to the whole group — see [land-combat.md](land-combat.md).

## Theaters

A theater is a high-level, player-defined grouping of command groups. It exists for information and control, not for combat mechanics.

- Aggregates alerts (low supply, combat progress summaries) for everything inside it.
- Reinforcement priority can be set for an entire theater at once.
- Air and sea region names appear below the command theaters, giving alerts for impending invasions, ongoing sea battles and enemy air superiority.
- **Creating one:** with no theaters, creating a command group creates one. Otherwise select a command group — a "New Theater" button appears; clicking it creates a theater and moves that group into it. Right-click a theater to move a selected group into it.
- **Renaming:** click the gear icon left of the name (clicking the name itself does nothing). Unlimited theaters allowed.
- **Combat Log:** the document icon right of the theater name. Shows recent battle results, filterable by time (top-left slider) and command group (halo icons, top-right). Also shows equipment losses and performance broken down by division template.
- The theater interface shows **only divisions assigned to a command group**. Unassigned divisions appear in the armies list instead.

Typical use: separate Eastern/Western fronts as Germany; a dedicated training theater to exercise units up to Regular experience before reassigning them; a garrison theater for ports and victory points.

## Command groups

A command group is a collection of divisions under one commander, belonging to exactly one theater and movable between theaters freely.

Command groups are what receive **battle plan** orders: front line + offensive plan, garrison area, fallback line, naval invasion, paradrop. The commander portrait of each group in the selected theater appears at the bottom of the screen (a silhouette if leaderless). With one or more attack plans assigned, the portrait gains:

- a button to activate the plans,
- a button to halt plan execution,
- a bar showing the AI's assessment of relative strength.

## Strategic redeployment

Right-click destination with the redeployment mode to move divisions off the front quickly.

| Property | Value |
|---|---|
| Base speed on infrastructure (roads/bridges) | 5 km/h, up to **+10 km/h** depending on state infrastructure level |
| Base speed on railways | 15 km/h, up to **+25 km/h** depending on railway level |
| Organization while redeploying | Drops by **90%** |
| Attrition | None |
| Fuel use | Zero |
| Terrain / weather movement penalties | Not applied |

Because org drops 90%, a redeploying division that is caught cannot fight. Redeploy only through secure rear areas.

## Naval transport (port-to-port)

Troops move between two friendly ports over water.

- With a division standing in a port, right-click another port to transport it there.
- If the division is not in a port: right-click the port province, then shift-click the destination port symbol — one order does both legs.
- **Convoys required = the division's weight, rounded up.**
- Without naval supremacy over the sea region (own or allied), transports can be intercepted, causing casualties.
- Battle-planner orders (front line, fallback line, naval invasion, garrison) will automatically ship a unit across an ocean tile if no land path exists and enough convoys are free.

## Naval invasion

Launched via the naval invasion order in the battle planner. See also the naval-warfare files for escort and supremacy requirements.

| Transport technology | Max divisions a country may have assigned to naval invasions at once |
|---|---|
| Basic Transport Ship (starting tech) | **10** |
| Landing Craft | **50** |

Multiple invasion plans may originate from a single command group. Each plan must start from a friendly port, and the **total across all plans** must not exceed the transport-tech cap.

An army can also move into friendly territory using an invasion order, but port-to-port movement is more efficient for that.

## Volunteers

Sending divisions or air wings to fight another country's war without joining it.

**Rules**

- Only possible while the sender is **not at war** itself.
- In any given conflict a country may support **only one side**.
- Recipient capacity is calculated separately per recipient country.
- Gated by ideology and world tension: Fascists may send freely; Democracies are the most restricted. France can unlock it early.
- Sending increases world tension by **+0.02 per division sent**.
- Volunteers are controlled, supplied and reinforced by the **sending** country.
- Travel time is **14 days** each way.
- They return home if the sender goes to war or the recipient reaches peace. On return they bring back **95% of their equipment**; the rest is lost.
- Disbanding a volunteer division returns manpower and equipment to the sender, but a replacement division must be raised and trained from scratch.
- On arrival a new army theater is created for the player and the volunteer army group is placed in it. Armies cannot be transferred into or out of these special theaters.
- Commanders may be assigned and gain experience/traits normally, before or after arrival.

**Army volunteer capacity**

| Component | Amount |
|---|---|
| Minimum divisions to send anything at all | **30 active divisions** |
| From own army size | 1 division per **20** active divisions (rounded down) |
| From destination size | +1 division per **20 provinces** in the destination country |

Division size is irrelevant to the count: a 1-battalion division counts the same as a 25-battalion one. Examples: 176 divisions → 8 sendable; 181 divisions → 9.

**Air volunteer capacity**

| Component | Amount |
|---|---|
| From own planes (deployed + stockpile) | 20 planes per **100** owned |
| From destination air bases | 20 planes per **level** of air base in the destination country |

Both limits apply — the lower governs. Example: 1000 planes owned allows 200, but if the destination only has level-2 and level-3 air bases (5 levels total) the cap is 100. You must be *able* to send army volunteers to send air volunteers, but you do not need to actually send any divisions.

Air volunteers are sent by relocating wings to a destination airfield through the air interface, then ordering them normally.

**Focuses that unlock volunteers** exist for a large number of countries. Notable clusters: Spanish Civil War interventions (Germany **Legion Condor**, Italy **Corpo di Truppe Volontarie**, Soviet Union, Portugal, Mexico **International Struggle**, Hungary **Officialize the Rákosi Battalion**, Poland **The Dąbrowszczacy**, Czechoslovakia **State-Sponsored Recruitment for Spain**), Sino-Japanese interventions (Soviet **Two Red Flags**, **Support the Kuomintang**, **The Gobi Gambit**; Japan **Fund Resistance Groups in Asia**), Winter War aid (Germany **Support Finland**, Sweden **Swedish Volunteer Corps**, Hungary **Support for our Finnish Brothers**), and the generic tree's **Militarism**, **Interventionism Focus**, **Volunteer Corps** and **Foreign Expeditions**.

## Expeditionary forces

Handing divisions over to an ally already at war.

- Can be handed over and returned at any time; disbanding an expeditionary division simply returns it.
- **Equipment and manpower** come from the home country; **supply** comes from the controlling country. This makes expeditionaries a way to offload supply strain onto an ally with a better supply situation.
- The recipient has full operational control until return.
- War score for **occupation** goes to the controlling country; war score for **casualties** goes to the home country.
- Expeditionary divisions gain experience, but the recipient **cannot modify their template**.
- They keep the **home** country's military high command and Army chief of staff bonuses; the recipient's staff bonuses do not apply to them.
- To request them: create an empty army via the button under the empty portrait at the bottom of the screen, then give that army an order (e.g. a front line) so the AI has a reason to accept.
- Recipients often want to lend-lease matching equipment types back to the home country so the expeditionaries stay supplied.

## Capitulation and defeat

A country capitulates when it loses control of more victory points of its **owned core territory** than its surrender limit allows.

| Surrender-limit modifier | Value |
|---|---|
| Base surrender limit | **80%** |
| War support below 50% | up to **−30%** |
| Collaboration government set up against it (requires **La Résistance**) | up to **−30%** |
| France's **Disjointed Government** national spirit | **−50%** |
| Normal floor | **20%** |

The only exception to the 20% floor is Japan, which can go lower after losing Okinawa and Iwo Jima, having fewer than 40 ships, and being hit by two nuclear bombs.

**On capitulation:**

- The country capitulates to whoever dealt the highest war score against it. Holding the enemy capital grants a **+50% bonus and +150 flat war score** for this selection only.
- It loses control of all owned provinces contiguous with its capital, and all its troops there.
- Allied troops present must escape through now-enemy territory.
- The winner receives **50% of the capitulated country's equipment stockpile and land units**.
- Countries will not surrender within **7 days** of a war starting, giving them time to join a faction.
- Capitulation is not automatic defeat: with major allies still fighting, the war continues. Conversely a minor can be forced to surrender once all its major allies capitulate.

## Territorial control

### Province control

Control flips when the first division of a country at war with the current controller enters a province with no defenders present — after winning a battle, entering an undefended province, paradropping, or landing an invasion.

An eligible country is one at war with the original controller that has granted military access to the entering division's country (explicitly or by shared faction). Claims rank, strongest first:

1. Owns the state the province is in
2. Has a **core** claim on the state
3. Has a **generic** claim on the state

The strongest claim wins. Ties within the same claim tier break as follows:

1. If the division's own country is tied and controls more neighbouring provinces than any other tied country, it gains control.
2. Otherwise the tied candidate with the largest **civilian industry** gains control.

If no eligible country has any claim:

1. The eligible country controlling the most neighbouring provinces gains control (ties broken by civilian industry size).
2. Otherwise the division's own country gains control.

In every case **except the neighbourhood rule**, if the selected country is a subject, control passes to its master instead.

### State control

- Losing the last province of a state hands the **whole state** to the new controller if that controller also controls an adjacent state.
- Otherwise the surrounding states' controllers are checked for co-belligerent faction members of the new controller; if any exist, the state goes to the one with the largest industry, with a slight bias toward the faction leader.
- Faction members can transfer states explicitly with the diplomatic actions **"Give control of state"** and **"Ask for control of state"**. AI allies generally accept only if their own share of controlled states is large enough and the requester's is not already too large.

## War goals

A declaration of war requires a war goal. Justifying one costs political power, raises world tension, and normally takes **six to nine months**. A completed justified casus belli stays valid for **two months** after completion. Achieving a war goal gives an advantage at the peace conference, and the targeted state can be taken more cheaply there. Ahistorical war goals are possible (e.g. Sweden restoring its historical borders). A **border war** may be declared as an alternative to full war.

## Border wars

A border war (border conflict) is a small-scale, decision-and-event-driven conflict that can transfer a state without full war. It is centred on China's Nationalist/Communist conflict and the warlords — for Communist China it is the core early-game plan — but Japan, Mexico, Free France and Greece can also access it. Some entry points require **Waking the Tiger**.

Exactly two parties are involved: **Aggressor** (the decider) and **Defender** (the target). The vanilla game limits a given country pair to **one border conflict at a time**, and a country to **one active border conflict anywhere**.

### Phase 1 — Cause an incident

The decision is **visible** if:

- No other border conflict has been initiated between the two parties.
- Neither party is in the same faction as, or a subject of, the other.
- And one of the following trigger sets holds:
  - The decider has flag `CHI_institute_cross_border_raids` and neither side is the Leader of China (a warlord in opposition can border-war all other warlords; the PRC counts as a warlord here).
  - The decider has flag `CHI_provoke_border_clashes` and the target is the Leader of China (warlord took the focus to fight the Leader of China).
  - The target has flag `CHI_provoke_border_clashes` and the decider is the Leader of China (the Leader of China can fight back).
  - The decider has flag `CHI_anti_opposition_campaigns` and both sides picked focuses supporting the Nationalist/Communist conflict.
  - The decider is Communist China and the target cooperates with the Nationalists.
  - Both target and decider are Chinese factions.
  - **Japan** with a direct border with the **Soviet Union**.
  - **Mexico** having completed **Seize the Panamá Canal**.
  - **Free France** having completed the Intervention focuses.
  - **Greece** having completed **Stage an Incident in the Bosporus**.

The decision is **available** if the aggressor fully owns and controls a source state, has at least 1 division in that state, has no active border conflict anywhere, and has no non-aggression pact with the defender.

| Parameter | Value |
|---|---|
| Decision cost | **100 PP** |
| Decision duration | **30 days** |
| Re-take lockout | **180 days** (plus state- and faction-specific lockouts) |

On taking the decision a random defender state without an active border conflict is chosen, then a random neighbouring attacker state. The defender is informed; both sides get the 30 days to move troops into position.

### Phase 2 — Committing

After the warning timer expires the attacker has **30 days** to commit. Committing starts combat instantly. Letting the timer run out costs the aggressor a further **100 PP**.

### Phase 3 — Combat

- **6 divisions** are drawn from each side's state and moved into a separate, locked army. Each army gets a **random leader** from that country's pool — this can pull generals or field marshals off other fronts. **No leader abilities can be used** during the conflict.
- Division selection is entirely random and cannot be influenced except by moving divisions out of the state beforehand. This is outside moddable code.
- Neither side can add, remove or reassign divisions until the conflict ends.
- Combat width is the **respective terrain's width**, and **all units start in reserve** — it is possible for one or both sides to have 0 divisions actively fighting and deal no damage.
- Selected divisions not already at the border must march there before entering reserve (common for garrison units). If the state lacks enough divisions, extras are pulled from anywhere in the country and must travel.
- AI divisions that drop out on org loss will retreat, recover to full and rejoin as reserve. **Player divisions that drop out do not return.**
- Planning bonus and commander abilities such as forced attack remain in effect.
- If nobody wins within **360 days**, the conflict is a draw.

### Escalation

There is a **45-day cooldown** between escalation options. Either side may escalate.

| Escalation | Cost | Effect |
|---|---|---|
| First | **200 PP** | Combat width raised to **100**; both sides get **+15%** bonus |
| Second | — | Becomes a full war after **15 days**, cancelling the border conflict and its combat |

Either side may also back out, which is an instant win for the other side. Lend-lease requires full war, so it is unavailable during a border war.

### Results

| Outcome | Effects |
|---|---|
| Attacker wins | Attacker gains **100 PP** and control of the state. If it was the target's last state, the target is **annexed** instead |
| Defender wins | Defender gains **150 PP**, **30 Army XP**, and a **+100% research bonus to one land doctrine**. Attacker loses **150 PP** |
| Cancelled (both sides at war, same faction, or timeout) | Both sides gain **30 Army XP** and **50 PP** |

A failed initiator cannot start another border war against the same defender for **180 days**, win or lose.

### Border-war tactics

- Always exactly **6 divisions** regardless of width, so **high-width divisions are strongly favoured** — design and position them to be picked.
- Attack modifiers matter most. Location within the state is irrelevant and terrain modifiers do not apply to positioning, but supply does — place troops where supply is sufficient to avoid the low-supply debuff.
- Terrain, entrenchment and other **defensive** modifiers ARE in effect. The defender has a considerable edge because defence typically exceeds breakthrough.
- Strait-crossing penalties still apply (likely an oversight, since the mechanic was built for mainland China).
- The defender can win purely by surviving the full 360 days; the attacker must actually destroy the enemy, and should prefer a draw over a defeat.
- Leader abilities cannot be triggered during the conflict but can be selected just before it and still take effect.
- Because every unit starts in reserve, **reinforce rate is extremely important**.
- The AI cannot manipulate its selection and often has garrison cavalry dragged in — but a manned AI frontline drastically raises the average quality of what gets picked.
- Logistics priority resets to unmotorized (horse) regardless of the previous setting.
- Experience gained per manpower lost is exceptionally good, producing a few very highly experienced divisions for later use.

## Related files

- [division-designer.md](division-designer.md) — building templates
- [land-units-and-stats.md](land-units-and-stats.md) — battalion and support company stats
- [land-combat.md](land-combat.md) — battle resolution, width, terrain, entrenchment
- [combat-tactics.md](combat-tactics.md) — tactic phases and tables
- [historical-divisions.md](historical-divisions.md) — reference templates
