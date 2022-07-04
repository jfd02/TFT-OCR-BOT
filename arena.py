"""
This class handles the board / bench state inside of the game and
other variables used by the bot to make decisions
"""

from time import sleep
import game_assets
import mk_functions
import screen_coords
from champion import Champion
from game_assets import champion_data, full_items
import comps
import ocr
import arena_functions

class Arena:
    def __init__(self):
        self.board_size = 0
        self.bench = [None, None, None, None, None, None, None, None, None]
        self.board = []
        self.board_unknown = []
        self.unknown_slots = comps.get_unknown_slots()
        self.champs_to_buy = comps.champions_to_buy()
        self.board_names = []
        self.items = []
        self.final_comp = False
        self.level = 0
        self.spam_roll = False

    def fix_board_state(self):
        bench_occupied = arena_functions.bench_occupied_check()
        for index, slot in enumerate(self.bench):
            if slot is None and bench_occupied[index] is True:
                self.bench[index] = "?"
            if isinstance(slot, str) and bench_occupied[index] is False:
                self.bench[index] = None
            if isinstance(slot, Champion) and bench_occupied[index] is False:
                self.bench[index] = None

    def bought_champion(self, name, slot):
        items = []
        for item in comps.comp[name]["items"]:
            items.append(item)
        self.bench[slot] = Champion(name, screen_coords.bench_loc[slot].get_coords(), items, slot,
                                    champion_data[name]["Board Size"], comps.comp[name]["final_comp"])
        mk_functions.move_mouse(screen_coords.default_loc.get_coords())
        sleep(0.5)
        self.fix_board_state()

    def have_champion(self):
        for champion in self.bench:
            if isinstance(champion, Champion):
                if champion.name not in self.board_names:
                    return champion
        return None

    def move_known(self, champion):
        destination = screen_coords.board_loc[comps.comp[champion.name]["board_position"]].get_coords()
        mk_functions.left_click(champion.coords)
        mk_functions.left_click(destination)
        champion.coords = destination
        self.board.append(champion)
        self.board_names.append(champion.name)
        self.bench[champion.index] = None
        champion.index = comps.comp[champion.name]["board_position"]
        self.board_size += champion.size

    def move_unknown(self):
        for index, champion in enumerate(self.bench):
            if isinstance(champion, str):
                mk_functions.left_click(screen_coords.bench_loc[index].get_coords())
                mk_functions.left_click(screen_coords.board_loc[self.unknown_slots[len(self.board_unknown)]].get_coords())
                self.bench[index] = None
                self.board_unknown.append(champion)
                self.board_size += 1
                return

    def sell_bench(self):
        for index, _ in enumerate(self.bench):
            mk_functions.press_e(screen_coords.bench_loc[index].get_coords())
            self.bench[index] = None

    def unknown_in_bench(self):
        for slot in self.bench:
            if isinstance(slot, str):
                return True
        return False

    def move_champions(self):
        self.level = arena_functions.get_level()
        while self.level > self.board_size:
            champion = self.have_champion()
            if champion is not None:
                self.move_known(champion)
            elif self.unknown_in_bench():
                self.move_unknown()
            else:
                bought_unknown = False
                shop = arena_functions.get_shop()
                for index, champion in enumerate(shop):
                    try:  # Can fail if the shop slot is ""
                        if champion_data[champion]["Gold"] <= arena_functions.get_gold() and champion_data[champion][
                            "Board Size"] == 1 and champion not in self.champs_to_buy and champion not in self.board_unknown:
                            none_slot = arena_functions.empty_slot()
                            mk_functions.left_click(screen_coords.buy_loc[index].get_coords())
                            sleep(0.2)
                            self.bench[none_slot] = f"{champion}"
                            self.move_unknown()
                            bought_unknown = True
                            break
                    except KeyError:
                        pass
                if not bought_unknown:
                    self.sell_bench()
                    return

    def replace_unknown(self):
        champion = self.have_champion()
        if len(self.board_unknown) > 0 and champion is not None:
            mk_functions.press_e(screen_coords.board_loc[self.unknown_slots[len(self.board_unknown) - 1]].get_coords())
            self.board_unknown.pop()
            self.board_size -= 1
            self.move_known(champion)

    def bench_cleanup(self):
        for index, champion in enumerate(self.bench):
            if champion == "?" or isinstance(champion, str):
                mk_functions.press_e(screen_coords.bench_loc[index].get_coords())
                self.bench[index] = None
            elif isinstance(champion, Champion):
                if champion.name not in self.champs_to_buy and champion.name in self.board_names:
                    mk_functions.press_e(screen_coords.bench_loc[index].get_coords())
                    self.bench[index] = None

    def place_items(self):
        self.items = arena_functions.get_items()
        log_items = list(filter((None).__ne__, self.items))
        for index, _ in enumerate(self.items):
            if self.items[index] is not None:
                self.add_item_to_champs(index)

    def add_item_to_champs(self, item_index):
        for champ in self.board:
            if champ.does_need_items() and self.items[item_index] is not None:
                self.add_item_to_champ(item_index, champ)

    def add_item_to_champ(self, item_index, champ):
        item = self.items[item_index]
        if item in full_items:
            if item in champ.build:
                mk_functions.left_click(screen_coords.item_pos[item_index][0].get_coords())
                mk_functions.left_click(champ.coords)
                champ.completed_items.append(item)
                champ.build.remove(item)
                self.items[self.items.index(item)] = None
        else:
            if len(champ.current_building) == 0:
                item_to_move = None
                for build_item in champ.build:
                    build_item_components = list(full_items[build_item])
                    if item in build_item_components:
                        item_to_move = item
                        build_item_components.remove(item)
                        champ.current_building.append((build_item, build_item_components[0]))
                        champ.build.remove(build_item)
                if item_to_move is not None:
                    mk_functions.left_click(screen_coords.item_pos[item_index][0].get_coords())
                    mk_functions.left_click(champ.coords)
                    self.items[self.items.index(item)] = None
            else:
                for builditem in champ.current_building:
                    if item == builditem[1]:
                        mk_functions.left_click(screen_coords.item_pos[item_index][0].get_coords())
                        mk_functions.left_click(champ.coords)
                        champ.completed_items.append(builditem[0])
                        champ.current_building.clear()
                        self.items[self.items.index(item)] = None
                        return

    def fix_unknown(self):
        sleep(0.25)
        mk_functions.press_e(screen_coords.board_loc[self.unknown_slots[0]].get_coords())
        self.board_unknown.pop(0)
        self.board_size -= 1

    def remove_champion(self, champion):
        for index, slot in enumerate(self.bench):
            if isinstance(slot, Champion):
                if slot.name == champion.name:
                    mk_functions.press_e(slot.coords)
                    self.bench[index] = None

        self.champs_to_buy = list(filter(f"{champion.name}".__ne__,
                                         self.champs_to_buy))  # Remove all instances of champion in champs_to_buy

        mk_functions.press_e(champion.coords)
        self.board_names.remove(champion.name)
        self.board_size -= champion.size
        self.board.remove(champion)

    def final_comp_check(self):
        for slot in self.bench:
            if isinstance(slot, Champion):
                if slot.final_comp is True and slot.name not in self.board_names:
                    for champion in self.board:
                        if champion.final_comp is False and champion.size == slot.size:
                            self.remove_champion(champion)
                            self.move_known(slot)
                            break

    def tacticians_check(self):
        mk_functions.move_mouse(screen_coords.item_pos[0][0].get_coords())
        sleep(2)
        item = ocr.get_text(screenxy=screen_coords.item_pos[0][1].get_coords(), scale=3, psm=13,
                            whitelist="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
        item = arena_functions.valid_item(item)
        try:
            if "TacticiansCrown" in item:
                self.board_size -= 1
        except TypeError:
            return


    def spend_gold(self):  # Rework this function
        first_run = True
        min_gold = 24 if self.spam_roll is True else 56
        while first_run or arena_functions.get_gold() >= min_gold:
            if not first_run:
                if arena_functions.get_level() != 9:
                    mk_functions.buy_xp()
                mk_functions.reroll()
            shop = arena_functions.get_shop()
            for index, champion in enumerate(shop):
                if champion in self.champs_to_buy:
                    if arena_functions.get_gold() - game_assets.champion_data[champion]["Gold"] >= 0:
                        none_slot = arena_functions.empty_slot()
                        if none_slot != -1:
                            mk_functions.left_click(screen_coords.buy_loc[index].get_coords())
                            self.bought_champion(champion, none_slot)
                            self.champs_to_buy.remove(champion)
            first_run = False

    def krug_round(self):
        if arena_functions.get_gold() >= 4:
            mk_functions.buy_xp()

    def pick_augment(self):
        augments = []
        for coords in screen_coords.augment_pos:
            augment = ocr.get_text(screenxy=coords.get_coords(), scale=3, psm=7, whitelist="")
            augments.append(augment)

        for augment in augments:
            for potential in comps.priority_augments:
                if potential in augment:
                    mk_functions.left_click(screen_coords.augment_loc[augments.index(augment)].get_coords())
                    return

        for augment in augments:
            for potential in comps.backup_augments:
                if potential in augment:
                    mk_functions.left_click(screen_coords.augment_loc[augments.index(augment)].get_coords())
                    return

        mk_functions.left_click(screen_coords.augment_loc[0].get_coords())

    def check_health(self):
        health = arena_functions.get_health()
        if health <= 100 and health >= 0:
            if self.spam_roll is False:
                if health < 30:
                    self.spam_roll = True
        else:
            return
