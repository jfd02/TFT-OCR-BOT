
class vec4:
    screen_x_offset = 0
    screen_y_offset = 0

    def __init__(self, x, y, w, h, use_screen_offset: bool = True):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.use_screen_offset = use_screen_offset

    def get_coords(self) -> tuple:
        if self.use_screen_offset:
            return (self.x + vec4.screen_x_offset, self.y + vec4.screen_y_offset, self.w + vec4.screen_x_offset, self.h + vec4.screen_y_offset)
            
        return (self.x, self.y, self.w, self.h)