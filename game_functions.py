# Original code from the TFT_OCR_BOT repository on GitHub:
# Repository URL: https://github.com/jfd02/TFT-OCR-BOT
# Original authors:
# - @jfd02
# - @danparizher
# - @anthony5301
# Modified by the-user-created
#

"""
Functions used by the Game class to retrieve relevant data
"""

from time import sleep
import cv2
from PIL import ImageGrab
import numpy as np
import screen_coords
import ocr
import game_assets
import mk_functions
from math import sqrt


def get_round() -> str:
    """Gets the current game round"""
    screen_capture = ImageGrab.grab(bbox=screen_coords.ROUND_POS.get_coords())
    # Round 2+ has a different position on screen than round 1-x, so we check round two first
    round_two = screen_capture.crop(screen_coords.ROUND_POS_TWO.get_coords())
    game_round: str = ocr.get_text_from_image(image=round_two, whitelist=ocr.ROUND_WHITELIST)
    if game_round in game_assets.ROUNDS:
        return game_round

    round_one = screen_capture.crop(screen_coords.ROUND_POS_ONE.get_coords())
    game_round: str = ocr.get_text_from_image(image=round_one, whitelist=ocr.ROUND_WHITELIST)
    return game_round


def get_centers(template_path: str, image: np.ndarray) -> list[tuple[int, int]]:
    """Gets the centers of the circles on the board"""
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    centers = ocr.find_circle_centers(image=image, template=template)
    return filter_circle_centers(centers=centers)


def pickup_items() -> None:
    """Picks up items from the board after PVP round"""
    # TODO: This is not perfect, it occasionally misses orbs due to obstructions preventing cv2 from matching
    #  the template.
    #  Also haven't tested for yellow orbs yet

    # Screenshot the board, convert to a numpy array (for cv2), and convert to grayscale
    screen_capture = np.array(ImageGrab.grab(bbox=screen_coords.BOARD_AREA.get_coords()).convert('L'))
    # Save the image to disk for debugging
    cv2.imwrite("ProgramFiles/screen_capture.png", screen_capture)

    # Load and process templates
    blue_centers = get_centers("ProgramFiles/blueTemplate.png", screen_capture)
    gray_centers = get_centers("ProgramFiles/grayTemplate.png", screen_capture)

    # Adjust the centers to the correct position on screen
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

    # Move through the shortest path
    for step in shortest_route:
        mk_functions.right_click(coords=step)
        sleep(2.0)


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


def filter_circle_centers(centers):
    unique_centers = []
    for center in centers:
        if not any(
                [np.linalg.norm(np.array(center) - np.array(unique_center)) < 10 for unique_center in unique_centers]
        ):
            unique_centers.append(center)
    return unique_centers


def get_champ_carousel(tft_round: str) -> None:
    """Gets a champion from the carousel"""
    while tft_round == get_round():
        mk_functions.right_click(screen_coords.CAROUSEL_LOC.get_coords())
        sleep(0.7)


def check_alive() -> bool:    # Refactor this function to use API
    """Checks the screen to see if the player is still alive"""
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


def default_tactician_pos() -> None:
    """Moves the mouse to the default tactician position"""
    mk_functions.right_click(screen_coords.DEFAULT_TACTICIAN_LOC.get_coords())