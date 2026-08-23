---
title: Special Projects and Scientists
category: mechanics
tags: [special-projects, scientists, gotterdammerung, facilities, prototypes, breakthroughs, nuclear, jets, rockets]
game_version: "1.19"
dlc: [Götterdämmerung]
sources:
  - https://hoi4.paradoxwikis.com/Special_project
  - https://hoi4.paradoxwikis.com/Scientist
  - https://hoi4.paradoxwikis.com/List_of_scientists
---

## Summary

Special projects (Götterdämmerung, patch 1.15) are long research programmes run by an employed **scientist** at a matching **experimental facility**. Each project costs **scientific breakthroughs** in its category to start, then runs through an establishing phase, an initial research phase, and a long prototyping phase in which successive prototypes add random progress and can fire outcome events. Completing a project unlocks equipment, modules, buildings, support companies or hidden technologies. This file covers the four categories, breakthrough sources, scientist skill/traits/experience, all named scientists, the full project list, and the prototype outcome tables.

## The four categories

| Category | Facility | Feeds off breakthroughs from | Focus of projects |
|---|---|---|---|
| Nuclear Research | Nuclear Research Facility | Computing technologies, RADAR technologies | Nuclear weapons, civilian nuclear power, naval nuclear reactors |
| Naval Engineering | Naval Engineering Facility | Naval technologies, naval support technologies | New ship hulls, submarine modules and upgrades, naval support tech |
| Aerodynamics and Avionics | Aerodynamics and Avionics Facility | Air technologies, anti-air technologies, rocket artillery technologies, rocketry technologies, radio technologies, RADAR technologies | New airframes, aircraft modules, early missiles, RADAR |
| Land Warfare | Land Warfare Facility | Armor technologies, motorized technologies, all artillery technologies except rocket artillery, radio technologies, RADAR technologies | Armored vehicles, artillery designs, advanced fortification |

Technology icons carry ribbons in the lower-right corner marking the categories they feed: **yellow = Nuclear Research, blue = Naval Engineering, red = Aerodynamics and Avionics, green = Land Warfare**. A technology with multiple ribbons feeds and benefits from multiple fields at once.

