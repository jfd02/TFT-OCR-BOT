"""
Contains static item & champion data
"""

COMPONENT_AND_CRAFTABLE_ITEMS: set[str] = {"BFSword", "ChainVest", "GiantsBelt", "NeedlesslyLargeRod",
                       "NegatronCloak", "RecurveBow", "SparringGloves", "Spatula",
                       "TearoftheGoddess",
                       "ChallengerEmblem", "Crownguard", "DemaciaEmblem",
                       "IoniaEmblem", "JuggernautEmblem", "NoxusEmblem", "ShurimaEmblem", "SlayerEmblem",
                       "SorcererEmblem",
                       "AdaptiveHelm", "ArchangelsStaff", "Bloodthirster", "BlueBuff",
                       "BrambleVest", "Deathblade", "DragonsClaw",
                       "EdgeofNight", "GargoyleStoneplate", "GiantSlayer", "Guardbreaker",
                       "GuinsoosRageblade", "HandofJustice", "HextechGunblade", "InfinityEdge",
                       "IonicSpark", "JeweledGauntlet", "LastWhisper",
                       "Morellonomicon", "ProtectorsVow", "Quicksilver", "RabadonsDeathcap",
                       "RapidFirecannon", "Redemption", "RunaansHurricane",
                       "SpearofShojin", "StatikkShiv", "SunfireCape", "TacticiansCrown",
                       "ThiefsGloves", "TitansResolve", "WarmogsArmor"}

SUPPORT_ITEMS: set[str] = {"AegisoftheLegion", "BansheesVeil", "CrestOfCinders", "VirtueoftheMartyr", "ChaliceofPower"
                           "LocketoftheIronSolari", "NeedlesslyBigGem", "ObsidianCleaver", "RanduinsOmen",
                           "ShroudofStillness", "ZekesHerald", "Zephyr", "ZzRotPortal"}

TRAIT_ITEMS: set[str] = {"BastionEmblem", "BruiserEmblem", "ChallengerEmblem", "DeadeyeEmblem", "DemaciaEmblem",
                           "FreljordEmblem", "GunnerEmblem", "InvokerEmblem", "IoniaEmblem", "JuggernautEmblem",
                           "NoxusEmblem", "PiltoverEmblem", "RogueEmblem", "ShadowIslesEmblem", "ShurimaEmblem",
                           "SlayerEmblem", "SorcererEmblem", "StrategistEmblem", "TargonEmblem", "VoidEmblem",
                           "ZaunEmblem"}

# Trait Items that cannot be crafted
ELUSIVE_ITEMS: set[str] = {"BastionEmblem", "BruiserEmblem", "DeadeyeEmblem", "FreljordEmblem",
                           "GunnerEmblem", "InvokerEmblem", "PiltoverEmblem", "RogueEmblem",
                           "StrategistEmblem", "TargonEmblem", "VoidEmblem", "ZaunEmblem"}

ORNN_ITEMS: set[str] = {"AnimaVisage", "BlacksmithsGloves", "DeathsDefiance", "DeathfireGrasp", "EternalWinter",
                        "GoldCollector", "GoldmancersStaff", "Hullcrusher", "InfinityForce", "Manazane", "MogulsMail",
                        "RaduinsSanctum", "RocketPropelledFist", "SnipersFocus", "TrickstersGlass",
                        "ZhonyasParadox"}

RADIANT_ITEMS: set[str] = {"Absolution", "BlessedBloodthirster", "BlueBlessing", "BrinkofDawn", "BulkwarsOath",
                           "ChaliceofCharity", "CovalentSpark", "DemonSlayer", "DragonsWill", "DvarapalaStoneplate",
                           "EternalWhisper", "FistofFairness", "GlamorousGauntlet", "GuinsoosReckoning",
                           "HextechLifeblade", "LocketofTargonPrime", "LuminousDeathblade", "Mistral",
                           "MoreMoreellonomicon", "Quickestsilver", "RabadonsAscendedDeathcap", "RapidLightcannon",
                           "RascalsGloves", "RosethornVest", "RunaansTempest", "ShroudofReverance", "SpearofHirana",
                           "StatikkFavor", "SteraksMegashield", "Stridebreaker", "SunlightCape", "TitansVow",
                           "UrfAngelsStaff", "WarmogsPride", "ZekesHarmony", "ZenithEdge", "ZzrotsInvitation"}

MOGUL_ITEMS: set[str] = {"DeterminedInvestor", "DiamondHands", "DravensAxe", "GamblersBlade"}

# Items that can only be given to Zaun trait units and pop off after each round.
ZAUN_ITEMS: set[str] = {"AdaptiveImplant", "HextechExoskeleton", "RoboticArm", "ShimmerInjector", "UnstableChemtank"
                                                                                                  "VirulentBioware"}

