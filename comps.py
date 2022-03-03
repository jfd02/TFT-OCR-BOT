# Comps come from https://tftactics.gg/tierlist/team-comps
# Challengers Academy
# Items are in camel case and a-Z


comp = {"Ezreal": {"board_position": 4,
                "items": [],
                "level": 2,
                "final_comp": True},

        "Singed": {"board_position": 24,
                "items": [],
                "level": 2,
                "final_comp": False},

        "Ekko": {"board_position": 3,
                "items": [],
                "level": 2,
                "final_comp": True},

        "Talon": {"board_position": 2,
                "items": [],
                "level": 2,
                "final_comp": False},

        "Leona": {"board_position": 22,
                "items": [],
                "level": 2,
                "final_comp": False},

        "Zilean": {"board_position": 12,
                "items": [],
                "level": 2,
                "final_comp": True},

        "Senna": {"board_position": 6,
                "items": ["GiantSlayer", "InfinityEdge", "LastWhisper"],
                "level": 2,
                "final_comp": True},

        "Orianna": {"board_position": 13,
                "items": [],
                "level": 2,
                "final_comp": True},

        "Vi": {"board_position": 25,
                "items": ["BrambleVest", "DragonsClaw", "WarmogsArmor"],
                "level": 2,
                "final_comp": True},

        "Seraphine": {"board_position": 5,
                "items": [],
                "level": 2,
                "final_comp": True},

        "Jayce": {"board_position": 26,
                "items": [],
                "level": 2,
                "final_comp": True},
        }

# This tries to get a trait in the priority trait (priority is from left to right) before looking in backup traits
# No logic for traits like Phony Frontline meaning the bot won't know what to do if they are included in here.
priority_augments = ["Thrill of the Hunt", "Celestial Blessing", "Makeshift Armor", "Cybernetic Implants",
                     "Knife's Edge", "Sunfire Board", "Featherweights", "Woodland Charm", "High End Shopping",
                     "Level Up!", "Wise Spending", "Windfall", "Titanic Force", "Rich Get Richer", "Weakspot",
                     "Underdogs", "Ascension", "Dominance", "First Aid Kit"]

backup_augments = {"Dominance", "Hyper Roll", "Ascension", "Built Different", "Celestial Blessing", "Knife's Edge",
                   "Cybernetic Implants", "Exiles", "Featherweights", "First Aid Kit", "Makeshift Armor",
                   "Stand United", "Thrill of the Hunt", "Underdogs", "Weakspot", "Academy Heart", "Arcanist Heart",
                   "Runic Shield", "Assassin Heart", "Cutthroat", "Bodyguard Heart", "Stand Behind Me", "Bruiser Heart",
                   "Challenger Heart", "En Garde", "Chemical Overload", "Chemtech Heart", "Clockwork Heart",
                   "Enchanter Heart", "Ardent Censer", "Enforcer Heart", "Imperial Heart", "Dual Rule",
                   "Innovator Heart", "Self-Repair", "Mercenary Heart", "Pirates", "Mutant Heart", "Unstable Evolution",
                   "Protector Heart", "Scholar Heart", "Lifelong Learning", "Scrap Heart", "Sniper's Nest",
                   "Sniper Heart", "Duet", "Socialite Heart", "Syndicate Heart", "One For All", "Payday",
                   "Twinshot Heart", "So Small", "Rich Get Richer", "Binary Airdrop", "Clear Mind", "Sunfire Board",
                   "Metabolic Accelerator", "Titanic Force", "Cram Session", "Spell Blade", "Smoke Bomb", "Safety Vest",
                   "Shrug It Off", "Instant Injection", "Armor Plating", "All For One", "Gold Reserves", "Deadeye",
                   "Shady Business", "Sharpshooter", "Share the Spotlight", "Windfall", "Wise Spending", "Level Up!",
                   "High End Shopping", "Woodland Charm", "Academy Soul", "Arcanist Soul", "Assassin Soul",
                   "Bodyguard Soul", "Bruiser Soul", "Challenger Soul", "Chemtech Soul", "Clockwork Soul",
                   "Broken Stopwatch", "Enchanter Soul", "Enforcer Soul", "Imperial Soul", "Innovator Soul",
                   "Mercenary Soul", "Mutant Soul", "Protector Soul", "Scholar Soul", "Scrap Soul", "Sniper Soul",
                   "Socialite Soul", "Syndicate Soul", "Twinshot Soul"}


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
