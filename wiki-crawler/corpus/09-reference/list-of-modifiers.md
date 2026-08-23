---
title: List of modifiers
category: reference
tags: [modifiers, effects, game_mechanics, country_modifier, state_modifier]
game_version: "1.19"
dlc: []
sources:
  - https://hoi4.paradoxwikis.com/List_of_modifiers
---

Complete reference of all modifiers recognized by the game engine. All numbers support up to 3 decimal places; displayed decimals vary by modifier type.

## Intelligence & Espionage

| Modifier | Effect | Type |
|---|---|---|
| agency_upgrade_time | Agency upgrade time | 2 decimal places |
| civilian_intel_factor | Civilian Intelligence | 2 decimal places |
| army_intel_factor | Army Intelligence | 2 decimal places |
| navy_intel_factor | Navy Intelligence | 2 decimal places |
| airforce_intel_factor | Air Intelligence | 2 decimal places |
| crypto_department_enabled | Crypto Department Enabled | Boolean |
| crypto_strength | Cryptology Level | 0 decimal places |
| decryption_power | Decryption Power | 0 decimal places |
| decryption_power_factor | Decryption Power Factor | 2 decimal places |
| civilian_intel_decryption_bonus | Decrypted Civilian Cipher Bonus | 0 decimal places |
| army_intel_decryption_bonus | Decrypted Army Cipher Bonus | 0 decimal places |
| navy_intel_decryption_bonus | Decrypted Navy Cipher Bonus | 0 decimal places |
| airforce_intel_decryption_bonus | Decrypted Airforce Cipher Bonus | 0 decimal places |
| intelligence_agency_defense | Counter intelligence | 2 decimal places |
| encryption | Encryption | 2 decimal places |
| encryption_factor | Encryption | 2 decimal places |
| decryption | Decryption | 2 decimal places |
| decryption_factor | Decryption | 2 decimal places |

## Operatives & Espionage Operations

| Modifier | Effect | Type |
|---|---|---|
| operative_slot | Operative slots | 0 decimal places |
| new_operative_slot_bonus | Operative recruitment choices | 0 decimal places |
| female_random_operative_chance | Added Female Operative Chance | 0 decimal places |
| commando_trait_chance_factor | Chance of recruiting an Operative with the Commando trait | 0 decimal places |
| enemy_operative_recruitment_chance | Enemy nationality recruit chance | 2 decimal places |
| occupied_operative_recruitment_chance | Occupied friendly nationality recruit chance | 2 decimal places |
| operative_death_on_capture_chance | Death chance of our Operative on capture | 2 decimal places |
| intel_network_gain | Intel network strength gain | 2 decimal places |
| intel_network_gain_factor | Intel network strength gain | 2 decimal places |
| intel_from_operatives_factor | Intelligence gained from Operatives and Infiltrated Assets | 2 decimal places |
| defense_impact_on_blueprint_stealing | Impact of enemy Counter Intelligence on Steal Blueprints operation | 1 decimal place |
| boost_ideology_mission_factor | Boost Ideology mission effects | 2 decimal places |
| control_trade_mission_factor | Control Trade mission effects | 2 decimal places |
| propaganda_mission_factor | Propaganda mission effects | 2 decimal places |
| diplomatic_pressure_mission_factor | Diplomatic Pressure mission effects | 2 decimal places |
| boost_resistance_factor | Strengthen Resistance efficiency | 2 decimal places |
| root_out_resistance_effectiveness_factor | Root Out Resistance mission effects | 2 decimal places |

## Espionage Operation Costs & Outcomes

Operations and their subcategories (cost, outcome, risk) are parameterized. Examples include:

| Operation | Effect | Type |
|---|---|---|
| operation_cost / operation_outcome / operation_risk | Operation <parameter> | 2 decimal places |
| operation_fake_intel_* | False Intelligence <parameter> | 2 decimal places |
| operation_rescue_operative_* | Rescue Operative <parameter> | 2 decimal places |
| operation_make_resistance_contacts_* | Make Resistance Contacts <parameter> | 2 decimal places |
| operation_boost_resistance_* | Strengthen Resistance <parameter> | 2 decimal places |
| operation_collaboration_government_* | Prepare Collaboration Government <parameter> | 2 decimal places |
| operation_coup_government_* | Stage Coup <parameter> | 2 decimal places |
| operation_capture_cipher_* | Capture Cipher <parameter> | 2 decimal places |
| operation_coordinated_strike_* | Coordinated Strike <parameter> | 2 decimal places |
| operation_infiltrate_* | Infiltration <parameter> | 2 decimal places |
| operation_infiltrate_armed_forces_army_* | Infiltrate Army <parameter> | 2 decimal places |
| operation_infiltrate_armed_forces_navy_* | Infiltrate Navy <parameter> | 2 decimal places |
| operation_infiltrate_armed_forces_airforce_* | Infiltrate Airforce <parameter> | 2 decimal places |
| operation_infiltrate_civilian_* | Infiltrate Civilian Administration <parameter> | 2 decimal places |
| operation_steal_tech_* | Steal Blueprint <parameter> | 2 decimal places |
| operation_steal_tech_army_* | Steal Military Blueprints <parameter> | 2 decimal places |
| operation_steal_tech_navy_* | Steal Naval Blueprints <parameter> | 2 decimal places |
| operation_steal_tech_airforce_* | Steal Aviation Industry Blueprints <parameter> | 2 decimal places |
| operation_steal_tech_civilian_* | Steal Industrial Blueprints <parameter> | 2 decimal places |
| target_sabotage_* | Sabotage <parameter> | 2 decimal places |
| operation_targeted_sabotage_industry_* | Sabotage Industry <parameter> | 2 decimal places |
| operation_targeted_sabotage_infrastructure_* | Sabotage Infrastructure <parameter> | 2 decimal places |
| operation_targeted_sabotage_resources_* | Sabotage Resources <parameter> | 2 decimal places |

## AI Modifiers

| Modifier | Effect | Type |
|---|---|---|
| ai_focus_defense_factor | AI Modifier: Focus on Defense | 1 decimal place |
| ai_focus_aggressive_factor | AI Modifier: Focus on Offense | 1 decimal place |
| ai_focus_war_production_factor | AI Modifier: Focus on War Production | 1 decimal place |
| ai_focus_military_advancements_factor | AI Modifier: Focus on Military Advancements | 1 decimal place |
| ai_focus_peaceful_factor | AI Modifier: Focus on Peace | 1 decimal place |
| ai_focus_naval_factor | AI Modifier: Focus on Navy | 1 decimal place |
| ai_focus_naval_air_factor | AI Modifier: Focus on Naval Air | 1 decimal place |
| ai_focus_aviation_factor | AI Modifier: Focus on Aviation | 1 decimal place |
| ai_focus_military_equipment_factor | AI Modifier: Focus on Military Equipment | 1 decimal place |
| ai_badass_factor | AI Modifier: Threat receptivity | 1 decimal place |
| ai_desired_divisions_factor | Factor on how many divisions the country aims to produce | 1 decimal place |
| ai_get_ally_desire_factor | AI Modifier: Desire to be in or expand a faction | 0 decimal places |
| ai_call_ally_desire_factor | AI Modifier: Call Ally Desire | 0 decimal places |
| ai_join_ally_desire_factor | AI Modifier: Join Ally Desire | 0 decimal places |
| ai_license_acceptance | Acceptance when requesting to buy license | 0 decimal places |