MISC_ITEMS: set[str] = {"CrownofDemacia", "Masterworkupgrade", "ScrollofKnowledge", "TheDarkinBlade"}

ITEMS: set[str] = COMPONENT_AND_CRAFTABLE_ITEMS.union(ELUSIVE_ITEMS)\
                                               .union(SUPPORT_ITEMS)\
                                               .union(TRAIT_ITEMS)\
                                               .union(ORNN_ITEMS)\
                                               .union(RADIANT_ITEMS)\
                                               .union(ZAUN_ITEMS)\
                                               .union(MISC_ITEMS)

# All the augments in the game that won't require the bot to react to
# (i.e. don't give a unit or item, affect level, cost to buy xp, etc.).
FULLY_PASSIVE_SILVER_AUGMENTS: set[str] = \
    {"All Natural I", "Balanced Budget I", "Battle Ready I", "Blood Money", "Bronze Ticket", "Consistency",
     "Cybernetic Bulk I", "Cybernetic Leech I", "Gotta Go Fast!!! I", "Harmacist I", "Healing Orbs I", "Inconsistency",
     "Indomitable Will", "It Pays To Learn I", "Jeweled Lotus I", "Knowledge Download", "Lategame Specialist", "Money!",
     "Partial Ascension", "Pumping Up I", "Red Buff", "Rolling for Day I", "Silver Spoon", "Social Distancing I",
     "Tiny Titans", "Tiny Power I", "Transfusion I", "Unburdened I", "Unified Resistance I", "Well-Earned Comforts I"}

FULLY_PASSIVE_GOLD_AUGMENTS: set[str] = []

FULLY_PASSIVE_PLATINUM_AUGMENTS: set[str] = []

FULLY_PASSIVE_AUGMENTS: set[str] = FULLY_PASSIVE_SILVER_AUGMENTS.union(FULLY_PASSIVE_GOLD_AUGMENTS) \
    .union(FULLY_PASSIVE_PLATINUM_AUGMENTS)

CHAMPIONS: dict[str, dict[str, int]] = {
    "Aatrox": {"Gold": 5, "Board Size": 1},
    "Ahri": {"Gold": 5, "Board Size": 1},
    # "Akshan": {"Gold": 3, "Board Size": 1},
    "Aphelios": {"Gold": 4, "Board Size": 1},
    "Ashe": {"Gold": 2, "Board Size": 1},
    "Azir": {"Gold": 4, "Board Size": 1},
    "Belveth": {"Gold": 5, "Board Size": 1},
    "Cassiopeia": {"Gold": 1, "Board Size": 1},
    "Chogath": {"Gold": 1, "Board Size": 1},
    "Darius": {"Gold": 3, "Board Size": 1},
    "Ekko": {"Gold": 3, "Board Size": 1},
    "Fiora": {"Gold": 4, "Board Size": 1},
    "Galio": {"Gold": 2, "Board Size": 1},
    "Gangplank": {"Gold": 5, "Board Size": 1},
    # "Garen": {"Gold": 3, "Board Size": 1},
    "Graves": {"Gold": 1, "Board Size": 1},
    # "Gwen": {"Gold": 4, "Board Size": 1},
    "Heimerdinger": {"Gold": 5, "Board Size": 1},
    "Irelia": {"Gold": 1, "Board Size": 1},
    "Illaoi": {"Gold": 1, "Board Size": 1},
    "Jarvan IV": {"Gold": 4, "Board Size": 1},
    "Jayce": {"Gold": 3, "Board Size": 1},
    "Jhin": {"Gold": 1, "Board Size": 1},
    "Jinx": {"Gold": 2, "Board Size": 1},
    "KSante": {"Gold": 5, "Board Size": 1},
    "Kaisa": {"Gold": 4, "Board Size": 1},
    # "Kalista": {"Gold": 3, "Board Size": 1},
    "Karma": {"Gold": 3, "Board Size": 1},
    "Kassadin": {"Gold": 2, "Board Size": 1},
    "Katarina": {"Gold": 3, "Board Size": 1},
    "Kayle": {"Gold": 1, "Board Size": 1},
    # "Kled": {"Gold": 2, "Board Size": 1},
    # "Lissandra": {"Gold": 3, "Board Size": 1},
    # "Lux": {"Gold": 4, "Board Size": 1},
    "Malzahar": {"Gold": 1, "Board Size": 1},
    # "Maokai": {"Gold": 1, "Board Size": 1},
    "Milio": {"Gold": 1, "Board Size": 1},
    "Miss Fortune": {"Gold": 3, "Board Size": 1},
    "Mordekaiser": {"Gold": 4, "Board Size": 1},
    "Naafiri": {"Gold": 2, "Board Size": 1},
    "Nasus": {"Gold": 4, "Board Size": 1},
    "Nautilus": {"Gold": 3, "Board Size": 1},
    "Nilah": {"Gold": 4, "Board Size": 1},
    "Neeko": {"Gold": 3, "Board Size": 1},
    "Orianna": {"Gold": 1, "Board Size": 1},
    "Poppy": {"Gold": 1, "Board Size": 1},
    "Qiyana": {"Gold": 2, "Board Size": 1},
    "Quinn": {"Gold": 3, "Board Size": 1},
    "RekSai": {"Gold": 3, "Board Size": 1},
    "Renekton": {"Gold": 1, "Board Size": 1},
    "Ryze": {"Gold": 5, "Board Size": 1},
    "Samira": {"Gold": 1, "Board Size": 1},
    "Sejuani": {"Gold": 4, "Board Size": 1},
    # "Senna": {"Gold": 5, "Board Size": 1},
    "Sett": {"Gold": 2, "Board Size": 1},
    "Shen": {"Gold": 4, "Board Size": 1},
    "Silco": {"Gold": 4, "Board Size": 1},
    "Sion": {"Gold": 5, "Board Size": 1},
    "Sona": {"Gold": 3, "Board Size": 1},
    "Soraka": {"Gold": 2, "Board Size": 1},
    "Swain": {"Gold": 2, "Board Size": 1},
    "Taliyah": {"Gold": 2, "Board Size": 1},
    "Taric": {"Gold": 3, "Board Size": 1},
    # "Teemo": {"Gold": 2, "Board Size": 1},
    # "Tristana": {"Gold": 1, "Board Size": 1},
    "Twisted Fate": {"Gold": 2, "Board Size": 1},
    # "Urgot": {"Gold": 4, "Board Size": 1},
    "Velkoz": {"Gold": 3, "Board Size": 1},
    "Vi": {"Gold": 2, "Board Size": 1},
    # "Viego": {"Gold": 1, "Board Size": 1},
    "Warwick": {"Gold": 2, "Board Size": 1},
    "Xayah": {"Gold": 4, "Board Size": 1},
    # "Yasuo": {"Gold": 4, "Board Size": 1},
    # "Zed": {"Gold": 2, "Board Size": 1},
    # "Zeri": {"Gold": 4, "Board Size": 1}
    }

