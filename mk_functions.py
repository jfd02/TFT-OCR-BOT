"""
Handles sending input to the game
"""

import random
import pydirectinput

def left_click(coords_tuple):
    offset = random.randint(-3, 3)
    pydirectinput.moveTo(coords_tuple[0] - offset, coords_tuple[1] - offset)
    pydirectinput.mouseDown()
    pydirectinput.mouseUp()

def right_click(coords_tuple):
    offset = random.randint(-3, 3)
    pydirectinput.moveTo(coords_tuple[0]- offset, coords_tuple[1] - offset)
    pydirectinput.mouseDown(button='right')
    pydirectinput.mouseUp(button='right')

def press_e(coords_tuple):
    offset = random.randint(-3, 3)
    pydirectinput.moveTo(coords_tuple[0] - offset, coords_tuple[1] - offset)
    pydirectinput.press("e")

def move_mouse(coords_tuple):
    pydirectinput.moveTo(coords_tuple[0], coords_tuple[1])

def buy_xp():
    pydirectinput.press("f")

def reroll():
    pydirectinput.press("d")

def press_esc():
    pydirectinput.press("esc")
