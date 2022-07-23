"""
Vector2 that handles point screen coordinates
Transformations related to the game position & game size happen here
"""

class vec2:
    screen_x_offset = 0
    screen_y_offset = 0
    screen_x_scale = 1
    screen_y_scale = 1 

    def __init__(self, x, y, use_screen_offset: bool = True):
        self.x = x
        self.y = y
        self.use_screen_offset = use_screen_offset

    def get_coords(self) -> tuple:
        x = self.x * vec2.screen_x_scale
        y = self.y * vec2.screen_y_scale

        if self.use_screen_offset:
            return (round(x + vec2.screen_x_offset), round(y + vec2.screen_y_offset))
        return (round(x), round(y))

    @classmethod
    def setup_screen(cls, x, y, w, h):
        vec2.screen_x_offset = x
        vec2.screen_y_offset = y
        vec2.screen_x_scale = w / 1920
        vec2.screen_y_scale = h / 1080
