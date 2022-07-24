"""
Handles sending input to the game
"""

import random
import pydirectinput

def left_click(coords: tuple) -> None:
    offset = random.randint(-3, 3)
    pydirectinput.moveTo(coords[0] - offset, coords[1] - offset)
    pydirectinput.mouseDown()
    pydirectinput.mouseUp()

def right_click(coords: tuple) -> None:
    offset = random.randint(-3, 3)
    pydirectinput.moveTo(coords[0]- offset, coords[1] - offset)
    pydirectinput.mouseDown(button='right')
    pydirectinput.mouseUp(button='right')

def press_e(coords: tuple) -> None:
    offset = random.randint(-3, 3)
    pydirectinput.moveTo(coords[0] - offset, coords[1] - offset)
    pydirectinput.press("e")

def move_mouse(coords: tuple) -> None:
    pydirectinput.moveTo(coords[0], coords[1])

def buy_xp() -> None:
    pydirectinput.press("f")

def reroll() -> None:
    pydirectinput.press("d")

def press_esc() -> None:
    pydirectinput.press("esc")
