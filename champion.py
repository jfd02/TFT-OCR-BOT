class Champion:
    def __init__(self, name, coords, build, slot, size, final_comp, completed_items=None, current_building=None, level=1):
        if current_building is None:
            current_building = []
        if completed_items is None:
            completed_items = []
        self.name = name
        self.level = level
        self.coords = coords
        self.build = build
        self.index = slot
        self.size = size
        self.completed_items = completed_items
        self.current_building = current_building
        self.final_comp = final_comp

    def does_need_items(self):
        return False if len(self.completed_items) == 3 or len(self.build) + len(self.current_building) == 0 else True
