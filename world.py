import constants
import numpy as np
from pymem.exception import MemoryReadError
from collections import namedtuple, defaultdict
from utils import bool_from_buffer, double_from_buffer, float_from_buffer, int_from_buffer, linked_insert, Node

# Object = namedtuple('Object', 'name, ability_power, armor, attack_range, attack_speed_multiplier, base_attack, bonus_attack, health, network_id, magic_resist, mana, max_health, size_multiplier, x, y, z, level, team, spawn_count, targetable, visibility, spells, buffs')
Object = namedtuple('Object', 'name, x, y, z, spawn_count, visibility')
Spells = namedtuple('Spells', 'Q, W, E, R, D, F')
Spell = namedtuple('Spell', 'level, cooldown_expire')
Buff = namedtuple('Buff', 'name, count, end_time')


def get_str(mem, address):
    data = mem.read_bytes(address, constants.BUFF_SIZE)
    if int_from_buffer(data, 0x10) > 15:
        name = mem.read_string(int_from_buffer(data, 0), 50)
    else:
        name = mem.read_string(address, 50)
    return name

def read_buff(mem, address):
    if not address:
        return None
    data = mem.read_bytes(address, constants.BUFF_SIZE)
    info = int_from_buffer(data, constants.oBuffInfo)
    if not info:
        return None
    name = mem.read_string(info + constants.oBuffInfoName, 255)
    count = int_from_buffer(data, constants.oBuffCount)
    end_time = float_from_buffer(data, constants.oBuffEndTime)
    return Buff(name, count, end_time)


def read_buffs(mem, begin_address, end_address):
    buffs = defaultdict(lambda: [])
    if not begin_address:
        return buffs

    current_address = begin_address
    while current_address != end_address:
        buff_pointer = mem.read_int(current_address)
        buff = read_buff(mem, buff_pointer)
        if buff:
            buffs[buff.name].append(buff)
        current_address += 0x8
    return buffs


def read_spell(mem, spell_address):
    data = mem.read_bytes(spell_address, constants.SPELL_SIZE)
    level = int_from_buffer(data, constants.oSpellSlotLevel)
    cooldown_expire = double_from_buffer(data, constants.oSpellSlotCooldownExpire)
    return Spell(level, cooldown_expire)


def read_spells(mem, spell_addresses_pointer):
    number_of_spells = len(Spells._fields)
    data = mem.read_bytes(spell_addresses_pointer + constants.oObjectSpellBookArray, number_of_spells * 4)
    spell_addresses = [int_from_buffer(data, n * 4) for n in range(number_of_spells)]
    spells = [read_spell(mem, spell_address) for spell_address in spell_addresses]
    params = {Spells._fields[n]: spell for n, spell in enumerate(spells)}
    return Spells(**params)


def read_object(mem, address):
    data = mem.read_bytes(address, constants.OBJECT_SIZE)

    params = {}
    params['name'] = get_str(mem, address + constants.oObjectName)
    # params['ability_power'] = float_from_buffer(data, constants.oObjectAbilityPower)
    # params['armor'] = float_from_buffer(data, constants.oObjectArmor)
    # params['attack_range'] = float_from_buffer(data, constants.oObjectAtkRange)
    # params['attack_speed_multiplier'] = float_from_buffer(data, constants.oObjectAtkSpeedMulti)
    # params['base_attack'] = float_from_buffer(data, constants.oObjectBaseAtk)
    # params['bonus_attack'] = float_from_buffer(data, constants.oObjectBonusAtk)
    # params['magic_resist'] = float_from_buffer(data, constants.oObjectMagicRes)
    # params['mana'] = float_from_buffer(data, constants.oObjectMana)
    # params['health'] = float_from_buffer(data, constants.oObjectHealth)
    # params['max_health'] = float_from_buffer(data, constants.oObjectMaxHealth)
    # params['size_multiplier'] = float_from_buffer(data, constants.oObjectSizeMultiplier)
    params['x'] = float_from_buffer(data, constants.oObjectX)
    params['y'] = float_from_buffer(data, constants.oObjectY)
    params['z'] = float_from_buffer(data, constants.oObjectZ)

    # params['network_id'] = int_from_buffer(data, constants.oObjectNetworkID)
    # params['level'] = int_from_buffer(data, constants.oObjectLevel)
    # params['team'] = int_from_buffer(data, constants.oObjectTeam)
    params['spawn_count'] = int_from_buffer(data, constants.oObjectSpawnCount)
    #
    # params['targetable'] = bool_from_buffer(data, constants.oObjectTargetable)
    params['visibility'] = bool_from_buffer(data, constants.oObjectVisibility)
    #
    # spell_pointers_address = int_from_buffer(data, constants.oObjectSpellBook)
    # params['spells'] = read_spells(mem, spell_pointers_address)
    #
    # buffs_start = int_from_buffer(data, constants.oObjectBuffManagerEntriesStart)
    # buffs_end = int_from_buffer(data, constants.oObjectBuffManagerEntriesEnd)
    #
    # params['buffs'] = read_buffs(mem, buffs_start, buffs_end)

    return Object(**params)