## Land Combat

| Modifier | Effect | Type |
|---|---|---|
| offence | Attack | 2 decimal places |
| defence | Defense | 2 decimal places |
| attack_bonus_against | Attack bonus against country | 1 decimal place |
| attack_bonus_against_cores | Attack on their core territory | 1 decimal place |
| defense_bonus_against | Defense bonus against country | 1 decimal place |
| land_night_attack | Land Night Attack | 1 decimal place |
| army_attack_factor | Division Attack | 2 decimal places |
| army_defence_factor | Division Defense | 2 decimal places |
| army_core_attack_factor | Division Attack on core territory | 2 decimal places |
| army_core_defence_factor | Division Defense on core territory | 2 decimal places |
| army_speed_factor | Divisions speed | 2 decimal places |
| army_speed_factor_for_controller | Divisions speed (state modifier) | 2 decimal places |
| army_org | Division Organization | 1 decimal place |
| army_org_factor | Division Organization | 1 decimal place |
| army_org_regain | Army Organization Regain | 2 decimal places |
| org_loss_when_moving | Org Loss when Moving | 1 decimal place |
| army_morale | Division Recovery Rate | 1 decimal place |
| army_morale_factor | Division Recovery Rate | 1 decimal place |

## Breakthrough & Armor

| Modifier | Effect | Type |
|---|---|---|
| breakthrough | Breakthrough (must be used in land equipment category) | 2 decimal places |
| breakthrough_factor | Breakthrough | 2 decimal places |
| breakthrough_bonus_against | Breakthrough bonus against country | 1 decimal place |
| armor_value | Armor (must be used in equipment category) | 2 decimal places |

## Entrenchment & Positioning

| Modifier | Effect | Type |
|---|---|---|
| dig_in_speed | Entrenchment speed | 0 decimal places |
| dig_in_speed_factor | Entrenchment speed | 1 decimal place |
| max_dig_in | Max Entrenchment (can be applied to a state) | 1 decimal place |
| max_dig_in_factor | Max Entrenchment | 1 decimal place |
| dont_lose_dig_in_on_attack | No Entrenchment Lose On Attack | Boolean |
| recon_factor | Reconnaissance | 1 decimal place |
| recon_factor_while_entrenched | Recon Bonus While Entrenched | 1 decimal place |

## Planning & Supply

| Modifier | Effect | Type |
|---|---|---|
| max_planning | Max planning | 1 decimal place |
| max_planning_factor | Max planning factor | 1 decimal place |
| planning_speed | Planning Speed | 1 decimal place |
| supply_consumption_factor | Supply Consumption | 1 decimal place |
| out_of_supply_factor | Out of Supply | 1 decimal place |
| no_supply_grace | Supply Grace | 1 decimal place |
| extra_marine_supply_grace | Extra Marine Supply Grace | 1 decimal place |
| extra_paratrooper_supply_grace | Extra Paratrooper Supply Grace | 1 decimal place |

## Attrition

| Modifier | Effect | Type |
|---|---|---|
| attrition | Division Attrition | 1 decimal place |
| attrition_for_controller | Division Attrition (state modifier) | 1 decimal place |
| winter_attrition | Winter Attrition | 1 decimal place |
| winter_attrition_factor | Winter Attrition | 2 decimal places |
| heat_attrition | Heat Attrition | 1 decimal place |
| heat_attrition_factor | Heat Attrition | 2 decimal places |
| unit_upkeep_attrition_factor | Unit Upkeep | 0 decimal places |

## Training & Reinforce Rate

| Modifier | Effect | Type |
|---|---|---|
| land_reinforce_rate | Reinforce Rate | 1 decimal place |
| minimum_training_level | Minimum training level | 0 decimal places |
| max_training | Max training | 2 decimal places |
| training_time_factor | Training time | 2 decimal places |
| training_time_army | Division training time | 1 decimal place |
| training_time_army_factor | Division training time | 1 decimal place |

## Terrain & Special Conditions

| Modifier | Effect | Type |
|---|---|---|
| combat_width_factor | Own Combat Width | 1 decimal place |
| river_crossing_factor | River Crossing Speed Penalty | 2 decimal places |
| terrain_penalty_reduction | Terrain Penalty Reduction | 1 decimal place |
| pocket_penalty | Encirclement penalty | 1 decimal place |
| fortification_damage | Fort Damage from Combat | 1 decimal place |
| fortification_collateral_chance | Fort Combat Damage Chance | 1 decimal place |
| acclimatization_cold_climate_gain_factor | Cold acclimatization gain factor | 1 decimal place |
| acclimatization_hot_climate_gain_factor | Hot acclimatization gain factor | 1 decimal place |

## Special Forces & Airborne

| Modifier | Effect | Type |
|---|---|---|
| special_forces_min | Special Forces Minimum Capacity | 0 decimal places |
| special_forces_cap | Special Forces Capacity Multiplier | 1 decimal place |
| special_forces_training_time_factor | Special Forces Division training time | 1 decimal place |
| special_forces_no_supply_grace | Special Forces Supply Grace | 1 decimal place |
| special_forces_out_of_supply_factor | Special Forces Out of Supply | 2 decimal places |
| paratrooper_count_per_plane | Paratrooper per Plane | 1 decimal place |
| paradrop_organization_factor | Paratrooper Organization Factor | 1 decimal place |
| paratrooper_aa_defense | Paratrooper Anti Air Defense | 1 decimal place |

## Unit Type Modifiers (Army)

Unit-specific modifiers follow the pattern `<unit_type>_attack_factor`, `<unit_type>_defence_factor`, `<unit_type>_speed_factor` with 1 decimal place. Unit types include:

- infantry, armor, artillery, cavalry, motorized, mechanized, special_forces

Examples: `army_infantry_attack_factor`, `army_armor_defence_factor`, `cavalry_speed_factor`

## Air Force - General

