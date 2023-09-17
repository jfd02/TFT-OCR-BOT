"""
Contains static item & champion data
"""

BASIC_ITEM: set[str] = {"BFSword","ChainVest","GiantsBelt","NeedlesslyLargeRod",
                            "NegatronCloak","RecurveBow","SparringGloves","Spatula",
                            "TearoftheGoddess"}

COMBINED_ITEMS: set[str] = {"BilgewaterEmblem","ChallengerEmblem","IoniaEmblem","JuggernautEmblem",
                            "NoxusEmblem","ShurimaEmblem","SorcererEmblem","VanquisherEmblem",
                            "AdaptiveHelm","ArchangelsStaff","Bloodthirster","BlueBuff",
                            "BrambleVest","Crownguard","Deathblade","DragonsClaw",
                            "EdgeofNight","Evenshroud","GargoyleStoneplate","GiantSlayer",
                            "Guardbreaker","GuinsoosRageblade","HandofJustice","HextechGunblade",
                            "InfinityEdge","IonicSpark","JeweledGauntlet","LastWhisper",
                            "Morellonomicon","NashorsTooth","NightHarvester","ProtectorsVow",
                            "Quicksilver","RabadonsDeathcap","RapidFirecannon","Redemption",
                            "RunaansHurricane","SpearofShojin","StatikkShiv","SteraksGage",
                            "SunfireCape","TacticiansCrown","ThiefsGloves","TitansResolve",
                            "WarmogsArmor"}

SUPPORT_ITEM: set[str] = {"AegisoftheLegion","BansheesVeil","ChaliceofPower","CrestofCinders",
                            "LocketoftheIronSolari","NeedlesslyBigGem","ObsidianCleaver","RanduinsOmen",
                            "ShroudofStillness","VirtueoftheMartyr","ZekesHerald","Zephyr","ZzRotPortal"}

NON_CRAFTABLE_ITEMS: set[str] = {"BastionEmblem","BruiserEmblem","DeadeyeEmblem","FreljordEmblem",
                                    "GunnerEmblem","InvokerEmblem","PiltoverEmblem","RogueEmblem",
                                    "StrategistEmblem","TargonEmblem","VoidEmblem","ZaunEmblem"}

ORNN_ITEMS: set[str] = {"AnimaVisage","BlacksmithsGloves","DeathfireGrasp","DeathsDefiance",
                        "EternalWinter","GoldCollector","GoldmancersStaff","Hullcrusher",
                        "InfinityForce","MogulsMail","Muramana","Rocket-PropelledFist",
                        "SnipersFocus","TrickstersGlass","ZhonyasParadox"}

ITEMS: set[str] = BASIC_ITEM.union(COMBINED_ITEMS).union(SUPPORT_ITEM).union(NON_CRAFTABLE_ITEMS).union(ORNN_ITEMS)

CHAMPIONS: dict[str, dict[str, int]] = {
    "Aatrox": {"Gold": 5, "Board Size": 1},
    "Ahri": {"Gold": 5, "Board Size": 1},
    "Aphelios": {"Gold": 4, "Board Size": 1},
    "Ashe": {"Gold": 2, "Board Size": 1},
    "Azir": {"Gold": 4, "Board Size": 1},
    "BelVeth": {"Gold": 5, "Board Size": 1},
    "Cassiopeia": {"Gold": 1, "Board Size": 1},
    "ChoGath": {"Gold": 1, "Board Size": 1},
    "Darius": {"Gold": 3, "Board Size": 1},
    "Ekko": {"Gold": 3, "Board Size": 1},
    "Fiora": {"Gold": 4, "Board Size": 1},
    "Galio": {"Gold": 2, "Board Size": 1},
    "Gangplank": {"Gold": 5, "Board Size": 1},
    "Graves": {"Gold": 1, "Board Size": 1},
    "Heimerdinger": {"Gold": 5, "Board Size": 1},
    "Illaoi": {"Gold": 1, "Board Size": 1},
    "Irelia": {"Gold": 1, "Board Size": 1},
    "Jarvan IV": {"Gold": 4, "Board Size": 1},
    "Jayce": {"Gold": 3, "Board Size": 1},
    "Jhin": {"Gold": 1, "Board Size": 1},
    "Jinx": {"Gold": 2, "Board Size": 1},
    "KaiSa": {"Gold": 4, "Board Size": 1},
    "Karma": {"Gold": 3, "Board Size": 1},
    "Kassadin": {"Gold": 2, "Board Size": 1},
    "Katarina": {"Gold": 3, "Board Size": 1},
    "Kayle": {"Gold": 1, "Board Size": 1},
    "KSante": {"Gold": 5, "Board Size": 1},
    "Malzahar": {"Gold": 1, "Board Size": 1},
    "Milio": {"Gold": 1, "Board Size": 1},
    "MissFortune": {"Gold": 3, "Board Size": 1},
    "Mordekaiser": {"Gold": 4, "Board Size": 1},
    "Naafiri": {"Gold": 2, "Board Size": 1},
    "Nasus": {"Gold": 4, "Board Size": 1},
    "Nautilus": {"Gold": 3, "Board Size": 1},
    "Neeko": {"Gold": 3, "Board Size": 1},
    "Nilah": {"Gold": 4, "Board Size": 1},
    "Orianna": {"Gold": 1, "Board Size": 1},
    "Poppy": {"Gold": 1, "Board Size": 1},
    "Qiyana": {"Gold": 2, "Board Size": 1},
    "Quinn": {"Gold": 3, "Board Size": 1},
    "RekSai": {"Gold": 3, "Board Size": 1},
    "Renekton": {"Gold": 1, "Board Size": 1},
    "Ryze": {"Gold": 5, "Board Size": 1},
    "Samira": {"Gold": 1, "Board Size": 1},
    "Sejuani": {"Gold": 4, "Board Size": 1},
    "Sett": {"Gold": 2, "Board Size": 1},
    "Shen": {"Gold": 4, "Board Size": 1},
    "Silco": {"Gold": 4, "Board Size": 1},
    "Sion": {"Gold": 5, "Board Size": 1},
    "Sona": {"Gold": 3, "Board Size": 1},
    "Soraka": {"Gold": 2, "Board Size": 1},
    "Swain": {"Gold": 2, "Board Size": 1},
    "Taliyah": {"Gold": 2, "Board Size": 1},
    "Taric": {"Gold": 3, "Board Size": 1},
    "TwistedFate": {"Gold": 2, "Board Size": 1},
    "VelKoz": {"Gold": 3, "Board Size": 1},
    "Vi": {"Gold": 2, "Board Size": 1},
    "Warwick": {"Gold": 2, "Board Size": 1},
    "Xayah": {"Gold": 4, "Board Size": 1}}

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

