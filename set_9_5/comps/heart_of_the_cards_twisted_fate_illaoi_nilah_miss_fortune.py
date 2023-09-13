"""
Heart of the Cards - A Tier
Comp from https://app.mobalytics.gg/tft/comps-guide/heart-of-the-cards-2UiFaH0he2Q79A36gooRYd56OYY
Strategy: Slow Roll: This comp rolls gold above 50 to look for 3-star champions.
Difficulty: Easy
Legend: Lee Sin
Items are in camel case and a-Z
"""

STRATEGY = "Slow Roll"

DIFFICULTY = "Easy"

TRAITS = ["Bilgewater", "Bastion", "Multicaster"]

RECOMMENDED_LEGEND = "Lee Sin"

COMP = {
    "Twisted Fate": {
        "board_position": 1,
        "items_to_build": ["BlueBuff", "HextechGunblade", "JeweledGauntlet"],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "raidiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "final_comp": True
    },
    "Illaoi": {
        "board_position": 23,
        "items_to_build": ["DragonsClaw", "Redemption", "WarmogsArmor"],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "raidiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "final_comp": True
    },
    "Nilah": {
        "board_position": 16,
        "items_to_build": ["TitansResolve", "Bloodthirster"],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "raidiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": True
    },
    "Miss Fortune": {
        "board_position": 3,
        "items_to_build": ["Guardbreaker", "SpearofShojin"],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "raidiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "final_comp": True
    },
    "Nautilus": {
        "board_position": 24,
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
    "Poppy": {
        "board_position": 25,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "raidiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 3,
        "final_comp": True
    },
    "Sona": {
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
    "Taliyah": {
        "board_position": 2,
        "items_to_build": [],
        "completed_items_to_accept": [],
        "support_items_to_accept": [],
        "trait_items_to_accept": [],
        "ornn_items_to_accept": [],
        "raidiant_items_to_accept": [],
        "zaun_items_to_accept": [],
        "level": 2,
        "final_comp": False
    },
    "Swain": {
        "board_position": 22,
        "items_to_build": ["Redemption", "WarmogsArmor"],
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
    "AFK",
    "Battle Ready I",
    "Money!",
    "On a Roll",
    "Pandora's Items I",
    "Tiny Power I",
    "Unified Resistance I",

    "Ascension",
    "Balanced Budget II",
    "Battle Ready II",
    "Last Stand",
    "Money Money!",
    "Pandora's Items II",
    "Patient Study",
    "Perfected Repetition",
    "Pumping Up II",
    "Tiny Power II",
    "Unified Resistance II",
    "You Have My Bow",

    "Battle Ready III",
    "Final Ascension",
    "Golden Ticket",
    "Impenetrable Bulwark",
    "Lucky Gloves",
    "Money Money Money!",
    "Pandora's Items III",
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