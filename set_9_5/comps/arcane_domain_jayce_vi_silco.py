"""
Title: Arcane Domain - S Tier
Comp: https://app.mobalytics.gg/tft/comps-guide/piltovers-pride-2VG56xmI0csHVkF4qX6Uo0443fa
Set: 9.5
Strategy: Slow Roll: This comp rolls gold above 50 to look for 3-star champions.
Difficulty: Medium
Legend: Urf
"""

NAME = "Arcane Domain"

STRATEGY = "Slow Roll"

DIFFICULTY = "Easy"

# In the order from most active to least active.
ACTIVE_FINAL_COMP_TRAITS = ["Zaun", "Gunner", "Piltover", "Reaver King"]

# just alphabetical order
INACTIVE_FINAL_COMP_TRAITS = ["Bilgewater", "Bruiser", "Challenger", "Juggernaut", "Rogue", "Sorcerer", "Targon"]

RECOMMENDED_LEGEND = "Urf"

COMP = {
    "Jayce": {
        "board_position": 1,
        "best_in_slot": ["LastWhisper", "InfinityEdge", "GuinsoosRageblade"],
        "secondary_items": ["GiantSlayer", "NashorsTooth", "RunaansHurricane"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Vi": {
        "board_position": 24,
        "best_in_slot": ["DragonsClaw", "BrambleVest", "WarmogsArmor"],
        "secondary_items": ["GargoyleStoneplate", "SunfireCape", "Evenshroud"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["JuggernautEmblem", "ZaunEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Silco": {
        "board_position": 4,
        "best_in_slot": ["BlueBuff", "JeweledGauntlet"],
        "secondary_items": ["SpearofShojin", "GiantSlayer", "Morellonomicon"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": ["AdaptiveImplant", "VirulentBioware"],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Gangplank": {
        "board_position": 0,
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["ZaunEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Aphelios": {
        "board_position": 2,
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["BilgewaterEmblem", "PiltoverEmblem", "ZaunEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Ekko": {
        "board_position": 26,
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["BilgewaterEmblem", "BruiserEmblem", "JuggernautEmblem", "NoxusEmblem",
                                  "ShurimaEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": ["HextechExoskeleton", "ShimmerInjector", "UnstableChemtech", "VirulentBioware"],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Jinx": {
        "board_position": 6,
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["PiltoverEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": ["AdaptiveImplant", "RoboticArm", "ShimmerInjector"],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Warwick": {
        "board_position": 22,
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["GunnerEmblem", "RogueEmblem", "BilgewaterEmblem", "PiltoverEmblem", "BruiserEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": ["AdaptiveImplant", "HextechExoskeleton", "RoboticArm", "ShimmerInjector", "UnstableChemtech"],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Taric": {
        "board_position": 23,
        "best_in_slot": ["DragonsClaw", "BrambleVest", "WarmogsArmor"],
        "secondary_items": ["GargoyleStoneplate", "SunfireCape", "Evenshroud"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Qiyana": {
        "board_position": 27,
        "best_in_slot": ["DragonsClaw", "BrambleVest", "WarmogsArmor"],
        "secondary_items": ["GargoyleStoneplate", "SunfireCape", "Evenshroud"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Renekton": {
        "board_position": 25,
        "best_in_slot": ["DragonsClaw", "BrambleVest", "WarmogsArmor"],
        "secondary_items": ["GargoyleStoneplate", "SunfireCape", "Evenshroud"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Graves": {
        "board_position": 7,
        "best_in_slot": ["InfinityEdge", "LastWhisper"],
        "secondary_items": ["GiantSlayer", "NashorsTooth", "RunaansHurricane"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Orianna": {
        "board_position": 3,
        "best_in_slot": ["BlueBuff"],
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
# Picks these augments 100% of the time.
PRIMARY_AUGMENTS: list[str] = [
    "Branching Out",
    "Consistency",
    "Cybernetic Bulk I",

    "Ancient Archives I",
    "Dueling Gunners",
    "Shimmering Inventors",

    "Ancient Archives II",
    "Cybernetic Bulk III",
    "Piltover Soul"
]

# Picks these augments when there are no primary augments to pick from after re-rolling augments in neither list.
SECONDARY_AUGMENTS: list[str] = [
    "Battle Ready I",
    "Money!",
    "Pandora's Items I",
    "Tiny Power I",
    "Unified Resistance I",

    "Balanced Budget II",
    "Battle Ready II",
    "Gunner Crest",
    "Last Stand",
    "Money Money!",
    "Pandora's Items II",
    "Patient Study",
    "Perfected Repetition",
    "Piltover Heart",
    "Pumping Up II",
    "Tiny Power II",
    "Unified Resistance II",
    "You Have My Bow",
    "Zaun Crest",

    "Battle Ready III",
    "Gunner Crown",
    "Lucky Gloves",
    "Money Money Money!",
    "Pandora's Items III",
    "Radiant Relics",
    "Tiny Power III",
    "Unified Resistance III",
    "Zaun Crown"
]