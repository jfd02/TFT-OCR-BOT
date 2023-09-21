"""
Mage Spam - A Tier - Meta Comp
Comp from https://app.mobalytics.gg/tft/comps-guide/magespam-2VMPSMjQZr2opnuTKOppIiafElN
Set: 9.5
Strategy: Fast 8: This comp looks to level up to 8 aggressively with a strong economy.
Difficulty: Medium
Legend: Twisted Fate
"""

NAME = "Mage Spam"

STRATEGY = "Fast 8"

DIFFICULTY = "Medium"

# In the order from most active to least active.
ACTIVE_FINAL_COMP_TRAITS = ["Sorcerer", "Strategist", "Bastion", "Invoker", "Targon"]

# just alphabetical order
INACTIVE_FINAL_COMP_TRAITS = ["Demacia", "Ionia", "Multicaster", "Noxus", "Void", "Zaun"]

RECOMMENDED_LEGEND = "Twisted Fate"

COMP = {
    "Silco": {
        "board_position": 0,
        "best_in_slot": ["BlueBuff", "HextechGunblade", "JeweledGauntlet"],
        "secondary_items": ["GiantSlayer", "Guardbreaker", "Morellonomicon", "SpearofShojin"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": ["DeathfireGrasp", "GoldmancersStaff", "Muramana", "SnipersFocus"],
        "zaun_items_to_accept": ["AdaptiveImplant", "VirulentBioware"],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Shen": {
        "board_position": 23,
        "best_in_slot": ["IonicSpark", "SorcererEmblem", "SunfireCape"],
        "secondary_items": ["Crownguard", "GargoyleStoneplate"],
        "support_items_to_accept": ["Crest of Cinders", "LocketoftheIronSolari", "RanduinsOmen", "VirtueoftheMartyr"],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": ["EternalWinter", "MogulsMail"],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Taric": {
        "board_position": 24,
        "best_in_slot": ["BrambleVest", "DragonsClaw", "WarmogsArmor"],
        "secondary_items": ["GargoyleStoneplate", "Redemption"],
        "support_items_to_accept": ["Crest of Cinders", "LocketoftheIronSolari", "RanduinsOmen", "VirtueoftheMartyr"],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": ["AnimaVisage", "EternalWinter", "MogulsMail"],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Ahri": {
        "board_position": 4,
        "best_in_slot": ["BlueBuff", "JeweledGauntlet"],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["InvokerEmblem", "StrategistEmblem"],
        "ornn_items_to_accept": ["BlacksmithsGloves", "ZhonyasParadox"],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Jarvan IV": {
        "board_position": 21,
        "best_in_slot": [],
        "secondary_items": ["ProtectorsVow"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["BastionEmblem", "NoxusEmblem", "TargonEmblem", "VoidEmblem", "ZaunEmblem"],
        "ornn_items_to_accept": ["BlacksmithsGloves", "InfinityForce", "RocketPropelledFist", "TrickstersGlass"],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "VelKoz": {
        "board_position": 13,
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": ["Zephyr"],
        "trait_items_to_accept": ["InvokerEmblem"],
        "ornn_items_to_accept": ["BlacksmithsGloves", "GoldCollector", "GoldmancersStaff", "SnipersFocus"],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Swain": {
        "board_position": 26,
        "best_in_slot": [],
        "secondary_items": ["AdaptiveHelm", "Crownguard", "ProtectorsVow", "GargoyleStoneplate"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["DemaciaEmblem", "MulticasterEmblem", "TargonEmblem"],
        "ornn_items_to_accept": ["BlacksmithsGloves", "DeathsDefiance", "EternalWinter", "Hullcrusher"],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Soraka": {
        "board_position": 2,
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": ["NeedlesslyBigGem"],
        "trait_items_to_accept": ["MulticasterEmblem"],
        "ornn_items_to_accept": ["ZhonyasParadox"],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Taliyah": {
        "board_position": 3,
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Kassadin": {
        "board_position": 22,
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Galio": {
        "board_position": 25,
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Malzahar": {
        "board_position": 5,
        "best_in_slot": ["BlueBuff", "JeweledGauntlet"],
        "secondary_items": [],
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
    "Pandora's Items",
    "Social Distancing I",
    "Sorcerer Heart",

    "Magic Wand",
    "Overcharged Manafont",
    "Social Distancing II",
    "Sorcerer Crest",

    "Golden Ticket",
    "Social Distancing III",
    "Sorcerer Crown",
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
