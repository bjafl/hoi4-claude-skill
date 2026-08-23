---
title: Difficulty Settings Strategy
category: strategy
tags: [difficulty, custom-difficulty, AI-modifiers, achievement, gameplay-balance]
game_version: "1.19"
dlc: []
sources:
  - https://hoi4.paradoxwikis.com/Difficulty
  - https://hoi4.paradoxwikis.com/Custom_difficulty
---

## Summary

HOI4 offers five preset difficulty levels that apply numerical modifiers to player and AI bonuses. Higher difficulties reduce player efficiency, research, production, and unit stats while boosting AI combat performance and fuel efficiency. Custom difficulty allows fine-grained control over major nation strength (Germany, Soviet Union, France, UK, US, Italy, Japan, China) via sliders, with most customizations disabling achievements. Only Regular and higher are achievement-eligible.

## Preset Difficulty Levels

Difficulties are set at game creation and range from Civilian to Elite. Each applies a fixed set of modifiers listed below. All modifiers stack additively unless noted. AI modifiers on higher difficulties are *applied in addition to* all previous difficulty tiers.

### Civilian

**Player modifiers:**
- Political Power Gain: +50%
- Supply Consumption: -10.0%
- Production Efficiency Cap: +30.00%
- Lack of Resources Penalty: -80.00%
- Research Speed: +15.0%
- Supply Grace: +72.0 hours
- Army Fuel Consumption: -50.00%
- Navy Fuel Consumption: -50.00%
- Air Fuel Consumption: -50.00%

**AI modifiers:**
- Peace score transferred to player: +25.00%

**Quotation:** "We Can Do It!"

**Inferred:** Civilian eliminates fuel as a strategic constraint and lets the player research at accelerated pace. Lack of resources penalties are largely neutered, allowing military production to proceed despite resource shortages. This is the easiest way to learn HOI4 mechanics.

### Recruit

**Player modifiers:**
- Political Power Gain: +25%
- Supply Consumption: -5.0%
- Production Efficiency Cap: +20.00%
- Lack of Resources Penalty: -30.00%
- Research Speed: +7.00%
- Supply Grace: +48.0 hours
- Army Fuel Consumption: -25.00%
- Navy Fuel Consumption: -25.00%
- Air Fuel Consumption: -25.00%

**AI modifiers:**
- Peace score transferred to player: +10.00%
- Supply Grace: +24.0 hours

**Quotation:** "I have full confidence in your courage, devotion to duty, and skill in battle. We will accept nothing less than full victory. Good Luck!"

**Inferred:** Recruit halves the Civilian bonuses but preserves the player's advantage in all key areas. **Inferred:** This is the recommended difficulty for first playthroughs after learning the UI on Civilian; the AI remains non-threatening but forces attention to fuel and research timing.

### Regular

**Player modifiers:**
- Supply Grace: +36.0 hours

**AI modifiers:**
- Supply Grace: +36.0 hours

**Quotation:** "For the enemy is strong. He may hurl back our forces. Success may not come with rushing speed, but we shall return again and again."

**Inferred:** Regular is the baseline — both player and AI receive the same minor supply grace boost. No production, research, or fuel handicaps apply. **Inferred:** This is the minimum difficulty for achievements and represents the game as intended for competitive play.

### Veteran

**Player modifiers:**
- Political Power Gain: -10%
- Supply Consumption: +5.0%
- Production Efficiency Cap: -20.00%
- Research Speed: -15.00%
- Supply Grace: +24.0 hours

**AI modifiers:**
- Supply Grace: +48.0 hours
- Army Fuel Consumption: -25.00%
- Navy Fuel Consumption: -25.00%
- Air Fuel Consumption: -25.00%

**Quotation:** "Thirty years from now when you're sitting by your fireside with your grandson on your knee and he asks 'What did you do in the great World War Two?' you won't have to cough and say, 'Well, your granddaddy shoveled shit in Louisiana.'"

**Inferred:** Veteran inverts player bonuses into penalties: research slows by 15%, production efficiency cap drops by 20%, and fuel consumption rises 25%. The AI gains fuel efficiency and an extended supply grace period. **Inferred:** Use Veteran to test your economic and supply discipline; fuel becomes a real limiter.

### Elite

**Player modifiers:**
- Political Power Gain: -15%
- Supply Consumption: +10.0%
- Production Efficiency Cap: -30.00%
- Research Speed: -30.00%

**AI modifiers:**
- Supply Grace: +72.0 hours
- Army Fuel Consumption: -50.00%
- Navy Fuel Consumption: -50.00%
- Air Fuel Consumption: -50.00%

**Quotation:** "I have nothing to offer but blood, toil, tears, and sweat."

