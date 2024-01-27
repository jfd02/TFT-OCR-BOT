"""
This module contains the CompsManager class, which manages team compositions and champions.
"""

import random
from typing import Dict, List, Union


class CompsManager:
    """
    Class to manage team compositions and champions.
    """

    def __init__(self) -> None:
        self.index_current: int = -1
        self.sequence_index: int = -1
        self.is_sequence_mode = False
        self.sequence: list = []
        self.augments: list = []
        self.comps_loaded: list[str, dict[str, dict[str,]]] = []
        self.champions: dict[str, dict[str, int]] = {}

    def set_comps_loaded(
        self, input_data: List[Union[str, Dict[str, Dict[str, int]]]]
    ) -> None:
        """
        Set the loaded compositions.

        Args:
        - input_data (List[Union[str, Dict[str, Dict[str, int]]]]): Input data containing compositions.
        """
        self.comps_loaded = input_data

    def select_next_comp(self) -> None:
        """
        Select the next composition.
        """
        if self.is_sequence_mode is False:
            comps_size = len(self.comps_loaded)
            self.index_current = random.randint(0, comps_size - 1)
        else:
            self.sequence_index = self.sequence_index + 1
            sequence_len = len(self.sequence)
            if self.sequence_index >= sequence_len:
                self.sequence_index = 0
            self.index_current = self.sequence[self.sequence_index]
        print(
            f"[!] {self.current_comp()[0]} [{','.join(self.current_comp()[1])}] comp is selected"
        )

    def current_comp(self) -> List[Union[str, dict[str, dict[str,]]]]:
        """
        Get the currently selected composition.

        Returns:
        - List[Union[str, dict[str, dict[str,]]]]: Currently selected composition.
        """
        return self.comps_loaded[self.index_current]

    def champion_board_size(self, champion: str) -> int:
        """
        Get the board size of a specific champion.

        Args:
        - champion (str): Name of the champion.

        Returns:
        - int: Board size of the champion.
        """
        return self.champions[champion]["Board Size"]

    def champion_gold_cost(self, champion: str) -> int:
        """
        Get the gold cost of a specific champion.

        Args:
        - champion (str): Name of the champion.

        Returns:
        - int: Gold cost of the champion.
        """
        return self.champions[champion]["Gold"]

    def champions_to_buy(self) -> dict:
        """
        Create a list of champions to buy during the game.

        Returns:
        - dict: Dictionary of champions to buy.
        """
        champs_to_buy: dict = {}
        for champion, champion_data in self.current_comp()[1].items():
            if champion_data["level"] == 1:
                champs_to_buy[champion] = 1
            elif champion_data["level"] == 2:
                champs_to_buy[champion] = 3
            elif champion_data["level"] == 3:
                champs_to_buy[champion] = 9
            else:
                raise ValueError(
                    "Comps.py | Champion level must be a valid level (1-3)"
                )
        return champs_to_buy

    def get_unknown_slots(self) -> List[int]:
        """
        Create a list of slots on the board that don't have a champion from the team composition.

        Returns:
        - list: List of slots without champions.
        """
        container: List[int] = [
            champion_data["board_position"]
            for _, champion_data in self.current_comp()[1].items()
        ]
        return [n for n in range(27) if n not in container]

    def convert_headliner_data(self, name, headliner_data):
        """Convert headliner data to a boolean list."""
        if not headliner_data or headliner_data == "[]":
            return [False, False, False]

        champion_data = self.champions.get(name, {})
        return [
            champion_data.get(f"Trait{i+1}", "").lower() == headliner_data.lower()
            for i in range(3)
        ]

    def get_headliner_tag(self, name: str) -> int:
        """Return what trait of specified champion can become headliner"""
        try:
            headliner_data = self.comps_loaded[self.index_current][1][name]["headliner"]
            headliner_data_list = self.convert_headliner_data(name, headliner_data)

            if len(headliner_data_list) >= 3:
                digit_1 = int(headliner_data_list[0])
                digit_2 = int(headliner_data_list[1]) * 2
                digit_3 = int(headliner_data_list[2]) * 4

                return digit_1 + digit_2 + digit_3

        except (IndexError, KeyError, TypeError, ValueError):
            return
