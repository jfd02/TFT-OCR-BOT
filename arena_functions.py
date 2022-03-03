import json
from time import sleep, perf_counter
import numpy as np
import pydirectinput
import requests
from PIL import ImageGrab

import comps
import game_assets
import mk_functions
import ocr
import screen_coords
from champion import Champion
from game_assets import champion_data

client_champion_data = {}


def check_GameStart():
    try:
        allrespones = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', timeout=10, verify=False)
        for events in allrespones.json()['events']['Events']:
            if events['EventName'] == "GameStart":
                return True
        return False
    except Exception:
        return False


def check_GameLoading():
    try:
        allrespones = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', timeout=10, verify=False)
        if allrespones.json()['httpStatus'] == 404:
                return True
        return False
    except Exception:
        return False

def get_champion_data():
    global client_champion_data
    try:
        with open('./champion.json', encoding='utf-8') as f:
            client_champion_data = json.load(f)

    except FileNotFoundError:
        pass
    except json.JSONDecodeError as e:
        print('champion_data 不规范')


def get_level() -> int:
    try:
        allrespones = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', timeout=10, verify=False)
        return int(allrespones.json()['activePlayer']['level'])
    except Exception:
        return 1
    # level = ocr.get_text(screenxy=screen_coords.level_pos, scale=3, psm=7, whitelist="0123456789")
    # try:
    #     level = int(level)
    #     return level
    # except ValueError:
    #     return 1


def get_health() -> int:
    try:
        allrespones = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', timeout=10, verify=False)
        return int(allrespones.json()['activePlayer']['championStats']["currentHealth"])
    except Exception:
        return 100

    #
    # mk_functions.left_click(screen_coords.health_loc)
    # health = ocr.get_text(screenxy=screen_coords.health_pos, scale=3, psm=7, whitelist="0123456789")
    # try:
    #     health = int(health)
    #     return health
    # except ValueError:
    #     return 100


def get_gold() -> int:
    gold = ocr.get_text(screenxy=screen_coords.gold_pos, scale=3, psm=7, whitelist="0123456789")
    try:
        return int(gold)
    except ValueError:
        return 0


def replaceItemKeyName(name):
    return name.replace("Item_Icons/Spatula/", "").replace("Item_Icons/Standard/", "").replace(
        "Item_Icons/Standard_New/", "").replace("Item_Icons/Radiant/", "").replace("Item_Icons/Shadow/", "").replace(
        "ASSETS/Maps/Particles/TFT/", "").replace("ASSETS/Maps/Particles/TFT2/", "").replace(
        "ASSETS/Maps/Particles/TFT3/", "").replace("ASSETS/Maps/Particles/TFT4/", "").replace(
        "ASSETS/Maps/Particles/TFT5/", "").replace("ASSETS/Maps/Particles/TFT6/", "").replace("TFT_Item_Backhand",
                                                                                              "TFT_Item_TrapClaw").replace(
        "TFT_Item_", "").replace("TFT2_Item_", "").replace("TFT3_Item_", "").replace("TFT4_Item_", "").replace(
        "TFT5_Item_", "").replace("TFT6_Item_", "").replace("TFT_Set4", "").replace("TFT_Set5", "").replace("TFT_Set6",
                                                                                                            "").replace(
        "Icon_", "").replace(".dds", "").replace("Shroud", "ShroudofStillness").replace("MortalReminder",
                                                                                        "Last Whisper").replace(
        "Mercurial", "Quicksilver").replace("Jeweled_Guantlet", "Jeweled_Gauntlet").replace("Gaints_Belt", "Giants_Belt").replace("_", "").replace(".", "").replace("ThievesGloves", "ThiefsGloves")


def get_shop() -> list:
    shop = []
    try:
        with open('./live_data/store.txt', encoding='utf-8') as f:
            shop_dict = json.load(f)
            # print(json.dumps(shop_dict))

            s = json.loads(shop_dict["store"]["shop_pieces"])
            for slot in s:
                name_tmp = s[slot]["name"]
                champ = client_champion_data["data"][name_tmp.replace("TFT6_", "").lower().replace("tft6b_", "")][
                    "name"] if name_tmp != "Sold" else name_tmp
                if champ in game_assets.champions:
                    shop.append(champ)
                else:
                    shop.append("")
    except FileNotFoundError:
        pass
    except json.JSONDecodeError as e:
        print('shop_dict 不规范')
    except Exception as p:
        print(f'get_shop {p}')

    return shop


def get_bench() -> list:
    _bench = [None, None, None, None, None, None, None, None, None]
    try:
        with open('./live_data/bench.txt', encoding='utf-8') as f:
            bench_dict = json.load(f)
            # print(json.dumps(bench_dict))

            s = json.loads(bench_dict["bench"]["bench_pieces"])

            _solt = []
            _name = []
            _level = []

            for slot in s:
                _solt.append(int(slot.replace("slot_", "")))
                _name.append(s[slot]["name"])
                _level.append((int(s[slot]["level"])))

            for i in range(1, 10):
                if i in _solt:
                    if _name[_solt.index(i)] == "TFT5_EmblemArmoryKey":
                        mk_functions.press_e(screen_coords.bench_loc[_solt.index(i)])
                        sleep(1)
                        mk_functions.left_click(screen_coords.buy_loc[2])
                        continue
                    champ = client_champion_data["data"][_name[_solt.index(i)].replace("TFT6_", "").lower().replace("tft6b_", "")]["name"]
                    if champ in game_assets.champions:
                        items = []
                        if champ in comps.comp:
                            for item in comps.comp[champ]["items"]:
                                items.append(item)
                        _bench[i - 1] = Champion(champ, screen_coords.bench_loc[i - 1], items, i - 1,
                                                 champion_data[champ]["Board Size"],
                                                 comps.comp[champ]["final_comp"] if champ in comps.comp else False, None,None,_level[_solt.index(i)])
                    else:
                        _bench[i - 1] = None
                else:
                    _bench[i - 1] = None

    except FileNotFoundError:
        pass
    except json.JSONDecodeError as e:
        print('get_bench 不规范')
    except Exception as p:
        print(f'get_bench {p}')

    return _bench


