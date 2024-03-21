"""
Contains static item & champion data
"""

BASIC_ITEM: set[str] = {"BFSword","ChainVest","GiantsBelt","NeedlesslyLargeRod",
                            "NegatronCloak","RecurveBow","SparringGloves","Spatula",
                            "TearoftheGoddess"}

COMBINED_ITEMS: set[str] = {"DryadEmblem","FatedEmblem","GhostlyEmblem","HeavenlyEmblem",
                            "MythicEmblem","PorcelainEmblem","StoryweaverEmblem","UmbralEmblem",
                            "AdaptiveHelm","ArchangelsStaff","Bloodthirster","BlueBuff",
                            "BrambleVest","Crownguard","Deathblade","DragonsClaw",
                            "EdgeofNight","Evenshroud","GargoyleStoneplate","GiantSlayer",
                            "Guardbreaker","GuinsoosRageblade","HandofJustice","HextechGunblade",
                            "InfinityEdge","IonicSpark","JeweledGauntlet","LastWhisper",
                            "Morellonomicon","NashorsTooth","ProtectorsVow","Quicksilver",
                            "RabadonsDeathcap","RedBuff","Redemption","RunaansHurricane",
                            "SpearofShojin","StatikkShiv","SteadfastHeart","SteraksGage",
                            "SunfireCape","TacticiansCrown","ThiefsGloves","TitansResolve",
                            "WarmogsArmor"}

SUPPORT_ITEM: set[str] = {"AccomplicesGloves","AegisoftheLegion","BansheesVeil","ChaliceofPower",
                            "CrestofCinders","LocketoftheIronSolari","NeedlesslyBigGem","ObsidianCleaver",
                            "RanduinsOmen","ShroudofStillness","VirtueoftheMartyr","ZekesHerald",
                            "Zephyr","ZzRotPortal"}

NON_CRAFTABLE_ITEMS: set[str] = {"AltruistEmblem","ArcanistEmblem","BehemothEmblem","BruiserEmblem",
                                    "DragonlordEmblem","DuelistEmblem","Exaltedemblem","FortuneEmblem",
                                    "InkshadowEmblem","InvokerEmblem","ReaperEmblem","SageEmblem",
                                    "ScrollofForce","ScrollofHaste","SniperEmblem","TalismanofAid",
                                    "TalismanofMight","TalismanofSpeed","TattooofBombardement","TattooofForce",
                                    "TattooofFury","TattooofProtection","TattooofToxin","TattooofVitality",
                                    "TomeofMending","TomeofPower","TomeofSwiftness","Wardenemblem"}

ORNN_ITEMS: set[str] = {"AnimaVisage","BlacksmithsGloves","DeathfireGrasp","DeathsDefiance",
                        "DiamondHands","EternalWinter","GamblersBlade","GoldCollector",
                        "GoldmancersStaff","Hullcrusher","InfinityForce","Manazane",
                        "MogulsMail","Rocket-PropelledFist","SnipersFocus","TrickstersGlass",
                        "ZhonyasParadox"}

ITEMS: set[str] = BASIC_ITEM.union(COMBINED_ITEMS).union(SUPPORT_ITEM).union(NON_CRAFTABLE_ITEMS).union(ORNN_ITEMS)

