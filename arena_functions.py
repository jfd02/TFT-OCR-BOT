"""
Functions used by the Arena class to get game data
"""

import threading
from difflib import SequenceMatcher
from time import sleep

import numpy as np
import requests
from PIL import ImageGrab

import mk_functions
import ocr
import screen_coords
from champion import Champion
from set_9_5 import game_assets
from vec2 import Vec2
from vec4 import Vec4


def get_level_via_https_request() -> int:
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


def get_valid_champ(champ_name: str) -> str:
    """Matches champion string to a valid champion name string and returns it"""
    if champ_name in game_assets.CHAMPIONS:
        return champ_name
    for champion in game_assets.CHAMPIONS:
        if SequenceMatcher(a=champion, b=champ_name).ratio() >= 0.7:
            return champion
    if champ_name is not None and len(champ_name) > 0:
        # print(f"  [!] The champ_name {champ_name} did not match any unit in game_assets.CHAMPIONS!")
        return ""


def is_valid_champ(champ_name: str) -> bool:
    if champ_name == "":
        return False
    if champ_name in game_assets.CHAMPIONS:
        print(f"       Confirmed that {champ_name} is a valid champ.")
        return True
    elif champ_name is not None and champ_name != "" and champ_name != " ":
        print(f"       Unable to confirm that {champ_name} is a valid champ.")
    return False


def get_champ(screen_capture: ImageGrab.Image, name_pos: Vec4, shop_pos: int, shop_array: list) -> str:
    """Returns a tuple containing the shop position and champion name"""
    champ: str = screen_capture.crop(name_pos.get_coords())
    champ: str = ocr.get_text_from_image(image=champ, whitelist="")
    shop_array[shop_pos] = get_valid_champ(champ)


def get_shop() -> list:
    """Returns the list of champions in the shop"""
    screen_capture = ImageGrab.grab(bbox=screen_coords.SHOP_POS.get_coords())
    shop: list = [None] * 5
    thread_list: list = []
    for shop_index, name_pos in enumerate(screen_coords.CHAMP_NAME_POS):
        thread = threading.Thread(target=get_champ, args=(screen_capture, name_pos, shop_index, shop))
        thread_list.append(thread)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    return shop


def empty_bench_slot() -> int:
    """Finds the first empty spot on the bench"""
    for slot, positions in enumerate(screen_coords.BENCH_HEALTH_POS):
        screen_capture = ImageGrab.grab(bbox=positions.get_coords())
        screenshot_array = np.array(screen_capture)
        if not (np.abs(screenshot_array - (0, 255, 18)) <= 3).all(axis=2).any():
            return slot  # Slot 0-8
    return -1  # No empty slot


def bench_occupied_check() -> list:
    """Returns a list of booleans that map to each bench slot indicating if it's occupied by a unit.
        Does this by looping through the screen coordinates defined as where health bars would appear,
        and checking if that position matches the specific color of health bars.
    """
    bench_occupied: list = []
    for positions in screen_coords.BENCH_HEALTH_POS:
        screen_capture = ImageGrab.grab(bbox=positions.get_coords())
        screenshot_array = np.array(screen_capture)
        if not (np.abs(screenshot_array - (0, 255, 18)) <= 2).all(axis=2).any():
            bench_occupied.append(False)
        else:
            bench_occupied.append(True)
    return bench_occupied


def valid_item_from_all_items(item: str) -> str | None:
    """Checks if the item passed in arg one is valid"""
    return next(
        (
            valid_item_name
            for valid_item_name in game_assets.ALL_ITEMS
            if valid_item_name in item
               or SequenceMatcher(a=valid_item_name, b=item).ratio() >= 0.7
        ),
        None,
    )


