"""
Auto comps loader WompWomp99 (with autocache)
Champion names are different in lolchess/communitydragon/tftactics
Some champion names is repeating because of different patches (but it's the same champion), for example Nomsy
In-game champion names only in communitydragon
"""
import re
from urllib import parse

import game_assets
import json
import requests
from difflib import SequenceMatcher
import os
from comps import CompsManager
from bs4 import BeautifulSoup

LOLCHESS_CHAMPIONS_URL = 'https://lolchess.gg/champions/'
LOLCHESS_META_COMPS_URL = 'https://lolchess.gg/meta'
DRAGON_URL = 'https://raw.communitydragon.org/latest/cdragon/tft/en_us.json'

HARD_OVERRIDE_LIST = {'TFT7_Wukong': 'Wukong'}
LOLCHESS_BOARD_ARRANGE = [21, 22, 23, 24, 25, 26, 27, 14, 15, 16, 17, 18, 19, 20, 7, 8, 9, 10, 11, 12, 13, 0, 1, 2, 3,
                          4, 5, 6]

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
            character_code = each_character['code']
            character_price = int(each_character['cost'])
            output_dictionary[character_name_ingame] = (character_price, character_code)
    return [current_tft_set, output_dictionary]


def __LoadLolChessComps(input_str, set_str, comps_manager: CompsManager):
    output_comps = []
    url_start_string = "https://lolchess.gg/builder" + "?deck="
    parsed_links = ParseMultiple(input_str, url_start_string, '"')
    deck_soup = BeautifulSoup(input_str, "lxml")
    deck_list = []
    for deck in deck_soup.select(".guide-meta__deck-box"):
        nms = deck.select_one(".guide-meta__deck__column.name.mr-3").find(text=True).strip()
        afs = deck.select_one(".open-builder>a").attrs['href']
        deck_list.append((nms, afs))
    for nms, afs in deck_list:
        deck_keys = parse.parse_qs(parse.urlparse(afs).query)['deck'][0]
        deck_response = requests.get(
            f"https://lolchess.gg/builder/set8?hl=en&deck={deck_keys}"
        )
        pattern = r'<script id="__NEXT_DATA__" type="application/json">\s*({[\s\S]*?})\s*</script>'
        json_in_text = re.search(pattern, deck_response.text)[1]
        query_data = json.loads(json_in_text).get("props").get("pageProps").get("dehydratedState").get("queries")[
            1].get("state").get("data").get("refs")
        with open("cached_data/deck.json", "w") as f:
            f.write(json.dumps(query_data))
        deck_slots = requests.get(f"https://tft.dakgg.io/api/v1/team-builders/{deck_keys}").json()
        slots = {}
        counter = 0
        augments = deck_slots.get("teamBuilder", {}).get("augments", [])
        real_augments = [arg.get("name") for arg in query_data.get('augments', [])
                         if arg.get("key") in augments]
        for each_slot in deck_slots.get("teamBuilder", {}).get("slots", []):

            if each_slot is not None:
                try:
                    champion_name = \
                    list(filter(lambda e: e['key'] == each_slot.get("champion"), query_data.get("champions")))[
                        0]['name']
                except Exception:
                    continue
                slot_items = render_item(query_data.get("items"), each_slot.get("items", []))
                slots[champion_name] = {'board_position': LOLCHESS_BOARD_ARRANGE[each_slot.get("index")], 'items': slot_items,
                                        'level': 3, 'final_comp': True}
            counter += 3

        output_comps.append([nms, slots, real_augments])
    return output_comps


def render_item(ob, ids):
    items = list(filter(lambda e: e['key'] in ids, ob))
    return [i['name'].replace(" ", "").replace("'", "") for i in items]


def __LoadCommunityDragon():
    loaded_string = requests.get(DRAGON_URL)
    json_parsed = json.loads(loaded_string.text)
    set_data_champions = json_parsed["setData"][2]["champions"]
    output = {}
    for each_champion in set_data_champions:
        traits = each_champion["traits"]
        board_size = next((2 for each_trait in traits if each_trait == 'Dragon'), 1)
        name_tft = each_champion["apiName"]
        if name_tft not in output:
            ingame_name = each_champion["name"]
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
        comp_manager.comps_loaded = lol_chess_comps
        jsoned_champions = json.dumps(comp_manager.champions)
        jsoned_comps = json.dumps(comp_manager.comps_loaded)
        with open(cached_file_path + set_current + '.json', 'w') as f:
            f.write(jsoned_champions + '\n')
            f.write(jsoned_comps)
    print(
        f'Set: {set_current}, loaded champions: {len(comp_manager.champions)}, comps: {len(comp_manager.comps_loaded)}'
    )
    for i in range(len(comp_manager.comps_loaded)):
        temp = ','.join(comp_manager.comps_loaded[i][1])
        print(f'{str(i)} - {comp_manager.comps_loaded[i][0]} [{temp}]')

    inputed = ''
    temp_inputed = ''
    inputed_file_path = os.path.join(cached_path, 'inputed')
    if os.path.isfile(inputed_file_path):
        with open(inputed_file_path, 'r') as f:
            temp_inputed = f.read()
        if temp_inputed != '':
            print(
                f'Your last selection was: "{temp_inputed}", press Enter to use last selection, or type "n" and press Enter to make new selection'
            )
            inputed = '' if input().lower() == 'n' else temp_inputed
    if inputed == '':
        print(
            'Select mode: \n-Press Enter to play random comps without sequence\n-Type "all" and press Enter to play all comps in sequence\n-Type "all_except 2 3 4"(for example) and press Enter to play all comps in sequence except selected\n-Type "1 2 3"(for example) and press Enter to play only selected comps in sequence (it will loop)')
        inputed = input()
    if inputed == '':
        comp_manager.is_sequence_mode = False
    elif inputed == 'all':
        comp_manager.is_sequence_mode = True
        for i in range(len(comp_manager.comps_loaded)):
            comp_manager.sequence.append(i)
    elif inputed.startswith('all_except'):
        comp_manager.is_sequence_mode = True
        splitted = inputed.split(' ')
        temp_except = [int(each) for each in splitted if each.isnumeric()]
        for i in range(len(comp_manager.comps_loaded)):
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
    print(comps_manager)