| Modifier | Effect | Type |
|---|---|---|
| air_attack | Air Attack (must be used in air equipment category) | 0 decimal places |
| air_attack_factor | Air Attack | 2 decimal places |
| air_defence | Air Defense (must be used in air equipment category) | 0 decimal places |
| air_defence_factor | Air Defense | 2 decimal places |
| air_agility | Agility (must be used in air equipment category) | 0 decimal places |
| air_agility_factor | Agility | 2 decimal places |
| maximum_speed | Max Air Speed (must be used in air equipment category) | 0 decimal places |
| air_maximum_speed_factor | Max Air Speed | 2 decimal places |
| air_range | Air Range (must be used in air equipment category) | 0 decimal places |
| air_range_factor | Air Range | 2 decimal places |
| air_superiority | Air Superiority (must be used in air equipment category) | 1 decimal place |

## Air Force - Accidents, Weather & Operations

| Modifier | Effect | Type |
|---|---|---|
| air_accidents | Air Accidents Chance | 1 decimal place |
| air_accidents_factor | Air Accidents Chance | 2 decimal places |
| air_weather_penalty | Bad Weather Penalty | 2 decimal places |
| air_night_penalty | Night Operations Penalty | 2 decimal places |
| air_detection | Air Detection | 2 decimal places |
| air_fuel_consumption_factor | Air Fuel Consumption | 2 decimal places |
| air_mission_efficiency | Air Mission Efficiency | 1 decimal place |
| air_superiority_efficiency | Air Superiority Mission Efficiency | 2 decimal places |
| air_intercept_efficiency | Interception Mission Efficiency | 2 decimal places |
| air_cas_efficiency | Air Support Mission Efficiency | 2 decimal places |
| air_escort_efficiency | Escort Efficiency | 2 decimal places |
| air_nav_efficiency | Naval Mission Efficiency | 2 decimal places |
| air_cas_present_factor | Ground support | 2 decimal places |

## Air Force - Experience & Aces

| Modifier | Effect | Type |
|---|---|---|
| experience_gain_air | Air Experience Gain | 2 decimal places |
| experience_gain_air_factor | Air Experience Gain | 1 decimal place |
| air_training_xp_gain_factor | Air Wing Training Experience Gain | 0 decimal places |
| air_mission_xp_gain_factor | Air Wing Mission Experience Gain | 0 decimal places |
| air_ace_generation_chance_factor | Ace generation chance | 2 decimal places |
| air_wing_xp_loss_when_killed_factor | Air Wing Experience loss when killed | 0 decimal places |

## Air Force - Mission-Specific Modifiers

Air mission modifiers follow the pattern `air_<mission>_<stat>_factor` with 2 decimal places:

**Interception:** air_interception_attack_factor, air_interception_defence_factor, air_interception_agility_factor, air_interception_detect_factor

**Air Superiority:** air_air_superiority_attack_factor, air_air_superiority_defence_factor, air_air_superiority_agility_factor, air_superiority_detect_factor

**Close Air Support:** air_close_air_support_attack_factor, air_close_air_support_defence_factor, air_close_air_support_agility_factor

**Strategic Bomber:** air_strategic_bomber_attack_factor, air_strategic_bomber_defence_factor, air_strategic_bomber_agility_factor, air_strategic_bomber_bombing_factor, air_strategic_bomber_night_penalty

**Naval Strike:** naval_strike_attack_factor, naval_strike_targetting_factor, naval_strike_agility_factor

**Paradrop:** air_paradrop_attack_factor, air_paradrop_defence_factor (air_paradrop_agility_factor exists but has no effect)

## Air Force - Bombing & Rockets

| Modifier | Effect | Type |
|---|---|---|
| ground_attack | Ground attack | 2 decimal places |
| ground_attack_factor | Ground attack factor | 2 decimal places |
| air_bombing | Ground Bombing (must be used in air equipment category) | 1 decimal place |
| air_bombing_targetting | Ground Bombing Targeting | 1 decimal place |
| strategic_bomb_visibility | Strategic bombing visibility | 2 decimal places |
| naval_strike_attack_factor | Naval Bombing | 0 decimal places |
| naval_strike_targetting_factor | Naval Targeting | 0 decimal places |
| naval_strike_agility_factor | Naval Agility | 0 decimal places |
| mines_planting_by_air_factor | Aerial minelaying efficiency | 0 decimal places |
| mines_sweeping_by_air_factor | Aerial minesweeping efficiency | 0 decimal places |
| modifier_enemy_port_superiority_limit | Port strike enemy superiority limit | 0 decimal places |
| rocket_attack_factor | Rocket Damage | 1 decimal place |
| army_bonus_air_superiority_factor | Air Superiority (army bonus) | 2 decimal places |
| enemy_army_bonus_air_superiority_factor | Enemy Air Support | 2 decimal places |
| air_superiority_bonus_in_combat | Air Superiority Bonus in Combat | 1 decimal place |
| cas_damage_reduction | Damage Reduction Against CAS | 1 decimal place |
| shore_bombardment_bonus | Shore Bombardment Bonus | 1 decimal place |

## Navy - General Combat

| Modifier | Effect | Type |
|---|---|---|
| naval_damage_factor | Damage | 2 decimal places |
| naval_defense_factor | Defense | 2 decimal places |
| navy_org | Navy Organization | 1 decimal place |
| navy_org_factor | Navy Organization | 1 decimal place |
| naval_morale | Ship Recovery Rate | 1 decimal place |
| naval_morale_factor | Ship Recovery Rate | 1 decimal place |
| naval_speed_factor | Naval Speed | 0 decimal places |
| navy_max_range | Naval max range | (no type listed) |
| navy_max_range_factor | Naval max range factor | 2 decimal places |
| navy_fuel_consumption_factor | Navy Fuel Consumption | 2 decimal places |

## Navy - Attrition & Visibility

| Modifier | Effect | Type |
|---|---|---|
| naval_attrition | Attrition | 2 decimal places |
| navy_visibility | Visibility | 2 decimal places |
| spotting_chance | Spotting Chance | 0 decimal places |
| ships_at_battle_start | Number of ships in the first contact | 0 decimal places |

## Navy - Positioning & Detection

| Modifier | Effect | Type |
|---|---|---|
| positioning | Positioning | 1 decimal place |
| naval_coordination | Fleet Coordination | 0 decimal places |
| naval_detection | Naval Detection | 0 decimal places |
| naval_strike | Naval Strike | 0 decimal places |

## Navy - Hit Chance & Targeting

| Modifier | Effect | Type |
|---|---|---|
| naval_hit_chance | Naval Hit Chance | 0 decimal places |
| strike_force_movement_org_loss | Strike Force Org loss | 2 decimal places |
| naval_has_potf_in_combat_attack | Attack when in combat alongside the Pride of the Fleet | 2 decimal places |
| naval_has_potf_in_combat_defense | Defense when in combat alongside the Pride of the Fleet | 2 decimal places |

## Navy - Casualties & Accidents