def valid_item_from_holdable_items(item: str) -> str | None:
    """Checks if the item passed in arg one is valid item and that item is holdable, not a consumable item."""
    for valid_item_name in game_assets.HOLDABLE_ITEMS:
        if valid_item_name in item or SequenceMatcher(a=valid_item_name, b=item).ratio() >= 0.7:
            print(f"    Item: {item} --- matched with --- Valid Item: {valid_item_name}")
            return valid_item_name
    if len(item) > 3:
        print(f"  [!] The item {item} did not match any items in game_assets.HOLDABLE_ITEMS!")


def get_items() -> list:
    """Returns a list of items currently on the board"""
    item_bench: list = []
    for positions in screen_coords.ITEM_POS:
        mk_functions.move_mouse(positions[0].get_coords())
        item: str = ocr.get_text(screenxy=positions[1].get_coords(), scale=3, psm=13,
                                 whitelist=ocr.ALPHABET_WHITELIST)
        item_bench.append(valid_item_from_all_items(item))
    mk_functions.move_mouse(screen_coords.DEFAULT_LOC.get_coords())
    return item_bench


def tacticians_crown_check(self) -> None:
    """Checks if the item from carousel is tacticians crown"""
    print("    Checking for a Tacticians Crown.")
    mk_functions.move_mouse(screen_coords.ITEM_POS[0][0].get_coords())
    sleep(0.5)
    item: str = ocr.get_text(screenxy=screen_coords.ITEM_POS[0][1].get_coords(), scale=3, psm=13,
                             whitelist=ocr.ALPHABET_WHITELIST)
    item: str = valid_item_from_all_items(item)
    try:
        if "TacticiansCrown" in item:
            print("  Tacticians Crown on bench, adding extra slot to board")
            # self.max_board_size -= 1
        else:
            print(f"{item} is not TacticiansCrown")
    except TypeError:
        print("  Item could not be read for Tacticians Check")


def get_level_via_ocr() -> int:
    """Returns the level of the tactician"""
    level: str = ocr.get_text(screenxy=screen_coords.TACTICIAN_LEVEL_POS.get_coords(), scale=3, psm=8,
                              whitelist="0123456789")
    try:
        return int(level)
    except ValueError:
        return -1


def get_cost_to_buy_xp() -> int:
    """Returns the cost to buy xp for the tactician"""
    xp_cost: str = ocr.get_text(screenxy=screen_coords.BUY_XP_COST_POS.get_coords(), scale=3, psm=7,
                                whitelist="0123456789")
    try:
        return int(xp_cost)
    except ValueError:
        return 10


def get_seconds_remaining() -> int:
    """Returns how many seconds are remaining before the next phase of this round."""
    seconds: str = ocr.get_text(screenxy=screen_coords.SECONDS_REMAINING_UNTIL_NEXT_STEP_POS.get_coords(), scale=3,
                                psm=7, whitelist="0123456789")
    try:
        return int(seconds)
    except ValueError:
        return -1


def get_win_loss_streak() -> int:
    """Returns the number of the win streak or the loss streak."""
    streak: str = ocr.get_text(screenxy=screen_coords.WIN_STREAK_LOSS_STREAK_AMOUNT_POS.get_coords(), scale=3, psm=7,
                               whitelist="0123456789")
    try:
        return int(streak)
    except ValueError:
        return -1


def get_cost_to_refresh_shop() -> int:
    """Returns how much gold it costs to refresh the shop."""
    cost: str = ocr.get_text(screenxy=screen_coords.SHOP_REFRESH_COST_POS.get_coords(), scale=3, psm=8,
                             whitelist="0123456789")
    try:
        return int(cost)
    except ValueError:
        return -1


def get_current_xp_and_total_needed_xp() -> int:
    """Returns how much xp the player current has towards their next level
    and the total amount of xp they need to get that level."""
    current_xp_and_total_needed_xp: str = ocr.get_text(screenxy=screen_coords.TACTICIAN_XP_FRACTION_POS.get_coords(),
                                                       scale=3, psm=7, whitelist="0123456789")
    try:
        return int(current_xp_and_total_needed_xp)
    except ValueError:
        return -1


