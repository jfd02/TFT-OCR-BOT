"""
Team composition used by the bot
Comps come from https://tftactics.gg/tierlist/team-comps
Items are in camel case and a-Z
"""

COMP = {
    "Ezreal": {
        "board_position": 0,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "Twitch": {
        "board_position": 1,
        "items": ["InfinityEdge", "LastWhisper", "RunaansHurricane"],
        "level": 2,
        "final_comp": True,
    },
    "Xayah": {
        "board_position": 5,
        "items": ["GiantSlayer", "GuinsoosRageblade", "Quicksilver"],
        "level": 2,
        "final_comp": True,
    },
    "Varus": {
        "board_position": 6,
        "items": ["Deathblade", "GuinsoosRageblade", "RunaansHurricane"],
        "level": 3,
        "final_comp": True,
    },
    "Ornn": {
        "board_position": 23,
        "items": ["GiantSlayer", "GuinsoosRageblade", "InfinityEdge"],
        "level": 3,
        "final_comp": True,
    },
    "Shen": {
        "board_position": 24,
        "items": [],
        "level": 3,
        "final_comp": True
    },
    "Illaoi": {
        "board_position": 25,
        "items": ["GargoyleStoneplate", "SunfireCape", "WarmogsArmor"],
        "level": 3,
        "final_comp": True,
    },
    "Skarner": {"board_position": 26, "items": [], "level": 3, "final_comp": True},
}

# No logic for certain augments meaning the bot won't know what to do if they are included in here
# (Anything that changes gameplay or adds something to the bench).
AUGMENTS: list[str] = [
    "Cybernetic Implants",
    "Stand United",
    "Electrocharge",
    "Cybernetic Uplink",
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
    "Featherweights",
    "Thrill of the Hunt",
    "Preparation",
    "Blue Battery",
    "Hustler",
    "Windfall++",
    "Verdant Veil",
    "First Aid Kit",
    "Rich Get Richer+",
    "Combat Training",
    "Meditation",
    "Axiom Arc",
]


def champions_to_buy() -> list:
    """Creates a list of champions to buy during the game"""
    champs_to_buy: list = []
    for champion, champion_data in COMP.items():
        if champion_data["level"] == 1:
            champs_to_buy.append(champion)
        elif champion_data["level"] == 2:
            champs_to_buy.extend([champion] * 3)
        elif champion_data["level"] == 3:
            champs_to_buy.extend([champion] * 9)
        else:
            raise Exception("Comps.py | Champion level must be a valid level (1-3)")
    return champs_to_buy


def get_unknown_slots() -> list:
    """Creates a list of slots on the board that don't have a champion from the team composition"""
    container: list = []
    for _, champion_data in COMP.items():
        container.append(champion_data["board_position"])
    return [n for n in range(27) if n not in container]