| Modifier | Effect | Type |
|---|---|---|
| navy_casualty_on_hit | Casualties factor on hit | 2 decimal places |
| navy_casualty_on_sink | Casualties on sink | 2 decimal places |
| naval_accidents_chance | Accident chance | 2 decimal places |
| critical_receive_chance | Chance to Receive Critical Hit | 1 decimal place |
| naval_critical_effect_factor | Effects of sustained Critical Hits | 2 decimal places |
| naval_critical_score_chance_factor | Chance to score Critical Hit | 2 decimal places |

## Navy - Ship Role Modifiers

Ship role modifiers follow the pattern `navy_<ship_role>_<stat>_factor` with 2 decimal places:

- submarine: navy_submarine_attack_factor, navy_submarine_defence_factor, navy_submarine_detection_factor
- screen: navy_screen_attack_factor, navy_screen_defence_factor
- capital_ship: navy_capital_ship_attack_factor, navy_capital_ship_defence_factor
- carrier_air: navy_carrier_air_attack_factor, navy_carrier_air_targetting_factor, navy_carrier_air_agility_factor

## Navy - Screening & Escort

| Modifier | Effect | Type |
|---|---|---|
| screening_efficiency | Screening Efficiency | 1 decimal place |
| convoy_escort_efficiency | Escort efficiency | 1 decimal place |
| submarine_attack | Submarine Attack | 1 decimal place |
| convoy_raiding_efficiency_factor | Convoy Raiding Efficiency | 2 decimal places |

## Navy - Sortie & Carrier

| Modifier | Effect | Type |
|---|---|---|
| sortie_efficiency | Sortie efficiency | 0 decimal places |
| fighter_sortie_efficiency | Fighters sortie efficiency | 0 decimal places |
| carrier_traffic | Carrier Traffic | 0 decimal places |
| carrier_capacity_penalty_reduction | Carrier overcrowding | 1 decimal place |
| port_strike | Port strikes | 1 decimal place |

## Navy - Mines

| Modifier | Effect | Type |
|---|---|---|
| naval_mine_hit_chance | Chance to hit naval mine | 2 decimal places |
| naval_mines_damage_factor | Naval mines damage | 0 decimal places |
| naval_mines_effect_reduction | Naval mines avoidance | 0 decimal places |
| mines_planting_by_fleets_factor | Naval minelaying efficiency | 0 decimal places |
| mines_sweeping_by_fleets_factor | Naval minesweeping efficiency | 0 decimal places |

## Navy - Torpedoes

| Modifier | Effect | Type |
|---|---|---|
| naval_torpedo_hit_chance_factor | Torpedo hit chance | 2 decimal places |
| naval_torpedo_reveal_chance_factor | Torpedo reveal chance | 2 decimal places |
| naval_torpedo_screen_penetration_factor | Torpedo screen penetration | 2 decimal places |
| naval_torpedo_cooldown_factor | Torpedo cooldown | 2 decimal places |

## Navy - Anti-Air & Retreat

| Modifier | Effect | Type |
|---|---|---|
| navy_anti_air_attack | Naval AA attack | 1 decimal place |
| navy_anti_air_attack_factor | Naval AA attack | 2 decimal places |
| naval_retreat_chance | Retreat Decision Chance | 0 decimal places |
| naval_retreat_speed | Fleet speed while retreating | 0 decimal places |
| sub_retreat_speed | Submarine speed while retreating | 0 decimal places |
| convoy_retreat_speed | Convoy speed while retreating | 0 decimal places |
| naval_enemy_retreat_chance | Enemy retreat chance | 2 decimal places |
| naval_enemy_fleet_size_ratio_penalty_factor | Enemy fleet size penalty | 2 decimal places |

## Navy - Leaders & Experience

| Modifier | Effect | Type |
|---|---|---|
| navy_leader_cost_factor | Navy Leader Cost | 1 decimal place |
| female_random_admiral_chance | Added Female Admiral Chance | 0 decimal places |
| navy_leader_start_level | Starting level of new navy leaders | 0 decimal places |
| navy_leader_start_attack_level | Starting Attack skill level of new navy leaders | 0 decimal places |
| navy_leader_start_defense_level | Starting Defense skill level of new navy leaders | 0 decimal places |
| navy_leader_start_maneuvering_level | Starting Maneuvering skill level of new navy leaders | 0 decimal places |
| navy_leader_start_coordination_level | Starting Coordination skill level of new navy leaders | 0 decimal places |
| experience_gain_navy | Naval Experience Gain | 2 decimal places |
| experience_gain_navy_factor | Naval Experience Gain | 1 decimal place |
| experience_gain_navy_unit_factor | Ship Experience Gain | 1 decimal place |
| experience_gain_navy_unit | Ship Experience Gain | 1 decimal place |

## Navy - Production & Refitting

| Modifier | Effect | Type |
|---|---|---|
| production_cost_max_convoy | Convoy Max Cost | 0 decimal places |
| production_cost_max_ship_hull_submarine | Submarine Hull Max Cost | 0 decimal places |
| production_cost_max_ship_hull_light | Light Hull Max Cost | 0 decimal places |
| production_cost_max_ship_hull_heavy | Heavy Hull Max Cost | 0 decimal places |
| production_cost_max_ship_hull_cruiser | Cruiser Hull Max Cost | 0 decimal places |
| production_cost_max_ship_hull_carrier | Carrier Hull Max Cost | 0 decimal places |
| refit_speed | Naval Equipment Refitting Speed | 0 decimal places |
| refit_ic_cost | Naval Equipment Refitting Cost | 0 decimal places |
| repair_speed_factor | Ship Repair Speed | 0 decimal places |

## Invasion & Amphibious

| Modifier | Effect | Type |
|---|---|---|
| transport_capacity | Troop convoy requirements | 2 decimal places |
| invasion_preparation | Invasion Preparation Time | 1 decimal place |
| naval_invasion_prep_speed | Invasion Preparation Speed | 1 decimal place |
| naval_invasion_capacity | Naval Invasion Capacity | 0 decimal places |
| naval_invasion_penalty | Invasion Penalty (can be applied to a state) | 0 decimal places |
| amphibious_invasion | Amphibious Invasion Speed | 1 decimal place |
| amphibious_invasion_defence | Invasion Defense (can be applied to a state) | 0 decimal places |

## Ideology & Stability

| Modifier | Effect | Type |
|---|---|---|
| democratic_drift | Daily Democratic Support | 2 decimal places |
| communism_drift | Daily Communism Support | 2 decimal places |
| fascism_drift | Daily Fascism Support | 2 decimal places |
| neutrality_drift | Daily Neutrality Support | 2 decimal places |
| democratic_acceptance | Acceptance of Democratic Diplomacy | 2 decimal places |
| communism_acceptance | Acceptance of Communism Diplomacy | 2 decimal places |
| fascism_acceptance | Acceptance of Fascism Diplomacy | 2 decimal places |
| neutrality_acceptance | Acceptance of Neutrality Diplomacy | 2 decimal places |
| drift_defence_factor | Ideology drift defense | 1 decimal place |
| master_ideology_drift | Master Ideology Drift | 2 decimal places |

