import random


class CompsManager:
    def __init__(self):
        self.index_current : int = -1
        self.sequence_index : int = -1
        self.is_sequence_mode = False
        self.sequence : list = []
        self.augments: list = []
        self.comps_loaded : list[str, dict[str, dict[str,]]] = []
        self.champions: dict[str, dict[str, int]] = {}

    def SetCOMPSLoaded(self, input):
        self.comps_loaded = input
    def SelectNextComp(self):
        if self.is_sequence_mode is False:
            comps_size = len(self.comps_loaded)
            self.index_current = random.randint(0, comps_size-1)
        else:
            self.sequence_index = self.sequence_index + 1
            sequence_len = len(self.sequence)
            if self.sequence_index >= sequence_len:
                self.sequence_index = 0
            self.index_current = self.sequence[self.sequence_index]
        print(f"[!] {self.CURRENT_COMP()[0]} [{','.join(self.CURRENT_COMP()[1])}] comp is selected")

    def CURRENT_COMP(self):
        return self.comps_loaded[self.index_current]

    def champion_board_size(self, champion: str) -> int:
        return self.champions[champion]["Board Size"]

    def champion_gold_cost(self, champion: str) -> int:
        return self.champions[champion]["Gold"]


    def champions_to_buy(self) -> list:
        """Creates a list of champions to buy during the game"""
        champs_to_buy: list = []
        for champion, champion_data in self.CURRENT_COMP()[1].items():
            if champion_data["level"] == 1:
                champs_to_buy.append(champion)
            elif champion_data["level"] == 2:
                champs_to_buy.extend([champion] * 3)
            elif champion_data["level"] == 3:
                champs_to_buy.extend([champion] * 9)
            else:
                raise ValueError("Comps.py | Champion level must be a valid level (1-3)")
        return champs_to_buy


    def get_unknown_slots(self) -> list:
        """Creates a list of slots on the board that don't have a champion from the team composition"""
        container: list = [
            champion_data["board_position"] for _, champion_data in self.CURRENT_COMP()[1].items()
            ]
        return [n for n in range(27) if n not in container]
