"""
Vector2 that handles point screen coordinates
Transformations related to the game position & game size happen here
"""

class Vec2:
    "Vector 2 class that has methods to scale screen coordinates"

    screen_x_offset: int = 0
    screen_y_offset: int = 0
    screen_x_scale: int = 1
    screen_y_scale: int = 1

    def __init__(self, x_pos, y_pos, use_screen_offset: bool = True) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.use_screen_offset: bool = use_screen_offset

    def get_coords(self) -> tuple:
        """Returns screen coordinates with transformations"""
        x_pos = self.x_pos * Vec2.screen_x_scale
        y_pos = self.y_pos * Vec2.screen_y_scale

        if self.use_screen_offset:
            return (round(x_pos + Vec2.screen_x_offset),
                    round(y_pos + Vec2.screen_y_offset))

        return (round(x_pos), round(y_pos))

    @classmethod
    def setup_screen(cls, x_pos: int, y_pos: int, width: int, height: int) -> None:
        """Setup for screen coordinate offset and scale"""
        Vec2.screen_x_offset = x_pos
        Vec2.screen_y_offset = y_pos
        Vec2.screen_x_scale = width / 1920
        Vec2.screen_y_scale = height / 1080