## Political Power

| Modifier | Effect | Type |
|---|---|---|
| political_power_cost | Daily Political Power Cost | 0 decimal places |
| political_power_gain | Daily Political Power Gain | 2 decimal places |
| political_power_factor | Political Power Gain | 2 decimal places |

## Stability & War Support

| Modifier | Effect | Type |
|---|---|---|
| stability_factor | Stability | 2 decimal places |
| stability_weekly | Weekly Stability | 2 decimal places |
| stability_weekly_factor | Weekly Stability Gain | 2 decimal places |
| party_popularity_stability_factor | Party Popularity Stability Modifier | 2 decimal places |
| war_stability_factor | War Penalty Stability Modifier | 2 decimal places |
| defensive_war_stability_factor | Defensive War Penalty Stability Modifier | 2 decimal places |
| offensive_war_stability_factor | Offensive War Penalty Stability Modifier | 2 decimal places |
| war_support_factor | War Support | 2 decimal places |
| war_support_weekly | Weekly War Support | 2 decimal places |
| war_support_weekly_factor | Weekly War Support Gain | 2 decimal places |

## Command Power

| Modifier | Effect | Type |
|---|---|---|
| command_power_gain | Daily Command Power Gain | 2 decimal places |
| command_power_gain_mult | Daily Command Power Gain Multiplier | 0 decimal places |
| max_command_power | Maximum Command Power Increase | 0 decimal places |
| max_command_power_mult | Maximum Command Power Increase Multiplier | 0 decimal places |

## Surrender Limit

| Modifier | Effect | Type |
|---|---|---|
| surrender_limit | Surrender Limit | 2 decimal places |
| forced_surrender_limit | Surrender Limit (forced) | 2 decimal places |
| max_surrender_limit_offset | Minimum Surrender Limit | 2 decimal places |

## Population & Conscription

| Modifier | Effect | Type |
|---|---|---|
| monthly_population | Monthly Population | 1 decimal place |
| conscription | Recruitable Population | 2 decimal places |
| conscription_factor | Recruitable Population Factor | 0 decimal places |
| recruitable_population | Additional Recruitable Population | 3 decimal places |
| recruitable_population_factor | Recruitable Population | 2 decimal places |
| non_core_manpower | Non-core Manpower | 2 decimal places |
| weekly_manpower | Weekly Manpower | 0 decimal places |
| mobilization_speed | Mobilization speed | 2 decimal places |

## Research & Technology

| Modifier | Effect | Type |
|---|---|---|
| research_speed_factor | Research Speed | 2 decimal places |
| research_sharing_per_country_bonus | Technology sharing bonus | 2 decimal places |
| research_sharing_per_country_bonus_factor | Technology sharing bonus | 2 decimal places |
| land_doctrine_cost_factor | Land doctrine cost (example: -0.05 for 5% reduction) | 2 decimal places; percentual |

## Trade & Commerce

| Modifier | Effect | Type |
|---|---|---|
| civilian_factory_use | Civilian Factory Use | 0 decimal places |
| consumer_goods_factor | Consumer Goods Factories | 2 decimal places |
| min_export | Resources to Market | 2 decimal places |
| trade_opinion_factor | Trade deal opinion factor | 2 decimal places |
| faction_trade_opinion_factor | Faction trade deal opinion factor | 2 decimal places |
| trade_cost_for_target_factor | Target country trade cost | 2 decimal places |
| extra_trade_to_target_factor | Extra trade to overlord | 2 decimal places |
| overlord_trade_cost_factor | Overlord trade cost | 2 decimal places |
| extra_trade_to_overlord_factor | Extra trade to overlord | 2 decimal places |

## Relations & Diplomacy

| Modifier | Effect | Type |
|---|---|---|
| improve_relations_maintain_cost_factor | Improve relations maintain cost | 0 decimal places |
| opinion_gain_monthly | Improve relations opinion | 1 decimal place |
| opinion_gain_monthly_factor | Improve relations opinion | 2 decimal places |
| opinion_gain_monthly_same_ideology | Same ideology monthly opinion | 1 decimal place |
| opinion_gain_monthly_same_ideology_factor | Same ideology monthly opinion | 2 decimal places |
| guarantee_cost | Guarantee Cost | 0 decimal places |
| guarantee_tension | Guarantee tension limit | 1 decimal place |
| join_faction_tension | Join faction tension limit | 1 decimal place |

## Subversion & War Goals

| Modifier | Effect | Type |
|---|---|---|
| subversive_activites_upkeep | Subversive activities cost | 0 decimal places |
| foreign_subversive_activities | Foreign subversive activities efficiency | 0 decimal places |
| justify_war_goal_time | Justify war goal time | 1 decimal place |
| justify_war_goal_when_in_major_war_time | Justify war goal time when at war with a major | 1 decimal place |
| generate_wargoal_tension | Generate war goal tension limit | 1 decimal place |
| generate_wargoal_tension_against | Generate war goal tension limit against country | 1 decimal place |
| civil_war_involvement_tension | Civil war involvement tension | 1 decimal place |
| enemy_justify_war_goal_time | Justify war goal time on us | 1 decimal place |
| enemy_declare_war_tension | Declare war tension on us | 1 decimal place |

## Volunteers & Diplomacy

| Modifier | Effect | Type |
|---|---|---|
| send_volunteer_divisions_required | Divisions required for sending volunteer force | 1 decimal place |
| send_volunteer_size | Max volunteer force divisions | 0 decimal places |
| send_volunteer_factor | Max volunteer force divisions | 1 decimal place |
| send_volunteers_tension | Send volunteers tension limit | 1 decimal place |
| air_volunteer_cap | Air volunteer cap | 0 decimal places |

## Occupation & Compliance

| Modifier | Effect | Type |
|---|---|---|
| no_compliance_gain | No Compliance Gain | Boolean |
| starting_compliance | Starting Compliance | 0 decimal places |
| required_garrison_factor | Required Garrisons (state modifier) | 0 decimal places |
| compliance_gain | Daily Compliance Gain (state modifier) | 3 decimal places |
| compliance_growth | Compliance Growth Speed (state modifier) | 0 decimal places |
| compliance_growth_on_our_occupied_states | Compliance Growth Speed in our states occupied by the enemy (state modifier) | 0 decimal places |

## Resistance

