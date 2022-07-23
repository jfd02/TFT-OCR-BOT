"""
Team composition used by the bot
Comps come from https://tftactics.gg/tierlist/team-comps
Items are in camel case and a-Z
"""

comp = {"Ezreal": {"board_position": 0,
                "items": [],
                "level": 2,
                "final_comp": True},

        "Twitch": {"board_position": 1,
                "items": ["InfinityEdge", "LastWhisper", "RunaansHurricane"],
                "level": 2,
                "final_comp": True},

        "Xayah": {"board_position": 5,
                "items": ["GiantSlayer", "GuinsoosRageblade", "Quicksilver"],
                "level": 2,
                "final_comp": True},

        "Varus": {"board_position": 6,
                   "items": ["Deathblade", "GuinsoosRageblade", "RunaansHurricane"],
                   "level": 3,
                   "final_comp": True},
        "Ornn": {"board_position": 23,
                    "items": ["GiantSlayer", "GuinsoosRageblade", "InfinityEdge"],
                    "level": 3,
                    "final_comp": True},
        "Shen": {"board_position": 24,
                  "items": [],
                  "level": 3,
                  "final_comp": True},
        "Illaoi": {"board_position": 25,
                "items": ["GargoyleStoneplate", "SunfireCape", "WarmogsArmor"],
                "level": 3,
                "final_comp": True},
        "Skarner": {"board_position": 26,
                "items": [],
                "level": 3,
                "final_comp": True},
}

# No logic for certain augments meaning the bot won't know what to do if they are included in here (Anything that changes gameplay or adds something to the bench).
augments = ["Cybernetic Implants", "Stand United", "Electrocharge", "Cybernetic Uplink", "Celestial Blessing",
            "Cybernetic Shell", "Weakspot", "Tri Force", "Gadget Expert", "Metabolic Accelerator", "Second Wind",
             "Luden's Echo", "Last Stand", "Ascension", "Tiny Titans", "Sunfire Board", "Wise Spending", "Component Grab Bag+",
             "Featherweights", "Thrill of the Hunt", "Preparation", "Blue Battery", "Hustler", "Windfall++", "Verdant Veil",
             "First Aid Kit", "Rich Get Richer+", "Combat Training", "Meditation", "Axiom Arc"]

def champions_to_buy() -> list:
    champs_to_buy = []
    for champion in comp:
        if comp[champion]["level"] == 1:
            champs_to_buy.append(champion)
        elif comp[champion]["level"] == 2:
            for _ in range(3):
                champs_to_buy.append(champion)
        elif comp[champion]["level"] == 3:
            for _ in range(9):
                champs_to_buy.append(champion)
    return champs_to_buy

def get_unknown_slots():
    container = []
    for champion in comp:
        container.append(comp[champion]["board_position"])
    return [n for n in range(27) if n not in container]
