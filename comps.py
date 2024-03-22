"""
Team composition used by the bot
Comps come from https://tftactics.gg/tierlist/team-comps
Items are in camel case and a-Z
The "headliner" tag represents a trait from bottom to top.
Set to True if you want it in your team.
Only final comp champion will become headliner and need to set the corresponding 'headliner' tag to True.
e.g. Only want "Sentinel" Ekko, set it to "headliner": [True, False, False]
e.g.2 want either "Sentinel" or "True Damage" Ekko, set it to "headliner": [True, False, True]
"""

COMP = {
    "Galio": {
        "board_position": 25,
        "items": ["BrambleVest", "DragonsClaw", "WarmogsArmor"],
        "level": 2,
        "final_comp": True
    },
    "Kaisa": {
        "board_position": 5,
        "items": ["InfinityEdge", "LastWhisper", "SpearofShojin"],
        "level": 3,
        "final_comp": True
    },
    "Sivir": {
        "board_position": 4,
        "items": ["SpearofShojin", "StatikkShiv"],
        "level": 2,
        "final_comp": True
    },
    "Aatrox": {
        "board_position": 27,
        "items": ["Evenshroud"],
        "level": 2,
        "final_comp": True
    },
    "Riven": {
        "board_position": 21,
        "items": ["ThiefsGloves"],
        "level": 2,
        "final_comp": True
    },
    "Teemo": {
        "board_position": 0,
        "items": ["BlueBuff", "RabadonsDeathcap"],
        "level": 2,
        "final_comp": True
    },
    "Sylas": {
        "board_position": 23,
        "items": ["ThiefsGloves"],
        "level": 2,
        "final_comp": True
    },
    "Xayah": {
        "board_position": 6,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "Kobuko": {
        "board_position": 24,
        "items": [],
        "level": 2,
        "final_comp": False
    },
    "Zoe": {
        "board_position": 3,
        "items": [],
        "level": 2,
        "final_comp": False
    }
}

# No logic for certain augments meaning the bot won't know what to do if they are included in here
# (Anything that changes gameplay or adds something to the bench).
# The ones on the top will be prioritized for selection.
# For those augments names with suffixes like I, II, III, such as 'Cybernetic Uplink II',
# You only need to add 'Cybernetic Uplink' in the list to cover all three levels.
AUGMENTS: list[str] = [
    "That's Jazz Baby!",
    "You Have My Bow",
    "Blistering Strikes",
    "Buried Treasures",
    "Switching Gears",
    "Caretaker's Favor",
    "Gotta Go Fast",
    "Tiny Power",
    "Shurima's Legacy",
    "Featherweights",
    "Reconnaissance Team",
    "Electrocharge",
    "Quickdraw Soul",
    "InfiniTeam",
    "Big Friend",
    "First Aid Kit",
    "Stand United",
    "Grab Bag",
    "Component Grab Bag",
    "Thrill of the Hunt",
    "Better Together",
    "Cybernetic Uplink",
    "Cybernetic Implants",
    "Celestial Blessing",
    "Cybernetic Shell",
    "Weakspot",
    "Tri Force",
    "Gadget Expert",
    "Metabolic Accelerator",
    "Second Wind",
    "Luden's Echo",
    "Last Stand",
    "Ascension",
    "Tiny Titans",
    "Sunfire Board",
    "Wise Spending",
    "Component Grab Bag+",
    "Preparation",
    "Blue Battery",
    "Hustler",
    "Windfall++",
    "Verdant Veil",
    "Rich Get Richer+",
    "Combat Training",
    "Meditation",
    "Axiom Arc",
]

AVOID_AUGMENTS: list[str] = [
    "Stationary Support",
    "Escort Quest",
    "Mind Over Matter",
    "Scapegoat",
    "Wandering Trainer",
    "Recombobulator",
    "Forge"
]


def champions_to_buy() -> dict:
    """Creates a list of champions to buy during the game"""
    champs_to_buy: dict = {}
    for champion, champion_data in COMP.items():
        if champion_data["level"] == 1:
            champs_to_buy[champion] = 1
        elif champion_data["level"] == 2:
            champs_to_buy[champion] = 3
        elif champion_data["level"] == 3:
            champs_to_buy[champion] = 9
        else:
            raise ValueError("Comps.py | Champion level must be a valid level (1-3)")
    return champs_to_buy


def get_unknown_slots() -> list:
    """Creates a list of slots on the board that don't have a champion from the team composition"""
    container: list = []
    for _, champion_data in COMP.items():
        container.append(champion_data["board_position"])
    return [n for n in range(27) if n not in container]
