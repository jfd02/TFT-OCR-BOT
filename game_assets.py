"""
Contains static item & champion data
"""

BASIC_ITEM: set[str] = {"BFSword","ChainVest","GiantsBelt","NeedlesslyLargeRod",
                            "NegatronCloak","RecurveBow","SparringGloves","Spatula",
                            "TearoftheGoddess"}

COMBINED_ITEMS: set[str] = {"BFSword","ChainVest","GiantsBelt","NeedlesslyLargeRod",
                            "NegatronCloak","RecurveBow","SparringGloves","Spatula",
                            "TearoftheGoddess","8bitEmblem","EmoEmblem","HEARTSTEELEmblem",
                            "JazzEmblem","KDAEmblem","PentakillEmblem","PunkEmblem",
                            "TrueDamageEmblem","AdaptiveHelm","ArchangelsStaff","Bloodthirster",
                            "BlueBuff","BrambleVest","Crownguard","Deathblade",
                            "DragonsClaw","EdgeofNight","Evenshroud","GargoyleStoneplate",
                            "GiantSlayer","Guardbreaker","GuinsoosRageblade","HandofJustice",
                            "HextechGunblade","InfinityEdge","IonicSpark","JeweledGauntlet",
                            "LastWhisper","Morellonomicon","NashorsTooth","ProtectorsVow",
                            "Quicksilver","RabadonsDeathcap","RedBuff","Redemption",
                            "RunaansHurricane","SpearofShojin","StatikkShiv","SteadfastHeart",
                            "SteraksGage","SunfireCape","TacticiansCrown","ThiefsGloves",
                            "TitansResolve","WarmogsArmor","BigShotEmblem","BruiserEmblem",
                            "CountryEmblem","CrowdDiverEmblem","DazzlerEmblem","DiscoEmblem",
                            "EdgelordEmblem","ExecutionerEmblem","GuardianEmblem","HyperpopEmblem",
                            "MosherEmblem","RapidfireEmblem","SentinelEmblem","SpellweaverEmblem",
                            "SuperfanEmblem"}

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
    "Ahri": {"Gold": 4, "Board Size": 1},
    "Akali": {"Gold": 4, "Board Size": 1},
    "Amumu": {"Gold": 3, "Board Size": 1},
    "Annie": {"Gold": 1, "Board Size": 1},
    "Aphelios": {"Gold": 2, "Board Size": 1},
    "Bard": {"Gold": 2, "Board Size": 1},
    "Blitzcrank": {"Gold": 4, "Board Size": 1},
    "Caitlyn": {"Gold": 4, "Board Size": 1},
    "Corki": {"Gold": 1, "Board Size": 1},
    "Ekko": {"Gold": 3, "Board Size": 1},
    "Evelynn": {"Gold": 1, "Board Size": 1},
    "Ezreal": {"Gold": 4, "Board Size": 1},
    "Garen": {"Gold": 2, "Board Size": 1},
    "Gnar": {"Gold": 2, "Board Size": 1},
    "Gragas": {"Gold": 2, "Board Size": 1},
    "Illaoi": {"Gold": 5, "Board Size": 1},
    "Jax": {"Gold": 2, "Board Size": 1},
    "Jhin": {"Gold": 5, "Board Size": 1},
    "Jinx": {"Gold": 1, "Board Size": 1},
    "KaiSa": {"Gold": 2, "Board Size": 1},
    "Karthus": {"Gold": 4, "Board Size": 1},
    "Katarina": {"Gold": 2, "Board Size": 1},
    "Kayle": {"Gold": 2, "Board Size": 1},
    "Kayn": {"Gold": 5, "Board Size": 1},
    "Kennen": {"Gold": 1, "Board Size": 1},
    "KSante": {"Gold": 1, "Board Size": 1},
    "Lillia": {"Gold": 1, "Board Size": 1},
    "Lucian": {"Gold": 5, "Board Size": 1},
    "Lulu": {"Gold": 3, "Board Size": 1},
    "Lux": {"Gold": 3, "Board Size": 1},
    "MissFortune": {"Gold": 3, "Board Size": 1},
    "Mordekaiser": {"Gold": 3, "Board Size": 1},
    "Nami": {"Gold": 1, "Board Size": 1},
    "Neeko": {"Gold": 3, "Board Size": 1},
    "Olaf": {"Gold": 1, "Board Size": 1},
    "Pantheon": {"Gold": 2, "Board Size": 1},
    "Poppy": {"Gold": 4, "Board Size": 1},
    "Qiyana": {"Gold": 5, "Board Size": 1},
    "Riven": {"Gold": 3, "Board Size": 1},
    "Samira": {"Gold": 3, "Board Size": 1},
    "Senna": {"Gold": 2, "Board Size": 1},
    "Seraphine": {"Gold": 2, "Board Size": 1},
    "Sett": {"Gold": 3, "Board Size": 1},
    "Sona": {"Gold": 5, "Board Size": 1},
    "TahmKench": {"Gold": 1, "Board Size": 1},
    "Taric": {"Gold": 1, "Board Size": 1},
    "Thresh": {"Gold": 4, "Board Size": 1},
    "TwistedFate": {"Gold": 4, "Board Size": 1},
    "Twitch": {"Gold": 2, "Board Size": 1},
    "Urgot": {"Gold": 3, "Board Size": 1},
    "Vex": {"Gold": 3, "Board Size": 1},
    "Vi": {"Gold": 1, "Board Size": 1},
    "Viego": {"Gold": 4, "Board Size": 1},
    "Yasuo": {"Gold": 1, "Board Size": 1},
    "Yone": {"Gold": 3, "Board Size": 1},
    "Yorick": {"Gold": 5, "Board Size": 1},
    "Zac": {"Gold": 4, "Board Size": 1},
    "Zed": {"Gold": 4, "Board Size": 1},
    "Ziggs": {"Gold": 5, "Board Size": 1}}

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

