"""
Items are in camel case and a-Z
"""

COMP = {
    "Ekko": {
        "board_position": 22,
        "items": ["JeweledGauntlet", "HandofJustice", "HandofJustice"],
        "level": 3,
        "final_comp": True
    },
    "Katarina": {
        "board_position": 24,
        "items": ["ArchangelsStaff", "JeweledGauntlet", "HandofJustice"],
        "level": 3,
        "final_comp": True
    },
    "Lissandra": {
        "board_position": 23,
        "items": ["ChaliceofPower"],
        "level": 2,
        "final_comp": True
    },
    "Sejuani": {
        "board_position": 21,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "Urgot": {
        "board_position": 25,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "Sion": {
        "board_position": 26,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "Heimerdinger": {
        "board_position": 0,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "Ashe": {
        "board_position": 6,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "Viego": {
        "board_position": 22,
        "items": ["JeweledGauntlet", "HandofJustice", "HandofJustice"],
        "level": 2,
        "final_comp": False
    },
    "Maokai": {
        "board_position": 23,
        "items": [],
        "level": 2,
        "final_comp": False
    },
    "Zed": {
        "board_position": 24,
        "items": [],
        "level": 2,
        "final_comp": False
    },
    "Poppy": {
        "board_position": 25,
        "items": [],
        "level": 2,
        "final_comp": False
    },
    "Vi": {
        "board_position": 25,
        "items": [],
        "level": 2,
        "final_comp": False
    },
    "Orianna": {
        "board_position": 2,
        "items": ["JeweledGauntlet"],
        "level": 2,
        "final_comp": False
    }
}

# No logic for certain augments meaning the bot won't know what to do if they are included in here
# (Anything that changes gameplay or adds something to the bench).
AUGMENTS: list[str] = [
    "Battle Ready I",
    "Bronze Ticket",
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
    "Social Distancing I",
    "Tiny Titans",
    "Unified Resistance I",

    "Ascension",
    "Balanced Budget II",
    "Battle Ready II",
    "Big Grab Bag",
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
    "Idealism",
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
    "Social Distancing II",
    "Sorcerer Crest",
    "Tactical Superiority",
    "Tiny Power II",
    "Tons of Stats!",
    "Unified Resistance II",
    "Vampiric Blades",
    "What Doesn't Kill You",
    "You Have My Bow",

    "Ancient Archives II",
    "Balanced Budget III",
    "Battle Ready III",
    "Blinding Speed",
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
    "Social Distancing III",
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