"""
Arcane Domain - S Tier
Comp from https://app.mobalytics.gg/tft/comps-guide/piltovers-pride-2VG56xmI0csHVkF4qX6Uo0443fa
Strategy: Slow Roll: This comp rolls gold above 50 to look for 3-star champions.
Difficulty: Medium
Legend: Urf
Items are in camel case and a-Z
"""

STRATEGY = "Slow Roll"

DIFFICULTY = "Easy"

TRAITS = ["Zaun", "Gunner", "Piltover", "Reaver King"]

RECOMMENDED_LEGEND = "Lee Sin"

COMP = {
    "Jayce": {
        "board_position": 1,
        "items": ["LastWhisper", "InfinityEdge", "GuinsoosRageblade"],
        "level": 3,
        "final_comp": True
    },
    "Vi": {
        "board_position": 24,
        "items": ["DragonsClaw", "BrambleVest", "WarmogsArmor"],
        "level": 3,
        "final_comp": True
    },
    "Silco": {
        "board_position": 4,
        "items": ["BlueBuff", "JeweledGauntlet"],
        "level": 3,
        "final_comp": True
    },
    "Gangplank": {
        "board_position": 0,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "Aphelios": {
        "board_position": 2,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "Ekko": {
        "board_position": 26,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "Jinx": {
        "board_position": 6,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "Warwick": {
        "board_position": 22,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "Graves": {
        "board_position": 7,
        "items": ["InfinityEdge", "LastWhisper"],
        "level": 2,
        "final_comp": False
    },
    "Orianna": {
        "board_position": 3,
        "items": ["BlueBuff"],
        "level": 2,
        "final_comp": False
    }
}

# No logic for certain augments meaning the bot won't know what to do if they are included in here
# (Anything that changes gameplay or adds something to the bench).
AUGMENTS: list[str] = [
    "Battle Ready I",
    "Branching Out",
    "Consistency",
    "Cybernetic Bulk I",
    "Money!",
    "Pandora's Items I",
    "Tiny Power I",
    "Unified Resistance I",

    "Ancient Archives I",
    "Balanced Budget II",
    "Battle Ready II",
    "Dueling Gunners",
    "Last Stand",
    "Money Money!",
    "Pandora's Items II",
    "Patient Study",
    "Perfected Repetition",
    "Pumping Up II",
    "Shimmering Inventors",
    "Tiny Power II",
    "Unified Resistance II",
    "You Have My Bow",

    "Ancient Archives II",
    "Battle Ready III",
    "Cybernetic Bulk III",
    "Lucky Gloves",
    "Money Money Money!",
    "Pandora's Items III",
    "Piltover Soul",
    "Tiny Power III",
    "Unified Resistance III",
]
