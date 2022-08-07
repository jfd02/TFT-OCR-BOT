"""
Contains static item & champion data
"""

COMBINED_ITEMS = {"BFSword", "ChainVest", "GiantsBelt", "NeedlesslyLargeRod",
                  "NegatronCloak", "SparringGloves", "Spatula", "TearoftheGoddess",
                  "ArchangelsStaff", "AssassinEmblem", "BansheesClaw", "Bloodthirster",
                  "BlueBuff", "BrambleVest", "CavalierEmblem", "ChaliceofPower",
                  "Deathblade", "DragonmancerEmblem", "DragonsClaw", "EdgeofNight",
                  "FrozenHeart", "GargoyleStoneplate", "GiantSlayer", "HandofJustice",
                  "HextechGunblade", "InfinityEdge", "IonicSpark", "JewledGauntlet",
                  "LastWhisper", "LocketoftheIronSolari", "MageEmblem", "MirageEmblem",
                  "Morellonomicon", "Quicksilver", "RabadonsDeathcap", "Ragewing Emblem",
                  "RapidFirecannon", "Redemption", "RunaansHurricane", "ShimmerscaleEmblem",
                  "ShroudofStillness", "SpearofShojin", "StatikkShiv", "SunfireCape",
                  "TacticiansCrown", "ThiefsGloves", "TitansResolve", "WarmogsArmor",
                  "ZekesHerald", "Zephyr", "ZZRotPortal", "RecurveBow",
                  "GuardianEmblem", "GuinsoosRageblade"}

ELUSIVE_ITEMS = {"AstralEmblem", "BruiserEmblem", "Cannoneer Emblem",
                 "DragonmancersBlessing", "EvokerEmblem", "GuildEmblem",
                 "JadeEmblem", "LegendEmblem", "MysticEmblem",
                 "RevelEmblem", "ScalescornEmblem", "SwiftshotEmblem",
                 "TempestEmblem", "WarriorEmblem", "WhispersEmblem"}

SHIMMERSCALE_ITEMS = {"CrownOfChampions", "DeterminedInvestor", "DiamondHands",
                      "DravensAxe", "GamblersBlade", "GoldmancersStaff",
                      "MogulsMail", "NeedlesslyBigGem", "PhilosophersStone"}

ORNN_ITEMS = {"AnimaVisage", "DeathsDefiance", "EternalWinter",
              "GoldCollector", "InfinityForce",
              "Manazane", "ObsidianCleaver", "RaduinsSanctum",
              "RocketPropelledFist", "ZhonyasParadox"}

RADIANT_ITEMS = {"Absolution", "BansheesSilence", "BlessedBloodthirster",
                 "BlueBlessing", "BrinkofDawn", "ChaliceofCharity",
                 "CovalentSpark", "DemonSlayer", "DragonsWill",
                 "DvarapalaStoneplate", "EternalWhisper", "FistofFairness",
                 "FrozenHeartOfGold", "GlamorousGauntlet", "GuinsoosReckoning",
                 "HextechLifeblade", "LocketofTargonPrime", "LuminousDeathblade",
                 "Mistral", "MoreMoreellonomicon", "Quickestsilver",
                 "RabadonsAscendedDeathcap", "RadiantRedemption", "RapidLightcannon",
                 "RascalsGloves", "RosethornVest", "RunaansTempest",
                 "ShroudofReverance", "SpearofHirana", "StatikkFavor",
                 "SunlightCape", "TitansVow", "UrfAngelsStaff",
                 "WarmogsPride", "ZekesHarmony", "ZenithEdge",
                 "ZzRotsInvitation"}

ITEMS = COMBINED_ITEMS.union(ELUSIVE_ITEMS).union(
    SHIMMERSCALE_ITEMS).union(ORNN_ITEMS).union(RADIANT_ITEMS)

