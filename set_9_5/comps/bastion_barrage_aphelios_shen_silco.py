"""
Bastion Barrage - A Tier - Meta Comp
Comp from https://app.mobalytics.gg/tft/comps-guide/bastion-barrage-2VFVBh0WEe8SVFe78rMEMX1klCS
Set: 9.5
Strategy: Default: This comp uses the standard leveling strategy that revolves around a 4-cost carry.
Difficulty: Medium
Legend: Ezreal
"""

NAME = "Bastion Barrage"

STRATEGY = "Default"

DIFFICULTY = "Medium"

# In the order from most active to least active.
ACTIVE_FINAL_COMP_TRAITS = ["Targon", "Bastion", "Sorcerer", "Invoker", "Zaun", "Gunner"]

# just alphabetical order
INACTIVE_FINAL_COMP_TRAITS = ["Ionia", "Ixtal", "Shurima"]

RECOMMENDED_LEGEND = "Ezreal"

COMP = {
    "Aphelios": {
        "board_position": 6,
        "items_to_build": ["Deathblade", "GuinsoosRageblade", "GuinsoosRageblade"],
        "completed_items_to_accept": ["Deathblade", "GuinsoosRageblade", "InfinityEdge"],
        "support_items_to_accept": ["VirtueoftheMartyr", "ZzRotPortal"],
        "trait_items_to_accept": ["ZaunEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "max_amount_of_items": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Silco": {
        "board_position": 4,
        "items_to_build": ["ArchangelsStaff", "BlueBuff", "Morellonomicon"],
        "completed_items_to_accept": ["ArchangelsStaff", "BlueBuff", "JeweledGauntlet",
                                      "HextechGunblade", "Morellonomicon"],
        "support_items_to_accept": ["ObsidianCleaver", "ZekesHerald"],
        "trait_items_to_accept": ["InvokerEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": ["AdaptiveImplant", "VirulentBioware"],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Shen": {
        "board_position": 26,
        "items_to_build": ["Evenshroud", "Redemption", "WarmogsArmor",],
        "completed_items_to_accept": ["BrambleVest", "Crownguard", "Evenshroud", "GargoyleStoneplate",
                                      "IonicSpark", "Redemption", "SunfireCape", "WarmogsArmor"],
        "support_items_to_accept": ["ZzRotPortal"],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "KSante": {
        "board_position": 24,
        "items_to_build": ["ProtectorsVow"],
        "completed_items_to_accept": [],
        "support_items_to_accept": ["LocketoftheIronSolari", "VirtueoftheMartyr"],
        "trait_items_to_accept": ["GunnerEmblem", "IoniaEmblem", "InvokerEmblem", "IxtalEmblem", "TargonEmblem", "ZaunEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Taric": {
        "board_position": 25,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": ["AegisoftheLegion", "BansheesVeil", "Crest of Cinders", "LocketoftheIronSolari",
                                    "ShroudofStillness", "VirtueoftheMartyr", "ZzRotPortal"],
        "trait_items_to_accept": ["ChallengerEmblem", "IoniaEmblem", "IxtalEmblem", "GunnerEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Neeko": {
        "board_position": 22,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": ["ObsidianCleaver", "ShroudofStillness", "Zephyr"],
        "trait_items_to_accept": ["GunnerEmblem", "InvokerEmblem", "IoniaEmblem", "SorcererEmblem", "TargonEmblem", "ZaunEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Jinx": {
        "board_position": 2,
        "items_to_build": [],
        "completed_items_to_accept": ["Morellonomicon"],
        "support_items_to_accept": ["VirtueoftheMartyr"],
        "trait_items_to_accept": ["IoniaEmblem", "IxtalEmblem", "SorcererEmblem", "TargonEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": ["AdaptiveImplant", "RoboticArm", "ShimmerInjector"],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Soraka": {
        "board_position": 0,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": ["NeedlesslyBigGem", "Zephyr"],
        "trait_items_to_accept": ["BastionEmblem", "IoniaEmblem", "IxtalEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Galio": {
        "board_position": 23,
        "items_to_build": [],
        "completed_items_to_accept": ["LocketoftheIronSolari"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["BastionEmblem", "IoniaEmblem", "IxtalEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": True
    },
    "Illaoi": {
        "board_position": 21,
        "items_to_build": ["Evenshroud", "WarmogsArmor"],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["InvokerEmblem", "IxtalEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Kayle": {
        "board_position": 1,
        "items_to_build": ["GuinsoosRageblade", "GuinsoosRageblade"],
        "completed_items_to_accept": ["Bloodthirster", "HandofJustice", "TitansResolve"],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["IoniaEmblem", "IxtalEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Poppy": {
        "board_position": 16,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["InvokerEmblem", "IxtalEmblem"],
        "ornn_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "max_amount_of_items": 3,
        "final_comp": False
    },
    "Kassadin": {
        "board_position": 27,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": ["InvokerEmblem", "IxtalEmblem"],
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
    "Bastion Heart",
    "Buried Treasures I",
    "Red Buff",

    "Buried Treasures II",
    "Targon Heart",
    "Morning Light",

    "Bastion Crown",
    "Buried Treasures III",
    "Targon Soul",
]
SECONDARY_AUGMENTS: list[str] = [
    "Balanced Budget I",
    "Battle Ready I",
    "Blood Money",
    "Buried Treasures I",
    "Gotta Go Fast!!! I",
    "It Pays to Learn I",
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

