"""
Contains all information related to an individual board slot used by the bot
"""


class Champion:
    """Champion class that contains information about a single unit on the board or bench"""

    # pylint: disable=too-many-instance-attributes,too-few-public-methods,too-many-arguments

    def __init__(self, name: str, coords: tuple, build, slot: int, size: int, final_comp: bool) -> None:
        # The units name.
        self.name: str = name
        # Where the unit is located on the bench or board in Vec2 coordinates.
        self.coords: tuple = coords
        # All the items the unit is designated to build.
        self.build = build
        # The position on the board where the unit is designated in comps.py to be placed.
        self.index: int = slot
        # The previously empty slot on the bench the purchased unit was moved to.
        self.size: int = size
        # The list of completed items the unit has.
        self.completed_items: list = []
        # The list of component items that the unit has.
        self.current_building: list = []
        # Whether the unit is a part of the final comp.
        self.final_comp: bool = final_comp

    def does_need_items(self) -> bool:
        """Returns if the champion instance needs items"""
        return len(self.completed_items) != 3 or len(self.build) + len(self.current_building) == 0

    def print_all_class_variables(self):
        """Prints out all of a unit's information."""
        print(f"\t\tChampion Object: {self}")
        print(f"\t\tChampion Name: {self.name}")
        print(f"\t\tLocation in Coordinates: {self.coords}")
        print(f"\t\tItems The Unit is Designated to Build: {self.build}")
        print(f"\t\tLocation on the Board: {self.index}")
        print(f"\t\tSize: {self.size}")
        print(f"\t\tCompleted Items: {self.completed_items}")
        print(f"\t\tComponent Items: {self.current_building}")
        print(f"\t\tFinal Comp? {self.final_comp}")
