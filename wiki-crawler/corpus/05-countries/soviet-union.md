---
title: Soviet Union
category: countries
tags: [SOV, communist, stalinism, comintern, paranoia, purges, civil-war, five-year-plan]
game_version: "1.19"
dlc: []
sources:
  - https://hoi4.paradoxwikis.com/Soviet_Union
---

The Soviet Union enters 1936 as the world's premier communist state and leader of the Comintern faction, commanding vast territory, population, and natural resources across Asia and Eastern Europe. It faces severe internal instability from Stalin's purges and paranoia alongside urgent military modernization needs, but possesses the industrial capacity and ideological machinery to eventually become a superpower. The unique paranoia and civil-war systems make it a country fundamentally shaped by internal politics as much as external threat.

## 1936 starting position

**Tag:** SOV (tags SOS, SOT, SOB, SOP, SOU used for breakaway states)  
**Ideology:** Communist (Stalinism)  
**Ruling party:** Vsesoyuznaya Kommunisticheskaya Partiya (Bolshevikov) - VKP(B)  
**Government type:** Totalitarian Dictatorship  
**Faction:** Comintern (as leader; includes Tannu Tuva and Mongolia)

**1936 starting stats:**

| Stat | Value |
|---|---|
| States | 152 |
| Research slots | 3 (+ 3 unlockable via focus tree) |
| Population | 165.13M |
| Victory points | 152+ (largest empire) |

> ⚠️ Broken wiki template found in master stats table at factories column; exact values for all resource/VP/building-slot columns not reconstructed.

## Government and political situation

**Starting leader:** Iosif Stalin (Stalinism ideology, Heart of Steel trait)  
- Stability: -10%, War support: +5%, Political Power gain: +5%
- Master impact: -0.10 (improved autonomy control)

**Starting condition:** Stalin's Stalinist path is the historical route; the focus tree offers three alternative paths:
- **Left Opposition:** Replace Stalin with Lev Trotsky (Marxism) via civil war; foment communist uprisings abroad
- **Right Opposition:** Install Nikolay Bukharin (Marxism) via coup or civil war; implement New Economic Policy
- **Beaten, but not Defeated:** Trigger Second Russian Civil War; restore Tsardom (Vladimir III as Tsar), install Fascism (Konstantin Rodzayevsky), or establish Theocracy (Patriarch Meletius, Third Rome)

**Succession (if Stalin dies or is removed):** Lavrenty Beriya can assume leadership; The Supreme Soviet (Marxism) can take control if its focus is completed; other rivals Lev Kamenev emerge through opposition paths.

**Faction:** Leads the Comintern. Communist China and Sinkiang have favorable views but are not members in 1936. Can propose alliances to France, Poland, and Balkan minors via focus tree; can attempt to subvert non-communist neighbors (Finland, Baltic states, East Poland) through ideology and ultimatums.

## National spirits

The Soviet Union begins with six national spirits, each representing constraints and drawbacks of the 1936 regime:

### Home of the Revolution
- Ideology drift defense: +50.0%
- Can create factions

### Trotskyite Plot?
- Political Power gain: -15%
- Stability: -20.0%

### Politicized Military
- Division Defense on core territory: +3.0%
- Ideology drift defense: +10.0%
- Commander Abilities Cost: +10.0%
- Air Doctrine Cost: +20.0%
- Land Doctrine Cost: +20.0%
- Naval Doctrine Cost: +20.0%

### Five Year Plan
- Consumer Goods Factories factor: +10.0%
- Production Efficiency Cap: +5%
- Production Efficiency Growth: -15%
- Civilian factory construction speed: +5%

### Soviet Air Force
- Air Wing Experience loss when killed: +30%
- Ace generation chance: -50.0%
- Air Wing Training Experience Gain: -10%
- Air Accidents Chance: +75.0%
- Night Operations Penalty: +30.0%
- Bad Weather Penalty: +30.0%
- Air Wing Mission Experience Gain: +10%

### The Red Army
- Army experience Gain: -10.0%
- Division Organization: -15.0%
- Experienced soldier losses: +25.0%
- Conscription Laws Cost: -10%

## Unique mechanics

### Stalin's Paranoia meter