def get_current_amount_of_units_on_board() -> int:
    """Returns the ocr'd number rendered on the board by the game that is how many units the player has on the board."""
    current_unit_amount: str = ocr.get_text(
        screenxy=screen_coords.CURRENT_AMOUNT_OF_CHAMPIONS_ON_BOARD_POS.get_coords(),
        scale=3, psm=7, whitelist="0123456789")
    try:
        return int(current_unit_amount)
    except ValueError:
        return -1


def get_max_amount_of_units_on_board() -> int:
    """Returns the ocr'd number rendered on the board by the game that is
       the max amount of units the player could have on their board."""
    max_unit_amount: str = ocr.get_text(screenxy=screen_coords.MAX_AMOUNT_OF_CHAMPIONS_ON_BOARD_POS.get_coords(),
                                        scale=3, psm=7, whitelist="0123456789")
    try:
        return int(max_unit_amount)
    except ValueError:
        return -1


def print_item_placed_on_champ(item: str, champ: Champion):
    print(f"      Placed {item} on {champ.name}")


def get_area_of_item_orbs() -> [Vec4]:
    """Returns the coordinate positions of items if there are any on the board.
       Does this by searching the whole board to see if there are any question marks.
       Page Sementation Mode (PSM) 11 is for finding:
       'Sparse Text: Find as Much Text as Possible in No Particular Order'"""
    area_of_item_orbs: [Vec4] = ocr.get_coordinates_of_text(screenxy=screen_coords.BOARD_OF_ARENA_POS.get_coords(),
                                                            scale=3, psm=11, whitelist="?")
    try:
        return area_of_item_orbs
    except ValueError:
        return -1


def get_center_position_of_item_orbs() -> [Vec2]:
    """Returns the center coordinate positions of items if there are any on the board."""
    area_of_item_orbs = get_area_of_item_orbs()
    # Don't instantiate lists like this: center_of_item_orbs = [Vec2]
    center_of_item_orbs = []
    for item_orb in area_of_item_orbs:
        vec4 = item_orb.get_coords()
        x1 = vec4[0]
        y1 = vec4[1]
        x2 = vec4[0] + vec4[2]
        y2 = vec4[1] + vec4[3]
        x_center = (x1 + x2) / 2
        y_center = (y1 + y2) / 2
        vec_2 = Vec2(x_center, y_center)
        center_of_item_orbs.append(vec_2)
    return center_of_item_orbs


def identify_one_champion_on_the_board(unit: Champion) -> bool:
    """Confirms that the given unit is positioned on the board by right-clicking the unit,
       and checking for the units name, if the unit's info window appears."""
    unit_board_position = identify_unit_board_position(unit)
    # Right-click the unit to make the unit's info appear on the right side of the screen.
    mk_functions.right_click(unit.coords)
    # Press s to prevent the tactician from moving anywhere.
    mk_functions.press_s()
    sleep(0.1)
    champ_name: str = ocr.get_text(screenxy=screen_coords.SELECTED_UNIT_NAME_POS.get_coords(),
                                   scale=3, psm=8, whitelist=ocr.ALPHABET_WHITELIST)
    # print(f"      OCR text: {champ_name}")
    champ_name = get_valid_champ(champ_name)
    # Click at the default location so that the unit's info disappears.
    mk_functions.left_click(screen_coords.DEFAULT_LOC.get_coords())
    if is_valid_champ(champ_name) and champ_name == unit.name:
        return True
    else:
        return False


def identify_unit_board_position(unit: Champion) -> int:
    unit_board_position = -1
    for index, vec2 in enumerate(screen_coords.BOARD_LOC):
        if vec2.get_coords() == unit.coords:
            unit_board_position = index
    print(f"    There is a {unit.name} unit located at board space {unit_board_position}.")
    return unit_board_position


