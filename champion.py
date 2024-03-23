"""
Contains all information related to an individual board slot used by the bot
"""


class Champion:
    """Champion class that contains information about a single unit on the board or bench"""

    # pylint: disable=too-many-instance-attributes,too-few-public-methods,too-many-arguments

    def __init__(
        self,
        name: str,
        coords: tuple,
        build,
        slot: int,
        size: int,
        final_comp: bool,
    ) -> None:
        self.name: str = name
        self.coords: tuple = coords
        self.build = build
        self.index: int = slot
        self.size: int = size
        self.completed_items: list = []
        self.current_building: list = []
        self.max_item_slots: int = 3
        self.final_comp: bool = final_comp

    def __str__(self) -> str:
        return (
            f"Champion(name={self.name}, coords={self.coords}, "
            f"build={self.build}, index={self.index}, size={self.size}, "
            f"completed_items={self.completed_items}, "
            f"current_building={self.current_building}, final_comp={self.final_comp}, "
        )

    def does_need_items(self) -> bool:
        """Returns True if the champion instance needs items, False otherwise"""
        return (
            len(self.completed_items) != 3
            or len(self.build) + len(self.current_building) == 0
        )

    def has_available_item_slots(self):
        """Check if the champion has available item slots."""
        max_item_slots = 3
        return len(self.completed_items) < max_item_slots
