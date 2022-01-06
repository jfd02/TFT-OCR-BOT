import pydirectinput


def left_click(coords_tuple):
    pydirectinput.moveTo(coords_tuple[0], coords_tuple[1])
    pydirectinput.mouseDown()
    pydirectinput.mouseUp()


def right_click(coords_tuple):
    pydirectinput.moveTo(coords_tuple[0], coords_tuple[1])
    pydirectinput.mouseDown(button='right')
    pydirectinput.mouseUp(button='right')


def press_e(coords_tuple):
    pydirectinput.moveTo(coords_tuple[0], coords_tuple[1])
    pydirectinput.press("e")


def move_mouse(coords_tuple):
    pydirectinput.moveTo(coords_tuple[0], coords_tuple[1])


def buy_xp():
    pydirectinput.press("f")


def reroll():
    pydirectinput.press("d")
