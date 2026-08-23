# Why Germany's push into Russia runs out of supply

Running dry once you cross the Soviet border is the single most common way a
Barbarossa offensive stalls, and it's almost never bad luck — it's the
logistics system doing exactly what it's designed to do to an army that
outruns its supply infrastructure. Here's what's actually happening,
grounded in the game's supply mechanics, and the concrete fixes.

## What's going wrong, mechanically

**1. You're stretching hub range past what it can reach.**
A province's hub supply comes from the *weakest link* in the railway (or
port) chain back to your capital, and that connection has a hard falloff
with distance:

| Railway level | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Supply throughput | 15 | 20 | 25 | 30 | 35 |

Range from a hub decays sharply with each extra province of distance, so a
hub 6–8 provinces behind your front line (which is exactly where your only
hub tends to be once you've raced 500km into Russia) is often barely
reaching your forward divisions at all, or only at a fraction of its rated
throughput.

**2. Captured Soviet rail isn't usable immediately — and often stays at
low level.** Non-core captured territory needs **10 days** before its
railway is usable (5 for core territory, 0 in a civil war), and *every
province* along the line has to finish converting before the hub behind it
comes back online. Soviet rail you capture also inherits whatever level it
was built at — frequently level 1 in the interior — so even once it's
usable, it's only delivering 15 supply total for everything drawing from
it.

**3. Interior Soviet states give little state supply.** State supply
(drawn *before* hub supply) comes from victory points, infrastructure, and
population. Deep interior USSR states are often lower-infrastructure and
sparsely populated relative to their size, so the state-supply floor your
divisions fall back on is thin — a level-1 infrastructure state gives just
0.30 supply, shared across every unit in that state, land or air.

**4. You probably don't have hubs motorized, or don't have enough trucks
for the ones you tried to motorize.** Extending hub range requires
motorizing the hub (40 trucks for one truck-level, 80 for full
motorization), and if you're short on trucks the benefit is reduced
*proportionally* to the shortfall — a half-stocked motorized hub gives you
roughly half the range boost, not "some."

**5. Terrain and (if this drags into winter) weather are compounding it.**
Supply-flow penalties from terrain are flat subtractions from the hub's
supply output, not percentages, and they stack per province crossed:
Forest −0.08, Hills −0.1, Marsh −0.16 per province. Individually small, but
several such provinces between your hub and the front add up, and Russia's
interior has plenty of forest/marsh/hills. If the campaign runs into
autumn/winter, add Mud (−15% supply factor, and a brutal 500% truck
attrition multiplier), Snow (−20%), Deep Snow (−40%), and Blizzard events
(−25% supply factor, +15% consumption) on top.

**6. Germany's own national spirit is working against you.** The
**Deutsches Heer** national spirit gives Germany **+15% Supply
Consumption** baseline (alongside +5% org and +25% planning speed) — every
division is drawing more than the raw battalion numbers would suggest
before you even account for terrain.

**7. Your divisions may just be heavy.** Supply draw is per-battalion:
infantry is cheap (0.06 each), but artillery (0.21), tanks (0.22–0.40), and
motorized/mechanized elements (0.065–0.18) add up fast. A tank-heavy
spearhead division draws far more supply per unit than the infantry that's
supposed to be holding ground behind it — and if you're pushing armor deep
into Russia on a single stretched hub, that's the fastest way to hit the
attrition threshold (supply below 35% triggers equipment losses, not just
speed/attack/org penalties).

## How to fix it

- **Build forward supply hubs as you advance**, not after you stall. A
  hub costs 20,000 CIC but saves you from losing whole divisions to
  starvation — aim for a hub within 3–4 provinces of the front line at all
  times, same as you'd plan for any other offensive.
- **Upgrade the railway to your forward hubs**, don't just capture and
  leave it at level 1. Each level costs `300 + 130×current level` CIC (up
  to 2,800 total for level 1→5), and going from level 1 (15 supply) to
  level 3 (25) or 5 (35) is often the difference between "starving" and
  "fine." Remember the connection is only as strong as its *weakest*
  segment — one un-upgraded stretch caps the whole line.
- **Let captured rail finish converting** (10 days non-core / 5 core)
  before routing your main push's supply through it, and check that every
  province on the line, not just the hub province, has finished.
- **Motorize hubs in good terrain, not bad.** Truck attrition is 0 in
  plains but 3–4x in jungle/marsh — motorizing a hub sitting in marsh will
  burn through your 40/80 trucks fast and give you a shrinking, not
  growing, range bonus. Make sure you actually have the trucks in stock
  before motorizing (a shortfall gives a proportionally reduced benefit,
  not full).
- **Fit a Logistics Company support company** into your spearhead
  divisions — it's a flat −10% division supply usage (and −5% fuel) per
  tier researched, stacking with later Logistics Company techs, and it
  costs nothing structurally (0 supply use itself).
- **Don't run at 100% of theoretical hub capacity.** Weather alone can
  swing supply by up to 40–50% (Blizzard −25% flow / +15% consumption,
  Deep Snow −40% flow). Size the force actually operating past a hub to
  roughly 70–80% of what the hub can sustain at full throughput, so you
  have margin when weather or a Logistical Strike air raid degrades it.
- **Pace the offensive to your supply build, not the other way round.**
  Push, then pause to land a hub and rail upgrades before pushing again,
  rather than racing tank divisions hundreds of kilometers ahead of any
  hub. Use the supply map mode (F4) to watch this in real time — purple
  means low supply but no penalty yet, yellow means units are starting to
  starve, bright red means active attrition; hold Ctrl over a province for
  the hub-supply source breakdown, and Shift over a hub to see its current
  range.
- **Keep armor and artillery-heavy divisions behind the infantry line**
  where possible, or at least keep them near the strongest hub — their
  supply draw per battalion is 3–6x an infantry battalion's, so they're
  the first thing to break when a hub is stretched thin.

If you do all of the above and are still starving, the likely remaining
culprit is trains: rail throughput needs enough trains to actually carry
it (check the crate-icon logistics tooltip at the top of the screen for
your national train shortfall), and Soviet partisans or Logistical Strike
missions against your trains/trucks can silently cut delivered supply even
when the hub and rail levels look fine on paper.

## Files consulted

- `references/01-mechanics/supply-and-logistics.md`
- `references/08-strategy/common-mistakes.md`
- `references/05-countries/germany.md`
