"""
Walk the Plank - S Tier
Comp from https://app.mobalytics.gg/tft/comps-guide/walk-the-plank-2UcDQkBTlGA2Y6MTIQOQXhAsWil
Strategy: Default: This comp uses the standard leveling strategy that revolves around a 4-cost carry.
Difficulty: Medium
Legend: Poro
Items are in camel case and a-Z
"""

STRATEGY = "Default"

DIFFICULTY = "Medium"

TRAITS = ["Bilgewater", "Reaver King", "Juggernaut", "Vanquisher", "Gunner"]

RECOMMENDED_LEGEND = "Poro"

COMP = {
    "Nilah": {
        "board_position": 15,
        "items": ["TitansResolve", "Bloodthirster", "RapidFirecannon"],
        "level": 3,
        "final_comp": True
    },
    "Miss Fortune": {
        "board_position": 3,
        "items": ["JeweledGauntlet", "BlueBuff", "HextechGunblade"],
        "level": 3,
        "final_comp": True
    },
    "Gangplank": {
        "board_position": 6,
        "items": ["SpearofShojin"],
        "level": 2,
        "final_comp": True
    },
    "Nautilus": {
        "board_position": 24,
        "items": ["Redemption", "DragonsClaw", "BrambleVest"],
        "level": 3,
        "final_comp": True
    },
    "Darius": {
        "board_position": 23,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "Twisted Fate": {
        "board_position": 0,
        "items": [],
        "level": 3,
        "final_comp": True
    },
    "Graves": {
        "board_position": 25,
        "items": [],
        "level": 3,
        "final_comp": True
    },
    "Illaoi": {
        "board_position": 22,
        "items": [],
        "level": 3,
        "final_comp": True
    },
    "Kassadin": {
        "board_position": 22,
        "items": ["Bloodthirster", "TitansResolve"],
        "level": 2,
        "final_comp": False
    }
}

# No logic for certain augments meaning the bot won't know what to do if they are included in here
# (Anything that changes gameplay or adds something to the bench).
AUGMENTS: list[str] = [
    "Battle Ready I",
    "Harmacist I",
    "Healing Orbs I"
    "Money!",
    "Pandora's Items I",
    "Tiny Power I",
    "Unified Resistance I",

    "Ascension",
    "Balanced Budget II",
    "Battle Ready II",
    "Bilgewater Crest",
    "Dedication",
    "Last Stand",
    "Magic Wand"
    "Money Money!",
    "Pandora's Items II",
    "Patient Study",
    "Pumping Up II",
    "Rising Infamy",
    "Tiny Power II",
    "Unified Resistance II",
    "You Have My Bow",

    "Battle Ready III",
    "Bilgewater Crown",
    "Final Ascension",
    "Impenetrable Bulwark",
    "Lucky Gloves",
    "Money Money Money!",
    "Pandora's Items III",
    "Stationary Support III",
    "Strategist Soul",
    "Tiny Power III",
    "Unified Resistance III",
]

"""
    "Bronze Ticket",
    "Cybernetic Bulk I",
    "Cybernetic Leech I",
    "Gotta Go Fast!!! I",
    "Healing Orbs I",
    "Pumping Up I",
    "Red Buff",
    "Social Distancing I",
    
    
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
    "Martyr",
    "Salvage Bin",
    "Salvage Bin+",
    "Scrappy Inventions",
    "Social Distancing II",
    "Sorcerer Crest",
    "Tons of Stats!",
    "What Doesn't Kill You",
    
    "Ancient Archives II",
    "Balanced Budget III",
    "Blinding Speed",
    "Buried Treasures III",
    "Cybernetic Bulk III",
    "Cybernetic Leech III",
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
    "Masterful Job",
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
    "Tactician's Tools",
    "Tiniest Titan",
    "Transfusion III",
    "Unleashed Arcana",
    "Wandering Trainer"
    "Well-Earned Comforts III",
    "Wellness Trust",
"""