ANVIL_ROUNDS: set[str] = {"1-3", "2-1", "2-5", "3-1", "3-5", "4-1", "4-5", "5-1", "5-5", "6-1", "6-5", "7-1", "7-5"}

AUGMENT_ROUNDS: set[str] = {"2-1", "3-2", "4-2"}

ITEM_PLACEMENT_ROUNDS: set[str] = {"2-2", "3-2", "4-2", "5-2",
                                   "6-2", "7-2", "2-5", "3-5", "4-5", "5-5", "6-5", "7-5"}

FINAL_COMP_ROUND = "4-5"

FULL_ITEMS = {"8bitEmblem":("Spatula","RecurveBow"),
                "EmoEmblem":("Spatula","TearoftheGoddess"),
                "HEARTSTEELEmblem":("Spatula","GiantsBelt"),
                "JazzEmblem":("Spatula","NegatronCloak"),
                "KDAEmblem":("Spatula","NeedlesslyLargeRod"),
                "PentakillEmblem":("Spatula","ChainVest"),
                "PunkEmblem":("Spatula","SparringGloves"),
                "TrueDamageEmblem":("Spatula","SparringGloves"),
                "AdaptiveHelm":("NegatronCloak","B.F.Sword"),
                "ArchangelsStaff":("NeedlesslyLargeRod","TearoftheGoddess"),
                "Bloodthirster":("B.F.Sword","NegatronCloak"),
                "BlueBuff":("TearoftheGoddess","TearoftheGoddess"),
                "BrambleVest":("ChainVest","ChainVest"),
                "Crownguard":("ChainVest","NeedlesslyLargeRod"),
                "Deathblade":("B.F.Sword","B.F.Sword"),
                "DragonsClaw":("NegatronCloak","NegatronCloak"),
                "EdgeofNight":("B.F.Sword","ChainVest"),
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
                "ProtectorsVow":("ChainVest","TearoftheGoddess"),
                "Quicksilver":("NegatronCloak","SparringGloves"),
                "RabadonsDeathcap":("NeedlesslyLargeRod","NeedlesslyLargeRod"),
                "RedBuff":("RecurveBow","RecurveBow"),
                "Redemption":("GiantsBelt","TearoftheGoddess"),
                "RunaansHurricane":("NegatronCloak","RecurveBow"),
                "SpearofShojin":("BFSword","TearoftheGoddess"),
                "StatikkShiv":("RecurveBow","TearoftheGoddess"),
                "SteadfastHeart":("ChainVest","SparringGloves"),
                "SteraksGage":("B.F.Sword","GiantsBelt"),
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
