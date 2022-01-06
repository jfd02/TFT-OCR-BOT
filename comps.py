# Comps come from https://tftactics.gg/tierlist/team-comps
# Challengers Academy
# Items are in camel case and a-Z


comp = {"Lux": {"board_position": 0,
                "items": ["BlueBuff", "InfinityEdge", "JeweledGauntlet", "SpearofShojin", "GuinsoosRageblade"],
                "level": 2,
                "final_comp": True},

        "Ziggs": {"board_position": 6,
                  "items": ["BlueBuff", "SpearofShojin", "JeweledGauntlet", "ArchangelsStaff", "StatikkShiv"],
                  "level": 2,
                  "final_comp": False},

        "Katarina": {"board_position": 7,
                     "items": ["HandofJustice", "InfinityEdge", "IonicSpark"],
                     "level": 2,
                     "final_comp": True},

        "Twisted Fate": {"board_position": 13,
                         "items": [],
                         "level": 2,
                         "final_comp": False},

        "Graves": {"board_position": 22,
                   "items": ["GiantSlayer", "GuinsoosRageblade", "HandofJustice", "InfinityEdge"],
                   "level": 2,
                   "final_comp": True},

        "Blitzcrank": {"board_position": 19,
                       "items": [],
                       "level": 2,
                       "final_comp": False},

        "Yuumi": {"board_position": 20,
                  "items": ["ArchangelsStaff", "BlueBuff", "Morellonomicon"],
                  "level": 2,
                  "final_comp": True},

        "Fiora": {"board_position": 23,
                  "items": ["InfinityEdge", "GuardianAngel", "JeweledGauntlet"],
                  "level": 2,
                  "final_comp": True},

        "Leona": {"board_position": 24,
                  "items": ["BrambleVest", "DragonsClaw", "WarmogsArmor", "SunfireCape"],
                  "level": 2,
                  "final_comp": True},

        "Garen": {"board_position": 25,
                  "items": ["Bloodthirster", "TitansResolve", "WarmogsArmor"],
                  "level": 2,
                  "final_comp": False},

        "Braum": {"board_position": 26,
                  "items": [],
                  "level": 2,
                  "final_comp": True},

        "Yone": {"board_position": 27,
                 "items": ["GuardianAngel", "LastWhisper", "RunaansHurricane"],
                 "level": 2,
                 "final_comp": True}}

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