When following the **Centre (Stalinist) path**, the Soviet Union runs a hidden Paranoia meter (0–100) that drives periodic purges of military and political characters (generals, admirals, advisors, theorists). The meter rises each week from active modifiers (primarily Stalin's Paranoid trait and the current Head of the NKVD):

| Paranoia level | Effect |
|---|---|
| Below 25 | Calm; no purges initiated |
| 25–75 | Random purges occur periodically |
| Above 89 | Each day carries 20% chance to trigger Soviet Civil War if on Opposition path |

**Four forced Great Purges** occur on the Centre path regardless of meter state:
1. The Zinovyevite Terrorist Center
2. The Anti-Soviet Trotskyist Center
3. The Military Conspiracy
4. The Bloc of Rights and Trotskyites

Characters already purged by the random meter are skipped; total purged cannot be reduced, only which characters die changes.

### Soviet Civil War (Opposition paths)

If the player follows **Left Opposition** (Trotsky) or **Right Opposition** (Bukharin) paths and paranoia climbs above 89 (or if the coup decision is taken), the Soviet Civil War begins. Stalin's loyalists break away as **Stalinist Soviet Union (tag SOS)**, keeping Moscow; the player leads the rebels.

**Force division mechanics:**
- Each branch (army, navy, air) has its own "opposition support" value (20% floor to 90% cap, remainder goes to SOS)
- Officers align to Opposition only if their support has been won via focus; all others defect to SOS
- During the war, a monthly event allows cowed officers to defect to Opposition (~25% chance)
- **Exiles path destabilizes the union:** From the third month onward, breakaway states may spawn — Ukraine, Belarus, Georgia, Armenia, Azerbaijan, Crimea, Karelia, Central Asian republics; Karelian revolt drags in Finland

**Opposition Popular Support modifier** (active for the war duration) shifts surrender limits in the rebels' favor proportional to that support.

### National focus tree structure

The Soviet focus tree divides into **7 main branches and 9 sub-branches:**

- **Infrastructure Effort / Heavy Industry:** Bonuses to infrastructure, modifies Five Year Plan spirit
- **Transpolar Flights:** Modifies Soviet Airforce spirit
- **Expand the Red Fleet:** Modifies The Red Fleet spirit, coastal bonuses
- **Found the PCDI:** Grants Defense Industry spirit, artillery/armor bonuses; includes Military Engineering University sub-branch (forts, move industry to Urals)
- **Strengthen the Mobilization Plan:** Modifies The Red Army spirit, infantry bonuses
- **The Path of Marxism-Leninism:** Opens three ideological sub-branches (Centre/Stalinist, Left Opposition/Trotskyist, Right Opposition/Bukharinist), plus Gain Support, Strengthen Trade Unions, Addressing Internal Affairs, Comintern (external politics), and Beaten but not Defeated (end communism, restore Tsardom/Fascism/Theocracy)
- **Comintern Sub-branch:** Handles external alliances and political maneuvering with European and Asian powers; includes decisions to demand Eastern Poland, Baltic states, Kuril Islands/South Sakhalin from Japan, and Offer Protection ultimatums

See [06-focus-trees/soviet-union.md](../06-focus-trees/soviet-union.md) for the full focus tree.

### Ideological decisions and foreign ultimatums

Through focus tree progression (mainly Comintern and Collective Security branches), the USSR gains diplomatic decisions to propose pacts, pacts with guarantees, ideology pushes, and territorial demands to foreign AI nations. Base acceptance rates vary widely:

- **France (Popular Front/democratic):** Nearly always accepts defense pacts and guarantees
- **Poland:** ~40% accept Protection (alliance + guarantee) if unguaranteed; 0% if already guaranteed by Germany
- **Baltic states (Estonia, Latvia, Lithuania):** Always cede territorial demands unless protected/guaranteed by a major
- **Finland:** Always refuses on historical AI (triggers Winter War); ~25% if not guaranteed off-historical
- **Balkan minors (Bulgaria, Greece, Yugoslavia, Romania, Turkey):** Base ~17% puppet/cede; scales dramatically with USSR strength ratio (up to ~90% if far weaker than USSR)
- **Japan (Kuril Islands / South Sakhalin demand):** ~33% accept at parity, rising with USSR military superiority
- **Stir the Masses (subversion):** Costs 50 Political Power per target; applies Trotskyist Revolutionary Agitation spirit (3%/month ideology drift, -10% stability, -10% ideology drift defence) for 120 days + 90-day topple government war goal

## Neighbours and diplomatic position

**Bordering countries:**
- **West/Southwest:** Poland (territorial disputes, can demand Eastern Poland), German Reich (Fascist, future antagonist), Italy (Fascist ally of Germany)
- **Northwest:** Baltic States — Estonia, Latvia, Lithuania (can be demanded or guaranteed protection)
- **North:** Finland (Non-Aligned, disputes; Winter War triggered if refuses Protection ultimatum)
- **East:** Japan (Fascist, frequent border clashes; Kuril Islands/South Sakhalin disputes)

**Faction and alliances (1936):**
- **Comintern leader** — controls faction; Tannu Tuva and Mongolia are members
- **Friendly:** Communist China, Sinkiang (favorable view but not in faction)
- **Potential allies:** France (if pursuing Collective Security focus), UK (if pursuing Collective Security), Poland (if guaranteed before Germany acts)

**Victory points:** Soviet Union holds 152+ states; Stalingrad, Moscow, Leningrad, Alma-Ata, Crimea, and others are major population/production centers. Control of these and neighbor capitals (Warsaw, Helsinki, Tokyo, Berlin) determines war progress.

**Starting military position:** Despite vast manpower and resources, the Red Army is severely weakened by purges — low experience, poor organization, high soldier losses. Military modernization is urgent; the Five Year Plan industrial bonuses are essential for recovery. Air Force is particularly poor (high accident rates, low ace generation). Naval forces exist but are limited compared to major powers.
