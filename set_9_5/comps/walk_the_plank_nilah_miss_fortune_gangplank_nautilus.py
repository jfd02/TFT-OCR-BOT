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
        "best_in_slot": ["Bloodthirster", "RapidFirecannon", "TitansResolve"],
        "secondary_items": ["Deathblade", "GiantSlayer", "SteraksGage"],
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
        "best_in_slot": ["JeweledGauntlet", "BlueBuff", "HextechGunblade"],
        "secondary_items": [],
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
        "best_in_slot": ["SpearofShojin"],
        "secondary_items": ["Guardbreaker", "SpearofShojin"],
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
        "best_in_slot": ["Redemption", "DragonsClaw", "BrambleVest"],
        "secondary_items": ["GargoyleStoneplate", "IonicSpark", "SunfireCape"],
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
        "best_in_slot": [],
        "secondary_items": ["IonicSpark"],
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
        "best_in_slot": [],
        "secondary_items": [],
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
        "best_in_slot": [],
        "secondary_items": [],
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
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["JuggernautEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Swain": {
        "board_position": 21,
        "best_in_slot": ["Redemption", "DragonsClaw", "BrambleVest", "IonicSpark"],
        "secondary_items": ["GargoyleStoneplate", "SunfireCape"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Kassadin": {
        "board_position": 21,
        "best_in_slot": ["Bloodthirster", "TitansResolve"],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Warwick": {
        "board_position": 26,
        "best_in_slot": ["Bloodthirster", "TitansResolve"],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Sett": {
        "board_position": 19,
        "best_in_slot": [],
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

    "Ancient Archives I",
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
    "What Doesn't Kill You",
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
