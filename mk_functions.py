"""
Handles sending input to the game, coords contain a cartesian ordered pair (x, y)
"""

import random
import pydirectinput

def left_click(coords: tuple) -> None:
    """Simulate a left click at the specified coordinates.

    Args:
        coords (tuple): A tuple containing cartesian coordinates (x, y).
    """
    offset: int = random.randint(-3, 3)
    pydirectinput.moveTo(coords[0] - offset, coords[1] - offset)
    pydirectinput.mouseDown()
    pydirectinput.mouseUp()

def right_click(coords: tuple) -> None:
    """Simulate a right click at the specified coordinates.

    Args:
        coords (tuple): A tuple containing cartesian coordinates (x, y).
    """
    offset: int = random.randint(-3, 3)
    pydirectinput.moveTo(coords[0] - offset, coords[1] - offset)
    pydirectinput.mouseDown(button="right")
    pydirectinput.mouseUp(button="right")

def press_e(coords: tuple) -> None:
    """Simulate pressing the 'e' key at the specified coordinates.

    Args:
        coords (tuple): A tuple containing cartesian coordinates (x, y).
    """
    offset: int = random.randint(-3, 3)
    pydirectinput.moveTo(coords[0] - offset, coords[1] - offset)
    pydirectinput.press("e")

def move_mouse(coords: tuple) -> None:
    """Move the mouse to the specified coordinates.

    Args:
        coords (tuple): A tuple containing cartesian coordinates (x, y).
    """
    pydirectinput.moveTo(coords[0], coords[1])

def buy_xp() -> None:
    """Simulate pressing the 'f' key to purchase XP."""
    pydirectinput.press("f")

def reroll() -> None:
    """Simulate pressing the 'd' key to purchase a reroll."""
    pydirectinput.press("d")

def press_esc() -> None:
    """Simulate pressing the 'esc' key."""
    pydirectinput.press("esc")

def press_enter() -> None:
    """Simulate pressing the 'enter' key."""
    pydirectinput.press("enter")

def press_slash() -> None:
    """Simulate pressing the '/' key."""
    pydirectinput.press("/")

def press_f() -> None:
    """Simulate pressing the 'f' key."""
    pydirectinput.press("f")
