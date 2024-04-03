"""
Team composition used by the bot
Comps come from https://tftactics.gg/tierlist/team-comps
Items are in camel case and a-Z
Items will be placed on the top champion first, and prioritize building items on the left.
"""

COMP = {
    "Tristana": {
        "board_position": 6,
        "items": ["GuinsoosRageblade", "InfinityEdge", "LastWhisper"],
        "level": 3,
        "final_comp": True
    },
    "Volibear": {
        "board_position": 27,
        "items": ["Bloodthirster", "TitansResolve", "WarmogsArmor"],
        "level": 3,
        "final_comp": True
    },
    "Irelia": {
        "board_position": 0,
        "items": ["GiantSlayer", "GuinsoosRageblade", "InfinityEdge"],
        "level": 2,
        "final_comp": True
    },
    "Wukong": {
        "board_position": 22,
        "items": ["HandofJustice"],
        "level": 2,
        "final_comp": True
    },
    "LeeSin": {
        "board_position": 25,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "Diana": {
        "board_position": 26,
        "items": ["BrambleVest", "DragonsClaw", "WarmogsArmor"],
        "level": 2,
        "final_comp": True
    },
    "Qiyana": {
        "board_position": 24,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "Darius": {
        "board_position": 23,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "Yorick": {
        "board_position": 20,
        "items": [],
        "level": 2,
        "final_comp": False
    },
    "Yasuo": {
        "board_position": 19,
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
    "Tiny but Deadly",
    "Pumping up",
    "Extended Duel",
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
    "Forge",
    "Crest Test Dummies"
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