ROUNDS: set[str] = {"1-1", "1-2", "1-3", "1-4",
                    "2-1", "2-2", "2-3", "2-4", "2-5", "2-6", "2-7",
                    "3-1", "3-2", "3-3", "3-4", "3-5", "3-6", "3-7",
                    "4-1", "4-2", "4-3", "4-4", "4-5", "4-6", "4-7",
                    "5-1", "5-2", "5-3", "5-4", "5-5", "5-6", "5-7",
                    "6-1", "6-2", "6-3", "6-4", "6-5", "6-6", "6-7",
                    "7-1", "7-2", "7-3", "7-4", "7-5", "7-6", "7-7"}

SECOND_ROUND: set[str] = {"1-2"}

THIRD_ROUND: set[str] = {"1-3"}

CAROUSEL_ROUND: set[str] = {"1-1", "2-4", "3-4", "4-4", "5-4", "6-4", "7-4"}

PVE_ROUND: set[str] = {"1-3", "1-4", "2-7", "3-7", "4-7", "5-7", "6-7", "7-7"}

PVP_ROUND: set[str] = {"2-1", "2-2", "2-3", "2-5", "2-6",
                       "3-1", "3-2", "3-3", "3-5", "3-6",
                       "4-1", "4-2", "4-3", "4-5", "4-6",
                       "5-1", "5-2", "5-3", "5-5", "5-6",
                       "6-1", "6-2", "6-3", "6-5", "6-6",
                       "7-1", "7-2", "7-3", "7-5", "7-6"}

# Picking up items currently takes a long time, so limit as much as possible.
PICKUP_ROUNDS: set[str] = {"2-1", "3-2", "4-2", "5-1", "6-1", "7-1"}

ANVIL_ROUNDS: set[str] = {"2-3", "3-3", "4-3", "5-3", "6-3", "7-3"}

AUGMENT_ROUNDS: set[str] = {"2-1", "3-2", "4-2"}

ITEM_PLACEMENT_ROUNDS: set[str] = {"2-1", "3-1", "4-1", "5-1", "6-1", "7-1",
                                   "2-3", "3-3", "4-3", "5-3", "6-3", "7-3",
                                   "2-5", "3-5", "4-5", "5-5", "6-5", "7-5"}

