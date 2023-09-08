"""
Contains static item & champion data
"""

COMBINED_ITEMS: set[str] = {"BFSword","ChainVest","GiantsBelt","NeedlesslyLargeRod",
                            "NegatronCloak","RecurveBow","SparringGloves","Spatula",
                            "TearoftheGoddess","ChallengerEmblem","DemaciaEmblem","IoniaEmblem",
                            "JuggernautEmblem","NoxusEmblem","ShurimaEmblem","SlayerEmblem",
                            "SorcererEmblem","ArchangelsStaff","Bloodthirster","BlueBuff",
                            "BrambleVest","ChaliceofPower","Deathblade","DragonsClaw",
                            "EdgeofNight","GargoyleStoneplate","GiantSlayer","Guardbreaker",
                            "GuinsoosRageblade","HandofJustice","HextechGunblade","InfinityEdge",
                            "IonicSpark","JeweledGauntlet","LastWhisper","LocketoftheIronSolari",
                            "Morellonomicon","ProtectorsVow","Quicksilver","RabadonsDeathcap",
                            "RapidFirecannon","Redemption","RunaansHurricane","ShroudofStillness",
                            "SpearofShojin","StatikkShiv","SunfireCape","TacticiansCrown",
                            "ThiefsGloves","TitansResolve","WarmogsArmor","ZekesHerald",
                            "Zephyr","ZzRotPortal"}

ELUSIVE_ITEMS: set[str] = {"BastionEmblem","BruiserEmblem","DeadeyeEmblem","FreljordEmblem",
                            "GunnerEmblem","InvokerEmblem","PiltoverEmblem","RogueEmblem",
                            "StrategistEmblem","TargonEmblem","VoidEmblem","ZaunEmblem"}

ORNN_ITEMS: set[str] = {"AnimaVisage", "DeathsDefiance", "EternalWinter",
                        "GoldCollector", "InfinityForce",
                        "Manazane", "ObsidianCleaver", "RaduinsSanctum",
                        "RocketPropelledFist", "ZhonyasParadox"}

ITEMS: set[str] = COMBINED_ITEMS.union(ELUSIVE_ITEMS).union(ORNN_ITEMS)

