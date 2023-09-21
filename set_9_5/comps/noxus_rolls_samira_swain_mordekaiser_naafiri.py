"""
Noxus Rolls - S Tier - Meta Comp
Tip: DON'T LEVEL UP
Comp from https://app.mobalytics.gg/tft/comps-guide/noxus-rolls-2VTkBpEpG2dgiVmjbQPJWXknUFY
Set: 9.5
Strategy: Slow Roll: This comp rolls gold above 50 to look for 3-star champions.
Difficulty: Easy
Legend: Lee Sin
"""

NAME = "Noxus Rolls"

STRATEGY = "Slow Roll"

DIFFICULTY = "Easy"

# In the order from most active to least active.
ACTIVE_FINAL_COMP_TRAITS = ["Darkin", "Noxus", "Challenger", "Shurima", "Juggernaut"]

# just alphabetical order
INACTIVE_FINAL_COMP_TRAITS = ["Invoker", "Slayer", "Sorcerer", "Strategist", "Vanquisher", "Zaun"]

RECOMMENDED_LEGEND = "Lee Sin"

COMP = {
    "Samira": {
        "board_position": 0,
        "best_in_slot": ["BlueBuff", "Bloodthirster", "EdgeofNight"],
        "secondary_items": ["GiantSlayer", "HandofJustice", "InfinityEdge", "GuinsoosRageblade"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["SlayerEmblem"],
        "ornn_items_to_accept": ["GoldCollector", "InfinityForce", "ObsidianCleaver", "SnipersFocus"],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Swain": {
        "board_position": 25,
        "best_in_slot": ["Crownguard", "ProtectorsVow", "GargoyleStoneplate"],
        "secondary_items": ["Evenshroud", "IonicSpark", "Redemption", "SunfireCape", "WarmogsArmor"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["ChallengerEmblem", "InvokerEmblem", "JuggernautEmblem", "ShurimaEmblem", "SorcererEmblem"],
        "ornn_items_to_accept": ["AnimaVisage", "EternalWinter", "Hullcrusher", "MogulsMail", "ObsidianCleaver"],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Cassiopeia": {
        "board_position": 6,
        "best_in_slot": ["HextechGunblade", "NashorsTooth"],
        "secondary_items": ["ArchangelsStaff", "Guardbreaker", "RabadonsDeathcap"],
        "support_items_to_accept": ["Zephyr"],
        "trait_items_to_accept": ["VanquisherEmblem"],
        "ornn_items_to_accept": ["DeathfireGrasp", "GoldmancersStaff", "ZhonyasParadox"],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Mordekaiser": {
        "board_position": 13,
        "best_in_slot": ["JeweledGauntlet", "RapidFirecannon"],
        "secondary_items": ["Quicksilver", "RabadonsDeathcap"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["DarkinEmblem", "JuggernautEmblem", "SorcererEmblem"],
        "ornn_items_to_accept": ["EternalWinter", "GoldmancersStaff", "TrickstersGlass", "ZhonyasParadox"],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Sion": {
        "board_position": 27,
        "best_in_slot": ["DragonsClaw", "SunfireCape", "WarmogsArmor"],
        "secondary_items": ["AdaptiveHelm"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Naafiri": {
        "board_position": 21,
        "best_in_slot": ["ThiefsGloves"],
        "secondary_items": ["Quicksilver", "SpearofShojin", "ThiefsGloves", "TitansResolve"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["NoxusEmblem", "SlayerEmblem"],
        "ornn_items_to_accept": ["BlacksmithsGloves"],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Darius": {
        "board_position": 4,
        "best_in_slot": [],
        "secondary_items": ["TitansResolve", "SteraksGage"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["ChallengerEmblem", "DarkinEmblem", "ShurimaEmblem",
                                  "SlayerEmblem", "SorcererEmblem", "StrategistEmblem"],
        "ornn_items_to_accept": ["Muramana", "RocketPropelledFist"],
        "zaun_items_to_accept": ["ZaunEmblem"],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Warwick": {
        "board_position": 5,
        "best_in_slot": [],
        "secondary_items": ["GuinsoosRageblade", "Quicksilver"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["DarkinEmblem", "NoxusEmblem", "ShurimaEmblem"],
        "ornn_items_to_accept": ["DeathsDefiance", "InfinityForce"],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Aatrox": {
        "board_position": 23,
        "best_in_slot": ["Bloodthirster", "Quicksilver", "TitansResolve"],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    }
}

# No logic for certain augments meaning the bot won't know what to do if they are included in here
# (Anything that changes gameplay or adds something to the bench).
PRIMARY_AUGMENTS: list[str] = [
    "Army Building",
    "Challenger Heart",
    "Cybernetic Leech I",
    "Training Reward I",
    "Money!",

    "Challenger Crest",
    "Cybernetic Leech II",
    "Frequent Flier",
    "Money Money!",
    "Total Domination",
    "Training Reward II",

    "Challenger Crown",
    "Cybernetic Leech III",
    "Money Money Money!",
    "Training Reward III",
]
SECONDARY_AUGMENTS: list[str] = [
    "Balanced Budget I",
    "Battle Ready I",
    "Blood Money",
    "Buried Treasures I",
    "Gotta Go Fast!!! I",
    "Jeweled Lotus I",
    "Money!",
    "On a Roll",
    "Pandora's Items",
    "Partial Ascension",
    "Rolling for Days I",
    "Social Distancing I",
    "Tiny Power I",
    "Tiny Titans",
    "Unified Resistance I",

    "Ancient Archives I",
    "Ascension",
    "Balanced Budget II",
    "Battle Ready II",
    "Buried Treasures II",
    "Capricious Forge",
    "Dedication",
    "Demon Flare",
    "Early Education",
    "Escort Quest",
    "Gotta Go Fast!!! II",
    "Infusion",
    "Jeweled Lotus II",
    "Last Stand",
    "Metabolic Accelerator",
    "Money Money!",
    "Pandora's Items II",
    "Rolling for Days II",
    "Shoplifting",
    "Stars Are Born",
    "Support Cache"
    "Tiny Power II",
    "Tons of Stats!",
    "Unified Resistance II",
    "What Doesn't Kill You",

    "Ancient Archives II",
    "Balanced Budget III",
    "Battle Ready III",
    "Binary Airdrop",
    "Buried Treasure III",
    "Caretaker's Chosen",
    "Final Ascension",
    "Final Reserves",
    "Giant Grab Bag",
    "Golden Ticket",
    "Gotta Go Fast!!! III",
    "Impenetrable Bulwark",
    "Jeweled Lotus III",
    "Living Forge",
    "Lucky Gloves",
    "Money Money Money!",
    "Pandora's Box",
    "Radiant Relics",
    "Roll The Dice",
    "Shopping Spree",
    "Tiniest Titan",
    "Tiny Power III",
    "Unified Resistance III",
    "Wandering Trainer",
    "Wellness Trust"
]