FINAL_COMP_ROUND = "4-1"

CRAFTABLE_ITEMS_DICT = {"ChallengerEmblem": ("Spatula", "RecurveBow"),
                        "DemaciaEmblem": ("Spatula", "NegatronCloak"),
                        "IoniaEmblem": ("Spatula", "B.F.Sword"),
                        "JuggernautEmblem": ("Spatula", "ChainVest"),
                        "NoxusEmblem": ("Spatula", "GiantsBelt"),
                        "ShurimaEmblem": ("Spatula", "NeedlesslyLargeRod"),
                        "SlayerEmblem": ("Spatula", "SparringGloves"),
                        "SorcererEmblem": ("Spatula", "TearoftheGoddess"),

                        "AdaptiveHelm": ("NegatronCloak", "TearoftheGoddess"),
                        "ArchangelsStaff": ("NeedlesslyLargeRod", "TearoftheGoddess"),
                        "Bloodthirster": ("B.F.Sword", "NegatronCloak"),
                        "BlueBuff": ("TearoftheGoddess", "TearoftheGoddess"),
                        "BrambleVest": ("ChainVest", "ChainVest"),
                        "Crownguard": ("ChainVest", "NeedlesslyLargeRod"),
                        # "ChaliceofPower": ("NegatronCloak", "TearoftheGoddess"),
                        "Deathblade": ("B.F.Sword", "B.F.Sword"),
                        "DragonsClaw": ("NegatronCloak", "NegatronCloak"),
                        "EdgeofNight": ("B.F.Sword", "ChainVest"),
                        "Evenshroud": ("GiantsBelt", "NegatronCloak"),
                        "GargoyleStoneplate": ("ChainVest", "NegatronCloak"),
                        "GiantSlayer": ("BFSword", "RecurveBow"),
                        "Guardbreaker": ("GiantsBelt", "SparringGloves"),
                        "GuinsoosRageblade": ("NeedlesslyLargeRod", "RecurveBow"),
                        "HandofJustice": ("SparringGloves", "TearoftheGoddess"),
                        "HextechGunblade": ("BFSword", "NeedlesslyLargeRod"),
                        "InfinityEdge": ("BFSword", "SparringGloves"),
                        "IonicSpark": ("NeedlesslyLargeRod", "NegatronCloak"),
                        "JeweledGauntlet": ("NeedlesslyLargeRod", "SparringGloves"),
                        "LastWhisper": ("RecurveBow", "SparringGloves"),
                        # "LocketoftheIronSolari": ("ChainVest", "NeedlesslyLargeRod"),
                        "Morellonomicon": ("GiantsBelt", "NeedlesslyLargeRod"),
                        "NashorsTooth": ("GiantsBelt", "RecurveBow"),
                        "NightHarvester": ("ChainVest", "SparringGloves"),
                        "ProtectorsVow": ("ChainVest", "TearoftheGoddess"),
                        "Quicksilver": ("NegatronCloak", "SparringGloves"),
                        "RabadonsDeathcap": ("NeedlesslyLargeRod", "NeedlesslyLargeRod"),
                        "RapidFirecannon": ("RecurveBow", "RecurveBow"),
                        "Redemption": ("GiantsBelt", "TearoftheGoddess"),
                        "RunaansHurricane": ("NegatronCloak", "RecurveBow"),
                        # "ShroudofStillness": ("ChainVest", "SparringGloves"),
                        "SpearofShojin": ("BFSword", "TearoftheGoddess"),
                        "StatikkShiv": ("RecurveBow", "TearoftheGoddess"),
                        "SteraksGage": ("BFSword", "GiantsBelt"),
                        "SunfireCape": ("ChainVest", "GiantsBelt"),
                        "TacticiansCrown": ("Spatula", "Spatula"),
                        "ThiefsGloves": ("SparringGloves", "SparringGloves"),
                        "TitansResolve": ("ChainVest", "RecurveBow"),
                        "WarmogsArmor": ("GiantsBelt", "GiantsBelt"),
                        # "ZekesHerald": ("BFSword", "GiantsBelt"),
                        # "Zephyr": ("GiantsBelt", "NegatronCloak"),
                        # "ZzRotPortal": ("GiantsBelt", "RecurveBow")
                        }


def champion_board_size(champion: str) -> int:
    """Takes a string (champion name) and returns board size of champion"""
    return CHAMPIONS[champion]["Board Size"]


def champion_gold_cost(champion: str) -> int:
    """Takes a string (champion name) and returns gold of champion"""
    return CHAMPIONS[champion]["Gold"]