CHAMPIONS: dict[str, dict[str, int]] = {
    "Aatrox": {"Gold": 5, "Board Size": 1},
    "Ahri": {"Gold": 5, "Board Size": 1},
    "Akshan": {"Gold": 3, "Board Size": 1},
    "Aphelios": {"Gold": 4, "Board Size": 1},
    "Ashe": {"Gold": 2, "Board Size": 1},
    "Azir": {"Gold": 4, "Board Size": 1},
    "Belveth": {"Gold": 5, "Board Size": 1},
    "Cassiopeia": {"Gold": 1, "Board Size": 1},
    "Chogath": {"Gold": 1, "Board Size": 1},
    "Darius": {"Gold": 3, "Board Size": 1},
    "Ekko": {"Gold": 3, "Board Size": 1},
    "Galio": {"Gold": 2, "Board Size": 1},
    "Garen": {"Gold": 3, "Board Size": 1},
    "Gwen": {"Gold": 4, "Board Size": 1},
    "Heimerdinger": {"Gold": 5, "Board Size": 1},
    "Irelia": {"Gold": 1, "Board Size": 1},
    "Jarvan IV": {"Gold": 4, "Board Size": 1},
    "Jayce": {"Gold": 3, "Board Size": 1},
    "Jhin": {"Gold": 1, "Board Size": 1},
    "Jinx": {"Gold": 2, "Board Size": 1},
    "KSante": {"Gold": 5, "Board Size": 1},
    "Kaisa": {"Gold": 4, "Board Size": 1},
    "Kalista": {"Gold": 3, "Board Size": 1},
    "Karma": {"Gold": 3, "Board Size": 1},
    "Kassadin": {"Gold": 2, "Board Size": 1},
    "Katarina": {"Gold": 3, "Board Size": 1},
    "Kayle": {"Gold": 1, "Board Size": 1},
    "Kled": {"Gold": 2, "Board Size": 1},
    "Lissandra": {"Gold": 3, "Board Size": 1},
    "Lux": {"Gold": 4, "Board Size": 1},
    "Malzahar": {"Gold": 1, "Board Size": 1},
    "Maokai": {"Gold": 1, "Board Size": 1},
    "Nasus": {"Gold": 4, "Board Size": 1},
    "Orianna": {"Gold": 1, "Board Size": 1},
    "Poppy": {"Gold": 1, "Board Size": 1},
    "RekSai": {"Gold": 3, "Board Size": 1},
    "Renekton": {"Gold": 1, "Board Size": 1},
    "Ryze": {"Gold": 5, "Board Size": 1},
    "Samira": {"Gold": 1, "Board Size": 1},
    "Sejuani": {"Gold": 4, "Board Size": 1},
    "Senna": {"Gold": 5, "Board Size": 1},
    "Sett": {"Gold": 2, "Board Size": 1},
    "Shen": {"Gold": 4, "Board Size": 1},
    "Sion": {"Gold": 5, "Board Size": 1},
    "Sona": {"Gold": 3, "Board Size": 1},
    "Soraka": {"Gold": 2, "Board Size": 1},
    "Swain": {"Gold": 2, "Board Size": 1},
    "Taliyah": {"Gold": 2, "Board Size": 1},
    "Taric": {"Gold": 3, "Board Size": 1},
    "Teemo": {"Gold": 2, "Board Size": 1},
    "Tristana": {"Gold": 1, "Board Size": 1},
    "Urgot": {"Gold": 4, "Board Size": 1},
    "Velkoz": {"Gold": 3, "Board Size": 1},
    "Vi": {"Gold": 2, "Board Size": 1},
    "Viego": {"Gold": 1, "Board Size": 1},
    "Warwick": {"Gold": 2, "Board Size": 1},
    "Yasuo": {"Gold": 4, "Board Size": 1},
    "Zed": {"Gold": 2, "Board Size": 1},
    "Zeri": {"Gold": 4, "Board Size": 1}}

ROUNDS: set[str] = {"1-1", "1-2", "1-3", "1-4",
                    "2-1", "2-2", "2-3", "2-4", "2-5", "2-6", "2-7",
                    "3-1", "3-2", "3-3", "3-4", "3-5", "3-6", "3-7",
                    "4-1", "4-2", "4-3", "4-4", "4-5", "4-6", "4-7",
                    "5-1", "5-2", "5-3", "5-4", "5-5", "5-6", "5-7",
                    "6-1", "6-2", "6-3", "6-4", "6-5", "6-6", "6-7",
                    "7-1", "7-2", "7-3", "7-4", "7-5", "7-6", "7-7"}

SECOND_ROUND: set[str] = {"1-2"}

CAROUSEL_ROUND: set[str] = {"1-1", "2-4", "3-4", "4-4", "5-4", "6-4", "7-4"}

PVE_ROUND: set[str] = {"1-3", "1-4", "2-7", "3-7", "4-7", "5-7", "6-7", "7-7"}

PVP_ROUND: set[str] = {"2-1", "2-2", "2-3", "2-5", "2-6",
                       "3-1", "3-2", "3-3", "3-5", "3-6",
                       "4-1", "4-2", "4-3", "4-5", "4-6",
                       "5-1", "5-2", "5-3", "5-5", "5-6",
                       "6-1", "6-2", "6-3", "6-5", "6-6",
                       "7-1", "7-2", "7-3", "7-5", "7-6"}

PICKUP_ROUNDS: set[str] = {"2-1", "2-5", "3-1", "3-2", "3-5", "4-1", "4-2", "4-5", "5-1", "5-5", "6-1", "6-5", "7-1"}

ANVIL_ROUNDS: set[str] = {"2-1", "2-3", "2-5", "3-1", "3-3", "3-5", "4-1", "4-3", "4-5", "5-1", "5-3", "5-5", "6-1", "6-3", "6-5", "7-1", "7-3", "7-5"}

AUGMENT_ROUNDS: set[str] = {"2-1", "3-2", "4-2"}

