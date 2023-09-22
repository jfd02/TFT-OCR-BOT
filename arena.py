"""
Handles the board / bench state inside of the game and
other variables used by the bot to make decisions
"""
import collections
import random
from time import sleep
import numpy as np
from PIL import ImageGrab

import arena_functions
import game_functions
import mk_functions
import ocr
import screen_coords
from ansi_colors import AnsiColors
import champion as champion_class
from champion import Champion
from set_9_5 import game_assets


class Arena:
    """Arena class that handles game logic such as board and bench state"""

    # pylint: disable=too-many-instance-attributes,too-many-public-methods
    def __init__(self, message_queue) -> None:
        self.message_queue = message_queue
        # The comp the bot will play.
        self.comp_to_play = game_functions.pick_a_random_comp_to_play()
        # How many slots for units we can have on the board. (Set 6 Colossus units could take up to 2 slots)
        self.board_size = 0
        # The max amount of slot for units that we can have. Can increase from augments or items.
        self.max_board_size = 1
        # A list representing each location on the bench.
        self.bench: list[Champion | None] = [None, None, None, None, None, None, None, None, None]
        # All the spaces of the board. Can be an instance of a Champion or None.
        self.board: list[Champion | None] = [None] * 28
        # All the spaces on the board that have a unit, but we don't know what that unit is.
        self.board_unknown: list = []
        # All the non-Champion units and the board spaces they occupy. Should be a list of tuple(str, int).
        self.board_unknown_and_pos: list = []
        # All the spaces on the board that we haven't designated to put a unit from our comp on.
        self.board_slots_for_non_comp_units: list = self.comp_to_play.get_unknown_slots()  # initializing this way is probably bad practice?
        self.champs_to_buy: list[str] = self.comp_to_play.champions_to_buy()  # initializing this way is probably bad practice?
        # A list of the names of all units on the board (not the bench), including duplicates.
        self.board_names: list = []
        # Items on the player's bench. A max of 10 items can be on the bench.
        self.items: list = [None] * 10
        # All the augments that the player currently has.
        self.augments: list = []
        self.final_comp = False
        self.level = 1
        self.augment_roll = True
        self.spam_roll = False
        self.spam_roll_to_zero = False

    def fix_bench_state(self, mistaken_identiy: bool = False) -> None:
        """Iterates through bench and fixes invalid slots"""
        self.identify_champions_on_bench(mistaken_identiy)
        self.sell_non_comp_units_on_bench()

    def move_unknown_units_to_bench(self):
        units_on_board_found_from_health = self.board_occupied_check()
        print("  Moving unknown units to the bench.")
        if len(units_on_board_found_from_health) == 0:
            print("    No unknown units were found.")
        for index, unit in enumerate(self.board):
            if isinstance(unit, Champion):
                print(f"    Unit: {unit} and Index: {index}")
                if not units_on_board_found_from_health[index]:
                    print(f"    We failed to find a unit at index: {index}!")
                else:
                    print(f"    We know there is a unit at index: {index}. Changing the units_on_board_found to False for that index.")
                    units_on_board_found_from_health[index] = False
        for index, boolean in enumerate(units_on_board_found_from_health):
            if boolean and arena_functions.empty_bench_slot() != -1:
                mk_functions.press_w(screen_coords.BOARD_LOC[index].get_coords())
                # Will turn into a bug if we ever have units that take up 2 board spaces again.
                self.set_board_size(self.board_size - 1)
            if boolean and arena_functions.empty_bench_slot() == -1:
                print("    Oh no! We have an unknown unit that we can't move to the board.")

    def bought_champion(self, name: str, bench_position: int) -> None:
        """Purchase champion and creates champion instance"""
        self.bench[bench_position] = \
            Champion(name=name,
                     coords=screen_coords.BENCH_LOC[bench_position].get_coords(),
                     item_slots_filled=0,
                     build=self.comp_to_play.comp[name]["best_in_slot"].copy(),
                     build2=self.comp_to_play.comp[name]["secondary_items"].copy(),
                     ornn_items=self.comp_to_play.comp[name]["ornn_items_to_accept"].copy(),
                     support_items=self.comp_to_play.comp[name]["support_items_to_accept"].copy(),
                     trait_items=self.comp_to_play.comp[name]["trait_items_to_accept"].copy(),
                     zaun_items=self.comp_to_play.comp[name]["zaun_items_to_accept"].copy(),
                     board_position=self.comp_to_play.comp[name]["board_position"],
                     size=game_assets.CHAMPIONS[name]["Board Size"],
                     final_comp=self.comp_to_play.comp[name]["final_comp"])
        mk_functions.move_mouse(screen_coords.DEFAULT_LOC.get_coords())
        # sleep(0.3)
        self.fix_bench_state()

    def get_next_champion_on_bench(self) -> Champion | None:
        """Checks the bench to see if champion exists"""
        return next(
            (
                champion
                for champion in self.bench
                if isinstance(champion, Champion)
                   and champion.name not in self.board_names
            ),
            None,
        )

    def get_next_unit_from_our_comp_on_bench(self) -> Champion | None:
        """Checks to see if a unit from our comp is on the bench."""
        return next(
            (
                champion
                for champion in self.bench
                if isinstance(champion, Champion)
                   and champion.name not in self.board_names
                   and champion.name in self.comp_to_play.comp
            ),
            None,
        )

    def move_known(self, champion: Champion) -> None:
        """Moves champion to the board"""
        print(f"    Moving known unit {champion.name} to board.")
        board_position = -1
        # If the unit is in our comp. Put it in its designated spot on the board.
        if champion.name in self.comp_to_play.comp:
            print("      Selecting the designated board space because the unit is in our comp.")
            board_position = champion.board_position
        # Otherwise, put it in a random spot on the board that our wanted units won't use.
        # Might accidentally replace an unwanted unit with this one.
        else:
            print("      Selecting a random board space because the unit isn't in our comp.")
            while True:
                board_position = random.choice(self.board_slots_for_non_comp_units)
                if self.board[board_position] is None:
                    break
                else:
                    print("    Almost moved a unit to a random board space with another unit on it.")
        destination: tuple = screen_coords.BOARD_LOC[board_position].get_coords()
        arena_functions.move_unit(champion.coords, destination)
        successful_move = True  # arena_functions.was_moving_unit_successful(destination)
        if successful_move:
            champion.coords = destination
            self.board[board_position] = champion
            self.board_names.append(champion.name)
            self.bench[self.bench.index(champion)] = None
            self.set_board_size(self.board_size + champion.size)
            print(f"      Moved {champion.name} to {board_position}.")
            print(f"        There are now {self.board_size} slots for units taken up on the board.")
        else:
            print(f"      Failed to move {champion.name} to {board_position}.")

    def move_unknown(self) -> None:
        """Moves unknown champion to the board"""
        for index, champion in enumerate(self.bench):
            if isinstance(champion, str):
                print(f"    [!] Moving unknown unit {champion} from bench slot {index} "
                      f"to board space {self.board_slots_for_non_comp_units[len(self.board_unknown)]}.")
                arena_functions.move_unit(screen_coords.BENCH_LOC[index].get_coords(), screen_coords.BOARD_LOC[
                    self.board_slots_for_non_comp_units[len(self.board_unknown)]].get_coords())
                self.bench[index] = None
                self.board_unknown.append(champion)
                self.set_board_size(self.board_size + 1)
                print(f"      There are now {self.board_size} slots for units taken up on the board.")
                return
        return

    def sell_bench(self) -> None:
        """Sells all of the champions on the bench"""
        print(f"    Selling all the units on the bench.")
        for index, _ in enumerate(self.bench):
            mk_functions.press_e(screen_coords.BENCH_LOC[index].get_coords())
            self.bench[index] = None
        return

    def unknown_in_bench(self) -> bool:
        """Returns True if there is a spot on the bench taken up and that spot is not recognized as a champion/unit."""
        return any(isinstance(slot, str) for slot in self.bench)

    def move_champions(self) -> None:
        """Moves champions to the board"""
        if self.max_board_size > self.board_size:
            print(f"  Our max board size {self.max_board_size} is greater than our board size {self.board_size}.")
        # can currently run into an infinite while loop on augment stages
        while self.max_board_size > self.board_size:
            unit: Champion | None = self.get_next_champion_on_bench()
            if unit is not None:
                self.move_known(unit)
            elif self.unknown_in_bench():
                # No more moving unknown units to the board.
                # self.move_unknown()
                print("  Instead of moving an unknown unit to the board, I'm going to identify what's on the bench.")
                self.fix_bench_state()
            else:
                print("    I think the point of this code is to always have the max units on the board?")
                shop: list = arena_functions.get_shop()
                for index, purchaseable_unit in enumerate(shop):
                    gold: int = arena_functions.get_gold()
                    valid_champ_not_in_champs_to_buy_or_board_unknown: bool = (
                            purchaseable_unit in game_assets.CHAMPIONS and
                            game_assets.champion_gold_cost(purchaseable_unit) <= gold and
                            game_assets.champion_board_size(purchaseable_unit) == 1 and
                            purchaseable_unit not in self.champs_to_buy and
                            purchaseable_unit not in self.board_unknown
                    )

                    if valid_champ_not_in_champs_to_buy_or_board_unknown:
                        empty_bench_slot: int = arena_functions.empty_bench_slot()
                        mk_functions.left_click(screen_coords.BUY_LOC[index].get_coords())
                        new_champion = champion_class.create_default_champion(purchaseable_unit, empty_bench_slot, True, self.comp_to_play)
                        sleep(0.1)
                        self.bench[empty_bench_slot] = new_champion
                        self.move_known(new_champion)
                        break
        return

    def replace_unknown(self) -> None:
        """Removes an unknown champion on the board.
           Then places a known champion from the bench."""
        print("  replace_unknown")
        champion: Champion | None = self.get_next_champion_on_bench()
        if len(self.board_unknown_and_pos) > 0 and champion is not None:
            print(f"    [?]Replacing an unknown champion with {champion.name}.")
            unknown_unit_and_pos = self.board_unknown_and_pos.pop()
            value = screen_coords.BOARD_LOC[unknown_unit_and_pos[1]].get_coords()
            mk_functions.press_e(value)
            self.set_board_size(self.board_size - 1)
            self.move_known(champion)
        return

    def replace_units_not_in_our_comp(self) -> None:
        """Replaces a unit on the board with a unit from the bench that is in our comp."""
        for unit in self.board:
            if isinstance(unit, Champion):
                champion: Champion | None = self.get_next_unit_from_our_comp_on_bench()
                if champion is None:
                    return
                if unit.name not in self.comp_to_play.comp and champion.name in self.comp_to_play.comp:
                    print(f"    Replacing {unit.name} with {champion.name} because {unit.name} is not in our comp.")
                    mk_functions.press_e(unit.coords)
                    self.board[self.board.index(unit)] = None
                    self.board_names.remove(unit.name)
                    self.set_board_size(self.board_size - unit.size)
                    self.move_known(champion)
        return

    def bench_cleanup(self) -> None:
        """Sells unknown champions"""
        for index, champion in enumerate(self.bench):
            if champion == "?" or isinstance(champion, str):
                print(f"  1Selling unknown champion: {champion}")
                mk_functions.press_e(screen_coords.BENCH_LOC[index].get_coords())
                self.bench[index] = None
            elif isinstance(champion, Champion):
                if champion.name not in self.champs_to_buy and champion.name in self.board_names:
                    # Make this fix the champion instead of being unknown?
                    print(f"  Champion not in champs_to_buy: {champion} - Name: {champion.name}")
                    mk_functions.press_e(screen_coords.BENCH_LOC[index].get_coords())
                    self.bench[index] = None
        return

    def clear_anvil(self) -> None:
        """Clears anvil on the bench,
           selects a good Emblem if a Tome of Traits was sold,
           otherwise select the middle item."""
        print("  Looking for anvils to sell.")
        bench_units = arena_functions.bench_occupied_check()
        for index, unit in enumerate(bench_units):
            if unit:
                continue
            returned_number = arena_functions.identify_component_anvil(index)
            if returned_number != 0:
                mk_functions.press_e(screen_coords.BENCH_LOC[index].get_coords())
                sleep(0.2)
                screen_coords_vec2_tuple = screen_coords.BUY_LOC[2].get_coords()
                if returned_number == 3:
                    print("    Selecting emblem from the Tome of Traits shop.")
                    emblem_shop_index = self.pick_one_of_four_emblems_from_shop()
                    if emblem_shop_index is not None:
                        screen_coords_vec2_tuple = screen_coords.CHOOSE_FROM_TOME_OF_TRAITS_SHOP_LOC[emblem_shop_index].get_coords()
                else:
                    print("    Selecting middle item from Anvil/Ornn Item Anvil.")
                mk_functions.left_click(screen_coords_vec2_tuple)
        return

    # Pretty much deprecated. Use Arena.give_items_to_units() instead
    def place_items_by_looping_through_items_first(self) -> None:
        """Iterates through items and tries to add them to champion"""
        self.items = arena_functions.get_items()
        print(f"  Items: {list(filter(None.__ne__, self.items))}")

        self.check_if_we_should_make_lucky_gloves()
        self.check_if_we_should_spam_sparring_gloves()

        will_try_to_place_item = True
        item_count = 0
        item_amount_at_start = self.count_items_on_bench()
        # Place items until we fail to place an item once.
        print(f"  Looking to place items.")
        while will_try_to_place_item:
            item_count += 1
            # print(f"  Looking for item #{item_count} to place:")
            # print("    Item Loop 1")
            # so that we can place multiple items on a unit at once
            for index, _ in enumerate(self.items):
                if self.items[index] is not None:
                    item = self.items[index]
                    if item in game_assets.SUPPORT_ITEMS:
                        print(f"    Found a Support Item: {item}")
                    if item in game_assets.MOGUL_ITEMS:
                        print(f"    Found a Mogul Item: {item}")
                    if item in game_assets.TRAIT_ITEMS:
                        print(f"    Found a Trait Item: {item}")
                    if item in game_assets.RADIANT_ITEMS:
                        print(f"    Found a Radiant Item: {item}")
                    if item in game_assets.ORNN_ITEMS:
                        print(f"    Found an Ornn Item: {item}")
                    if item in game_assets.ZAUN_ITEMS:
                        print(f"    Found a Zaun Item: {item}")
                    if item in game_assets.CRAFTABLE_ITEMS_DICT:
                        print(f"    Found a Completed Item: {item}")
                    self.add_item_to_champs(index)
                    if self.is_same_amount_or_more_items_on_bench(item_amount_at_start):
                        will_try_to_place_item = False
                    if self.check_if_we_should_spam_items_before_dying(index):
                        if self.is_same_amount_or_more_items_on_bench(item_amount_at_start):
                            will_try_to_place_item = False
            # print("    Item Loop 2")
            for index, _ in enumerate(self.items):
                if self.items[index] is not None:
                    self.add_item_to_champs(index)
                    if self.is_same_amount_or_more_items_on_bench(item_amount_at_start):
                        will_try_to_place_item = False
                    if self.check_if_we_should_spam_items_before_dying(index):
                        if self.is_same_amount_or_more_items_on_bench(item_amount_at_start):
                            will_try_to_place_item = False
            if item_count > 10:
                will_try_to_place_item = False
            if not will_try_to_place_item:
                print("    No longer placing items this round.")
        return

    # Pretty much deprecated. Use Arena.give_items_to_units() instead
    def add_item_to_champs(self, item_index: int) -> None:
        """Iterates through champions in the board and checks if the champion needs items"""
        for champ in self.board:
            if isinstance(champ, Champion):
                if champ.does_need_items() and self.items[item_index] is not None:
                    # print(f"      {champ.name} needs items.", end=" ")
                    self.add_item_to_champ(item_index, champ)
        # print("")

    # Pretty much deprecated. Use Arena.give_items_to_units() instead
    def add_item_to_champ(self, item_index: int, champ: Champion) -> None:
        """Takes item index and champ and applies the item"""
        item = self.items[item_index]
        if item in game_assets.SUPPORT_ITEMS:
            if champ.name in self.comp_to_play.comp \
                    and item in self.comp_to_play.comp[champ.name]["support_items_to_accept"]:
                print(f"        Attempting to add item {item} to {champ.name} because it is a Support item it accepts.")
                self.add_one_item_to_unit(champ, item_index)
                champ.non_component_items.append(item)
        if item in game_assets.TRAIT_ITEMS:
            if champ.name in self.comp_to_play.comp \
                    and item in self.comp_to_play.comp[champ.name]["trait_items_to_accept"]:
                print(f"        Attempting to add item {item} to {champ.name} because it is a Trait item it accepts.")
                self.add_one_item_to_unit(champ, item_index)
                champ.non_component_items.append(item)
        if item in game_assets.ORNN_ITEMS:
            if champ.name in self.comp_to_play.comp \
                    and item in self.comp_to_play.comp[champ.name]["ornn_items_to_accept"]:
                print(f"        Attempting to add item {item} to {champ.name} because it is an Ornn item it accepts.")
                self.add_one_item_to_unit(champ, item_index)
                champ.non_component_items.append(item)
        if item in game_assets.ZAUN_ITEMS:
            if champ.name in self.comp_to_play.comp \
                    and item in self.comp_to_play.comp[champ.name]["zaun_items_to_accept"]:
                print(f"        Attempting to add item {item} to {champ.name} because it is a Zaun item it accepts.")
                self.add_one_item_to_unit(champ, item_index)
        if item in game_assets.CRAFTABLE_ITEMS_DICT:
            if item in champ.build:
                print(
                    f"        Attempting to add item {item} to {champ.name} because it is a completed item it builds.")
                self.add_one_item_to_unit(champ, item_index)
                champ.non_component_items.append(item)
                champ.build.remove(item)
        elif len(champ.current_building) == 0:
            item_to_move: None = None
            for build_item in champ.build:
                build_item_components = []
                if build_item in game_assets.CRAFTABLE_ITEMS_DICT:
                    build_item_components: list = list(
                        game_assets.CRAFTABLE_ITEMS_DICT[build_item])
                if item in build_item_components:
                    print(f"        Attempting to complete item {build_item} for {champ.name}")
                    item_to_move: None = item
                    build_item_components.remove(item_to_move)
                    print(
                        f"        Adding item {build_item_components[0]} to the list of "
                        f"component items {champ.name} needs next.")
                    champ.current_building.append(
                        (build_item, build_item_components[0]))
                    champ.build.remove(build_item)
            if item_to_move is not None:
                print(f"        Attempting to add item {item} to {champ.name} because it is a component item it needs.")
                arena_functions.move_item(screen_coords.ITEM_POS[item_index][0].get_coords(), champ.coords)
                arena_functions.print_item_placed_on_champ(item, champ)
                self.items[self.items.index(item)] = None
        else:
            for builditem in champ.current_building:
                if item == builditem[1]:
                    arena_functions.move_item(screen_coords.ITEM_POS[item_index][0].get_coords(), champ.coords)
                    champ.non_component_items.append(builditem[0])
                    champ.current_building.clear()
                    self.items[self.items.index(item)] = None
                    arena_functions.print_item_placed_on_champ(item, champ)
                    print(f"  Completed {builditem[0]}")
                    return
        return

    def add_thiefs_gloves_to_champ(self, champ: Champion) -> bool:
        """Makes Thiefs Gloves if possible and gives them to a champ with no items."""
        # print("    Attempting to add Thief's Gloves to a random itemless champ.")
        gloves_index_1 = -1
        gloves_index_2 = -1
        for index, _ in enumerate(self.items):
            if self.items[index] == "SparringGloves":
                if gloves_index_1 == -1:
                    print("    Found Sparring Gloves #1 for a Thief's Gloves.")
                    gloves_index_1 = index
                if gloves_index_1 != -1 and gloves_index_2 == -1:
                    print("    Found Sparring Gloves #2 for a Thief's Gloves.")
                    gloves_index_2 = index
        if gloves_index_1 != -1 and gloves_index_2 != -1 and gloves_index_1 != gloves_index_2:
            print("    We have 2 Sparring Gloves to make Thief's Gloves with!")
            arena_functions.move_item(screen_coords.ITEM_POS[gloves_index_1][0].get_coords(), champ.coords)
            print(f"      Placed {self.items[gloves_index_1]} on {champ.name}")
            self.items[gloves_index_1] = None
            arena_functions.move_item(screen_coords.ITEM_POS[gloves_index_2][0].get_coords(), champ.coords)
            print(f"      Placed {self.items[gloves_index_2]} on {champ.name}")
            self.items[gloves_index_2] = None
            return True
        return False

    # Pretty much deprecated. Use arena.add_random_items_on_strongest_units_at_one_loss_left() instead.
    def add_item_to_champs_before_dying(self, item_index: int) -> None:
        """Iterates through champions in the board and checks if the champion needs items"""
        for champ in self.board:
            if isinstance(champ, Champion):
                if champ.does_need_items() and self.items[item_index] is not None:
                    self.add_item_before_dying(item_index, champ)
        return

    # Pretty much deprecated. Use arena.add_random_items_on_strongest_units_at_one_loss_left() instead.
    def add_item_before_dying(self, item_index: int, champ: Champion) -> None:
        """Takes the remaining full items and gives them to champs that already have items.
            Then takes remaining component items and tries to give them to champs that already have items.
        """
        # print("  Found a champ to add an item to before dying.")
        item = self.items[item_index]
        if item in game_assets.ORNN_ITEMS or item in game_assets.RADIANT_ITEMS:
            if champ.does_need_items():
                self.add_one_item_to_unit(champ, item_index)
                champ.non_component_items.append(item)
        elif item in game_assets.TRAIT_ITEMS:
            if champ.does_need_items():
                self.add_one_item_to_unit(champ, item_index)
                champ.non_component_items.append(item)
        elif item in game_assets.SUPPORT_ITEMS:
            if champ.does_need_items():
                self.add_one_item_to_unit(champ, item_index)
                champ.non_component_items.append(item)
        elif item in game_assets.ZAUN_ITEMS:
            if champ.does_need_items():
                self.add_one_item_to_unit(champ, item_index)
                champ.non_component_items.append(item)
        elif item in game_assets.CRAFTABLE_ITEMS_DICT:
            if champ.does_need_items():
                self.add_one_item_to_unit(champ, item_index)
                champ.non_component_items.append(item)
        elif len(champ.non_component_items) < 3:
            print("  ADD ITEMS BEFORE DYING:")
            print(f"   {champ.name} is building {len(champ.current_building)} items.")
            self.add_one_item_to_unit(champ, item_index)
        return

    def fix_unknown(self) -> None:
        """Removes the first unknown unit that is on the board."""
        print("  Fixing unknown unit.")
        sleep(0.25)
        mk_functions.press_e(
            screen_coords.BOARD_LOC[self.board_slots_for_non_comp_units[0]].get_coords())
        self.board_unknown.pop(0)
        # Might set the wrong size because an unknown unit could have a size of two.
        self.set_board_size(self.board_size - 1)

    def remove_champion(self, champion: Champion) -> None:
        """Removes all instances of the given Champion from the bench if it is on the bench.
           Removes the given Champion from the list of units to purchase.
           Removes one instance of the given Champion from the board."""
        print(f"    Looking to remove {champion} from the bench, board, and list of champs to buy.")
        for index, slot in enumerate(self.bench):
            if isinstance(slot, Champion) and slot.name == champion.name:
                print(f"      Removing {champion} from the bench.")
                mk_functions.press_e(slot.coords)
                self.bench[index] = None

        self.champs_to_buy = list(filter(f"{champion.name}".__ne__,
                                         self.champs_to_buy))  # Remove all instances of champion in champs_to_buy

        mk_functions.press_e(champion.coords)
        if champion.name in self.board_names:
            self.board_names.remove(champion.name)
        if champion in self.board:
            if isinstance(champion, Champion):
                self.set_board_size(self.board_size - champion.size)
                self.board[self.board.index(champion)] = None
        if champion in self.board and isinstance(champion, Champion) and champion.name not in self.board_names:
            print(AnsiColors.RED_REGULAR + f"      [!] Unit {champion} is registered as in self.board, "
                                           f"but its name is not registered as in self.board_names." + AnsiColors.RESET)
        return

    def final_comp_check(self) -> None:
        """Checks the board and replaces champions not in final comp"""
        for slot in self.bench:
            if (
                    isinstance(slot, Champion)
                    and slot.final_comp
                    and slot.name not in self.board_names
            ):
                for champion in self.board:
                    if isinstance(champion, Champion):
                        if not champion.final_comp and champion.size == slot.size:
                            print(f"  Replacing non-final-comp {champion.name} with {slot.name}")
                            self.remove_champion(champion)
                            champion.print_all_class_variables()
                            self.move_known(slot)
                            break
        return

    def spend_gold(self) -> None:
        """Spends gold every round.
           Sets the minimum gold to spend based on the spam_roll class variables.
           If the bot has above the min gold, it will purchase unit if they are in the list of champs_to_buy
           and buying the unit would not make the amount of gold the bot has go into negative values.
           It will buy xp if not level 9, and mark a spot on the bench for the purchased units.
           """
        first_run = True
        min_buy_xp_gold = 54
        min_buy_unit_gold = 56
        if self.spam_roll:
            min_buy_xp_gold = 25
            min_buy_unit_gold = 27
        if self.spam_roll_to_zero:
            min_buy_xp_gold = 5
            min_buy_unit_gold = 7
        previous_shop: list = []
        infinite_loop_count = 0
        while first_run or (arena_functions.has_enough_gold_to_purchase_xp(min_buy_xp_gold) and self.is_allowed_to_purchase_xp()) \
                or arena_functions.has_enough_gold_to_reroll_shop(min_buy_unit_gold):
            if not first_run:
                if arena_functions.get_level_via_https_request() != 9 and arena_functions.has_enough_gold_to_purchase_xp(min_buy_xp_gold):
                    # If the comp we are playing is not Slow Roll we can buy xp, otherwise
                    # don't level up until we have bought at least 2 2-stars of the 3-star units we need.
                    if self.is_allowed_to_purchase_xp():
                        print("  Purchasing XP")
                        mk_functions.buy_xp()
                        self.update_level_via_ocr()
                if arena_functions.has_enough_gold_to_reroll_shop(min_buy_unit_gold):
                    mk_functions.reroll()
                    print("  Re-rolling shop")
            shop = arena_functions.get_shop()

            if collections.Counter(previous_shop) == collections.Counter(shop):
                infinite_loop_count += 1
            if infinite_loop_count >= 6:
                break
            previous_shop = shop

            print(f"    Shop: {shop}")
            for index, champion in enumerate(shop):
                if (champion in self.champs_to_buy and
                        arena_functions.get_gold() - game_assets.CHAMPIONS[champion]["Gold"] >= 0):
                    none_slot: int = arena_functions.empty_bench_slot()
                    if none_slot != -1:
                        mk_functions.left_click(screen_coords.BUY_LOC[index].get_coords())
                        print(f"    Purchased {champion}")
                        self.bought_champion(champion, none_slot)
                        if champion in self.champs_to_buy:
                            self.champs_to_buy.remove(champion)
                    else:
                        # Try to buy champ 3 when bench is full
                        print(f"  Bench is full but want {champion}")
                        mk_functions.left_click(screen_coords.BUY_LOC[index].get_coords())
                        game_functions.default_pos()
                        sleep(0.5)
                        self.fix_bench_state(True)
                        none_slot = arena_functions.empty_bench_slot()
                        sleep(0.5)
                        if none_slot != -1:
                            print(f"    Bench no longer full. Purchased {champion}")
                            if champion in self.champs_to_buy:
                                self.champs_to_buy.remove(champion)
            first_run = False
        return

    def pick_augment(self, have_rerolled: bool, secondary_augments: list) -> bool | list:
        """Picks an augment from user defined primary augments. If none from that list exist,
           it re-rolls any augments that aren't the defined secondary augments.
           It then tries to choose from any new primary and secondary augments again.
           If none exist, it picks the first augment on the left.
           Returns True if this function picked an augment non-randomly."""
        sleep(1.5)  # So that when I'm watching the screen I can actually read the augments' descriptions.
        # Print what augments are in the comp we're using.
        # if not have_rerolled:
            # print("      Primary Augments")
            # print(f"          {self.comp_to_play.primary_augments}")
            # print("      Secondary Augments")
            # print(f"          {self.comp_to_play.secondary_augments}")
        augments: list = []
        for coords in screen_coords.AUGMENT_POS:
            augment: str = ocr.get_text(screenxy=coords.get_coords(), scale=3, psm=7)
            augments.append(arena_functions.get_valid_augment(augment))
        print("  Augments to Choose From:")
        print(f"      {augments}")
        for augment in augments:
            if augment in self.comp_to_play.primary_augments:
                print(f"  Choosing Primary Augment:")
                print(f"    Augment: {augment}")
                mk_functions.left_click(screen_coords.AUGMENT_LOC[augments.index(augment)].get_coords())
                self.augments.append(augment)
                return True
            if augment in self.comp_to_play.secondary_augments:
                if have_rerolled:
                    print(f"  Choosing Secondary Augment:")
                    print(f"    Augment: {augment}")
                    mk_functions.left_click(screen_coords.AUGMENT_LOC[augments.index(augment)].get_coords())
                    self.augments.append(augment)
                    return True
                else:
                    print(f"    Adding {augment} to the list of secondary augments (to not re-roll).")
                    secondary_augments.append(augment)
            elif not have_rerolled:
                # print("    Adding nothing to the list of secondary augments.")
                secondary_augments.append(None)
        # Only share that there were augments saved if we actually saved augments.
        if not all(x is None for x in secondary_augments):
            print(f"    Secondary Augments:")
            print(f"        {secondary_augments}")
        if have_rerolled:
            print("  Returning the list of augments after re-rolling:")
            return augments
        # If we decided before game that we would re-roll augments, and we have not re-rolled the first augments yet.
        if self.augment_roll and not have_rerolled:
            print("  Re-rolling augments.")
            # Only re-rolls the augments that are not secondary augments.
            # If a primary augment was on the screen, it should have already been picked.
            for index, reroll_button in enumerate(screen_coords.AUGMENT_ROLL):
                if secondary_augments[index] is None:
                    mk_functions.left_click(reroll_button.get_coords())
            # if we successfully chose a primary or secondary augment
            response = self.pick_augment(True, secondary_augments)
            # need to explicitly verify that this is a bool because a non-empty list is truthy
            if isinstance(response, bool) and response:
                return True
            else:
                print("  None of the augments were a desired augment.")
                # if we didn't we pick the first augment on the left side of the screen,
                # we were returned the new list of augments
                if isinstance(response, list):
                    mk_functions.left_click(screen_coords.AUGMENT_LOC[0].get_coords())
                    print(f"    Augment Chosen: {response[0]}")
                    self.augments.append(response[0])
        return False

    def check_health(self) -> int:
        """Checks if current health is below 30 and conditionally activates spam roll"""
        health: int = arena_functions.get_health()
        if health > 0:
            print(f"    Health: {health}")
            if not self.spam_roll and health < 30:
                print("      Health under 30, spam roll activated")
                self.spam_roll = True
            if not self.spam_roll_to_zero and health < 13:
                print("      Health under 13, spam roll to zero activated")
                self.spam_roll_to_zero = True
        else:
            print("    Health check failed")
        return health

    def set_labels(self) -> None:
        """Gets labels used to display champion name UI on window"""
        labels: list = [
            # Create labels for units on the bench.
            (f"{slot.name}", slot.coords, 15, 30)
            for slot in self.bench
            if isinstance(slot, Champion)
        ]
        # Create labels for units on the board.
        for slot in self.board:
            if isinstance(slot, Champion):
                labels.append((f"{slot.name}", slot.coords, 15, 30))
        # Create labels for unknown units on the board.
        for index, name_and_pos in enumerate(self.board_unknown_and_pos):
            print(
                f" name_and_pos: {name_and_pos}, name_and_pos[0]: "
                f"{name_and_pos[0]}, "
                f"name_and_pos[1]: {name_and_pos[1]}"
            )
            labels.append(("u:" + str(name_and_pos[0]), screen_coords.BOARD_LOC[name_and_pos[1]].get_coords(), 15, 30))
        # Create label for level of the tactician.
        labels.append(
            (f"{arena_functions.get_level_via_ocr()}", screen_coords.TACTICIAN_LEVEL_LOC.get_coords(), -10, -10))
        # Create label for current gold.
        labels.append((f"{arena_functions.get_gold()}", screen_coords.GOLD_LOC.get_coords(), 5, -10))
        # Create label for how much it costs to buy XP.
        labels.append((f"{arena_functions.get_cost_to_buy_xp()}", screen_coords.BUY_XP_COST_LOC.get_coords(), -10, -10))
        # Create label for how much it costs to refresh the shop.
        labels.append((f"{arena_functions.get_cost_to_refresh_shop()}", screen_coords.REFRESH_LOC.get_coords(), 0, 0))
        # Create label for the current win/loss streak.
        labels.append(
            (f"{arena_functions.get_win_loss_streak()}",
             screen_coords.WIN_STREAK_LOSS_STREAK_AMOUNT_LOC.get_coords(), -25, -10))
        # Create label for the remaining time in this phase.
        labels.append((f"{arena_functions.get_seconds_remaining()}",
                       screen_coords.SECONDS_REMAINING_UNTIL_NEXT_STEP_LOC.get_coords(), 10, 20))
        # Create label for the current stage and round we are in.
        labels.append((f"{game_functions.get_round()}", screen_coords.ROUND_LOC.get_coords(), 100, -10))
        # Create label for the current xp / total needed xp.
        labels.append((f"{arena_functions.get_current_xp_and_total_needed_xp()}",
                       screen_coords.TACTICIAN_XP_FRACTION_LOC.get_coords(), 20, 5))
        # Create label for the current amount of units on the board.
        labels.append((f"{arena_functions.get_current_amount_of_units_on_board()}",
                       screen_coords.CURRENT_AMOUNT_OF_CHAMPIONS_ON_BOARD_LOC.get_coords(), 0, 0))
        # Create label for the max units amount of units we can have on the board.
        labels.append((f"{arena_functions.get_max_amount_of_units_on_board()}",
                       screen_coords.MAX_AMOUNT_OF_CHAMPIONS_ON_BOARD_LOC.get_coords(), 0, 0))
        # Create label for the item orbs.
        # for item_orb_vec2 in arena_functions.get_center_position_of_item_orbs():
        #     labels.append((f"Item Orb", item_orb_vec2.get_coords(), 0, 0))
        self.message_queue.put(("LABEL", labels))

    def count_items_on_bench(self) -> int:
        """Returns the number of items on the bench."""
        item_amount = 0
        for i in self.items:
            if i is not None:
                item_amount += 1
        return item_amount

    def is_same_amount_or_more_items_on_bench(self, item_amount_at_start: int) -> bool:
        """Returns a boolean representing if the current amount of items on the bench
           is greater than or equal to the given amount."""
        i = self.count_items_on_bench()
        if i >= item_amount_at_start:
            # print(f"    Started Item Amount: {item_amount_at_start}")
            # print(f"      Current Item Amount: {i}")
            return True
        return False

    def check_if_we_should_spam_sparring_gloves(self) -> bool:
        """Checks if our health is at 30 or less and then calls the function to spam thief's gloves."""
        health: int = arena_functions.get_health()
        if health <= 30:
            for champ in self.board:
                if isinstance(champ, Champion):
                    if len(champ.build) == 0:
                        if self.add_thiefs_gloves_to_champ(champ):
                            return True
        return False

    def check_if_we_should_spam_items_before_dying(self, index: int) -> bool:
        """Checks if our health is at 15 or less and then calls the function spam items before dying"""
        health: int = arena_functions.get_health()
        if health <= 15:
            self.add_item_to_champs_before_dying(index)
            return True
        return False

    def check_if_we_should_make_lucky_gloves(self) -> bool:
        """If we have the Lucky Gloves augment, place thief's gloves on a champion that doesn't build items."""
        if "Lucky Gloves" in self.augments:
            print("    We have Lucky Gloves!")
            no_build_champ = self.get_random_final_comp_champ_on_board_with_no_build()
            if no_build_champ is not None:
                if self.add_thiefs_gloves_to_champ(no_build_champ):
                    return True
        return False

    def get_random_final_comp_champ_on_board_with_no_build(self) -> Champion | None:
        print("    Looking for a random champ that we don't want to build items.")
        for champ in self.board:
            if isinstance(champ, Champion):
                if len(champ.build) == 0:
                    print(f"      {champ.name} is a unit that we haven't specified items for.")
                    return champ
        return None

    def identify_champions_on_board(self):
        """Identify units that are on the board. If they are a champion, we right-click them to verify.
           If this a unit that is on our board, we don't need to do anything else.
           If we have found a unit that is not a valid champ (most likely because it is not on our board)
           remove it from our list of units on our self.board and self.board_names."""
        print("  Identifying units on the board:")
        # Double-check the units we know are Champion objects.
        if bool(random.getrandbits(1)):  # testing this. we don't need to do this all the time
            for board_index, unit in enumerate(self.board):
                if isinstance(unit, Champion):
                    if not arena_functions.identify_one_champion_on_the_board(unit):
                        print(f"         Was not able to confirm that {unit.name} is still on the board.")
                        self.board[self.board.index(unit)] = None
                        self.board_names.remove(unit.name)
                        # don't think we need to reduce the board_size (amount of units we have on the board)
                        # here because this happens this function checks stuff after combat, so we should have the
                        # max amount of units/board_size on the board already.
                    else:
                        print(f"         Confirmed that {unit.name} is still on the board.")
        # If there are more units in our "board" than should exist.
        if len([unit for unit in self.board if unit is not None]) > self.max_board_size:
            self.remove_random_duplicate_champions_from_board()

    def identify_unknown_champions_on_board(self) -> [(str, int)]:
        """Gets where units are located on the board from the board_occupied_check,
           right-clicks that space to open up a potential info window.
           Looks for a unit name in that info window and if it is a valid unit, adds the units name to a list.
           Returns a list of names of any valid units on the board."""
        print("    Identifying unknown units on the board.")
        valid_champs = []
        units_on_board = self.board_occupied_check()
        for index, value in enumerate(units_on_board):
            if value:
                unit_name = arena_functions.identify_one_space_on_the_board(screen_coords.BOARD_LOC[index].get_coords())
                # If the unit doesn't exist, continue.
                # Or if the unit is a unit we know about,
                # just continue along so that we don't create duplicate units in self.board.
                if unit_name is None:
                    continue
                # If the unknown unit we are looking at is a known unit on the board, also continue.
                duplicate_unit = False
                if self.board[index] is not None and unit_name is self.board[index].name:
                    duplicate_unit = True
                    break
                if unit_name is not None and arena_functions.is_valid_champ(unit_name) and not duplicate_unit:
                    print(f"        Found a valid {unit_name} unit from an unknown unit!")
                    valid_champs.append((unit_name, index))
        # self.board_unknown_and_pos = valid_champs
        return valid_champs

    def remove_random_duplicate_champions_from_board(self):
        """Loops through the entire self.board list,
           and if a unit is a Champion object, but is sharing the same space as another Champion unit,
           removes the duplicate unit from the self.board list and the self.board_names list."""
        print("    Attempting to remove random duplicate champions from the board.")
        for board_index, unit in enumerate(self.board):
            positions_of_all_unit = []
            if isinstance(unit, Champion):
                # Just remove the first duplicate Champion unit from the self.board.
                if unit.board_position in positions_of_all_unit:
                    print(f"    Removing a duplicate {unit.name} from self.board.")
                    self.board[board_index] = None
                    self.board_names.remove(unit.name)
                    # don't think we need to reduce the board_size (amount of units we have on the board)
                    # here because this happens this function checks stuff after combat, so we should have the
                    # max amount of units/board_size on the board already.
                else:
                    positions_of_all_unit.append(unit.board_position)
        return

    def identify_champions_on_bench(self, mistaken_identity: bool = False):
        print("  Identifying units on the bench:")
        bench_occupied: list = arena_functions.bench_occupied_check()
        for index, bench_space in enumerate(self.bench):
            if bench_space is None and bench_occupied[index] and not mistaken_identity:
                print(f"  Bench space {index} is occupied by a unit, but we don't know which unit!")
                # Right-click the unit to make the unit's info appear on the right side of the screen.
                mk_functions.right_click(screen_coords.BENCH_LOC[index].get_coords())
                mk_functions.press_s()
                sleep(0.05)  # a delay to make sure the info popup has enough time to animate before ocr kicks in.
                champ_name: str = ocr.get_text(screenxy=screen_coords.SELECTED_UNIT_NAME_POS.get_coords(),
                                               scale=3, psm=8, whitelist=ocr.ALPHABET_WHITELIST)
                print(f"       Champ: {champ_name}")
                champ_name = arena_functions.get_valid_champ(champ_name)
                # Click at the default location so that the unit's info disappears.
                mk_functions.left_click(screen_coords.DEFAULT_LOC.get_coords())
                # Confirm this is an actual unit that can be used
                if arena_functions.is_valid_champ(champ_name):
                    print(f"        Found a valid {champ_name} unit on the bench!")
                    new_champion = champion_class.create_default_champion(champ_name, index, True, self.comp_to_play)
                    self.bench[index] = new_champion
                    # If we get units from item orbs or the carousel, we need to make sure they are accounted for too.
                    # They won't get accounted for if they are immediately merged into an upgrade unit though.
                    if new_champion.name in self.champs_to_buy:
                        self.champs_to_buy.remove(new_champion.name)
            elif isinstance(bench_space, Champion) and mistaken_identity:
                print(f"  Bench space {index} is occupied by a unit, but it is possibly labeled the wrong unit.")
                # Right-click the unit to make the unit's info appear on the right side of the screen.
                mk_functions.right_click(screen_coords.BENCH_LOC[index].get_coords())
                mk_functions.press_s()
                sleep(0.05)  # a delay to make sure the info popup has enough time to animate before ocr kicks in.
                champ_name: str = ocr.get_text(screenxy=screen_coords.SELECTED_UNIT_NAME_POS.get_coords(),
                                               scale=3, psm=8, whitelist=ocr.ALPHABET_WHITELIST)
                print(f"       Champ: {champ_name}")
                champ_name = arena_functions.get_valid_champ(champ_name)
                # Click at the default location so that the unit's info disappears.
                mk_functions.left_click(screen_coords.DEFAULT_LOC.get_coords())
                # Confirm this is an actual unit that can be used
                if arena_functions.is_valid_champ(champ_name) and bench_space.name != champ_name:
                    print(f"        A {champ_name} was labeled as a {bench_space.name}.")
                    new_champion = champion_class.create_default_champion(champ_name, index, True, self.comp_to_play)
                    self.bench[index] = new_champion
        mk_functions.right_click(screen_coords.TACTICIAN_RESTING_SPOT_LOC.get_coords())
        # called to make sure the tactician moves to their spot
        sleep(0.1)  # either need to remove or move out of function since this function is called in too many places

    def sell_non_comp_units_on_bench(self):
        """Sells any units on the bench that aren't in our comp,
           so long as the board is full and the unit that will be sold doesn't have a copy on the board."""
        print("  Selling non-comp units that are on the bench.")
        for index, unit_on_bench in enumerate(self.bench):
            if isinstance(unit_on_bench, Champion):
                if unit_on_bench.name not in self.comp_to_play.comp \
                        and self.board_size >= self.max_board_size \
                        and unit_on_bench.name not in self.board_names:
                    print(f"    Sold non-comp unit: {unit_on_bench} at bench index: {index}.")
                    self.sell_unit(unit_on_bench, index)
        return

    def sell_unit(self, unit: Champion, index: int) -> None:
        """Sell a single unit on the bench."""
        print(f"    Selling the {unit.name} at bench position {index}.")
        mk_functions.press_e(screen_coords.BENCH_LOC[index].get_coords())
        self.bench[index] = None

    def create_champion_object_from_unit_name_on_the_board(self, unit_name: str, index: int):
        """Given the unit's name and the location on the board it should be placed at.
           This function creates a Champion unit that has the designated items
           and final_comp value from the comps file and adds the unit to the board."""
        # Create the Champion object.
        new_champion = champion_class.create_default_champion(unit_name, index, False, self.comp_to_play)
        print(f"      Created the Champion object for the {unit_name}.")
        self.board_names.append(unit_name)
        self.set_board_size(self.board_size + new_champion.size)
        # Remove the unit that was unknown, and is now no longer unknown, from the unknown list.
        if unit_name in self.board_unknown:
            print(f"      Removing the unknown unit {unit_name} from the list of unknown units.")
            self.board_unknown.remove(unit_name)
        self.board[index] = new_champion

    def set_board_size(self, new_size: int) -> bool:
        """Sets how many units we have on the board.
           If the value we are trying to set is below zero, this function fails.
           Returns True if the board size was successfully set."""
        if new_size >= 0:
            print(f"      Setting the board size {self.board_size} to {new_size}.")
            self.board_size = new_size
            return True
        else:
            print("      The board size cannot be less than 0!")
        if new_size > self.max_board_size:
            print(f"      [!] Something has gone wrong. The current board size {self.board_size} is greater than the max board size {self.max_board_size}.")
        return False

    def give_items_to_units(self):
        """Loops through the units first so that we can add multiple items to one unit first,
           before moving onto the next unit."""
        print("  Giving items to units:")
        self.items = arena_functions.get_items()
        units_on_board_sorted_by_bis_items: list[Champion] = self.get_list_of_units_on_board_in_order_of_amount_of_total_bis_items()
        for unit in units_on_board_sorted_by_bis_items:
            if isinstance(unit, Champion):
                # try to give completed items first
                # for loop like this because a unit can have 3 complete/non-component items
                print(f"    Unit: {unit.name}, # of Item Slots Filled: {unit.item_slots_filled}, Items: {unit.items}")
                combined_two_items = False
                for i in range(unit.item_slots_filled, 6):
                    # can't give completed items if there aren't two slots or more available
                    if unit.item_slots_filled < 5:
                        self.add_ornn_item_to_unit(unit)
                        self.add_radiant_version_of_bis_items_to_unit(unit)
                        self.add_completed_item_to_unit(unit)
                        self.add_radiant_version_of_accepted_completed_items_to_unit(unit)
                        self.add_support_item_to_unit(unit)
                        self.add_trait_item_to_unit(unit)
                    if unit.item_slots_filled % 2 == 0:
                        combined_two_items = self.add_any_bis_item_from_combining_two_component_items_on_unit(unit)
                        # Start giving units their 'good but not BIS' items if our health gets too low or we have too many items
                        if unit.item_slots_filled < 5 and (arena_functions.get_health() <= 30 or len([item for item in self.items if item is not None]) == 10):
                            combined_two_items = combined_two_items or self.add_any_secondary_item_from_combining_two_component_items_on_unit(unit)
                if not combined_two_items:
                    print(f"            Unable to complete an item for {unit.name}.")
                # Zaun units can hold 3 Zaun mods.
                for j in range(len(unit.held_zaun_items), 3):
                    self.add_zaun_item_to_unit(unit)
                # Items removers can be used any number of times on one unit.
                self.throwaway_reforger_item(unit)
                self.throwaway_magnetic_remover_item(unit)
                self.use_champion_duplicators(unit)
                self.use_scroll_of_knowledge(unit)
                self.use_masterwork_upgrade(unit)

    def add_one_item_to_unit(self, unit: Champion, the_items_bench_index: int, consumable: bool = False):
        """Move the item from its location on the board to the unit.
           Prints out the name of the item and the unit it was placed on.
           Adds it to the units list of items it has.
           Removes the instance of the item from the board's list of items."""
        item = self.items[the_items_bench_index]
        arena_functions.move_item(screen_coords.ITEM_POS[the_items_bench_index][0].get_coords(), unit.coords)
        arena_functions.print_item_placed_on_champ(item, unit)
        if not consumable:
            unit.items.append(item)
        self.items[the_items_bench_index] = None

    def add_completed_item_to_unit(self, unit: Champion) -> None:
        """If we have completed items waiting on the bench,
        that are the unit's 'best_in_slot' (BIS items) give them to the unit."""
        for item_index, completed_item in enumerate(unit.build):
            if completed_item in self.items:
                self.add_one_item_to_unit(unit, self.items.index(completed_item))
                unit.item_slots_filled += 2
                unit.build.remove(completed_item)
                unit.non_component_items.append(completed_item)
        return

    def add_radiant_version_of_bis_items_to_unit(self, unit: Champion) -> None:
        """If we have radiant items waiting on the bench,
           that are a better version of the unit's completed items it WANTS to build
           (i.e. the 'best_in_slot' (BIS items), not just the completed items it will accept)
           give them to the unit."""
        for radiant_item, completed_item in game_assets.RADIANT_ITEMS_DICT.items():
            if completed_item in unit.build and radiant_item in self.items:
                self.add_one_item_to_unit(unit, self.items.index(radiant_item))
                unit.item_slots_filled += 2
                unit.build.remove(completed_item)
                unit.non_component_items.append(radiant_item)
        return

    def add_radiant_version_of_accepted_completed_items_to_unit(self, unit: Champion) -> None:
        """If we have radiant items waiting on the bench,
           that are a better version of the unit's items IT IS OK WITH, give them to the unit"""
        for radiant_item, completed_item in game_assets.RADIANT_ITEMS_DICT.items():
            if completed_item in unit.secondary_items and radiant_item in self.items:
                self.add_one_item_to_unit(unit, self.items.index(radiant_item))
                unit.item_slots_filled += 2
                unit.secondary_items.remove(completed_item)
                unit.non_component_items.append(radiant_item)
        return

    def add_ornn_item_to_unit(self, unit: Champion) -> None:
        """If there is an Ornn item on the bench that this unit wants, give it to 'em."""
        for ornn_item in unit.ornn_items_will_accept:
            if ornn_item in self.items:
                self.add_one_item_to_unit(unit, self.items.index(ornn_item))
                unit.item_slots_filled += 2
                unit.ornn_items_will_accept.remove(ornn_item)
                unit.non_component_items.append(ornn_item)
        return

    def add_support_item_to_unit(self, unit: Champion) -> None:
        """If there is a Support item on the bench that this unit wants, give it to 'em."""
        for support_item in unit.support_items_will_accept:
            if support_item in self.items:
                self.add_one_item_to_unit(unit, self.items.index(support_item))
                unit.item_slots_filled += 2
                unit.support_items_will_accept.remove(support_item)
                unit.non_component_items.append(support_item)
        return

    def add_trait_item_to_unit(self, unit: Champion) -> None:
        """If there is a trait emblem item on the bench that this unit wants, give it to 'em."""
        for trait_item in unit.trait_items_will_accept:
            if trait_item in self.items:
                self.add_one_item_to_unit(unit, self.items.index(trait_item))
                unit.item_slots_filled += 2
                unit.trait_items_will_accept.remove(trait_item)
                unit.non_component_items.append(trait_item)
        return

    def add_zaun_item_to_unit(self, unit: Champion) -> None:
        """If there is a Zaun item on the bench that this unit wants, give it to 'em."""
        for zaun_item in unit.zaun_items_will_accept:
            if zaun_item in self.items:
                self.add_one_item_to_unit(unit, self.items.index(zaun_item))
                unit.zaun_items_will_accept.remove(zaun_item)
                unit.held_zaun_items.append(zaun_item)
        return

    def pick_one_of_four_emblems_from_shop(self) -> int:
        """Returns the index position of the emblem in the shop that we want to pick.
           Prioritizes emblems by whether they are:
              1. an active trait in the final comp
                a. tries to grab the largest trait first
              2. an inactive trait that is in the final comp
              3. I guess next should just be random                    
        """
        # If one of the trait in our comp's list of ACTIVE traits
        # exists as an Emblem in the shop, return the index of that Emblem
        trait_emblem_names_in_shop = arena_functions.identify_emblems_in_shop()
        for trait in self.comp_to_play.active_final_comp_traits:
            trait_emblem = trait + "Emblem"
            if trait_emblem in trait_emblem_names_in_shop:
                emblem_shop_index = trait_emblem_names_in_shop.index(trait_emblem)
                print(f"    Prioritizing emblems that are for the most used ACTIVE traits in our final comp.")
                print(f"      Emblem: {trait_emblem}      Index in Shop: {emblem_shop_index}")
                return emblem_shop_index
            else:
                print(f"          An emblem for {trait} was not in the Tome of Traits shop.")
        # If one of the trait in our comp's list of INACTIVE traits
        # exists as an Emblem in the shop, return the index of that Emblem
        for trait in self.comp_to_play.inactive_final_comp_traits:
            trait_emblem = trait + "Emblem"
            if trait_emblem in trait_emblem_names_in_shop:
                emblem_shop_index = trait_emblem_names_in_shop.index(trait_emblem)
                print(f"    Grabbing an emblem for a INACTIVE trait in our final comp.")
                print(f"      Emblem: {trait_emblem}      Index in Shop: {emblem_shop_index}")
                return emblem_shop_index
            else:
                print(f"          An emblem for {trait} was not in the Tome of Traits shop.")

    def add_consumable_item_to_unit(self, unit: Champion, the_items_bench_index: int):
        """Simply calls the self.add_one_item_to_unit() function with a consumable value of True."""
        self.add_one_item_to_unit(unit, the_items_bench_index, True)

    def throwaway_reforger_item(self, unit: Champion) -> bool:
        """Simply tries to use a Reforger on a unit with 1 component item.
           Returns True if we used it."""
        if "Reforger" in self.items:
            if unit.item_slots_filled == 1:
                self.add_consumable_item_to_unit(unit, self.items.index("Reforger"))
                unit.item_slots_filled -= 1
                for item in unit.current_building:
                    unit.current_building.remove(item)
                    print(f"    {unit.name} is no longer trying to build {unit.current_building} due to a Reforger.")
                if unit.component_item != "":
                    print(f"    A Reforger removed {unit.component_item} from {unit.name} and changed it into a new item.")
                else:
                    print(f"    [!] We removed a component item from a unit, but we didn't know what component it was!")
                return True
            else:
                print("  Tried to throw away a Reforger on a nearly-itemless unit, "
                      "but couldn't find a nearly itemless unit.")
                return False
        return False

    def throwaway_magnetic_remover_item(self, unit: Champion) -> bool:
        """Simply tries to use a Magnetic Remover on a unit with 1 component items.
           Returns True if we used it."""
        if "MagneticRemover" in self.items:
            if unit.item_slots_filled == 1:
                self.add_consumable_item_to_unit(unit, self.items.index("MagneticRemover"))
                unit.item_slots_filled -= 1
                # Removes the tuple of (completed_item, needed_component_item) that the unit had.
                for item in unit.current_building:
                    unit.current_building.remove(item)
                    print(f"    {unit.name} is no longer trying to build {unit.current_building} due to a Magnetic Remover.")
                if unit.component_item != "":
                    print(f"    A Magnetic Remover removed {unit.component_item} from {unit.name}.")
                else:
                    print(f"    [!] We removed a component item from a unit, but we didn't know what component it was!")
                return True
            else:
                print("  Tried to throw away a Magnetic Remover on a nearly-itemless unit, "
                      "but couldn't find a nearly itemless unit.")
                return False
        return False

    def is_possible_to_combine_two_components_into_given_bis_item(self, unit: Champion, complete_item: str) -> bool:
        """Assumes that the complete item in the unit's build, exists as a CRAFTABLE item.
           Returns a boolean value that represent if BOTH component items for a complete item exist in self.items."""
        if complete_item not in unit.build:
            # print(f"        {complete_item} is not in  {unit.name}'s build.")
            return False
        if complete_item not in game_assets.CRAFTABLE_ITEMS_DICT:
            print(f"    You have misspelled {complete_item}.")
            return False
        copy_of_owned_items = self.items.copy()
        for item in game_assets.CRAFTABLE_ITEMS_DICT[complete_item]:
            if item not in copy_of_owned_items:
                # print(f"        We are missing a {item} to build the {complete_item}.")
                return False
            else:  # make sure for items that need duplicate component items, this doesn't count one component twice
                # print(f"        Removing the {item} from the copy of owned items, because we don't want to count items twice.")
                copy_of_owned_items.remove(item)
        return True

    def get_bis_item_that_is_possible_to_combine_from_components(self, unit: Champion) -> str | None:
        """Searches through the unit's BIS items it wants to build and returns the complete BIS item
           if it can be crafted from component items currently on the bench."""
        for complete_item in unit.build:
            # print(f"      For {complete_item} in {unit.name}'s build.")
            if self.is_possible_to_combine_two_components_into_given_bis_item(unit, complete_item):
                # print(f"        It is possible to create the {complete_item} for {unit}.")
                return complete_item
            else:
                # print(f"        It is not possible to craft the {complete_item} for {unit}.")
                continue
        return None

    def add_any_bis_item_from_combining_two_component_items_on_unit(self, unit: Champion) -> bool:
        """Assumes that the unit has no component items on them.
           Gets any Best In Slot (BIS) craftable item from the unit
           that we have determined we have both components for.
           Then adds both components to the unit to create a completed item."""
        complete_item = self.get_bis_item_that_is_possible_to_combine_from_components(unit)
        if complete_item is not None:
            # print(f"      Creating complete item: {complete_item} for {unit.name}.")
            component_one = game_assets.CRAFTABLE_ITEMS_DICT[complete_item][0]
            component_two = game_assets.CRAFTABLE_ITEMS_DICT[complete_item][1]
            self.add_one_item_to_unit(unit, self.items.index(component_one))
            self.add_one_item_to_unit(unit, self.items.index(component_two))
            unit.non_component_items.append(complete_item)
            unit.build.remove(complete_item)
            # Just make sure we don't give them the same item twice.
            if complete_item in unit.secondary_items:
                unit.secondary_items.remove(complete_item)
            unit.item_slots_filled += 2
            return True
        return False

    def is_possible_to_combine_two_components_into_given_secondary_item(self, unit: Champion, complete_item: str) -> bool:
        """Assumes that the complete item in the unit's build, exists as a CRAFTABLE item.
           Returns a boolean value that represent if BOTH component items for a complete item exist in self.items."""
        if complete_item not in unit.secondary_items:
            return False
        copy_of_owned_items = self.items.copy()
        for item in game_assets.CRAFTABLE_ITEMS_DICT[complete_item]:
            if item not in copy_of_owned_items:
                return False
            else:  # makes sure for items that need duplicate component items, this doesn't count one component twice
                copy_of_owned_items.remove(item)
        return True

    def get_secondary_item_that_is_possible_to_combine_from_components(self, unit: Champion) -> str | None:
        """Searches through the unit's BIS items it wants to build and returns the complete BIS item
           if it can be crafted from component items currently on the bench."""
        for complete_item in unit.secondary_items:
            if self.is_possible_to_combine_two_components_into_given_bis_item(unit, complete_item):
                return complete_item
            else:
                return None
        return

    def add_any_secondary_item_from_combining_two_component_items_on_unit(self, unit: Champion) -> bool:
        """Assumes that the unit has no component items on them.
           Gets any Best In Slot (BIS) craftable item from the unit
           that we have determined we have both components for.
           Then adds both components to the unit to create a completed item."""
        complete_item = self.get_secondary_item_that_is_possible_to_combine_from_components(unit)
        if complete_item is not None:
            print(f"      Creating complete secondary item: {complete_item} for {unit.name}.")
            component_one = game_assets.CRAFTABLE_ITEMS_DICT[complete_item][0]
            component_two = game_assets.CRAFTABLE_ITEMS_DICT[complete_item][1]
            self.add_one_item_to_unit(unit, self.items.index(component_one))
            self.add_one_item_to_unit(unit, self.items.index(component_two))
            unit.non_component_items.append(complete_item)
            unit.build.remove(complete_item)
            # Just make sure we don't give them the same item twice.
            if complete_item in unit.build:
                unit.build.remove(complete_item)
            unit.item_slots_filled += 2
            return True
        return False

    def get_list_of_units_on_board_in_order_of_amount_of_total_bis_items(self) -> list[Champion]:
        """Returns a list of Champion objects that are on the board,
           ordered by how many items they have listed in BIS, in descending order.
           Extremely unlikely, but the list might return as empty."""
        units_on_board_dict = {}
        for unit in self.board:
            if isinstance(unit, Champion):
                if unit.name in self.comp_to_play.comp:
                    unit_in_comp = self.comp_to_play.comp[unit.name]
                    units_on_board_dict[unit] = len(unit_in_comp["best_in_slot"])
        # using just Champion.build would mean that when a unit builds an item, they receive less priority
        return sorted(units_on_board_dict, key=units_on_board_dict.get, reverse=True)

    def get_index_of_one_lesser_champion_duplicators_on_bench(self) -> int | None:
        if "LesserChampionDuplicator" in self.items:
            return self.items.index("LesserChampionDuplicator")
        else:
            return None

    def get_index_of_one_champion_duplicators_on_bench(self) -> int | None:
        if "ChampionDuplicator" in self.items:
            return self.items.index("ChampionDuplicator")
        else:
            return None

    def use_champion_duplicators(self, unit: Champion) -> None:
        """Uses Champion Duplicators on units.
           Makes a list of all units that are on the board and that still need to be bought to be raised
           to the desire star level. Sorts that list of units, by the amount of items they need, in descending order
           so that we duplicate most important champions first.
           Will only use non-lesser champion duplicators on units that cost 4 or 5."""
        print("    Looking for champion duplicators.")
        lesser_duplicator_index = self.get_index_of_one_lesser_champion_duplicators_on_bench()
        normal_duplicator_index = self.get_index_of_one_champion_duplicators_on_bench()
        # Exit the function sooner if we don't have any champion duplicators
        if lesser_duplicator_index is None and normal_duplicator_index is None:
            return
        print("    We have champion duplicators to use.")
        if unit.name in self.champs_to_buy and unit.name in game_assets.CHAMPIONS:
            unit_dict = game_assets.CHAMPIONS[unit.name]
            # print(f"      Unit Dict: {unit_dict}")
            cost = unit_dict["Gold"]
            # print(f"        Cost: {cost}")
            if cost <= 3 and lesser_duplicator_index is not None:
                self.add_one_item_to_unit(unit, lesser_duplicator_index, True)
            elif (cost > 3 or self.comp_to_play.strategy == "Slow Roll") and normal_duplicator_index is not None:
                self.add_one_item_to_unit(unit, normal_duplicator_index, True)
        return

    def use_scroll_of_knowledge(self, unit: Champion) -> None:
        """Uses a Scroll of Knowledge on a unit.
           Uses it on the first unit with the most BIS items,
           as I'm guessing those units will have the most traits active
           and therefore make the most value out of getting an Emblem of one of their traits.
           This function doesn't select the Emblem from the Armory shop."""
        print("    Try using Scroll of Knowledge.")
        if "ScrollofKnowledge" not in self.items:
            return
        self.add_one_item_to_unit(unit, self.items.index("ScrollofKnowledge"))

    def use_masterwork_upgrade(self, unit: Champion) -> None:
        """Uses a Masterwork Upgrade on a unit.
           Uses it on the first unit with the most BIS items, since the item upgrades craftable completed items
           to Radiant versions. This will fail if the unit isn't holding any completed items.
           This function doesn't select the item from the Armory shop."""
        print("    Try using Masterwork Upgrade.")
        if "MasterworkUpgrade" not in self.items:
            return
        if len(unit.non_component_items) > 0:
            self.add_one_item_to_unit(unit, self.items.index("MasterworkUpgrade"))

    def add_random_items_on_strongest_units_at_one_loss_left(self):
        """This function tries to add all the leftover items on the board before the bot loses the game.
           It focuses on placing items onto the most important units, as defined by how many BIS items they have in their comp file.
           It will place the strongest items first (e.g. Ornn Artifact Items and Radiant Items).
           Then place the normal completed items, because it's most likely those will help the damage-dealing carries the most.
           Then emblem items and support items. Hopefully by the time we are placing those items
             we are giving them to non-carries that will buff the carries.
           Then we take the remaining Mogul items and component items and try to give them too.
        """
        if self.check_health() > 16:
            return
        print("  Randomly adding items to our carry units since we are about to lose.")
        units_on_board_sorted_by_bis_items: list[Champion] = self.get_list_of_units_on_board_in_order_of_amount_of_total_bis_items()
        for unit in units_on_board_sorted_by_bis_items:
            # Zaun items don't care about your other items
            # Only put Zaun items on units with less than 3 of them, and their comp file already listed them as accepting zaun items.
            if unit in self.comp_to_play.comp and len(unit.held_zaun_items) < 3 \
                    and len(self.comp_to_play.comp[unit.name]["zaun_items_to_accept"]) > 0:
                print("    END GAME: Looking to add Zaun Items.")
                for item in game_assets.ZAUN_ITEMS:
                    if item in self.items:
                        self.add_one_item_to_unit(unit, self.items.index(item))
                        unit.held_zaun_items.append(item)
                        unit.zaun_items_will_accept.remove(item)
            # We don't need to add items to units with max items.
            if unit.item_slots_filled >= 6:
                print(f"    Unit: {unit.name} has an item_slots_filled value of {unit.item_slots_filled}. Continuing...")
                continue
            # Give non-component items first.
            if unit.item_slots_filled % 2 == 0:
                print("    END GAME: Looking to add Ornn, Radiant, Completed, Emblem, Support, and Mogul Items.")
                # try to place all the ornn items first...
                for item in game_assets.ORNN_ITEMS:
                    if item in self.items and unit.item_slots_filled < 6:
                        self.add_one_item_to_unit(unit, self.items.index(item))
                        unit.non_component_items.append(item)
                        if item in unit.ornn_items_will_accept:
                            unit.ornn_items_will_accept.remove(item)
                        unit.item_slots_filled += 2
                # then try to place all the radiant items next...
                for item in game_assets.RADIANT_ITEMS:
                    if item in self.items and unit.item_slots_filled < 6:
                        self.add_one_item_to_unit(unit, self.items.index(item))
                        unit.non_component_items.append(item)
                        if item in unit.build:
                            unit.build.remove(item)
                        if item in unit.secondary_items:
                            unit.secondary_items.remove(item)
                        unit.item_slots_filled += 2
                # and so on...
                for item in game_assets.CRAFTABLE_NON_EMBLEM_ITEMS:
                    if item in self.items and unit.item_slots_filled < 6:
                        self.add_one_item_to_unit(unit, self.items.index(item))
                        unit.non_component_items.append(item)
                        if item in unit.build:
                            unit.build.remove(item)
                        if item in unit.secondary_items:
                            unit.secondary_items.remove(item)
                        unit.item_slots_filled += 2
                # put emblem items after crafted completed items, because we are looking at our carries first
                for item in game_assets.CRAFTABLE_EMBLEM_ITEMS:
                    if item in self.items and unit.item_slots_filled < 6:
                        self.add_one_item_to_unit(unit, self.items.index(item))
                        unit.non_component_items.append(item)
                        if item in unit.trait_items_will_accept:
                            unit.trait_items_will_accept.remove(item)
                        unit.item_slots_filled += 2
                # this is here for same reasoning as CRAFTABLE_EMBLEM_ITEMS
                for item in game_assets.SUPPORT_ITEMS:
                    if item in self.items and unit.item_slots_filled < 6:
                        self.add_one_item_to_unit(unit, self.items.index(item))
                        unit.non_component_items.append(item)
                        if item in unit.support_items_will_accept:
                            unit.support_items_will_accept.remove(item)
                        unit.item_slots_filled += 2
                for item in game_assets.MOGUL_ITEMS:
                    if item in self.items:
                        self.add_one_item_to_unit(unit, self.items.index(item))
                        unit.non_component_items.append(item)
                        unit.item_slots_filled += 2
            for item in game_assets.COMPONENT_ITEMS:
                if item in self.items:
                    print("    END GAME: Looking to add component items.")
                    if unit.item_slots_filled % 2 == 0:
                        unit.component_item = item
                    else:
                        for current_building in unit.current_building:
                            print(f"    The unit {unit.name} was trying to build a {current_building}")
                            print(f"      But we gave them a {item} component item instead.")
                            unit.current_building.remove(unit.current_building)
                        unit.component_item = ""
                        if len(unit.items) != 0:
                            unit.items.pop()
                    self.add_one_item_to_unit(unit, self.items.index(item))
                    unit.item_slots_filled += 1

    def increase_level(self):
        print(f"  Increasing the level of the tactician from {self.level} to {self.level+1}.")
        self.level += 1

    # This is unreliable.
    def update_level_via_https_request(self) -> None:
        current_level = self.level
        if arena_functions.get_level_via_https_request() > current_level:
            self.increase_level()
            self.increase_max_board_size()

    def update_level_via_ocr(self) -> None:
        """Uses the OCR function to get the level of the tactician and uses that info to update class variables."""
        # Do a subtraction check instead of just checking if it's greater than,
        # incase the OCR messes up, like reading a 2 as a 9.
        difference = arena_functions.get_level_via_ocr() - self.level
        if 1 <= difference <= 3:
            self.increase_level()
            self.increase_max_board_size()

    def buy_xp_round(self) -> None:
        """Buys XP if gold is equals or over 4"""
        if arena_functions.get_gold() >= 4:
            mk_functions.buy_xp()
            self.update_level_via_ocr()

    def increase_max_board_size(self) -> None:
        print(f"  Increasing the max board size from {self.max_board_size} to {self.max_board_size+1}.")
        self.max_board_size += 1

    def board_occupied_check(self) -> list:
        """Returns a list of booleans that map to each board slot indicating if it's occupied by a unit.
            Does this by looping through the screen coordinates defined as where health bars would appear,
            and checking if that position matches the specific color of health bars.
        """
        board_occupied: list = []
        labels = []
        for index, positions in enumerate(screen_coords.BOARD_HEALTH_POS):
            screen_capture = ImageGrab.grab(bbox=positions.get_coords())
            screenshot_array = np.array(screen_capture)
            if not (np.abs(screenshot_array - (0, 255, 18)) <= 2).all(axis=2).any():
                board_occupied.append(False)
                # labels.append(("False", screen_coords.BOARD_LOC[index].get_coords(), 0, 0))  # it just clutters the screen
            else:
                board_occupied.append(True)
                labels.append(("True", screen_coords.BOARD_LOC[index].get_coords(), 0, 0))
        self.message_queue.put(("LABEL", labels))
        return board_occupied

    def is_allowed_to_purchase_xp(self):
        """Don't buy xp on Slow Roll comps if our level is
           above the optimum level for buying the cost of the units we need to 3-star,
           and we still need to buy those units"""
        if self.comp_to_play.strategy == "Slow Roll":
            three_star_unit_costs = self.get_the_costs_of_unit_we_want_to_three_star()
            for unit, cost in three_star_unit_costs.items():
                if self.level > game_assets.LEVELS_WITH_BEST_ODDS_PER_UNIT_COST_DICT[cost] and unit in self.champs_to_buy:
                    print(f"       Level: {self.level}")
                    return False
                else:
                    return True
        return True

    def get_the_costs_of_unit_we_want_to_three_star(self):
        """Returns a dict of the units we want to three star as keys and their costs as values."""
        costs_of_units_to_three_star = {}
        for unit, unit_data in self.comp_to_play.comp.items():
            if unit_data["level"] == 3:
                costs_of_units_to_three_star[unit] = game_assets.champion_gold_cost(unit)
        return costs_of_units_to_three_star