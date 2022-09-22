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
    screen_x_offset: int = 0
    screen_y_offset: int = 0
    screen_x_scale: int = 1
    screen_y_scale: int = 1

    def __init__(self, game_window: GameWindow, use_screen_offset: bool = True) -> None:
        self.x_pos: int = game_window.x_pos
        self.y_pos: int = game_window.y_pos
        self.width: int = game_window.width
        self.height: int = game_window.height
        self.use_screen_offset: bool = use_screen_offset

    def get_coords(self) -> tuple:
        """Returns screen coordinates with transformations"""
        x_pos: int = self.x_pos * Vec4.screen_x_scale
        y_pos: int = self.y_pos * Vec4.screen_y_scale
        width: int = self.width * Vec4.screen_x_scale
        height: int = self.height * Vec4.screen_y_scale

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