def find_object_pointers(mem, max_count=800):
    # Given a memory interface will iterate through objects in memory
    # returns object addresses
    object_pointers = mem.read_uint(mem.base_address + constants.oObjectManager)
    root_node = Node(mem.read_uint(object_pointers + constants.oObjectMapRoot), None)
    addresses_seen = set()
    current_node = root_node
    pointers = set()
    count = 0
    while current_node is not None and count < max_count:
        if current_node.address in addresses_seen:
            current_node = current_node.next
            continue
        addresses_seen.add(current_node.address)
        try:
            data = mem.read_bytes(current_node.address, 0x18)
            count += 1
        except MemoryReadError:
            pass
        else:
            for i in range(3):
                child_address = int_from_buffer(data, i * 4)
                if child_address in addresses_seen:
                    continue
                linked_insert(current_node, child_address)
            net_id = int_from_buffer(data, constants.oObjectMapNodeNetId)
            if net_id - 0x40000000 <= 0x100000:
            #     # help reduce redundant objects
                pointers.add(int_from_buffer(data, constants.oObjectMapNodeObject))

        current_node = current_node.next
    # print(pointers)
    # for p in pointers:
    #     try:
    #         name = mem.read_string(p + constants.oObjectName, 50)
    #
    #         print('{:08X}  {},'.format(p, name))
    #     except:
    #         pass
    return pointers


def find_pointers(mem, names):
    pointers = find_object_pointers(mem)
    # print(pointers)
    find_pointers = set()
    for pointer in pointers:
        try:
            o = read_object(mem, pointer)
            # data = mem.read_bytes(pointer, constants.OBJECT_SIZE)
            # name = get_str(mem, pointer + constants.oObjectName)
            # # if int_from_buffer(data, constants.oObjectName + 0x10) > 15:
            # #     name=mem.read_string(int_from_buffer(data, constants.oObjectName), 50)
            # # else:
            # #     name = mem.read_string(pointer + constants.oObjectName, 50)
            if o.name.lower() in names:
                # print(o.name)
                find_pointers.add(pointer)
        except (MemoryReadError, UnicodeDecodeError):
            pass
        else:
            if o.name.lower() in names:
                find_pointers.add(pointer)
    return find_pointers


def find_local_net_id(mem):
    local_player = mem.read_uint(mem.base_address + constants.oLocalPlayer)
    return mem.read_int(local_player + constants.oObjectNetworkID)


def find_game_time(mem):
    return mem.read_float(mem.base_address + constants.oGameTime)


def list_to_matrix(floats):
    m = np.array(floats)
    return m.reshape(4, 4)


def find_view_proj_matrix(mem):
    data0 = mem.read_bytes(mem.base_address + constants.oRenderer, 0x4)
    data = mem.read_bytes(int_from_buffer(data0, 0x0), constants.oRendererHeight + 0x4)
    width = int_from_buffer(data, constants.oRendererWidth)
    height = int_from_buffer(data, constants.oRendererHeight)

    data = mem.read_bytes(mem.base_address + constants.oViewProjMatrices, 128)
    view_matrix = list_to_matrix([float_from_buffer(data, i * 4) for i in range(16)])
    proj_matrix = list_to_matrix([float_from_buffer(data, 64 + (i * 4)) for i in range(16)])
    view_proj_matrix = np.matmul(view_matrix, proj_matrix)
    return view_proj_matrix.reshape(16), width, height


def world_to_screen(view_proj_matrix, width, height, x, y, z):
    # pasted / translated world to screen math
    clip_coords_x = x * view_proj_matrix[0] + y * view_proj_matrix[4] + z * view_proj_matrix[8] + view_proj_matrix[12]
    clip_coords_y = x * view_proj_matrix[1] + y * view_proj_matrix[5] + z * view_proj_matrix[9] + view_proj_matrix[13]
    clip_coords_w = x * view_proj_matrix[3] + y * view_proj_matrix[7] + z * view_proj_matrix[11] + view_proj_matrix[15]

    if clip_coords_w < 1.:
        clip_coords_w = 1.

    M_x = clip_coords_x / clip_coords_w
    M_y = clip_coords_y / clip_coords_w

    out_x = (width / 2. * M_x) + (M_x + width / 2.)
    out_y = -(height / 2. * M_y) + (M_y + height / 2.)

    if 0 <= out_x <= width and 0 <= out_y <= height:
        return out_x, out_y

    return None, None
