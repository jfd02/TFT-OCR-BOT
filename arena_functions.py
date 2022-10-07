"""
Functions used by the Arena class to get game data
"""

from difflib import SequenceMatcher
import threading
from PIL import ImageGrab
import numpy as np
import requests
import screen_coords
import ocr
import game_assets
import mk_functions
from vec4 import Vec4


def get_level() -> int:
    """Returns the level for the tactician"""
    try:
        response = requests.get(
            'https://127.0.0.1:2999/liveclientdata/allgamedata', timeout=10, verify=False)
        return int(response.json()['activePlayer']['level'])
    except (requests.exceptions.ConnectionError, KeyError):
        return 1


def get_health() -> int:
    """Returns the health for the tactician"""
    try:
        response = requests.get(
            'https://127.0.0.1:2999/liveclientdata/allgamedata', timeout=10, verify=False)
        return int(response.json()['activePlayer']['championStats']["currentHealth"])
    except (requests.exceptions.ConnectionError, KeyError):
        return 100


def get_gold() -> int:
    """Returns the gold for the tactician"""
    gold: str = ocr.get_text(screenxy=screen_coords.GOLD_POS.get_coords(), scale=3, psm=7, whitelist="0123456789")
    try:
        return int(gold)
    except ValueError:
        return 0


def valid_champ(champ: str) -> str:
    """Matches champion string to a valid champion name string and returns it"""
    if champ in game_assets.CHAMPIONS:
        return champ

    for champion in game_assets.CHAMPIONS:
        if SequenceMatcher(a=champion, b=champ).ratio() >= 0.7:
            return champion
    return ""

def get_champ(screen_capture: ImageGrab.Image, name_pos: Vec4, shop_pos: int, shop_array: list) -> str:
    """Returns a tuple containing the shop position and champion name"""
    champ: str = screen_capture.crop(name_pos.get_coords())
    champ: str = ocr.get_text_from_image(image=champ, whitelist="")
    shop_array.append((shop_pos, valid_champ(champ)))

def get_shop() -> list:
    """Returns the list of champions in the shop"""
    screen_capture = ImageGrab.grab(bbox=screen_coords.SHOP_POS.get_coords())
    shop: list = []
    thread_list: list = []
    for shop_index, name_pos in enumerate(screen_coords.CHAMP_NAME_POS):
        thread = threading.Thread(target=get_champ, args=(screen_capture, name_pos, shop_index, shop))
        thread_list.append(thread)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    return shop


def empty_slot() -> int:
    """Finds the first empty spot on the bench"""
    for slot, positions in enumerate(screen_coords.BENCH_HEALTH_POS):
        screen_capture = ImageGrab.grab(bbox=positions.get_coords())
        screenshot_array = np.array(screen_capture)
        if not (np.abs(screenshot_array - (0, 255, 18)) <= 3).all(axis=2).any():
            return slot  # Slot 0-8
    return -1  # No empty slot


def bench_occupied_check() -> list:
    """Returns a list of booleans that map to each bench slot indicating if its occupied"""
    bench_occupied: list = []
    for positions in screen_coords.BENCH_HEALTH_POS:
        screen_capture = ImageGrab.grab(bbox=positions.get_coords())
        screenshot_array = np.array(screen_capture)
        if not (np.abs(screenshot_array - (0, 255, 18)) <= 2).all(axis=2).any():
            bench_occupied.append(False)
        else:
            bench_occupied.append(True)
    return bench_occupied


def valid_item(item: str) -> str | None:
    """Checks if the item passed in arg one is valid"""
    for valid_item_name in game_assets.ITEMS:
        if valid_item_name in item or SequenceMatcher(a=valid_item_name, b=item).ratio() >= 0.7:
            return valid_item_name
    return None


def get_items() -> list:
    """Returns a list of items currently on the board"""
    item_bench: list = []
    for positions in screen_coords.ITEM_POS:
        mk_functions.move_mouse(positions[0].get_coords())
        item: str = ocr.get_text(screenxy=positions[1].get_coords(), scale=3, psm=13,
                            whitelist=ocr.ALPHABET_WHITELIST)
        item_bench.append(valid_item(item))
    mk_functions.move_mouse(screen_coords.DEFAULT_LOC.get_coords())
    return item_bench
    