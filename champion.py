"""
Contains all information related to an individual board slot used by the bot
"""

class Champion:
    """Champion class that contains information about a single unit on the board or bench"""
    # pylint: disable=too-many-instance-attributes,too-few-public-methods,too-many-arguments

    def __init__(self, name: str, coords: tuple, build, slot: int, size: int, final_comp: bool):
        self.name = name
        self.coords = coords
        self.build = build
        self.index = slot
        self.size = size
        self.completed_items = []
        self.current_building = []
        self.final_comp = final_comp

    def does_need_items(self):
        """Returns if the champion instance needs items"""
        return len(self.completed_items) != 3 or len(self.build) + len(self.current_building) == 0