Facility costs and rules are in [Construction and buildings](construction-and-buildings.md#experimental-facilities-requires-götterdämmerung): one per state, 3 supply upkeep, cost `12000 + 5000 × facilities of that type you control` (Nuclear Research: `15000 + 5000 × …`), immune to strategic bombing but exposed to the enemy **Facility Strike**, and **not** helped by infrastructure construction-speed bonuses.

## Breakthroughs

Breakthroughs are the currency needed to start a project. Six sources:

| Source | Rate |
|---|---|
| Researching technologies tied to a category | **+0.12% breakthrough progress per research slot per day**, in each tied category. Research speed and bonuses are irrelevant — only raw slot-days spent count |
| A scientist performing **basic research** at a facility | **+0.05% × the scientist's skill** per day in that facility's category. Traits like Genius and Brilliant Theorist raise it. Each additional scientist doing basic research in the same field is progressively multiplied by **0.5×** |
| Certain prototype iterations | Give breakthrough progress in the same category (many "third-tier" outcomes give +10%) |
| Certain national focuses | Give breakthrough progress in a category |
| Rocket sites | **+0.01% Aerodynamics and Avionics per site per day** |
| Nuclear reactors (normal, heavy water and civilian) | **+0.01% Nuclear Research per reactor per day** |
| Capturing an enemy facility that is researching a project | **+10%** breakthrough progress in that facility's category, **reduced by 60% for each such capture after the first** |

## Running a project

Three phases:
1. **Establishing** — repeated every time a project is started or restarted.
2. **Initial research** — happens once per project. Progress here is **retained** if the project is stopped mid-phase.
3. **Prototyping** — the long phase. Each prototype takes a fixed number of days (per project) and adds a random amount of progress within a per-project range. A finished prototype can also fire an **outcome**, which may add or remove progress, apply effects, or force a choice. The project completes at 100% progress.

Rules:
- The project must be run at a facility of the matching category that **already has a scientist employed doing passive research**. While on the project that scientist gives **no** passive research speed bonus, **no** passive breakthrough progress and **no** passive experience.
- The scientist can be swapped or reassigned only after **10 days** on the project.
- Facilities researching a project consume **3 supply** (reducible with the **Resourceful** trait, −10%).

Speed and progress modifiers:

| Condition | Effect |
|---|---|
| Resource shortage (projects with a resource cost must be supplied for the whole run) | Project speed down to **0.2×** |
| Supply shortage (train shortage, damaged supply infrastructure) | Project speed down to **0.2×**. Below 66% of supply need, the facility pane shows a warning |
| Scientist injured | Project speed **0×** while injured (can still be reassigned after 10 days on the project) |
| Facility damaged | All progress paused until repaired |
| Your facility captured while researching | Project progress lost by up to **−20%** |
| You capture an enemy facility researching a project you have not completed and they are further along | You gain **20% of the progress difference**; reduced by **60%** each subsequent time for the same project |

**Cancelling:** a project can be cancelled at any time but takes **10 days** to actually stop. During those 10 days the facility still consumes the project's resources, is still capturable, and cannot start a new project. Projects can be resumed later and keep both the current prototype's progress and overall progress.

---

## Scientists

### Hiring

| Scientist | Political power cost |
|---|---|
| 1st | 25 |
| 2nd | 50 |
| 3rd | 75 |
| 4th and every later one | 100 |

- Recruited from the special projects section of the research screen, even with no facilities built.
- Recruiting shows **one randomly generated scientist per category** (Nuclear Research, Naval Engineering, Aerodynamics and Avionics, Land Warfare).
- Each generated scientist has a **35% chance of a random trait**. New recruits start at **skill 1**.
- Scientists **cannot die**. They can only be dismissed through specific prototype outcome choices.

### Skill

| Level | Name | Experience to reach | Daily breakthrough progress (basic research) | Research speed to associated technologies | Special project speed |
|---|---|---|---|---|---|
| 0 | Inadequate | – | 0% | 0% | 0× |
| 1 | Inexperienced | 100 | +0.05% | +2% | 0.95× |
| 2 | Skilled | 100 | +0.1% | +4% | 1.05× |
| 3 | Experienced | 300 | +0.15% | +6% | 1.1× |
| 4 | Expert | 700 | +0.2% | +8% | 1.15× |
| 5 | Mastermind | 1500 | +0.25% | +10% | 1.25× |

### Experience gain

- Pursuing a project: experience from prototype iterations (commonly +70, +100, +150 or +200 from outcomes), plus a flat **+192 experience on completing any special project**.
- Basic research: **+0.28 experience per day**.

### Traits

Field-specific traits use medal icons; generic traits (available to any scientist) use magnifying-glass icons.

| Trait | Specialization | Effect | Notes |
|---|---|---|---|
| Genius | generic | Special project research speed 1.10×; daily breakthrough progress from passive research 1.05×; research speed bonus from passive research 1.05× | |
| Brilliant Theorist | generic | Special project research speed 1.05×; daily breakthrough progress from passive research 1.02× | |
| Gifted Engineer | generic | Special project research speed 1.05×; research speed bonus from passive research 1.02× | |
| Bright | generic | Special project research speed 1.05×; scientist experience gain +5% | |
| Fast Learner | generic | Scientist experience gain +10% | |
| Resourceful | generic | Special project facility supply consumption −10% | |
| Schrödinger's Trait | generic | Scientist experience gain +10% and −10% | Purely flavour — the modifiers are only visual |
| Aircraft Specialist | Aerodynamics and Avionics | Aircraft special project research speed 1.05× | |
| Rocket Specialist | Aerodynamics and Avionics | Rocket special project research speed 1.05× | |
| Electronics Specialist | Aerodynamics and Avionics | Radar special project research speed 1.05× | |
| Helicopter Expert | Aerodynamics and Avionics | Helicopter special project research speed 1.15× | Only with Götterdämmerung |
| Jet Expert | Aerodynamics and Avionics | Jet special project research speed 1.10× | |
| Bombs Expert | Aerodynamics and Avionics | Bombs special project research speed 1.10× | Only with Götterdämmerung |
| Guidance Systems Expert | Aerodynamics and Avionics | Guided bomb special project research speed 1.10× | |
| Armored Specialist | Land Warfare | Tank special project research speed 1.05× | |
| Artillery Specialist | Land Warfare | Artillery special project research speed 1.05× | Only with No Step Back or Götterdämmerung |
| Submarine Specialist | Naval Engineering | Submarine special project research speed 1.05× | |
| Surface Ship Specialist | Naval Engineering | Surface ship special project research speed 1.05× | |
| Nuclear Specialist | Nuclear Research | Nuclear special project research speed 1.05× | |
| Nuclear Warfare Expert | Nuclear Research | Nuclear warfare special project research speed 1.10× | |
| Nuclear Power Expert | Nuclear Research | Nuclear power special project research speed 1.10× | |

**Injury:** certain prototype outcomes injure the active scientist temporarily (commonly 30 or 60 days). An injured scientist contributes **no** project progress.

### Tasks

- **Basic research** — generates daily breakthrough progress by skill, and adds research speed to technologies in the scientist's field (identified by the coloured ribbon on the technology icon). With multiple scientists on basic research in the same field, **both** effects are multiplied by 0.5× for each scientist beyond the first.
- **Researching a special project** — see above.

### Predefined scientists by country

| Country | Name | Specialization | Skill | Traits | Unlock requirement |
|---|---|---|---|---|---|
| Austria | Herbert Wagner | Aerodynamics and Avionics | 3 | Guidance Systems Expert | Recruiting from the University or Royal Scientific Grants |
| Austria | Eugen Sanger | Aerodynamics and Avionics | 2 | Jet Expert | Recruiting from the University |
| Austria | Hedy Lamarr | Naval Engineering | 1 | Submarine Specialist, Fast Learner | Women's Education Initiative |
| Austria | Egon Schweidler | Nuclear Research | 2 | Nuclear Power Expert, Bright | Recruiting from the University |
| Austria | Paul Eisler | Aerodynamics and Avionics | 2 | Electronics Specialist | Royal Scientific Grants |
| Belgium | Nicholas Florine | Aerodynamics and Avionics | 2 | Helicopter Expert | – |
| Belgium | Karel Bossart | Aerodynamics and Avionics | 2 | Rocket Specialist | – |
| Belgium | Georges Lemaître | Nuclear Research | 2 | Nuclear Specialist | – |
| Belgium | Alfred Renard | Aerodynamics and Avionics | 2 | Aircraft Specialist | Renard Constructions Aéronautiques |
| Belgium | Auguste Piccard | Naval Engineering | 2 | Submarine Specialist | – |
| British Raj | Homi J. Bhabha | Nuclear Research | 2 | Nuclear Specialist | – |
| China | Wang Ganchang | Nuclear Research | 2 | Nuclear Specialist | – |
| Denmark | Niels Bohr | Nuclear Research | 3 | Nuclear Specialist, Bright | Expand Institut for Teoretisk Fysik |
| Dominion of Canada | George Volkoff | Nuclear Research | 2 | Nuclear Specialist | – |
| France | Irène Joliot-Curie | Nuclear Research | 2 | Nuclear Specialist, Bright | – |
| France | Frédéric Joliot-Curie | Nuclear Research | 2 | Nuclear Power Expert | – |
| France | François Hussenot | Aerodynamics and Avionics | 2 | Aircraft Specialist | – |
| France | Louis Renault | Land Warfare | 2 | Armored Specialist | – |
| France | Émile Rimailho | Land Warfare | 2 | Artillery Specialist, Fast Learner | – |
| France | Eugène Schneider II | Land Warfare | 2 | Artillery Specialist, Resourceful | – |
| France | Henri-Edmond Fouché | Naval Engineering | 2 | Surface Ship Specialist | – |
| France | Joseph Bethenod | Aerodynamics and Avionics | 2 | Electronics Specialist | – |
| German Reich | Werner Heisenberg | Nuclear Research | 2 | Nuclear Specialist, Bright | – |
| German Reich | Peter Adolf Thiessen | Nuclear Research | 1 | Nuclear Warfare Expert, Brilliant Theorist | – |
| German Reich | Gustav Ludwig Hertz | Nuclear Research | 1 | Nuclear Power Expert, Fast Learner | – |
| German Reich | Eduard Grote | Land Warfare | 2 | Armored Specialist | – |
| German Reich | Karl Heinrich Emil Becker | Land Warfare | 2 | Artillery Specialist, Fast Learner | – |
| German Reich | Hermann Burkhardt | Naval Engineering | 2 | Surface Ship Specialist | – |
| German Reich | Ulrich Gabler | Naval Engineering | 2 | Submarine Specialist | – |
| German Reich | Hellmuth Walter | Naval Engineering | 2 | Submarine Specialist, Bright | – |
| German Reich | Wernher von Braun | Aerodynamics and Avionics | 3 | Rocket Specialist, Brilliant Theorist | – |
| German Reich | Hans von Ohain | Aerodynamics and Avionics | 2 | Jet Expert | – |
| German Reich | Max Kramer | Aerodynamics and Avionics | 2 | Guidance Systems Expert | – |
| German Reich | Kurt Tank | Aerodynamics and Avionics | 2 | Aircraft Specialist, Fast Learner | – |
| German Reich | Henrich Focke | Aerodynamics and Avionics | 2 | Helicopter Expert, Bright | – |
| German Reich | Manfred von Ardenne | Aerodynamics and Avionics | 2 | Electronics Specialist, Fast Learner | – |
| German Reich | Konrad Zuse | Aerodynamics and Avionics | 1 | Electronics Specialist, Bright | – |
| Hungary | György Jendrassik | Aerodynamics and Avionics | 2 | Jet Expert | – |
| Hungary | Nicholas Straussler | Land Warfare | 2 | Armored Specialist | – |
| Hungary | Oszkár Asboth | Aerodynamics and Avionics | 1 | Helicopter Expert | – |
| Hungary | Leó Szilárd | Nuclear Research | 2 | Nuclear Power Expert | Guarantee Religious Liberties or Reverse the Brain Drain |
| Hungary | John von Neumann | Nuclear Research | 2 | Nuclear Specialist | Guarantee Religious Liberties or Reverse the Brain Drain |
| Hungary | Edward Teller | Nuclear Research | 2 | Nuclear Warfare Expert | Guarantee Religious Liberties or Reverse the Brain Drain |
| Hungary | László Varga | Aerodynamics and Avionics | 2 | Aircraft Specialist | Develop László Varga's Design |
| Ireland | Ernest Walton | Nuclear Research | 2 | Nuclear Specialist | – |
| Italy | Enrico Fermi | Nuclear Research | 3 | Nuclear Specialist, Gifted Engineer | Meritocracy or Bring Back Exiled Intellectuals |
| Italy | Gaetano Crocco | Aerodynamics and Avionics | 2 | Rocket Specialist | – |
| Italy | Robert Longhi | Aerodynamics and Avionics | 2 | Jet Expert, Gifted Engineer | – |
| Italy | Mario Castoldi | Aerodynamics and Avionics | 2 | Aircraft Specialist | – |
| Italy | Giovanni Giorgi | Aerodynamics and Avionics | 2 | Electronics Specialist | – |
| Italy | Filippo Bonfiglietti | Naval Engineering | 2 | Surface Ship Specialist | – |
| Italy | Curio Bernardis | Naval Engineering | 2 | Submarine Specialist, Bright | – |
| Japan | Isoroku Yamamoto | Naval Engineering | 2 | Submarine Specialist | – |
| Japan | Yoshio Nishina | Nuclear Research | 2 | Nuclear Specialist | – |
| Japan | Hideo Itokawa | Aerodynamics and Avionics | 2 | Rocket Specialist | – |
| Japan | Kijirō Nambu | Land Warfare | 2 | Armored Specialist | – |
| Japan | Keiji Fukuda | Naval Engineering | 2 | Surface Ship Specialist | – |
| Japan | Jiro Horikoshi | Aerodynamics and Avionics | 2 | Aircraft Specialist | Complete the "Agility Focus" focus |
| Japan | Hideki Yukawa | Nuclear Research | 2 | Nuclear Power Expert | – |
| Japan | Yoji Ito | Aerodynamics and Avionics | 2 | Electronics Specialist | – |
| Netherlands | Anthony Fokker | Aerodynamics and Avionics | 2 | Aircraft Specialist, Gifted Engineer | – |
| Persia | Kazem Hasibi | Aerodynamics and Avionics | 1 | Electronics Specialist, Fast Learner | Establish Tehran University |
| Persia | Ahmad Zirakzadeh | Naval Engineering | 2 | Bright | Increase Staffing Budget |
| Soviet Union | Igor Kurchatov | Nuclear Research | 2 | Nuclear Specialist, Fast Learner | – |
| Soviet Union | Abram Ioffe | Nuclear Research | 2 | Nuclear Power Expert | – |
| Soviet Union | Sergey Korolyov | Aerodynamics and Avionics | 2 | Rocket Specialist, Gifted Engineer | – |
| Soviet Union | Boris Stechkin | Aerodynamics and Avionics | 2 | Jet Expert, Brilliant Theorist | – |
| Soviet Union | Arkady Nazarov | Aerodynamics and Avionics | 2 | Aircraft Specialist, Fast Learner | – |
| Soviet Union | Vladimir Kotelnikov | Aerodynamics and Avionics | 2 | Electronics Specialist | – |
| Sweden | Lise Meitner | Nuclear Research | 2 | Nuclear Specialist | – |
| Turkey | Vecihi Hürkuş | Aerodynamics and Avionics | 2 | Aircraft Specialist, Resourceful | – |
| United Kingdom | James Chadwick | Nuclear Research | 2 | Nuclear Warfare Expert | – |
| United Kingdom | Frank Whittle | Aerodynamics and Avionics | 2 | Jet Expert, Bright | – |
| United Kingdom | John Cockcroft | Nuclear Research | 2 | Nuclear Power Expert | – |
| United Kingdom | Charles Goodeve | Naval Engineering | 2 | Surface Ship Specialist | – |
| United Kingdom | Nevil Shute | Aerodynamics and Avionics | 2 | Aircraft Specialist, Gifted Engineer | – |
| United Kingdom | Robert Watson Watt | Aerodynamics and Avionics | 2 | Electronics Specialist | – |
| United States | Robert Oppenheimer | Nuclear Research | 2 | Nuclear Specialist, Brilliant Theorist | – |
| United States | Robert H. Goddard | Aerodynamics and Avionics | 3 | Rocket Specialist, Bright | – |
| United States | Leslie Skinner | Aerodynamics and Avionics | 2 | Rocket Specialist, Gifted Engineer | – |
| United States | Edward Curtis Wells | Aerodynamics and Avionics | 2 | Aircraft Specialist | – |
| United States | William Francis Gibbs | Naval Engineering | 2 | Surface Ship Specialist | – |
| United States | Andrew McKee | Naval Engineering | 2 | Submarine Specialist | – |
| United States | John Walter Christie | Land Warfare | 2 | Armored Specialist, Gifted Engineer | – |
| United States | Vannevar Bush | Aerodynamics and Avionics | 2 | Electronics Specialist | – |

---

## Project list

"Cost" is the number of breakthroughs needed to start. "Days" is the length of one prototype iteration; "Progress" is the range of project progress each prototype adds.

### Nuclear Research projects

| Project | Historical names | Prerequisites | Break. | Resources | Traits that help | Days | Progress | Completion effects |
|---|---|---|---|---|---|---|---|---|
| Nuclear Reactor | UK Tube Alloys; France EL-1; USSR F-1; USA Pile-1; Germany Uranmaschine; Sweden R1; Belgian Congo TRIGA 1; Belgium BR1; South Africa Koeberg; Japan F-Go; Poland MSC-1 | Atomic research | 1 | Steel 8, Tungsten 2, Chromium 2 | Nuclear Specialist, Nuclear Power Expert | 90 | 10–15% | Per the Reactor Design outcome, either: unlock Nuclear Reactor construction + a free Nuclear Reactor in the facility's state; or unlock Heavy Water Nuclear Reactor + a free one in that state. Extra effects via the Isotope Separation Facilities and First Successful Nuclear Reactor Test outcomes |
| Commercial Nuclear Reactor | Sweden Civila Kärnkraftprogrammet | Götterdämmerung; Nuclear Reactor; Construction IV | 1 | Steel 6, Tungsten 4, Chromium 7 | Nuclear Specialist, Nuclear Power Expert | 90 | 10–15% | Unlock Civilian Nuclear Reactor construction; remove any Nuclear/Heavy Water reactor in the facility's state; free Civilian Nuclear Reactor there. Extra via the Concerns Over Nuclear Safety outcome |
| Nuclear Engines | – | Götterdämmerung; Commercial Nuclear Reactor | 1 | Steel 4, Tungsten 2, Chromium 5 | Nuclear Specialist, Nuclear Power Expert | 90 | 15–20% | Unlock Nuclear Submarine Reactor, Nuclear Heavy Ship Reactor, Nuclear Carrier Reactor ship modules |
| Nuclear Fission Bomb Project | USA The Manhattan Project; USSR RDS-1; UK High Explosive Research; Communist China Project 596; British Raj Smiling Buddha; Pakistan Chagai-I; Sweden Kärnvapenprogrammet; South Africa Hamerkop; Poland Projekt Polonium; Japan Jin Project | Nuclear Reactor | 1 | Steel 2, Tungsten 8, Chromium 2 | Nuclear Specialist, Nuclear Warfare Expert | 90 | 10–15% | +1 nuclear bomb; unlock the hidden Nuclear Bombs technology (nuclear bomb production +0.5). As the USA at war with Japan, plays "A Warning to Japan". Extra via Prototype Bomb, Espionage Threats, Information Leak |
| Thermonuclear Bomb | USSR RDS-6S; USA Ivy Mike; UK Green Granite; Poland The Ulam Device | Götterdämmerung; Nuclear Fission Bomb Project | 1 | Steel 2, Tungsten 10, Chromium 3 | Nuclear Specialist, Nuclear Warfare Expert | 90 | 5–10% | Unlock the hidden Thermonuclear Bombs technology (thermonuclear bomb production +1) |
| Nuclear Warheads | – | Götterdämmerung; Nuclear Fission Bomb Project; MRBM | 1 | Aluminium 4, Tungsten 4, Chromium 2 | Nuclear Specialist, Nuclear Warfare Expert | 90 | 10–15% | Unlock Medium Range Nuclear Missile |

### Naval Engineering projects

| Project | Historical names | Prerequisites | Break. | Resources | Traits that help | Days | Progress | Completion effects |
|---|---|---|---|---|---|---|---|---|
| Cruiser Submarine | – | Early Submarine Hull | 1 | Steel 8 | Submarine Specialist | 60 | 15–20% | Unlock Cruiser Submarine Hull; ×1 −100% design cost for it. Extra via Raiding Protocol |
| Fleet Submarine | – | Cruiser Submarine; 1936 Submarine Hull | 1 | Steel 12, Chromium 4 | Submarine Specialist | 90 | 15–20% | Unlock Fleet Submarine Hull; ×1 −100% design cost. Extra via Design Principles |
| Nuclear Submarine | USA USS Nautilus; UK HMS Dreadnought; USSR Project 627 K-3 | Götterdämmerung; Fleet Submarine; Nuclear Engines | 3 | Steel 20, Chromium 8, Tungsten 8 | Submarine Specialist, Nuclear Power Expert | 90 | 5–10% | Unlock Nuclear Submarine Hull; ×1 −100% design cost. Extra via Cost Concerns |
| Missile Launching Submarine | Japan I-400-class; USSR Project 611; Communist China Type 094 Jin | Götterdämmerung; Fleet Submarine; Ballistic Missile | 2 | Steel 12, Chromium 4, Tungsten 12 | Submarine Specialist, Rocket Specialist | 90 | 15–20% | Unlock Submarine Missile Launcher module. Extra via Question of Payload Delivery |
| Nuclear Missile Submarine | British Raj Arihant-class; France Triomphant-class; USA George Washington-class; Korea KSS-III; UK Resolution-class | Götterdämmerung; Nuclear Submarine; Missile Launching Submarine | 2 | Steel 16, Chromium 16 | Submarine Specialist, Nuclear Warfare Expert | 180 | 10–15% | Unlock Submarine Nuclear Missile Launcher module. Extra via Escaping the Hunt |
| Nuclear Torpedo | – | Götterdämmerung; Nuclear Submarine; Modern Ship Torpedo Launcher | 1 | Steel 8, Chromium 12, Tungsten 12 | Submarine Specialist, Nuclear Warfare Expert | 90 | 10–15% | Unlock Nuclear Torpedo module. Extra via New Torpedo Course |
| Midget Submarine | – | Early Submarine Hull | 1 | Steel 6 | Submarine Specialist | 45 | 10–15% | Unlock Midget Submarine Hull; ×1 −100% design cost. Extra via Squeezing in More |
| Air-Independent Propulsion | – | Götterdämmerung; 1936 Submarine Hull | 2 | Steel 8, Chromium 8 | Submarine Specialist, Surface Ship Specialist | 60 | 10–15% | Unlock Air-Independent Propulsion module; prerequisite for AIP-Diesel Combination Engines technology. Extra via Independent Improvements |
| Anechoic Tiles | – | Götterdämmerung; 1936 Submarine Hull | 1 | Rubber 12, Steel 8 | Submarine Specialist | 60 | 15–20% | Unlock Anechoic Tiles module. Extra via New Learnings – Submarine Hull Construction |
| Torpedo Cruiser | Japan Long-Lance Cruiser Integration | Early Cruiser Hull | 1 | Steel 8, Tungsten 2, Chromium 2 | Surface Ship Specialist | 60 | 15–25% | Unlock Torpedo Cruiser Hull; ×1 −100% design cost. Extra via Second Chance – Torpedo Cruiser |
| Super Heavy Battleship | Japan Yamato-class; USA Montana-class; UK Jellicoe-class; Poland Orkan-class | Early Heavy Ship Hull | 1 | Steel 12, Chromium 6, Tungsten 6 | Surface Ship Specialist | 60 | 15–20% | Unlock Super Heavy Battleship Hull and Super-Heavy Armor ship module; ×1 −100% design cost. Extra via Matter of Priorities (Attack / Defense) |
| Modern Battleship | Poland Huragan-class | Götterdämmerung; 1944 Heavy Ship Hull | 2 | Steel 24, Chromium 18, Tungsten 12 | Surface Ship Specialist | 90 | 10–15% | Unlock Modern Battleship Hull; ×1 −100% design cost. Extra via Modern Battleship – Hope / Strikes Back! |
| Modern Carrier | – | Götterdämmerung; 1944 Carrier Hull | 2 | Steel 24, Chromium 16 | Surface Ship Specialist | 90 | 10–15% | Unlock Modern Carrier Hull; ×1 −100% design cost. Extra via Modern Carrier – Purpose / Safety |
| Ice Aircraft Carrier | UK / USA / Canada Project Habakkuk | Götterdämmerung; 1940 Carrier Hull | 2 | Steel 32 | Surface Ship Specialist | 180 | 10–15% | Unlock Ice Carrier Hull, Floating Airfield Runway and Pykrete Runway Reinforcements modules; prerequisite for Refined Pykrete technology; ×1 −50% design cost; creates an Ice Carrier Hull variant and one production line of it at 95% completion. Extra via Reinforcing Ice-Aircraft Carrier |
| Underway Replenishment | – | Götterdämmerung; Base Strike **or** Fleet In Being | 2 | Steel 8 | Surface Ship Specialist | 60 | 10–15% | Unlock Underway Replenishment for all naval task forces; prerequisite for Multi-Product Supply Ship technology. Extra via Scale of Resupply |
| Proximity Fuze | – | Götterdämmerung; Improved Radio | 2 | Steel 12, Chromium 4, Tungsten 12 | Surface Ship Specialist | 90 | 10–15% | Naval anti-air +25%; prerequisite for Shock-Hardening Techniques technology. Extra via Efficiency or Effectiveness |
| Escort Carrier | – | No Compromise, No Surrender; Basic Carrier | 1 | Steel 9 | Surface Ship Specialist | 60 | 15–20% | _Not listed on the wiki._ |
| Submarine Carrier | – | No Compromise, No Surrender; Basic Carrier; Improved Submarine | 2 | Steel 12, Chromium 6 | Submarine Specialist | 60 | 10–15% | _Not listed on the wiki._ |
| Support Ships | – | No Compromise, No Surrender; Transports | 1 | Steel 6 | Surface Ship Specialist | 60 | 15–20% | _Not listed on the wiki._ |

### Aerodynamics and Avionics projects

| Project | Historical names | Prerequisites | Break. | Resources | Traits that help | Days | Progress | Completion effects |
|---|---|---|---|---|---|---|---|---|
| Bouncing Bomb | – | Götterdämmerung; with By Blood Alone: Heavy Bombs. Without BBA: Tactical Bomber II or Strategic Bomber II | 1 | Steel 4, Aluminium 4, Rubber 2 | Bombs Expert, Aircraft Specialist | 60 | 15–20% | Unlock Dam Bombing Raid and Lock Bombing Raid |
| Earthshaker Bomb | – | Götterdämmerung; with BBA: Heavy Bombs. Without BBA: Strategic Bomber II | 1 | Steel 4, Tungsten 8 | Bombs Expert, Aircraft Specialist | 90 | 15–20% | Unlock Mega-Gun Emplacement Strike; with BBA also the Earthshaker Bomb Release Mechanism module. Extra via Design Direction |
| Intercontinental Bomber | Germany Amerikabomber | Götterdämmerung; with BBA: Improved Large Airframe. Without BBA: Strategic Bomber II | 2 | Aluminium 24, Rubber 12 | Aircraft Specialist | 180 | 10–15% | Unlock Intercontinental Bomber. As Germany having completed Amerikabomber with Focke-Wulf as project lead: Intercontinental Bomber max speed +10%, production cost +5%, Focke-Wulf MIO research bonus +15% (reversing the project's penalty), and the Amerikabomber Learnings MIO trait (medium planes range +10%). Extra via Long-Range Delivery |
| Mothership Aircraft | – | Götterdämmerung; with BBA: Improved Large Airframe. Without BBA: Strategic Bomber II | 2 | Aluminium 18, Rubber 8 | Aircraft Specialist | 90 | 15–20% | Prerequisite for Reinforced Mothership Wings technology; unlock Mothership Aircraft. Extra via Peak Mothership Performance |
| Jet Engine | Japan Ishikawajima Ne-20 | With BBA: Engines II + (Improved Small Airframe or Improved Medium Airframe). Without BBA: Fighter II or Tactical Bomber II | 3 | Chromium 12, Aluminium 4, Steel 2 | Jet Expert, Aircraft Specialist | 90 | 10–15% | With BBA: unlock 1x/2x/3x/4x/6x Jet Engine modules; ×1 −75% and ×1 −50% aircraft design cost. Without BBA: prerequisite for Jet Fighter I and Jet Tactical Bomber I. With Götterdämmerung: prerequisite for Centrifugal Jet. With No Step Back: unlock Gas Turbine tank module. Extra via Development Priority |
| Axial Jet Engine | – | Jet Engine; with BBA: Engines III + (Advanced Small or Advanced Medium Airframe). Without BBA: Jet Fighter I or Jet Tactical Bomber I | 2 | Chromium 12, Aluminium 4, Steel 2 | Jet Expert, Aircraft Specialist | 90 | 10–15% | With BBA: unlock 1x/2x/3x/4x/6x Axial Jet Engine modules; ×1 −75% and ×1 −50% aircraft design cost; prerequisite for Modern Small/Medium/Large Airframe. Without BBA: prerequisite for Jet Fighter II, Jet Tactical Bomber II, Jet Strategic Bomber I. Extra via Development Déjà Vu |
| Supersonic Jet | – | Götterdämmerung; Axial Jet Engine | 2 | Aluminium 24, Chromium 16, Rubber 8 | Jet Expert, Aircraft Specialist | 90 | 10–15% | With BBA: unlock Supersonic Small Airframe, ×1 −100% design cost. Without BBA: unlock Supersonic Fighter. Extra via Cost Concerns |
| Helicopter | – | Götterdämmerung | 2 | Aluminium 12, Steel 8 | Helicopter Expert, Aircraft Specialist | 90 | 15–20% | Prerequisite for Helicopter Recon / Med-Evac / Transport Company technologies; unlock Helicopter equipment and the Helicopter Brigade support company; with No Step Back also the Helipad land cruiser module. Extra via Safety Concerns |
| Radar | Poland Codename 'Hejnał' | Electronic Mechanical Engineering | 1 | Steel 6, Aluminium 6 | Electronics Specialist | 60 | 15–20% | Unlock the hidden Radio Detection technology (Radar Station construction, coordination +1%); prerequisite for Cavity Magnetron; free level-1 Radar Station in the facility's state; with Götterdämmerung + No Step Back also the Radar land cruiser module and Radar I ship module |
| Flying Bomb | Germany The V1 Project; Japan MXY-7 Ohka; USA Bomb MK 57 | Experimental Rockets | 2 | Steel 8, Aluminium 8, Tungsten 2 | Guidance Systems Expert, Rocket Specialist | 60 | 15–20% | Prerequisite for Improved Guidance and Rocket Propelled Bombs technologies; unlock Basic Guided Missile. Extra via Range versus Payload? |
| Ballistic Missile | Germany The V2 Project; USA PGM-11 Redstone; France SE4200; Communist China Dong-Feng 15; British Raj Prithvi; Persia Naze'at; Iraq Al Fat'h; Israel Jericho I; Korea Hwasong; Pakistan Hatf-I; Yugoslavia/Serbia Šumadija; USSR R-1; China Sky Spear; Turkey J-600T Yıldırım I; Ukraine Hrim-2; Yemen Qaher-1 | Experimental Rockets | 3 | Steel 9, Aluminium 9, Chromium 9 | Rocket Specialist | 60 | 10–15% | With Götterdämmerung: unlock Basic Ballistic Missile. Without: unlock Improved Guided Missile. Extra via Guidance System |
| MRBM | Communist China Dong-Feng 16; France SSBS S1; British Raj Agni-Prime; Persia Ghadr-110; Iraq Badr-2000; Israel Jericho II; Korea Pukguksong; Pakistan Ababeel; Turkey Cenk; USSR RT-15; USA PGM-19 Jupiter | Ballistic Missile | 1 | Steel 12, Aluminium 9, Chromium 9 | Rocket Specialist | 60 | 10–15% | With Götterdämmerung: unlock Medium Range Ballistic Missile. Without: unlock Advanced Guided Missile |
| ICBM | Israel Jericho III; British Raj Agni-V; USA Minuteman; USSR R-16; Communist China Dong Feng 31 | Götterdämmerung; MRBM; Nuclear Warheads | 1 | Steel 12, Aluminium 12, Chromium 12 | Rocket Specialist, Nuclear Warfare Expert | 60 | 10–15% | Unlock Intercontinental Nuclear Missile. Extra via Launch Site Issues |
| Surface to Air Missiles | Germany Wasserfall; Japan Funryū; Communist China Hóng Qí; France Crotale; Greece Aris; British Raj Akash; Persia Sayyad; Iraq Al Arq; Israel Iron Dome; Italy Aster; British Burma GYD-1B; Romania CA-95; South Africa Umkhonto; Sweden BAMSE; Switzerland RSA; China Sky Bow; Turkey HİSAR; Ukraine Dnipro; UK Bristol Bloodhound; USA Avenger; USSR S-25 Berkut; Yugoslavia R-25 Vulkan; Korea KN-06 | Götterdämmerung; Ballistic Missile | 2 | Steel 6, Aluminium 9, Tungsten 6 | Guidance Systems Expert, Rocket Specialist | 60 | 10–15% | Unlock Surface to Air Missile I |
| Rocket Interceptor | Germany Me 163 Komet; Poland PZL Bielik; Japan Mitsubishi J8M Shūsui | Experimental Rockets | 1 | Tungsten 6, Aluminium 12, Chromium 6 | Rocket Specialist | 60 | 10–15% | Prerequisite for Dual Chamber Rocket Engines. With BBA: unlock Rocket Engine I module and create an Improved Small Airframe variant using it. Without BBA: unlock Rocket Interceptor I |

### Land Warfare projects

| Project | Historical names | Prerequisites | Break. | Resources | Traits that help | Days | Progress | Completion effects |
|---|---|---|---|---|---|---|---|---|
| Flamethrower Tank | Germany Flammpanzer; Italy Lancia Fiamme; Japan Sōkō Sagyō Ki 'Otsu'; USA M3 Satan; Canada Ram Badger; USSR KhT-133; UK Ronson Flamethrower; Sweden Nidhögg; Iceland Níðhöggr; Poland Wawel Dragon | No Step Back; Engineer Company I | 1 | – | Armored Specialist | 45 | 15–25% | Unlock Flamethrower tank module; ×1 −100% and ×2 −50% design cost for Light/Medium/Heavy Flame Tank; unlock Light/Medium/Heavy Flame Tank Company support companies; prerequisite for Advanced Flamethrower. With Götterdämmerung: Flamethrower Turret land cruiser module. As Italy having completed Italian Tankettes: creates the L3 Lf Basic Light Flame Tank variant |
| Military Engineering Vehicles | UK Hobart's Funnies; Japan Sōkō Sagyō Ki; Austria SB-20 Greif; Argentina TAM VCRT; Canada Ram ARV; USSR Inzhenernaya Mashina Razgrashdeniya | Engineer Company I | 1 | – | Armored Specialist | 45 | 15–25% | Unlock Armored Support Vehicle equipment and Assault Engineer Company; prerequisite for Armored Engineer Company, Motorized Military Police, Armored Maintenance Company and Armored Signal Company. With Götterdämmerung: creates an Armored Support Vehicle variant for the country |
| Land Cruiser | Germany Landkreuzer P. 1000 Ratte; USA T28 Super-Heavy Tank; UK Flying Elephant; Japan O-II Super-Heavy Tank; New Zealand Bigger Bob | Götterdämmerung; with No Step Back: Super-Heavy Tank Chassis. Without NSB: Super Heavy Tank | 3 | Steel 16, Chromium 8 | Armored Specialist | 60 | 5–10% | Prerequisite for Naval Engine Conversion, Transmission Improvements, Specialized Field Manuals; unlock Land Cruiser support company. With NSB: Land Cruiser Chassis, ×1 −100% design cost, prerequisite for High-Impact Obliterator Cannon, and the Heavy Naval Guns, Medium Naval Guns, Super-Heavy Howitzer, Aircraft Catapult, Internal Fuel Tanks, Internal Ammunition Compartments, Wet Ammunition Storage, Smoke Generators and Stabilizers land cruiser modules. Without NSB: unlock Land Cruiser, add 1 Land Cruiser and 1 production line at 35% completion. Many outcomes possible |
| Super-Heavy Howitzer | Austria 42 cm Haubitze M. 14/16; Belgium Mortier Monstre; USA M115 203 mm Howitzer | Götterdämmerung; Towed Artillery | 2 | Steel 8, Tungsten 4 | Artillery Specialist | 45 | 15–20% | Unlock Super-Heavy Artillery support company and Super-Heavy Howitzer equipment; prerequisite for Rocket-Assisted Projectiles. Extra via Design Focus |
| Self-Propelled Super-Heavy Howitzer | Iraq Al-Fao; South Africa G6 Rhino; USSR 2A3 Kondensator 2P | Götterdämmerung; Super-Heavy Howitzer; Military Engineering Vehicles | 2 | Steel 8, Tungsten 6, Chromium 2 | Artillery Specialist | 60 | 15–20% | Unlock Self-Propelled Super-Heavy Artillery support company and Self-Propelled Super-Heavy Howitzer equipment; prerequisite for Purpose-Built Gun Motor Carriages. Extra via Design Focus |
| Super-Heavy Railway Gun | Japan 41H Experimental Howitzer; Germany Schwerer Gustav; UK Boche Buster | No Step Back; Railway Gun | 1 | Steel 16, Tungsten 8, Chromium 8 | Artillery Specialist | 90 | 15–20% | Unlock Super-Heavy Railway Gun and add 1 (named **Dora** as the German Reich). With Götterdämmerung: Super-Heavy Railway Gun land cruiser module |
| Multi-Charge Large Caliber Gun | Germany V3; Iraq Project Babylon; Canada/USA Project HARP; UK Little David | Götterdämmerung; Super-Heavy Howitzer | 1 | Steel 6, Tungsten 4, Chromium 2 | Artillery Specialist | 60 | 15–25% | Unlock construction of the Multi-Charge Large Caliber Gun building |
| Stronghold Network | – | Götterdämmerung; Basic Fortification | 2 | Steel 4, Chromium 2, Tungsten 1 | Artillery Specialist | 60 | 10–15% | Unlock construction of the Stronghold Network building. Extra via Breakthrough in Concrete Reinforcement |
| Large Caliber Kinetic Energy Sabot | – | Peace for Our Time; Towed Anti-Tank | 1 | Steel 2, Chromium 4, Tungsten 2 | Artillery Specialist | 45 | 15–25% | _Not listed on the wiki._ |

---

## Prototype outcomes

Each finished prototype can fire an outcome. Outcomes are drawn by weighted random chance and gated by minimum/maximum project progress. Repeatable outcomes can fire more than once per project.

### Nuclear Research outcomes

| Outcome | Eligible projects | Min | Max | Weight | Effect | Repeat |
|---|---|---|---|---|---|---|
| Isotope Separation Facilities | Nuclear Reactor | 0% | 20% | 1000 | Choice: nothing; or unlock the hidden Centrifugal Isotope Separation technology (Nuclear Fission Bomb Project speed +5%, Thermonuclear Bomb speed +5%, nuclear bomb production rate +50%) plus the Secret Resource Procurement spirit for 365 days (consumer goods factory factor +10%) | No |
| Reactor Design | Nuclear Reactor | 25% | 45% | 1000 | Choice: the country will use Nuclear Reactors; or Heavy Water Nuclear Reactors | No |
| First Successful Nuclear Reactor Test | Nuclear Reactor | 60% | 90% | 100 if first in the world, else 0 | Choice: nothing; or governing ideology popularity +10%, +100 political power, publicize findings (affects future outcome chances), and every other country gets Nuclear Reactor project progress +10% if they have Atomic research, otherwise a 1× 25% research bonus for Atomic research | No |
| Major Breakthrough in Nuclear Reactions | Nuclear Reactor | 10% | 50% | 1 | Project progress +10% | No |
| Concerns Over Nuclear Safety | Commercial Nuclear Reactor | 30% | 90% | 1 | Choice: ideology popularity +5%, +50 political power, project progress −10%, add filters (affects future outcomes); or ideology popularity −5% | No |
| Prototype Bomb | Nuclear Fission Bomb Project | 70% | 84% | 100 | Choice: project progress +10%; or +1 nuclear bomb | No |
| Espionage Threats | Nuclear Fission Bomb Project | 0% | 80% | 10 at war, else 1 | Choice: scientist experience +70 and low security (affects future outcomes); or project progress −5% and high security | No |
| Information Leak | Nuclear Fission Bomb Project | 30% | 100% | 0.2; ×0 if not at war; ×0.5 with high security; ×5 with low security; ×2 if findings were publicized | A random enemy country gains Nuclear Fission Bomb Project progress +10% within 8–12 hours | No |
| Breakthrough in Plutonium Production | Nuclear Fission Bomb Project | 20% | 60% | 0.5 with high security, else 1 | Project progress +5% | No |
| Test Proposal | Thermonuclear Bomb | 50% | 80% | 1000 with ≥5 nuclear bombs, else 0 | Choice: nothing; or (needs ≥1 nuclear bomb) −1 nuclear bomb and project progress +15% | No |
| Technological Advancements | Any | 0% | 100% | 1 | 1× 10% research bonus for Industry | Yes |
| New Learnings | Any | 0% | 100% | 1 | Scientist experience +70 | Yes |
| Minor Breakthrough | Any | 0% | 80% | 1 | Project progress +5% | Yes |
| Technological Innovation | Any | 0% | 100% | 1 | Random: 10% chance 1× 10%, 70% chance 1× 20%, 20% chance 1× 35% research bonus for Electronics | Yes |
| Public Support | Any | 50% | 100% | 1 | War support +2% | No |
| Major Political Interference | Any | 15% | 85% | 1 if Fascist, 0.25 otherwise | Choice: −50 political power, project progress −10%, scientist experience +100; or +50 political power, project progress −5%, and the active scientist is permanently dismissed | No |
| Empty Outcome | Nuclear Reactor | 0% | 100% | 1 | Nothing | Yes |
| Empty Outcome | Commercial Nuclear Reactor, Nuclear Engines, Nuclear Fission Bomb Project, Thermonuclear Bomb, Nuclear Warheads | 0% | 100% | 0.5 | Nothing | Yes |
| Theoretical Breakthrough | Nuclear Fission Bomb Project, Thermonuclear Bomb, Nuclear Warheads | 0% | 70% | 0.5 | Project progress +10%; scientist experience +100 | No |
| Critical Mass Experiment Goes Wrong | Nuclear Fission Bomb Project, Thermonuclear Bomb, Nuclear Warheads | 0% | 60% | 0.5 | Project progress −5%; scientist experience +70; facility damaged 25% | No |

### Naval Engineering outcomes

| Outcome | Eligible projects | Min | Max | Weight | Effect | Repeat |
|---|---|---|---|---|---|---|
| Raiding Protocol | Cruiser Submarine | 40% | 90% | 100 | Choice: unlock Fuel Tank ship module; or unlock 200mm Battery ship module | No |
| Design Principles | Fleet Submarine | 40% | 90% | 100 | Choice: speed +5%, torpedo attack +5%, sub visibility −3%; or reliability +5%, HP +5%, weather penalty −10% | No |
| Cost Concerns | Nuclear Submarine | 40% | 90% | 100 | Choice: production cost −10%, reliability −5%, sub visibility +10%, range −10%; or nothing; or production cost +10%, HP +10%, reliability +5%, sub visibility −5% | No |
| Question of Payload Delivery | Missile Launching Submarine | 40% | 90% | 100 | Choice (applies to Fleet Submarine): range +10%, sub visibility +5%, production cost +7%; or reliability +5%; or sub visibility −5%, range −5%, production cost +10% | No |
| Escaping the Hunt | Nuclear Missile Submarine | 40% | 90% | 100 | Choice (Nuclear Submarine): sub visibility −5%, surface detection +2%, cost +5%; or nothing; or HP +2%, weather penalty −20%, cost +5% | No |
| New Torpedo Course | Nuclear Torpedo | 40% | 90% | 100 | Choice: submarine torpedo hit chance +2%, torpedo attack +10%, reliability −10%; or reliability +10%, production cost +10% | No |
| Squeezing in More | Midget Submarine | 40% | 90% | 100 | Choice: range −20%, sub visibility −10%; or reliability +10%; or range +20%, sub visibility +10% | No |
| Independent Improvements | Air-Independent Propulsion | 40% | 90% | 100 | Choice: sub visibility −5%, fuel consumption +10%; or speed +10%, fuel consumption +10%; or fuel consumption −5% | No |
| New Learnings – Submarine Hull Construction | Anechoic Tiles | 40% | 90% | 100 | Choice: cost +5%, surface detection +10%; or cost +10%, sub visibility −5%; or cost −5% | No |
| Second Chance – Torpedo Cruiser | Torpedo Cruiser | 40% | 90% | 100 | Choice: torpedo hit chance +10%, torpedo attack +15%; or light gun hit chance +15%, light attack +10%, light piercing +10% | No |
| Matter of Priorities – Attack | Super Heavy Battleship | 10% | 50% | 100 | Choice: heavy gun hit chance +15%, heavy attack +15%, heavy piercing +10%; or speed +10%, surface detection +15%, surface visibility −5%; or light gun hit chance +10%, light attack +10%, light piercing +10% | No |
| Matter of Priorities – Defense | Super Heavy Battleship | 55% | 95% | 100 | Choice: armor +10%, HP +10%; or anti-air +25%, reliability +5%; or incoming torpedo crit chance −15%, incoming torpedo damage −15% | No |
| Modern Battleship – Hope | Modern Battleship | 10% | 50% | 100 | Choice: heavy gun hit chance +20%, heavy attack +15%, heavy piercing +15%; or speed +10%, surface detection +15%, surface visibility −7%; or light gun hit chance +10%, light attack +10%, light piercing +15% | No |
| Modern Battleship – Strikes Back! | Modern Battleship | 55% | 95% | 100 | Choice: armor +15%, HP +10%; or anti-air +25%, reliability +7%; or incoming torpedo crit chance −15%, incoming torpedo damage −20% | No |
| Modern Carrier – Purpose | Modern Carrier | 10% | 50% | 100 | Choice: surface detection +20%, sub detection +20%; or speed +10%, weather penalty −25%; or light gun hit chance +10%, light attack +15%, light piercing +15% | No |
| Modern Carrier – Safety | Modern Carrier | 55% | 95% | 100 | Choice: armor +15%, HP +10%; or anti-air +25%, reliability +7%; or incoming torpedo crit chance −15%, incoming torpedo damage −20% | No |
| Reinforcing Ice-Aircraft Carrier | Ice Aircraft Carrier | 55% | 95% | 100 | Choice: weather penalty −15%; or production cost +5%, HP +10% | No |
| Scale of Resupply | Underway Replenishment | 40% | 90% | 100 | Choice: range +20%, convoy cost +10%; or nothing; or range −10%, convoy cost −20% | No |
| Efficiency or Effectiveness | Proximity Fuze | 40% | 90% | 100 | Choice: anti-air production cost −5%; or anti-air air attack +15%, production cost +5% | No |
| Empty Outcome | Any | 0% | 100% | 1 | Nothing | Yes |
| Swimming in Ideas / Drowning in Creativity / Bathtub – Eureka! | Any | 0% | 100% | 2 (0.5 if a sibling already fired; 0 if scientist skill > 4) | Scientist experience +70 / +100 / +150 (the last also gives Naval Engineering breakthrough progress +10%) | No |
| Change in the Flow of Ideas / Wave of Ideas / Tsunami of Innovations! | Any | 50% | 100% | 2 (0.5 if a sibling already fired) | +15 / +30 / +50 navy experience (the last also gives Naval Engineering breakthrough progress +10%) | No |
| Major Breakthrough! / Great Success! / Massive Progress! | Any | 0% | 100% | 2 (0.5 if a sibling already fired) | Project progress +5% / +10% / +15%, each with scientist experience +70 (the last also gives Naval Engineering breakthrough progress +10%) | No |
| Project Delay! / Merely a Setback! / Disastrous Results | Any | 15% / 30% / 50% | 100% | 2 (0.5 if a sibling already fired) | Project progress −5% / −10% / −15%, each with scientist experience +70 (the last also gives Naval Engineering breakthrough progress +10%) | No |
| New Armor Studies / Naval Armor Innovations / Future Armor Insights | Torpedo Cruiser, Super Heavy Battleship, Modern Battleship, Modern Carrier | 0% | 100% | 2 (0.5 if a sibling already fired) | 1× 10% / 20% / 35% research bonus for Battleships, Battlecruisers, Naval Armor (the last also gives breakthrough progress +10%) | No |
| Ship Gunnery Learnings / Naval Guns Innovations / Ship Batteries Insights | Torpedo Cruiser, Super Heavy Battleship, Modern Battleship | 0% | 100% | 2 (0.5 if a sibling already fired) | 1× 10% / 20% / 35% research bonus for Naval Guns (the last also gives breakthrough progress +10%) | No |
| Contained Nuclear Accident | Nuclear Submarine, Nuclear Missile Submarine, Nuclear Torpedo | 0% | 100% | 200 | Facility damaged 25% | No |
| Torpedo Explosion | Cruiser Submarine, Fleet Submarine, Midget Submarine, Torpedo Cruiser | 0% | 100% | 2 | Facility damaged 15% | No |

### Aerodynamics and Avionics outcomes

| Outcome | Eligible projects | Min | Max | Weight | Effect | Repeat |
|---|---|---|---|---|---|---|
| Backspin Mechanism | Bouncing Bomb | 0% | 80% | 1 | Project progress +10%; scientist experience +150 | No |
| Training Accidents | Bouncing Bomb | 0% | 80% | 1 | Project progress −2%; +25 air experience | No |
| Aircraft Modifications | Bouncing Bomb | 0% | 80% | 1 | Scientist experience +150 | No |
| Type of Explosives | Bouncing Bomb | 0% | 80% | 1 | Project progress +5%; +5 air experience | No |
| Design Direction | Earthshaker Bomb | 40% | 90% | 100 | With BBA (Large Airframe) choice: naval targeting +10%; or naval attack +5% and strategic bombing +5%; or both plus production cost +5%. Without BBA the same applies to Strategic Bombers | No |
| Long-Range Delivery | Intercontinental Bomber | 40% | 90% | 100 | Choice: reliability +5%; or strategic bombing +15%, air defense −5%, air attack −10%; or air defense +15%, air attack −10%, strategic bombing −10% | No |
| Peak Mothership Performance | Mothership Aircraft | 40% | 90% | 100 | Choice: agility +10%, speed +10%, fuel consumption +15%; or reliability +10%; or air defense +10%, air attack +10%, production cost +10% | No |
| Development Priority | Jet Engine | 40% | 90% | 100 | With BBA choice: 1× 50% research bonus for Light Aircraft; or 2× 25% for Aircraft; or 1× 50% for Medium Aircraft. Without BBA: jet fighter/bomber stat trade-offs (see wiki) | No |
| Development Déjà Vu | Axial Jet Engine | 40% | 90% | 100 | With BBA choice: 1× 50% for Light Aircraft; or 2× 33% for Aircraft; or 1× 50% for Medium Aircraft. Without BBA: jet fighter/bomber stat trade-offs | No |
| Cost Concerns | Supersonic Jet | 40% | 90% | 100 | Choice: range −5%, speed −5%, reliability −10%, cost −10%; or reliability +3% (BBA) / +5% (no BBA); or reliability +5%, cost +10%, agility +5%, defense +5% | No |
| Safety Concerns | Helicopter | 40% | 90% | 100 | Choice: speed +10%, fuel consumption +5%, cost +5%; or reliability +5%; or armor +10%, defense +10%, breakthrough +10%, fuel consumption +15%, cost +10% | No |
| Range versus Payload? | Flying Bomb | 0% | 50% | 50 | Choice: guided missile speed +5%, range +10%, strategic bombing −5%; or strategic bombing +15%, range −5% | No |
| Technical Breakthrough in Pulse Jet Design | Flying Bomb | 0% | 50% | 1 | Guided missile speed +3%, range +3% | No |
| Launch Ramp Innovations | Flying Bomb | 0% | 75% | 1 | Project progress +5% | No |
| Mass Production Scaling | Flying Bomb | 0% | 75% | 1 | Guided missile production cost −5% | No |
| Engine Optimization Breakthrough | Flying Bomb | 0% | 75% | 1 | Guided missile range +3% | No |
| Technological Innovation in Guidance Systems | Flying Bomb | 0% | 75% | 1 | Guided missile range +3%, strategic bombing +3% (a second variant instead gives project progress −5% and scientist experience +200) | No |
| Engineers Request Wind Tunnel | Ballistic Missile | 0% | 20% | 1000 | Choice: nothing; or project progress +10% and the Secret Resource Procurement spirit for 365 days (consumer goods factory factor +5%) | No |
| Ice Forming on Reentry | Ballistic Missile | 70% | 90% | 10 (100 as the German Reich) | Project progress −5%; scientist experience +70 | No |
| Guidance System | Ballistic Missile | 30% | 60% | 1000 (0 without both Radio and Mechanical Computing) | Choice: ballistic missile production cost −10%; or strategic bombing +5%, production cost +10% | No |
| Turbopump Frothing Issue | MRBM | 40% | 70% | 10 | Project progress −10%; scientist experience +70 | No |
| Relay Failure | MRBM | 70% | 95% | 10 | Choice: project progress −5%; or refuse to replace the relay (raises the chance of Onsite Explosion once for all future projects) | No |
| Rocket Rust | ICBM | 40% | 90% | 50 (100 as the United States) | Project progress +5% | No |
| Launch Site Issues | ICBM | 30% | 60% | 10 (1000 as the Soviet Union) | Choice: project progress −5%; or project progress +10%, Secret Resource Procurement spirit for 365 days (consumer goods factory factor +2.5%), a random owned state with ≥1 building slot and rocket site level < 2 gets rocket site level +2, and build a new facility (raises Onsite Explosion chance for all future projects) | No |
| Ground Control Improvements | Surface to Air Missiles | 0% | 75% | 1 | Project progress +5% | No |
| Vertical Launch System | Surface to Air Missiles | 0% | 30% | 1 | Project progress +5%; scientist experience +70 | No |
| High Speed Flight Control | Surface to Air Missiles | 25% | 80% | 1 | 1× 15% research bonus for Aircraft | No |
| Warhead Detonation Mechanisms | Surface to Air Missiles | 30% | 100% | 1 | Surface to Air Missile air attack +10%; scientist experience +70 | No |
| Technological Advancements | Radar | 0% | 100% | 1 | 1× 10% research bonus for Industry | Yes |
| Technological Innovation | Radar | 0% | 100% | 1 | Random: 10% chance 1× 10%, 70% chance 1× 20%, 20% chance 1× 35% research bonus for Electronics | Yes |
| Empty Outcome | Any | 0% | 100% | 1 | Nothing | Yes |
| Avionics Advancements | Any | 0% | 100% | 1 | +25 air experience | Yes |
| New Learnings | Helicopter, Flying Bomb, Ballistic Missile, MRBM, ICBM, Surface to Air Missiles, Rocket Interceptor | 0% | 100% | 1 | Scientist experience +200 | Yes |
| Major Breakthrough | Helicopter, Flying Bomb, Ballistic Missile, MRBM, ICBM, Surface to Air Missiles, Rocket Interceptor | 0% | 100% | 1 | Project progress +10% | Yes |
| Political Interference | Bouncing Bomb, Earthshaker Bomb, Intercontinental Bomber, Mothership Aircraft, Jet Engine, Axial Jet Engine, Supersonic Jet, Helicopter, Radar (and separately the missile projects) | 0% | 70% | 0.5 (1 if Fascist) | Project progress −5% | Yes |
| Valuable Insights / Increased Theoretical Knowledge / Limitless Discoveries | Most aero projects | 0% | 100% | 2 (0.5 if a sibling already fired; 0 if scientist skill > 4) | Scientist experience +70 / +100 / +150 (the last also gives Aerodynamics and Avionics breakthrough progress +10%) | No |
| Breath of Fresh Air / Breeze of Innovation / Winds of Change | Most aero projects | 50% | 100% | 2 (0.5 if a sibling already fired) | +15 / +30 / +50 air experience (the last also gives breakthrough progress +10%) | No |
| Project Takeoff / Expert Landing / Stroke of Genius | Most aero projects | 0% | 100% | 2 (0.5 if a sibling already fired) | Project progress +5% / +10% / +15%, each with scientist experience +70 (the last also gives breakthrough progress +10%) | No |
| Experiment Fell Flat / Breaking Bomb / Creative Disaster | Most aero projects | 15% / 30% / 50% | 100% | 2 (0.5 if a sibling already fired) | Project progress −5% / −10% / −15%, each with scientist experience +70 (the last also gives breakthrough progress +10%) | No |
| Onsite Explosion | Flying Bomb, Ballistic Missile, MRBM, ICBM, Surface to Air Missiles, Rocket Interceptor | 0% | 70% | 0.5; ×100 if the relay was not replaced; ×30 if a new facility was built | Facility damaged 15%; scientist experience +100; clears the raised-chance flag if it came from Relay Failure | Yes |
| New Related Findings | none currently | 0% | 100% | 1 | 1× 25% research bonus for Aircraft | Yes |

### Land Warfare outcomes

| Outcome | Eligible projects | Min | Max | Weight | Effect | Repeat |
|---|---|---|---|---|---|---|
| Overheating during Trials | Land Cruiser | 0% | 100% | 1 | Project progress −5% | No |
| Chassis Stress Failure | Land Cruiser | 20% | 70% | 4 | Choice: reliability +5% and progress −10%; or reliability −3%, armor +5%, progress −5%; or armor −5% | No |
| Engine Output Insufficient | Land Cruiser | 20% | 70% | 4 | Choice: progress −5%; or speed +5% and progress −10%; or reliability +5%, speed +5%, progress −15% | No |
| Complex Turret Mechanism | Land Cruiser | 50% | 100% | 4 | Choice: nothing; or breakthrough −3%, cost −2%, progress +5%; or breakthrough +3%, speed +3%, cost +5%, progress −5% | No |
| Track System Failure | Land Cruiser | 30% | 80% | 4 | Choice: progress −5%; or armor −3%; or reliability +5%, cost +3%, progress −10% | No |
| Communication System Issue | Land Cruiser | 60% | 100% | 4 | Choice: nothing; or breakthrough +3% and progress −5%; or breakthrough +3%, defense +3%, cost +2%, progress −10% | No |
| Precision Assembly | Land Cruiser | 20% | 60% | 4 | Choice: reliability +7%, cost +5%, progress −5%; or reliability +3% | No |
| Hydropneumatic Suspension System | Land Cruiser | 30% | 100% | 4 | Choice: speed +3%, reliability +3%, cost +5%, progress +5%; or reliability +3% | No |
| Ammunition Storage Solution | Land Cruiser | 50% | 100% | 4 | Choice: nothing; or breakthrough +3%, cost +2%; or breakthrough +5%, reliability +3%, cost +5%, progress −5% | No |
| Design Focus | Super-Heavy Howitzer (and separately Self-Propelled Super-Heavy Howitzer) | 30% | 100% | 50 | Choice: nothing; or cost +10%, soft attack +5%, collateral damage +10%; or cost −15%, soft attack −5%, collateral damage −10% | No |
| Successful Firing Test | Multi-Charge Large Caliber Gun | 0% | 70% | 5 | Project progress +10%; scientist experience +70 | No |
| Catastrophical Explosion | Multi-Charge Large Caliber Gun | 0% | 70% | 1 | Facility damaged 25%; state infrastructure damaged 15%; progress −10%; scientist experience +70; scientist injured 60 days | No |
| Breakthrough in Propulsion Technology | Multi-Charge Large Caliber Gun | 60% | 100% | 2 | Progress +15%; Land Warfare breakthrough progress +10%; 30% chance the scientist gains Fast Learner, else 20% chance of gaining Bright | No |
| Structural Weakness Discovered | Stronghold Network | 20% | 70% | 1 | Progress −10%; prevents the Collapse During Tunnel Construction outcome | No |
| Delayed by Concrete Shortage | Stronghold Network | 0% | 90% | 1 | Progress −5%; scientist experience +70 | No |
| Underground Rail Systems | Stronghold Network | 30% | 100% | 2 | Progress +5%; 1× 10% research bonus for Fortifications, Engineers | No |
| Integration of Anti-Blast Doors | Stronghold Network | 30% | 100% | 2 | Progress +5% | No |
| Communication System Overhaul | Stronghold Network | 50% | 100% | 5 | Choice: 1× 25% research bonus for Fortifications, Construction; or scientist experience +100 | No |
| Leadership Approach | Stronghold Network | 0% | 100% | 100 (forced to maximum if nothing else is forced) | Choice: progress +5%, scientist experience +70, **field work** option; or Land Warfare breakthrough progress +5%, **office work** option | No |
| Breakthrough in Concrete Reinforcement | Stronghold Network | 50% | 100% | 15 | Field work: 1× 50% research bonus for Fortifications, Construction and progress +5%; or scientist experience +70 and progress +10%. Office work: 1× 75% research bonus for Fortifications, Construction and another land warfare scientist gains +150 experience; or another scientist +100 experience and progress +5% | No |
| Collapse During Tunnel Construction | Stronghold Network | 60% | 100% | 0 if Structural Weakness Discovered already fired, else 10 | Field work: progress −15% + scientist injured 30 days; or progress −10% + injured 60 days; or progress −5% + injured 60 days + the Emergency Labor Draft state modifier for 60 days (repair speed −50%, free repair −50%, resource gain efficiency −50%, local construction speed −50%). Office work: progress −10%; or progress −5% + Emergency Labor Draft | No |
| Empty Outcome | Any | 0% | 100% | 1 | Nothing | Yes |
| New Learnings / Refined Expertise / Insightful Discovery | Any | 0% | 100% | 2 (0.5 if a sibling already fired; 0 if scientist skill > 4) | Scientist experience +70 / +100 / +150 (the last also gives Land Warfare breakthrough progress +10%) | No |
| Battlefield Innovations / Operational Insight / Adapted Field Tactics | Any | 50% | 100% | 2 (0.5 if a sibling already fired) | +15 / +30 / +50 army experience (the last also gives breakthrough progress +10%) | No |
| Promising Prototype / Critical Test Successful / Pivotal Discovery | Any | 0% | 100% | 2 (0.5 if a sibling already fired) | Progress +5% / +10% / +15%, each with scientist experience +70 (the last also gives breakthrough progress +10%) | No |
| Testing Inconclusive / Design Flaw Detected / Minor Test Failure | Any | 15% / 30% / 50% | 100% | 2 (0.5 if a sibling already fired) | Progress −5% / −10% / −15%, each with scientist experience +70 (the last also gives breakthrough progress +10%) | No |
| Pioneering Techniques / Innovative Advancements / Experimental Methodology | Military Engineering Vehicles, Land Cruiser | 0% | 100% | 2 (0.5 if a sibling already fired) | 1× 10% / 20% / 35% research bonus for Tanks (the last also gives breakthrough progress +10%) | No |
| Pioneering Techniques / Innovative Advancements / Experimental Methodology | Super-Heavy Howitzer, Self-Propelled Super-Heavy Howitzer, Super-Heavy Railway Gun, Multi-Charge Large Caliber Gun | 0% | 100% | 2 (0.5 if a sibling already fired) | 1× 10% / 20% / 35% research bonus for Artillery (the last also gives breakthrough progress +10%) | No |
| Enhanced Plating / Ballistic Resistance Improvements / Improved Armor Alloys | Land Cruiser | 50% | 100% | 2 (0.5 if a sibling already fired) | Armor: armor +2% / hardness +2% / both plus Land Warfare breakthrough progress +10% | No |
| Fuel Efficiency Engines / Enhanced Engine Reliability / Optimized Engine Performance | Military Engineering Vehicles, Land Cruiser | 50% | 100% | 2 (0.5 if a sibling already fired) | Armor speed +3% / armor reliability +3% / both plus breakthrough progress +10% | No |
| Improved Ranged Accuracy / New Recoil Reduction Systems / Advanced Muzzle Design | Super-Heavy Howitzer, Self-Propelled Super-Heavy Howitzer, Super-Heavy Railway Gun, Multi-Charge Large Caliber Gun | 50% | 100% | 2 (0.5 if a sibling already fired) | Artillery soft attack +2% / anti-tank hard attack +2% and anti-air air attack +2% / all three plus breakthrough progress +10% | No |
| Resource Scarcity | Any | 25% | 80% | 0.5 | Progress −5%; scientist experience +70 | No |
| Critical Failure | Any | 25% | 80% | 0.25 | Progress −10%; scientist experience +70; scientist injured 30 days; facility damaged 25% | No |

See also: [Research and technology](research-and-technology.md), [Construction and buildings](construction-and-buildings.md), [Production and equipment](production-and-equipment.md).
