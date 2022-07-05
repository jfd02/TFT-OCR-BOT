"""
Vec4 class that handles box screen coordinates
Transformations related to the game position & game size happen here
  x,y
   *----------------*
   |                |
   *----------------*
                x+w, y+h
"""

class vec4:
    screen_x_offset = 0
    screen_y_offset = 0
    screen_x_scale = 1
    screen_y_scale = 1

    def __init__(self, x, y, w, h, use_screen_offset: bool = True):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.use_screen_offset = use_screen_offset

    def get_coords(self) -> tuple:
        x = self.x * vec4.screen_x_scale
        y = self.y * vec4.screen_y_scale
        w = self.w * vec4.screen_x_scale
        h = self.h * vec4.screen_y_scale

        if self.use_screen_offset:
            return (round(x + vec4.screen_x_offset), round(y + vec4.screen_y_offset), round(w + vec4.screen_x_offset), round(h + vec4.screen_y_offset))

        return (round(x), round(y), round(w), round(h))

    @classmethod
    def setup_screen(cls, x, y, w, h):
        vec4.screen_x_offset = x
        vec4.screen_y_offset = y
        vec4.screen_x_scale = w / 1920
        vec4.screen_y_scale = h / 1080
