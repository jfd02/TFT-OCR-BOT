"""
The champion class contains all information related to an individual board slot used by the bot
"""

class Champion:
    def __init__(self, name, coords, build, slot, size, final_comp):
        self.name = name
        self.coords = coords
        self.build = build
        self.index = slot
        self.size = size
        self.completed_items = []
        self.current_building = []
        self.final_comp = final_comp

    def does_need_items(self):
        return False if len(self.completed_items) == 3 or len(self.build) + len(self.current_building) == 0 else True
