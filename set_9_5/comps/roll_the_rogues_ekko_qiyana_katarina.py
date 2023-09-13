"""
Arcane Domain - S Tier
Comp from https://app.mobalytics.gg/tft/comps-guide/piltovers-pride-2VG56xmI0csHVkF4qX6Uo0443fa
Strategy: Slow Roll: This comp rolls gold above 50 to look for 3-star champions.
Difficulty: Easy
Legend: Twisted Fate
Don't level up at stage 2-1.
Items are in camel case and a-Z
"""

STRATEGY = "Slow Roll"

DIFFICULTY = "Easy"

TRAITS = ["Rogue", "Ixtal", "Zaun", "Bastion", "Sorcerer"]

RECOMMENDED_LEGEND = "Twisted Fate"

COMP = {
    "Qiyana": {
        "board_position": 26,
        "items_to_build": ["InfinityEdge", "SteraksGage", "HandofJustice"],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "raidiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "final_comp": True
    },
    "Ekko": {
        "board_position": 22,
        "items_to_build": ["HandofJustice", "JeweledGauntlet", "HandofJustice"],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "raidiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "final_comp": True
    },
    "Katarina": {
        "board_position": 24,
        "items_to_build": ["IonicSpark", "NightHarvester"],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "raidiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "final_comp": True
    },
    "Silco": {
        "board_position": 0,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "raidiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": True
    },
    "Taric": {
        "board_position": 23,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "raidiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": True
    },
    "Neeko": {
        "board_position": 25,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "raidiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": True
    },
    "Graves": {
        "board_position": 14,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "raidiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": True
    },
    "Milio": {
        "board_position": 6,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "raidiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": True
    },
    "Illaoi": {
        "board_position": 21,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "raidiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": False
    }
}

# No logic for certain augments meaning the bot won't know what to do if they are included in here
# (Anything that changes gameplay or adds something to the bench).
AUGMENTS: list[str] = [
    "Battle Ready I",
    "Consistency",
    "Cybernetic Leech I",
    "Money!",
    "Pandora's Items I",
    "Rogue Heart",
    "Tiny Power I",
    "Unified Resistance I",

    "Balanced Budget II",
    "Battle Ready II",
    "Idealism",
    "Last Stand",
    "Money Money!",
    "Pandora's Items II",
    "Patient Study",
    "Pumping Up II",
    "Tiny Power II",
    "Unified Resistance II"
    "Vampiric Blades",

    "Battle Ready III",
    "Golden Ticket",
    "Lucky Gloves",
    "Money Money Money!",
    "Pandora's Items III",
    "Rogue Crown",
    "Tiny Power III",
    "Unified Resistance III",
]
