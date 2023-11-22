"""
Contains static item constants and sets.
"""

# Basic component items
COMPONENT_ITEMS: set[str] = {
    "BFSword",
    "ChainVest",
    "GiantsBelt",
    "NeedlesslyLargeRod",
    "NegatronCloak",
    "RecurveBow",
    "SparringGloves",
    "Spatula",
    "TearoftheGoddess"
    }

# Craftable non-emblem items
CRAFTABLE_NON_EMBLEM_ITEMS: set[str] = {
    "AdaptiveHelm",
    "ArchangelsStaff",
    "Bloodthirster",
    "BlueBuff",
    "BrambleVest",
    "Crownguard",
    "Deathblade",
    "DragonsClaw",
    "EdgeofNight",
    "Evenshroud",
    "GargoyleStoneplate",
    "GiantSlayer",
    "Guardbreaker",
    "GuinsoosRageblade",
    "HandofJustice",
    "HextechGunblade",
    "InfinityEdge",
    "IonicSpark",
    "JeweledGauntlet",
    "LastWhisper",
    "Morellonomicon",
    "NashorsTooth",
    "ProtectorsVow",
    "Quicksilver",
    "RabadonsDeathcap",
    "RedBuff",
    "Redemption",
    "RunaansHurricane",
    "SpearofShojin",
    "StatikkShiv",
    "SteadfastHeart",
    "SunfireCape",
    "SteraksGage",
    "TacticiansCrown",
    "ThiefsGloves",
    "TitansResolve",
    "WarmogsArmor"
    }

# Craftable emblem items
CRAFTABLE_EMBLEM_ITEMS: set[str] = {
    "8bitEmblem",
    "EmoEmblem",
    "HEARTSTEELEmblem",
    "JazzEmblem",
    "KDAEmblem",
    "PentakillEmblem",
    "PunkEmblem",
    "TrueDamgeEmblem",
    }

# Union of component, craftable non-emblem, and craftable emblem items
COMPONENT_AND_CRAFTABLE_ITEMS: set[str] = COMPONENT_ITEMS.union(CRAFTABLE_NON_EMBLEM_ITEMS).union(
    CRAFTABLE_EMBLEM_ITEMS)

# Support items
SUPPORT_ITEMS: set[str] = {
    "AegisoftheLegion",
    "BansheesVeil",
    "ChaliceofPower",
    "CrestOfCinders",
    "LocketoftheIronSolari",
    "NeedlesslyBigGem",
    "ObsidianCleaver",
    "RanduinsOmen",
    "ShroudofStillness",
    "VirtueoftheMartyr",
    "ZekesHerald",
    "Zephyr",
    "ZzRotPortal"
    }

# Trait items
TRAIT_ITEMS: set[str] = {
    "BastionEmblem",
    "BilgewaterEmblem",
    "BruiserEmblem",
    "ChallengerEmblem",
    "DeadeyeEmblem",
    "DemaciaEmblem",
    "FreljordEmblem",
    "GunnerEmblem",
    "InvokerEmblem",
    "IoniaEmblem",
    "IxtalEmblem",
    "JuggernautEmblem",
    "NoxusEmblem",
    "PiltoverEmblem",
    "RogueEmblem",
    "ShadowIslesEmblem",
    "ShurimaEmblem",
    "SlayerEmblem",
    "SorcererEmblem",
    "StrategistEmblem",
    "TargonEmblem",
    "VanquisherEmblem",
    "VoidEmblem",
    "ZaunEmblem"
    }

# Trait Items that cannot be crafted
ELUSIVE_ITEMS: set[str] = {
    "BigShotEmblem",
    "BruiserEmblem",
    "CountryEmblem",
    "CrowdDiverEmblem",
    "DazzlerEmblem",
    "DiscoEmblem",
    "EdgelordEmblem",
    "ExecutionerEmblem",
    "GuardianEmblem",
    "HyperpopEmblem",
    "MosherEmblem",
    "RapidfireEmblem",
    "SentinelEmblem",
    "SpellweaverEmblem",
    "SuperfanEmblem",
    }

