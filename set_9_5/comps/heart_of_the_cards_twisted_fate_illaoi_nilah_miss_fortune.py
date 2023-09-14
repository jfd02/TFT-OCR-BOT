"""
Title: Heart of the Cards - A Tier
Set: 9.5
Comp: https://app.mobalytics.gg/tft/comps-guide/heart-of-the-cards-2UiFaH0he2Q79A36gooRYd56OYY
Strategy: Slow Roll: This comp rolls gold above 50 to look for 3-star champions.
Difficulty: Easy
Legend: Lee Sin
Items are in camel case and a-Z
"""

NAME = "Heart of the Cards"

STRATEGY = "Slow Roll"

DIFFICULTY = "Easy"

TRAITS = ["Bilgewater", "Bastion", "Multicaster"]

RECOMMENDED_LEGEND = "Lee Sin"

COMP = {
    "Twisted Fate": {
        "board_position": 1,
        "items_to_build": ["BlueBuff", "HextechGunblade", "JeweledGauntlet"],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "radiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "final_comp": True
    },
    "Illaoi": {
        "board_position": 23,
        "items_to_build": ["DragonsClaw", "Redemption", "WarmogsArmor"],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "radiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "final_comp": True
    },
    "Nilah": {
        "board_position": 16,
        "items_to_build": ["TitansResolve", "Bloodthirster"],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "radiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": True
    },
    "Miss Fortune": {
        "board_position": 3,
        "items_to_build": ["Guardbreaker", "SpearofShojin"],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "radiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "final_comp": True
    },
    "Nautilus": {
        "board_position": 24,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "radiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": True
    },
    "Poppy": {
        "board_position": 25,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "radiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "final_comp": True
    },
    "Sona": {
        "board_position": 0,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "radiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": True
    },
    "Taliyah": {
        "board_position": 2,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "radiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": False
    },
    "Swain": {
        "board_position": 22,
        "items_to_build": ["Redemption", "WarmogsArmor"],
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
# Picks these augments 100% of the time.
PRIMARY_AUGMENTS: list[str] = [
    "AFK",
    "Money!",
    "On a Roll",

    "Money Money!",
    "Perfected Repetition",
    "Strategist Heart",

    "Golden Ticket",
    "Money Money Money!",
    "Strategist Soul"
]

# Picks these augments when there are no primary augments to pick from after re-rolling augments in neither list.
SECONDARY_AUGMENTS: list[str] = [
    "Battle Ready I",
    "Pandora's Items I",
    "Tiny Power I",
    "Unified Resistance I",

    "Ascension",
    "Balanced Budget II",
    "Battle Ready II",
    "Last Stand",
    "Pandora's Items II",
    "Patient Study",
    "Pumping Up II",
    "Tiny Power II",
    "Unified Resistance II",
    "You Have My Bow",

    "Battle Ready III",
    "Final Ascension",
    "Impenetrable Bulwark",
    "Lucky Gloves",
    "Pandora's Items III",
    "Tiny Power III",
    "Unified Resistance III",
]