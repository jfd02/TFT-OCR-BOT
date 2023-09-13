"""
Title: Arcane Domain - S Tier
Set: 9.5
Comp: https://app.mobalytics.gg/tft/comps-guide/piltovers-pride-2VG56xmI0csHVkF4qX6Uo0443fa
Strategy: Slow Roll: This comp rolls gold above 50 to look for 3-star champions.
Difficulty: Medium
Legend: Urf
Items are in camel case and a-Z
"""

STRATEGY = "Slow Roll"

DIFFICULTY = "Easy"

TRAITS = ["Zaun", "Gunner", "Piltover", "Reaver King"]

RECOMMENDED_LEGEND = "Urf"

COMP = {
    "Jayce": {
        "board_position": 1,
        "items_to_build": ["LastWhisper", "InfinityEdge", "GuinsoosRageblade"],
        "completed_items_to_accept": ["GiantSlayer", "NashorsTooth", "RunaansHurricane"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "radiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "final_comp": True
    },
    "Vi": {
        "board_position": 24,
        "items_to_build": ["DragonsClaw", "BrambleVest", "WarmogsArmor"],
        "completed_items_to_accept": ["GargoyleStoneplate", "SunfireCape", "Evenshroud"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["JuggernautEmblem"],
        "ornn_items_to_accept": [],
        "radiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "final_comp": True
    },
    "Silco": {
        "board_position": 4,
        "items_to_build": ["BlueBuff", "JeweledGauntlet"],
        "completed_items_to_accept": ["SpearofShojin", "GiantSlayer", "Morellonomicon"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "radiant_items_to_accept": [],
        "zaun_items_to_accept": ["AdaptiveImplant", "VirulentBioware"],
        "level": 3,
        "final_comp": True
    },
    "Gangplank": {
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
    "Aphelios": {
        "board_position": 2,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["BilgewaterEmblem", "PiltoverEmblem"],
        "ornn_items_to_accept": [],
        "radiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": True
    },
    "Ekko": {
        "board_position": 26,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["JuggernautEmblem", "BilgewaterEmblem", "BruiserEmblem"],
        "ornn_items_to_accept": [],
        "radiant_items_to_accept": [],
        "zaun_items_to_accept": ["HextechExoskeleton", "ShimmerInjector", "UnstableChemtech", "VirulentBioware"],
        "level": 2,
        "final_comp": True
    },
    "Jinx": {
        "board_position": 6,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["PiltoverEmblem"],
        "ornn_items_to_accept": [],
        "radiant_items_to_accept": [],
        "zaun_items_to_accept": ["AdaptiveImplant", "RoboticArm", "ShimmerInjector"],
        "level": 2,
        "final_comp": True
    },
    "Warwick": {
        "board_position": 22,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["GunnerEmblem", "RogueEmblem", "BilgewaterEmblem", "PiltoverEmblem", "BruiserEmblem"],
        "ornn_items_to_accept": [],
        "radiant_items_to_accept": [],
        "zaun_items_to_accept": ["AdaptiveImplant", "HextechExoskeleton", "RoboticArm", "ShimmerInjector", "UnstableChemtech"],
        "level": 2,
        "final_comp": True
    },
    "Graves": {
        "board_position": 7,
        "items_to_build": ["InfinityEdge", "LastWhisper"],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "radiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": False
    },
    "Orianna": {
        "board_position": 3,
        "items_to_build": ["BlueBuff"],
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
    "Gunner Crest",
    "Last Stand",
    "Money Money!",
    "Pandora's Items II",
    "Patient Study",
    "Perfected Repetition",
    "Piltover Heart",
    "Pumping Up II",
    "Shimmering Inventors",
    "Tiny Power II",
    "Unified Resistance II",
    "You Have My Bow",
    "Zaun Crest",

    "Ancient Archives II",
    "Battle Ready III",
    "Cybernetic Bulk III",
    "Gunner Crown",
    "Lucky Gloves",
    "Money Money Money!",
    "Pandora's Items III",
    "Piltover Soul",
    "Radiant Relics",
    "Tiny Power III",
    "Unified Resistance III",
    "Zaun Crown"
]
