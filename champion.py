"""
Contains all information related to an individual board slot used by the bot
"""


class Champion:
    """Champion class that contains information about a single unit on the board or bench"""

    # pylint: disable=too-many-instance-attributes,too-few-public-methods,too-many-arguments

    # TODO: make some of these have default parameters
    def __init__(self, name: str, coords: tuple, item_slots_filled: int, build: list[str], build2: list[str],
                 ornn_items: list[str], support_items: list[str], trait_items: list[str], zaun_items: list[str],
                 slot: int, size: int, final_comp: bool) -> None:
        # The units name.
        self.name: str = name
        # Where the unit is located on the bench or board in Vec2 coordinates.
        self.coords: tuple = coords
        # How many item slots are taken up by the unit. There are only 3 item slots, which get translated to 6 slots:
        # completed/non-component items fill up two slots and component items fill up 1. Zaun items fill up 0.
        self.item_slots_filled: int = item_slots_filled
        # A list of the items that are likely the unit's best items it can be given, a.k.a. their "Best In Slot" (BIS)
        self.build: list[str] = build
        # A list of completed items that aren't BIS, but would also work on this unit.
        self.completed_items_will_accept: list[str] = build2
        # The Ornn items this unit would like.
        self.ornn_items_will_accept: list[str] = ornn_items
        # The Support items this unit would like.
        self.support_items_will_accept: list[str] = support_items
        # The Trait items this unit would like.
        self.trait_items_will_accept: list[str] = trait_items
        # The Trait items this unit would like.
        self.zaun_items_will_accept: list[str] = zaun_items
        # The position on the board where the unit is designated in comps.py to be placed.
        self.index: int = slot
        # The 'amount of units' this unit counts as, because sometimes a unit counts as 2 of your total possible units.
        self.size: int = size
        # The list of every item the unit has.
        self.items: list = []
        # The list of non-component items the unit has that aren't Zaun items.
        self.non_component_items: list = []
        # The unit can only hold one component item at a time.
        self.component_item: str = ""
        # A list that should only be a tuple of (completed_item, component_item), where the component item in the tuple
        # combines with another component item the unit is currently holding to create the completed item.
        # TODO: this shouldn't be a list. might not even be needed
        self.current_building: list = []
        # The list of Zaun items the unit has. Max of 3 items.
        self.held_zaun_items: list = []
        # Whether the unit is a part of the final comp.
        self.final_comp: bool = final_comp

    def does_need_items(self) -> bool:
        """Returns if the champion instance needs items"""
        return len(self.non_component_items) != 3 or len(self.build) + len(self.current_building) == 0

    def print_all_class_variables(self):
        """Prints out all of a unit's information."""
        print(f"\t\tChampion Object: {self}")
        print(f"\t\tChampion Name: {self.name}")
        print(f"\t\tLocation in Coordinates: {self.coords}")
        print(f"\t\tItems The Unit is Designated to Build: {self.build}")
        print(f"\t\tLocation on the Board: {self.index}")
        print(f"\t\tAmount of Spaces This Unit Takes Up on the Board: {self.size}")
        print(f"\t\tCompleted Items: {self.non_component_items}")
        print(f"\t\tComponent Items: {self.current_building}")
        print(f"\t\tFinal Comp? {self.final_comp}")