ITEM_PLACEMENT_ROUNDS: set[str] = {"2-1", "3-1", "4-1", "5-1", "6-1", "7-1",
                                   "2-3", "3-3", "4-3", "5-3", "6-3", "7-3",
                                   "2-5", "3-5", "4-5", "5-5", "6-5", "7-5"}

FINAL_COMP_ROUND = "4-5"

FULL_ITEMS = {"ChallengerEmblem":("Spatula","RecurveBow"),
                "DemaciaEmblem":("Spatula","NegatronCloak"),
                "IoniaEmblem":("Spatula","B.F.Sword"),
                "JuggernautEmblem":("Spatula","ChainVest"),
                "NoxusEmblem":("Spatula","GiantsBelt"),
                "ShurimaEmblem":("Spatula","NeedlesslyLargeRod"),
                "SlayerEmblem":("Spatula","SparringGloves"),
                "SorcererEmblem":("Spatula","TearoftheGoddess"),
                "ArchangelsStaff":("NeedlesslyLargeRod","TearoftheGoddess"),
                "Bloodthirster":("B.F.Sword","NegatronCloak"),
                "BlueBuff":("TearoftheGoddess","TearoftheGoddess"),
                "BrambleVest":("ChainVest","ChainVest"),
                "ChaliceofPower":("NegatronCloak","TearoftheGoddess"),
                "Deathblade":("B.F.Sword","B.F.Sword"),
                "DragonsClaw":("NegatronCloak","NegatronCloak"),
                "EdgeofNight":("B.F.Sword","ChainVest"),
                "GargoyleStoneplate":("ChainVest","NegatronCloak"),
                "GiantSlayer":("BFSword","RecurveBow"),
                "Guardbreaker":("GiantsBelt","SparringGloves"),
                "GuinsoosRageblade":("NeedlesslyLargeRod","RecurveBow"),
                "HandofJustice":("SparringGloves","TearoftheGoddess"),
                "HextechGunblade":("BFSword","NeedlesslyLargeRod"),
                "InfinityEdge":("BFSword","SparringGloves"),
                "IonicSpark":("NeedlesslyLargeRod","NegatronCloak"),
                "JeweledGauntlet":("NeedlesslyLargeRod","SparringGloves"),
                "LastWhisper":("RecurveBow","SparringGloves"),
                "LocketoftheIronSolari":("ChainVest","NeedlesslyLargeRod"),
                "Morellonomicon":("GiantsBelt","NeedlesslyLargeRod"),
                "ProtectorsVow":("ChainVest","TearoftheGoddess"),
                "Quicksilver":("NegatronCloak","SparringGloves"),
                "RabadonsDeathcap":("NeedlesslyLargeRod","NeedlesslyLargeRod"),
                "RapidFirecannon":("RecurveBow","RecurveBow"),
                "Redemption":("GiantsBelt","TearoftheGoddess"),
                "RunaansHurricane":("NegatronCloak","RecurveBow"),
                "ShroudofStillness":("ChainVest","SparringGloves"),
                "SpearofShojin":("BFSword","TearoftheGoddess"),
                "StatikkShiv":("RecurveBow","TearoftheGoddess"),
                "SunfireCape":("ChainVest","GiantsBelt"),
                "TacticiansCrown":("Spatula","Spatula"),
                "ThiefsGloves":("SparringGloves","SparringGloves"),
                "TitansResolve":("ChainVest","RecurveBow"),
                "WarmogsArmor":("GiantsBelt","GiantsBelt"),
                "ZekesHerald":("BFSword","GiantsBelt"),
                "Zephyr":("GiantsBelt","NegatronCloak"),
                "ZzRotPortal":("GiantsBelt","RecurveBow")}

def champion_board_size(champion: str) -> int:
    """Takes a string (champion name) and returns board size of champion"""
    return CHAMPIONS[champion]["Board Size"]


def champion_gold_cost(champion: str) -> int:
    """Takes a string (champion name) and returns gold of champion"""
    return CHAMPIONS[champion]["Gold"]
