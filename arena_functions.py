import string
import pydirectinput
from PIL import ImageGrab
from difflib import SequenceMatcher
import numpy as np
import requests

import screen_coords
import ocr
import game_assets
import mk_functions


def get_level() -> int:
    try:
        resposne = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', timeout=10, verify=False)
        return int(resposne.json()['activePlayer']['level'])
    except Exception:
        return 1


def get_health() -> int:
    try:
        resposne = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', timeout=10, verify=False)
        return int(resposne.json()['activePlayer']['championStats']["currentHealth"])
    except Exception:
        return 100


def get_gold() -> int:
    gold = ocr.get_text(screenxy=screen_coords.gold_pos, scale=3, psm=7, whitelist="0123456789")
    try:
        return int(gold)
    except ValueError:
        return 0

def match_string(champ) -> string:
    for champion in game_assets.champions:
        if SequenceMatcher(a=champ,b=champion).ratio() >= 0.7:
            return champion
    return ""

def get_shop() -> list:
    screen_capture = ImageGrab.grab(bbox=screen_coords.shop_pos)
    shop = []
    for names in screen_coords.champ_name_pos:
        champ = screen_capture.crop(names)
        champ = ocr.get_text_image(image=champ, whitelist="")
        if champ in game_assets.champions:
            shop.append(champ)
        else:
            shop.append(match_string(champ))
    return shop


def empty_slot() -> int:
    for slot, positions in enumerate(screen_coords.bench_health_pos):
        screen_capture = ImageGrab.grab(bbox=positions)
        screenshot_array = np.array(screen_capture)
        if not (np.abs(screenshot_array - (0, 255, 18)) <= 3).all(axis=2).any():
            return slot  # Slot 0-8
    return -1  # No empty slot


def bench_occupied_check() -> list:
    bench_occupied = []
    for positions in screen_coords.bench_health_pos:
        screen_capture = ImageGrab.grab(bbox=positions)
        screenshot_array = np.array(screen_capture)
        if not (np.abs(screenshot_array - (0, 255, 18)) <= 2).all(axis=2).any():
            bench_occupied.append(False)
        else:
            bench_occupied.append(True)
    return bench_occupied


def valid_item(item):
    for valid_item_name in game_assets.items:
        if valid_item_name in item:
            return valid_item_name
        elif SequenceMatcher(a=valid_item_name,b=item).ratio() >= 0.7:
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