CHAMPIONS = {
    "Aatrox": {"Gold": 1, "Board Size": 1},
    "Anivia": {"Gold": 3, "Board Size": 1},
    "Ao Shin": {"Gold": 10, "Board Size": 2},
    "Ashe": {"Gold": 2, "Board Size": 1},
    "Aurelion Sol": {"Gold": 10, "Board Size": 2},
    "Bard": {"Gold": 5, "Board Size": 1},
    "Braum": {"Gold": 2, "Board Size": 1},
    "Corki": {"Gold": 4, "Board Size": 1},
    "Daeja": {"Gold": 8, "Board Size": 2},
    "Diana": {"Gold": 3, "Board Size": 1},
    "Elise": {"Gold": 3, "Board Size": 1},
    "Ezreal": {"Gold": 1, "Board Size": 1},
    "Gnar": {"Gold": 2, "Board Size": 1},
    "Hecarim": {"Gold": 4, "Board Size": 1},
    "Heimerdinger": {"Gold": 1, "Board Size": 1},
    "Idas": {"Gold": 8, "Board Size": 2},
    "Illaoi": {"Gold": 3, "Board Size": 1},
    "Jinx": {"Gold": 2, "Board Size": 1},
    "Karma": {"Gold": 1, "Board Size": 1},
    "Kayn": {"Gold": 2, "Board Size": 1},
    "Lee sin": {"Gold": 3, "Board Size": 1},
    "Leona": {"Gold": 1, "Board Size": 1},
    "Lillia": {"Gold": 2, "Board Size": 1},
    "Lulu": {"Gold": 3, "Board Size": 1},
    "Nami": {"Gold": 2, "Board Size": 1},
    "Neeko": {"Gold": 4, "Board Size": 1},
    "Nidalee": {"Gold": 1, "Board Size": 1},
    "Nunu": {"Gold": 3, "Board Size": 1},
    "Olaf": {"Gold": 3, "Board Size": 1},
    "Ornn": {"Gold": 4, "Board Size": 1},
    "Pyke": {"Gold": 5, "Board Size": 1},
    "Qiyana": {"Gold": 2, "Board Size": 1},
    "Ryze": {"Gold": 3, "Board Size": 1},
    "Sejuani": {"Gold": 1, "Board Size": 1},
    "Senna": {"Gold": 1, "Board Size": 1},
    "Sett": {"Gold": 1, "Board Size": 1},
    "Shen": {"Gold": 2, "Board Size": 1},
    "Shi Oh Yu": {"Gold": 8, "Board Size": 2},
    "Shyvana": {"Gold": 10, "Board Size": 2},
    "Skarner": {"Gold": 1, "Board Size": 1},
    "Sona": {"Gold": 4, "Board Size": 1},
    "Soraka": {"Gold": 5, "Board Size": 1},
    "Swain": {"Gold": 3, "Board Size": 1},
    "Syfen": {"Gold": 8, "Board Size": 2},
    "Sylas": {"Gold": 3, "Board Size": 1},
    "Tahm Kench": {"Gold": 1, "Board Size": 1},
    "Talon": {"Gold": 4, "Board Size": 1},
    "Taric": {"Gold": 1, "Board Size": 1},
    "Thresh": {"Gold": 2, "Board Size": 1},
    "Tristana": {"Gold": 2, "Board Size": 1},
    "Twitch": {"Gold": 2, "Board Size": 1},
    "Varus": {"Gold": 3, "Board Size": 1},
    "Vladmir": {"Gold": 1, "Board Size": 1},
    "Volibear": {"Gold": 3, "Board Size": 1},
    "Xayah": {"Gold": 4, "Board Size": 1},
    "Yasuo": {"Gold": 5, "Board Size": 1},
    "Yone": {"Gold": 2, "Board Size": 1},
    "Zoe": {"Gold": 5, "Board Size": 1}}

ROUNDS = {"1-1", "1-2", "1-3", "1-4",
          "2-1", "2-2", "2-3", "2-4", "2-5", "2-6", "2-7",
          "3-1", "3-2", "3-3", "3-4", "3-5", "3-6", "3-7",
          "4-1", "4-2", "4-3", "4-4", "4-5", "4-6", "4-7",
          "5-1", "5-2", "5-3", "5-4", "5-5", "5-6", "5-7",
          "6-1", "6-2", "6-3", "6-4", "6-5", "6-6", "6-7",
          "7-1", "7-2", "7-3", "7-4", "7-5", "7-6", "7-7"}

CAROUSEL_ROUND = {"1-1", "2-4", "3-4", "4-4", "5-4", "6-4", "7-4"}

PVE_ROUND = {"1-2", "1-3", "1-4", "2-7", "3-7", "4-7", "5-7", "6-7", "7-7"}

PVP_ROUND = {"2-1", "2-2", "2-3", "2-5", "2-6",
             "3-1", "3-2", "3-3", "3-5", "3-6",
             "4-1", "4-2", "4-3", "4-5", "4-6",
             "5-1", "5-2", "5-3", "5-5", "5-6",
             "6-1", "6-2", "6-3", "6-5", "6-6",
             "7-1", "7-2", "7-3", "7-5", "7-6"}

