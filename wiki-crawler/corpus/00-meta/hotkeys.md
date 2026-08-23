---
title: Hotkeys
category: meta
tags: [hotkeys, keyboard shortcuts, controls]
game_version: "1.19"
dlc: []
sources:
  - https://hoi4.paradoxwikis.com/Hotkeys
---

Keyboard shortcuts for quick access to game functions without using the mouse. Hotkeys cannot be changed via the in-game interface; modification requires editing game files or using third-party tools.

## Top menu hotkeys

Direct access to primary menus from the top-left corner of the screen. These keys follow the top row of the keyboard from left to right. La Résistance adds one additional button (Shift+E).

| Hotkey | Function |
|---|---|
| Q | Government |
| Shift+Q | Decisions |
| Shift+W | Intelligence agency |
| W | Research |
| E | International Market |
| R | Trade |
| T | Construction |
| Y | Production |
| U | Recruit & Deploy |
| I | Logistics |
| Shift+E | Officer Corps (La Résistance only) |

## Map hotkeys

| Key | Action |
|---|---|
| Ctrl + number (0–9) | Assign a province or Strategic Region to a number. Left-click to select, then Ctrl+number to hotkey. Pressing the number twice centers the map on that location. |
| Home | Zoom in |
| End | Zoom out |
| Ctrl+F9 | Toggle GUI (hide all UI elements, show map only). Equivalent to console command `debug_nogui`. |
| Ctrl+F10 | Save political province map to Screenshots folder |
| Ctrl+Shift+F10 | Toggle freeze camera (disable zoom and pan until pressed again) |
| F11 | Screenshot (save to Screenshots folder) |
| Space / Pause / Break | Toggle pause (works in multiplayer) |
| Backspace | Jump to capital |
| Arrow keys | Pan camera (equivalent to moving cursor to screen edge or middle-mouse drag) |
| AltGr+Shift+Click | Add attack marker for multiplayer allies |
| AltGr+Click | Add defend marker for multiplayer allies |
| Ctrl+Alt+Click | Add defend marker for multiplayer allies |

## Map mode interface hotkeys

Located in the bottom-right corner of the map. Each mode emphasizes different information and updates tooltips accordingly.

| Key | Map Mode | Description |
|---|---|---|
| Ctrl+F1 | All Possible Map Modes | Opens window showing 12 available map modes |
| F | Search (Find) | Find countries, states, and cities. Type ≥2 letters to filter. Flags mark countries; circles (≥20 VP) or squares (<20 VP) mark cities. Green = your control, gray = friendly/neutral, red = enemy. "Go Home" centers on your capital. |
| F1 | Default | Blend of Political and Terrain modes showing country borders, terrain type, and province control. Recommended for land combat. |
| F2 | Strategic Navy | Emphasizes naval regions. Colors: green (naval superiority), yellow (parity), red (inferiority). Shows naval bases, convoy routes, and mission icons. Yellow diagonal bars = "avoid" regions; red = "blocked" regions. |
| F3 | Strategic Air | Emphasizes air regions. Colors: green (air superiority), yellow (parity), red (inferiority). Shows air bases, air zones, and mission icons. |
| F4 | Supply | Displays current supply situation by province color. Shows capital hub, railway/convoy connections to supply hubs, and bottlenecks via tooltips. Third map mode to display convoy routes. |
| F5 | Terrain | Displays terrain types as simplified colors. Hovering shows tooltip with terrain effects on units. |
| F6 | Resistance | Colors states by resistance level. Tooltip provides detailed resistance information. |
| F7 | Compliance | Colors states by compliance level. Tooltip provides detailed compliance information. |
| F8 | Resource | Displays resource location by state and quantity worldwide (including synthetic production). Third map mode to display convoy routes. |
| F9 | Infrastructure | Shows infrastructure level of each state. |
| F10 | Factions | Displays faction names and colors nations by faction affiliation. |
| M | Unit Counters toggle | Toggle display of all unit counters or only player counters. |
| , | Counter Colors toggle | Toggle allied counter colors between country colors or Friendly/Neutral/Enemy colors. |
| . | Allied Battleplans toggle | Toggle display of allied battleplans on/off. |
| N | Day/Night toggle | Toggle day/night map overlay. |
| (no hotkey) | States | Color states by starting construction slot category (color does not change, but slots increase via technology/focuses). |
| (no hotkey) | Diplomacy | Color nations by opinion of selected nation (right-click to select). Green = your territory; blue = same faction; gray = neutral opinion; orange = very bad opinion; red = at war. |
| (no hotkey) | Players | Show which country is controlled by which player. |
| (no hotkey) | Population | Show population count in each state. |
| (no hotkey) | Ideology | Color countries by ideology. Blue = Democratic; brown = Fascist; red = Communist; gray = Non-Aligned. |
| (no hotkey) | Operatives | Emphasize operatives, missions, ongoing operations, and intel network spread. See [Espionage and Operations](../01-mechanics/espionage-and-operations.md). |
| (no hotkey) | Fog of War | Toggle clouds that obscure terrain on/off. |
| (no hotkey) | Radar | Toggle radar range visibility lines on/off. |