def identify_one_space_on_the_board(tuple_board_space: tuple) -> str | None:
    """Tries to identify the name of the unit at the given vec2 coordinates, if a unit exists there."""
    # Right-click the board space to make the unit's info appear on the right side of the screen,
    # if a unit is located there.
    mk_functions.right_click(tuple_board_space)
    # Press s to prevent the tactician from moving anywhere.
    mk_functions.press_s()
    # sleep(0.1)
    champ_name: str = ocr.get_text(screenxy=screen_coords.SELECTED_UNIT_NAME_POS.get_coords(),
                                   scale=3, psm=8, whitelist=ocr.ALPHABET_WHITELIST)
    # print(f"      OCR text: {champ_name}")
    champ_name = get_valid_champ(champ_name)
    # Click at the default location so that the unit's info disappears.
    mk_functions.left_click(screen_coords.DEFAULT_LOC.get_coords())
    if is_valid_champ(champ_name):
        return champ_name
    else:
        return None


def move_unit(start_location: tuple, destination: tuple):
    """A function to make it easy to adjust all instances of moving a unit on the board."""
    mk_functions.left_click(start_location)
    sleep(0.1)
    mk_functions.move_mouse(destination)
    sleep(0.1)
    mk_functions.left_click(destination)


def move_item(start_location: tuple, destination: tuple):
    """A function to make it easy to adjust all instances of moving a item on the board."""
    mk_functions.left_click(start_location)
    sleep(0.1)
    mk_functions.move_mouse(destination)
    sleep(0.1)
    mk_functions.left_click(destination)


def identify_component_anvil(index: int) -> int:
    """Right-clicks a spot on the bench and if this can find the 'Component Anvil' text
       then it declares this spot on the bench as containing an anvil."""
    # setup coordinate values
    right_click_tuple = screen_coords.BENCH_LOC[index].get_coords()
    vec4_anvil = screen_coords.COMPONENT_ANVIL_TEXT_POS.get_coords()
    x_start = right_click_tuple[0] + vec4_anvil[0]
    y_start = right_click_tuple[1] + vec4_anvil[1]
    x_end = x_start + vec4_anvil[2]
    y_end = y_start + vec4_anvil[3]
    anvil_coords_tuple = (x_start, y_start, x_end, y_end)
    # grab text and validate
    mk_functions.right_click(right_click_tuple)
    mk_functions.press_s()  # make sure the tactician doesn't move around too much
    anvil_text: str = ocr.get_text(screenxy=anvil_coords_tuple, scale=3, psm=7,
                                   whitelist=ocr.ALPHABET_WHITELIST)
    if valid_anvil(anvil_text):
        return 1
    elif valid_ornn_anvil(anvil_text):
        return 2
    elif valid_tome_of_traits(anvil_text):
        return 3
    else:
        return 0


def valid_anvil(anvil_text: str) -> bool:
    """Checks if the anvil text passed in arg one matches 'Component Anvil'."""
    return anvil_text == "Component Anvil" or SequenceMatcher(a=anvil_text, b="Component Anvil").ratio() >= 0.7


def valid_ornn_anvil(anvil_text: str) -> bool:
    """Checks if the anvil text passed in arg one matches 'Component Anvil'."""
    return anvil_text == "Ornn Item Anvil" or SequenceMatcher(a=anvil_text, b="Ornn Item Anvil").ratio() >= 0.7


def valid_tome_of_traits(anvil_text: str) -> bool:
    """Checks if the anvil text passed in arg one matches 'Component Anvil'."""
    return anvil_text == "Tome of Traits" or SequenceMatcher(a=anvil_text, b="Tome of Traits").ratio() >= 0.7


def count_number_of_item_slots_filled_on_unit(unit: Champion):
    item_slots_filled = count_number_of_item_slots_filled_on_unit_at_coords(unit.coords)
    set_number_of_item_slot_filled_on_unit(unit, item_slots_filled)