| Modifier | Effect | Type |
|---|---|---|
| resistance_activity | Resistance Activity Chance (state modifier) | 1 decimal place |
| resistance_garrison_penetration_chance | Garrison Penetration Chance (state modifier) | 2 decimal places |
| resistance_growth | Resistance Growth Speed (state modifier) | 0 decimal places |
| resistance_growth_on_our_occupied_states | Resistance Growth Speed in our states occupied by the enemy (state modifier) | 0 decimal places |
| resistance_decay | Resistance Decay Speed (state modifier) | 0 decimal places |
| resistance_decay_on_our_occupied_states | Resistance Decay Speed in our states occupied by the enemy (state modifier) | 0 decimal places |
| resistance_target | Resistance Target (state modifier) | 0 decimal places |
| resistance_target_on_our_occupied_states | Resistance Target in our states occupied by the enemy (state modifier) | 0 decimal places |
| resistance_damage_to_garrison | Damage to Garrisons (state modifier) | 2 decimal places |
| resistance_damage_to_garrison_on_our_occupied_states | Damage to Enemy Garrisons in our states occupied by the enemy (state modifier) | 2 decimal places |

## Legitimacy & Exile

| Modifier | Effect | Type |
|---|---|---|
| legitimacy_daily | Daily Legitimacy Gain | 2 decimal places |
| targeted_legitimacy_daily | Daily Legitimacy Gain (targeted) | 1 decimal place |
| legitimacy_gain_factor | Legitimacy Gain | 0 decimal places |
| exile_manpower_factor | Daily Exile Manpower | 2 decimal places |

## Autonomy

| Modifier | Effect | Type |
|---|---|---|
| puppet_cost_factor | Puppet cost | 1 decimal place |
| occupation_cost | Occupation Cost | 2 decimal places |
| annex_cost_factor | Annex cost | 1 decimal place |
| subjects_autonomy_gain | Master impact | 1 decimal place |
| autonomy_gain | Daily autonomy progress gain | 1 decimal place |
| autonomy_gain_global_factor | All autonomy gain | 1 decimal place |
| autonomy_gain_warscore | Freedom gain by war score | 2 decimal places |
| autonomy_gain_trade | Freedom gain by trade | 2 decimal places |
| autonomy_gain_trade_factor | Freedom gain by trade | 2 decimal places |
| autonomy_gain_ll_to_subject | Freedom gain by subject from lend lease from overlord | 2 decimal places |
| autonomy_gain_ll_to_subject_factor | Freedom gain by subject from lend lease from overlord | 2 decimal places |
| autonomy_gain_ll_to_overlord | Freedom gain by lend lease to overlord | 2 decimal places |
| autonomy_gain_ll_to_overlord_factor | Freedom gain by lend lease to overlord | 2 decimal places |

## Master-Subject Relations

| Modifier | Effect | Type |
|---|---|---|
| autonomy_manpower_share | Subject manpower requirement | 2 decimal places |
| license_subject_master_purchase_cost | License cost between subject and master | 2 decimal places |
| can_master_build_for_us | Master can build constructions on the subject's territory | Boolean |
| master_build_autonomy_factor | Autonomy from building | Boolean |
| cic_to_overlord_factor | Civilian industry to overlord | 2 decimal places |
| mic_to_overlord_factor | Military industry to overlord | 2 decimal places |
| cic_to_target_factor | Civilian industry to target country | 2 decimal places |
| mic_to_target_factor | Military industry to target country | 2 decimal places |

## Fuel & Energy

| Modifier | Effect | Type |
|---|---|---|
| production_oil_factor | Synthetic Oil | 0 decimal places |
| fuel_cost | Fuel Cost | 0 decimal places |
| base_fuel_gain | Fuel Gain | 2 decimal places |
| base_fuel_gain_factor | Fuel Gain | 2 decimal places |
| fuel_gain | Fuel Gain per Oil | 0 decimal places |
| fuel_gain_factor | Fuel Gain per Oil | 2 decimal places |
| fuel_gain_from_states | Fuel Gain from Refineries | 2 decimal places |
| fuel_gain_factor_from_states | Fuel Gain from Refineries | 2 decimal places |
| max_fuel | Fuel Capacity (K) | 2 decimal places |
| max_fuel_building | Fuel Capacity (K) | 2 decimal places |
| max_fuel_factor | Fuel Capacity | 2 decimal places |
| army_fuel_capacity_factor | Army Fuel Capacity | 2 decimal places |
| army_fuel_consumption_factor | Army Fuel Consumption | 2 decimal places |
| air_fuel_consumption_factor | Air Fuel Consumption | 2 decimal places |
| navy_fuel_consumption_factor | Navy Fuel Consumption | 2 decimal places |

## Factory Donations & Buildings

| Modifier | Effect | Type |
|---|---|---|
| industrial_factory_donations | Industrial Factory Donations | 0 decimal places |
| military_factory_donations | Military Factory Donations | 0 decimal places |
| dockyard_donations | Dockyard Donations | 0 decimal places |
| global_building_slots | Max Factories in a State | 0 decimal places |
| global_building_slots_factor | Max Factories in a State | 0 decimal places |

## Construction Speed

| Modifier | Effect | Type |
|---|---|---|
| production_speed_buildings_factor | Construction Speed | 2 decimal places |
| production_speed_infrastructure_factor | Infrastructure construction speed | 2 decimal places |
| production_speed_rail_way_factor | Railway construction speed | 2 decimal places |
| production_speed_supply_node_factor | Supply node construction speed | 2 decimal places |
| production_speed_industrial_complex_factor | Industrial complex construction speed | 2 decimal places |
| production_speed_arms_factory_factor | Arms factory construction speed | 2 decimal places |
| production_speed_dockyard_factor | Dockyard construction speed | 2 decimal places |
| production_speed_fuel_silo_factor | Fuel silo construction speed | 2 decimal places |
| production_speed_synthetic_refinery_factor | Synthetic refinery construction speed | 2 decimal places |
| production_speed_naval_base_factor | Naval base construction speed | 2 decimal places |
| production_speed_radar_station_factor | Radar station construction speed | 2 decimal places |
| production_speed_air_base_factor | Air base construction speed | 2 decimal places |
| production_speed_anti_air_building_factor | Anti-air building construction speed | 2 decimal places |
| production_speed_bunker_factor | Bunker construction speed | 2 decimal places |
| production_speed_coastal_bunker_factor | Coastal bunker construction speed | 2 decimal places |
| production_speed_rocket_site_factor | Rocket site construction speed | 2 decimal places |
| production_speed_nuclear_reactor_factor | Nuclear reactor construction speed | 2 decimal places |

## Conversion & Efficiency

| Modifier | Effect | Type |
|---|---|---|
| conversion_cost_civ_to_mil_factor | Civilian to Military Factory conversion cost | 2 decimal places |
| conversion_cost_mil_to_civ_factor | Military to Civilian Factory conversion cost | 2 decimal places |

