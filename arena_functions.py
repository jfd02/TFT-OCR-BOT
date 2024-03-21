"""
Functions used by the Arena class to get game data
"""

import threading
from difflib import SequenceMatcher
from time import sleep

from typing import Optional
import numpy as np
import requests
from PIL import ImageGrab

import game_assets
import mk_functions
import ocr
import screen_coords
from comps import CompsManager
from vec4 import Vec4


def get_level_via_https_request() -> int:
    """Returns the level for the tactician"""
    try:
        response = requests.get(
            "https://127.0.0.1:2999/liveclientdata/allgamedata",
            timeout=20,
            verify=False,
        )
        return int(response.json()["activePlayer"]["level"])
    except (requests.exceptions.ConnectionError, KeyError):
        return 1


def get_level_via_ocr() -> int:
    """Returns the level of the tactician"""
    level: str = ocr.get_text(
        screenxy=screen_coords.TACTICIAN_LEVEL_POS.get_coords(),
        scale=3,
        psm=8,
        whitelist="0123456789",
    )
    try:
        return int(level)
    except ValueError:
        return -1


def get_health() -> int:
    """Returns the health for the tactician"""
    try:
        response = requests.get(
            "https://127.0.0.1:2999/liveclientdata/allgamedata",
            timeout=20,
            verify=False,
        )
        return int(response.json()["activePlayer"]["championStats"]["currentHealth"])
    except (
        requests.exceptions.ReadTimeout,
        requests.exceptions.ConnectionError,
        KeyError,
    ):
        return -1


def get_gold() -> int:
    """Returns the gold for the tactician"""
    gold: str = ocr.get_text(
        screenxy=screen_coords.GOLD_POS.get_coords(),
        scale=3,
        psm=7,
        whitelist="0123456789",
    )
    try:
        return int(gold)
    except ValueError:
        return 0


def valid_champ(champ: str, comps: CompsManager) -> str:
    """Matches champion string to a valid champion name string and returns it"""
    if champ in comps.champions:
        return champ

    return next(
        (
            champion
            for champion in comps.champions
            if SequenceMatcher(a=champion, b=champ).ratio() >= 0.7
        ),
        "",
    )


def get_champ(
    screen_capture: ImageGrab.Image,
    name_pos: Vec4,
    shop_pos: int,
    shop_array: list,
    comps: CompsManager,
) -> str:
    """Returns a tuple containing the shop position and champion name"""
    champ: str = screen_capture.crop(name_pos.get_coords())
    champ: str = ocr.get_text_from_image(image=champ, whitelist="")
    shop_array.append((shop_pos, valid_champ(champ, comps)))


def get_shop(comps: CompsManager) -> list:
    """Returns the list of champions in the shop"""
    screen_capture = ImageGrab.grab(bbox=screen_coords.SHOP_POS.get_coords())
    shop: list = []
    thread_list: list = []
    for shop_index, name_pos in enumerate(screen_coords.CHAMP_NAME_POS):
        thread = threading.Thread(
            target=get_champ, args=(screen_capture, name_pos, shop_index, shop, comps)
        )
        thread_list.append(thread)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    return sorted(shop)


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


def board_occupied_check() -> list:
    """Returns a list of booleans that map to each board slot indicating if its occupied"""
    board_occupied: list = []
    for positions in enumerate(screen_coords.BOARD_HEALTH_POS):
        screen_capture = ImageGrab.grab(bbox=positions.get_coords())
        screenshot_array = np.array(screen_capture)
        if not (np.abs(screenshot_array - (0, 255, 18)) <= 2).all(axis=2).any():
            board_occupied.append(False)
            # labels.append(("False", screen_coords.BOARD_LOC[index].get_coords(), 0, 0))  # it just clutters the screen
        else:
            board_occupied.append(True)
    return board_occupied


def valid_item(item: str) -> Optional[str]:
    """Checks if the item passed in arg one is valid"""
    return next(
        (
            valid_item_name
            for valid_item_name in game_assets.ALL_ITEMS
            if valid_item_name in item
            or SequenceMatcher(a=valid_item_name, b=item).ratio() >= 0.85
        ),
        None,
    )


def get_items() -> list:
    """Returns a list of items currently on the board"""
    item_bench: list = []
    for positions in screen_coords.ITEM_POS:
        mk_functions.move_mouse(positions[0].get_coords())
        sleep(0.1)
        item: str = ocr.get_text(
            screenxy=positions[1].get_coords(),
            scale=3,
            psm=8,
            whitelist=ocr.ALPHABET_WHITELIST,
        )
        item_bench.append(valid_item(item))
    mk_functions.move_mouse(screen_coords.DEFAULT_LOC.get_coords())
    return item_bench


def check_headliner() -> bool:
    """Check if the last Champion in the store is a headliner"""
    result: int = 0
    for index, positions in enumerate(screen_coords.HEADLINER_POS):
        headliner: str = ocr.get_text(
            screenxy=positions.get_coords(),
            scale=3,
            psm=10,
            whitelist=ocr.ROUND_WHITELIST.replace("-", ""),
        )
        if headliner == "2":
            result += 2**index
    return result


def get_seconds_remaining() -> int:
    """Returns how many seconds are remaining before the next phase of this round."""
    seconds: str = ocr.get_text(
        screenxy=screen_coords.SECONDS_REMAINING_POS.get_coords(),
        scale=3,
        psm=7,
        whitelist="0123456789",
    )
    try:
        if int(seconds) > 60:
            return -1

        return int(seconds)
    except ValueError:
        return -1
