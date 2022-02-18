PROCESS_NAME = 'League of Legends.exe'

oObjectManager = 0x18670C8
oObjectMapRoot = 0x28
oObjectMapNodeNetId = 0x10
oObjectMapNodeObject = 0x14

OBJECT_SIZE = 0x3400
oObjectAbilityPower = 0x1788
oObjectArmor = 0x12E4
oObjectAtkRange = 0x1304
oObjectAtkSpeedMulti = 0x12B8
oObjectBaseAtk = 0x12BC
oObjectBonusAtk = 0x1234
oObjectHealth = 0xDB4
oObjectMaxHealth = oObjectHealth + 0x10
oObjectLevel = 0x3394
oObjectMagicRes = 0x12EC
oObjectMana = 0x2B4
oObjectPos = 0x23C
oObjectTeam = 0x4C
oObjectTargetable = 0xD1C
oObjectVisibility = 0x28C
oObjectName = 0x2DAC
oObjectNetworkID = 0xCC
oObjectSizeMultiplier = 0x12D4
oObjectSpawnCount = 0x2A0
oObjectSpellBook = 0x27e4
oObjectSpellBookArray = 0x488
oObjectBuffManager = 0x21B8
oObjectBuffManagerEntriesStart = oObjectBuffManager + 0x10
oObjectBuffManagerEntriesEnd = oObjectBuffManager + 0x14

SPELL_SIZE = 0x30
oSpellSlotLevel = 0x20
oSpellSlotCooldownExpire = 0x28

BUFF_SIZE = 0x78
oBuffInfo = 0x8
oBuffCount = 0x74
oBuffEndTime = 0x10
oBuffInfoName = 0x8

oObjectX = oObjectPos
oObjectZ = oObjectPos + 0x4
oObjectY = oObjectPos + 0x8

oLocalPlayer = 0x310473C
oViewProjMatrices = 0x312DDD8
oRenderer = 0x3130C78
oRendererWidth = 0xC
oRendererHeight = 0x10
oGameTime = 0x30FB7CC
