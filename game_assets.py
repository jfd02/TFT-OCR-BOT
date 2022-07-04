"""
Contains static item & champion data
"""

combined_items = {"BFSword", "ChainVest", "GiantsBelt", "NeedlesslyLargeRod", "NegatronCloak",
                  "SparringGloves", "Spatula", "TearoftheGoddess", "ArchangelsStaff", "AssassinEmblem",
                  "BansheesClaw", "Bloodthirster", "BlueBuff", "BrambleVest", "CavalierEmblem", "ChaliceofPower",
                  "Deathblade","DragonmancerEmblem","DragonsClaw","EdgeofNight","FrozenHeart","GargoyleStoneplate","GiantSlayer",
                  "HandofJustice", "HextechGunblade","InfinityEdge","IonicSpark","JewledGauntlet","LastWhisper","LocketoftheIronSolari", "MageEmblem", "MirageEmblem",
                  "Morellonomicon", "Quicksilver","RabadonsDeathcap","Ragewing Emblem", "RapidFirecannon","Redemption","RunaansHurricane","ShimmerscaleEmblem",
                  "ShroudofStillness", "SpearofShojin","StatikkShiv","SunfireCape","TacticiansCrown","ThiefsGloves","TitansResolve","WarmogsArmor",
                  "ZekesHerald","Zephyr","ZZRotPortal", "RecurveBow", "GuardianEmblem", "GuinsoosRageblade"}

elusive_items ={"AstralEmblem", "BruiserEmblem", "Cannoneer Emblem", "DragonmancersBlessing", "EvokerEmblem", "GuildEmblem",
                "JadeEmblem", "LegendEmblem", "MysticEmblem", "RevelEmblem", "ScalescornEmblem", "SwiftshotEmblem",
                "TempestEmblem", "WarriorEmblem", "WhispersEmblem"}

shimmerscale_items = {"CrownOfChampions", "DeterminedInvestor", "DiamondHands", "DravensAxe", "GamblersBlade",
                      "GoldmancersStaff", "MogulsMail", "NeedlesslyBigGem", "PhilosophersStone"}

ornn_items = {"AnimaVisage","DeathsDefiance","EternalWinter","GoldCollector","InfinityForce",
              "Manazane", "ObsidianCleaver","RaduinsSanctum","RocketPropelledFist","ZhonyasParadox"}

radiant_items = { "Absolution", "BansheesSilence","BlessedBloodthirster","BlueBlessing",
                  "BrinkofDawn","ChaliceofCharity","CovalentSpark","DemonSlayer","DragonsWill",
                  "DvarapalaStoneplate", "EternalWhisper", "FistofFairness","FrozenHeartOfGold",
                  "GlamorousGauntlet","GuinsoosReckoning","HextechLifeblade",
                  "LocketofTargonPrime","LuminousDeathblade","Mistral","MoreMoreellonomicon",
                  "Quickestsilver","RabadonsAscendedDeathcap","RadiantRedemption","RapidLightcannon",
                  "RascalsGloves","RosethornVest","RunaansTempest","ShroudofReverance",
                  "SpearofHirana","StatikkFavor","SunlightCape","TitansVow",
                  "UrfAngelsStaff","WarmogsPride", "ZekesHarmony", "ZenithEdge",
                  "ZzRotsInvitation"}

items = combined_items.union(elusive_items).union(shimmerscale_items).union(ornn_items).union(radiant_items)

champions = {'Aatrox', 'Anivia', 'Ao Shin', 'Ashe', 'Aurelion Sol', 'Bard', 'Braum', 'Corki', 'Daeja', 'Diana', 'Elise', 'Ezreal', 'Gnar',
             'Hecarim', 'Heimerdinger', 'Idas', 'Illaoi', 'Jinx', 'Karma', 'Kayn', 'Lee sin', 'Leona', 'Lillia', 'Lulu', 'Nami', 'Neeko',
             'Nidalee', 'Nunu', 'Olaf', 'Ornn', 'Pyke', 'Qiyana', 'Ryze', 'Sejuani', 'Senna', 'Sett', 'Shen', 'Shi Oh Yu', 'Shyvana', 'Skarner',
             'Sona', 'Soraka', 'Swain', 'Syfen', 'Sylas', 'Tahm Kench', 'Talon', 'Taric', 'Thresh', 'Tristana', 'Twitch', 'Varus', 'Vladmir',
             'Volibear', 'Xayah', 'Yasuo', 'Yone', 'Zoe'}

champion_data = {
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

rounds = {"1-1", "1-2", "1-3", "1-4",
          "2-1", "2-2", "2-3", "2-4", "2-5", "2-6", "2-7",
          "3-1", "3-2", "3-3", "3-4", "3-5", "3-6", "3-7",
          "4-1", "4-2", "4-3", "4-4", "4-5", "4-6", "4-7",
          "5-1", "5-2", "5-3", "5-4", "5-5", "5-6", "5-7",
          "6-1", "6-2", "6-3", "6-4", "6-5", "6-6", "6-7",
          "7-1", "7-2", "7-3", "7-4", "7-5", "7-6", "7-7"}

carousel_rounds = {"1-1", "2-4", "3-4", "4-4", "5-4", "6-4", "7-4"}

pve_round = {"1-2", "1-3", "1-4", "2-7", "3-7", "4-7", "5-7", "6-7", "7-7"}

pvp_round = {"2-1", "2-2", "2-3", "2-5", "2-6",
             "3-1", "3-2", "3-3", "3-5", "3-6",
             "4-1", "4-2", "4-3", "4-5", "4-6",
             "5-1", "5-2", "5-3", "5-5", "5-6",
             "6-1", "6-2", "6-3", "6-5", "6-6",
             "7-1", "7-2", "7-3", "7-5", "7-6"}

pickup_round = {"2-1", "3-1", "4-1", "5-1", "6-1", "7-1"}

augment_rounds = {"1-4", "3-3", "4-6"}

item_placement_rounds = {"2-2", "3-2", "4-2", "5-2", "6-2", "7-2", "2-5", "3-5", "4-5", "5-5", "6-5", "7-5"}

final_comp_round = "4-5"

full_items = {"ArchangelsStaff": ("NeedlesslyLargeRod", "TearoftheGoddess"),
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