PICKUP_ROUNDS = {"2-1", "3-1", "4-1", "5-1", "6-1", "7-1"}

AUGMENT_ROUNDS = {"2-1", "3-2", "4-2"}

ITEM_PLACEMENT_ROUNDS = {"2-2", "3-2", "4-2", "5-2",
                         "6-2", "7-2", "2-5", "3-5", "4-5", "5-5", "6-5", "7-5"}

FINAL_COMP_ROUND = "4-5"

FULL_ITEMS = {"ArchangelsStaff": ("NeedlesslyLargeRod", "TearoftheGoddess"),
              "AssassinEmblem": ("SparringGloves", "Spatula"),
              "BansheesClaw": ("GiantsBelt", "SparringGloves"),
              "Bloodthirster": ("BFSword", "NegatronCloak"),
              "BlueBuff": ("TearoftheGoddess", "TearoftheGoddess"),
              "BrambleVest": ("ChainVest", "ChainVest"),
              "CavalierEmblem": ("ChainVest", "Spatula"),
              "ChaliceofPower": ("NegatronCloak", "TearoftheGoddess"),
              "Deathblade": ("BFSword", "BFSword"),
              "DragonmancerEmblem": ("NeedlesslyLargeRod", "Spatula"),
              "DragonsClaw": ("NegatronCloak", "NegatronCloak"),
              "EdgeofNight": ("BFSword", "ChainVest"),
              "FrozenHeart": ("ChainVest", "TearoftheGoddess"),
              "GargoyleStoneplate": ("ChainVest", "NegatronCloak"),
              "GiantSlayer": ("BFSword", "RecurveBow"),
              "GuardianEmblem": ("GiantsBelt", "Spatula"),
              "GuinsoosRageblade": ("NeedlesslyLargeRod", "RecurveBow"),
              "HandofJustice": ("SparringGloves", "TearoftheGoddess"),
              "HextechGunblade": ("BFSword", "NeedlesslyLargeRod"),
              "InfinityEdge": ("BFSword", "SparringGloves"),
              "IonicSpark": ("NeedlesslyLargeRod", "NegatronCloak"),
              "JeweledGauntlet": ("NeedlesslyLargeRod", "SparringGloves"),
              "LastWhisper": ("RecurveBow", "SparringGloves"),
              "LocketoftheIronSolari": ("ChainVest", "NeedlesslyLargeRod"),
              "MageEmblem": ("TearoftheGoddess", "Spatula"),
              "MirageEmblem": ("NegatronCloak", "Spatula"),
              "Morellonomicon": ("GiantsBelt", "NeedlesslyLargeRod"),
              "Quicksilver": ("NegatronCloak", "SparringGloves"),
              "RabadonsDeathcap": ("NeedlesslyLargeRod", "NeedlesslyLargeRod"),
              "RagewingEmblem": ("RecurveBow", "Spatula"),
              "RapidFirecannon": ("RecurveBow", "RecurveBow"),
              "Redemption": ("GiantsBelt", "TearoftheGoddess"),
              "RunaansHurricane": ("NegatronCloak", "RecurveBow"),
              "ShimmerscaleEmblem": ("BFSword", "Spatula"),
              "ShroudofStillness": ("ChainVest", "SparringGloves"),
              "SpearofShojin": ("BFSword", "TearoftheGoddess"),
              "StatikkShiv": ("RecurveBow", "TearoftheGoddess"),
              "SunfireCape": ("ChainVest", "GiantsBelt"),
              "TacticiansCrown": ("Spatula", "Spatula"),
              "ThiefsGloves": ("SparringGloves", "SparringGloves"),
              "TitansResolve": ("ChainVest", "RecurveBow"),
              "WarmogsArmor": ("GiantsBelt", "GiantsBelt"),
              "ZekesHerald": ("BFSword", "GiantsBelt"),
              "Zephyr": ("GiantsBelt", "NegatronCloak"),
              "ZzRotPortal": ("GiantsBelt", "RecurveBow")
              }


def champion_board_size(champion: str) -> int:
    """Takes a string (champion name) and returns board size of champion"""
    return CHAMPIONS[champion]["Board Size"]


def champion_gold_cost(champion: str) -> int:
    """Takes a string (champion name) and returns gold of champion"""
    return CHAMPIONS[champion]["Gold"]
