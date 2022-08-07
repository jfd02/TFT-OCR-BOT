"""
Vector4 class that handles box screen coordinates
Transformations related to the game position & game size happen here
  x,y
   *----------------*
   |                |
   *----------------*
                x+w, y+h
"""

from dataclasses import dataclass

@dataclass
class GameWindow:
    """Struct that contains information about the game window size and position"""
    x_pos: int
    y_pos: int
    width: int
    height: int


class Vec4:
    "Vector 4 class that has methods to scale screen coordinates"
    screen_x_offset = 0
    screen_y_offset = 0
    screen_x_scale = 1
    screen_y_scale = 1

    def __init__(self, game_window: GameWindow, use_screen_offset: bool = True):
        self.x_pos = game_window.x_pos
        self.y_pos = game_window.y_pos
        self.width = game_window.width
        self.height = game_window.height
        self.use_screen_offset = use_screen_offset

    def get_coords(self) -> tuple:
        """Returns screen coordinates with transformations"""
        x_pos = self.x_pos * Vec4.screen_x_scale
        y_pos = self.y_pos * Vec4.screen_y_scale
        width = self.width * Vec4.screen_x_scale
        height = self.height * Vec4.screen_y_scale

        if self.use_screen_offset:
            return (round(x_pos + Vec4.screen_x_offset),
                    round(y_pos + Vec4.screen_y_offset),
                    round(width + Vec4.screen_x_offset),
                    round(height + Vec4.screen_y_offset))

        return (round(x_pos), round(y_pos), round(width), round(height))

    @classmethod
    def setup_screen(cls, x_pos: int, y_pos: int, width: int, height: int) -> None:
        """Setup for screen coordinate offset and scale"""
        Vec4.screen_x_offset = x_pos
        Vec4.screen_y_offset = y_pos
        Vec4.screen_x_scale = width / 1920
        Vec4.screen_y_scale = height / 1080