CHAMPIONS: dict[str, dict[str, int]] = {
    "Aatrox":{"Gold":2,"Board Size":1,"Trait1":"Bruiser","Trait2":"Ghostly","Trait3":"Inkshadow"},
    "Ahri":{"Gold":1,"Board Size":1,"Trait1":"Arcanist","Trait2":"Fated","Trait3":""},
    "Alune":{"Gold":3,"Board Size":1,"Trait1":"Invoker","Trait2":"Umbral","Trait3":""},
    "Amumu":{"Gold":3,"Board Size":1,"Trait1":"Warden","Trait2":"Porcelain","Trait3":""},
    "Annie":{"Gold":4,"Board Size":1,"Trait1":"Invoker","Trait2":"Fortune","Trait3":""},
    "Aphelios":{"Gold":3,"Board Size":1,"Trait1":"Sniper","Trait2":"Fated","Trait3":""},
    "Ashe":{"Gold":4,"Board Size":1,"Trait1":"Sniper","Trait2":"Porcelain","Trait3":""},
    "Azir":{"Gold":5,"Board Size":1,"Trait1":"Invoker","Trait2":"Dryad","Trait3":""},
    "Bard":{"Gold":3,"Board Size":1,"Trait1":"Trickshot","Trait2":"Mythic","Trait3":""},
    "Caitlyn":{"Gold":1,"Board Size":1,"Trait1":"Sniper","Trait2":"Ghostly","Trait3":""},
    "ChoGath":{"Gold":1,"Board Size":1,"Trait1":"Behemoth","Trait2":"Mythic","Trait3":""},
    "Darius":{"Gold":1,"Board Size":1,"Trait1":"Duelist","Trait2":"Umbral","Trait3":""},
    "Diana":{"Gold":3,"Board Size":1,"Trait1":"Sage","Trait2":"Dragonlord","Trait3":""},
    "Galio":{"Gold":4,"Board Size":1,"Trait1":"Bruiser","Trait2":"Storyweaver","Trait3":""},
    "Garen":{"Gold":1,"Board Size":1,"Trait1":"Warden","Trait2":"Storyweaver","Trait3":""},
    "Gnar":{"Gold":2,"Board Size":1,"Trait1":"Warden","Trait2":"Dryad","Trait3":""},
    "Hwei":{"Gold":5,"Board Size":1,"Trait1":"Artist","Trait2":"Mythic","Trait3":""},
    "Illaoi":{"Gold":3,"Board Size":1,"Trait1":"Arcanist","Trait2":"Warden","Trait3":"Ghostly"},
    "Irelia":{"Gold":5,"Board Size":1,"Trait1":"Duelist","Trait2":"Storyweaver","Trait3":""},
    "Janna":{"Gold":2,"Board Size":1,"Trait1":"Invoker","Trait2":"Dragonlord","Trait3":""},
    "Jax":{"Gold":1,"Board Size":1,"Trait1":"Warden","Trait2":"Inkshadow","Trait3":""},
    "KaiSa":{"Gold":4,"Board Size":1,"Trait1":"Trickshot","Trait2":"Inkshadow","Trait3":""},
    "Kayn":{"Gold":4,"Board Size":1,"Trait1":"Reaper","Trait2":"Ghostly","Trait3":""},
    "KhaZix":{"Gold":1,"Board Size":1,"Trait1":"Reaper","Trait2":"Heavenly","Trait3":""},
    "Kindred":{"Gold":2,"Board Size":1,"Trait1":"Reaper","Trait2":"Fated","Trait3":"Dryad"},
    "Kobuko":{"Gold":1,"Board Size":1,"Trait1":"Bruiser","Trait2":"Fortune","Trait3":""},
    "KogMaw":{"Gold":1,"Board Size":1,"Trait1":"Sniper","Trait2":"Invoker","Trait3":"Mythic"},
    "LeeSin":{"Gold":4,"Board Size":1,"Trait1":"Duelist","Trait2":"Dragonlord","Trait3":""},
    "Lillia":{"Gold":4,"Board Size":1,"Trait1":"Invoker","Trait2":"Mythic","Trait3":""},
    "Lissandra":{"Gold":5,"Board Size":1,"Trait1":"Arcanist","Trait2":"Porcelain","Trait3":""},
    "Lux":{"Gold":2,"Board Size":1,"Trait1":"Arcanist","Trait2":"Porcelain","Trait3":""},
    "Malphite":{"Gold":1,"Board Size":1,"Trait1":"Behemoth","Trait2":"Heavenly","Trait3":""},
    "Morgana":{"Gold":4,"Board Size":1,"Trait1":"Sage","Trait2":"Ghostly","Trait3":""},
    "Nautilus":{"Gold":4,"Board Size":1,"Trait1":"Warden","Trait2":"Mythic","Trait3":""},
    "Neeko":{"Gold":2,"Board Size":1,"Trait1":"Arcanist","Trait2":"Heavenly","Trait3":"Mythic"},
    "Ornn":{"Gold":4,"Board Size":1,"Trait1":"Behemoth","Trait2":"Dryad","Trait3":""},
    "Qiyana":{"Gold":2,"Board Size":1,"Trait1":"Duelist","Trait2":"Heavenly","Trait3":""},
    "Rakan":{"Gold":5,"Board Size":1,"Trait1":"Altruist","Trait2":"Lovers","Trait3":"Dragonlord"},
    "RekSai":{"Gold":1,"Board Size":1,"Trait1":"Bruiser","Trait2":"Dryad","Trait3":""},
    "Riven":{"Gold":2,"Board Size":1,"Trait1":"Bruiser","Trait2":"Altruist","Trait3":"Storyweaver"},
    "Senna":{"Gold":2,"Board Size":1,"Trait1":"Sniper","Trait2":"Inkshadow","Trait3":""},
    "Sett":{"Gold":5,"Board Size":1,"Trait1":"Warden","Trait2":"Umbral","Trait3":"Fated"},
    "Shen":{"Gold":2,"Board Size":1,"Trait1":"Behemoth","Trait2":"Ghostly","Trait3":""},
    "Sivir":{"Gold":1,"Board Size":1,"Trait1":"Trickshot","Trait2":"Storyweaver","Trait3":""},
    "Soraka":{"Gold":3,"Board Size":1,"Trait1":"Altruist","Trait2":"Heavenly","Trait3":""},
    "Sylas":{"Gold":4,"Board Size":1,"Trait1":"Bruiser","Trait2":"Umbral","Trait3":""},
    "Syndra":{"Gold":4,"Board Size":1,"Trait1":"Arcanist","Trait2":"Fated","Trait3":""},
    "TahmKench":{"Gold":3,"Board Size":1,"Trait1":"Bruiser","Trait2":"Mythic","Trait3":""},
    "Teemo":{"Gold":2,"Board Size":1,"Trait1":"Trickshot","Trait2":"Fortune","Trait3":""},
    "Thresh":{"Gold":3,"Board Size":1,"Trait1":"Behemoth","Trait2":"Fated","Trait3":""},
    "Tristana":{"Gold":3,"Board Size":1,"Trait1":"Duelist","Trait2":"Fortune","Trait3":""},
    "Udyr":{"Gold":5,"Board Size":1,"Trait1":"Behemoth","Trait2":"SpiritWalker","Trait3":"Inkshadow"},
    "Volibear":{"Gold":3,"Board Size":1,"Trait1":"Duelist","Trait2":"Inkshadow","Trait3":""},
    "Wukong":{"Gold":5,"Board Size":1,"Trait1":"Sage","Trait2":"Great","Trait3":"Heavenly"},
    "Xayah":{"Gold":5,"Board Size":1,"Trait1":"Trickshot","Trait2":"Lovers","Trait3":"Dragonlord"},
    "Yasuo":{"Gold":1,"Board Size":1,"Trait1":"Duelist","Trait2":"Fated","Trait3":""},
    "Yone":{"Gold":3,"Board Size":1,"Trait1":"Reaper","Trait2":"Umbral","Trait3":""},
    "Yorick":{"Gold":2,"Board Size":1,"Trait1":"Behemoth","Trait2":"Umbral","Trait3":""},
    "Zoe":{"Gold":3,"Board Size":1,"Trait1":"Arcanist","Trait2":"Fortune","Trait3":"Storyweaver"},
    "Zyra":{"Gold":2,"Board Size":1,"Trait1":"Sage","Trait2":"Storyweaver","Trait3":""}
}


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
