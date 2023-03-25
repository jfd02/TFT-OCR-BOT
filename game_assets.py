"""
Contains static item
"""

COMBINED_ITEMS: set[str] = {"BFSword", "ChainVest", "GiantsBelt", "NeedlesslyLargeRod",
                            "NegatronCloak", "SparringGloves", "Spatula", "TearoftheGoddess",
                            "ArchangelsStaff", "RenegadeEmblem", "Guardbreaker", "Bloodthirster",
                            "BlueBuff", "BrambleVest", "MascotEmblem", "ChaliceofPower",
                            "Deathblade", "HeartEmblem", "DragonsClaw", "EdgeofNight",
                            "FrozenHeart", "GargoyleStoneplate", "GiantSlayer", "HandofJustice",
                            "HextechGunblade", "InfinityEdge", "InfiniTeamEmblem", "IonicSpark", 
                            "JeweledGauntlet", "LastWhisper", "LocketoftheIronSolari", 
                            "AnimaSquadEmblem", "ADMINEmblem", "Morellonomicon", "Quicksilver", 
                            "RabadonsDeathcap", "OxForceEmblem", "RapidFirecannon", "Redemption", 
                            "RunaansHurricane", "DuelistEmblem","ShroudofStillness", "SpearofShojin", 
                            "StatikkShiv", "SunfireCape","TacticiansCrown", "ThiefsGloves", 
                            "TitansResolve", "WarmogsArmor", "ZekesHerald", "Zephyr", 
                            "ZzRotPortal", "RecurveBow", "GuinsoosRageblade"}

ELUSIVE_ITEMS: set[str] = {"AceEmblem", "AegisEmblem", "BrawlerEmblem", "PRIMESelector", 
                           "SpellslingerEmblem", "StarGuardianEmblem", "SureshotEmblem", 
                           "DefenderEmblem", "MechaPRIMEEmblem", "GadgeteenEmblem", 
                           "HackerEmblem", "LaserCorpsEmblem", "PranksterEmblem", 
                           "RiftwalkerEmblem", "StarGuardianEmblem", "TheUndergroundEmblem"}

GADGETEEN_ITEMS: set[str] = {"InductionPoweredWarmogsArmor", "JumpStartedSpearofShojin", "GadgeteensTitansResolve",
                             "MagnetizedIonicSpark", "HandofNondeterministicJustice", "OVERFLOWERROR//GiantSlayer",
                             "ChainswordBloodthirster", "ShroudofEvenStillerness", "OverclockedSunfireCape"}

ORNN_ITEMS: set[str] = {"AnimaVisage", "DeathsDefiance", "EternalWinter",
                        "GoldCollector", "InfinityForce",
                        "Manazane", "ObsidianCleaver", "RaduinsSanctum",
                        "RocketPropelledFist", "ZhonyasParadox"}

RADIANT_ITEMS: set[str] = {"BulwarksOath", "UrfAngelsStaff", "BlessedBloodthirster", 
                           "BlueBlessing", "RosethornVest", "ChaliceofCharity", 
                           "LuminousDeathblade", "DragonsWill", "BrinkofDawn", 
                           "DvarapalaStoneplate", "DemonSlayer", "GuinsoosReckoning", 
                           "FistofFairness", "HextechLifeblade", "ZenithEdge", 
                           "CovalentSpark", "GlamorousGauntlet", "EternalWhisper", 
                           "LocketofTargonPrime", "Moremoreellonomicon", "Quickestsilver", 
                           "RabadonsAscendedDeathcap", "RapidLightcannon", "Absolution", 
                           "RunnansTempest", "ShroudofReverance", "SpearofHiranna", 
                           "StatikkFavor", "Stridebreaker", "SunlightCape", "RascalsGloves", 
                           "TitansVow", "WarmogsPride", "ZekesHarmony", "Mistral", 
                           "ZzRotsInvitation"}

ITEMS: set[str] = COMBINED_ITEMS.union(ELUSIVE_ITEMS).union(
    GADGETEEN_ITEMS).union(ORNN_ITEMS).union(RADIANT_ITEMS)

ITEMS_WITHOUT_COMBINED: set[str] = ELUSIVE_ITEMS.union(
    GADGETEEN_ITEMS).union(ORNN_ITEMS).union(RADIANT_ITEMS)


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

ANVIL_ROUNDS: set[str] = {"5-1", "6-1", "7-1"}

AUGMENT_ROUNDS: set[str] = {"2-1", "3-2", "4-2"}

ITEM_PLACEMENT_ROUNDS: set[str] = {"2-1", "2-5", "2-7",
             "3-1", "3-5", "3-7",
             "4-1", "4-5", "4-7",
             "5-2", "5-5", "5-7",
             "6-2", "6-3", "6-5", "6-6", "6-7",
             "7-2", "7-3","7-5", "7-6", "7-7"}

FINAL_COMP_ROUND = "5-5"

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
              "InfiniTeamEmblem": ("BFSword", "Spatula"),
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

# No logic for certain augments meaning the bot won't know what to do if they are included in here
# (Anything that changes gameplay or adds something to the bench).
AUGMENTS: list[str] = [
    "Featherweights",
    "Combat Training",
    "Celestial Blessing",
    "Knife's Edge",
    "First Aid Kit",
    "Contempt for the Weak",
    "Laser Focus",
    "Corps Focus",
    "Rising Spell Force",
    "Raider's Spoils",
    "Flaming Ricochet",
    "Get Paid",
    "Flurry",
    "Invigorate",
    "Reign of Anger",
    "Cull the Meek",
    "Rock Solid",
    "Guardian Spirit",
    "Cybernetic Implants",
    "Stand United",
    "Electrocharge",
    "Cybernetic Uplink",
    "Cybernetic Shell",
    "Tri Force",
    "Metabolic Accelerator",
    "Second Wind",
    "Luden's Echo",
    "Last Stand",
    "Ascension",
    "Tiny Titans",
    "Sunfire Board",
    "Wise Spending",
    "Component Grab Bag+",
    "Thrill of the Hunt",
    "Preparation",
    "Hustler",
    "Windfall++",
    "Verdant Veil",
    "Rich Get Richer+",
    "Axiom Arc",
]