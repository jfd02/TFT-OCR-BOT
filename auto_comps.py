"""
Auto comps loader for lolchess.gg with auto cache
"""

import json
import os
import re
import pathlib
import requests
from bs4 import BeautifulSoup


from comps import CompsManager

# Constants
LOLCHESS_CHAMPIONS_URL = "https://lolchess.gg/champions/"
LOLCHESS_META_COMPS_URL = "https://lolchess.gg/meta"
LOLCHESS_BOARD_ARRANGE = [
    21, 22, 23, 24, 25, 26, 27,
    14, 15, 16, 17, 18, 19, 20,
    7, 8, 9, 10, 11, 12, 13,
    0, 1, 2, 3, 4, 5, 6,
]

def find_substring_index(input_str, from_where, to, start_index=0):
    """
    Find the index of a substring in the input string between two specified markers.
    """
    index_from = input_str.find(from_where, start_index)
    if index_from != -1:
        index_to = input_str.find(to, index_from + 1)
        if index_to != -1:
            return index_from, input_str[index_from + len(from_where):index_to]
    return -1, None

def extract_substrings(input_str, from_where, to):
    """
    Extract multiple substrings from the input string between the specified markers.
    """
    output = []
    index = 0
    while index != -1:
        current = find_substring_index(input_str, from_where, to, index)
        index = current[0]
        if index != -1:
            output.append(current)
            index += len(from_where)
    return output

def load_lolchess_prices():
    """
    Load champion prices from LOLCHESS.
    """
    lolchess_url = LOLCHESS_CHAMPIONS_URL
    response = requests.get(lolchess_url, timeout=10)
    current_tft_set = response.url.split("/")[4][3:]

    # Extracting JSON data from the response text
    json_in_text = (
        find_substring_index(
            response.text,
            "window.guideChampion = {\n            champions: ",
            r"}}],",
        )[1]
        + r"}}]"
    )
    json_parsed = json.loads(json_in_text)

    output_dictionary = {}
    for each_character in json_parsed:
        character_code = each_character["code"]
        character_name_ingame = each_character["ingame_code"]
        character_price = int(each_character["cost"])
        if character_name_ingame not in output_dictionary:
            character_code = each_character["code"]
            character_price = int(each_character["cost"])
            output_dictionary[character_name_ingame] = (character_price, character_code)
    return [current_tft_set, output_dictionary]

