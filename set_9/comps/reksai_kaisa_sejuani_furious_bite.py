"""
Items are in camel case and a-Z
Comp from https://app.mobalytics.gg/tft/comps-guide/icy-rogues-2UqelNVz4mmfhfiE11Tew1uHtju
Strategy: Slow Roll: This comp rolls gold above 50 to look for 3-star champions.
Difficulty: Easy
"""

COMP = {
    "Reksai": {
        "board_position": 21,
        "items": ["Bloodthirster", "TitansResolve", "TitansResolve"],
        "level": 3,
        "final_comp": True
    },
    "Kaisa": {
        "board_position": 3,
        "items": ["ArchangelsStaff", "GuinsoosRageblade"],
        "level": 3,
        "final_comp": True
    },
    "Sejuani": {
        "board_position": 26,
        "items": ["GargoyleStoneplate", "WarmogsArmor"],
        "level": 2,
        "final_comp": True
    },
    "Lissandra": {
        "board_position": 14,
        "items": ["SpearofShojin"],  # BruiserEmblem
        "level": 2,
        "final_comp": True
    },
    "Sion": {
        "board_position": 22,
        "items": ["ZekesHerald"],
        "level": 2,
        "final_comp": True
    },
    "ChoGath": {
        "board_position": 23,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "Vi": {
        "board_position": 24,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "Ashe": {
        "board_position": 0,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "Renekton": {
        "board_position": 27,
        "items": ["WarmogsArmor", "GargoyleStoneplate"],
        "level": 2,
        "final_comp": False
    },
    "Malzahar": {
        "board_position": 1,
        "items": ["ArchangelsStaff"],
        "level": 2,
        "final_comp": False
    },
    "Velkoz": {
        "board_position": 6,
        "items": [],
        "level": 2,
        "final_comp": False
    },
    "Kalista": {
        "board_position": 4,
        "items": ["GuinsoosRageblade"],
        "level": 2,
        "final_comp": False
    },
    "Yasuo": {
        "board_position": 18,
        "items": ["Bloodthirster", "TitansResolve"],
        "level": 2,
        "final_comp": False
    },
}

# No logic for certain augments meaning the bot won't know what to do if they are included in here
# (Anything that changes gameplay or adds something to the bench).
AUGMENTS: list[str] = [
    "Battle Ready I",
    "Bronze Ticket",
    "Bruiser Heart",
    "Cybernetic Bulk I",
    "Cybernetic Leech I",
    "Gotta Go Fast!!! I",
    "Healing Orbs I",
    "Jeweled Lotus I",
    "Money!",
    "Pandora's Items",
    "Partial Ascension",
    "Pumping Up I",
    "Red Buff",
    "Tiny Titans",
    "Unified Resistance I",

    "Ascension",
    "Balanced Budget II",
    "Battle Ready II",
    "Big Grab Bag",
    "Bruiser Crest",
    "Buried Treasures II",
    "Caretaker's Favor",
    "Cybernetic Bulk II",
    "Cybernetic Leech II",
    "Early Education",
    "Endurance Training",
    "Final Grab Bag II",
    "Gifts from the Fallen",
    "Gotta Go Fast!!! II",
    "Healing Orbs II",
    "Infusion",
    "Item Grab Bag II",
    "It Pays to Learn II",
    "Jeweled Lotus",
    "Knowledge Download II",
    "Know Your Enemy",
    "Last Stand",
    "Magic Wand"
    "Martyr",
    "Money Money!",
    "Pandora's Items II",
    "Patient Study",
    "Pumping Up II",
    "Salvage Bin",
    "Salvage Bin+",
    "Scrappy Inventions",
    "Tiny Power II",
    "Titanic Strength",
    "Tons of Stats!",
    "Unified Resistance II",
    "Vampiric Blades",
    "What Doesn't Kill You",
    "You Have My Bow",

    "Ancient Archives II",
    "Balanced Budget III",
    "Battle Ready III",
    "Blinding Speed",
    "Bruiser Crown",
    "Buried Treasures III",
    "Cybernetic Bulk III",
    "Cybernetic Leech III",
    "Final Ascension",
    "Final Reserves",
    "Freljord Soul",
    "Giant Grab Bag",
    "Gifts From Above",
    "Golden Ticket",
    "Gotta Go Fast!!! III",
    "Harmacist III",
    "Hedge Fund",
    "Hedge Fund+",
    "Hedge Fund++",
    "High End Sector",
    "Impenetrable Bulwak",
    "Item Grab Bag III",
    "It Pays to Learn III",
    "Jeweled Lotus III",
    "Knowledge Download III",
    "Large Forge",
    "Level Up!",
    "Living Forge",
    "Lucky Gloves",
    "Masterful Job",
    "Money Money Money!",
    "Pandora's Box",
    "Parting Gifts",
    "Phreaky Friday",
    "Phreaky Friday+",
    "Pumping Up III",
    "Rolling for Days III",
    "Roll The Dice",
    "Shopping Spree",
    "Spoils of War III",
    "Tactician's Tools",
    "Tiniest Titan",
    "Tiny Power III",
    "Transfusion III",
    "Unified Resistance III",
    "Unleashed Arcana",
    "Wandering Trainer"
    "Well-Earned Comforts III",
    "Wellness Trust",
]