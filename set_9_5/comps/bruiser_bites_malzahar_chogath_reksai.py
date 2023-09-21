"""
Super Nash Bros - S Tier - Meta Comp
Comp from https://app.mobalytics.gg/tft/comps-guide/super-nash-bros-2UiEdDoF20ICXwQnw5Kd3nwkeIP
Set: 9.5
Strategy: Default: This comp uses the standard leveling strategy that revolves around a 4-cost carry.
Difficulty: Medium
Legend: Urf
"""

NAME = "Super Nash Bros"

STRATEGY = "Default"

DIFFICULTY = "Medium"

# In the order from most active to least active.
ACTIVE_FINAL_COMP_TRAITS = ["Void", "Empress", "Bruiser", "Challenger", "Sorcerer"]

# just alphabetical order
INACTIVE_FINAL_COMP_TRAITS = ["Bastion", "Demacia", "Multicaster", "Slayer"]

RECOMMENDED_LEGEND = "Urf"

COMP = {
    "KaiSa": {
        "board_position": 4,
        "best_in_slot": ["Guardbreaker", "JeweledGauntlet", "SpearofShojin"],
        "secondary_items": ["GuinsoosRageblade", "GiantSlayer", "StatikkShiv"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "BelVeth": {
        "board_position": 18,
        "best_in_slot": ["Bloodthirster", "TitansResolve"],
        "secondary_items": ["HandofJustice", "LastWhisper", "Quicksilver", "SteraksGage"],
        "support_items_to_accept": ["VirtueoftheMartyr", "ZzRotPortal"],
        "trait_items_to_accept": ["ChallengerEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "ChoGath": {
        "board_position": 25,
        "best_in_slot": ["IonicSpark", "Redemption", "SunfireCape"],
        "secondary_items": ["Evenshroud", "GargoyleStoneplate"],
        "support_items_to_accept": ["AegisoftheLegion", "LocketoftheIronSolari"],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Fiora": {
        "board_position": 27,
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": ["ObsidianCleaver", "VirtueoftheMartyr"],
        "trait_items_to_accept": ["VoidEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "RekSai": {
        "board_position": 20,
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": ["ObsidianCleaver", "VirtueoftheMartyr"],
        "trait_items_to_accept": ["ChallengerEmblem", "FreljordEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "VelKoz": {
        "board_position": 6,
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": ["Zephyr"],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Kassadin": {
        "board_position": 23,
        "best_in_slot": [],
        "secondary_items": ["Morellonomicon"],
        "support_items_to_accept": ["VirtueoftheMartyr"],
        "trait_items_to_accept": ["BastionEmblem", "BruiserEmblem", "FreljordEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Malzahar": {
        "board_position": 0,
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": ["RabadonsDeathcap", "Zephyr"],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Ahri": {
        "board_position": 6,
        "best_in_slot": [],
        "secondary_items": [],
        "support_items_to_accept": ["Zephyr"],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Orianna": {
        "board_position": 1,
        "best_in_slot": ["SpearofShojin"],
        "secondary_items": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["VoidEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Renekton": {
        "board_position": 24,
        "best_in_slot": [],
        "secondary_items": ["Bloodthirster", "HandofJustice", "HextechGunblade", "TitansResolve"],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Vi": {
        "board_position": 21,
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
    "Challenger Heart",
    "Branching Out",
    "Tiny Grab Bag"

    "Ancient Archives I",
    "Void Heart",
    "Social Distancing II",
    "Stable Evolution",

    "Ancient Archives II",
    "Challenger Crown",
    "Ixtal Soul",
    "Void Soul",
]
SECONDARY_AUGMENTS: list[str] = [
    "Balanced Budget I",
    "Battle Ready I",
    "Blood Money",
    "Buried Treasures I",
    "Cutting Corners",
    "Gotta Go Fast!!! I",
    "It Pays to Learn I",
    "Jeweled Lotus I",
    "Knowledge Download I",
    "Money!",
    "On a Roll",
    "Pandora's Items",
    "Partial Ascension",
    "Rolling for Days I",
    "Silver Spoon",
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
    "Caretaker's Favor",
    "Dedication",
    "Early Education",
    "Escort Quest",
    "Gotta Go Fast!!! II",
    "Infusion",
    "It Pays to Learn II",
    "Jeweled Lotus II",
    "Knowledge Download II",
    "Last Stand",
    "Metabolic Accelerator",
    "Money Money!",
    "Pandora's Items II",
    "Patient Study",
    "Rolling for Days II",
    "Shoplifting",
    "Tiny Power II",
    "Tons of Stats!",
    "Unified Resistance II",
    "What Doesn't Kill You",

    "Ancient Archives II",
    "Balanced Budget III",
    "Bastion Crown",
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
    "It Pays to Learn III",
    "Jeweled Lotus III",
    "Knowledge Download III",
    "Level Up!",
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