def get_board() -> dict:
    board = []
    board_useless = []
    board_size = 0
    try:
        with open('./live_data/board.txt', encoding='utf-8') as f:
            board_dict = json.load(f)
            # print(json.dumps(board_dict))

            s = json.loads(board_dict["board"]["board_pieces"])

            _solt = []
            _name = []
            _level = []
            _item = []

            for slot in s:
                name_tmp = s[slot]["name"].replace("TFT6_", "").lower().replace("tft6b_", "")
                if name_tmp not in client_champion_data["data"]:
                    continue
                _name.append(name_tmp)
                _solt.append(int(slot.replace("cell_", "")))
                _level.append((int(s[slot]["level"])))

                if s[slot]["item_1"] != "":
                    _item_name = replaceItemKeyName(s[slot]["item_1"])
                    if _item_name in game_assets.items:
                        _item.append(_item_name)
                    else:
                        print(f"[!] get_board: unknow item1: {_item_name}")
                if s[slot]["item_2"] != "":
                    _item_name = replaceItemKeyName(s[slot]["item_2"])
                    if _item_name in game_assets.items:
                        _item.append(_item_name)
                    else:
                        print(f"[!] get_board: unknow item2: {_item_name}")
                if s[slot]["item_3"] != "":
                    _item_name = replaceItemKeyName(s[slot]["item_3"])
                    if _item_name in game_assets.items:
                        _item.append(_item_name)
                    else:
                        print(f"[!] get_board: unknow item3: {_item_name}")


            for i in range(1, 29):
                if i in _solt:
                    champ = client_champion_data["data"][_name[_solt.index(i)]]["name"]
                    if champ in game_assets.champions:
                        items = [] # 阵容设置装备
                        if champ in comps.comp:
                            for item in comps.comp[champ]["items"]:
                                items.append(item)

                            completed_items = []
                            current_building = []
                            for item in _item: # 遍历已有装备
                                if item in game_assets.full_items: # 是成装
                                    if item in items:
                                        completed_items.append(item)
                                        items.remove(item)
                                else:
                                    for build_item in items:
                                        build_item_components = list(game_assets.full_items[build_item])
                                        if item in build_item_components:
                                            build_item_components.remove(item)
                                            current_building.append((build_item, build_item_components[0]))
                                            items.remove(build_item)

                            board.append(Champion(champ, screen_coords.board_loc[i - 1], items, i - 1,
                                                  champion_data[champ]["Board Size"],
                                                  comps.comp[champ]["final_comp"] if champ in comps.comp else False,
                                                  completed_items, current_building, _level[_solt.index(i)]))
                        else:
                            board_useless.append(champ)

                        board_size += champion_data[champ]["Board Size"]

    except FileNotFoundError:
        pass
    except json.JSONDecodeError as e:
        print('shop_dict 不规范')
    except Exception as p:
        print(f'get_board {p}')


    return {"board": board,
            "board_useless": board_useless,
            "board_size": board_size}

    # screen_capture = ImageGrab.grab(bbox=screen_coords.shop_pos)
    # shop = []
    # for names in screen_coords.champ_name_pos:
    #     champ = screen_capture.crop(names)
    #     champ = ocr.get_text_image(image=champ, whitelist="")
    #     if champ in game_assets.champions:
    #         shop.append(champ)
    #     else:
    #         shop.append("")
    # return shop


def empty_slot() -> int:
    for slot, positions in enumerate(screen_coords.bench_health_pos):
        screen_capture = ImageGrab.grab(bbox=positions)
        screenshot_array = np.array(screen_capture)
        if not (np.abs(screenshot_array - (0, 255, 18)) <= 3).all(axis=2).any():
            return slot  # Slot 0-8
    return -1  # No empty slot


# def bench_occupied_check() -> list:
#     bench_occupied = []
#     for positions in screen_coords.bench_health_pos:
#         screen_capture = ImageGrab.grab(bbox=positions)
#         screenshot_array = np.array(screen_capture)
#         if not (np.abs(screenshot_array - (0, 255, 18)) <= 2).all(axis=2).any():
#             bench_occupied.append(False)
#         else:
#             bench_occupied.append(True)
#     return bench_occupied


def valid_item(item):
    for valid_item_name in game_assets.items:
        if valid_item_name in item:
            return valid_item_name
    return None


def get_items() -> list:
    item_bench = []
    for positions in screen_coords.item_pos:
        pydirectinput.moveTo(positions[0][0], positions[0][1])
        item = ocr.get_text(screenxy=positions[1], scale=3, psm=13,
                            whitelist="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
        item_bench.append(valid_item(item))
    mk_functions.move_mouse(screen_coords.default_loc)
    return item_bench