## Army hotkeys

| Key | Action |
|---|---|
| O | Open Division Overview |
| Ctrl + number (0–9) | Assign an Army or Divisions to a number. Left-click army or Shift+click multiple divisions, then Ctrl+number. Pressing number twice centers map on unit(s). |

### Battleplan hotkeys

Active only when units from a single army are selected and battleplan interface is visible.

| Key | Order | Description |
|---|---|---|
| K | Exercise | All divisions commence exercise order (cancels battleplans but not movement orders). Low Organization; keep out of combat. |
| Shift+K | Exercise until trained | Troops train until reaching Regular experience level, then stop individually. |
| Z | Front Line | Click border or right-click and drag to customize size. Cannot drag across multiple borders except in wartime. |
| X | Offensive Line | Right-click and drag after creating Front Line. Tab cycles through possible starting points for multi-step plans. Requires existing Front Line. |
| Shift+X | Spearhead | Right-click and drag to draw spearhead. Aggressively seizes all provinces present when order painted. Preferred for overlapping encirclements and armored thrusts. Requires existing Front Line. |
| C | Fallback Line | Right-click and drag to create defensive line anywhere (not just borders). |
| V | Garrison Area | Activate, select states, press V again to exit. Divisions spread across states and occupy cities, airbases, naval bases. Exclusive order; entire army must use it. |
| Ctrl | Divisions Assignment Mode | Left-click while holding Ctrl on a battleplan to assign selected units. Right-click with Ctrl to select all units assigned to that plan. |
| Ctrl+H | Unassign Divisions Mode | Unassign currently selected divisions from their orders. |
| Alt | Edit Mode | Alt + right-click and drag to alter front/offensive/fallback line length and shape. Alt + left-click to bend offensive arrows or change origin point. |
| Del | Delete Order | Remove individual battleplans from current army. Right-click button to delete all orders. |
| (no hotkey) | Battleplan execution mode | Set AI execution to "carefully", "balanced", or "aggressively". |
| (no hotkey) | Cohesion | Set AI unit frontline assignment to "flexible", "balanced", or "rigid". |
| (no hotkey) | Naval Invasion | Highlight launch ports (turquoise diagonal stripes), click desired port (becomes blue), right-click coastal target (becomes orange). Reserves convoys automatically. |
| (no hotkey) | Naval Invasion with Floating Harbor support | Same as Naval Invasion; requires ≥1 Floating Harbor produced and in stockpile. |
| (no hotkey) | Paratroop Order | Highlight air bases (turquoise if transport planes present, yellow if none), click desired base (becomes blue), right-click drop target (becomes orange). Requires ≥70% air superiority and sufficient transport planes. |

### Division management hotkeys

Applied when divisions are selected.

| Key | Action | Description |
|---|---|---|
| S | Select Half | Deselect half of selected units (rounding up). Press repeatedly to halve selection further. Allows isolating single units from stacks. |
| H | Hold | Order unit to hold position, canceling move/attack orders. Will not cancel battleplan assignment. |
| B | Strategic Redeployment | Press before movement order. Divisions use roads, bridges, and railroads to increase movement speed at Organization cost. |
| Ctrl+B | Toggle Strategic Redeployment | Press after movement order to toggle strategic redeployment on/off. |
| X | Unassign Units | Remove selected divisions from army. Preserves divisions for reassignment. |
| Shift | Waypoint | Right-click while holding Shift to set waypoint series. Units navigate to each waypoint in succession, choosing optimal paths. |
| Ctrl | Support Attack | Right-click existing battle while holding Ctrl to "support" that battle. Allows participation without entering battle hex afterward. |
| Ctrl+H | Remove from Assigned Battleplan | Remove selected divisions from battleplan without removing from army. Does not work with armies having garrison orders. |
| (no hotkey) | Disband All Selected Units | Return division manpower to recruitable pool and equipment to stockpile. Caution: Encircled units lose manpower/equipment permanently. |
| (no hotkey) | Consolidate | Merge selected divisions (same template only) into stronger divisions with no experience loss. Excess manpower/equipment returned to pools. |
| (no hotkey) | Change Division Template | Change selected divisions to different template from pull-down menu. |

