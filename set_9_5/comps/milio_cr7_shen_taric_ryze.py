"""
Milio CR7 - ? Tier - Community Comp
This comp is a bit of a meme: CR7 refers to Cristiano Ronaldo and his jersey number.
Comp from https://app.mobalytics.gg/tft/comps-guide/millio-cr7-2VMjGJBsC4FWcslLvfM7pRG3Ekq
Strategy: Default: This comp uses the standard leveling strategy that revolves around a 4-cost carry.
Difficulty: Unknown
Legend: Caitlyn, Urf, Poro
Items are in camel case and a-Z
"""

NAME = "Milio CR7"

STRATEGY = "Default"

DIFFICULTY = "Medium"

TRAITS = ["Ixtal", "Wanderer", "Bastion", "Invoker", "Targon"]

RECOMMENDED_LEGEND = "Twisted Fate"

COMP = {
    "Milio": {
        "board_position": 0,
        "items_to_build": ["ArchangelsStaff", "BlueBuff", "JeweledGauntlet"],
        "completed_items_to_accept": ["ArchangelsStaff", "BlueBuff", "JeweledGauntlet", "GiantSlayer"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "final_comp": True
    },
    "Shen": {
        "board_position": 23,
        "items_to_build": ["BrambleVest", "DragonsClaw", "WarmogsArmor"],
        "completed_items_to_accept": ["BrambleVest", "DragonsClaw", "WarmogsArmor"],
        "support_items_to_accept": ["VirtueoftheMartyr", "ZzRotPortal"],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "final_comp": True
    },
    "Taric": {
        "board_position": 24,
        "items_to_build": ["IonicSpark", "Redemption", "SunfireCape"],
        "completed_items_to_accept": ["IonicSpark", "Redemption", "SunfireCape"],
        "support_items_to_accept": ["Crest of Cinders", "LocketoftheIronSolari", "RanduinsOmen", "VirtueoftheMartyr"],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": True
    },
    "Ryze": {
        "board_position": 2,
        "items_to_build": ["BlueBuff", "JeweledGauntlet"],
        "completed_items_to_accept": ["BlueBuff", "JeweledGauntlet"],
        "support_items_to_accept": ["NeedlesslyBigGem", "Zephyr"],
        "trait_items_to_accept": ["IxtalEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "final_comp": True
    },
    "Neeko": {
        "board_position": 21,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": ["VirtueoftheMartyr"],
        "trait_items_to_accept": ["InvokerEmblem", "TargonEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": True
    },
    "Soraka": {
        "board_position": 4,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["IxtalEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": True
    },
    "Kassadin": {
        "board_position": 25,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": ["VirtueoftheMartyr"],
        "trait_items_to_accept": ["InvokerEmblem", "IxtalEmblem", "TargonEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": True
    },
    "Qiyana": {
        "board_position": 20,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": ["Obsidian Cleaver"],
        "trait_items_to_accept": ["InvokerEmblem", "TargonEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": True
    },
    "Ahri": {
        "board_position": 6,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": ["Zephyr"],
        "trait_items_to_accept": ["IxtalEmblem", "TargonEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": True
    },
    "Poppy": {
        "board_position": 17,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["InvokerEmblem", "IxtalEmblem", "TargonEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": False
    },
    "Galio": {
        "board_position": 16,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["IxtalEmblem", "TargonEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": False
    },
    "Kayle": {
        "board_position": 3,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["InvokerEmblem", "IxtalEmblem", "TargonEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": False
    }
}

# No logic for certain augments meaning the bot won't know what to do if they are included in here
# (Anything that changes gameplay or adds something to the bench).
PRIMARY_AUGMENTS: list[str] = [
    "Pandora's Items",
    "Red Buff"
    "Army Building",

    "Early Education",
    "Magic Wand",
    "Social Distancing II",

    "Golden Ticket",
    "Pandora's Box",
    "Social Distancing III"
]

SECONDARY_AUGMENTS: list[str] = [
    "Battle Ready I",
    "Money!",
    "Pandora's Items I",
    "Tiny Power I",

    "Ascension",
    "Balanced Budget II",
    "Battle Ready II",
    "Last Stand",
    "Money Money!",
    "Pandora's Items II",
    "Patient Study",
    "Pumping Up II",
    "Tiny Power II",
    "Unified Resistance II",
    "You Have My Bow",

    "Battle Ready III",
    "Final Ascension",
    "Lucky Gloves",
    "Money Money Money!",
    "Pandora's Items III",
    "Tiny Power III",
    "Unified Resistance III",
]