**Inferred:** Elite is the hardest preset. Research is halved, production caps are cut 30%, political power accumulation is severely limited, and supply consumption is at +10.0% (vs. Regular's baseline). The AI operates with half fuel costs and a massive supply buffer. **Inferred:** Only attempt Elite after mastering Veteran, as it forces extreme focus on early-game production efficiency and fuel logistics.

## Achievement Eligibility

Only **Regular** and higher difficulties permit achievement progression. Custom difficulty modifications that alter major nation strength also disable achievements *for those nations*. However, custom changes to non-major-nation-related rules (wargoals, fort levels, paradrops, etc.) may preserve achievement eligibility depending on the specific setting.

## Custom Difficulty: Major Nation Buffs

Custom difficulty allows sliders to boost any of the eight major nations: **Germany, Italy, Soviet Union, France, United Kingdom, United States, Japan** (including Manchukuo and Mengkukuo), **China** (Republic and Communist). Sliders scale from 0% to 100% in increments; at 50% slider position, 50% of the full modifier set applies.

**Inferred:** Boosting a major nation via custom difficulty entirely disables achievements for that nation, but not for neutral or minor nations you play. Use custom difficulty to increase AI nation strength if you want a stronger opponent without sacrificing your own country's achievement eligibility.

### Full Modifier Set at 100% Strength (Major Nations)

| Modifier | Value |
|---|---|
| Political Power Gain | +50% |
| Army Experience Gain | +50% |
| Division Experience Gain | +20% |
| Naval Experience Gain | +50% |
| Ship Experience Gain | +20% |
| Air Experience Gain | +50% |
| Division Attrition | -15% |
| Supply Consumption | -50% |
| Division Recovery Rate | +30% |
| Entrenchment Speed | +50% |
| Production Efficiency Cap | +30% |
| Production Efficiency Growth | +50% |
| Lack of Resources Penalty | -60% |
| Division Attack on Core Territory | +30% |
| Division Defense on Core Territory | +30% |
| Research Speed | +20% |
| Dockyard Output | +40% |
| Reinforce Rate | +4% |
| Planning Speed | +50% |
| Army Fuel Consumption | -80% |
| Navy Fuel Consumption | -80% |
| Air Fuel Consumption | -80% |
| Air Wing Mission Experience Gain | +50% |

**Inferred:** A major nation at 100% custom buff receives enormous multipliers: 50% faster political power (negates political crises), 50% bonus to all military experience (shortens the learning curve for new divisions and aircraft), and critically, −80% fuel consumption across all branches. **Inferred:** If you boost Germany to 100%, it effectively never runs out of fuel for military operations. Combining this with −50% supply consumption and +30% production efficiency cap creates an AI opponent that is extremely difficult to overextend logistically.

**Inferred:** At 50% slider position, each modifier is halved: +25% political power, +25% experience gains, −40% fuel consumption, etc. **Inferred:** Use 25–50% buffs to create opponents that are threatening without being impossible; a 50%-boosted Germany will have notably better fuel management and more experienced divisions, but is still vulnerable to early aggression.

## Custom Difficulty: Gameplay Rules

Beyond major nation buffs, custom difficulty allows modification of:

- **Wargoals:** Free (unrestricted), Limited (default, ideology + World Tension gating), Free at 25/50/75/100% WT, Focuses Only (with optional year cutoffs).
  - **Inferred:** "Free at 50% World Tension" makes early-war aggression possible but reserves mid-game for major power scrambles. "Focuses Only" simulates a scripted historical campaign.

- **Military Access, Docking Rights, Release Nations, Production Licenses, Lend-Lease, Volunteers, Guarantees, Faction Mechanics, Paradrops, Fort Levels, Scorched Earth.**
  - **Inferred:** These all disable achievements if modified from defaults. Use them to create thematic constraints (e.g., "Blocked" faction leadership changes to force historical alliances) without affecting single-nation achievement hunting.

- **AI National Focus Paths:** Every major nation and many minors (France, Germany, Italy, Japan, Soviet Union, Poland, Australia, Canada, etc.) can be set to Historical (default, achievement-eligible) or Alternative paths (achievements disabled for that nation).
  - **Inferred:** Set Germany to "Alternative Fascism" or the Soviet Union to "Left Opposition" if you want a radically different geopolitical landscape without affecting your own country's achievement track.

## Strategic Recommendations

**Inferred:** For first achievement run: Play Regular difficulty as a minor nation (Poland, Romania, Sweden). Regular has no player penalties and permits achievements on all nations.

**Inferred:** For harder challenge without custom rules: Jump to Veteran. The −15% research and −20% production cap force precision in what you build; fuel economy becomes a real limiter but is still manageable.

**Inferred:** To maximize difficulty without disabling achievements: Use custom difficulty to set the AI major nations to 75–100% buff instead of switching to Elite, which handicaps your own nation. This lets you earn achievements while fighting a substantially harder AI.

**Inferred:** For competitive multiplayer: Regular difficulty is the standard. Custom modifications almost always disable achievements, so they are used only for scenario design or roleplay runs.