## Naval hotkeys

| Key | Action |
|---|---|
| Ctrl + number (0–9) | Assign Task Force(s) to a number. Left-click task force or Shift+click multiple. Ctrl+number to hotkey. Pressing number twice centers map. |
| P | Open Navy Overview |
| D | Split | Divide selected task force into two. |
| S | Select Half | Select half of currently selected naval units, maintaining equal type distribution. |
| G | Merge | Merge selected task forces. If not in same province, they navigate to each other. |
| K | Naval Exercises | Task force performs exercises in adjacent region. Crews gain ship experience, country gains navy experience. Costs fuel; risks ship damage. Crew experience caps at Regular level. Continues until manually halted. |
| Shift+K | Naval Exercises until trained | Exercises until all ships reach Regular level, then auto-stops and returns to base. |
| H | Hold - return to port | Cancel task force mission and return to closest port. |
| Ctrl+H | Hold - stay in place | Cancel task force mission and remain stationary. Capital ships on hold in sea provinces adjacent to land battles provide shore bombardment. Carriers on hold at sea can use airwings for standard air missions. |
| Z | Patrol | Patrol selected regions. Primary purpose: spotting enemy fleets. |
| X | Strike Force | Wait at closest naval base until patrol spots enemy, then intercept. |
| C | Convoy Raiding | Raid enemy convoys in selected regions. |
| V | Convoy Escort | Escort convoys in selected regions against enemy threats. |
| B | Minelaying | Lay sea mines in selected regions. |
| Shift+B | Minesweeping | Search and neutralize enemy sea mines in selected regions. |
| A | Naval Invasion Support | Escort naval invasions and provide shore bombardment. |
| Del | Remove Region | Click region to remove it from currently selected fleet. Right-click button to remove all regions. |

## Air hotkeys

| Key | Action |
|---|---|
| Ctrl + number (0–9) | Assign Air Wing(s) to a number. Left-click air wing or Shift+click multiple. Ctrl+number to hotkey. Pressing number twice centers map. |
| L | Open Airforce Overview |
| D | Split | Split selected air wings into two. |
| G | Merge Air Wings | Merge two or more selected air wings into one. |
| O | Merge Air Groups | Merge two or more selected air groups into one. |
| A | Select/Deselect All | Select/deselect all air wings in given airfield or carrier. |
| S | Select Half | Select half of currently selected air wings. |
| H | Hold Order | Hold selected air wings. |
| X | Remove Selection From Air Group | Remove selected planes from air group. Preserves planes for reassignment. |
| N | New Wing | Open new wing option for selected airfield or carrier. |
| K | Pilot Exercises | Gain air wing and air experience. Costs fuel; increases accident risk. |
| Shift+K | Pilot Exercises until trained | Exercises until air wing fully trained. |
| Z | Air Superiority Mission | Conduct air superiority mission. |
| X | Close Air Support Mission | Conduct close air support mission. |
| C | Interception Mission | Conduct interception mission. |
| V | Strategic Bombing Mission | Conduct strategic bombing mission. |
| B | Naval Strike Mission | Conduct naval strike mission. |
| J | Port Strike Mission | Conduct port strike mission. |
| Ctrl+R | Logistics Strike Mission | Conduct logistics strike mission. |
| Ctrl+B | Kamikaze Strike Mission | Conduct kamikaze strike mission. |
| (no hotkey) | Air Supply Mission | Conduct air supply mission. |
| (no hotkey) | Air Recon Mission | Conduct air recon mission. |
| (no hotkey) | Naval Patrol Mission | Conduct naval patrol mission. |
| (no hotkey) | Create Air Group | Combine selected air wings into air group. |