## Factory Output & Production

| Modifier | Effect | Type |
|---|---|---|
| industrial_capacity_factory | Factory Output | 2 decimal places |
| industrial_capacity_dockyard | Dockyard Output | 2 decimal places |
| production_factory_start_efficiency_factor | Production Efficiency Base | 2 decimal places |
| production_factory_max_efficiency_factor | Production Efficiency Cap | 2 decimal places |
| production_factory_efficiency_gain_factor | Production Efficiency growth | 2 decimal places |
| production_lack_of_resource_penalty_factor | Lack of Resources Penalty | 2 decimal places |
| line_change_production_efficiency_factor | Production Efficiency Retention | 2 decimal places |

## Repair Speed

| Modifier | Effect | Type |
|---|---|---|
| repair_speed_infrastructure_factor | Infrastructure repair speed | 2 decimal places |
| repair_speed_industrial_complex_factor | Industrial complex repair speed | 2 decimal places |
| repair_speed_arms_factory_factor | Arms factory repair speed | 2 decimal places |
| repair_speed_dockyard_factor | Dockyard repair speed | 2 decimal places |
| repair_speed_fuel_silo_factor | Fuel silo repair speed | 2 decimal places |
| repair_speed_synthetic_refinery_factor | Synthetic refinery repair speed | 2 decimal places |
| repair_speed_naval_base_factor | Naval base repair speed | 2 decimal places |
| repair_speed_radar_station_factor | Radar station repair speed | 2 decimal places |
| repair_speed_air_base_factor | Air base repair speed | 2 decimal places |
| repair_speed_anti_air_building_factor | Anti-air building repair speed | 2 decimal places |
| repair_speed_bunker_factor | Bunker repair speed | 2 decimal places |
| repair_speed_coastal_bunker_factor | Coastal bunker repair speed | 2 decimal places |
| repair_speed_rocket_site_factor | Rocket site repair speed | 2 decimal places |
| repair_speed_nuclear_reactor_factor | Nuclear reactor repair speed | 2 decimal places |

## Industry & Defense

| Modifier | Effect | Type |
|---|---|---|
| industry_free_repair_factor | Free repair | 2 decimal places |
| industry_repair_factor | Factory Repair Speed | 2 decimal places |
| industry_air_damage_factor | Factory Bomb Vulnerability | 2 decimal places |
| tech_air_damage_factor | Anti-Air Bombing Damage Reduction | 2 decimal places |
| static_anti_air_damage_factor | Static Anti Air damage factor | 2 decimal places |
| static_anti_air_hit_chance_factor | Static Anti Air hit chance factor | 2 decimal places |

## Nuclear Production

| Modifier | Effect | Type |
|---|---|---|
| nuclear_production | Allows Nuclear Bomb | Boolean |
| nuclear_production_factor | Nuclear Production | 0 decimal places |

## State-Level Building & Resources

| Modifier | Effect | Type |
|---|---|---|
| local_building_slots | Max Factories in State (state modifier) | 0 decimal places |
| local_building_slots_factor | Max Factories in State (state modifier) | 0 decimal places |
| local_factories | Local Factories (state modifier) | 0 decimal places |
| local_factory_sabotage | Chance to Sabotage Constructions (state modifier) | 0 decimal places |
| local_intel_to_enemies | Intel to Enemies (state modifier) | 0 decimal places |
| local_manpower | Local Manpower (state modifier) | 0 decimal places |
| local_non_core_manpower | Local Non-core Manpower (state modifier) | 2 decimal places |
| local_org_regain | Organization Regain (state modifier) | 2 decimal places |
| local_supplies | Local Supplies (state modifier) | 0 decimal places |
| local_supplies_for_controller | Local Supplies (state modifier) | 0 decimal places |
| local_resources | Local Resources (state modifier) | 0 decimal places |
| local_resources_factor | Resource Gain Efficiency (state modifier) | 2 decimal places |
| state_resources_factor | Local Available Resources (state modifier) | 0 decimal places |

## State Resource Modifiers

Resource modifiers follow the pattern for: aluminum, chromium, oil, rubber, steel, tungsten.

| Modifier | Effect | Type |
|---|---|---|
| state_resource_<resource> | <Resource> (state modifier) | 0 decimal places |
| temporary_state_resource_<resource> | <Resource> temporary (state modifier) | 0 decimal places |
| state_resource_cost_<resource> | <Resource> Consumption (state modifier) | 0 decimal places |
| country_resource_<resource> | <Resource> | 0 decimal places |
| country_resource_cost_<resource> | <Resource> Consumption | 0 decimal places |

## State Production Speed (by building type)

State-level building construction modifiers follow the pattern `state_production_speed_<building_type>_factor` with 2 decimal places:

- infrastructure, industrial_complex, arms_factory, dockyard, fuel_silo, synthetic_refinery, naval_base, radar_station, air_base, anti_air_building, bunker, coastal_bunker, rocket_site, nuclear_reactor

## State Repair Speed (by building type)

State-level repair modifiers follow the pattern `state_repair_speed_<building_type>_factor` with 2 decimal places (same building types as above).

## Equipment Upgrade Experience

| Modifier | Effect | Type |
|---|---|---|
| equipment_upgrade_xp_cost | Equipment Experience Cost (country modifier) | 0 decimal places |
| land_equipment_upgrade_xp_cost | Land Equipment Experience Cost (country modifier) | 0 decimal places |
| naval_equipment_upgrade_xp_cost | Naval Equipment Experience Cost (country modifier) | 0 decimal places |
| air_equipment_upgrade_xp_cost | Air Equipment Experience Cost (country modifier) | 0 decimal places |

## Equipment Conversion & Capture

| Modifier | Effect | Type |
|---|---|---|
| equipment_conversion_speed | Conversion speed bonus | 1 decimal place |
| equipment_capture | Equipment Capture Ratio Gain | 1 decimal place |
| equipment_capture_factor | Equipment Capture Ratio Modifier | 1 decimal place |

## Lend-Lease & Licenses

| Modifier | Effect | Type |
|---|---|---|
| lend_lease_tension | Lend-lease tension limit | 1 decimal place |
| license_purchase_cost | License purchase cost | 0 decimal places |
| license_production_speed | License production speed | 0 decimal places |
| license_tech_difference_speed | License production speed from technology difference | 0 decimal places |

## License Purchase & Production (by equipment archetype)

Modifiers follow patterns for: infantry, naval, air, armor

