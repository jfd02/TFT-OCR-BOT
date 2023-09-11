"""
Handles the board / bench state inside of the game and
other variables used by the bot to make decisions
"""

from time import sleep
import random

import game_assets
import mk_functions
import screen_coords
from champion import Champion
import comps
import ocr
import game_functions
import arena_functions


class Arena:
    """Arena class that handles game logic such as board and bench state"""

    # pylint: disable=too-many-instance-attributes,too-many-public-methods
    def __init__(self, message_queue) -> None:
        self.message_queue = message_queue
        # How many units we are currently fielding.
        self.board_size = 0
        self.bench: list[None] = [None, None, None, None, None, None, None, None, None]
        # All the spaces of the board. Can be an instance of a Champion or None.
        self.board: list = []
        # All the spaces on the board that have a unit, but we don't know what that unit is.
        self.board_unknown: list = []
        # All the spaces on the board that we haven't designated to put a unit from our comp on.
        self.board_slots_for_non_comp_units: list = comps.get_unknown_slots()
        self.champs_to_buy: list = comps.champions_to_buy()
        # A list of the names of all units on the board (not the bench), including duplicates.
        self.board_names: list = []
        self.items: list = []
        # All the augments that the player currently has.
        self.augments: list = []
        self.final_comp = False
        self.level = 0
        self.augment_roll = True
        self.spam_roll = False
        self.spam_roll_to_zero = False

    def fix_bench_state(self) -> None:
        """Iterates through bench and fixes invalid slots"""
        self.identify_champions_on_bench()
        bench_occupied: list = arena_functions.bench_occupied_check()
        for index, slot in enumerate(self.bench):
            if slot is None and bench_occupied[index]:
                self.bench[index] = "?"
            if isinstance(slot, str) and not bench_occupied[index]:
                print(f"  [!]fix_bench_state slot isinstance str\n    slot:{slot}")
                self.bench[index] = None
            if isinstance(slot, Champion) and not bench_occupied[index]:
                # surely this should never happen?
                print(f"  [!!!]fix_bench_state slot isinstance Champion")
                print(f"         slot:{slot}")
                print(f"         unit name:{slot.name}")
                self.bench[index] = None

    def bought_champion(self, name: str, slot: int) -> None:
        """Purchase champion and creates champion instance"""
        self.bench[slot] = Champion(name=name,
                                    coords=screen_coords.BENCH_LOC[slot].get_coords(
                                    ),
                                    build=comps.COMP[name]["items"].copy(),
                                    slot=slot,
                                    size=game_assets.CHAMPIONS[name]["Board Size"],
                                    final_comp=comps.COMP[name]["final_comp"])
        mk_functions.move_mouse(screen_coords.DEFAULT_LOC.get_coords())
        sleep(0.5)
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
                and champion.name in comps.COMP
            ),
            None,
        )

    def move_known(self, champion: Champion) -> None:
        """Moves champion to the board"""
        print(f"    Moving known unit {champion.name} to board.")
        board_position = -1
        # If the unit is in our comp. Put it in its designated spot on the board.
        if champion.name in comps.COMP:
            print("      Selecting the designated board space because the unit is in our comp.")
            board_position = comps.COMP[champion.name]["board_position"]
        # Otherwise, put it in a random spot on the board that our wanted units won't use.
        # Might accidentally replace an unwanted unit with this one.
        else:
            print("      Selecting a random board space because the unit isn't in our comp.")
            board_position = random.choice(self.board_slots_for_non_comp_units)
        destination: tuple = screen_coords.BOARD_LOC[board_position].get_coords()
        mk_functions.left_click(champion.coords)
        sleep(0.1)
        mk_functions.left_click(destination)
        champion.coords = destination
        self.board.append(champion)
        self.board_names.append(champion.name)
        if champion.index >= len(self.bench):
            print(f"      [!] The index {champion.index} of unit {champion.name} "
                  f"is larger than the length of the bench.")
        else:
            self.bench[champion.index] = None
        champion.index = board_position
        self.board_size += champion.size
        print(f"      Moved {champion.name} to {board_position}.")
        print(f"        There are now {self.board_size} units on the board.")

    def move_unknown(self) -> None:
        """Moves unknown champion to the board"""
        for index, champion in enumerate(self.bench):
            if isinstance(champion, str):
                print(f"    Moving unknown unit {champion} from bench slot {index} "
                      f"to board space {self.board_slots_for_non_comp_units[len(self.board_unknown)]}.")
                mk_functions.left_click(screen_coords.BENCH_LOC[index].get_coords())
                sleep(0.1)
                mk_functions.left_click(
                    screen_coords.BOARD_LOC[self.board_slots_for_non_comp_units[len(self.board_unknown)]].get_coords())
                self.bench[index] = None
                self.board_unknown.append(champion)
                self.board_size += 1
                print(f"      There are now {self.board_size} units on the board.")
                return

    def sell_bench(self) -> None:
        """Sells all of the champions on the bench"""
        print(f"    Selling all the units on the bench.")
        for index, _ in enumerate(self.bench):
            mk_functions.press_e(screen_coords.BENCH_LOC[index].get_coords())
            self.bench[index] = None

    def unknown_in_bench(self) -> bool:
        """Returns True if there is a spot on the bench taken up and that spot is not recognized as a champion/unit."""
        return any(isinstance(slot, str) for slot in self.bench)

    def move_champions(self) -> None:
        """Moves champions to the board"""
        self.level: int = arena_functions.get_level_via_https_request()
        while self.level > self.board_size:
            champion: Champion | None = self.get_next_champion_on_bench()
            if champion is not None:
                self.move_known(champion)
            elif self.unknown_in_bench():
                self.move_unknown()
            else:
                bought_unknown = False
                shop: list = arena_functions.get_shop()
                for champion in shop:
                    gold: int = arena_functions.get_gold()
                    valid_champ: bool = (
                            champion[1] in game_assets.CHAMPIONS and
                            game_assets.champion_gold_cost(champion[1]) <= gold and
                            game_assets.champion_board_size(champion[1]) == 1 and
                            champion[1] not in self.champs_to_buy and
                            champion[1] not in self.board_unknown
                    )

                    if valid_champ:
                        none_slot: int = arena_functions.empty_bench_slot()
                        mk_functions.left_click(screen_coords.BUY_LOC[champion[0]].get_coords())
                        sleep(0.2)
                        self.bench[none_slot] = f"{champion[1]}"
                        self.move_unknown()
                        bought_unknown = True
                        break

                if not bought_unknown:
                    print("  Need to sell entire bench to keep track of board")
                    self.sell_bench()
                    return

    def replace_unknown(self) -> None:
        """Replaces an unknown champion on the board with a known champion from the bench."""
        champion: Champion | None = self.get_next_champion_on_bench()
        if len(self.board_unknown) > 0 and champion is not None:
            print(f"    Replacing an unknown champion with {champion.name}.")
            mk_functions.press_e(screen_coords.BOARD_LOC[self.board_slots_for_non_comp_units[len(
                self.board_unknown) - 1]].get_coords())
            self.board_unknown.pop()
            self.board_size -= 1
            self.move_known(champion)

    def replace_units_not_in_our_comp(self) -> None:
        """Replaces a unit on the board with a unit from the bench that is in our comp."""
        champion: Champion | None = self.get_next_unit_from_our_comp_on_bench()
        if champion is None:
            return
        for unit in self.board:
            if isinstance(unit, Champion):
                if unit.name not in comps.COMP:
                    print(f"    Replacing {unit.name} with {champion.name} because {unit.name} is not in our comp.")
                    mk_functions.press_e(unit.coords)
                    self.board_size -= 1
                    self.move_known(champion)

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

    def clear_anvil(self) -> None:
        """Clears anvil on the bench, selects middle item"""
        print("  Looking for anvils to sell.")
        for index, champion in enumerate(self.bench):
            if champion is None:
                mk_functions.press_e(screen_coords.BENCH_LOC[index].get_coords())
        sleep(0.2)
        mk_functions.left_click(screen_coords.BUY_LOC[2].get_coords())

    def place_items(self) -> None:
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
            for index, _ in enumerate(self.items):
                if self.items[index] is not None:
                    item = self.items[index]
                    if item in game_assets.ORNN_ITEMS:
                        print(f"    Found an Ornn Item: {item}")
                        self.add_item_to_champs(index)
                        if self.is_same_amount_or_more_items_on_bench(item_amount_at_start):
                            will_try_to_place_item = False
                        if self.check_if_we_should_spam_items_before_dying(index):
                            if self.is_same_amount_or_more_items_on_bench(item_amount_at_start):
                                will_try_to_place_item = False
                    if item in game_assets.FULL_ITEMS:
                        print(f"    Found a Completed Item: {item}")
                        self.add_item_to_champs(index)
                        if self.is_same_amount_or_more_items_on_bench(item_amount_at_start):
                            will_try_to_place_item = False
                        if self.check_if_we_should_spam_items_before_dying(index):
                            if self.is_same_amount_or_more_items_on_bench(item_amount_at_start):
                                will_try_to_place_item = False
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

    def add_item_to_champs(self, item_index: int) -> None:
        """Iterates through champions in the board and checks if the champion needs items"""
        for champ in self.board:
            if champ.does_need_items() and self.items[item_index] is not None:
                self.add_item_to_champ(item_index, champ)

    def add_item_to_champ(self, item_index: int, champ: Champion) -> None:
        """Takes item index and champ and applies the item"""
        item = self.items[item_index]
        if item in game_assets.FULL_ITEMS:
            if item in champ.build:
                mk_functions.left_click(
                    screen_coords.ITEM_POS[item_index][0].get_coords())
                mk_functions.left_click(champ.coords)
                arena_functions.print_item_placed_on_champ(item, champ)
                champ.completed_items.append(item)
                champ.build.remove(item)
                self.items[self.items.index(item)] = None
        elif len(champ.current_building) == 0:
            item_to_move: None = None
            for build_item in champ.build:
                build_item_components: list = list(
                    game_assets.FULL_ITEMS[build_item])
                if item in build_item_components:
                    item_to_move: None = item
                    build_item_components.remove(item_to_move)
                    champ.current_building.append(
                        (build_item, build_item_components[0]))
                    champ.build.remove(build_item)
            if item_to_move is not None:
                mk_functions.left_click(
                    screen_coords.ITEM_POS[item_index][0].get_coords())
                mk_functions.left_click(champ.coords)
                arena_functions.print_item_placed_on_champ(item, champ)
                self.items[self.items.index(item)] = None
        else:
            for builditem in champ.current_building:
                if item == builditem[1]:
                    mk_functions.left_click(
                        screen_coords.ITEM_POS[item_index][0].get_coords())
                    mk_functions.left_click(champ.coords)
                    champ.completed_items.append(builditem[0])
                    champ.current_building.clear()
                    self.items[self.items.index(item)] = None
                    arena_functions.print_item_placed_on_champ(item, champ)
                    print(f"  Completed {builditem[0]}")
                    return

    def add_thiefs_gloves_to_champ(self, champ: Champion) -> bool:
        """Makes Thiefs Gloves if possible and gives them to a champ with no items."""
        print("  Attempting to add Thiefs Gloves to a random itemless champ.")
        gloves_index_1 = -1
        gloves_index_2 = -1
        for index, _ in enumerate(self.items):
            if self.items[index] == "SparringGloves":
                if gloves_index_1 == -1:
                    gloves_index_1 = index
                if gloves_index_1 != -1 and gloves_index_2 == -1:
                    gloves_index_2 = index
        if gloves_index_1 != -1 and gloves_index_2 != -1 and gloves_index_1 != gloves_index_2:
            mk_functions.left_click(
                screen_coords.ITEM_POS[gloves_index_1][0].get_coords())
            mk_functions.left_click(champ.coords)
            print(f"    Placed {self.items[gloves_index_1]} on {champ.name}")
            self.items[gloves_index_1] = None
            mk_functions.left_click(
                screen_coords.ITEM_POS[gloves_index_2][0].get_coords())
            mk_functions.left_click(champ.coords)
            print(f"    Placed {self.items[gloves_index_2]} on {champ.name}")
            self.items[gloves_index_2] = None
            return True
        return False

    def add_item_to_champs_before_dying(self, item_index: int) -> None:
        """Iterates through champions in the board and checks if the champion needs items"""
        print("    Adding items to champs before dying.")
        for champ in self.board:
            if champ.does_need_items() and self.items[item_index] is not None:
                self.add_item_before_dying(item_index, champ)

    def add_item_before_dying(self, item_index: int, champ: Champion) -> None:
        """Takes the remaining full items and gives them to champs that already have items.
            Then takes remaining component items and tries to give them to champs that already have items.
        """
        # print("  Found a champ to add an item to before dying.")
        item = self.items[item_index]
        if item in game_assets.ORNN_ITEMS:
            if champ.does_need_items():
                mk_functions.left_click(
                    screen_coords.ITEM_POS[item_index][0].get_coords())
                mk_functions.left_click(champ.coords)
                arena_functions.print_item_placed_on_champ(item, champ)
                champ.completed_items.append(item)
                self.items[self.items.index(item)] = None
        if item in game_assets.FULL_ITEMS:
            if champ.does_need_items():
                mk_functions.left_click(
                    screen_coords.ITEM_POS[item_index][0].get_coords())
                mk_functions.left_click(champ.coords)
                arena_functions.print_item_placed_on_champ(item, champ)
                champ.completed_items.append(item)
                self.items[self.items.index(item)] = None
        if len(champ.current_building) != 0:
            print("  ADD ITEMS BEFORE DYING:")
            print(f"     {champ.name} is building {len(champ.current_building)} items.")
            mk_functions.left_click(
                screen_coords.ITEM_POS[item_index][0].get_coords())
            mk_functions.left_click(champ.coords)
            arena_functions.print_item_placed_on_champ(item, champ)
            self.items[self.items.index(item)] = None

    def fix_unknown(self) -> None:
        """Removes the first unknown unit that is on the board."""
        sleep(0.25)
        mk_functions.press_e(
            screen_coords.BOARD_LOC[self.board_slots_for_non_comp_units[0]].get_coords())
        self.board_unknown.pop(0)
        self.board_size -= 1

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
            self.board_size -= champion.size
            self.board.remove(champion)
        if champion in self.board and champion.name not in self.board_names:
            print(f"      [!] Unit {champion} is registered as in self.board, but its name is not registered as in "
                  f"self.board_names.")

    def final_comp_check(self) -> None:
        """Checks the board and replaces champions not in final comp"""
        for slot in self.bench:
            if (
                    isinstance(slot, Champion)
                    and slot.final_comp
                    and slot.name not in self.board_names
            ):
                for champion in self.board:
                    if not champion.final_comp and champion.size == slot.size:
                        print(f"  Replacing non-final-comp {champion.name} with {slot.name}")
                        self.remove_champion(champion)
                        champion.print_all_class_variables()
                        self.move_known(slot)
                        break

    def tacticians_crown_check(self) -> None:
        """Checks if the item from carousel is tacticians crown"""
        mk_functions.move_mouse(screen_coords.ITEM_POS[0][0].get_coords())
        sleep(0.5)
        item: str = ocr.get_text(screenxy=screen_coords.ITEM_POS[0][1].get_coords(), scale=3, psm=13,
                                 whitelist=ocr.ALPHABET_WHITELIST)
        item: str = arena_functions.valid_item(item)
        try:
            if "TacticiansCrown" in item:
                print("  Tacticians Crown on bench, adding extra slot to board")
                self.board_size -= 1
            else:
                print(f"{item} is not TacticiansCrown")
        except TypeError:
            print("  Item could not be read for Tacticians Check")

    def spend_gold(self) -> None:
        """Spends gold every round"""
        first_run = True
        min_gold = 54
        if self.spam_roll:
            min_gold = 25
        if self.spam_roll_to_zero:
            min_gold = 6
        while first_run or arena_functions.get_gold() >= min_gold:
            if not first_run:
                if arena_functions.get_level_via_https_request() != 9:
                    mk_functions.buy_xp()
                    print("  Purchasing XP")
                mk_functions.reroll()
                print("  Re-rolling shop")
            shop: list = arena_functions.get_shop()
            print(f"  Shop: {shop}")
            for champion in shop:
                if (champion[1] in self.champs_to_buy and
                        arena_functions.get_gold() - game_assets.CHAMPIONS[champion[1]]["Gold"] >= 0
                ):
                    none_slot: int = arena_functions.empty_bench_slot()
                    if none_slot != -1:
                        mk_functions.left_click(screen_coords.BUY_LOC[champion[0]].get_coords())
                        print(f"    Purchased {champion[1]}")
                        self.bought_champion(champion[1], none_slot)
                        self.champs_to_buy.remove(champion[1])
                    else:
                        # Try to buy champ 3 when bench is full
                        print(f"  Board is full but want {champion[1]}")
                        mk_functions.left_click(screen_coords.BUY_LOC[champion[0]].get_coords())
                        game_functions.default_pos()
                        sleep(0.5)
                        self.fix_bench_state()
                        none_slot = arena_functions.empty_bench_slot()
                        sleep(0.5)
                        if none_slot != -1:
                            print(f"    Purchased {champion[1]}")
                            self.champs_to_buy.remove(champion[1])
            first_run = False

    def pick_augment(self) -> None:
        """Picks an augment from user defined augment priority list or defaults to first augment"""
        sleep(5)
        augments: list = []
        for coords in screen_coords.AUGMENT_POS:
            augment: str = ocr.get_text(screenxy=coords.get_coords(), scale=3, psm=7)
            augments.append(augment)

        for augment in augments:
            for potential in comps.AUGMENTS:
                if potential in augment:
                    print(f"  Choosing augment.")
                    print(f"    Augment: {augment}")
                    mk_functions.left_click(screen_coords.AUGMENT_LOC[augments.index(augment)].get_coords())
                    self.augments.append(augment)
                    return

        if self.augment_roll:
            print("  Rolling for augment")
            for reroll_button in screen_coords.AUGMENT_ROLL:
                mk_functions.left_click(reroll_button.get_coords())
            self.augment_roll = False
            self.pick_augment()

        print("  [!] No priority or backup augment found, undefined behavior may occur for the rest of the round")
        mk_functions.left_click(screen_coords.AUGMENT_LOC[0].get_coords())

    def check_health(self) -> None:
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
        labels.extend(
            (slot, screen_coords.BOARD_LOC[self.board_slots_for_non_comp_units[index]].get_coords(), 15, 30)
            for index, slot in enumerate(self.board_unknown)
        )
        # Create label for level of the tactician.
        labels.append((f"{arena_functions.get_level_via_ocr()}", screen_coords.TACTICIAN_LEVEL_LOC.get_coords(), 0, 0))
        # Create label for current gold.
        labels.append((f"{arena_functions.get_gold()}", screen_coords.GOLD_LOC.get_coords(), 0, 0))
        # Create label for how much it costs to buy XP.
        labels.append((f"{arena_functions.get_cost_to_buy_xp()}", screen_coords.BUY_XP_COST_LOC.get_coords(), 0, 0))
        # Create label for how much it costs to refresh the shop.
        labels.append((f"{arena_functions.get_cost_to_refresh_shop()}", screen_coords.REFRESH_LOC.get_coords(), 0, 0))
        # Create label for the current win/loss streak.
        labels.append(
            (f"{arena_functions.get_win_loss_streak()}",
             screen_coords.WIN_STREAK_LOSS_STREAK_AMOUNT_LOC.get_coords(), 0, 0))
        # Create label for the remaining time in this phase.
        labels.append((f"{arena_functions.get_seconds_remaining()}",
                       screen_coords.SECONDS_REMAINING_UNTIL_NEXT_STEP_LOC.get_coords(), 0, 0))
        # Create label for the current stage and round we are in.
        labels.append((f"{game_functions.get_round()}", screen_coords.ROUND_LOC.get_coords(), 0, 0))
        # Create label for the current xp / total needed xp.
        labels.append((f"{arena_functions.get_current_xp_and_total_needed_xp()}",
                       screen_coords.TACTICIAN_XP_FRACTION_LOC.get_coords(), 0, 0))
        # Create label for the current amount of units on the board.
        labels.append((f"{arena_functions.get_current_amount_of_units_on_board()}",
                       screen_coords.CURRENT_AMOUNT_OF_CHAMPIONS_ON_BOARD_LOC.get_coords(), 0, 0))
        # Create label for the max units amount of units we can have on the board.
        labels.append((f"{arena_functions.get_max_amount_of_units_on_board()}",
                       screen_coords.MAX_AMOUNT_OF_CHAMPIONS_ON_BOARD_LOC.get_coords(), 0, 0))
        # Create label for the item orbs.
        for item_orb_vec2 in arena_functions.get_center_position_of_item_orbs():
            labels.append((f"?", item_orb_vec2.get_coords(), 0, 0))
        self.message_queue.put(("LABEL", labels))

    def count_items_on_bench(self) -> int:
        """Returns the number of items on the bench."""
        item_amount = 0
        for i in self.items:
            if i is not None:
                item_amount += 1
        return item_amount

    def is_same_amount_or_more_items_on_bench(self, item_amount_at_start: int) -> bool:
        """
        Returns a boolean representing if the current amount of items on the bench
        is greater than or equal to the given amount.
        """
        i = self.count_items_on_bench()
        if i >= item_amount_at_start:
            print(f"    Started Item Amount: {item_amount_at_start}")
            print(f"      Current Item Amount: {i}")
            return True

    def check_if_we_should_spam_sparring_gloves(self) -> bool:
        """Checks if our health is at 15 or less and then calls the function to spam thief's gloves."""
        health: int = arena_functions.get_health()
        if health <= 15:
            print(f"  Health <= 15 - Health: {health}")
            for champ in self.board:
                if champ.completed_items == 0 and champ.current_building == 0:
                    if self.add_thiefs_gloves_to_champ(champ):
                        return True
        return False

    def check_if_we_should_spam_items_before_dying(self, index: int) -> bool:
        """Checks if our health is at 15 or less and then calls the function spam items before dying"""
        health: int = arena_functions.get_health()
        if health <= 15:
            print(f"    Health <= 15 - Health: {health}")
            self.add_item_to_champs_before_dying(index)
            return True
        return False

    def check_if_we_should_make_lucky_gloves(self) -> bool:
        """If we have the Lucky Gloves augment, place thief's gloves on a champion that doesn't build items."""
        if "Lucky Gloves" in self.augments:
            no_build_champ = self.get_random_final_comp_champ_on_board_with_no_build()
            if no_build_champ is not None:
                if self.add_thiefs_gloves_to_champ(no_build_champ):
                    return True
        return False

    def get_random_final_comp_champ_on_board_with_no_build(self) -> Champion | None:
        for champ in self.board:
            if champ.build is None:
                return champ
        return None

    def identify_champions_on_board(self):
        print("  Double-checking the champions on the board.")
        for index, board_space in enumerate(self.board):
            if isinstance(board_space, Champion):
                print(f"  [!]Board space: {board_space} at index: {index} is occupied by a unit,"
                      f" but we don't know which unit!")
                # print(f"       Board Space Occupied: {board_space}")
                # Right-click the unit to make the unit's info appear on the right side of the screen.
                # print(f"       Right-clicking the unit to make its info appear.")
                mk_functions.right_click(board_space.coords)
                mk_functions.press_s()
                # print(f"       Sleeping for 0.1 seconds.")
                sleep(0.1)
                champ_name: str = ocr.get_text(screenxy=screen_coords.SELECTED_UNIT_NAME_POS.get_coords(),
                                               scale=3, psm=13, whitelist=ocr.ALPHABET_WHITELIST)
                print(f"       Champ: {champ_name}")
                # print(f"       I hope the info box appeared because I already tried to grab the info.")
                champ_name = arena_functions.get_valid_champ(champ_name)
                # Confirm this is an actual unit that can be used
                if arena_functions.is_valid_champ(champ_name):
                    # Set default values if we don't want to use this champ in our comp.
                    items_to_build = []
                    final_comp = False
                    # If we actually plan on using this champ in our comp:
                    if champ_name in comps.COMP:
                        items_to_build = comps.COMP[champ_name]["items"].copy()
                        final_comp = comps.COMP[champ_name]["final_comp"]
                    # Create the Champion object.
                    self.board[index] = Champion(name=champ_name,
                                                 coords=screen_coords.BENCH_LOC[index].get_coords(
                                                 ),
                                                 build=items_to_build,
                                                 slot=index,
                                                 size=game_assets.CHAMPIONS[champ_name]["Board Size"],
                                                 final_comp=final_comp)

    def identify_champions_on_bench(self):
        print("  Double-checking the champions on the bench.")
        bench_occupied: list = arena_functions.bench_occupied_check()
        for index, bench_space in enumerate(self.bench):
            # check is this bench space is labeled "?"
            if bench_space is None and bench_occupied[index]:
                print(f"  [!]Bench space {index} is occupied by a unit, but we don't know which unit!")
                # print(f"       Bench Occupied: {bench_occupied[index]}")
                # Right-click the unit to make the unit's info appear on the right side of the screen.
                # print(f"       Right-clicking the unit to make its info appear.")
                mk_functions.right_click(screen_coords.BENCH_LOC[index].get_coords())
                mk_functions.press_s()
                # print(f"       Sleeping for 0.1 seconds.")
                sleep(0.1)
                champ_name: str = ocr.get_text(screenxy=screen_coords.SELECTED_UNIT_NAME_POS.get_coords(),
                                               scale=3, psm=13, whitelist=ocr.ALPHABET_WHITELIST)
                print(f"       Champ: {champ_name}")
                # print(f"       I hope the info box appeared because I already tried to grab the info.")
                champ_name = arena_functions.get_valid_champ(champ_name)
                # Confirm this is an actual unit that can be used
                if arena_functions.is_valid_champ(champ_name):
                    # Set default values if we don't want to use this champ in our comp.
                    items_to_build = []
                    final_comp = False
                    # If we actually plan on using this champ in our comp:
                    if champ_name in comps.COMP:
                        items_to_build = comps.COMP[champ_name]["items"].copy()
                        final_comp = comps.COMP[champ_name]["final_comp"]
                    # Create the Champion object.
                    self.bench[index] = Champion(name=champ_name,
                                                 coords=screen_coords.BENCH_LOC[index].get_coords(
                                                 ),
                                                 build=items_to_build,
                                                 slot=index,
                                                 size=game_assets.CHAMPIONS[champ_name]["Board Size"],
                                                 final_comp=final_comp)
