"""
Walk the Plank - S Tier
Comp from https://app.mobalytics.gg/tft/comps-guide/walk-the-plank-2UcDQkBTlGA2Y6MTIQOQXhAsWil
Strategy: Default: This comp uses the standard leveling strategy that revolves around a 4-cost carry.
Difficulty: Medium
Legend: Poro
Items are in camel case and a-Z
"""

STRATEGY = "Default"

DIFFICULTY = "Medium"

TRAITS = ["Bilgewater", "Reaver King", "Juggernaut", "Vanquisher", "Gunner"]

RECOMMENDED_LEGEND = "Poro"

COMP = {
    "Nilah": {
        "board_position": 15,
        "items_to_build": ["TitansResolve", "Bloodthirster", "RapidFirecannon"],
        "completed_items_to_accept": ["SteraksGage"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "radiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "final_comp": True
    },
    "Miss Fortune": {
        "board_position": 3,
        "items_to_build": ["JeweledGauntlet", "BlueBuff", "HextechGunblade"],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "radiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "final_comp": True
    },
    "Gangplank": {
        "board_position": 6,
        "items_to_build": ["SpearofShojin"],
        "completed_items_to_accept": ["Guardbreaker"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "radiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": True
    },
    "Nautilus": {
        "board_position": 24,
        "items_to_build": ["Redemption", "DragonsClaw", "BrambleVest"],
        "completed_items_to_accept": ["GargoyleStoneplate", "SunfireCape"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "radiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "final_comp": True
    },
    "Darius": {
        "board_position": 23,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["BastionEmblem", "BilgewaterEmblem", "RogueEmblem", "VanquisherEmblem"],
        "ornn_items_to_accept": [],
        "radiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": True
    },
    "Twisted Fate": {
        "board_position": 0,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["VanquisherEmblem"],
        "ornn_items_to_accept": [],
        "radiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "final_comp": True
    },
    "Graves": {
        "board_position": 25,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["JuggernautEmblem", "VanquisherEmblem"],
        "ornn_items_to_accept": [],
        "radiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "final_comp": True
    },
    "Illaoi": {
        "board_position": 22,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["JuggernautEmblem"],
        "ornn_items_to_accept": [],
        "radiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "final_comp": True
    },
    "Kassadin": {
        "board_position": 22,
        "items_to_build": ["Bloodthirster", "TitansResolve"],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "radiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": False
    }
}

# No logic for certain augments meaning the bot won't know what to do if they are included in here
# (Anything that changes gameplay or adds something to the bench).
PRIMARY_AUGMENTS: list[str] = [
    "Harmacist I",
    "Healing Orbs I"
    "Unified Resistance I",

    "Bilgewater Crest",
    "Dedication",
    "Rising Infamy",

    "Bilgewater Crown",
    "Impenetrable Bulwark",
    "Stationary Support III"
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
    "Magic Wand"
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
    "Strategist Soul",
    "Tiny Power III",
    "Unified Resistance III",
]
