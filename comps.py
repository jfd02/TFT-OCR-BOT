"""
Team composition used by the bot
Comps come from https://tftactics.gg/tierlist/team-comps
Items are in camel case and a-Z
"""

comp = {"Sejuani": {"board_position": 23,
                "items": [],
                "level": 1,
                "final_comp": True},

        "Shen": {"board_position": 24,
                "items": [],
                "level": 2,
                "final_comp": True},

        "Twitch": {"board_position": 1,
                "items": [],
                "level": 2,
                "final_comp": True},

        "Hecarim": {"board_position": 22,
                   "items": ["BrambleVest", "DragonsClaw", "WarmogsArmor"],
                   "level": 4,
                   "final_comp": True},
        "Xayah": {"board_position": 0,
                    "items": ["GiantSlayer", "GuinsoosRageblade", "InfinityEdge"],
                    "level": 4,
                    "final_comp": True},
        "Bard": {"board_position": 3,
                  "items": [],
                  "level": 5,
                  "final_comp": True},
}

# This tries to get a trait in the priority trait (priority is from left to right) before looking in backup traits
# No logic for traits like Phony Frontline meaning the bot won't know what to do if they are included in here.
priority_augments = ["Celestial Blessing", "Backfoot", "Cybernetic Implants", "Cybernetic Shell", "Cybernetic Uplink", 
                     "Disintegrator", "Thrill of the Hunt", "Electrocharge", "Knife's Edge", "Featherweights", "Makeshift Armor",
                     "Underdogs", "Second Wind", "Tri Force", "Weakspot", "Rich Get Richer",
                     "Woodland Charm", "Metabolic Accelerator", "Wise Spending", "Woodland Trinket", "Sunfire Board"]

backup_augments = {"Arcane Nullifier", "Ascension", "Backfoot", "Battlemage", "Blue Battery",
                   "Celestial Blessing", "Cybernetic Implants", "Cybernetic Shell", "Cybernetic Uplink", "Disintegrator", "Dominance",
                   "Electrocharge", "Exiles", "Featherweights", "First Aid Kit", "Item Grab Bag", "Keepers",
                   "Knife's Edge", "Luden's Echo", "Makeshift Armor", "Meditation", "Phalanx", "Second Wind",
                   "Stand United", "Thrill of the Hunt", "Tri Force", "Underdogs", "Weakspot",
                   "Binary Airdrop", "Component Grab Bag", "Metabolic Accelerator", "Rich Get Richer", "Salvage Bin",
                   "Sunfire Board", "Titanic Force", "Woodland Trinket", "Wise Spending", "Ardent Censer", "High End Shopping"}

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
