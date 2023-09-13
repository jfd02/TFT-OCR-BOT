"""
Functions used by the Game class to retrieve relevant data
"""
from difflib import SequenceMatcher
from time import sleep
from PIL import ImageGrab

import arena_functions
import screen_coords
import ocr
from set_9_5 import game_assets
import mk_functions


def get_round() -> str:
    """Gets the current game round"""
    screen_capture = ImageGrab.grab(bbox=screen_coords.ROUND_POS.get_coords())
    round_two = screen_capture.crop(screen_coords.ROUND_POS_TWO.get_coords())
    game_round: str = ocr.get_text_from_image(image=round_two, whitelist=ocr.ROUND_WHITELIST)
    if game_round in game_assets.ROUNDS:
        return game_round

    round_one = screen_capture.crop(screen_coords.ROUND_POS_ONE.get_coords())
    game_round: str = ocr.get_text_from_image(image=round_one, whitelist=ocr.ROUND_WHITELIST)
    return game_round


def move_to_items_orbs_on_board():
    """Attempts to move the tactician to any item orbs that are on the board."""
    print("    Trying to move directly to the item orbs:")
    # labels = []
    item_orb_vec2_list = arena_functions.get_center_position_of_item_orbs()
    if len(item_orb_vec2_list) == 0:
        print("      The OCR didn't register any items on the board.")
    for item_orb_vec2 in item_orb_vec2_list:
        print(f"      item_orb_vec2: {item_orb_vec2}")
        print(f"        Coordinates: {item_orb_vec2.get_coords()}")
        # labels.append((f"?", item_orb_vec2.get_coords(), 0, 0))
        mk_functions.right_click(item_orb_vec2.get_coords())
        sleep(2)
    # Move the tactician back to their pedestal after looting items.
    mk_functions.right_click(screen_coords.TACTICIAN_RESTING_SPOT.get_coords())
    # self.message_queue.put(("LABEL", labels))


def pickup_items() -> None:  # Refactor this function to make it more clear what's happening
    """Picks up items from the board after PVP round"""
    for index, coords in enumerate(screen_coords.ITEM_PICKUP_LOC):
        if do_we_have_too_many_items_popup():
            mk_functions.right_click(screen_coords.TACTICIAN_RESTING_SPOT.get_coords())
            sleep(2)
            return
        mk_functions.right_click(coords.get_coords())
        if index == 7:
            sleep(1) #  give more time for the bot to reach the top-left of the screen
            return
        if index == 0:
            sleep(1.2)
        if index % 2 == 0:
            sleep(2)
        else:
            sleep(1.2)


def do_we_have_too_many_items_popup() -> bool:
    too_much_loot_popup = ocr.get_text(screenxy=screen_coords.TOO_MUCH_LOOT.get_coords(), scale=3, psm=7)
    text_to_match = "Loot contains more"
    if too_much_loot_popup == text_to_match or SequenceMatcher(a=text_to_match, b=too_much_loot_popup).ratio() >= 0.7:
        print("    We can't pick up anymore items.")
        return True
    return False


def get_champ_carousel(tft_round: str) -> None:
    """Gets a champion from the carousel"""
    while tft_round == get_round():
        mk_functions.right_click(screen_coords.CAROUSEL_LOC.get_coords())
        sleep(0.7)


def check_alive() -> bool:  # Refactor this function to use API
    """Checks the screen to see if player is still alive"""
    if ocr.get_text(screenxy=screen_coords.EXIT_NOW_POS.get_coords(), scale=3, psm=7) == 'EXIT NOW':
        return False
    return (
            ocr.get_text(
                screenxy=screen_coords.VICTORY_POS.get_coords(), scale=3, psm=7
            )
            != 'CONTINUE'
    )


def exit_game() -> None:
    """Exits the game"""
    mk_functions.left_click(screen_coords.EXIT_NOW_LOC.get_coords())
    print("  Sleeping so that we can take a look at the end game screen.")
    sleep(25)  # sleep for 25 seconds to add time between games, so that the end-game screen can show.


def default_pos() -> None:
    """Moves the mouse to a default position to ensure no data is being blocked from OCR"""
    mk_functions.left_click(screen_coords.DEFAULT_LOC.get_coords())


def forfeit() -> None:
    """Forfeits the game"""
    mk_functions.press_esc()
    mk_functions.left_click(screen_coords.SURRENDER_LOC.get_coords())
    sleep(0.1)
    mk_functions.left_click(screen_coords.SURRENDER_TWO_LOC.get_coords())
    sleep(1)
