import pydirectinput
from PIL import ImageGrab
import numpy as np

import screen_coords
import ocr
import game_assets
import mk_functions


def get_level() -> int:
    level = ocr.get_text(screenxy=screen_coords.level_pos, scale=3, psm=7, whitelist="0123456789")
    try:
        level = int(level)
        return level
    except ValueError:
        return 1


def get_health() -> int:
    mk_functions.left_click(screen_coords.health_loc)
    health = ocr.get_text(screenxy=screen_coords.health_pos, scale=3, psm=7, whitelist="0123456789")
    try:
        health = int(health)
        return health
    except ValueError:
        return 100


def get_gold() -> int:
    gold = ocr.get_text(screenxy=screen_coords.gold_pos, scale=3, psm=7, whitelist="0123456789")
    try:
        return int(gold)
    except ValueError:
        return 0


def get_shop() -> list:
    screen_capture = ImageGrab.grab(bbox=screen_coords.shop_pos)
    shop = []
    for names in screen_coords.champ_name_pos:
        champ = screen_capture.crop(names)
        champ = ocr.get_text_image(image=champ, whitelist="")
        if champ in game_assets.champions:
            shop.append(champ)
        else:
            shop.append("")
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