def load_lolchess_comps(input_str: str, set_str: str, comps_manager: CompsManager):
    # pylint: disable=unused-argument
    """
    Load LOLCHESS comps.
    """
    output_comps = []
    url_start_string = "https://lolchess.gg/builder/guide/"
    extract_substrings(input_str, url_start_string, '"')
    deck_soup = BeautifulSoup(input_str, "lxml")
    deck_list = []
    for deck in deck_soup.select(".guide-meta__deck-box"):
        nms = (
            deck.select_one(".guide-meta__deck__column.name.mr-3")
            .find(text=True)
            .strip()
        )
        afs = deck.select_one(".open-builder>a").attrs["href"]
        deck_list.append((nms, afs))
    pattern = r'<script id="__NEXT_DATA__" type="application/json">\s*({[\s\S]*?})\s*</script>'
    for nms, afs in deck_list:
        deck_keys = afs.split("/guide/")[-1].split("?type=guide")[0]
        deck_response = requests.get(
            f"https://lolchess.gg/builder/set{set_str}?hl=en&deck={deck_keys}",
            timeout=10)
        json_in_text = re.search(pattern, deck_response.text)[1]
        query_data = (
            json.loads(json_in_text)
            .get("props")
            .get("pageProps")
            .get("dehydratedState")
            .get("queries")[1]
            .get("state")
            .get("data")
            .get("refs")
        )
        with open("cached_data/deck.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(query_data))
        deck_slots = requests.get(
            f"https://tft.dakgg.io/api/v1/team-builders/{deck_keys}",
            timeout=10).json()
        counter = 0
        augments = deck_slots.get("teamBuilder", {}).get("augments", [])
        real_augments = [
            arg.get("name")
            for arg in query_data.get("augments", [])
            if arg.get("key") in augments
        ]
        slots = {}
        for each_slot in deck_slots.get("teamBuilder", {}).get("slots", []):
            if each_slot is not None:
                try:
                    champion_name = (
                        list(
                            filter(
                                lambda e, each_slot=each_slot: e["key"] == each_slot.get("champion"),
                                query_data.get("champions"),
                            ),
                        )[0]["name"]
                        .replace("Akali (K/DA)", "Akali")
                        .replace("Akali (True Damage)", "Akali")
                    )
                    star = each_slot.get("star", 1)
                except Exception:
                    continue
                slot_items = render_item(
                    query_data.get("items"),
                    each_slot.get("items", []),
                )
                slots[champion_name] = {
                    "board_position": LOLCHESS_BOARD_ARRANGE[each_slot.get("index")],
                    "items": slot_items,
                    "level": star,
                    "final_comp": True,
                }
            counter += 3
        output_comps.append([nms, slots, real_augments])
    return output_comps

def render_item(ob, ids):
    """
    Renders a list of items based on their IDs from given object.
    """
    items = list(filter(lambda e: e["key"] in ids, ob))
    return [
        i["name"].replace(" ", "").replace("'", "").replace("\u2019", "") for i in items
    ]

def load_from_cache(cached_file_path, comp_manager: CompsManager, set_current):
    """
    Load champions and comps data from the cache file.
    """
    with open(cached_file_path + set_current + ".json", encoding="utf-8") as f:
        comp_manager.champions = json.loads(f.readline())
        comp_manager.set_comps_loaded(json.loads(f.readline()))

def load_champions_and_comps(comp_manager: CompsManager):
    """
    Loads champion and composition data into CompsManager.
    """
    print("Loading champions and comps...")
    cached_path = os.path.join(os.path.curdir, "cached_data")

    if not os.path.isdir(cached_path):
        os.mkdir(cached_path)

    cached_file_path = os.path.join(cached_path, "cached")
    lol_chess_tftnames_and_price = load_lolchess_prices()
    set_current = lol_chess_tftnames_and_price[0]

    if os.path.isfile(cached_file_path + set_current + ".json"):
        print("Loading from cache file...")
        load_from_cache(cached_file_path, comp_manager, set_current)
    else:
        save_to_cache(
            comp_manager,
            set_current,
            cached_file_path,
        )

    print(
        f"Set: {set_current}, loaded champions: {len(comp_manager.champions)}, comps: {len(comp_manager.comps_loaded)}",
    )

    for i, comps_loaded_item in enumerate(comp_manager.comps_loaded):
        temp = ",".join(comps_loaded_item[1])
        print(f"{str(i)} - {comps_loaded_item[0]} [{temp}]")

    inputed = ""
    inputed_file_path = os.path.join(cached_path, "inputed")

    if os.path.isfile(inputed_file_path):
        temp_inputed = ""
        if temp_inputed := pathlib.Path(inputed_file_path).read_text(encoding="utf-8"):
            print(
                f'Your last selection was: "{temp_inputed}", '
                'press Enter to use the last selection, '
                'or type "n" and press Enter to make a new selection',
            )
            inputed = "" if input().lower() == "n" else temp_inputed

    if not inputed:
        print(
            'Select mode:',
            '\n-Press Enter to play random comps without a sequence',
            '\n-Type "all" and press Enter to play all comps in sequence',
            '\n-Type "all_except 2 3 4" (for example) and press Enter to play all comps in sequence except selected',
            '\n-Type "1 2 3" (for example) and press Enter to play only selected comps in sequence (it will loop)',
        )
        inputed = input()

    if not inputed:
        comp_manager.is_sequence_mode = False
    elif inputed == "all":
        comp_manager.is_sequence_mode = True
        for i in range(len(comp_manager.comps_loaded)):
            comp_manager.sequence.append(i)
    elif inputed.startswith("all_except"):
        comp_manager.is_sequence_mode = True
        splitted = inputed.split(" ")
        temp_except = [int(each) for each in splitted if each.isnumeric()]
        for i in range(len(comp_manager.comps_loaded)):
            if i not in temp_except:
                comp_manager.sequence.append(i)
    else:
        comp_manager.is_sequence_mode = True
        splitted = inputed.split(" ")
        for each in splitted:
            if each.isnumeric():
                inted = int(each)
                comp_manager.sequence.append(inted)

    with open(inputed_file_path, "w", encoding="utf-8") as f:
        f.write(inputed)

def save_to_cache(comp_manager: CompsManager, set_current, cached_file_path):
    """
    Save champions and comps data to a cache file.
    """
    print("Loading from web... (It can take up to ~1 min)")

    # Fetch meta comps data from LOLCHESS
    response_meta_comps = requests.get(LOLCHESS_META_COMPS_URL, timeout=10).text

    # Load LOLCHESS comps data
    lol_chess_comps = load_lolchess_comps(
        response_meta_comps,
        set_current,
        comp_manager,
    )

    # Update comps_loaded with LOLCHESS comps data
    comp_manager.comps_loaded = lol_chess_comps

    # Convert champions and comps data to JSON
    jsoned_champions = json.dumps(comp_manager.champions)
    jsoned_comps = json.dumps(comp_manager.comps_loaded)

    # Write JSON data to the cache file
    with open(cached_file_path + set_current + ".json", "w", encoding="utf-8") as f:
        f.write(jsoned_champions + "\n") # Writes champions data to the file
        f.write(jsoned_comps) # Writes comps data to the file