PICKUP_ROUNDS: set[str] = {"2-1", "3-1", "4-1", "5-1", "6-1", "7-1"}

ANVIL_ROUNDS: set[str] = {"2-1", "2-5", "3-1", "3-5", "4-1", "4-5", "5-1", "5-5", "6-1", "6-5", "7-1", "7-5"}

AUGMENT_ROUNDS: set[str] = {"2-1", "3-2", "4-2"}

ITEM_PLACEMENT_ROUNDS: set[str] = {"2-2", "3-2", "4-2", "5-2",
                                   "6-2", "7-2", "2-5", "3-5", "4-5", "5-5", "6-5", "7-5"}

FINAL_COMP_ROUND = "4-5"

FULL_ITEMS = {"BilgewaterEmblem":("Spatula","NegatronCloak"),
                "ChallengerEmblem":("Spatula","RecurveBow"),
                "IoniaEmblem":("Spatula","BFSword"),
                "JuggernautEmblem":("Spatula","ChainVest"),
                "NoxusEmblem":("Spatula","GiantsBelt"),
                "ShurimaEmblem":("Spatula","NeedlesslyLargeRod"),
                "SorcererEmblem":("Spatula","TearoftheGoddess"),
                "VanquisherEmblem":("Spatula","SparringGloves"),
                "AdaptiveHelm":("NegatronCloak","TearoftheGoddess"),
                "ArchangelsStaff":("NeedlesslyLargeRod","TearoftheGoddess"),
                "Bloodthirster":("BFSword","NegatronCloak"),
                "BlueBuff":("TearoftheGoddess","TearoftheGoddess"),
                "BrambleVest":("ChainVest","ChainVest"),
                "Crownguard":("ChainVest","NeedlesslyLargeRod"),
                "Deathblade":("BFSword","BFSword"),
                "DragonsClaw":("NegatronCloak","NegatronCloak"),
                "EdgeofNight":("BFSword","ChainVest"),
                "Evenshroud":("GiantsBelt","NegatronCloak"),
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
                "Morellonomicon":("GiantsBelt","NeedlesslyLargeRod"),
                "NashorsTooth":("GiantsBelt","RecurveBow"),
                "NightHarvester":("ChainVest","SparringGloves"),
                "ProtectorsVow":("ChainVest","TearoftheGoddess"),
                "Quicksilver":("NegatronCloak","SparringGloves"),
                "RabadonsDeathcap":("NeedlesslyLargeRod","NeedlesslyLargeRod"),
                "RapidFirecannon":("RecurveBow","RecurveBow"),
                "Redemption":("GiantsBelt","TearoftheGoddess"),
                "RunaansHurricane":("NegatronCloak","RecurveBow"),
                "SpearofShojin":("BFSword","TearoftheGoddess"),
                "StatikkShiv":("RecurveBow","TearoftheGoddess"),
                "SteraksGage":("BFSword","GiantsBelt"),
                "SunfireCape":("ChainVest","GiantsBelt"),
                "TacticiansCrown":("Spatula","Spatula"),
                "ThiefsGloves":("SparringGloves","SparringGloves"),
                "TitansResolve":("ChainVest","RecurveBow"),
                "WarmogsArmor":("GiantsBelt","GiantsBelt")}

def champion_board_size(champion: str) -> int:
    """Takes a string (champion name) and returns board size of champion"""
    return CHAMPIONS[champion]["Board Size"]


def champion_gold_cost(champion: str) -> int:
    """Takes a string (champion name) and returns gold of champion"""
    return CHAMPIONS[champion]["Gold"]
