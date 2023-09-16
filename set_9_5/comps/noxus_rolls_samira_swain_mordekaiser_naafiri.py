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
        "items_to_build": ["BlueBuff", "Bloodthirster", "EdgeofNight"],
        "completed_items_to_accept": ["BlueBuff", "Bloodthirster", "EdgeofNight", "GiantSlayer", "HandofJustice", "InfinityEdge"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["SlayerEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Swain": {
        "board_position": 25,
        "items_to_build": ["Crownguard", "ProtectorsVow", "GargoyleStoneplate"],
        "completed_items_to_accept": ["Crownguard", "Evenshroud", "GargoyleStoneplate",
                                      "ProtectorsVow", "Redemption", "SunfireCape", "WarmogsArmor"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["ChallengerEmblem", "InvokerEmblem", "JuggernautEmblem", "ShurimaEmblem", "SorcererEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Cassiopeia": {
        "board_position": 6,
        "items_to_build": ["HextechGunblade", "NashorsTooth"],
        "completed_items_to_accept": ["Guardbreaker", "HextechGunblade", "NashorsTooth"],
        "support_items_to_accept": ["Zephyr"],
        "trait_items_to_accept": ["VanquisherEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Mordekaiser": {
        "board_position": 13,
        "items_to_build": ["JeweledGauntlet", "RapidFirecannon"],
        "completed_items_to_accept": ["JeweledGauntlet", "Quicksilver", "RapidFirecannon"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["DarkinEmblem", "JuggernautEmblem", "SorcererEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Naafiri": {
        "board_position": 21,
        "items_to_build": ["ThiefsGloves"],
        "completed_items_to_accept": ["Quicksilver", "SpearofShojin", "ThiefsGloves", "TitansResolve"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["NoxusEmblem", "SlayerEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Darius": {
        "board_position": 4,
        "items_to_build": [],
        "completed_items_to_accept": ["SteraksGage"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["ChallengerEmblem", "DarkinEmblem", "ShurimaEmblem",
                                  "SlayerEmblem", "SorcererEmblem", "StrategistEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": ["ZaunEmblem"],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Warwick": {
        "board_position": 5,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["DarkinEmblem", "NoxusEmblem", "ShurimaEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Irelia": {
        "board_position": 12,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["DarkinEmblem", "NoxusEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
}

# No logic for certain augments meaning the bot won't know what to do if they are included in here
# (Anything that changes gameplay or adds something to the bench).
PRIMARY_AUGMENTS: list[str] = [
    "Challenger Heart",
    "Cybernetic Leech I",
    "Training Reward I",
    "Money!",

    "Challenger Crest",
    "Cybernetic Leech II",
    "Money Money!",
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

