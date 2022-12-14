"""
Contains static item & champion data
"""

COMBINED_ITEMS: set[str] = {"BFSword", "ChainVest", "GiantsBelt", "NeedlesslyLargeRod",
                            "NegatronCloak", "SparringGloves", "Spatula", "TearoftheGoddess",
                            "ArchangelsStaff", "RenegadeEmblem", "Guardbreaker", "Bloodthirster",
                            "BlueBuff", "BrambleVest", "MascotEmblem", "ChaliceofPower",
                            "Deathblade", "HeartEmblem", "DragonsClaw", "EdgeofNight",
                            "FrozenHeart", "GargoyleStoneplate", "GiantSlayer", "HandofJustice",
                            "HextechGunblade", "InfinityEdge", "IonicSpark", "JeweledGauntlet",
                            "LastWhisper", "LocketoftheIronSolari", "AnimaEmblem", "ADMINEmblem",
                            "Morellonomicon", "Quicksilver", "RabadonsDeathcap", "OxForceEmblem",
                            "RapidFirecannon", "Redemption", "RunaansHurricane", "DuelistEmblem",
                            "ShroudofStillness", "SpearofShojin", "StatikkShiv", "SunfireCape",
                            "TacticiansCrown", "ThiefsGloves", "TitansResolve", "WarmogsArmor",
                            "ZekesHerald", "Zephyr", "ZZRotPortal", "RecurveBow",
                            "LaserCorpsEmblem", "GuinsoosRageblade"}

ELUSIVE_ITEMS: set[str] = {"AceEmblem", "AegisEmblem", "BrawlerEmblem",
                           "PRIMESelector", "SpellslingerEmblem", "CivilianEmblem",
                           "ReconEmblem", "StarGuardianEmblem", "TheUndergroundEmblem",
                           "SureshotEmblem", "DefenderEmblem", "MechaPRIMEEmblem",
                           "GadgeteenEmblem", "HackerEmblem", "PranksterEmblem"}

GADGETEEN_ITEMS: set[str] = {"InductionPoweredWarmogsArmor", "JumpStartedSpearofShojin", "SpringLoadedRapidFirecannon",
                             "MagnetizedIonicSpark", "HandofNondeterministicJustice", "OVERFLOWERROR//GiantSlayer",
                             "ChainswordBloodthirster"}

ORNN_ITEMS: set[str] = {"AnimaVisage", "DeathsDefiance", "EternalWinter",
                        "GoldCollector", "InfinityForce",
                        "Manazane", "ObsidianCleaver", "RaduinsSanctum",
                        "RocketPropelledFist", "ZhonyasParadox"}

