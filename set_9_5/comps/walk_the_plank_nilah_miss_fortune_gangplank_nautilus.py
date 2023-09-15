"""
Walk the Plank - S Tier
Comp from https://app.mobalytics.gg/tft/comps-guide/walk-the-plank-2UcDQkBTlGA2Y6MTIQOQXhAsWil
Set: 9.5
Strategy: Default: This comp uses the standard leveling strategy that revolves around a 4-cost carry.
Difficulty: Medium
Legend: Poro
"""

NAME = "Walk the Plank"

STRATEGY = "Default"

DIFFICULTY = "Medium"

# In the order from most active to least active.
ACTIVE_FINAL_COMP_TRAITS = ["Bilgewater", "Reaver King", "Juggernaut", "Vanquisher", "Gunner"]

# just alphabetical order
INACTIVE_FINAL_COMP_TRAITS = ["Bastion", "Multicaster", "Noxus", "Rogue", "Strategist"]

RECOMMENDED_LEGEND = "Poro"

COMP = {
    "Nilah": {
        "board_position": 15,
        "items_to_build": ["Bloodthirster", "RapidFirecannon", "TitansResolve"],
        "completed_items_to_accept": ["Bloodthirster", "Deathblade", "GiantSlayer", "RapidFirecannon",
                                      "SteraksGage", "TitansResolve"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Miss Fortune": {
        "board_position": 3,
        "items_to_build": ["JeweledGauntlet", "BlueBuff", "HextechGunblade"],
        "completed_items_to_accept": ["HextechGunblade"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Gangplank": {
        "board_position": 6,
        "items_to_build": ["SpearofShojin"],
        "completed_items_to_accept": ["Guardbreaker", "SpearofShojin"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Nautilus": {
        "board_position": 24,
        "items_to_build": ["Redemption", "DragonsClaw", "BrambleVest"],
        "completed_items_to_accept": ["GargoyleStoneplate", "IonicSpark", "SunfireCape"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Darius": {
        "board_position": 23,
        "items_to_build": [],
        "completed_items_to_accept": ["IonicSpark"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["BastionEmblem", "BilgewaterEmblem", "RogueEmblem", "VanquisherEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Twisted Fate": {
        "board_position": 0,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["VanquisherEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Graves": {
        "board_position": 25,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["JuggernautEmblem", "VanquisherEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Illaoi": {
        "board_position": 22,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["JuggernautEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Kassadin": {
        "board_position": 21,
        "items_to_build": ["Bloodthirster", "TitansResolve"],
        "completed_items_to_accept": [],
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