| Modifier | Effect | Type |
|---|---|---|
| license_infantry_purchase_cost | Infantry license purchase cost | 0 decimal places |
| license_naval_purchase_cost | Naval license purchase cost | 0 decimal places |
| license_air_purchase_cost | Air license purchase cost | 0 decimal places |
| license_armor_purchase_cost | Armor license purchase cost | 0 decimal places |
| license_<equipment>_eq_cost_factor | License purchase cost for <equipment> | 0 decimal places |
| license_<equipment>_eq_production_speed_factor | License production speed for <equipment> | 0 decimal places |
| license_<equipment>_eq_tech_difference_speed_factor | License production speed from technology difference for <equipment> | 0 decimal places |

Equipment types: infantry, artillery, anti_tank, light_tank

## Idea Costs

Idea group modifiers follow the pattern `<idea_group>_cost_factor` with 0 decimal places:

- political_advisor_cost_factor
- economy_cost_factor
- trade_laws_cost_factor
- mobilization_laws_cost_factor
- army_chief_cost_factor
- navy_chief_cost_factor
- air_chief_cost_factor
- high_command_cost_factor
- theorist_cost_factor
- materiel_manufacturer_cost_factor
- naval_manufacturer_cost_factor
- aircraft_manufacturer_cost_factor
- tank_manufacturer_cost_factor
- industrial_concern_cost_factor
- country_cost_factor
- hidden_ideas_cost_factor

## Leader Costs & Abilities

| Modifier | Effect | Type |
|---|---|---|
| military_leader_cost_factor | Military Leader Cost | 1 decimal place |
| army_leader_cost_factor | Army Leader Cost | 1 decimal place |
| female_random_army_leader_chance | Added Female Army Leader Chance | 0 decimal places |
| female_random_country_leader_chance | Added Female Country Leader Chance | 0 decimal places |
| cannot_use_abilities | Cannot Use Combat Abilities | Boolean |
| skill_bonus_factor | Leader Skill Bonuses | 1 decimal place |

## Army Leader Skills

| Modifier | Effect | Type |
|---|---|---|
| army_leader_start_level | Starting level of new army leaders | 0 decimal places |
| army_leader_start_attack_level | Starting Attack skill level of new army leaders | 0 decimal places |
| army_leader_start_defense_level | Starting Defense skill level of new army leaders | 0 decimal places |
| army_leader_start_logistics_level | Starting Logistics skill level of new army leaders | 0 decimal places |
| army_leader_start_planning_level | Starting Planning skill level of new army leaders | 0 decimal places |

## Leader Reassignment & Health

| Modifier | Effect | Type |
|---|---|---|
| reassignment_duration_factor | Army reassignment duration | 1 decimal place |
| sickness_chance | Chance to Get Sick | 2 decimal places |
| wounded_chance_factor | Chance to get wounded in combat | 2 decimal places |

## Leader Promotions & Limits

| Modifier | Effect | Type |
|---|---|---|
| promote_cost_factor | Promotion Cost | 1 decimal place |
| max_commander_army_size | General Max Army Size | 0 decimal places |
| max_commander_army_group_size | General Max Army Group Size | 0 decimal places |
| max_marshal_army_size | Field Marshal Max Army Size | 0 decimal places |
| max_marshal_army_group_size | Field Marshal Max Army Group Size | 0 decimal places |

## Experience Gain - General

| Modifier | Effect | Type |
|---|---|---|
| experience_gain_factor | Leader Experience Gain | 1 decimal place |
| experience_gain_army | Army Experience Gain | 2 decimal places |
| experience_gain_army_factor | Army Experience Gain | 1 decimal place |
| experience_gain_army_unit | Division Experience Gain | 1 decimal place |
| experience_gain_army_unit_factor | Division Experience Gain | 1 decimal place |
| experience_loss_factor | Experienced soldier losses | 1 decimal place |

## Strategic Redeployment

| Modifier | Effect | Type |
|---|---|---|
| disable_strategic_redeployment | Strategic Redeployment Disabled | Boolean |
| disable_strategic_redeployment_for_controller | Strategic Redeployment Disabled (state modifier) | Boolean |

## Exile Divisions

| Modifier | Effect | Type |
|---|---|---|
| exiled_divisions_attack_factor | Exiled Divisions Attack | 2 decimal places |
| exiled_divisions_defense_factor | Exiled Divisions Defense | 2 decimal places |
| own_exiled_divisions_attack_factor | Own Exiled Divisions Attack | 2 decimal places |
| own_exiled_divisions_defense_factor | Own Exiled Divisions Defense | 2 decimal places |

## Unit Type Experience Gain

Experience gain modifiers exist for each unit type and context (training/combat). Pattern: `experience_gain_<unit_type>_training_factor` and `experience_gain_<unit_type>_combat_factor` with 0 decimal places.

Unit types include:

**Infantry units:** infantry, mountaineers, marine, paratrooper, bicycle_battalion

**Support companies:** engineer, recon, military_police, maintenance_company, field_hospital, logistics_company, signal_company

**Vehicle units:** cavalry, armored_car, armored_car_recon, motorized, motorized_rocket_brigade, mechanized, amphibious_mechanized

**Artillery:** mot_recon, artillery, rocket_artillery

**Light armor:** light_armor, light_sp_artillery_brigade, light_sp_anti_air_brigade, light_tank_destroyer_brigade, light_tank_recon

**Medium armor:** medium_armor, medium_sp_artillery_brigade, medium_sp_anti_air_brigade, medium_tank_destroyer_brigade

**Heavy armor:** heavy_armor, heavy_sp_artillery_brigade, heavy_sp_anti_air_brigade, heavy_sp_anti_tank_brigade, heavy_tank_destroyer_brigade

**Super heavy armor:** super_heavy_armor, super_heavy_sp_artillery_brigade, super_heavy_sp_anti_air_brigade, super_heavy_sp_anti_tank_brigade, super_heavy_tank_destroyer_brigade

**Modern armor:** modern_armor, modern_sp_artillery_brigade, modern_sp_anti_air_brigade, modern_tank_destroyer_brigade

**Amphibious:** amphibious_armor

**Naval units:** submarine, destroyer, light_cruiser, heavy_cruiser, battle_cruiser, battleship, carrier

**Air units:** fighter, cv_fighter, heavy_fighter, jet_fighter, cas, cv_cas, nav_bomber, cv_nav_bomber, tac_bomber, jet_tac_bomber, strat_bomber, jet_strat_bomber, transport_plane, scout_plane, rocket_interceptor, suicide_craft, guided_missile

## Notes

- All numbers support up to 3 decimal places internally; display format varies by modifier type.
- Some modifiers are parameterized and accept sub-parameters (e.g., operation_* modifiers take cost, outcome, risk).
- State modifiers can only be applied at state level and are marked `state modifier` in the source.
- Country modifiers apply to countries; unit-specific variants apply to individual unit types.
- Boolean modifiers enable/disable features; number modifiers scale effects.
