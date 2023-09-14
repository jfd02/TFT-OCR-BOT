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
    pydirectinput.mouseDown(button="right")
    pydirectinput.mouseUp(button="right")


def press_e(coords: tuple) -> None:
    """Presses e at argument ones coordinates. Pressing e allows the player to sell units."""
    offset: int = random.randint(-3, 3)
    pydirectinput.moveTo(coords[0] - offset, coords[1] - offset)
    pydirectinput.press("e")


def press_s() -> None:
    """Presses s. Pressing s stop the movement of the tactician."""
    pydirectinput.press("s")

def press_w(coords: tuple) -> None:
    """Presses w. Moves a unit from the bench to the board or the board to the bench."""
    offset: int = random.randint(-3, 3)
    pydirectinput.moveTo(coords[0] - offset, coords[1] - offset)
    pydirectinput.press("w")


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


def hold_down_right_mouse_button() -> None:
    """Simulates a human holding down the right mouse button, without releasing it."""
    print("[   Holding Down the Right Mouse Button   ]")
    pydirectinput.mouseDown(button='right')


def release_right_mouse_button() -> None:
    """Simulates a human releasing the right mouse button, after it has been pushed down."""
    print("[   Releasing the Right Mouse Button   ]")
    pydirectinput.mouseUp(button='right')
