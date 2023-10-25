# Original code from the TFT_OCR_BOT repository on GitHub:
# Repository URL: https://github.com/jfd02/TFT-OCR-BOT
# Original authors:
# - @jfd02
# - @danparizher
# Modified by the-user-created
#

"""
Handles sending input to the game; coords contain a cartesian ordered pair (x, y)
"""

import random
import platform

if platform.system() == 'Darwin':
    import pyautogui
else:
    import pydirectinput


def left_click(coords: tuple) -> None:
    """Left clicks at argument ones coordinates"""
    offset: int = random.randint(-3, 3)

    if platform.system() == 'Darwin':
        pyautogui.moveTo(coords[0] - offset, coords[1] - offset)
        pyautogui.click()
        return

    pydirectinput.moveTo(coords[0] - offset, coords[1] - offset)
    pydirectinput.mouseDown()
    pydirectinput.mouseUp()


def right_click(coords: tuple) -> None:
    """Right-clicks at argument ones coordinates"""
    offset: int = random.randint(-3, 3)

    if platform.system() == 'Darwin':
        pyautogui.moveTo(coords[0] - offset, coords[1] - offset)
        pyautogui.click(button='right')
        return

    pydirectinput.moveTo(coords[0] - offset, coords[1] - offset)
    pydirectinput.mouseDown(button="right")
    pydirectinput.mouseUp(button="right")


def press_e(coords: tuple) -> None:
    """Presses e at argument ones coordinates"""
    offset: int = random.randint(-3, 3)

    if platform.system() == 'Darwin':
        pyautogui.moveTo(coords[0] - offset, coords[1] - offset)
        pyautogui.press("e")
        return

    pydirectinput.moveTo(coords[0] - offset, coords[1] - offset)
    pydirectinput.press("e")


def move_mouse(coords: tuple) -> None:
    """Moves mouse to argument ones coordinates"""
    if platform.system() == 'Darwin':
        pyautogui.moveTo(coords[0], coords[1])
        return

    pydirectinput.moveTo(coords[0], coords[1])


def buy_xp() -> None:
    """Presses hotkey to purchase XP"""
    if platform.system() == 'Darwin':
        pyautogui.press("f")
        return

    pydirectinput.press("f")


def reroll() -> None:
    """Presses hotkey to purchase reroll"""
    if platform.system() == 'Darwin':
        pyautogui.press("d")
        return

    pydirectinput.press("d")


def press_esc() -> None:
    """Presses escape key"""
    if platform.system() == 'Darwin':
        pyautogui.press("esc")
        return

    pydirectinput.press("esc")
