"""
Functions used by the Game class to retrieve relevant data
"""

from time import sleep
from PIL import ImageGrab
import screen_coords
import ocr
import game_assets
import mk_functions
from typing import Any

import cv2 as cv
import numpy as np
from PIL import ImageGrab

import pydirectinput


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
def image_resize(image: int, scale: int) -> Any:
    """Resizes the image using the scale passed in argument two"""
    (width, height) = (image.width * scale, image.height * scale)
    return image.resize((width, height))

def matrix_resize(image: int, scale: int) -> Any:
    """Resizes the matrix using the scale passed in argument two"""
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    dim = (width, height)

    # resize image
    resized = cv.resize(image, dim, interpolation=cv.INTER_AREA)
    return resized

def pickup_items() -> None:  # Refacor this function to make it more clear whats happening
    """Picks up items from the board after PVE round"""
    how_meny_times_pickup_items = 3
    for x in range(how_meny_times_pickup_items):
        board_image_should_be_increased_by = 3
        orb_image_should_be_increased_by = 2.5

        # Get screenshot and process image
        scene = ImageGrab.grab(bbox=screen_coords.PLACE_WHERE_ORBS_FALL.get_coords())
        scene = image_resize(scene, board_image_should_be_increased_by)
        scene = np.array(scene)
        # Download the pattern of the orb and process image
        wanted_orb_picture = cv.imread(r'./assets/OrbQuestionMark.PNG')
        wanted_orb_picture = matrix_resize(wanted_orb_picture, 2.5)

        # Find useful elements
        _, w, h = wanted_orb_picture.shape[::-1]
        scene_r, scene_g, scene_b = cv.split(scene)
        wanted_orb_picture_r, wanted_orb_picture_g, wanted_orb_picture_b = cv.split(wanted_orb_picture)

        # Find an orb on the board
        res = cv.matchTemplate(scene_g, wanted_orb_picture_g, cv.TM_CCORR_NORMED)

        # Prepare the data to read the position of the orb on the bord
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        top_left = max_loc

        main_image_offset_x = screen_coords.PLACE_WHERE_ORBS_FALL.x_pos
        main_image_offset_y = screen_coords.PLACE_WHERE_ORBS_FALL.y_pos

        real_orb_width = int((int(w / orb_image_should_be_increased_by) / 2))
        real_orb_height = int((int(h / orb_image_should_be_increased_by) / 2))

        real_image_width = int((top_left[0] / board_image_should_be_increased_by))
        real_image_height = int((top_left[1] / board_image_should_be_increased_by))

        # Click where the orb is
        pydirectinput.moveTo(real_image_width + main_image_offset_x + real_orb_width,
                             real_image_height + main_image_offset_y + real_orb_height)
        pydirectinput.mouseDown(button='right')
        pydirectinput.mouseUp(button='right')

        # Wait for the character to move to this place
        sleep(3)
    # Back to start position
    mk_functions.right_click(screen_coords.StartPosision.get_coords())

def get_champ_carousel(tft_round: str) -> None:
    """Gets a champion from the carousel"""
    while tft_round == get_round():
        mk_functions.right_click(screen_coords.CAROUSEL_LOC.get_coords())
        sleep(0.7)


def check_alive() -> bool:  # Refactor this function to use API
    """Checks the screen to see if player is still alive"""
    if ocr.get_text(screenxy=screen_coords.EXIT_NOW_POS.get_coords(), scale=3, psm=7) == 'EXIT NOW':
        return False
    if ocr.get_text(screenxy=screen_coords.VICTORY_POS.get_coords(), scale=3, psm=7) == 'CONTINUE':
        return False
    return True


def select_shop() -> None:
    """Clicks the take all button on special round"""
    mk_functions.left_click(screen_coords.TAKE_ALL_BUTTON.get_coords())


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