# Ornn items
ORNN_ITEMS: set[str] = {
    "AnimaVisage",
    "BlacksmithsGloves",
    "DeathsDefiance",
    "DeathfireGrasp",
    "EternalWinter",
    "GoldCollector",
    "GoldmancersStaff",
    "Hullcrusher",
    "InfinityForce",
    "Manazane",
    "MogulsMail",
    "SnipersFocus",
    "TrickstersGlass",
    "ZhonyasParadox"
    }

# Radiant items
RADIANT_ITEMS: set[str] = {
    "Absolution",
    "BlessedBloodthirster",
    "BlueBlessing",
    "BrinkofDawn",
    "BulkwarsOath",
    "CovalentSpark",
    "CrestofCinders"
    "DemonSlayer",
    "DragonsWill",
    "DvarapalaStoneplate",
    "Equinox",
    "EternalWhisper",
    "FistofFairness",
    "GlamorousGauntlet",
    "GuinsoosReckoning",
    "HextechLifeblade",
    "JakshotheProtean",
    "LeagacyoftheColossus",
    "LuminousDeathblade",
    "MidnightReaper",
    "MoreMoreellonomicon",
    "NashorsToothRadiant",
    "Quickestsilver",
    "RabadonsAscendedDeathcap",
    "RascalsGloves",
    "RosethornVest",
    "RoyalCrownshield",
    "RunaansTempest",
    "SpearofHirana",
    "StatikkFavor",
    "SteraksMegashield",
    "StrideBreaker",
    "SunlightCape",
    "TitansVow",
    "UrfAngelsStaff",
    "WarmogsPride",
    "ZenithEdge",
    }

# Miscellaneous items
MISC_ITEMS: set[str] = {
    "ChampionDuplicator",
    "LesserChampionDuplicator",
    "LoadedDice",
    "MagneticRemover",
    "MasterworkUpgrade",
    "Reforger",
    "ScrollofKnowledge",
    "TargetDummy"
    }

# Union of all holdable items
HOLDABLE_ITEMS: set[str] = COMPONENT_AND_CRAFTABLE_ITEMS \
    .union(ELUSIVE_ITEMS) \
    .union(SUPPORT_ITEMS) \
    .union(TRAIT_ITEMS) \
    .union(ORNN_ITEMS) \
    .union(RADIANT_ITEMS)

# All items, including miscellaneous items
ALL_ITEMS: set[str] = HOLDABLE_ITEMS.union(MISC_ITEMS)

# All rounds
ROUNDS: set[str] = {
    "1-1",
    "1-2",
    "1-3",
    "1-4",
    "2-1",
    "2-2",
    "2-3",
    "2-4",
    "2-5",
    "2-6",
    "2-7",
    "3-1",
    "3-2",
    "3-3",
    "3-4",
    "3-5",
    "3-6",
    "3-7",
    "4-1",
    "4-2",
    "4-3",
    "4-4",
    "4-5",
    "4-6",
    "4-7",
    "5-1",
    "5-2",
    "5-3",
    "5-4",
    "5-5",
    "5-6",
    "5-7",
    "6-1",
    "6-2",
    "6-3",
    "6-4",
    "6-5",
    "6-6",
    "6-7",
    "7-1",
    "7-2",
    "7-3",
    "7-4",
    "7-5",
    "7-6",
    "7-7"
}

