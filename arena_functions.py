# Original code from the TFT_OCR_BOT repository on GitHub:
# Repository URL: https://github.com/jfd02/TFT-OCR-BOT
# Original authors:
# - @jfd02
# - @Squarific
# - @danparizher
# Modified by the-user-created
#

"""
Functions used by the Arena class to get game data
"""

from difflib import SequenceMatcher
import threading
from PIL import ImageGrab, Image
import numpy as np
import requests
import screen_coords
import ocr
import game_assets
import mk_functions
from vec2 import Vec2
from vec4 import Vec4
from time import sleep
from math import sqrt

# pylint: disable=fixme


def get_level() -> int:
    """Returns the level for the tactician"""
    try:
        response = requests.get(
            "https://127.0.0.1:2999/liveclientdata/allgamedata",
            timeout=10,
            verify=False,
        )
        return int(response.json()["activePlayer"]["level"])
    except (requests.exceptions.ConnectionError, KeyError):
        return 1


def get_health() -> int:
    """Returns the health for the tactician"""
    try:
        response = requests.get(
            "https://127.0.0.1:2999/liveclientdata/allgamedata",
            timeout=10,
            verify=False,
        )
        return int(response.json()["activePlayer"]["championStats"]["currentHealth"])
    except (requests.exceptions.ConnectionError, KeyError):
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


def valid_champ(champ: str) -> str:
    """Matches champion string to a valid champion name string and returns it"""
    if champ in game_assets.CHAMPIONS:
        return champ

    return next(
        (
            champion
            for champion in game_assets.CHAMPIONS
            if SequenceMatcher(a=champion, b=champ).ratio() >= 0.7
        ),
        "",
    )


def get_champ(
    screen_capture: ImageGrab.Image, name_pos: Vec4, shop_pos: int, shop_array: list
) -> str:
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
        thread = threading.Thread(
            target=get_champ, args=(screen_capture, name_pos, shop_index, shop)
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
        if not (np.abs(screenshot_array - (0, 255, 18, 255)) <= 3).all(axis=2).any():
            return slot  # Slot 0-8
    return -1  # No empty slot


def process_portal_data(position, portal_button_pos) -> dict:
    """Process portal data based on given position and button coordinates"""
    screen_capture = ImageGrab.grab(bbox=position.get_coords())
    portal_name = ocr.get_text_from_image(image=screen_capture, whitelist=ocr.PORTAL_WHITELIST)

    match = {portal: SequenceMatcher(a=portal, b=portal_name).ratio() for portal in game_assets.PORTALS}
    closest_match = max(match, key=match.get)

    if match[closest_match] >= 0.7:
        # Returns a dict of portal names and their button coordinates (button of the portal)
        return {closest_match: portal_button_pos}

    # TODO: This is a hacky fix, but it works for now
    return {"NULL": "NULL"}


def get_portals() -> dict:
    """Gets the portals that are currently open in round 1-1"""
    portals: dict = {}
    for position, portal_button_pos in zip(screen_coords.PORTAL_POS, screen_coords.PORTAL_BUTTON_POS):
        portal_data = process_portal_data(position, portal_button_pos)
        portals.update(portal_data)

    return portals  # Returns a dict of portals and their button coordinates (button of the portal)


def get_active_portal() -> str:
    """Gets the active portal name from the arena info flag thing using OCR"""
    arena_info_button = screen_coords.ARENA_INFO_BUTTON_POS
    mk_functions.right_click(arena_info_button.get_coords())
    sleep(0.1)  # Sleep for a short period to allow the portal name to appear
    portal_name = screen_coords.PORTAL_NAME_POS
    portal_data = process_portal_data(portal_name, None)
    if not portal_data:
        return ""
    return list(portal_data.keys())[0]  # Returns the portal name


def get_portal_vote_loc() -> Vec2:
    """Returns the location of the portal vote button"""
    vote_button = ocr.find_template_centers(template_path="ProgramFiles/vote_button.png", threshold=0.65,
                                            region=screen_coords.PORTAL_VOTE_AREA.get_coords())

    # De-apply the crop
    crop_coords = screen_coords.PORTAL_VOTE_AREA.get_coords()
    vote_button = [(x + crop_coords[0], y + crop_coords[1]) for x, y in vote_button]
    # TODO: vote_button should only be one coordinate, not a list of coordinates

    # Convert the coordinates of the vote button to a Vec2 object and return
    return Vec2(vote_button[0][0], vote_button[0][1])


def nearest_neighbor(coordinates) -> list:
    """Find the shortest route to visit all coordinates"""
    unvisited = set(range(len(coordinates)))
    current_point = 0
    route = [current_point]
    unvisited.remove(current_point)

    while unvisited:
        nearest_point = min(unvisited, key=lambda x: calculate_distance(coordinates[current_point], coordinates[x]))
        route.append(nearest_point)
        current_point = nearest_point
        unvisited.remove(current_point)

    return route


def calculate_distance(coord1, coord2):
    """Calculate Euclidean distance between two coordinates"""
    return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)


def get_orb_pick_up_route() -> list:
    """Picks up items from the board after PVP round"""
    # TODO: This is not perfect, it occasionally misses orbs due to obstructions preventing cv2 from matching
    #  the template.
    #  Also haven't tested for yellow orbs yet

    # Load and process templates
    blue_centers = ocr.find_template_centers(template_path="ProgramFiles/blueTemplate.png", threshold=0.55,
                                             region=screen_coords.BOARD_AREA.get_coords())
    gray_centers = ocr.find_template_centers(template_path="ProgramFiles/grayTemplate.png", threshold=0.55,
                                             region=screen_coords.BOARD_AREA.get_coords())

    # Adjust the centers to the correct position on screen ("de-apply" the crop)
    crop_coords = screen_coords.BOARD_AREA.get_coords()
    blue_centers = [(x + crop_coords[0], y + crop_coords[1]) for x, y in blue_centers]
    gray_centers = [(x + crop_coords[0], y + crop_coords[1]) for x, y in gray_centers]

    # Merge the blue and gray centers
    centers = [(screen_coords.DEFAULT_TACTICIAN_LOC.get_coords())] + blue_centers + gray_centers

    # Get the shortest path
    shortest_route = nearest_neighbor(centers)
    shortest_route = [centers[i] for i in shortest_route]

    # Remove tactician location from the route
    shortest_route.remove(screen_coords.DEFAULT_TACTICIAN_LOC.get_coords())

    # Return the route
    return shortest_route


def bench_occupied_check() -> list:
    """Returns a list of booleans that map to each bench slot indicating if its occupied"""
    bench_occupied: list = []
    for positions in screen_coords.BENCH_HEALTH_POS:
        screen_capture = ImageGrab.grab(bbox=positions.get_coords())
        screenshot_array = np.array(screen_capture)
        if not (np.abs(screenshot_array - (0, 255, 18, 255)) <= 2).all(axis=2).any():
            bench_occupied.append(False)
        else:
            bench_occupied.append(True)
    return bench_occupied


def valid_item(item: str) -> str | None:
    """Checks if the item passed in arg one are valid"""
    return next(
        (
            valid_item_name
            for valid_item_name in game_assets.ITEMS
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
        item: str = ocr.get_text(
            screenxy=positions[1].get_coords(),
            scale=3,
            psm=7,
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