RADIANT_ITEMS: set[str] = {"Absolution", "BlessedBloodthirster",
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

ITEMS: set[str] = COMBINED_ITEMS.union(ELUSIVE_ITEMS).union(
    GADGETEEN_ITEMS).union(ORNN_ITEMS).union(RADIANT_ITEMS)

CHAMPIONS: dict[str, dict[str, int]] = {
    "Alistar": {"Gold": 3, "Board Size": 1},
    "Annie": {"Gold": 2, "Board Size": 1},
    "Aphelios": {"Gold": 5, "Board Size": 1},
    "Ashe": {"Gold": 1, "Board Size": 1},
    "AurelionSol": {"Gold": 4, "Board Size":1},
    "Belveth": {"Gold": 4, "Board Size": 1},
    "Blitzcrank": {"Gold": 1, "Board Size": 1},
    "Camille": {"Gold": 2, "Board Size": 1},
    "Chogath": {"Gold": 3, "Board Size": 1},
    "Draven": {"Gold": 2, "Board Size": 1},
    "Ekko": {"Gold": 4, "Board Size": 1},
    "Ezreal": {"Gold": 2, "Board Size": 1},
    "Fiddlesticks": {"Gold": 5, "Board Size": 1},
    "Fiora": {"Gold": 2, "Board Size": 1},
    "Galio": {"Gold": 1, "Board Size": 1},
    "Gangplank": {"Gold": 1, "Board Size": 1},
    "Janna": {"Gold": 5, "Board Size": 1},
    "Jax": {"Gold": 3, "Board Size": 1},
    "Jinx": {"Gold": 2, "Board Size": 1},
    "Kaisa": {"Gold": 3, "Board Size": 1},
    "Kayle": {"Gold": 1, "Board Size": 1},
    "Leblanc": {"Gold": 3, "Board Size": 1},
    "LeeSin": {"Gold": 2, "Board Size": 1},
    "Leona": {"Gold": 5, "Board Size": 1},
    "Lulu": {"Gold": 1, "Board Size": 1},
    "Lux": {"Gold": 1, "Board Size": 1},
    "Malphite": {"Gold": 2, "Board Size": 1},
    "MissFortune": {"Gold": 4, "Board Size": 1},
    "Mordekaiser": {"Gold": 5, "Board Size": 1},
    "Nasus": {"Gold": 1, "Board Size": 1},
    "Nilah": {"Gold": 3, "Board Size": 1},
    "Nunu": {"Gold": 5, "Board Size": 1},
    "Poppy": {"Gold": 1, "Board Size": 1},
    "Rammus": {"Gold": 3, "Board Size": 1},
    "Rell": {"Gold": 2, "Board Size": 1},
    "Renekton": {"Gold": 1, "Board Size": 1},
    "Riven": {"Gold": 3, "Board Size": 1},
    "Samira": {"Gold": 4, "Board Size": 1},
    "Sejuani": {"Gold": 4, "Board Size": 1},
    "Senna": {"Gold": 3, "Board Size": 1},
    "Sett": {"Gold": 4, "Board Size": 1},
    "Sivir": {"Gold": 2, "Board Size": 1},
    "Sona": {"Gold": 3, "Board Size": 1},
    "Soraka": {"Gold": 4, "Board Size": 1},
    "Sylas": {"Gold": 1, "Board Size": 1},
    "Syndra": {"Gold": 5, "Board Size": 1},
    "Taliyah": {"Gold": 4, "Board Size": 1},
    "Talon": {"Gold": 1, "Board Size": 1},
    "Urgot": {"Gold": 5, "Board Size": 1},
    "Vayne": {"Gold": 3, "Board Size": 1},
    "Velkoz": {"Gold": 3, "Board Size": 1},
    "Vi": {"Gold": 2, "Board Size": 1},
    "Viego": {"Gold": 4, "Board Size": 1},
    "Wukong": {"Gold": 1, "Board Size": 1},
    "Yasuo": {"Gold": 2, "Board Size": 1},
    "Yuumi": {"Gold": 2, "Board Size": 1},
    "Zac": {"Gold": 4, "Board Size": 1},
    "Zed": {"Gold": 4, "Board Size": 1},
    "Zoe": {"Gold": 3, "Board Size": 1}}

ROUNDS: set[str] = {"1-1", "1-2", "1-3", "1-4",
                    "2-1", "2-2", "2-3", "2-4", "2-5", "2-6", "2-7",
                    "3-1", "3-2", "3-3", "3-4", "3-5", "3-6", "3-7",
                    "4-1", "4-2", "4-3", "4-4", "4-5", "4-6", "4-7",
                    "5-1", "5-2", "5-3", "5-4", "5-5", "5-6", "5-7",
                    "6-1", "6-2", "6-3", "6-4", "6-5", "6-6", "6-7",
                    "7-1", "7-2", "7-3", "7-4", "7-5", "7-6", "7-7"}

CAROUSEL_ROUND: set[str] = {"1-1", "2-4", "3-4", "4-4", "5-4", "6-4", "7-4"}

PVE_ROUND: set[str] = {"1-2", "1-3", "1-4", "2-7", "3-7", "4-7", "5-7", "6-7", "7-7"}

PVP_ROUND: set[str] = {"2-1", "2-2", "2-3", "2-5", "2-6",
                       "3-1", "3-2", "3-3", "3-5", "3-6",
                       "4-1", "4-2", "4-3", "4-5", "4-6",
                       "5-1", "5-2", "5-3", "5-5", "5-6",
                       "6-1", "6-2", "6-3", "6-5", "6-6",
                       "7-1", "7-2", "7-3", "7-5", "7-6"}

PICKUP_ROUNDS: set[str] = {"2-1", "3-1", "4-1", "5-1", "6-1", "7-1"}

AUGMENT_ROUNDS: set[str] = {"2-1", "3-2", "4-2"}

ITEM_PLACEMENT_ROUNDS: set[str] = {"2-2", "3-2", "4-2", "5-2",
                                   "6-2", "7-2", "2-5", "3-5", "4-5", "5-5", "6-5", "7-5"}

FINAL_COMP_ROUND = "4-5"

FULL_ITEMS = {"ArchangelsStaff": ("NeedlesslyLargeRod", "TearoftheGoddess"),
              "RenegadeEmblem": ("SparringGloves", "Spatula"),
              "Guardbreaker": ("GiantsBelt", "SparringGloves"),
              "Bloodthirster": ("BFSword", "NegatronCloak"),
              "BlueBuff": ("TearoftheGoddess", "TearoftheGoddess"),
              "BrambleVest": ("ChainVest", "ChainVest"),
              "OxForceEmblem": ("ChainVest", "Spatula"),
              "ChaliceofPower": ("NegatronCloak", "TearoftheGoddess"),
              "Deathblade": ("BFSword", "BFSword"),
              "AnimaSquadEmblem": ("NeedlesslyLargeRod", "Spatula"),
              "DragonsClaw": ("NegatronCloak", "NegatronCloak"),
              "EdgeofNight": ("BFSword", "ChainVest"),
              "FrozenHeart": ("ChainVest", "TearoftheGoddess"),
              "GargoyleStoneplate": ("ChainVest", "NegatronCloak"),
              "GiantSlayer": ("BFSword", "RecurveBow"),
              "MascotEmblem": ("GiantsBelt", "Spatula"),
              "GuinsoosRageblade": ("NeedlesslyLargeRod", "RecurveBow"),
              "HandofJustice": ("SparringGloves", "TearoftheGoddess"),
              "HextechGunblade": ("BFSword", "NeedlesslyLargeRod"),
              "InfinityEdge": ("BFSword", "SparringGloves"),
              "IonicSpark": ("NeedlesslyLargeRod", "NegatronCloak"),
              "JeweledGauntlet": ("NeedlesslyLargeRod", "SparringGloves"),
              "LastWhisper": ("RecurveBow", "SparringGloves"),
              "LocketoftheIronSolari": ("ChainVest", "NeedlesslyLargeRod"),
              "HeartEmblem": ("TearoftheGoddess", "Spatula"),
              "ADMINEmblem": ("NegatronCloak", "Spatula"),
              "Morellonomicon": ("GiantsBelt", "NeedlesslyLargeRod"),
              "Quicksilver": ("NegatronCloak", "SparringGloves"),
              "RabadonsDeathcap": ("NeedlesslyLargeRod", "NeedlesslyLargeRod"),
              "DuelistEmblem": ("RecurveBow", "Spatula"),
              "RapidFirecannon": ("RecurveBow", "RecurveBow"),
              "Redemption": ("GiantsBelt", "TearoftheGoddess"),
              "RunaansHurricane": ("NegatronCloak", "RecurveBow"),
              "LaserCorpsEmblem": ("BFSword", "Spatula"),
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