# Specific rounds
PORTAL_ROUND: set[str] = {"1-1"}
SECOND_ROUND: set[str] = {"1-2"}
THIRD_ROUND: set[str] = {"1-3"}
FOURTH_ROUND: set[str] = {"1-4"}
CAROUSEL_ROUND: set[str] = {"2-4", "3-4", "4-4", "5-4", "6-4", "7-4"}
PVE_ROUND: set[str] = {"2-7", "3-7", "4-7", "5-7", "6-7", "7-7"}
PVP_ROUND: set[str] = {
    "2-1", "2-2", "2-3", "2-5", "2-6",
    "3-1", "3-2", "3-3", "3-5", "3-6",
    "4-1", "4-2", "4-3", "4-5", "4-6",
    "5-1", "5-2", "5-3", "5-5", "5-6",
    "6-1", "6-2", "6-3", "6-5", "6-6",
    "7-1", "7-2", "7-3", "7-5", "7-6"
}
PICKUP_ROUNDS: set[str] = {"2-1", "3-1", "4-1", "5-1", "6-1", "7-1"}
ANVIL_ROUNDS: set[str] = {
    "2-1", "2-5",
    "3-1", "3-5",
    "4-1", "4-5",
    "5-1", "5-5",
    "6-1", "6-5",
    "7-1", "7-5"
}
LEVEL_ROUNDS: set[str] = {"2-1": 4, "2-5": 5, "3-2": 6, "4-1": 7, "5-1": 8}
AUGMENT_ROUNDS: set[str] = {"2-1", "3-2", "4-2"}
REGION_ROUNDS: set[str] = {"2-5", "4-5"}
ITEM_PLACEMENT_ROUNDS: set[str] = {
    "2-1", "2-3", "2-5",
    "3-1", "3-3", "3-5",
    "4-1", "4-3", "4-5",
    "5-1", "5-3", "5-5", "5-7",
    "6-1", "6-3", "6-5",
    "7-1", "7-3", "7-5"
}
FINAL_COMP_ROUND = "4-1"

# Dictionary of craftable items and their components
CRAFTABLE_ITEMS_DICT = {
    "8BitEmblem":("Spatula","RecurveBow"),
    "AdaptiveHelm":("NegatronCloak","TearoftheGoddess"),
    "ArchangelsStaff":("NeedlesslyLargeRod","TearoftheGoddess"),
    "Bloodthirster":("BFSword","NegatronCloak"),
    "BlueBuff":("TearoftheGoddess","TearoftheGoddess"),
    "BrambleVest":("ChainVest","ChainVest"),
    "Crownguard":("ChainVest","NeedlesslyLargeRod"),
    "Deathblade":("BFSword","BFSword"),
    "DragonsClaw":("NegatronCloak","NegatronCloak"),
    "EdgeofNight":("BFSword","ChainVest"),
    "EmoEmblem":("Spatula","TearoftheGoddess"),
    "Evenshroud":("GiantsBelt","NegatronCloak"),
    "GargoyleStoneplate":("ChainVest","NegatronCloak"),
    "GiantSlayer":("BFSword","RecurveBow"),
    "Guardbreaker":("GiantsBelt","SparringGloves"),
    "GuinsoosRageblade":("NeedlesslyLargeRod","RecurveBow"),
    "HeartsteelEmblem":("Spatula","GiantsBelt"),
    "HandofJustice":("SparringGloves","TearoftheGoddess"),
    "HextechGunblade":("BFSword","NeedlesslyLargeRod"),
    "InfinityEdge":("BFSword","SparringGloves"),
    "IonicSpark":("NeedlesslyLargeRod","NegatronCloak"),
    "JazzEmblem":("Spatula","NegatronCloak"),
    "JeweledGauntlet":("NeedlesslyLargeRod","SparringGloves"),
    "KDAEmblem":("Spatula","NeedlesslyLargeRod"),
    "LastWhisper":("RecurveBow","SparringGloves"),
    "Morellonomicon":("GiantsBelt","NeedlesslyLargeRod"),
    "NashorsTooth":("GiantsBelt","RecurveBow"),
    "PentakillEmblem":("Spatula","ChainVest"),
    "ProtectorsVow":("ChainVest","TearoftheGoddess"),
    "PunkEmblem":("Spatula","SparringGloves"),
    "Quicksilver":("NegatronCloak","SparringGloves"),
    "RabadonsDeathcap":("NeedlesslyLargeRod","NeedlesslyLargeRod"),
    "RedBuff":("RecurveBow","RecurveBow"),
    "Redemption":("GiantsBelt","TearoftheGoddess"),
    "RunaansHurricane":("NegatronCloak","RecurveBow"),
    "SpearofShojin":("BFSword","TearoftheGoddess"),
    "StatikkShiv":("RecurveBow","TearoftheGoddess"),
    "SteadfastHeart":("ChainVest","SparringGloves"),
    "SteraksGage":("BFSword","GiantsBelt"),
    "SunfireCape":("ChainVest","GiantsBelt"),
    "TacticiansCrown":("Spatula","Spatula"),
    "ThiefsGloves":("SparringGloves","SparringGloves"),
    "TitansResolve":("ChainVest","RecurveBow"),
    "TrueDamageEmblem":("Spatula","BFSword"),
    "WarmogsArmor":("GiantsBelt","GiantsBelt")
}

