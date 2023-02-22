"""
Team composition used by the bot
Comps come from https://tftactics.gg/tierlist/team-comps
Items are in camel case and a-Z
"""

COMP = {
    "Ashe": {
        "board_position": 0,
        "items": ["GuinsoosRageblade", "LastWhisper", "GiantSlayer"],
        "level": 3,
        "final_comp": True,
    },
    "Ezreal": {
        "board_position": 6,
        "items": ["BlueBuff", "GiantSlayer", "JeweledGauntlet"],
        "level": 3,
        "final_comp": True
    },
    "Gangplank": {
        "board_position": 15,
        "items": [],
        "level": 3,
        "final_comp": True,
    },
    "Malphite": {
        "board_position": 22,
        "items": ["ZzRotPortal"],
        "level": 3,
        "final_comp": True,
    },
    "Renekton": {
        "board_position": 24,
        "items": ["WarmogsArmor", "DragonsClaw", "Redemption"],
        "level": 3,
        "final_comp": True,
    },
    "LeeSin": {
        "board_position": 25,
        "items": [],
        "level": 3,
        "final_comp": True
    },
    "Yasuo": {
        "board_position": 26,
        "items": ["Bloodthirster", "TitansResolve"],
        "level": 3,
        "final_comp": True,
    },
    "Zed": {
        "board_position": 18,
        "items": ["EdgeofNight", "RunaansHurricane", "LastWhisper"],
        "level": 3,
        "final_comp": True,
    },
    "Mordekaiser": {
        "board_position": 19,
        "items": ["RabadonsDeathcap", "HextechGunblade", "Morellonomicon"],
        "level": 3,
        "final_comp": True,
    }
}
"""
Team composition used by the bot
Comps come from https://tftactics.gg/tierlist/team-comps
Items are in camel case and a-Z
"""


# No logic for certain augments meaning the bot won't know what to do if they are included in here
# (Anything that changes gameplay or adds something to the bench).
AUGMENTS: list[str] = [
    "Featherweight",
    "Combat Training",
    "Tiny Legends",
    "Celestial Blessing",
    "Knife's Edge",
    "First Aid",
    "Shadow Jutsu",
    "Contempt for the Weak",
    "Laser Focus",
    "Corps Focus",
    "Siphoning Winds",
    "Spirit of the Exile",
    "Rising Spell Force",
    "Raider's Spoils",
    "Flaming Ricochet",
    "Get Paid",
    "Flurry",
    "Invigorate",
    "Reign of Anger",
    "Cull the Meek",
    "Rock Solid",
    "Guardian Spirit",
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
            raise ValueError("Comps.py | Champion level must be a valid level (1-3)")
    return champs_to_buy


def get_unknown_slots() -> list:
    """Creates a list of slots on the board that don't have a champion from the team composition"""
    container: list = [
        champion_data["board_position"] for _, champion_data in COMP.items()
    ]
    return [n for n in range(27) if n not in container]
