
class vec2:
    screen_x_offset = 0
    screen_y_offset = 0

    def __init__(self, x, y, use_screen_offset: bool = True):
        self.x = x
        self.y = y
        self.use_screen_offset = use_screen_offset

    def get_coords(self) -> tuple:
        if self.use_screen_offset:
            return (self.x + vec2.screen_x_offset, self.y + vec2.screen_y_offset)
        return (self.x, self.y)