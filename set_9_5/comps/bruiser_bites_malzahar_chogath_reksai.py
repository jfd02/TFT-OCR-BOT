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
ACTIVE_FINAL_COMP_TRAITS = ["Bruiser", "Void", "Sorcerer"]

# just alphabetical order
INACTIVE_FINAL_COMP_TRAITS = ["Noxus", "Freljord", "Piltover", "Slayer", "Shurima", "Zaun"]

RECOMMENDED_LEGEND = "Lee Sin"

COMP = {
    "RekSai": {
        "board_position": 14,
        "best_in_slot": ["Bloodthirster", "TitansResolve", "InfinityEdge"],
        "secondary_items": ["Bloodthirster", "HandofJustice", "SteraksGage"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["SlayerEmblem"],
        "ornn_items_to_accept": ["GoldCollector", "InfinityForce", "ObsidianCleaver"],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "ChoGath": {
        "board_position": 22,
        "best_in_slot": ["BrambleVest", "DragonsClaw", "WarmogsArmor"],
        "secondary_items": ["Crownguard", "Evenshroud", "GargoyleStoneplate", "IonicSpark", "SunfireCape"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Malzahar": {
        "board_position": 0,
        "best_in_slot": ["ArchangelsStaff", "BlueBuff", "HextechGunblade"],
        "secondary_items": ["ArchangelsStaff", "GiantSlayer", "Guardbreaker", "JeweledGauntlet", "NashorsTooth", "RabadonsDeathcap", "SpearofShojin"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": ["DeathfireGrasp", "GoldmancersStaff", "SnipersFocus", "ZhonyasParadox"],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Silco": {
        "board_position": 3,
        "best_in_slot": ["Morellonomicon"],
        "secondary_items": ["BlueBuff", "JeweledGauntlet", "RabadonsDeathcap"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["BruiserEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Sion": {
        "board_position": 26,
        "best_in_slot": [],
        "secondary_items": ["AdaptiveHelm", "DragonsClaw", "SunfireCape", "WarmogsArmor"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["NoxusEmblem", "FreljordEmblem", "SlayerEmblem", "SorcererEmblem", "VoidEmblem"],
        "ornn_items_to_accept": ["BlacksmithsGloves"],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Sejuani": {
        "board_position": 27,
        "best_in_slot": [],
        "secondary_items": ["ProtectorsVow", "Redemption", "WarmogsArmor"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["PiltoverEmblem", "ShurimaEmblem", "VoidEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Vi": {
        "board_position": 25,
        "best_in_slot": [],
        "secondary_items": ["BrambleVest", "DragonsClaw", "IonicSpark", "SteraksGage"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["NoxusEmblem", "FreljordEmblem", "ShurimaEmblem", "VoidEmblem", "ZaunEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Renekton": {
        "board_position": 5,
        "best_in_slot": [],
        "secondary_items": ["GuinsoosRageblade", "Quicksilver"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["NoxusEmblem", "FreljordEmblem", "VoidEmblem"],
        "ornn_items_to_accept": ["DeathsDefiance", "InfinityForce"],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Mordekaiser": {
        "board_position": 23,
        "best_in_slot": ["JeweledGauntlet", "RapidFirecannon"],
        "secondary_items": ["Quicksilver", "RabadonsDeathcap"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    }
}

# No logic for certain augments meaning the bot won't know what to do if they are included in here
# (Anything that changes gameplay or adds something to the bench).
PRIMARY_AUGMENTS: list[str] = [
    "Bruiser Heart",
    "Cybernetic Bulk I",
    "Training Reward I",
    "Money!",

    "Bruiser Crest",
    "Cybernetic Bulk II",
    "Money Money!",
    "Titanic Strength",
    "Training Reward II",

    "Bruiser Crown",
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
