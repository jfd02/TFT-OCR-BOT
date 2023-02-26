"""
Auto comps loader WompWomp99 (with autocache)
Champion names are different in lolchess/communitydragon/tftactics
Some champion names is repeating because of different patches (but it's the same champion), for example Nomsy
In-game champion names only in communitydragon
"""

import game_assets
import json
import requests
from difflib import SequenceMatcher
import os
from comps import CompsManager

LOLCHESS_CHAMPIONS_URL = 'https://lolchess.gg/champions/'
LOLCHESS_META_COMPS_URL = 'https://lolchess.gg/meta'
DRAGON_URL = 'https://raw.communitydragon.org/latest/cdragon/tft/en_us.json'

HARD_OVERRIDE_LIST = {'TFT7_Wukong': 'Wukong'}
SOFT_OVERRIDE_LIST = {'nomsycannoneerforbuilder': ('nomsy', 'Nomsy'),
                      'nomsyevokerforbuilder': ('nomsy', 'Nomsy'),
                      'nomsymageforbuilder': ('nomsy', 'Nomsy')}
ITEMS_OVERRIDE_LIST = {'CrownofChampions': 'CrownOfChampions'}
FINAL_CHAMP_NAMES_LIST = {'Nunu': 'Nunu & Willump'}
LOLCHESS_BOARD_ARRANGE = [21, 22, 23, 24, 25, 26, 27, 14, 15, 16, 17, 18, 19, 20, 7, 8, 9, 10, 11, 12, 13, 0, 1, 2, 3, 4, 5, 6]
JSON_TO_FIX = ["isReadOnly", "isChallengerComment", "currentSet", "isWithGuide", "isWithYoutuber", "setKey",
               "isLolchessggApp", "isDakggMobileApp",
               "championStats", "championClasses", "championOrigins", "items", "fromItems", "deck", "deckUuid",
               "deckMetaItems", "extraData"]


def Parse(input, fromwhere, to, startindex=0):
    index_from = input.find(fromwhere, startindex)
    if index_from != -1:
        index_to = input.find(to, index_from + 1)
        if index_to != -1:
            return (int(index_from), input[index_from + len(fromwhere):index_to])
    return (-1, None)


def ParseMultiple(input, fromwhere, to):
    output = []
    index = 0
    while index != -1:
        current = Parse(input, fromwhere, to, index)
        index = current[0]
        if index != -1:
            output.append(current)
            index += len(fromwhere)
    return output


# def __LoadLolChessCurrentSetVersion(input_str):
#     return Parse(input_str, 'lolchess.gg/champions/set', '"')[1]

def __LoadLoLChessPrices():
    lolchess_url = LOLCHESS_CHAMPIONS_URL  # + set_input+ '/'
    response = requests.get(lolchess_url)
    current_tft_set = response.url.split('/')[4][3:]

    json_in_text = Parse(response.text, 'window.guideChampion = {\n            champions: ', r'}}],')[1] + r'}}]'
    json_parsed = json.loads(json_in_text)

    output_dictionary = {}
    for each_character in json_parsed:
        character_code = each_character['code']
        character_name_ingame = each_character['ingame_code']
        character_price = int(each_character['cost'])
        if character_name_ingame not in output_dictionary:
            output_dictionary[character_name_ingame] = (character_price, character_code)
    return [current_tft_set, output_dictionary]


def __FixJson(input: str):
    for each_json in JSON_TO_FIX:
        input = input.replace(each_json + ':', '"' + each_json + '":')
    return input


