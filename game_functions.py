"""
Functions used by the Game class to retrieve relevant data
"""
from difflib import SequenceMatcher
from time import sleep
from PIL import ImageGrab

import arena_functions
import comps
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
    mk_functions.right_click(screen_coords.TACTICIAN_RESTING_SPOT_LOC.get_coords())
    # self.message_queue.put(("LABEL", labels))


def pickup_items() -> None:  # Refactor this function to make it more clear what's happening
    """Picks up items from the board after PVP round"""
    for index, coords in enumerate(screen_coords.ITEM_PICKUP_LOC):
        if do_we_have_too_many_items_popup():
            mk_functions.right_click(screen_coords.TACTICIAN_RESTING_SPOT_LOC.get_coords())
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


def pick_up_items_holding_down_right_click() -> None:
    """Holds down the right-click button and moves the tactician in an arc around the board
       as item orbs should fall in a sort-of circle shape. Releases the right-click mouse button
       when it reaches the end of the arc.
       This should speed up grabbing compared to the game_functions.pickup_items(),
       though picking up items should still be reworked to read the question marks and move directly to the orbs."""
    mk_functions.move_mouse(screen_coords.TACTICIAN_RESTING_SPOT_LOC.get_coords())
    mk_functions.hold_down_right_mouse_button()
    for index, coords in enumerate(screen_coords.ITEM_PICKUP_DRAGGING_MOUSE_LOC):
        if do_we_have_too_many_items_popup():
            mk_functions.release_right_mouse_button()
            mk_functions.right_click(screen_coords.TACTICIAN_RESTING_SPOT_LOC.get_coords())
            sleep(2)
            return
        else:
            mk_functions.move_mouse(coords.get_coords())
            if index == 0:
                sleep(1.5)  # need more time to set the tactician in the correct starting position
            else:
                sleep(0.8)  # 0.6 is too little sometimes.
    # Hopefully we went in the complete arc and picked up all items.
    mk_functions.release_right_mouse_button()
    mk_functions.move_mouse(screen_coords.TACTICIAN_RESTING_SPOT_LOC.get_coords())


def do_we_have_too_many_items_popup() -> bool:
    # print("  Double-checking that a pop-up saying we have too many items isn't appearing.")
    too_much_loot_popup = ocr.get_text(screenxy=screen_coords.TOO_MUCH_LOOT_POS.get_coords(), scale=3, psm=7)
    # print(f"    OCR found: {too_much_loot_popup}")
    text_to_match = "Loot contains more"
    if too_much_loot_popup == text_to_match or SequenceMatcher(a=text_to_match, b=too_much_loot_popup).ratio() >= 0.7:
        print("    We can't pick up anymore items.")
        return True
    return False


def get_champ_carousel(tft_round: str) -> None:
    """Gets a champion from the carousel"""
    while tft_round == get_round():
        mk_functions.right_click(screen_coords.CAROUSEL_LOC.get_coords())
        sleep(1.0)


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
    mk_functions.left_click(screen_coords.EXIT_NOW_LOC.get_coords())  # done twice in case the game wasn't the focused window.
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


def pick_a_random_comp_to_play():
    """Make the bot play a random comp from the comps we have created."""
    random_comp = comps.return_random_comp()
    comp_to_play = comps.Comp(random_comp)
    print(f"B.O.T. has decided to play {comp_to_play.name}")
    return comp_to_play
