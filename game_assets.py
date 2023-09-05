"""
Contains static item
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

GADGETEEN_ITEMS: set[str] = {"InductionPoweredWarmogsArmor", "JumpStartedSpearofShojin",
                             "MagnetizedIonicSpark", "HandofNondeterministicJustice", "OVERFLOWERROR//GiantSlayer",
                             "ChainswordBloodthirster", "ShroudofEvenStillerness", "OverclockedSunfireCape"}

ORNN_ITEMS: set[str] = {"AnimaVisage","DeathsDefiance","EternalWinter",
                        "GoldCollector","InfinityForce",
                        "Manazane","ObsidianCleaver","RaduinsSanctum",
                        "RocketPropelledFist","ZhonyasParadox"}

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

ITEMS: set[str] = COMBINED_ITEMS.union(ELUSIVE_ITEMS).union(ORNN_ITEMS)

ROUNDS: set[str] = {"1-1", "1-2", "1-3", "1-4",
          "2-1", "2-2", "2-3", "2-4", "2-5", "2-6", "2-7",
          "3-1", "3-2", "3-3", "3-4", "3-5", "3-6", "3-7",
          "4-1", "4-2", "4-3", "4-4", "4-5", "4-6", "4-7",
          "5-1", "5-2", "5-3", "5-4", "5-5", "5-6", "5-7",
          "6-1", "6-2", "6-3", "6-4", "6-5", "6-6", "6-7",
          "7-1", "7-2", "7-3", "7-4", "7-5", "7-6", "7-7"}

PORTAL_ROUND: set[str] = {"1-1"}

SECOND_ROUND: set[str] = {"1-2"}

CAROUSEL_ROUND: set[str] = {"2-4", "3-4", "4-4", "5-4", "6-4", "7-4"}

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

REGION_ROUNDS: set[str] = {"2-5", "4-5"}

ITEM_PLACEMENT_ROUNDS: set[str] = {"2-1", "2-5", "2-7",
             "3-2", "3-5", "4-2", "4-5", "5-2", "5-5", 
             "5-7", "6-2", "6-5", "7-2", "7-5", "7-7"}

FINAL_COMP_ROUND = "4-5"

FULL_ITEMS = {  "ChallengerEmblem":("Spatula","RecurveBow"),
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

# No logic for certain augments meaning the bot won't know what to do if they are included in here
# (Anything that changes gameplay or adds something to the bench).
AUGMENTS: list[str] = [
    "March of Progress",
    "Tons of Stats!",
    "Gifts from the Fallen",
    "Item Grab Bag II",
    "Know Your Enemy",
    "Red Buff",
    "Unified Resistance I",
    "Unified Resistance II",
    "Level Up!",
    "You Have My Bow",
    "Harmacist II",
    "You Have My Sword",
    "Harmacist I",
    "Matyr",
    "Jewled Lotus III",
    "Built Different III",
    "Cybernetic Leech I",
    "Final Ascension",
    "Long Distance Pals II",
    "Cybernetic Leech II",
    "Combat Caster",
    "Magic Wand",
    "Idealism",
    "Battle Ready III",
    "Item Grab Bag I",
    "Harmacist III",
    "Final Grab Bag II",
    "Healing Orbs I",
    "Return on Investment",
    "Contagion",
    "Tiny Titans",
    "Battle Ready II",
    "Risky Moves",
    "Shoplifting",
    "Last Stand",
    "Jewled Lotus II",
    "Money Money!",
    "Healing Orbs II",
    "Giant Grab Bag",
    "Cybernetic Leech III",
]

PORTALS: list[str] = [
    "Marus Omegnum",
    "Stillwater Hold",
    "Ecliptic Vaults",
    "Petricite Forest",
    "The Lavender Sea",
    "The University",
    "Jayce's Workshop",
    "Glasc Industries",
    "The Sump",
    "The Rupture",
]
