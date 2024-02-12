"""
Handles the board / bench state inside of the game and
other variables used by the bot to make decisions
"""
from time import sleep
from typing import List, Optional, Union

import arena_functions
import game_assets
import game_functions
import mk_functions
import ocr
import screen_coords
from champion import Champion
from comps import CompsManager


class Arena:
    """Arena class that handles game logic such as board and bench state"""

    # pylint: disable=too-many-instance-attributes,too-many-public-methods,fixme
    def __init__(self, message_queue, comps_manager: CompsManager) -> None:
        self.comps_manager = comps_manager
        self.comps_manager.select_next_comp()
        self.message_queue = message_queue
        self.board_size = 0
        self.bench: List[Optional[Union[Champion, str]]] = [None] * 9
        self.anvil_free: List[bool] = [False] * 9
        self.board: List[Optional[Champion]] = [None] * 28
        self.board_unknown: List[Optional[str]] = []
        self.unknown_slots: List[int] = comps_manager.get_unknown_slots()
        self.champs_to_buy: dict = comps_manager.champions_to_buy()
        self.board_names: List[str] = []
        self.items: List[Optional[str]] = [None] * 10
        self.final_comp = False
        self.level = 0
        self.augment_roll = True
        self.tacticians_crown = True
        self.spam_roll = False
        self.active_portal: str = ""
        self.radiant_item = False
        self.have_headliner = False

    def portal_vote(self) -> None:
        """Picks a portal based on a comp-specific/user-defined portal list
        or defaults to the first portal that is not in the AVOID list"""
        while True:
            sleep(1)
            portals: list = []
            for coords in screen_coords.PORTALS_POS:
                portal: str = ocr.get_text(
                    screenxy=coords.get_coords(), scale=3, psm=7
                )
                portals.append(portal)
            print(portals)
            if len(portals) == 3 and "" not in portals:
                break

        for potential in game_assets.PORTALS:
            for portal in portals:
                if potential in portal:
                    print(f"  Choosing portal: {portal}")
                    mk_functions.left_click(
                        screen_coords.PORTALS_LOC[portals.index(portal)].get_coords()
                    )
                    sleep(0.7)
                    mk_functions.left_click(
                        screen_coords.PORTALS_VOTES[portals.index(portal)].get_coords()
                    )
                    return

        print(
            "  [!] No priority or backup portal found, undefined behavior may occur for the rest of the round"
        )

        for portal in portals:
            found = False
            for potential in game_assets.AVOID_PORTALS:
                if potential in portal:
                    found = True
                    break
            if not found:
                mk_functions.left_click(screen_coords.PORTALS_LOC[portals.index(portal)].get_coords())
                sleep(0.7)
                mk_functions.left_click(screen_coords.PORTALS_VOTES[portals.index(portal)].get_coords())
                return
        mk_functions.left_click(screen_coords.PORTALS_LOC[0].get_coords())

    def portal_augment(self) -> None:
        """Check the region augment and set flags accordingly"""
        mk_functions.right_click(screen_coords.PORTAL_AUGMENT_LOC.get_coords())
        sleep(1)
        region = ocr.get_text(
            screenxy=screen_coords.PORTAL_AUGMENT_POS.get_coords(), scale=3, psm=7
        )
        self.active_portal = region

        augment_flags = {
            "Artifact Anvil": "Clearing Anvils at round 1-3",
            "Completed Anvil": "Clearing Anvils at round 1-3",
            "Component Anvils": "Clearing Anvils at round 1-3",
            "Support Anvil": "Clearing Anvils at round 1-3",
            "Tome of Traits": "Clearing Anvils at round 1-3",
            "Radiant Item": "Clearing Radiant Item shop at 3-7",
            "Tactician’s Crown": "Checking for Tactician’s Crown"
        }

        augment_name = next((name for name in augment_flags if name in region), None)

        if augment_name:
            flag = augment_flags[augment_name]
            print(f"  Region Augment: {region}. {flag}")
            if augment_name == "Radiant Item":
                self.radiant_item = True
        else:
            print(f"  Region Augment: {region}")

    def fix_bench_state(self) -> None:
        """Iterate through the bench, fix invalid slots, and handle unknown champions"""
        bench_occupied: list = arena_functions.bench_occupied_check()
        for index, slot in enumerate(self.bench):
            if slot is None and bench_occupied[index]:
                # ocr + right click
                mk_functions.right_click(screen_coords.BENCH_LOC[index].get_coords())
                champ_name: str = ocr.get_text(
                    screenxy=screen_coords.PANEL_NAME_LOC.get_coords(),
                    scale=3,
                    psm=7,
                    whitelist=ocr.ALPHABET_WHITELIST
                    + ocr.SPACE_WHITELIST
                    + ocr.APOSTROPHE_WHITELIST,
                )
                if self.champs_to_buy.get(champ_name, 0) > 0:
                    print(
                        f"  The unknown champion {champ_name} exists in comps, keeping it."
                    )
                    self.bench[index] = Champion(
                        name=champ_name,
                        coords=screen_coords.BENCH_LOC[index].get_coords(),
                        build=self.comps_manager.current_comp()[1][champ_name][
                            "items"
                        ].copy(),
                        slot=index,
                        size=self.comps_manager.champions[champ_name]["Board Size"],
                        final_comp=self.comps_manager.current_comp()[1][champ_name][
                            "final_comp"
                        ],
                    )
                    self.champs_to_buy[champ_name] -= 1
                else:
                    self.bench[index] = "?"
                continue
            if isinstance(slot, str) and not bench_occupied[index]:
                self.bench[index] = None
                continue
            if isinstance(slot, Champion) and not bench_occupied[index]:
                self.bench[index] = None

    def bought_champion(self, name: str, slot: int) -> None:
        """Purchase a champion and create a Champion instance"""
        self.bench[slot] = Champion(
            name=name,
            coords=screen_coords.BENCH_LOC[slot].get_coords(),
            build=self.comps_manager.current_comp()[1][name]["items"].copy(),
            slot=slot,
            size=self.comps_manager.champions[name]["Board Size"],
            final_comp=self.comps_manager.current_comp()[1][name]["final_comp"],
        )
        mk_functions.move_mouse(screen_coords.DEFAULT_LOC.get_coords())
        sleep(0.5)
        self.fix_bench_state()

    def have_champion(self) -> Champion | None:
        """Check if there is a champion on the bench that is not on the board"""
        return next(
            (
                champion
                for champion in self.bench
                if isinstance(champion, Champion)
                and champion.name not in self.board_names
            ),
            None,
        )

    def move_known(self, champion: Champion) -> None:
        """Moves a known champion to the board"""
        print(f"  Moving {champion.name} to board")
        destination: tuple = screen_coords.BOARD_LOC[
            self.comps_manager.current_comp()[1][champion.name]["board_position"]
        ].get_coords()
        mk_functions.left_click(champion.coords)
        sleep(0.18)
        mk_functions.left_click(destination)
        champion.coords = destination
        self.board.append(champion)
        self.board_names.append(champion.name)
        self.bench[champion.index] = None
        champion.index = self.comps_manager.current_comp()[1][champion.name][
            "board_position"
        ]
        self.board_size += champion.size

    def move_unknown(self) -> None:
        """Moves unknown champion to the board"""
        for index, champion in enumerate(self.bench):
            if isinstance(champion, str):
                print(f"  Moving {champion} to board")
                mk_functions.left_click(screen_coords.BENCH_LOC[index].get_coords())
                sleep(0.1)
                mk_functions.left_click(
                    screen_coords.BOARD_LOC[
                        self.unknown_slots[len(self.board_unknown)]
                    ].get_coords()
                )
                self.bench[index] = None
                self.board_unknown.append(champion)
                self.board_size += 1
                return

    def sell_bench(self) -> None:
        """Sells all of the champions on the bench"""
        for index, name in enumerate(self.bench):
            print(f"  Selling {name}")
            mk_functions.press_e(screen_coords.BENCH_LOC[index].get_coords())
            self.bench[index] = None

    def unknown_in_bench(self) -> bool:
        """Sells all of the unknown champions on the bench"""
        return any(isinstance(slot, str) for slot in self.bench)

    def move_champions(self) -> None:
        """Moves champions to the board"""
        self.level: int = arena_functions.get_level_via_https_request()
        while self.level > self.board_size:
            champion: Champion | None = self.have_champion()
            if champion is not None:
                self.move_known(champion)
            elif self.unknown_in_bench():
                self.move_unknown()
            else:
                bought_unknown = False
                shop: list = arena_functions.get_shop(self.comps_manager)
                for champion in shop:
                    gold: int = arena_functions.get_gold()
                    valid_champ: bool = (
                        champion[1] in self.comps_manager.champions
                        and self.comps_manager.champion_gold_cost(champion[1]) <= gold
                        and self.comps_manager.champion_board_size(champion[1]) == 1
                        and self.champs_to_buy.get(champion[1], -1) < 0
                        and champion[1] not in self.board_unknown
                    )
                    if valid_champ:
                        none_slot: int = arena_functions.empty_slot()
                        mk_functions.left_click(
                            screen_coords.BUY_LOC[champion[0]].get_coords()
                        )
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
        """Replaces unknown champion"""
        champion: Champion | None = self.have_champion()
        if len(self.board_unknown) > 0 and champion is not None:
            mk_functions.press_e(
                screen_coords.BOARD_LOC[
                    self.unknown_slots[len(self.board_unknown) - 1]
                ].get_coords()
            )
            self.board_unknown.pop()
            self.board_size -= 1
            self.move_known(champion)

    def bench_cleanup(self) -> None:
        """Sells unknown champions"""
        self.anvil_free: list[bool] = [False] * 9
        for index, champion in enumerate(self.bench):
            if champion == "?" or isinstance(champion, str):
                print("  Selling unknown champion")
                mk_functions.press_e(screen_coords.BENCH_LOC[index].get_coords())
                self.bench[index] = None
                self.anvil_free[index] = True
            elif isinstance(champion, Champion):
                if (
                    self.champs_to_buy.get(champion.name, -1) < 0
                    and champion.name in self.board_names
                ):
                    print("  Selling unknown champion")
                    mk_functions.press_e(screen_coords.BENCH_LOC[index].get_coords())
                    self.bench[index] = None
                    self.anvil_free[index] = True

    def clear_anvil(self) -> None:
        """Clears anvil on the bench, selects middle item"""
        for index, champion in enumerate(self.bench):
            if champion is None and not self.anvil_free[index]:
                mk_functions.press_e(screen_coords.BENCH_LOC[index].get_coords())
        sleep(0.8)
        anvil_msg: str = ocr.get_text(
            screenxy=screen_coords.ANVIL_MSG_POS.get_coords(), scale=3, psm=7
        )
        if anvil_msg == "Choose One":
            print("clearing anvil")
            mk_functions.left_click(screen_coords.BUY_LOC[2].get_coords())
        sleep(1)

    def place_items(self) -> None:
        """Iterates through items and tries to add them to champion"""
        self.items = arena_functions.get_items()
        print(f"  Items: {list(filter(None.__ne__, self.items))}")
        for index, _ in enumerate(self.items):
            if self.items[index] is not None:
                self.add_item_to_champs(index)

    def add_item_to_champs(self, item_index: int) -> None:
        """Iterates through champions in the board and checks if the champion needs items"""
        for champ in self.board:
            if isinstance(champ, Champion):
                if self.items[item_index] is not None:
                    if champ.does_need_items():
                        self.add_item_to_champ(item_index, champ)
                    if len(champ.build) == 0:
                        if champ.has_available_item_slots():
                            item = self.items[item_index]
                            gloves = [
                                "ThiefsGloves",
                                "BlacksmithsGloves",
                                "RascalsGloves",
                            ]
                            if (
                                self.other_instances_dont_need_item(item)
                                and (
                                    (item not in gloves)
                                    or (len(champ.completed_items) == 0)
                                )
                                and item
                                in set(game_assets.CRAFTABLE_ITEMS_DICT.values()).union(
                                    game_assets.RADIANT_ITEMS_DICT.values(),
                                    game_assets.FORCED_ITEMS,
                                )
                            ):
                                mk_functions.left_click(
                                    screen_coords.ITEM_POS[item_index][0].get_coords()
                                )
                                mk_functions.left_click(champ.coords)
                                if "TacticiansCrown" in item and self.tacticians_crown:
                                    print(
                                        "  Tacticians Crown on bench, adding extra slot to board"
                                    )
                                    self.board_size -= 1
                                    #print(f"self.board_size = {self.board_size}")
                                    self.move_champions()
                                print(
                                    f"  Placed {item} on {champ.name} to free up space"
                                )
                                if item in gloves and champ.max_item_slots == 3:
                                    champ.completed_items = [
                                        item
                                    ] * 3  # Set to 3 completed_items
                                    #print(
                                    #    f"  {champ.name} completed items: {champ.completed_items}"
                                    #    f"  {champ.name} item slots number: {champ.max_item_slots}"
                                    #)
                                champ.completed_items.append(item)
                                self.items[self.items.index(item)] = None
                                #print(
                                #    f"  {champ.name} completed items: {champ.completed_items}"
                                #)

    def item_needed_on_champions(self, champions, item):
        """Checks if the item is needed on any champions"""
        return any(
            champ is not None
            and getattr(champ, "build", None) is not None
            and item in champ.build
            for champ in champions
        )

    def other_instances_dont_need_item(self, item):
        """Checks if any other instance needs the item"""
        item_needed_on_board = self.item_needed_on_champions(self.board, item)
        item_needed_on_bench = self.item_needed_on_champions(self.bench, item)
        item_needed_on_champions_to_buy = any(
            item
            in self.comps_manager.current_comp()[1].get(champion, {"items": []})[
                "items"
            ]
            for champion in self.champs_to_buy
        )
        return not (
            item_needed_on_board
            or item_needed_on_bench
            or item_needed_on_champions_to_buy
        )

    def add_item_to_champ(self, item_index: int, champ: Champion) -> None:
        """Takes item index and champ and applies the item"""
        item = self.items[item_index]

        if item in game_assets.CRAFTABLE_ITEMS_DICT:
            if item in champ.build:
                mk_functions.left_click(
                    screen_coords.ITEM_POS[item_index][0].get_coords()
                )
                mk_functions.left_click(champ.coords)
                print(f"  Placed {item} on {champ.name}")
                champ.completed_items.append(item)
                champ.build.remove(item)
                self.items[self.items.index(item)] = None
                #print(
                #    f"1  {champ.name} Completed Items: {champ.completed_items}\n"
                #    f"1  {champ.name} Build: {champ.build}"
                #)
        elif len(champ.current_building) == 0:
            item_to_move = None
            for build_item in champ.build:
                build_item_components = list(
                    game_assets.CRAFTABLE_ITEMS_DICT.get(build_item, [])
                )
                if item in build_item_components:
                    item_to_move = item
                    build_item_components.remove(item_to_move)
                    champ.current_building.append(
                        (build_item, build_item_components[0])
                    )
                    champ.build.remove(build_item)
            if item_to_move is not None:
                mk_functions.left_click(
                    screen_coords.ITEM_POS[item_index][0].get_coords()
                )
                mk_functions.left_click(champ.coords)
                print(f"  Placed {item} on {champ.name}")
                self.items[self.items.index(item)] = None
                #print(
                #    f"2  {champ.name} Currently Building: {champ.current_building[0][0]}\n"
                #    f"2  {champ.name} Completed Items: {champ.completed_items}\n"
                #    f"2  {champ.name} Build: {champ.build}"
                #)
        else:
            for build_item in champ.current_building:
                if item == build_item[1]:
                    mk_functions.left_click(
                        screen_coords.ITEM_POS[item_index][0].get_coords()
                    )
                    mk_functions.left_click(champ.coords)
                    champ.completed_items.append(build_item[0])
                    champ.current_building.clear()
                    self.items[self.items.index(item)] = None
                    print(f"  Placed {item} on {champ.name}")
                    print(f"  Completed {build_item[0]} on {champ.name}")
                    #print(
                    #    f"3  {champ.name} Completed Items: {build_item[0]}\n"
                    #    f"3  {champ.name} Build: {champ.build}"
                    #)
                    return

    def fix_unknown(self) -> None:
        """Checks if the item passed in arg one is valid"""
        sleep(0.25)
        mk_functions.press_e(
            screen_coords.BOARD_LOC[self.unknown_slots[0]].get_coords()
        )
        if len(self.board_unknown) > 0:
            self.board_unknown.pop(0)
            self.board_size -= 1

    def remove_champion(self, champion: Champion) -> None:
        """Remove a champion from the board and update relevant attributes"""
        for index, slot in enumerate(self.bench):
            if isinstance(slot, Champion) and slot.name == champion.name:
                mk_functions.press_e(slot.coords)
                self.bench[index] = None

        # Remove all instances of champion in champs_to_buy
        if champion.name in self.champs_to_buy:
            self.champs_to_buy.pop(champion.name)

        mk_functions.press_e(champion.coords)
        self.board_names.remove(champion.name)
        self.board_size -= champion.size
        self.board.remove(champion)

    def final_comp_check(self) -> None:
        """Check the board and replace champions not in the final composition"""
        for slot in self.bench:
            if (
                isinstance(slot, Champion)
                and slot.final_comp
                and slot.name not in self.board_names
            ):
                for champion in self.board:
                    if isinstance(champion, Champion):
                        if not champion.final_comp and champion.size == slot.size:
                            print(f"  Replacing {champion.name} with {slot.name}")
                            self.remove_champion(champion)
                            self.move_known(slot)
                            break

    def tacticians_crown_check(self) -> None:
        """Checks if the item from carousel is tacticians crown"""
        mk_functions.move_mouse(screen_coords.ITEM_POS[0][0].get_coords())
        sleep(0.5)
        item: str = ocr.get_text(
            screenxy=screen_coords.ITEM_POS[0][1].get_coords(),
            scale=3,
            psm=7,
            whitelist=ocr.ALPHABET_WHITELIST,
        )
        item: str = arena_functions.valid_item(item)
        try:
            if "TacticiansCrown" in item:
                print("  Tacticians Crown on bench, adding extra slot to board")
                self.board_size -= 1
                self.tacticians_crown = False
            else:
                print(f"{item} is not TacticiansCrown")
        except TypeError:
            print("  Item could not be read for Tacticians Check")

    def spend_gold(self, speedy=False) -> None:
        """Spend gold to buy champions and XP"""
        first_run = True
        min_gold = 100 if speedy else (24 if self.spam_roll else 56)
        while first_run or arena_functions.get_gold() >= min_gold:
            if not first_run:
                current_level = arena_functions.get_level_via_https_request()
                if current_level != 10:
                    mk_functions.buy_xp()
                    print("  Purchasing XP")
                mk_functions.reroll()
                print("  Rerolling shop")
            shop: list = arena_functions.get_shop(self.comps_manager)
            print(f"  Shop: {shop}")
            for champion in shop:
                if (
                    self.champs_to_buy.get(champion[1], -1) >= 0
                    and arena_functions.get_gold()
                    - self.comps_manager.champions[champion[1]]["Gold"]
                    >= 0
                ):
                    if (
                        champion[0] != 4 or not arena_functions.check_headliner()
                    ) and self.champs_to_buy.get(champion[1], -1) > 0:
                        self.buy_champion(champion, 1)
                    elif (
                        champion[0] == 4
                        and (
                            arena_functions.check_headliner()
                            & self.comps_manager.get_headliner_tag(champion[1])
                            != 0
                        )
                        and not self.have_headliner
                        and self.comps_manager.current_comp()[1][champion[1]][
                            "final_comp"
                        ]
                        and arena_functions.get_gold()
                        - self.comps_manager.champions[champion[1]]["Gold"] * 3
                        >= 0
                    ):
                        self.buy_headliner(champion[1])
            first_run = False

    def buy_headliner(self, champion: str) -> None:
        """Buy headliner and replace the normal one if the level is not equal to 3"""
        if self.comps_manager.current_comp()[1].get(champion, {}).get("level", 0) >= 3:
            self.buy_champion([4, champion], 3)
            self.have_headliner = True
            return

        champion_found = self.replace_champion_with_headliner_on_board(champion)
        if not champion_found:
            champion_found = self.replace_champion_with_headliner_on_bench(champion)

        if not champion_found:
            print(f"No matching champion found on the board or bench for {champion}")
            self.buy_champion([4, champion], 3)

        self.have_headliner = True

    def replace_champion_with_headliner_on_board(self, champion: str) -> bool:
        """Replace champion on the board with the headliner"""
        for champ in self.board:
            if champ and champ.name == champion:
                headliner_trait = self.comps_manager.current_comp()[1].get(champion, {}).get("headliner", "")
                print(f"  Replaced {champion} with Headliner: {champion} ({headliner_trait})")
                self.remove_champion(champ)
                self.buy_champion([4, champion], 0)
                for newchamp in self.bench:
                    if isinstance(newchamp, Champion) and newchamp.name == champion:
                        self.move_known(newchamp)
                        self.place_items()
                return True
        return False

    def replace_champion_with_headliner_on_bench(self, champion: str) -> bool:
        """Replace champion on the bench with the headliner"""
        for index, slot in enumerate(self.bench):
            if isinstance(slot, Champion) and slot.name == champion:
                mk_functions.press_e(slot.coords)
                self.bench[index] = None
                self.buy_champion([4, champion], 3)
                return True
        return False

    def buy_champion(self, champion, quantity) -> None:
        """Buy champion in shop"""
        none_slot: int = arena_functions.empty_slot()
        if none_slot != -1:
            buy_coords = screen_coords.BUY_LOC[champion[0]].get_coords()
            mk_functions.left_click(buy_coords)
            print(f"Purchased {champion[1]}")
            self.bought_champion(champion[1], none_slot)
            if champion[1] in self.champs_to_buy:
                self.champs_to_buy[champion[1]] -= quantity
        else:
            print(f"Board is full but want {champion[1]}")
            buy_coords = screen_coords.BUY_LOC[champion[0]].get_coords()
            mk_functions.left_click(buy_coords)
            game_functions.default_pos()
            sleep(0.5)
            self.fix_bench_state()
            none_slot = arena_functions.empty_slot()
            sleep(0.5)
            if none_slot != -1:
                print(f"Purchased {champion[1]}")
                if champion[1] in self.champs_to_buy:
                    self.champs_to_buy[champion[1]] -= quantity

    def buy_xp_round(self) -> None:
        """Buy XP if gold is equal to or over 4"""
        if arena_functions.get_gold() >= 4:
            mk_functions.buy_xp()

    def load_aguments(self):
        """Augments from lolchess.gg"""
        return self.comps_manager.current_comp()[2]

    def pick_augment(self) -> None:
        """Picks an augment based on a comp-specific/user-defined augment list
        or defaults to the first augment that is not in the AVOID list"""
        while True:
            sleep(1)
            augments: list = []
            comp_augments = self.load_aguments()
            for coords in screen_coords.AUGMENT_POS:
                augment: str = ocr.get_text(
                    screenxy=coords.get_coords(), scale=3, psm=7
                )
                augments.append(augment)
            print(augments)
            if len(augments) == 3 and "" not in augments:
                break

        for potential in comp_augments + game_assets.AUGMENTS:
            for augment in augments:
                if potential in augment:
                    print(f"  Choosing augment: {augment}")
                    mk_functions.left_click(
                        screen_coords.AUGMENT_LOC[augments.index(augment)].get_coords()
                    )
                    return

        if self.augment_roll:
            print("  Rolling for augment")
            for i in range(0, 3):
                mk_functions.left_click(screen_coords.AUGMENT_ROLL[i].get_coords())
            self.augment_roll = False
            self.pick_augment()
            return

        print(
            "  [!] No priority or backup augment found, undefined behavior may occur for the rest of the round"
        )

        for augment in augments:
            found = False
            for potential in game_assets.AVOID_AUGMENTS:
                if potential in augment:
                    found = True
                    break
                if not found:
                    mk_functions.left_click(
                    screen_coords.AUGMENT_LOC[augments.index(augment)].get_coords()
                )
                    return
            mk_functions.left_click(screen_coords.AUGMENT_LOC[0].get_coords())

    def check_health(self) -> None:
        """Check the current health and activate spam roll if health is 30 or below"""
        health: int = arena_functions.get_health()
        if health > 0:
            print(f"  Health: {health}")
            if not self.spam_roll and health <= 30:
                print("    Health under 30, spam roll activated")
                self.spam_roll = True
        else:
            print("  Health check failed")

    def get_label(self) -> None:
        """Gets labels used to display champion name UI on window"""
        labels = [
            (f"{slot.name}", slot.coords)
            for slot in self.bench
            if isinstance(slot, Champion)
        ]

        for slot in self.board:
            if isinstance(slot, Champion):
                labels.append((f"{slot.name}", slot.coords))

        labels.extend(
            (slot, screen_coords.BOARD_LOC[self.unknown_slots[index]].get_coords())
            for index, slot in enumerate(self.board_unknown)
        )
        self.message_queue.put(("LABEL", labels))
