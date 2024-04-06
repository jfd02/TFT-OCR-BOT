"""
Functions used by the Game class to retrieve relevant data
"""

from time import sleep
from PIL import ImageGrab
import screen_coords
import ocr
import game_assets
import mk_functions


def get_round() -> list[str, int]:
    """Gets the current game round"""
    screen_capture = ImageGrab.grab(bbox=screen_coords.ROUND_POS.get_coords())
    round_three = screen_capture.crop(screen_coords.ROUND_POS_THREE.get_coords())
    game_round: str = ocr.get_text_from_image(image=round_three, whitelist=ocr.ROUND_WHITELIST)
    if game_round in game_assets.ROUNDS:
        return [game_round, 3]

    round_two = screen_capture.crop(screen_coords.ROUND_POS_TWO.get_coords())
    game_round: str = ocr.get_text_from_image(image=round_two, whitelist=ocr.ROUND_WHITELIST)
    if game_round in game_assets.ROUNDS:
        return [game_round, 2]

    round_one = screen_capture.crop(screen_coords.ROUND_POS_ONE.get_coords())
    game_round: str = ocr.get_text_from_image(image=round_one, whitelist=ocr.ROUND_WHITELIST)
    if game_round in game_assets.ROUNDS:
        return [game_round, 1]
    return ["999-999",0]


def check_encounter_round() -> list[str]:
    """Get the game round list by checking round text for encounter add rounds"""
    round_list: list = []
    for positions in screen_coords.ROUND_ENCOUNTER_ICON_POS:
        mk_functions.move_mouse(positions[0].get_coords())
        round_message: str = ocr.get_text(
            screenxy=positions[1].get_coords(),
            scale=3,
            psm=7,
            whitelist=(ocr.ALPHABET_WHITELIST + " "),
        )
        if any(keyword in round_message for keyword in ["Carousel"]):
            round_list.append("carousel")
        elif any(keyword in round_message for keyword in ["Get pulled into an Encounter"]):
            round_list.append("encounter")
        elif any(keyword in round_message for keyword in ["Krugs", "Murk Wolves", "Raptors", "Elder Dragon"]):
            round_list.append("pve")
        else:
            round_list.append("pvp")
    mk_functions.move_mouse(screen_coords.DEFAULT_LOC.get_coords())
    return round_list

def pickup_items() -> None:  # Refacor this function to make it more clear whats happening
    """Picks up items from the board after PVP round"""
    for index, coords in enumerate(screen_coords.ITEM_PICKUP_LOC):
        mk_functions.right_click(coords.get_coords())
        if index == 7:  # Don't need to sleep on final click
            return
        if index == 0:
            sleep(1.2)
        if index % 2 == 0:
            sleep(2)
        else:
            sleep(1.2)


def get_champ_carousel(tft_round: str) -> None:
    """Gets a champion from the carousel"""
    while tft_round == get_round()[0]:
        mk_functions.right_click(screen_coords.CAROUSEL_LOC.get_coords())
        sleep(0.7)
    sleep(3)


def check_alive() -> bool:    # Refactor this function to use API
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
