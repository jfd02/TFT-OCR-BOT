"""
Handles sending input to the game, coords contain a cartesian ordered pair (x, y)
"""

import random
import pydirectinput


def left_click(coords: tuple) -> None:
    """Left clicks at argument ones coordinates"""
    offset: int = random.randint(-3, 3)
    pydirectinput.moveTo(coords[0] - offset, coords[1] - offset)
    pydirectinput.mouseDown()
    pydirectinput.mouseUp()


def right_click(coords: tuple) -> None:
    """Right clicks at argument ones coordinates"""
    offset: int = random.randint(-3, 3)
    pydirectinput.moveTo(coords[0] - offset, coords[1] - offset)
    pydirectinput.mouseDown(button='right')
    pydirectinput.mouseUp(button='right')


def press_e(coords: tuple) -> None:
    """Presses e at argument ones coordinates"""
    offset: int = random.randint(-3, 3)
    pydirectinput.moveTo(coords[0] - offset, coords[1] - offset)
    pydirectinput.press("e")


def move_mouse(coords: tuple) -> None:
    """Moves mouse to argument ones coordinates"""
    pydirectinput.moveTo(coords[0], coords[1])


def buy_xp() -> None:
    """Presses hotkey to purchase XP"""
    pydirectinput.press("f")


def reroll() -> None:
    """Presses hotkey to purchase reroll"""
    pydirectinput.press("d")


def press_esc() -> None:
    """Presses escape key"""
    pydirectinput.press("esc")