def __LoadLolChessComps(input_str, set_str, comps_manager: CompsManager):
    output_comps: dict = {}
    url_start_string = "https://lolchess.gg/builder/set" + set_str + "?deck="
    parsed_links = ParseMultiple(input_str, url_start_string, '"')
    champions_keys: dict = {}
    items: dict = {}
    comps_name: dict(str) = {}
    for each_link in parsed_links:
        is_good_comp = True
        response_each_link = requests.get(url_start_string + each_link[1])
        json_in_text = Parse(response_each_link.text, "      window.simulator = ", "              }")
        text_proceed = __FixJson(json_in_text[1].replace("'", '"'))[:-4] + '}'
        json_parsed = json.loads(text_proceed)
        slots = []
        if len(comps_name) == 0:
            for each_comp in json_parsed["deckMetaItems"]:
                url = each_comp["url"]
                name = each_comp["name_en"]
                id = Parse(url, "deck=", "&")
                comps_name[id[1]] = name
        if len(champions_keys) == 0:
            for each_champ_stat in json_parsed["championStats"]:
                id = each_champ_stat["key"]
                normal_name = each_champ_stat["champion"]["name"]
                if id in SOFT_OVERRIDE_LIST:
                    normal_name = SOFT_OVERRIDE_LIST[id][1]
                    id = SOFT_OVERRIDE_LIST[id][0]
                champions_keys[id] = normal_name
        if len(items) == 0:
            for each_item in json_parsed["items"]:
                item = json_parsed["items"][each_item]
                id = item["id"]
                name = item["name"].replace("'", '').replace('’', '').replace(' ', '')
                items[id] = name
        counter = 0
        for each_slot in json_parsed["deck"]["slots"]:
            index = counter
            counter += 1
            if each_slot is not None:
                slot_items = []
                slot_champion_name_temp = each_slot["champion"]
                if slot_champion_name_temp in SOFT_OVERRIDE_LIST:
                    slot_champion_name_temp = SOFT_OVERRIDE_LIST[slot_champion_name_temp][0]
                if slot_champion_name_temp not in champions_keys:
                    is_good_comp = False
                    break
                slot_champion_name_temp = champions_keys[slot_champion_name_temp]
                is_good_champion = False
                best_score = 0.0
                best_possible: str = None
                for each_known_champ in comps_manager.champions:
                    if each_known_champ == slot_champion_name_temp:
                        is_good_champion = True
                        break
                    ratio = SequenceMatcher(a=each_known_champ, b=slot_champion_name_temp).ratio()
                    if ratio >= 0.7 and ratio > best_score:
                        best_score = ratio
                        best_possible = each_known_champ
                if is_good_champion == False:
                    if best_possible is not None:
                        slot_champion_name_temp = best_possible
                        is_good_champion = True
                    else:
                        if slot_champion_name_temp in FINAL_CHAMP_NAMES_LIST:
                            slot_champion_name_temp = FINAL_CHAMP_NAMES_LIST[slot_champion_name_temp]
                            is_good_champion = True
                if is_good_champion == False:
                    is_good_comp = False
                for each_item in each_slot.get("items", []):
                    normal_item = items[each_item]
                    if normal_item in ITEMS_OVERRIDE_LIST:
                        normal_item = ITEMS_OVERRIDE_LIST[normal_item]
                    if normal_item not in game_assets.ITEMS and normal_item not in game_assets.FULL_ITEMS:
                        is_good_comp = False
                        break
                    slot_items.append(normal_item)
                slots.append((slot_champion_name_temp, LOLCHESS_BOARD_ARRANGE[index], slot_items))
        if is_good_comp:
            output_comps[comps_name[each_link[1]]] = slots
    return output_comps


def __LoadCommunityDragon():
    loaded_string = requests.get(DRAGON_URL)
    json_parsed = json.loads(loaded_string.text)
    set_data_champions = json_parsed["setData"][2]["champions"]
    output = {}
    for each_champion in set_data_champions:
        board_size = 1
        traits = each_champion["traits"]
        for each_trait in traits:
            if each_trait == 'Dragon':
                board_size = 2
                break
        name_tft = each_champion["apiName"]
        ingame_name = each_champion["name"]
        if name_tft not in output:
            output[name_tft] = (ingame_name, board_size)
    return output


