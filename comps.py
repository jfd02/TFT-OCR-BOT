# Comps come from https://tftactics.gg/tierlist/team-comps
# Challengers Academy
# Items are in camel case and a-Z

comp = {"Poppy": {"board_position": 23,
                "items": ["BrambleVest", "GargoyleStoneplate", "SunfireCape"],
                "level": 3,
                "final_comp": True},

        "Ziggs": {"board_position": 0,
                "items": [],
                "level": 2,
                "final_comp": True},

        "Blitzcrank": {"board_position": 24,
                "items": [],
                "level": 2,
                "final_comp": False},
                
        "Corki": {"board_position": 5,
                "items": ["BlueBuff", "InfinityEdge", "JeweledGauntlet"],
                "level": 3,
                "final_comp": True},

        "Lulu": {"board_position": 4,
                "items": ["ChaliceofPower", "ZekesHerald", "BlueBuff"],
                "level": 3,
                "final_comp": True},

        "Gnar": {"board_position": 12,
                "items": ["BrambleVest", "DragonsClaw", "WarmogsArmor"],
                "level": 3,
                "final_comp": True},

        "Lucian": {"board_position": 13,
                "items": [],
                "level": 2,
                "final_comp": True},

        "Vex": {"board_position": 25,
                "items": [],
                "level": 2,
                "final_comp": True},

        "Veigar": {"board_position": 6,
                "items": ["BlueBuff", "InfinityEdge", "JeweledGauntlet"],
                "level": 2,
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