# Dictionary of radiant items and their base items
RADIANT_ITEMS_DICT = {
    "Absolution": "Redemption",
    "BlessedBloodthirster": "Bloodthirster",
    "BlueBlessing": "BlueBuff",
    "BrinkofDawn": "EdgeofNight",
    "BulkwarsOath": "ProtectorsVow",
    "CovalentSpark": "IonicSpark",
    "CrestofCinders": "RedBuff",
    "DemonSlayer": "GiantSlayer",
    "DragonsWill": "DragonsClaw",
    "DvarapalaStoneplate": "GargoyleStoneplate",
    "Equinox": "Evenshroud",
    "EternalWhisper": "LastWhisper",
    "FistofFairness": "HandofJustice",
    "GlamorousGauntlet": "JeweledGauntlet",
    "GuinsoosReckoning": "GuinsoosRageblade",
    "HextechLifeblade": "HextechGunblade",
    "JakshotheProtean": "AdaptiveHelm",
    "LeagacyoftheColossus": "SteadyfastHeart",
    "LuminousDeathblade": "Deathblade",
    "MidnightReaper": "NightHarvester",
    "MoreMoreellonomicon": "Morellonomicon",
    "NashorsToothRadiant": "NashorsTooth",
    "Quickestsilver": "Quicksilver",
    "RabadonsAscendedDeathcap": "RabadonsDeathcap",
    "RascalsGloves": "ThiefsGloves",
    "RosethornVest": "BrambleVest",
    "RoyalCrownshield": "Crownguard",
    "RunaansTempest": "RunaansHurricane",
    "SpearofHirana": "SpearofShojin",
    "StatikkFavor": "StatikkShiv",
    "SteraksMegashield": "SteraksGage",
    "StrideBreaker": "Guardbreaker",
    "SunlightCape": "SunfireCape",
    "TitansVow": "TitansResolve",
    "UrfAngelsStaff": "ArchangelsStaff",
    "WarmogsPride": "WarmogsArmor",
    "ZenithEdge": "InfinityEdge",
    }

# List of augment names
AUGMENTS: list[str] = [
    "That's Jazz, Baby!",
    "Three's a Crowd",
    "Bigger Shot",
    "Binary Aidrop",
    "Phreaky Friday",
    "Stationary Support I",
    "Crash Test Dummies",
    "Heroic Presence",
    "Stationary Support III",
    "Bounty Hunters",
    "The Golden Egg",
    "March of Progress",
    "A Cut Above",
    "Cutting Corners",
    "Lucky Gloves+",
    "Endless Hordes",
    "Escort Quest",
    "Stationary Support II",
    "Expose Weakness",
    "Sleight of Hand",
    "Portable Forge",
    "Shopping Spree",
    "Roll The Dice",
    "Pumping Up III",
    "Buried Treasures III",
    "Silver Spoon",
    "Inspiring Epitaph",
    "Emotional Connection",
    "Scrappy Inventions",
    "Impentrable Bulwark",
    "Phreaky Friday+",
    "Iron Assets",
    "Good For Something I",
    "Burried Treasures II",
    "Scape goat",
    "Overwhelming Force",
    "Living Forge",
    "Idealism",
    "Patient Study",
    "Jeweled Lotus III",
    "Blistering Strikes",
    "Cybernetic Bulk I",
    "Cybernetic Bulk III",
    "Vampirism I"
]

# List of portal names
PORTALS: list[str] = [
    "Pot of Gold",
    "Completed Anvil",
    "Component Anvils",
    "Support Anvil",
    "Max Interest",
    "Scuttle Puddle",
    "Tome of Traits"
]