def LoadChampionsAndComps(comp_manager: CompsManager):
    print('Loading champions and comps...')
    cached_path = os.path.join(os.path.curdir, 'cached_data')
    if os.path.isdir(cached_path) == False:
        os.mkdir(cached_path)
    cached_file_path = os.path.join(cached_path, 'cached')
    lol_chess_tftnames_and_price = __LoadLoLChessPrices()
    set_current = lol_chess_tftnames_and_price[0]
    if os.path.isfile(cached_file_path + set_current + '.json'):
        print('Loading from cache file...')
        with open(cached_file_path + set_current + '.json', 'r') as f:
            comp_manager.champions = json.loads(f.readline())
            comp_manager.SetCOMPSLoaded(json.loads(f.readline()))
    else:
        print('Loading from web... (It can take up to ~1 min)')
        response_meta_comps = requests.get(LOLCHESS_META_COMPS_URL).text
        dragon_info_names_and_boardsize = __LoadCommunityDragon()
        for each in dragon_info_names_and_boardsize:
            if each in lol_chess_tftnames_and_price[1]:
                final_name = dragon_info_names_and_boardsize[each][0]
                final_price = lol_chess_tftnames_and_price[1][each][0]
                final_code_name = lol_chess_tftnames_and_price[1][each][1]
                if each in HARD_OVERRIDE_LIST:
                    final_code_name = HARD_OVERRIDE_LIST[each]
                final_boardsize = dragon_info_names_and_boardsize[each][1]
                comp_manager.champions[final_name] = {'Gold': final_price, 'Board Size': final_boardsize}
        lol_chess_comps = __LoadLolChessComps(response_meta_comps, set_current, comp_manager)
        for each_comp_name in lol_chess_comps:
            temp = {}
            for each_character in lol_chess_comps[each_comp_name]:
                temp[each_character[0]] = {'board_position': each_character[1], 'items': each_character[2],
                                           'level': 3, 'final_comp': True}
            comp_manager.comps_loaded.append((each_comp_name, temp))
        jsoned_champions = json.dumps(comp_manager.champions)
        jsoned_comps = json.dumps(comp_manager.comps_loaded)
        with open(cached_file_path + set_current + '.json', 'w') as f:
            f.write(jsoned_champions + '\n')
            f.write(jsoned_comps)
    print('Set: ' + set_current + ', loaded champions: ' + str(len(comp_manager.champions)) + ', comps: ' + str(
        len(comp_manager.comps_loaded)))
    for i in range(0, len(comp_manager.comps_loaded)):
        temp = ','.join(comp_manager.comps_loaded[i][1])
        print(str(i) + ' - ' + comp_manager.comps_loaded[i][0] + ' [' + temp + ']')

    inputed = ''
    temp_inputed = ''
    inputed_file_path = os.path.join(cached_path, 'inputed')
    if os.path.isfile(inputed_file_path):
        with open(inputed_file_path, 'r') as f:
            temp_inputed = f.read()
        if temp_inputed != '':
            print(
                'Your last selection was: "' + temp_inputed + '", press Enter to use last selection, or type "n" and press Enter to make new selection')
            if input().lower() == 'n':
                inputed = ''
            else:
                inputed = temp_inputed

    if inputed == '':
        print(
            'Select mode: \n-Press Enter to play random comps without sequence\n-Type "all" and press Enter to play all comps in sequence\n-Type "all_except 2 3 4"(for example) and press Enter to play all comps in sequence except selected\n-Type "1 2 3"(for example) and press Enter to play only selected comps in sequence (it will loop)')
        inputed = input()
    if inputed == '':
        comp_manager.is_sequence_mode = False
    elif inputed == 'all':
        comp_manager.is_sequence_mode = True
        for i in range(0, len(comp_manager.comps_loaded)):
            comp_manager.sequence.append(i)
    elif inputed.startswith('all_except'):
        comp_manager.is_sequence_mode = True
        splitted = inputed.split(' ')
        temp_except = []
        for each in splitted:
            if each.isnumeric():
                inted = int(each)
                temp_except.append(inted)
        for i in range(0, len(comp_manager.comps_loaded)):
            if i not in temp_except:
                comp_manager.sequence.append(i)
    else:
        comp_manager.is_sequence_mode = True
        splitted = inputed.split(' ')
        for each in splitted:
            if each.isnumeric():
                inted = int(each)
                comp_manager.sequence.append(inted)
    with open(inputed_file_path, 'w') as f:
        f.write(inputed)


if __name__ == "__main__":
    comps_manager = CompsManager()
    comps_manager.champions = {}
    LoadChampionsAndComps(comps_manager)