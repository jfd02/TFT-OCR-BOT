"""
Items are in camel case and a-Z
"""

COMP = {
    "Azir": {
        "board_position": 6,
        "items": ["GuinsoosRageblade", "HextechGunblade", "StatikkShiv", "RapidFirecannon", "Guardbreaker",
                  "GiantSlayer"],
        "level": 3,
        "final_comp": True
    },
    "Nasus": {
        "board_position": 24,
        "items": ["Redemption", "DragonsClaw", "BrambleVest", "GargoyleStoneplate", "WarmogsArmor"],
        "level": 3,
        "final_comp": True
    },
    "Jarvan IV": {
        "board_position": 26,
        "items": ["ProtectorsVow"],
        "level": 2,
        "final_comp": True
    },
    "KSante": {
        "board_position": 9,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "Taliyah": {
        "board_position": 9,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "Teemo": {
        "board_position": 3,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "Swain": {
        "board_position": 22,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "Garen": {
        "board_position": 23,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "Lux": {
        "board_position": 0,
        "items": ["BlueBuff", "JeweledGauntlet"],
        "level": 2,
        "final_comp": True
    },
    "Renekton": {
        "board_position": 16,
        "items": ["BrambleVest", "DragonsClaw"],
        "level": 2,
        "final_comp": False
    },
    "Vi": {
        "board_position": 14,
        "items": ["BrambleVest", "DragonsClaw"],
        "level": 2,
        "final_comp": False
    },
    "Cassiopeia": {
        "board_position": 7,
        "items": ["GuinsoosRageblade", "HextechGunblade", "JeweledGauntlet"],
        "level": 2,
        "final_comp": False
    },
    "Sona": {
        "board_position": 8,
        "items": [],
        "level": 2,
        "final_comp": False
    },
    "Orianna": {
        "board_position": 12,
        "items": ["StatikkShiv", "BlueBuff"],
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
    "Money!",
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
    "Patient Study",
    "Pumping Up II",
    "Salvage Bin",
    "Salvage Bin+",
    "Scrappy Inventions",
    "Shurima Crest",
    "Shurima's Legacy",
    "Social Distancing II",
    "Sorcerer Crest",
    "Strategist Heart",
    "Tactical Superiority",
    "Tiny Power II",
    "Tons of Stats!",
    "Unified Resistance II",
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
    "Giant Grab Bag",
    "Gifts From Above",
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
    "Multicaster Soul",
    "Parting Gifts",
    "Phreaky Friday",
    "Phreaky Friday+",
    "Pumping Up III",
    "Rolling for Days III",
    "Roll The Dice",
    "Shopping Spree",
    "Shurima Crown",
    "Social Distancing III",
    "Spoils of War III",
    "Strategist Soul",
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