def count_number_of_item_slots_filled_on_unit_at_coords(coordinates: tuple) -> int:
    """Assumes the unit actually exists. Opens the info panel on a unit and then hovers over
       the center of each item slot that displays in that screen. If the color of that slot is not close to black,
       then we assume the item slot is filled. As soon as the check fails, we find a color close to black,
       we can return how many items we've counted, because the item slots of a unit are filled up like a stack."""
    print(f"    Counting how many items are on the unit at {coordinates}.")
    item_slots_filled = 0
    mk_functions.right_click(coordinates)
    mk_functions.press_s()
    # Search the unit's item slots from left to right.
    THRESHOLD_VALUE = 8
    for positions in screen_coords.UNIT_INFO_MENU_ITEM_SLOTS_POS:
        screen_capture = ImageGrab.grab(bbox=positions.get_coords())
        screenshot_array = np.array(screen_capture)
        if not (np.abs(screenshot_array - (0, 0, 0)) <= THRESHOLD_VALUE).all(axis=2).any():
            item_slots_filled += 1
        else:
            return item_slots_filled
    return item_slots_filled


def set_number_of_item_slot_filled_on_unit(unit: Champion, item_slots_filled: int):
    print(f"  {unit.name} has had their number of item-slots-filled set from {unit.item_slots_filled} to {item_slots_filled}.")
    unit.item_slots_filled = item_slots_filled


def is_valid_trait_item(trait_item: str) -> str | None:
    for valid_trait_item in game_assets.TRAIT_ITEMS:
        if trait_item in game_assets.TRAIT_ITEMS or SequenceMatcher(a=valid_trait_item, b=trait_item).ratio() >= 0.7:
            print(f"    Trait Item {trait_item} -- matched with -- Valid Trait Item: {valid_trait_item}")
            return valid_trait_item
    if len(trait_item) > 3:
        print(f"  [!] The item {trait_item} did not match any items in game_assets.TRAIT_ITEMS!")


def identify_emblem_name(screen_capture: ImageGrab.Image, name_pos: Vec4, shop_pos: int, shop_array: list) -> str:
    """Returns a tuple containing the shop position and champion name"""
    trait_item: str = screen_capture.crop(name_pos.get_coords())
    trait_item: str = ocr.get_text_from_image(image=trait_item, whitelist="")
    shop_array.append((shop_pos, is_valid_trait_item(trait_item)))


def identify_emblems_in_shop() -> list[str]:
    """Make a list of the Emblems that appear in the Tome of Traits shop and return it."""
    screen_capture = ImageGrab.grab(bbox=screen_coords.TOME_OF_TRAITS_SHOP_POS.get_coords())
    emblem_shop: list = []
    thread_list: list = []
    for shop_index, name_pos in enumerate(screen_coords.TOME_OF_TRAITS_SHOP_NAMES_POS):
        thread = threading.Thread(target=identify_emblem_name, args=(screen_capture, name_pos, shop_index, emblem_shop))
        thread_list.append(thread)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    return emblem_shop


def was_moving_unit_successful(destination: tuple) -> bool:
    print("  Checking if moving the unit was successful.")
    mk_functions.right_click(destination)
    unit_name = identify_one_space_on_the_board(destination)
    if unit_name is not None:
        return True
    else:
        return False


def get_valid_augment(augment_name: str) -> str:
    """Matches champion string to a valid champion name string and returns it"""
    if augment_name in game_assets.ALL_AUGMENTS:
        return augment_name
    for augment in game_assets.ALL_AUGMENTS:
        if SequenceMatcher(a=augment, b=augment_name).ratio() >= 0.7:
            return augment
    if augment_name is not None and len(augment_name) > 0:
        print(f"  [!] The augment_name {augment_name} did not match any unit in game_assets.ALL_AUGMENTS!")
    return ""


def has_enough_gold_to_purchase_xp(minimum_amount_of_gold_to_buy_xp: int):
    if get_gold() >= minimum_amount_of_gold_to_buy_xp:
        return True
    else:
        return False


def has_enough_gold_to_reroll_shop(minimum_amount_of_gold_to_reroll_shop: int):
    if get_gold() >= minimum_amount_of_gold_to_reroll_shop:
        return True
    else:
        return False
